---
title: Asymmetric Effects of Self-Corrective Learning on Chain-of-Thought Reasoning for Efficient Policy Adaptation
title_zh: 自我纠正学习对链式思维推理的不对称效应：高效策略适应
authors: "Woo Kyung Kim, Jooyoung Kim, Minjong Yoo, Honguk Woo"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=HfiNG4QCFs"
tags: ["query:ase"]
score: 7.0
evidence: 自我纠正学习用于具身代理适应
tldr: 本文针对LM代理在多样任务上持续适应面临有限监督和资源约束的问题，提出BiCL框架。采用双向链式思维学习联合优化，实现仅用0.5B参数模型和每任务少量数据的持续微调。实验表明该方法能有效适应多个具身任务，为资源受限下的代理持续学习提供新方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: LM代理在多样任务上的持续适应面临挑战，尤其是在有限监督和资源约束下。
method: 提出BiCL框架，通过双向链式思维学习联合优化，实现小模型在少量数据下的持续微调。
result: 仅用0.5B参数模型和少量数据即可实现跨任务适应。
conclusion: 为资源受限下的持续代理适应提供了有效方法。
---

## Abstract
Recent advances in language model (LM)-powered agents have demonstrated the potential to tackle complex embodied tasks by grounding the models’ commonsense world knowledge in the interactive physical environments in which the agents operate. However, these LM-based agents' adaptation to a stream of diverse tasks over time remains challenging, particularly under limited supervision and resource constraints. In this paper, we present BiCL, an embodied task adaptation framework that addresses the problem of continual LM finetuning across diverse tasks and adaptation stages using only a small dataset per task and a small LM (i.e., with 0.5B parameters). We devise bidirectional CoT learning, which jointly optimizes chain-of-thought (CoT) reasoning and reflexive reasoning through per-task bidirectional supervision: few-shot CoT guidance and rationale-wise correction. The latter enables the model to revise its prior rationale trajectories for new tasks, while the former strengthens multi-step task-specific reasoning through minimal demonstrations. This dual optimization allows the agent to adapt more efficiently through forward knowledge transfer over time, ultimately yielding asymmetric effects by fostering robust CoT reasoning at inference without requiring explicit reflection. Furthermore, we implement rationale-wise test-time scaling, a mechanism that dynamically adjusts the depth of CoT reasoning based on the model’s confidence in actions inferred from its own rationales. Through extensive experiments on VirtualHome and ALFWorld, we demonstrate performance superiority over other LM-based planning and continual task adaptation approaches, while achieving strong efficiency in computation, data usage and model parameters.

---

## 论文详细总结（自动生成）

## 论文核心问题与整体含义

- **研究动机**：语言模型（LM）驱动的具身代理在持续适应多样化任务时面临挑战，尤其是在有限监督和资源约束（如少量标注数据、小模型参数）的场景下。
- **核心问题**：如何在小模型（0.5B参数）和每任务少量样本的条件下，实现跨任务的持续微调，并提升推理效率和适应效果。
- **整体含义**：提出双向链式思维学习（BiCL）框架，通过不对称的自我纠正机制，在推理时无需显式反思即可获得鲁棒的链式思维（CoT）推理能力，为资源受限下的持续代理适应提供高效方案。

## 方法论

- **核心思想**：利用每任务的双向监督信号——少量示例的CoT引导（few-shot CoT guidance）和理由级别的修正（rationale-wise correction），联合优化前向推理（CoT推理）与反思推理（reflexive reasoning），实现正向知识迁移，产生不对称效应：训练时使用反思修正，推理时仅依赖鲁棒的CoT推理，无需显式反思。
- **关键技术细节**：
  - **双向CoT学习**：两个方向同时优化。① 前向：通过少量CoT示例强化多步任务特定推理；② 反向：通过理由级别的修正让模型修正先前任务的推理轨迹，从而学习纠正错误。
  - **理由级别测试时缩放（rationale-wise test-time scaling）**：根据模型对自己推理出的动作的置信度，动态调整CoT推理的深度（即推理步骤数或推理链长度），从而在推理时平衡效率与准确性。
- **算法流程（文字描述）**：
  1. 对每个新任务，提供少量带有CoT推理链的示例（前向监督）。
  2. 同时，对模型生成的先前（不同）任务的推理链，利用正确标注进行理由级别修正（反向监督），让模型学习修改错误推理。
  3. 联合优化两个方向的损失，更新小模型参数。
  4. 推理时：模型直接生成CoT推理而不进行显式反思，根据动作置信度动态调整推理深度。

## 实验设计

- **数据集/场景**：VirtualHome 和 ALFWorld 两个具身环境，覆盖多种家庭/室内任务（如整理物品、烹饪等），模拟持续任务流。
- **基准（Benchmark）**：与其他LM-based规划方法和持续任务适应方法对比，包括标准微调、仅前向CoT、反思型推理等方法（具体方法名未在摘要中列出，但提及“other LM-based planning and continual task adaptation approaches”）。
- **对比方法**：包括基于LM的规划基线以及持续适应基线（未给出具体名称，需参考原文）。
- **评估指标**：任务成功率、计算效率（参数规模、数据使用量）等。

## 资源与算力

- 文中明确提到使用**0.5B参数的小模型**（即500M参数），每任务仅使用**少量数据**（未给出具体数量）。
- 未明确说明训练所用的GPU型号、数量、训练时长等算力细节。仅突出参数和数据效率，暗示对算力要求较低。

## 实验数量与充分性

- 实验覆盖两个具身环境（VirtualHome 和 ALFWorld），多个持续任务流。
- 应包含与多种基线方法的对比实验（未列出具体数量）。
- 可能包含消融实验（如去除双向监督、去除测试时缩放等），但摘要未明确提及。
- **充分性评价**：从摘要看，实验覆盖了主流具身任务场景，与多个基线对比，验证了效率和性能。但缺乏详细数据支撑（如具体成功率、方差等），且未提及鲁棒性分析或统计显著性检验。总体来说框架清晰但实验透明度有限。

## 主要结论与发现

- BiCL框架能在**仅用0.5B参数和少量数据**的情况下，在多个连续具身任务上取得优于其他LM规划方法和持续适应方法的性能。
- 不对称效应：训练时进行理由级别修正，推理时无需显式反思，即可获得强健的CoT推理。
- 理由级别测试时缩放进一步提升了推理效率与准确性平衡。
- 在计算效率、数据使用和模型参数方面均表现出强效性。

## 优点

1. **参数高效**：仅使用0.5B小模型，适合资源受限场景。
2. **数据高效**：每任务仅需少量标注样本。
3. **创新机制**：双向CoT学习和不对称效应设计巧妙，训练时利用反思修正，推理时无需额外开销。
4. **动态推理深度**：测试时缩放机制能自适应调整推理复杂度，提升效率。
5. **持续学习能力**：支持跨任务正向知识迁移，避免灾难性遗忘。

## 不足与局限

1. **实验透明度不足**：摘要未提供具体数值结果（如成功率、绝对提升比例）、消融实验设计细节，以及统计显著性说明。
2. **场景覆盖有限**：仅测试了两个模拟环境（VirtualHome 和 ALFWorld），未涉及真实物理机器人或更复杂、开放式的任务。
3. **对比基线不够详细**：未列出具体对比方法的名称和配置，难以评估公平性。
4. **风险偏差**：自我纠正机制可能对初始示范质量敏感，若示范有偏可能导致错误放大；未讨论对噪声标注的鲁棒性。
5. **应用限制**：依赖预先提供的CoT示例和理由修正数据，在某些无法获取高质量解释的任务中可能难以应用。
6. **未讨论超参数敏感性**：如动态缩放阈值、修正强度等关键超参数的影响。

（完）
