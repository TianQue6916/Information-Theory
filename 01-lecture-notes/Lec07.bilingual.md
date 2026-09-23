> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l7 · 行内双语视觉转录版 · 原图见 fig/l7/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l7-p1](fig/l7/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 本页为课程总览页。左侧是一幅装饰性图形：圆形盘面内由绿色线条把圆、正方形、三角形节点连成多层树状网络，边缘呈自相似的密铺式结构〔本页左图无文字，为纯装饰性图示〕。右侧打印体课程大纲：

- 第 1 讲 Noisy-channel coding（噪声信道编码）
- **Source coding (Data compression)（信源编码，即数据压缩）**
  - 第 2 讲 Information content, entropy（信息量与熵）
  - 第 3 讲 Typicality and the source coding theorem（典型性与信源编码定理）
  - 第 4 讲 Symbol codes（符号码）
  - 第 5 讲 Symbol codes and Arithmetic coding（符号码与算术编码）
- **Noisy-channel coding（噪声信道编码）**
  - 第 6 讲 Inference and Information measures for noisy channels（推断与噪声信道的信息量度）
  - 第 7 讲 Capacity of a noisy channel（噪声信道的容量）
  - 第 8 讲 The noisy-channel coding theorem（噪声信道编码定理）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页大纲把课程分成两大板块：信源编码（数据压缩）与噪声信道编码（可靠传输），本讲正式进入第二板块。你在 CSAPP 第 2、6 章已经接触过"一切信息都是比特"以及存储与传输中比特可能出错的事实：信源编码回答"最少用多少比特表示信源"，信道编码回答"如何在有噪信道上可靠传比特"，两个方向恰好相反。从概率论视角看，熵就是随机变量自信息函数的期望 $H(X)=\sum_x P(x)\log_2\frac{1}{P(x)}$，本讲要定义的容量同样只是"先取期望、再对输入分布取最大值"。上一讲已备好推断与相关变量的信息量度（条件熵、互信息），本讲把它们用到信道上并引出容量 $C$ 这一核心概念。还请注意第 3 讲的典型性（typicality）会在第 8 讲证明编码定理时回归，它是从大数定律通向编码定理的桥梁。

### p.2 〔Last time（上次课回顾）〕

![l7-p2](fig/l7/mgp00002.png)

打印体标题 Last time（上次课）。两条打印 bullet：

- inference（推断）
- information measures for dependent variables（相关变量的信息量度）

### p.3 〔The rules（游戏规则）〕

![l7-p3](fig/l7/mgp00003.png)

<span style="color:#2471a3;">**[example]**</span> 右上角打印体红字标题 The rules（游戏规则）。左侧手写图示：黑色手写大字 THREE DOORS（三扇门）；一个戴领结的火柴人（主持人）站在三扇拱形门左侧，门上红色编号 1、2、3；一条青色箭头从主持人头顶弯向门 2 方向，箭头末端有一个红色涂改符号〔无法辨认，形如被划掉的记号〕。右侧手写 bullet（洋红色手写，绿色小圆圈作项目符号）：

- Gameshow host hides prize behind one door（综艺节目主持人把奖品藏在其中一扇门后面）

> <span style="color:#7f8c8d;">旁注：箭头末端红色符号疑似被涂改的标记，原意〔无法辨认〕。</span>

### p.4 〔The rules（游戏规则）〕

![l7-p4](fig/l7/mgp00004.png)

图示与上页相同，但门 1 被青色圆圈圈出（表示玩家选中的门）。右侧在原 bullet 之下新增一条手写 bullet：

- Player chooses a door（玩家选择一扇门）
  - eg door 1（例如门 1）〔此行为青色小字〕

### p.5 〔The rules（游戏规则）〕

![l7-p5](fig/l7/mgp00005.png)

图示更新：门 1 仍为青色圈选，门 2 为蓝色，门 3 被主持人（火柴人）拉开、门框改画为绿色（表示已打开）。手写 bullet：

- Host opens another door, promising the prize will not be revealed.（主持人打开另一扇门，并承诺奖品不会被亮出来。）

### p.6 〔The rules（游戏规则）〕

![l7-p6](fig/l7/mgp00006.png)

图示同上页（门 3 已被主持人打开）。在原有 bullet 之下新增一条手写 bullet（其中 stick、switch 两词用红色标出）：

- Player chooses to stick or switch, ie, receive what's behind his original door, or the other closed door.（玩家选择坚持（stick）还是换门（switch），即：拿走自己最初那扇门后的东西，或拿走另一扇仍关着的门后的东西。）

### p.7 〔Q（问题）〕

![l7-p7](fig/l7/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 打印体标题 Q（问题）。两条打印 bullet：

- Player chooses door 1（玩家选择了门 1）
- Host opens door 3, revealing nothing, as promised（主持人如约打开门 3，门后空空如也）

中间手绘图：门 1 被青色圈出，正下方红字手写 STICK?（坚持？）；门 2 正下方红字手写 SWITCH?（换门？）；门 3 为绿色已打开状态。下方投票选项（打印体，选项字母为红色）：

- A should stick（应该坚持）
- B should switch（应该换门）
- C makes no difference（没有区别）
- Z don't know（不知道）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这就是著名的 Monty Hall 三门问题。MacKay 先用 A/B/C/Z 让全班投票，多数人第一反应是 C（没区别），这正是本例的教学点。从 Bertsekas 概率课的角度看，条件概率 $P(\mathcal{H}\mid D)$ 由"观察到的数据 + 生成数据的协议"共同决定：主持人"绝不打开奖品门、也绝不打开你选的门"这一承诺，正是似然取 $1/2$、$1$、$0$ 的来源；若换一个协议（比如主持人随机开门、只是碰巧没开出奖品），结论就会不同。这与 6.006 中分析随机算法前必须先明确随机性来源是同一个道理。接下来三页将用贝叶斯定理把"换门把胜率从 $1/3$ 提到 $2/3$"严格算出来。

### p.8 〔Solving Three Doors by Probability Theory（用概率论求解三门问题）〕

![l7-p8](fig/l7/mgp00008.png)

<span style="color:#2471a3;">**[theorem]**</span> 打印 bullet：Bayes's theorem（贝叶斯定理）。公式上方以绿色小标签标出三个组成部分（POSTERIOR 后验、LIKELIHOOD 似然、PRIOR 先验）：

```math
P(\mathcal{H}\mid \text{Data}) = \frac{P(\text{Data}\mid\mathcal{H})\;P(\mathcal{H})}{P(\text{Data})}
```

（分母 $P(\text{Data})$ 在图上未加彩色标签，即证据（evidence）。）

下方为一张表格（表头绿色打印体：HYPOTHESIS 假设、PRIOR 先验、LIKELIHOOD 似然、POSTERIOR 后验；表体红色手写体）。记 $\mathcal{H}$ 为"奖品在门 $\mathcal{H}$ 后面"这一假设，$D=3$ 为数据"主持人打开了门 3"：

| 假设 $\mathcal{H}$ | 先验 $P(\mathcal{H})$ | 似然 $P(D=3\mid\mathcal{H})$ | 后验 $P(\mathcal{H}\mid D=3)$ |
|:---:|:---:|:---:|:---:|
| $\mathcal{H}=1$ | $\frac{1}{3}$ | $\frac{1}{2}$ | （本页空缺） |
| $\mathcal{H}=2$ | $\frac{1}{3}$ | $1$ | （本页空缺） |
| $\mathcal{H}=3$ | $\frac{1}{3}$ | $0$ | （本页空缺） |

### p.9 〔Solving Three Doors by Probability Theory（用概率论求解三门问题）〕

![l7-p9](fig/l7/mgp00009.png)

版式与 p.8 相同（贝叶斯定理公式与三行表格均未变，后验列仍空缺）。本页在表格下方新增证据（evidence）$P(D=3)$ 的计算（红色手写，最终结果 $\frac{1}{2}$ 为紫色）：

```math
P(D=3) \;=\; \sum_{\mathcal{H}} P(D=3\mid\mathcal{H})\,P(\mathcal{H}) \;=\; \tfrac{1}{3}\times\tfrac{1}{2} + \tfrac{1}{3}\times 1 \;=\; \tfrac{1}{6} + \tfrac{1}{3} \;=\; \tfrac{1}{2}
```

### p.10 〔Solving Three Doors by Probability Theory（用概率论求解三门问题）〕

![l7-p10](fig/l7/mgp00010.png)

版式同前两页；本页表格的后验一列已填入（手写）：

| 假设 $\mathcal{H}$ | 先验 $P(\mathcal{H})$ | 似然 $P(D=3\mid\mathcal{H})$ | 后验 $P(\mathcal{H}\mid D=3)$ |
|:---:|:---:|:---:|:---:|
| $\mathcal{H}=1$ | $\frac{1}{3}$ | $\frac{1}{2}$ | $\frac{1}{3}\times\frac{1}{2}\,\big/\,\frac{1}{2} = \frac{1}{3}$ |
| $\mathcal{H}=2$ | $\frac{1}{3}$ | $1$ | $\frac{1}{3}\times 1\,\big/\,\frac{1}{2} = \frac{2}{3}$ |
| $\mathcal{H}=3$ | $\frac{1}{3}$ | $0$ | $0$ |

表格下方仍保留 p.9 的证据计算 $P(D=3)=\sum_{\mathcal{H}}P(D=3\mid\mathcal{H})P(\mathcal{H})=\frac{1}{2}$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张表是贝叶斯定理的标准流水线：先验 → 似然 → 全概率归一化 → 后验。似然列其实把"主持人协议"编码成了条件分布：奖品在门 1 时，他在 2、3 两扇门中等概率挑一扇打开，故 $P(D{=}3\mid\mathcal{H}{=}1)=\frac{1}{2}$；奖品在门 2 时，他被协议逼着只能开门 3，故为 $1$；奖品在门 3 时，他绝不会打开门 3，似然为 $0$。归一化常数 $P(D=3)=\frac{1}{2}$ 就是全概率公式（Bertsekas 概率论第 1 章的内容），后验 = 先验 × 似然 ÷ 证据。算出的后验 $\frac{1}{3}:\frac{2}{3}:0$ 严格回答了 p.7 的投票：坚持门 1 胜率仅 $\frac{1}{3}$，换到门 2 胜率 $\frac{2}{3}$，应选 B。最常见的直觉错误是把"开了门 3"这一事实对各假设一视同仁；信息量取决于生成数据的协议，这一思想在信道译码（把噪声的实现也当作数据来用）中还会反复出现。

### p.11 〔Information measures（信息量度）〕

![l7-p11](fig/l7/mgp00011.png)

打印体标题 Information measures（信息量度）。本页是一张"盒式文氏图"，无其他正文：

- 最上方的长条框：$H(X,Y)$（联合熵，横贯整行，代表全部不确定性）；
- 其下一层左框：$H(X)$（右端恰好伸到 $I(X;Y)$ 左边界的位置，示意"部分重叠"）；
- 再下一层右框：$H(Y)$（左端同样伸入中部）；
- 最下一行三个并排小框：$H(X\mid Y)$（条件熵）、$I(X;Y)$（互信息，对应上下两框的"重叠带"）、$H(Y\mid X)$（条件熵）。

〔本页为纯框图页：以嵌套框的位置关系表达各信息量度之间的"面积"分解，无其他文字。〕

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张盒式图可以当作信息量度的"文氏图"来读：联合熵 $H(X,Y)$ 是全部面积，$H(X)$、$H(Y)$ 是两个子块，中间小框 $I(X;Y)$ 是二者的"重叠"，两侧条件熵是"独占"部分。熟悉 Strang 线性代数的话，可以类比子空间维数公式 $\dim(U{+}V)=\dim U+\dim V-\dim(U\cap V)$，它正对应 $H(X,Y)=H(X)+H(Y)-I(X;Y)$。同样地，"交不超过任一侧"对应互信息不超过任一边缘熵：$I(X;Y)\le\min\{H(X),H(Y)\}$。这些恒等式都可由 KL 散度（相对熵）非负性证明，而 KL 非负性本身用凸性加 Jensen 不等式即可论证，正是你在概率课与线代课都见过的那套凸函数思路。记住这张图，后面推导容量时所有熵量都能在图上"对号入座"。

### p.12 〔Communication over noisy channels（噪声信道上的通信）〕

![l7-p12](fig/l7/mgp00012.png)

<span style="color:#2471a3;">**[section]**</span> 打印 bullet：Noisy channels（噪声信道），其下两条子 bullet：

- inference（推断）
- information measures（信息量度）

右侧两幅示意图：

1. 二元对称信道（binary symmetric channel, BSC）小图：左端输入 $x\in\{0,1\}$、右端输出 $y\in\{0,1\}$（红色标注）；0→0 与 1→1 的箭头标绿色 $1-f$，0→1 与 1→0 的两条交叉箭头标绿色 $f$。
2. 一幅"打字机"式大图：左列自上而下为字母 A、B、C、D、E、F、G、H，中间省略号，再到 Y、Z 与符号 –，右列同样一组字母与 –；两列之间画满细交叉箭头，表示每个输入都可能混叠到多个输出；其中从 G 发出的三支箭头（指向 F、G、H）被加粗，示意非零转移概率的局部结构。

### p.13 〔Inference for channels（信道上的推断）〕

![l7-p13](fig/l7/mgp00013.png)

打印正文（关键词分别以绿、紫、红、绿等颜色强调）：

- Channel **Q** defines conditional probabilities（信道 Q 定义了一组条件概率）$P(y\mid x)$；
- If we choose an input distribution $P(x)$, we have a joint distribution（若再选定一个输入分布 $P(x)$，就得到一个联合分布）：

```math
P(x,y) = P(x)\,P(y\mid x)
```

- with which we can do inference.（据此我们就可以做推断（inference）。）

右侧仍为 BSC 小图与"打字机"大图（同 p.12）。

### p.14 〔Information measures for noisy channels（噪声信道的信息量度）〕

![l7-p14](fig/l7/mgp00014.png)

正文前三行与 p.13 相同（信道 $\mathbf{Q}$ 定义 $P(y\mid x)$；选定 $P(x)$ 得联合分布 $P(x,y)=P(x)P(y\mid x)$），但结尾改为：

- for which we can compute the **mutual information**（对它我们可以计算互信息）：

```math
I(X;Y) \;=\; H(X) - H(X\mid Y) \;=\; H(Y) - H(Y\mid X)
```

下方再现 p.11 的盒式文氏图（$H(X,Y)$、$H(X)$、$H(Y)$、$H(X\mid Y)$、$I(X;Y)$、$H(Y\mid X)$ 各框按原位排布），右侧仍为 BSC 与"打字机"两幅示意图。

### p.15 〔Mutual information for the BSC（二元对称信道的互信息）〕

![l7-p15](fig/l7/mgp00015.png)

左上：BSC 示意图（输入 $x\in\{0,1\}$、输出 $y\in\{0,1\}$，转移概率 $1-f$ 与 $f$），旁边给出信道矩阵（绿色打印）：

```math
\mathbf{Q} = \begin{bmatrix}\;1-f \quad f\; \\ \;f \quad 1-f\;\end{bmatrix}
```

打印正文：

- Consider $f=0.1$.（取翻转概率 $f=0.1$。）
- Assume input distribution $\mathcal{P}_X=\{p_0,p_1\}=\{0.9,\ 0.1\}$.（设输入分布 $\mathcal{P}_X=\{p_0,p_1\}=\{0.9,0.1\}$。）
- Find（求 $I(X;Y)$）：

```math
\begin{aligned}
I(X;Y) &= H(Y) - H(Y\mid X)\\
&= H_2(0.18) - H_2(0.1)\\
&= 0.68 - 0.47\\
&= 0.21 \text{ bits.}
\end{aligned}
```

（四行依次以红、黑、绿、红色标出。）

右下角：一幅手绘坐标图：纵轴手写标注 $I(x,y)$，轴上标有 $0.21$；横轴手写标注 $p_1$，刻度为 $0.1$、$\frac{1}{2}$、$1$；图上仅在 $(0.1,\ 0.21)$ 处画了一个数据点。图下方打印洋红色文字：Complete the curve（请把整条曲线补全）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页的算术值得逐步复盘：输出分布由全概率公式给出，$P(y{=}1)=p_0 f+p_1(1-f)=0.9\times0.1+0.1\times0.9=0.18$，这正是 $H(Y)=H_2(0.18)$ 的来历。而给定任一输入后，输出只是"翻错概率为 $f$"的一枚硬币，故 $H(Y\mid X)=H_2(0.1)\approx0.469$ 比特。二元熵函数 $H_2(p)=p\log_2\frac{1}{p}+(1-p)\log_2\frac{1}{1-p}$ 在 $p=\frac{1}{2}$ 处取最大值 $1$，是凹函数（用 Jensen 不等式即可证明），这解释了为何 $H_2(0.18)<1$。用 CSAPP 的语言说，BSC 无非是"以概率 $f$ 做一次 XOR 翻转"的噪声源。$I=0.21$ 比特/信道用意味着：若直接逐位硬传，平均每传 1 比特只有 0.21 比特信息可靠抵达；能否做得更好，正是接下来容量概念要回答的问题。

### p.16 〔The Capacity of a channel（信道的容量）〕

![l7-p16](fig/l7/mgp00016.png)

<span style="color:#2471a3;">**[definition]**</span> 本页无标题栏，正文直接给出定义（Capacity 为绿色强调，$P(x)$、$\mathcal{P}^*_X$ 为紫色）：

- The **Capacity** of a channel is the maximum, over all input distributions $P(x)$, of the mutual information:（信道的容量（capacity）是互信息在所有输入分布 $P(x)$ 上取到的最大值：）

```math
C \;\equiv\; \max_{\mathcal{P}_X}\, I(X;Y)
```

- The distribution $\mathcal{P}^*_X$ that achieves the maximum is called the **optimal input distribution**.（达到该最大值的分布 $\mathcal{P}^*_X$ 称为最优输入分布（optimal input distribution）。）

### p.17 〔The Capacity of a channel（信道的容量）〕

![l7-p17](fig/l7/mgp00017.png)

上半页与 p.16 完全相同：容量定义、$C\equiv\max_{\mathcal{P}_X}I(X;Y)$ 与最优输入分布 $\mathcal{P}^*_X$ 的命名。下半页新增打印 bullet：

<span style="color:#2471a3;">**[theorem]**</span>

- Shannon's noisy-channel coding theorem:（Shannon 噪声信道编码定理：）

> **Reliable (virtually error-free) communication is possible at rates up to C**（可靠（几乎无差错）的通信在码率（rate）不超过 $C$ 时是可能的；句末的 C 为红色加粗）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个定理与信源编码定理构成对偶：压缩的极限是熵 $H$，可靠传输的极限是容量 $C$。证明思想（第 8 讲展开）依赖大数定律与渐近均分性（AEP, asymptotic equipartition principle）：码长很大时，噪声的作用集中到少数"典型"模式上，于是可以按典型集（typical set）设计译码规则。随机选码字的想法与 6.006 的均匀散列类似：把消息随机映射到很长的码字上，就像把键均匀散列到桶里，两个码字"撞车"（混叠到同一接收序列的典型邻域）的概率随码长增大指数下降。注意措辞 "virtually error-free"（几乎无错）：错误概率可随分组长度增大而任意逼近零，但码率一旦超过 $C$ 则必定出错（逆定理，后面讲）。这里的码率指每次信道使用平均传送的信息比特数，单位为比特/信道用。

### p.18 〔Ternary confusion channel（三元混淆信道）〕

![l7-p18](fig/l7/mgp00018.png)

<span style="color:#2471a3;">**[example]**</span> 打印标题 Ternary confusion channel（三元混淆信道）。左侧信道图：输入 $x\in\{a,b,c\}$（红色小写字母），输出 $y\in\{M,N\}$（红色大写字母）；箭头旁绿色标注转移概率：$a\to M$ 为 $1$；$b\to M$ 为 $\frac{1}{2}$、$b\to N$ 为 $\frac{1}{2}$；$c\to N$ 为 $1$。右侧信道矩阵（绿色打印）：

```math
\mathbf{Q} = \begin{bmatrix}\;1 \quad 1/2 \quad 0\; \\ \;0 \quad 1/2 \quad 1\;\end{bmatrix}
```

打印文字：Assume input distribution $\mathcal{P}_X=\{\frac{1}{3},\frac{1}{3},\frac{1}{3}\}$.（设输入分布 $\mathcal{P}_X=\{\frac{1}{3},\frac{1}{3},\frac{1}{3}\}$。）

两条打印 bullet：

- If $y=M$, what's $x$?（若收到 $y=M$，$x$ 是什么？）
- What is the mutual information $I(X;Y)$?（互信息 $I(X;Y)$ 是多少？）

> <span style="color:#7f8c8d;">旁注：第二个问题的项目符号处并排画有两个橙色小圆点（疑为课堂标记），含义〔无法辨认〕。</span>

### p.19 〔Noisy typewriter（噪声打字机信道）〕

![l7-p19](fig/l7/mgp00019.png)

<span style="color:#2471a3;">**[example]**</span> 打印标题 Noisy typewriter（噪声打字机信道）。左侧信道图：左列自上而下为 A、B、C、D、E、F、G、H、省略号、Y、Z、–，右列同样一组字母与 –；每个输入字母发出三支箭头指向相邻的输出字母（细线交叉，整体呈"斜向重叠"结构）。右侧以 $x=G$ 为例给出条件分布（上下各有省略号 $\vdots$）：

```math
\begin{aligned}
P(y=\text{F}\mid x=\text{G}) &= 1/3;\\
P(y=\text{G}\mid x=\text{G}) &= 1/3;\\
P(y=\text{H}\mid x=\text{G}) &= 1/3;
\end{aligned}
```

下方两条打印 bullet（阶梯状缩进）：

- What is the optimal input distribution?（最优输入分布是什么？）
- What is the capacity?（容量是多少？）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 打字机信道是"看似有噪、实则无噪"的绝妙例子：每个输入以 $1/3$ 概率落到相邻三个输出之一，单看一个字符确实会混淆。但若只使用相隔 3 位的字母（如 A、D、G、……共 $27/3=9$ 个），各输入的"混淆三角"互不重叠，接收端可唯一反推输入，信道就退化为无噪信道。对这 9 个字母均匀输入得 $I=\log_2 9\approx3.17$ 比特/信道用，这正是该信道的容量（可证均匀分布就是最优输入分布）。用 6.006 的眼光看，这相当于刻意挑选互不冲突的键，让所选输入集合在输出端散列到互不重叠的"桶"里。建议先亲手把 p.18 的三元信道按均匀输入算一遍（提示：$H(Y)=1$ 比特、$H(Y\mid X)=\frac{1}{3}$ 比特，$I=\frac{2}{3}$ 比特），再思考非均匀输入能否更高——答案是能：只使用 $a$、$c$ 这两个无噪输入即可把 $I$ 提到 $1$ 比特。

### p.20 〔Recommended homework（推荐课后作业）〕

![l7-p20](fig/l7/mgp00020.png)

<span style="color:#2471a3;">**[note]**</span> 打印标题 Recommended homework（推荐课后作业）。各条打印 bullet（handout 2 为蓝色链接字，huffman.p、huffman.py 为红色）：

- Reading: Chapters 1-6; Advance reading: Chapters 8, 9, 10（阅读：第 1–6 章；预习：第 8、9、10 章）
- Arithmetic coding: 6.17 (p125) 6.3 (p118) 6.7 (p123)（算术编码：习题 6.17（第 125 页）、6.3（第 118 页）、6.7（第 123 页））
- Data compression recap:（数据压缩复习：）
  - 5.26 (p103)（习题 5.26（第 103 页））
  - Invent a question about data compression.（自己编一道关于数据压缩的题目。）
- See handout 2 on website for more recommended exercises（更多推荐习题见网站上的 handout 2）
  - Huffman programs huffman.p, huffman.py are on website（哈夫曼程序 huffman.p 与 huffman.py 已挂在网站上）
  - also a 'bent coin' file 0010000.... as a compression benchmark（另附一个"偏心硬币"文件 0010000…… 可作压缩基准测试）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "偏心硬币"文件（形如 0010000……的稀疏 1 串）是数据压缩课的经典基准：若 1 出现的频率为 $p$，信源熵只有 $H_2(p)$ 比特/字符，严格小于 1。而二元字母表上的哈夫曼编码每个字符至少要占 1 比特，所以逐比特的符号码压不动这类文件——这正是第 5 章要把字符成块编码、或改用算术编码（arithmetic coding）逼近熵的动机。网站上的 huffman.p 与 huffman.py 可以直接运行，建议把实测压缩长度与理论值 $N\,H_2(p)$ 对照验证。这种"文件即比特流"的观点与 CSAPP 的表示层教学一致：一切压缩算法最终都在比特层面操作。文中习题编号均指教材《Information Theory, Inference, and Learning Algorithms》的题号与页码。
