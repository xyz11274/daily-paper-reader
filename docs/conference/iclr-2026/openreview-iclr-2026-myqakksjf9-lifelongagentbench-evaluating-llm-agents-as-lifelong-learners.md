---
title: "LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners"
title_zh: LifelongAgentBench：评估LLM智能体作为终身学习者的基准
authors: "Junhao Zheng, Xidi Cai, Qiuke Li, Duzhen Zhang, Zhong-Zhi Li, Yingying Zhang, Le Song, Qianli Ma"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=MYqAKKsjF9"
tags: ["query:ase"]
score: 7.0
evidence: 评估LLM智能体终身学习能力的基准
tldr: 当前LLM智能体缺乏知识积累能力，且没有统一的终身学习评估标准。本文提出LifelongAgentBench，首个统一基准，包含数据库、操作系统和知识图谱三个交互环境中的多阶段任务，支持自动标签验证和模块扩展。实验发现传统经验回放效果有限，揭示了现有方法在知识迁移和灾难性遗忘方面的不足。该基准为智能体终身学习研究提供了标准化评估平台。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 当前LLM智能体缺乏知识积累能力，且没有统一的终身学习评估标准。
method: 设计三个交互环境中的多阶段任务，并支持自动标签验证和模块扩展。
result: 实验发现传统经验回放效果有限，现有智能体在知识迁移方面表现不佳。
conclusion: 该基准有助于推动LLM智能体终身学习能力的研究与改进。
---

## Abstract
Lifelong learning is essential for intelligent agents operating in dynamic environments. Current large language model (LLM)-based agents, however, remain stateless and unable to accumulate or transfer knowledge over time. Existing benchmarks treat agents as static systems and fail to evaluate lifelong learning capabilities. We present LifelongAgentBench, the first unified benchmark designed to systematically assess the lifelong learning ability of LLM agents. It provides skill-grounded, interdependent tasks across three interactive environments—Database, Operating System, and Knowledge Graph—with automatic label verification, reproducibility, and modular extensibility. Extensive experiments reveal that conventional experience replay has limited effectiveness for LLM agents due to irrelevant information and context length constraints. We further introduce a group self-consistency mechanism that significantly improves lifelong learning performance. We hope LifelongAgentBench will advance the development of adaptive, memory-capable LLM agents.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：当前基于大语言模型（LLM）的智能体（Agent）缺乏知识积累与迁移能力，表现为“无状态”，无法在动态环境中实现终身学习（Lifelong Learning）。
- **研究动机**：现有基准将智能体视为静态系统，仅评估单次交互能力，缺乏对终身学习能力（如知识积累、任务间迁移、抗灾难性遗忘）的统一评估标准。
- **整体含义**：提出首个专门用于评估LLM智能体终身学习能力的统一基准——**LifelongAgentBench**，旨在推动智能体向自适应、有记忆能力的方向发展。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：构建一个覆盖多领域、多阶段且任务间具有技能依赖关系的交互环境，模拟智能体终身学习场景。
- **关键技术细节**：
  - **三个交互环境**：数据库（Database）、操作系统（Operating System）、知识图谱（Knowledge Graph）。每个环境包含一系列逐层递进、相互依赖的子任务。
  - **自动标签验证（automatic label verification）**：无需人工标注，自动生成并验证任务标签，保证评估可复现。
  - **模块化可扩展（modular extensibility）**：支持添加新任务、新环境或新智能体算法，便于社区扩展。
  - **组自一致性机制（group self-consistency）**：针对传统经验回放失效问题提出，通过多组独立推理并聚合结果，提升终身学习中的知识迁移与稳定性。

## 3. 实验设计
- **数据集/场景**：使用自行构建的三个交互环境（Database、OS、Knowledge Graph），每个环境包含多个阶段任务，总计模拟多种终身学习场景。
- **基准（Benchmark）**：LifelongAgentBench本身作为统一基准，包含任务序列、技能依赖关系、自动评估指标。
- **对比方法**：
  - 传统经验回放（Experience Replay）——被证明效果有限。
  - 未明确列出其他基线，但提及提出**组自一致性机制**作为改进方案。
- **备注**：文中未详细列出所有对比方法，可能包括无终身学习能力的原始LLM智能体（如ReAct、Reflexion等常见框架）。

## 4. 资源与算力
- **未明确说明**：论文摘要及元数据中未提及使用的GPU型号、数量或训练时长。仅能从“LLM-based agents”推断需调用大模型（可能通过API或本地推理），但具体算力消耗未披露。

## 5. 实验数量与充分性
- **实验数量**：文中称“大量实验”（extensive experiments），但未给出具体组数（如多少场景、多少种子、消融实验细节）。从摘要推断可能包括：
  - 在每个环境上评估多种智能体策略（经验回放 vs. 组自一致性）。
  - 可能包含超参数消融、任务顺序影响分析等。
- **充分性评估**：
  - **客观性**：自动标签验证机制减少了人工偏差，但未说明任务难度平衡或数据泄露防护。
  - **公平性**：未提供其他基准（如OpenAI Agent Benchmark）的对比，缺乏横向比较；仅展示在自建基准上的效果。
  - **充分性**：信息有限，难以判断消融实验是否完整；仅提出“组自一致性有效”一个结论，未充分分析失败案例或在不同LLM上的泛化性。

## 6. 论文的主要结论与发现
- **主要发现**：
  - 传统经验回放（Experience Replay）在LLM智能体终身学习中效果有限，原因包括：
    - 回放的信息可能不相关（irrelevant information）。
    - 上下文长度限制（context length constraints）导致长程记忆失效。
  - 提出的**组自一致性机制**显著提升终身学习性能（具体提升幅度未给出）。
- **总体结论**：LifelongAgentBench为LLM智能体终身学习研究提供了标准化评估平台，现有方法在知识迁移与抗遗忘方面存在明显不足，亟需新范式。

## 7. 优点
- **首个统一基准**：填补了LLM智能体终身学习评估的空白。
- **模块化设计**：交互环境可扩展，支持自定义任务与智能体算法。
- **自动标签验证**：保证可复现性，降低人工成本。
- **任务间技能依赖**：更贴近真实终身学习场景（需逐步积累技能）。
- **提出实用改进**：组自一致性机制针对发现的问题给出具体解决方向。

## 8. 不足与局限
- **实验覆盖有限**：仅包含三个环境，缺乏更多领域（如游戏、机器人、网页导航）的验证，通用性存疑。
- **对比方法不充分**：仅对比传统经验回放，未与更先进的增量学习方法（如Elastic Weight Consolidation、Prompt-based方法）比较。
- **资源算力未披露**：难以评估方法的实际部署成本或可复现性。
- **基线与评估指标细节缺失**：未明确说明基线模型（GPT-4、Llama等）及具体量化指标（准确率、成功率、遗忘率等），结论说服力不足。
- **潜在偏差风险**：自定基准可能无意中过度适配所提方法；组自一致性机制的理论分析较弱，仅停留在实验现象。
- **应用限制**：上下文长度约束在未来更大规模任务中可能仍是瓶颈，组自一致性的计算开销未讨论。

（完）
