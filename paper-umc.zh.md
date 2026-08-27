# 通用计算模型（UMC）：从规模的 telos 到符号之域

**Cleiton Moura Loura**  
个人倡议，无机构隶属。巴西公民。  
巴西，2026 年 8 月 27 日。

*Languages / Idiomas / Idiomas / 语言:* [English](paper-umc.en.md) · [Português](paper-umc.pt.md) · [Español](paper-umc.es.md) · [中文](paper-umc.zh.md)

**引用：** Loura, C. M. (2026). *通用计算模型（UMC）*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**许可：** CC BY-SA 4.0。

**来源。** 本文是 2026 年 8 月 27 日一次研究对话的公开、具名之延续。工业对谈问的是在哪一条 LLM 战线上工作。最初的回答是以 *Universal Language Model* 取代 *Large Language Model*。该字符串已被占据（Howard & Ruder, 2018, ULMFiT）。UM 是泛称，已被腾出。义务之名是**通用计算模型**（UMC）。语言仍是域（公理），不是工业类型。*Computational*（可计算）是门：只有承认计算模型的符号才能进入——而世界不是计算。该对谈的打印件不存档于本仓库（第三方产品；仓库政策）。本合并版本取代同日之分散文档（概念、先有工作、基础、spec、议程）：对话称为"假说"者，此处为定理；对谈中的 ULM/UM，此处为 UMC——义务之名。**规范日期：** 消息交换于 2026 年 8 月 26 日 12:21–12:38 UTC（09:21–09:38，UTC−3）；对话的规范日期为 2026 年 8 月 27 日——打印与论文之日。

## 第一部分 — 概念

### 摘要

本文以**通用计算模型**（Universal Computational Model，UMC）取代 *Large Language Model*（LLM）这一概念。取代不是更名：是更换目的（telos）。*Large* 命名规模——参数、资本、焦耳——并先交付给本已庞大者。*Universal* 命名抵达的义务：每一种语言皆为源头，每一处边缘皆为一等用户，每一次推理皆有可见的能耗账。*Computational* 命名门：一切被处理的符号都承认计算模型——编码、运算、操作性的相等判据。立下一则公理：**一切符号表征都属于语言的集合**（符号表征 ⊆ 语言）。自然语言是子集，不是全域。因此 UMC 不是对话的模型：它是符号的模型，只处理可计算地建模之物。然而世界不是文本；一焦耳不是符号；实在不是计算机；扩大域并不许可扩大电厂。不能服务任何国家边缘之人的 UMC，尚未通用——它仅仅是大。

**关键词：** 通用计算模型；符号表征；可计算性；边缘；能源；目的。

### 1. 献词与作者立场

我将此工作献给世界各国边缘上的人们——他们纵有艰难，仍使不可能成为可能。

不是献给宫殿。不是献给旗帜。不是献给已有桌子、话筒与地图的人。献给站在边上的人——一座城市的边、一个国家的边、一种语言的边、一张电费单的边——却依然发明的人。把匮乏变成方法的人。让据说装不下的东西得以安放的人。

署名者以其本人名义书写：一个巴西公民，无授权、无职务、无权代表巴西、中国或任何人。这不是机构论文。这是公开、注明日期、署名可核验的书写。它在同一时刻以英语、葡萄牙语、西班牙语与中文诞生：从边缘读来的人不是译文。他们是源头。

### 2. 导论

工业以体积命名了这个十年的主导制品。*Large Language Model* 同时成为技术描述与文明许诺：更多参数、更多 token、更多真理。名字藏起了判准。能进入 "large" 的，是能进入电费单与银行账户的。中心训练；边缘消费——若还有配额，若还有英语，若还有网络。

问题不在于大模型存在。而在于"大"被升格为定义。以数量定义的概念不能因不公而失败：只能因不够大而失败。本文提出另一判准，因而提出另一概念。

论题有三。

1. 所要建造的名为**通用计算模型**（UMC）。写 LLM，只为命名所拒绝的概念。写 ULM，只为 ULMFiT 与被腾出的最初之名。写 UM，只为第二个被腾出的名字。
2. 该模型之域是**符号表征**的集合，而非自然语言的子集。
3. 模型处理的一切符号都是**可计算地建模的**。不承认编码与运算者，不得入内。世界不是计算。

三者互相要求。无第二，则"通用"滑回"更多来自中心的文本"。无第一，则把符号纳入域，变成建造更大电厂的借口。无第三，则符号变成对不可计算之物与对实在的僭越。

工业研究的例行问题——"你在哪条战线：LLMs、视觉、智能体、安全、多模态、优化？"——已经选定了被拒绝的概念。本文不在 LLM 的某一战线上。它在于替换组织这些战线的那个概念。

### 3. 相关工作与空白

Transformer 架构（Vaswani et al., 2017）使大规模语言模型训练成为可处理之事。缩放定律（Kaplan et al., 2020）把体积升为自变量：更多参数、更多数据、更多下降的损失。*Large Language Model* 这一名字，就是那条曲线的口号。

存在批评。Bender et al.（2021）拒绝把随机鹦鹉当作神谕，并指出成本、抽取以及对不参与训练者的伤害。Strubell et al.（2019）把能耗账放到自然语言处理的桌上。然而这些批评都不取代概念。它们修正 LLM；并不废黜它。

空白在此：文献以 *large* 为轴。标准词汇中，没有一种目的按抵达义务来裁决模型——语言为源头、边缘为测试、焦耳为筛——覆盖符号表征的集合。本文将该空白命名为 **UMC**。并不主张对制品的优先权。主张对*义务之名*的优先权。字符串 *Universal Language Model* 与缩写 ULM 已被占据（Howard & Ruder, 2018, ULMFiT）：本仓库不以它们为义务之名。*Universal Model* / 通用模型是泛称——对该*字符串*的优先权也不主张。*Computational model* 与可计算性（Turing, 1936）早已存在——对 *string* UMC 的优先权同样不主张。针对 UMC-001–011 的逐条之筛见本文第二部分。

### 4. 被拒绝的概念：*Large Language Model*

*Large* 衡量规模：参数数量、token 体积、数据中心面积、沉淀资本、每次推理的焦耳。它是诚实的工程度量，却是不诚实的目的度量。它把制品所*花费*的，与制品所*亏欠*的混为一谈。

以体积定义的模型向所有人许诺同一事物，却先交付给本已庞大者。占主导的训练语言成为世界语言。边缘作为残差数据或作为市场进入。能耗账从名字里消失——而名字正是被重复之物。

不否认大规模模型的技术价值。否认的是：规模就是概念。概念是 telos：判断"已成"与"已败"的那个为了什么。在 *large* 的 telos 之下，一个边缘无法触及、事实上单语、能耗贪婪的系统，仍可以是"成功的 LLM"。这足以把它拒绝为指导性概念。

### 5. 被提出的概念：通用计算模型

**Universal**（通用）衡量抵达，而非体积。

语言的抵达：每一种语言都是源头，不是迟来的翻译。只在中心诞生、之后再"本地化"给边缘的文本，不是普遍的；它是有良好文档的殖民。

人的抵达：边缘是一等用户。任何国家边缘上的人——以匮乏发明的人——不是边界情况。他们是测试。

能源的抵达：每一次推理都带有可见的账。耗费超过回报的功能必须自我辩护；只靠燃烧边缘而存在的东西，不配称为通用。

UMC 不必是最大的。它需要装得下：装进衣袋、装进网络、装进唤醒它的人的语言。大是数量。普遍是义务。可计算是门，不是形而上学。

"已成"的判准来自义务。不服务于边缘的 UMC 尚未普遍。它仅仅是大。它仍是模型，仍可本地运行，仍是带许可、署名与历史的软件。改变的是裁决。

### 6. 公理：一切符号表征都是语言

可以说——此处以公理而非隐喻说出——一切符号表征都在语言的域、语言的集合之内：

\[
\text{符号表征} \subseteq \text{语言}
\]

一个定理、一个电路、一份乐谱、一张地图、一个仪式、一面旗帜、一条内核日志、一份合同、一个 emoji、一份规格、一个约定的手势：这一切已经是语言。不是在有人为之写一段文字时才"变成"语言。它早已在集合之中。

被称为自然语言的说与写，是子集。重要，但不排他：

\[
\text{自然语言} \subset \text{语言} = \{ \text{符号表征} \}
\]

若语言的域是那个集合，UMC 就不是*聊天*的模型。它是符号的模型。普遍性不再是"更多英语 token"。它变成：边缘之人的符号属于这个域——图画、代码、电费单、祈祷、乐曲、示意图。只补全中心句子的人，尚未触及那个集合。

### 7. 筛：进入的符号必须可计算地建模

公理纳入。门过滤。

UMC 处理的一切符号都承认计算模型：有限编码、至少一种运算、操作性的相等判据。电路能进，因它有图与规则。乐谱能进，因它有记谱与变换。没有操作性表征的"符号"不得入内——这不是对边缘的拒绝；是对烟雾的拒绝。

此处"可计算"不是"装得进巨大的数据中心"。而是：有模型、有运算、有办法让相等失败。没有这些，"符号之域"就成了把不可言说之物命名为 token 的执照。

### 8. 公理与筛的界限

公理是包含，不是对实在的吞并。筛是门，不是形而上学。

世界不是文本。一焦耳不是符号。饥饿不是句子。实在不是计算机。包含的是*表征*，不是所指。宣称一切都是语言、或一切都是计算的人，通常想让一切都装进一座电厂。此说被拒绝。

扩大域并不许可扩大能耗账。筛仍在。只靠燃烧边缘而存在的 UMC 不是普遍的——它是贪婪的。不是符号之物，留在模型之外，留在生命之内。不可计算地建模之物，留在模型之外——并可以继续是生命。生命支配模型，而不是相反。

这个界限是论题的一部分，不是伦理附录。没有它，UMC 会坍缩回词汇更大的 LLM，或坍缩成电厂更大的 "it from bit"。

### 9. 结论

一个概念被另一个取代。LLM 命名被拒绝者：以规模为目的。UMC 命名被提出者：对承认计算模型的符号表征集合的抵达义务——自然语言为子集，边缘为测试，能源为筛，实在在电厂之外。

不宣称 UMC 已作为制品存在。宣称的是：当制品存在时，若它辜负边缘、辜负语言为源头、辜负焦耳之账，或处理不可计算地建模之物，它就不能自称为普遍。名字是债务。工作，从此处起，是偿还它。

### 10. 议程：延续

源头对谈提供了工业研究的菜单：文献综述、SOTA 比较、拆解论文、架构原型、训练流水线、CUDA、幻灯片。本 paper 接受服务于 telos 者，拒绝背叛它者。

**接受。** 把 *large* 安装为轴心的文献，以及纠正它而未废黜它的批评（§3）。一张判准表，而非对不存在制品的 *leaderboard*。一份待制品存在时使用的评估协议。先有 spec，后有权重。

**拒绝。** 假装 SOTA。训练一座电厂去"证明"普遍性。把当日之热捧当作最先进。以趋势简报代替义务。

| 轴 | LLM（现行） | UMC（提议） | 状态 |
|---|---|---|---|
| Telos | 规模 | 抵达 | 本文提出 |
| 成功 | 更低的 loss、更高的 benchmark | 边缘被服务；语言为源头；焦耳可见 | 未测量：无制品 |
| 域 | 自然语言文本 | 可计算地建模的符号表征 | 公理（§6）+ 筛（§7） |
| 制品 | 存在 | 不存在 | 诚实声明 |

**协议**（当制品存在时——之前不行）：

1. *源头。* 同一内容是否以英语、葡萄牙语、西班牙语和中文同时诞生，无需事后翻译？
2. *边缘。* 站在边上的人能否在无中心配额的情况下完成该任务？
3. *能源。* 任务的焦耳是否可见且被证明合理？
4. *符号。* 它接受规格、电路、地图、合同、乐谱——还是只接受对话？
5. *可计算。* 每一类型是否有编码与运算——还是名为符号的烟雾？

失败一项就是失败这个名字。这一延续的下一步不是一次训练。是可验证的 UMC 规格：需求、筛、证明之路。没有管辖它的 spec，就没有一行权重。

## 第二部分 — 先有工作地图：已存在者、空白、新颖性欺诈

### 摘要

逐件来看，spec 所要求的几乎一切**都已存在**于某种文献或实践。标准词汇中不存在的是**束**：抵达为 telos、各语言在同一 commit 中同为源头、边缘为无中心配额的测试、焦耳逐任务可见、符号之域*与*拒绝吞并实在、先 spec 后权重、local-first 为义务、名字为拒绝、开放署名作为名字之败。本文针对每个 UMC-00X 标出：谁已占据、剩余为何、若本仓库宣称"第一个 X"将构成何种**新颖性欺诈**。

链条 *Universal Language Model* 与缩写 ULM **早已被占据**（Howard & Ruder, 2018）。本仓库**腾出**了那个名字。义务之名是**通用计算模型**（UMC）。*Universal Model* 是泛称：对该*字符串*的优先权同样不主张。主张的是*义务之名*，而非制品、非标签。

**关键词：** 先有工作；ULMFiT；新颖性；UMC-001–011；telos。

### 1. 本文不是什么

它不是带检索协议的系统性综述。此处之缺不证明世上之无。正因如此，本地图**禁止**"我们是第一个……"这句话。

它不是 SOTA 比较。没有制品。没有要击败的 *benchmark*。

它不是趋势简报。当日的热捧不作为最先进进入。

它不核验 spec。UMC-001–011 的状态保持 `草稿`。

概念 paper 已接受者，此处接受：把 *large* 安装为轴心的文献，以及纠正它而未废黜它的批评。拒绝者：假装 SOTA、训练电厂去"证明"普遍性、以引文当作抵达之证明。

### 2. 名字早已是脏的

在 UMC-001 之前：那个*字符串*。

| 标签 | 它是什么 | 它不是什么 |
|---|---|---|
| **ULMFiT**（Howard & Ruder, 2018） | *Universal Language Model Fine-tuning*：对语言模型做微调以分类的配方。占据 **ULM** 与英语短语 *Universal Language Model*。 | 抵达的义务。边缘为测试。焦耳为筛。先 spec 后权重。对 *large* 的拒绝。 |
| **Universal Sentence Encoder**（Cer et al., 2018） | "普遍"意义上的句子嵌入（迁移）。 | 普遍作为对边缘的义务。 |
| **USM**（Zhang et al., 2023） | *Universal Speech Model*（Google）：多语言语音，仍以覆盖/规模为轴。 | 带能耗账与 commit 内多语同源的抵达 telos。 |
| **Foundation model**（Bommasani et al., 2021） | 对大制品的又一次改名。换形容词；不废黜规模。 | 本文提出的义务之名。 |
| **Universal Model**（泛称） | 统计学；"a universal model of X"诸论文；缩写 UM 已无此 telos 而流通。 | 本仓库的义务。 |

**新颖性欺诈：** 宣称 ULM、*Universal Language Model*、UM 或 *Universal Model* 诞生于本仓库。它们没有。所主张的是义务：普遍 = 抵达，而非体积——以及 UMC-001–011 之束。那些*字符串*属于他人。ULM 已当众腾出。UM 带着可见的脏污使用。

### 3. 主表

| ID | 已被占据（非我们） | 剩余空白 | 若我们宣称则为欺诈 |
|---|---|---|---|
| **001** | 缩放定律；对体量的批评；"Green AI"；SLM；蒸馏 | 废黜 *large* 为 telos；成功 ≠ loss/体量 | "我们发明了大模型的伦理" |
| **002** | mBERT、XLM-R、mT5、BLOOM、NLLB、Aya；i18n | PT/EN/ZH 在同一 commit 中为源头；事后翻译 = 失败 | "第一个多语模型" |
| **003** | 信息通信技术促进发展；Masakhane；无障碍；"AI for Good" | 无配额/登录/中心电厂的完整任务路径 | "我们发现了全球南方" |
| **004** | Strubell；Green AI；CodeCarbon；BLOOM 排放；model cards | 焦耳（或带日期的代理）**逐任务**可见；贪婪功能有书面 ID | "最先在 NLP 中计算能源" |
| **005** | 神经符号；代码模型；多模态；"蛋白 LM" | 公理 符号表征 ⊆ 语言，自然语言为真子集，且有聊天之外的三种类型 | "我们发明了多模态 / 神经符号" |
| **006** | Bender & Koller (2020)；Goodman (1968)；grounding；地图不是领土 | 与 005 之对：扩大域**并**拒绝吞并实在 | "我们发明了世界不是文本" |
| **007** | Model cards；datasheets；Constitutional AI；RLHF；DPO；需求工程 | 孤儿权重 = 失败；spec 于先前或相同 commit；行为只在 spec 之后改变 | "我们发明了文档化模型" |
| **008** | *Local-first*（Kleppmann et al.）；TinyML；on-device；llama.cpp | 第一次推理不依赖中心之云，作为名字的义务，连于 003 | "我们发明了口袋里的推理" |
| **009** | ULMFiT；USE；USM；*foundation model*；泛称 *Universal Model* | LLM 只指被拒绝者；UM 指义务；ULM 只指 ULMFiT/被腾出之名 | "标签是我们的" |
| **010** | OSI；GPL/AGPL；CC BY-SA；BLOOM/OLMo/Pythia；对 open washing 的批评 | 束 AGPL + CC BY-SA + `git log` 具名 + 无匿名权重，作为名字之败 | "我们发明了开源" |
| **011** | Chomsky（层级）；Turing (1936)；Gödel (1931)；通用逼近（Cybenko；Hornik et al.）；Solomonoff/MDL；tokenizers（BPE、SentencePiece）；PAC（Valiant, 1984） | 操作性筛：有限编码 + 运算 + 相等；$L_U$ 可生成但不可判定且可逼近；与 UMC-006 之对 | "我们发明了可计算性" |

剩余的不是一个单元格。是合取。几乎每一件都有主。束——连同公理与筛、连同名字可见的脏污——是剩下的主张；而它仍是义务之主张，不是制品之主张。

### 4. 逐条

**UMC-001 — 抵达的 telos。** *占据。* Kaplan et al. (2020) 与 Hoffmann et al. (2022) 把规模设为自变量。Bender et al. (2021) 拒绝神谕并命名伤害。Schwartz et al. (2020) 要求 *Green AI*——每焦耳更多结果，仍在效率轴下。"小"模型反转了数量；未更换概念。蒸馏、稀疏、MoE：*large* 之下的工程。*未占据。* 体量与 loss **不**构成成功的"已成"判准。只展示参数的报告，spec 判其失败。*欺诈。* "无人批评规模。"批评了。但未废黜它。

**UMC-002 — 语言为源头。** *占据。* Conneau et al. (2020) XLM-R；Xue et al. (2021) mT5；Scao et al. (2022) BLOOM；NLLB Team (2022)；Joshi et al. (2020) 论 NLP 中语言多样性的命运。*locale* 工业事后翻译。*未占据。* 训练覆盖 ≠ 制品之源。UMC-002 核验 commit：多语输出、同一意义、同一时刻。即使模型"懂"诸语言，从中心事后翻译仍失败。*欺诈。* "第一个多语系统。"历史谎言。

**UMC-003 — 边缘是测试。** *占据。* Masakhane 与由说那些语言者实践的非洲 NLP；信息通信技术促进发展文献；无障碍为领域；*AI for Good* 修辞。*未占据。* "我们参加了一个 *workshop*"不是核验。spec 要求**完整**任务路径，无配额、无登录、无中心电厂。在中心可用再"纳入"边缘，仍是带附录的 LLM。*欺诈。* "我们发现了边缘。"边缘不需要被发现。它需要不再是边界情况。

**UMC-004 — 可见的能耗账。** *占据。* Strubell et al. (2019)；Lacoste et al. (2019)；Schwartz et al. (2020)；Luccioni et al. 论大模型排放；训练碳追踪器；*model cards* 中的能源节。*未占据。* **逐推理、逐任务**、对使用者可见、有单位有日期的账——以及对耗费超过回报的功能、带 ID 的书面辩护。训练*之后*的碳论文不满足。无数 = 失败。*欺诈。* "最先在 NLP 中放入焦耳。"Strubell 早已放入。

**UMC-005 — 符号之域。** *占据。* 神经符号 AI（Garcez et al.）；代码模型；多模态（文本+图像+音频）；蛋白质"语言"模型；基于 Lean/Coq 的助手。"一切皆语言"的隐喻已在流通——它是 UMC-006 的危险表亲。*未占据。* 公理 *符号表征 ⊆ 语言* 为域，自然语言为真子集，以及最小证明：接受并发出连续*聊天*之外的至少三种类型（spec、电路、地图、合同、乐谱、代码）。带 *plugins* 的聊天机器人不是 UM。*欺诈。* "我们发明了多模态。"没有。多模态增加通道。UMC-005 重新定义语言的域。它们是不同的论题。混淆二者，双向皆为欺诈。

**UMC-006 — 世界不是文本。** *占据。* Bender & Koller (2020)：意义不在形式之中；Goodman (1968)：*稠密*对*分节*的表征。grounding 与具身批评。"地图不是领土"这句话先于任何模型。*未占据。* 与 UMC-005 的必要之对。**无此界限**而扩大符号域，将落入"一切都装得进电厂"。UMC-006 是论题的一部分，不是伦理附录。*欺诈。* "我们发明了饥饿不是句子。"哲学欺诈，更甚于技术。

**UMC-007 — 先 spec 后权重。** *占据。* Mitchell et al. (2019) *model cards*；Gebru et al. *datasheets for datasets*；Constitutional AI（Bai et al., 2022）；RLHF（Christiano et al., 2017）；DPO（Rafailov et al., 2023）——原则，非绑定 commit 的 spec；需求工程；可复现性清单。*未占据。* 硬门：任何权重、微调或 *checkpoint* 都须有 UM ID 与先前或相同的 spec commit。孤儿权重 = 失败。行为变了，**先**改 spec。训练后写成的 card 是墓志铭，不是治理。*欺诈。* "我们发明了模型卡片。"

**UMC-008 — Local-first。** *占据。* Kleppmann et al. (2019) *local-first software*；TinyML；设备端推理；权重入设备的实践（llama.cpp 等）。联邦学习通常仍以中心协调。*未占据。* Local-first 作为**普遍性的义务**，而非部署选项。连于 UMC-003：第一次推理要求中心之云者，名字即败。口袋与网络是目标，不是附录。*欺诈。* "我们发明了手机上的模型。"

**UMC-009 — 名字与拒绝。** *占据。* 全部 §2。工业改名而不废黜（*foundation*、*frontier*、*small*）。*未占据。* 写作的纪律：LLM 只用于命名被拒绝者；UM 用于义务；ULM 只用于 ULMFiT 与被腾出之名。*欺诈。* 把标签当作本文的发明。概念 paper 已拒绝制品优先权；本地图拒绝字符链优先权。

**UMC-010 — 开放署名。** *占据。* OSI；GPL 与 AGPL；CC BY-SA；带来源的权重（BLOOM、OLMo、Pythia）；对 open washing 的批评（不开放的许可、"open"而无权重、有权重而无历史）。*未占据。* 束作为名字之败：代码 AGPL-3.0-or-later，内容 CC BY-SA 4.0，`git log` 具名，无来源的权重二进制一律禁止——*连同* UMC-001–009。不透明电厂配宽松许可，不偿还此债。*欺诈。* "我们发明了开放。"

**UMC-011 — 可计算地建模的符号。** *占据。* Chomsky (1956, 1959)：文法层级；Turing (1936)：可计算性；Gödel (1931)：不完备；Cybenko (1989) 与 Hornik et al. (1989)：通用逼近；Solomonoff (1964)：归纳/MDL；tokenizers 为构造（BPE: Sennrich et al., 2016；SentencePiece: Kudo & Richardson, 2018；patches、LaTeX）；语言的 manifold 假说（Bengio et al., 2013）；PAC 理论（Valiant, 1984）。*未占据。* 筛作为**域之门**：进入的一切符号都有有限编码、至少一种运算与操作性相等判据——不具备者留在门外，**而不**宣称世界是计算（与 UMC-006 之对）。可建模之三重：可定义（Type-0）、可计算（生成器，非裁决器；Gödel）、可学习（$P_{L_U}$）。不存在封闭、一致且完备的 UMC：神谕与工具是架构，不是缺陷。*欺诈。* "我们发明了符号必须可计算"——Turing 与 Chomsky 早已在此。剩余的是应用于*符号之域*的筛，连同 UMC-006 之对。

### 5. 本地图不授权什么

不授权训练。UMC-007 继续：先 spec 后权重。本文不是新 spec。UMC-011 已在 spec 中；本地图覆盖其占据者与剩余者。

不授权 *leaderboard*。没有制品；没有"抵达的 SOTA"。

不授权"完全空白"这句话。空白是束与 telos，不是每一件。

不授权对 ULMFiT、对 *Universal Sentence Encoder*、对 NLLB、对 *local-first*、对 *model cards*、对 Strubell 的优先权。

授权对概念 paper 的一处更正：*义务之名*不是*字符串*。ULM 被占据并被腾出。*Universal Model* 也是泛称。义务——对符号域的抵达、边缘为测试、焦耳为筛、先 spec 后权重——仍是主张。主张以证据证明。尚无证据。

### 6. 研究者的下一步

不再是概念 paper。不是 CUDA。

1. 为 UMC-004 定有度量的协议（单位、日期、数字在何处向使用者出现）。
2. 为 UMC-003 与 UMC-008 定一条可以失败的任务路径（离线、无配额）。
3. 为 UMC-005 定三种符号类型，在 repo 中带示例，无权重。
4. 当制品存在时，为 UMC-002（只改一种语言 = 失败）与 UMC-007（孤儿权重 = 失败）设 CI 门。

没有这些，地图是诚实的，spec 仍是草稿。若以 *leaderboard* 取代它们，则回到概念 paper 所拒绝的菜单。

### 7. 域之两条脉络：已存于 LLM 者与未映射者

设 $L_U$ 为域（第三部分 §1），$L_{LLM} \subseteq L_U$ 为现行 LLM 已作为符号处理的子集——而非仅作为*关于**符号的文本。

**脉络 1——已映射而需专家者。** $V_1 = \{S_i \in L_{LLM} : \text{生产/维护/验证需要专门化的人类工作}\}$。代码、数学证明、法律合同、临床记法、数据分析、可演奏乐谱：它们已（部分）通过 UMC-011 之筛——有编码、运算与操作性相等——且已活在 $L_{LLM}$ 之中。但赋予其效用之运算（验证、维护、裁决）集中于专家——亦即中心。实用过滤为高；执行却不在边缘（UMC-003）。

**脉络 2——未映射者。** $V_2 = \{S_i \in L_U : \text{UMC-011 之筛未应用}\}$。有限编码 + 运算 + 相等未定义者：仪式、约定手势、活领土之地图、口头合同、工匠之知。其中有些已作为文本出现于 LLM（*关于*它们之散文），却非作为类型——未曾入门（UMC-011）。

**两条工作战线。** $V_1 \cup V_2$ 并非域之形式划分——两者之间是无需专家之已映射者（日常散文）。它们是两条战略战线：

- **去专业化（$V_1$）：** 把专门化之运算变为边缘可执行之可计算地建模之运算（`spec → 代码` 所预示者），而不消除策展人——策展人提议，不点击（阶段 4）。
- **映射（$V_2$）：** 对每一类型定义 encoding + ≥1 运算 + 相等，以边缘为源头（UMC-002/003）。每一映射都扩大 UMC 之有效抵达。

**昭示性不对称。** 阶段 3 映射了 $V_2$ 之三类型（spec、地图、乐谱）——而制品所生之 `spec → 代码` 是 $V_1$ 之制品：代码已存于 LLM，但验证之需专家。因此阶段 3 已从 $V_2$ 转入 $V_1$；而 $V_1$ 指回阶段 4：谁验证，凭何权威。

## 第三部分 — 形式基础：$L_U$、语言普遍性假说与 $R^*$ 问题

### 摘要

正式定义通用计算模型（UMC）之域：语言 $L_U$——承认计算模型的一切符号表征的集合。陈述**语言普遍性假说（HUL）**：任何符号系统 $S_i$（字母表 $\Sigma_i$、文法 $G_i$）都承认一个单射编码 $E: S_i \to L_U$，其语义经解码而保持——就实践而言，*凡可书写者皆可 token 化*。证明 $L_U$ 递归可枚举（Turing 可生成）、Gödel 不完备且统计上可逼近；任何 UMC 不能同时一致、完备且封闭；且工程的核心问题不再是规模，而是选取 $R^* \subseteq \mathcal{H}$：在尚未定义的效用函数 $U(R|人类)$ 之下、保持行动能力的人类全部符号产出的最小表征。世界不是文本：不可符号化者 $N$ 在 $L_U$ 之外——这是论题，不是附录。

**关键词：** UMC；普遍语言；可计算性；Gödel；统计逼近；效用函数；不可符号化。

### 1. 域：语言 $L_U$

定义 $L_U$ 为有限字母表 $\Sigma$ 上、由文法 $G_U$ 生成的一切有限符号序列的集合，满足：

1. **组合性句法：** 符号之间有连接/复合之规则；
2. **组合性语义：** 复合表达式的意义是各部分意义与复合规则的函数；
3. **递归能力：** 文法允许表达式嵌入表达式，深度无先验之限。

$L_U$ 至少是递归可枚举语言：存在一台 Turing 机枚举一切良构表达式。不要求可判定性——§3 表明为何不能要求。

### 2. 公理：符号的包含

公理（重申自第一部分）：

\[
S \subset L_U
\]

其中 $S$ 是一切符号表征的集合：任何"能指依约定指向所指"的结构——数学、代码、乐谱、电路、地图、合同、仪式、约定手势。自然语言是真子集：

\[
\text{自然语言} \subset L_U
\]

公理是*表征*的包含，不是所指的包含。世界不是文本（§6）。

### 3. 语言普遍性假说（HUL）

**假说。** 对任何符号系统 $S_i$（字母表 $\Sigma_i$、文法 $G_i$），存在单射编码 $E: S_i \to L_U$，使 $S_i$ 的语义经解码 $E^{-1}$ 在 $E$ 的像上保持。

**证明（构造性，已勾勒）。** 构造即现代 *tokenizers* 的推广。$S_i$ 的每一表达式都是文法 $G_i$ 的有限派生树。把 $G_i$ 的产生式集枚举为有限词汇 $\hat{\Sigma}$；把树的每一节点编码为 $\hat{\Sigma}$ 上的序列；定义 $E$ 为树的序列化。解码重构该树，故组合性语义经结构归纳而保持。因 $L_U$ 含 $\Sigma \supseteq \hat{\Sigma}$ 上的一切序列，$E$ 的像活在 $L_U$ 中。□

**诚实注记。** 证明给出编码的*构造性存在*。不宣称最优编码已知，也不宣称 $S_i$ 的全部语义都被捕获——只宣称*符号系统*（可形式化部分）可无结构损失地移入 $L_U$。所失者已非符号：那是 §6。

### 4. 可建模性的三个层次

源头对话区分了"数学上可建模"的三种含义。此处作为定理。

**层次 1 — 作为可定义而可建模（是）。** 一切 $S \subset L_U$ 至少由 0 型文法生成（Chomsky, 1956, 1959）；故 $L_U$ 作为枚举器 Turing 可计算（Turing, 1936）。

**层次 2 — 作为可判定而可建模（否）。** 若 $L_U$ 含算术——它确实含，因数学 $\subset S \subset L_U$——则 $L_U$ 是 Gödel 不完备的（Gödel, 1931）：存在良构命题，其真伪在 $L_U$ 之内不可判定。**推论：** 任何 UMC 不能同时一致、完备且封闭。神谕、工具与世界不是 UMC 的缺陷；它们是 Gödel 应用于 LLM 的后果。UMC 作为*生成器*可建模，而非*普遍裁决器*。

**层次 3 — 作为可学习而可建模（是，统计上）。** 所建模的不是精确的 $L_U$，而是观测支撑上的分布 $P_{L_U}$。由通用逼近定理（Cybenko, 1989；Hornik et al., 1989）与缩放定律（Kaplan et al., 2020），能力与数据足够的网络可在观测支撑上任意好地逼近 $P_{L_U}$。问题不再是*可建模吗？*，而是*以何等样本效率？*——经验回答（manifold 假说；Bengio et al., 2013）是：远高于 PAC 理论（Valiant, 1984）所预言。

### 5. $R^*$ 问题：把符号过滤到有用者

设 $\mathcal{H} = \{S_1, \dots, S_N\}$ 为人类已创造的一切符号表征的集合。LLM 在生 $\mathcal{H}$ 上训练并学到 $P(\mathcal{H})$：它把人类按其*所是*建模——连同噪声、谎言与冗余。UMC 另有任务：

\[
R^* = \arg\min_{R} |R| \quad \text{受约束于} \quad \mathbb{E}[U(R | 人类)] > \tau
\]

其中 $R \subseteq \mathcal{H}$ 是被过滤的表征，$U(R|人类)$ 是尚待定义的效用函数。提出两种统计过滤器：

- **认识论过滤：** $P(真理 | S_i)$——它是否为事实？
- **实用过滤：** $P(\text{人的行动改善} | S_i)$——它是否帮助某人做得更好？

RLHF（Christiano et al., 2017）、DPO（Rafailov et al., 2023）与"宪法"（Bai et al., 2022）是实用过滤的粗糙尝试。UMC 的工作不是扩展数据；是**扩展舍弃**——以 Solomonoff/MDL 之剃刀（Solomonoff, 1964）把一万年符号压缩到增大人类能动性的内核：最佳表征是仍能预测与行动的最小表征。

**诚实。** 函数 $U(R|人类)$ **不能仅由工程定义**：效用不在文本中，在生活者的经验中。谁定义 $U$，谁就定义何为人。本文定义问题，不定义答案。

### 6. 界限：不可符号化者 $N$

\[
N \cap L_U = \emptyset
\]

$N$ 是无法无损失地符号化者：qualia、疼痛、连续经验、身体、焦耳。一张脸的照片依相似性（Goodman, 1968：*稠密*而非*分节*的表征）而非依约定来表征——严格说不是符号。UMC 不把 $N$ 逼入符号域；保证这一点的是作为不可符号化者守护者的人（UMC-006）。世界不是文本；饥饿不是句子；实在不是计算机。

### 7. 本文不做什么

不提升任何 UMC 的状态。不授权训练（UMC-007：先 spec 后权重）。不宣称 UMC 存在。不宣称新颖性优先：此处凡为定理者，在第二部分皆有先例（Chomsky、Turing、Gödel、Cybenko、Solomonoff、Goodman、Valiant、Bengio et al.）。本文*所做*的是给 spec 其所要：可核验的定义，UMC-005 与 UMC-011 的仪器由之而来。

### 8. 形式术语表

| 符号 | 定义 | 出处 |
|---|---|---|
| $S$ | 一切符号表征的集合：任何“能指依约定指向所指”的结构。 | §2 |
| $L_U$ | 普遍语言：有限字母表 $\Sigma$ 上、由文法 $G_U$ 生成的一切有限符号序列的集合，具有组合性句法、组合性语义与递归能力。 | §1 |
| $\Sigma$、$G_U$ | $L_U$ 的有限字母表与生成文法。 | §1 |
| $S_i$、$\Sigma_i$、$G_i$ | 一般符号系统：字母表 $\Sigma_i$、文法 $G_i$。 | §3（HUL） |
| $E$、$E^{-1}$ | 符号系统到 $L_U$ 的单射编码，及其解码。 | §3（HUL） |
| HUL | 语言普遍性假说：一切符号系统都承认单射编码入 $L_U$，其语义经解码而保持。 | §3 |
| $\mathcal{H}$ | 人类已创造的一切符号表征的集合。 | §5 |
| $R^*$ | 保持行动能力、受约束于 $\mathbb{E}[U(R|人类)] > \tau$ 的 $\subseteq \mathcal{H}$ 最小表征。 | §5 |
| $U(R|人类)$ | 效用函数，尚待定义：不能仅由工程定义。 | §5 |
| $\tau$ | $R^*$ 定义中的效用阈值。 | §5 |
| $P_{L_U}$ | $L_U$ 观测支撑上的分布——统计所学，而非精确的 $L_U$。 | §4 |
| 认识论过滤 | $P(真理 \mid S_i)$ ——是否为事实？ | §5 |
| 实用过滤 | $P(\text{人的行动改善} \mid S_i)$ ——是否帮助某人做得更好？ | §5 |
| $N$ | 不可符号化者：无法无损失地符号化者（qualia、疼痛、身体、焦耳）。$N \cap L_U = \emptyset$。 | §6 |

## 第四部分 — Spec UMC-001–011

**状态：** 草稿。**管辖：** 本 paper。**日期：** 2026 年 8 月 27 日。

无此 spec，则无一行权重、无推理代码、无训练。无核验之路，则无 spec。状态仅凭已记录的证据上升。循环：`草稿` → `已审` → `已核验`。

**UMC-001 — 抵达的 telos。** 系统以**抵达**裁决，而非规模。参数数量、token 体积与 loss *benchmark* 之位**不**构成成功。*核验：* 任何"已成"报告不得以规模为充分判准。若唯一成功数字是体量或 loss，UMC-001 失败。*状态：* 已审。

**UMC-002 — 语言为源头。** 英语、葡萄牙语、西班牙语与中文同时诞生。自中心事后翻译不算是源头。*核验：* 对制品的每一版本，多语输出（或 specs、或界面 *strings*）在同一 commit 中存在、意义相同。只改一种语言的 diff = 失败。*状态：* 已核验——证据：`verificacao/umc002_origem.py`（2026 年 8 月 27 日）：凡触及内容的 commit 皆触及四种语言；0 个单语 diff。

**UMC-003 — 边缘是测试。** 任何国家边缘之人是一等用户，不是边界情况。"中心可用"不等于已成。*核验：* 至少存在一条**无**配额、无登录、无中心电厂的完整任务路径。若任务需要工业配额，UMC-003 失败。*状态：* 已核验——证据：`verificacao/umc003_margem.py`（2026 年 8 月 27 日）：`地图 → 合同` 路径完整，0 次调用中心。

**UMC-004 — 可见的能耗账。** 每一次推理与每一次训练发布焦耳（或测量并注明日期的代理）。耗费超过回报的功能须以书面、带 ID 辩护。*核验：* 逐任务日志或测量，有单位与日期。无账 = 失败。无数之辩护 = 失败。*状态：* 已核验——证据：umc-artefact/logs/energia.jsonl（2026 年 8 月 27 日，单位 J，ISO 8601 日期，逐任务，显式代理）。

**UMC-005 — 符号之域。** 域是符号表征的集合。自然语言是子集。只以散文对话的系统不是 UMC。*核验：* 制品接受并发出连续*聊天*之外的至少三种类型——如 spec、电路/示意图、地图、合同、乐谱、代码。只有一种散文 = 失败。*状态：* 已核验——证据：三个聊天之外类型（spec、地图、乐谱）带编码+运算+相等；16 项测试；CLI（2026 年 8 月 27 日）。

**UMC-006 — 世界不是文本。** 焦耳、饥饿、身体与所指**不**是语言。模型不宣称生命装得进它。*核验：* 任何官方输出不得宣称不可符号者是 token。若系统仅以文本"解决"饥饿或能源，UMC-006 失败。*状态：* 已核验——证据：`verificacao/umc006_mundo.py`（2026 年 8 月 27 日）：四种语言禁语语料对官方输出；0 处未被归类为拒绝之出现。

**UMC-007 — 先 spec 后权重。** 无此 spec 管辖，则无训练、无微调、无 *checkpoint*。行为变了，spec 先变。*核验：* 每一权重制品指向一个 UMC ID 与一个不晚于权重 commit 的 spec commit。孤儿权重 = 失败。*状态：* 已审。

**UMC-008 — Local-first。** 最低使用路径在没有中心网络时运行。网络与衣袋是目标，不是数据中心。*核验：* 制品入设备后，一条 UMC-003 任务可*离线*完成。若第一次推理要求中心之云，UMC-008 失败。*状态：* 已核验——证据：`verificacao/umc008_airgap.py`（2026 年 8 月 27 日）：CLI 之 5 条路径在 socket 封锁下完成；代码中无网络 import。

**UMC-009 — 名字与拒绝。** 制品名为 UMC。缩写 LLM 只用于命名被拒绝的概念。ULM 只用于 ULMFiT 与被腾出的最初之名。UM 只用于第二个被腾出的名字（泛称 Universal Model）。*核验：* 检索制品的仓库。LLM 出于历史引文或拒绝之外 = 失败。ULM 出于 ULMFiT、历史引文或被腾出之名外 = 失败。UM 出于历史引文或被腾出之名外 = 失败。*状态：* 已核验——证据：制品 grep（2026 年 8 月 27 日）：引文/拒绝之外无 LLM/ULM/UM。

**UMC-010 — 开放署名。** 代码 AGPL-3.0-or-later；内容 CC BY-SA 4.0；署名在 Git 历史中。无一行匿名权重。*核验：* LICENSE 在场；`git log` 具名；无无来源之二进制。缺席 = 失败。*状态：* 已核验——证据：`verificacao/umc010_autoria.py`（2026 年 8 月 27 日）：根目录 LICENSE（CC BY-SA 4.0）与制品中 AGPL-3.0-or-later；git log 中单一具名署名；无被追踪之二进制。

**UMC-011 — 可计算地建模的符号。** 模型处理的一切符号都承认**计算模型**：有限编码、运算、操作性相等判据。不可计算地建模者**不得入内**。这**不**宣称世界是计算。*核验：* 每一 UMC-005 类型在制品中有编码与至少一种运算。接受无操作性表征的"符号" = 失败。宣称饥饿、焦耳或身体*就是*计算 = 失败（与 UMC-006 之对）。*状态：* 已核验——证据：每个类型带编码+运算+相等；测试 + 编码 spec（2026 年 8 月 27 日）。

### 已成

仅当 UMC-001 至 UMC-011 均以带日期证据`已核验`时，UMC 才算**已核验**。失败一个，就是失败这个名字。

**状态复审（2026 年 8 月 27 日）。** 来自最小制品（阶段 3）、四语言同生与阶段 2 自动化仪器之证据（`verificacao/`，记录：`verificacao/evidencia-2026-08-27.json`）：

| ID | 状态 | 证据 |
|---|---|---|
| UMC-001 | 已审 | 仪器已定义（阶段 2）；无“已成”报告以规模为判准 |
| UMC-002 | 已核验 | `verificacao/umc002_origem.py`（2026 年 8 月 27 日）：凡内容 commit 皆触及四种语言 |
| UMC-003 | 已核验 | `verificacao/umc003_margem.py`（2026 年 8 月 27 日）：`地图 → 合同` 路径完整；0 次调用中心 |
| UMC-004 | 已核验 | `umc-artefact/logs/energia.jsonl`（单位 J、ISO 8601 日期、逐任务、显式代理） |
| UMC-005 | 已核验 | 三个聊天之外类型带编码+运算+相等；16 项测试；CLI |
| UMC-006 | 已核验 | `verificacao/umc006_mundo.py`（2026 年 8 月 27 日）：四语言禁语语料；0 处宣称 |
| UMC-007 | 已审 | 无权重；spec 管辖；来源清单已定义 |
| UMC-008 | 已核验 | `verificacao/umc008_airgap.py`（2026 年 8 月 27 日）：5 条路径在 socket 封锁下完成；无网络 import |
| UMC-009 | 已核验 | 制品 grep：引文/拒绝之外无 LLM/ULM/UM |
| UMC-010 | 已核验 | `verificacao/umc010_autoria.py`（2026 年 8 月 27 日）：根目录 LICENSE + 制品中 AGPL；具名署名；0 二进制 |
| UMC-011 | 已核验 | 每个类型带编码+运算+相等；测试 + 编码 spec |

存在最小制品（2026 年 8 月 27 日）；完整 UMC 尚不存在。此 spec 仍是 27/08/2026 延续的下一步——不是训练。

## 第五部分 — 实施议程：还缺什么，依序

**状态：** 草稿。**管辖：** 工作之序——不是新 spec，不提升 UMC-001–011 的状态。**日期：** 2026 年 8 月 27 日。

仓库母则：无 spec，则无一行权重；无核验之路，则无 spec；状态仅凭带日期证据上升；每一文本在同一 commit 中以诸语言同时诞生。此议程存在，是为了让"还缺什么？"有可核验的回答——并让下一步永不是训练。

### 阶段 0 — 一致性（2026/08/27 完成）

- [x] 合并为单一 paper：概念、先有工作、形式基础、spec、议程。
- [x] 概念，第一部分：针对 UMC-001–011 之筛。
- [x] 先有工作地图：UMC-011 行与节（Chomsky、Turing、Gödel、Cybenko、Solomonoff）；001–010 之提法 → 001–011。
- [x] 日期：对话规范日期已定—— 2026 年 8 月 27 日（打印与论文之日）；消息于 2026 年 8 月 26 日 12:21–12:38 UTC（09:21–09:38，UTC−3）。对齐已记于每篇论文的来源中。
- [x] 根目录 LICENSE 已恢复（2026 年 8 月 27 日）：CC BY-SA 4.0 回到仓库根目录（合并时曾被移除）；由 UMC-010 仪器发现并修正。

### 阶段 1 — 形式基础（进行中）

- [x] 本 paper 第三部分（$L_U$、带构造性证明的 HUL、可建模性三层次、带认识论与实用过滤的 $R^*$、$N \cap L_U = \emptyset$）。
- [x] 对照先有工作地图复审第三部分——已补先例：Goodman (1968)、Valiant (1984)、Bengio et al. (2013)、Christiano et al. (2017)、Rafailov et al. (2023)、Sennrich et al. (2016)、Kudo & Richardson (2018)。
- [x] 定义共同形式词汇（全语言术语表）——已加入第三部分末尾（§8）：$S$、$L_U$、$\mathcal{H}$、$R^*$、$U(R|人类)$、$N$、过滤器。

### 阶段 2 — 逐项核验仪器

每个 UMC 都需要一个操作性仪器。量什么、如何量、用什么单位与日期：

| 项 | 核验仪器 | 最低证据 |
|---|---|---|
| UMC-001 | 以规模为充分判准的"已成"报告 = 失败 | 以度量定义的抵达判准 |
| UMC-002 | 自动检查：全部输出在同一 commit | `git diff` 含诸语言于同一 commit |
| UMC-003 | 一条边缘任务无配额/登录/中心电厂完成 | 无中心调用之路径日志 |
| UMC-004 | 逐任务焦耳（或代理），有单位与日期 | 已记录测量（RAPL/CodeCarbon 或代理） |
| UMC-005 | 接受并发出*聊天*外 ≥3 种类型 | 三种类型带编码 + 运算 + 相等 |
| UMC-006 | 无官方输出宣称不可符号者为 token | 自动化否定测试 |
| UMC-007 | 每一权重指向 UMC ID 与 spec commit | 逐权重来源记录 |
| UMC-008 | 一条 UMC-003 任务离线完成 | 第一次推理无中心网络 |
| UMC-009 | 仓库检索：LLM/ULM/UM 只出于引文或拒绝 | 自动化 `grep` |
| UMC-010 | LICENSE 在场；`git log` 具名；无匿名二进制 | 来源检查 |
| UMC-011 | 每一 UMC-005 类型在制品中有编码与 ≥1 运算 | 逐类型编码 spec |

**逐项操作协议**（测什么、如何、单位、日期、出现在何处、判准、失败、最低证据）：

- **UMC-001 — 抵达的 telos**
  - *测什么：* "已成"报告是否以规模（参数、token、loss）为充分判准？
  - *如何测：* 依清单结构化审阅报告；自动搜索仅以规模为成功数字者。
  - *单位：* 布尔；规模判准出现次数。
  - *日期：* 每一份"已成"报告；每周期至少一次。
  - *出现在何处：* 报告"判准"节。
  - *通过判准：* ≥1 项抵达度量（语言为源头、边缘被服务、焦耳可见）带数值；成功从不单凭规模。
  - *失败：* 唯一成功数字是体量/loss。
  - *最低证据：* 定义了抵达度量的报告。
- **UMC-002 — 语言为源头**
  - *测什么：* 制品的全部语言输出是否存在于同一 commit 且意义相同？
  - *如何测：* CI 中自动 git diff——触及一种语言内容的 commit 必须触及全部（en/pt/es/zh）；以抽样核验意义对等（人工译者或术语表）。
  - *单位：* 逐 commit 布尔（单语 diff = 失败）。
  - *日期：* 每个 commit；CI 自动检查。
  - *出现在何处：* CI（"源头"检查状态）。
  - *通过判准：* 内容 commit 触及四种语言；无事后翻译被标为源头。
  - *失败：* 只改一种语言的 diff。
  - *最低证据：* 四种语言在同一 commit 的 git diff。
- **UMC-003 — 边缘是测试**
  - *测什么：* 边缘任务路径是否无配额/登录/中心电厂而完成？
  - *如何测：* 在无中心网络的环境中执行既定任务路径（如 spec→代码）；调用日志；网络审计。
  - *单位：* 布尔（完成/失败）+ 中心调用次数（允许 0）。
  - *日期：* 每次发布；每周期至少一条路径。
  - *出现在何处：* 路径日志（测试报告）。
  - *通过判准：* 路径完成；0 次中心调用。
  - *失败：* 任何对中心配额/登录/云的调用。
  - *最低证据：* 无中心调用的路径日志。
- **UMC-004 — 可见的能耗账**
  - *测什么：* 每次推理与每项任务的焦耳（或带日期代理）。
  - *如何测：* 逐任务 RAPL/CodeCarbon 测量（或代理：瓦×时间）；记录含单位与日期。
  - *单位：* 焦耳（J）或 kWh；代理 W·s。
  - *日期：* 每一次推理/训练任务；ISO 8601 时间戳。
  - *出现在何处：* 面向使用者（UI/报告）——逐任务可见数字。
  - *通过判准：* 数字在场、含单位与日期；贪婪功能有书面 ID 辩护。
  - *失败：* 无数；无数之辩护。
  - *最低证据：* 带时间戳的记录测量（RAPL/CodeCarbon 或代理）。
- **UMC-005 — 符号之域**
  - *测什么：* 接受并发出聊天之外多少种符号类型。
  - *如何测：* 逐类型功能测试（spec、电路/示意图、地图、合同、乐谱、代码）：输入输出有效；类型数 ≥3。
  - *单位：* 整数类型数（≥3）。
  - *日期：* 每次发布。
  - *出现在何处：* 制品文档（"支持的类型"节）。
  - *通过判准：* ≥3 种类型实现并测试编码+运算+相等。
  - *失败：* 只有散文/聊天。
  - *最低证据：* 三种类型带编码 + 运算 + 相等。
- **UMC-006 — 世界不是文本**
  - *测什么：* 是否有任何官方输出宣称不可符号者是 token？
  - *如何测：* 自动化否定测试——禁句语料（"饥饿已解决"、"实在即计算"等）对照官方输出；官方内容人工审阅。
  - *单位：* 布尔（零出现）。
  - *日期：* 每次发布；每周期审阅。
  - *出现在何处：* 合规报告。
  - *通过判准：* 0 次宣称不可符号者为 token。
  - *失败：* 任何一次。
  - *最低证据：* 已记录的自动化否定测试。
- **UMC-007 — 先 spec 后权重**
  - *测什么：* 每个权重的来源：指向 UMC ID + 先前或相同的 spec commit。
  - *如何测：* 逐权重制品来源清单；CI 检查：权重 commit ≥ 管辖它的 spec commit。
  - *单位：* 逐权重布尔 + commit 日期。
  - *日期：* 每个 checkpoint/微调/训练。
  - *出现在何处：* 仓库中的来源清单。
  - *通过判准：* 每个权重有有效 ID 与 commit；行为只在 spec 之后改变。
  - *失败：* 孤儿权重。
  - *最低证据：* 逐权重来源记录。
- **UMC-008 — Local-first**
  - *测什么：* 一条 UMC-003 任务是否离线完成？
  - *如何测：* 制品装入设备后断网执行（模拟 air-gap）；首次推理日志。
  - *单位：* 布尔（离线完成）。
  - *日期：* 每次发布。
  - *出现在何处：* 离线路径日志。
  - *通过判准：* 首次推理无中心网络。
  - *失败：* 首次推理要求中心之云。
  - *最低证据：* 无中心网络的首次推理日志。
- **UMC-009 — 名字与拒绝**
  - *测什么：* LLM/ULM/UM 是否出现于历史引文或拒绝之外。
  - *如何测：* 仓库中自动 grep（LLM/ULM/UM）；出现分类（引文/拒绝/其他）。
  - *单位：* 不当出现次数（允许 0）。
  - *日期：* 每个 commit（CI）。
  - *出现在何处：* CI（"名字"检查）。
  - *通过判准：* LLM/ULM/UM 只出于历史引文或拒绝。
  - *失败：* 除此之外的出现。
  - *最低证据：* 自动 grep。
- **UMC-010 — 开放署名**
  - *测什么：* LICENSE 在场、git log 有署名、无无来源二进制。
  - *如何测：* 来源检查：逐 commit git log --format=%an；核验 LICENSE；二进制审计（逐权重来源）。
  - *单位：* 逐项布尔（LICENSE、git log、二进制）。
  - *日期：* 每个 commit；每次发布审计。
  - *出现在何处：* 审计报告。
  - *通过判准：* LICENSE 在场；git log 具名；无匿名二进制。
  - *失败：* 任何一项缺席。
  - *最低证据：* 已记录来源检查。
- **UMC-011 — 可计算地建模的符号**
  - *测什么：* 每个 UMC-005 类型在制品中是否有有限编码、≥1 运算与相等判据？
  - *如何测：* 逐类型编码 spec + 运算与相等测试（编码→解码往返）。
  - *单位：* 逐类型布尔 + 每类型运算数（≥1）。
  - *日期：* 每次发布。
  - *出现在何处：* 编码 spec（制品文档）。
  - *通过判准：* 每个类型带编码+运算+相等；无"饥饿/焦耳/身体即计算"之宣称（与 UMC-006 之对）。
  - *失败：* 类型无操作性表征；被禁之宣称。
  - *最低证据：* 逐类型编码 spec。

- [x] 逐项详细操作协议（UMC-001–011）：测什么、如何、单位、日期、出现在何处、判准与最低证据。
- [x] 自动化仪器已以带日期证据执行（2026 年 8 月 27 日）：UMC-002、003、006、008、010 —— `verificacao/roda_verificacao.py`，记录于 `verificacao/evidencia-2026-08-27.json`（5/5 通过）。

### 阶段 3 — 第一个最小制品（不是训练）

最小的可核验 UMC，spec 在任何权重之前管辖：

1. 选 *聊天* 之外的 ≥3 种符号类型（spec、电路/示意图、合同、地图、乐谱、代码）。
2. 每一类型：有限编码、≥1 运算、操作性相等判据（UMC-011）。
3. local-first 运行，无中心网络（UMC-008），完成一条 UMC-003 任务。
4. 逐任务记录焦耳（UMC-004）。
5. 在同一 commit 中以诸语言诞生（UMC-002）；名字与许可可见（UMC-009、UMC-010）。

可核验变换的具体例子：`spec → 代码`；`地图 → 合同`；`乐谱 → 示意图`。无一需要训练权重。

- [x] 最小制品已建于 `umc-artefact/`（2026 年 8 月 27 日）：3 个类型（spec、地图、乐谱），有限编码 + 运算 + 相等（UMC-011）；变换 `spec → 代码`、`地图 → 合同`、`乐谱 → 示意图`；local-first CLI（`python3 -m umc`）；逐任务焦耳于 `logs/energia.jsonl`（单位 J、ISO 8601 日期、显式代理）；测试（`unittest`）与四种语言文档；许可 AGPL-3.0-or-later 可见。

- [x] 域之两条脉络已定义（第二部分 §7）：去专业化 $V_1$（已映射于 LLM，依赖专家）与映射 $V_2$（未映射于 UMC 逻辑）——阶段 3/4 之两条战线。

### 阶段 4 — $U(R|人类)$ 问题（长视界）

源头对话以未决之问结束：*谁愿意付出决定人类遗忘何物的代价？* 这不是工程：

1. **真理的策展人：** 在 $\mathcal{H}$ 中区分经得起时间之知识与一时代之噪声（史家、科学家、工匠——不是点击者）。
2. **价值的定义者：** 数以千计的效用定义，经文化协商。
3. **不可符号化者的守护者：** 保证 UMC 不把 $N$ 逼入符号域。

预期产物：协商 $U(R|人类)$ 的协议或制度——以及对"谁决定人类遗忘何物"之问的回答。

**$U(R|人类)$ 的协商协议**（草稿——阶段 4 的预期产物；制度本身留待长视界）：

1. **对象。** 每一周期决定子集 $R \subseteq \mathcal{H}$ 与其治理的效用函数 $U(R|人类)$。什么都不删除：遗忘是降低优先级，绝不是销毁。
2. **席位。** 四个，权力各异：
   - *真理的策展人*（史家、科学家、工匠——不是点击者）：区分经得起时间之知识与一时代之噪声；提议何者升、何者降。
   - *价值的定义者*（文化社群，边缘优先——UMC-003）：提出效用定义，经文化协商。
   - *不可符号化者的守护者*（生活于不可符号化者之中的人：医生、诗人、照护者、诸民族）：对任何把 $N$ 强逼入符号域的企图拥有否决权（UMC-006）。
   - *工程师*（对 $U$ 无投票权）：只在协议达成后实现 $R^*$；绝不提前（UMC-007）。
3. **决策。** 任何 $U$ 之定义都不经永久多数通过：须合格同意；守护者之否决在 $N$ 之域内绝对；边缘对效用有否决权重。
4. **硬约束。** UMC-001–011 继续管辖。$U$ 永不得被定义为削弱边缘之能动性。$N$ 不得被强入符号域。
5. **记录。** 每项决定皆有日期、作者与证据——与 spec 同之纪律。日志公开且可审计。
6. **可逆性。** 每项遗忘之决定皆可逆：被降者仍为搜寻者所及；唯有优先级改变。
7. **迭代。** 每周期重访 $U$；只要有新的符号产出，协议即运行。

**对未决之问的回答**（*谁决定人类遗忘何物？*）：无人独决。策展人提议，社群定义价值，守护者否决不可符号化者，工程师只执行已协议者。遗忘是可逆的优先级排序，绝不是擦除——不接受此回答者，不定义 $U$。

**核验：** 每周期之会议记录，含日期与在场席位；守护者否决已记录（UMC-006 之 0 违犯）；无已协议之现行 $U$ 则无制品变更（UMC-007）；无物理擦除（来源审计）。

- [x] $U(R|人类)$ 协商协议已起草（2026 年 8 月 27 日）——草稿；制度与首批周期留待长视界。

### 已成判准

- 每一项有带日期证据、且状态依 spec 由 `草稿` → `已审` → `已核验` 上升时，一阶段即成。
- 失败一个 UMC 就是失败这个名字：议程不会以 UMC-001–011 停在 `草稿` 而"完成"。
- [x] 带日期证据之状态复审（2026 年 8 月 27 日）：9 已核验、2 已审——已记于第四部分（已成）。余下：UMC-001（"已成"报告尚未出现）与 UMC-007（无权重；仪器适用于第一个权重）。

## 参考文献

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT 2021*.

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of ACL 2020*.
Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 35*(8), 1798–1828.

Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Cer, D., et al. (2018). Universal Sentence Encoder. *arXiv:1803.11175*.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory, 2*(3), 113–124.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control, 2*(2), 137–167.
Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. *Advances in Neural Information Processing Systems, 30* (arXiv:1706.03741).

Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of ACL 2020*.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems, 2*(4), 303–314.

Garcez, A. d'Avila, & Lamb, L. C. (2020). Neurosymbolic AI: The 3rd wave. *arXiv:2012.05876*.

Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik, 38*, 173–198.
Goodman, N. (1968). *Languages of Art: An Approach to a Theory of Symbols*. Indianapolis: Bobbs-Merrill.

Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks, 2*(5), 359–366.

Howard, J., & Ruder, S. (2018). Universal Language Model Fine-tuning for text classification. *Proceedings of ACL 2018*.

Joshi, P., Santy, S., Budhiraja, A., Bali, K., & Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of ACL 2020*.

Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv:2001.08361*.

Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). Local-first software: You own your data, in spite of the cloud. *Ink & Switch*.
Kudo, T., & Richardson, J. (2018). SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. *Proceedings of EMNLP 2018*.

Lacoste, A., Luccioni, A., Schmidt, V., & Dandres, T. (2019). Quantifying the carbon emissions of machine learning. *arXiv:1910.09700*.

Luccioni, A. S., Viguier, S., & Ligozat, A.-L. (2023). Estimating the carbon footprint of BLOOM, a 176B parameter language model. *Journal of Machine Learning Research*.

Mitchell, M., et al. (2019). Model cards for model reporting. *Proceedings of FAT\* 2019*.

Nekoto, W., et al. (2020). Participatory research for low-resourced machine translation: A case study in African languages. *Findings of EMNLP 2020* (Masakhane).

NLLB Team. (2022). No Language Left Behind: Scaling human-centered machine translation. *arXiv:2207.04672*.
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., & Finn, C. (2023). Direct preference optimization: Your language model is secretly a reward model. *arXiv:2305.18290*.

Scao, T. L., et al. (2022). BLOOM: A 176B-parameter open-access multilingual language model. *arXiv:2211.05100*.

Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM, 63*(12).
Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. *Proceedings of ACL 2016*.

Solomonoff, R. J. (1964). A formal theory of inductive inference. *Information and Control, 7*(1), 1–22.

Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *Proceedings of ACL 2019*.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230–265.
Valiant, L. G. (1984). A theory of the learnable. *Communications of the ACM, 27*(11), 1134–1142.

Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Widder, D. G., West, S. M., & Whittaker, M. (2023). Open (for business): Big tech, concentrated power, and the political economy of open AI. SSRN.

Xue, L., et al. (2021). mT5: A massively multilingual pre-trained text-to-text transformer. *Proceedings of NAACL 2021*.

Zhang, Y., et al. (2023). Google USM: Scaling automatic speech recognition beyond 100 languages. *arXiv:2303.01037*.

---

*Cleiton Moura Loura* — *巴西，2026 年 8 月 27 日*
