# MacKay《Information Theory, Inference, and Learning Algorithms》Ch.03 习题解答（双语译注）

## Exercise 3.5（習題 3.5）　[2, p.59]

**題幹原文：** Sketch the posterior probability $P(p_a \mid s = aba, F = 3)$. What is the most probable value of $p_a$ (i.e., the value that maximizes the posterior probability density)? What is the mean value of $p_a$ under this distribution? Answer the same questions for the posterior probability $P(p_a \mid s = bbb, F = 3)$.

**中文：** 画出后验概率（posterior probability）$P(p_a \mid s = aba, F = 3)$ 的草图。$p_a$ 的最可能取值（即令后验概率密度取最大值的那个值）是多少？在该分布下 $p_a$ 的均值（mean）是多少？再对后验概率 $P(p_a \mid s = bbb, F = 3)$ 回答同样的问题。

**解答：**

本章研究的是「抛一枚可能偏斜的硬币（bent coin）」的问题：硬币以概率 $p_a$ 正面朝上（记作字符 $a$），以概率 $1-p_a$ 反面朝上（记作字符 $b$）。模型 $H_1$ 假设 $p_a$ 未知，且先验取均匀分布 $P(p_a \mid H_1) = 1$（$0 \le p_a \le 1$，见式 (3.9)）。观测到长度为 $F$、含 $F_a$ 个 $a$、$F_b$ 个 $b$ 的字符串 $s$ 后，由式 (3.11) 与 (3.12)，$p_a$ 的后验为

```math
P(p_a \mid s, F, H_1)
= \frac{p_a^{F_a} (1-p_a)^{F_b}}{P(s \mid F, H_1)},
\qquad
P(s \mid F, H_1) = \frac{F_a!\, F_b!}{(F_a + F_b + 1)!}.
```

这是一个 Beta 分布（beta distribution）$\mathrm{Beta}(F_a+1,\; F_b+1)$。下面分别计算两种情况。

**情形一：$s = aba$，$F=3$。** 计数为 $F_a = 2$，$F_b = 1$，故归一化常数为

```math
P(s \mid F=3, H_1) = \frac{2!\, 1!}{3!} = \frac{2}{6} = \frac{1}{3}.
```

后验概率密度为

```math
P(p_a \mid s=aba, F=3)
= \frac{p_a^2 (1-p_a)}{1/3}
= 3\, p_a^2 (1-p_a),
\qquad 0 \le p_a \le 1.
```

这是 $\mathrm{Beta}(3, 2)$ 分布，其草图是单峰的曲线：在 $p_a=0$ 与 $p_a=1$ 两端取值均为 $0$，中间隆起，偏向 $p_a$ 较大的一侧。

**最可能取值**：令密度对 $p_a$ 求导为零。由于对数单调，等价地令 $\ln P \propto 2\ln p_a + \ln(1-p_a)$ 的导数为零：

```math
\frac{d}{dp_a}\big[2\ln p_a + \ln(1-p_a)\big]
= \frac{2}{p_a} - \frac{1}{1-p_a} = 0
\quad\Longrightarrow\quad 2(1-p_a) = p_a
\quad\Longrightarrow\quad p_a = \frac{2}{3}.
```

所以最可能取值（众数，mode）是 $p_a = \dfrac{2}{3}$。

**均值**：Beta 分布 $\mathrm{Beta}(\alpha,\beta)$ 的均值为 $\dfrac{\alpha}{\alpha+\beta}$，此处 $\alpha = F_a+1 = 3$，$\beta = F_b+1 = 2$，故

```math
\mathbb{E}[p_a] = \frac{F_a+1}{F_a+F_b+2} = \frac{3}{5}.
```

（也可直接积分验证：$\mathbb{E}[p_a] = \int_0^1 p_a \cdot 3 p_a^2 (1-p_a)\, dp_a = 3\int_0^1 (p_a^3 - p_a^4)\,dp_a = 3\left(\tfrac14 - \tfrac15\right) = \tfrac35$。）

**情形二：$s = bbb$，$F=3$。** 计数为 $F_a = 0$，$F_b = 3$，归一化常数为

```math
P(s \mid F=3, H_1) = \frac{0!\, 3!}{3!} = 1.
```

后验概率密度为

```math
P(p_a \mid s=bbb, F=3)
= p_a^0 (1-p_a)^3
= (1-p_a)^3,
\qquad 0 \le p_a \le 1.
```

这是 $\mathrm{Beta}(1, 4)$ 分布，其草图是单调下降的曲线：在 $p_a = 0$ 处取最大值 $1$，随后随 $p_a$ 增大而递减到 $p_a=1$ 处为 $0$。

**最可能取值**：密度 $(1-p_a)^3$ 在区间 $[0,1]$ 上单调递减，故最大值在左端点 $p_a = 0$ 处取得（导数 $\dfrac{d}{dp_a}(1-p_a)^3 = -3(1-p_a)^2 \le 0$，除端点外恒为负，无内部驻点）。所以最可能取值（众数）是 $p_a = 0$。

**均值**：$\mathrm{Beta}(1,4)$ 的均值为 $\dfrac{1}{1+4} = \dfrac15$：

```math
\mathbb{E}[p_a] = \frac{F_a+1}{F_a+F_b+2} = \frac{0+1}{0+3+2} = \frac{1}{5}.
```

（直接积分：$\mathbb{E}[p_a] = \int_0^1 p_a (1-p_a)^3\, dp_a = \int_0^1 (p_a - 3p_a^2 + 3p_a^3 - p_a^4)\,dp_a = \tfrac12 - 1 + \tfrac34 - \tfrac15 = \tfrac15$。）

> <span style="color:#1e8449;">**[note] 众数与均值为何不同：**</span> 后验概率密度不是对称的（除非 $F_a = F_b$），因此「最可能取值」（众数，使密度最大的点）与「均值」（按密度加权平均）一般不等。对 $s=aba$：众数 $2/3$，均值 $3/5 = 0.6$，均值被 $p_a$ 较小一侧的「尾巴」拉低了。对 $s=bbb$：密度单调递减，众数在边界 $p_a=0$，但均值 $1/5$ 反映了「$p_a$ 仍可能有小概率为正值」的尾部贡献。这一点正对应正文式 (3.16) 的 Laplace 规则：用后验均值 $\dfrac{F_a+1}{F_a+F_b+2}$ 做预测（而不是用众数 $F_a/(F_a+F_b)$），正是为了避免在零计数时（如 $s=bbb$）给出 $p_a=0$ 的「过度自信」预测。

