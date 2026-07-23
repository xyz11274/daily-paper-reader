---
title: Building Learning Context For Autonomous Agents Through Generative Optimization
title_zh: 通过生成式优化构建自主代理的学习环境
authors: "Allen Nie, Xavier Daull, Zhiyi Kuang, Abhinav Akkiraju, Anish Chaudhuri, Max Piasevoli, Ryan Rong, YuCheng Yuan, Prerit Choudhary, Shannon Xiao, Rasool Fakoor, Adith Swaminathan, Ching-An Cheng"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=wtLyksjIdl"
tags: ["query:ase"]
score: 7.0
evidence: 使用生成式优化来演化代理行为
tldr: 构建自主学习的代理面临行为不稳定和可解释性差的问题。本文揭示使用LLM作为优化器（生成式优化）时，代理学习任务存在欠定问题，并提出将行为逻辑（工作流）与更新逻辑（优化器）分离的设计范式，使代理能更稳定、可控地基于经验演化行为。这一方法为自进化代理提供了系统化的优化框架。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有LLM代理学习方法存在行为不稳定、可解释性差的问题。
method: 将代理设计分为工作流和优化器两部分，利用生成式优化实现可控的行为演化。
result: 分析表明该分离设计能提升自进化代理的稳定性和可控性。
conclusion: 生成式优化为代理自进化提供了系统化的设计原则。
---

## Abstract
Building intelligent agents that learn involves designing systems that can evolve their behavior based on experiences. While early approaches to large language models (LLMs) agent learning relied mostly on structured memory and in-context learning, they often led to behavioral instability, poor interpretability, and difficulty in control.
Recent success in generative optimization, where an LLM is used as an optimizer, has shown the possibility of creating autonomous software agents. By separating behavior logic (workflow) and how that logic is updated (optimizer), the agent designer can exhibit more control over the agent.
In this work, we show the surprising fact that the agent learning problem is \textit{under-specified} with the generative optimization framework. If we want an agent to learn the right behavior, we must set up the right context that will induce such behavior. 
We investigate three types of software engineering problems that span data science, computer security, game playing, and question answering. We show that the original generative optimization framework can only learn robustly under one of the three settings. To address the issue, we propose to construct a meta-graph through templates to introduce the right learning context to an LLM optimizer. With this addition, we demonstrate that defining the right learning context enables agents to discover behaviors aligned with the designer's objectives. In particular, we show the first known result of using generative optimizers to learn executable programs that play Atari games, where the resulting agents achieve performance comparable to deep reinforcement learning while requiring 50%-90% less training time.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：基于大语言模型（LLM）的自主代理在从经验中学习时，面临行为不稳定、可解释性差、难以控制等挑战。
- **背景**：早期LLM代理学习方法依赖结构化记忆和上下文学习，但未能实现稳定、可控的行为演化。近期生成式优化（generative optimization）——即用LLM作为优化器——展示了创建自主软件代理的潜力。
- **研究动机**：本文揭示了一个令人惊讶的现象——在生成式优化框架下，代理学习问题本质上是**欠定**的（under-specified）。即若要让代理学到正确行为，必须设置恰当的“学习环境”（learning context），否则优化器无法可靠地诱导期望行为。为此，作者提出通过构建元图（meta-graph）来引入正确的学习环境，从而提升代理自进化过程的稳定性和可控性。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：将代理的行为逻辑（工作流，workflow）与更新逻辑（优化器，optimizer）分离，形成“工作流-优化器”设计范式。代理通过生成式优化（LLM作为优化器）基于经验演化行为，但需要定义正确的学习环境来约束优化过程。
- **关键技术细节**：
  - **元图（Meta-Graph）的构建**：通过模板（templates）自动生成结构化的学习环境，为LLM优化器提供明确的上下文信息，使优化器能够理解代理的目标、当前状态和演化方向。
  - **三类型问题分析与修正**：作者将软件工程问题（数据科学、计算机安全、游戏、问答）归纳为三种设置，发现原始生成式优化仅在一种设置下能鲁棒学习。通过元图引入学习环境后，其余两种设置也实现了有效学习。
  - **算法流程**（文字说明）：
    1. 定义代理的基本工作流（如：观察→推理→行动）。
    2. 设计一个LLM作为优化器，输入代理的经验数据（如成功/失败轨迹）和当前工作流。
    3. 构建元图模板，将任务目标、历史行为模式、评价指标等结构化信息整合进优化器的提示中。
    4. 优化器输出更新后的工作流（如修改推理规则、行动选择逻辑），从而演化代理行为。
    5. 迭代上述过程，直到代理达到性能要求或收敛。

## 3. 实验设计
- **数据集/场景**：覆盖四类软件工程问题：
  - 数据科学
  - 计算机安全
  - 游戏（包括Atari游戏）
  - 问答（Question Answering）
- **Benchmark**：
  - 对于Atari游戏：与**深度强化学习（Deep RL）** 进行性能对比。
  - 其他场景：未明确说明具体基准，但提到了三种设置下的鲁棒性分析。
- **对比方法**：
  - 原始生成式优化（无元图）作为基线。
  - 深度强化学习（仅在Atari游戏中作为对比）。
  - 未提及其他自进化代理方法。

## 4. 资源与算力
- **未明确说明**：论文中未提及使用的GPU型号、数量、训练时长等具体算力信息。仅提到Atari游戏实验中，所提方法相比深度强化学习**减少50%-90%的训练时间**，但未给出绝对训练时长或硬件配置。

## 5. 实验数量与充分性
- **实验数量**：
  - 针对三类设置（数据科学、计算机安全、游戏、问答）进行了鲁棒性分析，表明原始框架只在其中一类有效。
  - 设置了元图后的对比实验（展示了改善效果）。
  - 在Atari游戏上展示了首个用生成式优化学习可执行程序的结果，并与Deep RL比较。
- **充分性评估**：
  - **优点**：覆盖了多个领域，包含跨任务类型验证，且指出自我分析（self-analysis）表明原始框架的局限性。
  - **不足**：实验数量相对有限，未报告消融实验（如不同元图设计的影响）、统计显著性检验、多轮随机种子重复等细节。对于“三种设置”的具体划分和每个设置下的任务数量也未详述。此外，仅在Atari游戏上与Deep RL对比，其他场景缺乏SOTA基线。整体实验设计较为初步，但足以支持该论文的核心论点和设计原则。

## 6. 主要结论与发现
1. **核心发现**：代理学习问题在生成式优化框架下是**欠定的**——优化器需要正确的学习环境才能诱导出目标行为。
2. **解决方案有效性**：通过构建元图模板引入学习环境，可使代理发现与设计者目标一致的行为。
3. **首个成果**：首次使用生成式优化器学习可执行程序来玩Atari游戏，且性能与深度强化学习相当。
4. **效率提升**：所需训练时间比深度强化学习减少50%-90%。
5. **设计范式**：将工作流与优化器分离，是构建自进化代理的系统化设计原则。

## 7. 优点
- **方法创新性**：揭示了生成式优化中“学习环境”的关键作用，并提出元图构建这一可操作的解决方案；分离工作流与优化器提升了可控性。
- **实验覆盖广度**：涉及数据科学、安全、游戏、问答等多个领域，验证了跨任务适用性。
- **效率优势**：在Atari游戏上大幅降低训练时间，且性能可比Deep RL，具有实际应用潜力。
- **理论洞察**：基于欠定问题的分析，为后续研究提供了理论指导。

## 8. 不足与局限
- **实验细节缺失**：未报告算力消耗、消融实验、统计显著性检验、多个随机种子重复，影响结论的稳健性。
- **基准对比不足**：除Atari外，其他场景缺少与SOTA（如强化学习、进化算法、其他自进化LLM代理方法）的对比，无法判定相对优势。
- **元图设计依赖**：元图模板如何自动生成或手工设计未详细说明，可能导致复现困难或引入设计偏差。
- **任务规模有限**：实验任务多为简单或中等复杂度问题，未在大规模真实世界应用（如机器人控制、复杂决策）上验证。
- **欠定问题普适性**：仅针对生成式优化框架下的三类设置分析，结论是否适用于其他自进化范式的代理有待进一步验证。

（完）
