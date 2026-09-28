const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const requestId = '12345678-1234-1234-1234-123456789abc';
const name = `dpr-query-${requestId}`;
const candidates = { keywords: [{ keyword: 'agent memory', query: 'agent memory' }], intent_queries: [] };
const completed = { id: 42, head_sha: 'abc123', display_title: name, status: 'completed', conclusion: 'success' };
const resultCheck = (result = { ok: true, request_id: requestId, run_id: '42', candidates }) => ({
  name, external_id: requestId, head_sha: completed.head_sha, status: 'completed',
  details_url: 'https://github.com/tester/papers/actions/runs/42',
  conclusion: result.ok ? 'success' : 'failure', output: { text: JSON.stringify(result) },
});
const response = (data, status = 200) => ({ ok: status >= 200 && status < 300, status, json: async () => data });

function harness(fetcher, context = { owner: 'tester', repo: 'papers', token: 'test-github-token', defaultBranch: 'main' }) {
  let now = 0;
  const calls = [];
  const sandbox = {
    window: { DPRWorkflowRunner: { getQueryGenerationContext: async () => context } },
    TextEncoder, AbortController, TypeError,
    crypto: { randomUUID: () => requestId },
    Date: { now: () => now },
    setTimeout: (fn, ms) => { if (ms === 5000) { now += ms; queueMicrotask(fn); } return 1; },
    clearTimeout() {},
    fetch: async (url, opts) => { calls.push({ url, opts }); return fetcher(url, opts, calls); },
  };
  vm.runInNewContext(fs.readFileSync('app/query-generation.js', 'utf8'), sandbox);
  return { generate: sandbox.window.DPRQueryGeneration.generate, calls, elapsed: () => now };
}

function runFetcher(checks, run = completed) {
  return async (url) => {
    if (url.endsWith('/dispatches')) return response(null, 204);
    if (url.includes('/runs?')) return response({ workflow_runs: [run] });
    if (url.endsWith('/runs/42')) return response(run);
    assert.match(url, /check-runs\?/);
    return response({ check_runs: typeof checks === 'function' ? checks() : checks });
  };
}

async function main() {
  for (const details_url of [null, '', 'https://github.com/tester/papers/runs/999']) {
    const rewritten = harness(runFetcher([{ ...resultCheck(), details_url }]));
    assert.deepEqual(JSON.parse(JSON.stringify(await rewritten.generate('retrieval JSON'))), candidates);
  }

  // Existing results created before run_id was added remain readable.
  const legacy = harness(runFetcher([{ ...resultCheck({ ok: true, request_id: requestId, candidates }), details_url: null }]));
  assert.deepEqual(JSON.parse(JSON.stringify(await legacy.generate('retrieval JSON'))), candidates);

  let polls = 0;
  const h = harness(async (url, opts) => {
    assert.ok(url.startsWith('https://api.github.com/repos/tester/papers/'));
    if (url.endsWith('/dispatches')) {
      const input = JSON.parse(opts.body);
      assert.deepEqual(input, { ref: 'main', inputs: { request_id: requestId, prompt: 'retrieval JSON' } });
      return response(null, 204);
    }
    if (url.includes('/runs?')) {
      polls++;
      // Ignore unrelated concurrent requests and wait for this exact request.
      return response({ workflow_runs: polls === 1 ? [{ ...completed, display_title: 'another-request' }] : [completed] });
    }
    assert.match(url, /commits\/abc123\/check-runs\?check_name=dpr-query-/);
    return response({ check_runs: [{ ...resultCheck(), external_id: 'wrong-request' }, resultCheck()] });
  });
  const progress = [];
  assert.deepEqual(JSON.parse(JSON.stringify(await h.generate('retrieval JSON', (s) => progress.push(s)))), candidates);
  assert.equal(h.calls.filter((x) => x.opts.method === 'POST').length, 1);
  assert.ok(progress.some((s) => s.includes('排队')));

  const local = harness(async (url, opts) => {
    assert.equal(url, 'http://127.0.0.1:8567/api/local/query-candidates');
    assert.deepEqual(JSON.parse(opts.body), { prompt: 'retrieval JSON' });
    assert.equal(opts.headers.Authorization, undefined);
    return response({ ok: true, candidates });
  }, { localUrl: 'http://127.0.0.1:8567/api/local/query-candidates' });
  assert.deepEqual(await local.generate('retrieval JSON'), candidates);

  for (const [status, pattern] of [[404, /generate-query.yml/], [403, /Actions 读写权限/]]) {
    const failed = harness(async () => response({}, status));
    await assert.rejects(failed.generate('retrieval JSON'), pattern);
    assert.equal(failed.calls.length, 1);
  }

  const modelFailure = harness(async (url) => {
    if (url.endsWith('/dispatches')) return response(null, 204);
    if (url.includes('/runs?')) return response({ workflow_runs: [{ ...completed, conclusion: 'failure' }] });
    return response({ check_runs: [resultCheck({ ok: false, request_id: requestId, error: '请配置 SUMMARY_API_KEY' })] });
  });
  await assert.rejects(modelFailure.generate('retrieval JSON'), /SUMMARY_API_KEY/);

  let networkCalls = 0;
  const interrupted = harness(async (url) => {
    if (url.endsWith('/dispatches')) return response(null, 204);
    if (++networkCalls <= 2) throw new TypeError('Failed to fetch');
    if (url.includes('/runs?')) return response({ workflow_runs: [completed] });
    return response({ check_runs: [resultCheck()] });
  });
  assert.deepEqual(JSON.parse(JSON.stringify(await interrupted.generate('retrieval JSON'))), candidates);
  assert.equal(interrupted.calls.filter((x) => x.opts.method === 'POST').length, 1);

  const timeout = harness(async (url) => url.endsWith('/dispatches') ? response(null, 204) : response({ workflow_runs: [] }));
  await assert.rejects(timeout.generate('retrieval JSON'), /等待生成结果超时/);
  assert.equal(timeout.calls.filter((x) => x.opts.method === 'POST').length, 1);

  const wrongRun = harness(runFetcher([resultCheck({ ok: true, request_id: requestId, run_id: '41', candidates })]));
  await assert.rejects(wrongRun.generate('retrieval JSON'), /运行编号不匹配/);

  for (const patch of [{ name: 'another-name' }, { external_id: 'another-request' }, { head_sha: 'another-commit' }]) {
    const missing = harness(runFetcher([{ ...resultCheck(), ...patch }]));
    await assert.rejects(missing.generate('retrieval JSON'), /未返回候选/);
    assert.equal(missing.elapsed(), 65000, 'wait 60 seconds from first observing completion');
    assert.equal(missing.calls.filter((x) => x.opts.method === 'POST').length, 1);
  }

  for (const result of [
    { ok: true, request_id: 'wrong', run_id: '42', candidates },
    { ok: false, request_id: requestId, run_id: '42', error: '模型生成失败' },
    { ok: true, request_id: requestId, run_id: '42' },
  ]) {
    const invalid = harness(runFetcher([resultCheck(result)]));
    await assert.rejects(invalid.generate('retrieval JSON'), /编号不匹配|模型生成失败|未收到候选/);
  }
  const failedCheck = harness(runFetcher([{ ...resultCheck(), conclusion: 'failure' }]));
  await assert.rejects(failedCheck.generate('retrieval JSON'), /模型生成失败/);

  // Completion can be visible well before the result check, including at the end of the total wait.
  let delayedPolls = 0;
  const delayed = harness(runFetcher(() => ++delayedPolls < 10 ? [] : [resultCheck()]));
  const delayedProgress = [];
  assert.deepEqual(JSON.parse(JSON.stringify(await delayed.generate('retrieval JSON', (s) => delayedProgress.push(s)))), candidates);
  assert.equal(delayed.elapsed(), 50000);
  assert.ok(delayedProgress.some((s) => s.includes('同步')));

  let discoveryPolls = 0;
  let lateCheckPolls = 0;
  const late = harness(async (url) => {
    if (url.endsWith('/dispatches')) return response(null, 204);
    if (url.includes('/runs?')) return response({ workflow_runs: ++discoveryPolls < 119 ? [] : [completed] });
    if (url.endsWith('/runs/42')) return response(completed);
    return response({ check_runs: ++lateCheckPolls < 10 ? [] : [resultCheck()] });
  });
  assert.deepEqual(JSON.parse(JSON.stringify(await late.generate('retrieval JSON'))), candidates);
  assert.ok(late.elapsed() > 600000, 'completion gets its own synchronization window');
  console.log('query generation transport tests passed');
}

main().catch((err) => { console.error(err); process.exitCode = 1; });
