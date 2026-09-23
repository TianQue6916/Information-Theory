> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l5 · 行内双语视觉转录版 · 原图见 fig/l5/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l5-p1](fig/l5/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程封面页：大标题为 Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络），标题下衬一条青绿色横线。页面左侧是一张圆形装饰图：绿色圆圈与方块节点连成的网络不断向边缘递归细分，圆周边缘环绕粉红色分形小圆圈。〔本页图形为纯装饰性图示〕

右侧为本讲在课程中的位置（大纲，当前主题以大号青绿色圆点标出）：

- 1 Noisy-channel coding（噪声信道编码）
- **Source coding (Data compression)（信源编码，即数据压缩）** ← 青绿色大圆点标记，为本讲主题
- 2 Information content, entropy（信息量、熵）
- 3 Typicality and the source coding theorem（典型性与信源编码定理）
- 4 Symbol codes（符号码）
- 5 Symbol codes and arithmetic coding（符号码与算术编码）

### p.2 〔Practical data compression（实用数据压缩）〕

![l5-p2](fig/l5/mgp00002.png)

<span style="color:#2471a3;">**[definition]**</span> Claims:（论断：）

1. 一个结果（outcome）的 Shannon information content（香农信息量）

```math
h(x=a_i) = \log_2 \frac{1}{P(x=a_i)}
```

是信息量的一种合理度量。

2. entropy（熵）

```math
H(X) = \sum_x P(x) \log_2 \frac{1}{P(x)}
```

是期望信息量（expected information content）的一种合理度量。

3. <span style="color:#2471a3;">**[theorem]**</span> Source coding theorem（信源编码定理）——来自信源 $X$ 的 $N$ 个结果可以被压缩成大约 $NH(X)$ 比特。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 用概率论的话说，熵没有引入任何新机制：固定分布 $P$ 之后，$h(x)=\log_2\frac{1}{P(x)}$ 只是随机变量（即自信息 self-information），而 $H(X)$ 就是它的期望 $\mathbb{E}_P[h]$，与 Bertsekas 概率论中「期望 = 按概率加权的平均」完全同构。第 3 条之所以成立，靠的是大数定律：$N$ 个独立同分布符号的总自信息 $-\log_2 P(x_1,\dots,x_N)$ 会以高概率集中在 $NH(X)$ 附近，这正是渐近均分性（AEP, asymptotic equipartition principle）与典型集（typical set）思想的种子，教材第 6 章会正式展开。Jensen 不等式（$\log$ 的凹性）还保证熵在均匀分布处取最大值 $\log_2$（字母表大小），说明熵确实度量「不确定性」。以 2 为底时熵的单位是比特，与 CSAPP 中一个二进制位的信息含义直接对接。MacKay 强调 sensible（合理），是在提醒：这些定义不是约定俗成，而是能被定理兑现成压缩业绩的度量。

### p.3 〔Symbol codes（符号码）〕

![l5-p3](fig/l5/mgp00003.png)

<span style="color:#2471a3;">**[example]**</span> 本页是一张 27 行的表格：左侧三列为编号 $i$、符号 $a_i$、概率 $p_i$（英文文本的 26 个字母加空格「–」）；右侧黑底白字给出每个符号的二进制码字，与左表按行一一对应（此处合并转录为四列）：

| $i$ | $a_i$ | $p_i$ | $c(a_i)$ |
|---|---|---|---|
| 1 | a | 0.0575 | 0000 |
| 2 | b | 0.0128 | 001000 |
| 3 | c | 0.0263 | 00101 |
| 4 | d | 0.0285 | 10000 |
| 5 | e | 0.0913 | 1100 |
| 6 | f | 0.0173 | 111000 |
| 7 | g | 0.0133 | 001001 |
| 8 | h | 0.0313 | 10001 |
| 9 | i | 0.0599 | 1001 |
| 10 | j | 0.0006 | 1101000000 |
| 11 | k | 0.0084 | 1010000 |
| 12 | l | 0.0335 | 11101 |
| 13 | m | 0.0235 | 110101 |
| 14 | n | 0.0596 | 0001 |
| 15 | o | 0.0689 | 1011 |
| 16 | p | 0.0192 | 111001 |
| 17 | q | 0.0008 | 110100001 |
| 18 | r | 0.0508 | 11011 |
| 19 | s | 0.0567 | 0011 |
| 20 | t | 0.0706 | 1111 |
| 21 | u | 0.0334 | 10101 |
| 22 | v | 0.0069 | 11010001 |
| 23 | w | 0.0119 | 1101001 |
| 24 | x | 0.0073 | 1010001 |
| 25 | y | 0.0164 | 101001 |
| 26 | z | 0.0007 | 1101000001 |
| 27 | – | 0.1928 | 01 |

（「–」即空格符，概率 0.1928 为全表最大；概率栏与码字栏在原页分列于左右两块面板，首行码字「0000」后有一处屏幕光标残影。）

### p.4 〔Last time（上次课回顾）〕

![l5-p4](fig/l5/mgp00004.png)

<span style="color:#2471a3;">**[section]**</span> Symbol codes（符号码）回顾要点：

- unique decodeability（唯一可译性）——requires（要求）

```math
\sum_i 2^{-l_i} \le 1
```

即 Kraft inequality（Kraft 不等式）；[if equality holds, the code is 'complete']（等号成立时，称该码是「完备的 / complete」）

- prefix codes（前缀码）
  - ▸ and binary trees（与二叉树）
- whenever a code achieved $L=H$, it had（凡达到 $L=H$ 的码，其 codelengths（码长）$l_i^*$ 都等于 information contents（信息量））

```math
l_i^* = \log \frac{1}{p_i}
```

- optimal symbol codes（最优符号码）——The optimal symbol code's expected length $L$ satisfies（最优符号码的期望长度 $L$ 满足）

```math
H(X) \le L < H(X) + 1
```

- Huffman algorithm（Huffman 算法）

> <span style="color:#7f8c8d;">旁注：页面右侧竖排三棵小二叉树示意图——第一棵叶标 0、10、110、111；第二棵叶标 00、01、10、11；第三棵可见标注 0 与 101（未用满预算的树）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 「前缀码 ↔ 二叉树」的等价关系值得用 CSAPP 的眼光吃透：一个二进制码字就是从树根出发的一串左右分支选择，与整数的二进制表示同构；「任何码字都不是另一码字的前缀」翻译成树的语言就是「叶节点不能兼任内部节点」，于是译码器从根往下走、到叶即输出，天然无需分隔符——UTF-8 的自同步设计正是这个直觉。Kraft 不等式可以用「预算」来记：给长度 $l$ 的码字付 $2^{-l}$ 份预算，总预算 $\sum_i 2^{-l_i}\le 1$ 恰好对应整棵二叉树的「叶面积」。等号成立时树被种满，每个无限比特序列都能被唯一译码，这就是 complete（完备）的含义；上一页 p.3 的码正是完备码。哈夫曼算法要做的事情，就是在这一预算约束下把期望长度 $L$ 压到 $H(X)$ 附近。

### p.5 〔What is the optimal symbol code for …（这两个系综的最优符号码是什么？）〕

![l5-p5](fig/l5/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span> 标题句接排两个例子：

Ensemble X（系综 X）：五个符号等概率——a $1/5$，b $1/5$，c $1/5$，d $1/5$，e $1/5$（e 的概率后附一个绿色问号，提示此处需要思考）。

Ensemble Y（系综 Y）：十个符号，概率与 $1/Z, 2/Z, \dots, 10/Z$ 成比例——a $1/Z$，b $2/Z$，c $3/Z$，d $4/Z$，e $5/Z$，f $6/Z$，g $7/Z$，h $8/Z$，i $9/Z$，j $10/Z$（j 的概率后同样附一个绿色问号）。

> <span style="color:#7f8c8d;">旁注：两处绿色「?」为幻灯片自带的提问标记，页面上未写出答案，供课堂当场讨论。</span>

### p.6 〔Prefix codes suffice（前缀码就足够了）〕

![l5-p6](fig/l5/mgp00006.png)

本页主体是一张占满页面的二叉树「预算表」：最左一列是树根的 0 与 1 两格；第二列为 $00, 01 \mid 10, 11$ 四格；第三列为 $000, 001, \dots, 111$ 八格；第四列为 $0000, 0001, \dots, 1111$ 十六格，逐层二分。右侧竖排长框标注 The total symbol code budget（全部符号码的总预算）。图下方为页标题大字：Prefix codes suffice（前缀码就足够了）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张「预算图」值得用 6.006/CLRS 的目光再看一遍：比较排序下界 $\Omega(n\log n)$ 的证明正是同一类叶子计数论证——任何比较算法都是一棵决策树，$n!$ 种排列各需一片叶子，故树高至少 $\log_2 n! \approx n\log_2 n$。Kraft 不等式 $\sum_i 2^{-l_i}\le 1$ 说的是同一件事：二叉树第 $l$ 层只有 $2^l$ 个节点，分给码字的预算不能超支。它解释了两个现象：其一，若把码长都取成 $\lceil\log_2\frac{1}{p_i}\rceil$，预算大致恰好用满；其二，短码字是稀缺资源，把短码分给高频符号正是哈夫曼算法的动机。今后遇到任何「前缀/字典序/决策树」类下界问题，都可以先问一句：这片叶子预算够不够？

### p.7 〔（无标题页）Huffman 编码表与码树〕

![l5-p7](fig/l5/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 本页是 p.3 字母表的 Huffman 编码结果，表格五列：符号 $a_i$、概率 $p_i$、理想码长 $\log_2 \frac{1}{p_i}$、实际码长 $l_i$、码字 $c(a_i)$：

| $a_i$ | $p_i$ | $\log_2 \frac{1}{p_i}$ | $l_i$ | $c(a_i)$ |
|---|---|---|---|---|
| a | 0.0575 | 4.1 | 4 | 0000 |
| b | 0.0128 | 6.3 | 6 | 001000 |
| c | 0.0263 | 5.2 | 5 | 00101 |
| d | 0.0285 | 5.1 | 5 | 10000 |
| e | 0.0913 | 3.5 | 4 | 1100 |
| f | 0.0173 | 5.9 | 6 | 111000 |
| g | 0.0133 | 6.2 | 6 | 001001 |
| h | 0.0313 | 5.0 | 5 | 10001 |
| i | 0.0599 | 4.1 | 4 | 1001 |
| j | 0.0006 | 10.7 | 10 | 1101000000 |
| k | 0.0084 | 6.9 | 7 | 1010000 |
| l | 0.0335 | 4.9 | 5 | 11101 |
| m | 0.0235 | 5.4 | 6 | 110101 |
| n | 0.0596 | 4.1 | 4 | 0001 |
| o | 0.0689 | 3.9 | 4 | 1011 |
| p | 0.0192 | 5.7 | 6 | 111001 |
| q | 0.0008 | 10.3 | 9 | 110100001 |
| r | 0.0508 | 4.3 | 5 | 11011 |
| s | 0.0567 | 4.1 | 4 | 0011 |
| t | 0.0706 | 3.8 | 4 | 1111 |
| u | 0.0334 | 4.9 | 5 | 10101 |
| v | 0.0069 | 7.2 | 8 | 11010001 |
| w | 0.0119 | 6.4 | 7 | 1101001 |
| x | 0.0073 | 7.1 | 7 | 1010001 |
| y | 0.0164 | 5.9 | 6 | 101001 |
| z | 0.0007 | 10.4 | 10 | 1101000001 |
| – | 0.1928 | 2.4 | 2 | 01 |

页面右侧是一棵以细线条画出的 Huffman 码树：叶从上到下依次标注 a, n, b, g, c, s, –, d, h, i, k, x, y, u, o, e, j, z, q, v, w, m, r, f, p, l, t，枝权向左逐级汇聚到根。

> <span style="color:#7f8c8d;">旁注：右下角有黄色页码「3b」；逐行可见实际码长 $l_i$ 基本贴着理想码长上下取整（如 –：2.4→2，e：3.5→4，j：10.7→10）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张表背后的 Huffman 算法你在 6.006 里见过「同款」：每次贪心取出概率最小的两棵子树合并，与「最优文件归并顺序」是同一个问题，正确性靠交换论证（贪心选择不劣于任何最优解的第一步）。最右两列的关系尤其值得玩味：实际码长 $l_i$ 紧贴理想码长 $\log_2\frac{1}{p_i}$ 浮动，但受两件事约束——码长必须是非负整数（符号码的先天缺陷，本讲后半的算术编码将打破它），且 Kraft 预算 $\sum_i 2^{-l_i}\le 1$ 限制短码数量。逐行检查可见个别行（如 q：10.3→9）码长低于理想值的上取整，这正是整数化与预算约束相互博弈的结果。对这种 27 符号的大字母表，整数化损失摊到每个符号上很小，符号码还算划算；但下一节的极端例子会让它翻车。

### p.8 〔Symbol code summary（符号码小结）〕

![l5-p8](fig/l5/mgp00008.png)

<span style="color:#2471a3;">**[theorem]**</span> Gibbs inequality（Gibbs 不等式）：

```math
\sum_i p_i \log \frac{p_i}{q_i} \ge 0
```

[equality only if $\mathbf{q} = \mathbf{p}$]（仅当 $\mathbf{q}=\mathbf{p}$ 时取等号）

<span style="color:#2471a3;">**[section]**</span> Symbol codes（符号码）：

- unique decodeability（唯一可译性）——要求 $\sum_i 2^{-l_i} \le 1$，即 Kraft inequality（Kraft 不等式）；[若等号成立，该码是「完备的」]
- prefix codes（前缀码）▸ and binary trees（与二叉树）
- optimal symbol codes（最优符号码）——The ideal codelengths $l_i^*$ are the information contents（理想码长 $l_i^*$ 就是信息量）

```math
l_i^* = \log \frac{1}{p_i}
```

The optimal symbol code's expected length $L$ satisfies（最优符号码的期望长度 $L$ 满足）

```math
H(X) \le L < H(X) + 1
```

- Huffman algorithm（Huffman 算法）

> <span style="color:#7f8c8d;">旁注：右侧与 p.4 相同的三棵小二叉树示意（0/10/110/111、00/01/10/11、0/101）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Gibbs 不等式就是相对熵 / KL 散度（relative entropy / KL divergence）$D_{\mathrm{KL}}(p\,\|\,q)=\sum_i p_i\log\frac{p_i}{q_i}\ge 0$ 的非负性，证明只需一步 Jensen：$\log$ 凹，故 $-\sum_i p_i\log\frac{q_i}{p_i}\ge -\log\big(\sum_i p_i\frac{q_i}{p_i}\big)=-\log 1=0$，等号当且仅当 $q=p$。用 Strang 线代的语言：把分布看作概率单纯形（各分量非负、和为 1 的向量）上的点，KL 散度就是两个概率向量之间一种非对称「距离」，其非负性来自 $\log$ 的凹性（凸性论证），与内积空间里「范数非负」味道相似但机制不同。这个不等式是全讲结论的引擎：把 $q_i\propto 2^{-l_i}$ 代入，立刻得到 $L\ge H(X)$。KL 非负、熵不超过码长、最大熵原理，其实是同一个凸性事实的三副面孔。

### p.9 〔Today（本课内容）〕

![l5-p9](fig/l5/mgp00009.png)

开场复述两条上节结论：The ideal codelengths $l_i^*$ are the information contents（理想码长 $l_i^*$ 就是信息量）$l_i^* = \log \frac{1}{p_i}$；最优符号码的期望长度 $L$ 满足

```math
H(X) \le L < H(X) + 1
```

<span style="color:#2471a3;">**[section]**</span> Does that wrap up compression?（这样压缩就到此为止了吗？）

- What's wrong with optimal symbol codes?（最优符号码还有什么问题？）

<span style="color:#2471a3;">**[section]**</span> Arithmetic coding（算术编码）

### p.10 〔The Guessing Game（猜谜游戏）〕

![l5-p10](fig/l5/mgp00010.png)

Headline composed of（一条由以下字符集写成的新闻标题）

{ A, B, C, D, E, F, G, H, I, J, K, L, M, …, Z, – }

（「–」代表空格。）

> <span style="color:#7f8c8d;">旁注：本页正文仅此一行，其余留白；标题文字为青绿色，字符集为红色。</span>

### p.11 〔Realistic compression（真实的压缩场景）〕

![l5-p11](fig/l5/mgp00011.png)

<span style="color:#2471a3;">**[example]**</span> Optimal symbol code for（为如下信源构造的最优符号码）——11 个符号的极端偏斜分布：

| 符号 | $p_i$ | 码字 |
|---|---|---|
| a | 0.001 | 00000 |
| b | 0.001 | 00001 |
| c | 0.990 | 1 |
| d | 0.001 | 00010 |
| e | 0.001 | 00011 |
| f | 0.001 | 0100 |
| g | 0.001 | 0101 |
| h | 0.001 | 0110 |
| i | 0.001 | 0111 |
| j | 0.001 | 0010 |
| k | 0.001 | 0011 |

expected length（期望长度）1.034；entropy（熵）0.11401；length / entropy（长度 ÷ 熵）9。

> <span style="color:#7f8c8d;">旁注：图中符号与概率为蓝紫色等宽字体，码字与末尾三行汇总数据为红色等宽字体。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张表把符号码的软肋暴露得一清二楚：概率 0.990 的 c 理想码长只有 $\log_2(1/0.99)\approx 0.014$ 比特，但任何符号码都必须给它整 1 比特；十个 0.001 的符号理想长度约 10 比特，实际却只分到 4–5 比特——Kraft 预算强迫短码字存在，于是期望长度被托高到 1.034 比特，约为熵的 9 倍。修补办法是「分组」：一次编码 $N$ 个符号，让大数定律把长序列的概率质量集中到典型集（typical set）里，整串只花约 $NH(X)$ 比特——这正是本讲开头第 3 条信源编码定理的内容，也是渐近均分性（AEP）的用武之地。用概率论的语言说：单符号损失是有界的整数化开销，按 $N$ 摊薄后趋于零。这和 CSAPP 里「按字节对齐浪费空间、按块传输才划算」是同一种权衡。

### p.12 〔Arithmetic coding（算术编码）〕

![l5-p12](fig/l5/mgp00012.png)

<span style="color:#2471a3;">**[section]**</span> 本页为算术编码演示程序的界面截图，可辨认的文字如下：

- 顶部工具栏：uniform（均匀）、bounded（有界）、at_mouse（在鼠标处）、at_cross（在十字线处）四种模式；参数框：Colors: 28、Truncate: 6、At: < > 6、Slide: < > -2。
- 左画布：单位区域按概率剖分成彩色子块，可见粉色块标 ":a"、品红块标 ":b"，其余大片浅蓝；左缘中部有红/蓝十字准星标记，右下角另有一极小的品红块〔无法辨认〕。
- 右画布：剖分进一步细分，可见大块 ":0" 与 ":1"，上方小块 ":00"、其下 ":01"（旁有绿色小角标 0 与 1）。
- 黄色控制条：Reset；magnify: 0；width: 1.0；centre: 0.5；最右端刻度 0.0 与 1.0。
- 参数行（左，红框）：english1、english2、jack、Alphabet 3、adaptive、0.43 0.43 0.14；Active、Pushiness: 1、ps；下方粉色回显条 ":ba" 与数字 2。
- 参数行（右，绿框）：Alphabet 2、adaptive、0.5 0.5；Active、Pushiness: 1、ps；下方绿色回显条 ":01" 与数字 2。
- 中排按钮：Clean、VariableL〔?〕、DelDiaRel〔?〕、Reinstate。
- 底排按钮：Quit、Hide、Show（灰置）、OneCanvas、Dump、Mousepad、Help。

〔本页为程序界面截图〕

### p.13 〔Other uses for arithmetic coding（算术编码的其他用途）〕

![l5-p13](fig/l5/mgp00013.png)

<span style="color:#2471a3;">**[section]**</span> Efficient writing（高效书写）

- Compression:（压缩：）Text（文本）$\longrightarrow$ Bit string（比特串）(preferably short)（越短越好）
- Writing:（书写：）Text（文本）$\longleftarrow$ Gesture（手势）(preferably brief)（越简短越好）

### p.14 〔Dasher（Dasher 文字输入软件）〕

![l5-p14](fig/l5/mgp00014.png)

本页为 Dasher 文字输入软件的截图：

- 顶部菜单栏：File、Edit、Options、Help；菜单下为已输出文本的显示框（当前为空）。
- 主画布：绿色背景，中央一大块黄色区域；一条黑色竖线贯穿画布作准星，中心处有一小段水平黑线，红色细线从中心指向右上方（指示行进方向）。
- 画布右缘纵向排列彩色字母方块（黄、粉、蓝相间，块高与该字母的预测概率成正比）：A, B, C, D, E, F, G, H, I, J, K, M, N, O, P, R, S, T, U, V, W, Y 等字母块及标点块（下缘可见绿色小方块与「.」等符号）。
- 主画布右上缘有正在移出视野的黑色字符（形似 m）〔无法辨认〕。
- 底部：Speed（速度）滑杆，示数 2.8。
- 页面左下角以蓝色显示网址：www.inference.phy.cam.ac.uk/dasher/

〔本页为软件界面截图〕

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Dasher 是算术编码的「逆向驱动」：压缩时是编码器读符号、按概率剖分区间、输出二进制位；Dasher 把箭头反过来——用户的手势相当于译码器在按概率剖分的区间树里选路，走进哪个字母块就等于「选中」该字母，累积的选择路径写出来就是被「编码」出的文本。从 6.006 的视角看，这是一棵带权区间的二分查找树：每步把当前区间按各符号概率切开，块越大越容易被命中，常用字母自动获得更大的「靶子」。从 CSAPP 的视角看，最终文本等价于 $[0,1)$ 内某个实数的二进制展开，输入速度对应信息率——你是在用鼠标「写出」香农信息量。这个界面最初为残障用户的单键/眼动输入设计，是信息论直接变成可用软件的著名案例。

### p.15 〔（无标题页）课堂问答题：编码流中 1 的概率〕

![l5-p15](fig/l5/mgp00015.png)

<span style="color:#2471a3;">**[example]**</span> 页面左上角为绿色「Q:」，题目：若我们对来自如下系综（ensemble）的符号进行编码

$\mathcal{A}_X = \{\text{a}, \text{b}, \text{c}, \text{d}\}$

$\mathcal{P}_X = \{1/2, 1/4, 1/8, 1/8\}$

所用符号码（symbol code）为

$\mathcal{C} = \{0, 10, 110, 111\}$，

what is the probability '$p_1$' that a bit plucked at random from the encoded stream is a 1?（那么从编码后的比特流中随机抽取一比特，它是 1 的概率「$p_1$」是多少？）

横线下方给出三个选项：

- A　$p_1 < \frac{1}{2}$
- B　$p_1 = \frac{1}{2}$
- C　$p_1 > \frac{1}{2}$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 用概率论的两件基本功就能算出答案：全概率公式与期望的线性性。随机比特落在第 $i$ 个符号码字内的概率是 $p_i$，故 $p_1=\sum_i p_i\cdot\frac{\text{码字中 1 的个数}}{l_i}=\frac14\cdot\frac12+\frac18\cdot\frac23+\frac18\cdot\frac33=\frac13<\frac12$，选 A（a 的码字 0 不贡献 1）。这揭示了一个反直觉的事实：即使码长完全「理想」，符号码输出的比特流也是 0 多 1 少的偏斜流——压缩的本质恰恰是制造这种偏斜，再用后续手段把它摊平。回头看 p.11 的 9 倍差距与信源编码定理：长序列层面（典型集、AEP、大数定律）才是精确达到 $NH(X)$ 的舞台，符号码只在单符号层面工作，所以永远差着整数化的「零头」。

### p.16 〔Recommended exercises（推荐练习）〕

![l5-p16](fig/l5/mgp00016.png)

<span style="color:#2471a3;">**[section]**</span> Project:（项目：）为一个 $N = 10{,}000$ 比特、每比特以概率 $f = 0.01$ 取值为 1 的源文件，发明一对 compressor（压缩器）与 uncompressor（解压器）；Implement them and/or estimate how well your method works.（把它们实现出来，和/或估计你的方法效果如何。）

- Huffman programs（Huffman 程序）huffman.p、huffman.py 已放到课程网站上；
  - also a 'bent coin' file 0010000… as a compression benchmark（另附一个「弯硬币」文件 0010000…，可作压缩性能基准）
- Also exercises 5.22, 5.26, 5.27（另有习题 5.22、5.26、5.27）
- Reading: Chapters 1, 2, 4, 5. And 6.（阅读：第 1、2、4、5 章以及第 6 章）
- Advance reading: Chapters 8, 9, 10（预读：第 8、9、10 章）
