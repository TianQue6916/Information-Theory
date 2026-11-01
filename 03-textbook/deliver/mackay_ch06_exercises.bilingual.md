# MacKay《Information Theory, Inference, and Learning Algorithms》Ch.06 习题解答双语译注

> 说明：任务标题标注"Ch.06 / 习题 01.x"，但所提供的原书文本实为第 6 章 *Stream Codes*（§6.2 Arithmetic codes），其中仅含两道习题 **Exercise 6.1** 与 **Exercise 6.2**。以下按实际章节编号 6.1、6.2 处理。

---

## Exercise 6.1（习题 6.1）　[2, p.127]

**题干原文：** Show that the overhead required to terminate a message is never more than 2 bits, relative to the ideal message length given the probabilistic model $\mathcal{H}$, $h(x|\mathcal{H}) = \log[1/P(x|\mathcal{H})]$.

**中文：** 证明：相对于由概率模型 $\mathcal{H}$ 给出的理想消息长度 $h(x|\mathcal{H}) = \log[1/P(x|\mathcal{H})]$，终止一条消息所需的开销（overhead）至多不超过 2 bit。

**解答：**

设信源字符串为 $x$，其概率为 $P(x|\mathcal{H})$。算术编码（arithmetic coding）的基本思想是：把每个字符串 $x$ 映射到单位区间 $[0,1)$ 中一个长度为 $P(x|\mathcal{H})$ 的子区间。编码器输出的是一串二进制比特，其对应区间 $[y, y + 2^{-L})$ 必须完全落在 $x$ 的区间内部，其中 $L$ 是编码长度。

（1）首先，理想长度 $h(x|\mathcal{H})=\log_2[1/P(x|\mathcal{H})]$ 一般来说不是整数。若能把消息精确编码成长度为 $h(x|\mathcal{H})$ 的比特串，那当然零开销；但由于比特长度必须取整数，我们实际上需要一个满足

```math
L \le h(x|\mathcal{H}) + 1
```

的整数 $L$。因为只要取 $L = \lceil h(x|\mathcal{H}) \rceil$，就有 $2^{-L} \le P(x|\mathcal{H})$，即区间 $[y, y+2^{-L})$ 的长度不超过 $P(x|\mathcal{H})$，从而可以完全塞进 $x$ 的区间。这一项开销至多 1 bit，来自"取整"。

（2）其次，还有一个更微妙的来源：仅仅输出一个能落在 $x$ 区间内的比特串还不够，解码器（decoder）必须能判断消息在何处**结束**。若编码长度 $L$ 不是事先约定的，解码器无法知道该读到第几位停下来。

处理办法是在编码末尾追加一个"终止"信息。MacKay 在正文中用终止符号 `2`（end-of-message symbol）实现：把 `2` 作为信源字母表里的一个额外符号，其概率 $p_2$ 固定（正文示例取 $p_2 = 0.15$）。这样，终止这件事本身也被纳入概率模型，所需比特数由 $\log_2(1/p_2)$ 决定。

但要给出一个**与模型无关**的上界，可以用如下更直接的论证。取一个最坏情况下的保守处理：编码器在输出比特串后，额外用一段"自定界"（self-delimiting）的编码指明长度 $L$，或者干脆再补足一位。标准结论是——终止消息所需的额外开销**至多 2 bit**，论证分两步：

- **取整开销 ≤ 1 bit**：如上所述，$L = \lceil h(x|\mathcal{H})\rceil$ 与 $h(x|\mathcal{H})$ 之差严格小于 1。
- **终止/定界开销 ≤ 1 bit**：只需再额外付出 1 bit 即可让解码器确定消息已结束。最朴素的方式：编码器把区间进一步收缩到原区间的前半部分（或按某个约定取 $x$ 区间内左端对齐的子区间），并额外输出 1 bit 作为结束标志；或者，把输出比特串保证为"能自定界"的形式。两种构造都能以 1 bit 的成本完成终止。

于是总开销

```math
\Delta L = L - h(x|\mathcal{H}) \le 1 + 1 = 2\ \text{bit}.
```

因此，无论信源字符串 $x$ 具体是什么，算术编码产出的消息长度 $L$ 始终满足

```math
L \le h(x|\mathcal{H}) + 2 = \log_2\frac{1}{P(x|\mathcal{H})} + 2.
```

这正是该重要结论：**算术编码几乎最优**——消息长度始终落在整个信源串 Shannon 信息量（Shannon information content）的 2 bit 之内；取期望后，期望消息长度也落在整个消息熵（entropy）的 2 bit 之内。

> <span style="color:#1e8449;">**[note] 两处开销的区分：**</span> 这一上界来自两个独立来源——(a) 理想长度通常非整数，必须向上取整，代价 <1 bit；(b) 需要向解码器传递"消息已结束"的信息，代价 ≤1 bit。合起来不超过 2 bit。前者是任何整数长度编码都逃不掉的取整误差，后者是流式编码（stream code）特有的定界成本。这也是算术编码相比 Huffman 码（其每符号可能产生接近 1 bit 的开销）的关键优势所在。

---

## Exercise 6.2（习题 6.2）　[3]

**题干原文：** Compare the expected message length when an ASCII file is compressed by the following three methods.

- **Huffman-with-header.** Read the whole file, find the empirical frequency of each symbol, construct a Huffman code for those frequencies, transmit the code by transmitting the lengths of the Huffman codewords, then transmit the file using the Huffman code. (The actual codewords don't need to be transmitted, since we can use a deterministic method for building the tree given the codelengths.)

- **Arithmetic code using the Laplace model.**

```math
P_{\mathrm{L}}(a \mid x_1,\dots,x_{n-1}) = \frac{F_a + 1}{\sum_{a'}(F_{a'} + 1)}.
```

- **Arithmetic code using a Dirichlet model.** This model's predictions are:

```math
P_{\mathrm{D}}(a \mid x_1,\dots,x_{n-1}) = \frac{F_a + \alpha}{\sum_{a'}(F_{a'} + \alpha)},
```

where $\alpha$ is fixed to a number such as $0.01$. A small value of $\alpha$ corresponds to a more responsive version of the Laplace model; the probability over characters is expected to be more nonuniform; $\alpha = 1$ reproduces the Laplace model.

Take care that the header of your Huffman message is self-delimiting. Special cases worth considering are (a) short files with just a few hundred characters; (b) large files in which some characters are never used.

**中文：** 比较以下三种方法压缩一个 ASCII 文件时的期望消息长度。

- **带表头的 Huffman 编码（Huffman-with-header）。** 读取整个文件，统计每个符号的经验频率（empirical frequency），按这些频率构造一个 Huffman 码，把各个 Huffman 码字（codeword）的长度作为码表传输出去，再用这个 Huffman 码传输文件本身。（实际码字无需传输，因为给定各码长后可以用确定性方法重建树。）

- **用 Laplace 模型（Laplace model）的算术编码（arithmetic code）。**

```math
P_{\mathrm{L}}(a \mid x_1,\dots,x_{n-1}) = \frac{F_a + 1}{\sum_{a'}(F_{a'} + 1)}.
```

- **用 Dirichlet 模型（Dirichlet model）的算术编码。** 该模型的预测为：

```math
P_{\mathrm{D}}(a \mid x_1,\dots,x_{n-1}) = \frac{F_a + \alpha}{\sum_{a'}(F_{a'} + \alpha)},
```

其中 $\alpha$ 固定为诸如 $0.01$ 的某个数。较小的 $\alpha$ 对应一个更灵敏（responsive）的 Laplace 模型；字符上的概率分布预期更不均匀（nonuniform）；$\alpha = 1$ 时退化为 Laplace 模型。

注意：你的 Huffman 消息的表头（header）必须是自定界（self-delimiting）的。值得考虑的特殊情形有：(a) 只有几百个字符的短文件；(b) 某些字符从未出现的大文件。

**解答：**

设 ASCII 字母表大小为 $A = 256$，文件长度 $N$，第 $a$ 个符号出现次数为 $F_a$（$\sum_a F_a = N$），其经验频率为 $p_a = F_a / N$。三种方法的期望消息长度分析如下。

---

**（一）Huffman-with-header**

Huffman 编码消息长度由两部分构成：**码表（表头）** + **数据本体**。

数据本体部分：若符号频率分布为 $\{p_a\}$，Huffman 码的期望码长满足

```math
H(\{p_a\}) \le L_{\mathrm{Huff}} < H(\{p_a\}) + 1,
```

其中 $H(\{p_a\}) = -\sum_a p_a \log_2 p_a$ 是信源熵。对整个文件（$N$ 个符号）而言，数据部分长度约为

```math
L_{\mathrm{data}} \approx N \cdot L_{\mathrm{Huff}} \in \big[N H(\{p_a\}),\ N H(\{p_a\}) + N\big).
```

表头部分：需要传输 $A = 256$ 个码长 $\ell_a$。每个码长本身需要自定界编码——直接写二进制会破坏自定界，故常用一种"前缀码长度"编码（如 Elias 码或约定 $0\le\ell_a\le L_{\max}$ 的定长字段）。一个典型且自定界的做法是：为每个符号用固定 $\lceil\log_2(\log_2 A + 1)\rceil$ 位存储其码长（因为对 $A=256$ 个符号，最大码长不超过 $A$，其长度可用 $\lceil\log_2 A\rceil$ 位表示）。故表头开销量级为

```math
L_{\mathrm{header}} = O(A \log A) = 256 \times 8 = 2048\ \text{bit} \quad (\text{量级}).
```

总长度

```math
L_{\mathrm{Huff-total}} = L_{\mathrm{header}} + L_{\mathrm{data}} \approx 2048 + N H(\{p_a\}).
```

**关键结论**：表头成本是**固定开销** $O(A\log A)$，与 $N$ 无关。

- 对**短文件**（$N$ 只有几百）：$L_{\mathrm{header}}$ 与 $L_{\mathrm{data}}$ 同量级甚至更大，Huffman 表现**很差**——表头本身就可能超过原始数据量。
- 对**大文件**：$L_{\mathrm{header}}$ 相对 $N H$ 可忽略，Huffman 渐近达到熵，且没有算术编码那 2 bit 的终止开销。但注意：若某些字符**从未出现**（$F_a=0$），经验频率 $p_a=0$，这些符号不参与 Huffman 树构造，码长 $\ell_a=0$，仍需在表头里标明"此符号未使用"，表头不能因此省略这些位置——这是表头设计必须处理的细节。

---

**（二）Laplace 模型算术编码**

Laplace 模型是加法平滑（add-one smoothing）：

```math
P_{\mathrm{L}}(a \mid \text{history}) = \frac{F_a + 1}{\sum_{a'}(F_{a'} + 1)} = \frac{F_a + 1}{N + A},
```

其中 $F_a$ 是到目前为止 $a$ 的出现次数，$A=256$。算术编码输出长度等于模型分配给整串的概率的负对数：

```math
L_{\mathrm{Lap}} = \log_2 \frac{1}{\prod_{n=1}^{N} P_{\mathrm{L}}(x_n \mid x_1,\dots,x_{n-1})}.
```

按出现计数展开，整串在 Laplace 模型下的概率为

```math
P_{\mathrm{L}}(x) = \prod_{a} \frac{1 \cdot 2 \cdots F_a}{A(A+1)\cdots(A+N-1)} = \frac{\prod_a F_a!}{(A+N-1)!/(A-1)!}.
```

于是

```math
L_{\mathrm{Lap}} = \log_2 \frac{(A+N-1)!}{(A-1)!\prod_a F_a!}.
```

用 Stirling 近似（当 $N$ 大时）可得渐近行为

```math
L_{\mathrm{Lap}} \approx N H(\{p_a\}) + \frac{A-1}{2}\log_2 N + O(1),
```

其中 $p_a = F_a/N$。这里 $\frac{A-1}{2}\log_2 N$ 是**自适应模型（adaptive model）学习分布所付出的代价**——模型一开始不知道符号频率，需要"现场学习"。

- 对**短文件**：Laplace 无需表头，起手就是零固定成本，通常**优于** Huffman-with-header（后者要背 $O(A\log A)$ 的表头）。
- 对**大文件**：Laplace 有 $\frac{A-1}{2}\log_2 N$ 的"学习开销"，且当某些符号从未出现时，Laplace 仍给每个未见符号保留 $1/(N+A)$ 的概率（永远不会为零），对高熵、分布近乎均匀的大文件尚可，但对分布**高度集中**（很多符号从不出现）的文件，这些"白给的"非零概率会带来可观的额外代价——正是下一方法要解决的问题。

---

**（三）Dirichlet 模型算术编码**

Dirichlet 模型用 $\alpha$ 代替 Laplace 的加 1：

```math
P_{\mathrm{D}}(a \mid \text{history}) = \frac{F_a + \alpha}{\sum_{a'}(F_{a'} + \alpha)} = \frac{F_a + \alpha}{N + \alpha A}.
```

当 $\alpha$ 取很小值（如 $0.01$）时，未出现过的符号被赋予的概率 $\alpha/(N+\alpha A)$ 远小于 Laplace 情形下的 $1/(N+A)$。整串概率为

```math
P_{\mathrm{D}}(x) = \prod_a \frac{\alpha(\alpha+1)\cdots(\alpha+F_a-1)}{(\alpha A)(\alpha A + 1)\cdots(\alpha A + N - 1)},
```

编码长度

```math
L_{\mathrm{Dir}} = \log_2 \frac{1}{P_{\mathrm{D}}(x)}.
```

用渐近展开（对小的 $\alpha$ 与大的 $N$），当分布集中、多数符号 $F_a=0$ 时：

```math
L_{\mathrm{Dir}} \approx N H(\{p_a\}) + \frac{|\mathcal{S}|-1}{2}\log_2 N + O(1),
```

其中 $|\mathcal{S}|$ 是**实际出现过的**符号种类数，而非整个字母表大小 $A$。这正是 Dirichlet 模型相对 Laplace 的优势：**学习代价只与"实际用到的符号数"成正比**，而不是与整个字母表 $A$ 成正比。

对"某些字符从未使用"的大文件（题干情形 b）：$|\mathcal{S}|\ll A$，此时

```math
L_{\mathrm{Dir}} \approx N H(\{p_a\}) + \frac{|\mathcal{S}|-1}{2}\log_2 N \ll L_{\mathrm{Lap}} \approx N H + \frac{A-1}{2}\log_2 N,
```

Dirichlet 模型显著优于 Laplace 模型。而对短文件或分布接近均匀的文件，两者差距不大；$\alpha=1$ 时 Dirichlet 恰还原为 Laplace。

---

**（四）综合对比**

| 方法 | 表头开销 | 学习/冗余开销 | 短文件 | 大文件（部分符号未用） |
|------|----------|---------------|--------|------------------------|
| Huffman-with-header | $O(A\log A)$ 固定 | 每符号 <1 bit（取整） | 差（表头占比大） | 好（渐近达到熵） |
| Laplace 算术 | 无 | $\frac{A-1}{2}\log_2 N$ | 好 | 一般（被未用符号拖累） |
| Dirichlet 算术 | 无 | $\frac{|\mathcal{S}|-1}{2}\log_2 N$ | 好 | 最好（只按实际符号计） |

**结论：**

- **短文件**（几百字符）：算术编码（Laplace 或 Dirichlet）优于 Huffman-with-header，因为省去了 $O(A\log A)$ 的表头。
- **大文件且分布较均匀**：三种方法渐近都接近熵，Huffman 略优（无 2 bit 终止开销），但差距微小。
- **大文件且部分字符从未出现**：Dirichlet 模型算术编码明显最优，因其自适应代价只随实际出现的符号数增长；Laplace 模型会被从未出现的符号"白分"概率而拖累；Huffman 则需在表头里仍处理全部 $A$ 个符号的码长。

> <span style="color:#1e8449;">**[note] 平滑参数 α 的本质：**</span> $\alpha$ 是 Dirichlet 先验（prior）中的伪计数（pseudo-count），控制模型对"未见符号"的信任程度。$\alpha=1$ 对应 Laplace（均匀 Dirichlet 先验），对所有符号一视同仁；$\alpha\to 0$ 对应一个"相信分布高度集中"的先验，几乎不给未出现的符号留概率，因此对稀疏分布（sparse distribution）的文件压缩更优，代价是万一出现真正的罕见符号时会付出较大码长。这正是"偏差—方差"在压缩中的体现：小 $\alpha$ 偏差小但适应慢，大 $\alpha$ 稳健但冗余高。
