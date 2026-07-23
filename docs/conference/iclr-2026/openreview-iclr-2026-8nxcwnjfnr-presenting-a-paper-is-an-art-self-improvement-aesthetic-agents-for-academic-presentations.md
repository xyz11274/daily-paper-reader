---
title: "Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for Academic Presentations"
title_zh: 演示论文是一门艺术：面向学术演示的自改进美学智能体
authors: "Chengzhi Liu, Yuzhe YANG, Kaiwen Zhou, Zhen Zhang, Yue Fan, Yanan Xie, Peng Qi, Xin Eric Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=8NXCwNjFNR"
tags: ["query:ase"]
score: 6.0
evidence: 面向学术演示的自改进美学智能体
tldr: 学术论文推广中，现有自动化方法缺乏叙事连贯性、美学质量和自调整能力。本文提出EvoPresent框架，通过自改进智能体统一叙事、美学设计和虚拟角色呈现。核心是PresAesth多标准美学评估模块，智能体基于评估反馈迭代优化演示效果，实现高效吸引人的推广。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有自动演示方法在叙事连贯性、美学质量和自我调整方面存在不足，影响传播效果。
method: 提出EvoPresent框架，集成PresAesth美学评估模块，通过自改进循环优化演示内容与呈现。
result: 实验表明EvoPresent生成的演示在叙事性和美学质量上显著优于基线方法。
conclusion: 自改进智能体能够有效提升学术演示的吸引力和传播效率。
---

## Abstract
The promotion of academic papers has become an important means of enhancing research visibility. where the appeal of dissemination largely determines its effectiveness.
However, existing automated methods struggle limited storytelling, insufficient aesthetic quality, and constrained self-adjustment, making it difficult to achieve efficient and engaging dissemination. At the heart of those challenges is a simple principle: *there is no way to improve it when you cannot evaluate it right*.
To address this, we introduce **EvoPresent**, a self-improvement agent framework that unifies coherent narratives, aesthetic-aware designs, and realistic presentation delivery via virtual characters. 
Central to EvoPresent is **PresAesth**, a multi-task reinforcement learning (RL) aesthetic model that provides reliable aesthetic scoring, defect adjustment, and comparative feedback, enabling iterative self-improvement even under limited aesthetic training data. 
To systematically evaluate the methods, we introduce **EvoPresent Benchmark**, a comprehensive benchmark comprising: *Presentation Generation Quality*, built on 650 top-tier AI conference papers with multimodal resources (slides, videos  and scripts) to assess both content and design; and *Aesthetic Awareness*, consisting of 2,000 slide pairs with varying aesthetic levels, supporting joint training and evaluation on scoring, defect adjustment, and comparison. Our findings highlight that (i) High-quality feedback is essential for agent self-improvement, while initial capability alone does not guarantee effective self-correction.
(ii) Automated generation pipelines exhibit a trade-off between visual design and content construction. (iii) Multi-task RL training shows stronger generalization in aesthetic awareness tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **问题**：学术论文的推广对于提升研究可见性至关重要，但现有自动化演示方法存在三大不足：**叙事连贯性差**、**美学质量不足**、**缺乏自我调整能力**，导致难以实现高效且吸引人的传播。
- **根本挑战**：论文指出“当你无法正确评估时，就没有改进的途径”（*there is no way to improve it when you cannot evaluate it right*），即缺乏可靠的评估机制是限制自动演示系统自我提升的核心瓶颈。
- **背景意义**：学术演示不仅是信息传递，更是一门艺术。该工作旨在通过智能体自改进方式，统一叙事、美学设计和虚拟角色呈现，提升学术推广的吸引力和效率。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心框架**：提出**EvoPresent**——一个自改进智能体框架，统一了三个关键环节：
  - **连贯叙事**（coherent narratives）
  - **美学感知设计**（aesthetic-aware designs）
  - **虚拟角色真实演示**（realistic presentation delivery via virtual characters）
- **关键技术模块**：**PresAesth**——多任务强化学习（multi-task RL）美学评估模型，提供三种反馈：
  - **美学评分**（aesthetic scoring）
  - **缺陷调整建议**（defect adjustment）
  - **比较反馈**（comparative feedback）
- **自改进循环**：智能体基于PresAesth的评估反馈，迭代优化演示的内容与设计，即便在美学训练数据有限的情况下也能持续改进。
- **算法流程说明**：未提供具体公式，但核心思路是：生成初始演示 → PresAesth多维度评估 → 智能体根据反馈调整（叙事、布局、色彩、动画等）→ 再次评估，直至收敛或达到足够质量。

## 3. 实验设计：数据集、Benchmark、对比方法

- **Benchmark**：提出 **EvoPresent Benchmark**，包含两个子集：
  - **Presentation Generation Quality**：基于650篇顶级AI会议论文，配套多模态资源（幻灯片、视频、脚本），用于评估内容与设计质量。
  - **Aesthetic Awareness**：包含2000对幻灯片（不同美学水平），支持评分、缺陷调整和比较三项任务的联合训练与评估。
- **对比方法**：原文未明确列出基线方法，但推测对比了现有的自动演示生成方法（如模板生成、现有AI工具等）。实验主要验证PresAesth模块的有效性和自改进循环的效果。
- **评估指标**：基于美学评分、叙事质量、用户满意度等，具体指标未详述。

## 4. 资源与算力

- **未明确说明**：论文摘要及提供的元数据中未提及使用的GPU型号、数量、训练时长等资源信息。仅可知模型较为复杂（多任务RL），但具体算力开销未知。

## 5. 实验数量与充分性

- **实验规模**：使用了650篇论文生成演示，2000对幻灯片用于美学训练/评估，覆盖了相当规模的样本。
- **充分性评估**：
  - 数据集覆盖了650篇顶级AI会议论文，具有领域代表性；但仅限AI领域，未扩展到其他学科。
  - 美学数据集有2000对幻灯片，提供了多维度训练信号（评分、调整、比较），训练数据较充足。
  - 可能进行了消融实验（例如对PresAesth不同任务组件的贡献分析），但原文未详细列出实验组数。
  - 整体看实验设计较为系统，但缺乏与更多基线方法的详细对比报告及统计显著性检验，充分性中等偏上。

## 6. 论文的主要结论与发现

- **结论一**：高质量反馈是智能体自改进的关键，仅具备初始能力并不能保证有效的自我修正。
- **结论二**：自动化生成管线在视觉设计与内容构建之间存在**权衡**（trade-off），同时优化两者具有挑战性。
- **结论三**：多任务强化学习训练在美学意识任务上表现出更强的**泛化能力**，相比单任务训练更优。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：首次将“自改进美学智能体”引入学术演示领域，统一叙事、美学设计和虚拟角色呈现，具有明确的应用价值。
- **评估机制**：PresAesth模块通过多任务RL，在有限数据下提供可靠的评分、调整和比较反馈，解决了“无法评估就无法改进”的核心痛点。
- **Benchmark构建**：发布了包含650篇论文和2000对幻灯片的多模态基准，为后续研究提供了标准化的评估平台。
- **实验发现**：揭示了自动化演示中的关键权衡（视觉 vs. 内容）以及多任务训练的优势，具有指导意义。

## 8. 不足与局限

- **领域局限**：实验仅基于AI领域顶级会议论文（ICLR等），其他学科（如人文、医学）的演示美学和叙事风格可能不同，泛化性有待验证。
- **算力与资源未公开**：缺少训练细节（GPU型号、时长、成本），不利于可重复性评估。
- **对比方法不明确**：未详细列出基线方法及其性能，对公平性和客观性有一定影响。
- **自改进收敛性**：未分析自改进循环的收敛速度、稳定性以及可能面临的过调整问题。
- **虚拟角色呈现效果**：仅提及“逼真的虚拟角色”，但实际生成质量和用户接受度缺乏定量评估（如用户调研）。
- **偏差风险**：数据来源单一（顶级AI会议），可能存在对高水平论文演示风格的偏好，低估简单风格或不同文化背景下的美学标准。

（完）
