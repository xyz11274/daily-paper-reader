---
title: "SemVac: A Semantic Vaccinology Paradigm Powered by LLMs for Antigen Discovery"
title_zh: SemVac：一种由大语言模型驱动的语义疫苗学范式，用于抗原发现
authors: "Zhao, Y., Shu, Y., Shu, L., Lv, P., Chi, X., Li, D., Zhang, J., Huang, Z., Ren, H., Xu, J., Zai, X., Chen, W."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.13.737696v1.full.pdf"
tags: ["query:llm-trends"]
score: 9.0
evidence: 使用链式思维推理进行抗原预测
tldr: 传统反向疫苗学依赖序列信息，忽略了海量生物医学文献中的语义知识。本文提出SemVac范式，利用大语言模型从科学文本中推理预测保护性抗原，在14个模型基准测试中文本推理方法精度媲美专门深度学习模型，但对猴痘病毒全蛋白组应用时显式推理模式（如思维链）会导致过推理陷阱。SemVac成功复现已知抗原并发现新型候选B20R，建立了文献驱动语义推理作为疫苗学补充范式，对AI科学发现具有广阔前景。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-737696-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1336, \"height\": 1352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-13-737696-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1328, \"height\": 1485, \"label\": \"Figure\"}]"
motivation: 传统反向疫苗学仅用序列信息，忽视文献中蕴含的丰富语义知识，限制了抗原发现。
method: 提出SemVac范式，利用大语言模型对科学文本进行语义推理预测保护性抗原。
result: 文本推理方法精度匹配或超出深度学习模型，但思维链降低精度；在猴痘病毒中识别已知和新型候选抗原B20R。
conclusion: 语义推理作为传统疫苗学的强大补充，为AI辅助科学发现开辟了新路径。
---

## 摘要
逆向疫苗学实现了基于序列的抗原发现，但它忽略了生物医学文献中蕴含的丰富语义知识。本文建立了语义疫苗学（SemVac）这一范式，利用大语言模型（LLMs）直接从科学文本中预测保护性抗原。在精心整理的抗原数据集上对14个最先进的LLM进行基准测试表明，基于文本推理的方法在精度上匹配或超越专门的深度学习模型，同时在功能模糊的蛋白质上展现出更优的鲁棒性。有趣的是，显式推理模式（例如思维链）提高了召回率，但持续降低了精度，揭示了生物发现任务中的过度推理陷阱。将SemVac应用于Mpox病毒的完整蛋白质组，它重现了已知的保护性抗原，并识别出先前未被发现的候选抗原如B20R——我们的语义分析将其与免疫逃逸和结构暴露联系起来。这项工作确立了文献驱动的语义推理作为传统疫苗学强大补充的地位，对人工智能辅助的科学发现具有广泛意义。

## Abstract
Reverse vaccinology has enabled sequence-based antigen discovery, but it over-looks the rich semantic knowledge embedded in the biomedical literature. Here we establish Semantic Vaccinology (SemVac), a paradigm that leverages large language models (LLMs) to predict protective antigens directly from scientific text. Benchmarking 14 state-of-the-art LLMs on a curated antigen dataset shows that text-reasoning-based approaches match or exceed specialized deep learning models in precision, while offering superior robustness on functionally ambiguous proteins. Intriguingly, explicit reasoning modes (e.g., chain-of-thought) increase recall but consistently reduce precision, revealing an over-reasoning pitfall in biological discovery tasks. Applied to the complete proteome of Mpox virus, SemVac recapitulates known protective antigens and identifies previously unrecognized candidates such as B20R, which our semantic analysis links to immune evasion and structural exposure. This work establishes literature-driven semantic reasoning as a powerful complement to conventional vaccinology, with broad implications for AI-aided scientific discovery.

---

## 论文详细总结（自动生成）

### 论文详细中文总结

#### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：传统反向疫苗学仅依赖蛋白质序列和结构特征进行抗原筛选，忽略了生物医学文献中积累的丰富功能与免疫学知识（如致病机制、宿主相互作用、实验证据等），导致大量潜在保护性抗原被遗漏。
- **研究动机**：大型语言模型（LLM）经过海量科学语料训练，天然编码了语义知识并具备推理能力。能否直接利用LLM从文献描述的文献中通过语义推理预测保护性抗原，从而弥补传统方法的“语义鸿沟”？
- **整体含义**：本文提出**语义疫苗学（SemVac）**，将LLM应用于抗原发现，证明文本推理可以媲美甚至超越专用深度学习模型，并发现了一种新的“过度推理”陷阱，为AI辅助科学发现提供新范式。

#### 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：将蛋白质相关的科学文献文本（通过PaperBLAST检索得到）输入LLM，利用其编码的领域知识和推理能力，直接输出0~1之间的抗原性概率分数。
- **关键技术细节**：
  - **文献检索**：对每个目标蛋白质，使用BLAST同源搜索从PaperBLAST数据库中召回相关出版物（平均每蛋白268篇），提取文本片段构建结构化语义证据。
  - **提示设计**：系统指令设定模型为“专业计算免疫学家和疫苗学家”，并给出JSON格式输入（包括蛋白标识符、同源性统计、出版物信息和文献片段）。
  - **推理输出**：模型仅返回一个浮点数（0~1），表示该蛋白是保护性抗原的概率，禁止输出解释或其他文本。
  - **推理模式对比**：部分模型开启显式链式思维（chain-of-thought）模式，以对比标准模式。

#### 3. 实验设计：数据集、基准、对比方法
- **数据集**：
  - **主要基准**：246个细菌抗原（131个保护性，115个非保护性），来自已发表的RV研究（Vaxign-ML）。阳性为动物模型验证的保护性蛋白，阴性为无实验支持的细菌蛋白。
  - **扩展验证集**：1200个抗原（600阳性，600阴性），涵盖病毒、细菌和真核生物，来自Protegen、IEDB等来源，测试跨病原体泛化性。
  - **真实场景**：Mpox病毒（猴痘病毒Zaire-96-I-16株）完整蛋白组187个蛋白质。
- **基准和方法**：
  - **LLM基线**：14个前沿LLM（闭源：GPT-5.2 Pro/5.2、Claude 4.5 Opus、Gemini 3 Pro/Flash、Grok-4/4.1 Fast、Qwen 3 Max；开源/开放权重：Kimi-K2-0905、DeepSeek-V3.2、MiniMax M2.1、Mistral Large 3、Qwen 3.5 Plus、GLM-5）。
  - **非LLM基线**：PLGDL（蛋白质语言+几何深度学习模型，靶抗原预测SOTA）。
  - **消融实验**：屏蔽输入中包含“vaccine”、“protective”、“antigen”等关键词的论文，验证预测是否靠关键词匹配。
  - **推理模式实验**：在Claude 4.5 Opus、Kimi K2等模型上对比标准vs链式推理模式。
- **评估指标**：主要指标为**精度（Precision）**（因假阳性代价高），同时报告召回率、F1、准确率、ROC-AUC、PR-AUC。

#### 4. 资源与算力
- 论文**未明确说明**LLM的训练算力需求（如GPU型号、数量、训练时长），因为所有LLM均为已训练好的模型，仅通过OpenRouter API调用进行推理。
- 仅提供了**推理成本**分析：闭源模型（如GPT-5.2 Pro）成本最高，开源模型（如Kimi K2）成本低且精度靠前。但未报告具体硬件配置或运行时间。

#### 5. 实验数量与充分性
- **主要实验组数**：
  - 14个LLM在246抗原基准上的性能比较（含成本-精度图）。
  - 2个代表性模型（GPT-5.2 Pro、Kimi K2）在1200抗原扩展集上的验证。
  - 关键词屏蔽消融实验（Kimi K2）。
  - 推理模式对比（标准 vs 链式思维）在4个模型上（Claude 4.5 Opus、Kimi K2等）。
  - Mpox全蛋白组应用（187蛋白），给出Top15候选并与PLGDL对比，包括推理轨迹分析。
- **充分性与公平性**：
  - 实验设计较为系统：覆盖多个病原类型、多种模型家族、有无关键词的对照、推理模式对比，并针对实际病原体进行案例研究。
  - 所有LLM使用相同的提示格式、温度(0)和输出约束，确保了横向公平。
  - 但**主要基准大小有限（246样本）**，虽使用扩展集验证，但两种数据集来源层级存在一定偏差风险（阴性样本的定义依赖文献证据不完备性）。
  - 未做多次运行或置信区间报告（温度固定0，但模型推理本身仍有随机性？），不过趋势一致性强。

#### 6. 论文的主要结论与发现
- **LLM语义推理可媲美专用模型**：Kimi K2 0905（开源）精度0.8382，超越PLGDL（0.7985）；GPT-5.2 Pro精度最高（0.8974）。
- **预测非靠关键词匹配**：屏蔽关键词后性能几乎不变（Kimi K2精度0.8382 vs 0.8358），证明模型学习内在生物特征。
- **显式推理模式（链式思维）反而有害**：在所有测试模型中，链式思维提升召回率（最多8.4%）但持续降低精度（最多7.6%），导致**过度推理陷阱**（产生生物学上合理但错误的解释，如幻觉机制、过度同源物解释）。
- **开源模型成本效率最优**：Kimi K2在成本-精度权衡上远优于闭源模型，适合资源受限场景。
- **Mpox应用成功发现已知和新型候选**：SemVac复现了已知保护性抗原（M1R、A35R等），并识别出B20R（TNF受体同源物，与免疫逃逸相关）、C19L（包膜蛋白）等八个传统方法未检测到的靶点，验证了语义推理的互补价值。

#### 7. 优点
- **创新性**：首次提出利用通用LLM进行文献驱动的抗原发现，突破传统序列/结构方法的局限，开启“语义疫苗学”新范式。
- **实验全面性**：覆盖多种LLM、两个独立抗原数据集、真实病原体应用，并设计了关键词屏蔽和推理模式消融。
- **发现洞察**：揭示“过度推理”现象，为LLM在生物发现中的使用提供重要警示；同时证实开源模型的高效性，便于复现和推广。
- **实用性**：直接给出概率排名，且能整合多维度语义信息（功能、保守性、免疫调控、实验证据），更贴近专家决策过程。

#### 8. 不足与局限
- **数据集偏差与完整性**：抗原数据集可能存在注释不完全或阴性样本定义主观的风险（“真阴性”缺乏实验证据并不保证绝对非保护性）；基准规模有限（246），可能不足以覆盖抗原多样性。
- **验证闭环缺失**：SemVac目前仅做静态推理和回顾性验证，缺乏前瞻性湿实验验证来确认新候选的真实有效性。
- **文献检索依赖**：PaperBLAST检索质量影响输入；同源文献可能引入噪音或遗漏关键证据。
- **解释性不足**：虽然提供了推理轨迹示例，但整体输出仅为概率分数，缺乏系统性的不确定性量化或置信度估计。
- **计算代价描述不完整**：仅报告推理成本（美元/API调用），未评估模型部署的实际硬件资源、内存或延迟，且缺少端到端流程（检索+推理）的总时间开销。

（完）
