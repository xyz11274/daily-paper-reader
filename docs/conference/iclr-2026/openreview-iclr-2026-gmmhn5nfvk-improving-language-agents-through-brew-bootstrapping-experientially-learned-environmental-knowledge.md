---
title: "Improving Language Agents through BREW: Bootstrapping expeRientially-learned Environmental knoWledge"
title_zh: 通过BREW改进语言代理：引导经验性环境知识
authors: "Shashank Kirtania, Param Biyani, Priyanshu Gupta, Yasharth Bajpai, Roshni Iyer, Sumit Gulwani, Gustavo Soares"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=gmmHn5nFvK"
tags: ["query:ase"]
score: 8.0
evidence: 引导经验性知识用于代理改进
tldr: 本文针对现有模型权重优化方法(如PPO)计算开销大、难以解释和增量改进的问题，提出BREW框架。该框架通过构建和精炼代理从环境中习得的经验性结构化记忆来优化代理行为。实验表明，结构化记忆可作为代理持续学习的有效替代方案，提高了可解释性和增量改进能力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有模型权重优化方法(如PPO)计算开销大且难以解释，需要更高效的代理改进途径。
method: 提出BREW框架，通过构建和精炼代理从环境中习得的经验性结构化记忆来优化代理行为。
result: 提供了除权重优化外的另一种代理优化路径，提高了可解释性和增量改进能力。
conclusion: 经验性结构化记忆可作为代理持续学习的有效替代方案。
---

## Abstract
Large Language Model (LLM)-based agents are increasingly applied to tasks requiring structured reasoning, tool use, and environmental adaptation, such as data manipulation, multistep planning, and computer-use automation. However, despite their versatility, current training paradigms for model weight optimization methods, like PPO and GRPO, remain relatively impractical with their high computational overhead for rollout convergence. In addition, the resulting agent policies are difficult to interpret, adapt, or incrementally improve. To address this, we investigate creating and refining structured memory of experiential learning of an agent from its environment as an alternative route to agent optimization. We introduce \textbf{BREW} (Bootstrapping expeRientially-learned Environmental knoWledge), a framework for agent optimization for downstream tasks via KB construction and refinement. In our formulation, we introduce an effective method for partitioning agent memory for more efficient retrieval and refinement. BREW uses task graders and behavior rubrics to learn insights while leveraging state-space search for ensuring robustness from the noise and non-specificity in natural language. Empirical results on real world, domain-grounded benchmarks---OSWorld and $\tau^2$Bench---show BREW achieves 10--20\% improvement in task precision, 10--15\% reduction in API/tool calls leading to faster execution time, all while maintaining computational efficiency on par with base models. Unlike prior work where memory is treated as static context, we establish the KB as a modular and controllable substrate for agent optimization---an explicit lever for shaping behavior in a transparent, interpretable, and extensible manner.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前基于大型语言模型（LLM）的智能体（agent）在结构化推理、工具使用和环境适应等任务中表现出色，但其优化方法（如PPO、GRPO等权重优化方法）存在两大缺陷：① 计算开销巨大，尤其是在策略收敛阶段需要大量rollout；② 优化后的策略难以解释、难以增量改进或适应新任务。
- **研究动机**：探索一种替代方案，即通过构建和精炼智能体从环境中经验学习到的**结构化记忆**，而非直接修改模型权重，来实现对智能体行为的透明、可解释且低成本的优化。
- **整体含义**：提出名为**BREW**（Bootstrapping expeRientially-learned Environmental knoWledge）的框架，旨在将智能体的经验转化为可检索、可更新、可解释的知识库（KB），从而成为权重优化之外的另一条高效路径。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将智能体在环境交互中获得的经验性知识系统化，形成结构化记忆（知识库），并通过任务评分器（task graders）和行为准则（behavior rubrics）进行精炼，同时利用状态空间搜索（state-space search）来增强鲁棒性，克服自然语言噪声和非特异性问题。
- **关键技术细节**：
  - **记忆分区策略**：提出一种有效的记忆分区方法，将智能体记忆划分为更小的模块，便于高效检索和增量精炼。
  - **知识库构建与精炼**：通过任务执行反馈，自动生成或更新KB条目；利用行为准则引导记忆的修正方向。
  - **状态空间搜索**：在自然语言知识中引入搜索机制，确保精炼后的知识在不确定性环境下依然稳定可靠。
  - **模块化与可控性**：KB被视为独立于模型权重的可控组件，可随时添加、删除或修改，从而透明地调整智能体行为。

### 3. 实验设计：数据集/场景、benchmark、对比方法

- **使用的数据集/场景**：两个真实世界领域基准——**OSWorld**（操作系统层面的计算机任务）和 **τ²Bench**（多步规划和工具使用任务）。
- **Benchmark**：直接在两个基准上评估任务完成精度、API/工具调用次数和执行时间。
- **对比方法**：摘要未明确列出具体的基线方法，但提及与“base models”比较（即未使用BREW的原始模型）。推测对比了无记忆增强的LLM智能体以及可能的静态上下文记忆方法。

### 4. 资源与算力

- 论文中**未明确说明**使用的GPU型号、数量或训练时长等具体算力资源。仅提及BREW在计算效率上与基础模型持平（computational efficiency on par with base models），暗示无需额外的大规模权重训练。

### 5. 实验数量与充分性

- **实验组数**：从摘要看，主要在两个基准（OSWorld和τ²Bench）上进行了实验，可能包含多组不同任务难度的对比。未明确说明消融实验的具体数量，但“behavior rubrics”“state-space search”等组件可能通过消融验证必要性。
- **充分性与公平性**：实验覆盖了真实世界任务，且结果改善显著（10-20%精度提升，10-15%调用减少）。但缺乏与现有权重优化方法（如PPO）的直接对比，也未报告统计显著性检验或多次运行的标准差，可能降低了说服力。

### 6. 论文的主要结论与发现

- BREW框架在不需要高成本权重更新的前提下，通过构建和精炼经验性结构化记忆，使智能体在任务精度上提升10-20%，同时减少10-15%的API/工具调用，执行速度更快。
- 知识库作为模块化、可控的优化基底，能够以透明、可解释、可扩展的方式塑造行为，远超“静态上下文”记忆的局限。
- 经验性结构化记忆可作为模型权重优化的一种有效替代或补充，尤其适用于持续学习和增量改进场景。

### 7. 优点：方法或实验设计上的亮点

- **方法亮点**：
  - 提出了“经验知识引导”的新范式，绕过了权重优化的高成本和不可解释性。
  - 引入记忆分区与状态空间搜索结合，提升鲁棒性和检索效率。
  - 知识库独立于模型，便于集成到不同LLM后端，且支持手工干预。
- **实验设计亮点**：
  - 选择两个具有代表性的真实世界基准（OSWorld和τ²Bench），覆盖多步骤规划与工具使用。
  - 不仅评估精度，还衡量调用次数和执行时间，体现实际部署价值。

### 8. 不足与局限

- **实验覆盖不足**：仅两个benchmark，且未与PPO、GRPO等主流权重优化方法进行直接比较，无法判断“替代”路径的相对优势。
- **偏差风险**：可能只在特定类型的任务（如结构化操作）上有效，对开放对话、创造性任务等泛化性未知。
- **应用限制**：记忆的构建依赖任务评分器和行为准则，这些规则的设计可能引入人工偏差；且状态空间搜索在复杂任务中成本可能上升。
- **可复现性**：未提及开源代码或详细超参数，资源消耗细节缺失，外部复现困难。
- **统计严谨性**：未报告多次实验的均值和方差，结果的稳定性和显著性未经检验。

（完）
