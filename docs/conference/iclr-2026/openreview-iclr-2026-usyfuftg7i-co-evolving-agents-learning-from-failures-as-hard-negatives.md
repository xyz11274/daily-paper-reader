---
title: "Co-Evolving Agents: Learning from Failures as Hard Negatives"
title_zh: 共进化代理：从失败中作为硬负样本学习
authors: "Yeonsung Jung, Trilok Padhi, Sina Shaham, Dipika Khullar, Joonhyun Jeong, Ninareh Mehrabi, Eunho Yang"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=usYfUfTG7I"
tags: ["query:ase"]
score: 8.0
evidence: 共进化代理从失败中作为硬负样本学习
tldr: 自改进代理常依赖预测轨迹与真实轨迹的偏好优化，但真实轨迹稀缺。本文提出共进化框架，让代理从自身失败中作为硬负样本学习，通过迭代生成和改进轨迹，无需大量真实数据。在多个任务上，该方法比监督微调和标准偏好优化显著提升性能，实现了更高效的自进化。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 自改进代理过度依赖稀缺的真实轨迹数据。
method: 代理自主生成轨迹，并将失败实例作为硬负样本用于偏好优化，迭代改进。
result: 在多个任务上超过监督微调和标准偏好优化方法。
conclusion: 利用失败作为硬负样本能有效提升自改进代理的性能。
---

## Abstract
The rapid progress of large foundation models has accelerated the development of task-specialized agents across diverse domains. However, the effectiveness of agents remains tightly coupled with the quality of training data, while curating task-specific datasets remains costly and often infeasible in real-world scenarios. 
Recent work has explored self-improving agents that autonomously generate, refine, and re-train on their own trajectories. A prominent line of approaches further leverages preference optimization by pairing predicted trajectories with scarce ground-truth trajectories, enabling agents to learn directly from their own failures.
While these methods outperform supervised fine-tuning, their heavy reliance on predicted trajectories under limited ground-truth supervision leaves them prone to overfitting.
To address this, we propose a co-evolving agents framework in which a target agent improves jointly with an auxiliary failure agent. The failure agent learns through preference optimization over failure trajectories from both the target and itself, thereby generating hard negatives that are close to success yet remain failures. 
Incorporating these informative hard negatives into the target agent’s optimization sharpens decision boundaries and enhances generalization.
Our comprehensive analysis and experiments across benchmark datasets show that our method not only show improved performance but also highlights that failures, instead of being used as-is, can be systematically transformed into structured and valuable learning signals in self-improving agents.

---

## 论文详细总结（自动生成）

## 论文要点

### 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：大型基础模型的进步推动了任务特定智能体的开发，但其性能高度依赖训练数据的质量。在现实场景中，手动收集特定任务的高质量轨迹数据（尤其是真实轨迹）成本高昂且往往不可行。
- **问题背景**：现有自改进智能体通过自主生成轨迹并利用偏好优化（将预测轨迹与少量真实轨迹配对）来学习。但这些方法过度依赖有限真实轨迹下的预测轨迹，容易导致过拟合。
- **本文目标**：提出一种新的共进化框架，让智能体能够从自身的失败中学习，将失败转化为结构化的硬负样本，从而在无需大量真实数据的前提下提升泛化能力。

### 2. 方法论：核心思想与关键技术细节
- **核心思想**：构建两个共进化的智能体——目标智能体（target agent）和辅助失败智能体（failure agent）。失败智能体通过偏好优化学习来自目标智能体和自身的失败轨迹，生成“硬负样本”（hard negatives），即那些接近成功但仍然是失败的轨迹。将这些信息丰富的硬负样本纳入目标智能体的优化过程，可以锐化决策边界并增强泛化。
- **关键技术细节**：
  - 目标智能体：自主生成轨迹并不断改进。
  - 辅助失败智能体：接收目标智能体的失败轨迹以及自身生成的失败轨迹，通过偏好优化学习如何生成更“有挑战性”的失败案例。
  - 硬负样本的生成：失败智能体输出接近成功边界的失败轨迹，作为目标智能体训练中的负样本。
  - 训练流程：迭代进行——目标智能体生成轨迹→失败智能体学习并生成硬负样本→目标智能体利用硬负样本进行偏好优化→重复迭代。
- **公式/算法流程**：文中未提供具体公式，但整体流程可概括为：
  1. 初始化目标智能体 $T_0$ 和失败智能体 $F_0$。
  2. 对于每一轮 $t$：
     - $T_t$ 生成一批轨迹，标记成功/失败。
     - 将失败轨迹送入 $F_t$，$F_t$ 通过偏好优化（如DPO）学习区分自身失败与$T_t$失败，生成新的硬负样本。
     - 将硬负样本与原始成功轨迹组合，对 $T_t$ 进行偏好优化，更新为目标智能体 $T_{t+1}$。
     - 同时更新失败智能体 $F_{t+1}$。

### 3. 实验设计
- **使用的数据集/场景**：论文提到在“benchmark datasets”上进行了实验，但未明确列举具体数据集名称（可能为常见的智能体任务如WebShop、ALFWorld、Minecraft等，但文本未给出）。
- **基准（Benchmark）**：对比了监督微调（SFT）和标准偏好优化（如DPO）方法。
- **对比方法**：自改进基线（仅用预测轨迹偏好优化）、监督微调（SFT）、标准偏好优化（如DPO）。
- **评估指标**：未具体描述，但暗示性能提升（improved performance）。

### 4. 资源与算力
- **明确信息**：论文中未提及使用的GPU型号、数量、训练时长等算力信息。
- **说明**：可能是由于论文在ICLR评审中被拒，且为早期版本，未包含实验资源细节。需要指出这一点。

### 5. 实验数量与充分性
- **实验数量**：文中描述为“comprehensive analysis and experiments across benchmark datasets”，但未给出具体实验组数。推测至少包含2-3个基准数据集的对比实验，以及消融实验（如去除失败智能体、仅用自身失败等），但缺乏量化数字。
- **充分性评价**：从摘要看，实验覆盖了多个基准任务，并与SFT、标准偏好优化对比，但缺少详细的统计显著性分析、超参数敏感性、以及不同失败生成策略的对比。因此，实验的充分性和客观性存在一定不足，尤其在具体数据集名称和结果展示上不够透明。

### 6. 主要结论与发现
- 所提出的共进化代理框架在多个任务上显著优于监督微调和标准偏好优化方法。
- 失败轨迹经过系统转化（成为硬负样本）后，能够作为有价值的学习信号，提升自改进智能体的性能。
- 利用失败作为硬负样本能有效缓解对真实轨迹的过度依赖，提高泛化能力。

### 7. 优点
- **新颖性**：将失败转化为硬负样本的核心思想具有创意，区别于直接使用失败作为负样本的简单方式，通过辅助失败智能体生成更困难的负样本。
- **数据效率**：不依赖大量真实轨迹，只需要初始少量成功/失败数据即可启动自改进循环。
- **通用性**：框架可以适用于多种任务智能体，具有潜在迁移价值。

### 8. 不足与局限
- **实验细节缺失**：未提供具体数据集、结果表格、误差线等，难以评估方法的实际性能提升幅度和统计可靠性。
- **算力与复现**：未注明硬件配置，不利于复现。
- **消融分析不足**：没有系统分析失败智能体设计的各个组件（如用不同偏好优化算法、不同生成数量）的影响。
- **偏差风险**：如果初始失败轨迹分布偏斜，失败智能体可能生成偏向性硬负样本，导致目标智能体学习偏差。
- **应用限制**：方法假设可以不断生成失败轨迹，对于某些高风险场景（如自动驾驶）可能不适用；且迭代计算成本可能较高。

（完）
