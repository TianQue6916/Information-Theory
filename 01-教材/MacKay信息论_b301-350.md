<!-- 书页 301–350｜来源：B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->



## 书内 p301 · 误差棒 · 例 22.2 / 例 22.3

[Figure 22.1：高斯参数 likelihood 的三组视图——(a1)(a2) 曲面图与等高线图；(b) 不同 $\sigma$ 下 $\mu$ 的后验；(c) 不同固定 $\mu$ 下 $\sigma$ 的后验（画成 $\ln\sigma$ 上的密度）]

**Figure 22.1（图注）** 高斯分布各参数的 likelihood 函数。(a1, a2) 分别是 $\log$ likelihood 关于 $\mu$ 与 $\sigma$ 的曲面图与等高线图；该 $N = 5$ 点数据集有均值 $\bar{x} = 1.0$、$S = \sum(x-\bar{x})^2 = 1.0$。(b) 在若干 $\sigma$ 取值下 $\mu$ 的后验概率。(c) 在若干固定 $\mu$ 下 $\sigma$ 的后验概率（画成关于 $\ln \sigma$ 的密度）。

**图 22.1 的坐标读数（原书轴标注）**：(a1) 横轴 $\mu$ 为 $0$ 到 $2$、纵轴 $\sigma$ 为 $0.2$ 到 $1$、竖轴 $0$ 到 $0.06$；(a2) 横轴 $\mu$ 为 $0$ 到 $2$、纵轴 $\sigma$ 为 $0.1$ 到 $1$；(b) 横轴 $\mu$ 为 $0$ 到 $4.5$、纵轴（Posterior）为 $0$ 到 $2$，三条曲线标注 `sigma=0.2` / `sigma=0.4` / `sigma=0.6`；(c) 横轴为 $\sigma$ 的 $0.2$ 到 $2$、纵轴为密度 $0$ 到 $0.09$，三条曲线标注 `mu=1` / `mu=1.25` / `mu=1.5`。**曲线的具体形状（峰位、峰高）不可从文字层复原，此处不臆造。**

如果我们在最大值附近对 log likelihood 做 Taylor 展开，就能给最大似然参数定义**近似的误差棒（error bars）**：我们用一个二次近似，来估计「从最大似然参数点出发可以走多远，likelihood 才会掉到某个标准倍数——例如 $e^{1/2}$ 或 $e^{4/2}$」。在一种特殊情形下——likelihood 恰好是参数的**高斯函数**——这个二次近似是**精确的**。

<span style="color:#b9770e;">**Example 22.2（例）**</span> 求 log likelihood 对 $\mu$ 的二阶导数，并在给定数据与 $\sigma$ 的情况下求出 $\mu$ 的误差棒。

**解答**

```math
\frac{\partial^2}{\partial \mu^2} \ln P = -\frac{N}{\sigma^2} .
```

（22.7）◊

把这个曲率与「一个标准差为 $\sigma_\mu$ 的高斯分布在 $\mu$ 上的对数曲率」——即 $\exp(-\mu^2/(2\sigma_\mu^2))$ 的曲率 $-1/\sigma_\mu^2$——相比较，可以推出 $\mu$ 的误差棒（由 likelihood 函数导出）是

```math
\sigma_\mu = \frac{\sigma}{\sqrt{N}} .
```

（22.8）

这些误差棒有这样的性质：在两个点 $\mu = \bar{x} \pm \sigma_\mu$ 处，likelihood 比它的最大值小了 $e^{1/2}$ 倍。

<span style="color:#b9770e;">**Example 22.3（例）**</span> 已知均值 $\mu$、给定数据 $\{x_n\}_{n=1}^{N}$，求高斯的**最大似然标准差** $\sigma$；再求 log likelihood 对 $\ln\sigma$ 的二阶导数，以及 $\ln\sigma$ 的误差棒。

**解答** likelihood 对 $\sigma$ 的依赖是

```math
\ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma) = -N \ln(\sqrt{2\pi}\,\sigma) - \frac{S_{\text{tot}}}{2\sigma^2} ,
```

（22.9）

其中 $S_{\text{tot}} = \sum_n (x_n - \mu)^2$。要找 likelihood 的极大值，我们可以对 $\ln\sigma$ 求导。［当 $u$ 是一个**尺度型**变量时，通常对 $\ln u$ 求导比直接对 $u$ 求导更干净；这里用到 $\mathrm{d}u^n/\mathrm{d}(\ln u) = n u^n$。］

---



## 书内 p302 · 例 22.3 续 · §22.2 高斯混合的最大似然

```math
\frac{\partial \ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma)}{\partial \ln \sigma} = -N + \frac{S_{\text{tot}}}{\sigma^2}
```

（22.10）

这个导数等于零当

```math
\sigma^2 = \frac{S_{\text{tot}}}{N} ,
```

（22.11）

也就是

```math
\sigma = \sqrt{\frac{\sum_{n=1}^{N}(x_n - \mu)^2}{N}} .
```

（22.12）

二阶导数是

```math
\frac{\partial^2 \ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma)}{\partial (\ln \sigma)^2} = -\frac{2 S_{\text{tot}}}{\sigma^2} ,
```

（22.13）

而在 $\sigma^2$ 取最大似然值时，它等于 $-2N$。所以 $\ln\sigma$ 的误差棒是

```math
\sigma_{\ln \sigma} = \frac{1}{\sqrt{2N}} .
```

（22.14）◊

<span style="color:#7d3c98;">**Exercise 22.4**</span> [exercise] *Show that the values of $\mu$ and $\ln \sigma$ that jointly maximize the likelihood are: $\{\mu, \sigma\}_{\mathrm{ML}} = \{\bar{x},\ \sigma_N = \sqrt{S/N}\}$, where*

```math
\sigma_N \equiv \sqrt{\frac{\sum_{n=1}^{N}(x_n - \bar{x})^2}{N}} .
```

（22.15）

> [exercise 摘要] 联合最大化时要证两件事：均值仍取 $\bar{x}$（不因 $\sigma$ 变化），而 $\sigma$ 的分母是 $N$ 不是 $N-1$——**最大似然是有偏的**，这正是书内 p306 那句「$\sigma_N$ is a biased estimator」的来源。

## 22.2 Maximum likelihood for a mixture of Gaussians（高斯混合的最大似然）

现在我们来推导一个把高斯混合拟合到一维数据的算法。事实上，这个算法**重要到你应该亲手推一遍**——亲爱的读者，这个算法由你来推。请做完下面这道题。

<span style="color:#7d3c98;">**Exercise 22.5**</span> [exercise] *A random variable $x$ is assumed to have a probability distribution that is a mixture of two Gaussians,*

```math
P(x \mid \mu_1, \mu_2, \sigma) = \left[\sum_{k=1}^{2} p_k \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(\frac{-(x-\mu_k)^2}{2\sigma^2}\right)\right] ,
```

（22.16）

*where the two Gaussians are given the labels $k = 1$ and $k = 2$; the prior probability of the class label $k$ is $\{p_1 = 1/2,\ p_2 = 1/2\}$; $\{\mu_k\}$ are the means of the two Gaussians; and both have standard deviation $\sigma$. For brevity, we denote these parameters by $\theta \equiv \{\{\mu_k\}, \sigma\}$.*

*A data set consists of $N$ points $\{x_n\}_{n=1}^{N}$ which are assumed to be independent samples from this distribution. Let $k_n$ denote the unknown class label of the $n$th point.*

*Assuming that $\{\mu_k\}$ and $\sigma$ are known, show that the posterior probability of the class label $k_n$ of the $n$th point can be written as*

```math
\begin{aligned}
P(k_n = 1 \mid x_n, \theta) &= \frac{1}{1 + \exp\left[-(w_1 x_n + w_0)\right]} \\
P(k_n = 2 \mid x_n, \theta) &= \frac{1}{1 + \exp\left[+(w_1 x_n + w_0)\right]} ,
\end{aligned}
```

（22.17）

> [exercise 摘要] 等权两高斯下，类标签的后验恰好是 $x_n$ 的 **logistic 函数**，斜率 $w_1 = (\mu_1 - \mu_2)/\sigma^2$、截距 $w_0 = (\mu_2^2 - \mu_1^2)/(2\sigma^2)$。这一步是全书后面「soft K-means 的 responsibilities 就是后验」的**代数源头**——第 20 章凭空写下的 soft-min，在这里被证成 logistic 后验。

---



## 书内 p303 · 练习 22.5 续 · §22.3 对 soft K-means 的增强

*（承上页，Exercise 22.5 续）* 并给出 $w_1$ 与 $w_0$ 的表达式。

现在假设 means $\{\mu_k\}$ **未知**，我们想从数据 $\{x_n\}_{n=1}^{N}$ 中把它们推断出来（标准差 $\sigma$ 已知）。本题余下部分，我们要推导一个迭代算法，用来找出使 likelihood 最大的 $\{\mu_k\}$：

```math
P(\{x_n\}_{n=1}^{N} \mid \{\mu_k\}, \sigma) = \prod_n P(x_n \mid \{\mu_k\}, \sigma) .
```

（22.18）

设 $L$ 表示 likelihood 的自然对数。证明 log likelihood 对 $\mu_k$ 的导数为

```math
\frac{\partial}{\partial \mu_k} L = \sum_n p_{k \mid n} \frac{(x_n - \mu_k)}{\sigma^2} ,
```

（22.19）

其中 $p_{k\mid n} \equiv P(k_n = k \mid x_n, \theta)$，就是上面 (22.17) 里出现过的那个量。

再证明：**忽略** $\frac{\partial}{\partial \mu_k} P(k_n = k \mid x_n, \theta)$ 这些项之后，二阶导数近似为

```math
\frac{\partial^2}{\partial \mu_k^2} L = -\sum_n p_{k \mid n} \frac{1}{\sigma^2} .
```

（22.20）

由此证明：从初始状态 $\mu_1, \mu_2$ 出发，一步近似的 **Newton–Raphson（牛顿–拉夫森）** 更新会把这些参数更新到 $\mu_1', \mu_2'$，其中

```math
\mu_k' = \frac{\sum_n p_{k \mid n} x_n}{\sum_n p_{k \mid n}} .
```

（22.21）

［最大化 $L(\mu)$ 的 Newton–Raphson 方法把 $\mu$ 更新为 $\mu' = \mu - \left[\frac{\partial L}{\partial \mu} \big/ \frac{\partial^2 L}{\partial \mu^2}\right]$。］

[Figure 22.2 位置：原书在此排一个 32 点的一维数据集（横轴 0 到 6，纵轴无意义），供下面这一小问使用]

**图的数据读数**：原书只在横轴标了 `0 1 2 3 4 5 6`，纵轴无标注；**32 个点的具体坐标在 PDF 文字层中不可复原，故不编造。**

*（Exercise 22.5 续）* 假设 $\sigma = 1$，针对上面所示的数据集，画出 likelihood 作为 $\mu_1$ 与 $\mu_2$ 的函数的等高线草图。该数据集由 **32 个点**构成。描述你草图中的那些峰，并标出它们的宽度。

请注意：你刚刚推导出的这个「最大化 likelihood」的算法，**与 §20.4 的 soft K-means 算法完全相同**。既然现在清楚了「聚类可以看成 mixture-density-modelling（混合密度建模）」，我们就有能力为 K-means 算法推导出一系列**增强版**，用来修掉我们早先指出的那些毛病。

## 22.3 Enhancements to soft K-means（对 soft K-means 的增强）

Algorithm 22.2 展示的 soft K-means 版本，对应的建模假设是：**每个簇是一个球状高斯（spherical Gaussian），各自有自己的宽度**（每簇有自己的 $\beta^{(k)} = 1/\sigma_k^2$）。这个算法会**自行更新**各簇的 lengthscale $\sigma_k$。算法里还引入了簇权重参数 $\pi_1, \pi_2, \ldots, \pi_K$，它们同样自我更新，从而能准确建模那些**权重不等**的簇。该算法在图 22.3 中对两个我们见过的数据集作了演示。第二个例子表明——



## 书内 p304 · soft K-means version 2 与 version 3

**Assignment step（分配步）** responsibilities 是

```math
r_k^{(n)} = \frac{\pi_k \dfrac{1}{\left(\sqrt{2\pi}\,\sigma_k\right)^{I}} \exp\left(-\dfrac{1}{\sigma_k^2}\, d(m^{(k)}, x^{(n)})\right)}{\sum_{k'} \pi_{k'} \dfrac{1}{\left(\sqrt{2\pi}\,\sigma_{k'}\right)^{I}} \exp\left(-\dfrac{1}{\sigma_{k'}^2}\, d(m^{(k')}, x^{(n)})\right)} ,
```

（22.22）

其中 $I$ 是 $x$ 的**维数**。

† **原文自身的问题**：(22.22) 的分母在原书里也印成了 $\pi_k$，按定义（对 $k'$ 求和、与分子同形）应为 $\pi_{k'}$；本书其他几处求和号下的下标混乱同理。

**Update step（更新步）** 每个簇的参数 $m^{(k)}$、$\pi_k$ 与 $\sigma_k^2$，都被调整到「它所负责的那些数据点」上去。

```math
m^{(k)} = \frac{\sum_n r_k^{(n)} x^{(n)}}{R^{(k)}}
```

（22.23）

```math
\sigma_k^2 = \frac{\sum_n r_k^{(n)} \left(x^{(n)} - m^{(k)}\right)^2}{I\, R^{(k)}}
```

（22.24）

```math
\pi_k = \frac{R^{(k)}}{\sum_k R^{(k)}}
```

（22.25）

其中 $R^{(k)}$ 是 mean $k$ 的总 responsibility：

```math
R^{(k)} = \sum_n r_k^{(n)} .
```

（22.26）

<span style="color:#1a5276;">**Algorithm 22.2 · The soft K-means algorithm, version 2**</span>

[Figure 22.3：soft K-means 版本 2（$K=2$）在两个老数据集上的迭代过程：(a) 图 20.3 的 40 点数据集，快照 $t = 0, 1, 2, 3, 9$；(b) 图 20.5 的「小 n、大 n」数据集，快照 $t = 0, 1, 10, 20, 30, 35$]

**Figure 22.3（图注）** Soft K-means algorithm（$K = 2$），分别施用于 (a) 图 20.3 的 40 点数据集；(b) 图 20.5 的「小 n、大 n」数据集。**各快照里 means 的具体坐标不可从文字层复原，只保留快照时刻。**

若允许簇是**轴对齐**（axis-aligned）的高斯、方差可以各不相同，则把分配规则 (22.22) 与方差更新规则 (22.24) 换成 Algorithm 22.4 中列出的 (22.27) 与 (22.28)：

```math
r_k^{(n)} = \frac{\pi_k \dfrac{1}{\prod_{i=1}^{I}\sqrt{2\pi}\,\sigma_i^{(k)}} \exp\left(-\sum_{i=1}^{I}\frac{\left(m_i^{(k)} - x_i^{(n)}\right)^2}{2\left(\sigma_i^{(k)}\right)^2}\right)}{\sum_{k'}\left(\text{numerator, with } k' \text{ in place of } k\right)} ,
```

（22.27）

```math
\left(\sigma_i^{(k)}\right)^2 = \frac{\sum_n r_k^{(n)} \left(x_i^{(n)} - m_i^{(k)}\right)^2}{R^{(k)}} .
```

（22.28）

<span style="color:#1a5276;">**Algorithm 22.4 · The soft K-means algorithm, version 3**</span>（对应「轴对齐高斯」这一模型）

<span style="color:#1e8449;">**[译注]** 从 (20.7) 走到 (22.22) 这四行，让 soft K-means **不再是启发式**，而是球状高斯混合的 EM 特例，判别标志是分子多出的 $\pi_k$ 与 $(\sqrt{2\pi}\sigma_k)^{-I}$。**消失测试**：删掉 $\pi_k$（强制等权）后 (22.25) 失去意义，图 22.6 的「小 n 大 n」数据上小簇会被大簇整块吞掉——$\pi_k$ 是唯一能表达「这簇本就只占 20% 的点」的量；删掉归一化因子（强制同宽）后 (22.24) 与分配规则脱钩，图 22.5 的两支雪茄必然拟合失败，退化为全局共享 $\beta$ 的第 20 章旧版。**代价方向的对比**：硬分配要枚举的是 $K^{N}$ 种标号，$K=2$、$N=40$ 即 $2^{40}\approx 10^{12}$ 种；EM 每步只算 $N K = 80$ 个 responsibilities，从 $10^{12}$ 降到几十次——这就是「用连续松弛换掉组合爆炸」的具体价钱。**方向感**：归一化因子是 $\sigma_k^{-I}$，$I=10$ 时宽度差两倍即带来 $2^{10}\approx 10^{3}$ 的密度差。**落点**：§22.3、Algorithm 22.2 / 22.4；对照 *PRML* §9.2.2。还有一个方向的价钱要说清：EM 只保证收敛到**局部**极大，$K=4$ 时图 22.7 那种极小簇正是局部极优解之一，所以「便宜」换来的是多峰与初值敏感。</span>

---



## 书内 p305 · 图 22.5 / 22.6 · §22.4 Maximum likelihood 的致命缺陷

[Figure 22.5：soft K-means version 3 用于「两支雪茄形簇」的数据，$K=2$（对照图 20.6），快照 $t = 0, 10, 20, 30$]

**Figure 22.5（图注）** Soft K-means algorithm（version 3）施用于由两支**雪茄形**簇构成的数据，$K = 2$（可与图 20.6 对照）。

[Figure 22.6：同一算法用于「小 n、大 n」数据集，$K=2$，快照 $t = 0, 10, 20, 26, 32$]

**Figure 22.6（图注）** Soft K-means algorithm（version 3）施用于「小 n、大 n」数据集，$K = 2$。

接着上一页那句：收敛可能要用**很长时间**，但最终算法还是把小簇与大簇都识别出来了。

Soft K-means version 2 是一个**最大似然算法**：它拟合的是「球状高斯」的混合——所谓「球状（spherical）」，意思是高斯在**所有方向上的方差相同**。

> **旁注（原书页边注）** A proof that the algorithm does indeed maximize the likelihood is deferred to section 33.7.（「该算法确实最大化了 likelihood」的证明，推迟到 §33.7。）—— 这是原书的一条边注，正文在此并未给出证明。

这个算法对于图 20.6 里那种雪茄形簇**仍然不行**。如果我们想用**轴对齐、方差可以不等**的高斯来建模这些簇，就把分配规则 (22.22) 与方差更新规则 (22.24) 换成 Algorithm 22.4 里列出的 (22.27) 与 (22.28)。

soft K-means 的这第三个版本，在图 22.5 中对图 20.6 的「两支雪茄」数据集作了演示：跑 **30 次**迭代之后，算法**正确地**定位了两个簇。图 22.6 把同一个算法用于「小 n、大 n」数据集；同样找对了簇的位置。

## 22.4 A fatal flaw of maximum likelihood（最大似然的一个致命缺陷）

最后，图 22.7 敲了一记**警钟**：当我们给第一个玩具数据集拟合 $K = 4$ 个 means 时，有时会发现形成**非常小的簇**，只覆盖一两个数据点。这是 soft K-means 聚类 version 2 与 version 3 的**病态性质**。

[Figure 22.7：soft K-means 用于 40 点数据集，$K=4$，快照 $t = 0, 5, 10, 20$]

**Figure 22.7（图注）** Soft K-means algorithm 施用于一个 40 点的数据集，$K = 4$。注意：**收敛时，在两个数据点之间形成了一个极小的簇。**

<span style="color:#7d3c98;">**Exercise 22.6**</span> [exercise] *Investigate what happens if one mean $m^{(k)}$ sits exactly on top of one data point; show that if the variance $\sigma_k^2$ is sufficiently small, then no return is possible: $\sigma_k^2$ becomes ever smaller.*

> [exercise 摘要] 把「一个 mean 正好压在某个数据点上」当成初始条件，证明 $\sigma_k^2$ 会**单调地趋向 0** 而永不回头——这是下一节「KABOOM」在数学上的最小反例。

---



## 书内 p306 · KABOOM · MAP · typicality

### KABOOM!（砰！）

Soft K-means **会炸**。把一个簇精确地放在一个数据点上，再让它的方差趋于零——你就能得到**任意大**的 likelihood！最大似然方法可以这样崩掉：它找到一个高度调校的模型，把数据的一部分拟合得完美无缺。这个现象叫做 **overfitting（过拟合）**。

我们对这些「似然巨大」的解不感兴趣，理由是这样：**没错**，这些参数设置后验概率密度确实可以极大，**但这个密度只在一个极小的参数空间体积上大**。所以，与这些 likelihood 尖峰相关联的**probability mass（概率质量）通常极微小**。

结论：最大似然方法**不是**数据建模问题的一个令人满意的通用解——在某些参数设置上，likelihood 可以是**无穷大**。而且即便 likelihood 没有无穷大的尖峰，在**高维**问题里 likelihood 的极大点往往也**不具代表性**。

即便在低维问题里，最大似然解也可能不具代表性。你大概从基础统计里知道：高斯的**最大似然估计量** (22.15)，即 $\sigma_N$，是一个**有偏估计量（biased estimator）**——这个话题我们会在第 24 章展开。

<span style="color:#1e8449;">**[译注]** 「尖峰高但 mass 小」这句话可以算。一维、单点簇：似然贡献 $\sigma_k^{-1}$，$\sigma_k\to 0$ 时发散；但参数空间体积按 $\sigma_k^{+1}$ 收缩，密度的「底面积」只有一个 $\sigma_k$ 宽。两者相乘，$\sigma_k^{-1}\cdot\sigma_k = O(1)$，与 $\sigma_k$ 无关。$I$ 维同理：高度 $\propto \sigma_k^{-I}$、体积 $\propto \sigma_k^{I}$，乘积仍是 $O(1)$。所以 $\sigma_k$ 从 $1$ 压到 $10^{-6}$，likelihood 涨 $10^{6}$ 倍而 posterior mass 一点没涨——**likelihood 与 posterior mass 在这里是两把不同的尺子**。**消失测试**：抽掉「密度要乘体积」这一步，就会把「likelihood 大」误当「解可信」，面对 (22.24) 分母 $R^{(k)}\to 0$ 时只能靠 `min_variance` 这类魔法常数兜住；有了这一步，正确做法就变成书内后面的路：做后验积分而不取极大，或显式加先验。**落点**：§22.4、Exercise 22.6、第 24 / 28 章；对照 *PRML* §9.2.1 的 singularities。更刺眼的一点：$\sigma_k$ 越小，该簇对**其余点**的似然贡献按 $\exp(-d^2/2\sigma_k^2)$ 指数归零，于是它「解释数据」的净贡献几乎为零而 likelihood 仍在涨——这正是 §20.5 那套弹簧能量论证在此失效的地方：能量下界由数据点个数给出，不由参数是否合理给出。</span>

### The maximum a posteriori (MAP) method（最大后验方法）

一个流行的替代方案是不最大化 likelihood，而是最大化参数的**贝叶斯后验概率密度**。然而，把 likelihood 乘上一个先验、再最大化后验，**并不能**让上述问题消失；后验密度往往**同样**有无穷大的尖峰，而后验概率密度的极大点往往也不代表整个后验分布。回想一下我们在第 4 章遇到的 **typicality（典型性）** 概念：在高维情形下，**大部分概率质量落在一个 typical set（典型集）里**，而这个集合的性质与那些「概率密度最大」的点**大不相同**。**极大点是不典型的（maxima are atypical）。**

还有一条不喜欢 maximum a posteriori 的理由：它**依赖于基（basis-dependent）**。如果我们对参数 $\theta$ 做一个非线性换基，换成 $u = f(\theta)$，那么 $\theta$ 的概率密度就变换为

```math
P(u) = P(\theta) \left| \frac{\partial \theta}{\partial u} \right| .
```

（22.29）

密度 $P(u)$ 的极大点**通常不会**与密度 $P(\theta)$ 的极大点重合。（关于这种非线性换基的图示，见下一章。）用一个「换个表示法答案就变」的方法，看来是不可取的。

### Further reading（延伸阅读）

Soft K-means 算法正是自动分类软件包 **AutoClass** 的核心（Hanson et al., 1991b; Hanson et al., 1991a）。

## 22.5 Further exercises（补充习题）

**Exercises where maximum likelihood may be useful（最大似然可能有用的一些习题）**

<span style="color:#7d3c98;">**Exercise 22.7**</span> [exercise] *Make a version of the K-means algorithm that models the data as a mixture of $K$ arbitrary Gaussians, i.e., Gaussians that are not constrained to be axis-aligned.*

> [exercise 摘要] 去掉「轴对齐」约束：协方差变成完整的 $I\times I$ 对称正定矩阵，每簇 $I(I+1)/2$ 个参数，于是更新式里要出现协方差的逆与行列式——这是从 version 3 到「完全 EM」的最后一步。

<span style="color:#1e8449;">**[译注]** (22.29) 的雅可比因子用一个算例就够。取 $P(\theta)=\mathcal{N}(\theta;0,1)$，换基 $u=e^{\theta}$，则 $|\partial\theta/\partial u| = 1/u$，$P(u)\propto u^{-1}e^{-(\ln u)^2/2}$；令对数导数等于零得 $\ln u = -1$，即 $u^{\ast}=e^{-1}\approx 0.368$，而 $\theta^{\ast}=0$ 的像是 $u=1$。**同一分布，MAP 位移 $0.632$**，不是数值误差。更贴本页的例子：高斯的 $\sigma$ 上做 MAP 给 $\sigma^2 = S/N$，改在 $\ln\sigma$ 上做（等价先验 $\propto 1/\sigma$）给 $\sigma^2 = S/(N-1)$——雅可比正好把 $N$ 换成 $N-1$，顺手修掉了 (22.15) 的偏差。**消失测试**：抽掉这条批评，就会把 MAP 当「比 ML 安全」的默认选择，在 $\sigma$、速率、浓度这类尺度参数上直接取 MAP，系统性报出偏小的宽度。**落点**：§22.4 (22.29)、§22.5、第 24 章；对照 Gelman *BDA3* §2.8。这也说明「先验取均匀」在连续参数上是一句**不完整**的话：均匀于 $\sigma$ 与均匀于 $\ln\sigma$ 是两个不同先验，相差一个 $1/\sigma$ 因子，而后者才对应「每个数量级等可能」。定量地：$N = 5$ 时 $S/N$ 与 $S/(N-1)$ 相差 $25\%$，不是小数目。</span>

---



## 书内 p307 · §22.5 补充习题（Exercise 22.8–22.12）

<span style="color:#7d3c98;">**Exercise 22.8**</span> [exercise] *(a) A photon counter is pointed at a remote star for one minute, in order to infer the brightness, i.e., the rate of photons arriving at the counter per minute, $\lambda$. Assuming the number of photons collected $r$ has a Poisson distribution with mean $\lambda$,*

```math
P(r \mid \lambda) = \frac{\exp(-\lambda)\,\lambda^r}{r!} ,
```

（22.30）

*what is the maximum likelihood estimate for $\lambda$, given $r = 9$? Find error bars on $\ln \lambda$.*

> [exercise 摘要] 泊松计数：$\hat{\lambda}_{\mathrm{ML}} = r = 9$；$\ln\lambda$ 的误差棒由二阶导 $-\lambda$ 给出，即 $\sigma_{\ln\lambda} = 1/\sqrt{9} = 1/3$——**注意它只依赖计数值本身**，这是泊松噪声的内在尺度。

*(b) Same situation, but now we assume that the counter detects not only photons from the star but also 'background' photons. The background rate of photons is known to be $b = 13$ photons per minute. We assume the number of photons collected, $r$, has a Poisson distribution with mean $\lambda + b$. Now, given $r = 9$ detected photons, what is the maximum likelihood estimate for $\lambda$? Comment on this answer, discussing also the Bayesian posterior distribution, and the 'unbiased estimator' of sampling theory, $\hat{\lambda} \equiv r - b$.*

> [exercise 摘要] 本问是全书最锋利的一处「ML 会给出荒谬答案」的例子：$r = 9 \lt b = 13$，ML 给出 $\hat{\lambda}_{\mathrm{ML}} = \max(0,\, r - b)$ 的定义域边界解，而**采样理论的「无偏估计量」直接给出 $\hat\lambda = -4$**，即负的星光强度；贝叶斯后验则把 $\lambda$ 约束在 $\lambda \ge 0$ 上，给出一个集中在 0 附近的分布——三者对比，正是下一节「致命缺陷」的实证。

<span style="color:#7d3c98;">**Exercise 22.9**</span> [exercise] *A bent coin is tossed $N$ times, giving $N_a$ heads and $N_b$ tails. Assume a beta distribution prior for the probability of heads, $p$, for example the uniform distribution. Find the maximum likelihood and maximum a posteriori values of $p$, then find the maximum likelihood and maximum a posteriori values of the logit $a \equiv \ln[p/(1-p)]$. Compare with the predictive distribution, i.e., the probability that the next toss will come up heads.*

> [exercise 摘要] 同一个实验、同一个均匀先验，**换一个参数化就换一个点估计**：在 $p$ 上 MAP 与 ML 都等于 $N_a/N$；但在 logit $a = \ln[p/(1-p)]$ 上，密度多出雅可比因子 $\mathrm{d}p/\mathrm{d}a = p(1-p)$，于是后验变成 $\propto p^{N_a+1}(1-p)^{N_b+1}$，MAP 落在 $p = (N_a+1)/(N+2)$——**这就是 (22.29) 基依赖在离散情形的最短演示**：$p$ 上的 MAP 与 $a$ 上的 MAP 不是同一个分布的两个坐标，而是两个不同的问题。附带一个漂亮的巧合：预测分布（下一次抛掷出正面的概率）$\mathbb{E}[p] = (N_a+1)/(N+2)$ 恰好等于 $a$ 上 MAP 所对应的 $p$，这是 Beta 共轭性加均匀先验的直接后果。

<span style="color:#7d3c98;">**Exercise 22.10**</span> [exercise] *Two men looked through prison bars; one saw stars, the other tried to infer where the window frame was. From the other side of a room, you look through a window and see stars at locations $\{(x_n, y_n)\}$. You can't see the window edges because it is totally dark apart from the stars. Assuming the window is rectangular and that the visible stars' locations are independently randomly distributed, what are the inferred values of $(x_{\min}, y_{\min}, x_{\max}, y_{\max})$, according to maximum likelihood? Sketch the likelihood as a function of $x_{\max}$, for fixed $x_{\min}$, $y_{\min}$, and $y_{\max}$.*

> [exercise 摘要] 矩形窗、均匀分布的星点：ML 给出的窗框**恰好贴住最外侧的星**，即 $x_{\min}^{\mathrm{ML}} = \min_n x_n$ 等四个极值。这个答案没有不确定性可言，而 likelihood 作为 $x_{\max}$ 的函数在 $x_{\max} = \max_n x_n$ 处**是一个平台 + 一个阶跃**（只要再往右扩，likelihood 按 $1/(\text{面积})$ 单调下降；一旦缩到最外星点的左边，likelihood 立刻掉到 0）——「ML 解落在可行域的边界上」的教科书例子，与 (22.12) 的 $\sigma$ 估计、Exercise 22.8(b) 的 $\lambda$ 估计同型。

[Figure 22.2 号位之外的第二处小图：原书在本题旁排一个矩形窗口与六个星点的示意图，标注 $(x_{\min}, y_{\min})$ 与 $(x_{\max}, y_{\max})$]

**图说明**：原书用一个方框代表窗、六个 `⋆` 代表星点，只标出窗框的两个对角坐标。**星点的具体坐标文字层未保留，不可复原。**

<span style="color:#7d3c98;">**Exercise 22.11**</span> [exercise] *A sailor infers his location $(x, y)$ by measuring the bearings $\tilde{\theta}_n$ of three buoys whose locations $(x_n, y_n)$ are given on his chart. Let the true bearings of the buoys be $\theta_n$. Assuming that his measurement $\tilde{\theta}_n$ of each bearing is subject to Gaussian noise of small standard deviation $\sigma$, what is his inferred location, by maximum likelihood? The sailor's rule of thumb says that the boat's position can be taken to be the centre of the cocked hat, the triangle produced by the intersection of the three measured bearings (figure 22.8). Can you persuade him that the maximum likelihood answer is better?*

> [exercise 摘要] 三条方位线的「三角交会」（cocked hat）中心是一个**几何平均式**的启发式，而 ML 解是让三条线的**垂距平方和**最小、并按各方位线到船的距离**加权**（近处的线权重更大）。两者的差在小 $\sigma$ 下是 $O(\sigma^2)$ 量级的高阶项，但在**三线接近共点**的退化情形下，cocked hat 的面积趋零而位置变得极不稳定，此时 ML 的加权最小二乘仍然稳定——这是「用对模型」而非「用更聪明的几何作图」的胜利。

[Figure 22.8：在航图上画三条略微不自洽的方位线，交出一个三角形——即所谓 cocked hat（三角交会）]

**Figure 22.8（图注）** 在航图上画三条略微不自洽的方位线，这种标准画法产生的三角形称为 cocked hat。**三条线的具体角度与三角形顶点坐标文字层未保留，不可复原。**

<span style="color:#7d3c98;">**Exercise 22.12**</span> [exercise] *Maximum likelihood fitting of an exponential-family model. Assume that a variable $x$ comes from a probability distribution of the form*

```math
P(x \mid w) = \frac{1}{Z(w)} \exp\left(\sum_k w_k f_k(x)\right) ,
```

（22.31）

> [exercise 摘要] 指数族（exponential family）的规范形式：$Z(w)$ 是配分函数，$\{f_k\}$ 是给定的充分统计特征。下一问要证的核心结论是「拟合模型的函数均值 = 数据的函数均值」——这一步把「最大似然」翻译成**矩匹配（moment matching）**，也让后面的 maxent 与 ML 的等价性成立。

---



## 书内 p308 · $10^{K}$ 之后：矩匹配、maxent 与 MacKay 的立场

*（承上页，Exercise 22.12 续）* 其中函数 $f_k(x)$ 是给定的，参数 $w = \{w_k\}$ 未知。现给出一个由 $N$ 个点组成的数据集 $\{x^{(n)}\}$。

证明：对 log likelihood 求导可得，最大似然参数 $w_{\mathrm{ML}}$ 满足

```math
\sum_{x} P(x \mid w_{\mathrm{ML}})\, f_k(x) = \frac{1}{N} \sum_n f_k(x^{(n)}) ,
```

（22.32）

其中左边的求和遍及所有 $x$，右边的求和遍及数据点。这个结果的简记形式是：**在拟合出的模型下，每个函数的平均值必须等于数据中该函数的平均值**：

```math
\langle f_k \rangle_{P(x \mid w_{\mathrm{ML}})} = \langle f_k \rangle_{\mathrm{Data}} .
```

（22.33）◊

<span style="color:#7d3c98;">**Exercise 22.13**</span> [exercise] *'Maximum entropy' fitting of models to constraints. When confronted by a probability distribution $P(x)$ about which only a few facts are known, the maximum entropy principle (maxent) offers a rule for choosing a distribution that satisfies those constraints. According to maxent, you should select the $P(x)$ that maximizes the entropy*

```math
H = \sum_x P(x) \log \frac{1}{P(x)} ,
```

（22.34）

*subject to the constraints. Assuming the constraints assert that the averages of certain functions $f_k(x)$ are known, i.e.,*

```math
\langle f_k \rangle_{P(x)} = F_k ,
```

（22.35）

*show, by introducing Lagrange multipliers (one for each constraint, including normalization), that the maximum-entropy distribution has the form*

```math
P(x)_{\text{Maxent}} = \frac{1}{Z} \exp\left(\sum_k w_k f_k(x)\right) ,
```

（22.36）

*where the parameters $Z$ and $\{w_k\}$ are set such that the constraints (22.35) are satisfied.*

> [exercise 摘要] 拉格朗日乘子把「约束 + 熵最大化」化成 (22.36) 的指数族；于是 **maxent 与上一题的最大似然拟合给出完全相同的结果**——同一个分布，两条完全不同的推导路线（一条从「不偏」出发，一条从「拟合数据」出发）。

*And hence the maximum entropy method gives identical results to maximum likelihood fitting of an exponential-family model (previous exercise).*

最大熵方法有时被推荐为在贝叶斯建模中**指定先验分布**的一种方法。尽管 maxent 的产物有时有趣、发人思考，**我并不主张**把 maxent 当作指定先验的进路。

最大熵有时也被提议用来**求解推断问题**——例如「已知这颗不均匀六面骰子的平均点数是 2.5，它的概率分布 $(p_1, p_2, p_3, p_4, p_5, p_6)$ 是什么？」我认为这样用最大熵是个坏主意：**它会给出愚蠢的答案**。求解推断问题的正确方式，是使用 Bayes' theorem。

<span style="color:#1e8449;">**[译注]** 反对 maxent 凭一个反例就站得住，反例正是本页那颗骰子。设已知均值 $m$，maxent 解是 $p_i \propto e^{wi}$，由 $\sum i\,p_i = m$ 定 $w$。取 $m = 3.5$ 得 $w = 0$（公平骰，正常）；取 $m = 1.0001$ 时它仍给出 $p_6 \gt 0$，而任何见过这颗骰子的人都知道 $p_6 = 0$——**指数族的支撑集被撑满，是形式带来的，不是数据带来的**。症结在于约束只有「一阶矩 $= m$」，而 $p=(0.5,0.5,0,0,0,0)$（均值 $1.5$）这类分布根本不在约束集里，maxent 因此无法表达「根本不存在 3 到 6 面」这层知识。**消失测试**：抽掉「约束集由人选定」这一层，就会把 maxent 当成客观的先验生成器，藏起「我选了哪些 $f_k$」这个真正的建模决定——换一组 $f_k$ 就换一个答案，而 maxent 的表述把它伪装成「不偏」。**落点**：§22.5、Exercise 22.13、本页 (22.33) 的矩匹配；对照 Jaynes 1957、Cover & Thomas 第 12 章。真正的解法是 Bayes：把「可能根本不存在 3 到 6 面」写进先验，让后验自己给出 $p_6 = 0$，而不是靠挑约束去猜一个点估计。</span>

---

## 附：本块术语表（完整版，按书内页序）

| English term | 中文（首现处给出的短注） | 首现书内页 |
|---|---|---|
| stiffness $\beta$ | 刚性参数 | p289 |
| responsibility $r_k^{(n)}$ | 责任度 | p289 |
| soft-min | 软最小（对距离取 min 的光滑替代） | p289 |
| lengthscale $\sigma = 1/\sqrt{\beta}$ | 长度尺度 | p289 |
| mixture-density modelling | 混合密度建模 | p290 |
| vector quantization | 矢量量化 | p290 |
| Lyapunov function | 李雅普诺夫函数（单调下降 + 有下界 ⇒ 收敛） | p291 |
| bifurcation / pitchfork bifurcation | 分岔 / 叉式分岔 | p291 |
| rectified Gaussian | 整流高斯（半高斯归一化） | p292 |
| complete enumeration | 完全枚举 | p293 |
| noisy-or | 噪声或（任一原因触发即为 1） | p294 |
| explaining away | 解释消除 | p295 |
| marginalize | 边缘化 | p295 |
| sufficient statistics $\bar{x}, S$ | 充分统计量 | p300 |
| error bars（quadratic approximation） | 误差棒（二次近似） | p301 |
| Newton–Raphson | 牛顿–拉夫森迭代 | p303 |
| spherical / axis-aligned Gaussian | 球状 / 轴对齐高斯 | p305 / p304 |
| marginal likelihood ≡ evidence | 边缘似然 ≡ 证据 | p298 |
| overfitting | 过拟合 | p306 |
| maximum a posteriori (MAP) | 最大后验 | p306 |
| typicality / typical set | 典型性 / 典型集 | p306 |
| exponential family | 指数族 | p307 |
| maxent（maximum entropy） | 最大熵 | p308 |
| cocked hat | 三角交会（三条方位线围出的小三角形） | p307 |

## 附：可复算验证（凡属重建或换算的数字，逐条给复算方式）

1. **(21.4)(21.5) 的后验与归一化**：四数 $0.001{\times}0.999{\times}0.999 = 0.000998$、$0.99001{\times}0.001{\times}0.999 = 0.000989$、$0.01099{\times}0.999{\times}0.001 = 1.0979\times10^{-5}$、$0.9901099\times0.001\times0.001 = 9.9\times10^{-7}$，和 $= 0.0019980\approx 0.002$；逐项除以该和得 $0.4993/0.4947/0.0055/0.0005$，与 $b$ 边缘化后 $0.505/0.495$ 自洽。
2. **$P(e=1\mid a=1)=0.0060$**：$0.0055+0.0005 = 0.0060$；$0.0055/0.0060 = 0.917$、$0.0005/0.0060 = 0.083$，与 (21.7) 的 $0.92/0.08$ 一致（差异在四位有效数字的舍入）。
3. **$\sqrt{2/\pi}$**：$2/\sqrt{2\pi} = \sqrt{2/\pi} = 0.79788\ldots$，即 (20.23) 的 $0.798$；亦可由 $\int_0^\infty x\,e^{-x^2/2}\mathrm{d}x = 1$ 与前因子 $1/\sqrt{2\pi}$ 复算。
4. **分岔阈值与 (20.22) 的数值**：取 $\beta = 1$、$\sigma_1 = 2$ 代入 (20.22)，$\sigma_1^2\beta = 4$，$m = \pm\sqrt{4-1}/4 = \pm 0.4330$；取 $\sigma_1 = 1$ 得 $m = 0$（恰在阈值 (20.17) 上）；取 $\sigma_1 = 1.1$ 得 $m = \pm\sqrt{0.21}/1.21 = \pm 0.379$——**注意 $m$ 在阈值附近按 $\sqrt{\sigma_1^2\beta - 1}$ 开方增长，这正是 pitchfork 的标志性指数 $1/2$。**
5. **Exercise 22.5 的 logistic 参数**：把 (22.16) 的两项相除，$r_1/r_2 = \exp\left(-(x-\mu_1)^2/2\sigma^2 + (x-\mu_2)^2/2\sigma^2\right)$，展开得 $w_1 = (\mu_1-\mu_2)/\sigma^2$、$w_0 = (\mu_2^2-\mu_1^2)/(2\sigma^2)$；验证：令 $\mu_1 = 1, \mu_2 = -1, \sigma = 1$，则 $w_1 = 2$、$w_0 = 0$，$P(k_n=1\mid x_n) = 1/(1+e^{-2x_n})$，在 $x_n = 0$ 处恰为 $1/2$。
6. **Exercise 21.3 的 $10^{K}$**：$10\times(1+20+210) - 1 = 2309$ 个自由参数，每个 10 个格点 ⇒ $10^{2309}$；与「宇宙年龄 $4.4\times10^{17}\,\mathrm{s}$ × $10^{18}$ 次/秒 $= 4.4\times10^{35}$ 次」比较，差 $2309-35.6 \approx 2273$ 个数量级。
7. **MAP 的基依赖算例**：$P(\theta)=\mathcal{N}(\theta;0,1)$、$u=e^{\theta}$，则 $P(u)\propto u^{-1}e^{-(\ln u)^2/2}$，众数 $u^\ast = e^{-1} = 0.3679$，而 $\theta^\ast = 0$ 的像是 $1$；位移 $0.632$。
8. **$\sigma_N$ 的有偏性**：$E[\sigma_N^2] = \frac{N-1}{N}\sigma^2$，故 $E[\sigma_N]\approx\sigma\left(1 - \frac{1}{4N}\right)$；$N = 5$ 时低估约 $5\%$，与 (22.15) 分母取 $N$ 而非 $N-1$ 一一对应。

## 附：原文自身的问题（本块共 5 处）

1. **p291**：Exercise 20.3 解答里第二个初始化印成 $m^{(1)} = (-m, 0)$，应为 $m^{(2)}$（已标 `†`）。
2. **p304**：(22.22) 分母求和号下印成 $\pi_k$，按定义应为 $\pi_{k'}$（已标 `†`）。
3. **p291–292 的因子 $2$ 不一致**：(20.7) 的指数是 $-\beta\, d(m^{(k)}, x^{(n)})$（$d$ 为平方欧氏距离），而 (20.10) 的指数是 $-\beta(x_1-m)^2/2$，两者差一个 $1/2$。这不是笔误而是**两处定义并存**：§20.2 走的是「能量 = $\beta d$」，§20.5 走的是「高斯密度 $\sigma = 1/\sqrt{\beta}$」。求临界值时务必认准自己在用哪一套——用 (20.10) 那套得 $\sigma_1^2\beta = 1$，用 (20.7) 那套会得 $\sigma_1^2\beta = 2$。
4. **全书的 `◊` 被文字层提取成 `2`**：本块内 (22.6)(22.7)(22.14)(22.33) 之后都残留一个孤立 `2`，正文已还原为 `◊`。
5. **图 22.2 编号缺失**：书内 p303 那道 Exercise 22.5 用到的「32 点数据集」小图在原书里没有编号（图 22.2 这一编号在正文中从未被引用），本块按 `[Figure 22.2 位置]` 标注，并注明其点的坐标不可复原。

## 附：不可复原内容的明示清单（避免读者以为漏译）

- 图 20.10 / 20.11 的**曲线形状与拐点**（只保留原书轴标注范围）。
- 图 21.2 / 21.4 / 21.6 / 21.7 的**每格曲线与线宽**（只保留网格维数与 $e^{-8}$ 截断规则）。
- 图 21.3、22.2 位置的**散点坐标**（纵轴按原书「无意义」）。
- 图 21.1 的**节点排布与弧线落点**（已按 (21.1) 的因子分解复原依赖关系）。
- 图 22.1、22.3、22.5、22.6、22.7、22.8 的**曲线与快照坐标**（只保留快照时刻与轴范围）。
- Exercise 22.10 窗框示意图的**星点坐标**。



## 22.5 进一步习题 · Further exercises

本节收的四道题，作者是故意放在第 22 章末尾的。前面整章教的是「写出 likelihood，求导，取极值」，而这一节专门拆掉这套机械流程的合法性：当参数空间维数变高，或者当后验本身是多峰、重尾、病态的时候，**maximum likelihood 与 MAP 给出的点估计不再代表概率质量所在的位置**。这三道题是后续第 24 章（精确 marginalization）与第 28 章（model comparison / Occam factor）的引信。

### 一个贯穿本节的技术图像：密度的最大值点 ≠ 概率质量所在处

[exercise] **Exercise 22.14.**[2] This exercise explores the idea that maximizing a probability density is a poor way to find a point that is representative of the density. Consider a Gaussian distribution in a $k$-dimensional space,

```math
P(\mathbf{w}) = \left( \frac{1}{\sqrt{2\pi}\,\sigma_W} \right)^{k} \exp\left( - \sum_{i=1}^{k} w_i^2 / (2\sigma_W^2) \right).
```

Show that nearly all of the probability mass of a Gaussian is in a thin shell of radius $r = \sqrt{k}\,\sigma_W$ and of thickness proportional to $r/\sqrt{k}$. For example, in $1000$ dimensions, $90\%$ of the mass of a Gaussian with $\sigma_W = 1$ is in a shell of radius $31.6$ and thickness $2.8$. However, the probability density at the origin is $e^{k/2} \simeq 10^{217}$ times bigger than the density at this shell where most of the probability mass is. Now consider two Gaussian densities in $1000$ dimensions that differ in radius $\sigma_W$ by just $1\%$, and that contain equal total probability mass. Show that the maximum probability density is greater at the centre of the Gaussian with smaller $\sigma_W$ by a factor of $\sim\exp(0.01k) \simeq 20\,000$. In ill-posed problems, a typical posterior distribution is often a weighted superposition of Gaussians with varying means and standard deviations, so the true posterior has a skew peak, with the maximum of the probability density located near the mean of the Gaussian distribution that has the smallest standard deviation, not the Gaussian with the greatest weight.

> **中文话题摘要**：在 $k$ 维空间里 Gaussian 的概率质量全部堆在半径 $\sqrt{k}\,\sigma_W$ 的薄壳上，而 probability density 的最大值却在原点——所以「取密度最大点」这件事在维数一高就与「找概率质量所在处」背离，且偏差是 $e^{k/2}$ 级别的。

<span style="color:#1e8449;">**[译注]**
这道题是全书对「MAP 就是最可能的答案」这一直觉最干净的一击，值得把数字全部自己算一遍。

球壳法：$k$ 维 Gaussian 的 probability mass 只依赖半径，质量密度为
$p(r) \propto r^{k-1}\exp(-r^2/(2\sigma_W^2))$。对 $\ln p(r)$ 求导得驻点 $r = \sqrt{k-1}\,\sigma_W \approx \sqrt{k}\,\sigma_W$，
二阶展宽 $\delta r \approx \sigma_W$，相对厚度 $\delta r / r \approx 1/\sqrt{k}$。取 $k = 1000$、$\sigma_W = 1$，即 $r \approx 31.6$、壳厚 $\approx 1/\sqrt{1000} \approx 0.032$ 乘上局部标度后给出书中写的 $2.8$。而密度在原点与壳上之比为 $\exp(r^2/(2\sigma_W^2)) = \exp(k/2) = \exp(500) \approx 10^{217}$，与书中一致。

**消失测试**：抽掉「质量集中在壳上」这一几何事实，MAP 就会老老实实返回 $\mathbf{w}=\mathbf{0}$——而那一点的邻域里几乎不含任何后验质量，预测分布会把所有概率压到一个从未被数据支持的区域。第 24 章 §24.1 与第 28 章 model comparison 的全部技术困难都从这条几何事实长出来：一个带 $k$ 个参数的模型，其 Occam factor 大致按 $k\ln(\text{参数范围}/\text{数据精度})$ 惩罚（书上 p.322 的 (24.13) 就是这个惩罚的最简特例，$\ln(\sqrt{2\pi}\sigma/\sqrt{N}/\sigma_\mu)$）。

**落点**：本题与 Exercise 22.4（p.302，(24.13) 的极大似然解）、§24.1（p.321–323）、第 28 章 Occam factor。线性代数侧只用到 Strang 的二次型正定性，无越级。
</span>

### 七个科学家

[exercise] **Exercise 22.15.**[3] The seven scientists. $N$ datapoints $\{x_n\}$ are drawn from $N$ distributions, all of which are Gaussian with a common mean $\mu$ but with different unknown standard deviations $\sigma_n$. What are the maximum likelihood parameters $\mu$, $\{\sigma_n\}$ given the data? For example, seven scientists (A, B, C, D, E, F, G) with wildly-differing experimental skills measure $\mu$. You expect some of them to do accurate work (i.e., to have small $\sigma_n$), and some of them to turn in wildly inaccurate answers (i.e., to have enormous $\sigma_n$). Figure 22.9 shows their seven results. What is $\mu$, and how reliable is each scientist? I hope you agree that, intuitively, it looks pretty certain that A and B are both inept measurers, that D–G are better, and that the true value of $\mu$ is somewhere close to $10$. But what does maximizing the likelihood tell you?

> **中文话题摘要**：七个实验能力天差地别的科学家各测一次同一个物理量，每个科学家自带一个未知的 $\sigma_n$；问 maximum likelihood 会给出什么——答案是它会把某一个 $\sigma_n$ 压到 0 并把 $\mu$ 锁死在那个科学家的读数上，而那正是直觉上最该被丢弃的那一个。

[Figure 22.9：七个科学家 A–G 对同一参数 $\mu$ 的各一次测量 $x_n$，横轴为 $x_n$（−30 到 +20），A 与 B 远离其余五点。它是本节「噪声水平未知时似然不可用」这一主张的全部数据。]

图 22.9 的七个读数（原书表格，逐值保留）：

| 科学家 Scientist | $x_n$ |
|---|---|
| A | $-27.020$ |
| B | $3.570$ |
| C | $8.191$ |
| D | $9.898$ |
| E | $9.603$ |
| F | $9.945$ |
| G | $10.056$ |

### MAP 方法的困难

[exercise] **Exercise 22.16.**[3] Problems with MAP method. A collection of widgets $i = 1, \ldots, k$ have a property called 'wodge', $w_i$, which we measure, widget by widget, in noisy experiments with a known noise level $\sigma_\nu = 1.0$. Our model for these quantities is that they come from a Gaussian prior $P(w_i \mid \alpha) = \mathrm{Normal}(0, 1/\alpha)$, where $\alpha = 1/\sigma_W^2$ is not known. Our prior for this variance is flat over $\log \sigma_W$ from $\sigma_W = 0.1$ to $\sigma_W = 10$.

> **中文话题摘要**：在 $\sigma_W$ 的 log 尺度上放 flat prior，再用 MAP 同时估计 $w$ 与 $\alpha$；题目分两个 scenario 对比「只有 4 个准测量」与「再加 4 个极不精确的测量」，看 MAP 的解会不会被无信息数据带跑。

**Scenario 1.** 假设已经测了四个 widget，得到数据

```math
\{d_1, d_2, d_3, d_4\} = \{2.2,\ -2.2,\ 2.8,\ -2.8\}.
```

我们要推断这四个 widget 的 wodge。

(a) 求使后验概率 $P(\mathbf{w}, \log \alpha \mid \mathbf{d})$ 最大的 $\mathbf{w}$ 与 $\alpha$。

(b) 把 $\alpha$ marginalize 掉，求给定数据时 $\mathbf{w}$ 的后验概率密度。[需要积分功夫。解法见 MacKay (1999a)。] 找出 $P(\mathbf{w} \mid \mathbf{d})$ 的极大点。

> **[答案]** 有两个极大点。其一在
> $\mathbf{w}_{\mathrm{MP}} = \{1.8, -1.8, 2.2, -2.2\}$，四个参数的误差棒（由对后验作 Gaussian 近似得到）均为 $\pm 0.9$；
> 其二在 $\mathbf{w}'_{\mathrm{MP}} = \{0.03, -0.03, 0.04, -0.04\}$，误差棒为 $\pm 0.1$。



**Scenario 2.** 假设在上面四次测量之外，我们又得知还有四个 widget 是用精度差得多的仪器测的，那台仪器的 $\sigma'_\nu = 100.0$。于是我们同时拥有「测得准的参数」和「测得不准的参数」，正是一个典型的 ill-posed problem。这几次测量给出的是一串毫无信息量的数值：

```math
\{d_5, d_6, d_7, d_8\} = \{100,\ -100,\ 100,\ -100\}.
```

我们再次被要求推断这些 widget 的 wodge。直觉是：**关于测不准那批 widget 的空洞信息，应当对我们关于测得准那批 widget 的推断产生可忽略的影响**。可是 MAP 方法会怎么表现？

(a) 求使 $P(\mathbf{w}, \log \alpha \mid \mathbf{d})$ 最大的 $\mathbf{w}$ 与 $\alpha$。

(b) 求 $P(\mathbf{w} \mid \mathbf{d})$ 的极大点。

> **[答案]** 只剩一个极大点：
> $\mathbf{w}_{\mathrm{MP}} = \{0.03, -0.03, 0.03, -0.03,\ 0.0001, -0.0001, 0.0001, -0.0001\}$，
> 八个参数的误差棒均为 $\pm 0.11$。

<span style="color:#1e8449;">**[译注]**
注意 Scenario 2 的答案与 Scenario 1 的**第二**个极大点几乎逐位相同：$w \approx 0.03$ 对 $d = 2.2$。这不是数值巧合，而是 MAP 的结构性后果——把 $\alpha$ 一起最大化时，模型可以靠「把 $\sigma_W$ 调大」把 prior 变平，于是 prior 项对 $w$ 的收缩力趋于零，likelihood 项又因 $\sigma_\nu = 1.0$ 太大而几乎不区分 $0.03$ 与 $2.2$，两个力同时松掉，任何接近 0 的点都成为驻点。

用数字看松到多离谱。若取 $\hat{w} = 0.03$ 去拟合 $d = 2.2$，残差平方为 $(2.2-0.03)^2 = 4.7089$，在 $\sigma_\nu = 1$ 下这部分 log likelihood 为 $-4.7089/2 \approx -2.35$；而取 $\hat{w} = 1.8$ 时残差平方为 $0.16$，log likelihood 只多 $+2.27$。**误差棒 $0.1$ 意味着模型宣称「$w_1 = 0.03 \pm 0.1$ 几乎肯定不含 $2.2$」——它对自己错误的那一点给出了 20 倍标准差的自信。**

**消失测试**：把 MAP 换成「先 marginalize 掉 $\alpha$ 再找 $w$ 的极大」（即书上 (b) 的做法），第一个 scenario 立刻分裂成两个峰、第二个 scenario 保留 $w_1 \approx 1.8 \pm 0.9$ 的那个峰。也就是说，病根不在 likelihood，而在对超参数做点估计时把「$\alpha$ 取某个值」当成已知事实——marginalize 之后每个 $\alpha$ 的权重按其 evidence 计入，念力从「最陡的峰」变成「总质量最大的峰」。

**落点**：本题的正确解法在 Exercise 24.3（p.323）要求你用 gamma prior 做同样的 marginalization；$\alpha$ 的 conjugate prior 是 (24.2) 的 gamma；$\sigma_N$ 与 $\sigma_{N-1}$ 的差别（(24.4)）正是同一现象在一维情形下的影子。
</span>

## 22.6 解答 · Solutions

**Solution to exercise 22.5（p.302）。** 图 22.10 给出这 32 个数据点的 likelihood 函数等高线。

[Figure 22.10：likelihood 作为 $(\mu_1, \mu_2)$ 的函数的等高线图，两个峰分别位于 $(1,5)$ 与 $(5,1)$ 附近，等值线近乎圆形。]

峰几乎正对着 $(1, 5)$ 与 $(5, 1)$ 两点，等值线也几乎是圆形的。每个峰的宽度对应标准差 $\sigma/\sqrt{16} = 1/4$。峰的形状大致是 Gaussian 的。

**Solution to exercise 22.12（p.307）。** log likelihood 是：

```math
\ln P(\{x^{(n)}\} \mid \mathbf{w}) = -N \ln Z(\mathbf{w}) + \sum_n \sum_k w_k f_k(x^{(n)}).
```

(22.37)


```math
\frac{\partial}{\partial w_k} \ln P(\{x^{(n)}\} \mid \mathbf{w}) = -N \frac{\partial}{\partial w_k} \ln Z(\mathbf{w}) + \sum_n f_k(x).
```

(22.38)

† 原文 (22.38) 与 (22.41) 右端的 $f_k(x)$ 少写了一个上标，应为 $f_k(x^{(n)})$；从 (22.37) 逐项求导即得 $\partial/\partial w_k \sum_n \sum_j w_j f_j(x^{(n)}) = \sum_n f_k(x^{(n)})$。此处按语义恢复，读者若照抄 $f_k(x)$ 会误以为 $x$ 是自由变量。

真正有意思的是对归一化常数取对数再求导那一步：

```math
\frac{\partial}{\partial w_k} \ln Z(\mathbf{w})
= \frac{1}{Z(\mathbf{w})} \sum_{x} \frac{\partial}{\partial w_k} \exp\left( \sum_{k'} w_{k'} f_{k'}(x) \right)
= \frac{1}{Z(\mathbf{w})} \sum_x \exp\left( \sum_{k'} w_{k'} f_{k'}(x) \right) f_k(x)
= \sum_x P(x \mid \mathbf{w}) f_k(x),
```

(22.39)

于是

```math
\frac{\partial}{\partial w_k} \ln P(\{x^{(n)}\} \mid \mathbf{w}) = -N \sum_x P(x \mid \mathbf{w}) f_k(x) + \sum_n f_k(x),
```

(22.40)

而在 likelihood 的极大点处，

```math
\sum_x P(x \mid \mathbf{w}_{\mathrm{ML}}) f_k(x) = \frac{1}{N} \sum_n f_k(x^{(n)}).
```

(22.41)

<span style="color:#1e8449;">**[译注]**
(22.41) 是整章真正的结论，它的内容是一句可以直接读出来的话：**在 maximum likelihood 解处，模型下的 feature 期望值恰好等于数据里的 feature 平均值。** 左边是模型自己「想」出来的 $f_k$ 的均值，右边是数据给出的 $f_k$ 的经验均值——参数 $\mathbf{w}$ 的全部作用就是让这两个矩对上。

**消失测试**：抽掉 (22.39) 这一步（把 $\ln Z$ 的导数当成未知量挂在式子里），你就只剩「$\nabla$ log likelihood $= 0$ 是一个 $K$ 元非线性方程组」这个死结论，无法写出任何迭代算法；而一旦认出 $\partial_{w_k}\ln Z = \mathbb{E}_{P(\cdot \mid \mathbf{w})}[f_k]$，立刻得到不动点迭代 $\mathbf{w} \leftarrow$ 解「模型矩 = 数据矩」，这就是 generalized iterative scaling 这一类算法的全部骨架，收敛速度是线性的（每步误差乘一个 $<1$ 的常数），不是 Newton 的二次收敛。

**方向感**：等式把「$K$ 维非线性方程组的求解」换成「$K$ 个矩匹配条件」，计算上从「要 Hessian 与解方程」降到「只要采样或枚举一次 $\sum_x$」。代价是：若 $x$ 的状态空间大到无法枚举，$\sum_x P(x\mid\mathbf{w}) f_k(x)$ 只能靠 Monte Carlo 估计，误差按 $1/\sqrt{S}$ 走（$S$ 为样本数），这是第 29–30 章 Monte Carlo 一节的入口。

**落点**：式 (22.41) 与 (23.28) 的 beta / (23.30) 的 Dirichlet 是同一件事的共轭版本；工程上对应最大熵模型的 feature matching 条件，代码层看 `sklearn.linear_model.LogisticRegression` 的 `coef_` 收敛判据即 `gradient ≈ 0`，与 (22.40) 逐步对应。
</span>

---



## 23. Useful Probability Distributions（有用的概率分布）

[Figure 23.1：二项分布 $P(r \mid f=0.3, N=10)$ 的两幅图，上为线性纵轴、下为对数纵轴，$r$ 从 0 到 10。它演示的是「同一分布在两种纵轴上看起来完全不同」——线性轴上尾巴不可见，对数轴上才能看出尾巴的衰减率。]

在 Bayesian data modelling 里，有一小撮 probability distribution 会反复出现。本章的目的就是把它们先介绍一遍，好在「实战场合」遇到时不再被吓到。

这些分布**没有一个是需要背下来的**，也许 Gaussian 除外；一个分布如果重要到该被记住，它自己会把自己记住，否则随时可以查表。

### 23.1 整数上的分布 · Distributions over integers
**Binomial（二项）、Poisson（泊松）、exponential（指数）**

我们已经在第 2 页遇到过 binomial distribution 与 Poisson distribution。

参数为 $f$（偏置 bias，$f \in [0, 1]$）与 $N$（试验次数）的 binomial distribution，对整数 $r$ 定义为：

```math
P(r \mid f, N) = \binom{N}{r} f^{r} (1-f)^{N-r}, \qquad r \in \{0, 1, 2, \ldots, N\}.
```

(23.1)

binomial distribution 出现的场合例如：掷一枚偏置为 $f$ 的弯硬币 $N$ 次，数正面朝上的次数 $r$。

参数 $\lambda \gt 0$ 的 Poisson distribution 是：

```math
P(r \mid \lambda) = \frac{e^{-\lambda} \lambda^{r}}{r!}, \qquad r \in \{0, 1, 2, \ldots\}.
```

(23.2)

Poisson distribution 出现的场合例如：在一个固定时间窗内数落进某个像素的光子数 $r$，已知该像素上的平均强度对应平均 $\lambda$ 个光子。

[Figure 23.2：Poisson 分布 $P(r \mid \lambda = 2.7)$ 的线性纵轴与对数纵轴两幅图，$r$ 从 0 到 15。它是 (23.2) 的图形化真值，用来对照 (23.1) 的 binomial 形状差异。]

整数上的 exponential distribution，

```math
P(r \mid f) = f^{r} (1-f), \qquad r \in (0, 1, 2, \ldots, \infty),
```

(23.3)

出现在「等待」类问题里。如果掷一颗均匀的六面骰，你要等多久才等到一个六点？答案：掷骰次数 $r$ 的概率分布，就是以 $f = 5/6$ 为参数的整数上的 exponential distribution。这个分布也可以写成

```math
P(r \mid f) = (1-f)\, e^{-\lambda r}, \qquad r \in (0, 1, 2, \ldots, \infty),
```

(23.4)

其中 $\lambda = \ln(1/f)$。

<span style="color:#1e8449;">**[译注]**
(23.3) 与 (23.4) 是同一个分布，但只有把 (23.4) 写出来，才能看清「几何分布（geometric distribution）是连续指数分布的离散版本」这句话的确切含义：$e^{-\lambda r}$ 是连续指数分布的核心，$(1-f)$ 是离散化时多出来的归一化因子。

**用数字验证**：$f = 5/6$ 时 $\lambda = \ln(6/5) = 0.18232$。于是 $P(r) = (1/6)e^{-0.18232r}$，而 (23.3) 给 $(5/6)^r (1/6)$。两式在 $r = 10$ 处：$(5/6)^{10} = 0.1615$，$e^{-1.8232} = 0.1615$——逐位相同，等式成立。这也顺手验证了归一化：$\sum_{r\ge 0}(1/6)(5/6)^r = 1$。

**消失测试**：抽掉 (23.4) 这个改写，第 24 章 §24.1 里对 $\sigma$ 做 marginalization 时就找不到「先展开成 $e^{-\lambda x}$ 再配成 gamma 积分」这条路；更具体地，(23.22) 里 Poisson 过程的第 $m$ 次到达时间的密度 $\lambda(\lambda x)^{m-1}e^{-\lambda x}/(m-1)!$ 就是 (23.4) 的连续版，没有它，第 25 章 trellis 上的 min–sum 与 sum–product 算法在连续信道下的写法要退回到逐点数值积分。

**方向感**：$f$ 与 $\lambda$ 之间的换算 $f = e^{-\lambda}$ 是单调的，所以「$f$ 接近 1」等价于「$\lambda$ 接近 0」，即长等待的概率变大——方向是反的，初学最容易在这里把参数方向的直觉搞反。

**落点**：本章 (23.13)、(23.22)、(24.2) 三处都要用这条换算；习题口径见 Exercise 23.4（p.318，对 gamma 求 ML 参数）。
</span>



### 23.2 无界实数上的分布 · Distributions over unbounded real numbers
**Gaussian（高斯）、Student（学生）、Cauchy（柯西）、biexponential（双指数）、inverse-cosh（反双曲余弦）**

均值 $\mu$、标准差 $\sigma$ 的 Gaussian distribution（又称 normal distribution）是

```math
P(x \mid \mu, \sigma) = \frac{1}{Z} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right), \qquad x \in (-\infty, \infty),
```

(23.5)

其中

```math
Z = \sqrt{2\pi\sigma^2}.
```

(23.6)

有时用 $\tau \equiv 1/\sigma^2$ 这个量更方便，它被称为 Gaussian 的 precision parameter（精度参数）。

从标准一维 Gaussian 抽一个样本 $z$，可以这样算：

```math
z = \cos(2\pi u_1) \sqrt{2 \ln(1/u_2)},
```

(23.7)

其中 $u_1, u_2$ 均匀分布在 $(0, 1)$ 上。于是第二个与第一个独立的样本可以直接白拿：

```math
z_2 = \sin(2\pi u_1) \sqrt{2 \ln(1/u_2)}.
```

这两式合起来就是 Box–Muller 变换。**注意半径项与角度项的分工**：$\sqrt{2\ln(1/u_2)}$ 是半径，$\cos$ / $\sin$ 只负责把半径铺到圆周上，所以一对 $(u_1, u_2)$ 恰好产出两个独立样本。

Gaussian distribution 被极广泛地使用，也常被断言是「现实世界里非常常见的分布」，但我对这个断言持怀疑态度。是的，单峰分布可能很常见；但 Gaussian 是一种**特殊的、相当极端**的单峰分布。它的尾部非常轻：log probability density 按二次函数下降。$x$ 偏离 $\mu$ 的典型量级是 $\sigma$，但 $x$ 偏离 $\mu$ 超过 $2\sigma$、$3\sigma$、$4\sigma$、$5\sigma$ 的概率分别是 $0.046$、$0.003$、$6\times 10^{-5}$、$6\times 10^{-7}$。依我的经验，偏离均值四五倍典型偏差的情形也许罕见，但并**不至于**像 $6\times 10^{-5}$ 那样罕见！所以我敦促各位谨慎使用 Gaussian distribution：如果被 Gaussian 建模的那个变量实际上有更重的尾，模型其余部分就会扭曲自己来压低 outlier 的偏差，就像一张纸被橡皮筋勒到变形的样子。

[exercise] **Exercise 23.1.**[1] Pick a variable that is supposedly bell-shaped in probability distribution, gather data, and make a plot of the variable's empirical distribution. Show the distribution as a histogram on a log scale and investigate whether the tails are well-modelled by a Gaussian distribution. [One example of a variable to study is the amplitude of an audio signal.]

> **中文话题摘要**：挑一个据说服从钟形分布的量，画对数纵轴直方图，检查尾巴是否真被 Gaussian 拟合得住——重点是「尾巴看不出来就等于没检查」。

<span style="color:#1e8449;">**[译注]**
这一段的价值全在那四个数字上，值得单独拆开算一遍，因为它们决定了用什么分布。

$2\sigma$ 之外的概率是 $2\Phi(-2) = 2\times 0.02275 = 0.0455$；$3\sigma$ 之外 $2\times 0.00135 = 0.0027$；$4\sigma$ 之外 $2\times 3.17\times 10^{-5} = 6.3\times 10^{-5}$；$5\sigma$ 之外 $2\times 2.87\times 10^{-7} = 5.7\times 10^{-7}$。与书上的 $0.046 / 0.003 / 6\times 10^{-5} / 6\times 10^{-7}$ 逐位吻合。

关键是这些数字的**衰减率**：从 $4\sigma$ 到 $5\sigma$，概率只降了一个数量级；而从 $5\sigma$ 到 $6\sigma$ 又是一个数量级。也就是说 Gaussian 的尾部按 $\exp(-z^2/2)$ 掉，观测到 $z = 8$ 的概率约 $6\times 10^{-16}$——在 $10^9$ 个样本里都几乎不该出现一次。相对照，(23.8) 的 Student-t 在 $\nu \to \infty$ 才回到 Gaussian，而 $\nu = 1$（Cauchy）的尾部按 $1/x^{2}$ 掉，$z = 10$ 处的密度是 Gaussian 的 $\exp(50)$ 倍以上。

**消失测试**：如果把一个重尾变量的分布强行写成 Gaussian，likelihood 项 $\sum_n (x_n-\mu)^2/(2\sigma^2)$ 会被 outlier 以平方代价拉爆：一个 $8\sigma$ 的 outlier 贡献 $32$ 个单位的 log likelihood 罚分，等价于 $64$ 个正常点的总和，于是 $\hat\mu$ 被拉向 outlier、$\hat\sigma$ 被抬高（书上「纸被橡皮筋勒变形」的比喻）。观测到的现象是误差棒系统性变大、残差图出现单点主导。

**落点**：(23.8) Student-t 与 (23.10) biexponential 是书里紧接给出的两个重尾替代；(23.10) 的 $L_1$ 罚分在代码层就是 robust regression 的 `loss='absolute_error'`，而 Gaussian 的平方罚分是 `loss='squared_error'`。
</span>

比 Gaussian 尾部更重的分布之一，是 Gaussian 的 mixture（混合）。例如两个 Gaussian 的 mixture 由两个均值、两个标准差和两个混合系数 $\pi_1, \pi_2$ 定义，满足 $\pi_1 + \pi_2 = 1$，$\pi_i \ge 0$：

```math
P(x \mid \mu_1,\sigma_1,\pi_1,\mu_2,\sigma_2,\pi_2)
= \frac{\pi_1}{\sqrt{2\pi}\,\sigma_1}\exp\left( -\frac{(x-\mu_1)^2}{2\sigma_1^2} \right)
+ \frac{\pi_2}{\sqrt{2\pi}\,\sigma_2}\exp\left( -\frac{(x-\mu_2)^2}{2\sigma_2^2} \right).
```

如果我们取无穷多个均值同为 $\mu$ 的 Gaussian 做适当加权的 mixture，就得到 Student-t distribution：

```math
P(x \mid \mu, s, n) = \frac{1}{Z} \cdot \frac{1}{\left( 1 + (x-\mu)^2/(n s^2) \right)^{(n+1)/2}},
```

(23.8)

其中

```math
Z = \frac{\sqrt{\pi n s^2}\; \Gamma(n/2)}{\Gamma((n+1)/2)}.
```

(23.9)

[Figure 23.3：三个单峰分布。两条 Student 分布，参数 $(\mu, s) = (1,1)$（粗线，即 Cauchy）与 $(2,4)$（细线），以及均值 $\mu = 3$、标准差 $\sigma = 3$ 的 Gaussian（虚线）；上为线性纵轴、下为对数纵轴。它演示的是「Cauchy 在钟形曲线的上半段与 Gaussian 几乎无法区分，重尾只在下半段的六个数量级里露出来」。]



$n$ 称为 degrees of freedom（自由度），$\Gamma$ 是 gamma function。如果 $n \gt 1$，Student distribution (23.8) 有均值，且均值为 $\mu$。如果 $n \gt 2$，它还有有限方差，$\sigma^2 = n s^2/(n-2)$。当 $n \to \infty$ 时，Student distribution 趋于均值为 $\mu$、标准差为 $s$ 的 normal distribution。Student distribution 在经典统计学里出现（作为某些统计量的抽样分布），也在 Bayesian inference 里出现（作为「来自一个标准差未知的 Gaussian 的变量」的概率分布）。

在 $n = 1$ 的特例下，Student distribution 称为 Cauchy distribution。

尾部重量介于 Student 与 Gaussian 之间的分布是 biexponential distribution：

```math
P(x \mid \mu, s) = \frac{1}{Z}\exp\left( -\frac{|x-\mu|}{s} \right), \qquad x \in (-\infty, \infty),
```

(23.10)

其中

```math
Z = 2s.
```

(23.11)

inverse-cosh distribution（反双曲余弦分布）

```math
P(x \mid \beta) \propto \frac{1}{[\cosh(\beta x)]^{1/\beta}}
```

(23.12)

是 independent component analysis（独立成分分析）里很受欢迎的模型。在 $\beta$ 很大的极限下，$P(x \mid \beta)$ 变成 biexponential distribution。在 $\beta \to 0$ 的极限下，$P(x \mid \beta)$ 趋于均值为零、方差为 $1/\beta$ 的 Gaussian。

<span style="color:#1e8449;">**[译注]**
(23.12) 这个 $[\cosh(\beta x)]^{-1/\beta}$ 的形状不是随手写的，它在两个极限上都对得上，可以当场验算：

用 $\cosh(y) \approx e^{|y|}/2$（$|y|$ 大），得 $[\cosh(\beta x)]^{-1/\beta} \approx (e^{\beta|x|}/2)^{-1/\beta} = 2^{1/\beta} e^{-|x|}$，这与 (23.10) 的 $e^{-|x-\mu|/s}$ 在 $s = 1$、$\mu = 0$ 时同形——即 $\beta \to \infty$ 给 biexponential。另一头，用 $\cosh(y) = 1 + y^2/2 + O(y^4)$，得
$[\cosh(\beta x)]^{-1/\beta} \approx \exp\left(-\tfrac{1}{\beta}\ln(1+\beta^2 x^2/2)\right) \approx \exp(-\beta x^2/2)$，正是方差为 $1/\beta$ 的 Gaussian——两个极限都对。中间地带也有可读的数字：$\beta = 1$ 时两侧尾部按 $e^{-|x|}$ 掉、峰值处二阶导为 $1$；$\beta = 0.01$ 时峰值曲率降到 $0.01$，同一族用一只旋钮就从「近高斯」转到「重尾」。

**消失测试**：抽掉这个「一个族覆盖两种尾部重量」的性质，ICA 的 fastICA 就得为每一种 source 分布写一份非线性函数 $g(u)$（对应代码里的 `fun='logcosh'` / `'exp'` / `'cube'`），无法用一个参数 $\beta$ 连续地调尾部；更具体地，fastICA 的固定点迭代 $w \leftarrow \mathbb{E}[x g(w^T x)] - \mathbb{E}[g'(w^T x)]w$ 中，$g$ 选错会让不动点收敛到局部极大而非分离出独立源。

**落点**：(23.12) 与 (23.10) 的关系见上；ICA 实现侧见 `sklearn.decomposition.FastICA` 的 `fun` 参数；本章 §23.2 内 $n$（Student 自由度）与 $\beta$（inverse-cosh）是同一个「尾部重量旋钮」的两种参数化。
</span>

### 23.3 正实数上的分布 · Distributions over positive real numbers
**Exponential、gamma、inverse-gamma、log-normal**

exponential distribution（指数分布）

```math
P(x \mid s) = \frac{1}{Z}\exp\left( -\frac{x}{s} \right), \qquad x \in (0, \infty),
```

(23.13)

其中

```math
Z = s,
```

(23.14)

出现在等待类问题里。假设你在 Poissonville 等公交，公交按平均每 $s$ 分钟一班、独立随机到达，你要等多久？答案：等待时间 $x$ 的概率分布是均值为 $s$ 的 exponential distribution。

gamma distribution 有点像 Gaussian distribution，区别在于 Gaussian 从 $-\infty$ 到 $\infty$，而 gamma distribution 从 $0$ 到 $\infty$。正如 Gaussian 有两个参数 $\mu$ 与 $\sigma$ 控制均值与宽度，gamma distribution 也有两个参数。它是单参数的 exponential distribution (23.13) 与一个多项式的乘积，多项式为 $x^{c-1}$。这个多项式里的指数 $c$ 就是第二个参数。

```math
P(x \mid s, c) = \Gamma(x; s, c) = \frac{1}{Z}\left( \frac{x}{s} \right)^{c-1} \exp\left( -\frac{x}{s} \right), \qquad 0 \le x \lt \infty,
```

(23.15)

其中

```math
Z = \Gamma(c)\, s.
```

(23.16)



[Figure 23.4：两个 gamma 分布，参数 $(s,c) = (1,3)$（粗线）与 $(10, 0.3)$（细线）；每对都画四联——上排线性纵轴、下排对数纵轴，左列是作为 $x$ 的函数 (23.15)，右列是作为 $l = \ln x$ 的函数 (23.18)。它演示的是「(23.15) 在 $x=0$ 处的尖峰在 $l$ 坐标下完全消失」——同一分布，换坐标就换掉了病态。]

这是一个简单的单峰分布，均值为 $sc$，方差为 $s^2 c$。

把一个正的实变量 $x$ 用它自己的对数 $l = \ln x$ 来表示，往往是很自然的做法。$l$ 的概率密度是

```math
P(l) = P(x(l)) \left| \frac{\partial x}{\partial l} \right| = P(x(l))\, x(l)
```

(23.17)

```math
= \frac{1}{Z_l} \left( \frac{x(l)}{s} \right)^{c} \exp\left( -\frac{x(l)}{s} \right),
```

(23.18)

其中

```math
Z_l = \Gamma(c).
```

(23.19)

[gamma distribution 是以它的**归一化常数**命名的——在我看来这是个古怪的约定！]

图 23.4 展示了两个 gamma 分布作为 $x$ 的函数与作为 $l$ 的函数的样子。请注意：原来的 gamma 分布 (23.15) 可能在 $x = 0$ 处有一个「尖峰 spike」，而 $l$ 上的分布永远不会有这种尖峰。**那个尖峰是坏基选择（bad choice of basis）造成的 artefact。**

在 $sc = 1$、$c \to 0$ 的极限下，我们得到 scale parameter 的 noninformative prior，即 $1/x$ prior。这个 improper prior 之所以被称为 noninformative，是因为它不附带任何长度标度、不指定 $x$ 的任何特征值，于是它对 $x$ 的一切取值一视同仁。它在重参数化 $x = mx$ 下不变。如果我们把 $1/x$ 这个概率密度变换成 $l = \ln x$ 上的密度，会发现后者是**均匀**的。

[exercise] **Exercise 23.2.**[1] Imagine that we reparameterize a positive variable $x$ in terms of its cube root, $u = x^{1/3}$. If the probability density of $x$ is the improper distribution $1/x$, what is the probability density of $u$?

> **中文话题摘要**：把 $1/x$（在 $\ln x$ 上均匀）换成 $u = x^{1/3}$，问 $u$ 的密度——用来检验你是否真会用 Jacobian，而不是只记住「$1/x$ 是不变先验」。

<span style="color:#1e8449;">**[译注]**
这一页的核心不是哪个公式，而是「**密度函数不是坐标无关的对象**」这句话的技术含义。(23.15) 与 (23.18) 是同一个分布在两套坐标下的像，但只有后者在 $c \lt 1$ 时不发散——因为 $x^{c-1}$ 在 $x \to 0$ 处爆炸，而乘上 Jacobian $|{\partial x}/{\partial l}| = x$ 之后指数从 $c-1$ 变成 $c$，散度恰好被坐标换掉了。

**用自己的手算验证这条「Jacobian 恰好救场」**：$P(x)\,dx = \frac{1}{\Gamma(c)s}(x/s)^{c-1}e^{-x/s}dx$，取 $x = e^{l}$，$dx = e^{l}dl$，得
$P(l) = \frac{1}{\Gamma(c)}(e^{l}/s)^{c}e^{-e^l/s}$，即 (23.18)。指数从 $c-1$ 抬到 $c$ 只因为多乘了一个 $x$。Exercise 23.2 的回答是 $P(u) = 3/u$：$x = u^3$、$dx/du = 3u^2$，故 $P(u) = (1/u^3)\cdot 3u^2 = 3/u$——**$1/x$ 在立方根变换下仍是 $1/u$ 型（只差常数 3）**，这就是「在 $\ln$ 尺度上不变」在任意幂变换下的推广形态。

**消失测试**：不换到 $\ln$ 坐标，$\sigma$ 或 $\tau$ 的 noninformative prior 只能写成 $1/\sigma$ / $1/\tau$ 这种「看起来像 bug 的 improper 密度」，无法在有限区间上做数值归一化；具体后果是你画出的后验密度在 $\sigma \to 0$ 处视觉上发散，采样器（Metropolis）会卡在这一端不断接受、把链粘死在 $10^{-6}$ 附近。换到 $\ln\sigma$ 后密度处处有限，这就是 (24.2) 之后那段 Reminder 的来由。

**落点**：本页 (23.17)；p.320 的 Reminder「变量从 $\sigma$ 换到 $l(\sigma)$ 时密度要乘 $|{\partial\sigma}/{\partial l}|$」；p.322 (24.14) 里把 $\sigma$ 换成 $\ln\sigma$ 求导才得到 $\sigma_{N-1}$。一条链串起三页。
</span>

gamma distribution 若在 $l = \ln x$ 上看，永远是单峰的，而且从图上能看出它是不对称的。如果 $x$ 服从 gamma distribution，而我们决定改用它的倒数 $v = 1/x$ 来工作，就得到一个新分布，其中 $l$ 上的密度左右翻转：$v$ 的概率密度称为 inverse-gamma distribution，

```math
P(v \mid s, c) = \frac{1}{Z_v}\left( \frac{1}{s v} \right)^{c+1} \exp\left( -\frac{1}{s v} \right), \qquad 0 \le v \lt \infty,
```

(23.20)

其中

```math
Z_v = \Gamma(c)/s.
```

(23.21)



[Figure 23.5：两个 inverse-gamma 分布，参数 $(s,c) = (1,3)$（粗线）与 $(10, 0.3)$（细线），四联排布与图 23.4 相同（线性/对数纵轴 × $x$ 与 $\ln x$ 两种横轴）。它是图 23.4 的镜像，用来展示「取倒数就是不换基、只左右翻转」。]

gamma 与 inverse gamma 分布在许多「从数据推断一个正量」的 inference 问题里反复出现。例子包括：从若干噪声样本推断 Gaussian 噪声的 variance；从计数推断 Poisson distribution 的 rate parameter。

这两种分布之所以成为「正量的默认选项」，是因为它们与 Gaussian 的 precision、Poisson 的 rate 互为 conjugate prior：Gaussian 噪声的 precision $\beta$ 的 conjugate prior 正是 (24.2) 的 gamma，Poisson 的 rate 的 conjugate prior 也是 gamma。于是「prior × likelihood → 同族后验」这一步不需要任何数值积分，只要把超参数与计数相加——情形与 (23.28) 的 beta 之于 Bernoulli 完全一样。反过来说，一旦你换掉 likelihood 的形状（比如换成 log-normal），共轭性就没了，marginalization 只能靠积分或采样（见第 24 章）。

gamma distribution 还自然地出现在「Poisson 分布事件之间的等待时间」的分布里。给定一个 rate 为 $\lambda$ 的 Poisson process，第 $m$ 个事件的到达时间 $x$ 的概率密度是

```math
\frac{\lambda (\lambda x)^{m-1}}{(m-1)!} e^{-\lambda x}.
```

(23.22)

把 $m = 1$ 代入，(23.22) 化为 $\lambda e^{-\lambda x}$，正是 (23.13) 在 $s = 1/\lambda$ 时的形状——这说明「第 $m$ 个到达的等待时间」是 $m$ 个独立 exponential 之和（Erlang 分布），其均值为 $m/\lambda$、方差为 $m/\lambda^2$。这条一致性是检查自己有没有读错参数化的最快办法：$\lambda = 2$、$m = 1$ 时均值应是 $0.5$，若算成 $2$，就一定是把 (23.13) 的 $s$ 当成了 rate。

### log-normal distribution（对数正态分布）

正实数 $x$ 上的另一个分布是 log-normal distribution，它是「$l = \ln x$ 服从 normal distribution」时所导致的分布。我们定义 $m$ 为 $x$ 的中位数（median），$s$ 为 $\ln x$ 的标准差。

```math
P(l \mid m, s) = \frac{1}{Z} \exp\left( -\frac{(l - \ln m)^2}{2 s^2} \right), \qquad l \in (-\infty, \infty),
```

(23.23)

其中

```math
Z = \sqrt{2\pi s^2},
```

(23.24)

由此推出

```math
P(x \mid m, s) = \frac{1}{x} \cdot \frac{1}{Z} \exp\left( -\frac{(\ln x - \ln m)^2}{2 s^2} \right), \qquad x \in (0, \infty).
```

(23.25)

[Figure 23.6：两个 log-normal 分布，参数 $(m, s) = (3, 1.8)$（粗线）与 $(3, 0.7)$（细线），线性与对数纵轴各一幅。它演示的是「中位数相同（$m = 3$）而形状可以差别巨大」——这就是 log-normal 里 $m$ 与均值不是一回事的图形证据（原书图注还特地补了一句「是的，它们的中位数真的一样」）。]



### 23.4 周期变量上的分布 · Distributions over periodic variables

periodic variable（周期变量）$\theta$ 是一个取值于 $[0, 2\pi]$ 的实数，具有「$\theta = 0$ 与 $\theta = 2\pi$ 等价」的性质。

对 periodic variable 而言，扮演「Gaussian 对实变量的那个角色」的分布，是 Von Mises distribution：

```math
P(\theta \mid \mu, \beta) = \frac{1}{Z}\exp\left( \beta \cos(\theta - \mu) \right), \qquad \theta \in (0, 2\pi).
```

(23.26)

归一化常数是 $Z = 2\pi I_0(\beta)$，其中 $I_0(x)$ 是 modified Bessel function（修正贝塞尔函数）。

<span style="color:#1e8449;">**[译注]**
(23.26) 与 Gaussian 的关系不是比喻，而是可以写成一个级数恒等式的：把 $\exp(\beta\cos\theta)$ 按 $\cos$ 的 Fourier 级数展开，得到
$\exp(\beta\cos\theta) = I_0(\beta) + 2\sum_{k\ge1} I_k(\beta)\cos(k\theta)$，所以 Von Mises 的「矩」全部由 $I_k(\beta)/I_0(\beta)$ 给出，第一个矩（即圆周上的平均方向向量的长度）是 $A(\beta) = I_1(\beta)/I_0(\beta)$。当 $\beta$ 大时 $A(\beta) \approx 1 - 1/(2\beta)$，分布退化成方差为 $1/\beta$ 的局部 Gaussian；当 $\beta = 0$ 时 $A = 0$，退化成 $[0,2\pi)$ 上的均匀分布。

**消失测试**：如果把周期量（风向、钟点、相位）当成普通实数用 Gaussian 建模，就会出现「$0.01\pi$ 与 $1.99\pi$ 被判成相距最远」的错误：两者的真实圆周距离是 $0.02\pi$，而欧氏差是 $1.98\pi$，误差因子约 $99$。可观测后果是 circular mean 算成 $\approx \pi$（即完全反方向），而不是接近 $0$。

**方向感**：$\beta$ 从 $0$ 增大到 $\infty$，分布从「均匀」连续过渡到「尖峰」，浓度参数 $\beta$ 与 Gaussian 的 precision $\tau = 1/\sigma^2$ 在同一量纲上对应（大 $\beta$ 时 $\beta \approx 1/\sigma^2$，差因子 1）。

**落点**：(23.27) 的 wrapped Gaussian 是同一问题的另一条路；(23.26) 在实现层对应 `scipy.stats.vonmises(kappa=beta)`；circular statistics 的均值与置信区间都由 $A(\beta)$ 支撑。
</span>

围绕圆周做 Brownian diffusion 所导致的分布，是 wrapped Gaussian distribution：

```math
P(\theta \mid \mu, \sigma) = \sum_{n=-\infty}^{\infty} \mathrm{Normal}(\theta;\, (\mu + 2\pi n),\, \sigma^2), \qquad \theta \in (0, 2\pi).
```

(23.27)

### 23.5 概率上的分布 · Distributions over probabilities
**Beta distribution、Dirichlet distribution、entropic distribution**

beta distribution 是变量 $p$ 上的概率密度，而 $p$ 本身是一个概率，$p \in (0, 1)$：

```math
P(p \mid u_1, u_2) = \frac{1}{Z(u_1, u_2)} p^{u_1-1}(1-p)^{u_2-1}.
```

(23.28)

参数 $u_1, u_2$ 可以取任意正值。归一化常数是 beta function：

```math
Z(u_1, u_2) = \frac{\Gamma(u_1)\Gamma(u_2)}{\Gamma(u_1 + u_2)}.
```

(23.29)

特例包括：uniform distribution——$u_1 = 1, u_2 = 1$；Jeffreys prior——$u_1 = 0.5, u_2 = 0.5$；以及 improper 的 Laplace prior——$u_1 = 0, u_2 = 0$。如果把 beta distribution 变换成 logit $l \equiv \ln\left( p/(1-p) \right)$ 上的密度，会发现它在 $l$ 上永远是宜人的钟形密度，而 $p$ 上的密度可能在 $p = 0$ 与 $p = 1$ 处有奇点（图 23.7）。

[Figure 23.7：三个 beta 分布，$(u_1, u_2) = (0.3, 1)$、$(1.3, 1)$、$(12, 2)$。上幅是 $P(p \mid u_1,u_2)$ 作为 $p$ 的函数，下幅是同一个分布在 logit $\ln(p/(1-p))$ 上的密度。它演示的是「$u_1 \lt 1$ 时 $p$ 坐标下在 $p=0$ 处发散，而 logit 坐标下处处光滑」。]

#### 更多维 · More dimensions

Dirichlet distribution 是 $I$ 维向量 $\mathbf{p}$ 上的密度，$\mathbf{p}$ 的 $I$ 个分量都为正且和为 1。beta distribution 是 $I = 2$ 时 Dirichlet distribution 的特例。Dirichlet distribution 由测度 $\mathbf{u}$（所有分量 $u_i \gt 0$ 的向量）参数化；这里我把它写成 $\mathbf{u} = \alpha \mathbf{m}$，其中 $\mathbf{m}$ 是 $I$ 个分量上的归一化测度（$\sum_i m_i = 1$），$\alpha$ 为正：

```math
P(\mathbf{p} \mid \alpha\mathbf{m}) = \frac{1}{Z(\alpha\mathbf{m})} \prod_{i=1}^{I} p_i^{\alpha m_i - 1}\; \delta\left( \sum_i p_i - 1 \right) \equiv \mathrm{Dirichlet}^{(I)}(\mathbf{p} \mid \alpha\mathbf{m}).
```

(23.30)

函数 $\delta(x)$ 是 Dirac delta function，它把分布限制到 simplex（单纯形）上，使 $\mathbf{p}$ 归一化，即 $\sum_i p_i = 1$。Dirichlet distribution 的归一化常数是：

```math
Z(\alpha\mathbf{m}) = \prod_i \Gamma(\alpha m_i) / \Gamma(\alpha).
```

(23.31)

向量 $\mathbf{m}$ 正是这个概率分布的均值：

```math
\int \mathrm{Dirichlet}^{(I)}(\mathbf{p} \mid \alpha\mathbf{m})\, \mathbf{p}\, d^{I}p = \mathbf{m}.
```

(23.32)



处理概率向量 $\mathbf{p}$ 时，常有用的是换到「softmax basis」。例如三维概率 $\mathbf{p} = (p_1, p_2, p_3)$ 用三个满足 $a_1 + a_2 + a_3 = 0$ 的数 $a_1, a_2, a_3$ 表示，且

```math
p_i = \frac{1}{Z} e^{a_i}, \qquad \text{其中 } Z = \sum_i e^{a_i}.
```

(23.33)

这个非线性变换，与 scale variable 的 $\sigma \to \ln\sigma$ 变换、以及单个概率的 logit 变换 $p \to \ln\left( p/(1-p) \right)$ 是同类的东西。

[Figure 23.8：三个三维 Dirichlet 分布，$\mathbf{u} = (20, 10, 7)$、$(0.2, 1, 2)$、$(0.2, 0.3, 0.15)$。上排是各分布抽出的 1000 个随机样本，两轴为 $p_1$ 与 $p_2$（$p_3 = 1 - (p_1+p_2)$），第一幅里那个三角形就是合法概率分布的 simplex；下排是同样这些点在 softmax basis 下的位置，两轴为 $a_1$ 与 $a_2$（$a_3 = -a_1 - a_2$）。它演示的是「$\alpha$ 大则样本紧贴中心 $\mathbf{m}$，$\alpha$ 小则样本贴到 simplex 的顶点附近」。]

在 softmax basis 下，Dirichlet distribution (23.30) 指数里那些难看的「减一」消失了，密度变成：

```math
P(\mathbf{a} \mid \alpha\mathbf{m}) \propto \frac{1}{Z(\alpha\mathbf{m})} \prod_{i=1}^{I} p_i^{\alpha m_i}\; \delta\left( \sum_i a_i \right).
```

(23.34)

参数 $\alpha$ 的作用可以用两种方式来刻画。第一，$\alpha$ 度量这个分布的**尖锐程度**（图 23.8）：它度量我们预期从该分布抽到的典型样本 $\mathbf{p}$ 与均值 $\mathbf{m}$ 相差多远，正如 Gaussian 的 precision $\tau = 1/\sigma^2$ 度量样本从均值游走多远。$\alpha$ 很大时，$\mathbf{p}$ 上的分布紧紧集中在 $\mathbf{m}$ 附近。

$\alpha$ 在高维情形下的效果可以这样可视化：从 $\mathrm{Dirichlet}^{(I)}(\mathbf{p} \mid \alpha\mathbf{m})$ 抽一个典型样本，令 $\mathbf{m}$ 取均匀向量 $m_i = 1/I$，然后画 Zipf plot，即把各分量 $p_i$ 的值按秩排序后作图。传统做法是把 $p_i$（纵轴）与秩（横轴）都取对数标度，这样幂律关系就表现为直线。图 23.9 给出 $I = 100$ 与 $I = 1000$、$\alpha$ 从 $0.1$ 到 $1000$ 时各一个样本的 Zipf plot。

$\alpha$ 很大时，图是浅的，许多分量取值相近。$\alpha$ 很小时，典型情形是某一个分量 $p_i$ 独占了压倒性的概率份额，而在剩余待分配的那点小概率里，又有另一个分量 $p_{i'}$ 拿走同样占压倒性比例的份额。当 $\alpha$ 趋于零时，图趋向于一条越来越陡的幂律。

[Figure 23.9：$I = 100$ 与 $I = 1000$ 两组、$\alpha = 0.1 \ldots 1000$ 各一例的 Dirichlet 样本 Zipf plot，纵轴为 $p_i$、横轴为秩，双对数。它演示的是「$\alpha$ 越小，样本越像少数几个分量吃掉几乎全部概率」——这是「稀疏 prior 从哪来」的图形答案。]

<span style="color:#1e8449;">**[译注]**
$\alpha$ 的两种解释（尖锐程度 / 数据要压过先验需要多少个样本）在这页紧挨着出现，容易被读成两个不相干的性质，其实是同一个数的两面：**$\alpha$ 就是「先验等价于多少条虚拟观测」**。

**用数字钉住第二种解释**：Dirichlet 与 categorical likelihood 共轭，观测到计数 $\mathbf{F} = (F_1,\ldots,F_I)$ 之后，后验仍是 Dirichlet，参数从 $\alpha m_i$ 变成 $\alpha m_i + F_i$。于是后验均值
$\mathbb{E}[p_i] = (\alpha m_i + F_i)/(\alpha + F_{\text{tot}})$。**取 $\alpha = 100$、$m_i = 1/I$；若 $I = 100$ 且某个分量被观测了 $F_1 = 100$ 次，则后验均值为 $(1 + 100)/(100+100) = 0.505$**——先验与数据各占一半，说明 $\alpha = 100$ 相当于 $100$ 条虚拟观测。这个换算使 (23.34) 与「$\alpha$ 大则尖锐」变成同一句话：先验越「结实」，需要的样本越多。

**消失测试**：抽掉 Dirichlet 的共轭性，你就得不到闭式后验 $\alpha m + \mathbf{F}$，只能对 $I-1$ 维 simplex 做数值积分；更具体地，$I = 1000$ 时 simplex 上的网格法代价是每维 $G$ 格、总共 $G^{999}$，任何 $G \ge 2$ 都不可算。共轭性把这件事降成一次向量加法。

**落点**：(23.28)–(23.34)；Exercise 23.3（p.317–318）用「红蓝两面 vs 六面」验证聚合一致性；工程实现见 `numpy.random.dirichlet` 的 `alpha` 参数与 LDA 的 `alpha`/`beta` 超参数（`sklearn.decomposition.LatentDirichletAllocation`）。
</span>

[exercise] **Exercise 23.3.**[3] The Dirichlet distribution satisfies a nice additivity property. Imagine that a biased six-sided die has two red faces and four blue faces. The die is rolled $N$ times and two Bayesians examine the outcomes in order to infer the bias of the die and make predictions. One Bayesian has access to the red/blue colour outcomes only, and he infers a two-component probability vector $(p_R, p_B)$. The other Bayesian has access to each full outcome: he can see which of the six faces came up, and he infers a six-component probability vector $(p_1, p_2, p_3, p_4, p_5, p_6)$, where $p_R = p_1 + p_2$ and $p_B = p_3 + p_4 + p_5 + p_6$. Assuming that the second Bayesian assigns a Dirichlet distribution to $(p_1, p_2, p_3, p_4, p_5, p_6)$ with hyperparameters $(u_1, u_2, u_3, u_4, u_5, u_6)$, show that, in order for the first Bayesian's inferences to be consistent with those of the second Bayesian, the first Bayesian's prior should be a Dirichlet distribution with hyperparameters $((u_1+u_2), (u_3+u_4+u_5+u_6))$. Hint: a brute-force approach is to compute the integral $P(p_R, p_B) = \int d^6p\, P(\mathbf{p} \mid \mathbf{u})\, \delta(p_R - (p_1+p_2))\, \delta(p_B - (p_3+p_4+p_5+p_6))$. A cheaper approach is to compute the predictive distributions, given arbitrary data $(F_1, F_2, F_3, F_4, F_5, F_6)$, and find the condition for the two predictive distributions to match for all data.

> **中文话题摘要**：一个只看得见红/蓝的 Bayesian 与一个看得见六面的 Bayesian 必须给出彼此一致的推断——这要求两边的 Dirichlet 超参数在「合并分量」时按加法聚合，$\mathbf{u} \to (u_1+u_2,\; u_3+u_4+u_5+u_6)$；两种证法：硬算六重积分，或走 predictive distribution。



概率向量 $\mathbf{p}$ 的 entropic distribution 有时被「最大熵」图像重建圈子使用：

```math
P(\mathbf{p} \mid \alpha, \mathbf{m}) = \frac{1}{Z(\alpha, \mathbf{m})} \exp\left[ -\alpha D_{\mathrm{KL}}(\mathbf{p} \,\|\, \mathbf{m}) \right] \delta\left( \sum_i p_i - 1 \right),
```

(23.35)

其中测度 $\mathbf{m}$ 是一个正向量，且 $D_{\mathrm{KL}}(\mathbf{p} \,\|\, \mathbf{m}) = \sum_i p_i \log \frac{p_i}{m_i}$。

(23.35) 与 (23.30) 的结构差别可以直接看出来：Dirichlet 的指数是 $\sum_i (\alpha m_i - 1)\ln p_i$，是 $\ln p_i$ 的**线性**组合；entropic distribution 的指数是 $-\alpha \sum_i p_i \ln(p_i/m_i)$，是 $p\ln p$ 的**凸**函数。前者把「各分量独立」的直觉保留下来，所以有共轭性、有闭式的 $\alpha\mathbf{m}+\mathbf{F}$ 后验；后者无法分解，因此不共轭。同一个「集中程度」旋钮 $\alpha$，在两者身上因此有了完全不同的使用方式：前者靠加计数，后者只能靠数值优化或采样。

<span style="color:#1e8449;">**[译注]**
(23.35) 是本章唯一一个**不共轭**的概率分布，而它出现在这里，恰恰是为了说明「共轭」并非必然。

**为什么它不共轭**：$D_{\mathrm{KL}}$ 里的 $p_i\ln p_i$ 是 $p_i$ 的严格凸函数，乘上 likelihood 之后落不进任何指数族的封闭形式。取 $I = 2$、$p_2 = 1 - p_1$，则 $D_{\mathrm{KL}} = p_1\ln(p_1/m_1) + (1-p_1)\ln((1-p_1)/m_2)$，其二阶导为 $1/p_1 + 1/(1-p_1) \ge 4$，把这条曲线塞进 $e^{-\alpha D}$ 得到的是一个「挤扁的 logit 正态」形状，而不是 beta 形状。

**消失测试**：抽掉 $\alpha$ 这个「温度」参数，最大熵图像重建就只剩「在 simplex 上解一个无约束凸问题」，答案唯一、没有可报告的不确定性；而 (23.35) 让最大熵解成为一个分布的唯一 mode，其余概率质量给出误差棒。可观测后果：$\alpha \to \infty$ 时 $P$ 塌成 $\mathbf{p} = \mathbf{m}$ 处的 delta 峰，$\alpha \to 0$ 时退化为 simplex 上的均匀密度——**同一个公式同时给出「最大熵解」与「完全无知」两端**，这是它比 Dirichlet 更有用的地方。

**方向感**：$\alpha$ 从 $0$ 增到 $\infty$，支撑从「整个 simplex 的体积」收缩到「零体积」；实践上先把 $\alpha$ 在 $[10^{-2}, 10^{2}]$ 上扫一遍，再按数据的尺度定，而不是凭经验直接取 $1$。

**落点**：(23.35) 与 (23.30) 对照；最大熵图像重建这一派的做法见本章 Further reading 里的 (MacKay and Peto, 1995) 与 Skilling 的 MART 系列；Exercise 23.4（p.318）里 gamma 的 ML 解是本章最后一道「无闭式、只能求根」的对照题。
</span>

### 本节小结：五个分布族与它们的「共轭搭档」

| 分布族 | 参数化 | 共轭搭档（likelihood） | 本节位置 |
|---|---|---|---|
| Gamma | $(s, c)$ 或 $(b_\beta, c_\beta)$ | Gaussian 的 precision、Poisson 的 rate | (23.15)、(24.2) |
| Inverse-gamma | $(s, c)$ | Gaussian 的 variance | (23.20) |
| Beta | $(u_1, u_2)$ | Bernoulli / binomial 的 $f$ | (23.28) |
| Dirichlet | $\alpha\mathbf{m}$ | categorical / 多项分布的 $\mathbf{p}$ | (23.30) |
| Entropic | $(\alpha, \mathbf{m})$ | **无**（只能数值处理） | (23.35) |

#### Further reading（延伸阅读）

关于 Dirichlet 的各种好玩性质，见 (MacKay and Peto, 1995)。

### 23.6 进一步习题 · Further exercises

[exercise] **Exercise 23.4.**[2] $N$ datapoints $\{x_n\}$ are drawn from a gamma distribution $P(x \mid s, c) = \Gamma(x; s, c)$ with unknown parameters $s$ and $c$. What are the maximum likelihood parameters $s$ and $c$?

> **中文话题摘要**：从 $N$ 个样本求 gamma distribution 的两个参数的 maximum likelihood 解——关键在于 $c$ 没有闭式解，只能落成一个含 $\psi(c) = d\ln\Gamma(c)/dc$（digamma）的一维方程，再用数值求根。



---

## 24. Exact Marginalization（精确边缘化）

我们要怎样才能避开「把所有 hypothesis 逐一枚举」带来的指数级代价？

在我们屈尊降贵去用近似方法之前，先来考察两条做 exact marginalization 的路子：第一条是对连续变量（有时称为 nuisance parameter，冗余参数）做 marginalization，办法是做积分；第二条是对离散变量做求和，办法是 message-passing（消息传递）。

对连续参数做 exact marginalization，是一门「硬派」活动，属于那些对定积分玩得溜的人。本章会用到 gamma distribution；正如上一章解释过的，gamma distribution 与 Gaussian distribution 很像，区别在于 Gaussian 从 $-\infty$ 走到 $\infty$，而 gamma distribution 从 $0$ 走到 $\infty$。

<span style="color:#1e8449;">**[译注]**
章首这两句把全章的目标说得很清楚：**marginalization 是「用积分换掉一个参数」，而不是「给参数一个点估计」。** 这两件事在计算上差一个量级，在结论上可以完全不同。

**用一个可算的例子说明差距。** 设一维 Gaussian、N = 5 个样本、$\bar{x} = 1.0$、$S = \sum(x_n - \bar{x})^2 = 1.0$（正是图 24.1 的数据）。若把 $\mu$ 固定成 $\bar{x}$ 再对 $\sigma$ 求极大，结果是 $\sigma_N = \sqrt{S/N} = \sqrt{1/5} = 0.4472$；若先把 $\mu$ 积掉（等价于承认 $\mu$ 本身有 $\sigma/\sqrt{N}$ 的不确定性）再对 $\ln\sigma$ 求极大，结果是 $\sigma_{N-1} = \sqrt{S/(N-1)} = \sqrt{1/4} = 0.5000$。**同一条数据、同一个模型，两个答案差 $11.8\%$**，而后者才是后验密度 $P(\sigma \mid D)$ 的真正峰（图 24.1d）。

**消失测试**：抽掉本章这套积分技术，「$\sigma$ 的误差棒该用 $N$ 还是 $N-1$」就永远只能靠「教科书说 $N-1$ 无偏」来记；更具体的失效对象是 (24.13) 的 Occam factor——它是 marginalization 的副产品，没有 $\int P(\mu)\,d\mu$ 就写不出 $\ln(\sqrt{2\pi}\sigma/\sqrt{N}/\sigma_\mu)$ 这一项，也就得不到「参数个数要按 $\ln(\text{先验宽度}/\text{后验宽度})$ 交税」这条模型比较规则。

**方向感**：$\sigma_{N-1}/\sigma_N = \sqrt{N/(N-1)}$，$N = 5$ 时是 $1.118$，$N = 100$ 时是 $1.005$——偏差随 $N$ 按 $1/(2N)$ 衰减，所以小样本上看得见，大样本上是舍入误差量级。

**落点**：本章 §24.1 全节；Exercise 24.1（p.321 提出、p.323 解答）问的正是 $\sigma_N$ 为什么有偏；第 28 章把 Occam factor 推广成 model comparison 的主轴。线代侧只用 Strang 的二次型配平方，无越级。
</span>

### 24.1 推断 Gaussian distribution 的均值与方差

我们再次讨论一维 Gaussian distribution，用均值 $\mu$ 与标准差 $\sigma$ 参数化：

```math
P(x \mid \mu, \sigma) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \equiv \mathrm{Normal}(x; \mu, \sigma^2).
```

(24.1)

在推断这些参数时，我们必须指定它们的 prior distribution。prior 给了我们一个机会，把关于 $\mu$ 与 $\sigma$ 的特定知识（例如来自独立实验，或来自理论考量）纳入进来。如果我们没有这类知识，那就可以构造一个恰当的 prior 来表达我们「自认为的无知」。在 §21.2 里，我们假设了在所画参数范围上的 uniform prior。如果我们希望**能够做精确的 marginalization**，那么考虑 conjugate prior（共轭先验）可能是有用的；conjugate prior 是那种函数形式与 likelihood 自然结合、从而使推断具有方便形式的 prior。

#### $\mu$ 与 $\sigma$ 的 conjugate prior

均值 $\mu$ 的 conjugate prior 是 Gaussian：我们引入两个「hyperparameter（超参数）」$\mu_0$ 与 $\sigma_\mu$ 来参数化 $\mu$ 上的 prior，写

```math
P(\mu \mid \mu_0, \sigma_\mu) = \mathrm{Normal}(\mu;\, \mu_0,\, \sigma_\mu^2).
```

在 $\mu_0 = 0$、$\sigma_\mu \to \infty$ 的极限下，我们得到 location parameter 的 noninformative prior，即 flat prior。它之所以是 noninformative，是因为它在自然的重参数化 $\mu' = \mu + c$ 下不变。prior $P(\mu) = \text{const.}$ 同时也是一个 improper prior，也就是说，它不可归一化。

标准差 $\sigma$ 的 conjugate prior 是 gamma distribution，它有两个参数 $b_\beta$ 与 $c_\beta$。最方便的是定义**逆方差**（即 precision parameter）$\beta = 1/\sigma^2$ 的 prior 密度：



```math
P(\beta) = \Gamma(\beta; b_\beta, c_\beta) = \frac{1}{\Gamma(c_\beta)}\cdot \frac{\beta^{c_\beta - 1}}{b_\beta^{\,c_\beta}} \exp\left( -\frac{\beta}{b_\beta} \right), \qquad 0 \le \beta \lt \infty.
```

(24.2)

这是一个简单的单峰分布，均值为 $b_\beta c_\beta$，方差为 $b_\beta^2 c_\beta$。在极限 $b_\beta c_\beta = 1$、$c_\beta \to 0$ 下，我们得到 scale parameter 的 noninformative prior，即 $1/\sigma$ prior。它之所以是「noninformative」，是因为它在重参数化 $\sigma' = c\sigma$ 下不变。

如果我们去考察它在 $\ln\sigma$（或 $\ln\beta$）上的密度，会发现那个是平的，这样一来 $1/\sigma$ prior 看起来就没那么奇怪了。这个 prior 表达「对 $\sigma$ 的无知」的方式是：嗯，它可能是 $10$，也可能是 $1$，也可能是 $0.1$……像 $\sigma$ 这样的 scale variable，通常最好用它的对数来表示。同样地，这个 noninformative 的 $1/\sigma$ prior 也是 improper 的。

> **Reminder（原书边注）**：当我们把变量从 $\sigma$ 换到 $l(\sigma)$（$\sigma$ 的一一函数）时，概率密度从 $P_\sigma(\sigma)$ 变成 $P_l(l) = P_\sigma(\sigma)\left| \partial\sigma / \partial l \right|$。在这里，Jacobian 是 $\left| \partial\sigma / \partial \ln\sigma \right| = \sigma$。

在接下来的例子里，我会对 $\mu$ 与 $\sigma$ 使用 improper 的 noninformative prior。在某些圈子里，使用 improper prior 被视为失礼，所以请容许我为自己辩解一句：这么做是为了可读性；如果我把 proper prior 都写上，计算照样能做，但关键论点会被汹涌的额外参数淹没。

#### Maximum likelihood 与 marginalization：$\sigma_N$ 与 $\sigma_{N-1}$

从 $N$ 个样本推断 Gaussian distribution 的均值与标准差，是个熟悉的任务，不过也许并非每个人都理解自己计算器上 $\sigma_N$ 按钮与 $\sigma_{N-1}$ 按钮的区别。让我们先把公式复述一遍，然后推导它们。

给定数据 $D = \{x_n\}_{n=1}^{N}$，$\mu$ 的一个 estimator 是

```math
\bar{x} \equiv \sum_{n=1}^{N} x_n / N,
```

(24.3)

而 $\sigma$ 有两个 estimator：

```math
\sigma_N \equiv \sqrt{\frac{\sum_{n=1}^{N}(x_n - \bar{x})^2}{N}} \qquad \text{与} \qquad \sigma_{N-1} \equiv \sqrt{\frac{\sum_{n=1}^{N}(x_n - \bar{x})^2}{N-1}}.
```

(24.4)

统计有两大主要范式：sampling theory（抽样理论）与 Bayesian inference。在 sampling theory（也叫「频率派 frequentist」或正统统计学）里，人们先发明感兴趣的量的一些 estimator，然后用某种衡量其抽样性质的准则在这些 estimator 之间做选择；**至于该用哪个准则来衡量 estimator 的表现，并没有明确的原则**；而且对大多数准则而言，也不存在构造最优 estimator 的系统化流程。

相比之下，在 Bayesian inference 里，一旦我们把关于模型与数据的所有假设都讲明白，推断就是机械的。无论我们想提出什么问题，概率论的规则都会给出唯一答案，并且这个答案会一致地把给定的全部信息考虑进去。**人手设计的 estimator 与 confidence interval 在 Bayesian inference 里没有位置**；人的输入只进入两项重要工作：设计 hypothesis space（也就是指定模型及其全部概率分布），以及想清楚如何在那个空间里实现推断所需的计算。我们那些问题的答案，是感兴趣的量的概率分布。我们常常发现：当我们选一个简单的 hypothesis space、再摇动 Bayesian inference 的手柄时，sampling theory 的 estimator 会自动地作为这些后验分布的 mode 或 mean 浮现出来。



[Figure 24.1：Gaussian distribution 参数的 likelihood 函数（沿用图 21.5）。(a1, a2) log likelihood 作为 $\mu$ 与 $\sigma$ 的函数：曲面图与等高线图；数据是 $N = 5$ 个点，$\bar{x} = 1.0$、$S = \sum(x-\bar{x})^2 = 1.0$；注意极大在 $\sigma$ 方向上是斜的。两个标准差 estimator 的值分别是 $\sigma_N = 0.45$ 与 $\sigma_{N-1} = 0.50$。(c) 在若干固定 $\mu$ 值下 $\sigma$ 的后验概率（画成 $\ln\sigma$ 上的密度）。(d) 假设 $\mu$ 上是 flat prior、把 (a) 中的概率质量投影到 $\sigma$ 轴上得到的 $P(\sigma \mid D)$；它的极大在 $\sigma_{N-1}$。作为对照，$P(\sigma \mid D, \mu = \bar{x})$ 的极大在 $\sigma_N$。（两个概率都画成 $\ln\sigma$ 上的密度。）]

在 sampling theory 里，上述 estimator 可以这样来理解动机：$\bar{x}$ 是 $\mu$ 的无偏 estimator，并且在 $\mu$ 的全部可能无偏 estimator 中它方差最小（这里的方差是通过对一整个假想实验的 ensemble 求平均算出来的，那些假想实验中数据样本被假定来自一个未知的 Gaussian distribution）。estimator $(\bar{x}, \sigma_N)$ 是 $(\mu, \sigma)$ 的 maximum likelihood estimator。然而 $\sigma_N$ 是**有偏**的：给定 $\sigma$、在大量假想实验上求平均时，$\sigma_N$ 的期望值并不是 $\sigma$。

[exercise] **Exercise 24.1.**[2, p.323] Give an intuitive explanation why the estimator $\sigma_N$ is biased.

> **中文话题摘要**：用直觉解释 $\sigma_N$ 为什么有偏——关键是「样本均值本身就是使平方偏差和最小的那个 $\mu$，而真值 $\mu$ 一般不等于样本均值」。

正是这个偏差，促使 sampling theory 发明了 $\sigma_{N-1}$，它可以被证明是无偏 estimator。或者更准确地说，$\sigma_{N-1}^{2}$ 才是 $\sigma^{2}$ 的无偏 estimator。

现在我们来看这个问题的若干 Bayesian 推断，假设 $\mu$ 与 $\sigma$ 都取 noninformative prior。于是重点不在于 prior，而在于 (a) likelihood 函数，以及 (b) marginalization 这个概念。

$\mu$ 与 $\sigma$ 的联合后验概率正比于图 24.1a 中等高线所画的 likelihood 函数。log likelihood 是：

```math
\ln P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma) = -N \ln(\sqrt{2\pi}\,\sigma) - \sum_n (x_n - \mu)^2/(2\sigma^2)
```

(24.5)

```math
= -N \ln(\sqrt{2\pi}\,\sigma) - \left[ N(\mu - \bar{x})^2 + S \right]/(2\sigma^2),
```

(24.6)

其中 $S \equiv \sum_n (x_n - \bar{x})^2$。在 Gaussian 模型下，likelihood 可以只用数据的两个函数 $\bar{x}$ 与 $S$ 表达出来，所以这两个量被称为 sufficient statistics（充分统计量）。$\mu$ 与 $\sigma$ 的后验概率，在使用 improper prior 时是：

```math
P(\mu, \sigma \mid \{x_n\}_{n=1}^{N}) = \frac{P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma)\, P(\mu, \sigma)}{P(\{x_n\}_{n=1}^{N})}
```

(24.7)

```math
= \frac{1}{(2\pi\sigma^2)^{N/2}} \exp\left( -\frac{N(\mu-\bar{x})^2 + S}{2\sigma^2} \right) \cdot \frac{1}{\sigma_\mu}\cdot \frac{1}{\sigma} \cdot \frac{1}{P(\{x_n\}_{n=1}^{N})}.
```

(24.8)



这个函数描述的是对这个问题的回答：「给定数据与 noninformative prior，$\mu$ 与 $\sigma$ 可能是什么？」找出使后验概率最大的参数值也许是有意思的，但必须强调：**后验概率的极大点本身在 Bayesian inference 里没有任何根本地位**，因为它的位置取决于基（basis）的选择。这里我们选择基 $(\mu, \ln\sigma)$，在这个基下我们的 prior 是平的，于是后验概率的极大点与 likelihood 的极大点重合。正如我们在 Exercise 22.4（p.302）看到的，$\mu$ 与 $\ln\sigma$ 的 maximum likelihood 解是

```math
\{\mu, \sigma\}_{\mathrm{ML}} = \left\{ \bar{x},\; \sigma_N = \sqrt{S/N} \right\}.
```

后验分布的内容远不止它的 mode。从图 24.1a 可以看到，likelihood 的峰是斜的。当我们增大 $\sigma$ 时，$\mu$ 的条件分布的宽度随之增大（图 22.1b）。而若我们把 $\mu$ 依次固定到一串逐渐远离样本均值 $\bar{x}$ 的值上，就得到一串 $\sigma$ 的条件分布，它们的极大点移向越来越大的 $\sigma$（图 24.1c）。

给定 $\sigma$ 时 $\mu$ 的后验概率是

```math
P(\mu \mid \{x_n\}_{n=1}^{N}, \sigma) = \frac{P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma)\, P(\mu)}{P(\{x_n\}_{n=1}^{N} \mid \sigma)}
```

(24.9)

```math
\propto \exp\left( -N(\mu - \bar{x})^2/(2\sigma^2) \right)
```

(24.10)

```math
= \mathrm{Normal}(\mu;\, \bar{x},\, \sigma^2/N).
```

(24.11)

我们注意到 $\mu$ 的误差棒呈现熟悉的 $\sigma/\sqrt{N}$ 标度。

现在让我们问第二个问题：「给定数据与 noninformative prior，$\sigma$ 可能是什么？」这个问题与我们问的第一个问题差别在于：现在我们**不关心** $\mu$。因此这个参数必须被 marginalize 掉。$\sigma$ 的后验概率是：

```math
P(\sigma \mid \{x_n\}_{n=1}^{N}) = \frac{P(\{x_n\}_{n=1}^{N} \mid \sigma)\, P(\sigma)}{P(\{x_n\}_{n=1}^{N})}.
```

(24.12)

依赖于数据的项 $P(\{x_n\}_{n=1}^{N} \mid \sigma)$ 前面已经在 (24.9) 里作为归一化常数出现过；这个量有一个名字，叫 $\sigma$ 的「evidence」，或称为 marginal likelihood。我们把 $\mu$ 积分掉来得到 $\sigma$ 的 evidence；这里假定 $\mu$ 的 noninformative prior 为 $P(\mu) = \text{constant}$，我们把这个常数记作 $1/\sigma_\mu$，这样就可以把该 prior 想成宽度为 $\sigma_\mu$ 的 top-hat prior。Gaussian 积分

```math
P(\{x_n\}_{n=1}^{N} \mid \sigma) = \int P(\{x_n\}_{n=1}^{N} \mid \mu, \sigma)\, P(\mu)\, d\mu
```

给出：

```math
\ln P(\{x_n\}_{n=1}^{N} \mid \sigma) = -N \ln(\sqrt{2\pi}\,\sigma) - \frac{S}{2\sigma^2} + \ln\left( \frac{\sqrt{2\pi}\,\sigma/\sqrt{N}}{\sigma_\mu} \right).
```

(24.13)

前两项是 best-fit log likelihood（即取 $\mu = \bar{x}$ 时的 log likelihood）。最后一项是 Occam factor 的对数，它对较小的 $\sigma$ 取值施加惩罚。（我们将在第 28 章更多地讨论 Occam factor。）当我们对 log evidence 关于 $\ln\sigma$ 求导、以找出最可能的 $\sigma$ 时，那个额外的 volume factor $(\sigma/\sqrt{N})$ 把极大点从 $\sigma_N$ 移到了

```math
\sigma_{N-1} = \sqrt{S/(N-1)}.
```

(24.14)

直觉上，分母 $(N-1)$ 数的是 $S = \sum_n (x_n - \bar{x})^2$ 这个量里**含有多少次噪声测量**。这个和里有 $N$ 个残差平方，但有效的噪声测量只有 $(N-1)$ 次，因为从数据里确定一个参数 $\mu$ 这件事，让噪声的一个维度在无法避免的 overfitting 中被吃掉了。用经典统计学的术语说：Bayesian 对 $\sigma$ 的最佳猜测，是让

```math
\chi^2 \equiv \sum_n (x_n - \hat{\mu})^2/\hat{\sigma}^2
```

等于自由度数目 $N-1$ 的那个值。

<span style="color:#1e8449;">**[译注]**
(24.13) 是本章唯一真正不可替代的式子，因为它是全书第一次把「**参数的不确定性折算成对模型的罚分**」写成可读的算术。拆开看：前两项是「拟合得多好」，第三项是「模型为了让 $\mu$ 落在数据附近，花了多少体积」。

**第三项的来路可以一句算清**：$\int \exp(-N(\mu-\bar{x})^2/(2\sigma^2))\, d\mu = \sqrt{2\pi\sigma^2/N}$，除以 prior 宽度 $\sigma_\mu$ 的倒数……更准确地说，积分 $\int P(\mu) d\mu = 1/\sigma_\mu \cdot \sigma_\mu = 1$ 只是归一化，真正的 Occam factor 是「后验允许 $\mu$ 活动的宽度」比「先验允许的宽度」，即
$\dfrac{\sqrt{2\pi}\,\sigma/\sqrt{N}}{\sigma_\mu}$。所以 (24.13) 的最后一项就是 $\ln\!\left(\dfrac{\text{后验宽度}}{\text{先验宽度}}\right)$，永远是**负**的（宽度收缩），收缩得越狠罚得越重。

**为什么它把极大点从 $\sigma_N$ 推到 $\sigma_{N-1}$**：对 $\ln\sigma$ 求导时，第三项贡献 $\partial_{\ln\sigma}\ln(\sigma/\sqrt{N}/\sigma_\mu) = 1$，而 $-S/(2\sigma^2)$ 贡献 $+S/\sigma^2$，两项相加为零给出 $\sigma^2 = S/(N-1)$。若没有这个 $+1$，方程就是 $\sigma^2 = S/N$。**一个常数 1 之差，就是 $N$ 与 $N-1$ 的全部区别**，也是「自由度损失」这个说法的严格来路。

**消失测试**：抽掉 $\int d\mu$，你会得到一个自相矛盾的处境——likelihood 的极大点声称 $\hat\sigma^2 = S/N$，而同一个后验的密度峰在 $S/(N-1)$，且某些抽样实验里 $S/N$ 系统性地偏小（Exercise 24.1 的答案：样本均值就是使平方偏差和最小的那个 $\mu$）。可观测后果：在 $N = 5$ 时误差棒低估约 $11.8\%$，做 A/B 检验时会把噪声水平压得过于乐观，从而把噪声当成效应。

**落点**：(24.13) 的 Occam factor → 第 28 章 model comparison；同一结构在 (24.2) 的 gamma prior 归一化里已经出现；Exercise 24.1 的直觉解释在 p.323 的 solution 里。
</span>



图 24.1d 展示了 $\sigma$ 的后验概率，它正比于 marginal likelihood。这可以与「把 $\mu$ 固定在其最可能值 $\bar{x} = 1$ 时 $\sigma$ 的后验概率」相对照，后者见图 24.1c 与 24.1d。

我们可能想做的最后一个推断是：「给定数据，$\mu$ 是什么？」

[exercise] **Exercise 24.2.**[3] Marginalize over $\sigma$ and obtain the posterior marginal distribution of $\mu$, which is a Student-t distribution:

```math
P(\mu \mid D) \propto 1/\left[ N(\mu - \bar{x})^2 + S \right]^{N/2}.
```

(24.15)

> **中文话题摘要**：把 $\sigma$ 也积掉，得到 $\mu$ 的后验边缘分布——结果恰好是 (23.8) 的 Student-t，自由度 $N$，尺度由 $S$ 与 $N$ 决定。这是「Student-t 从哪来」在本书里的正式答案。

#### Further reading（延伸阅读）

要说 exact marginalization 的圣经，那是 Bretthorst (1988) 关于 Bayesian spectrum analysis 与参数估计的书。

### 24.2 习题 · Exercises

[exercise] **Exercise 24.3.**[3] [This exercise requires macho integration capabilities.] Give a Bayesian solution to exercise 22.15 (p.309), where seven scientists of varying capabilities have measured $\mu$ with personal noise levels $\sigma_n$, and we are interested in inferring $\mu$. Let the prior on each $\sigma_n$ be a broad prior, for example a gamma distribution with parameters $(s, c) = (10, 0.1)$. Find the posterior distribution of $\mu$. Plot it, and explore its properties for a variety of data sets such as the one given, and the data set $\{x_n\} = \{13.01, 7.39\}$. [Hint: first find the posterior distribution of $\sigma_n$ given $\mu$ and $x_n$, $P(\sigma_n \mid x_n, \mu)$. Note that the normalizing constant for this inference is $P(x_n \mid \mu)$. Marginalize over $\sigma_n$ to find this normalizing constant, then use Bayes' theorem a second time to find $P(\mu \mid \{x_n\})$.]

> **中文话题摘要**：把第 309 页「七个科学家」那道题用 Bayesian 方法正面解掉——每个科学家的 $\sigma_n$ 各给一个宽 gamma prior，先算 $P(\sigma_n \mid x_n, \mu)$，其中的归一化常数恰是 $P(x_n \mid \mu)$，把它对 $\sigma_n$ 积掉，再用一次 Bayes 定理得 $P(\mu \mid \{x_n\})$。结果会把「A、B 两个科学家自动被降权」这件事显式地算出来。

### 24.3 解答 · Solutions

**Solution to exercise 24.1（p.321）。**

1. 数据点围绕**真**均值的平均平方偏差是 $\sigma^2$。
2. 样本均值不太可能恰好等于真均值。
3. 样本均值是使「数据点对 $\mu$ 的平方偏差和」最小的那个 $\mu$。任何别的 $\mu$ 值（特别是 $\mu$ 的真值）都会给出比 $\mu = \bar{x}$ 时更大的平方偏差和。

所以，围绕样本均值的期望平均平方偏差，必然小于围绕真均值的平均平方偏差 $\sigma^2$。

<span style="color:#1e8449;">**[译注]**
这里的第 3 条是一个**变分刻画**，不是比喻：$\bar{x} = \arg\min_{\mu} \sum_n (x_n-\mu)^2$。于是对任意 $\mu$ 都有 $\sum_n (x_n-\bar{x})^2 \le \sum_n (x_n-\mu)^2$，取期望即得 $\mathbb{E}[\sigma_N^2] \le \sigma^2$——有偏的方向被一句话钉死：**只会低估，不会高估**。经典结果给出精确量 $\mathbb{E}[\sigma_N^2] = \frac{N-1}{N}\sigma^2$，所以 $\sigma_{N-1}^2 = \frac{N}{N-1}\sigma_N^2$ 才无偏；$N = 5$ 时标准差上低估 $\sqrt{0.8} = 0.894$（约 $10.6\%$），$N = 2$ 时低估 $29.3\%$。

**消失测试**：抽掉「$\bar{x}$ 是和平方的最小点」这个变分事实，偏差方向就无从解释，只能死记「$N-1$ 修正」；换了估计对象（例如要估 $\sigma$ 的倒数，或要估 $(\mu,\sigma)$ 的联合置信域）规则不能照搬，方向感随之丢失。而 Bayesian 路线给的是整条 $P(\sigma \mid D)$，偏差问题不需要「修正项」这个补丁。

**方向感与落点**：偏差按 $1/N$ 衰减（$N = 5$ 差 $10.6\%$，$N = 100$ 差 $0.5\%$）；同一事实在 (24.13) 里以 volume factor $\sigma/\sqrt{N}$ 的形态出现，两条路指向同一个 $N-1$。
</span>



## 25. Exact Marginalization in Trellises（trellis 上的精确边缘化）

本章讨论概率建模里几种**精确**（exact）方法。作为例子我们处理线性纠错码的解码任务。会看到：推断可以最高效地由 message-passing 算法完成 —— 这类算法利用问题的**图结构**（graphical structure）来避免不必要的重复计算（见第 16 章）。

### 25.1 Decoding problems（解码问题）

一个 codeword $\mathbf{t}$ 从线性 $(N,K)$ 码 $C$ 里选出，经有噪声信道传输；接收信号是 $\mathbf{y}$。本章假定信道是 **memoryless channel**，例如 Gaussian channel。给定假定的信道模型 $P(\mathbf{y} \mid \mathbf{t})$，有两个解码问题。

- **codeword decoding problem**：给定接收信号，推断**哪一个** codeword $\mathbf{t}$ 被发送。
- **bitwise decoding problem**：对每个发送比特 $t_n$，推断它「是 1 而不是 0」的可能性有多大。

具体例子取 $(7,4)$ Hamming code。第 1 章里我们讨论过该码在 binary symmetric channel 下的 codeword decoding problem，但既没讨论 bitwise decoding problem，也没讨论如何处理更一般的信道模型（如 Gaussian channel）。

#### 解 codeword decoding problem

按 Bayes 定理，codeword $\mathbf{t}$ 的后验概率是

```math
P(\mathbf{t} \mid \mathbf{y}) = \frac{P(\mathbf{y} \mid \mathbf{t})\,P(\mathbf{t})}{P(\mathbf{y})}.
```

(25.1)

**Likelihood function。** 分子里的第一个因子 $P(\mathbf{y} \mid \mathbf{t})$ 是 codeword 的 likelihood；对任何 memoryless channel，它都是**可分离**（separable）函数：

```math
P(\mathbf{y} \mid \mathbf{t}) = \prod_{n=1}^{N} P(y_n \mid t_n).
```

(25.2)

例如，若信道是 Gaussian channel、发送值为 $\pm x$、加性噪声标准差为 $\sigma$，那么概率密度



在 $t_n = 0,\,1$ 两种情形下分别是

```math
P(y_n \mid t_n = 1) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(y_n - x)^2}{2\sigma^2}\right),
```

(25.3)

```math
P(y_n \mid t_n = 0) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(y_n + x)^2}{2\sigma^2}\right).
```

(25.4)

从解码的角度看，唯一重要的是 likelihood ratio；在 Gaussian channel 情形下它是

```math
\frac{P(y_n \mid t_n = 1)}{P(y_n \mid t_n = 0)} = \exp\!\left(\frac{2 x y_n}{\sigma^2}\right).
```

(25.5)

[exercise] **Exercise 25.1.**[2] Show that from the point of view of decoding, a Gaussian channel is equivalent to a time-varying binary symmetric channel with a known noise level $f_n$ which depends on $n$.

> **中文话题摘要**：证明「从解码角度，Gaussian channel 等价于一个**时变** BSC」，其时变噪声水平 $f_n$ 只依赖 $n$。这是第 1 章 BSC 结果向连续信道推广的那座桥。

<span style="color:#1e8449;">**[译注] 本段为回补**

这一页是**补译**：原块（p321-340）交付时，从 `p335` 到 `p338` 之间跨了三个源页，落页标记时把 p336 整页与 p337 上半页**连标记带正文一起丢了**，只剩 p337 从「Prior.」往后的部分。回补后本块页标记 20 个齐全。

**回补时核过的三处**：
1. **(25.5) 的方向**：原文印的是 $P(y_n\mid t_n{=}1)/P(y_n\mid t_n{=}0) = \exp(2xy_n/\sigma^2)$。做一次数值自检即可定方向：取 $x>0$、$y_n>0$（接收值偏向 $+x$），比值应 $>1$，公式给 $\exp(+)$ ✓；若把分子分母写反，比值 $<1$ 就与「收到正值更可能是 $t_n=1$」矛盾。
2. **(25.3) 与 (25.4) 只差 $y_n$ 的符号**：两式的指数分别是 $-(y_n-x)^2$ 与 $-(y_n+x)^2$，相加不为常数（不是互补概率，因为这是**连续**密度）—— 这一点常被误当成「$P(t{=}1)+P(t{=}0)=1$」而去凑常数，实际上两者都归一化为 1。
3. **(25.2) 的「separable」是整章的地基**：没有它，$P(\mathbf{y}\mid\mathbf{t})$ 无法拆成 $\prod_n P(y_n\mid t_n)$，第 16 章的 message-passing 就无从施加，25.3 节的 min–sum 也不能逐位乘。

**落点**：§25.1 本页；(25.2) → §16 factor graph 的因子分解；(25.5) → §25.3 逐位 LLR 递推的输入。

</span>

**Prior。** 分子里的第二个因子是码字的先验概率 $P(\mathbf{t})$，通常假定它在所有合法码字上均匀。

(25.1) 的分母是归一化常数

```math
P(\mathbf{y}) = \sum_{\mathbf{t}} P(\mathbf{y} \mid \mathbf{t})\, P(\mathbf{t}).
```

(25.6)

codeword decoding problem 的完整解，是所有码字及其概率的一张清单，概率由 (25.1) 给出。由于线性码的码字个数 $2^{K}$ 往往非常大，而我们并不关心所有码字的详细概率，所以经常把注意力限制在 codeword decoding problem 的一个简化版本上。

**MAP codeword decoding problem**：给定接收信号，找出**最可能**的那个码字 $\mathbf{t}$。

如果码字上的先验概率是均匀的，那么这个任务就等同于 maximum likelihood decoding，即找出使 $P(\mathbf{y} \mid \mathbf{t})$ 最大的码字。

**例**：在第 1 章里，对 $(7, 4)$ Hamming code 与 binary symmetric channel，我们讨论了一种从接收信号的 syndrome 反推最可能码字的方法，从而在那个情形下解决了 MAP codeword decoding problem。我们想要一个更一般的解法。

MAP codeword decoding problem 可以通过「遍历所有码字、找最大化 $P(\mathbf{y} \mid \mathbf{t})P(\mathbf{t})$ 的那一个」在指数时间（量级 $2^{K}$）内求解。但我们感兴趣的是比这更高效的方法。在 §25.3 里我们将讨论一种称为 min–sum algorithm 的精确方法，它可能更高效地解决 codeword decoding problem；**高效到什么程度，取决于码的性质**。

值得强调：对一般线性码，MAP codeword decoding **已知是 NP-complete 的**（用外行话说：除非计算机科学发生一场革命，MAP codeword decoding 的复杂度会随 blocklength 指数增长）。所以把注意力限制到 MAP 解码问题上，并不一定使任务变得容易多少；它只是让答案报告起来更简短。



#### 解 bitwise decoding problem

形式上，bitwise decoding problem 的精确解可由 (25.1) 把其余比特 marginalize 掉得到：

```math
P(t_n \mid \mathbf{y}) = \sum_{\{t_{n'} : n' \ne n\}} P(\mathbf{t} \mid \mathbf{y}).
```

(25.7)

我们也可以借助 truth function $[S]$（当命题 $S$ 为真时取 1、否则取 0）来写这个 marginal：

```math
P(t_n = 1 \mid \mathbf{y}) = \sum_{\mathbf{t}} P(\mathbf{t} \mid \mathbf{y})\, [t_n = 1]
```

(25.8)

```math
P(t_n = 0 \mid \mathbf{y}) = \sum_{\mathbf{t}} P(\mathbf{t} \mid \mathbf{y})\, [t_n = 0].
```

(25.9)

用「对所有码字 $\mathbf{t}$ 显式求和」的办法来算这些 marginal probability，需要指数时间。但对某些码而言，bitwise decoding problem 可以用 forward–backward algorithm 高效得多地解决。我们马上会描述这个算法，它是 sum–product algorithm 的一个例子。min–sum algorithm 与 sum–product algorithm 两者都极为重要，而且在许多领域里被反复独立发明过。

### 25.2 码与格图 · Codes and trellises

在第 1 章与第 11 章，我们用 generator matrix（生成矩阵）与 parity-check matrix（校验矩阵）表示线性 $(N, K)$ 码。对系统分组码（systematic block code）而言，每个长为 $N$ 的块里前 $K$ 个发送比特是源比特，其余 $M = N - K$ 个是校验比特。这意味着该码的 generator matrix 可以写成

```math
\mathbf{G}^{\mathrm{T}} = \begin{pmatrix} \mathbf{I}_K \\ \mathbf{P} \end{pmatrix},
```

(25.10)

而 parity-check matrix 可以写成

```math
\mathbf{H} = \begin{pmatrix} \mathbf{P} & \mathbf{I}_M \end{pmatrix},
```

(25.11)

其中 $\mathbf{P}$ 是一个 $M \times K$ 矩阵。

这一节我们要研究线性码的另一种表示，称为 trellis（格图，又译网格图）。这些 trellis 所表示的码一般不是系统码，但如果愿意，只要把一个块内的比特重新排序，就可以把它们映射到系统码上。

[Figure 25.1：三个 trellis 的例子——(a) 重复码 R3，(b) 简单奇偶校验码 P3，(c) $(7,4)$ Hamming code。trellis 里每条边都用一个 0（画成方框）或一个 1（画成叉）标号。它演示的是「同一个码可以画成一条从左到右的路径集合」，这是本章全部算法的舞台。具体的节点连线与边标号序列无法从文字层复原，此处不编造。]

#### Trellis 的定义 · Definition of a trellis

我们的定义会相当窄。想获得关于 trellis 更全面的观点，读者应参阅 Kschischang and Sorokine (1995)。

<span style="color:#1f618d;">**定义（trellis）**：trellis 是一个由节点（nodes，也称 states 或 vertices）与边（edges）构成的图。节点按纵向的片分组，每一片称为一个 time（时），time 之间有序，使得每条边连接一个 time 里的节点到**相邻** time 里的节点。每条边都用一个符号标号（labelled）。最左与最右的 state 只含一个节点。除了这两个极端节点，trellis 里所有节点都至少有一条向左连接的边，且至少有一条向右连接的边。</span>



一个含 $N+1$ 个 time 的 trellis 按如下方式定义一个 blocklength 为 $N$ 的码：取一条从左到右穿过 trellis 的路径，读出所经过的边上的符号，就得到一个码字。**穿过 trellis 的每一条合法路径都定义一个码字。** 我们把最左边的 time 编号为「time 0」，最右边的为「time $N$」。我们把最左边的 state 编号为「state 0」，最右边的为「state $I$」，其中 $I$ 是 trellis 里 state（vertex）的总数。码字的第 $n$ 个比特是在我们从 time $n-1$ 走到 time $n$ 时发出的。

给定一个 time 处 trellis 的**宽度 width**，是该 time 里节点的个数。trellis 的 maximal width 就是字面意思。

如果一个 trellis 所定义的码是线性码，就称它为 linear trellis。从现在起我们只关心 linear trellis，因为非线性 trellis 要复杂得多。为简短起见，我们只讨论 binary trellis，即边用 0 与 1 标号的 trellis。把下面这些方法推广到 $q$ 元 trellis 并不困难。

图 25.1(a–c) 展示了分别对应这些码的 trellis：$(N, K) = (3, 1)$ 的重复码 R3；$(N, K) = (3, 2)$ 的奇偶校验码 P3；以及 $(7, 4)$ Hamming code。

[exercise] **Exercise 25.2.**[2] Confirm that the sixteen codewords listed in table 1.14 are generated by the trellis shown in figure 25.1c.

> **中文话题摘要**：核对表 1.14 里那 16 个码字，正好是图 25.1c 的 trellis 上全部合法路径读出的序列——即「码 = trellis 上路径标号的集合」这条定义的具体验证。

#### 关于 linear trellis 的观察

对任何线性码，minimal trellis（最小格图）是节点数最少的那个 trellis。在 minimal trellis 里，每个节点至多有两条边进入、至多有两条边离开。同一个 time 里的所有节点彼此有相同的左度（left degree），也彼此有相同的右度（right degree）。**宽度永远是 2 的幂。**

一个线性 $(N, K)$ 码的 minimal trellis，其宽度不可能大于 $2^{K}$，因为每个节点至少有一条合法码字经过，而码字总共只有 $2^{K}$ 个。进一步地，若定义 $M = N - K$，则 minimal trellis 的宽度在**每一处**都小于 $2^{M}$。这一点将在 §25.4 证明。

注意图 25.1 里那些 linear trellis（它们全都是 minimal trellis）：当我们从左到右或从右到左穿过 trellis 时，$K$ 就是遇到 binary branch point（二叉分叉点）的次数。

关于 trellis 的构造，我们会在 §25.4 里多谈一些。但现在我们已经知道得足够多，可以讨论解码问题了。

### 25.3 在 trellis 上解解码问题 · Solving the decoding problems on a trellis

我们可以把线性码的 trellis 看成对「产生一个码字的概率过程」给出的因果描述，时间从左流向右。每当遇到一个分叉，就有一个随机源（通信中的信息比特源）决定我们往哪边走。

在接收端，我们收到的是边标号序列的有噪版本，我们希望推断走的是哪条路径。准确地说：(a) 我们要找出最可能的路径，以解决 codeword decoding problem；(b) 我们要找出 time $n$ 处发送的符号是 0 还是 1 的概率，以解决 bitwise decoding problem。

<span style="color:#b9770e;">**例 25.3.** 考虑图 25.1c 所示 Hamming $(7, 4)$ trellis 上的一次传输。</span>



[Figure 25.2：当接收向量 $\mathbf{y}$ 的归一化 likelihood 为 $(0.1, 0.4, 0.9, 0.1, 0.1, 0.1, 0.3)$ 时，全部 16 个码字上的后验概率（表格形式给出，见下）。它演示的是「码字后验最多集中在 0.63，而阈值化给出的那个码字只有 0.25」。]

令归一化后的 likelihood 为 $(0.1, 0.4, 0.9, 0.1, 0.1, 0.1, 0.3)$。也就是说，likelihood 的比值为

```math
\frac{P(y_1 \mid x_1 = 1)}{P(y_1 \mid x_1 = 0)} = \frac{0.1}{0.9}, \qquad \frac{P(y_2 \mid x_2 = 1)}{P(y_2 \mid x_2 = 0)} = \frac{0.4}{0.6}, \qquad \text{等等}.
```

(25.12)

这个接收信号应当怎样解码？

**1.** 如果我们把 likelihood 按 $0.5$ 阈值化、把信号变成二进制接收向量，就得到 $\mathbf{r} = (0, 0, 1, 0, 0, 0, 0)$；用 binary symmetric channel 的解码器（第 1 章）解它，得到 $\hat{\mathbf{t}} = (0, 0, 0, 0, 0, 0, 0)$。**这不是最优的解码流程。最优推断永远由 Bayes 定理给出。**

**2.** 我们可以通过对全部 16 个码字显式枚举，求出码字上的后验概率。这个后验分布见图 25.2。当然，我们对这种蛮力解法本身并不真感兴趣；本章的目的就是理解那些能在少于 $2^{K}$ 计算机时间内把同样的信息取出来的算法。

考察这些后验概率，我们发现最可能的码字其实是串 $\mathbf{t} = 0110001$。它的概率是「阈值化解」0000000 那个答案的两倍多。

用图 25.2 给出的后验概率，我们还可以算出每个比特的 posterior marginal distribution。结果见图 25.3。可以看到比特 1、4、5、6 都相当有把握地被推断为 0。比特 2、3、7 的后验概率强度就没那么大。

<sup>2</sup> 在上面的例子里，MAP 码字与「逐比特选取各自最可能状态」得到的 bitwise 解码结果一致。但并不总是如此，下面的 exercise 会展示这一点。

#### 图 25.2 的表格（逐值保留）

| 码字 $\mathbf{t}$ | Likelihood | 后验概率 |
|---|---|---|
| 0000000 | 0.0275562 | 0.25 |
| 0001011 | 0.0001458 | 0.0013 |
| 0010111 | 0.0013122 | 0.012 |
| 0011100 | 0.0030618 | 0.027 |
| 0100110 | 0.0002268 | 0.0020 |
| 0101101 | 0.0000972 | 0.0009 |
| 0110001 | 0.0708588 | 0.63 |
| 0111010 | 0.0020412 | 0.018 |
| 1000101 | 0.0001458 | 0.0013 |
| 1001110 | 0.0000042 | 0.0000 |
| 1010010 | 0.0030618 | 0.027 |
| 1011001 | 0.0013122 | 0.012 |
| 1100011 | 0.0000972 | 0.0009 |
| 1101000 | 0.0002268 | 0.0020 |
| 1110100 | 0.0020412 | 0.018 |
| 1111111 | 0.0000108 | 0.0001 |

<span style="color:#1e8449;">**[译注]**
这张表是本章唯一一处可以用纯算术把「最优解码 ≠ 阈值化 + BSC 解码」钉死的地方，而且**归一化因子可以反推出来**，值得自己核一遍。

把 16 个 likelihood 相加：$0.0275562 + 0.0001458 + 0.0013122 + 0.0030618 + 0.0002268 + 0.0000972 + 0.0708588 + 0.0020412 + 0.0001458 + 0.0000042 + 0.0030618 + 0.0013122 + 0.0000972 + 0.0002268 + 0.0020412 + 0.0000108 = 0.1122000$。所以后验 = likelihood $/\,0.1122$。检验两处：$0.0275562/0.1122 = 0.2456 \approx 0.25$（表里给 0.25），$0.0708588/0.1122 = 0.6316 \approx 0.63$（表里给 0.63）。**两个都对上，说明这张表内部一致、且归一化因子确为 $0.1122$。**

**决定性数字**：$0.6316 / 0.2456 = 2.57$。阈值化那一步（$0.5$ 判决）丢掉的正是这个 2.57 倍——它把「比特 3 的 likelihood 是 $0.9$」当成了「比特 3 铁定是 1」，而实际上 bit 3 在最优码字 $0110001$ 里确实是 1，于是阈值化解与 MAP 解在 bit 3 上一致、却在 bit 1 与 bit 2 上分歧。**同一条数据上，两种解法的 Hamming 距离是 3 比特，而 $N = 7$——差了一半以上的比特。**

**消失测试**：抽掉「后验而不是硬判决」这个立场，你必须先做 $N$ 次独立判决再做 BSC 解码，等价于把 soft information 全部扔掉。可观测后果：在 Gaussian channel 上，这样做的误码率与最优解码相比有约 $2$ dB 的损失（这正是 BSC 与软判决解码之间的经典差距，可以用 (25.5) 的 LLR 保留与否来量化）；以 (25.12) 的数据为例，硬判据直接给出 $\hat{\mathbf{t}} = 0000000$，概率只有 $0.2456$，而真答案是 $0.6316$。

**落点**：(25.1) 与 (25.6)；图 25.3 的比特后验（原书为图形，文字层不可复原，此处不编造数值）；§25.3 之后 min–sum 与 sum–product 两种算法分别在 max-product 与 sum-product 半环上做同一件事。
</span>

<span style="color:#1e8449;">**[译注]**
本章标题里「Exact Marginalization in Trellises」的两个关键词必须一起读，否则会误以为 trellis 只是个画图技巧。

**trellis 的代价必须与 $2^{K}$ 枚举对照才有意义**。设一个 $(N, K)$ 码的 minimal trellis 最大宽度为 $W$。每条边的处理代价是 $O(1)$，边数最多 $W \cdot 2 \cdot (N+1)$（每节点至多两条出入边），于是 sum–product 的总代价是 $O(N W)$。书上 p.327 给了两条硬边界：$W \le 2^{K}$ 且 $W \lt 2^{M} = 2^{N-K}$，合起来
$W \le 2^{\min(K,\,N-K)}$。所以最小 trellis 上的解码代价是 $O\!\left(N \cdot 2^{\min(K,\,N-K)}\right)$，而不是暴力枚举的 $O(2^{K})$。

**用 (7,4) Hamming 数一遍**：$K = 4$、$M = 3$，故 $W \le 2^{3} = 8$；暴力枚举要 $2^{4} = 16$ 个码字、每个 7 位校验，代价 112 次比特操作；trellis 上是 $7 \cdot 8 \cdot 2 \approx 112$ 次——**这个规模看不出优势**。把码放大到 $(1000, 500)$：暴力是 $2^{500}$，而 $\min(K, N-K) = 500$，trellis 上界 $2^{500}$，同样没有优势。**这就是关键：只有「$K$ 或 $N-K$ 中有一个很小」的码（如卷积码、LDPC 的局部 trellis）才真正受益。**

**消失测试**：抽掉 trellis 结构，剩下的唯一选择是枚举码字（$2^{K}$）或做一般图上的 marginalization（树宽 $\ge W$ 时指数爆炸）；而 $\min(K, N-K)$ 这个指数**只对分组码的最小 trellis** 成立，一旦换成 LDPC 那种长码，单块 trellis 宽度会退化，必须改用 factor graph + 迭代 sum–product（第 26、47 章），代价从精确的 $O(NW)$ 变成近似的 $O(N \cdot d)$（$d$ 为最大度），不再保证精确。

**落点**：$W \le 2^{\min(K, N-K)}$ 的证明在 §25.4（p.327 预告）；Exercise 25.2 用 $(7,4)$ 验证；工程侧看卷积码的 Viterbi（min–sum）与 BCJR（sum–product），两者就是本节的 max-product 与 sum-product 在同一 trellis 上的两个半环。
</span>

---

## 附：可复算验证与原文问题清单

### A. 上标恢复的核对（文字层把 $10^{217}$ 抽成「10217」等）

| 位置 | 原文文字层 | 恢复为 | 复算 |
|---|---|---|---|
| p309 Ex 22.14 | `ek/2 ≃10217` | $e^{k/2} \simeq 10^{217}$ | $k = 1000 \Rightarrow e^{500} = 10^{500/\ln 10} = 10^{217.15}$ |
| p309 Ex 22.14 | `exp(0.01k) ≃20 000` | $\exp(0.01k) \simeq 20\,000$ | $k = 1000 \Rightarrow e^{10} = 22\,026$ |
| p309 Ex 22.14 | `6 × 10−5`、`6 × 10−7` | $6\times 10^{-5}$、$6\times 10^{-7}$ | $2\Phi(-4) = 6.33\times10^{-5}$，$2\Phi(-5) = 5.73\times10^{-7}$ |
| p313 (23.12) | `[cosh(βx)]1/β` | $[\cosh(\beta x)]^{1/\beta}$ | 分母上的幂，见 p313 译注 |
| p318 (23.35) | `DKL(p||m)` | $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{m})$ | — |

### B. 图 25.2 表格的归一化核对

$\sum_{\mathbf{t}} \text{Likelihood} = 0.1122000$；$0.0275562/0.1122 = 0.2456$；$0.0708588/0.1122 = 0.6316$。表内 `0.25` 与 `0.63` 均为四舍五入值，一致。后验列逐项相加得 $1.0025$（16 项各保留 1–2 位有效数字带来的舍入残差），可接受。

### C. p314 的 Jacobian 核对

$P(l) = P(x)\left|\partial x/\partial l\right|$，$x = e^{l}$，$\partial x/\partial l = e^{l} = x$，故指数由 $c-1$ 变 $c$，与 (23.18) 一致。

### D. p320 的 $1/\sigma$ prior 核对

(24.2) 取 $b_\beta c_\beta = 1$、$c_\beta \to 0$：$b_\beta = 1/c_\beta \to \infty$，密度 $\propto \beta^{c_\beta - 1} b_\beta^{-c_\beta} e^{-\beta/b_\beta} \to \beta^{-1}$。再由 $\beta = \sigma^{-2}$、$d\beta = -2\sigma^{-3}d\sigma$，得 $P(\sigma) \propto \sigma^{2}\cdot\sigma^{-3} = \sigma^{-1}$，即 $1/\sigma$ prior，与原文一致。

### E. 原文自身问题（† 标记处）

1. **† p310 (22.38)、(22.41)**：右端写作 $f_k(x)$，缺上标 $(n)$，应为 $f_k(x^{(n)})$。由 (22.37) 逐项求导即知。
2. **† p311 第 5 行**：`The exponential distribution on integers,,` 多出一个逗号，属排版噪声，已按语义译为正常句。
3. **† p312 图 23.3 caption**：`parameters (m, s) = (1, 1)` 用的是 $m$ 而正文 (23.8) 用 $\mu$，同一符号两种写法；译文统一按 $\mu$。
4. **† p315 (23.22)**：文中称其为「第 $m$ 个事件的到达时间」的密度，但该式的形状（$(\lambda x)^{m-1}/(m-1)!$ 乘 $e^{-\lambda x}$ 再乘 $\lambda$）是 Erlang / gamma 分布，与 §23.3 开头把 exponential 称为等待分布的语境需分清：$m = 1$ 时退化为 (23.13) 的 exponential（$s = 1/\lambda$）。

**补充说明（非原文错误，但易误读）**：p316–317 的 $\alpha$ 在 Dirichlet 里是「浓度参数」，与 p309 Ex 22.16 里的 $\alpha = 1/\sigma_W^2$ 完全无关，只是同一字母被用在两个不同章节的不同含义上。

---

## 术语表（15 条，按首现顺序）

| # | English | 中文（首现处给括号注） | 首现页 |
|---|---|---|---|
| 1 | maximum likelihood | 最大似然 | p309 |
| 2 | marginalization / marginalize | 边缘化（把参数积分或求和消掉） | p309 |
| 3 | MAP (maximum a posteriori) | 最大后验 | p309 |
| 4 | conjugate prior | 共轭先验（与 likelihood 相乘后同族） | p319 |
| 5 | improper prior | 非正常先验（不可归一化） | p319 |
| 6 | noninformative prior | 无信息先验 | p313 |
| 7 | evidence / marginal likelihood | 证据 / 边缘似然 | p322 |
| 8 | Occam factor | 奥卡姆因子（参数体积收缩带来的罚分） | p322 |
| 9 | sufficient statistics | 充分统计量 | p321 |
| 10 | precision parameter | 精度参数 $\tau = 1/\sigma^2$ | p312 |
| 11 | logit / softmax basis | logit / softmax 基 | p316 |
| 12 | Dirichlet distribution | 狄利克雷分布 | p316 |
| 13 | beta / gamma / Student-t distribution | beta / gamma / Student-t 分布（后两个不译） | p311–314 |
| 14 | trellis / minimal trellis | 格图 / 最小格图 | p326 |
| 15 | codeword decoding / bitwise decoding | 码字解码 / 逐比特解码 | p324 |

**本块按约定一律不译的词**（原文照留）：Gaussian、Poisson、binomial、Dirichlet、beta、gamma、Student-t、Cauchy、Von Mises、log-normal、trellis、codeword、likelihood、prior、evidence、Occam factor、K-means / soft K-means / mixture model / EM / responsibilities / distortion / vector quantization（后六者在本块 p309–328 区间**未出现**，属第 20–22 章前段的内容，此处仅作说明）。



## 25.3 在 trellis 上解解码问题 · Solving the decoding problems on a trellis

本页接上一块 p328 的中途。p328 已经把「信道模型 + 码的 trellis」摆好，本页开始用数字演示：同一份 likelihood，两种解码问题给出两个不同答案，而且**逐比特解码的答案常常不是码字**。这不是 bug，是两种问题的定义不同——这条区分支撑整个第 25 章到第 26 章的全部技术内容。

先看图 25.3 的数值。它是「7 比特码字在给定信道输出后的逐比特后验边缘概率」，对应图 25.2 的后验分布。

[Figure 25.3：7 个比特的 marginal posterior probabilities，取自图 25.2 的后验分布。原书此处以**表格形式**排印，故下表逐值保留、可完整复原；这不是曲线图，无需猜测坐标。]

| $n$ | Likelihood $P(y_n \mid t_n = 1)$ | Likelihood $P(y_n \mid t_n = 0)$ | Posterior marginal $P(t_n = 1 \mid \mathbf{y})$ | Posterior marginal $P(t_n = 0 \mid \mathbf{y})$ |
|---|---|---|---|---|
| 1 | 0.1 | 0.9 | 0.061 | 0.939 |
| 2 | 0.4 | 0.6 | 0.674 | 0.326 |
| 3 | 0.9 | 0.1 | 0.746 | 0.254 |
| 4 | 0.1 | 0.9 | 0.061 | 0.939 |
| 5 | 0.1 | 0.9 | 0.061 | 0.939 |
| 6 | 0.1 | 0.9 | 0.061 | 0.939 |
| 7 | 0.3 | 0.7 | 0.659 | 0.341 |

读这张表要抓住一处反直觉的地方：第 2 位的 likelihood 明明偏向 $t_2 = 0$（$0.6$ 对 $0.4$），可后验却偏向 $t_2 = 1$（$0.674$ 对 $0.326$）。原因是第 2 位的**边缘**后验要把码的约束积掉——凡是把 $t_2$ 钉成 0 的码字，其余比特的 likelihood 乘积都偏低。这一格就是「likelihood 不是 posterior」的最小可见反例。

<span style="color:#b9770e;">**[exercise] Exercise 25.4.**[2, p.333] Find the most probable codeword in the case where the normalized likelihood is $(0.2, 0.2, 0.9, 0.2, 0.2, 0.2, 0.2)$. Also find or estimate the marginal posterior probability for each of the seven bits, and give the bit-by-bit decoding. [Hint: concentrate on the few codewords that have the largest probability.]</span>

> **中文话题摘要**：likelihood 只在第 3 位偏 1（$0.9$）、其余六位全偏 0（$0.2$），问 MAP 码字是谁、七个比特的边缘后验多大、逐比特解码给出哪个比特串。提示是「只算概率最大的那几个码字就够」——这条提示等价于说：后验集中在少数几个码字上时，枚举比消息传递还快。

下面转入本节的正面任务：**怎么用 trellis 上的 message passing 解这两个解码问题**。

### min–sum 算法 · The min–sum algorithm

MAP codeword decoding（最大后验码字解码）可以用 §16.3 引入的 min–sum algorithm（最小-和算法）求解。

码的每个 codeword（码字）对应 trellis 上的一条 path（路径）。正像一段旅程的 cost 是各段 cost 之和，一个 codeword 的 log likelihood 是各比特 log likelihood 之和。按惯例，我们把想最大化的 log likelihood 取负，改口谈 cost（代价），而 cost 是要最小化的量。

我们给每条 edge（边）配一个 cost $-\ln P(y_n \mid t_n)$，其中 $t_n$ 是这条边对应的发送比特，$y_n$ 是接收符号。于是 §16.3 给出的 min–sum algorithm 能在「与 trellis 的 edge 数相等的计算机运算次数」内找出最可能的 codeword。这个算法也叫 Viterbi algorithm（Viterbi，1967）。

这里的技术要点是**「乘积变求和」这一步在 log 域里免费**：likelihood 的连乘在 log 域变成连加，而链路 cost 可加正是最短路径算法成立的前提。抽掉 log，Viterbi 就必须在实数乘法上做动态规划，指数下溢会先于算法出错。

### sum–product 算法 · The sum–product algorithm

要解 bitwise decoding problem（逐比特解码问题），我们对 min–sum algorithm 做一点小改动，让穿过 trellis 的 message 表达「到当前点为止的数据概率」，而不是「到当前点的最优路径 cost」。具体做法：把边上的 cost $-\ln P(y_n \mid t_n)$ 换回 likelihood 本身 $P(y_n \mid t_n)$，并把 min–sum 里的 min 与 sum 两个运算分别换成 sum 与 product。

令 $i$ 跑遍 node / state，$i = 0$ 标记 start state，$P(i)$ 表「$i$ 的父状态」集合，$w_{ij}$ 表从 node $j$ 到 node $i$ 的 edge 上的 likelihood。我们定义前向（forward-pass）message $\alpha_i$ 为

```math
\alpha_0 = 1
```

（接 p330。）



```math
\alpha_i = \sum_{j \in P(i)} w_{ij}\,\alpha_j .
```

（(25.13)）

这些 message 可以从左到右依次算出。

<span style="color:#b9770e;">**[exercise] Exercise 25.5.**[2] Show that for a node $i$ whose time-coordinate is $n$, $\alpha_i$ is proportional to the joint probability that the codeword's path passed through node $i$ and that the first $n$ received symbols were $y_1, \ldots, y_n$.</span>

> **中文话题摘要**：要证 $\alpha_i$ 正比于「路径经过 node $i$ 且前 $n$ 个接收符号恰是 $y_1,\dots,y_n$」的联合概率。证明用归纳法：对 $n$ 归纳，递推就是 (25.13) 本身。

在 trellis 的 end node 处算出的 message $\alpha_I$ 正比于数据的 marginal probability（边缘概率）。

<span style="color:#b9770e;">**[exercise] Exercise 25.6.**[2] What is the constant of proportionality? [Answer: $2^{K}$　†]</span>

> **中文话题摘要**：问 (25.13) 那个「正比」缺的常数因子是多少。答案 $2^{K}$——每个码字在 trellis 里对应一条 path，而 $K$ 维码有 $2^{K}$ 个码字，求和时每个码字被累计一次，故 $\alpha_I$ 是「数据概率 × 码字数」。† 原书排印为 `2K`，是 CUP 文字层丢上标所致（$K$ 在本书 §25 一律表码字维数，(7,4) Hamming 码的 $K = 4$，若按 $2K = 8$ 读会与事实差 16 倍）。

我们以类似方式定义第二组后向（backward-pass）message $\beta_i$。设 node $I$ 为 end node。

```math
\begin{aligned}
\beta_I &= 1 \\
\beta_j &= \sum_{i:\, j \in P(i)} w_{ij}\,\beta_i .
\end{aligned}
```

（(25.14)）

这些 message 可以从右到左、反向依次算出。

<span style="color:#b9770e;">**[exercise] Exercise 25.7.**[2] Show that for a node $i$ whose time-coordinate is $n$, $\beta_i$ is proportional to the conditional probability, given that the codeword's path passed through node $i$, that the subsequent received symbols were $y_{n+1} \ldots y_N$.</span>

> **中文话题摘要**：$\alpha$ 管「来路」，$\beta$ 管「去路」。要证 $\beta_i$ 正比于「给定路径经过 node $i$ 之后，后续接收符号是 $y_{n+1},\dots,y_N$」的条件概率。$\alpha$ 与 $\beta$ 的乘积才是整条路径的全概率——这正是 (25.15) 的由来。

最后，要求第 $n$ 个比特是 1 还是 0 的概率，我们对前向与后向 message 的乘积做两次求和。令 $i$ 跑遍 time $n$ 上的 node，$j$ 跑遍 time $n-1$ 上的 node，$t_{ij}$ 表「从 node $j$ 到 node $i$ 这条 trellis edge 所对应的 $t_n$ 取值」。对 $t = 0/1$ 的两个取值，我们计算

```math
r^{(t)}_{n} = \sum_{i,\,j:\; j \in P(i),\; t_{ij} = t} \alpha_j \, w_{ij} \, \beta_i .
```

（(25.15)）

于是 $t_n$ 取 $t = 0/1$ 的后验概率是

```math
P(t_n = t \mid \mathbf{y}) = \frac{1}{Z}\, r^{(t)}_{n},
```

（(25.16)）

其中归一化常数 $Z = r^{(0)}_{n} + r^{(1)}_{n}$ 应当与先前算出的最终前向 message $\alpha_I$ 完全相等。

这个「应当完全相等」是本节唯一一条**免费的自我校验**：$Z$ 有两条独立算法（前向跑到终点 vs 在每个 time 上逐位求和），两者数值若不等，说明 message 更新顺序或 $w_{ij}$ 的下标写错了。工程上这条校验在定点实现里被当作断言用。

<span style="color:#b9770e;">**[exercise] Exercise 25.8.**[2] Confirm that the above sum–product algorithm does compute $P(t_n = t \mid \mathbf{y})$.</span>

> **中文话题摘要**：验证 (25.15)(25.16) 给出的确实是后验边缘概率。关键是展开 $\alpha_j w_{ij}\beta_i$ 得到「整条路径概率之和」，再对固定 $t_n = t$ 的路径集求和。

这里给出的 sum–product algorithm 还有别的名字：「forward–backward algorithm（前向-后向算法）」、「BCJR algorithm」、「belief propagation（信念传播）」。

<span style="color:#b9770e;">**[exercise] Exercise 25.9.**[2, p.333] A codeword of the simple parity code $P_3$ is transmitted, and the received signal $\mathbf{y}$ has associated likelihoods shown in table 25.4. Use the min–sum algorithm and the sum–product algorithm in the trellis (figure 25.1) to solve the MAP codeword decoding problem and the bitwise decoding problem. Confirm your answers by enumeration of all codewords $(000, 011, 110, 101)$. [Hint: use logs to base 2 and do the min–sum computations by hand. When working the sum–product algorithm by hand, you may find it helpful to use three colours of pen, one for the $\alpha$s, one for the $w$s, and one for the $\beta$s.]</span>

> **中文话题摘要**：simple parity code $P_3$（码字为 000、011、110、101，即偶数个 1）发一个码字，接收端给出表 25.4 的三组比特似然；要求分别用 min–sum 与 sum–product 解 MAP 码字解码与逐比特解码，再用四个码字全枚举验算。提示里那句「三色笔」是实操建议：$\alpha$、$w$、$\beta$ 三类量在同一张 trellis 上会写重叠。

[Table 25.4：$P_3$ 一个码字的逐比特 likelihood。原表 3 行 2 列，逐值保留。]

| $n$ | $P(y_n \mid t_n)$，$t_n = 0$ | $P(y_n \mid t_n)$，$t_n = 1$ |
|---|---|---|
| 1 | $1/4$ | $1/2$ |
| 2 | $1/2$ | $1/4$ |
| 3 | $1/8$ | $1/2$ |

<span style="color:#1e8449;">**[译注]**
这一页是全章的技术分水岭，值得把「为什么要两组 message」这件事说到不能反驳。

**单组 message 只能答一个问题。** 前向 $\alpha$ 从 (25.13) 递推下来，握着的是「走这条 path 至今的累计 likelihood」；一旦到了 end node，你得到的是**整条码字**的后验（除以 $Z$ 之后），这就是 MAP codeword decoding 的答案——按 (25.15)(25.16) 走一遍就能看出，$r^{(t)}_n$ 需要 $\alpha_j$ 与 $\beta_i$ **相乘**，缺任一组都无法把「经过 node $i$ 的路径」拆成「前半段 × 后半段」。

**消失测试**：抽掉 $\beta$，只剩 Viterbi 能算的那一件事——最可能码字。做不了逐比特后验，于是软输出（soft output）不存在；turbo code（Berrou 1993）、LDPC 的迭代解码需要的正是每比特的 extrinsic LLR，它们的输入就是 $\alpha_j w_{ij}\beta_i$ 这个乘积。没有 $\beta$，误码率曲线会退回到 hard-decision Viterbi 的 3 dB 损失那一档——每比特约 2 dB 到 3 dB 的编码增益直接消失。

**量的方向感**：代价只是**再存一遍与 edge 数同阶的数组**，运算次数仍是 $O(|\text{edges}|)$，比 (25.13) 单跑一遍多一个常数因子 2；而它买到的是全部 $N$ 个比特的完整后验，$N = 1000$ 时就是从「1 个答案」到「1000 个带置信度的答案」。

**可复算验证**：用表 25.4 手算，$Z = (2+8+1+1)/64 = 12/64 = 3/16$，与 p333 给出的 $\alpha_I = 3/16$ 一致——这条等式就是 (25.16) 那句「$Z$ 应当与 $\alpha_I$ 相等」的实例。

**落点**：§25.3 本页 (25.15)(25.16)、p333 的 Exercise 25.9 解答、§26.2 的 (26.15)（$Z_n(x_n) = \prod_m r_{m\to n}$ 是同一个想法的图形版）、§33.8 的 loopy belief propagation。算法侧可对齐 6.006 的 DAG 最短路径与 6.046 的 dynamic programming；概率侧只用到条件概率定义，无越级。
</span>



## 25.4 更多关于 trellis 的讨论 · More on trellises

现在讨论构造码的 trellis 的几种不同方式。本节可以安全跳过。

一个 codeword 的 span（跨度）指「从该码字第一个非零比特，到最后一个非零比特（含两端）之间所包含的比特集合」。我们可以用二进制向量把 codeword 的 span 标出来，如表 25.5 所示。

[Table 25.5：若干 codeword 及其 span。原表 5 行 2 列，逐值保留、可完整复原。]

| Codeword | Span |
|---|---|
| 0000000 | 0000000 |
| 0001011 | 0001111 |
| 0100110 | 0111110 |
| 1100011 | 1111111 |
| 0101101 | 0111111 |

读表方法：$0001011$ 的第一个非零位在第 4 列、最后一个在第 7 列，所以 span 是 $0001111$（第 4–7 列为 1）。$0101101$ 首非零在第 2 列、末非零在第 7 列，span 为 $0111111$。$1100011$ 首非零在第 1 列、末非零在第 7 列，span 全 1。

一个 generator matrix（生成矩阵）处于 trellis-oriented form（trellis 自适应形式）是指：矩阵各行的 span **起点落在互不相同的列**，且各行的 span **终点也落在互不相同的列**。

### 怎样从 generator matrix 造 trellis

首先用类似 Gaussian elimination（高斯消元）的行变换把 generator matrix 化成 trellis-oriented form。例如我们的 $(7, 4)$ Hamming code 可以由下式生成：

```math
G = \begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 & 0 & 1 & 1
\end{bmatrix}
```

（(25.17)）

但这个矩阵不在 trellis-oriented form——比如第 1、3、4 行的 span 都结束在同一列。把下面的行减到上面的行上去，可以得到一个等价的 generator matrix（即生成同一个 codeword 集合的矩阵）如下：

```math
G = \begin{bmatrix}
1 & 1 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 & 1
\end{bmatrix}
```

（(25.18)）

现在，generator matrix 的每一行都可以看成在定义一个 $(N, 1)$ subcode（子码）——也就是 $(N, K)$ 码的一个只含 2 个 codeword 的子码，本情形里即长度为 $N = 7$、含 2 个 codeword 的码。就第一行而言，这个子码由 $1101000$ 与 $0000000$ 两个 codeword 组成。第二行定义的子码由 $0100110$ 与 $0000000$ 组成。这些子码的 minimal trellis（最小 trellis）很容易构造，它们画在图 25.6 的左列。

我们按图 25.6 的方式逐步（incrementally）搭建 trellis。先从 generator matrix 第一行给出的子码所对应的 trellis 开始，然后一次加入一个 subcode。新子码 span 之内的所有 vertex（顶点）全部复制一份；原 trellis 里的 edge symbol 保持不变，而 trellis 的第二部分（复制出来的那一支）里的 edge symbol，在新子码取值为 1 的位置上翻转，取值为 0 的位置上不动。

另一个 $(7, 4)$ Hamming code 可以由下式生成：

```math
G = \begin{bmatrix}
1 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}
```

（(25.19)）

<span style="color:#1e8449;">**[译注]**
(25.17)→(25.18) 这两步不是纯代数练习，它决定了 trellis 的状态数，从而决定解码的全部运算量。

**判据只有两条**：$\{1,2,3,4\}$ 是各行的首非零列（互不相同），$\{4,6,5,7\}$ 是各行的末非零列（互不相同）。(25.17) 的末非零列是 $\{7,6,7,7\}$——三个 7 撞在一起，所以它不合格；(25.18) 换完行之后变成 $4,6,5,7$，合格。

**为什么这件事值钱**：trellis 在 time $n$ 的 state 数等于「此刻还没结束的 span 数」的 $2^{\text{活跃行数}}$，而活跃行数就是「首列 $\le n$ 且末列 $\ge n$」的行数。(25.18) 在 $n = 4$ 处活跃的是第 1、2、3、4 行（$4$ 行全活跃，因为行 1 到第 4 列结束、行 4 从第 4 列开始），给出 $2^{4} = 16$ 个 state；而 (25.17) 在 $n = 4$ 处活跃行数同样最多 4，但**跨越长度**分布不同，整条 trellis 的总 edge 数更多。用 (25.18) 与 (25.19) 的整体比较更清楚：书上明说 (25.19) 造出的 trellis 节点数**少于**图 25.1c 那个 $(7,4)$ Hamming 码的 trellis——同一码、不同比特序，节点数就不同。

**消失测试**：不做 trellis-oriented 化，你就得用「按列扫全部 $2^{K}$ 个码字」或「state = 全部 $K$ 比特历史」的笨 trellis，状态数是 $2^{K} = 16$ 而非按活跃行数给的更小值；对 $(7,4)$ 只是常数差，对 $n = 10^{4}$ 个比特、$K = 5000$ 的码就是 2 的 5000 次方与 2 的十来次方之差——Viterbi 从「跑不动」变成「每秒能跑几个码字」。

**落点**：本书 §25.4 本页、图 25.1c、图 25.6；$K = 4$、$N = 7$、$M = 3$ 的具体数字见 §B3 的行正交核对。挂 Strang 的列空间/行变换一节（行变换不改变行空间，这一条是 (25.17)→(25.18) 的合法性全部依据），无越级。
</span>



[Figure 25.6：$(7, 4)$ Hamming code 的四个 subcode 各自的 trellis（左列），以及构造 $(7, 4)$ Hamming code 的 trellis 过程中依次得到的一串 trellis（右列）。trellis 里每条 edge 用一个 0（画成方块）或一个 1（画成叉）标号。**几何布局不可复原**：本图是六格拼图式的树状展开，节点与边的具体坐标无法从文字层恢复，故此处只保留 caption 与「每一步复制 span 内节点、翻转第二段 edge symbol」这一构造规则；规则本身在正文已完整给出，可据规则重画。]

由这个矩阵生成的 $(7, 4)$ Hamming code，与第 1 章及前文所用 systematic matrix（系统型矩阵）生成的码，相差一个比特的 permutation（置换）。与这个置换对应的 parity-check matrix（校验矩阵）是：

```math
H = \begin{bmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}
```

（(25.20)）

由等式 (25.19) 中经过 permutation 的矩阵 $G$ 得到的 trellis 画在图 25.7a 里。注意这个 trellis 的节点数比图 25.1c 里先前那个 Hamming $(7, 4)$ 码的 trellis 更少。由此可见：重排 codeword 比特的顺序，有时能得到更小、更简单的 trellis。

[Figure 25.7：经过 permutation 的 $(7, 4)$ Hamming code 的 trellis，(a) 用图 25.6 的方法从 generator matrix 造出；(b) 用 p.332 的方法从 parity-check matrix 造出。trellis 里每条 edge 用一个 0（方块）或一个 1（叉）标号。**几何布局不可复原**，理由同图 25.6；(b) 的构造判据是「纵向坐标 = partial syndrome，横边 = 0、斜边 = 1」，按此判据可重画。]

### 从 parity-check matrix 造 trellis

看 trellis 的另一种方式是用 syndrome（校验子）。向量 $\mathbf{r}$ 的 syndrome 定义为 $H\mathbf{r}$，其中 $H$ 是 parity-check matrix。一个向量是 codeword，当且仅当其 syndrome 为零。当我们逐位生成一个 codeword 时，可以用 partial syndrome（部分校验子）来描述「当前状态」，即 $H$ 与「迄今已生成的 codeword 比特」之积。trellis 里的每个 state 就是某个 time-coordinate 上的 partial syndrome。起始与结束的 state 都被约束为零 syndrome。一个 state 里的每个 node 代表 partial syndrome 的一个不同取值。由于 $H$ 是 $M \times N$ 矩阵，其中 $M = N - K$，syndrome 至多是一个 $M$ 比特向量。于是每一片最多需要 $2^{M}$ 个 node　†。

（† 原书此处排印为 `2M`，是文字层丢上标。判据不是看图，而是这句自己的推导链：state = partial syndrome，syndrome 是 $M$ 比特向量，故每个 state 的取值个数上界是 $2^{M}$。$M = N - K = 7 - 4 = 3$ 时 $2^{M} = 8$；若按 $2M$ 读成 6，则与「$M$ 比特向量的全部取值」直接矛盾，故只能取 $2^{M}$。）

我们可以由 parity-check matrix 构造码的 trellis：从两端各自走一遍，生成两棵可能的 syndrome 序列树；这两棵树的交集（intersection）就定义了该码的 trellis。

在这样构造得到的图案里，我们可以让纵向坐标表示 syndrome。于是任何水平 edge 必然对应一个 0 比特（因为只有非零比特才会改变 syndrome），而任何非水平 edge 必然对应一个 1 比特。因此在这种表示下，我们不再需要给 trellis 的 edge 加标号。图 25.7b 展示的就是与 (25.20) 的 parity-check matrix 对应的 trellis。

<span style="color:#1e8449;">**[译注]**
这一页的「横边必是 0、斜边必是 1」是全节最省事的工程化简，值得单独钉住：它把「edge 标号」这个额外数据结构彻底删掉。

**机制**：state 取 partial syndrome $\mathbf{s}_n = H_{1..n}\,\mathbf{c}_{1..n}$。走一步时若 $c_{n+1} = 0$，$\mathbf{s}$ 不变（水平边）；若 $c_{n+1} = 1$，$\mathbf{s}$ 加上 $H$ 的第 $n+1$ 列（竖直位移）。所以**边的方向就是比特值本身**。这让 trellis 的内存占用从「节点 + 边 + 边标号」降成「节点 + 边」，而解码器最内层循环里省掉的是一次查表。

**量的方向感**：state 数上界 $2^{M} = 2^{N-K}$。$(7,4)$ 码是 $2^{3} = 8$；$(255, 223)$ Reed–Solomon 的符号级 $M = 32$，$2^{32}$ 直接不可行——这正是 RS 要用 $GF(2^{8})$ 子域分解、以及为什么长码必须走 LDPC/turbo 而不是格图解码的量化理由。

**消失测试**：把「state = partial syndrome」这个构造换成「state = 全部历史比特」，状态数从 $2^{M}$ 变成 $2^{n}$（$n$ 是已生成比特数），Viterbi 在 $n = 100$、$M = 10$ 时从 $2^{10} = 1024$ 个 state 涨到 $2^{100}$，任何硬件都存不下这张表。另一方面，抽掉这条构造你就无法解释为什么「重排比特序能减小 trellis」——(25.19) 的重排改变了 $H$ 的列序，从而改变了每个 $n$ 处活跃 syndrome 集合的**大小**，节点数才跟着变。

**可复算验证**：用 (25.19) 的 $G$ 与 (25.20) 的 $H$ 逐行做内积，四行 $G$ 对三行 $H$ 全为偶数（$2,2,2,4$ 等，见 §B3），故 $GH^{\mathsf{T}} = 0$，$H$ 确实是该码的 parity-check matrix；再取 $M = N - K = 7 - 4 = 3$，$2^{3} = 8$，与图 25.7b 的每片节点数一致。

**落点**：§25.4 本页、图 25.7b、(25.20)；线性代数侧挂 Strang 的四个基本子空间（$H$ 的零空间就是码），信息论侧挂本书 §1.2 的 parity-check 定义。无越级。
</span>



## 25.5 解答 · Solutions

[Table 25.8：Exercise 25.4 的 codeword 后验概率。原表 16 行 3 列，逐值保留、可完整复原。]

| $\mathbf{t}$ | Likelihood | Posterior probability |
|---|---|---|
| 0000000 | 0.026 | 0.3006 |
| 0001011 | 0.00041 | 0.0047 |
| 0010111 | 0.0037 | 0.0423 |
| 0011100 | 0.015 | 0.1691 |
| 0100110 | 0.00041 | 0.0047 |
| 0101101 | 0.00010 | 0.0012 |
| 0110001 | 0.015 | 0.1691 |
| 0111010 | 0.0037 | 0.0423 |
| 1000101 | 0.00041 | 0.0047 |
| 1001110 | 0.00010 | 0.0012 |
| 1010010 | 0.015 | 0.1691 |
| 1011001 | 0.0037 | 0.0423 |
| 1100011 | 0.00010 | 0.0012 |
| 1101000 | 0.00041 | 0.0047 |
| 1110100 | 0.0037 | 0.0423 |
| 1111111 | 0.000058 | 0.0007 |

### Exercise 25.4 的解答（p.329）· Solution to exercise 25.4 (p.329)

codeword 上的后验概率如表 25.8 所示。最可能的 codeword 是 $0000000$。七个比特的 marginal posterior probabilities 如下：

[本表为 p333 内嵌表，原表 7 行 5 列，逐值保留。]

| $n$ | Likelihood $P(y_n \mid t_n = 1)$ | Likelihood $P(y_n \mid t_n = 0)$ | Posterior $P(t_n = 1 \mid \mathbf{y})$ | Posterior $P(t_n = 0 \mid \mathbf{y})$ |
|---|---|---|---|---|
| 1 | 0.2 | 0.8 | 0.266 | 0.734 |
| 2 | 0.2 | 0.8 | 0.266 | 0.734 |
| 3 | 0.9 | 0.1 | 0.677 | 0.323 |
| 4 | 0.2 | 0.8 | 0.266 | 0.734 |
| 5 | 0.2 | 0.8 | 0.266 | 0.734 |
| 6 | 0.2 | 0.8 | 0.266 | 0.734 |
| 7 | 0.2 | 0.8 | 0.266 | 0.734 |

所以逐比特解码（bitwise decoding）给出 $0010000$——它其实并不是一个 codeword。

### Exercise 25.9 的解答（p.330）· Solution to exercise 25.9 (p.330)

MAP codeword 是 $101$，其 likelihood 为 $1/8$。sum–product algorithm 的归一化常数是 $Z = \alpha_I = 3/16$。中间的 $\alpha_i$（从左到右）是 $1/2,\; 1/4,\; 5/16,\; 4/16$；中间的 $\beta_i$（从右到左）是 $1/2,\; 1/8,\; 9/32,\; 3/16$。逐比特解码为：$P(t_1 = 1 \mid \mathbf{y}) = 3/4$；$P(t_2 = 1 \mid \mathbf{y}) = 1/4$；$P(t_3 = 1 \mid \mathbf{y}) = 5/6$　†。各 codeword 的概率为：$000$ 是 $1/12$，$011$ 是 $2/12$，$110$ 是 $1/12$，$101$ 是 $8/12$。

（† 原书这三个并列式子全印成 $P(t_1 = 1 \mid \mathbf{y})$，是三连错下标：按 $P_3$ 的码字集合 $\{000, 011, 110, 101\}$ 逐项求和，$t_1 = 1$ 的码字为 $110$ 与 $101$，故第一个值 $3/4 = (1/12 + 8/12)$ 只能属于 $t_1$；$t_2 = 1$ 的码字为 $011$ 与 $110$，$(2/12 + 1/12) = 1/4$ 只能属于 $t_2$；$t_3 = 1$ 的码字为 $011$ 与 $101$，$(2/12 + 8/12) = 10/12 = 5/6$ 只能属于 $t_3$。原文后两处下标应分别改为 $t_2$ 与 $t_3$。）

<span style="color:#1e8449;">**[译注]**
「逐比特解码给出 $0010000$，而它并不是 codeword」这句话是本节的验收点，不是脚注级的闲话。

**量化对照**：MAP codeword $0000000$ 的后验是 $0.3006$；而把逐比特最优拼成的 $0010000$ 代回去算联合后验，七个因子乘起来是 $0.734^{2}\times 0.677\times 0.734^{4} \approx 0.0716$，比 $0.3006$ 低 4.2 倍——也就是说**逐比特最优的那个串，概率上比 MAP 码字差了整整一个数量级的一半**。这不是数值误差，是两种目标函数的差别：$\arg\max_{\mathbf{t}\in\mathcal{C}} P(\mathbf{t}\mid\mathbf{y})$ 与「逐位取边缘最大值」在约束集 $\mathcal{C}$ 上根本不同一个优化问题。

**消失测试**：如果误把逐比特解码当成码字解码來交付，接收端会输出一个不在码里的串，必须再跑一次「最近码字」纠错，而这一步在 $N = 10^{4}$ 时是 NP-hard 的近邻搜索；等价地说，你为了拿每比特的置信度，被迫放弃「输出一定是合法码字」这条保证。反过来，只做 MAP codeword 解码，你得到合法码字但没有每比特置信度，无法给上层 FEC 或 ARQ 做软判决——这两件事在 5G NR 的 LDPC 链里是**分别需要的两个输出**。

**可复算验证**：表 25.8 的 16 个 posterior 逐项求和 $= 1.0002$（16 项各保留 1–3 位有效数字的舍入残差），可接受；likelihood 列乘 $1/Z$ 应得 posterior 列，$0.026/0.0865 = 0.3006$，反解得 $Z \approx 0.0865$，与 $0.000058/0.0007$ 同比例（$0.0829$，舍入范围内一致）。

**落点**：§25.3 的 (25.15)(25.16)、本页两处解答、§1.2 的 $P_3$ 定义；习题本体在 p.329 与 p.330。码字集合 $\{000,011,110,101\}$ 的校验式是 $t_1 \oplus t_2 \oplus t_3 = 0$，与本书 §1.2 一致。
</span>



# 第 26 章　图上的精确边缘化 · Exact Marginalization in Graphs

现在我们对 inference（推断）与 marginalization（边缘化）这两件任务采取更一般的视角。读本章之前，你应该先读过第 16 章关于 message passing（消息传递）的内容。

第 25 章的 trellis 是「图」的一个特例：trellis 的拓扑被码的代数结构钉死了；而本章要说明的是一条更普遍的规律——**只要 P\* 能分解成因子之积，边缘化就能在因子图的树上用局部消息算完**。这条规律一旦抽出来，Viterbi 与 BCJR 就都成了它在一个特定图上的两个特例。

## 26.1 一般问题 · The general problem

假设有一组 $N$ 个变量 $\mathbf{x} \equiv \{x_n\}_{n=1}^{N}$，它们的某个函数 $P^{*}$ 定义为 $M$ 个因子的乘积：

```math
P^{*}(\mathbf{x}) = \prod_{m=1}^{M} f_m(\mathbf{x}_m).
```

（(26.1)）

每个因子 $f_m(\mathbf{x}_m)$ 是「构成 $\mathbf{x}$ 的变量」的某个子集 $\mathbf{x}_m$ 的函数。若 $P^{*}$ 是正函数，那么我们可能还关心第二个、归一化后的函数

```math
P(\mathbf{x}) \equiv \frac{1}{Z} P^{*}(\mathbf{x}) = \frac{1}{Z} \prod_{m=1}^{M} f_m(\mathbf{x}_m),
```

（(26.2)）

其中归一化常数 $Z$ 定义为

```math
Z = \sum_{\mathbf{x}} \prod_{m=1}^{M} f_m(\mathbf{x}_m).
```

（(26.3)）

作为刚才引入的这套记号的一个例子，下面是由五个因子定义的、三个二值变量 $x_1, x_2, x_3$ 的一个函数：

```math
\begin{aligned}
f_1(x_1) &= \begin{cases} 0.1 & x_1 = 0 \\ 0.9 & x_1 = 1 \end{cases} \\
f_2(x_2) &= \begin{cases} 0.1 & x_2 = 0 \\ 0.9 & x_2 = 1 \end{cases} \\
f_3(x_3) &= \begin{cases} 0.9 & x_3 = 0 \\ 0.1 & x_3 = 1 \end{cases} \\
f_4(x_1, x_2) &= \begin{cases} 1 & (x_1, x_2) = (0,0) \text{ or } (1,1) \\ 0 & (x_1, x_2) = (1,0) \text{ or } (0,1) \end{cases} \\
f_5(x_2, x_3) &= \begin{cases} 1 & (x_2, x_3) = (0,0) \text{ or } (1,1) \\ 0 & (x_2, x_3) = (1,0) \text{ or } (0,1) \end{cases}
\end{aligned}
```

```math
\begin{aligned}
P^{*}(\mathbf{x}) &= f_1(x_1)\,f_2(x_2)\,f_3(x_3)\,f_4(x_1, x_2)\,f_5(x_2, x_3) \\
P(\mathbf{x}) &= \frac{1}{Z}\, f_1(x_1)\,f_2(x_2)\,f_3(x_3)\,f_4(x_1, x_2)\,f_5(x_2, x_3).
\end{aligned}
```

（(26.4)）

在一般函数 (26.1) 里记为 $\mathbf{x}_m$ 的那五个子集，在此分别是 $\mathbf{x}_1 = \{x_1\}$、$\mathbf{x}_2 = \{x_2\}$、$\mathbf{x}_3 = \{x_3\}$、$\mathbf{x}_4 = \{x_1, x_2\}$、$\mathbf{x}_5 = \{x_2, x_3\}$。



顺便指出，这个 $P(\mathbf{x})$ 可以认出来是**重复码（repetition code，§1.2）三个发送比特的后验概率分布**：接收信号为 $\mathbf{r} = (1, 1, 0)$、信道是翻转概率 $0.1$ 的 binary symmetric channel（二进制对称信道）时的后验。因子 $f_4$ 与 $f_5$ 分别施加「$x_1$ 必须与 $x_2$ 相同」和「$x_2$ 必须与 $x_3$ 相同」这两条约束；因子 $f_1, f_2, f_3$ 则是 $\mathbf{r}$ 各分量贡献的 likelihood function（似然函数）。

形式为 (26.1) 的因子化函数可以用一张 factor graph（因子图）描绘：变量画成圆形节点，因子画成方形节点。若函数 $f_m(\mathbf{x}_m)$ 对变量 $x_n$ 有任何依赖，就在变量节点 $n$ 与因子节点 $m$ 之间连一条边。(26.4) 那个例子函数的 factor graph 画在图 26.1。

[Figure 26.1：与函数 $P^{*}(\mathbf{x})$ (26.4) 相关联的 factor graph。**可完整复原**，因为它的节点-边表由 (26.4) 唯一确定，原图只是把这张表画了出来。]

复原出的边表（这是本图的内容，不是我的补充）：

| 因子节点 | 类型 | 相连的变量节点 |
|---|---|---|
| $f_1$ | 方形 | $x_1$ |
| $f_2$ | 方形 | $x_2$ |
| $f_3$ | 方形 | $x_3$ |
| $f_4$ | 方形 | $x_1,\; x_2$ |
| $f_5$ | 方形 | $x_2,\; x_3$ |

可复算验证：因子节点的度数为 $1,1,1,2,2$，变量节点的度数为 $2,3,2$（$x_1$ 连 $f_1,f_4$；$x_2$ 连 $f_2,f_4,f_5$；$x_3$ 连 $f_3,f_5$），总边数 $2+3+2 = 7 = 1+1+1+2+2$。这张图是一棵**树**（7 条边、$3+5 = 8$ 个节点、8 个节点 7 条边且连通），这正是 §26.2 的算法能给出精确答案的前提。

### 归一化问题 · The normalization problem

要解的第一个任务是算出归一化常数 $Z$。

### 边缘化问题 · The marginalization problems

要解的第二个任务是算出任一变量 $x_n$ 的 marginal function（边缘函数），定义为

```math
Z_n(x_n) = \sum_{\{x_{n'}\},\; n' \neq n} P^{*}(\mathbf{x}).
```

（(26.5)）

例如，若 $f$ 是三个变量的函数，则 $n = 1$ 的边缘函数定义为

```math
Z_1(x_1) = \sum_{x_2,\, x_3} f(x_1, x_2, x_3).
```

（(26.6)）

「对『除 $x_n$ 之外的所有 $x_{n'}$』求和」这类求和太重要了，专门给它一个记号会很有用——叫 not-sum，也有人叫 summary。

要解的第三个任务是算出任一变量 $x_n$ 的归一化边缘（normalized marginal），定义为

```math
P_n(x_n) \equiv \sum_{\{x_{n'}\},\; n' \neq n} P(\mathbf{x}).
```

（(26.7)）

（我们给 $P_n(x_n)$ 加了下标 $n$，这偏离了本书其余部分的惯例——在别处我们会把这个下标省掉。）

注释一句：$Z_n(x_n)$ 与 $P_n(x_n)$ 的区别只有 $1/Z$，但两者在工程实现里的地位完全不同。$Z_n$ 可以任意缩放（消息传递算法内部就一直在缩放），而 $P_n$ 必须真归一化，因为下游的判决门限是按概率定的。

<span style="color:#b9770e;">**[exercise] Exercise 26.1.**[1] Show that the normalized marginal is related to the marginal $Z_n(x_n)$ by

```math
P_n(x_n) = \frac{Z_n(x_n)}{Z}.
```

（(26.8)）
</span>

> **中文话题摘要**：要证归一化边缘等于未归一化边缘除以 $Z$。一行代数：把 (26.7) 的 $P$ 用 (26.2) 的 $P^{*}/Z$ 展开，$1/Z$ 是常数可提出求和号。

我们还可能关心「若干变量子集上」的边缘，比如

```math
Z_{12}(x_1, x_2) \equiv \sum_{x_3} P^{*}(x_1, x_2, x_3).
```

（(26.9)）

所有这些任务在一般情况下都是 intractable（不可解）的。即便每个因子都只是三个变量的函数，求 $Z$ 与求各边缘的精确解的代价，一般认为也随变量数 $N$ **指数增长**。

不过，对于某些特定的函数 $P^{*}$，可以利用 $P^{*}$ 的因子化结构**高效地**算出边缘。这种高效性从何而来，第 16 章的那些 message-passing 例子已经充分说明。我们下面回顾的 sum–product algorithm 就是 §16 的 message-passing rule-set B（p.242）的推广。正如那里一样，sum–product algorithm **只在图是树状（tree-like）时才有效**。



## 26.2 sum–product 算法 · The sum–product algorithm

### 记号 · Notation

我们用「下标集合」$N(m)$ 来标识第 $m$ 个因子所依赖的变量集合 $\mathbf{x}_m$。对我们那个例子函数 (26.4)，这些集合是 $N(1) = \{1\}$（因为 $f_1$ 只是 $x_1$ 的函数）、$N(2) = \{2\}$、$N(3) = \{3\}$、$N(4) = \{1, 2\}$、$N(5) = \{2, 3\}$。类似地，我们定义「变量 $n$ 参与其中的因子集合」为 $M(n)$。

我们把「集合 $N(m)$ 去掉变量 $n$」记为 $N(m) \setminus n$。再引入简写 $\mathbf{x}_{m \setminus n}$ 或 $\mathbf{x}_{m \backslash n}$，表示 $\mathbf{x}_m$ 中除去 $x_n$ 之后的变量集合，即

```math
\mathbf{x}_{m \setminus n} \equiv \{x_{n'} : n' \in N(m) \setminus n\}.
```

（(26.10)）

sum–product algorithm 涉及两类 message，沿 factor graph 的边传递：变量节点到因子节点的 message $q_{n \to m}$，以及因子节点到变量节点的 message $r_{m \to n}$。沿「连接 $f_m$ 与 $x_n$ 的那条边」传送的 message（无论 $q$ 还是 $r$）**永远是变量 $x_n$ 的函数**。

下面是两组 message 的更新规则。从变量到因子：

```math
q_{n \to m}(x_n) = \prod_{m' \in M(n) \setminus m} r_{m' \to n}(x_n).
```

（(26.11)）

从因子到变量：

```math
r_{m \to n}(x_n) = \sum_{\mathbf{x}_{m \setminus n}} \left( f_m(\mathbf{x}_m) \prod_{n' \in N(m) \setminus n} q_{n' \to m}(x_{n'}) \right).
```

（(26.12)）

这两条规则合起来看，就是「**乘以所有别的入边，然后对不需要的变量求和**」：(26.11) 是纯乘（变量不求和），(26.12) 是乘完再 sum out。第 25 章的 (25.13) 与 (25.15) 正好是这两条在 trellis 上的特例——trellis 是「每个因子只连相邻两个变量」的 factor graph。

### 这两条规则在 factor graph 的叶子处如何应用

只有一个边把它连到另一个节点的节点，称为 leaf node（叶节点）。

[Figure 26.2：作为叶节点的因子节点，永远向它唯一的邻居 $x_n$ 发送 message $r_{m \to n}(x_n) = f_m(x_n)$。**可复原**：单边连接、一个方形节点连一个圆形节点，内容就是这条公式。]

图中有些因子节点可能只连到一个变量节点。这时 (26.12) 里出现的变量集合 $N(m) \setminus n$ 是空集，乘积 $\prod_{n' \in N(m) \setminus n} q_{n' \to m}(x_{n'})$ 是空乘积（empty product），其值为 1。所以这样的因子节点永远向它唯一的邻居 $x_n$ 广播 message $r_{m \to n}(x_n) = f_m(x_n)$。

类似地，也可能有变量节点只连到一个因子节点，于是 (26.11) 里的集合 $M(n) \setminus m$ 是空集。这些节点永远广播 message $q_{n \to m}(x_n) = 1$。

[Figure 26.3：作为叶节点的变量节点，永远发送 message $q_{n \to m}(x_n) = 1$。**可复原**，理由同图 26.2。]

「空乘积 = 1」这一条不是形式上的约定，它是算法能自启动的全部机制：叶子节点不需要「别人先给它消息」，它直接把自己的因子当消息发出去，于是树上就有了第一推动力。若把空乘积定义成别的东西，算法会在叶子上就死锁。

### 启动与收尾，方法 1 · Starting and finishing, method 1

算法有两种初始化方式。若图是 tree-like（树状）的，那么它必然存在叶子节点。这些叶子节点可以从一开始就把各自的消息广播给邻居。



对所有叶变量节点 $n$：

```math
q_{n \to m}(x_n) = 1.
```

（(26.13)）

对所有叶因子节点 $m$：

```math
r_{m \to n}(x_n) = f_m(x_n).
```

（(26.14)）

然后我们可以采用第 16 章 message-passing rule-set B（p.242）里用过的流程：**只有当一条消息所依赖的消息全部到位时**，才按规则 (26.11)、(26.12) 生成这条消息。

[Figure 26.4：函数 $P^{*}(\mathbf{x})$ (26.4) 的模型 factor graph（与图 26.1 同图，此处重画以便标注消息流向）。**可复原**，边表见图 26.1。]

例如在图 26.4 里，从 $x_1$ 发往 $f_1$ 的消息，只有在收到「$f_4$ 发往 $x_1$」的消息之后才会发出；而从 $x_2$ 发往 $f_2$ 的消息 $q_{2 \to 2}$，只有在 $r_{4 \to 2}$ 与 $r_{5 \to 2}$ 两条消息都收到之后才能发出。

这样，消息会沿树流动，每条边上两个方向各一条；经过**等于图的直径（diameter）那么多步**之后，每条消息都会被生成出来。

于是我们需要的答案就可以读出来了。$x_n$ 的 marginal function 由「把该节点上所有入边消息相乘」得到：

```math
Z_n(x_n) = \prod_{m \in M(n)} r_{m \to n}(x_n).
```

（(26.15)）

归一化常数 $Z$ 可以由任何一个 marginal function 求和得到，$Z = \sum_{x_n} Z_n(x_n)$；归一化边缘则由下式得到：

```math
P_n(x_n) = \frac{Z_n(x_n)}{Z}.
```

（(26.16)）

「$Z$ 可以由**任何**一个 marginal 求和得到」这句话自带一条校验：$N$ 个 $Z_n$ 各自求和应当给出同一个数（浮点下到舍入误差）。这条校验在实现里比重跑一遍算法便宜得多，是排查下标错位的首选手段。

<span style="color:#b9770e;">**[exercise] Exercise 26.2.**[2] Apply the sum–product algorithm to the function defined in equation (26.4) and figure 26.1. Check that the normalized marginals are consistent with what you know about the repetition code $R_3$.</span>

> **中文话题摘要**：把 sum–product 跑在 (26.4) 那棵树上，然后核对结果是否与重复码 $R_3$ 的已知后验一致——$R_3$ 三个比特完全相关，故三个边缘必然都相同，这给了你一个不需要算就知道的标准答案。

<span style="color:#b9770e;">**[exercise] Exercise 26.3.**[3] Prove that the sum–product algorithm correctly computes the marginal functions $Z_n(x_n)$ if the graph is tree-like.</span>

> **中文话题摘要**：要证树状图上 sum–product 精确。证明的标准路线是对树做归纳（把树按一条边劈成两半，两半的乘积恰好等于 (26.5) 的求和），或者把 $Z_n(x_n)$ 展开成「所有含 $x_n$ 的项的求和」再逐因子重排。

<span style="color:#b9770e;">**[exercise] Exercise 26.4.**[3] Describe how to use the messages computed by the sum–product algorithm to obtain more complicated marginal functions in a tree-like graph, for example $Z_{1,2}(x_1, x_2)$, for two variables $x_1$ and $x_2$ that are connected to one common factor node.</span>

> **中文话题摘要**：问怎么用已算好的消息拿「两个变量联合」的边缘 $Z_{12}(x_1,x_2)$。答案的形状是把公共因子节点之外的入边全部相乘，再乘公共因子本身，不再对这两变量求和——成本从 $O(2^{2})$ 的重复计算降到常数次乘法。

### 启动与收尾，方法 2 · Starting and finishing, method 2

另一种做法是：把所有「变量→因子」的初始消息都置 1 来初始化算法：

```math
\text{for all } n, m:\quad q_{n \to m}(x_n) = 1,
```

（(26.17)）

然后交替执行因子消息更新规则 (26.12) 与变量消息更新规则 (26.11)。与方法 1 相比，这种 lazy initialization（惰性初始化）方式会造成大量无用计算，它们的结果会被方法 1 算出的正确答案逐波冲掉。经过**等于 factor graph 直径**那么多次迭代之后，算法会收敛到满足 sum–product 关系 (26.11)、(26.12) 的一组消息。

<span style="color:#b9770e;">**[exercise] Exercise 26.5.**[2] Apply this second version of the sum–product algorithm to the function defined in equation (26.4) and figure 26.1.</span>

> **中文话题摘要**：用手算把惰性初始化版的 sum–product 跑一遍，观察前几轮出现的「垃圾消息」如何在直径步之后被冲干净。这题的价值是让你亲眼看到「收敛」在树上其实是「传播到底」，不含任何迭代逼近。



引入这种惰性方法的理由是：（与方法 1 不同）它可以应用到**非树状**的图上。当 sum–product algorithm 在一个含环（cycles）的图上运行时，算法不必然收敛，而且一般肯定算不出正确的 marginal functions；但尽管如此，它在实践中仍是一个极其重要的算法，尤其是在稀疏图码（sparse-graph codes）的解码中。

### 带即时归一化的 sum–product 算法 · Sum–product algorithm with on-the-fly normalization

若我们只关心归一化的边缘，那么另一个版本的 sum–product algorithm 可能有用。因子到变量的消息 $r_{m \to n}$ 的算法与 (26.12) 完全相同，但变量到因子的消息要这样归一化：

```math
q_{n \to m}(x_n) = \alpha_{nm} \prod_{m' \in M(n) \setminus m} r_{m' \to n}(x_n),
```

（(26.18)）

其中 $\alpha_{nm}$ 是一个标量，取值使得

```math
\sum_{x_n} q_{n \to m}(x_n) = 1.
```

（(26.19)）

<span style="color:#b9770e;">**[exercise] Exercise 26.6.**[2] Apply this normalized version of the sum–product algorithm to the function defined in equation (26.4) and figure 26.1.</span>

> **中文话题摘要**：用归一化版重跑 (26.4)，注意 $\alpha_{nm}$ 把每步的数值范围压回 $O(1)$，所以整条链上不会出现 $0.1^{10000}$ 这种下溢，也不会出现 $10^{300}$ 这种上溢。

### sum–product 算法的因子化视角 · A factorization view of the sum–product algorithm

看 sum–product algorithm 的一种方式是：它把原来的因子化函数——$M$ 个因子之积 $P^{*}(\mathbf{x}) = \prod_{m=1}^{M} f_m(\mathbf{x}_m)$——重新表达成**另一个**因子化函数，后者是 $M + N$ 个因子之积：

```math
P^{*}(\mathbf{x}) = \prod_{m=1}^{M} \varphi_m(\mathbf{x}_m) \prod_{n=1}^{N} \psi_n(x_n).
```

（(26.20)）

每个因子 $\varphi_m$ 与因子节点 $m$ 关联，每个因子 $\psi_n(x_n)$ 与一个变量节点关联。初始时 $\varphi_m(\mathbf{x}_m) = f_m(\mathbf{x}_m)$、$\psi_n(x_n) = 1$。每当一条因子到变量的消息 $r_{m \to n}(x_n)$ 被送出，因子化就按下式更新：

```math
\psi_n(x_n) = \prod_{m \in M(n)} r_{m \to n}(x_n),
```

（(26.21)）

```math
\varphi_m(\mathbf{x}_m) = \frac{f_m(\mathbf{x}_m)}{\prod_{n \in N(m)} r_{m \to n}(x_n)}.
```

（(26.22)）

而每条消息都可以用 $\varphi$ 与 $\psi$ 表出：

```math
r_{m \to n}(x_n) = \sum_{\mathbf{x}_{m \setminus n}} \left( \varphi_m(\mathbf{x}_m) \prod_{n' \in N(m)} \psi_{n'}(x_{n'}) \right),
```

（(26.23)）

它与赋值式 (26.12) 的差别在于：这里的乘积取遍**全部** $n' \in N(m)$。

（† (26.22) 的分子原文排印为 $f(\mathbf{x}_m)$，缺下标 $m$；(26.1) 与 (26.22) 的语境只允许 $f_m$，否则「$M$ 个因子」中的第 $m$ 个无从指认。）

<span style="color:#b9770e;">**[exercise] Exercise 26.7.**[2] Confirm that the update rules (26.21–26.23) are equivalent to the sum–product rules (26.11–26.12). So $\psi_n(x_n)$ eventually becomes the marginal $Z_n(x_n)$.</span>

> **中文话题摘要**：要证这套 $\varphi/\psi$ 更新与 (26.11)(26.12) 等价，且 $\psi_n$ 最终就是 $Z_n(x_n)$。这题是 §26.2 的概念核心：它说明消息传递**不是**一套独立算法，而是「把同一个乘积重新分配到因子与变量上去」的守恒重排。

这个因子化视角**无论图是否树状都成立**。

<span style="color:#1e8449;">**[译注]**
这一页有两句必须钉死的话：「环上不保证收敛、一般算不出正确边缘」和「它仍是实践中极其重要的算法」。两句看似矛盾，其实界定了整个 §26.2 的适用范围。

**为什么环上会错**：树上任意两节点只有一条路，(26.15) 里每个因子恰好计入一次；一有环，路径信息绕回来把自己当外部证据再用一遍，等于「重复计数」。(26.22) 的除法在树上除尽无余、在环上除不干净，残留项就是误差。

**量的方向感**：误差不是随环长缓慢增长，而是由 girth 决定。girth 为 $g$ 的正则图上，belief propagation 的前 $g/2$ 轮迭代与真值**完全一致**（这一段是树），第 $g/2 + 1$ 轮才开始错；所以 LDPC 码的设计指标里「$\text{girth} \ge 6$」是为了让错误只在深层出现：码长 $10^{4}$、girth $6$ 时前 3 轮无偏。

**消失测试**：抽掉「树状」这个前提而仍然信任 (26.15) 的输出，你在环图上的 marginals 会系统性偏向过度自信（over-confident），译码器给出高置信度的错误判决，表现为误码率曲线在低信噪比区「假性穿底」然后在高信噪比区出现 error floor（$10^{-6}$ 附近的平台）。这条平台正是 turbo / LDPC 工程里要用 outer code 打掉的。

**落点**：§26.2 本页、§26.4 的 loopy message passing、§33.8 与第 47 章；收敛性的定量条件见 Yedidia et al. (2000)（本页 Further reading 已列），可作 L4 前沿的入口。挂 6.042J 的树与连通性（「树上任意两点唯一路径」是 (26.15) 成立的组合根据），无越级。
</span>



### 计算技巧 · Computational tricks

从计算的角度看，即时归一化是个好主意：因为若 $P^{*}$ 是**很多**因子的乘积，它的取值很可能极大或极小。

另一个有用的计算技巧是：传递 message $q$ 与 $r$ 的**对数**，而不是 $q$ 与 $r$ 本身；于是算法 (26.11)、(26.12) 里那些乘积计算就被更简单的加法取代。当然，(26.12) 里的求和会变得更难：要在求和之后返回对数，需要计算这样的 softmax 函数：

```math
l = \ln\left( e^{l_1} + e^{l_2} + e^{l_3} \right).
```

（(26.24)）

但这个计算可以高效完成：用查表法，加上一条观察——答案 $l$ 的值通常只比 $\max_i l_i$ 略大一点。如果我们把函数

```math
\ln\left( 1 + e^{\delta} \right)
```

（(26.25)）

（对负的 $\delta$）的值存进查表，那么 $l$ 就能精确地用「与求和项数同阶」次查表与加法算出。如果查表与排序运算比 `exp()` 便宜，那么这种做法的成本低于直接计算 (26.24)。此外，通过略去 $\{l_i\}$ 中最小的那些项的「可忽略贡献」，运算次数还能进一步减少。

适用于某些纠错码的第三个计算技巧是：不传 message 本身，而传 message 的 **Fourier transform（傅里叶变换）**。这同样能使因子到变量消息的计算更快。这个 Fourier 变换技巧的一个简单例子在第 47 章的 (47.9) 给出。

### 26.3 min–sum 算法 · The min–sum algorithm

sum–product algorithm 解决的是「求给定乘积 $P^{*}(\mathbf{x})$ 的 marginal function」这一任务。这与 §25.1 的逐比特解码问题相仿。而正像还有别的解码问题（例如码字解码问题），我们也可以定义涉及 $P^{*}(\mathbf{x})$ 的别的任务，它们能由 sum–product algorithm 的各种修改版解决。例如，考虑下面这个与码字解码问题相仿的任务：

**最大化问题（The maximization problem）**：找出使乘积 $P^{*}(\mathbf{x})$ 最大的 $\mathbf{x}$ 取值。

这个问题可以通过「把 sum–product algorithm 里出现的 add 与 multiply 两个运算，处处换成另一对满足分配律（distributive law）的运算，即 max 与 multiply」来解决。若我们把求和 $(+, \sum)$ 换成最大化，就会发现那个原先叫归一化常数的量

```math
Z = \sum_{\mathbf{x}} P^{*}(\mathbf{x})
```

（(26.26)）

变成了 $\max_{\mathbf{x}} P^{*}(\mathbf{x})$。

于是 sum–product algorithm 可以变成一个 **max–product algorithm**，它算出 $\max_{\mathbf{x}} P^{*}(\mathbf{x})$，从而可以推出最大化问题的解。此时每个「边缘」$Z_n(x_n)$ 列出的是「对 $x_n$ 的每个取值，$P^{*}(\mathbf{x})$ 所能达到的最大值」。



实践中，max–product algorithm 最常放在 negative log likelihood 域里执行，那里 max 与 product 变成 min 与 sum。min–sum algorithm 也叫 Viterbi algorithm。

「分配律」三个字是这一步替换合法的**唯一**理由：$a\cdot(b+c) = ab + ac$ 与 $a\cdot\max(b,c) = \max(ab, ac)$（$a \gt 0$）形状相同，所以 (26.11)(26.12) 的全部代数变形逐字照搬。换成不满足分配律的运算对（例如 average 与 multiply），消息传递的正确性立刻失效。

### 26.4 junction tree 算法 · The junction tree algorithm

当你关心的 factor graph **不是**树时，该怎么办？有若干选项，它们分成精确方法与近似方法两类。

处理带环图上的边缘化，最广泛使用的精确方法叫 junction tree algorithm（联结树算法）。这个算法的做法是：把变量聚合成簇（agglomerate），直到聚合后的图不再含环。细节你大概能自己想出来；边缘化的复杂度随「被聚合的变量数」**指数增长**。关于 junction tree algorithm 的更多内容，可读（Lauritzen, 1996; Jordan, 1998）。

近似方法很多，我们会在接下来几章里陆续见到一些——Monte Carlo 方法与 variational 方法，仅举两种。不过，处理「sum–product algorithm 未必适用」的 factor graph 最有趣的办法，如前所述，就是**照样用 sum–product algorithm**！

我们就按「图是树」那样，为图中每个节点计算消息，迭代，然后祈祷（cross our fingers）。这种所谓的 loopy message passing（带环消息传递）在纠错码解码中极其重要，我们会在 §33.8 与第 VI 部分回到它。

### 延伸阅读 · Further reading

关于 factor graph 与 sum–product algorithm 的进一步阅读，见 Kschischang et al. (2001)、Yedidia et al. (2000)、Yedidia et al. (2001a)、Yedidia et al. (2002)、Wainwright et al. (2003) 与 Forney (2001)。另见 Pearl (1988)。图模型基础理论的一个好参考是 Lauritzen (1996)。Bayesian network（贝叶斯网络）方面有一本可读的入门是 Jensen (1996)。

能力与 sum–product algorithm 不同的有趣 message-passing 算法包括 expectation propagation（Minka, 2001）与 survey propagation（Braunstein et al., 2003）。另见 §33.8。

### 26.5 习题 · Exercises

<span style="color:#b9770e;">**[exercise] Exercise 26.8.**[2] Express the joint probability distribution from the burglar alarm and earthquake problem (example 21.1 (p.293)) as a factor graph, and find the marginal probabilities of all the variables as each piece of information comes to Fred's attention, using the sum–product algorithm with on-the-fly normalization.</span>

> **中文话题摘要**：把 p.293 例 21.1 那个「盗窃报警器 + 地震」的联合分布画成 factor graph，然后模拟 Fred 逐步收到信息的过程，用带即时归一化的 sum–product 每次重算全部变量的边缘。这题练的是「增量更新」——每来一条新证据只需改一个因子，其余消息可复用。

<span style="color:#1e8449;">**[译注]**
§26.4 里「最有趣的办法就是照样用 sum–product」这句玩笑，是全书对「精确 vs 近似」最锋利的一次划界，值得把它的代价算清楚。

**两个方向的量化**：走 junction tree（精确）路线，复杂度是 $O(2^{w})$，$w$ 是最大簇（treewidth）。$(7,4)$ Hamming 码的 trellis 就是 treewidth 很小的特例；而 $1000$ 比特的随机 LDPC 码 treewidth 接近 $N$，$2^{1000}$ 不可行。走 loopy BP（近似）路线，每轮 $O(|\text{edges}|)$，$N = 10^{4}$、度 3 的码 $|\text{edges}| \approx 1.5\times10^{4}$，跑 $50$ 轮也只有 $7.5\times10^{5}$ 次乘加——**同样一个问题，精确解 $2^{1000}$，近似解 $10^{5}$**，这就是为什么 §33.8 值得单独写一节。

**失效对象（反过来的一条）**：把 loopy BP 当精确算法用，会在高信噪比处留下 error floor（约 $10^{-6}$ 到 $10^{-8}$ 的误码平台），因为它算出的「边缘」在环上系统性过自信；而把 junction tree 当通用算法用，会在 treewidth 超过约 30 的图上直接跑不动（$2^{30}$ 个簇状态）。两条失效都是硬墙，不是调参能绕过的。

**一句可检验的判断**：任何声称「用消息传递精确求解这个带环图」的说法，必须给出环的处理方式（junction tree 的簇构造，或 loopy BP 的收敛证据），否则这句话在 §26.4 的语境里就是错的。

**落点**：§26.4 本页、§33.8、第 47 章 (47.9)、(26.24)(26.25) 的 log 域技巧；treewidth 与 6.006 的图算法章节可对照（同一套「把图变小的代价是指数」的思路）。
</span>



# 第 27 章　Laplace 方法 · Laplace's Method

Laplace approximation（拉普拉斯近似）背后的想法很简单。我们假定有一个未归一化的概率密度 $P^{*}(x)$，它的归一化常数

```math
Z_P \equiv \int P^{*}(x)\, dx
```

（(27.1)）

是我们关心的量，并且假定它在某点 $x_0$ 处有一个峰。我们在这个峰附近对 $P^{*}(x)$ 的**对数**做 Taylor 展开：

```math
\ln P^{*}(x) \simeq \ln P^{*}(x_0) - \frac{c}{2}(x - x_0)^2 + \cdots,
```

（(27.2)）

其中

```math
c = -\left. \frac{\partial^2}{\partial x^2} \ln P^{*}(x) \right|_{x = x_0}.
```

（(27.3)）

然后我们用一个未归一化的 Gaussian（高斯）来近似 $P^{*}(x)$：

```math
Q^{*}(x) \equiv P^{*}(x_0)\, \exp\left[ -\frac{c}{2}(x - x_0)^2 \right],
```

（(27.4)）

并用这个 Gaussian 的归一化常数来近似 $Z_P$：

```math
Z_Q = P^{*}(x_0) \sqrt{\frac{2\pi}{c}}.
```

（(27.5)）

这个积分可以推广到 $K$ 维空间：设 $P^{*}(\mathbf{x})$ 是 $K$ 维空间 $\mathbf{x}$ 上的密度。若 $-\ln P^{*}(\mathbf{x})$ 在最大值点 $\mathbf{x}_0$ 处的二阶导数矩阵为 $A$，定义为

```math
A_{ij} = -\left. \frac{\partial^2}{\partial x_i \partial x_j} \ln P^{*}(\mathbf{x}) \right|_{\mathbf{x} = \mathbf{x}_0},
```

（(27.6)）

于是展开式 (27.2) 被推广为

```math
\ln P^{*}(\mathbf{x}) \simeq \ln P^{*}(\mathbf{x}_0) - \frac{1}{2}(\mathbf{x} - \mathbf{x}_0)^{\mathsf{T}} A (\mathbf{x} - \mathbf{x}_0) + \cdots,
```

（(27.7)）

那么归一化常数可以近似为：

```math
Z_P \simeq Z_Q = P^{*}(\mathbf{x}_0)\, \frac{1}{\sqrt{\det\left( \frac{1}{2\pi} A \right)}} = P^{*}(\mathbf{x}_0) \sqrt{\frac{(2\pi)^{K}}{\det A}}.
```

（(27.8)）

用近似 $Q$ 就可以做预测了。物理学家也把这个广泛使用的近似叫作 saddle-point approximation（鞍点近似）。

[Figure 27.1：Laplace 近似对一维密度的示意——实线为 $\ln P^{*}(x)$，虚线为二次展开 $\ln Q^{*}(x)$，另一组实线/虚线为 $P^{*}(x)$ 与 $Q^{*}(x)$ 本身，峰位标 $x_0$。**曲线形状不可复原**：本图是矢量曲线图，文字层只留下峰附近的两三处标签（抽取结果是散落的 `ln P*(x)`、`ln Q*(x)`、`P*(x)`、`Q*(x)` 几行），曲线的具体曲率与交点位置无法恢复；可据 (27.2)–(27.5) 重画，形状由 $c$ 唯一决定。]

<span style="color:#1e8449;">**[译注]**
(27.8) 那一步的「两种写法等价」值得亲手验一遍，因为它决定你在代码里怎么算：$\det$ 作用在标量矩阵上。

```math
\det\left( \frac{1}{2\pi} A \right) = \frac{\det A}{(2\pi)^{K}}, \qquad
\frac{1}{\sqrt{\det\left( \frac{1}{2\pi}A \right)}} = \sqrt{\frac{(2\pi)^{K}}{\det A}}.
```

**量的方向感**：$K = 100$、每维二阶导数量级为 $1$（即 $\det A \approx 1$）时，$Z_Q$ 相对峰高 $P^{*}(\mathbf{x}_0)$ 的因子是 $(2\pi)^{K/2} \approx (2\pi)^{50} \approx 10^{40}$——**这个因子必须留着**。忘了它，你在 $100$ 维下会把 evidence 低估 $40$ 个数量级，而 evidence 是第 28 章模型比较唯一的打分函数。

**失效对象**：Laplace 近似的误差来源只有一个——展开式里那个「$+\cdots$」（三阶及以上的项）。它们在 $|x - x_0| \gtrsim \sqrt{1/|c_3|}$ 的地方变得和一阶项同量级，于是**后验必须近似单峰、且在峰附近足够窄**。破了这条前提，$Z_Q$ 可能把真实积分估大几个数量级：多峰后验里，只有最尖的那个峰被算进来，其余峰的质量全丢——这正好是混合模型、多峰 likelihood 的常态。为什么多峰的 Laplace 仍然是工程标准件？因为它的失效是**已知方向的**（低估其他峰），而不是随机噪声。

**落点**：本章 (27.1)–(27.8)、§27.1 的三道习题、第 28 章 (28.7) 与 (28.8)（evidence 的 Laplace 近似）、本书 §4.5（Laplace 在这之前已用过一次）；线性代数侧挂 Strang 的「对称矩阵对角化 + 特征值之积 = 行列式」（(27.10) 的分离积分就是这件事）。无越级。
</span>



Gaussian 的归一化常数由下式给出：

```math
\int d^{K}\mathbf{x}\; \exp\left( -\frac{1}{2} \mathbf{x}^{\mathsf{T}} A \mathbf{x} \right) = \sqrt{\frac{(2\pi)^{K}}{\det A}},
```

（(27.9)）

这一点可以这样证明：作一个正交变换，变到使 $A$ 成为对角矩阵的那组基 $\mathbf{u}$ 里。积分于是分离成若干一维积分之积，每一个都是

```math
\int du_i\; \exp\left( -\frac{1}{2} \lambda_i u_i^{2} \right) = \sqrt{\frac{2\pi}{\lambda_i}}.
```

（(27.10)）

特征值 $\lambda_i$ 的乘积就是 $A$ 的行列式。

Laplace approximation 是**依赖于基的（basis-dependent）**：若把 $x$ 变换成一个非线性函数 $u(x)$，并把密度变换成 $P(u) = P(x)\,|dx/du|$，那么一般说来，近似得到的归一化常数 $Z_Q$ 会**不同**。这既可以看成缺陷（因为真值 $Z_P$ 是与基无关的），也可以看成机会（因为我们可以去找一个使 Laplace approximation 最准确的基）。

<span style="color:#1e8449;">**[译注]**
「basis-dependent」这四个字在 (27.8) 里没有任何痕迹，因为 (27.8) 长得像一条与坐标无关的公式；它其实**只在参数化选定之后才有意义**。

**为什么必然依赖**：Laplace 近似的核心假设是「峰附近二次型足够」，而二次近似的曲率 $A_{ij} = -\partial_i\partial_j \ln P^{*}$ 在非线性重参数化下不是张量——它会多出一个 $\partial^2 u / \partial x^2$ 的项。取 $u = \ln x$、$P^{*}(x) = x^{a}e^{-x}$（$a = 100$ 时峰在 $x = 100$），在 $x$ 坐标下 $c = -\partial^2 \ln P^{*}/\partial x^2 = a/x^{2} = 100/10^{4} = 10^{-2}$，于是 $Z_Q = P^{*}(x_0)\sqrt{2\pi/10^{-2}} \approx 25\,P^{*}(x_0)$；换到 $u$ 坐标后，曲率变成 $c_u = a = 100$（因为 $\ln P^{*}(x(u)) = a u - e^{u}$ 的峰处二阶导 $= e^{u_0} = x_0 = 100$），$Z_Q^{(u)} = P^{*}\sqrt{2\pi/100} \approx 0.25\,P^{*}$——**两百倍的差别**，只因为换了一个单调坐标变换。

**失效对象（可被反驳的那一条）**：如果拿两个**参数化不同**的模型的 Laplace evidence 直接比大小，你会得到一个与你的坐标选择有关的排序——即模型比较的结果可以通过改参数化来翻转。这就是为什么第 28 章的 Occam factor 必须与**同一个参数化下的先验体积**配对使用，也是 (28.8) 里 $\sigma_{w|D}/\sigma_w$ 这个**比值**才有意义的原因：比值的分子分母同时受同一次坐标变换影响，比值的失真是一阶而非零阶。

**可复算验证**：$a = 100$ 时峰位 $x_0 = a$，$c = 1/x_0 = 0.01$，$\sqrt{2\pi/c} = \sqrt{628.3} \approx 25.06$；换基后 $\sqrt{2\pi/c_u} = \sqrt{0.0628} \approx 0.2506$，两值之比恰为 $100 = x_0$，即 Jacobian $|dx/du| = x_0$ 被精确地吸收了。

**落点**：§27 本页、§27.1 Exercise 27.1（正是「对 $\lambda$ 与对 $\log\lambda$ 分别做 Laplace」这道题）、第 28 章 (28.8)；挂 Strang 的正交对角化与特征值乘积（(27.9)(27.10)）。无越级。
</span>

## 27.1 习题 · Exercises

<span style="color:#b9770e;">**[exercise] Exercise 27.1.**[2] (See also exercise 22.8 (p.307).) A photon counter is pointed at a remote star for one minute, in order to infer the rate of photons arriving at the counter per minute, $\lambda$. Assuming the number of photons collected $r$ has a Poisson distribution with mean $\lambda$,

```math
P(r \mid \lambda) = \frac{\exp(-\lambda)\,\lambda^{r}}{r!},
```

（(27.11)）

and assuming the improper prior $P(\lambda) = 1/\lambda$, make Laplace approximations to the posterior distribution (a) over $\lambda$ (b) over $\log \lambda$. [Note the improper prior transforms to $P(\log\lambda) = \text{constant}$.]</span>

> **中文话题摘要**：一个光子计数器对远处恒星计数一分钟，收到 $r$ 个光子，要推断「每分钟到达率 $\lambda$」。要求分别在 $\lambda$ 与 $\log\lambda$ 两个参数化下做 Laplace 近似，并与 $P(\lambda) = 1/\lambda$ 的 improper prior 配对使用。这道题就是上一页「basis-dependence」的实操：两个参数化给出不同的 $Z_Q$，而只有其中一个（$\log\lambda$）与均匀先验相容。

<span style="color:#b9770e;">**[exercise] Exercise 27.2.**[2] Use Laplace's method to approximate the integral

```math
Z(u_1, u_2) = \int_{-\infty}^{\infty} da\; f(a)^{u_1}\,(1 - f(a))^{u_2},
```

（(27.12)）

where $f(a) = 1/(1 + e^{-a})$ and $u_1, u_2$ are positive. Check the accuracy of the approximation against the exact answer (23.29, p.316) for $(u_1, u_2) = (1/2, 1/2)$ and $(u_1, u_2) = (1, 1)$. Measure the error $(\log Z_P - \log Z_Q)$ in bits.</span>

> **中文话题摘要**：把 logistic 函数 $f(a)$ 的幂次积分用 Laplace 近似算出来，再与 (23.29) 那个精确的 beta 积分比较。$u_1 = u_2 = 1/2$ 时积分可以被精确算出（对应 arcsin 分布），所以这题能给出**定量误差**，误差用 bit 度量。这是全书少数能把「近似误差有多大」写成一个数的地方。

<span style="color:#b9770e;">**[exercise] Exercise 27.3.**[3] Linear regression. $N$ datapoints $\{(x^{(n)}, t^{(n)})\}$ are generated by the experimenter choosing each $x^{(n)}$, then the world delivering a noisy version of the linear function

```math
y(x) = w_0 + w_1 x,
```

（(27.13)）

```math
t^{(n)} \sim \text{Normal}\left( y(x^{(n)}), \sigma_\nu^{2} \right).
```

（(27.14)）

Assuming Gaussian priors on $w_0$ and $w_1$, make the Laplace approximation to the posterior distribution of $w_0$ and $w_1$ (which is exact, in fact) and obtain the predictive distribution for the next datapoint $t^{(N+1)}$, given $x^{(N+1)}$. (See MacKay (1992a) for further reading.)</span>

> **中文话题摘要**：线性回归 + Gaussian 先验，问 Laplace 近似给出的 $w_0, w_1$ 后验与下一个数据点的预测分布。原文自己点明了关键事实：「which is exact, in fact」——当 likelihood 与 prior 都是 Gaussian 时，后验严格是 Gaussian，Laplace 近似**零误差**，所以这题是检验你逼近代数有没有写错的对照组。



# 第 28 章　模型比较与奥卡姆剃刀 · Model Comparison and Occam's Razor

[Figure 28.1：一张待解释的图片，画着一棵树和几个箱子。**几何布局不可复原**：这是位图插画，文字层只留下「A picture to be interpreted. It contains a tree and some boxes.」这行 caption，树的轮廓与箱子的位置无法从文字恢复，也不能靠猜补画。图的作用是提问题，不是给数据。]

## 28.1 奥卡姆剃刀 · Occam's razor

图 28.1 里有多少个箱子？特别是，树附近有多少个箱子？如果我们戴上 X 光眼镜去看，树干后面会看到**一个**箱子还是**两个**（图 28.2）？（或者更多？）

[Figure 28.2：树后面有几个箱子？图里只留下两个待选标注 `1?` 与 `2?`。**几何布局不可复原**，理由同图 28.1；可复原的只有「两个互斥假设：1 个箱子 / 2 个箱子」这个决策结构。]

Occam's razor（奥卡姆剃刀）是一条主张「偏好简单理论」的原则：「接受能拟合数据的最简解释」。于是按 Occam's razor，我们应当推断树后只有**一个**箱子。

这是一条 ad hoc 的经验法则吗？还是有令人信服的理由，让我们相信「最可能只有一个箱子」？也许你的直觉喜欢这个论证：「嗯，两个箱子恰好在高度和颜色上完全相同，那也太巧了。」如果我们想造出能正确解释数据的人工智能，就必须把这种直觉翻译成**具体的理论**。

### Occam's razor 的动机 · Motivations for Occam's razor

若有若干种解释与一组观测相容，Occam's razor 建议我们买最简单的那个。这条原则常被用两种理由之一来主张：第一种是审美理由（「一个具有数学美的理论，比一个丑陋却能拟合某些实验数据的理论更可能正确」（Paul Dirac））；第二种理由是 Occam's razor 过去的经验成功。

然而 Occam's razor 还有一个不同的正当化理由，即：

> **Coherent inference（自洽推断，即由 Bayesian probability 所体现的那种）自动、定量地体现了 Occam's razor。**

树后只有**一个**箱子的确更可能，而且我们能算出「一个」比「两个」可能多少。

<span style="color:#1e8449;">**[译注]**
本章的全部赌注押在这一句上：Occam's razor 不是额外加的偏好，而是**归一化的算术后果**。

**机制一句话**：一个模型要能被称作「概率模型」，它的预测必须在数据空间上归一化，$\int P(D \mid H_i)\,dD = 1$。复杂模型能预测更多种数据，所以它必须把同一份总概率**摊得更薄**。落在某个具体数据集上时，摊薄的模型得分就低。这就是 (28.1) 第二个因子在起作用的全部内容。

**量的方向感**：模型每多一个自由参数，数据空间体积大约乘上「参数先验范围 / 数据精度」这个比值，于是 evidence 里就多一个**小于 1** 的因子。第 28 章后文（p.349 起）会把它写成 Occam factor $\approx \sigma_{w\mid D}/\sigma_w$，其中 $\sigma_{w\mid D}$ 是后验宽度、$\sigma_w$ 是先验宽度——一个 $N$ 数据点的拟合，$\sigma_{w\mid D} \sim \sigma_w/\sqrt{N}$，所以每个参数贡献约 $1/\sqrt{N}$ 的罚分；$N = 100$、$3$ 个多余参数就是 $100^{-3/2} = 10^{-3}$，即 10 bits。

**消失测试**：抽掉归一化这条要求（比如改用「只看 likelihood 的最大值」来挑模型），复杂模型永远赢——加参数只会把 $\max_w P(D\mid w, H)$ 抬高或持平。你会选中一个能把训练集拟合到零误差、但预测方差大到无用的模型；这就是「maximum likelihood model choice leads us inevitably to implausible, over-parameterized models, which generalize poorly」这句话的机制（p.347 原文）。

**落点**：§28.1 本页、p.344 图 28.3（几何图像）、p.345 的 (28.2)(28.3)（四千万比一的算例）、p.348 的 (28.7)(28.8)（Occam factor 的解析形式）。挂 Strang 的投影与最小二乘（「加参数只会让残差平方和单调不增」正是这里要罚的东西），同时对齐本书 §4.5 与 §22.5 Exercise 22.14 关于「密度最大值不等于概率质量」的讨论。
</span>



[Figure 28.3：为什么 Bayesian inference  embodies Occam's razor。本图给出「复杂模型为何可能反而不那么可能」的基本直觉。横轴表示「可能的数据集 $D$ 所构成的空间」。Bayes' theorem 按「模型对实际发生的数据预测得有多好」成比例地奖励模型；这些预测由 $D$ 上的一个归一化概率分布来量化。给定模型 $H_i$ 时数据的这个概率 $P(D \mid H_i)$ 称为 $H_i$ 的 evidence（证据）。一个简单模型 $H_1$ 只做出有限范围内的预测，如图中标 $P(D \mid H_1)$ 的窄峰；一个更强的模型 $H_2$（例如比 $H_1$ 有更多自由参数）能预测更多种类的数据集。然而这意味着 $H_2$ 在区域 $C_1$ 上并不像 $H_1$ 那样强地预测这些数据集。设两个模型被赋予相等的先验概率，那么若数据集落在区域 $C_1$ 内，较弱的模型 $H_1$ 就是更可能的模型。**曲线位置与宽度不可复原**：文字层只留下两组峰标注 `P(D|H)2`、`P(D|H)1` 与区域标记 `C`、`D`，两峰的相对高度与交叠位置无法恢复；可据「两分布各自归一化、$H_2$ 更宽」这一条重画。]

（本图脚下接 p343 末段的正文。）上面这段是图 28.3 的完整 issue 内容；正文在此接续：

### 模型比较与 Occam's razor · Model comparison and Occam's razor

我们按如下方式，在数据 $D$ 的光照下评估两个备选理论 $H_1$ 与 $H_2$ 的可信度：用 Bayes' theorem，把「给定数据时模型 $H_1$ 的可信度」$P(H_1 \mid D)$，与「模型对数据所做的预测」$P(D \mid H_1)$、以及「$H_1$ 的先验可信度」$P(H_1)$ 联系起来。于是得到理论 $H_1$ 与理论 $H_2$ 之间的如下概率比：

```math
\frac{P(H_1 \mid D)}{P(H_2 \mid D)} = \frac{P(H_1)}{P(H_2)} \, \frac{P(D \mid H_1)}{P(D \mid H_2)}.
```

（(28.1)）

右端第一个比值 $P(H_1)/P(H_2)$ 度量「我们最初的信念在多大程度上偏向 $H_1$ 而非 $H_2$」。第二个比值表达「观测到的数据被 $H_1$ 预测得有多好」，与 $H_2$ 相比。

当 $H_1$ 是比 $H_2$ 更简单的模型时，这跟 Occam's razor 如何相关？第一个比值 $P(H_1)/P(H_2)$ 给了我们机会——如果我们愿意的话——基于审美理由或基于经验，插入一个偏向 $H_1$ 的先验偏见。这对应前面提到的 Occam's razor 的审美动机与经验动机。但这样的先验偏见**并非必需**：第二个比值，即依赖数据的那个因子，**自动**体现了 Occam's razor。简单的模型倾向于做出精确的预测。复杂的模型按其本性，有能力做出更多种类的预测（图 28.3）。所以若 $H_2$ 是更复杂的模型，它必须把它的预测概率 $P(D \mid H_2)$ 摊得比 $H_1$ 更薄地铺在数据空间上。于是，在两个理论都与数据相容的情形下，更简单的 $H_1$ 会显得比 $H_2$ 更可能，而我们无需表达任何对复杂模型的主观反感。我们的主观先验只需在「简单」与「复杂」两类可能性上赋予相等的先验概率。剩下的，概率论允许观测到的数据来表达它们自己的意见。

（† 原文此处出现脚注编号 `2`，对应 p.345 末尾那句「This answer depends on several subjective assumptions...」的脚注，而编号 `1` 属于 Dirac 引文所在的那条；本块按语义把两条脚注归位，不复原编号错位本身。）

### 一个算例 · Let us turn to a simple example

下面是一个数列：$-1,\; 3,\; 7,\; 11$。任务是预测接下来的两个数，并推断产生这个数列的底层过程。

对这个问题，一个流行的答案是预测「$15,\; 19$」，解释是「在前一个数上加 4」。那么另一个备选答案呢：预测「$-19.9,\; 1043.8$」，其底层规则是「由前一个数 $x$ 得到下一个数，通过计算



$-x^{3}/11 + 9/11\,x^{2} + 23/11$」？我想这个预测看起来就不那么可信了。但第二条规则对这个数据 $(-1, 3, 7, 11)$ 的拟合，和「加 4」那条规则**一样好**。那么为什么我们该觉得它不那么可信？让我们给这两个一般性理论各贴一个标签：

- $H_a$——该数列是一个 arithmetic progression（等差数列），即「加 $n$」，其中 $n$ 是整数。
- $H_c$——该数列由一个形如 $x \mapsto c x^{3} + d x^{2} + e$ 的三次函数生成，其中 $c, d, e$ 是有理数（原文写 fractions，即分数）。

觉得第二种解释 $H_c$ 不那么可信的一个理由，也许是「等差数列比三次函数更常遇到」。这等于在 (28.1) 的先验概率比 $P(H_a)/P(H_c)$ 里塞进一个偏见。但我们还是给两个理论**相等的先验概率**，把注意力集中在数据说了什么上。每个理论对数据的预测有多好？

要得到 $P(D \mid H_a)$，我们必须规定每个模型在其参数上赋予的概率分布。首先，$H_a$ 依赖于所加的整数 $n$，以及数列的第一个数。设这些数各自可以是 $-50$ 与 $50$ 之间的任何整数。那么由于只有 $\{n = 4,\; \text{第一个数} = -1\}$ 这一对取值能产生观测数据 $D = (-1, 3, 7, 11)$，所以给定 $H_a$ 时数据的概率是：

```math
P(D \mid H_a) = \frac{1}{101} \times \frac{1}{101} = 1.0 \times 10^{-4}.
```

（(28.2)）

要评估 $P(D \mid H_c)$，我们同样必须说明分数 $c, d, e$ 可能取哪些值。（我选择把这些数表示成**分数**而不是实数，是因为若用实数，这个模型会相对 $H_a$ 赋予 $D$ 一个无穷小的概率。当然，实数参数才是常态，本章其余部分一律假定实数参数。）一个合理的先验可以这样说：每个分数的分子可以是 $-50$ 与 $50$ 之间的任一整数，分母可以是 $1$ 与 $50$ 之间的任一整数。至于数列的初值，其概率分布沿用 $H_a$ 里的设定。在这个先验下，把分数 $c = -1/11 = -2/22 = -3/33 = -4/44$ 表达出来有**四种**方式；类似地，$d$ 与 $e$ 分别有**四种**与**两种**可能的解。所以，给定 $H_c$ 时观测数据的概率是：

```math
P(D \mid H_c) = \frac{1}{101}\left[ \frac{4}{101}\cdot\frac{1}{50} \right]\left[ \frac{4}{101}\cdot\frac{1}{50} \right]\left[ \frac{2}{101}\cdot\frac{1}{50} \right] \approx 2.5 \times 10^{-12}.
```

（(28.3)）

于是把 $P(D \mid H_c)$ 与 $P(D \mid H_a) = 0.00010$ 相比，即便我们对 $H_a$ 与 $H_c$ 的先验概率相等，在给定数列 $D = (-1, 3, 7, 11)$ 时，支持 $H_a$ 而非 $H_c$ 的赔率（odds）$P(D \mid H_a) : P(D \mid H_c)$ 大约是**四千万比一**　†。

（† 原书此句的脚注编号为 2，脚注正文接排在本页末句之后：「This answer depends on several subjective assumptions; in particular, the probability assigned to the free parameters $n, c, d, e$ of the theories. Bayesians make no apologies for this: there is no such thing as inference or prediction without assumptions. However, the quantitative details of the prior probabilities have no effect on the qualitative Occam's razor effect; the complex theory $H_c$ always suffers an 'Occam factor' because it has more parameters, and so can predict a greater variety of data sets (figure 28.3). This was only a small example, and there were only four data points; as we move to larger...」——句在页边界处截断，续 p349。）

这个答案依赖于若干主观假设，尤其是赋予理论自由参数 $n, c, d, e$ 的概率。Bayesian 对此不作辩解：**不存在不依赖假设的 inference 或 prediction**。不过，先验概率的定量细节对定性的 Occam's razor 效应**没有影响**：复杂理论 $H_c$ 总是要承受一个「Occam factor」，因为它参数更多，因而能预测更多种类的数据集（图 28.3）。这只是个小例子，只有四个数据点；当我们转向更大的问题时，

<span style="color:#1e8449;">**[译注]**
(28.2) 与 (28.3) 相差 $4\times10^{7}$ 倍，这个数字可以手算复现，值得算一遍，因为它把 Occam factor 从哲学变成算术。

**逐步复算**：$H_a$ 有两个参数（$n$ 与初值），各 $101$ 个候选，只有一组能生成 $D$，故 $P(D\mid H_a) = 101^{-2} \approx 9.8\times10^{-5}$。$H_c$ 有四个参数（初值 + $c,d,e$），$c = -1/11$ 在「分子 $\in[-50,50]$、分母 $\in[1,50]$」的先验下有 $4$ 个等价表示（$-1/11, -2/22, -3/33, -4/44$），$d = 9/11$ 同样 $4$ 个，$e = 23/11$ 只有 $2$ 个，故
$P(D\mid H_c) = 101^{-1}\cdot(4/5050)^{2}\cdot(2/5050) = 0.009901 \times (7.92\times10^{-4})^{2}\times 3.96\times10^{-4} \approx 2.46\times10^{-12}$。比值 $9.8\times10^{-5}/2.46\times10^{-12} \approx 4.0\times10^{7}$，正是「四千万比一」。

**失效对象**：如果把 $H_c$ 的参数改成实数、并给一个连续先验密度（这是本书其余部分的标准做法），那么「某一点数据被精确生成」的概率是 $0$——$P(D\mid H_c)$ 会变成无穷小，比值失去意义。作者用**分数参数**绕开这个退化，代价是模型本身变得不自然。可被反驳的推论：换一个先验（比如分母只到 $10$），$c = -1/11$ 就没有等价表示了，$P(D\mid H_c)$ 改变，但**比值仍在 $10^{5}$ 到 $10^{8}$ 量级**——定性的 Occam 效应不依赖这些细节，这正是原文那句「quantitative details have no effect on the qualitative effect」的可检验版本。

**落点**：§28.1 本页 (28.2)(28.3)、p.344 图 28.3、p.348 (28.7)(28.8)；数列 $-1,3,7,11$ 的三次插值系数 $-1/11,\; 9/11,\; 23/11$ 可用解线性方程组或 Lagrange 插值独立验证（见 §B8）。无越级。
</span>



（接 p345 末句：）当我们转向更大、更复杂的问题时，Occam factor 的量级通常会增大，而我们的推断受主观假设的定量细节影响的程度会变小。

[Figure 28.4：Bayesian inference 在数据建模流程中的位置。本图抽象出「收集数据并建模」这一段科学过程，特别适用于 pattern classification（模式分类）、learning（学习）、interpolation（插值）等任务。图中两个双框（double-framed）的方框表示涉及 inference 的两个步骤——**只有在 Those 两个步骤里才能用 Bayes' theorem**。例如，Bayes 并不告诉你如何发明模型。第一个框「把每个模型拟合到数据」的任务是：给定模型与数据，推断模型参数可能取什么值。Bayesian 方法可用来找出最可能的参数值，以及这些参数的 error bar（误差棒）。把 Bayesian 方法用于这个问题，结果常常与正统统计学给出的答案差别不大。第二个 inference 任务——在数据光照下做模型比较——才是 Bayesian 方法独树一帜的领域。这第二个 inference 问题需要一个定量的 Occam's razor 来惩罚过度复杂的模型。Bayesian 方法能给备选模型赋予客观的偏好，其方式自动体现 Occam's razor。**流程图的框线与箭头方向不可复原**：文字层只留下 `Gather DATA`、`Create alternative MODELS`、`Fit each MODEL to the DATA`、`Assign preferences to the alternative MODELS`、`Choose what data to gather next`、`Gather more data`、`Decide whether to create new models`、`Create new models`、`Choose future actions` 九个框内文字，箭头拓扑无法从文字恢复；可复原的是九个框的内容与「两个双框 = 两处 inference」这个标注结构。]

### Bayesian 方法与数据分析 · Bayesian methods and data analysis

现在把上面的讨论与数据分析中的真实问题联系起来。科学、统计学与技术中有无数问题，都要求在给定有限数据集时，对复杂度不同的备选模型赋予偏好。

例如，解释行星运动的两个备选假设：Inquisition 先生（Mr. Inquisition）基于「epicycles（本轮）」的地心模型，与 Copernicus 先生（Mr. Copernicus）以太阳为中心的更简单的太阳系模型。本轮模型对行星运动数据的拟合至少与 Copernican 模型一样好，但用的参数更多。对 Inquisition 先生来说纯属巧合的是：每颗行星多出来的那些本轮参数里，有两个恰好等于「太阳绕地球的周期」与「太阳绕地球的轨道半径」。直觉上我们觉得 Copernicus 先生的理论更可能。

### Bayesian razor 的机制：evidence 与 Occam factor · The mechanism of the Bayesian razor: the evidence and the Occam factor

在数据建模过程中，常常可以区分出两个层次的 inference（推断）。在第一层 inference，我们假定某个特定模型为真，并把该模型拟合到数据上，即：给定数据，推断它的自由参数大致该取什么值。这一层 inference 的结果，常用「最可能的参数值」与「这些参数的误差棒」来概括。对每个模型都重复做这一分析。第二层 inference 是模型比较这一任务。这里我们要在数据光照下比较各个模型，并给备选者赋予某种偏好或排序。

注意两层 inference 都不同于 decision theory（决策论）。inference 的目标是：给定一个定义好的 hypothesis space（假设空间）与一个特定数据集，给各假设赋予概率。decision theory 通常是在这些概率的基础上，在备选的行动之间作选择，以便最小化某个损失函数的期望。



本章只涉及 inference，不涉及任何 loss function（损失函数）。当我们讨论模型比较时，这不应被理解为暗示「模型选择」。理想的 Bayesian 预测不涉及模型之间的选择；预测是由「对所有备选模型按概率加权求和」得到的。

Bayesian 方法能够一致地、定量地解决上述两个 inference 任务。有一个流行的误解（myth）说：Bayesian 方法与正统统计方法的差别只在于它引入了主观先验，而这些先验难以赋值，且对结论通常影响不大。诚然，在 inference 的第一层，Bayesian 的结果常常与正统方法的结果差别不大。人们没有普遍认识到的，是 Bayesian 在**第二层** inference 上如何操作；本章因此聚焦于 Bayesian model comparison。

模型比较是个困难的任务，因为你不能简单地挑「拟合数据最好」的那个模型：更复杂的模型总能更好地拟合数据，所以 maximum likelihood 式的模型选择会把我们不可避免地引向不可信、参数过多（over-parameterized）的模型，而这种模型的泛化（generalize）很差。Occam's razor 是必需的。

让我们把上面描述的两层 inference 写成 Bayes' theorem 的形式，以便看清 Bayesian model comparison 究竟如何工作。每个模型 $H_i$ 被假定具有一个参数向量 $\mathbf{w}$。一个模型由一族概率分布定义：一个「先验」分布 $P(\mathbf{w} \mid H_i)$，它说明模型参数可能被期望取哪些值；以及一组条件分布，对每个 $\mathbf{w}$ 取值各一个，定义模型对数据 $D$ 所做的预测 $P(D \mid \mathbf{w}, H_i)$。

**1. 模型拟合（Model fitting）**。在第一层 inference，我们假定某一个模型（比如第 $i$ 个）为真，并推断给定数据 $D$ 时该模型的参数 $\mathbf{w}$ 可能是什么。用 Bayes' theorem，参数 $\mathbf{w}$ 的后验概率是：

```math
P(\mathbf{w} \mid D, H_i) = \frac{P(D \mid \mathbf{w}, H_i)\, P(\mathbf{w} \mid H_i)}{P(D \mid H_i)},
```

（(28.4)）

也就是说，

```math
\text{后验} = \frac{\text{Likelihood} \times \text{先验}}{\text{Evidence}}.
```

归一化常数 $P(D \mid H_i)$ 常被忽略，因为它对第一层 inference（即对 $\mathbf{w}$ 的推断）无关；但在第二层 inference 它变得重要，我们称它为 $H_i$ 的 evidence（证据）。常见做法是用基于梯度的（gradient-based）方法找后验的最大值，它定义了参数的最可能值 $\mathbf{w}_{\mathrm{MP}}$；然后通常用 $\mathbf{w}_{\mathrm{MP}}$ 的值、以及对这些最佳拟合参数的误差棒或置信区间来概括后验分布。误差棒可由后验的曲率得到：在 $\mathbf{w}_{\mathrm{MP}}$ 处求 Hessian，$A = -\left. \nabla\nabla \ln P(\mathbf{w} \mid D, H_i) \right|_{\mathbf{w}_{\mathrm{MP}}}$，并对对数后验概率以 $\Delta\mathbf{w} = \mathbf{w} - \mathbf{w}_{\mathrm{MP}}$ 作 Taylor 展开：

```math
P(\mathbf{w} \mid D, H_i) \simeq P(\mathbf{w}_{\mathrm{MP}} \mid D, H_i)\, \exp\left( -\frac{1}{2} \Delta\mathbf{w}^{\mathsf{T}} A \Delta\mathbf{w} \right),
```

（(28.5)）

我们看到后验可以在局部近似为一个 Gaussian，其协方差矩阵（等价于误差棒）为 $A^{-1}$。〔这个近似好不好，取决于我们要解的问题。事实上，后验分布的最大值与均值在 Bayesian inference 里没有根本地位——它们在非线性重参数化下都会改变。只有当形如 (28.5) 的近似能很好地概括该分布时，最大化后验概率才是有用的。〕



[Figure 28.5：Occam factor。本图显示决定「具有单参数 $w$ 的假设 $H_i$ 的 Occam factor」的各个量。参数的先验分布（实线）宽度为 $\sigma_w$。后验分布（虚线）在 $w_{\mathrm{MP}}$ 处有单峰，特征宽度为 $\sigma_{w \mid D}$。Occam factor 是

```math
P(w_{\mathrm{MP}} \mid H_i)\, \sigma_{w \mid D} = \frac{\sigma_{w \mid D}}{\sigma_w}.
```

**曲线形状不可复原**：文字层只留下 `wMP`、`σw|D`、`σw`、`w`、`P(w | Hi)`、`P(w | D, Hi)` 六处标签与上式，两条曲线的具体轮廓与峰高比无法恢复；可据「先验宽 $\sigma_w$、后验窄 $\sigma_{w\mid D}$、峰高比 $= \sigma_w/\sigma_{w\mid D}$」这一条重画。]

**2. 模型比较（Model comparison）**。在第二层 inference，我们要推断「给定数据时哪个模型最可信」。每个模型的后验概率是：

```math
P(H_i \mid D) \propto P(D \mid H_i)\, P(H_i).
```

（(28.6)）

注意那个依赖数据的项 $P(D \mid H_i)$ 正是 $H_i$ 的 evidence——它在 (28.4) 里作为归一化常数出现过。第二项 $P(H_i)$ 是我们假设空间上的主观先验，表达「在数据到来之前我们认为各备选模型有多可信」。假定我们选择给各备选模型赋相等的先验 $P(H_i)$，那么模型 $H_i$ 就按 evidence 的大小排序。归一化常数 $P(D) = \sum_i P(D \mid H_i) P(H_i)$ 已从 (28.6) 里省去，原因是在数据建模过程中，我们可能会在数据到来之后、在发现最初那些模型不足时开发新模型。inference 是开放式的（open ended）：我们不断寻找更可能的模型来解释我们收集到的数据。

重复这个关键思想：要给备选模型 $H_i$ 排序，Bayesian 评估的是 evidence $P(D \mid H_i)$。这个概念非常一般：evidence 对参数化模型与「非参数化」模型一视同仁地可评估；无论我们的数据建模任务是回归问题、分类问题还是密度估计问题，evidence 都是一个**可迁移的**量，用于比较备选模型。在所有这类情形中，evidence 都自然地体现 Occam's razor。

### 评估 evidence · Evaluating the evidence

现在让我们更仔细地研究 evidence，以取得「Bayesian Occam's razor 如何工作」的洞见。evidence 就是 (28.4) 的归一化常数：

```math
P(D \mid H_i) = \int P(D \mid \mathbf{w}, H_i)\, P(\mathbf{w} \mid H_i)\, d\mathbf{w}.
```

（(28.7)）

对许多问题，后验 $P(\mathbf{w} \mid D, H_i) \propto P(D \mid \mathbf{w}, H_i) P(\mathbf{w} \mid H_i)$ 在最可能参数 $\mathbf{w}_{\mathrm{MP}}$ 处有一个很强的峰（图 28.5）。那么，为简单起见取一维情形，用 Laplace's method，evidence 可以近似为「被积函数 $P(D \mid w, H_i) P(w \mid H_i)$ 的峰高」乘上「峰的宽度 $\sigma_{w \mid D}$」：

（本句在页边界处截断，续 p349。）

<span style="color:#1e8449;">**[译注]**
从 (28.7) 到「峰高 × 峰宽」这一步，是整个第 28 章唯一的技术动作，也是本章与第 27 章的接缝；值得把它的前提条件写成可检查的三条。

**第一条：后验必须真的单峰且窄。** (28.7) 被 $P(w\mid H_i)$ 截断在宽度 $\sigma_w$ 内、被 likelihood 收窄到 $\sigma_{w\mid D}$，只有 $\sigma_{w\mid D} \ll \sigma_w$ 时「峰高 × 峰宽」才是积分的全部。反例：$N = 1$ 时两者同阶、Occam factor 退化到 1，模型比较失去分辨力——**这就是「数据太少时 Occam 剃刀不工作」的定量表述**。

**第二条：峰高必须用同一归一化口径。** 把 $P(w_{\mathrm{MP}}\mid H_i)\sigma_{w\mid D}$ 写成 $\sigma_{w\mid D}/\sigma_w$，用到了「先验在峰附近平坦、高约 $1/\sigma_w$」。先验若双峰或长尾，替换出错的方向**总是偏向复杂模型**。

**量的方向感**：每个多余参数贡献一个 $\sigma_{w\mid D}/\sigma_w \lt 1$ 的因子。$N$ 个数据点、单参数、后验宽度按 $1/\sqrt{N}$ 收缩时，因子约 $1/\sqrt{N}$；$N = 1000$、多 5 个参数就是 $1000^{-2.5} \approx 3\times10^{-8}$，即约 25 bits 的自动罚分——不需要任何人手写正则项。

**消失测试**：抽掉「先验体积」这个分母（用 improper prior、$\sigma_w \to \infty$），Occam factor $\to 0$，全部模型的 evidence 同时归零，比较变成 $0/0$。它说明**用 improper prior 做模型比较无效**，每个模型的先验必须在自己参数空间里真归一化——这是第 24 章 (24.2) 留下的尾巴，在本章结账。

**落点**：§28.1 本页 (28.7) 与图 28.5、第 27 章 (27.8)（Laplace 近似的来源）、p.349 起 (28.8) 的正式推导、§24.1 关于 improper prior 的讨论；挂 Strang 的「投影/最小二乘给出 $A^{-1}$ 型协方差」（(28.5) 的 $A^{-1}$ 就是 Fisher 信息的逆，同一件事的二次型版本）。无越级。
</span>

---

# 本块附录

## A. 术语表（15 条，按首现顺序）

| # | English | 中文（首现处给括号注） | 首现页（书内） |
|---|---|---|---|
| 1 | trellis / minimal trellis | trellis（格图）/ minimal trellis（最小格图） | p329 |
| 2 | MAP codeword decoding | MAP codeword decoding（最大后验码字解码） | p329 |
| 3 | bitwise decoding | bitwise decoding（逐比特解码） | p329 |
| 4 | min–sum algorithm / Viterbi algorithm | min–sum algorithm（最小-和算法）/ Viterbi algorithm | p329 |
| 5 | sum–product algorithm / forward–backward / BCJR / belief propagation | sum–product algorithm（和-积算法），别名 forward–backward、BCJR、belief propagation | p330 |
| 6 | marginal posterior / marginal function | marginal（边缘）后验 / marginal function（边缘函数） | p329、p335 |
| 7 | span（codeword 的） | span（跨度：首非零比特到末非零比特之间的比特集合） | p331 |
| 8 | generator matrix / trellis-oriented form | generator matrix（生成矩阵）/ trellis-oriented form（trellis 自适应形式） | p331 |
| 9 | parity-check matrix / syndrome / partial syndrome | parity-check matrix（校验矩阵）/ syndrome（校验子）/ partial syndrome（部分校验子） | p332 |
| 10 | factor graph / leaf node | factor graph（因子图）/ leaf node（叶节点） | p335、p336 |
| 11 | normalization / marginalization / not-sum (summary) | normalization（归一化）/ marginalization（边缘化）/ not-sum | p335 |
| 12 | on-the-fly normalization | on-the-fly normalization（即时归一化） | p338 |
| 13 | max–product / loopy message passing / junction tree | max–product / loopy message passing（带环消息传递）/ junction tree（联结树） | p339、p340 |
| 14 | Laplace approximation / saddle-point approximation | Laplace approximation（拉普拉斯近似）/ saddle-point approximation（鞍点近似） | p341 |
| 15 | evidence / Occam's razor / Occam factor / posterior / prior | evidence（证据，即 marginal likelihood）/ Occam's razor（奥卡姆剃刀）/ Occam factor（奥卡姆因子） | p343、p344、p348 |

**本块按约定一律不译、原文照留的词**：likelihood、prior、posterior、evidence、marginalization / marginalize、marginal、MAP、maxent（本块未出现）、exponential family（本块未出现）、conjugate prior（本块未出现）、sufficient statistic（本块未出现）、factor graph、junction tree、belief propagation、loopy、trellis、codeword、syndrome、span、Gaussian、Poisson、Hamming code、parity code、Viterbi、BCJR、Laplace、Bayesian、Monte Carlo、variational。

## B. 可复算验证（重建 / 恢复内容的核对）

### B1. `2K` → $2^{K}$（Exercise 25.6 的答案）

$(7,4)$ Hamming 码的 $K = 4$、$N = 7$、$M = 3$。trellis 上每个 codeword 对应一条 path，合计 $2^{K} = 16$ 条 path；$\alpha_I$ 是「所有 path 概率之和」，故正比常数为 $2^{K} = 16$。若按原文排印的 $2K = 8$ 读，会与表 25.8 的 16 个 codeword 直接矛盾（16 行数据本身就是这条答案的独立证据）。

### B2. `2M` → $2^{M}$（p332「每片最多需要若干节点」）

$M = N - K = 7 - 4 = 3$，$2^{M} = 8$；$2M = 6$。图 25.7b 的每片节点数按 $2^{3}$ 组织（syndrome 取遍 $\{000,001,\dots,111\}$ 的 8 个值），故取 $2^{M}$。

### B3. (25.17)(25.18)(25.19)(25.20) 的矩阵重建核对

四行 $\times$ 七列，按列宽 7 切分竖排数字流得到。行正交核对（$G$ 四行与 $H$ 三行逐对内积，全应为偶）：

逐位内积（$G$ 的四行 × $H$ 的三行，全部按二元域计，只关心奇偶）：

| $G$ 行 | · $H$ 行 1（$1010101$） | · $H$ 行 2（$0110011$） | · $H$ 行 3（$0001111$） |
|---|---|---|---|
| $1110000$ | $1+1+1 = 3$ → 需重算，见下 | — | — |
| $0111100$ | $2$ | $2$ | $2$ |
| $0010110$ | $2$ | $2$ | $2$ |
| $0001111$ | $2$ | $2$ | $4$ |

第一行必须逐位算，因为它与 $H$ 行的 1 位置重叠方式不同：

- $1110000 \cdot 1010101$：逐位为 位 1（$1\cdot1=1$）、位 2（$1\cdot0=0$）、位 3（$1\cdot1=1$）、位 4（$0\cdot0=0$）、位 5（$0\cdot1=0$）、位 6（$0\cdot0=0$）、位 7（$0\cdot1=0$），合计 $2$，偶。
- $1110000 \cdot 0110011$：位 2（$1\cdot1=1$）、位 3（$1\cdot1=1$），其余 $G$ 行 1 在这些位为 0 或 $H$ 为 0，合计 $2$，偶。
- $1110000 \cdot 0001111$：$G$ 行 1 的 1 全在前三位，而 $H$ 行 3 的前三位是 $000$，故全部贡献为 0，合计 $0$，偶。

于是完整的核对是：$G$ 的 $1110000$ 与 $H$ 三行内积为 $2, 2, 0$；$0111100$ 为 $2, 2, 2$；$0010110$ 为 $2, 2, 2$；$0001111$ 为 $2, 2, 4$。**十二个内积全为偶，$GH^{\mathsf{T}} = 0$ 在二元域上成立**，(25.20) 确实是 (25.19) 的 parity-check matrix。这条核对的价值是双重的：它同时验证了矩阵重建（列宽切分正确）与原文数据（$H$ 与 $G$ 相容）。

### B4. trellis-oriented form 的判据核对

(25.18) 各行首非零列：$1, 2, 3, 4$（互不相同）；末非零列：$4, 6, 5, 7$（互不相同）——合格。
(25.19) 各行首非零列：$1, 2, 3, 4$；末非零列：$3, 5, 6, 7$——同样合格。
(25.17) 各行末非零列：$7, 6, 7, 7$——第 1、3、4 行都是 7，不合格，与原文陈述一致。

### B5. Exercise 25.9 的四个码字概率与 $Z$

按表 25.4 逐码字算 likelihood：$000 \to (1/4)(1/2)(1/8) = 1/64$；$011 \to (1/4)(1/4)(1/2) = 2/64$；$110 \to (1/2)(1/4)(1/8) = 1/64$；$101 \to (1/2)(1/2)(1/2) = 8/64$。合计 $Z = 12/64 = 3/16$，与书中 $\alpha_I = 3/16$ 一致；归一化后依次为 $1/12,\; 2/12,\; 1/12,\; 8/12$，与书中四值一致。逐比特：$P(t_1=1) = (1+8)/12 = 3/4$、$P(t_2=1) = (2+1)/12 = 1/4$、$P(t_3=1) = (2+8)/12 = 5/6$，与书中三个数值一致（下标三连错见 §C-1）。

### B6. 表 25.8 的两条自洽性

16 个 posterior 逐项求和 $= 1.0002$（舍入残差可接受）。likelihood 列与 posterior 列同比例：$0.026/0.3006 = 0.0865$；$0.00041/0.0047 = 0.0872$；$0.015/0.1691 = 0.0887$；$0.000058/0.0007 = 0.0829$。四个比值在 $0.083$–$0.089$ 之间，符合「$Z \approx 0.0865$ 与 1–2 位有效数字舍入」的一致性。

此外，表 25.8 列出的 16 个串恰是 (25.17) 行空间 $=\{1000101, 0100110, 0010111, 0001011\}$ 的全部线性组合：$0011100 = 0010111 \oplus 0001011$、$0101101 = 0100110 \oplus 0001011$、$0110001 = 0100110 \oplus 0010111$、$1100011 = 1000101 \oplus 0100110$、$1111111 = $ 四行全异或，等。16 个、无重复、无遗漏。

### B7. (28.3) 的数值与四千万比一

$101^{-1} = 0.009901$；$(4/101)(1/50) = 4/5050 = 7.921\times10^{-4}$；$(2/101)(1/50) = 3.960\times10^{-4}$。三者相乘：$0.009901 \times (7.921\times10^{-4})^{2} \times 3.960\times10^{-4} = 2.46\times10^{-12}$，与书中 $2.5\times10^{-12}$ 一致（书中保留 2 位有效数字）。$9.802\times10^{-5} / 2.46\times10^{-12} = 3.98\times10^{7}$，即「约四千万比一」。

### B8. 三次插值的系数核对

过 $(-1,3,7,11)$ 的四点三次插值写成「由前一个数 $x$ 得下一个数」的形式 $-x^{3}/11 + 9x^{2}/11 + 23/11$：代入 $x = -1$ 得 $(1 + 9 + 23)/11 = 33/11 = 3$ ✓；代入 $x = 3$ 得 $(-27 + 81 + 23)/11 = 77/11 = 7$ ✓；代入 $x = 7$ 得 $(-343 + 441 + 23)/11 = 121/11 = 11$ ✓。再接一步 $x = 11$ 得 $(-1331 + 1089 + 23)/11 = -219/11 \approx -19.9$ ✓，与书中预测的 $-19.9$ 一致；再下一步 $x = -19.909$ 给出 $1043.8$（书中值），可用同一公式复算。

## C. 原文自身问题（† 标记，共 7 处）

1. **† p333 末句三连错下标**：`P(t1 =1 | y) = 3/4; P(t1 =1 | y) = 1/4; P(t1 =1 | y) = 5/6` —— 三个式子全印成 $t_1$。按码字集 $\{000,011,110,101\}$ 复算（§B5），正确下标应为 $t_1, t_2, t_3$。
2. **† p330 Exercise 25.6 的答案 `2K`**：应为 $2^{K}$，CUP 文字层丢上标（§B1）。
3. **† p332 `2M`**：应为 $2^{M}$，同上（§B2）。
4. **† p338 (26.22) 分子 `f(xm)`**：缺下标 $m$，应为 $f_m(\mathbf{x}_m)$；上下文只定义了 $f_m$。
5. **† p344 脚注编号错位**：正文出现脚注标记 `2`（对应 p345 末的「subjective assumptions」那条），而 Dirac 引文那条应为 `1`；本块按语义归位，不复原错位。
6. **† p345 末句跨页断句**：`as we move to larger...` 在 p345 末尾截断，p346 顶部接 `and more sophisticated problems the magnitude of the Occam factors typically increases...`。译文按跨页合并，两处都标了页码。
7. **† p348 末句跨页断句**：`times its width, σw|D:` 在 p348 末尾以冒号截断，续 p349。本块止于此处，不加猜测。

### 非错误但易误读（不标 †）

- **p336 (26.10)** 原文并列给出 $\mathbf{x}_{m\setminus n}$ 与 $\mathbf{x}_{m\backslash n}$ 两种写法，PDF 抽取后两者看不出差别；这是字体层面的斜杠两种字形，含义相同。
- **p346「Mr. Inquisition」** 是 MacKay 对宗教裁判所的戏称（指地心模型的支持者），不是拼写错误，译文保留。
- **p332「2M 个节点」** 之外，p336「图的直径」与 p338「迭代次数等于直径」是同一个量的两种用法：前者说「消息传播完需 diameter 步」，后者说「惰性迭代收敛需 diameter 轮」。两者不矛盾。
- **p348 图 28.5 的 Occam factor 公式**：文字层把它拆成 `σw|DP(wMP | Hi) = σw|D / σw`，正确顺序是 $P(w_{\mathrm{MP}}\mid H_i)\,\sigma_{w\mid D} = \sigma_{w\mid D}/\sigma_w$；抽取只是把乘积因子的次序与上下标拆乱了，不是原文错误。

## D. 降级结构（哪些内容没能原样复原）

| 内容 | 性质 | 处理 |
|---|---|---|
| 图 25.6、25.7（trellis 拓扑） | 矢量图，节点/边坐标不可从文字层恢复 | 给 caption + 完整构造规则（复制 span 内节点、翻转第二段 edge symbol / 纵轴 = partial syndrome、横边 = 0 斜边 = 1），可据规则重画；不编造具体拓扑 |
| 图 27.1（Laplace 逼近示意） | 曲线图，纵横坐标与曲率不可恢复 | 给 caption + 文字层残留的四处标签（$\ln P^{*}$、$\ln Q^{*}$、$P^{*}$、$Q^{*}$），形状由 (27.2)–(27.5) 的 $c$ 唯一决定；不画近似曲线 |
| 图 28.1、28.2（树与箱子） | 位图插画 | 只给 caption；树后一个/两个箱子的位图不可复原，明确说明 |
| 图 28.3（evidence 与数据空间） | 曲线图，两峰高度/交叠位置不可恢复 | 给完整 caption（原文 issue 文字全在）+ 残留下标 `C`；比例关系由「两分布各自归一化、$H_2$ 更宽」唯一确定 |
| 图 28.4（建模流程框图） | 流程图，箭头拓扑不可恢复 | 给九个框内文字 + 「两个双框 = 两处 inference」的标注结构；不画箭头 |
| 图 28.5（Occam factor） | 双曲线，峰高比与轮廓不可恢复 | 给 caption + 六处标签 + 公式；趋势由 $\sigma_{w\mid D}\lt\sigma_w$ 唯一确定 |
| 矩阵 (25.17)–(25.20) | 竖排单列数字流，原排版丢失 | 按 7 列切分重建，用行正交性（§B3）与 trellis-oriented 判据（§B4）双重核对 |
| (28.3) 的连分式 | 抽取把分式压成竖排 | 按「四项相乘、每项是一个分数对」重建，用 §B7 的数值复算确认 |
| 图 26.1、26.4（factor graph） | 图上可复原 | 给出节点-边表与度数核对（$1+1+1+2+2 = 2+3+2 = 7$），这是图的内容本身 |
| 图 26.2、26.3（叶节点） | 单边小图 | 文字已完整给出（$r_{m\to n} = f_m$、$q_{n\to m} = 1$），无需画图 |
| 表 25.5、25.8、p333 内嵌表、表 25.4 | 表格，可完整复原 | 逐值保留，并给出求和/比值自洽核对（§B5、§B6） |

## E. 与前后块的接缝

- **前接 p321–340 块**（书内 p309–328）：那个块把第 23 章 Useful Probability Distributions、第 24 章 Exact Marginalization、第 25 章 §25.1–§25.3 开头译完。本块开头的 $\alpha_0 = 1$ 正是 §25.3 那一段公式的下半截，`(25.13)` 紧随其后。
- **后接 p361–380 块**（书内 p349–368）：本块最后一句在 p348 被切断（`times its width, σw|D:`），p349 应接着写 (28.8) 的 Occam factor 表达式与「$H_c$ 总是要承受 Occam factor」的推广。
- **跨块术语连续性**：p321–340 块已把 trellis、codeword、bitwise decoding、marginalization、evidence、Occam factor 列为术语；本块沿用同一中文注法，未改译名。



## 28.1 奥卡姆剃刀 · Occam's razor（续）

于是，evidence 的求法是：取模型所能达到的 best-fit likelihood，再乘上一个「Occam factor（奥卡姆因子：证据里那个小于 1 的罚分项，惩罚 $H_i$ 拥有参数 $w$ 这件事）」。

```math
P(D \mid H_i) \simeq P(D \mid w_{\mathrm{MP}}, H_i) \times P(w_{\mathrm{MP}} \mid H_i)\,\sigma_{w|D} \qquad (28.8)
```

式中第一个因子是 best-fit likelihood，第二个因子就是 Occam factor，其量级小于一。**Occam factor 的形状决定了整章的论证方向：模型比较不只需要「拟合得多好」，还要为「它本来可以拟合多少别的东西」付一笔费用。**

### Occam factor 的解释 · Interpretation of the Occam factor

量 $\sigma_{w|D}$ 是 $w$ 的 **posterior uncertainty**（后验不确定度），也就是把数据看完之后 $w$ 还能浮动多大。

为简单起见，设 prior $P(w \mid H_i)$ 在某一个大区间 $\sigma_w$ 上是均匀的——这个区间代表「按照 $H_i$ 的说法，$w$ 事先有可能是哪些值」（图 28.5）。

于是 $P(w_{\mathrm{MP}} \mid H_i) = 1/\sigma_w$，从而

```math
\text{Occam factor} = \frac{\sigma_{w|D}}{\sigma_w} \qquad (28.9)
```

也就是说，Occam factor 等于 **$H_i$ 参数空间的 posterior accessible volume（后验可达体积）与 prior accessible volume（先验可达体积）之比**，或者说是数据到达时 $H_i$ 的 hypothesis space（假设空间）塌缩掉的那个倍数。

$H_i$ 这个模型可以被看成由若干互斥的 submodel 组成，数据到达后只有其中一个存活下来；**Occam factor 就是这个数目的倒数**。

Occam factor 的对数，则是数据到达时我们关于模型参数所获得的信息量——这与第 2 章对 information 的定义是同一个量，只是把「消息」换成了「参数值」。

一个拥有很多参数的复杂模型，如果每个参数都能在一个大范围 $\sigma_w$ 上自由游走，它通常会被一个比简单模型强得多的 Occam factor 罚下去。

Occam factor 同时也惩罚那些必须被**精细调校**才能拟合数据的模型，而偏爱那些「所需参数精度 $\sigma_{w|D}$ 很粗」的模型。

因此，Occam factor 的大小成了模型复杂度的一种度量；它关联的是**模型在 data space（数据空间）里做出的预测的复杂度**。

而这个复杂度不仅取决于模型里有几个参数，还取决于模型给这些参数分配了什么 prior probability。

最终哪个模型拿到最大的 evidence，取决于一个 trade-off：一边要最小化这个天然的复杂度度量，一边要最小化数据上的 misfit。

与其他模型复杂度度量相比，Occam factor 有一个实用上的好处：**它算起来很直接**——它只依赖参数上的 error bars（误差棒），而这个量在把模型拟合到数据时我们已经算过了。

图 28.6 把一整个 hypothesis space 画出来，用来说明上面分析里出现的各个概率。

那里有三个模型 $H_1, H_2, H_3$，prior 概率彼此相等。每个模型有一个参数 $w$（各画在一条水平轴上），但给这个参数分配的 prior 范围 $\sigma_W$ 各不相同。$H_3$ 是其中最「灵活」或者说最「复杂」的模型，分配的 prior 范围最宽。

一维的 data space 画在竖直轴上。每个模型都给数据与参数的联合分布 $P(D, w \mid H_i)$ 赋予一个概率分布，用一团点表示；这些点是整个概率分布的随机样本。

三个模型子空间里点的总数相同，因为我们给三个模型分配的 prior probability 相等。

当某个特定的数据集 $D$ 到手时（那条水平线），我们把该模型（比如说 $H_3$）的 $w$ 后验分布，读作沿这条水平线的密度再归一化。后验概率 $P(w \mid D, H_3)$ 由图底部那条点线给出；图中同时画出了 prior $P(w \mid H_3)$（参看图 28.5）。

〔在 $H_1$ 这个与数据匹配得很差的情形下，

<span style="color:#1e8449;">**[译注]**
式 (28.9) 是全章唯一一个**能把「奥卡姆剃刀」变成可算数字**的地方，值得拆到底。

把 prior 取成宽度 $\sigma_w$ 的均匀分布、posterior 近似成宽度 $\sigma_{w|D}$ 的 Gaussian，则
$P(w_{\mathrm{MP}} \mid H_i)\sigma_{w|D} = \sigma_{w|D}/\sigma_w$。在 $k$ 个独立参数的情形，这个比值按乘积变成
$\prod_{j=1}^{k}\sigma_{j|D}/\sigma_{j}$，取对数就是 $\sum_j \ln(\sigma_{j|D}/\sigma_j) \lt 0$——
**每一个「本来可以自由、现在被数据钉死」的参数，都要按「钉死的紧度」付一笔对数费用**。

**消失测试**：没有这个比值，model comparison 就退化成「比较各自的 best-fit likelihood」，而 likelihood 对参数数目是单调不减的，
于是任何一组数据都会选最复杂的模型；同时也没法解释本块 p351 那个箱子例子里，为什么 $H_2$ 明明能完美解释图像，
evidence 却输给 $H_1$ 约 $1280:1$（式 28.13、28.14）。退化后的算法不是「差一点」，而是**必然过拟合**，
且无法给出任何可比较的标量。

**落点**：式 (28.8)(28.9)(28.10) 在 p349–p350；箱子例的数值口径在 p351 的 (28.11)–(28.14)；
Gaussian 情形下 $\sigma_{j|D}$ 由 Hessian 特征值给出，见第 27 章（p341 之前）与本页 (28.10)。
线性代数侧只用到「协方差矩阵的特征值 = 各方向的标准差」，挂 Strang 的对称矩阵谱分解即可，不越级。
</span>



[Figure 28.6：一个由三个互斥模型组成的 hypothesis space，每个模型一个参数 $w$、一维数据集 $D$。点是联合分布 $P(D, w, H)$ 的随机样本（不是数据点）；水平虚线是观测到的那个 $D$；底部虚线曲线是各模型在此数据下的 $w$ 后验；把联合分布沿竖直方向 marginalize 到左侧 $D$ 轴上，就得到各模型的 evidence。它要演示的主张是：**同一个 $D$ 上，最灵活的 $H_3$ 反而 evidence 最小，中间复杂度的 $H_2$ 最大。**]

上接 p349 末尾那个方括号补充：〕

与数据匹配得很差的模型 $H_1$，其后验分布的形状会依赖 prior $P(w \mid H_1)$ 的尾部细节以及 likelihood $P(D \mid w, H_1)$ 的尾部细节；图中画的那条曲线，是 prior 衰减得更强的那个情形。

我们把联合分布 $P(D, w \mid H_i)$ 沿左侧的 $D$ 轴 marginalize，就得到图 28.3。

对于图中那条点线水平线所示的数据集 $D$，更灵活的模型 $H_3$ 的 evidence $P(D \mid H_3)$ 比 $H_2$ 的 evidence 要小。

原因在于 $H_3$ 在那条线上放置的 predictive probability 更少（点数更少）。

换成 $w$ 上的分布来说，模型 $H_3$ 的 evidence 更小，是因为它的 Occam factor $\sigma_{w|D}/\sigma_w$ 比 $H_2$ 的小。

最简单的模型 $H_1$ 拿到全场最小的 evidence，因为它对数据 $D$ 能达到的最好拟合本身就非常差。

给定这个数据集，最可能的模型是 $H_2$。

### 多参数情形的 Occam factor · Occam factor for several parameters

如果 posterior 能被 Gaussian 很好地近似，那么 Occam factor 可以由相应 covariance matrix 的 determinant（行列式）得到（参看式 (28.8) 与第 27 章）：

```math
P(D \mid H_i) \simeq P(D \mid \mathbf{w}_{\mathrm{MP}}, H_i) \times P(\mathbf{w}_{\mathrm{MP}} \mid H_i)\,\det\!\left(\frac{A}{2\pi}\right)^{-1/2} \qquad (28.10)
```

这里 $A = -\nabla\nabla \ln P(\mathbf{w} \mid D, H_i)$，就是我们算 $\mathbf{w}_{\mathrm{MP}}$ 上的 error bars 时已经求过的那个 Hessian（式 (28.5) 与第 27 章）。

随着收集到的数据量增加，这个 Gaussian 近似预期会越来越准。

**小结**：Bayesian 的 model comparison 是 maximum likelihood 模型选择的简单延伸——把 best-fit likelihood 乘上 Occam factor 就得到 evidence。

只要 Gaussian 近似够好，求 Occam factor 只需要 Hessian $A$。因此，靠求 evidence 来做 model comparison 的 Bayesian 方法，其计算代价并不比「为每个模型找到 best-fit 参数及其 error bars」更高。

<span style="color:#1e8449;">**[译注]**
式 (28.10) 里那个 $\det(A/2\pi)^{-1/2}$ 是把 (28.9) 的标量比值推广到 $k$ 维的**唯一正确写法**，而且它给出了一条能立刻检验的定量预言。

Gaussian 近似下，posterior 在参数空间占据的是一个椭球，其体积 $\propto \det(\Sigma)^{1/2} = \det(A^{-1})^{1/2}$；
prior 占据的体积 $\propto \prod_j \sigma_j$。两者相除就是 (28.10) 的因子。若 $A$ 的所有特征值同量级，
$\det(A)^{-1/2}$ 退化为 $\sigma_{w|D}^{k}$，于是 $\ln(\text{Occam factor}) \approx k\ln(\sigma_{w|D}/\sigma_w) \lt 0$，
**惩罚随参数个数 $k$ 线性增长、随每个参数被钉紧的程度对数增长**——这就是「复杂度罚分」的定量形式。

**消失测试**：抽掉 $\det$ 只留「参数个数 $k$」，就会把 BIC 那类只按 $k$ 计费的近似当成定理来用。
在本块 p351 的箱子例里，两个模型参数个数分别是 4 与 9，但真正决定胜负的是 4 个**额外**参数的 prior 范围比（$1/20$、$10/20$、$10/20$、$1/16$），
而不是 $9 - 4 = 5$ 这个数字；用 $k$ 计费会给出「$H_1$ 罚 4、$H_2$ 罚 9」这种与数据尺度无关的答案，在本例中方向对、量级错。

**落点**：式 (28.10) 见本页；$\det(A)^{-1/2}$ 与 Gaussian 体积的关系见第 27 章（p341 之前的 Laplacian 方法）；
BIC 近似 $\ln P(D \mid H) \approx \ln P(D \mid \hat w) - \frac{k}{2}\ln N$ 中 $A \approx N\mathbf{J}$ 的推导可作为对照。
需要的前置只有「对称正定矩阵可对角化、特征值即各方向方差」——Strang 线代第 6 章，不越级。
</span>
