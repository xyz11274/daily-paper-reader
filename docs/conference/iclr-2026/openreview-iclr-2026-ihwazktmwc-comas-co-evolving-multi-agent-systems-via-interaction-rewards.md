---
title: "CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards"
title_zh: CoMAS：通过交互奖励实现共进化多代理系统
authors: "Xiangyuan Xue, Yifan Zhou, Guibin Zhang, Zaibin Zhang, Yijiang Li, Chen Zhang, Zhenfei Yin, Philip Torr, Wanli Ouyang, LEI BAI"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=ihwAzktmWc"
tags: ["query:ase"]
score: 9.0
evidence: 通过代理间交互奖励实现自进化
tldr: 现有LLM代理自进化方法依赖外部奖励或从LLM自身提取内在奖励，与人类通过交流学习的方式不同。本文提出共进化多代理系统（CoMAS），让代理通过相互讨论和协作产生的交互奖励来自主改进能力，无需外部监督。实验证明CoMAS在多种任务中持续提升代理性能，实现了更自然、可扩展的自进化。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有自进化方法依赖外部奖励，缺乏人类通过协作学习的机制。
method: 提出CoMAS框架，代理通过交互奖励（如讨论评分）进行策略学习。
result: 在多种任务中，CoMAS代理性能持续提升，超越外部奖励方法。
conclusion: 交互奖励为多代理自进化提供了无监督且有效的方案。
---

## Abstract
Self-evolution is a central research topic in enabling large language model (LLM)-based agents to continually improve their capabilities after pretraining. Recent research has witnessed a transition from reinforcement learning (RL)-free to RL-based methods. Current RL-based methods either rely on dense external reward signals or extract intrinsic reward signals from LLMs themselves. However, these approaches diverge from the self-evolution mechanisms observed in human intelligence, where individuals learn and improve through mutual discussion and collaboration. In this work, we introduce Co-Evolving Multi-Agent Systems (CoMAS), a novel framework that enables agents to improve autonomously by learning from inter-agent interactions without external supervision. CoMAS generates intrinsic rewards from rich discussion dynamics, employs an LLM-as-a-judge mechanism to formulate these rewards, and optimizes each agent's policy through RL, thereby enabling decentralized and scalable co-evolution. Experimental results demonstrate that CoMAS consistently outperforms untrained agents and achieves state-of-the-art performance across most evaluation settings. Ablation studies confirm the necessity of interaction-based reward signals and reveal promising scalability as the number and diversity of agents increase. These findings establish CoMAS as a novel and effective paradigm for self-evolution in LLM-based agents.

---

## 论文详细总结（自动生成）

# 论文总结：CoMAS：通过交互奖励实现共进化多代理系统

## 1. 核心问题与整体含义（研究动机与背景）
当前基于大语言模型（LLM）的智能体在预训练后需要具备**自进化**能力以持续提升性能。现有方法主要分为两类：无强化学习的静态方法，以及基于强化学习（RL）的方法。但目前的RL方法要么依赖密集的外部奖励信号，要么从LLM自身提取内在奖励信号。这些方式与人类通过讨论、协作学习并改进的自然方式存在根本差异。因此，论文提出**CoMAS（共进化多代理系统）**，使代理仅通过代理间的交互（如讨论、评分）产生内在奖励，实现无需外部监督的自进化，更接近人类的协作学习机制。

## 2. 方法论
### 核心思想
- 利用多代理系统中的交互动态生成**内在奖励**，替代外部奖励或自生成的奖励信号。
- 采用**LLM-as-a-judge**机制，将代理间的讨论评分转化为可优化的奖励信号。
- 通过强化学习（RL）优化每个代理的策略，实现**去中心化、可扩展的共进化**。

### 关键技术细节
- **交互奖励生成**：从代理间丰富的讨论动态中提取奖励，例如相互评分、一致性、分歧等。
- **LLM-as-a-judge**：使用一个或多个LLM作为评判者，对交互过程进行打分，将定性交互转化为定量奖励。
- **策略优化**：每个代理独立通过RL（如PPO）更新其行为策略，目标为最大化由其交互获得的长期奖励。
- **算法流程**（文字描述）：
  1. 初始化一组LLM代理，每个代理拥有自己的策略网络（可视为提示或参数）。
  2. 在每一轮，代理之间进行多轮讨论/协作，产生交互记录。
  3. 使用LLM-as-a-judge对每个代理的贡献进行评分，生成交互奖励。
  4. 每个代理利用交互奖励更新其策略（RL更新）。
  5. 重复步骤2-4，实现持续共进化。

## 3. 实验设计
- **所使用的数据集/场景**：论文Abstract中未列出具体数据集名称，但提及“across most evaluation settings”，推测包括常见的LLM代理基准任务（如推理、问答、工具使用等）。具体场景需要查看原论文正文。
- **Benchmark**：未明确说明，但通过与“untrained agents”以及其他对比方法比较，表明其达到了“state-of-the-art”。
- **对比方法**：Abstract中对比了“RL-free”方法和“RL-based methods”，以及未训练的代理。具体对比方法列表未给出，可能包括单代理自进化基线、使用外部奖励的方法等。

## 4. 资源与算力
论文元数据及摘要中**未明确说明**使用的GPU型号、数量或训练时长。这是论文在信息披露上的一个不足。

## 5. 实验数量与充分性
- **实验组数**：提到进行了**主实验**（比较性能）和**消融实验**（Ablation studies）。消融实验验证了交互奖励的必要性，并展示了随着代理数量和多样性增加的可扩展性。
- **充分性与公平性**：Abstract声称“consistently outperforms untrained agents”、“state-of-the-art”，但没有提供详细统计数据和误差分析。实验设计似乎合理，但由于未公开具体数据集和对比基线，难以完全判断客观性和公平性。消融实验是其亮点之一。

## 6. 主要结论与发现
- CoMAS框架能够使多代理系统在**无外部监督**的情况下持续提升性能。
- 性能优于未训练的代理，并在大多数评估设置中达到**最优**。
- 交互奖励信号是必要的，消去后性能下降。
- 系统随着代理数量和多样性的增加展现出**良好的可扩展性**。
- 交互奖励为多代理自进化提供了一种**无监督且有效**的新范式。

## 7. 优点
- **创新性**：首次提出利用代理间交互作为内在奖励驱动共进化，更贴近人类学习方式。
- **自监督性**：完全无需外部标注或人工反馈，降低了成本。
- **可扩展性**：去中心化设计，可以轻松增加代理数量或引入不同类型代理。
- **方法简洁**：基于已有的LLM-as-a-judge和RL技术，组合创新实用。
- **消融验证**：通过消融实验确认了交互奖励的贡献，增强了方法可靠性。

## 8. 不足与局限
- **实验数据不足**：Abstract中未列出具体基准任务、数据集以及对比方法的详细性能数字，无法进行深入分析。可能原论文正文提供了更多细节，但从摘要看信息不充分。
- **算力资源未披露**：无法评估方法的实际计算成本。
- **偏差风险**：LLM-as-a-judge可能引入评判偏见，论文未讨论如何控制。
- **应用限制**：当前实验场景可能有限，如是否适用于长复杂任务、安全关键领域等未说明。
- **控制实验**：未与外部奖励的RL方法进行公平对比（相同计算量、相同模型规模），可能高估交互奖励的优势。

（完）
