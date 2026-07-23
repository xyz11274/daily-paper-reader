---
title: Towards Agentic Self-Learning LLMs in Search Environment
title_zh: 搜索环境中代理自学习LLM的实现
authors: "Wangtao Sun, Xiang Cheng, Jialin Fan, Yao Xu, XingYu, Shizhu He, Jun Zhao, Kang Liu"
date: 2025-09-16
pdf: "https://openreview.net/pdf?id=ySSq8Yavs4"
tags: ["query:ase"]
score: 9.0
evidence: 无人工干预的代理自学习
tldr: 本文研究无需人工数据集或预定义奖励的LLM代理自学习。通过搜索环境实验，发现生成式奖励模型优于规则信号，且合成数据可提升能力。提出代理自学习(ASL)框架，包含生成式奖励模型与策略共进化的全闭环多角色强化学习。为完全自主的代理学习提供了可扩展方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有LLM代理训练依赖人工数据集或预定义奖励，限制规模化自我提升。
method: 提出代理自学习(ASL)框架，包含生成式奖励模型与策略共进化，全闭环多角色强化学习。
result: 发现生成式奖励模型优于规则信号，合成数据可提升代理能力。
conclusion: 为完全自主的代理学习提供了可扩展方案。
---

## Abstract
We study whether self-learning can scale LLM-based agents without relying on human-curated datasets or predefined rule-based rewards. Through controlled experiments in a search-agent setting, we identify two key determinants of scalable agent training: the source of reward signals and the scale of agent task data. We find that rewards from a Generative Reward Model (GRM) outperform rigid rule-based signals for open-domain learning, and that co-evolving the GRM with the policy further boosts performance. Increasing the volume of agent task data—even when synthetically generated—substantially enhances agentic capabilities. Building on these insights, we propose Agentic Self-Learning (ASL), a fully closed-loop, multi-role reinforcement learning framework that unifies task generation, policy execution, and evaluation within a shared tool environment and LLM backbone. ASL coordinates a Prompt Generator, a Policy Model, and a Generative Reward Model to form a virtuous cycle of harder task setting, sharper verification, and stronger solving. Empirically, ASL delivers steady, round-over-round gains, surpasses strong RLVR baselines (e.g., Search-R1) that plateau or degrade, and continues improving under zero-labeled-data conditions, indicating superior sample efficiency and robustness. We further show that GRM verification capacity is the main bottleneck: if frozen, it induces reward hacking and stalls progress; continual GRM training on the evolving data distribution mitigates this, and a small late-stage injection of real verification data raises the performance ceiling. This work establishes reward source and data scale as critical levers for open-domain agent learning and demonstrates the efficacy of multi-role co-evolution for scalable, self-improving agents. The data and code of this paper are released at https://anonymous.4open.science/r/Towards-Agentic-Self-Learning-4D63

---

## 论文详细总结（自动生成）

好的，以下是对给定论文的详细中文总结，严格遵循您要求的要点和格式。

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：当前基于大语言模型（LLM）的智能代理（Agent）训练严重依赖人工策划的数据集或预定义的基于规则的奖励函数，这限制了代理的规模化自我提升能力和在开放域环境中的泛化性。论文旨在探索LLM代理能否通过自学习（Self-Learning）实现完全自主的进化，无需人工干预。
- **整体含义**：本文通过搜索环境下的受控实验，识别出可扩展代理训练的两个关键决定因素：**奖励信号源**（生成式奖励模型优于规则信号）和**任务数据规模**（即使是合成数据也能显著提升能力）。在此基础上，提出了“代理自学习（ASL）”框架，证明通过多角色（提示生成器、策略模型、奖励模型）共进化的全闭环强化学习，可以实现零标注数据下的稳步提升。这为构建完全自主、可扩展的LLM代理学习范式提供了理论和实践基础。

### 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：构建一个完全闭环的多角色强化学习框架（ASL），让三个核心组件（提示生成器、策略模型、生成式奖励模型）在共享的工具环境和LLM骨干网络上协同进化，形成“生成更难的任务→更精确的验证→更强的解决问题能力”的良性循环。
- **关键技术细节**：
    - **三个角色**：
        1.  **提示生成器（Prompt Generator）**：负责生成难度递进的搜索任务（基于Query?）。
        2.  **策略模型（Policy Model）**：作为实际执行任务的代理，生成动作（如搜索、推理、回答）。
        3.  **生成式奖励模型（Generative Reward Model, GRM）**：代替规则信号，对策略模型的输出进行开放式、细粒度的质量评判，提供更丰富的训练信号。
    - **共进化机制**：GRM与策略模型在训练过程中动态协同进化。策略模型在越来越难的任务上训练，而GRM相应地在策略模型生成的轨迹分布上持续进行训练，以保持验证能力与策略能力同步提升。这避免了固定奖励模型可能导致的“奖励黑客”（reward hacking）问题。
    - **全闭环流程**：一个训练轮次包含：任务生成（提示生成器）→策略执行→GRM评估→策略模型基于GRM奖励进行强化学习更新→（可选）若GRM也参与训练，则更新GRM。此过程循环进行。

### 3. 实验设计：使用的数据集/场景、Benchmark、对比方法
- **应用场景**：搜索环境（Search Environment），具体是开放域问答或信息检索任务（论文摘要未指明具体Benchmark名称，需以实际论文为准，但场景明确）。
- **Benchmark**：文中未明确公布Benchmark名称，但通过**对比强RLVR基线（如Search-R1）** 来验证ASL的有效性。
- **对比方法**：
    - **强基线**：Search-R1（一种基于规则的奖励+强化学习的方法）。
    - **消融对照组**：
        - 使用规则信号而非GRM进行奖励。
        - 使用冻结（不更新）的GRM。
        - 不同规模的任务数据（小规模 vs 大规模）。
        - 不同GRM初始化的版本。
- **实验设置**：在搜索环境中，比较ASL与上述方法在多个训练轮次后的性能变化。特别关注了零标注数据（zero-labeled-data）条件下的表现。

### 4. 资源与算力
- **文中未明确说明**：论文摘要和元数据中没有提及所使用的GPU型号、数量、训练时长等具体算力信息。这属于论文的未公开细节。

### 5. 实验数量与充分性
- **实验数量**：虽然未列出具体组数，但从摘要描述可推断实验数量较为充分：
    - 关键发现验证实验：对比GRM vs 规则信号（至少一组）。
    - 规模效应实验：不同任务数据量对比。
    - 共进化有效性实验：GRM固定 vs 持续训练（消融实验）。
    - 与强基线对比实验：ASL vs Search-R1。
    - 最后针对GRM瓶颈的验证实验（注入少量真实验证数据）。
- **充分性与公平性**：
    - **充分**：覆盖了核心变量（奖励来源、数据规模、GRM更新策略），对关键瓶颈进行了剖析，提供了多轮次/持续提升的实验证据。
    - **客观公平**：明确指出ASL“优于强RLVR基线（如Search-R1）”，后者在后期出现平台期或退化，而ASL持续改进。消融实验证明了各组件（GRM、共进化、数据规模）的必要性。评价标准应基于任务成功率或质量指标。

### 6. 论文的主要结论与发现
1.  **奖励信号源是关键**：生成式奖励模型（GRM）提供的开放式奖励信号，显著优于刚性基于规则的信号（如Search-R1），尤其在开放域学习中。
2.  **共进化提升性能**：将生成式奖励模型（GRM）与策略模型进行共进化（持续训练），比固定GRM带来更大的性能提升。
3.  **数据规模效应显著**：增加代理任务数据量——即使是**合成生成**的数据——也能大幅增强代理能力。
4.  **ASL框架有效**：所提出的全闭环多角色强化学习框架ASL能够实现**稳步的、轮次间的持续提升**，超越了对比的强基线，且在**零标注数据**条件下也能持续改进，展现了优越的样本效率和鲁棒性。
5.  **GRM验证能力是主要瓶颈**：如果GRM被冻结（不更新），会诱导“奖励黑客”问题，导致训练停滞。对GRM在演化的数据分布上进行**持续训练**能缓解此问题，且**在训练后期注入少量真实验证数据**能进一步提高性能天花板。

### 7. 优点：方法或实验设计上的亮点
- **方法亮点**：
    - **完全自主性**：实现了无需任何人工数据集或预定义奖励的“自学习”，极大降低了人力成本和领域限制。
    - **闭环多角色协同**：提示生成器、策略、GRM三者共进化的设计，模拟了“教学相长”的良性循环，解决了固定奖励模型的天花板问题。
    - **实用性**：明确指出GRM持续训练是瓶颈并给出解决方案（后期少量注入真实数据），为实际部署提供了可操作的指导。
- **实验亮点**：
    - **聚焦于因果变量**：通过控制变量法清晰揭示了奖励来源和数据规模两个关键因素的作用。
    - **零资源评估**：评价了模型在完全无监督环境下的学习能力，具有很强的现实意义。

### 8. 不足与局限
- **场景单一**：所有实验均在**搜索环境**中进行，结论是否能泛化到其他复杂代理任务（如工具使用、多步规划、代码生成）尚需验证。
- **算力成本未提及**：多角色共进化框架（三个模型同时训练）的计算资源消耗远大于单策略模型训练，论文未讨论其训练效率或是否过重。
- **数据合成质量**：合成数据虽然能提升能力，但论文未深入分析如何保证合成任务的质量与多样性，以及在低质量合成数据下框架的鲁棒性。
- **瓶颈分析依赖后注入**：虽然发现了GRM瓶颈，但解决方案依赖后期注入“少量真实验证数据”，这在一定程度上打破了“完全零标注”的纯洁性。
- **缺乏大规模域间验证**：只在单一领域（搜索）内进行了实验，未进行跨领域迁移或通用性验证。

（完）
