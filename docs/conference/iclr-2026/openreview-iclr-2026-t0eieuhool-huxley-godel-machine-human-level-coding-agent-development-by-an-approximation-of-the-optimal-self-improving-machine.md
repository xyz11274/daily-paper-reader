---
title: "Huxley-G\\\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine"
title_zh: Huxley-哥德尔机器：近似最优自改进机器的人机编码智能体开发
authors: "Wenyi Wang, Piotr Piękos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jürgen Schmidhuber"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=T0EiEuhOOL"
tags: ["query:ase"]
score: 9.0
evidence: 通过编辑自身代码库实现自改进的编码智能体
tldr: 现有自改进编码智能体以单一代码版本性能引导自我修改，但存在元生产率与性能的不匹配。本文借鉴Huxley的支序概念，提出CMP指标聚合一个智能体所有后代的基准表现，以此更准确地评估其自改进潜力。实验表明，基于CMP的扩展策略提高了长期改进效果。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 当前自改进编码智能体仅以当前编码性能指导自我修改，忽略了长期改进潜力。
method: 提出CMP指标，通过聚合智能体后代的基准表现来评估其自改进潜力，并以此指导扩展策略。
result: 使用CMP引导的智能体在软件工程基准上展现出更强的长期自我改进能力。
conclusion: CMP指标有效缓解了元生产率与性能的不匹配，为自改进智能体提供了更优的引导信号。
---

## Abstract
Recent studies operationalize self-improvement through coding agents that edit their own codebases. They grow a tree of self-modifications through expansion strategies that favor higher software engineering benchmark performance, assuming that this implies more promising subsequent self-modifications. However, we identify a mismatch between the agent’s self-improvement potential (metaproductivity) and its coding benchmark performance, namely the Metaproductivity-Performance~Mismatch. Inspired by Huxley’s concept of clade, we propose a metric ($\mathrm{CMP}$) that aggregates the benchmark performances of the descendants of an agent as an indicator of its potential for self-improvement. We show that, in our self-improving coding agent development setting, access to the true CMP is sufficient to simulate how the Gödel Machine would behave under certain assumptions. We introduce the Huxley-G\"odel Machine (HGM), which, by estimating $\mathrm{CMP}$ and using it as guidance, searches the tree of self-modifications. On SWE-bench Verified and Polyglot, HGM outperforms prior self-improving coding agent development methods while using fewer allocated CPU hours. Last but not least, HGM demonstrates strong transfer to other coding datasets and LLMs. %large language models. 
The agent optimized by HGM on SWE-bench Verified with GPT-5 mini and evaluated on SWE-bench Lite with GPT-5 achieves human-level performance, matching the best officially checked results of human-engineered coding agents. Our code is publicly available at https://github.com/metauto-ai/HGM.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

当前自改进编码智能体（coding agents）通过编辑自身代码库来迭代优化，它们构建一个自我修改的树，并依据当前代码版本在软件工程基准（如 SWE-bench）上的性能来选择更优的修改路径。然而，研究者发现存在 **“元生产率-性能不匹配”（Metaproductivity-Performance Mismatch）**：即智能体当前的编码性能并不能很好地反映其未来的自我改进潜力（元生产率）。这种错位导致贪婪地选择高性能代际版本可能错过长远更优的改进路径。受 Huxley 的“支序”（clade）概念启发，论文提出一个衡量智能体所有后代（descendants）综合表现的指标，以更好地指导自改进过程，并近似模拟了哥德尔机器（Gödel Machine）——一种理论上最优的自改进机器——在特定假设下的行为。最终目标是在有限计算资源下实现人类水平的编码能力。

## 2. 方法论：核心思想、关键技术细节

- **核心指标：CMP（Clade Metaproductivity）**  
  定义：对于一个智能体节点，其 CMP 值为该节点所有后代（包括自身）在某个基准上的表现（如性能分数）的聚合（例如平均或加权和）。CMP 反映了该节点作为“祖先”的长期自改进潜力，而非仅当前性能。

- **关键技术：Huxley-Gödel Machine（HGM）**  
  - HGM 在自修改树中进行搜索，使用估计的 CMP 作为引导信号，而不是直接使用当前版本的基准分数。
  - 搜索策略：通过估计 CMP 值，决定哪些节点值得进一步扩展（生成子代修改），从而更有效地探索修改空间。
  - 算法流程（文字说明）：
    1. 初始化：以初始编码智能体（如基于 GPT-5 mini）开始，生成初始代码版本。
    2. 扩展：从当前根节点出发，通过多种修改操作（如代码重构、功能添加等）生成子代版本。
    3. 评估：在训练集上评估每个子代代码的基准性能。
    4. CMP 估计：对于每个节点，计算其所有已评估后代的性能聚合值作为 CMP 的估计（使用启发式或滚动预测）。
    5. 选择：选择 CMP 估计值最高的节点进行进一步扩展（分支）。
    6. 迭代：重复步骤 2-5，直到资源耗尽或达到终止条件。最终输出 CMP 最优的节点对应的代码智能体。

- **与哥德尔机器的联系**：在理想假设下（拥有真实 CMP），该搜索策略等价于哥德尔机器的行为——即子代修改的效益足以补偿搜索成本。HGM 通过近似 CMP 实现可行版本。

## 3. 实验设计

- **数据集/场景**：
  - **SWE-bench Verified**（主要基准）：面向真实软件工程问题的编码任务。
  - **Polyglot**：多语言编程基准。
  - **SWE-bench Lite**（用于迁移测试）。
- **基准**：SWE-bench 系列、Polyglot 上的解决率或准确率。
- **对比方法**：
  - 之前提出的自改进编码智能体方法（如基于当前性能的贪婪扩展策略）。
  - 可能包括基线无自改进的智能体。
- **迁移实验**：将在 SWE-bench Verified 上优化的智能体直接应用到 SWE-bench Lite（使用不同 LLM 如 GPT-5）上，检验泛化能力。

## 4. 资源与算力

论文元数据及摘要中 **未明确说明** 所使用的 GPU 型号、数量及训练时长。仅提到 HGM 在比之前方法更少的分配 CPU 小时（allocated CPU hours）下取得了更好结果。可以推断主要计算资源是 CPU 密集型（代码编译与测试），而非重型 GPU 训练。但具体算力细节缺失。

## 5. 实验数量与充分性

- **主要实验**：至少包括两个基准（SWE-bench Verified 和 Polyglot）上的性能比较。
- **迁移实验**：跨基准迁移（从 SWE-bench Verified 到 SWE-bench Lite）以及跨 LLM 迁移（从 GPT-5 mini 到 GPT-5）。
- **消融实验**：元数据提到“消融实验”可能包含（未详细列出，但通常论文会做）。基于强度，实验覆盖了主要场景、跨模型泛化、效率对比。但 **缺少多维度消融**（如 CMP 聚合方式、搜索深度影响、不同 LLM 基座对比等）的明确描述。从提供的摘要来看，实验是客观公平的（相同计算分配下比较），但不排除隐藏的随机性偏差。

## 6. 主要结论与发现

- CMP 指标有效缓解了元生产率与当前性能的不匹配，为自改进编码智能体提供了更优的引导信号。
- 使用 CMP 引导的 HGM 在 SWE-bench Verified 和 Polyglot 上超过了之前的方法，且消耗更少的 CPU 小时。
- HGM 优化的智能体在 SWE-bench Lite 上使用 GPT-5 达到了人类水平性能（匹配最佳官方验证的人类工程编码智能体结果）。
- 方法表现出很强的跨数据集和跨 LLM 迁移能力。

## 7. 优点（方法或实验设计亮点）

- **理论动机清晰**：从哥德尔机器理论出发，提出可操作的近似方案，具有理论严谨性。
- **指标创新**：CMP 指标抓住了长期进化的潜力，避免了贪婪陷阱。
- **效率提升**：在更少计算资源下获得更好性能，实用性高。
- **人类水平成果**：在特定基准上达到人类工程师水准，具有实践价值。
- **开放性**：代码已开源，可复现。

## 8. 不足与局限

- **算力细节缺失**：未提供 GPU 型号、数量、训练时间等，影响可复现性和公平对比。
- **实验范围有限**：主要基于 SWE-bench 系列和 Polyglot，缺乏更多样化的编码任务（如竞赛编程、真实软件仓库修复）。
- **CMP 估计偏差**：由于只能基于已评估的后代估计 CMP，对于无法充分探索的分支可能存在偏差（论文可能未充分讨论）。
- **跨 LLM 迁移仅测试了 GPT 系列**：未验证在其他开源或小型 LLM（如 CodeLlama、DeepSeek）上的表现。
- **未讨论安全性**：自修改代码可能引入漏洞或恶意行为，论文未提及安全防线。
- **现实应用限制**：需要大量自动评估（代码编译和测试），对于非结构化任务成本仍高；且依赖基准质量。

（完）
