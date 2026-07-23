---
title: "MoSEL: Modular Self-Reflective Learning for Embodied Decision-Making"
title_zh: MoSEL：面向具身决策的模块化自反思学习
authors: "Jr-Jen Chen, Yu-Chiang Frank Wang, Yilun Du"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=QVjyFrXOrn"
tags: ["query:ase"]
score: 7.0
evidence: 模块化自反思学习用于具身决策
tldr: 机器人执行长程任务需要层次推理和动态适应，但现有系统无法自主从经验中学习。本文提出模块化自反思学习框架MoSEL，融合LVLM、视频扩散和逆动力学模型进行层次规划，并通过自反思模块从执行结果中学习改进。实验证明MoSEL使机器人能自主适应新任务场景，减少人为干预。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 机器人无法像人类一样从经验中自主学习和适应。
method: 结合多模态基础模型进行层次规划，并引入自反思模块评估和改进。
result: 在长程操作任务中，MoSEL显著提升成功率并减少人工监督。
conclusion: 模块化自反思学习是赋予机器人自主进化能力的关键。
---

## Abstract
Enabling robots to autonomously perform complex, long-horizon tasks remains challenging due to the need for hierarchical reasoning and dynamic adaptability. Humans overcome this by interacting with environment and learning from their own experience, which is infeasible for existing robots without human supervision. To enable similar capabilities in robotic agents, we introduce MoSEL, an modular self-reflective learning framework for robotic decision making. MoSEL combines hierarchical planning with multimodal foundation models, including LVLMs, video diffusion, and inverse dynamics models. These components work together to break down complex tasks, generate executable visual plans, and perform actions. We further introduce a modular self-reflective learning framework that autonomously identifies failures and iteratively refines policies with minimal human intervention. Evaluations on LIBERO-LONG and RoboTwin benchmarks demonstrate that MoSEL outperforms existing methods, achieving over $33\%$ and $46\%$ average performance improvements, respectively. Our results underscore the effectiveness of autonomous self-improvement and accurate failure identification in advancing robust robotic manipulation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：机器人执行复杂、长程（long-horizon）任务时面临层次推理与动态适应的挑战。现有机器人系统无法像人类一样通过与环境交互并从自身经验中自主学习，通常需要大量人工监督。
- **整体含义**：本文旨在赋予机器人自主从经验中学习与改进的能力，减少人为干预，使机器人能够适应新任务场景，实现具身智能体的自主进化。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：提出**模块化自反思学习框架（MoSEL）**，将层次规划与多模态基础模型结合，并引入自反思模块，使机器人从执行结果中识别失败、迭代改进策略。
- **关键技术细节**：
  - **层次规划**：将复杂任务分解为子任务，生成可执行的视觉计划。
  - **多模态基础模型**：包括大型视觉语言模型（LVLM）、视频扩散模型（Video Diffusion）以及逆动力学模型（Inverse Dynamics Model）。
    - LVLM：用于任务理解和高层次推理。
    - 视频扩散模型：生成未来动作的视觉预测（视觉计划）。
    - 逆动力学模型：将视觉计划映射为具体动作。
  - **模块化自反思学习**：自动识别执行过程中的失败，并基于反思结果对策略进行迭代细化，仅需最少的人工介入。过程可描述为：执行 → 失败检测 → 反思 → 策略更新 → 重试。

## 3. 实验设计
- **使用的数据集/场景**：LIBERO-LONG 和 RoboTwin 两个基准（benchmark）。
- **对比方法**：未明确列出具体对比方法名称，但提到“现有方法”（existing methods），在评估中MoSEL优于这些方法。
- **实验内容**：在长程操作任务上评估成功率，并验证自主故障识别的准确性。

## 4. 资源与算力
- **未明确说明**：文中未提及使用的GPU型号、数量、训练时长等算力信息。元数据及摘要均无相关描述。

## 5. 实验数量与充分性
- **实验数量**：在两个基准（LIBERO-LONG 和 RoboTwin）上进行了评估，未明确说明消融实验数量。但摘要提到“超过33%和46%的平均性能提升”，表明有定量比较。
- **充分性评价**：实验覆盖了至少两个主流长程任务基准，但缺乏对消融研究的详细描述（例如不同模块贡献、反思机制的影响）。对比方法未指明具体路线，公平性有待验证。整体实验设计基本合理，但充分性一般，缺少更细粒度的分析。

## 6. 主要结论与发现
- MoSEL在LIBERO-LONG和RoboTwin上分别取得了超过33%和46%的平均性能提升，显著优于现有方法。
- 自主自改进与准确的失败识别是提升机器人操作鲁棒性的关键。
- 模块化自反思学习框架能够有效减少人工监督，使机器人具备自主适应能力。

## 7. 优点
- **方法上的亮点**：
  - 创新地结合LVLM、视频扩散和逆动力学模型进行层次规划，结构清晰。
  - 自反思模块使机器人能从经验中学习，无需大量人类示范或人工反馈。
  - 模块化设计便于各组件独立升级或替换。
- **实验上的亮点**：
  - 在多个长程任务基准上验证，提升幅度显著（>33%和>46%），说服力较强。

## 8. 不足与局限
- **实验覆盖不足**：缺乏对不同任务类型、不同环境动态性的测试；仅两个基准，可能无法代表真实世界的多样性。
- **对比方法不透明**：未列出具体对比的方法名称，难以重现与判断公平性。
- **偏差风险**：自主失败检测的准确率是否受任务复杂度影响？文中未分析失败情况下的误报/漏报。
- **应用限制**：依赖多种基础模型（LVLM、扩散模型等），计算资源需求可能较高；且反思学习仅针对失败情况，未考虑探索新策略的主动学习。
- **算力信息缺失**：无法评估方法的实际部署成本。

（完）
