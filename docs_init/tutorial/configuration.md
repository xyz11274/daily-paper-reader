# 订阅与查询配置

## 网页生成检索词条

填写研究需求后，点击生成，等待候选出现，再勾选关键词与意图查询并保存。

网页通过 GitHub Actions 生成候选，和日报共用仓库 `Settings → Secrets and variables → Actions` 中的配置：

| Secret | 火山引擎套餐配置 |
| --- | --- |
| `SUMMARY_API_KEY` | 你的火山 API Key |
| `SUMMARY_BASE_URL` | `https://ark.cn-beijing.volces.com/api/plan/v3` |
| `SUMMARY_MODEL` | `deepseek-v4.1-flash` |

词条生成使用这三个 Secrets，浏览器保存的旧模型参数不会覆盖它们。只需要在网页解锁用于触发工作流的 GitHub Token；细粒度 Token 需要当前仓库的 Actions 读写和 [Checks 读取权限](https://docs.github.com/en/rest/checks/runs#list-check-runs-for-a-git-reference)。

生成时请保持页面打开。任务可能需要排队，结果返回后仍由你选择和保存，不会自动修改订阅。

### 常见问题

- **升级后仍提示 `Failed to fetch`**：确认仓库默认分支已包含 `.github/workflows/generate-query.yml` 和新版网页文件；等待 Pages 部署完成后强制刷新。旧版网页直接请求火山接口，会被浏览器的跨域检查拦截。
- **未找到生成工作流**：同步上述工作流到默认分支，确认已启用 Actions，并检查 GitHub Token 的仓库访问权限。
- **模型鉴权失败**：检查 `SUMMARY_API_KEY` 与 `SUMMARY_BASE_URL` 是否属于同一服务和套餐。
- **生成超时**：先查看页面提示的 Actions 运行记录，确认本次任务状态后再重试。
- **本地调试**：启动 `python src/local_debug_server.py`，在 `.env` 中配置相同的 `SUMMARY_*`。网页会使用本地后端生成；更新代码后需要重启后端。

## 关键词与意图查询

`keyword` 是用于 BM25 召回的英文短语，`query` 是对应的英文语义改写。独立的意图查询用于语义召回。候选中的中文字段用于解释检索含义；应用候选后，仍需点击设置面板的保存按钮。
