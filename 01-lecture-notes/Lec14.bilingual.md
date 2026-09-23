> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l14 · 行内双语视觉转录版 · 原图见 fig/l14/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l14-p1](fig/l14/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程总标题：**Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）**。左侧为一张绿色分形树图：圆盘上一个树状网络，中央大圆节点向四周分形展开，越靠外节点越小，边缘点缀红、蓝小图形。右侧课程内容列表：

- Source coding（信源编码，即 Data compression 数据压缩）
- Noisy-channel coding（噪声信道编码）
- Inference + probabilistic methods（推断 + 概率方法）：
  - 9–10 Inference（推断）
  - 11 Clustering（聚类）
  - 12 Monte Carlo methods（蒙特卡洛方法）
  - 13 Advanced Monte Carlo methods（高级蒙特卡洛方法）
  - 14 Variational methods（变分方法）——本讲
- Neural networks（神经网络）
- State-of-the-art error-correcting codes（最先进的纠错码）

页面底部两个网址：www.inference.phy.cam.ac.uk/itprnn/ 与 www.inference.phy.cam.ac.uk/itila/

### p.2 〔Overview（课程总览）〕

![l14-p2](fig/l14/mgp00002.png)

<span style="color:#2471a3;">**[section]**</span> **Overview（课程总览）**：

- Data compression（数据压缩）
- Noisy-channel coding（噪声信道编码）——Chs 1–6, 8–10, 14（第 1–6、8–10、14 章）
- Inference, data modelling（推断与数据建模）——clustering, pattern recognition（聚类、模式识别），Chs 20, 22
- Probability toolbox（概率工具箱）：
  - Monte Carlo methods（蒙特卡洛方法）——Ch 29
  - Variational methods（变分方法）——Ch 33，本讲内容
- Neural networks（神经网络）——Chs 38, 39, (& perhaps 41, 44), 42（第 38、39 章（也许还有 41、44 章）、42 章）
- State-of-the-art error-correcting codes（最先进的纠错码）

右侧为教材封面图：David J. C. MacKay《Information Theory, Inference, and Learning Algorithms》（Cambridge，封面为草地图案）。下方 **Additional reading（补充阅读）**：

- Laplace's method (Ch 27)（Laplace 方法，第 27 章）
- Ising models (Ch 31)（伊辛模型，第 31 章）

### p.3 〔The course / The book（课程与教材）〕

![l14-p3](fig/l14/mgp00003.png)

<span style="color:#2471a3;">**[section]**</span> **The course（课程）**：www.inference.phy.cam.ac.uk/itprnn/

**The book（教材）**：www.inference.phy.cam.ac.uk/itila/

右侧为教材封面图：David J. C. MacKay《Information Theory, Inference, and Learning Algorithms》（Cambridge 出版社，封面为草地图案）。

### p.4 〔Variational methods（变分方法）〕

![l14-p4](fig/l14/mgp00004.png)

<span style="color:#2471a3;">**[definition]**</span> 我们感兴趣的是（Interested in）

```math
P(\mathbf{x}) = \frac{1}{Z}\, P^*(\mathbf{x}) = \frac{1}{Z}\, e^{-E(\mathbf{x})}.
```

$E(\mathbf{x})$ is simple, but not simple enough（$E(\mathbf{x})$ 很简单，但还不够简单——难在归一化常数 $Z$）。

**Idea（思想）**：用一个更简单的分布 $Q(\mathbf{x};\theta)$ 来近似 $P(\mathbf{x})$；调节 $\theta$ 以得到"最佳（best）"近似；然后用 $\sum_{\mathbf{x}} \phi(\mathbf{x})\, Q(\mathbf{x};\theta^*)$ 来近似 $\sum_{\mathbf{x}} \phi(\mathbf{x})\, P(\mathbf{x})$。

How to measure 'best'?（如何度量"最佳"？）Possible ideas（可能的思路）：

```math
D_{\mathrm{KL}}(Q \| P) = \sum_x Q(x) \log \frac{Q(x)}{P(x)}
```

或（or）

```math
D_{\mathrm{KL}}(P \| Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页抛出的问题——用哪个方向的相对熵 / KL 散度来度量"最佳"——是整个变分推断的枢纽。你在 Strang 线代里学过凸集与凸泛函，在概率论里学过 Jensen 不等式：$\log$ 是凹函数，故 $\mathbb{E}[\log u] \le \log \mathbb{E}[u]$；把 $u = P/Q$ 代入，立刻得到 Gibbs 不等式 $D_{\mathrm{KL}} \ge 0$，等号当且仅当两个分布相同。这个论证与比较排序下界 $\Omega(n \log n)$（6.006/CLRS）同源：都是"某个非负量在最均匀处取极值"的论证。但 KL 不是距离——它不对称。选 $D_{\mathrm{KL}}(Q\|P)$（变分方法的标准选择，俗称反向/排他 KL）意味着只拟合 $P$ 的某一个峰，$Q$ 会偏窄；选 $D_{\mathrm{KL}}(P\|Q)$（包容 KL）则强迫 $Q$ 覆盖 $P$ 的全部支撑。下一页的 $\{1/3,1/3,1/3,\epsilon\}$ 例子会把这种不对称性推向极端。

### p.5 〔Distances between probability distributions（概率分布之间的距离）〕

![l14-p5](fig/l14/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span> **Q（问题）**：若 $P(x) = \{1/3,\ 1/3,\ 1/3,\ \epsilon\}$，且（and）$Q(x) = \{1/4,\ 1/4,\ 1/4,\ 1/4\}$，

which is bigger（哪个更大）：

```math
D_{\mathrm{KL}}(Q \| P) = \sum_x Q(x) \log \frac{Q(x)}{P(x)}
```

还是（or）

```math
D_{\mathrm{KL}}(P \| Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}
```

？

右侧图示：黑底上两个四格柱状直方图——上方红色柱表示 $P$（前三格等高、第四格高度几乎为零，即 $\epsilon$），下方绿色柱表示 $Q$（四格完全等高，即均匀分布）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把极限 $\epsilon \to 0^+$ 代进去算一遍，非对称性会吓你一跳。$D_{\mathrm{KL}}(Q\|P)$ 的第四项是 $\tfrac14 \log \tfrac{1/4}{\epsilon}$：$\epsilon$ 趋于 0 时它趋于 $+\infty$——只要 $P$ 在某点严格为零而 $Q$ 在该点非零，这个方向的 KL 就直接爆炸。反过来 $D_{\mathrm{KL}}(P\|Q)$ 的每一项都有限：$\epsilon \to 0$ 时第四项 $\epsilon \log(4\epsilon) \to 0$，前三项各为 $\tfrac13\log\tfrac43$。所以答案是 $D_{\mathrm{KL}}(Q\|P)$ 无界地更大。用概率论的语言：KL 是对数似然比在对应分布下取期望，期望虽是线性算子，但"对数惩罚零概率"这件事是致命的。这也解释了变分方法为何选 $D_{\mathrm{KL}}(Q\|P)$：它虽"排他"，却保证 $Q$ 在 $P=0$ 处也取 0，使后文变分下界的每一项都可计算。你在 CSAPP 里见过同款取舍：把浮点比较换成整数比较，丢掉 NaN 语义，换来可判定性与速度。

### p.6 〔Variational methods（变分方法：目标函数=变分自由能）〕

![l14-p6](fig/l14/mgp00006.png)

<span style="color:#2471a3;">**[definition]**</span> 上半部分重复 p.4 的引入：我们感兴趣的是 $P(\mathbf{x}) = \frac{1}{Z} P^*(\mathbf{x}) = \frac{1}{Z} e^{-E(\mathbf{x})}$；$E(\mathbf{x})$ is simple, but not simple enough（$E(\mathbf{x})$ 简单，但还不够简单）；**Idea（思想）**：用更简单的分布 $Q(\mathbf{x};\theta)$ 近似 $P(\mathbf{x})$，调节 $\theta$ 得"最佳"近似，再用 $\sum_{\mathbf{x}} \phi(\mathbf{x}) Q(\mathbf{x};\theta^*)$ 近似 $\sum_{\mathbf{x}} \phi(\mathbf{x}) P(\mathbf{x})$。

<span style="color:#2471a3;">**[definition]**</span> **Objective function: Variational free energy（目标函数：变分自由能）**

```math
\tilde{F}(\theta) = \sum_{\mathbf{x}} Q(\mathbf{x};\theta)\, E(\mathbf{x}) \;-\; \sum_{\mathbf{x}} Q(\mathbf{x};\theta) \ln \frac{1}{Q(\mathbf{x};\theta)}
```

$\tilde{F}(\theta)$ is lower-bounded by $-\log Z$（$\tilde{F}(\theta)$ 被 $-\log Z$ 下界）：

```math
\tilde{F}(\theta) = D_{\mathrm{KL}}(Q \| P) - \log Z
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页是全讲的核心。变分自由能 $\tilde F = \mathbb{E}_Q[E] - H_Q$：第一项是能量在 $Q$ 下的期望；第二项里 $\ln \frac{1}{Q} = -\ln Q$，所以减去它等于加上 $Q$ 的熵。直接展开可证 $\tilde F(\theta) = D_{\mathrm{KL}}(Q\|P) - \log Z$：由 Gibbs 不等式 $\mathrm{KL}\ge 0$ 立得 $\tilde F \ge -\log Z$，这就是"下界"的来历——机器学习文献称之为 ELBO（证据下界），$-\log Z$ 则是数据的负对数证据。注意两条优化线索完全等价：最小化 KL 等价于最小化 $\tilde F$，因为 $-\log Z$ 是常数。这套"可计算下界"的构造你在概率论里见过原型——用 Jensen 不等式夹逼 $\log \mathbb{E}[X]$；Strang 线代里凸泛函的极小化（如最小二乘）是它的无随机特例。第 11 页会把这一泛函真正落到伊辛模型上逐项算出。

### p.7 〔Examples（示例：两个动画演示）〕

![l14-p7](fig/l14/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> **Examples（示例）**：本页并排放两张演示截图。

- 左图标注 "Inferring mu and sigma（推断 $\mu$ 与 $\sigma$）"：黑底等高线图（其放大序列见 p.8–p.10），横轴 mu 从 0 到 2，纵轴 sigma 从 0.1 到 1，绿、橙两族等高线同心嵌套于中心 $(\mu,\sigma)\approx(1,0.5)$ 附近，另有绿、橙两条水平线自右侧延伸指向中心。
- 右图标注 "Two coupled spins（两个耦合自旋）"（其放大图见 p.12）：两个三维网格曲面（橙黄色网格、碗状），坐标刻度 0、0.5、1，左下角有蓝、红两根竖条与标注 beta = 1.4。

### p.8 〔mu–sigma 平面上的两族等高线（纯图示页）〕

![l14-p8](fig/l14/mgp00008.png)

一张黑底 mu–sigma 等高线图：横轴 mu（0 到 2），纵轴 sigma（0.1 到 1）。绿色等高线族为圆形，位于左上角、紧贴纵轴，中心约在 $(\mu,\sigma) \approx (0.1,\ 1)$；橙色等高线族共四层，呈上宽下窄的圆三角状，中心约在 $(\mu,\sigma) \approx (1,\ 0.55)$，整体明显比绿色族更宽。〔本页为纯手绘图示〕

### p.9 〔mu–sigma 平面上的重合等高线族（纯图示页）〕

![l14-p9](fig/l14/mgp00009.png)

一张黑底 mu–sigma 等高线图（轴同前：mu 0–2，sigma 0.1–1）。绿色与橙色两族等高线此时同心嵌套于同一中心 $(\mu,\sigma) \approx (1,\ 0.5)$：橙色（真实分布）轮廓略呈圆三角状、外层更宽，绿色（近似分布）轮廓为圆形、略窄，两者逐层交错。〔本页为纯手绘图示〕

### p.10 〔收敛轨迹：两条水平箭头（纯图示页）〕

![l14-p10](fig/l14/mgp00010.png)

与 p.9 相同的绿橙同心等高线图，但新增两条水平箭头：绿色与橙色各一条，均从图右侧（mu 约 2 处，sigma 分别约 0.55 与 0.50）水平指向中心，箭头分别嵌入最内层绿、橙等高线——示意从远处初值出发的迭代优化轨迹收敛到中心。〔本页为纯手绘图示〕

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这三页连放的是同一个演示的三个瞬间，读法如下：橙色是真实后验（比如"给定数据反推高斯噪声模型的 $\mu$ 与 $\sigma$"），绿色是可分解（factorized）变分近似 $Q(\mu)\,Q(\sigma)$——p.8 里它卡在一个错误的解上（$\mu$ 贴 0、$\sigma$ 偏大），p.9 里它已收敛到真值附近，p.10 的水平箭头是从右侧初值出发的迭代轨迹。注意绿色轮廓始终比橙色"瘦"：这不是巧合，而是反向 KL 的通病——最小化 $D_{\mathrm{KL}}(Q\|P)$ 的 $Q$ 会系统性低估方差。用 6.006 的话说，变分方法是对"难解的耦合问题"做松弛：把联合分布松弛成边缘乘积，把指数级的精确推断换成可迭代的固定点更新；松弛换来偏差，这与哈希表用均匀随机换确定性保证是同一种工程哲学。这也正是 p.7 左图演示标题 Inferring mu and sigma 的完整语境。

### p.11 〔Variational methods - example（变分方法·实例，教材 Page 508）〕

![l14-p11](fig/l14/mgp00011.png)

<span style="color:#2471a3;">**[example]**</span> **Variational methods - example**（右上角红字：Page 508，即教材第 508 页）。

Approximate the spin system whose energy function is（对能量函数如下的自旋系统做近似）：

```math
E(\mathbf{x};\mathbf{J}) = -\frac{1}{2} \sum_{m,n} J_{mn}\, x_m x_n \;-\; \sum_n h_n\, x_n
```

with a separable distribution（用一个可分离 / 可分解分布）：

```math
Q(\mathbf{x};\mathbf{a}) = \frac{1}{Z_Q} \exp\left( \sum_n a_n x_n \right).
```

We optimize $Q$ so as to minimize the variational free energy（我们优化 $Q$ 以最小化变分自由能）：

```math
\beta \tilde{F}(\mathbf{a}) = \beta \sum_{\mathbf{x}} Q(\mathbf{x};\mathbf{a})\, E(\mathbf{x};\mathbf{J}) \;-\; \sum_{\mathbf{x}} Q(\mathbf{x};\mathbf{a}) \ln \frac{1}{Q(\mathbf{x};\mathbf{a})},
```

```math
= \beta \left( -\frac{1}{2} \sum_{m,n} J_{mn}\, \bar{x}_m \bar{x}_n \;-\; \sum_n h_n\, \bar{x}_n \right) \;-\; \sum_n H_2^{(e)}(q_n).
```

- Minimum (with respect to $\mathbf{a}$) can be found by the iterative equations（关于 $\mathbf{a}$ 的最小值可由下列迭代方程求出）：

```math
a_m = \beta \left( \sum_n J_{mn}\, \bar{x}_n + h_m \right) \quad \text{and} \quad \bar{x}_n = \tanh(a_n)
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是教材第 31 章伊辛模型（Ising models）的变分处理：$x_n \in \{-1,+1\}$ 是自旋，$J_{mn}$ 是耦合强度（正值为铁磁），$h_n$ 是外场，$\beta = 1/(kT)$ 是逆温度（p.12 的演示取 $\beta = 1.4$）。关键一步是可分解近似 $Q(\mathbf{x}) = \prod_n q_n(x_n)$：在乘积分布下各变量独立，故 $\mathbb{E}_Q[x_m x_n] = \bar{x}_m \bar{x}_n$——独立性把耦合期望拆成均值乘积，能量期望只剩 $-\frac12\sum J_{mn}\bar x_m \bar x_n - \sum h_n \bar x_n$；熵项因分布可乘也拆成每个变量的贡献 $\sum_n H_2^{(e)}(q_n)$，其中 $H_2^{(e)}$ 是以 $e$ 为底的二元熵（$q_n$ 是 $x_n = +1$ 的概率）。$\bar x_n = \tanh(a_n)$ 你也不该陌生：若 $q_n(+1) = 1/(1+e^{-2a_n})$，则期望 $= 2q_n - 1 = \tanh(a_n)$，正是 logistic–tanh 恒等式。整个推导把 $N$ 个自旋 $2^N$ 个组态的联合分布问题压成 $N$ 个一维问题——指数爆炸被乘积假设消掉了。

### p.12 〔Two coupled spins（两个耦合自旋的三维演示，beta = 1.4 · 纯图示页）〕

![l14-p12](fig/l14/mgp00012.png)

一张黑底三维演示图，左下角白字标注 beta = 1.4，左侧有蓝、红两根竖条（示意数值高低的标尺）。画面含两个三维线框框体（蓝色边框，两个水平轴刻度均为 0、0.5、1）：左框内是一张橙黄色网格曲面，呈碗状——两端翘起、中部有一浅谷；右框内是同一曲面的另一视角，碗状曲面下方铺有黄白色等高线投影，等高线在谷底附近出现封闭圈。〔本页为纯手绘图示〕

### p.13 〔Have you seen this before?（你以前见过它吗？）〕

![l14-p13](fig/l14/mgp00013.png)

<span style="color:#2471a3;">**[section]**</span> **Have you seen this before?（你以前见过它吗？）**

```math
a_m = \beta \left( \sum_n J_{mn}\, \bar{x}_n + h_m \right) \quad \text{and} \quad \bar{x}_n = \tanh(a_n)
```

or equivalently...（或者等价地……）

```math
\bar{x}_m = \tanh\left( \beta h_m + \beta \sum_n J_{mn}\, \bar{x}_n \right)
```

？

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> MacKay 这个问句的答案是：这就是 Hopfield 网络（第 42 章）与 Boltzmann machine（第 43 章）的单元更新规则。对照来看：Hopfield 网络用 $s_m = \mathrm{sgn}\big(\sum_n w_{mn} s_n\big)$ 做阈值更新；把符号函数"软化"成 $\tanh(\beta\cdot)$，就得到平均场 Boltzmann machine 的确定性更新——$\beta \to \infty$ 时 $\tanh$ 退化回 sgn。从 CSAPP 的视角看，网络状态就是一串 $\pm 1$ 位（双极表示，与二进制位的 0/1 只差一个仿射变换 $x \mapsto 2x-1$），每个神经元做一次"乘加 + 非线性"，与位运算、点积的心智模型同构。更妙的是信息论视角：$\sum_n J_{mn}\bar x_n + h_m$ 是邻居传来的"证据"，$\tanh$ 把对数几率（log-odds）压缩成软化的后验均值——与前面讲过的贝叶斯推断"先验 + 似然 → 后验"完全同构。这条固定点迭代正是平均场消息传递的雏形，后来发展为变分消息传递（VMP）与期望传播（EP）。

### p.14 〔'Mean field theory' is a variational method（"平均场理论"是一种变分方法）〕

![l14-p14](fig/l14/mgp00014.png)

页面顶部以大号字重复上一页的公式：

```math
\bar{x}_m = \tanh\left( \beta h_m + \beta \sum_n J_{mn}\, \bar{x}_n \right)
```

下方绿色大字结论：**'Mean field theory' is a variational method**（"平均场理论"是一种变分方法）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是全讲的落点：统计物理里的平均场理论不是一条孤立技巧，而是"选一个可分解分布族 + 最小化变分自由能"的变分方法实例。回顾整条链：Gibbs 分布 / 玻尔兹曼分布 $P \propto e^{-\beta E}$ 难在归一化（$Z$ 要对 $2^N$ 个组态求和）→ 用乘积分布 $Q$ 近似 → 变分自由能 $\tilde F = \mathbb{E}_Q[E] - \frac{1}{\beta}\,H_Q$ → 固定点方程 $\bar x = \tanh(\beta J \bar x + \beta h)$。与上一讲的 Monte Carlo 方法对比很有味道：MCMC 用随机采样逼近精确答案（无偏但慢、有噪声），平均场用确定性迭代换一个有偏但极快的近似——现代方法常把二者组合（变分初始化 + MCMC 精修）。你以后会在 VAE、扩散模型、图模型的变分消息传递里不断遇到今天这套语言；甚至典型集思想也在此回响：变分方法本质上是把"指数多个典型组态"的描述压缩为"对均值的一个自洽方程"。
