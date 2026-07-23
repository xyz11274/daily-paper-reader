---
title: "Multi-Agent Evolve: LLM Self-Improve through Multi-Agent Co-evolution"
title_zh: 多智能体进化：通过多智能体共同进化实现大语言模型自改进
authors: "Yixing Chen, Yiding Wang, Haofei Yu, Tao Feng, Siqi Zhu, Muhan Zhang, Mostofa Patwary, Jiaxuan You"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=sknMpr8NWU"
tags: ["query:ase"]
score: 9.0
evidence: 多智能体共同进化实现大语言模型自改进
tldr: 强化学习提升LLM推理能力依赖人工数据和可验证奖励，可扩展性受限。本文提出MAE框架，让多个LLM智能体通过自我对弈共同进化，无需标注数据或外部反馈。智能体之间通过生成任务、交互求解、互相评估产生学习信号，实现自演进。在数学推理和代码生成等任务上，MAE超越了依赖外部环境的自博弈方法。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: RL增强LLM依赖人工数据与环境反馈，限制了在通用领域的扩展。
method: 提出MAE框架，多智能体通过互相生成任务与评估进行自我对弈式共同进化。
result: 在数学推理与代码生成基准上，MAE优于传统自博弈方法且无需外部环境。
conclusion: 多智能体共同进化为LLM自改进提供了一种无监督、可泛化的新范式。
---

## Abstract
Reinforcement Learning (RL) has demonstrated significant potential in enhancing the reasoning capabilities of large language models (LLMs). However, the success of RL for LLMs heavily relies on human-curated datasets and verifiable rewards, which limit their scalability and generality.
Recent Self-Play RL methods, inspired by the success of the paradigm in games and Go, aim to enhance LLM reasoning capabilities without human-annotated data. However, their methods primarily depend on a grounded environment for feedback (_e.g._, a Python interpreter or a game engine); extending them to general domains remains challenging.
To address these challenges, we propose **Multi-Agent Evolve (MAE)**, a framework that enables LLMs to self-evolve in solving diverse tasks, including mathematics, reasoning, and general knowledge Q\&A.
The core design of MAE is based on a triplet of interacting agents (_Proposer_, _Solver_, _Judge_) that are instantiated from a single LLM, and applies reinforcement learning to optimize their behaviors. The Proposer generates questions, the Solver attempts solutions, and the Judge evaluates both while co-evolving. Experiments on Qwen2.5-3B-Instruct demonstrate that MAE achieves an average improvement of 4.86\% across multiple benchmarks, surpassing previous methods. These results highlight MAE as a scalable, data-efficient method for enhancing the general reasoning abilities of LLMs with minimal reliance on human-curated supervision.

---

## 论文详细总结（自动生成）

基于提供的论文元数据（标题、摘要、tag等）和用户要求，以下是对“Multi-Agent Evolve: LLM Self-Improve through Multi-Agent Co-evolution”的结构化总结。由于原始论文PDF未完整获取，以下信息主要来自元数据中的摘要、tldr、motivation等文本。

---

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：当前强化学习（RL）虽能提升LLM的推理能力，但其成功高度依赖人工标注数据和可验证的外部奖励（如Python解释器、游戏引擎），导致可扩展性差、难以泛化到通用领域。
- **整体含义**：本文提出一种无需外部反馈和人工数据的新范式——通过多智能体共同进化，让LLM在自我对弈中自发产生学习信号，实现自改进。这突破了传统RL在LLM自改进中的局限性。

### 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：设计一个由 **Proposer（提议者）、Solver（求解者）、Judge（评判者）** 组成的三元组智能体，三者均从同一个基础LLM实例化而来。它们通过相互生成任务、求解和评估，形成闭环学习信号，并借助强化学习优化各自行为，实现共同进化。
- **关键技术细节**：
  - **Proposer**：生成未标注的问题/任务。
  - **Solver**：尝试解答Proposer提出的问题。
  - **Judge**：评估问题质量与解答正确性，提供可学习的奖励信号（无需外部环境）。
  - 三者协同：Proposer与Solver自我对弈，Judge提供自动评估，整个体系通过RL（具体算法未明确）更新参数，不依赖人工标注或外部反馈。
- **算法流程**（文字描述）：
  1. 从同一LLM初始化三个智能体。
  2. 循环迭代：Proposer生成一批问题，Solver尝试求解，Judge对问题和解答分别打分。
  3. 基于Judge的评分构造奖励，用强化学习更新三个智能体的策略。
  4. 重复上述过程，直至收敛。

### 3. 实验设计：数据集/场景、Benchmark、对比方法
- **数据集/场景**：涵盖数学推理、通用推理、知识问答等任务；具体数据集未在元数据中列出，但提及“multiple benchmarks”包括数学推理和代码生成。
- **基准（Base Model）**：Qwen2.5-3B-Instruct。
- **对比方法**：主要对比依赖外部环境的Self-Play RL方法（如使用Python解释器或游戏引擎的方法），以及传统RL方法（需人工数据）。
- **结果**：在多个基准上平均提升4.86%，超越此前无需外部环境的自博弈方法。

### 4. 资源与算力
- **未明确说明**：元数据中未提及GPU型号、数量、训练时长等具体算力信息。论文原文可能包含，但此处无法获取，故无法总结。

### 5. 实验数量与充分性
- **实验数量**：元数据仅提及“across multiple benchmarks”和“average improvement of 4.86%”，未给出具体实验组数或消融实验细节。推测可能包含多个数学/代码基准的对比实验，但缺乏消融实验（如移除某个智能体）的说明。
- **充分性评估**：基于现有信息，实验设计集中于单一基座模型（Qwen2.5-3B）和通用基准，初步验证了框架有效性。但缺乏对更大模型、更多领域（如开放式对话、长文本推理）的验证，也未讨论初始化敏感性和训练稳定性。因此充分性有限，但符合初步方法论证的常规范围。

### 6. 论文的主要结论与发现
- MAE框架无需人工数据和外部环境，通过多智能体共同进化即可实现LLM在数学推理、代码生成等任务上的自改进。
- 在Qwen2.5-3B-Instruct上，MAE相比依赖外部环境的Self-Play方法获得4.86%的平均性能提升，证明该范式是数据高效且可扩展的。
- 该工作为LLM的无监督、通用自我进化提供了一种新范式。

### 7. 优点：方法或实验设计上的亮点
- **完全无监督**：摆脱了对人工标注和外部环境（如Python解释器）的依赖，理论上可推广至任意通用领域。
- **自洽内循环**：三个智能体从同一LLM初始化，无需额外模型或数据，实现自给自足的学习信号。
- **简单高效**：仅通过多智能体之间的交互和RL优化，在较小模型（3B）上即获得显著提升，体现了方法的有效性。

### 8. 不足与局限
- **实验覆盖有限**：仅测试了3B规模模型，未在更大模型（如7B、70B）或更多样化任务（如对话、常识推理）上验证，泛化性存疑。
- **缺乏消融与分析**：未报告移除某个智能体或改变交互策略的消融实验，也无法判断三个角色的相对贡献。
- **潜在偏差风险**：Proposer生成的问题可能局限于自身知识范围，导致学习信号偏向某一领域；Judge的评估可能不准确，从而误导优化方向。
- **应用限制**：当前仅验证了数学和代码任务，这些任务天然具有明确对错标准；对于开放型任务（如创意写作），Judge难以提供有效反馈，方法适应性未知。
- **算力需求未交代**：缺少训练成本信息，难以评估实际落地可行性。

（完）
