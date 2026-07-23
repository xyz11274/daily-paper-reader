---
title: "Alita-G: Self-Evolving Generative Agent for Agent Generation"
title_zh: Alita-G：用于智能体生成的自演化生成式智能体
authors: "Jiahao Qiu, Xuan Qi, Hongru WANG, Xinzhe Juan, Yimin Wang, Zelin Zhao, Jiayi Geng, Jiacheng Guo, Shilong Liu, Mengdi Wang"
date: 2025-09-02
pdf: "https://openreview.net/pdf?id=xf2JC4531b"
tags: ["query:ase"]
score: 10.0
evidence: 自演化框架通过生成MCP工具将通用智能体转化为领域专家
tldr: 现有自演化智能体仅局限于提示重写或失败重试，Alita-G提出一种更系统的方法：通用智能体在目标域任务上执行并合成候选MCP工具，通过抽象参数化基元并构建MCP盒，在推理时检索增强选择。实验表明，该方法显著提升了智能体在未见任务上的领域专业能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 当前自演化智能体的适应能力有限，仅停留在提示改写或失败重试层面。
method: Alita-G框架让通用智能体执行目标域任务，从成功轨迹合成MCP工具，抽象为参数化基元并整合为MCP盒，推理时检索增强选择。
result: 在多个领域任务上，Alita-G生成的智能体显著优于未演化基线及现有自演化方法。
conclusion: 通过自动化工具生成与抽象，Alita-G实现了从通用到领域专家的有效自演化。
---

## Abstract
Large language models (LLMs) perform better when scaffolded into agents with memory, tools, and feedback. Beyond this, self-evolving agents have emerged, but current work largely limits adaptation to prompt rewriting or failure retries. Therefore, we present Alita-G, a self-evolution framework that transforms a general-purpose agent into a domain expert by systematically generating, abstracting, and curating Model Context Protocol (MCP) tools. In this framework, a generalist agent executes a curated suite of target-domain tasks and synthesizes candidate MCPs from successful trajectories. These are then abstracted to parameterized primitives and consolidated into a MCP Box. At inference time, Alita-G performs retrieval-augmented MCP selection with the help of each tool’s descriptions and use cases, before executing an agent equipped with the MCP Executor. Across several benchmarks GAIA, PathVQA, and Humanity's Last Exam, Alita-G attains strong gains while reducing computation costs. On GAIA validation, it achieves 83.03% pass@1 and 89.09% pass@3, establishing a new state-of-the-art result while reducing mean tokens per example by approximately 15% relative to a strong baseline agent. Alita-G thus provides a principled pathway from generalist capability to reusable, domain-specific competence, improving both accuracy and efficiency on complex reasoning tasks.

---

## 论文详细总结（自动生成）

# 论文 Alita-G 详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
当前大型语言模型（LLM）在与智能体框架（含记忆、工具、反馈）结合后表现更佳，但自演化智能体的适应能力非常有限——现有工作大多局限于**提示重写**或**失败重试**，无法实现从通用智能体到领域专家的系统性转变。  
**Alita-G** 提出一种全新的自演化框架，核心动机是让通用智能体通过**自动生成、抽象和整理领域专用工具（MCP 工具）**，从而具备可重用的领域专业知识，在未见任务上也能高效、准确地执行。

## 2. 方法论：核心思想、关键技术细节与算法流程
### 核心思想
将自演化过程视为**工具生成与组织**问题：通用智能体在目标域任务上执行并记录成功轨迹，从中合成候选 MCP（Model Context Protocol）工具，再将这些工具抽象为参数化基元，合并为一个“MCP Box”。推理时，基于工具的说明和使用案例进行检索增强选择，最终由配备 MCP 执行器的智能体完成任务。

### 关键技术细节与流程（文字描述）
1. **任务执行与轨迹收集**：通用智能体在一组精心策划的目标域任务上执行，获得成功/失败轨迹。
2. **候选 MCP 工具合成**：从成功轨迹中提取可复用的子程序，将其封装为 MCP 工具（每个工具包含描述、参数、使用示例）。
3. **工具抽象与整合**：将相似的候选工具抽象为参数化基元（parameterized primitives），消除冗余，合并形成统一的 **MCP Box**（工具库）。
4. **推理时检索增强选择**：当新任务到来时，通过相似度检索从 MCP Box 中选取最相关的工具（利用描述和用例），动态装备到智能体中。
5. **执行**：智能体借助 MCP 执行器调用所选工具完成推理，无需从头学习或重复尝试。

## 3. 实验设计
### 数据集 / 场景
- **GAIA**（通用AI助手基准，含多步推理和工具使用）
- **PathVQA**（病理视觉问答，需专业领域知识）
- **Humanity's Last Exam**（高难度综合推理测试）
### Benchmark 与对比方法
- 对比了**未演化的通用智能体基线**（无工具生成与抽象）以及现有**自演化方法**（如仅提示重写或重试）。
- 在 GAIA 验证集上，Alita-G 达到 **83.03% pass@1** 和 **89.09% pass@3**，创下新 SOTA，同时平均每个样本的 token 消耗相比强基线减少约 **15%**。

## 4. 资源与算力
论文**未明确说明**所使用的 GPU 型号、数量、训练时长或推理硬件细节。仅在元数据中提及“减少计算成本”，但无具体算力报告。

## 5. 实验数量与充分性
- 实验覆盖了 **3 个数据集**（GAIA、PathVQA、Humanity's Last Exam），每个数据集上报告了主要指标（pass@1、pass@3 等）。
- 未明确列出消融实验数量，但从方法论描述可推断应有工具生成 vs 不生成、有无检索增强等对比。
- **充分性评估**：实验设计较为客观，使用公开基准并与强基线对比；但缺少更多领域（如代码、数学）的验证，且未探讨不同工具合成策略的消融细节。整体上在已报告场景中具有说服力。

## 6. 主要结论与发现
- Alita-G 通过**自动化工具生成与抽象**，有效将通用智能体转化为领域专家，在多个复杂推理任务上显著超越未演化基线和现有自演化方法。
- 实现了 **准确性与效率的双重提升**：更高的通过率（GAIA pass@1 83.03%）同时降低 token 消耗约 15%。
- 证明“工具生成+检索增强”比单纯的提示重写或失败重试更具普适性和可重用性。

## 7. 优点（方法与实验设计亮点）
- **系统性工具生成**：从成功轨迹自动合成 MCP 工具，而非手工定义，更具扩展性。
- **参数化抽象与整合**：减少冗余工具，形成紧凑的 MCP Box，推理时检索高效。
- **显式降低计算成本**：通过复用工具和减少重复尝试，实现了 token 节省。
- **多领域验证**：涵盖通用问答、专业视觉问答和极端难度测试，展示了广泛适用性。
- **SOTA 结果**：在 GAIA 上刷新纪录，且方法简洁、易于复现。

## 8. 不足与局限
- **实验覆盖不全**：仅测试了三个数据集，缺少对代码生成、数学推理、多轮对话等领域的验证。
- **资源消耗未公开**：未提供训练/推理硬件配置，难以评估算力门槛。
- **偏差风险**：工具合成依赖成功轨迹，若任务集有偏，可能生成有偏的工具库；未讨论工具失效或幻觉的应对策略。
- **应用限制**：需要预先设计目标域任务集来驱动演化，对于全新领域可能需要额外劳动；同时 MCP 工具的可移植性（跨域重用）未深入探讨。

（完）
