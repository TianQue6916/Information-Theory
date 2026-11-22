# MacKay《Information Theory, Inference, and Learning Algorithms》Ch.02 习题解答（第 1 部分）双语译注

## Exercise 2.2（習題 2.2）　[1, p.40]

**题干原文：** Are the random variables X and Y in the joint ensemble of figure 2.2 independent?

**中文：** 图 2.2 中的联合系综（joint ensemble）里，随机变量（random variables）X 与 Y 是否独立（independent）？

**解答：**

先写出图 2.2 的联合概率表（joint probability table）`P(x, y)`，其中 `x ∈ {a, b, c, d}`，`y ∈ {α, β, γ, δ}`：

| P(x,y) | x = a | x = b | x = c | x = d |
|:--:|:--:|:--:|:--:|:--:|
| y = α | 1/8 | 1/16 | 1/32 | 1/32 |
| y = β | 1/16 | 1/8 | 1/32 | 1/32 |
| y = γ | 1/16 | 1/16 | 1/16 | 1/16 |
| y = δ | 1/4 | 0 | 0 | 0 |

独立性的定义（式 2.11）是：

```math
P(x, y) = P(x)P(y) \quad \text{对所有 } x, y
```

因此只需找出一组 `(x, y)` 使得上式不成立，即可判定不独立。为此先算出边际分布（marginal distribution）。

**对 `x` 求和得到 `P(y)`：**

```math
\begin{aligned}
P(y=\alpha) &= \frac{1}{8}+\frac{1}{16}+\frac{1}{32}+\frac{1}{32} = \frac{4+2+1+1}{32} = \frac{8}{32} = \frac{1}{4},\\[2pt]
P(y=\beta)  &= \frac{1}{16}+\frac{1}{8}+\frac{1}{32}+\frac{1}{32} = \frac{2+4+1+1}{32} = \frac{8}{32} = \frac{1}{4},\\[2pt]
P(y=\gamma) &= \frac{1}{16}+\frac{1}{16}+\frac{1}{16}+\frac{1}{16} = \frac{4}{16} = \frac{1}{4},\\[2pt]
P(y=\delta) &= \frac{1}{4}+0+0+0 = \frac{1}{4}.
\end{aligned}
```

**对 `y` 求和得到 `P(x)`：**

```math
\begin{aligned}
P(x=a) &= \frac{1}{8}+\frac{1}{16}+\frac{1}{16}+\frac{1}{4} = \frac{2+1+1+4}{16} = \frac{8}{16} = \frac{1}{2},\\[2pt]
P(x=b) &= \frac{1}{16}+\frac{1}{8}+\frac{1}{16}+0 = \frac{1+2+1}{16} = \frac{4}{16} = \frac{1}{4},\\[2pt]
P(x=c) &= \frac{1}{32}+\frac{1}{32}+\frac{1}{16}+0 = \frac{1+1+2}{32} = \frac{4}{32} = \frac{1}{8},\\[2pt]
P(x=d) &= \frac{1}{32}+\frac{1}{32}+\frac{1}{16}+0 = \frac{1+1+2}{32} = \frac{4}{32} = \frac{1}{8}.
\end{aligned}
```

现在任取一项验证乘积关系。例如 `x = d, y = δ`：

```math
P(x=d, y=\delta) = 0, \qquad P(x=d)\,P(y=\delta) = \frac{1}{8}\times\frac{1}{4} = \frac{1}{32} \neq 0.
```

于是

```math
P(x=d, y=\delta) \neq P(x=d)\,P(y=\delta).
```

因为独立性要求**所有** `x, y` 都满足 `P(x,y)=P(x)P(y)`，只要存在一组不成立，X 与 Y 就不独立。

**结论：X 与 Y 不独立（not independent）。**

> <span style="color:#1e8449;">**[note] 判定独立性的判据：**</span> 只需找一组反例即可否定独立，无需逐项验证全部 `4×4=16` 项；但若要「证明独立」则必须验证所有组合。这里的联合表有强关联（例如 `y=δ` 时 `x` 只能是 `a`），属于典型的不独立结构。

---

_说明：题干引用的图 2.2 数据未包含在本段原文中，联合概率表按 MacKay 原书图 2.2 的标准内容补全（x ∈ {a,b,c,d}，y ∈ {α,β,γ,δ}），用于完成独立性判定。若你的版本图 2.2 数值不同，替换表格即可复用同样的判定流程。_
# MacKay《Information Theory, Inference, and Learning Algorithms》Ch.02 习题解答（第 2 部分）双语译注

## Exercise 2.8（習題 2.8）　[2, p.43]

**题干原文：** Assuming a uniform prior on $f_H$, $P(f_H)=1$, solve the problem posed in example 2.7 (p.30). Sketch the posterior distribution of $f_H$ and compute the probability that the $N+1$th outcome will be a head, for
(a) $N=3$ and $n_H=0$;
(b) $N=3$ and $n_H=2$;
(c) $N=10$ and $n_H=3$;
(d) $N=300$ and $n_H=29$.
You will find the beta integral useful:

```math
\int_0^1 dp_a \; p_a^{\,F_a}(1-p_a)^{\,F_b}
= \frac{\Gamma(F_a+1)\,\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}
= \frac{F_a!\,F_b!}{(F_a+F_b+1)!}.
\tag{2.32}
```

**中文：** 假设对 $f_H$ 取均匀先验（uniform prior）$P(f_H)=1$，解出例题 2.7（example 2.7，p.30）所提出的问题。画出 $f_H$ 的后验分布（posterior distribution）草图，并计算第 $N+1$ 次结果为正面的概率，分别对
(a) $N=3$、$n_H=0$；
(b) $N=3$、$n_H=2$；
(c) $N=10$、$n_H=3$；
(d) $N=300$、$n_H=29$。
你会发现以下贝塔积分（beta integral）很有用：

```math
\int_0^1 dp_a \; p_a^{\,F_a}(1-p_a)^{\,F_b}
= \frac{\Gamma(F_a+1)\,\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}
= \frac{F_a!\,F_b!}{(F_a+F_b+1)!}.
\tag{2.32}
```

**解答：**

**设定回顾（例题 2.7）。** 一枚硬币抛 $N$ 次，观察到 $n_H$ 个正面（head），$N-n_H$ 个反面（tail）。未知参数 $f_H$ 表示下一次抛掷出现正面的真实概率。在均匀先验 $P(f_H)=1$（$f_H\in[0,1]$）之下，由贝叶斯定理（Bayes' theorem）得后验密度正比于似然（likelihood）：

```math
P(f_H \mid n_H, N) \;\propto\; P(n_H \mid f_H, N)\,P(f_H)
= f_H^{\,n_H}\,(1-f_H)^{\,N-n_H}\times 1
= f_H^{\,n_H}\,(1-f_H)^{\,N-n_H}.
```

**第 1 步：归一化常数（normalization constant）。** 令

```math
Z = \int_0^1 f_H^{\,n_H}(1-f_H)^{\,N-n_H}\,df_H .
```

套用贝塔积分（式 2.32），取 $p_a=f_H$、$F_a=n_H$、$F_b=N-n_H$：

```math
Z = \frac{n_H!\,(N-n_H)!}{(n_H+N-n_H+1)!}
= \frac{n_H!\,(N-n_H)!}{(N+1)!}.
```

于是归一化的后验是一个贝塔分布（Beta distribution）：

```math
P(f_H \mid n_H, N)
= \frac{(N+1)!}{n_H!\,(N-n_H)!}\,
  f_H^{\,n_H}(1-f_H)^{\,N-n_H}
= \mathrm{Beta}\bigl(f_H;\, n_H+1,\; N-n_H+1\bigr).
```

**第 2 步：第 $N+1$ 次的预测概率（predictive probability）。** 由全概率公式，第 $N+1$ 次为正面的概率是对 $f_H$ 求期望：

```math
\begin{aligned}
P(x_{N+1}=\text{head}\mid n_H, N)
&= \int_0^1 P(x_{N+1}=\text{head}\mid f_H)\, P(f_H \mid n_H, N)\, df_H \\[2pt]
&= \int_0^1 f_H \cdot \frac{(N+1)!}{n_H!\,(N-n_H)!}\,
   f_H^{\,n_H}(1-f_H)^{\,N-n_H}\, df_H \\[2pt]
&= \frac{(N+1)!}{n_H!\,(N-n_H)!}
   \int_0^1 f_H^{\,n_H+1}(1-f_H)^{\,N-n_H}\, df_H .
\end{aligned}
```

再次套用式 2.32，取 $F_a=n_H+1$、$F_b=N-n_H$：

```math
\int_0^1 f_H^{\,n_H+1}(1-f_H)^{\,N-n_H}\, df_H
= \frac{(n_H+1)!\,(N-n_H)!}{(n_H+1+N-n_H+1)!}
= \frac{(n_H+1)!\,(N-n_H)!}{(N+2)!}.
```

代入得

```math
P(x_{N+1}=\text{head}\mid n_H, N)
= \frac{(N+1)!}{n_H!\,(N-n_H)!}
  \cdot \frac{(n_H+1)!\,(N-n_H)!}{(N+2)!}
= \frac{n_H+1}{N+2}.
```

这就是均匀先验下的**拉普拉斯平滑规则（Laplace's rule of succession）**：预测概率等于后验均值 $\mathbb{E}[f_H]$。注意它只依赖 $n_H$ 与 $N$，与先验的整个形状（此处为均匀）通过贝塔积分共同决定。

**第 3 步：逐小题计算。**

**(a) $N=3,\ n_H=0$**

```math
P(x_{4}=\text{head}) = \frac{0+1}{3+2} = \frac{1}{5} = 0.2.
```

后验为 $\mathrm{Beta}(1,4)$，密度 $P(f_H)\propto (1-f_H)^3$，在 $f_H=0$ 处取最大值并单调下降：三次全是反面，使我们对「$f_H$ 很小」的信念最强。

**(b) $N=3,\ n_H=2$**

```math
P(x_{4}=\text{head}) = \frac{2+1}{3+2} = \frac{3}{5} = 0.6.
```

后验为 $\mathrm{Beta}(3,2)$，众数（mode）在 $\dfrac{a-1}{a+b-2}=\dfrac{3-1}{3+2-2}=\dfrac{2}{3}\approx0.667$，即对「$f_H$ 偏大」给出较高的信念。

**(c) $N=10,\ n_H=3$**

```math
P(x_{11}=\text{head}) = \frac{3+1}{10+2} = \frac{4}{12} = \frac{1}{3}\approx0.333.
```

后验为 $\mathrm{Beta}(4,8)$，众数在 $\dfrac{4-1}{4+8-2}=\dfrac{3}{10}=0.3$，均值在 $\dfrac{4}{4+8}=\dfrac{1}{3}\approx0.333$。

**(d) $N=300,\ n_H=29$**

```math
P(x_{301}=\text{head}) = \frac{29+1}{300+2} = \frac{30}{302} = \frac{15}{151}\approx0.0993.
```

后验为 $\mathrm{Beta}(30,272)$，众数在 $\dfrac{30-1}{30+272-2}=\dfrac{29}{300}\approx0.0967$，均值在 $\dfrac{30}{302}\approx0.0993$。数据量增大后，后验高度集中在观测频率 $\tfrac{29}{300}\approx0.0967$ 附近。

**第 4 步：后验分布草图（sketch）。** 下表给出四种情形下后验贝塔分布的参数与关键统计量，形状据此可画出：

| 情形 | $N$ | $n_H$ | 后验分布 | 众数 mode | 均值 mean | 预测概率 $P(\text{head})$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| (a) | 3 | 0 | $\mathrm{Beta}(1,4)$ | $0$ | $0.2$ | $0.2$ |
| (b) | 3 | 2 | $\mathrm{Beta}(3,2)$ | $0.667$ | $0.6$ | $0.6$ |
| (c) | 10 | 3 | $\mathrm{Beta}(4,8)$ | $0.3$ | $0.333$ | $0.333$ |
| (d) | 300 | 29 | $\mathrm{Beta}(30,272)$ | $0.0967$ | $0.0993$ | $0.0993$ |

形状特点：(a) 单调递减（众数在端点 0）；(b) 单峰、峰值偏向 $f_H$ 较大一侧；(c)、(d) 均为单峰，且随 $N$ 增大，峰越来越窄、越来越贴近观测频率 $n_H/N$。预测概率在数值上恒等于后验均值，因为 $P(x_{N+1}=\text{head}\mid f_H)=f_H$，对其取后验期望即得 $\mathbb{E}[f_H]$。

> <span style="color:#1e8449;">**[note] 拉普拉斯平滑的直观含义：**</span> 均匀先验等价于「预先假想」了 1 个正面与 1 个反面（先验 $\mathrm{Beta}(1,1)$），故预测概率为 $\dfrac{n_H+1}{N+2}$，而非频率派的 $\dfrac{n_H}{N}$。当 $N\to\infty$ 时两者趋于一致，但有限样本下贝叶斯方法因先验信息而对极端频率（如 (a) 中 $0/3$）给出非零的平滑估计，避免了「三次全反面就断言 $f_H=0$」的过度自信。这正是例题 2.6（p.27，瓮中摸球）与式 2.31 所强调的逆概率（inverse probability）思想：先验是 $f_H$ 上的完整概率密度，而非对 $f_H$ 值的单一猜测，后续预测依赖整个先验而非仅其均值（见式 2.33 之后的讨论）。
