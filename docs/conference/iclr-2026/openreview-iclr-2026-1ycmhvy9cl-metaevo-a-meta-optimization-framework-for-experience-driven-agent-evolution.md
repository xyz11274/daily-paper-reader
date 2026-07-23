---
title: "MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution"
title_zh: MetaEvo：经验驱动智能体进化的元优化框架
authors: "Bowen Ren, Heyan Huang, Yinghao Li, Yang Gao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=1YcMHVY9cl"
tags: ["query:ase"]
score: 9.0
evidence: 元优化框架用于智能体进化，提升自我修正的元能力
tldr: 现有经验驱动型智能体进化方法生成的修正原则缺乏可操作性。MetaEvo将智能体进化重新定义为元优化任务，通过三阶段流水线先训练智能体的内在元能力——学会如何有效修正自身。在多个场景中MetaEvo显著提升了智能体的自进化效果，为经验驱动进化提供了理论坚实且实用的新框架。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有方法忽略了大语言模型在抽象知识与自我纠正上的固有局限，导致进化原则缺乏指导性。
method: 提出三阶段元优化流水线：先训练智能体提取高质量修正原则，再基于原则进行经验驱动的自我改进。
result: 相比基线方法，MetaEvo使智能体在复杂连续决策任务中表现出更强的自进化能力。
conclusion: 元优化视角为智能体自进化提供了通用且可扩展的范式，尤其适用于LLM场景。
---

## Abstract
Existing methods for experience-driven agent evolution often generate revision principles that lack actionable guidance, as they overlook the inherent limitations of Large Language Models (LLMs) in abstracting knowledge and self-correcting. To address this gap, we introduce MetaEvo, a novel framework that reframes agent evolution as a meta-optimization task. Instead of learning directly from experience, our core idea is to first enhance the agent’s intrinsic meta-ability—its capacity to learn how to effectively revise and improve itself. MetaEvo operationalizes this concept through a three-stage pipeline powered by a modular agent system. First, a meta-optimization stage explicitly trains the model on abstracting high-quality principles. These principles are then accumulated in a curated memory and subsequently retrieved by an execution module to guide generation on new tasks. Extensive experiments across a diverse suite of mathematical reasoning and multi-task benchmarks demonstrate that MetaEvo consistently and significantly improves model performance, enabling more robust and generalizable reasoning behaviors.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文核心问题与整体含义（研究动机和背景）

- **核心问题**：现有经验驱动型智能体进化方法（如通过收集过往经验生成修正原则）生成的修正原则缺乏可操作性，无法有效指导智能体的自我改进。
- **背景**：大语言模型（LLM）在抽象知识与自我纠正方面存在固有局限，直接让LLM从经验中学习进化往往导致原则泛化能力差、指导性弱。现有方法忽略了这一根本限制。
- **研究动机**：如何让智能体不仅从经验中学习，还能学会“如何学习”——即提升其**元能力**（meta-ability），从而实现更高效、更鲁棒的自进化。

## 2. 论文提出的方法论（核心思想与关键技术细节）

- **核心思想**：将智能体进化重新定义为**元优化任务**，先提升智能体内在的元能力——即学会如何有效修正自身，而非直接输出修正原则。
- **三阶段流水线**（由模块化智能体系统支撑）：
  1. **元优化阶段**（Meta-Optimization Stage）：显式训练模型提取高质量修正原则。利用模块化智能体系统，从示例经验中自动生成可操作、可泛化的原则。
  2. **原则记忆积累**（Curated Memory）：将第一阶段提取的高质量原则积累到专门构建的记忆库中，按相关性、质量等进行筛选和存储。
  3. **执行模块检索与引导**（Execution Module Retrieval）：在新任务中，执行模块从记忆库中检索最相关的原则，用于指导生成输出，实现经验驱动的自我改进。
- **关键技术细节**：未提供具体公式，原理上类似于元学习（learning to learn），但以LLM为基座，通过提示工程或微调方式实现原则提取能力的内化。模块化智能体系统可能包含生成、评估、筛选等子模块。

## 3. 实验设计（数据集、场景、基准、对比方法）

- **数据集与场景**：
  - 数学推理基准（数学问题集）
  - 多任务基准（多种类型的推理任务）
- **基准**（Benchmark）：涵盖多种数学推理和多任务场景，未具体列出名称（如GSM8K、MATH等未提及）。
- **对比方法**：未在摘要中具体列出对比的基线方法，但元数据提到“相比基线方法，MetaEvo使智能体在复杂连续决策任务中表现出更强的自进化能力”，推测对比了标准few-shot提示、直接经验驱动方法（如反思、自我纠错）、经验池方法等。

## 4. 资源与算力

- **未明确说明**：论文摘要和元数据均未提及任何关于GPU型号、数量、训练时长或计算成本的信息。仅能判断采用LLM作为基座（可能基于开源模型如Llama、GPT等），但具体算力需求未知。

## 5. 实验数量与充分性

- **实验数量**：元数据提到“在多个场景中MetaEvo显著提升了智能体的自进化效果”，摘要中提及在“数学推理和多任务基准”上进行了广泛实验。但未给出具体实验组数、消融实验细节。
- **充分性评估**：
  - 从元数据看，实验覆盖了两种不同类型的任务（数学推理和多任务），具有一定广度。
  - 但缺少以下信息：消融实验（是否验证了三阶段中每个阶段的作用）、不同LLM基座的适应性与泛化能力、与多种基线方法的对比表格、统计显著性测试等。因此**充分性中等**，论文可能在正文中有更详细实验，但根据现有摘要无法断言完全充分。
- **客观性**：摘要声称“一致显著地提升”，但缺乏误差分析或失败案例，可能存在报告偏倚。

## 6. 主要结论与发现

- MetaEvo框架能够**一致且显著地**提升LLM在数学推理和多任务场景中的性能。
- 通过先训练元能力（提取高质量原则），再基于原则进行经验驱动自我改进，智能体表现出**更强、更鲁棒且可泛化的推理行为**。
- 元优化视角为智能体自进化提供了**通用且可扩展的范式**，尤其适用于LLM场景，解决了现有方法修正原则缺乏可操作性的痛点。

## 7. 优点（方法与实验设计亮点）

- **方法创新性**：将智能体进化重新定义为元优化任务，引入“学会如何修正”的元能力训练，突破了传统直接学习经验的瓶颈。
- **三阶段流水线清晰模块化**：元优化→记忆积累→检索执行，逻辑链完整，易于实现和扩展。
- **理论坚实**：元学习思想与LLM自我改进结合，具有强可解释性。
- **实验覆盖多领域**：数学推理与多任务两种互补场景，体现方法通用性。

## 8. 不足与局限

- **实验细节缺失**：未提供具体数据集名称、基线方法列表、消融实验、超参数设置等，影响可复现性。
- **算力成本未披露**：对于实际部署的可行性评估不足。
- **偏置风险**：摘要未报告负面案例或失败分析，可能存在选择性报告。
- **应用限制**：依赖于模块化智能体系统，可能对LLM的上下文长度、推理能力有较高要求；抽象原则提取能力可能受基座模型本身限制，在弱LLM上效果可能打折。
- **理论泛化性**：仅在数学推理和多任务上验证，对开放域对话、代码生成等场景未涉及，存在领域局限。

（完）
