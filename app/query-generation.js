// 词条模型调用由 Actions / 本地后端执行，统一读取 SUMMARY_*。
window.DPRQueryGeneration = (function () {
  const WORKFLOW = 'generate-query.yml';
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  const request = async (url, options = {}, timeoutMs = 20000) => {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetch(url, { ...options, signal: controller.signal });
      const data = response.status === 204 ? null : await response.json().catch(() => null);
      if (!response.ok) {
        const error = new Error(`请求失败（HTTP ${response.status}）`);
        error.status = response.status;
        // 只信任本地后端的结构化错误；不展示第三方原始响应。
        if (data && typeof data.error === 'string') error.message = data.error;
        throw error;
      }
      return data;
    } catch (error) {
      if (error.name === 'AbortError') throw new Error('请求超时，请检查网络后重试。');
      throw error;
    } finally {
      clearTimeout(timer);
    }
  };

  const generate = async (prompt, onProgress = () => {}) => {
    const runner = window.DPRWorkflowRunner;
    if (!runner || !runner.getQueryGenerationContext) {
      throw new Error('词条生成组件尚未加载，请刷新页面后重试。');
    }
    if (!prompt || new TextEncoder().encode(prompt).length > 24000) {
      throw new Error('检索需求为空或过长，请缩短后重试。');
    }
    const context = await runner.getQueryGenerationContext();
    if (context.localUrl) {
      onProgress('正在生成候选，请稍候…');
      let data;
      try {
        data = await request(context.localUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt }),
        }, 300000);
      } catch (error) {
        if (error.status === 404) throw new Error('本地后端版本过旧，请更新并重启 src/local_debug_server.py。');
        throw error;
      }
      if (!data || !data.ok || !data.candidates) throw new Error(data?.error || '未收到生成结果。');
      return data.candidates;
    }

    const { owner, repo, defaultBranch, token } = context;
    const api = `https://api.github.com/repos/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}`;
    const headers = {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    };
    const requestId = crypto.randomUUID();
    const name = `dpr-query-${requestId}`;
    const actionsUrl = `https://github.com/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}/actions/workflows/${WORKFLOW}`;
    onProgress('正在提交生成任务…');
    try {
      // 请求中只发送检索需求；模型 Key、地址和模型名都由 Actions Secrets 提供。
      await request(`${api}/actions/workflows/${WORKFLOW}/dispatches`, {
        method: 'POST',
        headers: { ...headers, 'Content-Type': 'application/json' },
        body: JSON.stringify({ ref: defaultBranch, inputs: { request_id: requestId, prompt } }),
      });
    } catch (error) {
      if (error.status === 404) throw new Error('未找到生成工作流或无仓库访问权限。请将 generate-query.yml 同步到仓库默认分支，并检查 GitHub Token。');
      if ([401, 403].includes(error.status)) throw new Error('GitHub Token 无权触发生成，请检查仓库的 Actions 读写权限。');
      throw new Error(`生成任务提交未确认，请先查看 ${actionsUrl} 是否已启动，避免重复生成。`);
    }

    const deadline = Date.now() + 10 * 60 * 1000;
    let runId = null;
    let failures = 0;
    let lastStatus = '';
    let resultDeadline = null;
    let completedConclusion = null;
    const missingResultError = () => new Error(`生成任务结束但未返回候选（${completedConclusion}），结果同步等待已超时。请查看 https://github.com/${owner}/${repo}/actions/runs/${runId}`);
    while (Date.now() < (resultDeadline ?? deadline)) {
      await sleep(5000);
      let run;
      try {
        if (runId) {
          run = await request(`${api}/actions/runs/${runId}`, { headers });
        } else {
          const data = await request(`${api}/actions/workflows/${WORKFLOW}/runs?event=workflow_dispatch&per_page=100`, { headers });
          run = (data?.workflow_runs || []).find((item) => item.display_title === name);
          if (run) runId = run.id;
        }
        if (run && run.status === 'completed') {
          // 完成后的结果可见性等待单独计时，不被前面的排队时间挤掉。
          if (resultDeadline === null) resultDeadline = Date.now() + 60000;
          completedConclusion = run.conclusion;
          const checks = await request(`${api}/commits/${encodeURIComponent(run.head_sha)}/check-runs?check_name=${encodeURIComponent(name)}&filter=all&per_page=100`, { headers });
          const check = (checks?.check_runs || []).find((item) => (
            item.name === name && item.external_id === requestId
            && item.head_sha === run.head_sha && item.status === 'completed'
          ));
          if (check) {
            let result;
            try { result = JSON.parse(check.output?.text || '{}'); }
            catch { throw new Error('生成结果格式无效，请查看本次运行。'); }
            if (!result || result.request_id !== requestId) throw new Error('生成结果编号不匹配，请重试。');
            // GitHub 会改写 details_url，不能用展示链接认领结果。
            // 旧 Check 没有 run_id，仍按名称、请求编号和提交 SHA 读取。
            if (result.run_id !== undefined && String(result.run_id) !== String(runId)) throw new Error('生成结果运行编号不匹配，请查看本次运行。');
            if (!result.ok || check.conclusion !== 'success') throw new Error(result.error || '模型生成失败，请查看本次运行。');
            if (!result.candidates) throw new Error('未收到候选词条，请重试。');
            return result.candidates;
          }
          if (Date.now() >= resultDeadline) throw missingResultError();
        }
        failures = 0;
      } catch (error) {
        // 只重试读取网络错误和服务错误，不重复派发、不重试确定的任务失败。
        if ((error instanceof TypeError || error.status >= 500 || /请求超时/.test(error.message)) && ++failures <= 3) continue;
        if ([401, 403].includes(error.status)) throw new Error('无法读取生成结果，请检查 GitHub Token 的 Actions 和 Checks 读取权限。');
        throw error;
      }
      const status = resultDeadline !== null
        ? '任务已结束，正在同步候选结果，请保持页面打开…'
        : run?.status === 'in_progress' ? '正在生成候选，请保持页面打开…' : '生成任务排队中，请保持页面打开…';
      if (status !== lastStatus) onProgress(status);
      lastStatus = status;
    }
    if (resultDeadline !== null) throw missingResultError();
    throw new Error(`等待生成结果超时。任务可能仍在运行，请先查看 ${runId ? `https://github.com/${owner}/${repo}/actions/runs/${runId}` : actionsUrl}`);
  };

  return { generate };
})();
