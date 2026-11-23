<!-- 书页 101–150｜来源：A 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->


<span style="color:#7f8c8d">书内 p102 ｜ 5.6: Disadvantages of the Huffman code</span>

### 5.7 Summary（小结）

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Kraft inequality（Kraft 不等式）</span>

如果一个码是 uniquely decodeable 的，那么它的长度必须满足

```math
\sum_i 2^{-l_i} \le 1. \qquad (5.25)
```

对任何满足 Kraft 不等式的长度，都存在具有这些长度的 prefix code。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Optimal source codelengths（最优的 source codelength）</span>

一个 ensemble 的 optimal source codelength 等于其 Shannon information content，

```math
l_i = \log_2 \frac{1}{p_i}, \qquad (5.26)
```

反过来，任何一组 codelength 都定义 implicit probabilities

```math
q_i = \frac{2^{-l_i}}{z}. \qquad (5.27)
```

relative entropy $D_{KL}(p||q)$ 度量的是：当 ensemble 的真实概率分布是 $p$，而我们使用 implicit probabilities 为 $q$ 的码时，每符号浪费了多少 bit。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Source coding theorem for symbol codes（symbol code 的信源编码定理）</span>

对 ensemble $X$，存在一个 prefix code，其 expected length 满足

```math
H(X) \le L(C, X) < H(X) + 1. \qquad (5.28)
```

Huffman coding algorithm 迭代地产生一个 optimal symbol code。在每一轮迭代中，把概率最小的两个符号合并。

### 5.8 Exercises（习题）


<span style="color:#7f8c8d">书内 p102 ｜ 5 -- Symbol Codes</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.19 [2]</span>

Is the code {00, 11, 0101, 111, 1010, 100100, 0110} uniquely decodeable?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.20 [2]</span>

Is the ternary code {00, 012, 0110, 0112, 100, 201, 212, 22} uniquely decodeable?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.21 [3, p.106]</span>

Make Huffman codes for X^2, X^3 and X^4 where A_X = {0, 1} and P_X = {0.9, 0.1}. Compute their expected lengths and compare them with the entropies H(X^2), H(X^3) and H(X^4).

Repeat this exercise for X^2 and X^4 where P_X = {0.6, 0.4}.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.22 [2, p.106]</span>

Find a probability distribution {p_1, p_2, p_3, p_4} such that there are two optimal codes that assign different lengths {l_i} to the four symbols.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.23 [3]</span>

(Continuation of exercise 5.22.) Assume that the four probabilities {p_1, p_2, p_3, p_4} are ordered such that p_1 >= p_2 >= p_3 >= p_4 >= 0. Let Q be the set of all probability vectors p such that there are two optimal codes with different lengths. Give a complete description of Q. Find three probability vectors q^(1), q^(2), q^(3), which are the convex hull of Q, i.e., such that any p in Q can be written as

```math
p = \lambda_1 q^{(1)} + \lambda_2 q^{(2)} + \lambda_3 q^{(3)}, \qquad (5.29)
```

where {lambda_i} are positive.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.24 [1]</span>

Write a short essay discussing how to play the game of twenty questions optimally. [In twenty questions, one player thinks of an object, and the other player has to guess the object using as few binary questions as possible, preferably fewer than twenty.]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.25 [2]</span>

Show that, if each probability p_i is equal to an integer power of 2 then there exists a source code whose expected length equals the entropy.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.26 [2, p.106]</span>

Make ensembles for which the difference between the entropy and the expected length of the Huffman code is as big as possible.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.27 [2, p.106]</span>

A source X has an alphabet of eleven characters {a, b, c, d, e, f, g, h, i, j, k}, all of which have equal probability, 1/11.

Find an optimal uniquely decodeable symbol code for this source. How much greater is the expected length of this optimal code than the entropy of X?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.28 [2]</span>

Consider the optimal symbol code for an ensemble X with alphabet size I from which all symbols have identical probability p = 1/I. I is not a power of 2.

Show that the fraction f^+ of the I symbols that are assigned codelengths equal to

```math
l^+ \equiv \lceil \log_2 I \rceil \qquad (5.30)
```

satisfies

```math
f^+ = 2 - \frac{2^{l^+}}{I} \qquad (5.31)
```

and that the expected length of the optimal symbol code is

```math
L = l^+ - 1 + f^+. \qquad (5.32)
```

By differentiating the excess length Delta L = L - H(X) with respect to I, show that the excess length is bounded by

```math
\Delta L \le \frac{1}{\ln 2} - \frac{\ln \ln 2}{\ln 2} - 1 = 0.086. \qquad (5.33)
```

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.29 [2]</span>

Consider a sparse binary source with P_X = {0.99, 0.01}. Discuss how Huffman codes could be used to compress this source efficiently. Estimate how many codewords your proposed solutions require.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.30 [2]</span>

Scientific American carried the following puzzle in 1975.

The poisoned glass. `Mathematicians are curious birds', the police commissioner said to his wife. `You see, we had all those partly filled glasses lined up in rows on a table in the hotel kitchen. Only one contained poison, and we wanted to know which one before searching that glass for fingerprints. Our lab could test the liquid in each glass, but the tests take time and money, so we wanted to make as few of them as possible by simultaneously testing mixtures of small samples from groups of glasses. The university sent over a


<span style="color:#7f8c8d">书内 p103 ｜ 5.8: Exercises</span>

mathematics professor to help us. He counted the glasses, smiled and said:

` "Pick any glass you want, Commissioner. We'll test it first."
` "But won't that waste a test?" I asked.
` "No," he said, "it's part of the best procedure. We can test one glass first. It doesn't matter which one."
` "How many glasses were there to start with?" the commissioner's wife asked.
` "I don't remember. Somewhere between 100 and 200."

What was the exact number of glasses?

Solve this puzzle and then explain why the professor was in fact wrong and the commissioner was right. What is in fact the optimal procedure for identifying the one poisoned glass? What is the expected waste relative to this optimum if one followed the professor's strategy? Explain the relationship to symbol coding.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.31 [2, p.106]</span>

Assume that a sequence of symbols from the ensemble X introduced at the beginning of this chapter is compressed using the code C3. Imagine picking one bit at random from the binary encoded sequence c = c(x_1)c(x_2)c(x_3).... What is the probability that this bit is a 1?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.32 [2, p.107]</span>

How should the binary Huffman encoding scheme be modified to make optimal symbol codes in an encoding alphabet with q symbols? (Also known as `radix q'.)

#### Mixture codes（混合码）

一个诱人的想法是：由若干个给不同符号指派不同长度 codeword 的 symbol code 构造一个「metacode」，然后在这些码之间切换，选用那个给当前符号指派最短 codeword 的码。显然我们不能免费这样做。如果希望在两个码之间选择，那么必须把消息加长，以指明正在使用两个码中的哪一个。如果我们用一个前导 bit 来表明这个选择，就会发现所得码是次优的，因为它不完备（也就是说，它不满足 Kraft 等式）。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.33 [3, p.108]</span>

Prove that this metacode is incomplete, and explain why this combined code is suboptimal.

### 5.9 Solutions（解答）

#### Solution to exercise 5.8（p.93）

是的，$C_2 = \{1, 101\}$ 是 uniquely decodeable 的，尽管它不是 prefix code，因为没有两个不同的串会映射到同一个串；只有 codeword $c(a_2) = 101$ 含有符号 0。

#### Solution to exercise 5.14（p.95）

我们想证明：对任何满足 Kraft 不等式的 codeword 长度集合 $\{l_i\}$，都存在具有这些长度的 prefix code。只需设想图 5.8 所示的那些 codeword 处在一个「codeword 超市」里（大小表示代价），证明就很容易得到。我们想象一次买一个 codeword，从最短的 codeword（即最大的那份采购）开始，使用图 5.8 右侧所示的预算。我们从 codeword 超市的一端（比如说顶部）出发，买下所需长度的第一个 codeword。我们在超市里向下前进 $2^{-l}$ 的距离，买下所需的下一个长度的 codeword，如此继续。由于 codeword 长度越来越长、相应区间越来越短，我们总能买到与最近一次采购相邻的 codeword，所以预算不会有浪费。于是到第 $I$ 个 codeword 时，我们已经沿超市向下前进了 $\sum_{i=1}^{I} 2^{-l_i}$ 的距离；如果 $\sum_i 2^{-l_i} \le 1$，我们就能买下全部 codeword 而不会耗尽预算。

[Figure 5.8：codeword 超市与 symbol coding budget。每个 codeword（长度为 $l$）的「代价」$2^{-l}$ 由它所处方框的大小表示。构造 uniquely decodeable 码时可用的总预算是 1。]

#### Solution to exercise 5.16（p.99）

Huffman coding 最优性的证明，取决于证明算法中的关键一步——把概率最小的两个符号赋予相等的码长——不会导致比任何其他码更长的 expected length。我们可以用反证法证明这一点。

假设概率最小的两个符号（记作 $a$ 与 $b$，Huffman 算法会给它们指派等长 codeword）在任何 optimal symbol code 中长度并不相等。那个 optimal symbol code 是某个别的竞争码，其中这两个 codeword 长度 $l_a$ 与 $l_b$ 不相等，且 $l_a < l_b$。不失一般性，我们可以假设这个别的码是 complete prefix code，因为 uniquely decodeable 码的任何一组 codelength 都可以由某个 prefix code 实现。


<span style="color:#7f8c8d">书内 p106 ｜ 5 -- Symbol Codes</span>

在这个竞争码中，必然存在另一个符号 $c$，其概率 $p_c$ 大于 $p_a$，且它在竞争码中的长度大于或等于 $l_b$；因为 $b$ 的 codeword 必然有一个长度相同或更大的相邻 codeword——complete prefix code 从不会有一个长度为最大值的孤立 codeword。

考虑交换 $a$ 与 $c$ 的 codeword（图 5.9），于是 $a$ 用原本属于 $c$ 的较长 codeword 编码，而比 $a$ 更可能的 $c$ 得到较短的 codeword。显然这减小了码的 expected length。expected length 的变化量是 $(p_a - p_c)(l_c - l_a)$。这样我们就与「竞争码是最优的」这一假设矛盾。因此，把相等的编码长度赋予概率最小的两个符号是合理的。

Huffman coding 产生 optimal symbol code。$\square$

[Figure 5.9：证明 Huffman coding 给出 optimal symbol code。假定那个被称为最优的竞争码给概率最小的两个符号 $a$ 与 $b$ 指派了不等长的 codeword。把竞争码中 $a$ 与 $c$ 的 codeword 互换（其中 $c$ 在竞争码中的长度与 $b$ 一样长），我们就能得到一个比竞争码更好的码。这说明竞争码并非最优。表中列出符号、概率、Huffman codeword、竞争码 codeword、修改后的竞争码 codeword。]

#### Solution to exercise 5.21（p.102）

当 $\mathcal{A}_X = \{0, 1\}$、$P_X = \{0.9, 0.1\}$ 时，$X^2$ 的一个 Huffman code 是 $\{00, 01, 10, 11\} \to \{1, 01, 000, 001\}$。这个码的 $L(C, X^2) = 1.29$，而 entropy $H(X^2)$ 是 0.938。

$X^3$ 的一个 Huffman code 是

```math
\{000, 100, 010, 001, 101, 011, 110, 111\} \to \{1, 011, 010, 001, 00000, 00001, 00010, 00011\}.
```

其 expected length 为 $L(C, X^3) = 1.598$，而 entropy $H(X^3)$ 是 1.4069。

$X^4$ 的一个 Huffman code 把十六个 source 串映射为下列 codelength：

```math
\{0000, 1000, 0100, 0010, 0001, 1100, 0110, 0011, 0101, 1010, 1001, 1110, 1101, 1011, 0111, 1111\} \to \{1, 3, 3, 3, 4, 6, 7, 7, 7, 7, 7, 9, 9, 9, 10, 10\}.
```

其 expected length 为 $L(C, X^4) = 1.9702$，而 entropy $H(X^4)$ 是 1.876。

当 $P_X = \{0.6, 0.4\}$ 时，$X^2$ 的 Huffman code 长度为 $\{2, 2, 2, 2\}$；expected length 是 2 bit，entropy 是 1.94 bit。$X^4$ 的一个 Huffman code 见表 5.10。expected length 是 3.92 bit，entropy 是 3.88 bit。

| $a_i$ | $p_i$ | $l_i$ | $c(a_i)$ |
|---|---|---|---|
| 0000 | 0.1296 | 3 | 000 |
| 0001 | 0.0864 | 4 | 0100 |
| 0010 | 0.0864 | 4 | 0110 |
| 0100 | 0.0864 | 4 | 0111 |
| 1000 | 0.0864 | 3 | 100 |
| 1100 | 0.0576 | 4 | 1010 |
| 1010 | 0.0576 | 4 | 1100 |
| 1001 | 0.0576 | 4 | 1101 |
| 0110 | 0.0576 | 4 | 1110 |
| 0101 | 0.0576 | 4 | 1111 |
| 0011 | 0.0576 | 4 | 0010 |
| 1110 | 0.0384 | 5 | 00110 |
| 1101 | 0.0384 | 5 | 01010 |
| 1011 | 0.0384 | 5 | 01011 |
| 0111 | 0.0384 | 4 | 1011 |
| 1111 | 0.0256 | 5 | 00111 |

（上表为 Table 5.10：$p_0 = 0.6$ 时 $X^4$ 的 Huffman code。第 3 列是所分配的 codelength，第 4 列是 codeword。某些概率相同的串，例如第四行与第五行，得到了不同的 codelength。）

#### Solution to exercise 5.22（p.102）

概率集合 $\{p_1, p_2, p_3, p_4\} = \{1/6, 1/6, 1/3, 1/3\}$ 引出两组不同的 optimal codelength，因为在 Huffman coding algorithm 的第二步，我们可以选择三种可能的配对中的任何一种。我们可以把它们放进定长码 $\{00, 01, 10, 11\}$，或者用码 $\{000, 001, 01, 1\}$。两个码的 expected length 都是 2。

另一个解是 $\{p_1, p_2, p_3, p_4\} = \{1/5, 1/5, 1/5, 2/5\}$。

第三个解是 $\{p_1, p_2, p_3, p_4\} = \{1/3, 1/3, 1/3, 0\}$。

#### Solution to exercise 5.26（p.103）

设 $p_{\max}$ 是 $p_1, p_2, \ldots, p_I$ 中最大的概率。expected length $L$ 与 entropy $H$ 之差不会大于 $\max(p_{\max}, 0.086)$（Gallager, 1978）。

要看这个奇怪的 0.086 是怎么来的，请参见 exercise 5.27–5.28。

#### Solution to exercise 5.27（p.103）

长度减 entropy $= 0.086$。


<span style="color:#7f8c8d">书内 p107 ｜ 5.9: Solutions</span>

#### Solution to exercise 5.31（p.104）

这个题有两种正确解法，以及一种流行的错误解法。我们先给出错误答案：

> [note] **Erroneous answer（错误答案）。** 「我们可以先以概率 $p_i$ 随机选一个 source symbol $x_i$，然后从 $c(x_i)$ 中随机取一个 bit 来随机选出一个 bit。若定义 $f_i$ 为 $c(x_i)$ 中取值为 1 的 bit 所占比例，则
>
> ```math
> P(\text{bit is 1}) = \sum_i p_i f_i \qquad (5.34)
> ```
>
> ```math
> = 1/2 \times 0 + 1/4 \times 1/2 + 1/8 \times 2/3 + 1/8 \times 1 = 1/3." \qquad (5.35)
> ```

这个答案是错的，因为它掉进了 bus-stop fallacy（公交站谬误），即 exercise 2.35（p.38）引入的那个谬误：如果公交随机到达，而我们对「从一辆车到下一辆车的平均时间」感兴趣，那么必须区分两种可能的平均值：(a) 从随机选中的一辆车到下一辆车的平均时间；(b) 从你刚错过的那辆车到下一辆车的平均公交间隔。第二种「平均」是第一种的两倍，因为在一个随机时刻等车，会使你的选择偏向那些跟在大间隔之后的车。你不太可能恰好赶上一辆在前一辆车之后 10 秒才到的车！同理，符号 $c$ 与 $d$ 被编码成比 $a$ 更长的二进制串，所以当我们从压缩串中随机取一个 bit 时，我们更可能落在属于 $c$ 或 $d$ 的 bit 上，而不是 (5.34) 式中期望给出的概率。所有概率都需要按 $l_i$ 放大再重新归一化。

> [note] **Correct answer in the same style（同样风格的正确答案）。** 每次编码符号 $x_i$ 时，都往二进制串里加入 $l_i$ 个 bit，其中 $f_i l_i$ 个是 1。每符号加入的 1 的期望个数是
>
> ```math
> \sum_i p_i f_i l_i, \qquad (5.36)
> ```
>
> 而每符号加入的 bit 总数期望是
>
> ```math
> \sum_i p_i l_i. \qquad (5.37)
> ```
>
> 所以传输串中 1 所占比例是
>
> ```math
> P(\text{bit is 1}) = \frac{\sum_i p_i f_i l_i}{\sum_i p_i l_i} \qquad (5.38)
> ```
>
> ```math
> = \frac{1/2 \times 0 + 1/4 \times 1 + 1/8 \times 2 + 1/8 \times 3}{7/4} = \frac{7/4}{7/4} = 1/2.
> ```

对一般的 symbol code 与一般的 ensemble，(5.38) 式这个期望就是正确答案。但在本例中，我们可以用一个更有力的论证。

> [note] **Information-theoretic answer（信息论答案）。** 编码串 $c$ 是最优压缩器的输出，这个压缩器把来自 $X$ 的样本压缩到期望长度为 $H(X)$ bit。我们不能指望把这数据再压缩下去。但如果概率 $P(\text{bit is 1})$ 不等于 1/2，那么就有可能把二进制串进一步压缩（比如用块压缩码）。因此 $P(\text{bit is 1})$ 必须等于 1/2；实际上，压缩流中任何 $l$ 个 bit 的序列取任何特定值的概率都必须是 $2^{-l}$。完美压缩器的输出永远是完美的随机 bit。

> [note] 换句话说，如果概率 $P(\text{bit is 1})$ 不等于 1/2，那么压缩串每 bit 的 information content 至多是 $H_2(P(1))$，它会小于 1；但这与「我们能从 $c$ 恢复原始数据」相矛盾，所以压缩串每 bit 的 information content 必须是 $H(X)/L(C, X) = 1$。

| $a_i$ | $c(a_i)$ | $p_i$ | $l_i$ |
|---|---|---|---|
| a | 0 | 1/2 | 1 |
| b | 10 | 1/4 | 2 |
| c | 110 | 1/8 | 3 |
| d | 111 | 1/8 | 3 |

（上表为码 $C_3$ 的 codeword 与 codelength。）

#### Solution to exercise 5.32（p.104）

编码 alphabet 有 $q$ 个符号时，通用的 Huffman coding algorithm 与二进制情形有一处不同。把 $q$ 个符号合并为 1 个符号，会使符号数减少 $q - 1$。所以如果一开始有 $A$ 个符号，那么只有当 $A \bmod (q-1) = 1$ 时，我们最终才会得到一棵完整的 $q$ 叉树。


<span style="color:#7f8c8d">书内 p108 ｜ 5 -- Symbol Codes</span>

否则我们知道，无论做出什么样的 prefix code，它必然是一棵不完备的树，缺失叶节点的个数（模 $q-1$）等于 $A \bmod (q-1) - 1$。例如，若为八个符号构造三叉树，那么树中不可避免地会缺一个叶节点。

optimal $q$ 叉码的做法是把这些多余的叶节点放在树的最长分支上。这可以通过往原始 source 符号集中加入适当数目的符号来实现，这些额外符号的概率全为零。于是叶节点总数就等于 $r(q-1) + 1$，其中 $r$ 为某整数。随后像二进制 Huffman coding algorithm 那样，反复取概率最小的 $q$ 个符号，用单个符号替换它们。

#### Solution to exercise 5.33（p.104）

我们想表明，贪心的 metacode（那个挑出最短编码的码）实际上是次优的，因为它违反 Kraft 不等式。

我们假设每个符号 $x$ 都得到每个候选码 $C_k$ 所指派的长度 $l_k(x)$。设有 $K$ 个备选码，并且我们可以用一个长度为 $\log K$ bit 的 header（头）来标明正在使用哪个码。那么 metacode 指派的长度 $l'(x)$ 由下式给出：

```math
l'(x) = \log_2 K + \min_k l_k(x). \qquad (5.39)
```

我们计算 Kraft 和：

```math
S = \sum_x 2^{-l'(x)} = \frac{1}{K} \sum_x 2^{-\min_k l_k(x)}. \qquad (5.40)
```

我们把集合 $\mathcal{A}_X$ 划分成互不重叠的子集 $\{A_k\}_{k=1}^{K}$，使得子集 $A_k$ 包含 metacode 通过码 $k$ 发送的所有符号 $x$。那么

```math
S = \frac{1}{K} \sum_k \sum_{x \in A_k} 2^{-l_k(x)}. \qquad (5.41)
```

现在，若某个子码 $k$ 满足 Kraft 等式

```math
\sum_{x \in \mathcal{A}_X} 2^{-l_k(x)} = 1, \qquad (5.42)
```

那么必然有

```math
\sum_{x \in A_k} 2^{-l_k(x)} \le 1,
```

等号只当所有符号 $x$ 都在 $A_k$ 里时才成立，而那将意味着我们只使用了 $K$ 个码中的一个。所以

```math
S \le \frac{1}{K} \sum_{k=1}^{K} 1 = 1, \qquad (5.43)
```

等号只当 (5.42) 式对所有码 $k$ 都取等号时才成立。但所有符号不可能同时属于所有互不重叠的子集 $\{A_k\}_{k=1}^{K}$，所以我们不可能让 (5.42) 式对所有 $k$ 都成立。因此 $S < 1$。


<span style="color:#7f8c8d">书内 p108（续）｜ 5.9: Solutions</span>

看清 mixture code 次优的另一种方式，是考察它所定义的那棵二叉树。考虑两个码的特殊情形。我们发出的第一个 bit 表明正在使用哪个码。现在，在一个 complete code 中，任何后续的二进制串都是合法的串。但一旦我们知道正在使用（比如说）码 A，我们就知道后面只能是一个 codeword，它对应某个在码 A 下比在码 B 下编码更短的符号 $x$。所以有些串是无效的延续，于是 mixture code 不完备，因而次优。

关于这个问题的进一步讨论以及它与 probabilistic modelling（概率建模）的关系，请阅读 28.3 节以及 Frey (1998) 中关于「bits back coding」的内容。


<span style="color:#7f8c8d">书内 p108 ｜ 5 -- Symbol Codes</span>

（书内 p108 是本章正文的收尾页，其内容——$q$ 叉 Huffman 的叶节点数 $r(q-1)+1$、exercise 5.33 的 Kraft 和计算、以及 mixture code 次优性的第二种（二叉树）论证与对 28.3 节 / Frey (1998) 的引用——已按其跨页顺序并入上面的 p118 与 p119 两块。此处只留页码锚点，不重复内容，以免注水。）

---

<span style="color:#7f8c8d">本文件覆盖 PDF p101-p120 = 书内 p089-p108。下一块 PDF（p121-140）自书内 p109 起，为第 6 章 Stream Codes（含 arithmetic coding）。</span>


<span style="color:#7f8c8d">书内 p109 ｜ About Chapter 6（第 6 章导读）</span>

#### 关于第 6 章（About Chapter 6）

在读第 6 章之前，你应当已经读过上一章（第 5 章 Symbol Codes），并且动手做过其中大部分习题。

我们还会用到一些 Bayesian modelling（贝叶斯建模）的想法，它们出现在 exercise 2.8（p.30）附近。


<span style="color:#7f8c8d">书内 p110 ｜ 第 6 章开篇 ／ 6.1 The guessing game</span>

## 6 Stream Codes（第 6 章 流码）

本章讨论两种 data compression（数据压缩）方案。

第一种是 arithmetic coding（算术编码），它是个漂亮的方法，与这样一条哲学紧密配套：压缩来自某个 source 的数据，就意味着对该 source 做 probabilistic modelling（概率建模）。截至 1999 年，文本文件最好的压缩方法都用 arithmetic coding；若干 state-of-the-art（最先进）的图像压缩系统也用它。

第二种是 Lempel-Ziv coding，一种 `universal'（通用）方法，其设计哲学是：我们想要单个压缩算法，它对任何 source 都能干得还算像样。事实上，对许多现实生活中的 source，这种算法所谓的 universal 性质只在数据量大到不切实际的极限下才成立；但即便如此，Lempel-Ziv 压缩仍被广泛使用，而且常常有效。

### 6.1 The guessing game（猜字游戏）

作为理解这两种压缩方法的动机，先看一个典型英文文本文件里的 redundancy（冗余）。这类文件的冗余有若干层次：例如，它包含的 ASCII 字符出现频率并不相等；某些相邻字母对出现的概率高于其他对；而给定上下文、并且对文本有语义理解时，整个词都是可以被预测出来的。

为了展示英文的冗余，以及一种奇特的压缩方式，我们可以设想一场 guessing game（猜字游戏）：让一位说英语的人反复尝试预测文本文件中的下一个字符。

为简单起见，假定允许的 alphabet（字母表）由 26 个大写字母 A, B, C, …, Z 再加一个空格 `-` 组成。游戏要求受试者反复猜下一个字符，唯一反馈是猜对还是猜错，一直猜到猜对为止。猜对之后，我们记下识别该字符共用了多少次猜，然后用同样方式请他猜下一个字符。

让一个人来猜一个句子时，其中一句话给出了如下结果。每个字符下方列出所需的猜次数。

```text
THERE-IS-NO-REVERSE-ON-A-MOTORCYCLE-
1 1 1 5 1 1 2 1 1 2 1 1 15 1 17 1 1 1 2 1 3 2 1 2 2 7 1 1 1 1 4 1 1 1 1 1
```

注意：很多时候下一个字母一次就猜中；而另一些时候，尤其是音节开头，需要猜更多次。

这场游戏和这些结果给了我们什么？第一，它们从英语母语者的视角展示了英文的冗余。第二，这场游戏可以被用于一种 data compression 方案，如下所述。


<span style="color:#7f8c8d">书内 p111 ｜ 6.1 The guessing game ／ 6.2 Arithmetic codes</span>

上面列出的那串数字 `1, 1, 1, 5, 1, …`，是把文本呈现给受试者后得到的。受试者对给定字母最多会猜 27 次，所以受试者为我们做的事情是：把 27 个字母 $\{A, B, C, \ldots, Z, -\}$ 做一个时变的 mapping（映射），映到 27 个数字 $\{1, 2, 3, \ldots, 27\}$ 上，而这 27 个数字可以看成新 alphabet 里的 symbol（符号）。符号总数并没有减少，但因为他使用其中某些符号的频率远高于其他符号 —— 例如 1 和 2 —— 所以这串新符号应当很容易压缩。

那数字串 `1, 1, 1, 5, 1, …` 的解压（uncompression）又该怎么做？解压时我们手上没有原始串 `THERE…`，只有编码后的序列。设想受试者有一个完全相同的双胞胎，也跟我们一起玩这场猜字游戏，就像我们已知源文本一样。如果我们在他猜的次数恰好等于给定数字时叫停他，那么他刚刚猜中的正是正确字母，于是我们可以说「对，就是这个」，然后转向下一个字符。另一种做法是：如果没有同卵双胞胎可用，我们也可以只借助一个人类来设计压缩系统，办法如下。我们选定窗口长度 $L$，也就是展示给这个人的上下文字符数。对长度为 $L$ 的全部 $27^L$ 种可能串，逐一问他「你预测下一个字符是什么？」以及「如果这个预测错了，你接下来会猜什么？」。把他们的回答对 $26 \times 27^L$ 个问题列成表之后，我们就可以在 encoder（编码器）和 decoder（解码器）两端各放一份这份巨大的表，用来替代那两个人类双胞胎。这样的 language model（语言模型）称为 $L$ 阶 Markov model（L 阶马尔可夫模型）。

这些系统显然不现实，无法用于实际压缩，但它们展示了若干条我们马上要用到的原理。

### 6.2 Arithmetic codes（算术编码）

在讨论变长 symbol code、以及构造它们的 optimal（最优）Huffman algorithm 时，我们在收尾处指出了 Huffman code 的两个实际缺陷与理论缺陷（section 5.6）。

这些缺陷由 arithmetic codes 矫正，它由 Elias、Rissanen 和 Pasco 各自发明，后来由 Witten et al. (1987) 做成实用方案。在 arithmetic code 中，probabilistic modelling 与 encoding 运算被清楚分开。整个系统与猜字游戏相当像：人类预测者被 source 的 probabilistic model 取代。当 source 产出每个 symbol 时，概率模型给出下一个 symbol 所有可能取值的 predictive distribution（预测分布），也就是一列正数 $\{p_i\}$，其和为 1。如果我们选择把 source 建模成具有某个已知分布的 i.i.d. symbol，那么预测分布每次都相同；但 arithmetic coding 同样可以毫不费力地处理复杂的 adaptive model（自适应模型），它们给出依赖上下文的预测分布。预测模型通常实现在一个计算机程序里。

<span style="color:#1e8449;">**[译注]**</span> **arithmetic coding 突破的正是符号码那个"每符号至少 1 bit"的天花板：码长直接等于 $-\log P(x)$**

机制：把整条消息 $x_1x_2\ldots x_N$ 映成 $[0,1)$ 里一个长度恰为 $P(x)$ 的子区间，输出该区间的任一内点（足够多 bit 即唯一确定）；编码长度 $\approx \log_2\frac{1}{P(x)}$，于是平均长度 $\approx H$，**误差可以做到远小于 1 bit/消息**，而不是 1 bit/符号。关键在于它不对齐符号边界，所以能"把半个 bit 借给下一个符号"。解码靠同一个累积分布 $F$ 做二分：给定点 $y$，反复查它在哪一段，逐个恢复符号。工程实现要把无限精度换成整数区间 $[\text{low},\text{high})$ 加 renormalization（区间落进 $[0,0.5)$ 或 $[0.5,1)$ 时输出一个 bit 并把区间放大两倍），否则精度会被浮点位数卡死——这一点与 CSAPP 第 2 章"定点运算必须自己管标度与溢出"是同一类工程约束。

代价：arithmetic code 是**脆弱**的——任一 bit 出错，后续区间全错（无自同步），所以存储/传输必须配 ECC（原文 §6.6 明说）。这就是它和 LZ 共享的弱点。

挂载：区间嵌套即 6.042J 的区间套与二进制展开（$[0,1)$ 上的前缀决定区间）；与 Kraft 的"子树占 $2^{-l}$"是同一机制在实数轴上的版本（见 §5.2）。

坐标：§6.2（原书 p.110–116，PDF p.122–128），式 (6.4) 与 Figure 6.4 的 `bbba2` 例子；renormalization 的实用细节见 Witten et al. (1987)。

encoder 利用模型的预测造出一个 binary string（二进制串）。decoder 则利用这个模型的「同卵双胞胎」（正如猜字游戏中那样）来解释这个二进制串。

设 source alphabet 为 $\mathcal{A}_X = \{a_1, \ldots, a_I\}$，其中第 $I$ 个 symbol $a_I$ 具有特殊含义「传输结束」（end of transmission）。source 吐出序列 $x_1, x_2, \ldots, x_n, \ldots$。source 未必产出 i.i.d. symbol。我们假定为 encoder 提供了一个计算机程序，它给出在已出现序列条件下的预测概率分布

$P(x_n = a_i \mid x_1, \ldots, x_{n-1})$。


<span style="color:#7f8c8d">书内 p112 ｜ 6.2 Arithmetic codes</span>

也就是在已出现的序列 $x_1, \ldots, x_{n-1}$ 下，$a_i$ 的 predictive probability distribution（预测概率分布）：$P(x_n = a_i \mid x_1, \ldots, x_{n-1})$。接收端有一个完全相同的程序，产出同一个预测概率分布 $P(x_n = a_i \mid x_1, \ldots, x_{n-1})$。

[Figure 6.1：二进制串在实数轴 $[0, 1)$ 上定义的区间。左侧竖轴标出 $0.00$、$0.25$、$0.50$、$0.75$、$1.00$ 五个刻度，右侧标注对应的二进制表示与串。串 `01` 取出 $[0.25, 0.50)$ 这一段，串 `01101` 取出其中更窄的一段，刻度 1 附近标着指针 $T$ 起始位置，图底部标注 `1`。这张图在第 5 章讨论 symbol-code supermarket（符号码超市）时已经出现过同款。]

#### Concepts for understanding arithmetic coding（理解算术编码的几个概念）

**区间的记号。** 区间 $[0.01, 0.10)$ 指 0.01 与 0.10 之间的所有数，包含 $0.010 \equiv 0.01000\ldots$，但不包含 $0.100 \equiv 0.10000\ldots$。

一段二进制传输在 0 到 1 的实数轴上定义一个区间。例如串 `01` 被解释为二进制实数 $0.01\ldots$，它对应二进制下的区间 $[0.01, 0.10)$，也就是十进制下的区间 $[0.25, 0.50)$。

更长的串 `01101` 对应更小的区间 $[0.01101, 0.01110)$。由于 `01101` 以第一个串 `01` 为 prefix（前缀），新区间是 $[0.01, 0.10)$ 的子区间。因此，一个 1 MB 的二进制文件（$2^{23}$ bit）可以被看成在 0 与 1 之间指定一个数，精度约为两百万个十进制位 —— 两百万个十进制数字，因为每个 byte 译成略多于两个十进制数字。

现在，我们也可以把实数轴 $[0, 1)$ 划分成 $I$ 个区间，长度分别等于概率 $P(x_1 = a_i)$，如图 6.2 所示。

[Figure 6.2：一个 probabilistic model 在实数轴 $[0, 1)$ 上定义出的区间。竖轴自下而上标出 $0.00$、$P(x_1 = a_1)$、$P(x_1 = a_1) + P(x_1 = a_2)$、……、$P(x_1 = a_1) + \ldots + P(x_1 = a_{I-1})$、$1.0$，各段分别标为 $a_1$、$a_2$、……、$a_I$；$a_1$ 与 $a_2$ 两段内部又画出更细的分段，标着 $a_2 a_1$、$a_2 a_5$ 等，用来示意下一层细分。]

接着，我们可以取每个区间 $a_i$，把它再细分成记作 $a_i a_1, a_i a_2, \ldots, a_i a_I$ 的区间，使得 $a_i a_j$ 的长度正比于 $P(x_2 = a_j \mid x_1 = a_i)$。实际上区间 $a_i a_j$ 的长度恰好就是 joint probability（联合概率）

```math
P(x_1 = a_i, x_2 = a_j) = P(x_1 = a_i) P(x_2 = a_j \mid x_1 = a_i). \qquad (6.1)
```

把这个过程迭代下去，区间 $[0, 1)$ 就可以划分成一列区间，分别对应所有可能的有限长串 $x_1 x_2 \ldots x_N$，并且一个区间的长度等于在给定模型下该串的概率。


<span style="color:#7f8c8d">书内 p113 ｜ 6.2 Arithmetic codes ／ Algorithm 6.3 ／ Example：压弯硬币的抛掷</span>

[Algorithm 6.3：arithmetic coding（算术编码）。为串 $x_1 x_2 \ldots x_N$ 迭代地找出区间 $[u, v)$ 的过程：

```text
u := 0.0
v := 1.0
p := v - u
for n = 1 to N {
    Compute the cumulative probabilities Qn and Rn   (6.2, 6.3)
    v := u + p * Rn(xn | x1, ..., xn-1)
    u := u + p * Qn(xn | x1, ..., xn-1)
    p := v - u
}
```

]

#### Formulae describing arithmetic coding（描述算术编码的公式）

图 6.2 所描绘的过程可以明确写出来。区间由下累积概率与上累积概率定义：

```math
Q_n(a_i \mid x_1, \ldots, x_{n-1}) \equiv \sum_{i'=1}^{i-1} P(x_n = a_i \mid x_1, \ldots, x_{n-1}), \qquad (6.2)
```

```math
R_n(a_i \mid x_1, \ldots, x_{n-1}) \equiv \sum_{i'=1}^{i} P(x_n = a_i \mid x_1, \ldots, x_{n-1}). \qquad (6.3)
```

（$Q_n$ 是把下标 $i$ 之前的所有概率累加起来，$R_n$ 是把下标 $i$ 及其之前的概率累加起来；两者之差正是 $P(x_n = a_i \mid \cdot)$，即第 $i$ 个 symbol 在当前上下文下的预测概率。）

当第 $n$ 个 symbol 到达时，我们在第 $n-1$ 层区间上按 $Q_n$ 与 $R_n$ 定义的点做细分。例如，从第一个 symbol 开始，区间 `a_1`、`a_2` 与 `a_I` 分别是

```math
a_1 \leftrightarrow [Q_1(a_1), R_1(a_1)) = [0, P(x_1 = a_1)), \qquad (6.4)
```

```math
a_2 \leftrightarrow [Q_1(a_2), R_1(a_2)) = [P(x_1 = a_1), P(x_1 = a_1) + P(x_1 = a_2)), \qquad (6.5)
```

以及

```math
a_I \leftrightarrow [Q_1(a_I), R_1(a_I)) = [P(x_1 = a_1) + \ldots + P(x_1 = a_{I-1}), 1.0). \qquad (6.6)
```

Algorithm 6.3 描述了通用流程。

要编码一个串 $x_1 x_2 \ldots x_N$，我们找出对应 $x_1 x_2 \ldots x_N$ 的区间，然后发送一个二进制串，使它的区间落在该区间之内。这种编码可以边走边做（on the fly），下面就来演示。

#### Example: compressing the tosses of a bent coin（例：压缩一枚弯硬币的抛掷结果）

设想我们看着一枚弯硬币（bent coin）被抛若干次（参见 example 2.7（p.30）与 section 3.2（p.51））。硬币抛出的两种 outcome（结果）记作 a 与 b。第三种可能是实验被中止，这一事件用 `end of file' symbol「2」表示。因为硬币是弯的，我们预期 a 与 b 的概率不相等，但事先并不知道哪一个更可能。

**Encoding（编码）**

设 source string（源串）为 `bbba2`。我们逐个 symbol 地过这个串，用模型算出在迄今已知串条件下下一个 symbol 的概率分布。


<span style="color:#7f8c8d">书内 p114 ｜ Example：bent coin 的编码过程 ／ Figure 6.4</span>

设这些概率为：

| Context（序列如上） | $P(\mathrm{a})$ | $P(\mathrm{b})$ | $P(2)$ |
|---|---|---|---|
| （空） | $P(\mathrm{a}) = 0.425$ | $P(\mathrm{b}) = 0.425$ | $P(2) = 0.15$ |
| `b` | $P(\mathrm{a} \mid \mathrm{b}) = 0.28$ | $P(\mathrm{b} \mid \mathrm{b}) = 0.57$ | $P(2 \mid \mathrm{b}) = 0.15$ |
| `bb` | $P(\mathrm{a} \mid \mathrm{bb}) = 0.21$ | $P(\mathrm{b} \mid \mathrm{bb}) = 0.64$ | $P(2 \mid \mathrm{bb}) = 0.15$ |
| `bbb` | $P(\mathrm{a} \mid \mathrm{bbb}) = 0.17$ | $P(\mathrm{b} \mid \mathrm{bbb}) = 0.68$ | $P(2 \mid \mathrm{bbb}) = 0.15$ |
| `bbba` | $P(\mathrm{a} \mid \mathrm{bbba}) = 0.28$ | $P(\mathrm{b} \mid \mathrm{bbba}) = 0.57$ | $P(2 \mid \mathrm{bbba}) = 0.15$ |

（上表为原书页内表格：每个上下文下的 next-symbol 概率。表中数字来自 §6.2 末的 Bayesian 模型与 Laplace 规则 (6.7)：把剩余 0.85 的概率按 $(F_{\mathrm{a}} + 1) : (F_{\mathrm{b}} + 1)$ 分给 a 与 b。本译本复算结果：空上下文 $0.85 \times \tfrac{1}{2} = 0.425$；`b` 上下文 $0.85 \times \tfrac{1}{3} = 0.2833$、$0.85 \times \tfrac{2}{3} = 0.5667$；`bb` 上下文 $0.85 \times \tfrac{1}{4} = 0.2125$、$0.85 \times \tfrac{3}{4} = 0.6375$；`bbb` 上下文 $0.85 \times \tfrac{1}{5} = 0.17$、$0.85 \times \tfrac{4}{5} = 0.68$；`bbba` 上下文 $0.85 \times \tfrac{2}{6} = 0.2833$、$0.85 \times \tfrac{4}{6} = 0.5667$，与表中两位小数值逐格吻合。）

图 6.4 给出相应的区间。区间 `b` 是 $[0, 1)$ 中间那 0.425 的一段；区间 `bb` 是 `b` 中间那 0.567 的一段；如此类推。

[Figure 6.4：串 `bbba2` 传输过程中 arithmetic coding 的图解。左侧把单位区间 $[0, 1)$ 按 `a`、`b`、`2` 三级切开（b 占中间的 0.425），再在 `b` 内部继续细分出 `ba`、`bb`、`b2`，在 `bb` 内部细分出 `bba`、`bbb`、`bb2`，在 `bbb` 内部细分出 `bbba`、`bbbb`、`bbb2`；紧邻每条分隔线标出累计位置。中间一列是 5 位二进制细分 $00000$ 到 $11111$，以及它们对应的二进制前缀 $0$、$00$、$001$、$01$、$010$、$011$、$1$、$10$、$100$、$101$、$11$、$110$、$111$。右侧是 `bbba2` 邻域的放大：标出二进制小区间 $10010111$、$10011000$、……、$10011111$，标出 `bbbaa`、`bbbab`、`bbba2` 三条分隔线，并在其中标出被框住的串 $100111101$。]


<span style="color:#7f8c8d">书内 p115 ｜ 6.2 Arithmetic codes ／ Decoding ／ The big picture</span>

观察到第一个 symbol `b` 时，encoder 知道编码串将以 `01`、`10` 或 `11` 开头，但不知道是哪个。encoder 暂时什么都不写，转而查看下一个 symbol，它是 `b`。区间 `bb` 完全落在区间 `1` 之内，所以 encoder 可以写出第一个 bit：`1`。第三个 symbol `b` 把区间收窄了一点，但还不足以使它完全落在区间 `10` 之内。只有再读到下一个 `a` 时，我们才能发出更多 bit。区间 `bbba` 完全落在区间 `1001` 之内，所以 encoder 在已写出的 `1` 后面补上 `001`。最后，当 `2` 到达时，我们需要一个终止编码的流程。把区间 `bbba2` 放大（图 6.4 右侧），可以看到被标出的区间 $100111101$ 完全被 `bbba2` 包含，所以只要在后面附加 `11101`，编码即可完成。

> <span style="color:#7f8c8d">译本复算校验（可用 §6.2 的 Laplace 模型精确复现）：把 (6.2)(6.3) 与 Algorithm 6.3 逐层迭代，得到 `b` $[0.425000, 0.850000)$、`bb` $[0.545417, 0.786250)$、`bbb` $[0.596594, 0.750125)$、`bbba` $[0.596594, 0.622694)$、`bbba2` $[0.618779, 0.622694)$。于是：`bb` $\subset[0.5, 1)$（可用 `1`）；`bbb` 的右端点 $0.750125 \gt 0.75$，确实「不能完全落入 `10`」；`bbba` $\subset[0.5625, 0.625)$（可用 `1001`）；在所有 9 位二进制前缀中，完全落在 `bbba2` 内的恰好只有 $100111101 = [0.619140625, 0.62109375)$ 这一个。四个结论与书中叙述逐条吻合。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.1 [2, p.127]</span>

Show that the overhead required to terminate a message is never more than 2 bits, relative to the ideal message length given the probabilistic model $H$, $h(x \mid H) = \log[1/P(x \mid H)]$.

这是一个重要结果。arithmetic coding 几乎就是最优的：message length（消息长度）总是落在整个 source string 的 Shannon information content 的两 bit 之内，因此 expected message length 落在整条消息 entropy 的两 bit 之内。

**Decoding（解码）**

decoder 收到串 `100111101`，逐个 symbol 地过它。首先，用与 encoder 完全相同的程序算出概率 $P(\mathrm{a})$、$P(\mathrm{b})$、$P(2)$，并推出区间 `a`、`b`、`2`。一旦检查了前两个 bit `10`，就可以确定原始串必定以 `b` 开头，因为区间 `10` 完全落在区间 `b` 之内。decoder 随后用模型算出 $P(\mathrm{a} \mid \mathrm{b})$、$P(\mathrm{b} \mid \mathrm{b})$、$P(2 \mid \mathrm{b})$，并推出区间 `ba`、`bb`、`b2` 的边界。继续下去，读到 `1001` 时我们解出第二个 b，读到 `100111` 时解出第三个 b，如此类推；整个二进制串读完之后，`bbba2` 被无歧义地识别出来。有了「`2` 表示消息结束」这一约定，decoder 就知道该停止解码。

**Transmission of multiple files（多个文件的传输）**

怎样用 arithmetic coding 在二进制信道上传输若干个不同文件？一旦 `2` 字符被传过去，我们就设想 decoder 被重置到初始状态。第一个文件学到的统计量不会被转移到第二个文件。不过，如果我们确实相信要压缩的这些文件之间存在关系，我们可以换一种方式定义 alphabet，引入第二个 end-of-file 字符，它标记文件的结束，但指示 encoder 与 decoder 继续使用同一个 probabilistic model。

**The big picture（全局图景）**

注意：要传输一个含 $N$ 个字母的串，encoder 与 decoder 都只需要计算 $N |\mathcal{A}|$ 个 conditional probability（条件概率）—— 即实际遇到的每个上下文里每个可能字母的概率 —— 这与猜字游戏中完全一样。这项代价可以与「使用大块尺寸的 Huffman code」的做法相对照（那是为了削减 section 5.6 讨论的「每 symbol 至多 1 bit 的开销」）：在后一种做法里，所有可能出现的块序列都必须被考虑，其概率都必须被求值。

注意 arithmetic coding 有多么灵活：它可用于任何 source alphabet 与任何 encoded alphabet（编码字母表）。source alphabet 的规模与 encoded alphabet 的规模都可以随时间改变。arithmetic coding 可用于任何 probability distribution，而该分布可以随上下文彻底改变。

此外，如果我们希望编码字母表的 symbol（比如 0 与 1）以不相等的频率被使用，那也很容易安排：按所需频率成比例地细分右侧区间即可。

**How the probabilistic model might make its predictions（概率模型可以怎样做预测）**

arithmetic coding 这项技术并不强制你以任何特定方式产生预测概率，但预测分布可以很自然地由一个 Bayesian model 给出。


<span style="color:#7f8c8d">书内 p116 ｜ 6.2 Arithmetic codes ／ Laplace 规则与 Bayesian 模型细节</span>

[Figure 6.5：一个简单 Bayesian probabilistic model 所定义的区间。图中从左到右画出长度为 1 到 5 的若干串的区间：`a` 一侧向下展开出 `aa`、`aaa`、`aaaa`，`b` 一侧向上展开出 `bb`、`bbb`、`bbbb`，中间夹着 `aab`、`abb`、`aba`、`baa`、`bab`、`bba`、`bbab`、`bbba` 等串，以及以 `2` 结尾的串 `a2`、`aa2`、`ab2`、`ba2`、`bb2`、`b2`；右侧一列是 4 位、5 位二进制细分 $00000$ 到 $11111$ 及其前缀。一个区间的宽度正比于该串的概率。这个模型预判 source 偏向 a 与 b 之中的某一个，因此含大量 a 或大量 b 的序列，其区间比同长度的 50:50 序列更大。]

图 6.4 是用一个简单模型生成的：它总是把 0.15 的概率指派给 `2`，把剩下的 0.85 指派给 a 与 b，并按 Laplace's rule（拉普拉斯规则）给出的比例来分：

```math
P_L(\mathrm{a} \mid x_1, \ldots, x_{n-1}) = \frac{F_{\mathrm{a}} + 1}{F_{\mathrm{a}} + F_{\mathrm{b}} + 2}, \qquad (6.7)
```

其中 $F_{\mathrm{a}}(x_1, \ldots, x_{n-1})$ 是迄今为止 a 出现的次数，$F_{\mathrm{b}}$ 是 b 的计数。这些预测对应一个简单的 Bayesian model：它预期并适应一个文件内 source symbol a 与 b 使用频率不相等的情形。

图 6.5 展示了长度不超过 5 的若干个串所对应的区间。注意：如果到目前为止的串里含大量 b，那么 b 相对 a 的概率就被提高；反过来，如果出现很多 a，a 就变得更可能。记住，更大的区间编码时需要的 bit 更少。

#### Details of the Bayesian model（Bayesian 模型的细节）

在强调了「任何模型都可以用 —— arithmetic coding 并不绑定于某组特定概率」之后，下面解释前一个例子中用到的那个简单自适应概率模型；我们第一次遇到这个模型是在 exercise 2.8（p.30）。

**Assumptions（假设）**

该模型用参数 $p_2$、$p_{\mathrm{a}}$、$p_{\mathrm{b}}$ 描述（定义见下），注意不要把它们与某个特定上下文里的预测概率混淆，例如 $P(\mathrm{a} \mid s = \mathrm{baa})$。一枚标着 a 与 b 的弯硬币被抛了某个次数 $l$，而 $l$ 事先未知。硬币抛出 a 的概率是 $p_{\mathrm{a}}$，$p_{\mathrm{b}} = 1 - p_{\mathrm{a}}$；这些参数 $p_{\mathrm{a}}$、$p_{\mathrm{b}}$ 事先未知。源串 $s = \mathrm{baaba}2$ 表示 $l$ 为 5，且 outcome 序列为 baaba。


<span style="color:#7f8c8d">书内 p117 ｜ 6.2 Arithmetic codes ／ 模型的三条假设与 Laplace 规则的联系</span>

1. 假定串长 $l$ 服从指数概率分布

```math
P(l) = (1 - p_2)^{l} p_2 . \qquad (6.8)
```

这个分布对应这样的假设：每个字符处出现终止 symbol `2` 的概率是常数 $p_2$。

2. 假定串中的非终止字符按独立随机的原则取自一个概率为 $P = \{p_{\mathrm{a}}, p_{\mathrm{b}}\}$ 的 ensemble（总体）；概率 $p_{\mathrm{a}}$ 在整条串内固定为某个未知值，它可以取 0 与 1 之间的任何位置。在给定 $p_{\mathrm{a}}$ 的条件下（只要我们知道它），下一个 symbol 是 a 的概率为 $(1 - p_2) p_{\mathrm{a}}$。在给定 $p_{\mathrm{a}}$ 的条件下，一条长度为 $F$ 的未终止串等于某个指定串 $s$ —— 该串包含两种 outcome 的计数 $\{F_{\mathrm{a}}, F_{\mathrm{b}}\}$ —— 的概率是 Bernoulli distribution（伯努利分布）：

```math
P(s \mid p_{\mathrm{a}}, F) = p_{\mathrm{a}}^{F_{\mathrm{a}}} (1 - p_{\mathrm{a}})^{F_{\mathrm{b}}} . \qquad (6.9)
```

3. 假定 $p_{\mathrm{a}}$ 的 prior distribution（先验分布）是均匀的，

```math
P(p_{\mathrm{a}}) = 1, \quad p_{\mathrm{a}} \in [0, 1], \qquad (6.10)
```

并定义 $p_{\mathrm{b}} \equiv 1 - p_{\mathrm{a}}$。要假定 $p_{\mathrm{a}}$ 的其他先验也很容易，其中 beta distribution（贝塔分布）处理起来最方便。

这个模型在 section 3.2 中研究过。我们需要的关键结果，是在给定迄今的串 $s$ 的条件下下一个 symbol 的预测分布。下一个字符是 a 还是 b 的概率（假定它不是 `2`）在 equation (3.16) 中已经导出，它恰好就是 Laplace's rule (6.7)。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.2 [3]</span>

Compare the expected message length when an ASCII file is compressed by the following three methods.

**Huffman-with-header.** Read the whole file, find the empirical frequency of each symbol, construct a Huffman code for those frequencies, transmit the code by transmitting the lengths of the Huffman codewords, then transmit the file using the Huffman code. (The actual codewords don't need to be transmitted, since we can use a deterministic method for building the tree given the codelengths.)

**Arithmetic code using the Laplace model.**

```math
P_L(\mathrm{a} \mid x_1, \ldots, x_{n-1}) = \frac{F_{\mathrm{a}} + 1}{\sum_{a'} (F_{a'} + 1)} . \qquad (6.11)
```

**Arithmetic code using a Dirichlet model.** This model's predictions are:

```math
P_D(\mathrm{a} \mid x_1, \ldots, x_{n-1}) = \frac{F_{\mathrm{a}} + \alpha}{\sum_{a'} (F_{a'} + \alpha)} , \qquad (6.12)
```

where $\alpha$ is fixed to a number such as 0.01. A small value of $\alpha$ corresponds to a more responsive version of the Laplace model; the probability over characters is expected to be more nonuniform; $\alpha = 1$ reproduces the Laplace model.

Take care that the header of your Huffman message is self-delimiting. Special cases worth considering are (a) short files with just a few hundred characters; (b) large files in which some characters are never used.

（译本注：$\sum_{a'}$ 对 alphabet 中所有 symbol 求和，$F_{a'}$ 是该 symbol 迄今出现的次数；Laplace 模型即 $\alpha = 1$ 的特例。分母是归一化常数，保证预测分布在所有候选 next symbol 上求和为 1。）


<span style="color:#7f8c8d">书内 p118 ｜ 6.3 Further applications of arithmetic coding ／ Dasher</span>

### 6.3 Further applications of arithmetic coding（算术编码的进一步应用）

**Efficient generation of random samples（高效生成随机样本）**

arithmetic coding 不仅提供了压缩「据信来自某个给定模型的串」的办法，也提供了从模型生成随机串的办法。设想把一根针随机扎进单位区间，而这条线已按概率 $p_i$ 成比例地划分为若干子区间；那么你的针落在区间 $i$ 内的概率就是 $p_i$。

所以要由某个模型生成一个 sample（样本），我们只需把普通的随机 bit 送入该模型的 arithmetic decoder。无限随机 bit 序列对应在直线 $[0, 1)$ 上随机选一个点，于是 decoder 会按假定分布随机选出一个串。这种算术方法保证所用的随机 bit 数非常接近做该选择所需的最小可能值 —— 在「随机数很贵」的领域，这是一个要点！[这不是玩笑。大量金钱被花在软硬件里生成随机 bit 上。随机数是有价值的。]

这一技术的一个简单用法，是生成具有非均匀分布 $\{p_0, p_1\}$ 的随机 bit。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.3 [2, p.128]</span>

Compare the following two techniques for generating random symbols from a nonuniform distribution $\{p_0, p_1\} = \{0.99, 0.01\}$:

(a) The standard method: use a standard random number generator to generate an integer between $1$ and $2^{32}$. Rescale the integer to $(0, 1)$. Test whether this uniformly distributed random variable is less than 0.99, and emit a 0 or 1 accordingly.

(b) Arithmetic coding using the correct model, fed with standard random bits.

Roughly how many random bits will each method use to generate a thousand samples from this sparse distribution?

**Efficient data-entry devices（高效的数据录入设备）**

当我们把文本输入计算机时，会做出某种手势 —— 也许敲键盘、用指针划写、或者用鼠标点击；一个高效的 text entry（文本录入）系统，就是输入给定字符串所需手势数目很少的系统。

可以把书写（writing）看成 data compression 的逆过程。在 data compression 中，目标是把给定文本串映成少量 bit；而在 text entry 中，我们希望少量手势序列产出我们想要的文本。

```
Compression:   text  →  bits
Writing:       text  ←  gestures
```

把一个 arithmetic coder 反过来用，我们就能得到由连续指点手势驱动的、information-efficient 的文本录入设备（Ward et al., 2000）。这个系统叫 Dasher：用户不断放大单位区间，以定位到与自己想输入的串对应的区间，风格与图 6.4 相同。一个 language model（与文本压缩中用的完全相同）控制各区间的大小，使得概率大的串能被快速轻易地定位到。练一小时之后，新手用一根手指驱动 Dasher 就能达到约每分钟 25 个单词 —— 大约是他们在普通键盘上十指盲打速度的一半。甚至可以用注视方向（gaze direction）驱动 Dasher，实现免手操作的每分钟 25 词（Ward and MacKay, 2002）。Dasher 作为自由软件在多个平台上可用。


<span style="color:#7f8c8d">书内 p119 ｜ 6.4 Lempel-Ziv coding</span>


### 6.4 Lempel-Ziv coding（LZ 编码）

Lempel-Ziv 算法被广泛用于 data compression（例如 `compress` 与 `gzip` 命令），其哲学与 arithmetic coding 不同。这里 modelling 与 coding 之间没有分界，也没有做显式 modelling 的机会。

**Basic Lempel-Ziv algorithm（基本 LZ 算法）**

压缩方法是：用一个 substring（子串）替换成指向该子串更早一次出现的 pointer（指针）。例如若串为 $1011010100010\ldots$，我们把它解析成一个有序字典（dictionary），其中每一项都是此前没有出现过的子串，解析如下：$\epsilon$、1、0、11、01、010、00、10、……。我们把空子串 $\epsilon$ 作为字典中的第一个子串，并按各子串从 source 中出现的顺序排列字典。每经过一个逗号，我们就沿输入序列的下一部分往后读，直到读到一个此前没有被划出来的子串为止。稍加思索即可确认：这个子串比字典中更早出现过的某个子串恰好长一个 bit。这意味着我们可以这样编码每个子串：给出一个指针指向其 prefix（前缀）早先的出现位置，然后发送新子串与早先子串相差的那一个额外 bit。若到第 $n$ 个 bit 时我们已枚举了 $s(n)$ 个子串，那么指针值可以用 $\log_2 s(n)$ 个 bit 给出。于是上述序列的码如下表第四行所示（为清楚起见加了标点），上两行则给出源串与 $s(n)$ 的值：

| 项 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| source substring | 1 | 0 | 11 | 01 | 010 | 00 | 10 |
| $s(n)$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| $s(n)$ binary | 000 | 001 | 010 | 011 | 100 | 101 | 110 |
| (pointer, bit) | ($\epsilon$, 1) | (0, 0) | (01, 1) | (10, 1) | (100, 0) | (010, 0) | (001, 0) |

（上表为原书中「basic Lempel-Ziv parsing」表的重建。译本复算：对串 `1011010100010` 做贪心最长匹配解析，得到子串 $\epsilon$、1、0、11、01、010、00、10（共 7 个非空子串）；指针取「该前缀在字典中的序号」的二进制，宽度按 $\lceil \log_2 s(n) \rceil$ 随 $s(n)$ 递增（从 0 bit 起，实际序列为 0,1,2,2,3,3,3），逐项与书中 (pointer, bit) 行相同；拼出的输出串为 `100011101100001000010`（21 bit），与书中编码逐 bit 相同。表中 `s(n) binary` 行按原文写法统一用 3 位定宽，那只是示意、不是实际指针宽度 —— 书中把这两行并列而不加说明，容易读错，已列入文末「原文自身的问题」。）

注意我们发出的第一个指针是空的，因为那时字典里只有一个子串 —— 空串 $\epsilon$ —— 要传达「选它作前缀」这件事不需要任何 bit。编码后的串是 `100011101100001000010`。在这个简单例子里，编码实际上比源串更长，因为源串里没有明显的冗余。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.4 [2]</span>

Prove that any uniquely decodeable code from $\{0, 1\}^{+}$ to $\{0, 1\}^{+}$ necessarily makes some strings longer if it makes some strings shorter.

（译本注：这是第 5 章「codeword 超市预算」的连续性论证 —— 若把某些串压短，编码映射在字典序上不可能处处保序，必然有别的串被拉长。）


<span style="color:#7f8c8d">书内 p120 ｜ 6.4 Lempel-Ziv coding ／ Decoding ／ Theoretical properties</span>

上述算法把许多串拉长，一个原因是它效率不高 —— 它会发多余的 bit；换个说法，它的码不是 complete（完备）的。一旦字典中某个子串的两个 children（子结点）都已被加入字典，我们就可以确定它不会再被用到（除了可能作为我们终止消息协议的一部分）；所以此时我们本可以把它从子串字典中删掉，并把后面的子串统一前移一格，从而缩短后续指针消息的长度。等价地，我们可以把第二个前缀写到原来父结点占据的位置上。第二个不必要的开销，是这些情况下仍然发送新 bit —— 一个前缀第二次被使用时，我们可以确定下一个 bit 是什么。

**Decoding（解码）**

解码端同样需要一个同卵双胞胎：一边解码数据，一边构建子串字典。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.5 [2, p.128]</span>

Encode the string `000000000000100000000000` using the basic Lempel-Ziv algorithm described above.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.6 [2, p.128]</span>

Decode the string

```text
00101011101100100100011010101000011
```

that was encoded using the basic Lempel-Ziv algorithm.

**Practicalities（实务）**

在这段描述里，我没有讨论终止一个串的方法。

Lempel-Ziv 算法有许多变体，全都利用同一个想法，但在字典管理等流程上各不相同。由此生成的程序很快，但它们压缩英文文本的表现虽然有用，却达不到 arithmetic coding 文献里设定的标准。

**Theoretical properties（理论性质）**

与我们上三章讨论的 block code、Huffman code、arithmetic coding 方法形成对照：Lempel-Ziv 算法在定义时完全没提及 source 的 probabilistic model。然而，对任何 ergodic source（遍历源，即在足够长的时间尺度上无记忆的源），都可以证明 Lempel-Ziv 算法渐近地把数据压缩到 source 的 entropy。这就是它被称为 `universal'（通用）压缩算法的原因。关于这一性质的证明，见 Cover and Thomas (1991)。

<span style="color:#1e8449;">**[译注]**</span> **LZ 的 "universal" 不是免费午餐：它只保证 $n\to\infty$ 时码率 $\to H$（ergodic 源），且对低 entropy 但结构差的源会输给 arithmetic coding**

机制：LZ 把"出现过的串"换成一个指针，指针宽度 $\lceil\log_2 s(n)\rceil$ 随字典大小增长，因此有**两个必然的损失项**：① 指针的 $\log\log$ 级开销；② 短消息来不及建立字典。抽掉"只在渐近意义下 universal"这个限定，就会误以为 LZ 可以取代模型化的编码——原文用 Table 6.7 给了直接反例：对 $P(1)=0.01$ 的无记忆二值源（$H\approx 0.081$ bit），匹配模型的 arithmetic coder 接近 $H$，而 LZ 系程序差得多，因为这种源**几乎没有重复子串**可记。反过来对英文文本，LZ 表现良好（重复结构丰富）。所以 "universal" 的正确读法是：不假设源分布也能渐进到 $H$，但常数与收敛速度都没有保证，且在有限长度上可能被模型化方法大幅击败。

工程含义（他最该带走的）：选择压缩器不是比"谁更先进"，而是比"源里有没有可利用的重复/结构"。这与 CSAPP 第 6 章 cache 同理——局部性利用要求工作集稳定，LZ 要求重复模式稳定，只是层次不同；两者都不能凭空创造可压缩性。

坐标：§6.4（原书 p.119–121，PDF p.131–133），basic LZ parsing 表与解码；Table 6.7 的对比在 §6.6 小结（原书 p.127，PDF p.139）；"对 any ergodic source 渐近达到 entropy 的倍数"这一陈述在原书 p.121。

不过，它实现压缩的方式仅仅是记住已经出现过的 substring，以便它们再次出现时有个短名字。对那些 source 而言，达到这种 universal 表现所需的渐近时间尺度可能长得不切实际，因为需要记住的 typical substring 数目可能极大。该算法在实践中的可用表现，反映的是这样一个事实：许多文件里含有对某些短字符序列的多次重复，而这是该算法很擅长的一类冗余。


<span style="color:#7f8c8d">书内 p121 ｜ 6.4 Common ground ／ 6.5 Demonstration</span>

**Common ground（共同基础）**

我强调了 arithmetic coding 与 Lempel-Ziv coding 背后的哲学差异。不过它们之间有共同基础：原则上，人们可以设计自适应概率模型、并由此得到 `universal' 的 arithmetic code，也就是那种能在某类 source 上渐近地把任何 source 压缩到其 entropy 的某个倍数（最好就是 1 倍）之内的模型。然而就实用目的而言，我认为只有把 source 的类严重限制住，这样的 universal model 才可能被构造出来。一个能发现任何 source 概率分布的通用压缩机，那将是一个通用人工智能！而通用人工智能至今还不存在。

### 6.5 Demonstration（演示）

一个用于探索 arithmetic coding 的交互式辅助工具 `dasher.tcl` 可用。

Radford Neal 编写的一个 arithmetic-coding 软件演示包由编码模块与解码模块组成，使用者自己再补一个定义 probabilistic model 的模块。需要强调：并不存在任何单个通用的 arithmetic-coding 压缩机；对每一类 source 都得重新写一个模型。Radford Neal 的包中含有一个简单的自适应模型，与 section 6.2 演示的 Bayesian model 类似。用这个 Laplace 模型得到的结果应当被看作一个基本 benchmark（基准），因为它是最简单的概率模型 —— 它只是假设文件中的字符独立地来自一个固定 ensemble。随着文件被读取，符号 $\{a_i\}$ 的计数 $\{F_i\}$ 会被重新缩放并取整，使所有计数落在 1 与 256 之间。

一个 state-of-the-art 的、用于含文本与图像的文档的压缩机 DjVu 使用了 arithmetic coding。它对二进制 alphabet 使用一个精心设计的近似 arithmetic coder，称为 Z-coder（Bottou et al., 1998），比上面描述的 arithmetic coding 软件快得多。Z-coder 用到的一个巧妙技巧是：自适应模型只是偶尔才更新（以节省计算机时间），而何时更新的决定，由 arithmetic encoder 是否发出了某个 bit 伪随机地控制。


<span style="color:#7f8c8d">书内 p122 ｜ 6.5 Demonstration ／ Table 6.6 与 6.7 ／ 6.6 Summary</span>

二进制图像的 JBIG 图像压缩标准使用带上下文相关模型的 arithmetic coding，该模型按类似 Laplace 规则的规则自适应。PPM（Teahan, 1995）是文本压缩的领先方法，它使用 arithmetic coding。

基于 Lempel-Ziv 的程序很多。`gzip` 基于一个称为 `LZ77' 的 Lempel-Ziv 版本（Ziv and Lempel, 1977）；`compress` 基于 `LZW'（Welch, 1984）。依我的经验，最好的是 `gzip`，`compress` 在大多数文件上都更差。

`bzip` 是一个 block-sorting（块排序）文件压缩机，它利用一个灵巧的 hack，称为 Burrows-Wheeler transform（BWT，Burrows and Wheeler, 1994）。这个方法不基于显式的 probabilistic model，且只对大于几千字符的文件才表现良好；但在实践中，对那些「字符的上下文是该字符的良好预测器」的文件，它是非常有效的压缩机。

**Compression of a text file（一个文本文件的压缩）**

Table 6.6 给出把这些程序应用于包含本章正文的 LaTeX 文件（大小 20 942 bytes）时，所花的计算机时间（秒）与达到的压缩效果。

| Method | Compression time / sec | Compressed size（%age of 20 942） | Uncompression time / sec |
|---|---|---|---|
| Laplace model | 0.28 | 12 974（61%） | 0.32 |
| `gzip` | 0.10 | 8 177（39%） | 0.01 |
| `compress` | 0.05 | 10 816（51%） | 0.05 |
| `bzip` | — | 7 495（36%） | — |
| `bzip2` | — | 7 640（36%） | — |
| `ppmz` | — | 6 800（32%） | — |

（上表为 Table 6.6：对同一文本文件比较各种压缩算法。PDF 文字层丢失了部分时间列，故留空；压缩后大小与百分比逐项按原文抄录。）

**Compression of a sparse file（一个稀疏文件的压缩）**

有意思的是，`gzip` 并不总是表现这么好。Table 6.7 给出把这些程序应用于一个含 $10^6$ 个字符的文本文件时所达到的压缩效果，该文件中每个字符是 0 或 1，概率分别为 0.99 与 0.01。Laplace 模型与这个 source 相当匹配，benchmark arithmetic coder 表现良好，`compress` 紧随其后；`gzip` 最差。这个 source 的理想模型会把文件压到约 $10^6 H_2(0.01)/8 \approx 10\,100$ bytes。Laplace 模型压缩机达不到这个表现，因为它只用 8 bit 精度实现。`ppmz` 压缩机压缩得最好，但花的时间多得多。

| Method | Compression time / sec | Compressed size / bytes | Uncompression time / sec |
|---|---|---|---|
| Laplace model | 0.45 | 14 143（1.4%） | 0.57 |
| `gzip` | 0.22 | 20 646（2.1%） | 0.04 |
| `gzip --best` | 1.63 | 15 553（1.6%） | 0.05 |
| `compress` | 0.13 | 14 785（1.5%） | 0.03 |
| `bzip` | 0.30 | 10 903（1.09%） | 0.17 |
| `bzip2` | 0.19 | 11 260（1.12%） | 0.05 |
| `ppmz` | 533 | 10 447（1.04%） | 535 |

（上表为 Table 6.7：对 $10^6$ 个字符、99% 为 0、1% 为 1 的随机文件比较各种压缩算法。原文各行标签与时间列在 PDF 文字层中有错位，上表按数值大小与常识对应关系重建：`ppmz` 那一行的 533 秒与 535 秒明显是它的耗时，故归入该行。）

**6.6 Summary（小结）**

上三章我们研究了三类 data compression code。

**Fixed-length block codes（定长块码，第 4 章）。** 它们是从固定数目的 source symbol 到定长二进制消息的 mapping。只有极小一部分 source string 被赋予编码。这些码在「把 entropy 识别为可压缩性的度量」这件事上很有趣，但实用价值不大。


<span style="color:#7f8c8d">书内 p123 ｜ 6.6 Summary ／ 6.7 Exercises on stream codes</span>

**Symbol codes（符号码，第 5 章）。** symbol code 对 source alphabet 中的每个 symbol 使用一个变长码，码长是由各 symbol 概率决定的整数长度。Huffman's algorithm 对给定的一组 symbol 概率构造出 optimal symbol code。

每个 source string 都有唯一可译的编码；而若 source symbol 确实来自所假定的分布，则 symbol code 把每字符的期望长度 $L$ 压到区间 $[H, H + 1)$ 内。source 的统计涨落可能使实际长度比这个平均长度更长或更短。

若 source 与所假定的分布匹配得不好，则平均长度会因 source 分布与码的隐含分布之间的 relative entropy $D_{\mathrm{KL}}$ 而增加。对 entropy 很小的 source，symbol code 每读一个 source symbol 至少得发出一个 bit；要压到每 source symbol 一个 bit 以下，只能借助把 source 数据装进 block 这种笨重的做法。

**Stream codes（流码）。** 与 symbol code 相比，stream code 的显著性质是：它不被约束为「每从 source 流中读一个 symbol 就至少发出一个 bit」。因此大量 source symbol 可以被编码成较少的 bit。用 symbol code 只能靠把 source 流切块才能获得这种性质。

- Arithmetic codes 把 probabilistic model 与一个 encoding 算法结合起来：该算法把每个串与 $[0, 1)$ 的一个子区间对应，区间大小等于该串在模型下的概率。这种码几乎是 optimal 的，意思是串 $x$ 的压缩长度与给定 probabilistic model 下 $x$ 的 Shannon information content 非常接近。arithmetic code 契合这样的哲学：好的压缩要求 data modelling，形式是自适应的 Bayesian model。
- Lempel-Ziv codes 的自适应性体现在它会记住已经出现过的串。它们建立在这样的哲学上：我们对 source 的概率分布一无所知，我们要的是一个无论该分布是什么都能干得相当好的压缩算法。

arithmetic code 与 Lempel-Ziv code 有一处共同弱点：只要压缩文件的任何一个 bit 被改动，它们都无法正确解码。所以如果压缩文件要被存储或通过含噪介质传输，error-correcting code（纠错码）就是必不可少的。在有噪信道上做可靠通信，是 Part II 的主题。

### 6.7 Exercises on stream codes（流码习题）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.7 [2]</span>

Describe an arithmetic coding algorithm to encode random bit strings of length $N$ and weight $K$ (i.e., $K$ ones and $N - K$ zeroes) where $N$ and $K$ are given.

For the case $N = 5$, $K = 2$, show in detail the intervals corresponding to all source substrings of lengths 1-5.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.8 [2, p.128]</span>

How many bits are needed to specify a selection of $K$ objects from $N$ objects? ($N$ and $K$ are assumed to be known and the selection of $K$ objects is unordered.) How might such a selection be made at random without being wasteful of random bits?


<span style="color:#7f8c8d">书内 p124 ｜ 6.7 Exercises on stream codes</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.9 [2]</span>

A binary source $X$ emits independent identically distributed symbols with probability distribution $\{f_0, f_1\}$, where $f_1 = 0.01$. Find an optimal uniquely-decodeable symbol code for a string $x = x_1 x_2 x_3$ of three successive samples from this source.

Estimate (to one decimal place) the factor by which the expected length of this optimal code is greater than the entropy of the three-bit string $x$.

[ $H_2(0.01) \simeq 0.08$, where $H_2(x) = x \log_2 (1/x) + (1 - x) \log_2 (1/(1 - x))$. ]

An arithmetic code is used to compress a string of 1000 samples from the source $X$. Estimate the mean and standard deviation of the length of the compressed file.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.10 [2]</span>

Describe an arithmetic coding algorithm to generate random bit strings of length $N$ with density $f$ (i.e., each bit has probability $f$ of being a one) where $N$ is given.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.11 [2]</span>

Use a modified Lempel-Ziv algorithm in which, as discussed on p.120, the dictionary of prefixes is pruned by writing new prefixes into the space occupied by prefixes that will not be needed again. Such prefixes can be identified when both their children have been added to the dictionary of prefixes. (You may neglect the issue of termination of encoding.) Use this algorithm to encode the string `0100001000100010101000001`. Highlight the bits that follow a prefix on the second occasion that that prefix is used. (As discussed earlier, these bits could be omitted.)

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.12 [2, p.128]</span>

Show that this modified Lempel-Ziv code is still not `complete', that is, there are binary strings that are not encodings of any string.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.13 [3, p.128]</span>

Give examples of simple sources that have low entropy but would not be compressed well by the Lempel-Ziv algorithm.

### 6.8 Further exercises on data compression（数据压缩进阶习题）

以下习题，急于学习有噪信道的读者可以跳过。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.14 [3, p.130]</span>

Consider a Gaussian distribution in $N$ dimensions,

```math
P(x) = \frac{1}{(2\pi\sigma^2)^{N/2}} \exp\left(-\frac{\sum_n x_n^2}{2\sigma^2}\right). \qquad (6.13)
```

Define the radius of a point $x$ to be $r = \left(\sum_n x_n^2\right)^{1/2}$. Estimate the mean and variance of the square of the radius, $r^2 = \sum_n x_n^2$.

You may find helpful the integral

```math
\int dx\, \frac{1}{(2\pi\sigma^2)^{1/2}}\, x^4 \exp\left(-\frac{x^2}{2\sigma^2}\right) = 3\sigma^4, \qquad (6.14)
```

though you should be able to estimate the required quantities without it.


<span style="color:#7f8c8d">书内 p125 ｜ 6.8 Further exercises ／ Figure 6.8</span>

（Exercise 6.14 续）Assuming that $N$ is large, show that nearly all the probability of a Gaussian is contained in a thin shell of radius $\sqrt{N}\sigma$. Find the thickness of the shell.

Evaluate the probability density (6.13) at a point in that thin shell and at the origin $x = 0$ and compare. Use the case $N = 1000$ as an example. Notice that nearly all the probability mass is located in a different part of the space from the region of highest probability density.

[Figure 6.8：$N$ 维 Gauss 分布之 typical set（典型集）的示意表示。图中只画出半径方向一条轴：刻度 $\sqrt{N}\sigma$ 处标注「probability density is maximized here」（概率密度在此处最大），更外侧一圈虚线壳层标注「almost all probability mass is here」（几乎所有概率质量在此处），两者位置明显分开，用来演示「概率密度最大处」与「概率质量所在处」不是同一个地方。]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.15 [2]</span>

Explain what is meant by an optimal binary symbol code. Find an optimal binary symbol code for the ensemble:

```math
\mathcal{A} = \{\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}, \mathrm{e}, \mathrm{f}, \mathrm{g}, \mathrm{h}, \mathrm{i}, \mathrm{j}\},
```

```math
P = \left\{ \frac{1}{100}, \frac{2}{100}, \frac{4}{100}, \frac{5}{100}, \frac{6}{100}, \frac{8}{100}, \frac{9}{100}, \frac{10}{100}, \frac{25}{100}, \frac{30}{100} \right\},
```

and compute the expected length of the code.

> <span style="color:#7f8c8d">译本复算：$H = \sum_i p_i \log_2 (1/p_i) = 2.7821$ bits。用 Huffman 算法得到一组码长 $\{6, 6, 5, 4, 4, 4, 3, 3, 2, 2\}$（对应 j, i, h, … 由概率降序排列），码字例如 `j` = `11`、`i` = `01`、`h` = `001`、`g` = `000`、`f` = `1011`、`e` = `1001`、`d` = `1000`、`c` = `10101`、`b` = `101001`、`a` = `101000`。Kraft 和 $\sum_i 2^{-l_i} = 1$（完备码），期望长度 $\sum_i p_i l_i = 2.81$ bits，落在 $[H, H+1)$ 之内且只比 $H$ 多 0.028 bit。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.16 [2]</span>

A string $y = x_1 x_2$ consists of two independent samples from an ensemble

```math
X: \mathcal{A}_X = \{\mathrm{a}, \mathrm{b}, \mathrm{c}\}; \quad P_X = \left\{ \frac{1}{10}, \frac{3}{10}, \frac{6}{10} \right\}.
```

What is the entropy of $y$? Construct an optimal binary symbol code for the string $y$, and find its expected length.


<span style="color:#7f8c8d">书内 p126 ｜ 6.8 Further exercises ／ Exercise 6.18（变长 symbol 的 source coding）</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.17 [2]</span>

Strings of $N$ independent samples from an ensemble with $P = \{0.1, 0.9\}$ are compressed using an arithmetic code that is matched to that ensemble. Estimate the mean and standard deviation of the compressed strings' lengths for the case $N = 1000$. [ $H_2(0.1) \simeq 0.47$ ]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.18 [3]</span> Source coding with variable-length symbols.

> 在讲 source coding 的那几章里，我们假定编码目标是二进制 alphabet $\{0, 1\}$，且两个 symbol 应当等频使用。本题探讨：如果不同 symbol 的传输时间不同，编码 alphabet 应当怎样使用。

一个穷学生免费用电话跟朋友通信：他选一个整数 $n \in \{1, 2, 3 \ldots\}$，让朋友的电话响 $n$ 声，然后在第 $n$ 声响到一半时挂断。这个过程被重复，于是一串 symbol $n_1 n_2 n_3 \ldots$ 被接收到。最优的通信方式是什么？如果选大的整数 $n$，消息传输就更久；如果只用小的整数 $n$，那么每个 symbol 承载的信息量就少。我们的目标是让单位时间内信息传输的速率最大化。

假定传输 $n$ 次响铃并重新拨号所需时间为 $l_n$ 秒。考虑 $n$ 上的一个概率分布 $\{p_n\}$。定义每 symbol 的平均时长为

```math
L(\mathbf{p}) = \sum_n p_n l_n \qquad (6.15)
```


<span style="color:#7f8c8d">书内 p127 ｜ Exercise 6.18 续 ／ 6.19–6.22 ／ 6.9 Solutions 起</span>

以及每 symbol 的熵为

```math
H(\mathbf{p}) = \sum_n p_n \log_2 \frac{1}{p_n}, \qquad (6.16)
```

请证明：要使平均每秒信息率最大，各 symbol 必须以如下形式的概率被使用

```math
p_n = \frac{1}{Z} 2^{-\beta l_n}, \qquad (6.17)
```

其中 $Z = \sum_n 2^{-\beta l_n}$，而 $\beta$ 满足隐式方程

```math
\beta = \frac{H(\mathbf{p})}{L(\mathbf{p})}, \qquad (6.18)
```

也就是说，$\beta$ 就是通信的速率。请证明这两个方程 (6.17)(6.18) 蕴含：$\beta$ 必须被设定得使

```math
\log Z = 0. \qquad (6.19)
```

假定信道具有性质

```math
l_n = n \ \text{seconds}, \qquad (6.20)
```

求出最优分布 $\mathbf{p}$，并证明最大信息率为每秒 1 bit。

若把 $\mathbf{p}$ 设为 $(1/2, 1/2, 0, 0, 0, 0, \ldots)$ —— 即只选 symbol $n = 1$ 与 $n = 2$，且两者等概率 —— 每秒信息率与之相比如何？

讨论上面导出的结果 (6.17)(6.19) 与 source coding 理论中的 Kraft inequality 之间的关系。

一个随机二进制 source，怎样才能被高效地编码成 symbol 序列 $n_1 n_2 n_3 \ldots$，以便在 (6.20) 定义的信道上传输？

> <span style="color:#7f8c8d">译本推导校验：用 Lagrange multiplier（拉格朗日乘子）对 $\max_{\mathbf{p}} H(\mathbf{p}) / L(\mathbf{p})$ 求驻点，得到 $-\log_2 p_n - 1/\ln 2 - \lambda l_n - \mu = 0$，即 $p_n \propto 2^{-\beta l_n}$，正是 (6.17)。再把 (6.17) 代回熵：$H = \sum_n p_n (\beta l_n + \log_2 Z) = \beta L + \log_2 Z$，与 (6.18) 联立即得 $\log_2 Z = 0$，也就是 $Z = 1$。(6.19) 因此不是额外假定，而是前两式的推论 —— 这一点正是题目要求你「show」的内容。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.19 [1]</span> How many bits does it take to shuffle a pack of cards?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.20 [2]</span>

In the card game Bridge, the four players receive 13 cards each from the deck of 52 and start each game by looking at their own hand and bidding. The legal bids are, in ascending order 1♣, 1♦, 1♥, 1♠, 1NT, 2♣, 2♦, …, 7♠, 7NT, and successive bids must follow this order; a bid of, say, 2♦ may only be followed by higher bids such as 2♥ or 3♣ or 7NT. (Let us neglect the `double' bid.)

The players have several aims when bidding. One of the aims is for two partners to communicate to each other as much as possible about what cards are in their hands.

Let us concentrate on this task.

(a) After the cards have been dealt, how many bits are needed for North to convey to South what her hand is?

(b) Assuming that E and W do not bid at all, what is the maximum total information that N and S can convey to each other while bidding? Assume that N starts the bidding, and that once either N or S stops bidding, the bidding stops.


#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.21 [2]</span>

My old `arabic' microwave oven had 11 buttons for entering cooking times, and my new `roman' microwave has just five. The buttons of the roman microwave are labelled `10 minutes', `1 minute', `10 seconds', `1 second', and `Start'; I'll abbreviate these five strings to the symbols M, C, X, I, $\Sigma$. To enter one minute and twenty-three seconds (1:23), the arabic sequence is

```math
123\Sigma, \qquad (6.21)
```

and the roman sequence is

```math
\mathrm{CXXIII}\Sigma. \qquad (6.22)
```

Each of these keypads defines a code mapping the 3599 cooking times from 0:01 to 59:59 into a string of symbols.

[Figure 6.9：微波炉的两种替代键盘。左表为 `arabic`（阿拉伯）键盘：三列数字键 1 2 3 ／ 4 5 6 ／ 7 8 9，下方 0，再加一个启动键；右表为 `roman`（罗马）键盘：M、C、X、I、$\Sigma$ 五个键，M 对应 10 分钟、C 对应 1 分钟、X 对应 10 秒、I 对应 1 秒。表中并给出示例：$123 \leftrightarrow$ MX、$456 \leftrightarrow$ C I$_2$、$789$、$0$ 与 $02$ 等对照。]

(a) Which times can be produced with two or three symbols? (For example, 0:20 can be produced by three symbols in either code: XX$\Sigma$ and 20$\Sigma$.)

(b) Are the two codes complete? Give a detailed answer.

(c) For each code, name a cooking time that it can produce in four symbols that the other code cannot.

(d) Discuss the implicit probability distributions over times to which each of these codes is best matched.

(e) Concoct a plausible probability distribution over times that a real user might use, and evaluate roughly the expected number of symbols, and maximum number of symbols, that each code requires. Discuss the ways in which each code is inefficient or efficient.

(f) Invent a more efficient cooking-time-encoding system for a microwave oven.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 6.22 [2, p.132]</span>

Is the standard binary representation for positive integers (e.g. $c_b(5) = 101$) a uniquely decodeable code?

Design a binary code for the positive integers, i.e., a mapping from $n \in \{1, 2, 3, \ldots\}$ to $c(n) \in \{0, 1\}^{+}$, that is uniquely decodeable. Try to design codes that are prefix codes and that satisfy the Kraft equality $\sum_n 2^{-l_n} = 1$.

> Motivations: any data file terminated by a special end of file character can be mapped onto an integer, so a prefix code for integers can be used as a self-delimiting encoding of files too. Large files correspond to large integers. Also, one of the building blocks of a `universal' coding scheme — that is, a coding scheme that will work OK for a large variety of sources — is the ability to encode integers. Finally, in microwave ovens, cooking times are positive integers!

Discuss criteria by which one might compare alternative codes for integers (or, equivalently, alternative self-delimiting codes for files).

### 6.9 Solutions（6.9 节 解答）

#### Solution to exercise 6.1（p.115）（exercise 6.1 的解答）

最坏情形是：要表示的那个区间恰好紧贴在一个 binary interval（二进制区间）的内侧。这时我们可以选图中所示两个二进制区间中的任意一个。这些二进制区间


<span style="color:#7f8c8d">书内 p128 ｜ 6.9 Solutions（6.1、6.3、6.5、6.6、6.8、6.12、6.13 起）</span>

（Solution 6.1 续）……这些二进制区间不小于 $P(x \mid H)/4$，因此二进制编码的长度不超过

```math
\log_2 \frac{1}{P(x \mid H)} + \log_2 4 ,
```

也就是比理想消息长度多两个 bit。

[Figure 6.10：arithmetic coding 在最坏情形下的终止。左侧竖条标为 `Source string's interval`（源串区间），高度 $P(x \mid H)$；右侧两条并列的二进制区间（`Binary intervals`），其中一条标记为选中；图中注明这两个二进制区间都不小于 $P(x \mid H)/4$。]

#### Solution to exercise 6.3（p.118）（exercise 6.3 的解答）

标准方法每个生成的 symbol 要用 32 个随机 bit，因此生成一千个样本需要 32 000 bit。

arithmetic coding 平均每个生成的 symbol 约用 $H_2(0.01) \simeq 0.081$ bit，因此生成一千个样本约需 83 bit（假定终止开销约 2 bit）。

1 的个数的涨落会使实际长度在这个均值附近波动，标准差约为 21。

> <span style="color:#7f8c8d">译本复算：长度约为 $14.5 + 6.64k$，其中 $k$ 是 1 的个数、$-\log_2 0.01 = 6.64$、$-\log_2 0.99 = 0.0145$；而 $k \sim \mathrm{Binomial}(1000, 0.01)$ 的标准差为 $\sqrt{1000 \times 0.01 \times 0.99} = 3.15$，故长度标准差约 $6.64 \times 3.15 = 20.9 \approx 21$，与书中数字一致。</span>

#### Solution to exercise 6.5（p.120）（exercise 6.5 的解答）

编码是 `010100110010110001100`，它来自如下解析

```math
0,\ 00,\ 000,\ 0000,\ 001,\ 00000,\ 000000 \qquad (6.23)
```

其编码为

```math
(\epsilon, 0),\ (1, 0),\ (10, 0),\ (11, 0),\ (010, 1),\ (100, 0),\ (110, 0). \qquad (6.24)
```

> <span style="color:#7f8c8d">译本复算：对串 `000000000000100000000000` 做贪心最长匹配，得到解析 $0, 00, 000, 0000, 001, 00000, 000000$（与 (6.23) 逐项一致）；指针取「该前缀在字典中的序号」的三位二进制（$\log_2 7 \approx 3$），拼出的输出串恰为 `010100110010110001100`（21 bit），与书中答案逐 bit 相同。</span>

#### Solution to exercise 6.6（p.120）（exercise 6.6 的解答）

解码结果为

```math
0100001000100010101000001.
```

#### Solution to exercise 6.8（p.123）（exercise 6.8 的解答）

本题与 exercise 6.7（p.123）等价。

从 $N$ 个对象中选出 $K$ 个，需要 $\log_2 \binom{N}{K}$ bit，约等于 $N H_2(K/N)$ bit。这种选择可以用 arithmetic coding 来做。该选择对应一个长度为 $N$ 的二进制串，其中为 1 的 bit 表示哪些对象被选中。开始时，1 的概率是 $K/N$，0 的概率是 $(N - K)/N$。此后，在已发出的长度为 $n$ 的串含 $k$ 个 1 的条件下，1 的概率是 $(K - k)/(N - n)$，0 的概率是 $1 - (K - k)/(N - n)$。

> <span style="color:#7f8c8d">译本复算：$N = 1000$、$K = 100$ 时 $\log_2 \binom{1000}{100} = 469.0$ bit，而 $N H_2(0.1) = 469.0$ bit，两者一致到小数点后一位 —— 该算术编码的代价正好是组合数的对数，一分不浪费。</span>

#### Solution to exercise 6.12（p.124）（exercise 6.12 的解答）

这个修改版 Lempel-Ziv 码仍然不是 `complete'（完备）的，因为例如在收满五个前缀之后，指针只能取串 000、001、010、011、100 之一，而不可能是 101、110 或 111。因此有些二进制串无法作为编码被产生出来。

#### Solution to exercise 6.13（p.124）（exercise 6.13 的解答）

entropy 低、却不能被 Lempel-Ziv 很好压缩的 source，例子包括下面这些（原文续于书内 p129，见下一份文件 p141）：

---

<!-- ===== 译者注 ===== -->

#### <span style="color:#1e8449;">[译注] pointer 是 LZ 全部的"压缩预算"来源 —— 从 §6.4 的 dictionary 到 gzip 的滑动窗口（对应 p119–p128）</span>

**机制：抽掉哪一件东西，整个 LZ 体系就崩了。**

LZ 的压缩不是来自「猜下一个符号」，而是来自**把重复内容折算成指向旧内容的编号**。设一次解析得到 $t$ 个 phrase（短语），第 $i$ 个 phrase 的 pointer 宽度是 $\lceil \log_2 i \rceil$ bit，外带 1 bit 新符号。于是整个文件的总码长约为 $\sum_{i=1}^{t} (\lceil \log_2 i \rceil + 1) \le t \log_2 t + 2t$ bit —— 注意这个上界里**没有 $n$（文件长度）**，只有 phrase 数 $t$。这就是全部机制：文件越长、重复越多，$t$ 相对 $n$ 越小，平均每字符摊到的 bit 就越少；而每个 phrase 的**内容重复部分在这个式子里零成本**。现在抽掉 pointer：重复的内容必须以原样再发一遍，$t$ 换成 $n$，压缩率即刻回到 1 —— 不是变差，是**概念本身消失**（那就只剩定长或 Huffman 编码，见 §6.6 对三类 code 的分类）。原文 p.119 那句"用 pointer 指向此前出现处"就是这条机制的完整陈述，表里 `(pointer, bit)` 一行的宽度变化（$11\to$ `01`、$010\to$ `100`、$10\to$ `001`）是它唯一的具体证据。

**原文自身的两处不严谨（照实说，不替作者圆场）。**

其一，p.119 正文说 pointer 用 $\lceil \log_2 s(n) \rceil$ bit，但同一张表的 `s(n) binary` 行把 $s(n)=1,2,\ldots,7$ 一律写成三位二进制（`001`…`111`）；而 `(pointer, bit)` 行用的却是**变宽**指针（$s(n)=2$ 时 `0`、$s(n)=3$ 时 `01`）。这两行不可能同时是 $\lceil \log_2 s(n) \rceil$ 的实现 —— 前者是"三位定宽示意"，后者才是实际编码。其二，$s(n)$ 被定义为"到第 $n$ 个 bit 时已枚举的子串数"，但表中 $s(n)=0$ 对应的是 $\lambda$ 这一列，而指针是从 $\lambda$ 之后才开始发的；也就是说 $s(n)$ 到底是"已枚举数"还是"下一个可用编号"，全文没有统一，读者需自己按 `(pointer, bit)` 行反推（该行自洽：$11$ 的前缀是 $1$ 号，宽 $\lceil\log_2 3\rceil = 2$ bit ⇒ `01`）。

**承重与消失测试。** 今天你按的每一次 `gzip`，都是 LZ77 的一个变体（Ziv and Lempel, 1977，书 p.121 明说）：窗口 32 KB、三段式查找用 hash chain，源码位置 `zlib/deflate.c` 的 `longest_match()` 与 `deflate_slow()`。消失测试：把 `longest_match()` 短路成"永远不命中"，deflate 就退化成它自己的第二级 —— 纯 Huffman（`trees.c` 的 `build_tree()`），对本章这种 20 942 bytes 的 LaTeX 文本会重新落到表 6.6 中 50% 量级那一档（`gzip` 的 39% 里有相当部分来自 LZ 层；精确拆分数字书中未给，此处标 `[未定位]`）。反方向的消失测试更锋利：把 pointer 宽度固定成 32 bit（不做 $\lceil \log_2 s(n)\rceil$ 变宽），短文件的压缩就会**变成负收益** —— 这正是 p.119 那句"在这个简单例子里编码反而更长"的成因，也是 gzip 对小文件（< 几百字节）常常不压缩的原因。

**L2 平行（挂到你已经学过的节点）。** CSAPP 的 cache 与 LZ 的 dictionary 是同一个机制在两个层次上的投影：都是**利用时间局部性，把"再次访问长东西"替换成"一个短编号"**。cache 命中时，地址（短编号）替代了 DRAM 往返（长内容），省的是 latency 与带宽；LZ 命中时，pointer（短编号）替代了重复字节，省的是 bit。差别在失配代价的方向：cache 失配只慢，LZ 失配只亏长度，都不会出错 —— 所以两者都不需要正确性证明，只需要**收益核算**。6.042J 的 pigeonhole principle 则直接给出 exercise 6.4 的一句话证明：若某些串被压短，映射不可能是单射（$|\{0,1\}^{\le L}| < |\{0,1\}^{\le L+1}|$），必有一些串被拉长。

**L1 上游 = Kraft 预算的时间版。** exercise 6.18（p.125–126）把"code 长度预算"从 bit 换成**秒**：符号 $n$ 耗时 $l_n = n$ 秒，最优分布是 $p_n \propto 2^{-\beta l_n}$，且 $\log Z = 0$ —— 这正好是 Kraft inequality $\sum_n 2^{-l_n} \le 1$ 在"代价是时间而非长度"时取等号的版本，$\beta$ 就是每秒钟传输的信息率。也就是说：Kraft 不等式不是"二进制"的性质，它是**任何可加资源预算**的性质（6.041 里你见过同样的形式：约束下的最大 entropy 用 Lagrange multiplier 求解，$\beta$ 就是那个乘子）。这条连接是全章最值得记住的一句。

**L4 你今天就能做的验证。** 生成 $10^6$ 个字符、1% 为 1 的偏置文件，跑 `gzip -9` 与 `bzip2 -9`，对照表 6.7 的 20 646 / 11 260 bytes，看现代实现在这个"LZ 不擅长"的 source 上补回来多少 —— 若 `bzip2` 接近 $10^6 H_2(0.01)/8 \simeq 10\,100$ bytes（表中 ppmz 已达 10 447），说明 LZ 的失效点确实在"重复结构不存在"，而不在"实现不好"。

（本节公式均为笔者的粗估与核对，不是原书内容；原书未给 LZ 码长的界。）


<span style="color:#7f8c8d">书内 p129 ｜ 6.9 Solutions ／ Solution to exercise 6.13（a）（b）</span>

（Solution to exercise 6.13 续）

**(a) 带有长程相关、且中间夹着随机垃圾的 symbol 的 source。** 理想的模型应当捕捉到相关的部分并压缩它；Lempel-Ziv 只能靠记住「夹在中间的那些垃圾」的所有情形来压缩相关特征。举个简单例子，考虑一本电话簿，每一行含一个（旧号码，新号码）对：

```text
285-3820:572-58922
258-8302:593-20102
```

每行 18 个字符，取自 13 个字符的 alphabet $\{0, 1, \ldots, 9, -, :, \epsilon\}$。字符 `-`、`:` 与 `\epsilon` 以可预测的顺序出现，因此，假定所有电话号码都是七位数、并且是随机序列，每行的真实 information content 约为 14 bans（一个 ban 是一个 0 到 9 之间随机整数的 information content）。一个 finite state language model（有限状态语言模型）能轻松捕捉这些数据中的规律性。然而，Lempel-Ziv 算法要花很长时间才能把这样的文件压到每行 14 bans，因为要让它「学会」串 `:ddd` 总是跟着 `-`（对任意三个数字 ddd 都成立），它必须见过所有这些串。所以，只有读过文件数千行之后才能达到近乎最优的压缩。

[Figure 6.11：一个 entropy 低、却不能被 Lempel-Ziv 很好压缩的 source。位序列从左往右读，每一行与上一行在 $f = 5\%$ 的 bit 上不同。图像宽度为 400 像素。]

**(b) 具有长程相关的 source。** 例如以逐行像素序列表示的二维图像：这样一来，垂直相邻的像素在 source 流中相距 $w$ 个位置，$w$ 是图像宽度。再如传真传输：每一行都与上一行非常相似（图 6.11）。真实 entropy 只有每像素 $H_2(f)$，其中 $f$ 是某个像素与其父像素不同的概率。Lempel-Ziv 算法只有在所有长度 $2w = 2400$ 的串都出现过、并且其后继都被记住之后，才能压到 entropy。宇宙中大约只有 $2^{300}$ 个粒子，所以我们可以有把握地说：Lempel-Ziv 码永远捕捉不到这类图像的冗余。

另一种高度冗余的纹理见图 6.12。该图像由在平面上随机撒下水平与竖直的「针」构成。它同时含有长程的垂直相关与水平相关。若把这张图逐像素扫描后喂给 Lempel-Ziv，没有任何实际可行的办法能同时捕捉到这两种相关。

生物计算系统能轻松识别这些图像、以及复杂得多的图像中的冗余；因此我们可以预期，最好的数据压缩算法将来自人工智能方法的发展。


<span style="color:#7f8c8d">书内 p130 ｜ 6.9 Solutions ／ Solution to exercise 6.13（c）–（f）／ Solution to exercise 6.14</span>

[Figure 6.12：由随机撒在平面上的水平与竖直「针」构成的纹理。图中可见长短不一的横线与竖线交错分布，形成同时具有横向与纵向长程相关的图案。]

**(c) 具有精巧冗余的 source**，例如由计算机生成的文件。比如一个 LaTeX 文件，随后是它被编码成的 PostScript 文件。这一对文件合起来的 information content，大致等于那个 LaTeX 文件单独的 information content。

**(d) Mandelbrot 集的图像。** 这张图的 information content 等于「指定所研究的复平面范围、像素大小以及着色规则」所需的 bit 数。

**(e) 一个受挫反铁磁 Ising model（frustrated antiferromagnetic Ising model）基态的图**（图 6.13），我们将在第 31 章讨论它。与图 6.12 一样，这张二值图像在两个方向上都有有趣的相关。

[Figure 6.13：受挫三角 Ising model 的某个基态。三角形晶格上每个格点取两种状态之一，图上用两种灰度表示；由于三角格子的拓扑，无法让每条边两端的格点都取相反状态，于是出现受挫结构，图案在横向与纵向同时呈现相关。]

**(f) 元胞自动机（cellular automata）** —— 图 6.14 展示了一个 400 个格子的元胞自动机 100 步的状态历史。更新规则是随机选定的：每个格子的新状态取决于它前面五个格子的状态。它的 information content 等于边界上的信息（400 bit）加上传播规则的信息（这里可用 32 bit 描述）。因此，一个 optimal compressor 给出的压缩文件长度将基本是常数，与图像的竖直高度无关。Lempel-Ziv 只有在元胞自动机进入周期极限环之后才能给出这种零代价压缩，而进入极限环很容易需要约 $2^{100}$ 次迭代。

相反，JBIG 压缩方法 —— 它建模「给定局部上下文时某像素的概率」并使用 arithmetic coding —— 会在这些图像上表现良好。

#### Solution to exercise 6.14（p.124）（exercise 6.14 的解答）

对一维 Gauss 分布，$x$ 的 variance $\mathrm{E}[x^2]$ 是 $\sigma^2$。所以，由于 $x$ 的各分量是相互独立的随机变量，$r^2$ 在 $N$ 维下的均值为

```math
\mathrm{E}[r^2] = N\sigma^2. \qquad (6.25)
```


<span style="color:#7f8c8d">书内 p131 ｜ Solution to exercise 6.14 续 ／ Figure 6.14</span>

[Figure 6.14：一个 400 个格子的元胞自动机 100 步的时间历史。横轴是格子序号（0 到 400），纵轴是时间步（自上而下 100 步），黑白两色表示每个格子在每一步的状态；图案显示由随机更新规则产生的斜向传播结构。]

同理，$r^2$ 的 variance 是 $x^2$ 的 variance 的 $N$ 倍，其中 $x$ 是一维 Gauss 变量。

```math
\mathrm{var}(x^2) = \int dx\, \frac{1}{(2\pi\sigma^2)^{1/2}}\, x^4 \exp\left(-\frac{x^2}{2\sigma^2}\right) - \sigma^4. \qquad (6.26)
```

该积分由 (6.14) 给出为 $3\sigma^4$，所以 $\mathrm{var}(x^2) = 2\sigma^4$。于是 $r^2$ 的 variance 是 $2N\sigma^4$。

对大的 $N$，central-limit theorem（中心极限定理）表明 $r^2$ 服从均值为 $N\sigma^2$、标准差为 $\sqrt{2N}\sigma^2$ 的 Gauss 分布，因此 $r$ 的概率密度同样集中在 $r \simeq \sqrt{N}\sigma$ 附近。

这个壳层的厚度由「把 $r^2$ 的标准差转换成 $r$ 的标准差」给出：对小的 $\Delta r / r$，有 $\Delta \log r = \Delta r / r = (1/2)\Delta \log r^2 = (1/2)(\Delta r^2)/r^2$；于是取 $\Delta(r^2) = \sqrt{2N}\sigma^2$，得 $r$ 的标准差为 $\Delta r = (1/2) r (\Delta r^2)/r^2 = \sigma/\sqrt{2}$。

Gauss 分布在壳层上一点 $x_{\text{shell}}$（此处 $r = \sqrt{N}\sigma$）的概率密度为

```math
\begin{aligned}
P(x_{\text{shell}}) &= \frac{1}{(2\pi\sigma^2)^{N/2}} \exp\left(-\frac{N\sigma^2}{2\sigma^2}\right) \\
&= \frac{1}{(2\pi\sigma^2)^{N/2}} \exp\left(-\frac{N}{2}\right).
\end{aligned} \qquad (6.27)
```

而在原点的概率密度是

```math
P(x = 0) = \frac{1}{(2\pi\sigma^2)^{N/2}}. \qquad (6.28)
```

于是 $P(x_{\text{shell}})/P(x = 0) = \exp(-N/2)$。在 typical radius 处的概率密度比原点处的密度小 $e^{-N/2}$ 倍。若 $N = 1000$，则原点的概率密度比它大 $e^{500}$ 倍。


<span style="color:#7f8c8d">书内 p132 ｜ 第 7 章 Codes for Integers 开篇</span>

## 7 Codes for Integers（第 7 章 整数的编码）

> <span style="color:#7f8c8d">边注：这一章是一段旁白（aside），可以安全跳过。</span>

**Solution to exercise 6.22（p.127）**

要讨论整数的编码，我们需要一些定义。

**正整数 $n$ 的 standard binary representation（标准二进制表示）** 记作 $c_b(n)$，例如 $c_b(5) = 101$，$c_b(45) = 101101$。

**正整数 $n$ 的 standard binary length（标准二进制长度）** $l_b(n)$ 是串 $c_b(n)$ 的长度。例如 $l_b(5) = 3$，$l_b(45) = 6$。

标准二进制表示 $c_b(n)$ 对整数而言不是 uniquely decodeable（唯一可译）的码，因为我们无法知道一个整数在哪里结束。例如 $c_b(5) c_b(5)$ 与 $c_b(45)$ 完全相同。如果在收到每个整数之前我们就知道它的 standard binary length，那它就会是唯一可译的。

注意到所有正整数的标准二进制表示都以 1 开头，我们就可以定义另一种表示：

**正整数 $n$ 的 headless binary representation（无头二进制表示）** 记作 $c_B(n)$，例如 $c_B(5) = 01$，$c_B(45) = 01101$，$c_B(1) = \epsilon$（其中 $\epsilon$ 表示空串）。

如果我们知道整数的长度 $l_b(n)$，这种表示就是唯一可译的。

那么，怎样才能为整数造出一个唯一可译的码？可以区分出两种策略。

1. **Self-delimiting codes（自定界码）。** 我们先用某种方式传达整数的长度 $l_b(n)$，而它本身也是一个正整数；然后传达整数 $n$ 本身，用 $c_B(n)$。
2. **Codes with `end of file' characters（带「文件结束」字符的码）。** 我们把整数编码成长度为 $b$ 个 bit 的块，并保留 $2^b$ 个 symbol 中的一个，赋予它「end of file」的特殊含义。把整数编码成块的方案要安排得使这个保留 symbol 不会因其他目的而被用到。

最简单的、唯一可译的整数码是 unary code（一元码），它可以被看成带 end of file 字符的码。


<span style="color:#7f8c8d">书内 p133 ｜ 第 7 章 ／ unary code ／ Code C 与 Code C̄</span>

**Unary code（一元码）。** 整数 $n$ 的编码是：发送 $n - 1$ 个 0，随后跟着一个 1。

| $n$ | $c_U(n)$ |
|---|---|
| 1 | `1` |
| 2 | `01` |
| 3 | `001` |
| 4 | `0001` |
| 5 | `00001` |
| $\vdots$ | $\vdots$ |
| 45 | `000000000000000000000000000000000000000000001` |

unary code 的长度是 $l_U(n) = n$。

如果 $n$ 上的概率分布是 $p_U(n) = 2^{-n}$，那么 unary code 就是整数的 optimal code。

**Self-delimiting codes（自定界码）**

我们可以用 unary code 来编码 $n$ 的二进制编码的长度，从而做出一个自定界码：

**Code $\bar{C}$。** 我们先发送 $l_b(n)$ 的 unary code，随后发送 $n$ 的 headless binary representation。

```math
\bar{c}(n) = c_U[l_b(n)]\, c_B(n). \qquad (7.1)
```

Table 7.1 给出若干整数的码。上划线表示把每个串划分成 $c_U[l_b(n)]$ 与 $c_B(n)$ 两部分。我们也可以等价地把 $\bar{c}(n)$ 看成「$l_b(n) - 1$ 个 0」后面接 $n$ 的标准二进制表示 $c_b(n)$。

codeword $\bar{c}(n)$ 的长度为 $\bar{l}(n) = 2 l_b(n) - 1$。

码 $\bar{C}$ 隐含的 $n$ 上概率分布可以分解成 $l$ 上的分布与「给定长度时整数上的均匀分布」两部分之积：

```math
P(l) = 2^{-l}, \qquad (7.2)
```

```math
P(n \mid l) = \begin{cases} 2^{-l+1} & l_b(n) = l \\ 0 & \text{otherwise}. \end{cases} \qquad (7.3)
```

| $n$ | $c_b(n)$ | $l_b(n)$ | $\bar{c}(n)$ |
|---|---|---|---|
| 1 | `1` | 1 | `1` |
| 2 | `10` | 2 | `010` |
| 3 | `11` | 2 | `011` |
| 4 | `100` | 3 | `00100` |
| 5 | `101` | 3 | `00101` |
| 6 | `110` | 3 | `00110` |
| $\vdots$ | | | |
| 45 | `101101` | 6 | `00000101101` |

（上表为 Table 7.1：Code $\bar{C}$。上划线在原文中用来标出 $c_U[l_b(n)]$ 与 $c_B(n)$ 的分界，本表用独立列替代。）

现在，对上面这个码 $\bar{C}$ 而言，传达长度的 header 占用的 bit 数总是与整数的标准二进制表示一样多（上下差一个）。如果我们预期会遇到大整数（大文件），这种表示就显得次优，因为它导致所有文件都占据其未编码大小的两倍。我们可以不用 unary code 来编码长度 $l_b(n)$，而用 $C$ 本身。

**Code $\bar{\bar{C}}$。** 我们用 $\bar{C}$ 发送长度 $l_b(n)$，随后发送 $n$ 的 headless binary representation。

```math
\bar{\bar{c}}(n) = \bar{c}[l_b(n)]\, c_B(n). \qquad (7.4)
```

把这个过程迭代下去，我们可以定义一串码。

**Code $\bar{\bar{\bar{C}}}$。**

```math
\bar{\bar{\bar{c}}}(n) = \bar{\bar{c}}[l_b(n)]\, c_B(n). \qquad (7.5)
```

**Code $\bar{\bar{\bar{\bar{C}}}}$。**

```math
\bar{\bar{\bar{\bar{c}}}}(n) = \bar{\bar{\bar{c}}}[l_b(n)]\, c_B(n). \qquad (7.6)
```

| $n$ | $\bar{\bar{c}}(n)$ | $\bar{\bar{\bar{c}}}(n)$ |
|---|---|---|
| 1 | `1` | `1` |
| 2 | `0100` | `01000` |
| 3 | `0101` | `01001` |
| 4 | `01100` | `010100` |
| 5 | `01101` | `010101` |
| 6 | `01110` | `010110` |
| $\vdots$ | | |
| 45 | `0011001101` | `0111001101` |

（上表为 Table 7.2：Code $\bar{\bar{C}}$ 与 $\bar{\bar{\bar{C}}}$。原文表题为「$\bar{\bar{C}}$ and $\bar{\bar{\bar{C}}}$」，PDF 文字层把上划线的重数丢掉了；逐值复算确认第一列是 $\bar{\bar{c}}(n)$、第二列是 $\bar{\bar{\bar{c}}}(n)$ —— 例 $n = 4$：$\bar{\bar{c}}(4) = \bar{c}(3)\,c_B(4) = $ `011` + `00` = `01100`，与表中一致。）

> <span style="color:#7f8c8d">译本复算：$n = 1 \ldots 10000$ 全部满足 $\bar{l}(n) = 2 l_b(n) - 1$；上表逐行按 (7.1) 机械生成，与书中值一致（例：$n = 45$，$l_b(45) = 6$，$c_U(6) = $ `000001`，$c_B(45) = $ `01101`，故 $\bar{c}(45) = $ `00000101101`，共 11 bit，与 Table 7.1 中的值逐 bit 相同）。</span>


<span style="color:#7f8c8d">书内 p134 ｜ 第 7 章 ／ Codes with end-of-file symbols ／ Exercise 7.1 ／ tiny file</span>

**Codes with end-of-file symbols（带 end-of-file symbol 的码）**

我们也可以做基于 byte 的表示。（这里 `byte' 一词用得宽松，指任何定长 bit 串，不只是 8 bit 长的串。）如果我们以某个 base 编码这个数，例如十进制，那么每个 digit（数码）可以用一个 byte 表示。要把 0 到 9 的一个 digit 表示在 byte 中，我们需要 4 bit。因为 $2^4 = 16$，这就剩下 6 个多余的四 bit symbol $\{1010, 1011, 1100, 1101, 1110, 1111\}$，它们不对应任何十进制 digit。我们可以把它们用作 end-of-file symbol，标记正整数结束。

显然，拥有不止一个 end-of-file symbol 是冗余的，所以更高效的码会把整数编成 base 15，只用第十六个 symbol $1111$ 作为标点字符。把这个想法一般化，我们可以为 base 3、base 7、以及任何形如 $2^n - 1$ 的 base 做出类似的基于 byte 的整数码。

| $n$ | $c_3(n)$ | $c_7(n)$ |
|---|---|---|
| 1 | `01` `11` | `001` `111` |
| 2 | `10` `11` | `010` `111` |
| 3 | `01` `00` `11` | `011` `111` |
| … | | |
| 45 | `01` `10` `00` `00` `11` | `110` `011` `111` |

[Table 7.3：两个带 end-of-file symbol 的码，$C_3$ 与 $C_7$。原书用空格显示 byte 边界（$C_3$ 的 block 是 2 bit、$C_7$ 的 block 是 3 bit），每行最后那个保留符号 —— $C_3$ 的 `11`、$C_7$ 的 `111` —— 就是「到此结束」的标点；本表用代码块标出同样的分组。]

> <span style="color:#7f8c8d">译本复算：$45 = 1200_3$（因 $1 \times 27 + 2 \times 9 + 0 + 0 = 45$），故 $c_3(45)$ 的数值部分是四个 2 bit 组 `01` `10` `00` `00`，再接 EOF 组 `11`；又 $45 = 63_7$（因 $6 \times 7 + 3 = 45$），故 $c_7(45)$ 是 `110` `011` 再接 `111`。两组都与书中逐 bit 相同，也说明 base 必须是 $2^k - 1$ 才能让「每个 digit 占 $k$ bit、留出一个全 1 的标点」同时成立。</span>


这些码几乎都是 complete 的（回忆：若一个码满足 Kraft inequality 且取等号，则称它是 complete 的）。它们剩下的低效之处在于：它们还提供了编码整数零与空串的能力，而这两者都不是我们需要的。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 7.1 [2, p.136]</span>

Consider the implicit probability distribution over integers corresponding to the code with an end-of-file character.

(a) If the code has eight-bit blocks (i.e., the integer is coded in base 255), what is the mean length in bits of the integer, under the implicit distribution?

(b) If one wishes to encode binary files of expected size about one hundred kilobytes using a code with an end-of-file character, what is the optimal block size?

**Encoding a tiny file（编码一个极小的文件）**

为了演示上面讨论的各个码，现在我们用每个码来编码一个小文件，它只有 14 个字符：

```text
Claude Shannon .
```

- 如果我们把 ASCII 字符映射到七位 symbol（例如十进制下 C = 67、l = 108 等），这 14 个字符的文件就对应整数

```text
n = 167 987 786 364 950 891 085 602 469 870 (decimal)
```

> <span style="color:#7f8c8d">译本复算：把 `Claude Shannon` 的 14 个 ASCII 字符各写成 7 bit 并依次拼接，得到 98 bit 串，其十进制值正是上述数字（`int(''.join(format(ord(c), '07b') for c in 'Claude Shannon'), 2) = 167987786364950891085602469870`，与书中值逐位相同）；$2^{97} \approx 1.58 \times 10^{29}$，与该值同量级，说明 98 bit 恰好用满。</span>

- $n$ 的 unary code 由这么多个（减一的）0，再加一个 1 构成。如果把所有海洋都变成墨水，并且每立方毫米写一百个 bit，这些墨水也许才够写出 $c_U(n)$。

- $n$ 的标准二进制表示是这个长度为 98 的 bit 序列：

```text
c_b(n) = 1000011110110011000011110101110010011001010100000
         1010011110100011000011101110110111011011111101110
```

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 7.2 [2]</span>

Write down or describe the following self-delimiting representations of the above number $n$: $\bar{c}(n)$, $\bar{\bar{c}}(n)$, $\bar{\bar{\bar{c}}}(n)$, $\bar{\bar{\bar{\bar{c}}}}(n)$, $c_3(n)$, $c_7(n)$, and $c_{15}(n)$. Which of these encodings is the shortest? [Answer: $c_{15}$.]


<span style="color:#7f8c8d">书内 p135 ｜ 第 7 章 ／ Comparing the codes ／ Algorithm 7.4</span>

**Comparing the codes（比较这些码）**

有人会用这样一句话回答「两个码中哪一个更优？」：「对 $n \gt k$，码 1 更优；对 $n \lt k$，码 2 更优。」但我主张这种回答没有抓住要点：**任何 complete code 都对应一个使它最优的 prior（先验）；你不应该说别的码比它更优。** 别的码对其他 prior 才是最优的。应当去思考这些隐含的 prior，从而为自己的应用得到最好的码。

注意：你不能免费地在两个码之间切换、哪个短就用哪个。一旦这样做，就必须以某种方式把消息加长，以指明用的是两个码中的哪一个。如果这靠一个前导 bit 来完成，就会发现所得的码是次优的，因为它不满足 Kraft equality，正如 exercise 5.33（p.104）所讨论的。

比较整数码的另一种方式，是考虑一列概率分布，例如 $n \ge 1$ 上的单调概率分布，然后给各个码排名：它们编码这些分布中的任何一个有多好。如果一个码对某个给定类别中的任何分布，其平均长度都在理想平均长度的某个倍数之内，那么它就称为 `universal' code（通用码）。

让我再说一遍。我们这里遇到的是另一种世界观 —— 与上面主张的「找出整数上的好 prior」不同，许多理论家研究的是这样一个问题：造出「对一大类 prior 而言都是相当好的码」的码。这里通常考虑的 prior 类，是满足下面两条的 prior 集合：(a) 在整数上指派单调递减的概率；(b) entropy 有限。

上面讨论的若干码都是 universal 的。另一个优雅地超越整个自定界码序列的码，是 Elias 的「universal code for integers」（Elias, 1975）：它实际上是从所有码 $C, \bar{C}, \ldots$ 中自动挑选。它的工作方式是发送一列消息，每条消息编码下一条消息的长度，并用单个 bit 指明这条消息是不是最终那个整数（按其 standard binary representation）。因为长度是正整数，而所有正整数都以 `1` 开头，所以所有前导的 1 都可以省掉。

<span style="color:#1e8449;">**[译注]**</span> **整数码必须自定界：没有分隔符时，"码字在哪里结束"只能由码字自己携带**

机制：如果只把 $n$ 写成二进制，接收端无法知道后面还有几位属于 $n$。解法是**递归地先发长度**：$C(n)$ 用固定宽度，$\bar C(n)$ 发"$C(n)$ 的长度 + $C(n)$"，$\bar{\bar C}(n)$ 再套一层，直到某层长度落进可判定的范围（Elias 的 universal code 用"终止于 1"来封顶，等价于自动挑选层数）。每套一层多花约 $\log\log n$ 位，总长 $\approx \log n + \log\log n + \cdots$，是双对数收敛的级数，因此总开销只比 $\log n$ 多一点点。

抽掉自定界，整数码只能用在定长块里：无法把整数序列拼成一条流，也无法在流中间插入——这就是为什么通信协议里长度字段必须自带边界，否则一个错位就全盘皆错。词表码与整数码的分工也在此：Kraft 管的是**给定长度表能不能造前缀码**（§5.2），这一章管的是**长度本身怎么传**。

挂载（真同构，不是术语对照）：这就是 utf-8 与 protobuf varint 的做法——首字节的高位标记后面跟着几个续字节，长度信息编码在码字内部；也是 Huffman 码字能直接拼接的原因（prefix property 保证边界）。三者数学上是同一件事：**码字自定界 = 码字集合前缀无关**。

坐标：第 7 章（原书 p.133–137，PDF p.145–149），$C/\bar C/\bar{\bar C}$ 的定义、Algorithm 7.4、Table 7.5（Elias universal code）。

[Algorithm 7.4：Elias 的整数 encoder。生成过程从右往左进行：

```text
Write '0'
Loop {
    if floor(log2(n)) == 0 then halt
    Prepend cb(n) to the written string
    n := floor(log2(n))
}
```

]

$C_{\text{Elias}}$ 的 encoder 见 algorithm 7.4。编码是从右往左生成的。Table 7.5 给出所得的 codeword。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 7.3 [2]</span>

Show that the Elias code is not actually the best code for a prior distribution that expects very large integers. (Do this by constructing another code and specifying how large $n$ must be for your code to give a shorter length than Elias's.)


<span style="color:#7f8c8d">书内 p136 ｜ Table 7.5：Elias 的 universal code</span>

| $n$ | $c(n)$ | $n$ | $c(n)$ | $n$ | $c(n)$ | $n$ | $c(n)$ |
|---|---|---|---|---|---|---|---|
| 1 | `0` | 9 | `1110010` | 31 | `10100111110` | 256 | `1110001000000000` |
| 2 | `100` | 10 | `1110100` | 32 | `101011000000` | 365 | `1110001011011010` |
| 3 | `110` | 11 | `1110110` | 45 | `101011011010` | 511 | `1110001111111110` |
| 4 | `101000` | 12 | `1111000` | 63 | `101011111110` | 512 | `11100110000000000` |
| 5 | `101010` | 13 | `1111010` | 64 | `1011010000000` | 719 | `11100110110011110` |
| 6 | `101100` | 14 | `1111100` | 127 | `1011011111110` | 1023 | `11100111111111110` |
| 7 | `101110` | 15 | `1111110` | 128 | `10111100000000` | 1024 | `111010100000000000` |
| 8 | `1110000` | 16 | `10100100000` | 255 | `10111111111110` | 1025 | `111010100000000010` |

（上表为 Table 7.5：Elias 的「universal」整数码，$n = 1$ 到 1025 的部分示例。原文以四栏并排排版，本表按 $n$ 从小到大重排成八列。）

> <span style="color:#7f8c8d">译本复算：按 Algorithm 7.4 逐字实现（先写 `0`；循环中若 $\lfloor \log_2 n \rfloor = 0$ 则停机，否则把 $c_b(n)$ 前插到已写串前面、并令 $n := \lfloor \log_2 n \rfloor$），对表中 32 个 $n$ 全部重算，**32 项与书中值逐 bit 相同**。例：$n = 4$，先写 `0`，前插 $c_b(4) = $ `100` 得 `1000`，$n := 2$；前插 $c_b(2) = $ `10` 得 `101000`，$n := 1$，停机，结果 `101000` 与表中一致。</span>


<span style="color:#7f8c8d">书内 p137 ｜ Solutions（exercise 7.1）／ Part II 扉页</span>

#### Solutions（解答）

#### Solution to exercise 7.1（p.134）（exercise 7.1 的解答）

在一个把整数表示成某个 base $q$ 的码里，end-of-file symbol 的用法对应这样一个信念：当前字符是「这个数的最后一个字符」的概率为 $1/(q + 1)$。因此，这个码所匹配的 prior 在整数长度上放了一个指数先验分布。

**(a)** 期望的字符数是 $q + 1 = 256$，所以整数的期望长度是 $256 \times 8 \simeq 2000$ bit。

**(b)** 我们希望找到 $q$ 使 $q \log q \simeq 800\,000$ bit。$2^{15}$ 与 $2^{16}$ 之间的 $q$ 值满足这个条件，所以假定只有一个 end-of-file 字符，16 bit 的块大致就是最优块大小。


<span style="color:#7f8c8d">书内 p138 ｜ Part II Noisy-Channel Coding ／ 第 8 章 Dependent Random Variables ／ 8.1</span>

# Part II ｜ Noisy-Channel Coding（有噪信道编码）

## 8 Dependent Random Variables（第 8 章 相依随机变量）

在上三章讨论 data compression 时，我们把注意力集中在来自一个极简单概率分布的随机向量 $x$ 上，也就是那种各分量 $x_n$ 彼此独立的可分（separable）分布。

本章我们考虑各随机变量相互依赖的 joint ensemble（联合总体）。这份材料有两个动机。第一，现实世界的数据有有趣的相关性，所以要把数据压缩做好，我们就需要知道如何与包含依赖关系的模型打交道。第二，一个输入为 $x$、输出为 $y$ 的 noisy channel（有噪信道）定义一个联合总体，其中 $x$ 与 $y$ 相依 —— 如果它们独立，就不可能通过该信道通信 —— 所以有噪信道上的通信（第 9–11 章的主题）是用 joint ensemble 的 entropy 来描述的。

### 8.1 More about entropy（entropy 的更多内容）

本节给出与 entropy 有关的定义与习题，接续 section 2.4。

$X, Y$ 的 **joint entropy（联合熵）** 是：

```math
H(X, Y) = \sum_{xy \in \mathcal{A}_X \mathcal{A}_Y} P(x, y) \log \frac{1}{P(x, y)}. \qquad (8.1)
```

entropy 对独立随机变量是可加的：

```math
H(X, Y) = H(X) + H(Y) \quad \text{iff} \quad P(x, y) = P(x)P(y). \qquad (8.2)
```

**给定 $y = b_k$ 时 $X$ 的 conditional entropy（条件熵）** 是概率分布 $P(x \mid y = b_k)$ 的 entropy：

```math
H(X \mid y = b_k) = \sum_{x \in \mathcal{A}_X} P(x \mid y = b_k) \log \frac{1}{P(x \mid y = b_k)}. \qquad (8.3)
```

**给定 $Y$ 时 $X$ 的 conditional entropy** 是「给定 $y$ 时 $X$ 的条件熵」在 $y$ 上的平均。

```math
\begin{aligned}
H(X \mid Y) &= \sum_{y \in \mathcal{A}_Y} P(y) \left[ \sum_{x \in \mathcal{A}_X} P(x \mid y) \log \frac{1}{P(x \mid y)} \right] \\
&= \sum_{xy \in \mathcal{A}_X \mathcal{A}_Y} P(x, y) \log \frac{1}{P(x \mid y)}.
\end{aligned} \qquad (8.4)
```

它度量的是：当 $y$ 已知之后，关于 $x$ 仍剩下的平均不确定性。


<span style="color:#7f8c8d">书内 p139 ｜ 8.1 More about entropy</span>

<span style="color:#7f8c8d">边注：$X$ 的 marginal entropy（边缘熵）就是 $X$ 的 entropy $H(X)$ 的另一个名字，用它与上面列出的各种 conditional entropy 相区别。</span>

**information content 的链式法则（Chain rule for information content）。** 由概率的 product rule，equation (2.6)，我们得到：

```math
\log \frac{1}{P(x, y)} = \log \frac{1}{P(x)} + \log \frac{1}{P(y \mid x)}, \qquad (8.5)
```

因此

```math
h(x, y) = h(x) + h(y \mid x). \qquad (8.6)
```

用文字说：$x$ 与 $y$ 的 information content，等于 $x$ 的 information content 加上给定 $x$ 时 $y$ 的 information content。

**entropy 的链式法则（Chain rule for entropy）。** joint entropy、conditional entropy 与 marginal entropy 之间的关系是：

```math
H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y). \qquad (8.7)
```

用文字说：$X$ 与 $Y$ 的不确定性，等于 $X$ 的不确定性加上给定 $X$ 时 $Y$ 的不确定性。

$X$ 与 $Y$ 之间的 **mutual information（互信息）** 是

```math
I(X; Y) \equiv H(X) - H(X \mid Y), \qquad (8.8)
```

它满足 $I(X; Y) = I(Y; X)$，以及 $I(X; Y) \ge 0$。它度量的是：学到 $y$ 的值之后，关于 $x$ 的不确定性的平均减少量；反过来也一样 —— 它是 $x$ 关于 $y$ 所传递的平均信息量。

**给定 $z = c_k$ 时 $X$ 与 $Y$ 的 conditional mutual information（条件互信息）**，是在联合总体 $P(x, y \mid z = c_k)$ 中随机变量 $X$ 与 $Y$ 之间的 mutual information，

```math
I(X; Y \mid z = c_k) = H(X \mid z = c_k) - H(X \mid Y, z = c_k). \qquad (8.9)
```

**给定 $Z$ 时 $X$ 与 $Y$ 的 conditional mutual information** 是上述条件互信息在 $z$ 上的平均。

```math
I(X; Y \mid Z) = H(X \mid Z) - H(X \mid Y, Z). \qquad (8.10)
```

不会再定义任何其他的「三项 entropy」。例如，像 $I(X; Y; Z)$ 与 $I(X \mid Y; Z)$ 这样的表达式是非法的。但你可以在表达式 $I(X; Y \mid Z)$ 的三个位置中的每一个里，放入任意多个变量的合取 —— 例如 $I(A, B; C, D \mid E, F)$ 是可以的：它度量的是，在已知 $e$ 与 $f$ 的前提下，$c$ 与 $d$ 平均传递了多少关于 $a$ 与 $b$ 的信息。

图 8.1 展示了联合总体总 entropy $H(X, Y)$ 可以怎样分解。这张图很重要。


<span style="color:#7f8c8d">书内 p140 ｜ Figure 8.1 ／ 8.2 Exercises</span>

[Figure 8.1：joint information、marginal entropy、conditional entropy 与 mutual entropy 之间的关系。整条横条的高度是 $H(X, Y)$；左段是 $H(X)$，右段是 $H(Y)$，两者重叠部分是 $I(X; Y)$；左段不重叠部分标 $H(X \mid Y)$，右段不重叠部分标 $H(Y \mid X)$。注意与图 8.2 的 Venn 图表示相对照。]

### 8.2 Exercises（8.2 节 习题）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.1 [1]</span>

Consider three independent random variables $u$, $v$, $w$ with entropies $H_u$, $H_v$, $H_w$. Let $X \equiv (U, V)$ and $Y \equiv (V, W)$. What is $H(X, Y)$? What is $H(X \mid Y)$? What is $I(X; Y)$?

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.2 [3, p.142]</span>

Referring to the definitions of conditional entropy (8.3-8.4), confirm (with an example) that it is possible for $H(X \mid y = b_k)$ to exceed $H(X)$, but that the average, $H(X \mid Y)$, is less than $H(X)$. So data are helpful — they do not increase uncertainty, on average.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.3 [2, p.143]</span>

Prove the chain rule for entropy, equation (8.7). [ $H(X, Y) = H(X) + H(Y \mid X)$ ].

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.4 [2, p.143]</span>

Prove that the mutual information $I(X; Y) \equiv H(X) - H(X \mid Y)$ satisfies $I(X; Y) = I(Y; X)$ and $I(X; Y) \ge 0$.

[Hint: see exercise 2.26 (p.37) and note that

```math
I(X; Y) = D_{\mathrm{KL}}(P(x, y) \| P(x)P(y)). \qquad (8.11)
```

]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.5 [4]</span>

The `entropy distance' between two random variables can be defined to be the difference between their joint entropy and their mutual information:

```math
D_H(X, Y) \equiv H(X, Y) - I(X; Y). \qquad (8.12)
```

Prove that the entropy distance satisfies the axioms for a distance — $D_H(X, Y) \ge 0$, $D_H(X, X) = 0$, $D_H(X, Y) = D_H(Y, X)$, and $D_H(X, Z) \le D_H(X, Y) + D_H(Y, Z)$. [Incidentally, we are unlikely to see $D_H(X, Y)$ again but it is a good function on which to practise inequality-proving.]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.6 [2, p.147]</span>

A joint ensemble $XY$ has the following joint distribution.

| $P(x, y)$ | $x = 1$ | $x = 2$ | $x = 3$ | $x = 4$ |
|---|---|---|---|---|
| $y = 1$ | 1/8 | 1/16 | 1/32 | 1/32 |
| $y = 2$ | 1/16 | 1/8 | 1/32 | 1/32 |
| $y = 3$ | 1/16 | 1/16 | 1/16 | 1/16 |
| $y = 4$ | 1/4 | 0 | 0 | 0 |

（上表为原书页内表格的重建。原文以行标签 `y` 与列标签 `x` 排出 4×4 矩阵。译本复算：行和均为 $1/4$，列和为 $1/2, 1/4, 1/8, 1/8$，总和为 1。）

What is the joint entropy $H(X, Y)$? What are the marginal entropies $H(X)$ and $H(Y)$? For each value of $y$, what is the conditional entropy $H(X \mid y)$? What is the conditional entropy $H(X \mid Y)$? What is the conditional entropy of $Y$ given $X$? What is the mutual information between $X$ and $Y$?


<span style="color:#7f8c8d">书内 p141 ｜ 8.3 Further exercises ／ 三变量 entropy ／ data-processing theorem</span>

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.7 [2, p.143]</span>

Consider the ensemble $XYZ$ in which $\mathcal{A}_X = \mathcal{A}_Y = \mathcal{A}_Z = \{0, 1\}$, $x$ and $y$ are independent with $P_X = \{p, 1 - p\}$ and $P_Y = \{q, 1 - q\}$ and

```math
z = (x + y) \bmod 2. \qquad (8.13)
```

(a) If $q = 1/2$, what is $P_Z$? What is $I(Z; X)$?

(b) For general $p$ and $q$, what is $P_Z$? What is $I(Z; X)$? Notice that this ensemble is related to the binary symmetric channel, with $x$ = input, $y$ = noise, and $z$ = output.

[Figure 8.2：一种会误导人的 entropy 表示（请与图 8.1 对照）。这里把 $H(X)$ 与 $H(Y)$ 画成两个部分重叠的圆（Venn 图）：左圆独有部分标 $H(X \mid Y)$，右圆独有部分标 $H(Y \mid X)$，交集标 $I(X; Y)$，而两圆并集的外框标为 $H(X, Y)$。图 8.3 沿用同一种画法却更糟。]

**Three term entropies（三项 entropy）**

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.8 [3, p.143]</span>

Many texts draw figure 8.1 in the form of a Venn diagram (figure 8.2). Discuss why this diagram is a misleading representation of entropies. Hint: consider the three-variable ensemble $XYZ$ in which $x \in \{0, 1\}$ and $y \in \{0, 1\}$ are independent binary variables and $z \in \{0, 1\}$ is defined to be $z = x + y \bmod 2$.

### 8.3 Further exercises（8.3 节 进阶习题）

**The data-processing theorem（数据处理定理）**

data processing theorem 断言：数据处理只能破坏信息。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.9 [3, p.144]</span>

Prove this theorem by considering an ensemble $WDR$ in which $w$ is the state of the world, $d$ is data gathered, and $r$ is the processed data, so that these three variables form a Markov chain

```math
w \rightarrow d \rightarrow r, \qquad (8.14)
```

that is, the probability $P(w, d, r)$ can be written as

```math
P(w, d, r) = P(w) P(d \mid w) P(r \mid d). \qquad (8.15)
```

Show that the average information that $R$ conveys about $W$, $I(W; R)$, is less than or equal to the average information that $D$ conveys about $W$, $I(W; D)$.

这个定理既是对 data processing 的警示，也同样是对我们「information」定义的警示！


<span style="color:#7f8c8d">书内 p142 ｜ Inference and information measures ／ 8.4 Solutions（8.2 起）</span>

**Inference and information measures（推断与信息度量）**

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.10 [2]</span> The three cards（三张卡片）

(a) 一张卡片两面都是白色；一张两面都是黑色；还有一张一面白一面黑。把三张卡片洗乱、朝向随机化。抽出一张放在桌上，朝上的一面是黑色。它朝下那一面是什么颜色？（解这个推断问题。）

(b) 看到朝上一面是否传达了关于朝下一面颜色的信息？讨论这一情形中的 information content 与 entropy。令朝上一面的颜色取值为 $u$、朝下一面的颜色取值为 $l$。设想我们随机抽一张卡片、并且同时得知 $u$ 与 $l$。$u$ 的熵 $H(U)$ 是多少？$l$ 的熵 $H(L)$ 是多少？$U$ 与 $L$ 之间的 mutual information $I(U; L)$ 是多少？

**Entropies of Markov processes（Markov 过程的 entropy）**

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 8.11 [3]</span>

In the guessing game, we imagined predicting the next letter in a document starting from the beginning and working towards the end. Consider the task of predicting the reversed text, that is, predicting the letter that precedes those already known. Most people find this a harder task. Assuming that we model the language using an $N$-gram model (which says the probability of the next character depends only on the $N - 1$ preceding characters), is there any difference between the average information contents of the reversed language and the forward language?

> <span style="color:#7f8c8d">译本注：这一问的答案藏在「$N$-gram 模型把条件方向固定为从左到右」这件事里：若语言模型本身是前向的，那么反向预测所需的期望 information content 与正向并不相同；但若把模型换成真正的双向模型（或把 $N$-gram 视为对联合分布的一种近似），两者的平均 information content 只差模型误差项。MacKay 在此只想提示：**「读起来更难」不等于「信息量更大」**，难易感与 entropy 是两件事。</span>

### 8.4 Solutions（8.4 节 解答）

#### Solution to exercise 8.2（p.140）（exercise 8.2 的解答）

$H(X \mid y)$ 超过 $H(X)$ 的例子见 exercise 8.6（p.140）（取 $y = 3$）。

我们可以把表达式转成 relative entropy（用 Bayes 定理），再援引 Gibbs' inequality（exercise 2.26（p.37）），来证明不等式 $H(X \mid Y) \le H(X)$：

```math
\begin{aligned}
H(X \mid Y) &= \sum_{y \in \mathcal{A}_Y} P(y) \left[ \sum_{x \in \mathcal{A}_X} P(x \mid y) \log \frac{1}{P(x \mid y)} \right] \\
&= \sum_{xy \in \mathcal{A}_X \mathcal{A}_Y} P(x, y) \log \frac{1}{P(x \mid y)} \qquad (8.16) \\
&= \sum_{xy} P(x) P(y \mid x) \log \frac{P(y)}{P(y \mid x) P(x)} \qquad (8.17) \\
&= \sum_x P(x) \log \frac{1}{P(x)} + \sum_x P(x) \sum_y P(y \mid x) \log \frac{P(y)}{P(y \mid x)}. \qquad (8.18)
\end{aligned}
```

最后一个表达式是一族 relative entropy 之和，即在分布 $P(y \mid x)$ 与 $P(y)$ 之间。所以

```math
H(X \mid Y) \le H(X) + 0, \qquad (8.19)
```

等号当且仅当对所有 $x$ 与 $y$ 都有 $P(y \mid x) = P(y)$ 时成立（也就是 $X$ 与 $Y$ 独立时）。


<span style="color:#7f8c8d">书内 p143 ｜ 8.4 Solutions（8.3、8.4）</span>

#### Solution to exercise 8.3（p.140）（exercise 8.3 的解答）

entropy 的链式法则来自联合概率的分解：

```math
\begin{aligned}
H(X, Y) &= \sum_{xy} P(x, y) \log \frac{1}{P(x, y)} \qquad (8.20) \\
&= \sum_{xy} P(x) P(y \mid x) \left[ \log \frac{1}{P(x)} + \log \frac{1}{P(y \mid x)} \right] \qquad (8.21) \\
&= \sum_x P(x) \log \frac{1}{P(x)} + \sum_x P(x) \sum_y P(y \mid x) \log \frac{1}{P(y \mid x)} \qquad (8.22) \\
&= H(X) + H(Y \mid X). \qquad (8.23)
\end{aligned}
```

#### Solution to exercise 8.4（p.140）（exercise 8.4 的解答）

mutual information 的对称性：

```math
\begin{aligned}
I(X; Y) &= H(X) - H(X \mid Y) \qquad (8.24) \\
&= \sum_x P(x) \log \frac{1}{P(x)} - \sum_{xy} P(x, y) \log \frac{1}{P(x \mid y)} \qquad (8.25) \\
&= \sum_{xy} P(x, y) \log \frac{P(x \mid y)}{P(x)} \qquad (8.26) \\
&= \sum_{xy} P(x, y) \log \frac{P(x, y)}{P(x)P(y)}. \qquad (8.27)
\end{aligned}
```

这个表达式在 $x$ 与 $y$ 中是对称的，所以

```math
I(X; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X). \qquad (8.28)
```

我们可以用两种办法证明 mutual information 非负。第一种是从

```math
I(X; Y) = \sum_{x, y} P(x, y) \log \frac{P(x, y)}{P(x)P(y)} \qquad (8.29)
```

继续往下：它是个 relative entropy，用 Gibbs' inequality（在 p.44 证明）即可断言它 $\ge 0$，等号仅在 $P(x, y) = P(x)P(y)$ 时成立，也就是 $X$ 与 $Y$ 独立时。

另一种办法是对下式用 Jensen's inequality：

```math
- \sum_{x, y} P(x, y) \log \frac{P(x)P(y)}{P(x, y)} \ge - \log \sum_{x, y} P(x, y) \frac{P(x)P(y)}{P(x, y)} = \log 1 = 0. \qquad (8.30)
```


<span style="color:#7f8c8d">书内 p144 ｜ 8.4 Solutions（8.7、8.8、8.9）</span>

#### Solution to exercise 8.7（p.141）（exercise 8.7 的解答）

$z = x + y \bmod 2$。

(a) 若 $q = 1/2$，则 $P_Z = \{1/2, 1/2\}$，且 $I(Z; X) = H(Z) - H(Z \mid X) = 1 - 1 = 0$。

(b) 对一般的 $q$ 与 $p$，$P_Z = \{pq + (1 - p)(1 - q),\ p(1 - q) + q(1 - p)\}$。mutual information 是 $I(Z; X) = H(Z) - H(Z \mid X) = H_2(pq + (1 - p)(1 - q)) - H_2(q)$。

**Three term entropies（三项 entropy）**

#### Solution to exercise 8.8（p.141）（exercise 8.8 的解答）

用 Venn 图来描述 entropy 会误导读者，至少有两条理由。

第一，人们习惯把 Venn 图理解为描述集合的图形；但在图 8.2 里画出的「集合」$H(X)$ 与 $H(Y)$ 究竟是什么？那些集合的元素又是什么？我认为这张图会诱导初学者做不恰当的类比。例如，有些学生会以为随机结果 $(x, y)$ 对应图中的某个点，于是把 entropy 与概率混淆。

第二，用 Venn 图来描述，会让人以为所有区域都对应正的量。在两随机变量这一特殊情形下，$H(X \mid Y)$、$I(X; Y)$、$H(Y \mid X)$ 确实都是正的量。可一旦进入三变量总体，我们就会得到一个「看起来都是正面积」的图，而其中某些面积实际上可能对应负的量。图 8.3 正确地表示了诸如

```math
H(X) + H(Z \mid X) + H(Y \mid X, Z) = H(X, Y, Z) \qquad (8.31)
```

这样的关系。但它给人一种误导性的印象：conditional mutual information $I(X; Y \mid Z)$ 小于 mutual information $I(X; Y)$。事实上，标着 A 的那块面积可以对应负的量。考虑联合总体 $(X, Y, Z)$，其中 $x \in \{0, 1\}$ 与 $y \in \{0, 1\}$ 是独立的二值变量，而 $z \in \{0, 1\}$ 被定义为 $z = x + y \bmod 2$。这时显然 $H(X) = H(Y) = 1$ bit，又 $H(Z) = 1$ bit，而 $H(Y \mid X) = H(Y) = 1$，因为这两个变量独立。所以 $X$ 与 $Y$ 之间的 mutual information 为零：$I(X; Y) = 0$。然而，一旦观测到 $z$，$X$ 与 $Y$ 就变得相依了 —— 在已知 $z$ 的前提下知道 $x$，就告诉你 $y$ 是什么：$y = z - x \bmod 2$。所以 $I(X; Y \mid Z) = 1$ bit。于是，标着 A 的那块面积必须对应 $-1$ bit，这张图才能给出正确答案。

[Figure 8.3：又一种会误导人的 entropy 表示（图 8.2 的续）。三个圆分别代表 $H(X)$、$H(Y)$、$H(Z)$，两两交叠；图中标出 $I(X; Y)$、$H(X \mid Y, Z)$、$A$、$I(X; Y \mid Z)$、$H(Y \mid X, Z)$、$H(Z \mid X)$、$H(Z \mid Y)$、$H(Z \mid X, Y)$ 等区域，其中 A 区被单独标出 —— 按文中例子，它必须取 $-1$ bit。]

上面的例子绝不是刻意构造的特例。输入为 $X$、噪声为 $Y$、输出为 $Z$ 的 binary symmetric channel 就是这种情况：$I(X; Y) = 0$（输入与噪声独立），但 $I(X; Y \mid Z) \gt 0$（一旦你看到输出，未知的输入与未知的噪声就紧密相关了！）。

因此，只有在读者清楚「正面积也可能代表负的量」这一前提下，Venn 图表示才是有效的。记住这个附注之后，用集合来解释 entropy 仍然是有帮助的（Yeung, 1991）。

#### Solution to exercise 8.9（p.141）（exercise 8.9 的解答）

对任何联合总体 $XYZ$，下面的 mutual information 链式法则都成立。

```math
I(X; Y, Z) = I(X; Y) + I(X; Z \mid Y). \qquad (8.32)
```

现在，在 $w \rightarrow d \rightarrow r$ 的情形下，给定 $d$ 时 $w$ 与 $r$ 独立，所以 $I(W; R \mid D) = 0$。把链式法则用两次，我们有：

```math
I(W; D, R) = I(W; D) \qquad (8.33)
```

以及

```math
I(W; D, R) = I(W; R) + I(W; D \mid R), \qquad (8.34)
```

所以

```math
I(W; R) - I(W; D) \le 0. \qquad (8.35)
```

> <span style="color:#7f8c8d">译本补一句：把 (8.33) 与 (8.34) 的右边相减得 $I(W; D) - I(W; R) = I(W; D \mid R) \ge 0$，这才是 (8.35) 的完整来源 —— 也就是说，处理之后的数据 $R$ 关于 $W$ 的信息量不会超过原始数据 $D$。这正是 data processing theorem。</span>


<span style="color:#7f8c8d">书内 p145 ｜ About Chapter 9（第 9 章导读）</span>

#### 关于第 9 章（About Chapter 9）

在读第 9 章之前，你应当已经读过第 1 章，做过 exercise 2.26（p.37），以及 exercise 8.2–8.7（pp.140–141）。


<span style="color:#7f8c8d">书内 p146 ｜ 第 9 章 Communication over a Noisy Channel ／ 9.1 The big picture</span>

## 9 Communication over a Noisy Channel（第 9 章 在有噪信道上通信）

### 9.1 The big picture（全局图景）

[Figure 9.1：一个完整的通信系统框图。自上而下的数据流：`Source` → `Source coding`（其内部是 `Compressor`）→ `Channel coding`（其内部是 `Encoder`）→ 标着 $E$ 的 `Noisy channel` → `Decoder` → `Decompressor` → 交付端。箭头之间的标注为：源到压缩器之间是原始文本，压缩器到编码器之间是压缩后的 bit 串，编码器送入信道的是受保护的码字，信道输出送进解码器，解压后还原出文本。]

在第 4–6 章，我们讨论了以 block code、symbol code 和 stream code 做的 source coding。我们隐含地假定：从 compressor 到 decompressor 的信道是无噪的。真实信道是有噪的。现在我们要用两章篇幅讨论 noisy-channel coding 这个主题 —— 即通过有噪信道做无错通信的根本可能性与根本限制。channel coding 的目的是让有噪信道表现得像无噪信道。我们将假定待传输的数据已经过一个好的 compressor，所以这个 bit 流没有明显的冗余。承担传输任务的 channel code 会重新放回一种特殊类型的冗余，其设计目的是让含噪的接收信号可解码。

设想我们以每秒 1000 bit 的速率、取 $p_0 = p_1 = 1/2$，通过一个以概率 $f = 0.1$ 翻转 bit 的有噪信道传输。信息传输速率是多少？我们或许会猜：用每秒期望错误数去减，速率就是每秒 900 bit。但这并不正确，因为接收方并不知道错误发生在哪里。考虑噪声大到「接收 symbol 与发送 symbol 相互独立」的情形：这对应 $f = 0.5$ 的噪声水平，因为仅凭运气就有一半接收 symbol 是对的。而当 $f = 0.5$ 时，一点信息都没传过去。

根据我们学过的 entropy 知识，看起来合理的是：传输的信息量应当用 source 与接收信号之间的 mutual information 来度量，也就是 source 的 entropy 减去「给定接收信号时 source 的 conditional entropy」。

下面我们复习 conditional entropy 与 mutual information 的定义。然后考察：能否用这样的有噪信道做可靠通信。我们将证明：对任何信道 $Q$ 都存在一个非零速率 —— capacity（容量）$C(Q)$ —— 在它以下，信息可以以任意小的错误概率被送达。


<span style="color:#7f8c8d">书内 p147 ｜ 9.2 Review of probability and information ／ 9.3 Noisy channels</span>

### 9.2 Review of probability and information（概率与信息复习）

作为例子，我们取 exercise 8.6（p.140）中的联合分布 $XY$。边缘分布 $P(x)$ 与 $P(y)$ 显示在表的边栏上。

| $P(x, y)$ | $x = 1$ | $x = 2$ | $x = 3$ | $x = 4$ | $P(y)$ |
|---|---|---|---|---|---|
| $y = 1$ | 1/8 | 1/16 | 1/32 | 1/32 | 1/4 |
| $y = 2$ | 1/16 | 1/8 | 1/32 | 1/32 | 1/4 |
| $y = 3$ | 1/16 | 1/16 | 1/16 | 1/16 | 1/4 |
| $y = 4$ | 1/4 | 0 | 0 | 0 | 1/4 |
| $P(x)$ | 1/2 | 1/4 | 1/8 | 1/8 | |

joint entropy 是 $H(X, Y) = 27/8$ bit。marginal entropy 是 $H(X) = 7/4$ bit、$H(Y) = 2$ bit。

我们可以对每个 $y$ 值算出 $x$ 的条件分布，以及每个条件分布的 entropy：

| $P(x \mid y)$ | $x = 1$ | $x = 2$ | $x = 3$ | $x = 4$ | $H(X \mid y)$ / bit |
|---|---|---|---|---|---|
| $y = 1$ | 1/2 | 1/4 | 1/8 | 1/8 | 7/4 |
| $y = 2$ | 1/4 | 1/2 | 1/8 | 1/8 | 7/4 |
| $y = 3$ | 1/4 | 1/4 | 1/4 | 1/4 | 2 |
| $y = 4$ | 1 | 0 | 0 | 0 | 0 |
| | | | | | $H(X \mid Y) = 11/8$ |

注意：$H(X \mid y = 4) = 0$ 小于 $H(X)$，而 $H(X \mid y = 3)$ 却大于 $H(X)$。所以在某些情形下，学到 $y$ 反而会增加我们对 $x$ 的不确定性。还要注意：虽然 $P(x \mid y = 2)$ 与 $P(x)$ 是不同的分布，但条件 entropy $H(X \mid y = 2)$ 等于 $H(X)$。所以得知 $y$ 是 2 这件事改变了我们关于 $x$ 的知识，却没有减少 $x$ 的不确定性（以 entropy 衡量）。不过平均而言，学到 $y$ 确实传递了关于 $x$ 的信息，因为 $H(X \mid Y) \lt H(X)$。

也可以算出 $H(Y \mid X) = 13/8$ bit。mutual information 是 $I(X; Y) = H(X) - H(X \mid Y) = 3/8$ bit。

> <span style="color:#7f8c8d">译本复算（全部命中书中数值）：$H(X, Y) = 3.375 = 27/8$；$H(X) = 1.75 = 7/4$；$H(Y) = 2$；四个条件 entropy 依次为 $1.75, 1.75, 2, 0$，加权得 $H(X \mid Y) = (1/4)(1.75 + 1.75 + 2 + 0) = 1.375 = 11/8$；$H(Y \mid X) = 1.625 = 13/8$；$I(X; Y) = 1.75 - 1.375 = 0.375 = 3/8$。</span>

### 9.3 Noisy channels（有噪信道）

**discrete memoryless channel（离散无记忆信道）$Q$** 由输入 alphabet $\mathcal{A}_X$、输出 alphabet $\mathcal{A}_Y$、以及一组 conditional probability distribution $P(y \mid x)$ 刻画，每个 $x \in \mathcal{A}_X$ 对应一个。

这些 transition probability（转移概率）可以写成一个矩阵

```math
Q_{j|i} = P(y = b_j \mid x = a_i). \qquad (9.1)
```

我通常让输出变量 $j$ 索引行、输入变量 $i$ 索引列，于是 $Q$ 的每一列都是一个概率向量。按这个约定，可以由输入上的概率分布 $p_X$ 通过右乘得到输出的概率 $p_Y$：

```math
p_Y = Q p_X. \qquad (9.2)
```


<span style="color:#7f8c8d">书内 p148 ｜ 9.3 常用信道模型（续） ／ 9.4 Inferring the input given the output</span>

[Figure 9.3（原书无编号的小图）：Binary erasure channel 的转移示意图。左侧输入结点 0、1，右侧输出结点 0、?、1；0→0 与 1→1 各以概率 $1-f$ 直达，0→? 与 1→? 各以概率 $f$ 汇入中间的擦除态，0→1 与 1→0 的转移概率为 0。]

### 9.4 Inferring the input given the output（由输出推断输入）

如果我们假定信道的输入 $x$ 来自某个 ensemble $X$，就得到一个 joint ensemble $XY$，其中随机变量 $x$ 与 $y$ 具有 joint distribution：

```math
P(x, y) = P(y \mid x)P(x). \qquad (9.3)
```

那么，若我们收到某个特定符号 $y$，输入符号 $x$ 是什么？通常我们不会确切知道。我们可以用 Bayes' theorem 写出输入的后验分布：

```math
P(x \mid y) = \frac{P(y \mid x)P(x)}{P(y)} = \frac{P(y \mid x)P(x)}{\sum_{x'} P(y \mid x')P(x')}. \qquad (9.4)
```

#### <span style="color:#c0392b">Example 9.1（例 9.1）</span>

考虑一个错误概率 $f = 0.15$ 的 binary symmetric channel。设输入 ensemble 为 $P_X : \{p_0 = 0.9, p_1 = 0.1\}$。假定我们观测到 $y = 1$。

<span style="color:#1e8449;">**[译注]**</span> **同一个观测，MAP 与 ML 会给出相反判决——先验不是装饰，它决定 §9.5 之后所有核算的起点**

用本节 Example 9.1 的数字点破：$Q$ 是 $f=0.15$ 的 BSC，先验 $P_X=\{0.9,0.1\}$，观测到 $y=1$。**ML 准则**只看似然 $Q(y\mid x)$：$0.85>0.15$，判 $x=1$。**MAP 准则**乘上先验：$P(x=1\mid y=1)=0.085/0.22=0.39<0.5$，判 $x=0$。同一份观测、同一条信道，两个准则给出相反答案——差别全在「先验偏置 $\log_2\frac{0.9}{0.1}\approx3.17$ bit 能否压过似然比 $\log_2\frac{0.85}{0.15}\approx2.50$ bit」。抽掉先验这一项，接下来所有以 $I(X;Y)$ 为枢纽的陈述都会失去定义域：capacity 是 $C=\max_{P_X}I(X;Y)$，**最大化就是对先验取**，没有 $P_X$ 连容量都写不出来。

工程含义（真实系统里这条会咬人）：turbo/LDPC 的 APP 解码器最小化的是 bit error rate，那是 MAP 家族；若误把 ML 当最优，在对称信道上恰好同序、看不出问题，一旦信道非对称（擦除、衰落、有记忆）判决就系统性偏移。

挂载：6.042J 的 Bayes 公式与全概率公式（后验 = 似然 × 先验 / 证据）；机器学习的「MAP = ML + 先验（+ 正则）」是同一件事的算法版本。

坐标：§9.4（原书 p.148–149，PDF p.160–161），式 (9.3)(9.4)(9.5)；页边「译本复算」已给出 $0.22$ 与 $0.3864$ 的算术。

```math
P(x = 1 \mid y = 1) = \frac{P(y = 1 \mid x = 1)P(x = 1)}{\sum_{x'} P(y \mid x')P(x')} = \frac{0.85 \times 0.1}{0.85 \times 0.1 + 0.15 \times 0.9} = \frac{0.085}{0.22} = 0.39. \qquad (9.5)
```

> <span style="color:#7f8c8d">译本复算：分母 $P(y = 1) = 0.85 \times 0.1 + 0.15 \times 0.9 = 0.085 + 0.135 = 0.22$；后验 $0.085/0.22 = 0.3864 \simeq 0.39$。注意这个数大于先验 $p_1 = 0.1$ 却仍远小于 $1/2$ —— 因为 $f = 0.15$ 虽小，先验却强烈偏向 0；这正是 §9.4 想让你养成的习惯：**看到输出只是把 belief 往哪边推一点，而不是直接判定输入**。</span>

---

<!-- ===== 译者注 ===== -->

#### <span style="color:#1e8449;">[译注] "信息"为什么不能当集合来数 —— Figure 8.2/8.3 的负面积，与第二编全部定理的唯一引擎（对应 p139–p148）</span>

**机制：抽掉哪一条，整个第二编就崩。**

本块里最容易被当成"记号琐事"跳过的一句，其实是全书的承重墙：$I(X; Y) \equiv H(X) - H(X \mid Y) \ge 0$（式 8.8）。为什么它重要？因为**信道容量**（第 10 章的 channel coding theorem：$R < C(Q)$ 时可任意可靠地传输）的说服力，全部来自「mutual information 是某种可以用一次传输"结算"的量，且它不会为负」这一条。抽掉 $I \ge 0$：capacity 的下界论证立刻失效 —— 你无法再说"接收符号平均而言没有带来负的信息"，也就无法把"可解码"与"信息量"挂上钩，第 11 章 Hamming code 的"每 bit 花多少冗余"的核算也跟着散架。也就是说，$I(X;Y) \ge 0$ 之于第二编，等于"能量守恒"之于力学：不是一条结论，是所有核算的记账规则。

**三种证明，同一个引擎。** 原书给了两条（p.139–140、p.143），加上 §8.4 的 8.9 解答构成第三条，但它们在数学上是同一件事：
- 式 (8.11)：$I(X;Y) = D_{\mathrm{KL}}(P(x,y) \,\|\, P(x)P(y))$，而 relative entropy 非负是 **Gibbs' inequality**（原书 p.44 有证明）。
- 式 (8.30)：直接对 $-\sum P \log \frac{P(x)P(y)}{P(x,y)}$ 用 **Jensen's inequality**（$\log$ 是凹函数）。
- cross-entropy 视角：$-\sum_{x,y} P(x,y)\log P(x)P(y) \ge -\sum P(x,y)\log P(x,y)$，即"用错误的联合分布去算平均码长，一定更长"。

三者的共同内核只有一句话：**$\log$ 的凹性**。这条你已经有的工具（6.041 里 Jensen 用来证 $E[X^2] \ge (E X)^2$；Strang 线代里 $\log\det$ 的凹性带来同样形状的不等式）在这里给出了信息论的"不可能性"半边。

**Venn 图为什么骗人（exercise 8.8 的真正内容）。** 原书说"图 8.1 很重要"，紧接着用一整页说明为什么把它画成圆是误导。机制很清楚：Venn 图的可加性以"集合的测度非负"为前提，而 $H$ 与 $I$ 的可加性只保证某些组合非负。取 exercise 8.8 的 $z = x + y \bmod 2$（$x, y$ 独立）：$I(X;Y) = 0$，但 $I(X; Y \mid Z) = 1$ bit —— 于是图里那块标为 $I(X;Y)$ 的区域必须是 $-1$ bit，等式才配平。这不是构造出来的怪例：**binary symmetric channel 本身就是这个结构**（输入 $X$、噪声 $Y$、输出 $Z$；输入与噪声独立，但一旦看到输出，未知输入与未知噪声就紧密相关）。所以"用集合理解 entropy"只在附加"面积可为负"的告诫后才成立（Yeung, 1991 的 I-measure 正是把这条补丁形式化）。

**落点（可点开）。** 式 8.1–8.12 全在 p.139；Gibbs 的原证明在 p.44（exercise 2.26 之后）；负面积的具体例子是 exercise 8.8（p.141）与其解答（p.143）；同一结构在第 9 章 §9.4 变成 Bayes 后验（式 9.4–9.5，p.148），在第 10 章变成 channel coding theorem 的 $C = \max_{P_X} I(X;Y)$。真实系统里的承重位置：LDPC / Turbo code 的迭代译码器就是在 **belief propagation** 里反复结算 $I(X;Y \mid Z)$ 型的量 —— 若 $I$ 可以为负，"置信度"就没有意义。作为对照的源码级落点：`zlib` 的 Huffman 表构造（`trees.c` 的 `build_tree()`）用的正是"error 越小越好"的同一种记账法，而 error 就是 relative entropy 的估计（Kraft 的等号在此被强制满足，见 exercise 6.22 与第 7 章的 complete code 讨论）。

**L4 你今天能做的一行验证。** 用 exercise 8.6 的表算 $\sum P \log \frac{P(x,y)}{P(x)P(y)}$，应得 $3/8$ bit（原书 p.147 给的 $I(X;Y)$），再用 Jensen 式 (8.30) 从另一侧复算一次 —— 两次都 $= 3/8$，而"Venn 面积"若按字面加减会得到 $0$。这就是那 1/8 与 3/8 之间差别的来源。

（本注中的"三种证明同源"与负面积机制是笔者对原文的整理，不是原书逐字内容；原书分散在 p.44、p.139–140、p.141–143 三处。）


<span style="color:#7f8c8d">书内 p149 ｜ 9.5: Information conveyed by a channel</span>

因此 `x = 1` 仍然比 `x = 0` 更不可能，尽管它已经不像原先那么不可能了。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.2 [1, p.157]</span>

Now assume we observe $y = 0$. Compute the probability of $x = 1$ given $y = 0$.

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.3（例 9.3）</span>

考虑一个 error probability（错误概率）$f = 0.15$ 的 Z channel（Z 信道）。设 input ensemble（输入 ensemble）为 $P_X : \{p_0 = 0.9,\ p_1 = 0.1\}$。假设我们观测到 $y = 1$。

```math
P(x = 1 \mid y = 1) = \frac{0.85 \times 0.1}{0.85 \times 0.1 + 0 \times 0.9} = \frac{0.085}{0.085} = 1.0. \qquad (9.6)
```

于是，给定输出 $y = 1$，我们对输入就变得完全确定。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.4 [1, p.157]</span>

Alternatively, assume we observe $y = 0$. Compute $P(x = 1 \mid y = 0)$.

### 9.5 Information conveyed by a channel（一个信道传递了多少信息）

现在我们来考虑：有多少信息能够通过一个 channel 被传递出去。用 operational（操作式）的说法，我们感兴趣的是找出使用该 channel 的方式，使得所有被传递的 bit 都能以可忽略的 error probability 被恢复出来。用数学的说法，在给定某个 input ensemble $X$ 之后，我们可以用 mutual information（互信息）来度量输出关于输入传递了多少信息：

```math
I(X; Y) \equiv H(X) - H(X \mid Y) = H(Y) - H(Y \mid X). \qquad (9.7)
```

我们的目标是把这两种想法联系起来。让我们对上面几个 channel 计算 $I(X; Y)$。

#### 计算 mutual information 的提示

我们往往会以 $I(X; Y) = H(X) - H(X \mid Y)$ 的形式来思考 $I(X; Y)$，即：当我们观察输出 $Y$ 时，输入 $X$ 的不确定性被减少了多少。但就实际计算而言，改去计算 $H(Y) - H(Y \mid X)$ 通常更方便。

[Figure 9.1：joint information、marginal entropy、conditional entropy 与 mutual entropy 之间的关系图。$H(X)$ 与 $H(Y)$ 两个圆相交，交集为 $I(X; Y)$，各自挖掉交集剩下的部分为 $H(X \mid Y)$ 与 $H(Y \mid X)$，两圆并集为 $H(X, Y)$。原书页边注：「这张图很重要，所以我把它展示两次。」]

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.5（例 9.5）</span>

再次考虑 binary symmetric channel（二进制对称信道），取 $f = 0.15$、$P_X : \{p_0 = 0.9,\ p_1 = 0.1\}$。上面我们已经隐含算出了 marginal probabilities（边缘概率）$P(y)$：$P(y = 0) = 0.78$；$P(y = 1) = 0.22$。mutual information 是：

```math
I(X; Y) = H(Y) - H(Y \mid X).
```


<span style="color:#7f8c8d">书内 p150 ｜ 9 -- Communication over a Noisy Channel</span>

那 $H(Y \mid X)$ 是什么？它按定义是对 $x$ 加权求和 $\sum_x P(x) H(Y \mid x)$；但对每个 $x$ 取值，$H(Y \mid x)$ 都相同：$H(Y \mid x = 0)$ 是 $H_2(0.15)$，$H(Y \mid x = 1)$ 也是 $H_2(0.15)$。所以

```math
I(X; Y) = H(Y) - H(Y \mid X) = H_2(0.22) - H_2(0.15) = 0.76 - 0.61 = 0.15\ \text{bits}. \qquad (9.8)
```

这可以与 source（信源）的 entropy $H(X) = H_2(0.1) = 0.47$ bits 相对照。

注意：这里我们用到了 binary entropy function（二元熵函数）$H_2(p) \equiv H(p, 1-p) = p \log \frac{1}{p} + (1-p)\log \frac{1}{(1-p)}$。在整本书中，$\log$ 一律指 $\log_2$。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.6（例 9.6）</span>

现在换到 Z channel，$P_X$ 同上。$P(y = 1) = 0.085$。

```math
I(X; Y) = H(Y) - H(Y \mid X) = H_2(0.085) - \left[ 0.9\,H_2(0) + 0.1\,H_2(0.15) \right] = 0.42 - (0.1 \times 0.61) = 0.36\ \text{bits}. \qquad (9.9)
```

source 的 entropy 同上，是 $H(X) = 0.47$ bits。请注意：Z channel 的 mutual information $I(X; Y)$ 比同样 $f$ 的 binary symmetric channel 的 mutual information 更大。Z channel 是一个更可靠的 channel。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.7 [1, p.157]</span>

Compute the mutual information between $X$ and $Y$ for the binary symmetric channel with $f = 0.15$ when the input distribution is $P_X = \{p_0 = 0.5,\ p_1 = 0.5\}$.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 9.8 [2, p.157]</span>

Compute the mutual information between $X$ and $Y$ for the Z channel with $f = 0.15$ when the input distribution is $P_X : \{p_0 = 0.5,\ p_1 = 0.5\}$.

#### 最大化 mutual information

在上面的例子里我们观察到：输入与输出之间的 mutual information 依赖于所选的 input ensemble。

让我们假定我们希望通过对 input ensemble 作最优选择，使 channel 所传递的 mutual information 达到最大。我们把 channel 的 capacity（容量）定义为它的最大 mutual information。

channel $Q$ 的 capacity 是：

```math
C(Q) = \max_{P_X} I(X; Y). \qquad (9.10)
```

达到该最大值的分布 $P_X$ 称为 optimal input distribution（最优输入分布），记作 $P_X^*$。[可能存在多个 optimal input distribution 取得相同的 $I(X; Y)$ 值。]

在第 10 章我们将证明：capacity 确实度量了每单位时间能够在该 channel 上无错传输的最大信息量。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 9.9（例 9.9）</span>

考虑 $f = 0.15$ 的 binary symmetric channel。上面我们取 $P_X = \{p_0 = 0.9,\ p_1 = 0.1\}$，得到 $I(X; Y) = 0.15$ bits。
