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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页真正在问的不是"该套哪个公式"，而是"用一个什么标准来判定近似的好坏"，而标准一旦选定，整个算法的性格就被决定了：它会在哪里让步、会在哪里过度自信，全部写在这个标准里。
>
> 先看机制。KL divergence（KL 散度）衡量的是一个 distribution（分布）相对另一个 distribution（分布）的"意外程度"，它的定义式里求和号前面挂着的权重，决定了"你按谁的口味来承担失望"。所以同一个记号天然有两个方向：$D_{\mathrm{KL}}(P\|Q)$ 用真实 distribution（分布）$P$ 加权，$D_{\mathrm{KL}}(Q\|P)$ 用近似 distribution（分布）$Q$ 加权。两个方向都满足非负性，但非负性的证明走的是同一条路，只是权重换了位置。取 $u = P(x)/Q(x)$，按 $Q$ 求期望：$\sum_x Q(x)\log\frac{P(x)}{Q(x)} \le \log\sum_x Q(x)\frac{P(x)}{Q(x)} = \log 1 = 0$，这一步用的是 $\log$ 的凹性与 Jensen's inequality（Jensen 不等式）；把它取负号就得到 $D_{\mathrm{KL}}(Q\|P) \ge 0$，等号当且仅当比值 $u$ 在 $Q$ 的 support（支撑集）上是常数，再由两边各自求和为 $1$ 推出两个 distribution（分布）逐点相同。
>
> 这里有个容易被跳过的关键：非负性对两个方向**都**成立，所以"哪个更小"根本不是判断依据，选方向的依据是你要 $Q$ 在哪里取零。若 $P(x)=0$ 而 $Q(x)>0$，则 $D_{\mathrm{KL}}(Q\|P)$ 在这一项上直接发散，于是最小化它的 $Q$ 被迫在 $P$ 为零的地方也为零；反过来 $D_{\mathrm{KL}}(P\|Q)$ 对 $Q(x)=0$ 而 $P(x)>0$ 的位置同样发散，于是那个方向逼着 $Q$ 覆盖 $P$ 的全部 support（支撑集）。一句话：两个方向的差别不是数值大小，而是"谁的零点必须被尊重"。
>
> 手算一个两点例子。取 $P = (0.9,\ 0.1)$、$Q = (0.5,\ 0.5)$。按 $P$ 加权：$D_{\mathrm{KL}}(P\|Q) = 0.9\ln 1.8 + 0.1\ln 0.2 = 0.9\times 0.5878 + 0.1\times(-1.6094) = 0.5290 - 0.1609 = 0.3681$。按 $Q$ 加权：$D_{\mathrm{KL}}(Q\|P) = 0.5\ln(0.5/0.9) + 0.5\ln(0.5/0.1) = 0.5\times(-0.5878) + 0.5\times 1.6094 = -0.2939 + 0.8047 = 0.5108$。换成以 $2$ 为底就是 $0.531$ bit 与 $0.737$ bit（除以 $\ln 2 = 0.6931$）。反方向大出约 $39\%$，而且这个差距随 $P$ 的尖锐程度一起变大——$P$ 越尖，"按 $Q$ 的口味失望"就越严重。
>
> 跨课程连接有三条。第一条接 6.042J 的 equivalence relation（等价关系）：它要求自反、对称、传递三条公理，而 KL divergence（KL 散度）一条都不满足——它不对称，也不满足三角不等式，所以它在数学上属于 divergence（散度）而不是 metric（度量）。这个区分在 CSAPP 里有同款：IEEE 754 浮点里 NaN 与自身比较返回假，破坏了自反性，因此编译器不能把 `x == x` 优化成真；区别在于 NaN 是"不可比较"，KL 是"可算但不对称"。第二条接 CLRS 的比较排序下界 $\Omega(n\log n)$：那个证明靠的是"叶子数不少于 $n!$"的计数，而这里靠的是"凹性把期望压到常数以下"，两者都属于"极值只在最均匀处取到"的论证模板，区别是一个数信息量、一个用凸性。第三条接概率论：KL divergence（KL 散度）就是对数似然比的期望，而期望是线性算子，线性性保证它可逐项拆开计算——这正是后面第 11 页能把整个 variational free energy（变分自由能）拆成 $N$ 项的前提。
>
> 顺带说一句"对称化"的代价。把两个方向各取一半就得到 Jensen–Shannon divergence（JS 散度）：令 $M = (P+Q)/2$，$JSD = \frac12 D(P\|M) + \frac12 D(Q\|M)$，它对称、有界，取值落在 $[0,\ \ln 2]$ 之内。但它不是变分推断想优化的东西：它的定义里 $P$ 与 $Q$ 同时出现在分母上，最小化它对 $Q$ 的要求是"贴近 $P$"和"覆盖 $P$ 的尾巴"两股力量互相拉扯，结果既不是一个可分解的下界，也失去了解析的固定点。换言之，想要一个真正的 metric（度量）是可以做到的，但代价是把"可优化"这个性质赔进去——这就是为什么变分方法守着那个不对称的、看起来别扭的反向形式不放。
>
> 所以 p.4 把两个方向并排摆出来，不是让你挑一个"更正确的"，而是在提醒：你在定义"最佳"时，已经悄悄写进了"错在哪里更不可接受"。下一页的 $\{1/3,1/3,1/3,\epsilon\}$ 会把这个偏好推到极致。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页要你亲手代一次极限。答案不只是"哪个更大"，而是"差到无穷"——而"差到无穷"恰恰是选方向的唯一硬依据：不可比的大小，才逼得你回去看定义。
>
> 把两个方向展开成逐项之和，机制就摊在纸上了。取 $Q = (1/4,1/4,1/4,1/4)$、$P = (1/3,1/3,1/3,\epsilon)$。按 $Q$ 加权时，前三项各是 $\tfrac14\ln\frac{1/4}{1/3} = \tfrac14\ln\tfrac34$，第四项是 $\tfrac14\ln\frac{1/4}{\epsilon}$，于是 $D_{\mathrm{KL}}(Q\|P) = \tfrac34\ln\tfrac34 + \tfrac14\ln\frac{1}{4\epsilon}$。按 $P$ 加权时，前三项各是 $\tfrac13\ln\frac{1/3}{1/4} = \tfrac13\ln\tfrac43$，第四项是 $\epsilon\ln\frac{\epsilon}{1/4} = \epsilon\ln(4\epsilon)$，于是 $D_{\mathrm{KL}}(P\|Q) = \ln\tfrac43 + \epsilon\ln(4\epsilon)$。
>
> 关键只有一条约定：$0\ln 0 = 0$，它的理由是 $\lim_{x\to 0^{+}} x\ln x = 0$。把这条约定用到 $\epsilon \to 0$ 的极限上，两个方向立刻分道扬镳。若 $P$ 在某点严格为零而 $Q$ 在该点为正，则 $D_{\mathrm{KL}}(Q\|P)$ 在这一项上出现 $\tfrac14\ln\frac{1/4}{0} = +\infty$，整个和发散；而在 $D_{\mathrm{KL}}(P\|Q)$ 里这一项是 $0\cdot\ln\frac{0}{1/4}$，按约定等于 $0$，毫发无损。所以"一个炸一个不炸"不是某种抽象的"不对称"，而是一条零乘无穷的约定只在一个方向上生效。这两种惩罚在机器学习文献里有专门的名字：反向形式叫 zero-forcing（零强制），它不许 $Q$ 伸到 $P$ 的零点上去；正向形式叫 zero-avoiding（零回避），它要求 $Q$ 必须覆盖 $P$ 全部非零处，否则同样发散。
>
> 手算一遍量级。取 $\epsilon = 10^{-3}$：$\tfrac14\ln 250 = 0.25\times 5.5215 = 1.3804$，减去 $0.2158$ 得 $D_{\mathrm{KL}}(Q\|P) = 1.1646$；而 $D_{\mathrm{KL}}(P\|Q) = 0.2877 + 10^{-3}\times\ln(4\times 10^{-3}) = 0.2877 - 0.0055 = 0.2822$。取 $\epsilon = 10^{-6}$：$\tfrac14\ln 250000 = 0.25\times 12.4292 = 3.1073$，减 $0.2158$ 得 $2.8915$；另一边是 $0.2877 - 12.4292\times 10^{-6} \approx 0.28767$。规律很清楚：$\epsilon$ 每缩小 $10^{3}$ 倍，反向那支就抬高 $\tfrac14\ln 1000 = 1.7269$，约合 $2.49$ bit，永无上限；正向那支则以线性速度趋近 $\ln\tfrac43 = 0.2877$，约合 $0.415$ bit，稳稳收住。一个是 logarithmic divergence（对数发散），一个是线性趋零，两者的量级不在同一个世界里。
>
> 这件事在代码里会真实咬人。CSAPP 第 2 章讲过 IEEE 754 的规则：$0\times\infty$ 得到的是 NaN 而不是 $0$。所以你若照公式直译写循环，遇到 $q=0$ 的项会先算出 $\ln 0 = -\infty$，再乘一个 $0$ 的权重，得到 NaN，整个求和被污染成 NaN。正确写法是显式判断并跳过：`if (q == 0.0) continue;`。数学上的 $0\ln 0 = 0$ 是靠极限正当化的，浮点没有极限，只有规则——这是"数学约定"与"机器实现"之间的一个典型缝。顺带说，浮点里的极小正数（非规格化数可以小到约 $4.9\times 10^{-324}$）在概率意义下并不是零：只要 $Q$ 那一位是正的，$D_{\mathrm{KL}}(Q\|P)$ 就会给出任意大的惩罚，"很小"和"为零"在这里是性质完全不同的两件事。
>
> 实际实现里还有一层细节。若要算 $D_{\mathrm{KL}}(P\|Q)$ 而 $Q$ 是模型输出，模型可能给出严格为零的概率，softmax 下溢就是这么来的，这时必须加 pseudocount（伪计数）把零抬成小正数；而在 $D_{\mathrm{KL}}(Q\|P)$ 里，$P$ 为零的项本来就该被跳过，加平滑反而是往答案里掺进不该有的偏差。所以这两条公式不仅在数学上不等价，在代码里也需要两套不同的数值防护——"选哪个方向"这个决定会一路传导到你写的那几行循环里。另外提醒单位：上面所有数字都是 nat（自然单位），若换成 bit（比特）要除以 $\ln 2$，MacKay 的讲义通篇用 nat，因为求导时可以少背一个常数因子。
>
> 于是选择就清楚了：变分方法把自己限制在 $D_{\mathrm{KL}}(Q\|P)$ 上，是因为 $Q$ 是我们自己造出来的、参数可控的 distribution（分布），"让它在 $P$ 为零处也为零"是一条可以落实到参数约束上的设计规定；反过来要求 $D_{\mathrm{KL}}(P\|Q)$ 有限，等于要求 $Q$ 覆盖 $P$ 的全部 support（支撑集），而高维情形下那个 support（支撑集）通常根本无法刻画。下一页的 free energy（自由能）下界之所以每一项都可算，根子就在这个方向的选取上。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页的关键动作只有一句话：把"我不知道 $Z$"翻译成"我知道一个下界"。翻译用的全部工具是一条恒等式和一个非负性，没有别的。
>
> 先做恒等变形。第一项 $\sum_{\mathbf{x}} Q\,E$ 就是 energy（能量）在 $Q$ 下的期望，不用动。第二项要拆一下：定义里的 $-\sum_{\mathbf{x}} Q\ln\frac{1}{Q}$，因为 $\ln\frac{1}{Q} = -\ln Q$ 而变成 $+\sum_{\mathbf{x}} Q\ln Q$；而 $-\sum_{\mathbf{x}} Q\ln Q$ 正是 entropy（熵），所以这一项实际是"加上 entropy（熵）"，前半是期望 energy（能量）、后半是负 entropy（熵），两个都要算。于是 $\tilde F = \sum_{\mathbf{x}} Q\,E + \sum_{\mathbf{x}} Q\ln Q$。第二件工具是 Gibbs distribution（吉布斯分布）的定义式取对数：$P = \frac{1}{Z}e^{-E}$ 给出 $\ln P(\mathbf{x}) = -E(\mathbf{x}) - \ln Z$，注意右边那个 $\ln Z$ 与 $\mathbf{x}$ 无关，是个常数。把两个 $\sum_{\mathbf{x}} Q\ln Q$ 与 $\sum_{\mathbf{x}} Q\ln P$ 相减：$\sum_{\mathbf{x}} Q\ln\frac{Q}{P} = D_{\mathrm{KL}}(Q\|P)$；而把 $\ln P$ 展开后代进去，同一件事又等于 $\sum_{\mathbf{x}} Q\ln Q + \sum_{\mathbf{x}} Q\,E + \ln Z\cdot\sum_{\mathbf{x}} Q = \tilde F + \ln Z$，最后一步用了 $\sum_{\mathbf{x}} Q = 1$。两式联立即得 $\tilde F(\theta) = D_{\mathrm{KL}}(Q\|P) - \ln Z$。
>
> 有了这个恒等式，下界就是一行：KL divergence（KL 散度）非负，所以 $\tilde F \ge -\ln Z$；等号当且仅当 $Q$ 与 $P$ 处处相同。这里的 $-\ln Z$ 在统计里叫 negative log evidence（负对数证据），在机器学习文献里 $-\tilde F$ 就是 ELBO（证据下界），两个名字指同一件事，只是符号方向相反——一个说"越小越好"，一个说"越大越好"。
>
> 这个推导值得抽象成模板，因为你会反复用到：**先隔离不可算的常数，再用一个非负量夹逼**。第一步把所有含 $Z$ 的东西收拢成一个与参数无关的加性常数；第二步找一个恒非负的量（这里是 KL divergence（KL 散度），别处可以是势函数、可以是平方误差），把它和执行代价绑在一起；第三步让可算部分去追那个常数。CLRS 里的摊还分析是同一个骨架：真实代价等于摊还代价加上势函数的变化量，而势函数恒非负，于是摊还代价构成真实代价的上界——一个给上界一个给下界，结构完全同构。区别在于摊还分析里势函数是你要设计的，这里 KL divergence（KL 散度）是定义自带非负性的，不需要设计。
>
> 手算一个两状态例子把整个链条走完。取 $\mathbf{x}\in\{0,1\}$，$E(0)=0$、$E(1)=\ln 3$。此时 $Z = e^{0} + e^{-\ln 3} = 1 + \tfrac13 = \tfrac43$，$\ln Z = 0.28768$，所以 $-0.28768$ 就是那条下界线。真实 distribution（分布）是 $P = (3/4,\ 1/4)$。取均匀的 $Q = (1/2,\ 1/2)$：$\tilde F = \tfrac12\ln 3 + \tfrac12\ln\tfrac12 + \tfrac12\ln\tfrac12 = 0.54931 - 0.69315 = -0.14384$，于是 $D_{\mathrm{KL}}(Q\|P) = \tilde F + \ln Z = 0.14384$，与直接代入公式 $\tfrac12\ln\tfrac{2}{3} + \tfrac12\ln 2 = -0.20273 + 0.34657 = 0.14384$ 完全一致。再取 $Q = (3/4,\ 1/4)$ 正好等于 $P$：$\tilde F = 0.27465 - 0.21576 - 0.34657 = -0.28768$，恰好压在 $- \ln Z$ 上，KL 为零。再取一个更偏的 $Q = (1/4,\ 3/4)$：$\tilde F = 0.82396 - 0.34657 - 0.21576 = 0.26162$，比下界高出 $0.54931$。三个点摆在一起就能看出：$\tilde F$ 是一座以真实 distribution（分布）为底的谷，越偏离 $P$ 抬得越高，而谷底的高度就是 $-\ln Z$。
>
> 跨课程连接要点明区别。概率论里用 Jensen's inequality（Jensen 不等式）夹 $\log\mathbb{E}[X]$，得到的是"期望的对数不超过对数的期望"，这里是它的离散版，Cover 的书里把同一件事叫 log sum inequality，两条路都通向 $\tilde F \ge -\ln Z$。最优化里这套做法有名字，叫 minorize–maximize（下界代理最大化）：当目标函数算不动时，构造一个处处不超过它、且在当前点恰好取等号的代理函数，然后反复最大化代理。它与 6.006 里说的"松弛"不是一回事：松弛改的是可行域，把整数约束放宽成实数；minorize–maximize（下界代理最大化）改的是目标函数，可行域一点没动。CSAPP 里也有同款：真实运行时间测不准，就用指令计数当代理指标，代理与真值同序但不同量——只要同序，梯度方向就不会错。
>
> 所以这一页给出的不是一个公式，而是一个可复用的套路：遇到"归一化常数算不出来"，就去构造一个把它隔离在外、再用非负性换来的可算目标。第 11 页的伊辛模型会把这条套路落到 $2^{N}$ 个组态上逐项兑现。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这三页不是三张不同的图，而是同一个 fixed-point iteration（不动点迭代）的三个瞬间：拉远、收敛、画轨迹。而绿色轮廓始终比橙色"瘦"这件事，不是画图误差，是反向 KL divergence（KL 散度）的必然后果，可以在纸上算出来。
>
> 先把机制拆成因果链。第一环：真实后验 $P(\mu,\sigma\mid D)$ 里 $\mu$ 与 $\sigma$ 不独立。$\sigma$ 越小，同样的数据量对 $\mu$ 的约束就越紧，$\mu$ 的不确定度跟着变小；反过来 $\sigma$ 大时数据几乎不提供关于 $\mu$ 的信息。所以 $P$ 在 $(\mu,\sigma)$ 平面上的等高线是斜着的一条"香蕉"，而不是一个正放的椭圆。第二环：变分族 $Q(\mu)Q(\sigma)$ 是乘积形式，它的等高线必然与坐标轴对齐——这是"独立"这个假设在几何上的样子。第三环：用 $D_{\mathrm{KL}}(Q\|P)$ 当目标，而它是 zero-forcing（零强制）的，$Q$ 一旦伸进 $P$ 的低密度区就要付对数代价，于是质量被逼着往 $P$ 的一个高密度区域里挤。第四环：挤的结果是 $Q$ 的 variance（方差）系统性偏小——它只敢描述 $P$ 最确定的那一小块，不敢描述 $P$ 的尾巴。四环连起来，绿色"瘦"就是必然。
>
> 用一个能心算的例子把"偏小多少"量化。设真实后验是一个双峰 mixture（混合分布）：$P = \tfrac12\mathcal{N}(-1,\ 0.01) + \tfrac12\mathcal{N}(+1,\ 0.01)$，两个峰各自很窄（标准差 $0.1$）。它的总 variance（方差）按全方差公式是组内加组间：$0.01 + 1 = 1.01$。现在用单个高斯 $Q = \mathcal{N}(m, s^{2})$ 去近似。若最小化 $D_{\mathrm{KL}}(Q\|P)$，最优解会贴到其中一个峰上：$m \approx 1$、$s \approx 0.1$，variance（方差）约 $0.01$，而它付出的代价只有 $\ln 2 = 0.693$——因为它完全放弃了另一个峰，而"放弃"在零强制方向上是免费的（$Q$ 不在那里取正值，就不被罚）。反过来若最小化 $D_{\mathrm{KL}}(P\|Q)$，$Q$ 必须覆盖两个峰，否则 $P$ 在另一个峰处的质量会撞上 $Q\approx 0$ 而产生 $\ln$ 发散，于是最优解被逼成 $m\approx 0$、$s^{2}\approx 1.01$，variance（方差）与真值同量级，但它在 $x=0$ 附近搭了一座完全没有概率质量的"桥"。这就是机器学习里 mode-seeking（模式寻求）与 mass-covering（质量覆盖）的分野，两者相差约两个数量级。
>
> 跨课程连接。第一条接 6.042J：独立性在集合上对应笛卡尔积，"假设 $\mu$ 与 $\sigma$ 独立"等于把 $Q$ 的 support（支撑集）限制成 $A\times B$ 这种矩形块，而真实的 support（支撑集）是一条斜带，矩形永远是斜带的真子集——所以这个限制一定带来偏差，问题只是偏差落在哪。区别在于等价关系是把集合切块，这里是把函数族切块，切的对象不同。第二条接 CSAPP 第 6 章：cache 的 hit rate（命中率）用 locality（局部性）去近似真实的访存 distribution（分布），换来可算的模型；牺牲精确性换可算性，是同一笔交易。第三条接 6.006：这里的求解器是 coordinate ascent（坐标上升），固定 $\sigma$ 更新 $\mu$、再固定 $\mu$ 更新 $\sigma$，每步有闭式解且目标单调不增；代价是只保证收敛到局部最优，与 Dijkstra 那种"每轮确定一个点且保证全局最优"的性质完全不同——松弛换来的偏差，就体现在这里。
>
> p.8 到 p.10 这三页读下来其实是一句话：$Q$ 从错误的初值出发，沿着坐标轴方向一步步挪，最后停在真值附近，但它停下的那个形状永远比橙色窄一圈。这正是 p.7 左图标题 Inferring mu and sigma 的完整语境——推断的不是两个数，而是两个数背后那个被强行掰直的相关性。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页要完成的事只有一件：把 $N$ 个 spin（自旋）上 $2^{N}$ 个组态的求和，换成 $N$ 个一元方程的 self-consistent（自洽）系统。而完成这件事靠的假设少得可怜，只有一个——独立。
>
> 推导分三步，每一步都要问"这一步为什么必须这样"。第一步拆 energy（能量）的期望。Ising model（伊辛模型）的 energy（能量）是 $E(\mathbf{x};\mathbf{J}) = -\tfrac12\sum_{m,n}J_{mn}x_m x_n - \sum_n h_n x_n$，其中 $x_n\in\{-1,+1\}$ 是 spin（自旋），$J_{mn}$ 是 coupling（耦合）强度，正值表示铁磁倾向，$h_n$ 是 external field（外场）。若 $Q(\mathbf{x}) = \prod_n q_n(x_n)$ 是乘积形式，则不同位置上的随机变量互相独立，于是 $\mathbb{E}_Q[x_m x_n] = \mathbb{E}_Q[x_m]\,\mathbb{E}_Q[x_n] = \bar x_m \bar x_n$。这一步是全篇的支点：它把"两两相关"这个二维对象压成两个一维均值的乘积，代价是把 correlation（相关性）整个丢掉——若真实系统在临界点附近强相关，这个假设就错得最狠。第二步拆 entropy（熵）。因为 $\ln Q(\mathbf{x}) = \sum_n \ln q_n(x_n)$ 是逐项相加，求和号可以分离，$H(Q) = \sum_n H_2^{(e)}(q_n)$，其中 $H_2^{(e)}$ 是以 $e$ 为底的 binary entropy（二元熵），只依赖单个 spin（自旋）取 $+1$ 的概率 $q_n$。第三步对每个 $q_n$ 求导。用 $\bar x_n = 2q_n - 1$ 得 $\partial \bar x_n/\partial q_n = 2$；再用 $\mathbf{J}$ 对称（$J_{mn}=J_{nm}$）得 $\partial E/\partial \bar x_n = -(\sum_m J_{mn}\bar x_m + h_n)$；于是 $\partial(\beta\tilde F)/\partial q_n = -2\beta(\sum_m J_{mn}\bar x_m + h_n) + \ln\frac{q_n}{1-q_n}$。令它为零，解出 $\ln\frac{q_n}{1-q_n} = 2\beta(\sum_m J_{mn}\bar x_m + h_n) = 2a_n$，即 $q_n = \frac{1}{1+e^{-2a_n}}$、$\bar x_n = \tanh(a_n)$，正是讲义里那对迭代方程。
>
> 手算两个 spin（自旋）的情形，把数字代进去。取 $J_{12}=J_{21}=1$、$h_1=h_2=0$、$\beta = 1.4$，方程退化成 $\bar x = \tanh(1.4\bar x)$。$\bar x = 0$ 永远是一个解，对应顺磁相（两个 spin（自旋）平均而言各朝一半）。非零解用迭代找：从 $\bar x = 0.1$ 出发反复代入，收敛到 $0.81453$；从 $\bar x = 0.9$ 出发也收敛到同一个数 $0.81453$——初值不影响结果，说明这是一个吸引的 fixed point（不动点）。回代验证：$\tanh(1.4\times 0.81453) = \tanh(1.14034) = 0.81453$，闭合。物理读法是：每个 spin（自旋）的平均磁化达到 $81.45\%$ 饱和，两个 spin（自旋）明显倾向于同向。再看 $\beta$ 的依赖性：以 $J=1$ 为单位，临界值恰好是 $\beta_c = 1$；$\beta = 1.0$ 时从 $0.9$ 迭代会一路滑到 $0.086$ 并继续掉向零（收敛极慢，因为临界点附近导数正好等于 $1$），只有平凡解；$\beta = 2.0$ 给 $\bar x = 0.9575$，$\beta = 3.0$ 给 $0.9949$，越来越接近完全饱和。$\beta = 1.4$ 落在有序相里，这就是 p.12 那张图取 $1.4$ 的原因。
>
> 跨课程连接。Strang 线代里 $a = \beta(\mathbf{J}\bar{\mathbf{x}} + \mathbf{h})$ 就是一个标准的 matrix–vector product（矩阵向量积），$\mathbf{J}$ 是以 coupling（耦合）为权的 adjacency matrix（邻接矩阵）；6.042J 的图论里同一个 $\mathbf{J}$ 描述一张带权图，只是那边问的是连通分量与最短路径，这边问的是这张图上有没有非零的不动点——问题换了，数据结构没换。CSAPP 第 5 章讲的那个优化对象正是这个形状：矩阵向量积访存连续、可向量化，用 SIMD 与循环展开能接近峰值吞吐，所以这个"每轮 $N^2$ 次乘加"的迭代在现代机器上真的很快。区别在于 CSAPP 只保证这段代码跑得快，不保证这个迭代有解、更不保证解是对的；收敛与正确性要靠上面那条导数条件去论证。
>
> 反过来问一句更值得追问的：如果不做独立假设会怎样？那就必须把二元相关 $\mathbb{E}_Q[x_mx_n]$ 保留成独立参数，参数个数从 $N$ 涨到 $N(N-1)/2$，方程不再逐变量分离，每次更新都要对其它所有变量的联合分布求边缘——计算量直接回到指数级。所以独立假设不是偷懒，它是把问题从不可解拉回可解的那一道门。而所有更精细的方法（结构化变分、区域图、belief propagation）做的事本质相同：在"假设全独立"与"精确求和"之间插一个中间层，只丢掉一部分 correlation（相关性），把图结构里最强的那几条边保留在联合分布里。
>
> 算一笔规模账：$N = 100$ 时精确的 partition function（配分函数）要对 $2^{100}\approx 1.27\times 10^{30}$ 个组态求和，而平均场每轮只需 $100\times 100 = 10^{4}$ 次乘加。指数爆炸不是被更快的机器消掉的，是被"独立"这两个字消掉的——而代价，就是第 4 条注里那个偏瘦的轮廓。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> MacKay 这句 "Have you seen this before?" 是个真问题，答案也确实在书里：同一个方程在三个地方各出现一次——它是 Hopfield network（霍普菲尔德网络）的阈值更新被软化之后的样子，是 logistic regression（逻辑回归）的链接函数，也是贝叶斯后验均值的一次线性化。
>
> 先看"软化"这一步做了什么。Hopfield network（霍普菲尔德网络）的更新是 $s_m = \mathrm{sgn}\big(\sum_n w_{mn}s_n\big)$，输出严格落在 $\{-1,+1\}$ 两个点上，函数图像是阶梯，除了零点处处导数为零。把 $\mathrm{sgn}$ 换成 $\tanh(\beta\cdot)$，输出落进开区间 $(-1,1)$，图像变成一条光滑的 S 形曲线。这两者的关系不是类比而是极限：$\beta\to\infty$ 时 $\tanh(\beta a)\to\mathrm{sgn}(a)$，硬更新是软更新在 zero temperature（零温）下的特例。为什么要花这一步？三个理由都很实。其一，$\tanh$ 处处可导，梯度下降才有东西可算；其二，输出不再是一个判决而是一个均值，于是每次更新都附带"我有多确信"这个信息；其三，$\beta$ 有物理含义，它是 inverse temperature（逆温度），高温对应热噪声大、更新软，低温对应噪声小、更新硬。还有一个必须记住的恒等式：$\tanh(z) = 2\sigma(2z) - 1$，其中 $\sigma$ 是 logistic function（逻辑函数）；所以 $\bar x = \tanh(a)$ 与 $q = \sigma(2a)$ 是同一件事换了个坐标，而 $2a$ 恰好就是 log-odds（对数几率）。
>
> 手算几个点，看"软化"到底改了什么。取 $a = 0.7$：$\sigma(1.4) = \frac{1}{1+e^{-1.4}} = \frac{1}{1+0.2466} = 0.8022$，而 $\tanh(0.7) = 0.6044 = 2\times 0.8022 - 1$，恒等式成立。取 $\beta = 1.4$、邻居贡献之和为 $1$：$\tanh(1.4) = 0.8854$，已经很接近 $1$ 但还差一点。真正的差别集中在阈值附近：$a = 0.02$ 时软更新给出 $0.02$（几乎不动），硬更新直接给出 $+1$（全或无）。而 $\tanh$ 在原点的斜率正好是 $1$，是它梯度最大的地方，也是学习信号最有用武之地的位置。再看饱和：$\tanh(2.5) = 0.98661$、$\tanh(3) = 0.99505$，而导数 $1-\tanh^2$ 在 $a = 2.5$ 处只剩 $0.0264$，只有原点处（斜率恰好为 $1$）的 $2.6\%$。这解释了为什么"软化"在大输入时其实与硬判决几乎重合——差别全部挤在阈值附近那一小段。
>
> 这条迭代能否收敛，可以用第 5 条注里那个不动点来验。$g(x) = \tanh(\beta x)$，则 $g'(x) = \beta(1-\tanh^2(\beta x))$；在不动点 $\bar x^{*} = 0.81453$、$\beta = 1.4$ 处，$g' = 1.4\times(1 - 0.66346) = 0.4711 < 1$。这满足 contraction mapping（压缩映射）的条件，所以局部收敛，而且误差每轮大约缩到 $0.47$ 倍——十轮之后误差降到原来的 $0.4711^{10}\approx 5.4\times 10^{-4}$。反过来 $\beta$ 刚过临界值时 $g'$ 逼近 $1$，收敛会慢到几乎看不出动静，这正是第 5 条注里 $\beta = 1.0$ 那个例子磨磨蹭蹭的原因。
>
> 跨课程连接。CSAPP 第 3 章把这类更新拆成 `imul` 加 `add` 的乘加链，第 5 章再告诉你这个形状正好被 SIMD 与循环展开吃到接近峰值吞吐——两个视角都只管"算得快"，不管"算得对不对"。判定对错要靠压缩映射那个不等式，那属于 6.006 的语言：迭代法的收敛性由迭代函数的导数决定，与图的规模无关。区别在于 6.006 通常讨论的是"多久收敛到机器精度"，这里是"收敛到哪一个不动点"，而后者依赖初值——双稳系统里初值决定你落到有序相还是顺磁相。
>
> 往前看一步：这条"对每个变量单独更新、循环到自洽"的规则，就是变分 message passing（消息传递）的雏形，后来被推广成 VMP 与 EP 两条路线，做法都是把单点更新换成沿因子图的边传递消息。Hopfield 在 1982 年的 PNAS 论文里给出这套动力学，Ackley、Hinton 与 Sejnowski 在 1985 年把它扩展成带随机性的 Boltzmann machine（玻尔兹曼机），而本页的方程正是那台机器在平均场近似下的确定性版本。

### p.14 〔'Mean field theory' is a variational method（"平均场理论"是一种变分方法）〕

![l14-p14](fig/l14/mgp00014.png)

页面顶部以大号字重复上一页的公式：

```math
\bar{x}_m = \tanh\left( \beta h_m + \beta \sum_n J_{mn}\, \bar{x}_n \right)
```

下方绿色大字结论：**'Mean field theory' is a variational method**（"平均场理论"是一种变分方法）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是全讲的落点，它给出一个判据而不是一个技巧：判定"某个方法算不算 variational method（变分方法）"，看的不是它叫什么名字，而是它有没有在优化一个下界。按这个判据，统计物理里的 mean field theory（平均场理论）不是旁门左道，它就是"选一个可分解的 distribution family（分布族）+ 最小化 variational free energy（变分自由能）"这件事的一个实例。
>
> 把整条链摊开，每一步都标上它付的代价。起点是 Boltzmann distribution（玻尔兹曼分布）$P(\mathbf{x}) = \frac{1}{Z}e^{-\beta E(\mathbf{x})}$，它的麻烦全在 partition function（配分函数）$Z = \sum_{\mathbf{x}}e^{-\beta E(\mathbf{x})}$ 上，因为求和要跑遍 $2^{N}$ 个组态。第一步，把 $P$ 换成一个可分解的 $Q$：代价是丢掉 correlation（相关性），换来对 $\mathbf{x}$ 的求和可以逐变量分离。第二步，把"最小化 $D_{\mathrm{KL}}(Q\|P)$"换成"最小化 $\tilde F = \mathbb{E}_Q[E] - \frac{1}{\beta}H_Q$"：这两件事只差一个常数 $-\ln Z$，而那个常数恰好是算不出来的东西，所以从后者入手是等价且更可行的。第三步，对每个 $q_n$ 求偏导得 self-consistent equation（自洽方程）$\bar x = \tanh(\beta\mathbf{J}\bar{\mathbf{x}} + \beta\mathbf{h})$：代价是只能得到局部最优，而且解可能不止一个。终点：你手里握着的是 $-\ln Z$ 的一个下界，不是一个等号。
>
> 算一笔数量级的账，让"快了多少"变成具体数字。取 $N = 100$：精确的 partition function（配分函数）需要对 $2^{100}\approx 1.27\times 10^{30}$ 项求和。假设每项只花 $1$ ns，总时间是 $1.27\times 10^{21}$ s，而一年约 $3.156\times 10^{7}$ s，折合 $4.0\times 10^{13}$ 年；宇宙年龄约 $1.38\times 10^{10}$ 年，也就是要跑约 $2900$ 倍宇宙年龄。平均场这边：全连接时每轮 $\mathbf{J}\bar{\mathbf{x}}$ 是 $100\times 100 = 10^{4}$ 次乘加，迭代 $20$ 轮不过 $2\times 10^{5}$ 次运算，微秒量级。两边的差距在 $25$ 个数量级上下——这不是"优化"能补的，是换了一类数学对象。
>
> 那什么时候平均场会错？答：在 critical point（临界点）附近错得最狠。远离临界点时涨落小，用均值代替涨落还说得过去；接近临界点时涨落与均值同量级，而平均场把涨落整个抹掉了。这个判断是可以被验证的：Onsager 在 1944 年给出了二维 square lattice（方格点阵）在零外场下的精确解，其临界指数与平均场预言的不一致，这是平均场失效最干净的一手证据。
>
> 与上一讲的 Monte Carlo（蒙特卡洛）方法对比，差别在误差的性质而不在速度。MCMC 用随机采样逼近精确答案：无偏，但误差按 $1/\sqrt{M}$ 收缩，$M$ 是样本数，要把误差从 $0.1$ 压到 $0.01$ 得把样本数翻 $100$ 倍，而且结果带噪声、不同随机种子给出不同答案。平均场给出确定性的、可重复的结果，但可能系统性地偏。现代做法常常把两者串起来：先用平均场快速定位初值，再用 MCMC 在那个局部精修——先用有偏但廉价的办法缩小搜索范围，再用无偏但昂贵的办法收尾。这是数值方法里很常见的分工，与 CS144 里 TCP 用平滑的 round-trip time（往返时延）估计代替精确排队模型是同一种思路：把一个算不动的高维对象换成一个可观测的低维统计量。区别在于 TCP 的估计每一轮都有实测样本做反馈校正，而平均场是一次性解方程，解完就没有纠正机制了。
>
> 往前看，这套语言你今天就会在别处再遇到。variational autoencoder（变分自编码器）的训练目标就是把 $\tilde F$ 取负号，即 ELBO（证据下界）；扩散模型的训练目标同样是变分下界的一个具体化。而更根本的一层是：变分方法做的事情，本质上是把"指数多个典型组态"的描述，压缩成"对均值的一个自洽方程"——这与典型集思想里"用一个集合概括绝大多数概率质量"是同一个动作，只不过一个压缩的是状态空间，一个压缩的是分布本身。p.14 那句大字结论之所以是结论，是因为到这一页为止，你已经有了一条完整的、可算的、带误差说明的替代路径，而不只是一个听起来高深的物理名词。
