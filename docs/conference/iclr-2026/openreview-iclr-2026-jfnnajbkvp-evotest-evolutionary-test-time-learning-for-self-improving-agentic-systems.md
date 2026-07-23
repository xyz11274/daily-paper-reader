---
title: "EvoTest: Evolutionary Test-Time Learning for Self-Improving Agentic Systems"
title_zh: EvoTest：面向自改进智能体系统的进化式测试时学习
authors: "Yufei He, Juncheng Liu, Yue Liu, Yibo Li, Tri Cao, Zhiyuan Hu, Xinxing Xu, Bryan Hooi"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=JFnnajbkvP"
tags: ["query:ase"]
score: 9.0
evidence: 直接提出进化式测试时学习方法用于智能体自我改进
tldr: 现有AI智能体在测试时无法快速学习新技能，严重限制了实用性。针对这一局限，本文提出EvoTest框架，通过进化搜索机制让智能体在连续回合中自动优化策略。在J-TTL基准测试上，EvoTest相比反射、记忆和强化学习等传统方法取得了显著提升，为智能体自我进化提供了新路径。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 智能体在陌生环境下无法动态学习，行为像“聪明但无知的实习生”，严重阻碍实际应用。
method: 提出EvoTest框架，利用进化算法在测试时搜索最优策略，使得智能体在连续回合中持续改进。
result: 在J-TTL基准上，EvoTest优于反射、记忆和强化学习等现有自适应方法。
conclusion: 测试时进化学习是推动智能体自进化的有效方向，EvoTest为相关研究提供了新范式。
---

## Abstract
A fundamental limitation of current AI agents is their inability to learn complex skills on the fly at test time, often behaving like “clever but clueless interns” in novel environments. This severely limits their practical utility. To systematically measure and drive progress on this challenge, we first introduce the Jericho Test-Time Learning (J-TTL) benchmark. J-TTL is a new evaluation setup where an agent must play the same game for several consecutive episodes, attempting to improve its performance from one episode to the next. On J-TTL, we find that existing adaptation methods like reflection, memory, or reinforcement learning struggle. To address the challenges posed by our benchmark, we present EvoTest, an evolutionary test-time learning framework that improves an agent without any fine-tuning or gradients—by evolving the entire agentic system after every episode. EvoTest has two roles: the Actor Agent, which plays the game, and the Evolver Agent, which analyzes the episode transcript to propose a revised configuration for the next run. This configuration rewrites the prompt, updates memory by logging effective state–action choices, tunes hyperparameters, and learns the tool-use routines. On our J-TTL benchmark, EvoTest consistently increases performance, outperforming not only reflection and memory-only baselines but also more complex online fine-tuning methods. Notably, our method is the only one capable of winning two games (Detective and Library), while all baselines fail to win any.

---

## 论文详细总结（自动生成）

好的，以下是根据您提供的论文摘要及元数据信息，生成的结构化中文总结。

---

# EvoTest：面向自改进智能体系统的进化式测试时学习

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：当前 AI 智能体在测试时无法动态学习新技能，面对陌生环境时行为类似于“聪明但无知的实习生”，严重限制了实际部署的实用性。
- **研究动机**：亟需一种无需微调或梯度更新的机制，使智能体在连续回合中自动改进策略，实现真正的自我进化。
- **整体含义**：本文提出 **测试时学习（Test-Time Learning）** 的新范式，将智能体的自我改进从训练阶段扩展到推理阶段，为解决智能体在动态环境中的适应性问题提供了新路径。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：通过进化算法在测试时搜索最优策略，使智能体在连续回合中持续自我改进，无需梯度更新或额外微调。
- **框架名称**：**EvoTest**（Evolutionary Test-Time Learning）
- **两个角色**：
  - **Actor Agent（执行智能体）**：负责与环境交互（如玩游戏）。
  - **Evolver Agent（进化智能体）**：分析上一回合的完整日志，提出下一回合的配置更新。
- **配置更新内容**：
  - 重写 prompt（提示词）
  - 更新记忆：记录有效的状态-动作对
  - 调整超参数
  - 学习工具使用例程
- **技术特点**：
  - 无需梯度：完全基于进化搜索。
  - 全系统进化：对整个智能体系统（prompt、记忆、超参数、工具）进行演化，而非仅参数级调整。
- **算法流程（文字说明）**：
  1. 初始化 Actor Agent 和 Evolver Agent 的配置。
  2. Actor Agent 执行第 \(t\) 回合游戏，产生完整日志。
  3. Evolver Agent 分析日志，提出新的配置（包括修改 prompt、更新记忆策略、调整超参数等）。
  4. 应用新配置到 Actor Agent，进入第 \(t+1\) 回合。
  5. 重复直至性能收敛或达到回合数上限。

## 3. 实验设计：数据集、基准和对比方法

- **数据集/场景**：使用文本游戏环境 **Jericho** 作为测试平台。
- **基准**：作者提出了 **J-TTL（Jericho Test-Time Learning）** 基准，要求智能体连续多次游玩同一款游戏，并逐回合提升表现。
- **对比方法**：
  - 反射（Reflection）
  - 记忆（Memory-only）
  - 强化学习（Reinforcement Learning）——即在线微调方法
  - 以及更复杂的在线微调方法
- **结果**：EvoTest 在所有对比方法中一致提升性能，且是唯一能够赢下两款游戏（Detective 和 Library）的方法，所有基线均未能赢下任何一局。

## 4. 资源与算力

- 论文摘要及元数据中 **未明确说明** 使用的 GPU 型号、数量、训练时长等算力信息。
- 仅提及 EvoTest 无需梯度，因此可能比强化学习更节省算力，但具体资源消耗未见量化。

## 5. 实验数量与充分性

- **实验数量**：基于摘要，主要实验在 J-TTL 基准上，覆盖了多款游戏（具体数量未列出，但提到两款游戏获胜）。未提及消融实验或额外的数据集实验。
- **充分性与公平性**：
  - 与反射、记忆、强化学习等主流自适应方法进行了对比，基线设置合理。
  - 唯一能获胜的方法，效果显著。
  - 但缺乏针对不同进化策略（如变异算子、种群大小）的消融实验，也未讨论在不同类型任务（非文本游戏）上的泛化能力。
  - 因此，初步实验充分但不够完备，需要更多维度验证。

## 6. 主要结论与发现

- 测试时进化学习是推动智能体自进化的有效方向。
- EvoTest 在 J-TTL 基准上优于现有自适应方法，无需梯度即可实现持续改进。
- 现有方法（反射、记忆、强化学习）在面对需要跨回合积累技能的任务时困难重重，而进化式搜索能够持续优化系统级配置。

## 7. 优点：方法与实验设计亮点

- **方法创新**：首次将进化算法引入测试时学习，联合优化 prompt、记忆、超参数和工具例程，形成完整的“系统级进化”。
- **无梯度需求**：避免了大模型微调的高计算成本，适合资源受限或无法访问模型参数的场景。
- **实验设计**：J-TTL 基准设计清晰，直接量化了“跨回合学习”能力，填补了相关评估空白。
- **结果突出**：唯一能赢下部分游戏的方法，展示了进化策略在长程依赖任务中的潜力。

## 8. 不足与局限

- **实验覆盖有限**：仅基于 Jericho 文本游戏环境，未在视觉、对话或机器人等更广泛的智能体任务中验证。
- **消融研究缺失**：未单独分析进化中各组件（prompt 重写、记忆更新、超参数调优）的贡献，难以解释具体改进来源。
- **可复现性风险**：未提供模型权重、代码或详细超参数设置，仅给出概念框架。
- **计算资源未公开**：无法评估方法的实际效率与可扩展性。
- **偏差风险**：可能只适用于可拆解为回合制、日志可解析的环境；对于实时或连续控制任务，进化延迟可能成为瓶颈。

---

（完）
