<!-- 书页 1–50｜来源：A 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->



> <span style="color:#7f8c8d;">原书 p.1｜About Chapter 1（第 1 章预备知识：二项分布与 Stirling 近似）</span>

## About Chapter 1（第 1 章的预备知识）

在第 1 章中，你需要熟悉 binomial distribution（二项分布）。而要解正文中的习题——我强烈建议你去解——你还需要知道阶乘函数的 Stirling's approximation（Stirling 近似），即 $x! \simeq x^{x}e^{-x}\sqrt{2\pi x}$，并且要能把它用到 $\binom{N}{r}=\frac{N!}{(N-r)!\,r!}$ 上。这些主题在下面复习。

> <span style="color:#7f8c8d;">边注：Unfamiliar notation? See Appendix A, p.598.（记号不熟？见附录 A，p.598。）</span>

### The binomial distribution（二项分布）

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 1.1（例 1.1）**</span> 一枚弯曲的硬币（bent coin）出现正面的概率为 $f$。把这枚硬币抛 $N$ 次。正面次数 $r$ 的概率分布是什么？$r$ 的均值与方差是什么？

**Solution（解）** 正面次数服从 binomial distribution（二项分布）：

```math
P(r \mid f, N) = \binom{N}{r} f^{r}(1-f)^{N-r}. \qquad (1.1)
```

该分布的均值 $E[r]$ 与方差 $\mathrm{var}[r]$ 分别定义为

```math
E[r] \equiv \sum_{r=0}^{N} P(r \mid f, N)\, r \qquad (1.2)
```

```math
\mathrm{var}[r] \equiv E\left[(r - E[r])^{2}\right] \qquad (1.3)
```

```math
= E[r^{2}] - (E[r])^{2} = \sum_{r=0}^{N} P(r \mid f, N)\,r^{2} - (E[r])^{2}. \qquad (1.4)
```

与其直接计算 (1.2) 与 (1.4) 中对 $r$ 的求和，最容易的做法是注意到：$r$ 是 $N$ 个独立随机变量之和，这 $N$ 个变量分别是第一次抛掷中正面的个数（取值 0 或 1）、第二次抛掷中正面的个数，依此类推。一般而言，

```math
E[x+y] = E[x] + E[y] \quad \text{for any random variables } x \text{ and } y; \qquad (1.5)
```

```math
\mathrm{var}[x+y] = \mathrm{var}[x] + \mathrm{var}[y] \quad \text{if } x \text{ and } y \text{ are independent.}
```

所以 $r$ 的均值是这些随机变量各自均值之和，$r$ 的方差是它们各自方差之和。单次抛掷中正面个数的均值为 $f \cdot 1 + (1-f) \cdot 0 = f$，而单次抛掷中正面个数的方差为

```math
f \cdot 1^{2} + (1-f) \cdot 0^{2} - f^{2} = f - f^{2} = f(1-f), \qquad (1.6)
```

于是 $r$ 的均值与方差为

```math
E[r] = Nf \quad \text{and} \quad \mathrm{var}[r] = Nf(1-f). \qquad (1.7)
```

<span style="color:#7f8c8d;">1</span>

[Figure 1.1：binomial distribution（二项分布）$P(r \mid f=0.3, N=10)$ 的柱状图，横轴为 $r = 0,1,\ldots,10$，纵轴为概率（0 至 0.3）。它演示的是：$N=10$、单次成功概率 $f=0.3$ 时，概率质量集中在 $r=3$ 附近，即 $Nf$ 附近，且分布左右大致对称、随 $r$ 远离 $Nf$ 迅速衰减。]



> <span style="color:#7f8c8d;">原书 p.2｜用 Poisson 分布推出 Stirling 近似，并引入 binary entropy function</span>

### Approximating $x!$ and $\binom{N}{r}$（逼近 $x!$ 与 $\binom{N}{r}$）

让我们走一条非常规的路线来推导 Stirling 近似。我们从均值为 $\lambda$ 的 Poisson distribution（Poisson 分布）出发：

```math
P(r \mid \lambda) = \frac{e^{-\lambda}\lambda^{r}}{r!} \qquad r \in \{0, 1, 2, \ldots\}. \qquad (1.8)
```

当 $\lambda$ 很大时，这个分布在 $r \simeq \lambda$ 附近——至少在该邻域内——可以被一个均值为 $\lambda$、方差为 $\lambda$ 的 Gaussian distribution（Gaussian 分布）很好地近似：

```math
\frac{e^{-\lambda}\lambda^{r}}{r!} \simeq \frac{1}{\sqrt{2\pi\lambda}} e^{-\frac{(r-\lambda)^{2}}{2\lambda}}. \qquad (1.9)
```

让我们把 $r = \lambda$ 代入这个式子，然后重排它。

```math
\frac{e^{-\lambda}\lambda^{\lambda}}{\lambda!} \simeq \frac{1}{\sqrt{2\pi\lambda}} \qquad (1.10)
```

```math
\lambda! \simeq \lambda^{\lambda} e^{-\lambda}\sqrt{2\pi\lambda}. \qquad (1.11)
```

这就是阶乘函数的 Stirling 近似。

<span style="color:#1e8449;">**[译注]**</span> **Stirling 近似的真正用途不是算阶乘，而是把 $\log\binom{N}{r}$ 的误差压到 $O(\log N)$——这是第 4 章全部论证的算术底座**

$$\ln x! \simeq x\ln x - x + \tfrac12\ln 2\pi x,\qquad \ln\binom{N}{r}\simeq N H_2(\delta),\ \ \delta = r/N.$$

关键在**误差的量级**：主导项是 $\Theta(N)$，修正项是 $O(\log N)$。于是 $\frac{1}{N}\log\binom{N}{r}\to H_2(\delta)$，也就是「每个符号平均多少个 bit」这个量在 $N\to\infty$ 时收敛。抽掉这个 $O(\log N)$ 界的合法来源（比如误用 $\ln x!\approx x\ln x - x$ 就去估计指数率），你会发现误差项仍是 $\Theta(\log N)$ 而非零，但由于它比 $N$ 低一阶，「指数率」这个说法依然成立——这正是 asymptotic equipartition 里「典型集大小 $2^{NH}$」能说成"精确到次指数因子"的全部依据。反过来说：如果 Stirling 的误差是 $\Theta(N)$ 而不是 $O(\log N)$，第 4 章就无法把「典型集几乎包含全部概率」与「典型集只占 $2^{NH}/2^{NH_0}$ 的比例」两条同时成立地讲出来。

数字感：$N=1000$、$p_1=0.1$ 时 $H_2(0.1)=0.469$ bit，$NH=469$ 而 $H_0=1$ 故 $|\mathcal{A}^N|=2^{1000}$——典型集只占 $2^{-531}$，但承载几乎全部概率（译文在 §4.4 后立刻给出这个对比）。

挂载：6.042J 的组合计数与 $\log$ 恒等式（$\log\binom Nr=\log N!-\log r!-\log(N-r)!$）；工程上对应**一切 log-domain 计算**——把概率相乘变成 log 相加、把下溢变成可加量级，与 CSAPP 第 2 章「float 在 $10^{-38}$ 以下下溢成 0」是同一个动机，只是这里的量级是 $2^{-1000}$，double 根本存不下。

坐标：About Chapter 1（原书 p.1–2，PDF p.13–14），式 (1.12)(1.14)；Stirling 的 Poisson 推导在同页；被 §4.4–§4.5（原书 p.79–83，PDF p.91–95）直接调用。


```math
x! \simeq x^{x}e^{-x}\sqrt{2\pi x} \qquad \ln x! \simeq x\ln x - x + \tfrac{1}{2}\ln 2\pi x. \qquad (1.12)
```

我们不仅推出了主导阶的行为 $x! \simeq x^{x}e^{-x}$，而且还免费得到了下一阶的修正项 $\sqrt{2\pi x}$。现在把 Stirling 近似用到 $\ln\binom{N}{r}$ 上：

```math
\ln\binom{N}{r} = \ln\frac{N!}{(N-r)!\,r!} \simeq (N-r)\ln\frac{N}{N-r} + r\ln\frac{N}{r}. \qquad (1.13)
```

由于这个方程中所有项都是对数，结果可以换到任意底数重写。我们将用 `ln` 表示自然对数（$\log_e$），用 `log` 表示以 2 为底的对数（$\log_2$）。

> <span style="color:#7f8c8d;">边注：Recall that $\log_2 x = \log_e x \cdot \log_e 2$。（回忆 $\log_2 x = \log_e x \cdot \log_e 2$。）Note that $\frac{\partial}{\partial x}\log_2 x = \frac{1}{x}\frac{1}{\log_e 2}$。（注意 $\frac{\partial}{\partial x}\log_2 x = \frac{1}{x}\frac{1}{\log_e 2}$。）</span>

如果我们引入 binary entropy function（二元熵函数）

```math
H_2(x) \equiv x\log\frac{1}{x} + (1-x)\log\frac{1}{1-x}, \qquad (1.14)
```

那么我们就可以把近似 (1.13) 重写为

```math
\log\binom{N}{r} \simeq N H_2(r/N), \qquad (1.15)
```

或者等价地

```math
\binom{N}{r} \simeq 2^{N H_2(r/N)}. \qquad (1.16)
```

如果我们需要更精确的近似，可以保留 Stirling 近似 (1.12) 中下一阶的项：

```math
\log\binom{N}{r} \simeq N H_2(r/N) - \tfrac{1}{2}\log\left(2\pi N \frac{r}{N}\frac{N-r}{N}\right). \qquad (1.17)
```

[Figure 1.2：Poisson 分布 $P(r \mid \lambda = 15)$ 的柱状图，横轴为 $r$（0 到 25 左右），纵轴为概率（0 到 0.12）。它演示的是：$\lambda = 15$ 时 Poisson 分布的形状与 Gaussian 形状几乎重合，这正是 (1.9) 得以成立的原因——以便在 $r = \lambda$ 处取值从而得到 Stirling 近似。]

[Figure 1.3：binary entropy function（二元熵函数）$H_2(x)$ 的曲线，横轴为 $x \in [0,1]$，纵轴为 $H_2$（0 到 1）。它演示的是：$H_2$ 在 $x = 0$ 与 $x = 1$ 处取 0，在 $x = 1/2$ 处取最大值 1，且关于 $x = 1/2$ 对称——这是 (1.15)(1.16) 中 $\binom{N}{r}$ 在 $r = N/2$ 处取最大值的来源。]



> <span style="color:#7f8c8d;">原书 p.3｜第 1 章 Introduction to Information Theory 开篇与 §1.1</span>

# 1 Introduction to Information Theory（信息论导论）

> <span style="color:#7f8c8d;">The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point.（通信的根本问题，是在一点上精确地或近似地复现另一点上所选出的消息。）—— (Claude Shannon, 1948)</span>

在本书的前半部分，我们研究如何度量 information content（信息含量）；我们学习如何压缩数据；我们学习如何在并不完善的 communication channels（通信信道）上完美地通信。

我们先对最后这个问题建立一点感觉。

## 1.1 How can we achieve perfect communication over an imperfect, noisy communication channel?（我们如何在一个不完善、带噪的通信信道上实现完美通信？）

带噪通信信道的一些例子是：

- 一条 analog telephone line（模拟电话线），两个 modem（调制解调器）在它上面传输数字信息；
- 从环绕 Jupiter（木星）的航天器 Galileo（伽利略号）到地球的 radio communication link（无线电通信链路）；
- 复制中的细胞，其中子代细胞的 DNA 携带来自亲代细胞的信息；
- 一块 disk drive（磁盘驱动器）。

最后一个例子说明，通信未必是信息从一个地方传到另一个地方。当我们在磁盘驱动器上写一个文件时，我们会在同一位置把它读回来——但是在更晚的时刻。

这些信道都是带噪的。电话线会与其他线路发生 cross-talk（串扰）；线路中的硬件会扭曲传输信号并给它加上噪声。用来接收 Galileo 那台微弱发射机的 deep space network（深空网络）会收到来自地球与宇宙源的 background radiation（背景辐射）。DNA 会遭受突变与损伤。磁盘驱动器通过把一小块磁性材料按两种取向之一排列来写入一个二进制数字（一个 0 或 1，也称 bit（比特）），而它后来可能读不出所存储的那个二进制数字：那块材料可能自发地翻转磁化方向，或者背景噪声的一次扰动可能使读取电路报出错误的二进制数字值，或者由于相邻比特的干扰，写入头一开始就没有诱发出磁化。

在所有这些情形中，如果我们把数据——例如一串比特——通过信道传输，那么收到的消息与发送的消息不完全相同的概率就非零。

<span style="color:#7f8c8d;">3</span>

[Figure：四个带噪信道实例的并排小示意图，从左到右依次把 source（信源）与 destination（信宿）用竖线隔开：(a) `modem → telephone line → modem`；(b) `Galileo → radio waves → Earth`；(c) `parent cell → daughter cell` 与 `cell → daughter cell`（细胞分裂）；(d) `computer memory → disk drive → computer memory`。它演示的是 §1.1 开头所列的四类信道，并特别点出最后一种（存储）中「信道」连接的是同一地点的两个不同时刻，而非两个不同地点。]



> <span style="color:#7f8c8d;">原书 p.4｜binary symmetric channel、physical solution 与 `system' solution</span>

我们更希望有一个通信信道，使这个概率为零——或者接近于零，以至于在实际意义上无法与零区分。

<span style="color:#1e8449;">**[译注]**</span> **「错误概率任意小」是定理的全部内容——要求严格为零，capacity 立刻坍缩成 0**

这句「接近于零，以至于在实际意义上无法与零区分」不是修辞让步，而是定理的量化形式：$\forall \epsilon>0\ \exists N,\ \text{code}$ 使 $P_e<\epsilon$，且码率 $R<C$ 固定。抽掉「任意小」这个 $\epsilon$ 语言、改成要求 $P_e=0$，结论就崩：$f>0$ 的 BSC 上，零错误只能靠 $R\to0$（例如 $R_9$ 重复码把 $P_e$ 压到 $10^{-3}$ 量级，但要继续压只能加长重复、码率趋于 0）。也就是说「perfect communication over an imperfect channel」这句话里的 "perfect" 必须读成 "arbitrarily reliable"，否则定理是假的。

这也解释了为什么第 1 章的 Hamming 码只是引子：（7,4）码率 $4/7\approx0.571$、只能纠一个错，而 §1.3 会给出 $f=0.1$ 时 $C\approx0.5$ 且要求 $\epsilon$ 任意小——同一个信道，一个具体码（有限 $N$、有限纠错能力）与一个极限陈述（$N\to\infty$）之间的距离，就是整个第 10 章要填的。

挂载：Thomson 实分析里 $\epsilon$-$N$ 定义与「极限不是达到」这条纪律：$\sup$ 与 $\max$ 的区别正是这里 $\epsilon$ 与 $0$ 的区别；若把这句读成「存在一个码使 $P_e=0$」，就等于把 $\sup$ 当 $\max$ 用，是同一类错误。

坐标：§1.1（原书 p.3–4，PDF p.15–16）；定理的精确形式与 $\epsilon$ 在 §1.3（原书 p.24–25，PDF p.36–37）与 §10.1（原书 p.149，PDF p.161）。


让我们考虑一块带噪磁盘驱动器，它正确地传输每个比特的概率为 $(1-f)$，错误地传输每个比特的概率为 $f$。这个通信信道模型被称为 binary symmetric channel（二元对称信道，图 1.4）。

```math
\begin{aligned}
P(y=0 \mid x=0) &= 1-f, &\quad P(y=0 \mid x=1) &= f, \\
P(y=1 \mid x=0) &= f, &\quad P(y=1 \mid x=1) &= 1-f.
\end{aligned}
```

[Figure 1.4：binary symmetric channel（二元对称信道）的示意图。两个节点分别标注 $x = 0$ 与 $x = 1$（发送符号），另两个节点标注 $y = 0$ 与 $y = 1$（接收符号）；从 $x=0$ 到 $y=0$ 与从 $x=1$ 到 $y=1$ 的边标 $(1-f)$，交叉的两条边标 $f$。它演示的是：发送符号 $x$ 与接收符号 $y$ 之间，比特被翻转的概率就是噪声水平 $f$，且 $0$、$1$ 两个符号被正确传输的概率相同——这就是「对称」的含义。]

[Figure 1.5：一段长度为 10 000 的二进制数据序列通过噪声水平 $f = 0.1$ 的 binary symmetric channel（二元对称信道）的结果，以 Dilbert 漫画的形式呈现（漫画中有若干比特显示为错乱；原书图注注明 Dilbert image Copyright © 1997 United Feature Syndicate, Inc., used with permission）。它演示的是：当 $f = 0.1$ 时，每十个比特就大约有一个被翻转，信道输出看上去已经面目全非。]

作为例子，让我们设想 $f = 0.1$，也就是百分之十的比特被翻转（图 1.5）。一块有用的磁盘驱动器在它整个寿命中一个比特都不会翻转。如果我们预期十年间每天读写 1 gigabyte（吉字节），那么我们需要的 bit error probability（误比特概率）量级为 $10^{-15}$，或者更小。达到这个目标有两条路。

### The physical solution（物理解法）

物理解法是改善通信信道的物理特性以降低其错误概率。我们可以通过以下方式改进我们的磁盘驱动器：

1. 在其电路中采用更可靠的元件；

2. 把空气从磁盘外壳中抽走，从而消除扰动读取头偏离磁道的湍流；

3. 用更大块的磁性材料来表示每个比特；或者

4. 采用更高功率的信号，或者对电路制冷，以降低热噪声。

这些物理改造通常会提高通信信道的成本。

### The `system' solution（「系统」解法）

信息论与编码理论提供了另一条（也令人兴奋得多的）途径：我们接受给定的带噪信道，把它当成既成事实，然后给它加上通信系统，使我们能够检测并纠正信道引入的错误。如图 1.6 所示，我们在信道之前加一个 encoder（编码器），在信道之后加一个 decoder（解码器）。编码器把 source message（源消息）$s$ 编码成 transmitted message（发送消息）$t$，用某种方式给原消息加上 redundancy（冗余）。信道给发送消息加上 noise（噪声），得到 received message（接收消息）$r$。解码器利用编码系统所引入的、已知的冗余，同时推断出原始信号 $s$ 与被加入的噪声。



> <span style="color:#7f8c8d;">原书 p.5｜图 1.6 与 §1.2 开头：repetition codes</span>

[Figure 1.6：实现带噪信道上可靠通信的「系统」解法框图。源消息 $s$ 进入 encoder（编码器），编码器输出发送消息 $t$；$t$ 通过 noisy channel（带噪信道）得到接收消息 $r$；$r$ 进入 decoder（解码器），解码器输出估计的源消息 $\hat{s}$。它演示的是：编码系统把系统性的冗余注入发送向量 $t$，而解码系统利用这份已知的冗余，从接收向量 $r$ 中同时推断出原始源向量与信道引入的噪声——代价从「改造物理信道」转移到「编码器与解码器的计算」。]

与物理解法只能以不断增高的成本换取信道的一点一点改善不同，系统解法可以把带噪信道变成可靠的通信信道，而唯一的成本是编码器与解码器上的计算需求。

信息论关心的是这类系统的理论局限与理论潜力。「我们所能达到的最好的纠错性能是什么？」

编码理论关心的是构造出实用的编码与解码系统。

## 1.2 Error-correcting codes for the binary symmetric channel（二元对称信道上的纠错码）

我们现在来考察编码与解码系统的例子。给一次传输加上有用的冗余，最简单的办法是什么？[为了让游戏规则清楚：我们想要能够检测并纠正错误；而且重传不是一个选项。我们只有一次机会去编码、传输和解码。]

### Repetition codes（重复码）

一个直截了当的想法是：把消息的每个比特重复预先约定的次数——例如重复三次，如表 1.7 所示。我们把这种 repetition code（重复码）称为 `R3`。

设想我们用这个重复码，在一个噪声水平 $f = 0.1$ 的 binary symmetric channel（二元对称信道）上传输源消息

```math
s = 0\,0\,1\,0\,1\,1\,0 .
```

我们可以把该信道描述为给发送向量「加上」一个稀疏的噪声向量 $n$——这里的加法是在 modulo 2 arithmetic（模 2 算术）下做的，也就是 $1+1=0$ 的二进制代数。图 1.8 给出了一个可能的噪声向量 $n$ 与接收向量 $r = t + n$。

```math
\begin{aligned}
s \;&\; 0\ 0\ 1\ 0\ 1\ 1\ 0 \\
t \;&\; 000\ 000\ 111\ 000\ 111\ 111\ 000 \\
n \;&\; 000\ 001\ 000\ 000\ 101\ 000\ 000 \\
r \;&\; 000\ 001\ 111\ 000\ 010\ 111\ 000
\end{aligned}
```

[Table 1.7：repetition code（重复码）`R3` 的对照表——源序列 $s$ 中比特 `0` 映射为发送序列 $t$ 中的 `000`，比特 `1` 映射为 `111`。它演示的是这个码的全部编码规则：一个比特变成三个相同的比特。]

[Figure 1.8：用 `R3` 的一次传输实例，即上面那四行 $s, t, n, r$。它演示的是：噪声向量 $n$ 在模 2 算术下「加」到发送向量 $t$ 上得到接收向量 $r$——第一个代码块的 `000` 完好，第二个代码块的 `000` 被翻成 `001`，第五个代码块的 `111` 被翻成 `010`（两个比特被翻转）。]

我们应该如何解码这个接收向量？最优算法是每次看三个接收比特，取 majority vote（多数票），见算法 1.9。



> <span style="color:#7f8c8d;">原书 p.6｜算法 1.9（majority-vote decoding）与它的 Bayes 推导</span>

[Algorithm 1.9：`R3` 的 majority-vote（多数票）解码算法，以及假定信道为 binary symmetric channel、$\lambda \equiv (1-f)/f$ 时各接收序列的 likelihood ratio（似然比）$P(r \mid s=1)/P(r \mid s=0)$：`000` 比值为 $\lambda^{-3}$ → 解码为 0；`001`、`010`、`100` 比值为 $\lambda^{-1}$ → 0；`101`、`110`、`011` 比值为 $\lambda^{1}$ → 1；`111` 比值为 $\lambda^{3}$ → 1。它演示的是：三个比特里多数是什么，就解码成什么；而这一规则恰好与似然比的符号一致。]

冒着把显然之事讲一遍的风险，让我们来证明这个结果。最优的解码判决（「最优」指判错的概率最小）是：给定 $r$，找出最可能的 $s$ 取值。考虑单个比特 $s$ 的解码，它被编码为 $t(s)$，并产生了三个接收比特 $r = r_1r_2r_3$。由 Bayes' theorem（Bayes 定理），$s$ 的 posterior probability（后验概率）为

```math
P(s \mid r_1r_2r_3) = \frac{P(r_1r_2r_3 \mid s)P(s)}{P(r_1r_2r_3)}. \qquad (1.18)
```

我们可以把两个备选项的后验概率分别写成：

```math
P(s=1 \mid r_1r_2r_3) = \frac{P(r_1r_2r_3 \mid s=1)P(s=1)}{P(r_1r_2r_3)}; \qquad (1.19)
```

```math
P(s=0 \mid r_1r_2r_3) = \frac{P(r_1r_2r_3 \mid s=0)P(s=0)}{P(r_1r_2r_3)}. \qquad (1.20)
```

这个后验概率由两个因素决定：prior probability（先验概率）$P(s)$，以及与数据有关的项 $P(r_1r_2r_3 \mid s)$，后者称为 $s$ 的 likelihood（似然）。在寻找最优解码判决时，归一化常数 $P(r_1r_2r_3)$ 不必计算；该判决是：若 $P(s=0 \mid r) > P(s=1 \mid r)$ 就猜 $\hat{s} = 0$，

否则 $\hat{s} = 1$。

为了求出 $P(s=0 \mid r)$ 与 $P(s=1 \mid r)$，我们必须对两个假设 $s=0$ 与 $s=1$ 的先验概率作假设，还必须对给定 $s$ 时 $r$ 的概率作假设。我们假设先验概率相等：$P(s=0) = P(s=1) = 0.5$；于是最大化后验概率 $P(s \mid r)$ 就等价于最大化似然 $P(r \mid s)$。并且我们假设信道是噪声水平 $f < 0.5$ 的 binary symmetric channel（二元对称信道），于是似然为

```math
P(r \mid s) = P(r \mid t(s)) = \prod_{n=1}^{N} P(r_n \mid t_n(s)), \qquad (1.21)
```

其中 $N = 3$ 是我们所考虑的块中发送比特的个数，并且

```math
P(r_n \mid t_n) =
\begin{cases}
(1-f) & \text{if } r_n = t_n \\
f & \text{if } r_n \neq t_n.
\end{cases} \qquad (1.22)
```

于是两个假设的 likelihood ratio（似然比）为

```math
\frac{P(r \mid s=1)}{P(r \mid s=0)} = \prod_{n=1}^{N}\frac{P(r_n \mid t_n(1))}{P(r_n \mid t_n(0))}; \qquad (1.23)
```

每个因子 $\frac{P(r_n \mid t_n(0))}{P(r_n \mid t_n(1))}$ 在 $r_n = 1$ 时等于 $f/(1-f)$，在 $r_n = 0$ 时等于 $(1-f)/f$。比值 $\frac{(1-f)}{f}$ 大于 1，因为 $f < 0.5$，所以胜出的假设就是「票数」最多的那个，每一票在似然比中贡献一个因子 $\lambda$。



> <span style="color:#7f8c8d;">原书 p.7｜多数票解码的应用、习题 1.2、图 1.10 与图 1.11</span>

因此，如果假设信道是 binary symmetric channel（二元对称信道）、并且两个可能的源消息 0 与 1 先验概率相等，那么算法 1.9 所示的 majority-vote decoder（多数票解码器）就是最优解码器。

现在我们把这个多数票解码器用到图 1.8 的接收向量上。前三个接收比特全是 0，所以我们把这个三元组解码为 0。在图 1.8 的第二个三元组中，有两个 0 和一个 1，所以我们把这个三元组解码为 0——在这个情形中错误被纠正了。然而并不是所有错误都能被纠正。如果我们不走运，两个错误落在同一个块里，就像图 1.8 的第五个三元组那样，那么解码规则就会给出错误答案，如图 1.10 所示。

```math
\begin{aligned}
s \;&\; 0\ 0\ 1\ 0\ 1\ 1\ 0 \\
t \;&\; 000\ 000\ 111\ 000\ 111\ 111\ 000 \\
n \;&\; 000\ 001\ 000\ 000\ 101\ 000\ 000 \\
r \;&\; 000\ 001\ 111\ 000\ 010\ 111\ 000 \\
\hat{s} \;&\; 0\ 0\ 1\ 0\ 0\ 1\ 0
\end{aligned}
```

`s` 与 `ŝ` 的最后两行下方分别标注 `corrected errors`（已纠正的错误，第 2 个代码块）与 `undetected errors`（未被发现的错误，第 5 个代码块）。

[Figure 1.10：用多数票解码器解码图 1.8 的接收向量的结果，即上面那五行 $s, t, n, r, \hat{s}$。它演示的是：第二个代码块中的单个错误被纠正（$\hat{s}$ 该位恢复为 1），而第五个代码块中的两个错误反而使解码结果偏离正确值（$\hat{s}$ 该位被判为 0），于是总共留下三个未纠正的比特错误。]

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.2.[2, p.16]**</span> Show that the error probability is reduced by the use of `R3` by computing the error probability of this code for a binary symmetric channel with noise level $f$.

> <span style="color:#7f8c8d;">边注：The exercise's rating, e.g. `[2 ]', indicates its difficulty: `1' exercises are the easiest. Exercises that are accompanied by a marginal rat are especially recommended. If a solution or partial solution is provided, the page is indicated after the difficulty rating; for example, this exercise's solution is on page 16.（习题的等级，例如 `[2 ]`，标示其难度：`1` 级习题最容易。旁边带注边小老鼠的习题是特别推荐的。若给出解答或部分解答，页码标在难度等级之后；例如这道习题的解答在第 16 页。）</span>

误码概率由三个比特的块中有两个比特被翻转的概率主导，它按 $f^{2}$ 的规模变化。在 $f = 0.1$ 的 binary symmetric channel（二元对称信道）情形下，`R3` 码在解码之后每个比特的误码概率为 $p_b \simeq 0.03$。图 1.11 展示了用重复码通过 binary symmetric channel 传输一幅二值图像的结果。

[Figure 1.11：用重复码与多数票解码算法，把 10 000 个源比特通过 $f = 10\%$ 的 binary symmetric channel 传输的完整链路示意，按 `s → encoder → t → channel (f=10%) → r → decoder → ŝ` 从左到右排列，并配有对应的图像。它演示的是：解码后的比特错误概率降到了约 3%，但 rate（码率）也降到了 1/3——这就是 §1.2 之后反复要权衡的那笔账。]



> <span style="color:#7f8c8d;">原书 p.8｜图 1.12（误差-码率权衡）、习题 1.3、block codes 的引入</span>

[Figure 1.12：repetition codes（重复码）在 $f = 0.1$ 的 binary symmetric channel 上的 error probability（误码概率）$p_b$ 对 rate（码率）的关系图，左右两幅分别是线性纵轴与对数纵轴。左图纵轴 $p_b \in [0, 0.1]$，标出 $R1$、$R3$、$R5$、$R61$ 四点；右图纵轴为对数刻度（$1$ 到 $10^{-15}$），标出 $R1$、$R5$、$R61$ 与 BCH 码的位置。两图都标了一句 `more useful codes`（更有用的码）指向右下方。它演示的是：重复次数越多，$p_b$ 越小，但码率 $R = 1/N$ 也越小；「更有用的码」应当同时落在码率大、$p_b$ 小的区域——重复码永远到不了那里。]

因此 `R3` 重复码确实如我们所愿地降低了错误概率。然而我们失去了某些东西：我们的信息传输率降到了三分之一。所以，如果用重复码在电话线上传输数据，它会降低出错频次，但它同时也会降低我们的通信速率。每次通话我们将不得不付出三倍的价钱。同样地，要造出一块 $p_b = 0.03$ 的 1 gigabyte（吉字节）磁盘驱动器，我们需要三块原有的带噪 1 吉字节磁盘驱动器。

我们能不能把错误概率压得更低，压到一块能卖得出去的磁盘驱动器所要求的数值——$10^{-15}$？我们可以用重复次数更多的重复码来达到更低的错误概率。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.3.[3, p.16]**</span> (a) Show that the probability of error of $R_N$, the repetition code with $N$ repetitions, is

```math
p_b = \sum_{n=(N+1)/2}^{N} \binom{N}{n} f^{n}(1-f)^{N-n}, \qquad (1.24)
```

for odd $N$.

(b) Assuming $f = 0.1$, which of the terms in this sum is the biggest? How much bigger is it than the second-biggest term?

(c) Use Stirling's approximation (p.2) to approximate the $\binom{N}{n}$ in the largest term, and find, approximately, the probability of error of the repetition code with $N$ repetitions.

(d) Assuming $f = 0.1$, find how many repetitions are required to get the probability of error down to $10^{-15}$. [Answer: about 60.]

所以，要用 $f = 0.1$ 的带噪 1 吉字节驱动器造出一块所需可靠度的 1 吉字节磁盘驱动器，我们需要六十块带噪磁盘驱动器。重复码在错误概率与码率之间的权衡如图 1.12 所示。

### Block codes — the (7, 4) Hamming code（分组码——(7, 4) Hamming 码）

我们希望以极小的错误概率、并且以可观的码率来通信。我们能在重复码之外做得更好吗？如果我们给一块一块的数据加冗余，而不是一次只编码一个比特，会怎样？我们现在来研究一个简单的 block code（分组码）。



> <span style="color:#7f8c8d;">原书 p.9｜§1.2：(7, 4) Hamming 码的编码规则、表 1.14、generator matrix</span>

一个 block code（分组码）是一条规则，把一个长度为 $K$ 的源比特序列 $s$ 转换成一条长度为 $N$ 比特的发送序列 $t$。为了加入冗余，我们让 $N$ 大于 $K$。在 linear block code（线性分组码）中，多出来的 $N-K$ 个比特是原来 $K$ 个比特的线性函数；这些多出来的比特称为 parity-check bits（奇偶校验比特）。线性分组码的一个例子是 (7, 4) Hamming code（Hamming 码），它对每 $K = 4$ 个源比特发送 $N = 7$ 个比特。

[Figure 1.13：用三个相交的圆表示 (7, 4) Hamming 码编码的图示。(a) 三个圆两两相交，七个位置分别放 $t_1,t_2,t_3,t_4,t_5,t_6,t_7$——四个源比特 $s_1s_2s_3s_4$ 放在两两相交的中央区域（图中标 $s_1\ s_3\ s_2$ 与 $t_7$、$st$ 一带），三个 parity-check bits 放在三个圆各自只属于本部的那一块。(b) 一个具体例子：源比特取 $s = 1000$ 时的发送码字。它演示的是：每个 parity-check bit 恰好属于一个圆，因此每个圆给出一个 parity constraint（奇偶约束），三个圆给出三个约束。]

这个码的编码操作如图 1.13 所示。我们把七个发送比特安排在三个相交的圆里。前四个发送比特 $t_1t_2t_3t_4$ 被设为等于四个源比特 $s_1s_2s_3s_4$。parity-check bits（奇偶校验比特）$t_5t_6t_7$ 被设为使得每个圆内的 parity（奇偶性）都是 even（偶）：第一个奇偶校验比特是前三个源比特的奇偶性（也就是说，如果这三个比特之和为偶，它就是 0，如果和为奇，它就是 1）；第二个是后三个源比特的奇偶性；第三个奇偶比特是源比特一、三、四的奇偶性。

作为例子，图 1.13b 给出了 $s = 1000$ 情形下的发送码字。表 1.14 给出了四个源比特的 $2^{4} =$ 十六种取法各自生成的码字。这些码字有一个特殊性质：任意两个码字之间至少有三个比特不同。

[Table 1.14：(7, 4) Hamming 码的十六个码字 $\{t\}$，按源比特 $s$ 的取值列出：`0000`→`0000000`、`0001`→`0001011`、`0010`→`0010111`、`0011`→`0011100`、`0100`→`0100110`、`0101`→`0101101`、`0110`→`0110001`、`0111`→`0111010`、`1000`→`1000101`、`1001`→`1001110`、`1010`→`1010010`、`1011`→`1011001`、`1100`→`1100011`、`1101`→`1101000`、`1110`→`1110100`、`1111`→`1111111`。它演示的是：任意一对码字之间至少相差三个比特（即 minimum distance（最小距离）为 3），这正是这个码能纠正任意单个比特错误的原因。]

因为 Hamming 码是线性码，它可以用矩阵简洁地写出来。发送码字 $t$ 由源序列 $s$ 通过一个线性操作得到：

```math
t = G^{T}s, \qquad (1.25)
```

其中 $G$ 是该码的 generator matrix（生成矩阵），

```math
G^{T} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 1 & 1 & 0 \\
0 & 1 & 1 & 1 \\
1 & 0 & 1 & 1
\end{bmatrix}, \qquad (1.26)
```

而编码操作 (1.25) 使用 modulo-2 arithmetic（模 2 算术，$1+1=0$、$0+1=1$ 等等）。

在编码操作 (1.25) 中，我假定了 $s$ 与 $t$ 是 column vector（列向量）。如果它们改为 row vector（行向量），那么这个方程就换成

```math
t = sG, \qquad (1.27)
```



> <span style="color:#7f8c8d;">原书 p.10｜generator matrix 的行向量解读、(7, 4) Hamming 码的解码问题</span>

其中

```math
G =
\begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 1 & 1 \\
0 & 0 & 1 & 0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 & 1
\end{bmatrix}. \qquad (1.28)
```

> <span style="color:#7f8c8d;">边注：我觉得右乘 (1.25) 比左乘 (1.27) 更好理解。不过许多编码理论的教材采用左乘的约定 (1.27–1.28)。</span>

generator matrix (1.28) 的各行可以看作是在一个七维二进制空间中定义了四个 basis vector（基向量）。十六个码字由这些向量的全部可能 linear combination（线性组合）得到。

### Decoding the (7, 4) Hamming code（(7, 4) Hamming 码的解码）

当我们发明一个更复杂的编码器 $s \to t$ 时，解码接收向量 $r$ 的任务就不那么直截了当了。记住：任何一个比特都可能被翻转，包括 parity bits（奇偶校验比特）。

如果我们假设信道是 binary symmetric channel（二元对称信道）、并且所有源向量等概率，那么 optimal decoder（最优解码器）所找的源向量 $s$，是使编码 $t(s)$ 与接收向量 $r$ 在最少比特上不同的那个。[为什么是这样，请参见 likelihood（似然）函数 (1.23)。]我们可以通过度量 $r$ 与表 1.14 中十六个码字各自的距离，然后挑最近的那个，来解这个解码问题。有没有更高效的办法来找出最可能的源向量？

### Syndrome decoding for the Hamming code（Hamming 码的 syndrome 解码）

对 (7, 4) Hamming 码，解码问题有一个图形化的解法，它基于编码图 1.13。

作为第一个例子，让我们假设传输的是 $t = 1000101$，而噪声翻转了第二个比特，于是接收向量是 $r = 1000101 \oplus 0100000 = 1100101$。我们把接收向量按图 1.15a 写进三个圆里，然后看这三个圆各自的奇偶性是否为偶。奇偶性不是偶的那些圆在图 1.15b 中用虚线画出。解码任务是找出能解释这些奇偶规则违反的最小翻转比特集合。[违反 parity checks（奇偶校验）的模式称为 syndrome（伴随式），可以写成一个二进制向量——例如在图 1.15b 中，syndrome 是 $z = (1, 1, 0)$，因为前两个圆「不高兴」（奇偶性为 1），而第三个圆「高兴」（奇偶性为 0）。]

为了完成解码任务，我们问这个问题：我们能不能找到一个唯一的比特，它位于所有「不高兴」的圆之内、并且位于所有「高兴」的圆之外？如果能，那么翻转这个比特就能解释所观察到的 syndrome。在图 1.15b 所示的情形中，比特 $r_2$ 位于两个不高兴的圆之内、且位于那个高兴的圆之外；没有其他单个比特具有这个性质，所以 $r_2$ 是唯一能够解释该 syndrome 的单个比特。

让我们再做几个例子。图 1.15c 展示了当某个奇偶校验比特 $t_5$ 被噪声翻转时会发生什么。只有一个校验被违反。只有 $r_5$ 位于这个不高兴的圆之内、且位于另外两个高兴的圆之外，所以 $r_5$ 被认定为唯一能够解释该 syndrome 的单个比特。

如果中间那个比特 $r_3$ 被接收为翻转的，图 1.15d 表明三个校验全被违反；只有 $r_3$ 位于三个圆之内，所以 $r_3$ 被认定为可疑比特。



> <span style="color:#7f8c8d;">原书 p.11｜图 1.15、算法 1.16（syndrome 查表）、两比特错误的情形、一般线性码的 syndrome 解码</span>

[Figure 1.15：(7, 4) Hamming 码解码的图示（五幅小图 (a)–(e)）。(a) 把接收向量写进图 1.13 的那三个相交圆里。(b)(c)(d) 分别对应「发送向量如图 1.13b、且某个比特被翻转」的情形，被违反的 parity checks 用虚线圆高亮；每幅图中标注出的那一个比特（$r_2$、$r_5$、$r_3$）就是最能解释该 syndrome 的可疑比特，而它恰好就是真正被翻转的比特。(e) 两个比特 $s_3$ 与 $t_7$ 被翻转的情形；(e') 是解码算法的输出——最可能的可疑比特被判为 $r_2$（图中画圈标出）。它演示的是：seven 个比特中总有一个比特最能解释每一种 syndrome，即每一种「违反/满足」的模式；一对一错误时它就是真正出错的比特，而对某些两比特错误它会给出错误答案。]

[Algorithm 1.16：(7, 4) Hamming 码 optimal decoder（最优解码器）在假设 binary symmetric channel（二元对称信道）、噪声水平 $f$ 很小的前提下的动作表。按 syndrome $z$（列出各项奇偶校验是否被违反，违反 1、满足 0，顺序依次为 $r_5, r_6, r_7$ 所对应的校验）查表：$z = 000$ 时无动作；$z = 001$ 时翻转 $r_7$；$010$ 时翻转 $r_6$；$011$ 时翻转 $r_4$；$100$ 时翻转 $r_5$；$101$ 时翻转 $r_1$；$110$ 时翻转 $r_2$；$111$ 时翻转 $r_3$。它演示的是：七个非零 syndrome 与七种单比特错误模式一一对应，所以查表即可解码。]

如果你试着翻转这七个比特中的任何一个，你会发现每种情形得到的 syndrome 都不同——七个非零 syndrome，每个比特一个。还有一个 syndrome，就是全零 syndrome。所以，如果信道是噪声水平 $f$ 很小的 binary symmetric channel（二元对称信道），那么正如算法 1.16 所示，最优解码器根据 syndrome 最多翻转一个比特。每个 syndrome 也可能由别的噪声模式造成，但任何具有同一 syndrome 的其他噪声模式必定更不可能，因为它涉及更多次噪声事件。

如果噪声实际上翻转了不止一个比特，会怎样？图 1.15e 展示了两个比特 $r_3$ 与 $r_7$ 被接收为翻转时的情形。syndrome 是 $110$，它使我们怀疑单个比特 $r_2$；于是我们的最优解码算法翻转这个比特，得到一个含三个错误的解码模式，如图 1.15e' 所示。如果我们使用最优解码算法，任何两比特的错误模式都会导致一个含三个错误的七比特解码向量。

### General view of decoding for linear codes: syndrome decoding（线性码解码的一般观点：syndrome 解码）

我们也可以用矩阵来表述线性码的解码问题。前四个接收比特 $r_1r_2r_3r_4$ 自称是那四个源比特；接收比特 $r_5r_6r_7$ 自称是源比特的奇偶性，其定义由 generator matrix $G$ 给出。我们针对接收比特 $r_1r_2r_3r_4$ 算出三个 parity-check bits，再看它们是否与那三个接收比特 $r_5r_6r_7$ 相符。这两个三元组之间的差（模 2）称为接收向量的 syndrome（伴随式）。如果 syndrome 为零——如果三个奇偶校验都「高兴」——那么接收向量就是一个码字，最可能的解码结果就是



> <span style="color:#7f8c8d;">原书 p.12｜parity-check matrix $H$、习题 1.4、maximum-likelihood decoder、(7, 4) Hamming 码性质小结</span>

读出它的前四个比特。如果 syndrome 非零，那么这个块的噪声序列就非零，而 syndrome 就是指向最可能错误模式的指针。

syndrome 向量的计算是一个线性操作。如果我们定义 $3\times4$ 矩阵 $P$，使方程 (1.26) 中的矩阵可以写成

```math
G^{T} =
\begin{bmatrix}
I_4 \\ P
\end{bmatrix}, \qquad (1.29)
```

其中 $I_4$ 是 $4\times4$ 的 identity matrix（单位矩阵），那么 syndrome 向量就是 $z = Hr$，其中 parity-check matrix（奇偶校验矩阵）$H$ 由 $H = \left[-P \mid I_3\right]$ 给出；在模 2 算术下 $-1 \equiv 1$，所以

```math
H = \left[P \mid I_3\right] =
\begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 1 & 0 & 0 & 1
\end{bmatrix}. \qquad (1.30)
```

该码的所有码字 $t = G^{T}s$ 都满足

```math
Ht =
\begin{bmatrix}
0 \\ 0 \\ 0
\end{bmatrix}. \qquad (1.31)
```

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.4.[1 ]**</span> Prove that this is so by evaluating the $3\times4$ matrix $HG^{T}$.

由于接收向量由 $r = G^{T}s + n$ 给出，syndrome-decoding（伴随式解码）问题就是：找出满足方程

```math
Hn = z \qquad (1.32)
```

的最可能的噪声向量 $n$。

能解这个问题的解码算法称为 maximum-likelihood decoder（最大似然解码器）。我们将在后面的各章讨论这类解码问题。

### Summary of the (7, 4) Hamming code's properties（(7, 4) Hamming 码性质小结）

每一个可能的 7 比特接收向量，要么本身是一个码字，要么与某个码字只差一次翻转。

由于有三个奇偶约束，每个约束可能被违反也可能不被违反，因此共有 $2\times2\times2 = 8$ 个不同的 syndrome。它们可以分成：七个非零 syndrome——每个对应一种单比特错误模式——以及全零 syndrome，对应无噪声的情形。

<span style="color:#1e8449;">**[译注]**</span> **syndrome 把 $2^7$ 个可能接收向量压成 8 类，靠的是 $H$ 是线性映射——这就是 Strang 的维数公式在纠错码里的样子**

$z=Hr\in\mathbb{F}_2^3$。$\ker H$ 的维数是 $7-3=4$（就是那 16 个码字），而 $z$ 只取 8 个值，于是 $2^7=128$ 个接收向量被切成 8 个**大小相等**的类（每个 16 个向量），每类共享同一个 syndrome。解码器要做的只是查一张 8 行的表：$z\mapsto$ 最可能的噪声模式。

为什么这个压缩是合法的：$H(r+n)=Hr+Hn$，噪声与数据在同一条线性通道上相加，所以「接收向量长什么样」可以拆成「数据部分（被 $\ker H$ 吸收）」+「噪声部分（由 $z$ 标记）」。抽掉线性（换一个非线性码），syndrome 这个同态就没了，解码只能枚举全部 $2^7$ 个候选——这正是 §1.2 末尾「一般线性码的 syndrome 解码」能推广、而任意码不能的原因。

挂载两个真同构：① Strang 的 $\dim\ker A+\dim\operatorname{im}A=n$ 在这里就是 $4+3=7$；② 6.042J 的**等价关系与划分**：$x\sim y\iff Hx=Hy$ 是等价关系，8 个 syndrome 就是 8 个等价类，$\mathbb{F}_2^7/\ker H$ 是一个 partition——查表解码就是在 partition 上取值。这两条不是类比，是同一件事的不同语言。

坐标：§1.2 syndrome 解码（原书 p.11–13，PDF p.23–25），Algorithm 1.16 与 parity-check matrix $H=[-P\mid I_3]$；8 个 syndrome 的分类在原书 p.13。


最优解码器在 syndrome 为零时不做任何动作，否则就利用这张「非零 syndrome → 单比特错误模式」的映射表，把可疑比特翻回去。



> <span style="color:#7f8c8d;">原书 p.13｜block error 与 bit error 概率（式 1.33–1.34）、图 1.17、习题 1.5–1.8、code 性能小结</span>

如果四个解码比特 $\hat{s}_1, \hat{s}_2, \hat{s}_3, \hat{s}_4$ 不全与源比特 $s_1, s_2, s_3, s_4$ 相符，就发生了一次 decoding error（解码错误）。block error probability（块错误概率）$p_B$ 是一个块中有一个或多个解码比特未能与对应源比特相符的概率：

```math
p_B = P(\hat{s} \neq s). \qquad (1.33)
```

bit error probability（比特错误概率）$p_b$ 是一个解码比特未能与对应源比特相符的平均概率：

```math
p_b = \frac{1}{K}\sum_{k=1}^{K} P(\hat{s}^{k} \neq s^{k}). \qquad (1.34)
```

在 Hamming 码的情形中，只要噪声在七个比特的块中翻转了不止一个比特，就会发生解码错误。于是块错误概率就是块中有两个或更多比特被翻转的概率。这个概率按 $O(f^{2})$ 的规模变化，和重复码 `R3` 的误码概率一样。但要注意，Hamming 码以更高的 rate（码率）通信，$R = 4/7$。

图 1.17 展示了一幅二值图像在 binary symmetric channel（二元对称信道）上用 (7, 4) Hamming 码传输的结果。约 7% 的解码比特出错。注意这些错误是相关的：常常有两三个相邻的解码比特被翻转。

[Figure 1.17：用 (7, 4) Hamming 码把 10 000 个源比特通过 $f = 10\%$ 的 binary symmetric channel 传输的完整链路示意（`s → encoder → t → channel → r → decoder → ŝ`），并配有解码后的图像。它演示的是：与图 1.11 的 `R3` 相比，Hamming 码的码率提高到 $4/7$，但解码后的比特错误概率不降反升，约为 7%——错误还倾向于成串出现。]

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.5.[1 ]**</span> This exercise and the next three refer to the (7, 4) Hamming code. Decode the received strings:

(a) $r = 1101011$
(b) $r = 0110110$
(c) $r = 0100111$
(d) $r = 1111111$.

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.6.[2, p.17]**</span> (a) Calculate the probability of block error $p_B$ of the (7, 4) Hamming code as a function of the noise level $f$ and show that to leading order it goes as $21f^{2}$.

(b) **[$3$ ]** Show that to leading order the probability of bit error $p_b$ goes as $9f^{2}$.

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.7.[2, p.19]**</span> Find some noise vectors that give the all-zero syndrome (that is, noise vectors that leave all the parity checks unviolated). How many such noise vectors are there?

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.8.[2 ]**</span> I asserted above that a block decoding error will result whenever two or more bits are flipped in a single block. Show that this is indeed so. [In principle, there might be error patterns that, after decoding, led only to the corruption of the parity bits, with no source bits incorrectly decoded.]

### Summary of codes' performances（各种码的性能小结）

图 1.18 展示了重复码与 Hamming 码的性能。它还展示了一族线性分组码的性能，这族码是 Hamming 码的推广，称为 BCH codes（BCH 码）。

这张图表明，我们可以用线性分组码取得比重复码更好的性能；但渐近情形看上去仍然不妙。



> <span style="color:#7f8c8d;">原书 p.14｜图 1.18、习题 1.9–1.11、§1.3 开头</span>

[Figure 1.18：repetition codes、$(7,4)$ Hamming 码与 BCH codes 在 $f = 0.1$ 的 binary symmetric channel 上 error probability $p_b$ 对 rate $R$ 的关系图，左右两幅分别是线性纵轴与对数纵轴。左图纵轴 $p_b \in [0, 0.1]$，标出 $R1$、$R5$、$R3$ 与 $H(7,4)$；右图纵轴为对数刻度，标出 $H(7,4)$、$BCH(15,7)$、$BCH(31,16)$、$BCH(511,76)$、$BCH(1023,101)$。两图都标 `more useful codes`（更有用的码）指向右下方。它演示的是：BCH 码族随块长增大越来越靠近右下方（码率与 $p_b$ 同时改善），但在给定的 $R$ 上 $p_b$ 仍随块长增大而缓慢恶化——渐近上仍看不到 $p_b \to 0$ 的希望，这正是 §1.3 要问的问题。]

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.9.[4, p.19]**</span> Design an error-correcting code and a decoding algorithm for it, estimate its probability of error, and add it to figure 1.18. [Don't worry if you find it difficult to make a code better than the Hamming code, or if you find it difficult to find a good decoder for your code; that's the point of this exercise.]

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.10.[3, p.20]**</span> A (7, 4) Hamming code can correct any one error; might there be a (14, 8) code that can correct any two errors?

Optional extra: Does the answer to this question depend on whether the code is linear or nonlinear?

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.11.[4, p.21]**</span> Design an error-correcting code, other than a repetition code, that can correct any two errors in a block of size $N$.

## 1.3 What performance can the best codes achieve?（最好的码能达到什么性能？）

看起来，在解码后的 bit-error probability（比特错误概率）$p_b$（我们想压低它）与 rate（码率）$R$（我们想保持它大）之间有一种权衡。这种权衡如何刻画？$(R, p_b)$ 平面中哪些点是可达的？这个问题由 Claude Shannon 在他 1948 年的开创性论文中提出，在那篇论文里他既创立了 information theory（信息论）这门学科，又解决了它的大部分基本问题。

在那个时候，人们普遍相信 $(R, p_b)$ 平面中「可达」与「不可达」点之间的边界是一条经过原点的曲线 $(R, p_b) = (0,0)$；若果真如此，那么为了达到 vanishingly small（趋于零的）错误概率 $p_b$，就必须把码率相应地压到接近零。「No pain, no gain.（没有付出就没有收获。）」

然而 Shannon 证明了一个非凡的结果：可达点与不可达点之间的边界在 $R$ 轴上相交于一个非零值 $R = C$，如图 1.19 所示。对任意信道，都存在一些码，使得以非零码率通信时错误概率 $p_b$ 可以任意小。本书的前半部分（第 I–III 部分）将致力于理解这个非凡的结果，它被称为 noisy-channel coding theorem（带噪信道编码定理）。

### Example: $f = 0.1$（例：$f = 0.1$）

能以任意小的 $p_b$ 进行通信的最大码率，称为信道的 capacity（容量）。噪声水平为 $f$ 的 binary symmetric channel 的容量公式是



> <span style="color:#7f8c8d;">原书 p.15｜图 1.19、容量公式 (1.35)、Shannon 的「两碟」对话、§1.4 Summary</span>

[Figure 1.19：Shannon noisy-channel coding theorem（带噪信道编码定理）的示意图，即 $f = 0.1$ 的 binary symmetric channel 上可达 $(R, p_b)$ 区域的边界。实线曲线即 Shannon limit（Shannon 极限），曲线左侧标注 `achievable`（可达）、右侧标注 `not achievable`（不可达），曲线与 $R$ 轴交于 $R = C \simeq 0.53$；图中还标出 $R1$、$R3$、$R5$、$H(7,4)$ 等教科书码的位置；左右两幅分别为线性与对数纵轴。图注给出定界曲线的方程 $R = C/(1 - H_2(p_b))$，其中 $C$ 与 $H_2$ 由式 (1.35) 定义。它演示的是：与图 1.18 相比，$p_b \to 0$ 时 $R$ 并不趋于 0，而是趋于一个正的 $C$——所有教科书码都离这条极限曲线很远。]

```math
C(f) = 1 - H_2(f) = 1 - \left[f\log_2\frac{1}{f} + (1-f)\log_2\frac{1}{1-f}\right]; \qquad (1.35)
```

我们前面讨论的噪声水平 $f = 0.1$ 的那个信道，容量是 $C \simeq 0.53$。让我们看看这在带噪磁盘驱动器上意味着什么。重复码 `R3` 能以 $R = 1/3$ 的码率在这个信道上以 $p_b = 0.03$ 通信。所以我们知道如何从三块带噪的 1 gigabyte（吉字节）驱动器造出一块 $p_b = 0.03$ 的 1 吉字节磁盘驱动器。我们也知道如何从六十块带噪的 1 吉字节驱动器造出一块 $p_b \simeq 10^{-15}$ 的 1 吉字节驱动器（习题 1.3，p.8）。而现在 Shannon 路过，看见我们在摆弄磁盘驱动器和码，说道：

> <span style="color:#7f8c8d;">「你想达到什么性能？$10^{-15}$？你不需要六十块磁盘驱动器——你只要两块驱动器就能拿到那个性能（因为 $1/2$ 小于 $0.53$）。而如果你想要 $p_b = 10^{-18}$ 或者 $10^{-24}$ 或者随便多少，你也用两块驱动器就能做到！」</span>

[严格地说，上面这些话未必完全正确，因为正如我们将看到的，Shannon 证明他的 noisy-channel coding theorem 时研究的是块长不断增大的 block code 序列，而所需的块长可能比 1 gigabyte（我们磁盘驱动器的大小）还大；在那种情形下，Shannon 也许会说：「好吧，用那些小磁盘驱动器你做不到，但如果你有两块带噪的 1 terabyte（太字节）驱动器，你就能用它们造出一块高质量 1 太字节驱动器。」]

## 1.4 Summary（小结）

### The (7, 4) Hamming Code（(7, 4) Hamming 码）

通过在一个 7 比特的块中纳入三个 parity-check bits（奇偶校验比特），就可能检测并纠正每个块中的任意单比特错误。

### Shannon's noisy-channel coding theorem（Shannon 带噪信道编码定理）

信息可以以非零的码率、以任意小的错误概率在带噪信道上传输。

<span style="color:#1e8449;">**[译注]**</span> **这句小结故意把两条断言压成一句：$R<C$ 可行、$R>C$ 不可行——后半句才是信息论真正独特的地方**

「可以以非零的码率、以任意小的错误概率传输」只说了一半。定理的第二半是**converse**：$R>C$ 时 $P_e$ 有正下界（§10.5 给出不可达区域）。抽掉 converse，信息论就退化成「存在好码」的构造性陈述，无法回答「为什么 $f=0.1$ 时 $R_9$ 再努力也只能到 $1/9$ 而 $C\approx0.5$ 却可达」这类反直觉事实——注意 $R_9$ 的码率 $1/9\approx0.111$ 远低于 $C$，它性能差不是因为违反 capacity，而是因为**具体码没到极限**。区分「定理的上界」与「某个码的表现」是这一章最容易混的地方。

数值对照（$f=0.1$，BSC）：$C=1-H_2(0.1)=1-0.469=0.531$ bit/use；$R_9$ 用 9 次通道传 1 bit，即 $0.111$；Hamming(7,4) 是 $0.571>C$，所以它**必然**有不可消除的错误率（实际 $\approx 1.5\times10^{-2}$ 量级），这不是码设计得不好，是越界了。

挂载：6.006 里「算法下界 vs 某个算法的复杂度」是同一种区分（比较排序 $\Omega(n\log n)$ 是下界，冒泡的 $O(n^2)$ 只是某个算法）；Thomson 实分析的 $\sup$/$\max$ 之别同样在此显形。

坐标：§1.4 小结（原书 p.16，PDF p.28）；完整证明在 §10（原书 p.149–160，PDF p.161–172），converse 与 Fano 不等式见 §10.5。



> <span style="color:#7f8c8d;">原书 p.16｜§1.4 小结续、§1.5 进阶习题（习题 1.12）、§1.6 解答开始</span>

information theory（信息论）既讨论通信的局限，也讨论通信的可能性。noisy-channel coding theorem（带噪信道编码定理）——我们将在第 10 章证明它——同时断言：在高于容量的任何码率上，可靠通信是不可能的；而在直到容量的所有码率上，可靠通信都是可能的。

接下来的几章将通过讨论如何度量 information content（信息含量），以及与之紧密相关的 data compression（数据压缩）主题，为这个结果打下基础。

## 1.5 Further exercises（进阶习题）

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 1.12.[2, p.21]**</span> Consider the repetition code $R_9$. One way of viewing this code is as a concatenation of $R_3$ with $R_3$. We first encode the source stream with $R_3$, then encode the resulting output with $R_3$. We could call this code `$R_3^{2}$'. This idea motivates an alternative decoding algorithm, in which we decode the bits three at a time using the decoder for $R_3$; then decode the decoded bits from that first decoder using the decoder for $R_3$.

Evaluate the probability of error for this decoder and compare it with the probability of error for the optimal decoder for $R_9$.

Do the concatenated encoder and decoder for $R_3^{2}$ have advantages over those for $R_9$?

## 1.6 Solutions（解答）

**Solution to exercise 1.2 (p.7).（习题 1.2 的解答）** 如果三个比特的块中有两个或更多比特被翻转，`R3` 就会犯错。所以 `R3` 的误码概率是两项之和：三个比特全被翻转的概率 $f^{3}$；以及恰好两个比特被翻转的概率 $3f^{2}(1-f)$。[如果这些表达式不显然，见例 1.1（p.1）：它们就是 $P(r = 3 \mid f, N = 3)$ 与 $P(r = 2 \mid f, N = 3)$。]

```math
p_b = p_B = 3f^{2}(1-f) + f^{3} = 3f^{2} - 2f^{3}. \qquad (1.36)
```

当 $f$ 小时，这个概率由 $3f^{2}$ 这一项主导。

关于这个问题的进一步讨论，见习题 2.38（p.39）。

**Solution to exercise 1.3 (p.8).（习题 1.3 的解答）** 重复码 $R_N$ 的误码概率，由 $N/2$ 个比特被翻转的概率主导，对奇数 $N$ 它按如下规模变化：

```math
\binom{N}{N/2} f^{N/2}(1-f)^{N/2}. \qquad (1.37)
```

> <span style="color:#7f8c8d;">边注：Notation: $\lfloor N/2 \rfloor$ denotes the smallest integer greater than or equal to $N/2$.（记号：$\lfloor N/2 \rfloor$ 表示不小于 $N/2$ 的最小整数。）</span>

项 $\binom{N}{K}$ 可以用 binary entropy function（二元熵函数）来近似：

```math
\frac{1}{N+1}2^{NH_2(K/N)} \le \binom{N}{K} \le 2^{NH_2(K/N)}, \qquad (1.38)
```

其中这个近似引入的误差是 $O(N^{-1/2})$ 量级的，如方程 (1.17) 所示。于是

```math
p_b = p_B \simeq 2^{N}\left(f(1-f)\right)^{N/2} = \left(4f(1-f)\right)^{N/2}. \qquad (1.39)
```

令它等于所需的数值 $10^{-15}$，我们求得 $N \simeq \frac{2\log 10^{-15}}{\log 4f(1-f)} = 68$。

这个答案偏了一点，因为我们所用的近似高估了 $\binom{N}{K}$，而且我们没有区分 $\lfloor N/2 \rfloor$ 与 $N/2$。



> <span style="color:#7f8c8d;">原书 p.17｜习题 1.3 解答续（迭代求 $N \approx 61$）、习题 1.6 解答开始</span>

一个稍微更仔细的答案（不显式做数值计算）如下。把 $\binom{N}{K}$ 的近似取到下一阶，我们得到：

```math
\binom{N}{N/2} \simeq 2^{N}\sqrt{\frac{2}{\pi N}}. \qquad (1.40)
```

这个近似可以从精确版的 Stirling 近似 (1.12) 证明，也可以通过考虑 $p = 1/2$ 的 binomial distribution（二项分布）并注意到

```math
1 = \sum_{K}\binom{N}{K}2^{-N} \simeq \binom{N}{N/2}2^{-N}\sum_{r=-N/2}^{N/2} e^{-r^{2}/2\sigma^{2}} \simeq \binom{N}{N/2}2^{-N}\sqrt{2\pi\sigma^{2}}, \qquad (1.41)
```

其中 $\sigma^{2} = N/4$，由此得到方程 (1.40)。在这一项里，$\lfloor N/2 \rfloor$ 与 $N/2$ 的区别并不重要，因为 $\binom{N}{K}$ 在 $K = N/2$ 处取最大值。

于是（对奇数 $N$）误码概率的主导阶为

```math
p_b \simeq N\binom{N}{(N+1)/2} f^{(N+1)/2}(1-f)^{(N-1)/2} \qquad (1.42)
```

```math
\simeq 2^{N}\sqrt{\frac{2}{\pi N/2}}\; f\left[f(1-f)\right]^{(N-1)/2} \simeq \frac{1}{\sqrt{\pi N/8}}\, f\left[4f(1-f)\right]^{(N-1)/2}. \qquad (1.43)
```

方程 $p_b = 10^{-15}$ 可以写成

```math
\frac{(N-1)}{2} \simeq \frac{\log 10^{-15} + \log\sqrt{\pi N/8}}{\log 4f(1-f)}, \qquad (1.44)
```

> <span style="color:#7f8c8d;">边注：In equation (1.44), the logarithms can be taken to any base, as long as it's the same base throughout. In equation (1.45), I use base 10.（在方程 (1.44) 中，对数可以取任意底，只要全式底数一致。在方程 (1.45) 中我用以 10 为底。）</span>

它可以对 $N$ 迭代求解，第一次迭代从 $\hat{N}^{(1)} = 68$ 开始：

```math
\frac{(\hat{N}^{(2)} - 1)}{2} \simeq \frac{-15 + 1.7}{-0.44} \simeq 29.9 \quad \Rightarrow \quad \hat{N}^{(2)} \simeq 60.9. \qquad (1.45)
```

这个答案被证明是稳定的，所以 $N \simeq 61$ 就是使 $p_b \simeq 10^{-15}$ 的块长。

**Solution to exercise 1.6 (p.13).（习题 1.6 的解答）**

(a) Hamming 码的块错误概率是六项之和——即一个块中出现 2、3、4、5、6 或 7 个错误的概率。

```math
p_B = \sum_{r=2}^{7}\binom{7}{r} f^{r}(1-f)^{7-r}. \qquad (1.46)
```

到主导阶，它按如下规模变化：

```math
p_B \simeq \binom{7}{2} f^{2} = 21f^{2}. \qquad (1.47)
```

(b) Hamming 码的比特错误概率小于块错误概率，因为一次块错误很少会破坏解码块中的所有比特。主导阶行为可以通过考察最可能的情形——噪声向量的 weight（重量）为二——的结果来得到。解码器会错误地再翻转第三个比特，于是被修改过的接收向量（长度 7）与发送向量在三个比特上不同。也就是说，如果我们对全部七个比特取平均，那么一个随机选中的比特被翻转的概率，到主导阶，是块错误概率的 $3/7$ 倍。现在，我们真正关心的是



> <span style="color:#7f8c8d;">原书 p.18｜习题 1.6 解答续、Hamming 码的对称性证明（式 1.49–1.53）</span>

一个源比特被翻转的概率。在这三个被翻转的比特中，parity bits（奇偶校验比特）与源比特谁更可能？还是说当噪声向量重量为二时，七个比特同样可能被破坏？Hamming 码在它对这七个比特提供的保护上，实际上是完全对称的（假设是 binary symmetric channel（二元对称信道））。[这个对称性可以这样证明：说明一个奇偶校验比特的角色可以与一个源比特交换，而所得出的码仍然是一个 (7, 4) Hamming 码；见下文。]任何一个比特最终被破坏的概率，对全部七个比特都相同。所以（对源比特而言的）比特错误概率，就是块错误概率的七分之三。

```math
p_b \simeq \frac{3}{7}p_B \simeq 9f^{2}. \qquad (1.48)
```

### Symmetry of the Hamming (7, 4) code（Hamming (7, 4) 码的对称性）

为了证明 (7, 4) 码对所有比特的保护是均等的，我们从 parity-check matrix（奇偶校验矩阵）

```math
H =
\begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 1 & 0 & 0 & 1
\end{bmatrix}. \qquad (1.49)
```

出发。若用 permutation（置换）$(t_1t_2t_3t_4t_5t_6t_7) \to (t_5t_2t_3t_4t_1t_6t_7)$ 重排这七个比特，则七个发送比特之间的对称性最容易看出来。于是我们可以把 $H$ 重写为：

```math
H =
\begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 1
\end{bmatrix}. \qquad (1.50)
```

现在，如果我们取 $t$ 所满足的任意两个奇偶约束并把它们相加，就得到另一个奇偶约束。例如，第一行断言 $t_5 + t_2 + t_3 + t_1 = \text{even}$，第二行断言 $t_2 + t_3 + t_4 + t_6 = \text{even}$，而这两个约束之和是

```math
t_5 + 2t_2 + 2t_3 + t_1 + t_4 + t_6 = \text{even}; \qquad (1.51)
```

我们可以丢掉 $2t_2$ 与 $2t_3$ 这两项，因为无论 $t_2$、$t_3$ 取什么，它们都是偶的；于是我们推出了奇偶约束 $t_5 + t_1 + t_4 + t_6 = \text{even}$，如果愿意的话，我们可以把它作为第四行加进奇偶校验矩阵。[满足 $Ht = 0$ 的向量集合不会改变。]于是我们定义

```math
H =
\begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 1 & 0
\end{bmatrix}. \qquad (1.52)
```

第四行是上面两行之和（模二）。注意第二、三、四行都是第一行的 cyclic shifts（循环移位）。如果在加入这第四个冗余约束之后，我们把第一个约束丢掉，就得到一个新的奇偶校验矩阵 $H'$：

```math
H' =
\begin{bmatrix}
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 1 & 0
\end{bmatrix}, \qquad (1.53)
```

它对所有码字仍然满足 $H't = 0$，而且它看上去就像 (1.50) 中起始的 $H$，只不过所有列都向右移动了一



> <span style="color:#7f8c8d;">原书 p.19｜对称性证明续、cyclic codes、习题 1.7 与 1.9 解答（图 1.20）</span>

位，而最右边那一列从左端重新出现（各列的一个 cyclic permutation（循环置换））。

这就建立了七个比特之间的对称性。把上述步骤再重复五次，我们可以为同一个原始码一共造出七个不同的 $H$ 矩阵，每一个都把各个比特指派到不同的角色上。

我们也可以为这个码构造超级冗余的七行奇偶校验矩阵

```math
H'' =
\begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 1 & 0 \\
0 & 1 & 0 & 0 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 0 & 0 & 1
\end{bmatrix}. \qquad (1.54)
```

这个矩阵是「冗余的」，意思是它的各行张成的空间只有三维，而不是七维。

这个矩阵也是一个 cyclic matrix（循环矩阵）。每一行都是第一行的循环置换。

> <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition（定义）——Cyclic codes（循环码）.**</span> 如果在比特 $t_1 \ldots t_N$ 上存在某种排序，使得一个线性码具有循环的奇偶校验矩阵，那么这个码就被称为 cyclic code（循环码）。
>
> 这类码的码字也具有循环性质：一个码字的任意循环置换仍是一个码字。
>
> 例如，Hamming (7, 4) 码在按上面那种方式排序比特时，由码字 `1110100` 与 `1011000` 的全部七个循环移位、以及码字 `0000000` 与 `1111111` 组成。

循环码是纠错码代数方法的基石。不过本书后面不会再使用它们，因为它们已经被 sparse-graph codes（稀疏图码）取代了（第 VI 部分）。

**Solution to exercise 1.7 (p.13).（习题 1.7 的解答）** 有十五个非零噪声向量给出全零 syndrome；它们恰好就是 Hamming 码的十五个非零码字。注意：由于 Hamming 码是线性的，任意两个码字之和仍是码字。

### Graphs corresponding to codes（与码对应的图）

[Figure 1.20：(7, 4) Hamming 码的图表示：7 个圆代表 bit nodes（比特节点），3 个方块代表 parity-check nodes（奇偶校验节点）；每个方块与它那一个奇偶校验所涉及的那四个比特相连，图中的边只存在于圆与方块之间。它演示的是：这个 bipartite graph（二分图）与奇偶校验矩阵 (1.30) 一一对应——方块对应 $H$ 的行，圆对应 $H$ 的列，$H$ 中的每个 1 对应一条边。]

**Solution to exercise 1.9 (p.14).（习题 1.9 的解答）** 回答这个问题时，你很可能会发现，发明新的码比给它们找到最优解码器要容易。设计码的办法有很多，下面只是其中一条思路。我们造一个与 (7, 4) Hamming 码相似、但更大的线性分组码。

许多码都可以方便地用图来表示。在图 1.13 中，我们引入了 (7, 4) Hamming 码的图形表示。如果我们把那张图中那些大圆——每一个都表示某四个特定比特的奇偶性为偶——换成与这四个比特相连的 parity-check node（奇偶校验节点），就得到如图 1.20 所示的 (7, 4) Hamming 码的 bipartite graph（二分图）表示。7 个圆是 7 个发送比特。3 个方块是奇偶校验节点（不要与 3 个奇偶校验比特混淆，后者是最外围的三个圆）。这个图是一个「二分」图，因为它的节点分成两类——比特与校验



> <span style="color:#7f8c8d;">原书 p.20｜dodecahedron code（图 1.21）、LDPC 码（图 1.22）、习题 1.10 解答开始</span>

——而边只存在于不同类的节点之间。图与码的奇偶校验矩阵 (1.30) 之间的关系很简单：每个奇偶校验节点对应 $H$ 的一行，每个比特节点对应 $H$ 的一列；$H$ 中每有一个 1，对应的一对节点之间就有一条边。

注意到线性码与图之间的这层联系之后，发明线性码的一种办法就是直接去想一个二分图。例如，把一个 dodecahedron（正十二面体）的顶点称为奇偶校验节点，并在正十二面体的每条棱上放一个发送比特，就得到一个漂亮的二分图。这个构造定义了一个奇偶校验矩阵，其中每一列的 weight（重量）为 2，每一行的重量为 3。[一个二进制向量的 weight（重量）是它所含 1 的个数。]

[Figure 1.21：定义 (30, 11) dodecahedron code（正十二面体码）的图。30 个圆是 30 个发送比特（放在正十二面体的棱上），20 个三角形是 20 个奇偶校验（对应顶点）。它演示的是：每个比特恰好参与两个校验（列重 2），每个校验恰好涉及三个比特（行重 3）；其中有一个奇偶校验是冗余的，所以独立约束只有 19 个。]

[Figure 1.22：一个 rate-1/4（码率 1/4）的 low-density parity-check code（低密度奇偶校验码，Gallager 码）的图，块长 $N = 16$，奇偶校验约束 $M = 12$。每个白圆代表一个发送比特，每个比特参与 $j = 3$ 个由方块表示的约束，节点之间的边是随机放置的。它演示的是：好的线性码其图通常比正十二面体的图纠缠得多，无法平铺在平面上。（更多内容见第 47 章。）]

这个码有 $N = 30$ 个比特，看起来有 $M_{\text{apparent}} = 20$ 个奇偶校验约束。实际上只有 $M = 19$ 个独立约束；第 20 个约束是冗余的（也就是说，如果 19 个约束被满足，第 20 个就自动被满足）；因此源比特数目是 $K = N - M = 11$。这个码是一个 (30, 11) 码。

为这个码找到解码算法很难，但我们可以通过找出它最低重量的码字来估计它的错误概率。如果我们把原正十二面体某一个面周围的所有比特都翻转，那么所有奇偶校验都会被满足；所以这个码有 12 个重量为 5 的码字，每个面对应一个。既然最低重量的码字重量为 5，我们就说这个码的 distance（距离）为 $d = 5$；(7, 4) Hamming 码的距离为 3，能够纠正所有的单比特翻转错误。距离为 5 的码可以纠正所有双比特翻转错误，但有一些三比特翻转错误它纠正不了。所以这个码的错误概率（假设是 binary symmetric channel（二元对称信道））至少对低噪声水平 $f$ 而言，将由一个 $f^{3}$ 阶的项主导，或许大致是

```math
12\binom{5}{3} f^{3}(1-f)^{27}. \qquad (1.55)
```

当然，并没有义务去造那些图能够像这个码一样画在平面上的码；最好的线性码虽然有简洁的图描述，但它们的图更纠缠，就像图 1.22 那个微小的 (16, 4) 码所展示的那样。

此外，也没有理由只固守线性码；确实有些 nonlinear codes（非线性码）——其码字不能由像 $Ht = 0$ 这样的线性方程定义——具有非常好的性质。但是非线性码的编码与解码是更棘手的任务。

**Solution to exercise 1.10 (p.14).（习题 1.10 的解答）** 首先让我们假设我们造的是线性码，并用 syndrome decoding（伴随式解码）来解它。如果有 $N$ 个发送比特，那么重量不超过二的可能的错误模式数目是

```math
\binom{N}{2} + \binom{N}{1} + \binom{N}{0}. \qquad (1.56)
```

对 $N = 14$，那是 $91 + 14 + 1 = 106$ 个模式。现在，每一个可区分的错误模式都必须产生一个不同的 syndrome；而 syndrome 是一个 $M$ 比特的列表，所以 syndrome 的最大可能数目是 $2^{M}$。对一个 (14, 8) 码，$M = 6$，所以最多有 $2^{6} = 64$ 个 syndrome。重量不超过二的错误模式数目 106 大于 syndrome 的数目 64，所以我们可以立即排除存在一个能纠正两个错误的 (14, 8) 码的可能性。



> <span style="color:#7f8c8d;">原书 p.21｜计数论证（式 1.57–1.58）、习题 1.11 与 1.12 的解答（concatenated codes）</span>

同样的计数论证对非线性码也完全适用。当解码器收到 $r = t + n$ 时，它的目标是从 $r$ 同时推断出 $t$ 与 $n$。如果发送方可以从一个大小为 $S_t$ 的码中任选一个发送向量 $t$，而信道可以从一个大小为 $S_n$ 的集合中任选一个噪声向量，并且这两个选择都能从接收到的比特串 $r$（它只是至多 $2^{N}$ 个可能串之一）中恢复出来，那么必然有

```math
S_t S_n \le 2^{N}. \qquad (1.57)
```

于是，对一个 $(N, K)$ 的能纠正两个错误的码，无论线性还是非线性，都有

```math
2^{K}\left[\binom{N}{2} + \binom{N}{1} + \binom{N}{0}\right] \le 2^{N}. \qquad (1.58)
```

**Solution to exercise 1.11 (p.14).（习题 1.11 的解答）** 造能纠正多个错误的码有各种策略，我强烈建议你自己想出一两个来。

如果你的办法使用线性码，例如一个带 $M$ 个奇偶校验的码，那么记住上一题给出的计数论证会很有帮助，以便预估你可能需要多少个奇偶校验 $M$。

能纠正任意两个错误的码的例子，有 p.20 的 (30, 11) dodecahedron code（正十二面体码），以及将在 p.221 引入的 (15, 6) pentagonful code（五边形码）。关于如何从只能纠正一个错误的码造出能纠正多个错误的码，还有若干简单的想法，在 §13.7 讨论。

**Solution to exercise 1.12 (p.16).（习题 1.12 的解答）** $R_3^{2}$ 的误码概率，到主导阶，是

```math
p_b(R_3^{2}) \simeq 3\left[p_b(R_3)\right]^{2} = 3(3f^{2})^{2} + \cdots = 27f^{4} + \cdots, \qquad (1.59)
```

而 $R_9$ 的误码概率由五个比特被翻转的概率主导：

```math
p_b(R_9) \simeq \binom{9}{5} f^{5}(1-f)^{4} \simeq 126f^{5} + \cdots. \qquad (1.60)
```

因此 $R_3^{2}$ 的解码过程是次优的，因为存在重量为四的噪声向量会使它发生解码错误。

然而它的优点是所需的计算资源更小：只需记住三个比特、并数到三，而不是数到九。

这个简单的码说明了一个重要的概念。concatenated codes（级联码）在实践中被广泛使用，因为 concatenation（级联）允许用简单的编码与解码硬件来实现大的码。一些最著名的实用码就是级联码。



> <span style="color:#7f8c8d;">原书 p.22｜第 2 章 Probability, Entropy, and Inference 开篇与 §2.1(Probabilities and ensembles)</span>

# 2 Probability, Entropy, and Inference（概率、熵与推断）

本章及其姊妹章第 8 章要花一些篇幅讨论记号。正如 White Knight（白骑士）区分了歌、歌的名字、以及歌的名字的称呼（Carroll, 1998），我们有时也需要小心区分：一个 random variable（随机变量）、该随机变量的取值、以及断言该随机变量取某个特定值的 proposition（命题）。不过在任何一个具体的章节里，我都会使用尽可能简单友好的记号，即使冒着惹恼纯正读者的风险。例如，如果某件事「以概率 1 为真」，我通常就简单地说它「为真」。

[Figure 2.1：一个英语言文档中随机选取一个字母时 27 个结果上的 probability distribution（概率分布），以白色方块面积表示各结果的概率。表中列出 $i$、字母 $a_i$ 与概率 $p_i$：a 0.0575、b 0.0128、c 0.0263、d 0.0285、e 0.0913、f 0.0173、g 0.0133、h 0.0313、i 0.0599、j 0.0006、k 0.0084、l 0.0335、m 0.0235、n 0.0596、o 0.0689、p 0.0192、q 0.0008、r 0.0508、s 0.0567、t 0.0706、u 0.0334、v 0.0069、w 0.0119、x 0.0073、y 0.0164、z 0.0007、空格 0.1928（这些数值估计自 *The Frequently Asked Questions Manual for Linux*）。它演示的是：27 个可能字母（a–z 加一个空格字符 `-`）上确实存在一个高度不均匀的分布——空格的频率几乎是任何字母的三倍，而 j、q、z 的频率低到千分之一量级。]

## 2.1 Probabilities and ensembles（概率与 ensemble）

> <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition（定义）：Ensemble.**</span> 一个 ensemble $X$ 是一个三元组 $(x, A_X, P_X)$，其中 outcome（结果）$x$ 是一个 random variable（随机变量）的取值，该随机变量取一组可能值之一，$A_X = \{a_1, a_2, \ldots, a_i, \ldots, a_I\}$，各值对应的概率为 $P_X = \{p_1, p_2, \ldots, p_I\}$，且 $P(x = a_i) = p_i$，$p_i \ge 0$，以及 $\sum_{a_i \in A_X} P(x = a_i) = 1$。

名字 $A$ 是「alphabet（字母表）」的助记。ensemble 的一个例子是从一个英语言文档中随机选出的一个字母。这个 ensemble 如图 2.1 所示。共有二十七个可能的字母：a–z，加上一个空格字符 `-`。

> <span style="color:#7f8c8d;">**Abbreviations（缩写）.** 有时会用更简短的记号。例如 $P(x = a_i)$ 可以写成 $P(a_i)$ 或 $P(x)$。</span>

> <span style="color:#7f8c8d;">**Probability of a subset（子集的概率）.** 如果 $T$ 是 $A_X$ 的一个子集，那么：</span>

```math
P(T) = P(x \in T) = \sum_{a_i \in T} P(x = a_i). \qquad (2.1)
```

例如，如果我们把图 2.1 中的元音定义为 $V$，即 $V = \{a, e, i, o, u\}$，那么

```math
P(V) = 0.06 + 0.09 + 0.06 + 0.07 + 0.03 = 0.31. \qquad (2.2)
```

> <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition（定义）——Joint ensemble（联合 ensemble）.**</span> 一个 joint ensemble $XY$ 是一个 ensemble，其中每个 outcome 是一个有序对 $x, y$，$x \in A_X = \{a_1, \ldots, a_I\}$，$y \in A_Y = \{b_1, \ldots, b_J\}$。
> 我们把 $P(x, y)$ 称为 $x$ 与 $y$ 的 joint probability（联合概率）。
> 写有序对时逗号是可选的，所以 $xy \equiv x, y$。
> **N.B.** 在联合 ensemble $XY$ 中，两个变量未必独立。



> <span style="color:#7f8c8d;">原书 p.23｜图 2.2（bigram 分布）、marginal probability、conditional probability、例 2.1</span>

[Figure 2.2：一个英语言文档（*The Frequently Asked Questions Manual for Linux*）中 27×27 个可能的 bigrams（双字母组）$xy$ 上的概率分布，横轴为第二个字母 $y$（a–z 与空格），纵轴为第一个字母 $x$（同）。它演示的是：bigram 分布远不像单字母分布那样均匀——大部分概率质量集中在少数格子上（例如 `q` 后面几乎总是 `u`，空格前后的字母组合有强偏好），这正是「相邻字母不独立」的可视证据。]

> <span style="color:#7f8c8d;">**Marginal probability（边缘概率）.** 我们可以用求和从联合概率 $P(x, y)$ 得到边缘概率 $P(x)$：</span>

```math
P(x = a_i) = \sum_{y \in A_Y} P(x = a_i, y). \qquad (2.3)
```

同样地，用更简短的记号，$y$ 的边缘概率是：

```math
P(y) = \sum_{x \in A_X} P(x, y). \qquad (2.4)
```

### Conditional probability（条件概率）

```math
P(x = a_i \mid y = b_j) \equiv \frac{P(x = a_i, y = b_j)}{P(y = b_j)} \quad \text{if } P(y = b_j) \neq 0. \qquad (2.5)
```

[如果 $P(y = b_j) = 0$，那么 $P(x = a_i \mid y = b_j)$ 没有定义。]

我们把 $P(x = a_i \mid y = b_j)$ 读作「在 $y$ 等于 $b_j$ 的给定下，$x$ 等于 $a_i$ 的概率」。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 2.1（例 2.1）**</span> joint ensemble（联合 ensemble）的一个例子，是由一个英语言文档中两个相继字母组成的有序对 $XY$。可能的 outcome 是诸如 aa、ab、ac 以及 zz 这样的有序对；在它们之中，我们可以预料 ab 与 ac 比 aa 与 zz 更可能。对两个相邻字符的联合概率分布的一个估计，以图形方式画在图 2.2 中。

这个联合 ensemble 有一个特殊性质：它的两个边缘分布 $P(x)$ 与 $P(y)$ 完全相同。它们都等于图 2.1 所示的 monogram（单字母）分布。

从这个联合 ensemble $P(x, y)$ 出发，我们可以通过分别对行与列做归一化，得到条件分布 $P(y \mid x)$ 与 $P(x \mid y)$（图 2.3）。概率 $P(y \mid x = q)$ 是在给定第一个字母是 q 时第二个字母的概率分布。正如你在图 2.3a 中所见，在给定第一个字母 $x$ 是 q 时第二个字母 $y$ 的两个最可能的取值



> <span style="color:#7f8c8d;">原书 p.24｜图 2.3（条件分布）、product rule / sum rule / Bayes' theorem、independence、习题 2.2</span>

是 u 与 `-`（空格）。（q 后面常常跟空格，因为源文档大量使用了 FAQ 这个词。）

概率 $P(x \mid y = u)$ 是在给定第二个字母 $y$ 是 u 时第一个字母 $x$ 的概率分布。正如你在图 2.3b 中所见，在给定 $y = u$ 时 $x$ 的两个最可能的取值是 n 与 o。

[Figure 2.3：条件概率分布，两幅 27×27 的图。(a) $P(y \mid x)$：每一行给出 bigram $xy$ 中给定第一个字母 $x$ 时第二个字母 $y$ 的条件分布。(b) $P(x \mid y)$：每一列给出给定第二个字母 $y$ 时第一个字母 $x$ 的条件分布。它演示的是：条件化会显著集中概率质量——例如 $x = q$ 那一行只在 u 与空格上有显著质量，$y = u$ 那一列只在 n 与 o 上有显著质量。]

我们往往不直接写出联合概率，而是用一组条件概率来定义一个 ensemble。下列概率论法则会很有用。（$H$ 表示这些概率所基于的 assumptions（假设）。）

**Product rule（乘规则）**——由条件概率的定义得到：

```math
P(x, y \mid H) = P(x \mid y, H)P(y \mid H) = P(y \mid x, H)P(x \mid H). \qquad (2.6)
```

这条规则也叫 chain rule（链规则）。

**Sum rule（和规则）**——边缘概率定义的一个改写：

```math
P(x \mid H) = \sum_{y} P(x, y \mid H) \qquad (2.7)
```

```math
= \sum_{y} P(x \mid y, H)P(y \mid H). \qquad (2.8)
```

**Bayes' theorem（Bayes 定理）**——由乘规则得到：

```math
P(y \mid x, H) = \frac{P(x \mid y, H)P(y \mid H)}{P(x \mid H)} \qquad (2.9)
```

```math
= \frac{P(x \mid y, H)P(y \mid H)}{\sum_{y'} P(x \mid y', H)P(y' \mid H)}. \qquad (2.10)
```

> <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition（定义）——Independence（独立）.**</span> 两个随机变量 $X$ 与 $Y$ 独立（有时写作 $X \perp\!\!\!\perp Y$）当且仅当
>
> ```math
> P(x, y) = P(x)P(y). \qquad (2.11)
> ```

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 2.2.[1, p.40]**</span> Are the random variables X and Y in the joint ensemble of figure 2.2 independent?



> <span style="color:#7f8c8d;">原书 p.25｜例 2.3（疾病检测与 Bayes 定理）、§2.2 开头</span>

我说过，我们常常用一组条件概率来定义一个 ensemble。下面这个例子说明这个想法。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 2.3（例 2.3）**</span> Jo 有一种针对某种可怕疾病的检测。我们用变量 $a$ 表示 Jo 的健康状态，用 $b$ 表示检测结果。

```math
a = 1 \equiv \text{Jo has the disease} \qquad (2.12)
```

```math
a = 0 \equiv \text{Jo does not have the disease.}
```

检测结果要么是「阳性」（$b = 1$），要么是「阴性」（$b = 0$）；这个检测的可靠度是 95%：在真正患该病的人当中，有 95% 的情形返回阳性结果；在没有患该病的人当中，有 95% 的情形得到阴性结果。最后一条背景信息是：在 Jo 这个年龄与背景的人当中，有 1% 患有该病。

好——Jo 做了检测，结果是阳性。Jo 患该病的概率是多少？

**Solution（解）** 我们把所给的各项概率都写下来。检测的可靠度给出了给定 $a$ 时 $b$ 的条件概率：

```math
\begin{aligned}
P(b=1 \mid a=1) &= 0.95, &\quad P(b=1 \mid a=0) &= 0.05, \\
P(b=0 \mid a=1) &= 0.05, &\quad P(b=0 \mid a=0) &= 0.95;
\end{aligned} \qquad (2.13)
```

而疾病的流行率告诉我们 $a$ 的边缘概率：

```math
P(a=1) = 0.01, \qquad P(a=0) = 0.99. \qquad (2.14)
```

从边缘概率 $P(a)$ 与条件概率 $P(b \mid a)$，我们可以推出联合概率 $P(a, b) = P(a)P(b \mid a)$ 以及我们感兴趣的任何其他概率。例如，由和规则，$b = 1$ 的边缘概率——得到阳性结果的概率——是

```math
P(b=1) = P(b=1 \mid a=1)P(a=1) + P(b=1 \mid a=0)P(a=0). \qquad (2.15)
```

Jo 收到了阳性结果 $b = 1$，她关心的是她患该病（即 $a = 1$）这件事有多大可能。街上的普通人可能会被这句话骗住：「这个检测的可靠度是 95%，所以 Jo 的阳性结果意味着 Jo 患该病的概率是 95%」——但这是不正确的。推断问题的正确解法要用 Bayes' theorem（Bayes 定理）来求。

```math
P(a=1 \mid b=1) = \frac{P(b=1 \mid a=1)P(a=1)}{P(b=1 \mid a=1)P(a=1) + P(b=1 \mid a=0)P(a=0)} \qquad (2.16)
```

```math
= \frac{0.95 \times 0.01}{0.95 \times 0.01 + 0.05 \times 0.99} \qquad (2.17)
```

```math
= 0.16. \qquad (2.18)
```

所以，尽管结果是阳性，Jo 患该病的概率只有 16%。

## 2.2 The meaning of probability（概率的含义）

概率可以用两种方式来使用。

概率可以描述随机实验中结果的频率，但给「频率」和「随机」这两个词下非循环的定义是个挑战——说一枚抛出硬币出现正面的频率是 $1/2$ 究竟是什么意思？如果我们说这个频率是长序列中正面的平均比例，我们就得定义「平均」；而不用一个与概率同义的词，就很难定义「平均」！我不打算去解开这个哲学上的结。



> <span style="color:#7f8c8d;">原书 p.26｜Cox axioms（Box 2.4）、Bayesian viewpoint</span>

概率也可以更一般地用来描述对不涉及随机变量的命题的相信程度——例如「在给定证据的情况下，S 先生是 S 夫人凶手的概率」（他要么是、要么不是，陪审团的职责就是评估他作案有多大可能）；「Thomas Jefferson 与他的一个奴隶生下孩子的概率」；「Shakespeare 的剧作是 Francis Bacon 写的概率」；或者举一个当代的例子，「某张支票上的某个签名是真迹的概率」。

普通人对这两种使用概率的方式都很乐意，但有些概率论书籍把概率限制为只指可重复随机实验中结果的频率。

> <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition（定义）——Notation（记号）.**</span> 用 $B(x)$ 表示「对命题 $x$ 的相信程度」。$x$ 的否定（not-$x$）写作 $\bar{x}$。对条件命题「在假定命题 $y$ 为真的前提下 $x$」的相信程度，用 $B(x \mid y)$ 表示。
>
> **Axiom 1（公理 1）.** 相信程度可以排序；如果 $B(x)$ 比 $B(y)$「大」，且 $B(y)$ 比 $B(z)$「大」，那么 $B(x)$ 比 $B(z)$「大」。[推论：相信程度可以映射到实数上。]
>
> **Axiom 2（公理 2）.** 对命题 $x$ 及其否定 $\bar{x}$ 的相信程度是相互关联的。存在一个函数 $f$ 使得
>
> ```math
> B(\bar{x}) = f\left[B(x)\right].
> ```
>
> **Axiom 3（公理 3）.** 对命题 $x, y$ 的合取（$x$ 且 $y$）的相信程度，与对条件命题 $x \mid y$ 的相信程度、以及对命题 $y$ 的相信程度相互关联。存在一个函数 $g$ 使得
>
> ```math
> B(x, y) = g\left[B(x \mid y), B(y)\right].
> ```
>
> <span style="color:#7f8c8d;">Box 2.4 图注：The Cox axioms（Cox 公理）。如果一组信念满足这些公理，那么它们可以被映射到满足 $P(\text{false}) = 0$、$P(\text{true}) = 1$、$0 \le P(x) \le 1$ 以及概率诸规则的概率上：$P(\bar{x}) = 1 - P(x)$，以及 $P(x, y) = P(x \mid y)P(y)$。（Cox, 1946）</span>

尽管如此，只要相信程度满足称为 Cox axioms（Cox 公理）的简单一致性规则（Cox, 1946）（图 2.4），它们就可以被映射到概率上。因此概率可以用来描述 assumptions（假设），也可以用来描述在这些假设之下的 inferences（推断）。概率的规则保证：如果两个人作出相同的假设并收到相同的数据，那么他们会得出完全相同的结论。这种把概率更一般地用来量化信念的做法，称为 Bayesian viewpoint（Bayesian 观点）。它也被称为概率的主观解释，因为这些概率依赖于假设。拥护用 Bayesian 方法做数据建模与模式识别的人并不把这种主观性看作缺陷，因为在他们看来，

> 你不作假设就无法做推断。

本书会不时把 Bayesian 方法是有意义的这一点当作理所当然，但要提醒读者，这并不是一个已被普遍接受的立场——20 世纪的大部分时间里，统计学领域被非 Bayesian 方法所主导，在那些方法中概率只允许描述随机变量。两种方法之间的巨大差别在于：



> <span style="color:#7f8c8d;">原书 p.27｜§2.3 Forward probabilities and inverse probabilities、习题 2.4 与 2.5、例 2.6</span>

Bayesian 派也使用概率来描述推断。

## 2.3 Forward probabilities and inverse probabilities（正向概率与逆向概率）

概率计算常常落入两类之一：forward probability（正向概率）与 inverse probability（逆向概率）。下面是一个正向概率问题的例子：

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 2.4.[2, p.40]**</span> An urn contains $K$ balls, of which $B$ are black and $W = K - B$ are white. Fred draws a ball at random from the urn and replaces it, $N$ times.

(a) What is the probability distribution of the number of times a black ball is drawn, $n_B$?

(b) What is the expectation of $n_B$? What is the variance of $n_B$? What is the standard deviation of $n_B$? Give numerical answers for the cases $N = 5$ and $N = 400$, when $B = 2$ and $K = 10$.

正向概率问题涉及一个 generative model（生成模型），它描述一个被假定会产生某些数据的 process（过程）；任务是计算某个依赖于该数据的量的概率分布或期望。下面是另一个正向概率问题的例子：

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 2.5.[2, p.40]**</span> An urn contains $K$ balls, of which $B$ are black and $W = K - B$ are white. We define the fraction $f_B \equiv B/K$. Fred draws $N$ times from the urn, exactly as in exercise 2.4, obtaining $n_B$ blacks, and computes the quantity

```math
z = \frac{(n_B - f_B N)^{2}}{N f_B(1 - f_B)}. \qquad (2.19)
```

What is the expectation of $z$? In the case $N = 5$ and $f_B = 1/5$, what is the probability distribution of $z$? What is the probability that $z < 1$? [Hint: compare $z$ with the quantities computed in the previous exercise.]

与正向概率问题一样，inverse probability（逆向概率）问题也涉及一个过程的生成模型，但不是计算该过程所产生的某个量的概率分布，而是计算该过程中一个或多个未被观察的变量在给定被观察变量下的条件概率。这必然要用到 Bayes' theorem（Bayes 定理）。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 2.6（例 2.6）**</span> 有十一个坛子，用 $u \in \{0, 1, 2, \ldots, 10\}$ 标号，每个坛子里装有十个球。坛子 $u$ 装有 $u$ 个黑球与 $10 - u$ 个白球。Fred 随机选一个坛子 $u$，从该坛子有放回地抽取 $N$ 次，得到 $n_B$ 个黑球与 $N - n_B$ 个白球。Fred 的朋友 Bill 在一旁看着。如果 $N = 10$ 次抽取之后已经抽到了 $n_B = 3$ 个黑球，那么在 Bill 看来，Fred 所用的坛子是坛子 $u$ 的概率是多少？（Bill 不知道 $u$ 的取值。）

**Solution（解）** 随机变量 $u$ 与 $n_B$ 的联合概率分布可以写成

```math
P(u, n_B \mid N) = P(n_B \mid u, N)P(u). \qquad (2.20)
```

从 $u$ 与 $n_B$ 的联合概率，我们可以得到给定 $n_B$ 时 $u$ 的条件分布：

```math
P(u \mid n_B, N) = \frac{P(u, n_B \mid N)}{P(n_B \mid N)} \qquad (2.21)
```

```math
= \frac{P(n_B \mid u, N)P(u)}{P(n_B \mid N)}. \qquad (2.22)
```



> <span style="color:#7f8c8d;">原书 p.28｜图 2.5 与 2.6、后验概率的计算、inverse probability 的术语</span>

[Figure 2.5：Bill 与 Fred 的坛子问题中 $u$ 与 $n_B$ 的联合概率（$N = 10$ 次抽取后），横轴为 $n_B = 0 \ldots 10$，纵轴为 $u = 0 \ldots 10$。它演示的是：联合概率按二维网格分布，$u$ 的边缘概率是各行的和（每行都相同，均为 $1/11$），而第 3 列（$n_B = 3$）归一化后给出图 2.6 的后验分布。]

$u$ 的边缘概率是 $P(u) = \frac{1}{11}$，对所有 $u$ 成立。你解习题 2.4（p.27）时已经写出了给定 $u$ 与 $N$ 时 $n_B$ 的概率 $P(n_B \mid u, N)$。[你确实在做那些强烈推荐的习题，对吧？]如果我们定义 $f_u \equiv u/10$，那么

```math
P(n_B \mid u, N) = \binom{N}{n_B} f_u^{n_B}(1 - f_u)^{N - n_B}. \qquad (2.23)
```

分母 $P(n_B \mid N)$ 呢？这是 $n_B$ 的边缘概率，我们可以用和规则得到它：

```math
P(n_B \mid N) = \sum_{u} P(u, n_B \mid N) = \sum_{u} P(u)P(n_B \mid u, N). \qquad (2.24)
```

所以给定 $n_B$ 时 $u$ 的条件概率是

```math
P(u \mid n_B, N) = \frac{P(u)P(n_B \mid u, N)}{P(n_B \mid N)} \qquad (2.25)
```

```math
= \frac{1}{P(n_B \mid N)} \cdot \frac{1}{11}\binom{N}{n_B} f_u^{n_B}(1 - f_u)^{N - n_B}. \qquad (2.26)
```

这个条件分布可以通过把图 2.5 的第 3 列归一化得到，画在图 2.6 中。归一化常数，即 $n_B$ 的边缘概率，是 $P(n_B = 3 \mid N = 10) = 0.083$。后验概率 (2.26) 对所有的 $u$ 都成立，包括端点 $u = 0$ 与 $u = 10$，那里分别有 $f_u = 0$ 与 $f_u = 1$。给定 $n_B = 3$ 时 $u = 0$ 的后验概率等于零，因为如果 Fred 是从坛子 0 里抽，那不可能抽到任何黑球。$u = 10$ 的后验概率同样是零，因为那个坛子里没有白球。其余的假设 $u = 1, 2, \ldots, 9$ 都有非零的后验概率。

[Figure 2.6：给定 $n_B = 3$、$N = 10$ 时 $u$ 的条件概率（即后验概率），横轴为 $u = 0 \ldots 10$，纵轴为概率。表中列出 $u$ 与 $P(u \mid n_B = 3, N = 10)$：0 为 0、1 为 0.063、2 为 0.22、3 为 0.29、4 为 0.24、5 为 0.13、6 为 0.047、7 为 0.0099、8 为 0.00086、9 为 0.0000096、10 为 0。它演示的是：数据把后验质量集中在 $u = 3$ 附近（与观测到的 3 个黑球相符），而 $u = 0$ 与 $u = 10$ 这两个端点被数据彻底排除。]

### Terminology of inverse probability（逆向概率的术语）

在逆向概率问题中，给 Bayes' theorem 中出现的那些概率起名字会很方便。在方程 (2.25) 中，我们把边缘概率 $P(u)$ 称为 $u$ 的 prior probability（先验概率），而 $P(n_B \mid u, N)$ 称为 $u$ 的 likelihood（似然）。要注意，likelihood 与 probability 这两个词并不是同义词。量 $P(n_B \mid u, N)$ 同时是 $n_B$ 与 $u$ 的函数。对固定的 $u$，$P(n_B \mid u, N)$ 定义了 $n_B$ 上的一个概率。对固定的 $n_B$，$P(n_B \mid u, N)$ 定义了 $u$ 的 likelihood（似然）。


> <span style="color:#7f8c8d;">p.41 ⇄ 书内 p.29</span>

> <span style="color:#c0392b;">**切勿说「data 的 likelihood」。永远说「parameters 的 likelihood」。likelihood function 不是概率分布。**</span>

（若你想提到某个 likelihood function 所关联的 data，可以说「parameters 在给定 data 下的 likelihood」。）

条件概率 $P(u \mid n_B, N)$ 称为 u 在给定 $n_B$ 下的 **posterior probability**（后验概率）。归一化常数 $P(n_B \mid N)$ 不依赖 u，所以当我们只想评估各替代假设 u 的相对概率时，它的取值并不重要。然而，在大多数稍有复杂度的 data-modelling 问题中，这个量会变得重要，而它被赋予了好几个名字：$P(n_B \mid N)$ 称为 **evidence**，或称 **marginal likelihood**（边缘似然）。

若用 $\theta$ 表示未知 parameters，$D$ 表示 data，$H$ 表示总体的 hypothesis space（假设空间），则一般方程

```math
P(\theta \mid D, H) = \frac{P(D \mid \theta, H)\,P(\theta \mid H)}{P(D \mid H)} \tag{2.27}
```

被写成

```math
\text{posterior} = \frac{\text{likelihood} \times \text{prior}}{\text{evidence}}. \tag{2.28}
```

### Inverse probability and prediction（逆概率与预测）

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.6（例 2.6，续）</span>

仍假设 Bill 在 $N = 10$ 次抽取中观察到 $n_B = 3$ 个黑球，让 Fred 从同一个坛中再抽一个球。下一个抽出的球是黑球的概率是多少？〔你应当利用图 2.6 中的 posterior probabilities。〕

**Solution（解答）。** 由 sum rule（求和规则），

```math
P(\text{ball}_{N+1}\ \text{is black} \mid n_B, N) = \sum_u P(\text{ball}_{N+1}\ \text{is black} \mid u, n_B, N)\,P(u \mid n_B, N). \tag{2.29}
```

因为球是从选定的坛中**有放回**地抽出的，所以无论 $n_B$ 与 $N$ 是什么，概率 $P(\text{ball}_{N+1}\ \text{is black} \mid u, n_B, N)$ 就是 $f_u = u/10$。于是

```math
P(\text{ball}_{N+1}\ \text{is black} \mid n_B, N) = \sum_u f_u\,P(u \mid n_B, N). \tag{2.30}
```

代入图 2.6 给出的 $P(u \mid n_B, N)$ 数值，我们得到

```math
P(\text{ball}_{N+1}\ \text{is black} \mid n_B = 3, N = 10) = 0.333. \tag{2.31}
```

∎

**Comment（评注）。** 注意这个用概率论做出的预测，与统计学中流行的做法之间的差别：后者先挑出最可信的单个假设（在此例中就是「坛是 $u = 3$ 号坛」），再假定该假设为真去作预测（那会给出下一个球为黑球的概率 0.3）。正确的预测是**把不确定性考虑进去**的预测 —— 通过对假设 u 的可能取值做 marginalization（边缘化）而得到。这里的边缘化导致预测略微更温和、更不极端。


> <span style="color:#7f8c8d;">p.42 ⇄ 书内 p.30</span>

### Inference as inverse probability（把推断看作逆概率）

现在考虑下面这道练习，它具有一次简单科学研究的性质。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.7（例 2.7）</span>

Bill 把一枚弯曲的硬币（bent coin）掷 $N$ 次，得到一串正面与反面。我们假设这枚硬币出现正面的概率为 $f_H$；我们并不知道 $f_H$。若 $N$ 次投掷中出现了 $n_H$ 次正面，那么 $f_H$ 的概率分布是什么？（例如 $N$ 可能是 10，$n_H$ 可能是 3；或者，在大量投掷之后，我们可能有 $N = 300$ 而 $n_H = 29$。）在给定 $N$ 次投掷中出现 $n_H$ 次正面的条件下，第 $N+1$ 次结果为正面概率是多少？

> <span style="color:#7f8c8d;">此处的 $P(f)$ 表示概率**密度**（probability density），而不是概率分布。</span>

与例 2.6（p.27）不同，这个问题含有一个主观成分。如果按「概率是随机变量的频率」这一受限的概率定义，本例与十一坛问题并不相同。坛号 u 是随机变量，而硬币的 bias $f_H$ 通常不会被叫作随机变量 —— 它只是一个我们感兴趣的、固定但未知的参数。可是例 2.6 与例 2.7 难道不具有本质上的相似性吗？〔尤其是当 $N = 10$、$n_H = 3$ 的时候！〕

要解例 2.7，我们必须对硬币的 bias $f_H$ 可能是什么做出某个假设。这个定义在 $f_H$ 上的 **prior probability distribution**（先验概率分布）$P(f_H)$，对应十一坛问题里定义在 u 上的 prior。在那个例子中，友好的题目定义直接给出了 $P(u)$。而在现实生活中，我们必须靠假设来指定 priors；这些假设将是主观的，而我们的答案将依赖于它们。对我们 generative model（生成模型）里的其他概率，也完全可以说同样的话。例如，我们假设球是从坛中**独立**抽出的；但 Fred 抽球的动作并不完全随机，序列里难道不可能存在相关性吗？确实可能存在，所以连我们使用的 likelihood function 也依赖于假设。在真实的数据建模问题中，**priors 是主观的，likelihoods 也是主观的。**

我们现在用 $P(\cdot)$ 既表示连续变量上的概率密度，也表示离散变量上的概率，以及逻辑命题的概率。连续变量 $v$ 落在数值 $a$ 与 $b$ 之间（其中 $b > a$）的概率，定义为 $\int_a^b \mathrm{d}v\,P(v)$。量 $P(v)\,\mathrm{d}v$ 是无量纲的。密度 $P(v)$ 则是有量纲的量，其量纲与 $v$ 的量纲互为倒数 —— 这与无量纲的离散概率形成对照。看到概率密度大于 1 时不要惊讶。这是正常的，没有任何问题，只要对任意区间 $(a, b)$ 都有 $\int_a^b \mathrm{d}v\,P(v) \le 1$ 即可。

条件概率密度与联合概率密度的定义方式，与条件概率、联合概率完全一样。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.8. <span style="color:#7f8c8d;">[2]</span>

Assuming a uniform prior on $f_H$, $P(f_H) = 1$, solve the problem posed in example 2.7 (p.30). Sketch the posterior distribution of $f_H$ and compute the probability that the $N+1$th outcome will be a head, for

(a) $N = 3$ and $n_H = 0$;
(b) $N = 3$ and $n_H = 2$;
(c) $N = 10$ and $n_H = 3$;
(d) $N = 300$ and $n_H = 29$.

You will find the beta integral useful:

```math
\int_0^1 \mathrm{d}p_a\; p_a^{F_a}(1-p_a)^{F_b} = \frac{\Gamma(F_a+1)\,\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)} = \frac{F_a!\,F_b!}{(F_a+F_b+1)!}. \tag{2.32}
```


> <span style="color:#7f8c8d;">p.43 ⇄ 书内 p.31</span>

（接上题）回头看例 2.6（p.27）与方程 (2.31)，也许同样会让你有所启发。

人们有时会把「给未知参数（如 $f_H$）指定一个 prior distribution」与「对该参数的取值做出初始猜测」混为一谈。但 $f_H$ 上的 prior $P(f_H)$ 并不是「起初我猜 $f_H = 1/2$」这样一个简单的陈述。prior 是定义在 $f_H$ 上的概率**密度**，它规定了「$f_H$ 落在任意区间 $(f, f+\delta f)$ 内」这件事的先验置信度（prior degree of belief）。完全可能出现这样的情况：我们对 $f_H$ 的 prior 关于 1/2 对称，于是 $f_H$ 在 prior 下的均值为 1/2。在这种情况下，第一次投掷的 predictive distribution（预测分布）$x_1$ 确实会是

```math
P(x_1 = \text{head}) = \int \mathrm{d}f_H\, P(f_H)\,P(x_1 = \text{head} \mid f_H) = \int \mathrm{d}f_H\, P(f_H)\, f_H = 1/2. \tag{2.33}
```

但对后续各次投掷的预测，将依赖**整个** prior distribution，而不仅是它的均值。

### Data compression and inverse probability（数据压缩与逆概率）

考虑下面这个任务。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.9（例 2.9）</span>

写一个能压缩如下二进制文件的计算机程序：

```
0000000000000000000010010001000000100000010000000000000000000000000000000000001010000000000000110000
1000000000010000100000000010000000000000000000000100000000000000000100000000011000001000000011000100
0000000001001000000000010001000000000000000011000000000000000000000000000010000000000000000100000000
```

所示字符串中含有 $n_1 = 29$ 个 1 与 $n_0 = 271$ 个 0。

直观上，压缩之所以有效，是因为它利用了文件的可预测性。在此例中，该文件的信源似乎更**倾向**于发出 0 而不是 1。一个能压缩这个文件的数据压缩程序，必然隐含地或明确地在回答这个问题：「这个文件中下一个字符是 1 的概率是多少？」

你觉得这个问题在性质上与例 2.7（p.30）相似吗？我觉得是。本书的主题之一是：**数据压缩与数据建模是同一件事**，两者都应当像例 2.6 的坛子那样，用 inverse probability（逆概率）来处理。例 2.9 在第 6 章解决。

### The likelihood principle（likelihood 原理）

请先解下面两道练习。

[Figure 2.7：例 2.10 的两个坛子示意图 —— 坛 A 与坛 B，每坛三个球，颜色构成不同，框内标注 `A  B`]

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.10（例 2.10）</span>

坛 A 中含有三个球：一个黑球、两个白球；坛 B 中含有三个球：两个黑球、一个白球。随机选定其中一个坛，并抽出一个球。抽出的球是黑球。所选之坛为坛 A 的概率是多少？

[Figure 2.8：例 2.11 的两个坛子示意图 —— 坛 A 五个球（`p g c s ...` 等色名标注）、坛 B 五百个球，颜色多样]

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.11（例 2.11）</span>

坛 A 中含有五个球：一个黑球、两个白球、一个绿球、一个粉球；坛 B 中含有五百个球：二百个黑球、一百个白球、50 个黄球、40 个青球、30 个赭球、25 个绿球、25 个银球、20 个金球、10 个紫球。〔A 的球中有五分之一是黑球；B 的球中有五分之二是黑球。〕随机选定其中一个坛，并抽出一个球。抽出的球是黑球。此坛为坛 A 的概率是多少？


> <span style="color:#7f8c8d;">p.44 ⇄ 书内 p.32</span>

你对两个答案注意到了什么？它们的答案是否依赖于每个坛的详细构成？

**其他可能结果及其概率的细节是无关的。** 唯一要紧的是「实际发生的那个结果（这里是抽到黑球）」在不同假设下的概率。我们只需要知道 **likelihood**，即「已发生之 data 的概率如何随假设而变化」。这条关于推断的简单规则，称为 **likelihood principle**（likelihood 原理）。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">The likelihood principle（likelihood 原理）</span>

给定 data $d$ 关于 parameters $\theta$ 的 generative model $P(d \mid \theta)$，并且已经观察到一个具体结果 $d_1$，那么**所有推断与预测都应当只依赖于函数 $P(d_1 \mid \theta)$**。

> <span style="color:#00838f;">尽管这条原理如此简单，许多经典统计方法却违反了它。</span>

### 2.4 Definition of entropy and related functions（熵及相关函数的定义）

结果 $x$ 的 **Shannon information content**（香农信息量）定义为

```math
h(x) = \log_2 \frac{1}{P(x)}. \tag{2.34}
```

它以 **bits** 为度量单位。〔「bit」一词也用来表示取值 0 或 1 的变量；希望上下文总能澄清这里指的是两种含义中的哪一种。〕

在接下来的几章里，我们将确立：$h(a_i)$ 确实是事件 $x = a_i$ 的信息量的一个自然度量。到那时，我们会把这个量的名字简称为「the information content」。

表 2.9 的第四列给出了「从一份英文文档中随机取一个字符」时 27 个可能结果的 Shannon information content。结果 $x = z$ 的 Shannon information content 为 10.4 bits，而 $x = e$ 的为 3.5 bits。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Entropy（熵）</span>

**ensemble**（系综）$X$ 的 **entropy** 定义为结果的平均 Shannon information content：

```math
H(X) \equiv \sum_{x \in \mathcal{A}_X} P(x) \log \frac{1}{P(x)}, \tag{2.35}
```

其中约定：当 $P(x) = 0$ 时取 $0 \times \log 1/0 \equiv 0$，因为 $\lim_{\theta \to 0^+} \theta \log 1/\theta = 0$。

与 information content 一样，entropy 也以 bits 度量。

在方便时，我们也可以把 $H(X)$ 写成 $H(\mathbf{p})$，其中 $\mathbf{p}$ 是向量 $(p_1, p_2, \ldots, p_I)$。$X$ 的 entropy 的另一个名字是 $X$ 的 **uncertainty**（不确定性）。

<span style="color:#1e8449;">**[译注]**</span> **entropy 测的是「不确定性」，不是「信息量」——而 $h(x)=\log_2\frac{1}{P(x)}$ 里的 log 是从一条加法要求里逼出来的**

$h(x)$ 的定义式里那个 log 不是习惯，是唯一解。要求三条：① 越稀有的事件信息越多（$h$ 关于 $P$ 单调递减）；② **独立事件的信息量相加**——收到「A 发生」和「B 发生」两条独立消息，总 bit 数应等于各自 bit 数之和；③ 连续性。独立意味着 $P(A,B)=P(A)P(B)$，而只有对数能把乘法变成加法：$h(A,B)=\log\frac{1}{P(A)P(B)}=\log\frac{1}{P(A)}+\log\frac{1}{P(B)}$。换成 $1/P$ 或 $1/P^2$ 这类任何非 log 的单调函数，②立刻崩，于是「两段独立通信的带宽相加」这条工程事实在模型里无法表达，后面所有流码、信道容量的推导都失去可加骨架。反过来，$H(X)$ 取 $h$ 的期望，也不是审美选择：期望是唯一使「分阶段生成」的 log 可加性向下传递的聚合方式（见 §2.5 那条注）。

注意本节的用词：Boyd 的书里没有 entropy，MacKay 在这里给的第二个名字是 **uncertainty**，不是「信息量」。这个区分在两处显形：$H$ 是 ensemble 的属性（对整个分布取平均），$h(x)$ 才是单个结果的；而 $H$ 在 $P$ 均匀时取最大 $\log|\mathcal{A}_X|$——「最大不确定性」造句成立，「最大信息量」造句不成立（均匀分布恰恰什么都没告诉你）。

约定 $0\log\frac10\equiv0$ 值得单独点出：它不是魔改，而是 $g(\theta)=\theta\log\frac1\theta$ 在 $\theta\to0^+$ 时的极限，即把 $g$ 连续延拓到 $0$。抽掉这个约定，任何有零概率结果的 ensemble 的 entropy 都变成"未定义"，而实际分布普遍带零项（如 $P(x)=\frac12,\frac14,\frac14,0$），公式 (2.35) 会处处不可用。这和 Thomson 里「函数在开集上连续即可延拓到边界点」是同一件事，只是这里延拓点是 $0$ 而不是区间端点。

坐标：§2.4（书页 32，PDF 44；译文页标记 `p.44 ⇄ 书内 p.32`），式 (2.34)(2.35)；唯一性公理的完整版见 Cover & Thomas《Elements of Information Theory》§2.1 Theorem 2.1.1（三条公理 ⟹ $H$ 唯一到常数倍）。挂载：6.042J 对数把乘法化加法、期望的线性；Thomson 实分析极限与连续延拓。


#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.12（例 2.12）</span>

在英文文档中随机选取一个字母，其 entropy 约为 4.11 bits（假定其概率如表 2.9 所示）。我们把这个数算出来，靠的是在概率分布 $p_i$（表第三列）下对 $\log 1/p_i$（表第四列）取平均。

| $i$ | $a_i$ | $p_i$ | $h(p_i)$ |
|:--:|:--:|:--:|:--:|
| 1 | a | .0575 | 4.1 |
| 2 | b | .0128 | 6.3 |
| 3 | c | .0263 | 5.2 |
| 4 | d | .0285 | 5.1 |
| 5 | e | .0913 | 3.5 |
| 6 | f | .0173 | 5.9 |
| 7 | g | .0133 | 6.2 |
| 8 | h | .0313 | 5.0 |
| 9 | i | .0599 | 4.1 |
| 10 | j | .0006 | 10.7 |
| 11 | k | .0084 | 6.9 |
| 12 | l | .0335 | 4.9 |
| 13 | m | .0235 | 5.4 |
| 14 | n | .0596 | 4.1 |
| 15 | o | .0689 | 3.9 |
| 16 | p | .0192 | 5.7 |
| 17 | q | .0008 | 10.3 |
| 18 | r | .0508 | 4.3 |
| 19 | s | .0567 | 4.1 |
| 20 | t | .0706 | 3.8 |
| 21 | u | .0334 | 4.9 |
| 22 | v | .0069 | 7.2 |
| 23 | w | .0119 | 6.4 |
| 24 | x | .0073 | 7.1 |
| 25 | y | .0164 | 5.9 |
| 26 | z | .0007 | 10.4 |
| 27 | - | .1928 | 2.4 |
| | | $\sum_i p_i \log_2 \frac{1}{p_i}$ | 4.1 |

<span style="color:#7f8c8d;">Table 2.9 ── 从英文文档中随机取一字符时，各结果 a–z 与空格（-）的 Shannon information content（原书 Table 2.9）。</span>


> <span style="color:#7f8c8d;">p.45 ⇄ 书内 p.33</span>

我们现在来记下 entropy 函数的一些性质。

- $H(X) \ge 0$，等号成立当且仅当（iff）某个 $i$ 有 $p_i = 1$。〔「iff」意为「if and only if」（当且仅当）。〕
- 当 $\mathbf{p}$ 为均匀分布时，entropy 取最大值：

```math
H(X) \le \log(|\mathcal{A}_X|) \quad \text{with equality iff } p_i = 1/|\mathcal{A}_X| \text{ for all } i. \tag{2.36}
```

> <span style="color:#7f8c8d;">记号说明：竖线「$|\cdot|$」有两种含义。若 $\mathcal{A}_X$ 是集合，则 $|\mathcal{A}_X|$ 表示 $\mathcal{A}_X$ 中元素的个数；若 $x$ 是数，则 $|x|$ 表示 $x$ 的绝对值。</span>

**redundancy**（冗余度）度量的是 $H(X)$ 与其最大可能值 $\log(|\mathcal{A}_X|)$ 之间的相对差。$X$ 的 redundancy 为：

```math
1 - \frac{H(X)}{\log |\mathcal{A}_X|}. \tag{2.37}
```

本书不会用到「redundancy」，所以我没有给它指定符号。

$X, Y$ 的 **joint entropy**（联合熵）为：

```math
H(X, Y) = \sum_{xy \in \mathcal{A}_X \mathcal{A}_Y} P(x, y) \log \frac{1}{P(x, y)}. \tag{2.38}
```

对**独立**随机变量，entropy 是可加的：

```math
H(X, Y) = H(X) + H(Y) \quad \text{iff } P(x, y) = P(x)P(y). \tag{2.39}
```

到目前为止，我们对 information content 的定义只适用于有限集合 $\mathcal{A}_X$ 上的离散概率分布。这些定义可以推广到无限集，尽管此时 entropy 可能是无限的。连续集上概率密度的情形将在 §11.3 讨论。与 entropy 有关的其他重要定义与练习，将在 §8.1 陆续出现。

### 2.5 Decomposability of the entropy（entropy 的可分解性）

entropy 函数满足一条递归性质，计算 entropies 时非常有用。为方便起见，我们将把记号放宽一些，从而可以把 $H(X)$ 写成 $H(\mathbf{p})$，其中 $\mathbf{p}$ 是与 ensemble $X$ 相关联的概率向量。

先用一个例子说明这条性质。设想随机变量 $x \in \{0, 1, 2\}$ 是这样产生的：先掷一枚公平硬币，决定 $x$ 是否为 0；然后，若 $x$ 不为 0，再掷一次公平硬币，决定 $x$ 取 1 还是 2。$x$ 的概率分布为

```math
P(x = 0) = \frac{1}{2}; \qquad P(x = 1) = \frac{1}{4}; \qquad P(x = 2) = \frac{1}{4}. \tag{2.40}
```

$X$ 的 entropy 是多少？我们可以暴力地算出来：

```math
H(X) = \tfrac{1}{2}\log 2 + \tfrac{1}{4}\log 4 + \tfrac{1}{4}\log 4 = 1.5; \tag{2.41}
```

也可以用下面的分解，其中 $x$ 的取值是**逐步**揭示的。设想先得知 $x$ 是否为 0，然后，若 $x$ 不为 0，再得知它取的是哪个非零值。「$x$ 是否为 0」这一揭示，等价于


> <span style="color:#7f8c8d;">p.46 ⇄ 书内 p.34（接上页：跨页句子在此继续）</span>

揭示一个概率分布为 $\{1/2, 1/2\}$ 的二元变量。这次揭示的 entropy 为 $H(1/2, 1/2) = \tfrac{1}{2}\log 2 + \tfrac{1}{2}\log 2 = 1$ bit。若 $x$ 不为 0，我们随后得知第二次掷币的结果。这同样是一个概率分布为 $\{1/2, 1/2\}$ 的二元变量，其 entropy 也是 1 bit。然而我们只有一半的时候才会经历第二次揭示，所以 entropy 可以写成：

```math
H(X) = H(1/2, 1/2) + \tfrac{1}{2}\,H(1/2, 1/2). \tag{2.42}
```

推广之，我们对任意概率分布 $\mathbf{p} = \{p_1, p_2, \ldots, p_I\}$ 的 entropy 所做的观察是：

```math
H(\mathbf{p}) = H(p_1, 1-p_1) + (1-p_1)\,H\!\left(\frac{p_2}{1-p_1}, \frac{p_3}{1-p_1}, \ldots, \frac{p_I}{1-p_1}\right). \tag{2.43}
```

写成公式时，这条性质显得遗憾地丑陋；然而它其实是一条简单的性质，而且是一条你应当用起来的性质。

<span style="color:#1e8449;">**[译注]**</span> **可分解性 $H(X,Y)=H(X)+H(Y|X)$ 是概率链式法则在 log 下变成加法——它是所有 sequential 算法的合法性来源**

概率侧的事实是 $P(x,y)=P(x)P(y\,|\,x)$。取 $-\log$ 后乘法变加法，于是
$$H(X,Y)=\sum_{x,y}P(x,y)\log\frac{1}{P(x)P(y|x)}=H(X)+\sum_x P(x)\sum_y P(y|x)\log\frac{1}{P(y|x)}=H(X)+H(Y|X).$$
(2.42) 那个三分支例子只是这条恒等式在 $x\in\{0,1,2\}$ 上的特例：$H(\frac12,\frac14,\frac14)=1+\frac12\cdot 1=1.5$。别把它当技巧，它是「按阶段生成」这个建模结构与「按阶段编码」这个算法结构之间的桥：只要数据确实是分阶段产生的（先掷硬币决定是不是 0，再掷一次决定 1 还是 2），entropy 就自动按阶段相加，于是编码器可以逐阶段分配码字长度而不损失最优性。

抽掉它，一切 sequential 算法退化成枚举：Huffman 的分块构造（§5.5）无法论证最优、arithmetic coding（§6.2）无法逐符号更新区间、HMM 的 forward 算法无法线性递推、「按 token 计算 per-token loss 再相加等于整句的 $-\log P$」这条训练时的记账规则也不成立。做语言模型时你在 loss 上除以 token 数，用的正是这条可加性。

挂载：6.042J 条件概率链式法则 $P(A\cap B)=P(A)P(B|A)$（同一恒等式，只是取了对数）；6.006 动态规划的最优子结构（「整体最优 = 阶段最优之和」在这里是精确等式，不是不等式，所以比 DP 的论证更强）。

坐标：§2.5（书页 33–34，PDF 45–46），式 (2.40)–(2.42)；一般形式即 chain rule for entropy，MacKay 在 §8.1（书页 141+，PDF 153+）再次使用。


再进一步推广，对任意 $m$，entropy 都具有下述性质：

```math
\begin{aligned}
H(\mathbf{p}) ={}& H\big[(p_1 + p_2 + \cdots + p_m),\ (p_{m+1} + p_{m+2} + \cdots + p_I)\big] \\
&+ (p_1 + \cdots + p_m)\,H\!\left(\frac{p_1}{p_1 + \cdots + p_m}, \ldots, \frac{p_m}{p_1 + \cdots + p_m}\right) \\
&+ (p_{m+1} + \cdots + p_I)\,H\!\left(\frac{p_{m+1}}{p_{m+1} + \cdots + p_I}, \ldots, \frac{p_I}{p_{m+1} + \cdots + p_I}\right).
\end{aligned} \tag{2.44}
```

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.13（例 2.13）</span>

一个信源从字母表 $\mathcal{A} = \{0, 1, \ldots, 9, \mathrm{a}, \mathrm{b}, \ldots, \mathrm{z}\}$ 中产生一个字符 $x$：以概率 $1/3$，$x$ 是数字（$0, \ldots, 9$）；以概率 $1/3$，$x$ 是元音（a, e, i, o, u）；以概率 $1/3$，它是 21 个辅音之一。所有数字等概率，元音与辅音亦然。估计 $X$ 的 entropy。

**Solution（解答）。**

```math
\log 3 + \tfrac{1}{3}(\log 10 + \log 5 + \log 21) = \log 3 + \tfrac{1}{3}\log 1050 \approx \log 30 \ \text{bits}.
```

∎

### 2.6 Gibbs' inequality（Gibbs 不等式）

> <span style="color:#7f8c8d;">Leibler 里的「ei」读法与 heist 中的相同。</span>

定义在同一字母表 $\mathcal{A}_X$ 上的两个概率分布 $P(x)$ 与 $Q(x)$ 之间的 **relative entropy**（相对熵），或称 **Kullback–Leibler divergence**（KL 散度），为

```math
\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}. \tag{2.45}
```

relative entropy 满足 **Gibbs' inequality**（Gibbs 不等式）

```math
\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) \ge 0 \tag{2.46}
```

且等号仅在 $P = Q$ 时成立。注意：一般而言，交换分布 $P$ 与 $Q$ 时 relative entropy 并不对称 —— 通常 $\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) \ne \mathrm{D}_{\mathrm{KL}}(Q\,\|\,P)$，所以 $\mathrm{D}_{\mathrm{KL}}$ 尽管有时被叫作「KL distance」（KL 距离），严格说来并不是一种距离。relative entropy 在 pattern recognition（模式识别）、neural networks（神经网络）以及信息论中都很重要。

Gibbs 不等式很可能是本书中最重要的不等式。它以及许多其他不等式，都可以借助 **convexity**（凸性）这一概念来证明。

<span style="color:#1e8449;">**[译注]**</span> **Gibbs 不等式是全书唯一的「不等式母机」——一行证明，抽掉它四条结论同时崩**

证明只要一行，用的是 $\log$ 的凹性（Jensen）：$-\mathrm{D}_{\mathrm{KL}}(P\|Q)=\sum_x P(x)\log\frac{Q(x)}{P(x)}\le\log\sum_x P(x)\frac{Q(x)}{P(x)}=\log 1=0$。注意 $\sum_x Q(x)=1$ 正是这一步的落脚点——没有「两边同字母表、概率和都为 1」，不等式不成立（$Q$ 不是概率分布时 $D_{KL}$ 可以为负）。

抽掉它，这几条立刻失去依据：① $H(X)\le\log|\mathcal{A}_X|$，等号仅在均匀分布取到——即「最大熵 = 均匀」，这是最大熵建模、Jaynes 一切推断的出发点；② 任何「给定约束求最大 entropy 分布」的求解失去最优性证书（只能用 Lagrange 乘子算出驻点，却无法证明它是全局最大；反过来有 Gibbs 就能给对偶间隙）；③ 变分推断的 ELBO 单调上升（EM 每次迭代不降的证明全靠 $D_{KL}\ge0$）；④ Huffman / arithmetic code 的平均码长 $\ge H$ 这条下界（见 §5.1）。

还有一个必须记清的性质：$D_{KL}$ **不对称、不满足三角不等式**，所以它是 divergence 而不是 metric。这与 6.042J 里等价关系三条件（自反、对称、传递）的分界线完全一致：把 $\mathrm{D}_{\mathrm{KL}}$ 当距离用，就会写出「$d(p,q)=d(q,p)$」的错误推理（$D_{KL}(P\|Q)\ne D_{KL}(Q\|P)$ 是最常见的坑）；它在 $P=Q$ 时为 0，但"为 0 则相等"这条成立靠的是 Gibbs 不等式本身，不是定义。

坐标：§2.6（书页 34–35，PDF 46–47），式 (2.45)(2.46)；Jensen 证明在 §2.7 之后（书页 37，PDF 49；译文行 931 附近「我们用 Jensen's inequality 来证明 Gibbs' inequality」）；$H\le\log|\mathcal{A}|$ 与 Huffman 下界见 §5.1（书页 89+，PDF 101+）。挂载：6.042J 等价关系与度量的区别；Boyd《凸优化》§3.1.3 一阶条件与 §3.1.8 Jensen 不等式。


> <span style="color:#7f8c8d;">p.47 ⇄ 书内 p.35</span>

### 2.7 Jensen's inequality for convex functions（凸函数的 Jensen 不等式）

「convex」与「concave」这两个词可以按「convex-smile」（凸＝微笑）与「concave-frown」（凹＝皱眉）来记。这套命名有有益的冗余性：人可能忘记 convex 与 concave 哪个朝上，但把微笑与皱眉搞混要难得多。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Convex functions（凸函数）</span>

若函数 $f(x)$ 在 $(a, b)$ 上的每一条弦都位于函数图像**上方**（如图 2.10 所示），则称 $f(x)$ 在 $(a, b)$ 上是 **convex** 的；也就是说，对一切 $x_1, x_2 \in (a, b)$ 与 $0 \le \lambda \le 1$，都有

```math
f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2). \tag{2.47}
```

若对一切 $x_1, x_2 \in (a, b)$，上式仅在 $\lambda = 0$ 与 $\lambda = 1$ 时取等号，则称 $f$ 是 **strictly convex**（严格凸）的。

对 concave（凹函数）与 strictly concave（严格凹函数），定义类似。

一些 strictly convex 函数：

- $x^2$、$\mathrm{e}^{x}$ 与 $\mathrm{e}^{-x}$（对一切 $x$）；
- $\log(1/x)$ 与 $x \log x$（对 $x > 0$）。

[Figure 2.10：凸性定义示意图 —— 曲线上两点 $(x_1, f(x_1))$、$(x_2, f(x_2))$ 连成弦，弦在曲线上方；图中标注 $\lambda f(x_1) + (1-\lambda)f(x_2)$、$f(x^*)$、$x^* = \lambda x_1 + (1-\lambda)x_2$]

[Figure 2.11：几个凸函数的曲线图 —— 依次为 $x^2$、$\mathrm{e}^{-x}$、$\log \frac{1}{x}$、$x \log x$，横轴取 $-1$ 到 $3$ 区间]

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Jensen's inequality（Jensen 不等式）</span>

若 $f$ 是 convex function，$x$ 是随机变量，则

```math
\mathbb{E}\left[f(x)\right] \ge f\left(\mathbb{E}[x]\right), \tag{2.48}
```

其中 $\mathbb{E}$ 表示 expectation（期望）。若 $f$ 是 strictly convex 的，且 $\mathbb{E}\left[f(x)\right] = f(\mathbb{E}[x])$，则随机变量 $x$ 是常数。

对 concave function，Jensen's inequality 也可以改写，只需把不等号方向反转。

Jensen's inequality 有一个物理版本，如下所述。

> <span style="color:#00838f;">若把一组质量 $p_i$ 放在凸曲线 $f(x)$ 上的位置 $(x_i, f(x_i))$ 处，那么这些质量的质心（centre of gravity）位于 $\left(\mathbb{E}[x], \mathbb{E}[f(x)]\right)$，它落在曲线**上方**。</span>

[Figure 2.10 右侧标注：Centre of gravity（质心）]

若这还不能说服你，那么不妨做下面这道练习。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.14. <span style="color:#7f8c8d;">[2, p.41]</span>

Prove Jensen's inequality.

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2.15（例 2.15）</span>

三个正方形的平均面积 $\bar{A} = 100\ \mathrm{m}^2$，它们边长的平均值为 $\bar{l} = 10\ \mathrm{m}$。关于这三个正方形中最大的那个，能说什么？〔用 Jensen's inequality。〕

**Solution（解答）。** 设 $x$ 为正方形的边长，并令 $x$ 在三条边长 $l_1, l_2, l_3$ 上各取概率 $1/3$。于是我们掌握的信息是 $\mathbb{E}[x] = 10$ 与 $\mathbb{E}[f(x)] = 100$，其中 $f(x) = x^2$ 是把边长映射为面积的函数。这是一个 strictly convex function。我们注意到等号 $\mathbb{E}[f(x)] = f(\mathbb{E}[x])$ 竟然成立，因此 $x$ 是常数，三条边长必然全部相等。最大正方形的面积为 $100\ \mathrm{m}^2$。∎


> <span style="color:#7f8c8d;">p.48 ⇄ 书内 p.36</span>

### Convexity and concavity also relate to maximization（凸性与凹性也关系到取极大值）

若 $f(\mathbf{x})$ 是 concave 的，且存在某点使

```math
\frac{\partial f}{\partial x_k} = 0 \quad \text{for all } k, \tag{2.49}
```

则 $f(\mathbf{x})$ 在该点取得最大值。

**逆命题不成立**：若 concave 的 $f(\mathbf{x})$ 在某 $\mathbf{x}$ 处取最大值，未必有那里的梯度 $\nabla f(\mathbf{x})$ 等于零。例如 $f(x) = -|x|$ 在 $x = 0$ 处取最大值，而其导数在该处未定义；又如对概率 $p \in (0, 1)$，$f(p) = \log(p)$ 在取值范围的边界 $p = 1$ 处取最大值，那里 $\mathrm{d}f(p)/\mathrm{d}p = 1$。

### 2.8 Exercises（习题）

#### Sums of random variables（随机变量之和）

> <span style="color:#7f8c8d;">这道练习意在帮你思考 central-limit theorem（中心极限定理）：它说的是，若独立随机变量 $x_1, x_2, \ldots, x_N$ 具有均值 $\mu_n$ 与有限方差 $\sigma_n^2$，则在 $N$ 很大时，和 $\sum_n x_n$ 的分布趋于均值 $\sum_n \mu_n$、方差 $\sum_n \sigma_n^2$ 的正态（Gaussian）分布。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.16. <span style="color:#7f8c8d;">[3, p.41]</span>

(a) Two ordinary dice with faces labelled $1, \ldots, 6$ are thrown. What is the probability distribution of the sum of the values? What is the probability distribution of the absolute difference between the values?

(b) One hundred ordinary dice are thrown. What, roughly, is the probability distribution of the sum of the values? Sketch the probability distribution and estimate its mean and standard deviation.

(c) How can two cubical dice be labelled using the numbers $\{0, 1, 2, 3, 4, 5, 6\}$ so that when the two dice are thrown the sum has a uniform probability distribution over the integers $1$–$12$?

(d) Is there any way that one hundred dice could be labelled with integers such that the probability distribution of the sum is uniform?

#### Inference problems（推断问题）

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.17. <span style="color:#7f8c8d;">[2, p.41]</span>

If $q = 1 - p$ and $a = \ln p/q$, show that

```math
p = \frac{1}{1 + \exp(-a)}. \tag{2.50}
```

Sketch this function and find its relationship to the hyperbolic tangent function $\tanh(u) = \dfrac{\mathrm{e}^{u} - \mathrm{e}^{-u}}{\mathrm{e}^{u} + \mathrm{e}^{-u}}$.

It will be useful to be fluent in base-2 logarithms also. If $b = \log_2 p/q$, what is $p$ as a function of $b$?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.18. <span style="color:#7f8c8d;">[2, p.42]</span>

Let $x$ and $y$ be dependent random variables with $x$ a binary variable taking values in $\mathcal{A}_X = \{0, 1\}$. Use Bayes' theorem to show that the log posterior probability ratio for $x$ given $y$ is

```math
\log \frac{P(x = 1 \mid y)}{P(x = 0 \mid y)} = \log \frac{P(y \mid x = 1)}{P(y \mid x = 0)} + \log \frac{P(x = 1)}{P(x = 0)}. \tag{2.51}
```

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.19. <span style="color:#7f8c8d;">[2, p.42]</span>

Let $x$, $d_1$ and $d_2$ be random variables such that $d_1$ and $d_2$ are conditionally independent given a binary variable $x$. Use Bayes' theorem to show that the posterior probability ratio for $x$ given $\{d_i\}$ is

```math
\frac{P(x = 1 \mid \{d_i\})}{P(x = 0 \mid \{d_i\})} = \frac{P(d_1 \mid x = 1)}{P(d_1 \mid x = 0)}\,\frac{P(d_2 \mid x = 1)}{P(d_2 \mid x = 0)}\,\frac{P(x = 1)}{P(x = 0)}. \tag{2.52}
```


> <span style="color:#7f8c8d;">p.49 ⇄ 书内 p.37</span>

#### Life in high-dimensional spaces（高维空间中的生活）

概率分布与体积在高维空间里有一些出人意料的性质。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.20. <span style="color:#7f8c8d;">[2, p.42]</span>

Consider a sphere of radius $r$ in an $N$-dimensional real space. Show that the fraction of the volume of the sphere that is in the surface shell lying at values of the radius between $r - \epsilon$ and $r$, where $0 < \epsilon < r$, is:

```math
f = 1 - \left(1 - \frac{\epsilon}{r}\right)^{N}. \tag{2.53}
```

Evaluate $f$ for the cases $N = 2$, $N = 10$ and $N = 1000$, with (a) $\epsilon/r = 0.01$; (b) $\epsilon/r = 0.5$.

Implication: points that are uniformly distributed in a sphere in $N$ dimensions, where $N$ is large, are very likely to be in a thin shell near the surface.

> <span style="color:#7f8c8d;">〔原文此处 $\epsilon$ 因排版丢失；按上下文与式 (2.53) 补回。〕</span>

#### Expectations and entropies（期望与熵）

你大概熟悉「计算 $x$ 的某个函数的期望」这个想法：

```math
\mathbb{E}\left[f(x)\right] = \overline{f(x)} = \sum_x P(x) f(x). \tag{2.54}
```

但当函数 $f(x)$ 本身依赖于概率 $P(x)$ 时，你可能就不那么习惯去算这个期望了。接下来几个例子处理的正是这一疑虑。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.21. <span style="color:#7f8c8d;">[1, p.43]</span>

Let $p_a = 0.1$, $p_b = 0.2$, and $p_c = 0.7$. Let $f(a) = 10$, $f(b) = 5$, and $f(c) = 10/7$. What is $\mathbb{E}[f(x)]$? What is $\mathbb{E}[1/P(x)]$?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.22. <span style="color:#7f8c8d;">[2, p.43]</span>

For an arbitrary ensemble, what is $\mathbb{E}[1/P(x)]$?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.23. <span style="color:#7f8c8d;">[1, p.43]</span>

Let $p_a = 0.1$, $p_b = 0.2$, and $p_c = 0.7$. Let $g(a) = 0$, $g(b) = 1$, and $g(c) = 0$. What is $\mathbb{E}[g(x)]$?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.24. <span style="color:#7f8c8d;">[1, p.43]</span>

Let $p_a = 0.1$, $p_b = 0.2$, and $p_c = 0.7$. What is the probability that $P(x) \in [0.15, 0.5]$? What is

```math
P\left(\log \frac{P(x)}{0.2} > 0.05\right)?
```

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.25. <span style="color:#7f8c8d;">[3, p.43]</span>

Prove the assertion that $H(X) \le \log(|\mathcal{A}_X|)$ with equality iff $p_i = 1/|\mathcal{A}_X|$ for all $i$. ($|\mathcal{A}_X|$ denotes the number of elements in the set $\mathcal{A}_X$.) [Hint: use Jensen's inequality (2.48); if your first attempt to use Jensen does not succeed, remember that Jensen involves both a random variable and a function, and you have quite a lot of freedom in choosing these; think about whether your chosen function $f$ should be convex or concave.]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.26. <span style="color:#7f8c8d;">[3, p.44]</span>

Prove that the relative entropy (equation (2.45)) satisfies $\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) \ge 0$ (Gibbs' inequality) with equality only if $P = Q$.

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.27. <span style="color:#7f8c8d;">[2]</span>

Prove that the entropy is indeed decomposable as described in equations (2.43–2.44).


> <span style="color:#7f8c8d;">p.50 ⇄ 书内 p.38</span>

[Figure：习题 2.28 的二叉树示意 —— 先用 bias 为 $f$ 的弯曲硬币决定结果落在 $\{0, 1\}$ 还是 $\{2, 3\}$，再用 bias 为 $g$ 或 $h$ 的第二、第三枚弯曲硬币决定具体取值；图中标注 $g_0$、$f$、$1-g$、$d$、$1-f$、$h$、$1-h$ 与 $0,1,2,3$]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.28. <span style="color:#7f8c8d;">[2, p.45]</span>

A random variable $x \in \{0, 1, 2, 3\}$ is selected by flipping a bent coin with bias $f$ to determine whether the outcome is in $\{0, 1\}$ or $\{2, 3\}$; then either flipping a second bent coin with bias $g$ or a third bent coin with bias $h$ respectively. Write down the probability distribution of $x$. Use the decomposability of the entropy (2.44) to find the entropy of $X$. [Notice how compact an expression is obtained if you make use of the binary entropy function $H_2(x)$, compared with writing out the four-term entropy explicitly.] Find the derivative of $H(X)$ with respect to $f$. [Hint: $\mathrm{d}H_2(x)/\mathrm{d}x = \log((1-x)/x)$.]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.29. <span style="color:#7f8c8d;">[2, p.45]</span>

An unbiased coin is flipped until one head is thrown. What is the entropy of the random variable $x \in \{1, 2, 3, \ldots\}$, the number of flips? Repeat the calculation for the case of a biased coin with probability $f$ of coming up heads. [Hint: solve the problem both directly and by using the decomposability of the entropy (2.43).]

### 2.9 Further exercises（进阶习题）

#### Forward probability（前向概率）

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.30. <span style="color:#7f8c8d;">[1]</span>

An urn contains $w$ white balls and $b$ black balls. Two balls are drawn, one after the other, without replacement. Prove that the probability that the first ball is white is equal to the probability that the second is white.

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.31. <span style="color:#7f8c8d;">[2]</span>

A circular coin of diameter $a$ is thrown onto a square grid whose squares are $b \times b$ ($a < b$). What is the probability that the coin will lie entirely within one square? [Ans: $(1 - a/b)^2$]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.32. <span style="color:#7f8c8d;">[3]</span>

Buffon's needle. A needle of length $a$ is thrown onto a plane covered with equally spaced parallel lines with separation $b$. What is the probability that the needle will cross a line? [Ans, if $a < b$: $2a/\pi b$] [Generalization – Buffon's noodle: on average, a random curve of length $A$ is expected to intersect the lines $2A/\pi b$ times.]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.33. <span style="color:#7f8c8d;">[2]</span>

Two points are selected at random on a straight line segment of length 1. What is the probability that a triangle can be constructed out of the three resulting segments?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.34. <span style="color:#7f8c8d;">[2, p.45]</span>

An unbiased coin is flipped until one head is thrown. What is the expected number of tails and the expected number of heads?

Fred, who doesn't know that the coin is unbiased, estimates the bias using $\hat{f} \equiv h/(h + t)$, where $h$ and $t$ are the numbers of heads and tails tossed. Compute and sketch the probability distribution of $\hat{f}$.

N.B., this is a forward probability problem, a sampling theory problem, not an inference problem. Don't use Bayes' theorem.

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.35. <span style="color:#7f8c8d;">[2, p.45]</span>

Fred rolls an unbiased six-sided die once per second, noting the occasions when the outcome is a six.

(a) What is the mean number of rolls from one six to the next six?
(b) Between two rolls, the clock strikes one. What is the mean number of rolls until the next six?


> <span style="color:#7f8c8d;">p.51 ⇄ 书内 p.39（习题 2.35 续）</span>

(c) Now think back before the clock struck. What is the mean number of rolls, going back in time, until the most recent six?

(d) What is the mean number of rolls from the six before the clock struck to the next six?

(e) Is your answer to (d) different from your answer to (a)? Explain.

> <span style="color:#7f8c8d;">这道练习还有另一个版本：Fred 在 Poissonville 的一个公交站等车，那里的公交车独立地随机到达（一个 Poisson process），平均每六分钟一班。Fred 到站后，平均要等多久才有车？〔6 分钟。〕那么，他刚错过的那班车与他要赶上的那班车之间，时间间隔是多少？〔12 分钟。〕请解释这个表面上的悖论。并注意它与 Clockville 情形的对照 —— 那里车次精确地每隔 6 分钟一班。你可以核实：在 Clockville，车站的平均等待时间是 3 分钟，而错过的那班车与下一班车之间的间隔是 6 分钟。</span>

#### Conditional probability（条件概率）

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.36. <span style="color:#7f8c8d;">[2]</span>

You meet Fred. Fred tells you he has two brothers, Alf and Bob.

What is the probability that Fred is older than Bob?

Fred tells you that he is older than Alf. Now, what is the probability that Fred is older than Bob? (That is, what is the conditional probability that $F > B$ given that $F > A$?)

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.37. <span style="color:#7f8c8d;">[2]</span>

The inhabitants of an island tell the truth one third of the time. They lie with probability 2/3.

On an occasion, after one of them made a statement, you ask another 'was that statement true?' and he says 'yes'.

What is the probability that the statement was indeed true?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.38. <span style="color:#7f8c8d;">[2, p.46]</span>

Compare two ways of computing the probability of error of the repetition code R3, assuming a binary symmetric channel (you did this once for exercise 1.2 (p.7)) and confirm that they give the same answer.

> <span style="color:#7f8c8d;">式 (1.18) 给出的是：在给定接收向量 $r$ 时，输入 $s$ 的 posterior probability。</span>

Binomial distribution method. Add the probability that all three bits are flipped to the probability that exactly two bits are flipped.

Sum rule method. Using the sum rule, compute the marginal probability that $r$ takes on each of the eight possible values, $P(r)$. [$P(r) = \sum_s P(s)P(r \mid s)$.] Then compute the posterior probability of $s$ for each of the eight values of $r$. [In fact, by symmetry, only two example cases $r = (000)$ and $r = (001)$ need be considered.] Notice that some of the inferred bits are better determined than others. From the posterior probability $P(s \mid r)$ you can read out the case-by-case error probability, the probability that the more probable hypothesis is not correct, $P(\text{error} \mid r)$. Find the average error probability using the sum rule,

```math
P(\text{error}) = \sum_r P(r)\,P(\text{error} \mid r). \tag{2.55}
```


> <span style="color:#7f8c8d;">p.52 ⇄ 书内 p.40</span>

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 2.39. <span style="color:#7f8c8d;">[3C, p.46]</span>

The frequency $p_n$ of the $n$th most frequent word in English is roughly approximated by

```math
p_n \simeq \begin{cases} \dfrac{0.1}{n}, & \text{for } n \in 1, \ldots, 12\,367 \\ 0, & n > 12\,367. \end{cases} \tag{2.56}
```

[This remarkable $1/n$ law is known as Zipf's law, and applies to the word frequencies of many languages (Zipf, 1949).] If we assume that English is generated by picking words at random according to this distribution, what is the entropy of English (per word)? [This calculation can be found in 'Prediction and entropy of printed English', C.E. Shannon, Bell Syst. Tech. J. 30, pp.50–64 (1950), but, inexplicably, the great man made numerical errors in it.]

### 2.10 Solutions（解答）

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.2（习题 2.2 的解答，p.24）

否，它们并不独立。若独立，则所有条件分布 $P(y \mid x)$ 都会是 $y$ 的同一函数，与 $x$ 无关（参见图 2.3）。

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.4（习题 2.4 的解答，p.27）

我们定义比例 $f_B \equiv B/K$。

```math
f_B \equiv B/K. \tag{2.57}
```

(a) 黑球个数服从二项分布（binomial distribution）：

```math
P(n_B \mid f_B, N) = \binom{N}{n_B}\, f_B^{\,n_B}\,(1 - f_B)^{N-n_B}.
```

(b) 该分布的均值与方差为：

```math
\mathbb{E}[n_B] = N f_B \tag{2.58}
```

```math
\mathrm{var}[n_B] = N f_B (1 - f_B). \tag{2.59}
```

这两个结果在例 1.1（p.1）中推导过。$n_B$ 的标准差为 $\sqrt{\mathrm{var}[n_B]} = \sqrt{N f_B(1 - f_B)}$。

当 $B/K = 1/5$、$N = 5$ 时，$n_B$ 的期望与方差分别为 1 与 $4/5$，标准差为 0.89。

当 $B/K = 1/5$、$N = 400$ 时，$n_B$ 的期望与方差分别为 80 与 64，标准差为 8。

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.5（习题 2.5 的解答，p.27）

量

```math
z = \frac{(n_B - f_B N)^2}{N f_B (1 - f_B)}
```

的分子可以辨认为 $(n_B - \mathbb{E}[n_B])^2$；分母等于 $n_B$ 的方差（式 2.59），而按定义，方差正是分子的期望。所以 $z$ 的期望为 1。〔像 $z$ 这样度量 data 对期望值的偏离的随机变量，有时称为 $\chi^2$（卡方）。〕

在 $N = 5$、$f_B = 1/5$ 的情形下，$N f_B$ 为 1，$\mathrm{var}[n_B]$ 为 $4/5$。分子有五个可能取值，其中只有一个小于 1：$(n_B - f_B N)^2 = 0$ 对应概率 $P(n_B = 1) = 0.4096$；所以 $z < 1$ 的概率是 0.4096。


> <span style="color:#7f8c8d;">p.53 ⇄ 书内 p.41</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.14（习题 2.14 的解答，p.35）

我们希望证明：给定性质

```math
f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2), \tag{2.60}
```

则在 $\sum_i p_i = 1$、$p_i \ge 0$ 时，

```math
\sum_{i=1}^{I} p_i f(x_i) \ge f\left(\sum_{i=1}^{I} p_i x_i\right). \tag{2.61}
```

我们从右端出发，用递归方式推进。（本证明不处理某些 $p_i = 0$ 的情形；此类细节留给吹毛求疵的读者。）第一行我们使用 convexity 的定义 (2.60)，取 $\lambda = p_1 / \sum_{i=1}^{I} p_i = p_1$；第二行取 $\lambda = p_2 / \sum_{i=2}^{I} p_i$。

```math
\begin{aligned}
f\left(\sum_{i=1}^{I} p_i x_i\right) &= f\left(p_1 x_1 + \sum_{i=2}^{I} p_i x_i\right) \\
&\le p_1 f(x_1) + \left(\sum_{i=2}^{I} p_i\right) f\!\left(\frac{\sum_{i=2}^{I} p_i x_i}{\sum_{i=2}^{I} p_i}\right) \\
&\le p_1 f(x_1) + \left(\sum_{i=2}^{I} p_i\right)\left[\frac{p_2}{\sum_{i=2}^{I} p_i} f(x_2) + \frac{\sum_{i=3}^{I} p_i}{\sum_{i=2}^{I} p_i} f\!\left(\frac{\sum_{i=3}^{I} p_i x_i}{\sum_{i=3}^{I} p_i}\right)\right],
\end{aligned} \tag{2.62}
```

如此依此类推。∎

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.16（习题 2.16 的解答，p.36）

(a) 对结果 $\{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$，概率为 $P = \left\{\tfrac{1}{36}, \tfrac{2}{36}, \tfrac{3}{36}, \tfrac{4}{36}, \tfrac{5}{36}, \tfrac{6}{36}, \tfrac{5}{36}, \tfrac{4}{36}, \tfrac{3}{36}, \tfrac{2}{36}, \tfrac{1}{36}\right\}$。

(b) 单枚骰子的取值为均值 3.5、方差 $35/12$。所以一百枚之和的均值为 350、方差为 $3500/12 \simeq 292$；由 central-limit theorem，其概率分布大致为 Gaussian（但被限制在整数上），均值与方差如上。

(c) 要得到均匀分布的和，我们必须从一些分布「尖峭」、概率质量集中在极端的随机变量出发。唯一解是：一枚普通骰子，另一枚骰子六面标成 $6, 6, 6, 0, 0, 0$。

(d) 可以，均匀分布有若干构造方式，例如把第 $r$ 枚骰子标成 $\{0, 1, 2, 3, 4, 5\} \times 6^{r}$。

> <span style="color:#7f8c8d;">值得思考：这个均匀分布与 central-limit theorem 矛盾吗？</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.17（习题 2.17 的解答，p.36）

```math
a = \ln \frac{p}{q} \quad \Rightarrow \quad \frac{p}{q} = \mathrm{e}^{a} \tag{2.63}
```

```math
\text{and } q = 1 - p \text{ gives } \quad \frac{p}{1-p} = \mathrm{e}^{a} \tag{2.64}
```

```math
\Rightarrow \quad p = \frac{\mathrm{e}^{a}}{\mathrm{e}^{a} + 1} = \frac{1}{1 + \exp(-a)}. \tag{2.66}
```


> <span style="color:#7f8c8d;">p.54 ⇄ 书内 p.42</span>

双曲正切是

```math
\tanh(a) = \frac{\mathrm{e}^{a} - \mathrm{e}^{-a}}{\mathrm{e}^{a} + \mathrm{e}^{-a}},
```

所以

```math
\begin{aligned}
f(a) \equiv \frac{1}{1 + \exp(-a)} &= \frac{1}{2}\left(\frac{1 - \mathrm{e}^{-a}}{1 + \mathrm{e}^{-a}} + 1\right) \\
&= \frac{1}{2}\,\frac{\mathrm{e}^{a/2} - \mathrm{e}^{-a/2}}{\mathrm{e}^{a/2} + \mathrm{e}^{-a/2}} + \frac{1}{2} = \frac{1}{2}\left(\tanh(a/2) + 1\right). \tag{2.67}
\end{aligned}
```

在 $b = \log_2 p/q$ 的情形下，我们可以重复步骤 (2.63–2.65)，把 $\mathrm{e}$ 换成 2，得到

```math
p = \frac{1}{1 + 2^{-b}}. \tag{2.68}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.18（习题 2.18 的解答，p.36）

```math
P(x \mid y) = \frac{P(y \mid x)\,P(x)}{P(y)} \tag{2.69}
```

```math
\Rightarrow \quad \frac{P(x = 1 \mid y)}{P(x = 0 \mid y)} = \frac{P(y \mid x = 1)}{P(y \mid x = 0)}\,\frac{P(x = 1)}{P(x = 0)} \tag{2.70}
```

```math
\Rightarrow \quad \log \frac{P(x = 1 \mid y)}{P(x = 0 \mid y)} = \log \frac{P(y \mid x = 1)}{P(y \mid x = 0)} + \log \frac{P(x = 1)}{P(x = 0)}. \tag{2.71}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.19（习题 2.19 的解答，p.36）

$d_1$ 与 $d_2$ 在给定 $x$ 下的条件独立性意味着

```math
P(x, d_1, d_2) = P(x)\,P(d_1 \mid x)\,P(d_2 \mid x). \tag{2.72}
```

这使得 posterior probability ratio 可以分解为一串因子之积 —— 每个 data point 一个因子 —— 再乘以 prior probability ratio。

```math
\frac{P(x = 1 \mid \{d_i\})}{P(x = 0 \mid \{d_i\})} = \frac{P(\{d_i\} \mid x = 1)}{P(\{d_i\} \mid x = 0)}\,\frac{P(x = 1)}{P(x = 0)} \tag{2.73}
```

```math
= \frac{P(d_1 \mid x = 1)}{P(d_1 \mid x = 0)}\,\frac{P(d_2 \mid x = 1)}{P(d_2 \mid x = 0)}\,\frac{P(x = 1)}{P(x = 0)}. \tag{2.74}
```

#### Life in high-dimensional spaces（高维空间中的生活）

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.20（习题 2.20 的解答，p.37）

$N$ 维空间中半径为 $r$ 的超球体积其实是

```math
V(r, N) = \frac{\pi^{N/2}\,r^{N}}{(N/2)!}, \tag{2.75}
```

但你并不需要知道这个。对本题，我们只需要它对 $r$ 的依赖关系：$V(r, N) \propto r^{N}$。于是 $(r - \epsilon, r)$ 中的体积占比为

```math
\frac{r^{N} - (r - \epsilon)^{N}}{r^{N}} = 1 - \left(1 - \frac{\epsilon}{r}\right)^{N}. \tag{2.76}
```

本题所要求各情形下的壳层体积占比为：

| | $N = 2$ | $N = 10$ | $N = 1000$ |
|:--|:--:|:--:|:--:|
| $\epsilon/r = 0.01$ | 0.02 | 0.096 | 0.99996 |
| $\epsilon/r = 0.5$ | 0.75 | 0.999 | $1 - 2^{-1000}$ |

注意：无论 $\epsilon$ 多小，只要 $N$ 足够大，几乎全部概率质量都落在厚度为 $\epsilon$ 的表面壳层里。


> <span style="color:#7f8c8d;">p.55 ⇄ 书内 p.43</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.21（习题 2.21 的解答，p.37）

$p_a = 0.1$、$p_b = 0.2$、$p_c = 0.7$，$f(a) = 10$、$f(b) = 5$、$f(c) = 10/7$。

```math
\mathbb{E}[f(x)] = 0.1 \times 10 + 0.2 \times 5 + 0.7 \times 10/7 = 3. \tag{2.77}
```

对每个 $x$ 都有 $f(x) = 1/P(x)$，所以

```math
\mathbb{E}[1/P(x)] = \mathbb{E}[f(x)] = 3. \tag{2.78}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.22（习题 2.22 的解答，p.37）

对一般的 $X$，

```math
\mathbb{E}[1/P(x)] = \sum_{x \in \mathcal{A}_X} P(x)\,\frac{1}{P(x)} = \sum_{x \in \mathcal{A}_X} 1 = |\mathcal{A}_X|. \tag{2.79}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.23（习题 2.23 的解答，p.37）

$p_a = 0.1$、$p_b = 0.2$、$p_c = 0.7$，$g(a) = 0$、$g(b) = 1$、$g(c) = 0$。

```math
\mathbb{E}[g(x)] = p_b = 0.2. \tag{2.80}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.24（习题 2.24 的解答，p.37）

```math
P\left(P(x) \in [0.15, 0.5]\right) = p_b = 0.2. \tag{2.81}
```

```math
P\left(\log \frac{P(x)}{0.2} > 0.05\right) = p_a + p_c = 0.8. \tag{2.82}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.25（习题 2.25 的解答，p.37）

这类问题有两种切入方式：或者对待极大化的函数求导、求极值点、再证明它是全局最大值 —— 这一策略有风险，因为函数的最大值可能落在空间边界上、落在导数不等于零的地方；或者，精心选择一个不等式来确立答案。第二种方法干净得多。

**Proof by differentiation (not the recommended method)（用微分证明，不推荐）。** 由于对 $\ln 1/p$ 求导比对 $\log_2 1/p$ 略容易，我们暂时改用自然对数来度量 $H(X)$，这相当于把它按因子 $\log_2 \mathrm{e}$ 缩放。

```math
H(X) = \sum_i p_i \ln \frac{1}{p_i} \tag{2.83}
```

```math
\frac{\partial H(X)}{\partial p_i} = \ln \frac{1}{p_i} - 1 \tag{2.84}
```

我们在约束 $\sum_i p_i = 1$ 下求极大，该约束可用 Lagrange multiplier（拉格朗日乘子）施加：

```math
G(\mathbf{p}) \equiv H(X) + \lambda\left(\sum_i p_i - 1\right) \tag{2.85}
```

```math
\frac{\partial G(\mathbf{p})}{\partial p_i} = \ln \frac{1}{p_i} - 1 + \lambda. \tag{2.86}
```

在极值点处，

```math
\ln \frac{1}{p_i} - 1 + \lambda = 0 \tag{2.87}
```

```math
\Rightarrow \quad \ln \frac{1}{p_i} = 1 - \lambda, \tag{2.88}
```

所以所有 $p_i$ 都相等。这个极值点确实是最大值，可由曲率看出：

```math
\frac{\partial^2 G(\mathbf{p})}{\partial p_i \partial p_j} = -\frac{1}{p_i}\,\delta_{ij}, \tag{2.89}
```

它是负定的（negative definite）。∎


> <span style="color:#7f8c8d;">p.56 ⇄ 书内 p.44（习题 2.25 的第二种证明）</span>

**Proof using Jensen's inequality (recommended method)（用 Jensen 不等式证明，推荐方法）。** 先回顾一下这条不等式。

> <span style="color:#00838f;">若 $f$ 是 convex function，$x$ 是随机变量，则 $\mathbb{E}[f(x)] \ge f(\mathbb{E}[x])$。若 $f$ 是 strictly convex 的，且 $\mathbb{E}[f(x)] = f(\mathbb{E}[x])$，则随机变量 $x$ 是常数（以概率 1）。</span>

用 Jensen's inequality 做证明的诀窍，在于选对函数、选对随机变量。我们可以定义

```math
f(u) = \log \frac{1}{u} = -\log u \tag{2.90}
```

（这是个 convex function），并把 $H(X) = \sum_i p_i \log \frac{1}{p_i}$ 看成 $f(u)$ 在 $u = P(x)$ 下的均值；但这样走不通 —— 它会给出**方向相反**的不等式。若改而定义

```math
u = 1/P(x), \tag{2.91}
```

就得到：

```math
H(X) = -\mathbb{E}\left[f(1/P(x))\right] \le -f\left(\mathbb{E}[1/P(x)]\right); \tag{2.92}
```

而由习题 2.22（p.37）我们知道 $\mathbb{E}[1/P(x)] = |\mathcal{A}_X|$，所以

```math
H(X) \le -f(|\mathcal{A}_X|) = \log |\mathcal{A}_X|. \tag{2.93}
```

等号仅在随机变量 $u = 1/P(x)$ 为常数时成立，也就是说，对所有 $x$ 都有 $P(x)$ 相同。∎

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.26（习题 2.26 的解答，p.37）

```math
\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}. \tag{2.94}
```

我们用 Jensen's inequality 来证明 Gibbs' inequality。令 $f(u) = \log 1/u$，并令 $u = Q(x)/P(x)$。则

```math
\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) = \mathbb{E}\left[f\left(Q(x)/P(x)\right)\right] \tag{2.95}
```

```math
\ge f\left(\sum_x P(x)\,\frac{Q(x)}{P(x)}\right) = f\left(\sum_x Q(x)\right) = \log 1 = 0, \tag{2.96}
```

等号仅在 $u = Q(x)/P(x)$ 为常数时成立，即 $Q(x) = P(x)$。∎

**Second solution（第二个解）。** 上述证明中的 expectation 是关于概率分布 $P(x)$ 取的。另一个解法改用 $Q(x)$ 来施加 Jensen's inequality。我们定义 $f(u) = u \log u$，并令 $u = P(x)/Q(x)$。则

```math
\mathrm{D}_{\mathrm{KL}}(P\,\|\,Q) = \sum_x Q(x)\,\frac{P(x)}{Q(x)} \log \frac{P(x)}{Q(x)} = \sum_x Q(x)\, f\!\left(\frac{P(x)}{Q(x)}\right) \tag{2.97}
```

```math
\ge f\left(\sum_x Q(x)\,\frac{P(x)}{Q(x)}\right) = f(1) = 0, \tag{2.98}
```

等号仅在 $u = P(x)/Q(x)$ 为常数时成立，即 $Q(x) = P(x)$。∎


> <span style="color:#7f8c8d;">p.57 ⇄ 书内 p.45</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.28（习题 2.28 的解答，p.38）

```math
H(X) = H_2(f) + f\,H_2(g) + (1 - f)\,H_2(h). \tag{2.99}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.29（习题 2.29 的解答，p.38）

先有 $x - 1$ 个反面、随即出现一个正面（于是第一次正面出现在第 $x$ 次投掷）的概率是

```math
P(x) = (1 - f)^{x-1} f. \tag{2.100}
```

若第一次投掷是反面，那么未来的概率分布看起来与第一次投掷之前完全一样。于是我们得到 entropy 的递归表达：

```math
H(X) = H_2(f) + (1 - f)\,H(X). \tag{2.101}
```

整理得

```math
H(X) = H_2(f)/f. \tag{2.102}
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.34（习题 2.34 的解答，p.38）

反面个数 $t$ 的概率为

```math
P(t) = \left(\frac{1}{2}\right)^{t}\frac{1}{2}, \quad \text{for } t \ge 0. \tag{2.103}
```

正面个数的期望按题目设定为 1。反面个数的期望是

```math
\mathbb{E}[t] = \sum_{t=0}^{\infty} t \left(\frac{1}{2}\right)^{t}\frac{1}{2}, \tag{2.104}
```

可以有好几种方法证明它等于 1。例如，由于掷出一个反面之后的处境与开局处境等价，我们可以写下递推关系

```math
\mathbb{E}[t] = \tfrac{1}{2}\left(1 + \mathbb{E}[t]\right) + \tfrac{1}{2}\,0 \quad \Rightarrow \quad \mathbb{E}[t] = 1. \tag{2.105}
```

在 $f = 1/2$ 的前提下，「估计量」（estimator）$\hat{f} = 1/(1 + t)$ 的概率分布绘于图 2.12。$\hat{f}$ 的概率就是相应 $t$ 取值的概率。

[Figure 2.12：估计量 $\hat{f} = 1/(1+t)$ 在 $f = 1/2$ 时的概率分布曲线 —— 横轴 $\hat{f}$ 从 0 到 1，纵轴概率从 0 到 0.5，质量集中在 $\hat{f}$ 较小的一端]

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.35（习题 2.35 的解答，p.38）

(a) 从一个六到下一个六之间的平均投掷次数是六（假定我们从两个六中的第一个之后开始计数）。下一个六出现在第 $r$ 次投掷的概率，是「此前 $r - 1$ 次都没出六」的概率乘以「这一次出六」的概率：

```math
P(r_1 = r) = \left(\frac{5}{6}\right)^{r-1}\frac{1}{6}, \quad \text{for } r \in \{1, 2, 3, \ldots\}. \tag{2.106}
```

这个「投掷次数 $r$」的概率分布可以称为 exponential distribution（指数分布），因为

```math
P(r_1 = r) = \mathrm{e}^{-\alpha r}/Z, \tag{2.107}
```

其中 $\alpha = \ln(6/5)$，$Z$ 是归一化常数。

(b) 从钟声响起之时到下一个六之间的平均投掷次数是六。

(c) 逆着时间往回看，从此刻回到最近一个六之间的平均投掷次数也是六。


> <span style="color:#7f8c8d;">p.58 ⇄ 书内 p.46</span>

(d) 从钟响之前的那个六，到钟响之后的那个六，平均投掷次数是 (b) 与 (c) 两答案之和再减一，即十一。

(e) 与其直接解释 (a) 与 (d) 的差别，不如再给一个提示。设想 Poissonville 的公交车独立地随机到达（一个 Poisson process），平均每六分钟一班。设想乘客以均匀的速率到达车站，被公交车毫不延迟地捞走，于是两班车之间的间隔保持不变。那些跟在前车间隔大于六分钟之后到达的车，会变得过度拥挤。乘客代表抱怨说：有三分之二的乘客发现自己挤在过度拥挤的车上。公交运营方则声称：「不不 —— 我们只有三分之一的班次是拥挤的。」这两个说法能同时为真吗？

[Figure 2.13：从一次六到下一次六的投掷次数 $r_1$ 的概率分布（实线），$P(r_1 = r) = \left(\tfrac{5}{6}\right)^{r-1}\tfrac{1}{6}$；以及从下午 1 点前那个六到下一个六的投掷次数 $r_{\text{tot}}$ 的概率分布（虚线），$P(r_{\text{tot}} = r) = r\left(\tfrac{5}{6}\right)^{r-1}\tfrac{1}{6}$。$P(r_1 > 6)$ 约为 $1/3$，$P(r_{\text{tot}} > 6)$ 约为 $2/3$。$r_1$ 的均值为 6，$r_{\text{tot}}$ 的均值为 11]

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.38（习题 2.38 的解答，p.39）

**Binomial distribution method（二项分布法）。** 由习题 1.2 的解答，$p_B = 3f^2(1 - f) + f^3$。

**Sum rule method（sum rule 法）。** $r$ 的八个取值的边缘概率，可用下式说明：

```math
P(r = 000) = \tfrac{1}{2}(1 - f)^3 + \tfrac{1}{2}f^3, \tag{2.108}
```

```math
P(r = 001) = \tfrac{1}{2}f(1 - f)^2 + \tfrac{1}{2}f^2(1 - f) = \tfrac{1}{2}f(1 - f). \tag{2.109}
```

posterior probabilities 由下式代表：

```math
P(s = 1 \mid r = 000) = \frac{f^3}{(1 - f)^3 + f^3} \tag{2.110}
```

以及

```math
P(s = 1 \mid r = 001) = \frac{\tfrac{1}{2}f^2(1 - f)}{\tfrac{1}{2}f(1 - f)^2 + \tfrac{1}{2}f^2(1 - f)} = f. \tag{2.111}
```

于是这些代表性情形下的出错概率为

```math
P(\text{error} \mid r = 000) = \frac{f^3}{(1 - f)^3 + f^3} \tag{2.112}
```

以及

```math
P(\text{error} \mid r = 001) = f. \tag{2.113}
```

注意：虽然 $R_3$ 的平均出错概率约为 $3f^2$，但在给定 $r$ 的条件下，任何一个特定位出错的概率要么约为 $f^3$，要么为 $f$。

用 sum rule 求平均出错概率：

```math
\begin{aligned}
P(\text{error}) &= \sum_r P(r)\,P(\text{error} \mid r) \\
&= 2\left[\tfrac{1}{2}(1 - f)^3 + \tfrac{1}{2}f^3\right]\frac{f^3}{(1 - f)^3 + f^3} + 6\left[\tfrac{1}{2}f(1 - f)\right] f.
\end{aligned}
```

> <span style="color:#7f8c8d;">前两项对应 $r = 000$ 与 $111$ 两种情形；其余六项对应其他结果，它们出现的概率相同、出错概率也相同，都是 $f$。</span>

于是

```math
P(\text{error}) = f^3 + 3f^2(1 - f).
```

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 2.39（习题 2.39 的解答，p.40）

entropy 为每个词 9.7 bits。


> <span style="color:#7f8c8d;">p.59 ⇄ 书内 p.47</span>

### About Chapter 3（关于第 3 章）

如果你急着进入信息论、数据压缩与噪声信道的内容，可以直接跳到第 4 章。然而数据压缩与数据建模是紧密相连的，所以等你读到第 6 章时，大概会想回到本章来。在读第 3 章之前，先看看下面几道练习会有好处。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.1. <span style="color:#7f8c8d;">[2, p.59]</span>

A die is selected at random from two twenty-faced dice on which the symbols $1$–$10$ are written with nonuniform frequency as follows.

| Symbol | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Number of faces of die A | 6 | 4 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 0 |
| Number of faces of die B | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1 |

The randomly chosen die is rolled 7 times, with the following outcomes: $5, 3, 9, 3, 8, 4, 7$.

What is the probability that the die is die A?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.2. <span style="color:#7f8c8d;">[2, p.59]</span>

Assume that there is a third twenty-faced die, die C, on which the symbols $1$–$20$ are written once each. As above, one of the three dice is selected at random and rolled 7 times, giving the outcomes: $3, 5, 4, 8, 3, 9, 7$.

What is the probability that the die is (a) die A, (b) die B, (c) die C?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.3. <span style="color:#7f8c8d;">[3, p.48]</span>

Inferring a decay constant（推断衰减常数）

Unstable particles are emitted from a source and decay at a distance $x$, a real number that has an exponential probability distribution with characteristic length $\lambda$. Decay events can be observed only if they occur in a window extending from $x = 1\ \mathrm{cm}$ to $x = 20\ \mathrm{cm}$. $N$ decays are observed at locations $\{x_1, \ldots, x_N\}$. What is $\lambda$?

```
*  **  *   *    *     *
              x
```

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.4. <span style="color:#7f8c8d;">[3, p.55]</span>

Forensic evidence（法庭证据）

Two people have left traces of their own blood at the scene of a crime. A suspect, Oliver, is tested and found to have type 'O' blood. The blood groups of the two traces are found to be of type 'O' (a common type in the local population, having frequency 60%) and of type 'AB' (a rare type, with frequency 1%). Do these data (type 'O' and 'AB' blood were found at scene) give evidence in favour of the proposition that Oliver was one of the two people present at the crime?


> <span style="color:#7f8c8d;">p.60 ⇄ 书内 p.48</span>

## 3 More about Inference（再谈推断）

> <span style="color:#00838f;">「Bayes' theorem 为「描述在噪声信道上传递的消息之推断」提供了正确的语言」—— 这并不是一个有争议的说法，第 1 章（p.6）我们已经这样用过它。但奇怪的是，一旦涉及其他推断问题，Bayes' theorem 的使用却并不那么普遍。</span>

### 3.1 A first inference problem（第一个推断问题）

我在剑桥读本科时，有幸受教于 Steve Gull 的 supervisions（小班辅导）。在圣约翰学院他那间凌乱的办公室里，坐在他的书桌前，我问他：一道古老的 Tripos 考题（习题 3.3）应当怎么解？

> <span style="color:#00838f;">不稳定粒子自源中发射出，在距离 $x$ 处衰变，$x$ 是实数，服从特征长度为 $\lambda$ 的指数概率分布。只有当衰变事件落在 $x = 1\ \mathrm{cm}$ 到 $x = 20\ \mathrm{cm}$ 的窗口之内时，才能被观测到。在位置 $\{x_1, \ldots, x_N\}$ 观测到 $N$ 次衰变。$\lambda$ 是多少？</span>

```
*  **  *   *    *     *
              x
```

我为这道题挠了好一阵头。我所受的教育提供了几种解决此类推断问题的路径：构造未知参数的「estimators」（估计量）；或者把模型「拟合」到 data 上，或拟合到 data 的某个加工版本上。

既然无约束指数分布的均值为 $\lambda$，那么考察样本均值 $\bar{x} = \sum_n x_n / N$、看看能否由它得到某个估计量 $\hat{\lambda}$，看起来是合理的。显然，估计量 $\hat{\lambda} = \bar{x}^{-1}$ 在 $\lambda \ll 20\ \mathrm{cm}$ 时是恰当的，但当分布右端的截断变得显著时就不行了；稍加巧思、引入一些 ad hoc 的分箱（bins），可以为 $\lambda \ll 20\ \mathrm{cm}$ 构造出不错的估计量。但没有任何一个显然的估计量能在所有条件下都管用。

我也找不到一种令人满意的做法，去把密度 $P(x \mid \lambda)$ 拟合到由 data 导出的直方图上。我卡住了。

这类问题以及类似问题的一般解法是什么？每当面对一个新的推断问题，是否总得在黑暗中摸索恰当的「estimators」、并为寻找「最佳」估计量（不管那是什么意思）而操心？


> <span style="color:#7f8c8d;">p.61 ⇄ 书内 p.49</span>

[Figure 3.1：概率密度 $P(x \mid \lambda)$ 作为 $x$ 的函数图 —— 三条曲线 $\lambda = 2, 5, 10$，横轴 $x$ 从 0 到 20，纵轴密度从 0 到 0.25；三条曲线都是归一化的指数形状]

[Figure 3.2：同一个概率密度 $P(x \mid \lambda)$，改画成 $\lambda$ 的函数 —— 三条曲线对应 $x = 3, 5, 12$，横轴 $\lambda$ 为对数刻度（1 到 100）。这样横过来画时，该函数称为 $\lambda$ 的 likelihood。图中标记出前一幅图所用的三个 $\lambda$ 值：$\lambda = 2, 5, 10$]

[Figure 3.3：$P(x \mid \lambda)$ 作为 $x$ 与 $\lambda$ 两个变量的曲面图 —— 图 3.1 与图 3.2 都是这张曲面的竖直截面]

Steve 写下了「给定 $\lambda$ 时单个 data point 的概率」：

```math
P(x \mid \lambda) = \begin{cases} \dfrac{1}{\lambda}\,\mathrm{e}^{-x/\lambda} \big/ Z(\lambda), & 1 < x < 20 \\ 0, & \text{otherwise} \end{cases} \tag{3.1}
```

其中

```math
Z(\lambda) = \int_1^{20} \mathrm{d}x\;\frac{1}{\lambda}\,\mathrm{e}^{-x/\lambda} = \mathrm{e}^{-1/\lambda} - \mathrm{e}^{-20/\lambda}. \tag{3.2}
```

这看起来足够显然。接着他写下了 Bayes' theorem：

```math
P(\lambda \mid \{x_1, \ldots, x_N\}) = \frac{P(\{x\} \mid \lambda)\,P(\lambda)}{P(\{x\})} \tag{3.3}
```

```math
\propto \frac{1}{\left(\lambda Z(\lambda)\right)^{N}} \exp\left(-\sum_n x_n/\lambda\right) P(\lambda). \tag{3.4}
```

突然间，那个直截了当的分布 $P(\{x_1, \ldots, x_N\} \mid \lambda)$ —— 它定义的是「给定假设 $\lambda$ 时 data 的概率」—— 被整个翻转过来，变成了「给定 data 时假设的概率」。一幅简单的图把单个 data point 的概率 $P(x \mid \lambda)$ 画成 $x$ 的熟悉函数、对不同 $\lambda$ 各画一条（图 3.1）。每条曲线都是无害的指数形状，归一化为面积 1。把同一个函数对固定的 $x$ 改画成 $\lambda$ 的函数，一件值得注意的事情发生了：**峰冒出来了**（图 3.2）。为帮助理解这一个函数的这两种视角，图 3.3 画出了 $P(x \mid \lambda)$ 作为 $x$ 与 $\lambda$ 的函数之曲面图。

对于一个由若干点组成的数据集，例如六点 $\{x\}_{n=1}^{N} = \{1.5, 2, 3, 4, 5, 12\}$，likelihood function $P(\{x\} \mid \lambda)$ 就是 $N$ 个 $\lambda$ 的函数 $P(x_n \mid \lambda)$ 的乘积（图 3.4）。

[Figure 3.4：六点数据集下的 likelihood function $P(\{x\} = \{1.5, 2, 3, 4, 5, 12\} \mid \lambda)$ 作为 $\lambda$ 的函数图 —— 横轴 $\lambda$ 为对数刻度，峰值位于 $\lambda \approx 3$ 附近，量级 $10^{-6}$]


> <span style="color:#7f8c8d;">p.62 ⇄ 书内 p.50</span>

Steve 把 Bayes' theorem 的实质总结为一句话：

> <span style="color:#00838f;">data 到来之后你对 $\lambda$ 的认识，等于你**原先**知道的 $[P(\lambda)]$，加上 data 告**诉**你的 $[P(\{x\} \mid \lambda)]$。</span>

这里用概率来量化置信度（degree of belief）。为把可能的混淆在根上掐掉，必须强调：正确描述该情形的假设 $\lambda$ **并不是一个随机变量**；Bayesian 使用概率分布 $P$ 这一事实，并不意味着他认为世界会在不同假设所描述的状态之间随机地改变本性。他只是用概率这套记号来表达他对若干互斥的 micro-hypotheses（此处即 $\lambda$ 的各个取值）的信念，而这些 micro-hypotheses 中只有一个实际为真。概率可以表示「在给定假设下的置信度」—— 在我看来这是合理的。

posterior probability distribution (3.4) 是这个问题的**唯一且完整**的解。既不需要发明「estimators」，也不需要发明用来互相比较不同估计量的准则。正统统计学家给出二十种解题方法，再加另外二十种不同准则去判定这些解法中哪个最好；而 Bayesian statistics 对一个提法良好的问题只给一个答案。

> <span style="color:#7f8c8d;">若你在理解本章时遇到困难，我建议先确认自己对习题 3.1 与 3.2（p.47）没有疑问，然后注意它们与习题 3.3 的相似之处。</span>

### Assumptions in inference（推断中的假设）

我们的推断以我们的假设为条件〔例如 prior $P(\lambda)$〕。批评者把这类 priors 视为难题，因为它们是「主观的」；可我看不出还能怎样。不做假设，怎么可能做推断？我认为 Bayesian 方法迫使一个人把这些默会假设明确写出来，这一点价值极大。

**第一**，假设一旦给定，推断就是客观且唯一的 —— 任何掌握相同信息、做出相同假设的人都能完全一致地复现它。例如，给定上面列出的一整套假设 $H$ 与 data $D$，每个人都会同意衰减长度 $\lambda$ 的 posterior probability：

```math
P(\lambda \mid D, H) = \frac{P(D \mid \lambda, H)\,P(\lambda \mid H)}{P(D \mid H)}. \tag{3.5}
```

**第二**，假设一旦明确写出，就更容易被批评、也更容易修改 —— 事实上，我们还可以定量地刻画我们的推断对假设细节的敏感程度。例如，从图 3.2 的 likelihood 曲线可以注意到：在单个 data point 落在 $x = 5$ 的情形下，likelihood function 的峰比 $x = 3$ 的情形更平缓；样本均值 $\bar{x}$ 越接近窗口中央 10.5，prior $P(\lambda)$ 的细节就越重要。在 $x = 12$ 的情形下，likelihood function 根本没有峰 —— 这样的 data 只是排除了较小的 $\lambda$ 取值，对较大的 $\lambda$ 取值的相对概率不给任何信息。所以这种情形下，prior 在小 $\lambda$ 一端的细节不重要，而大 $\lambda$ 一端的 prior 才是重要的。

**第三**，当我们不确定若干替代假设中哪一个最适合某个问题时，可以把这个问题本身当作又一个推断任务。于是给定 data $D$，我们可以用 Bayes' theorem 比较各替代假设 $H$：

```math
P(H \mid D, I) = \frac{P(D \mid H, I)\,P(H \mid I)}{P(D \mid I)}, \tag{3.6}
```
