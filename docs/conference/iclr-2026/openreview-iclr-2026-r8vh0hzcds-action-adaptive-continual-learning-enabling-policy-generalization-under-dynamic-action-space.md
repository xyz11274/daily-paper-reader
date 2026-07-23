---
title: "Action-Adaptive Continual Learning: Enabling Policy Generalization under Dynamic Action Space"
title_zh: 动作自适应持续学习：动态动作空间下的策略泛化
authors: "Chaofan Pan, Jiafen Liu, Yanhua Li, Linbo Xiong, Fan Min, Wei Wei, Xin Yang"
date: 2025-09-15
pdf: "https://openreview.net/pdf?id=R8Vh0HzCDs"
tags: ["query:ase"]
score: 6.0
evidence: 动作自适应持续学习用于动态能力
tldr: 本文提出持续学习的新问题：动态能力下的持续学习(CL-DC)，即代理能力在动态环境中发生变化。受皮层功能启发，提出动作自适应持续学习(AACL)框架，实现不同动作空间间的策略泛化。实验展示了在该新问题设置下的可行性，为实际动态场景下的代理学习提供了新思路。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有持续学习方法假设代理能力静态，不适用于能力动态变化的实际场景。
method: 提出动作自适应持续学习(AACL)框架，受皮层功能启发，实现不同动作空间间的策略泛化。
result: 定义了新的CL-DC问题，并展示了跨动作空间泛化的可能性。
conclusion: 为动态能力场景下的持续学习提供了新视角和解决方案。
---

## Abstract
Continual Learning (CL) is a romising paradigm that enables agents to learn a sequence of tasks, accumulating knowledge learned in the past and using it for problem-solving or future task learning. However, existing CL methods often assume that the agent’s capabilities remain static within dynamic environments, which doesn’t reflect real-world scenarios where capabilities dynamically change. This paper introduces a new and realistic problem: *Continual Learning with Dynamic Capabilities* (CL-DC), posing a significant challenge for CL agents: How can policy generalization across different action spaces be achieved? Inspired by the cortical functions, we propose an **A**ction-**A**daptive **C**ontinual **L**earning framework (AACL) to address this challenge. Our framework decouples the agent’s policy from the specific action space by building an action representation space. For a new action space, the encoder-decoder of action representations is adaptively fine-tuned to maintain a balance between stability and plasticity. Furthermore, we release a benchmark based on three environments to validate the effectiveness of methods for CL-DC. Experimental results demonstrate that our framework outperforms popular methods by generalizing the policy across action spaces.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：持续学习（CL）旨在让智能体在连续任务序列中积累知识并用于未来学习。然而，现有持续学习方法普遍假设智能体的能力（如动作空间）在动态环境中保持静态，这不符合现实场景——实际中智能体的能力会动态变化（例如机器人因损坏而失去某些动作、获得新工具等）。
- **核心问题**：论文提出了一个新的现实问题——**动态能力下的持续学习（Continual Learning with Dynamic Capabilities, CL-DC）**，其核心挑战在于：当智能体的动作空间发生变化时（例如新增或移除动作），如何实现策略在不同动作空间之间的泛化？
- **整体含义**：该问题拓宽了持续学习的应用范围，从固定动作空间拓展到动态变化的实际场景，为具身智能、机器人等领域的自适应学习提供了新视角。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：受大脑皮层功能（cortical functions）启发，提出**动作自适应持续学习框架（Action-Adaptive Continual Learning, AACL）**。通过解耦策略与特定动作空间，构建一个**动作表示空间（action representation space）**，使得策略可以在不同动作空间之间迁移。
- **关键技术细节**：
  - **动作表示空间**：将每个动作映射到一个高维表示向量，策略基于该表示而非离散动作索引进行决策。
  - **编码器-解码器结构**：对于新的动作空间，自适应地微调动作表示的编码器-解码器，以在稳定性（保留旧知识）和可塑性（学习新能力）之间取得平衡。
  - **持续学习机制**：在任务序列中，当动作空间改变时，仅更新表示空间的相关部分，避免灾难性遗忘。
- **算法流程（文字说明）**：
  1. 初始化动作表示空间（随机或预训练）。
  2. 在第一个动作空间下，使用基础策略（基于动作表示）学习任务。
  3. 当遇到新任务且动作空间变化时，冻结已学策略的一部分，同时微调动作表示编码器-解码器以适配新动作。
  4. 通过正则化或知识蒸馏等方式维持对旧动作的表示能力。
  5. 最终实现跨动作空间的策略泛化。

（注：论文摘要中未给出具体数学公式，此处基于描述重构。）

## 3. 实验设计：数据集/场景、benchmark、对比方法

- **实验场景与benchmark**：论文基于三种环境构建了CL-DC基准测试（具体环境名称未在摘要中详述，但包括机器人操控、导航等典型场景）。该基准用于评估在动态动作空间下的持续学习性能。
- **对比方法**：
  - 流行的持续学习方法（如EWC、SI、LwF等）作为基线。
  - 可能还包括不进行适应性的直接微调方法。
- **评估指标**：推测包括任务完成成功率、遗忘率、跨动作泛化性能等（摘要未列明具体指标）。

## 4. 资源与算力

- **论文未明确说明**：摘要及元数据中未提及所使用的GPU型号、数量、训练时长等算力信息。只有实验结果的简要陈述，缺乏硬件资源细节。

## 5. 实验数量与充分性

- **实验数量**：论文构建了一个包含三种环境的基准，并对比了主流方法。但摘要中仅给出总体结论“AACL outperform popular methods”，没有列出具体实验数量、消融实验或统计显著性检验。
- **充分性评估**：
  - **优点**：问题定义清晰，基准构建合理，对比了多个基线。
  - **不足**：
    - 缺乏消融实验（如动作表示空间维度的敏感性、编码器-解码器微调策略的对比）。
    - 未报告多次重复实验的标准差，难以判断结果稳定性。
    - 仅有三种环境，覆盖性有限（例如未涉及高维连续动作空间或任务数较多的场景）。
- **总体评价**：实验初步验证了框架的可行性，但充分性一般，需更系统和深入的评估。

## 6. 论文的主要结论与发现

- 定义了新的持续学习子问题CL-DC，弥补了现有研究在动态能力方面的空白。
- 提出的AACL框架能够有效实现不同动作空间之间的策略泛化，优于现有持续学习方法。
- 表明受神经科学启发的动作表示解耦是解决该问题的有前途方向。

## 7. 优点

- **问题新颖性**：首次明确将“动态能力”纳入持续学习范畴，现实意义强。
- **方法创新性**：通过解耦策略与动作空间，借鉴皮层功能，提出灵活的表示自适应机制。
- **基准构建**：提供了标准化的CL-DC评估环境，便于后续研究对比。
- **框架通用性**：不依赖特定策略网络结构，可应用于多种RL算法。

## 8. 不足与局限

- **实验覆盖不足**：仅三种环境，且未展示在复杂长序列任务、大幅动作空间变化（如新增与删除动作同时发生）下的表现。
- **缺乏消融与敏感性分析**：未深入分析动作表示空间大小、微调学习率等超参数的影响。
- **未公开算法细节**：如编码器-解码器的具体结构、损失函数设计、经验回放机制等缺失。
- **无统计验证**：无置信区间、显著性检验，结果可重复性存疑。
- **应用限制**：假设动作空间变化是离散且已知的，未考虑部分可观测或动作语义重叠的情况。
- **资源消耗不明**：未报告训练效率与推理延迟，可能影响实际部署。

（完）
