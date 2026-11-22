# MacKay《Information Theory, Inference, and Learning Algorithms》Ch.01 习题解答（双语译注）

## Exercise 1.2（習題 1.2）　[2, p.16]

**題幹原文：** Show that the error probability is reduced by the use of $R_3$ by computing the error probability of this code for a binary symmetric channel with noise level $f$.

**中文：** 通过计算该编码在噪声水平（noise level）为 $f$ 的二元对称信道（binary symmetric channel, BSC）上的差错概率，说明使用重复码 $R_3$ 之后差错概率得到了降低。

**解答：**

设信源比特（source bit）$s \in \{0,1\}$，用重复码 $R_3$ 编成三个相同比特 $t = (s,s,s)$，经 BSC 传输后接收 $r$，译码规则为多数判决（majority vote）。单个比特被信道翻转的概率为 $f$，且各比特独立。

译码出错的充要条件是：三个比特中至少有两个被翻转（即翻转数 $\ge 2$）。因此每位解码后的差错概率（probability of decoded bit error）为

```math
p_b = P(\text{翻转 2 个}) + P(\text{翻转 3 个})
= \binom{3}{2} f^2 (1-f)^{1} + \binom{3}{3} f^3
= 3 f^2 (1-f) + f^3.
```

代入 $f = 0.1$：

```math
p_b = 3 \times 0.1^2 \times 0.9 + 0.1^3 = 0.027 + 0.001 = 0.028 \simeq 0.03 .
```

而不用编码（$R_1$，即直接传输单个比特）时，差错概率就是 $p_b = f = 0.1$。可见 $R_3$ 把每位差错概率从 $0.1$ 降到了约 $0.03$，误差概率确被降低。

> <span style="color:#1e8449;">**[note] 差错概率由 $f^2$ 量级主导：**</span> 译码出错要求一个三比特块中至少两个比特同时出错，其概率按 $f^2$ 缩放（$3f^2(1-f)+f^3 \approx 3f^2$），远小于单比特的 $f$（当 $f<0.5$ 时）。这正是重复码以「降低码率」换取「降低误码」的本质——码率降为 $1/3$，但错误概率从一阶量 $f$ 降为二阶量 $f^2$。

---

## Exercise 1.3（習題 1.3）　[3, p.16]

**題幹原文：**

(a) Show that the probability of error of $R_N$, the repetition code with $N$ repetitions, is

```math
p_b = \sum_{n=(N+1)/2}^{N} \binom{N}{n} f^{n} (1-f)^{N-n},
```

for odd $N$.

(b) Assuming $f = 0.1$, which of the terms in this sum is the biggest? How much bigger is it than the second-biggest term?

(c) Use Stirling's approximation (p.2) to approximate the $\binom{N}{n}$ in the largest term, and find, approximately, the probability of error of the repetition code with $N$ repetitions.

(d) Assuming $f=0.1$, find how many repetitions are required to get the probability of error down to $10^{-15}$.

**中文：**

(a) 证明：对于奇数的 $N$，重复码 $R_N$（$N$ 次重复）的差错概率为

```math
p_b = \sum_{n=(N+1)/2}^{N} \binom{N}{n} f^{n} (1-f)^{N-n}.
```

(b) 假设 $f = 0.1$，上式中哪一项最大？它比第二大的项大多少？

(c) 用斯特林近似（Stirling's approximation，见 p.2）来近似最大项中的 $\binom{N}{n}$，并近似求出 $N$ 次重复码的差错概率。

(d) 假设 $f=0.1$，要使差错概率降到 $10^{-15}$，需要多少次重复？

**解答：**

**(a)** 重复码 $R_N$ 把单个信源比特复制 $N$ 次（$N$ 取奇数，保证多数判决不会平票），译码规则为多数判决：当 $N$ 个接收比特中超过半数出错（即出错个数 $n > N/2$）时，判决就出错。出错个数 $n$ 服从参数为 $N,f$ 的二项分布（binomial distribution），每个出错个数为 $n$ 的概率为 $\binom{N}{n} f^n (1-f)^{N-n}$。因为 $N$ 为奇数，$n$ 是整数，条件 $n > N/2$ 等价于 $n \ge (N+1)/2$。于是

```math
p_b = \sum_{n=(N+1)/2}^{N} \binom{N}{n} f^{n} (1-f)^{N-n}.
```

**(b)** 取 $f = 0.1$，二项分布的项 $T_n = \binom{N}{n} f^n (1-f)^{N-n}$。相邻项之比为

```math
\frac{T_{n+1}}{T_n} = \frac{N-n}{n+1} \cdot \frac{f}{1-f}.
```

当 $f = 0.1$ 时 $\dfrac{f}{1-f} = \dfrac{0.1}{0.9} = \dfrac{1}{9}$，故当 $T_{n+1} > T_n$，即 $\dfrac{N-n}{n+1} > 9$，也就是 $n < \dfrac{N-9}{10}$ 时，各项递增；超过该点后递减。因此最大项出现在满足 $n \ge \dfrac{N-9}{10}$ 的第一个整数 $n$，即 $n \approx N/10$ 处（这正是二项分布的众数，位于均值 $Nf = 0.1N$ 附近）。

由于 $p_b$ 只对 $n \ge (N+1)/2$（即 $n \ge 0.5N$）求和，而最大项在 $n \approx 0.1N$ 处，远小于求和下限 $0.5N$，所以**对 $p_b$ 求和贡献最大的项，其实是求和范围内的第一项** $n_{\min} = (N+1)/2$（求和从下限开始，各项随 $n$ 增大而急剧递减）。

记 $m = (N+1)/2$。该项与紧随其后的第二项之比为

```math
\frac{T_m}{T_{m+1}} = \frac{m+1}{N-m} \cdot \frac{1-f}{f}
= \frac{(N+3)/2}{(N-1)/2} \cdot 9
= 9 \cdot \frac{N+3}{N-1}.
```

当 $N$ 较大时 $9 \cdot \dfrac{N+3}{N-1} \approx 9 \cdot \left(1 + \dfrac{4}{N-1}\right) \to 9$。所以第一项比第二项大 **约 9 倍**（精确地，为 $9 \cdot \dfrac{N+3}{N-1}$）。

> <span style="color:#1e8449;">**[note] 为什么最大项不是众数：**</span> 二项分布自身的众数在 $n \approx Nf = 0.1N$，但它落在 $n < (N+1)/2$ 的「不产生错误」区域，被排除在 $p_b$ 的求和之外。真正进入求和范围的项从 $n=(N+1)/2$ 开始就单调递减，因此第一项（$n_{\min}$）最大。这也直观说明：多数判决出错，最「便宜」的方式就是恰好过半数的比特出错，再多出错则概率按因子 $\approx f/(1-f)=1/9$ 逐级衰减。

**(c)** 斯特林近似（Stirling's approximation）为 $\ln n! \approx n \ln n - n$，等价地 $\binom{N}{n} \approx 2^{N H_2(n/N)}$（其中 $H_2$ 为二元熵），更精确的形式（见原书 p.2）是

```math
\binom{N}{n} \approx \frac{2^{N H_2(n/N)}}{\sqrt{2\pi N (n/N)(1-n/N)}} .
```

对最大项 $n = m = (N+1)/2$，取 $p = m/N \approx 1/2$（$N$ 很大时），有 $H_2(1/2) = 1$，于是

```math
\binom{N}{m} \approx 2^{N} \cdot \sqrt{\frac{2}{\pi N}} .
```

代入 $f^{m}(1-f)^{N-m}$，取 $m = (N+1)/2$：

```math
p_b \approx \binom{N}{m} f^{m} (1-f)^{N-m}
\approx 2^{N} \sqrt{\frac{2}{\pi N}} \, f^{(N+1)/2} (1-f)^{(N-1)/2}.
```

提取公共因子，令 $\beta = 4f(1-f)$：

```math
f^{(N+1)/2}(1-f)^{(N-1)/2}
= f \cdot \left( f(1-f) \right)^{(N-1)/2}
= f \cdot \left( \frac{\beta}{4} \right)^{(N-1)/2}.
```

再结合 $2^{N} \cdot 4^{-(N-1)/2} = 2^{N} \cdot 2^{-(N-1)} = 2$，得到

```math
p_b \approx 2 f \, \sqrt{\frac{2}{\pi N}} \;\; \beta^{(N-1)/2},
\qquad \beta = 4f(1-f).
```

（更精确地，含常数因子的形式为 $p_b \approx 2^{N} \sqrt{\frac{2}{\pi N}} \, f^{(N+1)/2}(1-f)^{(N-1)/2}$；对 $f=0.1$，$\beta = 4 \times 0.1 \times 0.9 = 0.36$。）

**(d)** 由 (c)，当 $f=0.1$ 时 $\beta = 0.36$，要求 $p_b \approx 2 f \sqrt{\frac{2}{\pi N}} \,\beta^{(N-1)/2} \le 10^{-15}$。代入 $f=0.1$：

```math
0.2 \sqrt{\frac{2}{\pi N}} \;(0.36)^{(N-1)/2} \le 10^{-15}.
```

两边取以 10 为底的对数，忽略慢变的 $\sqrt{N}$ 项（它只贡献量级 $10^{-1}$ 的因子），有

```math
(N-1)/2 \cdot \log_{10}(0.36) \lesssim -15.
```

而 $\log_{10}(0.36) = \log_{10} 36 - 2 = 1.5563 - 2 = -0.4437$，即 $|{\log_{10} 0.36}| = 0.4437$。于是

```math
\frac{N-1}{2} \gtrsim \frac{15}{0.4437} \approx 33.8,
\qquad N \gtrsim 68.6.
```

因此取 $N \approx 68$，考虑到常数因子与 $N$ 必须为奇数，**大约需要 $N \approx 68$（取最近的奇数 $69$）次重复**，即可把差错概率降到约 $10^{-15}$。

> <span style="color:#1e8449;">**[note] 指数主导与慢变项：**</span> 关键量是 $\beta = 4f(1-f)$，它是小于 1 的数（当 $f \ne 0.5$）。差错概率按 $\beta^{(N-1)/2}$ 指数下降，所以所需重复次数 $N$ 只随目标 $p_b$ 的**对数**线性增长；斯特林近似中的 $\sqrt{N}$ 因子是慢变的，对 $N$ 的估计只产生常数级修正。这也呼应了书中图 1.12 右侧对数坐标图中，$R_N$ 的 $p_b$ 随 $N$ 呈直线下降的现象。

---

## Exercise 1.4（習題 1.4）　[1, p.16]

**題幹原文：** \[原文 OCR 缺失，待核\] Compute the probability of bit error of $R_5$ for a binary symmetric channel with $f = 0.1$, and check that it matches the value shown in figure 1.12.

**中文：** 〔原书此处模糊，疑似为：计算 $f=0.1$ 的二元对称信道上重复码 $R_5$ 的比特差错概率，并验证它与图 1.12 所示的数值一致，待核〕

**解答：**

重复码 $R_5$ 为每个信源比特复制 5 次（$N=5$），多数判决译码。出错条件是 5 个比特中至少 3 个被翻转：

```math
p_b = \sum_{n=3}^{5} \binom{5}{n} f^{n}(1-f)^{5-n}
= \binom{5}{3} f^3 (1-f)^2 + \binom{5}{4} f^4 (1-f) + \binom{5}{5} f^5.
```

代入 $f = 0.1$：

```math
p_b = 10 \times 0.1^3 \times 0.9^2 + 5 \times 0.1^4 \times 0.9 + 1 \times 0.1^5
= 0.0081 + 0.00045 + 0.00001
= 0.00856 \approx 0.0086 .
```

该值与图 1.12 中 $R_5$ 对应的 $p_b \approx 0.0086$（对数坐标图）一致。

> <span style="color:#1e8449;">**[note] 三项量级对比：**</span> 主要贡献来自恰好翻转 3 个的项（$0.0081$），翻转 4 个的项小一个数量级，翻转 5 个的项可忽略。与 $R_3$ 的 $p_b\approx0.028$ 相比，$R_5$ 把误差再降了约一个数量级，代价是码率进一步降到 $1/5$——再次体现「误码率下降」与「码率下降」的权衡。

---

## Exercise 1.5（習題 1.5）　[3, p.16]

**題幹原文：** (OCR 缺失，待核) ... the noise level $f$ ... \[原文此处模糊，待核\]

**中文：** 〔原书此处模糊，疑似为：若信道噪声水平 $f$ 未知，如何……，待核〕

**解答：**

〔本題原文残缺，无法确定确切题干，暂不给出可能错误的推导。请提供该题完整原文后再补全解答。〕
