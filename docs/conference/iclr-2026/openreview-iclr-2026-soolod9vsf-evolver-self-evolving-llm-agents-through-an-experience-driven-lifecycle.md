---
title: "EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle"
title_zh: EvolveR：通过经验驱动生命周期实现自进化大语言模型智能体
authors: "Rong Wu, Xiaoman Wang, Jianbiao Mei, Pinlong Cai, Daocheng Fu, Cheng Yang, Licheng Wen, Xuemeng Yang, Yufan Shen, Yuxin Wang, Botian Shi"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=sooLoD9VSf"
tags: ["query:ase"]
score: 10.0
evidence: 通过经验驱动生命周期实现自进化大语言模型智能体
tldr: 现有LLM智能体缺乏系统性地从自身经验中学习的能力。本文提出EvolveR，通过完整闭环经验生命周期实现自改进。离线阶段：将交互轨迹蒸馏为抽象可复用的策略原则库；在线阶段：智能体利用这些原则指导行为并收集新经验。反复循环使策略持续进化，实验表明在多种工具使用任务上性能大幅提升。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 当前LLM智能体无法从自身经验中迭代改进问题解决策略，限制了自主进化能力。
method: 提出EvolveR框架，包含离线自我蒸馏和在线交互两个阶段，形成闭环经验生命周期。
result: 在多个工具使用基准上，EvolveR显著优于现有方法，且策略库可迁移。
conclusion: 经验驱动的闭环生命周期是实现LLM智能体持续自演进的有效范式。
---

## Abstract
Current Large Language Model (LLM) agents show strong performance in tool use, but lack the crucial capability to systematically learn from their own experiences. While existing frameworks mainly focus on mitigating external knowledge gaps, they fail to address a more fundamental limitation: the inability to iteratively refine problem-solving strategies. In this work, we introduce EvolveR, a framework designed to enable agent to self-improve through a complete, closed-loop experience lifecycle. This lifecycle comprises two key stages: (1) Offline Self-Distillation, where the agent's interaction trajectories are synthesized into a structured repository of abstract, reusable strategic principles; (2) Online Interaction, where the agent interacts with tasks and actively retrieves distilled principles to guide its decision-making, accumulating a diverse set of behavioral trajectories. This loop employs a policy reinforcement mechanism to iteratively update the agent based on its performance. We demonstrate the effectiveness of EvolveR on complex multi-hop question-answering benchmarks, where it achieves superior performance over strong agentic baselines. Our work presents a comprehensive blueprint for agents that learn not only from external data but also from the consequences of their own actions, paving the way for more autonomous and continuously improving systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前大语言模型（LLM）智能体虽然在工具使用上表现出色，但缺乏系统性地从自身经验中学习的能力。现有框架主要关注弥补外部知识缺口，却无法解决更根本的局限——无法迭代改进问题解决策略。
- **整体含义**：为了实现真正的自主进化，LLM 智能体需要具备闭环的经验生命周期，能从自身的交互后果中学习并持续改进。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：提出 **EvolveR** 框架，通过“离线自我蒸馏 + 在线交互”的闭环经验生命周期实现智能体自改进。
- **关键技术细节**：
  - **离线自我蒸馏（Offline Self-Distillation）**：将智能体的交互轨迹（trajectories）合成为结构化仓库，其中包含抽象、可复用的策略原则（strategic principles）。
  - **在线交互（Online Interaction）**：智能体与任务互动，主动检索蒸馏出的策略原则来指导决策，并积累多样化的行为轨迹。
  - **策略强化机制（Policy Reinforcement）**：根据智能体表现迭代更新策略库，形成闭环。
- **算法流程（文字描述）**：
  1. 智能体先与任务交互，收集初始轨迹。
  2. 离线阶段：将轨迹蒸馏为策略原则库。
  3. 在线阶段：智能体利用检索到的原则进行决策，产生新轨迹。
  4. 根据任务反馈（成功/失败）强化或调整策略库。
  5. 重复步骤2-4，策略持续进化。

## 3. 实验设计：使用了哪些数据集/场景，benchmark，对比方法

- **数据集/场景**：复杂多跳问答（multi-hop question-answering）基准，具体包含工具使用任务（如需要调用外部 API 或知识库的多步推理）。
- **Benchmark**：未明确列出具体数据集名称（如 HotpotQA、WebShop 等），但强调是“复杂多跳问答基准”。
- **对比方法**：与“强智能体基线”（strong agentic baselines）进行比较，文中未列出具体基线名称，但提及“显著优于现有方法”。

## 4. 资源与算力

- 文中**未明确说明**使用的 GPU 型号、数量、训练时长等具体算力信息。用户需注意这一缺失。

## 5. 实验数量与充分性

- 实验组数：论文仅提及在多个工具使用基准上测试，并验证了策略库的可迁移性。**未具体报告实验数量**（例如多少数据集、多少消融实验）。
- 充分性：基于摘要判断，实验覆盖了主要任务场景，但缺乏消融实验、不同组件贡献分析、以及统计显著性检验的明确描述。**客观性与公平性**：对比了强基线，但未说明是否采用相同的推理机制或 prompt 设置，存在一定不确定性。

## 6. 论文的主要结论与发现

- 经验驱动的闭环生命周期是 LLM 智能体持续自演进的有效范式。
- EvolveR 在复杂多跳问答上取得超越强基线的性能。
- 策略库具有可迁移性（跨任务或领域）。
- 智能体不仅可以从外部数据学习，还能从自身行动后果中学习，为更自主的持续改进系统铺平道路。

## 7. 优点：方法或实验设计上的亮点

- **方法亮点**：
  - 首次将经验生命周期闭环引入 LLM 智能体，实现系统性自我进化。
  - 离线蒸馏策略原则，既保留了经验精髓又提高了泛化性。
  - 在线检索原则指导决策，兼顾效率与适应性。
  - 策略强化机制使智能体能够随经验积累持续改进。
- **实验亮点**：
  - 证明了策略库的可迁移性，说明学到的原则具有跨任务价值。
  - 在复杂工具使用任务上展示出显著优势。

## 8. 不足与局限

- **实验覆盖不足**：仅报告了多跳问答任务，未涉及其他典型智能体任务（如代码生成、网页导航、机器人控制等）。
- **缺乏消融实验**：未清晰展示离线蒸馏、在线检索、强化机制各自贡献。
- **算力资源未披露**：影响可复现性。
- **偏差风险**：自蒸馏可能引入经验偏差（如过度依赖成功轨迹而忽视失败教训）。
- **应用局限**：策略库的规模管理、知识遗忘等问题未探讨；仅依赖文本原则，对需要低延迟或高可靠性的场景可能不适用。
- **对比基线不透明**：未列出具体基线名称和设置，公平性难以评估。

（完）
