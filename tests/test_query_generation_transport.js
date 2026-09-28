const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const requestId = '12345678-1234-1234-1234-123456789abc';
const name = `dpr-query-${requestId}`;
const candidates = { keywords: [{ keyword: 'agent memory', query: 'agent memory' }], intent_queries: [] };
const completed = { id: 42, head_sha: 'abc123', display_title: name, status: 'completed', conclusion: 'success' };
const resultCheck = (result = { ok: true, request_id: requestId, candidates }) => ({
  name, external_id: requestId, details_url: 'https://github.com/tester/papers/actions/runs/42',
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
  return { generate: sandbox.window.DPRQueryGeneration.generate, calls };
}

async function main() {
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

  const missing = harness(async (url) => {
    if (url.endsWith('/dispatches')) return response(null, 204);
    if (url.includes('/runs?')) return response({ workflow_runs: [completed] });
    if (url.endsWith('/runs/42')) return response(completed);
    // Even a check on the same commit is rejected if it belongs to another run.
    return response({ check_runs: [{ ...resultCheck(), details_url: 'https://github.com/tester/papers/actions/runs/41' }] });
  });
  await assert.rejects(missing.generate('retrieval JSON'), /未返回候选/);
  console.log('query generation transport tests passed');
}

main().catch((err) => { console.error(err); process.exitCode = 1; });
