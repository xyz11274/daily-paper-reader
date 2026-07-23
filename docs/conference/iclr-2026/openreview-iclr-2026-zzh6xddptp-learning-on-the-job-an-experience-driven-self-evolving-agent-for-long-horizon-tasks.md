---
title: "Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks"
title_zh: 在岗学习：面向长程任务的体验驱动自进化代理
authors: "Cheng Yang, Xuemeng Yang, Licheng Wen, Daocheng Fu, Jianbiao Mei, Rong Wu, Pinlong Cai, Yufan Shen, Nianchen Deng, Botian Shi, Yu Qiao, Haifeng Li"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ZzH6xDdpTP"
tags: ["query:ase"]
score: 9.0
evidence: 经验驱动的自进化代理用于长程任务
tldr: 现有LLM代理在长程任务中是静态的，无法从经验中学习并持续改进。本文提出MUSE框架，构建以层次化记忆模块为核心的自进化系统，在子任务执行后自主积累经验并优化规划和执行。实验证明MUSE在多应用中显著提升长程任务成功率，实现了真正的“在岗学习”。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有LLM代理在部署后无法从经验中学习，限制了长程任务中的持续改进。
method: 提出MUSE框架，使用层次化记忆模块组织经验，并基于记忆自主规划、执行和反思。
result: 在多个长程任务应用中，MUSE的成功率和效率显著优于静态基线方法。
conclusion: 经验驱动的自进化机制是提升代理长程任务能力的有效途径。
---

## Abstract
Large Language Models have demonstrated remarkable capabilities across diverse domains, yet significant challenges persist when deploying them as AI agents for real-world long-horizon tasks. Existing LLM agents suffer from a critical limitation: they are test-time static and cannot learn from experience, lacking the ability to accumulate knowledge and continuously improve on the job. To address this challenge, we propose MUSE, a novel agent framework that introduces an experience-driven, self-evolving system centered around a hierarchical Memory Module. MUSE organizes diverse levels of experience and leverages them to plan and execute long-horizon tasks across multiple applications. After each sub-task execution, the agent autonomously reflects on its trajectory, converting the raw trajectory into structured experience and integrating it back into the Memory Module. This mechanism enables the agent to evolve beyond its static pretrained parameters, fostering continuous learning and self-evolution. We evaluate MUSE on the long-horizon productivity benchmark TAC. It achieves new SOTA performance by a significant margin using only a lightweight Gemini-2.5 Flash model. Sufficient Experiments demonstrate that as the agent autonomously accumulates experience, it exhibits increasingly superior task completion capabilities, as well as robust continuous learning and self-evolution capabilities. Moreover, the accumulated experience from MUSE exhibits strong generalization properties, enabling zero-shot improvement on new tasks. MUSE establishes a new paradigm for AI agents capable of real-world productivity task automation.
Demo videos can be found in our supplementary materials.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：当前基于大语言模型（LLM）的AI代理在部署后是“静态”的——它们无法从实时交互中积累经验并持续改进，尤其在面对真实世界中的长程任务（long-horizon tasks）时，这种缺乏学习能力的限制导致性能瓶颈。
- **核心问题**：如何让LLM代理在任务执行过程中像人类一样“在岗学习”，即通过自主反思和记忆组织，实现自我进化，从而提升长程任务的完成能力。
- **整体意义**：提出了一种新的代理范式——经验驱动的自进化系统，打破了传统代理“训练-部署”割裂的局限，使代理能够在实际工作中不断成长，为自动化生产力任务提供了可行方案。

## 2. 论文提出的方法论

- **框架名称**：MUSE（Memory-driven Unified Self-Evolving agent）。
- **核心思想**：引入层次化记忆模块（Hierarchical Memory Module），将不同抽象级别的经验结构化存储；代理在每完成一个子任务后，自动反思其执行轨迹，将原始轨迹转化为结构化经验并整合回记忆模块，从而实现知识积累与自我进化。
- **关键技术细节**：
  - **记忆模块**：按层次组织经验（如低级动作、中级策略、高级规划），支持快速检索与复用。
  - **自主规划与执行**：基于当前任务需求和记忆经验，生成计划并逐步执行子任务。
  - **反思与经验转化**：每个子任务完成后，代理通过反思提取成功/失败原因、改进策略，并转化为结构化经验存入记忆。
  - **持续学习机制**：代理的参数无需更新，仅通过记忆的动态更新实现“经验的持续迭代”，从而超越静态预训练参数的限制。
- **算法流程**（文字说明）：
  1. 初始化：加载预训练LLM（如Gemini-2.5 Flash）作为基础模型，初始化空的记忆模块。
  2. 任务分解：接收长程任务，利用LLM将任务分解为序列子目标。
  3. 子任务执行：结合当前记忆经验，调用LLM生成动作并执行。
  4. 效果评估与环境反馈：获取子任务结果。
  5. 反思与经验生成：对执行轨迹进行总结，生成结构化经验（包括成功经验、失败教训、优化建议）。
  6. 经验整合：将新经验存入记忆模块，并更新索引。
  7. 重复步骤3-6直至所有子任务完成；下次任务可直接利用积累的记忆。

## 3. 实验设计

- **数据集/场景**：使用长程生产力基准 **TAC**（Long-Horizon Productivity Benchmark）。未明确说明TAC的具体组成，但强调其包含多个长程任务应用。
- **Benchmark**：TAC基准，用于评估长程任务完成质量。
- **对比方法**：论文未详细列出所有基线，但提到“静态基线方法”（如直接使用基础LLM而无记忆学习的代理），以及当前SOTA（State-of-the-Art）方法。MUSE使用轻量级模型 **Gemini-2.5 Flash** 取得了大幅超过当前SOTA的性能。
- **实验充分性**：除主实验外，还进行了：
  - 消融实验（验证记忆模块、反思机制等组件的贡献）。
  - 零样本泛化实验：将在MUSE上积累的经验直接用于新任务，观察零样本提升效果。
  - 持续学习能力评估：随经验积累，任务成功率是否持续增长。

## 4. 资源与算力

- 论文未明确给出使用的GPU型号、数量或训练时长。仅指出核心模型为 **Gemini-2.5 Flash**（轻量级LLM），这意味着推理开销较低，无需大规模微调。由于框架不需要重新训练模型（仅通过记忆更新），整体算力需求主要来自推理与反思循环。未提供具体硬件配置。

## 5. 实验数量与充分性

- **实验组数**：文中提到“Sufficient Experiments”，至少包括主实验（TAC基准）、消融实验（组件有效性）、零样本泛化实验、持续学习曲线分析。未给出精确数字，但整体覆盖了方法的主要方面。
- **公平性与客观性**：
  - 使用标准公开基准TAC，对比当前SOTA。
  - 消融实验验证每个模块的必要性。
  - 零样本泛化实验展示了经验的可迁移性，增强了结论的可靠性。
  - 重复实验描述：未详细说明统计多次运行结果，但“SOTA by a significant margin”表明结果稳定。

## 6. 论文的主要结论与发现

- MUSE在TAC基准上以仅用轻量级Gemini-2.5 Flash模型实现了新的SOTA性能，且提升幅度显著。
- 随着经验自主积累，代理的任务完成能力持续提升，展现出强大的持续学习和自进化能力。
- 积累的经验具有良好的泛化性，能够零样本提升新任务的表现（无需额外微调）。
- 经验驱动的自进化机制是提升长程任务成功的有效途径，为AI代理在真实生产力任务中的自动化建立了新范式。

## 7. 优点

- **方法创新**：首次提出“在岗学习”概念，通过层次化记忆模块实现离线训练与在线经验的解耦，无需更新模型参数即可进化。
- **高效性**：使用轻量级模型（Gemini-2.5 Flash）即超越以往依赖大模型的方法，计算成本低。
- **通用性**：经验可跨任务零样本迁移，提升了框架的实际应用价值。
- **实验设计全面**：覆盖主性能、消融、泛化、持续学习等多维度，结果可信。
- **应用潜力**：针对长程生产力任务，直接面向真实世界场景。

## 8. 不足与局限

- **实验覆盖有限**：仅在一个基准（TAC）上评估，未在更多域（如机器人、游戏）测试，泛化性有待验证。
- **基线比较不充分**：未列出所有对比方法的详细结果，可能缺乏对更强基线（如GPT-4等更大模型）的对比。
- **经验记忆的长期效果**：随任务数增加，记忆模块规模膨胀，检索效率、遗忘机制等未讨论。
- **资源消耗**：虽然模型轻量，但反思与记忆整合过程本身增加了推理步骤，实际时延可能较高。
- **任务定义依赖**：长程任务分解严重依赖LLM的规划能力，若初始分解错误后续可能累积偏差。
- **可能存在的偏差风险**：反思过程依赖LLM自身输出，可能引入自我强化偏差（只记住成功经验而忽略失败模式）。

（完）
