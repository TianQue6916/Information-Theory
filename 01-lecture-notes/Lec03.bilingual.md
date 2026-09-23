> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l3 · 行内双语视觉转录版 · 原图见 fig/l3/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l3-p1](fig/l3/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 本页为第 3 讲（Lecture 3）标题页。主标题：**Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）**，其下标注 **Lecture 3（第 3 讲）**。页面底部给出课程网址：`www.inference.phy.cam.ac.uk/itprnn/`。页面左侧有一幅圆形分形树图案：一棵绿色的树状结构，节点为圆圈与方块交替连接，树枝向外逐级分支、越来越细密，末梢点缀着蓝色与红色的小圆圈，整棵树收拢在一个大圆之内。

### p.2 〔Course outline（课程大纲）〕

![l3-p2](fig/l3/mgp00002.png)

<span style="color:#2471a3;">**[section]**</span> 课程大纲分为两大板块：

- **Information Theory（信息论）**
  - Source coding（信源编码），即 Data compression（数据压缩）
  - Noisy-channel coding（噪声信道编码）
- **Data modelling, pattern recognition, learning & memory（数据建模、模式识别、学习与记忆）**
  - Tools（工具）：
    - Exact inference methods（精确推断方法）
    - Monte Carlo methods（蒙特卡洛方法）
    - Variational methods（变分方法）
  - Neural networks（神经网络）

页面右下角再次出现与上一页相同的圆形分形树图案。

### p.3 〔How to compress a redundant file?（如何压缩一个冗余文件？）〕

![l3-p3](fig/l3/mgp00003.png)

<span style="color:#2471a3;">**[example]**</span> 页面主体是一整屏密集排布的 0/1 二进制数字块（约 25 行 × 80 列，绝大多数是 0，1 稀疏地散布其间）。图下方红色文字给出这串数据的来源：

e.g., $N = 1000$ tosses of a bent coin with $p_1 = 0.1$（例如：$N=1000$ 次投掷一枚不均匀硬币（bent coin），其中出现 1 的概率 $p_1=0.1$）。

### p.4 〔How to measure information content?（如何度量信息量？）〕

![l3-p4](fig/l3/mgp00004.png)

<span style="color:#2471a3;">**[definition]**</span> 本页给出两条 **Claims:（论断）**：

1. 某个结果（outcome）的 **Shannon information content（Shannon 信息量）**——即自信息（self-information）：

   $h(x=a_i) \;=\; \log_2 \frac{1}{P(x=a_i)}$

   是信息量（information content）的一个合理度量（a sensible measure）。

2. **entropy（熵）**：

   $H(X) \;=\; \sum_x P(x)\,\log_2 \frac{1}{P(x)}$

   是期望信息量（expected information content）的合理度量。

> <span style="color:#7f8c8d;">旁注：页面左下角有两行黄色小字，为讲者备课提示："(sketch h(p))"（画出 h(p) 的草图）、"Point out additivity of h."（指出 h 的可加性）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这两条定义本质上是把"信息量"定义成概率的函数，再对它取期望。$h(x=a_i)=\log_2\frac{1}{P(x=a_i)}$ 只依赖该结果的概率：越罕见的结果自信息越大，概率为 1 的必然事件自信息为 0。熵 $H(X)=\sum_x P(x)\,h(x)$ 恰是自信息这个随机变量在分布 $P$ 下的期望，即 $H(X)=\mathbb{E}[h(x)]$——这正是你在 Bertsekas 概率论中学过的"期望 = 随机变量按概率加权平均"的直接应用。对数以 2 为底时信息单位是比特（bit），与 CSAPP 中一个二进制位相对应：一个 0/1 各半的均匀比特携带 1 比特信息，而一个几乎恒为 0 的比特携带的信息趋近 0。讲者提醒"画出 $h(p)$ 的草图"：$h(p)=\log_2\frac1p$ 是 $p$ 的减函数、凸函数，在 $p=1/2$ 处取值 1，$p\to 1$ 时趋于 0；这条曲线后面分析熵的性质时会反复用到。此外，遇到 $p=0$ 的项须按约定 $p\log_2\frac1p\to 0$ 处理，这在计算含零概率的熵时必须用到。</span>

### p.5 〔Testing 'Shannon information content' claims（检验"Shannon 信息量"论断）〕

![l3-p5](fig/l3/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span> 本页标题下的第一个检验例子：**Weighing problem（称重问题）**。配图为一张天平示意图：一架红色天平，左盘放 2 个青色圆球，右盘也放 2 个圆球，天平底座旁还堆放着另外 8 个圆球（合计 12 个球）。

图下方的要点：

**Shannon says（Shannon 说）**：Most 'informative' experiment is the one with maximum entropy（最有"信息量"的实验，就是熵最大的那个实验）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** 称球问题是检验"熵度量信息"的第一块试金石。经典设定是 12 个球中恰有 1 个坏球（不知偏轻还是偏重），天平每称一次有"左倾、右倾、平衡"三种结果，$k$ 次称量共有 $3^k$ 种可区分的结果序列，因此要区分全部情况，称量次数至少为 $\log_3(\text{需区分的情况数})$ 的上取整。这和你在 6.006 里分析决策树深度、CLRS 里证明比较排序下界 $\Omega(n\log n)$ 是同一套论证：任何策略都对应一棵决策树，叶子必须多到足以给每种可能性一个结局，树高就是所需提问次数。"熵最大的实验最有信息量"落到实处就是：把每个问题设计成各答案的概率尽量均等，使每次提问获得接近其上限的比特数，避免"问了等于白问"的冗余提问——这与二十个问题的二分策略一脉相承，也是后面"典型集把概率质量集中起来"这一核心思想的雏形。</span>

### p.6 〔How to measure information content?（如何度量信息量？）〕

![l3-p6](fig/l3/mgp00006.png)

<span style="color:#2471a3;">**[definition]**</span> 本页与 p.4 为同一标题页的完整版，论断扩展为三条：

1. 某个结果的 **Shannon information content（Shannon 信息量）**：

   $h(x=a_i) \;=\; \log_2 \frac{1}{P(x=a_i)}$

   是信息量的一个合理度量。

2. **entropy（熵）**：

   $H(X) \;=\; \sum_x P(x)\,\log_2 \frac{1}{P(x)}$

   是期望信息量的合理度量。

3. **Source coding theorem（信源编码定理）**——来自信源 $X$ 的 $N$ 个结果可以被压缩（can be compressed）到大约 $NH(X)$ 比特（bits）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** 第 3 条论断是本课程第一个"定理级"的定量陈述：$N$ 个结果压到约 $NH(X)$ 比特，即平均每个符号只花 $H(X)$ 比特。用 p.3 的文件做个直观验算：若把每个 0/1 原样存盘需要 $N$ 比特；而对 $p_1=0.1$ 的信源，$H=H_2(0.1)\approx 0.469$ 比特/结果，理论极限约 $0.469N$ 比特，节省一半以上。注意措辞里"大约（roughly）"二字：定理的精确表述和证明要等典型集（typical set）工具在第 4 章就位后才成立，本页先作为论断抛出，留待后面兑现。还要留意单位：$H(X)$ 的单位是比特/结果，乘以结果个数 $N$ 才得到总比特数，量纲才自洽。这个"平均每符号 $H$ 比特"的思想正是"信源编码定理"名字的由来；后续将看到，哈夫曼编码等符号码（symbol code）能做到的期望码字长度被夹在 $H$ 与 $H+1$ 之间，而算术编码可进一步逼近 $H$。</span>

### p.7 〔The Bent Coin Lottery（不均匀硬币彩票）〕

![l3-p7](fig/l3/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 题设：

- A coin with $p_1 = 0.1$ will be tossed $N = 1000$ times.（一枚 $p_1=0.1$ 的硬币将被投掷 $N=1000$ 次。）
- The outcome is $\mathbf{x} = x_1 x_2 \ldots x_N$.（结果是一个长度为 $N$ 的序列 $\mathbf{x} = x_1 x_2 \ldots x_N$。）
- e.g., $\mathbf{x}$ = 0000001001000100…00010（例如 $\mathbf{x}$ = 0000001001000100…00010）。
- You can buy any of the $2^N$ possible tickets for £1 each, before the coin-tossing.（在投币之前，你可以以每张 £1 的价格购买 $2^N$ 张可能彩票中的任意一张。）
- If you own ticket $\mathbf{x}$, you win £1,000,000,000.（如果你持有的彩票 $\mathbf{x}$ 与投币结果完全一致，你就赢得 £1,000,000,000，即十亿英镑。）

问题：

- **Q**：To have a **99%** chance of winning, at lowest possible cost, which tickets would you buy?（要想以 99% 的概率中奖，且总花费尽可能低，你会买哪些彩票？）
- • And how many tickets is that?（那样需要买多少张彩票？）
- Express your answer in the form $2^{(\cdots)}$.（请把答案写成 $2^{(\cdots)}$ 的形式。）

右侧边栏 **Lottery tickets available（可供购买的彩票）**：一个标着 $2^N$ 的大花括号，括号内自上而下罗列全部 $2^N$ 个二进制串：`0000000000.....00000`、`0000000000.....00001`、`0000000000.....00010`、`0000000000.....00011`、`0000000000.....00100`、`0000000000.....00101`、`0000000000.....00110`、`0000000000.....00111`，中间以省略号略去，再列 `0010000001.....01000`、……、直到 `1111111111.....11101`、`1111111111.....11110`、`1111111111.....11111`。

> <span style="color:#7f8c8d;">旁注：页面底部有一行黄色小字："We'll come back to this in a moment. First..."（我们稍后会回到这个问题。首先……）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这道彩票题是渐近均分性（AEP (asymptotic equipartition principle)）的绝妙预热。按 Bertsekas 概率论里的大数定律，$N=1000$ 次投掷中 1 的个数会以压倒性概率落在 $Np_1=100$ 附近，涨落量级约为 $\sqrt{Np_1(1-p_1)}\approx 9.5$；因此中奖序列几乎必然是"恰好含约 100 个 1"的那些串，而不是 $2^{1000}$ 张彩票平摊概率。精确算账：每条典型序列的概率约为 $2^{-NH}$，其中 $H=H_2(0.1)\approx 0.469$ 比特；要让中奖概率达到 99%，买下整个典型集就够了，所需张数约 $2^{NH}\approx 2^{469}$——虽是天文数字，却远小于 $2^{1000}$。顺带预告一个反直觉的点：概率最大的单张彩票是全 0 串，可它中奖概率只有 $0.9^{1000}$ 这个量级，几乎必输；"最可能的单张"与"最可能的结果集合"是两个完全不同的问题，这正是典型性（typicality）思想的起点。</span>

### p.8 〔Testing 'Shannon information content' claims（检验"Shannon 信息量"论断）〕

![l3-p8](fig/l3/mgp00008.png)

<span style="color:#2471a3;">**[example]**</span> 本页是标题页的目录式预告，列出三个检验例子（天平图与 p.5 相同：红色天平，左盘 2 个青色球、右盘 2 个球，底座旁另有 8 个球，共 12 个球）：

- **Weighing problem（称重问题）**
- **Sixty-three（六十三）**
- **Submarine（潜艇）**

（后续 p.9–p.11 依次展开这三个例子。）

### p.9 〔Sixty-three（六十三）〕

![l3-p9](fig/l3/mgp00009.png)

<span style="color:#2471a3;">**[example]**</span> 页面中央仅有一行公式：

$x \in \{0, 1, 2, 3, 4, 5, 6, \ldots, 63\}$

（即 $x$ 取值于 0 到 63 的全部整数，共 64 个可能取值。）

### p.10 〔Sixty-three（六十三）〕

![l3-p10](fig/l3/mgp00010.png)

<span style="color:#2471a3;">**[example]**</span> 正文：

We were able to give unique binary names to every one of **64** outcomes if each name was **6 bits** long.（只要每个名字长 6 比特，我们就能给 64 个结果中的每一个都起一个独一无二的二进制名字。）

e.g.（例如）：

- $c(42) = $ 101010
- $c(20) = $ 010100

**Generalize（推广）**——

- **Q**：If there are $S$ possible outcomes, **how many bits** long must each name be, if each outcome has a unique name?（如果有 $S$ 个可能的结果，要让每个结果都有唯一的名字，每个名字必须多长——多少比特？）

> <span style="color:#1e8449;">**[note] Note（译者注）:** "给 $S$ 个结果起唯一二进制名字，至少需要 $\lceil\log_2 S\rceil$ 比特"是整门课最基本的信息论下界，证明只需数数：长为 $L$ 的二进制串至多 $2^L$ 个，要覆盖 $S$ 个对象就必须 $2^L\ge S$。你在 CLRS 里见过的比较排序下界 $\Omega(n\log n)$ 正是同型论证：$n$ 个元素有 $n!$ 种排列，比较决策树的每个叶子只能对应一种排列，而每次比较恰好提供 1 比特信息，故树高至少 $\log_2(n!)\approx n\log_2 n$。另外注意 $c(42)=101010$、$c(20)=010100$ 用的是 6 位定长二进制表示，与 CSAPP 中无符号数的位表示完全一致——$\{0,\ldots,63\}$ 恰是 6 位机器字能表示的全部无符号整数，位运算（移位、掩码）在这里就是"名字"的生成规则。定长码对均匀分布是完美的，但对偏斜分布（如 p.3 的稀疏文件）会造成浪费，改用变长码又引入新的约束，这正是后面 Kraft 不等式与哈夫曼编码（Huffman coding）要解决的核心矛盾。</span>

### p.11 〔Submarine（潜艇）〕

![l3-p11](fig/l3/mgp00011.png)

<span style="color:#2471a3;">**[example]**</span> 页面中央是一张 8×8 网格棋盘图：黑色底板，左侧标行号 A–H，上方标列号 1–8，每个格子画成蓝色方块、绿色描边，样式类似"海战棋"（battleship）的作战图。它对应"Submarine（潜艇）"问题：一艘潜艇藏在 64 个格子中的某一行某一列，提问者通过设计提问把它定位出来。〔本页为纯图示页〕

### p.12 〔The Bent Coin Lottery（不均匀硬币彩票）〕

![l3-p12](fig/l3/mgp00012.png)

<span style="color:#2471a3;">**[example]**</span> 题设与 p.7 完全相同（$p_1=0.1$ 的硬币投掷 $N=1000$ 次；结果为 $\mathbf{x}=x_1x_2\ldots x_N$；投币前可按每张 £1 买入 $2^N$ 张可能彩票中的任意一张；持有与结果一致的彩票 $\mathbf{x}$ 即赢得 £1,000,000,000）。右侧边栏同样是标注 $2^N$ 的完整彩票清单（`0000000000.....00000` 到 `1111111111.....11111`，中间以省略号略去）。本页把问题扩充为两问：

- **Q**：If you are forced to buy **one** ticket, which would you buy?（如果你被迫只买一张彩票，你会买哪一张？）
- **Q**：To have a **99%** chance of winning, at lowest possible cost, which tickets would you buy?（要想以 99% 的概率中奖，且总花费尽可能低，你会买哪些彩票？）
- • And how many tickets is that?（那样需要买多少张彩票？）
- Express your answer in the form $2^{(\cdots)}$.（请把答案写成 $2^{(\cdots)}$ 的形式。）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 两问的"最优"含义截然不同，值得对照体会。第一问被强制只买一张时，理性选择是概率最大的那张，即全 0 串 $000\ldots0$，其概率为 $0.9^{1000}\approx 10^{-46}$——"最优单张"依然近乎必输。这说明在指数级的假设空间里，单点最优微不足道，必须转向集合思维。第二问换成功率导向：让覆盖概率不小于 0.99 的彩票集合尽量小，最优策略是把全部 $2^N$ 张彩票按概率从大到小排序后买下最前面的一段前缀；由于序列概率只取决于 1 的个数，这段前缀恰好近似就是"1 的个数接近 100"的典型集，其大小约为 $2^{NH}\approx 2^{469}$。"小集合承载大概率质量"的现象与你在 Strang 线性代数中建立的高维几何直觉相通：高维球体的体积集中在半径附近薄薄一层球壳上，序列的概率质量也同样集中在典型集这个"薄壳"里。</span>

### p.13 〔Source coding theorem（信源编码定理）〕

![l3-p13](fig/l3/mgp00013.png)

<span style="color:#2471a3;">**[theorem]**</span> 本页单独完整展示 p.6 中的第 3 条论断：

3. **Source coding theorem（信源编码定理）**——来自信源 $X$ 的 $N$ 个结果可以被压缩（can be compressed）到大约 $NH(X)$ 比特。

下方给出证明思路（蓝字）：Proved by counting the typical set（通过"数典型集（typical set）的大小"来证明）。

页面底部绿色小字：Read chapter 4 to see the full proof and the general definition of typicality（阅读第 4 章，可看到完整证明以及 typicality（典型性）的一般定义）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** "通过统计典型集来证明"一句给出了信源编码定理的完整路线图。第一步，用大数定律说明 $N$ 长序列中 1 的频率趋于 $p_1$，这样的"典型序列"中每一条的概率都约为 $2^{-NH}$；第二步，既然总概率 1 几乎全部落在典型集上，典型集的大小就约为 $1/2^{-NH}=2^{NH}$；第三步，给典型集内每条序列发一个约 $\lceil NH\rceil$ 比特的索引即可完成压缩，非典型序列因极其罕见而可以牺牲。这套"概率质量集中于小子集"的论证方式，与 Strang 线性代数中高维空间的集中现象异曲同工：高维随机向量几乎总落在球壳薄层内，概率测度也集中于典型子空间附近的区域，二者都体现"高维下随机性高度集中"。第 4 章将给出典型性的一般定义并补全误差估计，届时你会发现今天彩票题里的每一笔账都是该定理证明的预演。</span>

### p.14 〔How to compress a redundant file, practically?（如何"实际地"压缩一个冗余文件？）〕

![l3-p14](fig/l3/mgp00014.png)

<span style="color:#2471a3;">**[section]**</span> 页面标题为 How to compress a redundant file,（如何压缩一个冗余文件，）标题之下用红色大字强调：**practically?（"实际上"怎么做？）**。页面主体再次出现与 p.3 相同的一整屏 0/1 二进制数字块（约 25 行 × 80 列，1 稀疏地散布在大量的 0 之间）。本页把前面"理论上能压到 $NH$ 比特"的论断转化为一个工程问题：需要给出实际可操作的压缩算法——为后续哈夫曼编码（Huffman coding）、算术编码（arithmetic coding）等符号码与流码（stream code）内容埋下伏笔。

### p.15 〔Project:（课程项目）〕

![l3-p15](fig/l3/mgp00015.png)

<span style="color:#2471a3;">**[note]**</span> 页面顶部一行小字：Project:（项目：）。任务描述：

- Invent a **compressor** and **uncompressor** for a source file of $N = 10{,}000$ bits, each having probability $f = 0.01$ of being a 1.（为一个 $N=10{,}000$ 比特的信源文件发明一个压缩器（compressor）与一个解压器（uncompressor），文件中每个比特取 1 的概率为 $f=0.01$。）
- Implement them and/or estimate how well your method works.（实现它们，并且/或者估计你的方法效果如何。）

页面底部两条补充：

- Also: exercises 5.22, 5.26, 5.27（另外：完成习题 5.22、5.26、5.27）
- Reading: Chapters 1-6（阅读：第 1–6 章）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这个项目让你亲手把定理变成代码。先算理论极限：$f=0.01$ 时单比特熵 $H_2(0.01)=-0.99\log_2 0.99-0.01\log_2 0.01\approx 0.0808$ 比特，故 $10{,}000$ 比特文件的总信息量约 808 比特，理想压缩器应把文件压到 810 比特上下（压缩率约 12 倍）；习题 5.22 起的几道题正是围绕这一场景展开，建议先做再动手写代码。实现层面你会大量用到 CSAPP 第 2 章的位级操作：把比特打包进机器字、用移位与掩码统计游程等；最朴素的游程编码（记录相邻两个 1 之间 0 的个数）已能显著缩短文件，而要逼近 808 比特极限则需要算术编码这类能逼近熵的流码。评估方法效果时，建议以"压缩后平均长度 ÷ 理论极限 $NH$"作为指标，并在多种随机种子下重复实验取平均，以消除个别极端序列带来的偏差。</span>
