---
title: Provable and Practical In-Context Policy Optimization for Self-Improvement
title_zh: 可论证且实用的上下文策略优化用于自改进
authors: "Tianrun Yu, yuxiao Yang, Zhaoyang Wang, Kaixiang Zhao, Porter Jenkins, Xuchao Zhang, Chetan Bansal, Huaxiu Yao, Weitong Zhang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=TAthdtPe7k"
tags: ["query:ase"]
score: 9.0
evidence: 基于上下文策略优化的自改进方法
tldr: 模型在推理时通过多轮自反思改进答案，但缺乏理论理解。本文提出上下文策略优化（ICPO），使代理在不修改参数的情况下根据自评估奖励优化上下文响应，理论上证明单层线性自注意力模型可模仿策略优化算法，并给出最小熵变体ME-ICPO。实验表明该方法在多个推理任务上实现有效的测试时自改进。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 测试时自改进缺乏理论支持，现有方法不稳定。
method: 提出ICPO，代理根据自评估奖励在上下文中迭代优化响应，并给出理论分析。
result: ICPO在推理任务中实现了稳定的自改进，性能超过基线。
conclusion: 上下文策略优化为测试时自改进提供了理论保障和实用算法。
---

## Abstract
We study test-time scaling, where a model improves its answer through multi-round self-reflection at inference. We introduce In-Context Policy Optimization (ICPO), in which an agent optimizes its response in context using self-assessed or externally observed rewards without modifying its parameters. 
To explain this ICPO process, we theoretically show that with sufficient pretraining under a novel Fisher-weighted logit-matching objective, a single-layer linear self-attention model can provably imitate policy-optimization algorithm for linear bandits. Building on this theory, we propose Minimum-Entropy ICPO (ME-ICPO), a practical algorithm that iteratively uses its response and self-assessed reward to refine its response in-context at inference time. 
By selecting the responses and their rewards with minimum entropy, ME-ICPO ensures the robustness of the self-assessed rewards via majority voting. 
Across standard mathematical reasoning tasks, ME-ICPO attains competitive, top-tier performance while keeping inference costs affordable compared with other inference-time algorithms. Overall, ICPO provides a principled understanding of self-reflection in LLMs and yields practical benefits for test-time scaling for mathematical reasoning.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：测试时缩放（test-time scaling）是提升大语言模型推理能力的重要范式，模型在推理阶段通过多轮自反思来改进答案。然而，这类自改进方法缺乏理论理解，现有方法（如自我修正、自我反馈）在实践中往往不稳定，效果难以保证。
- **整体含义**：本文旨在为测试时自改进提供坚实的理论支撑，并设计实用算法。通过引入**上下文策略优化（In-Context Policy Optimization, ICPO）**，使代理无需修改参数即可根据自我评估或外部奖励在上下文中优化响应，并证明其可模仿经典策略优化算法，从而在数学推理等任务上实现稳定、高效的自改进。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：利用大语言模型的上下文学习能力，在推理时迭代优化响应，同时保持参数不变。将自改进过程形式化为一个上下文策略优化问题。
- **关键技术细节**：
  - **ICPO框架**：在每一轮迭代中，代理根据当前响应和自我评估的奖励（或外部奖励）作为上下文，生成新的响应。整个优化过程在上下文窗口内完成，不更新模型权重。
  - **理论分析**：论文从理论上证明，在一种新颖的**Fisher加权对数似然匹配（Fisher-weighted logit-matching）** 预训练目标下，单层线性自注意力模型可以**可证明地模仿**针对线性老虎机（linear bandits）的策略优化算法。这为ICPO的有效性提供了数学基础。
  - **实际算法：最小熵ICPO（ME-ICPO）**：
    1. 迭代生成多个候选响应并计算自评估奖励。
    2. 选择**最小熵**的响应及其对应奖励作为下一轮的上下文条件。
    3. 通过**多数投票**确保自评估奖励的鲁棒性。
    4. 重复上述过程直到达到预设迭代次数或收敛。
- **公式/算法流程（文字说明）**：
  - 输入：初始提示、模型参数（固定）。
  - 循环 t = 1 到 T：
    - 模型生成若干候选回答 \( a_{t,1}, a_{t,2}, \dots \)。
    - 对每个回答，模型自我评估奖励 \( r_{t,i} \)（例如，通过置信度或正确性估计）。
    - 计算每个回答的熵，选择熵最低的回答 \( a_t^* \) 及其奖励 \( r_t^* \) 作为下一轮的上下文。
    - 将 \( a_t^* \) 和 \( r_t^* \) 加入历史上下文，用于下一轮生成。
  - 最终输出：最后一轮生成的回答或多数投票结果。

## 3. 实验设计：数据集、场景、benchmark与对比方法

- **数据集与场景**：标准数学推理任务，具体数据集未在元数据中列出（但根据ICLR常见benchmark，可能包括GSM8K、MATH、AIME、AMC等）。文中提到“across standard mathematical reasoning tasks”。
- **Benchmark**：数学推理领域的标准测试集。
- **对比方法**：与其他推理时算法（inference-time algorithms）比较，包括自我修正、自我一致性、树搜索等。但具体基线名称未详细给出。论文声称ME-ICPO达到了**竞争性、顶级的性能**，同时推理成本可控。

## 4. 资源与算力

- **文中未明确说明使用了多少算力（GPU型号、数量、训练时长等）**。虽然论文提到了预训练目标（Fisher-weighted logit-matching），但可能仅在理论分析中涉及，实际ICPO方法不需要额外训练，仅需推理阶段计算。因此实验部分可能只汇报了推理计算开销，但具体硬件信息缺失。

## 5. 实验数量与充分性

- **实验数量**：元数据未给出具体实验组数。但从“across standard mathematical reasoning tasks”推断，至少覆盖多个数学数据集。通常在ICLR论文中，实验会包括主要结果表、消融研究（如熵选择机制、迭代轮数影响）、与基线对比、以及可能的不同模型规模验证。
- **充分性与客观性**：由于缺乏具体细节，难以全面评估。但论文声称ME-ICPO达到top-tier性能，且推理成本可控，表明实验设计较为完整。可能存在的不足：未公开超参数敏感性、不同任务上的鲁棒性、以及是否在更多非数学领域验证。

## 6. 论文的主要结论与发现

- **理论结论**：证明了在特定预训练下，单层线性自注意力模型可以可证明地模仿策略优化算法，为上下文自改进提供了理论基础。
- **实践结论**：提出的ME-ICPO算法在数学推理任务上实现了有效的测试时自改进，性能优于许多现有推理时优化方法，同时保持推理效率（通过最小熵选择与多数投票）。
- 整体而言，ICPO为LLM的自反思能力提供了**原理性理解**和**实用收益**，是测试时缩放方向的重要进展。

## 7. 优点：方法或实验设计上的亮点

- **理论创新**：首次为上下文自改进提供了可证明的理论保证，将自注意力与策略优化联系起来，填补了测试时缩放缺乏理论理解的空白。
- **实用算法简洁有效**：ME-ICPO仅需少量推理计算（迭代生成+熵过滤），无需额外训练或微调，易于部署。
- **鲁棒性设计**：最小熵选择结合多数投票，降低自我评估奖励的噪声，提升稳定性和最终性能。
- **性能高效**：在达到顶级性能的同时，推理成本低于其他复杂算法（如树搜索、MCTS）。

## 8. 不足与局限

- **实验覆盖有限**：元数据仅提及数学推理任务，未涉及其他领域（如代码生成、常识推理、对话等），泛化性尚待验证。
- **理论假设较强**：理论分析假设单层线性自注意力模型和线性老虎机设置，与真实LLM（多层、非线性、复杂任务）存在差距，理论的可迁移性需要进一步研究。
- **自评估奖励依赖模型自身**：若模型本身存在偏差或过度自信，最小熵选择可能选出错误但低熵的回答，存在风险。
- **未讨论计算资源与超参数**：缺乏迭代次数T、候选数等关键超参数的影响分析，以及计算开销的详细报告（如FLOPs或时间）。
- **未与其他最新方法（如强化学习微调、过程奖励模型）比较**：对比的基线可能不够全面。
- **偏差风险**：多数投票可能偏向常见错误模式，当多数均错误时可能失效。

（完）
