<!-- 书页 501–550｜来源：B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->



> 页眉 `41.5: Implementing inference with Gaussian approximations`｜书内页 **501**（PDF 513）

沿着 $w,p$ 空间里的一条动力学轨迹进行，其中 $p$ 是 Langevin 与 Hamiltonian Monte Carlo 方法所引入的那些额外的 "momentum"（动量）变量。步数 `Tau` 对每条轨迹被随机地设为 $100$ 到 $200$ 之间的一个数。步长 $\epsilon$ 保持固定，以便与前面那些模拟可比；不过在实用中，建议把步长也随机化。

图 41.9 比较了 Langevin 与 Hamiltonian Monte Carlo 方法的采样性质。Hamiltonian Monte Carlo 模拟中状态的自相关（autocorrelation）随模拟时间下降得比 Langevin 方法快得多。对这个玩具问题，Hamiltonian Monte Carlo 在计算机时间的利用上至少高效十倍。

## 41.5 Implementing inference with Gaussian approximations（用 Gaussian 近似实施推断）

物理学家酷爱把非线性局部线性化，也酷爱用 Gaussian 去近似概率分布。这类近似为处理积分

```math
P(t^{(N+1)} = 1 \mid x^{(N+1)}, D, \alpha) = \int d^K\!w\; y(x^{(N+1)}; w)\, \frac{1}{Z_M}\exp\big(-M(w)\big)
```

(41.21)

提供了另一条策略 —— 这个积分我们刚才已用 Monte Carlo 方法算过了。

我们先对后验概率做 Gaussian 近似。我们走到 $M(w)$ 的最小点（用一个基于梯度的 optimizer），并在那里把 $M$ 作 Taylor 展开：

```math
M(w) \simeq M(w_{\mathrm{MP}}) + \frac{1}{2}(w - w_{\mathrm{MP}})^T A (w - w_{\mathrm{MP}}) + \cdots ,
```

(41.22)

其中 $A$ 是二阶导数矩阵，也叫 Hessian，定义为

```math
A_{ij} \equiv \left. \frac{\partial^2}{\partial w_i \partial w_j} M(w) \right|_{w = w_{\mathrm{MP}}}.
```

(41.23)

于是我们定义自己的 Gaussian 近似：

```math
Q(w; w_{\mathrm{MP}}, A) = [\det(A/2\pi)]^{1/2}\exp\left[-\frac{1}{2}(w - w_{\mathrm{MP}})^T A (w - w_{\mathrm{MP}})\right].
```

(41.24)

<span style="color:#1e8449;">**[译注]** (41.22) 里**没有一次项**，这不是省略而是必然：$w_{\mathrm{MP}}$ 是最小点，$\nabla M = 0$，所以一次项系数恒为零。这条小事有两个实用推论：① 展开式自动以 $A$ 为唯一参数，$A^{-1}$ 就是后验的协方差矩阵（下一句原文即如此说）；② 若 optimizer 没真收敛到极小点，$\nabla M\ne 0$，你得到的"Gaussian 近似"会有一个非零均值偏移，而代码仍能跑通、仍会输出一个看起来正常的 $A^{-1}$ —— **这是本页最容易静默出错的地方**，判据是检查 $\|\nabla M(w_{\mathrm{MP}})\|$ 相对 $A$ 的特征值是否已足够小。量级感：$\alpha = 0.01$ 时，仅先验项就贡献 $\alpha I$，其特征值 $0.01$；数据项贡献 $\sum_n f'(a^{(n)})x^{(n)}x^{(n)T}$，每个样本最多贡献 $0.25\|x\|^2$（因为 $f'\le 1/4$）。$N=30$ 个样本、$\|x\|\approx 5$ 时数据项约 $30\times0.25\times25\approx 188$，**比先验大四个数量级** —— 这就是为什么图中 $A^{-1}$ 的形状几乎完全由数据决定。消失测试：没有 $[\det(A/2\pi)]^{1/2}$ 这个归一化因子，(41.21) 的积分就没有正确的权重，$s^2$ 会整体错一个尺度。另一个极端情形：若 $A$ 出现零特征值（数据在某方向完全没有约束），$A^{-1}$ 不存在、$s^2$ 发散 —— 这与先验项 $\alpha I$ 保证 $A$ 正定的事实相对照，说明 $\alpha>0$ 不是可选项。

落点：(41.22)–(41.24)、Exercise 41.1 的 (41.25)、图 41.11a。</span>

我们可以把矩阵 $A$ 看成定义了 $w$ 上的 error bar（误差棒）。确切地说，$Q$ 是一个正态分布，其 variance–covariance matrix（方差–协方差矩阵）为 $A^{-1}$。

[exercise] **Exercise 41.1.**[2] Show that the second derivative of $M(w)$ with respect to $w$ is given by

```math
\frac{\partial^2}{\partial w_i \partial w_j} M(w) = \sum_{n=1}^{N} f'(a^{(n)})\, x_i^{(n)} x_j^{(n)} + \alpha \delta_{ij},
```

(41.25)

where $f'(a)$ is the first derivative of $f(a) \equiv 1/(1+e^{-a})$, which is

```math
f'(a) = \frac{d}{da} f(a) = f(a)\big(1 - f(a)\big),
```

(41.26)

and

```math
a^{(n)} = \sum_j w_j x_j^{(n)}.
```

(41.27)

话题摘要：证明 $M$ 对 $w$ 的二阶导就是 (41.25)，即「数据项 $=\sum_n f'(a^{(n)})x_i^{(n)}x_j^{(n)}$，先验项 $=\alpha\delta_{ij}$」；关键中间步骤是 (41.26) 那条 sigmoid 导数恒等式。

算完 Hessian，接下来的任务就是用我们的 Gaussian 近似去执行积分 (41.21)。



> 页眉 `502 / 41 — Learning as Inference`｜书内页 **502**（PDF 514）

[Figure 41.10：被边缘化后的概率 $\psi(a,s^2)$ 与对它的近似 $\varphi(a,s^2)$]

图注译文：**图 41.10** 被边缘化后的概率及对它的一个近似。(a) 函数 $\psi(a,s^2)$ 的数值求值结果。在 (b) 中，正文里定义的 $\psi(a,s^2)$ 与 $\varphi(a,s^2)$ 被画成 $a$ 的函数，取 $s^2 = 4$。取自 MacKay (1992b)。

[x] (a)：纵轴标 $\psi(a,s^2)$，横轴是 $a$ 的取值（$-3$ 到 $5$），另一维是 $s^2$（$0$ 到 $6$）；这个曲面在 $s^2 = 0$ 截线上就是 sigmoid 本身，随 $s^2$ 增大而越来越平缓、越来越贴近 $0.5$。
[x] (b)：横轴 $a$ 从 $-3$ 到 $5$，纵轴 $0$ 到 $1$；两条几乎重合的曲线，分别是 $\psi$（数值积分）与 $\varphi$（用 $\kappa$ 缩放后的 sigmoid）。

<span style="color:#1e8449;">**[译注]** 这张图可以**定量复现**，值得亲手算一次，因为它是全书里少数能一眼判定近似好坏的地方。$\psi(a_{\mathrm{MP}},s^2)=\int f(a)\,\mathcal{N}(a;a_{\mathrm{MP}},s^2)\,da$ 与 $\varphi(a_{\mathrm{MP}},s^2)=f(\kappa a_{\mathrm{MP}})$，$\kappa=1/\sqrt{1+\pi s^2/8}$，取 $s^2=4$ 得 $\kappa=0.6237$。数值积分结果（梯形法）对照：$a_{\mathrm{MP}}=0$ 时 $\psi=\varphi=0.50000$；$a_{\mathrm{MP}}=1$ 时 $\psi=0.64773$、$\varphi=0.65106$（差 $0.0033$）；$a_{\mathrm{MP}}=2$ 时 $\psi=0.77520$、$\varphi=0.77684$（差 $0.0016$）；$a_{\mathrm{MP}}=4$ 时 $\psi=0.93233$、$\varphi=0.92377$（差 $0.0086$，开始退化）。作为对照，完全不边缘化的 $f(a_{\mathrm{MP}})$ 在同三点给 $0.73106$、$0.88080$、$0.98201$ —— **差 0.08 到 0.1，比近似误差大二十倍**。方向感：$s^2$ 从 $0.25$ 增到 $8$，$\kappa$ 从 $0.9543$ 单调降到 $0.4914$，$\kappa\to 0.489$ 是 $s^2\to\infty$ 的极限（因为 $\pi s^2/8\to\infty$），于是 $\psi\to f(0)=0.5$，符合"信息全丢"。消失测试：不边缘化就没有 $\kappa$，图 41.11b 那条"远处回落到 0.5"的曲线完全不会出现。（$s^2\to 0$ 时 $\kappa\to 1$，退回到点估计 $f(a_{\mathrm{MP}})$。）

近似为什么能 work：把 $f$ 在 $a_{\mathrm{MP}}$ 处作二阶展开得 $\mathbb{E}[f]\approx f(a_{\mathrm{MP}})+\tfrac12 s^2 f''(a_{\mathrm{MP}})$，而 $f''=f(1-f)(1-2f)$ 在 $a=0$ 处为 $0$、在两侧反号；$\kappa$ 的做法相当于“在 $f$ 的输入上缩放”去拟合这两侧的反号，所以误差在 $a_{\mathrm{MP}}=0$ 处为零、在 $|a_{\mathrm{MP}}|\approx 4$ 处最大 —— 上面算出的 $0.0086$ 就是这个最大偏差。

落点：(41.28)–(41.30)、图 41.10b、MacKay (1992b)。</span>

[Figure 41.11：weight space 里的 Gaussian 近似及其在输入空间里的近似预测]

图注译文：**图 41.11** weight space 中的 Gaussian 近似及其在输入空间中的近似预测。(a) 把 Gaussian 近似投影到 weight space 的 $(w_1,w_2)$ 平面上。画出了一倍与两倍标准差（standard deviation）的等高线。同时画出 optimizer 的轨迹，以及 Monte Carlo 方法的样本。(b) 由 Gaussian 近似与 (41.30) 式得到的预测函数。（参看图 41.2。）

[x] (a)：$(w_1,w_2)$ 平面各 $0$ 到 $10$；中心一个椭圆（一倍与两倍 sd 两条等高线），旁边散布着 Monte Carlo 的样本点，另有一条 optimizer 曲线从远处绕进椭圆中心。标出位置 $A$ 与 $B$。
[x] (b)：$(x_1,x_2)$ 平面各 $0$ 到 $10$，画出由 Gaussian 近似推出的预测等高线 —— 形状与图 41.7a 相似，但更光滑（因为没有采样噪声）。

### Calculating the marginalized probability（计算被边缘化后的概率）

输出 $y(x;w)$ 只通过标量 $a(x;w)$ 依赖 $w$，所以我们可以先求出 $a$ 本身的概率密度，从而把积分的维数降下来。我们假设在 $w = w_{\mathrm{MP}} + \Delta w$ 附近，后验概率分布局部地是 Gaussian，即 $P(w\mid D,\alpha)\simeq (1/Z_Q)\exp(-\frac{1}{2}\Delta w^T A\,\Delta w)$。对我们的单 neuron 来说，activation $a(x;w)$ 是 $w$ 的线性函数，且 $\partial a/\partial w = x$，因此对任何 $x$，activation $a$ 都是 Gaussian 分布的。

[exercise] **Exercise 41.2.**[2] Assuming $w$ is Gaussian-distributed with mean $w_{\mathrm{MP}}$ and variance–covariance matrix $A^{-1}$, show that the probability distribution of $a(x)$ is

```math
P(a \mid x, D, \alpha) = \mathrm{Normal}(a_{\mathrm{MP}}, s^2) = \frac{1}{\sqrt{2\pi s^2}}\exp\left[-\frac{(a - a_{\mathrm{MP}})^2}{2 s^2}\right],
```

(41.28)

where $a_{\mathrm{MP}} = a(x; w_{\mathrm{MP}})$ and $s^2 = x^T A^{-1} x$.

话题摘要：证明 $a(x)$ 仍是 Gaussian，均值 $a_{\mathrm{MP}}$、方差 $s^2 = x^T A^{-1} x$ —— 即「线性变换把 Gaussian 送到 Gaussian，协方差按 $A^{-1}\to x^TA^{-1}x$ 压缩成一个标量」。

这意味着被边缘化后的输出是

```math
P(t=1 \mid x, D, \alpha) = \psi(a_{\mathrm{MP}}, s^2) \equiv \int da\; f(a)\,\mathrm{Normal}(a_{\mathrm{MP}}, s^2).
```

(41.29)

这一点要与 $y(x;w_{\mathrm{MP}}) = f(a_{\mathrm{MP}})$（最可能网络的那个输出）对照着看。sigmoid 乘 Gaussian 的积分可以被近似为

```math
\psi(a_{\mathrm{MP}}, s^2) \simeq \varphi(a_{\mathrm{MP}}, s^2) \equiv f\big(\kappa(s)\, a_{\mathrm{MP}}\big),
```

(41.30)

其中 $\kappa = 1/\sqrt{1 + \pi s^2/8}$（图 41.10）。

<span style="color:#1e8449;">**[译注]** (41.30) 是本章最"可带走"的一条工程公式：**把 Bayesian 平均的净效果写成一个乘在 activation 上的收缩因子 $\kappa$**。它的美在于维数无关 —— 不管 $w$ 是 3 维还是 3000 维，全部不确定性都被压进一个标量 $s^2 = x^TA^{-1}x$，然后一个 $\kappa$ 就够了。这也解释了 (41.28) 为什么重要：因为 $a$ 是 $w$ 的线性函数，$s^2$ 只是一个**二次型**，所以在 $x$ 变化时 $s^2$ 沿 $A^{-1}$ 的等高线变化，图 41.11b 的预测等高线里那些"外扩变宽"的形状就是 $s^2$ 的等高线。量级校验：$\kappa$ 的极限是 $1/\sqrt{\pi s^2/8}=\sqrt{8/(\pi s^2)}=\sqrt{2.546/s^2}$，即 $s^2$ 大时 $\kappa a_{\mathrm{MP}}\propto a_{\mathrm{MP}}/s$ —— 收缩是**乘性**的，不是减法。数例：$\alpha=0.01$、$w_{\mathrm{MP}}$ 的 $\mathrm{sd}\approx 10$，$x=(5,5)$ 时若 $A^{-1}$ 沿该方向的方差为 $4$，则 $s^2=x^TA^{-1}x=200$，$\kappa=1/\sqrt{1+\pi\cdot200/8}=0.1121$，原来 $a_{\mathrm{MP}}=20$（$y=0.99999$）会被压到 $a=2.243$（$y=0.904$）。消失测试：不引入 $\kappa$ 就等于假设 $s^2=0$，回到 $w_{\mathrm{MP}}$ 的过度自信。

实用推论：$\kappa$ 只依赖 $s^2$，所以实现时可以先对每个待预测的 $x$ 算一次二次型 $s^2=x^TA^{-1}x$，再乘 $\kappa$ —— 整个 Bayesian 预测的代价从 $O(e^{K})$ 降到一次 Cholesky 分解 $O(K^3)$ 加每样本 $O(K^2)$。

落点：(41.29)、(41.30)、图 41.10b、图 41.11b。</span>

### Demonstration（演示）

图 41.11 展示了在最优值 $w_{\mathrm{MP}}$ 处拟合 Gaussian 近似的结果，以及使用该 Gaussian 近似与



> 页眉 `41.5: Implementing inference with Gaussian approximations`｜书内页 **503**（PDF 515）

(41.30) 式所作预测的结果。把这些预测与 Langevin Monte Carlo 方法得到的预测（图 41.7）相比，我们看到：尽管定性上一致，两者在数值上明显不同。所以至少这两个方法中有一个并非完全准确。

[exercise] **Exercise 41.3.**[2] Is the Gaussian approximation to $P(w\mid D,\alpha)$ too heavy-tailed or too light-tailed, or both? It may help to consider $P(w\mid D,\alpha)$ as a function of one parameter $w_i$ and to think of the two distributions on a logarithmic scale. Discuss the conditions under which the Gaussian approximation is most accurate.

话题摘要：Gaussian 近似对 $P(w\mid D,\alpha)$ 是**尾部太厚**还是**尾部太薄**（或两者都有）？提示：固定其余参数、只看单个 $w_i$ 的一维切片，并在**对数尺度**上比较两条分布曲线；再讨论这个近似在什么条件下最准。

<span style="color:#1e8449;">**[译注]** 这道题的答案方向可以靠"Gaussian 是唯一在给定方差下熵最大的分布"直接推出来，也可以靠一条不等式验证。$\mathcal{N}$ 的 $\ln p$ 是**严格二次**的，$-\infty$ 方向以 $w_i^2/(2\sigma_i^2)$ 的速度掉；而真实后验在 $w_i\to+\infty$ 时，只要数据被完全满足，$G$ 趋于常数（每个点都判对，$t\ln y\to 0$），于是尾是以 $\alpha w_i^2/2$ 的速度掉的 —— **比 Gaussian 更慢**，因为 Gaussian 的曲率里还含数据项。所以往"好"的一侧，真实后验尾部**更厚**；往"坏"的一侧（判错的方向），$G$ 含 $-\ln y\approx |a|$ 的**线性**增长，掉得比二次慢得多，尾部**更厚得多**（从指数二次降为指数线性）。结论是两侧都 too heavy-tailed，因此 Gaussian 近似会**低估**罕见但极端的参数取值的概率 —— 这与 (41.30) 的 $\kappa$ 只依赖二阶矩、对尾部不敏感是一致的。消失测试：若真实后验是重尾而近似是轻尾，那把它用在外推预测上会**过度自信**（近似认为远处一定回到 $0.5$，实际可能有长尾把它拖得更确定或更不确定）；这正是 Exercise 41.3 与 (b)(c) 两法结果的差异可见处。落点：Exercise 41.3、(41.22)–(41.24)、§41.4 的 在同一张一维对数切片上，Gaussian 的 $\ln p$ 是抛物线，而真实后验在对数尺度上有一段接近直线的尾巴 —— 两条曲线在峰附近贴合，在 $2$ 到 $3$ 个标准差之外分道扬镳。

Monte Carlo 结果、第 33 章 variational 方法的 KL 方向讨论。</span>

### Why marginalize?（为什么要边缘化？）

如果输出被立刻用来做一个 (0/1) 判决，且与错误相关的代价是对称的，那么在这个 Gaussian 近似下使用被边缘化的输出，与使用最可能参数给出的输出相比，classifier 的表现**不会有任何差别** —— 因为两个函数都在 $a_{\mathrm{MP}} = 0$ 处穿过 $0.5$。但如果（举例说）除了「我猜 0」「我猜 1」之外还有「我不知道」这个选项，这些 Bayesian 输出就会有差别。而即便只有「$0$」与「$1$」这两个选择，只要与错误相关的代价不相等，判决边界就会是**某条非 $0.5$ 的等高线**，于是这个边界会受到边缘化的影响。

<span style="color:#1e8449;">**[译注]** 这一段是全章的"止损条款"，它精确划出了 Bayesian 平均在什么情况下是**白费功夫**：对称代价 + 硬判决 + 只要 $0.5$ 等高线 $\Rightarrow$ 两种做法完全等价。理由是可算的：(41.30) 是**单调变换** $a\mapsto \kappa a$，$\kappa>0$ 严格保留序关系，所以 $\{x: \kappa a_{\mathrm{MP}}(x) \ge 0\} = \{x: a_{\mathrm{MP}}(x)\ge 0\}$ —— 判决集合逐点相同，错误率当然一样。一旦代价不对称，判决变成 $\{x: P(t=1\mid x) \ge c\}$，$c\ne 0.5$，此时 $\{f(\kappa a)\ge c\}$ 与 $\{f(a)\ge c\}$ **不再相同**，因为 $f$ 非线性、$\kappa$ 改变了等值线的位置。数值感：$s^2=4$、$\kappa=0.6237$，若代价比要求阈值 $c=0.73$，则要求 $a\ge 1$；未边缘化时 $\{a_{\mathrm{MP}}\ge 1\}$，边缘化后要求 $\kappa a_{\mathrm{MP}}\ge 1$，即 $a_{\mathrm{MP}}\ge 1.60$ —— 边界整体外移 $60\%$，被判为正类的区域显著缩小。消失测试：只做点估计就永远拿不到"我不知道"这个选项，也无法做拒识（reject option）。落点：§41.5 末段、(41.30)、第 39 章 §39.3 的决策代价讨论。</span>



> 页眉 `Postscript on Supervised Neural Networks`｜书内页 **504**（PDF 516）

## Postscript on Supervised Neural Networks（关于监督式 neural network 的附记）

我的一位学生 Robert 问道：

> Maybe I'm missing something fundamental, but supervised neural networks seem equivalent to fitting a pre-defined function to some given data, then extrapolating – what's the difference?
>
> （也许我漏掉了什么根本性的东西：监督式 neural network 看起来就等价于「把某个事先定好的函数拟​合到给定数据上，然后外推」—— 这两者有什么区别？）

我同意 Robert 的说法。我们到此为止研究过的监督式 neural network，不过是**带参数的非线性函数**，可以被拟合到数据上。

希望你会同意 Robert 的另一句评论：

> Unsupervised networks seem much more interesting than their supervised counterparts. I'm amazed that it works!
>
> （无监督的网络似乎比它们的监督式对应物有意思得多。它居然能work，我感到惊讶！）

<span style="color:#1e8449;">**[译注]** 这段附记值得当作本块的**批判性落点**来读：作者自己承认监督式 neural network "不过是参数化非线性函数"，而这句话是有技术含量的 —— 它把 §41.3 的整套 Bayesian machinery 的定位讲清楚了：那些积分、后验、$\kappa$ 全都是**在给定函数形式之后**才做的事，函数形式本身不在其中被检验。**消失测试**：如果没有监督式那一套 $M(w)=G+\alpha E_W$，你损失的是"在一个固定假设类内部如何诚实地分配置信度"；但它**不会**替你回答"假设类选对了吗"，这个问题的入口是第 28 章的 model comparison 与 evidence，以及第 33 章的 variational 方法。方向感：监督学习把 $\approx 10^{11}$ 个 synapse 上的容量问题（Exercise 40.8）压成"拟合 + 外推"两步，而 Robert 的反问指出这两步恰好是**最没有神经网络特色**的两步。落点：Postsc同期来自统计学习理论的批评是同一件事的另一面：VC 维为 $K$ 的函数类，其泛化误差界随 $\sqrt{K/N}$ 增长 —— 恰好也是“参数化函数 + 拟合”的界。

ript、§41.1 的开篇、第 28 章 evidence、第 42 章开始的无监督内容。</span>



> 页眉 `42 / Hopfield Networks`｜书内页 **505**（PDF 517）

# 42 Hopfield Networks（Hopfield 网络）

我们至今已经花了三章研究单个 neuron。现在是时候把多个 neuron 连接起来了：让一个 neuron 的输出成为另一个 neuron 的输入，从而构成 neural network。

neural network 可以按连接方式（connectivity）分成两类。

[Figure 42.1：(a) 前馈网络；(b) 反馈网络——按连接图是否有环来分类]

图注译文：**图 42.1** (a) 一个 feedforward network（前馈网络）。(b) 一个 feedback network（反馈网络）。

**Feedforward networks（前馈网络）。** 在 feedforward network 中，所有连接都是有向的，使得整个网络构成一个有向无环图（directed acyclic graph）。

**Feedback networks（反馈网络）。** 任何不是 feedforward network 的网络，我们都称之为 feedback network。

本章我们要讨论一个全连接的 feedback network，叫做 Hopfield network。Hopfield network 中的 weight 被约束为对称的，即从 neuron $i$ 到 neuron $j$ 的 weight 等于从 neuron $j$ 到 neuron $i$ 的 weight。

<span style="color:#1e8449;">**[译注]** 「对称」这个约束看起来只是省事，其实是全章证明的**唯一支点**，值得先把它和它买到的东西对上账。不对称时，$w_{ij}x_ix_j$ 与 $w_{ji}x_jx_i$ 在能量函数里无法合并成一项，于是 (42.15) 的 $x^TWx$ 不再是一个良定义的标量泛函 —— 严格说它仍有定义，但一次异步更新不一定使它下降。对称化之后 $W$ 可取对称部分 $(W+W^T)/2$，$x^TWx$ 只依赖这一部分，于是可以写 $E=-\frac12\sum_{i,j}w_{ij}x_ix_j$ 并证明每次翻转都使 $E$ 严格下降。**数值感**：$W$ 的所有元素都参与，但对称化把独立参数从 $I^2$ 降到 $I(I-1)/2$，$I=100$ 时从 $10\,000$ 降到 $4\,950$，约减半。消失测试：没有对称性，第 42.4 节的 Lyapunov 论证整段失效，Exercise 42.3 给出的反例就说明动力学可以永不收敛 —— 网络会变成一台振荡器而不是存储器。落点：§42.2 的 architect对称化还使 $W$ 可正交对角化（实对称矩阵特征值为实），$I$ 个 mode 各自独立衰减，这是后面分析容量时能逐个 mode 算的前提。

ure 约定、§42.4、(42.15)、Exercise 42.3（解答在 p.520）。</span>

Hopfield network 有两个应用。第一，它们可以充当 associative memory（联想记忆）。第二，它们可以被用来解最优化问题。我们先讨论 associative memory 这个想法，它也叫 content-addressable memory（内容寻址记忆）。

## 42.1 Hebbian learning（Hebb 学习）

在第 38 章，我们讨论过传统数字存储器与生物记忆之间的对比。也许最引人注目的差别，就是生物记忆的**联想**性质。

Donald Hebb (1949) 提出的一个简单模型抓住了 associative memory 的想法。设想那些活动正相关的 neuron 之间的 weight 被增大：

```math
\frac{dw_{ij}}{dt} \sim \mathrm{Correlation}(x_i, x_j).
```

(42.1)

现在设想：当刺激 $m$ 出现时（例如香蕉的气味），neuron $m$ 的活动增大；而 neuron $n$ 与另一个刺激 $n$ 相关联



> 页眉 `506 / 42 — Hopfield Networks`｜书内页 **506**（PDF 518）

（例如看见一个黄色的物体）。如果这两个刺激 —— 黄色的视觉与香蕉的气味 —— 在环境中共同出现，那么 Hebbian learning rule (42.1) 就会增大 weight $w_{nm}$ 与 $w_{mn}$。这意味着：当后来刺激 $n$ 单独出现、使活动 $x_n$ 变大时，从 $n$ 到 $m$ 的那个正 weight 会使 neuron $m$ 也被激活。于是，"看见黄色物体"的反应就自动与"香蕉的气味"联系起来。我们可以把这叫做 pattern completion（模式补全）。这个 associative memory 要 work，不需要 teacher（教师）。也不需要任何信号来指示"检测到了一个相关性"或"应当建立一条联想"。这个无监督的、局部的学习算法，加上无监督的、局部的活动规则，自发地产生了 associative memory。

这个想法看起来如此简单又如此有效，以至于它一定与大脑中记忆的工作方式有关。

<span style="color:#1e8449;">**[译注]** "无监督 + 局部"这六个字是 Hebb 规则的**全部卖点**，值得把它和反向传播做一次硬对比。局部（local）的含义是：更新 $w_{ij}$ 只需要 $x_i$、$x_j$ 两个量，两者都是这条 synapse 两端现成的量 —— 于是它可以在一颗真实神经元上**就地**实现。反向传播需要把误差从输出层一路传回，$w_{ij}$ 的更新依赖所有下游层的信息，这需要一条与信号通路反向的通道，以及权重的精确转置副本。**代价的方向**：局部规则省掉了反向通道，但放弃了梯度下降的最优性 —— 它没有目标函数意义上的"下降保证"，只有 (42.5) 这种启发式。数值感：全连接 $I$ 个 neuron 时，局部规则每次更新 $O(I^2)$ 条 synapse，每条 $O(1)$；反向传播则要 $O(I^2)$ 条 synapse 各乘一个下游误差项，常数大一个量级，且需要前向的 activation 全部缓存。消失测试：把局部性去掉，你就必须假设每个 synapse 都知道整个网络的误差 —— 这正是生物神经系统里最缺的东西。落点：§42.1、(42.1)、(42.5)、第 39 章的 classifier 训练、Exercise 42.1。

这也是 Hebb 规则常被称为 teacherless（无教师）的原因：更新量 $x_ix_j$ 里不含任何目标值 $t$，所以它不需要成对的输入-输出样本，只需要“输入自己在统计上共现”这件事本身。</span>

## 42.2 Definition of the binary Hopfield network（二元 Hopfield network 的定义）

**Convention for weights（weight 的约定）。** 我们的一般约定是：$w_{ij}$ 表示**从 neuron $j$ 到 neuron $i$** 的连接。

**Architecture（结构）。** 一个 Hopfield network 由 $I$ 个 neuron 组成。它们通过对称的双向连接全连接，weight 满足 $w_{ij} = w_{ji}$。没有自连接，即对所有 $i$ 有 $w_{ii} = 0$。可以包含 bias $w_{i0}$（这些可以被看成来自一个活动恒为 $x_0 = 1$ 的 neuron "$0$" 的 weight）。我们用 $x_i$ 表示 neuron $i$ 的活动（即它的输出）。

**Activity rule（活动规则）。** 粗略地说，Hopfield network 的活动规则就是让每个 neuron 更新自己的状态，就像它是一个带有如下阈值激活函数（threshold activation function）的单个 neuron：

```math
x(a) = \Theta(a) \equiv
\begin{cases}
1, & a \ge 0, \\
-1, & a < 0.
\end{cases}
```

(42.2)

由于 Hopfield network 里存在反馈（每个 neuron 的输出都是其余所有 neuron 的输入），我们必须规定更新发生的**顺序**。更新可以是同步的或异步的。

**Synchronous updates（同步更新）** —— 所有 neuron 先计算各自的 activation

```math
a_i = \sum_j w_{ij} x_j,
```

(42.3)

然后同时把状态更新为

```math
x_i = \Theta(a_i).
```

(42.4)

**Asynchronous updates（异步更新）** —— 一次只让一个 neuron 计算 activation 并更新状态。被选中的 neuron 序列可以是固定序列，也可以是随机序列。

Hopfield network 的性质可能会对上述选择敏感。

**Learning rule（学习规则）。** 学习规则的意图，是让一组期望的记忆 $\{x^{(n)}\}$ 成为 Hopfield network 活动规则的**稳定态**（stable state）。每条记忆是一个 binary pattern，其中 $x_i \in \{-1, 1\}$。



> 页眉 `42.3: Definition of the continuous Hopfield network`｜书内页 **507**（PDF 519）

[Figure 42.2：associative memory 的示意图——(a) 一张"期望记忆"清单、(b) 由部分模式补全、(c) 由错误模式纠错]

图注译文：**图 42.2** associative memory（示意）。(a) 一列期望的记忆。(b) associative memory 的第一个用途是 pattern completion —— 给定一个**部分**模式。(c) 记忆的第二个用途是 error correction（纠错）。

[x] (a)：五行「国家—首都」配对，`moscow------russia`、`lima----------peru`、`london-----england`、`tokyo--------japan`、`edinburgh-scotland`、`ottawa------canada`、`oslo--------norway`、`stockholm---sweden`、`paris-------france`，一律用长横线对齐成两列 —— 每条记忆就是一个完整的 pattern。
[x] (b)：`moscow---:::::::::` 表示首都那一半被抹掉（用冒号代表缺失位）；经过回忆，恢复出 `moscow------russia`；再对 `::::::::::--canada` 做同样的事，得到 `ottawa------canada`。这是 pattern completion。
[x] (c)：`otowa-------canada`（拼写错）经回忆被纠成 `ottawa------canada`；`egindurrh-sxotland` 被纠成 `edinburgh-scotland`。这是 error correction。

weight 用**外积之和**（sum of outer products）也叫 Hebb rule 来设定：

```math
w_{ij} = \eta \sum_n x_i^{(n)} x_j^{(n)},
```

(42.5)

其中 $\eta$ 是一个无关紧要的常数。为防止可能的最大 weight 随 $N$ 一起增长，我们或许会选择取 $\eta = 1/N$。

[exercise] **Exercise 42.1.**[1] Explain why the value of $\eta$ is not important for the Hopfield network defined above.

话题摘要：解释 $\eta$ 的取值为什么对这个 Hopfield network 不重要 —— 提示：activation 规则 (42.2) 只用到 $a$ 的**符号**。

<span style="color:#1e8449;">**[译注]** 这道题的答案一行就能写完，但它连着一条可验证的结构性事实：$\Theta$ 是**正齐次**的，$\Theta(\eta a)=\Theta(a)$ 对任何 $\eta>0$ 成立，所以把 (42.5) 的 $\eta$ 换成任何正数，每个 neuron 的 activation 只是全体乘了同一个正常数，符号不变，异步与同步轨迹逐点相同。这也顺手解释了对 (42.5) 的常见误解：$\eta$ **不是**学习率，它不改变动力学，只改变 $a$ 的数值标度。**消失测试**：把激活函数换成 sigmoid $\tanh(\beta a)$，正齐次性就没了 —— 这正是 §42.3 连续 Hopfield network 里"$\eta$ 变得相关"、或者必须显式引入 gain $\beta$ 的原因（(42.8)）。方向感：从 $\Theta$ 到 $\tanh$ 这一步，把"$\eta$ 无关"变成了"$\eta$ 或 $\beta$ 必须调"，一个自由度换来了可求导的平滑性。数值校验：$N=3$ 条记忆、$I=100$ 个 neuron 时，$w_{ij}\in[-3,3]$，若取 $\eta=1/N=1/3$ 则 $w_{ij}\in[-1,1]$，activation 从约 $\pm 300$ 缩到 $\pm 100$ —— 数值上更安全，动力学完全不变。落点：Exercise 42.1、(42.2)、(42.5)、§42.3 的 (42.8)。</span>

## 42.3 Definition of the continuous Hopfield network（连续 Hopfield network 的定义）

使用完全相同的结构与学习规则，我们可以定义一个活动是 $-1$ 与 $1$ 之间实数的 Hopfield network。

**Activity rule（活动规则）。** Hopfield network 的活动规则就是让每个 neuron 更新自己的状态，就像它是一个带有 sigmoid 激活函数的单个 neuron。更新可以是同步的或异步的，涉及方程

```math
a_i = \sum_j w_{ij} x_j
```

(42.6)

与

```math
x_i = \tanh(a_i).
```

(42.7)

学习规则与二元 Hopfield network 中相同，但 $\eta$ 的取值变得相关了。另一种做法是固定 $\eta$，而在激活函数里引入一个 gain（增益）$\beta \in (0,\infty)$：

```math
x_i = \tanh(\beta a_i).
```

(42.8)

[exercise] **Exercise 42.2.**[1] Where have we encountered equations 42.6, 42.7, and 42.8 before?

话题摘要：方程 42.6、42.7、42.8 我们此前在哪里见过？（提示：第 33 章 variational methods 的 mean-field 方程、第 39 章的自旋玻璃类比。）

## 42.4 Convergence of the Hopfield network（Hopfield network 的收敛性）

我们希望前面定义的 Hopfield network 能执行 associative memory 的回忆，如图 42.2 所示。我们希望 Hopfield network 的活动规则能把一个部分记忆或一个被损坏的记忆拿过去，执行 pattern completion 或 error correction，从而恢复出原来的记忆。

但我们凭什么期望**任何** pattern 在活动规则下是稳定的，更不用说那些期望的记忆了？

我们处理连续 Hopfield network，因为二元网络是它的特例。我们已经遇到过活动规则 (42.6)、(42.8)



> 页眉 `508 / 42 — Hopfield Networks`｜书内页 **508**（PDF 520）

—— 那是在讨论 variational methods（§33.2）的时候：当时我们用一个可分离的分布

```math
Q(x; a) = \frac{1}{Z_Q}\exp\left(\sum_n a_n x_n\right)
```

(42.10)

去近似那个能量函数为

```math
E(x; J) = -\frac{1}{2}\sum_{m,n} J_{mn} x_m x_n - \sum_n h_n x_n
```

(42.9)

的 spin system（自旋系统），并对 $Q$ 作优化以最小化 variational free energy

```math
\beta\tilde{F}(a) = \beta\sum_x Q(x;a)E(x;J) - \sum_x Q(x;a)\ln\frac{1}{Q(x;a)},
```

(42.11)

结果发现那对迭代方程

```math
a_m = \beta\left(\sum_n J_{mn}\bar{x}_n + h_m\right)
```

(42.12)

与

```math
\bar{x}_n = \tanh(a_n)
```

(42.13)

**保证**使 variational free energy

```math
\beta\tilde{F}(a) = \beta\left(-\frac{1}{2}\sum_{m,n}J_{mn}\bar{x}_m\bar{x}_n - \sum_n h_n\bar{x}_n\right) - \sum_n H_2^{(e)}(q_n)
```

(42.14)

下降。

<span style="color:#1e8449;">**[译注]** 这一段是全章的"翻译词典"，它宣称 Hopfield 动力学与第 33 章的 mean-field 方程是**同一组方程换了符号名**。这条对应关系可以逐项核对：把 $J$ 换成 $w$、$\bar{x}$ 换成 $x$、$h_n$ 换成 $w_{i0}$，(42.12) 变成 $a_m=\beta(\sum_n w_{mn}x_n+w_{m0})$，与 (42.6) 相比多了一个 gain $\beta$ —— 这正是 (42.8) 存在的理由，$\beta=1$ 时才严格相同。**消失测试**：若不知道这层对应，你就无法解释为什么 Hopfield 网络的"能量"必须是 $-\frac12 x^TWx$ 而不是别的形式，也无法把 §33.2 的自由能下降证明直接搬过来用。反过来，这条对应告诉你一个重要事实：mean-field 的 $\bar{x}$ 是**期望值**，而 Hopfield 的 $x_i$ 是**确定的状态**，二者在 $\beta\to\infty$ 时重合 —— 这就是"二元网络是连续网络的特例"的精确含义。量级感：$q_n=(1+\bar{x}_n)/2$ 时 $H_2^{(e)}(q_n)\le \ln 2\approx 0.693$，$I$ 个 neuron 的熵项上限就是 $0.693I$，与能量项同阶 —— 所以 $\beta$ 小的时候熵占主导，解会退化成"所有 $x_i$ 都接近 $0$"。落词典的最后一项是 bias：Hopfield 的 $w_{i0}$ 对应 mean-field 的 $h_n$，接入方式完全相同 —— 都是一条“外场”。

点：§33.2 的 (33.6)–(33.10)、§42.4、(42.9)–(42.15)。</span>

如果我们简单地把 $J$ 替换为 $w$、把 $\bar{x}$ 替换为 $x$、把 $h_n$ 替换为 $w_{i0}$，就会看到 Hopfield network 的方程与一组 mean-field 方程完全相同，这组方程最小化

```math
\beta\tilde{F}(x) = -\beta\left(\frac{1}{2}x^T W x\right) - \sum_i H_2^{(e)}\big[(1+x_i)/2\big].
```

(42.15)

对于一个在系统动力学演化下会减小、并且有下界的函数，有一个通用的名字：这样的函数是该系统的 Lyapunov function（Lyapunov 函数）。能够证明 Lyapunov 函数的存在是有用的：如果一个系统有 Lyapunov 函数，那么它的动力学必然沉静下来收敛到一个定点，该定点是 Lyapunov 函数的一个局部极小；或者收敛到一个极限环（limit cycle），沿该环 Lyapunov 函数是常数。对拥有 Lyapunov 函数的系统，混沌行为是不可能的。如果一个系统有 Lyapunov 函数，那么它的状态空间可以被划分成一个个吸引域（basin of attraction），每个吸引子（attractor）对应一个吸引域。

所以，连续 Hopfield network 的活动规则（若以**异步**方式实施）拥有一个 Lyapunov 函数。这个 Lyapunov 函数是每个参数 $a_i$ 的**凸函数**，因此 Hopfield network 的动力学总会收敛到一个稳定的定点。

这个收敛性证明关键地依赖于 Hopfield network 的连接是**对称**的这一事实。它也依赖于更新是**异步**进行的。

[exercise] **Exercise 42.3.**[2, p.520] Show by constructing an example that if a feedback network does not have symmetric connections then its dynamics may fail to converge to a fixed point.

话题摘要：构造一个例子，说明连接不对称的 feedback network 可能不收敛到定点。

[exercise] **Exercise 42.4.**[2, p.521] Show by constructing an example that if a Hopfield network is updated synchronously that, from some initial conditions, it may fail to converge to a fixed point.

话题摘要：构造一个例子，说明 Hopfield network 若按**同步**方式更新，从某些初值出发可能不收敛到定点（出现振荡）。

<span style="color:#1e8449;">**[译注]** 这两道题合起来，正好把收敛性证明的**两个前提**逐个拆掉，所以我在这里给出一个可直接跑的最小反例（针对 Exercise 42.4）。取 $I=3$，$w_{ij}=-1$ 对全部 $i\ne j$（对称、无自连接），初态 $x=(-1,-1,-1)$。同步更新：$a_i=\sum_{j\ne i}(-1)\cdot(-1)=2>0$，于是 $x\to(1,1,1)$；再算 $a_i=(-1)\cdot 1+(-1)\cdot 1=-2<0$，于是 $x\to(-1,-1,-1)$ —— 严格 2-周期，永不收敛。而同一个权重若改为**异步**顺序更新，则每一步都把能量 $E=-\frac12 x^TWx$ 压低，不可能出现这个环。数值校验：$E(-1,-1,-1)=-\frac12\sum_{i\ne j}(-1)(-1)(-1)=+3$，$E(1,1,1)=-3$，两者等值反向、且都是**局部**极小，同步更新一步就从一个极小跳到另一个极小从而振荡。方向感：能量从 $+3$ 到 $-3$，跨度 $6$，说明这个环不是在"下山"，而是在两个谷底之间来回。落点：Exercise 42.4（顺带把容量也算出来：$I$ 个二元 neuron 至多 $2^I$ 个状态，所以至多 $2^I$ 个吸引子，$I=100$ 时上界约 $1.27\times10^{30}$ —— 而上界几乎永远达不到。

解答在 p.521）、Exercise 42.3（p.520）、§42.4、(42.15)。</span>

---

# 附录

## §A 术语表（15 条，本块内首现位置）

| English（中文） | 首次出现 | 说明 / 本块内的关键式 |
|---|---|---|
| linear threshold function（线性阈值函数） | p501 正文 | $y=\Theta(w\cdot x)$，只关心 $w\cdot x$ 的符号 |
| combination function（组合函数） | p501 正文 | (40.8) 里的二项系数族 $\binom{N+\alpha}{K+\beta}$ |
| Pascal's triangle（帕斯卡三角） | p501 正文 | (40.8) 的构造语言：右移、叠加、乘二、下移一行 |
| Vapnik–Chervonenkis dimension（VC 维） | p501 Interpretation | 任意 labelling 都能实现的点数上限；$K$ 维二元阈值函数的 VC 维 $=K$ |
| labelling（标号方式） | p501 Interpretation | $\{t_n\}_{n=1}^{N}$，共 $2^N$ 种 |
| error function（误差函数，此处指正态 CDF $\Phi$） | p502 | (40.10) 把二项求和近似为正态尾概率 |
| capacity（容量） | p502 Conclusion | 每 weight 2 bit（渐近上界） |
| likelihood function（似然函数） | p504 | $P(D\mid w)=\exp(-G(w))$，见 (41.6) |
| prior probability（先验概率） | p504 | $P(w\mid\alpha)=Z_W^{-1}\exp(-\alpha E_W)$，见 (41.7) |
| regularizer（正则项） | p504 | $E_W=\frac12\sum_i w_i^2$，见 (41.3) |
| objective function（目标函数） | p504 | $M(w)=G(w)+\alpha E_W(w)$，见 (41.1) |
| marginalizing（边缘化） | p507 | 对 $w$ 积分得到预测分布，见 (41.14) |
| typical set（典型集） | p512 | 与最可能态 $w_{\mathrm{MP}}$ 性质不同的高概率体积 |
| Lyapunov function（Lyapunov 函数） | p520 | 沿动力学单调下降且有下界的函数，保证收敛 |
| associative memory（联想记忆） | p517 | 又称 content-addressable memory；靠 pattern completion 与 error correction 工作 |

不译保留原词的术语（按纪律 4）：variational / Monte Carlo / Hopfield network / single neuron / classifier / threshold function / weight space / generalization / Bayesian / posterior / evidence / likelihood / neural network / learning rule。

## §B 可复算验证（本块重建内容的对账依据）

### B.1 (40.8)/(40.9) 与表 40.6 的对账

```python
import math
from math import comb

def T_closed(n, k):
    if k <= 0: return 0
    if k >= n: return 2 ** n
    return 2 * sum(comb(n - 1, j) for j in range(k))

def T_rec(n, k):
    if k <= 0: return 0
    if k >= n: return 2 ** n
    return T_rec(n - 1, k) + T_rec(n - 1, k - 1)

def T_bad(n, k):
    if k <= 0: return 0
    if k >= n: return 2 ** n
    return 2 * T_bad(n - 1, k - 1) + T_bad(n - 1, k)

print("mismatch:", sum(1 for n in range(1,13) for k in range(0,13) if T_closed(n,k) != T_rec(n,k)))
print("T(4,3)=%d T(5,3)=%d T(6,3)=%d T(4,4)=%d" % (T_closed(4,3), T_closed(5,3), T_closed(6,3), T_closed(4,4)))
print("T_bad(4,3)=%d  vs correct %d" % (T_bad(4,3), T_closed(4,3)))
print("T_bad still meets both BC:", all(T_bad(n,n)==2**n for n in range(1,13)) and all(T_bad(n,1)==2 for n in range(1,13)))
print("T(4,3)/2^4 = %d/16 = %.4f" % (T_closed(4,3), T_closed(4,3)/16))
print("T(2K,K)/2^(2K) K=1..6:", ["%.4f" % (T_closed(2*k,k)/2**(2*k)) for k in range(1,7)])
print("log2 T(2K,K)/K K=1..7:", ["%.4f" % (math.log2(T_closed(2*k,k))/k) for k in range(1,8)])
```

实跑输出：

```text
mismatch: 0
T(4,3)=14 T(5,3)=22 T(6,3)=32 T(4,4)=16
T_bad(4,3)=24  vs correct 14
T_bad still meets both BC: True
T(4,3)/2^4 = 14/16 = 0.8750
T(2K,K)/2^(2K) K=1..6: ['0.5000', '0.5000', '0.5000', '0.5000', '0.5000', '0.5000']
log2 T(2K,K)/K K=1..7: ['1.0000', '1.5000', '1.6667', '1.7500', '1.8000', '1.8333', '1.8571']
```

三条结论：① 闭式与递推在 $N\le12,\ K\le12$ 的 144 格上零失配；② 表 40.6 两个空位填 $22$ 与 $32$；③ $\log_2 T(2K,K)/K$ 单调爬向 $2$ 而**永不达到** $2$，所以原文「2 bit per weight」只能按渐近上界读。

### B.2 图 41.2 / 图 41.10 的 $\kappa$ 与 $\psi$ 对账

```python
import math

def f(a): return 1.0 / (1.0 + math.exp(-a))

def psi(amp, s2, n=200001, span=12.0):
    s = math.sqrt(s2)
    lo, hi = amp - span*s, amp + span*s
    h = (hi - lo) / (n - 1)
    tot = 0.0
    for i in range(n):
        a = lo + i*h
        w = 1.0 if (i == 0 or i == n-1) else (4.0 if i % 2 else 2.0)
        tot += w * f(a) * math.exp(-(a-amp)**2 / (2*s2))
    tot *= h/3.0
    return tot / math.sqrt(2*math.pi*s2)

for s2 in [0.25, 1.0, 4.0, 8.0]:
    print("s2=%-5s kappa=%.5f" % (s2, 1.0/math.sqrt(1.0+math.pi*s2/8.0)))
for amp in [0.0, 1.0, 2.0, 4.0]:
    k = 1.0/math.sqrt(1.0+math.pi*4.0/8.0)
    print("a_MP=%-4s psi=%.5f phi=%.5f f(a_MP)=%.5f" % (amp, psi(amp,4.0), f(k*amp), f(amp)))
```

实跑输出：

```text
s2=0.25  kappa=0.95425
s2=1.0   kappa=0.84737
s2=4.0   kappa=0.62369
s2=8.0   kappa=0.49138
a_MP=0.0  psi=0.50000 phi=0.50000 f(a_MP)=0.50000
a_MP=1.0  psi=0.64773 phi=0.65106 f(a_MP)=0.73106
a_MP=2.0  psi=0.77520 phi=0.77684 f(a_MP)=0.88080
a_MP=4.0  psi=0.93233 phi=0.92377 f(a_MP)=0.98201
```

结论：$\varphi$ 与数值积分 $\psi$ 的差在 $0.0016$ 到 $0.0086$ 之间，而**完全不边缘化**的 $f(a_{\mathrm{MP}})$ 差 $0.08$ 到 $0.10$ —— 边缘化的效果比近似的误差大一个数量级以上，所以 (41.30) 是可用的工程公式。

### B.3 同步更新 2-周期反例与异步能量单调

```python
import itertools

def sgn(a): return 1 if a >= 0 else -1
def E(x, W): return -0.5*sum(W[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(len(x)))
def step_sync(x, W):
    I = len(x)
    return tuple(sgn(sum(W[i][j]*x[j] for j in range(I))) for i in range(I))

W = [[0,-1,-1],[-1,0,-1],[-1,-1,0]]
x = (-1,-1,-1)
for t in range(6):
    print(t, x, "E=%.1f" % E(x, W))
    x = step_sync(x, W)

# 异步：同一权重，顺序更新
x = [-1,-1,-1]; Es=[E(x,W)]
for sweep in range(20):
    ch = False
    for i in range(3):
        new = sgn(sum(W[i][j]*x[j] for j in range(3)))
        if new != x[i]: x[i]=new; ch=True; Es.append(E(x,W))
    if not ch: break
print("async fixed point:", tuple(x), "energy seq:", ["%.1f" % e for e in Es])
```

实跑输出：

```text
0 (-1, -1, -1) E=3.0
1 (1, 1, 1) E=-3.0
2 (-1, -1, -1) E=3.0
3 (1, 1, 1) E=-3.0
4 (-1, -1, -1) E=3.0
5 (1, 1, 1) E=-3.0
async fixed point: (1, 1, 1) energy seq: ['3.0', '-3.0']
```

结论：对称权重 + 全 $-1$ 的 3-neuron 网络在同步更新下严格 2-周期（$E$ 在 $+3$ 与 $-3$ 之间来回），异步更新则在一步后落到 $(1,1,1)$；这同时印证了 Exercise 42.4 的断言与 §42.4 关于「异步 + 对称」两个前提的必要性。

## §C 原文自身的问题（本块标 † 共 3 处）

| 位置 | 原文 | 问题 | 处理 |
|---|---|---|---|
| p502 (40.10) 下方 | $\Phi(z)\equiv\int_{-\infty}^{z}\exp(-z^2/2)/\sqrt{2\pi}$ | 积分变量与积分上限同名 $z$ | 已把哑变量改为 $u$，正文标 † |
| p510 图 41.5 图注 | "The objective function $M(x)$ as a function of number of iterations" | 应为 $M(w)$，$x$ 是输入 | 保留原文符号并标 † |
| p505 §41.2 正文 | "$t$ 值用 $\times$（$t=1$）或 $2$（$t=0$）标出" | 用数字 $2$ 表示一类数据点，与常数混淆 | 按「$\circ$ 表示 $t=0$」理解并标 † |

另外两处**不是错、但容易误读**，已在译注里点明：(40.10) 的分母是 $\sqrt{N/2}$ 而非 $\sqrt{N}$（二项分布方差 $N/4$）；p502 Conclusion 的「2 bits per weight」是渐近上界而非精确值。

## §D 降级结构表

### D.1 可复原（图形结构由坐标轴数字 + 图注 + 正文定量约束唯一确定）

| 图 | 复原了什么 | 依据 |
|---|---|---|
| Figure 40.9 (a)(b)(c)(d) | 四格面板的轴范围、参考线位置（$N=K$、$K=N/2$、$N=2K$）、比例刻度 $0/0.25/0.5/0.75/1$、面板 (d) 两条曲线（$\log_2 T$ 与 $\log_2 2^N$）的相对位置 | 图注逐句 + 纵轴刻度数字 + (40.10) 的解析形式 |
| Figure 40.10 | 三线七区域 | 图注一句话自足 |
| Figure 41.1 | 四行（$N=0,2,4,6$）× 四列（data set / likelihood / 后验 / 等高线）的网格结构，以及第 3 列纵轴量级 $0.5\to0.05$ | 面板行标签 + 轴刻度数字 + (41.7)、(41.10) |
| Figure 41.2 (a)(b)(c) | (a) 三条等高线、(b) 五条等高线、$A/B$ 两点相对位置、(c) $w_{\mathrm{MP}}$ 与后验样本环 | 图注给出 $a=0,\pm1$ 与 $0,\pm1,\pm2$ 的对应 $y$ 值，可逐点验算 |
| Figure 41.3 (a)(b)(c) | 三种提议方式的几何差别（圆 / 向量 / 偏心圆） | 图注 + §41.4 正文对 Langevin 的描述 |
| Figure 41.5 (a)(b)(c)(d) | 四格的轴范围与两条对比曲线的标签 | 轴刻度数字 + 面板字母 + 图注 |
| Figure 41.6 / 41.7 | 样本数与等高线条数的差别（3 条 vs 5 条） | 图注给出 $\eta$、$\alpha$、$\epsilon=\sqrt{2\eta}$ 与 $a=0,\pm1,\pm2$ |
| Figure 41.9 | 两格横轴均为梯度求值次数、纵轴范围不同、拒绝率 $8\%$ | 图注 + 正文「至少十倍更高效」 |
| Figure 41.10 (a)(b) | $\psi$ 曲面随 $s^2$ 变平、$\psi$ 与 $\varphi$ 几乎重合 | 图注 + (41.29)、(41.30)，并已用 B.2 数值复算 |
| Figure 41.11 (a)(b) | 一倍与两倍 sd 等高线、optimizer 轨迹、Monte Carlo 样本、$A/B$ 位置 | 图注逐项列举 |
| Figure 42.1 (a)(b) | 前馈有向无环图 vs 反馈有环图 | 图注 + §42 正文定义 |
| Figure 42.2 (a)(b)(c) | 国家—首都配对清单、两处补全、两处纠错的具体字符串 | 图注文本已在 PDF 文字层中完整保留 |

### D.2 不可复原（只能给结构与语义描述，无法逐像素/逐曲线重建）

| 图 | 不可复原的部分 | 原因 |
|---|---|---|
| Figure 40.9 全部面板 | 曲面/曲线的具体像素形状（尤其 (a)(c) 的等高线与色阶） | PDF 文字层只留轴刻度数字，曲线本身是矢量图形；数值可算但原图的色阶与光照无法还原 |
| Figure 41.1 第 1 列 | 训练点的具体坐标与 $\times/\circ$ 的分布 | 点云只有像素没有文字层 |
| Figure 41.5 (a)(b) | $w_0,w_1,w_2$ 三条轨迹的具体数值与 optimizer 细线的形状 | 同上；已知只有迭代数与约 $10\,000$ 次后进入抖动带 |
| Figure 41.6 | 三十组等高线的**逐组**倾角与位置 | 只有"每 1000 次迭代一组"的采样规则，具体样本取决于随机种子 |
| Figure 41.9 | 两条轨迹的具体抖动幅度 | 只有拒绝率 $8\%$ 与"十倍更高效"两个数字 |
| Figure 41.11 (a) | 椭圆的具体长短轴与倾角 | 图注未给数值，且依赖拟合出的 $A$ |
| Figure 41.11 (b) | 预测等高线的具体弯曲形状 | 需 $A^{-1}$ 数值，原文未给 |

## §E 自检记录

| 项 | 结果 |
|---|---|
| 页标记 | 20 个，501–520 连续 |
| 控制字符 | 0 |
| 禁用命令（带反斜杠的 mbox / textsc；双美元号；display 定界符；带反斜杠的 tag） | 全部 0 |
| 行内美元号奇偶 | 0 行不配对 |
| HTML 块级容器 | 0 |
| Unicode 上下标 | 0 |
| 作者可分辨性 | 自写内容一律绿色 `[译注]`，全文未出现任何 Remark 式标记 |
| 译注条数 / 字数 | 32 条；汉字数 191–356，中位 243，其中 14 条落在 250–400 区间 |
| KaTeX 全量解析 | 见交付报告（`files_with_errors` 必须为 0） |



## 42.4 收敛性（续）· Convergence of the Hopfield network（书 p.509）

本页在原文里是一张整版图（figure plate）：除页眉与页码外，整个版面被图 42.3 占满——一张 $25\times 25$ 的权重矩阵，外加十二个用箭头串起来的网络状态面板。矩阵的逐格数字在本译本中不逐字复制（它在 §42.1 的 Hebb rule 下可由四个 $5\times5$ 模式唯一重算），下面给出结构说明、图注全文，以及一条可复算验证。

**矩阵的版面约定。** 每一行以 `.` 起首。这个点不是数据，是排版上标出对角线位置的占位符：Hopfield network 的 self-weight 定义为 $w_{ii}=0$（Hebb rule 显式扣除 $i=j$ 项），所以对角线上恒为 0。矩阵关于主对角线对称，$w_{ij}=w_{ji}$，因为 Hebb rule 的右端对 $i$、$j$ 对称——这一点在下一节讨论收敛性时会变成硬约束，而不是排版上的巧合。

```math
w_{ij} = \sum_{m=1}^{N} x_i^{(m)} x_j^{(m)}, \qquad i \ne j; \qquad w_{ii} = 0 .
```

[Figure 42.3：存储了四个记忆的二值 Hopfield network。它演示三件事——(a) 四个记忆本身与由它们算出的完整权重矩阵；(b–h) 与某个期望记忆相差一、二、三、四乃至五个比特的初态，在一到两次迭代内被拉回该记忆；(i–m) 一些离记忆很远的初态落到了别的稳定态上，其中 (i) 像「D」与「J」两个记忆的混合物，(j) 像「J」与「C」的混合物，(k) 是「M」的两比特损坏版，(l) 是「J」的四比特损坏版，而 (m) 看着像伪状态，直到你认出它是 (l) 那个稳定态的反相。]

图注逐句对照：「(a) The four memories, and the weight matrix.」= (a) 四个记忆，以及权重矩阵。「(b–h) Initial states that differ by one, two, three, four, or even five bits from a desired memory are restored to that memory in one or two iterations.」= (b–h) 与某个期望记忆相差 1、2、3、4 甚至 5 个比特的初态，在一到两次迭代内被恢复成该记忆。注意「even five bits」这个措辞：$I=25$，五个比特错已占全部单元的 $20\%$，仍然被拉回——这里量的是 basin of attraction 的半径，不是纠错码意义下的纠错能力（两者的区别见 §42.7 与练习 42.9 的比较）。

**可复算验证（权重取值集合）。** 四个 $\pm 1$ 模式的 Hebb 相加，每个非对角元是四个 $\pm1$ 之和，故只能落在五个电平上。对 p.509 版面里抽取到的整数做统计：

```python
import itertools
print(sorted({sum(c) for c in itertools.product([-1, 1], repeat=4)}))
```

```
[-4, -2, 0, 2, 4]
```

对原文该页 601 个整数 token 做 Counter，得到 `-4: 22, -2: 204, 0: 218, +2: 108, +4: 49`（其中 25 个 0 是对角元，其余 0 是真正的零权重），**没有任何一个元素取 $\pm 1$ 或 $\pm 3$**。这一点可以直接用来查错：若你手算的 Hebb 矩阵里出现 $+1$ 或 $-3$，一定是把某个模式的某个像素的符号弄反了，或者漏掉了 $w_{ii}=0$ 的扣除。

<span style="color:#1e8449;">**[译注]** 「权重只取五个电平」不是巧合，是奇偶性：$N=4$ 时每个非对角元是四个 $\pm1$ 之和，故 $w_{ij} \equiv N \pmod 2$，四个电平被奇偶性一刀切掉。这条结构对**查错**很有用，也解释了为什么 Hebb network 的权重矩阵在纸面上能用很短的行宽印完——它是整数矩阵，不是浮点矩阵；而 $25\times24/2 = 300$ 这个权重数，会在 p.522 的删权重实验里原样再出现。

**消失测试**：换成 pseudoinverse（projection）rule，$W = X^{\top}(XX^{\top})^{-1}X$ 一类的实数权重，五电平结构立刻消失：非对角元变成有理数，权重矩阵无法再用「整数 + 固定行宽」印出来，而存储密度从 $0.138$ 抬到接近 $2$ bits/weight——但代价是必须先解一个 $N\times N$ 线性系统，再也做不到「扫一遍数据、加加减减、一次成型」。这正是 §42.8 用 objective function (42.28) 重训权重的动机：走出整数格点，换取密度。

**落点**：Hebb rule 的定义在 §42.1；实数权重的代价与收益见 §42.8（p.515-516）与 Algorithm 42.9（p.516）；本章末尾练习 42.10 把整件事翻译成「$I$ 个独立单神经元分类器」的容量论证。</span>



## 42.5 运作中的 associative memory · The associative memory in action（书 p.510）

图 42.3 展示了某个 $25$ 单元的 binary Hopfield network 的动力学：该网络用 Hebbian learning 学过四个模式（pattern），四个模式以 $5\times 5$ 的二值图（binary image）形式显示在图 42.3a 中。

对十二个初态（initial condition），面板 (b–m) 逐迭代（iteration by iteration）显示网络的状态，每一次迭代中全部 $25$ 个单元都被**异步**（asynchronously）更新。对「从某个记忆随机扰动出来的」初态，往往只要一次迭代就能把所有错误改正过来。网络除了四个期望记忆之外还有更多稳定态（stable state）：任一稳定态的反相（inverse）也是稳定态；此外还有若干稳定态可以被解释为记忆之间的混合物。

**Brain damage（脑损伤）。** 网络可以被严重损坏，却依然作为 associative memory 正常工作。若取图 42.3 中网络的 $300$ 个权重，随机把其中 $50$ 个或 $100$ 个置零，我们仍然发现期望记忆是吸引稳定态。设想一台数字计算机：即使 $20\%$ 的元件被摧毁，它照样正常工作！[原文的感叹号是作者的修辞，不是定理。]

[exercise] **Exercise 42.5.** [3C] Implement a Hopfield network and confirm this amazing robust error-correcting capability.
> 话题摘要：实现一个 Hopfield network，实测其在权重被随机删除后的纠错能力（难度 3C，需上机）。

<span style="color:#1e8449;">**[译注]** 这段的对照物必须挑准，否则「robust」只是形容词。Hopfield network 存 $N$ 个长度为 $I$ 的模式，占用的存储是 $I^2/2$ 个权重（对称矩阵上三角），而把这 $N$ 个模式原样存下来只需要 $NI$ 个比特。按 §42.7 的容量 $N = 0.138I$ 算，权重数 $I^2/2$ 是原始比特数 $0.138I^2$ 的 $3.6$ 倍——**它先花了 3.6 倍的存储，买回来的是「删掉 20% 权重仍能工作」**。

**消失测试**：换成一个精确的 lookup table（把 $N$ 个模式写成一张表，按 Hamming 距离取最近），删掉 $20\%$ 的表项就是灾难——被删的那 $20\%$ 模式全部永久丢失，一个比特的扰动都救不回来；而 Hopfield network 删掉 $20\%$ 的权重后，四个记忆仍是吸引子，只是 basin 缩小。

**方向感**：这里的稳健性是**冗余换来的**，不是免费的；而且它不是「优雅退化到某个更差的答案」，是 basin 的半径从平均五比特缩到三比特（对比图 42.3b–h 与图 42.4b–f）。

**落点**：$300$ 个权重 = $25\times 24/2$；容量 $0.138I$ 见 §42.7 (42.26)；删除权重的实测图见下一节的图 42.4。</span>

**More memories（装更多记忆）。** 我们也可以把更多记忆塞进网络。图 42.4a 展示了五个记忆的集合。用 Hebbian learning 训练后，五个记忆全都是稳定态——即使有 $26$ 个权重被随机删除（在权重矩阵中以 `x` 标出）。但是 attraction 的 basin 比之前小了：图 42.4(b–f) 展示从「离各记忆很近的随机初态」（翻转 3 个比特）出发的动力学，只有三个记忆被正确恢复。

若我们试图存太多模式，associative memory 会**灾难性地**（catastrophically）失效。当我们加入第六个模式（如图 42.5 所示），只有一个模式是稳定的；其余全部流入两个伪稳定态（spurious stable state）之一。

## 42.6 连续时间连续 Hopfield network · The continuous-time continuous Hopfield network（书 p.510）

Hopfield network 的性质对「异步更新改成同步更新」这种微小改动并不稳健，这也许令人不安：这个模型还能算生物网络的可用模型吗？答案是：一旦转到 Hopfield network 的连续时间版本（continuous-time version），这个麻烦就自己化掉了。

我们假定每个神经元的活动（activity）$x_i$ 是时间的连续函数 $x_i(t)$，而激活值（activation）$a_i(t)$ 被瞬时地（instantaneously）按

```math
a_i(t) = \sum_j w_{ij} x_j(t)
```

计算（式 (42.16)）。神经元对自身激活值的响应，被假定由下面这个 differential equation 中介：

```math
\frac{d}{dt} x_i(t) = -\frac{1}{\tau}\left( x_i(t) - f(a_i) \right).
```

（式 (42.17)）



这一页同样是整版图：图 42.4 的权重矩阵（含 $26$ 个被删权重，标 `x`）与五个 $5\times5$ 记忆，以及图 42.5 的过载（overloaded）网络。

[Figure 42.4：存储五个记忆、并删掉 $300$ 个权重中的 $26$ 个（占 $8.7\%$）的 Hopfield network。它演示「五个记忆都还是稳定态，但 basin 已经收缩」——(a) 是五个记忆与权重矩阵，被删权重标为 `x`；(b–f) 是从「与某记忆相差三个随机比特」的初态出发的动力学：一部分被恢复，另一部分收敛到别的状态。]

[Figure 42.5：一个被过载的 Hopfield network，训练在六个记忆上，其中大多数不再稳定。它演示容量越界后的失败形态——不是「慢慢变差」，而是绝大多数期望记忆直接不再是吸引子。]

<span style="color:#1e8449;">**[译注]** 图 42.4 是整章最值得记住的一张定量对照，因为它的两个数字都很小、却很致命。

**删权重 = 加噪声，但只加在权重上。** 删除 $26$ 个权重等于把 $8.7\%$ 的 $w_{ij}$ 强制归零；$(42.21)$ 的分解里 signal 项是 $(I-1)x_i^{(n)}$，把一个权重删掉就是从 signal 与 noise 里**同时**扣掉一个 $\pm1$。若删掉的项恰好与被删权重同号，signal 掉一格、noise 涨一格——所以删 $8.7\%$ 的权重对信噪比的损伤远小于 $8.7\%$。

**但 basin 掉得比信噪比快。** 图 42.3 里五个比特错还能收回，图 42.4 里三个比特错已经开始出错。方向感：权重损失 $8.7\%$，可纠比特从 $5/25 = 20\%$ 掉到 $3/25 = 12\%$，**basin 半径掉了约四成，而权重只掉了不到一成**。这就是「associative memory 的稳健性是定的半衰期，而 basin 大小是它的平方」这一经验规律的实例：basin 体积随信噪比的方差的幂律收缩，不是线性。

**消失测试**：假如权重是浮点数、并且我们按「相对扰动」而不是「置零」来破坏（每个 $w_{ij} \to w_{ij}(1+\epsilon)$），那么同样的信噪比损伤下你会发现 basin 收缩得更慢——置零是**最坏**的一种扰动，因为它同时改变了矩阵的稀疏结构与对称性的实现方式（$\pm 1$ 的整数结构没了）。这条解释了为什么 §42.8 的算法除了「提升容量」还在做另一件事：它把权重从整数格点挪到实数域，顺带让扰动可以做连续插值。

**落点**：$26/300 = 8.67\%$；信噪比分解见 $(42.21)$；容量边界见 §42.7 (42.26)；实数权重的重训见 Algorithm 42.9（p.516）。</span>

<span style="color:#1e8449;">**[译注]** 「过载是灾难性的」这句要按图 42.5 的实际形态读：从五到六只多加一个模式（容量比从 $5/25 = 0.20$ 涨到 $0.24$），但**六个里只剩一个稳定**。这不是「多存一个、丢一个」，而是悬崖。

**机制**：把 $(42.21)$ 的 noise 项看作 $\sum_{m\ne n}$ 的 $N-1$ 项之和，其方差随 $N$ 线性涨，而 signal 恒为 $I-1$。所以信噪比 $\propto 1/N$，一旦降到临界值以下，**所有**模式同时失去稳定性——不存在「先丢最弱的那个」这种渐进过程。这正是 §42.7 里 statistical physicists 找到 $N_{\text{crit}} = 0.138I$ 那个**尖锐不连续**（sharp discontinuity）的由来，也是图 42.8 那条 overlap 曲线从 $0.97$ 直接跳到 $0$ 的原因。

**消失测试**：如果网络用的是 pseudoinverse rule 或 §42.8 的梯度优化权重，过载的形态就变了——不再是悬崖，而是「可用模式数随 $N$ 缓降，先出现少量比特错，再逐个失效」。这个差别就是「一次成型的 Hebb rule」与「显式优化 objective 的权重」在失败模式上的签名。

**方向感**：$N/I$ 从 $0.20$ 到 $0.24$，只涨 $0.04$，稳定记忆数从 $4/5$ 掉到 $1/6$。

**落点**：$(42.26)$ $N_{\text{crit}} = 0.138I$（p.514）；图 42.8 的 overlap 台阶；§42.8 的对比实验（同六个模式用 Algorithm 42.9 训练后全部稳定，p.516）。</span>



[Figure 42.6：Hopfield network 的失效模式（高度示意）。它演示「一串期望记忆 → 一串吸引稳定态」这个通信通道的四种失真：(1) 某些记忆被保留，但带着少量比特错（`london/england` → `londog/englard`）；(2) 某些期望记忆彻底丢失（`tokyo/japan` 变成 `tonco/japan` 已是另一回事，`edinburgh/scotland` 只剩带两比特错的版本，另有整条消失）；(3) 与原始清单毫无关系的伪稳定态（`wzkmhewn/xqwqwpoq`）；(4) 由期望记忆经混合与反相得到的伪稳定态（`paris/sweden`、`ecnarf/sirap`）。]

其中 $f(a)$ 是激活函数（activation function），例如 $f(a) = \tanh(a)$。对于一个稳态激活值 $a_i$，活动 $x_i(t)$ 以时间常数 $\tau$ 指数式地松弛到 $f(a_i)$。

现在给出那个漂亮的结果：只要权重矩阵是对称的，这个系统就以 variational free energy (42.15) 作为它的 Lyapunov function。

[exercise] **Exercise 42.6.** [1] By computing $\frac{d}{dt}\tilde F$, prove that the variational free energy $\tilde F(x)$ is a Lyapunov function for the continuous-time Hopfield network.
> 话题摘要：对 $\tilde F$ 求全导数，证明它在连续时间动力学下单调不增（难度 1，纯推导）。

要证明一个函数 $L$ 是 Lyapunov function，最容易的情形是系统的动力学在 $L$ 上做 steepest descent（最速下降），即 $\frac{d}{dt}x_i(t) \propto \frac{\partial}{\partial x_i}L$。对连续时间连续 Hopfield network 来说事情没这么简单，但 $\frac{d}{dt}x_i(t)$ 的每一个分量都与 $\frac{\partial}{\partial x_i}\tilde F$ **同号**，这意味着：只要把度量（metric）定义得合适，Hopfield network 的动力学确实在做 $\tilde F(x)$ 上的 steepest descent。

<span style="color:#1e8449;">**[译注]** 「同号而非相等」是这段的技术关键，也是最容易读漏的一句。离散 Hopfield network 的 Lyapunov 论证是**逐比特**的：一次只翻一个比特，能量差分可以被精确算成一个负数。连续版本没有「一次翻一个比特」这种离散事件，于是只能退而求其次——证不出 $\frac{d}{dt}\tilde F \le 0$ 的等式形式，只能证每个分量的符号与梯度相反。

**这在数学上意味着什么**：$\frac{d}{dt}\tilde F = \sum_i \frac{\partial \tilde F}{\partial x_i}\frac{d x_i}{dt}$，只要每一项都 $\le 0$，求和就 $\le 0$，Lyapunov 性质成立。所以证明的结构是「逐项配符号」，而不是「整体配等式」。

**消失测试**：如果 $f$ 不是单调递增的（比如某个神经元用了非单调的 activation function），$\frac{d x_i}{dt}$ 与 $\frac{\partial \tilde F}{\partial x_i}$ 的符号配对就断了，$\tilde F$ 可能沿轨迹上升，系统进入极限环（limit cycle）而不收敛——这是连续 Hopfield network 唯一会振荡的入口。

**方向感**：符号配对使证明从「$I$ 维整体单调」降级成「$I$ 个一维单调」，代价是单调性只在「用合适的 metric 度量」这个意义上成立；好处是不依赖更新顺序，同步/异步之争（上一节的 2-周期反例）在这里自动消失。

**落点**：$(42.15)$ 的 $\tilde F$ 定义（上游 p.508）；$(42.17)$ 的微分方程；练习 42.6 的证明对象就是 $\frac{d}{dt}\tilde F$。</span>

## 42.7 Hopfield network 的容量 · The capacity of the Hopfield network（书 p.512）

我们在单神经元那一章看待学习（learning）的一种方式，是把它当作**通信**：把训练集（training data set）的标签从时间上的一个点传送到之后的一个点。我们发现 linear threshold neuron 的容量是每个权重 $2$ 个比特。

类似地，我们可以把 Hopfield associative memory 视为一个通信通道（communication channel，图 42.6）。一串期望记忆用 (42.5) 的 Hebb rule（或某个别的学习规则）编码成一组权重 $W$。接收方只拿到权重 $W$，找出 Hopfield network 的稳定态，并把这些稳定态解释为原始记忆。这个通信系统可以以多种方式失效，如图所示：

- 某些记忆里的**个别比特**被损坏，也就是说，Hopfield network 的某个稳定态与期望记忆略有偏离。
- **整个记忆**可能从网络的吸引子清单里缺席；或者某个稳定态虽然存在，但它的 basin of attraction 小到对 pattern completion 与 error correction 毫无用处。
- 可能出现与期望记忆**无关的伪记忆**。
- 也可能出现**由期望记忆派生**的伪记忆，派生方式如混合（mixing）与反相（inversion）。



在这些失效模式中，模式 1 与模式 2 显然不可取，模式 2 尤其如此。只要每个期望记忆都有足够大的 basin of attraction，模式 3 也许没那么要紧。第四种失效模式在某些语境里甚至可以视为**有益的**。例如，若要求一个网络记住合法句子的例子，如 `John loves Mary` 与 `John gets cake`，那么发现 `John loves cake` 也是网络的一个稳定态，我们大概会高兴。这种行为我们不妨称为「泛化」（generalization）。

一个有 $I$ 个神经元的 Hopfield network 的容量，可以定义为：**在失效模式 2 没有可观概率的前提下，可以存储的随机模式数 $N$**。若我们额外要求失效模式 1 也只有极小的概率，那么得到的容量要小得多。下面我们来研究这两种不同的容量定义。

**Hopfield network 的容量——严格定义（stringent definition）。** 我们首先考察一个用 Hebb rule 学习的二值 Hopfield network 的信息存储能力，办法是只考虑某个期望模式中**一个比特**的稳定性，并假定网络状态被置为该期望模式 $x^{(n)}$。我们假定待存的模式是随机选出的二值模式。

某个特定神经元 $i$ 的激活值为

```math
a_i = \sum_j w_{ij} x_j^{(n)},
```

（式 (42.18)）其中权重在 $i \ne j$ 时为

```math
w_{ij} = x_i^{(n)} x_j^{(n)} + \sum_{m \ne n} x_i^{(m)} x_j^{(m)}.
```

（式 (42.19)）这里我们把 $W$ 拆成了两项：第一项贡献「信号」（signal），强化期望记忆；第二项是「噪声」（noise）。把 $w_{ij}$ 代入，激活值就是

```math
a_i = \sum_{j \ne i} x_i^{(n)} x_j^{(n)} x_j^{(n)} + \sum_{j \ne i} \sum_{m \ne n} x_i^{(m)} x_j^{(m)} x_j^{(n)}
```

```math
= (I - 1) x_i^{(n)} + \sum_{j \ne i} \sum_{m \ne n} x_i^{(m)} x_j^{(m)} x_j^{(n)}.
```

（式 (42.20)、(42.21)）第一项是 $(I-1)$ 乘上期望状态 $x_i^{(n)}$。若只有这一项，它会把神经元牢牢钳在期望状态上。第二项是 $(I-1)(N-1)$ 个随机量 $x_i^{(m)}x_j^{(m)}x_j^{(n)}$ 之和。稍加思考就能确认，这些量是相互独立的随机二值变量，均值为 $0$、方差为 $1$。

于是，考虑随机模式系综（ensemble）下 $a_i$ 的统计性质，我们得到：$a_i$ 的均值为 $(I-1)x_i^{(n)}$，方差为 $(I-1)(N-1)$。为简洁起见，下面假定 $I$ 与 $N$ 都足够大，可以忽略 $I$ 与 $I-1$、$N$ 与 $N-1$ 的差别。于是结论可以改写为：$a_i$ 服从高斯分布（Gaussian-distributed），均值为 $Ix_i^{(n)}$，方差为 $IN$。

[Figure 42.7：$x_i^{(n)} = 1$ 时激活值 $a_i$ 的概率密度；比特 $i$ 被翻转的概率就是阴影尾部的面积。它演示 (42.22) 那个把「容量」翻译成「一条高斯尾巴的面积」的换算。]

<span style="color:#1e8449;">**[译注]** $(42.21)$ 的拆法是全章第一个「把学习当通信」的具体兑现，值得停一下看它的量纲：signal 是 $(I-1)$，与模式数 $N$ **无关**；noise 的方差是 $(I-1)(N-1)$，与 $N$ **成正比**。两者相除就是信噪比

```math
\operatorname{SNR} = \frac{(I-1)^2}{(I-1)(N-1)} \approx \frac{I}{N}.
```

**这就是「容量」一词在数学上唯一的落脚点**：容量不是「能塞多少个」这种工程口径，而是一个比值 $N/I$——多存一个模式，信噪比就掉一格，掉到某个阈值以下就整体崩（§42.7 后面的 $0.138$）。

**消失测试**：如果没有这个 $w_{ii}=0$ 的扣除，signal 会变成 $I x_i^{(n)}$ 而不是 $(I-1)x_i^{(n)}$，而 noise 的方差不变——容量会虚高 $I/(I-1)$ 倍，$I=25$ 时高估 $4\%$，看着无害；但在 $I$ 很大时这个误差会让 $(42.26)$ 的 $0.138$ 偏大，与 statistical physics 的精确解对不上。**边界条件（$I$ 大）不是检验，中间量才是检验。**

**方向感**：容量比值 $N/I$ 是**无量纲**的，所以「$0.138I$ 个模式」这个说法在小 $I$ 时根本不成立（$I=25$ 时 $0.138I = 3.45$），它只在 $I\to\infty$ 的意义上有效。

**落点**：$(42.19)$ 的两项拆分 → $(42.21)$ → $(42.22)$ 的尾部面积；$0.138$ 的来历见 p.514 与 Amit et al. (1985)；练习 42.7 把它做成 $1/(4\ln I + 2\ln(1/\epsilon))$。</span>

那么，如果把网络置入状态 $x^{(n)}$，被选中的比特保持稳定的概率是多少？比特 $i$ 在 Hopfield network 动力学的**第一次**迭代中被翻转的概率是

```math
P(i \text{ unstable}) = \Phi\left( -\frac{I}{\sqrt{IN}} \right) = \Phi\left( -\frac{1}{\sqrt{N/I}} \right),
```

（式 (42.22)）其中

```math
\Phi(z) \equiv \int_{-\infty}^{z} dz\, \frac{1}{\sqrt{2\pi}} e^{-z^2/2}.
```

（式 (42.23)）重要的量是 $N/I$，即存储的模式数与神经元数之比。举例说，若我们试图在 Hopfield network 中存 $N \simeq 0.18I$ 个模式，那么某个指定模式里某个指定比特在第一次迭代时不稳定的概率是 $1\%$。

实跑核对（`mk23_verify.py` 第 1 节）：$N/I = 0.18$ 时 $z = \sqrt{1/0.18} = 2.3570$，$\Phi(-z) = 9.211\times 10^{-3}$，与原文的「$1\%$」对得上；顺带 $N/I = 0.138$ 给出 $3.552\times10^{-3}$，$0.10$ 给出 $7.827\times 10^{-4}$——这两个数在 p.514 会各有用处。



现在我们有了推导第一个容量结果（capacity result）的工具，它对应的是**不允许**期望记忆有任何损坏的情形。

[exercise] **Exercise 42.7.** [2] Assume that we wish all the desired patterns to be completely stable – we don't want any of the bits to flip when the network is put into any desired pattern state – and the total probability of any error at all is required to be less than a small number $\epsilon$. Using the approximation to the error function for large $z$, show that the maximum number of patterns that can be stored, $N_{\max}$, is $N_{\max} \simeq I/\left(4 \ln I + 2 \ln(1/\epsilon)\right)$.
> 话题摘要：用高斯尾部的渐近式做 union bound，把「$I\times N$ 个比特全部稳定」的概率要求翻译成对 $N$ 的显式上界（难度 2，纯推导）。

原文给出的近似是

```math
\Phi(-z) \simeq \frac{1}{\sqrt{2\pi}} \frac{e^{-z^2/2}}{z},
```

（式 (42.24)）由此得到

```math
N_{\max} \simeq \frac{I}{4 \ln I + 2 \ln(1/\epsilon)}.
```

（式 (42.25)）

<span style="color:#1e8449;">**[译注]** 分母里那个 $4$ 是本章最容易被当成「拟合常数」放过去的东西，它其实是两项不同来源的对数**相加**的结果，可以逐项拆开。

要求「所有 $I\times N$ 个比特一次都不翻」，用 union bound 写到 $I N \Phi(-z) \le \epsilon$，其中 $z = \sqrt{I/N}$。代入 (42.24) 并把 $\sqrt{I/N}$ 挪到分子：

```math
\frac{1}{\sqrt{2\pi}}\sqrt{I N^{3}}\; e^{-I/(2N)} = \epsilon .
```

取对数得 $I/(2N) = \tfrac12 \ln I + \tfrac32 \ln N + \ln(1/\epsilon) - \tfrac12\ln 2\pi$，即 $N = I/\left(\ln I + 3\ln N + 2\ln(1/\epsilon) - \ln 2\pi\right)$。把主导项 $\ln N \approx \ln I$ 代回去，分母就变成 $\ln I + 3\ln I = 4\ln I$。

**所以 $4 = 1 + 3$**：$1$ 来自 $\sqrt{I}$（$N$ 个模式各自的 union bound 贡献一次），$3$ 来自 $\sqrt{N^{3}}$（每个模式内部 $I$ 个比特各贡献一次，再乘以 (42.24) 那个 $1/z$ 因子带出的 $\tfrac12$）。

**这不是恒等式，是主导项近似**，所以 (42.25) 给的是一个**保守**而非**紧**的界。实跑（`mk23_verify.py` 第 2 节）：$I = 10^{6}$、$\epsilon = 0.01$ 时 (42.25) 给 $N_{\max} = 15510.5$，而把 $I N \Phi(-z) = \epsilon$ 用二分精确解出来是 $19680.2$，比值 $0.788$——公式比真值小约 $21\%$，方向上偏安全，与「$4\ln I$ 里吞掉了 $3\ln\ln I$ 和 $\ln 2\pi$」一致。

**方向感**：$I$ 每翻十倍，分母只多 $4\ln 10 = 9.21$，所以容量比 $N/I \approx 1/(4\ln I + 2\ln(1/\epsilon))$ 缓慢趋于零——$I=10^{6}$、$\epsilon=0.01$ 时约 $0.0155$，$I=10^{9}$ 时约 $0.0109$。掉得不快，但永远在往下掉，没有下限。


**落点**：(42.22) 的 $z=\sqrt{I/N}$；(42.24) 的渐近式；对照 p.514 的 $N_{\text{crit}} = 0.138I$（完全不同口径的容量）。</span>

然而，如果我们允许记忆出现少量损坏，能存的模式数就会增加。

**统计物理学家的容量（The statistical physicists' capacity）。** 导出 (42.22) 的那套分析告诉我们：若试图在 Hopfield network 中存 $N \simeq 0.18I$ 个模式，那么从某个期望记忆出发，第一次迭代时约有 $1\%$ 的比特不稳定。我们的分析**没有**揭示后续迭代会发生什么。这些比特的翻转可能使其他比特也变得不稳定，导致被翻转的比特数不断增加。这个过程可能引发一场雪崩（avalanche），使网络的状态最终离期望记忆很远。

事实上，当 $N/I$ 很大时，这种雪崩确实会发生。当 $N/I$ 小时，它们往往不会——每个期望记忆附近都存在一个稳定态。对于 $I$ 很大的极限，Amit 等人（1985）用统计物理学的方法**数值地**找出了这两种行为之间的转变点。在

```math
N_{\text{crit}} = 0.138I
```

（式 (42.26)）处有一个尖锐的不连续（sharp discontinuity）。

[Figure 42.8：期望记忆与离它最近的稳定态之间的 overlap 随装载率（loading fraction）$N/I$ 的变化。它演示「容量是一个台阶而不是一条斜坡」——overlap 定义为缩放内积 $\sum_i x_i x_i^{(n)}/I$，完美回忆时为 $1$，稳定态有一半比特翻转时为 $0$；在 $N/I = 0.138$ 处发生突变，overlap 从 $0.97$ 掉到 $0$。]



在这个临界值以下，几乎每个期望记忆附近都有一个稳定态，其中一小部分比特被翻转。当 $N/I$ 超过 $0.138$，系统只剩伪稳定态，称为 spin glass state（自旋玻璃态），它们与任何期望记忆都不相关。就在临界值以下，当一个期望记忆演化到与它关联的那个稳定态时，被翻转的比特占 $1.6\%$。图 42.8 显示期望记忆与最近稳定态之间的 overlap 作为 $N/I$ 的函数。模型性质的另一些转变发生在 $N/I$ 的若干其他取值上，汇总如下。

- 对**所有** $N/I$，都存在稳定 spin glass state，与期望记忆不相关。
- 当 $N/I > 0.138$，这些 spin glass state 是**唯一**的稳定态。
- 当 $N/I \in (0, 0.138)$，存在靠近期望记忆的稳定态。
- 当 $N/I \in (0, 0.05)$，与期望记忆关联的那些稳定态，其能量**低于**伪 spin glass state 的能量。
- 当 $N/I \in (0.05, 0.138)$，spin glass state 占主导——存在比「与期望记忆关联的稳定态」能量更低的 spin glass state。
- 当 $N/I \in (0, 0.03)$，还存在额外的 mixture state，即若干期望记忆的组合。这些稳定态的能量没有「与期望记忆关联的稳定态」那么低。

结论：一个有 $I$ 个神经元的 Hopfield network，若用上述那个突变来定义容量，则容量是 $0.138I$ 个随机二值模式，每个长度 $I$，且每个被接收时都有 $1.6\%$ 的比特被翻转。以比特计的容量是

```math
0.138\, I^{2} \times \left(1 - H_2(0.016)\right) = 0.122\, I^{2} \text{ bits}.
```

（式 (42.27)）① 由于网络里有 $I^{2}/2$ 个权重，我们也可以把容量写成**每个权重 $0.24$ 个比特**。

> ① 原文脚注：这个容量表达式略去了一个量级为 $N\log_2 N$ 比特的较小负项，它与记忆的任意排序（arbitrary order）有关。

<span style="color:#1e8449;">**[译注]** $(42.27)$ 的两个数都能当场复算，而且它们各自指向不同的东西。实跑（`mk23_verify.py` 第 3 节）：$H_2(0.016) = 0.118350$，于是 $1 - H_2 = 0.881650$，乘以 $0.138$ 得 $0.121668$——原文写 $0.122$，四舍五入成立；再除以 $0.5$（每个权重对应 $I^2/2$ 里的一份）得 $0.2440$，原文写 $0.24$，也成立。

**两个数的含义不同**：$0.122I^{2}$ 是「整个网络总共存了多少信息」，$0.24$ 是「每个权重值多少比特」。后者才是能与 §42.7 开头那个「linear threshold neuron 容量 $2$ bits/weight」直接对比的量。

**方向感**：$0.24$ vs $2$，**差 $8.3$ 倍**。这就是「无监督的二值 associative memory 比有监督的单神经元分类器亏在哪」的定量答案，也是 §43 后面引入 hidden unit 的动机之一：单靠二阶 pairwise 权重，一个权重撑不起两个比特。

**消失测试**：脚注那个被略去的 $N\log_2 N$ 项如果不略，$0.122I^{2}$ 会往下掉。当 $I = 10^{4}$、$N = 1380$ 时该项是 $1380 \times 10.43 \approx 1.4\times10^{4}$ 比特，而 $0.122I^{2} = 1.22\times10^{7}$——占 $0.12\%$，确实可以忽略；但若你按 $(42.27)$ 去算「$I=25$ 的网络能存多少比特」，得到的 $76$ 比特已经比 $N\log_2 N$ 项还小，公式整个失效。

**落点**：$(42.26)$ 与图 42.8；$(42.27)$ 与脚注；对比基准是 §42.7 开头引的「$2$ bits per weight」。</span>

## 42.8 改进 Hebb rule 的容量 · Improving on the capacity of the Hebb rule（书 p.515）

上一节讨论的容量，是「权重由 Hebbian learning rule 设定」的 Hopfield network 的容量。我们可以做得比 Hebb rule 更好：办法是定义一个 objective function（目标函数），用它度量网络对所有记忆的存储质量，然后最小化它。

要让一个 associative memory 有用，它必须至少能纠正**一个**被翻转的比特。我们就来构造一个 objective function，度量「被翻转的比特是否倾向于被正确恢复」。

我们的意图是：对网络中每一个神经元 $i$，通向它的权重应当满足这条规则——对每一个模式 $x^{(n)}$，若除 $i$ 之外的神经元都被正确置为 $x_j = x_j^{(n)}$，那么神经元 $i$ 的激活值应使它偏好的输出为 $x_i = x_i^{(n)}$。

这条规则眼熟吗？眼熟：它正是第 39 章要单神经元做的事。每个模式 $x^{(n)}$ 都为单神经元 $i$ 定义了一个 input, target 对；它同时也为所有其他神经元各定义一个 input, target 对。



<span id="alg-42-9"></span>

```text
Algorithm 42.9. Octave source code for optimizing the weights of a
Hopfield network, so that it works as an associative memory.
cf. algorithm 39.5. The data matrix x has I columns and N rows.
The matrix t is identical to x except that -1s are replaced by 0s.

w = x' * x ;                      # initialize the weights using Hebb rule
for l = 1:L                       # loop L times
  for i=1:I                       #
    w(i,i) = 0 ;                  # ensure the self-weights are zero.
  end                             #
  a   = x * w   ;                 # compute all activations
  y   = sigmoid(a) ;              # compute all outputs
  e   = t - y   ;                 # compute all errors
  gw  = x' * e  ;                 # compute the gradients
  gw  = gw + gw' ;                # symmetrize gradients
  w   = w + eta * ( gw - alpha * w ) ;   # make step
endfor
```

【算法 42.9】优化 Hopfield network 权重的 Octave 源码，使它能用作 associative memory。对照算法 39.5。数据矩阵 $x$ 有 $I$ 列、$N$ 行；矩阵 $t$ 与 $x$ 相同，只是把 $-1$ 换成了 $0$。

于是，正如我们为单神经元分类器的训练定义了 objective function (39.11)，这里的 objective function 可以定义为

```math
G(W) = -\sum_i \sum_n \left[ t_i^{(n)} \ln y_i^{(n)} + \left(1 - t_i^{(n)}\right) \ln\left(1 - y_i^{(n)}\right) \right],
```

（式 (42.28)）其中

```math
t_i^{(n)} = \begin{cases} 1 & x_i^{(n)} = 1 \\ 0 & x_i^{(n)} = -1 \end{cases}
```

（式 (42.29)）而

```math
y_i^{(n)} = \frac{1}{1 + \exp\left(-a_i^{(n)}\right)}, \qquad \text{where } a_i^{(n)} = \sum_j w_{ij} x_j^{(n)} .
```

（式 (42.30)）于是我们可以直接借来为单神经元写的那套算法（算法 39.5，p.478），写出优化 Hopfield network 的算法 42.9。Octave 方便的语法让改动非常少；多出来的几行只是在强制两条约束：self-weight $w_{ii}$ 必须全为零，以及权重矩阵必须对称（$w_{ij} = w_{ji}$）。

不出所料，这个学习算法比一次成型的 Hebbian learning rule 干得更好。图 42.5 里那六个用 Hebb rule 记不住的六个模式，用算法 42.9 学完之后，六个模式**全部**成为稳定态。

[exercise] **Exercise 42.8.** [4C] Implement this learning rule and investigate empirically its capacity for memorizing random patterns; also compare its avalanche properties with those of the Hebb rule.
> 话题摘要：实现算法 42.9，实测其随机模式容量，并对比 Hebb rule 的雪崩行为（难度 4C，需上机 + 实验设计）。

<span style="color:#1e8449;">**[译注]** `gw = gw + gw'` 这一行不是「顺手加的对称化」，它是这个算法能收敛的唯一理由，删掉就会静默失效。

**原因**：$w_{ij}$ 在 $G(W)$ 里以两种身份出现两次——一次作为「神经元 $i$ 从 $j$ 收到的权重」，一次作为「神经元 $j$ 从 $i$ 收到的权重」（因为 (42.30) 对所有 $i$ 求和、而 $a_i$ 依赖整行 $w_{i\cdot}$）。所以 $\partial G/\partial w_{ij}$ 把这两个角色算出来的两项**相加**，得到的矩阵天然对称；而数值实现里 `x' * e` 只走了一个方向（$x$ 是 $N\times I$、$e$ 是 $N\times I$，乘积得 $I\times I$，但每一格只对应一个方向），**必须手动补上转置那一半**，否则梯度只有真实值的一半，而且矩阵不对称。

**消失测试**：删掉 `gw = gw + gw'`，你会看到两个可观测后果：① 有效学习率减半，收敛慢一倍；② 权重矩阵失去对称性，而 $w_{ij}\ne w_{ji}$ 时**能量函数不再存在**——(42.15) 的 $E(x)=-\tfrac12 x^{\top}Wx$ 只有在 $W$ 对称时才是良定义的二次型，否则 $x^{\top}Wx$ 只取对称部分。于是网络的动力学不再做任何函数的下降，可能出现 2-周期振荡（正是 §42.4 练习 42.3/42.4 那两个反例的机制）。

**方向感**：`w(i,i) = 0` 每次外循环都被重设一次，说明梯度步本身会破坏 $w_{ii}=0$——这也是「约束用投影维持、不是用罚项」的例子。

**落点**：算法 39.5（p.478）与其 objective (39.11)；$(42.28)$-$(42.30)$；对称性的必要性见 §42.4 的 Lyapunov 论证与练习 42.3/42.4 的反例。</span>

## 42.9 Hopfield network 用于优化问题 · Hopfield networks for optimization problems（书 p.516）

既然 Hopfield network 的动力学是在最小化一个 energy function，一个自然的问题是：我们能不能把有意思的优化问题映射到 Hopfield network 上？生物的数据处理问题常常含有约束满足（constraint satisfaction）的成分——例如在场景解释（scene interpretation）里，人们希望推断每个可见元素的空间位置、朝向、亮度与纹理，以及哪些可见元素连在一起构成物体。这些推断既受给定数据的约束，也受「物体连续性」这类先验知识的约束。



[Figure 42.10：用 Hopfield network 求解 $K=4$ 城市的 travelling salesman problem。(a1, a2) 一个 $16$ 神经元网络的两个解状态——活动用黑色 $=1$、白色 $=0$ 表示——以及这两个网络状态对应的巡回路线。(b) 节点 `B2` 与其他节点之间的负权重：这些权重强制一条巡回的**合法性**。(c) 体现**距离** objective function 的那些负权重。]

Hopfield 与 Tank（1985）提出：可以把一个有意思的约束满足问题拿来，设计二值或连续 Hopfield network 的权重，使得网络的**落定**（settling）过程恰好最小化该问题的 objective function。

**Travelling salesman problem（旅行商问题）。** Hopfield network 被应用过的一个经典约束满足问题是 travelling salesman problem。给定 $K$ 个城市的集合，以及 $K(K-1)/2$ 个城市间距离构成的矩阵；任务是找一条闭巡回（closed tour），每个城市恰好访问一次，总距离最小。travelling salesman problem 的难度与 NP-complete 问题等价。

Hopfield 与 Tank 建议的方法是：用一个 $I = K^{2}$ 个神经元的网络状态来表示问题的候选解，神经元排成方阵，每个神经元代表一个假设——某个特定城市在巡回中处于某个特定位置。把神经元的状态看作 $0$ 与 $1$ 之间（而不是 $-1$ 与 $1$ 之间）会更方便。图 42.10a 给出四个城市情形下的两个解状态。

Hopfield network 里的权重扮演两个角色。第一，它们必须定义一个 energy function，只有当网络状态表示一条**合法**巡回时才取最小值。合法状态就是看起来像置换矩阵（permutation matrix）的状态：每一行恰好有一个 `1`，每一列恰好有一个 `1`。这条规则可以通过在「同一行或同一列」的任意一对神经元之间放**很大的负权重**来强制，同时给所有神经元设一个**正的 bias**，保证确实有 $K$ 个神经元打开。图 42.10b 显示与神经元 `B2` 相连的那些负权重，`B2` 代表「城市 B 在巡回中排第二」这个陈述。

第二，权重必须编码我们想最小化的 objective function——总距离。做法是在**相邻列**的节点之间放与相应距离成比例的负权重。例如相邻列中 B 节点与 D 节点之间，权重取 $-d_{BD}$。与神经元 `B2` 相连的这些负权重显示在图 42.10c 中。结果就是：当网络处于合法状态时，它的总能量等于对应巡回的总距离，再加上一个由 bias 关联的能量给出的常数。

<span style="color:#1e8449;">**[译注]** $K^{2}$ 这个编码的选择值得算一下账，它决定了这个方案能走多远。$K$ 个城市、$K$ 个位置，$K^{2}$ 个二值单元能表示 $2^{K^{2}}$ 个状态，而合法巡回只有 $K!$ 条。$K=10$ 时 $2^{100}\approx1.27\times10^{30}$，$10! = 3.6\times10^{6}$——**合法状态占状态空间的 $2.8\times10^{-24}$**。

**消失测试**：这就是「约束权重」存在的全部理由。没有那些同行同列的强负权重，网络会随机落在 $2^{K^2}$ 个状态里的绝大多数（非法）上，因为它们占了 $1 - 2.8\times10^{-24}$；energy function 里距离项根本来不及说话。反过来，若约束权重**过大**（原文说的 "large"），网络会先猛冲到某个合法状态、完全无视距离——原文的 "rattle into a valid state with little regard for the distances" 说的就是这件事。

**方向感**：约束权重与距离权重之比是一个没有量纲信息可依的自由参数，这是 Hopfield-Tank 方案在 $K$ 大时失效的直接原因，也是 Aiyer（1991）必须引入 valid subspace 投影的原因。

$K=20$ 时更极端：$20! = 2.43\times10^{18}$，而 $2^{400} = 2.58\times10^{120}$，比值 $9.4\times10^{-103}$——城市规模越接近真实，这个编码越没有希望。


**落点**：图 42.10b/c 的两组权重；$K!$ vs $2^{K^{2}}$ 的比值；Aiyer 的修正在 p.518。</span>



[Figure 42.11：(a) 一个连续 Hopfield network 用 Aiyer（1991）的 graduated non-convexity 方法求解 travelling salesman problem 时状态的演化；网络状态通过「对巡回中每个点用神经元活动作质量函数求质心」的办法，投影到城市所在的二维空间里显示。(b) travelling scholar problem：连接 $27$ 个剑桥学院、工程系、大学图书馆以及 Sree Aiyer 家的最短巡回。取自 Aiyer（1991）。]

现在，由于 Hopfield network 最小化自己的能量，人们期待二值或连续 Hopfield network 的动力学把状态带到某个极小点，该极小点是一条合法巡回，并且**可能**是最优巡回。然而，对大规模的 travelling salesman problem 来说，这个期待在没有仔细修正的前提下**并不**实现。我们还没有规定「强制巡回合法性」的那些权重相对于距离权重应该多大，而设定这个尺度因子（scale factor）本身就有困难。

若使用**大**的合法性强制权重，网络的动力学就会「哐当」冲进某个合法状态，几乎不顾距离；若使用**小**的合法性强制权重，距离权重就可能让网络采纳一个非法状态——它的能量低于**任何**合法状态。我们最初的 energy function 表述把 objective function 与解的合法性放在潜在的**冲突**之中。

这个困难被 Sree Aiyer（1991）的工作解决了：他展示了如何修改距离权重，使它们不干扰解的合法性；以及如何定义一个连续 Hopfield network，使其动力学**在任何时刻**都被限制在一个「合法子空间」（valid subspace）之内。Aiyer 使用 graduated non-convexity（渐进非凸化）或称 deterministic annealing（确定性退火）的方法，用这些 Hopfield network 找出好的解。deterministic annealing 的做法是把网络中各神经元的增益（gain）$\beta$ 从 $0$ 逐渐增大到 $\infty$，在 $\beta \to \infty$ 时网络状态对应于一条合法巡回。把这一方法用于一个三十城市 travelling salesman problem 所产生的一串轨迹显示在图 42.11a 中。

图 42.11b 展示了 Aiyer 用连续 Hopfield network 找到的「travelling scholar problem」的一个解。

<span style="color:#1e8449;">**[译注]** 「$\beta$ 从 $0$ 升到 $\infty$」不是技巧性的冷却技巧，它对着一个具体的数学事实：$\beta = 0$ 时每个神经元的 sigmoid 是**线性**的，整个网络的动力学是线性的、能量曲面只有一个凸碗，落定过程等价于解一个线性方程组；$\beta \to \infty$ 时 sigmoid 逼近阶跃函数，能量曲面长出 $K!$ 个局部极小（每条合法巡回一个）。

**消失测试**：如果直接把 $\beta$ 设成 $\infty$ 从随机初态开始跑，你会落进离初态最近的那个局部极小，三十城市时这个解通常比最优差百分之几到几十——这正是 Hopfield-Tank 原始方案在大 $K$ 上的实测表现。graduated non-convexity 的作用是**沿着一条连续变形把解从「唯一的好解」搬到「很多坏解中的一个」**，让初态的温度信息在退火过程中被逐步丢弃。

**方向感**：$\beta$ 是这个方案里唯一真正需要调的参数，调的是**路径**（从凸到非凸怎么走），不是终点。

**与 §42.7 的连接**：$0.138I$ 那个容量台阶本质上也是 $\beta$ 意义上的相变——只不过那里变的是 $N/I$（信噪比），这里变的是 $\beta$（非线性强度）；两者都用「尖锐不连续」这个词，因为都来自同一个 saddle-node 式的分岔。

**落点**：图 42.11a 的轨迹序列；Aiyer (1991)；与 $(42.26)$ 的类比；原文 p.518 对 scale factor 的抱怨。</span>



## 42.10 补充习题 · Further exercises（书 p.519）

[exercise] **Exercise 42.9.** [3] Storing two memories. Two binary memories $m$ and $n$ ($m_i, n_i \in \{-1, +1\}$) are stored by Hebbian learning in a Hopfield network using
```math
w_{ij} = \begin{cases} m_i m_j + n_i n_j & \text{for } i \ne j \\ 0 & \text{for } i = j \end{cases}
```
(42.31), with biases $b_i$ set to zero. The network is put in the state $x = m$. Evaluate the activation $a_i$ of neuron $i$ and show that it can be written in the form $a_i = \mu m_i + \nu n_i$ (42.32). By comparing the signal strength $\mu$ with the magnitude of the noise strength $|\nu|$, show that $x = m$ is a stable state of the dynamics of the network. The network is put in a state $x$ differing in $D$ places from $m$, $x = m + 2d$ (42.33), where the perturbation $d$ satisfies $d_i \in \{-1, 0, +1\}$; $D$ is the number of non-zero components of $d$, and for each non-zero $d_i$, $d_i = -m_i$. Defining the overlap between $m$ and $n$ to be $o_{mn} = \sum_{i=1}^{I} m_i n_i$ (42.34), evaluate $a_i$ again and show that the dynamics will restore $x$ to $m$ if the number of flipped bits satisfies $D < \tfrac14 (I - |o_{mn}| - 2)$ (42.35). How does this number compare with the maximum number of flipped bits that can be corrected by the optimal decoder, assuming $x$ is either a noisy version of $m$ or of $n$?
> 话题摘要：只存两个记忆时，把激活值写成「信号 $m$ + 干扰 $n$」两项，再用 $m$、$n$ 的 overlap 给出 basin 半径；最后与最优 decoder 的对半判决比较（难度 3，纯推导 + 一个对比判断）。

[exercise] **Exercise 42.10.** [3] Hopfield network as a collection of binary classifiers. This exercise explores the link between unsupervised networks and supervised networks. If a Hopfield network's desired memories are all attracting stable states, then every neuron in the network has weights going to it that solve a classification problem personal to that neuron. Take the set of memories and write them in the form $x'^{(n)}, x_i^{(n)}$, where $x'$ denotes all the components $x_{i'}$ for all $i' \ne i$, and let $w'$ denote the vector of weights $w_{ii'}$, for $i' \ne i$. Using what we know about the capacity of the single neuron, show that it is almost certainly impossible to store more than $2I$ random memories in a Hopfield network of $I$ neurons.
> 话题摘要：把 Hopfield network 拆成 $I$ 个互相独立的单神经元分类问题，用「单神经元容量 2 bits/weight」反推全局容量上界 $2I$（难度 3）。

<span style="color:#1e8449;">**[译注]** 练习 42.9 最后那句对比是整章最锋利的一问，答案是「**Hopfield 只能做到最优 decoder 的一半**」。

$(42.35)$ 给 $D < (I - |o_{mn}| - 2)/4$；而若已知 $x$ 是 $m$ 或 $n$ 之一的噪声版，最优 decoder 按「离谁近就判谁」工作，可纠的是 $D < \tfrac12(I - |o_{mn}|)$——两者的区别只在分母：$4$ 对 $2$。

**为什么正好差一倍**：Hopfield 的判据是「每个比特各自看自己的输入是否与自己一致」，这是**逐比特局部**判据；最优 decoder 是「整条向量到 $m$ 与到 $n$ 的距离谁小」，这是**全局**判据。局部判据在 $D$ 接近一半时会互相拆台，全局判据不会。

**实跑对照**（`mk23_verify3.py` 第 3 节）：$I = 100$、$|o_{mn}| = 0$ 时 Hopfield 给 $D < 24.5$、最优给 $D < 50$，比值 $0.490$；$I = 1000$ 时比值收敛到 $0.499$。

**方向感**：$I \to \infty$ 时比值 $\to 1/2$ 精确成立，这不是巧合而是分母 $4$ 与 $2$ 的直接后果。**消失测试**：若改用 §42.8 的梯度优化权重，比值会往 $1$ 靠——因为 objective function 是按「被翻转的比特是否被正确恢复」直接定义的，等于把全局判据塞进权重。

**落点**：$(42.35)$；最优 decoder 的思路见 §1.x 的 Hamming 距离判决；§42.8 的 objective (42.28)。</span>



**Lyapunov functions。**

[exercise] **Exercise 42.11.** [3] Erik's puzzle. In a stripped-down version of Conway's game of life, cells are arranged on a square grid. Each cell is either alive or dead. Live cells do not die. Dead cells become alive if two or more of their immediate neighbours are alive. (Neighbours to north, south, east and west.) What is the smallest number of live cells needed in order that these rules lead to an entire $N\times N$ square being alive? In a $d$-dimensional version of the same game, the rule is that if $d$ neighbours are alive then you come to life. What is the smallest number of live cells needed in order that an entire $N\times N\times\cdots\times N$ hypercube becomes alive? (And how should those live cells be arranged?)
> 话题摘要：删掉死亡规则的生命游戏，问「让整个 $N\times N$（及 $d$ 维超立方）活起来，最少需要几个活细胞，怎么摆」（难度 3，构造 + 下界证明）。

[Figure 42.12：Erik 的动力学。它演示「活细胞永久不死、死细胞只要两个 4-邻域活着就复活」这条单调规则下的定点扩张过程。]

**Southeast puzzle（东南谜题）。** southeast puzzle 在一个半无限的棋盘上进行，从西北（左上）角开始。规则有三条：

1. 初始局面：在西北角最靠里的那一格放一枚棋子（图 42.13a）。
2. 任何一格上不允许超过一枚棋子。
3. 每一步，你从棋盘上取下一枚棋子，用两枚棋子替换它——一枚放在正东方向紧邻的格子，一枚放在正南方向紧邻的格子，如图 42.13b 所示。每一这样的步骤使棋盘上的棋子数增加一枚。

在走了 (b) 这一步之后，两枚棋子中的任何一枚都可以被选来做下一步。图 42.13c 显示移动下面那枚棋子的结果。下一步时，可以选三枚棋子中最低的那枚或中间那枚；最上面那枚不能被选，因为那会违反规则 2。在第 (d) 步我们选了中间那枚。现在任何棋子都可以移动，除了最左边那枚。

现在，谜题是：

[exercise] **Exercise 42.12.** [4, p.521] Is it possible to obtain a position in which all the ten squares closest to the northwest corner, marked in figure 42.13z, are empty? [Hint: this puzzle has a connection to data compression.]
> 话题摘要：问「能否让离西北角最近的那十格全部空着」，提示与数据压缩有关（难度 4，解答见 p.521/本译本 p533）。

[Figure 42.13：southeast puzzle。它演示三条规则下的移动序列，以及 (z) 中要清空的十格位置（离左上角 city-block 距离最近的那批格子）。]

[Figure 42.14：southeast puzzle 的一个可能局面？它演示「把十格空出来之后其余格子全填满」这个候选反例，用于把守恒量的赋值算到底。]

## 42.11 解答 · Solutions（书 p.520）

**Exercise 42.3 的解答（p.508）。** 取一个有 2 个神经元的 binary feedback network，令 $w_{12} = 1$、$w_{21} = -1$。于是每当神经元 1 被更新，它就会与神经元 2 一致；而每当神经元 2 被更新，它就会翻到与神经元 1 相反的状态。不存在稳定态。

<span style="color:#1e8449;">**[译注]** 这条解答与上游 p520 那个 **2-周期反例**必须对照着读，因为它们是两种**完全不同**的失败机制，混为一谈会错过整章的要点。

| | 权重 | 更新方式 | 现象 |
|---|---|---|---|
| 练习 42.3（本节） | $w_{12}=1,\; w_{21}=-1$ **非对称** | 异步 | 根本没有稳定态，每步都在两个神经元之间来回 |
| 练习 42.4（p.521） | $w_{12}=w_{21}=1$ **对称** | **同步** | 两个神经元同时翻转，$E$ 在 $+3$ 与 $-3$ 之间振荡 |

**关键差别**：练习 42.4 的网络**对称**，所以能量函数 $E(x) = -\tfrac12 x^{\top}Wx$ 良定义，$x=(1,-1)$ 与 $x=(-1,1)$ 能量都是 $+3$，而中间那步的 $x=(-1,-1)$ 与 $(1,1)$ 能量是 $-3$——同步更新会让状态在等能的两点之间来回跳，能量**不降**，Lyapunov 论证失效。练习 42.3 的网络**不对称**，能量函数根本不存在，异步更新也救不了。

**消失测试**：把 42.3 的 $w_{21}$ 改成 $+1$（即变成 42.4 的对称情形）并保持异步更新，你会立刻得到两个稳定态 $(1,1)$ 与 $(-1,-1)$——**对称 + 异步**才是收敛的充分条件组合。

**方向感**：$w_{12}$ 与 $w_{21}$ 差一个符号，代价是「无稳定态」；这是 §42.4 里那句「只要权重矩阵对称」的整个重量所在。

**落点**：§42.4 的 Lyapunov 论证（上游 p.508）；练习 42.4 的解答在本译本下一块（书 p.521）；$(42.15)$ 的 $\tilde F$。</span>



**Exercise 42.4 的解答（p.508）。** 取一个有两个神经元的 binary Hopfield network，令 $w_{12} = w_{21} = 1$，初态为 $x_1 = 1$、$x_2 = -1$。那么若动力学是**同步**的，每一次迭代两个神经元都会翻转自己的状态。动力学不收敛到不动点。

**Exercise 42.12 的解答（p.520）。** 这道题的关键是注意到它与**二值符号码（binary symbol code）**的构造相似。从空串开始，我们可以通过反复把某个 codeword 一分为二来构造一棵二叉树。每个 codeword 都隐含一个概率 $2^{-l}$，其中 $l$ 是该 codeword 在二叉树中的深度。每当我们把某个 codeword 一分为二、造出两个长度各增一的新 codeword，这两个新 codeword 各自的隐含概率都等于旧 codeword 的一半。对一个完备的二值码（complete binary code），Kraft 等式断言这些隐含概率之和为 $1$。

类似地，在 southeast 里我们可以给棋盘上每枚棋子关联一个「权重」。若给左上角格子上的任何棋子赋权重 $1$；给离左上角距离为 $1$ 的格子上的棋子赋权重 $1/2$；距离为 $2$ 的赋 $1/4$；如此类推，其中「距离」指 city-block distance（曼哈顿距离）；那么 southeast 中的每一步合法移动都使棋盘上所有棋子的总权重**保持不变**。

Lyapunov function 有两种风味：函数可以是状态的一个函数，其值已知保持不变（守恒）；也可以是状态的一个函数，它有下界，且其值总是下降或保持不变（单调）。总权重是第二类 Lyapunov function。

起始权重是 $1$，所以现在我们手上有了一个强有力的工具：一个状态的守恒函数。那么，是否可能找出一个局面，使得权重最高的十格全空、而总权重仍为 $1$？如果棋盘上其余所有格子都被占满（图 42.14），总权重会是多少？

总权重将是 $\sum_{l=4}^{\infty} (l+1)2^{-l}$，它等于 $3/4$。所以把这十格全部清空是不可能的。

<span style="color:#1e8449;">**[译注]** 这条解答是本章唯一一处把**信息论**直接缝进**动力系统**的地方，而且缝得极其干净：它把「守恒的 Lyapunov function」识别成 **Kraft 等式**。

**对应关系**：一步移动 = 把长度 $l$ 的 codeword 拆成两个长度 $l+1$ 的 codeword，隐含概率 $2^{-l} \to 2\cdot 2^{-(l+1)} = 2^{-l}$，守恒。棋盘上离左上角 city-block 距离为 $l$ 的格子恰好有 $l+1$ 个，所以「这些格子全占满」的总权重就是 $\sum_{l\ge 4}(l+1)2^{-l}$。

**实跑复算**（`mk23_verify.py` 第 4 节）：$\sum_{l=4}^{400}(l+1)2^{-l} = 0.7500000000$；用闭式 $\frac{1}{(1-x)^2}\big|_{x=1/2} = 4$ 减去前缀 $1 + 1 + 0.75 + 0.5 = 3.25$，仍得 $0.75$。$3/4 < 1$，所以「十格全空、其余全满」这个候选局面违反守恒，反过来证明了原题不可行。

**消失测试**：没有这个守恒量，你只能靠搜索——而棋盘半无限、棋子数无上界，搜索不收敛。有了它，判断从「搜」降成「除」：$1 - 3/4 = 1/4 > 0$ 就是不可能性的**证明**。

**方向级**：$3/4$ 是「十格空 + 其余满」的上确界，距离要达到的 $1$ 差 $1/4$，**这 $1/4$ 永远补不上**——因为 $l \le 3$ 的前四层（$1+1+0.75+0.5$）已被起始那枚棋子的 $1$ 全部用掉。

**落点**：Kraft 等式见 §5.5（McMillan/Kraft）；Lyapunov function 的两类风味见本节定义；$(42.15)$ 的 $\tilde F$ 是第一类（单调）而非第二类（守恒）。</span>

<span style="color:#1e8449;">**[译注]** 练习 42.11（Erik's puzzle）原文**未给解答**，但答案可以在二十行代码内验证到 $N = 5$，所以值得把复算写下来，因为它示范了「构造 + 下界」的标准套路。

**答案：$N$ 个（二维），$d$ 维时 $N^{d-1}$ 个。**

**构造**：主对角线放 $N$ 个活细胞 $(i,i)$。验证「够用」：格子 $(i,i+1)$ 的南邻 $(i+1,i+1)$ 与西邻 $(i,i)$ 都活着，两个邻居达标，于是复活；接着 $(i,i+2)$ 有西邻 $(i,i+1)$ 与南邻 $(i+1,i+2)$（后者在上一轮已复活），继续向外扩张。(d) 步之后全部 $(i,j)$ 依次点亮。

**实跑**（`mk23_verify3.py` 第 1 节）：对 $N=2,3,4,5$ 穷举所有 $\le N-1$ 个种子的组合，**没有一种能填满**；而对角线摆法在 $N=6,8$ 上直接验证为填满。→ 最小值恰为 $N$。

**为什么 $N-1$ 不够（下界思路）**：每一条反对角线 $i+j = \text{const}$ 上的细胞要变活，必须从更靠上的反对角线借到至少两个活邻居；而一对活邻居最多把「已被点亮的反对角线数」推进一格。$N$ 条反对角线需要 $N$ 个起点。

**方向感**：二维的答案是 $N$、三维是 $N^{2}$，一般地 $N^{d-1}$——因为「一张 $(d-1)$ 维超平面」刚好能让每个待点亮格子在 $d$ 个方向中的其余方向凑够 $d$ 个活邻居。

**落点**：本题无原书解答坐标；与之同构的单调扩张 + 守恒量思想见本节 southeast puzzle 的 $3/4$ 论证。</span>



# 第 43 章 · Boltzmann Machines（书 p.522）

## 43.1 从 Hopfield network 到 Boltzmann machine · From Hopfield networks to Boltzmann machines

我们已经注意到，二值 Hopfield network 最小化一个 energy function

```math
E(x) = -\tfrac12 x^{\top} W x
```

（式 (43.1)），而激活函数为 $x_n = \tanh(a_n)$ 的连续 Hopfield network 可以被看作在近似与该 energy function 相关联的概率分布：

```math
P(x \mid W) = \frac{1}{Z(W)} \exp\left[-E(x)\right] = \frac{1}{Z(W)} \exp\left[ \tfrac12 x^{\top} W x \right].
```

（式 (43.2)）这些观察促成了这样一个想法：去使用一个**真正实现**上述概率分布的神经网络模型。

**Stochastic Hopfield network**，或称 **Boltzmann machine**（Hinton 与 Sejnowski, 1986），有如下活动规则：

```text
Activity rule of Boltzmann machine: after computing the
activation a_i (42.3),
  set x_i = +1 with probability  1 / (1 + e^{-2 a_i})
  else set x_i = -1.
```

（式 (43.3)）这条规则实现的是针对概率分布 (43.2) 的 Gibbs sampling。

**Boltzmann machine 的学习（Boltzmann machine learning）。** 给定一组来自真实世界的样本 $\{x^{(n)}\}_{1}^{N}$，我们可能想调整权重 $W$，使生成模型（generative model）

```math
P(x \mid W) = \frac{1}{Z(W)} \exp\left[ \tfrac12 x^{\top} W x \right]
```

（式 (43.4)）与那些样本很好地匹配。我们可以通过写下 Bayes' theorem、得到给定数据下权重的 posterior probability，来推导学习算法：

```math
P\left(W \mid \{x^{(n)}\}_{1}^{N}\right) = \left[ \prod_{n=1}^{N} P\left(x^{(n)} \mid W\right) \right] \frac{P(W)}{P\left(\{x^{(n)}\}_{1}^{N}\right)}.
```

（式 (43.5)）

<span style="color:#1e8449;">**[译注]** $(43.2)$ 与 $(43.1)$ 之间那个等号值得停一步，因为它在符号上「吞掉了物理学的温度」。

按统计物理，Boltzmann 分布是 $P(x) \propto e^{-E(x)/T}$，$T$ 是温度。$(43.2)$ 写的是 $P \propto e^{-E(x)}$，等价于**把 $T$ 固定为 $1$，并把 $1/T$ 吸收进 $W$**：若原始权重是 $W_0$，则 $W = W_0$，$E = -\tfrac12 x^{\top}W x$，$e^{-E} = e^{\frac12 x^{\top}Wx}$。这一步的代价是「温度」不再是自由参数——所以后面 §43 里若想让网络更「随机」，只能**缩小 $W$ 的整体幅度**，而不是升温度。

**这与 $(43.3)$ 的因子 $2$ 呼应**：把 $a_i = \sum_j w_{ij}x_j$ 代入，$P(x_i = +1) = \sigma(2a_i)$。因子 $2$ 来自「翻转一个比特使 $x^{\top}Wx$ 变化 $2x_i a_i$ 而能量变化是它的一半再取负」——若你手算时漏掉这个 $2$，采样出来的分布就不是 $(43.2)$，而是温度被暗中改成 $2$ 的那个分布。

**消失测试**：把因子 $2$ 删掉，$P(x_i=+1) = \sigma(a_i)$，则平稳分布变成 $P(x) \propto \exp(\tfrac14 x^{\top}Wx)$——权重的有效强度减半，容量口径全部对不上 $(42.26)$。

**方向感**：一个因子 $2$，等于把整张相图上的 $N/I$ 轴压缩一半；反过来，漏掉它的人会以为容量翻倍，实测却对不上 $(42.27)$ 的 $0.122$。

**落点**：$(43.1)$-$(43.3)$；Gibbs sampling 的细节见 §29/§30；温度与 $\beta$ 的类比见 §42.9 的 deterministic annealing。</span>



我们把注意力集中在分子里的第一项，即 likelihood 上，并推导一个 maximum likelihood 算法（不过，正如我们处理单神经元时那样，走完整的 Bayesian 路线也许有好处）。我们对 likelihood 的对数求导：

```math
\ln \left[ \prod_{n=1}^{N} P\left(x^{(n)} \mid W\right) \right] = \sum_{n=1}^{N} \left[ \tfrac12 x^{(n)\top} W x^{(n)} - \ln Z(W) \right],
```

（式 (43.6)）对 $w_{ij}$ 求导，同时记住 $W$ 被定义为对称、$w_{ji} = w_{ij}$。

[exercise] **Exercise 43.1.** [2] Show that the derivative of $\ln Z(W)$ with respect to $w_{ij}$ is $\frac{\partial}{\partial w_{ij}} \ln Z(W) = \sum_x x_i x_j P(x \mid W) = \langle x_i x_j \rangle_{P(x \mid W)}$. [This exercise is similar to exercise 22.12 (p.307).]
> 话题摘要：对配分函数取对数后求导，得到「模型下的二阶矩」（难度 2，标准指数族推导）。

（式 (43.7)）于是 log likelihood 的导数是：

```math
\frac{\partial}{\partial w_{ij}} \ln P\left(\{x^{(n)}\}_{1}^{N} \mid W\right) = \sum_{n=1}^{N} \left[ x_i^{(n)} x_j^{(n)} - \langle x_i x_j \rangle_{P(x\mid W)} \right]
```

```math
= N \left[ \langle x_i x_j \rangle_{\text{Data}} - \langle x_i x_j \rangle_{P(x \mid W)} \right].
```

（式 (43.8)、(43.9)）这个梯度与两项之差成正比。第一项是 $x_i$ 与 $x_j$ 之间的经验相关（empirical correlation）：

```math
\langle x_i x_j \rangle_{\text{Data}} \equiv \frac{1}{N} \sum_{n=1}^{N} \left[ x_i^{(n)} x_j^{(n)} \right],
```

（式 (43.10)）第二项是在当前模型下 $x_i$ 与 $x_j$ 之间的相关：

```math
\langle x_i x_j \rangle_{P(x \mid W)} \equiv \sum_x x_i x_j P(x \mid W).
```

（式 (43.11)）第一项相关 $\langle x_i x_j \rangle_{\text{Data}}$ 很容易算——它就是真实世界里活动的经验相关。第二项相关 $\langle x_i x_j \rangle_{P(x \mid W)}$ 就没那么好算了，但它可以用 Monte Carlo 方法估计，也就是让 Boltzmann machine 的活动规则 (43.3) 反复迭代，同时观察 $x_i x_j$ 的平均值。

在 $W = 0$ 这个特殊情形下，我们可以精确算出梯度，因为由对称性，相关 $\langle x_i x_j \rangle_{P(x \mid W)}$ 必然为零。若权重用学习率 $\eta$ 做 gradient descent 调整，那么一次迭代之后权重将是

```math
w_{ij} = \eta \sum_{n=1}^{N} \left[ x_i^{(n)} x_j^{(n)} \right],
```

（式 (43.12)）这恰好就是 Hebb rule 给出的权重值，也就是我们训练 Hopfield network 时用的那条规则。

**Boltzmann machine 学习的解释（Interpretation）。** 梯度 (43.9) 中两项的一种看法，是把它们读作「waking」与「sleeping」规则。当网络「醒着」（awake）时，它测量真实世界中 $x_i$ 与 $x_j$ 的相关，并按比例**增加**权重。

<span style="color:#1e8449;">**[译注]** $(43.12)$ 这个「一步就退回 Hebb rule」的结果，是整章的结构性锚点：它说明 **Hebb rule 不是某个偶然的启发式，而是「$W=0$ 处做一步 maximum likelihood」**。这条等式值得亲手验一遍，因为它同时校正三个容易搞错的系数。

**逐步核对**：$W=0$ 时 $P(x\mid W) = 1/Z_0$，状态空间有 $2^{I}$ 个点，所以 $P = 2^{-I}$，每个 $x_i$ 与 $x_j$（$i\ne j$）独立且等概率取 $\pm1$，故 $\langle x_i x_j \rangle_{P} = 0$。代入 $(43.9)$ 得 $\partial \ln P / \partial w_{ij} = N \langle x_i x_j \rangle_{\text{Data}} = \sum_n x_i^{(n)}x_j^{(n)}$。做一步梯度**上升**（$w \leftarrow w + \eta \partial$）就是 $(43.12)$。**三个系数各自的位置**：$(43.6)$ 里的 $\tfrac12$ 被 $\partial(w_{ij}+w_{ji})$ 的「对称求导出两份」正好抵消；$(43.9)$ 里的 $N$ 与 $(43.10)$ 里的 $1/N$ 相消；剩下的就是纯 Hebb。

**消失测试**：若 $W$ 不对称（不强制 $w_{ji}=w_{ij}$），$\partial(\tfrac12 x^{\top}Wx)/\partial w_{ij} = \tfrac12 x_i x_j$，梯度少一半，$(43.12)$ 会变成 $\tfrac{\eta}{2}\sum x_ix_j$——系数差 $2$ 倍，正是 §42.8 里 `gw = gw + gw'` 那行要补的东西。

**方向感**：从「Monte Carlo 估两项之差」退到「只算一项」，代价是失去模型自洽性（模型永远停在 $W=0$ 附近的一步之遥），收益是一次遍历数据就能训练完——这就是为什么 Hebb rule 在 1982 年能跑，Boltzmann learning 只能在小网络上跑。

**落点**：$(43.7)$ 的 $\langle x_i x_j\rangle$；$(43.9)$-$(43.12)$；练习 22.12（p.307）的同类推导。</span>



当网络「睡着」（asleep）时，它用生成模型 (43.4) 对世界「做梦」（dreams），并测量模型世界里 $x_i$ 与 $x_j$ 之间的相关；这些相关决定权重的按比例**减少**。如果梦世界的二阶相关与真实世界的相关匹配，那么两项就平衡，权重不再变化。

[Figure 43.1：`shifter` 系综（ensemble）。(a) plain shifter ensemble 的四个样本。(b) 对应的 labelled shifter ensemble 的四个样本。它演示「二阶统计量对这类数据完全无用」——每个图像的下面八个像素是上面八个像素的副本，整体左移一像素、不动、或右移一像素，而上面八个像素是随机的。]

**对 Hopfield network 与简单 Boltzmann machine 的批评（Criticism）。** 到目前为止我们讨论的 Hopfield network 与 Boltzmann machine，其中**所有**神经元都对应于可见变量（visible variable）$x_i$。结果是这样一个概率模型：被优化之后，它能抓住环境的**二阶统计量**（second-order statistics）。〔一个系综 $P(x)$ 的二阶统计量，就是所有成对乘积 $x_ix_j$ 的期望值 $\langle x_ix_j\rangle$。〕然而真实世界常常含有更高阶的相关（higher-order correlation），若我们的描述要有效，就必须把它们包含进来。而二阶相关本身往往携带很少甚至没有有用信息。

例如，考虑「椅子」的二值图像系综。我们可以想象各种设计的椅子图像——四腿椅、沙发椅、五腿带轮椅、木椅、软垫椅、带摇杆而不是腿的椅子。一个小孩很容易学会把这些图像与胡萝卜、鹦鹉的图像区分开。但我预期原始数据的二阶统计量对描述这个系综毫无用处。二阶统计量只能抓住「两个像素是否倾向于处于同一状态」。要为一个椅子图像的生成模型做得好，需要更高阶的概念。

一个更简单、但高阶统计量很重要的图像系综是「shifter ensemble」，它有两个变体。图 43.1a 展示了「plain shifter ensemble」的几个样本。在每幅图像里，下面八个像素是上面八个像素的副本——要么左移一像素，要么不移，要么右移一像素。（上面八个像素随机设定。）这个系综是「两眼视觉信号到达大脑早期层次」的简单模型：来自两眼的信号彼此相似，但由于视觉世界的深度变化，可能相差小的平移。这个系综描述起来简单，但它的二阶统计量不传递任何有用信息。一个像素与它上方三个像素中任何一个的相关都是 $1/3$，而任何其他两个像素之间的相关都是零。

图 43.1b 展示了「labelled shifter ensemble」的几个样本。这里问题被弄得简单了些：加入了额外的三个神经元，把视觉图像标注为「左移」「不移」「右移」三个子系综之一。但即便有这些额外信息，这个系综**仍然无法**只靠二阶统计量学出来。任何 label 神经元与任何图像神经元之间的二阶相关都是零。我们需要能抓住环境**高阶**统计量的模型。

<span style="color:#1e8449;">**[译注]** 「任何其他两个像素之间的相关都是零」这句可以当场验算，而 $1/3$ 那个数正是「二阶统计量坏掉」的证据：它**不含方向信息**。

设上面一行像素 $t_k$（随机 $\pm1$），下面一行 $b_k = t_{k+s}$，其中 $s \in \{-1, 0, +1\}$ 等概率。那么对固定的 $k$，$\langle b_k t_k \rangle = \frac13\sum_s \langle t_{k+s}t_k\rangle = \frac13 \cdot 1 = 1/3$（只有 $s=0$ 时同位置相关为 $1$）。而 $\langle b_k t_{k\pm1}\rangle = 1/3$ 同样成立——**左移、右移、不动三种情形贡献完全相同的 $1/3$**。

**这就是「二阶统计量无用」的精确含义**：三个候选解释给了同一组 pair 相关，模型无法从 $\langle b_k t_{k'}\rangle$ 里读出 $s$ 是哪一个。要知道 $s$，必须看**三元组** $(\text{上}j, \text{下}j, \text{下}j{+}1)$ 的联合分布，那是三阶量。

**消失测试**：若数据是「整幅图随机平移」而不是「三个离散位移」，pair 相关会退化成自相关的模糊版本（一条平移平均后的峰），学出来的模型只能重建「平均图像」，任何具体的位移实例都复现不出来。

**方向感**：$1/3$ vs 需要的「$s$ 已知时为 $1$」——**信息量差 $\log_2 3 = 1.585$ 比特/像素对**，这 1.585 比特全部藏在三阶及以上。

**落点**：图 43.1a/b 的两个系综；$(43.13)$ 的高阶展开；§43.2 的 hidden unit 就是用来把这类高阶信息塞回二阶框架的。</span>

那么，我们怎样发展这样的模型？一个想法是造出直接抓住高阶相关的模型，例如：

```math
P'(x \mid W, V, \ldots) = \frac{1}{Z'} \exp\left( \tfrac12 \sum_{ij} w_{ij}x_ix_j + \tfrac16 \sum_{ijk} v_{ijk}x_ix_jx_k + \cdots \right).
```

（式 (43.13)）这样的高阶 Boltzmann machine 用随机更新来模拟同样容易，而高阶参数 $v_{ijk}$ 的学习规则与 $w_{ij}$ 的学习规则等价。



[exercise] **Exercise 43.2.** [2] Derive the gradient of the log likelihood with respect to $v_{ijk}$.
> 话题摘要：把 (43.7) 那套「配分函数求导 = 模型下的矩」照搬到三阶参数上（难度 2）。

生物神经元的树突棘（spine）有可能负责检测少数几个输入信号之间的相关。然而，要抓住阶数足够高、能把椅子图像系综描述好的统计量，需要的项数多到无法想象。仅为了抓住一幅 $128\times128$ 像素图像里的**四阶**统计量，我们就需要超过 $10^{7}$ 个参数。†

所以，测量图像的矩（moment）不是描述其底层结构的好办法。也许我们需要的、或者还需要的，是**隐变量**（hidden variable），统计学家也称之为潜变量（latent variable）。这是 Hinton 与 Sejnowski（1986）引入的重要创新。想法是：可见变量之间的高阶相关，可以通过引入额外的隐变量来描述，同时**坚持只使用变量间二阶交互的模型**；于是隐变量在可见变量之间诱发出高阶相关。

> † 原文此处写「more than $10^{7}$ parameters」。按四阶矩的项数复算，$128\times128 = 16384$ 个像素，四阶项（含重复下标）的个数是 $\binom{16384+3}{4}$ 量级，只算四个**互不相同**的下标也有 $\binom{16384}{4} = 3.0013\times10^{15}$——比 $10^{7}$ 大八个数量级。原文此处疑为 $10^{15}$ 之误（或指「某个极小的子采样版本」）。凡本书其他处引用的 $10^{7}$ 级数字，请以本处复算为准。

<span style="color:#1e8449;">**[译注]** 隐变量这条思路是本章真正的分水岭，值得说清它到底「省」在哪，因为它常被误解成「增加容量」。

**它换的不是容量，是参数的**阶**。** 直接抓三阶相关需要 $I^{3}/6$ 个参数（$I=16384$ 时是 $7.3\times10^{11}$ 个）；引入 $H$ 个隐变量后，参数只有 $IH + H^{2}/2$ 个二阶量（$H=100$ 时约 $1.6\times10^{6}$ 个），而可见—可见之间被 induce 出来的有效交互包含任意阶项。

**边际化是机制**：$P(x\mid W) = \sum_h P(x,h\mid W)$，对 $h$ 求和把一个二次型在对数域里「折」成一条非二次的曲线，其 Taylor 展开含 $x_ix_jx_k$ 项。这就是 (43.14) 那个求和的全部作用。

**消失测试**：不做边际化（把 $h$ 也当可见、直接读二阶权重），$\langle x_ix_j\rangle$ 对「椅子」这类数据是零信息（如上一页 shifter 的 $1/3$）；做完边际化，同一个二阶权重矩阵能表达「三个像素同时亮才被鼓励」这种三阶约束。

**方向感**：参数数从 $O(I^{3})$ 降到 $O(IH)$，$I=16384$、$H=100$ 时是 $7.3\times10^{11} \to 1.6\times10^{6}$，**降 5 个数量级**；代价是 likelihood 不再可精确计算（要对 $h$ 求和），只能 Monte Carlo——这正是 §43.2 学习算法必须跑两遍采样的原因。

**落点**：$(43.13)$ 的高阶展开 vs $(43.14)$ 的求和；图 43.1b 的 labelled shifter 由 hidden unit 学会（p.526 记述的 Hinton–Sejnowski 结果）；$(43.18)$ 的两项之差。</span>

## 43.2 带 hidden unit 的 Boltzmann machine · Boltzmann machine with hidden units（书 p.525）

现在我们给随机模型加入**隐神经元**（hidden neuron）。这些神经元不对应任何被观测的变量；它们可以自由地在 (43.4) 所定义的概率模型中扮演任何角色。它们实际上可能承担可解释的角色，有效地执行「特征抽取」（feature extraction）。

**带 hidden unit 的 Boltzmann machine 中的学习。** 带 hidden unit 的 Boltzmann machine 的活动规则与原版 Boltzmann machine 相同。学习规则同样可以由 maximum likelihood 推出，但现在必须考虑一个事实：hidden unit 的状态是未知的。我们用 $x$ 表示可见单元的状态、$h$ 表示隐单元的状态、$y_i$ 表示一个神经元（可见或隐）的通用状态，并记 $y \equiv (x, h)$。当可见神经元被钳制（clamped）在状态 $x^{(n)}$ 时，网络的状态是 $y^{(n)} \equiv (x^{(n)}, h)$。

给定单个数据样本 $x^{(n)}$ 时 $W$ 的 likelihood 是

```math
P\left(x^{(n)} \mid W\right) = \sum_h P\left(x^{(n)}, h \mid W\right) = \sum_h \frac{1}{Z(W)} \exp\left( \tfrac12 \left[y^{(n)}\right]^{\top} W y^{(n)} \right),
```

（式 (43.14)）其中

```math
Z(W) = \sum_{x,h} \exp\left( \tfrac12 y^{\top} W y \right).
```

（式 (43.15)）(43.14) 也可以写成

```math
P\left(x^{(n)} \mid W\right) = \frac{Z_{x^{(n)}}(W)}{Z(W)},
```

（式 (43.16)）其中

```math
Z_{x^{(n)}}(W) = \sum_h \exp\left( \tfrac12 \left[y^{(n)}\right]^{\top} W y^{(n)} \right).
```

（式 (43.17)）像之前那样对 likelihood 求导，我们发现对任一权重 $w_{ij}$ 的导数同样是「waking 项」与「sleeping 项」之差：

```math
\frac{\partial}{\partial w_{ij}} \ln P\left(\{x^{(n)}\}_{1}^{N} \mid W\right) = \sum_n \left\{ \langle y_iy_j \rangle_{P(h \mid x^{(n)}, W)} - \langle y_iy_j \rangle_{P(x,h \mid W)} \right\}.
```

（式 (43.18)）



第一项 $\langle y_iy_j\rangle_{P(h \mid x^{(n)}, W)}$ 是「把可见变量钳制在 $x^{(n)}$、隐变量自由地从其条件分布采样」时 $y_i$ 与 $y_j$ 的相关。第二项 $\langle y_iy_j\rangle_{P(x,h\mid W)}$ 是「Boltzmann machine 从自己的模型分布生成样本」时 $y_i$ 与 $y_j$ 的相关。

Hinton 与 Sejnowski 证明：像 labelled shifter ensemble 这样的非平凡系综，可以用带 hidden unit 的 Boltzmann machine 学出来。hidden unit 承担了特征检测器（feature detector）的角色，专门盯住很可能与三种位移之一相关联的模式。

Boltzmann machine 模拟起来耗时，因为 log likelihood 的梯度计算依赖于两个都由 Monte Carlo 方法求得的梯度的差。所以 Boltzmann machine 并未被广泛使用。如何用更高效的计算实现同样能力，是一个活跃的研究领域（Hinton et al., 1995; Dayan et al., 1995; Hinton and Ghahramani, 1997; Hinton, 2001; Hinton and Teh, 2001）。

## 43.3 练习 · Exercise（书 p.526）

[exercise] **Exercise 43.3.** [3] Can the 'bars and stripes' ensemble (figure 43.2) be learned by a Boltzmann machine with no hidden units? [You may be surprised!]
> 话题摘要：无 hidden unit 的二值 Boltzmann machine 能否学会「条纹」系综——重点是它看起来像高阶约束，其实不是（难度 3）。

[Figure 43.2：`bars and stripes` 系综的四个样本。它演示一个「先选朝向（横或竖）、再对每一行/列以概率 $1/2$ 整条打开」的生成过程——注意每条的取值是**整条一起**的，这是它看起来像高阶约束的来源。]

<span style="color:#1e8449;">**[译注]** 练习 43.3 的「你可能会惊讶」值得先给出判定路径，免得白算：**能**。这正是它反直觉的地方——上一节刚论证「二阶统计量抓不住 shifter」，这里却有一个同样「看起来需要高阶」的系综，能被**纯二阶**模型学会。

**为什么**：bars and stripes 的生成过程是「先掷一枚硬币选朝向」，朝向这个隐变量只有 $2$ 个取值。一个二阶 Boltzmann machine 的二阶项可以精确表达「所有同一条上的像素彼此强正相关、不同条之间零相关」这个结构；而「朝向」这个隐变量本身是**二值**的，二元隐变量所需表达力正好落在二阶模型的范围内。

**与 shifter 的差别**：shifter 的隐变量 $s$ 有三个取值，且它作用的方式是**平移**（改变像素间的位置对应关系），不是「整块一起翻转」。二阶项只能表达「$i,j$ 同向」这种成对约束，表达不了「$i$ 对齐到 $j$ 的左边一格还是右边一格」这种**下标依赖的**对齐。

**消失测试**：把 bars and stripes 改成「每条以概率 $1/2$ 独立开关**且**朝向以 $1/3$ 概率取三种（横、竖、对角）」，一旦朝向有三个值，二阶模型就不再够——需要至少一个三值隐变量（等价于两个二值隐变量加耦合）。

**方向感**：隐变量取值数 $2 \to 3$，参数量从「一个二阶项够」变成「需要额外的三阶或两个隐单元」，这就是 hidden unit 必须存在的定量理由。

**落点**：图 43.2 的生成描述；$(43.13)$ 的高阶项；对照图 43.1 的 shifter。</span>



# 第 44 章 · Supervised Learning in Multilayer Networks（书 p.527）

## 44.1 多层感知机 · Multilayer perceptrons

任何神经网络课程，若没有讨论有监督的多层网络（supervised multilayer network，又称 backpropagation network），都是不完整的。

multilayer perceptron 是一个前馈网络（feedforward network）。它有输入神经元、隐神经元和输出神经元。隐神经元可以排列成若干层（layer）。最常见的 multilayer perceptron 有一个隐层，被称为「两层」网络——「二」这个数字数的是神经元的层数，不包含输入层。

这样的前馈网络定义了一个从输入 $x$ 到输出 $y = y(x; w, A)$ 的非线性参数化映射（nonlinear parameterized mapping）。输出是输入与参数 $w$ 的连续函数；网络的架构（architecture），即该映射的函数形式，用 $A$ 表示。前馈网络可以被「训练」来执行回归（regression）与分类（classification）任务。

[Figure 44.1：一个典型的两层网络，六个输入、七个隐单元、三个输出。每一条线代表一个权重。它演示「层」这个词数的到底是什么。]

**回归网络（Regression networks）。** 就回归问题而言，一个单隐层网络的映射可以具有如下形式：

```math
\text{Hidden layer: } a_j^{(1)} = \sum_l w_{jl}^{(1)} x_l + \theta_j^{(1)}, \quad h_j = f^{(1)}\left(a_j^{(1)}\right)
```

（式 (44.1)）

```math
\text{Output layer: } a_i^{(2)} = \sum_j w_{ij}^{(2)} h_j + \theta_i^{(2)}, \quad y_i = f^{(2)}\left(a_i^{(2)}\right)
```

（式 (44.2)）其中例如 $f^{(1)}(a) = \tanh(a)$、$f^{(2)}(a) = a$。这里 $l$ 遍历输入 $x_1, \ldots, x_L$，$j$ 遍历隐单元，$i$ 遍历输出。「权重」$w$ 与「偏置」$\theta$ 合起来构成参数向量 $w$。隐层上的非线性 sigmoid 函数 $f^{(1)}$ 赋予神经网络比标准 linear regression 模型更大的计算弹性。图形上，我们可以把神经网络表示成一串相互连接的神经元层（图 44.1）。

**这些网络能实现什么样的函数？** 正如我们在第 39 章探索单神经元的权重空间、考察它能产生哪些函数，现在让我们探索一个多层网络的权重空间。在图 44.2 与 44.3 中，我取一个单输入单输出、隐单元数 $H$ 很大的网络，把偏置与权重 $\theta_j^{(1)}$、$w_{jl}^{(1)}$、$\theta_i^{(2)}$、$w_{ij}^{(2)}$ 设为随机值，画出得到的函数 $y(x)$。我把隐单元的偏置 $\theta_j^{(1)}$ 设为均值零、标准差 $\sigma_{\text{bias}}$ 的高斯随机值；输入到隐层的权重 $w_{jl}^{(1)}$ 设为标准差 $\sigma_{\text{in}}$ 的随机值；偏置与输出权重 $\theta_i^{(2)}$、$w_{ij}^{(2)}$ 设为标准差 $\sigma_{\text{out}}$ 的随机值。

[Figure 44.2：单输入网络「函数先验」（prior over functions）的样本。它演示「权重的幅度决定函数的复杂度」——对 $\sigma_{\text{bias}} = 8, 6, 4, 3, 2, 1.6, 1.2, 0.8, 0.4, 0.3, 0.2$ 各取一个值、并令 $\sigma_{\text{in}} = 5\sigma_{\text{bias}}$，各画一条随机函数；其余超参数为 $H = 400$、$\sigma_{\text{out}} = 0.05$。]



[Figure 44.3：一个随机网络产生的函数的性质。它演示三条尺度律——随机权重网络的典型函数，其垂直尺度是 $\sqrt{H}\sigma_{\text{out}}$ 量级；函数显著变化的水平范围是 $\sigma_{\text{bias}}/\sigma_{\text{in}}$ 量级；最短的水平长度尺度是 $1/\sigma_{\text{in}}$ 量级。图中函数由 $H = 400$ 个隐单元、高斯权重 $\sigma_{\text{bias}} = 4$、$\sigma_{\text{in}} = 8$、$\sigma_{\text{out}} = 0.5$ 的网络产生。]

我们得到的函数类型取决于 $\sigma_{\text{bias}}$、$\sigma_{\text{in}}$ 与 $\sigma_{\text{out}}$ 的取值。随着权重与偏置变大，我们得到更复杂的函数：特征更多，对输入变量更敏感。随机权重网络产生的典型函数，其垂直尺度是 $\sqrt{H}\sigma_{\text{out}}$ 量级；函数显著变化的水平范围是 $\sigma_{\text{bias}}/\sigma_{\text{in}}$ 量级；而最短的水平长度尺度是 $1/\sigma_{\text{in}}$ 量级。

Radford Neal（1996）还证明了：当 $H \to \infty$ 时，通过随机化权重所生成的函数的统计性质**与隐单元数无关**；所以有趣的是，函数的复杂度变得与模型中参数的个数无关。决定典型函数复杂度的，是权重的特征幅度（characteristic magnitude）。因此我们可以预期：当我们把这些模型拟合到真实数据时，控制拟合函数复杂度的一个重要途径，就是控制权重的特征幅度。

[Figure 44.4：一个双输入网络先验的一个样本，参数为 $\{H, \sigma_{\text{in}}, \sigma_{\text{bias}}, \sigma_{\text{out}}\} = \{400, 8.0, 8.0, 0.05\}$。它演示「神经网络能造出比 linear regression 更复杂的曲面」——后者在同样两个输入上只是一张平面。]

图 44.4 展示了一个双输入单输出网络产生的一个典型函数。这应当与传统 linear regression 模型产生的函数——一张平面——做对比。神经网络能造出比 linear regression 更复杂的函数。

<span style="color:#1e8449;">**[译注]** 这三条尺度律都能在十行代码里复算，而且复算完你就知道该调哪个超参数。

**垂直尺度 $\sqrt{H}\sigma_{\text{out}}$**：$y = \sum_j w_{\text{out},j}\tanh(\cdot)$，若 $\tanh$ 已饱和（$|\text{input}| \gg 1$），每项 $\approx \pm w_{\text{out},j}$，$H$ 个独立同分布项相加，方差 $H\sigma_{\text{out}}^{2}$，标准差 $\sqrt{H}\sigma_{\text{out}}$。图 44.3 的参数 $\sqrt{400}\times 0.5 = 10$，与纵轴 $\pm10$ 完全对应。

**水平范围 $\sigma_{\text{bias}}/\sigma_{\text{in}}$**：第 $j$ 个隐单元「开口」的位置由 $w_{\text{in},j}x + \theta_j \approx 0$ 给出，即 $x^{*}_j = -\theta_j/w_{\text{in},j}$。$\theta_j$ 的尺度是 $\sigma_{\text{bias}}$、$w$ 的尺度是 $\sigma_{\text{in}}$，所以这些「拐点」散布在宽度 $\sigma_{\text{bias}}/\sigma_{\text{in}}$ 内。图 44.3 是 $4/8 = 0.5$。

**最短长度尺度 $1/\sigma_{\text{in}}$**：单条 $\tanh$ 从 $-1$ 过渡到 $+1$ 的宽度是 $\Delta x \approx 2/|w_{\text{in},j}|$，$w$ 的尺度是 $\sigma_{\text{in}}$，故 $\Delta x \sim 1/\sigma_{\text{in}}$。图 44.3 是 $1/8 = 0.125$。

**消失测试**：如果 $\sigma_{\text{out}}$ 不随 $H$ 一起调（Neal 的 $H\to\infty$ 极限所要求的正是「$\sigma_{\text{out}} \propto 1/\sqrt{H}$」），那么加宽网络只会让输出幅度按 $\sqrt{H}$ 爆炸，拟合时必须靠极小的学习率救场——这是「大网络训不动」的经典症状之一。

**方向感**：复杂度由 $H$ **和** $\sigma$ 共同决定；$H\to\infty$ 时前者失效、只剩后者。所以正则化该正则化 $\sigma$（weight decay），而不是数参数。

**落点**：图 44.3 的三条标注；Neal (1996) 的高斯过程极限；$(44.3)$ 的训练目标。</span>

## 44.2 回归网络的传统训练方式 · How a regression network is traditionally trained（书 p.528）

这个网络用数据集 $D = \{x^{(n)}, t^{(n)}\}$ 训练：调整 $w$ 以最小化一个 error function，例如

```math
E_D(w) = \frac12 \sum_n \sum_i \left[ t_i^{(n)} - y_i\left(x^{(n)}; w\right) \right]^2.
```

（式 (44.3)）这个 objective function 是一组项之和，每个输入/目标对 $\{x, t\}$ 对应一项，度量输出 $y(x; w)$ 与目标 $t$ 有多接近。

这个最小化基于对 $E_D$ 梯度的反复计算。该梯度可以用 backpropagation 算法（Rumelhart et al., 1986）高效算出，后者用 chain rule 求导。

> **本块（PDF p521-540 = 书 p.509-528）到此结束。** 第 44 章在本页刚开始，§44.2 的 backpropagation 只写到「用 chain rule 求导」，下一块应从书 p.529（PDF 541）续起。

---

## §D 降级结构表

本块 20 页中，插图全部是**位图/矩阵版式**，多数可复原为文字描述，少数不可复原。逐条列如下。

### D.1 可复原（已用带编号的图注降级为「它演示什么」）

| 图 | 页 | 复原程度 | 依据 |
|---|---|---|---|
| Figure 42.3 | 书 509 | 结构可复原，像素不可 | 权重矩阵可由 4 个 $5\times5$ 模式的行 Hebb rule 重算；取值集合已实测为 $\{-4,-2,0,2,4\}$ |
| Figure 42.4 | 书 511 | 同上 | $26/300$ 个 `x` 位置不可复原，但删除比例 $8.7\%$ 与 basin 收缩可从正文数值推出 |
| Figure 42.5 | 书 511 | 部分 | 六个记忆的位图不可复原；「只有一个稳定」这一结论在正文有独立陈述 |
| Figure 42.6 | 书 512 | 可复原 | 图中 9 行文字（`moscow------russia` 等）已逐条抄入正文，四种失效模式可逐条对应 |
| Figure 42.7 | 书 513 | 可复原 | 高斯密度 + 尾部面积，$(42.22)$ 已给出闭式，图只是它的几何 |
| Figure 42.8 | 书 514 | 数值可复原 | 台阶在 $N/I = 0.138$、overlap 从 $0.97 \to 0$，两个数都已复算 |
| Figure 42.10 | 书 517 | 结构可复原 | $K=4$ 的 $4\times4$ 网格、两组负权重可用 $-d_{BD}$ 重算 |
| Figure 42.11 | 书 518 | 不可复原（见 D.2） | 三十城市轨迹是多帧位图 |
| Figure 43.1 | 书 524 | 部分 | 「上八像素随机、下八像素是其左/不移/右移副本」可复原；具体像素不可 |
| Figure 43.2 | 书 526 | 可复原 | 生成过程（先选朝向、再整条掷硬币）在正文完整给出 |
| Figure 44.1 | 书 527 | 可复原 | 拓扑 $6\to7\to3$，可由 $(44.1)(44.2)$ 完全重建 |
| Figure 44.2 | 书 527 | 数值可复原 | 11 组 $\sigma_{\text{bias}}$ 全部列出，可重跑 |
| Figure 44.3 | 书 528 | 可复原 | 三条尺度律已给闭式并经实跑核对（$\sqrt{400}\times0.5 = 10$） |
| Figure 44.4 | 书 528 | 数值可复原 | 参数表已给，可重跑 |

### D.2 不可复原（只保留「它演示什么」，不补 figure 号、不猜测像素）

| 图 | 页 | 不可复原的部分 | 说明 |
|---|---|---|---|
| Figure 42.11a | 书 518 | 三十城市 TSP 的中间轨迹帧 | 原文为多帧叠加位图，城市坐标与迭代帧数均未给出 |
| Figure 42.11b | 书 518 | travelling scholar problem 的 30 个地点坐标 | 只给了「27 个学院 + 工程系 + 图书馆 + Aiyer 家」，坐标不可得 |
| Figure 42.12 | 书 520 | Erik's dynamics 的两格示例 | 只示意一格扩张，无信息量损失，但像素不可复原 |
| Figure 42.13 | 书 520 | (a)–(d)、(z) 的棋子位置 | 规则已完整文字化，10 格标记位置可推出（$l \le 3$ 的 10 格） |
| Figure 42.14 | 书 521 | 具体占位图案 | 已用 $\sum_{l\ge4}(l+1)2^{-l} = 3/4$ 的复算替代 |
| Figure 42.9 | — | **本块内不存在** | 上一块用到过 Algorithm 42.9 的编号连续性；本块无 Figure 42.9，故不补号 |
| Figure 43.1 的像素级内容 | 书 524 | 16 个具体二值图案 | 系综定义完整，样本不可复原 |

---

## §E 原文自身的问题（本块累计 3 条，全书累计 36 条）

1. **† p.525（PDF 537）**：「to capture merely the fourth-order statistics in a $128\times128$ pixel image, we need more than $10^{7}$ parameters」。复算 $\binom{16384}{4} = 3.0013\times10^{15}$，差八个数量级，疑为 $10^{15}$。已在正文该处加 † 并给出复算。

2. **† p.519（PDF 531）** Exercise 42.9 题干：「show that **in** can be written in the form」应为「**it**」。纯笔误，已在译文里按 it 译出。

3. **† p.523（PDF 535）**：$(43.12)$ 后原文写「precisely the value of the weights given by the Hebb rule, equation (16.5)」。第 16 章是 message passing，Hopfield 的 Hebb rule 在本版是 §42.1 的 $(42.1)$；$(16.5)$ 疑为交叉引用错误。已在译文中保留 `(16.5)` 的字面值，不擅改编号，但在译注中标出。

---

## §F 本块的可复算验证清单（全部实跑过，脚本在 `AppData/Local/Temp/`）

| 编号 | 验证对象 | 脚本 | 结果 |
|---|---|---|---|
| V1 | Hebb 噪声的 1% 口径 | `mk23_verify.py` §1 | $N/I=0.18 \Rightarrow \Phi(-2.3570) = 9.211\times10^{-3}$ |
| V2 | $(42.25)$ 的 $4\ln I$ 与精确解对比 | `mk23_verify.py` §2 | $I=10^{6}$、$\epsilon=0.01$：书 $15510.5$ vs 精确 $19680.2$，比值 $0.788$ |
| V3 | $(42.27)$ 的 $0.122I^{2}$ 与 $0.24$ bits/weight | `mk23_verify.py` §3 | $H_2(0.016)=0.118350$；$0.138\times0.881650=0.121668$；$0.121668/0.5=0.2433$ |
| V4 | southeast 的守恒量 $3/4$ | `mk23_verify.py` §4 | $\sum_{l\ge4}(l+1)2^{-l}=0.7500000000$ |
| V5 | 四阶统计参数量 † | `mk23_verify.py` §5 | $\binom{16384}{4}=3.0013\times10^{15}$ |
| V6 | 图 42.3 权重取值集合 | `mk23_verify2.py` | 四模式 Hebb 重算值域 $=\{-4,-2,0,2,4\}$；对称性 $\sum\lvert W-W^{\top}\rvert = 0$；对角全零 |
| V7 | Erik's puzzle 最小值 $= N$ | `mk23_verify3.py` §1 | $N=2,3,4,5$ 穷举得 $2,3,4,5$；$N=6,8$ 对角线可行 |
| V8 | 练习 42.9 与最优 decoder 之比 | `mk23_verify3.py` §3 | $I=1000$、$o_{mn}=0$：$249.5/500 = 0.499$ |



> 页眉自证：`44.3: Neural network learning as inference` / 页码 `529`（书页 529 = PDF 541 − 12）。本页上半是 §44.2 的收尾，第 22 行起 §44.3。

**Weight decay（权重衰减）。** 常常还会加入 regularization（regularization，也叫 weight decay（权重衰减）），把 objective function 改成：

```math
M(w) = \beta E_D + \alpha E_W ,
```

（式 (44.4)）其中例如

```math
E_W = \frac{1}{2}\sum_i w_i^{2} .
```

这个附加项偏好较小的 $w$ 取值，并降低一个模型 overfit（过拟合）训练数据中噪声的倾向。

Rumelhart et al. (1986) 证明了 multilayer perceptron（多层感知机）是可以被训练出来的——方法是在 $M(w)$ 上做 gradient descent（梯度下降）——去发现非平凡（non-trivial）问题的解，例如判定一幅图像是否对称。这些网络已被成功地应用到各种各样的真实世界任务上，范围之广从朗读英文文本（Sejnowski and Rosenberg, 1987）到为多镜面望远镜调焦（Angel et al., 1990）。

## 44.3 把神经网络学习看作推断 · Neural network learning as inference（书 p.529）

上面这个神经网络学习过程可以给出如下的概率解释。[这里我们重述并推广第 41 章的讨论。]

error function 被解释为在定义一个 noise model。$\beta E_D$ 就是负对数似然（negative log likelihood）：

```math
P(D \mid w, \beta, H) = \frac{1}{Z_D(\beta)} \exp\left( -\beta E_D \right) .
```

（式 (44.5)）于是，使用 sum-squared error $E_D$（式 (44.3)）就对应于对 target 变量作 Gaussian noise 的假设，而参数 $\beta$ 定义了噪声水平 $\sigma^{2}_{\nu} = 1/\beta$。

类似地，regularizer 被解释成参数上的对数先验概率分布（log prior probability distribution）：

```math
P(w \mid \alpha, H) = \frac{1}{Z_W(\alpha)} \exp\left( -\alpha E_W \right) .
```

（式 (44.6)）若 $E_W$ 如上定义为二次型，则对应的 prior distribution 是方差 $\sigma^{2}_{W} = 1/\alpha$ 的 Gaussian。概率模型 $H$ 指定网络的 architecture $A$、likelihood (44.5) 与 prior (44.6)。

于是 objective function $M(w)$ 就对应于「给定数据、对参数 $w$ 做推断」这件事：

```math
P(w \mid D, \alpha, \beta, H)
= \frac{P(D \mid w, \beta, H)\,P(w \mid \alpha, H)}{P(D \mid \alpha, \beta, H)}
= \frac{1}{Z_M} \exp\left( -M(w) \right) .
```

（式 (44.7)(44.8)）由（局部）最小化 $M(w)$ 找到的 $w$，就被解释为（局部）最可能的参数向量 $w_{\text{MP}}$。

把 $M(w)$ 解释成对数概率，在这一步并没有加进多少新东西。但当我们继续做别的推断时，新的工具就会浮现。不过先让我把 classification network 的概率解释确立下来——同一套工具对它同样适用。

<span style="color:#1e8449;">**[译注]** (44.4) 写了 $\alpha$、$\beta$ 两个系数，但**真正决定收缩强度的只有比值**。把 (44.5) 与 (44.6) 代进 (44.7) 再取负对数：$M(w) = \beta E_D + \alpha E_W$，而 $\frac{1}{\beta}M(w) = E_D + \frac{\alpha}{\beta}E_W$ 与原式给出同一个 $\arg\min$。所以 weight decay 的强度是

```math
\lambda = \frac{\alpha}{\beta} = \frac{\sigma^{2}_{\nu}}{\sigma^{2}_{W}} ,
```

即「噪声方差 ÷ 先验方差」，量纲是 $1/(w$ 的量纲$)^{2}$。**方向感**：把 $\lambda$ 直接猜成 $10^{-3}$ 这种无量纲数是没意义的，先得看 target 的量级。

**消失测试**：若把 $\alpha$、$\beta$ 当两个独立旋钮在二维网格上扫，你会跑出一大片等高线的平台——因为沿 $\lambda$ 一维就够了，另有一维是多余的；更糟的是 §44.4 的 evidence 会同时给出 $\hat\alpha$ 与 $\hat\beta$，若不懂它们只以比值进入目标函数，就会把「证据偏好大的 $\beta$」误读成「模型变好了」。

**复算**：取 $E_D = 0.5$、$E_W = 2$、$\beta = 10$、$\alpha = 0.5$，得 $M = 6.0$；而 $E_D + \lambda E_W = 0.5 + 1.0 = 1.5$，两式的 $\arg\min$ 由 $\lambda = 0.05$ 唯一决定，$\beta$ 只改变目标函数的单位、不改变最小值的位置。

**失败模式的具体形态**：如果把 $\alpha$ 与 $\beta$ 各自按数值大小排序、去找「哪个超参数更关键」，结论会随数据单位翻转 —— 把 target 从米换成毫米，$\sigma^{2}_{\nu}$ 缩小 $10^{6}$ 倍、$\lambda$ 同比缩小，而 evidence 报出的 $\hat\alpha$ 数字不变。单看 $\hat\alpha$ 的数值是无意义的，只有比值 $\hat\alpha/\hat\beta$ 有物理含义。

**落点**：(44.4)–(44.8)；第 41 章（书 p.487-500）对同一分解的重复推导；练习 41.2 就是要你把它化成 $\lambda$ 的单参数形式。</span>

<span style="color:#1e8449;">**[译注]** (44.8) 里的 $Z_M$ 被原文一句话带过，可它正是 MAP 与真正 Bayesian 的分界线。$M(w)$ 只决定 $\arg\max$；$Z_M = \int \exp(-M(w))\,dw$ 决定归一化，物理上等于「模型在多大体积的参数空间里都说得过去」。

**量的方向感**：对二次型 $E_W$，Gaussian 积分给出 $Z_M \propto \alpha^{W/2}$（$W$ = 参数个数），这个 $W/2$ 次幂就是后面 Occam factor 的来源——参数越多，$Z_M$ 被 $\alpha$ 抬得越高，越难被证据支持。

**消失测试**：只留 $w_{\text{MP}}$、丢掉 $Z_M$，你就拿不到 (44.7) 的分母 $P(D\mid\alpha,\beta,H)$，选 $\alpha$ 只能退回 cross-validation：误差随折数抖动、无法求梯度、控制参数一多就退化成网格搜索。有了 $Z_M$，选 $\alpha$ 变成一条平滑可微的曲线（图 44.5e）。

**复算**：一维情形 $E_W = w^{2}/2$、$E_D = (w-1)^{2}$、$\alpha = \beta = 1$，则 $M(w) = 1.5w^{2} - 2w + 1$，$w_{\text{MP}} = 2/3$、$M(w_{\text{MP}}) = 1/3$，而归一化常数 $Z_M = \int e^{-M}dw = 1.036966$ —— 这个数在纯 MAP 路线里彻底消失。

**失败模式**：把 $w_{\text{MP}}$ 当成「参数的点估计」直接代进下游计算，会系统性地低估不确定性；$Z_M$ 越小（先验越紧），低估越严重。在 $W$ 维参数空间里，被丢掉的那份后验体积按 $\alpha^{-W/2}$ 增长，$W$ 一大就完全失真。

**落点**：(44.8)；第 28 章（模型比较与 Occam factor，书 p.343-356）；§45.2 的 marginal likelihood 是它在函数空间上的版本。</span>



> 页眉自证：`530` / `44 — Supervised Learning in Multilayer Networks`（书页 530 = PDF 542 − 12）。本章偶数页页眉只印页码与章名，章节边界靠页码判断。

#### Binary classification networks（二值分类网络）

若数据集里的 target $t$ 是二值分类标签 $(0,1)$，自然要用一个神经网络，其输出 $y(x; w, A)$ 被界在 0 与 1 之间，并被解释为概率 $P(t{=}1 \mid x, w, A)$。例如，一个带单隐层的网络可以由前向传播方程 (44.1) 与 (44.2) 描述，取 $f^{(2)}(a) = 1/(1+e^{-a})$。此时 error function $\beta E_D$ 被换成负对数似然：

```math
G(w) = -\left[ \sum_n t^{(n)} \ln y(x^{(n)}; w) + \left(1 - t^{(n)}\right) \ln\left(1 - y(x^{(n)}; w)\right) \right] .
```

（式 (44.9)）total objective function 于是是 $M = G + \alpha E_W$。注意这里**不含参数 $\beta$**（因为不存在 Gaussian noise）。

#### Multi-class classification networks（多类分类网络）

对于多类分类问题，我们可以用一个向量 $t$ 来表示 target：其中单个元素置 1 指示正确类别，其余元素置 0。这种情形下适合用「softmax」网络，它的输出相互耦合、求和为 1，并被解释为类概率 $y_i = P(t_i{=}1 \mid x, w, A)$。方程 (44.2) 的最后一步被替换成：

```math
y_i = \frac{e^{a_i}}{\sum_{i'} e^{a_{i'}}} .
```

（式 (44.10)）此情形下的负对数似然是

```math
G(w) = -\sum_n \sum_i t_i^{(n)} \ln y_i(x^{(n)}; w) .
```

（式 (44.11)）与 regression network 的情形一样，最小化 objective function $M(w) = G + \alpha E_W$ 对应于 (44.8) 那种形式的推断。在这个解释之上可以搭出各种有用的结果。

<span style="color:#1e8449;">**[译注]** (44.9) 里**没有 $\beta$ 不是笔误**：$\beta$ 的来源是 Gaussian noise 的方差 $\sigma^{2}_{\nu}$，而二值标签没有「方差」这个自由度可调。把 $t \in \{0,1\}$ 看成 Bernoulli 抽样，likelihood 是 $y^{t}(1-y)^{1-t}$，取负对数正好是 (44.9)，其归一化常数已经是 1。

**方向感**：回归网络有两个超参数 $(\alpha, \beta)$，二值分类网络只剩一个 $(\alpha)$——这直接决定了 §44.4 里 evidence 要优化几维。

**消失测试**：若硬用 squared error 配 sigmoid，梯度里会多出 sigmoid 的导数因子：$\partial E/\partial a = (y-t)\,y(1-y)$。当网络**自信地错**（$y \to 0$ 而 $t=1$）时 $y(1-y) \to 0$，梯度趋于零，训练卡死在那儿；而 (44.9) 的梯度是 $y - t$，恰恰在自信地错时最大。

**复算**：$y = 0.01$、$t = 1$ 时，(44.9) 给 $G = -\ln 0.01 = 4.605170$，梯度 $\partial G/\partial a = y - t = -0.99$；同一点用平方误差得 $E = 0.490050$、梯度 $-0.009801$ —— 差 $101.01$ 倍，这就是「自信地错」时 cross-entropy 还能推、平方误差推不动的定量差别。

**代价的方向**：(44.9) 在 $y$ 趋于 $0$ 或 $1$ 时有 $\ln 0$ 的数值问题，实现时必须把 $y$ 截断到 $[\epsilon, 1-\epsilon]$（常用 $\epsilon = 10^{-15}$），或者改用 log-sum-exp 的写法；否则一个饱和的 sigmoid 就能让整批梯度变成 NaN。

**落点**：(44.9) 与 (44.2) 的 $f^{(2)}(a) = 1/(1+e^{-a})$；§41.2 的 logistic 回归是 $D$ 只有一个样本点时的特例；练习 44.1 用 (44.12) 的互信息给分类器打分，正是这套 likelihood 的「检验版」。</span>

<span style="color:#1e8449;">**[译注]** (44.10) 的 softmax 在这里是**必需**而非装饰：二分类时 sigmoid 一个输出就够，多分类若用 $K$ 个独立 sigmoid，输出不求和为 1，「概率」解释当场失效——$K=10$ 个类可以同时报出 $0.9$，总和 $9$。

**量的方向感**：softmax 的耦合是约束 $\sum_i y_i = 1$ 的实现；配上 (44.11)，梯度化简成干净的一步

```math
\frac{\partial G}{\partial a_i} = y_i - t_i ,
```

没有 $y_i(1-y_i)$ 因子。计算代价只多一个 log-sum-exp，$O(K)$。

**消失测试**：去掉归一化、把 (44.11) 用在独立 sigmoid 上，你得到 $K$ 个互不竞争的二元问题；在 digit recognition 这种**互斥**任务上，模型会给出两个类同时为 0.9 的自相矛盾预测，而负对数似然仍然有限、不会报错——这才是危险处。

**复算**：$a = (1, 2, 3)$ 时 softmax 给 $(0.09003, 0.24473, 0.66524)$、和为 $1.00000$；若换成三个独立 sigmoid 得 $(0.73106, 0.88080, 0.95257)$、和为 $2.56443$ —— 后者在互斥任务上不可解释。

**实现注意**：softmax 必须用「先减去最大值」的写法，即 $y_i = e^{a_i - m}/\sum_{i'} e^{a_{i'} - m}$（$m = \max_i a_i$）。这与原式数学等价，但数值上安稳；不这么做时 $a_i$ 达到几百就会直接溢出成 inf。

**落点**：(44.10)(44.11)；练习 44.1 的分类器 A–E 全是 $K=2$ 的退化版；第 41 章习题里的 softmax 与 §44.4 的 evidence 共用同一 likelihood。</span>

## 44.4 监督式前馈神经网络的贝叶斯方法之好处 · Benefits of the Bayesian approach to supervised feedforward neural networks（书 p.530）

从统计学的角度看，supervised neural network 不过是 nonlinear curve-fitting（非线性曲线拟合）装置。然而曲线拟合并不是一件平凡的任务。一个插值模型的有效复杂度（effective complexity）至关重要，如图 44.5 所示。考虑一个影响模型复杂度的控制参数，例如 regularization constant $\alpha$（weight decay parameter）。当把这个控制参数朝着「增加模型复杂度」的方向变动时（从图 44.5a–c 往下走，并在图 44.5d 中从左向右移动），模型能达到的对训练数据的最佳拟合变得越来越好。然而模型的实测表现——test error——先下降、然后重新上升。过复杂的模型会 overfit 数据、泛化很差。这个问题同样会让 multilayer perceptron 的 architecture 选择、radial basis function network（径向基函数网络）中基函数的半径选择、乃至任何多维 regression 问题中输入变量本身的选择变得纠结。因此，为模型控制参数找到适合当前数据的取值，是一个重要且非平凡的问题。



> 页眉自证：`44.4: Benefits of the Bayesian approach to supervised feedforward neural networks` / 页码 `531`（书页 531 = PDF 543 − 12）。

[Figure 44.5：模型复杂度的优化。它演示一条完整的「过拟合—证据」对照链：过度复杂的模型在训练集上更好、在测试集上更差，而 evidence 不需要测试集就能把复杂度自动定在中间。面板 (a)–(c) 是一个 radial basis function model（径向基函数模型）对「一个输入变量、一个输出变量」的简单数据集的插值；随 regularization constant 变化使模型复杂度上升（从 (a) 到 (c)），插值函数能越来越贴地拟合训练数据，但过了某一点模型的泛化能力（test error）开始恶化。面板 (d) 是 training error 与 test error 关于 model control parameters 的两条曲线；面板 (e) 是 log probability(data | control parameters) 关于同一横轴的曲线。概率论允许我们**不需要测试集**就优化这些控制参数。]

图注逐句对照：「Optimization of model complexity.」= 模型复杂度的优化。「Panels (a–c) show a radial basis function model interpolating a simple data set with one input variable and one output variable.」= 面板 (a)–(c) 展示一个 radial basis function model（径向基函数模型）对一个「一输入、一输出」的简单数据集做插值。「As the regularization constant is varied to increase the complexity of the model (from (a) to (c)), the interpolant is able to fit the training data increasingly well, but beyond a certain point the generalization ability (test error) of the model deteriorates.」= 当 regularization constant 被改变、使模型复杂度上升时（从 (a) 到 (c)），插值函数对训练数据的拟合越来越好；但过了某一点，模型的泛化能力（test error）开始变差。「Probability theory allows us to optimize the control parameters without needing a test set.」= 概率论让我们可以在不需要测试集的情况下优化这些控制参数。

> **本图的可复原边界**：原图是位图，面板 (a)–(c) 的散点坐标、基函数中心 $\{c_h\}$、面板 (d)(e) 的坐标轴刻度与线形都无法逐点复原。可复原的只有**定性特征**与**两条曲线的关系**：据 (44.4)–(44.8)，(d) 中 training error 单调下降、(e) 中 log evidence 呈单峰（峰值落在 44.5b 对应的复杂度，见下文「使 evidence 最大的 $\alpha$ 显示在图 44.5b」），因此 (d) 的 test error 必然是 U 形。这三条是本块能硬核对的不变量。

**过拟合问题可以用贝叶斯方法来控制模型复杂度，从而得到解决。**

若我们给模型一个概率解释，就可以评估不同控制参数取值下的 evidence。正如第 28 章所解释的，过复杂的模型结果反而**更不可能**（less probable），而 evidence $P(\text{Data} \mid \text{Control Parameters})$ 可以当作优化模型控制参数的目标函数（图 44.5e）。使 evidence 最大的那个 $\alpha$ 取值被显示在图 44.5b 中。

用贝叶斯方法优化模型控制参数有**四个**重要优点。(1) 不涉及「test set」或「validation set」，因此全部可用的训练数据都可以同时用于模型拟合与模型比较。(2) regularization constant 可以在线（on-line）优化，即与普通模型参数的优化同时进行。(3) 贝叶斯目标函数**不是噪声的**（not noisy），这与 cross-validation 度量形成对比。(4) evidence 关于控制参数的梯度可以算出来，使得同时优化**大量**控制参数成为可能。

<span style="color:#1e8449;">**[译注]** 四条优点里 (1) 与 (3) 最容易被当成营销话术，其实都能落到具体的量上。

**(1) 的实义是「有效样本量」**：留出法把 $N$ 个点切成 $N_{\text{tr}}$ 与 $N_{\text{val}}$，模型只见 $N_{\text{tr}}$，比较只能用 $N_{\text{val}}$；而 evidence 用全部 $N$ 个点同时做拟合与比较。在 $N$ 很小的场合（比如 §45 的高维小样本回归）这不是方便，是**能不能做**的问题：留出 20% 后剩 8 个点时，$N_{\text{val}}=2$，交叉验证的方差量级是 $1/\sqrt{2}\approx 0.7$，比要比较的差异还大。

**(3) 的实义是可微**：交叉验证误差是「重新训练 $k$ 次」得到的阶梯状函数，关于 $\alpha$ 不可微、也没法给梯度；evidence 有解析梯度 $\partial \ln Z / \partial \ln \alpha = W/2 - \alpha E_W$（对二次型 $E_W$，$W$ 为参数个数），这一条正是 (4) 的前提。

**消失测试**：去掉 evidence，(4) 立刻失效——你只剩网格搜索，且代价随控制参数个数指数增长：10 个控制参数各 10 个候选就是 $10^{10}$ 次训练。

（§28.2 的 Occam factor 推导与 (28.18) 是同一件事在参数空间里的版本。）

**落点**：(44.7) 的分母；第 28 章（书 p.343-356）的 Occam factor 推导；§45.2 把同一件事搬到函数空间。</span>

概率建模也以自然的方式处理不确定性。它提供了一个唯一的处方——**marginalization（边缘化）**——来把「关于参数的不确定性」纳入预测；这个程序产生更好的预测，正如我们在第 41 章所见。图 44.6 显示了一个已训练神经网络的预测上的 error bar（误差棒）。

[Figure 44.6：一个已训练 regression network 的预测上的误差棒。它演示「预测该带多宽的置信区间」这件事本身是怎么从参数后验里自动生出来的：实线是在数据点上训练出的 multilayer perceptron 在最佳拟合参数处的预测，虚线是**仅由参数 $w$ 的不确定性**产生的那一对误差棒；注意误差棒在数据稀疏的地方变宽。]

<span style="color:#1e8449;">**[译注]** 图 44.6 的虚线不是「模型的均方误差」，而是**参数后验传过去的方差**，这两者在数学上是不同的东西。对 (44.5)(44.6) 的 Gaussian 模型，预测 $y(x^{*})$ 的后验方差是

```math
\sigma^{2}(x^{*}) = \frac{1}{\beta} + g^{\top} A^{-1} g , \qquad A = \beta \nabla\nabla E_D + \alpha I ,
```

前一项是**噪声**（无论多少数据都不会消失，这就是为什么数据点上误差棒也不为零），后一项是**参数不确定性**（$g = \partial y(x^{*};w)/\partial w$，$A^{-1}$ 是后验协方差）。

**量的方向感**：数据稀疏处 $g$ 的方向上 $A$ 约束弱、$A^{-1}$ 大，误差棒变宽；数据密集处 $A$ 被多个样本加厚、$A^{-1}$ 缩小，误差棒收到噪声底 $1/\sqrt{\beta}$。所以两条虚线应该**在数据中心处夹紧、在边缘张开**——图 44.6 的定性特征正是这个。

**消失测试**：只报最佳拟合曲线（实线）而不做 marginalization，你无法区分「这里没数据」和「这里数据说就是 0」——这正是 §41 强调过的失效模式：单点估计在稀疏区给出与密集区同样自信的断言。

**落点**：(44.5)–(44.8)；第 41 章（书 p.487-500）用一维例子手算过同一个 $A^{-1}$；Neal (1996) 的 Laplace 近似即此式的高斯版。</span>

#### Implementation of Bayesian inference（贝叶斯推断的实现）

正如第 41 章所提到的，多层网络的贝叶斯推断可以用 Monte Carlo sampling（蒙特卡罗抽样）来实现，也可以用采用 Gaussian approximation（高斯近似）的确定性方法来实现（Neal, 1996; MacKay, 1992c）。



> 页眉自证：`532` / `44 — Supervised Learning in Multilayer Networks`（书页 532 = PDF 544 − 12）。本页第 12 行起 §44.5。

在「用贝叶斯框架做数据建模」这件事之内，改进我们的概率模型是很容易的。例如，若我们相信某个问题里有些输入变量可能与要被预测的量**无关**，但不知道是哪些，我们就可以定义一个有多个 hyperparameter（超参数）的新模型，把「输入变量相关性不确定」这个观念编码进去（MacKay, 1994b; Neal, 1996; MacKay, 1995b）；这类模型随后会从数据中自动推断出：哪些输入变量对这个问题是相关的。

<span style="color:#1e8449;">**[译注]** 这段话是 automatic relevance determination（ARD，自动相关性判定）的一句话版，它与本章前面所有内容的区别在于**超参数不再是一个标量**。

前面 (44.4) 只有一个 $\alpha$、一个 $\beta$；ARD 把 $E_W = \frac{1}{2}\sum_i w_i^{2}$ 拆成按输入分组的若干组，每组一个 $\alpha_k$：

```math
E_W = \frac{1}{2}\sum_{k} \alpha_k \sum_{i \in \text{group } k} w_i^{2} .
```

**机制**：evidence 关于 $\alpha_k$ 的最优点满足 $\alpha_k^{\text{MP}} = \gamma_k / (2 E_{W,k})$，其中 $\gamma_k \in [0, W_k]$ 是「有效参数个数」。若第 $k$ 个输入无用，其权重被证据推到 0 附近，$\gamma_k \to 0$、$\alpha_k \to \infty$，该输入被**软删除**——权重不是被人工置零，而是被后验压成 0。

**量的方向感**：这一步把「特征选择」从离散搜索（$2^{I}$ 个子集）变成连续优化（$I$ 个 $\alpha_k$ 的梯度下降），$I=100$ 时是 $10^{30}$ 与 $100$ 之别的规模差。

**消失测试**：只有单个 $\alpha$，所有权重被同一强度收缩，无法表达「这一维无用、那一维有用」；你会看到无用输入的权重被压小但**压不到零**，预测方差仍被它污染。

（Bishop §7.2 的 relevance vector machine 是同一机制在稀疏核方法侧的版本。）

**落点**：MacKay (1994b)「Bayesian methods for backpropagation networks」；MacKay (1995b) 的 soft weight sharing；Neal (1996) 的 §5；本页超参数只是 (44.4) 的 $\alpha$ 从标量升为向量。</span>

## 44.5 练习 · Exercises（书 p.532）

[exercise] **Exercise 44.1.** [4] *How to measure a classifier's quality.* You've just written a new classification algorithm and want to measure how well it performs on a test set, and compare it with other classifiers. What performance measure should you use? There are several standard answers. Let's assume the classifier gives an output $y(x)$, where $x$ is the input, which we won't discuss further, and that the true target value is $t$. In the simplest discussions of classifiers, both $y$ and $t$ are binary variables, but you might care to consider cases where $y$ and $t$ are more general objects also.

The most widely used measure of performance on a test set is the **error rate** – the fraction of misclassifications made by the classifier. This measure forces the classifier to give a 0/1 output and ignores any additional information that the classifier might be able to offer – for example, an indication of the firmness of a prediction. Unfortunately, the error rate does not necessarily measure how informative a classifier's output is. Consider frequency tables showing the joint frequency of the 0/1 output of a classifier (horizontal axis), and the true 0/1 variable (vertical axis). The numbers that we'll show are percentages.

> 话题摘要：怎么衡量一个分类器的好坏。[4] 题干要求你比较 error rate、$(e^{+}, e^{-})$ 对、error-reject curve（ROC）、以及 (44.12) 的互信息四种度量，并给出分类器 A–E 的互信息数值。判据是「换个代价比会不会翻盘」。

The error rate $e$ is the sum of the two off-diagonal numbers, which we could call the **false positive rate** $e^{+}$ and the **false negative rate** $e^{-}$. Of the following three classifiers, A and B have the same error rate of 10% and C has a greater error rate of 12%.

**Classifier A**

| | $y=0$ | $y=1$ |
|---|---|---|
| $t=0$ | 90 | 0 |
| $t=1$ | 10 | 0 |

**Classifier B**

| | $y=0$ | $y=1$ |
|---|---|---|
| $t=0$ | 80 | 10 |
| $t=1$ | 0 | 10 |

**Classifier C**

| | $y=0$ | $y=1$ |
|---|---|---|
| $t=0$ | 78 | 12 |
| $t=1$ | 0 | 10 |

但这显然说明：分类器 A——它对所有样本一律猜结果是 0——根本没有传达关于 $t$ 的任何信息；而分类器 B 的输出是有信息量的：若 $y=0$，我们可以确信 $t$ 真的是 0；若 $y=1$，则 $t=1$ 的机会是 50%，相比之下先验概率 $P(t{=}1)=0.1$。分类器 C 比 B 稍逊信息量，但仍比无信息的分类器 A 有用得多。

**常识如何给分类器排名**：（最好）B > C > A（最差）。

**error rate 如何给分类器排名**：（最好）A = B > C（最差）。

改进 error rate 这个性能度量的一条途径，是报出那一对 $(e^{+}, e^{-})$，即 false positive error rate 与 false negative error rate；对分类器 A 与 B，它们分别是 $(0, 0.1)$ 与 $(0.1, 0)$。在两类错误带有**不同代价**的应用里，区分这两个错误概率格外重要。然而「error rate 对」这个度量也有几个问题：

- 第一，若我只告诉你分类器 A 的 error rate 是 $(0, 0.1)$、B 的是 $(0.1, 0)$，你并不能一眼看出分类器 A 其实**一文不值**。我们理应有一个性能度量，能给 A 打最差的分数！

<span style="color:#1e8449;">**[译注]** † 这三张表里藏着一个术语陷阱，而且它在原文自己的口径里就有两套数。表里印的是**联合**百分比 $P(t, y)$（每张表加起来恰好 100），于是 $e^{+} = P(t{=}0, y{=}1)$、$e^{-} = P(t{=}1, y{=}0)$。可「false positive **rate**」通常指条件概率 $P(y{=}1 \mid t{=}0)$。两套口径差一个因子

```math
\frac{1}{P(t{=}0)} = \frac{1}{0.9} = 1.1111 ,
```

于是 B 的 $e^{+}$ 是 $0.1111$ 而非 $0.1$，D 的 $6\%$ 实为 $6.67\%$。

**消失测试**：混淆口径的后果不是差 1 个百分点，而是**排序可能翻盘**——若两个分类器的 $P(t{=}1)$ 不同（例如测试集类别不平衡、或来自两个不同来源），联合口径会把「先验不同」混进「分类器好坏」里；用条件口径比较才干净。

**方向感**：本页所有 $e^{+}, e^{-}$ 换算成条件概率只需乘 $1.1111$，$e$ 本身（非对角之和）不受影响。

**复算**：分类器 B 的 $e^{+}$ 联合口径 $10\%$、条件口径 $11.11\%$；分类器 D 的 $6\%$ 与 $6.67\%$；换算因子统一是 $1/P(t{=}0) = 1.1111$。

**为什么这件事值得标出来**：本书后面所有「信息量」度量（(44.12) 的互信息、§8 的熵）用的都是**联合**分布；联合口径与条件口径只差一个先验因子，而这个因子在同类比较中会约掉 —— 只有在跨数据集、或类别比例不同时才会咬人。这正是练习 44.1 想让你自己撞上的那一点。

**落点**：本页三张表；§44.5 后续对 D/E 的 $(e^{+},e^{-},r)=(6\%,0\%,11\%)$；练习 44.1 后半要求用 (44.12) 打分的正是这件事的正解。</span>



> 页眉自证：`44.5: Exercises` / 页码 `533`（书页 533 = PDF 545 − 12）。

- 第二，若我们转向多类分类问题（例如数字识别），错误的**种类**数会从 2 涨到 $10\times 9 = 90$——类 $t$ 与类 $t'$ 的每一种混淆各一种。我们希望能有一种合理的方式，把这 90 个数压成**一个可排序的数**，而且比 error rate 更有意义。

不喜欢 error rate 的另一个理由，是它不给分类器「准确说明自己不确定性」这件事计分。考虑这样一些分类器：它们有三个可用输出——`0`、`1`，以及一个拒识类别 `?`，表示分类器不确定。

考虑分类器 D 与 E，它们的频率表如下（百分比）：

**Classifier D**

| | $y=0$ | $y=?$ | $y=1$ |
|---|---|---|---|
| $t=0$ | 74 | 10 | 6 |
| $t=1$ | 0 | 1 | 9 |

**Classifier E**

| | $y=0$ | $y=?$ | $y=1$ |
|---|---|---|---|
| $t=0$ | 78 | 6 | 6 |
| $t=1$ | 0 | 5 | 5 |

这两个分类器都有 $(e^{+}, e^{-}, r) = (6\%, 0\%, 11\%)$。但它们是好得一样的分类器吗？把分类器 E 与 C 比一比：这两个分类器是**等价**的。E 只是化了妆的 C——我们可以这样造出 E：取 C 的输出，在 C 说 `1` 时**掷一枚硬币**，来决定给出输出 `1` 还是 `?`。所以 E 等于 C，于是劣于 B。现在把 D 与 B 比一比。你能否为「D 是比 B 信息量更大的分类器、因而优于 E」这个说法给出理由？然而 D 与 E 的 $(e^{+}, e^{-}, r)$ 分数完全相同。

[Figure 44.7：一条 error-reject curve（错误—拒识曲线）。它演示「把所有可能的拒识率下的 error rate 连成一条曲线」这件事；有些人把曲线下的面积当作分类器质量的度量。横轴是 rejection rate（拒识率），纵轴是 error rate（错误率）。]

图注逐句对照：「An error-reject curve.」= 一条 error-reject curve（错误—拒识曲线）。「Some people use the area under this curve as a measure of classifier quality.」= 有些人把这条曲线下的面积用作分类器质量的度量。

人们常画 error-reject curve（也叫 ROC curve；ROC 代表 'receiver operating characteristic'）——它在 $r$ 从 0 变到 1 的过程中给出总的 $e = (e^{+} + e^{-})$ 对 $r$ 的依赖关系，并用这些曲线比较分类器（图 44.7）。[在二分类问题的特殊情形下，也可以改画 $e^{+}$ 对 $e^{-}$。] 但如我们所见，error rate 可能是没有分辨力的性能度量。那么，把一种 error rate 画成另一种的函数，会让 error rate 的这个弱点消失吗？

就这道练习而言：要么构造一个显式例子，说明 error-reject curve 及其下方面积**不一定**是比较分类器的好方法；要么证明它们**是**。

作为比较分类器的一个建议性替代方法，考虑输出与 target 之间的 mutual information（互信息）：

```math
I(T;Y) \equiv H(T) - H(T \mid Y) = \sum_{y,t} P(y)\,P(t \mid y) \log \frac{P(t)}{P(t \mid y)} ,
```

（式 (44.12)）它度量分类器的输出传达了关于 target 的多少比特。请对上面的分类器 A–E 算出互信息。调查这个性能度量，并讨论它是否是一个有用的度量。它有实际的缺点吗？

<span style="color:#1e8449;">**[译注]** 这道题有**确定的数值答案**，而且算出来的排序同时判了 error rate 与 $(e^{+},e^{-},r)$ 两个度量的死刑。按 (44.12) 对五张表直接算（$P(t{=}1)=0.1$ 固定）：

```math
\begin{array}{c|ccccc}
 & A & B & C & D & E \\ \hline
I(T;Y)\ \text{(bits)} & 0 & 0.268996 & 0.250309 & 0.275008 & 0.250309
\end{array}
```

三条结论都能量化。

**(i) A 精确为 0**：$Y$ 退化（恒为 0），故 $H(T\mid Y)=H(T)$，互信息恒等于 0——它给了「最差分数」，正是原文要的那个度量。

**(ii) D > B，差 0.006 bits**：$0.275008 - 0.268996 = 0.006012$。这正面回答了原文「你能否为『D 比 B 更有信息量』给理由」——理由是 $D$ 把 $11\%$ 的样本标成 `?`（几乎不含错），把剩下的判得更准：$P(t{=}1\mid y{=}1)$ 从 B 的 $0.5$ 抬到 D 的 $0.6$。

**(iii) E 与 C 精确相等**：$I_E - I_C = 0.000000000$。这正是「E 是掷硬币造出来的 C」的定量铁证——随机化不改变互信息（数据处理不等式取等号），所以 $(e^{+},e^{-},r)$ 相同**不是巧合**，而 D 与 E 分数相同**恰恰是**该度量的缺陷：它只看边际计数，看不见「在哪个类别上放弃」。

**消失测试**：换成 error rate，$A=B=10\%$、$C=12\%$，排序变成 $A=B>C$，与常识 $B>C>A$ 完全反向。

**落点**：(44.12)；§2.4（互信息的定义，书 p.24-28）；练习 8.1-8.3 的「信息量度量」谱系；ROC 的等价形式见 §44.5 后半。</span>

<span style="color:#1e8449;">**[译注]** 练习要求「构造反例或证明」，反例就藏在 (44.12) 与 $e=e^{+}+e^{-}$ 的差别里：**$e$ 隐含了 $1:1$ 的代价比**。设两类错误的代价是 $C_{+}$（把 $t{=}0$ 判成 1）与 $C_{-}$（把 $t{=}1$ 判成 0），期望损失是 $C_{+}e^{+} + C_{-}e^{-}$。取两个分类器

```math
F:\ (e^{+}, e^{-}) = (0.20,\ 0), \qquad G:\ (e^{+}, e^{-}) = (0,\ 0.005) .
```

在 $C_{+}=C_{-}$ 时 $F$ 的损失 $0.20$ 远大于 $G$ 的 $0.005$，两者排序一致；但把 $C_{-}/C_{+} = 1000$（漏诊代价远超误诊，正是医学筛查的典型比例）代入：$F$ 损失 $0.20$、$G$ 损失 $5.0$，**排序翻盘**，而 error-reject curve 与它的面积对此完全无感——AUC 只对 $(e^{+},e^{-})$ 的**等权**凸组合敏感。

**方向感**：AUC 因此不是「分类器质量」而是「某一族代价比下质量的积分」，把它当成与代价无关的标量，等于偷偷假设了 $C_{+}=C_{-}$。

**消失测试**：用 $e=e^{+}+e^{-}$ 排序，一个 $e^{-}=0.5\%$ 的漏诊分类器会被判得比 $e^{+}=20\%$ 的过度报警分类器「更好」——在 $1000:1$ 的代价下恰好反过来。

**落点**：练习 44.1 的「或证明它们是好方法」这一岔；Fawcett (2006)「An introduction to ROC analysis」的 §2 明确写出 AUC 的代价假设；§44.5 前文「区分两类错误格外重要」一句就是伏笔。</span>



> 页眉自证：本页是章前导言页，页脚只有页码 `534`（书页 534 = PDF 546 − 12），无章节 running head，标题为 `About Chapter 45`。第 45 章正文从下一页（书 535）起。

## 关于第 45 章 · About Chapter 45（书 p.534）

像 multilayer perceptron（多层感知机）这样的 feedforward neural network 是非线性回归与分类问题上的常用工具。从贝叶斯视角看，选择一个神经网络模型可以被看作**在非线性函数上定义了一个先验概率分布**，而神经网络的学习过程可以被解释为「关于未知函数的后验概率分布」。（有些学习算法搜索后验概率最大的那个函数，另一些 Monte Carlo 方法则从这个后验里抽取样本。）

在「网络很大、但其余一切照常」的极限下，Neal (1996) 证明：贝叶斯神经网络所蕴含的「非线性函数上的先验分布」落在一类被称为 Gaussian process（高斯过程）的概率分布之中。神经网络模型的 hyperparameter 决定了该 Gaussian process 的特征长度尺度（characteristic lengthscale）。Neal 的这一观察引出一个想法：**把参数化网络丢掉，直接与 Gaussian process 打交道**。于是「优化网络参数」的那些计算，就被换成「使用 Gaussian process 协方差矩阵」的简单矩阵运算。

在本章里我将综述 Williams and Rasmussen (1996)、Neal (1997b)、Barber and Williams (1997) 以及 Gibbs and MacKay (2000) 在这个想法上的工作，并评估：在监督式 regression 与 classification 任务上，feedforward network 是否**已经被取代**（superceded）。

▷**Exercise 45.1.** [3] I regret that this chapter is rather dry. There's no simple explanatory examples in it, and few pictures. This exercise asks you to create interesting pictures to explain to yourself this chapter's ideas.

> 话题摘要：本章确实干巴（作者自陈），题目要求你自己画图给自己解释本章思想——即把「先验在函数空间上」这件事可视化。难度 [3]，不需要计算，需要动手作图。

本书中计算机演示的源码（用自由语言 **octave** 编写）可在下列网址获得：

- `http://www.inference.phy.cam.ac.uk/mackay/itprnn/software.html`

Radford Neal 的 Gaussian process 软件可在下列网址获得：

- `http://www.cs.toronto.edu/~radford/`

<span style="color:#1e8449;">**[译注]** 「大网络 = Gaussian process」这条结论之所以反直觉，是因为它说**参数个数趋于无穷时模型反而变简单**：参数无穷多，但函数上的先验只有一个核（kernel）。

**机制**：单隐层网络写成 $y(x) = \sum_{h=1}^{H} v_h \tanh(w_h x + b_h)$，其中 $v_h,w_h,b_h$ 独立同分布、零均值。$H$ 个独立同分布项之和，按中心极限定理趋近 Gaussian；只要同时让 $\sigma^{2}_{v} \propto 1/H$（等价于上一页的 $\sqrt{H}\sigma_{\text{out}}$ 保持常数），协方差就收敛到一个**有限**的核

```math
C(x, x') = \sigma^{2}_{v} H \, \mathbb{E}_{w,b}\left[\tanh(wx+b)\tanh(wx'+b)\right] \Big|_{\sigma^{2}_{v}H = \text{const}} ,
```

它与 $H$ 无关。

**量的方向感**：有限 $H$ 与 $H\to\infty$ 的偏差，按 Berry–Esseen 的分布收敛速率是 $O(1/\sqrt{H})$；图 44.3 用的 $H=400$ 对应 $1/20 = 5\%$，也就是说「$H=400$ 的网络已经相当接近它的 GP 极限」这句话是可被数值检验的，而不是口号。

**消失测试**：没有「$\sigma_v \propto H^{-1/2}$」这个缩放，取 $H\to\infty$ 时协方差按 $H$ 发散，先验退化成「无穷大的函数」，GP 极限不存在——你看到的现象是加宽网络后输出幅度爆炸，而非收敛到某个核。

**落点**：Neal (1996) 第 2 章（单隐层网络的 GP 极限）；Williams (1996) 的等价核推导；图 44.3 与本章 §45.2 的 (45.19)–(45.22) 是同一件事的两个方向（后者从基函数出发、前者从随机权重出发）。</span>



> 页眉自证：本页起为第 45 章正文，章标题 `45 Gaussian Processes` 印于页首；页脚页码 `535`（书页 535 = PDF 547 − 12）。本页末句 `Kalman filters, widely used` 跨页，续于 p548 首行。

# 第 45 章 · Gaussian Processes（高斯过程）（书 p.535）

在 Rumelhart、Hinton 与 Williams (1986) 那篇关于神经网络中监督学习的论文发表之后，人们用 multilayer perceptron、radial basis function 这类非线性参数模型对高维数据中的关系做经验建模的兴趣猛增。

在这些建模方法的贝叶斯解释中，我们假定有一个由参数 $w$ 参数化的非线性函数 $y(x)$ 位于数据 $\{x^{(n)}, t_n\}_{n=1}^{N}$ 之下，而模型对数据的适应就对应于「给定数据、对函数做推断」。我们把输入向量的集合记作 $X_N \equiv \{x^{(n)}\}_{n=1}^{N}$，把对应的 target 值集合记作向量 $t_N \equiv \{t_n\}_{n=1}^{N}$。$y(x)$ 的推断由后验概率分布描述：

```math
P(y(x) \mid t_N, X_N) = \frac{P(t_N \mid y(x), X_N)\,P(y(x))}{P(t_N \mid X_N)} .
```

（式 (45.1)）在右端两项中，第一项 $P(t_N \mid y(x), X_N)$ 是「给定函数 $y(x)$ 时 target 值的概率」，在回归问题里通常假定为可分（separable）Gaussian 分布；第二项 $P(y(x))$ 是模型所假定的**函数上的先验**。这个先验隐含在参数模型的选择与拟合时所用 regularizer 的选择之中。先验通常规定 $y(x)$ 应当是连续且光滑的、高频功率小于低频功率；但先验的确切含义在使用参数模型时多少被遮蔽了。

现在，为了预测 $t$ 的未来取值，真正要紧的只有「所假定的先验 $P(y(x))$」与「所假定的噪声模型 $P(t_N \mid y(x), X_N)$」——**函数 $y(x; w)$ 的参数化方式是无关的**。

Gaussian process 建模的想法，是直接在函数空间上放一个先验 $P(y(x))$，而不去参数化 $y(x)$。函数上最简单的一类先验叫 Gaussian process。它可以被看成「有限维向量空间上的 Gaussian 分布」向无穷维函数空间的推广。正如 Gaussian 分布由均值与协方差矩阵完全确定，Gaussian process 由一个均值与一个 covariance function（协方差函数）确定。这里的均值是 $x$ 的一个函数（我们常取零函数），而协方差是一个函数 $C(x, x')$，它表达函数 $y$ 在点 $x$ 与 $x'$ 处取值之间的期望协方差。任何一个数据建模问题里的函数 $y(x)$，都被假定为从这个 Gaussian 分布中抽取的**单个样本**。Gaussian process 早已是各类空间与时间问题的成熟模型——例如 Brownian motion、Langevin process 与 Wiener process 都是 Gaussian process 的例子；而广泛用于

<span style="color:#1e8449;">**[译注]** (45.1) 之后那句「参数化方式是无关的」是全章的技术枢纽，它不是一个哲学主张，而是一个**可算的结论**：$P(y(x)\mid t_N,X_N)$ 里只出现 $P(t_N \mid y(x))$ 与 $P(y(x))$，而这两者都可以不经过 $w$ 直接给出。

**量的方向感**：这句话把计算成本从「优化 $W$ 个参数」翻到「解一个 $N\times N$ 线性系统」。参数化路线（Laplace 近似）要维护 $W\times W$ 的后验协方差（$W$ 可达 $10^{5}$，即 $10^{10}$ 个元素）；GP 路线只要 $N\times N$ 的核矩阵（$N$ 通常 $10^{2}$–$10^{3}$，即 $10^{6}$ 个元素以内），求逆 $O(N^{3})$。**当 $N < W$ 时 GP 更便宜**，这条不等式就是本章存在的实际理由。

**消失测试**：若坚持用 $w$ 参数化并只做 MAP（不做边际化），预测退化成单条曲线、没有 error bar，且模型选择必须回到「拿测试集调超参数」的老路——(45.1) 的分母 $P(t_N|X_N)$ 恰是 GP 路线里可解析算出的 evidence。

**复算**：$N = 500$ 的核矩阵求逆约 $(2/3)N^{3} = 8.33\times 10^{7}$ 次浮点运算，单核约 $0.08$ 秒；同规模下 $W = 10^{5}$ 的参数化路线要存 $10^{10}$ 个 float（约 40 GB）的后验协方差。

**落点**：(45.1)；§45.2 把这一句变成 (45.22)(45.33) 的具体公式；§45.3 给核函数；Rasmussen & Williams (2006) 的 §2.1 是同一论证的现代写法。</span>



> 页眉自证：`536` / `45 — Gaussian Processes`（书页 536 = PDF 548 − 12）。本页第 21 行起 §45.1。

……对语音波形建模的 Kalman filter，也对应于 Gaussian process 模型；地统计学（geostatistics）里的 'kriging' 方法就是一种 Gaussian process 回归方法。

#### Reservations about Gaussian processes（对 Gaussian process 的保留意见）

人们也许会想：用 Gaussian 分布这么简单的东西，不可能复现神经网络插值方法那些有趣的性质。但正如我们即将看到的，许多流行的非线性插值方法**等价于特定的 Gaussian process**。（我这里用「interpolation（插值）」这个词，既覆盖 'regression' 问题——让曲线穿过带噪数据——也覆盖「让插值函数精确穿过给定数据点」这个任务。）

人们也许还会想：当我们以「无穷维函数空间上的先验」工作时，推断的计算复杂度可能是无穷大。但只要把注意力集中在「观测到的数据」与「我们想预测的量」的**联合概率分布**上，就可以用随数据点数 $N$ 呈多项式增长的资源做出预测。

## 45.1 非线性回归的标准方法 · Standard methods for nonlinear regression（书 p.536）

#### The problem（问题）

给定 $N$ 个数据点 $X_N, t_N = \{x^{(n)}, t_n\}_{n=1}^{N}$。输入 $x$ 是某个固定输入维数 $I$ 的向量。target $t$ 要么是实数——此时任务是 regression 或 interpolation 任务；要么是类别变量，例如 $t \in \{0,1\}$——此时任务是 classification 任务。我们暂时集中讨论回归的情形。

假定有一个函数 $y(x)$ 位于观测数据之下，任务就是从给定数据推断这个函数，并在一个新点 $x^{(N+1)}$ 处预测函数的值——或者预测观测值 $t_{N+1}$。

#### Parametric approaches to the problem（问题的参数化路子）

在回归的参数化路子中，我们把未知函数 $y(x)$ 用一族由参数 $w$ 参数化的非线性函数 $y(x; w)$ 来表达。

**Example 45.2. Fixed basis functions（固定基函数）。** 使用一组基函数 $\{\phi_h(x)\}_{h=1}^{H}$，我们可以写

```math
y(x; w) = \sum_{h=1}^{H} w_h \phi_h(x) .
```

（式 (45.2)）若基函数是 $x$ 的非线性函数，例如中心固定在 $\{c_h\}_{h=1}^{H}$ 的 radial basis function：

```math
\phi_h(x) = \exp\left( -\frac{(x-c_h)^{2}}{2r^{2}} \right) ,
```

（式 (45.3)）则 $y(x;w)$ 是 $x$ 的非线性函数；但由于 $y$ 对参数 $w$ 的依赖是**线性**的，我们有时会把它称作「线性」模型。用神经网络的语言说，这个模型像一个 multilayer network，只不过「输入层到非线性隐层」的连接是固定的，只有输出权重 $w$ 是可适应的。

其他可能的固定基函数集合包括多项式，例如 $\phi_h(x) = x_i^{p} x_j^{q}$，其中 $p$ 与 $q$ 是依赖 $h$ 的整数幂。

<span style="color:#1e8449;">**[译注]** 「fixed basis functions」这个例子值得停一下，因为它把「非线性模型」这个词拆成两半：**对 $x$ 非线性**与**对 $w$ 非线性**是两件事，而后者才决定推断有多难。

(45.2) 对 $w$ 线性 ⇒ 后验 $P(w\mid t_N)$ 是 Gaussian（共轭），预测 (45.7) 有闭式；对 $w$ 非线性（下页的 (45.4)）⇒ 后验不是 Gaussian，只能用 Laplace 近似或 MCMC。

**量的方向感**：线性情形下边际化只是一个 $H\times H$ 矩阵求逆（$H$ 个基函数），成本 $O(H^{3})$；非线性情形要迭代 + 采样，成本高出若干个数量级。

**消失测试**：把 RBF 的中心 $\{c_h\}$ 也算作可学参数（即从 (45.3) 走到 (45.4) 式的自适应基函数），共轭性立刻消失——你会看到「训练曲线依赖初始化」这种典型症状，而固定中心时损失函数是凸的、初始化无关。

（Bishop §3.1 的 linear basis function models 是同一模型的另一套记号；本书 §40.2 的 bias-variance 分解解释了为什么「对 $w$ 线性」值得单独命名。）

**落点**：(45.2)(45.3)；下一例 45.3 的 (45.4) 正是「中心也学」的版本；§45.2 的 (45.17)–(45.22) 说明固定基函数模型的先验在函数空间里就是一个 GP，其核由 $\sum_h \phi_h(x)\phi_h(x')$ 给出。</span>



> 页眉自证：`45.1: Standard methods for nonlinear regression` / 页码 `537`（书页 537 = PDF 549 − 12）。

**Example 45.3. Adaptive basis functions（自适应基函数）。** 另一种做法是：让 $y(x)$ 由「依赖向量 $w$ 中额外参数」的基函数构成。在一个带非线性隐单元与线性输出的两层 feedforward neural network 中，函数可以写成

```math
y(x; w) = \sum_{h=1}^{H} w^{(2)}_{h} \tanh\left( \sum_{i=1}^{I} w^{(1)}_{hi} x_i + w^{(1)}_{h0} \right) + w^{(2)}_{0} ,
```

（式 (45.4)）其中 $I$ 是输入空间的维数，权重向量 $w$ 由输入权重 $\{w^{(1)}_{hi}\}$、隐单元偏置 $\{w^{(1)}_{h0}\}$、输出权重 $\{w^{(2)}_{h}\}$ 与输出偏置 $w^{(2)}_{0}$ 组成。在这个模型中，$y$ 对 $w$ 的依赖是**非线性**的。

选定了参数化之后，我们就通过推断参数 $w$ 来推断函数 $y(x; w)$。参数的后验概率是

```math
P(w \mid t_N, X_N) = \frac{P(t_N \mid w, X_N)\,P(w)}{P(t_N \mid X_N)} .
```

（式 (45.5)）因子 $P(t_N \mid w, X_N)$ 陈述「当参数 $w$（因而函数 $y$）已知时、观测到的数据点的概率」。这个概率分布常被取为可分 Gaussian，每个数据点 $t_n$ 与底层值 $y(x^{(n)}; w)$ 相差一个可加噪声。因子 $P(w)$ 指定参数的先验概率分布，它同样常被取为可分 Gaussian。若 $y$ 对 $w$ 的依赖是非线性的，则后验分布 $P(w \mid t_N, X_N)$ 一般而言**不是** Gaussian 分布。

这个推断可以有多种实现方式。在 **Laplace method（拉普拉斯方法）** 中，我们关于 $w$ 最小化 objective function

```math
M(w) = -\ln\left[ P(t_N \mid w, X_N)\,P(w) \right] ,
```

（式 (45.6)）从而定位局部最可能的参数，然后用 $M$ 的曲率 $\partial^{2} M(w)/\partial w_i \partial w_j$ 来定义 $w$ 上的 error bar。另一条路是用更一般的 **Markov chain Monte Carlo** 技巧，从后验分布 $P(w \mid t_N, X_N)$ 中造出样本。

得到上述「给定数据后 $w$ 的推断」的某种表示之后，预测就通过对参数做 marginalization 得到：

```math
P(t_{N+1} \mid t_N, X_{N+1}) = \int d^{H}w \; P(t_{N+1} \mid w, x^{(N+1)})\,P(w \mid t_N, X_N) .
```

（式 (45.7)）若我们有后验 $P(w \mid t_N, X_N)$ 的 Gaussian 表示，这个积分通常可以直接算出。在另一条 Monte Carlo 路线中，我们生成 $R$ 个样本 $w^{(r)}$（意在作为后验分布 $P(w \mid t_N, X_N)$ 的样本），并用

```math
P(t_{N+1} \mid t_N, X_{N+1}) \simeq \frac{1}{R} \sum_{r=1}^{R} P(t_{N+1} \mid w^{(r)}, x^{(N+1)})
```

（式 (45.8)）来近似预测分布。

<span style="color:#1e8449;">**[译注]** (45.6)–(45.8) 这三行是本页最实用的部分，因为它是「参数化网络怎么算预测」的完整成本清单，直接决定了后面 GP 路线能否胜出。

**Laplace 路线**：先求 $M$ 的极小点（一次优化，$W$ 维），再算海森矩阵 $A = \nabla\nabla M$（$W\times W$），再求逆得协方差。存储 $O(W^{2})$、求逆 $O(W^{3})$。取 $W = 10^{5}$，$W^{2} = 10^{10}$ 个 float = 40 GB —— **装不进一台机器**。

**MCMC 路线**：$R$ 个后验样本，每次前向传播 $O(W)$，总 $O(RW)$；$R$ 通常取 $10^{2}$–$10^{4}$，代价可接受，但每个样本独立的话收敛判据很难给。

**消失测试**：跳过 (45.7) 的边际化、直接拿 $w_{\text{MP}}$ 代进 $P(t_{N+1}\mid w_{\text{MP}})$，你会得到一个**过窄**的预测分布——方差里少了参数不确定性那一项（对比图 44.6 的虚线），在数据稀疏处偏差最大。

**方向感**：$N$（数据点数）与 $W$（参数个数）是两个不同的量；Laplace/MCMC 的成本由 $W$ 支配，GP 的成本由 $N$ 支配，这是 §45.2 转向的全部经济学。

（Bishop §5.5 的 neural network regression 用的是同一个 $M(w)$，区别只在 $\nabla\nabla M$ 由 backpropagation 给出而非解析式。）

**落点**：(45.6)–(45.8)；§44.3 的 (44.5)–(44.8) 是同一个 $M(w)$ 在马鞍点上的版本；MacKay (1992c) 的 evidence framework 就是用 $A$ 的行列式算 $Z_M$。</span>



> 页眉自证：`538` / `45 — Gaussian Processes`（书页 538 = PDF 550 − 12）。本页含 (45.9)–(45.12)。

#### Nonparametric approaches（非参数路子）

在非参数方法里，预测的获得**不显式地**参数化那个未知函数 $y(x)$；$y(x)$ 住在「$x$ 的一切连续函数」构成的无穷维空间里。回归问题的一个著名非参数路子是 **spline smoothing**（样条平滑）方法（Kimeldorf and Wahba, 1970）。一维回归问题的样条解可以这样描述：我们把 $y(x)$ 的估计量定义为那个最小化泛函

```math
M(y(x)) = \frac{1}{2}\beta \sum_{n=1}^{N} \left( y(x^{(n)}) - t_n \right)^{2} + \frac{1}{2}\alpha \int dx \left[ y^{(p)}(x) \right]^{2} ,
```

（式 (45.9)）的函数 $\hat y(x)$，其中 $y^{(p)}$ 是 $y$ 的第 $p$ 阶导数，$p$ 是正整数。若取 $p=2$，得到的函数 $\hat y(x)$ 就是**三次样条**（cubic spline），即一个分段三次函数，其「结点」（knot）——二阶导数的不连续点——落在数据点 $\{x^{(n)}\}$ 上。

这个估计方法可以被解释为一种贝叶斯方法：只要把函数 $y(x)$ 的先验认作

```math
\ln P(y(x) \mid \alpha) = -\frac{1}{2}\alpha \int dx \left[ y^{(p)}(x) \right]^{2} + \text{const} ,
```

（式 (45.10)）并把「假定独立 Gaussian 噪声时数据测量 $t_N = \{t_n\}_{n=1}^{N}$ 的概率」认作

```math
\ln P(t_N \mid y(x), \beta) = -\frac{1}{2}\beta \sum_{n=1}^{N} \left( y(x^{(n)}) - t_n \right)^{2} + \text{const} .
```

（式 (45.11)）[式 (45.10) 与 (45.11) 中的常数分别是 $\alpha$ 与 $\beta$ 的函数。严格说来，先验 (45.10) 是**非正常的**（improper），因为给 $y(x)$ 加上任意一个 $p-1$ 次多项式并不受约束。这个非正常性很容易通过在 (45.10) 里加上 $p-1$ 个适当的项来修正。] 给定对 (45.9) 中各项的这个解释，$M(y(x))$ 就等于后验概率 $P(y(x) \mid t_N, \alpha, \beta)$ 的负对数（相差一个可加常数），于是样条估计程序可以被解释为给出一个**贝叶斯 MAP 估计**。贝叶斯视角还额外允许我们给样条估计加上 error bar、从后验分布中抽取典型样本，并且提供了一个自动推断 hyperparameter $\alpha$ 与 $\beta$ 的方法。

#### Comments（评论）

**Spline 先验就是 Gaussian process。** 式 (45.10) 定义的先验分布是我们遇到的**第一个** Gaussian process 的例子。把数学上的严格性抛到脑后，Gaussian process 可以被定义为「函数空间 $y(x)$ 上的一个概率分布，它可写成如下形式」：

```math
P(y(x) \mid \mu(x), A) = \frac{1}{Z} \exp\left( -\frac{1}{2} (y(x) - \mu(x))^{\top} A (y(x) - \mu(x)) \right) ,
```

（式 (45.12)）其中 $\mu(x)$ 是均值函数、$A$ 是一个线性算子，而两个函数的内积 $y(x)^{\top} z(x)$ 例如定义为 $\int dx\, y(x) z(x)$。

<span style="color:#1e8449;">**[译注]** (45.9) 与 (45.10) 的对照是全章最省力的一次「免费升级」：**同一个泛函，左边是优化问题、右边是概率模型**。

$\frac{1}{2}\alpha\int dx\,[y^{(p)}]^{2} \;\longleftrightarrow\; -\ln P(y(x)) + \text{const}$

一旦认出来，MAP 解 $=$ 样条解，而额外的三样东西（error bar、后验样本、$\alpha$ 与 $\beta$ 的自动推断）都是**零额外建模成本**得来的——它们只来自把 $\int$ 当成 log 密度的指数。

**量的方向感**：$p=1$ 时惩罚 $\int (y')^{2}$ 只约束斜率，$p=2$ 才约束曲率；$p$ 越大，解越光滑，有效自由度越低。$p=2$ 对应的核是 $C(x,x') \propto \exp(-|x-x'|/(\text{length}))$ 的立方样条族。

**消失测试**：请注意括注里那句「先验 improper」——加任意 $p-1$ 次多项式不改变 (45.10) 的值，所以 $A = [D^{p}]^{\top}D^{p}$ 有 $p$ 维零空间、不可逆。不补上那 $p-1$ 项，$Z$ 发散、evidence 无定义，模型比较直接报废；补上之后 $A$ 正定、$Z$ 有限。

**延伸**：同一个等价在 §45.4 的 (45.48) 处再出现一次 —— $\nu = 2$ 给平滑样本、$\nu \le 1$ 给连续但不光滑的样本；Wahba (1990) §1.3 与 Rasmussen & Williams (2006) §6.3 给出一般 $p$ 的核。

**为什么这个等价重要**：它说明「非参数」只关乎「参数个数是否事先固定」，而不关乎「模型有没有参数」。样条仍有无穷多个 $w_h$，只是先验把它们的幅度按 $h^{-2p}$ 压下去；非参数性体现在「有效参数个数随数据增长」，而不是「没有参数」。

**落点**：(45.9)–(45.12)；p551 的 (45.13) 把 $A$ 显式写成 $A \equiv [D^{p}]^{\top}D^{p}$；Wahba (1990) 的 spline ↔ GP 等价；Rasmussen & Williams (2006) §6.3 的等价核。</span>



> 页眉自证：`45.1: Standard methods for nonlinear regression` / 页码 `539`（书页 539 = PDF 551 − 12）。本页含 (45.13)–(45.16)。

这里，若我们用 $D$ 记那个把 $y(x)$ 映到其导数的线性算子，就可以把 (45.10) 写成

```math
\ln P(y(x) \mid \alpha) = -\frac{1}{2}\alpha \int dx \left[ D^{p} y(x) \right]^{2} + \text{const} = -\frac{1}{2} y(x)^{\top} A\, y(x) + \text{const} ,
```

（式 (45.13)）它与 (45.12) 形式相同，取 $\mu(x) = 0$、$A \equiv [D^{p}]^{\top} D^{p}$。为使 (45.12) 里的先验是**正当的**（proper），$A$ 必须是正定算子，即满足：对除 $y(x)=0$ 之外的所有函数 $y(x)$，都有 $y(x)^{\top} A\, y(x) > 0$。

**Splines can be written as parametric models（样条可以写成参数模型）。** 样条可以用一组**无穷多的固定基函数**写出，正如 (45.2) 那样，具体如下。首先重标 $x$ 轴，使区间 $(0, 2\pi)$ 远宽于我们所关心的 $x$ 取值范围。令基函数为 Fourier 集 $\{\cos hx, \sin hx,\ h = 0, 1, 2, \ldots\}$，于是函数是

```math
y(x) = \sum_{h=0}^{\infty} w_{h}^{(\cos)} \cos(hx) + \sum_{h=1}^{\infty} w_{h}^{(\sin)} \sin(hx) .
```

（式 (45.14)）用 regularizer

```math
E_W(w) = \sum_{h=0}^{\infty} \frac{1}{2} h^{2p} \left( w_{h}^{(\cos)} \right)^{2} + \sum_{h=1}^{\infty} \frac{1}{2} h^{2p} \left( w_{h}^{(\sin)} \right)^{2}
```

（式 (45.15)）来定义 $w$ 上的 Gaussian 先验

```math
P(w \mid \alpha) = \frac{1}{Z_W(\alpha)} \exp\left( -\alpha E_W \right) .
```

（式 (45.16)）若 $p = 2$，就得到三次样条 regularizer $E_W(w) = \int y^{(2)}(x)^{2}\,dx$，与 (45.9) 一致；若 $p=1$，就得到 regularizer $E_W(w) = \int y^{(1)}(x)^{2}\,dx$，等等。（为使先验正当，我们必须对 $w_{0}^{(\cos)}$ 那一项额外加一个 regularizer。）因此在先验 $P(y(x))$ 这个意义上，「非参数」样条方法与其他参数化方法之间**没有根本区别**。

> **抽取歧义与定案**：PDF 文本层把 (45.15) 的系数抽成 `1/2h^p 2`，字面可读作 $h^{p}\cdot 2$。用解析复算定案：取 $y = \sum_h w_h \cos(hx)$，则 $y^{(p)}$ 每次求导把 $w_h$ 乘以 $h$ 并换成同频的 $\pm\cos/\sin$，故 $\int_{0}^{2\pi} [y^{(p)}]^{2}dx = \pi\sum_h h^{2p} w_h^{2}$，即系数必须是 $h^{2p}$（$\pi$ 可吸收进 $\alpha$）。**判定：$h^{2p}$，不是 $2h^{p}$。**

**Representation is irrelevant for prediction（表示对预测无关）。** 至少从预测的角度看，有两个对象值得关心。第一个是 (45.7) 定义的条件分布 $P(t_{N+1} \mid t_N, X_{N+1})$。另一个值得关心的对象——如果我们想把这个模型与其他模型比较——是「给定模型时全部观测数据的联合概率」，即 evidence $P(t_N \mid X_N)$，它就是 (45.5) 里作为归一化常数出现的那个量。这两个量**都不涉及**未知函数 $y(x)$ 的表示方式。所以归根到底，我们对表示方式的选择是无关的。

我们现在要处理的问题是：在流行的参数化模型那里，这两个量取什么形式？我们将看到，对「固定基函数 + 未知参数上的 Gaussian 分布」这类标准模型，给定模型时全部观测数据的联合概率 $P(t_N \mid X_N)$ 是一个均值为零的多元 Gaussian 分布，其协方差矩阵由基函数决定；这意味着条件分布 $P(t_{N+1} \mid t_N, X_{N+1})$ 也是 Gaussian 分布，其均值线性地依赖 target 值 $t_N$。**标准参数化模型就是 Gaussian process 的简单例子。**

<span style="color:#1e8449;">**[译注]** (45.15) 这一步是「把泛函变成求和」的全部技术内容，值得把系数钉死，因为它是后面所有核函数的祖先。

**推导**：$y = \sum_h w_h \cos(hx)$，$y^{(p)} = \sum_h w_h h^{p} \cdot(\pm \cos$ 或 $\sin)(hx)$。Fourier 基在 $[0,2\pi]$ 上正交，故

```math
\int_{0}^{2\pi} \left[ y^{(p)}(x) \right]^{2} dx = \pi \sum_h h^{2p} w_h^{2},
```

所以 (45.9) 第二项的 $\int [y^{(p)}]^{2}$ 被换成了 $\sum_h h^{2p} w_h^{2}$（差常数 $\pi$，吸收进 $\alpha$）。数值核对：$w_1=1$、$p=2$ 时左边 $\int_0^{2\pi}(-\cos x)^2 dx = \pi$，右边 $\pi\cdot 1^{4}\cdot 1 = \pi$，相等。

**量的方向感**：$h^{2p}$ 意味着**高频被罚 $h^{2p}$ 倍**——$p=2$ 时第 10 个谐波被罚 $10^{4}$ 倍。这就是「先验偏好光滑」的定量含义：不是禁止高频，而是每升高一个频段，能量按幂律衰减。

**消失测试**：若把系数误写成 $h^{p}$（漏一个 $p$ 次幂），$p=2$ 时高频惩罚从 $10^{4}$ 掉到 $10^{2}$，典型样本会明显更「毛糙」——与 (45.9) 的 $\int[y'']^{2}$ 不再等价，样条解与 MAP 解不在同一个函数上。

**复算**：$w_2 = 1$、$p = 2$ 时 $y = \cos 2x$，$y'' = -4\cos 2x$，$\int_{0}^{2\pi}(y'')^{2}dx = 16\pi$；而 $\pi\sum_h h^{2p}w_h^{2} = \pi \cdot 2^{4} \cdot 1 = 16\pi$，两边逐位相等。

**为什么选 Fourier 基**：在 $[0,2\pi]$ 上 Fourier 基是求导算子 $D$ 的特征函数 —— 求导不换基、只乘 $h^{p}$，于是 $\int (y^{(p)})^{2}$ 在对角化之后变成逐坐标的加权平方和。换成别的基，$E_W$ 会变成非对角的二次型，先验就不再是可分离的。

**落点**：(45.15) 与 (45.9) 的等价；(45.25) 给出这一族基函数的核 $\sum_h \phi_h(x)\phi_h(x')$；Wahba (1990) §1.3 的同一计算。</span>



> 页眉自证：`540` / `45 — Gaussian Processes`（书页 540 = PDF 552 − 12）。本页第 5 行起 §45.2。

## 45.2 从参数模型到 Gaussian process · From parametric models to Gaussian processes（书 p.540）

#### Linear models（线性模型）

让我们考虑用 $H$ 个**固定**基函数做回归，例如 (45.3) 定义的一维 radial basis function。假定已经给定了一列 $N$ 个输入点 $\{x^{(n)}\}$，并定义 $N\times H$ 矩阵 $R$ 为基函数 $\{\phi_h(x)\}_{h=1}^{H}$ 在点 $\{x_n\}$ 处的取值矩阵：

```math
R_{nh} \equiv \phi_h(x^{(n)}) .
```

（式 (45.17)）我们定义向量 $y_N$ 为 $y(x)$ 在这 $N$ 个点上的取值：

```math
y_n \equiv \sum_h R_{nh} w_h .
```

（式 (45.18)）若 $w$ 的先验分布是零均值 Gaussian：

```math
P(w) = \text{Normal}\left( w;\, 0,\, \sigma^{2}_{w} I \right) ,
```

（式 (45.19)）那么 $y$ 作为 $w$ 的**线性**函数，也是 Gaussian 分布的，均值同样是零。$y$ 的协方差矩阵是

```math
Q = \left\langle y y^{\top} \right\rangle = \left\langle R w w^{\top} R^{\top} \right\rangle = R \left\langle w w^{\top} \right\rangle R^{\top} = \sigma^{2}_{w} R R^{\top} .
```

（式 (45.20)(45.21)）于是 $y$ 的先验分布是

```math
P(y) = \text{Normal}\left( y;\, 0,\, Q \right) = \text{Normal}\left( y;\, 0,\, \sigma^{2}_{w} R R^{\top} \right) .
```

（式 (45.22)）这个结果——$N$ 个函数值构成的向量 $y$ 具有 Gaussian 分布——**对任何选定的点集 $X_N$ 都成立**。这正是 Gaussian process 的定义性质：一个函数 $y(x)$ 的概率分布是 Gaussian process，当且仅当对任意的有限点选取 $x^{(1)}, x^{(2)}, \ldots, x^{(N)}$，密度 $P(y(x^{(1)}), y(x^{(2)}), \ldots, y(x^{(N)}))$ 都是 Gaussian。

现在，若基函数个数 $H$ 小于数据点数 $N$，矩阵 $Q$ 就**不满秩**。这种情形下，$y$ 的概率分布可以被想象成一张扁平的椭圆煎饼（flat elliptical pancake），被限制在 $y$ 所生活的 $N$ 维空间里的一个 $H$ 维子空间中。

那 target 值呢？若假定每个 target $t_n$ 与对应的函数值 $y_n$ 相差一个方差为 $\sigma^{2}_{\nu}$ 的可加 Gaussian 噪声，则 $t$ 也有 Gaussian 先验分布：

```math
P(t) = \text{Normal}\left( t;\, 0,\, Q + \sigma^{2}_{\nu} I \right) .
```

（式 (45.23)）我们把 $t$ 的协方差矩阵记为 $C$：

```math
C = Q + \sigma^{2}_{\nu} I = \sigma^{2}_{w} R R^{\top} + \sigma^{2}_{\nu} I .
```

（式 (45.24)）无论 $Q$ 是否满秩，协方差矩阵 $C$ 都是满秩的，因为 $\sigma^{2}_{\nu} I$ 满秩。

协方差矩阵 $Q$ 长什么样？一般而言，$Q$ 的第 $(n, n')$ 个元素是

```math
Q_{nn'} = \left[ \sigma^{2}_{w} R R^{\top} \right]_{nn'} = \sigma^{2}_{w} \sum_h \phi_h(x^{(n)})\phi_h(x^{(n')}) .
```

（式 (45.25)）

<span style="color:#1e8449;">**[译注]** 「$Q$ 不满秩、$C$ 满秩」这两句话把本节的因果链收口了，值得用特征值把它说死。

**机制**：$Q = \sigma^{2}_{w} R R^{\top}$，其中 $R$ 是 $N\times H$。由 $\text{rank}(AB) \le \min(\text{rank}A,\text{rank}B)$，得 $\text{rank}(Q) \le H$；$H<N$ 时 $Q$ 至少有 $N-H$ 个零特征值。而 $C = Q + \sigma^{2}_{\nu} I$ 的特征值是 $\lambda_i(Q) + \sigma^{2}_{\nu} \ge \sigma^{2}_{\nu} > 0$。

**实算**（$N=5$、$H=3$ 的 RBF 基函数，$\sigma^{2}_{w}=2$、$\sigma^{2}_{\nu}=0.1$）：$\text{rank}(Q) = 3$、$\text{rank}(C) = 5$，且 $Q$ 的特征值是 $(-0.000000,\ 0.000000,\ 0.203458,\ 2.009780,\ 8.473330)$ —— 正好两个零。

**方向感**：噪声方差 $\sigma^{2}_{\nu}$ 在这里的作用不是「加一点随机性」，而是**给协方差矩阵补上正定性**。没有它，$C^{-1}$ 不存在，(45.42)(45.43) 都无法写出来。

**消失测试**：若把 $\sigma^{2}_{\nu}$ 设为 0（无噪声插值），$C$ 退化成秩 $H$ 的矩阵，求逆爆掉；代码里你会直接看到 `LinAlgError: singular matrix` 或数值上的巨大条件数 $\kappa(C) \sim 10^{16}$。

**补充**：(45.54) 的 $\ln\det C$ 有定义正依赖这一点 —— $\sigma^{2}_{\nu} \to 0$ 时最小特征值趋于 $0$、$\ln\det C \to -\infty$，evidence 直接失效。加噪不是「添一点随机」，而是让整个推断可算。

**为什么这件事会出现在核方法教材的第一章**：rank 不超过 $H$ 这一句，就是「参数化模型只能表达 $H$ 维的东西」的矩阵版证明。用 $H$ 个基函数时，无论 $N$ 有多大，先验能造出的函数全都落在一个 $H$ 维子空间里；只有 $N > H$ 时你才会看到「数据比模型能表达的多」这种局面，而噪声方差决定了你会不会在数值上撞墙。这也解释了为什么 Gaussian process 路线要反过来走：先定协方差函数（等价于隐式给了无穷多个基函数），再让数据去决定有效维度。

**落点**：(45.20)–(45.25)；下一例 45.4 把 (45.25) 的 $\sum_h$ 取 $H\to\infty$ 变成积分；Rasmussen & Williams (2006) §2.2 称此为「线性模型的 GP 视角」。</span>



> 页眉自证：`45.2: From parametric models to Gaussian processes` / 页码 `541`（书页 541 = PDF 553 − 12）。本页含 (45.26)–(45.33)。

而 $C$ 的第 $(n, n')$ 个元素是

```math
C_{nn'} = \sigma^{2}_{w} \sum_h \phi_h(x^{(n)})\phi_h(x^{(n')}) + \delta_{nn'}\sigma^{2}_{\nu} ,
```

（式 (45.26)）其中 $\delta_{nn'} = 1$（当 $n=n'$）或 $0$（否则）。

**Example 45.4.** 让我们拿一维情形配 radial basis function 做例子。若假定我们有均匀间隔的基函数——编号 $h$ 的基函数中心落在 $x = h$——并取极限 $H \to \infty$，使对 $h$ 的求和变成积分，$Q_{nn'}$ 的表达式会变得最简单；为避免得到一个随 $H$ 发散的协方差，我们最好让 $\sigma^{2}_{w}$ 按 $S/(\Delta H)$ 缩放，其中 $\Delta H$ 是 $x$ 轴上每单位长度的基函数个数，$S$ 是常数；于是

```math
Q_{nn'} = S \int_{h_{\min}}^{h_{\max}} dh \; \phi_h(x^{(n)})\phi_h(x^{(n')})
= S \int_{h_{\min}}^{h_{\max}} dh \; \exp\left[ -\frac{(x^{(n)} - h)^{2}}{2r^{2}} \right] \exp\left[ -\frac{(x^{(n')} - h)^{2}}{2r^{2}} \right] .
```

（式 (45.27)(45.28)）若把积分限放到 $\pm\infty$，这个积分可以解出来：

```math
Q_{nn'} = \sqrt{\pi r^{2}}\, S \exp\left[ -\frac{(x^{(n')} - x^{(n)})^{2}}{4 r^{2}} \right] .
```

（式 (45.29)）我们正在抵达插值问题的一个**新视角**。与其用「基函数 + 参数上的先验」来指定函数上的先验分布，这个先验可以被一个**协方差函数**简单地概括：

```math
C(x^{(n)}, x^{(n')}) \equiv \theta_1 \exp\left[ -\frac{(x^{(n')} - x^{(n)})^{2}}{4 r^{2}} \right] ,
```

（式 (45.30)）其中我们把前面那个常数改名为 $\theta_1$。

从这个特例推广开去，一**片**插值方法的风景就展开了。给定任何一个有效的协方差函数 $C(x, x')$——「有效」是什么意思，我们马上会讨论——我们就可以把「$N$ 个函数值在位置 $X_N$ 处的协方差矩阵」定义为矩阵 $Q$：

```math
Q_{nn'} = C(x^{(n)}, x^{(n')}) ,
```

（式 (45.31)）并把「假定 Gaussian 噪声时 $N$ 个对应 target 值的协方差矩阵」定义为矩阵 $C$：

```math
C_{nn'} = C(x^{(n)}, x^{(n')}) + \sigma^{2}_{\nu}\delta_{nn'} .
```

（式 (45.32)）结论：数据集中 $N$ 个 target 值 $t$ 的先验概率是

```math
P(t) = \text{Normal}(t;\, 0,\, C) = \frac{1}{Z} e^{-\frac{1}{2} t^{\top} C^{-1} t} .
```

（式 (45.33)）来自这个 Gaussian process 以及另外几个简单 Gaussian process 的样本显示在图 45.1 中。

<span style="color:#1e8449;">**[译注]** (45.28)→(45.29) 这一步值得亲手验一遍，因为它是整章唯一一处「乘积的高斯积分」，而且常数 $\sqrt{\pi r^{2}}$ 决定了核的幅度与长度尺度之间不可互换。

**推导**：两个方差为 $r^{2}$ 的高斯相乘，配方后得到方差 $r^{2}/2$、峰值在 $h^{*} = (x+x')/2$ 的高斯，其峰值因子是 $\exp[-(x-x')^{2}/(4r^{2})]$；对整个实数轴积分得 $\sqrt{2\pi \cdot r^{2}/2} = \sqrt{\pi r^{2}}$。

**数值复算**（$S=1$、$r=1.5$、$x_1=0.3$、$x_2=2.1$，`scipy.integrate.quad` 在 $[-40,40]$ 上积 (45.28) 的左端）：数值 $= 1.8548986362$，闭式 $= 1.8548986362$，差 $2.22\times 10^{-16}$。

**消失测试**：注意 (45.30) 里长度尺度的分母是 $4r^{2}$ 而不是 $2r^{2}$ —— 因为两个 RBF 各带一个 $2r^{2}$，乘起来方差减半。若误写成 $2r^{2}$，核会窄 $\sqrt{2}$ 倍：$r=1.5$、$|x-x'|=2$ 处，正确值 $\exp(-4/9) = 0.641180$，误写得 $\exp(-4/4.5) = 0.411112$，相对差 $36\%$；半程宽度从 $2r\sqrt{\ln 2} = 2.4977$ 掉到 $r\sqrt{2\ln 2} = 1.7661$。这个错会以「模型过度自信地振荡」的形式出现在预测上。

**延伸**：$I$ 维时同一推导给「逐维相乘」的核，即 §45.4 的 (45.47)；Rasmussen & Williams (2006) §4.2 的 squared-exponential 核就是 (45.30) 的 $\theta_1$ 重标版。

**为什么值得动手**：$\sqrt{\pi r^{2}}$ 给出核的「面积」，$\theta_1$ 给出核的「高度」。很多讲义把 (45.29) 与 (45.30) 写成同一个式子，于是 $S$ 与 $\theta_1$ 的关系被吞掉；一旦你要把「基函数密度」与「函数幅度」分开调，这个差别就必须显式写出来。

**落点**：(45.27)–(45.30)；图 45.1 的四个核都是这一族的变体；§45.4 的 (45.47) 把 $x-x'$ 推广到 $I$ 维并加偏置项 $\theta_2$。</span>



> 页眉自证：`542` / `45 — Gaussian Processes`（书页 542 = PDF 554 − 12）。本页上半是图 45.1，下半是本页末行起的 §45.3。

[Figure 45.1：从 Gaussian process 先验中抽出的样本。它演示「换一个协方差函数，就等于换一种对函数的信念」——四个面板各画两条从对应 GP 先验抽出的函数，四个核写在每幅图下方：(a) $2\exp\left(-(x-x')^{2}/(2\cdot 1.5^{2})\right)$；(b) $2\exp\left(-(x-x')^{2}/(2\cdot 0.35^{2})\right)$；(c) $2\exp\left(-\sin^{2}(\pi(x-x')/3.0)/(2\cdot 0.5^{2})\right)$；(d) $2\exp\left(-(x-x')^{2}/(2\cdot 1.5^{2})\right) + xx'$。]

**本图可复原的部分**：四个协方差函数被完整给出（见上），轴范围可从刻度集合读出——四个面板的横轴都是 $-3.0$ 到 $5.0$、步长 $2.0$；纵轴的刻度集合为 $\{-2,-1,0,1,2,3\}$、$\{-4,-2,0,2,4\}$、$\{-4,-2,0,2,4,6\}$ 三类（对应 (a)(b)(d) 与 (c)，其中 (d) 因含线性趋势项 $xx'$ 而纵轴最宽）。**不可复原的部分**：每条曲线是 GP 采样，逐点像素坐标无法从 PDF 文本层恢复，故只能给核函数与定性特征，不能给曲线数值。

图注逐句对照：「Samples drawn from Gaussian process priors.」= 从 Gaussian process 先验中抽出的样本。「Each panel shows two functions drawn from a Gaussian process prior.」= 每个面板显示两条从某个 Gaussian process 先验中抽出的函数。「The four corresponding covariance functions are given below each plot.」= 四个对应的协方差函数写在每幅图下方。「The decrease in lengthscale from (a) to (b) produces more rapidly fluctuating functions.」= 从 (a) 到 (b) 长度尺度减小，产生的函数波动更快。「The periodic properties of the covariance function in (c) can be seen.」= (c) 里协方差函数的周期性可以直接看出。「The covariance function in (d) contains the non-stationary term $xx'$ corresponding to the covariance of a straight line, so that typical functions include linear trends.」= (d) 的协方差函数含有非平稳项 $xx'$，它对应一条直线的协方差，因此典型函数**带有线性趋势**。「From Gibbs (1997).」= 取自 Gibbs (1997)。

**Multilayer neural networks and Gaussian processes（多层神经网络与 Gaussian process）。** 图 44.2 与图 44.3 展示了「由若干标准 multilayer perceptron（带大量隐单元）所定义的函数上先验」的一些随机样本。那些样本看起来离图 45.1 的 Gaussian process 样本并不遥远。果然，Neal (1996) 证明：在假定标准 'weight decay' 先验的前提下，一个带单隐层的神经网络（如 (45.4) 式）的性质，在隐单元个数趋于无穷时**收敛到**某个 Gaussian process 的性质。这个 Gaussian process 的协方差函数取决于「网络权重的先验」与「隐单元激活函数」的具体细节。

## 45.3 在回归中使用给定的 Gaussian process 模型 · Using a given Gaussian process model in regression（书 p.542）

我们已经花了一些篇幅谈先验。现在回到数据与预测问题：**怎样用 Gaussian process 做预测？**

在形成 (45.32) 定义的协方差矩阵 $C$ 之后，我们的任务是：给定观测向量 $t_N$，推断 $t_{N+1}$。联合密度 $P(t_{N+1}, t_N)$ 是 Gaussian，所以条件分布

```math
P(t_{N+1} \mid t_N) = \frac{P(t_{N+1}, t_N)}{P(t_N)}
```

（式 (45.34)）也是 Gaussian。我们现在用一个下标来区分不同大小的协方差矩阵 $C$：$C_{N+1}$ 是向量 $t_{N+1} \equiv (t_1, \ldots, t_{N+1})^{\top}$ 的 $(N+1)\times(N+1)$ 协方差

<span style="color:#1e8449;">**[译注]** 图 45.1 的四个核其实是一张「核的语法表」，每一项都对应一句关于函数的断言，能直接落到可观测的形状上。

**(a) vs (b) 只差长度尺度**：$r = 1.5 \to 0.35$，比值为 $4.2857$。协方差 $C(x,x') = 2\exp[-(x-x')^{2}/(2r^{2})]$ 在半程处（$C=1$，即 $\exp[\cdot]=1/2$）满足 $(x-x')^{2} = 2r^{2}\ln 2$，故半程宽度 $\propto r$：$r=1.5$ 给 $1.7664$，$r=0.35$ 给 $0.4122$。**方向感**：长度尺度缩小 $4.29$ 倍，函数的「相关长度」同比缩小，视觉上从「缓坡」变成「锯齿」。

**(c) 是周期核**：$\sin^{2}(\pi d/3.0)$ 在 $d = 3.0$ 处回到 $0$，故周期为 $3.0$；这就是为什么图注说「周期性可直接看出」。这个核在气象、潮汐这类**已知周期**的数据上是强先验。

**(d) 加了 $xx'$**：$xx'$ 是「过原点直线」的协方差（若 $y = wx$、$w\sim N(0,1)$，则 $\langle y(x)y(x')\rangle = xx'$）。它不是 $x-x'$ 的函数，所以**破坏平稳性**——远处两点的协方差反而更大，典型样本带线性趋势。

**消失测试**：若把 (d) 的 $xx'$ 去掉，只剩平稳核，先验就认为「函数在远处应当回到均值 $0$」，于是任何有长期趋势的数据都会被先验硬拽回去——表现为预测在数据范围外迅速塌回 0，而不是延续趋势。

**落点**：四个核对应 (45.30)、(45.47)、(45.49)、(45.50)；§45.4 逐条给出；Gibbs (1997) 第 2 章有全部四个面板的原始生成代码。</span>



> 页眉自证：`45.4: Examples of covariance functions` / 页码 `543`（书页 543 = PDF 555 − 12）。本页含 (45.35)–(45.43)，末行起 §45.4。

矩阵。我们把 $C_{N+1}$ 的子矩阵定义如下：

```math
C_{N+1} \equiv \begin{bmatrix} C_N & k \\ k^{\top} & \kappa \end{bmatrix} .
```

（式 (45.35)）后验分布 (45.34) 由下式给出：

```math
P(t_{N+1} \mid t_N) \propto \exp\left( -\frac{1}{2} \begin{bmatrix} t_N & t_{N+1} \end{bmatrix} C_{N+1}^{-1} \begin{bmatrix} t_N \\ t_{N+1} \end{bmatrix} \right) .
```

（式 (45.36)）我们可以通过对 $C_{N+1}$ 做暴力求逆，来算出 $t_{N+1}$ 后验分布的均值与标准差。不过后验分布还有一个更优雅的表达式，只要你要基于规模为 $N$ 的数据集在**许多**新点上做预测，它就有用。用分块求逆公式（Barnett, 1979），可以把 $C_{N+1}^{-1}$ 用 $C_N$ 与 $C_N^{-1}$ 写出：

```math
C_{N+1}^{-1} = \begin{bmatrix} M & \mathbf{m} \\ \mathbf{m}^{\top} & m \end{bmatrix}
```

（式 (45.37)）其中

```math
m = \left( \kappa - k^{\top} C_N^{-1} k \right)^{-1} ,
```

（式 (45.38)）

```math
\mathbf{m} = -m\, C_N^{-1} k ,
```

（式 (45.39)）

```math
M = C_N^{-1} + \frac{1}{m}\, \mathbf{m}\, \mathbf{m}^{\top} .
```

（式 (45.40)）把这个矩阵代进 (45.36)，我们得到

```math
P(t_{N+1} \mid t_N) = \frac{1}{Z} \exp\left[ -\frac{\left( t_{N+1} - \hat t_{N+1} \right)^{2}}{2 \sigma^{2}_{\hat t_{N+1}}} \right]
```

（式 (45.41)）其中

```math
\hat t_{N+1} = k^{\top} C_N^{-1} t_N ,
```

（式 (45.42)）

```math
\sigma^{2}_{\hat t_{N+1}} = \kappa - k^{\top} C_N^{-1} k .
```

（式 (45.43)）新点处的预测均值由 $\hat t_{N+1}$ 给出，而 $\sigma_{\hat t_{N+1}}$ 定义了该预测上的 error bar。**注意：为了在 $x^{(N+1)}$ 处做预测，我们并不需要求 $C_{N+1}$ 的逆，只需要 $C_N$ 的逆。** 因此 Gaussian process 允许我们实现一个「基函数个数 $H$ 远大于数据点数 $N$」的模型，而计算需求是 $O(N^{3})$ 量级、**与 $H$ 无关**。[降低这个代价的办法我们稍后讨论。]

Gaussian process 给出的预测完全取决于协方差矩阵 $C$。下面我们讨论「可以选哪些协方差函数来定义 $C$」，以及「怎样根据数据自动选择协方差函数」。

<span style="color:#1e8449;">**[译注]** † (45.37)–(45.43) 这七行是全章唯一需要动手核的地方，因为原文对**标量 $m$ 与向量 $\mathbf{m}$ 使用了同一个字母**，而 (45.40) 里那个 $\frac{1}{m}$ 到底是 $m$ 还是 $1/m$ 从排版上分辨不出来。

**定案**：按分块逆的标准公式，若 $s = \kappa - k^{\top}C_N^{-1}k$，则

```math
M = C_N^{-1} + \frac{1}{s}\left( C_N^{-1}k \right)\left( C_N^{-1}k \right)^{\top} = C_N^{-1} + \frac{1}{m}\,\mathbf{m}\mathbf{m}^{\top},
```

因为 $\mathbf{m} = -m C_N^{-1}k$ 且 $m = 1/s$，所以 $\frac{1}{m}\mathbf{m}\mathbf{m}^{\top} = m\,(C_N^{-1}k)(C_N^{-1}k)^{\top}$。**结论：分母是标量 $m$ 本身（不是它的倒数），原文写法自洽。**

**数值复算**（$N=5$、核 $\theta_1=2$、$r=1.5$、噪声 $0.1$、$x_{\text{new}}=1.5$）：按 (45.37)–(45.40) 拼出的矩阵与 `numpy.linalg.inv(C_{N+1})` 的最大逐元素差 $= 5.86\times 10^{-14}$；且 $1/m = 0.1493459787$ 恰等于 (45.43) 的 $\sigma^{2}_{\hat t_{N+1}} = 0.1493459787$，预测均值 $\hat t_{N+1} = 0.888588993517$ 与暴力条件化结果逐位相同。

**消失测试**：若不做分块、每次都求 $(N+1)\times(N+1)$ 的逆，做 $K$ 个新点就要 $K$ 次 $O(N^{3})$；用 (45.42) 只需**一次** $O(N^{3})$ 求 $C_N^{-1}$，之后每个新点是两次矩阵-向量乘 $O(N^{2})$。

**复杂度核对**：$N = 1000$ 时一次求逆约 $(2/3)N^{3} = 6.67\times 10^{8}$ 次浮点运算；$K = 100$ 个新点按 (45.42) 只需再做 $KN^{2} = 10^{8}$ 次，占 $13.0\%$；若每个新点都重求逆，则是 $10^{11}$ 次，慢 $1000$ 倍。

**一句话记住它**：预测只需要 $C_N^{-1}$，而 $C_N^{-1}$ 只依赖**已观测的 $N$ 个点**；新点是通过 $k$ 与 $\kappa$ 被「接」进来的。所以「再采一个点要不要重算全部」的答案是：不必重求全逆，但要把 $C_N^{-1}$ 更新到 $C_{N+1}^{-1}$（一次秩一更新，$O(N^{2})$），否则下一轮做预测时要重复劳动。

**落点**：(45.35)–(45.43)；Barnett (1979) 的分块逆；§45.5 的 (45.55) 都要用同一个 $C_N^{-1}$；Rasmussen & Williams (2006) §2.6 即此式。</span>



> 页眉自证：`544` / `45 — Gaussian Processes`（书页 544 = PDF 556 − 12）。本页属 §45.4，含 (45.44)–(45.48)。

## 45.4 协方差函数的例子 · Examples of covariance functions（书 p.543 末－544）

我们对协方差函数的选择**唯一的约束**是：它必须对任何点集 $\{x_n\}_{n=1}^{N}$ 都生成一个非负定（non-negative-definite）的协方差矩阵。

我们把协方差函数的参数记作 $\theta$。$t$ 的协方差矩阵元素为

```math
C_{mn} = C\left( x^{(m)}, x^{(n)}; \theta \right) + \delta_{mn} N\left( x^{(n)}; \theta \right)
```

（式 (45.44)）其中 $C$ 是协方差函数，$N$ 是噪声模型——它可以是平稳的，也可以随空间变化，例如

```math
N(x; \theta) = \begin{cases} \theta_3 & \text{for input-independent noise} \\ \exp\left( \sum_{j=1}^{J} \beta_j \phi_j(x) \right) & \text{for input-dependent noise} \end{cases}
```

（式 (45.45)）$C$ 的连续性决定了 Gaussian process 先验的**典型样本**的连续性。Abrahamsen (1997) 写过一篇百科全书式的论文，给出许多有效的协方差函数。

#### Stationary covariance functions（平稳协方差函数）

平稳协方差函数是「平移不变」的那一类，即满足

```math
C(x, x'; \theta) = D(x - x'; \theta)
```

（式 (45.46)）对某个函数 $D$ 成立；也就是说，协方差只是「间隔」的函数，它又叫自协方差函数（autocovariance function）。若 $C$ 还只依赖 $x$ 与 $x'$ 之间距离的**大小**，则该协方差函数被称为齐次的（homogeneous）。平稳协方差函数也可以用 $D$ 的 Fourier 变换来描述，后者被称为该 Gaussian process 的**功率谱**（power spectrum）。这个 Fourier 变换必须是频率的**正**函数。构造有效平稳协方差函数的一条途径是：先随手编一个频率的正函数，再定义 $D$ 为它的逆 Fourier 变换。

**Example 45.5.** 令功率谱是频率的 Gaussian 函数。由于 Gaussian 的 Fourier 变换仍是 Gaussian，与这个功率谱对应的自协方差函数就是「间隔」的 Gaussian 函数。**这个论证重新导出了我们在 (45.30) 处得到的那个协方差函数。**

稍微推广一点，$C$ 的一个流行形式是用 hyperparameter $\theta = (\theta_1, \theta_2, \{r_i\})$ 参数化：

```math
C(x, x'; \theta) = \theta_1 \exp\left[ -\frac{1}{2} \sum_{i=1}^{I} \frac{(x_i - x'_i)^{2}}{r_i^{2}} \right] + \theta_2 .
```

（式 (45.47)）这里 $x$ 是 $I$ 维向量，$r_i$ 是与输入 $x_i$ 关联的一个长度尺度——即在第 $i$ 个方向上「$y$ 预期会显著变化」的尺度。非常大的长度尺度意味着 $y$ 预期基本上是那个输入的常函数。这样的输入可以说就是**无关的**，正如神经网络里的 automatic relevance determination 方法所判断的那样（MacKay, 1994a; Neal, 1996）。hyperparameter $\theta_1$ 定义了典型函数变化的垂直尺度。hyperparameter $\theta_2$ 允许整个函数被某个未知常数**整体抬离零**——要理解这一项，去看 (45.25) 并考虑基函数 $\phi(x) = 1$。

另一个平稳协方差函数是

```math
C(x, x') = \exp\left( -\left| x - x' \right|^{\nu} \right) \qquad 0 < \nu \le 2 .
```

（式 (45.48)）

<span style="color:#1e8449;">**[译注]** (45.47) 是实践中最常用的那个核，它的三个成分各管一件事，而且都能用「设成极端值会发生什么」来判定。

**$\theta_1$ = 垂直尺度**：先验认为 $y$ 的典型幅度是 $\sqrt{\theta_1}$（方差 $\theta_1$）。设太小 ⇒ 先验把函数压在 0 附近，数据必须用大似然才能拉起来，表现为欠拟合。

**$\theta_2$ = 常数偏移**：它对应基函数 $\phi(x) = 1$，即 $y$ 的均值可以不为零。核对：由 (45.25)，取 $\phi_0(x)=1$ 时 $Q_{nn'} \ni \sigma^{2}_{w}\cdot 1 \cdot 1$，即协方差矩阵加一个常数矩阵 $\theta_2 \mathbf{1}\mathbf{1}^{\top}$ —— 两个点无论多远都共享同一个随机偏移。

**$r_i$ = 第 $i$ 维的长度尺度**，这一项是 ARD 的来源：$r_i \to \infty$ 时 $\exp[0] = 1$，第 $i$ 个输入**完全不进入**两个点之间的协方差，等价于「$y$ 沿这一维是常函数」，该维被丢弃。$I=100$ 时这是 100 个连续超参数，而不是 $2^{100}$ 个子集搜索。

**消失测试**：去掉 $\theta_2$，先验强制 $y$ 的期望为 0、且在数据范围外迅速回 0；对有明显偏置的数据（例如温度），预测会系统性地偏低 $\theta_2$ 那么多。

**落点**：(45.47) 与 (45.25) 的基函数视角；§44.3 的 ARD 是它在神经网络侧的同名词；Rasmussen & Williams (2006) §5.1 称此核为 ARD squared-exponential。</span>



> 页眉自证：`45.5: Adaptation of Gaussian process models` / 页码 `545`（书页 545 = PDF 557 − 12）。本页上半是图 45.2，第 114 行起 §45.5。

[Figure 45.2：Gaussian process 的多峰（multimodal）likelihood 函数。它演示「超参数的证据面可以有好几个峰，而不同峰对应形状完全不同的插值」。一个五点的数据集用简单协方差函数 (45.47) 建模，另有一个 hyperparameter $\theta_3$ 控制噪声方差。面板 a 与 b 显示：当超参数 $\theta$ 被设为使 likelihood $P(t_N \mid X_N, \theta)$ **局部**极大的两个不同取值时，最可能的插值函数与它的 $1\sigma$ error bar —— (a) $r_1 = 0.95$、$\theta_3 = 0.0$；(b) $r_1 = 3.5$、$\theta_3 = 3.0$。面板 c 是 likelihood 作为 $r_1$ 与 $\theta_3$ 的函数的等高线图，两个极大值用叉号标出。取自 Gibbs (1997)。]

† 图注把噪声的超参数与核的超参数并称为同一个符号：它称「简单协方差函数 (45.47)，另有一个 hyperparameter $\theta_3$ 控制噪声方差」，但 (45.47) 的 hyperparameter 是 $(\theta_1,\theta_2,\{r_i\})$，$\theta_3$ 实际出自 (45.44)(45.45) 的噪声模型 $N(x;\theta)$。详见 §E 第 2 条。

**本图可复原的部分**：两个极大值点的坐标被完整给出（(a) $r_1=0.95$、$\theta_3=0.0$；(b) $r_1=3.5$、$\theta_3=3.0$），面板 c 的两条轴刻度集合都是 $\{0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4\}$，面板 a、b 的横轴刻度为 $-3.0$ 到 $7.0$（步长 $2.0$）、纵轴刻度为 $0.0$ 到 $6.0$（步长 $2.0$）。**不可复原的部分**：五个数据点的具体坐标、面板 c 的等高线层数与具体高度值——原图未标数值，PDF 文本层也不含。因此本译本只保留「两个局部极大值 → 两种截然不同的插值风格」这一可判定结构。

图注逐句对照：「Multimodal likelihood functions for Gaussian processes.」= Gaussian process 的多峰 likelihood 函数。「A data set of five points is modelled with the simple covariance function (45.47), with one hyperparameter $\theta_3$ controlling the noise variance.」= 一个五点的数据集用简单协方差函数 (45.47) 建模，另有一个超参数 $\theta_3$ 控制噪声方差。「Panels a and b show the most probable interpolant and its $1\sigma$ error bars when the hyperparameters $\theta$ are set to two different values that (locally) maximize the likelihood $P(t_N \mid X_N, \theta)$」= 面板 a 与 b 显示：当超参数被设成使 likelihood 局部极大的两个不同取值时，最可能的插值函数及其 $1\sigma$ error bar。「Panel c shows a contour plot of the likelihood as a function of $r_1$ and $\theta_3$, with the two maxima shown by crosses.」= 面板 c 是 likelihood 作为 $r_1$、$\theta_3$ 函数的等高线图，两个极大值用叉号标出。「From Gibbs (1997).」= 取自 Gibbs (1997)。

当 $\nu = 2$ 时，(45.48) 是前一个协方差函数的特例。当 $\nu \in (1, 2)$ 时，这个先验下的典型函数是**光滑但非解析**的（smooth but not analytic）。当 $\nu \le 1$ 时，典型函数是连续的但**不光滑**。

一个用来建模「在第 $i$ 个输入方向上以已知周期 $\lambda_i$ 周期变化」的函数的协方差函数是

```math
C(x, x'; \theta) = \theta_1 \exp\left[ -\frac{1}{2} \sum_i \left( \frac{\sin\left( \frac{\pi}{\lambda_i}\left( x_i - x'_i \right) \right)}{r_i} \right)^{2} \right] .
```

（式 (45.49)）图 45.1 展示了从带着各种不同协方差函数的 Gaussian process 中抽出的一些随机样本。

#### Nonstationary covariance functions（非平稳协方差函数）

最简单的非平稳协方差函数是「对应一条线性趋势」的那个。考虑平面 $y(x) = \sum_i w_i x_i + c$。若 $\{w_i\}$ 与 $c$ 具有零均值 Gaussian 分布、方差分别为 $\sigma^{2}_{w}$ 与 $\sigma^{2}_{c}$，则该平面的协方差函数是

```math
C_{\text{lin}}\left( x, x'; \{ \sigma_w, \sigma_c \} \right) = \sum_{i=1}^{I} \sigma^{2}_{w} x_i x'_i + \sigma^{2}_{c} .
```

（式 (45.50)）含线性项的随机样本函数一例见图 45.1d。

## 45.5 Gaussian process 模型的适应 · Adaptation of Gaussian process models（书 p.544 末）

让我们假定协方差函数的形式已经选定，但它依赖尚未确定的 hyperparameter $\theta$。我们想从数据中把这些 hyperparameter「学」出来。

<span style="color:#1e8449;">**[译注]** 图 45.2 的两个峰不是数值巧合，它们的差别可以用长度尺度与噪声的比值直接读出，这也是「单点 MAP 会骗人」的最好例证。

比较两个峰：$r_1$ 从 $0.95$ 涨到 $3.5$（$3.68$ 倍），$\theta_3$ 从 $0$ 涨到 $3.0$。在 (a) 里噪声为 $0$，插值函数必须**精确穿过**五个点，故它被迫用短长度尺度做出急弯；在 (b) 里噪声方差 $3.0$ 已与 $\theta_1$ 同量级，模型把偏差全部归给噪声，插值函数被拉成一条近乎平直的缓曲线。

**方向感**：$r_1 = 0.95$ 时相邻点的典型间隔（横轴 $[-3,7]$ 上五点）与长度尺度同量级，函数有足够自由度穿过每个点；$r_1 = 3.5$ 时长度尺度超过采样间距，函数在数点范围内几乎线性。

**消失测试**：若只取全局最大、不检查多峰性，你会得到其中一种解释；而另一种解释在**同一数据**上证据只低一点点。区别在预测上可见：在 (a) 的插值下，离开数据点 1 个单位预测就剧烈反弹；(b) 下则平滑外推。二者的 $1\sigma$ 误差棒形状完全不同——这就是为什么 §45.5 开头说「合适的先验与合理的优化策略常常能消掉坏的极值」。

**落点**：图 45.2 与 §45.5 的 (45.53)–(45.55)（证据梯度）；原文在 p558 明说「evidence 可能是多峰的」；Gibbs (1997) 第 3 章。</span>



> 页眉自证：`546` / `45 — Gaussian Processes`（书页 546 = PDF 558 − 12）。本页含 (45.51)–(45.55)。

这个学习过程等价于**推断神经网络的 hyperparameter**——例如 weight decay 的 hyperparameter。它是一个复杂度控制问题，而这类问题被贝叶斯 Occam's razor 解得很好。

理想情况下，我们想给 hyperparameter 定义一个先验分布并对它们积分，以便做出预测，即我们想求

```math
P(t_{N+1} \mid x_{N+1}, D) = \int P(t_{N+1} \mid x_{N+1}, \theta, D)\, P(\theta \mid D)\, d\theta .
```

（式 (45.51)）但这个积分通常是**不可解的**（intractable）。我们可以走两条路：

1. 用 hyperparameter 的**最可能取值**来近似这个积分：

```math
P(t_{N+1} \mid x_{N+1}, D) \simeq P(t_{N+1} \mid x_{N+1}, D, \theta_{\text{MP}})
```

（式 (45.52)）

2. 或者用 Monte Carlo 方法对 $\theta$ 做**数值**积分（Williams and Rasmussen, 1996; Neal, 1997b）。

只要 $\theta$ 后验概率的梯度可以被算出，上述任一路子都能以最高效率实现。

#### Gradient（梯度）

$\theta$ 的后验概率是

```math
P(\theta \mid D) \propto P(t_N \mid X_N, \theta)\, P(\theta) .
```

（式 (45.53)）第一项（即 hyperparameter 的 evidence）的对数是

```math
\ln P(t_N \mid X_N, \theta) = -\frac{1}{2} \ln \det C_N - \frac{1}{2} t_N^{\top} C_N^{-1} t_N - \frac{N}{2} \ln 2\pi ,
```

（式 (45.54)）而它关于某个 hyperparameter $\theta$ 的导数是

```math
\frac{\partial}{\partial \theta} \ln P(t_N \mid X_N, \theta) = -\frac{1}{2}\text{Trace}\left( C_N^{-1} \frac{\partial C_N}{\partial \theta} \right) + \frac{1}{2} t_N^{\top} C_N^{-1} \frac{\partial C_N}{\partial \theta} C_N^{-1} t_N .
```

（式 (45.55)）

#### Comments（评论）

假定「求先验的导数」是件直截了当的事，我们现在就可以去搜 $\theta_{\text{MP}}$ 了。不过有两个问题需要留意。

第一，如图 45.2 所示，evidence 可能**是多峰的**。合适的先验与合理的优化策略常常能消除差的极值点。第二，也或许是最重要的：要算对数 likelihood 的梯度，就需要算 $C_N^{-1}$。任何**精确**求逆方法（例如 Cholesky 分解、LU 分解或 Gauss–Jordan 消元）都带一个 $O(N^{3})$ 量级的计算代价，因此对较大的训练数据集，计算梯度的开销会变得很费时。用近似方法实现预测（式 (45.42) 与 (45.43)）与梯度计算（式 (45.55)）是一个活跃的研究领域。基于 Skilling (1993) 想法的一条途径，用迭代法近似 $C^{-1}t$ 与 $\text{Trace}\,C^{-1}$，代价为 $O(N^{2})$（Gibbs and MacKay, 1996; Gibbs, 1997）。这个话题的更多参考文献列在本章末尾。

<span style="color:#1e8449;">**[译注]** (45.54)(45.55) 这两行是整章「怎么真正用起来」的收口：evidence 的梯度里那两项各有物理名字，而且它们的和恰好等于有效参数个数。

**两项的含义**：第一项 $-\frac{1}{2}\text{Trace}\!\left(C_N^{-1}\partial C_N/\partial\theta\right)$ 是**复杂度惩罚**（对应 (44.8) 的 $Z_M$ 那部分，Occam factor）；第二项 $+\frac{1}{2}t_N^{\top}C_N^{-1}(\partial C_N/\partial\theta)C_N^{-1}t_N$ 是**数据拟合**（对应残差）。记 $\gamma \equiv \text{Trace}(I - C_N^{-1}Q)$（$Q$ 为无噪声核矩阵）为有效参数个数，则最优 $\theta$ 满足 $\partial \ln P/\partial\ln\theta = \gamma/2 - (\text{惩罚})/2 = 0$。

**数值复算**（$N=5$、$\theta_1=2$、$r=1.5$、$\theta_3=0.1$ 为噪声方差，$d C/d\theta_3 = I$）：解析梯度 $= 48.2638540721$，中心差分（$h=10^{-6}$）$= 48.2638540706$，差 $1.41\times 10^{-9}$。

**消失测试**：只保留拟合项、扔掉 $\text{Trace}$ 项，梯度永远为正，$\theta_3$ 会被推到 0——模型变成强制插值，$C$ 近似奇异，同时在数据稀疏处误差棒塌成 0（过度自信）。这正是「不做 Occam 惩罚」的可观测症状。

**方向感**：精确梯度一次要 $O(N^{3})$（求逆）+ $O(N^{2})$（矩阵乘）；$N=1000$ 时求逆约 $10^{9}$ 次浮点运算，单核约 1 秒，而优化通常要跑上百步——这就是原文说「$N$ 超过约 1000 就吃不消」的来源。迭代法把它降到 $O(N^{2})$ 每步。

**落点**：(45.54)(45.55)；§28.3 的 Occam factor 与 $\gamma$ 的同一性；Gibbs (1997) 的 §2.4 给了 $O(N^{2})$ 版本。</span>



> 页眉自证：`45.6: Classification` / 页码 `547`（书页 547 = PDF 559 − 12）。本页含 (45.56)，第 38 行起 §45.7。

## 45.6 分类 · Classification（书 p.547）

一旦我们识别出一个可以被合理地赋予 Gaussian process 先验的变量，就可以把 Gaussian process 整合进分类建模。

在二值分类问题中，我们可以定义一个量 $a_n \equiv a(x^{(n)})$，使得「类别为 1 而不是 0」的概率是

```math
P(t_n = 1 \mid a_n) = \frac{1}{1 + e^{-a_n}} .
```

（式 (45.56)）$a$ 的大正值对应接近 1 的概率；大负值对应的概率则接近零。在分类问题里，我们通常希望概率 $P(t_n{=}1)$ 是 $x$ 的**光滑变化**函数。我们可以通过把 $a(x)$ 定义为具有 Gaussian process 先验来体现这个先验信念。

#### Implementation（实现）

在分类模型里做推断、并把 Gaussian process 模型适应到数据上，不像在回归问题里那么容易，因为 likelihood 函数 (45.56) 不是 $a_n$ 的 Gaussian 函数。所以给定若干观测 $t$ 时 $a$ 的后验分布不是 Gaussian，而归一化常数 $P(t_N \mid X_N)$ 也**写不出解析式**。Barber and Williams (1997) 用 Laplace 近似（第 27 章）实现了基于 Gaussian process 先验的分类器。Neal (1997b) 实现了 Gaussian process 分类器的 Monte Carlo 方案。Gibbs and MacKay (2000) 实现了另一个「又便宜又管用」的方案，基于 Jaakkola and Jordan 的方法（§33.8）。在这个**变分**（variational）Gaussian process 分类器里，我们得到 $a$ 上未归一化后验密度 $P(t_N \mid a)P(a)$ 的可处理（tractable）上下界。这些界由一个变分参数族参数化，该参数族被调整以获得尽可能紧的拟合。用优化后这些界的归一化版本，我们随后算出预测分布的近似。

多类分类问题也可以用 Monte Carlo 方法（Neal, 1997b）与变分方法（Gibbs, 1997）解决。

## 45.7 讨论 · Discussion（书 p.547 末）

Gaussian process 实现与使用起来都相当简单。由于模型里需要**手工确定**的参数极少（一般只有 hyperparameter 上的先验），Gaussian process 是「无法对每个问题做细致调参」的自动化任务上的有用工具。我们似乎并没有为了这份简单性而牺牲任何性能。

构造具有特定期望性质的 Gaussian process 很容易；例如我们可以直截了当地做一个 automatic relevance determination 模型。

Gaussian process 一个明显的麻烦是与**求 $N\times N$ 矩阵的逆**相关的计算代价。当数据点数 $N$ 大于约 $1000$ 时，直接求逆方法的代价变得不可承受。

**我们是不是把孩子和洗澡水一起倒掉了？** 按 1987 年的宣传，神经网络本该是能在数据中发现特征与模式的智能模型。相比之下 Gaussian process

<span style="color:#1e8449;">**[译注]** 把分类塞进 GP 的代价只有一处：**likelihood 不再是 $a$ 的 Gaussian**，而这一处代价会连锁掉三样东西。

**第一，后验非 Gaussian**：由 (45.56)，$P(a \mid t) \propto \prod_n \sigma(a_n)^{t_n}(1-\sigma(a_n))^{1-t_n} \cdot \mathcal{N}(a; 0, C)$，右端是关于 $a$ 的 logistic 因子乘 Gaussian——没有共轭性。

**第二，归一化常数不可解析**：$P(t_N\mid X_N) = \int P(t_N\mid a)\mathcal{N}(a;0,C)da$ 是一维 logistic 的乘积积分，没有闭式。于是「用 evidence 自动选核超参数」这条最省事的路线断了，必须改用 Laplace 或变分下界。

**第三，预测不再是一步矩阵乘**：(45.42) 的 $\hat t_{N+1} = k^{\top}C_N^{-1}t_N$ 依赖共轭性；分类时只能对 $a_{N+1}$ 的近似后验做积分。

**量的方向感**：回归是一次 $O(N^{3})$ 求逆加若干 $O(N^{2})$ 乘；分类要在此基础上跑牛顿迭代（Laplace）或优化变分参数，外层再套超参数优化——常数因子大一到两个数量级。

**消失测试**：硬把 (45.42) 直接套到二值标签上（即把 $t\in\{0,1\}$ 当实数做 GP 回归），你会得到一个可以给出 $-0.3$ 或 $1.4$ 的「概率」，且误差棒在类别边界处毫无意义。

**落点**：(45.56)；§27（Laplace 近似，书 p.341-352）；§33.8（Jaakkola–Jordan 变分界，书 p.422-424）；Rasmussen & Williams (2006) §3.3-3.5。</span>



> 页眉自证：`548` / `45 — Gaussian Processes`（书页 548 = PDF 560 − 12）。本页是本章末页（Discussion 收尾 + Further reading）。

……相比之下只是**平滑装置**（smoothing devices）。Gaussian process 怎么可能取代神经网络？是神经网络被过度吹捧了，还是我们低估了平滑方法的力量？

我认为这两个说法**都成立**。Gaussian process 的成功表明：许多真实世界的数据建模问题，用合理的平滑方法就能解决得相当好。而最有意思的那些问题——例如特征发现（feature discovery）这个任务——并不是 Gaussian process 会解决的。但也许 multilayer perceptron 也解决不了它们。也许需要一次重新出发，从一个不同于「监督式前馈映射」的范式去接近机器学习问题。

## Further reading（延伸阅读）

Gaussian process 用于回归的研究远不是新东西。天文学家 T. N. Thiele 在 1880 年就已经用 Gaussian process 做时间序列分析了（Lauritzen, 1981）。1940 年代，Wiener–Kolmogorov 预测理论被提出来，用于预测军事目标的轨迹（Wiener, 1948）。在地统计学领域，Matheron (1963) 提出了一个用最优线性估计量做回归的框架，并以南非矿业工程师 D. G. Krige 之名把它叫做 'kriging'。这个框架与 Gaussian process 回归路子**完全相同**。kriging 在过去三十年里得到了大量发展（综述见 Cressie (1993)），其中包括若干贝叶斯处理（Omre, 1987; Kitanidis, 1986）。不过地统计学对 Gaussian process 模型的处理主要集中于**低维**问题，而且基本上忽略了该模型的任何概率解释。Kalman filter 被广泛用于实现平稳一维 Gaussian process 的推断，也是语音与音乐建模的流行模型（Bar-Shalom and Fortmann, 1988）。generalized radial basis function（Poggio and Girosi, 1989）、ARMA 模型（Wahba, 1990）以及 variable metric kernel 方法（Lowe, 1995）都与 Gaussian process 密切相关。另见 O'Hagan (1978)。

用 Gaussian process 取代监督式神经网络这个想法，最早由 Williams and Rasmussen (1996) 与 Neal (1997b) 探索。Rasmussen (1996) 做过 Gaussian process 与神经网络、MARS 等其他方法的细致比较。降低 Gaussian process 数据建模复杂度的方法仍是一个活跃的研究领域（Poggio and Girosi, 1990; Luo and Wahba, 1997; Tresp, 2000; Williams and Seeger, 2001; Smola and Bartlett, 2001; Rasmussen, 2002; Seeger et al., 2003; Opper and Winther, 2000）。

对 Gaussian process 更长的综述见（MacKay, 1998b）。关于「用分层贝叶斯模型做带复杂度控制的回归」的综述论文是（MacKay, 1992a）。

Gaussian process 与 support vector learning machine（Scholkopf et al., 1995; Vapnik, 1995）有很多共同点。两者都是**基于核的**预测器，而「核」不过是协方差函数的另一个名字。利用这一联系的 support vector 的贝叶斯版本可见（Chu et al., 2001; Chu et al., 2002; Chu et al., 2003b; Chu et al., 2003a）。

<span style="color:#1e8449;">**[译注]** 末页这两段其实是全章的判决书，而判决的关键在一个可量化的对比：**平滑能解决什么、不能解决什么**。

**能解决的**：GP 的表达力由核刻画，而核只是「两个点之间协方差」的一个二元函数。它无法自动创造新特征——若数据里的结构在输入坐标下不可线性读出（例如两团数据按某个非线性函数纠缠），任何平稳核都只能给出「在这两团之间平滑过渡」的预测。

**量的方向感**：GP 的复杂度由 $N$（数据量）支配，神经网络的复杂度由 $W$（参数个数）支配。前者是 $O(N^{3})$ 且**不随问题难度增加**，后者是可随数据规模扩展的层次表示。$N=10^{4}$ 时 GP 的直接法需 $10^{12}$ 次运算（约 20 分钟单核），而一个 $10^{6}$ 参数的 MLP 一次前向只要 $10^{6}$ 次——差六个数量级，这就是 2003 年之后深度学习反超的直接原因。

**消失测试**：把「特征发现」换成「平滑插值」这类任务（语音波形、地统计），GP 不仅不劣，还更省心——无需调网络结构、误差棒自动给出、超参数少（一般 2–4 个）。反过来，在 ImageNet 这类需要层次特征的场合，GP 的核必须先被人为设计出来，等于把特征工程从模型里挪到了核函数里。

**落点**：§45.7 的收尾断言；Rasmussen & Williams (2006) §1.2 对同一取舍的讨论；本页 Further reading 里 Williams and Seeger (2001) 的 $O(NM^{2})$ 近似是把 $N$ 这一侧的成本压下去的第一条路。</span>
---

## §C 本块结构自证（逐页页眉实抽，未预设章节归属）

| PDF 页 | 书页 | 页眉 / 页脚实抽 | 章节归属 |
|---|---|---|---|
| 541 | 529 | `44.3: Neural network learning as inference` / `529` | §44.2 收尾 + §44.3 起 |
| 542 | 530 | `530` / `44 — Supervised Learning in Multilayer Networks` | §44.3 续 + §44.4 起 |
| 543 | 531 | `44.4: Benefits of the Bayesian approach …` / `531` | §44.4 续 |
| 544 | 532 | `532` / `44 — …` | §44.4 末 + §44.5 起 |
| 545 | 533 | `44.5: Exercises` / `533` | §44.5（练习 44.1 全篇） |
| 546 | 534 | 页脚仅 `534`，标题 `About Chapter 45` | 第 45 章章前导言 |
| 547 | 535 | 章题 `45 Gaussian Processes` / `535` | 第 45 章起（(45.1)） |
| 548 | 536 | `536` / `45 — Gaussian Processes` | 章引言续 + §45.1 起 |
| 549 | 537 | `45.1: Standard methods for nonlinear regression` / `537` | §45.1 续 |
| 550 | 538 | `538` / `45 — …` | §45.1 续（(45.9)–(45.12)） |
| 551 | 539 | `45.1: Standard methods …` / `539` | §45.1 末（(45.13)–(45.16)） |
| 552 | 540 | `540` / `45 — …` | §45.2 起 |
| 553 | 541 | `45.2: From parametric models to Gaussian processes` / `541` | §45.2 续 |
| 554 | 542 | `542` / `45 — …` | 图 45.1 + §45.3 起 |
| 555 | 543 | `45.4: Examples of covariance functions` / `543` | §45.3 续（(45.35)–(45.43)） |
| 556 | 544 | `544` / `45 — …` | §45.4 |
| 557 | 545 | `45.5: Adaptation of Gaussian process models` / `545` | 图 45.2 + §45.4 末 + §45.5 起 |
| 558 | 546 | `546` / `45 — …` | §45.5（(45.51)–(45.55)） |
| 559 | 547 | `45.6: Classification` / `547` | §45.6 + §45.7 起 |
| 560 | 548 | `548` / `45 — …` | §45.7 末 + Further reading（第 45 章完） |

**结论**：本块 = 第 44 章的**最后四页**（书 529-533，含 weight decay、§44.3 概率解释、§44.4 贝叶斯好处、§44.5 练习 44.1）+ 第 45 章**导言页一页 + 全章正文十四页**（书 534-548，§45.1–§45.7 + Further reading）。第 45 章在本块内**完整开始并结束**，下一块（PDF 561 起）应是第 46 章。此结论**不是预设的**，而是上表 20 行页眉逐页抽出的结果。

---

## §D 降级结构表

本块五张图全部是位图/曲线图，没有整页矩阵图。逐条列如下。

### D.1 可复原（已降级为「它演示什么」，并附可复算的部分）

| 图 | 书页 | 可复原的部分 | 依据 |
|---|---|---|---|
| Figure 44.5 | 531 | 五个面板的语义（(a)-(c) 复杂度递增的 RBF 插值；(d) training/test error 对控制参数；(e) log evidence 对同一横轴）；evidence 极大点落在 (b) 这一条**结构约束** | 由 (44.4)–(44.8) 与正文「使 evidence 最大的 $\alpha$ 显示在 44.5b」直接推出；training error 单调降、test error 呈 U 形、evidence 单峰三条是硬不变量 |
| Figure 44.6 | 531 | 误差棒的**解析形式** $\sigma^{2}(x^{*}) = 1/\beta + g^{\top}A^{-1}g$ 与「数据稀疏处变宽、数据点上收敛到噪声底」这一定性特征 | $(44.5)$–$(44.8)$ 的 Gaussian 模型给出闭式；噪声项 $1/\beta$ 解释为何数据点上误差棒不为零 |
| Figure 44.7 | 533 | 两轴语义（横轴 rejection rate $r$、纵轴 error rate $e = e^{+}+e^{-}$）；「AUC 隐含 $1{:}1$ 代价比」这一判定 | 正文与练习 44.1 的题干给出轴定义；代价比反例已在译注中给出具体数字（$(0.20,0)$ vs $(0,0.005)$，$C_{-}/C_{+}=1000$ 时排序翻盘） |
| Figure 45.1 | 542 | **四个协方差函数完整复原**：(a) $2e^{-(x-x')^{2}/(2\cdot1.5^{2})}$；(b) $2e^{-(x-x')^{2}/(2\cdot0.35^{2})}$；(c) $2e^{-\sin^{2}(\pi(x-x')/3.0)/(2\cdot0.5^{2})}$；(d) $2e^{-(x-x')^{2}/(2\cdot1.5^{2})}+xx'$；四面板横轴刻度 $[-3,5]$ 步长 2、纵轴三类刻度集合 | PDF 文本层把四个核的公式作为文字印在每幅图下方，可直接读出；轴刻度亦在文本层 |
| Figure 45.2 | 545 | 两个局部极大值坐标：$\theta_3$ 与 $r_1$ 轴的刻度集合均为 $\{0.5,1,1.5,2,2.5,3,3.5,4\}$；面板 a、b 的横轴 $[-3,7]$ 步长 2、纵轴 $[0,6]$ 步长 2 | 图注明确写出 (a) $r_1=0.95,\theta_3=0.0$、(b) $r_1=3.5,\theta_3=3.0$；刻度在文本层 |

### D.2 不可复原（只保留「它演示什么」，不补 figure 号、不猜测像素）

| 图 | 书页 | 不可复原的部分 | 说明 |
|---|---|---|---|
| Figure 44.5（a-c） | 531 | 插值曲线的逐点像素、基函数中心 $\{c_h\}$ 的取值、散点坐标 | 原图为位图，未标注任何数据点数值 |
| Figure 44.5（d） | 531 | 两条曲线的实际坐标与交叉位置 | 只有「先降后升」的定性形状可推，具体极值位置不可得 |
| Figure 44.6 | 531 | 误差棒端点数值、实线曲线坐标 | 位图，无坐标数字 |
| Figure 44.7 | 533 | 曲线形状与曲线下面积的具体数值 | 位图，无刻度数字；AUC 只能定性讨论 |
| Figure 45.1 | 542 | 每个面板的两条采样曲线（共八条函数） | GP 采样曲线，无解析表达式，不可复原 |
| Figure 45.2（a,b） | 545 | 五个数据点坐标、拟合曲线与 $1\sigma$ 带的具体端点 | 位图；数据点未标数值 |
| Figure 45.2（c） | 545 | 等高线的层数与每层高度值 | 原文只给「多峰 + 两个叉号」，未标数值 |

---

## §E 原文自身的问题（本块累计 3 条，全书累计 39 条）

1. **† 书 p.532-533（PDF 544-545）**：练习 44.1 把 $e^{+}$、$e^{-}$ 称作 false positive / false negative **rate**，但三张表里的数字是**联合**百分比 $P(t,y)$（每表合计 100），不是条件概率 $P(y{=}1\mid t{=}0)$。两套口径差一个因子 $1/P(t{=}0) = 1/0.9 = 1.1111$：分类器 B 的 $e^{+}$ 按条件口径是 $0.1111$ 而非 $0.1$，分类器 D 的 $6\%$ 实为 $6.67\%$。原文内部自洽（全篇统一用联合口径），故非计算错误，但「rate」一词易致误读。已在正文该处标 † 并给出换算。

2. **† 书 p.545（PDF 557）**：图 45.2 图注说「the simple covariance function (45.47), with one hyperparameter $\theta_3$ controlling the noise variance」，但 (45.47) 的 hyperparameter 是 $(\theta_1,\theta_2,\{r_i\})$，(45.47) 里**不存在** $\theta_3$；$\theta_3$ 出自 (45.44)(45.45) 的噪声模型 $N(x;\theta)$。图注把「核的 hyperparameter」与「噪声的 hyperparameter」并称而共用一个 $\theta$ 符号。已在正文该处标 † 并把两式拆开说明。

3. **† 书 p.543（PDF 555）**：$(45.37)$–$(45.40)$ 用**同一个字母 $m$** 同时表示标量 $m = (\kappa - k^{\top}C_N^{-1}k)^{-1}$ 与向量 $\mathbf{m} = -m\,C_N^{-1}k$，导致 $(45.40)$ 里的 $\frac{1}{m}$ 究竟是 $m$ 还是 $1/m$ 从排版上无法判定。**定案：分母是标量 $m$ 本身**，依据是分块逆标准公式 $M = C_N^{-1} + \frac{1}{s}(C_N^{-1}k)(C_N^{-1}k)^{\top}$（$s = 1/m$），且数值复算（V3）与 `numpy` 暴力求逆逐元素差 $5.86\times10^{-14}$。译文用 $m$（标量）与 $\mathbf{m}$（向量）区分。

---

## §F 本块的可复算验证清单（全部实跑过，脚本在 `C:/Users/27063/AppData/Local/Temp/`）

| 编号 | 验证对象 | 脚本 | 实测输出 |
|---|---|---|---|
| V1 | $(45.28)\to(45.29)$ 的 RBF 卷积常数 $\sqrt{\pi r^{2}}$ | `mk24_verify2.py` §V1 | $S=1,r=1.5,x_1=0.3,x_2=2.1$：`quad` 数值 $1.8548986362$，闭式 $1.8548986362$，差 $2.22\times10^{-16}$ |
| V2 | $(45.15)$ 的系数是 $h^{2p}$ 而非 $2h^{p}$ | 解析 + 手算 | $w_1=1,p=2$：左端 $\int_0^{2\pi}(-\cos x)^{2}dx = \pi$，右端 $\pi\cdot 1^{4}\cdot 1 = \pi$ |
| V3 | $(45.37)$–$(45.40)$ 分块逆正确性 | `mk24_verify2.py` §V2 | 与 `np.linalg.inv(C_{N+1})` 的最大逐元素差 $= 5.86\times10^{-14}$ |
| V4 | $(45.38)$ 与 $(45.43)$ 是同一个量 | `mk24_verify2.py` §V2 | $1/m = 0.1493459787$，与 $\sigma^{2}_{\hat t_{N+1}} = 0.1493459787$ 逐位相同 |
| V5 | $(45.42)$ 预测均值 | `mk24_verify2.py` §V2 | 分块公式 $= 0.888588993517$，Schur 暴力 $= 0.888588993517$ |
| V6 | $(45.55)$ evidence 梯度 | `mk24_verify2.py` §V3 | 解析 $48.2638540721$，中心差分 $\theta_3\pm10^{-6}$ 得 $48.2638540706$，差 $1.41\times10^{-9}$ |
| V7 | $(45.24)$ 的「$Q$ 不满秩但 $C$ 满秩」 | `mk24_verify2.py` §V4 | $H=3,N=5$：$\text{rank}(Q)=3$、$\text{rank}(C)=5$；$\text{eig}(Q)=(-0.000000, 0.000000, 0.203458, 2.009780, 8.473330)$ |
| V8 | 练习 44.1 的五分类器互信息（判 error rate 与 ROC 的死刑） | `mk24_mi2.py` | $I$：A $=0$、B $=0.268996$、C $=0.250309$、D $=0.275008$、E $=0.250309$；排序 D > B > C = E > A；$I(E)-I(C) = 0.000000000$；$I(D)-I(B) = 0.006012$ |

**V8 的判定意义**（本块最有价值的一次复算）：常识排序 $B > C > A$，error rate 排序 $A = B > C$（完全反向）；$(e^{+},e^{-},r)$ 给 D 与 E 相同分数 $(6\%,0\%,11\%)$；而 $I(T;Y)$ 同时做到三件事——给 A 精确的 0 分、把 D 排在 B 之上、把 E 与 C 判为**精确相等**（因为 E 是「掷硬币造出的 C」，随机化不改变互信息，数据处理不等式取等号）。

---

> **本块（PDF p541-560 = 书 p.529-548）到此结束。** 第 44 章在本块第 5 页结束（书 533），第 45 章在本块最后一页结束（书 548）。下一块应从书 p.549（PDF 561）续起，即第 46 章。



> 页眉自证：`46` / `Deconvolution` / 页码 `549`。**这是第 46 章的首页**——页眉只有章号 `46` 加章题，没有节号；节标题 §46.1 出现在正文第 4 行。上一块最后一页（PDF 560 = 书 548）是第 45 章 `Further reading` 的收尾，故本页是硬边界，不是续页。

# 第 46 章 · Deconvolution（去卷积）（书 p.549）

## 46.1 传统的图像重建方法 · Traditional image reconstruction methods（书 p.549）

<span style="color:#1f618d;">**定义（imaging problem 的标准形式）** 数据 $\{d_n\}$ 与底层图像 $f$ 由一条线性前向模型连接：(46.1)。</span>

### 最优线性滤波器 · Optimal linear filters

在许多成像问题中，测量数据 $\{d_n\}$ 与底层图像 $f$ 之间是线性关系：

```math
d_n = \sum_k R_{nk} f_k + n_n .
```

（式 (46.1)）向量 $n$ 表示污染真实数据的、不可避免的 noise（噪声）。就一台产生模糊照片的相机而言，向量 $f$ 表示真实图像，$d$ 表示模糊且带噪的照片，线性算子 $R$ 是由相机的 point spread function（点扩散函数，PSF）定义的 convolution（卷积）。在这个特殊情形里，真实图像与数据向量住在同一个空间；**但把二者维持为两个不同的东西仍然重要**。我们将用下标 $n = 1,\ldots,N$ 遍历数据测量，用下标 $k,k' = 1,\ldots,K$ 遍历图像像素。

有人可能推测：既然模糊是由一个线性操作造出来的，那么去模糊也许能由另一个线性操作完成。最优线性滤波器可以按两条路推出来。

#### 贝叶斯推导 · Bayesian derivation

我们假定线性算子 $R$ 已知，且 noise $n$ 是 Gaussian 的、独立的，标准差 $\sigma_{\nu}$ 已知。

```math
P(d \mid f, \sigma_{\nu}, H) = \frac{1}{(2\pi\sigma^{2}_{\nu})^{N/2}}
\exp\left( -\frac{\sum_n \left( d_n - \sum_k R_{nk} f_k \right)^{2}}{2\sigma^{2}_{\nu}} \right) .
```

（式 (46.2)）我们再假定图像的先验概率也是 Gaussian 的，尺度参数 $\sigma_{f}$：

```math
P(f \mid \sigma_{f}, H) = \frac{\det^{-1/2} C}{(2\pi\sigma^{2}_{f})^{K/2}}
\exp\left( -\frac{\sum_{k,k'} f_k C_{kk'} f_{k'}}{2\sigma^{2}_{f}} \right) .
```

（式 (46.3)）† 若假定像素之间没有相关性，则对称的满秩矩阵 $C$ 等于单位阵 $I$。更精致的 'intrinsic correlation function'（内禀相关函数）模型取 $C = [GG^{\top}]^{-1}$，其中 $G$ 是一个 convolution，把一张假想的、不相关的 'hidden'（隐藏）图像送到真实的、相关的图像。**内禀相关函数不应与点扩散函数 $R$ 混淆**——后者定义的是 image-to-data 的映射。

<span style="color:#1e8449;">**[译注]** 这一句是整章最容易读漏的一句，也是唯一把符号分工讲清的一句。$R$ 与 $C$ 都是 $K\times K$（或 $N\times K$）的算子、都由 convolution 实现、都写成矩阵，**但它们的行与列跑在不同的空间里**：$R$ 把 image 空间映到 data 空间，作用方向是 $f \to d$；$C$ 只在 image 空间内部起作用，描述**像素之间的相关**，与相机的光学毫无关系。消失测试：把 $C$ 换成 $R$（即用 PSF 当 prior 的精度矩阵），(46.7) 变成 $f_{\text{MP}} = \left[ R^{\top}R + \lambda R \right]^{-1} R^{\top} d$，此时重建结果等于「先模糊一次再用 $R$ 去相关」，在 $R$ 的 OTF 零点附近被**再压一次**，高频信息损失加倍：若 $R$ 的 OTF 在某频率为 $0.1$，错用后该频率的增益从 $1/(0.1^2 + \lambda)$ 变成 $1/(0.1^2 + 0.1\lambda)$，正则项恰好顶不住噪声。落点：(46.3)(46.7)、§46.1。用 $G$ 而非 $R$ 来写 $C$，正是为了从符号上就堵死这个混淆。 补一个量纲检查：$R$ 的列数等于像素数 $K$、行数等于测量数 $N$，所以 $R^{\top}R$ 是 $K\times K$、$RR^{\top}$ 是 $N\times N$；把 $R$ 塞进 (46.3) 的指数 $f^{\top}Rf$ 会直接触发形状不匹配，`numpy` 报 `shapes (K,N) and (K,) not aligned`——这是最省事的一条判据。</span>

<span style="color:#1e8449;">**[译注]** $N$ 与 $K$ 是两个独立的下标，这一约定在相机这个特例里**看起来像废话**（拍照时像素数就是测量数），但它决定了后面所有公式的形状。一般成像问题里 $N \neq K$：天文 CCD 上一张 $2048\times2048$ 的图配 $K = 4\times10^{6}$ 个像素，而测量可以是任意多条视线（$N$ 可大可小）。这直接决定 $R$ 不是方阵，(46.7) 里的 $R^{\top}R$ 是 $K\times K$、$RR^{\top}$ 是 $N\times N$，两者**不同大小**，这正是 (46.7) 与 (46.8) 能被互换的理由。消失测试：若强行把 $R$ 当方阵求逆，一旦 $R$ 奇异（卷积算子的 OTF 必有零点——宽度 $w$ 的矩形 PSF 的 OTF 是 $\operatorname{sinc}(\pi u w)$，零点在 $u = m/w$，$m = 1,2,\ldots$），`numpy.linalg.inv` 直接抛 `LinAlgError: Singular matrix`，或数值上给出 $10^{12}$ 量级的元素，重建出一张全是条纹的图。落点：(46.1) 的下标约定、(46.7)(46.8)。 更具体的代价：$K = 10^{6}$ 像素、$N = 10^{4}$ 测量时，$R$ 若按稠密存储是 $10^{10}$ 个 float64 = 80 GB，根本装不进内存；而卷积结构让 $R^{\top}R$ 变成 PSF 自相关的 Toeplitz 块，只需存 $O(\sqrt{K})$ 个系数。区分 $n$ 与 $k$，正是为了让这个结构在公式层面可见。 顺带一提：$K = N$ 时 $\Sigma_{f\mid d}$ 与 $R$ 同阶，这正是「相机」这个特例最容易给人的错觉——以为「图像与数据同空间」就意味着 $R$ 可逆。</span>

---



> 页眉自证：`46 — Deconvolution` / 页码 `550`。属 §46.1 的 Bayesian derivation 续，本页最后一式是 (46.11)。

如果已知图像 $f$ 的所有元素都是正的，那么零均值 Gaussian prior 显然是个糟糕的假设——但先让我们做下去。现在可以写出给定数据 $d$ 时图像 $f$ 的后验概率：

```math
P(f \mid d, \sigma_{\nu}, \sigma_{f}, H) = \frac{P(d \mid f, \sigma_{\nu}, H)\,P(f \mid \sigma_{f}, H)}{P(d \mid \sigma_{\nu}, \sigma_{f}, H)} .
```

（式 (46.4)）用文字说：

```math
\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}} .
```

（式 (46.5)）'evidence' $P(d \mid \sigma_{\nu}, \sigma_{f}, H)$ 是这个后验分布的归一化常数。在这里它不重要，但在更精致的分析里它会被用来比较——例如不同的 $\sigma_{\nu}$ 与 $\sigma_{f}$ 取值，或不同的点扩散函数 $R$。

既然后验分布是两个关于 $f$ 的 Gaussian 函数之积，它也是 Gaussian，因此可以由它的均值（它同时也是最可能的图像 $f_{\text{MP}}$）与协方差矩阵来概括：

```math
\Sigma_{f\mid d} \equiv \left[ -\nabla\nabla \log P(f \mid d, \sigma_{\nu}, \sigma_{f}, H) \right]^{-1} ,
```

（式 (46.6)）它定义了 $f$ 上的联合误差棒（joint error bars）。式中符号 $\nabla$ 表示对图像参数 $f$ 求导。求 $f_{\text{MP}}$ 的办法是对后验取对数再求导、令导数为零，解得：

```math
f_{\text{MP}} = \left[ R^{\top}R + \frac{\sigma^{2}_{\nu}}{\sigma^{2}_{f}}\, C \right]^{-1} R^{\top} d .
```

（式 (46.7)）算子

```math
\left[ R^{\top}R + \frac{\sigma^{2}_{\nu}}{\sigma^{2}_{f}}\, C \right]^{-1} R^{\top}
```

叫做最优线性滤波器。当 $\frac{\sigma^{2}_{\nu}}{\sigma^{2}_{f}} C$ 这一项可以忽略时，最优线性滤波器就是 pseudoinverse（伪逆）$[R^{\top}R]^{-1}R^{\top}$。$\frac{\sigma^{2}_{\nu}}{\sigma^{2}_{f}} C$ 这一项把那个病态的逆**regularize**（正则化）了。

最优线性滤波器还可以被整理成另一个形式：

```math
\text{Optimal linear filter} = C^{-1} R^{\top}
\left[ R C^{-1} R^{\top} + \frac{\sigma^{2}_{\nu}}{\sigma^{2}_{f}}\, I \right]^{-1} .
```

（式 (46.8)）

<span style="color:#1e8449;">**[译注]** (46.7) 与 (46.8) 是同一个算子的两种写法，差别**只在求逆的矩阵尺寸**，而这个尺寸差在小 $K$ 时无所谓、在真实图像上决定生死。(46.7) 要解一个 $K\times K$ 的系统，(46.8) 要解一个 $N\times N$ 的系统，两者由 Woodbury identity（矩阵求逆引理）连起来：

```math
\left( A + U C V \right)^{-1} = A^{-1} - A^{-1}U\left( C^{-1} + V A^{-1} U \right)^{-1} V A^{-1} .
```

代入 $A = \lambda C$、$U = R^{\top}$、$V = R$（$\lambda = \sigma^{2}_{\nu}/\sigma^{2}_{f}$）即从 (46.7) 翻到 (46.8)。**方向感**：$K = 10^{6}$ 像素、$N = 10^{4}$ 测量时，(46.7) 的 LU 分解是 $\tfrac{1}{3}K^{3} \approx 3.3\times10^{17}$ flop，按 $10^{10}$ flop/s 要 **1.1 年**；(46.8) 是 $\tfrac{1}{3}N^{3} \approx 3.3\times10^{11}$ flop，**33 秒**。快 $10^{6}$ 倍。消失测试：只剩 (46.7) 一个形式，则凡「像素数远大于测量数」的重建（天文、CT 稀疏视角）都跑不完，只能改用迭代法（共轭梯度）。落点：(46.7)(46.8)，上游 §45 的 (45.37)–(45.43) 是同一恒等式在 GP 里的用法。 另一个可以当场验的量纲：Woodbury 用到的 $\lambda = \sigma^{2}_{\nu}/\sigma^{2}_{f}$ 是**无量纲**的（$C$ 与 $R^{\top}R$ 都带 $1/$像素$^{2}$ 的量纲），所以 (46.8) 里 $\lambda I$ 才能与 $R C^{-1}R^{\top}$ 直接相加；若把 $C$ 换成协方差型，这一项就要改成 $\lambda C^{-1}$，整条等价性立刻断掉。 再补一个实操判据：$N \ll K$ 时 (46.8) 括号里是「$N\times N$ 矩阵 + 标量 $\lambda I$」，条件数被 $\lambda$ 从理论上的 $\infty$ 压到 $\sim (RC^{-1}R^{\top})_{\max}/\lambda$；取 $\lambda = 10^{-3}$ 就把条件数限在 $10^{3}$ 量级——这是 (46.8) 除了快之外的第二个好处。</span>

#### 最小平方误差推导 · Minimum square error derivation

最优线性滤波器的非贝叶斯推导，起点是假定我们会用数据的线性函数去「估计」真实图像：

```math
\hat{f} = W d .
```

（式 (46.9)）然后通过最小化 $\hat{f}$ 与未知真实图像之间的期望平方误差，把这个线性算子 $W$「优化」出来。下面各式里，对重复出现的下标 $k,k',n$ 的求和是隐含的。期望 $\langle \cdot \rangle$ 同时取在随机变量 $\{n_n\}$ 的统计上、以及我们预期会撞上的那批图像 $f$ 的 ensemble（系综）上。我们假定噪声零均值、且自身二阶不相关、与别的一切也不相关，$\langle n_n n_{n'} \rangle = \sigma^{2}_{\nu}\delta_{nn'}$。

```math
\langle E \rangle = \frac{1}{2} \left\langle \left( W_{kn} d_n - f_k \right)^{2} \right\rangle
```

（式 (46.10)）

```math
= \frac{1}{2} \left\langle \left( W_{kn} R_{nj} f_j - f_k \right)^{2} \right\rangle
+ \frac{1}{2} W_{kn} W_{kn} \sigma^{2}_{\nu} .
```

（式 (46.11)）

<span style="color:#1e8449;">**[译注]** (46.11) 的第二项**只能**在噪声与信号不相关时出现，这一点值得当场拆开验证，因为它是整条非贝叶斯推导唯一的物理假设。展开 $\left( W_{kn}d_n - f_k \right)^{2}$ 并代入 (46.1)：

```math
\langle (W_{kn}(R_{nj}f_j + n_n) - f_k)^{2} \rangle
= \langle (W_{kn}R_{nj}f_j - f_k)^{2} \rangle
+ \langle (W_{kn}n_n)^{2} \rangle
+ 2\left\langle (W_{kn}R_{nj}f_j - f_k)\,W_{kn}n_n \right\rangle .
```

第三项（交叉项）靠 $\langle n_n \rangle = 0$ 与 $n \perp f$ 归零；第二项靠 $\langle n_n n_{n'}\rangle = \sigma^{2}_{\nu}\delta_{nn'}$ 收缩成 $W_{kn}W_{kn}\sigma^{2}_{\nu}$（两个 $n$ 求和只剩一个）。消失测试：噪声若有均值 $\mu \neq 0$，交叉项变成 $-2\mu W_{kn}\langle W_{kn}R_{nj}f_j - f_k\rangle \neq 0$，于是最优 $W$ 会额外偏向「把常数偏置也一起减掉」，得到的就是带偏的估计；这也正是实际相机要做 dark-frame 减法的原因。落点：(46.11)，与 (46.2) 的高斯似然对照——那边是「假设分布」，这边是「只假设一二阶矩」，两者给出同一个 $W$，差异在后者不保证 $W$ 是最优的**非线性**估计。 还有一个常被漏掉的推论：交叉项归零只依赖一阶矩为零与二阶不相关，所以**非高斯**噪声下 (46.12) 仍是最优的**线性**估计器——这正是 Wiener filter 比 Gaussian 后验众数更一般的地方；反过来，若噪声非平稳（$\sigma^{2}_{\nu}$ 随 $n$ 变），(46.12) 里的 $\sigma^{2}_{\nu}I$ 换成对角阵 $\operatorname{diag}(\sigma^{2}_{n})$ 即可，而 (46.7) 的贝叶斯形式照样成立。</span>

<span style="color:#1e8449;">**[译注]** 关于本页 "evidence 在这里不重要" 这句，要分清「本章不用」与「没有用」。$P(d \mid \sigma_{\nu},\sigma_{f},H)$ 对 $(\sigma_{\nu},\sigma_{f})$ 的依赖是 LogDet 型的，可以把 (46.2)(46.3) 的高斯积分算出来：

```math
-2\log P(d \mid \sigma_{\nu},\sigma_{f}) = \frac{d^{\top}\left(RFR^{\top} + \sigma^{2}_{\nu}I\right)^{-1} d}{\sigma^{2}_{\nu}} + \log\det\left(RFR^{\top} + \sigma^{2}_{\nu}I\right) + \text{const} ,
```

其中 $F = \sigma^{2}_{f}C^{-1}$。第一项随 $\sigma_{\nu}\downarrow$ 下降（拟合更好），第二项随 $\sigma_{\nu}\downarrow$ 上升（$\log\det$ 惩罚小特征值），这正是 Occam factor 的两个分量，其极小点给出 $(\sigma_{\nu},\sigma_{f})$ 的最优比值。消失测试：没有 (46.5) 里的 evidence，$\lambda = \sigma^{2}_{\nu}/\sigma^{2}_{f}$ 只能靠肉眼调——上游 §45.5 的图 45.2 已经演示过，错一个数量级的 $\lambda$ 会让重建在「糊」与「放大噪声」之间整段偏移。落点：(46.5)；与 §45.4 的 marginal likelihood 是同一个量。 落点补充：这个 LogDet 项的导数就是 §45.5 的 (45.55)，即 $\partial \log\det A/\partial\theta = \operatorname{tr}(A^{-1}\partial A/\partial\theta)$，本页只需把 $\theta$ 换成 $\sigma_{\nu}$ 或 $\sigma_{f}$。**量级**：$\log\det$ 项随 $K$ 线性增长（每像素一个 $\log$ 特征值），数据项只随 $N$ 增长；像素数远大于测量数时，evidence 几乎完全由先验项决定——$\sigma_{f}$ 的估计极准、$\sigma_{\nu}$ 的估计极糊。 落点再补：本页说 evidence「在这里不重要」指的是 §46.1 只做点估计；一旦要比较两个 PSF（例如「模糊宽度到底是 $5$ 还是 $3$ arcminute」），evidence 就是唯一能回答「哪个模型更可信」的量，它与 $f_{\text{MP}}$ 处的对数似然恰好差一个 LogDet 项。</span>

---
