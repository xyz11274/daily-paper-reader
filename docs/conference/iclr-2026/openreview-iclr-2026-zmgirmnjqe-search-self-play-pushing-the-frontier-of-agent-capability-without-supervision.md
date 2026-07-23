---
title: "Search Self-Play: Pushing the Frontier of Agent Capability without Supervision"
title_zh: 搜索自博弈：无监督下推动代理能力边界
authors: "Hongliang Lu, Yuhang Wen, Pengyu Cheng, Ruijin Ding, Jiaqi Guo, Haotian Xu, Chutian Wang, Haonan Chen, xiaoxi jiang, guanjunjiang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=ZmGirmNJqE"
tags: ["query:ase"]
score: 8.0
evidence: 通过自博弈训练提升代理能力且无需监督
tldr: 基于可验证奖励的强化学习（RLVR）依赖人工设计的任务和答案，难以扩展。本文提出搜索自博弈，让学习LLM同时扮演任务提议者和求解者，通过多轮搜索引擎调用生成难度可控的代理任务，实现无监督的RL训练。该方法显著提升了深度搜索代理的能力，并突破了人工标注瓶颈。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: RLVR依赖人工任务标注，难以扩展。
method: 代理同时作为任务提议者和求解者进行自博弈，通过搜索引擎生成任务。
result: 深度搜索代理在多种基准上性能大幅提升，且无需人工标注。
conclusion: 自博弈范式能有效扩展RLVR到代理场景。
---

## Abstract
Reinforcement learning with verifiable rewards (RLVR) has become the mainstream technique for training LLM agents. However, RLVR highly depends on well-crafted task queries and corresponding ground-truth answers to provide accurate rewards, which requires significant human effort and hinders the scaling of RL processes, especially in agentic scenarios. Although a few recent works explore task synthesis methods, the difficulty of generated agentic tasks can hardly be controlled to provide effective RL training advantages. To achieve agentic RLVR with higher scalability, we explore self-play training for deep search agents, in which the learning LLM utilizes multi-turn search engine calling and acts simultaneously as both a task proposer and a problem solver. The task proposer aims to generate deep search queries with well-defined ground-truth answers and increasing task difficulty. The problem solver tries to handle the generated search queries and output the correct answer predictions. To ensure that each generated search query has accurate ground truth, we collect all the searching results from the proposer's trajectory as external knowledge, then conduct retrieval-augmentation generation (RAG) to test whether the proposed query can be correctly answered with all necessary search documents provided. In this search self-play (SSP) game, the proposer and the solver co-evolve their agent capabilities through both competition and cooperation. With substantial experimental results, we find that SSP can significantly improve search agents' performance uniformly on various benchmarks without any supervision under both from-scratch and continuous RL training setups. The code is at https://github.com/Qwen-Applications/SSP.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有强化学习中的可验证奖励（RLVR）虽然在训练LLM代理方面取得了主流地位，但其严重依赖于人工精心设计的任务查询和对应的真实答案。这种人工标注方式消耗大量人力，难以扩展到复杂的代理场景（agentic scenarios），尤其是当任务数量和数据量需要不断增大时，人工标注成为瓶颈。
- **研究动机**：尽管已有一些工作尝试自动合成任务，但生成的代理任务难度难以控制，无法提供有效的强化学习训练优势。因此，作者希望探索一种无需人工监督、能自动生成难度可控且具有真实答案的代理任务的方法，从而推动RLVR在代理场景下的可扩展性。
- **整体含义**：本文提出的搜索自博弈（Search Self-Play, SSP）范式，让一个学习中的LLM同时扮演任务提议者和求解者，通过多轮搜索引擎调用和自博弈训练，实现无监督下代理能力的提升。这突破了RLVR对人工标注的依赖，为训练深度搜索代理提供了一种可扩展的新路径。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- **自博弈（Self-Play）**：学习中的LLM在同一环境中同时担任两个角色：
  - **任务提议者（Task Proposer）**：生成带有真实答案的深度搜索查询，并逐步增加任务难度。
  - **问题求解者（Problem Solver）**：处理提议者生成的搜索查询，输出正确答案预测。
- 两个角色通过竞争与合作共同演化：提议者试图生成更难的任务，而求解者努力解决这些任务，从而推动双方能力提升。

### 关键技术细节
1. **任务生成与真实性保障**：
   - 提议者生成搜索查询时，会执行多轮搜索引擎调用，收集搜索轨迹中的所有结果作为外部知识。
   - 采用**检索增强生成（RAG）** 技术：用这些外部文档测试提议的查询是否能被正确回答。若在提供所有必要文档后查询能被正确回答，则认定该查询具有准确的真实答案，可以被纳入训练。
2. **训练流程**：
   - 在训练过程中，该LLM交替作为提议者和求解者。通过强化学习（RL）优化策略，使得提议者能生成难度递增的任务，求解者能提升解决任务的能力。
   - 整个过程无需任何人工标注，完全依赖搜索引擎和自博弈机制生成训练信号。
3. **算法流程（文字描述）**：
   - 初始化LLM策略。
   - 循环：
     - 采样一些搜索查询及其搜索轨迹（提议者行为）。
     - 基于RAG验证查询的正确性，筛选出可验证的任务。
     - 将这些任务作为RLVR的训练数据，训练求解者。
     - 同时更新提议者的策略以生成难度更高的新任务。
   - 重复此循环直到收敛。

## 3. 实验设计

- **使用的数据集/场景**：实验主要针对**深度搜索代理**（deep search agents）的能力评估，在多种基准（多种benchmark）上进行测试。具体数据集名称未在元数据中列出，但摘要指出“uniformly on various benchmarks”。
- **Benchmark**：未详细说明，但暗示涵盖了多个标准代理或搜索任务评测集合。
- **对比方法**：
  - 本文并未在元数据中明确列出对比基线，但从摘要可推测对比了传统RLVR方法（依赖人工数据）和其他任务合成方法（如无难度控制的合成）。具体对比方法需要阅读原文才能完整了解。
  - 实验设置包括两种：
    - **从零开始训练（from-scratch）**：完全使用SSP生成的数据训练代理。
    - **持续RL训练（continuous RL training）**：在已有模型基础上继续用SSP微调。

## 4. 资源与算力

- 元数据及摘要中**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。通常学术论文会在实验部分详细列出，但这里未提供。需要指出这一点。

## 5. 实验数量与充分性

- **实验数量**：论文进行了多组实验，包括“在不同基准上”、“从零开始和持续RL训练两种设置”下的性能评估。此外，可能还包含消融实验（如验证RAG过滤的作用、任务难度递增的影响等）。但元数据未给出具体实验组数。
- **充分性评价**：根据摘要声明“SSP可以显著提升搜索代理性能，且在各种基准上表现一致”，可推测实验覆盖了多个不同的评测环境，因此具有一定的广泛性。但缺少详细的统计显著性和误差分析等信息，只从摘要看实验设计看似合理，但公平性和客观性需要全文证据支持（如是否与足够基线对比、是否控制变量等）。由于无法访问完整论文，这里仅基于已有信息做初步判断——实验数量可能充分，但具体严谨性待考。

## 6. 论文的主要结论与发现

- **主要结论**：搜索自博弈（SSP）能够在**无需任何人工监督**的条件下，显著提升深度搜索代理在各种基准上的性能。无论是从零开始训练还是持续RL训练，SSP都表现出稳定的改进效果。
- **关键发现**：
  - 自博弈范式可以自动生成难度可控且具有真实答案的代理任务，有效克服了传统RLVR的人工标注瓶颈。
  - 提议者和求解者的共同演化使得代理能力持续提升。
  - 该方法具有良好的可扩展性，为训练通用代理提供了新方向。

## 7. 优点：方法或实验设计上的亮点

- **方法创新性**：
  - 提出“搜索自博弈”概念，将自博弈从游戏领域扩展到LLM代理的训练，让LLM同时扮演任务生成者和求解者，实现闭环自我改进。
  - 利用RAG技术验证生成任务的真实性，确保强化学习奖励的可靠性，这是前人工作中未充分解决的难题。
  - 无需任何人工标注数据，完全自动化，极大降低了训练成本。
- **实验设计亮点**：
  - 同时在“从零开始”和“持续训练”两种设置下评估，验证了方法的通用性和实用性。
  - 测试了多个基准，展示了泛化能力。
  - 代码开源（GitHub），便于复现和后续研究。

## 8. 不足与局限

- **实验覆盖**：文中未详细列出所评测的基准和对比基线，难以判断是否涵盖了最有挑战的场景。代理类型仅限“深度搜索代理”，是否适用于其他类型的代理（如工具使用、代码执行等）尚不明确。
- **偏差风险**：
  - 自博弈过程中，任务难度可能受限于LLM自身能力上限，存在自我强化的循环偏差。
  - RAG验证依赖搜索引擎返回结果的质量，若搜索引擎存在偏见或不完整，可能影响任务真实性。
- **应用限制**：
  - 该方法目前仅针对搜索场景，对于不需要搜索引擎的代理任务（如基于API操作）可能不直接适用。
  - 训练效率：自博弈需要反复调用搜索引擎和RAG，计算成本可能较高，论文未提供效率分析。
  - 未讨论多智能体或更复杂的环境。
- **资源与算力缺失**：未提供训练所需的硬件和时长，影响了可复现性和对实际可行性的评估。

（完）
