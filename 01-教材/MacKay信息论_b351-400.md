<!-- 书页 351–400｜来源：B 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->



## 28.2 例子 · Example

让我们回到本章开头那个例子。图 28.1 里，树后面究竟有一个箱子还是两个箱子？**为什么巧合（coincidence）会让我们起疑？**

设树干与箱子附近那块区域的图像大小为 50 pixels（像素），树干宽 10 pixels，而箱子能分辨出 16 种不同颜色。

理论 $H_1$ 说树旁只有一个箱子，它有四个自由参数：定义箱子上面三条边的三个坐标，加上一个给出箱子颜色的参数。（如果箱子能悬浮，就会有五个自由参数。）

理论 $H_2$ 说树旁有两个箱子，它有八个自由参数（四的两倍），外加第九个——一个二值变量，指明两个箱子中哪一个离观察者更近。

[Figure 28.7：树干后面到底有一个箱子还是两个箱子？图上是卡通图（树与箱子的简笔画），矢量线条本身不承载数值信息，无法从文字层复原；它在这里的作用只是把「$H_1$ 还是 $H_2$」这个问题具体化。]

那么每个模型的 evidence 是多少？先做 $H_1$。

我们需要参数上的 prior 才能算 evidence。为方便起见，一切以 pixels 为单位。

给箱子的水平位置、宽度、高度、颜色各分配一个可分离的 prior。高度可以取比如说 20 个可分辨值，宽度、位置也是 20 个；颜色可以取 16 个值。这些变量上一律放均匀 prior。

图像里其他物体关联的那些参数我们全部忽略，因为它们不进入 $H_1$ 与 $H_2$ 的比较。于是 evidence 是

```math
P(D \mid H_1) = \frac{1}{20}\cdot\frac{1}{20}\cdot\frac{1}{20}\cdot\frac{1}{16} \qquad (28.11)
```

因为只有一组参数设置能拟合该数据，而它完美地预测了数据。

至于模型 $H_2$，它的九个参数里有六个被数据定得很死，另三个被数据部分约束。举例来说，若左边那个箱子离得最远，它的宽度至少 8 pixels、至多 30；若它是两个箱子里更近的那个，宽度就在 8 到 18 pixels 之间。（这里我假设左边箱子的可见部分大约 8 pixels 宽。）

求 evidence 需要把一切可行假设的 prior probability 加起来。要做精确计算，得把数据与 prior 说得更具体；不过我们先把 ballpark（量级答案）拿到，假设两个不受约束的实变量各有一半取值可用，而那个二值变量完全未定。（作为练习，你可以做一个显式模型把精确答案算出来。）

```math
P(D \mid H_2) \simeq \frac{1}{20}\cdot\frac{1}{20}\cdot\frac{10}{20}\cdot\frac{1}{16}\times\frac{1}{20}\cdot\frac{1}{20}\cdot\frac{10}{20}\cdot\frac{1}{16}\times\frac{2}{2} \qquad (28.12)
```

† 按式 (28.12) 的记账口径，$H_2$ 每个箱子有 2 个参数付满额罚分 $1/20$、1 个参数付半额 $10/20$、1 个颜色参数付 $1/16$，加末尾那个完全未定的二值变量因子 $2/2 = 1$；这与正文「六个参数被定死、三个被部分约束」的措辞不能逐项对上（正文按 9 个参数数，算式按 8 个参数 + 1 个二值变量记）。两处记账方式不同，但都落在同一个量级上。

于是后验概率比（假定两模型 prior probability 相等）为

```math
\frac{P(D \mid H_1)P(H_1)}{P(D \mid H_2)P(H_2)} = \frac{1}{\frac{1}{20}\cdot\frac{10}{20}\cdot\frac{10}{20}\cdot\frac{1}{16}} = 20 \times 2 \times 2 \times 16 \simeq 1000/1 \qquad (28.13\text{–}28.14)
```

† 末端的 $20 \times 2 \times 2 \times 16$ 精确等于 $1280$；作者写 $\simeq 1000/1$，是把它当成「大约三个数量级」的量级陈述。用 $1280:1$ 复算更准。

所以数据以大约 1000 比 1 支持更简单的那个假设。

式 (28.13) 里那四个因子可以用 Occam factor 来解释。更复杂的模型为尺寸和颜色多出四个参数——三个给尺寸，一个给颜色。它必须为「两个箱子的高度完全相等、两个箱子的颜色完全一致」这两个**高度可疑的巧合**，各付一个很大的 Occam factor（$1/20$ 与 $1/16$）；此外它还要为另外两个较小的巧合——两个箱子恰好各有一条边被树或彼此遮住——付两个较小的 Occam factor。

<span style="color:#1e8449;">**[译注]**
这一节最容易被误读成「参数越多罚得越多」，而 MacKay 在这里给出的真实主张更窄也更硬：**Occam factor 惩罚的是参数之间的巧合，不是参数的个数。**

看式 (28.13) 的四个因子：$1/20$（两个高度相等）、$1/16$（两个颜色相同）、$10/20$（左箱宽度被遮挡后仍有半数取值可用）、$10/20$（同理）。
两个箱子的**位置**参数完全没有出现在这个乘积里——因为位置没有巧合，$H_2$ 不需要为它付任何额外的钱。
所以「$H_2$ 有 9 个参数」这件事本身几乎不影响结论，$9-4=5$ 这个数字在式子里根本不出现。

**消失测试**：把 Occam factor 理解成「按参数个数计费」，就会预测两个**尺寸相同、只是箱子数不同**的场景罚分差一个固定常数；
而按本页的记账，罚分取决于「哪些参数被数据钉死到偶然相等的程度」。
一旦把这个机制换成「$k$ 计费」，就无法解释为什么 $1/20$ 与 $1/16$ 的量级差（$20$ 对 $16$）会直接进入比值，
也预测不出「把颜色从 16 种改成 2 种，证据比从 $1280:1$ 变成 $160:1$」——这个可被反驳的预言正是本页记账方式的价值所在。

**落点**：式 (28.11)–(28.14) 在本页；同一记账方式在 §28.1 的 (28.9) 给出标量版、在 (28.10) 给出 $k$ 维版；
「巧合付费」这一读法与 p352 的 MDL 参数块/数据块分解（图 28.8）是同一件事的两种讲法。
</span>



[Figure 28.8：minimum description length 视角下的 model comparison。每个模型 $H_i$ 用三段消息把数据 $D$ 传给接收方——先发「我是哪个模型」$L(H_i)$，再发「我的 best-fit 参数」$L(w^*_{(i)} \mid H_i)$，最后发「相对于这些参数的数据残差」$L(D \mid w^*_{(i)}, H_i)$。随模型变复杂，参数消息变长，而数据消息变短（复杂模型拟合得更好、残差更小）；中间的模型 $H_2$ 取得两条趋势之间的最优权衡。三行消息块都是同心矩形，长度可读出相对长短但无绝对数值刻度。]

## 28.3 最小描述长度 · Minimum description length (MDL)

把事件的概率换成「把该事件无损地传给接收方所需消息的比特长度」，就得到 Bayesian model comparison 的一个互补视角。消息长度 $L(x)$ 与事件 $x$ 上的概率模型通过下面两式对应：

```math
P(x) = 2^{-L(x)}, \qquad L(x) = -\log_2 P(x) \qquad (28.15)
```

MDL 原则（Wallace and Boulton, 1968）断言：应当偏爱那些能用最少比特把数据传出去的模型。

考虑一条两段式消息：先说清用的是哪个模型 $H$，再在该模型内把数据 $D$ 传到某个事先约定的精度 $\delta_D$。这样得到的长为 $L(D, H) = L(H) + L(D \mid H)$。

不同 $H$ 的 $L(H)$ 定义了各个备选模型上的一个隐式 prior $P(H)$；类似地，$L(D \mid H)$ 对应一个密度 $P(D \mid H)$。于是，任何一套「消息长度分配」的做法都可以映射到后验概率上：

```math
L(D, H) = -\log P(H) - \log\big(P(D \mid H)\,\delta_D\big) \qquad (28.16)
```

```math
\phantom{L(D, H)} = -\log P(H \mid D) + \text{const.} \qquad (28.17)
```

原则上，MDL 总能被解释成 Bayesian model comparison，反之亦然。

不过，这套简单讨论并没有处理一个关键问题：那个依赖数据的项 $L(D \mid H)$——也就是 $H$ 的 evidence——实际上要怎么算。

通常人们把这条消息想象成再细分成一个参数块和一个数据块（图 28.8）。

参数少的模型，参数块很短，但拟合不好，于是数据消息（一长串大残差）很长。

参数一多，参数块变长，数据消息变短。存在一个最优的模型复杂度（图中是 $H_2$），使两者之和最小。

这幅图景掩盖了几个微妙问题。我们一直没有说明参数 $w$ 应当被送到什么精度。**这个精度是有实质影响的**（这一点不同于实数数据 $D$ 的发送精度 $\delta_D$——只要 $\delta_D$ 相对噪声水平很小，后者就只是引入一个加性常数）。

当我们降低 $w$ 的发送精度时，参数消息会变短，但数据消息通常变长，因为被截断的参数和数据对不上了。**存在一个非平凡的最优精度。**

在简单的 Gaussian 情形里，这个最优精度可以解出来（Wallace and Freeman, 1987），它与参数上的 posterior error bars $A^{-1}$ 密切相关，其中 $A = -\nabla\nabla \ln P(w \mid D, H)$。结果是：最优的参数消息长度，几乎就等于式 (28.10) 里 Occam factor 的对数。（参数截断里那个随机成分，使这个编码略微次优。）

所以，只要足够小心，用 MDL 的语言可以复现 Bayesian 的结果。

尽管关于复杂模型比较的一些最早工作就落在 MDL 框架里（Patrick and Wallace, 1982），**MDL 相对于直接的 probabilistic 方法并没有什么看得见的好处。**

<span style="color:#1e8449;">**[译注]**
式 (28.15) 与其说是「另一个理论」，不如说是一本**双向字典**：$L(x) = -\log_2 P(x)$ 把「消息长度」翻译成「概率」，于是「哪种编码更短」与「哪个模型 evidence 更大」变成同一句陈述。

能把字典写死的，是 prefix code 的长度必须满足 Kraft 不等式 $\sum_x 2^{-L(x)} \le 1$——这条不等式保证「任何一套可解码的码长都对应一个概率分布」，反过来，任何概率分布也都能做出一套码长与之匹配的编码（算术编码、Huffman 码）。
所以 (28.16)(28.17) 里那句「$L$ 与 $P$ 互为对应」不是比喻，是**双向完备**的：给定码长就能反推 posterior，给定 posterior 就能反推码长，误差只在对 $\delta_D$ 这类常数上。

**消失测试**：抽掉 Kraft 这一层，MDL 就退化成一套「编个码、比长度」的启发式，无法回答「凭什么短的码就代表更可信的假设」，
也无法解释为什么 (28.17) 的右端能写成 $-\log P(H \mid D)$ 加一个常数——只能停在「经验上管用」。
一旦退化到这个程度，第 28.1 节那套 Occam factor 的定量记账就完全接不上，两种语言各说各话。

**落点**：式 (28.15)–(28.17) 在本页；Kraft 不等式的证明见第 5 章（p85 前后的 prefix code 一节，式 (5.10) 附近）；
与 Occam factor 的对接见本页下半段「最优参数消息长度 ≈ $\ln$(Occam factor)」。挂 6.042J 的计数与指数即可，不越级。
</span>



MDL 倒确实有它作为教学工具的用处。

description length 这个概念，对**给 prior probability 分布找动机**很有帮助。此外，用模型传达数据这件事的不同拆法，能给建模过程带来有用的洞见，下面就来演示。

### 在线学习与交叉验证 · On-line learning and cross-validation

当数据是一串点 $D = t^{(1)}, t^{(2)}, \ldots, t^{(N)}$ 时，log evidence 可以分解为一串「在线」预测性能之和：

```math
\begin{aligned}
\log P(D \mid H) = {} & \log P(t^{(1)} \mid H) + \log P(t^{(2)} \mid t^{(1)}, H) \\
& + \log P(t^{(3)} \mid t^{(1)}, t^{(2)}, H) + \cdots \\
& + \log P(t^{(N)} \mid t^{(1)} \ldots t^{(N-1)}, H).
\end{aligned} \qquad (28.18)
```

这个分解可以用来解释 evidence 与 leave-one-out cross-validation 这两种「预测能力」度量之间的差别。

cross-validation 只考察最后一项 $\log P(t^{(N)} \mid t^{(1)} \ldots t^{(N-1)}, H)$ 在数据的随机重排下的平均值。

而 evidence 求和的是：**模型从零开始**对整个数据预测得有多好。

### 「比特回吐」编码 · The 'bits-back' encoding method

另一个 MDL 思想实验（Hinton and van Camp, 1993）把随机比特也掺进消息里。

数据用参数块加数据块来传达。发出去的参数向量是从 posterior $P(w \mid D, H) = P(D \mid w, H)P(w \mid H)/P(D \mid H)$ 里抽的一个随机样本。

这个样本 $w$ 按任意小的粒度 $\delta_w$ 发送，用掉消息长度 $L(w \mid H) = -\log[P(w \mid H)\delta_w]$。

数据则相对于 $w$ 编码，用掉 $L(D \mid w, H) = -\log[P(D \mid w, H)\delta_D]$。

数据消息一旦被接收，接收方就能推断出当初用来从 posterior 里抽出 $w$ 的那些随机比特。

这样回收到的比特数是 $-\log[P(w \mid D, H)\delta_w]$。这些回收的比特不必计入消息长度——因为我们可以把另一条已最优编码的消息当作随机比特串来用，从而**在同一个传输里把那条消息也免费送出去了**。

于是净描述代价是：

```math
\begin{aligned}
& L(w \mid H) + L(D \mid w, H) - \text{`Bits back'} \\
&\quad = -\log \frac{P(w \mid H)\,P(D \mid w, H)\,\delta_D}{P(w \mid D, H)}
= -\log P(D \mid H) - \log \delta_D.
\end{aligned} \qquad (28.19)
```

这样，这个思想实验就给出了最优的描述长度。bits-back 编码后来被 Frey（1998）变成了一个实用压缩方法，用来压缩以 latent variable model 建模的数据。

### 延伸阅读 · Further reading

Bayesian 方法在 (Jaynes, 1983; Gull, 1988; Loredo, 1990) 里被介绍，并与 sampling-theory statistics 对照。

Bayesian 版本的奥卡姆剃刀在 (Gull, 1988; MacKay, 1992a) 的模型问题上被演示过。有用的教科书是 (Box and Tiao, 1973; Berger, 1985)。

有一场值得弄懂的争论：在 Bayesian inference 里到底允不允许使用 improper prior（Dawid et al., 1996）。

如果我们想做 model comparison（正如本章所讨论的），那**必须**用 proper prior——否则 evidence 和 Occam factor 都会变成

<span style="color:#b9770e;">**[关键结论]** 式 (28.19) 是本章最不平凡的一行：三段长度相加减出来的结果，**恰好等于最优值 $-\log P(D \mid H)$**，一个比特都不多。这不是巧合，而是「参数块里掺杂的随机性，正好抵消了为发送参数所付的代价」。</span>

<span style="color:#1e8449;">**[译注]**
把 (28.19) 的算术摊开，机制一目了然。三个对数相加时，$P(w \mid H)\cdot P(D \mid w, H)$ 恰好等于 $P(w \mid D, H)\cdot P(D \mid H)$（Bayes 公式移项），
所以分子分母里那个 $P(w \mid D, H)$ 直接约掉，只剩 $-\log P(D \mid H) - \log\delta_D$。
**「bits back」不是免费午餐，它是把「为了指定 $w$ 花了多少比特」用「$w$ 是从 posterior 抽出来的，因此携带了 $-\log P(w \mid D,H)\delta_w$ 比特的信息」精确抵扣掉。**

**消失测试**：没有这个抵扣，把 latent variable 模型的描述长度老老实实写成 $L(w \mid H) + L(D \mid w, H)$，会多出一项
$\mathrm{KL}\big(P(w \mid D, H) \,\|\, P(w \mid H)\big) \ge 0$，于是「变分下界」永远紧不上，你也无法说明为什么训练好的 VAE 的 ELBO 编码长度是**最优**的而不是「一个可优化的上界」。
换句话说，退化后的账本只能给出 $\text{ELBO} \le \log P(D)$，给不出等式成立的条件。

**落点**：式 (28.19) 在本页；Hinton and van Camp (1993) 是原出处，Frey (1998) 把它做成实用压缩器（factor analysis 的 bits-back 编码）；
variational 侧的同样结论见第 33 章（ELBO 与 $\mathrm{KL}$ 的关系）。前置只需 Bayes 公式与对数的四则运算，不越级。
</span>



变成毫无意义。

只有在**根本不打算做 model comparison**时，使用 improper prior 才可能是安全的；而即便在那种场合也有陷阱，Dawid 等人已经解释过。

我同意他们的建议：永远使用 proper prior；同时加一句鼓励——做计算时要聪明，要看出可以近似的地方。

## 28.4 习题 · Exercises

[exercise] **Exercise 28.1.**[3] Random variables $x$ come independently from a probability distribution $P(x)$. According to model $H_0$, $P(x)$ is a uniform distribution

```math
P(x \mid H_0) = \frac{1}{2}, \qquad x \in (-1, 1). \qquad (28.20)
```

According to model $H_1$, $P(x)$ is a nonuniform distribution with an unknown parameter $m \in (-1, 1)$:

```math
P(x \mid m, H_1) = \frac{1}{2}(1 + mx), \qquad x \in (-1, 1). \qquad (28.21)
```

Given the data $D = \{0.3, 0.5, 0.7, 0.8, 0.9\}$, what is the evidence for $H_0$ and $H_1$?

> **中文话题摘要**：五个数据点全部落在 $x \gt 0$ 一侧，$H_0$（均匀）与 $H_1$（带斜率 $m$ 的线性倾斜）各自的 evidence 是多少——关键在于 $H_1$ 的 $m$ 要知道到多准才能解释这五个点全为正，而那笔精度费用正好是 Occam factor。

[exercise] **Exercise 28.2.**[3] Datapoints $(x, t)$ are believed to come from a straight line. The experimenter chooses $x$, and $t$ is Gaussian-distributed about

```math
y = w_0 + w_1 x \qquad (28.22)
```

with variance $\sigma_\nu^2$. According to model $H_1$, the straight line is horizontal, so $w_1 = 0$. According to model $H_2$, $w_1$ is a parameter with prior distribution $\mathrm{Normal}(0, 1)$. Both models assign a prior distribution $\mathrm{Normal}(0, 1)$ to $w_0$. Given the data set $D = \{(-8, 8), (-2, 10), (6, 11)\}$, and assuming the noise level is $\sigma_\nu = 1$, what is the evidence for each model?

> **中文话题摘要**：三个点 $(x, t)$ 明显沿着一条正斜率直线走，比较「水平线」与「斜率带 $\mathrm{Normal}(0,1)$ prior 的直线」两个模型的 evidence——$H_2$ 的拟合更好，但要为「斜率事先可能落在 $[-1,1]$ 之外」付 Occam factor，两项谁大谁小要靠算。

[exercise] **Exercise 28.3.**[3] A six-sided die is rolled 30 times and the numbers of times each face came up were $F = \{3, 3, 2, 2, 9, 11\}$. What is the probability that the die is a perfectly fair die ('$H_0$'), assuming the alternative hypothesis $H_1$ says that the die has a biased distribution $p$, and the prior density for $p$ is uniform over the simplex $p_i \ge 0$, $\sum_i p_i = 1$?

Solve this problem two ways: exactly, using the helpful Dirichlet formulae (23.30, 23.31), and approximately, using Laplace's method. Notice that your choice of basis for the Laplace approximation is important. See MacKay (1998a) for discussion of this exercise.

> **中文话题摘要**：$30$ 次投掷得到 $F = \{3, 3, 2, 2, 9, 11\}$，问「这是一颗公平骰子」的概率——要用 Dirichlet 精确算一次、用 Laplace 近似再算一次，并体会**近似结果依赖你把参数坐标选在哪**（选 simplex 的自然坐标还是 log-ratio 坐标，得到的 Gaussian 体积不同）。

[exercise] **Exercise 28.4.**[3] The influence of race on the imposition of the death penalty for murder in America has been much studied. The following three-way table classifies $326$ cases in which the defendant was convicted of murder. The three variables are the defendant's race, the victim's race, and whether the defendant was sentenced to death. (Data from M. Radelet, 'Racial characteristics and imposition of the death penalty,' *American Sociological Review*, 46 (1981), pp. 918–927.)

原文把 $326$ 个案子排成并排的两栏小表（被告白人一栏、被告黑人一栏），这里合并成一张等价的四行表，行合计与原文一致：

| 被告 race | 受害者 race | 判死刑 Yes | 判死刑 No | 小计 |
|---|---|---|---|---|
| White defendant | White victim | 19 | 132 | 151 |
| White defendant | Black victim | 0 | 9 | 9 |
| Black defendant | White victim | 11 | 52 | 63 |
| Black defendant | Black victim | 6 | 97 | 103 |
| **合计** | — | **36** | **290** | **326** |

> **中文话题摘要**：一张 $2 \times 2 \times 2$ 的列联表，问「判死刑是否依赖受害者种族 / 被告种族」这四个图形模型的 evidence 各是多少——这是全书用 Occam factor 处理真实（且政治上敏感）数据的少数例子之一，作者本人明确说它只是 model comparison 的学术练习，不是关于种族偏见的严肃研究。

<span style="color:#1e8449;">**[译注]**
习题 28.1 是全书把 Occam factor 用到不能再用近似的地方的一个样板，值得先手算它再往下读第 29 章。

$H_0$ 下五个点各有密度 $1/2$，likelihood 与 $m$ 无关，$\mathrm{evidence}_{H_0} = (1/2)^5 = 1/32$。
$H_1$ 下先对 $m$ 取 prior（取均匀于 $(-1,1)$，密度 $1/2$）积分：
$P(D \mid H_1) = \int_{-1}^{1} \frac{1}{2}\prod_{n=1}^{5}\frac{1+mx_n}{2}\,dm = \frac{1}{2^6}\int_{-1}^{1}\prod_n (1+mx_n)\,dm$。
因为 $\prod_n(1+mx_n)$ 里 $m$ 的奇次项在对称区间上积分为零，只剩常数项与 $m^2$、$m^4$ 项：
结果为 $\frac{1}{64}\left(2 + \frac{2}{3}e_2 + \frac{2}{5}e_4\right)$，其中 $e_2 = \sum_{i \lt j} x_i x_j$、$e_4 = \sum x_i x_j x_k x_l$ 是初等对称多项式。

**消失测试**：不做这个积分而直接拿 $m_{\mathrm{MP}}$ 处的最高 likelihood 当 evidence，会得到 $\prod_n (1 + m_{\mathrm{MP}}x_n)$ 这一项，
它随 $m_{\mathrm{MP}}$ 单调增大到某个极端值，于是 $H_1$ 永远赢——**证据比会变成无条件支持倾斜模型**，
而正确的答案里 $H_1$ 要为「我们必须指定 $m$ 到多细」付一笔约 $\ln(1/\sigma_{m|D})$ 的费用。这笔费用不是修辞：五个点全正时 $\sigma_{m|D}$ 很小，$H_1$ 的胜幅因此被压下来。

**落点**：式 (28.20)(28.21) 在本页；Occam factor 的标量形式见 p349 的 (28.9)；同一道题的 Dirichlet 版本与 Laplace 版本见 Exercise 28.3（本页）与 (23.30)(23.31)。
</span>



看上去，受害者是白人时死刑适用得比受害者是黑人时频繁得多。受害者是白人时，$14\%$ 的被告被判死刑；受害者是黑人时，$6\%$ 的被告被判死刑。

† 用本页表格逐格复算：受害者白人时 $(19+11)/(19+132+11+52) = 30/214 = 14.0\%$；受害者黑人时 $(0+6)/(0+9+6+97) = 6/112 = 5.4\%$，原文写 $6\%$ 是取整。

〔顺带一提，这些数据提供了一个后来被称为 Simpson's paradox（辛普森悖论）的现象的例子：总体上被判死刑的白人被告比例更高，但在涉及黑人受害者的案子里黑人被告被判死刑的比例更高，在涉及白人受害者的案子里黑人被告被判死刑的比例也更高。〕

† 复算：总体白人被告 $(19+0)/(19+132+0+9) = 19/160 = 11.9\%$，总体黑人被告 $(11+6)/(11+52+6+97) = 17/166 = 10.2\%$，确实白人更高；而分层后黑人被告在两层的比例都更高（黑人受害者层 $6/103 = 5.8\%$ 对 $0/9 = 0\%$；白人受害者层 $11/63 = 17.5\%$ 对 $19/151 = 12.6\%$）。悖论成立的原因是「受害者种族」与「被告种族」严重不独立：白人被告的案子里 $151/160 = 94\%$ 的受害者是白人，黑人被告的案子里只有 $63/166 = 38\%$。

[Figure 28.9：关于「判死刑 $d$ 是否依赖受害者种族 $v$ 与凶手种族 $m$」的四个假设，画成 graphical model（图模型），箭头表示依赖方向。**已用 PyMuPDF 按 3 倍缩放裁图并视觉核对过连线，四张子图的确切结构是：**$\mathcal{H}_{11}$ 有两条箭头 $v \to d$ 与 $m \to d$；$\mathcal{H}_{10}$ 只有 $v \to d$；$\mathcal{H}_{01}$ 只有 $m \to d$；$\mathcal{H}_{00}$ 没有任何箭头。图注原文以 $\mathcal{H}_{01}$ 为例说明：它断言判死刑的概率依赖凶手的种族，但不依赖受害者的种族。]

量化图 28.9 所示四个备择假设各自的 evidence。

我得说明一下：我认为这四个模型**没有一个**是充分的——谋杀案里还有好几个额外变量很重要，比如说受害者与凶手是否相识、谋杀是否预谋、被告有无前科；这些变量一个都没进这张表。所以这是一个 model comparison 的学术练习，而不是对佛罗里达州种族偏见的严肃研究。

这些假设被画成 graphical model，箭头表示变量 $v$（受害者种族）、$m$（凶手种族）、$d$（是否判死刑）之间的依赖关系。

模型 $\mathcal{H}_{00}$ 只有一个自由参数，即被判死刑的概率；模型 $\mathcal{H}_{11}$ 有四个这样的参数，变量 $v$ 与 $m$ 的每种组合各一个。

给这些变量分配均匀 prior。结论对 prior 的选择有多敏感？

<span style="color:#1e8449;">**[译注]**
Simpson's paradox 在这个例子里不是花边，它是**为什么必须做 model comparison 而不能只看合并比例**的现场证据。

设 $P(d{=}1 \mid v, m)$ 为真值，合并比例是 $P(d{=}1) = \sum_{v,m} P(d{=}1 \mid v,m)P(v,m)$，它把「条件概率」与「$v,m$ 的联合分布」乘在一起。
本块数据里 $P(v{=}\text{white} \mid m{=}\text{black}) = 63/166 = 0.38$，而 $P(v{=}\text{white} \mid m{=}\text{white}) = 151/160 = 0.94$——
两层权重相差 $2.5$ 倍，足以把「每层都是黑人更高」翻转成「总体白人更高」。

**消失测试**：如果只报合并比例（$11.9\%$ 对 $10.2\%$），结论的方向会被完全颠倒；
只有把 $v$ 与 $m$ 都放进模型（即 $\mathcal{H}_{11}$ 那四个参数）才能看见分层的真实结构。
但反过来，$\mathcal{H}_{11}$ 有四个参数，要用 Occam factor 为它付账——这正是本页要你算的东西：
**数据本身支持哪种依赖结构，取决于「层级结构存在」这件事带来的拟合改善，是否超过四个参数的体积罚分。**

**落点**：四个模型的结构见本页图 28.9（已视觉核对）；Occam factor 的记账见 p349 (28.9)(28.10)；被判死刑比例的逐格复算见本页两处 `†`。
前置只需条件概率与全概率公式（6.042J 的离散概率一节），不越级。
</span>



## 关于第 29 章 · About Chapter 29

前面两章一直假设：我们关心的概率分布，用 Gaussian 近似就够了。**要是不够呢？**

我们已经见过一个例子——clustering（聚类）：那里的 likelihood function 是多峰的，而且在参数空间的某些位置有讨厌的无界高峰；所以「最大化后验概率 + 拟合一个 Gaussian」并不总行得通。

Laplace 方法碰到的这个困难，正是我们对 Monte Carlo methods 感兴趣的一个动机。事实上，Monte Carlo methods 提供了一整套通用工具，在 Bayesian 数据建模以及许多其他领域都有应用。

本章依次介绍一串方法：importance sampling、rejection sampling、Metropolis 方法、Gibbs sampling 与 slice sampling。对每一种方法，我们都讨论它是否预期能用于高维问题——比如 graphical model（图模型）推断里出现的那类问题。

〔graphical model 是一类概率模型，其中变量之间的依赖与独立关系，由一张图的边表示，图的节点就是这些变量。〕

沿途还会引入 Markov chain Monte Carlo（MCMC）方法的术语。下一章讨论减少 random walk 行为的高级方法。

关于 Monte Carlo methods 的细节、定理与证明，以及完整参考文献，请读者看 Neal (1993b)、Gilks et al. (1996)、Tanner (1996)。

本章里「sample」一词按下面这个意思用：**从一个分布 $P(x)$ 抽出的 sample，是单个实现 $x$，它的概率分布是 $P(x)$。** 这与统计学里另一种用法不同——那里的「sample」指的是一组实现 $\{x\}$。

讨论 transition probability matrix（转移概率矩阵）时，我用**右乘**约定：我喜欢让矩阵作用在右边，偏爱

```math
\mathbf{u} = M\mathbf{v} \qquad (29.1)
```

而不是

```math
\mathbf{u}^{\mathrm{T}} = \mathbf{v}^{\mathrm{T}}M^{\mathrm{T}}. \qquad (29.2)
```

一个 transition probability matrix $T_{ij}$（也写作 $T_{i|j}$）给出的是：已知当前 state 是 $j$，从 $j$ 跳到 $i$ 的概率。$T$ 的各列都是概率向量。

如果写成 transition probability density，参数顺序用同一套约定：$T(x'; x)$ 是从 $x$ 到 $x'$ 的转移概率密度。

这就很遗憾地意味着，你得习惯**从右往左读**——序列 $xyz$ 的概率是 $T(z; y)T(y; x)\pi(x)$。

<span style="color:#1e8449;">**[译注]**
这个「右乘 + 从右往左读」的约定不是排版偏好，它决定了本块后面所有矩阵表达式的书写顺序，一旦搞反，$T_{i|j}$ 与 $T_{j|i}$ 会整章互换。

具体说：$T_{ij}$ 定义为「已知当前在 $j$、跳到 $i$ 的概率」，即 $T_{ij} = P(x_{t+1} = i \mid x_t = j)$。
**列是概率向量**（$\sum_i T_{ij} = 1$），所以一个分布向量 $\pi$ 按 $T\pi$ 更新一次之后仍是概率向量；
而 $T$ 的行和一般不为一。若按行随机的习惯写 $P_{ij} = P(i \to j)$，那么本页的 $T$ 就是那个 $P$ 的转置。

**消失测试**：把约定搞反，stationary distribution 的条件 $\pi = T\pi$ 就变成 $\pi^{\mathrm{T}} = \pi^{\mathrm{T}}T$，
在 $T$ 不对称时（本块 p366 的 (29.31) 里 $Q(x';x) \ne Q(x;x')$ 一般成立），两种写法的解**不是同一个分布**。
更具体的可观测后果：p366 的 acceptance ratio 里那两个 proposal 比值的方向会反过来，
于是 detailed balance 不成立，链收敛到一个偏置的分布，而代码不会报错——这是 MCMC 实现里最常见、也最难用 trace plot 看出来的静默错误。

**落点**：式 (29.1)(29.2) 在本页；$T_{ij} = P(i \leftarrow j)$ 的用法见 p366 的 (29.31) 与 p366「Convergence」一段；
连续情形 $T(x';x)$ 的读法见本页末句。线性代数侧只用到「矩阵乘向量」与「转置」，Strang 第 1–2 章即可，不越级。
</span>



# 29 Monte Carlo Methods

## 29.1 要解决的问题 · The problems to be solved

Monte Carlo methods 是利用随机数的计算技术。它的目标，是解决下面两个问题中的一个或两个。

**问题 1**：从给定的概率分布 $P(x)$ 生成样本 $\{x^{(r)}\}_{r=1}^{R}$。

**问题 2**：估计该分布下某函数的 expectation（期望），例如

```math
\Phi = \langle \phi(x) \rangle \equiv \int \mathrm{d}^N\!x\; P(x)\,\phi(x). \qquad (29.3)
```

这个概率分布 $P(x)$ 我们称为 **target density**（目标密度）。它可能是统计物理里的一个分布，也可能是数据建模里冒出来的某个条件分布——比如给定观测数据后，某模型参数的后验概率。

我们一般假设 $x$ 是 $N$ 维实向量，分量为 $x_n$；但有时也会考虑离散空间。

我们可能想求 expectation 的函数 $\phi(x)$，简单例子包括我们想预测的量的第一、第二阶矩——由它们可以算出均值与方差。比如某个量 $t$ 依赖 $x$，那么 $t$ 在 $P(x)$ 下的均值与方差，可以通过求 $\phi_1(x) = t(x)$ 与 $\phi_2(x) = (t(x))^2$ 的 expectation 得到：

```math
\Phi_1 \equiv \mathrm{E}[\phi_1(x)], \qquad \Phi_2 \equiv \mathrm{E}[\phi_2(x)], \qquad (29.4)
```

然后用

```math
\bar{t} = \Phi_1, \qquad \mathrm{var}(t) = \Phi_2 - \Phi_1^2. \qquad (29.5)
```

这里假定 $P(x)$ 足够复杂，我们没法用精确方法求出这些 expectation；所以我们才关心 Monte Carlo methods。

我们将集中在第一个问题（sampling）上，因为一旦它解决了，第二个问题就能靠那些随机样本 $\{x^{(r)}\}_{r=1}^{R}$ 用下面的 estimator 解决：

```math
\hat{\Phi} \equiv \frac{1}{R}\sum_{r}\phi(x^{(r)}). \qquad (29.6)
```

如果这些向量 $\{x^{(r)}\}_{r=1}^{R}$ 确实是从 $P(x)$ 生成的，那么 $\hat{\Phi}$ 的 expectation 就是 $\Phi$。而且随样本数 $R$ 增加，$\hat{\Phi}$ 的方差按 $\sigma^2/R$ 下降，其中 $\sigma^2$ 是 $\phi$ 的方差：

```math
\sigma^2 = \int \mathrm{d}^N\!x\; P(x)\,\big(\phi(x) - \Phi\big)^2. \qquad (29.7)
```

<span style="color:#1f618d;">**[定义]** 本章反复出现的三个量要分清：**target density** $P(x)$（我们想要的分布）、**estimator** $\hat{\Phi}$（用样本算出的随机变量）、**variance** $\sigma^2/R$（估计误差的尺度，$R$ 是样本数）。三者里只有 $\hat{\Phi}$ 是随机的。</span>



[Figure 29.1：(a) 函数 $P^*(x) = \exp\{0.4(x-0.4)^2 - 0.08x^4\}$，横轴 $x \in [-4, 4]$，纵轴 $P^*(x) \in [0, 3]$。曲线的具体形状（单峰的位置与高度）无法从文字层复原，只能读出坐标轴范围；正文只用它提「即使画得出这条曲线，也不等于能从中抽样」。(b) 同一个 $P^*(x)$ 在一组等距离散点 $\{x_i\}$ 上求值的结果，对应「能不能从这个离散分布抽样」。]

这是 Monte Carlo methods 的重要性质之一。

**Monte Carlo 估计 (29.6) 的精度只取决于 $\phi$ 的方差，不取决于被采样空间的维数。**

准确地说，$\hat{\Phi}$ 的方差按 $\sigma^2/R$ 走。因此不管 $x$ 是多少维，也许只要十来个独立样本 $\{x^{(r)}\}$ 就足以把 $\Phi$ 估到令人满意的程度。

不过我们后面会发现，高维会给 Monte Carlo methods 带来**别的**困难：从一个给定分布 $P(x)$ 得到独立样本，往往并不容易。

### 为什么从 $P(x)$ 抽样很难？ · Why is sampling from $P(x)$ hard?

我们假设想抽样的密度 $P(x)$ 至少能算到一个乘性常数之内；也就是说，我们能算出一个函数 $P^*(x)$，使

```math
P(x) = P^*(x)/Z. \qquad (29.8)
```

既然能算 $P^*(x)$，为什么不能轻易解决第一个问题？为什么从 $P(x)$ 得到样本一般是困难的？

有两个困难。

**第一**，我们通常不知道那个归一化常数

```math
Z = \int \mathrm{d}^N\!x\; P^*(x). \qquad (29.9)
```

**第二**，就算知道了 $Z$，从 $P(x)$ 抽样仍然是个难题，在高维空间里尤其如此——因为除了枚举大部分或全部可能状态之外，没有明显办法从 $P$ 里抽样。

按定义，$P$ 的正确样本会倾向于落在 $x$ 空间里 $P(x)$ 大的地方；可是，**不逐处计算 $P(x)$，你怎么找出那些 $P(x)$ 大的地方？**

只有少数几种高维密度是容易直接抽样的，例如 Gaussian distribution。

让我们从一个简单的一维例子开始。想象我们要从密度 $P(x) = P^*(x)/Z$ 抽样，其中

```math
P^*(x) = \exp\left\{0.4(x - 0.4)^2 - 0.08x^{4}\right\}, \qquad x \in (-\infty, \infty). \qquad (29.10)
```

我们可以把这条曲线画出来（图 29.1a）。但这并不意味着我们能从中抽样——首先，我们并不知道归一化常数 $Z$。

<span style="color:#1e8449;">**[译注]**
(29.7) 里的 $\sigma^2$ 是整章唯一一次「好消息」，必须看清它好在哪里、又不好在哪里。

好消息：$\mathrm{var}(\hat{\Phi}) = \sigma^2/R$ **没有 $N$**。同样 $R = 10^4$ 个样本，无论 $N = 2$ 还是 $N = 1000$，
误差棒都是 $\sigma/100$。这与网格法的 $50^N$ 形成残酷对比（见 p359 的 $(50)^{1000}$ 与 $2^{1000}$）。

不好的一面藏在 $\sigma^2$ 里：$\sigma^2 = \int \mathrm{d}^N\!x\, P(x)(\phi(x) - \Phi)^2$ 是对 $P$ 的一个**全域**积分，
若 $\phi(x)$ 在高维下相对 $P$ 波动剧烈（比如 $\phi$ 是多峰函数、或 $P$ 的典型集极窄），$\sigma^2$ 本身可以大到让 $\sigma/\sqrt{R}$ 失去意义。
更麻烦的是 $\sigma^2$ 通常**算不出来**——它正是问题 2 的一种情形。

**消失测试**：如果误差真的只依赖 $\sigma^2$ 而与 $N$ 无关，那高维就完全不成问题；
偏偏 (29.7) 在 $N$ 大时既算不出、又常常很大，于是一个本来「维数无关」的定理，在实际使用中必须靠「如何从 $P$ 抽到真正独立的样本」来兜底——这就是本章后面五种方法存在的全部理由。
抽掉「$R^{-1/2}$ 收敛」这一条，Monte Carlo 相对确定性求积就没有任何优势；抽掉「$\sigma^2$ 通常未知」这一条，就不会有人去写 p362 那整段关于「importance sampling 的方差估不出来」的警告。

**落点**：式 (29.3)–(29.7) 见 p357–358；$\sigma^2$ 不可算的后果见 p362「A practical difficulty with importance sampling」一段；
$R^{-1/2}$ 与网格法 $h^{-N}$ 的对比见 p359 的 $50^{1000}$、$2^{1000}$ 与投资回报式的算账。前置只需 Chebyshev / 大数定律（6.042J 概率部分），不越级。
</span>



为了给自己一个更简单的问题，我们可以把变量 $x$ 离散化，于是要问的是：从一组有限、等距点 $\{x_i\}$ 上的离散概率分布里抽样（图 29.1b）。这个问题怎么解？

如果在每点 $x_i$ 上算出 $p_i^* = P^*(x_i)$，我们就能算

```math
Z = \sum_i p_i^* \qquad (29.11)
```

以及

```math
p_i = p_i^*/Z \qquad (29.12)
```

然后就能用各种基于随机比特源的方法，从概率分布 $\{p_i\}$ 抽样（见 §6.3）。

但是——这套做法的**代价**是多少？它随空间维数 $N$ 怎么增长？

让我们盯住第一步、也就是算 $Z$（式 29.11）的代价。要算 $Z$，必须访问空间里的**每一个点**。

图 29.1b 里一维有 50 个等距点。如果我们这个系统是 $N$ 维的，比如 $N = 1000$，那么相应的点数就是 $50^{1000}$——一个难以想象的 $P^*$ 求值次数。

哪怕每个分量 $x_n$ 只取两个离散值，$P^*$ 的求值次数也是 $2^{1000}$，一个仍然可怕地巨大的数。

假使宇宙里的每个电子（大约有 $2^{266}$ 个）都是一台 1000 千兆赫的计算机，每秒能对一万亿（$2^{40}$）个状态求 $P^*$，而这 $2^{266}$ 台机器跑上相当于宇宙年龄的时间（$2^{58}$ 秒），它们加起来也只能访问 $2^{364}$ 个状态。

要让 $2^{1000}$ 个状态全都被访问过，我们得等 $2^{636} \simeq 10^{190}$ 个宇宙年龄过去。

† $2^{636} = 10^{636 \times 0.30103} = 10^{191.45}$，数量级应是 $10^{191}$ 而不是 $10^{190}$；作者此处按 $10^{190}$ 写，误差在 $\times 3.5$ 之内，不影响「不可行」这个结论。

有 $2^{1000}$ 个状态的系统遍地都是。⋆ 一个例子是 1000 个 spin 的集合，比如 $30 \times 30$ 的一小块 Ising model（伊辛模型），其概率分布正比于

```math
P^*(x) = \exp\left[-\beta E(x)\right] \qquad (29.13)
```

其中 $x_n \in \{\pm 1\}$，而

```math
E(x) = -\left[\frac{1}{2}\sum_{m,n} J_{mn}x_m x_n + \sum_n H_n x_n\right]. \qquad (29.14)
```

⋆ 给美国读者的翻译：「such systems are a dime a dozen」（这种系统一毛钱一打）；顺带说，这个等价关系（$10$ 美分 $= 6$ 便士）正好说明我们两国货币的正确汇率是 $£1.00 = \$1.67$。

能量函数 $E(x)$ 对任何 $x$ 都能随手算出来。可如果我们想在**所有**状态 $x$ 上算它，所需机时就是 $2^{1000}$ 次函数求值。

Ising model 是个存在已久的老模型，但「从分布 $P(x) = P^*(x)/Z$ 生成样本」这件事至今仍是活跃的研究领域；从这个分布抽出的第一批「精确」样本，出自 Propp and Wilson (1996) 的开创性工作，我们将在第 32 章描述。

### 一个有用的类比 · A useful analogy

[Figure 29.2：一个湖，湖在 $x = (x, y)$ 处的深度就是 $P^*(x)$。它把「从 $P$ 抽样」类比成「在湖里随机取水样」，把「估 $\Phi$」类比成「估平均浮游生物浓度」，核心难点是「事先对湖底地形一无所知」。]

想象这两件事：从湖里随机取水样，以及求平均浮游生物浓度（图 29.2）。

湖在 $x = (x, y)$ 处的深度是 $P^*(x)$；为了让这个类比成立，我们再断言浮游生物浓度是 $x$ 的一个函数 $\phi(x)$。

需要的平均浓度就是一个像 (29.3) 那样的积分，即

```math
\Phi = \langle \phi(x) \rangle \equiv \frac{1}{Z}\int \mathrm{d}^N\!x\; P^*(x)\,\phi(x), \qquad (29.15)
```



其中 $Z = \int \mathrm{d}x\,\mathrm{d}y\; P^*(x)$ 就是湖的体积。

你被提供了一条船、一套卫星导航系统，以及一条测深锤。

用导航系统，你可以把船开到地图上任意想要的位置 $x$；用测深锤，你可以测得该点的 $P^*(x)$。你也可以量出那里的浮游生物浓度。

**问题 1** 是：在湖里随机取 $1\ \mathrm{cm}^3$ 的水样，取法要使每一份水样来自湖内任意位置的机会均等。

**问题 2** 是：求平均浮游生物浓度。

这两个问题难解，是因为开局时我们对深度 $P^*(x)$ 一无所知。

[Figure 29.3：湖的一个剖面（切片），其中包含若干峡谷。它要演示的是：湖的大部分体积可能藏在狭窄而深的水下峡谷里，于是「正确地抽样」与「正确地估 $\Phi$」都要求方法自己去发现这些峡谷，并算出它们的体积相对于湖其余部分的比例。]

也许湖的大部分体积都装在那狭窄、深邃的水下峡谷里（图 29.3）；若真是这样，那么为了正确地从湖中抽样、并正确地估计 $\Phi$，我们的方法必须**隐含地**发现这些峡谷，并求出它们的体积相对于湖其余部分的比例。

难是难，不过我们将会看到，聪明的 Monte Carlo methods 能解决它们。

### 均匀抽样 · Uniform sampling

既然已经承认我们无法穷尽地访问状态空间里的每个位置 $x$，那我们也许可以考虑另一种做法：从状态空间里**均匀**随机地抽样本 $\{x^{(r)}\}_{r=1}^{R}$，在这些点上算 $P^*(x)$，用这个来解决问题 2（估计函数 $\phi(x)$ 的 expectation）。

于是可以引入归一化常数 $Z_R$：

```math
Z_R = \sum_{r=1}^{R} P^*(x^{(r)}), \qquad (29.16)
```

再用

```math
\hat{\Phi} = \frac{\sum_{r=1}^{R}\phi(x^{(r)})\,P^*(x^{(r)})}{Z_R} \qquad (29.17)
```

来估计 $\Phi = \int \mathrm{d}^N\!x\,\phi(x)P(x)$。

这个策略有什么毛病吗？那要看具体的函数 $\phi(x)$ 与 $P^*(x)$。

让我们假定 $\phi(x)$ 是个良性、光滑变化的函数，把注意力放在 $P^*(x)$ 的性质上。

正如我们在第 4 章学到的：高维分布常常集中在状态空间里一个被称为 typical set（典型集）$T$ 的小区域内，其体积为 $|T| \simeq 2^{H(X)}$，其中 $H(X)$ 是概率分布 $P(x)$ 的 entropy。

如果几乎全部概率质量都位于 typical set 里，而 $\phi(x)$ 又是良性函数，那么 $\Phi = \int \mathrm{d}^N\!x\,\phi(x)P(x)$ 的值主要由 $\phi(x)$ 在 typical set 上取的值决定。

所以，均匀抽样要想有机会给出 $\Phi$ 的靠谱估计，必须让样本数 $R$ 足够大，大到我们**至少有一两次**命中 typical set 的可能性不低。

那么，需要多少样本？还是拿 Ising model 说。

〔严格地说，Ising model 未必是个好例子，因为它不一定有第 4 章所定义的那种 typical set；那里对 typical set 的定义是「所有状态的 log probability 都接近 entropy」，对 Ising model 来说这意味着「能量非常接近平均能量」；但是在相变附近，能量的方差（也就是 heat capacity，热容）可能发散，这意味着随机状态的能量并不一定被期望很接近平均能量。〕

状态空间的总大小是 $2^N$ 个状态，而 typical set 的大小是 $2^H$。所以每一个样本落进 typical set 的机会是 $2^H/2^N$。

<span style="color:#1e8449;">**[译注]**
这一页的算账是全章的气势所在，值得把每一步都钉死，因为它证明的不是「均匀抽样慢一点」，而是**「均匀抽样在物理上不可能」**。

数字链：$50^{1000} = 10^{1000\lg 50} = 10^{1699}$；$2^{1000} = 10^{301.03}$；
电子数 $10^{80} = 2^{265.75}$；$1000\ \mathrm{GHz} = 10^{12} = 2^{39.86}$ 次/秒；宇宙年龄 $1.4\times10^{10}$ 年 $\approx 4.4\times10^{17}\ \mathrm{s} = 2^{58.6}$。
相乘：$2^{266+40+58} = 2^{364}$，与 $2^{1000}$ 相差 $2^{636}$，挡住我们的正是这个指数差。

**消失测试**：把这条算账抽掉，「为什么不能用网格 / 均匀抽样」就退化成一句印象式的「维数灾难」；
而它的真实含义是**可判定**的：想要 $\Phi$ 的 $10\%$ 精度，网格法需要的点数随 $N$ 指数增长，
在 $N = 1000$ 时需求量级比「宇宙全体电子算到宇宙终结」还多 $10^{191}$ 倍。反之，只要有一种方法能让误差按 $R^{-1/2}$ 走（p358 的 (29.7)），
$R = 10^{4}$ 就够——**从 $10^{190}$ 宇宙年龄降到一万次函数求值，指数级换成对数级**，这就是 Monte Carlo 存在的唯一理由。

**落点**：$50^{1000}$、$2^{1000}$、$2^{364}$、$2^{636}$ 都在本页；$R^{-1/2}$ 见 p358 的 (29.7)；
Ising model 的概率定义见 (29.13)(29.14)；替代网格法的均匀抽样估计量见 p360 的 (29.16)(29.17)。
数值侧只需换底公式 $\lg 2 = 0.30103$，不越级。
</span>



[Figure 29.4：(a) 64 个 spin 的 Ising model 的 entropy 随温度的变化，横轴温度 $0$–$6$，纵轴熵从 $0$ 到 $64\log 2$（即 64 bits 是上限）。曲线无法在这些坐标上逐点复原，正文只用到「临界温度 $\theta_c = 2.27$ 附近熵约为 $N/2$ bits」这一个读数。(b) 1024 个 spin 的 Ising model 的一个状态，是个 $32 \times 32$ 的黑白格图，格子取值无法复原。]

于是，要命中 typical set 一次，所需样本数是

```math
R_{\min} \simeq 2^{N-H} \qquad (29.18)
```

这个量级。

那么 $H$ 是多少？在高温下，Ising model 的概率分布趋于均匀分布，熵趋于 $H_{\max} = N$ bits，这意味着 $R_{\min}$ 是 1 的量级。在这种条件下，均匀抽样完全可能是个估 $\Phi$ 的可行技术。

但高温没什么意思。有意思得多的是**中间温度**，比如 Ising model 从有序相融化为无序相的那个临界温度。无限大 Ising model 的临界温度是 $\theta_c = 2.27$。在这个温度上，Ising model 的熵大约是 $N/2$ bits（图 29.4）。

对这个概率分布，仅仅为了命中 typical set 一次，所需样本数就是

```math
R_{\min} \simeq 2^{N - N/2} = 2^{N/2} \qquad (29.19)
```

的量级；当 $N = 1000$ 时，这大约是 $10^{150}$。这差不多是宇宙粒子数的**平方**。

于是，均匀抽样对研究中等尺度的 Ising model 来说完全没用。而且在大多数高维问题里，如果分布 $P(x)$ 并非真的均匀，均匀抽样也多半派不上用场。

### 总览 · Overview

既然已经确认：**即便 $P^*(x)$ 很好算，从一个高维分布 $P(x) = P^*(x)/Z$ 抽样也是困难的**，下面我们来研究一串更精巧的 Monte Carlo methods：importance sampling、rejection sampling、Metropolis 方法、Gibbs sampling、slice sampling。

## 29.2 重要性抽样 · Importance sampling

Importance sampling 不是从 $P(x)$ 生成样本的方法（那是问题 1）；它只是一个估计函数 $\phi(x)$ 的 expectation 的方法（问题 2）。它可以看成均匀抽样方法的推广。

为了说明方便，设想 target distribution 是一维密度 $P(x)$。

假设我们能在任意选定的点 $x$ 上算出这个密度，至少算到一个乘性常数之内；也就是我们能算出一个函数 $P^*(x)$，使

```math
P(x) = P^*(x)/Z. \qquad (29.20)
```

<span style="color:#1e8449;">**[译注]**
式 (29.18) 把「均匀抽样为什么失败」从叙事变成了一个**只依赖 entropy 的判据**，这是本章最可复用的一个式子。

推导只需一行：典型集体积 $|T| \simeq 2^{H}$，全空间 $2^{N}$，故单次命中的概率是 $2^{H-N}$，
$R$ 次独立抽样至少命中一次的概率是 $1 - (1 - 2^{H-N})^{R} \approx 1 - e^{-R\,2^{H-N}}$，要它达到常数即得 $R_{\min} \simeq 2^{N-H}$。

**判据的用处在于它给出「什么时候均匀抽样还行」的边界**：$H = N$ 时 $R_{\min} \simeq 1$（高温，分布本来就近均匀）；
$H = N/2$ 时 $R_{\min} \simeq 2^{N/2}$（临界温度）。$N = 1000$ 给出 $2^{500} = 10^{150.5}$，正是书里的 $10^{150}$，
而宇宙粒子数 $10^{80}$，所以「平方」这个说法是精确的。

**消失测试**：没有这个判据，你会把均匀抽样的失败归因于「样本不够多」，于是试图把 $R$ 从 $10^{4}$ 提到 $10^{8}$ 来补救；
而判据说得很清楚，要补的量是 $10^{150}$ 量级，**不是换台更快的机器或写更快的 C 代码能解决的**，必须是换算法。
这条判据同时解释了为什么后面五种方法都刻意去做同一件事——把「盲抽」换成「沿概率质量走」。

**落点**：式 (29.18)(29.19) 在本页；$2^{H-N}$ 的来源是第 4 章的 typical set（$|T| \simeq 2^{H(X)}$），见 p360；
$\theta_c = 2.27$ 与 $H \approx N/2$ 出自图 29.4(a)。前置是 entropy 的定义 $H = -\sum p \log p$ 与典型集，不越级。
</span>



但 $P(x)$ 这个函数太复杂，我们没法直接从中抽样。

现在假设我们有另一个更简单的密度 $Q(x)$，可以从中生成样本，也能算到一个乘性常数之内（也就是说，我们能算出 $Q^*(x)$，其中 $Q(x) = Q^*(x)/Z_Q$）。

$P^*$、$Q^*$ 与 $\phi$ 的一个例子画在图 29.5 里，我们把 $Q$ 叫作 **sampler density**（抽样密度）。

[Figure 29.5：importance sampling 涉及的三个函数。我们想估 $\phi(x)$ 在 $P(x) \propto P^*(x)$ 下的 expectation；我们可以从更简单的分布 $Q(x) \propto Q^*(x)$ 抽样本；$Q^*$ 与 $P^*$ 在任意点都能算。图中三条曲线共用一条横轴，$P^*$ 与 $Q^*$ 形状相近但不同，$\phi$ 是一条平缓曲线；具体曲线形状无法从文字层复原。]

在 importance sampling 里，我们从 $Q(x)$ 生成 $R$ 个样本 $\{x^{(r)}\}_{r=1}^{R}$。

如果这些点是从 $P(x)$ 抽的，那我们就能用式 (29.6) 估 $\Phi$。可是当我们从 $Q$ 抽样时，$Q(x)$ 大于 $P(x)$ 的位置上，$x$ 的取值会在这个 estimator 里被**过度代表**；而 $Q(x)$ 小于 $P(x)$ 的位置上则被**代表不足**。

为了补偿「我们是从错误的分布抽的」这个事实，我们引入权重

```math
w_r \equiv \frac{P^*(x^{(r)})}{Q^*(x^{(r)})} \qquad (29.21)
```

用它来调整每个点在 estimator 里的「重要性」：

```math
\hat{\Phi} \equiv \frac{\sum_r w_r \,\phi(x^{(r)})}{\sum_r w_r}. \qquad (29.22)
```

[exercise] **Exercise 29.1.**[2, p.384] Prove that, if $Q(x)$ is non-zero for all $x$ where $P(x)$ is non-zero, the estimator $\hat{\Phi}$ converges to $\Phi$, the mean value of $\phi(x)$, as $R$ increases. What is the variance of this estimator, asymptotically? Hint: consider the statistics of the numerator and the denominator separately. Is the estimator $\hat{\Phi}$ an unbiased estimator for small $R$?

> **中文话题摘要**：要证明「$Q$ 在所有 $P$ 非零处也非零」时 $\hat{\Phi}$ 依概率收敛到 $\Phi$，并求出渐近方差（提示：分子分母分别看）；最后追问「$R$ 很小时它是不是 unbiased」——答案是不是，自归一化的比值估计有 $O(1/R)$ 的偏置。

importance sampling 有一个实用上的困难：**很难估计 $\hat{\Phi}$ 到底有多可靠。**

这个 estimator 的方差事先未知，因为它依赖一个涉及 $P^*(x)$ 的函数在 $x$ 上的积分。

而且 $\hat{\Phi}$ 的方差很难估，因为 $w_r$ 与 $w_r\phi(x^{(r)})$ 的经验方差，未必是式 (29.22) 里分子分母真实方差的好指标。

如果 proposal density $Q(x)$ 在某个 $|\phi(x)P^*(x)|$ 很大的区域里很小，那么完全可能出现这种情况：即便已经生成了很多点 $x^{(r)}$，也没有一个落进那个区域。

这时对 $\Phi$ 的估计会错得离谱，而**经验方差里不会有任何迹象**显示 $\hat{\Phi}$ 的真实方差很大。

[Figure 29.6：importance sampling 实况。(a) 用 Gaussian sampler density；(b) 用 Cauchy sampler density。纵轴是估计值 $\hat{\Phi}$，范围 $-7.2$ 到 $-6.2$；水平线表示 $\Phi$ 的真值；横轴是样本数，对数坐标，从 $10$ 到 $10^{6}$。逐点数值无法复原；正文只用到「(a) 在 $500$ 个样本处看似稳定其实错、(b) 在约 $5000$ 个样本后收敛」这两个定性结论。]

### importance sampling 的一个警示性例子 · Cautionary illustration of importance sampling

在一个关于氨基酸概率分布建模的玩具问题里（一维变量 $x$），我用 importance sampling 估了一个感兴趣的量。用 Gaussian sampler 与 Cauchy sampler 的结果画在图 29.6 里。横轴是样本数，对数刻度。



在 Gaussian sampler 的情形，评估到大约 500 个样本时，人可能就想叫停了；但显然有一些罕见样本对 $\hat{\Phi}$ 贡献巨大，于是 500 个样本处的估计值是错的。

即便采样到一百万次，估计值也仍然没有稳定到真值附近。

相比之下，Cauchy sampler 没有这种 glitch；它（在这个图所示的尺度上）大约 5000 个样本后就收敛了。

这个例子说明：**importance sampler 必须有重尾（heavy tails）。**

[Figure 29.7：一个多峰的 $P^*(x)$（若干相距很远的峰）与一个单峰的 sampler $Q(x)$（只拟合其中一个峰）。它要说的是：用一个只覆盖一个峰的单峰 $Q$ 去做 importance sampling，会把其余峰的贡献几乎全部漏掉，权重动态范围因此失控。]

[exercise] **Exercise 29.2.**[2, p.385] Consider the situation where $P^*(x)$ is multimodal, consisting of several widely-separated peaks. (Probability distributions like this arise frequently in statistical data modelling.) Discuss whether it is a wise strategy to do importance sampling using a sampler $Q(x)$ that is a unimodal distribution fitted to one of these peaks. Assume that the function $\phi(x)$ whose mean $\Phi$ is to be estimated is a smoothly varying function of $x$ such as $mx + c$. Describe the typical evolution of the estimator $\hat{\Phi}$ as a function of the number of samples $R$.

> **中文话题摘要**：$P^*$ 有若干个相距很远的峰，若只拿一个单峰 $Q$ 去拟合其中一个峰做 importance sampling，会怎样——以及当 $\phi$ 是 $mx+c$ 这种平缓函数时，$\hat{\Phi}$ 随 $R$ 的典型演化长什么样（答案：长时间在错值附近「稳定」，偶尔跳一下）。

### 高维下的 importance sampling · Importance sampling in many dimensions

我们已经看到，即使在一维的 importance sampling 问题上也要小心。那么 importance sampling 在更高维的空间里（比如说 $N = 1000$）是不是个有用的技术？

考虑一个简单的案例研究：target density $P(x)$ 是球内的均匀分布，

```math
P^*(x) = \begin{cases} 1, & 0 \le \rho(x) \le R_P, \\ 0, & \rho(x) \gt R_P, \end{cases} \qquad (29.23)
```

其中 $\rho(x) \equiv \left(\sum_i x_i^2\right)^{1/2}$；而 proposal density 是以原点为中心的 Gaussian：

```math
Q(x) = \prod_i \mathrm{Normal}(x_i; 0, \sigma^2). \qquad (29.24)
```

如果 estimator $\hat{\Phi}$ 被少数几个大权重 $w_r$ 支配，importance-sampling 方法就要出麻烦。那么权重 $w_r$ 的典型取值范围是多少？

从第一部分关于典型序列的讨论——例如看 Exercise 6.14（p.124）——我们知道：若 $\rho$ 是 $Q$ 的一个样本到原点的距离，则 $\rho^2$ 大致服从 Gaussian 分布，其均值与标准差为

```math
\rho^2 \sim N\sigma^2 \pm \sqrt{2N}\,\sigma^2. \qquad (29.25)
```

因此几乎所有的 $Q$ 样本，都落在一个到原点距离非常接近 $\sqrt{N}\sigma$ 的 typical set 里。

设 $\sigma$ 取得使 $Q$ 的 typical set 落在半径 $R_P$ 的球内。〔若不这样取，大数定律就意味着从 $Q$ 生成的几乎所有样本都会落到 $R_P$ 之外，权重为零。〕

那么我们知道，$Q$ 的大多数样本上 $Q$ 的取值落在范围

```math
\frac{1}{(2\pi\sigma^2)^{N/2}}\exp\left(-\frac{N}{2} \pm \frac{\sqrt{2N}}{2}\right) \qquad (29.26)
```

之内。于是权重 $w_r = P^*/Q$ 的典型取值就在范围

```math
(2\pi\sigma^2)^{N/2}\exp\left(\frac{N}{2} \pm \frac{\sqrt{2N}}{2}\right) \qquad (29.27)
```

之内。



[Figure 29.8：rejection sampling。(a) 涉及的两个函数：我们想要来自 $P(x) \propto P^*(x)$ 的样本，能从 $Q(x) \propto Q^*(x)$ 抽样本，并且知道一个常数 $c$ 使得对所有 $x$ 有 $cQ^*(x) \gt P^*(x)$。(b) 在曲线 $cQ^*(x)$ 下方的浅阴影区域里随机生成一个点 $(x, u)$；若该点同时落在 $P^*(x)$ 下方则接受它。曲线形状无法从文字层复原，正文只用到「浅色区是 $cQ^*$ 下、深色区是 $P^*$ 下」这个上下包含关系。]

所以，如果抽一百个样本，权重的典型范围会是什么？我们可以用式 (29.27) 里标准差的**两倍**来粗略估计最大权重与中位权重之比。最大权重与中位权重典型上会落在比值

```math
\frac{w_r^{\max}}{w_r^{\mathrm{med}}} = \exp\left(\sqrt{2N}\right) \qquad (29.28)
```

上。

于是在 $N = 1000$ 维里，一百个样本之后的最大权重，很可能比中位权重大约 $10^{19}$ 倍。

因此，一个高维问题的 importance sampling 估计，极可能被少数几个权重巨大的样本彻底支配。

**结论**：高维下的 importance sampling 常常有两个困难。

第一，我们需要拿到落在 $P$ 的 typical set 里的样本，而这可能很费时间，除非 $Q$ 是 $P$ 的好近似。

第二，即便拿到了 typical set 里的样本，与它们关联的权重也很可能相差很大的倍数——因为 typical set 里各点的概率虽然彼此相近，却仍然相差 $\exp(\sqrt{N})$ 量级，于是权重也会这样，除非 $Q$ 是 $P$ 的近乎完美近似。

## 29.3 拒绝抽样 · Rejection sampling

我们再次假设有一个一维密度 $P(x) = P^*(x)/Z$，它太复杂，没法直接抽样。

假设我们有一个更简单的 proposal density $Q(x)$（像之前一样，能算到一个乘性因子 $Z_Q$ 之内），并且能从中生成样本。

再假设我们知道一个常数 $c$ 的值，使得

```math
c\,Q^*(x) \gt P^*(x), \quad \text{for all } x. \qquad (29.29)
```

两个函数的示意图画在图 29.8a 里。

我们生成两个随机数。第一个 $x$ 由 proposal density $Q(x)$ 生成。

接着算出 $cQ^*(x)$，并在区间 $[0, cQ^*(x)]$ 上生成一个均匀分布的随机变量 $u$。

这两个随机数可以看成在二维平面上选了一个点，如图 29.8b 所示。

现在我们算出 $P^*(x)$，把 $u$ 与 $P^*(x)$ 比较，据此接受或拒绝样本 $x$：若 $u \gt P^*(x)$ 则拒绝 $x$；否则接受，也就是把 $x$ 加进样本集 $\{x^{(r)}\}$。$u$ 的取值随后丢掉。

<span style="color:#1e8449;">**[译注]**
式 (29.28) 的 $\exp(\sqrt{2N})$ 是本章最容易被低估的一个数，因为它看上去只是「某个常数倍」，实际是**维度上加倍的指数**。

来源很直接：由 (29.26)(29.27)，$\ln w$ 在典型集上的波动幅度是 $\pm\frac{\sqrt{2N}}{2}$（单位是 nats），
所以「最大与中位相差一个标准差」就意味着比值 $e^{\sqrt{2N}/2}$。书里取**两倍**标准差，于是得到 $e^{\sqrt{2N}}$。
$N = 1000$ 时 $\sqrt{2000} = 44.72$，$e^{44.72} = 10^{19.4}$，正是书里的 $10^{19}$。

**消失测试**：没有这个估计，你会以为 importance sampling 在高维「只是效率低一些」，于是老老实实从 $R = 10^{4}$ 加到 $10^{6}$ 想补救；
而 $e^{\sqrt{2N}}$ 说的是一件不同的事：**权重动态范围本身随 $\sqrt{N}$ 指数增长**，加样本只会让「更多同样巨大的权重」出现，
估计值不会向真值收敛（这正是图 29.6a 在 $10^{6}$ 样本处仍未稳住的机制）。
换句话说，退化后的判断会说「样本不够」，正确的判断是「这个 sampler 与 $P$ 的失配在 $N$ 维下不可修」。

**落点**：式 (29.25)–(29.28) 在 p363–364；图 29.6a 的实证见 p362–363；
Exercise 6.14（p.124）给出 $\rho^2$ 的高斯集中这一上游事实。前置是 $\chi^2$ 型集中（$N$ 个独立 $x_i^2$ 求和），
可用中心极限定理推，属 6.042J 概率内容，不越级。
</span>



这套做法为什么能生成 $P(x)$ 的样本？

被提议的点 $(x, u)$ 是以均匀概率落在曲线 $cQ^*(x)$ 下方的浅阴影区里的（图 29.8b）。拒绝规则会拒掉所有落在曲线 $P^*(x)$ 上方的点。于是被接受的这些点 $(x, u)$，均匀分布在 $P^*(x)$ 下方的深阴影区里。

这就意味着被接受点的 $x$ 坐标的概率密度必定正比于 $P^*(x)$，所以这些样本必定是 $P(x)$ 的独立样本。

若 $Q$ 是 $P$ 的好近似，rejection sampling 效果最好。如果 $Q$ 与 $P$ 差得很远，那么为了让 $cQ$ 处处超过 $P$，$c$ 必然要取得很大，拒绝的频率也就很高。

[Figure 29.9：一个 Gaussian $P(x)$ 与一个稍宽的 Gaussian $Q(x)$，后者被乘以因子 $c$ 使 $cQ(x) \ge P(x)$。图中可见 $cQ$ 的峰比 $P$ 高出一截，这一截就是「被浪费掉的抽样量」；曲线无法复原，但「$Q$ 略宽于 $P$、故只需很小的 $c$」这个关系可以读出来。]

### 高维下的 rejection sampling · Rejection sampling in many dimensions

在高维问题里，很可能出现这种情况：要求 $cQ^*$ 成为 $P^*$ 的上界，会迫使 $c$ 大到接受变得极其罕见。而且找出这样的 $c$ 值本身也可能很难，因为在很多问题里，我们既不知道 $P^*$ 的峰在哪里，也不知道它们有多高。

作为一个案例，考虑一对均值为零的 $N$ 维 Gaussian 分布（图 29.9）。设想从一个标准差为 $\sigma_Q$ 的分布抽样本，并用 rejection sampling 去得到另一个标准差为 $\sigma_P$ 的分布的样本。

设这两个标准差的值彼此接近——比如说 $\sigma_Q$ 比 $\sigma_P$ 大 $1\%$。〔$\sigma_Q$ 必须大于 $\sigma_P$，否则不存在使 $cQ$ 对所有 $x$ 都超过 $P$ 的 $c$。〕

那么，如果维数是 $N = 1000$，需要多大的 $c$？

$Q(x)$ 在原点的密度是 $1/(2\pi\sigma_Q^2)^{N/2}$，所以要让 $cQ$ 超过 $P$，必须取

```math
c = \frac{(2\pi\sigma_Q^2)^{N/2}}{(2\pi\sigma_P^2)^{N/2}} = \exp\left(N\ln\frac{\sigma_Q}{\sigma_P}\right). \qquad (29.30)
```

取 $N = 1000$ 与 $\sigma_Q/\sigma_P = 1.01$，得到 $c = \exp(10) \simeq 20{,}000$。

对这个 $c$，接受率会是多少？答案立刻可得：由于接受率是曲线 $P(x)$ 下方的体积与 $cQ(x)$ 下方体积之比，而这里 $P$ 与 $Q$ 都是归一化的，所以接受率就是 $1/c$，例如 $1/20{,}000$。

一般地，$c$ 随维数 $N$ 指数增长，所以接受率预期随 $N$ 指数变小。

因此，rejection sampling 虽是一维问题的有用方法，却不被指望成为从高维分布 $P(x)$ 生成样本的实用技术。

## 29.4 Metropolis–Hastings 方法 · The Metropolis–Hastings method

只有当 proposal density $Q(x)$ 与 $P(x)$ 相似时，importance sampling 与 rejection sampling 才好用。在又大又复杂的问题里，很难造出一个具备这种性质的单一密度 $Q(x)$。

[Figure 29.10：一维的 Metropolis–Hastings 方法。proposal distribution $Q(x'; x)$ 在这里画成形状随 $x$ 而变（对两个不同状态 $x^{(1)}$、$x^{(2)}$ 各画一条），不过实际用到的 proposal density 通常不是这样的——固定形状（如以当前点为中心的 Gaussian）才是常态。]

Metropolis–Hastings 算法改用**依赖当前状态** $x^{(t)}$ 的 proposal density $Q$。密度 $Q(x'; x^{(t)})$ 可以是个简单分布，比如说以当前 $x^{(t)}$ 为中心的 Gaussian。

proposal density $Q(x'; x)$ 可以是任何固定的、我们能从中抽样的密度。与 importance sampling、rejection sampling 不同，**并不要求** $Q(x'; x^{(t)})$ 看上去与 $P(x)$ 有任何相似之处，算法才能实际有用。

图 29.10 给出了一个 proposal density 的例子；该图画出两个不同状态 $x^{(1)}$ 与 $x^{(2)}$ 下的密度 $Q(x'; x^{(t)})$。

与之前一样，我们假设对任意 $x$ 都能算出 $P^*(x)$。先由 proposal density $Q(x'; x^{(t)})$ 生成一个试探性的新状态 $x'$。

<span style="color:#1e8449;">**[译注]**
式 (29.30) 把「rejection sampling 在高维无法使用」变成了一个可以**当场手算的反驳**，而不是一句经验之谈。

推一遍：两个 Gaussian 都归一化，比值 $c$ 只需补偿「原点处密度之比」，于是
$c = (\sigma_Q/\sigma_P)^{N}$（$2\pi$ 与平方项相消），取对数得 $c = \exp(N\ln(\sigma_Q/\sigma_P))$。
$N = 1000$、$\sigma_Q/\sigma_P = 1.01$ 时 $N\ln 1.01 = 1000 \times 0.00995 = 9.95$，$e^{9.95} = 2.08\times10^{4}$。

**关键的一步是接受率 $= 1/c$**：因为 $\int cQ = c \ge \int P = 1$，被拒绝的体积占 $(c-1)/c$，接受占 $1/c$。

**消失测试**：把「接受率 $= 1/c$」这一步抽掉，你会得到「$Q$ 只宽 $1\%$，所以接受率大概 $99\%$」这种**方向完全相反**的估计——
真实接受率是 $1/20{,}000$。可观测后果：一个在 $N = 1000$ 上跑的 rejection sampler，跑 $10^{6}$ 步只得到约 50 个样本，
而且这 50 个还高度相关；代码不会报错，只是慢到你以为程序卡住了。更狠的一点：把 $\sigma_Q/\sigma_P$ 从 $1.01$ 改成 $1.001$ 只让 $c$ 降到 $\exp(1) \approx 2.7$，
说明这个指数对 1% 这个数字极其敏感——**参数精度在这里是致命的**。

**落点**：式 (29.30) 在本页；归一化 Gaussian 的密度见第 23 章 §23.1（式 23.6 附近）；
$\int cQ = c$ 这一步只用归一化定义。Exercise 29.2（p.363）与本页构成一对「$Q$ 失配的两种后果」。
</span>



为了决定是否接受新状态，我们计算

```math
a = \frac{P^*(x')}{P^*(x^{(t)})}\cdot\frac{Q(x^{(t)}; x')}{Q(x'; x^{(t)})}. \qquad (29.31)
```

若 $a \ge 1$，则接受新状态。否则，以概率 $a$ 接受新状态。若这一步被接受，就令 $x^{(t+1)} = x'$；若被拒绝，则令 $x^{(t+1)} = x^{(t)}$。

注意这与 rejection sampling 的差别：在 rejection sampling 里，被拒的点直接丢掉，对收集到的样本列表 $\{x^{(r)}\}$ 毫无影响；**而这里，一次拒绝会把当前状态再写一遍到列表上。**

### 记号 · Notation

我一直用上标 $r = 1, \ldots, R$ 标记「从分布中抽出的独立样本」，用上标 $t = 1, \ldots, T$ 标记「Markov chain 里的状态序列」。重要的一点是：**一次 $T$ 次迭代的 Metropolis–Hastings 模拟，并不产生 $T$ 个来自 target distribution $P$ 的独立样本。这些样本是相关的。**

为了算接受概率 (29.31)，我们需要能算出概率比 $P(x')/P(x^{(t)})$ 与 $Q(x^{(t)}; x')/Q(x'; x^{(t)})$。

如果 proposal density 是个简单的对称密度（比如以当前点为中心的 Gaussian），那么后一个因子为 1，Metropolis–Hastings 方法就退化为比较两个点上 target density 的取值。这个特例有时被称为 Metropolis 方法。

不过，为了向 Hastings 致歉，我把一般的不对称 $Q$ 的 Metropolis–Hastings 算法也叫「Metropolis 方法」——因为我认为重要的想法配得上短名字。

### Metropolis 方法收敛到 target density

可以证明：对任何正的 $Q$（即任何满足「对所有 $x, x'$ 有 $Q(x'; x) \gt 0$」的 $Q$），当 $t \to \infty$ 时 $x^{(t)}$ 的概率分布趋于 $P(x) = P^*(x)/Z$。

〔这句话不应被理解为「$Q$ 必须给每个点 $x'$ 都分配正概率」——后面我们会讨论一些例子，其中对某些 $x, x'$ 有 $Q(x'; x) = 0$；同时也请注意，我们完全没说收敛到 $P(x)$ 有多快。〕

Metropolis 方法是 Markov chain Monte Carlo（简称 MCMC）方法的一个例子。

与 rejection sampling 不同——那里被接受的点 $\{x^{(r)}\}$ 就是所要分布的独立样本——Markov chain Monte Carlo 方法涉及一个 Markov 过程，生成一串状态 $\{x^{(t)}\}$，其中每个样本 $x^{(t)}$ 的概率分布依赖前一个值 $x^{(t-1)}$。

由于相邻样本是相关的，Markov chain 可能得跑相当长的时间，才能生成实际上是 $P$ 的独立样本的那些样本。

正如 importance sampling 的 estimator 方差难以估计一样，要判断一个 Markov chain Monte Carlo 方法是否「收敛」、要量化「得等多久才能拿到实际上是 $P$ 的独立样本」，同样困难。

### Metropolis 方法的演示 · Demonstration of the Metropolis method

Metropolis 方法被广泛用于高维问题。许多 Metropolis 方法的实现都采用一个 proposal distribution，

<span style="color:#1e8449;">**[译注]**
式 (29.31) 那第二个因子（proposal 比的**反向**）是整章最容易写反的地方，而写反之后程序不报错、结果只偏一点点——于是最难查。

它存在的理由是 detailed balance。要求链的平稳分布是 $P$，只需对任意 $x, x'$ 满足
$P(x)T(x';x) = P(x')T(x;x')$。取 $T(x';x) = Q(x';x)a(x,x')$，代入后要消掉 $Q$ 的方向差异，
$a$ 就必须带上 $Q(x;x')/Q(x';x)$ 这个**反向比值**。$Q$ 对称时它等于 1，这就是本页说的「退化成 Metropolis」；
$Q$ 不对称（比如 p367 讲的带漂移的 proposal）时它不能省。

**消失测试**：把反向比值当成 1（即误用对称公式处理非对称 $Q$），detailed balance 立刻破缺，
链仍会收敛，但收敛到的是 $P(x)Q(x';x)/\text{归一化}$ 那类**扭曲分布**而不是 $P$——
可观测后果是：用 $\mathrm{Normal}(x'{-}x; \mu_{\text{drift}}, \sigma)$ 这种有偏 proposal 采样一个已知 Gaussian，
样本均值会偏 $\mu_{\text{drift}}\cdot$（某个与 $\sigma$ 有关的因子），偏差不随迭代数消失。这类 bug 在看 trace plot 时毫无症状。

**落点**：式 (29.31) 在本页；对称特例与「Metropolis 方法」命名见本页下一段；
detailed balance 的完整论证见第 30 章（p369 之后）或 Gilks et al. (1996)。前置只需条件概率的乘法定理，不越级。
</span>



其长度尺度 $\epsilon$ 相对于 probable region（高概率区域）中最长的长度尺度 $L$ 是短的（图 29.11）。

选小长度尺度的理由是：对大多数高维问题，从一个典型点（也就是 $P(x)$ 的一个样本）迈出一大步，极可能落到一个概率极低的状态；这种步子不太会被接受。

如果 $\epsilon$ 很大，那么只有在「跳到低概率状态竟然被接受」或者「一大步恰好落进另一个高概率状态」时，状态空间里的移动才会发生。所以用大步子的话，进展速度会很慢。

反过来，小步子的缺点是：Metropolis 方法会以 random walk（随机游走）的方式探索概率分布，而随机游走要走到任何地方都得很久，尤其当步子小的时候。

[Figure 29.11：二维情形下的 Metropolis 方法，画出一个传统的 proposal density，其步长 $\epsilon$ 足够小，使接受频率约为 $0.5$。图中 $L$ 标出 probable region 的最长长度尺度，$\epsilon$ 标出单步长度，$L$ 明显远大于 $\epsilon$。]

[exercise] **Exercise 29.3.**[1] Consider a one-dimensional random walk, on each step of which the state moves randomly to the left or to the right with equal probability. Show that after $T$ steps of size $\epsilon$, the state is likely to have moved only a distance about $\sqrt{T}\,\epsilon$. (Compute the root mean square distance travelled.)

> **中文话题摘要**：一维对称随机游走，每步长 $\epsilon$、左右各半，证明走 $T$ 步之后净位移的均方根只有约 $\sqrt{T}\epsilon$——这就是「随机游走要覆盖长度 $L$ 就得 $\sim (L/\epsilon)^{2}$ 步」的全部依据。

回想一下，Monte Carlo 抽样的首要目标是生成若干个（比如说十来个）来自给定分布的独立样本。

如果状态空间的最大长度尺度是 $L$，那么我们必须把一个随机游走式的 Metropolis 方法模拟

```math
T \simeq (L/\epsilon)^{2}
```

那么久，才能指望得到一个大致与初始条件无关的样本——而且这还是假设每一步都被接受：如果平均只有比例 $f$ 的步被接受，那么这个时间还要乘上因子 $1/f$。

<span style="color:#1f618d;">**[经验法则 Rule of thumb：Metropolis 方法迭代次数的下界]** 若 probable states 空间的最大长度尺度是 $L$，则一个 proposal distribution 的步长为 $\epsilon$ 的随机游走 Metropolis 方法，至少要跑

```math
T \simeq (L/\epsilon)^{2} \qquad (29.32)
```

次迭代，才能得到一个独立样本。</span>

这条经验法则只给出下界；实际情况可能糟得多——比如说，如果概率分布由若干个被低概率区域隔开的高概率「岛屿」组成。

<span style="color:#1e8449;">**[译注]**
式 (29.32) 是进入第 30–31 章（Gibbs sampling、slice sampling、Hamiltonian Monte Carlo）的**唯一入口**，因为那些方法全部在做同一件事：降低这个二次增长的时间代价。

推导只需两行：由 Exercise 29.3，$T$ 步之后净位移的均方根是 $\sqrt{T}\epsilon$；要它达到 $L$，就得 $T \simeq (L/\epsilon)^{2}$。
代入数：$L/\epsilon = 100$ 给出 $T = 10^{4}$，若接受率 $f = 0.5$ 则要 $2\times 10^{4}$ 次迭代才换一个独立样本。
更要紧的是维数：$N$ 维里总位移要走遍各方向，$L$ 是每维尺度，于是「走遍」要 $N \times (L/\epsilon)^{2}$ 量级，
**同时**为了让接受率不掉，$\epsilon$ 必须随 $N$ 变小（p367 上一段），两项合起来就是 MCMC 著名的「随机游走病」。

**消失测试**：抽掉 (29.32)，你会以为「多跑几步总能收敛」，于是把迭代数从 $10^{4}$ 提到 $10^{6}$ 试图解决高维采样；
而它说的是每多要一个独立样本，就要**再付** $(L/\epsilon)^{2}$ 次迭代，且 $\epsilon$ 还得随维数缩小——
可观测后果是：$N = 1000$ 的 Gaussian 目标下，一个各向同性随机游走 Metropolis 的实际效率比理想独立抽样低好几个数量级，
而这正是第 30 章之后所有「梯度辅助」方法要抢回来的东西。

**落点**：式 (29.32) 在本页；Exercise 29.3 给出 $\sqrt{T}\epsilon$ 的上游事实；$1/f$ 修正与「岛屿」警告见本页末两段；
随机游走病的正式处理见第 30 章与 Neal (1993b)。前置是随机游走的均方根位移（6.042J 期望与方差线性性），不越级。
</span>



[Figure 29.12：一个玩具问题上的 Metropolis 方法。(a) $t = 1, \ldots, 600$ 的状态序列：横向是状态（$0$ 到 $20$），纵向是时间（$1$ 到 $600$），横杠标出每 $50$ 个时间单位的间隔。(b) 迭代 $100$、$400$、$1200$ 次之后各状态的占据直方图。(c) 作为对照，当相继的点是从 target distribution **独立**抽出时得到的直方图。

**可复原性说明**：直方图的纵轴刻度与每根柱的具体高度在文字层里完全不存在（PyMuPDF 只抽出数字刻度 $0, 2, 4, \ldots, 12$ 与 $0, 5, \ldots, 90$ 这些轴标），柱高无法复原，因此这里不编造任何数值。可确证的结构只有三件事：① (b) 的三个面板对应迭代数 $100$ / $400$ / $1200$，横轴状态数相同（$0$ 到 $20$）；② (c) 的三个面板与 (b) 一一对应，但由独立抽样生成；③ (a) 的状态序列在时间上明显成块（相邻时刻状态强相关），这是「链的样本不独立」的直接图像。]

<span style="color:#1e8449;">**[译注]**
图 29.12 是本章唯一一处**用图像而不是公式**论证「MCMC 的样本不是样本」的地方，它要你盯住的是 (b) 与 (c) 在同样迭代数下的差别。

(c) 的每个点都是从 $P$ 独立抽的，因此直方图的起伏纯粹是多项分布的抽样噪声，其标准差为 $\sqrt{n_i(1-n_i/R)}$ 量级；
(b) 的点是链产生的，相邻点高度相关，(a) 里的「成块」正是自相关函数 $\rho(k)$ 衰减慢的直接后果。
于是同样的 $R$ 之下，(b) 的有效样本量 $R_{\mathrm{eff}} = R/(1 + 2\sum_k \rho(k))$ 远小于 $R$，直方图更「块状」、更迟才趋于平稳形状。

**消失测试**：把 (a) 与 (b)(c) 的对照去掉，只留一段「MCMC 样本相关」的文字，读者无法意识到后果有多具体：
$R = 1200$ 次迭代可能只等于几十个独立样本，于是任何从链上算出来的方差、误差棒、置信区间**都会低估一个量级**，
而且低估程度随 $\rho(k)$ 的衰减速度变化，无法用一个固定修正因子补救。图 (c) 的存在正是为了让这个低估变得可见。

**落点**：图 29.12 在本页（数值不可复原，已在图注中如实说明）；自相关与有效样本量的公式见第 29 章之后的第 30 章讨论；
$(L/\epsilon)^{2}$ 的定量来源见 p367 的 (29.32)。前置只需「方差的可加性 + 协方差」，6.042J 概率内容，不越级。
</span>

---

## 可复算验证（重建内容逐条核对）

本块所有重建的数值，都可以用下面几行算式独立验证（Python 或手算均可）：

```python
import math
lg2 = math.log10(2)
print(2**1000 == 10**(1000*lg2))            # 1.07e301，书里写 2^1000
print(10**(266*lg2), 10**80)                # 电子数 ≈ 1.2e80
print(266+40+58)                            # 2^364
print(636*lg2)                              # 191.4  → 书里写 10^190（†）
print(500*lg2)                              # 150.5  → 书里写 10^150 ✓
print(math.exp(math.sqrt(2000)), 10**(math.sqrt(2000)/math.log(10)))   # 1.9e19 → 书里写 10^19 ✓
print(math.exp(1000*math.log(1.01)))        # 20837 → 书里写 20,000 ✓
print(1/20837)                              # 接受率 4.8e-5 = 1/c ✓
print(20*2*2*16)                            # 1280 → 式(28.14) 书里写 ≃1000（†）
print(1/((1/20)*(10/20)*(10/20)*(1/16)))    # 1280，与上式一致 ✓
print(30/214, 6/112)                        # 14.0% 与 5.36% → 书里 14% / 6%（†）
print(19/160, 17/166)                       # 11.9% 与 10.2%（Simpson 悖论方向核对）✓
print(151/160, 63/166)                      # 0.944 与 0.380（悖论成因）✓
print((50)**1000 == 10**(1000*math.log10(50)))   # 1e1699
```

## 原文自身问题（`†`）

1. **† p359**：$2^{636} \simeq 10^{190}$。正确值是 $2^{636} = 10^{191.45}$，数量级差 1。不影响「不可行」这一结论，但读者若拿 $10^{190}$ 去与 $10^{80}$（电子数）比较，会少算一个因子 $10^{1.5}$。
2. **† p351 式 (28.12)**：正文说 $H_2$ 的九个参数里「六个被数据定死、三个被部分约束」，而 (28.12) 的记账口径是「每箱 2 个满额 $1/20$、1 个半额 $10/20$、1 个颜色 $1/16$，再加二值变量因子 $2/2$」，共 8 个参数 + 1 个二值变量。两套数法不能逐项对上，但结果同量级。
3. **† p351 式 (28.14)**：$20 \times 2 \times 2 \times 16 = 1280$，作者写 $\simeq 1000/1$。这是量级陈述，宜按 $1280:1$ 复算。
4. **† p355 第一段**：受害者是黑人时作者写「$6\%$ 的被告被判死刑」，按表格复算是 $6/112 = 5.36\%$（$14\%$ 那个数则精确：$30/214 = 14.02\%$）。

**补充说明（不是原文错误，但极易误读）**：p365 式 (29.30) 之前那句「$\sigma_Q$ 必须大于 $\sigma_P$」的括号解释里，作者从 $Q$ 跳到 $Q^*$（未归一化密度）。在 $N$ 维下这句话应理解为「不存在**有限的** $c$ 使 $cQ^* \gt P^*$ 处处成立」。这不是笔误，而是同一段里归一化量与未归一化量混用的书写习惯——本译文在 math 块里统一写成 $Q^*$ 形式，与该段口径一致。

## 术语表（15 条，按首现顺序）

| # | English | 中文（首现处给括号注） | 首现页 |
|---|---|---|---|
| 1 | Occam factor | 奥卡姆因子（证据里那个小于 1 的罚分项；本译按约定不译该词） | p349 |
| 2 | evidence / marginal likelihood | 证据（把参数积分掉后数据的概率） | p349 |
| 3 | hypothesis space | 假设空间（参数可取值的整个范围） | p349 |
| 4 | posterior accessible volume | 后验可达体积（数据到达后仍可能的那部分参数体积） | p349 |
| 5 | Hessian $A$ | 海森矩阵（$-\nabla\nabla\ln P$，其逆即协方差） | p350 |
| 6 | minimum description length (MDL) | 最小描述长度 | p352 |
| 7 | bits-back encoding | 比特回吐编码（把参数块里的随机比特回收抵扣） | p353 |
| 8 | cross-validation / leave-one-out | 交叉验证 / 留一法 | p353 |
| 9 | improper prior / proper prior | 不可归一化先验 / 可归一化先验 | p353 |
| 10 | Simpson's paradox | 辛普森悖论（分层与合并的方向相反） | p355 |
| 11 | graphical model | 图模型（节点是变量、边是依赖） | p355 |
| 12 | Monte Carlo method / MCMC | 蒙特卡洛方法 / 马尔可夫链蒙特卡洛 | p357 |
| 13 | target density / sampler density / proposal density | 目标密度 / 抽样密度 / 提议密度（后两者常混用） | p357 / p362 |
| 14 | typical set | 典型集（概率质量集中的那个小区域） | p360 |
| 15 | importance / rejection sampling · Metropolis–Hastings · acceptance rate · random walk | 重要性抽样 / 拒绝抽样 · Metropolis–Hastings · 接受率 · 随机游走（后四者按约定保留英文） | p361 / p364 / p365 / p367 |

**本块按约定一律保留英文原词的术语**（不译）：trellis、Viterbi、forward-backward、HMM、state、transition matrix、marginalization、Occam factor、likelihood、evidence、prior、posterior、Gaussian、Ising model、Dirichlet、Laplace's method、Metropolis–Hastings、Gibbs sampling、slice sampling、Markov chain Monte Carlo、proposal density、sampler density、acceptance rate、random walk、bits-back、latent variable model。

## 交付自检

- 页标记 20 个（p349 … p368），与 PDF 20 页一一对应（书内页码 = PDF 页码 − 12）。
- 禁用记号全部为 0：dollar 号双写、反斜杠＋方括号、反斜杠 mbox、反斜杠 tag、反斜杠 middle。
- 控制字符（TAB / FF / VT / BS / NUL）计数 0；抽取阶段已清除 PyMuPDF 从矢量图缝隙带出的 10 页控制字符。
- 自写内容一律绿色 `[译注]` 标记，没有使用 remark 标记；`[exercise]` 题干保留英文原文并附中文话题摘要。
- 矩阵 / 对齐：本块仅 (28.18)、(28.19)、(29.23) 三处需要 aligned 与 cases 环境，均用 write 工具落盘，双反斜杠未经过 heredoc。



## §29.4 Metropolis–Hastings 方法 · The Metropolis–Hastings method（节尾）

页眉：`29.4: The Metropolis–Hastings method` · 书内 p369

上接 p368 的经验法则 (29.32)。为了说明一个 random walk（随机游走）探索 state space 究竟有多慢，图 29.12 给出了一个 Metropolis 算法的模拟，用来从下面这个分布里产生样本：

```math
P(x)=\begin{cases} 1/21 & x\in\{0,1,2,\dots,20\},\\ 0 & \text{otherwise}. \end{cases} \qquad (29.33)
```

那个 proposal distribution（提议分布）是

```math
Q(x';x)=\begin{cases} 1/2 & x'=x\pm 1,\\ 0 & \text{otherwise}. \end{cases} \qquad (29.34)
```

因为 target distribution（目标分布）$P(x)$ 是均匀的，所以只有当 proposal 把状态带到 $x' = -1$ 或 $x' = 21$ 时才会出现 rejection（拒绝）。

模拟从状态 $x_0 = 10$ 出发，演化过程画在图 29.12a 里。

那么，要走多久才能到达两个端点状态 $x = 0$ 与 $x = 20$ 之一？

两者距离是 10 步，于是经验法则 (29.32) 预测：典型情况下需要 $T \simeq 100$ 次迭代才能到达某个端点状态。

本例证实了这一点：第一次踏进端点状态发生在**第 178 次**迭代。

那么，要走多久才能把两个端点状态都访问一遍？

经验法则预测：走遍整个 state space 大约需要 400 次迭代；而事实上，第一次遇到另一个端点状态发生在**第 540 次**迭代。

于是，所谓「实际上独立的（effectively-independent）」样本，是要**每四百次左右的迭代才换得一个**。

这个简单的例子说明：在 Monte Carlo 方法里，努力去**废除随机游走行为**是件要紧的事。

对那个玩具 state space $\{0,1,2,\dots,20\}$ 做一次系统性的探索，用同样的步长，大约二十步就能走完——而不是四百步。

减少随机游走行为的方法在下一章讨论。

<span style="color:#1e8449;">**[译注]**
$100$ 对 $178$、$400$ 对 $540$：这两对数字不是「作者算错了」，而是**在示范一个下界的正确用法**——(29.32) 给的是 $T \simeq (L/\epsilon)^2$ 这个**量级**，不是 $T$ 的估计值。$L = 10$、$\epsilon = 1$ 给出 $10^2$；实测 $178$ 与 $540$ 分别是 $1.8\times10^2$ 与 $5.4\times10^2$，**同一个数量级，没有被推翻**。

数量级上还能再对一次：一端到另一端的首达时间期望，对这段区间上的简单随机游走是 $\mathbb{E}[\tau] \simeq L^2 = 100$（从 $x=10$ 到 $\{0,20\}$ 的首次命中），而要走遍两端等于连续命中两个相距 20 的点，量级 $20^2/2 = 200$ 到 $400$。所以 $400$ 这个数是从 $L_{\text{full}} = 20$ 而非 $L = 10$ 得来的——作者在同一段里对「到达一端」和「访问两端」用了**两个不同的 $L$**，这一点原文没有明说。

**消失测试**：抽掉这段数值对照，只留公式 (29.32)，读者会把经验法则当成「迭代 $100$ 次就好了」的处方。可观测后果是：把一条 $N=20$ 的玩具链跑 $100$ 步就宣称收敛，而真实首达时间落在 $10^2$ 到 $10^3$ 之间，**误差是 2 到 5 倍**；在 $N = 10^4$ 维的真实问题上这个倍数会放大成「跑完以为收敛、其实只在初始点附近打转」。

**落点**：本页；(29.32) 在 p368；$178$ / $540$ 这两个数在图 29.12a 上可直接数出（第 178 个时刻首次触及 $x=0$，第 540 个时刻首次触及 $x=20$）。上游是简单随机游走的首达时间 $O(L^2)$（6.042J 期望线性性 + 6.006 的 BFS 距离概念），不越级。
</span>

### 高维中的 Metropolis 方法 · Metropolis method in high dimensions

给出随机游走 Metropolis 方法迭代次数**下界**的经验法则 (29.32)，同样适用于高维问题。

考虑一个简单情形：target distribution 是 $N$ 维 Gaussian（高斯），proposal distribution 是每个方向上标准差都为 $\epsilon$ 的球状 Gaussian（spherical Gaussian）。

不失一般性，可以假定 target distribution 是一个与各坐标轴 $\{x_n\}$ 对齐的 separable distribution（可分离分布），且在第 $n$ 个方向上标准差为 $\sigma_n$。

令 $\sigma_{\max}$ 与 $\sigma_{\min}$ 是这些标准差中最大与最小的两个。

再假定 $\epsilon$ 被调整到使 acceptance frequency（接受频率）接近 1。

在这个假定下，每个变量 $x_n$ 都独立于其它所有变量演化，各自执行一个步长约为 $\epsilon$ 的随机游走。

于是，产生「实际独立」样本所需的时间将由**最大的那个长度尺度 $\sigma_{\max}$** 控制。

正像上一节里需要至少 $T \simeq (L/\epsilon)^2$ 次迭代才得到一个独立样本一样，这里需要

```math
T \simeq (\sigma_{\max}/\epsilon)^{2}.
```

现在的问题是：$\epsilon$ 能取多大？

$\epsilon$ 越大，这个 $T$ 越小；但若 $\epsilon$ 太大——大到超过 $\sigma_{\min}$——acceptance rate（接受率）就会急剧下降。

看起来合理的是：最优的 $\epsilon$ 应当与 $\sigma_{\min}$ 同量级。

严格说来这未必成立；在特殊情形下，如果第二小的 $\sigma_n$ 明显大于 $\sigma_{\min}$，那么最优的 $\epsilon$ 可能更接近那个第二小的 $\sigma_n$。

但我们这个粗糙的结论是：**只要用的是简单的球状 proposal distribution，就至少需要 $T \simeq (\sigma_{\max}/\sigma_{\min})^2$ 次迭代才能得到一个独立样本**，其中 $\sigma_{\max}$ 与 $\sigma_{\min}$ 是 target distribution 最长与最短的长度尺度。

<span style="color:#1e8449;">**[译注]**
$(\sigma_{\max}/\sigma_{\min})^2$ 这个名字值得记住：它就是 target distribution 的**条件数（condition number）的平方**。设 $\Sigma$ 是目标的协方差，$\kappa = \lambda_{\max}/\lambda_{\min}$，则 $\sigma_{\max}/\sigma_{\min} = \sqrt{\kappa}$，于是 $T \simeq \kappa$ —— **迭代数的代价恰好等于协方差矩阵的条件数本身**，而不是它的平方。这个等式把采样难度与 Strang 线代里那个熟悉的量接上了：一个病态矩阵让迭代求解器慢多少倍，就让各向同性随机游走采样慢多少倍。

**消失测试**：抽掉这条判据，你在高维问题上唯一的调节手段就剩「盯 acceptance rate 到 0.5」——而这一页恰恰说明 $0.5$ 的接受率**可以和灾难性的慢同时存在**。可观测后果：目标是 $\sigma_{\max}/\sigma_{\min} = 100$ 的各向异性 Gaussian 时，你把 $\epsilon$ 调到 $\sigma_{\min}$ 附近、接受率 $0.5$，看着一切正常，而每换一个独立样本要 $10^4$ 次迭代；在 $N=1000$ 维里同一个超参还能让接受率掉到 $10^{-3}$ 以下，链根本不移动（这与 Exercise 29.18 的追问一致）。

**落点**：本页；Exercise 29.18（p383）把它做成定量题；Exercise 29.19（p384）把同一逻辑搬到 $\ln P^*$ 这个「能量维」上。上游是协方差与特征值（Strang 线代 §6.4 对称矩阵的对角化），下游是第 30 章 HMC 用梯度把 $\kappa$ 依赖压成 $\sqrt{\kappa}$。
</span>

---



[Figure 29.13：Gibbs sampling（吉布斯采样）。(a) 需要的联合密度 $P(x)$；(b) 从状态 $x^{(t)}$ 出发，$x_1$ 从条件密度 $P(x_1 \mid x_2^{(t)})$ 中抽样；(c) 接着从条件密度 $P(x_2 \mid x_1)$ 中抽一个样本；(d) 做几次 Gibbs 迭代后的样子。

**可复原性说明**：四个面板的等高线形状（(a) 是一个二维的椭圆状联合密度，(b)(c) 是沿坐标方向的切片）在文字层里只剩 `x1`、`x2`、`P(x)`、`P(x1 | x(t) 2 )`、`P(x2 | x1)`、`x(t)`、`x(t+1)`、`x(t+2)` 这十个标签，**曲线与箭头的位置、切片的宽度全部不可复原**，因此本译文不编造轮廓，只按图注与正文重建其逻辑结构：每一步只沿一根坐标轴移动。]

这既是好消息也是坏消息。

好消息是：与 rejection sampling（拒绝抽样）和 importance sampling（重要性抽样）的情形不同，这里**没有对维数 $N$ 的灾难性依赖**。

我们的计算机在比宇宙年龄更短的时间里就能给出有用的答案。

但坏消息依旧成立：这个对长度尺度之比的**二次依赖**，仍可能迫使我们做极长的模拟。

所幸，有一些方法可以压制 Monte Carlo 模拟里的随机游走，我们在下一章讨论它们。

## 29.5 Gibbs sampling（吉布斯采样）

我们引入 importance sampling、rejection sampling 与 Metropolis 方法时用的都是一维例子。

Gibbs sampling 也称为 heat bath method（热浴法）或「Glauber dynamics」，是一个用于从**至少两维**的分布里抽样的方法。

Gibbs sampling 可以看作一种 Metropolis 方法：其中一串 proposal distribution $Q$ 是**用联合分布 $P(x)$ 的条件分布来定义的**。

它假定：虽然 $P(x)$ 过于复杂、无法直接从中抽样，但它的 conditional distribution（条件分布）$P(x_i \mid \{x_j\}_{j\neq i})$ 是容易处理的。

对许多 graphical model（图模型，但并非所有）而言，这些一维条件分布可以直接抽样。

例如，若某些变量 $d$ 的 Gaussian 分布有一个未知均值 $m$，而 $m$ 的 prior distribution（先验分布）也是 Gaussian，那么给定 $d$ 之后 $m$ 的条件分布同样是 Gaussian。

那些不具备标准形式的条件分布，只要满足某些凸性（convexity）条件，仍然可以用 adaptive rejection sampling（自适应拒绝抽样）来抽样（Gilks and Wild, 1992）。

Gibbs sampling 用两个变量 $(x_1, x_2) = x$ 的情形画在图 29.13 里。

在每一次迭代中，我们从当前状态 $x^{(t)}$ 出发，把 $x_2$ 固定为 $x_2^{(t)}$，从条件密度 $P(x_1 \mid x_2)$ 中抽 $x_1$。

接着用 $x_1$ 的新值，从条件密度 $P(x_2 \mid x_1)$ 中抽 $x_2$——这一步落在下一页。

<span style="color:#1e8449;">**[译注]**
「Gibbs sampling 是一个每次都接受提议的 Metropolis 方法」这句话是全节的枢纽，值得当场验一遍，因为它决定了你后面所有关于收敛性的结论能不能借用 Metropolis 的理论。单变量更新时提议密度取 $Q(x';x) = P(x_i' \mid x_{-i})$，而目标的条件分布也是它，于是 Metropolis 的接受概率

```math
A(x' \mid x)=\min\left\{1,\ \frac{P(x')\,Q(x \mid x')}{P(x)\,Q(x' \mid x)}\right\}=\min\left\{1,\ \frac{P(x')\,P(x_i \mid x'_{-i})}{P(x)\,P(x_i' \mid x_{-i})}\right\}=1,
```

最后一步因为 $x'_{-i} = x_{-i}$（只改了一个坐标），两对条件密度约掉。**接受率恒为 1 是恒等式逼出来的，不是调参调出来的。**

**消失测试**：抽掉这个等价性，Exercise 29.4 就无从下手，更重要的是你失去了「Gibbs 的收敛性 = Metropolis 的收敛性」这一免费定理：一页之后 (29.35–29.37) 的块更新、以及 p374 上「Gibbs 是否满足 detailed balance」的追问，全都建立在「它就是 Metropolis 的一个特例」之上；没有它，你必须重新证一遍每条链的不变分布，而**这种重证极容易漏掉坐标更新顺序这个陷阱**（Exercise 29.9 正是问这个）。

**落点**：本页与下一页的 (29.35)–(29.37)；正式命题是 Exercise 29.4（p371）；「恒等接受率」的代价在 p371 的 syndrome decoding 反例里一次性暴露（Exercise 29.5）。上游只需条件概率的定义（6.042J 条件化 + 全概率），不越级。
</span>

---



接上页：这就把我们带到新状态 $x^{(t+1)}$，一次迭代到此完成。

在系统有 $K$ 个变量的一般情形下，**一次迭代要逐个参数地抽样**：

```math
\begin{aligned}
x_1^{(t+1)} &\sim P\bigl(x_1 \mid x_2^{(t)}, x_3^{(t)}, \dots, x_K^{(t)}\bigr) && (29.35)\\
x_2^{(t+1)} &\sim P\bigl(x_2 \mid x_1^{(t+1)}, x_3^{(t)}, \dots, x_K^{(t)}\bigr) && (29.36)\\
x_3^{(t+1)} &\sim P\bigl(x_3 \mid x_1^{(t+1)}, x_2^{(t+1)}, \dots, x_K^{(t)}\bigr),\ \text{etc.} && (29.37)
\end{aligned}
```

请注意上下标的不对称：**已经更新过的坐标用 $t+1$，尚未更新的仍用 $t$**。这个「就地更新（in place）」的顺序正是 Gibbs 与「同时更新」的区别所在。

### Gibbs sampling 收敛到目标密度 · Convergence of Gibbs sampling to the target density

<span style="color:#b9770e;">**[exercise 29.4]** `[2]` Show that a single variable-update of Gibbs sampling can be viewed as a Metropolis method with target density $P(x)$, and that this Metropolis method has the property that every proposal is always accepted.

**话题摘要**：把单坐标的 Gibbs 更新重写成 Metropolis 形式，并证明接受概率恒等于 1（本页译注给了两行推导）。</span>

正因为 Gibbs sampling 是一个 Metropolis 方法，所以只要 $P(x)$ 没有病态（pathological）性质，$x^{(t)}$ 的概率分布就会在 $t \to \infty$ 时趋向 $P(x)$。

<span style="color:#b9770e;">**[exercise 29.5]** `[2, p.385]` Discuss whether the syndrome decoding problem for a $(7,4)$ Hamming code can be solved using Gibbs sampling. The syndrome decoding problem, if we are to solve it with a Monte Carlo approach, is to draw samples from the posterior distribution of the noise vector $n = (n_1, \dots, n_n, \dots, n_N)$,

```math
P(n \mid f, z)=\frac{1}{Z}\prod_{n=1}^{N} f_n^{\,n_n}(1-f_n)^{(1-n_n)}\,\mathbb{1}[Hn = z], \qquad (29.38)
```

where $f_n$ is the normalized likelihood for the $n$th transmitted bit and $z$ is the observed syndrome. The factor $\mathbb{1}[Hn = z]$ is 1 if $n$ has the correct syndrome $z$ and 0 otherwise. What about the syndrome decoding problem for any linear error-correcting code?

**话题摘要**：为什么 syndrome decoding 的后验在 Gibbs 看来是病态分布——合法 codeword 稀疏且互不相邻，任何单比特翻转都落进零概率区，链一旦进入某个合法假设就再也出不来（答案在 p385）。</span>

### 高维中的 Gibbs sampling · Gibbs sampling in high dimensions

Gibbs sampling 有着与简单 Metropolis 算法**同样的缺陷**——除非碰巧选到了一个使概率分布 $P(x)$ 成为 separable 的参数化方式，否则 state space 是靠一个缓慢的随机游走来探索的。

比如说，若两个变量 $x_1$ 与 $x_2$ 强相关，其 marginal density（边缘密度）宽度为 $L$、条件密度宽度为 $\epsilon$，那么要产生一个独立样本，至少需要大约 $(L/\epsilon)^2$ 次迭代。

图 30.3（p390）演示了当 $L \gg \epsilon$ 时 Gibbs sampling 那缓慢的进展。

然而 Gibbs sampling **不涉及任何可调参数**，所以当你想让一个模型尽快跑起来时，它是个有吸引力的策略。

有一个极好的软件包 BUGS，可以让人轻松搭起几乎任意的概率模型并用 Gibbs sampling 来模拟（Thomas et al., 1992）。[^1]

[^1]: `http://www.mrc-bsu.cam.ac.uk/bugs/`

<span style="color:#1e8449;">**[译注]**
Exercise 29.5 是本章唯一一个**把你从「Gibbs 很好用」直接拽进「Gibbs 会死锁」**的地方，值得把死锁机制算清楚。$(7,4)$ Hamming 码有 $2^4 = 16$ 个 codeword，而噪声向量空间有 $2^7 = 128$ 个点，合法集只占 $16/128 = 1/8$。更要命的是**汉明距离**：任意两个不同 codeword 的最小距离是 $d = 3$，所以从任何合法 $n$ 出发翻转**任意一比特**，新向量与全部 16 个 codeword 都至少差 1 位，syndrome 不再为 $z$，指示函数 $\mathbb{1}[Hn = z]$ 变成 0，条件密度**根本没有定义**（分母为零）。

**消失测试**：如果 (29.38) 里没有那个硬约束因子 $\mathbb{1}[Hn=z]$（比如换成软的先验），条件分布处处有定义，Gibbs 能正常移动，问题就退化成普通的连续松弛——而正是这个「以概率 1 恰好落在超平面 $Hn = z$ 上」的约束，使链的支撑集只有 $2^K$ 个孤立点。可观测后果：任何针对 $(7,4)$ 码实现的 Gibbs 解码器，跑 $10^6$ 步后**状态一次都没变过**，你会把它误诊为「已收敛」。

**落点**：本页 (29.38)；完整答案在 p385（§29.12 Solutions）；同一死锁在通用线性码上依然成立（答案里作者自己说明了「no two codewords are adjacent」）；替代路线是 p385 末段提出的「拿原消息比特 $s$ 当变量」。上游是线性分组码的最小距离概念（MacKay §1.1–§1.2 已讲），不越级。
</span>

---



## 29.6 Markov chain Monte Carlo 方法的术语 · Terminology for Markov chain Monte Carlo methods

现在花一点篇幅勾画 Metropolis 方法与 Gibbs sampling 所依据的理论。

我们用 $p^{(t)}(x)$ 记一个 Markov chain（马尔可夫链）模拟器其状态的概率分布。（要把这个分布可视化，可以想象**同时并行运行无穷多个完全相同的模拟器**，看状态在它们之间的分布。）

我们的目标是要找一条 Markov chain，使得随着 $t \to \infty$，$p^{(t)}(x)$ 趋向我们想要的分布 $P(x)$。

一条 Markov chain 可以由一个初始概率分布 $p^{(0)}(x)$ 与一个 transition probability（转移概率）$T(x'; x)$ 完全指定。

Markov chain 在第 $(t+1)$ 次迭代时状态的概率分布 $p^{(t+1)}(x)$ 由下式给出：

```math
p^{(t+1)}(x')=\int \mathrm{d}^N x\; T(x';x)\,p^{(t)}(x). \qquad (29.39)
```

<span style="background:#eaf2f8;">**例 29.6（Example）**</span> Markov chain 的一个实例，就是 §29.4（图 29.12）那个 Metropolis 演示，其 transition probability 是

```math
T=\begin{bmatrix}
\tfrac12 & \tfrac12 & & & & \\
\tfrac12 & 0 & \tfrac12 & & & \\
 & \tfrac12 & 0 & \tfrac12 & & \\
 & & \ddots & \ddots & \ddots & \\
 & & & \tfrac12 & 0 & \tfrac12 \\
 & & & & \tfrac12 & \tfrac12
\end{bmatrix}
```

〔重建说明：原矩阵是 $21\times 21$，文字层里被抽成约 660 行竖排单列数字流；此处按首行首列与末行末列的实际元素重建示意形式，中间行用 $\ddots$ 折叠。核对方式见文件末尾「可复算验证」第 1 条。〕

而初始分布是

```math
p^{(0)}(x)=\begin{bmatrix} 0 & \cdots & 0 & 1 & 0 & \cdots & 0\end{bmatrix}^{\mathsf{T}}, \qquad (29.40)
```

那个 $1$ 落在第 $11$ 个分量（即 $x = 10$）上。

状态在第 $t$ 次迭代时的概率分布 $p^{(t)}(x)$，对 $t = 0, 1, 2, 3, 5, 10, 100, 200, 400$ 的情形画在图 29.14 里；另一组等价的分布序列画在图 29.15 里，那是从初始状态 $x_0 = 17$ 出发的链。

两条链都在 $t \to \infty$ 时收敛到 target density，也就是那个均匀分布。

[Figure 29.14：Example 29.6 那条 Markov chain 的状态概率分布，八个面板依次是 $p^{(0)}(x)$、$p^{(1)}(x)$、$p^{(2)}(x)$、$p^{(3)}(x)$、$p^{(10)}(x)$、$p^{(100)}(x)$、$p^{(200)}(x)$、$p^{(400)}(x)$，每个面板的横轴是状态 $0, 5, 10, 15, 20$。

**可复原性说明**：每根柱的高度文字层里完全没有，只有横轴刻度 $0/5/10/15/20$ 与标签 $p^{(t)}(x)$，**柱高不可复原**。可确证的只有结构：$p^{(0)}$ 是单点，随后逐次向相邻两格扩散（第 $t$ 步的支撑最多 $2t+1$ 个点），到 $t = 400$ 时已接近 $1/21 \approx 0.048$ 的平坦形。]

<span style="color:#1e8449;">**[译注]**
(29.39) 是整章的记号枢纽，值得把**行列表向**钉死，因为后面 (29.41) 的不变性、(29.46) 的 detailed balance、以及 Example 29.6 那个三对角矩阵全都靠它。$p^{(t+1)}(x') = \int \mathrm{d}^N x\, T(x';x)p^{(t)}(x)$ 里积分变量是**旧状态 $x$**，输出是**新状态 $x'$**，所以有限状态下 $T$ 的第 $x'$ 行、第 $x$ 列是 $T(x';x)$——**行随机（每行和为 1）而非列随机**。检查 Example 29.6 的首行：$T(0;0) = 1/2$（提议到 $-1$ 被拒，留在原地）、$T(0;1) = 1/2$，和为 1 ✓；末行 $T(20;19) = T(20;20) = 1/2$ ✓。

这一步为什么不能搞反：不变分布的条件是 $\pi(x') = \int \mathrm{d}^N x\, T(x';x)\pi(x)$，在矩阵语言里就是 $\pi = \pi T^{\mathsf T}$，即 $\pi$ 是 $T^{\mathsf T}$ 的**左**特征向量。若你把 $T$ 的行列写反，得到的将是「$T$ 的列和为 1」，此时不变分布是右特征向量、且通常**不再是均匀分布**。

**消失测试**：抽掉 (29.39)（也就是抽掉把链写成一个线性算子的能力），(29.41) 的「不变分布 = 特征值 1 的特征向量」、p373 的 reducible / periodic 判据、p374 的 detailed balance 全都无处落脚；更实际地，你无法**数值检验**一条自造 kernel 是否保留 $P$——只能靠反复跑链看直方图，而这在 $21$ 个状态上还行，在 $10^6$ 个状态上等于不可检验。可观测后果：转移矩阵方向写反的代码，跑出来的「稳态」是 $T$ 的平稳分布而不是 $P$，直方图看着平滑、完全不像出错。

**落点**：本页；(29.41) 与特征值说法在 p372 末段；Example 29.6 的矩阵核对见末尾「可复算验证」第 1 条。上游是矩阵乘法的行列约定（Strang 线代 §1.3–§1.4），不越级。
</span>

### 对链的要求 · Required properties

设计一个 Markov chain Monte Carlo 方法时，我们构造的链要满足下面这些性质：

**1. 想要的分布 $P(x)$ 是这条链的一个 invariant distribution（不变分布）。**

称分布 $\pi(x)$ 是 transition probability $T(x';x)$ 的一个不变分布，如果

```math
\pi(x')=\int \mathrm{d}^N x\; T(x';x)\,\pi(x). \qquad (29.41)
```

不变分布就是 transition probability **矩阵中特征值为 $1$ 的那个特征向量**。

---



**2. 链还必须是 ergodic（遍历的）**，也就是

```math
p^{(t)}(x)\to \pi(x)\quad \text{as } t\to\infty,\ \text{for any } p^{(0)}(x). \qquad (29.42)
```

一条链可能不满足遍历性，原因有这样两个：

**(a) 它的矩阵可能是 reducible（可约的）**，意思是 state space 里含有两个或多个互相**永远无法到达**的子集。

这样的链有很多个不变分布；$p^{(t)}(x)$ 随 $t \to \infty$ 趋向哪一个，将取决于初始条件 $p^{(0)}(x)$。

[Figure 29.15：从初始条件 $x_0 = 17$ 出发的 Markov chain 的状态概率分布（Example 29.6，p372）。八个面板与图 29.14 相同，只是起点换成了 $x_0 = 17$。

**可复原性说明**：与图 29.14 同源，柱高不可复原。可确证的结构是：$p^{(0)}$ 的单点落在状态 $17$，且由于 $17$ 到 $0$ 的距离（$17$ 步）大于到 $20$ 的距离（$3$ 步），分布会**先**向右侧端点扩张、再缓慢铺满全区间——这是与图 29.14 唯一的实质差异。]

这样的链的 transition probability 矩阵会有**多于一个**特征值等于 $1$。

**(b) 链可能含有一个 periodic set（周期集）**，意思是：对某些初始条件，$p^{(t)}(x)$ 并不趋向一个不变分布，而是趋向一个周期的 limit-cycle（极限环）。

具有这个性质的一个简单的 Markov chain，是 $N$ 维 hypercube（超立方体）上的随机游走。

这条链 $T$ 把状态从一个顶点带到随机选定的一个相邻顶点。

这条链唯一的不变分布，是全部 $2^N$ 个状态上的均匀分布；但这条链**不是遍历的**：它以 $2$ 为周期。

如果我们把状态分成奇宇称（odd parity）与偶宇称（even parity）两类，就会发现每个奇数状态都被偶数状态包围，反之亦然。

于是，若 $t = 0$ 时的初始条件是一个偶宇称状态，那么 $t = 1$ 时——以及所有奇数时刻——状态必定是奇宇称的；而在所有偶数时刻，状态将是偶宇称的。

这样的链的 transition probability 矩阵，会有**多于一个**模等于 $1$ 的特征值。

比如 hypercube 上的随机游走，其特征值就包含 $+1$ 与 $-1$。

<span style="color:#1e8449;">**[译注]**
「特征值 $1$ 的个数」是**可约性**的度量，「模为 $1$ 的特征值」是**周期性**的度量——这两个判据的差别不是修辞，而是两个不同的失效模式，必须分清。

Reducible：$T$ 分块上三角，第 $k$ 个对角块各有一个特征值 $1$，于是 $\lambda = 1$ 的重数是块数 $k$。$N$ 维 hypercube 的随机游走恰好是另一头：它的转移矩阵可对角化，特征值是 $\lambda_j = 1 - 2j/N$，$j = 0,\dots,N$，最大的是 $1$（$j=0$）、最小的是 $-1$（$j=N$）。**只有一个特征值模为 1 之外还有第二个 $-1$**，所以它不可约却非遍历。$N = 1$ 时就退化成一个两点互跳的链，$T = \begin{bmatrix}0 & 1\\ 1 & 0\end{bmatrix}$，特征值 $\pm1$，$p^{(t)}$ 精确地每步翻转，永不收敛。

**消失测试**：把「模为 1」这个限定去掉，只查「特征值是否等于 1」，hypercube 链会被判为合格（它确实只有一个 $+1$），你会以为它收敛到均匀分布。可观测后果：在 $N=3$、$2^3 = 8$ 个状态上跑 $10^4$ 步，偶数时刻永远落在 4 个偶宇称点、奇数时刻落在另外 4 个，无论跑多久**直方图都只覆盖一半状态**，而每半边的形状看起来完全像均匀分布；若你把奇偶两次采样混在一起统计，反而看不出任何异常，误差却恰好是 $\sqrt{2}$ 倍。

**落点**：本页两处判据（(a) reducible 与 (b) periodic）；特征值 $1 - 2j/N$ 的推导可在 hypercube 的邻接矩阵上验（每个顶点连 $N$ 个邻居，$T = A/N$）；Exercise 29.7（下页）用 detailed balance 给出不变性的充分证明路径。上游是特征值、可对角化（Strang 线代 §6.2），不越级。
</span>

### Markov chain 的构造方法 · Methods of construction of Markov chains

构造 $T$ 时，常常方便的做法是把若干简单的 base transition（基转移）$B$ **混合（mixing）**或**串接（concatenating）**起来，而这些 $B$ 全都满足

```math
P(x')=\int \mathrm{d}^N x\; B(x';x)\,P(x), \qquad (29.43)
```

也就是对想要的密度 $P(x)$ 而言，它们全都以 $P$ 为不变分布。

这些 base transition **不必各自都是遍历的**。

若我们随机挑一个 base transition 来做这一步、并让它决定转移，那 $T$ 就是若干个 base transition $B_b(x',x)$ 的**混合**：

```math
T(x',x)=\sum_b p_b\,B_b(x',x), \qquad (29.44)
```

其中 $\{p_b\}$ 是 base transition 上的一个概率分布。

若我们先用 $B_1$ 转移到某个中间状态 $x''$、再从 $x''$ 用 $B_2$ 转移到 $x'$，那 $T$ 就是两个 base transition $B_1(x',x)$ 与 $B_2(x',x)$ 的**串接**：

```math
T(x',x)=\int \mathrm{d}^N x''\; B_2(x',x'')\,B_1(x'',x). \qquad (29.45)
```

<span style="color:#1e8449;">**[译注]**
(29.43) 说「每个 $B$ 都保留 $P$」，(29.44) 与 (29.45) 说「保留 $P$ 这件事在混合与串接下都封闭」。这两条封闭性合起来，就是**所有实用 MCMC 算法可以「积木式」拼装**的许可证：Gibbs 是 $K$ 个单坐标 base transition 的串接，块更新（(29.47)）是把相邻几块合成一个 $B$，Metropolis-within-Gibbs 是混合，p380 提到的「$B$ 个 proposal 依次试」也是串接。

验证只需两行。混合：$\int \mathrm{d}x\sum_b p_bB_b(x';x)P(x) = \sum_b p_b P(x') = P(x')$ ✓。串接：$\int \mathrm{d}x''B_2(x';x'')\left[\int\mathrm{d}x B_1(x'';x)P(x)\right] = \int \mathrm{d}x''B_2(x';x'')P(x'') = P(x')$ ✓。**注意两步都只用到了「$B$ 保留 $P$」，没有用到 detailed balance**——这一点是下页那条注的伏笔：串接保持不变性，但不保持 detailed balance。

**消失测试**：抽掉 (29.44)/(29.45) 的封闭性，p374 的 detailed balance 讨论就变成一座孤岛：你无法解释为什么一个「单独的 $B$ 可逆、串起来就不可逆」的算法仍然是**正确的** MCMC（Exercise 29.8 正是这个反例），于是实践中看到串接 kernel 的转移计数不对称时，会误判为代码有 bug 而回退到更慢的单步 Metropolis。可观测后果：overrelaxation 与 slice sampling 的多步串接全部不敢用，采样效率退回 $(L/\epsilon)^2$ 的基线。

**落点**：本页 (29.43)–(29.45)；反例是 Exercise 29.8（p374）；实用拼装在 (29.47) 与 §30 的各个算法。上游是「矩阵乘法 + 条件期望的塔性质」（6.042J 全概率公式的连续版），不越级。
</span>

---



### Detailed balance（细致平衡）

许多有用的 transition probability 都满足 **detailed balance（细致平衡）**性质：

```math
T(x_a;x_b)\,P(x_b)=T(x_b;x_a)\,P(x_a),\quad \text{for all } x_b \text{ and } x_a. \qquad (29.46)
```

这个方程说的是：如果我们（借某种魔法）从 target density $P$ 里挑一个状态、并在 $T$ 下转移到另一个状态，那么「挑中 $x_b$ 并从 $x_b$ 走到 $x_a$」的概率，与「挑中 $x_a$ 并从 $x_a$ 走到 $x_b$」的概率**恰好一样大**。

满足 detailed balance 的 Markov chain 也称为 reversible Markov chain（可逆马尔可夫链）。

detailed balance 之所以值得关注，是因为**它蕴含 $P(x)$ 在链 $T$ 下的不变性**，而后者是我们想从 MCMC 模拟里得到的关键性质（链的概率分布应当收敛到 $P(x)$）的一个必要条件。

<span style="color:#b9770e;">**[exercise 29.7]** `[2]` Prove that detailed balance implies invariance of the distribution $P(x)$ under the Markov chain $T$.

**话题摘要**：把 (29.46) 两边对 $x_a$ 积分，左边给出 $P(x_b)$ 乘以「从 $x_b$ 出发的总流出 = 1」，右边给出 $P(x_b)$ 的右端——三行即可（本页译注给出）。</span>

在证明一个 Markov chain Monte Carlo 模拟会收敛到想要的分布时，**证明 detailed balance 成立**往往是关键的一步。

例如，Metropolis 方法就满足 detailed balance。

然而 detailed balance 并不是必要条件；我们后面会看到，不可逆的（irreversible）Markov chain 在实践中可以有用，因为它们可能具有不同的随机游走性质。

<span style="color:#b9770e;">**[exercise 29.8]** `[2]` Show that, if we concatenate two base transitions $B_1$ and $B_2$ that satisfy detailed balance, it is not necessarily the case that the $T$ thus defined (29.45) satisfies detailed balance.

**话题摘要**：可逆 + 可逆经串接**不必**可逆——(29.45) 的卷积只在「两个 $B$ 关于同一 $P$ 可逆」时保持不变性，可逆性本身丢失；这解释了为什么 slice sampling 的多步串接要另证。</span>

<span style="color:#b9770e;">**[exercise 29.9]** `[2]` Does Gibbs sampling, with several variables all updated in a deterministic sequence, satisfy detailed balance?

**话题摘要**：按固定顺序（$x_1, x_2, \dots, x_K$）逐坐标更新时，整轮 kernel 一般**不可逆**——反向轮的更新顺序必须是 $x_K, \dots, x_1$；只有两坐标时才碰巧可逆。这直接回应「Gibbs 是 Metropolis 所以可逆」的误推。</span>

<span style="color:#1e8449;">**[译注]**
Exercise 29.7 的三行证明值得背下来，因为它说明了 detailed balance 的**真实身份**：它是「逐点流量守恒」，比全局不变性（(29.41)）强、比它好证。

对 (29.46) 两边关于 $x_a$ 积分：

```math
\int \mathrm{d}x_a\, T(x_b;x_a)P(x_a)=\int \mathrm{d}x_a\, T(x_a;x_b)P(x_b)=P(x_b)\int \mathrm{d}x_a\,T(x_a;x_b)=P(x_b),
```

最后一步用了「链必须去某个地方」——$\int \mathrm{d}x_a\,T(x_a;x_b) = 1$（**行随机归一**，正是前一条译注钉死的那个方向）。左边就是 (29.41) 的右端，故 $P$ 不变。

反过来不成立：不变性只要求**净流量为零**，detailed balance 要求**每一对 $x_a \leftrightarrow x_b$ 的净流量各自为零**。前者的解空间严格更大——这正是 Trefethen 那类「非可逆链、特征值可以取复值，从而谱隙更大、混合更快」的 MCMC 变体（overrelaxation、lifted chains）存在的原因。

**消失测试**：只会用 (29.41) 而不知道 (29.46) 的人，在验证 Metropolis 的正确性时必须对全体 $x$ 积分（高维下不可行）；有了 (29.46)，只需逐对检查 $A(x'|x)Q(x';x) = A(x|x')Q(x|x')$，**这是一次逐点的、无需任何积分的核对**。抽掉它，Kitagawa 关于非可逆链更快的整套结果（以及 §30 的 overrelaxation）就失去了对话对象。

**落点**：本页 (29.46) 与紧接其后的说明；反例见 Exercise 29.8；Gibbs 的反例见 Exercise 29.9；「不可逆链在实践中可以有用」这句在本页倒数第二段，正式展开在第 30 章。上游是概率流的守恒（6.042J 全概率 + Strang 线代「转置即对偶」），不越级。
</span>

## 29.7 Slice sampling（切片采样）

Slice sampling（Neal, 1997a; Neal, 2003）是一种 Markov chain Monte Carlo 方法，它与 rejection sampling、Gibbs sampling 以及 Metropolis 方法都有相似之处。

凡是能用 Metropolis 方法的地方，就能用它——也就是，**只要目标密度 $P^*(x)$ 在任意点 $x$ 处可以被求值**。

与简单的 Metropolis 方法相比，它的优点是：对步长之类的参数选择**更稳健（robust）**。

Slice sampling 最简单的那一版与 Gibbs sampling 相似，也由 state space 里的一维转移构成；但并不要求一维条件分布容易抽样，也不要求它们具备 adaptive rejection sampling 所需的那种凸性。

Slice sampling 又与 rejection sampling 相似，因为它也是一种**渐近地从 $P^*(x)$ 所描述的曲线下方的体积里抽样**的方法；但并不需要存在一个上界函数（upper-bounding function）。

我先把一个一维抽样算法的骨架给出来，然后再给一个图示描述——图示里含有使方法成立的那些细节。

---



### Slice sampling 的骨架 · The skeleton of slice sampling

让我们假定要从 $P(x) \propto P^*(x)$ 中抽样，其中 $x$ 是实数。

一个一维 slice sampling 算法，是一种从「位于曲线 $P^*(x)$ 下方的一个二维点 $(x, u)$」转移到「位于同一曲线下方的另一个点 $(x', u')$」的方法，并且要求：无论从哪个初始点出发，$(x,u)$ 的概率分布都趋向曲线 $P^*(x)$ 下方**面积上的均匀分布**——正像 rejection sampling（§29.3）在曲线 $P^*(x)$ 下方产生的那个均匀分布一样。

一次一维 slice sampling 转移 $(x,u) \to (x',u')$ 包含下列步骤，其中第 3 步与第 8 步还需要进一步展开：

```
1: evaluate P*(x)
2: draw a vertical coordinate u' ~ Uniform(0, P*(x))
3: create a horizontal interval (xl, xr) enclosing x
4: loop {
5:     draw x' ~ Uniform(xl, xr)
6:     evaluate P*(x')
7:     if P*(x') > u' break out of loop 4-9
8:     else modify the interval (xl, xr)
9: }
```

创建区间 $(x_l, x_r)$（第 3 步）有若干种方法，修改它（第 8 步）也有若干种方法。

要紧的一点是：整个方法**必须满足 detailed balance**，这样 $(x,u)$ 在曲线 $P^*(x)$ 下方的均匀分布才是不变分布。

### 第 3 步的 'stepping out'（向外步进）方法

在 'stepping out' 方法里，为了构造一个包含 $x$ 的区间 $(x_l, x_r)$，我们以长度 $w$ 为步长向外走，直到找到端点 $x_l$ 与 $x_r$，在那里 $P^*$ 小于 $u$ 为止。

算法画在图 29.16 里。

```
3a: draw r ~ Uniform(0, 1)
3b: xl := x - rw
3c: xr := x + (1 - r)w
3d: while (P*(xl) > u') { xl := xl - w }
3e: while (P*(xr) > u') { xr := xr + w }
```

### 第 8 步的 'shrinking'（收缩）方法

每当抽到的点 $x'$ 使得 $(x', u')$ 落在曲线 $P^*(x)$ **上方**，我们就把区间收缩，使它的一个端点成为 $x'$，同时保证原来的点 $x$ 仍被这个区间包含。

```
8a: if (x' > x) { xr := x' }
8b: else { xl := x' }
```

### Slice sampling 的性质 · Properties of slice sampling

像标准的 Metropolis 方法一样，slice sampling 也是靠随机游走来移动的；但两者的差别在于：在 Metropolis 方法里，步长的选择对于推进的速率是决定性的——下文落在下一页。

<span style="color:#1e8449;">**[译注]**
这一页是整个第 29 章最漂亮的一步：它用**一根辅助变量（auxiliary variable）$u$** 把「从 $P(x)$ 抽样」换成了「在曲线下的二维区域里均匀抽样」。机制是三行代数。

在曲线下面积 $A = \int \mathrm{d}x\,P^*(x)$ 上取均匀分布 $p(x,u) = 1/A$（$0 \lt u \lt P^*(x)$），则对 $u$ 积分掉：

```math
\int_0^{P^*(x)}\frac{\mathrm{d}u}{A}=\frac{P^*(x)}{A}=P(x),
```

**边际分布恰好是 $P$**。于是「在面积上均匀」与「按 $P$ 抽样」是同一件事，只是前者多带一个可以随便丢掉的坐标。

第 2 步是 $u' \sim \text{Uniform}(0, P^*(x))$，第 5–7 步是在水平条 $[x_l, x_r]\times\{u'\}$ 上重新抽 $x'$ 并检查是否仍在曲线下——这就是一个**Gibbs 式的一步**：固定 $u$ 抽 $x$、固定 $x$ 抽 $u$ 交替进行，而 $u$ 的更新被做成了「只往上抽、不再往下调」的确定性写法。

**消失测试**：抽掉这个辅助变量，只剩「按 $P^*$ 稠密程度抽 $x$」，你就必须**知道 $P^*$ 的上界**才能做 rejection sampling（这正是本页强调 slice sampling 不需要 upper-bounding function 的意思）。可观测后果：一个 $P^*$ 有 $10^{9}$ 量级动态范围的模型（典型的后验），上界估计只要差 $10$ 倍，拒绝率就从可接受变成 $1 - 10^{-8}$，每抽一个样本要试 $10^{8}$ 次。

**落点**：本页第 2 步与第 5–7 步；形式等价在 (Neal, 2003) §1；与 rejection sampling 的差别在第 29.3 节（p367）的上界函数要求。上游只需二维联合分布与边际分布（6.042J + 第 2 章概率），不越级。
</span>

---



[Figure 29.16：Slice sampling。每个面板用「在该面板里被执行的算法步骤号」标注：1；2；3a,3b,3c；3d,3e；5,6；8；5,6,7。

**图注译文**：第 1 步在当前位置 $x$ 处求 $P^*(x)$ 的值。第 2 步选一个纵向坐标，得到由方框标出的点 $(x, u')$。第 3a–c 步随机创建一个大小为 $w$、包含 $(x,u')$ 的区间。第 3d 步在区间左端求 $P^*$，发现它比 $u'$ 大，于是向左走一步、步长 $w$。第 3e 步在区间右端求 $P^*$，发现它比 $u'$ 小，所以向右无需 step out。再重复第 3d 步时，$P^*$ 被查到比 $u'$ 小，于是 step out 停止。第 5 步从区间里抽一个点，用 $\circ$ 标出。第 6 步确认这个点位于 $P^*$ 之上（即曲线之上），第 8 步就把区间收缩到那个被拒的点，同时保证原来的点 $x$ 仍在区间内。再重复第 5 步时，新坐标 $x'$（位于区间右手侧）给出的 $P^*$ 大于 $u'$，于是这个 $x'$ 就是第 7 步的输出。

**可复原性说明**：文字层里只抽出步骤号 `1`、`2`、`3a,3b,3c`、`3d,3e`、`5,6`、`8`、`5,6,7` 与符号 `◦`，**曲线的具体形状、方框位置、每条水平线段的两端坐标全部不可复原**。因此本译文只保留「步骤号 + 图注逻辑」，不重画几何；读者若需看排版，请对照原书 p376。]

<span style="color:#1e8449;">**[译注]**
七个面板其实在演示**两个分支各走一次**，而这两个分支恰好是 detailed balance 的两个半边。

**半边一（3d/3e）：扩张可以不对称。** 左端 $P^*(x_l) \gt u'$ 时继续向左走，右端 $P^*(x_r) \le u'$ 时停下——**同一轮里两侧的行为不同，这是常态而不是异常**。合法性来自 3a 那个随机偏移 $r$：区间的初始宽度固定为 $w$，但 $x$ 在其中的位置由 $r \sim \text{Uniform}(0,1)$ 决定，于是「以 $x$ 为中心、宽度 $w$」与「以 $x$ 为左端点、宽度 $w$」这两个极端都只是 $r = 0.5$ 与 $r = 0$ 的特例。若把 $r$ 写死成 $0.5$（区间恒以 $x$ 居中），detailed balance 会被一个因子 2 破坏。

**半边二（8）：收缩必须保留 $x$。** 8a/8b 只把**远离 $x$ 的那一侧**端点收到 $x'$，$x$ 始终留在区间内。这是返回路径存在的唯一保证：从 $x'$ 出发的那一步，区间由 $x'$ 重新扩张，必须仍能覆盖 $x$。

**消失测试**：把 8b 改成「$x_l := x'$ 且 $x_r := x'$」（即把区间收到单点），接受率仍是 $1$（步骤 5–7 不变），链也不会报错，但 $x$ 被挤出后区间再也长不回来；从 $x$ 出发走 $10^{4}$ 步统计往返次数，正向与反向不再相等，**分布在 $\sigma$ 量级上被拉斜**。

**落点**：本页图 29.16 与 p375 的 8a/8b 伪码；$r$ 的作用在 p375 的 3a–3c；(Neal, 2003) §4 给出「shrinkage 必须保留当前点」的正式条件。上游是「可逆性 = 存在返回路径」（6.042J 图的对称关系），不越级。
</span>

---



在 slice sampling 里步长是**自调（self-tuning）**的。

设初始区间大小 $w$ 与 probable region（概率集中的区域）的宽度相比**小了一个因子 $f$**，那么 stepping-out 过程会把区间扩大。

这个 stepping-out 的代价**只是 $f$ 的线性函数**；而在 Metropolis 方法里，如果步长太小，计算机时间按 $f$ 的**平方**增长。

反过来，若选定的 $w$ **大了一个因子 $F$**，那么算法花在把区间缩到正确大小上的时间与 $\log F$ 成正比——因为每次有点被拒时，区间典型地会收缩大约 $0.6$ 这个量级的因子。

相比之下，Metropolis 算法对过大的步长的反应是**几乎拒绝所有 proposal**，于是推进速率在 $F$ 上是**指数级地坏**。

Slice sampling 里**没有拒绝**；停在完全相同位置的概率极小。

[Figure 29.17：$P^*(x)$。横轴 $x$ 从 $1$ 到 $11$（刻度 $1,2,\dots,11$），纵轴是**对数刻度**（标注 $0$、$1$、$10$），曲线在 $x \in (0,1)$ 有一个峰、在 $x \in (1,11)$ 有一段很长的低尾。

**可复原性说明**：文字层只抽出刻度数字与轴标，**曲线的函数形式与峰值均不可复原**；可确证的只有三件事：① 纵轴是对数轴（同时标出 $1$ 与 $10$）；② 图注给出的定义域是段状的，Exercise 29.10 说 $x$ 是 $0.0$ 到 $11.0$ 之间的实数；③ 峰与尾之间隔着一段高概率的谷，这使 slice sampling 必须「跨过谷」才能连通两个区域。]

<span style="color:#b9770e;">**[exercise 29.10]** `[2]` Investigate the properties of slice sampling applied to the density shown in figure 29.17. $x$ is a real variable between $0.0$ and $11.0$. How long does it take typically for slice sampling to get from an $x$ in the peak region $x \in (0,1)$ to an $x$ in the tail region $x \in (1,11)$, and vice versa? Confirm that the probabilities of these transitions do yield an asymptotic probability density that is correct.

**话题摘要**：一个峰 + 一个长尾的双区密度上，slice sampling 跨区的时间远小于 Metropolis——因为区间扩张会自动跨过峰尾之间的低谷；题目要你验证跨区概率之比恰好等于两侧概率质量之比（即 detailed balance 在起作用的可观测形式）。</span>

### 真实问题里怎么用 slice sampling · How slice sampling is used in real problems

一个 $N$ 维密度 $P(x) \propto P^*(x)$，可以借助上面的一维 slice sampling 方法来抽样：取一串方向 $y^{(1)}, y^{(2)}, \dots$，并令 $x = x^{(t)} + x\,y^{(t)}$。

上面出现的函数 $P^*(x)$ 就换成 $\tilde P^*(x) = P^*(x^{(t)} + x\,y^{(t)})$。

方向可以按多种方式选取；例如，像 Gibbs sampling 那样，方向可以取坐标轴；另一种做法是把方向 $y^{(t)}$ 按任意一种能使整体过程满足 detailed balance 的方式随机选取。

### 对计算机友好的 slice sampling · Computer-friendly slice sampling

概率模型里的实变量，在计算机里总是用有限个比特来表示。

下面这个由 Skilling 给出的 slice sampling 实现，把上文用浮点运算描述的 stepping-out、随机化与 shrinking 操作，换成了**二进制与整数运算**。

我们假定被 slice 采样的变量 $x$ 由一个 $b$ 比特整数 $X$ 表示，$X$ 取 $B = 2^b$ 个值 $0, 1, 2, \dots, B-1$ 中的一个，其中许多或全部对应于合法的 $x$ 值。

采用整数网格，就**消除了浮点数变精度舍入可能给 detailed balance 带来的误差**。

从 $X$ 到 $x$ 的映射不必是线性的；若是非线性的，我们假定函数 $P^*(x)$ 被相应地换成了一个经过变换的函数——例如 $P^{**}(X) \propto P^*(x)\,|\mathrm{d}x/\mathrm{d}X|$。

我们假定下列作用于 $b$ 比特整数的算子可用：

| 算子 | 含义 |
|---|---|
| `X + N` | $X$ 与 $N$ 的算术和，模 $B$ |
| `X - N` | $X$ 与 $N$ 的差，模 $B$ |
| `X ⊕ N` | $X$ 与 $N$ 的按位异或（bitwise exclusive-or） |
| `N := randbits(l)` | 把 $N$ 设为随机的 $l$ 比特整数 |

针对整数的 slice sampling 过程如下（原文下一页）。

<span style="color:#1e8449;">**[译注]**
这一页的 $f$ / $F$ 成本对照是全章**唯一给出函数形式（而非仅量级）**的地方，值得把它当成工程判据而不是修辞。假设 probable region 宽度为 $L$、初始区间 $w$。

**太小**（$w = L/f$）：stepping out 每侧要走 $\log$ 意义上…不，是**按步数线性**地扩，共需 $f/2$ 步左右，代价 $O(f)$。而 Metropolis 在步长 $\epsilon = L/f$ 时，由 (29.32) 每换一个独立样本需 $(L/\epsilon)^2 = f^2$ 次迭代，**代价 $O(f^2)$**。

**太大**（$w = FL$）：每次拒绝把区间收缩到「被拒点与新点之间」，几何平均收缩比约 $0.6$，于是从 $FL$ 缩到 $L$ 需要 $\log_{1/0.6}(F) \approx 2.3\log F$ 次，代价 $O(\log F)$。Metropolis 在 $\epsilon = FL$ 时，接受概率约为 $\exp(-(\epsilon/L)^2/2) \simeq e^{-F^2/2}$，要凑够一次成功提议需 $e^{F^2/2}$ 次，**代价 $O(e^{F^2})$**。

代入 $F = 3$：slice 约 $2.3\times1.1 \approx 2.5$ 次评估，Metropolis 约 $e^{4.5}\approx 90$ 次；$F = 10$ 时分别是 $5.3$ 与 $e^{50}\approx 5\times10^{21}$。

**消失测试**：抽掉「无拒绝」这一条，slice sampling 就与「试很多步长、挑一个接受的」启发式没有区别，你也就无法解释为什么它对 $w$ 的选择不敏感。可观测后果：把 $w$ 误设为 probable region 的 $10$ 倍，一个正确的实现只是慢 5 倍（可接受），而同一参数下的 Metropolis 跑 $10^{6}$ 步都动不了一次——**用户会以为是自己的模型写错了**。

**落点**：本页前三段；$0.6$ 这个收缩常数来自 (Neal, 2003) §4 的经验值；$(L/\epsilon)^2$ 的对照见 p368 的 (29.32)。上游是等比收缩的步数 $\log F/\log(1/0.6)$（6.042J 对数性质），不越级。
</span>

---



给定：当前点 $X$ 与高度 $Y = P^*(X)\times \text{Uniform}(0,1) \le P^*(X)$

| 步 | 语句 | 说明 |
|---|---|---|
| 1 | `U := randbits(b)` | 定义二进制坐标系的一个随机平移 $U$ |
| 2 | 把 $l$ 设成某个 $l \le b$ | 设定初始的 $l$ 比特采样范围 |
| 3 | `do {` | —— |
| 4 | `N := randbits(l)` | 在当前宽度为 $2^l$ 的区间里定义一个随机移动 |
| 5 | `X' := ((X - U) ⊕ N) + U` | 把 $X$ 的最低 $l$ 个比特随机化（在平移后的坐标系里） |
| 6 | `l := l - 1` | 若 $X'$ 不可接受，减小 $l$、用更小的扰动再试 |
| 7 | `} until (X' = X) or (P*(X') >= Y)` | 保证在 $l = 0$ 处或之前终止 |

引入平移 $U$，是为了**避免永久性的锐利边界**：否则相邻的两个二进制整数 `0111111111` 与 `1000000000` 会永远待在不同的区段里，使 $X$ 难以从一个走到另一个。

[Figure 29.18：候选点被抽出的那串区间，横轴是 $X$，从 $0$ 到 $B-1$。

**可复原性说明**：文字层只抽出 `0`、`B−1`、`X` 三个标签与图注，**每层区间的端点位置不可复原**。可确证的结构是图注里那两句：第一次从整个区间抽点（最上面那条水平线），随后每次抽点，区间都**减半且保持包含前一个点 $X$**。]

新的候选点所来自的区间序列画在图 29.18 里：首先从整个区间抽一个点（最上面那条水平线）；其后每次抽样，区间都减半，减半的方式保证它包含前一个点 $X$。

如果需要从初始范围先做一步 stepping-out，那么上面第 2 步可以换成下面这个类似的过程：

```
2a: set l to a value l < b           # l sets the initial width
2b: do {
2c:     N := randbits(l)
2d:     X' := ((X - U) ⊕ N) + U
2e:     l := l + 1
2f: } until (l = b) or (P*(X') < Y)
```

这些 shrinking 与 stepping-out 方法**每次求值把区间缩小或扩大一个因子 2**。

一个变体是每次缩/扩**不止一个比特**，即令 $l := l \pm \Delta l$，其中 $\Delta l \gt 1$。

每一步从任意一个预先指定的分布里取 $\Delta l$（该分布可以包含 $\Delta l = 0$）会带来额外的灵活性。

<span style="color:#b9770e;">**[exercise 29.11]** `[4]` In the shrinking phase, after an unacceptable $X'$ has been produced, the choice of $\Delta l$ is allowed to depend on the difference between the slice's height $Y$ and the value of $P^*(X')$, without spoiling the algorithm's validity. (Prove this.) It might be a good idea to choose a larger value of $\Delta l$ when $Y - P^*(X')$ is large. Investigate this idea theoretically or empirically.

**话题摘要**：收缩幅度 $\Delta l$ 可以依赖 $Y - P^*(X')$ 这个「差多远」的信息而不破坏细致平衡——因为被拒点所在的半区间**无论如何都要被丢掉**，其内部信息不影响剩余支撑集上的均匀性；离得越远，说明该多砍。</span>

使用整数表示有一个特点：只要比特数取得足够多，**单个整数 $X$ 就可以表示两个或更多实参数**——例如通过 Peano 曲线这类 space-filling curve（空间填充曲线）把 $X$ 映射到 $(x_1, x_2, x_3)$。

于是多维 slice sampling 可以用与一维相同的软件来完成。

<span style="color:#1e8449;">**[译注]**
那个平移 $U$ 不是洁癖，它修的是**一个会静默毁掉遍历性的边界效应**。设 $b = 10$，$X = 511 = $ `0111111111`，$X' = 512 = $ `1000000000`。若不做平移，第 5 步给出 $X' = (X \oplus N)$：要把 $0111111111$ 变成 $1000000000$，$N$ 必须是 `1111111111`（全 1），在 $l = 10$ 时概率是 $1/1024$；而 $l$ 一减小，这个 $N$ 就**不可能**再用上。也就是说，当 $l$ 收缩到 $l = 9$ 时，$X$ 与 $X'$ 共享高比特、最低 $9$ 位可翻转，**跨过 511/512 这条边界的概率恒为 0**；两个半区就是两个不可约分量，链落在哪一半取决于初始值（与 p373 的 reducible 是同一个病）。

加上平移后，$X \mapsto X - U$（模 $B$）把边界挪到一个**随机**位置，每次迭代重新抽 $U$，于是任何一对相邻整数在某个 $U$ 下都会变成「最低比特不同」的一对，穿越概率回到 $1/2$。用一句话概括：**$U$ 把「固定的二分边界」换成了「随机位置的二分边界」，从而让所有边界在长时间平均下被均匀地跨过。**

**消失测试**：抽掉 $U$（令 $U \equiv 0$），在 $b = 10$ 的整数网格上从 $X = 512$ 出发、$P^*$ 处处相等（这样所有 $X'$ 都可接受），跑 $10^{6}$ 步统计 $X \lt 512$ 的比例：正确实现应得 $\approx 0.5$，无平移实现得**精确的 0**。这是一个零成本、单行可查的回归测试，而症状（「采样总在左半边」）在真实后验上会被误读成「数据偏向该区域」。

**落点**：本页 `U := randbits(b)` 与紧随其后的解释段；同类的不可约性问题在 p373 的 (b) 与 hypercube 例子；$\Delta l$ 的推广见 Exercise 29.11。上游是模运算与按位异或（CSAPP §2.1 位级运算），不越级。
</span>

---



## 29.8 实务问题 · Practicalities

**我们能预测一个 Markov chain Monte Carlo 模拟要多久才平衡（equilibrate）吗？**

通过考察 Markov chain Monte Carlo 模拟中涉及的那些随机游走，我们可以得到收敛所需时间的**简单下界**。

但更精确地预测这个时间是个难题，而给出收敛时间上界的大部分理论结果都**没有多少实际用处**。

第 32 章的 exact sampling（精确抽样）方法对某些 Markov chain 给出了这个问题的解。

**我们能诊断或检测一条正在运行的模拟是否收敛吗？**

这同样是个难题。有几个可用的实用工具，但没有一个是完美的（Cowles and Carlin, 1996）。

**我们能加快 Markov chain Monte Carlo 方法的收敛时间、以及独立样本之间的间隔吗？**

这里有好消息，放在下一章讲——那一章介绍 Hamiltonian Monte Carlo 方法、overrelaxation（过松弛）以及 simulated annealing（模拟退火）。

## 29.9 进一步的实际问题 · Further practical issues

**归一化常数能算出来吗？**

如果 target density $P(x)$ 是以未归一化密度 $P^*(x)$ 的形式给出的，即 $P(x) = \frac{1}{Z}P^*(x)$，那么 $Z$ 的值很可能正是你关心的东西。

Monte Carlo 方法**并不直接**给出这个量的估计，如何求它是一片活跃的研究领域。

估计 $Z$ 的技术包括：

1. Importance sampling（Neal (1993b) 有综述）以及 annealed importance sampling（Neal, 1998）。
2. 在 simulated annealing 期间做「thermodynamic integration（热力学积分）」、'acceptance ratio' 方法，以及 'umbrella sampling'（均由 Neal (1993b) 综述）。
3. 'Reversible jump Markov chain Monte Carlo'（Green, 1995）。

不过，对付 $Z$ 的一个办法，是**找一个不需要求 $Z$ 的任务解**。

在 Bayesian 数据建模中，只要手上**不超过一个模型**，就可能避免去求 $Z$——而求 $Z$ 本来是 model comparison（模型比较）才需要的。

替代做法是：不去用若干个（比如复杂度不同的）模型并比较它们的相对后验概率，而是造**一个**层级模型（hierarchical model），让它带上若干个连续的超参数（hyperparameter），这些超参数扮演的角色与那些不同模型所扮演的角色类似（Neal, 1996）。

在指出「可以不算 $Z$」这个可能性的同时，我**并不是**在推荐这条路。

归一化常数 $Z$ 常常是整个问题里唯一最重要的那个数，我认为应当尽一切努力把它算出来。

### 大模型上的 Metropolis 方法 · The Metropolis method for big models

我们最初对 Metropolis 方法的描述，是用一个 proposal density $Q(x';x)$ 对**所有**变量做一次联合更新。

对大问题来说，更有效率的做法可能是用**若干个** proposal distribution $Q^{(b)}(x';x)$，每一个只更新 $x$ 的一部分分量；每一个 proposal 各自被接受或拒绝，而这些 proposal distribution 被反复依次跑一遍。

<span style="color:#1e8449;">**[译注]**
「predict / diagnose / speed up」这三问是本章的工程收束，其中第一问那句「上界理论多半没用」值得当判据记住，因为它给了**为什么实践者只能靠下界 + 经验法则**的理由。具体地说：收敛时间的严格上界依赖谱隙 $\gamma = 1-\lambda_2$，而 $\lambda_2$ 对 $N$ 的依赖在最坏情形是灾难性的——对 $N$ 维超立方上的 Ising 模型，谱隙随 $N$ 指数小，但「典型」的随机初始条件下链几万步就混合了。

**消失测试**：如果只给上界不给下界（也就是只有 (29.32) 的否定版），你无法区分「这条链需要 $10^{6}$ 步」和「这条链需要 $10^{60}$ 步」，而两者的工程决策完全相反。可观测后果：拿一个严格上界去规划计算预算，会在 $N=100$ 的模型上得出「需要跑到宇宙寿命」的结论而**放弃一个实际几秒就能跑完的任务**；反过来，只有下界而没有收敛诊断，就会在真正没混合的链上宣称收敛。

**落点**：本页 §29.8 三段（predict / diagnose / speed up）；exact sampling（完美抽样）在第 32 章；加速方法在第 30 章；诊断工具综述是 Cowles and Carlin (1996)。上游是「上界与下界是不同的知识」这一基本区分（6.006 复杂度分析的 best/worst case），不越级。
</span>

<span style="color:#1e8449;">**[译注]**
关于 $Z$ 的这一段是全书**立场最鲜明**的一处，而且它和前后章节的逻辑扣得很紧，值得算一笔账。$Z = \int \mathrm{d}^N x\, P^*(x)$ 在高维下是典型的「典型集之外全是零、典型集之内测度极小」的积分：由 AEP，$-\ln P^*(x) \approx N H + O(\sqrt{N})$，于是 $Z$ 的主要贡献来自一个测度约 $e^{-N H}$ 的区域，其上的 $P^*$ 约 $e^{N H}$。**任何从 $P^*$ 无关的分布抽样的方法（如朴素 importance sampling）都抽不到那个区域**，权重方差按 $e^{N(\cdots)}$ 爆炸——这与 p386 上 Exercise 29.13 在一维里给出的 $\sigma_q^2 \gt \sigma_p^2/2$ 是同一个现象的标量版。

**消失测试**：把「$Z$ 才是 model comparison 的核心」这句删掉，读者会顺着上一段「可以用层级模型绕开 $Z$」直接放弃求 $Z$——而 bayesian model comparison 的答案就是比值 $Z_1/Z_2$（p349 的 evidence 与 Occam factor 全部由它承载）。可观测后果：绕开 $Z$ 的层级模型给出的是后验预测，**不再是模型之间的相对证据**，于是你无法回答「该用 2 个高斯还是 3 个高斯」这类问题，只能看拟合优度，退回 p350 批评过的过拟合判据。

**落点**：本页 §29.9 第一问；$Z$ 的三种估计路线在本页列表（importance / thermodynamic integration / reversible jump）；$\sigma_q^2 \gt \sigma_p^2/2$ 的临界条件在 p386 的 (29.61)；$Z_1/Z_2$ 与 Occam factor 的关系见 p349。上游是 AEP 与典型集（第 4 章、第 29.1 节已讲），不越级。
</span>

---



<span style="color:#b9770e;">**[exercise 29.12]** `[2, p.385]` Explain why the rate of movement through the state space will be greater when $B$ proposals $Q^{(1)}, \dots, Q^{(B)}$ are considered individually in sequence, compared with the case of a single proposal $Q^*$ defined by the concatenation of $Q^{(1)}, \dots, Q^{(B)}$. Assume that each proposal distribution $Q^{(b)}(x';x)$ has an acceptance rate $f \lt 1/2$.

**话题摘要**：逐个提议 vs 串接成一个提议——串接的接受概率按 $f^{B}$ 衰减而净位移按 $f^{B}B\epsilon^{2}$，逐个的净位移按 $fB\epsilon^{2}$，两者差一个 $f^{B-1}$（答案在 p385，给出 $f^{B}$ 与 $f$ 的对比）。</span>

在 Metropolis 方法里，proposal density $Q(x';x)$ 通常带有若干个参数，用来控制比如它的「宽度」。

这些参数通常靠试错来定，经验法则是瞄准**约 $0.5$ 的拒绝频率**。

有一种做法是**不允许**的：让宽度参数在模拟过程中、以依赖模拟历史的方式动态更新。

这种对 proposal density 的修改会违反 detailed-balance 条件，而正是这个条件保证了 Markov chain 具有正确的不变分布。

### 大模型里的 Gibbs sampling · Gibbs sampling in big models

我们对 Gibbs sampling 的描述，讲的是每次抽一个参数，如 (29.35–29.37) 所述。

对大问题而言，更有效的做法可能是**成组地联合抽样**变量，也就是用若干个 proposal distribution：

```math
\begin{aligned}
x_1^{(t+1)},\dots,x_a^{(t+1)} &\sim P\bigl(x_1,\dots,x_a \mid x_{a+1}^{(t)},\dots,x_K^{(t)}\bigr) && (29.47)\\
x_{a+1}^{(t+1)},\dots,x_b^{(t+1)} &\sim P\bigl(x_{a+1},\dots,x_b \mid x_1^{(t+1)},\dots,x_a^{(t+1)},x_{b+1}^{(t)},\dots,x_K^{(t)}\bigr),\ \text{etc.} &&
\end{aligned}
```

### 需要多少样本？ · How many samples are needed?

在本章开头我们说过，估计量 $\hat\Phi$ 的方差只取决于**独立样本的个数 $R$** 与下面这个量：

```math
\sigma^2=\int \mathrm{d}^N x\; P(x)\,\bigl(\varphi(x)-\Phi\bigr)^2. \qquad (29.48)
```

现在我们已经讨论过产生 $P(x)$ 样本的各种方法了。

那么，$R$ 该瞄准多大？

**在许多问题里，我们真正需要的只是大约十二个独立样本。**

设想 $x$ 是某个未知向量，比如剑桥周围一万条地下管道各自存在的腐蚀量，而 $\varphi(x)$ 是修这些管道的总费用。

分布 $P(x)$ 描述了「在已经对部分管道做过检测、并对腐蚀物理有若干假设」的条件下，状态 $x$ 的概率。

量 $\Phi$ 是期望的修理费用。

量 $\sigma^2$ 是费用的方差——$\sigma$ 衡量的是：实际费用应当预期比期望值 $\Phi$ 差多少。

那么，一个经理希望把 $\Phi$ 知道到多准？

我的看法是：把 $\Phi$ 知道到比 $\sigma/3$ 更精细，几乎没有意义。

毕竟真实费用本身就很可能在 $\Phi$ 附近 $\pm\sigma$ 的范围内浮动。

若我们从 $P(x)$ 取得 $R = 12$ 个独立样本，就能把 $\Phi$ 估计到精度 $\sigma/\sqrt{12}$ ——这比 $\sigma/3$ 更小。

所以十二个样本就够了。

### 资源的分配 · Allocation of resources

假定我们已经决定了需要多少个独立样本 $R$，那么一个重要的问题是：怎样用有限的计算机资源去取得这些样本。

<span style="color:#1e8449;">**[译注]**
「十二个样本」这个数字不是随手写的，它是**三个常数凑出来的**，值得把账算开，因为同类推理在别处会反复出现。设 $\hat\Phi_R$ 用 $R$ 个独立样本估计 $\Phi$，则 $\mathrm{sd}(\hat\Phi_R) = \sigma/\sqrt{R}$。要求这个标准差小于 $\sigma/3$：

```math
\frac{\sigma}{\sqrt{R}} \lt \frac{\sigma}{3}\iff R \gt 9,
```

取整数、留一点余量就是 $R = 12$（作者选的 $\sqrt{12} \approx 3.46 \gt 3$）。注意这条路**每一步只用到「方差按 $1/R$ 降」这一条**，没有用到任何分布形状假设。

两处要点。第一，判据的基准是 $\sigma$（被估量自身的波动），不是 $\Phi$ 的量级——所以「相对精度」这个概念在这里**不出现**，这正确得多了：一个费用问题里，你再精确地知道期望也没用，因为真实值本来就在 $\pm\sigma$ 里晃。第二，$\sqrt{R}$ 的收益意味着把精度从 $\sigma/3$ 提到 $\sigma/30$ 要 100 倍样本，**这是 Monte Carlo 方法最本质的诅咒**（$O(R^{-1/2})$ 而非 $O(R^{-1})$），也是 quasi-Monte Carlo 与 polynomial chaos 一类方法存在的理由。

**消失测试**：抽掉「以 $\sigma$ 为基准」这一步，剩下的就只是「样本越多越好」，你无法为任何实际问题定一个**停止条件**。可观测后果：要么跑得远超需要（$\sigma/30$ 的精度要 $900$ 个独立样本，而每个样本在 MCMC 里还要再乘 $(L/\epsilon)^2$ 次迭代），要么在 $\sigma/\sqrt{1} = \sigma$ 的量级就停手——两种做法都错，而错的方向相反。

**落点**：本页三段（(29.48) 定义 $\sigma^2$、$\sigma/3$ 的判据、$R=12$ 的结论）；$1/\sqrt{R}$ 的来源在本章开头（p357 的第一个公式）；相关样本下 $\hat\Phi$ 的方差不按 $1/R$ 降，见本页末段。上游是方差的可加性与 $\sqrt{n}$ 律（6.042J 期望方差 + 大数律），不越级。
</span>

---



[Figure 29.19：在固定的计算机时间内取得十二个样本的三种可能 Markov chain Monte Carlo 策略。时间用水平线表示，样本用白色圆圈表示。(1) 一次单独的运行，由一个较长的 'burn in' 期加上一段采样期构成。(2) 四次中等长度的运行，初始条件各不相同，各带一个中等长度的 burn in。(3) 十二次短运行。

**可复原性说明**：文字层只抽出 `(1) (2) (3)` 三个编号，**水平线的长度、圆圈的位置与个数全部不可复原**；但图注本身足以复原三种策略的骨架，本译文按图注重建，不重画。]

一个典型的 Markov chain Monte Carlo 实验，包含一段初始时期，其间模拟的控制参数（比如步长）可以被调整。

随后是一段 'burn in'（预热）期，其间我们希望模拟「收敛」到想要的分布。

最后，随着模拟继续，我们**时不时**记录一下状态向量，从而造出一张状态清单 $\{x^{(r)}\}_{r=1}^{R}$，我们希望这些是 $P(x)$ 的、大致独立的样本。

策略有几种可能（图 29.19）：

1. 做**一次长的**运行，从它里面取得全部 $R$ 个样本。
2. 做**几次中等长度**的运行，初始条件各不相同，每次取一部分样本。
3. 做 $R$ 次**短的**运行，每次都从不同的随机初始条件出发，只记录每次模拟的**最终状态**。

第一种策略最有机会达到「收敛」。

最后一种策略可能有个好处：记录下来的样本之间的相关性更小。

中间那条路在 Markov chain Monte Carlo 专家中间更受欢迎（Gilks et al., 1996），因为它避免了在许多次运行里丢弃 burn-in 迭代的低效，同时又仍然允许你**发现那些单次运行看不出来的、缺乏收敛的问题**。

最后，我要强调：**没有必要让估计里用到的那些点几乎独立**。

对有依赖的点取平均是可以的——它不会给估计带来任何偏差。

例如，当你用策略 1 或 2 时，若愿意，你可以把每次运行中第一个与最后一个样本之间的所有点都算进去。

当然，当这些点相关时，**估计的精度**就更难估计了。

## 29.10 小结 · Summary

- Monte Carlo 方法是强有力的工具，它让人能从**任何**可以写成 $P(x) = \frac{1}{Z}P^*(x)$ 形式的概率分布中抽样。
- Monte Carlo 方法能回答几乎任何与 $P(x)$ 有关的问询，只要把问询写成

```math
\int \varphi(x)\,P(x)\simeq \frac{1}{R}\sum_r \varphi\bigl(x^{(r)}\bigr). \qquad (29.49)
```

<span style="color:#1e8449;">**[译注]**
「不必让点独立」这一句是本章最容易被跳过、又最能立刻改善实践的一句，因为它把**偏差（bias）**与**方差（variance）**这两件事干净地切开了。$\hat\Phi_R = \frac{1}{R}\sum_r\varphi(x^{(r)})$ 无论点是否相关，只要每个 $x^{(r)}$ 的边际分布是 $P$，就有 $\mathbb{E}[\hat\Phi_R] = \Phi$ ——**无偏是边际性质，与相关性无关**。

有相关性时变的是方差：$\mathrm{var}(\hat\Phi_R) = \frac{\sigma^2}{R} + \frac{2}{R^2}\sum_{r \lt s}\mathrm{cov}(r,s)$，对 AR(1) 型自相关 $\rho^{|r-s|}$，这给出 $\mathrm{var} \approx \frac{\sigma^2}{R}\cdot\frac{1+\rho}{1-\rho}$。取 $\rho = 0.9$：有效样本量只剩 $R/19$，方差放大 $19$ 倍；$\rho = 0.99$ 时放大 $199$ 倍。

**消失测试**：抽掉这句话，读者会照着教科书的「thinning（稀疏化）」习惯，每 $k$ 步只留一个点丢掉其余——这在 $\rho$ 高时**白扔 $k$ 倍算力而不减小方差**（因为被丢的点里也有信息），并且让误差估计变得更难（样本变少）。可观测后果：一条自相关时间 $\tau = 100$ 的链，thinning 到每 100 步一取，样本数从 $10^{6}$ 掉到 $10^{4}$，误差棒反而**变宽**而不是变准，因为有效样本量本来就只有 $10^{4}$，你只是把可用的自相关结构信息扔了。

**落点**：本页倒数第三段；$\sigma^2$ 的定义在 (29.48)；有效样本量在 p368 的图 29.12 译注里已引入；误差估计的困难正是 §29.8 第一问「能否诊断收敛」的一部分。上游是协方差与方差的可加性（6.042J），不越级。
</span>

---



- 在高维问题里，唯一令人满意的方法是那些**基于 Markov chain** 的方法：Metropolis 方法、Gibbs sampling、slice sampling。Gibbs sampling 有吸引力，因为它没有可调参数，但它的使用被限制在「能从条件分布抽样」的情形。Slice sampling 有吸引力，是因为虽然它带着步长参数，其表现对这些参数的取值并不很敏感。
- 简单的 Metropolis 算法与 Gibbs sampling 算法虽然被广泛使用，表现却不好，因为它们靠一个缓慢的随机游走来探索空间。下一章讨论加速 Markov chain Monte Carlo 模拟的方法。
- Slice sampling 并**没有**避开随机游走行为，但它自动选择了最大的合适步长，从而与比如「步长极小的 Metropolis 方法」相比，减轻了随机游走的不良后果。

## 29.11 习题 · Exercises

<span style="color:#b9770e;">**[exercise 29.13]** `[2C, p.386]` A study of importance sampling. We already established in section 29.2 that importance sampling is likely to be useless in high-dimensional problems. This exercise explores a further cautionary tale, showing that importance sampling can fail even in one dimension, even with friendly Gaussian distributions. Imagine that we want to know the expectation of a function $\varphi(x)$ under a distribution $P(x)$,

```math
\Phi=\int \mathrm{d}x\, P(x)\,\varphi(x), \qquad (29.50)
```

and that this expectation is estimated by importance sampling with a distribution $Q(x)$. Alternatively, perhaps we wish to estimate the normalizing constant $Z$ in $P(x) = P^*(x)/Z$ using

```math
Z=\int \mathrm{d}x\,P^*(x)=\int \mathrm{d}x\,Q(x)\frac{P^*(x)}{Q(x)}=\left\langle \frac{P^*(x)}{Q(x)}\right\rangle_{x\sim Q}. \qquad (29.51)
```

Now, let $P(x)$ and $Q(x)$ be Gaussian distributions with mean zero and standard deviations $\sigma_p$ and $\sigma_q$. Each point $x$ drawn from $Q$ will have an associated weight $P^*(x)/Q(x)$. What is the variance of the weights? [Assume that $P^* = P$, so $P$ is actually normalized, and $Z = 1$, though we can pretend that we didn't know that.] What happens to the variance of the weights as $\sigma_q^2 \to \sigma_p^2/2$? Check your theory by simulating this importance-sampling problem on a computer.

**话题摘要**：即使一维、即使两侧都是友好的 Gaussian，重要性抽样的权重方差在 $\sigma_q^2 \to \sigma_p^2/2$ 时**发散**——而 $Q$ 看起来只是略窄一点（$\sigma_q \approx 0.707\sigma_p$）。这是全章最重要的警告（答案与图 29.20 在 p386）。</span>

<span style="color:#b9770e;">**[exercise 29.14]** `[2]` Consider the Metropolis algorithm for the one-dimensional toy problem of section 29.4, sampling from $\{0,1,\dots,20\}$. Whenever the current state is one of the end states, the proposal density given in equation (29.34) will propose with probability 50% a state that will be rejected. To reduce this 'waste', Fred modifies the software responsible for generating samples from $Q$ so that when $x = 0$, the proposal density is 100% on $x' = 1$, and similarly when $x = 20$, $x' = 19$ is always proposed.

**话题摘要**：把端点处的 proposal 改成「必定向内」，再让软件接受所有提议——问这样采到的是什么分布（答：不是均匀，端点的稳态概率被放大），以及正确的接受规则该是什么（答案在下一页）。</span>

---



（接上页 Exercise 29.14）Fred 把实现接受规则的那部分软件设成**接受所有提议的移动**。

那么 Fred 改过的软件会从什么概率分布 $P'(x)$ 里产生样本？

为了从 $P(x)$ 取样，Fred 的 proposal density 应有的**正确接受规则**是什么？

<span style="color:#b9770e;">**[exercise 29.15]** `[3C]` Implement Gibbs sampling for the inference of a single one-dimensional Gaussian, which we studied using maximum likelihood in section 22.1. Assign a broad Gaussian prior to $\mu$ and a broad gamma prior (24.2) to the precision parameter $\beta = 1/\sigma^2$. Each update of $\mu$ will involve a sample from a Gaussian distribution, and each update of $\sigma$ requires a sample from a gamma distribution.

**话题摘要**：一维 Gaussian 的贝叶斯推断：$\mu$ 给宽 Gaussian 先验、精度 $\beta = 1/\sigma^2$ 给宽 gamma 先验 (24.2)，则 $\mu$ 的条件分布是 Gaussian、$\beta$ 的条件分布是 gamma，两两交替抽样。</span>

<span style="color:#b9770e;">**[exercise 29.16]** `[3C]` Gibbs sampling for clustering. Implement Gibbs sampling for the inference of a mixture of $K$ one-dimensional Gaussians, which we studied using maximum likelihood in section 22.2. Allow the clusters to have different standard deviations $\sigma_k$. Assign priors to the means and standard deviations in the same way as the previous exercise. Either fix the prior probabilities of the classes $\{\pi_k\}$ to be equal or put a uniform prior over the parameters $\pi$ and include them in the Gibbs sampling. Notice the similarity of Gibbs sampling to the soft K-means clustering algorithm (algorithm 22.2). We can alternately assign the class labels $\{k_n\}$ given the parameters $\{\mu_k,\sigma_k\}$, then update the parameters given the class labels. The assignment step involves sampling from the probability distributions defined by the responsibilities (22.22), and the update step updates the means and variances using probability distributions centred on the K-means algorithm's values (22.23, 22.24). Do your experiments confirm that Monte Carlo methods bypass the overfitting difficulties of maximum likelihood discussed in section 22.4? A solution to this exercise and the previous one, written in octave, is available.

**话题摘要**：$K$ 个一维 Gaussian 混合的 Gibbs 版本 = soft K-means 的随机版：分配步从 responsibilities (22.22) 定义的分布里抽标签，更新步用中心在 K-means 值 (22.23/22.24) 的分布更新均值方差；问 Monte Carlo 是否绕开了 §22.4 的过拟合。</span>

<span style="color:#b9770e;">**[exercise 29.17]** `[3C]` Implement Gibbs sampling for the seven scientists inference problem, which we encountered in exercise 22.15 (p.309), and which you may have solved by exact marginalization (exercise 24.3 (p.323)) [it's not essential to have done the latter].

**话题摘要**：七位科学家的推断问题（Ex 22.15）用 Gibbs sampling 重做一遍，与 Ex 24.3 的 exact marginalization 结果对照——同一个后验，两种完全不同的算法。</span>

<span style="color:#b9770e;">**[exercise 29.18]** `[2]` A Metropolis method is used to explore a distribution $P(x)$ that is actually a 1000-dimensional spherical Gaussian distribution of standard deviation 1 in all dimensions. The proposal density $Q$ is a 1000-dimensional spherical Gaussian distribution of standard deviation $\epsilon$. Roughly what is the step size $\epsilon$ if the acceptance rate is 0.5? Assuming this value of $\epsilon$, (a) roughly how long would the method take to traverse the distribution and generate a sample independent of the initial condition? (b) By how much does $\ln P(x)$ change in a typical step? By how much should $\ln P(x)$ vary when $x$ is drawn from $P(x)$? (c) What happens if, rather than using a Metropolis method that tries to change all components at once, one instead uses a concatenation of Metropolis updates changing one component at a time?

**话题摘要**：$N = 1000$ 的球状 Gaussian 上，接受率 $0.5$ 逼出 $\epsilon \approx 2.4/\sqrt{N} \approx 0.076$，于是走遍一遍要 $(1/\epsilon)^2 \approx 173$ 次迭代；但每步 $\ln P$ 只变约 $0.07$，而 $P$ 下 $\ln P$ 本身要变化 $\sqrt{N/2}\approx 22$——这就是「能量维」上的随机游走病（与 (c) 的单坐标串接对照）。</span>

<span style="color:#1e8449;">**[译注]**
Exercise 29.14 是本章**最短、最锋利**的一个陷阱题，答案是一条只差归一化的三对角方程。设 Fred 的 proposal 为 $\tilde Q$：$x=0$ 时 $\tilde Q(1;0)=1$；$x=20$ 时 $\tilde Q(19;20)=1$；其余 $x$ 仍是 $\tilde Q(x\pm1;x)=1/2$。

设内点 $x\in\{1,\dots,19\}$ 的稳态概率为 $c$。对 $x=1$ 做流量核算：流入 $= \pi(0) + \pi(2)/2 = \pi(0)+c/2$，流出 $= \pi(1) = c$，故 $\pi(0)=c/2$；对 $x=0$ 核对：流入 $= \pi(1)/2 = c/2$，流出 $= \pi(0)$ ✓ 自洽。对称地 $\pi(20)=c/2$。归一化是 19 个内点加 2 个半权端点：$19c + 2\cdot(c/2) = 20c = 1$，即 $c = 1/20$。所以

```math
P'(x)=\begin{cases} 1/20 & x\in\{1,\dots,19\},\\ 1/40 & x\in\{0,20\}. \end{cases}
```

**消失测试**：只记住「接受所有提议就等于更快」，你会在这个 $P'$ 上毫无察觉——它看起来仍然平坦。可观测后果：均值仍是 $10$（对称性救了你），但二阶矩变成 $\sum_1^{19}i^2/20 + 400/40 = 123.5+10 = 133.5$，而正确值是 $2870/21 = 136.67$，**方差 $33.5$ 对 $36.67$，偏小 $8.6\%$**——这是统计上几个标准差就能看出来的系统性偏差，而不是噪声。正确的接受规则是 Metropolis 的 $A = \min\{1,\ P(x')\tilde Q(x;x')/(P(x)\tilde Q(x';x))\}$，它在端点处给出的比例因子恰为 $2$，正好把 $1/40$ 抬回 $1/42$ 附近、恢复均匀。

**落点**：交叉页 Exercise 29.14（p382–383）；(29.34) 的原始 proposal 在 p369；同类教训「改 proposal 必须配套改接受率」在 p380 的「禁止动态调宽」一段；形式化的 detailed balance 在 p374 的 (29.46)。上游是线性方程组的流量守恒（6.042J 图论流 + Strang 线代），不越级。
</span>

---



<span style="color:#b9770e;">**[exercise 29.19]** `[2]` When discussing the time taken by the Metropolis algorithm to generate independent samples we considered a distribution with longest spatial length scale $L$ being explored using a proposal distribution with step size $\epsilon$. Another dimension that a MCMC method must explore is the range of possible values of the log probability $\ln P^*(x)$. Assuming that the state $x$ contains a number of independent random variables proportional to $N$, when samples are drawn from $P(x)$, the 'asymptotic equipartition' principle tell us that the value of $-\ln P(x)$ is likely to be close to the entropy of $x$, varying either side with a standard deviation that scales as $\sqrt{N}$. Consider a Metropolis method with a symmetrical proposal density, that is, one that satisfies $Q(x;x') = Q(x';x)$. Assuming that accepted jumps either increase $\ln P^*(x)$ by some amount or decrease it by a small amount, e.g. $\ln e = 1$ (is this a reasonable assumption?), discuss how long it must take to generate roughly independent samples from $P(x)$. Discuss whether Gibbs sampling has similar properties.

**话题摘要**：MCMC 还要探索的第二个维度是 $\ln P^*$ 的取值范围——由 AEP，$-\ln P(x)$ 在熵附近以 $\sqrt{N}$ 的尺度涨落；对称 proposal 下「向上跳大、向下跳小」，于是 $\ln P$ 本身也做一步长约 $1$ 的随机游走，要跨 $\sqrt{N}$ 需 $N$ 步。</span>

<span style="color:#b9770e;">**[exercise 29.20]** `[3]` Markov chain Monte Carlo methods do not compute partition functions $\bar Z$, yet they allow ratios of quantities like $Z$ to be estimated. For example, consider a random-walk Metropolis algorithm in a state space where the energy is zero in a connected accessible region, and infinitely large everywhere else; and imagine that the accessible space can be chopped into two regions connected by one or more corridor states. The fraction of times spent in each region at equilibrium is proportional to the volume of the region. How does the Monte Carlo method manage to do this without measuring the volumes?

**话题摘要**：能量在可达区为 0、区外无穷大时，链在两区的驻留时间之比等于两区**体积**之比——而算法从不测量体积；机制是「穿过走廊的净流量相等」，即 detailed balance 把体积信息编码进了穿越频率。</span>

<span style="color:#b9770e;">**[exercise 29.21]** `[5]` Philosophy. One curious defect of these Monte Carlo methods – which are widely used by Bayesian statisticians – is that they are all non-Bayesian (O'Hagan, 1987). They involve computer experiments from which estimators of quantities of interest are derived. These estimators depend on the proposal distributions that were used to generate the samples and on the random numbers that happened to come out of our random number generator. In contrast, an alternative Bayesian approach to the problem would use the results of our computer experiments to infer the properties of the target function $P(x)$ and generate predictive distributions for quantities of interest such as $\Phi$. This approach would give answers that would depend only on the computed values of $P^*(x^{(r)})$ at the points $\{x^{(r)}\}$; the answers would not depend on how those points were chosen. Can you make a Bayesian Monte Carlo method? (See Rasmussen and Ghahramani (2003) for a practical attempt.)

**话题摘要**：哲学题：MCMC 的估计量依赖 proposal 与随机数种子，因此本身是「非贝叶斯」的；纯贝叶斯的做法是把 $\{x^{(r)}, P^*(x^{(r)})\}$ 当作数据去推断 $P$ 的积分，答案与「点怎么来的」无关（Bayesian Monte Carlo，Rasmussen & Ghahramani 2003）。</span>

## 29.12 解答 · Solutions

### Exercise 29.1 的解答（p362）

我们要证明

```math
\hat\Phi\equiv \frac{\sum_r w_r\,\varphi(x^{(r)})}{\sum_r w_r} \qquad (29.52)
```

收敛到 $\Phi$ 在 $P$ 下的期望。把分子与分母分开考虑。

先看分母。考虑单个 importance weight（重要性权重）

```math
w_r\equiv \frac{P^*(x^{(r)})}{Q^*(x^{(r)})}. \qquad (29.53)
```

<span style="color:#1e8449;">**[译注]**
Exercise 29.20 的答案是本章里**最能说明「MCMC 免费得到体积」的一句话**，值得把机制写到底：它靠的不是测量，而是**频率即体积比**这一恒等式，而恒等式来自 detailed balance 在走廊上的逐点形式。

设两区 $A$、$B$，走廊状态集合 $C$，能量处处为零（可达区内）。在稳态，跨过任意一个「切面」$S \subset C$ 的双向流量相等：$\sum_{a\in A}\pi(a)T(b;a) = \sum_{b\in B}\pi(b)T(a;b)$。若取 $\pi$ 均匀（能量为零 ⇒ 均匀是稳态），则这个等式变成「$A$ 的边界体积等于 $B$ 的边界体积」，进而在对称 proposal 下给出 $|A|/|B| = $ 驻留时间之比。**体积比恰好等于频率比，因为两者由同一个均匀稳态 + 对称 proposal 决定。**

**消失测试**：抽掉「detailed balance 逐点成立」这一步，你就只剩一个全局的不变方程 $\pi = \pi T$，它有**无穷多解**（任何 $A$、$B$ 上的任意组合都是解，只要边界流平衡）；链收敛到哪一个取决于初始条件。可观测后果：一个从 $A$ 区出发、走廊极窄的链，跑 $10^{6}$ 步可能一次都没进过 $B$，于是你统计出的频率比是 $1:0$，而真实体积比是 $1:1$——**错误的方向是「看起来非常确定的 1:0」，没有任何误差棒能提示你**。

**落点**：本页 Exercise 29.20；detailed balance 在 p374 的 (29.46)；同类的不可约/探索失败在 p373 与 p378 的 $U$ 平移译注；图 30.3（p390）是「走廊窄 ⇒ Gibbs 几乎不动」的可视化。上游是流守恒与马尔可夫链稳态（6.042J 图的连通性 + Strang 线代特征值 1），不越级。
</span>

---



它在分布 $Q = Q^*/Z_Q$ 下、对点 $x^{(r)}$ 取平均的期望是什么？

```math
\langle w_r\rangle=\int \mathrm{d}x\; Q(x)\frac{P^*(x)}{Q^*(x)}=\int \mathrm{d}x\;\frac{1}{Z_Q}P^*(x)=\frac{Z_P}{Z_Q}. \qquad (29.54)
```

于是分母的期望是

```math
\left\langle \sum_r w_r\right\rangle = R\,\frac{Z_P}{Z_Q}. \qquad (29.55)
```

只要 $w_r$ 的方差有限，分母除以 $R$ 就会随着 $R$ 增大而收敛到 $Z_P/Z_Q$。〔事实上，即使这个方差无穷大，只要期望有良好定义，估计仍会收敛到正确答案。〕

同样地，分子中一项的期望是

```math
\langle w_r\,\varphi(x)\rangle=\int \mathrm{d}x\; Q(x)\frac{P^*(x)}{Q^*(x)}\varphi(x)=\int\mathrm{d}x\;\frac{1}{Z_Q}P^*(x)\varphi(x)=\frac{Z_P}{Z_Q}\Phi, \qquad (29.56)
```

其中 $\Phi$ 是 $\varphi$ 在 $P$ 下的期望。

于是分子除以 $R$ 随 $R$ 增大而收敛到 $\frac{Z_P}{Z_Q}\Phi$。因此 $\hat\Phi$ 收敛到 $\Phi$。

分子与分母分别是 $RZ_P/Z_Q$ 与 $RZ_P\Phi/Z_Q$ 的**无偏**估计量，但当 $R$ 有限时，它们的**比值** $\hat\Phi$ 未必是无偏估计量。

### Exercise 29.2 的解答（p363）

当真实密度 $P$ 是 multimodal（多峰）时，用一个「拟合到某一个峰」的 sampler density 去做 importance sampling 是不明智的，因为在这种情形下，偶尔会有点落在**另外某个峰**里，而那个点对应的权重会**大得惊人**。

于是估计量的方差会极大；但如果至今没见到任何落在其它峰里的点，这个极大的方差**在用户看来可能完全不明显**。

### Exercise 29.5 的解答（p371）

从 Gibbs sampling 的角度看，syndrome decoding 问题的后验分布是一个**病态**分布。

因子 $\mathbb{1}[Hn = z]$ 只在可能向量 $n$ 空间的一个很小的部分上等于 $1$，也就是对应于合法 codeword 的那 $2^K$ 个点上。

任意两个 codeword 都互不相邻，所以同样地，从任一可行状态 $n$ 翻转任何一个比特，都会把我们带到一个概率为零的状态，于是在 Gibbs sampling 里状态**永远不会移动**。

一个一般的码也有完全相同的问题。

对应合法 codeword 的点数目相对很少，而且它们互不相邻（至少对任何有用的码是这样）。

所以 Gibbs sampling 对 syndrome decoding 没用，理由有两条。**第一**，找到一个还过得去的假设本身就很困难，而且只要状态不在某个合法 codeword 附近，Gibbs sampling 就帮不上忙，因为所有条件分布都没有定义。**第二**，一旦我们处于某个合法假设里，Gibbs sampling 就永远无法把我们带出去。

可以尝试用原消息 $s$ 的各个比特作为变量来做 Gibbs sampling。这种做法的确不会以刚才描述的方式锁死，但对一个好码而言，翻转任何一个比特都会**大幅改变重建出来的 codeword**，于是即使已经找到了一个有相当大似然的状态，Gibbs sampling 要从中逃出来所需要的时间也是不切实际的。

### Exercise 29.12 的解答（p380）

每一个 Metropolis proposal 都会把状态的能量提高或降低某个量。

当 $B$ 个 proposal 被串接起来时，总的能量变化将是一个**含 $B$ 步的随机游走的终点**——下文落在下一页。

---



这个游走可能均值为零，也可能有向上漂移的趋势（如果多数移动都增加能量、只有少数降低它）。

一般说来，若接受率 $f$ 很小，后者会成立：任何一次移动带来的平均能量变化是某个 $\Delta E \gt 0$，于是 $B$ 次移动串接之后的接受概率是 $1/(1+\exp(-B\Delta E))$ 的量级，它大致按 $f^{B}$ 缩放。

移动的均方位移将是 $f^{B}B\epsilon^{2}$ 的量级，其中 $\epsilon$ 是典型的步长。

相比之下，当这些移动被**逐个**考虑时，均方位移是 $fB\epsilon^{2}$ 的量级。

[Figure 29.20：一维的重要性抽样。对 $R = 1000$、$10^{4}$、$10^{5}$，用一个标准差为 $\sigma_q$（横轴）的 sampler density 来估计一个 Gaussian 分布的归一化常数（事实上已知它等于 1）。所有运行使用同一个随机数种子。三个图画的是：(a) 估计出的归一化常数；(b) $R$ 个权重的经验标准差；(c) 其中 30 个权重。三个面板共享横轴 $\sigma_q$（刻度 $0.2, 0.4, \dots, 1.6$），图例是 `1000`、`10000`、`100000`、`theory` 四条曲线。

**可复原性说明**：文字层抽出的是三组纵轴刻度（(a) $0$–$1.6$、(b) $0$–$10$、(c) $0$–$3.5$）与共享横轴刻度，**曲线本身不可复原**。可确证的结构：三条 $R$ 曲线在 $\sigma_q \gtrapprox 0.7$ 处彼此靠拢、与 theory 曲线一致；在 $\sigma_q \lesssim 0.7$ 处 (a) 的估计值崩落、(b) 的经验标准差随 $R$ 增大而发散（而非按 $1/\sqrt{R}$ 收缩）——这正是 (29.61) 相变的可视化。]

### Exercise 29.13 的解答（p382）

权重是 $w = P(x)/Q(x)$，而 $x$ 是从 $Q$ 中抽的。权重的均值是

```math
\int \mathrm{d}x\; Q(x)\,\frac{P(x)}{Q(x)}=\int \mathrm{d}x\; P(x)=1, \qquad (29.57)
```

假定该积分收敛。方差是

```math
\mathrm{var}(w)=\int \mathrm{d}x\; Q(x)\left(\frac{P(x)}{Q(x)}-1\right)^{2} \qquad (29.58)
```

```math
=\int \mathrm{d}x\;\frac{P(x)^{2}}{Q(x)}-2P(x)+Q(x) \qquad (29.59)
```

```math
=\frac{Z_Q}{Z_P^{2}}\int \mathrm{d}x\; \exp\left[-\frac{x^{2}}{2}\left(\frac{2}{\sigma_p^{2}}-\frac{1}{\sigma_q^{2}}\right)\right]-1, \qquad (29.60)
```

其中 $Z_Q/Z_P^{2} = \sigma_q/\bigl(\sqrt{2\pi}\,\sigma_p^{2}\bigr)$。

(29.60) 里的积分只有当指数中 $x^{2}$ 的系数为正时才有限，也就是当

```math
\sigma_q^{2} \gt \frac{1}{2}\sigma_p^{2}. \qquad (29.61)
```

若这个条件满足，方差是

```math
\mathrm{var}(w)=\frac{\sigma_q^{2}}{\sigma_p^{2}}\left(\frac{2\sigma_q^{2}-\sigma_p^{2}}{\sigma_p^{2}}\right)^{-1/2}-1. \qquad (29.62)
```

当 $\sigma_q$ 趋近临界值——大约 $0.7\sigma_p$——时，方差变得**无穷大**。

图 29.20 以 $\sigma_p = 1$、$\sigma_q$ 从 $0.1$ 变到 $1.5$ 的情形演示了这些现象。

所有运行使用同一个随机数种子，所以权重与估计值都沿着光滑曲线走。

请注意：$R$ 个权重的**经验标准差**看起来可以相当小、相当规矩（比如说在 $\sigma_q \simeq 0.3$ 处），而它真正的标准差** nonetheless 是无穷大**。

<span style="color:#1e8449;">**[译注]**
这一页是本章**唯一一次把「理论发散」与「经验看起来正常」摆在一起**的地方，它的分量值得算清楚。

$P = N(0,\sigma_p^2)$、$Q = N(0,\sigma_q^2)$ 时，权重 $w = P/Q = (\sigma_q/\sigma_p)\exp\left[-\frac{x^2}{2}\left(\frac{1}{\sigma_p^2}-\frac{1}{\sigma_q^2}\right)\right]$。取 $\sigma_q = 0.3\sigma_p$（图里那个「看起来规矩」的值），指数系数为 $\frac{1}{\sigma_p^2}\left(1 - \frac{1}{0.09}\right) = -\frac{10.1}{\sigma_p^2}$，即 $w \propto \exp(+10.1 x^2/\sigma_p^2)$——**关于 $x$ 是凸的指数**。它的二阶矩 $\int Q w^2$ 要求 $\frac{2}{\sigma_p^2}-\frac{1}{\sigma_q^2} = \frac{2-11.1}{\sigma_p^2} \lt 0$，即 $\sigma_q^2 \gt \sigma_p^2/2$ 被违反，故 $\mathbb{E}[w^2] = \infty$，同时 $\mathbb{E}[w] = 1$ 有限。

**消失测试**：如果只记住「$Q$ 越接近 $P$ 越好」这条定性准则，你会把 $\sigma_q = 0.7\sigma_p$ 当成「已经够接近」，而 (29.61) 说的是**这张图上的临界点就落在 $\sigma_q/\sigma_p = 1/\sqrt{2}\approx 0.707$ 处**，跨过去就是相变。可观测后果：$R = 10^{5}$ 个样本里只要抽到一个 $|x| \gt 4\sigma_q$ 的点，它的权重就能让整条估计曲线跳一个量级——而 图 (b) 说明了最阴险的部分：**经验标准差在 $\sigma_q \simeq 0.3$ 处看起来只有 1 的量级**（因为 $10^{5}$ 个样本里最大的 $\exp(10.1x^2)$ 还没爆），于是任何基于「样本标准差」的收敛判据都会给你绿灯，而真实方差无穷。

**落点**：本页 (29.57)–(29.62) 与图 29.20；题目在 p382 的 Exercise 29.13；同类的「高维必崩」在 §29.2（p362，上一块已译）；$\sigma_q^2 \gt \sigma_p^2/2$ 与本块 p379 「$Z$ 才是最重要的数」一段互为正反面。上游是 Gaussian 的二阶矩 $\int e^{-ax^2}\mathrm{d}x = \sqrt{\pi/a}$（Thomson 实分析 / 6.042J 积分技巧），不越级。
</span>

---



# 第 30 章 Efficient Monte Carlo Methods（高效的 Monte Carlo 方法）

本章讨论若干**减轻 Metropolis 方法中随机游走行为**的方法。

目的是缩短取得「实际独立」样本所需的时间。为简省起见，后文说「独立样本」时，指的都是「实际独立的样本」。

## 30.1 Hamiltonian Monte Carlo（哈密顿蒙特卡洛）

Hamiltonian Monte Carlo 方法是一种 Metropolis 方法，适用于连续 state space，它**利用梯度信息**来减少随机游走行为。

〔Hamiltonian Monte Carlo 方法在历史上原本叫 hybrid Monte Carlo（混合蒙特卡洛）。〕

对许多系统来说，其概率 $P(x)$ 可以写成

```math
P(x)=\frac{e^{-E(x)}}{Z} \qquad (30.1)
```

的形式，而且不仅 $E(x)$、连它关于 $x$ 的梯度都可以容易地求值。

在梯度可得的情况下还用简单的随机游走 Metropolis 方法，看来是**浪费**——梯度指明了应当往哪个方向走，才能找到概率更高的状态！

### Hamiltonian Monte Carlo 概览 · Overview of Hamiltonian Monte Carlo

在 Hamiltonian Monte Carlo 方法里，state space $x$ 被**动量变量（momentum variables）$p$** 扩充，而 proposer 有两类，交替使用。

第一类 proposal 把动量变量**随机化**，保持状态 $x$ 不变。

第二类 proposal 则用由下面这个 Hamiltonian（哈密顿量）所定义的模拟 Hamiltonian 动力学，同时改变 $x$ 与 $p$：

```math
H(x,p)=E(x)+K(p), \qquad (30.2)
```

其中 $K(p)$ 是「kinetic energy（动能）」，例如 $K(p) = p^{\mathsf T}p/2$。

这两类 proposal 合起来，用来产生（渐近地）来自联合密度

```math
P_H(x,p)=\frac{1}{Z_H}\exp[-H(x,p)]=\frac{1}{Z_H}\exp[-E(x)]\exp[-K(p)] \qquad (30.3)
```

的样本。

这个密度是**可分离（separable）**的，所以 $x$ 的 marginal distribution 就是我们想要的分布 $\exp[-E(x)]/Z$。

于是，只要把动量变量丢掉，我们就得到一串样本 $\{x^{(t)}\}$，它渐近地来自 $P(x)$。

<span style="color:#1e8449;">**[译注]**
(30.2)–(30.3) 里那个「separable（可分离）」一词承担了 HMC 正确性的全部重量，值得把它与第 24 章的 exact marginalization 接起来看。

$H = E(x)+K(p)$ 是**两个分别只依赖 $x$ 和 $p$ 的项之和**，于是 $\exp[-H] = e^{-E(x)}e^{-K(p)}$ 是两个单变量函数的**乘积**。对 $p$ 积分时 $e^{-E(x)}$ 是常数可以提出，剩下 $\int e^{-K(p)}\mathrm{d}p = Z_K$：

```math
P(x)=\int \mathrm{d}p\,P_H(x,p)=\frac{e^{-E(x)}}{Z_H}\int \mathrm{d}p\,e^{-K(p)}=\frac{e^{-E(x)}}{Z_H}\,Z_K=\frac{e^{-E(x)}}{Z},
```

最后一步因为 $Z_H = Z\,Z_K$。**「丢掉 $p$ 就得到 $P$」这件事只用了可分离性，别的一概不需要。**

**消失测试**：抽掉可分离性（例如取 $K(p,x) = \frac{1}{2}p^{\mathsf T}\Sigma^{-1}(x)p$ 这种依赖位置的动能，即「Riemannian HMC」），上面的积分不再能提出 $e^{-E(x)}$，边际分布**不再是** $P$；你必须引入额外的修正项（Fischer–Riemann 体积元，或 Girolami–Calderhead 的 metric 修正），否则采样目标就偏了。可观测后果：一个忘了 metric 修正的 Riemannian HMC 实现在 $N=2$、相关系数 $0.998$ 的 Gaussian 上跑 $10^{5}$ 步（即 图 30.2 那个设定），样本协方差与目标相差数个百分点以上，而这个偏差**随跑得更久不会消失**——它是系统偏差，不是噪声。

**落点**：本页 (30.2)–(30.3)；可分离性在第 24 章 exact marginalization 里是同一个工具（把联合分布拆成可积因子的乘积、积分掉不关心的那块）；图 30.2 的 $\rho = 0.998$ 例子在下一页。上游只需「乘积的积分 = 积分的乘积」（Thomson 实分析 / 6.042J），不越级。
</span>

---



<span style="background:#eaf2f8;">**算法 30.1（Algorithm）**</span> Hamiltonian Monte Carlo 方法的 Octave 源码。

```text
g = gradE(x);              # set gradient using initial x
E = findE(x);              # set objective function too
for l = 1:L                # loop L times
  p = randn(size(x));      # initial momentum is Normal(0,1)
  H = p'*p/2 + E;          # evaluate H(x,p)
  xnew = x; gnew = g;
  for tau = 1:Tau          # make Tau 'leapfrog' steps
    p = p - epsilon*gnew/2;      # make half-step in p
    xnew = xnew + epsilon*p;     # make step in x
    gnew = gradE(xnew);          # find new gradient
    p = p - epsilon*gnew/2;      # make half-step in p
  endfor
  Enew = findE(xnew);      # find new value of H
  Hnew = p'*p/2 + Enew;
  dH = Hnew - H;           # Decide whether to accept
  if (dH < 0)
    accept = 1;
  elseif (rand() < exp(-dH))
    accept = 1;
  else
    accept = 0;
  endif
  if (accept)
    g = gnew; x = xnew; E = Enew;
  endif
endfor
```

[Figure 30.2：(a,b) 用 Hamiltonian Monte Carlo 从一个相关系数 $\rho = 0.998$ 的二元 Gaussian 中产生样本。(c,d) 作为对照，在**相同计算机时间**下用简单的随机游走 Metropolis 方法。

**可复原性说明**：文字层只抽出四个面板的坐标轴刻度（$-1,-0.5,0,0.5,1$ 与 (b) 的 $-1.5,-1,-0.5,0,0.5,1$）与 `(a) (b) (c) (d)` 标签，**样本点的散点分布不可复原**，本译文不编造散点。可确证的是图注给出的对照关系：(a)(b) 是 HMC，(c)(d) 是等计算量的随机游走 Metropolis，目标分布的相关系数为 $0.998$——这正是 $\sigma_{\max}/\sigma_{\min}$ 约为 $31.6$（由 $1/\sqrt{(1-\rho)/(1+\rho)}$ 给出）的那种病态目标。]

<span style="color:#1e8449;">**[译注]**
这段 20 行代码里有**三个各自都能独立导致采样错误**的细节，而它们全都不会报错、只会让样本悄悄偏掉。

**① leapfrog 的三段式对称。** `p` 走半步 → `x` 走整步 → `p` 再走半步，两次半步用的是**不同位置的梯度**（第一次用旧的 `gnew`，第二次用新位置的 `gnew`）。这个结构叫 stagger（交错），它给了积分器两个性质：**时间可逆**（把 $\epsilon$ 换成 $-\epsilon$ 走一遍就回到原点）与**保体积**（三个子映射的 Jacobian 行列式都是 $1$，乘起来还是 $1$）。Metropolis 的接受式 $\min\{1,e^{-\Delta H}\}$ 之所以成立，正是靠这两个性质——它们是 detailed balance 的充分条件（前面 p374 的 (29.46)）。

**② 保体积为什么不能省。** 换成显式 Euler（`x += εp; p -= εg`）后 Jacobian 行列式变成 $1+\epsilon^2\mathrm{tr}\,\nabla^2E/2 \ne 1$，接受式必须**额外乘这个行列式比**；$N=1000$ 维时它按 $\exp((\epsilon^2/2)\mathrm{tr}H)$ 漂移，接受率随 $N$ 指数衰减。

**③ 动量必须每次重抽。** `p = randn(...)` 在外层、不在 `tau` 循环里，这一步才是「Gibbs 式的 $p$ 更新」，保证 $p$ 的边际恒为 $N(0,1)$。移到里面就不是 HMC 了。

**消失测试**：抽掉 ①（例如把两次半步改成「先全步 p 再全步 x」），detailed balance 破了，但样本**看起来仍然聚集在正确区域**（因为动力学方向对了），只是分布形状被系统性拉斜；在 $\rho = 0.998$ 的目标上，边缘标准差会偏大约 $2\%$——肉眼看不出，审稿人会抓。

**落点**：本页 Algorithm 30.1；接受式的正确性来自 (29.46)（p374）；$\rho=0.998$ 的对照在 图 30.2；下一块（p401 起）继续 §30.1 的正式推导。上游是 Jacobian 行列式与链式法则（Strang 线代 §5.3 行列式），不越级。
</span>

---

## 可复算验证（重建内容逐条核对）

本块所有重建的数值与结构，都可以用下面几行代码独立核对（Python 即可）：

```python
import numpy as np

# 1) Example 29.6 的 21x21 转移矩阵：行随机、列为旧状态，均匀分布不变。
n = 21
T = np.zeros((n, n))
for x in range(n):
    for xp in (x - 1, x + 1):
        if 0 <= xp <= n - 1:
            T[xp, x] += 0.5
        else:
            T[x, x] += 0.5          # 越界的提议被拒，留在原地
print(np.allclose(T.sum(axis=0), 1), np.allclose(T.sum(axis=1), 1))
# 列和为 1（行随机 = 每列和为 1，因为 T[x', x] 的第 x 列是"从 x 出发的去向"）
pi = np.ones(n) / n
print(np.allclose(pi @ T, pi), T[0, 0], T[0, 1], T[20, 19], T[20, 20])
# → True True 0.5 0.5 0.5 0.5：首行前两位、末行末两位都是 1/2，与正文重建一致

# 2) p369 的两个首达时间与 (29.32) 的量级
print(10**2, 178 / 100, 540 / 400)        # 100, 1.78, 1.35 → 同量级

# 3) p371 Gibbs 接受率恒为 1（单坐标更新）
#    只改第 i 个坐标 ⇒ x'_{-i} = x_{-i} ⇒ 两个条件密度相同 ⇒ 比值恒为 1

# 4) p373 hypercube 随机游走的特征值 ±1
for N in (1, 2, 3, 4):
    A = np.array([[bin(i ^ j).count("1") == 1 for j in range(2**N)] for i in range(2**N)], float)
    ev = np.linalg.eigvalsh(A / N)
    print(N, ev.min(), ev.max(), (np.abs(np.abs(ev) - 1) < 1e-9).sum())
# → N=1: min -1.0 max 1.0，模为 1 的特征值 2 个（+1 与 -1）⇒ 不可约但周期 2

# 5) p385 解 29.13 的方差公式：(29.60) 与 (29.62) 必须给出同一个数
sp = 1.0
for sq in (0.8, 1.0, 1.2, 1.5):
    v60 = sq / (np.sqrt(2*np.pi)*sp**2) * np.sqrt(2*np.pi / (2/sp**2 - 1/sq**2)) - 1
    v62 = (sq**2/sp**2) * ((2*sq**2 - sp**2)/sp**2)**(-0.5) - 1
    print(round(v60, 6), round(v62, 6), abs(v60 - v62) < 1e-9)
# → 两列完全相同；sq = sp 时得 0；sq → sp/sqrt(2) 时发散

# 6) p383 解 29.14（Fred 的链）的稳态分布：19 个内点各 c、2 个端点各 c/2
c = 1/20
print(c, c/2, 19*c + 2*(c/2))                         # 0.05 0.025 1.0（归一化成立）
m  = sum(i*c for i in range(1, 20)) + 20*(c/2)        # 均值 10.0（对称性保证）
m2 = sum(i*i*c for i in range(1, 20)) + 400*(c/2)     # 二阶矩 133.5
print(m, m2, m2 - m*m)                                # 10.0 133.5 33.5
print(10.0, 2870/21, 2870/21 - 100)                   # 正确分布：均值 10、E[x^2]=136.67、方差 36.67
print((36.6667 - 33.5) / 36.6667)                     # 0.0864 → Fred 的方差偏小 8.6%

# 7) p384 解 29.18 的步长与能量维
N = 1000
eps = 2.4/np.sqrt(N)                                  # 接受率 0.5 的经验值（Roberts-Gelman-Gilks）
print(eps, (1/eps)**2, np.sqrt(N/2), 0.5*N*eps**2)
# → 0.0759, 173, 22.4, 2.88

# 8) p380 的「十二个样本」
import math
print(math.sqrt(12), math.sqrt(9))                    # 3.46 > 3 ⇒ R=12 已够，R=9 是临界

# 9) p378 的译注：无平移时跨 511/512 的概率
B = 2**10
print(bin(511), bin(512), bin(511 ^ 512))             # 0b1111111111 / 0b1000000000 / 0b1111111111
# 需要 N 全为 1 才能跨越 ⇒ 随 l 减小概率归零；加随机 U 后恒为 1/2

# 10) p388 图 30.2 的 ρ=0.998 对应的条件数
rho = 0.998
lam = np.array([1 + rho, 1 - rho])
print(np.sqrt(lam.max()/lam.min()), lam.max()/lam.min())   # 31.6 与 999
```

## 原文自身问题（`†`）

1. **† p371 (29.38)**：噪声向量的记号自相矛盾——正文写 $n = (n_1, \dots, n_n, \dots, n_N)$，把**向量名 $n$** 与**下标 $n$**、以及**索引上限 $n$** 三者混用；乘积号里又同时出现 $n_n$ 与 $f_n^{\,n_n}$。按上下文（$(7,4)$ 码、$N = 7$ 比特），正确写法应是 $n = (n_1, \dots, n_N)$、乘积 $\prod_{j=1}^{N}$。本译文保留了原记号以免与 p385 的解答失联，但这处排版会让「$n_n$ 是第 $n$ 个比特」这一读法在 $N$ 与 $n$ 分不清时失效。
2. **† p384 Exercise 29.20**：正文写 partition functions $\bar Z$（抽取层显示为 `Z`），而本章其余各处 $Z$ 是**归一化常数**；在 $P = P^*/Z$ 的语境下 $Z$ 与配分函数是同一个量，但在 Ising 模型语境里「partition function」通常写成 $Z(\beta)$ 并含温度参数。此处记号未统一，含义需按上下文判断。
3. **† p377 与图 29.20**：正文说 $\sigma_q$ 从 $0.1$ 变到 $1.5$，而图的横轴刻度从 $0.2$ 起（抽出的是 $0.2, 0.4, \dots, 1.6$）。取值范围的表述与坐标轴刻度不一致，属排版层面而非结论层面的瑕疵，但按图复现实验时会偏差一个 $\sigma_q = 0.1$ 的点。
4. **（非错误，但极易误读）p369**：「到达某个端点 $T \simeq 100$」与「访问两个端点 400」用的是**两个不同的长度尺度**（$L = 10$ 与 $L_{\mathrm{full}} = 20$），原文没有明说这一点；若按同一个 $L$ 复算，会误以为作者算错了。已在本页译注中拆开说明。

## 术语表（15 条，按首现顺序）

| # | English | 中文（首现处给一次括号注） | 首现页 |
|---|---|---|---|
| 1 | random walk | 随机游走（state space 里无方向的逐步移动；本译按约定保留英文） | p369 |
| 2 | acceptance frequency / rate | 接受频率 / 接受率（proposal 被接受的比例） | p369 |
| 3 | spherical Gaussian | 球状高斯（各方向同方差的 Gaussian proposal） | p369 |
| 4 | lengthscale / separable distribution | 长度尺度 / 可分离分布（$P$ 能写成单变量因子的乘积） | p369 |
| 5 | Gibbs sampling = heat bath / Glauber dynamics | 吉布斯采样（逐坐标从条件分布抽样；三者同义） | p370 |
| 6 | conditional distribution | 条件分布（固定其余坐标后单个坐标的分布） | p370 |
| 7 | adaptive rejection sampling | 自适应拒绝抽样（要求条件分布有凸性） | p370 |
| 8 | syndrome decoding | 伴随式译码（从一个观测到的 syndrome 反推噪声向量） | p371 |
| 9 | invariant distribution | 不变分布（转移后仍是自己的分布；$T$ 的特征值 1 的特征向量） | p372 |
| 10 | ergodic / reducible / periodic set | 遍历的 / 可约的 / 周期集（三种不收敛方式：到不了、跑不遍、来回振荡） | p373 |
| 11 | base transition · mixture · concatenation | 基转移 · 混合 · 串接（构造 $T$ 的两种积木方式） | p373 |
| 12 | detailed balance / reversible | 细致平衡 / 可逆（逐对状态流量相等，$T(x_a;x_b)P(x_b) = T(x_b;x_a)P(x_a)$） | p374 |
| 13 | slice sampling · stepping out · shrinking · auxiliary variable | 切片采样 · 向外步进 · 收缩 · 辅助变量（$u$ 那根多出来的坐标） | p374–375 |
| 14 | burn in / thinning / effective sample | 预热 / 稀疏化 / 有效样本（前两者常见但前者必要、后者不必要） | p378 / p381 |
| 15 | Hamiltonian Monte Carlo · momentum · kinetic energy · leapfrog | 哈密顿蒙特卡洛 · 动量 · 动能 · 蛙跳积分器（四者本译均保留英文原词） | p387–388 |

**本块按约定一律保留英文原词的术语**（不译）：Monte Carlo、importance sampling、rejection sampling、annealed importance sampling、variational、Laplace approximation、evidence、Occam factor、likelihood、marginalization、Markov chain、Gibbs sampling、slice sampling、Metropolis–Hastings、Hamiltonian Monte Carlo、hybrid Monte Carlo、overrelaxation、simulated annealing、thermodynamic integration、umbrella sampling、reversible jump、burn in、proposal density、sampler density、acceptance rate、random walk、auxiliary variable、leapfrog、separable、ergodic、reducible、periodic、detailed balance、reversible、state space、target density、normalizing constant、partition function、hyperparameter、hierarchical model、space-filling curve、Peano curve。

## §D 降级结构表（图与不可复原内容，逐条声明）

本块共 10 张图 / 代码块，其中 1 个可完整复原、9 个只能复原结构：

| 编号 | 页 | 类型 | 复原状态 | 处理方式 |
|---|---|---|---|---|
| 图 29.13 | p370 | Gibbs 采样四面板示意图 | **几何不可复原**（只抽出 10 个标签，无曲线坐标） | 保留图注逻辑，正文补一句「每步只沿一根坐标轴移动」，不重画 |
| 图 29.14 | p372 | 8 个面板的 $p^{(t)}(x)$ 柱状图 | **柱高不可复原**（只抽出横轴刻度 $0/5/10/15/20$） | 图注保留面板顺序与 $t$ 值；补充可确证的结构（$t$ 步支撑 $\le 2t+1$） |
| 图 29.15 | p373 | 同上，初始 $x_0 = 17$ | **柱高不可复原** | 同上，并指出与 29.14 的唯一实质差异（先向右扩张） |
| 图 29.16 | p376 | slice sampling 九面板步骤图 | **几何不可复原**（只抽出步骤号标签） | 图注全文照译（它本身已足够描述逻辑）；步骤号顺序原样保留 |
| 图 29.17 | p377 | $P^*(x)$ 曲线 + 对数纵轴 | **函数形式不可复原**（只抽出刻度与 $1/10$ 轴标） | 声明三段可确证事实：对数轴、定义域 $[0,11]$、峰尾之间有谷；不编造曲线 |
| 图 29.18 | p378 | 逐次减半的区间序列 | **端点位置不可复原**（只抽出 $0$、$B-1$、$X$） | 按图注原文重建「第一次全区间、之后每次减半且含前一点」 |
| 图 29.19 | p381 | 三种 MCMC 策略的时间线 | **线与圆位置不可复原**（只抽出 `(1)(2)(3)`） | 三种策略的骨架由正文 + 图注完整给出，按文字重建 |
| 图 29.20 | p386 | 一维重要性抽样三联图 | **曲线不可复原**（抽出三组纵轴刻度与图例） | 声明轴范围与四条曲线标签；把「$\sigma_q \simeq 0.7$ 处崩落」写成可确证的结构性事实（与 (29.61) 一致） |
| 图 30.2 | p388 | HMC vs 随机游走 Metropolis 散点 | **散点不可复原**（只抽出轴刻度与面板标签） | 保留图注的对照关系与 $\rho = 0.998$；换算成 $\sigma_{\max}/\sigma_{\min}\approx 31.6$ |
| 算法 30.1 | p388 | Octave 源码 | **完整可复原** | 逐行照录，只把排印用的弯引号 `p’` 还原成 ASCII `p'`，语法与行序未改 |

**另有两处结构重建（非图）**，均已在正文标注：

1. **p372 Example 29.6 的 $21\times 21$ 转移矩阵**：文字层里是约 660 行竖排单列数字流（每个 `1/2` 与每个 `·` 各占一行，无缩进信息）。按「列为旧状态、行为新状态、每列和为 1」的判据重建为 $6\times 6$ 示意形式，用 $\ddots$ 折叠中间 15 行；首行 `1/2 1/2`、末行 `1/2 1/2`、中间行 `1/2 · 1/2` 三处元素与抽取流逐项对上（见「可复算验证」第 1 条）。
2. **p378 的伪码表格**：原文是「语句 + 右侧说明」两栏版式，抽取后说明文字与语句分离；按原顺序重排成三列表格（步号 / 语句 / 说明），语句本身逐字未改。

## 译注索引（21 条，逐条给位置、字数与消失测试对象）

| # | 页 | 主题 | 汉字 | 消失测试对象（可被判真假的失效句） |
|---|---|---|---|---|
| 1 | p369 | $100/178$、$400/540$：经验法则给量级，且两处用了两个不同的 $L$ | 336 | 把 (29.32) 当「跑 100 步就好」⇒ 低估 2–5 倍 |
| 2 | p369 | $(\sigma_{\max}/\sigma_{\min})^2 = \kappa$，就是协方差的条件数 | 293 | 只盯 acceptance rate 0.5 ⇒ 病态目标上接受率正常而混合灾难 |
| 3 | p370 | Gibbs = 恒接受 Metropolis 的两行证明 | 295 | 抽掉等价性 ⇒ 失去「收敛性免费继承」 |
| 4 | p371 | syndrome decoding 死锁：$2^K$ 个孤立点、单比特翻转落进零概率区 | 315 | 抽掉 $\mathbb{1}[Hn=z]$ ⇒ 链能移动，死锁消失 |
| 5 | p372 | (29.39) 的行列方向：$T(x';x)$ 为行 $x'$ 列 $x$，行随机 | 356 | 方向写反 ⇒ 稳态是另一个分布，直方图仍平滑 |
| 6 | p373 | 「特征值 $1$ 的个数」= 可约性，「模为 $1$」= 周期性 | 373 | 只查 $\lambda=1$ ⇒ hypercube 链被判合格，只覆盖一半状态 |
| 7 | p373 | (29.44)/(29.45) 的封闭性 ⇒ MCMC 可积木式拼装 | 295 | 抽掉封闭性 ⇒ 串接 kernel 不敢用，效率退回基线 |
| 8 | p374 | (29.46) → (29.41) 三行证明；逐点核对 vs 全局积分 | 320 | 只会 (29.41) ⇒ 必须对全体 $x$ 积分，高维不可行 |
| 9 | p375 | 辅助变量 $u$：$\int_0^{P^*}\mathrm{d}u/A = P(x)$ | 318 | 抽掉 $u$ ⇒ 必须知道 $P^*$ 上界，差 10 倍就拒绝率 $1-10^{-8}$ |
| 10 | p376 | 图 29.16 的两个分支 = detailed balance 的两个半边 | 366 | 收缩不保留 $x$ ⇒ 往返次数不对称，分布被拉斜 |
| 11 | p377 | $w$ 太小的 $O(f)$ vs $O(f^2)$；太大的 $O(\log F)$ vs $O(e^{F^2})$ | 313 | 抽掉「无拒绝」⇒ $w$ 设错 10 倍即慢 5 倍 vs 完全不动 |
| 12 | p378 | 整数 slice 的 $U$ 平移：消除 511/512 的永久边界 | 374 | 令 $U\equiv0$ ⇒ 从 512 出发跑 $10^6$ 步，左半区比例为精确 0 |
| 13 | p379 | predict / diagnose / speed up：上界理论为何没用 | 314 | 只有上界 ⇒ 在 $N=100$ 上误判「宇宙寿命」而放弃 |
| 14 | p379 | $Z$ 才是 model comparison 的核心，绕开它的代价 | 309 | 抽掉「$Z$ 是核心」⇒ 退回拟合优度，p350 的过拟合重现 |
| 15 | p380 | 「十二个样本」= $R \gt 9$，且以 $\sigma$ 而非 $\Phi$ 为基准 | 392 | 抽掉以 $\sigma$ 为基准 ⇒ 没有停止条件，两个方向都错 |
| 16 | p381 | 「不必让点独立」：无偏是边际性质，相关只吃方差 | 321 | 抽掉这句 ⇒ 照教科书做 thinning，白扔 $k$ 倍算力 |
| 17 | p383 | 解 29.14：Fred 链的稳态 $1/20$ 与 $1/40$，方差偏小 $8.6\%$ | 273 | 只记「全接受更快」⇒ 端点权重错半，二阶矩系统性偏 |
| 18 | p384 | 解 29.20：体积比 = 频率比，靠逐点 detailed balance | 370 | 抽掉逐点平衡 ⇒ 只剩无穷多解，跑出「非常确定的 1:0」 |
| 19 | p386 | 解 29.13 的相变：$\sigma_q^2 \gt \sigma_p^2/2$，经验标准差正常而真实方差无穷 | 295 | 抽掉相变 ⇒ 以样本标准差做收敛判据会给绿灯 |
| 20 | p387 | HMC 的可分离性：$\int e^{-E}e^{-K}\mathrm{d}p$ 才丢掉 $p$ 不变 | 304 | 不可分离（Riemannian HMC）⇒ 边际偏，偏差永不消失 |
| 21 | p388 | Algorithm 30.1 的三个陷阱：leapfrog 交错、保体积、动量重抽 | 385 | 破掉时间可逆 ⇒ 样本仍聚在正确区域但分布被拉斜约 $2\%$ |

（共 21 条，全部 250–400 字，每条至少含一个 $...$ 公式或一个具体数、一句可被判真假的消失测试、以及一处可点开的落点。）

### 全块最有价值的一条（#19 全文，位于 p386）

<span style="color:#1e8449;">**[译注]**
这一页是本章**唯一一次把「理论发散」与「经验看起来正常」摆在一起**的地方，它的分量值得算清楚。

$P = N(0,\sigma_p^2)$、$Q = N(0,\sigma_q^2)$ 时，权重 $w = P/Q = (\sigma_q/\sigma_p)\exp\left[-\frac{x^2}{2}\left(\frac{1}{\sigma_p^2}-\frac{1}{\sigma_q^2}\right)\right]$。取 $\sigma_q = 0.3\sigma_p$（图里那个「看起来规矩」的值），指数系数为 $\frac{1}{\sigma_p^2}\left(1 - \frac{1}{0.09}\right) = -\frac{10.1}{\sigma_p^2}$，即 $w \propto \exp(+10.1 x^2/\sigma_p^2)$——**关于 $x$ 是凸的指数**。它的二阶矩 $\int Q w^2$ 要求 $\frac{2}{\sigma_p^2}-\frac{1}{\sigma_q^2} = \frac{2-11.1}{\sigma_p^2} \lt 0$，即 $\sigma_q^2 \gt \sigma_p^2/2$ 被违反，故 $\mathbb{E}[w^2] = \infty$，同时 $\mathbb{E}[w] = 1$ 有限。

**消失测试**：如果只记住「$Q$ 越接近 $P$ 越好」这条定性准则，你会把 $\sigma_q = 0.7\sigma_p$ 当成「已经够接近」，而 (29.61) 说的是**这张图上的临界点就落在 $\sigma_q/\sigma_p = 1/\sqrt{2}\approx 0.707$ 处**，跨过去就是相变。可观测后果：$R = 10^{5}$ 个样本里只要抽到一个 $|x| \gt 4\sigma_q$ 的点，它的权重就能让整条估计曲线跳一个量级——而图 (b) 说明了最阴险的部分：**经验标准差在 $\sigma_q \simeq 0.3$ 处看起来只有 1 的量级**（因为 $10^{5}$ 个样本里最大的 $\exp(10.1x^2)$ 还没爆），于是任何基于「样本标准差」的收敛判据都会给你绿灯，而真实方差无穷。

**落点**：本页 (29.57)–(29.62) 与图 29.20；题目在 p382 的 Exercise 29.13；同类的「高维必崩」在 §29.2（p362，上一块已译）；$\sigma_q^2 \gt \sigma_p^2/2$ 与本块 p379「$Z$ 才是最重要的数」一段互为正反面。上游是 Gaussian 的二阶矩 $\int e^{-ax^2}\mathrm{d}x = \sqrt{\pi/a}$（Thomson 实分析 / 6.042J 积分技巧），不越级。
</span>

## 交付自检

- 页标记 20 个（p369 … p388 ↔ PDF p381 … p400），与 PDF 20 页一一对应（书内 = PDF − 12），逐页页眉已用 fitz 抽取比对（`29.4:` / `29.5:` / `29.6:` / `29.7:` / `29.8:` / `29.9:` / `29.10:` / `29.11:` / `29.12:` / `第 30 章` / `30 — Efficient Monte Carlo Methods` / `30.1:`）。
- 禁用记号全部为 0：dollar 号双写、反斜杠＋方括号、反斜杠 mbox、反斜杠 tag、反斜杠 middle。
- 控制字符（TAB / FF / VT / BS / NUL）计数 0；抽取阶段已清除 PyMuPDF 从矢量图缝隙与数学排版带出的 94 个控制字符。
- 自写内容一律绿色 `[译注]` 标记，未使用 remark 标记；**17 道** `[exercise]`（29.4、29.5、29.7–29.21，原文跳过 29.6）保留英文题干，每题附一行中文话题摘要。译注 **21 条**，全部 250–400 汉字，每条含公式或数 + 消失测试 + 落点。
- 矩阵 / 对齐：`bmatrix` 3 处（Example 29.6 的 $T$、(29.40) 的列向量）、`cases` 3 处（(29.33)、(29.34)、解 29.14 的 $P'$）、`aligned` 2 处（(29.35)–(29.37)、(29.47)），全部用 write 工具落盘，双反斜杠未经过 heredoc；行距一律裸双反斜杠，未使用「反斜杠 + 方括号 + 间距」那种可选行距写法（该写法全块出现 0 次，已用正则核对）。
- 图：10 个图 / 代码块逐一处理，9 个在 §D 表里声明为「几何不可复原」，1 个（算法 30.1）完整照录；每一处都写明了**可确证的结构**与**不可复原的部分**，未编造任何曲线、柱高或散点。



## §30.1 Hamiltonian Monte Carlo（续）· 细节

页眉：`30.1: Hamiltonian Monte Carlo` · 书内 p389

上接上一块 p388 的 Algorithm 30.1（也就是图 30.1 那段 Octave 源码，上一块已逐行照录）。

**第一个 proposal（提议）**可以看成一次 Gibbs sampling 更新：从 Gaussian density（高斯密度）$\exp[-K(p)]/Z_K$ 里重抽一个新的 momentum $p$。这个 proposal **永远被接受**。

在第二个、**动力学（dynamical）**的 proposal 里，momentum 变量决定状态 $x$ 往哪里走，而 $E(x)$ 的 gradient（梯度）决定 $p$ 如何变化，依据的是

```math
\dot{x} = p \qquad (30.4)
```

```math
\dot{p} = -\frac{\partial E(x)}{\partial x}. \qquad (30.5)
```

因为每个动力学 proposal 期间 $x$ 都沿着 $p$ 的方向**持续**运动，系统状态移动的距离倾向于**与计算机时间成线性关系**，而不是与它的平方根成关系。

**第二个 proposal** 按 Metropolis rule 接受。如果 Hamiltonian dynamics 的数值模拟是完美的，那么这些 proposal **每次都被接受**，因为总能量 $H(x,p)$ 是运动常数（a constant of the motion），于是 (29.31) 里的 $a$ 等于一。如果模拟不完美——比如因为有限步长——那么一部分动力学 proposal 会被拒绝。拒绝规则用到的正是 $H(x,p)$ 的变化量，模拟完美时它为零。偶发的拒绝保证我们**渐近地**得到来自所需 joint density（联合密度）$P_H(x,p)$ 的样本 $(x(t),p(t))$。

图 30.1 的源码描述的是一种 Hamiltonian Monte Carlo 方法，它用 'leapfrog' 算法在函数 `findE(x)` 上模拟动力学，而这个函数的梯度由函数 `gradE(x)` 给出（源码本身见上一块 p388，此处只作坐标）。图 30.2 展示这个算法从一个二元 Gaussian 中产生样本，该 Gaussian 的能量函数是 $E(x)=\frac{1}{2}x^{\mathsf T}Ax$，其中

```math
A = \begin{bmatrix} 250.25 & -249.75 \\ -249.75 & 250.25 \end{bmatrix}, \qquad (30.6)
```

对应的 variance–covariance matrix（方差–协方差矩阵）是

```math
\begin{bmatrix} 1 & 0.998 \\ 0.998 & 1 \end{bmatrix}. \qquad (30.7)
```

在图 30.2a 中，从箭头标出的那个状态出发，实线表示 Hamiltonian dynamics 产生的**两段连续轨迹**。方块表示这两段轨迹的**端点**。

每段轨迹由 $\tau = 19$ 个 'leapfrog' 步组成，$\epsilon = 0.055$。这些步在放大插图里用叉号标出。**每段轨迹之后，momentum 被重新随机化。** 这里两段轨迹都被接受；Hamiltonian 的误差分别只有 $+0.016$ 与 $-0.06$。

图 30.2b 展示四段轨迹怎样从一个初值收敛过来，那个初值（箭头标出）离目标分布的 typical set（典型集）并不近。每段轨迹的 $\tau$ 与 $\epsilon$ 都用均值分别为 19 与 0.055 的 uniform distribution（均匀分布）随机化。第一段轨迹把我们带到一个新状态 $(-1.5,-0.5)$，能量与初态相近。第二段轨迹恰好在一个更靠近能量地形底部的状态上结束。这里，因为 potential energy $E$ 更小，kinetic energy $K=p^2/2$ 就必然比轨迹开始时**更大**。在第三段轨迹之前重抽 momentum 时，它的 kinetic energy 变得小得多。第四段轨迹模拟完之后，

<span style="color:#1e8449;">**[译注]**
「线性而不是平方根」这半句话是全章的经济学核心，值得把它换算成一个能对比的数字。

设目标是一个标准差比 $\kappa = \sigma_{\max}/\sigma_{\min}$ 的 Gaussian。(30.7) 给出 $\rho = 0.998$，于是 $\kappa = \sqrt{(1+\rho)/(1-\rho)} = \sqrt{1.998/0.002} \approx 31.6$，条件数 $\kappa^2 \approx 10^{3}$。随机游走 Metropolis 在最优步长下每一步只走 $\sigma_{\min}$ 量级，要横穿 $31.6\,\sigma_{\min}$ 的窄方向需要约 $\kappa^2 \approx 10^{3}$ 步；而 HMC 一段轨迹只有 $\tau = 19$ 步就已跨过整个 $0.998$ 相关的长轴（图 30.2a 的实线从 $-1$ 附近走到 $+1$ 附近）。**加速度约 $10^{3}/19 \approx 50$ 倍**。

**消失测试**：抽掉「momentum 在轨迹内保持方向」这一条（例如每步都重抽 $p$，那就退化成一次普通的 random-walk Metropolis），位移立刻从 $\propto T$ 掉回 $\propto \sqrt{T}$；在 $\kappa = 31.6$ 的目标上，你要把步数从 $19$ 加到 $10^{3}$ 才等效，而每次迭代的 gradient 计算成本**并没有降**，总成本按 $\kappa^2$ 增长。

**落点**：本页 (30.4)–(30.5)；§30.1 的入口在上一块 p387；图 30.2 的 $\rho=0.998$ 与条件数换算在上一块 p388 已算过一次（$\sigma_{\max}/\sigma_{\min}\approx 31.6$），本页这段是同一句话的动力学版。上游是「$\dot x = p$ 的解是 $x(t) = x(0)+pt$」这一行一阶 ODE（Thomson 实分析 / 6.006 的线性增长 vs $\sqrt{t}$ 扩散尺度），不越级。
</span>

<span style="color:#1e8449;">**[译注]**
(30.6) 与 (30.7) **互为逆矩阵**，这不是巧合而是 $E=\frac{1}{2}x^{\mathsf T}Ax$ 的定义使然：$P(x)\propto e^{-E}$ 是协方差为 $A^{-1}$ 的 Gaussian。验一下就能确认重建没错——$\Sigma_{11}^{-1} = 1/(1-\rho^2) = 1/0.003996 = 250.2503$；$-\rho/(1-\rho^2) = -0.998\times 250.2503 = -249.7498$。两个数与 (30.6) 的 `250.25` / `−249.75` **在 4 位有效数字上完全吻合**。

**消失测试**：这是本章最容易静默失败的一处。HMC 只要求 $E$ 可微，**不检查 $A$ 与 $\Sigma$ 是否互为逆**。若把 $A$ 错写成 $\begin{bmatrix}1 & 0.998\\ 0.998 & 1\end{bmatrix}$（也就是把协方差矩阵当成了精度矩阵），HMC 会照常跑、照常给出 $100\%$ 的接受率、样本点仍然聚集在一条 $45^\circ$ 斜线上——只是这条线的标准差从 $1$ 变成 $1/\sqrt{1-0.998^2}\approx 15.8$，**大了一个数量级而没有任何报错**。审稿人看不出散点图形状哪里不对，因为形状确实对。

顺带算一下这个错法对 HMC 步长的影响：目标的最大频率是 $\omega_{\max}=\sqrt{\lambda_{\max}(A)}$。真值是 $\lambda_{\max}=250.25+249.75=500$，$\omega_{\max}=22.36$；错法下 $\lambda_{\max}=1.998$，$\omega_{\max}=1.414$。于是同一份 $\epsilon=0.055$ 的代码，在真目标上 $\epsilon\omega=1.23$（已经偏大），在错目标上只有 $0.078$——**接受率从「偶尔被拒」变成「永远接受」**，而这恰好会让人得出「我的 HMC 调得很好」的错误结论。

**落点**：本页 (30.6)–(30.7)；同一个 $\rho=0.998$ 在上一块 p388 的图 30.2 里已用过；$A=\Sigma^{-1}$ 的代数事实是 Strang 线代里的 inverse of a $2\times2$ matrix（$1/(ad-bc)$ 那条公式）；$\omega_{\max}=\sqrt{\lambda_{\max}}$ 与 $\epsilon\omega\approx1$ 这个稳定边界在本块 p402 译注里还会用到；本页的重建数值核对脚本见文末 §E 第 1 条，可直接 `python` 复算。
</span>

---



## 图 30.3：overrelaxation 与 Gibbs sampling 的对照

页眉：`390` / `30 — Efficient Monte Carlo Methods` · 书内 p390

[Figure 30.3：它演示的是什么——同样是那个 $\rho = 0.998$ 的二元 Gaussian，(a) 中 Gibbs sampling 走出锯齿状的慢随机游走，而 overrelaxation 走出沿对角线方向的**定向**前进；(b) 放大一次迭代里的两步；(c) 单看 $x_1$ 的时间序列，2000 次迭代内 Gibbs 仍在原点附近来回，overrelaxation 已经扫过整个 $[-3,3]$。]

**图注原文与译**：

> Figure 30.3. Overrelaxation contrasted with Gibbs sampling for a bivariate Gaussian with correlation $\rho = 0.998$. (a) The state sequence for 40 iterations, each iteration involving one update of both variables. The overrelaxation method had $\alpha = -0.98$. (This excessively large value is chosen to make it easy to see how the overrelaxation method reduces random walk behaviour.) The dotted line shows the contour $x^{\mathsf T}\Sigma^{-1}x = 1$. (b) Detail of (a), showing the two steps making up each iteration. (c) Time-course of the variable $x_1$ during 2000 iterations of the two methods. The overrelaxation method had $\alpha = -0.89$. (After Neal (1995).)

译文：**图 30.3.** overrelaxation 与 Gibbs sampling 的对照，目标是一个相关系数 $\rho = 0.998$ 的二元 Gaussian。(a) 40 次迭代的状态序列，每次迭代包含两个变量各更新一次。overrelaxation 方法取 $\alpha = -0.98$。（这个**过分大**的取值是为了让人一眼看出 overrelaxation 方法如何削减随机游走行为。）虚线画出等值线 $x^{\mathsf T}\Sigma^{-1}x = 1$。(b) (a) 的细节，展示组成每次迭代的**两步**。(c) 两种方法各跑 2000 次迭代期间变量 $x_1$ 的时间进程。overrelaxation 方法取 $\alpha = -0.89$。（取自 Neal (1995)。）

**可复原性说明**：文字层只抽出四个面板的坐标轴刻度（(a)(b) 的 $-1,-0.5,0,0.5,1$ 与 $-1,-0.8,-0.6,-0.4,-0.2,0$；(c) 的 $x_1$ 纵轴 $-3\ldots3$、横轴 $0\ldots2000$）与图例 `Gibbs sampling` / `Overrelaxation`。**点的连线、锯齿形状、等值线椭圆的具体长短轴比例不可复原**，本译文不编造。可确证的结构性事实有四条：① 目标 $\rho=0.998$；② (a)(b) 用 $\alpha=-0.98$、(c) 用 $\alpha=-0.89$；③ 迭代数分别为 $40$ 与 $2000$；④ 每次迭代两个变量各更新一次。

<span style="color:#1e8449;">**[译注]**
这张图是被**跨块引用**的，必须与上一块的措辞对齐：上一块 p371（PDF p383）在「Gibbs sampling 在高维」一节写过「图 30.3（p390）演示了当 $L \gg \epsilon$ 时 Gibbs sampling 那缓慢的进展」，并给出「产生一个独立样本至少需要约 $(L/\epsilon)^2$ 次迭代」。这里的**同一组数**必须能互相代入：

对二元 Gaussian，边缘标准差 $L = 1$、条件标准差 $\epsilon = \sqrt{1-\rho^2} = \sqrt{0.003996} = 0.0632$，于是 $L/\epsilon = 15.8$，$(L/\epsilon)^2 = 250.25$ —— **正好是 (30.6) 里 $A$ 的对角元**。这不是巧合：$A_{11} = 1/(1-\rho^2)$ 就是条件精度。

**消失测试**：若图注的 $\rho$ 与上一块写的 $\rho$ 不一致（例如一处 0.998、一处 0.9），$(L/\epsilon)^2$ 就从 $250$ 变成 $5.26$，图 (c) 里「2000 次迭代仍未走完」立刻变成「2000 次迭代绰绰有余」——两个结论**方向相反**。这就是跨块引用必须共用同一组数的理由。

**落点**：本页图 30.3；(30.6) 的对角元 $250.25$ 在上一页；$(L/\epsilon)^2$ 的原始出处是上一块 p371（PDF p383）的 §29.5；$\epsilon=\sqrt{1-\rho^2}$ 是二元 Gaussian 的条件方差公式（Strang 线代的条件数与 Schur 补）。$\alpha=-0.98$ 与 $-0.89$ 分属两个面板，**不可混用**：$|\alpha|$ 越接近 1，减随机游走越强，作者用 $-0.98$ 只是为了可视化。
</span>

接 p401 末尾被截断的那句：四段轨迹模拟完之后，状态看起来已经成为目标密度的典型状态。

图 30.2(c) 与 (d) 用一个 Gaussian proposal density 的 random-walk Metropolis 方法从**同一个** Gaussian 分布抽样，初值分别取 (a) 与 (b) 的初始条件。在 (c) 里步长被调到使 acceptance rate（接受率）为 **$58\%$**。proposal 数是 $38$，所以花掉的计算机时间总量与 (a) 相近。因为 random walk 行为，**移动的距离很小**。在 (d) 里用的也是 random-walk Metropolis，从与 (b) 相同的初值出发、给到相似的计算机时间。

<span style="color:#1e8449;">**[译注]**
$+0.016$ 与 $-0.06$ 这一对**反号**的数是本页最值得盯的细节：leapfrog 的 Hamiltonian 误差**有界且会振荡**，可以正、可以负，但不会随步数累积。这正是「模拟不完美却不妨碍 $100\%$ 接受率」的机制，也是 Exercise 30.11（本块 p397）为什么要专门追问「不精确但必须完美可逆」。

给一个量的界：对频率 $\omega$ 的简谐振子，leapfrog 在任意步数 $n$ 后的能量偏差满足 $|\Delta H| \le C\epsilon^2\omega^2$，$C$ 与 $n$ **无关**；而 forward Euler 的每步放大因子是 $1+\epsilon^2\omega^2$，$n$ 步后 $\Delta H \approx n\epsilon^2\omega^2$ **线性累积**。

**消失测试**：抽掉 leapfrog 的「半步–整步–半步」交错（改成先整步更新 $p$ 再整步更新 $x$），误差从有界变成指数增长；在 $\epsilon=0.055$、$\omega_{\max}=\sqrt{500.5}\approx22.36$（由 (30.6) 的 $\lambda_{\max}=250.25+249.75=500$ 给出）时，$\epsilon\omega_{\max}\approx1.23$，**一步就把能量推到发散区**，接受率从 $\approx 1$ 掉到 $e^{-\Delta H}$ 的机器零——你会看到链原地不动而误判为「已收敛」。

**落点**：本页两段轨迹的 $\tau=19$、$\epsilon=0.055$；Algorithm 30.1 在上一块 p388 已被逐行拆成三个陷阱；Exercise 30.11 在本块 p397；$\omega_{\max}=\sqrt{\lambda_{\max}(A)}$ 由 (30.6) 直接给出，见文末 §E 第 1 条脚本。
</span>

---

## §30.2 Overrelaxation

页眉：`30.2 Overrelaxation` · 书内 p390

overrelaxation（过度松弛）方法是一种**削减 Gibbs sampling 中随机游走行为**的方法。overrelaxation 最初是为「所有条件分布都是 Gaussian」的系统引入的。

一个**整体非 Gaussian、但条件分布全是 Gaussian** 的联合分布的例子是

```math
P(x,y) = \exp\left(-x^2y^2 - x^2 - y^2\right)/Z .
```

（检查一下这条断言：固定 $y$ 时指数里 $-x^2(y^2+1)$ 是 $x$ 的二次型，故 $x\mid y$ 是 Gaussian；对称地 $y\mid x$ 也是。但 $P$ 本身按 $(x^2+1)(y^2+1)-1$ 的形状展开，不是任何二元 Gaussian——四条「臂」而不是一个椭圆。§D 会说明这一点对本块图 30.3 的意义。）

---



## Gaussian 条件分布下的 overrelaxation

页眉：`30.2: Overrelaxation` · 书内 p391

在**普通的** Gibbs sampling 里，我们从当前变量 $x_i$ 的条件分布中抽出它的新值 $x_i^{(t+1)}$，**完全无视**旧值 $x_i^{(t)}$。当变量之间强相关时，状态会走出漫长的随机游走，正如图 30.3 左手面板所示。那张图用的目标密度是一个相关的 Gaussian 分布。

在 Adler (1981) 的 overrelaxation 方法里，我们改从一个**被偏置到条件分布另一侧**的 Gaussian 中抽 $x_i^{(t+1)}$。若 $x_i$ 的条件分布是 $\mathrm{Normal}(\mu,\sigma^2)$、$x_i$ 的当前值是 $x_i^{(t)}$，那么 Adler 方法把 $x_i$ 置为

```math
x_i^{(t+1)} = \mu + \alpha\left(x_i^{(t)}-\mu\right) + \left(1-\alpha^2\right)^{1/2}\sigma\,\nu, \qquad (30.8)
```

其中 $\nu\sim\mathrm{Normal}(0,1)$，$\alpha$ 是介于 $-1$ 与 $1$ 之间的参数，通常取**负值**。（若 $\alpha$ 取正值，这个方法就叫 under-relaxation（欠松弛）。）

**[exercise] Exercise 30.1.** `[2] Show that this individual transition leaves invariant the conditional distribution x_i ~ Normal(μ, σ²).`
**话题摘要**：证明 (30.8) 这个单坐标 transition 保持条件分布 $\mathrm{Normal}(\mu,\sigma^2)$ 不变——本质是算一次「线性变换 + 独立噪声」的均值与方差（答案不在本书，需自证）。

Adler 的 overrelaxation 的**一次迭代**，与 Gibbs sampling 的一次迭代一样，按 (30.8) 逐个更新每个变量。由「按某个固定顺序对全部变量做完一轮更新」所定义的 transition matrix（转移矩阵）$T(x';x)$ **不满足 detailed balance**。

刚刚描述的那个**单坐标** transition 是满足 detailed balance 的——所以整条链给出的是一个合法的抽样策略，收敛到目标密度 $P(x)$——但是当我们把各个单坐标 transition **按固定顺序**施加上去组成一条链时，整体链**不是可逆的（reversible）**。这个时间上的不对称性，正是 overrelaxation 可能有益的关键。比如说，若两个变量正相关，那么它们（在短时间尺度上）会沿着**定向**方式演化，而不是随机游走，如图 30.3 所示。这可以显著缩短获得独立样本所需的时间。

**[exercise] Exercise 30.2.** `[3] The transition matrix T(x′; x) defined by a complete update of all variables in some fixed order does not satisfy detailed balance. If the updates were in a random order, then T would be symmetric. Investigate, for the toy two-dimensional Gaussian distribution, the assertion that the advantages of overrelaxation are lost if the overrelaxed updates are made in a random order.`
**话题摘要**：把固定更新顺序改成随机顺序，$T$ 就变对称、整体链就变可逆——而作者断言此时 overrelaxation 的**全部优势消失**。要在二元 Gaussian 玩具上验证「优势来自不可逆性本身，不是来自每一步的形状」。

<span style="color:#1e8449;">**[译注]**
(30.8) 里那个 $\left(1-\alpha^2\right)^{1/2}$ 是**唯一**不能写错的地方，写错不会有任何报错，只会让分布悄悄变胖或变瘦。

验算：$x' = \mu + \alpha(x-\mu) + \sqrt{1-\alpha^2}\,\sigma\nu$，取期望得 $\mathbb{E}[x'] = \mu + \alpha(x-\mu)$，取方差得 $\mathrm{Var}(x') = \alpha^2\sigma^2 + (1-\alpha^2)\sigma^2 = \sigma^2$（**精确守恒**，与 $\alpha$ 无关）。

$\alpha \lt 0$ 时的几何：若当前值在 $\mu$ 右侧 $d$ 处，新值落在 $\mu$ 右侧 $|\alpha|d$ 处但**符号已翻到左侧方向**——当 $\alpha = -1$ 时恰好是 $-d$，即关于 $\mu$ 的**镜像反射**，方差守恒退化成「$\nu$ 项系数为零、位置完全确定」。这正是 §30.2 与 §30.4 的 leapfrog (30.13) 共用的那一个动作。

**消失测试**：$|\alpha|$ 每远离 $1$ 一点，一步的「定向程度」就掉一点；$\alpha\to0$ 时退回普通 Gibbs。可观测判据：在 $\rho=0.998$ 的目标上，$\alpha=-1$ 时 $x_1$ 的相邻两步是强负相关（锯齿），$\alpha=0$ 时是白噪声——图 30.3(c) 的锯齿状正是 $|\alpha|$ 接近 $1$ 的读数。

**消失测试**：如果误写成 $\mu + \alpha(x-\mu) + (1-\alpha)\sigma\nu$（把平方根忘了），则 $\mathrm{Var}(x') = \left[\alpha^2 + (1-\alpha)^2\right]\sigma^2$；$\alpha = -0.98$ 时括号内为 $0.9604 + 3.9204 = 4.8808$，样本方差变成目标的 **$4.88$ 倍**。可观测后果：2000 次迭代后，图 30.3(c) 的 $x_1$ 会扫到 $[-3,3]$ 之外（标准差从 $1$ 变 $2.2$），而链**照样收敛到某个东西**、照样没有报错——你会以为 overrelaxation 只是「方差大一点」。

**落点**：本页 (30.8)；Exercise 30.1 就是要你补上这段方差计算；图 30.3(c) 的 $\alpha=-0.89$ 时可算出系数 $0.7921+3.5721=4.364$（同样的错法）；上游是「独立随机变量之和的方差相加」（6.042J 期望与方差），不越级。
</span>

<span style="color:#1e8449;">**[译注]**
「整体链不可逆、但仍是合法的 MCMC」这句话在 2003 年只是解释 overrelaxation 为何有效的脚注，到今天已经长成一整条研究线（non-reversible MCMC：zig-zag sampler、bouncy particle sampler、piecewise deterministic Markov process），值得把这里的论证结构抽出来。

关键在于**保持分布不变（invariance）与可逆性（reversibility）是两件事**。若每个单坐标 kernel $T_i$ 都以 $P$ 为不变分布（即 $\int P(x)T_i(x';\mathrm{d}x) = P(x')$），那么复合 $T = T_1T_2\cdots T_N$ 也以 $P$ 为不变分布——**因为 $P$ 在经过每个因子时都没变**。而 detailed balance（$P(x)T(x';x) = P(x')T(x;x')$）要求更强的东西，它在复合下**不封闭**。

**消失测试**：如果误以为「不满足 detailed balance ⇒ 不能收敛」，你会把整个 §30.2 判为无效方法而跳过，于是在 $\rho=0.998$ 的目标上继续付 $(L/\epsilon)^2 \approx 250$ 倍的代价。反过来，如果误以为「不变性已经够，可逆性无所谓」，你会漏掉下一句：**正是不可逆**才带来定向运动，可逆的随机顺序版本（Exercise 30.2）优势**全部消失**。

**落点**：本页这段论证；detailed balance 的定义与 (29.46) 在上一块 p374；Exercise 30.2 要求你把「随机顺序 ⇒ $T$ 对称 ⇒ 优势消失」跑出来；上游是马尔可夫链的平稳分布与细致平衡（6.042J 的 Markov chain 章节 + Strang 线代里「对称矩阵特征值实」这一条），不越级。
</span>

## Ordered Overrelaxation

overrelaxation 方法被 Neal (1995) 推广了，他的 ordered overrelaxation（有序过度松弛）方法适用于**任何用得上 Gibbs sampling 的系统**。在 ordered overrelaxation 里，我们不从条件分布 $P(x_i\mid\{x_j\}_{j\neq i})$ 里只抽一个样本，而是造出 $K$ 个这样的样本 $x_i^{(1)},x_i^{(2)},\dots,x_i^{(K)}$，$K$ 可以取二十左右。通常，多造 $K-1$ 个样本给「做第一个样本所需的那批初始计算」带来的额外成本可以忽略。

这些点 $\{x_i^{(k)}\}$ 随后按数值大小排序，$x_i$ 的**当前值**被插入到这张有序表里，得到 $K+1$ 个点。我们给它们 rank（秩）$0,1,2,\dots,K$。设 $\kappa$ 是 $x_i$ 当前值在这张表里的 rank。我们把 $x_i'$ 置为**与表的另一端等距**的那个值，也就是 rank 为 $K-\kappa$ 的那个值。Adler 的 $\alpha$ 参数在这里扮演的角色由参数 $K$ 承担。当 $K=1$ 时，我们得到的就是普通的 Gibbs sampling。就实用而言，Neal 估计 ordered overrelaxation 能把一次模拟加速**十倍到二十倍**。

<span style="color:#1e8449;">**[译注]**
「rank $K-\kappa$」这个镜像规则是可以逐项验算的，而且它顺手解释了为什么 $K=1$ 必须退回 Gibbs——这两件事原文只用一句话带过。

取 $K=1$：表里只有两个点（当前值 + 一个样本），所以 $\kappa\in\{0,1\}$，而 $K-\kappa = 1-\kappa$ **恰好是另一个点的 rank**。于是无论当前值排在哪一边，输出总是「那个唯一的新样本」——这正是普通 Gibbs 的定义。

再取 $K=20$：$\kappa$ 落在 $0\ldots20$ 的 21 个位置上，输出取镜像位置，于是**当前值离分布中心越远，输出就被推得越远、越靠另一侧**——这跟 (30.8) 里 $\alpha\lt 0$ 的「偏置到另一侧」是同一个几何，只是用 rank 替代了 $z$ 分数。加速倍数的来源是：你花了 $20$ 次条件采样，换来一次「近乎定向」的大步，等效于 Gibbs 的 $10$–$20$ 步。

**消失测试**：若误写成「取 rank $\kappa+1$」（相邻而不镜像），方法仍然合法、仍然收敛，但输出与当前值强正相关，overrelaxation 效应**完全消失**，你会白花 $K$ 倍的采样成本换来与 Gibbs 相同的混合速度——而且任何收敛诊断都不会报错，因为你只是变慢了。

**落点**：本页 ordered overrelaxation 全段；$K=1$ 退回 Gibbs 一句在正文；Neal (1995) 是本节的原始出处，也是图 30.3 的出处；镜像规则与 (30.8) 的 $\alpha\lt 0$ 是同一个「反射」几何，见本页上一条译注；同类的「用秩替代数值」在 §29.7 slice sampling 的 step-out 里已出现过（上一块 p375–377）。
</span>

---



## §30.3 Simulated annealing

页眉：`30.3 Simulated annealing` · 书内 p392

第三种加速收敛的技术是 simulated annealing（模拟退火）。在 simulated annealing 里引入一个 'temperature'（温度）参数，它**大**的时候允许系统做出在温度 $1$ 下几乎不可能发生的 transition。温度被设到一个大值，然后逐渐降到 $1$。这个做法理应降低模拟**卡在一个不具代表性的概率孤岛里**的机会。

我们假定要从形如

```math
P(x) = \frac{e^{-E(x)}}{Z} \qquad (30.9)
```

的分布中抽样，其中 $E(x)$ 可以求值。在最简单的 simulated annealing 方法里，我们改为从分布

```math
P_T(x) = \frac{1}{Z(T)}e^{-E(x)/T} \qquad (30.10)
```

中抽样，并把 $T$ 逐渐降到 $1$。

能量函数**常常**可以拆成两项，

```math
E(x) = E_0(x) + E_1(x), \qquad (30.11)
```

其中第一项是 'nice' 的（例如 $x$ 的一个 separable 函数），第二项是 'nasty' 的。在这些情况下，一个更好的 simulated annealing 方法可以用分布

```math
P_T'(x) = \frac{1}{Z'(T)}e^{-E_0(x)-E_1(x)/T} \qquad (30.12)
```

并把 $T$ 逐渐降到 $1$。这样一来，高温下的分布就**退化（revert）到一个由 $E_0$ 定义的良态分布**。

simulated annealing 常常被当作**优化**方法使用，目标是要找一个 $x$ 使 $E(x)$ 最小；这种情况下温度是降到**零**而不是降到一。

作为 Monte Carlo 方法，上面描述的 simulated annealing **并不能精确地从正确的分布抽样**，因为**没有任何保证**说「掉进某个能量盆地的概率等于该盆地全部状态的总概率」。密切相关的 'simulated tempering'（模拟回火）方法（Marinari and Parisi, 1992）通过把温度本身变成一个 random variable、在模拟过程中按 Metropolis 方式更新它，来修正退火过程引入的偏置。Neal (1998) 的 'annealed importance sampling'（退火重要性抽样）方法则通过为每个生成点计算 importance weight（重要性权重）来移除退火引入的偏置。

<span style="color:#1e8449;">**[译注]**
(30.10) 与 (30.12) 的差别不是「写法不同」，而是**高温极限下链会不会乱跳**，这一点值得算清楚。

取 (30.10) 并令 $T\to\infty$：$P_T \to$ state space 上的均匀分布。于是链在高温下**在全体状态上做无记忆游走**，等你把 $T$ 降回 $1$ 时，它停在哪里与能量地形**毫无关系**——退火等于没做。(30.12) 则不同：$T\to\infty$ 时 $P_T' \propto e^{-E_0(x)}$，链停在 $E_0$ 的典型集里；而 $E_0$ 按设计是「好算、好采样」的那一半（典型例子：$E_1$ 是 $N$ 个变量的耦合项，$E_0$ 是逐变量的独立项）。于是降 $T$ 的过程变成「在保持 $E_0$ 结构的前提下逐步接入 $E_1$」。

**消失测试**：抽掉这个分离（只用 (30.10)），在 $N=100$ 的 Ising 型 $E$ 上，高温阶段每一步的能量变化都是 $O(N)$ 量级的噪声，接受率 $e^{-\Delta E/T}$ 在 $T$ 降到 $1$ 之前就已经把链钉死在某个随机构型；可观测后果是**同一份代码跑五次得到五个不同的末态，且每个末态的 $E$ 差 $O(N)$**，而你以为这叫「随机性」。

**落点**：本页 (30.9)–(30.12)；$E_0$ 的典型选择与 §30.7（本块 p397）里那个「$\beta$ 与 $\{x_n\}$ 耦合」的例子是同一套 hierarchical 结构；simulated tempering（Marinari–Parisi 1992）与 annealed importance sampling（Neal 1998）是两条修正路线；上游是「温度的倒数 $\beta$ 缩放能量」这一条统计物理约定（本块 p400 的 (31.2) 会正式引入 $\beta$），不越级。
</span>

<span style="color:#1e8449;">**[译注]**
「没有保证掉进某个盆地的概率等于该盆地总概率」这一句，是全书对 simulated annealing 最重的一句批评，而它的定量含义可以直接写出来。

设能量地形有 $B$ 个盆地，盆地 $j$ 的状态总数为 $n_j$、最低能量为 $E_j^{\min}$。**正确的**目标分布给盆地 $j$ 的概率是 $p_j \propto n_j e^{-\beta E_j^{\min}}$（$n_j$ 是熵因子）。而退火过程的动力学只让链「沿着 $E$ 下降」，它进入盆地 $j$ 的机会主要由**吸引域的边界长度**决定，与 $n_j$ **无关**。于是偏置量级是 $\left|p_j^{\text{anneal}} - p_j\right|/p_j$，在 $n_j$ 跨越几个数量级时它可以接近 $1$——**不是小偏差，是定性错误**。

**消失测试**：若用退火末态的样本去估 $\mathbb{E}[\Phi]$（这是最常见的误用），你会得到一个「干净、稳定、可重复」的数，而它与真值之差**不随样本数增大而消失**——它是系统偏置。可观测后果：把退火跑 $10$ 次取平均，标准差很小（看似收敛），但换一个随机种子族得到的均值整体平移。

**落点**：本页末段；simulated tempering 与 annealed importance sampling 两条修法在正文；「$Z$ 才是 model comparison 的核心」在上一块 p379 已立过同样的论点（绕开归一化常数就会偏）；若要一个能自测的例子，本块 p414–417 的 Ising 模型正好有两个盆地（全 $+1$ / 全 $-1$），可以拿它做消失测试的实验。
</span>

---



## §30.4 Skilling's multi-state leapfrog method

页眉：`30.4: Skilling's multi-state leapfrog method` · 书内 p393

第四种加速 Monte Carlo 模拟的方法出自 John Skilling，它的精神与 overrelaxation 相似，但**在更多维上**工作。这个方法适用于从连续 state space（状态空间）上的一个分布抽样，唯一要求是能量 $E(x)$ 容易求值。**gradient 不用。** 这个 leapfrog 方法不打算单独使用，而是与其他 Monte Carlo operator（算子）**串接**使用。

前面的所有 Monte Carlo 方法都只有一个状态向量 $x$ 在 state space 里移动；Skilling 的 leapfrog 方法则**同时维护一组 $S$ 个状态向量** $\{x^{(s)}\}$，$S$ 可能是六或者十二。目标是这 $S$ 个向量**全部**代表来自同一分布 $P(x)$ 的独立样本。

Skilling 的 leapfrog 为新的状态 $x^{(s)\prime}$ 造一个 proposal，按 Metropolis 方法接受或拒绝：它让当前状态 $x^{(s)}$ **越过**另一个状态向量 $x^{(t)}$ 做一次「跳背」，

```math
x^{(s)\prime} = x^{(t)} + \left(x^{(t)} - x^{(s)}\right) = 2x^{(t)} - x^{(s)}. \qquad (30.13)
```

所有其他状态向量留在原地，所以接受概率**只依赖 $x^{(s)}$ 的能量变化**。

哪个向量 $t$ 充当这次跳跃的**搭档**，可以有多种选法。最简单的做法是从其余向量中随机挑一个。更好的做法也许是：按某个选定的距离函数挑一个**最近邻** $x^{(t)}$——只要随后用一个能保证 detailed balance 的接受规则，即检查点 $t$ 是否仍在新点 $x^{(s)\prime}$ 的近邻之中。

## 为什么 leapfrog 是个好主意

想象目标密度 $P(x)$ 有强相关——例如这个密度是一根**针状 Gaussian**，宽度 $\epsilon$、长度 $L\epsilon$，其中 $L\gg 1$。如我们已经强调过的，用标准方法在这样的密度上移动，等于走一个缓慢的随机游走。

现在想象我们那 $S$ 个点的集合最初潜伏在一个「在该密度下概率不低、但尺寸小得不合适」的 $\epsilon$ 大小的球里。那么在 Skilling 的 leapfrog 下，典型的第一步会把点带到当前球**外面一点**，也许把它到球心的距离翻倍。等所有点都有机会动过一遍之后，球就变大了；若所有移动都被接受，球在各个维度上都会大出两倍左右。部分移动被拒，意味着装点的那只球很可能沿针的长方向被拉长了两倍左右。再让所有点轮流过一遍，球在长方向上又长两倍。于是**沿长维度走过的典型距离随迭代次数呈指数增长**。

当然，每迭代翻两倍可能偏乐观；但即便球每次只长 $1.1$ 倍，增长**仍然是指数的**。要让长维度被探索完，只需迭代次数与 $\log L/\log(1.1)$ 成正比。

**[exercise] Exercise 30.3.** `[2, p.398] Discuss how the effectiveness of Skilling's method scales with dimensionality, using a correlated N-dimensional Gaussian distribution as an example. Find an expression for the rejection probability, assuming the Markov chain is at equilibrium. Also discuss how it scales with the strength of correlation among the Gaussian variables. [Hint: Skilling's method is invariant under affine transformations, so the rejection probability at equilibrium can be found by looking at the case of a separable Gaussian.]`
**话题摘要**：用相关 $N$ 维 Gaussian 作靶子，求 equilibrium 下的 rejection probability，并讨论它与维度 $N$、与相关强度的 scaling。提示给出关键工具：方法在**仿射变换下不变**，所以只需算 separable（对角）Gaussian 那一例（解答在本块 p410，答案 $e^{-2N}$）。

这个方法与 Gilks et al. (1994) 的 'adaptive direction sampling'（自适应方向抽样）有些相似，但 leapfrog 方法更简单，并且能用在更多种类的分布上。

<span style="color:#1e8449;">**[译注]**
「指数增长」这四个字是本节的全部卖点，但它的**指数底数**与维度无关这一点才是真正反常的地方——值得把两件事分开算。

先算 $L$ 需要多少轮。若每轮把球的长度乘 $c$，从 $\epsilon$ 长到 $L\epsilon$ 需要 $c^{\,n} = L$，即 $n = \log L/\log c$。取 $L = 31.6$（上一块图 30.2 的条件数）：$c=2$ 时 $n = \log 31.6/\log 2 = 4.98$，**五轮**；$c = 1.1$ 时 $n = \log 31.6/\log 1.1 = 36.1$，**三十六轮**。对比 Gibbs 在同一个目标上的 $(L/\epsilon)^2 \approx 1000$ 次迭代，差两个数量级。

**消失测试**：抽掉「multi-state + 越过另一向量」这个结构（退化成单状态、每步随机方向），$x' = x + \delta$ 与 $x$ **独立于** $x^{(t)}$，球半径就按 $\sqrt{n}$ 而不是 $c^n$ 增长。可观测后果：跑 $37$ 轮之后尺度只到 $\sqrt{37}\approx 6.1$ 而不是 $31.6$，你会把「还差 5 倍」误判成「Skilling 方法没用」，而真实原因是 $S$ 被设成了 $1$。

**落点**：本页 (30.13) 与「指数增长」全段；$L=31.6$ 来自上一块 p388 图 30.2 的 $\rho=0.998$ 换算，本块 p402 的图 30.3 用的是同一个 $\rho$；Exercise 30.3 在本页提出、p410 给出解答；仿射不变性这条 hint 是本方法唯一比 HMC 强的地方（HMC 与 overrelaxation 都**不**仿射不变），这一点在 p410 的解答末尾被明确点出。
</span>

---



## §30.5 Monte Carlo algorithms as communication channels

页眉：`30.5 Monte Carlo algorithms as communication channels` · 书内 p394

在思考「怎样加速 Monte Carlo 方法」时，想到**正在被传递的信息**可能是个有帮助的视角。从一个分布 $P(x)$ 产生一个样本时，发生**两次**通信。

第一，从 $P(x)$ 中挑出某个特定的 $x$，必然要求**至少**消耗 $\log 1/P(x)$ 个随机比特。[回忆把 inverse arithmetic coding（逆算术编码）用作「从给定分布产生样本」的方法（§6.3）。]

第二，样本的生成把关于 $P(x)$ 的信息**从那个能求值 $P^*(x)$ 的子程序**（以及任何其他能访问 $P^*(x)$ 性质的子程序）传出来。

以 dumb Metropolis 方法为例。在 dumb Metropolis 方法里，proposal $Q(x';x)$ 与 $P(x)$ **毫无关系**。$P(x)$ 的性质只在接受那一步、也就是计算比值 $P^*(x')/P^*(x)$ 时才被用到。于是从真实分布 $P(x)$ 传向那位「对计算 $P(x)$ 性质感兴趣」的用户之间的信道，要穿过一个**瓶颈（bottleneck）**：关于 $P$ 的全部信息都由那串接受/拒绝（acceptances and rejections）传递。若把 $P(x)$ 换成另一个分布 $P_2(x)$，这个替换能产生的**唯一影响**就是那串接受/拒绝不同了。我并不知道这个关于 Monte Carlo 算法的信息论视角被多少工作用过，但我认为这是个有教益的视角：如果目标是获得关于 $P(x)$ 性质的信息，那么找出这条信息流经的信道、并**最大化信息传输率**，大概是有帮助的。

### Example 30.4：为什么经验法则是「接受率约二分之一」

<span style="color:#b03a2e;">**Example 30.4.**</span> 信息论视角给那条被广泛采纳的经验法则提供了一个简单的理由，那条法则是：dumb Metropolis 方法的参数应当调到使 acceptance rate 约为**二分之一**。

让我们把接受历史（acceptance history）——也就是那串由接受/拒绝决定组成的二元串——记作 $a$。算法跑了 $T$ 步之后学到的关于 $P(x)$ 的信息**小于或等于** $a$ 的信息量，因为关于 $P$ 的全部信息都由 $a$ 中介。而 $a$ 的信息量被 $T H_2(f)$ 上界控制，其中 $f$ 是接受率。这个「关于 $P$ 已获得信息」的界，在 $f = 1/2$ 时取到最大。

另一个对 dumb Metropolis 方法有帮助的类比是**演化**的类比。每个 proposal 从当前状态 $x$ 产生一个后代（progeny）$x'$。这两个个体随后相互竞争，Metropolis 方法用的是带噪声的「适者生存」规则。若后代 $x'$ 比父代更适（即 $P^*(x') \gt P^*(x)$，假定 $Q/Q$ 因子为一），那么后代就取代父代。生存规则也**有时**允许较不适的后代取代父代。于是关于**演化速率**的洞见可以搬到 Monte Carlo 方法上来。

**[exercise] Exercise 30.5.** `[3] Let x ∈ {0,1}^G and let P(x) be a separable distribution, P(x) = ∏_g p(x_g), with p(0) = p_0 and p(1) = p_1, for example p_1 = 0.1. Let the proposal density of a dumb Metropolis algorithm Q involve flipping a fraction m of the G bits in the state x. Analyze how long it takes for the chain to converge to the target density as a function of m. Find the optimal m and deduce how long the Metropolis method must run for. Compare the result with the results for an evolving population under natural selection found in Chapter 19.`
**话题摘要**：$G$ 个独立比特、每个以 $p_1=0.1$ 为 $1$，proposal 每次翻 $m$ 比例的比特。求收敛时间与 $m$ 的关系、最优 $m$，再与第 19 章自然选择下的演化群体对照。（原文用 $\prod_g p(x_g)$，本块 p406 的编号为 (30.14)。）

```math
P(x) = \prod_{g} p(x_g) \qquad (30.14)
```

<span style="color:#1e8449;">**[译注]**
$TH_2(f)$ 这个上界是本页唯一带数字的论证，而它的**适用边界**比结论本身更重要——原文没写，但跨过这条边就会得出相反的工程结论。

算一下：$H_2(1/2) = 1$ bit，故 $f=1/2$ 时 $T$ 步最多学到 $T$ bits，即**每步一整比特**；而 $H_2(0.9) = H_2(0.1) = 0.469$ bits，同样 $T$ 步只能学到 $0.469T$，**信息率砍掉一半还多**。

但这是**信道容量的上界**，不是混合速度的最优。现代结论是：高维 random-walk Metropolis 的最优接受率是 $0.234$（Roberts–Gelman–Gilks 1997），HMC 在其最优步长下是 $0.65$ 上下（Beskos et al. 2013），**两者都不等于 $1/2$**。

**消失测试**：若把 $f = 1/2$ 当成「最优参数」直接调进代码，在 $N=100$ 维的目标上你会把步长调成最优值的 $1.5$ 到 $2$ 倍；可观测后果是每步的 $\Delta E$ 变大、接受串的 $1$ bit 里混进更多「这次拒绝是因为运气不好」的噪声，**有效样本数反而下降约 $20\%$**。上界最大点 ≠ 效率最大点，这是两个不同的泛函。

**落点**：本页 Example 30.4；$H_2$ 的定义与算术编码在 §6.3；上一块 p374 的 (29.46) 给出接受概率的正确形式；$0.234$ 与 $0.65$ 两个数不在本书，属于 2003 年之后的结果，此处只作坐标标记，第 30 章正文不再回来读。
</span>

---



页眉：`30.6: Multi-state methods` · 书内 p395

（上页 Exercise 30.5 的题干在此续完。原文在 p406/p407 交界处断行，断点落在 `…how long it takes for the chain to` / `converge to the target density…` 之间；本译文已在上页给出完整题干，此处不重复。）

「标准 Metropolis 方法在信息意义上能取得的最快进展约为**每迭代一比特**」这个洞见，为「加速算法」提供了很强的动机。本章已经回顾了好几种削减随机游走行为的方法。这些方法是否**也**提高了信息获取的速率？

**[exercise] Exercise 30.6.** `[4] Does Gibbs sampling, which is a smart Metropolis method whose proposal distributions do depend on P(x), allow information about P(x) to leak out at a rate faster than one bit per iteration? Find toy examples in which this question can be precisely investigated.`
**话题摘要**：Gibbs sampling 是 proposal 依赖 $P(x)$ 的 **smart** Metropolis 方法；它能否让信息以**快于每迭代一比特**的速率漏出？要给出能精确验证这个问题的玩具例子。

**[exercise] Exercise 30.7.** `[4] Hamiltonian Monte Carlo is another smart Metropolis method in which the proposal distributions depend on P(x). Can Hamiltonian Monte Carlo extract information about P(x) at a rate faster than one bit per iteration?`
**话题摘要**：HMC 也是 proposal 依赖 $P(x)$ 的 smart 方法。同一个问题：它能快于每迭代一比特吗？

**[exercise] Exercise 30.8.** `[5] In importance sampling, the weight w_r = P*(x^(r))/Q*(x^(r)), a floating-point number, is computed and retained until the end of the computation. In contrast, in the dumb Metropolis method, the ratio a = P*(x′)/P*(x) is reduced to a single bit ('is a bigger than or smaller than the random number u?'). Thus in principle importance sampling preserves more information about P* than does dumb Metropolis. Can you find a toy example in which this extra information does indeed lead to faster convergence of importance sampling than Metropolis? Can you design a Markov chain Monte Carlo algorithm that moves around adaptively, like a Metropolis method, and that retains more useful information about the value of P*, like importance sampling?`
**话题摘要**：importance sampling 把权重 $w_r$ 当浮点数**全程保留**，而 dumb Metropolis 把比值 $a$ 压成**一个比特**（「$a$ 比随机数 $u$ 大还是小？」）。问：这份多出来的信息是否真能换来更快收敛？能否设计一种既像 Metropolis 那样自适应移动、又像 importance sampling 那样保留更多 $P^*$ 信息的链？

<span style="color:#1e8449;">**[译注]**
Exercise 30.6 与 30.7 问的是同一件事，而**答案恰恰暴露了 §30.5 那个瓶颈论证的适用范围**：能，而且理由不是「算法更好」，是**信道换了**。

dumb Metropolis 的信道是接受串 $a\in\{0,1\}^T$，所以上界是 $TH_2(f) \le T$ bits。而 Gibbs 的一次更新输出的是 $x_i^{(t+1)}$ 本身——一个**连续随机变量**，它的信息量是无穷多比特（严格说，是以精度为界的 $O(\log(1/\delta))$）。在 $x_1,x_2$ 都是 $\mathrm{Normal}(0,1)$ 的玩具例上算一下：一步 Gibbs 后样本的条件标准差是 $\sqrt{1-\rho^2} = 0.0632$（$\rho=0.998$），于是在 $[-1,1]$ 上可分辨的区间数是 $2/0.0632 \approx 31.6$，即一步泄漏 $\log_2 31.6 \approx 4.98$ bits。**一步近五比特，远超一比特。**

**消失测试**：若把「信道 = 接受串」这个视角当成普适定律，结论就是「所有 MCMC 都被 $1$ bit/迭代卡死」，于是 smart proposal 的研究（HMC、slice、Riemannian HMC）在纸面上都不值一做——而图 30.2 已经用 $38$ 次 proposal 对 $19$ 步的实验把这条推断否掉。可观测的判据很干脆：**数接受串的比特**只对 dumb 方法有意义；对恒接受的 Gibbs，接受串全是 $1$，熵为零。

**落点**：本页三道习题；瓶颈论证在上页 §30.5 全段；$H_2(f)\le 1$ 的上界在上页 Example 30.4；$\sqrt{1-\rho^2}=0.0632$ 与 $\rho=0.998$ 在本块 p402 图 30.3 的译注里已算过；上游是「连续随机变量的微分熵可以任意大」（信息论第 1 章 + Thomson 实分析的积分），不越级。
</span>

## §30.6 Multi-state methods

页眉：`30.6 Multi-state methods` · 书内 p395

在 multi-state（多状态）方法里，我们**维护多个**参数向量 $x$；它们各自在 Metropolis、Gibbs 之类的 move 下独立演化；向量之间**还有相互作用**。意图有两种：要么最终所有向量 $x$ 都成为来自 $P(x)$ 的样本（如 Skilling 的 leapfrog 方法所示），要么「与最终那批 $x$ 相关联的信息」允许我们逼近 $P(x)$ 下的期望，如 importance sampling 那样。

### 遗传方法 · Genetic methods

遗传算法（genetic algorithms）的支持者**不常**把它们描述成 Monte Carlo 算法，但我认为这才是正确的归类；而一个**理想的**遗传算法，应当能被证明是收敛到某个指定密度的合法 Monte Carlo 算法。

第 19 章里我们注意到，一个由 $N$ 个个体组成的演化群体，若个体之间进行**有性生殖**，演化进展可以更快。这个观察促使我们去考察「多个参数向量 $x$ 一起演化并相互作用」的 Monte Carlo 算法。

---



页眉：`396` / `30 — Efficient Monte Carlo Methods` · 书内 p396

我用 $R$ 表示群体中向量的个数。我们的目标是让 $P^*(\{x^{(r)}\}_1^R) = \prod_r P^*(x^{(r)})$。一个遗传算法包含两到三种 move。

**第一，个体 move**：扰动一个状态向量，$x^{(r)} \to x^{(r)\prime}$，这可以用我们到目前为止提到的任何 Monte Carlo 方法来做。

**第二，crossover（交叉）move**，形如 $x,y \to x',y'$；在典型的 crossover 里，后代 $x'$ 的状态向量一半来自一个亲本 $x$、一半来自另一个亲本 $y$；**遗传算法成功的秘密**在于：参数 $x$ 的编码方式必须使得「两个独立状态 $x$ 与 $y$（两者都有好的适应度 $P^*$）的 crossover」有**相当大的机会**产生同样适应的后代。这个约束在很多问题里都很难满足——这正是遗传算法**主要被谈论和吹捧、却很少被严肃专家真正使用**的原因。

在引入了 $x,y \to x',y'$ 这个 crossover move 之后，我们需要选一个接受规则。取得一个合法算法的一条简便途径是：用 Metropolis 规则、以 $P^*(\{x^{(r)}\}_1^R)$ 为目标密度来接受或拒绝 crossover proposal——这要用比值

```math
\frac{P^*(x')\,P^*(y')}{P^*(x)\,P^*(y)} \qquad (30.15)
```

来比较 crossover 前后的适应度。若 crossover 算子是可逆的，那么我们就有了一个简便的证明：这个过程满足 detailed balance，因此是「收敛到 $P^*(\{x^{(r)}\}_1^R)$ 的链」中的一个合法组件。

**[exercise] Exercise 30.9.** `[3] Discuss whether the above two operators, individual variation and crossover with the Metropolis acceptance rule, will give a more efficient Monte Carlo method than a standard method with only one state vector and no crossover.`
**话题摘要**：上面这两个算子（个体变异 + 带 Metropolis 接受规则的 crossover）会不会比「只有单个状态向量、无 crossover」的标准方法更高效？

第 19 章里，性群体能比无性群体更快获取信息，原因是：crossover 操作产生了标准差为 $\sqrt{G}$ 的多样性，于是「盲眼钟表匠（Blind Watchmaker）」能够通过**淘汰**较不适的后代来传递大量关于适应度函数的信息。上面这两个算子**并不能**带来相对标准 Monte Carlo 方法的 $\sqrt{G}$ 加速，因为**这里没有淘汰（killing）**。要取得加速，需要两样东西：**增殖（multiplication）与死亡（death）**；而且至少其中之一必须是**有选择性的**。要么我们必须淘汰掉较不适的状态向量，要么我们必须让较适的状态向量产生更多后代。这些想法**勾勒起来容易，要定义一个合法的做法却很难**。

**[exercise] Exercise 30.10.** `[5] Design a birth rule and a death rule such that the chain converges to P*({x^(r)}_1^R).`
**话题摘要**：设计一条 birth rule（出生规则）与一条 death rule（死亡规则），使得整条链收敛到 $P^*(\{x^{(r)}\}_1^R)$。

我认为这**至今仍是一个未解决的研究问题**。

### 粒子滤波 · Particle filters

particle filter（粒子滤波）在涉及时序跟踪（temporal tracking）的推断问题中特别流行，它是把 importance sampling 与 Markov chain Monte Carlo 两种思想**混合**起来的多状态方法。见 Isard and Blake (1996)、Isard and Blake (1998)、Berzuini et al. (1997)、Berzuini and Gilks (2001)、Doucet et al. (2001)。

<span style="color:#1e8449;">**[译注]**
「因为这里没有淘汰」这半句把第 19 章与本章的差距定位得非常精确，值得把 $\sqrt{G}$ 的来源与消失点一起算出来。

第 19 章的 $\sqrt{G}$ 加速链条是这样的：crossover 把两个独立好个体的 $G$ 个位点混合，后代在每一位上独立地「猜对」概率 $p$，于是后代群体携带的**信息量**正比于 $G$，而群体中最好的那个个体的适应度偏离均值约 $\sqrt{G}$ 个标准差——选择（killing）把这批 $\sqrt{G}$ 的偏移**读出**成群体均值的推进。$G=1000$ 时 $\sqrt{G} = 31.6$，即每一代可以推进 $31.6$ 个「单位」。

**消失测试**：拿掉 killing，只剩「Metropolis 接受/拒绝」。此时 $x$ 与 $y$ 的 crossover 被**对称地**接受或拒绝，被拒的后代不消失、被接受的后代也不排挤谁，群体里 $R$ 个向量的地位完全平等。于是每个向量等价于一条**独立的**单链——$R$ 条链各跑各的，总信息增益是 $R$ 倍而不是 $R\sqrt{G}$ 倍。可观测后果：跑 $10^{4}$ 代之后，群体适应度的分布与「把同一条 Metropolis 链复制 $R$ 份」的直方图**逐 bin 相同**，crossover 完全没起作用——而这个负结果不会触发任何断言或警告。

**落点**：本页 (30.15) 与「没有淘汰」一段；Exercise 30.9 就是要你说出这个负结果、Exercise 30.10 是那个至今开放的正结果；$\sqrt{G}$ 与 Blind Watchmaker 在第 19 章；粒子的流行度与 `temporal tracking` 的应用面在下一段；上游是「$G$ 个独立二元变量的和的标准差是 $\sqrt{G}$」（6.042J 方差 + 二项分布），不越级。
</span>

---



## §30.7 Methods that do not necessarily help

页眉：`30.7: Methods that do not necessarily help` · 书内 p397

为一个特定的 Markov chain 使用**许多初始条件**是常见的做法（图 29.19）。如果你担心从复杂密度 $P(x)$ 中抽不好样，那么「让初始点在整个 state space 上**分布良好**」，能不能保证模拟产生的状态也良好地分布在 $P(x)$ 的 typical set 周围？

答案是：**可惜不能。**

比如在 hierarchical Bayesian model（分层贝叶斯模型）里，大量参数 $\{x_n\}$ 可能通过另一个参数 $\beta$（称为 hyperparameter（超参数））耦合在一起。例如，$\{x_n\}$ 可以是独立的噪声信号，$\beta$ 可以是噪声源的 inverse-variance（逆方差）。$\beta$ 与 $\{x_n\}$ 的联合分布可能是

```math
P(\beta,\{x_n\}) = P(\beta)\prod_{n=1}^{N}P(x_n\mid\beta) = P(\beta)\prod_{n=1}^{N}\frac{1}{Z(\beta)}e^{-\beta x_n^2/2},
```

其中 $Z(\beta) = \sqrt{2\pi/\beta}$，而 $P(\beta)$ 是一个宽分布，用来描述我们**对噪声水平有多无知**。为简单起见，把所有其他变量——数据之类、真实问题里可能牵涉到的——都略去。让我们设想：想用 Gibbs sampling 从 $P(\beta,\{x_n\})$ 中有效地抽样——先由条件分布 $P(\beta\mid x_n)$ 抽 $\beta$，再由各自的条件分布 $P(x_n\mid\beta)$ 抽所有 $x_n$。[由此得到的 $\beta$ 的边缘分布应当渐近地就是那个宽分布 $P(\beta)$。]

若 $N$ 很大，那么给定 $\{x_n\}$ 的**任何**具体取值，$\beta$ 的条件分布都会**紧紧集中**在某个最可能的值上，其宽度正比于 $1/\sqrt{N}$。于是，沿 $\beta$ 轴上下移动就成了一次缓慢的随机游走，步长 $\propto 1/\sqrt{N}$。

那么，回到初始化策略。我们能否用「散布到整个 state space」的初始条件来绕开这个缓慢收敛问题？**可惜不能。** 如果我们把点 $\{x_n\}$ 铺得很开，实际做的事就是**偏好一个很大的初始噪声水平 $1/\beta$**。于是，在第一次由 $P(\beta\mid x_n)$ 抽完 $\beta$ 之后，$\beta$ 的随机游走**总是**从 $\beta$ 轴的一端出发。

### Further reading

Hamiltonian Monte Carlo 方法（Duane et al., 1987）在 Neal (1993b) 中有综述。那本出色的巨著还综述了大量其他 Monte Carlo 方法，包括 simulated annealing 与 free energy estimation（自由能估计）等相关主题。

## §30.8 Further exercises

**[exercise] Exercise 30.11.** `[4] An important detail of the Hamiltonian Monte Carlo method is that the simulation of the Hamiltonian dynamics, while it may be inaccurate, must be perfectly reversible, in the sense that if the initial condition (x, p) goes to (x′, p′), then the same simulator must take (x′, −p′) to (x, −p), and the inaccurate dynamics must conserve state-space volume. [The leapfrog method in algorithm 30.1 satisfies these rules.] Explain why these rules must be satisfied and create an example illustrating the problems that arise if they are not.`
**话题摘要**：HMC 的动力学模拟**可以不精确，但必须完美可逆**：$(x,p)\to(x',p')$ 蕴含 $(x',-p')\to(x,-p)$，并且不精确的动力学必须**保 state-space 体积**。（Algorithm 30.1 的 leapfrog 满足这两条。）解释为什么必须满足，并造一个「不满足时出什么错」的例子（这一条正是上一块 p388 拆过的三个陷阱的**正式习题化**）。

<span style="color:#1e8449;">**[译注]**
这一页是全书对「多初值能不能救」回答得最干脆的一处，而且它给出的数是可以拿来设计诊断的。

算 $\beta$ 的条件宽度。$\beta$ 的似然是 $\prod_n Z(\beta)^{-1}e^{-\beta x_n^2/2} \propto \beta^{N/2}\exp\left(-\frac{\beta}{2}\sum_n x_n^2\right)$，即 $\mathrm{Gamma}$ 形，均值与标准差都 $\sim N/\sum x_n^2$，相对宽度 $1/\sqrt{N}$。取 $N=100$：条件宽度是均值的 $10\%$；取 $N=10^{4}$：$1\%$。要让 $\beta$ 沿轴走「一个单位」（比如从 $0.1$ 走到 $10$，两个数量级），随机游走需要的步数是 $(1/\text{width})^2$ 量级——$N=10^{4}$ 时约 $10^{4}$ 次 Gibbs 迭代，而每次迭代要扫 $N=10^{4}$ 个 $x_n$，总计 $10^{8}$ 次求值。**这就是 Neal's funnel（漏斗）**，也是 2010 年代 Stan / NUTS 最经典的失败案例。

**消失测试**：抽掉 $\beta$ 与 $\{x_n\}$ 的耦合（每个 $x_n$ 自带方差），funnel 立刻消失，Gibbs 一步到位；可观测后果是同一个模型在「共享 $\beta$」版本上跑 $10^{6}$ 步仍报 $\hat R \gt 1.1$，而在「各自方差」版本上跑 $10^{3}$ 步就 $\hat R \approx 1.0$——差别不在算法而在**参数化**。

**落点**：本页 $\beta$ 段全段；「多初值无效」的机制在本页最后两句（铺开 $\{x_n\}$ ⇔ 偏好大 $1/\beta$ ⇔ 从 $\beta$ 轴一端出发）；图 29.19 的多初值策略在上一块 p381；图 29.17 的「峰尾之间有谷」在上一块 p377 已作为不可复原图声明过；上游是 Gamma 分布的相对宽度 $\propto 1/\sqrt{N}$（6.042J 方差 + 中心极限定理的量级），不越级。
</span>

---



页眉：`398` / `30 — Efficient Monte Carlo Methods` · 书内 p398

**[exercise] Exercise 30.12.** `[4] A multi-state idea for slice sampling. Investigate the following multi-state method for slice sampling. As in Skilling's multi-state leapfrog method (section 30.4), maintain a set of S state vectors {x^(s)}. Update one state vector x^(s) by one-dimensional slice sampling in a direction y determined by picking two other state vectors x^(v) and x^(w) at random and setting y = x^(v) − x^(w). Investigate this method on toy problems such as a highly-correlated multivariate Gaussian distribution. Bear in mind that if S − 1 is smaller than the number of dimensions N then this method will not be ergodic by itself, so it may need to be mixed with other methods. Are there classes of problems that are better solved by this slice-sampling method than by the standard methods for picking y such as cycling through the coordinate axes or picking u at random from a Gaussian distribution?`
**话题摘要**：把 multi-state 思想搬进 slice sampling——维护 $S$ 个向量，用另外两个向量之差 $y = x^{(v)} - x^{(w)}$ 定方向 $y$，沿 $y$ 做一维 slice sampling。要注意 $S-1 \lt N$ 时方法**自身不遍历**，须与其他方法混合。问：有没有哪类问题比「轮换坐标轴」或「从 Gaussian 随机取 $u$」这些标准取方向法更好？

## §30.9 Solutions

页眉：`30.9 Solutions` · 书内 p398

### 习题 30.3 的解答（原题在 p393）

**Solution to exercise 30.3 (p.393).** 考虑**球状** Gaussian 分布，所有分量均值为零、方差为一。在一维情形下，也就是第 $n$ 维，若 $x_n^{(1)}$ 越过 $x_n^{(2)}$ 跳背，我们得到提议的坐标

```math
\left(x_n^{(1)}\right)' = 2x_n^{(2)} - x_n^{(1)}. \qquad (30.16)
```

假定 $x_n^{(1)}$ 与 $x_n^{(2)}$ 都是来自 $\mathrm{Normal}(0,1)$ 的 Gaussian 随机变量，那么 $\left(x_n^{(1)}\right)'$ 是来自 $\mathrm{Normal}(0,\sigma^2)$ 的 Gaussian，其中 $\sigma^2 = 2^2 + (-1)^2 = 5$。这一维贡献的能量变化将是

```math
\frac{1}{2}\left[\left(2x_n^{(2)} - x_n^{(1)}\right)^2 - \left(x_n^{(1)}\right)^2\right] = 2\left(x_n^{(2)}\right)^2 - 2x_n^{(2)}x_n^{(1)}, \qquad (30.17)
```

所以能量的典型变化是 $2\left\langle\left(x_n^{(2)}\right)^2\right\rangle = 2$。这个**正的**变化是坏消息。在 $N$ 维中，处于 equilibrium 时做一次 leapfrog move 所导致的能量典型变化因此是 $+2N$。该 move 被接受的概率大致是

```math
e^{-2N}. \qquad (30.18)
```

这意味着，如所描述的 Skilling 方法**在高维问题上并不有效**——至少，一旦收敛发生之后就不有效。不过它有一个令人印象深刻的优点：**它的收敛性质与变量之间相关性的强弱无关**——这一点连 Hamiltonian Monte Carlo 与 overrelaxation 方法都做不到。

<span style="color:#1e8449;">**[译注]**
$e^{-2N}$ 这个式子值得把 $\sigma^2 = 5$ 与「典型变化 $=2$」两处都拆开验一遍，因为它是全章唯一一个**因为维度而彻底失效**的结论。

先验 $\sigma^2$：$x' = 2x^{(2)} - x^{(1)}$，两个独立 $\mathrm{Normal}(0,1)$ 之线性组合的方差是 $2^2\cdot 1 + (-1)^2\cdot 1 = 5$。✓ 再验 $\Delta E$：$\frac{1}{2}\left[(2a-b)^2 - b^2\right] = \frac{1}{2}\left[4a^2 - 4ab + b^2 - b^2\right] = 2a^2 - 2ab$。✓ 取期望，$\mathbb{E}[2a^2] = 2$、$\mathbb{E}[2ab] = 0$，故典型变化 $+2$。✓

于是 $N$ 维累加得 $+2N$，接受率 $\approx e^{-2N}$：$N=1$ 时 $0.135$，$N=3$ 时 $2.5\times10^{-3}$，$N=10$ 时 $2.06\times10^{-9}$，$N=100$ 时 $1.38\times10^{-87}$。**十维以上就等于全拒。**

**消失测试**：注意作者把「典型变化」直接代进了 $e^{-\Delta E}$，严格说 $\mathbb{E}[e^{-\Delta E}] \ne e^{-\mathbb{E}[\Delta E]}$（Jensen 给出 $\mathbb{E}[e^{-\Delta E}] \ge e^{-2N}$，即真实接受率**略高于**此值），但这个差别在 $N=10$ 时不足以救回任何东西——所以结论稳健，而**写法是近似的**（已在 §F 标为原文问题）。若抽掉「球状」这个前提（目标各向异性），$\sigma^2$ 不再是常数，$2N$ 要换成 $\sum_n \lambda_n$ 的形式，界就松了——但 Skilling 方法的仿射不变性保证换完后**接受率不变**，这正是作者强调的那个优点。

**落点**：本页 (30.16)–(30.18)；原题在 p393（本块 p405）并附了「仿射不变」的 hint；对照实验是本块 p402 图 30.3 那个 $\rho=0.998$ 的二元 Gaussian（$N=2$ 时 $e^{-4}=0.018$，**二维就已经很难用**）；上游是线性组合的方差与 $\mathbb{E}[x^2]=\sigma^2$（6.042J），不越级。
</span>

---



## 关于第 31 章 · About Chapter 31

页眉：`About Chapter 31` · 书内 p399

我们即将遇到的一些神经网络模型与 Ising model（伊辛模型）有关，后者是理想化的磁性系统。要理解这些神经网络，**并不**必须懂 Ising model 的统计物理，但我希望你会觉得它有帮助。

Ising model 还与本书另外几个主题相关。我们将用第 25 章引入的那类**基于树的精确计算方法**来求 Ising model 中感兴趣的性质。Ising model 为二值图像提供了粗糙的模型。而 Ising model 与**二维受约束信道（two-dimensional constrained channels）**相关（参见第 17 章）：一个二维条形码，其中黑点不可以被黑点完全包围、白点不可以被白点完全包围，这类似于**低温下的反铁磁 Ising model**。求这个 Ising model 的熵，**等价于**求这个受约束信道传输比特的 capacity（容量）。

如果你想温习统计物理与热力学，可能会觉得附录 B 有帮助。我也推荐 Reif (1965) 那本书。

<span style="color:#1e8449;">**[译注]**
「求 Ising 的熵 = 求信道的 capacity」这句话把第 17 章与第 31 章缝在一起，缝线是一个**每点比特数**的换算，值得把它写成等式。

受约束信道的 capacity 定义为单位长度（这里是单位**点数**）能承载的比特数 $C = \lim_{N\to\infty} S_N/N$，其中 $S_N = \ln(\text{合法构型数})$，用 nats 计，于是 $C_{\text{bits}} = S_N/(N\ln 2)$。而 Ising 的熵由 (31.15) 给出 $S = \ln Z + \beta\bar E$，在 $\beta\to\infty$（低温）时它趋于**基态简并度的对数**——对反铁磁棋盘格这是 $\ln 2$，即每点 $1$ bit。中间温度下的 $S(T)$ 才是「这个约束允许多少比特」的答案。

**消失测试**：抽掉这层等同，你会把「Ising 的配分函数」与「信道的容量」当成两个不相干的问题，于是一边用 Monte Carlo 求 $S(T)$、一边用 transfer matrix 求 capacity，**重复劳动且结果无法互校**。可观测后果：本块 p419 的 §31.2 用 transfer matrix 求 $Z$，而 $Z$ 的宽度指数 $2^W$ 与第 17 章 transfer matrix 的 $2^W$ 是**同一个矩阵**，参数只是 $\beta$ 与 $J$ 的映射；不做这个等同就不会发现代码可以复用。

**落点**：本页第 3 段；受约束信道的定义与 capacity 在第 17 章；$S = \ln Z+\beta\bar E$ 是 (31.15)（本块 p413 的 Exercise 31.1 要你证）；$S_N/N$ 的极限存在性靠次可加性（6.042J 的 subadditive 论证），不越级。
</span>

---



## 第 31 章 Ising Models

页眉：`31 Ising Models` · 书内 p400

Ising model 是一组 spin（自旋，例如能取 $\pm 1$ 两种状态的原子），它们彼此磁耦合。若一个 spin 处于（比如）$+1$ 态，那么对**铁磁（ferromagnetic）**模型，它的**紧邻**处于**相同**态在能量上是有利的；而对**反铁磁（antiferromagnet）**，则处于**相反**态才有能量优势。本章讨论研究 Ising model 的两种计算技术。

设一个含 $N$ 个 spin 的 Ising model 的状态为向量 $x$，其每个分量 $x_n$ 取 $-1$ 或 $+1$。若两个 spin $m$ 与 $n$ 是邻居，我们记 $(m,n)\in\mathcal{N}$。相邻 spin 之间的 coupling（耦合）是 $J$。我们定义：$m$ 与 $n$ 相邻时 $J_{mn}=J$，否则 $J_{mn}=0$。状态 $x$ 的能量是

```math
E(x;J,H) = -\left[\frac{1}{2}\sum_{m,n}J_{mn}x_mx_n + \sum_{n}Hx_n\right], \qquad (31.1)
```

其中 $H$ 是外加场（applied field）。若 $J \gt 0$ 则模型是铁磁的，若 $J \lt 0$ 则是反铁磁的。我们之所以放上那个 $\frac{1}{2}$ 因子，是因为第一重求和里每一对都被数了**两次**——一次作为 $(m,n)$、一次作为 $(n,m)$。在温度 $T$ 下处于 equilibrium（平衡）时，状态为 $x$ 的概率是

```math
P(x\mid\beta,J,H) = \frac{1}{Z(\beta,J,H)}\exp\left[-\beta E(x;J,H)\right], \qquad (31.2)
```

其中 $\beta = 1/k_BT$，$k_B$ 是 Boltzmann 常数，而

```math
Z(\beta,J,H) \equiv \sum_{x}\exp\left[-\beta E(x;J,H)\right]. \qquad (31.3)
```

### Ising model 的相关性 · Relevance of Ising models

Ising model 有三重相关性。

**第一**，Ising model 重要，首先是作为**有相变（phase transition）**的磁性系统的模型。统计物理里的普适性（universality）理论表明：所有具有相同维数（这里是二维）、相同对称性的系统，其临界性质是等价的，也就是说它们相变所呈现的 scaling law（标度律）完全相同。所以研究 Ising model 不仅让我们知道磁性相变，也知道许多其他系统里的相变。

**第二**，若把能量函数推广成

```math
E(x;J,h) = -\left[\frac{1}{2}\sum_{m,n}J_{mn}x_mx_n + \sum_{n}h_nx_n\right], \qquad (31.4)
```

其中 couplings $J_{mn}$ 与外加场 $h_n$ **都不是常数**，我们得到一族模型，物理学家称之为 'spin glass'（自旋玻璃），而神经网络界称之为 'Hopfield network' 或 'Boltzmann machine'。在有些这类模型里，所有 spin 都被宣布为彼此的邻居；这种情况下物理学家把系统叫 'infinite-range'（无限程）spin glass，而网络界把它叫 'fully connected'（全连接）网络。

**第三**，Ising model 本身作为一种统计模型也是有用的。本章我们将用**两种不同的计算技术**来研究 Ising model。

<span style="color:#1e8449;">**[译注]**
(31.1) 那个 $\frac{1}{2}$ 与 (31.2) 那个 $\beta$ 各承担一件事，混起来就会把「每自旋能量」算错一倍——而这两个数在本书后面每一页都会出现。

先数 $\frac{1}{2}$。二维方格的每自旋有 $z=4$ 个邻居，键（bond）总数是 $Nz/2 = 2N$。而 $\sum_{m,n}J_{mn}x_mx_n$ 里每个键被数**两次**，共 $2\cdot 2N = 4N$ 项，乘 $\frac{1}{2}$ 后回到 $2N$ 项。全 $+1$ 态、$J=1$、$H=0$ 时每项为 $1$，故 $E = -2N$，**每自旋 $-2$**（这正是本块 p415 用的那个数）。

再看 $\beta$ 的位置。$\beta$ 只出现在 $e^{-\beta E}$ 里，它**等于**把 $E$ 整体乘一个标量。所以「$J$ 与 $H$ 的值」与「$T$ 的值」不是独立的两个旋钮：$J\to 2J$ 与 $T\to T/2$ 给出**同一个** $P(x)$。

**消失测试**：若把 $\frac{1}{2}$ 丢了（直接写 $-\sum_{m,n}J_{mn}x_mx_n$），每自旋基态能量从 $-2$ 变成 $-4$，$T_c$ 也跟着偏一倍；可观测后果是本块 p417 图 31.5 里 $J=1$ 的能量曲线在低温下会钉在 $-4$ 而不是 $-2$，而这条曲线**照样平滑、照样单调**，没有任何报错提示你系数错了。相反，若以为 $J$ 与 $T$ 独立而「为了更低温」把 $J$ 加到 $10J$，你实际只是把温度除了 $10$，扫描范围白做一遍。

**落点**：本页 (31.1)–(31.4)；每自旋 $-2$ 在 p415；$T_c$ 的精确值 $\sinh(2J/k_BT_c)=1$ 即 $k_BT_c/J = 2/\ln(1+\sqrt2) = 2.269$ 不在本章正文，此处只作坐标；$\frac{1}{2}$ 与 $\beta$ 的「同一个东西」在 (31.12) 又被作者用来讲热容的 $1/T^2$；上游是「双重求和的对称性」（6.042J 计数），不越级。
</span>

---
