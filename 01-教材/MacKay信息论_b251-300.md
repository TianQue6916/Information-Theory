<!-- 书页 251–300｜来源：B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->



<span style="color:#7f8c8d">书内 p.251（PDF p.263）｜ 17.3: Counting the number of possible messages</span>

[Figure 17.2：通道 A 的四种等价表示，四幅子图并列。(a) 状态图：两个圈标着 0 与 1，边 0→0、0→1、1→0，边上标着该转移发出的符号（0 或 1）。(b) trellis section：两个相继时刻 $s_n$、$s_{n+1}$ 各一列两个节点，结构同状态图。(c) trellis：把 (b) 沿时间串接成一条带状有向图。(d) connection matrix：2×2 的 0/1 矩阵。**边的标签与子图 (c) 的层数无法从文字层复原**（文字层只留下 `0 1 0 1` 之类的碎片与 ASCII 箭头）。]

所以在这一章里，我们把长度为 $N$ 的可区分消息数记作 $M_N$，并把 capacity 定义为：

```math
C = \lim_{N\to\infty} \frac{1}{N} \log M_N. \qquad (17.10)
```

一旦搞清了一个通道的 capacity，我们就会回头做「为这个通道造一个实用码」的任务。

### 17.3 Counting the number of possible messages（数一数可能有多少条消息）

先引入受约束通道的几种表示。在 state diagram（状态图）里，发送端的状态画成圆，圆里写着状态名。从一个状态到另一个状态的有向边表示发送端**允许**从第一个状态走到第二个状态，边上的标签表示做这次转移时发出的符号。图 17.2a 是通道 A 的状态图：它有两个状态 0 和 1；转移到状态 0 时发出一个 0，转移到状态 1 时发出一个 1；从状态 1 到状态 1 的转移不可能。

我们也可以把状态图表示成一个 trellis section（网格段）：它把两个相继时刻的两个状态画在两个相继的水平位置上（图 17.2b）。发送端在时刻 $n$ 的状态记作 $s_n$。所有可能的状态序列可以用一张 trellis（网格图）表示，见图 17.2c。一条合法序列对应 trellis 中的一条 path（路径），而合法序列的条数就是路径的条数。

[Figure 17.3：通道 B 与 C 的状态图、trellis section 与 connection matrix。B 有四个状态（按 §17.4 的等价关系与图注推断为 `00`、`0`、`1`、`11`，即「最近两个已发符号」），每个状态的可选出边数为 2、1、1、2；C 也有四个状态。**状态名与边标签在文字层里断裂成单字符行（`00`、`0`、`1`、`11` 与 `m`、`n` 碎片），子图结构无法可靠复原**；但两个 connection matrix 的数值可从文字层逐位恢复，见下方译注（已用特征值校验）。]

> <span style="color:#1e8449;">**[译注]** 把图 17.2d 与 17.3 的矩阵从碎片里还原，是这页唯一「必须算过才敢写」的地方，因为**文字层给出的矩阵与 §17.3 正文的定义在索引顺序上是反的**。正文说 $A_{ss'} = 1$ 表示「从 $s$ 到 $s'$ 有边」，按这个定义通道 A 的矩阵应是 $\begin{bmatrix}1 & 1\\ 1 & 0\end{bmatrix}$（状态 0 可发 0 或 1）；文字层实际印的是 $\begin{bmatrix}0 & 1\\ 1 & 1\end{bmatrix}$，只有读成**行 = 目标状态、列 = 源状态**（即 $c^{(n+1)}_{s'} = \sum_s A_{s's}\,c^{(n)}_s$，与 (17.19) 的下标顺序一致）才自洽。校验办法：取 $c^{(0)} = [0, 1]^{\mathsf T}$（图 17.5 的起始假设），递推得 $c^{(1)} = [1,1]$、$c^{(2)} = [1,2]$、$c^{(3)} = [2,3]$，求和得 $M_1, M_2, M_3 = 2, 3, 5$，与图 17.4、17.5a 印的数字逐个吻合。同批矩阵的 B、C 两版（同样按行 = 目标读）为

```math
A_B = \begin{bmatrix}1 & 0 & 1 & 0\\ 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\\ 0 & 1 & 0 & 1\end{bmatrix},\qquad
A_C = \begin{bmatrix}0 & 0 & 1 & 0\\ 1 & 0 & 1 & 0\\ 0 & 1 & 0 & 1\\ 0 & 1 & 0 & 0\end{bmatrix},
```

两者最大特征值都等于 $\varphi = 1.618$（$A_B$ 的另两个特征值是 $e^{\pm \mathrm{i}\pi/3}$，$A_C$ 是 $-e^{\pm \mathrm{i}\pi/3}$），这正好解释下一节那句「三个 trellis 的 principal eigenvalue 相同」。**失效对象**：若按正文那句字面定义直接把 $A$ 当成 from-to 去用递推，第一个算就崩：$c^{(1)} = A[0,1]^{\mathsf T} = [1,0]^{\mathsf T}$，得 $M_1 = 1$ 而非 2，与图 17.5a 冲突。但要分清两件事：**容量本身不受这个方向影响**——两种读法互为转置，特征多项式同为 $\lambda^2-\lambda-1$，$\lambda_1 = \varphi$ 两边一样；错的只是「矩阵乘向量」那一侧。这条区分很实用：算 capacity 时可以随便转置，写生成器、做 DP 或核对计数时不行。落点：本书 §17.3 与式 (17.15)、表 C.4（书内 p.608 给出 A 与 B 的特征向量）；Strang 线代第 6 章的特征值与对角化、第 8 章正矩阵与 Perron 根。</span>



<span style="color:#7f8c8d">书内 p.252（PDF p.264）｜ 17 — Communication over Constrained Noiseless Channels</span>

[Figure 17.4：在通道 A 的 trellis 上数路径条数。图分三步（$M_1 = 2$、$M_2 = 3$、$M_3 = 5$），每步把 trellis 从左往右过一遍，节点旁的累积计数依次是 $(1,1) \to (2,1) \to (3,2)$。这三个小图的结构（两列节点 + 三条边）可从文字层的 ASCII 箭头与数字复原。]

[Figure 17.5：在通道 A、B、C 的 trellis 里数路径条数。三个子图各画了 $n = 1,\ldots,8$ 八段，顶端标出总数 $M_n$。图注给出起始假设：**第一个比特之前是 `00`**，于是通道 A 与 B 允许任意首字符，而通道 C 的首字符必须是 1。

能复原的是 $M_n$ 与通道 A 的逐节点计数（见下表，值与图 17.5a 逐个吻合）；B、C 的逐节点计数在文字层里断裂成 `- 1 1 1`、`2 2 1 3` 一类单字符行，且状态编号顺序不可知，故**只给总数，不给逐节点复原**。]

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| A：状态 0 的路径数 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 |
| A：状态 1 的路径数 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 |
| A：总数 $M_n$ | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 |
| B：总数 $M_n$ | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 |
| C：总数 $M_n$ | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 |

> <span style="color:#1e8449;">**[译注]** 三个通道的 $M_1$ 是 $2, 2, 1$，这个差别不是排版噪声，而是**图注那句「第一个比特之前是 `00`」在 C 上生效的结果**，值得算一遍。C 的规则是「所有游程长度为一或二」，若假定串前已有两个 0，那么第一个比特**不能**是 0（否则出现 `000`，三个 0 的游程非法），只能是 1；而 A、B 两种规则下首字符都可以自由选（A 允许 $0$ 与 `1`；B 要求游程 $\ge 2$，前面已有的 `00` 恰好让紧跟的 0 合法，紧跟的 1 也能开一个新游程）。校验办法：把 C 的序列 $1, 2, 3, 5, 8, 13, 21, 34$ 与 A 的序列 $2, 3, 5, 8, 13, 21, 34, 55$ 对齐，可见 **C 的 $M_n$ 恰好等于 A 的 $M_{n-1}$**（$34 = 34$、$21 = 21$、$13 = 13$ 逐个成立），也就是整条序列左移一格。**失效对象**：若忽略这条边界假设、把 C 的 $M_1$ 也写成 2，则 $M_8$ 会算成 55，与图 17.5c 印的 34 冲突；更要紧的是「C 与 A 等价」这个结论会差一个因子——等价性只能成立到**相差一个初始条件**，这正是习题 17.7 解答里那句「只有假定 A 的首字符必须是 0，两通道才严格等价」的来源。落点：本书图 17.5 图注、习题 17.7 及其解答（书内 p.257）；6.042J 的 Recurrences（同一条递推、不同初值）；6.006 的 Dynamic Programming（初值是 DP 表的第 0 行）。</span>



<span style="color:#7f8c8d">书内 p.253（PDF p.265）｜ 17.3: Counting the number of possible messages</span>

[Figure 17.6：在通道 A 的 trellis 里数路径条数的完整数据表。表头为 $n$、$M_n$、$M_n/M_{n-1}$、$\log_2 M_n$、$\frac{1}{n}\log_2 M_n$，全部数值可从文字层完整复原，见下表。]

| $n$ | $M_n$ | $M_n/M_{n-1}$ | $\log_2 M_n$ | $\frac{1}{n}\log_2 M_n$ |
|---|---|---|---|---|
| 1 | 2 | 1.0 | 1.00 | 2 |
| 2 | 3 | 1.500 | 1.6 | 0.79 |
| 3 | 5 | 1.667 | 2.3 | 0.77 |
| 4 | 8 | 1.600 | 3.0 | 0.75 |
| 5 | 13 | 1.625 | 3.7 | 0.74 |
| 6 | 21 | 1.615 | 4.4 | 0.73 |
| 7 | 34 | 1.619 | 5.1 | 0.73 |
| 8 | 55 | 1.618 | 5.8 | 0.72 |
| 9 | 89 | 1.618 | 6.5 | 0.72 |
| 10 | 144 | 1.618 | 7.2 | 0.72 |
| 11 | 233 | 1.618 | 7.9 | 0.71 |
| 12 | 377 | 1.618 | 8.6 | 0.71 |
| 100 | $9\times10^{20}$ | 1.618 | 69.7 | 0.70 |
| 200 | $7\times10^{41}$ | 1.618 | 139.1 | 0.70 |
| 300 | $6\times10^{62}$ | 1.618 | 208.5 | 0.70 |
| 400 | $5\times10^{83}$ | 1.618 | 277.9 | 0.69 |

> <span style="color:#1e8449;">**[译注]** 表 17.6 最后两列是同一条极限的两种收敛速度，值得单独看——**「$\lambda_1$ 决定容量」与「容量在第几项才看得出来」是两件事**。$\frac{1}{n}\log_2 M_n$ 从 $n=1$ 的 $2.00$ 掉到 $n=400$ 的 $0.69$，逼近速度是 $O(1/n)$：由 $M_n = F_{n+2} \approx \gamma^{n+2}/\sqrt{5}$ 得

```math
\frac{1}{n}\log_2 M_n = \log_2\gamma + \frac{2\log_2\gamma - \tfrac{1}{2}\log_2 5}{n} + O\!\left(\frac{1}{n^2}\right) = 0.6942 + \frac{0.228}{n},
```

代入 $n=400$ 得 $0.6947$，四舍五入印成 $0.69$ ✓；代入 $n=100$ 得 $0.6965$，印成 $0.70$ ✓；$n=10$ 得 $0.717$，印成 $0.72$ ✓。**失效对象**：若以为 $n=10$ 的 $0.72$ 就是容量，会高估 $0.026$ 比特，而这个偏差**不随 $n$ 指数消失**，只以 $1/n$ 衰减——$n = 10^{6}$ 时才降到 $0.6942 + 2.3\times10^{-7}$。这就是「容量是 $N\to\infty$ 的极限、不是任何有限 $N$ 的码率」的定量版本：任何定长块码只能取到 $\lfloor\log_2 M_N\rfloor/N$，$N = 16$ 时是 $0.625$，比 $0.694$ 低 10%（见 §17.5 与习题 17.8）。落点：本书表 17.6、§17.5、习题 17.8 的解答；6.042J 的 Asymptotics（$O(1/n)$ 展开）；6.006 的 Amortized analysis（同类「加常数修正项」的分析）。</span>

合法序列的条数就是路径的条数。为了数清穿过 trellis 的路径有多少条，我们可以**忽略边上的标签**，用一个 connection matrix（连接矩阵）$A$ 概括整段 trellis section：若从状态 $s$ 到 $s'$ 有一条边，则 $A_{ss'} = 1$，否则 $A_{ss'} = 0$（图 17.2d）。图 17.3 给出了通道 B 与 C 的状态图、trellis section 与连接矩阵。

让我们用 trellis 上的 message passing（消息传递）来数通道 A 的路径条数。图 17.4 画出了这个计数过程的前几步，图 17.5a 画出了走 $n$ 步之后终止于各状态的路径数（$n = 1,\ldots,8$）。长度为 $n$ 的路径总数 $M_n$ 标在图的上方。我们认出 $M_n$ 正是 Fibonacci series（斐波那契数列）。

> <span style="color:#1e8449;">**[译注]** 「$M_n$ 就是 Fibonacci」这句话要能被**算**出来才算理解，否则只是把两个名字并排放着。A 的递推是 $c^{(n+1)} = A c^{(n)}$，而 $A = \begin{bmatrix}0 & 1\\ 1 & 1\end{bmatrix}$ 的特征多项式是 $\lambda^2 - \lambda - 1$，于是 $M_n = M_{n-1} + M_{n-2}$ 而 $M_1 = 2$、$M_2 = 3$——**初值从 $2,3$ 起步而不是 $1,1$，所以 $M_n = F_{n+2}$**。逐项核对：$F_3 = 2$、$F_4 = 3$、$F_5 = 5$、$F_{10} = 55$ ✓，与图 17.5a 的 $2,3,5,8,13,21,34,55$ 一格不差。**这条下标位移是可反驳的**：若误记成 $M_n = F_n$，则 $M_8$ 会是 21 而不是 55，容量会被估成 $\log_2 21^{1/8} = 0.549$ 比特（真值 $0.694$），误差一路传到下一节的 $C = \log_2\gamma$。**失效对象**：抽掉「初始条件 $M_1 = 2$（两种首字符都合法）」这条、改成「首字符必须是 0」，序列退化成 $1,2,3,5,8,\ldots$，即 $M_n = F_{n+1}$——同一条 trellis、同一个 $\lambda_1$，所有 $M_n$ 都差一个因子 $\varphi$，**capacity 不变而首个分辨单元少了一半**。落点：本书 §17.3、表 17.6、习题 17.6；6.042J 的 Recurrences（特征方程法）与 Generating functions；6.006 的 Dynamic Programming。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.6.[1]**</span> Show that the ratio of successive terms in the Fibonacci series tends to the golden ratio,

```math
\gamma \equiv \frac{1 + \sqrt{5}}{2} = 1.618. \qquad (17.11)
```

> 中文话题：证明 Fibonacci 相邻两项之比的极限是 golden ratio——把比值的极限设成 $x$，得 $x = 1 + 1/x$，即 $x^2 = x + 1$，正根就是 $\gamma$。

于是，在相差一个常数因子的意义下，$M_N$ 随 $N\to\infty$ 按 $M_N \sim \gamma^N$ 增长，所以通道 A 的 capacity 是

```math
C = \lim \frac{1}{N}\log_2\left(\text{constant} \cdot \gamma^N\right) = \log_2 \gamma = \log_2 1.618 = 0.694. \qquad (17.12)
```

怎么描述我们刚才做的事？路径计数构成一个向量 $c^{(n)}$，我们可以用下式从 $c^{(n)}$ 得到 $c^{(n+1)}$：

```math
c^{(n+1)} = A\,c^{(n)}. \qquad (17.13)
```

于是

```math
c^{(N)} = A^{N} c^{(0)}, \qquad (17.14)
```

其中 $c^{(0)}$ 是任何符号被发送之前的那个状态计数。在图 17.5 里我们取 $c^{(0)} = [0, 1]^{\mathsf T}$，也就是说开头两个符号都是允许的。路径总数是 $M_n = \sum_s c^{(n)}_s = c^{(n)} \cdot \mathbf{1}$。在极限下，$c^{(N)}$ 由 $A$ 的 principal right-eigenvector（主右特征向量）主导：

```math
c^{(N)} \to \text{constant} \cdot \lambda_1^{N} e^{(R)}. \qquad (17.15)
```



<span style="color:#7f8c8d">书内 p.254（PDF p.266）｜ 17 — Communication over Constrained Noiseless Channels</span>

这里 $\lambda_1$ 是 $A$ 的 principal eigenvalue（主特征值）。所以，要找出任何受约束通道的 capacity，我们只需要求出它连接矩阵的主特征值 $\lambda_1$。然后

```math
C = \log_2 \lambda_1. \qquad (17.16)
```

### 17.4 Back to our model channels（回到我们的模型通道）

把图 17.5a 与图 17.5b、17.5c 对比，看起来通道 B 与 C 的 capacity 与通道 A 相同。三个 trellis 的 principal eigenvalue 确实相同（通道 A 与 B 的特征向量印在表 C.4 底部，书内 p.608）。而且这些通道之间有着密切的联系。

[Figure 17.7：一个 accumulator（累加器）与一个 differentiator（差分器）的框图。累加器：输入 $s$ 与反馈量 $z_0$ 相加，经一拍延迟得 $z_1$，输出 $t$；差分器结构对称。**框图里的连线方向与反馈点位置在文字层里只剩 `z0`、`z1`、`⊕`、`s`、`t` 碎片与 ASCII 箭头，无法复原成可靠的信号流图**，故此处只保留其数学定义 (17.17)、(17.18)，图本身按原文标注。]

### Equivalence of channels A and B（通道 A 与 B 的等价）

如果我们取通道 A 的任意合法串 $s$，把它送进一个 accumulator（累加器），得到 $t$：

```math
t_1 = s_1, \qquad t_n = t_{n-1} + s_n \bmod 2 \quad \text{for} \quad n \ge 2, \qquad (17.17)
```

那么得到的串是通道 B 的合法串，因为 $s$ 里没有 `11`，所以 $t$ 里没有孤立的数字。accumulator 是一个可逆算子，所以反过来，通道 B 的任意合法串 $t$ 也能通过二元 differentiator（差分器）

```math
s_1 = t_1, \qquad s_n = t_n - t_{n-1} \bmod 2 \quad \text{for} \quad n \ge 2 \qquad (17.18)
```

映回通道 A 的合法串 $s$。由于在模 2 算术里 $+$ 与 $-$ 等价，differentiator 同时也是一个 blurrer（模糊器），把信源流与滤波器 $(1, 1)$ 做卷积。

通道 C 也与通道 A、B 有着密切的联系。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.7.[1, p.257]**</span> What is the relationship of channel C to channels A and B?

> 中文话题：问 C 与 A、B 的等价关系——答案是把 A 的合法串先取反（1↔0）再过 accumulator；边界处需约定首字符，否则只差一个「前面垫 0」的假设。

> <span style="color:#1e8449;">**[译注]** 「累加器把 A 的串映成 B 的串」这句话的证明只有一行代数，但它省掉的算力是本章最实在的一笔：**通道 B 的 $4\times4$ 特征问题不必再解第二遍**。机制是：$s$ 中禁止 `11` ⇒ $s$ 的 1 位置互不相邻 ⇒ $t_n = t_{n-1} + s_n$ 在 $s_n = 1$ 时翻转、在 $s_n = 0$ 时保持 ⇒ $t$ 每次翻转之间至少隔一拍 ⇒ $t$ 中既无孤立 1 也无孤立 0，正是 B 的规则（runlength $\ge 2$）。验一遍最长的合法串：$s = 10010 \Rightarrow t = 1,1,1,0,0$（$t_1 = 1$，$t_2 = 1+0 = 1$，$t_3 = 1+0 = 1$，$t_4 = 1+1 = 0$，$t_5 = 0+0 = 0$）得 `11100`，游程长度 3 与 2 ✓ 合法。**失效对象**：若把 accumulator 换成「延迟相加后不取模」（普通整数累加），逆映射不再唯一，$t$ 会随 $N$ 位数增长而溢出，且 B 的合法串装不下——可逆性正是 mod 2 给的，去掉它这条等价就塌成单向的「A 的码可以当 B 的码用」，容量关系无从谈起。**方向感**：这条等价把 B、C 的容量判定变成一次查表（同为 $\log_2\varphi = 0.6942$），而不必再解两次特征方程；工程上它解释了磁盘为什么常用 precoder（预编码器，即这里的累加器）——先把 runlength-limited 的码流「积分」成无约束流再判决。落点：本书 §17.4、(17.17)、(17.18)、习题 17.7 的解答（书内 p.257）；CSAPP 第 3 章的移位/XOR 状态机与有限状态机的等价；6.042J 的 Modular arithmetic。</span>

### 17.5 Practical communication over constrained channels（在受约束通道上做实用通信）

好，实践中到底怎么做？既然三个通道等价，我们就集中看通道 A。

### Fixed-length solutions（定长方案）

我们从**显式枚举**的码开始。下表这个码达到 $3/5 = 0.6$ 的码率。

<span style="color:#00838f;">**Table 17.8**（通道 A 的一个 runlength-limited 码）</span>

| $s$ | $c(s)$ |
|---|---|
| 1 | 00000 |
| 2 | 10000 |
| 3 | 01000 |
| 4 | 00100 |
| 5 | 00010 |
| 6 | 10100 |
| 7 | 01010 |
| 8 | 10010 |

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.8.[1, p.257]**</span> Similarly, enumerate all strings of length 8 that end in the zero state. (There are 34 of them.) Hence show that we can map 5 bits (32 source strings) to 8 transmitted bits and achieve rate 5/8 = 0.625. What rate can be achieved by mapping an integer number of source bits to $N = 16$ transmitted bits?

> 中文话题：数长度为 8、终止于状态 0 的合法串有 34 条，从中取 32 条即可压进 5 个信源比特（rate $5/8 = 0.625$）；再问 $N=16$ 时能装几比特——答案是 10 比特（rate 仍 0.625），这一问暴露了定长码的离散化损失。



<span style="color:#7f8c8d">书内 p.255（PDF p.267）｜ 17.5: Practical communication over constrained channels</span>

### Optimal variable-length solution（最优变长方案）

在受约束通道上传送信息的最优方式，是找出 trellis 上每一点的最优转移概率 $Q_{s'|s}$，并按这些概率做转移。

讨论通道 A 时我们已经看到：密度 $f = 0.38$ 的稀疏信源驱动码 C2，就能达到 capacity。而我们知道怎么做 sparsifier（稀疏化器，见第 6 章）：设计一个对稀疏信源最优压缩的 arithmetic code，那么它对应的 decoder 就给出一个从稠密（也就是随机二元）串到稀疏串的最优映射。

求最优概率这件事留作习题。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 17.9.[3]**</span> Show that the optimal transition probabilities $Q$ can be found as follows. Find the principal right- and left-eigenvectors of $A$, that is the solutions of $Ae^{(R)} = \lambda e^{(R)}$ and $e^{(L)\mathsf T}A = \lambda e^{(L)\mathsf T}$ with largest eigenvalue $\lambda$. Then construct a matrix $Q$ whose invariant distribution is proportional to $e^{(R)}_i e^{(L)}_i$, namely

```math
Q_{s'|s} = \frac{e^{(L)}_{s'} A_{s's}}{\lambda\, e^{(L)}_{s}}. \qquad (17.19)
```

> 中文话题：给出「最优转移概率」的构造公式——用连接矩阵的主左、主右特征向量拼出 $Q$，其不变分布正比于 $e^{(R)}_i e^{(L)}_i$，这个分布恰好让每步熵达到 $\log_2\lambda$。
>
> [Hint: exercise 16.2 (p.245) might give helpful cross-fertilisation here.]

> 提示的中文：习题 16.2（书内 p.245）可能在这里提供有用的「交叉施肥」——那道题正是用前向/后向消息按比例做**均匀随机游走**，与这里用左右特征向量定转移概率是同一件事。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.10.[3, p.258]**</span> Show that when sequences are generated using the optimal transition probability matrix (17.19), the entropy of the resulting sequence is asymptotically $\log_2 \lambda$ per symbol. [Hint: consider the conditional entropy of just one symbol given the previous one, assuming the previous one's distribution is the invariant distribution.]

> 中文话题：证明按 (17.19) 生成的序列每符号熵趋于 $\log_2\lambda$——只需算一阶条件熵 $H(S_t\mid S_{t-1})$，在不变分布下 $e^{(L)}$ 项全部相消，只剩 $\log\lambda$。

> <span style="color:#1e8449;">**[译注]** (17.19) 看着像「凭空掉下来的特征向量组合」，其实它是**习题 16.2 的同一个技巧换了住址**，认出来能省掉一次重新推导。习题 16.2 要对 trellis 做**均匀**随机游走，办法是让每个岔口的概率正比于下游的路径条数（后向消息）；这里要对 trellis 做**熵最大化**的随机游走，办法是让转移概率正比于 $e^{(L)}_{s'}A_{s's}$——$e^{(L)}$ 就是左那侧的势函数，作用与后向消息完全相同。检验不变分布：设 $P(s)\propto e^{(R)}_s e^{(L)}_s$，则

```math
\sum_s P(s)Q_{s'|s} = \frac{1}{Z}\sum_s e^{(R)}_s e^{(L)}_s\cdot\frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s} = \frac{e^{(L)}_{s'}}{Z\lambda}\sum_s A_{s's}e^{(R)}_s = \frac{e^{(L)}_{s'} e^{(R)}_{s'}}{Z} = P(s'),
```

第三个等号用了 $Ae^{(R)} = \lambda e^{(R)}$，即 $\sum_s A_{s's}e^{(R)}_s = \lambda e^{(R)}_{s'}$（注意 (17.19) 的 $A$ 下标顺序是 to-from）。**失效对象**：若省掉 $e^{(L)}$ 那一项、只按 $e^{(R)}$ 定概率（最常见的错，因为右特征向量看起来更「自然」），不变分布就不再是 $\propto e^{(R)}_s e^{(L)}_s$，习题 17.10 的熵会算得**小于** $\log_2\lambda$；模拟时你会看到路径在 trellis 上偏向某些状态，长串统计明显偏离 $\varphi$ 的等比增长。落点：本书习题 16.2 与 §16.6 的解答、习题 17.10 的解答（书内 p.258）、表 C.4（特征向量数值）；Strang 线代第 6 章（左/右特征向量与相似对角化）、第 8 章（Perron–Frobenius 保证 $e^{(R)} \gt 0$）。</span>

实践中我们多半会用有限精度近似这个最优变长方案。有人可能不喜欢变长方案，因为它使**实际**编码长度在具体情形下不可预测。某些应用里我们希望有保证：一个 $N$ 比特的信源文件，编码后的长度一定短于某个给定值，比如 $N/(C+\epsilon)$。举例来说，如果所有 512 字节的块都已知占用同样多的磁盘面积，磁盘驱动器就好控制得多。对某些受约束通道，我们可以对变长编码做一个简单修改，给出这种保证：找两个码、两个把二元串映成变长编码的映射，它们具有这样的性质——对任何信源串 $x$，若 $x$ 在第一个码下的编码短于平均，则它在第二个码下的编码长于平均，反之亦然。于是要发送串 $x$ 时，我们用两个码把整条串都编一遍，发送较短的那一个，并在前面加上一个适当编码的比特，说明用的是哪个码。

[Figure 17.9：1 的最大 runlength 分别为 2 与 3 的两个通道的状态图与连接矩阵。**状态图与边标签无法从文字层复原**（只剩 `0 1`、`1 1 1` 之类的碎片），但两个连接矩阵的数值可恢复，见下方译注。]

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.11.[3C, p.258]**</span> How many valid sequences of length 8 starting with a 0 are there for the run-length-limited channels shown in figure 17.9? What are the capacities of these channels? Using a computer, find the matrices $Q$ for generating a random path through the trellises of the channel A, and the two run-length-limited channels shown in figure 17.9.

> 中文话题：数图 17.9 那两个通道里「以 0 开头、长度 8」的合法串条数，并求各自容量；再用计算机按 (17.19) 求出三个通道的 $Q$ 矩阵。

> <span style="color:#1e8449;">**[译注]** 图 17.9 的两个矩阵是本章唯一能**一行代码验完**的结论，值得当成「特征值决定容量」的实测样本。按文字层复原（行 = 目标状态、列 = 源状态；若状态编号换了顺序只是相似变换 $P^{\mathsf T}AP$，特征值不变）：

```math
A_{\max 2} = \begin{bmatrix}0 & 1 & 0\\ 0 & 0 & 1\\ 1 & 1 & 1\end{bmatrix},\qquad
A_{\max 3} = \begin{bmatrix}0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\ 1 & 1 & 1 & 1\end{bmatrix},
```

两者的特征多项式分别是 $\lambda^3 - \lambda^2 - \lambda - 1$ 与 $\lambda^4 - \lambda^3 - \lambda^2 - \lambda - 1$，故 $\lambda_1$ 是 tribonacci 常数 $1.8393$ 与其四阶版本 $1.9276$，容量

```math
\log_2 1.8393 = 0.8792,\qquad \log_2 1.9276 = 0.9468,
```

与 §17.7 解答 17.11 印的 $0.879$、$0.947$ 逐位吻合 ✓。**失效对象**：若把 1 的最大 runlength 从 2 放宽到无上限，$\lambda_1$ 从 $1.8393$ 跳到 $2$、容量从 $0.879$ 跳到 $1$——多允许一个 1 的长度，容量只涨 $0.121$ 比特；再往上加，收益按 $2^{-L}$ 指数衰减（与习题 17.12 的 $\beta \simeq 1 - 2^{-(L+2)}/\ln 2$ 对得上：$L=2$ 时 $1 - 2^{-4}/0.6931 = 0.9098$）。**这个衰减率是可反驳的**：若有人以为加长 runlength 上限能线性提升容量，$L$ 从 2 到 9 会预期涨 $7/2$ 倍，实际只从 $0.879$ 涨到 $0.999$（涨 14%）。落点：本书 §17.6、习题 17.11、习题 17.12 及其解答（书内 p.258–259）；Strang 线代第 6 章的 companion matrix 与特征多项式；6.006 的 Dynamic Programming（$M_n$ 的 $L$ 阶递推）。</span>



<span style="color:#7f8c8d">书内 p.256（PDF p.268）｜ 17 — Communication over Constrained Noiseless Channels</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.12.[3, p.258]**</span> Consider the run-length-limited channel in which any length of run of 0s is permitted, and the maximum run length of 1s is a large number $L$ such as nine or ninety. Estimate the capacity of this channel. (Give the first two terms in a series expansion involving $L$.) What, roughly, is the form of the optimal matrix $Q$ for generating a random path through the trellis of this channel? Focus on the values of the elements $Q_{1|0}$, the probability of generating a 1 given a preceding 0, and $Q_{L|L-1}$, the probability of generating a 1 given a preceding run of $L-1$ 1s. Check your answer by explicit computation for the channel in which the maximum runlength of 1s is nine.

> 中文话题：把 1 的最大 runlength 放宽到很大的 $L$，求容量关于 $L$ 的展开（前两项）；再猜最优 $Q$ 的形状——关键是 $Q_{1|0}$ 略大于 $1/2$、而 $Q_{L|L-1}$ 要明显小于 $1/2$，因为「已连发 $L-1$ 个 1」时再发 1 就撞墙。

### 17.6 Variable symbol durations（符号时长可变）

我们还可以给「在受约束通道上通信」再加一层花样：假定我们发送的各个符号**时长不同**，而目标是单位时间内传送尽可能多的信息。这类通道分两种口味：unconstrained（无约束）与 constrained（受约束）。

### Unconstrained channels with variable symbol durations（符号时长可变的无约束通道）

我们在习题 6.18（书内 p.125）里遇到过符号时长可变的无约束无噪通道。把那道题做掉，这个题目就做完了。任务是：给定各符号的时长，确定它们的最优使用频率。

这个任务与「设计最优 symbol code」（第 4 章）之间有一个漂亮的类比。当我们为一个概率不等（$p_i$）的信源造二元 symbol code 时，最优消息长度是 $l^{*}_i = \log_2 1/p_i$，于是

```math
p_i = 2^{-l^{*}_i}. \qquad (17.20)
```

类似地，当我们有一个符号时长为 $l_i$（以某种时间单位计）的通道时，这些符号的最优使用概率是

```math
p^{*}_i = 2^{-\beta l_i}, \qquad (17.21)
```

其中 $\beta$ 是该通道的 capacity，单位是 bits per unit time（每时间单位的比特数）。

### Constrained channels with variable symbol durations（符号时长可变的受约束通道）

一旦掌握了本章前面的题目，你应该能自己想出如何定义并求出这类——最棘手的——受约束通道的 capacity。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 17.13.[3]**</span> A classic example of a constrained channel with variable symbol durations is the 'Morse' channel, whose symbols are the dot $\mathrm{d}$, the dash $\mathrm{D}$, the short space (used between letters in morse code) $\mathrm{s}$, and the long space (used between words) $\mathrm{S}$; the constraints are that spaces may only be followed by dots and dashes. Find the capacity of this channel in bits per unit time assuming (a) that all four symbols have equal durations; or (b) that the symbol durations are 2, 4, 3 and 6 time units respectively.

> 中文话题：把 Morse 码当成「符号时长可变 + 空格后必须跟点或划」的受约束通道，在 (a) 四符号等时长、(b) 时长分别为 2、4、3、6 两种情形下求每时间单位的容量。

> <span style="color:#1e8449;">**[译注]** (17.21) 与 (17.20) 是**同一条等式换了变量名**，但两者的约束方向相反，这一层不说清，很容易把 $\beta$ 当成某个待定常数。在 symbol code 里，$l^{*}_i$ 是**被优化出来的**（受 Kraft 不等式 $\sum_i 2^{-l_i}\le 1$ 约束），$p_i$ 是给定的；在变时长通道里，$l_i$ 是**给定的**（硬件决定），$p^{*}_i$ 是被优化出来的，而约束换成通道的转移结构（受约束时是 $A$ 的特征问题，无约束时是 $\sum_i 2^{-\beta l_i} = 1$ 这个隐式方程）。于是 (17.21) 里的 $\beta$ 不是自由参数，**它就是容量本身**：把 $p^{*}_i$ 代回去算每单位时间的信息量，得

```math
\frac{H}{\bar l} = \frac{-\sum_i p^{*}_i\log_2 p^{*}_i}{\sum_i p^{*}_i l_i} = \frac{\beta\sum_i p^{*}_i l_i}{\sum_i p^{*}_i l_i} = \beta,
```

分子里每项都是 $\beta l_i$，与分母的 $\bar l$ 正好相消——**这一步相消是整条类比的全部内容**。**失效对象**：若符号时长不等却按等时长处理（把 $\beta$ 直接写成 $\log_2\lambda$），算出的容量会偏高；Morse 通道 (b) 一问里点、划、短空、长空的时长是 $2, 4, 3, 6$，等时长近似抹掉了「短空比点还长」这个事实，答案会偏出十几个百分点。落点：本书第 4 章的 Kraft 不等式与 (4.12)、习题 6.18（书内 p.125）、习题 17.13；6.042J 的 Optimization 与约束极值（$\sum 2^{-\beta l_i} = 1$ 就是一个等式约束的极值条件）。</span>



<span style="color:#7f8c8d">书内 p.257（PDF p.269）｜ 17.7: Solutions</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 17.14.[4]**</span> How well-designed is Morse code for English (with, say, the probability distribution of figure 2.1)?

> 中文话题：用第 2 章图 2.1 的英文字母分布评价 Morse 码的设计好坏——本质是问时长分配是否接近 $p_i \propto 2^{-\beta l_i}$，即常见字母是否真拿到了短码。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 17.15.[3C]**</span> How difficult is it to get DNA into a narrow tube? To an information theorist, the entropy associated with a constrained channel reveals how much information can be conveyed over it. In statistical physics, the same calculations are done for a different reason: to predict the thermodynamics of polymers, for example.

> 中文话题：把「DNA 挤进窄管」翻译成一个受约束通道的容量问题——管壁把一维随机游走限制在宽度 $L$ 内，熵的减少量换成自由能，就是把它推进管里需要的力。

作为玩具例子，考虑一个长度 $N$ 的聚合物，它可以待在宽度为 $L$ 的约束管里，也可以在管外无约束的开阔处。在开阔处，聚合物从一维随机游走的集合里随机取一个状态，譬如说每步有 3 个可能方向。这个游走的熵是每步 $\log 3$，总共 $N\log 3$。[聚合物的自由能定义为 $-kT$ 乘以这个量，其中 $T$ 是温度。] 在管子里，聚合物的一维游走同样有 3 个方向，除非撞上管壁，所以连接矩阵是（例如 $L = 10$ 时）

```math
A_{\text{tube}} = \begin{bmatrix}1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\ 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0\\ 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0\\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0\\ 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0\\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1\end{bmatrix}.
```

[Figure 17.10：DNA 被挤在窄管里的模型。管子把 DNA 的一维游走限制在宽度 $L$ 内；管外游走有更大的熵，所以 DNA 有从管里跑出去的趋势。文字层里这幅图只剩图注与一根竖直的管状线，**箭头与分子形状无法复原**。]

现在，这个聚合物的熵是多少？聚合物进入管内造成的熵变是多少？如有可能，给出作为 $L$ 的函数的表达式。用计算机求某个具体 $L$（例如 20）下游走的熵，并画出聚合物在管内横向位置的概率密度。

注意两个通道——一个受约束、一个无约束——capacity 之差，正比于把 DNA 拉进管里所需的力。

> <span style="color:#1e8449;">**[译注]** 这个 $10\times10$ 矩阵的谱可以用**一行公式**写出来，值得当场验，因为它是本章唯一「物理量直接等于对数」的算例。它是三对角矩阵：对角全 1、次对角全 1（两端各缺一项，这正是「管壁挡住」的边界条件）；这类矩阵的特征值是

```math
\lambda_k = 1 + 2\cos\frac{k\pi}{L+1},\qquad k = 1,\ldots,L,
```

最大者 $\lambda_1 = 1 + 2\cos\frac{\pi}{11} = 2.918986$，于是管内熵是 $\log_2 2.918986 = 1.5455$ 比特/步；管外是 $\log_2 3 = 1.5850$，**每步差 $0.0395$ 比特**。$L = 20$ 时 $\lambda_1 = 2.977662$、熵 $1.5742$，每步只差 $0.0108$——**管加宽一倍，熵亏欠掉到约四分之一**（$0.0395/0.0108 \approx 3.7$，方向上符合 $\lambda_1 \approx 3 - (\pi/(L+1))^2$ 的 $L^{-2}$ 律：$L=10$ 时 $3 - 0.0816 = 2.918$ ✓）。**失效对象**：若把边界条件写成周期的（首尾也连上 1），特征值变成 $1 + 2\cos(2\pi k/L)$，$\lambda_1$ 会是 3 而不是 2.919，**熵差归零、管子对 DNA 毫无约束力**，「力正比于 capacity 之差」会直接把力算成 0。这条正好说明：物理上的「壁」在矩阵里就是一个缺失的次对角元素。落点：本书习题 17.15、§17.3 的容量定义；Strang 线代第 6 章（三对角矩阵与差分方程，特征值 $a + 2\sqrt{bc}\cos\theta$ 是同一套推导）；6.006 的 Matrix exponentiation（$A^N$ 的主导项）。</span>

### 17.7 Solutions（解答）

**Solution to exercise 17.5（书内 p.250，PDF p.262）。** 由 C2 传送的文件平均含三分之一的 1、三分之二的 0。若 $f = 0.38$，1 的比例是 $f/(1+f) = (\gamma - 1.0)/(2\gamma - 1.0) = 0.2764$。

**Solution to exercise 17.7（书内 p.254，PDF p.266）。** 把通道 A 的合法串先取反 [1→0；0→1]，再送过 accumulator，就得到通道 C 的合法串。这些操作都可逆，所以 C 的任意合法串也能映回 A 的合法串。唯一的保留意见来自**边界效应**：如果我们假定通道 C 发送的第一个字符前面是一串 0，从而第一个字符被迫为 1（图 17.5c），那么只有再假定通道 A 的第一个字符必须是 0，两个通道才严格等价。

**Solution to exercise 17.8（书内 p.254，PDF p.266）。** 在 $N = 16$ 个发送比特下，能编码的信源比特最大整数是 10，所以 $N = 16$ 的定长码的最大码率是 0.625。

> <span style="color:#1e8449;">**[译注]** 解答 17.8 的「10 比特」若不核一遍，读者会以为作者在暗示「$N$ 翻倍、码率不变」，而事实恰好相反：**定长码的码率随 $N$ 单调爬向 $0.694$ 但永远到不了**。数一下：终止于状态 0 的长度 16 串有多少条？由 $M_n = F_{n+2}$ 且「终止于状态 0」的计数恰好是 $M_{n-1}$（每条长度 $n$ 的路径都唯一对应一条长度 $n-1$ 的、末尾补 0 的路径），得 $M_{15} = F_{17} = 1597$，而 $2^{10} = 1024 \le 1597 \lt 2^{11} = 2048$，故能装 10 比特、码率 $10/16 = 0.625$ ✓。同法算：$N=8$ 时 $M_7 = F_9 = 34 \ge 32$，装 5 比特、码率 $0.625$；$N = 32$ 时 $F_{33} = 3524578 \ge 2^{21}$，装 21 比特、码率 $0.656$；$N = 64$ 时装 44 比特、码率 $0.688$。**失效对象**：若把「$\lfloor\log_2 M_{N-1}\rfloor$ 个整数比特」当成容量估计，$N=16$ 得 $0.625$，与真值差 $0.069$ 比特（10% 相对误差）；而这个差**不是**逼近误差，是「定长 + 整数比特」两层离散化叠加的结果，两层都要在 $N\to\infty$ 才同时归零。落点：本书习题 17.8 及其解答、表 17.6、§17.5 的 enumerative code；6.042J 的 Counting（$\lfloor\log_2 M\rfloor$ 的取整损失）；6.006 的 Dynamic Programming（用递推而非枚举数 $M_n$）。</span>



<span style="color:#7f8c8d">书内 p.258（PDF p.270）｜ 17 — Communication over Constrained Noiseless Channels</span>

**Solution to exercise 17.10（书内 p.255，PDF p.267）。** 设不变分布为

```math
P(s) = \alpha\, e^{(L)}_s e^{(R)}_s, \qquad (17.22)
```

其中 $\alpha$ 是归一化常数。这里 $S_t$ 与第 4 章一样，表示随机变量为状态 $s_t$ 的那个 ensemble（集合）。给定 $S_{t-1}$ 时 $S_t$ 的熵（假定 $S_{t-1}$ 服从不变分布）是

```math
H(S_t \mid S_{t-1}) = -\sum_{s,s'} P(s)P(s'|s)\log P(s'|s) \qquad (17.23)
```

```math
= -\sum_{s,s'} \alpha e^{(L)}_s e^{(R)}_s \frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s}\log\frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s} \qquad (17.24)
```

```math
= -\sum_{s,s'} \frac{\alpha}{\lambda}\, e^{(R)}_s e^{(L)}_{s'}A_{s's}\left[\log e^{(L)}_{s'} + \log A_{s's} - \log\lambda - \log e^{(L)}_{s}\right]. \qquad (17.25)
```

现在，$A_{s's}$ 不是 0 就是 1，所以正比于 $A_{s's}\log A_{s's}$ 的那些项全为零。于是

```math
H(S_t\mid S_{t-1}) = \log\lambda + \frac{-\alpha}{\lambda}\sum_{s'}\left(\sum_s A_{s's}e^{(R)}_s\right)e^{(L)}_{s'}\log e^{(L)}_{s'} + \frac{\alpha}{\lambda}\sum_s\left(\sum_{s'}e^{(L)}_{s'}A_{s's}\right)e^{(R)}_s\log e^{(L)}_s \qquad (17.26)
```

```math
= \log\lambda - \frac{\alpha}{\lambda}\sum_{s'}\lambda e^{(R)}_{s'}e^{(L)}_{s'}\log e^{(L)}_{s'} + \frac{\alpha}{\lambda}\sum_s \lambda e^{(L)}_s e^{(R)}_s\log e^{(L)}_s \qquad (17.27)
```

```math
= \log\lambda. \qquad (17.28)
```

**Solution to exercise 17.11（书内 p.255，PDF p.267）。** 这两个通道连接矩阵的主特征值是 1.839 与 1.928。capacity（$\log\lambda$）分别是 0.879 与 0.947 比特。

**Solution to exercise 17.12（书内 p.256，PDF p.268）。** 这个通道与无约束二元通道相似：$L$ 大时长度超过 $L$ 的游程很罕见，所以只能期望它与无约束通道有**微弱**差别；这些差别会出现在游程长度接近 $L$ 的上下文里。该通道的 capacity 非常接近一比特。

一个 capacity 的下界来自这个通道的一个简单变长码：把最长游程串 `111...1` 替换成 `111...10`，其余信源文件原样不动。这个码的平均码率是 $1/(1 + 2^{-L})$，因为不变分布会有 $2^{-L}$ 的比例落在「多加一个零」这个状态上。

我们可以复用习题 6.18（书内 p.125）里变长通道的解答。capacity 就是满足方程

```math
Z(\beta) = \sum_{l=1}^{L+1} 2^{-\beta l} = 1 \qquad (17.29)
```

的那个 $\beta$。求和里的 $L+1$ 项对应可以发出的 $L+1$ 种串：`0`、`10`、`110`、…、`11...10`。这个和恰好是

```math
Z(\beta) = 2^{-\beta}\,\frac{\left(2^{-\beta}\right)^{L+1} - 1}{2^{-\beta} - 1}. \qquad (17.30)
```

> <span style="color:#1e8449;">**[译注]** (17.28) 是本章最干净的一次「所有归一化项互相抵消」，但要记住它的**成立条件**：$A_{s's}$ 只取 0/1。若把矩阵换成带权重的版本（符号代价不等，或某些转移要付两拍时间），$\log A_{s's}$ 那组项不再为零，$H = \log\lambda$ 退化成

```math
H(S_t\mid S_{t-1}) = \log\lambda - \sum_{s,s'} P(s)Q_{s'|s}\log A_{s's},
```

多出来的那一项正是「每次转移的额外时间代价」的期望——**这就是 §17.6 变时长通道为什么不能直接用 $\log_2\lambda$ 当容量的代数原因**。另一条可验的细节：$A_{s's}\log A_{s's}$ 在 $A = 0$ 处按极限取 $0$（$x\log x\to 0$），这个约定不是偷懒，而是「不存在的边不贡献熵」。**失效对象**：若忽略 0/1 假设直接套 (17.28) 去算 Morse 通道，$\beta$ 会算成等时长值 $\log_2\lambda$，与 (b) 一问要求的 $2,4,3,6$ 时长答案差出一截；反过来，若把所有 $A_{s's}$ 都当 1（无视缺失的边），$H$ 会算成 $\log\lambda - \log 1 = \log\lambda$ 但仍会漏掉「某些转移根本不可用」对熵的实际削减。落点：本书 (17.23)–(17.28)、§17.6、习题 17.13；6.042J 的 Entropy 与期望的线性性；6.006 的 Randomized algorithms（条件熵的链式法则）。</span>



<span style="color:#7f8c8d">书内 p.259（PDF p.271）｜ 17.7: Solutions</span>

（承接上页，这里用到等比级数求和公式 $\sum_{n=0}^{N} ar^{n} = a(r^{N+1} - 1)/(r - 1)$。）我们预期 $\beta$ 应当略小于 1，才能使 $Z(\beta)$ 等于 1。整理并按 $\ln(1 + x) \simeq x$ 近似解出 $\beta$：

```math
Z(\beta) = 1 \qquad (17.31)
```

```math
\Rightarrow \beta \simeq 1 - 2^{-(L+2)}/\ln 2. \qquad (17.32)
```

我们在前面的习题里算过 $L = 2$ 与 $L = 3$ 的真实 capacity。下表把近似 capacity $\beta$ 与真实 capacity 作比较：

| $L$ | $\beta$（近似，(17.32)） | True capacity（真值） |
|---|---|---|
| 2 | 0.910 | 0.879 |
| 3 | 0.955 | 0.947 |
| 4 | 0.977 | 0.975 |
| 5 | 0.9887 | 0.9881 |
| 6 | 0.9944 | 0.9942 |
| 9 | 0.9993 | 0.9993 |

元素 $Q_{1|0}$ 会接近 $1/2$（只是略微大一点），因为在无约束二元通道里 $Q_{1|0} = 1/2$。当已经出现长度为 $L - 1$ 的游程时，我们实际上有「打印 `10`」与「打印 `0`」两个选择。设选择 `10` 的概率为 $f$。我们估计流中其余 $N$ 个字符的熵作为 $f$ 的函数，同时假定 $Q$ 的其余部分都已取最优值。流中随后 $N$ 个字符的熵，等于第一个比特的熵 $H_2(f)$ 加上其余字符的熵——若第一个比特选 0，其余字符的熵大约是 $(N-1)$ 比特；若选 1，则是 $(N-2)$ 比特。更精确地说，若 $C$ 是该通道的 capacity（大约为 1），

```math
\begin{aligned}
H(\text{the next } N \text{ chars}) &\simeq H_2(f) + \left[(N-1)(1-f) + (N-2)f\right]C\\
&= H_2(f) + NC - fC \simeq H_2(f) + N - f. \qquad (17.33)
\end{aligned}
```

求导并令其为零以找出最优的 $f$，得到：

```math
\log_2\frac{1-f}{f} \simeq 1 \;\Rightarrow\; \frac{1-f}{f} \simeq 2 \;\Rightarrow\; f \simeq 1/3. \qquad (17.34)
```

于是，随着已发出的 1 的个数增加，发出 1 的概率从约 $0.5$ 降到约 $1/3$。下面是最优矩阵：

```math
Q = \begin{bmatrix}0.6666 & 0.3334 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 0.5713 & 0 & 0.4287 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 0.5331 & 0 & 0 & 0.4669 & 0 & 0 & 0 & 0 & 0 & 0\\ 0.5159 & 0 & 0 & 0 & 0.4841 & 0 & 0 & 0 & 0 & 0\\ 0.5077 & 0 & 0 & 0 & 0 & 0.4923 & 0 & 0 & 0 & 0\\ 0.5037 & 0 & 0 & 0 & 0 & 0 & 0.4963 & 0 & 0 & 0\\ 0.5017 & 0 & 0 & 0 & 0 & 0 & 0 & 0.4983 & 0 & 0\\ 0.5007 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0.4993 & 0\\ 0.5002 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0.4998\\ 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\end{bmatrix}. \qquad (17.35)
```

我们这套粗略的理论管用。

> <span style="color:#1e8449;">**[译注]** 上表与 (17.35) 值得各验一次，因为它们是「近似—真值」对照里少见的**两端都能核**的例子。先核 $\beta$ 列：把 (17.32) 直接代入 $L = 2,3,4,5,6,9$，得 $1 - 2^{-4}/\ln 2 = 0.9098$、$0.9549$、$0.9775$、$0.9887$、$0.9944$、$0.9993$，与表中 $\beta$ 列逐格吻合，且 $L=4$ 时近似与真值只差 $0.002$、$L=9$ 时差小于 $0.0001$——**误差按 $2^{-L}$ 衰减，与「只有游程撞到上限才产生差别」这个物理图像一致**。再核 (17.35)：这个 $10\times10$ 矩阵**行随机**，除末行外每行两个非零元 $(q, 1-q)$，逐行相加得 $0.6666+0.3334 = 0.5713+0.4287 = 0.5331+0.4669 = 1.0000$ ✓（九行全部成立），末行 $Q_{0|9} = 1$（已连发 9 个 1，必须发 0）✓。**失效对象**：若把 (17.34) 的 $\log_2$ 误用成自然对数，$f$ 会算成 $(1+e^{-1})^{-1} = 0.731$，与 $1/3$ 差一倍多，整个 $Q$ 的对角线（$0.3334$ 到 $0.4998$ 那一列）会整条偏掉，而**行和仍为 1、特征值仍为 $\lambda$**——所以单靠「矩阵合法」检查不出来，必须回到 $f$ 的定义处核。落点：本书 (17.30)–(17.35)、习题 17.12 及其解答、习题 6.18（书内 p.125）；6.042J 的 Geometric series 与 Taylor 近似；6.006 的数值求根（$Z(\beta)=1$ 是一维根）。</span>



<span style="color:#7f8c8d">书内 p.260（PDF p.272）｜ 第 18 章首页</span>

## 第 18 章 Crosswords and Codebreaking（纵横字谜与密码破译）

本章我们在与 language modelling（语言建模）有关的几个题目上做一次随机游走。

### 18.1 Crosswords（纵横字谜）

纵横字谜的造法规则可以看成在定义一个 constrained channel（受约束通道）。**很多合法的字谜能被造出来**这一事实，说明这个受约束通道的 capacity 大于零。

[Figure 18.1：一幅 type A（美式）与一幅 type B（英式）纵横字谜。文字层里能读出成串的大写字母（例如 `ABELOSS`、`AMUMPAHS`、`SERTS`、`LIVES` 等片段，均可在 fitz 抽取结果中逐字核对），但**这些字母在网格中的行列位置无法复原**——PDF 把每个格子里的字母当独立文本块抽出，行序与列序全部丢失。故此处不重建网格，只按原图标注。]

有两种原型化的纵横字谜格式。在「type A」（或美式）字谜里，每一行与每一列都由若干个长度 $\ge 2$ 的词组成，词之间用一个或多个空格隔开。在「type B」（或英式）字谜里，每一行与每一列都是词与**单个字符**的混合，用一个或多个空格隔开，并且每个字符至少落在一个词（横向或纵向）里。type A 字谜里每个字母同时属于一个横向词和一个纵向词；而典型的 type B 字谜里只有大约一半字母如此，另一半只属于一个词。

type A 字谜比 type B 更难造，因为「不允许单个字符」这条约束更紧。type B 字谜通常更难解，因为每个字符上的约束更少。

### Why are crosswords possible?（为什么字谜是可能的？）

如果一个语言没有 redundancy（冗余），那么写在网格上的任何字母都构成合法字谜。反之，在一个冗余度很高的语言里，字谜很难造（也许只能造出少数几个平凡的例子）。因此，**在某个语言里能造出字谜**这件事，本身就证明了该语言冗余度的一个上界。字谜一般不是用真正的英语写的，而是用「word-English」——由字典里的词组成、词间用空格分隔的那种语言。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 18.1.[2]**</span> Estimate the capacity of word-English, in bits per character. [Hint: think of word-English as defining a constrained channel (Chapter 17) and see exercise 6.18 (p.125).]

> 中文话题：估计 word-English 的每字符容量——把「词 + 空格」看成变长符号（符号时长 = 词长 + 1），用第 17 章的 $\sum_i 2^{-\beta l_i} = 1$ 求解。

大量字谜可造这一事实，给出 word-English 熵的一个**下界**。为简单起见，我们用一个模型来代表 word-English，即 §4.1 引入的 Wenglish：由 $W$ 个长度全为 $L$ 的词构成的语言。这种语言每字符（含词间空格）的熵是

```math
H_W \equiv \frac{\log_2 W}{L + 1}. \qquad (18.1)
```

> <span style="color:#1e8449;">**[译注]** 把「造字谜」翻译成「受约束通道容量 $>0$」这句话，是本章唯一一次把第 17 章的机器直接搬到语言学上，值得说清它的**方向**，因为方向和直觉相反：通道容量为正 ⇒ 冗余度有**上界**，而不是下界。机制是这样：若语言完全无冗余（每字符 $\log_2 26 = 4.7$ 比特），任何字母填入都合法，字谜数按 $26^{f_1 S}$ 爆炸增长；若冗余极高（几乎只有少数几种合法填法），字谜数随面积 $S$ 指数**衰减**，只有极小尺寸的才造得出来。所以「能造出大尺寸字谜」等价于「合法填法数随 $S$ 增长」。(18.7) 给出的正是这个增长条件，而 (18.8) 把它解成 $H_W$ 的下界——注意这里出现了双重反转：**语言熵越大，字谜越容易造；但正因为字谜容易造，我们才知道语言熵不低于某个值**。**失效对象**：抽掉「每个字符同时受横向词与纵向词两重约束」这一点，二维约束就退化成两条独立的一维约束，字谜数变成 $(W^2 / 26^{L\cdot\ldots})$ 的乘积形式，$f_1 - f_wL$ 那一项变成 $f_1 - f_wL/2$，$H_W$ 的下界会松动近一倍。落点：本书 §18.1 与 (18.8)、本页末尾「Further reading」列的 Shannon (1948) 与 Wolf & Siegel (1998)；6.042J 的 Counting 与 Union bound（合法的比例即概率）。</span>



<span style="color:#7f8c8d">书内 p.261（PDF p.273）｜ 18.1: Crosswords</span>

我们会发现，最终结论只依赖 $H_W$ 的取值，对 $L$ 的取值并不特别敏感。考虑一幅面积为 $S$ 个格子的大字谜。设词的数目为 $f_wS$，被字母占据的格子数为 $f_1S$。对于由长度 $L$ 的词构成的典型 type A 与 type B 字谜，两个比例 $f_w$ 与 $f_1$ 大致取表 18.2 的值。

<span style="color:#00838f;">**Table 18.2**（词数与字母格数相对总格数的比例因子）</span>

| | A | B |
|---|---|---|
| $f_w$ | $\dfrac{2}{L+1}$ | $\dfrac{1}{L+1}$ |
| $f_1$ | $\dfrac{L}{L+1}$ | $\dfrac{3}{4}\cdot\dfrac{L}{L+1}$ |

现在用我们简陋的 Wenglish 模型估计面积 $S$ 的字谜有多少幅。我们假定 Wenglish 是这样随机生成的：从熵为 $H_0$ 的 monogram（单字符、无记忆）信源生成 $W$ 个串。例如，若该信源以等概率使用全部 $A = 26$ 个字符，则 $H_0 = \log_2 A = 4.7$ 比特；若改用第 2 章那个分布，熵是 4.2。Wenglish 的冗余来自两处：它倾向于多用某些字母；字典里只有 $W$ 个词。

现在我们来数字谜的数目：想象用**生成 Wenglish 字典的同一个分布**随机往字谜的格子里填字母，然后评估这个随机涂写「使所有行与列都成为合法词」的概率。$f_1S$ 个格子的典型填法总数是

```math
|\mathcal{T}| = 2^{f_1 S H_0}. \qquad (18.2)
```

一个长度为 $L$ 的词被合法填成的概率是

```math
\beta = \frac{W}{2^{L H_0}}, \qquad (18.3)
```

而整幅由 $f_wS$ 个词构成的字谜被**某一次**典型填法合法填成的概率约为

```math
\beta^{f_w S}. \qquad (18.4)
```

[边注原文：这个算法低估了合法 Wenglish 字谜的数目，因为它只数了用「典型」串填成的字谜。若 monogram 分布不均匀，真实计数由「非典型」填法主导，那些填法里「对字谜友好的词」出现得更频繁。]

> <span style="color:#7f8c8d">边注的中文：上述估计只统计「典型」填法，因而**低估**合法字谜数；真实计数在 monogram 分布不均匀时由非典型填法主导。</span>

于是面积 $S$ 的合法字谜数的对数估计为

```math
\log\left(\beta^{f_w S}|\mathcal{T}|\right) = S\left[(f_1 - f_w L)H_0 + f_w\log W\right] \qquad (18.5)
```

```math
= S\left[(f_1 - f_w L)H_0 + f_w(L+1)H_W\right], \qquad (18.6)
```

只有当

```math
(f_1 - f_w L)H_0 + f_w(L+1)H_W \gt 0 \qquad (18.7)
```

时，它才是 $S$ 的增函数。

所以，只有当 Wenglish 字典里词足够多、使得

```math
H_W \gt \frac{(f_w L - f_1)}{f_w(L+1)}\,H_0 \qquad (18.8)
```

时，才能造出任意多幅字谜。

把表 18.2 的 $f_1$、$f_w$ 代进去，我们得到：

| Crossword type（字谜类型） | A | B |
|---|---|---|
| Condition for crosswords（可造字谜的条件） | $H_W \gt \dfrac{1}{2}\cdot\dfrac{L}{L+1}H_0$ | $H_W \gt \dfrac{1}{4}\cdot\dfrac{L}{L+1}H_0$ |

若取 $H_0 = 4.2$ 比特、并假定一个正常英语使用者的字典里有 $W = 4000$ 个词、长度全为 $L = 5$，那么我们发现 type B 的字谜条件满足，而 type A 的条件只是**刚刚**满足。这与我自己的经验相符：type A 字谜通常包含更多生僻词。

> <span style="color:#1e8449;">**[译注]** 「type A 只是刚刚满足」这句话可以逐位复算，而且它会立刻给出一个可反驳的预测——这正是这一节最有价值的地方。代入 $W = 4000$、$L = 5$、$H_0 = 4.2$：$H_W = \log_2 4000 / 6 = 11.966/6 = 1.9943$，而两个阈值分别是 $0.5\times(5/6)\times4.2 = 1.750$ 与 $0.25\times(5/6)\times4.2 = 0.875$。所以 **type A 的裕度是 $1.9943 - 1.750 = 0.244$ 比特，type B 的裕度是 $1.119$ 比特，前者只有后者的 22%**。「刚刚满足」被量化成了 $0.244$ 比特。**可反驳的预测**：若字典规模从 4000 降到 $W = 2^{6\times1.75} = 2^{10.5} \approx 1448$ 以下，type A 字谜就完全造不出来（而 type B 要到 $W = 2^{6\times0.875} = 2^{5.25}\approx 38$ 才失效）——也就是说，「能造大尺寸美式字谜」这件事对字典规模的要求是英式的 $1448/38 \approx 38$ 倍。**失效对象**：若把 $f_1$ 的 $\frac{3}{4}$ 因子漏掉（英式字谜里有四分之一的格子只属于一个词），type B 的阈值会变成 $1.750$、与 type A 相同，那么「英式比美式容易造」这个结论就整个消失，与作者的经验冲突。落点：本书 §18.1、表 18.2、(18.8)、Shannon (1948)；6.042J 的 Counting（$|\mathcal{T}| = 2^{f_1SH_0}$ 就是计数）与 Logarithms（$W = 2^{6H_W}$ 的换算是关键一步）。</span>



<span style="color:#7f8c8d">书内 p.262（PDF p.274）｜ 18 — Crosswords and Codebreaking</span>

### Further reading（延伸阅读）

关于字谜的这些观察最早由 Shannon (1948) 提出；我是从 Wolf 与 Siegel (1998) 那里知道它们的。这个题目与二维受约束通道的 capacity 密切相关。二维受约束通道的一个例子是包裹上常见的二维条码。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 18.2.[3]**</span> A two-dimensional channel is defined by the constraint that, of the eight neighbours of every interior pixel in an $N \times N$ rectangular grid, four must be black and four white. (The counts of black and white pixels around boundary pixels are not constrained.) A binary pattern satisfying this constraint is shown in figure 18.3. What is the capacity of this channel, in bits per pixel, for large $N$?

> 中文话题：二维通道的容量——每个内部像素的 8 个邻居里恰有 4 黑 4 白；问 $N$ 很大时每像素多少比特。这是「局部约束→全局指数」的二维版本，答案不是 $1$ 比特而是低于 $1$ 的某个数（可用转移矩阵 / transfer-matrix 或数值模拟估计）。

[Figure 18.3：一个二维二值图案，其中每个像素都与四个黑像素和四个白像素相邻。文字层里该图只剩零散的黑白像素点阵碎片，**网格结构与图案无法复原**。]

### 18.2 Simple language models（简单的语言模型）

### The Zipf–Mandelbrot distribution（Zipf–Mandelbrot 分布）

对语言最粗糙的模型是 monogram 模型：它断言每个相继的词都是独立地从词上的某个分布里抽出来的。这个分布是什么性质？

Zipf 定律（Zipf, 1949）断言：语言里第 $r$ 个最常见的词，其概率约为

```math
P(r) = \frac{\kappa}{r^{\alpha}}, \qquad (18.9)
```

其中指数 $\alpha$ 的取值接近 1，$\kappa$ 是常数。按 Zipf 的说法，把频率对词秩做 log–log 图，应当得到一条斜率为 $-\alpha$ 的直线。

Mandelbrot（1982）对 Zipf 定律的修改引入第三个参数 $v$，断言概率由下式给出：

```math
P(r) = \frac{\kappa}{(r + v)^{\alpha}}. \qquad (18.10)
```

> <span style="color:#1e8449;">**[译注]** (18.10) 里那个 $v$ 不是装饰品，它保证的是**归一化可行性**，这一点决定了 $\alpha$ 的拟合值必须大于 1。若取 $v = 0$、$\alpha = 1$（Zipf 原始形式），则 $\sum_{r=1}^{W} 1/r$ 按 $\ln W$ 发散，概率只能靠**截断到词表大小 $W$** 才归一，于是

```math
\kappa(W) = \left[\sum_{r=1}^{W}\frac{1}{r+v}\right]^{-1} \approx \left[\ln\frac{W+v}{v}\right]^{-1},
```

$v = 8$、$W = 4000$ 时 $\ln(5008/8) = \ln 626 = 6.44$，$\kappa = 0.155$——注意这个 $\kappa$ **随语料规模漂移**：$W$ 从 $4000$ 涨到 $4\times10^{6}$，$\kappa$ 从 $0.155$ 掉到 $0.086$，同一作者的两份语料会给出不同的 $\kappa$。而图 18.4 拟合出 $\alpha = 1.26 \gt 1$，此时 $\sum_r (r+v)^{-\alpha}$ 收敛到与 $W$ 无关的常数（主导项 $1/(\alpha-1) = 3.85$），$\kappa$ 才是可迁移的参数。**失效对象**：若把 $\alpha$ 强行锁成 1 去拟合（Zipf 原教旨版本），$\kappa$ 就不再是语言的性质、而是语料长度的性质，跨语料比较词频会得出「同一作者的用词习惯变了」这种假结论。落点：本书 (18.9)、(18.10)、图 18.4 的拟合值（$\kappa = 0.56$、$v = 8.0$、$\alpha = 1.26$）、Mandelbrot (1982)；6.042J 的 Harmonic series 与 Integral test（$\sum 1/r$ 与 $\ln W$ 同阶）。</span>

对某些文档，例如 Jane Austen 的 *Emma*，Zipf–Mandelbrot 分布拟合得很好——见图 18.4。

[Figure 18.4：Zipf–Mandelbrot 分布 (18.10)（曲线）对 Jane Austen *Emma* 中词的经验频率（点）的拟合。拟合参数为 $\kappa = 0.56$、$v = 8.0$、$\alpha = 1.26$。可复原的刻度：纵轴概率从 $10^{-5}$ 到 $10^{3}$（十条十倍刻度），横轴秩 1 到约 $10^{4}$；横轴上标注的词含 `the`、`to`、`and`、`of`、`I`、`is`、`Harriet`、`information`。]

其他文档给出的分布则不那么符合 Zipf–Mandelbrot。图 18.5 画出的是**本书的 LaTeX 源文件**的频率对秩图。定性地看，这张图近于直线，但能看出弯曲。公平地说，这个源文件不是纯英语写的——它是英语、`x` 这类数学符号与 LaTeX 命令的混合物。



<span style="color:#7f8c8d">书内 p.263（PDF p.275）｜ 18.2: Simple language models</span>

[Figure 18.5：本书 LaTeX 文件里各词的频率对秩的 log–log 图。可复原的刻度：纵轴 $0.1$ 到 $10^{-5}$，横轴 1 到约 $10^{4}$；图上标注的词含 `the`、`of a`、`is`、`x`、`information`、`Shannon`、`Bayes`。]

[Figure 18.6：由参数 $\alpha$ 从 1 到 1000 的 Dirichlet process 随机生成的四个「语言」的 Zipf 图（$\alpha = 1, 10, 100, 1000$），并画出本书的 Zipf 图作对照。横轴标注 `book`。刻度：纵轴 $0.1$ 到 $10^{-5}$，横轴 1 到约 $10^{4}$。]

### The Dirichlet process（Dirichlet 过程）

假定我们对语言的 monogram 模型感兴趣，那么该用什么模型？给语言建模的一个困难是**词表无界**：语言的样本越大，遇到的词就越多。

语言的生成模型应当模仿这一性质。若有人问「在一部新发现的莎士比亚作品里，下一个词是什么？」，我们给出的词分布里，必须给莎士比亚从未用过的词留出非零概率。我们的生成式 monogram 模型还应当满足一条称为 exchangeability（可交换性）的一致性规则：如果我们想象用这个模型生成一种新语言、产出一个不断增长的文本语料，那么文本的所有统计性质都应当是齐性的——在文本流的任何位置，某个特定词出现的概率都应当相同。

Dirichlet process 模型描述一个符号流（我们把符号想成「词」），它满足可交换性规则，并且允许符号的词表无限增长。该模型有一个参数 $\alpha$。随着符号流被生成，我们用唯一的整数 $w$ 标识每个新符号。当我们已经看到长度为 $F$ 的符号流后，用目前已有的计数 $\{F_w\}$ 来定义下一个符号的概率：下一个符号是一个**从未见过的新符号**的概率是

```math
\frac{\alpha}{F + \alpha}. \qquad (18.11)
```

下一个符号是符号 $w$ 的概率是

```math
\frac{F_w}{F + \alpha}. \qquad (18.12)
```

图 18.6 画出了由 $\alpha$ 取 1 到 1000 的 Dirichlet process 先验生成的百万符号「文档」的 Zipf 图（即符号频率对秩的图）。

显然，Dirichlet process 不足以作为「近似服从 Zipf 定律」的观测分布的模型。

> <span style="color:#1e8449;">**[译注]** 「Dirichlet process 不够用」这个结论有个**可以当场算出来**的原因，不必靠看图：(18.12) 意味着第 $r$ 个词的期望频率由「它第一次出现的位置」决定，而 (18.11) 决定了新词出现的节奏——$\alpha/(F+\alpha)$ 关于 $F$ 是 $1/F$ 型衰减，于是词表大小按 $K(F) \approx \alpha\ln(1 + F/\alpha)$ 对数增长，而**已见词的频率分布很快被经验计数锁死**，尾部的衰减比幂律快得多。具体数：$\alpha = 1$、$F = 10^{6}$ 时，新词概率是 $10^{-6}$，词表约 $1\times\ln(10^{6}) = 13.8$ 个词；$\alpha = 1000$、$F = 10^{6}$ 时新词概率 $10^{-3}$，词表约 $1000\ln(1001) = 6908$ 个——但**最高频词与第 100 名之间的比值**在图 18.6 里只有几个量级，而真实英语（图 18.4）跨了 $10^{4}$ 量级。**失效对象**：若把 $\alpha$ 调小来「拟合」Zipf 的斜率，$Z$ 尾部的词会迅速消失（$\alpha=1$ 时总共只有十几个词），图上会出现明显的截断——这就是图 18.6 里四条曲线都是「弯的」而不是直线的量化原因。作者随后用「在字符级上跑 DP、再宣布某个字符为空格」这一手修正，恰好把「词的边界」也变成随机变量，曲线才变直。落点：本书 §18.2、图 18.6、图 18.7；6.042J 的 Expectation（$K(F)$ 的调和级数近似 $\sum 1/F \approx \ln F$）；统计学侧的 Pólya urn 模型（同一递推）。</span>



<span style="color:#7f8c8d">书内 p.264（PDF p.276）｜ 18 — Crosswords and Codebreaking</span>

[Figure 18.7：两个「语言」的词的 Zipf 图——先由 $\alpha = 2$ 的 Dirichlet process 逐个生成字符，再宣布某个字符为空格字符；两条曲线来自两种不同的空格字符选择。刻度：纵轴 $0.1$ 到 $10^{-5}$，横轴 1 到约 $10^{4}$。]

不过，只要稍作调整，Dirichlet process 就能产生相当漂亮的 Zipf 图。想象用参数 $\alpha$ 相当小的 Dirichlet process 生成一个由**基本符号**构成的语言，使相当频繁的符号大约有 27 个。如果我们随后宣布其中一个符号（现在它们该叫「字符」而不是「词」）为空格字符，那么就可以把空格字符之间的串认定为「词」。这样生成的语言，其词频常常给出非常漂亮的 Zipf 图，如图 18.7 所示。**选哪个字符当空格字符，决定了 Zipf 图的斜率**——一个更不频繁的空格字符会产生更丰富的语言，斜率更浅。

### 18.3 Units of information content（信息量的单位）

一个结果 $x$ 的信息量，在其概率为 $P(x)$ 时定义为

```math
h(x) = \log\frac{1}{P(x)}. \qquad (18.13)
```

一个 ensemble（集合）的熵是平均信息量

```math
H(X) = \sum_x P(x)\log\frac{1}{P(x)}. \qquad (18.14)
```

当我们借助数据来比较各个 hypothesis（假设）时，往往方便的做法是比较各备择假设下数据的概率的对数：

```math
\text{`log evidence for } H_i\text{' } = \log P(D \mid H_i), \qquad (18.15)
```

或者，在只比较两个假设时，我们计算「log odds」（对数几率）：

```math
\log \frac{P(D \mid H_1)}{P(D \mid H_2)}, \qquad (18.16)
```

它也被称为「支持 $H_1$ 的 weight of evidence（证据权重）」。

一个假设的 log evidence $\log P(D\mid H_i)$ 是数据 $D$ 的信息量的**负数**：若给定某个假设时数据的信息量很大，那么这些数据对该假设而言是令人吃惊的；若另一个假设对这批数据不那么吃惊，那个假设就变得更可能。「信息量」「惊讶值」以及 log likelihood 或 log evidence 是同一件事。

所有这些量都是概率的对数、或者概率对数的加权和，所以它们都能用同一套单位度量。单位取决于对数底的选取。给这些单位起的名字见表 18.8。



<span style="color:#7f8c8d">书内 p.265（PDF p.277）｜ 18.4: A taste of Banburismus</span>

<span style="color:#00838f;">**Table 18.8**（信息量的度量单位）</span>

| Unit | Expression that has those units |
|---|---|
| bit | $\log_2 p$ |
| nat | $\log_e p$ |
| ban | $\log_{10} p$ |
| deciban (db) | $10\log_{10} p$ |

bit 是本书最常用的单位。因为「bit」一词另有含义，这个单位的备用名是 shannon。一个 byte 是 8 bit。一个 megabyte 是 $2^{20} \simeq 10^{6}$ byte。若用自然对数，信息量与证据权重就用 nat 度量。最有趣的单位是 ban 与 deciban。

### The history of the ban（ban 的历史）

让我告诉你为什么「概率相差十倍」被称为一个 ban。当 Alan Turing 与 Bletchley Park 的其他密码破译者破解每一天新的 Enigma 密码时，他们的任务是一个巨大的 inference（推断）问题：给定当天的密文，推断当天 Enigma 机器里装的是哪三个轮子、它们的起始位置是什么、steckerboard（接线板）上还用了哪些字母替换，以及——同样重要——原始的德语消息是什么。这些推断是用 Bayesian 方法做的（当然！），所选单位是 deciban 或半个 deciban，因为人们判断 deciban 是人类能分辨的最小证据权重。支持特定假设的证据用**专门在 Banbury 印刷的纸**来记账——Banbury 是距 Bletchley 约 30 英里的一座城。这个推断任务被称为 Banburismus，而玩 Banburismus 所用的单位就叫 ban，取自那座城的名字。

### 18.4 A taste of Banburismus（Banburismus 一瞥）

Bletchley Park 的密码破译方法的细节被保密了很长时间，但 Banburismus 的某些方面还是能被拼凑出来。我希望下面这段对 Banburismus 一小部分的描述不至于太不准确。<sup>1</sup>

> <span style="color:#7f8c8d">脚注 1 原文：I've been most helped by descriptions given by Tony Sale (http://www.codesandciphers.org.uk/lectures/) and by Jack Good (1979), who worked with Turing at Bletchley.</span>
>
> 脚注 1 的中文：我受惠最多的是 Tony Sale 的描述（http://www.codesandciphers.org.uk/lectures/）以及 Jack Good（1979）的叙述，后者在 Bletchley 与 Turing 共事。

需要多少信息？Enigma 机器的可能设置约有 $8\times 10^{12}$ 种。要推出机器的状态，「therefore it was necessary to find about 129 decibans from somewhere」（如 Good 所说）。Banburismus 的目标**不是**推出机器的全部状态，而只是弄清当时用的是哪几个轮子；随后再让基于逻辑的 bombes（炸弹机）去吃 plaintext 猜测（cribs），破解轮子的设置到底是什么。

Enigma 机器一旦装好轮子与插线，就实现了一个不断变化的 permutation cypher（置换密码），它确定性地在一个 $26^{3}$ 个置换组成的状态空间里游走。由于每天发送的消息数量极大，很有可能：一台机器发送某条消息的某个字符时处于某个状态，而另一台机器在发送另一条消息的某个字符时也处在同一状态。由于机器状态的演化是确定性的，这两台机器在此后的整个传输过程中会一直保持同状态。

> <span style="color:#1e8449;">**[译注]** 129 decibans 这个数字不是文献里的传说，它**恰好等于 $8\times10^{12}$ 的对数**，值得当场核一次，因为它是全章唯一把「信息量单位」与「工程数字」直接对上的地方。$1\ \text{ban} = 10\ \text{db}$，而 $\log_{10}(8\times10^{12}) = \log_{10}8 + 12 = 0.903 + 12 = 12.903$ ban $= 129.03$ db ✓。也就是说：**「从 $8\times10^{12}$ 个等可能设置里唯一定出一个」所需的信息量，恰好就是要把它压到 1 所需的证据量**。同一个数换个说法：若每条消息只提供 $1.4$ db（下一节的估计），要凑够 $129$ db 需要 $129/1.4 \approx 92$ 段 20 字符的比对，也就是约 $1840$ 个字符——这与文末「大约需要检查 400 个字符才能达到 100:1」并不矛盾，因为那里算的是**单条假设判别**的证据，而这里是**在 $8\times10^{12}$ 个假设里选一个**（后者还要乘上假设数的对数）。**失效对象**：若把 deciban 当成「$\log_{10}$ 而不再乘 10」，$8\times10^{12}$ 会算成 12.9 db，所需的证据量差 10 倍，整套账目全乱——这正是 Bletchley 的人用「半 deciban」记账时要特别小心的单位约定。落点：本书表 18.8、§18.4、Good (1979)（见 §18.4 开头的脚注 1）；6.042J 的 Logarithms（换底公式）；本书 §18.4 后面 1.4 db/20 字符的估计。</span>



<span style="color:#7f8c8d">书内 p.266（PDF p.278）｜ 18 — Crosswords and Codebreaking</span>

由此产生的一对机器输出之间的相关性，提供了一点点信息量的细流，Turing 与同事们正是从这点细流里每天榨出他们那 129 decibans。

### How to detect that two messages came from machines with a common state sequence（怎样检测两条消息来自具有共同状态序列的机器）

这里有两个假设：null hypothesis（零假设）$H_0$ 声称两台机器处在**不同**状态，两条明文互不相关；「match」假设 $H_1$ 声称两台机器处在**同一**状态，而两条明文互不相关。这里**不**试图推断任何一台机器的状态是什么。提供的数据是两段密文 $x$ 与 $y$；假定它们长度都是 $T$、字母表大小为 $A$（Enigma 里是 26）。给定这两个假设，数据的概率是多少？

先看零假设。该假设断言两段密文由下式给出：

```math
x = x_1x_2x_3\ldots = c_1(u_1)c_2(u_2)c_3(u_3)\ldots \qquad (18.17)
```

```math
y = y_1y_2y_3\ldots = c'_1(v_1)c'_2(v_2)c'_3(v_3)\ldots, \qquad (18.18)
```

其中码 $c_t$ 与 $c'_t$ 是两个互不相关、随时间变化的字母表置换，$u_1u_2u_3\ldots$ 与 $v_1v_2v_3\ldots$ 是明文消息。精确计算数据 $(x,y)$ 的概率需要明文的语言模型与 Enigma 机器内部结构的模型；但若假定每台 Enigma 机器都是一个理想的随机时变置换，那么两段密文的概率分布就是均匀的。所有密文等可能。

```math
P(x, y \mid H_0) = \left(\frac{1}{A}\right)^{2T} \quad \text{for all } x, y \text{ of length } T. \qquad (18.19)
```

> <span style="color:#1e8449;">**[译注]** (18.23) 的两个分支不是随手写的，它们必须让 $x_t$ 的**边缘分布仍是均匀的** $1/A$，否则 (18.19) 与 (18.23) 的似然比会带上一个虚假的 $O(1)$ 因子。当场验一次边缘：

```math
P(x_t = a \mid H_1) = \frac{m}{A} + (A-1)\cdot\frac{1-m}{A(A-1)} = \frac{m}{A} + \frac{1-m}{A} = \frac{1}{A},
```

代入 $A = 26$、$m = 0.076$：$0.076/26 + 0.924/26 = 0.002923 + 0.035538 = 0.038461 = 1/26$ ✓。**这个自洽性是整节证据账目的基础**：H1 与 H0 下密文的**边缘**都是均匀的（单看一段密文毫无线索），全部判别力都藏在**共轭**（同一置换）带来的相关性里——这就是为什么必须比对两段密文、而不能单独分析一段。**失效对象**：若把不匹配分支的分母写成 $A^{2}$（漏掉 $A-1$ 这个「不能用同一个字母」的因子），边缘会变成 $m/A + (1-m)/A \cdot A/(A-1) = 1/A \cdot 1/(1-1/A) = 1/(A-1)$，H1 下的似然比整体高估 $A/(A-1) = 1.04$ 倍；单个位置的 0.17 db 偏差在 74 个位置累积成约 12 db——足以把「20 db 才敢下结论」的判定翻倒。落点：本书 (18.19)、(18.22)、(18.23)、表 18.9 与随后的数值表；6.042J 的 Conditional probability（全概率公式与边缘化）。</span>

那 $H_1$ 呢？该假设断言有一个**共同的**时变置换 $c_t$ 同时支配

```math
x = x_1x_2x_3\ldots = c_1(u_1)c_2(u_2)c_3(u_3)\ldots \qquad (18.20)
```

与

```math
y = y_1y_2y_3\ldots = c_1(v_1)c_2(v_2)c_3(v_3)\ldots. \qquad (18.21)
```

数据 $(x,y)$ 的概率是多少？我们必须对明文语言做若干假定。如果明文语言完全是随机的，那么 $u_1u_2u_3\ldots$ 与 $v_1v_2v_3\ldots$ 的概率均匀，$x$ 与 $y$ 也就均匀，于是 $P(x,y\mid H_1) = P(x,y\mid H_0)$，两个假设 $H_0$ 与 $H_1$ 就**不可区分**。

我们的进展来自假定明文**不**完全随机。两段明文都是用某种语言写的，而那种语言有冗余。例如假定某些明文字母用得比别的多。于是，尽管两条明文互不相关，它们**碰巧用到相同字母**的可能性仍略高于均匀情形；若 $H_1$ 为真，两段密文里**同步位置**上的两个字母就略微更可能相同。类似地，若某种语言频繁使用特定的 bigram 与 trigram，那么两条明文偶尔会在同一时刻包含相同的 bigram 与 trigram；若 $H_1$ 为真，



<span style="color:#7f8c8d">书内 p.267（PDF p.279）｜ 18.4: A taste of Banburismus</span>

就会产生一小簇 2 到 3 个相同字母。表 18.9 展示了这样一次巧合：两条明文互不相关，只是都用英语写成。

<span style="color:#00838f;">**Table 18.9**（两段对齐的英文明文 $u$ 与 $v$，匹配处用 `*` 标出）</span>

```
u  LITTLE-JACK-HORNER-SAT-IN-THE-CORNER-EATING-A-CHRISTMAS-PIE--HE-PUT-IN-H
v  RIDE-A-COCK-HORSE-TO-BANBURY-CROSS-TO-SEE-A-FINE-LADY-UPON-A-WHITE-HORSE
matches: .*....*..******.*..............*...........*................*...........
```

注意这里有十二处匹配，其中包含一段连续六个的匹配；而两条完全随机的长度 $T = 74$ 的串，期望匹配数只有约 3。两台处在相同状态的机器所对应的两段密文，也会有这十二处匹配。

> 说明：上表第三行的匹配标记原书共 74 个字符，文字层抽取时个别位置的对齐空格有丢失，**`*` 的个数（12）与最长连续段（6）可从原文文字层确认**，但逐字符对齐位置无法完全复原，故此处按可见内容转写。

密码破译者在一对对消息里寻找**可疑地相似**的那些对，数出匹配的 monogram、bigram、trigram 等的个数。这个方法最早由波兰密码破译者 Rejewski 使用。

让我们看 monogram 语言模型这个简单情形，并估计需要多长的消息才能判定两台机器是否在同一状态。我假定源语言是 monogram-English，即相继字母独立同分布地抽自图 2.1 的概率分布 $\{p_i\}$。

$x$ 与 $y$ 的概率是不均匀的：考虑两个单字符 $x_t = c_t(u_t)$ 与 $y_t = c_t(v_t)$，它们相同的概率是

```math
\sum_{u_t,v_t} P(u_t)P(v_t)\,[u_t = v_t] = \sum_i p_i^{2} \equiv m. \qquad (18.22)
```

我们给这个量取名 $m$，意思是「match probability（匹配概率）」；对英语与德语，$m$ 都约为 $2/26$ 而不是 $1/26$（后者是完全随机语言的值）。假定 $c_t$ 是理想随机置换，那么由对称性，

```math
P(x_t, y_t \mid H_1) = \begin{cases} \dfrac{m}{A} & \text{if } x_t = y_t\\[6pt] \dfrac{1-m}{A(A-1)} & \text{for } x_t \neq y_t. \end{cases} \qquad (18.23)
```

给定长度为 $T$、在 $M$ 处匹配、在 $N$ 处不匹配的一对密文 $x$ 与 $y$，支持 $H_1$ 的 log evidence 是

```math
\log\frac{P(x,y\mid H_1)}{P(x,y\mid H_0)} = M\log\frac{m/A}{1/A^{2}} + N\log\frac{(1-m)/(A(A-1))}{1/A^{2}} \qquad (18.24)
```

```math
= M\log mA + N\log\frac{(1-m)A}{A-1}. \qquad (18.25)
```

每一次匹配都贡献 $\log mA$ 支持 $H_1$；每一次不匹配都贡献 $\log\frac{A-1}{(1-m)A}$ 支持 $H_0$。

<span style="color:#00838f;">**（数值汇总，原书此处为一无框小表）**</span>

| 量 | 值 |
|---|---|
| monogram-English 的 match probability $m$ | 0.076 |
| 巧合匹配概率（coincidental match probability）$1/A$ | 0.037 |
| 每次匹配的支持 $H_1$ 的 log evidence $10\log_{10} mA$ | 3.1 db |
| 每次不匹配的支持 $H_1$ 的 log evidence $10\log_{10}\frac{(1-m)A}{(A-1)}$ | −0.18 db |

例如，若一对长度 $T = 51$ 的密文里有 $M = 4$ 处匹配、$N = 47$ 处不匹配，那么支持 $H_1$ 的证据权重是 $+4$ decibans，也就是似然比 $2.5$ 比 $1$。

一段长度为 $T = 20$ 个字符的文本给出的**期望**证据权重是 (18.25) 的期望，它取决于 $H_1$ 还是 $H_0$ 为真。若 $H_1$ 为真，匹配的期望出现率是 $m$，期望证据权重是每 20 个字符 $1.4$ decibans。若 $H_0$ 为真，

> <span style="color:#1e8449;">**[译注]** 那段数值汇总里 4 个数字可以**从 (18.25) 全部复算**，而它们正好解释了 Banburismus 为什么可行：匹配与不匹配的权重比是 $3.1 : 0.18 \approx 17$，所以「找到匹配」是强信号、「找到不匹配」是极弱的反信号。逐项核：$10\log_{10}(mA) = 10\log_{10}(0.076\times 26) = 10\log_{10}1.976 = 2.96 \approx 3.1$ db（原书印 3.1，比复算高 0.14——这是 $m$ 只取两位有效数字造成的舍入差 †）；$10\log_{10}\frac{(1-m)A}{A-1} = 10\log_{10}\frac{0.924\times26}{25} = 10\log_{10}0.9610 = -0.173 \approx -0.18$ db ✓。再看那两个期望值：$H_1$ 为真时，20 个字符里期望 $20\times0.076 = 1.54$ 个匹配、$18.46$ 个不匹配，总权重 $1.54\times3.1 - 18.46\times0.18 = 4.77 - 3.32 = 1.45$ db ✓（原文 1.4）；$H_0$ 为真时匹配率掉到 $1/26 = 0.0385$，期望 $0.77$ 个匹配，总权重 $0.77\times3.1 - 19.23\times0.18 = 2.39 - 3.46 = -1.07$ db ✓（原文 −1.1）。**失效对象**：若把 $m$ 当成 $1/26$（即「语言无冗余」），两个期望都归零、$\pm1.4$ db 的信号消失，必须在 $8\times10^{12}$ 个假设里盲搜——这就是「英语的冗余恰好是密码分析的燃料」的定量表述，也是 §18.1 字谜论证的同一条冗余在换战场。落点：本书 (18.22)–(18.25)、表 18.9、§18.4 末段；6.042J 的 Conditional probability 与 Logarithms；本书 §2.x 图 2.1 的字母频率表。</span>



<span style="color:#7f8c8d">书内 p.268（PDF p.280）｜ 18 — Crosswords and Codebreaking</span>

那么虚假匹配的期望出现率是 $1/A$，期望证据权重是每 20 个字符 $-1.1$ decibans。典型情况下，大约需要检查 400 个字符，才能取得大于一百比一（20 decibans）的证据权重，支持两个假设中的一个。

所以，两段英语明文之间的匹配数多于两段随机串之间的匹配数。此外，由于英语里相继字符不独立，英语的 bigram 与 trigram 统计是不均匀的，匹配倾向于**成簇出现**。[同样的观察也适用于德语。] 使用更好的语言模型，就能更准确地计算匹配连串所贡献的证据。这样一套打分系统由 Turing 提出、由 Good 精炼。正结果被传递给自动化与人工的破译者。据 Good 说，这项工作中出现的最长的 false-positive，是两台**实际处于不相关状态**的机器之间长达 8 个连续匹配的一串。

### Further reading（延伸阅读）

关于 Turing 与 Bletchley Park 的进一步阅读，见 Hodges (1983) 与 Good (1979)。若想深入读密码学，强烈推荐 Schneier (1996) 的书；它可读、清晰、且有趣。

### 18.5 Exercises（习题）

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 18.3.[2]**</span> Another weakness in the design of the Enigma machine, which was intended to emulate a perfectly random time-varying permutation, is that it never mapped a letter to itself. When you press Q, what comes out is always a different letter from Q. How much information per character is leaked by this design flaw? How long a crib would be needed to be confident that the crib is correctly aligned with the cyphertext? And how long a crib would be needed to be able confidently to identify the correct key?

> 中文话题：Enigma 的「字母不会映到自己」这一设计缺陷泄漏了多少信息；以及「用 crib 找对齐」与「用 crib 定密钥」各需要多长的 crib。
>
> [A crib is a guess for what the plaintext was. Imagine that the Brits know that a very important German is travelling from Berlin to Aachen, and they intercept Enigma-encoded messages sent to Aachen. It is a good bet that one or more of the original plaintext messages contains the string OBERSTURMBANNFUEHRERXGRAFXHEINRICHXVONXWEIZSAECKER, the name of the important chap. A crib could be used in a brute-force approach to find the correct Enigma key (feed the received messages through all possible Engima machines and see if any of the putative decoded texts match the above plaintext). This question centres on the idea that the crib can also be used in a much less expensive manner: slide the plaintext crib along all the encoded messages until a perfect mismatch of the crib and the encoded message is found; if correct, this alignment then tells you a lot about the key.]

> 方括号内的中文：crib（已知明文猜测）就是对明文曾经的样子的一个猜测。设想英国方面知道一位非常重要的德国人正从柏林前往 Aachen，于是截获了发往 Aachen 的 Enigma 密文。有理由打赌：原文消息里至少有一条包含字符串 `OBERSTURMBANNFUEHRERXGRAFXHEINRICHXVONXWEIZSAECKER`（这位要人的名字）。crib 可以用于暴力搜索正确的 Enigma 密钥（把收到的消息喂进所有可能的 Enigma 机器，看哪台解出的文本与上述明文相符）。但本题的着眼点是：crib 还能以**便宜得多**的方式使用——把明文 crib 在所有密文上滑动，直到找到「crib 与密文**完全错开**」的对齐位置；若这个对齐是对的，它就能告诉你大量关于密钥的信息。
>
> <span style="color:#7f8c8d">（原文如此。）</span>

> <span style="color:#1e8449;">**[译注]** 这道题的答案内核是**一个错误率而不是一个信息量**，值得先把提问方向掰正：Enigma 不把字母映到自身，于是每个位置上的密文字母有 $A - 1 = 25$ 个候选而不是 26 个，泄漏的信息量是 $\log_2\frac{26}{25} = 0.0566$ 比特/字符——**比 1 比特小两个数量级**。但它的用途不在「读信息」，而在「筛对齐」：把一个长 $K$ 的 crib 滑到某个偏移量上。若该偏移**正确**，Enigma 的自映射禁令保证每个位置上 crib 字母与密文字母必然不同——**这个条件以概率 1 成立**；若偏移**错误**，crib 与密文二者独立，每个位置「恰好不同」的概率是 $25/26$，于是整条 crib 全靠巧合通过筛选的概率是 $(25/26)^{K}$。判别力正来自这个不对称：正确偏移永不被排除，错误偏移以 $(25/26)^{K}$ 的概率漏网；只要在任意偏移上看到一个位置 crib 字母 = 密文字母，该偏移立刻被排除。这是「用否定证据搜索」的经典结构：$K = 20$ 时每个错误偏移的存活率是 $(25/26)^{20} = 0.457$，要在约 $10^{3}$ 个候选偏移里只剩一个，需要 $K$ 满足 $(25/26)^{K}\times 10^{3} \lt 1$，即 $K \gt 3/\log_{10}(26/25) = 3/0.0170 = 176$ 个字符。**失效对象**：若把「不自映射」错误地当成「每字符泄漏 1 比特」（例如以为排除一个字母的熵就是 $\log_2 26 - \log_2 25$ 里少了 1 比特），所需 crib 长度会算出一个数量级偏小的值；反过来，题目第三问「认出正确密钥」还要乘上密钥空间 $8\times10^{12}$ 的对数（约 43 比特），那是另一个量级的账。落点：本书 §18.4 与习题 18.3；6.042J 的 Union bound 与 Inclusion–exclusion（筛掉错误偏移是同一套计数）；6.006 的 String matching（滑动对齐就是 Brute-force string search 的复杂度分析）。</span>



<span style="color:#7f8c8d">书内 p.269（PDF p.281）｜ 19 Why have Sex? Information Acquisition and Evolution</span>

## 19 Why have Sex? Information Acquisition and Evolution（为什么要有性？信息的获取与演化）

演化（evolution）在地球上已经进行了大约 $10^9$ 年。无可否认，在这条进程中 information（信息）被获取了。多亏「盲眼钟表匠」（Blind Watchmaker）不知疲倦的工作，如今有些细胞体内携带着「成为一只出色蜘蛛」所需的全部 information，另一些细胞则携带着「成为一只优秀章鱼」所需的全部 information。这些 information 从哪里来？

这颗行星上所有生物的全套 blueprint（蓝图），是在一场 teaching process（教学进程）中浮现出来的，而这场教学里的教师就是 natural selection（自然选择）：fitness（适应度）更高的个体留下更多后代，而 fitness 由局部环境定义——包括环境里的其他生物。这个 teaching signal（教学信号）对每个个体而言只有几个比特：一个个体所做的事，不过是它的孙辈数量偏多或偏少，而偏多偏少取决于它自身的 fitness。

「Fitness」是个宽泛的词，它可以覆盖：

- 一只 antelope（羚羊）跑得比其他羚羊快、从而不被狮子吃掉的能力；
- 一只 lion（狮子）的伪装足够好、跑得足够快、每天能逮到一只羚羊的能力；
- 一只 peacock（雄孔雀）吸引 peahen（雌孔雀）与之交配的能力；
- 一只 peahen 同时抚育许多幼雏的能力。

一个生物的 fitness 在很大程度上由它的 DNA 决定——既包括 coding region（编码区，也就是 gene，基因），也包括 non-coding region（非编码区，它在调控 gene 的 transcription（转录）上扮演重要角色）。我们就把 fitness 看作 DNA 序列与环境的函数。

那么 DNA 如何决定 fitness，information 又如何从 natural selection 进入 genome（基因组）？这样看：如果编码羚羊某个 protein（蛋白质）的那个 gene 有缺陷，这只羚羊可能早早被狮子吃掉，只留下两个孙辈而不是四十个。natural selection 的 information content（信息量）完整地包含在「哪些后代活到了生育年龄」这一份名单里——其信息量每个后代至多一比特。teaching signal 并不向生态系统传达任何描述：它不描述生物体身上究竟是哪一处不完美导致它少生了孩子。teaching signal 的这些比特高度冗余，因为在一个物种之内，互不相同的 unfit（不适）个体往往正因为相似的原因而不能留下后代。

那么，整个物种每一代从 natural selection 那里获得的 information 有多少比特？自从生命之树上猿与人的分支分开以来，natural selection 成功传达给人类这一支的 information 又有多少比特？[本段跨页，下接 PDF p.282。]



<span style="color:#7f8c8d">书内 p.270（PDF p.282）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

分开发生在 $4\,000\,000$ 年前的 Australopithecines（南方古猿）与猿类之间。假设繁殖的 generation time（世代时间）为 10 年，那么自从与猿分道扬镳以来，人类前驱已经经过了约 $400\,000$ 代。假设种群规模为 $10^9$ 个个体†，每个个体从 natural selection 那里收到「几个比特」的 information，那么把 4 百万年前的 genome 改写为今天人类 genome 的全部 information 大约是 $8\times10^{14}$ 比特†。然而正如我们已经注意到的，natural selection 并不擅长把它分发给种群的那些 information 汇总（collate）起来，那份 information 里有极大的冗余。如果种群规模翻倍，演化会快一倍吗？不会——natural selection 只是把同样的缺陷多纠正了一倍的次数而已。

John Maynard Smith 曾提出：一个物种获取 information 的速率与种群规模无关，量级是每代 1 比特。这个数字只允许猿与人之间有 $400\,000$ 比特的差别，而这个数远小于人类 genome 的总规模——$6\times10^{9}$ 比特†。[一个人类 genome 含有约 $3\times10^{9}$ 个 nucleotide（核苷酸）。] 猿与人的 genome 重叠部分极大，这一点毫无疑问；但差别真有那么小吗？

在本章里，我们将为「通过演化获取 information」这一过程建立一个 crude model（粗糙模型），其假设是：带着两个缺陷的 gene 通常比带着一个缺陷的 gene 更坏，而带着两个 defective gene 的生物体比只带一个的 fitness 更低。无可否认这是个粗糙的模型，因为真实的生物系统是巴洛克式的构造、内部交互复杂。尽管如此，我们仍坚持一个简单模型，因为它能立刻给出醒目的结果。

从这个简单模型我们发现：

1. John Maynard Smith 那个「每代 1 比特」的数字，对**无性繁殖**的种群是正确的；
2. 相反地，如果物种**有性繁殖**，information 的获取速率可以达到每代 $\sqrt{G}$ 比特，其中 $G$ 是 genome 的规模。

我们还会得到一些关于「一个物种能承受的最大 mutation rate（突变率）」的有趣结果。

<span style="color:#00838f;">**19.1 The model（模型）**</span>

我们研究一个简单模型：繁殖种群有 $N$ 个个体，genome 规模为 $G$ 比特；variation（变异）由 mutation（突变）或 recombination（重组，也就是 sex）产生，而 truncation selection（截断选择）在每一代挑选最 fit 的 $N$ 个子代作为下一代的双亲。我们会看到，带 recombination 的种群与不带的种群之间存在刺眼的差别。

每个个体的 genotype（基因型）是一个 $G$ 比特的向量 $\mathbf{x}$，每一位有一个好状态 $x_g = 1$ 与一个坏状态 $x_g = 0$。个体的 fitness $F(\mathbf{x})$ 就是她各位之和：

```math
F(\mathbf{x}) = \sum_{g=1}^{G} x_g .
\qquad (19.1)
```

genome 里的这些比特可以被看成一堆 gene（各自有 good allele 好等位基因 $x_g=1$ 与 bad allele 坏等位基因 $x_g=0$），也可以被看成一个 genome 的 nucleotide。我们以后者这种解释为主。关于 fitness，我们实际假设的 essential property（本质性质）是它局部地近似为 genome 的线性函数，也就是说：你能对 genome 做的许多改动，每一个对 fitness 的影响都小，而它们的影响近似线性地叠加起来。



<span style="color:#7f8c8d">书内 p.271（PDF p.283）｜ 19.2: Rate of increase of fitness</span>

我们定义 normalized fitness（归一化适应度）$f(\mathbf{x}) \equiv F(\mathbf{x})/G$。

我们考虑 natural selection 之下的演化，variation 有两个模型。

> <span style="color:#00838f;">**Variation by mutation（由突变产生变异）**。</span>这个模型假设世代离散。在每一代 $t$，每个个体生两个孩子。子代的 genotype 与亲代的不同之处在于随机 mutation。natural selection 在子代群体中挑选最 fit 的 $N$ 个后代去繁殖，新的一代就此开始。
> [每一代都挑选最 fit 的 $N$ 个个体，这叫作 truncation selection。]
> 最简单的 mutation 模型是：子代的各位 $\{x_g\}$ 相互独立。每一位有一个小的被翻转概率；若把这些比特大致看成 nucleotide，那么这个概率取为常数 $m$，与 $x_g$ 无关。[另一种做法是把比特看成 gene，那时就要把「发现一个好 gene」的概率 $P(x_g=0 \to x_g=1)$ 建模为比「好 gene 发生有害突变」的概率 $P(x_g=1 \to x_g=0)$ 更小的数。]

> <span style="color:#00838f;">**Variation by recombination（由重组产生变异，也叫 crossover，也叫 sex）**。</span>我们的生物是 haploid（单倍体），不是 diploid（二倍体）。它们通过 recombination 享受 sex。种群中的 $N$ 个个体随机配对成 $M = N/2$ 对夫妻，每对生 $C$ 个孩子——标准假设取 $C = 4$，这样种群每一代仍然先翻倍再减半，与前面一样。给定双亲的 genotype，这 $C$ 个孩子的 genotype 相互独立。每个孩子通过双亲 genotype $\mathbf{x}$ 与 $\mathbf{y}$ 的随机 crossover 得到自己的 genotype $\mathbf{z}$。最简单的 recombination 模型没有 linkage（连锁），于是：

```math
z_g = \begin{cases}
x_g & \text{with probability } 1/2 \\
y_g & \text{with probability } 1/2 .
\end{cases}
\qquad (19.2)
```

等到 $MC$ 个后代出生，双亲随即死去，natural selection 选出最 fit 的 $N$ 个后代，新的一代就此开始。

下面我们详细研究这两个 variation 模型。

<span style="color:#00838f;">**19.2 Rate of increase of fitness（fitness 的增长速率）**</span>

**Theory of mutations（突变理论）**

我们假设：一个 normalized fitness 为 $f = F/G$ 的个体，其 genotype 受到翻转概率为 $m$ 的 mutation。我们首先证明：若种群的平均 normalized fitness $\bar f$ 大于 $1/2$，则最优 mutation rate 很小，information 的获取速率至多为一比特每代的量级。

由于靠简单 mutation 就能轻易达到 $f = 1/2$ 的 normalized fitness，我们将假设 $\bar f \gt 1/2$，并改用 excess normalized fitness（超出量）$\delta f \equiv \bar f - 1/2$ 来做推导。若一个 excess normalized fitness 为 $\delta f$ 的个体生了孩子、且 mutation rate $m$ 很小，那么孩子的 excess normalized fitness 的概率分布均值为

```math
\overline{\delta f}{}_{\text{child}} = (1 - 2m)\,\delta f ,
\qquad (19.3)
```



<span style="color:#7f8c8d">书内 p.272（PDF p.284）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

而方差为

```math
m(1 - m)\frac{1}{G} \simeq \frac{m}{G} .
\qquad (19.4)
```

若亲代种群的均值为 $\overline{\delta f}(t)$、方差为 $\sigma^2(t) \equiv \beta m/G$，那么在选择之前，子代种群的均值为 $(1-2m)\overline{\delta f}(t)$、方差为 $(1+\beta)m/G$。natural selection 挑走这个分布的上半部分，于是下一代的 fitness 均值与 fitness 方差为

```math
\overline{\delta f}(t+1) = (1 - 2m)\,\overline{\delta f}(t) + \alpha\sqrt{1+\beta}\,\sqrt{\frac{m}{G}} ,
\qquad (19.5)
```

```math
\sigma^2(t+1) = \gamma(1+\beta)\,\frac{m}{G} ,
\qquad (19.6)
```

其中 $\alpha$ 是「均值之上的平均偏离」，以标准差为单位；$\gamma$ 是「选择把子代分布的方差压缩了多少」的那个因子。$\alpha$ 与 $\gamma$ 都是 1 的量级。对于 Gaussian distribution（高斯分布）的情形，$\alpha = \sqrt{2/\pi} \simeq 0.8$，$\gamma = (1 - 2/\pi) \simeq 0.36$。若假设方差处于 dynamic equilibrium（动态平衡），即 $\sigma^2(t+1) \simeq \sigma^2(t)$，则

```math
\gamma(1+\beta) = \beta, \quad \text{so} \quad (1+\beta) = \frac{1}{1-\gamma} ,
\qquad (19.7)
```

而式 (19.5) 里的因子 $\alpha\sqrt{1+\beta}$ 就等于 1——只要我们采用 Gaussian distribution 的结果。这个近似在最糟时会失效：当 fitness 的离散性变得重要时，也就是 $m$ 很小时。于是 normalized fitness 的增长速率为：

```math
\frac{df}{dt} \simeq -2m\,\delta f + \sqrt{\frac{m}{G}} ,
\qquad (19.8)
```

在假设 $G(\delta f)^2 \gg 1$ 之下，它在

```math
m_{\text{opt}} = \frac{1}{16\,G(\delta f)^2}
\qquad (19.9)
```

处取最大；此时

```math
\left(\frac{df}{dt}\right)_{\text{opt}} = \frac{1}{8\,G\,\delta f} .
\qquad (19.10)
```

于是 fitness $F = fG$ 的增长速率至多是

```math
\frac{dF}{dt} = \frac{1}{8\,\delta f} \ \ \text{per generation}.
\qquad (19.11)
```

对于 fitness 偏低的种群（$\delta f \lt 0.125$），fitness 的增长速率可以超过每代一个单位。确实，若 $\delta f \ll 1/\sqrt{G}$，取 $m = 1/2$ 时增长速率为 $\sqrt{G}$ 的量级；这个初始冲刺只能持续 $\sqrt{G}$ 代左右。当 $\delta f \gt 0.125$ 时，fitness 的增长速率小于每代一个。当 fitness 逼近 $G$ 时，optimal mutation rate 趋于 $m = 1/(4G)$，也就是平均每个 genotype 翻转 $1/4$ 个比特，而 fitness 的增长速率也等于 $1/4$；information 的获取速率约为每代 $0.5$ 比特。种群中所有个体的 genotype 达到完美，约需 $2G$ 代。

对固定的 $m$，fitness 由下式给出：

```math
\delta f(t) = \frac{1}{2\sqrt{mG}}\left(1 - c\,e^{-2mt}\right),
\qquad (19.12)
```

<span style="color:#1e8449;">**[译注]** 式 (19.9)–(19.11) 这三行是整个 §19.2 的技术心脏，值得手推一遍，因为它的**结论有一条硬上限**，而这个上限是后面「无性物种为什么撑不住」的全部来源。把 $g(m) \equiv -2m\,\delta f + \sqrt{m/G}$ 对 $m$ 求导并置零：$\frac{dg}{dm} = -2\delta f + \frac{1}{2\sqrt{mG}} = 0$，解得 $\sqrt{m} = \frac{1}{4\,\delta f\sqrt{G}}$，即 $m_{\text{opt}} = \frac{1}{16G(\delta f)^2}$；代回得 $g(m_{\text{opt}}) = -\frac{1}{8G\delta f} + \frac{1}{4G\delta f} = \frac{1}{8G\delta f}$，与 (19.10) 逐字吻合——这条代回验算是本页唯一需要自己动手的地方。**失效对象是清楚的**：若没有这个最优化，就只剩「突变越少越好」这一句空话，从而看不出两个反常事实——其一，最优 mutation rate 随 $\delta f$ 的平方反比衰减，$f$ 越接近 $1$（$\delta f \to 1/2$）允许的 $m$ 越小，$m_{\text{opt}} \to 1/(4G)$ 恰好对应「平均每个 genome 翻 $1/4$ 位」；其二，把 $G$ 乘上去得 $m_{\text{opt}}G = 1/(16\delta f^2)$，**与 genome 规模无关**，永远是个常数，这就是原文「每代至多 1 比特 information」的算术来源（$dF/dt \le 1/(8\delta f)$，$\delta f = 1/2$ 时正是 $1/4$ 单位/代，折算 information 约 $0.5$ 比特/代）。失败模式具体到可观测：若有人把 (19.8) 中的 $-2m\delta f$ 与 $+\sqrt{m/G}$ 当成两个独立效应而**分别**优化，会得出「$m\to 0$ 时增长最快」的错误结论，那样就无法解释 $m = 1/2$（每代把半个 genome 翻个遍）在低 fitness 阶段反而最快、且能持续 $\sqrt{G}$ 代。落点：本书 §19.2 式 (19.8)–(19.11)；对照 §19.3 式 (19.17) 的 $m \lt \frac{1}{(2\delta f)^2 G}$，那里因子从 16 降到 4，正是「耐受」与「最优」两件事不能混用的证据；6.006 的 convexity / 一阶条件（求导置零取极值的前提是函数凹，$\sqrt{m}$ 的凹性在此承重）。</span>



<span style="color:#7f8c8d">书内 p.273（PDF p.285）｜ 19.2: Rate of increase of fitness</span>

受约束于 $\delta f(t) \le 1/2$，其中 $c$ 是积分常数，若 $f(0) = 1/2$ 则 $c = 1$。若每个 genotype 平均被翻转的比特数 $mG$ 超过 1，则 fitness $F$ 趋于平衡值 $F_{\text{eqm}} = \left(\frac{1}{2} + \frac{1}{2\sqrt{mG}}\right)G$。

这个理论有些不准确，因为 fitness 的真实概率分布是非 Gaussian 的、不对称的、并且被量化到整数值。尽管如此，理论的预测与下面描述的那些模拟结果并没有严重相悖。

[Figure 19.1：它演示的是什么——「为什么 sex 优于无 sex 的繁殖」。上下两层各画两条分布：左列 No sex（mutation 产生变异），右列 Sex（recombination 产生变异）；每列上层是「亲代 fitness 的直方图」，下层是「子代 fitness 的直方图」外加被选中的子代。要看的正是两条分布**均值的位置**：mutation 会把子代均值整体压低，变异越大、均值缺口越大；recombination 产生变异却**不压低均值**。无法复原：具体刻度与柱高，文字层只给出该图要主张的定性结构。]

正如图中所示：若用 mutation 在孩子之间造出变异，那么子代的平均 fitness 不可避免要低于亲代；变异越大，平均缺口越大，选择再把平均 fitness 抬回去。相反，recombination 产生变异而不降低平均 fitness。典型变异量按 $\sqrt{G}$ 标度，$G$ 为 genome 规模，于是选择之后平均 fitness 上升 $O(\sqrt{G})$。

**Theory of sex（性的理论）**

有性种群的分析在两个近似之下变得可解：第一，我们假设 gene pool（基因池）混合得足够快，gene 之间的相关性可以忽略；第二，我们假设 homogeneity（同质性），即处于好状态的比特 $g$ 所占比例 $f_g$ 对所有 $g$ 都相同，记为 $f(t)$。

在这些假设之下，若两个 fitness 为 $F = fG$ 的双亲交配，则其孩子 fitness 的概率分布**均值等于双亲的 fitness** $F$；sex 产生的变异不降低平均 fitness。孩子 fitness 的标准差按 $\sqrt{Gf(1-f)}$ 标度。由于选择之后的 fitness 增量与这个标准差成正比，每代的 fitness 增量就按 genome 规模的平方根 $\sqrt{G}$ 标度。

如 Box 19.2 所示，平均 fitness $\bar F = fG$ 依据下面的微分方程演化：

```math
\frac{d\bar F}{dt} \simeq \eta\sqrt{f(t)\left(1-f(t)\right)G} ,
\qquad (19.13)
```

其中 $\eta \equiv \sqrt{2/(\pi+2)} \simeq 0.624$。该方程的解是

```math
f(t) = \frac{1}{2}\left[\,1 + \sin\!\left(\frac{\eta}{\sqrt{G}}(t+c)\right)\right],
\quad \text{for } t+c \in \left(-\frac{\pi}{2}\frac{\sqrt{G}}{\eta},\ \frac{\pi}{2}\frac{\sqrt{G}}{\eta}\right),
\qquad (19.14)
```

其中 $c$ 是积分常数，$c = \sin^{-1}\!\left(2f(0)-1\right)$。于是这个理想化系统在**有限时间**内达到 eugenic perfection（优生完美态，$f = 1$）：$(\pi/\eta)\sqrt{G}$ 代†。

<span style="color:#7f8c8d">† 勘误：把 $f(0) = 1/2$ 代入 (19.14) 得 $\sin\!\left(\eta c/\sqrt{G}\right) = 0$，即 $c = 0$；那么 $f = 1$ 要求 $\sin\!\left(\eta t/\sqrt{G}\right) = 1$，即 $t = \frac{\pi}{2}\frac{\sqrt{G}}{\eta} \simeq 2.518\sqrt{G}$ 代，而不是原文写的 $(\pi/\eta)\sqrt{G} \simeq 5.036\sqrt{G}$ 代。两者差因子 2，怀疑原文把「半个正弦周期」与「四分之一周期」混淆了。以 (19.14) 为准。取 $G = 1000$ 时，两式分别给出 $79.6$ 代与 $159$ 代；原文图 19.3a 的横轴只到 $80$ 代左右就收敛，支持前一个数。</span>

**Simulations（模拟）**

Figure 19.3a 显示一个有性种群（$N = 1000$、genome 规模 $G = 1000$）的 fitness 演化：初始状态随机，normalized fitness 为 $0.5$。它同时画出了式 (19.14) 的理论曲线 $f(t)G$，吻合得出奇地好。

作为对比，Figure 19.3(b) 与 (c) 显示 variation 由 mutation 产生时的 fitness 演化，两个 mutation rate 分别是 $m = 0.25/G$ 与 $m = 6/G$。注意它们与 (a) 在横轴刻度上的差别。



<span style="color:#7f8c8d">书内 p.274（PDF p.286）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

<span style="color:#00838f;">**Box 19.2. Details of the theory of sex（性的理论细节）**</span>

$f(t+1)$ 如何依赖 $f(t)$？先假设一个孩子的两位亲代都恰好有 $f(t)G$ 个好比特，并且按我们的 homogeneity 假设，那些比特是 $G$ 个比特的独立随机子集。两位亲代都好的比特数约为 $f(t)^2 G$，只有一位亲代好的比特数约为 $2f(t)(1-f(t))G$。于是孩子的 fitness 是 $f(t)^2 G$ 加上 $2f(t)(1-f(t))G$ 次公平硬币投掷之和；后者服从二项分布，均值为 $f(t)(1-f(t))G$、方差为 $\frac{1}{2}f(t)(1-f(t))G$。因此孩子的 fitness 大致分布为

```math
F_{\text{child}} \sim \text{Normal}\left(\ \text{mean} = f(t)G,\ \ \text{variance} = \tfrac{1}{2}f(t)(1-f(t))G\ \right).
```

这个分布的重要性质——与 mutation 之下的分布相对照——是：**均值等于亲代的 fitness**；sex 产生的变异不降低平均 fitness。

若把亲代种群的方差也算进来，记作 $\sigma^2(t) = \beta(t)\,\frac{1}{2}f(t)(1-f(t))G$，则孩子的 fitness 分布为

```math
F_{\text{child}} \sim \text{Normal}\left(\ \text{mean} = f(t)G,\ \ \text{variance} = \left(1+\tfrac{\beta}{2}\right)\tfrac{1}{2}f(t)(1-f(t))G\ \right).
```

natural selection 从这个分布的上侧挑走孩子。fitness 的平均增量将是

```math
\bar F(t+1) - \bar F(t) = \left[\alpha\left(1+\tfrac{\beta}{2}\right)^{1/2}\middle/\sqrt{2}\right]\sqrt{f(t)(1-f(t))G},
```

而被选中的孩子的方差将是

```math
\sigma^2(t+1) = \gamma\left(1+\tfrac{\beta}{2}\right)\tfrac{1}{2}f(t)(1-f(t))G,
```

其中 $\alpha = \sqrt{2/\pi}$、$\gamma = (1-2/\pi)$。若存在 dynamic equilibrium（即 $\sigma^2(t+1) = \sigma^2(t)$），上述因子就化为

```math
\frac{\alpha\left(1+\tfrac{\beta}{2}\right)^{1/2}}{\sqrt{2}} = \sqrt{\frac{2}{\pi+2}} \simeq 0.62 .
```

把这个常数记作 $\eta \equiv \sqrt{2/(\pi+2)}$，我们得到结论：在 sex 加 natural selection 之下，种群的平均 fitness 以正比于 genome 规模平方根的速率增长，

```math
\frac{d\bar F}{dt} \simeq \eta\sqrt{f(t)\left(1-f(t)\right)G} \ \ \text{bits per generation}.
```



<span style="color:#7f8c8d">书内 p.275（PDF p.287）｜ 19.3: The maximal tolerable mutation rate</span>

[Figure 19.3：它演示的是什么——fitness 随时间（横轴，单位：代）的三组演化，genome 规模 $G = 1000$。散点表示每一代从出生群体里随机抽出的六个个体的 fitness。(a) 变异只由 sex 产生，实线是无限大 homogeneous 种群的理论曲线 (19.14)；(b)(c) 变异由 mutation 产生，分别在有 sex 与无 sex 两种情形，mutation rate 为 $mG = 0.25$（b）与 $mG = 6$（c）比特/genome，虚线是曲线 (19.12)。要看的对比是横轴量级：(a) 与 (b) 在几十代的量级内收敛，而 (c) 要几百代。无法复原：三张子图的具体纵轴刻度（文字层读到 (a) 约 500–1000、(b) 约 500–1000 后接 0–1600、(c) 约 500–1000 后接 0–350 的轴标签残片，无法判定哪条轴对应哪条曲线）、以及 sex / no sex 两条曲线的各自颜色。]

[Figure 19.4：它演示的是什么——**最大可耐受 mutation rate**（以每个 genome 的错误数 $mG$ 表示）与 normalized fitness $f = F/G$ 的关系。左图 $G = 1000$、$mG$ 轴到 20；右图 $G = 100\,000$、$mG$ 轴到 50。两张图各有 with sex 与 without sex 两条曲线。核心主张：**与 genome 规模无关**，孤雌生殖（无 sex）的物种每个 genome 每代只能耐受 1 个错误量级，而用 recombination 的物种能耐受大得多的 mutation rate。无法复原：曲线形状与具体数值点（原文只给出轴端点 0.65–1 的纵轴范围与 0/5/10/15/20 的横轴刻度，无采样数据）。]

<span style="color:#c0392b">**Exercise 19.1.**</span> <span style="color:#7f8c8d">[3, p.280]</span> <span style="color:#2471a3;">**[exercise]**</span> Dependence on population size. How do the results for a sexual population depend on the population size? We anticipate that there is a minimum population size above which the theory of sex is accurate. How is that minimum population size related to G?

> 中文话题：有性种群的结果对种群规模 $N$ 的依赖；并猜测存在一个「sex 理论成立所需的最小种群规模」，问这个规模与 $G$ 是什么关系。（书后 p.280 有解答，见本块 PDF p.292。）

<span style="color:#c0392b">**Exercise 19.2.**</span> <span style="color:#7f8c8d">[3]</span> <span style="color:#2471a3;">**[exercise]**</span> Dependence on crossover mechanism. In the simple model of sex, each bit is taken at random from one of the two parents, that is, we allow crossovers to occur with probability 50% between any two adjacent nucleotides. How is the model affected (a) if the crossover probability is smaller? (b) if crossovers occur exclusively at hot-spots located every d bits along the genome?

> 中文话题：crossover 机制对结论的影响——(a) 相邻位之间的 crossover 概率低于 50% 时会怎样；(b) 若 crossover 只发生在沿 genome 每隔 $d$ 比特设一个的 hot-spot（热点）上又会怎样。

<span style="color:#00838f;">**19.3 The maximal tolerable mutation rate（最大可耐受的突变率）**</span>

如果我们把两个 variation 模型合并起来会怎样？一个**有 sex** 的物种，能耐受的最大 mutation rate 是多少？fitness 的增长速率由下式给出：

```math
\frac{df}{dt} \simeq -2m\,\delta f + \frac{\eta}{\sqrt{2}}\sqrt{\frac{m + f(1-f)/2}{G}} ,
\qquad (19.15)
```



<span style="color:#7f8c8d">书内 p.276（PDF p.288）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

当 mutation rate 满足

```math
m \lt \eta\sqrt{\frac{f(1-f)}{G}}
\qquad (19.16)
```

时，上式为正。让我们把这个速率与无 sex 情形的结果比较——由式 (19.8) 得，无 sex 时最大可耐受的 mutation rate 是

```math
m \lt \frac{1}{G}\frac{1}{(2\delta f)^2} .
\qquad (19.17)
```

有 sex 时可耐受的 mutation rate，比无 sex 时大 $\sqrt{G}$ 的量级！

一个 parthenogenetic（孤雌生殖的，即无性的）物种可以试着靠加大它的 litter size（窝仔数）来绕开这个 mutation rate 的上界。但如果 mutation 平均翻转 $mG$ 个比特，那么一个 genome 里**一位都没被翻转**的概率约为 $e^{-mG}$，所以一位母亲需要生下约 $e^{mG}$ 个后代，才有像样的机会得到一个与她自己同样 fit 的孩子。于是无性物种若想存续，它的窝仔数必须是 $mG$ 的指数（当 $mG$ 大于 1 时）。

所以，对无性物种而言，最大可耐受的 mutation rate 被钉在接近 $1/G$ 处；而对有 recombination 的物种而言，这个数是 $1/\sqrt{G}$ 量级的、更大的数值。

把这些结果反过来用，我们就能在给定固定 mutation rate $m$ 的条件下预测 genome 规模的上限。对孤雌生殖物种，最大 genome 规模是 $1/m$ 的量级；对有性物种，是 $1/m^2$。取每代每 nucleotide 的 mutation rate 为 $m = 10^{-8}$（Eyre-Walker and Keightley, 1999），并允许最大 brood size（育雏数）为 $20\,000$（也就是 $mG \simeq 10$），我们预测：所有编码 nucleotide 数多于 $G = 10^{9}$† 的物种，都至少偶尔使用 recombination。若 brood size 是 12，这个数目降到 $G = 2.5\times10^{8}$†。

<span style="color:#1e8449;">**[译注]** 这两页（$1/G$ 与 $1/\sqrt{G}$ 之争）是本章唯一一个能拿真实数字对撞的结论，也是全章最值得亲手算一遍的地方——因为**它给出的是一条能判生死的数量级门槛，而不是一句「性有好处」**。代入真实参数：人类 genome 的编码 nucleotide 数约 $G = 3\times10^{9}$（原文别处写 $6\times10^{9}$ 比特，因每个 nucleotide 承载 2 比特的四种碱基状态），每代每 nucleotide 的实测 mutation rate $m = 10^{-8}$。若无 sex，由 (19.17) 取 $\delta f = 0.25$ 得门槛 $m \lt \frac{1}{4G\delta f^2} = \frac{1}{4 \cdot 3\times10^{9} \cdot 0.0625} \approx 1.3\times10^{-9}$——而实测 $m = 10^{-8}$ 已经**超出这个门槛约 7.5 倍**，也就是说孤雌生殖的哺乳动物根本不该存在于 $G = 3\times10^{9}$ 这个量级。有 sex 时，由 (19.16) 取 $f = 0.75$ 得 $m \lt \eta\sqrt{\frac{0.1875}{3\times10^{9}}} = 0.624\times 2.5\times10^{-5} \approx 1.6\times10^{-5}$，实测值在门槛之下还有三个半数量级的余量。**失效对象**：抽掉 recombination，$mG$ 这个乘积（每代每 genome 的期望翻转数）就被钉死在 $1$ 附近，而人类实测 $mG = 10^{-8}\times3\times10^{9} = 30$——30 倍的差距，这不是精度问题，是「该物种能否存在」的问题。原文紧接着用同一个乘积给出可检验的预测：$mG \simeq 10$ 对应 brood size $20\,000$，$G = 10^{9}$；brood size 降到 12（$mG$ 更小）则 $G$ 上限降到 $2.5\times10^{8}$。**失败模式具体到可观测**：若把 (19.16) 与 (19.17) 的下界当成同一个式子（都写成 $m \lesssim 1/G$），就会得出「有性物种的 genome 上限也是 $1/m = 10^{8}$」，于是无法解释为什么 $G$ 到 $10^{9}$ 以上乃至 $10^{10}$ 的物种仍然存在，也看不出「$e^{mG}$ 个后代」这条指数代价为什么足以让无性谱系灭绝。落点：本书 §19.3 式 (19.15)–(19.17) 与图 19.4；Eyre-Walker & Keightley (1999) 给出 $m = 10^{-8}$；跨学科挂到 6.042J 的指数增长与对数计数（$e^{mG}$ 是「$mG$ 次独立未命中」的概率），以及 CS144 里「错误率与冗余度」的同一套 trade-off。</span>

<span style="color:#00838f;">**19.4 Fitness increase and information acquisition（fitness 增长与信息获取）**</span>

对这个简单模型，我们可以把 fitness 的增长与 information 的获取联系起来。

如果各位是随机设定的，fitness 大致是 $F = G/2$。如果演化导致一个所有个体都有最大 fitness $F = G$ 的种群，那么该物种就获取了 $G$ 比特 information——也就是对每一位 $x_g$，物种都搞清了两个状态里哪一个更好。

我们把「中间 fitness 之下已获取的 information」定义为：要从 gene pool 中把完美状态挑出来，所需要进行的选择的「量」（以比特计）。设种群中有比例 $f_g$ 的个体有 $x_g = 1$。由于 $\log_2(1/f)$ 是在一个黑白球比例为 $f : 1-f$ 的 urn（瓮）里找到一个黑球所需的 information，我们就把已获取的 information 定义为

```math
I = \sum_g \log_2\!\left(\frac{f_g}{1/2}\right) \ \ \text{bits}.
\qquad (19.18)
```

若所有比例 $f_g$ 都等于 $F/G$，则

```math
I = G \log_2\!\left(\frac{2F}{G}\right),
\qquad (19.19)
```

它可以很好地近似为

```math
\tilde I \equiv 2\left(F - \frac{G}{2}\right).
\qquad (19.20)
```

于是 information 的获取速率大致是种群中 fitness 增长速率的两倍†。

<span style="color:#7f8c8d">† 勘误：把 (19.19) 在 $F = G/2$ 附近作一阶展开，令 $u \equiv \frac{2F}{G} - 1$（$u$ 小），则 $I = G\log_2(1+u) \simeq \frac{G\,u}{\ln 2} = \frac{2}{\ln 2}\left(F - \frac{G}{2}\right) \approx 2.885\left(F - \frac{G}{2}\right)$，系数是 $2.885 = 2/\ln 2$，而不是 $2$。原文 (19.20) 给出的 $2$ 比严格一阶展开小约 31%。这个差别在本章不影响任何定性结论（下一句的「两倍」应当按 $2/\ln 2 \approx 2.9$ 理解才与 (19.19) 自洽），但若有人拿 (19.20) 当定量公式去做数值核对，会稳定偏低三成。</span>



<span style="color:#7f8c8d">书内 p.277（PDF p.289）｜ 19.5: Discussion</span>

<span style="color:#00838f;">**19.5 Discussion（讨论）**</span>

这些结果量化了一个众所周知的论证：为什么物种要采用带 recombination 的有性繁殖。这个论证是说，recombination 让有用的 mutation 更快地在物种中扩散，也让有害的 mutation 更快地从种群中被清除（Maynard Smith, 1978; Felsenstein, 1985; Maynard Smith, 1988; Maynard Smith and Száthmary, 1995）。一个靠 recombination 繁殖的种群，从 natural selection 获取 information 的速率比 parthenogenetic 种群快 $\sqrt{G}$ 的量级，它能耐受的 mutation rate 也大 $\sqrt{G}$ 的量级。对编码 nucleotide 数为 $G \simeq 10^{8}$ 的 genome，这个 $\sqrt{G}$ 因子是相当可观的。

sex 带来的这个巨大优势，Kondrashov (1988) 早已指出过。但这个 meme（模因）——Kondrashov 称之为「deterministic mutation hypothesis（确定性突变假说）」——似乎并没有在演化研究共同体中扩散开来，因为至今仍有大量论文把 sex 的普遍存在看成一个需要靠精巧机制来解释的谜。

> <span style="color:#00838f;">**「雄性的代价」—— sex 或 parthenogenesis 基因的稳定性**</span>

为什么人们宣称 sex 是个谜？被弄糊涂的主要动机来自一个叫「cost of males（雄性的代价）」的想法。论证是这样的：与无性繁殖相比，有性繁殖是不利的，因为 sex 每产两个后代，平均就有一个是没用的雄性、不会生育，只有一个是有生产力的雌性。而在同样的时间里，一位孤雌生殖的母亲可以生下两个雌性克隆。换个说法：从个体角度看，parthenogenesis 的巨大优势在于，一个人能把自己 genome 的 100% 传给自己的孩子，而不是只有 50%。所以，如果一个物种存在两个版本，一个靠 sex 繁殖、一个不靠 sex，那么我们该预期那些单身母亲们会盖过它们的有性表亲。

到目前为止展示的简单模型既没有包含性别，也没有包含「从有性繁殖切换到无性繁殖」的能力，但我们可以轻松地修改模型。

我们这样改：让 genome 的 $G$ 个比特中的一位决定该个体倾向于孤雌生殖（$x = 1$）还是有性生殖（$x = 0$）。结果取决于一位孤雌生殖母亲所生孩子数 $K_p$ 与一对有性夫妻所生孩子数 $K_s$。$(K_p = 2, K_s = 4)$ 与 $(K_p = 4, K_s = 4)$ 都是合理的模型。前者 $(K_p = 2, K_s = 4)$ 似乎最适合单细胞生物的情形，那里双亲的 cytoplasm（细胞质）都进入了孩子。后者 $(K_p = 4, K_s = 4)$ 适用于「孩子只由双亲之一抚育」的情形，此时单身母亲的后代数与一对有性夫妻一样多。我集中看后一个模型，因为它给了 parthenogen（孤雌生殖者）最大的优势，而据说它们本该把有性社群繁殖得落花流水。由于 parthenogen 每代有四个孩子，它们最大可耐受的 mutation rate 是此前为 $K_p = 2$ 推出的表达式 (19.17) 的两倍。若 fitness 很大，最大可耐受速率是 $mG \simeq 2$。

初始的 genome 随机设定、$F = G/2$，一半种群带有 parthenogenesis 基因。Figure 19.5 给出结果。在演化的「learning」阶段——fitness 快速上升的那一段——一小块一小块的 parthenogen 会短暂出现，但在一两代之内就消失了，因为它们的有性表亲在 fitness 上超越了它们、把它们甩在后面。



<span style="color:#7f8c8d">书内 p.278（PDF p.290）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

然而一旦种群到达其 fitness 上限，如果 mutation rate 足够低（$mG = 1$），parthenogen 就能接管。(a) 与 (b) 两栏分别是 $mG = 4$ 与 $mG = 1$ 的结果。

[Figure 19.5：它演示的是什么——「当 genome 里存在一个 parthenogenesis 基因、两个亚种群不杂交、且单身母亲的孩子数与有性夫妻一样多时」的演化结局。$G = 1000$、$N = 1000$。(a) $mG = 4$；(b) $mG = 1$。每栏上半是两条曲线（sexual fitness 与 parthen fitness，纵轴 500–1000、横轴 $0$–250 代），下半是 parthenogenetic 个体占种群的百分比（纵轴 0–100%）。核心主张：$mG$ 高时 parthenogen 永远接管不了，$mG$ 低时 fitness 到顶后 parthenogen 会接管。无法复原：曲线轨迹与百分比的具体形状。]

然而在更高的 mutation rate 之下（$mG = 4$），parthenogen 永远接管不了。有性种群的 fitness 宽度是 $\sqrt{G}$ 的量级，所以一个 fitness 略高于平均的突变型 parthenogenetic 群落，会存活约 $\sqrt{G}/(mG) = 1/(m\sqrt{G})$ 代，之后它的 fitness 就落到有性表亲之下。只要种群规模足够大、能让一些有性个体活过这段时间，sex 就不会灭绝。

在一个足够不稳定的环境里——fitness 函数不断变化——parthenogen 将永远落后于有性社群。这些结果与 Haldane and Hamilton (2002) 的论证一致：sex 在与寄生虫的军备竞赛中有帮助。寄生虫定义了一个随时间变化的有效 fitness 函数，而有性种群总能更快地爬上当前的 fitness 函数。

<span style="color:#00838f;">**Additive fitness function（可加性适应度函数）**</span>

当然，我们的结果取决于我们假设的 fitness 函数与我们的选择模型。「把 fitness 一阶地建模为若干独立项之和」是否合理？Maynard Smith (1968) 论证它是合理的：比如，你拥有的好 gene 越多，你在啄序（pecking order）中的位置就越靠前。directional selection 模型（定向选择模型）在理论群体遗传学研究中被大量使用（Bulmer, 1985）。我们也许该预期真实的 fitness 函数涉及交互项，若如此，crossover 可能反而降低平均 fitness。然而，既然 recombination 给「fitness 函数可加」的物种带来最大优势，我们或许可以预测：演化会偏好那些使用某种 genome 表示、其对应的 fitness 函数只有弱交互的物种。而且即便存在交互，看上去仍然合理的是：fitness 依旧是若干此类交互项之和，只是项数变成 genome 规模 $G$ 的某个分数。



<span style="color:#7f8c8d">书内 p.279（PDF p.291）｜ 19.6: Further exercises</span>

<span style="color:#c0392b">**Exercise 19.3.**</span> <span style="color:#7f8c8d">[3C]</span> <span style="color:#2471a3;">**[exercise]**</span> Investigate how fast sexual and asexual species evolve if they have a fitness function with interactions. For example, let the fitness be a sum of exclusive-ors of pairs of bits; compare the evolving fitnesses with those of the sexual and asexual species with a simple additive fitness function.

> 中文话题：当 fitness 函数带交互项时，有性与无性物种各自演化得多快。具体做法是把 fitness 取为「成对比特的 exclusive-or（异或）之和」，再与简单可加 fitness 函数下两种物种的演化曲线做对照。（$C$ 标记表示这是 computer-exercise，需要写程序跑模拟。）

此外，如果 fitness 函数是 genotype 的强非线性函数，它可以通过 Baldwin effect（鲍德温效应）变得更光滑、局部更线性。Baldwin effect（Baldwin, 1896; Hinton and Nowlan, 1987）作为「学习引导演化」的机制被广泛研究，它也可能在 transcription 与 translation 这一层级上起作用。设想一条 peptide（肽）序列为某个新用途而演化。假设该肽的有效性是序列的强非线性函数，也许它有一个「好序列的小岛」，四周被「同样糟糕的序列的海洋」包围。在一个 transcription 与 translation 机制完美无缺的生物体里，fitness 就会是 DNA 序列的同样非线性的函数，演化只能在这片海洋里游荡，仅靠 random walk（随机游走）朝那座小岛取得进展。相反，一个拥有同样 DNA 序列、但 DNA 到 RNA 的 transcription 或 RNA 到 protein 的 translation 是「有毛病」的生物体，会偶尔因 mistranslation 或 mistranscription 而意外产出一个能工作的酶；而且如果它的 DNA 序列离一个好序列更近，它就这么干的概率更大。一个细胞可能从同一条 mRNA 序列产出 1000 个 protein，其中 999 个没有酶活性，而有一个有。那一个能工作的 catalyst（催化剂）就足以让这个细胞相对于「DNA 序列离好序列之岛更远」的竞争者拥有更高的 fitness。因为这个理由，我猜想：至少在演化的早期、也许至今仍然如此，genetic code（遗传密码）并不是被完美地实现的，而是被带噪地实现的——某些 codon（密码子）编码的是一个氨基酸的概率分布。这个带噪的密码甚至可以在同一个生物体内从细胞到细胞地被打开和关闭，办法是拥有多个 aminoacyl-tRNA synthetase（氨酰-tRNA 合成酶），其中一些比另一些更可靠。

尽管我们的模型假设 genome 的各位互不交互、忽略了 information 是被冗余表示的、假设 phenotypic fitness 与 genotype 之间有直接的对应关系、并假设 recombination 中的 crossover 概率很高，我相信若采用更复杂的 fitness 与 crossover 模型，这些定性结果仍然成立：sex 的相对好处仍将按 $\sqrt{G}$ 标度。只有在规模很小、近交（in-bred）的种群中，sex 的好处才会被削弱。

总而言之：为什么要有 sex？**因为 sex 对你的比特有好处！**

<span style="color:#00838f;">**Further reading（延伸阅读）**</span>

最初那个高信息量的自我复制系统究竟是怎么冒出来的？在生命起源这个总领域、以及关于演化的其他棘手问题上，我强烈推荐 Maynard Smith and Száthmary (1995)、Maynard Smith and Száthmary (1999)、Kondrashov (1988)、Maynard Smith (1988)、Ridley (2000)、Dyson (1985)、Cairns-Smith (1985) 以及 Hopfield (1978)。

<span style="color:#00838f;">**19.6 Further exercises（补充习题）**</span>

<span style="color:#c0392b">**Exercise 19.4.**</span> <span style="color:#7f8c8d">[3]</span> <span style="color:#2471a3;">**[exercise]**</span> How good must the error-correcting machinery in DNA replication be, given that mammals have not all died out long ago? Estimate the probability of nucleotide substitution, per cell division. [See Appendix C.4.]

> 中文话题：既然哺乳动物没有早早全部灭绝，DNA 复制中的 error-correcting machinery（纠错机器）必须好到什么程度？要求估计「每次 cell division（细胞分裂）发生 nucleotide 替换的概率」的上界。（提示见附录 C.4。）

<span style="color:#c0392b">**Exercise 19.5.**</span> <span style="color:#7f8c8d">[4]</span> <span style="color:#2471a3;">**[exercise]**</span> Given that DNA replication is achieved by bumbling Brownian motion and ordinary thermodynamics in a biochemical porridge at a temperature of 35 C, it’s astonishing that the error-rate of DNA replication is about $10^{-9}$ per replicated nucleotide. How can this reliability be achieved, given that the energetic difference between a correct base-pairing and an incorrect one is only one or two hydrogen bonds and the thermal energy $kT$ is only about a factor of four smaller than the free energy associated with a hydrogen bond? If ordinary thermodynamics is what favours correct base-pairing, surely the frequency of incorrect base-pairing should be about

```math
f = \exp(-\Delta E / kT),
\qquad (19.21)
```

where $\Delta E$ is the free energy difference, i.e., an error frequency of $f \simeq 10^{-4}$? How has DNA replication cheated thermodynamics?

> 中文话题：热力学「欺骗」问题。$35$ °C 的生物化学糊里，DNA 复制靠布朗运动与普通热力学完成，错误率却低到每位约 $10^{-9}$；而正确与错误碱基配对的自由能差只有一两个氢键、$kT$ 只比一个氢键的自由能小约四倍，若按热力学就应该是 $f = e^{-\Delta E/kT} \simeq 10^{-4}$。问真实可靠性从何而来、DNA 复制是如何「绕过」热力学的。

<span style="color:#2471a3;">**[exercise-continued]**</span> The situation is equally perplexing in the case of protein synthesis, which translates an mRNA sequence into a polypeptide in accordance with the genetic code. Two specific chemical reactions are protected against errors: the binding of tRNA molecules to amino acids, and the production of the polypeptide in the ribosome, which, like DNA replication, involves base-pairing. Again, the fidelity is high (an error rate of about $10^{-4}$), and this fidelity can’t be caused by the energy of the ‘correct’ final state being especially low – the correct polypeptide sequence is not expected to be significantly lower in energy than any other sequence. How do cells perform error correction? (See Hopfield (1974), Hopfield (1980).)

> 中文话题：protein synthesis（蛋白质合成）的同一困惑——tRNA 与氨基酸的结合、以及 ribosome（核糖体）里多肽的生成这两步被保护免于出错；错误率约 $10^{-4}$ 却无法用「正确终态能量特别低」解释，因为正确多肽序列并不比别的序列显著低能。问细胞如何做纠错。

<span style="color:#c0392b">**Exercise 19.6.**</span> <span style="color:#7f8c8d">[2]</span> <span style="color:#2471a3;">**[exercise]**</span> While the genome acquires information through natural selection at a rate of a few bits per generation, your brain acquires information at a greater rate. Estimate at what rate new information can be stored in long term memory by your brain. Think of learning the words of a new language, for example.

> 中文话题：给你的 brain 估一个「长期记忆写入 information 的速率」（比特/秒量级），办法是拿「学一门新语言的单词」当具体场景来数。（可与本章 genome 的每代几比特对照。）

<span style="color:#00838f;">**19.7 Solutions（解答）**</span>

**Solution to exercise 19.1 (p.275).** 当 $N$ 足够小时，虽然种群的平均 fitness 在上升，一些不走运的比特会被冻结在坏状态。（这些坏 gene 有时被称为 hitchhiker，搭便车者。）homogeneity 假设这时失效。最终，所有个体都拥有相同的 genotype，它们主要是 1 比特、但也含有一些 0 比特。种群越小，被冻结的 0 比特数目预期越多。若 sex 理论要成立，种群规模 $N$ 最小能到多少？

我们从实验上发现：只有在种群规模 $N$ 小于约 $\sqrt{G}$ 时，基于 homogeneity 假设的理论才会拟合得很差。如果 $N$ 显著小于 $\sqrt{G}$，information 根本不可能以 $\sqrt{G}$ 那么大的速率被获取，因为「盲眼钟表匠的决策」所含的 information content 不可能大于每代 $2N$ 比特——这正是「指定 $2N$ 个孩子里哪些能繁殖」所需的比特数。Baum et al. (1995) 分析了一个类似模型，表明要让 hitchhiker 不太可能产生，种群规模 $N$ 应约为 $\sqrt{G}(\log G)^2$。



<span style="color:#7f8c8d">书内 p.280（PDF p.292）｜ 19 — Why have Sex? Information Acquisition and Evolution</span>

<span style="color:#7f8c8d">（本页的原文只有一段续尾：从“We find experimentally that the theory…”到“…to make hitchhikers unlikely to arise.”，共 7 行。为不把句子切断，这 7 行已在上一页 p291 末尾一并译出，**原文页归属是 PDF p.292**。此后本页余下的全部内容是解答的结束，本块另附一条译注。）</span>

<span style="color:#1e8449;">**[译注]** §19.7 只解了 19.1，而这条解答本身是本章最容易被略过、却最该停一下的地方：它把「模型成立」这件事**折算成了一条关于种群规模的信息论上界**。逻辑是硬的：每一代 natural selection 的全部决策，无非是「$2N$ 个孩子里哪 $N$ 个留下」，这个名单的信息量不超过 $\log_2\binom{2N}{N} \simeq 2N - \frac{1}{2}\log_2(\pi N)$ 比特，而它又不超过 $2N$ 比特；于是「每代获取 $\sqrt{G}$ 比特」这条本章主结论，要求 $2N \gtrsim \sqrt{G}$，即 $N \gtrsim \frac{1}{2}\sqrt{G}$——与原文「实验上 $N \gtrsim \sqrt{G}$ 才拟合得好」只差常数因子。**失效对象非常具体**：抽掉这条界，就会误以为 sex 的优势 $\sqrt{G}$ 是「无条件的、只需 $G$ 大」；实际上存在一个反向约束——$G$ 越大的物种，维持 sex 优势所需的**最小有效种群规模**越大（$G = 10^{9}$ 时要 $N \gtrsim 3\times10^{4}$ 量级，而 Baum 等人给的更严的 $\sqrt{G}(\log G)^2$ 要求 $N \gtrsim 2\times10^{6}$）。这正好解释了 §19.6 那句「只有在小规模、近交的种群中 sex 的好处才被削弱」——不是因为 sex 本身变差，而是因为 teacher（natural selection）每代能说的比特数被 $2N$ 卡死了。**失败模式可观测**：若有人拿 $\sqrt{G}$ 去套濒危物种（$N = 100$、$G = 10^{9}$），会预言「每代获取 $3\times10^{4}$ 比特」，而实际上限是 $2N = 200$ 比特，预言超真实值 150 倍，且 hitchhiker 冻结现象会占据主导（homogeneity 假设崩掉，正弦解 (19.14) 完全不再描述系统）。落点：本书 §19.7 Solution to exercise 19.1、§19.6 Exercise 19.1（书内 p.275）、Baum et al. (1995)；跨学科挂到 6.042J 的 $\binom{2N}{N}$ 计数与 Stirling 近似、以及 CS144 里「信道每符号容量受字母表大小限制」的同构结构。</span>



<span style="color:#7f8c8d">书内 p.281（PDF p.293）｜ Part IV Probabilities and Inference</span>

## Part IV — Probabilities and Inference（第四部分：概率与推断）

<span style="color:#7f8c8d">（本页是第四部分的分隔页，整页只有标题两行，无正文。以下为空白页内容的如实记录，未添加任何原文没有的文字。）</span>

> **Part IV**
> **Probabilities and Inference**



<span style="color:#7f8c8d">书内 p.282（PDF p.294）｜ About Part IV</span>

<span style="color:#00838f;">**About Part IV（关于第四部分）**</span>

能被 Bayesian inference（贝叶斯推断）方法处理——或许说「本该被处理」——的 inference problem（推断问题）数量极其庞大。例如本书讨论了：error-correcting code（纠错码）的 decoding problem（译码问题），从数据中推断 cluster 的任务，穿过带噪数据做 interpolation（插值）的任务，以及在给定带标签样本的条件下做 pattern classification（模式分类）的任务。解决这些问题的绝大多数技术可以分类如下。

> **Exact methods（精确方法）** 直接计算所需的数量。只有少数有意思的问题有直接解法，但 exact method 作为「解决更大问题中某些子任务的工具」是重要的。inference problem 的精确解法是第 21、24、25、26 章的主题。
>
> **Approximate methods（近似方法）** 可以再分为：
>
> 1. **deterministic approximations（确定性近似）**，包括 maximum likelihood（最大似然，第 22 章）、Laplace’s method（拉普拉斯方法，第 27、28 章）与 variational methods（变分方法，第 33 章）；以及
> 2. **Monte Carlo methods**（蒙特卡洛方法）——在这类技术里随机数扮演不可分割的角色——将在第 29、30、32 章讨论。

本书的这一部分**并不构成一个一维的故事**。更确切地说，这些想法织成了一张相互关联的线索之网，它们会在后续各章中重新组合。

第 3 章是本部分的荣誉成员，它讨论了一系列 inference problem 的简单例子及其 Bayesian 解法。

为了给本部分讨论的 inference 方法工具箱提供进一步的动机，第 20 章讨论 clustering（聚类）问题；后续各章讨论把 clustering 解释为 mixture modelling（混合模型建模）的概率解读。第 21 章讨论「用完全枚举所有 hypothesis 来处理概率分布」这个选项。第 22 章引入 maximization method（最大化方法）的想法，作为规避完全枚举所带来的巨大代价的一条路，并指出 maximum likelihood 不够好的理由。第 23 章回顾 Bayesian inference 中最常出现的那些概率分布。第 24、25、26 章讨论另一条规避完全枚举代价的路：marginalization（边缘化）。第 25 章以 error-correcting code 的 decoding 为例，讨论适用于 graphical model（图模型）的 message-passing（消息传递）方法。第 26 章把这些想法与第 16、17 章的 message-passing 概念结合起来。这几章是理解高级 error-correcting code 的先修内容。

第 27 章讨论 deterministic approximation，包括 Laplace’s method。本章是理解「学习算法中的 complexity control（复杂度控制）」这一主题的先修内容，那个想法在第 28 章被一般性地讨论。



<span style="color:#7f8c8d">书内 p.283（PDF p.295）｜ About Part IV</span>

第 29 章讨论 Monte Carlo methods。第 30 章给出 state-of-the-art 的 Monte Carlo 技术的细节。

第 31 章引入 Ising model（伊辛模型），作为检验概率方法的 test-bed（试验台）。一个精确的 message-passing 方法与一个 Monte Carlo 方法都被演示。研究 Ising model 的一个动机是它与若干 neural network 模型密切相关。第 32 章描述「精确的」Monte Carlo 方法，并演示它们应用于 Ising model。

第 33 章讨论 variational methods 及其应用于 Ising model 与简单统计推断问题（含 clustering）的情形。本章将帮助读者理解 Hopfield network（第 42 章）与 EM algorithm（EM 算法）——后者是 latent-variable modelling（潜变量建模）中的一个重要方法。第 34 章讨论一个特别简单的 latent variable model，叫作 independent component analysis（独立成分分析）。

第 35 章讨论一堆各式各样的 inference 话题。第 36 章讨论 decision theory（决策论）的一个简单例子。第 37 章讨论 sampling theory（抽样理论）与 Bayesian methods 之间的差别。

> <span style="color:#00838f;">**A theme: what inference is about（一个主题：inference 到底在做什么）**</span>

一个流传很广的误解是：inference 的目标是找出对某批数据「最可能的解释」。这个 most probable hypothesis（最可能的假设）也许值得关心，一些 inference 方法也确实去定位它；但这个假设只是**一个概率分布的峰**，而我们真正关心的是**整个分布**。正如我们在第 4 章看到的，一个信源最可能的输出，往往**不是**该信源的一个典型输出。同样地，在给定某批数据之后最可能的那个 hypothesis，对于「全部合理可信的 hypothesis 的集合」而言也可能是非典型的。

> <span style="color:#00838f;">**About Chapter 20（关于第 20 章）**</span>

在读下一章之前，建议先读习题 2.17（书内 p.36，PDF p.48）以及 §11.2（推断 Gaussian channel 的输入）。



<span style="color:#7f8c8d">书内 p.284（PDF p.296）｜ 20 An Example Inference Task: Clustering</span>

## 20 An Example Inference Task: Clustering（一个示例性推断任务：聚类）

人的大脑擅长在数据中找到规律性（regularity）。表达规律性的一种方式，是把一组对象放进若干「彼此相似的组」。例如，生物学家发现自然界的绝大多数对象都落入两类之一：棕色且会跑掉的，以及绿色且不会跑掉的。他们管第一组叫 animals（动物），管第二组叫 plants（植物）。我们把这种「把事物归组」的操作称为 clustering（聚类）。如果生物学家进一步把植物这个 cluster 再分成若干 sub-cluster（子簇），我们会把这种操作称为「hierarchical clustering（层次聚类）」；不过我们暂时还不谈 hierarchical clustering。本章只讨论：取 $N$ 个对象，把它们分成 $K$ 个 cluster 的办法。

做 clustering 有几个动机。**第一，一个好的 clustering 有预测力。** 当一位早期生物学家遇到一个从未见过的新的绿色东西时，他头脑里关于植物与动物的内部模型会为这个绿色东西的诸多属性补上预测：它不太可能跳到他身上把他吃掉；如果他摸它，他可能会被刮伤或者被刺；如果他吃它，他可能会觉得恶心。这些预测虽然不确定，但都有用，因为它们帮助这位生物学家把资源投放得当（例如「花多少时间提防捕食者」）。于是，我们做 clustering，是因为我们相信底层的 cluster label（簇标签）是有意义的、会带来对数据的更高效描述、并会帮我们选择更好的行动。这一类 clustering 有时被称为「mixture density modelling（混合密度建模）」，而衡量「预测模型干得怎么样」的目标函数就是数据的 information content，即 $\log 1/P(\{x\})$。

**第二，cluster 可以是有用的交流辅助，因为它允许 lossy compression（有损压缩）。** 这位生物学家可以这样给朋友指路：「走到右边第三棵树，然后右转」——而不是「先走过那棵结红果的大绿东西，再走过那棵带刺的大绿东西，然后……」。那个简短的类别名「树」之所以有用，是因为它足以**识别**一个对象。类似地，在 lossy image compression（有损图像压缩）中，目标是用尽可能少的比特传达一幅图像的合理复制品；做到这一点的一种办法是把图像切成 $N$ 个小 patch（小块），并在一个由 $K$ 个 image-template（图像模板）组成的 alphabet 里为每个 patch 找一个最接近的匹配；然后我们通过发送匹配模板的标签列表 $k_1, k_2, \ldots, k_N$ 来传出一幅「近似贴合的」图像。创建一个好的 image-template 库，这个任务等价于找出一组 cluster centre（簇中心）。这一类 clustering 有时被称为「vector quantization（矢量量化）」。

我们可以用一条 assignment rule（指派规则）$x \to k(x)$ 把 datapoint（数据点）$x$ 指派到 $K$ 个 codename（代号）之一，再用一条 reconstruction rule（重建规则）$k \to m(k)$ 把代号还原，从而把一个 vector quantizer（矢量量化器）形式化；目标是选择函数 $k(x)$ 与 $m(k)$，使得



<span style="color:#7f8c8d">书内 p.285（PDF p.297）｜ 20.1: K-means clustering</span>

期望 distortion（失真）最小，而 distortion 可以定义为

```math
D = \sum_x P(x)\,\frac{1}{2}\left[m(k(x)) - x\right]^2 .
\qquad (20.1)
```

[理想的目标函数本该是「最小化人对图像所感知的那份 distortion」。可是人感知到的 distortion 很难量化，所以 vector quantization 与 lossy compression 并不像 data modelling 与 lossless compression 那样是定义得干净利落的问题。] 在 vector quantization 里，我们并不一定相信那些模板 $\{m(k)\}$ 有什么自然含义；它们只是干活的工具。顺带一提，注意 vector quantization 的 assignment rule（也就是 encoder，编码器）与「对 error-correcting code 做 decoding（译码）」之间的相似性。

**第三，建立 cluster 模型的理由之一是：cluster 模型的失败可能提示某些值得特别关注的有趣对象。** 如果我们训练了一个 vector quantizer 去压缩海面的卫星图片、而且它干得不错，那么也许那些**压不好**的图像 patch 就是含有船只的 patch！如果这位生物学家遇到一个绿色东西、并且看到它跑掉（或滑走），这个与其 cluster 模型（模型说绿色东西不会跑掉）之间的失配就在提示他「特别留意」。一个人不可能把全部时间都花在对各种东西着迷上；cluster model 可以帮我们从世界里众多对象中筛出那些真正值得注意的。

[Figure 20.1：$N = 40$ 个数据点。图中是二维平面上的 40 个点，作为后续 K-means 演示（图 20.3、20.4）的输入数据。无法复原：40 个点的具体坐标。]

**第四，喜欢 clustering 算法的理由之一是：它们可以作为神经系统学习过程的模型。** 我们现在要讨论的 clustering 算法——K-means 算法——就是一个 competitive learning（竞争学习）算法的例子。这个算法的工作方式是：让 $K$ 个 cluster 相互竞争，争夺对数据点的所有权。

> <span style="color:#7f8c8d">**关于这个名字……** 据我所知，K-means clustering 里的「K」不过是指「所选定的 cluster 个数」。如果 Newton 当年也采用同样的命名政策，也许我们在学校里学的就会是「关于变量 x 的微积分」了。这名字很傻，但我们只能将就着用。</span>

<span style="color:#00838f;">**20.1 K-means clustering（K-means 聚类）**</span>

K-means 算法是一个把 $I$ 维空间中的 $N$ 个数据点分成 $K$ 个 cluster 的算法。每个 cluster 用一个向量 $m^{(k)}$ 参数化，这个向量称为它的 mean（均值）。

数据点记作 $\{\mathbf{x}^{(n)}\}$，其中上标 $n$ 从 1 跑到数据点个数 $N$。每个向量 $\mathbf{x}$ 有 $I$ 个分量 $x_i$。我们将假设 $\mathbf{x}$ 所在的空间是实空间，并且我们有一个定义点与点之间距离的 metric（度量），例如

```math
d(\mathbf{x}, \mathbf{y}) = \frac{1}{2}\sum_i \left(x_i - y_i\right)^2 .
\qquad (20.2)
```

为了启动 K-means 算法（Algorithm 20.2），$K$ 个 mean $\{m^{(k)}\}$ 要以某种方式初始化，例如取随机值。此后 K-means 是一个迭代的两步算法。在 assignment step（指派步）中，每个数据点 $n$ 被指派给最近的 mean。在 update step（更新步）中，各个 mean 被调整，去匹配「它们所负责的那些数据点」的样本均值。

Figure 20.3 在一个玩具二维数据集上演示了 K-means 算法，那里用了 2 个 mean。点到两个 cluster 的归属用两种点型表示，两个 mean 用圆圈表示。算法在三次迭代之后收敛；此时归属不再变化，因此更新时 mean 也不再移动。**K-means 算法总是收敛到一个不动点。**



<span style="color:#7f8c8d">书内 p.286（PDF p.298）｜ 20 — An Example Inference Task: Clustering</span>

<span style="color:#00838f;">**Algorithm 20.2. The K-means clustering algorithm（K-means 聚类算法）**</span>

> **Initialization（初始化）.** 把 $K$ 个 mean $\{m^{(k)}\}$ 设为随机值。
>
> **Assignment step（指派步）.** 每个数据点 $n$ 被指派给最近的 mean。我们把「点 $\mathbf{x}^{(n)}$ 所属 cluster $k(n)$」的猜测记为 $\hat k^{(n)}$。
>
> ```math
> \hat k^{(n)} = \arg\min_k \left\{ d\left(m^{(k)}, \mathbf{x}^{(n)}\right) \right\}.
> \qquad (20.3)
> ```
>
> 这种「把点指派到 cluster」还有另一种等价的表示，就是 responsibilities（责任度），即指示变量 $r^{(n)}_k$。在 assignment step 中，若 mean $k$ 是离数据点 $\mathbf{x}^{(n)}$ 最近的 mean，我们就令 $r^{(n)}_k$ 为一；否则 $r^{(n)}_k$ 为零。
>
> ```math
> r^{(n)}_k = \begin{cases}
> 1 & \text{if } \hat k^{(n)} = k \\
> 0 & \text{if } \hat k^{(n)} \neq k .
> \end{cases}
> \qquad (20.4)
> ```
>
> **并列怎么办？**——我们并不预期两个 mean 离某个数据点恰好同样远；但若真的发生并列，$\hat k^{(n)}$ 取获胜的 $\{k\}$ 中最小的那个。
>
> **Update step（更新步）.** 模型参数，也就是各个 mean，被调整去匹配「它们所负责的那些数据点」的样本均值。
>
> ```math
> m^{(k)} = \frac{\sum_n r^{(n)}_k \mathbf{x}^{(n)}}{R^{(k)}}
> \qquad (20.5)
> ```
>
> 其中 $R^{(k)}$ 是 mean $k$ 的总 responsibility，
>
> ```math
> R^{(k)} = \sum_n r^{(n)}_k .
> \qquad (20.6)
> ```
>
> **没有责任度的 mean 怎么办？**——若 $R^{(k)} = 0$，我们就把 mean $m^{(k)}$ 留在原处不动。
>
> **重复 assignment step 与 update step，直到归属不再变化。**



<span style="color:#7f8c8d">书内 p.287（PDF p.299）｜ 20.1: K-means clustering</span>

[Figure 20.3：它演示的是什么——K-means 算法应用在一个 40 点的数据集上，$K = 2$。图上串有七帧：Data → Assignment → Update → Assignment → Update → Assignment → Update。核心主张：**两个 mean 在三次迭代之后演化到稳定位置**，最后一帧的 assignment 与 update 不再改变任何东西。无法复原：各帧中各点的坐标与两个圆圈的精确位置。]

[Figure 20.4：它演示的是什么——同一批 40 点数据上跑**两次**独立的 K-means（Run 1 与 Run 2），两次都用 $K = 4$。核心主张：**结果依赖于初始条件**——两次跑出不同的解；图中每一帧是相继的一次 assignment step。Run 1 在五次迭代后到达稳态，数据点相当均匀地分在四个 cluster 里；Run 2 在六次迭代后，一半数据点在同一个 cluster 里，其余的在另外三个 cluster 之间分摊。无法复原：两轮迭代中每帧的点归属与 mean 位置。]

<span style="color:#c0392b">**Exercise 20.1.**</span> <span style="color:#7f8c8d">[4, p.291]</span> <span style="color:#2471a3;">**[exercise]**</span> See if you can prove that K-means always converges. [Hint: find a physical analogy and an associated Lyapunov function.] [A Lyapunov function is a function of the state of the algorithm that decreases whenever the state changes and that is bounded below. If a system has a Lyapunov function then its dynamics converge.]

> 中文话题：证明 K-means 总是收敛。提示：找一个物理类比，以及与之配套的 Lyapunov function（Lyapunov 函数）——即一个「只要状态改变就下降、且有下界」的状态函数；若系统存在这样的函数，其动力学收敛。（书后 p.291 有解答，本块不含；见 PDF p.303 之后的 solutions。）

用更多 mean（4 个）的 K-means 算法在 Figure 20.4 中演示。**算法的结局依赖初始条件。** 第一种情形在五次迭代之后找到一个稳态，其中数据点相当均匀地分在四个 cluster 之间。第二种情形在六次迭代之后，一半数据点落在同一个 cluster 里，其余的在另外三个 cluster 之间分摊。

<span style="color:#00838f;">**Questions about this algorithm（关于这个算法的若干疑问）**</span>

K-means 算法有几个 ad hoc（临时凑合）的特征。为什么 update step 要把「mean」设成「被指派点的均值」？距离 $d$ 是从哪里来的？如果我们对 $\mathbf{x}$ 与 $m$ 之间的距离采用别的度量会怎样？我们怎么挑「最好的」距离？[在 vector quantization 里，距离函数是作为问题定义的一部分给定的；但我这里假设我们关心的是 data-modelling，而不是 vector quantization。] 我们怎么选 $K$？在给定 $K$ 之下找到了多个不同的 clustering 之后，我们怎么在它们之间挑一个？

<span style="color:#1e8449;">**[译注]** 「K-means 总是收敛到一个不动点」这句断言与 Exercise 20.1 的 Lyapunov 提示之间，隔着一步容易被跳过、但决定了这个算法**为什么值得学**的观察：assignment step 与 update step **下降的是同一个目标函数**，(20.1) 里的 $D$ 正是那个 Lyapunov 函数。把 (20.5) 代入 $D$ 并只用 (20.4) 的指示变量表示，得

```math
D(\{r\}, \{m\}) = \frac{1}{2}\sum_{n}\sum_{k} r^{(n)}_k \left\| m^{(k)} - x^{(n)} \right\|^2 .
```

assignment step 对每个 $n$ **独立**地把 $r^{(n)}_k$ 指向 $d(m^{(k)}, x^{(n)})$ 最小者，故 $D$ 只减不增；update step 把 $m^{(k)}$ 移到 $\{\mathbf{x}^{(n)} : r^{(n)}_k = 1\}$ 的算术均值，而这正是对 $m^{(k)}$ 的二次型取一阶条件 $\partial D/\partial m^{(k)} = \sum_n r^{(n)}_k (m^{(k)} - x^{(n)}) = 0$ 的解，故 $D$ 同样只减不增（这也顺带回答了原文「为什么均值就是均值」——不是灵机一动，是 (20.1) 选成平方误差的**必然结果**）。**失效对象**：抽掉「两步共用同一个 $D$」这一点，K-means 看上去就只是一个 ad hoc 的交替启发式，Exercise 20.1 无从下手；更实质的是，收敛证明依赖 $D$ 的**取值集合有限且单调下降**（$N$ 个点分给 $K$ 个 cluster 只有 $K^N$ 种指派、每种指派对应的 $D$ 是确定的），于是迭代次数上界是 $D$ 可能取到的不同值个数——这只给出有限步终止，**不给多项式时间**，也**不保证全局最优**（图 20.4 两次跑出不同答案正是局部极小的直接证据）。**失败模式具体到可观测**：若误把「收敛」当成「收敛到正确答案」，就会以为 K-means 是 $D$ 的全局最小化器，于是无法解释图 20.5b 那四个「本该属于宽 cluster 却被划给窄 cluster」的点——那不是实现 bug，而是 $D$ 的局部极小在「只按距离、不看每个 cluster 的权重与宽度」这一模型下的必然产物。落点：本书 §20.1 式 (20.1)–(20.6)、Algorithm 20.2、Exercise 20.1（书内 p.287）、图 20.4 与 20.5；跨学科挂到 Strang 线代的「投影到子空间即最小二乘最优」与 6.006 的「贪心/坐标下降只保证局部最优」，以及 CS144 里 vector quantization 与 lossy compression 的同一个 $D$。</span>



<span style="color:#7f8c8d">书内 p.288（PDF p.300）｜ 20 — An Example Inference Task: Clustering</span>

[Figure 20.5：它演示的是什么——K-means 在一个「两个不相似 cluster」的案例上的表现。(a) 称为「little ’n’ large」的数据：75 个点，来自两个 Gaussian 的混合，右手那个 Gaussian 权重更小（只占五分之一的数据点）、且是个更窄的 cluster。(b) 取 $K = 2$ 个 mean 时得到的一组稳定归属与均值。核心主张：**有四个属于那个宽 cluster 的点被错误地指派给了窄 cluster**，而且两个 mean 最后都被挤到了真实簇中心的左边；指派给右手 cluster 的点在图中用加号表示。无法复原：75 个点的具体坐标、两个 Gaussian 的真实参数。]

[Figure 20.6：它演示的是什么——两个**细长**的 cluster（a），以及 K-means 找到的稳定解（b）。核心主张：K-means 唯一的稳定态是「把两个簇各切一半」——因为算法只按到 mean 的距离指派，没有任何表示 cluster 尺寸或形状的手段。无法复原：点的坐标与切分线的具体位置。]

继续讨论「K-means 可能被视为失败」的那些情形。

**K-means 可能被看作失败的情形。**

当我们去寻找「算法表现很糟」的情形（糟的标准是街头路人所谓的「聚类」）时，更多疑问就冒出来了。Figure 20.5a 显示的 75 个数据点由两个 Gaussian 的混合生成。右手那个 Gaussian 权重更小（只占五分之一的数据点），而且它是一个不那么宽的 cluster。Figure 20.5b 显示用 $K = 2$ 个 mean 做 K-means clustering 的结局。大 cluster 的四个数据点被指派给了小 cluster，两个 mean 最终都被挪到了真实簇中心的左边。K-means 算法**只**考虑 mean 与数据点之间的距离；它没有任何表示每个 cluster 的权重或宽度的手段。结果是：实际上属于宽 cluster 的数据点被错误地指派给了窄 cluster。

Figure 20.6 显示 K-means 表现糟糕的另一个案例。数据显然落入两个细长的 cluster。但 K-means 算法唯一的稳定态就是 Figure 20.6b 所示的样子：两个 cluster 被**从中间各切一半**！这两个例子说明，K-means 算法里的距离 $d$ 有点问题。K-means 算法没有办法表示 cluster 的大小或形状。

对 K-means 的最后一条批评是：它是一个「hard」算法而不是「soft」算法——点被指派到恰好一个 cluster，而被指派到某个 cluster 的所有点在该 cluster 内一律平等。位于两个或多个 cluster 边界附近的点，按理说应当对「它有可能被指派到的所有 cluster」的位置确定都**部分地**起作用。但在 K-means 算法里，每个边界点被一把扔进一个 cluster，然后

<span style="color:#7f8c8d">（原文此处跨页截断：「…each borderline point is dumped in one cluster, and」，句子未完，下接 PDF p.301，不在本块范围内。）</span>

---

<span style="color:#7f8c8d">**本块结束**（PDF p.300 = 书内 p.288）。本文件覆盖 PDF p.281–300 共 20 页：第 19 章全章（§19.1–§19.7）、Part IV 分隔页、About Part IV、第 20 章开头至 §20.1 的「K-means 何时算失败」。**PDF p.301 起（书内 p.289 起）为第 20 章 §20.1 的续、§20.2 Soft K-means clustering 及以后，不在本文件内。**</span>



## 书内 p289 · §20.2 Soft K-means clustering（软 K-means 聚类）

<span style="color:#555;">（承接书内 p288 的末句，讲 K-means 里每个点的投票权：）</span>

它（每个数据点）在所属的那个簇里，与簇内其余所有点享有**同等的一票**；而在任何别的簇里，**一票都没有**。

### 20.2 Soft K-means clustering（软 K-means 聚类）

K-means 的这些毛病，正是 **soft K-means algorithm（软 K-means 算法）** 的动因，见 Algorithm 20.7。这个算法只有**一个**参数 $\beta$，我们可以把它叫作 **stiffness（刚性参数）**。

**Assignment step（分配步）** 每个数据点 $x^{(n)}$ 对每一个 mean（均值点）都得到一个「软」的 **degree of assignment（分配度）**。我们把 $x^{(n)}$ 被分配到簇 $k$ 的程度，称为簇 $k$ 对点 $n$ 的 **responsibility（责任度）** $r_k^{(n)}$：

```math
r_k^{(n)} = \frac{\exp\left(-\beta\, d(m^{(k)}, x^{(n)})\right)}{\sum_{k'} \exp\left(-\beta\, d(m^{(k')}, x^{(n)})\right)} .
```

（20.7）

第 $n$ 个点的 $K$ 个 responsibilities 之和为 $1$。

**Update step（更新步）** 模型参数——也就是那些 means——被调整到「它所负责的那些数据点的样本均值」上去：

```math
m^{(k)} = \frac{\sum_n r_k^{(n)} x^{(n)}}{R^{(k)}} ,
```

（20.8）

其中 $R^{(k)}$ 是 mean $k$ 的**总 responsibility**：

```math
R^{(k)} = \sum_n r_k^{(n)} .
```

（20.9）

<span style="color:#1a5276;">**Algorithm 20.7 · Soft K-means algorithm, version 1（软 K-means 算法第一版）**</span>

（原书此框的逐步伪码与硬 K-means 一一对应：初始化 means → 反复做 assignment step 与 update step，直到 responsibilities 与 means 不再变化。）

请注意这个 soft K-means 算法与硬 K-means（Algorithm 20.2）的相似之处。**update step 完全相同**；唯一的差别是 responsibilities $r_k^{(n)}$ 可以取 $0$ 到 $1$ 之间的值。而在 K-means 里，分配 $\hat{k}^{(n)}$ 是在距离上取一个 `min`；这里给 responsibilities 定值的规则，是一个 **soft-min（软最小）**，即 (20.7)。

<span style="color:#7d3c98;">**Exercise 20.2**</span> [exercise] *Show that as the stiffness $\beta$ goes to $\infty$, the soft K-means algorithm becomes identical to the original hard K-means algorithm, except for the way in which means with no assigned points behave. Describe what those means do instead of sitting still.*

> [exercise 摘要] 证明 $\beta \to \infty$ 时 soft-min 退化为硬 min，两算法完全相同；**唯一残留差别**是「没有任何点归它管」的那个 mean：硬版让它原地不动，软版让它往哪里跑？（答案方向：$R^{(k)} \to 0$ 时 (20.8) 是 $0/0$，实际数值上会被其余点的极小 responsibilities 拽向全体数据的重心。）

从量纲上看，stiffness $\beta$ 是 **inverse-length-squared（长度的负二次方）**，所以可以给它配一个 **lengthscale（长度尺度）**：

```math
\sigma \equiv 1/\sqrt{\beta} .
```

soft K-means 算法在图 20.8 中演示。lengthscale 由环绕四个 means 的圆的**半径**表示。每一幅子图给出的是：对**不同的** lengthscale $\sigma$，算法最终收敛到的那个 fixed point（不动点）。

### 20.3 Conclusion（小结）

到此为止，我们也许已经通过引入一个额外的**复杂度控制参数** $\beta$，修好了原始 K-means 算法的一部分毛病。可是 $\beta$ 该怎么设？还有 elongated clusters（细长簇）的问题——

[Figure 20.8：soft K-means version 1 在 40 点数据上，随 lengthscale 由大到小逐级分裂的五个收敛态]

---



## 书内 p290 · 图 20.8 图注 · 小结续 · 习题

**Figure 20.8（图注译文）** Soft K-means algorithm, version 1，施用于一个**40 个点**的数据集，$K = 4$。隐含的 lengthscale 参数 $\sigma = 1/\beta^{1/2}$ 由大变小地变化。每幅图显示四个 means 的状态，隐含 lengthscale 由四个圆的半径表示；这是跑了几十次迭代之后的结果。**在最大的 lengthscale 上，四个 means 精确地全部收敛到数据的均值（同一个点）**。接着四个 means 分成**两组、每组两个**。在更短的 lengthscale 上，这两对各自又 **bifurcate（分岔）** 成子群。

接着上一页的话说完：以及**权重不等、宽度不等**的簇，这些问题怎么办？只加一个 stiffness 参数 $\beta$，是不可能让这些麻烦统统消失的。

我们会在后面某一章回到这些问题，那时我们会发展出聚类的 **mixture-density-modelling（混合密度建模）** 视角。

### Further reading（延伸阅读）

聚类的 **vector quantization（矢量量化）** 进路，见 (Luttrell, 1989; Luttrell, 1990)。

### 20.4 Exercises（习题）

<span style="color:#7d3c98;">**Exercise 20.3**</span> [exercise] *Explore the properties of the soft K-means algorithm, version 1, assuming that the datapoints $\{x\}$ come from a single separable two-dimensional Gaussian distribution with mean zero and variances $(\mathrm{var}(x_1), \mathrm{var}(x_2)) = (\sigma_1^2, \sigma_2^2)$, with $\sigma_1^2 \gt \sigma_2^2$. Set $K = 2$, assume $N$ is large, and investigate the fixed points of the algorithm as $\beta$ is varied. [Hint: assume that $m^{(1)} = (m, 0)$ and $m^{(2)} = (-m, 0)$.]*

> [exercise 摘要] 数据本来只有一个簇（各向异性高斯），却强迫 $K=2$；扫 $\beta$ 找出软算法在什么条件下会**凭空劈成两半**。这是把「过拟合」翻译成一个可算的临界条件，答案就是下一节解出的 $\sigma_1^2 \beta = 1$。

<span style="color:#7d3c98;">**Exercise 20.4**</span> [exercise] *Consider the soft K-means algorithm applied to a large amount of one-dimensional data that comes from a mixture of two equal-weight Gaussians with true means $\mu = \pm 1$ and standard deviation $\sigma_P$, for example $\sigma_P = 1$. Show that the hard K-means algorithm with $K = 2$ leads to a solution in which the two means are further apart than the two true means. Discuss what happens for other values of $\beta$, and find the value of $\beta$ such that the soft algorithm puts the two means in the correct places.*

> [exercise 摘要] 硬 K-means 在「真均值 $\pm 1$ 的两个对称高斯」上会**把两个均值估得比真值更开**——这是系统性偏差，不是随机噪声；再问：取多大的 $\beta$ 才能把这个偏差刚好抵消回 $\pm 1$？（数值答案在书内 p481 的习题解里，本块不覆盖。）

---



## 书内 p291 · §20.5 Solutions（习题解答）

### 20.5 Solutions

**Solution to exercise 20.1（书内 p287 那道题）** 我们可以给 K-means 算法的状态配一个 **energy（能量）**：在每一个点 $x^{(n)}$ 与「对它负责的那个 mean」之间连一根弹簧。一根弹簧的能量正比于它长度的**平方**，即 $\beta\, d(x^{(n)}, m^{(k)})$，其中 $\beta$ 是弹簧的 stiffness。

所有弹簧的总能量，就是这个算法的一个 **Lyapunov function（李雅普诺夫函数）**，因为：

（a）**assignment step 只会让能量下降**——一个点只有在「它那根弹簧的长度会变短」的时候才会改换门庭；

（b）**update step 只会让能量下降**——把 $m^{(k)}$ 移到均值处，正是最小化它那些弹簧能量的做法；

（c）**能量有下界**——这是 Lyapunov function 的第二个条件。

既然算法有 Lyapunov function，它就收敛。

**Solution to exercise 20.3（书内 p290 那道题）** 若两个 means 初始化为 $m^{(1)} = (m, 0)$ 与 $m^{(1)} = (-m, 0)$†，则对位于 $x_1, x_2$ 的一个点，assignment step 给出

```math
r_1(x) = \frac{\exp\left(-\beta(x_1 - m)^2/2\right)}{\exp\left(-\beta(x_1 - m)^2/2\right) + \exp\left(-\beta(x_1 + m)^2/2\right)}
```

（20.10）

```math
= \frac{1}{1 + \exp\left(-2\beta m x_1\right)} ,
```

（20.11）

而更新后的 $m$ 是

```math
m' = \frac{\int \mathrm{d}x_1\, P(x_1)\, x_1\, r_1(x)}{\int \mathrm{d}x_1\, P(x_1)\, r_1(x)}
```

（20.12）

```math
= 2 \int \mathrm{d}x_1\, P(x_1)\, x_1\, \frac{1}{1 + \exp\left(-2\beta m x_1\right)} .
```

（20.13）

† **原文自身的问题**：这里第二个初始化写成了 $m^{(1)} = (-m, 0)$，按上下文（$K=2$、两个 means 对称）应当是 $m^{(2)}$。这是原书排版错误，不是记号约定。

现在，$m = 0$ 是一个 fixed point（不动点），但问题在于：它是**稳定**的还是**不稳定**的？对于很小的 $m$（即 $\beta \sigma_1 m \ll 1$），可以 Taylor 展开

```math
\frac{1}{1 + \exp\left(-2\beta m x_1\right)} \simeq \frac{1}{2}\left(1 + \beta m x_1\right) + \cdots
```

（20.14）

于是

```math
m' \simeq \int \mathrm{d}x_1\, P(x_1)\, x_1\, (1 + \beta m x_1)
```

（20.15）

```math
= \sigma_1^2 \beta m .
```

（20.16）

对小的 $m$，在这套映射下 $m$ 要么指数增长、要么指数衰减，取决于 $\sigma_1^2 \beta$ 是**大于**还是**小于** $1$。不动点 $m = 0$ **当**

```math
\sigma_1^2 \le 1/\beta
```

（20.17）

时稳定，否则不稳定。［顺带一提：这个推导说明该结论是**一般**的，对任何方差为 $\sigma_1^2$ 的真实分布 $P(x_1)$ 都成立，并不限于高斯。］

若 $\sigma_1^2 \gt 1/\beta$，就发生 **bifurcation（分岔）**：原先在 $m = 0$ 的不稳定不动点两侧，各出现一个稳定不动点。为了展示这个分岔，图 20.10 给出了在**固定** $\beta = 1$、一维数据标准差为 $\sigma_1$ 时，对各个 $\sigma_1$ 跑 soft K-means 的结果。图 20.11 从另一个视角展示这个 **pitchfork bifurcation（叉形分岔）**：数据的标准差 $\sigma_1$ 固定，而算法的 lengthscale $\sigma = 1/\beta^{1/2}$ 沿横轴变化。

[Figure 20.10：$\beta$ 固定时，稳定 mean 位置随数据标准差 $\sigma_1$ 的变化——粗线是数值结果，细线是 (20.22) 的解析近似]

**图 20.10 的坐标读数（原书轴标注）**：横轴 $\sigma_1$ 从 $-4$ 到 $4$（原书把纵轴刻度 0…4 与横轴 $-4$…4 一并排印，说明这是「均值位置 vs $\sigma_1$」的对称展开画法）；**曲线本身的精确形状无法从 PDF 文字层复原，此处只保留轴范围与图注，不臆造拐点坐标。**

[Figure 20.11：$\sigma_1$ 固定时，稳定 mean 位置随算法 lengthscale $1/\beta^{1/2}$ 的变化]

**图 20.11 的坐标读数**：纵轴 $-0.8$ 到 $0.8$，横轴 $0$ 到 $2$；另附 $x$ 轴 $-2$…$2$ 的两个小插图画数据密度与最终 mean 位置（原书以 `Data density` / `Mean locns.` 标注）。**叉臂的精确形状同样不可复原。**

---



## 书内 p292 · 解 20.3 续 · 习题 20.5 及其解答

这里有一个**廉价的**理论，用来建模超过分岔点之后被拟合出来的参数 $\pm m$ 会怎样变化，办法是把级数展开继续往下推。这种「把级数续到分岔之外」的做法相当可疑，因为本来就不能指望该级数在分岔点之外收敛，**但这个理论居然拟合得很好**。

我们把解析近似再多取一项：

```math
\frac{1}{1 + \exp\left(-2\beta m x_1\right)} \simeq \frac{1}{2}\left(1 + \beta m x_1 - \frac{1}{3}(\beta m x_1)^3\right) + \cdots
```

（20.18）

于是可以解出分岔的**领头阶形状**，它依赖于该分布的**四阶矩**：

```math
m' \simeq \int \mathrm{d}x_1\, P(x_1)\, x_1 \left(1 + \beta m x_1 - \frac{1}{3}(\beta m x_1)^3\right)
```

（20.19）

```math
= \sigma_1^2 \beta m - \frac{1}{3}(\beta m)^3\, 3\sigma_1^4 .
```

（20.20）

［在 (20.20) 处我们用了「$P(x_1)$ 是高斯」这一事实来求四阶矩：高斯的三阶矩为 $0$、四阶矩为 $3\sigma_1^4$，所以 $\int P x_1^3 = 0$、$\int P x_1^4 = 3\sigma_1^4$。］

这个映射在满足下式的 $m$ 处有不动点：

```math
\sigma_1^2 \beta \left(1 - (\beta m)^2 \sigma_1^2\right) = 1 ,
```

（20.21）

也就是

```math
m = \pm\, \beta^{-1/2}\, \frac{\left(\sigma_1^2 \beta - 1\right)^{1/2}}{\sigma_1^2 \beta} .
```

（20.22）

图 20.10 中的**细线**就是这条理论近似。图 20.10 展示的是**固定 $\beta$ 时**分岔随 $\sigma_1$ 的变化；图 20.11 展示的是**固定 $\sigma_1$ 时**分岔随 $1/\beta^{1/2}$ 的变化。

<span style="color:#7d3c98;">**Exercise 20.5**</span> [exercise] *Why does the pitchfork in figure 20.11 tend to the values $\sim \pm 0.8$ as $1/\beta^{1/2} \to 0$? Give an analytic expression for this asymptote.*

> [exercise 摘要] 当算法的 lengthscale 趋于 $0$（即 $\beta \to \infty$、分配趋于完全硬）时，两个稳定 mean 并不趋于 $\pm 1$（真均值），而是趋于 $\pm 0.798$。问：这个数从哪来？

**Solution to exercise 20.5（解答）** 这个渐近值就是 **rectified Gaussian（整流高斯）** 的均值：

```math
\left(\int_0^{\infty} \mathrm{Normal}(x, 1)\, x\, \mathrm{d}x\right) \Big/ 1/2 \;=\; \sqrt{2/\pi} \;\simeq\; 0.798 .
```

（20.23）

<span style="color:#1e8449;">**[译注]** $\sqrt{2/\pi}\approx 0.798$ 是硬 K-means 系统性偏差的闭式证据，不是拟合噪声。(20.23) 的来历：$\beta\to\infty$ 时 responsibilities 退化成半轴指示函数，(20.13) 于是只对 $x_1 \gt 0$ 求加权均值，得 $1/\sqrt{2\pi}\approx 0.3989$，再除以这段区间的质量 $1/2$，即 $0.7979$。三步都可手算，没有任何数值拟合。它给的方向感是：真均值 $\pm 1$、间距只有 $2\sigma_P$，硬 K-means 给出 $\pm 0.798$，偏差 $0.202$，约 20%，符号向内；而 Exercise 20.4 在 $\sigma_P$ 更小时给出向外撑的结果——**偏差的符号取决于簇间重叠度**，重叠越大越向内塌。**消失测试**：抽掉 (20.11) 这个 logistic 封闭形式，就只能对每个 $\beta$ 数值积分一次 (20.12)，(20.23) 的解析渐近与图 20.10 的细线全部写不出，只剩网格扫描。**落点**：§20.5 (20.23)、Exercise 20.4 / 20.5；对照 Bishop *PRML* §9.2（同款 $\sqrt{2/\pi}$）。定量地说：若数据真的只来自一个高斯，而硬把 $K$ 设成 $2$，$0.798$ 这个数就是**模型错配的价钱**——两个本该重合的均值被撑开到间距 $1.596$，而制造这一切所需的临界条件只是 $\sigma_1^2\beta \gt 1$。</span>

---



## 书内 p293 · 第 21 章 Exact Inference by Complete Enumeration（用完全枚举做精确推断）

# 21 Exact Inference by Complete Enumeration

我们打开工具箱，来讨论处理概率的一种**暴力**推断方法：把所有 hypotheses（假设）**完全枚举**出来，并逐一评估它们的概率。这是一个**精确**方法；而把它真正做下去的困难程度，正好motivate 后面几章要引入的那些更聪明的精确方法与近似方法。

## 21.1 The burglar alarm（防盗警报）

Bayesian probability theory（贝叶斯概率论）有时被称为「被放大的常识」（common sense, amplified）。在思考下面这些问题时，请先问问你的常识觉得答案是多少；然后我们来看贝叶斯方法如何**证实**你的日常直觉。

[Figure 21.1：防盗警报问题的 belief network（信念网络）——四个节点 Earthquake / Burglar / Alarm / Radio / Phonecall 的有向连接]

**Figure 21.1（图注）** 防盗警报问题的 belief network。原书用有向弧画出五个随机变量之间的依赖：Burglar 与 Earthquake 指向 Alarm，Alarm 指向 Phonecall，Earthquake 指向 Radio。**弧的具体落点与节点排布在文字层里只剩标签，此处按 (21.1) 的因子分解复原连接关系，图形位置不复原。**

<span style="color:#b9770e;">**Example 21.1（例）**</span> Fred 住在洛杉矶，每天开 60 英里车去上班。某天他在上班时接到邻居电话，说 Fred 家的防盗警报在响。**今天他家有窃贼的概率是多少？**

在开车回家查看的路上，Fred 从收音机里听到：当天在他家附近发生了一次**小地震**。「哦，」他松了一口气说，「那大概是地震触发了警报吧。」**那么他家有窃贼的概率又是多少？**（据 Pearl, 1988）

我们引入变量：$b$（今天 Fred 家有窃贼）、$a$（警报在响）、$p$（Fred 接到邻居报告警报的电话）、$e$（今天 Fred 家附近发生了小地震）、$r$（Fred 听到了地震的广播报道）。这些变量的联合概率可以这样因子分解：

```math
P(b, e, a, p, r) = P(b)\,P(e)\,P(a \mid b, e)\,P(p \mid a)\,P(r \mid e) ,
```

（21.1）

而各概率的合理取值如下：

**1. 有窃贼的概率：**

```math
P(b = 1) = \beta, \qquad P(b = 0) = 1 - \beta ,
```

（21.2）

例如取 $\beta = 0.001$，意味着**平均三年发生一次**入室盗窃。

**2. 发生地震的概率：**

```math
P(e = 1) = \epsilon, \qquad P(e = 0) = 1 - \epsilon ,
```

（21.3）

例如取 $\epsilon = 0.001$；我们断言地震与窃贼**相互独立**，即先验 $P(b, e) = P(b)P(e)$。这看起来是合理的——除非我们把那种「地震一过就趁乱下手」的机会主义窃贼考虑进来。



## 书内 p294 · noisy-or 真值表 · 第一次后验计算

**3. 警报响的概率** 我们假设：只要下列三件事之一发生，警报就会响：

（a）窃贼进屋，触发了警报（设警报的可靠度为 $\alpha_b = 0.99$，即 99% 的窃贼会触发警报）；

（b）发生地震，触发了警报（设 $\alpha_e = 0.01$，即 1% 的警报由地震触发？）；

（c）其他事件造成误报；设误报率 $f = 0.001$，于是 Fred 家平均三年碰到一次非地震原因的误报。

［$a$ 对 $b$ 与 $e$ 的这种依赖方式，称为 **noisy-or（噪声或）**。］

给定 $b$ 与 $e$ 时 $a$ 的条件概率于是是：

| 条件 | $P(a = 0 \mid b, e)$ | $P(a = 1 \mid b, e)$ |
|---|---|---|
| $b=0,\ e=0$ | $(1-f)$ | $f$ |
| $b=1,\ e=0$ | $(1-f)(1-\alpha_b)$ | $1-(1-f)(1-\alpha_b)$ |
| $b=0,\ e=1$ | $(1-f)(1-\alpha_e)$ | $1-(1-f)(1-\alpha_e)$ |
| $b=1,\ e=1$ | $(1-f)(1-\alpha_b)(1-\alpha_e)$ | $1-(1-f)(1-\alpha_b)(1-\alpha_e)$ |

换成数字就是：

| 条件 | $P(a = 0 \mid b, e)$ | $P(a = 1 \mid b, e)$ |
|---|---|---|
| $b=0,\ e=0$ | 0.999 | 0.001 |
| $b=1,\ e=0$ | 0.009 99 | 0.990 01 |
| $b=0,\ e=1$ | 0.989 01 | 0.010 99 |
| $b=1,\ e=1$ | 0.009 890 1 | 0.990 109 9 |

我们假设：**警报不响时邻居绝不会打电话**，即 $P(p = 1 \mid a = 0) = 0$；同理广播电台也是可信的报道者，$P(r = 1 \mid e = 0) = 0$。要回答上面那两个问题，我们**并不需要**指定 $P(p = 1 \mid a = 1)$ 或 $P(r = 1 \mid e = 1)$，因为观测到 $p = 1$ 与 $r = 1$ 分别给了我们「$a = 1$」与「$e = 1$」的**确定性**。

关于窃贼的那两个问题，可以这样回答：在给定现有信息的条件下，算出**所有** hypotheses 的后验概率。先提醒自己：在观测到 $p$ 或 $r$ 之前，有窃贼的概率是 $P(b = 1) = \beta = 0.001$，发生地震的概率是 $P(e = 1) = \epsilon = 0.001$，而且这两个命题**相互独立**。

首先，当 $p = 1$ 时，我们知道警报在响，即 $a = 1$。$b$ 与 $e$ 的后验概率变成：

```math
P(b, e \mid a = 1) = \frac{P(a = 1 \mid b, e)\,P(b)\,P(e)}{P(a = 1)} .
```

（21.4）

分子的四个可能取值是

| 项 | 计算 | 数值 |
|---|---|---|
| $P(a=1\mid b=0,e=0)\times P(b=0)\times P(e=0)$ | $0.001 \times 0.999 \times 0.999$ | 0.000 998 |
| $P(a=1\mid b=1,e=0)\times P(b=1)\times P(e=0)$ | $0.990\,01 \times 0.001 \times 0.999$ | 0.000 989 |
| $P(a=1\mid b=0,e=1)\times P(b=0)\times P(e=1)$ | $0.010\,99 \times 0.999 \times 0.001$ | 0.000 010 979 |
| $P(a=1\mid b=1,e=1)\times P(b=1)\times P(e=1)$ | $0.990\,109\,9 \times 0.001 \times 0.001$ | $9.9 \times 10^{-7}$ |

归一化常数就是这四数之和，$P(a = 1) = 0.002$；后验概率是

```math
\begin{aligned}
P(b=0, e=0 \mid a=1) &= 0.4993 \\
P(b=1, e=0 \mid a=1) &= 0.4947 \\
P(b=0, e=1 \mid a=1) &= 0.0055 \\
P(b=1, e=1 \mid a=1) &= 0.0005 .
\end{aligned}
```

（21.5）

---



## 书内 p295 · 边缘化 · explaining away · §21.2 起

为了回答「曾有窃贼的概率是多少」这个问题，我们对地震变量 $e$ 做 **marginalize（边缘化）**：

```math
\begin{aligned}
P(b=0 \mid a=1) &= P(b=0, e=0 \mid a=1) + P(b=0, e=1 \mid a=1) = 0.505 ,\\
P(b=1 \mid a=1) &= P(b=1, e=0 \mid a=1) + P(b=1, e=1 \mid a=1) = 0.495 .
\end{aligned}
```

（21.6）

所以「当时有窃贼」的机会**接近 50%**。有一点很重要：$b$ 与 $e$ 这两个变量**先验独立，后验却不再独立**。后验分布 (21.5) 不是 $b$ 与 $e$ 的可分离函数。要说明这一点，最简单的办法是看「得知 $e = 1$ 」会造成什么影响。

当我们得知 $e = 1$ 时，$b$ 的后验概率由下式给出：$P(b \mid e=1, a=1) = P(b, e=1 \mid a=1) / P(e=1 \mid a=1)$，也就是把 (21.5) 的**下面两行**除以它们的和 $P(e = 1 \mid a = 1) = 0.0060$。于是 $b$ 的后验概率是：

```math
\begin{aligned}
P(b = 0 \mid e=1, a=1) &= 0.92 \\
P(b = 1 \mid e=1, a=1) &= 0.08 .
\end{aligned}
```

（21.7）

于是现在「Fred 家有窃贼」的机会只剩 **8%**。这与日常直觉一致：当 Fred 得知发生了地震——那是警报的**另一种解释**——$b = 1$（警报的一个可能原因）的概率就下降了。

### Explaining away（解释消除）

这个现象——某个数据（本例中数据是 $a = 1$）的诸可能原因之一（$b = 1$），在**另一个**原因（$e = 1$）变得更可能时，自身反而变得更不可能，尽管这两个原因在先验上是相互独立的变量——就叫做 **explaining away**。

**Explaining away 是正确的推断的一个本质特征**，也是任何人工智能都应当复现的特征。

如果我们认为邻居和广播电台不可靠或反复无常，以至于我们并不确定警报真的在响、也不确定地震真的发生过，那么计算会更复杂，但 explaining-away 效应依然存在：地震报道 $r$ 的到来，同时让「警报真的在响」更可能、让「当时有窃贼」更不可能。

总结一下：我们通过**枚举** $(b, e)$ 的全部四个 hypotheses、求出它们的后验概率、再做边缘化，解出了关于窃贼的那些推断问题。

<span style="color:#7d3c98;">**Exercise 21.2**</span> [exercise] *After Fred receives the phone-call about the burglar alarm, but before he hears the radio report, what, from his point of view, is the probability that there was a small earthquake today?*

> [exercise 摘要] 只要「警报在响」这一个证据，地震的后验是多少？（答案可由 (21.5) 直接读出：$P(e=1\mid a=1) = 0.0060$，是**先验 0.001 的六倍**——这正是 explaining away 的另一半：`原因` 互为证据。）

### 21.2 Exact inference for continuous hypothesis spaces（连续假设空间上的精确推断）

我们今后会遇到许多 hypothesis spaces（假设空间），它们**天然**被视为连续的。例如 §3.1（书内 p48）里那个未知的衰变长度 $\lambda$ 生活在一维连续空间里；而高斯分布的未知均值与标准差 $\mu, \sigma$ 生活在二维连续空间里。

不过，在任何实际计算机实现中，这样的连续空间都必然会被**离散化**，因此原则上就可以被枚举——比如取一个参数值的网格。在图 3.2 中，我们曾经把「衰变长度的似然作为 $\lambda$ 的函数」画出来，办法是在一系列**细密间隔**的点上对 likelihood 求值。

---



## 书内 p296 · 两参数模型 · 五参数混合模型

### A two-parameter model（一个双参数模型）

我们拿高斯分布作为「二维假设空间」模型的一个例子。一维高斯的参数是均值 $\mu$ 与标准差 $\sigma$：

```math
P(x \mid \mu, \sigma) = \frac{1}{\sqrt{2\pi}\,\sigma} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) \equiv \mathrm{Normal}(x;\, \mu, \sigma^2) .
```

（21.8）

图 21.2 展示了关于一维高斯的均值与标准差的**一百个** hypotheses 的枚举。这些 hypotheses 均匀地排布在一个 $10 \times 10$ 的方格网上，覆盖 $\mu$ 的十个取值与 $\sigma$ 的十个取值。每个 hypothesis 用一幅小图表示：它给 $x$ 安置的概率密度长什么样。

[Figure 21.2：一维高斯的 100 个假设的枚举——横轴 $\mu$、纵轴 $\sigma$ 构成 $10\times10$ 网格，每格画一条该参数下的高斯密度曲线]

**Figure 21.2（图注）** 对整个（离散化后的）假设空间做枚举，对象是一个参数为 $\mu$（横轴）与 $\sigma$（纵轴）的高斯。**十个 $\mu$ × 十个 $\sigma$ 的具体取值、以及每格曲线的峰高，文字层里没有留下，只有图注文字；此处不臆造。**

现在我们来考察：给定数据点 $x_n$（$n = 1, \ldots, N$，假定是从该密度中独立抽取的），如何推断 $\mu$ 与 $\sigma$。

设想我们采到了数据，例如图 21.3 里的**五个**点。我们现在可以为这一百个 subhypotheses（子假设）逐个求出后验概率，办法是对**每个**子假设求 likelihood，即 $P(\{x_n\}_{n=1}^{5} \mid \mu, \sigma)$ 的值。这些 likelihood 值在图 21.4 中用**线的粗细**示意编码。**likelihood 小于最大 likelihood 的 $e^{-8}$ 倍**的子假设，已被删去不画。

[Figure 21.3：五个数据点 $\{x_n\}_{n=1}^{5}$，横轴是数据取值 $x_n$，纵轴无意义]

**图 21.3 的坐标读数**：原书横轴刻度为 $-0.5,\ 0,\ 0.5,\ 1,\ 1.5,\ 2,\ 2.5$；**五个点的具体横坐标文字层未保留（纵轴本身按图注「无意义」），故不臆造。**

换一个更细的网格，同样的信息可以画成 $\mu$ 与 $\sigma$ 的**曲面图或等高线图**（图 21.5）。

### A five-parameter mixture model（一个五参数混合模型）

用肉眼看数据（图 21.3），你大概会同意：它们看起来更像是来自**两个**高斯的 **mixture（混合）**，而不是单一高斯。两个高斯要用两个均值、两个标准差、两个混合系数 $\pi_1$ 与 $\pi_2$ 来定义，满足 $\pi_1 + \pi_2 = 1$、$\pi_i \ge 0$：

```math
P(x \mid \mu_1, \sigma_1, \pi_1, \mu_2, \sigma_2, \pi_2) = \frac{\pi_1}{\sqrt{2\pi}\,\sigma_1}\exp\left(\frac{-(x-\mu_1)^2}{2\sigma_1^2}\right) + \frac{\pi_2}{\sqrt{2\pi}\,\sigma_2}\exp\left(\frac{-(x-\mu_2)^2}{2\sigma_2^2}\right) .
```

我们来枚举这个替代模型的 subhypotheses。参数空间是**五维**的，想在一页纸上表示出来就变得有挑战性了。

---



## 书内 p297 · 图 21.4 与图 21.5

[Figure 21.4：用线的粗细编码 likelihood 的整张假设空间图——$10\times10$ 网格，每个子假设画一条高斯曲线，细到一定程度即视为被数据否决]

**Figure 21.4（图注）** 给定图 21.3 的数据，likelihood 函数用线的粗细表示。**likelihood 小于最大 likelihood 的 $e^{-8}$ 倍的子假设不画**。

[Figure 21.5：同一 likelihood 的曲面图与等高线图，横轴 $\mu$、纵轴 $\sigma$；右侧另有固定 $\sigma$ 切片上的后验]

**Figure 21.5（图注）** 一个高斯分布各参数的 likelihood 函数。左：$\log$ likelihood 关于 $\mu$ 与 $\sigma$ 的**曲面图**；右：同一函数的**等高线图**。该 $N = 5$ 点的数据集有均值 $\bar{x} = 1.0$、以及 $S = \sum (x - \bar{x})^2 = 1.0$。

**图 21.5 的坐标读数（原书轴标注）**：曲面图的横轴 $\mu$ 为 $0$ 到 $2$、纵轴 $\sigma$ 为 $0.2$ 到 $1$，竖轴为 $0$ 到 $0.06$；等高线图的横轴 $\mu$ 为 $0$ 到 $2$、纵轴 $\sigma$ 为 $0.1$ 到 $1$，等高线取 $0.1, 0.2, \ldots, 1$ 若干层。**曲面的真实峰位与脊线走向无法从文字层复原，此处只报轴范围。**

<span style="color:#1e8449;">**[译注]** $\bar{x}$ 与 $S$ 是这个 likelihood 的 sufficient statistics：$N=5$ 的五个自由度被压成两个数，压缩比 $5\to 2$；图 21.5 网格上每格的高度只是 $(\bar{x}, S, \mu, \sigma)$ 的函数（见书内 p300 的 (22.2)–(22.4)）。这话的分量在于它**把推断的输入规模与数据量解耦**：无论采 $5$ 个点还是 $5\times 10^{6}$ 个点，进入后验计算的状态始终是 $2$ 个数。**消失测试**：若 likelihood 依赖三阶矩或逐点残差，$\mu$-$\sigma$ 平面上的后验就不能用一张二维表表达，书内 p298–299 的 $10^K$ 枚举复杂度论证随之失效，只能改成逐点循环，网格法立刻从 $O(10^K)$ 退化为 $O(N\cdot 10^K)$。**落点**：§22.1 (22.2)–(22.4)、本页图 21.5；对照 Casella & Berger §6.2.2 的因子分解定理。顺带一个反例作对照：柯西分布连期望都不存在，因此不存在有限维充分统计量，对它连「两个数概括数据」这第一步都做不到，网格枚举也就无从谈起。</span>

---



## 书内 p298 · 五维枚举 · evidence 与 $10^K$

图 21.6 枚举了 **800 个** subhypotheses，它们在五个参数 $\mu_1, \mu_2, \sigma_1, \sigma_2, \pi_1$ 上取不同值。两个 means 沿**水平方向**各取**五个**值；两个标准差沿**竖直方向**各取**四个**值；而 $\pi_1$ 沿竖直方向取**两个**值。这五个参数结合起来，就是 $5 \times 5 \times 4 \times 4 \times 2 = 800$ 个 hypotheses。

[Figure 21.6：两个高斯混合的整个（离散化）假设空间的枚举——上半部分 $\pi_1,\pi_2 = 0.6,0.4$，下半部分 $0.8,0.2$；$\mu_1,\mu_2$ 横向变化，$\sigma_1,\sigma_2$ 纵向变化]

**Figure 21.6（图注）** 两个高斯之混合的整个（离散化）假设空间的枚举。混合分量的权重在上半部分是 $\pi_1, \pi_2 = 0.6, 0.4$，下半部分是 $0.8, 0.2$。均值 $\mu_1$ 与 $\mu_2$ 沿水平方向变化，标准差 $\sigma_1$ 与 $\sigma_2$ 沿竖直方向变化。

鉴于这五个数据点，我们可以把这五个参数上的推断表示成图 21.7 那样。

[Figure 21.7：同一 800 格假设空间上的 likelihood（线粗细编码），小于最大值的 $e^{-8}$ 倍者不画，因此留下大片空白]

**Figure 21.7（图注）** 推断「两个高斯的混合」。给定图 21.3 的数据，likelihood 用线的粗细表示，假设空间与图 21.6 完全相同。likelihood 小于最大 likelihood 的 $e^{-8}$ 倍的 subhypotheses 不画，于是出现空白区域——那些空白对应的是**已被数据排除**的假设。

如果我们想比较「单高斯模型」与「两高斯混合模型」，可以求出各模型的**后验概率**，办法是对每个模型 $H$ 求 **marginal likelihood（边缘似然）**，也叫 **evidence（证据）**：$P(\{x\} \mid H)$。这个 evidence 由对参数 $\theta$ 积分给出；积分可以通过对被枚举的各个 $\theta$ 取值**求和**来数值实现：

```math
P(\{x\} \mid H) = \sum_{\theta} P(\theta)\, P(\{x\} \mid \theta, H) ,
```

（21.9）

其中 $P(\theta)$ 是参数值网格上的先验分布，这里取为均匀分布。

对「两个高斯的混合」而言，这个积分是一个**五维**积分；要做得足够准，网格就必须比图中所示**细得多**。如果观测数据把 $K$ 个参数中每一个的不确定性都缩小了——比如说——十倍，那么暴力积分至少需要 $10^{K}$ 个格点。



## 书内 p299 · 图 21.7（续）· Exercise 21.3

<span style="color:#555;">（p298 末尾引用的图 21.7，其图注排在书内 p299 页首，故在此补全。）</span>

**Figure 21.7（图注）** 推断两个高斯的混合。给定图 21.3 的数据，likelihood 用线的粗细表示；假设空间与图 21.6 所示完全相同。likelihood 小于最大 likelihood 的 $e^{-8}$ 倍的 subhypotheses 不画，因而留下空白区域——这些空白对应的正是**被数据排除掉**的那些假设。

这种「计算量随模型规模**指数增长**」的现象，就是 complete enumeration（完全枚举）极少成为一种可行的计算策略的原因。

<span style="color:#7d3c98;">**Exercise 21.3**</span> [exercise] *Imagine fitting a mixture of ten Gaussians to data in a twenty-dimensional space. Estimate the computational cost of implementing inferences for this model by enumeration of a grid of parameter values.*

> [exercise 摘要] 把「$10^K$ 格点」这条经验法则算成一个具体数字：二十维、十个高斯，参数总共两千多个，于是枚举的代价是 $10^{2000}$ 量级——这不是「慢」，是物理上不可执行。

<span style="color:#1e8449;">**[译注]** 把 Exercise 21.3 算到底，才看得出 (21.9) 为何被判死刑。二十维高斯每簇有 $20$ 个均值、$210$ 个协方差元素（$20\times 21/2$）、$1$ 个权重，共 $231$ 个参数；十个簇 $2310$ 个，减去 $\sum_k \pi_k = 1$ 的约束约 $2309$ 个自由度。按本节「每参数十格」的规矩，格点数是 $10^{2309}$。即便放宽到球状高斯（每簇只有一个方差），也有 $10\times 22 = 220$ 个参数，$10^{220}$ 依旧荒谬。对比物理上限：宇宙年龄 $4.4\times 10^{17}\,\mathrm{s}$ 乘每秒 $10^{18}$ 次求值，总共 $4.4\times 10^{35}$ 次，差 $2273$ 个数量级。**消失测试**：没有这个数量级判断，「完全枚举不可行」只是口号；有了它，第 22 章之后的梯度上升与 EM 才被证明是**必需的**，而不是更优雅的。**落点**：§21.2 (21.9)、Exercise 21.3；对照 6.006 的 asymptotics 语言。若强行把协方差换成样本协方差、只对均值建网格，参数降到 $200$ 个，$10^{200}$ 依然天文；可见**指数爆炸的罪不在维数，而在「逐格求值」这个算法本身**。</span>

---



## 书内 p300 · 第 22 章 Maximum Likelihood and Clustering（最大似然与聚类）

# 22 Maximum Likelihood and Clustering

与其去枚举所有 hypotheses——其数目可能是指数级的——我们可以**直奔**一个拟合数据拟合得很好的 hypothesis，这样能省下大量时间。这就是 **maximum likelihood method（最大似然方法）** 背后的哲学：它找出使 likelihood $P(\mathrm{Data} \mid \theta, H)$ 最大的那组参数向量 $\theta$ 的取值。

对某些模型而言，最大似然参数可以从数据中**一眼看出**；对更复杂的模型，找最大似然参数可能得靠**迭代算法**。

对任何模型，通常都**用 likelihood 的对数**而不是 likelihood 本身来算更方便，因为 likelihood 是许多数据点概率的连乘，往往变得非常小。**Likelihood 相乘，log likelihood 相加。**

## 22.1 Maximum likelihood for one Gaussian（单个高斯的最大似然）

我们回到高斯来做第一批例子。设有数据 $\{x_n\}_{n=1}^{N}$。log likelihood 是：

```math
\ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma) = -N \ln(\sqrt{2\pi}\,\sigma) - \sum_n \frac{(x_n - \mu)^2}{2\sigma^2} .
```

（22.1）

这个 likelihood 可以用数据的**两个**函数来表达：**样本均值（sample mean）**

```math
\bar{x} \equiv \sum_{n=1}^{N} x_n / N ,
```

（22.2）

以及**平方偏差和**

```math
S \equiv \sum_n (x_n - \bar{x})^2 :
```

（22.3）

```math
\ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma) = -N \ln(\sqrt{2\pi}\,\sigma) - \left[N(\mu - \bar{x})^2 + S\right] / (2\sigma^2) .
```

（22.4）

因为 likelihood 只通过 $\bar{x}$ 与 $S$ 依赖数据，所以这两个量被称为 **sufficient statistics（充分统计量）**。

<span style="color:#b9770e;">**Example 22.1（例）**</span> 把 log likelihood 对 $\mu$ 求导，并证明：若标准差已知为 $\sigma$，则高斯的**最大似然均值** $\hat{\mu}$ 等于样本均值 $\bar{x}$，对任何 $\sigma$ 值都成立。

**解答**

```math
\frac{\partial}{\partial \mu} \ln P = -\frac{N(\mu - \bar{x})}{\sigma^2}
```

（22.5）

```math
= 0 \quad \text{当 } \mu = \bar{x} .
```

（22.6）◊

† **提取伪影说明**：原书在每个 Example / Solution 结尾排一个 `◊`（菱形）作结束符，本题源 PDF 的文字层把它提取成了数字 `2`（见 (22.6) 之后的孤立 `2`）。正文中一律还原为 `◊`。

---
