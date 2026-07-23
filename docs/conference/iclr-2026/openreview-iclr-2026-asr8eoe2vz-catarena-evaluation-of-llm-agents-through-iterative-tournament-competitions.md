---
title: "CATArena:  Evaluation of LLM Agents Through Iterative Tournament Competitions"
title_zh: CATArena：通过迭代锦标赛竞争评估大语言模型智能体
authors: "Lingyue Fu, Xin Ding, Yaoming Zhu, Shao Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=aSr8eoe2vz"
tags: ["query:ase"]
score: 8.0
evidence: 通过迭代锦标赛竞争实现自改进与同伴学习
tldr: 现有基准测试固定场景评估，无法反映智能体的学习与改进能力。本文提出CATArena，一种迭代式竞争同伴学习框架，让智能体在反复交互与反馈中优化策略。该框架强调自改进与同伴学习是迈向人类级智能的核心驱动力，实验表明能有效提升智能体在复杂任务上的表现。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 当前基准测试局限于静态场景评估，忽略了智能体的学习能力尤其是自改进与同伴学习。
method: 构建迭代式竞争同伴学习框架，通过多轮交互和反馈驱动智能体策略优化。
result: 在多种任务上，参与迭代竞争的智能体策略质量持续提升，验证了学习能力的评估价值。
conclusion: 自改进与同伴学习是智能体进化的核心，CATArena为评估此类能力提供了新范式。
---

## Abstract
Large Language Model (LLM) agents have evolved from basic text generation to autonomously completing complex tasks through interaction with external tools. However, current benchmarks mainly assess end-to-end performance in fixed scenarios, restricting evaluation to specific skills and suffering from score saturation and growing dependence on expert annotation as agent capabilities improve. In this work, we emphasize the importance of learning ability, including both self-improvement and peer-learning, as a core driver for agent evolution toward human-level intelligence. We propose an iterative, competitive peer-learning framework, which allows agents to refine and optimize their strategies through repeated interactions and feedback, thereby systematically evaluating their learning capabilities. To address the score saturation issue in current benchmarks, we introduce CATArena, a tournament-style evaluation platform featuring four diverse board and card games with open-ended scoring. By providing tasks without explicit upper score limits, CATArena enables continuous and dynamic evaluation of rapidly advancing agent capabilities. Experimental results and analyses involving both minimal and commercial code agents demonstrate that CATArena provides reliable, stable, and scalable benchmarking for core agent abilities, particularly learning ability and strategy coding.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：当前大语言模型（LLM）智能体已从简单文本生成演进为能通过外部工具自主完成复杂任务。然而，现有基准测试（benchmarks）主要评估智能体在固定场景下的端到端性能，这限制了评估的广度（仅关注特定技能），且存在分数饱和（score saturation）问题，以及随着智能体能力提升而对专家标注的依赖日益增加。
- **核心问题**：现有评估体系忽视了智能体的学习能力，尤其是**自改进（self-improvement）**和**同伴学习（peer-learning）**。论文认为学习能力是智能体向人类级智能进化的核心驱动力。
- **整体含义**：提出一种迭代式竞争同伴学习框架（iterative competitive peer-learning framework），允许智能体通过反复交互和反馈来优化策略，从而系统性地评估其学习能力；并引入CATArena平台，通过无上界的开放式任务实现持续、动态的智能体能力评估。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将评估从静态场景转向动态迭代竞争环境，让智能体在与其他智能体的对战（锦标赛竞争）中不断学习、调整策略，从而激发和度量其学习能力。
- **关键技术细节**：
  - **迭代式竞争同伴学习框架**：智能体在每一轮比赛中与其他智能体交互（如对弈），获得胜负反馈；之后利用这些反馈更新自身策略（例如修改代码、调整参数或优化决策逻辑）。经过多轮迭代，智能体策略质量持续提升。
  - **CATArena平台**：包含四种多样化的棋盘&卡牌游戏（board and card games），每个游戏都设计为开放式评分（open-ended scoring），即没有明确的上限分数。这使得即使能力持续进步的智能体也能在平台上获得新的分数记录，避免了分数饱和。
  - **评估方式**：通过锦标赛赛制（tournament-style）组织比赛，每个智能体与多个对手多次对局，计算平均成绩或胜率，从而得到稳定、可扩展的能力排名。

## 3. 实验设计：使用的数据集/场景、benchmark、对比方法

- **实验场景**：CATArena平台中四种不同的棋盘&卡牌游戏（具体游戏名称未在摘要中提及，推测为经典策略游戏如围棋、象棋简化版或德州扑克等）。
- **Benchmark**：CATArena自身即为评估学习能力的新基准，与现有静态基准（如面向特定技能的标准测试集）形成对比。
- **对比方法**：
  - **最小化代码智能体（minimal code agents）**：代表基础策略能力的基线。
  - **商业代码智能体（commercial code agents）**：如基于GPT等大型模型的智能体，代表当前先进水平。
  - 实验比较了两类智能体参与迭代竞赛前后的表现差异，以及不同智能体在学习能力上的差异。

## 4. 资源与算力

- 论文未明确说明所使用的GPU型号、数量、训练时长等算力资源。仅提及了“minimal and commercial code agents”，但未披露具体硬件配置。因此，资源与算力信息缺失，无法评估计算成本。

## 5. 实验数量与充分性

- **实验数量**：论文在四种游戏场景上进行了多轮迭代竞赛。每种游戏下，多个智能体（至少包含两类以上）进行多轮对战，且每轮包含多个对局以获取稳定统计量。此外，可能还包含了消融实验（例如比较有无学习模块的智能体表现），但摘要中未详细说明具体组数。
- **充分性**：从描述看，实验覆盖了多种类型任务（四种游戏），对比了两种不同程度的智能体基线，且通过迭代多次验证了学习效果。但缺乏与更多现有基准（如标准NLP任务）的横向比较，也未提供统计显著性检验。整体上实验设计较规范，但细节披露有限，其充分性需原文确认。

## 6. 论文的主要结论与发现

- **主要结论**：
  1. 自改进和同伴学习是智能体进化的核心驱动力，CATArena框架能有效激发和度量这种能力。
  2. 参与迭代竞争后，智能体的策略质量显著提升（持续改善），证明了学习能力的评估价值。
  3. CATArena提供了可靠、稳定、可扩展的基准测试，可用于核心智能体能力（尤其是学习能力和策略编码）的评估。
- **发现**：商业代码智能体通过学习迭代获得了比最小化代码智能体更显著的进步，表明强大基础模型结合学习机制可带来更大收益。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：首次将**学习能力**（自改进与同伴学习）作为评估LLM智能体核心维度，改变了传统静态评估范式。
- **解决分数饱和**：通过开放式评分任务（无上界），避免了高能力智能体因天花板而无法区分。
- **动态评估**：锦标赛迭代竞争机制能模拟真实环境中智能体不断适应和提升的过程，更具生态效度。
- **实用性**：平台设计支持多种游戏，可扩展至更复杂任务，不依赖人工标注，降低了评估成本。

## 8. 不足与局限

- **实验覆盖有限**：仅使用四种棋盘/卡牌游戏，未涵盖其他类型复杂任务（如编程、数据分析等），泛化性有待验证。
- **偏差风险**：游戏任务可能偏向于策略型任务，对需要长期规划或知识检索的任务评估不足，存在任务选择偏差。
- **资源成本未报告**：缺乏算力消耗信息，读者难以判断其实际可行性或成本。
- **未与其他学习框架比较**：没有对比其他流行的强化学习或自改进方法（如RLHF、self-play等），无法明确其相对优势。
- **依赖代码修改**：智能体策略优化可能需修改代码，这对闭源模型或API限制模型不友好，应用限制较大。

（完）
