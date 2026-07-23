---
title: Automated Stateful Specialization for Adaptive Agent Systems
title_zh: 自适应智能体系统的自动化有状态专业化
authors: "Myan Vu, Harrish Ayyanar, PANG JIANG, Anwiketh Reddy, Mayank Goel"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=UESTP6dR1K"
tags: ["query:ase"]
score: 8.0
evidence: 创建有状态的专业智能体，无需人工干预即可积累知识并适应
tldr: 当前自动智能体设计要么产生静态工作流，要么缺乏深度任务专业化。ASpec框架通过进化搜索自动发现专家原型，并用经验培育其专业知识，实现无需人工干预的持续自适应。其层级化编排机制进一步支持智能体团队根据新任务动态重组，推动了自适应智能体系统的可信自进化。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有自动设计框架在适应性与专业化深度之间存在矛盾。
method: 提出ASpec框架：先通过进化搜索发现专家原型，再用经验培育其能力，最后用层级化编排重组协作。
result: 在多种复杂任务中，ASpec生成的智能体团队能快速适应新场景且无需人工重新设计。
conclusion: 有状态专业化是构建可演化智能体系统的关键方向，ASpec提供了完整生命周期管理。
---

## Abstract
Current automated agent design frameworks produce either static workflows that lack adaptability or per-query optimizers that prevent the accumulation of deep, agent-level task expertise. We propose a new direction that reconciles these paradigms: creating stateful teams of specialist agents that accumulate knowledge over time and can be reconfigured for novel tasks entirely without human intervention. To this end, we introduce \textsc{ASpec}, a framework that manages this full agent lifecycle by first autonomously \textbf{discovering} specialist archetypes via evolutionary search and then \textbf{cultivating} their expertise through experience, mirroring how human experts learn through practice and reflection. We further introduce a lightweight hierarchical control policy, "retain-then-escalate," which governs when to leverage the established agent system versus when to adapt its structure. Through comprehensive experiments, we demonstrate that this approach leads to significant performance gains on expert-level scientific benchmarks like GPQA while matching the state-of-the-art on broader domain tasks, demonstrating a promising path toward agent systems that are simultaneously expert, adaptive, and efficient. We will release the code at https://github.com/myanvoos/ASpec.

---

## 论文详细总结（自动生成）

# 论文总结：自动化有状态专业化智能体系统

## 1. 核心问题与整体含义（研究动机和背景）
- **核心冲突**：现有自动化智能体设计方法存在两难困境——要么产生**静态工作流**（缺乏对新任务的适应性），要么采用**每查询优化器**（每轮独立优化，无法积累深度、智能体级别的任务专长）。
- **整体目标**：提出一种新的范式——“有状态的专业化智能体团队”，使其能够随时间积累知识，并能在**无需人工干预**的情况下为全新任务动态重组，实现可信的自进化。
- **意义**：填补自适应与专业化深度之间的矛盾，推动智能体系统从人工设计走向自动化持续演化。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **框架名称**：ASpec（Automated Stateful Specialization）
- **核心思想**：模拟人类专家通过实践和反思学习的过程，管理智能体系统的完整生命周期（发现 → 培育 → 编排）。
- **关键技术细节**：
  - **第一阶段：自主发现专家原型（Discover）**  
    通过**进化搜索**（如遗传算法或神经架构搜索变体）在任务空间中找到有潜力的智能体原型（即角色的基本行为模式）。
  - **第二阶段：经验培育专业知识（Cultivate）**  
    让发现的专家原型在实际执行任务中**积累经验**（类似在线学习或强化学习），通过反思机制不断更新其内部状态（知识库、策略参数等），形成深度专长。
  - **第三阶段：层级化动态编排（Orchestrate）**  
    引入轻量级层级控制策略 —— **“先保留，再升级”（Retain-then-Escalate）**。该策略决定何时沿用已有智能体系统（保留现有结构），何时需要调整结构（升级或重组），从而平衡稳定性和适应性。
- **算法流程文字描述**：
  - 初始化：随机生成一组候选智能体原型。
  - 进化搜索：在验证任务上评估原型的性能，选择表现优异的原型进行交叉/变异，迭代若干代后得到专家原型池。
  - 培育：每个专家原型在新任务上执行并收集反馈（例如成功率、错误分析），更新其内部记忆/参数。
  - 编排：给定新任务，先尝试用当前专家团队解决；若性能低于阈值，则触发升级操作（例如将失败案例用于培育，或添加/替换专家）。

## 3. 实验设计：数据集、基准、对比方法
- **数据集/任务**：
  - **专家级科学基准**：GPQA（Graduate-Level Physics QA）—— 高层次物理问答，测试智能体的专业知识深度。
  - **更广泛领域任务**：未在摘要中具体列出，但注明“匹配更广泛领域任务上的最先进水平”，推测包括通用问答、代码生成、数学推理等常见基准（如MATH、HumanEval等，需原文确认）。
- **基准对比**：
  - 对比方法：当前自动智能体设计框架（静态工作流型）和每查询优化型（如AutoGPT、AgentGPT等变种）以及SOTA方法（未列具体名称，摘要称“match state-of-the-art on broader domain tasks”）。
- **评价指标**：准确率、成功率、自适应效率（任务切换时的性能损失或恢复时间）等。

## 4. 资源与算力
- **未明确说明**：
  - 摘要及元数据中未提及GPU型号、数量、训练时长、参数量等具体算力信息。
  - 仅提到“lightweight hierarchical control policy”，暗示计算开销可能较小，但无量化数据。

## 5. 实验数量与充分性
- **实验数量**：仅从摘要可知进行了“comprehensive experiments”，具体组数未列明。推测包含：
  - 主要实验结果（GPQA + 广泛任务）至少两组。
  - 消融实验（例如去掉进化搜索/培育/编排模块的对比）可能涉及。
  - 可能包含不同规模的智能体团队、不同更新频率等超参数敏感性分析。
- **充分性评估**：
  - **优点**：选择GPQA作为专家级基准具有难度，可验证专业深度；同时匹配通用SOTA，验证泛化性。
  - **不足**：缺乏具体实验配置（如种子数、重复次数、统计显著性检验），无法判断结果的鲁棒性；对比方法未公开列出，公平性难以完全确认。但从ICLR-2026接收来看，实验设计应达到基本要求。

## 6. 论文的主要结论与发现
- ASpec在GPQA上取得显著性能提升（显著优于现有方法），证明有状态专业化能培养出深度任务专家。
- 在更广泛领域任务上，ASpec与当前最先进方法持平或略优，说明方法未牺牲通用性。
- 层级控制策略“retain-then-escalate”有效平衡了系统稳定性和自适应效率，无需人工重新设计即可应对新场景。
- **核心发现**：有状态专业化是构建可演化智能体系统的关键方向，ASpec提供了完整的生命周期管理方案。

## 7. 优点：方法或实验设计上的亮点
- **全自动化**：无需人工标注专家知识或设计角色，从零开始自主发现并培育专家。
- **持续自适应**：智能体团队可动态重组，无需重新训练，适合开放世界动态任务。
- **轻量层级控制**：避免频繁的全系统更新，计算开销低，适合实时部署。
- **模拟人类学习过程**：进化搜索对应创新，经验培育对应练习，编排对应决策，解释性强。
- **代码开源**（已承诺），促进可复现性。

## 8. 不足与局限
- **实验覆盖有限**：仅公开了一个专家级基准（GPQA），更多领域的细节（如Robotics、多智能体协作）未提及。
- **算力需求不透明**：无资源消耗报告，难以判断实际部署成本；进化搜索阶段可能仍需较大计算资源。
- **偏差风险**：若只针对特定类型任务（如问答）进行搜索，可能对其他模态（如代码、图文）效果未知。
- **应用限制**：依赖任务反馈的质量（如GPQA的答案评估），对于弱反馈或无反馈场景（如开放探索）可能效果打折。
- **可扩展性**：智能体团队规模增大时，层级编排的延迟和策略性能未讨论。

（完）
