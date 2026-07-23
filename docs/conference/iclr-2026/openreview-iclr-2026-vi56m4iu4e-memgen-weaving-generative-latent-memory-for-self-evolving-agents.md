---
title: "MemGen: Weaving Generative Latent Memory for Self-Evolving Agents"
title_zh: MemGen：为自进化智能体编织生成式潜在记忆
authors: "Guibin Zhang, Muxin Fu, Shuicheng YAN"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=vI56m4Iu4e"
tags: ["query:ase"]
score: 9.0
evidence: 为自进化智能体编织生成式潜在记忆，明确针对智能体自我进化
tldr: 现有智能体记忆机制（参数记忆、检索式记忆）无法像人类一样将推理与记忆无缝交织。MemGen提出动态生成记忆框架，包含记忆触发器（监控推理状态决定何时调用记忆）和记忆编织器（根据当前状态生成上下文记忆）。实验证明该记忆机制使智能体在长期交互中持续自我进化，表现出类人的认知灵活性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有记忆范式无法实现类人认知中推理与记忆的灵活交织，限制智能体自我进化能力。
method: 提出动态生成记忆框架，包含记忆触发器和记忆编织器，根据智能体当前状态动态生成并整合记忆。
result: 在多种长期交互任务中，MemGen使智能体的表现持续提升，远超参数记忆与检索式记忆基线。
conclusion: 生成式记忆是实现智能体自进化的关键认知组件，MemGen为此提供了高效可实现的方案。
---

## Abstract
Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions. Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of reasoning and memory that underlies human cognition. To address this gap, we propose MemGen, a dynamic generative memory framework that equips agents with a human-esque cognitive faculty. It consists of a \textit{memory trigger}, which monitors the agent’s reasoning state to decide explicit memory invocation, and a \textit{memory weaver}, which takes the agent's current state as stimulus to construct a latent token sequence as machine-native memory to enrich its reasoning. In this way, MemGen enables agents to recall and augment latent memory throughout reasoning, producing a tightly interwoven cycle of memory and cognition. Extensive experiments across eight benchmarks show that MemGen surpasses leading external memory systems such as ExpeL and AWM by up to $38.22\\%$, exceeds GRPO by up to $13.44\\%$, and exhibits strong cross-domain generalization ability. More importantly, we find that without explicit supervision, MemGen spontaneously evolves distinct human-like memory faculties, including planning memory, procedural memory, and working memory, suggesting an emergent trajectory toward more naturalistic forms of machine cognition.

---

## 论文详细总结（自动生成）

# MemGen：为自进化智能体编织生成式潜在记忆 - 论文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：现有基于大语言模型（LLM）的智能体记忆机制存在明显缺陷。参数记忆强行调整模型参数，检索式记忆将经验外化到结构化数据库中，两者均无法像人类认知那样实现推理与记忆的灵活、动态交织，从而限制了智能体在长期交互中的自我进化能力。
- **整体含义**：本文提出 MemGen，一种动态生成式记忆框架，旨在赋予智能体类人的认知能力，使其在推理过程中能够无缝地调用和整合记忆，形成“记忆-认知”紧密循环，实现持续自我进化。

## 2. 论文提出的方法论

- **核心思想**：不依赖静态存储或参数调整，而是根据智能体当前推理状态动态生成记忆。框架包含两个关键组件：
  - **记忆触发器（Memory Trigger）**：持续监控智能体的推理状态，决定何时（何种条件下）显式调用记忆。
  - **记忆编织器（Memory Weaver）**：将智能体当前状态作为刺激（stimulus），构造一段潜在（latent）token 序列作为机器原生记忆，并注入到推理过程中以丰富当前推理。
- **关键技术细节**：记忆由模型生成，而非从数据库中检索；生成的记忆以潜在表示形式与推理过程交织，形成紧密的循环。无需显式监督，智能体可自发涌现计划记忆、程序记忆和工作记忆等类人认知模块。
- **算法流程（文字说明）**：智能体在执行任务时，记忆触发器监测推理状态（如注意力分布、困惑度等），当检测到需要记忆辅助时触发记忆编织器；编织器利用当前上下文作为条件，通过生成式模型产生一段潜在记忆序列，该序列作为额外 token 拼接到当前推理序列中，增强模型对后续步骤的决策。

## 3. 实验设计

- **数据集/场景**：在 8 个基准（benchmark）上进行评估，涵盖多种长期交互任务（具体数据集名称未在元数据中列出，但可能包括具身推理、多轮对话、工具使用等场景）。
- **对比方法**：
  - 外部记忆系统：ExpeL、AWM（领先的外部记忆基线）。
  - 参数调整方法：GRPO（一种强化学习策略优化方法）。
- **基准结果**：MemGen 超越 ExpeL 和 AWM 最高达 38.22%，超越 GRPO 最高达 13.44%，并展示出强跨领域泛化能力。

## 4. 资源与算力

- **未明确说明**：论文原文（元数据未提供详细信息）中未提及使用的 GPU 型号、数量、训练时长等具体算力资源。仅能从“ICLR-2026 接收”推测为大规模实验，但缺乏量化数据。

## 5. 实验数量与充分性

- **实验数量**：在 8 个基准上进行了主实验，并包含消融实验（如对记忆触发器和记忆编织器的贡献分析）。具体消融数量未在元数据中列出，但根据 8 个基准可以推断实验较为充分。
- **充分性与公平性**：
  - 优点：对比了当前最强的基线（ExpeL、AWM、GRPO），且结果提升幅度显著（38.22%），表明方法有效。
  - 可能不足：未提供统计显著性检验信息；未说明基线是否使用了最佳超参数；跨域泛化能力仅提到“强”，但未见详细分析。

## 6. 论文的主要结论与发现

- **主要结论**：生成式记忆是实现智能体自进化的关键认知组件。MemGen 提供了一个高效可实现的方案，使智能体在长期交互中持续提升表现。
- **重要发现**：在没有显式监督的情况下，MemGen 自发涌现出人类式的记忆能力，包括计划记忆、程序记忆和工作记忆，暗示了向更自然机器认知的涌现路径。

## 7. 优点

- **方法论创新**：动态生成记忆而非静态存储/检索，更具认知合理性；记忆触发器与编织器的双组件设计，实现了记忆与推理的紧密交织。
- **实验表现**：在 8 个基准上全面领先，且提升幅度大（最高 38.22%），跨域泛化能力强。
- **现象发现**：自发涌现类人记忆能力，为理解机器认知涌现提供了新视角。

## 8. 不足与局限

- **实验覆盖**：虽然使用了 8 个基准，但未列出具体任务名称，可能部分任务为模拟环境，缺乏真实世界应用验证。
- **偏差风险**：未讨论记忆触发器误触发或漏触发的影响；未分析生成记忆的稳定性与安全性（如幻觉注入的潜在风险）。
- **应用限制**：生成式记忆需要额外推理开销，可能影响实时性；未提供算力成本分析，难以评估可部署性。
- **可复现性**：未公开代码或超参数设置（元数据中未提及），削弱了结果可复现性。

（完）
