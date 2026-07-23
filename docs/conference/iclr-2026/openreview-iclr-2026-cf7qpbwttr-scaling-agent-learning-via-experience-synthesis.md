---
title: Scaling Agent Learning via Experience Synthesis
title_zh: 通过经验合成扩展代理学习
authors: "Zhaorun Chen, Zhuokai Zhao, Kai Zhang, Bo Liu, Qi Qi, Yifan Wu, Tarun Kalluri, Xuefei Cao, Yuanhao Xiong, Haibo Tong, Huaxiu Yao, Hengduo Li, Jiacheng Zhu, Xian Li, Dawn Song, Bo Li, Jason E Weston, Dat Huynh"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=cf7qpBwttr"
tags: ["query:ase"]
score: 7.0
evidence: 合成经验实现可扩展的RL自改进
tldr: 强化学习使代理能通过交互自改进，但实际部署面临成本高、任务多样性有限等挑战。本文提出DreamGym，首个统一框架通过推理式经验模型合成多样化的状态转移和反馈信号，替代真实环境交互。该合成经验可支持大规模在线RL训练，使代理能高效自改进，同时避免真实部署的昂贵开销。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 在线RL面临环境交互成本高、经验数据缺乏多样化等扩展瓶颈。
method: DreamGym将环境动力学蒸馏为推理式经验模型，合成多样化经验用于RL训练。
result: 合成经验驱动的RL在多个代理任务上达到或超过真实交互训练的性能。
conclusion: 经验合成是一种可扩展的自改进训练范式。
---

## Abstract
While reinforcement learning (RL) can empower autonomous agents by enabling self-improvement through interaction, its practical adoption remains challenging due to costly rollouts, limited task diversity, unreliable reward signals, and infrastructure complexity, all of which obstruct the collection of scalable experience data. To address these challenges, we introduce DreamGym, the first unified framework designed to synthesize diverse experiences with scalability in mind to enable effective online RL training for autonomous agents. Rather than relying on expensive real-environment rollouts, DreamGym distills environment dynamics into a reasoning-based experience model that derives consistent state transitions and feedback signals through step-by-step reasoning, enabling scalable agent rollout collection for RL. To improve the stability and quality of transitions, DreamGym leverages an experience replay buffer initialized with offline real-world data and continuously enriched with fresh interactions to actively support agent training. To improve knowledge acquisition, DreamGym adaptively generates new tasks that challenge the current agent policy, enabling more effective online curriculum learning. Experiments across diverse environments and agent backbones demonstrate that DreamGym substantially improves RL training, both in fully synthetic settings and in sim-to-real transfer scenarios. On non-RL-ready tasks like WebArena, DreamGym outperforms all baselines by over 30%. And in RL-ready but costly settings, it matches GRPO and PPO performance using only synthetic interactions. When transferring a policy trained purely on synthetic experiences to real-environment RL, DreamGym yields significant additional performance gains while requiring far fewer real-world interactions, providing a scalable warm-start strategy for general-purpose RL.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：强化学习（RL）虽能通过交互实现代理自改进，但实际部署面临诸多瓶颈，包括真实环境交互成本高昂、任务多样性有限、奖励信号不可靠以及基础设施复杂，导致无法收集可扩展的经验数据。
- **整体含义**：为突破上述扩展性障碍，本文提出**DreamGym**——首个统一框架，通过**经验合成**（Experience Synthesis）替代真实环境交互，为代理提供大规模、多样化的合成经验，从而高效驱动在线RL训练，实现可扩展的自改进。

## 2. 论文提出的方法论

- **核心思想**：将环境动力学蒸馏为一个**推理式经验模型**（reasoning-based experience model），该模型通过逐步推理产生一致的状态转移和反馈信号，代替真实环境中的 rollout，从而支持大规模合成经验生成。
- **关键技术细节**：
  - **推理式经验模型**：基于离线真实世界数据初始化，再通过连续注入新鲜交互动态更新，保持转移和反馈的稳定性和质量。
  - **经验回放缓冲区**（Experience Replay Buffer）：初始化时使用离线真实数据，训练过程中持续填充合成交互，主动支持代理训练。
  - **自适应任务生成**：根据当前代理策略自动生成更具挑战性的新任务，实现高效的**在线课程学习**（online curriculum learning），提升知识获取效率。
- **算法流程（文字描述）**：
  1. 从真实环境中收集少量离线经验，初始化经验模型和回放缓冲区。
  2. 利用推理式经验模型合成大量状态转移和奖励信号，生成多样化经验。
  3. 在合成经验上执行在线RL训练（如PPO、GRPO等），同时不断从合成环境中采样新交互，更新回放缓冲区。
  4. 自适应生成难度递增的任务，引导代理逐步掌握更复杂技能。
  5. 训练完成后，可将纯合成经验训练的策略迁移至真实环境进行微调，显著减少真实交互次数。

## 3. 实验设计

- **使用的环境/场景**：
  - **WebArena**（非RL-ready任务）：需要复杂网页交互的基准测试。
  - 其他多样环境（论文摘要提及"diverse environments and agent backbones"），但具体名称未在摘要中列出，推测包括经典RL基准（如Atari、MuJoCo等）。
- **基准方法对比**：
  - 对比了**GRPO**（Group Relative Policy Optimization）和**PPO**（Proximal Policy Optimization）等标准在线RL方法。
  - 在WebArena上，DreamGym超越所有基线方法**超过30%**。
  - 在RL-ready但交互成本高的设置中，DreamGym仅使用合成交互就匹配了GRPO和PPO的性能。
- **迁移实验**：将纯合成经验训练的策略迁移至真实环境RL，获得显著额外性能提升，且所需真实交互大幅减少，可作为通用RL的**可扩展热启动**策略。

## 4. 资源与算力

- **文中未明确说明**：摘要及元数据中未提及所使用的GPU型号、数量、训练时长等具体算力信息。需查阅完整论文正文以获取相关细节。

## 5. 实验数量与充分性

- **实验数量**：从摘要可知，实验覆盖了**多类环境**（包括WebArena等非RL-ready场景和RL-ready低成本场景）以及**多种代理主干**（agent backbones），同时包含了**合成-真实迁移实验**。但未列出具体消融实验数量或不同任务数量。
- **充分性评估**：
  - **优点**：同时评估了全合成设置和sim-to-real迁移，证明了框架的通用性和实际价值。
  - **不足**：缺少对单个组件（如推理式模型、自适应任务生成等）的消融分析，也未说明是否在多个独立随机种子下重复实验（以减少方差）。实验设计的详细度和统计严谨性需通过全文进一步确认。

## 6. 论文的主要结论与发现

- **主要结论**：经验合成是一种**可扩展的自改进训练范式**。DreamGym通过合成经验驱动的RL，在多个代理任务上达到或超过真实交互训练的性能。
- **关键发现**：
  - 合成经验可完全替代真实环境rollout用于在线RL训练，且性能不降（在RL-ready任务上匹配GRPO/PPO）。
  - 在非RL-ready任务（如WebArena）上优势巨大，提升超过30%。
  - 合成-真实迁移策略可实现**更少的真实交互 + 更大的性能增益**，为通用RL提供了高效的热启动方案。

## 7. 优点

- **创新性**：首次提出统一的**推理式经验模型**用于合成多样化状态转移和奖励，突破了环境交互瓶颈。
- **可扩展性**：合成经验生成成本低，可无限量产生，支持大规模在线训练。
- **实用性**：同时适用于非RL-ready任务和RL-ready任务，且能无缝迁移到真实环境，降低部署代价。
- **自适应课程学习**：动态生成符合当前策略水平的任务，提升学习效率。
- **性能突出**：在多个场景下显著超越现有基线，验证了方法有效性。

## 8. 不足与局限

- **实验覆盖有限**：仅摘要中明确提到的环境为WebArena，其他环境具体类别及数量未交代，可能缺乏通用性验证。
- **消融实验缺失**：未说明是否对推理式模型结构、回放缓冲区大小、任务生成策略等进行消融分析，难以评估各组件贡献。
- **算力与效率未报告**：没有提供合成经验生成的额外计算开销与真实环境rollout成本的对比，可能影响实际部署评估。
- **偏差风险**：合成经验模型可能继承离线数据的偏见，导致在分布外任务上泛化不足（文中未针对此分析）。
- **应用限制**：对于需要物理交互或高精度环境建模的任务（如机器人控制），合成模型的保真度可能不足，文中未讨论此类场景。

（完）
