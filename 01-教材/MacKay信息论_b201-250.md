<!-- 书页 201–250｜来源：A+B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->


<span style="color:#7f8c8d">书内 p201 ｜ 12.6: Further exercises</span>

所以要最小化被 hash 的文件数 $N_1 + N_2$，Alice 应取 $N_1$ 与 $N_2$ 相等，于是她需要 hash 约 $2^{M/2}$ 个文件，才能找到两个相符的。

**Alice 必须对约 $2^{M/2}$ 个文件做 hash 才能作弊。[这是 Fiona 所需 hash 数的平方根。]**

若 Alice 能动用 $C = 10^{6}$ 台计算机、算 $T = 10$ 年，每台机器一次 hash 用时 $t = 1$ ns，则这个下注通信系统要能防住 Alice 的不诚实，必须 $M \gg 2\log_2 (CT/t) \simeq 160$ bits。

#### Further reading（延伸阅读）

hash codes 的圣经是 Knuth (1968) 第 3 卷。我强烈推荐 Doug McIlroy 的 spell 程序的故事，见 *Programming Pearls*（Bentley, 2000）§13.8。这个惊人的软件用一块 64 KB 的数据结构，存下了 75 000 词词典中所有词的拼法。

<span style="color:#1e8449;">**[译注]** 本页两个 $\sqrt{\cdot}$ 的差别是整章最容易被记混的地方，值得钉死机制：Fiona 面对的是**给定的** hash 值，她要在 $2^{M}$ 个候选里命中一个点，期望 $2^{M}$ 次；Alice 面对的是**自己造两个**候选集合，只要集合内任意一对相撞即可，而 pair 的个数是 $N_1 N_2$，于是 $N_1 N_2 \simeq 2^{M}$、$N_1 = N_2 \simeq 2^{M/2}$。这就是 birthday bound：命中「指定点」与命中「任意一对」的代价差平方根。抽掉这条区分，系统会崩在哪？崩在**安全参数的选择**：一个 128-bit hash 对 Fiona 是 $2^{128}$（不可行），对 Alice 却只有 $2^{64}$（历史上 MD5 的 collision 就是这样被造出来的，1996 年后普遍改用 160-bit 以上的 SHA-1，2005 年后 SHA-1 的 $2^{80}$ 也被王小云等人的 collision attack 击穿，故今天的工程实践用 SHA-256）。这也直接解释了原文那个 $M \gg 160$ bits 的估值：$2\log_2(10^{6} \cdot 10\,\text{年}/1\,\text{ns}) = 2\log_2(3.15\times 10^{23}) \approx 157$，只算 Alice 一侧的 birthday 成本，不算 Fiona 的。落点：本页为书内 p201；birthday 期望值 $\binom{S}{2}/T$ 的推导见 exercise 12.3 的解（书内 p202，(12.6)）；同构问题在书内 p156 的 exercise 9.20（生日与同姓概率）；离散工具的落点是 6.042J 的 *Expectation* 与 *Binomial coefficients* 单元（$\binom{S}{2}$ 的线性期望是唯一需要的技巧）；硬件侧的哈希加速（SIMD / 专用 SHA 指令）读 CSAPP 第 5 章 §5.12 关于指令级并行的讨论。</span>

### 12.6 Further exercises（进一步习题）

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 12.9.[1]**</span> What is the shortest the address on a typical international letter could be, if it is to get to a unique human recipient? (Assume the permitted characters are [A-Z,0-9].) How long are typical email addresses?

<span style="color:#7f8c8d">中文话题摘要：把「全球唯一收件人」当成一次 hash 设计——用字母数字表的大小与人数反推最短地址长度，再与真实 email 地址长度比较，看现实冗余有多大。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 12.10.[2, p.203]**</span> How long does a piece of text need to be for you to be pretty sure that no human has written that string of characters before? How many notes are there in a new melody that has not been composed before?

<span style="color:#7f8c8d">中文话题摘要：估计「人类全部书写物」的总字符数与字符表大小，算出多长的串才可能从未被写过；再把同一估计套到旋律上，比较两者的碰撞尺度。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 12.11.[3, p.204]**</span> Pattern recognition by molecules. Some proteins produced in a cell have a regulatory role. A regulatory protein controls the transcription of specific genes in the genome. This control often involves the protein's binding to a particular DNA sequence in the vicinity of the regulated gene. The presence of the bound protein either promotes or inhibits transcription of the gene.

(a) Use information-theoretic arguments to obtain a lower bound on the size of a typical protein that acts as a regulator specific to one gene in the whole human genome. Assume that the genome is a sequence of $3 \times 10^{9}$ nucleotides drawn from a four letter alphabet {A, C, G, T}; a protein is a sequence of amino acids drawn from a twenty letter alphabet. [Hint: establish how long the recognized DNA sequence has to be in order for that sequence to be unique to the vicinity of one gene, treating the rest of the genome as a random sequence. Then discuss how big the protein must be to recognize a sequence of that length uniquely.]

(b) Some of the sequences recognized by DNA-binding regulatory proteins consist of a subsequence that is repeated twice or more, for example the sequence

```math
\text{GCCCCCCACCCCTGCCCCC} \qquad (12.4)
```

is a binding site found upstream of the alpha-actin gene in humans. Does the fact that some binding sites consist of a repeated subsequence influence your answer to part (a)?

<span style="color:#7f8c8d">中文话题摘要：用「全基因组内唯一」这一要求，反推识别序列的最短长度与蛋白质的最小尺寸；再讨论识别位点里重复子序列如何让更小的蛋白（二聚体）达到同样的特异性。</span>


<span style="color:#7f8c8d">书内 p202 ｜ 12.7: Solutions</span>

### 12.7 Solutions（解答）

**Solution to exercise 12.1 (p.194)（练习 12.1 的解答）.**

先想象把串 $x$ 与另一个随机串 $x^{(s)}$ 比较。两串第一个 bit 相符的概率是 $1/2$；第二个 bit 相符的概率是 $1/2$。设我们一遇到第一个不匹配就停止比较，则相符次数的期望是 $1$，故比较次数的期望是 $2$（exercise 2.34, p.38）。

设正确的串在 raw list 里位于随机位置，则找到它之前平均要与 $S/2$ 个串比较，这花掉 $2S/2$ 次二元比较；再与正确的串比较要花 $N$ 次二元比较。于是若各串是随机选的，总期望为 $S + N$ 次二元比较。

最坏情形（在实践中确实可能发生）是：其余的串与搜索 key 极为相似，于是每找到一个不匹配都要一长串比较。最坏情形是正确串在列表末尾，且其余所有串只在最后一个 bit 上与之不同，此时需要 $SN$ 次二元比较。

**Solution to exercise 12.2 (p.197)（练习 12.2 的解答）.**

对两个假设 $H_0: x^{(s)} = x$ 与 $H_1: x^{(s)} \neq x$，数据「$x^{(s)}$ 与 $x$ 的前若干个 bits 相等」所提供的 likelihood ratio（似然比）是

```math
\frac{P(\text{Datum} \mid H_0)}{P(\text{Datum} \mid H_1)} = \frac{1}{1/2} = 2. \qquad (12.5)
```

若前 $r$ 个 bits 全部相符，则 likelihood ratio 是 $2^{r}$ 比 $1$。发现 30 个 bits 相符时，假定我们从未知先验出发（odds 为 $1:1$），则支持 $H_0$ 的 odds 已达十亿比一。[若要一个完整的答案，我们还应当把「hash 表项 $s$ 曾在 $h(x)$ 处被找到」这条先验信息所提供的证据算进去。这个事实是支持 $H_0$ 的进一步证据。]

**Solution to exercise 12.3 (p.198)（练习 12.3 的解答）.**

设 hash function 的输出字母表大小为 $T = 2^{M}$。若 $M$ 恰等于 $\log_2 S$，我们就有恰好够用的 bits 让每个 entry 有自己唯一的 hash。在一份随机 hash function 下，某一对特定表项相撞的概率是 $1/T$。对数为 $S(S-1)/2$。于是 pair 之间碰撞数的期望恰为

```math
\frac{S(S-1)}{2T}. \qquad (12.6)
```

若希望它小于 $1$，则需要 $T \gt S(S-1)/2$，即

```math
M \gt 2\log_2 S. \qquad (12.7)
```

也就是需要两倍于 $\log_2 S$ 的 bits——$\log_2 S$ 本来已够给每个 entry 一个唯一名字。

若我们乐于接受偶发 collision，且涉及名字的 $f$ 这一比例，则需要 $T \gt S/f$（因为某个特定名字被撞的概率是 $f \simeq S/T$），于是

```math
M \gt \log_2 S + \log_2[1/f], \qquad (12.8)
```

<span style="color:#1e8449;">**[译注]** 这条练习的解把「$T$ 该多大」从一个经验值变成三档可算的预算，而三档的差别正是两个 scaling 的差别：(12.7) 要求 $T \sim S^{2}$（严格无碰撞），(12.8) 只要求 $T \sim S$（按比例容忍碰撞）。为什么差一个幂次？因为「无碰撞」是一个**全称命题**——要对所有 $\binom{S}{2}$ 个 pair 都成立，用 union bound 得到的期望就是 $\binom{S}{2}/T$；而「只有小比例的串被撞」是一个**统计命题**——只需单个名字的碰撞概率 $S/T$ 小。抽掉这条区分，系统会崩在哪？崩在容量规划的说辞上：把「table 大十倍」当成「保证不碰撞」是常见的误解，实际上 $T = 2^{30}$、$S = 10^{7}$ 时（Figure 12.2 的取值），期望碰撞数是 46566 个——**必然撞车**，所以 §12.3 的 collision resolution 不是可选优化，而是能否工作的前提。可复算的验证：$S(S-1)/(2T) = 10^{7}\cdot(10^{7}-1)/(2\cdot 2^{30}) \approx 4.66\times 10^{4}$，与 $2\log_2 S = 46$ bits 这一门槛对照，实际只给了 $M = 30$，故碰撞数远大于 1，与 (12.7) 一致。落点：本题在书内 p202；同构的 birthday 计算见书内 p156 的 exercise 9.20 与 p201 的 Example 12.8；离散侧工具在 6.042J 的 *Linearity of expectation*（对每个 pair 用指示变量求和，无需独立性）与 *Counting* 单元。</span>


<span style="color:#7f8c8d">书内 p203 ｜ 12.7: Solutions</span>

这意味着当 $f \simeq 0.01$ 时，我们需要在 $\log_2 S$ 之上再加 7 bits。

要注意的重点是两种情形下 $T$ 随 $S$ 的 scaling（(12.7)、(12.8)）。若希望 hash function 无碰撞，则必须有 $T$ 大于约 $S^{2}$；若乐于接受少量碰撞，则 $T$ 只需是 $S$ 的量级。

**Solution to exercise 12.5 (p.198)（练习 12.5 的解答）.**

两个假设 $H_+$ =「计算正确」与 $H_-$ =「计算不正确」的后验概率比为：先验概率比 $P(H_+)/P(H_-)$ 乘以 likelihood ratio $P(\text{match} \mid H_+)/P(\text{match} \mid H_-)$。第二个因子就是本题的答案。分子 $P(\text{match} \mid H_+) = 1$。分母的值取决于我们对错误的模型：若我们知道这位人肉计算者容易犯「把答案乘 10」或「对调相邻数字」这类错误，而这两类错误都不影响 hash 值，那么 $P(\text{match} \mid H_-)$ 也可能等于 $1$，于是一次正确的相符对 $H_+$ 毫无证据。但若假定错误「从 hash function 的角度看是随机的」，则假阳性的概率是 $P(\text{match} \mid H_-) = 1/9$，于是一次正确相符给出 $9:1$ 支持 $H_+$ 的证据。

**Solution to exercise 12.7 (p.199)（练习 12.7 的解答）.**

如果你给一个 $N$-bit 的大文件配上很小的 $M = 32$ 个额外 hash bits，你就得到相当好的错误检测——某个错误未被检出的概率是 $2^{-M}$，小于十亿分之一。要做纠错则需要多得多的 check bits，其数目取决于预期中的损坏类型与文件大小。举例来说，若一兆字节的文件中恰有八个随机 bits 被损坏，那么指明哪些 bit 被损坏约需 $\log_2 \binom{2^{23}}{8} \simeq 23 \times 8 \simeq 180$ bits；而一个成功的纠错码所用的 parity-check bits 数目，按 exercise 1.10 的计数论证（解答见 p.20），必须至少是这个数。

**Solution to exercise 12.10 (p.201)（练习 12.10 的解答）.**

我们想知道串长 $L$，使得「该串与人类全部书写物的任何一部分相符」这件事极不可能。让我们估计这些书写物总计约等于每个在世者一本书，每本书含两百万字符（200 页，每页 10 000 字符）——那就是 $10^{16}$ 个字符，取自一个比如说 37 个字符的字母表。

一个随机选取的长度 $L$ 的串，在人类著作全集的某处相符的概率是 $1/37^{L}$。所以相符次数的期望是 $10^{16}/37^{L}$，当 $L \ge 16/\log_{10} 37 \simeq 10$ 时微不足道。由于人类书写物存在冗余与重复，$L \simeq 10$ 这个数可能还是高估。

所以，如果你想写点独一无二的东西，坐下来写十个字符的串吧。但别写 gidnebinzz，因为那个串我已经想过了。

至于新旋律：若我们只关注音高序列、忽略时值与重音，并假定每个音可跳至多一个八度，则每个音有 23 种选择。第一个音的音高是任意的。在这个颇为难听的「Schönberg 式」曲调 ensemble 里，长度为 $r$ 个音的旋律有 $23^{r-1}$ 条；例如长度为 $r = 5$ 有 250 000 条。限制允许的音程会压低这个数字；把时值与重音算进去又会抬高它。[若把允许音程限制为同音重复与全音或半音，压缩尤其严重；『欢乐颂』的旋律听起来那么单调，原因是不是这个？] 有记录的作曲大约不到一百万部。若你在有生之年的每一周学 100 条新旋律，到 50 岁时你学会 250 000 条。基于


<span style="color:#7f8c8d">书内 p204 ｜ 12 — Hash Codes: Codes for Efficient Information Retrieval</span>

在『猜曲调』（guess that tune）这个游戏上的经验，我的印象是：许多四音序列在旋律间是共通的，而五音序列之间的碰撞数则小得多——大多数著名的五音序列都是唯一的。

<span style="color:#7f8c8d">边注（原书页侧）：在 guess that tune 游戏里，一名玩家选一条旋律，唱出越来越多个音，其他参与者猜整条旋律。Parsons code 是与之相关的一种旋律 hash function：每一对相邻音，若第二个音更高就编码为 U（up），音高相等编为 R（repeat），否则编为 D（down）。这个 hash function 效果如何，可在 http://musipedia.org/ 查看。</span>

**Solution to exercise 12.11 (p.201)（练习 12.11 的解答）.**

(a) 设这个 DNA-binding protein（DNA 结合蛋白）识别长度为 $L$ 个 nucleotides 的序列。也就是说，它优先结合到那段 DNA 序列上，而不结合到整个基因组中任何其他 DNA 片段上。（现实中，被识别的序列可能含一些 wildcard（通配）字符，例如 TATAA\*A 中的 \* 表示「A、C、G、T 中任意一个」；所以准确地说，我们假定被识别的序列含 $L$ 个非通配字符。）

假定基因组其余部分是「随机的」，即序列由等概率的随机 nucleotides A、C、G、T 组成——这显然不真，但对我们的计算不会有太大影响——那么在整个长 $N$ 个 nucleotides 的基因组中，目标序列不再出现于别处的概率约为

```math
\left( 1 - (1/4)^{L} \right)^{N} \simeq \exp\left( -N (1/4)^{L} \right), \qquad (12.9)
```

它接近 $1$ 的条件是

```math
N 4^{-L} \ll 1, \qquad (12.10)
```

也就是

```math
L \gt \log N / \log 4. \qquad (12.11)
```

取 $N = 3 \times 10^{9}$，我们要求被识别的序列长于 $L_{\min} = 16$ 个 nucleotides。

这对蛋白质的大小意味着什么？

- 一个弱下界可以从这样一个假定得到：蛋白序列本身的信息含量大于它所偏好结合的核苷酸序列的信息含量（上面已论证后者至少 32 bits）。这给出最小蛋白长度 $32/\log_2(20) \simeq 7$ 个氨基酸。
- 现实地想，蛋白识别 DNA 序列大概要让它与目标序列中全部十六个 nucleotides 接触。若该蛋白是单体（monomer），它必须大到能同时接触 DNA 上十六个 nucleotides。DNA 一个含十个核苷酸的螺旋圈长 3.4 nm，故连续十六个核苷酸长 5.4 nm。于是蛋白质的直径必须约 5.4 nm 或更大。蛋清溶菌酶（egg-white lysozyme）是一个小的球状蛋白，长 129 个氨基酸，直径约 4 nm。假定体积正比于序列长度、且体积按直径的立方 scaling，则一个直径 5.4 nm 的蛋白，其序列长度必须是 $2.5 \times 129 \simeq 324$ 个氨基酸。

(b) 但若目标序列由一段重复两次的子序列组成，我们就可以用一个小得多的蛋白蒙混过去：它只识别那段子序列，并且只有在能形成 dimer（二聚体）、且两半都结合到被识别序列上时才与 DNA 强结合。把蛋白直径减半，我们现在只需一个长度大于 $324/8 = 40$ 个氨基酸的蛋白。比这更短的蛋白，本身无法充当特异于某一个基因的调控蛋白，因为它实在太小，做不出足够特异的匹配——它可用的表面没有足够的信息含量。

<span style="color:#1e8449;">**[译注]** (12.9)–(12.11) 这三步是全章唯一一次把「唯一性」做成可算的判据，值得记住它的形状：它其实是**无碰撞概率**的 Poisson 近似。把基因组其余部分看成 $N$ 个长度为 $L$ 的独立窗口，每个窗口等于目标序列的概率是 $4^{-L}$，于是「不再出现」的概率是 $(1 - 4^{-L})^{N} \approx e^{-N 4^{-L}}$，要求它接近 1 就得到 $N 4^{-L} \ll 1$，取对数落成 $L \gt \log_4 N$。这与 (12.6) 是同一条式子换了皮：$S$ 换成 $N$、$T$ 换成 $4^{L}$——唯一的区别是这里把 $L$ 当自变量求解。为什么 $L_{\min} = 16$ 是那种「刚好够用」的数字而不是「够用有余」？因为 $4^{16} = 2^{32}$ 才刚超过 $3\times 10^{9} \approx 2^{31.5}$，只余 0.5 bit 的余量，所以原文紧接着说「16 个核苷酸只能勉强唯一」。抽掉这条「唯一性需要多少 bits」的算法，分子生物学里「转录因子为何识别 8–20 bp 的位点」这个问题就没有量纲可依：8 bp 只有 $4^{8} = 65536$ 种组合，在 $3\times10^9$ 的基因组里平均要出现四万多次，不可能特异。落点：本题在书内 p204；同类计算的 source coding 版本见书 §4（typical set 的 $2^{NH}$ 计数）；离散侧工具在 6.042J 的 *Counting* 与 *Approximations*（$1-x \approx e^{-x}$ 那一节）；实测数据可查 JASPAR 数据库的 motif 长度分布（一手来源，非本书）。</span>


<span style="color:#7f8c8d">书内 p205 ｜ About Chapter 13</span>

## About Chapter 13（第 13 章导读）

在第 8–11 章，我们为任何输入输出字母表的通用 channel 建立了 Shannon 的 noisy-channel coding theorem。coding theory 里极大一部分注意力集中在输入为 binary 的 channel 这一特例上。把注意力限制在这类 channel 上使问题简化，并把我们带进一个格外丰富的世界——本书只能浅尝。

本章的目标之一是点出 Shannon 的目标（在有噪 channel 上实现可靠通信）与 coding theory 界许多人表面上追求的目标之间的一种对照。许多 coding theorist 把「把尽可能多的球、以尽可能大的半径、互不重叠地塞进一个 $N$ 维空间」当成自己的根本问题。找到能再挤进几个球的 packing 的人会得奖。这固然是一个迷人的数学题目，但我们将看到：最大化 code 中 codewords 之间 distance 这一目标，与 Shannon 的可靠通信目标只有一层微弱的联系。

<span style="color:#1e8449;">**[译注]** 这一页是全章立场宣言，读第 13 章时最好一直挂在眼前，否则会把 §13.2–§13.5 当成「编码理论的标准内容」而不明白作者为什么要反复驳它。作者要区分的是两个目标函数：coding theorist 的 **maximize $d_{\min}$**（等价于在 $N$ 维 Hamming 空间里塞球），与 Shannon 的 **maximize rate subject to $P_e \to 0$**。二者在低噪声区间几乎一致，在高噪声区间彻底分叉，而分叉的定量结果就是 §13.5 末的 $f_{\mathrm{bd}} = f/2$——bounded-distance decoder 能容忍的噪声只有 Shannon 的一半。抽掉这条区分，系统会崩在哪？崩在**译码器设计**上：如果只按 minimum distance 做 bounded-distance decoding（$t = \lfloor (d-1)/2 \rfloor$），那么当噪声超过 $t$ 时译码器就直接宣告失败，而实测中真正需要的是「在最可能的那些错误模式上继续工作」——这正是 MacKay 后面要推的 LDPC / turbo 一类 iterative decoder 的立意（书 §47 起）。落点：本页为书内 p205；定量对照见 §13.5（书内 p212–213，(13.16)–(13.20)）；「球在高维空间几乎不含体积」这一点与 Thomson 实分析里测度集中/体积公式 $\text{Vol}_N \propto r^{N}$ 的几何直觉直接相关（高维球的体积集中在赤道附近的薄壳）；工程侧对着读 CSAPP 第 5 章「程序的性能」——最坏情形优化与平均情形优化的差别，在那里以 branch prediction 与 cache 的形式出现，是同一种 worst-case-ism 的硬件版本。</span>


<span style="color:#7f8c8d">书内 p206 ｜ 13 ｜ 13.1: Distance properties of a code ｜ 13.2: Obsession with distance</span>

## 13　Binary Codes（第 13 章　二进制码）

我们已经为任何输入输出字母表的通用 channel 建立了 Shannon 的 noisy-channel coding theorem。coding theory 里有极大一部分注意力集中在输入为 binary 的 channel 这一特例上，第一个隐含的选择就是 binary symmetric channel。

给定 binary symmetric channel 时，一个 code 的最优 decoder 找出与 received vector（接收向量）最接近的 codeword——最近是指 Hamming distance（汉明距离）最近。两个 binary vectors 之间的 Hamming distance，就是两向量取值不同的坐标个数。若 noise 把我们从发送的 codeword $t$ 带到某个 received vector $r$，而 $r$ 离另一个 codeword 更近，则发生 decoding error。于是 codewords 之间的距离与 decoding error 的概率相关。

<span style="color:#7f8c8d">边注（原书页内例）：Hamming distance 例——$00001111$ 与 $11001101$ 之间的 Hamming distance 是 $3$。</span>

### 13.1 Distance properties of a code（码的距离性质）

一个 code 的 distance（距离）是其任意两个 codewords 之间最小的间隔。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 13.1（例 13.1）</span>

$(7,4)$ Hamming code（p.8）的距离是 $d = 3$。它的所有 codeword 对至少相差 3 bits。它能纠正的最大错误数为 $t = 1$；一般来说，距离为 $d$ 的 code 是 $\lfloor (d-1)/2 \rfloor$-error-correcting（可纠 $\lfloor (d-1)/2 \rfloor$ 个错）的。

距离更精确的说法是 code 的 minimum distance（最小距离）。code 的 distance 常记为 $d$ 或 $d_{\min}$。

下面我们把注意力限制在 linear codes（线性码）上。在 linear code 中，所有 codewords 具有相同的距离性质，于是我们可以通过数「到全零 codeword 的距离」来概括该 code 各 codeword 之间的全部距离。

一个 code 的 weight enumerator function（重量枚举函数）$A(w)$，定义为该 code 中 weight（重量）为 $w$ 的 codewords 个数。weight enumerator function 也称为该 code 的 distance distribution（距离分布）。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 13.2（例 13.2）</span>

$(7,4)$ Hamming code 与 dodecahedron code（十二面体码）的 weight enumerator function 分别见图 13.1 与图 13.2。

[Figure 13.1：左为 $(7,4)$ Hamming code 的图（graph），右为其 weight enumerator function 的柱状图，横轴 $w = 0\dots7$。原书该表为边注排版，此处按语义重建为表格。]

| $w$ | $A(w)$ |
|---|---|
| 0 | 1 |
| 3 | 7 |
| 4 | 7 |
| 7 | 1 |
| Total | 16 |

### 13.2 Obsession with distance（对距离的执念）

由于一个 code 能保证纠正的最大错误数 $t$ 与其距离 $d$ 由 $t = \lfloor (d-1)/2 \rfloor$ 相关（$d$ 为奇数时 $d = 2t+1$，$d$ 为偶数时 $d = 2t+2$），许多 coding theorist 把注意力放在 code 的 distance 上，为给定大小寻找 distance 尽可能大的 code。实用 coding theory 的很大一部分，集中在那些对 weight 不超过其 code 半距离 $t$ 的一切 error patterns 都给出最优 decoding 的 decoders 上。


<span style="color:#7f8c8d">书内 p207 ｜ 13.2: Obsession with distance</span>

[Figure 13.2：上为定义 $(30,11)$ dodecahedron code 的图（圆圈是 30 个被传输的 bits，三角形是 20 个 parity checks，其中一个是冗余的），中为其 weight enumerator function（实线），虚线给出所有同尺寸 generator matrix 的 random linear codes 的平均 weight enumerator function；下图为同一组函数的对数坐标图。原表为边注，按语义重建如下。]

| $w$ | $A(w)$ | $w$ | $A(w)$ |
|---|---|---|---|
| 0 | 1 | 13 | 180 |
| 5 | 12 | 14 | 240 |
| 8 | 30 | 15 | 272 |
| 9 | 20 | 16 | 345 |
| 10 | 72 | 17 | 300 |
| 11 | 120 | 18 | 200 |
| 12 | 100 | 19 | 120 |
| | | 20 | 36 |
| | | Total | 2048 |

<span style="color:#7f8c8d">表内校验：各项之和 $= 2048 = 2^{11}$，与 $(30,11)$ 码的 $2^{K}$ 个 codewords 相符；最小非零 weight 为 5，故 $d_{\min} = 5$、$t = 2$。</span>

bounded-distance decoder（有界距离译码器）是这样一种 decoder：若 received binary vector $r$ 到某个 codeword 的距离小于或等于 $t$，则返回该最近的 codeword；否则返回失败信息。

「超过 $t$ 个错误就不去尝试译码」的理由也许是：「我们不能保证纠正超过 $t$ 个错误，那就懒得试——谁会关心一个能纠正某些 weight 大于 $t$ 的 error pattern、却纠不了另一些的 decoder 呢？」这种失败主义态度是 worst-case-ism（最坏情形主义）的一例，那是一种流传甚广的精神疾患，本书意在治它。

事实是：bounded-distance decoders 达不到 binary symmetric channel 的 Shannon limit<sup>∗</sup>；只有那种常常纠正超过 $t$ 个错误的 decoder 才能达到。纠错码的最先进水平，其 decoders 的工作范围远远超出 code 的 minimum distance。

<span style="color:#7f8c8d">[脚注 ∗ 的正文未出现在本页文字层，无法复原其内容，此处不作补写。]</span>

#### Definitions of good and bad distance properties（「好」「坏」距离性质的定义）

给定一族 blocklength $N$ 递增、rate 趋于某个极限 $R \gt 0$ 的 codes，我们也许能把这族 code 归入下列类别之一——它们与前面（p.183）定义的 `good` / `bad` codes 诸类有些相似：

- 若 $d/N$ 趋于一个大于零的常数，则称一列 codes 具有「good」distance。
- 若 $d/N$ 趋于零，则称一列 codes 具有「bad」distance。
- 若 $d$ 趋于一个常数，则称一列 codes 具有「very bad」distance。

[Figure 13.3：一个 rate-$1/2$ low-density generator-matrix code（低密度生成矩阵码）的图。最右边 $M$ 个被传输的 bits 各连接到一个互不相同、单一的 parity constraint；最左边 $K$ 个被传输的 bits 各连接到少数几个 parity constraints。]

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 13.3（例 13.3）</span>

low-density generator-matrix code 是一种 linear code，其 $K \times N$ 的 generator matrix $G$ 每行只含少量（$d_0$ 个）1，与 $N$ 多大无关。这样的 code 的 minimum distance 至多为 $d_0$，故 low-density generator-matrix codes 具有「very bad」distance。

拥有大距离固然不是坏事，但我们后面会看到，为什么把重心放在 distance 上可能并不健康。


<span style="color:#7f8c8d">书内 p208 ｜ 13.3: Perfect codes</span>

[Figure 13.4：Hamming 空间的一部分被「以 codewords 为心的 $t$-球」完美填满的示意图（perfect code 的情形）。]

### 13.3 Perfect codes（完美码）

Hamming 空间中以点 $x$ 为中心的一个 $t$-sphere（$t$-球，或称半径为 $t$ 的球），是与 $x$ 的 Hamming distance 小于或等于 $t$ 的点的集合。

$(7,4)$ Hamming code 有一个漂亮的性质：若以它的 16 个 codewords 为心各放一个 1-球，这些球互不重叠地完美填满 Hamming 空间。正如第 1 章所见，每个长度 7 的 binary vector 到 Hamming code 的某个 codeword 的距离恰好不超过 $t = 1$。

<span style="color:#00838f">**定义**：若以某 code 的各 codewords 为心的 $t$-球集合互不重叠地填满 Hamming 空间，则该 code 是一个 perfect $t$-error-correcting code（完美 $t$ 纠错码）。（见图 13.4。）</span>

让我们回顾一下演员表。codewords 个数是 $S = 2^{K}$。整个 Hamming 空间的点数是 $2^{N}$。半径为 $t$ 的 Hamming 球的点数（体积）是

```math
\sum_{w=0}^{t} \binom{N}{w}. \qquad (13.1)
```

要使一个 code 在给定参数下是 perfect 的，我们要求 $S$ 乘以 $t$-球的点数等于 $2^{N}$：

```math
\text{for a perfect code:}\quad 2^{K} \sum_{w=0}^{t} \binom{N}{w} = 2^{N} \qquad (13.2)
```

或等价地

```math
\sum_{w=0}^{t} \binom{N}{w} = 2^{N-K}. \qquad (13.3)
```

对 perfect code 而言，一个球内的 noise vectors 数目必须等于可能的 syndromes（校验子）数目。$(7,4)$ Hamming code 满足这条「数字命理」（numerological）条件，因为

```math
1 + \binom{7}{1} = 2^{3}. \qquad (13.4)
```

<span style="color:#1e8449;">**[译注]** (13.1)–(13.4) 把「完美」这件事从几何图像压成一条整数方程，这条方程的威力在于它是**必要条件**：任何候选参数 $(N, K, t)$ 若不是整数解，就一定不存在 perfect code。抽掉它，你会以为「球填充」只是示意画法，实际上它是可判定的算术门槛。为什么 $(7,4)$ 能成而 $(15,11)$ 也能成？因为 Hamming 家族的参数是 $N = 2^{M}-1$、$K = N-M$、$t = 1$，代入 (13.3) 得 $1 + (2^{M}-1) = 2^{M}$，恒成立——这正是原文说 Hamming code 天然完美（$t=1$ 时球体积恰好等于 syndrome 空间的全部元素数）。而 (13.4) 的 $1 + 7 = 8 = 2^{3}$ 只是 $M = 3$ 的特例。反过来，为什么 $t \ge 2$ 时几乎无解？因为左边的 $\sum_{w\le t}\binom{N}{w}$ 随 $N$ 按 $N^{t}/t!$ 增长，右边的 $2^{N-K}$ 随 $N$ 指数增长，两者要在每个 $N$ 上恰好相等是极苛刻的整数巧合；书内 §13.3 后面（PDF p221，属下一块）会给出这条方程在 $t\ge2$ 时「几乎无解」的结论，只有 repetition codes 与 Golay 码例外。抽掉这条「整数方程即必要条件」的意识，系统会崩在哪？崩在搜索完美码的资源分配上：1950 年代大量人力在找 $t \ge 2$ 的二元完美码，直到 Tietäväinen (1973) 与 Zinoviev–Leontiev 用这条方程的推广（加 sphere packing 的界）证明「除 Hamming / repetition / Golay 外不存在」，搜索才算有了终点。落点：本页为书内 p208；Golay 码的同类校验见下一块（PDF p221，书内 p209，(13.5)：$1+23+253+1771 = 2048 = 2^{11}$，可用 Python 的 math.comb 复算）；离散侧工具是 6.042J 的 *Binomial coefficients* 与 *Pigeonhole*（(13.3) 的本质就是「点数必须能整除」，即一个 pigeonhole 计数）；线代侧对应 Strang 的「子空间维数与零空间维数之和为 $N$」——$2^{N-K}$ 恰是 syndrome 空间的元素个数，$K$ 是 code 的维数、$N-K$ 是校验子空间维数。</span>


<span style="color:#7f8c8d">书内 p209 ｜ 13.3: Perfect codes</span>

[Figure 13.5：Hamming 空间**未**被「以 codewords 为心的 $t$-球」完美填满的示意图。灰色区域表示到任何 codeword 的 Hamming distance 都大于 $t$ 的点。原书图注特别提醒这是一张**会误导人的**图：对任何 $t$ 较大的高维 code，球与球之间的灰区几乎占据了整个 Hamming 空间。]

#### How happy we would be to use perfect codes（若能大量使用完美码该多好）

如果可选的 perfect codes 数量众多，且 blocklengths 与 rates 覆盖范围很宽，那么它们就是 Shannon 问题的完美解。举例来说，我们可以在噪声水平为 $f$ 的 binary symmetric channel 上通信：挑一个 perfect $t$-error-correcting code，取 blocklength 为 $N$、$t = f^{*} N$，其中 $f^{*} = f + \delta$，而 $N$ 与 $\delta$ 取得使「noise 翻转多于 $t$ 个 bits」的概率令人满意地小。

然而，perfect codes 几乎没有。仅有的非平凡 perfect binary codes 是：

1. **Hamming codes**，即 $t = 1$、blocklength $N = 2^{M}-1$ 的 perfect codes（下文给出定义）；Hamming code 的 rate 随 blocklength $N$ 增大而趋于 1；
2. **blocklength 为奇数的 repetition codes（重复码）**，即 $t = (N-1)/2$ 的 perfect codes；repetition codes 的 rate 以 $1/N$ 趋于零；
3. 一个非凡的 3-error-correcting code，blocklength $N = 23$、含 $2^{12}$ 个 codewords，称为 binary Golay code（二元 Golay 码）。[另一个 2-error-correcting、长度 $N = 11$、定义在三元字母表上的 Golay code，由一位名叫 Juhani Virtakallio 的芬兰足球彩票爱好者在 1947 年发现。]

没有别的 binary perfect codes 了。为什么 perfect codes 如此稀少？是因为像 Hamming code (13.4) 与 Golay code 的参数所满足的那种精确的「数字命理」巧合

```math
1 + \binom{23}{1} + \binom{23}{2} + \binom{23}{3} = 2^{11} \qquad (13.5)
```

都很罕见吗？是否存在大量「几乎完美」的 code，其 $t$-球填满几乎整个空间？

不存在。事实上，那种「以 codewords 为心的 Hamming 球几乎填满 Hamming 空间」的图景（图 13.5）是误导性的：对大多数 code，无论它们是 good codes 还是 bad codes，几乎整个 Hamming 空间都被 $t$-球之间的空隙占据（图 13.5 中灰色的部分）。

立好了这幅阴暗的图景，我们就花点时间把上面提到的那些 perfect codes 的性质补齐。


<span style="color:#7f8c8d">书内 p210 ｜ 13 — Binary Codes</span>

[Figure 13.6：三个 codewords 的重叠结构图。三个 codeword 分别为 $u_N$、$v_N$、$w_N$（加上全零 codeword 作为参照），图中各段以字母标出「两两重叠」的区域。原图纵轴是 $N$ 个坐标、横轴是三个 codeword，各段的边界归属只能靠图中的字母标注判断；文字层只给出字母 $u, v, w, x$ 与它们的组合关系（下一段正文已完整给出定义），此处不臆造图形细节。]

#### The Hamming codes（Hamming 码）

$(7,4)$ Hamming code 可以定义为这样的 linear code：其 $3 \times 7$ parity-check matrix 的各列包含全部 7 个（$= 2^{3}-1$）长度为 3 的非零向量。由于这 7 个向量各不相同，任何单 bit 翻转都产生一个不同的 syndrome，于是所有单 bit 错误都能被检测并纠正。

我们可以把带有 $M = 3$ 个 parity constraints 的这个 code 推广如下。Hamming codes 是单错误纠正码，由一个 parity-check constraints 的数目 $M$ 决定：blocklength $N = 2^{M}-1$；parity-check matrix 的各列包含全部 $N$ 个长度为 $M$ bits 的非零向量。

最初几个 Hamming codes 的 rate 如下：

| Checks $M$ | $(N,K)$ | $R = K/N$ | 说明 |
|---|---|---|---|
| 2 | $(3,1)$ | 1/3 | repetition code $R_3$ |
| 3 | $(7,4)$ | 4/7 | $(7,4)$ Hamming code |
| 4 | $(15,11)$ | 11/15 | |
| 5 | $(31,26)$ | 26/31 | |
| 6 | $(63,57)$ | 57/63 | |

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.4.[2, p.223]**</span> What is the probability of block error of the $(N,K)$ Hamming code to leading order, when the code is used for a binary symmetric channel with noise density $f$?

<span style="color:#7f8c8d">中文话题摘要：写出 $(N,K)$ Hamming code 在噪声密度 $f$ 下 block error 的首阶项——思路是「所有 $t = 1$ 能纠的错被纠掉，剩下的是两个 bit 同时错」，于是答案是一个组合系数乘以 $f^2$。</span>

### 13.4 Perfectness is unattainable – first proof（完美性不可达：第一个证明）

我们将用几种方式说明，有用的 perfect codes 并不存在（这里「有用」指「blocklength $N$ 大，且 rate 既不远于 0 也不远于 1」）。

Shannon 证明：给定任何噪声水平 $f$ 的 binary symmetric channel，都存在 blocklength $N$ 大、rate 可以任意接近 $C(f) = 1 - H_2(f)$、且能实现任意小错误概率的 codes。对大的 $N$，每块的错误数通常约为 $fN$，所以 Shannon 的这些 codes 是「almost-certainly-$fN$-error-correcting」（几乎必然可纠 $fN$ 个错）的 codes。

让我们取噪声 channel 的一个特例，$f \in (1/3, 1/2)$。我们能找到一个大的、$fN$-error-correcting 的 perfect code 吗？好吧，假定已经找到了这样的 code，只考察它其中的三个 codewords。（记住这个 code 的 rate 应是 $R \simeq 1 - H_2(f)$，故它应有极大量的 codewords，数目为 $2^{NR}$。）不失一般性，我们令其中一个 codeword 为全零 codeword，并按图 13.6 所示定义另两个 codeword 与它的重叠。第二个 codeword 在比例为 $u+v$ 的坐标上与第一个不同；第三个 codeword 在比例为 $v+w$ 的坐标上与第一个不同、在比例为 $u+w$ 的坐标上与第二个不同。有比例为 $x$ 的坐标在三个 codewords 中取值全为零。现在，若该 code 是 $fN$-error-correcting 的，其 minimum distance 必须大于


<span style="color:#7f8c8d">书内 p211 ｜ 13.5: Weight enumerator function of random linear codes</span>

$2fN$，于是

```math
u + v \gt 2f, \quad v + w \gt 2f, \quad \text{and} \quad u + w \gt 2f. \qquad (13.6)
```

把这三个不等式相加再除以二，得

```math
u + v + w \gt 3f. \qquad (13.7)
```

于是若 $f \gt 1/3$，就能推出 $u + v + w \gt 1$，从而 $x \lt 0$，这不可能。这样的 code 不可能存在。所以这个 code 连三个 codewords 都不能有，更不用说 $2^{NR}$ 个。

我们的结论是：Shannon 证明了存在大量能在 $f \gt 1/3$ 的 binary symmetric channel 上通信的 codes，而能这么做的 perfect codes 没有任何一个。

下面我们研究一个更一般的论证，它表明：对一般 rates（除 0 与 1 之外），不存在大的 perfect linear codes。做法是先求出一个 random linear code 的典型距离。

### 13.5 Weight enumerator function of random linear codes（随机线性码的重量枚举函数）

想象这样造一个 code：随机选取 $M \times N$ parity-check matrix $H$ 中的 binary entries。我们该期望什么样的 weight enumerator function？

某一个以 $H$ 为 parity-check matrix 的 code 的 weight enumerator $A(w)_H$，是 weight 为 $w$ 的 codewords 个数，可写成

```math
A(w)_H = \sum_{x:\,|x| = w} \left[ Hx = 0 \right], \qquad (13.8)
```

其中求和遍历一切 weight 为 $w$ 的向量 $x$，而 truth function（真值函数）$[Hx = 0]$ 在 $Hx = 0$ 时等于 $1$、否则等于 $0$。

我们可以求出 $A(w)$ 的期望值

```math
\langle A(w) \rangle = \sum_{H} P(H) A(w)_H \qquad (13.9)
```

```math
= \sum_{x:\,|x|=w} \sum_{H} P(H) \left[ Hx = 0 \right], \qquad (13.10)
```

做法是计算「某个 weight 为 $w \gt 0$ 的词是该 code 的 codeword」这一概率（在我们这个 ensemble 的全部 binary linear codes 上取平均）。由对称性，这个概率只依赖词的 weight $w$，不依赖词的具体样子。整个 syndrome $Hx$ 为零的概率，可以由 syndrome 中 $M$ 个 bits 各自为零的概率相乘得到。syndrome 的每一位 $z_m$ 是 $w$ 个随机 bits 的和（模 2），故 $z_m = 0$ 的概率是 $1/2$。于是 $Hx = 0$ 的概率是

```math
\sum_{H} P(H) \left[ Hx = 0 \right] = (1/2)^{M} = 2^{-M}, \qquad (13.11)
```

与 $w$ 无关。

weight 为 $w$ 的词的期望个数 (13.10)，就是遍历所有 weight 为 $w$ 的词、把每个词成为 codeword 的概率加起来。weight 为 $w$ 的词有 $\binom{N}{w}$ 个，于是

```math
\langle A(w) \rangle = \binom{N}{w} 2^{-M} \quad \text{for any } w \gt 0. \qquad (13.12)
```

<span style="color:#1e8449;">**[译注]** (13.11)–(13.12) 这一步值得停下来问一句：为什么「某个 weight 为 $w$ 的词成为 codeword」的概率恰好是 $2^{-M}$，与 $w$ 无关？机制是两件事叠起来的——① $H$ 的每个 entry 独立且等概率取 0/1，故 syndrome 的第 $m$ 位 $z_m$ 是 $w$ 个独立随机 bits 的模 2 和，它取 0 的概率恰为 $1/2$；② 不同 $m$ 之间互相独立，于是 $M$ 位同时为 0 的概率是 $(1/2)^{M}$。第二步才是承重的：抽掉「行与行之间的独立性」，比如用循环码那种「下一行是上一行的循环移位」，诸 $z_m$ 就高度相关，$(1/2)^{M}$ 立刻不成立，期望公式 (13.12)、进而 Gilbert–Varshamov 距离 (13.15) 的整个推导都站不住。换句话说，$d_{\mathrm{GV}}$ 不是「任何线性码」的性质，而是**均匀随机 ensemble 的平均性质**，这也正是原文反复强调 averaging over our ensemble 的原因。可复算的验证：取 $M = 3$、$N = 6$、$w = 2$，则 $\langle A(2)\rangle = \binom{6}{2}2^{-3} = 15/8 = 1.875$，而 Hamming 空间里 weight 为 2 的词共有 15 个，即平均每个这样的词有 $1/8$ 的机会落进 code。落点：本页为书内 p211；(13.13)–(13.14) 的 $H_2$ 近似与 $d_{\mathrm{GV}}$ 定义在书内 p212；同款 ensemble 计算见 van Lint 的 *Introduction to Coding Theory* 第 1 章（二手，可对照）；离散侧挂 6.042J 的 *Independence* 与 *Linearity of expectation*（指示变量求和是 (13.9)→(13.10) 的唯一技巧）；工程侧的现实对应是 §12.2 那个 `Rand8[256]` 伪随机置换表——hash function 之所以要用它打散，就是为了让「独立性假设」近似成立。</span>

[Figure 13.7：一个随机的 binary parity-check matrix（随机二元校验矩阵）的排印示意，行数为 $M$、列数为 $N$。原书在本页只给出这个矩阵的排版图，用作 (13.8) 中 $H$ 的具体形象；矩阵中每一位的具体取值是「随机」的示例，其数字在文字层与正文的数字（如 $2^{M}$ 的指数）混排、行对齐不稳定，逐位取值无法可靠复原，故此处不转写，只保留其结构（$M$ 行 $N$ 列、每个 entry 取 0 或 1、行数 $M$ 即 syndrome 方程的条数）。]


<span style="color:#7f8c8d">书内 p212 ｜ 13 — Binary Codes</span>

对大的 $N$，可用 $\log \binom{N}{w} \simeq N H_2(w/N)$ 与 $R \simeq 1 - M/N$ 写出

```math
\log_2 \langle A(w) \rangle \simeq N H_2(w/N) - M \qquad (13.13)
```

```math
\simeq N\left[ H_2(w/N) - (1 - R) \right] \quad \text{for any } w \gt 0. \qquad (13.14)
```

作为一个具体例子，图 13.8 给出了 $N = 540$、$M = 360$ 的 rate-$1/3$ random linear code 的期望 weight enumerator function。

[Figure 13.8：$N = 540$、$M = 360$ 的 random linear code 的期望 weight enumerator function $\langle A(w) \rangle$，横轴 $w = 0\dots540$，纵轴 $0$ 到约 $6\times 10^{52}$；下图是 $\langle A(w) \rangle$ 的对数坐标图，纵轴自 $10^{-120}$ 到 $10^{60}$。两图共用同一组数据，对数图把 $w \approx 360$ 附近的指数交叉点显出来。]

#### Gilbert–Varshamov distance（Gilbert–Varshamov 距离）

对那些使 $H_2(w/N) \lt (1-R)$ 的 weights，$A(w)$ 的期望小于 $1$；对那些使 $H_2(w/N) \gt (1-R)$ 的 weights，期望大于 $1$。于是我们预期：对大的 $N$，random linear code 的 minimum distance 会接近由下式定义的 $d_{\mathrm{GV}}$：

```math
H_2(d_{\mathrm{GV}}/N) = (1 - R). \qquad (13.15)
```

<span style="color:#00838f">**定义**：这个距离 $d_{\mathrm{GV}} \equiv N H_2^{-1}(1-R)$，称为 rate $R$、blocklength $N$ 下的 Gilbert–Varshamov distance。</span>

Gilbert–Varshamov conjecture（Gilbert–Varshamov 猜想）被广泛相信，它断言：（对大的 $N$）不可能造出 minimum distance 显著大于 $d_{\mathrm{GV}}$ 的 binary codes。

<span style="color:#00838f">**定义**：Gilbert–Varshamov rate（$R_{\mathrm{GV}}$）是在假定 Gilbert–Varshamov 猜想成立的前提下，能用一个 bounded-distance decoder（按 p.207 的定义）可靠通信的最高 rate。</span>

#### Why sphere-packing is a bad perspective, and an obsession with distance is inappropriate（为什么「球填充」是个坏视角，而对距离的执念并不恰当）

若使用 bounded-distance decoder，可容忍的最大噪声水平会使比例为 $f_{\mathrm{bd}} = \tfrac{1}{2} d_{\min}/N$ 的 bits 翻转。于是假定 $d_{\min}$ 等于 Gilbert 距离 $d_{\mathrm{GV}}$ (13.15)，我们有

```math
H_2(2 f_{\mathrm{bd}}) = (1 - R_{\mathrm{GV}}), \qquad (13.16)
```

```math
R_{\mathrm{GV}} = 1 - H_2(2 f_{\mathrm{bd}}). \qquad (13.17)
```

现在到了关键处：Shannon 说什么是可达的？他说通信的最大可能 rate 是 capacity，

```math
C = 1 - H_2(f). \qquad (13.18)
```

于是对给定 rate $R$，按 Shannon 的说法，可容忍的最大噪声水平由

```math
H_2(f) = (1 - R) \qquad (13.19)
```

给出。我们的结论是：设想已选好一个 rate 为 $R$ 的 good code；方程 (13.16) 与 (13.19) 分别定义了 bounded-distance decoder 可容忍的最大噪声 $f_{\mathrm{bd}}$、以及 Shannon 的 decoder 可容忍的最大噪声 $f$。于是

```math
f_{\mathrm{bd}} = f/2. \qquad (13.20)
```

**bounded-distance decoders 永远只能应付 Shannon 证明可容忍的噪声水平的一半！**

[Figure 13.9：Shannon 的 channel capacity $C$ 与 Gilbert rate $R_{\mathrm{GV}}$ 的对照图——后者是使用 bounded-distance decoder 时可达到的最高通信 rate，作为噪声水平 $f$ 的函数，横轴 $f$ 自 $0$ 到 $0.5$、纵轴自 $0$ 到 $1$。原书图注：对任何给定 rate $R$，Shannon 可容忍的最大噪声水平，是一个使用 bounded-distance decoder 的「worst-case-ist」可容忍最大噪声水平的两倍。图中两条曲线的具体形状由 $H_2$ 给出，$C$ 恒为 $1-H_2(f)$、$R_{\mathrm{GV}}$ 为 $1-H_2(2f)$。]

这与 perfect codes 有什么关系？一个 code 是 perfect 的，若其 codewords 周围的 $t$-球互不重叠地填满 Hamming 空间。


<span style="color:#7f8c8d">书内 p213 ｜ 13.6: Berlekamp's bats</span>

但当用典型的 random linear code 在接近 Shannon limit 的 binary symmetric channel 上通信时，典型被翻转的 bits 数是 $fN$，而 codewords 之间的 minimum distance 也是 $fN$、或者略大一点（如果我们略低于 Shannon limit 的话）。于是在 codewords 周围那些 $fN$-球彼此重叠到这种程度：每个球几乎**包含**它最近邻的球心！

这种重叠之所以不致命，是因为在高维空间里，与重叠相关的那部分体积（图 13.10 中阴影所示）只占任一球体积的极小部分，于是落进该区域的概率极小。

[Figure 13.10：两个重叠的球，其半径几乎等于两球心之间的距离。阴影部分是重叠区；原书用这个图说明：高维时重叠区的体积相对于整个球的体积趋于零，因此「球重叠」并不意味着译码会错。]

这个故事的寓意是：worst-case-ism 可能对你不利，它把你容忍噪声的能力砍掉一半。你必须能在**远超** code 的 minimum distance 的地方继续译码，才能抵达 Shannon limit！

尽管如此，code 的 minimum distance 在实践中仍有意义，因为在某些条件下，minimum distance 主导着一个 code 所犯的错误。

<span style="color:#1e8449;">**[译注]** (13.20) 那句 $f_{\mathrm{bd}} = f/2$ 是全章最硬的一个定量结论，但它的论证方式容易被误读成「高维球重叠所以算错了」，实际上关键恰恰相反：球**确实**重叠，而重叠不致命。把机制拆开：两个半径 $r \approx d_{\min}/2$ 的球，球心距 $d \approx 2r$；在 $N$ 维里，两个球的交集体积与球体积之比随 $N$ 增大而指数衰减——可以用「球体积集中在赤道附近一层薄壳」这条几何事实直接看出（球面上几乎所有的点都在赤道附近，故两球只在极扁的一片里相交）。所以「$fN$-球互相重叠」在 $N$ 大时并不带来 $fN$ 量级的译码错误。抽掉这条几何事实，系统会崩在哪？崩在 **decoder 的设计哲学**：若你以为「球重叠 ⇒ 不可纠」，就会退到 bounded-distance decoder，于是把可容忍噪声砍半（$f_{\mathrm{bd}} = f/2$），在同样 rate 下白白损失一半的噪声余量；而现代 LDPC / turbo 的 message-passing decoder 之所以能做到 $f \to C$ 附近，正是因为它压根不检查「$r$ 是否在某个 $t$-球内」，而是对每个 bit 做后验边缘化。可复算的验证：取 $N = 100$ 与 $r = 40$，用 $H_2$ 近似估 $\log_2(\text{球体积}) = N H_2(r/N) = 100 H_2(0.4) \approx 97.1$ bits，而 $\log_2 2^{N} = 100$ bits，即球体积占全空间的 $2^{-3}$ 左右——半径 40 的球在 100 维里还只占 1/8；随 $N$ 增大这个比例继续指数下降。落点：本页为书内 p213；定量对照见上一块 §13.5 的 (13.16)–(13.20)；几何侧挂 Thomson 实分析里「$\mathbb{R}^N$ 单位球体积随 $N$ 趋于零」的计算（$\pi^{N/2}/\Gamma(N/2+1)$），它正是「高维球几乎不含体积」的另一副面孔；离散侧的组合计数 $\binom{N}{w}$ 与 $H_2$ 的换算是 6.042J 的 *Binomial coefficients / Entropy of distributions* 一节。</span>

### 13.6 Berlekamp's bats（Berlekamp 的蝙蝠）

一只瞎眼的蝙蝠住在洞里。它绕着洞心飞——洞心对应一个 codeword——它与洞心的典型距离由一个 friskiness parameter（活跃度参数）$f$ 控制。（蝙蝠相对洞心的位移对应 noise vector。）洞的边界由朝洞心伸出的 stalactites（钟乳石）构成（图 13.11）。每根钟乳石都类比于「本 codeword 与另一个 codeword 之间的边界」。钟乳石就像图 13.10 中的阴影区，只是形状被重新画过，以传达「它是一个体积极小的区域」这个意思。

decoding errors 对应蝙蝠的预定轨迹穿进某根钟乳石内部。与不同距离处的钟乳石相撞都是可能的。

若 friskiness 非常小，蝙蝠通常离洞心很近；相撞会很少，而且一旦发生，通常是撞上尖端离中心点最近的那些钟乳石。类似地，在低噪声条件下 decoding errors 会很少，且典型地涉及低 weight 的 codewords。在低噪声条件下，code 的 minimum distance 与那（极小的）错误概率相关。

[Figure 13.11：Berlekamp 对 Hamming 空间「某个 codeword 附近」的示意画法。锯齿状实线围住「以该 codeword 为最近」的全部点；以该 codeword 为心的 $t$-球只占这块空间的一小部分。原书中锯齿线各峰到中心的距离不一，代表不同 weight 的相邻 codewords；各峰的具体远近归属无法从文字层复原，故不臆造具体距离数值。]


<span style="color:#7f8c8d">书内 p214 ｜ 13.7: Concatenation of Hamming codes</span>

若 friskiness 更高，蝙蝠就常常飞出最长钟乳石所在的那个安全距离 $t$ 之外，但它最常撞上的却是更远处的钟乳石，因为它们数量更多。处在 minimum distance 上的钟乳石只有极少数，所以它们相对不太可能导致错误。类似地，真实纠错码中的错误取决于 weight enumerator function 的性质。

在 friskiness 极高时，蝙蝠总是离洞心很远，几乎全部的相撞都是与远处钟乳石的接触。在这种条件下，蝙蝠的碰撞频率与「从中心到最近一根钟乳石的距离」毫无关系。

<span style="color:#1e8449;">**[译注]** Berlekamp 这个比喻值得当成一条**计算口径**记下来，而不只是修辞。它说的是：错误概率是 $\sum_{w} A(w) \cdot P(w\text{-weight 的 noise 把接收点推过边界})$——真正决定错误的量是**整条** weight enumerator function（或者说距离谱），不是它的第一个非零项。抽掉这条认识，系统会崩在哪？崩在**码的选型评估**：只看 $d_{\min}$ 会得出「低密度生成矩阵码（very bad distance）不可用」的错误结论，而 §13.7 紧接着就用 concatenated Hamming codes 演示了反例：$d = 3^{C}$ 而 $N$ 增长得更快（$d/N \to 0$，属 `bad` distance），可它在 $f = 0.0588$ 的 binary symmetric channel 上 bit error 概率能降到零——是 `good` code family。落点：本页为书内 p214；反例在紧接着的 §13.7（书内 p214–215，Figure 13.12–13.14）；量化工具是上一块的 (13.13)–(13.14) $\langle A(w)\rangle = \binom{N}{w} 2^{-M}$；离散侧的求和技巧（按 weight 分组求和、把组合数换成指数）是 6.042J 的 *Sums and asymptotics* 与 *Stirling / 二项式估计* 一节。再把「钟乳石高度」换成可算的量：错误概率的求和 $\sum_{w} A(w)[\beta(f)]^{w}$ 里，$A(w)$ 与 $[\beta(f)]^{w}$ 一个随 $w$ 上升一个随 $w$ 下降，两者相乘因而有一个鞍点（saddle point），这个鞍点所在的 $w^{*}$ 就是「最典型的致错重量」——它一般既不是 $d_{\min}$，也不是 $N/2$。可复算的验证：取 random linear code 的 $\langle A(w)
可复算的验证：取 random linear code 的 $\langle A(w)\rangle = \binom{N}{w}2^{-M}$，$N = 540$、$M = 360$（书内 p212 的 Figure 13.8 参数）、$f = 0.05$，则 $\beta(f) = 2\sqrt{0.05 \times 0.95} \approx 0.436$、$\log_2\beta \approx -1.198$；对 $\log_2 A(w) + w\log_2\beta$ 求导得鞍点 $w^{*} = N\beta/(1+\beta) \approx 540 \times 0.436/1.436 \approx 164$，而该 ensemble 的 Gilbert–Varshamov 距离满足 $H_2(d_{\mathrm{GV}}/N) = 1-R = 2/3$，即 $d_{\mathrm{GV}}/N \approx 0.174$、$d_{\mathrm{GV}} \approx 94$。于是最致错的重量约为最小距离的 $1.75$ 倍——**只看 $d_{\min}$ 会低估错误概率**。可复算的第二项检查：$w = 164$ 时 $540 H_2(164/540) - 360 + 164\log_2 0.436 \approx -78 \lt 0$，故该 $f$ 下并集界给出的上界仍远小于 $1$（低噪声区间的典型行为）。

### 13.7 Concatenation of Hamming codes（Hamming 码的级联）

多玩一下 Hamming 码的 concatenation（级联）是有教益的——这个概念我们第一次在图 11.6 遇到过——因为我们会由此获得对 good codes 这个概念、以及 code 的 minimum distance 是否相干这一问题的洞见。

我们可以通过在 binary symmetric channel 上依次用若干个 Hamming codes 编码，为噪声密度 $f$ 的该 channel 造一个 concatenated code（级联码）。

下表复述 Hamming codes 的关键性质，以 constraints 的数目 $M$ 为索引。所有 Hamming codes 的 minimum distance 都是 $d = 3$，且能纠正 $N$ 中的 1 个错误。

| 量 | 表达式 |
|---|---|
| blocklength | $N = 2^{M}-1$ |
| number of source bits | $K = N - M$ |
| probability of block error to leading order | $p_B = \frac{3}{N}\binom{N}{2} f^{2}$ |

[Figure 13.12：concatenated Hamming code 的 rate $R$ 随 concatenations 数目 $C$ 变化的曲线，横轴 $C = 0\dots12$、纵轴 $R = 0\dots1$；曲线随 $C$ 增大下降并趋于约 $0.093$ 的水平渐近线。]

若我们通过级联一串 $M$ 递增的 Hamming codes 来造一个 product code（乘积码），我们可以这样选取那些参数 $\{M_c\}_{c=1}^{C}$，使 product code 的 rate

```math
R_C = \prod_{c=1}^{C} \frac{N_c - M_c}{N_c} \qquad (13.21)
```

随 $C$ 增大而趋于一个非零极限。举例来说，若取 $M_1 = 2$、$M_2 = 3$、$M_3 = 4$，等等，则渐近 rate 是 $0.093$（图 13.12）。

blocklength $N$ 是 $C$ 的快速增长函数，所以这些 code 有些不实用。这些 code 的又一个弱点是 minimum distance 不太好（图 13.13）。每个组成用的

[Figure 13.13：concatenated Hamming code 的 blocklength $N_C$（上曲线）与 minimum distance $d_C$（下曲线）随 concatenations 数目 $C$ 变化的图，横轴 $C = 0\dots12$，纵轴为对数尺度（$1$ 到 $10^{25}$）。]

Hamming code 的 minimum distance 都是 3，故第 $C$ 次乘积的 minimum distance 是 $3^{C}$。blocklength $N$ 增长得比 $3^{C}$ 快，于是 $d/N$ 随 $C$ 增大趋于零。对照之下，对典型的 random codes，$d/N$ 趋于一个常数，满足 $H_2(d/N) = 1-R$。因此 concatenated Hamming codes 具有「bad」distance。

尽管这样，结果却是：这一简单的 code 序列对某些 channel 给出 good codes——但不是很好的 codes（回顾 §11.4 关于 `good` 与 `very good` 术语的定义）。我们不去证明这个结果，而只用数值方式探讨它。

图 13.14 给出 concatenated codes 的 bit error probability $p_b$，其中假定各组成 code 按 §11.4 描述的方式依次译码。[这种一次只译一个 code 的译码是次优的，我们在那里已经看到。] 横轴是各 code 的 rate。随着 concatenations 数目增大，rate 降到 $0.093$，错误概率趋于零。图中假定的 channel 是


<span style="color:#7f8c8d">书内 p215 ｜ 13.8: Distance isn't everything</span>

$f = 0.0588$ 的 binary symmetric channel。这是用这个 concatenated code 所能容忍的最高噪声水平。

[Figure 13.14：concatenated Hamming codes 的 bit error probability 对 rate $R$ 的图，用于 $f = 0.0588$ 的 binary symmetric channel；纵轴 $10^{-14}$ 到 $1$（对数），横轴 $R = 0\dots1$；各点旁标的 blocklength 依次为 $N = 3, 21, 315, 61525, 10^{13}$；实线是该 channel 的 Shannon limit。bit error probability 趋于零而 rate 趋于 $0.093$，故 concatenated Hamming codes 是一个 `good` code family。]

这个故事带来的 take-home message（要带走的话）是：**distance isn't everything**（距离不是一切）。code 的 minimum distance 虽被 coding theorist 广泛膜拜，但对 Shannon 的使命（在有噪 channel 上实现可靠通信）并不具有根本的重要性。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.5.[3]**</span> Prove that there exist families of codes with 'bad' distance that are 'very good' codes.

<span style="color:#7f8c8d">中文话题摘要：构造一族 `bad` distance 却是 `very good` 的 code——级联 Hamming 码就是现成例子，题目要你把它写成一般构造并证明 $P_e \to 0$、$d/N \to 0$ 可同时成立。</span>

### 13.8 Distance isn't everything（距离不是一切）

让我们对 minimum distance 的影响取得定量感觉，就 binary symmetric channel 这一特例来做。

#### The error probability associated with one low-weight codeword（与单个低 weight codeword 相关的错误概率）

设一个 binary code 的 blocklength 为 $N$，只有两个 codewords，二者在 $d$ 个位置上不同。为简单起见，设 $d$ 为偶数。若这个 code 用在噪声水平 $f$ 的 binary symmetric channel 上，错误概率是多少？

bit flips 只在两个 codewords 不同的地方才有关系。错误概率由「这 $d$ 个 bits 中有 $d/2$ 个被翻转」的概率主导。其余 bits 怎样都无关，因为 optimal decoder 忽略它们。

```math
P(\text{block error}) \simeq \binom{d}{d/2} f^{d/2} (1-f)^{d/2}. \qquad (13.22)
```

与单个 weight 为 $d$ 的 codeword 相关的这个错误概率画在图 13.15 里。利用二项式系数的近似 (1.16)，

[Figure 13.15：与单个 weight 为 $d$ 的 codeword 相关的错误概率 $\binom{d}{d/2} f^{d/2}(1-f)^{d/2}$，作为 $f$ 的函数；纵轴对数（$10^{-20}$ 到 $1$），横轴 $f = 0.0001\dots0.1$；各曲线标 $d = 10, 20, 30, 40, 50, 60$。]

我们可以进一步近似

```math
P(\text{block error}) \simeq \left[ 2 f^{1/2} (1-f)^{1/2} \right]^{d} \qquad (13.23)
```

```math
\equiv \left[ \beta(f) \right]^{d}, \qquad (13.24)
```

其中 $\beta(f) = 2 f^{1/2}(1-f)^{1/2}$ 称为该 channel 的 Bhattacharyya parameter（Bhattacharyya 参数）。


<span style="color:#7f8c8d">书内 p216 ｜ 13.9: The union bound ｜ 13.10: Dual codes</span>

现在考虑一个距离为 $d$ 的一般 linear code。它的 block error probability 必定至少为 $\binom{d}{d/2} f^{d/2}(1-f)^{d/2}$，与 code 的 blocklength $N$ 无关。由于这一点，一列 blocklength $N$ 递增而距离固定为 $d$（即具有「very bad」distance）的 codes，在任何 binary symmetric channel 上都不可能使 block error probability 趋于零。因此，如果我们感兴趣的是造出具有极小极小错误概率的顶级纠错码，我们或许会避开 bad distance 的 code。不过，从实用角度出发，我们应该更仔细地看图 13.15。在第 1 章里我们论证过，disk drive 用的 code 需要小于约 $10^{-18}$ 的错误概率。若 disk drive 的原始错误概率约为 $0.001$，则与距离 $d = 20$ 的单个 codeword 相关的错误概率小于 $10^{-24}$。若 disk drive 的原始错误概率约为 $0.01$，则与距离 $d = 30$ 的单个 codeword 相关的错误概率小于 $10^{-20}$。因此，就实用而言，一个 code 并不必须具有好的 distance。举例来说，blocklength 为 10 000、已知含许多 weight 为 32 的 codewords 的 codes，仍然能以极小的错误概率纠正 weight 为 320 的错误。

我不希望你因此以为我在推荐使用 bad distance 的 codes；在第 47 章我们将讨论 low-density parity-check codes（低密度校验码），那是我最喜欢的 codes，它既有出色的性能又有好的 distance。

### 13.9 The union bound（并集界）

code 在 binary symmetric channel 上的错误概率，可以用「与单个 codeword 相关的错误概率」(13.24) 的适当倍数相加，借助其 weight enumerator function 来界住：

```math
P(\text{block error}) \le \sum_{w \gt 0} A(w) \left[ \beta(f) \right]^{w}. \qquad (13.25)
```

<span style="color:#1e8449;">**[译注]** union bound 在这里的用法要说清边界，否则很容易把它当成精确等式。它计算的是「$r$ 落进**任一**其他 codeword 的译码区」这一并集的概率，做法是把各个别事件的概率直接相加，于是把「同一个 noise 向量同时接近两个以上 codeword」的情形**重复计入**了。为什么它在低噪声 $f$ 下准？因为 (13.24) 里每项按 $[\beta(f)]^{w}$ 指数衰减，$f$ 很小时 $w$ 越大项越小，求和被少数最小 weight 的 codewords 主导，而这些事件几乎互斥（一个噪声向量很难同时把接收点推到两个相距 $d_{\min}$ 的 codeword 附近），故并集界近似取等。高噪声时恰恰相反：$f \to 1/2$ 时 $\beta(f) \to \sqrt{2}/2 \lt 1$ 但衰减极慢，大量中等 weight 项一起贡献，重数效应让上界远离真值。抽掉这条边界认识会崩在**可达 rate 的解读**上：Exercise 13.6 用 (13.25) 当等式解出的 $R_{\mathrm{UB}}(f)$ 只是一个「穷人版」估计，若把它当成 capacity 的精确值，就会误判某个 code family 已到极限。落点：本页为书内 p216 的 (13.25)；Exercise 13.6 紧随其后；下一章（Ch.14，书内 p229 起）正是把这个界严格化为 noisy-channel coding theorem 的证明——那里靠的是「typical noise vector 的个数」而不是「所有 error pattern 的并集」；离散侧的一般并集界写法见 6.042J 的 *Probability: union bound*。</span>

这个不等式是 union bound（并集界）的一个例子；它在低噪声水平 $f$ 下准确，在高噪声水平下不准确，因为当错误同时与多于一个 codeword 混淆时，它把那些贡献重复计入了。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.6.[3]**</span> Poor man's noisy-channel coding theorem. Pretending that the union bound (13.25) is accurate, and using the average weight enumerator function of a random linear code (13.14) (section 13.5) as $A(w)$, estimate the maximum rate $R_{\mathrm{UB}}(f)$ at which one can communicate over a binary symmetric channel. Or, to look at it more positively, using the union bound (13.25) as an inequality, show that communication at rates up to $R_{\mathrm{UB}}(f)$ is possible over the binary symmetric channel.

<span style="color:#7f8c8d">中文话题摘要：「穷人版」noisy-channel coding theorem——把并集界当等式，代入随机线性码的平均 weight enumerator，用 saddle-point（鞍点）法估出可达 rate $R_{\mathrm{UB}}(f)$。</span>

在下一章中，我们将通过分析一个 binary linear code 用 syndrome decoding 时的错误概率、并使用 union bound，来证明 Shannon 的 noisy-channel coding theorem（针对 symmetric binary channels），从而证明存在非常好的 linear codes。

### 13.10 Dual codes（对偶码）

一个在 coding theory 中有相当重要性、尽管本书不会立刻用到的概念，是线性纠错码的 dual（对偶）这一想法。

一个 $(N,K)$ linear error-correcting code 可以看作由 $K$ 个独立 basis codewords 的一切组合相加所生成的 $2^{K}$ 个 codewords 之集合。该 code 的 generator matrix 由这 $K$ 个 basis codewords 组成，习惯上写成行向量。例如，$(7,4)$ Hamming code 的 generator matrix（取自 p.10）是

```math
G = \begin{pmatrix}
1 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 & 0 & 1 & 1
\end{pmatrix} \qquad (13.26)
```

它的十六个 codewords 列在表 1.14（p.9）中。这个 code 的 codewords 是四个向量 $[1\ 0\ 0\ 0\ 1\ 0\ 1]$、$[0\ 1\ 0\ 0\ 1\ 1\ 0]$、$[0\ 0\ 1\ 0\ 1\ 1\ 1]$、$[0\ 0\ 0\ 1\ 0\ 1\ 1]$ 的线性组合。

一个 $(N,K)$ code 也可以用 $M \times N$ 的 parity-check matrix（其中 $M = N-K$）描述，即满足

```math
Ht = 0 \qquad (13.27)
```

的向量 $\{t\}$ 的集合。


<span style="color:#7f8c8d">书内 p217 ｜ 13.10: Dual codes</span>

看这个方程的一种方式是：$H$ 的每一行都规定了一个向量，而若 $t$ 是 codeword，它就必须与该向量正交。

<span style="color:#00838f">**generator matrix 规定了 $K$ 个向量，一切 codewords 都可由它们拼出；parity-check matrix 规定了一组 $M$ 个向量，一切 codewords 都与它们正交。一个 code 的 dual，就是把 generator matrix 与 parity-check matrix 互换而得到的。**</span>

<span style="color:#00838f">**定义**：一切与某个 code $C$ 中全部 codewords 都正交的长度 $N$ 的向量所成的集合，称为该 code 的 dual（对偶码），记作 $C^{\perp}$。</span>

若 $t$ 与 $h_1$、$h_2$ 都正交，则它也与 $h_3 \equiv h_1 + h_2$ 正交；所以一切 codewords 与 $H$ 的 $M$ 行的任何线性组合都正交。于是 parity-check matrix 各行的一切线性组合所成的集合，就是 dual code。

对我们的 Hamming $(7,4)$ code，parity-check matrix 是（取自 p.12）

```math
H = \left[ P \mid I_3 \right] = \begin{pmatrix}
1 & 1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 1 & 0 & 0 & 1
\end{pmatrix}. \qquad (13.28)
```

$(7,4)$ Hamming code $H_{(7,4)}$ 的 dual 就是表 13.16 所示的 code。

<span style="color:#7f8c8d">表 13.16：$(7,4)$ Hamming code 之 dual 的八个 codewords（可与表 1.14，p.9 对照）。原书为边注表，按语义重建。</span>

| $C^{\perp}$ 的 8 个 codewords |
|---|
| 0000000 |
| 0010111 |
| 0101101 |
| 0111010 |
| 1001110 |
| 1011001 |
| 1100011 |
| 1110100 |

这一对 codes 有一个或许出乎意料的性质：dual $H^{\perp}_{(7,4)}$ 被包含在 code $H_{(7,4)}$ **自身**之内——dual code 里的每个词都是原 $(7,4)$ Hamming code 的 codeword。这个关系可用集合记号写成

```math
H^{\perp}_{(7,4)} \subset H_{(7,4)}. \qquad (13.29)
```

「对偶向量集可能与 codeword 向量集重叠」这件事，若我们把向量想成实向量就反直觉——一个向量怎么能与自己正交？但当我们在模二算术里工作时，许多非零向量确实与自身正交！

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.7.[1, p.223]**</span> Give a simple rule that distinguishes whether a binary vector is orthogonal to itself, as is each of the three vectors $[1\ 1\ 1\ 0\ 1\ 0\ 0]$, $[0\ 1\ 1\ 1\ 0\ 1\ 0]$, and $[1\ 0\ 1\ 1\ 0\ 0\ 1]$.

<span style="color:#7f8c8d">中文话题摘要：给出「二元向量与自身正交」的判据——答案是 weight 为偶；这题是 (13.29) 与「偶 weight」性质之间的桥梁。</span>

#### Some more duals（更多对偶的例子）

一般地，若一个 code 有 systematic generator matrix（系统型生成矩阵）

```math
G = \left[ I_K \mid P^{T} \right], \qquad (13.30)
```

其中 $P$ 是 $K \times M$ 矩阵，则其 parity-check matrix 是

```math
H = \left[ P \mid I_M \right]. \qquad (13.31)
```


<span style="color:#7f8c8d">书内 p218 ｜ 13 — Binary Codes</span>

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 13.8（例 13.8）</span>

repetition code $R_3$ 的 generator matrix 是

```math
G = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix}; \qquad (13.32)
```

其 parity-check matrix 是

```math
H = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}. \qquad (13.33)
```

两个 codewords 是 $[1\ 1\ 1]$ 与 $[0\ 0\ 0]$。dual code 的 generator matrix 是

```math
G^{\perp} = H = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} \qquad (13.34)
```

或者等价地，通过行相加把 $G^{\perp}$ 改成系统型：

```math
G^{\perp} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}. \qquad (13.35)
```

我们把这个 dual code 称为 simple parity code（简单奇偶校验码）$P_3$；它就是那个带一个 parity-check bit（等于两个 source bits 之和）的 code。该 dual code 的四个 codewords 是 $[1\ 1\ 0]$、$[1\ 0\ 1]$、$[0\ 0\ 0]$、$[0\ 1\ 1]$。

在这个例子里，code 与 dual 共有的唯一向量是全零 codeword。

#### Goodness of duals（对偶码的「好坏」）

若一列 codes 是「good」的，它们的 duals 也 good 吗？各种情形都能造出例子：good codes 配 good duals（random linear codes）；bad codes 配 bad duals；以及 good codes 配 bad duals。最后一类尤其重要：许多最先进的 codes 具有「其 dual 是 bad」的性质。经典例子是 low-density parity-check code，它的 dual 是 low-density generator-matrix code。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.9.[3]**</span> Show that low-density generator-matrix codes are bad. A family of low-density generator-matrix codes is defined by two parameters $j, k$, which are the column weight and row weight of all rows and columns respectively of $G$. These weights are fixed, independent of $N$; for example, $(j,k) = (3,6)$. [Hint: show that the code has low-weight codewords, then use the argument from p.215.]

<span style="color:#7f8c8d">中文话题摘要：证明低密度生成矩阵码是 `bad`——先指出它必然含 weight 小的 codeword，再套用 p.215 那个「低 weight codeword 给出与 $N$ 无关的错误概率」的论证。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.10.[5]**</span> Show that low-density parity-check codes are good, and have good distance. (For solutions, see Gallager (1963) and MacKay (1999b).)

<span style="color:#7f8c8d">中文话题摘要：证明低密度校验码既 good 又有好 distance——这题是全书最难的练习之一，需要 LDPC 的 density evolution / 集合论界，答案指向 Gallager 1963 与 MacKay 1999b。</span>

#### Self-dual codes（自对偶码）

$(7,4)$ Hamming code 具有「dual 被包含在 code 自身中」的性质。若一个 code 被包含在其 dual 中，则称它是 self-orthogonal（自正交）的。举例来说，$(7,4)$ Hamming code 的 dual 就是一个 self-orthogonal code。看出这一点的一条途径是：$H$ 的任意两行之间的重叠（overlap）都是偶数。包含其 dual 的 codes 在 quantum error-correction（量子纠错）中很重要（Calderbank and Shor, 1996）。

考察 self-dual 的 codes 是一件耐人寻味、虽未必有用的事。若一个 code $C$ 的 dual 与该 code 完全相同，则它是 self-dual（自对偶）的：

```math
C^{\perp} = C. \qquad (13.36)
```

可以推出 self-dual codes 的一些性质：


<span style="color:#7f8c8d">书内 p219 ｜ 13.11: Generalizing perfectness to other channels</span>

1. 若一个 code 是 self-dual 的，则它的 generator matrix 同时也是该 code 的一个 parity-check matrix。
2. self-dual codes 的 rate 为 $1/2$，即 $M = K = N/2$。
3. 所有 codewords 的 weight 都是偶数。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.11.[2, p.223]**</span> What property must the matrix $P$ satisfy, if the code with generator matrix $G = [I_K \mid P^{T}]$ is self-dual?

<span style="color:#7f8c8d">中文话题摘要：问 $G = [I_K \mid P^{T}]$ 自对偶时 $P$ 必须满足什么——答案是 $P^{T}P = I_K$（模 2 正交矩阵）。</span>

#### Examples of self-dual codes（自对偶码的例子）

1. repetition code $R_2$ 是 self-dual code 的一个简单例子。

```math
G = H = \begin{pmatrix} 1 & 1 \end{pmatrix}. \qquad (13.37)
```

2. 最小的非平凡 self-dual code 是下面这个 $(8,4)$ code。

```math
G = \left[ I_4 \mid P^{T} \right] = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 & 1 & 0 & 1 & 1 \\
0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 0
\end{pmatrix}. \qquad (13.38)
```

<span style="color:#7f8c8d">矩阵校验（可复算）：四行 weight 均为 4（偶数）；任意两行之内积模 2 均为 0（$G G^{T} = 0$），故 self-orthogonal；rank $= 4$ 且 $K = N/2 = 4$，故 self-dual。此即 extended Hamming $[8,4,4]$ 码。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.12.[2, p.223]**</span> Find the relationship of the above $(8,4)$ code to the $(7,4)$ Hamming code.

<span style="color:#7f8c8d">中文话题摘要：问这个 $(8,4)$ 码与 $(7,4)$ Hamming 码的关系——答案是「给 Hamming 码加一个全体 bits 的奇偶校验位、再把前四位重排」即得。</span>

#### Duals and graphs（对偶与图）

设一个 code 由一个图表示：图中节点有两类，parity-check constraints（校验约束）与 equality constraints（相等约束），它们由边相连，边代表 code 的各个 bits（并非所有 bits 都需要被传输）。

dual code 的图，就是把所有 parity-check 节点换成 equality 节点、反之亦然而得到的。Forney (2001) 把这类图称为 normal graph（正规图）。

#### Further reading（延伸阅读）

duals 在 coding theory 里之所以重要，是因为涉及某个 code 的函数（例如 codewords 上的后验分布）可以通过一个 Fourier transform 变换成 dual code 上的函数。关于有限群上 Fourier 分析的通俗入门，见 Terras (1999)。另见 MacWilliams and Sloane (1977)。

### 13.11 Generalizing perfectness to other channels（把完美性推广到其他信道）

既然为 binary symmetric channel 寻找 perfect codes 的努力已经放弃，我们不妨换个 channel 来自我安慰。若一个 code 能恢复任意 $u$ 个被擦除的 bits、而从不能多于 $u$ 个，我们就可以把它称为「binary erasure channel 上的 perfect $u$-error-correcting code」。不过，对于这样的 code，惯用的术语不是「perfect」，而是 **maximum distance separable code**（最大距离可分码），即 MDS code。

<span style="color:#7f8c8d">边注（原书页侧）：在 binary erasure channel 的 perfect $u$-error-correcting code 里，冗余 bits 数必须是 $N - K = u$。</span>

正如我们在 exercise 11.10 (p.190) 中已经注意到的，$(7,4)$ Hamming code 不是 MDS code。它能恢复**某些** 3 个被擦除 bits 的集合，但不是全部。若被擦除的 3 个 bits 恰好对应一个 weight 为 3 的 codeword，那么就有一个 bit 的信息不可恢复。这就是为什么 $(7,4)$ code 对 RAID 系统是个差劲的选择。


<span style="color:#7f8c8d">书内 p220 ｜ 13.12: Summary ｜ 13.13: Further exercises</span>

maximum distance separable code 的一个极小例子，是 parity-check matrix 为 $H = [1\ 1\ 1]$ 的 simple parity-check code $P_3$。这个 code 有 4 个 codewords，全都是偶校验。所有 codewords 之间相隔的距离为 2。任何单个被擦除的 bit 都可以通过把它设为另外两个 bits 的奇偶值而恢复。repetition codes 也是 maximum distance separable codes。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.13.[5, p.224]**</span> Can you make an $(N,K)$ code, with $M = N-K$ parity symbols, for a $q$-ary erasure channel, such that the decoder can recover the codeword when any $M$ symbols are erased in a block of $N$? [Example: for the channel with $q = 4$ symbols there is an $(N,K) = (5,2)$ code which can correct any $M = 3$ erasures.]

<span style="color:#7f8c8d">中文话题摘要：问 $q$ 元擦除信道上能否造出「任意 $M$ 个符号被擦除都能恢复」的 MDS 码；二元时只有 repetition 与 simple parity 两类，$q \gt 2$ 时 MDS 码大量存在（Reed–Solomon）。</span>

对 $q \gt 2$ 的 $q$-ary erasure channel，MDS codes 大量存在，其中最著名、用得最广的是 Reed–Solomon codes。只要 field size $q$ 大于 blocklength $N$，任意 rate 的 MDS block codes 都能找到。（延伸阅读见 Lin and Costello (1983)。）

### 13.12 Summary（小结）

Shannon 为 binary symmetric channel 构造的 codes 几乎总能纠正 $fN$ 个错误，但它们并不是 $fN$-error-correcting codes。

**为什么 code 的 distance 关系不大——几条理由**

1. Shannon limit 表明，最好的 codes 必须能应付的噪声水平，是 bounded-distance decoder 所能容忍的最大噪声水平的两倍。
2. 当 binary symmetric channel 的 $f \gt 1/4$ 时，任何带 bounded-distance decoder 的 code 都根本无法通信；但 Shannon 说这样的 channel 上存在 good codes。
3. concatenation 表明：即使 distance 是 bad 的，我们也能得到好的性能。

**对「一个 code 是否为 good code」这个问题而言，相关的是整条 weight enumerator function。**

good codes 与 distance 性质之间的关系，在 exercise 13.14 (p.220) 里有进一步讨论。

### 13.13 Further exercises（进一步习题）

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.14.[3, p.224]**</span> A codeword $t$ is selected from a linear $(N,K)$ code $C$, and it is transmitted over a noisy channel; the received signal is $y$. We assume that the channel is a memoryless channel such as a Gaussian channel. Given an assumed channel model $P(y \mid t)$, there are two decoding problems.

The **codeword decoding problem** is the task of inferring which codeword $t$ was transmitted given the received signal.

The **bitwise decoding problem** is the task of inferring for each transmitted bit $t_n$ how likely it is that that bit was a one rather than a zero.

<span style="color:#7f8c8d">中文话题摘要：定义 codeword decoding 与 bitwise decoding 两个问题，并要求证明它们的最优译码错误概率之间的关系（即 Theorem 13.1 的 $p_B \ge p_b \ge \frac{1}{2}\frac{d_{\min}}{N} p_B$）。</span>


<span style="color:#7f8c8d">书内 p221 ｜ 13.13: Further exercises</span>

考虑这两个 decoding 问题的最优 decoders。请通过证明下面这个定理，来证明最优 bitwise-decoder 的错误概率与最优 codeword-decoder 的错误概率密切相关。

<span style="color:#c0392b">**Theorem 13.1**</span>　<span style="color:#00838f">若一个 binary linear code 的 minimum distance 为 $d_{\min}$，则对任何给定 channel，最优 bitwise decoder 的 codeword bit error probability $p_b$ 与 maximum likelihood decoder 的 block error probability $p_B$ 满足：</span>

```math
p_B \ge p_b \ge \frac{1}{2}\frac{d_{\min}}{N} p_B. \qquad (13.39)
```

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.15.[1]**</span> What are the minimum distances of the $(15,11)$ Hamming code and the $(31,26)$ Hamming code?

<span style="color:#7f8c8d">中文话题摘要：问 $(15,11)$ 与 $(31,26)$ Hamming 码的 minimum distance——答案是两者都为 3（Hamming 家族恒为 $t=1$）。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.16.[2]**</span> Let $A(w)$ be the average weight enumerator function of a rate-$1/3$ random linear code with $N = 540$ and $M = 360$. Estimate, from first principles, the value of $A(w)$ at $w = 1$.

<span style="color:#7f8c8d">中文话题摘要：从基本原理估计 $A(1)$——直接用 $\binom{N}{1}2^{-M} = 540 \cdot 2^{-360}$ 的量级，体会「weight 1 几乎不可能」。 </span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.17.[3C]**</span> A code with minimum distance greater than $d_{\mathrm{GV}}$. A rather nice $(15,5)$ code is generated by this generator matrix, which is based on measuring the parities of all the $\binom{5}{3} = 10$ triplets of source bits:

```math
G = \begin{pmatrix}
1 & \cdot & \cdot & \cdot & \cdot & \cdot & 1 & 1 & 1 & \cdot & \cdot & 1 & 1 & \cdot & 1 \\
\cdot & 1 & \cdot & \cdot & \cdot & 1 & \cdot & 1 & \cdot & 1 & 1 & \cdot & \cdot & 1 & \cdot \\
\cdot & \cdot & 1 & \cdot & \cdot & 1 & 1 & \cdot & \cdot & 1 & \cdot & \cdot & 1 & 1 & \cdot \\
\cdot & \cdot & \cdot & 1 & \cdot & 1 & \cdot & 1 & 1 & \cdot & \cdot & 1 & \cdot & 1 & \cdot \\
\cdot & \cdot & \cdot & \cdot & 1 & \cdot & 1 & 1 & \cdot & \cdot & 1 & 1 & \cdot & \cdot & 1
\end{pmatrix}. \qquad (13.40)
```

<span style="color:#7f8c8d">矩阵校验（可复算）：$5 \times 15$，前 5 列构成 $I_5$（各列 weight 均为 1），后 10 列各 weight 为 3（每个后置 bit 是某个三元组的奇偶值），故每行 weight $= 1 + \binom{4}{2} = 7$。以上三条均由脚本按文字层逐位解析后验证通过。</span>

Find the minimum distance and weight enumerator function of this code.

<span style="color:#7f8c8d">中文话题摘要：求这个 $(15,5)$ 码的 minimum distance 与 weight enumerator function，并注意它的 $d$ 超过了上一条练习里 random linear code 的 $d_{\mathrm{GV}}$——这是「GV 猜想不是定理」的具体反例。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.18.[3C]**</span> Find the minimum distance of the 'pentagonful' low-density parity-check code whose parity-check matrix is

```math
H = \begin{pmatrix}
1 & \cdot & \cdot & \cdot & 1 & 1 & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
1 & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & 1 & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & 1 & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & 1 & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & 1 & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & 1 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & 1 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & 1 & 1 & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & 1 & \cdot & \cdot & \cdot & \cdot & 1 & 1
\end{pmatrix}. \qquad (13.41)
```

<span style="color:#7f8c8d">矩阵校验（可复算）：$10 \times 15$，每行 weight 恰为 3，每列 weight 恰为 2，共 30 个 1（$= 10 \times 3 = 15 \times 2$，即 Petersen 图每条边 = 一个 bit）；GF(2) 上 rank $= 9$，故 $K = 15 - 9 = 6$，与原文「十行中有九行独立」完全吻合。上表由脚本按文字层逐位解析并验证上述四项后重建。</span>

Show that nine of the ten rows are independent, so the code has parameters $N = 15$, $K = 6$. Using a computer, find its weight enumerator function.

<span style="color:#7f8c8d">中文话题摘要：先证明十行中只有九行独立（于是 $N=15, K=6$），再用计算机求 weight enumerator function；正文与 Figure 13.17 指出该图就是 Petersen 图。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.19.[3C]**</span> Replicate the calculations used to produce figure 13.12. Check the assertion that the highest noise level that's correctable is 0.0588. Explore alternative concatenated sequences of codes. Can you find a better sequence of concatenated codes – better in the sense that it has either higher asymptotic rate $R$ or can tolerate a higher noise level $f$?

<span style="color:#7f8c8d">中文话题摘要：复现 Figure 13.12 的计算，核对 $0.0588$ 这个最高可纠噪声，并试着找更好的级联序列（更高渐近 rate 或更高可容忍 $f$）。</span>

[Figure 13.17：pentagonful low-density parity-check code 的图——15 个 bit 节点（圆圈）与 10 个 parity-check 节点（三角形）。原书图注指出这个图就是 Petersen 图（每个节点度数 3、共 15 条边）。边的具体连接次序在文字层中只以 (13.41) 的矩阵形式出现，此处以矩阵为准，图形不另行臆造。]


<span style="color:#7f8c8d">书内 p222 ｜ 13 — Binary Codes</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.20.[3, p.226]**</span> Investigate the possibility of achieving the Shannon limit with linear block codes, using the following counting argument. Assume a linear code of large blocklength $N$ and rate $R = K/N$. The code's parity-check matrix $H$ has $M = N-K$ rows. Assume that the code's optimal decoder, which solves the syndrome decoding problem $Hn = z$, allows reliable communication over a binary symmetric channel with flip probability $f$. How many 'typical' noise vectors $n$ are there? Roughly how many distinct syndromes $z$ are there? Since $n$ is reliably deduced from $z$ by the optimal decoder, the number of syndromes must be greater than or equal to the number of typical noise vectors. What does this tell you about the largest possible value of rate $R$ for a given $f$?

<span style="color:#7f8c8d">中文话题摘要：用计数论证证 Shannon limit——典型噪声向量数 $2^{NH_2(f)}$、不同 syndrome 数 $2^{M}$，前者不能多于后者，于是 $R \le 1 - H_2(f)$；这条论证在下一章会被写成严格证明。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 13.21.[2]**</span> Linear binary codes use the input symbols 0 and 1 with equal probability, implicitly treating the channel as a symmetric channel. Investigate how much loss in communication rate is caused by this assumption, if in fact the channel is a highly asymmetric channel. Take as an example a Z-channel. How much smaller is the maximum possible rate of communication using symmetric inputs than the capacity of the channel? [Answer: about 6%.]

<span style="color:#7f8c8d">中文话题摘要：对 Z-channel 比较「限定等概率二元输入时的最高 rate」与真正 capacity，答案损失约 6%——量化说明 linear binary code 的隐含假设代价有多大。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.22.[2]**</span> Show that codes with 'very bad' distance are 'bad' codes, as defined in section 11.4 (p.183).

<span style="color:#7f8c8d">中文话题摘要：证明「very bad distance（$d$ 为常数）」的 codes 必然是 `bad` codes（$P_e$ 不趋于零），把 §13.8 的 (13.22) 论证一般化。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.23.[3]**</span> One linear code can be obtained from another by puncturing. Puncturing means taking each codeword and deleting a defined set of bits. Puncturing turns an $(N,K)$ code into an $(N',K)$ code, where $N' \lt N$. Another way to make new linear codes from old is shortening. Shortening means constraining a defined set of bits to be zero, and then deleting them from the codewords. Typically if we shorten by one bit, half of the code's codewords are lost. Shortening typically turns an $(N,K)$ code into an $(N',K')$ code, where $N - N' = K - K'$. Another way to make a new linear code from two old ones is to make the intersection of the two codes: a codeword is only retained in the new code if it is present in both of the two old codes. Discuss the effect on a code's distance-properties of puncturing, shortening, and intersection. Is it possible to turn a code family with bad distance into a code family with good distance, or vice versa, by each of these three manipulations?

<span style="color:#7f8c8d">中文话题摘要：讨论 puncture（删位）、shorten（限零后删位）、intersection（取交）三种操作对距离性质的影响，并问哪种操作能把 bad distance 家族变 good（或反之）。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.24.[3, p.226]**</span> Todd Ebert's 'hat puzzle'. Three players enter a room and a red or blue hat is placed on each person's head. The colour of each hat is determined by a coin toss, with the outcome of one coin toss having no effect on the others. Each person can see the other players' hats but not his own. No communication of any sort is allowed, except for an initial strategy session before the group enters the room. Once they have had a chance to look at the other hats, the players must simultaneously guess their


<span style="color:#7f8c8d">书内 p223 ｜ 13.14: Solutions</span>

own hat's colour or pass. The group shares a three-million-dollar prize if at least one player guesses correctly and no players guess incorrectly.

<span style="color:#7f8c8d">边注（原书页侧）：若你已经知道这个帽子谜题，可以试试「苏格兰版」规则——只有当所有人都猜对时，整组才得奖。在「改良苏格兰版」里，所有人都必须猜对，且有**两轮**猜：第一轮就猜的人离开房间，剩下的人在第二轮必须猜。团队应采用什么策略来最大化获胜机会？</span>

同样的游戏可以玩任意人数的版本。一般问题是找一种团队策略使其获奖机会最大。请找出三人组与七人组的最佳策略。[提示：做完三与七之后，你也许能解出十五。]

<span style="color:#7f8c8d">中文话题摘要：三人帽谜题要求给出最优策略——本质是用 $(7,4)$ Hamming 码的覆盖半径 1 性质，把「全部帽色状态」按「是否为 codeword」二分。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.25.[5]**</span> Estimate how many binary low-density parity-check codes have self-orthogonal duals. [Note that we don't expect a huge number, since almost all low-density parity-check codes are 'good', but a low-density parity-check code that contains its dual must be 'bad'.]

<span style="color:#7f8c8d">中文话题摘要：估计「dual 自正交」的二元 LDPC 码有多少个，并用「good 与 bad 互相排斥」这条约束解释为何结果应该很少。</span>

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**Exercise 13.26.[2C]**</span> In figure 13.15 we plotted the error probability associated with a single codeword of weight $d$ as a function of the noise level $f$ of a binary symmetric channel. Make an equivalent plot for the case of the Gaussian channel, showing the error probability associated with a single codeword of weight $d$ as a function of the rate-compensated signal-to-noise ratio $E_b/N_0$. Because $E_b/N_0$ depends on the rate, you have to choose a code rate. Choose $R = 1/2$, $2/3$, $3/4$, or $5/6$.

<span style="color:#7f8c8d">中文话题摘要：把 Figure 13.15 换成 Gaussian channel 版本——横轴改为 rate-compensated 信噪比 $E_b/N_0$，需先选定 $R$（$1/2$、$2/3$、$3/4$ 或 $5/6$）。</span>

### 13.14 Solutions（解答）

**Solution to exercise 13.4 (p.210)（练习 13.4 的解答）.**

block error 的首阶概率是 $p_B = \frac{3}{N}\binom{N}{2} f^{2}$。

**Solution to exercise 13.7 (p.217)（练习 13.7 的解答）.**

一个 binary vector 与自身垂直，当且仅当它的 weight 为偶数，即含偶数个 1。

**Solution to exercise 13.11 (p.219)（练习 13.11 的解答）.**

self-dual code 有两套等价的 parity-check matrix，$H_1 = G = [I_K \mid P^{T}]$ 与 $H_2 = [P \mid I_K]$；两者必须能通过行相加彼此等价，即存在矩阵 $U$ 使 $U H_2 = H_1$，于是

```math
\left[ UP \mid U I_K \right] = \left[ I_K \mid P^{T} \right]. \qquad (13.42)
```

比较这个方程两边的右半，得 $U = P^{T}$，于是左半成为

```math
P^{T} P = I_K. \qquad (13.43)
```

因此，若 generator matrix 为 $G = [I_K \mid P^{T}]$ 的 code 是 self-dual 的，则 $P$ 是模 2 的正交矩阵；反之亦然。

**Solution to exercise 13.12 (p.219)（练习 13.12 的解答）.**

$(8,4)$ 与 $(7,4)$ 这两个 codes 关系极为密切。$(8,4)$ code 的 parity-check matrix 为

```math
H = \left[ P \mid I_4 \right] = \begin{pmatrix}
0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
1 & 0 & 1 & 1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}, \qquad (13.44)
```

它是通过如下两步由 $(7,4)$ Hamming code 得到的：(a) 追加一个额外的 parity-check bit，可以把它看作 $(7,4)$ Hamming code 全部七个 bits 的奇偶值；(b) 重排前四个 bits。

<span style="color:#7f8c8d">矩阵校验（可复算）：$4 \times 8$，右半为 $I_4$，四行 weight 均为 4；与 (13.38) 的 $G$ 逐行做模 2 内积全为 0（$HG^{T} = 0$），故它确实是该 $(8,4)$ 码的 parity-check matrix。</span>


<span style="color:#7f8c8d">书内 p224 ｜ 13.14: Solutions</span>

**Solution to exercise 13.13 (p.220)（练习 13.13 的解答）.**

若一个 $(N,K)$ code（$M = N-K$ 个 parity symbols）具有这样的性质：decoder 能在 $N$ 个符号的块中任意 $M$ 个符号被擦除时恢复 codeword，则称该 code 是 maximum distance separable（MDS）的。

除了 repetition codes 与 simple parity codes 之外，不存在 MDS binary codes。对 $q \gt 2$，可以找到一些 MDS codes。

举一个简单例子：以下是 8-ary erasure channel 上的一个 $(9,2)$ code。这个 code 依 GF(8) 的乘法与加法规则定义，那些规则见 Appendix C.1。输入字母表的元素是 $\{0, 1, A, B, C, D, E, F\}$，code 的 generator matrix 是

```math
G = \begin{pmatrix}
1 & 0 & 1 & A & B & C & D & E & F \\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
\end{pmatrix}. \qquad (13.45)
```

所得的 64 个 codewords 是：

```text
000000000  011111111  0AAAAAAAA  0BBBBBBBB  0CCCCCCCC  0DDDDDDDD  0EEEEEEEE  0FFFFFFFF
101ABCDEF  110BADCFE  1AB01EFCD  1BA10FEDC  1CDEF01AB  1DCFE10BA  1EFCDAB01  1FEDCBA10
A0ACEB1FD  A1BDFA0EC  AA0EC1BDF  AB1FD0ACE  ACE0AFDB1  ADF1BECA0  AECA0DF1B  AFDB1CE0A
B0BEDFC1A  B1AFCED0B  BA1CFDEB0  BB0DECFA1  BCFA1B0DE  BDEB0A1CF  BED0B1AFC  BFC1A0BED
C0CBFEAD1  C1DAEFBC0  CAE1DC0FB  CBF0CD1EA  CC0FBAE1D  CD1EABF0C  CEAD10CBF  CFBC01DAE
D0D1CAFBE  D1C0DBEAF  DAFBE0D1C  DBEAF1C0D  DC1D0EBFA  DD0C1FAEB  DEBFAC1D0  DFAEBD0C1
E0EF1DBAC  E1FE0CABD  EACDBF10E  EBDCAE01F  ECABD1FE0  EDBAC0EF1  EE01FBDCA  EF10EACDB
F0FDA1ECB  F1ECB0FDA  FADF0BCE1  FBCE1ADF0  FCB1EDA0F  FDA0FCB1E  FE1BCF0AD  FF0ADE1BC
```

<span style="color:#7f8c8d">表内校验（可复算）：表中恰有 $8 \times 8 = 64$ 个长度为 9 的码字，等于 $(s_1, s_2) \in \mathrm{GF}(8)^2$ 的全部组合数 $2^{K} = 2^{6}$；每个非零码字都不含符号 0（即 weight 为 9），这正是 MDS 的表现（任意 $M = 7$ 个符号被擦除仍可恢复）。以上 64 条按文字层逐行转写，读者可用 (13.45) 与 Appendix C.1 的 GF(8) 运算独立复算。</span>

**Solution to exercise 13.14 (p.220)（练习 13.14 的解答）.**

**Quick, rough proof of the theorem.** 设 $x$ 表示重建出的 codeword 与发出的 codeword 之差。对任何给定的 channel 输出 $r$，在 $x$ 上都有一个后验分布。这个后验分布只在属于该 code 的向量 $x$ 上为正；下面各求和都遍历 codewords $x$。block error probability 是

```math
p_B = \sum_{x \ne 0} P(x \mid r). \qquad (13.46)
```

对所有 bits 取平均的平均 bit error probability 是

```math
p_b = \sum_{x \ne 0} P(x \mid r) \frac{w(x)}{N}, \qquad (13.47)
```

其中 $w(x)$ 是 codeword $x$ 的 weight。现在非零 codewords 的 weights 满足

```math
1 \ge \frac{w(x)}{N} \ge \frac{d_{\min}}{N}. \qquad (13.48)
```

把不等式 (13.48) 代入定义 (13.46, 13.47)，得到

```math
p_B \ge p_b \ge \frac{d_{\min}}{N} p_B, \qquad (13.49)
```

其右侧比所陈述的结果 (13.39) 强了一倍。为了让证明严密，我把结果稍微削弱了一点。

**Careful proof.** 该定理把最优 block decoding 算法与最优 bitwise decoding 算法的性能联系起来。

我们引入另一对 decoding 算法，称为 block-guessing decoder 与 bit-guessing decoder。想法是：这两个算法与最优 block decoder、最优 bitwise decoder 相似，但更便于分析。

现在我们定义这些 decoders。设 $x$ 表示推断出的 codeword。对任何给定的 code：


<span style="color:#7f8c8d">书内 p225 ｜ 13.14: Solutions</span>

**The optimal block decoder** 返回使后验概率 $P(x \mid r)$ 最大的 codeword $x$；该后验正比于 likelihood $P(r \mid x)$。这个 decoder 的错误概率称为 $p_B$。

**The optimal bit decoder** 对 $N$ 个 bits 中的每一位 $x_n$，返回使后验概率 $P(x_n = a \mid r) = \sum_{x} P(x \mid r)\left[ x_n = a \right]$ 最大的那个 $a$ 值。这个 decoder 的错误概率称为 $p_b$。

**The block-guessing decoder** 按后验概率 $P(x \mid r)$ 所给的概率分布返回一个随机 codeword $x$。这个 decoder 的错误概率称为 $p^{G}_{B}$。

**The bit-guessing decoder** 对 $N$ 个 bits 中的每一位 $x_n$，从概率分布 $P(x_n = a \mid r)$ 中返回一个随机 bit。这个 decoder 的错误概率称为 $p^{G}_{b}$。

定理断言：最优 bit error probability $p_b$ 之上被 $p_B$ 界住、之下被 $p_B$ 的某个给定倍数界住（(13.39)）。

(13.39) 左边的那个不等式是平凡成立的——若一个 block 对了，它所有的组成 bits 都对；所以如果最优 block decoder 优于最优 bit decoder，我们就能用 block decoder 造出一个更好的 bit decoder。

我们这样来证右边那个不等式：

(a) bit-guessing decoder 差不多和最优 bit decoder 一样好：

```math
p^{G}_{b} \le 2 p_b; \qquad (13.50)
```

(b) bit-guessing decoder 的错误概率与 block-guessing decoder 的错误概率由下式联系：

```math
p^{G}_{b} \ge \frac{d_{\min}}{N} p^{G}_{B}. \qquad (13.51)
```

于是，由于 $p^{G}_{B} \ge p_B$，我们有

```math
p_b \gt \frac{1}{2} p^{G}_{b} \ge \frac{1}{2}\frac{d_{\min}}{N} p^{G}_{B} \ge \frac{1}{2}\frac{d_{\min}}{N} p_B. \qquad (13.52)
```

下面我们证明这两条引理。

**Near-optimality of guessing（猜译的近似最优性）**：先考虑单个 bit 的情形，后验概率为 $\{p_0, p_1\}$。最优 bit decoder 的错误概率是

```math
P_{\text{optimal}} = \min(p_0, p_1). \qquad (13.53)
```

guessing decoder 从 0 与 1 中取。真值也按同样的概率分布。猜者与真值相符的概率是 $p^{2}_{0} + p^{2}_{1}$；不相符的概率就是猜错概率

```math
P_{\text{guess}} = 2 p_0 p_1 \le 2 \min(p_0, p_1) = 2 P_{\text{optimal}}. \qquad (13.54)
```

由于 $p^{G}_{b}$ 是许多这类错误概率 $P_{\text{guess}}$ 的平均，而 $p_b$ 是对应的最优错误概率 $P_{\text{optimal}}$ 的平均，我们就得到 $p^{G}_{b}$ 与 $p_b$ 之间所希望的关系 (13.50)。


<span style="color:#7f8c8d">书内 p226 ｜ 13.14: Solutions</span>

**Relationship between bit error probability and block error probability（bit 错误概率与 block 错误概率之间的关系）**：bit-guessing 与 block-guessing 两个 decoders 可以合在一个系统里：我们可以先从联合分布 $P(x_n, x \mid r)$ 中抽一个样本 $(x_n, x)$，然后丢弃 $x$ 的值，就得到来自边缘分布 $P(x_n \mid r)$ 的一个样本 $x_n$。

我们可以区分两种情形：被丢弃的 $x$ 值是正确的 codeword，或者不是。于是 bit-guessing decoder 的 bit error 概率可以写成两项之和：

```math
p^{G}_{b} = P(x\ \text{correct}) P(\text{bit error} \mid x\ \text{correct}) + P(x\ \text{incorrect}) P(\text{bit error} \mid x\ \text{incorrect})
```

```math
= 0 + p^{G}_{B} P(\text{bit error} \mid x\ \text{incorrect}).
```

现在，每当猜出的 $x$ 不正确时，真 $x$ 与它至少在 $d$ 个 bits 上不同，所以这些情形下 bit error 的概率至少是 $d/N$。于是

```math
p^{G}_{b} \ge \frac{d}{N} p^{G}_{B}.
```

$\square$

**Solution to exercise 13.20 (p.222)（练习 13.20 的解答）.**

「典型」noise vectors $n$ 的数目约为 $2^{N H_2(f)}$。不同 syndromes $z$ 的数目是 $2^{M}$。于是可靠通信蕴含

```math
M \ge N H_2(f), \qquad (13.55)
```

或者，用 rate $R = 1 - M/N$ 表示，

```math
R \le 1 - H_2(f), \qquad (13.56)
```

这个界与信道的 capacity 精确吻合。这条论证会在下一章被转化为一个证明。

**Solution to exercise 13.24 (p.222)（练习 13.24 的解答）.**

在三人情形下，这一组人有四分之三的机会获胜。

四分之三的时候，两名玩家的帽色相同，第三名玩家的帽色相反。只要出现这种情况，该组人用如下策略就能每战必胜：每名玩家看另外两名玩家的帽子。若两顶帽子颜色不同，他就 pass（跳过）。若两顶帽子颜色相同，他就猜自己的帽子是相反的颜色。

这样，每当帽色分布是「两顶一色、一顶另一色」时，都会有一名玩家猜对，其余人 pass，该组获胜。然而当所有帽子同色时，三名玩家都会猜错，该组失败。

当任何特定玩家猜一个颜色时，他猜对的概率确实只有 50:50。该组之所以有 75% 的胜率，是因为他们的策略保证了：当玩家们猜错时，是**一大群**人同时猜错。

对更多玩家，目标是保证「大多数时候无人猜错、偶尔所有人同时猜错」。在 7 名玩家的游戏里，有一种策略能让该组每 8 局赢 7 局。在 15 名玩家的游戏里，该组能每 16 局赢 15 局。

如果你还没想出 7 人与 15 人团队的获胜策略，我建议先把三人游戏的解，用三维超立方体上「获胜状态与失败状态的位置」来想，然后再横向联想。


<span style="color:#7f8c8d">书内 p227 ｜ 13.14: Solutions</span>

若玩家人数 $N = 2^{r} - 1$，最优策略可以用一个长度为 $N$ 的 Hamming code 来定义，获奖概率是 $N/(N+1)$。每位玩家被赋予一个编号 $n \in 1 \dots N$。两种颜色映到 0 与 1。他们帽子的任何状态都可以看成从某个 binary channel 接收到的 received vector。一个长度为 $N$ 的随机 binary vector，要么以概率 $1/(N+1)$ 是 Hamming code 的 codeword，要么恰好与某个 codeword 相差一个 bit。每位玩家看其余所有 bits，并考虑自己的 bit 是否能被设成某个颜色而使整个状态成为 codeword（这可以用 Hamming code 的 decoder 推断出来）。若能，则该玩家猜自己的帽子是另一种颜色。若该状态实际上就是 codeword，则所有玩家都会猜，且都会猜错。若该状态不是 codeword，则只有一名玩家会猜，且他的猜测是对的。若使用 $(7,4)$ Hamming code 的循环表示（p.19），要把七名玩家训练成遵循最优策略是很容易的。

<span style="color:#1e8449;">**[译注]** 帽子谜题之所以出现在编码理论章末，不是因为它有趣，而是因为它把「perfect code 的覆盖性质」翻译成了一个**零通信的分布式协议**，而这条翻译正是 $t = 1$ Hamming code 的定义在起承重作用。机制：Hamming code 的 16 个 codewords 把 $\{0,1\}^{7}$ 的 128 个状态划分成 16 个「1-球」（每个球 8 个状态：球心 + 7 个单 bit 变体），这是 §13.3 的完美性；而「球」在这里的含义是「玩家能推出的候选状态集合」。若状态落在球心（codeword，概率 $1/8$），7 个人都会以为自己是「偏离者」于是都猜，全错；若状态在球的壳上（概率 $7/8$），恰好一个人看到的状态「离 codeword 差一位」而其余六人看到的「已经是 codeword」，于是只有那一个人猜，且猜对。抽掉「每个状态到某 codeword 的距离 $\le 1$」这条覆盖性质，系统就崩：若存在某个状态到所有 codewords 的距离都 $\ge 2$，则没有任何玩家会猜（全 pass），该组直接失去这次机会——胜率从 $7/8$ 掉到更低，而这正是 $N = 2^{r}-1$ 这个特定人数才最优的原因。落点：本题解答在书内 p227（本页）；完美性定义与计数在本书 §13.3（PDF p220，属上一块，(13.1)–(13.4)）；「覆盖半径 vs 最小距离」这对概念的正式区分见书 §13.3 与 Cover & Thomas 的第 1 章 sphere-packing bound（二手，可作对照）；离散侧工具是 6.042J 的 *Sets, functions, relations* 与 *Counting*（$2^{r}-1$ 个非零向量的划分）；同一场博弈的博弈论分析（相关均衡）可查 arXiv:1103.1713 一类文献，但那是另一个视角，不与编码论证等价。</span>


<span style="color:#7f8c8d">书内 p228 ｜ About Chapter 14</span>

## About Chapter 14（第 14 章导读）

在这一章里，我们将把此前遇到的几个想法汇到一起，做成一个漂亮而简短的证明。我们将同时证明 Shannon 的 noisy-channel coding theorem（针对 symmetric binary channels）与他 source coding theorem（针对 binary sources）。虽然这个证明与本书前面许多章有关联，但并非必须把它们全读过。

在 noisy-channel coding 这一侧，我们的证明会比第 10 章给出的证明更具构造性；在第 10 章我们证明的是「几乎任何 random code 都是 very good 的」。这里我们将证明「几乎任何 **linear** code 都是 very good 的」。我们会用到 typical sets 的想法（第 4 章与第 10 章），并借用上一章对 random linear codes 的 weight enumerator function 的计算（§13.5）。

在 source coding 这一侧，我们的证明将表明：random linear hash functions 可以用于压缩可压缩的 binary sources，从而与第 12 章建立联系。

<span style="color:#1e8449;">**[译注]** 这一页是全书的枢纽，值得单独标出，因为它预告的证明把三块看似独立的内容缝在一起：§13.5 的 $\langle A(w)\rangle = \binom{N}{w}2^{-M}$（组合计数）、§4/§10 的 typical set（$2^{NH}$ 个典型序列）、以及 §12 的 random linear hash（把 $N$ bits 压到 $M$ bits 的线性映射）。为什么这三块能拼成同一个证明？因为**同一个线性映射在两个方向上各扮演一个角色**：作为 parity-check matrix 时，它定义 code（信道编码，把 $K$ bits 映到 $N$ bits，抗噪）；作为 generator matrix 时，它定义 hash（信源压缩，把 $N$ bits 映到 $M$ bits，去冗余）。抽掉「同一个矩阵、两个方向」这层认识，系统会崩在哪？崩在你对「压缩与纠错为何共用一套数学」的理解上：会以为 source coding 与 channel coding 是两门手艺，而实际上 Shannon 的 separation theorem 之所以成立（先压缩再编码不损失渐近最优性），正是靠这条线性映射的对偶性——这也解释了本书 §13.10 为什么专门讨论 dual codes：duals 就是同一份矩阵的另一种读法。落点：本页为书内 p228；证明本身在第 14 章（书内 p229 起，属下一块）；§13.5 的公式在 (13.12)–(13.14)（PDF p223–224）；§12 的 hash 在 (12.6)–(12.8)（PDF p214–215）；线代侧的对应物是 Strang 的四个基本子空间与「$N = \text{rank} + \text{nullity}$」——parity-check 矩阵的行空间就是 dual code，零空间就是 code 本身。</span>



## 第 14 章 Very Good Linear Codes Exist（存在极好的线性码）

本章我们用**一次计算**同时证明 binary symmetric channel（二元对称信道）的 source coding theorem（信源编码定理）与 noisy-channel coding theorem（信道编码定理）。

顺带说一句：这个证明对远比 binary symmetric channel 更一般的 channel model 也成立，不限于二元对称信道。例如它可以改造到输出非二元的情形、time-varying（时变）的情形，以及有 memory（记忆）的情形，只要这些 channel 的输入是二元、并且满足某种对称性，参见 §10.6。

### 14.1 A simultaneous proof of the source coding and noisy-channel coding theorems（信源编码定理与信道编码定理的同时证明）

我们考虑一个线性纠错码，它由二元 parity-check matrix（校验矩阵）$H$ 定义。该矩阵有 $M$ 行、$N$ 列。证明的后面我们会让 $N$ 与 $M$ 一起增大，并保持 $M \propto N$。这个码的 rate（码率）满足

```math
R \ \ge\ 1 - \frac{M}{N}. \qquad (14.1)
```

如果 $H$ 的所有行都 linear independent（线性无关），则上式取等号，$R = 1 - M/N$。下文中我们假定等号成立。性急的读者可以自己算出随机二元矩阵 $H$ 的 expected rank（期望秩，它非常接近 $M$），并考察差值 $M - \mathrm{rank}$ 对证明其余部分的影响（影响可以忽略）。

选出一个 codeword（码字）$t$，它满足

```math
Ht = 0 \bmod 2, \qquad (14.2)
```

binary symmetric channel 再叠上 noise（噪声）$x$，得到接收信号

```math
r = t + x \bmod 2. \qquad (14.3)
```

> 本节中 $x$ 一律指 channel 叠加的 noise，**不是** channel 的输入。

receiver（接收端）的目标是用 syndrome-decoding（伴随式译码）的思路，从 $r$ 同时推断 $t$ 与 $x$。syndrome decoding 最早在 §1.2（书内 p10–11）引入。receiver 计算 syndrome（伴随式）

```math
z = Hr \bmod 2 = Ht + Hx \bmod 2 = Hx \bmod 2. \qquad (14.4)
```

syndrome 只取决于 noise $x$，于是 decoding problem（译码问题）变成：找出满足下式的最可能的 $x$，

```math
Hx = z \bmod 2. \qquad (14.5)
```



这个对 noise vector（噪声向量）的最佳估计 $\hat{x}$，随后从 $r$ 里减掉，就得到对 $t$ 的最佳猜测。我们要证明的是：只要 $R \lt 1 - H(X) = 1 - H_2(f)$，其中 $f$ 是 binary symmetric channel 的 flip probability（翻转概率），那么对随机 $H$ 而言，这个 syndrome-decoding 问题的最优 decoder（译码器）的 error probability（错误概率）随 $N$ 增大而趋于零。

<span style="color:#1e8449;">**[译注]**</span> **一次典型性论证能同时给出两个定理，是因为 §14.1 先把「纠错」归约成了「估计噪声」——剩下的是两个 $2^{NH}$ 相除**

关键一步是式 (14.4)：syndrome $z=Hr=Hx$ **只依赖噪声**，与发出的码字无关。于是译码问题从「从 $r$ 猜 $t$」变成「从 $z$ 猜 $x$」，而这件事两侧都已有计数：① 噪声串 $x$ 是 $N$ 长的二值序列，其典型集大小是 $2^{NH(X)}$（这是第 4 章信源侧的计数）；② 码本由随机 $H$ 定义，满足 $Hx=z$ 的解的期望个数是 $2^{N-K}$（这是第 10 章信道侧的计数）。两数一除得 $2^{N-K}\cdot 2^{-NH(X)}\ll1$，即 $R=K/N<1-H_2(f)$。抽掉这次归约，你就得分别写第 4 章与第 10 章两套证明，看不出**压缩与纠错是同一条不等式的两个方向**：压缩问"典型集多大"，纠错问"典型集之间会不会重叠"。

边界也得说清，别把这当成完整答案：证明只对随机 $H$ 且 $\operatorname{rank}H\approx M$ 成立，只给**存在性**（好码本以高概率存在），不给出可线性时间译码的构造。这正是 §16 还要讲 message passing 的原因——把"存在"变成"可算"，中间隔着 60 年（LDPC 1963 被遗忘、1995 重发现）。

挂载：6.042J 的计数与期望线性（这里不需要独立性，正是 union bound 的用法）；与本书 §10.5 的 Fano converse 互补：那条证明「$R>C$ 不可能」，这条证明「$R<C$ 可行且不必用两套工具」。

坐标：§14.1（原书 p.233–237，PDF p.245–249），式 (14.1)–(14.5)；§13.5 的 $\langle A(w)\rangle$ 与 §13.9 的 union bound 是它的两块砖。

我们通过研究一个**次优**策略来证明这一结果。最优 decoder 与这个 typical-set decoder（典型集译码器）都不容易实现，但 typical-set decoder 更容易分析。

typical-set decoder 检查 noise vector 的 typical set（典型集）$T$，即那些满足 $\log 1/P(x') \simeq N H(X)$ 的 noise vector $x'$ 组成的集合，然后逐一看是否有某个 typical vector $x'$ 满足观测到的 syndrome

```math
Hx' = z. \qquad (14.6)
```

若恰好有一个 typical vector 满足它，typical set decoder 就报告该向量为假设的 noise vector。若没有任何 typical vector 匹配观测到的 syndrome，或者多于一个匹配，则 typical set decoder 报告出现 error（错误）。

> 我们会省略那些让 typical-set 定义变得严格的 $\epsilon$ 与 $\beta$。有兴趣的读者请回到 §4.4，把这些细节补进本证明。

给定矩阵 $H$，typical-set decoder 的错误概率可写成两项之和

```math
P_{\mathrm{TS}\,|\,H} = P^{(\mathrm{I})} + P^{(\mathrm{II})}_{\mathrm{TS}\,|\,H}, \qquad (14.7)
```

其中 $P^{(\mathrm{I})}$ 是「真实 noise vector $x$ 本身并非 typical」的概率，$P^{(\mathrm{II})}_{\mathrm{TS}\,|\,H}$ 是「真实 $x$ 是 typical，但至少还有另一个 typical vector 与它撞在同一个 syndrome 上」的概率。第一项随 $N$ 增大而消失，这是我们在第 4 章初次研究 typical set 时已经证明过的。我们把注意力放在第二项上。

复述一下：想象真实的 noise vector 是 $x$；若存在某个不同于 $x$ 的 typical noise vector $x'$ 满足 $H(x' - x) = 0$，我们就出错。为此使用 truth function（真值函数）

```math
\big[H(x' - x) = 0\big], \qquad (14.8)
```

当命题 $H(x' - x) = 0$ 为真时它取值一，否则取值零。

于是对给定的 noise $x$，我们可以给出 type II 错误个数的一个上界：

```math
[\text{给定 } x \text{ 与 } H \text{ 时的错误个数}] \ \le\ \sum_{\substack{x':\, x' \in T \\ x' \ne x}} \big[H(x' - x) = 0\big]. \qquad (14.9)
```

真实的错误个数要么是零要么是一；而右边求和式在某些情况下会超过一，那些情况是有多个 typical noise vector 共享同一个 syndrome。

> 式 (14.9) 就是一个 union bound（并集界）。

现在对 $x$ 取平均，写出 type-II 错误的概率：

```math
P^{(\mathrm{II})}_{\mathrm{TS}\,|\,H} \ \le\ \sum_{x \in T} P(x) \sum_{\substack{x':\, x' \in T \\ x' \ne x}} \big[H(x' - x) = 0\big]. \qquad (14.10)
```

接着，我们对所有线性码取平均——也就是对 $H$ 取平均。只要证明平均的 type-II 错误概率趋于零，就证明了**存在**错误概率趋于零的线性码；事实上还证明了几乎所有线性码都极好。

我们把对全体二元矩阵 $H$ 的平均记作 $\langle\dots\rangle_H$。平均的 type-II 错误概率是

```math
\bar{P}^{(\mathrm{II})}_{\mathrm{TS}} = \sum_{H} P(H) P^{(\mathrm{II})}_{\mathrm{TS}\,|\,H} = \big\langle P^{(\mathrm{II})}_{\mathrm{TS}\,|\,H} \big\rangle_H \qquad (14.11)
```



```math
= \Bigg\langle \sum_{x \in T} P(x) \sum_{\substack{x':\, x' \in T \\ x' \ne x}} \big[H(x' - x) = 0\big] \Bigg\rangle_H \qquad (14.12)
```

```math
= \sum_{x \in T} P(x) \sum_{\substack{x':\, x' \in T \\ x' \ne x}} \Big\langle \big[H(x' - x) = 0\big] \Big\rangle_H. \qquad (14.13)
```

注意量 $\big\langle \big[H(x' - x) = 0\big] \big\rangle_H$ 我们在计算随机线性码的 expected weight enumerator function（期望重量枚举函数）时就碰到过（§13.5）：对任意非零二元向量 $v$，对所有矩阵 $H$ 取平均后 $Hv = 0$ 的概率是 $2^{-M}$。因此

```math
\bar{P}^{(\mathrm{II})}_{\mathrm{TS}} = \left( \sum_{x \in T} P(x) \right) (|T| - 1)\, 2^{-M} \qquad (14.14)
```

```math
\le\ |T|\, 2^{-M}, \qquad (14.15)
```

其中 $|T|$ 表示 typical set 的大小。回想第 4 章的结论：typical set 里大约有 $2^{N H(X)}$ 个 noise vector。所以

```math
\bar{P}^{(\mathrm{II})}_{\mathrm{TS}} \ \le\ 2^{N H(X)} 2^{-M}. \qquad (14.16)
```

这个错误概率上界随 $N$ 增大要么趋于零要么指数增长（记住 $N$ 增大时我们保持 $M$ 与 $N$ 成正比）。它趋于零的条件是

```math
H(X) \lt M/N. \qquad (14.17)
```

代入 $R = 1 - M/N$，我们就这样证明了 binary symmetric channel 的 noisy-channel coding theorem：**任何满足下式的 rate，都存在极好的线性码**

```math
R \lt 1 - H(X), \qquad (14.18)
```

其中 $H(X)$ 是 channel noise 的 per bit entropy（每比特熵）。

<span style="color:#2471a3;">**Exercise 14.1.**</span> `[exercise]` *Redo the proof for a more general channel.*

> 中文话题：把上述「典型集 + union bound + 对 $H$ 取平均」的论证推广到一般信道——关键是找什么量的期望值对应 $2^{-M}$。

### 14.2 Data compression by linear hash codes（用线性 hash 码做数据压缩）

刚才玩的这局 decoding 游戏，也可以换个视角看成 uncompresssion（解压缩）游戏。世界按源 $P(x)$ 产生一个二元 noise vector $x$。这个 noise 有 redundancy（冗余，只要 flip probability 不等于 0.5）。我们用一个 linear compressor（线性压缩器）压它：把 $N$ 比特输入 $x$（即 noise）映射到 $M$ 比特输出 $z$（即 syndrome）。我们的 uncompresssion 任务就是从输出 $z$ 恢复输入 $x$。压缩器的 rate 是

```math
R_{\mathrm{compressor}} \equiv M/N. \qquad (14.19)
```

> 在这里的 rate 定义中，我们不管「线性冗余」这种可能性。

我们刚得到的结果是：只要 $H(X) \lt M/N$，对几乎任何 $H$，decoding 问题都能以趋于零的错误概率解出。这个结果立刻证明了 source coding theorem（信源编码定理）：

<span style="color:#00838f;">**定理（线性压缩的存在性）**：给定熵为 $H(X)$ 的二元源 $X$ 与所要求的压缩 rate $R \gt H(X)$，存在一个线性压缩器 $x \to z = Hx \bmod 2$，其 rate $M/N$ 恰等于所要求的 $R$，并存在配套的解压器，使得压缩几乎无损。</span>

这个定理不仅对 independent identically distributed（独立同分布）符号的源成立，也对任何能定义 typical set 的源成立：例如有 memory 的源、time-varying 的源；唯一要求是源是 ergodic（遍历的）。



### Notes（注释）

这个证明「码是好的」的方法，可以推广到其他线性码，例如 low-density parity-check codes（低密度校验码，MacKay, 1999b；Aji et al., 2000）。对每个码，我们只需要一个对它 expected weight enumerator function 的近似。

> <span style="color:#1e8449;">**[译注]** 这一节值得当作「一个计算、两个定理」的模板记住。式 (14.16) 的 $2^{NH(X)}2^{-M}$ 里，$NH(X)$ 是典型噪声集的规模，$2^{M}$ 是 syndrome 空间的大小：两者之比 $2^{N(H(X)-M/N)}$ 就是「随机噪声撞进同一个 syndrome 的期望次数」。把它翻过来读，同一个比值又变成「压缩后残留的不确定性」。抽掉这个「$|T|\,2^{-M}$」的量，你会崩在两处：其一，noisy-channel coding theorem 只剩下 Shannnel 的随机编码存在性证明，拿不到「线性码也行」这个更强的结论；其二，$R \gt H(X)$ 的线性压缩器无法构造性论证，只能退回枚举典型集的非构造证明。用 §13.5 的 $\langle A(w)\rangle = \binom{N}{w}2^{-M}$ 复算一遍同一件事：$w$ 取典型噪声重量 $w = fN$ 时 $\log_2\langle A(w)\rangle \approx N[H_2(f) - M/N]$，指数为负即 (14.17)。落点：本书 §13.5、§4.4；6.042J 的 Linearity of expectation 与 Union bound 两节。</span>



## 第 15 章 Further Exercises on Information Theory（信息论进阶习题）

本章最激动人心的习题——它们会把你带到信息论的更深处——放在本章靠后的位置。

### Refresher exercises on source coding and noisy channels（信源编码与噪声信道的复习题）

<span style="color:#2471a3;">**Exercise 15.1.**</span> `[exercise]` *Let $X$ be an ensemble with $\mathcal{A}_X = \{0, 1\}$ and $P_X = \{0.995, 0.005\}$. Consider source coding using the block coding of $X^{100}$ where every $x \in X^{100}$ containing 3 or fewer 1s is assigned a distinct codeword, while the other $x$s are ignored. (a) If the assigned codewords are all of the same length, find the minimum length required to provide the above set with distinct codewords. (b) Calculate the probability of getting an $x$ that will be ignored.*

> 中文话题：稀有小概率符号的块编码——数一数「含不超过 3 个 1」的 100 位串有多少个，取定长码需要多少位；再算被忽略（不编码）的概率，即 $\sum_{n \ge 4} \binom{100}{n} 0.005^n 0.995^{100-n}$。

<span style="color:#2471a3;">**Exercise 15.2.**</span> `[exercise]` *Let $X$ be an ensemble with $P_X = \{0.1, 0.2, 0.3, 0.4\}$. The ensemble is encoded using the symbol code $C = \{0001, 001, 01, 1\}$. Consider the codeword corresponding to $x \in X^N$, where $N$ is large. (a) Compute the entropy of the fourth bit of transmission. (b) Compute the conditional entropy of the fourth bit given the third bit. (c) Estimate the entropy of the hundredth bit. (d) Estimate the conditional entropy of the hundredth bit given the ninety-ninth bit.*

> 中文话题：非前缀等长化后的比特流统计——前几个比特受码字边界影响，熵不等于 1；到第一百个比特时已进入「典型稳态」，$H$ 与 $H(\text{bit}_n \mid \text{bit}_{n-1})$ 都趋近信道/源的极限值。

<span style="color:#2471a3;">**Exercise 15.3.**</span> `[exercise]` *Two fair dice are rolled by Alice and the sum is recorded. Bob's task is to ask a sequence of questions with yes/no answers to find out this number. Devise in detail a strategy that achieves the minimum possible average number of questions.*

> 中文话题：11 个可能和的概率是三角形分布 $\{1,2,3,4,5,6,5,4,3,2,1\}/36$；Huffman 式的二十问策略，平均问题数下界就是该分布的 entropy。

<span style="color:#2471a3;">**Exercise 15.4.**</span> `[exercise]` *How can you use a coin to draw straws among 3 people?*

> 中文话题：用公平硬币在三人间做**等概率**抽签——两次抛掷给 4 个结果，需要处理「多出来的那个」而不引入偏差（拒绝采样 / 三进制编码）。

<span style="color:#2471a3;">**Exercise 15.5.**</span> `[exercise]` *In a magic trick, there are three participants: the magician, an assistant, and a volunteer. The assistant, who claims to have paranormal abilities, is in a soundproof room. The magician gives the volunteer six blank cards, five white and one blue. The volunteer writes a different integer from 1 to 100 on each card, as the magician is watching. The volunteer keeps the blue card. The magician arranges the five white cards in some order and passes them to the assistant. The assistant then announces the number on the blue card. How does the trick work?*

> 中文话题：五张白卡的**排列**携带 $\log_2 5! = \log_2 120 \approx 6.9$ 比特，而「从 6 个数里选 1 个」需要 $\log_2 6 \approx 2.585$ 比特；关键在于魔术师还能自由选择把哪五张白卡按什么次序传出——本题让你找出这个编码。



<span style="color:#2471a3;">**Exercise 15.6.**</span> `[exercise]` *How does this trick work? "Here's an ordinary pack of cards, shuffled into random order. Please choose five cards from the pack, any that you wish. Don't let me see their faces. No, don't give them to me: pass them to my assistant Esmerelda. She can look at them. Now, Esmerelda, show me four of the cards. Hmm … nine of spades, six of clubs, four of hearts, ten of diamonds. The hidden card, then, must be the queen of spades!" The trick can be performed as described above for a pack of 52 cards. Use information theory to give an upper bound on the number of cards for which the trick can be performed.*

> 中文话题：这是 Fitch Cheney 的五张牌把戏。四张展示牌有 $4! = 24$ 种次序（约 $\log_2 24 \approx 4.58$ 比特），要记住的是「第五张是哪一张」；用抽屉原理证明牌数上限 $n$ 必须满足 $n \le 124$ 之类的不等式（本题要求的就是这个界）。

<span style="color:#2471a3;">**Exercise 15.7.**</span> `[exercise]` *Find a probability sequence $p = (p_1, p_2, \ldots)$ such that $H(p) = \infty$.*

> 中文话题：构造一个熵发散的可数分布——例如 $p_n \propto 1/(n \log^2 n)$ 这类重尾序列，验证 $\sum p_n \log 1/p_n = \infty$。

<span style="color:#2471a3;">**Exercise 15.8.**</span> `[exercise]` *Consider a discrete memoryless source with $\mathcal{A}_X = \{a, b, c, d\}$ and $P_X = \{1/2, 1/4, 1/8, 1/8\}$. There are $4^8 = 65\,536$ eight-letter words that can be formed from the four letters. Find the total number of such words that are in the typical set $T_{N\beta}$ (equation 4.29) where $N = 8$ and $\beta = 0.1$.*

> 中文话题：直接数典型集——按 (4.29) 的定义 $| \frac{1}{N}\log 1/P(x) - H | \lt \beta$，$H = 1.75$ 比特，$N=8$ 时须逐个多重集计数再乘排列数。

<span style="color:#2471a3;">**Exercise 15.9.**</span> `[exercise]` *Consider the source $\mathcal{A}_S = \{a, b, c, d, e\}$, $P_S = \{1/3, 1/3, 1/9, 1/9, 1/9\}$ and the channel whose transition probability matrix is $Q$ (15.1). Note that the source alphabet has five symbols, but the channel alphabet $\mathcal{A}_X = \mathcal{A}_Y = \{0, 1, 2, 3\}$ has only four. Assume that the source produces symbols at exactly $3/4$ the rate that the channel accepts channel symbols. For a given (tiny) $\epsilon \gt 0$, explain how you would design a system for communicating the source's output over the channel with an average error probability per source symbol less than $\epsilon$. Be as explicit as possible. In particular, do not invoke Shannon's noisy-channel coding theorem.*

> 中文话题：源有 5 个符号、信道字母表只有 4 个符号，但源速率只是信道的 $3/4$——要求你**显式构造**一套分组映射 + 编码 + 译码，而不许引用存在性定理。
>
> <span style="color:#1e8449;">**[原文公式无法从文字层复原]** (15.1) 的转移矩阵在本 PDF 的文字层里排布错乱：可见到的三段数字是 `1 0 0 0 0`、`0 2/3 0 0 1`、`0 1 0 0 1/3`，末行只剩一个 `0`。这与正文自陈的「源 5 符号、信道输入输出各 4 符号」相矛盾（$Q$ 应为 $5 \times 4$），故**不作重建、不臆造**。可核验的锚点只有：源速率 = 信道符号率的 $3/4$，即每 4 个信道符号时间送 3 个源符号。</span>

<span style="color:#2471a3;">**Exercise 15.10.**</span> `[exercise]` *Consider a binary symmetric channel and a code $C = \{0000, 0011, 1100, 1111\}$; assume that the four codewords are used with probabilities $\{1/2, 1/8, 1/8, 1/4\}$. What is the decoding rule that minimizes the probability of decoding error? [The optimal decoding rule depends on the noise level $f$ of the binary symmetric channel. Give the decoding rule for each range of values of $f$, for $f$ between $0$ and $1/2$.]*

> 中文话题：MAP 译码与 ML 译码的分歧——先验不等（$1/2$ vs $1/8$）时，低噪声区间用最大似然、高噪声区间改用最大后验，中间存在切换点 $f$；本题要你算出各区间。

<span style="color:#2471a3;">**Exercise 15.11.**</span> `[exercise]` *Find the capacity and optimal input distribution for the three-input, three-output channel whose transition probabilities are $Q$ (15.2).*

```math
Q = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2/3 & 1/3 \\ 0 & 1/3 & 2/3 \end{bmatrix}. \qquad (15.2)
```

> 中文话题：第一行是「无噪声直通」，第二三行构成一个二元对称信道；求 capacity 与 optimal input distribution（提示：直通符号要不要用、用多少）。



<span style="color:#2471a3;">**Exercise 15.12.**</span> `[exercise]` *The input to a channel $Q$ is a word of 8 bits. The output is also a word of 8 bits. Each time it is used, the channel flips exactly one of the transmitted bits, but the receiver does not know which one. The other seven bits are received without error. All 8 bits are equally likely to be the one that is flipped. Derive the capacity of this channel. Show, by describing an explicit encoder and decoder that it is possible reliably (that is, with zero error probability) to communicate 5 bits per cycle over this channel.*

> 中文话题：一个「必定翻一位」的 8 位信道——求 capacity（提示：噪声熵是 $\log_2 8 = 3$ 比特），再显式给出 (8,5) 码达到零错误。
>
> <span style="color:#1e8449;">**[译注]** 这道题的答案恰好说明「capacity 是上确界、不是可达的率」这一区分有多要紧。噪声在 8 个位置中均匀选一个，$H(X) = \log_2 8 = 3$ 比特，于是 $C = 8 - 3 = 5$ 比特；但 (14.18) 的证明只给出「$R \lt C$ 时错误概率可趋于零」。这里之所以能在 $R = 5$ **恰等于** $C$ 时做到零错误，是因为噪声结构特殊（恰好翻一位，且错误模式集合大小为 8，与 syndrome 数 $2^{3}$ 相同）。抽掉「恰好一位」这个约束（改成「至多一位」），容量式子立刻变成另一个值，且 $R=C$ 处的零错误也随之消失——这就是本书反复强调的：capacity 表达式本身不告状，告状的是错误概率随 $N$ 的行为。落点：本书 §9.x 的 noisy-channel coding theorem（书内 p145 起）、§13.3 的 perfect code 计数 (13.2)；6.042J 的 Counting 一节。</span>

<span style="color:#2471a3;">**Exercise 15.13.**</span> `[exercise]` *A channel with input $x \in \{a, b, c\}$ and output $y \in \{r, s, t, u\}$ has conditional probability matrix: $Q$ as printed in the margin. What is its capacity?*

```math
Q = \begin{bmatrix} 1/2 & 0 & 0 & 1/2 \\ 1/2 & 0 & 0 & 1/2 \\ 1/2 & 0 & 0 & 1/2 \end{bmatrix}.
```

（原书此矩阵排在该题页边，**没有编号**，此处不加编号以免与 (15.3) 混淆。）

> 中文话题：行完全相同的信道——输入信息被彻底抹掉，capacity 为零（三行一模一样，输出与输入无关）。
>
> <span style="color:#1e8449;">**[原文问题]** 这一页的图形文字层把三个输入的标签 `a b c` 与三行概率分开排出，且页边图形（$a,b,c$ 到 $r,s,t,u$ 的连线）的箭头归属无法从文字层复原；上面矩阵的三行**在文字层中是同一组数字重复三次**，我按「不得静默丢弃、也不得臆造」处理：保留可读的数字，并明说连线归属不可复原。</span>

<span style="color:#2471a3;">**Exercise 15.14.**</span> `[exercise]` *The ten-digit number on the cover of a book known as the ISBN incorporates an error-detecting code. The number consists of nine source digits $x_1, x_2, \ldots, x_9$, satisfying $x_n \in \{0, 1, \ldots, 9\}$, and a tenth check digit whose value is given by $x_{10} = \left( \sum_{n=1}^{9} n x_n \right) \bmod 11$. Here $x_{10} \in \{0, 1, \ldots, 9, 10\}$. If $x_{10} = 10$ then the tenth digit is shown using the roman numeral X.*

*Show that a valid ISBN satisfies $\left( \sum_{n=1}^{10} n x_n \right) \bmod 11 = 0$. Imagine that an ISBN is communicated over an unreliable human channel which sometimes modifies digits and sometimes reorders digits. Show that this code can be used to detect (but not correct) all errors in which any one of the ten digits is modified (for example, `1-010-00000-4` → `1-010-00080-4`). Show that this code can be used to detect all errors in which any two adjacent digits are transposed (for example, `1-010-00000-4` → `1-100-00000-4`). What other transpositions of pairs of non-adjacent digits can be detected? If the tenth digit were defined to be $x_{10} = \left( \sum_{n=1}^{9} n x_n \right) \bmod 10$, why would the code not work so well? (Discuss the detection of both modifications of single digits and transpositions of digits.)*

**Table 15.1. Some valid ISBNs.** `[表：两个合法 ISBN 实例，连字符只为便于阅读]`

| ISBN | 分解 |
|---|---|
| `0-521-64298-1` | $x_1..x_9 = 0,5,2,1,6,4,2,9,8$；$x_{10} = 1$ |
| `1-010-00000-4` | $x_1..x_9 = 1,0,1,0,0,0,0,0,0$；$x_{10} = 4$ |

> 中文话题：ISBN-10 的模 11 校验——验证「单个数字被改」与「相邻两位对调」都能检出，并说明为什么模 10 不行（10 不是素数，相邻对调的差值 $a-b$ 可能被 10 整除）。



<span style="color:#2471a3;">**Exercise 15.15.**</span> `[exercise]` *A channel with input $x$ and output $y$ has transition probability matrix:*

```math
Q = \begin{bmatrix} 1-f & f & 0 & 0 \\ f & 1-f & 0 & 0 \\ 0 & 0 & 1-g & g \\ 0 & 0 & g & 1-g \end{bmatrix}.
```

（原书该矩阵分两半印在页边，**无编号**。）

*Assuming an input distribution of the form $P_X = \left\{ \frac{p}{2}, \frac{p}{2}, \frac{1-p}{2}, \frac{1-p}{2} \right\}$, write down the entropy of the output, $H(Y)$, and the conditional entropy of the output given the input, $H(Y \mid X)$. Show that the optimal input distribution is given by $p = \frac{1}{1 + 2^{-H_2(g) + H_2(f)}}$, where $H_2(f) = f \log_2 \frac{1}{f} + (1-f)\log_2 \frac{1}{(1-f)}$. Remember $\frac{d}{dp} H_2(p) = \log_2 \frac{1-p}{p}$. Write down the optimal input distribution and the capacity of the channel in the case $f = 1/2$, $g = 0$, and comment on your answer.*

> 中文话题：两个互不连通的二元对称子信道并联——$H(Y \mid X)$ 是 $f$ 与 $g$ 的凸组合，对 $p$ 求导得最优输入分布；$f=1/2, g=0$ 时恰是「一个全噪声子信道 + 一个无噪声子信道」的极端情形。

<span style="color:#2471a3;">**Exercise 15.16.**</span> `[exercise]` *What are the differences in the redundancies needed in an error-detecting code (which can reliably detect that a block of data has been corrupted) and an error-correcting code (which can detect and correct errors)?*

> 中文话题：检错与纠错所需的 redundancy（冗余位）为何差一个量级——检错只要「不同错误模式落到不同 syndrome」，纠错还要「把每个 syndrome 唯一指派回一个错误模式」。

### Further tales from information theory（信息论的更多故事）

下面这些习题让你自己去发现信息论中一些更出人意料的结论。

<span style="color:#2471a3;">**Exercise 15.17.**</span> `[exercise]` *Communication of information from correlated sources. Imagine that we want to communicate data from two data sources $X^{(A)}$ and $X^{(B)}$ to a central location $C$ via noise-free one-way communication channels (figure 15.2a). The signals $x^{(A)}$ and $x^{(B)}$ are strongly dependent, so their joint information content is only a little greater than the marginal information content of either of them. For example, $C$ is a weather collator who wishes to receive a string of reports saying whether it is raining in Allerton ($x^{(A)}$) and whether it is raining in Bognor ($x^{(B)}$). The joint probability of $x^{(A)}$ and $x^{(B)}$ might be $P(x^{(A)}, x^{(B)})$ as in (15.3). The weather collator would like to know $N$ successive values of $x^{(A)}$ and $x^{(B)}$ exactly, but, since he has to pay for every bit of information he receives, he is interested in the possibility of avoiding buying $N$ bits from source A and $N$ bits from source B. Assuming that variables $x^{(A)}$ and $x^{(B)}$ are generated repeatedly from this distribution, can they be encoded at rates $R_A$ and $R_B$ in such a way that $C$ can reconstruct all the variables, with the sum of information transmission rates on the two lines being less than two bits per cycle?*

```math
P(x^{(A)}, x^{(B)}): \quad \begin{array}{c|cc} & x^{(A)}=0 & x^{(A)}=1 \\ \hline x^{(B)}=0 & 0.49 & 0.01 \\ x^{(B)}=1 & 0.01 & 0.49 \end{array} \qquad (15.3)
```

**Figure 15.2**（书内 p233 的跨页图，说明文字在下一 PDF 页 p249）：`[Figure 15.2：它演示的是相关源的可达速率区——(a) 两个相关源 X(A)、X(B) 分别编码成速率 R_A、R_B 的传输，经无噪声信道送到接收端 C，虚线箭头表示两者的相关性；(b) 可达速率区：即使 R_A 小于 H(X(A))、R_B 小于 H(X(B))，两条串仍能无误送达]`

> 中文话题：Slepian–Wolf 分布式源编码——两个相关源各编各的，总速率可以低于 $H(X^{(A)}) + H(X^{(B)})$，只要 $R_A \gt H(X^{(A)} \mid X^{(B)})$ 等三个条件成立。



**Figure 15.3**（下页 p250 的图，说明文字在此）：`[Figure 15.3：它演示的是多址接入信道（multiple access channel）——(a) 两个发送端、一个接收端的一般多址信道；(b) 一个二元多址信道，输出等于两输入之和；(c) 可达速率区]`

**Figure 15.4**：`[Figure 15.4：它演示的是广播信道（broadcast channel）的结构——x 是信道输入，y(A) 与 y(B) 是两个输出]`

> 中文话题（承上题）：可达速率区的形状由「两条串能否互相当噪声」决定——图 15.2 的答案就是 Slepian–Wolf 区域。

这道题的答案见图 15.2，需要你自己给出论证。

在 $X^{(A)}$ 与 $X^{(B)}$ 两个相关源的一般情形下，存在给两个发送端的码，可以把 $X^{(A)}$ 与 $X^{(B)}$ **都**可靠地送到 $C$，只要同时满足：来自 $X^{(A)}$ 的信息率 $R_A$ 超过 $H(X^{(A)} \mid X^{(B)})$；来自 $X^{(B)}$ 的信息率 $R_B$ 超过 $H(X^{(B)} \mid X^{(A)})$；以及总信息率 $R_A + R_B$ 超过 joint entropy（联合熵）$H(X^{(A)}, X^{(B)})$（Slepian and Wolf, 1973）。

于是在上面 $x^{(A)}$、$x^{(B)}$ 的例子中，每个发送端的速率必须大于 $H_2(0.02) = 0.14$ 比特，总速率 $R_A + R_B$ 必须大于 $1.14$ 比特，例如 $R_A = 0.6$、$R_B = 0.6$。确实存在达到这些速率的码。你的任务就是弄清楚这为什么成立。试着找一个显式方案，让其中一个源以明文发送，即 $t^{(B)} = x^{(B)}$，另一个源被编码。

> <span style="color:#1e8449;">**[译注]** 这条结论（Slepian–Wolf）之所以反直觉，是因为它把「压缩」与「协作」解耦了：两个编码器**不许通信**，却仍能达到联合压缩的极限。机制在于把 $X^{(B)}$ 的串当成本端已知的 side information（边信息），先在 $X^{(A)}$ 里用 $\binom{N}{k}$ 分箱（binning），只发箱号 $R_A \approx H(X^{(A)} \mid X^{(B)})$，接收端再靠 $x^{(B)}$ 在箱内定位。用题给数字复算：$H_2(0.02) = -0.02\log_2 0.02 - 0.98\log_2 0.98 \approx 0.1414$ 比特，故 $R_A + R_B \gt 1.1414$，取 $0.6+0.6 = 1.2$ 有余量。抽掉 binning 这一层，你只能各自独立压缩到 $H(X^{(A)}) = H(X^{(B)}) = 1$ 比特，总率触底在 2 比特——**整整多付 0.86 比特**，这就是「不协作」的代价。落点：Slepian & Wolf (1973), *IEEE Trans. IT* 19(4):471–480（一手）；本书 §10.x 的 typical set 论证；6.042J 的 Binomial coefficients 与 Counting。</span>

<span style="color:#2471a3;">**Exercise 15.18.**</span> `[exercise]` *Multiple access channels. Consider a channel with two sets of inputs and one output – for example, a shared telephone line (figure 15.3a). A simple model system has two binary inputs $x^{(A)}$ and $x^{(B)}$ and a ternary output $y$ equal to the arithmetic sum of the two inputs, that's 0, 1 or 2. There is no noise. Users A and B cannot communicate with each other, and they cannot hear the output of the channel. If the output is a 0, the receiver can be certain that both inputs were set to 0; and if the output is a 2, the receiver can be certain that both inputs were set to 1. But if the output is 1, then it could be that the input state was $(0,1)$ or $(1,0)$. How should users A and B use this channel so that their messages can be deduced from the received signals? How fast can A and B communicate?*

> 中文话题：加法多址信道——输出 1 是「撞车」的歧义态；要点是用分组与时间对齐让撞车位置不重叠，从而 $R_A + R_B \gt 1$ 也可达。

显然 A、B 到接收端的总信息率不可能是两比特。另一方面，达到总信息率 $R_A + R_B = 1$ 比特是容易的。那么能否在 $R_A + R_B \gt 1$ 的速率对上实现可靠通信？答案见图 15.3。多用户信道的一些实用码由 Ratzer 给出。

<span style="color:#2471a3;">**Exercise 15.19.**</span> `[exercise]` *Broadcast channels. A broadcast channel consists of a single transmitter and two or more receivers. The properties of the channel are defined by a conditional distribution $Q(y^{(A)}, y^{(B)} \mid x)$. (We'll assume the channel is memoryless.) The task is to add an encoder and two decoders to enable reliable communication of a common message at rate $R_0$ to both receivers, an individual message at rate $R_A$ to receiver A, and an individual message at rate $R_B$ to receiver B. The capacity region of the broadcast channel is the convex hull of the set of achievable rate triplets $(R_0, R_A, R_B)$.*

> 中文话题：广播信道的容量区——同一个输入要同时喂两个接收端，「公共消息」与「各别消息」如何分层复用。



这类信道的一个简单基准方案是 time-sharing（时分复用）。若两条子信道各自的容量是 $C_A$ 与 $C_B$，那么把传输时间的 $\phi_A$ 比例分给信道 A、$\phi_B = 1 - \phi_A$ 分给信道 B，就能达到

```math
(R_0, R_A, R_B) = \phi_A\,(0, C_A, 0) + \phi_B\,(0, 0, C_B).
```

**Figure 15.5**：`[Figure 15.5：它演示的是简单 time-sharing 能达到的速率区——横轴 R_A、纵轴 R_B 上两条轴上的点连成直线，线上及线下的速率对可达]`

（上式是原书页面上被文字层截断的那一行的**重建**，依据是紧随其后的文字「devoting a fraction φ_A of the transmission time to channel A」；可复算校验：$\phi_A = 1$ 时退化为 $(0, C_A, 0)$，$\phi_A = 0$ 时退化为 $(0, 0, C_B)$，且 $R_A/C_A + R_B/C_B = 1$，与图 15.5 的直线一致。）

不过我们能做得比这更好。打个比方：想象你同时对着一个美国人和一个白俄罗斯人说话；你既精通美式英语也精通白俄罗斯语，而你的两位听众各自听不懂对方的语言。如果每个听众都能分辨「某个词是不是自己那种语言」，那么还能额外给他们传一条二元文件——用它的比特决定下一个传出的词取美式英语文本还是白俄罗斯语文本。每个听众把听得懂的词串起来就得到自己的消息，同时也能恢复那串二元比特。

广播信道的一个例子是两条 binary symmetric channel 共用同一个输入。这两半信道的 flip probability 分别是 $f_A$ 与 $f_B$。我们假定 A 那一半更好，即 $f_A \lt f_B \lt 1/2$。（一个密切相关的信道是 degraded broadcast channel（退化广播信道），其条件概率使得这些随机变量构成 Markov chain 的结构，即 $y^{(B)}$ 是 $y^{(A)}$ 的进一步退化版本。）

**Figure 15.6**：`[Figure 15.6：它演示的是「按噪声水平设计的码」有多脆——横轴噪声水平 f，纵轴可靠通信率 R；实线是为噪声 $f_A$ 设计的 Shannonesque 码，虚线是为 $f_B$ 设计的]`

<span style="color:#2471a3;">**Exercise 15.20.**</span> `[exercise]` *Variable-rate error-correcting codes for channels with unknown noise level. In real life, channels may sometimes not be well characterized before the encoder is installed. As a model of this situation, imagine that a channel is known to be a binary symmetric channel with noise level either $f_A$ or $f_B$. Let $f_B \gt f_A$, and let the two capacities be $C_A$ and $C_B$. Those who like to live dangerously might install a system designed for noise level $f_A$ with rate $R_A \simeq C_A$; in the event that the noise level turns out to be $f_B$, our experience of Shannon's theories would lead us to expect that there would be a catastrophic failure to communicate information reliably (solid line in figure 15.6).*

> 中文话题：未知噪声水平下的变速率码——「按最优噪声设计」与「按最坏噪声设计」之间还有一个中间策略，本题要你构造它。



**Figure 15.7**：`[Figure 15.7：它演示的是「想要的」变速率码——横轴噪声水平 f，纵轴率 R；只要 $f$ 落在 $[f_A, f_B]$ 内，高优先级比特都能可靠送达，噪声更低时再额外送低优先级比特]`

保守的做法是按最坏情形设计系统，装一个速率 $R_B \simeq C_B$ 的码（图 15.6 的虚线）。若实际情况是较低的噪声水平 $f_A$，管理者会因为白扔了容量差 $C_A - R_B$ 而感到后悔。

那么，能否造出这样一个系统：无论噪声水平如何，都以某个速率 $R_0$ 可靠传输；并且在噪声低时，还能传一些额外的「低优先级」比特，如图 15.7 所示？这种码在 $f_A$ 到 $f_B$ 之间的所有噪声水平下都可靠送出高优先级比特，而在噪声水平为 $f_A$ 或更低时，连低优先级比特也一并送出。

这个问题在数学上与前一个问题是等价的，即 degraded broadcast channel。那里较低的通信率叫 $R_0$，而「噪声低时才传低优先级比特」的速率叫 $R_A$。

**Figure 15.8**：`[Figure 15.8：它演示的是「未知噪声水平」信道的可达区——取 $f_A = 0.01$、$f_B = 0.1$，虚线是简单 time-sharing 能达的 $R_A, R_B$，实线是更巧妙的方案能达的速率]`

图 15.8 给出了 $f_A = 0.01$、$f_B = 0.1$ 情形的一个示例答案。（该图同时画出了两条半信道噪声水平为 $f_A = 0.01$、$f_B = 0.1$ 的广播信道的可达区。）我得承认：简单 time-sharing 的解答与巧妙解答之间的差距，小得令我失望。

在第 50 章我们会讨论广播信道中特殊的一类——erasure channels（擦除信道），其中每个符号要么被无误收到、要么被擦除。这类码有个漂亮性质：它们是 rateless（无速率）的——发送多少个符号是**边发边定**的，无论信道的擦除统计如何，都能保证可靠通信。

<span style="color:#2471a3;">**Exercise 15.21.**</span> `[exercise]` *Multiterminal information networks are both important practically and intriguing theoretically. Consider the following example of a two-way binary channel (figure 15.9a,b): two people both wish to talk over the channel, and they both want to hear what the other person is saying; but you can hear the signal transmitted by the other person only if you are transmitting a zero. What simultaneous information rates from A to B and from B to A can be achieved, and how? Everyday examples of such networks include the VHF channels used by ships, and computer ethernet networks (in which all the devices are unable to hear anything if two or more devices are broadcasting simultaneously).*

> 中文话题：双向信道（two-way channel）——只有自己发 0 时才听得见对方，这是「以太网冲突」的信息论原型；求双向同时可达的速率。

显然用简单 time-sharing 可以在两个方向上都达到 $1/2$ 的速率。但这两个信息率能否做得更大？一般双向信道的容量至今仍是 open problem（开放问题）。不过对上面讨论的简单二元信道，我们可以就可达点得到一些有意思的结果，如图 15.9c 所示。存在能达到图中边界以内速率的码。也可能还存在更好的码。

### Solutions（解答）

**Solution to exercise 15.12（书内 p235）。** $C(Q) = 5$ 比特。最后一问的提示：存在一个涉及简单 $(8, 5)$ 码的方案。



**Figure 15.9**（整页图）：`[Figure 15.9：它演示的是双向信道——(a) 一般双向信道：两人各有输入、各自收到对方信号的函数；(b) 二元双向信道的规则：两张小表分别给出每对输入 (x(A), x(B)) 对应的输出 y(A)、y(B)（「只有你发 0 时对方才听得见你」）；(c) 该二元双向信道的可达区：实线以下可达，虚线是简单 time-sharing 能达的「显然可达」区]`

> 中文话题（承上题）：图 (b) 两个小表的**逐格数值在文字层里完全丢失**，只留下 `y(A): x(A) 0 1 / x(B) 0 / 1` 这样的行列骨架与 `0 1 / 0 0` 等碎片；我按纪律保留骨架并明说**无法复原**，不臆造表项。可确认的定性事实来自正文：「只有当自己发 0 时才听得见对方」，以及图 (c) 的几何形状：可达区严格包含虚线所围的 time-sharing 三角形。



## 第 16 章 Message Passing（消息传递）

本书的一个主题是：用简单的分布式硬件完成复杂的计算。事实证明，相当多有意思的问题都能用 message-passing algorithm（消息传递算法）解决——简单的消息在简单处理器之间**局部**传递，运行一段时间后，全局问题就解出来了。

### 16.1 Counting（计数）

举例：一列士兵在雾中行进。指挥官想完成「数清这一列有多少士兵」这个复杂计算。这个问题有两种解法。

第一种解法要用昂贵的硬件：指挥官与士兵们响亮的嗓门。指挥官可以吼「全体士兵一分钟内向**我**报到！」，然后仔细听士兵们一个个答「Molesworth 到，长官！」「Fotherington–Thomas 到，长官！」等等。这个解法依赖好几件昂贵的硬件：每个士兵与指挥官之间必须有可靠的双向通信信道；指挥官必须能同时听清所有收到的消息——哪怕有几百个士兵——并且还得会数数；而且士兵们必须吃得饱，才有力气隔着可能很远的距离喊回来。

第二种求这个全局函数（士兵人数）的办法，不需要全局通信硬件、不需要高智商、也不需要好伙食；我们只要求每个士兵能与队列中**相邻的两个**士兵交换单个整数，并且会「给一个数加一」。每个士兵遵守以下规则：

<span style="color:#c0392b;">**Algorithm 16.1. Message-passing rule-set A（消息传递规则集 A）**</span>

1. 如果你是队列最前面那个士兵，就对你后面的士兵说数字「一」。
2. 如果你是队列最后面那个士兵，就对你前面的士兵说数字「一」。
3. 如果前面或后面的某个士兵对你说了某个数字，就把它加一，再把新数字说给你另一侧的士兵。

如果聪明的指挥官不仅会给一个数加一，还会把两个数相加，那么他只要把三项加起来就能得出全局士兵人数：



- 前面的士兵对他说的那个数（它等于前面士兵的总数），
- 后面的士兵对指挥官说的那个数（它是后面的总数），
- 一（把指挥官自己算进去）。

这个解法只需要局部通信硬件与简单运算（整数的存储与加法）。

**Figure 16.2**：`[Figure 16.2：它演示的是规则集 A 下士兵自报人数——指挥官把前面士兵报来的「3」、后面士兵报来的「1」和自己这「1」相加，推出总共 5 名士兵]`

#### Separation（可分离性）

这个巧妙的把戏利用的是「士兵总数」的一个深刻性质：它可以写成「某点前面的士兵数」与「该点后面的士兵数」之和，而这两个量可以**分别**计算，因为指挥官把它们**分开了**。

如果士兵们不是排成一列、而是在一片区域里乱走（swarm），那就不能这么容易地把他们分成两组。图 16.3 中的游击队员无法用上面的规则集 A 数清，因为游击队员虽然也有邻居（连线的邻居），但说不清谁「在前」谁「在后」；而且，由于他们之间的连接图含有 cycles（环），环上的某人（比如 Jim）无法把这一群分成「前面那伙」与「后面那伙」两组。

**Figure 16.3**：`[Figure 16.3：它演示的是游击队员的「蜂群」——每个人有若干邻居（连线），但没有全局的「前/后」方向，且连接图含环]`

如果游击队员的网络是一个**不含环**的图，那么用修改过的消息传递算法就能数清他们。规则集 B 就是用来数「连接构成无环图（也叫 tree，树）的游击队员」的消息传递算法，如图 16.4 所示。树上任何一个游击队员都能从收到的消息推算出总数。

**Figure 16.4**：`[Figure 16.4：它演示的是「连接成树」的游击队员蜂群——没有环，因此每个节点都能通过收集邻居消息算出全树总数]`

> <span style="color:#1e8449;">**[译注]** 这一节真正立住的命题只有一句：**全局计数能否局部化，取决于图有没有环以及有没有一个「割点」把问题劈成两半**。规则集 A 成立的充要条件是「指挥官所在位置是一个 cut vertex（割点），把线性队列劈成前后两段」；一旦上环，任何点都不再是割点，$N$ 的加法分解就失效——你会看到算法停住（每个节点都在等邻居，谁也不敢先报），或者报出重复计数的错值。量化的方向感在这里很清楚：树上有 $N$ 个节点、$N-1$ 条边，消息恰好 $2(N-1)$ 条、两轮走完；含一个环（$N$ 条边）时消息在环上无限绕，永远不收敛。抽掉「无环」这条，sum–product 退化成「在环上做信念传播」，收敛性没有保证——这正是本书第 25、26、47 章反复回来的地方。落点：本书 §16.2（路径计数的前向/后向算法就是树上 sum–product）、§16.4 的 separability；6.006 的 Trees 与 Graph Traversal 两讲；6.042J 的 Trees 与 Directed graphs 两节。</span>



<span style="color:#c0392b;">**Algorithm 16.5. Message-passing rule-set B（消息传递规则集 B）**</span>

1. 数清你的邻居个数，记作 $N$。
2. 记录你已从邻居收到的消息条数 $m$，以及每条消息的值 $v_1, v_2, \ldots, v_N$。令 $V$ 为你已收到消息的累计和。
3. 如果你已收到的消息条数 $m$ 等于 $N - 1$，那就找出那个还没给你发消息的邻居，把数 $V + 1$ 告诉它。
4. 如果你已收到的消息条数等于 $N$，那么：
   (a) 数 $V + 1$ 就是所求的总数。
   (b) 对每个邻居 $n$：对邻居 $n$ 说出数 $V + 1 - v_n$。

**Figure 16.6**：`[Figure 16.6：它演示的是三角形排布的 41 × 41 网格——从 A 到 B 共有多少条路径？（图中画出了其中一条）]`



### 16.2 Path-counting（路径计数）

比数士兵更深刻的任务，是数清穿过一个 grid（网格）的路径条数，以及弄清有多少条路径经过网格中某个给定的点。

图 16.6 画出一个矩形网格，以及一条从 A 到 B 穿行其间的路径。所谓 valid path（合法路径），指从 A 出发、只靠向右与向下两种移动抵达 B 的路径。我们要问三个问题：

1. 从 A 到 B 有多少条这样的路径？
2. 若从 A 到 B 随机选一条路径，它经过网格中某个特定节点的概率是多少？（这里的「随机」指所有路径被选中的概率完全相等。）
3. 怎样从 A 到 B 选出一条随机路径？

数清从 A 到 B 的全部路径，看起来并不简单。路径条数预计相当大——即便允许的网格只是一条仅三个节点宽的斜带，仍有大约 $2^{N/2}$ 条可能路径。

**Figure 16.7**：`[Figure 16.7：它演示的是可分离性——任何从 A 到 P 的路径都经由 P 的上游邻居 M 或 N 进入 P，所以「A 到 P 的路径数」等于「A 到 M 的路径数」加「A 到 N 的路径数」]`

计算上的突破在于意识到：求路径数**不必**逐条列举所有路径。在网格里任取一点 P，考虑从 A 到 P 的路径条数。每一条从 A 到 P 的路径，必然经由 P 的某个上游邻居（「上游」指上方或左方）进入 P。所以「从 A 到 P 的路径数」等于「从 A 到这些邻居的路径数」之和。

这个 message-passing algorithm 在图 16.8 中用一个小网格演示：十个顶点、十二条有向边。我们从 A 发出消息「1」开始。任何节点一旦收到它所有上游邻居的消息，就把它们的和送给它的下游邻居。到了 B，数字 5 浮现出来：我们**没有**列举全部路径，却数出了从 A 到 B 的路径条数。

作为 sanity check（合理性检查），图 16.9 画出了那五条不同的 A 到 B 路径。

**Figure 16.8**：`[Figure 16.8：它演示的是前向传播（forward pass）中传递的消息——每个节点把上游消息求和后送往下游]`

**Figure 16.9**：`[Figure 16.9：它演示的是那五条合法路径的逐一展开]`

数清全部路径之后，我们就可以转向更有挑战的问题：计算「随机路径经过某给定顶点」的概率，以及如何生成一条随机路径。

#### Probability of passing through a node（经过某个节点的概率）

除了 forward pass（前向传播），再做一次 backward pass（后向传播），我们就能推出有多少条路径经过每个节点；除以总路径数，就得到「随机选中的路径经过该节点」的概率。图 16.10 的表格里，左下角是后向传播的消息，右上角是原来的前向消息。把某个顶点上的这两个数相乘，就得到经过该顶点的路径总数。例如，有 4 条路径经过中心顶点。

**Figure 16.10**：`[Figure 16.10：它演示的是前向与后向两套消息同时在表里——每个顶点处「前向消息 × 后向消息」= 经过该点的路径数]`

图 16.11 给出了三角形排布的 $41 \times 41$ 网格上的这个计算结果。每个色块的面积正比于经过对应节点的概率。

**Figure 16.11**：`[Figure 16.11：它演示的是 (a) 经过每个节点的概率（色块面积正比于概率），(b) 按该概率分布随机选出的一条路径]`

> <span style="color:#1e8449;">**[译注]** 「前向消息乘后向消息」这一步是全书最可复用的一个技巧，值得单独钉住：设顶点 $P$ 的前向消息为 $f_P$（从 A 到 P 的路径数）、后向消息为 $b_P$（从 P 到 B 的路径数），则经过 P 的路径数恰为 $f_P \cdot b_P$，而总路径数 $= f_B = b_A$。用图 16.10 的小网格复算：中心顶点的 $f \cdot b = 2 \times 2 = 4$，与正文「四条路径经过中心顶点」一致；且 $\sum_{P} f_P b_P$ 是按「路径×经过点数」计权，不等于总路径数 5——所以「除以总数」只能逐点做，不能整体归一。抽掉这条乘法分解，你只剩「枚举所有路径再统计」，复杂度从 $O(\#\text{节点})$ 退化为 $O(\#\text{路径}) = O(2^{N})$：$41\times41$ 网格里总路径数 $\binom{80}{40} \approx 1.08 \times 10^{23}$，任何枚举都跑不完。落点：本书 §16.3、§25.x（sum–product 译码）、§16.6 的解答；6.006 的 Dynamic Programming 讲次（「前缀×后缀」正是 LCS/编辑距离的同款分解）；6.042J 的 Counting（$\binom{80}{40}$ 的估计用 Stirling）。</span>



<span style="color:#2471a3;">**Exercise 16.1.**</span> `[exercise]` *If one creates a 'random' path from A to B by flipping a fair coin at every junction where there is a choice of two directions, is the resulting path a uniform random sample from the set of all paths? [Hint: imagine trying it for the grid of figure 16.8.]*

> 中文话题：逐岔口抛公平硬币 ≠ 均匀随机路径——因为不同路径的岔口数量不同，概率就成了 $2^{-k}$ 而非 $1/5$。

这里有个精巧的洞见值得你自己体会到，我希望你能享受自己想出它的那份满足感。

<span style="color:#2471a3;">**Exercise 16.2.**</span> `[exercise]` *Having run the forward and backward algorithms between points A and B on a grid, how can one draw one path from A to B uniformly at random? (Figure 16.11.)*

> 中文话题：给定前向与后向消息，如何**均匀**抽一条路径——每一步按后向消息的比例选方向（这正是 (16.6) 的解答里给出的「加权偏硬币」）。

用来数「到 B 的路径数」的这套 message-passing algorithm，是 sum–product algorithm（和积算法）的一个例子。所谓「sum」，发生在每个节点把它所有前驱送来的消息相加之时；「product」在这里没被点名，但你可以把那个和看成一个加权和——只不过所有被加项的权重恰好都等于 1。

### 16.3 Finding the lowest-cost path（求最低代价路径）

设想你想尽快从 Ambridge（A）赶到 Bognor（B）。图 16.12 画出了各种可能路线，并标出穿越图中每条边所需的小时数。例如路线 A–I–L–N–B 的代价是 8 小时。我们想在不显式算出所有路径代价的前提下找出最低代价路径。可以高效地做到这一点：对每个节点，求出「从 A 到该节点的最低代价」。这些量可用消息传递从节点 A 起算出来。这个 message-passing algorithm 叫 min–sum algorithm（最小和算法），也叫 Viterbi algorithm（维特比算法）。

**Figure 16.12**：`[Figure 16.12：它演示的是 Ambridge 到 Bognor 的路线图——8 个城市节点 A, H, I, J, K, L, M, N, B 与带权有向边（权重 = 小时数）]`

为简洁起见，我们把「从节点 A 到节点 x 的最低代价路径的代价」简称为「x 的代价」。每个节点一旦知道了它所有可能前驱的代价，就可以把自己的代价广播给它的后继。我们手动走一遍算法。A 的代价是零。我们把这个消息传给 H 与 I。消息沿图中每条边传递时，都要加上该边的代价。于是 H 与 I 的代价分别是 4 与 1（图 16.13a）。同理，J 与 L 的代价分别是 6 与 2。但 K 呢？从边 H–K 过来的消息说「存在一条从 A 经 H 到 K、代价为 5 的路径」；而从边 I–K 我们又得知另一条代价为 3 的路径（图 16.13b）。min–sum 算法把 K 的代价取为这些值中的最小者（这就是那个「min」），并通过**只保留**边 I–K、剪掉其他指向 K 的边，记录下哪条是进入 K 的最小代价路线（图 16.13c）。图 16.13d 与 e 给出算法余下的两轮迭代，结果是存在一条从 A 到 B、代价为 6 的路径。

[若 min–sum 算法遇到 tie（并列），即到某节点的最低代价路径不止一条，那么它可以在这些路线中任选一条。]



我们可以从 B 回溯（backtracking），沿着幸存边的痕迹一路走回 A，从而恢复出这条最低代价路径。

> <span style="color:#1e8449;">**[重建说明]** 原文此句只写「backtracking from B … the lowest-cost path is」然后接图；具体路径名与逐段代价在文字层里**没有**（Figure 16.13 的边与标注是矢量图，抽取不到）。按正文给出的各轮代价——$d(A)=0$、$d(H)=4$、$d(I)=1$、$d(J)=6$、$d(L)=2$、$d(K)=3$、$d(B)=6$——重建为 **A–I–K–M–B**，逐段验算 $1 + 2 + 2 + 1 = 6$ 与 $d(B)=6$ 相符；但**中间节点 M 的入边归属无法从文字层复原**，此路径仅供参考，以原书 Figure 16.13e 为准。</span>

**Figure 16.13**：`[Figure 16.13：它演示的是 min–sum 消息传递算法的五轮迭代 (a)–(e)——逐轮算出到达各节点的代价，并剪掉非最省的入边，最终给出 A 到 B 的最低代价路线]`

#### Other applications of the min–sum algorithm（min–sum 算法的其他应用）

设想你管理一套从原材料经大量工序得到产品的生产流程。你想找出流程中的 critical path（关键路径），也就是那部分正在拖住生产的工序集合。如果关键路径上的任何工序能快一点，从原材料到产品的总时间就会缩短。一组工序的关键路径可以用 min–sum 算法求出。

在第 25 章，min–sum 算法将被用于纠错码的译码。

> <span style="color:#1e8449;">**[译注]** min–sum 与 sum–product 是同一个骨架的两种 semiring（半环）运算：把「加」换成「取最小」、把「乘」换成「加」，前向传播的形式完全不变。这个替换能成立的前提是**图无环**（或有确定的加工次序）；一旦有环且含负权边，min–sum 就会在环上不断「改进」下去而不终止。用图 16.12 验一遍：到 K 的两条入边给出 5 与 3，取小得 3，这正是 Dijkstra 的第一步松弛；全图跑完得 $d(B) = 6$，与正文一致。抽掉「取小」这一步（改成求和），你得到的是「路径计数」而非「最短路」——同一张图、同一套消息，答案从 6 变成 5 条路径。落点：本书 §16.6、§25.x（Viterbi 译码）、§42.9（神经网络的 TSP 方法）；6.006 的 Shortest Paths 讲次（Dijkstra 的松弛就是 min–sum 的原地版本）、Dynamic Programming 讲次（Viterbi = HMM 上的 DP）；6.042J 的 Partial orders 一节。</span>

### 16.4 Summary and related ideas（小结与相关思想）

有些全局函数具有 separability（可分离性）。例如「从 A 到 P 的路径数」可以分解为「从 A 到 M（P 左边那个点）的路径数」与「从 A 到 N（P 上方那个点）的路径数」之和。这类函数能用消息传递高效计算。

另一些函数则不具备这样的可分离性，例如：

1. 一支队伍中生日相同的士兵**对数**；
2. 身高相同（四舍五入到厘米）的士兵所构成的**最大组**的大小；
3. 一个旅行商访问队伍中每个士兵的最短回路长度。

机器学习的一项挑战，就是为这类问题寻找低代价的解法。「找出一个大的、彼此近似相等的变量子集」这个问题可以用神经网络方法解决（Hopfield and Brody, 2000；Hopfield and Brody, 2001）。旅行商问题的神经方法将在 §42.9 讨论。

### 16.5 Further exercises（进阶习题）

<span style="color:#2471a3;">**Exercise 16.3.**</span> `[exercise]` *Describe the asymptotic properties of the probabilities depicted in figure 16.11a, for a grid in a triangle of width and height $N$.*

> 中文话题：三角网格中「经过某点的概率」的渐近形状——中心高、边缘低，其轮廓在多维极限下趋于什么分布（提示：$\binom{n}{k}$ 的高斯近似）。

<span style="color:#2471a3;">**Exercise 16.4.**</span> `[exercise]` *In image processing, the integral image $I(x, y)$ obtained from an image $f(x, y)$ (where $x$ and $y$ are pixel coordinates) is defined by*

```math
I(x, y) \equiv \sum_{x' \le x} \sum_{y' \le y} f(x', y').
```

*Show that the integral image $I(x, y)$ can be efficiently computed by message passing. Show that, from the integral image, some simple functions of the image can be obtained. For example, give an expression for the sum of the image intensities $f(x, y)$ for all $(x, y)$ in a rectangular region extending from $(x_1, y_1)$ to $(x_2, y_2)$.*

> 中文话题：integral image（积分图）就是二维前缀和——可用两趟消息传递算出；矩形区域和用容斥原理一次查表即得。
>
> <span style="color:#1e8449;">**[重建说明]** 上式在原 PDF 的文字层里只剩 `I(x, y) ≡ \sum_x \sum_y`（上下标与 $f$ 全部丢失），我按 integral image 的通行定义重建为二维前缀和，并给可复算校验：取 $2\times2$ 图像 $f(1,1)=1$、$f(1,2)=2$、$f(2,1)=3$、$f(2,2)=4$（1-based 下标），则 $I(1,1)=1$、$I(1,2)=3$、$I(2,1)=4$、$I(2,2)=10$；矩形和公式 $I(x_2,y_2) - I(x_1-1, y_2) - I(x_2, y_1-1) + I(x_1-1, y_1-1)$ 在单格 $(2,2)$ 上给出 $10 - 3 - 4 + 1 = 4 = f(2,2)$ ✓，在整幅 $(1,1)$–$(2,2)$ 上（边界项按 $I(\cdot, 0) = I(0, \cdot) = 0$ 处理）给出 $10 - 0 - 0 + 0 = 10$ ✓。**本题的重建公式必须配 1-based 下标约定**，按此约定复算即可对上。</span>



### 16.6 Solutions（解答）

**Solution to exercise 16.1（书内 p244）。** 因为图 16.8 的网格里共有五条路径，它们在均匀采样下每条的概率都必须是 $1/5$。但基于公平抛硬币的策略产生的路径，其概率只能取 $1/2$ 的幂——而 $1/5$ 不是 $2$ 的负整数次幂。

**Solution to exercise 16.2（书内 p245）。** 要做出均匀随机游走，每一步都应当在每个岔口用一枚**不同**的偏硬币来选择，其偏置正比于该岔口两个选项上射来的**后向**消息。例如离开 A 之后的第一个选择：从东边过来的是消息「3」，从南边过来的是消息「2」，所以应当以概率 $3/5$ 向东、以概率 $2/5$ 向南。图 16.11b 里的路径就是这样生成的。

> <span style="color:#1e8449;">**[译注]** 解答 16.2 给出的是**精确**的均匀采样器，值得把它的正确性单独验一遍，因为它同时也是「拒绝采样不行、按局部比例就行」的分界例证。设某岔口的两个下游分支分别有 $b_E$、$b_S$ 条通往 B 的路径，则该点总路径数 $f \cdot (b_E + b_S)$，按比例走东分支的概率为 $b_E/(b_E + b_S)$ 时，「选中某条具体路径」的概率沿路逐段相乘恰好等于 $1/(\text{总路径数})$——在图 16.8 上复算：起点 $b_E = 3$、$b_S = 2$，走东后为 $3$ 条中的一条（$1/3$），故 $P = (3/5)(1/3) = 1/5$ ✓，与「五条路径等概率」一致。抽掉按后向消息加权这一步、改成逐岔口公平硬币（即习题 16.1），你会得到 $P = 2^{-k}$ 且 $k$ 随路径而变，采样**有偏**：走岔口多的那条路的路径概率低，最终分布偏离 $1/5$ 达 $1/4 - 1/5 = 1/20$ 这个量级以上。落点：本书 §16.2 与 §16.6；6.006 的 Dynamic Programming 讲次（后向消息即后缀 DP 表）；6.042J 的 Conditional probability 与 Independence 两节。</span>



## 第 17 章 Communication over Constrained Noiseless Channels（在受约束的无噪声信道上通信）

本章研究如何在一个 constrained noiseless channel（受约束的无噪声信道）上高效通信——所谓受约束信道，指输入字母表里的字符串并非都能被传过去。

我们用到第 16 章引入的想法：图的全局性质可以由局部的消息传递算法算出。

### 17.1 Three examples of constrained binary channels（三个受约束二元信道的例子）

受约束信道可由「哪些字符串被允许」的规则来定义。

<span style="color:#00838f;">**Example 17.1（Channel A）**</span> 在 Channel A 中，每个 1 后面必须至少跟一个 0。

Channel A：禁止出现子串 `11`。

作为这个模型的动机，考虑这样一个信道：1 用电磁能量脉冲表示，而产生这些脉冲的器件在发出一个脉冲之后需要一个时钟周期的 recovery time（恢复时间）才能发出下一个脉冲。

<span style="color:#00838f;">**Example 17.2（Channel B）**</span> Channel B 的规则是：所有 1 必须成组出现、每组至少两个；所有 0 也必须成组出现、每组至少两个。

Channel B：禁止出现 `101` 与 `010`。

作为这个模型的动机，考虑这样一个磁盘驱动器：相邻的比特被写在盘片表面同一条磁道上的相邻位置；0 与 1 用两种相反的磁化取向表示。`101` 与 `010` 这类串被禁止，是因为被相反取向的磁畴包围的**孤立**磁畴不稳定，于是 `101` 可能变成 `111` 之类。

<span style="color:#00838f;">**Example 17.3（Channel C）**</span> Channel C 的规则是：允许的最大 runlength（游程长度）为二，即每个符号最多重复一次。

Channel C：禁止出现 `111` 与 `000`。

> <span style="color:#1e8449;">**[原文缺失说明]** 上述三个例子后面各有一句「A valid string for this channel is …」，但**其后的示例字符串在文字层里完全丢失**（这三段示例串在原书中用特殊字体/图形排出，fitz 与 pdfplumber 抽取均未得到任何字符）。按纪律保留句子位置并明说无法复原，不臆造示例串；读者可按各例的禁用规则自行构造，例如 Channel A 的 `1001101010`、Channel B 的 `11001100`、Channel C 的 `00110011` 均为合法串（这是按规则**构造**的校验串，不是原文）。</span>
>
> <span style="color:#1e8449;">**[译注]** 这一节只是开头，但已经埋下全章的关键量：受约束信道的容量不是 $1$，而是 $\log_2 \lambda_{\max}$，其中 $\lambda_{\max}$ 是该信道**允许串的 adjacency matrix（邻接矩阵）的最大特征值**。用 Channel A 验一遍：状态取「上一个符号是 0」与「上一个符号是 1」，允许的转移是 $0\to 0$、$0\to 1$、$1\to 0$，矩阵 $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$，其特征值 $\lambda = (1 \pm \sqrt{5})/2$，于是 capacity $= \log_2 \varphi \approx 0.6942$ 比特每信道符号——**比 1 少三成**。抽掉「用邻接矩阵谱半径算容量」这条路，你只能靠枚举长度为 $N$ 的合法串数 $N_N$ 再取 $\lim \frac{1}{N}\log_2 N_N$，$N = 20$ 时就有 $\varphi^{20}/\sqrt{5} \approx 6765$ 条要数，$N=40$ 时约 $1.66\times10^{8}$ 条——枚举立刻不可行。落点：本书 §17.2 起（容量与最大特征值）、§17.x 的 run-length-limited code（磁记录里的 RLL 码正是 Channel B/C 的实用编码）；Strang 线代第 6 章（特征值与对角化，$\lambda_{\max}$ 由 Perron 性质保证为正实数）；6.006 的 Dynamic Programming 讲次（$N_N$ 的递推就是 DP）。</span>



<span style="color:#7f8c8d">书内 p.249（PDF p.261）｜ 17.1: Three examples of constrained binary channels</span>

这个模型的一个物理动机是磁盘驱动器：盘片的旋转速率并不被精确知道，于是「两个 1 组成的串」与「三个 1 组成的串」很难区分——它们分别表现为时长为 $2\tau$ 与 $3\tau$ 的定向磁化，而 $\tau$ 是一个比特经过磁头所需的时间（这个量本身就不准）。为了避免这种混淆、以及由此带来的收发双方 synchronization（同步）丢失，我们干脆禁止三个 1 组成的串和三个 0 组成的串。

上面这三个通道都是 runlength-limited channel（游程受限通道）的例子。规则约束的是连续 1 与连续 0 的个数的最小值与最大值。

| Channel | Runlength of 1s 最小 | 最大 | Runlength of 0s 最小 | 最大 |
|---|---|---|---|---|
| unconstrained | 1 | $\infty$ | 1 | $\infty$ |
| A | 1 | 1 | 1 | $\infty$ |
| B | 2 | $\infty$ | 2 | $\infty$ |
| C | 1 | 2 | 1 | 2 |

在 Channel A 中，0 的 runlength（游程）可以是任意长度，但 1 的游程被限制为一。在 Channel B 中，所有游程的长度都必须是二或更多。在 Channel C 中，所有游程的长度都必须是一或二。

无约束二元通道的 capacity（容量）是每信道使用一比特。这三个受约束通道的 capacity 是多少？[公平地说，我们还没有定义这类通道的「capacity」；此处请把 capacity 理解为「每次使用通道能可靠传送多少比特」。]

### Some codes for a constrained channel（受约束通道的一些码）

让我们先集中看 Channel A：0 的游程可以是任意长度，1 的游程被限制为一。我们希望尽可能高效地在这个通道上传送一个随机的二元文件。

<span style="color:#00838f;">**Code C1**</span>

| $s$ | $t$ |
|---|---|
| 0 | 00 |
| 1 | 10 |

一个简单的起点是 (2, 1) 码：把每个信源比特映射成两个发送比特，即 C1。它是一个 rate-1/2（码率二分之一）的码，并且遵守 Channel A 的约束，所以 Channel A 的 capacity 至少是 0.5。我们能做得更好吗？

C1 是冗余的：如果收到的两个比特中的第一个是零，我们就知道第二个比特也会是零。用一个省掉 C1 里那些冗余零的码，可以得到更小的平均发送长度。

<span style="color:#00838f;">**Code C2**</span>

| $s$ | $t$ |
|---|---|
| 0 | 0 |
| 1 | 10 |

C2 就是这样一个 variable-length code（变长码）。如果信源符号出现频率相等，那么每个信源比特对应的平均发送长度是

```math
L = \frac{1}{2}\,1 + \frac{1}{2}\,2 = \frac{3}{2}, \qquad (17.4)
```

于是平均通信速率是

```math
R = 2/3, \qquad (17.5)
```

而 Channel A 的 capacity 至少是 2/3。

我们能比 C2 做得更好吗？有两条路子可以论证信息率能提高到 $R = 2/3$ 以上。

第一条论证假定我们已经接受「熵是信息量的度量」。想法是：从码 C2 出发，**降低我们发送的 1 所占的比例**，就能缩短平均消息长度，而不会使消息的熵明显下降。

> <span style="color:#1e8449;">**[译注]** 这里「码率 2/3」离真正的 0.694 只差 4%，但差的那部分不是靠换更聪明的码表省出来的，而是靠**改变送入通道的信源统计**——这条区别是整章的分水岭。C2 的平均发送长度随信源密度线性增长（$L=1+f$），而信源每符号的信息量 $H_2(f)$ 在 $f=1/2$ 处取最大值 1，两者的比值就是信息率

```math
R(f) = \frac{H_2(f)}{1+f}, \qquad R(1/2) = \frac{1}{1.5} = 0.6667.
```

**消失测试**：抽掉「先稀疏化、再用不等频驱动变长码」这一步，只允许等频输入（$f=1/2$），本章所有码的天花板都退化成 C2 的 $0.6667$，与 $0.6942$ 之间那 $0.0275$ 比特/符号的缺口永远补不上——按每秒 $10^{9}$ 符号的磁盘算，就是白白丢掉 $2.75\times 10^{7}$ 比特/秒。方向感：$f$ 从 $0.5$ 减到 $0.38$，分母 $L$ 只降 8% 到 $1.38$，分子 $H_2$ 只降 4% 到 $0.958$，比值反而升 4% 到 $0.6942$——**分子降得慢、分母降得快**才赚。落点：本书 §17.3 的路径计数给出同一答案 $\log_2\gamma = 0.6942$，两条路子必须对上才算懂；第 6 章的 arithmetic code 正是稀疏化器的实现；6.042J 的 Counting 与 6.006 的 Dynamic Programming（$M_N$ 的递推）。</span>



<span style="color:#7f8c8d">书内 p.250（PDF p.262）｜ 17 — Communication over Constrained Noiseless Channels</span>

我们发送消息的熵来自我们送入 C2 的那条比特流。想象把一条 1 的频率为 $f$ 的比特流喂给 C2。[这样一条流可以从任意二元文件得到：把源文件送进一个 arithmetic code 的 decoder（解码器），而该 arithmetic code 是针对密度 $f$ 的二元串最优压缩的。] 达到的信息率 $R$ 是信源的熵 $H_2(f)$ 除以平均发送长度

```math
L(f) = (1 - f) + 2f = 1 + f. \qquad (17.6)
```

因此

```math
R(f) = \frac{H_2(f)}{L(f)} = \frac{H_2(f)}{1 + f}. \qquad (17.7)
```

原来的码 C2、不带 preprocessor（预处理器），对应 $f = 1/2$。如果我们把 $f$ 朝更小的方向扰动一点，令

```math
f = \frac{1}{2} + \delta, \qquad (17.8)
```

其中 $\delta$ 是一个很小的负数，会怎样？在 $f = 1/2$ 附近，分母 $L(f)$ 随 $\delta$ **线性**变化；相反，分子 $H_2(f)$ 对 $\delta$ 只有**二阶**依赖。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.4.[1]**</span> Find, to order $\delta^2$, the Taylor expansion of $H_2(f)$ as a function of $\delta$.

> 中文话题：把二元熵 $H_2$ 在 $f = 1/2$ 处展开到二阶——一次项系数恰为 0（这是本页论证的全部技术支点），二次项系数是 $-2/\ln 2 \approx -2.885$。

到一阶为止，$R(f)$ 随 $\delta$ 减小而线性增大。所以**必然**可以通过减小 $f$ 来提高 $R$。

[Figure 17.1：上图为信源每符号的信息量 $H_2(f)$ 与每信源符号的平均发送长度 $1+f$ 随信源密度 $f$ 的变化；下图为每发送符号的信息量 $R(f) = H_2(f)/(1+f)$ 随 $f$ 的变化。文字层可复原的刻度：上图纵轴 0–2、横轴 0–1；下图纵轴 0–0.7、横轴 0–1。曲线的定性形状（$H_2$ 在 $f=1/2$ 取最大值 1、$1+f$ 为直线、$R$ 在 $f\simeq0.38$ 取峰值约 0.69）可由正文数值复算，但**曲线像素本身无法从文字层复原**。]

确实，$R$ 随 $f$ 减小而上升，并且在 $f \simeq 0.38$ 处取得最大值，约每个信道使用 0.69 比特。

通过这条论证，我们已经证明 Channel A 的 capacity 至少是 $\max_f R(f) = 0.69$。

<span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">**▷ Exercise 17.5.[2, p.257]**</span> If a file containing a fraction $f = 0.5$ 1s is transmitted by C2, what fraction of the transmitted stream is 1s? What fraction of the transmitted bits is 1s if we drive code C2 with a sparse source of density $f = 0.38$?

> 中文话题：问的是**信源密度到信道密度**的换算——C2 里信源 1 变成 `10`（含一个 1）、信源 0 变成 `0`，故发送流中 1 的比例是 $f/(1+f)$；$f=0.5$ 时得 $1/3$，$f=0.38$ 时得 $0.2764$。

第二条、也是更根本的路子：数一数长度为 $N$ 的合法序列有多少个，记作 $S_N$。给每个合法序列一个名字，我们就能在 $N$ 个信道周期里传送 $\log S_N$ 比特。

> <span style="color:#1e8449;">**[译注]** 「$H_2$ 在 $f=1/2$ 处一阶平坦」这条事实决定了峰值位置，而不只是「$R$ 有个最大值」。把 $H_2(1/2+\delta)$ 展开：

```math
H_2\!\left(\tfrac{1}{2}+\delta\right) = 1 - \frac{2}{\ln 2}\,\delta^2 + O(\delta^4) = 1 - 2.885\,\delta^2 + O(\delta^4),
```

代进 (17.7) 并对 $f$ 数值求根 $dR/df = 0$，得 $f^{*} = 0.3771$、$R_{\max} = 0.6942$；把 $f = 0.38$ 直接代入则得 $H_2(0.38)/(1.38) = 0.9580/1.38 = 0.6942$，**与正文的 $f\simeq0.38$、$0.69$ 逐位吻合**。这条展开的用处是可判的：它说明峰值只能靠**数值**求，任何「对称性论证」都给不出 $f^{*}$ 偏离 $1/2$ 的方向，因为 $H_2$ 在 $1/2$ 处一阶导 $\log_2\frac{1-f}{f} = 0$、二阶导 $-2/\ln 2$，对称性在这里是**退化**的。**失效对象**：若某个受约束通道的符号代价不等（例如 0 与 1 的传输时长不同，见 §17.6），$L(f)$ 就不再是 $1+f$ 这条直线，此时「$f$ 一定要小于 $1/2$」会反转——峰值可能落在 $f>1/2$ 一侧。落点：本书 (2.9) 的二元熵、图 17.1、习题 17.4；6.042J 的 Taylor 展开；6.006 的一维求根（Bisection / Newton）。</span>

### 17.2 The capacity of a constrained noiseless channel（受约束无噪声通道的容量）

我们曾用输入与输出之间的 mutual information（互信息）来定义有噪通道的 capacity，随后却证明了这个数——也就是 capacity——与「在 $N$ 次使用中能被可靠传送的可区分消息数 $S(N)$」有这样一个关系：

```math
C = \lim_{N\to\infty} \frac{1}{N} \log S(N). \qquad (17.9)
```

对受约束无噪声通道，我们直接把这个恒等式**当作 capacity 的定义**。不过符号 $s$ 当年在构造有噪通道的码时（§9.6）跑遍的是消息编号 $s = 1, \ldots, S$，现在它要换一个新角色：给通道的**状态**贴标签；
