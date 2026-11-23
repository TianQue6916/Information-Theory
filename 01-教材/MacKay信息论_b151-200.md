<!-- 书页 151–200｜来源：A+B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->


<span style="color:#7f8c8d">书内 p151 ｜ 9.6: The noisy-channel coding theorem</span>

我们还能做到多好？由对称性，optimal input distribution 是 $\{0.5, 0.5\}$，capacity 是

```math
C(Q_{\text{BSC}}) = H_2(0.5) - H_2(0.15) = 1.0 - 0.61 = 0.39\ \text{bits}. \qquad (9.11)
```

我们稍后会为这个对称性论证给出理由。如果对对称性论证有任何怀疑，我们总可以退回对 mutual information $I(X; Y)$ 作显式最大化，

```math
I(X; Y) = H_2\big((1-f)p_1 + (1-p_1)f\big) - H_2(f) \qquad (\text{figure } 9.2). \qquad (9.12)
```

[Figure 9.2：binary symmetric channel 在 $f = 0.15$ 时的 mutual information $I(X; Y)$ 随 input distribution（横轴 $p_1$ 从 0 到 1）变化的曲线。纵轴 0 到 0.4，曲线在 $p_1 = 0.5$ 处取峰值约 0.39。]

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.10（例 9.10）</span>

noisy typewriter（含噪打字机）。optimal input distribution 是 $x$ 上的均匀分布，给出 $C = \log_2 9$ bits。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.11（例 9.11）</span>

考虑 $f = 0.15$ 的 Z channel。要确定 optimal input distribution 就没那么直接了。我们对 $P_X = \{p_0, p_1\}$ 显式地算出 $I(X; Y)$。首先需要算出 $P(y)$。其中 $y = 1$ 的概率最容易写下来：

```math
P(y = 1) = p_1 (1 - f). \qquad (9.13)
```

于是 mutual information 是：

```math
I(X; Y) = H(Y) - H(Y \mid X) = H_2\big(p_1(1-f)\big) - \big(p_0 H_2(0) + p_1 H_2(f)\big) = H_2\big(p_1(1-f)\big) - p_1 H_2(f). \qquad (9.14)
```

[Figure 9.3：Z channel 在 $f = 0.15$ 时的 mutual information $I(X; Y)$ 随 input distribution（横轴 $p_1$）变化的曲线。纵轴 0 到 0.7，曲线在 $p_1 \approx 0.445$ 处取峰值约 0.685，明显偏离 $p_1 = 0.5$。]

这是 $p_1$ 的一个非平凡函数，见图 9.3。对 $f = 0.15$，它在 $p_1^* = 0.445$ 处取最大。我们算得 $C(Q_Z) = 0.685$。注意 optimal input distribution 并不是 $\{0.5, 0.5\}$。通过比使用输入符号 1 更频繁地使用输入符号 0，我们可以多传递一点信息。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.12 [1, p.158]</span>

What is the capacity of the binary symmetric channel for general $f$?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.13 [2, p.158]</span>

Show that the capacity of the binary erasure channel with $f = 0.15$ is $C_{\text{BEC}} = 0.85$. What is its capacity for general $f$? Comment.

### 9.6 The noisy-channel coding theorem（含噪信道编码定理）

我们定义的这个「capacity」看上去有可能是对 channel 所传递信息量的一种度量；但尚不明显的是——而这正是我们将在下一章证明的东西——capacity 是否真的度量了数据 block 能够在那个 channel 上以任意小 error probability 传输的速率。

我们作如下定义。

channel $Q$ 上的一个 $(N, K)$ block code（分组码）是一列 $S = 2^K$ 个 codeword（码字）

```math
\{ x(1), x(2), \ldots, x(2^K) \}, \qquad x^{(s)} \in \mathcal{A}_X^N,
```

每个 codeword 长度都是 $N$。用这个码，我们可以把一个 signal $s \in \{1, 2, 3, \ldots, 2^K\}$ 编码为 $x^{(s)}$。[codeword 的个数 $S$ 是整数，但通过选定一个 codeword 所指定的 bit 数 $K \equiv \log_2 S$ 不一定是整数。]


<span style="color:#7f8c8d">书内 p152 ｜ 9 -- Communication over a Noisy Channel</span>

码的 rate（码率）是 $R = K/N$ bits per channel use（每次使用信道所传的 bit 数）。[我们对任何 channel 都采用这个 rate 定义，不只是输入为二进制的 channel；但请注意，有时学界习惯把输入符号数为 $q$ 的 channel 上码的 rate 定义为 $K/(N \log q)$。]

$(N, K)$ block code 的 decoder（解码器）是从长度为 $N$ 的 channel 输出串集合 $\mathcal{A}_Y^N$ 到 codeword 标号 $\hat{s} \in \{0, 1, 2, \ldots, 2^K\}$ 的一个 mapping（映射）。多出来的符号 $\hat{s} = 0$ 可以用来表示「失败」。

给定 channel、给定被编码 signal 上的概率分布 $P(s_{\text{in}})$，一个码连同 decoder 的 probability of block error（块错误概率）是：

```math
p_B = \sum_{s_{\text{in}}} P(s_{\text{in}}) \, P(s_{\text{out}} \ne s_{\text{in}} \mid s_{\text{in}}). \qquad (9.15)
```

maximal probability of block error（最大块错误概率）是

```math
p_{BM} = \max_{s_{\text{in}}} P(s_{\text{out}} \ne s_{\text{in}} \mid s_{\text{in}}). \qquad (9.16)
```

channel code 的 optimal decoder 是使 probability of block error 最小的那个。它把一个输出 $y$ 解码为使 posterior probability（后验概率）$P(s \mid y)$ 最大的输入 $s$。

```math
P(s \mid y) = \frac{P(y \mid s) P(s)}{\sum_{s'} P(y \mid s') P(s')} \qquad (9.17)
```

```math
\hat{s}_{\text{optimal}} = \arg\max P(s \mid y). \qquad (9.18)
```

通常假定 $s$ 上取均匀先验分布，此时 optimal decoder 同时也是 maximum likelihood decoder（最大似然解码器），即把输出 $y$ 映射到使 likelihood（似然）$P(y \mid s)$ 最大的输入 $s$ 的那个 decoder。

bit error 的概率 $p_b$ 是这样定义的：设 codeword 编号 $s$ 用一个长 $K$ bit 的二进制向量 $\mathbf{s}$ 表示；$p_b$ 就是 $s_{\text{out}}$ 的某一位不等于 $s_{\text{in}}$ 对应位的平均概率（对全部 $K$ 个 bit 取平均）。

#### <span style="color:#c0392b">Shannon's noisy-channel coding theorem (part one)（Shannon 含噪信道编码定理·第一部分）</span>

对每一个 discrete memoryless channel（离散无记忆信道），都联系着一个非负数 $C$（称为 channel capacity），它具有如下性质：对任意 $\epsilon > 0$ 与任意 $R < C$，当 $N$ 足够大时，存在一个长度为 $N$、rate $\ge R$ 的 block code 以及一个 decoding algorithm，使得 maximal probability of block error $< \epsilon$。

[Figure 9.4：$R$–$p_{BM}$ 平面上被 Shannon 含噪信道编码定理第一部分所断言为 achievable（可达）的那块区域：$R < C$ 且 $p_{BM}$ 任意的部分。]

#### 对 noisy typewriter channel 验证该定理

在 noisy typewriter 的情形下，我们可以很容易地验证该定理，因为我们可以用一个长度为 $N = 1$ 的 block code 造出完全无错的通信方案：我们只用字母 B、E、H、……、Z，也就是每隔两个字母取一个（每三个字母取一个）。这些字母构成输入 alphabet 的一个 non-confusable subset（不可混淆子集，见图 9.5）。任何输出都能被唯一解码。这个 non-confusable subset 中的输入个数是 9，因此该系统的无错信息率是 $\log_2 9$ bits，它等于我们在例 9.10（p.151）中算出的 capacity $C$。


<span style="color:#7f8c8d">书内 p153 ｜ 9.7: Intuitive preview of proof</span>

[Figure 9.5：noisy typewriter 的 non-confusable 输入子集。26 个字母加连字符排成一圈，每个输入映射到它自身与左右邻居（各概率 1/3）。取 B、E、H、…、Z 这一组（共 9 个）后，任意输出只可能来自其中一个输入，因此可唯一解码。]

[Figure 9.6：由 transition probability（转移概率）为 0.15 的 binary symmetric channel 导出的 extended channels（扩展信道），分别取 $N = 1$、$N = 2$、$N = 4$。$N = 1$ 是两点互连；$N = 2$ 是 4×4 的方格；$N = 4$ 是 16×16 的方格，交叉线越靠中心越粗（概率越大）。]

这如何翻译成定理的各个说法？下表给出解释。

| 定理的说法 | 它如何适用于 noisy typewriter |
|---|---|
| 对每一个 discrete memoryless channel，都联系着一个非负数 $C$。 | capacity $C$ 是 $\log_2 9$。 |
| 对任意 $\epsilon > 0$ 与 $R < C$，当 $N$ 足够大时， | 不管 $\epsilon$ 与 $R$ 是什么，我们都把 blocklength（块长）$N$ 取为 1。 |
| 存在一个长度为 $N$、rate $\ge R$ 的 block code | 该 block code 是 $\{B, E, \ldots, Z\}$。$K$ 的值由 $2^K = 9$ 给出，故 $K = \log_2 9$，于是这个码的 rate 是 $\log_2 9$，大于所要求的 $R$ 值。 |
| 以及一个 decoding algorithm， | decoding algorithm 把收到的字母映射到码中最近的字母； |
| 使得 maximal probability of block error $< \epsilon$。 | maximal probability of block error 为零，从而小于给定的 $\epsilon$。 |

### 9.7 Intuitive preview of proof（证明的直觉预览）

#### Extended channels（扩展信道）

为了对任意给定的 channel 证明该定理，我们考虑相应于 channel 被使用 $N$ 次的 extended channel。extended channel 有 $|\mathcal{A}_X|^N$ 个可能的输入 $x$ 与 $|\mathcal{A}_Y|^N$ 个可能的输出。由 binary symmetric channel 与由 Z channel 得到的 extended channels 分别画在图 9.6 与图 9.7 中，取 $N = 2$ 与 $N = 4$。


<span style="color:#7f8c8d">书内 p154 ｜ 9 -- Communication over a Noisy Channel</span>

[Figure 9.7：由 transition probability 为 0.15 的 Z channel 导出的 extended channels（$N = 1, 2, 4$）。每一列对应一个输入，每一行是一个不同的输出。因为 Z channel 把输入 0 无错传出、把输入 1 以概率 0.15 翻成 0，所以每个输入列的分布是「一个大概率格 + 若干小概率格」的稀疏图案，随 $N$ 增大而更稀疏。]

[Figure 9.8：(a) 相应于 typical inputs（典型输入）$x$ 的一些 typical outputs（典型输出）落在 $\mathcal{A}_Y^N$ 中的位置：每个 typical 输入 $x$ 对应一个圆，圆内是该输入下典型的 $y$ 集合。(b) 从 (a) 中挑出互不重叠的那些 typical 集合——这就是 non-confusable 的子集。此图可与图 9.5 中 noisy typewriter 的解对照。]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.14 [2, p.159]</span>

Find the transition probability matrices $Q$ for the extended channel, with $N = 2$, derived from the binary erasure channel having erasure probability 0.15. By selecting two columns of this transition probability matrix, we can define a rate-1/2 code for this channel with blocklength $N = 2$. What is the best choice of two columns? What is the decoding algorithm?

为了证明 noisy-channel coding theorem，我们要利用大的 blocklength $N$。直觉的想法是：当 $N$ 很大时，extended channel 看上去很像 noisy typewriter。任何特定的输入 $x$ 都很可能产生落在输出 alphabet 的一个小子空间——即给定该输入时的 typical output set（典型输出集）——里的输出。于是我们就能找到一个 non-confusable 的输入子集，它们产生的输出序列基本上互不相交。对给定的 $N$，让我们考虑一种产生这种 non-confusable 输入子集的办法，并数一数它含有多少个互不相同的输入。

想象我们从 ensemble $X^N$ 中抽取输入序列 $x$ 交给 extended channel，这里 $X$ 是输入 alphabet 上任意的 ensemble。回想第 4 章的 source coding theorem，并考虑 probable output sequences（可能出现的输出序列）$y$ 的个数。typical 输出序列 $y$ 的总数是 $2^{N H(Y)}$，它们的概率都差不多。而对任何特定的 typical 输入序列 $x$，大约有 $2^{N H(Y \mid X)}$ 个可能出现的序列。这些 $\mathcal{A}_Y^N$ 的子集在图 9.8a 中用圆圈表示。

现在我们想象把自己限制到 typical 输入 $x$ 的一个子集上，使得相应的 typical output 集合互不重叠，如图 9.8b 所示。于是我们可以通过用 typical $y$ 集合的大小 $2^{N H(Y)}$ 去除以每个 typical-$y$-集合的大小 $2^{N H(Y \mid X)}$，来给出 non-confusable 输入个数的上界。若这些输入是从 typical 输入集合 $x \sim X^N$ 中挑出来的，则 non-confusable 输入的个数 $\le 2^{N H(Y) - N H(Y \mid X)} = 2^{N I(X; Y)}$。


<span style="color:#7f8c8d">书内 p155 ｜ 9.8: Further exercises</span>

如果 $X$ 取为使 $I(X; Y)$ 最大化的那个 ensemble，这个界的最大值就达到，此时 non-confusable 输入的个数 $\le 2^{NC}$。于是渐近地，每一轮至多能传 $C$ bits、而不能更多，并且 error probability 可以忽略。$\square$

这一番勾勒并没有严格证明可靠通信真的可能——那是我们下一章的任务。

### 9.8 Further exercises（进一步习题）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.15 [3, p.159]</span>

Refer back to the computation of the capacity of the Z channel with $f = 0.15$.

(a) Why is $p_1^*$ less than 0.5? One could argue that it is good to favour the 0 input, since it is transmitted without error – and also argue that it is good to favour the 1 input, since it often gives rise to the highly prized 1 output, which allows certain identification of the input! Try to make a convincing argument.

(b) In the case of general $f$, show that the optimal input distribution is

```math
p_1^* = \frac{1/(1-f)}{1 + 2^{\left(H_2(f)/(1-f)\right)}}. \qquad (9.19)
```

(c) What happens to $p_1^*$ if the noise level $f$ is very close to 1?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.16 [2, p.159]</span>

Sketch graphs of the capacity of the Z channel, the binary symmetric channel and the binary erasure channel as a function of $f$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.17 [2]（▷ 标记：书中提示此题为「带陷阱」的题）</span>

What is the capacity of the five-input, ten-output channel whose transition probability matrix is

```math
Q = \begin{pmatrix} 0.25 & 0 & 0 & 0 & 0.25 & 0.25 & 0 & 0 & 0 & 0.25 \\ 0.25 & 0.25 & 0 & 0 & 0 & 0.25 & 0.25 & 0 & 0 & 0 \\ 0 & 0.25 & 0.25 & 0 & 0 & 0 & 0.25 & 0.25 & 0 & 0 \\ 0 & 0 & 0.25 & 0.25 & 0 & 0 & 0 & 0.25 & 0.25 & 0 \\ 0 & 0 & 0 & 0.25 & 0.25 & 0 & 0 & 0 & 0.25 & 0.25 \end{pmatrix} \qquad (9.20)
```

（原书此矩阵在图旁另配了一条曲线图：横轴为 $x \in \{0,1,2,3,4\}$，纵轴为输出标号 $0,\ldots,9$，五条曲线各自覆盖四个相邻输出。）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.18 [2, p.159]</span>

Consider a Gaussian channel with binary input $x \in \{-1, +1\}$ and real output alphabet $\mathcal{A}_Y$, with transition probability density

```math
Q(y \mid x, \alpha, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(y - x\alpha)^2}{2\sigma^2}}, \qquad (9.21)
```

where $\alpha$ is the signal amplitude.

(a) Compute the posterior probability of $x$ given $y$, assuming that the two inputs are equiprobable. Put your answer in the form

```math
P(x = 1 \mid y, \alpha, \sigma) = \frac{1}{1 + e^{-a(y)}}. \qquad (9.22)
```


<span style="color:#7f8c8d">书内 p156 ｜ 9 -- Communication over a Noisy Channel</span>

Sketch the value of $P(x = 1 \mid y, \alpha, \sigma)$ as a function of $y$.

(b) Assume that a single bit is to be transmitted. What is the optimal decoder, and what is its probability of error? Express your answer in terms of the signal-to-noise ratio（信噪比）$\alpha^2/\sigma^2$ and the error function（误差函数，即 Gaussian distribution 的累积分布函数）,

```math
\Phi(z) \equiv \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-\frac{z'^2}{2}} \, dz'. \qquad (9.23)
```

[注意：这里 $\Phi(z)$ 这个 error function 的定义可能与别人的定义不一致。]

#### Pattern recognition as a noisy channel（把模式识别看成一个含噪信道）

我们可以把许多 pattern recognition（模式识别）问题用通信 channel 的语言来思考。考虑识别手写数字（比如信封上的邮政编码）的情形。写数字的人想从集合 $\mathcal{A}_X = \{0, 1, 2, 3, \ldots, 9\}$ 中传递一条 message；这个被选中的 message 就是 channel 的输入。从 channel 出来的东西是纸上的一幅墨迹图案。如果把墨迹图案用 256 个二值 pixel 表示，那么 channel $Q$ 的输出就是一个随机变量 $y \in \mathcal{A}_Y = \{0, 1\}^{256}$。这个 alphabet 中一个元素的样子见页边插图。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.19 [2]</span>

Estimate how many patterns in $\mathcal{A}_Y$ are recognizable as the character '2'. [The aim of this problem is to try to demonstrate the existence of as many patterns as possible that are recognizable as 2s.]

[Figure 9.9：更多「2」的写法。页边一列手写数字 2 的变体样本，笔迹差异极大，用来提示同一个语义类别下图案的空间有多么庞大。]

讨论人们可以怎样为 channel $P(y \mid x = 2)$ 建模。估计概率分布 $P(y \mid x = 2)$ 的 entropy。

做 pattern recognition 的一种策略是：对输入的每个取值 $x = \{0, 1, 2, 3, \ldots, 9\}$ 各建一个 $P(y \mid x)$ 模型，然后用 Bayes' theorem（贝叶斯定理）由 $y$ 反推 $x$。

```math
P(x \mid y) = \frac{P(y \mid x) P(x)}{\sum_{x'} P(y \mid x') P(x')}. \qquad (9.24)
```

这种策略称为 full probabilistic modelling（完全概率建模）或 generative modelling（生成式建模）。当今的语音识别系统本质上就是这么工作的。除了 channel model $P(y \mid x)$ 之外，还要用一个先验概率分布 $P(x)$；在字符识别与语音识别两种情形下，这个先验都是一个 language model（语言模型），它规定在给定上下文、以及该语言已知的文法与统计规律下，下一个字符/词的概率。

#### Random coding（随机编码）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.20 [2, p.160]</span>

Given twenty-four people in a room, what is the probability that there are at least two people present who have the same birthday (i.e., day and month of birth)? What is the expected number of pairs of people with the same birthday? Which of these two questions is easiest to solve? Which answer gives most insight? You may find it helpful to solve these problems and those that follow using notation such as $A$ = number of days in year = 365 and $S$ = number of people = 24.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.21 [2]（▷ 标记）</span>

The birthday problem may be related to a coding scheme. Assume we wish to convey a message to an outsider identifying one of the twenty-four people. We could simply communicate a number $s$ from $\mathcal{A}_S = \{1, 2, \ldots, 24\}$, having agreed a mapping of people onto numbers; alternatively, we could convey a number from $\mathcal{A}_X = \{1, 2, \ldots, 365\}$, identifying the day of the year that is the selected person's birthday (with apologies to leapyearians). [The receiver is assumed to know all the people's birthdays.] What, roughly, is the probability of error of this communication scheme, assuming it is used for a single transmission? What is the capacity of the communication channel, and what is the rate of communication attempted by this scheme?


<span style="color:#7f8c8d">书内 p157 ｜ 9.9: Solutions</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.22 [2]（▷ 标记）</span>

Now imagine that there are $K$ rooms in a building, each containing $q$ people. (You might think of $K = 2$ and $q = 24$ as an example.) The aim is to communicate a selection of one person from each room by transmitting an ordered list of $K$ days (from $\mathcal{A}_X$). Compare the probability of error of the following two schemes.

(a) As before, where each room transmits the birthday of the selected person.

(b) To each $K$-tuple of people, one drawn from each room, an ordered $K$-tuple of randomly selected days from $\mathcal{A}_X$ is assigned (this $K$-tuple has nothing to do with their birthdays). This enormous list of $S = q^K$ strings is known to the receiver. When the building has selected a particular person from each room, the ordered string of days corresponding to that $K$-tuple of people is transmitted.

What is the probability of error when $q = 364$ and $K = 1$? What is the probability of error when $q = 364$ and $K$ is large, e.g. $K = 6000$?

### 9.9 Solutions（习题解答）

#### Solution to exercise 9.2（p.149）

若假定我们观测到 $y = 0$，

```math
P(x = 1 \mid y = 0) = \frac{P(y = 0 \mid x = 1) P(x = 1)}{\sum_{x'} P(y \mid x') P(x')} \qquad (9.25)
```

```math
= \frac{0.15 \times 0.1}{0.15 \times 0.1 + 0.85 \times 0.9} \qquad (9.26)
```

```math
= \frac{0.015}{0.78} = 0.019. \qquad (9.27)
```

#### Solution to exercise 9.4（p.149）

若我们观测到 $y = 0$，

```math
P(x = 1 \mid y = 0) = \frac{0.15 \times 0.1}{0.15 \times 0.1 + 1.0 \times 0.9} \qquad (9.28)
```

```math
= \frac{0.015}{0.915} = 0.016. \qquad (9.29)
```

#### Solution to exercise 9.7（p.150）

$y = 1$ 的概率是 0.5，所以 mutual information 是：

```math
I(X; Y) = H(Y) - H(Y \mid X) \qquad (9.30)
```

```math
= H_2(0.5) - H_2(0.15) \qquad (9.31)
```

```math
= 1 - 0.61 = 0.39\ \text{bits}. \qquad (9.32)
```

#### Solution to exercise 9.8（p.150）

我们再次用 $I(X; Y) = H(Y) - H(Y \mid X)$ 计算 mutual information。$y = 0$ 的概率是 0.575，而


<span style="color:#7f8c8d">书内 p158 ｜ 9 -- Communication over a Noisy Channel</span>

$H(Y \mid X) = \sum_x P(x) H(Y \mid x) = P(x = 1) H(Y \mid x = 1) + P(x = 0) H(Y \mid x = 0)$，于是 mutual information 是：

```math
I(X; Y) = H(Y) - H(Y \mid X) \qquad (9.33)
```

```math
= H_2(0.575) - \left[ 0.5 \times H_2(0.15) + 0.5 \times 0 \right] \qquad (9.34)
```

```math
= 0.98 - 0.30 = 0.679\ \text{bits}. \qquad (9.35)
```

#### Solution to exercise 9.12（p.151）

由对称性，optimal input distribution 是 $\{0.5, 0.5\}$。于是 capacity 是

```math
C = I(X; Y) = H(Y) - H(Y \mid X) \qquad (9.36)
```

```math
= H_2(0.5) - H_2(f) \qquad (9.37)
```

```math
= 1 - H_2(f). \qquad (9.38)
```

你想不借助对称性就求出 optimal input distribution 吗？我们可以对 input ensemble 为 $\{p_0, p_1\}$ 的一般情形算出 mutual information 来做：

```math
I(X; Y) = H(Y) - H(Y \mid X) \qquad (9.39)
```

```math
= H_2\big(p_0 f + p_1(1-f)\big) - H_2(f). \qquad (9.40)
```

对 $p$ 的依赖只出现在第一项 $H_2\big(p_0 f + p_1(1-f)\big)$ 里，而这一项在把自变量设为 0.5 时取最大。取 $p_0 = 1/2$ 即给出该值。

#### Solution to exercise 9.13（p.151）

**Answer 1.** 由对称性，optimal input distribution 是 $\{0.5, 0.5\}$。要算 capacity，最方便的做法是把 mutual information 写成 $I(X; Y) = H(X) - H(X \mid Y)$。conditional entropy（条件熵）$H(X \mid Y)$ 是 $\sum_y P(y) H(X \mid y)$；当 $y$ 已知时，只有当 $y = ?$ 时 $x$ 才不确定，而这件事发生的概率是 $f/2 + f/2$，所以 conditional entropy $H(X \mid Y)$ 是 $f H_2(0.5)$。

```math
C = I(X; Y) = H(X) - H(X \mid Y) \qquad (9.41)
```

```math
= H_2(0.5) - f H_2(0.5) \qquad (9.42)
```

```math
= 1 - f. \qquad (9.43)
```

binary erasure channel 有 $f$ 这么一部分时间处于失效状态。它的 capacity 恰好是 $1 - f$，也就是该 channel 可靠的那部分时间比例。这个结果看起来非常合理，但要用它来编码从而在该 channel 上可靠地通信却远不是显然的事。

**Answer 2.** 另一种做法是不援引上面假定的对称性，而从 input ensemble $\{p_0, p_1\}$ 出发。$y = ?$ 的概率是 $p_0 f + p_1 f = f$，而当我们收到 $y = ?$ 时，$x$ 的后验概率与先验概率相同，所以：

```math
I(X; Y) = H(X) - H(X \mid Y) \qquad (9.44)
```

```math
= H_2(p_1) - f H_2(p_1) \qquad (9.45)
```

```math
= (1 - f) H_2(p_1). \qquad (9.46)
```

当 $p_1 = 1/2$ 时，这个 mutual information 取得其最大值 $(1-f)$。


<span style="color:#7f8c8d">书内 p159 ｜ 9.9: Solutions</span>

[Figure 9.10：(a) 由 erasure probability 为 0.15 的 binary erasure channel 导出的 extended channel（$N = 2$）：$3 \times 3 = 9$ 个输入串（00、01、0?、10、11、1?、?0、?1、??）与 9 个输出串之间的转移，同一个输入行的三个可能输出分别是原样、擦掉一位、擦掉两位。(b) 由 codeword `00` 与 `11` 两列组成的 block code。(c) 这个码的 optimal decoder：把落在上半四个输出格（00、10、01、11 一带）的判为 $\hat{m} = 1$（原文图示按行标注 $\hat{m} = 2/1/0$，$\hat{m}=0$ 表示放弃），把落在下半四个输出格的判为 $\hat{m} = 2$（即 `11` 一路），输出为 `??` 时判为失败。]

#### Solution to exercise 9.14（p.153）

extended channel 见图 9.10。该 channel 在 $N = 2$ 时的最好码，是选取重叠最小的两列，例如列 `00` 与列 `11`。decoding algorithm 这样规定：若 extended channel 的输出落在上面四行之内就返回 `00`，落在下面四行之内就返回 `11`，若输出是 `??` 就放弃。

#### Solution to exercise 9.15（p.155）

在例 9.11（p.151）中我们已经证明，Z channel 的输入与输出之间的 mutual information 是

```math
I(X; Y) = H(Y) - H(Y \mid X) = H_2\big(p_1(1-f)\big) - p_1 H_2(f). \qquad (9.47)
```

我们把这个表达式对 $p_1$ 求导，小心不要把 $\log_2$ 与 $\log_e$ 混起来：

```math
\frac{d}{dp_1} I(X; Y) = (1-f) \log_2 \frac{1 - p_1(1-f)}{p_1(1-f)} - H_2(f). \qquad (9.48)
```

令该导数为零，并用 exercise 2.17（p.36）练出来的技巧整理，我们得到：

```math
p_1^* (1-f) = \frac{1}{1 + 2^{H_2(f)/(1-f)}}, \qquad (9.49)
```

所以 optimal input distribution 是

```math
p_1^* = \frac{1/(1-f)}{1 + 2^{\left(H_2(f)/(1-f)\right)}}. \qquad (9.50)
```

当噪声水平 $f$ 趋于 1 时，这个表达式趋于 $1/e$（可以用 L'Hôpital's rule 证明）。

对一切 $f$ 值，$p_1^*$ 都小于 $1/2$。关于「为什么输入 1 用得比输入 0 少」的一个粗略直觉是：使用输入 1 时含噪 channel 会把 entropy 注入到接收到的串中；而使用输入 0 时噪声的 entropy 为零。

#### Solution to exercise 9.16（p.155）

这三个 channel 的 capacity 如图 9.11 所示。对任何 $f < 0.5$，BEC 是 capacity 最高的 channel，而 BSC 最低。

[Figure 9.11：Z channel、binary symmetric channel、binary erasure channel 三者的 capacity 随 $f$（横轴 0 到 1）变化的曲线。BEC 是直线 $1-f$ 位于最上方；BSC 是 $1 - H_2(f)$ 位于最下方；Z channel 介于两者之间。三条线在 $f = 0.5$ 附近相交，在 $f > 0.5$ 后 Z channel 反而最高。]

#### Solution to exercise 9.18（p.155）

给定 $y$，后验概率比的对数是

```math
a(y) = \ln \frac{P(x = 1 \mid y, \alpha, \sigma)}{P(x = -1 \mid y, \alpha, \sigma)} = \ln \frac{Q(y \mid x = 1, \alpha, \sigma)}{Q(y \mid x = -1, \alpha, \sigma)} = \frac{2\alpha y}{\sigma^2}. \qquad (9.51)
```


<span style="color:#7f8c8d">书内 p160 ｜ 9 -- Communication over a Noisy Channel</span>

用我们从 exercise 2.17（p.36）学到的技巧，把它改写成

```math
P(x = 1 \mid y, \alpha, \sigma) = \frac{1}{1 + e^{-a(y)}}. \qquad (9.52)
```

optimal decoder 选出最可能的假设；这件事只要看 $a(y)$ 的符号就能做到。若 $a(y) > 0$ 就判 $\hat{x} = 1$。error probability 是

```math
p_b = \int_{-\infty}^{0} dy\, Q(y \mid x = 1, \alpha, \sigma) = \int_{-\infty}^{-x\alpha} dy\, \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{y^2}{2\sigma^2}} = \Phi\!\left(\frac{-x\alpha}{\sigma}\right). \qquad (9.53)
```

#### Random coding（随机编码）

#### Solution to exercise 9.20（p.156）

$S = 24$ 个生日从 $A = 365$ 天中随机抽出的、彼此都不同的概率是

```math
\frac{A(A-1)(A-2)\cdots(A-S+1)}{A^S}. \qquad (9.54)
```

两人（或更多人）共有一个生日的概率就是 1 减去这个量；对 $S = 24$、$A = 365$ 它约为 0.5。这种精确回答问题的做法信息量不大，因为看不出概率究竟在 $S$ 取什么值时从接近 0 变成接近 1。

人数对数是 $S(S-1)/2$，而某一特定对共有一个生日的概率是 $1/A$，所以 collision（碰撞）数的期望是

```math
\frac{S(S-1)}{2} \cdot \frac{1}{A}. \qquad (9.55)
```

这个答案更有教益。当 $S \ll \sqrt{A}$ 时 collision 的期望数极小，当 $S \gg \sqrt{A}$ 时很大。

对小的 $S$，我们还可以这样近似「所有生日都不同」的概率：

```math
\frac{A(A-1)(A-2)\cdots(A-S+1)}{A^S} = (1)(1 - 1/A)(1 - 2/A)\cdots(1 - (S-1)/A) \qquad (9.56)
```

```math
\simeq \exp(0)\exp(-1/A)\exp(-2/A)\cdots\exp(-(S-1)/A) \simeq \exp\!\left(-\frac{1}{A}\sum_{i=1}^{S-1} i\right) = \exp\!\left(-\frac{S(S-1)/2}{A}\right). \qquad (9.57)
```

[译注] <span style="color:#1e8449">**「随机编码」为什么是信息论的证明引擎，以及为什么它在这里出现得如此突兀。**

先看机制。上面这一页属于 9.8 节的 Random coding 小节，而这一小节的内容居然全是生日问题（exercise 9.20–9.22）。抽掉随机编码这个想法，整个 noisy-channel coding theorem 的证明会崩在哪？会崩在**存在性与可计算性的分离**上。定理断言「存在一个好码」，但没有任何人知道在 $N$ 很大时怎么构造它、更没法逐个检查某个具体码的 $p_{BM}$。MacKay 的整条证明路线是三步替换：① 不评估某个特定码的错误概率，而评估**所有码的平均**错误概率 $\langle p_B\rangle$；② 用 union bound 把平均值压到 $2\delta$ 以下；③ 用 expurgation（剔除最差的一半 codeword）把「平均小」升级成「maximal 小」。第 ① 步之所以能做，是因为「随机抽 $S$ 个 codeword」这个装置让 $S$ 个 codeword 之间、以及 codeword 与噪声之间**互相独立**——独立性一倒，$\langle p_B\rangle \le \delta + \sum_{s'=2}^{2^{NR'}} 2^{-N(I(X;Y)-3\beta)}$ 这个求和就直接退化成一个无法求和的未知项，$(2^{NR'}-1)$ 个 rival codeword 就不再是「各自独立地以 $2^{-NI}$ 的概率撞上典型集」，证明立刻断掉。所以第 10 章第 10.3 节（PDF p176-179）全部重量压在这个独立性上。

生日问题正是这个机制的最小可玩模型。把 $S$ 个人看作 $S$ 个 codeword，把 $A = 365$ 天看作 output alphabet 的大小，把「两人同生日」看作「两个 codeword 的典型集重叠 / 两个 codeword 在下游不可分辨」。exercise 9.20 逼你算两件事：精确的「至少一对相同」概率（$1 - A!/(A^S (A-S)!)$，$S=24$ 时约 0.5，这个 0.5 反直觉所以是著名的 birthday paradox），以及 collision 数的期望 $S(S-1)/(2A)$。后者的关键性质是**期望的线性性不需要独立性**——这就是 union bound 的原型：$\Pr[\bigcup_i A_i] \le \sum_i \Pr[A_i]$。而转折点在 $S \sim \sqrt{A}$：$S \ll \sqrt{A}$ 时碰撞罕见，$S \gg \sqrt{A}$ 时碰撞必然。翻译成编码语言：codeword 数 $S = 2^{NR}$ 与 output 空间大小 $2^{NH(Y)}$ 相比，临界点是 $2^{NR} \sim 2^{NH(Y)/2}$，即 $R \sim H(Y)/2$；而真正的阈值要从「$S$ 个典型集互不重叠」推出，得 $R < I(X;Y)$。exercise 9.22 就是这一步的显式推演：$q = 364$ 人、$K$ 个房间、$K$ 个日期组成的串，方案 (b)（给每个 $K$-tuple 随机指派一串日期，与真实生日无关）在 $K$ 很大时的错误概率会从「几乎必然错」翻成「几乎必然对」——这正是 random coding 的 shannon 式魔法在玩具规模上的复现。

再看可点开的落点。书本落点：§10.3「Proof of the noisy-channel coding theorem」（PDF p176-179，书内 p164-167）的 random coding + typical-set decoding 五步流程；§10.10 Solutions 里 exercise 10.13（PDF p185-186，书内 p173-174）用 $N = 20$ 条不可分辨的跨大西洋电缆把这件事算成具体数字——那是把 $C = 1 - H_2(p_b)$ 反解成「$p_b$ 要多小才可能」的实例。上游落点：第 4 章 source coding theorem 的典型集计数（$2^{NH}$ 与 $2^{N(H+\beta)}$ 的界），因为 jointly-typical 的证明就是把 source coding 的证明逐字搬过去（PDF p175 的 Theorem 证明开头明说「let the pair $x, y$ play the role of $x$」）。平行落点（跨学科）：6.042J 里 union bound 与「期望线性性不需独立性」；6.041 里 birthday paradox 作为「期望比概率更好算」的标准例子；CSAPP 里 hash table 的 load factor 与碰撞期望 $\lambda^2/2$ 同构——把 $A$ 换成 bucket 数、$S$ 换成 key 数，碰撞期望的公式一模一样。实现落点：真实的 random linear code（LDPC、Polar）无法真的「随机抽」，但在构造时用伪随机置换矩阵逼近随机性；`ITILA` 官方仓库（github.com/limix/... 之外，作者主页 inference.phy.cam.ac.uk/mackay/itila/ 提供源码包）里 `randcode.m`、`make_random_code.m` 就是 MacKay 自己用来做 exercise 9.20-9.22 数值验证的脚本。前沿落点：随机编码的「平均好」不给出高效 decoder，这是 coding theory 六十年的主轴问题；Polar code（Arıkan 2008，arXiv:0807.3917）是第一个**构造性**达到 capacity 且 $O(N\log N)$ 可译的码族，2016 年被 5G eMBB 控制信道采纳——你可以把它读成「MacKay 证明里那个『存在』终于被换成『显式构造』」。

我不打算在这里替原文圆场：上面 9.57 式的 $\exp(-S(S-1)/2A)$ 只在小 $S$ 时成立（要求 $S \ll \sqrt{A}$ 才好用），而 exercise 9.20 问的 $S = 24$、$A = 365$ 恰好落在 $\sqrt{A} \approx 19.1$ 附近，此时近似值 $\exp(-276/365) \approx 0.47$ 与精确值 0.4611 差约 2%，勉强能用但不能当精确答案报。这个近似边界原文没提醒。</span>


<span style="color:#7f8c8d">书内 p161 ｜ About Chapter 10（第 10 章导读页）</span>

#### About Chapter 10（关于第 10 章）

在读第 10 章之前，你应当已经读过第 4 章与第 9 章。exercise 9.14（p.153）特别推荐先做。

#### Cast of characters（角色表）

| 记号 | 含义 |
|---|---|
| $Q$ | the noisy channel（含噪信道） |
| $C$ | channel 的 capacity |
| $X^N$ | 用来生成 random code（随机码）的那个 ensemble |
| $\mathcal{C}$ | 一个 random code |
| $N$ | codeword 的长度 |
| $x^{(s)}$ | 一个 codeword，码中的第 $s$ 个 |
| $s$ | 被选中的那个 codeword 的编号（助记：the source selects $s$，信源选 $s$） |
| $S = 2^K$ | 码中 codeword 的总数 |
| $K = \log_2 S$ | 从 $S$ 个 codeword 中选一个所传递的 bit 数（假定等概率选取） |
| $\mathbf{s}$ | 编号 $s$ 的二进制表示 |
| $R = K/N$ | 码的 rate，单位是 bits per channel use（有时写作 $R'$） |
| $\hat{s}$ | decoder 对 $s$ 的猜测 |


<span style="color:#7f8c8d">书内 p162 ｜ 第 10 章章首页 ／ 10.1 The theorem</span>

## 10 The Noisy-Channel Coding Theorem（第 10 章 含噪信道编码定理）

### 10.1 The theorem（定理本身）

这个定理有三部分，两部分是正面的、一部分是否面的。主要的正面结果就是第一条。

[Figure 10.1：$R$–$p_b$ 平面上待证明可达到（1、2）与不可达到（3）的区域示意：横轴 $R$ 到 $C$ 为止，纵轴 $p_b$ 从 0 起；区域 1 是 $R < C$ 且 $p_b$ 任意小的那块，区域 2 是由 $R = C/(1 - H_2(p_b))$ 曲线所围的、$p_b > 0$ 时向右扩展的那块，区域 3 是曲线右侧的不可达区。]

**1.** 对每个 discrete memoryless channel，channel capacity

```math
C = \max_{P_X} I(X; Y) \qquad (10.1)
```

具有如下性质：对任意 $\epsilon > 0$ 与任意 $R < C$，当 $N$ 足够大时，存在一个长度为 $N$、rate $\ge R$ 的码以及一个 decoding algorithm，使得 maximal probability of block error $< \epsilon$。

**2.** 如果可以接受某个 bit error probability $p_b$，那么最高到 $R(p_b)$ 的 rate 都是 achievable（可达）的，其中

```math
R(p_b) = \frac{C}{1 - H_2(p_b)}. \qquad (10.2)
```

**3.** 对任何 $p_b$，大于 $R(p_b)$ 的 rate 都不可达。

### 10.2 Jointly-typical sequences（联合典型序列）

我们把上一章的直觉预览形式化。

我们将把 codeword $x^{(s)}$ 定义为取自 ensemble $X^N$，并考虑随机选取一个 codeword 以及相应的 channel 输出 $y$，由此定义一个联合 ensemble $(XY)^N$。我们将使用 typical-set decoder（典型集解码器），它把收到的 signal $y$ 解码为 $s$，当且仅当 $x^{(s)}$ 与 $y$ 是 jointly typical（联合典型）的——这个词随后马上定义。

证明的核心于是落在确定两个概率上：(a) 真实输入 codeword 与输出序列不是 jointly typical 的概率；(b) 某个错误输入 codeword 与输出是 jointly typical 的概率。我们将证明：当 $N$ 大时，只要 codeword 数少于 $2^{NC}$ 且 ensemble $X$ 是 optimal input distribution，这两个概率都趋于零。

#### Joint typicality（联合典型性）

长度均为 $N$ 的一对序列 $x, y$ 称为（在容差 $\beta$ 下）关于分布 $P(x, y)$ jointly typical，如果

$x$ 对 $P(x)$ 是 typical 的，即

```math
\left| \frac{1}{N} \log \frac{1}{P(x)} - H(X) \right| < \beta,
```

$y$ 对 $P(y)$ 是 typical 的，即

```math
\left| \frac{1}{N} \log \frac{1}{P(y)} - H(Y) \right| < \beta,
```

并且 $x, y$ 对 $P(x, y)$ 是 typical 的，即

```math
\left| \frac{1}{N} \log \frac{1}{P(x, y)} - H(X, Y) \right| < \beta.
```


<span style="color:#7f8c8d">书内 p163 ｜ 10.2: Jointly-typical sequences</span>

jointly-typical set（联合典型集）$J_{N\beta}$ 就是所有长度为 $N$ 的 jointly typical 序列对的集合。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example（例）</span>

下面是长度为 $N = 100$ 的一对 jointly typical 序列，所用 ensemble $P(x, y)$ 中 $P(x)$ 取 $(p_0, p_1) = (0.9, 0.1)$，而 $P(y \mid x)$ 对应一个噪声水平为 0.2 的 binary symmetric channel。

```
x  1111111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
y  0011111111000000000000000000000000000000000000000000000000000000000000000000000000111111111111111111
```

注意 $x$ 有 10 个 1，因而对概率 $P(x)$ 是 typical 的（在任何容差 $\beta$ 下都是）；$y$ 有 26 个 1，因而对 $P(y)$ 是 typical 的（因为 $P(y = 1) = 0.26$）；而 $x$ 与 $y$ 在 20 个 bit 上不同，这正是该 channel 下翻转 bit 数的典型值。

#### <span style="color:#c0392b">Joint typicality theorem（联合典型性定理）</span>

设 $x, y$ 取自 ensemble $(XY)^N$，该 ensemble 由

```math
P(x, y) = \prod_{n=1}^{N} P(x_n, y_n)
```

给出。那么

1. $x, y$ 是（在容差 $\beta$ 下）jointly typical 的概率当 $N \to \infty$ 时趋于 1；
2. jointly typical 序列的个数 $|J_{N\beta}|$ 接近 $2^{N H(X, Y)}$。精确地说，

```math
|J_{N\beta}| \le 2^{N(H(X,Y) + \beta)}; \qquad (10.3)
```

3. 若 $x' \sim X^N$ 与 $y' \sim Y^N$，即 $x'$ 与 $y'$ 是独立抽取的、且其 marginal distribution 与 $P(x, y)$ 的相同，那么 $(x', y')$ 落入 jointly-typical set 的概率约为 $2^{-N I(X; Y)}$。精确地说，

```math
P\big((x', y') \in J_{N\beta}\big) \le 2^{-N(I(X;Y) - 3\beta)}. \qquad (10.4)
```

**Proof（证明）.** 第 1、2 部分由 law of large numbers（大数律）给出，其证明照搬第 4 章 source coding theorem 的证明。对第 2 部分，让序列对 $x, y$ 扮演 source coding theorem 里 $x$ 的角色，把那里的 $P(x)$ 换成概率分布 $P(x, y)$ 即可。

对第三部分，

```math
P\big((x', y') \in J_{N\beta}\big) = \sum_{(x,y) \in J_{N\beta}} P(x) P(y) \qquad (10.5)
```

```math
\le |J_{N\beta}| \, 2^{-N(H(X) - \beta)} \, 2^{-N(H(Y) - \beta)} \qquad (10.6)
```

```math
\le 2^{N(H(X,Y) + \beta) - N(H(X) + H(Y) - 2\beta)} \qquad (10.7)
```

```math
= 2^{-N(I(X;Y) - 3\beta)}. \qquad \square \qquad (10.8)
```

jointly-typical set 的卡通式示意图见图 10.2。两个独立的 typical 向量是 jointly typical 的概率为

```math
P\big((x', y') \in J_{N\beta}\big) \simeq 2^{-N I(X; Y)} \qquad (10.9)
```

因为相互独立的 typical 序列对的总数是虚线矩形的面积 $2^{N H(X)} 2^{N H(Y)}$，而 jointly-typical 对的个数大致是 $2^{N H(X, Y)}$，于是命中一个 jointly-typical 对的概率大致是

```math
2^{N H(X,Y)} / 2^{N H(X) + N H(Y)} = 2^{-N I(X; Y)}. \qquad (10.10)
```


<span style="color:#7f8c8d">书内 p164 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

[Figure 10.2：jointly-typical set 的示意图。横方向表示 $\mathcal{A}_X^N$，即长度为 $N$ 的所有输入串的集合；纵方向表示 $\mathcal{A}_Y^N$，即长度为 $N$ 的所有输出串的集合。外框包含所有想得到的输入–输出对。每一个点代表一对 jointly typical 序列 $(x, y)$。jointly-typical 序列的总数约为 $2^{N H(X, Y)}$。框上标注了各条边的典型集大小：横轴方向 $2^{N H(X)}$、纵轴方向 $2^{N H(Y)}$，以及给定 $y$ 时 $x$ 的条件典型集 $2^{N H(X \mid Y)}$ 与给定 $x$ 时 $y$ 的条件典型集 $2^{N H(Y \mid X)}$；点云只占据「细长对角带」这一小块。]

### 10.3 Proof of the noisy-channel coding theorem（含噪信道编码定理的证明）

#### Analogy（一个比方）

想象我们想证明：在一百个婴儿组成的班里，存在一个体重不到 10 kg 的婴儿。单个婴儿既难抓又难称。Shannon 解决这个任务的办法是把所有婴儿一把抱起来，一起放到一台大秤上称。[Figure 10.3：Shannon 用来证明「有一个婴儿体重不到 10 kg」的办法——把整班婴儿一次性放上大秤。] 如果我们发现他们的平均体重小于 10 kg，那么必然至少存在一个体重小于 10 kg 的婴儿——实际上必然有很多个！Shannon 的办法不能保证揭示出一个体重不足的孩子，因为它依赖于班里只有极少数大象。但如果我们用他的办法，得出总重小于 1000 kg，那么任务就解决了。

#### From skinny children to fantastic codes（从瘦孩子到奇妙的好码）

我们想证明：存在一个码与一个 decoder，其 error probability 很小。要评估任何特定编码–解码系统的 error probability 并不容易。Shannon 的创新之处在于：他并不去构造一个好的编码–解码系统再评估它的 error probability，而是计算**所有码的**平均 block error probability，并证明这个平均值很小。既然平均很小，就必然存在个别码，其 block error probability 很小。

#### Random coding and typical-set decoding（随机编码与典型集解码）

考虑下面这个编码–解码系统，其 rate 是 $R'$。

**1.** 我们固定 $P(x)$，并按照

```math
P(x) = \prod_{n=1}^{N} P(x_n) \qquad (10.11)
```

随机生成 $(N, N R') = (N, K)$ 码 $\mathcal{C}$ 的 $S = 2^{N R'}$ 个 codeword。一个 random code 的示意画在图 10.4a 中。


<span style="color:#7f8c8d">书内 p165 ｜ 10.3: Proof of the noisy-channel coding theorem</span>

[Figure 10.4：(a) 一个 random code：在 $\mathcal{A}_X^N$ 空间里随机撒下若干个 codeword $x^{(1)}, x^{(2)}, x^{(3)}, x^{(4)}, \ldots$，各自的典型输出圆散布在 $\mathcal{A}_Y^N$ 中，有些圆互不重叠、有些重叠。(b) typical set decoder 的几个解码例子：与任何 codeword 都不 jointly typical 的序列 $y_a$ 被解码为 $\hat{s} = 0$；只与 codeword $x^{(3)}$ jointly typical 的 $y_b$ 被解码为 $\hat{s} = 3$；同理 $y_c$ 被解码为 $\hat{s} = 4$；与多于一个 codeword jointly typical 的 $y_d$ 被解码为 $\hat{s} = 0$。]

**2.** 这个码为发送方与接收方双方所知。

**3.** 从 $\{1, 2, \ldots, 2^{N R'}\}$ 中选出一条 message $s$，并发送 $x^{(s)}$。收到的 signal 是 $y$，满足

```math
P(y \mid x^{(s)}) = \prod_{n=1}^{N} P\big(y_n \mid x_n^{(s)}\big). \qquad (10.12)
```

**4.** 收到的 signal 由 typical-set decoding 解码。

**Typical-set decoding（典型集解码）.** 若 $(x^{(\hat{s})}, y)$ 是 jointly typical 且不存在另外的 $s'$ 使 $(x^{(s')}, y)$ 也是 jointly typical，则把 $y$ 解码为 $\hat{s}$；否则宣布失败（$\hat{s} = 0$）。

这不是 optimal decoding algorithm，但它足够好，而且更容易分析。typical-set decoder 示意见图 10.4b。

**5.** 若 $\hat{s} \ne s$，就发生了 decoding error。

有三种我们可以区分的 error probability。第一种是特定码 $\mathcal{C}$ 的 block error probability，即

```math
p_B(\mathcal{C}) \equiv P(\hat{s} \ne s \mid \mathcal{C}). \qquad (10.13)
```

这个量对任何给定的码都很难评估。

第二种是把这个 block error probability 对所有码取平均，

```math
\langle p_B \rangle \equiv \sum_{\mathcal{C}} P(\hat{s} \ne s \mid \mathcal{C}) P(\mathcal{C}). \qquad (10.14)
```


<span style="color:#7f8c8d">书内 p166 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

幸运的是，这个量比第一个量 $P(\hat{s} \ne s \mid \mathcal{C})$ 好算得多。$\langle p_B \rangle$ 恰好就是「上一页那个五步流程在第 5 步发生 decoding error」的概率。

第三种是码 $\mathcal{C}$ 的 maximal block error probability，

```math
p_{BM}(\mathcal{C}) \equiv \max_{s} P(\hat{s} \ne s \mid s, \mathcal{C}), \qquad (10.15)
```

这是我们最关心的量：我们希望证明存在一个具有所需 rate 的码 $\mathcal{C}$，其 maximal block error probability 很小。

我们先求平均 block error probability $\langle p_B \rangle$ 来抵达这个结果。一旦证明它可以被压到任意给定的小的数以下，我们就立刻推出：必然至少存在一个码 $\mathcal{C}$，其 block error probability 也小于这个小的数。最后，我们再说明：这个 block error probability 令人满意地小、但 maximal block error probability 未知（而且可以想象会非常大）的码，可以被改造为一个 rate 略小、而其 maximal block error probability 也保证很小的码。我们改造的办法是把它最差的 50% codeword 扔掉。

因此我们现在开始求平均的 block error probability。

#### Probability of error of typical-set decoder（typical-set decoder 的错误概率）

<span style="color:#1e8449;">**[译注]**</span> **typical-set decoder 的错误概率只能靠"三个互斥事件 + union bound"来压——少任何一件，存在性证明就断**

（分工声明：§9.8 页边那条注讲的是 random coding 这个**思想**为何出现、生日问题如何做它的玩具模型；这里只看 §10.3 里**具体的错误事件怎样被拆开与压下去**，两者互补。）

把错误事件拆成：① $(x^{(1)},y)$ 本身不 jointly typical（由 joint typicality theorem 第一部分，概率 $\to0$）；② 存在某个 $s'\ne1$ 使 $(x^{(s')},y)$ 也 jointly typical。第二件用 union bound：$\Pr\le (2^{NR}-1)\cdot 2^{-N(I(X;Y)-\delta)}$，当 $R<I(X;Y)$ 时指数小。这里有两个承重假设：**码本独立随机采样**（否则各 $s'$ 的典型事件不独立，union bound 之后还要处理相关性），以及**典型性阈值 $\delta$ 足够小**（保证单个错误对概率是 $2^{-N(I-\delta)}$ 而非只有多项式小）。抽掉任一条，第二条界不成立，$P_e\to0$ 的结论无从谈起。

几何版本更好记：把 $y$ 的典型球体积与混淆球体积相除，得 $\le 2^{-N(I-R)}$——这就是 §10.3 与第 11 章 Gaussian 情形球体积论证的同一个算式（式 (11.32)），离散与连续只差一个球体积公式。

坐标：§10.3（原书 p.163–166，PDF p.175–178）；joint typicality theorem 在 §10.2（原书 p.159，PDF p.171）。

使用 typical-set decoding 时有两个错误来源。要么 (a) 输出 $y$ 与所发送的 codeword $x^{(s)}$ 不是 jointly typical，要么 (b) $\mathcal{C}$ 中存在某个别的 codeword 与 $y$ 是 jointly typical。

由码构造的对称性，对所有码取平均的 error probability 不依赖于被选中的 $s$ 值；不妨设 $s = 1$。

**(a)** 输入 $x^{(1)}$ 与输出 $y$ 不是 jointly typical 的概率，由 joint typicality theorem 第一部分（p.163）可知趋于零。我们给这个概率的上界起个名字，叫 $\delta$，它满足当 $N \to \infty$ 时 $\delta \to 0$；对任何想要的 $\delta$，我们都能找到一个 blocklength $N(\delta)$ 使得 $P\big((x^{(1)}, y) \notin J_{N\beta}\big) \le \delta$。

**(b)** 对给定的 $s' \ne 1$，$x^{(s')}$ 与 $y$ 是 jointly typical 的概率，由第三部分可知 $\le 2^{-N(I(X;Y) - 3\beta)}$。而需要考虑的对手 $s'$ 有 $(2^{N R'} - 1)$ 个。

于是平均 error probability $\langle p_B \rangle$ 满足：

```math
\langle p_B \rangle \le \delta + \sum_{s'=2}^{2^{N R'}} 2^{-N(I(X;Y) - 3\beta)} \qquad (10.16)
```

```math
\le \delta + 2^{-N(I(X;Y) - R' - 3\beta)}. \qquad (10.17)
```

不等式 (10.16) 用各种足以造成错误的事件 $s'$ 的概率 $P_{s'}$ 之和去界定总错误概率 $P_{\text{TOT}}$，

```math
P_{\text{TOT}} \le P_1 + P_2 + \cdots,
```

这称为 union bound（并集界）。仅当这些不同致错事件从不同时发生时，它才取等号。

只要

```math
R' < I(X; Y) - 3\beta, \qquad (10.18)
```

增大 $N$ 就能把平均 error probability (10.17) 压到 $< 2\delta$。

我们几乎到了。我们做三处修改：

**1.** 我们在证明中把 $P(x)$ 取为 channel 的 optimal input distribution。此时条件 $R' < I(X; Y) - 3\beta$ 变成 $R' < C - 3\beta$。


<span style="color:#7f8c8d">书内 p167 ｜ 10.4: Communication (with errors) above capacity</span>

[Figure 10.5：expurgation 如何起作用。(a) 在一个典型的 random code 中，有一小部分 codeword 卷入 collision（碰撞）——某些 codeword 对彼此足够近，以致其中任一被发送时的 error probability 都不小。(b) 我们从 random code 中把所有这类可混淆的 codeword 删掉，得到一个新码。所得码的 codeword 略少一些，因而 rate 略低，但其 maximal probability of error 大大降低。]

**2.** 由于对所有码取平均的 error probability $< 2\delta$，必然存在一个码，其平均 block error probability $p_B(\mathcal{C}) < 2\delta$。

**3.** 为了说明不仅平均的、连 maximal 的 error probability $p_{BM}$ 也能做小，我们改造这个码，扔掉最差的一半 codeword——也就是最容易产生错误的那些。留下来的那些，其 conditional probability of error 必定都小于 $4\delta$。我们用这些剩下的 codeword 定义一个新码。这个新码有 $2^{N R' - 1}$ 个 codeword，即我们把 rate 从 $R'$ 降到 $R' - 1/N$（当 $N$ 大时是微不足道的降低），并取得 $p_{BM} < 4\delta$。这个技巧称为 expurgation（剔除）(figure 10.5)。所得码未必是该 rate 与该长度下的最好码，但它仍足以证明 noisy-channel coding theorem，而这正是我们此处要做的。

总之，我们可以「构造」一个 rate 为 $R' - 1/N$ 的码（其中 $R' < C - 3\beta$），其 maximal probability of error $< 4\delta$。只要令 $R' = (R + C)/2$、$\delta = \epsilon/4$、$\beta < (C - R')/3$，并取 $N$ 足够大使其余条件成立，就得到所陈述的定理。定理的第一部分于是证毕。$\square$

### 10.4 Communication (with errors) above capacity（在 capacity 之上带错通信）

[Figure 10.6：定理第一部分所证明为 achievable 的那部分 $R$–$p_b$ 平面：$R < C$ 时 $p_b$ 可以压到任意小。原书附注：我们已经证明 maximal probability of block error $p_{BM}$ 可做得任意小，因此 bit error probability $p_b$ 也一样，因为 $p_b$ 必定小于 $p_{BM}$。]

我们已经对任何 discrete memoryless channel 证明了图 10.6 所示 $R$–$p_b$ 平面某一部分的可达性。我们已说明：可以把任何含噪 channel 变成一个本质无噪的二进制 channel，rate 最高到每轮 $C$ bits。现在我们把这个可达区域的右边界扩展到非零 error probability 的情形。[这称为 rate-distortion theory（率失真理论）。]

我们用一个新技巧来做这件事。既然我们知道能把含噪 channel 变成一个 rate 更小的完美 channel，那么就足以只考虑在无噪 channel 上带错通信的问题。如果允许出错，我们能在无噪 channel 上通信得多快？

考虑一个无噪二进制 channel，并假定我们强迫以高于其 capacity（1 bit）的 rate 通信。例如，若要求发送方以 $R = 2$ bits per cycle 尝试通信，那么他实际上必须扔掉一半的信息。如果目标是使 bit error probability 尽可能小，怎样才能做得最好？一个简单策略是只传源 bit 的 $1/R$ 那一部分，其余忽略。接收方对缺失的 $1 - 1/R$ 那部分随机猜测，


<span style="color:#7f8c8d">书内 p168 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

于是平均 bit error probability 是

```math
p_b = \frac{1}{2}(1 - 1/R). \qquad (10.19)
```

这个策略对应的曲线在图 10.7 中用虚线画出。

我们可以做得比这更好（就最小化 $p_b$ 而言），办法是把被破坏的风险均匀分摊到所有 bit 上。事实上，我们可以达到 $p_b = H_2^{-1}(1 - 1/R)$，即图 10.7 中的实线曲线。那么，这个最优值怎样才能达到呢？

[Figure 10.7：achievable 点 $(R, p_b)$ 上的一个简单界与 Shannon 的界。横轴 $R$ 从 0 到 2.5，纵轴 $p_b$ 从 0 到 0.3。实线标 Optimum，是 $p_b = H_2^{-1}(1 - 1/R)$；虚线标 Simple，是 $p_b = \tfrac{1}{2}(1 - 1/R)$，位于实线上方，说明简单策略更差。两条线在 $R = 1$ 处都降到 $p_b = 0$。]

我们重用一件刚刚开发出来的工具，即含噪 channel 的 $(N, K)$ 码，并把它倒过来用，让 decoder 去定义一个 lossy compressor（有损压缩器）。具体来说，我们取一个用于 binary symmetric channel 的优秀 $(N, K)$ 码。假定这样的码 rate 为 $R' = K/N$，并能纠正 transition probability 为 $q$ 的 binary symmetric channel 所引入的错误。渐近地，存在 rate 为 $R'$ 且满足 $R' \simeq 1 - H_2(q)$ 的码。回想：若把这样一个达到 capacity 的长度为 $N$ 的码接到一个 binary symmetric channel 上，那么 (a) 输出的概率分布接近均匀，因为输出的 entropy 等于源的 entropy（$N R'$）加上噪声的 entropy（$N H_2(q)$）；并且 (b) 在这种情形下，该码的 optimal decoder 通常会把收到的长度为 $N$ 的向量映射到一个与收到的向量差 $q N$ 个 bit 的发送向量。

我们拿想发送的 signal，把它切成长度为 $N$ 的 block（是的，是 $N$，不是 $K$）。把每个 block 送进 decoder，得到一个长度更短、为 $K$ bit 的 signal，我们把它通过无噪 channel 传出去。要解码这次传输，我们把这条 $K$ bit message 送进原码的 encoder。重构出来的 message 会有若干 bit 与原始 message 不同——典型地是 $q N$ 个。于是 bit error probability 会是 $p_b = q$。这个 lossy compressor 的 rate 是 $R = N/K = 1/R' = 1/(1 - H_2(p_b))$。

现在，把这个 lossy compressor 接到我们那个 capacity 为 $C$ 的无错通信器上，我们就证明了最高可达到由下式定义的曲线的通信：

```math
R = \frac{C}{1 - H_2(p_b)}. \qquad \square \qquad (10.20)
```

关于 rate-distortion theory 的进一步阅读，见 Gallager (1968), p. 451，或 McEliece (2002), p. 75。

### 10.5 The non-achievable region (part 3 of the theorem)（不可达区域：定理第三部分）

<span style="color:#1e8449;">**[译注]**</span> **converse 才是 capacity 之所以是"硬边界"的原因：$R>C$ 时 $P_e$ 有正下界，靠 Fano 不等式把错误率与熵桥起来**

Fano：$H(S\mid\hat S)\le 1+P_e\log(2^{NR}-1)\approx 1+P_eNR$。左边又被 capacity 侧压住（$H(S\mid\hat S)\ge H(S)-I\ge NR-NC$），两式联立得 $P_e\ge 1-\frac{C}{R}-\frac{1}{NR}$，故 $R>C$ 时 $P_e$ 不可能趋 0。抽掉这一步，capacity 只是一个"可达速率的上确界"，无法排除"也许有更聪明的码能越过它"——所有工程直觉（为什么不能靠加大功率无限提速、为什么调制阶数有上限）都失去硬依据。

顺带纠正一个常见误读：越过 capacity 不等于"完全不能通信"，而是**错误率随 $R$ 增大单调上升**（§10.4 的曲线给出"软着陆"：把过载部分丢给 lossy compression，等价于在 $R>C$ 时故意引入受控失真）。这与"超频一定烧坏"不同，更像"超频后每提升一档，误码率按指数付账"。

挂载：Thomson 实分析里 sup 的"达不到"与 max 的"达到"之别；6.006 的下界证明（下界不告诉你算法，但排除一切算法）。

坐标：§10.5（原书 p.167，PDF p.179），Fano 不等式与不可达区域的证明；§10.4 的过载曲线在原书 p.167 前一页（PDF p.178）。

源、encoder、含噪 channel 与 decoder 定义了一条 Markov chain（马尔可夫链）：

```math
s \to x \to y \to \hat{s}
```

```math
P(s, x, y, \hat{s}) = P(s) P(x \mid s) P(y \mid x) P(\hat{s} \mid y). \qquad (10.21)
```

data processing inequality（数据处理不等式，exercise 8.9, p.141）必定适用于这条链：$I(s; \hat{s}) \le I(x; y)$。此外，由 channel capacity 的定义，$I(x; y) \le N C$，故 $I(s; \hat{s}) \le N C$。

假定某系统达到 rate $R$ 与 bit error probability $p_b$；那么 mutual information $I(s; \hat{s})$ 满足 $\ge N R\big(1 - H_2(p_b)\big)$。但 $I(s; \hat{s}) > N C$ 不可达，因此 $R > \dfrac{C}{1 - H_2(p_b)}$ 不可达。$\square$

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.1 [3]</span>

Fill in the details in the preceding argument. If the bit errors between $\hat{s}$ and $s$ are independent then we have $I(s; \hat{s}) = N R(1 - H_2(p_b))$.

---

<span style="color:#7f8c8d">本文件覆盖 PDF p161-p180 = 书内 p149-p168。第 10 章的证明与 capacity 计算续于下一块（PDF p181 起）。</span>


<span style="color:#7f8c8d">书内 p169 ｜ 10.6: Computing capacity</span>

如果那些 bit error 之间存在复杂的相关性，会怎样？为什么不等式 $I(s; \hat{s}) \ge N R(1 - H_2(p_b))$ 仍然成立？

### 10.6 Computing capacity（如何计算 capacity）

<span style="color:#1e8449;">**[译注]**</span> **capacity 之所以"算得出来"，靠的是 $I(X;Y)$ 对输入分布 $p$ 是凹函数——这正好是你刚补过注的 Boyd 那台机器**

$I(X;Y)=H(Y)-H(Y\mid X)$：$H(Y)$ 是 $p$ 的凹函数（$-\sum$ 的凸式），而 $H(Y\mid X)=\sum_x p_x H(Y\mid X=x)$ 对 $p$ **线性**。凹减线性仍凹，于是
$$C=\max_{p}\ I(X;Y)\quad \text{s.t.}\quad \sum_x p_x=1,\ p_x\ge0$$
是一个凸优化问题（最大化凹函数、线性约束）。KKT 给出一阶条件 $\frac{\partial I}{\partial p_x}=\text{const}$（对所有 $p_x>0$），这正是 Blahut–Arimoto 迭代的不动点方程——每轮先算给定 $p$ 下的信道后验 $Q(x\mid y)$，再用它更新 $p$，单调上升收敛到 $C$。抽掉凹性，capacity 就只是一个"定义"而非可计算量，只能对极小的信道枚举；抽掉 KKT，你就看不出迭代为何单调。

挂载（真同构）：Boyd《凸优化》§5.5.3 的 KKT 条件与 §4.2.5 的等式约束消除，正是这里的工具；凹性提供的"局部最优=全局最优"（Boyd §3.1.3）保证了 BA 迭代不会停在次优不动点。这条连接的价值在于：**同一台 KKT 机器，在 Boyd 里解的是几何规划的锥约束，在这里解的是信道容量的分布优化**。

坐标：§10.6（原书 p.169–171，PDF p.181–183），Arimoto (1972) / Blahut (1972) 算法；凹性的论证在同一节，$I$ 的凹性也可由 §2.7 的 Jensen 直接得到。

我们已经证明：channel 的 capacity 就是可靠通信能够达到的最大 rate。那么怎样计算一个给定 discrete memoryless channel 的 capacity 呢？我们需要求出它的 optimal input distribution。一般地，我们可以借助 mutual information 对输入概率的导数，用计算机搜索来找出 optimal input distribution。

> <span style="color:#7f8c8d">原书页边注：§10.6–10.8 包含进阶材料。初读者建议直接跳到 §10.9（p.172）。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.2 [2]（▷ 标记）</span>

Find the derivative of $I(X; Y)$ with respect to the input probability $p_i$, $\partial I(X; Y)/\partial p_i$, for a channel with conditional probabilities $Q_{j \mid i}$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.3 [2]</span>

Show that $I(X; Y)$ is a concave ⌢ function of the input probability vector $\mathbf{p}$.

（译注：原书用「concave ⌢」表示 concave（凹）、用「convex ⌣」表示 convex（凸），这两个小笑脸/哭脸符号只是提醒你哪个是哪个。）

由于 $I(X; Y)$ 在输入分布 $\mathbf{p}$ 上是 concave 的，任何使 $I(X; Y)$ 取驻点（stationary）的概率分布 $\mathbf{p}$ 都必须是 $I(X; Y)$ 的全局最大点。于是很自然会想把 $I(X; Y)$ 的导数塞进一个求 $I(X; Y)$ 局部最大的例行程序里，即求一个输入分布 $P(x)$ 使得

```math
\frac{\partial I(X; Y)}{\partial p_i} = \lambda \quad \text{for all } i, \qquad (10.22)
```

其中 $\lambda$ 是与约束 $\sum_i p_i = 1$ 相联系的 Lagrange multiplier（拉格朗日乘子）。

然而这个做法可能找不到正确答案，因为 $I(X; Y)$ 的最大值可能由某个对某些输入取 $p_i = 0$ 的分布达到。一个简单的例子是 ternary confusion channel（三值混淆信道）。

**Ternary confusion channel.** $\mathcal{A}_X = \{0, ?, 1\}$，$\mathcal{A}_Y = \{0, 1\}$。

```math
\begin{aligned} P(y = 0 \mid x = 0) &= 1; & P(y = 1 \mid x = 0) &= 0; \\ P(y = 0 \mid x = ?) &= 1/2; & P(y = 1 \mid x = ?) &= 1/2; \\ P(y = 0 \mid x = 1) &= 0; & P(y = 1 \mid x = 1) &= 1. \end{aligned}
```

只要用到输入 $?$，输出就是随机的；其余输入是 reliable inputs（可靠输入）。最大信息率 1 bit 是通过完全不用输入 $?$ 达到的。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.4 [2, p.173]（▷ 标记）</span>

Sketch the mutual information for this channel as a function of the input distribution $\mathbf{p}$. Pick a convenient two-dimensional representation of $\mathbf{p}$.

因此，这个最优化程序必须考虑到：当我们在 $I(X; Y)$ 上往高处爬时，可能会撞上不等式约束 $p_i \ge 0$。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.5 [2, p.174]（▷ 标记）</span>

Describe the condition, similar to equation (10.22), that is satisfied at a point where $I(X; Y)$ is maximized, and describe a computer program for finding the capacity of a channel.


<span style="color:#7f8c8d">书内 p170 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

#### 有助于寻找 optimal input distribution 的几个结果

**1.** 所有输出都必须被用到。

**2.** $I(X; Y)$ 是 channel 参数的一个 convex ⌣ 函数。

**3.** optimal input distribution 可能有多个，但它们在输出端看起来完全一样。

> <span style="color:#7f8c8d">原书页边注提醒：术语「convex ⌣」表示 convex，「concave ⌢」表示 concave；那个小笑脸与小哭脸的符号只是用来提醒你 convex 与 concave 分别是什么意思。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.6 [2]（▷ 标记）</span>

Prove that no output $y$ is unused by an optimal input distribution, unless it is unreachable, that is, has $Q(y \mid x) = 0$ for all $x$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.7 [2]</span>

Prove that $I(X; Y)$ is a convex ⌣ function of $Q(y \mid x)$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.8 [2]</span>

Prove that all optimal input distributions of a channel have the same output probability distribution $P(y) = \sum_x P(x) Q(y \mid x)$.

这些结果，连同「$I(X; Y)$ 是输入概率向量 $\mathbf{p}$ 的 concave ⌢ 函数」这一事实，共同证明了我们在求 symmetric channel 的 capacity 时所使用的那个对称性论证是有效的。如果一个 channel 在一组对称操作下不变——例如互换输入符号、互换输出符号——那么，给定任何不对称（即在这些操作下不不变）的 optimal input distribution，我们都可以把这个 optimal input distribution 与「对原 optimal input distribution 施加对称操作所能得到的一切置换形式」平均起来，造出另一个输入分布。由对称性，这些被置换过的分布必定与原分布有相同的 $I(X; Y)$；于是由 $I$ 的 concavity，这个平均得到的新输入分布必有 $I(X; Y)$ 大于或等于原分布的值。

#### Symmetric channels（对称信道）

为了使用对称性论证，先给 symmetric channel 一个定义会很有帮助。我喜欢 Gallager (1968) 的定义。

<span style="color:#00838f">一个 discrete memoryless channel 是 symmetric channel（对称信道），如果它的输出集合可以被划分成若干子集，使得对每个子集而言，transition probability 矩阵具有这样的性质：每一行（若不止一行）都是其他任一行的 permutation（置换），每一列也都是其他任一列的 permutation。</span>

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 10.9（例 10.9）</span>

下面这个 channel

```math
\begin{aligned} P(y = 0 \mid x = 0) &= 0.7; & P(y = ? \mid x = 0) &= 0.2; & P(y = 1 \mid x = 0) &= 0.1; \\ P(y = 0 \mid x = 1) &= 0.1; & P(y = ? \mid x = 1) &= 0.2; & P(y = 1 \mid x = 1) &= 0.7. \end{aligned} \qquad (10.23)
```

是对称 channel，因为它的输出可以划分成 $(0, 1)$ 与 $?$ 两部分，于是该矩阵可以重写成：

```math
\begin{aligned} P(y = 0 \mid x = 0) &= 0.7; & P(y = 1 \mid x = 0) &= 0.1; \\ P(y = 0 \mid x = 1) &= 0.1; & P(y = 1 \mid x = 1) &= 0.7; \\ P(y = ? \mid x = 0) &= 0.2; & P(y = ? \mid x = 1) &= 0.2. \end{aligned} \qquad (10.24)
```


<span style="color:#7f8c8d">书内 p171 ｜ 10.7: Other coding theorems</span>

对称性之所以有用，是因为——我们将在后面某一章看到——在 symmetric channel 上，capacity 通信可以由 linear code（线性码）达到。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.10 [2]</span>

Prove that for a symmetric channel with any number of inputs, the uniform distribution over the inputs is an optimal input distribution.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.11 [2, p.174]（▷ 标记）</span>

Are there channels that are not symmetric whose optimal input distributions are uniform? Find one, or prove there are none.

### 10.7 Other coding theorems（其他编码定理）

我们这一章证明的 noisy-channel coding theorem 相当一般，适用于任何 discrete memoryless channel；但它也相当不具体。该定理只说明：用 blocklength $N$ 足够大的码，可以达到 error probability 为 $\epsilon$、rate 为 $R$ 的可靠通信。定理并没有说，要达到给定的 $R$ 与 $\epsilon$，$N$ 需要多大。

可以推测，$\epsilon$ 越小、$R$ 越接近 $C$，$N$ 就得越大。

#### <span style="color:#c0392b">Noisy-channel coding theorem -- version with explicit N-dependence（带显式 N 依赖的版本）</span>

<span style="color:#00838f">对一个 discrete memoryless channel、一个 blocklength $N$ 与一个 rate $R$，存在长度为 $N$ 的 block code，其平均 error probability 满足：</span>

```math
p_B \le \exp\left[-N E_r(R)\right] \qquad (10.25)
```

<span style="color:#00838f">其中 $E_r(R)$ 是该 channel 的 random-coding exponent（随机编码指数），对 $0 \le R < C$ 而言是 $R$ 的一个 convex ⌣、递减、正的函数。random-coding exponent 也称为 reliability function（可靠性函数）。[借助 expurgation 论证还可以说明：存在某些 block code，其 maximal probability of error $p_{BM}$ 也是 $N$ 的指数小量。]</span>

$E_r(R)$ 的定义见 Gallager (1968), p. 139。当 $R \to C$ 时 $E_r(R)$ 趋于零；这个函数的典型行为见图 10.8。

[Figure 10.8：一条典型的 random-coding exponent 曲线。横轴是 $R$（从 0 到 $C$），纵轴是 $E_r(R)$；曲线在 $R = 0$ 处取最大值，单调下降，在 $R = C$ 处降到零。]

对有意义的 channel 计算 random-coding exponent 是一件很有挑战性的工作，人们为此投入了大量精力。即便对 binary symmetric channel 这样的简单 channel，$E_r(R)$ 也没有简单的表达式。

#### 以 blocklength 为函数的 error probability 下界

上面陈述的定理断言：存在某些码，其 $p_B$ 小于 $\exp[-N E_r(R)]$。但 error probability 能有多小？它可能小得多吗？

<span style="color:#00838f">对 discrete memoryless channel 上任何长度为 $N$ 的码，假定所有源 message 等概率使用，则 error probability 满足</span>

```math
p_B \succeq \exp\left[-N E_{sp}(R)\right], \qquad (10.26)^\dagger
```


<span style="color:#7f8c8d">书内 p172 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

<span style="color:#00838f">其中函数 $E_{sp}(R)$ 是该 channel 的 sphere-packing exponent（球堆积指数），对 $0 \le R < C$ 而言是 $R$ 的一个 convex ⌣、递减、正的函数。</span>

关于该结果的精确陈述与更多参考文献，见 Gallager (1968), p. 157。

† 说明：式 (10.26) 中的关系符号在 PDF 文字层中缺失（只余 `p_B` 与 `exp[...]` 两段），按球堆积界（sphere-packing bound）的数学语义补为「$\succeq$」，即 $p_B$ 是「不小于某个指数小量」的关系；此处记号以语义推定，原书该符号是一表示「下界」的复合不等号。

### 10.8 Noisy-channel coding theorems and coding practice（编码定理与编码实践）

设想一位顾客想为某个含噪 channel 买一套纠错码与 decoder。上面描述的结果允许我们提供如下服务：如果他告诉我们他 channel 的性质、想要的 rate $R$ 与想要的 error probability $p_B$，那么我们先算出相关的函数 $C$、$E_r(R)$、$E_{sp}(R)$，然后就可以告诉他：存在一个用特定 blocklength $N$ 的解决方案；而且事实上几乎任何在该 blocklength 下随机选取的码都能完成这件事。

不幸的是，我们还没搞清楚怎样在实践中实现这些 encoder 与 decoder；对 $N$ 很大的 random code 实现 encoder 与 decoder 的代价会是 $N$ 的指数级。

更进一步，就实用而言，顾客不太可能确切知道自己面对的是什么 channel。于是 Berlekamp (1980) 建议：处理纠错的明智做法是设计出各种编码–解码系统，并把它们的性能画在一系列理想化 channel 上、作为 channel 噪声水平的函数。这些图表（其中一张画在 p.568）可以拿给顾客看，顾客就能在现有的各种系统之间挑选，而不必说明他真正以为自己的 channel 是什么样子。以这种态度对待实际问题，函数 $E_r(R)$ 与 $E_{sp}(R)$ 的重要性就下降了。

### 10.9 Further exercises（进一步习题）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.12 [2]</span>

A binary erasure channel with input $x$ and output $y$ has transition probability matrix:

```math
Q = \begin{pmatrix} 1-q & 0 \\ q & q \\ 0 & 1-q \end{pmatrix}
```

Find the mutual information $I(X; Y)$ between the input and output for general input distribution $\{p_0, p_1\}$, and show that the capacity of this channel is $C = 1 - q$ bits.

A Z channel has transition probability matrix:

```math
Q = \begin{pmatrix} 1 & q \\ 0 & 1-q \end{pmatrix}
```

Show that, using a $(2, 1)$ code, two uses of a Z channel can be made to emulate one use of an erasure channel, and state the erasure probability of that erasure channel. Hence show that the capacity of the Z channel, $C_Z$, satisfies $C_Z \ge \frac{1}{2}(1-q)$ bits. Explain why the result $C_Z \ge \frac{1}{2}(1-q)$ is an inequality rather than an equality.


<span style="color:#7f8c8d">书内 p173 ｜ 10.10: Solutions</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 10.13 [3, p.174]</span>

A transatlantic cable contains $N = 20$ indistinguishable electrical wires. You have the job of figuring out which wire is which, that is, to create a consistent labelling of the wires at each end. Your only tools are the ability to connect wires to each other in groups of two or more, and to test for connectedness with a continuity tester. What is the smallest number of transatlantic trips you need to make, and how do you do it? How would you solve the problem for larger $N$ such as $N = 1000$?

As an illustration, if $N$ were 3 then the task can be solved in two steps by labelling one wire at one end $a$, connecting the other two together, crossing the Atlantic, measuring which two wires are connected, labelling them $b$ and $c$ and the unconnected one $a$, then connecting $b$ to $a$ and returning across the Atlantic, whereupon on disconnecting $b$ from $c$, the identities of $b$ and $c$ can be deduced.

This problem can be solved by persistent search, but the reason it is posed in this chapter is that it can also be solved by a greedy approach based on maximizing the acquired information. Let the unknown permutation of wires be $x$. Having chosen a set of connections of wires $C$ at one end, you can then make measurements at the other end, and these measurements $y$ convey information about $x$. How much? And for what set of connections is the information that $y$ conveys about $x$ maximized?

### 10.10 Solutions（习题解答）

#### Solution to exercise 10.4（p.169）

若输入分布是 $\mathbf{p} = (p_0, p_?, p_1)$，

```math
\begin{aligned} P(y = 0 \mid x = 0) &= 1, & P(y = 1 \mid x = 0) &= 0, \\ P(y = 0 \mid x = ?) &= 1/2, & P(y = 1 \mid x = ?) &= 1/2, \\ P(y = 0 \mid x = 1) &= 0, & P(y = 1 \mid x = 1) &= 1, \end{aligned}
```

则 mutual information 是

```math
I(X; Y) = H(Y) - H(Y \mid X) = H_2(p_0 + p_?/2) - p_?. \qquad (10.27)
```

我们可以用两种办法为这个函数画出好的草图：仔细考察函数本身，或者考察几个特例。

为作图方便，我对 $\mathbf{p}$ 采用二维表示，取 $p_0$ 与 $p_1$ 为自变量，于是 $\mathbf{p} = (p_0, p_?, p_1) = (p_0,\ 1 - p_0 - p_1,\ p_1)$。

**By inspection（直接考察）.** 若取 $p^* \equiv p_0 + p_?/2$ 与 $p_?$ 作为两个自由度，mutual information 就变得非常简单：$I(X; Y) = H_2(p^*) - p_?$。再换回 $p_0 = p^* - p_?/2$ 与 $p_1 = 1 - p^* - p_?/2$，就得到下面左图所示的草图。这个函数像一条沿 $p_0$、$p_1$ 增大方向上升的隧道。要得到所需的 $I(X; Y)$ 图，我们必须把这条隧道落在可行概率 simplex（单纯形）之外的部分剥掉；办法是重画这个曲面，只显示 $p_0 > 0$ 且 $p_1 > 0$ 的部分。函数的完整图形见右图。

[Figure：左图是 $(p_0, p_1)$ 平面上 $I(X; Y) = H_2(p_0 + p_?/2) - p_?$ 的曲面草图，两个横轴范围都是 $-0.5$ 到 $1$，纵轴 $-1$ 到 $1$；右图是同一曲面限制在 $p_0, p_1 \in [0,1]$、$p_0 + p_1 \le 1$ 的可行 simplex 内的那一片，纵轴 0 到 1。]


<span style="color:#7f8c8d">书内 p174 ｜ 10 -- The Noisy-Channel Coding Theorem</span>

**Special cases（特例）.** 在特例 $p_? = 0$ 下，channel 是无噪二进制 channel，$I(X; Y) = H_2(p_0)$。

在特例 $p_0 = p_1$ 下，$H_2(p_0 + p_?/2)$ 这一项等于 1，故 $I(X; Y) = 1 - p_?$。

在特例 $p_0 = 0$ 下，channel 是 error probability 为 0.5 的 Z channel。画这个我们在上一章已经会了（图 9.3）。

[Figure 10.9：ternary confusion channel 的 mutual information 的骨架图。横轴 $p_0$（0 到 1）与 $p_1$（0 到 1），纵轴 $I$（0 到 1）；先在 $p_? = 0$ 的边界上画出 $I = H_2(p_0)$ 的拱形，再在 $p_0 = p_1$ 的对角线上画出 $I = 1 - p_?$ 的直线，两条边界把整个曲面「撑」起来。]

这些特例使我们能够构造出图 10.9 所示的骨架。

#### Solution to exercise 10.5（p.169）

$\mathbf{p}$ 使 $I(X; Y)$ 取最大的充要条件是

```math
\left. \begin{aligned} \frac{\partial I(X;Y)}{\partial p_i} &= \lambda \quad \text{and} \quad p_i > 0 \\ \frac{\partial I(X;Y)}{\partial p_i} &\le \lambda \quad \text{and} \quad p_i = 0 \end{aligned} \right\} \quad \text{for all } i, \qquad (10.28)
```

其中 $\lambda$ 是一个常数，它与 capacity 的关系为 $C = \lambda + \log_2 e$。

这个结果可以用于一个计算导数的计算机程序，让程序中各概率 $p_i$ 按相应导数之差的 proportion（比例）增量或减量。

这个结果对懒惰但善于猜测的人类 capacity 求解者也有用：猜出 optimal input distribution 之后，只需确认式 (10.28) 成立即可。

#### Solution to exercise 10.11（p.171）

我们当然预期存在「非对称、但 optimal input distribution 是均匀分布」的 channel，因为发明一个 channel 时我们有 $I(J - 1)$ 个自由度，而 optimal input distribution 只有 $(I - 1)$ 维；于是，在一个 symmetric channel 周围的 $I(J - 1)$ 维扰动空间中，我们预期存在一个维数为 $I(J - 1) - (I - 1) = I(J - 2) + 1$ 的扰动子空间，使 optimal input distribution 保持不变。

下面是一个显式的例子，有点像 Z channel。

```math
Q = \begin{pmatrix} 0.9585 & 0.0415 & 0.35 & 0.0 \\ 0.0415 & 0.9585 & 0.0 & 0.35 \\ 0 & 0 & 0.65 & 0 \\ 0 & 0 & 0 & 0.65 \end{pmatrix} \qquad (10.29)^\dagger
```

† 说明：上式行列由 PDF 文字层的坐标重建核对（4 行 × 4 列，每行 4 个元素，已逐格对齐）。注意其**列和**均为 1、**行和**分别为 1.35、1.35、0.65、0.65 —— 与本书 §9.6 中 $Q(y \mid x)$ 按行归一的约定不符。唯一与数值自洽的读法是把它按列读作 $Q(y \mid x)$（列 = 输入 $x$，行 = 输出 $y$），即一个 4 输入、4 输出的 channel。此处记号与全书其他矩阵不一致（疑为排版时的转置），读者按列归一理解即可。

#### Solution to exercise 10.13（p.173）

对任何 $N > 2$，这个标号问题只需两趟行程即可解决——跨大西洋各一趟。

用信息论方法处理这个问题的关键一步，是写下一个划分（partition，即把一部分 wire 连接成子集这一组合对象）的 information content。若 $N$ 根 wire 被归成 $g_1$ 个大小为 1 的子集、$g_2$ 个大小为 2 的子集、……，则这样的划分的个数是

```math
\Omega = \frac{N!}{\prod_r (r!)^{g_r}\, g_r!}, \qquad (10.30)
```

而这样一个划分的 information content 就是这个量的对数。在 greedy（贪心）策略中，我们选第一个划分，使这个 information content 最大。

我们可以玩的一个游戏是：把 $g_r$ 当作实数，在约束 $\sum_r g_r r = N$ 之下最大化这个 information content。给该约束引进一个 Lagrange multiplier $\lambda$，则导数为

```math
\frac{\partial}{\partial g_r}\left( \log \Omega + \lambda \sum_r g_r r \right) = -\log r! - \log g_r + \lambda r, \qquad (10.31)
```


<span style="color:#7f8c8d">书内 p175 ｜ 10.10: Solutions</span>

令其为零，就得到一个相当漂亮的表达式

```math
g_r = \frac{e^{\lambda r}}{r!}; \qquad (10.32)
```

最优的 $g_r$ 正比于一个 Poisson distribution（泊松分布）！把 $g_r$ 代回约束 $\sum_r g_r r = N$，即可解出 Lagrange multiplier，得到隐式方程

```math
N = \mu e^{\mu}, \qquad (10.33)
```

其中 $\mu \equiv e^{\lambda}$ 是 Lagrange multiplier 的一个方便的重新参数化。图 10.10a 给出 $\mu(N)$ 的图形；图 10.10b 给出 $\mu = 2.2$ 时推得的那组非整数赋值 $g_r$，以及与之相近的整数 $g_r = \{1, 2, 2, 1, 1\}$，后者启发我们把第一个划分取为 $(a)(bc)(de)(fgh)(ijk)(lmno)(pqrst)$。这个划分在另一端产生一个随机划分，其 information content 为 $\log \Omega = 40.4$ bits，远多于我们为了推断跨大西洋的 permutation 所需获取的总信息量 $\log 20! \simeq 61$ bits 的一半。[相比之下，若把所有 wire 两两相连，所产生的 information content 只有约 29 bits。] 第二个划分怎么选留给读者。适合采用 Shannon 式的做法：在另一端取一个随机划分，用同一组 $\{g_r\}$；你需要确保两个划分尽可能彼此不同。

[Figure 10.10：用 Lagrange multiplier 近似求解电缆标号问题。(a) 参数 $\mu$ 作为 $N$ 的函数；横轴 $N$ 从 1 到 1000（对数轴），纵轴 $\mu$ 从 0.5 到 5.5，其中 $\mu(20) = 2.2$ 被标出。(b) 函数 $g_r = \mu^r/r!$ 的非整数值用折线表示，横轴 $r$ 从 1 到 10、纵轴 $g$ 从 0 到 2.5；由这些非整数值所启发的整数 $g_r$ 用叉号标出，落在 $g_r = 1, 2, 2, 1, 1$ 五个整数格上。]

若 $N \ne 2, 5, 9$，则这个标号问题有一些特别容易实现的解，称为 Knowlton–Graham partition（Knowlton–Graham 划分）：把 $\{1, \ldots, N\}$ 用两种方式 $A$ 与 $B$ 划分成不相交集合，并满足条件——对每一对 $j, k$，至多有一个元素同时出现在某个基数为 $j$ 的 $A$ 集合与某个基数为 $k$ 的 $B$ 集合中（Graham, 1966; Graham and Knowlton, 1968）。


<span style="color:#7f8c8d">书内 p176 ｜ About Chapter 11（第 11 章导读页）</span>

#### About Chapter 11（关于第 11 章）

在读第 11 章之前，你应当已经读过第 9 章与第 10 章。你还需要熟悉 Gaussian distribution（高斯分布）。

**One-dimensional Gaussian distribution（一维高斯分布）.** 若随机变量 $y$ 是 Gaussian 的，均值 $\mu$、方差 $\sigma^2$，我们写作

```math
y \sim \text{Normal}(\mu, \sigma^2), \quad \text{or} \quad P(y) = \text{Normal}(y; \mu, \sigma^2), \qquad (11.1)
```

那么 $y$ 的分布是：

```math
P(y \mid \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-(y - \mu)^2 / 2\sigma^2\right]. \qquad (11.2)
```

[我对概率密度与概率都用同一个符号 $P$。]

逆方差 $\tau \equiv 1/\sigma^2$ 有时称为该 Gaussian distribution 的 precision（精度）。

**Multi-dimensional Gaussian distribution（多维高斯分布）.** 若 $\mathbf{y} = (y_1, y_2, \ldots, y_N)$ 服从多元 Gaussian 分布，则

```math
P(\mathbf{y} \mid \mathbf{x}, \mathsf{A}) = \frac{1}{Z(\mathsf{A})} \exp\left(-\frac{1}{2}(\mathbf{y} - \mathbf{x})^{\text{T}} \mathsf{A} (\mathbf{y} - \mathbf{x})\right), \qquad (11.3)
```

其中 $\mathbf{x}$ 是该分布的均值，$\mathsf{A}$ 是 variance–covariance matrix（方差–协方差矩阵）之逆，归一化常数为 $Z(\mathsf{A}) = (\det(\mathsf{A}/2\pi))^{-1/2}$。

这个分布具有这样的性质：$y_i$ 的方差 $\Sigma_{ii}$、以及 $y_i$ 与 $y_j$ 的协方差 $\Sigma_{ij}$ 由

```math
\Sigma_{ij} \equiv \mathbb{E}\left[(y_i - \bar{y}_i)(y_j - \bar{y}_j)\right] = \left[\mathsf{A}^{-1}\right]_{ij} \qquad (11.4)
```

给出，其中 $\mathsf{A}^{-1}$ 是矩阵 $\mathsf{A}$ 之逆。

单个分量 $y_i$ 的 marginal distribution $P(y_i)$ 是 Gaussian 的；任何分量子集的联合边缘分布是多元 Gaussian 的；而任何子集在给定另一子集取值下的条件密度，例如 $P(y_i \mid y_j)$，也是 Gaussian 的。


<span style="color:#7f8c8d">书内 p177 ｜ 第 11 章章首页 ／ 11.1 The Gaussian channel</span>

## 11 Error-Correcting Codes & Real Channels（第 11 章 纠错码与真实信道）

我们已经证明的 noisy-channel coding theorem 表明：对任何含噪 channel，都存在可靠 error-correcting code（纠错码）。本章处理两个问题。

第一，许多实际 channel 的输入与输出是实数而不是离散的。对这些 continuous channel（连续信道），Shannon 能告诉我们什么？数字信号又该怎样映射成模拟波形、以及反过来？

第二，实用的 error-correcting code 是怎样造出来的？相对于 Shannon 所证明的可能性，实践中达到了什么水平？

### 11.1 The Gaussian channel（高斯信道）

最流行的实输入、实输出 channel 模型是 Gaussian channel。

Gaussian channel 有实输入 $x$ 与实输出 $y$。给定 $x$ 时 $y$ 的条件分布是 Gaussian distribution：

```math
P(y \mid x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-(y - x)^2 / 2\sigma^2\right]. \qquad (11.5)
```

这个 channel 的输入与输出都是连续的，但在时间上是离散的。下面我们将看到，某些连续时间 channel 与离散时间 Gaussian channel 等价。

这个 channel 有时称为 additive white Gaussian noise (AWGN) channel（加性白高斯噪声信道）。

与离散 channel 一样，我们也将讨论在这个 channel 上能达到多大的无错信息通信率。

#### 从连续时间 channel 引出的动机

考虑一个输入与输出在时间上都连续的物理（比方说电气的）channel。我们送入 $x(t)$，出来的则是 $y(t) = x(t) + n(t)$。

我们的传输是有功率代价的。一段长度为 $T$ 的传输，其平均功率可被约束为：

```math
\int_0^T dt\, [x(t)]^2 / T \le P. \qquad (11.6)
```

收到的 signal 被假定与 $x(t)$ 相差一个 additive noise（加性噪声）$n(t)$（例如 Johnson noise，约翰逊噪声），我们把它建模为白 Gaussian 噪声。这个噪声的大小由 noise spectral density（噪声谱密度）$N_0$ 来量化。


<span style="color:#7f8c8d">书内 p178 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

这样的 channel 怎样才能用来传递信息？考虑把一个由 $N$ 个实数 $\{x_n\}_{n=1}^{N}$ 组成的集合，用一段时长 $T$ 的 signal 送出去，这段 signal 由 orthonormal basis functions（标准正交基函数）$\varphi_n(t)$ 的加权组合构成，

```math
x(t) = \sum_{n=1}^{N} x_n \varphi_n(t), \qquad (11.7)
```

其中 $\int_0^T dt\, \varphi_n(t)\varphi_m(t) = \delta_{nm}$。接收方于是可以算出这些标量：

```math
y_n \equiv \int_0^T dt\, \varphi_n(t) y(t) = x_n + \int_0^T dt\, \varphi_n(t) n(t) \qquad (11.8)
```

```math
\equiv x_n + n_n \qquad (11.9)
```

对 $n = 1 \ldots N$ 成立。若没有噪声，$y_n$ 就会等于 $x_n$。白 Gaussian 噪声 $n(t)$ 给估计值 $y_n$ 加上一个标量噪声 $n_n$。这个噪声是 Gaussian 的：

```math
n_n \sim \text{Normal}(0, N_0/2), \qquad (11.10)
```

其中 $N_0$ 是上面引入的 spectral density。于是，这样使用的连续 channel 等价于式 (11.5) 所定义的 Gaussian channel。功率约束 $\int_0^T dt\, [x(t)]^2 \le PT$ 定义了 signal 幅度 $x_n$ 上的一个约束，

```math
\sum_n x_n^2 \le PT \quad \Rightarrow \quad \overline{x_n^2} \le \frac{PT}{N}. \qquad (11.11)
```

[Figure 11.1：三个基函数 $\varphi_1(t)$、$\varphi_2(t)$、$\varphi_3(t)$，以及它们的一个加权组合 $x(t) = \sum_{n=1}^{N} x_n \varphi_n(t)$，其中 $x_1 = 0.4$、$x_2 = -0.2$、$x_3 = 0.1$。]

在回到 Gaussian channel 之前，我们把连续 channel 的 bandwidth（带宽，以 Hertz 计）定义为：

```math
W = \frac{N^{\max}}{2T}, \qquad (11.12)
```

其中 $N^{\max}$ 是在长度 $T$ 的区间内能够产生的 orthonormal functions 的最大个数。这个定义可以由「用最高频率为 $W$ 的标准正交余弦与正弦曲线构造一段时长 $T$ 的带限 signal」来理解。orthonormal functions 的个数是 $N^{\max} = 2WT$。这个定义还与 Nyquist sampling theorem（奈奎斯特采样定理）相关：若一段 signal 中出现的最高频率是 $W$，那么该 signal 可以由一串间隔为 Nyquist interval（奈奎斯特间隔）$\Delta t = 1/2W$ 秒的离散采样点上的取值完全确定。

于是，使用一个带宽为 $W$、noise spectral density 为 $N_0$、功率为 $P$ 的实连续 channel，等价于每秒 $N/T = 2W$ 次使用一个噪声水平为 $\sigma^2 = N_0/2$、并受 signal 功率约束 $\overline{x_n^2} \le P/2W$ 的 Gaussian channel。

#### $E_b/N_0$ 的定义

想象 Gaussian channel $y_n = x_n + n_n$ 与某个编码系统一起使用，以每个 channel use $R$ bits 的 rate 传输二进制源 bit。我们怎样比较两个通信率 $R$ 不同、所用功率 $\overline{x_n^2}$ 也不同的编码系统呢？传输的 rate $R$ 大是好事；用的功率小也是好事。

习惯上，我们用「每源 bit 的功率」$E_b = \overline{x_n^2}/R$ 与 noise spectral density $N_0$ 之比，来度量经过 rate 补偿的 signal-to-noise ratio：

```math
E_b/N_0 = \frac{\overline{x_n^2}}{2\sigma^2 R}. \qquad (11.13)
```

$E_b/N_0$ 是无量纲的，但通常用 decibel（分贝）为单位报告；所给的值是 $10\log_{10} E_b/N_0$。$E_b/N_0$ 是用来比较 Gaussian channel 上各种编码方案的措施之一。


<span style="color:#7f8c8d">书内 p179 ｜ 11.2: Inferring the input to a real channel</span>

### 11.2 Inferring the input to a real channel（推断实信道的输入）

#### 「脉冲的最优检测」

1944 年，Shannon 写了一份备忘录（Shannon, 1993），讨论的问题是：给定两个形状已知、分别用向量 $\mathbf{x}_0$ 与 $\mathbf{x}_1$ 表示的脉冲，其中有一个经过含噪 channel 传了过来，怎样最好地区分它们。这是一个 pattern recognition 问题。这里假定噪声是 Gaussian 的，概率密度为

```math
P(\mathbf{n}) = \left[\det\left(\frac{\mathsf{A}}{2\pi}\right)\right]^{1/2} \exp\left(-\frac{1}{2}\mathbf{n}^{\text{T}}\mathsf{A}\mathbf{n}\right), \qquad (11.14)
```

其中 $\mathsf{A}$ 是噪声的 variance–covariance matrix 之逆，是一个对称正定矩阵。（若 $\mathsf{A}$ 是单位矩阵的倍数 $\mathsf{I}/\sigma^2$，则噪声是「白」的；对更一般的 $\mathsf{A}$，噪声是「有色」的。）

[Figure 11.2：两个脉冲 $\mathbf{x}_0$ 与 $\mathbf{x}_1$，表示为 31 维向量（图中画出它们作为时间的函数），以及其中之一的一个含噪版本 $\mathbf{y}$。]

那么，在源 signal 为 $s$（取 0 或 1）的条件下收到向量 $\mathbf{y}$ 的概率是

```math
P(\mathbf{y} \mid s) = \left[\det\left(\frac{\mathsf{A}}{2\pi}\right)\right]^{1/2} \exp\left(-\frac{1}{2}(\mathbf{y} - \mathbf{x}_s)^{\text{T}}\mathsf{A}(\mathbf{y} - \mathbf{x}_s)\right). \qquad (11.15)
```

optimal detector（最优检测器）基于后验概率比：

```math
\frac{P(s = 1 \mid \mathbf{y})}{P(s = 0 \mid \mathbf{y})} = \frac{P(\mathbf{y} \mid s = 1)}{P(\mathbf{y} \mid s = 0)} \cdot \frac{P(s = 1)}{P(s = 0)} \qquad (11.16)
```

```math
= \exp\left(-\frac{1}{2}(\mathbf{y} - \mathbf{x}_1)^{\text{T}}\mathsf{A}(\mathbf{y} - \mathbf{x}_1) + \frac{1}{2}(\mathbf{y} - \mathbf{x}_0)^{\text{T}}\mathsf{A}(\mathbf{y} - \mathbf{x}_0) + \ln\frac{P(s = 1)}{P(s = 0)}\right) = \exp\left(\mathbf{y}^{\text{T}}\mathsf{A}(\mathbf{x}_1 - \mathbf{x}_0) + \theta\right), \qquad (11.17)
```

其中 $\theta$ 是一个与收到的向量 $\mathbf{y}$ 无关的常数，

```math
\theta = -\frac{1}{2}\mathbf{x}_1^{\text{T}}\mathsf{A}\mathbf{x}_1 + \frac{1}{2}\mathbf{x}_0^{\text{T}}\mathsf{A}\mathbf{x}_0 + \ln\frac{P(s = 1)}{P(s = 0)}. \qquad (11.18)
```

如果检测器必须作决定（即猜 $s = 1$ 或 $s = 0$），那么使 error probability 最小的决定就是猜最可能的那个假设。我们可以用一个判别函数（discriminant function）写出最优决定：

```math
a(\mathbf{y}) \equiv \mathbf{y}^{\text{T}}\mathsf{A}(\mathbf{x}_1 - \mathbf{x}_0) + \theta \qquad (11.19)
```

判据为

```math
\begin{aligned} a(\mathbf{y}) &> 0 \;\to\; \text{guess } s = 1 \\ a(\mathbf{y}) &< 0 \;\to\; \text{guess } s = 0 \\ a(\mathbf{y}) &= 0 \;\to\; \text{guess either.} \end{aligned} \qquad (11.20)
```

注意 $a(\mathbf{y})$ 是收到的向量的线性函数，

```math
a(\mathbf{y}) = \mathbf{w}^{\text{T}}\mathbf{y} + \theta, \qquad (11.21)
```

其中 $\mathbf{w} \equiv \mathsf{A}(\mathbf{x}_1 - \mathbf{x}_0)$。[Figure 11.3：用来区分 $\mathbf{x}_0$ 与 $\mathbf{x}_1$ 的权重向量 $\mathbf{w} \propto \mathbf{x}_1 - \mathbf{x}_0$。]

### 11.3 Capacity of Gaussian channel（Gaussian channel 的 capacity）

到此为止，我们只度量了离散变量的 joint、marginal 与 conditional entropy。为了定义连续变量所传递的信息，我们必须处理两件事——real line 的无限长度，以及实数的无限精度。


<span style="color:#7f8c8d">书内 p180 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

#### Infinite inputs（无限输入）

在一次 Gaussian channel 的使用中，我们能传递多少信息？如果允许我们把任意实数 $x$ 送进 Gaussian channel，我们就能通过取 $x = d_1 d_2 d_3 \ldots d_N 000 \ldots 000$ 来传递一长串 $N$ 个数字 $d_1 d_2 d_3 \ldots d_N$。仅仅一次传输所传递的无错信息量就可以通过增大 $N$ 而变得任意大，而通信也可以通过增大 $x$ 末尾 0 的个数而变得任意可靠。不过，大输入通常伴随某种功率代价，更不必说接收方可接受的 dynamic range（动态范围）上的实际限制。

因此习惯上对每个输入 $x$ 引进一个 cost function（代价函数）$v(x)$，并把码约束为平均代价 $\bar{v}$ 小于或等于某个最大值。含输入代价函数的 generalized channel coding theorem（广义信道编码定理）是可以证明的——见 McEliece (1977)。结果是得到一个作为所允许代价之函数的 channel capacity $C(\bar{v})$。对 Gaussian channel 我们假定代价

```math
v(x) = x^2 \qquad (11.22)
```

使输入的「平均功率」$\overline{x^2}$ 受到约束。上面我们在实电气 channel 的情形下为这个代价函数给出了动机——物理功耗确实与 $x$ 呈二次关系。约束 $\overline{x^2} = \bar{v}$ 使得我们无法在一次 Gaussian channel 使用中传递无限多的信息。

#### Infinite precision（无限精度）

[Figure 11.4：(a) 一个概率密度 $P(x)$。问题是：我们能定义这个密度的「entropy」吗？(b) 我们可以对一串颗粒度（grain-size）$g$ 递减的概率分布计算 entropy，但这些 entropy 趋于 $\int P(x)\log\frac{1}{P(x)g}dx$，而它与 $g$ 有关：$g$ 每减半，entropy 就上涨一 bit。$\int P(x)\log\frac{1}{P(x)}dx$ 是一个不合法的积分。]

对实变量，人们很自然会想直接把求和换成积分来定义 joint、marginal 与 conditional entropy，但这个操作并不是良定义的。当我们把一个区间细分成越来越小的分段时，离散分布的 entropy 会发散（以颗粒度的对数发散，见图 11.4）。而且，对一个有量纲的量取对数也是不允许的，比如概率密度 $P(x)$（其量纲是 $[x]^{-1}$）。

不过，有一个 information measure 的极限是良态的，那就是 mutual information——而这正是真正要紧的那个量，因为它度量的是一个变量关于另一个变量传递了多少信息。在离散情形，

```math
I(X; Y) = \sum_{x,y} P(x, y) \log \frac{P(x, y)}{P(x)P(y)}. \qquad (11.23)
```

现在，由于 $\log$ 的自变量是同一个空间上两个概率之比，因此让 $P(x, y)$、$P(x)$、$P(y)$ 是概率密度并把求和换成积分是没问题的：

```math
I(X; Y) = \int dx\,dy\, P(x, y) \log \frac{P(x, y)}{P(x)P(y)} \qquad (11.24)
```

```math
= \int dx\,dy\, P(x) P(y \mid x) \log \frac{P(y \mid x)}{P(y)}. \qquad (11.25)
```

现在我们可以对 Gaussian channel 提出这些问题：(a) 在约束 $\overline{x^2} = v$ 下，什么概率分布 $P(x)$ 使 mutual information 最大？(b) 最大的 mutual information 是否仍然像离散 channel 那样，度量为这个实 channel 的最大无错通信率？


<span style="color:#7f8c8d">书内 p181 ｜ 11.3: Capacity of Gaussian channel</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.1 [3, p.189]</span>

Prove that the probability distribution $P(x)$ that maximizes the mutual information (subject to the constraint $\overline{x^2} = v$) is a Gaussian distribution of mean zero and variance $v$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.2 [2, p.189]（▷ 标记）</span>

Show that the mutual information $I(X; Y)$, in the case of this optimized distribution, is

```math
C = \frac{1}{2} \log\left(1 + \frac{v}{\sigma^2}\right). \qquad (11.26)
```

这是一个重要的结果。我们看到，Gaussian channel 的 capacity 是 signal-to-noise ratio $v/\sigma^2$ 的函数。

#### 在输入为 Gaussian 分布时作推断

若 $P(x) = \text{Normal}(x; 0, v)$ 且 $P(y \mid x) = \text{Normal}(y; x, \sigma^2)$，则 $y$ 的边缘分布是 $P(y) = \text{Normal}(y; 0, v + \sigma^2)$，而在输出为 $y$ 时输入的后验分布是：

```math
P(x \mid y) \propto P(y \mid x) P(x) \qquad (11.27)
```

```math
\propto \exp\left(-(y - x)^2/2\sigma^2\right)\exp\left(-x^2/2v\right) \qquad (11.28)
```

```math
= \text{Normal}\left(x;\ \frac{v}{v + \sigma^2}y,\ \left(\frac{1}{v} + \frac{1}{\sigma^2}\right)^{-1}\right). \qquad (11.29)
```

[从 (11.28) 到 (11.29) 的一步是靠对指数配方（completing the square）完成的。] 这个公式值得仔细研究。后验分布的均值 $\frac{v}{v + \sigma^2}y$ 可以看成两样东西的加权组合：最贴合输出的那个值 $x = y$，以及最贴合先验的那个值 $x = 0$：

```math
\frac{v}{v + \sigma^2}y = \frac{1/\sigma^2}{1/v + 1/\sigma^2}y + \frac{1/v}{1/v + 1/\sigma^2}\cdot 0. \qquad (11.30)
```

权重 $1/\sigma^2$ 与 $1/v$ 正是我们在 (11.28) 中相乘的那两个 Gaussian 的 precision：先验与 likelihood。后验分布的 precision 是这两个 precision 之和。这是一个普遍的性质：只要有两个独立的信息源通过 Gaussian 分布为某个未知变量提供信息，它们的 precision 就相加。[这是那条更著名的关系「独立变量相加时方差相加」的对偶。]

#### Gaussian channel 的 noisy-channel coding theorem

我们已经算出了一个最大的 mutual information。它是否对应着最大可能的无错信息传输速率？证明这一点的一种办法，是定义一串由 Gaussian channel 导出的离散 channel，输入与输出个数递增，并证明这些 channel 的最大 mutual information 趋于所断言的 $C$。离散 channel 的 noisy-channel coding theorem 适用于这每一个导出 channel，于是我们就得到了连续 channel 的一个 coding theorem。另外一种办法是，针对 Gaussian channel 给出一个直觉论证。


<span style="color:#7f8c8d">书内 p182 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

#### 含噪信道编码定理的几何图景：sphere packing（球堆积）

把一串输入 $x = (x_1, \ldots, x_N)$ 与相应的输出 $y$ 看成 $N$ 维空间中的两个点。当 $N$ 大时，噪声功率极可能（按比例）接近 $N\sigma^2$。因此输出 $y$ 极可能落在以 $x$ 为中心、半径 $\sqrt{N\sigma^2}$ 的球面附近。同样，若原始 signal $x$ 是在平均功率约束 $\overline{x^2} = v$ 之下随机生成的，则 $x$ 很可能落在以原点为中心、半径 $\sqrt{Nv}$ 的球附近；而由于 $y$ 的总平均功率是 $v + \sigma^2$，收到的 signal $y$ 很可能落在以原点为中心、半径 $\sqrt{N(v + \sigma^2)}$ 的球面上。

$N$ 维空间中半径为 $r$ 的球的体积是

```math
V(r, N) = \frac{\pi^{N/2}}{\Gamma(N/2 + 1)} r^N. \qquad (11.31)
```

现在考虑构造一个基于 non-confusable inputs 的通信系统，即各输入所对应的球彼此不发生显著重叠。non-confusable inputs 的最大个数 $S$ 由「可能的 $y$ 所在球的体积」除以「给定 $x$ 时 $y$ 所在球的体积」给出：

```math
S \le \left( \frac{\sqrt{N(v + \sigma^2)}}{\sqrt{N\sigma^2}} \right)^{N} \qquad (11.32)
```

于是 capacity 被界定为：

```math
C = \frac{1}{N}\log M \le \frac{1}{2}\log\left(1 + \frac{v}{\sigma^2}\right). \qquad (11.33)^\dagger
```

† 记号说明：式 (11.33) 里的 $M$ 就是本段上文的 $S$（non-confusable inputs 的最大个数）。原文在同一条推导里先后用 $S$ 与 $M$ 两个字母表示同一个量，属记号不一致；此处照录并标出。

用上一章那种更细致的论证可以确立等号成立。

#### 回到连续 channel

回想：使用一个带宽为 $W$、noise spectral density 为 $N_0$、功率为 $P$ 的实连续 channel，等价于每秒 $N/T = 2W$ 次使用一个 $\sigma^2 = N_0/2$、并受约束 $\overline{x_n^2} \le P/2W$ 的 Gaussian channel。把 Gaussian channel 的 capacity 结果代进去，我们得到连续 channel 的 capacity 为：

```math
C = W \log\left(1 + \frac{P}{N_0 W}\right) \quad \text{bits per second}. \qquad (11.34)
```

这个公式给出了关于实际通信中各种权衡的洞见。想象我们有一个固定的功率约束。要用这份功率，最好的带宽是多少？引进 $W_0 = P/N_0$，即 signal-to-noise ratio 为 1 的那个带宽，则图 11.5 画出 $C/W_0 = (W/W_0)\log(1 + W_0/W)$ 作为 $W/W_0$ 的函数。capacity 增长到渐近值 $W_0\log e$。就固定功率下的 capacity 而言，用大带宽在低 signal-to-noise ratio 下传输，远远优于用窄带宽在高 signal-to-noise ratio 下传输；这就是宽带通信方法（例如 3G 手机里用的「direct sequence spread-spectrum」（直接序列扩频）方案）的一个动机。当然，你并不是一个人在用频谱，你若占用大带宽，你的电磁邻居们可能不会高兴；所以出于社会原因，工程师们常常不得不将就于「高功率、窄带宽」的发射机。

[Figure 11.5：实 channel 的 capacity 与带宽的关系：$C/W_0 = (W/W_0)\log(1 + W_0/W)$ 作为 $W/W_0$ 的函数。横轴带宽（$W/W_0$）从 0 到 6，纵轴 capacity（$C/W_0$）从 0 到 1.4；曲线从 $(0, 1.44)$ 处起始、单调上升并趋于水平渐近线 $1$（以 $e$ 为底时是 $\log e \approx 1.4427$，图中渐近线标为 1）。]


<span style="color:#7f8c8d">书内 p183 ｜ 11.4: What are the capabilities of practical error-correcting codes?</span>

### 11.4 What are the capabilities of practical error-correcting codes?（实用纠错码能做到什么？）

几乎所有码都是好的，但几乎所有码在实现 encoder 与 decoder 时都需要查表，且表的规模是 blocklength $N$ 的指数级。而 coding theorem 恰恰要求 $N$ 很大。

所谓 practical error-correcting code（实用纠错码），我们指的是能在合理时间内完成编码与解码的码，例如所花时间随 blocklength $N$ 呈 polynomial（多项式）增长——最好是线性增长。

#### Shannon limit 在实践中并未达到

noisy-channel coding theorem 的非构造性证明表明：对任何含噪 channel 都存在好的 block code，而且事实上几乎所有 block code 都是好的。但要写出一个显式而实用的 encoder 与 decoder，使其和 Shannon 所承诺的一样好，仍是一个未解决的问题。

**Very good codes（极好的码）.** 对给定 channel，若一族 block code 在直到该 channel capacity 的任何通信率下都能取得任意小的 error probability，则称它们为该 channel 的「very good」码。

**Good codes（好的码）.** Good codes 是这样一些码族：在直到某个最大速率（可能小于给定 channel 的 capacity）的非零通信率下，都能取得任意小的 error probability。

**Bad codes（坏的码）.** Bad codes 是这样一些码族：它们不能取得任意小的 error probability，或者只能靠把 information rate 降到零才能取得任意小的 error probability。repetition code（重复码）就是 bad code family 的一个例子。（Bad codes 对实用目的未必无用。）

**Practical codes（实用的码）.** Practical codes 是这样一些码族：能在随 blocklength 呈多项式的时间和空间内完成编码与解码。

#### 大多数成熟码都是 linear codes

让我们复习 block code 的定义，然后补充 linear block code 的定义。

channel $Q$ 上的 $(N, K)$ block code 是一列 $S = 2^K$ 个 codeword $\{x(1), x(2), \ldots, x(2^K)\}$，每个长度都是 $N$：$x^{(s)} \in \mathcal{A}_X^N$。待编码的 signal $s$（取自大小为 $2^K$ 的 alphabet）被编码为 $x^{(s)}$。

<span style="color:#00838f">linear $(N, K)$ block code（线性分组码）是这样一种 block code：其 codeword $\{x^{(s)}\}$ 构成 $\mathcal{A}_X^N$ 的一个 $K$ 维子空间。编码操作可以用一个 $N \times K$ 的二进制矩阵 $G^{\text{T}}$ 表示：若待编码的 signal（用二进制记号）是 $\mathbf{s}$（一个长 $K$ bit 的向量），则编码后的 signal 是 $\mathbf{t} = G^{\text{T}}\mathbf{s} \bmod 2$。</span>

<span style="color:#00838f">codeword $\{\mathbf{t}\}$ 可以定义为满足 $H\mathbf{t} = 0 \bmod 2$ 的向量集合，其中 $H$ 是该码的 parity-check matrix（校验矩阵）。</span>

```math
G^{\text{T}} = \begin{pmatrix} 1 & \cdot & \cdot & \cdot \\ \cdot & 1 & \cdot & \cdot \\ \cdot & \cdot & 1 & \cdot \\ \cdot & \cdot & \cdot & 1 \\ 1 & 1 & 1 & \cdot \\ \cdot & 1 & 1 & 1 \\ 1 & \cdot & 1 & 1 \end{pmatrix}
```

例如 §1.2 的 $(7, 4)$ Hamming code 取 $K = 4$ 个 signal bit $\mathbf{s}$，把它们的原样发送出去，随后再发三个 parity-check bit。$N = 7$ 个被发送的符号由 $G^{\text{T}}\mathbf{s} \bmod 2$ 给出。

coding theory（编码理论）诞生于 Hamming 的工作：他发明了一族实用的 error-correcting code，每一个都能在一个长度为 $N$ 的 block 中纠正一个错误，其中 repetition code R3 与 $(7, 4)$ 码是最简单的两个。


<span style="color:#7f8c8d">书内 p184 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

自那以后，大多数成熟码都是 Hamming 码的推广：Bose–Chaudhury–Hocquenhem codes、Reed–Müller codes、Reed–Solomon codes、Goppa codes，如此等等。

#### Convolutional codes（卷积码）

另一族 linear code 是 convolutional code（卷积码），它不把源数据流分块，而是连续地读入并发送 bit。被发送的 bit 是过去源 bit 的线性函数。通常，产生发送 bit 的规则是把当前源 bit 送入一个长度为 $k$ 的 linear-feedback shift-register（线性反馈移位寄存器），并在每一轮发送该寄存器状态的一个或多个线性函数。由此得到的发送 bit 流，就是源数据流与一个 linear filter（线性滤波器）的卷积。这个滤波器的 impulse-response（冲激响应）可以是有限长或无限长的，取决于反馈移位寄存器的选择。

我们将在第 48 章讨论卷积码。

#### Linear codes 是「好的」吗？

人们可能会问：Shannon limit 在实践中达不到，是因为 linear code 天生不如 random code 好吗？答案是否定的——noisy-channel coding theorem 对 linear code 依然可证，至少对某些 channel 可以（见第 14 章），只不过这些证明和 Shannon 对 random code 的证明一样是非构造性的。

linear code 在编码端容易实现。解码 linear code 是否也容易呢？未必。一般的解码问题（在方程 $G^{\text{T}}\mathbf{s} + \mathbf{n} = \mathbf{r}$ 中求 maximum likelihood 的 $\mathbf{s}$）事实上是 NP-complete 的（Berlekamp et al., 1978）。[NP-complete 问题指的是这样一类计算问题：它们全都同样难，而且人们普遍相信一般情形下求解需要指数级计算机时间。] 所以注意力集中在那些存在快速 decoding algorithm 的码族上。

#### Concatenation（级联）

构造具有实用 decoder 的码的一个技巧是 concatenation（级联）的想法。

一个 encoder–channel–decoder 系统 $C \to Q \to D$ 可以看成定义了一个

```math
C' \to \underbrace{C \to Q \to D}_{Q'} \to D'
```

的 super-channel（超级信道）$Q'$，其 error probability 更小，但错误之间存在复杂的相关性。我们可以为这个 super-channel $Q'$ 造一个 encoder $C'$ 与 decoder $D'$。由外层码 $C'$ 与随后的内层码 $C$ 一起构成的码，称为 concatenated code（级联码）。

有些 concatenated code 利用了 interleaving（交织）的想法。我们把数据按 block 读入，每个 block 的尺寸大于各构成码 $C$ 与 $C'$ 的 blocklength。用码 $C'$ 把一个 block 的数据编码之后，在 block 内部把各 bit 重新排序，使得当这个 block 被送入第二个码 $C$ 时，原本相邻的 bit 彼此被分开。interleaver（交织器）的一个简单例子是 rectangular code（矩形码）或 product code（乘积码）：数据被排成一个 $K_2 \times K_1$ 的 block，先用一个 $(N_1, K_1)$ linear code 横向编码，再用一个 $(N_2, K_2)$ linear code 纵向编码。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.3 [3]（▷ 标记）</span>

Show that either of the two codes can be viewed as the inner code or the outer code.

作为一个例子，图 11.6 展示了一个 product code：我们先用 repetition code R3（也称为 Hamming code $H(3, 1)$）


<span style="color:#7f8c8d">书内 p185 ｜ 11.4: What are the capabilities of practical error-correcting codes?</span>

[Figure 11.6：一个 product code。(a) 一个串 `1011` 用由两个 Hamming 码（$H(3,1)$ 与 $H(7,4)$）构成的 concatenated code 编码后的矩阵。(b) 一个翻转 5 个 bit 的噪声图案（用 ⋆ 标出被翻转的位置）。(c) 收到的向量。(d) 用横向 $(3,1)$ decoder 解码之后的结果，(e) 随后再用纵向 $(7,4)$ decoder 之后的结果——解码出的向量与原始向量相符。(d′, e′) 若以相反顺序解码，则仍留下三个错误。]

横向编码、再用 $H(7, 4)$ 纵向编码。这个 concatenated code 的 blocklength 是 27。† 每个 codeword 中的源 bit 数是四个，由那个小矩形标出。

† 更正：原文此处写 blocklength $= 27$，与它自身的构造不符。按正文与图 11.6 的实际结构推：$K_1 = 1$（$H(3,1)$ 每次吃 1 个源 bit）、$K_2 = 4$，横向编码得 $4 \times 3 = 12$ 位，再对 3 列各做 $(7,4)$ 纵向编码，得 $3 \times 7 = 21$ 位；图 11.6(a)(c) 的方阵正是 7 行 × 3 列 = 21 格。故 blocklength 应为 **21**，不是 27。此处按数学语义纠正并标 †，不照抄原数。

我们可以用一种（虽非最优但）方便的方式解码：按某种顺序对各个子码分别使用它们各自的 decoder。最合理的做法是先解那个 rate 最低、因而纠错能力最强的码。

图 11.6(c–e) 展示了如下情形：我们收到图 11.6a 的 codeword，但带有一些错误（如图所示 5 个 bit 被翻转），先施加 $H(3, 1)$ 的 decoder，再施加 $H(7, 4)$ 的 decoder。第一个 decoder 纠正了其中三个错误，但在第二行那两个 bit error 处错误地改动了第三位。$(7, 4)$ decoder 随后能把这三个错误全部纠正。

图 11.6(d′–e′) 展示了以相反顺序解这两个码时的情形。在第一、二列各有两个错误，于是 $(7, 4)$ decoder 反而引入了两个额外的错误。它纠正了第三列的那一个错误。$(3, 1)$ decoder 随后清理掉四个错误，但错误地推断出第二位。

#### Interleaving（交织）

interleaving 的动机是：通过把一个码中原本相邻的 bit 分散开，我们就得以忽略内层码所产生的错误之间那些复杂的相关性。也许内层码会把整个 codeword 弄坏；但这个 codeword 是被一次一个 bit 地分散到外层码的若干个 codeword 上去的。于是我们就可以把内层码引入的错误当作独立的来处理。

#### Other channel models（其他信道模型）

除了 binary symmetric channel 与 Gaussian channel，编码理论家心里还装着更复杂的 channel。

**Burst-error channels（突发错误信道）** 是实践中重要的模型。Reed–Solomon codes 用元素个数很大的 Galois field（伽罗瓦域，见附录 C.1；例如 $2^{16}$ 个元素）作为它的输入 alphabet，从而自动获得一定程度的抗 burst-error 能力：即使连续 17 个 bit 被破坏，在 Galois field 表示下也只有 2 个连续符号被破坏。concatenation 与 interleaving 能进一步提供对 burst error 的保护。用在数字光盘上的级联 Reed–Solomon 码能够纠正长度达 4000 bit 的 burst。


<span style="color:#7f8c8d">书内 p186 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.4 [2, p.189]（▷ 标记）</span>

The technique of interleaving, which allows bursts of errors to be treated as independent, is widely used, but is theoretically a poor way to protect data against burst errors, in terms of the amount of redundancy required. Explain why interleaving is a poor method, using the following burst-error channel as an example. Time is divided into chunks of length $N = 100$ clock cycles; during each chunk, there is a burst with probability $b = 0.2$; during a burst, the channel is a binary symmetric channel with $f = 0.5$. If there is no burst, the channel is an error-free binary channel. Compute the capacity of this channel and compare it with the maximum communication rate that could conceivably be achieved if one used interleaving and treated the errors as independent.

**Fading channels（衰落信道）** 是除出现时间以外与 Gaussian channel 一样的实 channel：其接收功率被假定随时间变化。移动中的手机是一个重要例子。入射的无线电信号会被附近物体反射，从而形成干涉图案，手机收到的 signal 强度随其位置变化。当手机天线移动过与无线电信号波长相当的距离（几厘米）时，接收功率很容易变化 10 decibel（十倍）。

### 11.5 The state of the art（技术水平现状）

在 Gaussian channel 上通信，已知最好的码是哪些？所有实用码都是 linear code，并且要么基于 convolutional code，要么基于 block code。

#### Convolutional codes，以及基于它们的码

**Textbook convolutional codes（教科书式卷积码）.** 卫星通信的「事实标准」纠错码是一个 constraint length（约束长度）为 7 的 convolutional code。卷积码在第 48 章讨论。

**Concatenated convolutional codes（级联卷积码）.** 上述卷积码可以作为某个 concatenated code 的内层码，其外层码是一个使用八 bit 符号的 Reed–Solomon code。这个码曾用于深空通信系统，例如 Voyager 探测器。关于 Reed–Solomon code 的进一步阅读，见 Lin and Costello (1983)。

**The code for Galileo（Galileo 任务用的码）.** 一个格式相同、但卷积码的 constraint length 更长（15）、Reed–Solomon 码也更大的码由 Jet Propulsion Laboratory 开发（Swanson, 1988）。这个码的细节在 JPL 之外没有发表，解码只能用装满一屋子专用硬件的设备完成。1992 年，这是已知最好的 rate 1/4 的码。

**Turbo codes（Turbo 码）.** 1993 年，Berrou、Glavieux 与 Thitimajshima 报告了关于 turbo code 的工作。turbo code 的 encoder 基于两个卷积码的 encoder。源 bit 被分别送入两个 encoder，送入其中一路时源 bit 的次序被随机置换（permutation），然后把每个构成码产生的 parity bit 全部发送出去。解码算法则是迭代式地做：用每个构成码的标准 decoding algorithm 解它，然后把输出

[Figure 11.7：turbo code 的 encoder。每个方框 $C_1$、$C_2$ 内是一个 convolutional code。源 bit 在被送入 $C_2$ 之前用一个 permutation $\pi$ 重新排序。被发送的 codeword 由两个卷积码的输出 concatenation 或 interleave 而成。这个随机 permutation 在码的设计阶段选定，此后固定不变。]


<span style="color:#7f8c8d">书内 p187 ｜ 11.6: Summary</span>

作为另一个 decoder 的输入。这个解码算法是名为 sum–product algorithm（和积算法）的 message-passing algorithm（消息传递算法）的一个实例。

turbo code 在第 48 章讨论，message passing 在第 16、17、25、26 章讨论。

#### Block codes

**Gallager's low-density parity-check codes（Gallager 的低密度校验码）.** 已知在 Gaussian channel 上最好的 block code 是由 Gallager 在 1962 年发明的，但随即被编码理论界大多数人遗忘。它们在 1995 年被重新发现，并被证明具有出色的理论与实用性质。与 turbo code 一样，它们用 message-passing 算法解码。

[Figure 11.8：一个低密度 parity-check matrix 及其对应图（Tanner 图），属于一个 rate-1/4、blocklength $N = 16$、约束数 $M = 12$ 的低密度 parity-check code。每个白圈代表一个被发送的 bit。每个 bit 参与 $j = 3$ 个约束，约束用方框表示。每个约束强制它所连接的 $k = 4$ 个 bit 之和为偶数。这个码是一个 $(16, 4)$ 码。当 blocklength 增大到 $N \simeq 10\,000$ 时，可获得卓越的性能。]

我们将在第 47 章讨论这些漂亮而简单的码。

上述各种码在 Gaussian channel 上的性能比较见 p.568 的图 47.17。

### 11.6 Summary（本章小结）

random code 是好的，但它们需要指数级的资源来编码和解码。

非随机的码大多不如 random code 那样好。对一个非随机的码，编码也许容易，但即便是定义很简单的 linear code，解码问题依然非常困难。

最好的实用码 (a) 采用非常大的 block size；(b) 基于半随机的码构造；(c) 利用基于概率的解码算法。

### 11.7 Nonlinear codes（非线性码）

实际使用的大多数码是线性的，但并非全部。数字音轨是以二进制图案的形式编码到电影胶片上的。影响胶片的可能错误涉及灰尘与划痕，前者产生大量 1，后者产生大量 0。我们希望没有任何 codeword 看起来像全 1 或全 0，这样才容易检测出由灰尘与划痕引起的错误。数字影院音响系统所使用的一种码，是一个非线性的 $(8, 6)$ 码，由 $\binom{8}{4}$ 个权为 4 的二进制图案中的 64 个构成。

### 11.8 Errors other than noise（噪声之外的错误）

接收方不确定性的另一个来源，是关于所发送 signal $x(t)$ 的时序的不确定性。在通常的编码理论与信息论中，发送方的时间 $t$ 与接收方的时间 $u$ 被假定为完全同步。但如果接收方收到一个 signal $y(u)$，其中接收方的时间 $u$ 是发送方时间 $t$ 的一个不完美已知的函数 $u(t)$，那么这个 channel 用于通信的 capacity 就会降低。与我们到此为止讨论的同步 channel 相比，这类 channel 的理论是不完整的。甚至连带同步错误的 channel 的 capacity 都还不知道（Levenshtein, 1966; Ferreira et al., 1997）；在带同步错误的 channel 上可靠通信的码仍是一个活跃的研究领域（Davey and MacKay, 2001）。


<span style="color:#7f8c8d">书内 p188 ｜ 11 -- Error-Correcting Codes and Real Channels</span>

#### Further reading（进一步阅读）

关于 spread-spectrum 方法历史的综述，见 Scholtz (1982)。

### 11.9 Exercises（习题）

#### The Gaussian channel（Gaussian channel 相关）

##### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.5 [2, p.190]（▷ 标记）</span>

Consider a Gaussian channel with a real input $x$, and signal to noise ratio $v/\sigma^2$.

(a) What is its capacity $C$?

(b) If the input is constrained to be binary, $x \in \{\pm\sqrt{v}\}$, what is the capacity $C'$ of this constrained channel?

(c) If in addition the output of the channel is thresholded using the mapping

```math
y \to y' = \begin{cases} 1 & y > 0 \\ 0 & y \le 0, \end{cases} \qquad (11.35)
```

what is the capacity $C''$ of the resulting channel?

(d) Plot the three capacities above as a function of $v/\sigma^2$ from 0.1 to 2. [You'll need to do a numerical integral to evaluate $C'$.]

##### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.6 [3]（▷ 标记）</span>

For large integers $K$ and $N$, what fraction of all binary error-correcting codes of length $N$ and rate $R = K/N$ are linear codes? [The answer will depend on whether you choose to define the code to be an ordered list of $2^K$ codewords, that is, a mapping from $s \in \{1, 2, \ldots, 2^K\}$ to $x^{(s)}$, or to define the code to be an unordered list, so that two codes consisting of the same codewords are identical. Use the latter definition: a code is a set of codewords; how the encoder operates is not part of the definition of the code.]

#### Erasure channels（擦除信道相关）

##### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.7 [4]（▷ 标记）</span>

Design a code for the binary erasure channel, and a decoding algorithm, and evaluate their probability of error. [The design of good codes for erasure channels is an active research area (Spielman, 1996; Byers et al., 1998); see also Chapter 50.]

##### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.8 [5]（▷ 标记）</span>

Design a code for the $q$-ary erasure channel, whose input $x$ is drawn from $0, 1, 2, 3, \ldots, (q-1)$, and whose output $y$ is equal to $x$ with probability $(1-f)$ and equal to $?$ otherwise. [This erasure channel is a good model for packets transmitted over the internet, which are either received reliably or are lost.]

##### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 11.9 [3, p.190]</span>

How do redundant arrays of independent disks (RAID) work? These are information storage systems consisting of about ten disk drives, of which any two or three can be disabled and the others are able to still able to reconstruct any requested file. What codes are used, and how far are these systems from the Shannon limit for the problem they are solving? How would you design a better RAID system? Some information is provided in the solution section. See http://www.acnc.com/raid2.html; see also Chapter 50.

> <span style="color:#7f8c8d">原书页边注（关于 RAID 的缩写）：有些人说 RAID 代表「redundant array of inexpensive disks」（廉价磁盘冗余阵列），但我觉得这种说法很傻——即使磁盘很贵，RAID 依然是个好主意！</span>

[译注] <span style="color:#1e8449">**从「球堆积」到 5G：capacity 公式 $C = \frac{1}{2}\log(1 + v/\sigma^2)$ 的承重位置，以及为什么 $E_b/N_0 = -1.59$ dB 是工程界的宪法线。**

先看机制。§11.3 得到 $C = \frac{1}{2}\log_2(1 + v/\sigma^2)$ bits per channel use（PDF p193，式 11.26），§11.4 又把它翻译成带宽形式 $C = W\log_2(1 + P/N_0W)$（式 11.34）。抽掉这个结果，整个数字通信工程会崩在哪？会崩在**「给定功率和带宽，究竟能跑多快」这件事上失去硬上界**。具体地说，调制方式（QAM 星座有多大）、编码码率（rate 1/2 还是 8/9）、天线数量（MIMO 几层）、乃至频段拍卖的每 MHz 定价，都是拿这条曲线当标尺的：任何方案如果报告的点落在曲线之上，只可能是算错了或者测错了。这个公式不是「参考」，它是**测量坐标系本身**。

第二个更锋利的东西藏在 $E_b/N_0$ 里。由 $C = \frac{1}{2}\log_2(1 + v/\sigma^2)$ 与 $E_b/N_0 = v/(2\sigma^2 R)$（式 11.13）联立，在 $R \to C$（即信道被用到极限、误码率趋零）时解出 $E_b/N_0 \ge \frac{2^C - 1}{C}\cdot\frac{1}{2}$，令 $C \to 0$ 取极限得 $\lim = \ln 2 = 0.693$，换成分贝是 $10\log_{10}(0.693) = -1.59$ dB。这条 $-1.59$ dB 就是著名的 Shannon limit（香农极限）：**任何在 AWGN 信道上以任意低误码率传输的方案，其每信息 bit 的能量都不可能低于这个值**。它是一条真正的下界，不受编码技术进步的侵蚀——六十年来所有码的进展都只是在无限逼近它，而没有越过它。你可以这样检验这条线的现实重量：LTE/5G 的链路自适应算法里，MCS（modulation and coding scheme）表的每一行都对应一个「达到某个 $E_b/N_0$ 时需要多低的码率才不掉话」的阈值，而表格的下端就是逼近 $-1.59$ dB 的窄带极限；卫星链路的 link budget 计算同样是先把 $E_b/N_0$ 预算出来，再除以 $-1.59$ dB 得到「理论上还剩多少 dB 的编码增益可挖」。

再看可点开的落点。书本落点：§11.3（PDF p193，式 11.26 与 11.28-11.30 的 Gaussian 后验）与 §11.4 的几何证明（PDF p194，式 11.31-11.33 的球体积相除）；$E_b/N_0$ 的定义在 PDF p190（式 11.13，含页边注「$E_b/N_0$ 无量纲，但通常用 $10\log_{10}$ 的分贝报告」）；性能对比图在 p.568 的 Figure 47.17（各实用码相对 Shannon limit 的位置，是全书最实用的一张图）。上游落点：第 8 章 differential entropy（微分熵）——$C = \frac{1}{2}\log(1+v/\sigma^2)$ 本质是「Gaussian 在给定方差下微分熵最大」这一事实的推论（MacKay 用 Exercise 11.1 让你自己证），挂到 6.041 概率里的「Gaussian 是熵最大的连续分布」，以及 Strang 线代里的正定矩阵与二次型（式 11.14 的 $\mathsf{A}$ 是精度矩阵，$\det \mathsf{A}$ 出现在归一化常数里，这正是多元 Gaussian 的概率密度公式）。平行落点：球堆积论证（式 11.32）与 6.046J 里「高维球的体积几乎全集中在一层薄壳上」同构——把「球体积之比的 $N$ 次方开根」读成「每个维度上信噪比贡献一个因子」，就能看出为什么 capacity 与维数成线性、而不是指数。实现落点：`ITILA` 官方源码包里的 `gauss.m`、`capacity_of_gaussian_channel.m` 做数值验证；真实系统里 LDPC 码的 Tanner 图与 sum-product 解码在 MacKay 的 `ldpc` 源码包（作者主页提供，`decode.c` / `mod2dense.c`）里可读——那正是他 1995 年后推动 LDPC 复兴时写的代码。前沿落点：turbo code（Berrou, Glaviceux & Thitimajshima, 1993, ICC 会议论文）与 LDPC 的稀疏图构造；Polar code（Arıkan, 2008, arXiv:0807.3917）是第一个被证明**构造性**达到 capacity 且 $O(N\log N)$ 可译的码族，2016 年进入 5G eMBB 控制信道标准；在有限码长 $N$ 下的可达界（finite blocklength，Polyanskiy–Poor–Verdú 2010, arXiv:0712.0146）是目前 5G URLLC 场景真正在用的理论工具，因为 URLLC 要求 $N$ 只有几百、延迟 1 ms，渐近的 Shannon limit 根本不够紧。

最后不替原文圆场。原文 §11.4 说「几乎所有码都是好的，但几乎所有码实现需要 $N$ 的指数级查表」，紧接着 §11.5 又列出 LDPC 与 turbo 这些「好的且实用的」码——这不是矛盾，但 MacKay 没有把逻辑缝合点讲明：随机码「好」的证明用的是 average over codes，而实用解码器能工作靠的是**稀疏图上的局部 message passing 恰好收敛**，这两者之间没有一般性的定理搭桥（LDPC 的良好性能至今仍主要靠 density evolution 与实测，而非严格证明）。读者很容易误以为「LDPC 就是那个 random code 的实现」。这一点原文没有提醒，我把话挑明。</span>

---

<span style="color:#7f8c8d">本文件覆盖 PDF p181-p200 = 书内 p169-p188。第 11 章续于下一块（PDF p201 起，书内 p189 起，为 11.9 习题解答与第 12 章）。</span>


<span style="color:#7f8c8d">书内 p189 ｜ 11.10: Solutions</span>

## 11.10 Solutions（第 11.10 节 解答）

**Solution to exercise 11.1 (p.181)（练习 11.1 的解答）.**

对 power constraint（功率约束）引入一个 Lagrange multiplier（拉格朗日乘子）$\lambda$，对 $P(x)$ 的 normalization（归一化）约束引入另一个乘子 $\mu$。

```math
F = I(X;Y) - \lambda \int dx\, P(x) x^2 - \mu \int dx\, P(x) \qquad (11.36)
```

```math
= \int dx\, P(x) \left[ \int dy\, P(y \mid x) \ln \frac{P(y \mid x)}{P(y)} - \lambda x^2 - \mu \right]. \qquad (11.37)
```

对 $P(x^{*})$ 做 functional derivative（泛函导数）：

```math
\frac{\delta F}{\delta P(x^{*})} = \int dy\, P(y \mid x^{*}) \ln \frac{P(y \mid x^{*})}{P(y)} - \lambda x^{*2} - \mu - \int dx\, P(x) \int dy\, P(y \mid x) \frac{1}{P(y)} \frac{\delta P(y)}{\delta P(x^{*})}. \qquad (11.38)
```

最后一个因子 $\delta P(y)/\delta P(x^{*})$ 用 $P(y) = \int dx\, P(x) P(y \mid x)$ 求出，等于 $P(y \mid x^{*})$；于是末项整体「collapse in a puff of smoke」（化成一缕烟）变成 $1$，并被吸收进 $\mu$ 项。

代入 $P(y \mid x) = \exp\!\left(-(y-x)^2 / 2\sigma^2\right) / \sqrt{2\pi\sigma^2}$，并令导数为零：

```math
\int dy\, P(y \mid x) \ln \frac{P(y \mid x)}{P(y)} - \lambda x^2 - \mu' = 0 \qquad (11.39)
```

```math
\Rightarrow\ \int dy\, \frac{\exp\!\left(-(y-x)^2/2\sigma^2\right)}{\sqrt{2\pi\sigma^2}} \ln\left[ P(y)\sigma \right] = -\lambda x^2 - \mu' - \tfrac{1}{2}. \qquad (11.40)
```

这个条件必须对一切 $x$ 都被 $\ln[P(y)\sigma]$ 满足。把 $\ln[P(y)\sigma]$ 写成 Taylor expansion（泰勒展开）$a + by + cy^2 + \cdots$，则只有二次函数 $\ln[P(y)\sigma] = a + cy^2$ 能满足约束 (11.40)。（任何更高阶的项 $y^p$，$p \gt 2$，都会在右侧产生 $x^p$ 项，而右侧并不存在这些项。）因此 $P(y)$ 是 Gaussian（高斯分布）。我们只要用 Gaussian 的 input distribution（输入分布）$P(x)$，即可得到这个最优的 output distribution（输出分布）。

**Solution to exercise 11.2 (p.181)（练习 11.2 的解答）.**

给定方差为 $v$ 的 Gaussian input distribution，输出分布是 $\mathrm{Normal}(0, v + \sigma^2)$，因为 $x$ 与 noise（噪声）是独立随机变量，而独立随机变量的 variances（方差）相加。mutual information 为：

```math
I(X;Y) = \int dx\,dy\, P(x)P(y \mid x) \log P(y \mid x) - \int dy\, P(y) \log P(y) \qquad (11.41)
```

```math
= \tfrac{1}{2}\log \frac{1}{\sigma^2} - \tfrac{1}{2}\log \frac{1}{v + \sigma^2} \qquad (11.42)
```

```math
= \tfrac{1}{2}\log\left( 1 + \frac{v}{\sigma^2} \right). \qquad (11.43)
```

**Solution to exercise 11.4 (p.186)（练习 11.4 的解答）.**

该 channel 的 capacity 是 $1$ 减去它加入的 noise 的信息含量。那份信息含量，按 chunk（块）计，是「该 chunk 是否 bursty（成串出错）」这一选择的 entropy $H_2(b)$，加上以概率 $b$ 出现的翻转比特的 entropy $N$，于是每 chunk 合计 $H_2(b) + Nb$（粗略地说；当 $N$ 大时准确）。所以按 bit 计，对 $N = 100$，capacity 是

```math
C = 1 - \left( \frac{1}{N} H_2(b) + b \right) = 1 - 0.207 = 0.793. \qquad (11.44)
```

对照之下，interleaving（交织）把 error bursts 当作独立错误处理，使该 channel 被当成错误概率 $f = 0.2 \times 0.5 = 0.1$ 的 binary symmetric channel，其 capacity 约为 $0.53$。

<span style="color:#1e8449;">**[译注]** (11.44) 与 0.53 的对比，值得盯住机制而不只是记住 1.6 倍这个数。burst channel 的 capacity 之所以高于 interleaving 之后的 BSC，不是因为「burst 更友好」，而因为 interleaving **主动扔掉了一个可观测的量**：burst 内部各 bit 出错是强相关的，interleaving 把这份相关性打散、再当成独立噪声去编码，于是 decoder 面前的信道看起来更糟。抽掉「burst 结构」这个概念，系统会崩在哪？崩在 channel model 的**选择**环节：一切 code 设计的第一颗螺丝是「你在哪个 ensemble 上取平均」，一旦把 burst 误标成 BSC，后续所有 rate 预算就按 $1 - H_2(0.1) = 0.531$ 而不是 $0.793$ 来定，等于自愿放弃约 33% 的带宽。这是 MacKay 全书反复讲的 worst-case-ism 的一个财务版本：把结构化噪声摊平成无结构噪声，付出的是 rate。落点：本题解属书内 p189（本页）；「结构化噪声 → 更高 capacity」的完整处理见书 §11.4（书内 p183，`good` / `very good` code 的定义处）；离散侧的对偶工具挂在 6.042J 的 *Conditional expectation and conditional probability* 单元——conditional entropy 小 ⇒ 联合编码优于分开编码，那条链在 6.042J 只做到「条件化降低方差」，往上接到「条件化降低 rate 预算」需要本书 §11.4 的 coding 定义作桥。</span>


<span style="color:#7f8c8d">书内 p190 ｜ 11 — Error-Correcting Codes and Real Channels</span>

interleaving 丢掉了关于 errors 相关性的有用信息。理论上，如果用一个显式把 bursts 当作 bursts 处理的 code 和 decoder，我们能快约 $(0.79/0.53) \simeq 1.6$ 倍地通信。

**Solution to exercise 11.5 (p.188)（练习 11.5 的解答）.**

(a) 把 exercise 11.1 与 11.2 的结果合起来，我们推断：实输入 $x$、信噪比 $v/\sigma^2$ 的 Gaussian channel 的 capacity 是

```math
C = \tfrac{1}{2} \log\left( 1 + \frac{v}{\sigma^2} \right). \qquad (11.45)
```

(b) 若输入被约束为 binary，$x \in \{\pm\sqrt{v}\}$，则 capacity 由等概率使用这两个输入达到。capacity 退化成一个颇为凌乱的积分：

```math
C'' = \int_{-\infty}^{\infty} dy\, N(y;0) \log N(y;0) - \int_{-\infty}^{\infty} dy\, P(y) \log P(y), \qquad (11.46)
```

其中 $N(y;x) \equiv (1/\sqrt{2\pi}) \exp\left[-(y-x)^2/2\right]$ †，$x \equiv \sqrt{v}/\sigma$，且 $P(y) \equiv [N(y;x) + N(y;-x)]/2$。这个 capacity 小于无约束的 capacity (11.45)，但当信噪比小时，两个 capacity 的数值很接近。

<span style="color:#7f8c8d">† 原书 p190 此处印作 $\exp[(y-x)^2/2]$，**指数上漏了负号**。这不是 OCR 问题（文字层干净），而是原书排印错误：照它写，$N(y;x)$ 在 $|y| \to \infty$ 时发散、根本不归一，于是 (11.46) 里 $\int dy\, N(y;0)\log N(y;0)$ 发散，整条 $C''$ 无定义。按同页 (11.46) 自身的用法（$N$ 必须是概率密度、且 $P(y) = [N(y;x)+N(y;-x)]/2$ 要是混合密度）以及 §11.10 对 exercise 11.1 的解里写出的正确形式 $\exp\!\left(-(y-x)^2/2\sigma^2\right)/\sqrt{2\pi\sigma^2}$，此处应为 $\exp[-(y-x)^2/2]$。译文按语义纠正，原文错式在此记录。</span>

(c) 若输出被 thresholded（做门限判决），Gaussian channel 就变成 binary symmetric channel，其 transition probability 由 p156 定义的 error function $\Phi$ 给出。capacity 为

```math
C'' = 1 - H_2(f), \quad \text{其中} f = \Phi(\sqrt{v}/\sigma). \qquad (11.47)
```

[Figure 11.9：capacity 随信噪比 $\sqrt{v}/\sigma$ 的变化，图中自上而下三条曲线分别是 $C$、$C'$、$C''$；下方那张是同一组数据的 log–log 图。原文既未在本页给出 $C'$ 的解析式，(11.46) 又把它标成 $C''$，两处标签互相冲突；曲线与公式的对应关系无法从文字层复原，故此处不作臆测。]

<span style="color:#7f8c8d">边注（图 11.9 旁）：Capacities（每幅图中自上而下）$C$、$C'$、$C''$，对信噪比 $\sqrt{v}/\sigma$ 作图。下方那张是 log–log 图。</span>

**Solution to exercise 11.9 (p.188)（练习 11.9 的解答）.**

RAID 系统有若干种。最容易理解的一种由 7 块 disk drive（磁盘驱动器）组成，以 $4/7$ 的 rate 存数据，用的是一份 $(7,4)$ Hamming code：每相继的 4 个 bits 被编码，七个 codeword bits 各写入一块 disk。两块、或许三块 disk 挂掉后，其余仍可恢复数据。这里的 effective channel model（有效信道模型）是 binary erasure channel（二元擦除信道），因为假定我们能判断某块 disk 已死。

对某些三块死盘的选择，数据是不可能恢复的；你看得出为什么吗？

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 11.10.[2, p.190]**</span> Give an example of three disk drives that, if lost, lead to failure of the above RAID system, and three that can be lost without failure.

<span style="color:#7f8c8d">中文话题摘要：举出「失掉即失败」的三块盘与「失掉也不失败」的三块盘，并解释二者的结构差别。</span>

**Solution to exercise 11.10 (p.190)（练习 11.10 的解答）.**

$(7,4)$ Hamming code 的 codewords 中有 weight 为 3 的。若损失的三块 disk 恰好对应其中一个 codeword，则其余四块盘只能恢复关于四个 source bits 的 3 个 bits 的信息；第四个 bit 丢了。[cf. exercise 13.13 (p.220)，取 $q = 2$：不存在 binary MDS codes。这个亏空在 §13.11 还会讨论。]

任何其他三块盘的组合都可以安全失掉，因为 generator matrix 对应的那个 $4 \times 4$ submatrix（子矩阵）可逆。

更好的 code 是 digital fountain（数字喷泉）——见第 50 章。

<span style="color:#1e8449;">**[译注]** 「某些三块盘失掉就完蛋」不是偶然的坏运气，而是 linear code 的结构性后果，机制值得说透。设 generator matrix 为 $G$（$4 \times 7$），第 $j$ 列写第 $j$ 块盘。失掉三块盘 = 删掉三列，得到 $4 \times 4$ 方阵 $G_{S}$；能否恢复等价于 $\det G_{S} \neq 0$ 在 GF(2) 上是否成立。而「删三列后奇异」的充要条件是：存在非零 source vector $s$，使 $sG$ 在这三列上全为零、整体却非零——即存在 weight $\le 3$ 且支撑落在 $S$ 内的 codeword，这正是原文说的「三块盘对应一个 weight-3 codeword」。抽掉这条「weight 分布 ↔ 可恢复性」的桥，系统崩在哪？崩在 RAID 设计阶段的容量预算：工程师会以为「任意三块盘冗余」等于「防三故障」，实际上 $(7,4)$ Hamming 的 $d = 3$ 只保证 $t = 1$，$4/7$ 这个 rate 换来的是**平均**可靠性，不是**最坏**可靠性。落点：本题在书内 p190（本页）；反面（$q \gt 2$ 时 MDS 码大量存在，Reed–Solomon 即一例）见书 §13.11（书内 p219，本块 p232）；GF(2) 上的可逆性判定属 6.042J 的 *Modular arithmetic* 与线性方程组单元；工程侧对照读 CSAPP 第 6 章 §6.2 的 disk 组织（那里只讲 striping 与 parity，不讲 weight 分布，两者拼起来才完整）。</span>


<span style="color:#7f8c8d">书内 p191 ｜ Part III</span>

## Part III：Further Topics in Information Theory（第 III 部分　信息论的进一步专题）

<span style="color:#c0392b">**Part III　Further Topics in Information Theory（第 III 部分　信息论的进一步专题）**</span>

<span style="color:#7f8c8d">[本页只有分部扉页，原书无正文。PDF p203 除页眉页脚外，文字层仅有上述一行。]</span>


<span style="color:#7f8c8d">书内 p192 ｜ About Chapter 12</span>

## About Chapter 12（第 12 章导读）

在第 1–11 章里，我们集中处理了 information theory 与 coding theory 的两个侧面：**source coding（信源编码）**——压缩信息，以便高效使用数据传输与存储的 channel；以及 **channel coding（信道编码）**——对信息做冗余编码，以便检测并纠正通信 errors。

在这两个领域里，我们都从忽略实际考虑起步，专注于 coding 的理论极限与可能性问题；随后再讨论实用的 source-coding 与 channel-coding 方案，把重心移向 computational feasibility（计算可行性）。但比较各种 encoding 方案的首要判据，始终是 code 就其所需 channel 资源而言的 efficiency：最好的 source codes 是达到最大压缩的那些；最好的 channel codes 是在给定错误概率下以最高 rate 通信的那些。

本章我们把视角稍微挪一下，把 **information retrieval（信息检索）的易用性**当成首要目标。结果是：在 channel coding 研究里理论上有用的那些 random codes，对快速 information retrieval 也同样有用。

高效的信息检索是大脑似乎不费力就能解决的问题之一；而 content-addressable memory（内容可寻址存储）是我们考察 neural networks 时会研究的题目之一。

<span style="color:#1e8449;">**[译注]** 这一页是全书的一次换轴，值得标出来，否则读者会把第 12 章当成「编码理论的旁支」读过去。前三部分（Ch.1–11）的优化变量是 **rate**：给定错误概率，把 code 效率推向 Shannon limit。第 12 章把优化变量换成 **查询代价**：给定 $S$ 条记录，把「由 $x$ 找 $s$」的时间与空间压到最小。两个问题的数学形状相同（都是 $N$ bits $\to$ $M$ bits 的映射），但失败模式完全不同：code 的失败是「decoder 返回了错的 codeword」，hash 的失败是「返回一个非零 $s$ 而 $x(s) \neq x$」——后者可以靠一次逐 bit 比较就检出，前者不能。抽掉这个区分，系统会崩在哪？崩在「拿 parity-check 的直觉去设计 hash」这一步：你会去在意 minimum distance，而 hash 的正确性判据是 collision 概率加上**可复核性**（p197 的 decoding 段正是靠一次 $x$ 与 $x(s)$ 的逐 bit 比较把假阳性清零）。落点：本页为书内 p192；content-addressable memory 见本书第 39–40 章（Hopfield network，书内 p503 起）；机器侧对照读 CSAPP 第 6 章：cache 的 tag 比较本质上就是「hash + 一次比对」，set index 是 hash 的低位、tag 是被保留的高位，两者的取舍与 §12.3「表太小了怎么办」是同一个 tradeoff。</span>


<span style="color:#7f8c8d">书内 p193 ｜ 12 ｜ 12.1: The information-retrieval problem</span>

## 12　Hash Codes: Codes for Efficient Information Retrieval（第 12 章　哈希码：面向高效信息检索的编码）

### 12.1 The information-retrieval problem（信息检索问题）

information-retrieval（信息检索）问题的一个简单例子，是实现一个电话簿服务：给定一个人的姓名，返回 (a) 该人确实登记在册的确认；(b) 其电话号码与其他细节。我们可以把这个任务形式化如下，其中 $S$ 是必须存入电话簿的姓名条数。

[Figure 12.1：本问题的「演员表」（cast of characters）——三个数量级一览。原书以边注框排版，此处按语义重建为表格。]

| 量 | 符号与量级 |
|---|---|
| string length（串长） | $N \simeq 200$ |
| number of strings（已存串数） | $S \simeq 2^{23}$ |
| number of possible strings（可能串总数） | $2^{N} \simeq 2^{200}$ |

给定一张由 $S$ 个长度 $N$ bits 的 binary strings 组成的列表 $\{x^{(1)}, \dots, x^{(S)}\}$，其中 $S$ 显著小于可能串的总数 $2^{N}$。我们把 $x^{(s)}$ 里的上标 $s$ 称作该串的 record number（记录号）。这个设定的意思是：$s$ 按顾客被加入电话簿的次序遍历，$x^{(s)}$ 就是顾客 $s$ 的姓名。为简单起见，我们假定所有人姓名长度相同。姓名长度也许是 $N = 200$ bits，而我们想存一千万名顾客的细节，于是 $S \simeq 10^{7} \simeq 2^{23}$。我们忽略两位顾客姓名完全相同的可能性。

任务是构造从 $s$ 到 $x^{(s)}$ 的映射的 inverse（逆映射），即做一个系统：给定一个串 $x$，若存在 $s$ 使 $x = x^{(s)}$，就返回该 $s$；否则报告不存在这样的 $s$。（一旦拿到 record number，我们就能去另一块满是电话号码的 memory 里查 memory location $s$，取出所需号码。）解决这个任务的目标，是让所用 computational resources 最少：一方面是存 $x \to s$ 这个逆映射所占的 memory 量，另一方面是算出该逆映射所需的时间。而且，最好这个逆映射的实现方式还容许在少量机时内把新串加入电话簿。

#### 一些标准解法

对 information-retrieval 问题，最简单也最笨的两种解法是 look-up table（查找表）与 raw list（原始列表）。

**The look-up table（查找表）** 是一块大小为 $2^{N} \log_2 S$ 的 memory，其中 $\log_2 S$ 是存放一个 $1$ 到 $S$ 之间整数所需的 memory 量。在这 $2^{N}$ 个位置中，除对应某串 $x^{(s)}$ 的位置 $x$ 写入 $s$ 的值以外，其余都写零。

look-up table 又简单又快，但前提是有足够 memory 放这张表，且在该 memory 里查表项的成本与 memory 大小无关。可是按我们对任务的定义，$N$ 约为 200 bits 或更多，于是所需 memory 的量级会是 $2^{200}$；这个解法完全不可能。别忘了，太阳系里的粒子数也不过约 $2^{190}$。

**The raw list（原始列表）** 是一张按 $s$ 的值排序的、由有序对 $(s, x^{(s)})$ 组成的简单列表。由 $x$ 到 $s$ 的映射靠搜索这张串表来实现：从顶部开始，把进来的串 $x$ 与每条记录 $x^{(s)}$ 比较，直到找到匹配。这个系统极易维护，用的 memory 也少，约 $SN$ bits，但用起来很慢——平均要做五百万次两两比较。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 12.1.[2, p.202]**</span> Show that the average time taken to find the required string in a raw list, assuming that the original names were chosen at random, is about $S + N$ binary comparisons. (Note that you don't have to compare the whole string of length $N$, since a comparison can be terminated as soon as a mismatch occurs; show that you need on average two binary comparisons per incorrect string match.) Compare this with the worst-case search time – assuming that the devil chooses the set of strings and the search key.

<span style="color:#7f8c8d">中文话题摘要：证明平均搜索代价约 $S + N$ 次二元比较，其中「不匹配串平均只花 2 次比较」是关键；再与「魔鬼选串、魔鬼选 key」的最坏情形对照。</span>

电话簿实际采用的标准做法，比 look-up table 与 raw list 都更好：用按字母排好的列表。

**Alphabetical list（字母序列表）**。把各串 $\{x^{(s)}\}$ 按字母序排好。查一条记录现在通常比 raw list 快，因为我们可以利用这份 sortedness（有序性）：比如把电话簿翻到中间那页，把那里看到的姓名与目标串比较；若目标「大于」中间那个串，我们就知道所需串（如果存在）必在字母序目录的后半；否则查前半。迭代这个「对半切」的过程，我们就能在 $\lceil \log_2 S \rceil$ 次 string comparison 内确定目标串、或确定该串不在册。随着搜索推进，每次 string comparison 所期望的二元比较次数会趋于增大，但所需二元比较的总数不会超过 $\lceil \log_2 S \rceil N$。

所需 memory 量与 raw list 相同。

向数据库加入新串时，必须把它插到表中的正确位置。找到那个位置约需 $\lceil \log_2 S \rceil$ 次二元比较。

我们能改进这套行之有效的字母序表吗？让我们从几个新视角来看这个任务。

任务是构造一个从 $N$ bits 到 $\log_2 S$ bits 的映射 $x \to s$。这是个 pseudo-invertible（伪可逆）映射，因为对任何映到非零 $s$ 的 $x$，顾客数据库里都存着把我们从 $s$ 带回去的配对 $(s, x^{(s)})$。我们此前在哪儿见过「从 $N$ bits 映到 $M$ bits」这个想法？

我们碰到过两次。第一次是在 source coding 里，我们研究过把 $N$ 个符号的串映射到列表中某一个 label 的 block codes。information retrieval 这个任务，与「为典型集压缩码造一个 encoder」这件事相似（那件事我们其实从未真正解决）。

第二次把 bit strings 映到另一维数的 bit strings，是在研究 channel codes 的时候。那里我们考虑从 $K$ bits 到 $N$ bits 的 code，$N$ 大于 $K$，并用 random codes 取得了理论进展。

在 hash codes 里，我们把这两个概念合到一起：我们要研究从 $N$ bits 映到 $M$ bits 的 random codes，其中 $M$ 小于 $N$。

思路是把原来的高维空间映下来，映到一个低维空间；在那个低维空间里，实现我们刚才否决掉的笨办法（look-up table）是可行的。

[Figure 12.2：修订后的演员表——引入 hash 之后各量的量级。原书为边注框，此处按语义重建为表格。]

| 量 | 符号与量级 |
|---|---|
| string length | $N \simeq 200$ |
| number of strings | $S \simeq 2^{23}$ |
| size of hash function（hash 输出长度） | $M \simeq 30$ bits |
| size of hash table（表大小） | $T = 2^{M} \simeq 2^{30}$ |


<span style="color:#7f8c8d">书内 p194 ｜ 12 — Hash Codes: Codes for Efficient Information Retrieval</span>

<span style="color:#1e8449;">**[译注]** 上面两张「演员表」是全章唯一真正的定量骨架，抽掉它，后面所有「$T$ 该多大」的讨论都会变成无根的空谈。为什么 $M \simeq 30$ 是关键数字而不是随手取的值？因为 table 大小 $T = 2^{M}$ 要压到「能装进真实 memory」的量级：$2^{30}$ 个单元的表格、每单元 4 字节，就是 4 GB 量级的上限附近；而 $2^{200}$ 是不可能。这条从 $2^{200}$ 到 $2^{30}$ 的压缩比约为 $10^{-51}$，它一次性把 lookup 的 O(1) 换成了可以支付的成本，代价是 collision 从「不可能」变成「必然」（(12.6) 的期望值为 46566，见 p202 的解）。抽掉「$M$ 必须显著小于 $N$、又必须让 $T$ 略大于 $S$」这两条约束中的任何一条，系统就崩：$M$ 取 $N$ 则 memory 爆掉，$M$ 取得太小则 bucket 里挤满串、lookup 退化成 raw list 的 $O(S)$ 线性扫描。可点开验证的落点：$S \simeq 10^{7} \simeq 2^{23}$ 与 $T = 2^{30}$ 的比值 $T/S = 2^{7} = 128$，正是原文 p195 所说「比 $S$ 大一点，比如说十倍」这一档的合理邻域；而 $2^{200}$ 与「太阳系粒子数 $2^{190}$」的比值只有 $2^{10} = 1024$，也就是原文那句「别忘了」的量化含义。结构性的对照读 6.042J 的 *Counting / Pigeonhole principle* 单元：pigeonhole 只告诉你「$M \lt N$ 必有 collision」，而这里需要的是「collision 的**期望个数**是多少」——从存在性走到期望值，正是 (12.6) 那一步。</span>


<span style="color:#7f8c8d">书内 p195 ｜ 12.2: Hash codes</span>

### 12.2 Hash codes（哈希码）

先描述 hash code 如何工作，再研究理想化 hash codes 的性质。hash code 借助一个称为 hash function（哈希函数）的 pseudo-random function（伪随机函数）来实现 information-retrieval 问题的解：它把 $N$-bit 串 $x$ 映到 $M$-bit 串 $h(x)$，其中 $M$ 小于 $N$。$M$ 的典型取法是让「table size」$T \simeq 2^{M}$ 比 $S$ 稍大一点——比如说大十倍。举例来说，若我们预期 $S$ 约一百万，就可能把 $x$ 映成一个 30-bit 的 hash $h$（不管每个条目 $x$ 的大小 $N$ 是多少）。hash function 是某个固定的确定性函数，理想情况下应当与一个固定的 random code 无法区分。就实用而言，hash function 必须计算得快。

hash function 的两个简单例子：

**Division method（除法取余法）**。table size $T$ 取素数，最好是一个不接近 $2$ 的幂的素数。hash 值就是整数 $x$ 除以 $T$ 的余数。

**Variable string addition method（变长串加法）**。此法假定 $x$ 是一个 byte 串，table size $T = 256$。把 $x$ 的各字符按模 256 相加。这个 hash function 有个缺陷：它把互为 anagram（字母异位词）的串映到同一个 hash 上。

改进办法是：每加完一个字符，就把running total（累计值）过一个固定的 pseudorandom permutation（伪随机置换）。在 table size $\le 65536$ 的 **variable string exclusive-or method**（变长串异或法）里，串以这种方式被 hash 两次，两次的初始累计值分别取 $0$ 与 $1$（algorithm 12.3）。结果是一个 16-bit hash。

选定 hash function $h(x)$ 之后，我们按如下方式实现信息检索器。（见 figure 12.4。）

**Encoding（编码侧）**。创建一块名为 hash table（哈希表）的 memory，大小为 $2^{M} b$ 个 memory unit，其中 $b$ 是表示 $0$ 到 $S$ 之间一个整数所需的 memory 量。这张表初始时全部置零。每条 memory $x^{(s)}$ 都过一遍 hash function，并在 hash 表中对应所得向量 $h^{(s)} = h(x^{(s)})$ 的位置写入整数 $s$——除非该表项已被占用；那种情况下我们说 $x^{(s)}$ 与某个更早的 $x^{(s')}$ 发生了 collision（碰撞），两者碰巧有同一个 hash code。collision 可用多种方式处理——我们马上讨论几种——但先把基本图景讲完。


<span style="color:#7f8c8d">书内 p196 ｜ 12 — Hash Codes: Codes for Efficient Information Retrieval</span>

[Algorithm 12.3：变长串异或法的 C 实现（作者 Thomas Niemann），从一个串 $x$ 生成取值范围 $0 \dots 65535$ 的 hash $h$。原书排版为边注代码框，此处按文字层逐行保留代码本身。]

```c
unsigned char Rand8[256];
// This array contains a random permutation from 0..255 to 0..255
int Hash(char *x) {
  // x is a pointer to the first char;
  int h;                    // *x is the first character
  unsigned char h1, h2;
  if (*x == 0) return 0;    // Special handling of empty string
  h1 = *x; h2 = *x + 1;     // Initialize two hashes
  x++;                      // Proceed to the next character
  while (*x) {
    h1 = Rand8[h1 ^ *x];    // Exclusive-or with the two hashes
    h2 = Rand8[h2 ^ *x];    // and put through the randomizer
    x++;
  }                         // End of string is reached when *x=0
  h = ((int)(h1)<<8) |      // Shift h1 left 8 bits and add h2
      (int) h2 ;
  return h ;                // Hash is concatenation of h1 and h2
}
```

[Figure 12.4：hash 用于信息检索的机制图。左侧是 $S$ 条长度为 $N$ bits 的 strings，经 hash function 映到 $M$ bits 的 hashes，再落到大小为 $T = 2^{M}$ 的 hash table 各行；对每个串 $x^{(s)}$ 算出 $h = h(x^{(s)})$，把 $s$ 的值写进 hash 表的第 $h$ 行；表中空白行填零。原图的多条箭头（哪些 $x^{(s)}$ 落到同一行）取决于具体 hash 函数取值，文字层无法复原箭头归属，此处只保留结构与原文图注给出的规则。]


<span style="color:#7f8c8d">书内 p197 ｜ 12.3: Collision resolution</span>

**Decoding（解码侧）**。要取出与目标向量 $x$ 对应的那条信息，我们算出 $x$ 的 hash，并看 hash 表中对应位置。若那里是零，我们就立刻知道串 $x$ 不在数据库中。这个回答的代价是一次 hash-function 求值，加上在大小为 $2^{M}$ 的表里的一次查表。反之，若表中有一个非零表项 $s$，则有两种可能：要么向量 $x$ 确实等于 $x^{(s)}$；要么向量 $x^{(s)}$ 是另一个碰巧与目标 $x$ 有相同 hash code 的向量。（还有第三种可能：这个非零表项也许与我们尚未讨论的 collision-resolution 系统有关。）

要检查 $x$ 是否确实等于 $x^{(s)}$，我们取出这个试探性答案 $s$，在原来的正向数据库里查出 $x^{(s)}$，把它与 $x$ 逐 bit 比较；若匹配，就把 $s$ 作为所需答案报告。这次成功的检索，总代价是一次 hash-function 求值、一次在大小为 $2^{M}$ 的表里查表、一次在大小为 $S$ 的表里查表，以及 $N$ 次二元比较——这可能比 §12.1 里给出的那些简单解法便宜得多。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 12.2.[2, p.202]**</span> If we have checked the first few bits of $x^{(s)}$ with $x$ and found them to be equal, what is the probability that the correct entry has been retrieved, if the alternative hypothesis is that $x$ is actually not in the database? Assume that the original source strings are random, and the hash function is a random hash function. How many binary evaluations are needed to be sure with odds of a billion to one that the correct entry has been retrieved?

<span style="color:#7f8c8d">中文话题摘要：先用 likelihood ratio 把「逐 bit 相符」换算成 odds，再反推「要多少 bit 才够十亿比一」，本质仍是 Bayes 反演。</span>

只要 hash function $h(x)$ 能作用于任意长度的串，这套 hash 信息检索法就可以用于任意长度的 $x$。

### 12.3 Collision resolution（碰撞消解）

我们将研究两种消解 collision 的方式：表内追加（appending in table）与异地存放（storing elsewhere）。

**Appending in table（表内追加）**

编码时，若发生 collision，我们就沿 hash 表继续往下，把 $s$ 的值写进下一个当前为零的可用位置。若在碰到零之前就走到表底，则从表头继续。

解码时，若我们算出 $x$ 的 hash code，发现表中所含的 $s$ 并不指向一个与线索 $x$ 相符的 $x^{(s)}$，就沿 hash 表继续往下，直到要么找到一个 $x^{(s)}$ 确实与线索 $x$ 相符的 $s$（此时完成），要么碰到一个零（此时我们知道线索 $x$ 不在数据库中）。

对这个方法而言，表的大小显著大于 $S$ 是本质要求。若 $2^{M} \lt S$，编码规则就会卡住，最后那些串无处可放。

**Storing elsewhere（异地存放）**

更稳健、更灵活的方法是用指针指向额外的 memory 块，把撞车的串存在那里。具体做法很多。举例来说，我们可以在 hash 表的第 $h$ 个位置存一个指针（必须能与合法的 record number $s$ 区分开），指向一个「bucket（桶）」，所有 hash code 为 $h$ 的串都排成一个有序表存在该桶里。编码器在创建 hash 表与 buckets 的过程中，把每个 bucket 内的串按字母序排好。

解码器只需去相应 bucket 里看，然后对那里面短短的串表做一次简短的字母序搜索。

这种把串存进 buckets 的做法，允许把 hash 表做得相当小——这在实用上可能有益。我们可以把它做得小到几乎所有串都卷入 collision，于是所有 bucket 里都只有少量串。要在 bucket 中辨识出哪个串与线索 $x$ 相符，只需少量二元比较。

<span style="color:#1e8449;">**[译注]** §12.3 两种 collision resolution 放在一起看，才能看出「表大小」这个旋钮真正在换什么。Appending in table（开放寻址）把 collision 的代价推到**后续位置**，于是表必须显著大于 $S$（$2^{M} \lt S$ 时编码会卡死——这是原文唯一的硬性失败条件）；Storing elsewhere（链接 / bucket）把代价推到**表外的指针**，于是表可以故意做小。抽掉「collision 必然存在」这个前提，两者都会退化成毫无意义的复杂度：如果 $M = N$，hash 就是无损映射，根本不需要 resolution。而正因为 $M \lt N$ 是 chapter 的出发点（p195 的 Figure 12.2：$2^{200} \to 2^{30}$），resolution 不是补丁，而是**这套方案的组成部分**。落点：本页为书内 p197；期望 collision 数的定量结果在 §12.4 与 exercise 12.3 的解（书内 p202，(12.6)）；「装填因子与开放寻址代价」的工程细节读 CSAPP 第 6 章 §6.4 cache 的 set-associativity 与 conflict miss——组相联就是「bucket」在硬件里的形态，而直接映射 cache 的 thrashing 正是 appending 策略在小表下的病；离散侧的期望值计算在 6.042J 的 *Expectation / Linearity of expectation* 单元（线性期望不要求独立，这正是 (12.6) 能直接用 $\binom{S}{2}/T$ 的原因）。</span>


<span style="color:#7f8c8d">书内 p198 ｜ 12.4: Planning for collisions ｜ 12.5: Other roles for hash codes</span>

### 12.4 Planning for collisions: a birthday problem（为碰撞做规划：一个生日问题）

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 12.3.[2, p.202]**</span> If we wish to store $S$ entries using a hash function whose output has $M$ bits, how many collisions should we expect to happen, assuming that our hash function is an ideal random function? What size $M$ of hash table is needed if we would like the expected number of collisions to be smaller than 1? What size $M$ of hash table is needed if we would like the expected number of collisions to be a small fraction, say 1%, of $S$? [Notice the similarity of this problem to exercise 9.20 (p.156).]

<span style="color:#7f8c8d">中文话题摘要：算出期望 collision 数 $S(S-1)/(2T)$，再反解「期望小于 1」需要 $M \gt 2\log_2 S$、「只有 1% 的串撞车」只需 $M \gt \log_2 S + \log_2(1/f)$；这两条 scaling 是全节的结论。</span>

### 12.5 Other roles for hash codes（哈希码的其他角色）

#### Checking arithmetic（核对算术）

若你想核对一次手算的加法，nine casting out（弃九法）可能有用。在弃九法里，我们取各加数的所有数字之和（模九），再与被认为答案的各数字之和（模九）比较。[稍加练习，这些和可以算得比原式整体加法快得多。]

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 12.4（例 12.4）</span>

在边注所示的计算中，$189 + 1254 + 238$ 各数字之和模九为 $7$，而 $1+6+8+1$ 之和模九也是 $7$。于是这个计算通过了弃九检验。

<span style="color:#7f8c8d">边注（原书公式旁竖排）：$189 + 1254 + 238 = 1681$。</span>

弃九法给出了 hash function 的一个简单例子。对任何形如 $a + b + c + \cdots$ 的加法式，其中 $a, b, c, \dots$ 是十进制数，我们定义 $h \in \{0,1,2,3,4,5,6,7,8\}$ 为

```math
h(a + b + c + \cdots) = \text{sum modulo nine of all digits in } a, b, c, \dots ; \qquad (12.1)
```

于是十进制算术有一个好性质：若

```math
a + b + c + \cdots = m + n + o + \cdots \qquad (12.2)
```

则 hash 值 $h(a+b+c+\cdots)$ 与 $h(m+n+o+\cdots)$ 相等。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 12.5.[1, p.203]**</span> What evidence does a correct casting-out-nines match give in favour of the hypothesis that the addition has been done correctly?

<span style="color:#7f8c8d">中文话题摘要：把「弃九相符」当作 datum，写出 posterior ratio；答案取决于对错误模型的假设——若错误是「乘 10」或「换位相邻数字」这两类，弃九完全看不见，证据为零。</span>


<span style="color:#7f8c8d">书内 p199 ｜ 12.5: Other roles for hash codes</span>

#### Error detection among friends（友方之间的错误检测）

两个文件是否相同？若两个文件在同一台机器上，我们尽可逐 bit 比较。但若两个文件分处两台机器，最好能有办法在不把其中一个文件从 A 传到 B 的前提下，确认两者完全相同。[而且即使我们真的把其中一个传过去了，我们仍然希望有办法确认它收到时未被改动！]

这个问题可以用 hash codes 解决。设 Alice 与 Bob 分别是两个文件的持有者；Alice 把文件发给了 Bob，双方想确认它无误地收到了。若 Alice 算出她那文件的 hash 并发给 Bob，Bob 用同一个 $M$-bit hash function 算出他那文件的 hash，而两个 hash 相符，则 Bob 可以推断：两个文件几乎必然是同一个。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 12.6（例 12.6）</span>

false negative（假阴性）的概率是多少？也就是：已知两个文件确实不同，而两个 hash 仍然相同的概率是多少？

设 hash function 是随机的，且造成两文件不同的过程对 hash function 一无所知，则 false negative 的概率是 $2^{-M}$。

一个 32-bit hash 给出的 false negative 概率约为 $10^{-10}$。常见做法是使用一种称为 32-bit cyclic redundancy check（32 位循环冗余校验）的 linear hash function 来检测文件中的错误。（cyclic redundancy check 是一组 32 个 parity-check bits，类似于 $(7,4)$ Hamming code 的那 3 个 parity-check bits。）

若要求 false-negative rate 小于十亿分之一，只要错误来自 noise，$M = 32$ bits 就足够。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 12.7.[2, p.203]**</span> Such a simple parity-check code only detects errors; it doesn't help correct them. Since error-correcting codes exist, why not use one of them to get some error-correcting capability too?

<span style="color:#7f8c8d">中文话题摘要：问「既然有纠错码，为什么文件校验还用只查不纠的 CRC」；答案要走信息量账——指明 8 个坏 bit 的位置就要约 180 bits。</span>

#### Tamper detection（防篡改检测）

若两个文件的差异不是单纯「noise」，而是由对手造成的呢？设有一位聪明的伪造者 Fiona，她改动原文件，做出一份声称是 Alice 文件的伪件。Alice 怎样才能为该文件生成一个 digital signature（数字签名），使 Bob 能确认无人改动过它？又怎样才能防止 Fiona 窃听 Alice 的签名、再把它贴到别的文件上？

我们假定 Alice 为文件算出一个 hash function 并安全地发给 Bob。若 Alice 为文件算的是像 linear cyclic redundancy check 这样的简单 hash function，而 Fiona 知道这就是校验文件完整性的方法，那么 Fiona 可以对她选定的改动做完之后，用 linear algebra 轻松地另找出 32 个左右的单个 bits，把这些 bit 翻转就能把文件的 hash function 还原成原值。**linear hash functions 对伪造者不提供任何安全性。**

因此我们必须要求 hash function 难以求逆，使无人能构造出「改动之后 hash function 不受影响」的篡改。但我们仍希望 hash function 易于计算，这样 Bob 不必为验证收到的每个文件花上几小时。这样一种「易算、难逆」的 hash function 称为 one-way hash function（单向哈希函数）。找出这类函数是 cryptography（密码学）的活跃研究领域之一。


<span style="color:#7f8c8d">书内 p200 ｜ 12 — Hash Codes: Codes for Efficient Information Retrieval</span>

自由软件社区广泛使用、用于确认两个文件没有差异的 hash function 是 MD5，它产生 128-bit hash。它的工作原理细节相当复杂，涉及绕来绕去的 exclusive-or-ing、if-ing 与 and-ing。<sup>1</sup>

即使有了好的 one-way hash function，只要 Fiona 能接触到 hash function，上面描述的数字签名仍然易受攻击。Fiona 可以拿被篡改的文件，再去搜寻对它的一点微小改动，使它的 hash 与 Alice 文件的原始 hash 相符。这要花些时间——若 hash function 是 32 bits，平均约 $2^{32}$ 次尝试——但最终 Fiona 会找到一份与给定 hash 相符的篡改文件。

要能抵御伪造，数字签名要么得有足够多的 bits，使这种随机搜索耗时过久；要么 hash function 本身必须保密。

**Fiona 必须对大约 $2^{M}$ 个文件做 hash 才能作弊。$2^{32}$ 次文件改动并不算多，所以 32-bit hash function 不足以防止伪造。**

另一位有伪造动机的人是 Alice 自己。举例来说，她可能就某场比赛的结果下注，却不愿公开自己的预测；一种下注方法是把她那份注的 hash 发给赌注登记人 Bob。事后再把注的细节发给 Bob。每个人都可以确认她的注与此前公布的 hash 一致。[这种「秘密公布」的方法，Isaac Newton 与 Robert Hooke 想确立科学想法的优先权而又不愿泄露时都用过。Hooke 的 hash function 是字母排序，如把 UT TENSIO, SIC VIS 变成 anagram CEIIINOSSSTTUV 那样。] 这样的 protocol 依赖一个假设：事后 Alice 无法改动她的注而不让 hash 出错。要用多大的 hash function 才能确保 Alice 无法作弊？答案与上面为击败 Fiona 所需的 hash 大小不同，因为 Alice 是两份文件的作者。Alice 可以通过搜寻「hash 彼此相同的两份文件」来作弊。举例来说，若她想以一份注的价钱下两份注，她可以造出大量（$N_1$ 个）注一的版本（彼此只在细节上有微小差别），以及大量（$N_2$ 个）注二的版本，把它们全部 hash 一遍。若两个不同类型的注的 hash 之间出现 collision，她就可以提交那个共同的 hash，从而给自己买到「两份注任选其一」的选择权。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 12.8（例 12.8）</span>

若 hash 有 $M$ bits，$N_1$ 与 $N_2$ 要多大，Alice 才有较大机会找到两个 hash 相同的不同注？

这是个 birthday problem（生日问题），像 exercise 9.20 (p.156) 一样。若聚会上有 $N_1$ 个 Montague 与 $N_2$ 个 Capulet，每人被分配一个 $M$ bits 的「生日」，则一个 Montague 与一个 Capulet 之间碰撞的期望个数是

```math
N_1 N_2 2^{-M}, \qquad (12.3)
```

<sup>1</sup> http://www.freesoft.org/CIE/RFC/1321/3.htm
