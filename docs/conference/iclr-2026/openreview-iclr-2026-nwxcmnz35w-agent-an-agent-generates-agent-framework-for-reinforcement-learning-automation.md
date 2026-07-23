---
title: "Agent²: An Agent-Generates-Agent Framework for Reinforcement Learning Automation"
title_zh: Agent²：面向强化学习自动化的“智能体生成智能体”框架
authors: "Yuan Wei, Xiaohan Shan, Ran Miao, Jianmin Li"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=nwXCmnZ35w"
tags: ["query:ase"]
score: 7.0
evidence: 完全自主的框架，无需人工干预即可生成强化学习智能体
tldr: 强化学习智能体开发通常需要大量专家知识与迭代调试。Agent²框架通过LLM驱动的生成器智能体自动分析任务并设计可执行智能体，将MDP建模与算法优化分解为两阶段自动化流程，实现了无需人工干预的端到端智能体自动进化，显著降低了RL开发门槛。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: RL智能体开发高度依赖专家手工调参，失败率高且可访问性差。
method: 提出双智能体架构：生成智能体分析任务并设计目标智能体，自动完成MDP建模与算法优化。
result: 成功自动生成可执行RL智能体，在多种环境中完成高效训练与决策。
conclusion: Agent²展示了LLM驱动的自动化RL智能体设计可行性，为智能体自进化提供了全自动基线。
---

## Abstract
Reinforcement learning (RL) agent development traditionally requires substantial expertise and iterative effort, often leading to high failure rates and limited accessibility. This paper introduces Agent$^2$, an LLM-driven agent-generates-agent framework for fully automated RL agent design. Agent$^2$ autonomously translates natural language task descriptions and environment code into executable RL solutions without human intervention. 

The framework adopts a dual-agent architecture: a Generator Agent that analyzes tasks and designs agents, and a Target Agent that is automatically generated and executed. To better support automation, RL development is decomposed into two stages—MDP modeling and algorithmic optimization—facilitating targeted and effective agent generation. Built on the Model Context Protocol, Agent$^2$ provides a unified framework for standardized agent creation across diverse environments and algorithms, incorporating adaptive training management and intelligent feedback analysis for continuous refinement.

Extensive experiments on benchmarks including MuJoCo, MetaDrive, MPE, and SMAC show that Agent$^2$ outperforms manually designed baselines across all tasks, achieving up to 55\% performance improvement with consistent average gains. By enabling a closed-loop, end-to-end automation pipeline, this work advances a new paradigm in which agents can design and optimize other agents, underscoring the potential of agent-generates-agent systems for automated AI development.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：传统的强化学习（RL）智能体开发严重依赖专家知识和反复试错，开发门槛高、失败率高、可访问性差，限制了RL技术的普及。
- **核心问题**：如何实现完全自动化的RL智能体设计，无需人工干预即可从自然语言任务描述与环境代码生成可执行的RL解决方案。
- **整体含义**：该工作提出了一种“智能体生成智能体”的新范式，利用大型语言模型（LLM）驱动自动化闭环，使智能体能够自我设计与优化，推动AI开发向全自动演进。

## 2. 提出的方法论
- **核心思想**：采用双智能体架构——**生成智能体（Generator Agent）** 负责分析任务并设计目标智能体，**目标智能体（Target Agent）** 则被自动生成并执行。整个RL开发过程被分解为两个阶段：**MDP建模**（将任务转化为马尔可夫决策过程）与**算法优化**（针对MDP自动选择/调整算法），从而降低自动化难度。
- **关键技术细节**：
  - 基于**模型上下文协议（Model Context Protocol）** 构建统一框架，支持在不同环境与算法下标准化地创建智能体。
  - 集成自适应训练管理与智能反馈分析，实现持续改进的闭环流程。
- **算法流程（文字说明）**：
  1. 输入自然语言任务描述和环境代码；
  2. 生成智能体分析任务，提取MDP建模所需状态、动作、奖励等信息；
  3. 生成智能体自动设计目标智能体的网络结构、超参数与训练策略；
  4. 目标智能体被实例化并在环境中运行训练；
  5. 收集训练结果与反馈，生成智能体根据反馈调整设计，重复直到达到性能标准。

## 3. 实验设计
- **数据集/场景**：使用四个基准环境——MuJoCo（连续控制）、MetaDrive（自动驾驶）、MPE（多智能体粒子环境）、SMAC（星际争霸多智能体挑战）。
- **Benchmark**：对比方法为**手动设计的基线（manually designed baselines）**，未具体列出哪些经典RL算法（如PPO、SAC等），但声称在所有任务上超越。
- **对比的方法**：仅提及“manually designed baselines”，未给出具体名称。

## 4. 资源与算力
- **文中未明确说明**使用的GPU型号、数量、训练时长等算力信息。元数据中也无相关记载。因此无法提供具体算力细节。

## 5. 实验数量与充分性
- **实验数量**：覆盖四个不同领域的Benchmark，每个环境可能包含多个子任务（未明确数量）。摘要未提及消融实验或超参数敏感性分析。
- **充分性与公平性**：
  - 优点：覆盖多种典型RL任务（连续控制、多智能体、自动驾驶），基准选择具有代表性。
  - 不足：未与SOTA自动化方法（如AutoRL、基于进化的方法）对比；基线只提“手动设计”，缺乏具体方法名称和实现细节，不利于复现；缺乏消融实验验证双阶段分解或反馈机制的有效性；未报告标准差或多次运行结果，统计可靠性不足。

## 6. 主要结论与发现
- Agent²框架能够完全自动化地生成可执行RL智能体，在多个Benchmark上**优于手动设计的基线**，性能提升最高达55%，平均稳定提升。
- 证明了LLM驱动的“智能体生成智能体”范式在RL自动化领域的可行性，为智能体自进化提供了全自动的基线方案。

## 7. 优点
- **方法创新**：首次提出双智能体架构和MDP建模-算法优化两阶段分解，系统化利用LLM实现端到端自动化。
- **通用性**：基于模型上下文协议，支持不同环境与算法，框架可扩展。
- **自动化程度高**：完全无需人工干预，从任务描述到可执行智能体一步到位。
- **性能优势**：在多个标准Benchmark上显著超越手工设计，有明确量化提升（最高55%）。

## 8. 不足与局限
- **实验覆盖不足**：仅对比了手动基线，缺乏与现有自动化RL方法（如AutoRL、进化策略、元学习框架）的对比，说服力有限。
- **消融分析缺失**：未独立验证“两阶段分解”、“生成智能体设计策略”、“反馈机制”等关键组件的贡献。
- **可复现性风险**：未提供开源代码或超参数细节，基线方法不明确，实验设置难以复现。
- **算力资源未报告**：无法评估方法的计算成本与实用性。
- **应用限制**：仅测试了模拟环境，未涉及真实机器人或大规模现实场景；依赖LLM，可能受限于LLM的推理能力和上下文窗口，复杂任务可能设计不完善。
- **统计分析不足**：未报告多次运行的平均值、标准差，无法判断性能提升的统计显著性。

（完）
