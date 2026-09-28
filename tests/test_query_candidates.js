const assert = require('node:assert/strict');

global.window = {
  SubscriptionsManager: { getDraftConfig: () => ({}) },
  // A stale browser model must not override the repository SUMMARY_* settings.
  decoded_secret_private: { summarizedLLM: { baseUrl: 'https://api.deepseek.com', apiKey: 'old-key', model: 'deepseek-chat' } },
};
global.document = { readyState: 'loading', addEventListener() {} };
require('../app/subscriptions.smart-query.js');

async function testQueryUsesServerConfiguration() {
  let calls = 0;
  window.DPRQueryGeneration = {
    async generate(prompt) {
      calls++;
      assert.match(prompt, /experience memory/);
      return { keywords: [{ keyword: 'agent memory', query: 'agent experience memory' }], intent_queries: [] };
    },
  };
  global.fetch = async () => { throw new Error('browser must not call the model'); };
  const result = await window.SubscriptionsSmartQuery.generateResearchCandidates('agents', 'experience memory');
  assert.equal(calls, 1);
  assert.equal(result.keywords[0].keyword, 'agent memory');
  delete window.decoded_secret_private;
  await window.SubscriptionsSmartQuery.generateResearchCandidates('agents', 'experience memory');
  assert.equal(calls, 2, 'only GitHub credentials are required by the transport');
}

testQueryUsesServerConfiguration().then(() => console.log('query configuration regression passed')).catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
