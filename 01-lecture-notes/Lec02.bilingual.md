> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l2 · 行内双语视觉转录版 · 原图见 fig/l2/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l2-p1](fig/l2/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> **Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）**——课程封面页。右侧为课程全名大标题，页面底部标出课程网址 `www.inference.phy.cam.ac.uk/itprnn/`。左侧是一幅圆形图案：一个圆盘内部画着一棵递归分形树，主干与粗枝为绿色（节点有圆形、方形、菱形等形状），末梢细枝呈蓝色与品红色，逐层分叉并向圆盘边缘加密延伸。〔本页除标题与网址外为纯手绘图示〕

### p.2 〔The binary symmetric channel（二元对称信道）〕

![l2-p2](fig/l2/mgp00002.png)

<span style="color:#2471a3;">**[definition]**</span> **The binary symmetric channel（二元对称信道）**：页面中央是一张信道转移图——左端标红色输入 $x$，含两个输入节点 $0$ 与 $1$；右端标红色输出 $y$，含两个输出节点 $0$ 与 $1$。四条青色箭头：直箭头 $0 \to 0$ 与 $1 \to 1$ 各标绿色概率 $1-f$，交叉箭头 $0 \to 1$ 与 $1 \to 0$ 各标绿色概率 $f$。即输入比特以概率 $f$ 被翻转、以概率 $1-f$ 原样通过的最简噪声模型。

本页列出本讲要讨论的两个编码方案：

- Repetition codes（重复码）
- (7,4) Hamming code（(7,4) 汉明码）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 二元对称信道是整门课反复登场的"果蝇"，值得用你已有的知识把它拆开看。在 Bertsekas《概率导论》的框架里，一个信道无非是一张条件概率表：给定输入随机变量 $X$，输出随机变量 $Y$ 服从条件分布 $P(Y \mid X)$，而二元对称信道是其中最简单的特例——只有两个输入、两个输出，且翻转概率 $f$ 与输入取值无关（这种"与输入无关"的性质叫对称性，也正是名字里 symmetric 的由来）。再从 CSAPP 第 2 章的视角看，一个比特就是二进制表示的最小构件，该信道的噪声恰好可以写成位运算 $y = x \oplus e$，其中错误图样 $e$ 的每一位以概率 $f$ 取 1——异或正是模 2 的逐位加法。你以后会看到，围绕这个信道的一切编码与译码问题，本质上都是在回答"给定噪声信道的输出，如何反推最可能的输入"，这与贝叶斯推断里计算后验概率 $P(x \mid y)$ 完全同构。请把参数 $f$ 记牢，本讲后面演示汉明码表现时全靠它。

### p.3 〔（无标题页）通信系统框图：编码器—噪声信道—译码器〕

![l2-p3](fig/l2/mgp00003.png)

页面是一张框图：顶部青绿色字 **Source（信源）**，向下箭头（旁标红色 $s$）进入紫色方框 **Encoder（编码器）**；编码器输出红色 $t$，向右折入青绿色方框 **Noisy channel（噪声信道）**；信道输出红色 $r$，向上折入右侧紫色方框 **Decoder（译码器）**；译码器向上输出红色 $\hat{s}$（即信源的重构/估计）。框图下方左右各有一句点评：左边 **adds redundancy**（增加冗余，其中 redundancy 一词为绿色强调），右边 **does inference**（做推断，其中 inference 一词为灰蓝色强调）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页把通信系统的两半分工说得极简：编码器的职责是"加冗余"，译码器的职责是"做推断"。为什么冗余能对抗噪声？想想 CSAPP 里存储器的奇偶校验：多存的那 1 个校验位本身不携带任何"新信息"，它只是把原信息以另一种形式多复制了一份——这正是 redundancy 的含义，即码字长度超过表示信源信息所需的最短长度。而"译码=推断"这个提法要更激进：MacKay 想让你把译码器看成一台统计推断机器，它拿着接收到的 $r$，对每个候选信源序列 $s$ 计算后验概率 $P(s \mid r)$，挑最大者输出。你在 Bertsekas 概率课里学的贝叶斯公式 $P(s \mid r) \propto P(r \mid s)\,P(s)$ 就是它的引擎：似然 $P(r\mid s)$ 由信道模型（如上一页的翻转概率 $f$）给出，先验 $P(s)$ 刻画信源序列本身的规律。记住这对关键词——冗余与推断，它们贯穿整门课：数据压缩是把冗余去掉，信道纠错是把冗余加回来，一进一出正好构成闭环。

### p.4 〔Shannon's noisy channel coding theorem（Shannon 噪声信道编码定理）〕

![l2-p4](fig/l2/mgp00004.png)

<span style="color:#2471a3;">**[theorem]**</span> 页面左侧重画了 p.2 的二元对称信道转移图（左端 $x$ 的节点 $0/1$，右端 $y$ 的节点 $0/1$，直通箭头标 $1-f$，交叉箭头标 $f$）。右侧是一张 x-y 散点图：横轴标 **Rate（码率）**，从 0 到 1；纵轴为错误率，刻度 0 到 0.1（间隔 0.02）。图面散布大量十字形数据点（各种编码方案实测的"码率—错误率"表现），并有若干标注点：右上角 $R1$（码率约 1.0、错误率约 0.1）；$H(7,4)$（码率约 0.57、错误率约 0.06）；$R3$（码率约 0.28、错误率约 0.03）；$R5$（码率约 0.19、错误率约 0.02）。一条从横轴上 $C$（约 0.5 略右）出发、向右上延伸到 $R1$ 的曲线把图面分成两半：曲线左下方标 **achievable（可达）**，右上方标 **not achievable（不可达）**。

图下方结论文字：**For any channel: Reliable (virtually error-free) communication is possible at rates up to C.**（对任何信道：只要码率不超过 $C$，就可以实现几乎无差错的可靠通信。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张散点图是 Shannon 1948 年革命性论断的一页速写，也和你在 6.006/CLRS 学过的"信息论下界"血缘极近。回忆 CLRS 第 8 章：比较排序的决策树至多有 $n!$ 片叶子，每次比较至多提供 1 bit 的区分能力，故树高至少 $\log_2(n!) = \Omega(n\log n)$——那是"想做得比信息量允许的更快，必失败"的反向论证。Shannon 定理是同一枚硬币的另一面：$C$（信道容量，后面几讲会给出解析式）刻画了信道每次使用至多能可靠传输的信息量；码率低于 $C$ 时，用足够长的分组码可以把错误率压到任意小，高于 $C$ 则原则上必然失败。图中那条 achievable / not achievable 的分界线，正是这一下界的图形化表达。图上从 $R5$、$R3$ 一路排到 $H(7,4)$、$R1$ 的那些点，是"码率越高、错误率越高"的实测证据，而 Shannon 告诉你：靠更聪明的编码，可以贴着 $C$ 那条线走而几乎不出错。

### p.5 〔Homework（课后作业）〕

![l2-p5](fig/l2/mgp00005.png)

页面右上角标注 **(Exercise 1.9, page 14)（练习 1.9，第 14 页）**。主体作业题（蓝红两色书写）：

Design an error-correcting code for the binary symmetric channel（为二元对称信道设计一个纠错码），or another noisy channel, you choose（或者选一个你自己挑的噪声信道）；invent a decoding algorithm for it, and estimate its probability of error.（为它发明一个译码算法，并估计其错误概率。）Be creative!（发挥创意！）

下面一行绿色小字：**Other recommended exercises: 1.3, 1.5-7, 1.11; Reading: Chapters 1, 2, 4.**（其他推荐练习：1.3、1.5–7、1.11；阅读：第 1、2、4 章。）

右下角重画了 p.2 的二元对称信道转移图（左端 $x$ 节点 $0/1$、右端 $y$ 节点 $0/1$，直通箭头标 $1-f$，交叉箭头标 $f$）。

### p.6 〔（无标题页）被打码的文本：《Emma》开篇〕

![l2-p6](fig/l2/mgp00006.png)

整页是一大块打字机字体的英文文本（浅黄色底）：内容为 Jane Austen 小说《Emma》的开篇段落，其中大量字母被替换成星号 `*`（模拟"字符经噪声信道后丢失"的输出）。按图逐行转录如下（星号位置忠实于图）：

```
Emma Woodh*use, hands*me, clever* and rich,*with a
comfortab*e home an* happy di*position,*seemed to*unite som*
of the b*st bless*ngs of e*istence;*and had *ived nea*ly
twenty *ne year* in the*world w*th very*little *o distr*ss
or vex*her.   *he was*the yo*ngest  *f the *wo dau*hters  *f a
most *ffect*onate*  indu*gent  *ather*  and  *ad,  i*  cons*quenc*
of h*r si*ter'* mar*iage*  bee*  mis*ress*of h*s ho*se f*om a
ver*  ea*ly  *eri*d.  *er  *oth*r  h*d  d*ed  *oo  *ong*ago*for*her
to*ha*e *or* t*an*an*in*is*in*t *em*mb*an*e *f *er*ca*es*es*
a*d*h*r*p*a*e*h*d*b*e*  *u*p*i*d*b*  *n*e*c*l*e*t*w*m*n*a*
g**e**e**,*h**h**  **l**n**i**l**s**r**o**a**o**e**i*
a***c**n**S**e***y***s**d**s**a**r**e***n**
W***o***s***i***l***a***g***n***t***a***e***v***
```

其完整原文与中文翻译见下一页（p.7）。

### p.7 〔（无标题页）《Emma》片段：完整原文与打码版对照〕

![l2-p7](fig/l2/mgp00007.png)

页面为上下两块同一段文字的对照版。**上块是完整原文**（Jane Austen《Emma》第一章开头），逐句行内双语转录：

> Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition, seemed to unite some of the best blessings of existence; and had lived nearly twenty one years in the world with very little to distress or vex her.（爱玛·伍德豪斯又漂亮、又聪明、又有钱，家境舒适、性情开朗，似乎集人间最好的福气于一身；她在世上过了将近二十一年，几乎没什么事让她痛苦或烦恼。）
>
> She was the youngest of the two daughters of a most affectionate, indulgent father; and had, in consequence of her sister's marriage, been mistress of his house from a very early period.（她是两姐妹中的小女儿，父亲极其慈爱、百般纵容；也正因姐姐出了嫁，她年纪轻轻便当家做了女主人。）
>
> Her mother had died too long ago for her to have more than an indistinct remembrance of her caresses; and her place had been supplied by an excellent woman as governess, who had fallen little short of a mother in affection.（母亲去世太久，她对母亲的抚爱只剩一点模糊的记忆；母亲的位置由一位极出色的家庭女教师补上，她的疼爱几乎不亚于生母。）
>
> Sixteen years had Miss Taylor been in Mr Woodhouse's family, less as a governess than a friend, very（泰勒小姐在伍德豪斯先生家已经待了十六年，与其说是家庭女教师，不如说更像一位朋友，非常……〔原文在此页被截断〕）

**下块是打码版**，与上一页（p.6）逐行转录的星号文本完全相同，不再重复；两相对照可见：约一半字母被抹去后，句子仍然可读——这正是本例要演示的现象。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这两页是 MacKay 的招牌开场实验：把一段英文随机抹掉约一半字符，你几乎仍能毫不费力地读出全文。为什么？因为自然语言充满冗余——印刷英文每字符的真实信息量只有约 1 bit 的量级（Shannon 1951 年用逐字预测实验给出的著名估计），远小于其 ASCII 表示的 8 bit/字符；用 CSAPP 第 2 章的语言说，这是"表示位数远大于信息量"的典型浪费。被抹掉的字符大都能由上下文唯一恢复，说明它们在给定上下文时的条件信息量接近零。更有趣的是，此刻正在"译码"的你，扮演的正是 p.3 框图里的译码器：先验是你对英语词汇与语法的知识，似然由残存字母提供，你的大脑在做一次不自觉的贝叶斯推断——补全的是后验最可能的字母序列。MacKay 借此说明：人类语言解码与信道译码是同一个数学问题的两个化身，这也为整门课"推断无处不在"的主题定了调。

### p.8 〔（无标题页）两级通信系统框图：压缩/解压 + 编码/译码〕

![l2-p8](fig/l2/mgp00008.png)

页面是一张四级框图，数据流自上而下：顶部青绿色 **Source（信源）** 向下进入绿色方框 **Compressor（压缩器）**，输出红色 $s$ 进入紫色方框 **Encoder（编码器）**，输出红色 $t$ 进入中下方青绿色方框 **Noisy channel（噪声信道）**，输出红色 $r$ 进入右侧紫色方框 **Decoder（译码器）**，输出红色 $\hat{s}$ 向上进入绿色方框 **Decompressor（解压器）**，最终向上输出。左侧有两行大写标注：**CHANNEL CODING**（信道编码，位于 Compressor/Decompressor 一行的左侧）、**SOURCE CODING**（信源编码，位于 Encoder/Decoder 一行的左侧）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 先给一个阅读警告：按图中位置，CHANNEL CODING 标在 Compressor/Decompressor 一行旁、SOURCE CODING 标在 Encoder/Decoder 一行旁，这与两个模块的实际功能恰好相反——Compressor/Decompressor 做的是信源编码（把信源 $s$ 压到信息论极限，即"去冗余"），Encoder/Decoder 做的才是信道编码（给压缩后的比特加冗余以抗噪）；MacKay 教材第 1 章的系统图（图 1.5）正是按功能这样标注的。因此阅读本页请以框图结构与数据流 $s \to t \to r \to \hat{s}$ 为准。这张两级瀑布图是全书总纲：上层（信源编码）解决"表示效率"，回答"最少需要多少比特"；下层（信道编码）解决"传输可靠"，回答"噪声之下如何保真"。注意其中漂亮的对偶：压缩器千方百计让序列"看起来随机"（逼近熵最大），信道编码器却又故意往近乎随机的比特里注入精心设计的冗余——一去一加方向相反，背后却是同一套信息论数学。

### p.9 〔A simple redundant source - a bent coin（一个简单冗余信源——弯硬币）〕

![l2-p9](fig/l2/mgp00009.png)

<span style="color:#2471a3;">**[example]**</span> 整页为一大块打字机字体的 0/1 位串（约 28 行、每行约 70 字符），其中 1 十分稀疏（约占十分之一）、0 占绝对多数，直观呈现一个高度冗余的二进信源；页面底部以蓝色标出参数：$p_1 = 0.1$（输出 1 的概率为 0.1）。〔本页主体为数据图示，位串不逐位转录〕

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "弯硬币"（bent coin，指正反不等概的硬币）是 MacKay 全书最钟爱的教具。在概率论的语言里，它的每一位都是伯努利试验：独立地以 $p_1=0.1$ 取 1、以 $0.9$ 取 0。每位输出的熵为 $H_2(0.1) = -0.1\log_2 0.1 - 0.9\log_2 0.9 \approx 0.469$ bit——注意这里"熵是自信息 $-\log p$ 的期望"，正是 Bertsekas 概率论中"随机变量之函数取期望"的直接应用。$0.469 < 1$ 说明每位平均携带的信息远不足 1 bit，所以图上这片"几乎全是 0"的位串天然冗余、可压缩。更深刻的是大数定律的推论——渐近均分性（AEP）：当位数 $N$ 很大时，几乎所有高概率序列都落在"1 的个数约为 $Np_1$"的典型集里，其大小约为 $2^{NH}$。这很像 Strang 线代中"高维空间里质量集中在低维子空间附近"的投影直觉：$2^N$ 个顶点的超立方体中，概率质量其实蜷缩在维数仅约 $2^{NH}$ 的"典型子空间"里。下一页的问题就是要利用这一点。

### p.10 〔How to compress a redundant file?（如何压缩一个冗余文件？）〕

![l2-p10](fig/l2/mgp00010.png)

页面同样是一大块 0/1 位串（与 p.9 同为弯硬币输出样式：1 稀疏、0 密集，约 28 行、每行约 70 字符），底部以红色标注数据来源：**e.g., $N$ tosses of a bent coin with $p_1 = 0.1$**（例如：一枚 $p_1=0.1$ 的弯硬币掷 $N$ 次的输出）。页标题即本页提出的问题：**How to compress a redundant file?**（如何压缩一个冗余文件？）

### p.11 〔The weighing problem（称重问题）〕

![l2-p11](fig/l2/mgp00011.png)

页面上半是一幅红色简笔画：一架带梯形底座的天平明显向右倾斜，左右两盘各放 2 只青绿色圆球，天平左侧地面上还堆着另外 8 只球（合计 12 只）。下半是题目正文：

You are given 12 balls, all equal in weight except for one that is either heavier or lighter.（给你 12 只球，它们全部等重，只有一只例外——它要么偏重、要么偏轻。）

Design a strategy to determine which is the odd ball（设计一套策略，判定哪一只是坏球）and whether it is heavier or lighter,（以及它究竟是偏重还是偏轻，）in as few uses of the balance as possible.（并且所用天平次数要尽可能少。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 称球问题是决策树/信息论下界论证的又一块试金石，与 CLRS 第 8 章的比较排序下界、6.006 的决策树模型一脉相承。先把"假设空间"数清楚：坏球可能是 12 只中的任何一只，且各有"偏重/偏轻"两种可能，共 $12 \times 2 = 24$ 个假设（注意"3 号球偏重"与"3 号球偏轻"是两个不同假设）。每次称重只有三种结果：左重、右重、平衡——所以一次称重至多提供 $\log_2 3 \approx 1.585$ bit 的信息，$k$ 次称重的决策树至多 $3^k$ 片叶子。要区分 24 个假设，必须 $3^k \ge 24$，即 $k \ge \lceil \log_3 24 \rceil = 3$：三次是信息论下界。经典结论是三次确实可达，但策略要精心设计（第一次称 4 对 4，才能让每个分支的剩余假设数都压进 $3^2 = 9$ 以内）。这个"实验结果数 ≥ 假设数"的计数论证，与"叶子 $n!$ 个、比较 $\log_2 n!$ 次"的比较排序下界是同一个数学骨架：单次实验的信息量有上限，能区分的假设总数就有上限。

### p.12 〔The weighing problem（称重问题）〕

![l2-p12](fig/l2/mgp00012.png)

本页重复 p.11 的红色天平简笔画（两盘各 2 只球、旁边地面 8 只球），其下仅列出一条主题：

- The Bent Coin Lottery（弯硬币彩票）

### p.13 〔The Bent Coin Lottery（弯硬币彩票）〕

![l2-p13](fig/l2/mgp00013.png)

<span style="color:#2471a3;">**[example]**</span> 左栏题目：

A coin with $p_1 = 0.1$ will be tossed $N = 1000$ times.（一枚 $p_1=0.1$ 的硬币将被掷 $N=1000$ 次。）

The outcome is $\mathbf{x} = x_1x_2\ldots x_N$.（结果记为 $\mathbf{x} = x_1x_2\ldots x_N$。）

e.g., $\mathbf{x}$ = 000001001000100…00010（例如 $\mathbf{x}$ = 000001001000100…00010）

You can buy any of the $2^N$ possible tickets for £1 each, before the coin-tossing.（掷币开始前，你可以每张 £1 的价格购买 $2^N$ 种可能彩票中的任意若干张。）

If you own ticket $\mathbf{x}$, you win £1,000,000,000.（若你持有的票与最终结果 $\mathbf{x}$ 完全一致，即赢得 £1,000,000,000。）

Q　To have a 99% chance of winning, at lowest possible cost, which tickets would you buy?（问：想以 99% 的概率中奖、且花费尽可能低，你会买哪些票？）

•　And how many tickets is that?（那总共是多少张？）

Express your answer in the form $2^{(\cdots)}$.（请把答案表示成 $2^{(\cdots)}$ 的形式。）

页面底部绿色小字：Please think about this question before lecture 3（请在第 3 讲之前思考这个问题）。

右栏是一个标题为 **Lottery tickets available（可供购买的彩票）** 的列表框：左侧大括号（旁标 $2^N$）括起全部 $2^N$ 张票，按字典序从上到下列出——开头为 `0000000000....00000`、`0000000000....00001`、`0000000000....00010`、`0000000000....00011`、`0000000000....00100`、`0000000000....00101`、`0000000000....00110`、`0000000000....00111`，中部竖排省略号后出现 `0010000001....01000`，再经省略号直到末尾 `1111111111....11101`、`1111111111....11110`、`1111111111....11111`。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 彩票问题是渐近均分性的"付费验证版"。朴素策略是把 $2^{1000}$ 张票全部买下，花费 £$2^{1000}$——彻底的天文数字；聪明的策略则利用"概率质量高度集中"：由大数定律（Bertsekas 概率论中独立同分布情形的标准结论），$p_1=0.1$、$N=1000$ 时几乎所有概率质量都集中在"1 的个数约 100"的典型集附近，偏离太远的序列概率指数级趋零。于是只需买下典型集中概率最大的那些序列所对应的票，把它们覆盖的总概率凑到 0.99，花费量级约为 $2^{N H_2(0.1)} = 2^{469}$（题目要求把答案写成 $2^{(\cdots)}$ 形式，第 3 讲会给出精确推导）。对比 £$2^{1000}$ 与 £$2^{469}$：两者相差 $2^{531}$ 倍，这就是"冗余"在价格上的直观标度。本题还预演了信源编码定理的证明思路——只需对典型集编码，平均码长即可逼近 $NH$；换成 Strang 线代的语言，你要覆盖的那个"典型子空间"维数只有约 $2^{NH}$，而非整个 $2^N$ 维空间。

### p.14 〔Course outline（课程大纲）〕

![l2-p14](fig/l2/mgp00014.png)

- **Information Theory（信息论）**
  - Source coding (Data compression)（信源编码（数据压缩））
  - Noisy-channel coding（噪声信道编码）
- **Data modelling, pattern recognition, learning & memory（数据建模、模式识别、学习与记忆）**
  - Tools（工具）
    - Exact inference methods（精确推断方法）
    - Monte Carlo methods（蒙特卡洛方法）
    - Variational methods（变分方法）
  - Neural networks（神经网络）
