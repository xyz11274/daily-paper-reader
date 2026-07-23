---
title: Self-Guided Plan Extraction for Instruction-Following Tasks with Goal-Conditional Reinforcement Learning
title_zh: 基于目标条件强化学习的指令跟随任务自引导计划提取
authors: "Zoya Volovikova, Nikita Sorokin, Dmitriy-Lukashevskiy, Aleksandr Panov, Alexey Skrynnik"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=dYaIotpCiK"
tags: ["query:ase"]
score: 7.0
evidence: 利用自学习机制和RL反馈进行计划提取
tldr: 在指令跟随任务中，现有方法依赖预定义子任务，人工成本高。本文提出自引导计划提取框架，让语言模型通过自学习机制生成并精炼高层计划，再使用目标条件强化学习训练代理执行计划，两者迭代共训形成闭环。在动态随机环境中，代理指令遵循度显著提升，且无需人工标注。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 预定义子任务耗力且不灵活，需要自动化的计划生成与改进机制。
method: 语言模型自生成并精炼计划，RL代理根据计划训练并反馈，形成迭代共训。
result: 在动态环境中，代理指令遵循度超过基线方法，且无需人工标注。
conclusion: 自引导计划提取与RL共训能有效提升指令跟随性能。
---

## Abstract
We introduce a framework for instruction-following tasks. Unlike prior methods that rely on predefined subtasks, our approach enables a language model to generate and refine high-level plans through a self-learning mechanism, reducing the need for manual dataset annotation. The method involves iterative co-training: an RL agent is trained to follow the generated plans, while the language model adapts and modifies these plans based on RL feedback and preferences. This creates a feedback loop where both the agent and the planner improve jointly. We validate the framework in environments with rich dynamics and stochasticity. Results show that our agents adhere to instructions more strictly than baseline methods, while also demonstrating strong generalization to previously unseen instructions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：在指令跟随任务中，现有方法通常依赖预定义的子任务（subtasks）来辅助语言模型生成执行计划。预定义子任务需要大量人工标注，不仅成本高、耗时长，而且难以适应动态变化的环境。
- **研究动机**：探索一种自动化、无需人工标注的计划生成与改进机制，让语言模型能够自主生成高层计划，并通过强化学习（RL）反馈不断精炼，从而提升代理（agent）遵循指令的能力。
- **整体含义**：提出一种“自引导计划提取”框架，将语言模型计划生成与目标条件强化学习训练形成闭环，实现联合迭代优化，显著提高指令遵循度，并展现出对未见指令的良好泛化能力。

## 2. 方法论

- **核心思想**：语言模型（LM）通过自学习机制（self-learning mechanism）初始生成高层计划，随后RL代理基于该计划进行训练并产生反馈；语言模型根据反馈和偏好调整计划，两者交替迭代共训，形成互惠的闭环反馈回路。
- **关键技术细节**：
  - **自学习计划生成**：语言模型在无人工标注的情况下，利用环境信息和任务描述自生成高层步骤（如子目标序列）。
  - **目标条件强化学习**：RL代理以生成计划为条件，学习如何执行每个步骤；奖励函数设计鼓励严格遵循指令。
  - **反馈循环**：RL训练过程中产生的轨迹和成功率等信号被用于更新语言模型，促使计划更合理、更易执行。
- **算法流程（文字）**：
  1. 初始化语言模型（可预训练）和RL策略；
  2. 对当前指令，语言模型生成高层计划；
  3. RL代理基于该计划在环境交互中训练，积累轨迹数据；
  4. 评估代理执行结果，计算反馈（如成功率、偏差度）；
  5. 利用反馈对语言模型进行微调或偏好优化，生成改进后的计划；
  6. 重复步骤2-5，直至收敛或达到性能阈值。

## 3. 实验设计

- **使用场景/数据集**：在“具有丰富动态性和随机性”的环境中进行验证（论文未明确给出具体环境名称，但从任务类别推断应为类似机器人控制或导航等组合式指令跟随场景）。
- **Benchmark**：与基线方法对比，基线包括依赖预定义子任务的传统方法（如基于规则或静态计划的方法）。
- **对比方法**：未列出具体算法名称，但明确提及“基线方法”依赖预定义的子任务。
- **评价指标**：指令遵循度（adherence to instructions）、泛化能力（在未见指令上的表现）。

## 4. 资源与算力

- **论文未明确说明**：文中没有提及使用的GPU型号、数量或训练时长等具体算力资源。因此无法从原文获得相关细节，需要后续作者补充或自行估计。但在实际复现时，通常需要单/多张GPU（如V100/A100）进行数天的迭代训练。

## 5. 实验数量与充分性

- **实验数量**：论文仅提供了概括性结果，未列出多组实验的详细数据（如不同环境、不同随机种子、消融实验等）。根据摘要判断，至少进行了：
  - 主实验：在动态随机环境中对比基线。
  - 泛化实验：评估未见指令上的表现。
- **充分性评估**：由于缺少消融实验（如去掉自学习机制、去掉RL反馈、单独LM或单独RL等）和统计显著性分析，实验充分性有限。结论基于单一场景或少数案例，客观性存疑。不过，在ICLR等顶会要求下，可能正文中有更详细实验，但本处仅提供摘要信息。

## 6. 主要结论与发现

- **主要发现**：自引导计划提取与RL共训能有效提升指令跟随性能。
- **具体结论**：
  - 代理对指令的遵循度显著高于依赖预定义子任务的基线方法；
  - 表现出强大的泛化能力，能够应对之前未见过的指令；
  - 整个流程无需人工标注，降低了数据成本。

## 7. 优点

- **方法新颖**：将自学习计划生成与RL反馈结合，形成自引导闭环，避免了人工预定义子任务。
- **实用性**：适应动态随机环境，提升实际部署的鲁棒性。
- **泛化能力**：能处理未见指令，表明框架具备一定迁移能力。
- **自动化**：减少人工干预，降低开发成本。

## 8. 不足与局限

- **实验覆盖不足**：未提供具体环境名称、数据集规模、多场景验证结果，结论推广性需更多证据支持。
- **缺乏消融分析**：未量化各组件（自学习机制、RL反馈、迭代次数等）的贡献，难以判断核心瓶颈。
- **偏差风险**：若反馈设计不合理，可能导致语言模型陷入局部最优计划；RL代理对计划敏感，可能引发协同失败。
- **应用限制**：目前仅验证于特定指令跟随任务，对更复杂、长期依赖的任务效果未知；计算成本可能较高（迭代共训需要多次模型更新）。
- **未开源或复现细节不足**：未提供算法伪代码、超参数设置、环境配置等，复现困难。

（完）
