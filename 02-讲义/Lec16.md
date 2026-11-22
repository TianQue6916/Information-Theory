> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l16 · 行内双语视觉转录版 · 原图见 fig/l16/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l16-p1](fig/l16/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> **Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）**

左侧为课程标志：一张圆形分形网络图——中央有绿色大圆与绿色方形节点相连，向外逐级分支为蓝色小圆/方形节点，圆周边缘缀满红粉色细碎节点。

课程内容板块：
- **Source coding (Data compression)（信源编码，即数据压缩）**
- **Noisy-channel coding（噪声信道编码）**
- **Inference + probabilistic methods（推断与概率方法）**
  - 9–10 Inference（推断）
  - 11 Clustering（聚类）
  - 12 Monte Carlo methods（蒙特卡罗方法）
  - 13 Advanced Monte Carlo methods（高等蒙特卡罗方法）
  - 14 Variational methods（变分方法）
- **Neural networks（神经网络）**
  - 15 Introduction to feedforward neural networks（前馈神经网络导论）
  - 16 Content-addressable memories（内容寻址存储器）
- **State-of-the-art error-correcting codes（最先进的纠错码）**

底部两行网址：`www.inference.phy.cam.ac.uk/itprnn/`、`www.inference.phy.cam.ac.uk/itila/`

### p.2 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）· 本讲高亮版〕

![l16-p2](fig/l16/mgp00002.png)

与 p.1 同一课程总览页，差别在于强调色：列表中「16 Content-addressable memories（内容寻址存储器）」与「State-of-the-art error-correcting codes（最先进的纠错码）」两行以红色标出，点明本讲主题；其余板块与子条目（9–10 Inference（推断）、11 Clustering（聚类）、12 Monte Carlo methods（蒙特卡罗方法）、13 Advanced Monte Carlo methods（高等蒙特卡罗方法）、14 Variational methods（变分方法）、15 Introduction to feedforward neural networks（前馈神经网络导论）等）保持黑色正文；左侧课程标志圆形分形网络图与底部网址 `www.inference.phy.cam.ac.uk/itprnn/`、`www.inference.phy.cam.ac.uk/itila/` 与 p.1 相同。
### p.3 〔Content-addressable memory challenge（内容寻址存储器挑战）〕

![l16-p3](fig/l16/mgp00003.png)

<span style="color:#2471a3;">**[section]**</span> 挑战目标：**Make a dynamical system（构造一个动力系统）**
- 25 dynamical variables, 300 parameters (4-bit precision)（25 个动力学变量、300 个参数，每个参数 4 比特精度）
- that has **attracting fixed points** at desired memories（在期望的记忆处有吸引不动点（attracting fixed points））
- such that noisy versions are automatically cleaned up（使含噪版本被自动"清洗"复原）

页面中部：三对 5×5 二值像素小图案，每对之间有一个红色箭头，从左侧的含噪/残缺版本指向右侧干净的记忆版本（形如"笑脸""垂头""皱眉"三张小脸的含噪版与干净版）；左页边还有一个竖直窄条，叠放着若干 5×5 像素小图案。〔像素图案的逐格取值不逐一刻录〕

- and such that new memories can be added incrementally（且新记忆可以增量式加入）
- AND robust to corruption of **more than half the parameters**（并且当超过一半的参数被破坏时仍保持稳健——"more than half the parameters"为紫色强调）

> <span style="color:#7f8c8d;">旁注：300 = 25×24/2，恰是无自环对称权重对的数目；每对权重 4 比特精度。</span>

### p.4 〔An orthodox approach to content-addressable memory（内容寻址存储器的传统做法）〕

![l16-p4](fig/l16/mgp00004.png)

本页正文区大片空白（留给口头讲解），仅底部两行灰色小字：

> note that this is a **brute-force decoder** for the **error-correcting code** whose codewords are the required memories
> （注意：这是一个针对某纠错码（error-correcting code）的暴力译码器（brute-force decoder），而该码的码字（codeword）恰是我们想要的那些记忆）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页近乎空白，却是整讲的枢纽：传统关联存储器的做法是把所有记忆存成查找表，来一个含噪输入就遍历全部条目、挑汉明距离最近者——这正是 6.006 中暴力最近邻检索（brute-force nearest neighbor）的思路，代价随记忆条数线性增长，每次新增记忆还得改表。MacKay 提醒我们换一个视角："回忆"其实就是译码（decoding）——把每条记忆看成某个纠错码的码字，含噪输入就是信道输出，存储器的任务是在码字集合中找回"本来想取"的那一条。这与哈希表（hash table）的"地址寻址"形成有趣对照：哈希用键算出桶地址、要求键完整无缺，内容寻址却允许键残缺不全。理解了这一点，后面"Hopfield 网络为何有稳定态"的设问，以及它与变分自由能的联系，就都顺理成章了。
### p.5 〔Neural Networks, Part II: Feedback Networks（神经网络·第二部分：反馈网络）〕

![l16-p5](fig/l16/mgp00005.png)

<span style="color:#2471a3;">**[section]**</span> 章节扉页：
- **Neural Networks, Part II:（神经网络，第二部分：）Feedback Networks（反馈网络）**
- **The Hopfield Network（Hopfield 网络）**
- Chapter 42（第 42 章，红色小字）

### p.6 〔The Hopfield network（Hopfield 网络）〕

![l16-p6](fig/l16/mgp00006.png)

右上角红色小字：Chapter 42（第 42 章）；右侧有两张照片：上为 John Hopfield 的肖像，下为一人在海边木头上坐着写字的照片。

**Architecture（架构）**
- Feedback network（反馈网络）
- Symmetric weights（对称权重）：$w_{ij} = w_{ji}$，$w_{ii} = 0$

**Activity rule（活动规则）**
- Continuous Hopfield network（连续 Hopfield 网络）：
```math
a_i = \sum_j w_{ij} x_j + \theta_i,\qquad x_i = \tanh a_i
```
- Binary Hopfield network（二值 Hopfield 网络）：$x_i =$（后接一幅阶梯函数图：横轴为 $a_i$，纵轴上方标 $+1$、下方标 $-1$，在原点处跳变，即按 $a_i$ 的符号取 $+1$ 或 $-1$）

### p.7 〔Content-addressable memory challenge（内容寻址存储器挑战）〕

![l16-p7](fig/l16/mgp00007.png)

本页与 p.3 版式、文字完全相同（MacKay 在进入 Hopfield 网络前重放挑战页）：Make a dynamical system（构造一个动力系统）；25 dynamical variables, 300 parameters (4-bit precision)（25 个动力学变量、300 个参数，4 比特精度）；that has attracting fixed points at desired memories（在期望记忆处有吸引不动点）；such that noisy versions are automatically cleaned up（含噪版本自动复原，"attracting fixed points"为红色强调）；中部三对 5×5 像素图案（红色箭头由含噪版指向干净版）与左页边像素窄条同前；结尾两条：and such that new memories can be added incrementally（新记忆可增量添加）、AND robust to corruption of more than half the parameters（且在过半参数被破坏时仍稳健，紫色强调）。

### p.8 〔Hopfield network and Hebbian learning（Hopfield 网络与 Hebb 学习）〕

![l16-p8](fig/l16/mgp00008.png)

右上角红色小字：Chapter 42（第 42 章）。

**Architecture（架构）**
- Feedback network（反馈网络）；Symmetric weights（对称权重）：$w_{ij} = w_{ji}$，$w_{ii} = 0$

**Activity rule（活动规则）**
- Continuous Hopfield network（连续 Hopfield 网络）：$a_i = \sum_j w_{ij} x_j + \theta_i$，$x_i = \tanh a_i$
- Binary Hopfield network（二值 Hopfield 网络）：$x_i =$ 阶跃函数（横轴 $a_i$，取值 $+1/-1$）

**Learning rule（学习规则）**
- Hebb rule（Hebb 规则）：
```math
w_{ij} = \sum_{n=1}^{N} x_i^{(n)} x_j^{(n)}
```
### p.9 〔Hebbian learning（Hebb 学习）〕

![l16-p9](fig/l16/mgp00009.png)

<span style="color:#2471a3;">**[example]**</span> 现场演示页，左右两栏：
- 左栏标题 **Desired memories（期望记忆）**：三个 5×5 二值像素图案竖排（形如"笑脸""垂头""皱眉"三张小脸）。
- 右栏标题 **Weights（权重）**：一个终端窗口，首行标 `W:`，其下为 25 行×25 列的整数权重矩阵，元素只出现 $1$、$-1$、$3$、$-3$（对角线为空白）——正是 Hebb 规则把三条 $\pm1$ 记忆的外积逐对累加后的结果。〔矩阵 625 个数字不逐一刻录〕

右下角灰色小字：`cd ~/tp/hopfield ; source LONGDEMO`

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Hebb 规则 $w_{ij}=\sum_n x_i^{(n)}x_j^{(n)}$ 用线代语言看就是：把每条记忆 $x^{(n)}\in\{\pm1\}^{I}$ 做外积再累加，$W=\sum_n x^{(n)}(x^{(n)})^{\mathsf T}$。由于 $(x^{(n)})^{\mathsf T}x^{(n)}$ 等于神经元个数 $I$，可得 $Wx^{(n)}\approx x^{(n)}$，即每条记忆近似是 $W$ 的特征向量、特征值约为 $I$——这正是 Strang 线代里"实对称矩阵可正交对角化"的直接应用；多条记忆之间的串扰（crosstalk）则来自不同记忆向量不完全正交的非对角贡献。屏幕上矩阵元素只取 $\pm1,\pm3$ 也有了解释：三条记忆在每一对 $(i,j)$ 上各贡献 $x_i^{(n)}x_j^{(n)}\in\{\pm1\}$，三者求和只能落在 $\{-3,-1,1,3\}$。另外注意这里的 $\pm1$ 编码与 CSAPP 里的补码位运算不同：符号乘法天然实现"同号得正、异号得负"，恰好对应"两神经元同时激活则增强连接"的 Hebb 直觉。

### p.10 〔The Hopfield network（Hopfield 网络）〕

![l16-p10](fig/l16/mgp00010.png)

三个圆点条目：
- Why does Hopfield net have stable states at all?（为什么 Hopfield 网络会有稳定态？）
- What is the capacity of the Hopfield net?（Hopfield 网络的容量是多少？）
- What else can we do with them?（我们还能用它们做什么？）

**Q:（问：）** Where have we seen the Hopfield net before?（我们以前在哪里见过 Hopfield 网络？）

页面中央给出线索：$w_{ij} = w_{ji}$，$w_{ii} = 0$

**Dynamics（动力学）**：
```math
a_i = \sum_j w_{ij} x_j + \theta_i,\qquad x_i = \tanh a_i
```

**Hint:（提示：）**（右侧蓝色小字）：
```math
a_m = \sum_n J_{mn}\bar{x}_n + h_m,\qquad \bar{x}_n = \tanh a_n
```
### p.11 〔Variational methods（变分方法）〕

![l16-p11](fig/l16/mgp00011.png)

右上角红色小字：Page 508（教材第 508 页）。

正文为蓝色引导句串联红色公式（回顾教材第 33 章对自旋系统的变分近似）：
- When we approximated the spin system whose energy function was（当我们近似那个能量函数为
```math
E(\mathbf{x};\mathbf{J}) = -\frac{1}{2}\sum_{m,n} J_{mn} x_m x_n - \sum_n h_n x_n
```
的自旋系统时）
- with a separable distribution（用一个可分离分布（separable distribution））
```math
Q(\mathbf{x};\mathbf{a}) = \frac{1}{Z_Q}\exp\left(\sum_n a_n x_n\right)
```
- and optimized $Q$ so as to minimize the variational free energy（并优化 $Q$ 以最小化变分自由能（variational free energy））
```math
\beta\tilde{F}(\mathbf{a}) = \beta\sum_{\mathbf{x}} Q(\mathbf{x};\mathbf{a})\,E(\mathbf{x};\mathbf{J}) - \sum_{\mathbf{x}} Q(\mathbf{x};\mathbf{a})\ln\frac{1}{Q(\mathbf{x};\mathbf{a})},
```
- we found that the iterative equations（我们发现迭代方程）
```math
a_m = \beta\left(\sum_n J_{mn}\bar{x}_n + h_m\right) \quad\text{and}\quad \bar{x}_n = \tanh(a_n)
```
- were guaranteed to decrease the variational free energy（保证使变分自由能单调下降）
```math
\beta\tilde{F}(\mathbf{a}) = \beta\left(-\frac{1}{2}\sum_{m,n} J_{mn}\bar{x}_m\bar{x}_n - \sum_n h_n\bar{x}_n\right) - \sum_n H_2^{(e)}(q_n).
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 变分自由能并不是新对象：把 $Q$ 归一化后，$\beta\tilde F$ 等于 $\beta$ 乘能量在 $Q$ 下的期望再加 $Q$ 的熵，它可以写成 $\beta F + D_{\mathrm{KL}}(Q\,\|\,P_\beta)$，其中 $P_\beta\propto e^{-\beta E}$ 是真实的玻尔兹曼分布（Boltzmann distribution）。KL 散度（KL divergence）非负可由凸性/Jensen 不等式证明——正是你在 Strang 线代里处理凸函数时的同一套工具——所以 $\tilde F$ 是真实自由能的上界，最小化它就是在做"可信但可算"的近似推断，这也是概率论中"熵就是随机变量的期望"这一视角的延伸。关键结论是：对可分离的 $Q$ 求驻点得到的迭代方程 $a_m=\beta(\sum_n J_{mn}\bar x_n+h_m)$、$\bar x_n=\tanh a_n$，与 Hopfield 网络的连续更新规则逐字相同。于是"为什么 Hopfield 网有稳定态"有了答案：每次更新都单调下降一个有下界的量（变分自由能），如同梯度下降必然收敛到不动点。
### p.12 〔Capacity of Hopfield network（Hopfield 网络的容量）〕

![l16-p12](fig/l16/mgp00012.png)

右上角红色小字：page 512（教材第 512 页）。

图标题：**Overlap between a desired memory and the nearest stable state（期望记忆与最近稳定态之间的重叠度）**

一张双联曲线图：横轴均为 $N/I$（左图 0–0.16，右图放大至 0.09–0.15），纵轴为重叠度 overlap（左图 0–1，右图 0.95–1）。曲线在 $N/I\approx 0.138$ 之前贴近 1，随后在虚线标记处近乎垂直跌落至 0。

青色结论行：**Capacity for random patterns:（随机模式的容量：）** $N_{\mathrm{crit}} = 0.138\,I$

下方黑色小字：0.24 bits per weight.（每个权重 0.24 比特。）

（此处 $N$ 为存储的记忆条数、$I$ 为神经元数目：每 $I$ 个权重只能可靠存约 $0.138I$ 条随机记忆。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这条曲线的读法：横轴 $N/I$ 是"每个神经元存几条记忆"，纵轴 overlap 衡量网络收敛后的状态与目标记忆的接近程度。在 $N/I\lesssim 0.13$ 时 overlap 几乎贴着 1（右图放大后可见其缓慢下降），越过临界点 $N_{\mathrm{crit}}=0.138\,I$ 后骤然崩塌——这是统计物理中 Amit–Gutfreund–Sompolinsky 的经典解析结果，手法是把其余 $N-1$ 条记忆对某神经元输入的贡献当作高斯串扰噪声，再用大数定律估计其方差，本质是概率论里"信号+噪声"的信噪比分析。换算成信息论语言更有味：每个权重只贡献约 0.24 比特的有效记忆容量，远低于 4 比特的物理存储开销，说明 Hebb 学习极不"节省"，换来的却是增量添加与容错的简单性。这与信源编码定理恰成对照：定理保证存在逼近熵极限的最优码，却不保证构造简单；Hopfield 网络则是"构造简单、常数很差"的典型。

### p.13 〔The Hopfield network（Hopfield 网络）〕

![l16-p13](fig/l16/mgp00013.png)

同一组圆点条目重放，前两条黑色，第三条红色强调：
- Why does Hopfield net have stable states at all?（为什么 Hopfield 网络会有稳定态？）
- What is the capacity of the Hopfield net?（Hopfield 网络的容量是多少？）
- What else can we do with them?（我们还能用它们做什么？）——红色，提示接下来讨论其他用途。
### p.14 〔Hopfield networks for optimization（用于优化的 Hopfield 网络）〕

![l16-p14](fig/l16/mgp00014.png)

右上角红色小字：page 517（教材第 517 页）。

标题下方蓝色文字：**"The Travelling Scholar Problem" (Sree Ayer, 1991)（"旅行学者问题"，Sree Ayer，1991）**——用 Hopfield 网络解旅行商（TSP）式的环路优化问题。

- 左栏：8 幅小快照图（各自以 ITER 加数字标注迭代步数，从 0 递增至约 3636），画的是一个闭合轮廓从近乎一条弧线开始逐步变形、越来越复杂，最终形成不规则闭环——展示网络能量随迭代下降、解逐步成形的过程。
- 右栏：一张剑桥街道地图，上面标出 29 个编号地点，并用折线依次相连成一条经过各点的环游路线（"学者"的观光环线）。〔各地名小字标注无法一一辨认〕

### p.15 〔Q: What is this?（问：这是什么？）〕

![l16-p15](fig/l16/mgp00015.png)

<span style="color:#2471a3;">**[section]**</span> **Q:（问：）What is this?（这是什么？）**
```math
P_0(\mathbf{x}) = \frac{1}{Z_0}\,e^{\beta\left[x_1 x_2 x_3 x_5 +\; x_2 x_3 x_4 x_6 +\; x_1 x_3 x_4 x_7\right]}
```
where $\mathbf{x} = (x_1, x_2, x_3, \ldots, x_7)$，$x_n \in \pm 1$（其中 $\mathbf{x}$ 由 7 个取值 $\pm1$ 的变量组成）
and $\beta = $ large（且 $\beta$ 取大值）

**& What is this?（这又是什么？）**
```math
P_1(\mathbf{x}) = \frac{1}{Z_1}\,e^{\beta\left[x_1 x_2 x_3 x_5 + x_2 x_3 x_4 x_6 + x_1 x_3 x_4 x_7\right] + \sum_{n=1}^{N} b_n x_n}
```

### p.16 〔Idea（想法）〕

![l16-p16](fig/l16/mgp00016.png)

页首重写 $P_1$：
```math
P_1(\mathbf{x}) = \frac{1}{Z_1}\,e^{\beta\left[x_1 x_2 x_3 x_5 + x_2 x_3 x_4 x_6 + x_1 x_3 x_4 x_7\right] + \sum_{n=1}^{N} b_n x_n}
```

- **Solve the decoding problem（解决译码问题）**
```math
\max_{\mathbf{x}} P_1(\mathbf{x})
```
  using approximate methods?（用近似方法求解？）
- eg, Approximate $P_1(\mathbf{x})$ by $Q(\mathbf{x})$ using a variational method（例如：用变分方法（variational method）以 $Q(\mathbf{x})$ 近似 $P_1(\mathbf{x})$）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这两个分布值得拆开看：$P_0$ 中每个四次项如 $x_1x_2x_3x_5$ 是一个"四体约束"——只有当四个变量乘积为 $+1$（即含偶数个 $-1$）时能量才低，这与奇偶校验（parity-check）中"某几个比特异和应为 0"的思想同构，只是用 $\pm1$ 乘法代替了模 2 加法——CSAPP 里 XOR 与"符号乘"正有一一对应：$-1$ 扮演 1、$+1$ 扮演 0。$P_1$ 多出的 $\sum_n b_n x_n$ 是逐比特的"软信息"（soft information）：$b_n$ 编码信道观测对 $x_n$ 取值的偏好，即似然（likelihood）的对数比。于是 $\max_{\mathbf x}P_1(\mathbf x)$ 就是最大后验（MAP）译码：既要满足校验约束，又要贴合观测。难点在于变量经由约束相互耦合，精确枚举是指数级的——这正是要用变分方法以可分离 $Q$ 近似后验的动机，也引出下面两篇论文的主角。
### p.17 〔Electronics Letters, March 1995（〈电子学快报〉1995 年 3 月）〕

![l16-p17](fig/l16/mgp00017.png)

论文首页扫描件：
- 红色眉题：Electronics Letters, March 1995（〈电子学快报〉，1995 年 3 月）
- 标题：**Free energy minimisation algorithm for decoding and cryptanalysis（用于译码与密码分析的自由能最小化算法）**
- 作者：D.J.C. MacKay
- 索引词：*Indexing terms: Decoding, Cryptography（索引词：译码，密码学）*
- 摘要：An algorithm is derived for inferring a binary vector **s** given noisy observations of **As** modulo 2, where **A** is a binary matrix. The binary vector is replaced by a vector of probabilities, optimised by free energy minimisation. Experiments on the inference of the state of a linear feedback shift register indicate that this algorithm supersedes the Meier and Staffelbach polynomial algorithm.（摘要大意：给定二元矩阵 $\mathbf{A}$ 之下 $\mathbf{As}\bmod 2$ 的含噪观测，推导出一个推断二元向量 $\mathbf{s}$ 的算法；用概率向量代替二元向量，并以自由能最小化来优化；对线性反馈移位寄存器状态的推断实验表明，该算法胜过 Meier 与 Staffelbach 的多项式算法。）

> <span style="color:#7f8c8d;">旁注：扫描件右缘略被裁切，个别词尾按上下文补全。</span>

### p.18 〔Decoding error-correcting codes（纠错码的译码）〕

![l16-p18](fig/l16/mgp00018.png)

单一设问页：
- For which codes are **approximate message-passing methods** **effective**?（对哪些码，近似消息传递（message-passing）方法是有效的？）——"approximate message-passing methods"为绿色、"effective?"为紫色强调。
### p.19 〔Electronics Letters, August 1996（〈电子学快报〉1996 年 8 月）〕

![l16-p19](fig/l16/mgp00019.png)

论文首页扫描件：
- 红色眉题：Electronics Letters, August 1996（〈电子学快报〉，1996 年 8 月）
- 标题：**Near Shannon limit performance of low density parity check codes（低密度奇偶校验码的接近 Shannon 极限性能）**
- 作者：D.J.C. MacKay and R.M. Neal
- 绿色小注：[Low Density Parity Check Codes: Gallager 1962]（低密度奇偶校验码：Gallager，1962）
- 索引词：*Indexing terms: Probabilistic decoding, Error correction codes（索引词：概率译码，纠错码）*
- 摘要：The authors report the empirical performance of Gallager's low density parity check codes on Gaussian channels. They show that performance substantially better than that of standard convolutional and concatenated codes can be achieved; indeed the performance is almost as close to the Shannon limit as that of turbo codes.（摘要大意：作者报告了 Gallager 低密度奇偶校验码在高斯信道上的实测性能；显著优于标准卷积码与级联码的性能是可以达到的——事实上，其接近 Shannon 极限的程度几乎与 turbo 码相当。）

> <span style="color:#7f8c8d;">旁注：扫描件右缘略被裁切，个别词尾按上下文补全。</span>

### p.20 〔Low Density Parity Check Code（低密度奇偶校验码）〕

![l16-p20](fig/l16/mgp00020.png)

右上角红色小字：Ch 47（第 47 章）。

正文（衬线字体，三行）：
- We demonstrate a large code that encodes $K = 10000$ source bits into $N = 20000$ transmitted bits.（我们演示一个大码：把 $K=10000$ 个源比特编码为 $N=20000$ 个传输比特。）
- Each parity bit depends on about 5000 source bits.（每个校验位（parity bit）依赖约 5000 个源比特。）
- The encoder is derived from a very sparse $10000\times20000$ matrix $\mathbf{H}$ with three 1s per column.（该编码器由一个非常稀疏的 $10000\times20000$ 矩阵 $\mathbf{H}$ 导出，每列恰有 3 个 1。）

右侧插图：标注 **TRANSMITTED:（发送内容：）** 的漫画——一个人举着写有 "REDUNDANT GLASS（冗余玻璃杯）" 的杯子；漫画下方一大块噪声样像素被花括号标注为 **parity bits（校验位）**——幽默地表示发送的大部分内容都是冗余。

页面下方：$\mathbf{H} =$ 一整幅以极浅灰点显示的矩阵图（$10000\times20000$ 的稀疏 0/1 矩阵，稀疏到几乎全白）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页的数字要读出味道：$K=10000$ 个源比特、$N=20000$ 个传输比特，码率 1/2；校验矩阵 $\mathbf H$ 有 10000 行（每行是一个校验方程）、20000 列，每列仅 3 个 1、每行约 6 个 1——"低密度"（low density）指的正是这种稀疏性。稀疏是消息传递（message passing）可行的前提：每个校验节点只连约 6 个变量节点，一次局部迭代只需常数次运算；这好比 6.006 里邻接表之于稠密矩阵——图的规模巨大，但每个点的邻居很少。右上角的 "REDUNDANT GLASS"（冗余玻璃）卡通是 MacKay 式幽默：往玻璃里掺冗余，摔不碎。历史上 Gallager 1962 年就发明了 LDPC 码，但当年算力不足以验证其迭代译码的真实性能，被遗忘约三十年，直到 1990 年代 turbo 码兴起后由 MacKay 与 Neal 复兴——下一篇论文报告的正是它几乎贴近 Shannon 极限的性能。
### p.21 〔Low Density Parity Check Code (f = 7.5%)（低密度奇偶校验码，噪声水平 f = 7.5%）〕

![l16-p21](fig/l16/mgp00021.png)

标题行：**Low Density Parity Check Code (f = 7.5%)（低密度奇偶校验码，f = 7.5%）**

副标题（居中大字）：**Iterative probabilistic decoding（迭代概率译码）**

- 左侧：p.20 那幅 "REDUNDANT GLASS" 漫画的含噪版本——在 $f=7.5\%$ 的比特翻转噪声下，上半部人物轮廓仍勉强可辨，下半部"校验位"区域已成一片雪花噪声。
- 右侧：一张对数坐标性能图：纵轴 Probability of decoder error（译码器错误概率），刻度自下而上为 $10^{-6}$、$10^{-4}$、$0.001$、$0.01$、$0.1$；横轴 Rate（码率），0–1。图中有由方块/加号数据点连成的 LDPC 性能曲线与一条参考曲线，右侧引线标注 low-density parity-check code（低密度奇偶校验码）与 Shannon limit（Shannon 极限）；横轴附近另标 GV（Gilbert–Varshamov 界）与 C（信道容量）两个记号。曲线走势：错误概率随码率增大而上升，LDPC 可译区域明显越过 GV 界、逼近 Shannon 极限。

### p.22 〔International Symposium on Information Theory 1997 / 2002（国际信息论研讨会 1997 / 2002）〕

![l16-p22](fig/l16/mgp00022.png)

页首两段（黑色标题 + 绿色结论）：
- **International Symposium on Information Theory 1997（1997 年国际信息论研讨会 ISIT）**——**One** paper on low-density parity-check codes（关于低密度奇偶校验码仅**一**篇论文，"One"为绿色强调）
- **International Symposium on Information Theory 2002（2002 年 ISIT；左侧有 Lausanne 会议标志）**——**6 sessions on LDPC codes; 10 on sparse-graph codes（6 个 LDPC 码分会场；10 个稀疏图码分会场，绿色文字）**

下半部为 5 列 17 张分会场卡片（青色边框）：各卡上部为蓝色下划线的分会场名、底部红色为组织者姓名（卡内另有若干红色小数字，为论文集页码〔字迹过小，不逐一刻录〕）：
- 第 1 列：Analysis of LDPC Codes I（LDPC 码分析 I）— R. Michael Tanner；Analysis of LDPC Codes II（LDPC 码分析 II）— Evangelos Eleftheriou；Turbo Code Design（Turbo 码设计）— Johannes B. Huber；Analysis of Turbo Codes（Turbo 码分析）— Daniel J. Costello
- 第 2 列：Iterative Decoding I（迭代译码 I）— Tom Richardson；Iterative Decoding II（迭代译码 II）— Kamil Zigangirov；Applications of Iterative Decoding I（迭代译码应用 I）— Tolga Duman；Applications of Iterative Decoding II（迭代译码应用 II）— Steven W. McLaughlin
- 第 3 列：Decoding Techniques I（译码技术 I）— Hans-Andrea Loeliger；Coding and Statistical Physics（编码与统计物理）— David Forney
- 第 4 列：Construction of LDPC Codes I（LDPC 码构造 I）— Frank R. Kschischang；Construction of LDPC Codes II（LDPC 码构造 II）— Marc Fossorier；Soft-in Soft-Out Decoding（软入软出译码）— Joachim Hagenauer；Decoding Algorithms（译码算法）— Andrew Singer
- 第 5 列：Convolutional Codes I（卷积码 I）— Joachim Rosenthal；Convolutional Codes II（卷积码 II）— Ajay Ulokia〔?〕；Decoding Methods for LDPC Codes（LDPC 码的译码方法）— Thomas E Fuja；Construction of LDPC Codes III（LDPC 码构造 III）— Thomas Mittelholzer

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页是学术史的一手快照：1997 年 ISIT（信息论旗舰会议）上关于 LDPC 的论文只有一篇，到 2002 年已有 6 个 LDPC 分会场、10 个稀疏图码分会场——五年间完成了范式转移。卡片上的人名值得认识：Richardson（迭代译码）、Kschischang（因子图/factor graph）、Forney（编码与统计物理分会）、Hagenauer（软入软出）等，他们与 Gallager、MacKay、Neal 共同奠定了今天 5G 中 LDPC 码当道的信道编码版图。给学习者的启示有两层：其一，"好想法≠立即被接受"，Gallager 的想法沉睡了三十年，直到算力与迭代算法文化成熟才爆发；其二，稀疏图码的成功关键，恰是把一个 NP 难的全局译码问题拆成稀疏图上的局部消息传递——与你在 6.006 所学"利用图结构把全局问题化为局部子问题"是同一种智慧。
### p.23 〔（本页无文字：课程标志放大图）〕

![l16-p23](fig/l16/mgp00023.png)

一张无文字的纯图形页：课程标志的放大版——圆形分形网络图：中央偏右一个绿色大圆与一个绿色方形节点相连，向四周辐射出绿色圆/方形节点，再逐级分支为蓝色节点，最外围是红、粉、品红色的小圆碎屑，整体由品红色弧段围成一个不完整的圆环。〔本页为纯手绘图示〕

### p.24 〔Information Theory / Sustainable Energy（信息论 / 可持续能源）〕

![l16-p24](fig/l16/mgp00024.png)

页首两行大字（青绿色）：**Information Theory（信息论）**（左上）、**Sustainable Energy（可持续能源）**（右下）。

下方两本书的封面图：
- 左：David J. C. MacKay《Information Theory, Inference, and Learning Algorithms（信息论、推断与学习算法）》，剑桥出版社，浅绿色封面。
- 右：David JC MacKay《Sustainable Energy – Without the Hot Air（可持续能源——不说空话）》，彩色风车封面。封面上两段推荐语："THIS BOOK IS A TOUR DE FORCE ... AS A WORK OF POPULAR SCIENCE IT IS EXEMPLARY" — THE ECONOMIST（"这本书是杰作……作为科普作品堪称典范"——《经济学人》）；"THIS IS TO ENERGY AND CLIMATE WHAT FREAKONOMICS IS TO ECONOMICS." — CORY DOCTOROW, BOINGBOING.NET（"这本书之于能源与气候，正如《魔鬼经济学》之于经济学"——Cory Doctorow，Boing Boing 网站）。

### p.25 〔Both available free online（两本书均可在线免费获取）〕

![l16-p25](fig/l16/mgp00025.png)

页首黑色大字：Both available **free online**（两本书都可**在线免费**阅读，"free online"为红色强调）。

左侧：《Information Theory, Inference, and Learning Algorithms》封面，下方蓝色网址 `www.inference.phy.cam.ac.uk/itila/`。
右侧：《Sustainable Energy – Without the Hot Air》封面（含与 p.24 相同的两段推荐语），下方蓝色网址 `www.withouthotair.com`。

### p.26 〔Low Density Parity Check Code（低密度奇偶校验码）〕

![l16-p26](fig/l16/mgp00026.png)

标题：**Low Density Parity Check Code（低密度奇偶校验码）**；副标题（居中大字）：**Iterative probabilistic decoding（迭代概率译码）**。

- 左侧：一幅被噪声严重污染的二值图像（发送图像的接收版本，大半已成雪花点，仅上部隐约可辨内容轮廓）。
- 右侧：对数坐标性能图：纵轴 Probability of decoder error（译码器错误概率），刻度 $0.00001$、$0.00010$、$0.00100$、$0.01000$、$0.10000$；横轴 0–0.5，刻度间隔 0.1。图例：BCH/RM（方块数据点，代数码一类）、Gallager（十字数据点，即 LDPC 码）、Shannon（实线曲线）；横轴下方标有 GV（Gilbert–Varshamov 界）、R0（截止码率 $R_0$）、C（信道容量）三个记号。数据点显示：在相同码率下，Gallager（LDPC）的译码错误概率远低于 BCH/RM 代数码。