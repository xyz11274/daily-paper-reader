---
title: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
title_zh: 达尔文哥德尔机：自我改进代理的开放式进化
authors: "Jenny Zhang, Shengran Hu, Cong Lu, Robert Tjarko Lange, Jeff Clune"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=pUpzQZTvGY"
tags: ["query:ase"]
score: 10.0
evidence: 开放式进化自我改进代理
tldr: 本文针对当前AI系统受限于固定架构、无法自主持续改进的问题，提出达尔文哥德尔机框架。该框架结合元学习和递归自我修改，实现代理的开放式进化。理论上能够超越一阶元学习限制，使代理持续自我改进并解决更复杂问题。为自动化AI进步提供了前瞻性框架，同时强调安全性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 大多数AI系统受限于固定架构，无法自主持续改进，需要自动化科学发现过程。
method: 提出达尔文哥德尔机框架，结合元学习和递归自我修改，实现代理的开放式进化。
result: 理论上能够超越一阶元学习限制，实现持续的自我改进。
conclusion: 为自动化AI进步提供了前瞻性框架，需注意安全性。
---

## Abstract
Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. There is growing hope that the current manual process of advancing AI could itself be automated. If done safely, such automation would accelerate AI development and allow us to reap its benefits much sooner. This prospect raises the question of how AI systems can endlessly improve themselves while getting better at solving relevant problems. Meta-learning can automate the discovery of novel algorithms, but is limited by first-order improvements and the human design of a suitable search space. The Gödel machine proposed a theoretical alternative: a self-improving AI that repeatedly modifies itself in a provably beneficial manner. Unfortunately, proving that most changes are net beneficial is impossible in practice. We introduce the Darwin Gödel Machine (DGM), a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. Inspired by Darwinian evolution and open-endedness research, the DGM grows an archive of generated coding agents. It samples agents from this archive, which self-modify to create new, interesting versions of themselves. This open-ended exploration forms a growing tree of diverse, high-quality agents and allows the parallel exploration of many different paths through the search space. Empirically, the DGM automatically improves its coding capabilities (e.g., better code editing tools, long-context window management, peer-review mechanisms), increasing performance on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. Furthermore, the DGM significantly outperforms baselines without self-improvement or open-ended exploration. All experiments were done with safety precautions (e.g., sandboxing, human oversight). Overall, the DGM represents a significant step toward self-improving AI, capable of gathering its own stepping stones along a path that unfolds into endless innovation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前多数AI系统受限于人工设计的固定架构，无法自主持续改进。科学发现本身是累积、开放式的过程，而AI发展仍依赖大量人工手动迭代。论文旨在探索如何让AI系统实现**开放式自我改进**，即在不依赖人类干预的情况下，不断优化自身能力并解决更复杂的问题。
- **背景**：元学习能自动化发现新算法，但受限于一阶改进和人工设计搜索空间；哥德尔机理论上可自我修改，但实际中无法证明每次修改都有益。因此需要一种既实用又可扩展的自我改进框架。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：**达尔文哥德尔机（DGM）** 结合达尔文进化理论与开放式探索，让代理通过递归自我修改自己的代码（包括改进代码修改能力），并通过编程基准实证验证每个修改的价值。
- **关键技术细节**：
  - **代理库（Archive）**：持续收集和保存生成的编码代理，形成多样化的代理树。
  - **采样与自我修改**：从库中采样代理，代理对自身代码进行修改（如改进代码编辑工具、长上下文窗口管理、同行评审机制），产生新的、更有趣的版本。
  - **开放式探索**：并行探索搜索空间中的多条路径，形成不断生长的代理树。
  - **验证机制**：每个修改通过编码基准（如SWE-bench、Polyglot）进行实证测试，确保只有有益的修改被保留。
  - **与哥德尔机的区别**：不再要求严格的形式化证明，而是基于实证验证和进化选择。

## 3. 实验设计

- **数据集 / 场景**：
  - **SWE-bench**：评估代码编辑与软件工程能力的基准。
  - **Polyglot**：多语言编程能力基准。
- **对比方法**：
  - 无自我改进的基线（固定架构）。
  - 无开放式探索的基线（仅单次自我修改）。
- **评价指标**：在SWE-bench和Polyglot上的性能（准确率）。
- **结果**：DGM在SWE-bench上从20.0%提升至50.0%，在Polyglot上从14.2%提升至30.7%，显著优于基线。

## 4. 资源与算力

- **未明确说明**：论文摘要及提供的元数据中未提及GPU型号、数量、训练时长等具体算力信息。仅在安全措施中提到使用了沙箱和人工监督，但未给出计算资源细节。需要指出这一点。

## 5. 实验数量与充分性

- **实验组数**：主要报告了两个标准基准上的性能提升，并对比了两种基线（无自我改进、无开放式探索）。未明确列出消融实验的详细数量，但核心对比能够体现方法有效性。
- **充分性评估**：
  - **正面**：在两个不同基准上验证，涵盖代码编辑和多语言任务；对比了关键消融（自我改进和开放式探索的单独影响）；结果提升显著（25-30个百分点）。
  - **不足**：缺乏更大规模的消融实验（如不同库大小、修改次数的影响）；仅涉及编码任务，未拓展到其他领域（如强化学习、机器人控制）；可能无法完全排除数据集偏差或过度拟合。
  - **客观性**：使用了公开基准，对比基线合理，结果可信。但未提及多次运行统计显著性。

## 6. 论文的主要结论与发现

- DGM成功实现了代理的开放式自我改进，能够自动收集“垫脚石”并沿创新路径持续进步。
- 自我修改能力（代码编辑工具、长上下文管理、同行评审机制）的改进可转化为性能显著提升。
- 开放式探索（并行多地搜索）优于单一路径的自我改进。
- 该方法在安全措施（沙箱、人工监督）下运行，验证了可行性。
- 总体来说是迈向自主持续自我改进AI的重要一步。

## 7. 优点：方法或实验设计上的亮点

- **创新性**：将达尔文进化、开放式生成与哥德尔机自我修改思想融合，提出实用化框架。
- **实用性**：通过实证验证代替形式化证明，解决了哥德尔机不可行的问题。
- **可扩展性**：代理可以递归修改自己的代码（包括修改自身修改代码的能力），形成指数级创新潜力。
- **实验设计合理**：在标准编程基准上对比关键消融，结果清晰有力。
- **安全性意识**：明确提及沙箱和人工监督等防护措施。

## 8. 不足与局限

- **实验覆盖有限**：仅在两个编码基准上测试，未评估其他领域（如数学、科学发现、游戏）的自我改进泛化性。
- **资源消耗不透明**：未报告计算成本，难以评估可复现性和经济可行性。
- **潜在偏差风险**：自我修改可能引入未知漏洞或安全风险，尽管有沙箱，但长期演化中可能产生不可预测行为。
- **理论基础薄弱**：缺乏对收敛性、最优性的严格分析；实证成功可能依赖于特定基准。
- **可复现性**：未提供代码或超参数细节，仅依赖摘要无法确认具体实现。
- **未讨论失败模式**：未分析自我修改失败的案例或退化路径。

（完）
