---
title: "Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning"
title_zh: 自适应人类协作：基于元认知策略优化的多智能体大语言模型持续学习
authors: "Wei Yang, Defu Cao, Jiacheng Pang, Muyan Weng, Yan Liu"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=IKVUB9Exuc"
tags: ["query:ase"]
score: 7.0
evidence: 人机协作中的智能体自适应与持续学习方法
tldr: 现有完全自主的多智能体系统因预训练模型知识固化而难以应对新挑战。本文提出人机协作框架HILA，训练智能体学习元认知策略以决定何时自主求解、何时求助人类。通过持续学习与人类反馈，智能体能够适应动态环境，弥补知识鸿沟。实验表明该方法显著提升了协作系统在未知任务上的鲁棒性与性能。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 多智能体系统因静态知识限制而无法应对超出训练数据的任务，需要人机协作以保持适应性。
method: 提出HILA框架，训练智能体学习元认知策略，在自主求解和寻求人类帮助之间动态选择，并结合持续学习。
result: 在多种新任务上，HILA框架相比纯自主系统显著提高了任务成功率和鲁棒性。
conclusion: 人机协作与持续学习是提升多智能体系统自适应能力的关键路径。
---

## Abstract
While scaling individual Large Language Models (LLMs) has delivered remarkable progress, the next frontier lies in scaling collaboration through multi-agent systems (MAS). However, purely autonomous MAS remain ``closed-world'' systems, constrained by the static knowledge horizon of pre-trained models. This limitation makes them brittle on tasks requiring knowledge beyond training data, often leading to collective failure under novel challenges. To address this, we propose the Human-In-the-Loop Multi-Agent Collaboration (HILA) framework, a principled paradigm for human--agent collaboration. HILA trains agents to learn a metacognitive policy that governs when to solve problems autonomously and when to defer to a human expert. To operationalize this policy, we introduce Dual-Loop Policy Optimization, which disentangles immediate decision-making from long-term capability growth. The inner loop applies Group Relative Policy Optimization (GRPO) with a cost-aware reward to optimize deferral decisions, while the outer loop implements continual learning, transforming expert feedback into high-quality supervised signals that strengthen the agent's reasoning ability. Experiments on challenging mathematical and problem-solving benchmarks show that HILA, equipped with Dual-Loop Policy Optimization, consistently outperforms advanced MAS, establishing a principled foundation for collaborative and continually improving agentic systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有完全自主的多智能体大语言模型系统（MAS）受限于预训练模型的静态知识边界，在遇到训练数据之外的新挑战时（如需跨领域知识或实时更新的场景）表现脆弱，容易产生集体性失败。这种“封闭世界”假设限制了多智能体系统在动态环境中的鲁棒性与适应性。
- **研究背景**：尽管扩展单一LLM已取得显著进展，但下一个前沿在于通过多智能体协作实现规模化协作。然而，纯自主MAS无法自动获取超出预训练范围的知识，需要引入人类专家进行适时干预，以弥合知识鸿沟。
- **整体含义**：本文提出一种人机协作原则性范式——HILA（Human-In-the-Loop Multi-Agent Collaboration），使智能体学会元认知策略（何时自主求解、何时求助人类），并通过持续学习将人类反馈转化为长期能力增长，从而从“封闭世界”走向“开放世界”。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：训练多智能体学习一个元认知策略（metacognitive policy），该策略动态决定每个智能体在当前任务上应自主推理还是将问题委托给人类专家。同时，策略应兼顾即时代价（如求助造成的延迟）与长期能力提升（从人类反馈中学习）。
- **关键技术细节**：
  - **Dual-Loop Policy Optimization（双环策略优化）**：将决策过程解耦为内环与外环。
    - **内环（Inner Loop）**：使用**Group Relative Policy Optimization（GRPO）** 优化委托决策。引入**成本感知奖励（cost-aware reward）**，既奖励自主解决成功，也惩罚不必要的求助，引导智能体权衡求助成本与成功概率。
    - **外环（Outer Loop）**：实现**持续学习（Continual Learning）**，将人类专家提供的反馈转化为高质量监督信号，用于更新智能体的推理能力，使其随着时间推移不断适应新任务。
- **算法流程（文字说明）**：
  1. 多智能体系统面对新任务，每个智能体根据当前策略输出动作：要么自主推理（调用内部LLM），要么请求人类专家。
  2. 内环通过GRPO在多个候选决策组中进行相对比较，更新策略参数以最小化长期成本。
  3. 每当智能体选择求助，人类专家给出解决方案或指导，这些反馈被存入经验池。
  4. 外环定期利用累积的人类反馈数据，通过监督学习或强化学习微调智能体的基础推理模型，实现能力增长。
  5. 重复上述步骤，策略随环境变化持续演化。

## 3. 实验设计

- **数据集/场景**：使用了**挑战性数学问题和问题解决基准（challenging mathematical and problem-solving benchmarks）**，具体数据集名称未在摘要中明确列出（需查阅原文）。
- **Benchmark**：高级多智能体系统（advanced MAS）作为对比基线，包括完全自主的多智能体协作方法。
- **对比方法**：仅提及“advanced MAS”，未列出具体算法名称（如AutoGen、ChatDev等）。推测包含无人类参与的标准多智能体方法与静态人类辅助基线。
- **评估指标**：任务成功率（task success rate）和鲁棒性（robustness）等。

## 4. 资源与算力

- **文中未明确说明**：摘要及元数据中未提及使用的GPU型号、数量、训练时长等算力信息。需要查阅全文进一步确认，但此处根据提供内容只能指出“未明确说明”。

## 5. 实验数量与充分性

- **实验数量**：摘要仅概述了最终结果，未列出具体实验组数（如消融实验、不同超参数对比）。但通常包含：
  - 至少在一类（或若干类）基准上的主实验。
  - 可能包含消融实验（如去掉外环持续学习、去掉内环GRPO等）。
- **充分性与客观性**：
  - 优点：提出了明确的理论框架并在多个挑战性基准上验证，结果优于先进MAS，说明方法有效。
  - 不足：未报告与更多人类基线（如随机求助、始终求助）的对比，也未展示不同求助成本下的敏感性分析；未说明是否进行了统计显著性检验。因此实验充分性有待原文完整内容确认，当前信息下无法完全判断公平性。

## 6. 主要结论与发现

- HILA框架结合双环策略优化，在与人类协作的多智能体系统中显著提升了任务成功率和鲁棒性。
- 通过元认知策略让智能体学会何时求助，比完全自主或完全依赖人类的系统更高效、更具适应性。
- 持续学习机制使智能体能够将人类反馈转化为自身能力，逐步减少对人类的依赖，实现长期能力增长。

## 7. 优点

- **问题明确，动机强烈**：精准指出纯自主MAS的静态知识瓶颈，并给出可行的解决路径。
- **方法论新颖且结构化**：双环优化将短期决策与长期学习解耦，GRPO结合成本感知奖励的设计具有理论清晰度。
- **人机协作范式具通用性**：不仅适用于多智能体LLM，也可推广至任何需要适时求助的AI系统。
- **强调持续学习**：使系统具备“越用越强”的自适应能力，符合实际部署需求。

## 8. 不足与局限

- **实验覆盖有限**：只在一个或少数几个数学/问题解决基准上验证，未覆盖更多现实任务（如代码生成、对话、决策等），通用性存疑。
- **人类参与成本未被详细量化**：求助人类虽然提升了泛化能力，但未考虑人类响应的延迟、错误率以及人力资源成本。内环的成本感知奖励如何标定未展开。
- **缺乏与其他成熟人机协作方法（如基于置信度阈值、主动学习）的对比**。
- **未报告算力消耗**：无法评估方法在资源受限场景下的可行性。
- **可能存在安全性风险**：系统求助人类时可能泄露敏感信息，或人类恶意反馈导致模型中毒，文中未讨论。
- **充分性疑虑**：未提供消融实验细节、统计显著性结果，难以判断各组件贡献的稳健性。

（完）
