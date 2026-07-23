---
title: "EvoMAS : Heuristics in the Loop—Evolving Smarter Agentic Workflows"
title_zh: EvoMAS：循环中的启发式——演化更智能的智能体工作流
authors: "Yangbo Wei, Zhen huang, ronghaoxu, Hong Wang, WEI W. XING"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=0rJUulYnow"
tags: ["query:ase"]
score: 9.0
evidence: 动态进化策略和角色级进化的多智能体系统
tldr: 针对多智能体系统手工设计效率低的问题，EvoMAS提出生物启发的进化框架，通过六种探索/利用算子动态选择策略，并在角色层面优化智能体专业化与协作模式。实验表明，该方法自动生成的工作流优于人工设计，显著提升了复杂任务性能。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 当前多智能体系统构建依赖人工设计，自动化方法生成模板化智能体且忽略任务复杂度梯度。
method: 提出EvoMAS框架，包含动态多样化进化策略、角色级进化与课程引导三个维度，利用六种生物启发算子自适应选择策略。
result: 在多个复杂任务上，EvoMAS自动生成的智能体工作流性能优于人工设计基线。
conclusion: EvoMAS为多智能体系统的自动化设计提供了一种高效且可扩展的进化方案。
---

## Abstract
The rapid development of Large Language Models has driven Multi-Agent Systems (MAS) growth, but constructing efficient MAS requires labor-intensive manual design. Current automation methods generate templated agents, use monolithic optimization, and ignore task complexity gradients. This paper presents Evolutionary MAS (\textbf{EvoMAS}), a biologically-inspired framework that systematically addresses these limitations through three interconnected dimensions: (1) \textbf{dynamic and diverse evolutionary strategies} with six biologically-inspired operators (3 exploration, 3 exploitation) and adaptive strategy selection; (2) \textbf{role-level evolution} that dynamically optimizes agent specialization and collaboration patterns; and (3) \textbf{curriculum-guided evolution} partitioning tasks by difficulty levels and evolving sequentially from simple to complex with cross-stage stability constraints. Additionally, to resolve the contradiction between the inefficiency of pure evolutionary methods and the limited flexibility of manual design, we developed the \textbf{"Cyber Creator"}, a meta-control system combining dynamic rule formulation with reflective updates. Experimental evaluations demonstrate that EvoMAS consistently outperforms existing methods across multiple domains while maintaining cost efficiency, with agent roles dynamically evolving from homogeneous actors to specialized reasoning ensembles. Codes are available at \href{https://anonymous.4open.science/r/EvoMAS-DEF4}
{EvoMAS}.

---

## 论文详细总结（自动生成）

# EvoMAS：循环中的启发式——演化更智能的智能体工作流 详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前多智能体系统（MAS）的构建高度依赖人工设计（labor-intensive manual design），而现有自动化方法存在三个关键缺陷：生成模板化智能体、采用单一优化策略、忽略任务复杂度梯度。
- **研究动机**：受限于人工设计的低效与自动化方法的灵活性不足，亟需一种能够自适应地优化智能体专业化分工与协作模式的自动化框架。
- **整体含义**：提出一种受生物进化启发的框架 EvoMAS，通过动态进化策略、角色级进化和课程引导进化三个维度，实现多智能体工作流的自动设计和优化，从而在复杂任务上超越人工设计，同时保持成本效率。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程

- **核心思想**：将智能体工作流的优化建模为进化过程，利用六种生物启发算子（3种探索、3种利用）进行自适应策略选择；在角色层面动态优化智能体专业化和协作模式；通过课程学习按难度阶段进化。
- **关键技术细节**：
  - **动态多样化进化策略**：包含六种算子（探索型算子和利用型算子各3个），并采用自适应策略选择机制，平衡探索与利用。
  - **角色级进化**：不同于传统固定角色分配，允许智能体在进化过程中动态调整其角色（从同质化演员进化为专业化推理组合）。
  - **课程引导进化**：将任务按难度划分，从简单到复杂顺序进化，并加入跨阶段稳定性约束，防止灾难性遗忘或性能退化。
  - **“Cyber Creator”元控制系统**：为解决纯进化方法效率低与手工设计灵活性有限的矛盾，设计了结合动态规则制定与反射更新的元控制层。
- **算法流程（文字说明）**：
  1. 初始化一组多智能体工作流（种群）；
  2. 对每个工作流在任务上评估适应度（性能指标）；
  3. 根据自适应策略选择某个算子（探索或利用）对工作流进行变异或重组；
  4. 角色级进化允许调整智能体的专业分工；
  5. 按照课程阶段：从简单任务开始，逐步过渡到更复杂任务，以跨阶段稳定性约束保持已学能力；
  6. 重复迭代至收敛或达到最大代数，输出最佳工作流。

## 3. 实验设计：数据集/场景、基准、对比方法

- **数据集/场景**：摘要中未具体列出使用的任务名称或数据集，仅提及“multiple domains”（多个领域）和“multiple complex tasks”。可能涉及典型的 LLM 多智能体协作基准（如推理、代码生成、问答等），但缺乏明确信息。
- **基准（Benchmark）**：未公开；推测与现有的多智能体系统构建方法（如手动设计、模板化方法、单一代进化方法）对比。
- **对比方法**：文中提到与“existing methods”比较，包括人工设计的基线以及之前的自动化方法。具体方法名称未在摘要中给出。

## 4. 资源与算力

- 论文摘要**未明确说明**使用的 GPU 型号、数量或训练时长。仅提及“成本效率”（cost efficiency），但未提供具体资源消耗数据。需查看全文才可获知。

## 5. 实验数量与充分性

- **实验数量**：摘要中仅概括性描述“experimental evaluations demonstrate that EvoMAS consistently outperforms existing methods across multiple domains while maintaining cost efficiency”。未列出具体实验组数，也未说明消融实验（如对每个维度的贡献验证）。可能需要阅读全文才能判断。
- **充分性**：目前信息不足以评估实验设计的充分性、公平性和客观性。若全文包含多个领域、多种基线、消融研究和稳定性分析，则较为充分；但摘要内容有限，无法下定论。

## 6. 论文的主要结论与发现

- EvoMAS 自动生成的智能体工作流在多个复杂度任务上性能**优于**人工设计的工作流。
- 智能体角色能够从同质化演员**动态进化**为具有专业化分工的推理组合。
- 该方法保持了**成本效率**，避免因过度进化导致资源浪费。
- 验证了动态进化策略、角色级进化和课程引导进化三个维度同时工作时的有效性。

## 7. 优点

- **方法创新性**：首次将动态多样化进化策略、角色级进化与课程引导进化三个维度系统集成到多智能体工作流自动化设计中，解决了现有方法的三个根本缺陷。
- **生物启发机制**：六种探索/利用算子与自适应选择策略增强了搜索效率。
- **实用主义设计**：引入“Cyber Creator”元控制系统，解决了纯进化方法效率低与手工设计灵活性有限的矛盾，具备可扩展性。
- **成本意识**：在提升性能的同时保持成本效率，实际部署可行。

## 8. 不足与局限

- **实验信息不完整**：摘要中缺乏具体数据集、基准、对比方法和消融实验细节，难以独立验证结果的可靠性。
- **未报告资源消耗**：缺少 GPU 算力、训练时间等关键指标，影响可复现性和可比性。
- **未见泛化性分析**：文中未说明该方法在不同规模智能体、不同LLM底座上的表现。
- **可能出现局部最优**：进化算法本身存在收敛到局部最优的风险，课程引导可能引入阶段偏差，需要稳定性约束辅助，但约束强度设置可能依赖经验。
- **应用限制**：该方法适用于任务复杂度可分层且需要专业化协作的场景，对于简单任务或单一智能体即可解决的任务可能过度设计。

（完）
