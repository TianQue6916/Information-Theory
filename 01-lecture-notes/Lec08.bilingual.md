> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l8 · 行内双语视觉转录版 · 原图见 fig/l8/</span>

<span style="color:#2471a3;">**[lecture]**</span> 本讲主题：噪声信道编码定理（The noisy-channel coding theorem）——信道容量（channel capacity，信道容量）的定义、若干信道的容量计算、以及 Shannon 证明思路的路线图。

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l8-p1](fig/l8/mgp00001.png)

本页为课程大纲标题页。左侧为一张圆形分形网络装饰图：绿色节点（圆形、方形、三角形、星形）由绿色连线组成层级网络，边缘缀有蓝、红、粉色小节点，自中心向外递归展开〔图示为装饰性图形〕。右侧主标题：Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）。

<span style="color:#2471a3;">**[section]**</span> 课程大纲（绿色大圆点为分组条目，橙色圆点为子条目）：

- **1** Noisy-channel coding（噪声信道编码）
- <span style="color:#00838f;">**Source coding (Data compression)**（信源编码（数据压缩））</span>
  - **2** Information content, entropy（信息量、熵）
  - **3** Typicality and the source coding theorem（典型性与信源编码定理）
  - **4** Symbol codes（符号码）
  - **5** Symbol codes and Arithmetic coding（符号码与算术编码）
- <span style="color:#00838f;">**Noisy-channel coding**（噪声信道编码）</span>
  - **6** Inference and Information measures for noisy channels（噪声信道上的推断与信息度量）
  - **7** Capacity of a noisy channel（噪声信道的容量）
  - **8** The noisy-channel coding theorem（噪声信道编码定理）

> <span style="color:#7f8c8d;">旁注：本讲对应大纲第 8 条「噪声信道编码定理」，并顺带回顾第 6、7 条中的信息度量与容量。</span>

### p.2 〔Definition of Capacity（容量的定义）〕

![l8-p2](fig/l8/mgp00002.png)

<span style="color:#2471a3;">**[definition]**</span> 信道（channel，信道）的容量（Capacity，容量）定义为：在所有输入分布 $P(x)$ 上，互信息（mutual information，互信息）的最大值：

```math
C \equiv \max_{\mathcal{P}_X} I(X;Y)
```

达到该最大值的分布 $\mathcal{P}^*_X$ 称为最优输入分布（optimal input distribution，最优输入分布）。

<span style="color:#2471a3;">**[theorem]**</span> Shannon 噪声信道编码定理（Shannon's noisy channel coding theorem）：

**可靠（几乎无差错）的通信在码率高达 C 时是可能的**（Reliable (virtually error-free) communication is possible at rates up to C）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这条定义值得从你已有的概率论视角拆开看：互信息 $I(X;Y)$ 本身是一个期望值——$I(X;Y)=\mathbb{E}\big[\log\frac{P(x,y)}{P(x)P(y)}\big]$，即"对数似然比"这个随机变量在联合分布下的期望，这与 Bertsekas 概率论中"熵＝随机变量的函数的期望"的处理完全一致。信道（即条件分布 $Q(y|x)$）是环境给定的、不可控的，唯一可调的是输入分布，所以 $C$ 的计算本质上是一个约束优化问题：在概率单纯形 $\sum_x P(x)=1,\ P(x)\ge 0$ 上最大化 $I(X;Y)$。对固定信道而言 $I(X;Y)$ 是输入分布的凹函数，其非负性可由 KL 散度非负保证——而 KL 非负又可由凸性/Jensen 不等式推出，正是你在 Strang 线代之后接触凸优化时"凹目标＋凸约束⇒极值好刻划"的套路。Shannon 定理进而断言：这个优化出来的数值 $C$ 恰好是可靠通信码率的分水岭——低于它万事大吉，高于它必然出错。</span>

### p.3 〔Ternary confusion channel（三进制混淆信道）〕

![l8-p3](fig/l8/mgp00003.png)

<span style="color:#2471a3;">**[example]**</span> 三进制混淆信道（ternary confusion channel，三进制混淆信道）图示：输入 $x\in\{a,b,c\}$，输出 $y\in\{M,N\}$；转移箭头为 $a\xrightarrow{1}M$、$b\xrightarrow{1/2}M$、$b\xrightarrow{1/2}N$、$c\xrightarrow{1}N$。右侧信道矩阵：

```math
\mathbf{Q} = \begin{bmatrix} 1 & 1/2 & 0 \\ 0 & 1/2 & 1 \end{bmatrix}
```

（两行对应输出 $M,N$，三列对应输入 $a,b,c$，按图中数字排列转录。）

假设输入分布 $\mathcal{P}_X = \left\{\frac13, \frac13, \frac13\right\}$（Assume input distribution）。

- 若 $y = M$，那么 $x$ 是什么？（If $y=M$, what's $x$?）
- 互信息 $I(X;Y)$ 是多少？（What is the mutual information $I(X;Y)$?）

### p.4 〔Ternary confusion channel（三进制混淆信道）〕

![l8-p4](fig/l8/mgp00004.png)

（本页与 p.3 同图：三进制混淆信道图示、信道矩阵 $\mathbf{Q}=\begin{bmatrix} 1 & 1/2 & 0 \\ 0 & 1/2 & 1 \end{bmatrix}$ 与假设的输入分布 $\mathcal{P}_X = \left\{\frac13,\frac13,\frac13\right\}$ 均与上一页相同。）本页仅保留第一个提问：

- 若 $y = M$，那么 $x$ 是什么？（If $y=M$, what's $x$?）

### p.5 〔Ternary confusion channel II（三进制混淆信道 II）〕

![l8-p5](fig/l8/mgp00005.png)

（图示、信道矩阵 $\mathbf{Q}=\begin{bmatrix} 1 & 1/2 & 0 \\ 0 & 1/2 & 1 \end{bmatrix}$ 与输入分布 $\mathcal{P}_X=\left\{\frac13,\frac13,\frac13\right\}$ 均同 p.3。）本页提问：

- 互信息 $I(X;Y)$ 是多少？（What is the mutual information $I(X;Y)$?）

### p.6 〔Ternary confusion channel III（三进制混淆信道 III）〕

![l8-p6](fig/l8/mgp00006.png)

（图示与信道矩阵同 p.3。）本页提问：

- 最优输入分布 $\mathcal{P}^*_X$ 是什么？（What is the optimal input distribution $\mathcal{P}^*_X$?）
- 容量是多少？（What is the capacity?）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 我们可以亲手把这三问算出来，正好练一遍互信息的链式法则。先看 $y=M$：由全概率公式 $P(M)=\frac13\cdot 1+\frac13\cdot\frac12=\frac12$，于是后验 $P(a|M)=\frac{1/3}{1/2}=\frac23$、$P(b|M)=\frac13$——你无法唯一确定 $x$，只能说"三分之二是 $a$"，这正是"混淆"一词的含义，与哈希表中两个键碰撞进同一桶的情形同构。互信息用 $I(X;Y)=H(Y)-H(Y|X)$ 最顺手：$H(Y)=1$ 比特，而 $H(Y|X)=\frac13(0+1+0)=\frac13$ 比特，故 $I=\frac23$ 比特。至于容量：由对称性设 $P(a)=P(c)=q$、$P(b)=1-2q$，可验证 $P(M)=\frac12$ 与输入无关，于是 $I=2q$ 在 $q\to\frac12$（即 $P(b)\to 0$）时趋于 1 比特。最优策略竟是"干脆不用会混淆的中间输入 $b$"——这个"绕开坏输入"的直觉将在噪声打字机一例中大放异彩。</span>

### p.7 〔Noisy typewriter（噪声打字机信道）〕

![l8-p7](fig/l8/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 噪声打字机信道（noisy typewriter，噪声打字机信道）图示：左列为 27 个输入字符 A、B、C、D、E、F、G、H、⋯、Y、Z、−，右列为相同的 27 个输出字符；每个输入字符以各 1/3 的概率转移到自身或左右相邻字符（箭头在图中交叉成网状；字符 G 的三条出边在图上加粗；末尾 − 与开头 A 循环相邻；图中部以竖排省略号 ⋮ 省略中间字符）。右侧以 G 为例写出条件概率：

```math
P(y{=}\mathrm{F}\,|\,x{=}\mathrm{G}) = 1/3;\quad
P(y{=}\mathrm{G}\,|\,x{=}\mathrm{G}) = 1/3;\quad
P(y{=}\mathrm{H}\,|\,x{=}\mathrm{G}) = 1/3;
```

- 最优输入分布是什么？（What is the optimal input distribution?）
- 容量是多少？（What is the capacity?）

### p.8 〔Non-confusable subset of inputs（输入的非混淆子集）〕

![l8-p8](fig/l8/mgp00008.png)

（承接噪声打字机信道：从输入字母表中每隔 3 个取一个字符，构成非混淆子集 $\{\mathrm{B}, \mathrm{E}, \mathrm{H}, \ldots, \mathrm{Z}\}$。图示它们的输出集合互不重叠：$\mathrm{B}\to\{\mathrm{A},\mathrm{B},\mathrm{C}\}$、$\mathrm{E}\to\{\mathrm{D},\mathrm{E},\mathrm{F}\}$、$\mathrm{H}\to\{\mathrm{G},\mathrm{H},\mathrm{I}\}$、⋯（图中部以竖排省略号 ⋮ 表示省略）、$\mathrm{Z}\to\{\mathrm{Y},\mathrm{Z},-\}$。）

**在这个非混淆子集上，可靠通信是可能的：$C = \log 9$ 比特**（reliable communication **is** possible at **C = log 9 bits**，图中"is"与"C = log 9 bits"标红强调）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这页的做法叫"收缩输入字母表"：27 个字符里每隔 3 个取 1 个，得到 9 个两两输出不重叠的输入，每个字符可靠传输 $\log_2 9\approx 3.17$ 比特。为什么恰好隔 3 取 1？因为每个输入的"输出云"是宽 3 的区间（自身加左右邻居），跨度 3 的取样保证任意两朵云不相交——这与 6.006 哈希表里用间隔放置来避免冲突是同一个布局思想，"混淆"即"冲突"。更有趣的是可以证明：这个朴素子集恰好达到该信道的容量（对称信道的最优输入分布可取均匀分布，而这里等效于在一个 9 元无噪信道上均匀发送），所以 $\log_2 9$ 既是下界也是上界。它与比较排序下界 $\Omega(n\log n)$ 的信息论论证遥相呼应：那里是"每次比较至多消除 1 比特不确定性"，这里是"每个符号至多携带 $\log_2(\text{非混淆输入数})$ 比特"。MacKay 书第 9 章对一般对称信道有完整论证，值得回头看。</span>

### p.9 〔Shannon's noisy channel coding theorem（Shannon 噪声信道编码定理）〕

![l8-p9](fig/l8/mgp00009.png)

<span style="color:#2471a3;">**[theorem]**</span> 左侧为二元对称信道（binary symmetric channel，BSC）图示：输入 $x\in\{0,1\}$，输出 $y\in\{0,1\}$；转移为 $0\xrightarrow{1-f}0$、$0\xrightarrow{f}1$、$1\xrightarrow{f}0$、$1\xrightarrow{1-f}1$。右侧为一张 x-y 散点图：横轴 Rate（码率，0 到 1），纵轴（块错误概率，0 到 0.1）；图中散布许多以 $+$ 号表示的数据点；标注有 R1（码率≈1、错误率≈0.1 处）、H(7,4)（方块点，码率≈0.57、错误率≈0.065 处）、R3（码率≈0.3、错误率≈0.03 处）、R5（码率≈0.2、错误率≈0.01 处）；一条实曲线从横轴上一点 C（约 0.53）向右上方弯升至 R1 点；曲线右侧区域标注 not achievable（不可达），左侧区域标注 achievable（可达）。

**对任何信道：可靠（几乎无差错）的通信在码率高达 C 时是可能的。**（For any channel: Reliable (virtually error-free) communication is possible at rates up to **C**。）

### p.10 〔(7,4) Hamming Code（(7,4) 汉明码）〕

![l8-p10](fig/l8/mgp00010.png)

<span style="color:#2471a3;">**[example]**</span> (7,4) 汉明码（Hamming code，汉明码）的校验矩阵 $\mathbf{H}$：

```math
\mathbf{H} = \begin{bmatrix}
1&1&1&0&1&0&0\\
0&1&1&1&0&1&0\\
1&0&1&1&0&0&1
\end{bmatrix}
```

图中以红色箭头标注矩阵尺寸：右侧 $\updownarrow\ M=3$（3 行），下方 $\leftrightarrow\ N=7$（7 列）。

有效传输（valid transmissions）$\mathbf{t}$ 满足：

```math
\mathbf{H}\,\mathbf{t} = \begin{bmatrix}0\\0\\0\end{bmatrix}\ \mathrm{mod}\ 2
```

### p.11 〔(7,4) Hamming Code（(7,4) 汉明码）〕

![l8-p11](fig/l8/mgp00011.png)

（本页重绘同一校验矩阵 $\mathbf{H}$ 与尺寸标注 $M=3$、$N=7$，以及条件 $\mathbf{Ht}=\begin{bmatrix}0\\0\\0\end{bmatrix}\ \mathrm{mod}\ 2$，均同上一页。）另新增三行：

- 接收信号（received signal）：$\mathbf{r} = \mathbf{t} + \mathbf{n}$
- 校验子（syndrome，又译伴随式）：$\mathbf{z} = \mathbf{Hr} = \mathbf{Hn}$
- 校验子译码器（syndrome decoder，校验子译码器）：$\mathbf{z} \longrightarrow \hat{\mathbf{n}}$

> <span style="color:#1e8449;">**[note] Note（译者注）:** 用你熟悉的线代＋位运算语言看，汉明码毫无神秘之处。$\mathbf{Ht}=\mathbf{0}\ (\mathrm{mod}\ 2)$ 说的是：全部 $2^7=128$ 个 7 比特向量中，只有 $\mathbf{H}$ 的零空间（kernel）里的 $2^{7-3}=16$ 个才是合法码字——$7$ 列减去秩 $3$，正是 Strang 线代里秩—零化度定理在 $\mathrm{GF}(2)$ 上的版本。接收端 $\mathbf{z}=\mathbf{Hr}=\mathbf{Hn}$ 成立，是因为 $\mathbf{Ht}=\mathbf{0}$ 把码字部分"抵消"掉了，校验子只反映噪声。对 (7,4) 码，$\mathbf{H}$ 的 7 个列向量恰好取遍所有非零 3 比特向量，因此 7 种单比特错误各对应唯一一个非零校验子，译码就是查表 $\mathbf{z}\to\hat{\mathbf{n}}$；而 $2^3=8\ge 7+1$ 也正是 $M=3$、$N=7$ 的来历。这与你在 CSAPP 学的奇偶校验一脉相承：奇偶位就是 $M=1$ 的特例，只能"发现"错误却不能"定位"；多加两行校验，就把定位能力买了回来。$\mathrm{mod}\ 2$ 加法就是异或（XOR）位运算。</span>

### p.12 〔How we won the bent coin lottery（我们如何赢得弯曲硬币彩票）〕

![l8-p12](fig/l8/mgp00012.png)

<span style="color:#2471a3;">**[example]**</span> 右上角标注：Probability of '1' = f（字符 '1' 出现的概率为 $f$）。

正文：为了有 99.99% 的胜算，我们买下了所有 typical（典型）的彩票。（To have a 99.99% chance of winning, we bought all the typical tickets.）

配图为手绘图示：一个红色轮廓的袋子，袋内散乱堆放许多青色细长条（彩票），其中几张深蓝色票被高亮举起，票面画有一排小黑点（示意多次抛掷硬币得到的结果序列）〔本页配图为手绘图示〕。

### p.13 〔How we won the bent coin lottery（我们如何赢得弯曲硬币彩票）〕

![l8-p13](fig/l8/mgp00013.png)

（文字与袋图同上一页：为了有 99.99% 的胜算，买下所有 typical（典型）彩票。）本页新增手写批注（蓝、绿两色手写字，黑色箭头指向袋中高亮的蓝票）：

- Number of tickets in 'typical set'（"典型集（typical set，典型集）"中的彩票张数）：

```math
|T| \simeq 2^{N H_2(f)}
```

（其中 $H_2(f)$ 为二元熵函数；图中手写作 $\mathrm{H}_2(f)$，其右上角还有一个小加号标记。）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 手写的 $|T|\simeq 2^{NH_2(f)}$ 就是渐近均分性（AEP）的定量面孔。回忆大数定律：抛 $N$ 次正面概率为 $f$ 的弯曲硬币，"1"的个数以趋于 1 的概率落在 $Nf$ 附近；而含恰好约 $Nf$ 个 1 的序列共有 $\binom{N}{Nf}\simeq 2^{NH_2(f)}$ 个（用 Stirling 公式估计二项式系数即得）。每个典型序列的概率都约为 $2^{-NH_2(f)}$，所以"典型集"的总概率趋于 1——这正是"买下所有典型票"就能以 99.99% 概率中奖的原因：省下的钱全都省在那些几乎不会开出的"非典型票"上。这与信源编码定理是同一枚硬币的两面：既然典型序列只有 $2^{NH}$ 个，给它们逐一编号平均只需 $NH$ 比特，熵便从"平均信息量"变成了"可实际达到的压缩率"。99.99% 这个数字对应允许的失败概率 $\epsilon$；$N$ 越大，典型集的边界越锐利。</span>

### p.14 〔How to prove good codes exist（如何证明好码存在）〕

![l8-p14](fig/l8/mgp00014.png)

<span style="color:#2471a3;">**[section]**</span> 证明好码存在的两条路线：

- **构造性证明（constructive proof）**：给定所需码率 $R<C$ 与 $\epsilon>0$（Given required $R<C$, and $\epsilon>0$），取一个（伪）随机校验矩阵 $\mathbf{H}$——图中画出其开头三行（绿色 0/1 数字）：

```math
\begin{bmatrix}
1&1&1&0&0&1&0\\
0&1&1&1&0&0&1\\
1&0&1&1&1&0&0
\end{bmatrix}
```

矩阵右侧与下侧以省略号 $\cdots$、$\vdots$ 及斜向省略号示意其向右、向下延展（行数与列数随 $N$ 增大）。

- **非构造性证明（non-constructive proof）**（本页仅列出条目标题，展开见后续各页）。

### p.15 〔Shannon's way of proving malnutrition（Shannon 的"营养不良"证明法）〕

![l8-p15](fig/l8/mgp00015.png)

<span style="color:#2471a3;">**[example]**</span> 配图为手绘卡通：一大群圆滚滚的卡通婴儿挤坐在一台带表盘的磅秤上〔本页为纯手绘图示〕。图下文字：

如果所有婴儿的 average（平均）体重 $<\epsilon$，（If **average** weight of all babies is $<\epsilon$,）

那么必定（至少！）有 one（一个）婴儿体重 $<\epsilon$。（there must be **(at least!) one** baby with weight $<\epsilon$.）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这页漫画讲的是整个证明里最锋利的一步——"平均论证"，它在离散数学里的名字是鸽笼原理（pigeonhole principle）的加权版：若 $\frac1n\sum_i w_i<\epsilon$，则必有某个 $w_i<\epsilon$（否则所有 $w_i\ge\epsilon$ 会把平均值顶上去）。Shannon 的用法是：把"婴儿"换成"随机选出的码"，把"体重"换成"该码在信道上的错误概率"。先证明对随机码求平均，错误概率小于 $\epsilon$，再由平均论证断言"至少存在一个具体的好码"。这类手法在组合数学里叫概率方法（Erdős 的成名利器），特点是证明不给出场地图纸——你知道好码存在，却不知道是哪一个，所以上一页才并列了"构造性/非构造性"两条路线。非构造性存在性曾被工程界抱怨了几十年，直到 20 世纪 90 年代 LDPC 码与 turbo 码出现，人们才真正造出能逼近 $C$ 且可译码的具体码——"存在"终于落了地。</span>

### p.16 〔Capacity（容量）〕

![l8-p16](fig/l8/mgp00016.png)

<span style="color:#2471a3;">**[definition]**</span>（本页为 p.2 的定义与定理回顾版，正文相同：）信道的容量（Capacity of a channel）是在所有输入分布 $P(x)$ 上取最大值得到的互信息：

```math
C \equiv \max_{\mathcal{P}_X} I(X;Y)
```

达到该最大值的分布 $\mathcal{P}^*_X$ 称为最优输入分布（optimal input distribution）。

<span style="color:#2471a3;">**[theorem]**</span> Shannon 噪声信道编码定理：可靠（几乎无差错）的通信在码率高达 C 时是可能的。（Reliable (virtually error-free) communication is possible at rates up to C.）

右侧配图：上方重绘二元对称信道图示（$0\xrightarrow{1-f}0$、$0\xrightarrow{f}1$、$1\xrightarrow{f}0$、$1\xrightarrow{1-f}1$），下方重绘噪声打字机信道图示（27 个字符 A–Z 与 − 的网状箭头图，字符 G 的三条出边加粗，中下部以竖排省略号 ⋮ 省略中间字符）。

### p.17 〔Proof for the Binary Symmetric Channel（二元对称信道的证明）〕

![l8-p17](fig/l8/mgp00017.png)

<span style="color:#2471a3;">**[section]**</span>（页面左上重绘 BSC 图示；右上重绘 p.9 的码率—错误率散点图，标注 R1、H(7,4)、R3、R5、achievable（可达）/ not achievable（不可达）及曲线与横轴交点 C，均同前。）本讲对二元对称信道证明编码定理的路线图：

- 线性分组码（linear block code，线性分组码）
- 校验子译码器（syndrome decoder，校验子译码器）
- 使用 typical（典型）噪声向量（Use typical noise vectors）
- 计算 average（平均）错误概率（Compute average probability of error）

### p.18 〔How we won the bent coin lottery（我们如何赢得弯曲硬币彩票）〕

![l8-p18](fig/l8/mgp00018.png)

（首行文字同前：为了有 99.99% 的胜算，我们买下了所有 typical（典型）彩票；袋图与手写批注同 p.13：'典型集'中的彩票张数 $|T|\simeq 2^{N H_2(f)}$。）

<span style="color:#2471a3;">**[example]**</span> 本页下半部新增手写图示——典型集—校验子译码器（Typical-set Syndrome Decoder）：

- 一条长蓝框表示长度为 $N$ 的接收比特串：框内画 001000001000⋯（大部分为 0、稀疏处为 1），末尾为 00；框上方红色双箭头标注长度 $N$；左下角手写 $\underline{\mathbf{n}}$ 并以箭头指向框（示意接收串即噪声向量 $\mathbf{n}$ 之形）。
- 其下第二条蓝框内手写 $\mathbf{z} = \mathbf{Hn}$（红色下划线标注 $\mathbf{n}$），框内隐约可见 110、010 等三比特分组（即校验子 $\mathbf{z}$ 的内容）；框下方红色双箭头标注长度 $M$。

### p.19 〔Q（问答题）〕

![l8-p19](fig/l8/mgp00019.png)

<span style="color:#2471a3;">**[example]**</span> 标题仅一个字母 **Q**（question，提问）。正文：

若 $\mathbf{x}$ 是长度 $N$ 的固定非零（non-zero）二进制向量，而 $\mathbf{h}$ 是长度 $N$ 的随机 $\left(\frac12,\frac12\right)$ 二进制向量，则

```math
\mathbf{h}^\mathsf{T}\mathbf{x} = 0\ \mathrm{mod}\ 2
```

的概率是多少？（what is the probability that …）

例如（e.g.）：

```math
\mathbf{x}:\ 0\ \ 1\ \ 1\ \ 1 \qquad\quad
\mathbf{h}:\ h_1\ \ h_2\ \ h_3\ \ h_4
```

### p.20 〔Q（问答题）〕

![l8-p20](fig/l8/mgp00020.png)

（题目与例子同上一页：$\mathbf{x}$ 为固定非零二进制向量、$\mathbf{h}$ 为随机 $\left(\frac12,\frac12\right)$ 二进制向量，问 $\mathbf{h}^\mathsf{T}\mathbf{x}=0\ \mathrm{mod}\ 2$ 的概率。）本页给出答案：

Answer: 1/2（答案：$\frac12$）

### p.21 〔Q（问答题）〕

![l8-p21](fig/l8/mgp00021.png)

标题仍为 **Q**。正文：若 $\mathbf{x}$ 是长度 $N$ 的固定非零二进制向量，而 $\mathbf{H}$ 是随机 $\left(\frac12,\frac12\right)$ 二进制矩阵，则

```math
\mathbf{H}\mathbf{x} = \mathbf{0}\ \mathrm{mod}\ 2
```

的概率是多少？（what is the probability that …）

图中画出 $\mathbf{H}$ 的示意结构：$M$ 行随机行向量 $\mathbf{h}^{(1)}, \mathbf{h}^{(2)}, \ldots$ 堆叠而成，每行左右各画一个箭头（$\leftarrow\ \mathbf{h}^{(1)}\ \rightarrow$ 等），行间以竖排省略号 $\vdots$ 省略；右侧红色标注 $\updownarrow\ M$（行数 $M$），下方红色标注 $\leftrightarrow\ N$（每行长度 $N$）。

> <span style="color:#1e8449;">**[note] Note（译者注）:** 把 p.19–21 的问答串起来，就是随机编码论证的引擎。第一步（p.19–20）：$\mathbf{x}\ne\mathbf{0}$ 时，$\mathbf{h}^\mathsf{T}\mathbf{x}=\sum_i h_i x_i$ 只在 $\mathbf{x}$ 的支撑位上求和；支撑位上的 $h_i$ 都是公平硬币，其奇偶和为 0 与为 1 各占一半，故概率恰为 $1/2$——这是"固定向量撞上随机超平面"的基本事实，也是凸几何里证明 KL 非负之外的另一类对称性论证。第二步（本页）：$M$ 行相互独立，每行单独"打中"的概率都是 $1/2$，于是 $P(\mathbf{Hx}=\mathbf{0})=2^{-M}$。现在数一数：典型噪声向量约有 $2^{NH_2(f)}$ 个，随机 $\mathbf{H}$ 把其中任何一个"送进零空间"的概率是 $2^{-M}$，故期望错误概率约为 $2^{NH_2(f)-M}=2^{-N(1-H_2(f)-R)}$（码率 $R=1-M/N$）。只要 $R<C=1-H_2(f)$，指数就是负的，错误随 $N$ 指数消失。一句话：容量＝1 减去噪声熵，这正是 BSC 容量 $C=1-H_2(f)$ 的来历。</span>

### p.22 〔Binary erasure channel（二进制擦除信道）〕

![l8-p22](fig/l8/mgp00022.png)

<span style="color:#2471a3;">**[example]**</span> 二进制擦除信道（binary erasure channel，二进制擦除信道）图示：输入 $x\in\{0,1\}$，输出 $y\in\{0,1,?\}$；转移为 $0\xrightarrow{0.9}0$、$0\xrightarrow{0.1}?$、$1\xrightarrow{0.1}?$、$1\xrightarrow{0.9}1$（"?"表示擦除符号）。信道矩阵：

```math
\mathbf{Q} = \begin{bmatrix} 0.9 & 0 \\ 0.1 & 0.1 \\ 0 & 0.9 \end{bmatrix}
```

（三行对应输出 $0,?,1$，两列对应输入 $0,1$。）

**容量是多少？**（What is the capacity?）

### p.23 〔Feedback（反馈）〕

![l8-p23](fig/l8/mgp00023.png)

本页为两张黑白照片：左图为 Claude Shannon 的青年肖像照；右图为 Shannon 坐在黑板前的照片，黑板上画有 $E(R)$ 曲线草图（纵轴标注 $E(R)$，横轴标注 $R$，曲线自左上向右下降，其下与横轴之间画有斜线阴影）〔本页除照片外无其他文字〕。

### p.24 〔Feedback（反馈）〕

![l8-p24](fig/l8/mgp00024.png)

（两张 Shannon 照片同上一页。）页面下方新增红色大字（MacKay 模拟 Shannon 口吻的调侃）：

"反馈？呸！谁需要反馈？直接用随机码就行了！"（`Feedback? Pah! Who needs feedback? Just use a random code!'）

> <span style="color:#1e8449;">**[note] Note（译者注）:** 这句红色调侃背后藏着一个著名定理：Shannon 在 1956 年的论文《The zero error capacity of a noisy channel》中证明，对无记忆信道，反馈不能提高信道容量 $C$——即使接收端把收到的 $y$ 实时回传给发送端，可达码率的上限也不变。直觉是：容量由互信息的极值决定，而因果的反馈无法凭空创造输入与输出之间新的统计相关性。不过反馈并非无用：它能大幅简化编译码——例如 ARQ（自动重传请求）让接收端发现错误就喊"重来"，用时延换正确率——也能让容量定理的证明变简单。右图黑板上的 $E(R)$ 是可靠性函数：码率越接近 $C$，块错误概率随 $N$ 指数衰减的指数越小，这条曲线刻画了"离红线越近，代价越高"。"谁需要反馈？用随机码！"是 MacKay 替 Shannon 说出的一声吼，强调随机码思想本身已足以抵达容量，反馈不是必需品。</span>

### p.25 〔Homework recommendations（课后作业建议）〕

![l8-p25](fig/l8/mgp00025.png)

- 噪声信道——第 8、9、10 章（仅限 10.1–10.4 节）（Noisy channels - Chapters 8, 9, 10 (10.1-10.4 only)）
  - 练习 9.17（第 155 页）；10.12（第 172 页）；15.12（第 235 页）（Exercises 9.17 (p155); 10.12 (172); 15.12 (235)）
  - 以及（如果想做更多练习）15.11、15.13、15.15（and (if you want more practice) 15.11, 15.13, 15.15）
- 发明一个信道来考考你的同学：（Invent a channel to pose to your colleagues:）
  - "这个信道的容量是多少？"（'what's the capacity of _this_?'）
