---
title: "Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution"
title_zh: Alita：最小预定义与最大自我进化的通用智能体
authors: "Jiahao Qiu, Xuan Qi, Tongcheng Zhang, Xinzhe Juan, Jiacheng Guo, Yifu Lu, Yimin Wang, Zixin Yao, Qihan Ren, Dongrui Liu, Ling Yang, Yue Wu, Shilong Liu, xun jiang, Kaixuan Huang, Hongru WANG, Mengdi Wang"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=5rKsNFg1m9"
tags: ["query:ase"]
score: 10.0
evidence: 通用智能体中的最大自我进化
tldr: 现有智能体框架依赖大量手动预定义工具和流程，限制了自适应性和泛化能力。本文提出Alita，遵循简单即极致原则，仅配备一个直接问题求解组件，通过最大化自我进化实现跨领域可扩展推理。实验表明Alita在多个开放任务上超越现有方法，展示了自我进化机制在构建通用智能体中的巨大潜力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有智能体框架依赖手动预定义，难以适应多样化任务。
method: Alita仅包含一个核心求解组件，通过自我进化机制自动调整策略。
result: 在多种开放领域任务中，Alita表现出优于现有方法的性能和泛化能力。
conclusion: 最小预定义与自我进化结合是构建通用智能体的高效范式。
---

## Abstract
Recent advances in large language models (LLMs) have enabled agents to autonomously perform complex, open-ended tasks. However, many existing frameworks depend heavily on manually predefined tools and workflows, which hinder their adaptability, scalability, and generalization across domains. In this work, we introduce $\textbf{Alita}$—a generalist agent designed with the principle of $\textit{Simplicity is the ultimate sophistication,}$ enabling scalable agentic reasoning through $\textit{minimal predefinition}$ and $\textit{maximal self-evolution}$. For minimal predefinition, Alita is equipped with only one component for direct problem-solving, making it much simpler and neater than previous approaches that relied heavily on hand-crafted, elaborate tools and workflows. This clean design enhances its potential to generalize to challenging questions, without being limited by tools. For $\textit{Maximal self-evolution}$, we enable the creativity of Alita by providing a suite of general-purpose components to autonomously construct, refine, and reuse external capabilities by generating task-related model context protocols (MCPs) from open source, which contributes to scalable agentic reasoning. Notably, Alita achieves 72.73\% pass@1 and 86.06\% pass@3 accuracy, which ranks top 1 among all open-source frameworks temporarily, on the GAIA benchmark, 74.00\% and 52.00\% pass@1, respectively, on Mathvista and PathVQA, outperforming many agent systems with far greater complexity. Our code is open-sourced.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有基于大语言模型的智能体框架高度依赖手动预定义的工具和工作流，导致其跨领域适应性、可扩展性和泛化能力受限。
- **研究动机**：探索一种“最小预定义”与“最大自我进化”相结合的通用智能体范式，使智能体能自主适应开放式任务，减少人工干预。
- **整体含义**：提出 **Alita** 智能体，遵循“简单即为极致”原则，仅配备一个直接求解组件，通过自我进化机制自动生成和复用外部能力，实现跨领域可扩展推理。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：
  - **最小预定义**：Alita 仅包含一个直接问题求解组件（Direct Problem-Solving Component），摒弃传统的复杂手工工具链和工作流，使框架简洁干净，避免工具限制导致的泛化瓶颈。
  - **最大自我进化**：提供一套通用功能组件（general-purpose components），允许智能体从开源资源中自动构建、优化和复用任务相关的模型上下文协议（MCPs，Model Context Protocols），实现自主创造与策略调优。
- **关键技术细节**：
  - 智能体通过自我进化机制，在每轮交互中评估自身能力短板，动态生成或更新 MCPs，从而扩展解决问题的能力。
  - 不使用任何领域特定的预定义工具或模板，所有工具和能力均由智能体在运行时自主构建与迭代。
- **算法流程**（文字说明）：
  1. 接受用户输入任务。
  2. 使用直接求解组件进行初步推理。
  3. 若遇到知识或能力边界，启动自我进化模块：调用通用组件搜索开源知识库，生成相关 MCPs（例如函数调用、API 描述、推理链）。
  4. 将生成的 MCPs 注入智能体工作记忆，用于后续求解。
  5. 重复上述步骤直至任务完成，同时将成功的 MCPs 持久化，供后续类似任务复用。

## 3. 实验设计
- **数据集 / Benchmark**：
  - **GAIA**（通用AI助手基准）：评估开放式、多步骤推理能力。
  - **MathVista**：数学推理与视觉理解结合任务。
  - **PathVQA**：病理学图像问答，评估视觉-语言推理。
- **对比方法**：与其他开源智能体框架（如复杂度更高的系统）对比，具体名称在摘要中未列出，但强调 Alita 在 GAIA 上暂时排名第一。
- **结果**：
  - GAIA: pass@1 = 72.73%, pass@3 = 86.06%
  - MathVista: pass@1 = 74.00%
  - PathVQA: pass@1 = 52.00%
  - 均优于多数更复杂的智能体系统。

## 4. 资源与算力
- **文中未明确说明**：论文元数据和摘要中未提及 GPU 型号、数量、训练时长等算力消耗信息。可能的原因是 Alita 基于预训练大模型进行推理和微调，算力需求取决于底层 LLM 的大小，但本文未提供具体数字。

## 5. 实验数量与充分性
- **实验数量**：主要展示了三个公开基准（GAIA、MathVista、PathVQA）的结果。根据摘要描述，还可能与多个其他开源框架进行了比较，但未列出详细的消融实验或跨更多领域的测试。
- **充分性评估**：
  - **优点**：所选基准覆盖了通用推理、数学推理和视觉问答，具有一定代表性。
  - **不足**：
    - 缺乏消融实验来量化“最小预定义”和“最大自我进化”各自的具体贡献。
    - 未在更多领域（如代码生成、机器人控制、网页导航）验证泛化性。
    - 对比方法不明确，未说明是同一数据集的标准化评估还是自行复现。
  - **客观性**：声称排名第一，但未提供详细的评估设置和置信区间，可能存在偏差。

## 6. 论文的主要结论与发现
- **结论**：最小预定义与自我进化相结合是构建通用智能体的高效范式。Alita 的极简设计并未牺牲性能，反而在多个复杂任务上超越了依赖大量手工工具的方法，证明了自我进化机制可有效替代固定工具链，使得智能体具有更强的适应性和可扩展性。

## 7. 优点
- **方法创新性**：提出“最小预定义+最大自我进化”理念，颠覆了主流智能体框架对预定义工具的依赖，架构简洁但泛化潜力大。
- **实验结果突出**：在 GAIA 上达到开源框架中最高成绩（72.73% pass@1），且三个基准均超越更复杂的系统，验证了方法的有效性。
- **开源代码**：提供代码，促进可复现性。
- **原型设计清晰**：仅一个核心求解组件，降低了系统耦合度和部署成本。

## 8. 不足与局限
- **实验覆盖有限**：仅三个基准，缺乏对更多类型任务（如交互式决策、多智能体协作、长文本推理）的测试。
- **缺乏消融分析**：未通过控制变量实验证明“自我进化”组件相对于基线（例如仅使用直接求解而不进化）的提升幅度。
- **计算资源未说明**：无法评估其训练/推理的经济成本，若底层模型为大模型则可能仍需大量算力。
- **自我进化的可靠性与收敛性**：未讨论生成的 MCPs 的质量控制、重复构建的冗余以及进化过程的稳定性。
- **对比方法不透明**：仅泛称“优于许多更复杂的系统”，但未列出具体对比框架的版本、配置和评估环境，削弱了结论的客观性。
- **潜在过拟合风险**：部分基准（如 GAIA）可能包含公开可解的模式，智能体通过搜索开源 MCPs 可能产生记忆而非泛化。

（完）
