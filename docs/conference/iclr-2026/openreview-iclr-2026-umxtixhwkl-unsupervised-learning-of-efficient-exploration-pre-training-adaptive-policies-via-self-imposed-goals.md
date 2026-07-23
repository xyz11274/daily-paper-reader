---
title: "Unsupervised Learning of Efficient Exploration: Pre-training Adaptive Policies via Self-Imposed Goals"
title_zh: 高效探索的无监督学习：通过自我设定目标预训练自适应策略
authors: Octavio Pappalardo
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=UmxTIxHWkl"
tags: ["query:ase"]
score: 8.0
evidence: 通过自我设定目标在元学习框架中实现高效多幕探索与适应
tldr: 在下游任务分布宽广且零样本不可行时，智能体需高效多幕探索与适应。本文提出在元学习框架内优化智能体自我设定目标和追求目标的能力，使其在预训练后能快速适应未见任务。实验表明，该方法在多个连续任务集合上显著加速了学习。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 无监督预训练中，智能体如何有效生成、选择并从自我设定的目标中学习是关键挑战。
method: 采用元学习框架，优化智能体在多幕探索中自我设定目标并高效适应后续任务。
result: 在多个下游任务分布上，预训练策略显著提升了零样本和少样本适应性能。
conclusion: 自我设定目标的元学习预训练为实现高效探索与快速适应提供了有效途径。
---

## Abstract
Unsupervised pre-training can equip reinforcement learning agents with prior knowledge and accelerate learning in downstream tasks. A promising direction, grounded in human development, investigates agents that learn by setting and pursuing their own goals. The core challenge lies in how to effectively generate, select, and learn from such goals. Our focus is on broad distributions of downstream tasks where solving every task zero-shot is infeasible. Such settings naturally arise when the target tasks lie outside of the pre-training distribution or when their identities are unknown to the agent. In this work, we (i) optimize for efficient multi-episode exploration and adaptation within a meta-learning framework, and (ii) guide the training curriculum with evolving estimates of the agent’s post-adaptation performance. We present ULEE, an unsupervised meta-learning method that combines an in-context learner with an adversarial goal-generation strategy that maintains training at the frontier of the agent’s capabilities. On XLand-MiniGrid benchmarks, ULEE pre-training yields improved exploration and adaptation abilities that generalize to novel objectives, environment dynamics, and map structures. The resulting policy attains improved zero-shot and few-shot performance, and provides a strong initialization for longer fine-tuning processes. It outperforms learning from scratch, DIAYN pre-training, and alternative curricula.

---

## 论文详细总结（自动生成）

以下是根据给定论文（OpenReview PDF摘要及元数据）生成的结构化中文总结。

---

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：在无监督预训练中，智能体如何有效生成、选择并从自我设定的目标中学习，以实现高效的多幕探索和快速适应下游任务。
- **背景**：强化学习中的无监督预训练旨在赋予智能体先验知识，加速下游任务学习。受人类发展启发，智能体可通过自我设定并追求目标来学习。然而，当下游任务分布宽广、零样本求解不可行（例如目标任务超出预训练分布或身份未知）时，现有方法难以高效探索与适应。
- **整体含义**：本文提出通过元学习框架优化智能体自我设定目标和追求目标的能力，使其在预训练后能快速适应未见任务，从而提升零样本和少样本性能。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将无监督预训练视为一个元学习问题，优化智能体在多幕探索中自我设定目标并高效适应后续任务的能力。
- **关键技术细节**：
  - 采用**上下文学习器（in-context learner）** 作为策略表示，使智能体能够根据过去经验动态调整行为。
  - 引入**对抗式目标生成策略（adversarial goal-generation strategy）**，该策略根据智能体后适应性能的演变估计来引导训练课程，始终将训练维持在智能体能力前沿。
  - 方法命名为**ULEE（Unsupervised Learning of Efficient Exploration）**。整体框架结合了元学习与目标对抗生成，使预训练过程能持续挑战智能体，迫使它探索更复杂的情境。
  - **无公式/算法流程的文字说明**：预训练阶段，智能体在多轮幕中自主设定目标（例如新地图、新动力学），并尝试达成；对抗式机制根据智能体当前表现动态调整目标难度，使其始终处于“可学”但“有挑战”的状态；最终策略可无梯度地快速适应新任务（如在上下文学习）。

## 3. 实验设计：数据集 / 场景、benchmark、对比方法

- **数据集/场景**：使用 **XLand-MiniGrid** 基准，这是一个基于网格世界的多任务强化学习环境，涵盖多样化的目标、环境动态和地图结构。
- **Benchmark**：自身提出，未明确说明是否使用公开标准benchmark，但XLand-MiniGrid是通用测试平台。
- **对比方法**：
  - 从头学习（learning from scratch）
  - DIAYN 预训练（一种无监督技能发现方法）
  - 替代课程（alternative curricula）
- **评估指标**：零样本性能、少样本（few-shot）性能以及更长时间微调后的性能。

## 4. 资源与算力

- **论文中未明确说明**使用的GPU型号、数量、训练时长等算力信息。从文本（仅有摘要）无法获取此类细节。需注意，这可能是因为该论文的完整版本未提供，或作者未在摘要中披露。

## 5. 实验数量与充分性

- **实验数量**：摘要中提到在XLand-MiniGrid上进行了预训练，并评估了零样本和少样本性能，以及与多个基线比较。但未给出具体实验组数（如不同任务分布数量、消融实验组数等）。
- **充分性与公平性**：
  - 对比方法全面（包括从头学习、DIAYN、替代课程），且评估维度涵盖零样本、少样本和微调，设计合理。
  - 但缺乏消融实验的明确描述（如是否单独分析每个组件的作用），且未报告方差或统计显著性，因此充分性难以完全判断。不过作为会议论文的摘要，通常完整的实验部分会在正文中给出。

## 6. 论文的主要结论与发现

- ULEE预训练在XLand-MiniGrid上产生了改进的探索和适应能力，且这些能力能泛化到**新的目标、环境动态和地图结构**。
- 预训练策略在**零样本和少样本**任务上均取得了更好的性能，并为更长时间的微调提供了**强大的初始化**。
- 相比从头学习、DIAYN和替代课程，ULEE表现出明显优势。

## 7. 优点：方法或实验设计上的亮点

- **方法上**：
  - 将自我设定目标与元学习结合，使用对抗式目标生成动态调整训练课程，避免过早饱和或过度挑战，有效提升探索效率。
  - 使用上下文学习器实现无梯度快速适应，适合多幕学习场景。
- **实验设计上**：
  - 测试了多种下游任务分布（新目标、新动态、新地图），验证了泛化能力。
  - 比较了多种有代表性的基线（无监督预训练DIAYN、无预训练、替代课程），对比充分。

## 8. 不足与局限

- **实验覆盖**：仅在XLand-MiniGrid一个benchmark上验证，缺乏在连续控制、机器人操作等更复杂或高维环境的结果，泛化性有待验证。
- **偏差风险**：未报告多次试验的均值和方差，可能存在随机性导致的偏差；未明确说明是否进行超参数敏感性分析。
- **应用限制**：方法依赖于多幕交互和元学习框架，计算开销可能较大；对抗式目标生成需要额外奖励建模，可能难以扩展到奖励稀疏或大规模真实环境。
- **信息缺失**：算力消耗、代码或模型复现细节未提供，可复现性不明确。此外，论文元数据中作者仅一人，可能存在学术独立性问题（非多人团队）。

---

（完）
