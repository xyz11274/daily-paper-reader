---
title: "Towards Self-Evolving Agent Benchmarks : Validatable Agent Trajectory via Test-Time Exploration"
title_zh: 面向自进化智能体基准：通过测试时探索验证智能体轨迹
authors: "Dadi Guo, Tianyi Zhou, Dongrui Liu, Chen Qian, Qihan Ren, Shuai Shao, Zhiyuan Fan, Yi R. Fung, Kun Wang, Linfeng Zhang, Jing Shao"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=2H03gm4Rq6"
tags: ["query:ase"]
score: 4.0
evidence: 关注自进化基准，与智能体自进化间接相关
tldr: 现有智能体基准迅速达到上限，难以评估智能体真实能力。TRACE框架通过让智能体自由探索并演化任务难度，生成更复杂的评估场景。虽然焦点是基准而非智能体本身，但其方法可用于驱动智能体在新任务上自我进化。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有基准天花板现象严重，急需能随智能体能力提升而自动演化的评估方法。
method: 提出三阶段框架：原始任务演化、轨迹记录与复现验证，智能体在探索中提升任务难度并产生可验证轨迹。
result: TRACE成功生成了难度递增且可复现的基准任务，更好地区分了不同能力水平的智能体。
conclusion: 可演化基准为智能体持续学习和自我进化提供了更公平的评估环境。
---

## Abstract
Recent advances in large language models (LLMs) and agent system designs have empowered agents with unprecedented levels of capability. However, existing agent benchmarks are showing a trend of rapid ceiling-hitting by newly developed agents, making it increasingly difficult to meet the demands of evaluating agent abilities. To address this problem, we propose the Trajectory-based Validated-by-Reproducing Agent-benchmark Complexity Evolution (TRACE) framework. This framework takes an original task from an existing benchmark and encourages agents to freely explore and evolve it into a new task with higher difficulty while recording the corresponding execution trajectories. The framework proceeds in three stages: (1) evolutionary proposal mining, which generates task evolution proposals through preliminary exploration and divergent thinking; (2) problem construction via free exploration, where proposals are instantiated into concrete problem instances through agent exploration, with execution trajectories recorded along the process; and (3) multi-level validation, which ensures that the evolved tasks are accompanied by reproducible and logically coherent trajectories. Experiments on the GAIA benchmark demonstrate that the TRACE framework consistently enhances task complexity while improving correctness reliability through trajectory-level validation. In addition, our framework can successfully adapt to and improve reasoning benchmarks such as AIME-2024. This work marks a paradigm shift from static, manually curated benchmarks to dynamic, self-evolving evaluation systems, providing a sustainable and challenging foundation for agent development. Code and data can be found at https://github.com/titanwings/trace-benchmark-evolving.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：现有大语言模型驱动的智能体基准存在严重的“天花板效应”——新兴智能体迅速达到甚至饱和基准性能，导致难以有效区分不同能力水平的智能体，也限制了评估体系的持续发展。
- **核心问题**：如何构建一个能随智能体能力提升而自动演化、始终具有挑战性的动态评估环境。
- **整体含义**：论文提出从“静态人工基准”向“动态自进化基准”的范式转变，旨在为智能体的持续学习和自我进化提供更公平、更可持续的评估基础。

### 2. 论文提出的方法论
- **核心思想**：TRACE 框架通过让智能体在测试时自由探索，将一个原始任务逐步演化为难度递增的新任务，同时记录并验证其执行轨迹，确保演化后的任务可复现且逻辑连贯。
- **关键技术细节**：
  - **三阶段流程**：
    1. **演化提议挖掘**：通过初步探索和发散思维，生成任务演化的候选方向（如增加约束、引入新子任务等）。
    2. **自由探索构建问题**：将演化提议实例化为具体的问题实例，智能体在探索过程中自动生成并记录执行轨迹。
    3. **多级验证**：对演化后的任务进行轨迹级验证，确保轨迹的复现性和逻辑一致性，从而提升正确性可靠性。
- **无需额外公式或算法流程图**：以上文字描述已覆盖核心流程。

### 3. 实验设计
- **使用的数据集/场景**：
  - 主要基准：**GAIA**（一个通用智能体基准，包含多种真实世界任务）。
  - 推理基准：**AIME-2024**（数学竞赛题，用于验证适应性）。
- **对比方法**：论文未明确列出其他对比方法，而是将 TRACE 演化后的任务与原始未演化的任务进行对比，评估难度提升和智能体区分度。
- **评估指标**：任务复杂度（如所需步骤、信息检索量）、正确性可靠性（轨迹复现一致率）、智能体能力区分度。

### 4. 资源与算力
- 论文摘要及元数据中**未明确说明**使用的 GPU 型号、数量或训练时长。仅提及代码与数据已开源（GitHub），但未提及实验算力配置。因此无法总结具体资源消耗，需要指出这一信息缺失。

### 5. 实验数量与充分性
- **实验数量**：公开提及了在 GAIA 和 AIME-2024 两个基准上的实验，但未说明具体的子测试数量、演化轮次或消融实验组数。
- **充分性评价**：实验覆盖了通用任务（GAIA）和推理任务（AIME），表明框架具备一定泛化性；但缺乏在更多样基准（如代码生成、网络交互）上的验证，且未报告消融研究（如不同验证机制的效果）。因此实验充分性中等，结论的鲁棒性有待更多验证。

### 6. 论文的主要结论与发现
- TRACE 框架能够**持续提升任务复杂度**，生成难度递增且可复现的基准任务。
- 通过轨迹级验证机制，保证了演化任务**正确性可靠性**，使不同能力水平的智能体得到更清晰的区分。
- 在 GAIA 和 AIME-2024 上均验证了框架的有效性，表明该范式可适应多种任务类型。
- 标志着智能体评估从静态人工设计向**动态自进化**的转变，为智能体持续学习提供了可持续的挑战环境。

### 7. 优点
- **方法创新**：提出“测试时探索+轨迹记录+多级验证”的自动演化流程，无需人工干预，可自适应生成更难任务。
- **轨迹级验证**：不仅追求难度提升，还确保演化结果的复现性和逻辑性，增加了评估可信度。
- **范式转换**：将基准视为“可生长的评估工具”，而非一次性静态集合，契合智能体能力持续提升的需求。
- **开源代码与数据**：提供 GitHub 仓库，便于后续研究和复现。

### 8. 不足与局限
- **实验覆盖有限**：仅验证了两个基准，缺乏对多模态、代码交互等复杂智能体场景的测试，泛化性有待证实。
- **偏差风险**：演化过程依赖于智能体自身探索，可能引入对特定智能体策略的偏向，导致基准对非探索型代理不公平。
- **计算开销**：虽然未提及算力，但测试时探索和多次验证可能显著增加计算成本，论文未讨论效率问题。
- **初始任务依赖**：需要从现有基准的原始任务出发，无法从零生成任务，创新上限受限于初始任务集。
- **消融实验缺失**：未分析各阶段（如提议挖掘、自由探索、多级验证）对最终效果的独立贡献。

（完）
