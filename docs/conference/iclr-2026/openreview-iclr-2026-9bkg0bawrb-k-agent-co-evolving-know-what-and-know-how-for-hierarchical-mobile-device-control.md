---
title: "K²-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control"
title_zh: K²-Agent：面向分层移动设备控制的知什么与知如何共同进化
authors: "Zhe Wu, Donglin Mo, Hongjin Lu, Junliang Xing, Jianheng Liu, Yuheng Jing, Kai Li, Kun Shao, Jianye HAO, Yuanchun Shi"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=9BKg0BAWrb"
tags: ["query:ase"]
score: 9.0
evidence: 通过总结-反思-定位-修正循环实现自进化知识精炼
tldr: 移动设备控制智能体因缺乏任务经验与技能熟悉度而表现不佳。本文提出K²-Agent，通过分离和共同进化陈述性知识与程序性知识来模拟人类认知。高层推理器利用总结-反思-定位-修正循环从单次演示中蒸馏并迭代精炼任务知识，实现自进化。低层执行器通过课程引导组强化学习训练。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有移动设备控制智能体在长程规划和精确操作上表现差，缺乏任务经验与技能熟悉度。
method: 提出分层框架分别处理陈述性和程序性知识，高层通过SRLR循环自进化，低层采用课程强化学习。
result: 在移动设备控制基准上，K²-Agent显著优于先前方法，尤其在高难度任务中。
conclusion: 知识分离与自进化循环是提升智能体复杂任务能力的有效途径。
---

## Abstract
Existing mobile device control agents often perform poorly when solving complex tasks requiring long-horizon planning and precise operations, typically due to a lack of relevant task experience or unfamiliarity with skill execution. We propose $\textbf{K²-Agent}$, a hierarchical framework that models human-like cognition by separating and co-evolving declarative ("knowing what") and procedural ("knowing how") knowledge for planning and execution. K²-Agent’s high level reasoner is bootstrapped from a single demonstration per task and runs a Summarize–Reflect–Locate–Revise (SRLR) loop to distill and iteratively refine task-level declarative knowledge through self-evolution. The low-level executor is trained with our curriculum-guided Group Relative Policy Optimization (C-GRPO), which (i) constructs a balanced sample pool using decoupled reward signals and (ii) employs dynamic demonstration injection to guide the model in autonomously generating successful trajectories for training. On the challenging AndroidWorld benchmark, K$^2$-Agent achieves a new $\textbf{state of the art}$ with $\textbf{76.1\% success rate}$, ranking $\textbf{1st}$ among all methods $\textbf{using only raw screenshots and open-source backbones}$. Furthermore, K²-Agent shows powerful dual generalization: its high-level declarative knowledge transfers across diverse base models, while its low-level procedural skills achieve competitive performance on unseen tasks in ScreenSpot-v2 and Android-in-the-Wild (AitW).

---

## 论文详细总结（自动生成）

# K²-Agent：面向分层移动设备控制的“知什么”与“知如何”共同进化

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有移动设备控制智能体在解决需要长程规划和精确操作的复杂任务时表现不佳，主要原因是缺乏相关任务经验或对技能执行不够熟悉。
- **背景**：移动设备控制是自动化交互的重要场景，但现有方法通常将知识视为整体，导致高层规划与低层执行脱节，难以同时利用“任务知识”和“操作技能”。
- **核心思想**：借鉴人类认知中“陈述性知识（知道什么）”与“程序性知识（知道如何）”的分离与共同进化机制，提出分层框架 K²-Agent，让高层推理器专门处理任务级知识（Know-What），低层执行器专门处理技能级知识（Know-How），并通过自进化循环使两者协同提升。

## 2. 方法论：核心思想、关键技术细节、算法流程
- **核心思想**：将移动设备控制任务建模为“知识分离+共同进化”的分层过程，模拟人类从单次演示中学习任务描述，再通过反复练习精炼技能。
- **高层推理器——SRLR 循环**：
  - 从每个任务的单次演示中启动（bootstrapped）。
  - 运行 **Summarize（总结）– Reflect（反思）– Locate（定位）– Revise（修正）** 四步循环，用于蒸馏和迭代精炼任务级陈述性知识，实现自进化（self-evolution）。
  - 具体：总结当前任务经验，反思失败原因，定位错误步骤，修正知识库，反复迭代直至知识正确。
- **低层执行器——课程引导的组相对策略优化（C-GRPO）**：
  - 利用**解耦奖励信号**构建平衡样本池（balanced sample pool），避免训练样本偏差。
  - 采用**动态演示注入**（dynamic demonstration injection）引导模型自主生成成功的轨迹用于训练。
  - 训练方式为课程学习策略下的组相对策略优化，使执行器逐步学习精确的操作技能。
- **协同进化**：高层知识指导低层执行，低层执行反馈高层反思修正，两层次共同迭代优化。

## 3. 实验设计
- **基准与数据集**：
  - **AndroidWorld**：主要挑战性基准，评估复杂长程任务。
  - **ScreenSpot-v2**：用于评估低层视觉定位技能。
  - **Android-in-the-Wild (AitW)**：用于评估程序性技能在未见任务上的泛化能力。
- **对比方法**：与所有仅使用原始屏幕截图和开源骨干网络的方法进行对比（文中未列出具体对比方法名称，但强调 K²-Agent 排名第1）。
- **评价指标**：成功率（success rate），在 AndroidWorld 上达到 **76.1%**，为新的最先进水平。

## 4. 资源与算力
- 论文文本中**未明确说明**使用的 GPU 型号、数量、训练时长等算力信息。仅能推断其训练涉及强化学习（C-GRPO）和迭代知识精炼，可能对计算资源有一定需求，但具体细节未提供。

## 5. 实验数量与充分性
- **实验覆盖**：在三个不同难度的基准上进行了评估（AndroidWorld、ScreenSpot-v2、AitW），覆盖了复杂长程任务、视觉定位任务和技能泛化任务。
- **消融实验**：摘要未明确提及消融实验数量，但元数据提到“通过总结-反思-定位-修正循环实现自进化知识精炼”可作为消融的证据，具体消融设计未详述。
- **充分性评估**：实验基准选择全面，且展示了双重泛化能力（高层知识跨模型迁移、低层技能跨任务泛化），但缺少对每层次贡献的定量分解、超参数敏感性分析、以及更细粒度错误分析。整体实验设计较为充分，但细节公开有限。

## 6. 主要结论与发现
- K²-Agent 在 AndroidWorld 上以 **76.1% 成功率**取得新 SOTA，显著优于先前方法，尤其在高难度任务中。
- 高层陈述性知识能够跨不同基础模型转移（dual generalization 之一），低层程序性技能在未见任务上表现具有竞争力。
- 知识分离与自进化循环是提升智能体复杂任务能力的有效途径。

## 7. 优点（方法或实验设计亮点）
- **认知启发的分层框架**：将陈述性知识与程序性知识解耦，更符合人类学习过程，具有理论意义。
- **自进化机制**：SRLR 循环仅需单次演示即可启动，通过反思修正不断精炼知识，无需大量标注数据。
- **课程强化学习创新**：C-GRPO 通过解耦奖励和动态演示注入解决了训练样本不平衡和探索困难的问题。
- **泛化能力突出**：高层知识跨模型迁移，低层技能跨任务泛化，展示出实用性。
- **使用原始截图和开源骨干**：不依赖私有模型或结构化表示，可复现性高。

## 8. 不足与局限
- **算力成本未披露**：训练 C-GRPO 和 SRLR 循环的具体资源消耗未知，难以评估其可负担性。
- **实验细节不足**：消融实验、超参数设置、迭代轮次等关键细节未在摘要中说明，削弱了可复现性。
- **仅限移动设备控制**：框架设计针对移动 GUI 交互，是否可推广到机器人、桌面等其他领域未经检验。
- **对单次演示依赖性**：虽然启动成本低，但若演示质量差可能影响初始知识，鲁棒性未分析。
- **偏差风险**：AndroidWorld 等基准可能覆盖不全真实世界多样性，导致过拟合特定任务。

（完）
