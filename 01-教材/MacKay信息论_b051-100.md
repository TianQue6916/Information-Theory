<!-- 书页 51–100｜来源：A 套（A=新规范主套，B=旧套补缺）｜PDF 页 = 书页 + 12｜机械重组，内容未改 -->


> <span style="color:#7f8c8d;">p.63 ⇄ 书内 p.51</span>

其中 $I$ 表示最高层的假设，对它们我们不作怀疑。

**第四**，在做出后续预测时，我们可以把对这些假设的不确定性考虑进去。不是选定某一个假设 $H^{*}$、再由此给出关于某个量 $t$ 的预测 $P(t \mid D, H^{*}, I)$；我们改用 sum rule，得到把「对 $H$ 的不确定性」也一并计入的预测：

```math
P(t \mid D, I) = \sum_{H} P(t \mid D, H, I)\,P(H \mid D, I). \tag{3.7}
```

这又是与正统统计学的一处对照：后者习惯「检验」一个默认模型，然后，如果检验在某个「significance level」上「接受该模型」，就**专断地**只用那个模型做预测。

于是 Steve 说服了我：

> <span style="color:#00838f;">probability theory 能触及 ad hoc 方法够不到的地方。</span>

再看几个简单推断问题的例子。

## 3.2 The bent coin（弯曲的硬币）

一枚弯曲硬币被掷 $F$ 次；我们观察到一串由正面与反面构成的序列 $s$（我们用符号 a 与 b 表示两者）。我们想知道这枚硬币的 bias，并预测下一次投掷出现正面的概率。我们在例 2.7（p.30）中第一次遇到这个任务，还会在第 6 章讨论自适应数据压缩时再次遇到它。它也是 Thomas Bayes 在 1763 年发表的那篇文章中研究的原始推断问题。

如同习题 2.8（p.30）那样，我们假定一个均匀 prior distribution，用 likelihood 相乘得到 posterior distribution。批评者可能反对：「这个 prior 是从哪来的？」我不会声称均匀 prior 有任何基本性；后面我们确实会给出非均匀 priors 的例子。prior 是一个主观假设。本书的主题之一是：

> <span style="color:#00838f;">不做假设，你就无法做推断 —— 也无法做数据压缩。</span>

我们把我们的假设命名为 $H_1$。〔稍后我们会引入另一套假设。〕给定 $p_a$，$F$ 次投掷产生一个含 $F_a$ 个 a、$F_b$ 个 b 的序列 $s$ 的概率为

```math
P(s \mid p_a, F, H_1) = p_a^{F_a}(1 - p_a)^{F_b}. \tag{3.8}
```

〔例如 $P(s = \mathrm{aaba} \mid p_a, F = 4, H_1) = p_a p_a (1 - p_a) p_a$。〕我们的第一个模型假定 $p_a$ 的 prior distribution 均匀：

```math
P(p_a \mid H_1) = 1, \quad p_a \in [0, 1] \tag{3.9}
```

且 $p_b \equiv 1 - p_a$。

### Inferring unknown parameters（推断未知参数）

给定长度为 $F$ 的字符串（其中 a 有 $F_a$ 个、b 有 $F_b$ 个），我们关心的是：(a) 推断 $p_a$ 可能取什么值；(b) 预测下一个字符是 a 还是 b。〔预测总是用概率表达。所以「预测下一个字符是否为 a」就等于「计算下一个字符是 a 的概率」。〕


> <span style="color:#7f8c8d;">p.64 ⇄ 书内 p.52</span>

假定 $H_1$ 为真，则在给定长度为 $F$、计数为 $\{F_a, F_b\}$ 的字符串 $s$ 时，$p_a$ 的 posterior probability 由 Bayes' theorem 给出：

```math
P(p_a \mid s, F, H_1) = \frac{P(s \mid p_a, F, H_1)\,P(p_a \mid H_1)}{P(s \mid F, H_1)}. \tag{3.10}
```

因子 $P(s \mid p_a, F, H_1)$ 作为 $p_a$ 的函数称为 likelihood function，已由式 (3.8) 给出；prior $P(p_a \mid H_1)$ 由式 (3.9) 给出。于是我们对 $p_a$ 的推断是：

```math
P(p_a \mid s, F, H_1) = \frac{p_a^{F_a}(1 - p_a)^{F_b}}{P(s \mid F, H_1)}. \tag{3.11}
```

归一化常数由 Beta 积分（beta integral）给出：

```math
P(s \mid F, H_1) = \int_0^1 \mathrm{d}p_a\; p_a^{F_a}(1 - p_a)^{F_b} = \frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)} = \frac{F_a!\,F_b!}{(F_a+F_b+1)!}. \tag{3.12}
```

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.5. <span style="color:#7f8c8d;">[2, p.59]</span>

Sketch the posterior probability $P(p_a \mid s = \mathrm{aba}, F = 3)$. What is the most probable value of $p_a$ (i.e., the value that maximizes the posterior probability density)? What is the mean value of $p_a$ under this distribution?

Answer the same questions for the posterior probability $P(p_a \mid s = \mathrm{bbb}, F = 3)$.

### From inferences to predictions（从推断到预测）

我们关于下一次投掷的预测 —— 即下一次掷出 a 的概率 —— 靠对 $p_a$ 积分得到。这起到了「在预测时把对 $p_a$ 的不确定性考虑进去」的作用。由 sum rule，

```math
P(\mathrm{a} \mid s, F) = \int \mathrm{d}p_a\; P(\mathrm{a} \mid p_a)\,P(p_a \mid s, F). \tag{3.13}
```

给定 $p_a$ 时出现 a 的概率就是 $p_a$，所以

```math
P(\mathrm{a} \mid s, F) = \frac{\int \mathrm{d}p_a\; p_a\; p_a^{F_a}(1 - p_a)^{F_b}}{P(s \mid F)} \tag{3.14}
```

```math
= \frac{\int \mathrm{d}p_a\; p_a^{F_a+1}(1 - p_a)^{F_b}}{P(s \mid F)} \tag{3.15}
```

```math
= \frac{(F_a+1)!\,F_b!}{(F_a+F_b+2)!} \cdot \frac{(F_a+F_b+1)!}{F_a!\,F_b!} = \frac{F_a+1}{F_a+F_b+2}, \tag{3.16}
```

此式被称为 **Laplace's rule**（Laplace 规则）。

## 3.3 The bent coin and model comparison（弯曲硬币与模型比较）

设想一位科学家为我们的 data 提出另一种理论。他断言：信源其实不是一枚弯曲硬币，而是一枚完美规整的骰子，一面涂成正面（'a'），另外五面涂成反面（'b'）。于是参数 $p_a$ —— 在原模型 $H_1$ 中它可以取 0 到 1 之间的任意值 —— 按新假设 $H_0$ 根本不是自由参数；它等于 $1/6$。〔该假设被命名为 $H_0$，使每个模型的下标正好表示它的自由参数个数。〕

在 data 的照耀下，我们如何比较这两个模型？我们想推断 $H_1$ 相对于 $H_0$ 有多可信。


> <span style="color:#7f8c8d;">p.65 ⇄ 书内 p.53</span>

### Model comparison as inference（把模型比较当作推断）

要做模型比较，我们再把 Bayes' theorem 写一遍，只是这次左端的论点不同。我们想知道在给定 data 时 $H_1$ 有多可信。由 Bayes' theorem，

```math
P(H_1 \mid s, F) = \frac{P(s \mid F, H_1)\,P(H_1)}{P(s \mid F)}. \tag{3.17}
```

同理，$H_0$ 的 posterior probability 为

```math
P(H_0 \mid s, F) = \frac{P(s \mid F, H_0)\,P(H_0)}{P(s \mid F)}. \tag{3.18}
```

两式的归一化常数都是 $P(s \mid F)$，即「得到实际观测到的 data」的总概率。若 $H_1$ 与 $H_0$ 是唯一被考虑的两个模型，则这个概率由 sum rule 给出：

```math
P(s \mid F) = P(s \mid F, H_1)\,P(H_1) + P(s \mid F, H_0)\,P(H_0). \tag{3.19}
```

要算出各假设的 posterior probabilities，我们得给先验概率 $P(H_1)$ 与 $P(H_0)$ 赋值；此例中不妨各取 $1/2$。此外还得算出依赖 data 的两项 $P(s \mid F, H_1)$ 与 $P(s \mid F, H_0)$。我们可以给这些量起名字。量 $P(s \mid F, H_1)$ 度量 data 有多偏向 $H_1$，我们称它为模型 $H_1$ 的 **evidence**。我们已在式 (3.10) 遇到过这个量 —— 它在那里作为我们做的第一个推断（给定 data 推断 $p_a$）的归一化常数出现。

<span style="color:#1e8449;">**[译注]**</span> **先验 $P(H_1)=P(H_0)=1/2$ 不是「无所谓」——它是 Occam 判罚的零点**

模型比较算的是 posterior ratio
$$\frac{P(H_1\mid s,F)}{P(H_0\mid s,F)}=\underbrace{\frac{P(s\mid F,H_1)}{P(s\mid F,H_0)}}_{\text{evidence ratio}}\times\underbrace{\frac{P(H_1)}{P(H_0)}}_{\text{先验比}}.$$
右端两个因子量级完全不同：evidence ratio 随 $F$ 指数增长（$\sim 2^{F\cdot D_{KL}}$），先验比是常数。所以先验只在**数据量小**时决定判决——$F=1$ 时先验主导，$F=250$ 时先验几乎无关。取 $1/2$ 的实际含义是：让判决完全由 evidence 说话。若把先验改成 $0.99:0.01$，需要多积累约 $\log_2 99\approx 6.6$ bit 的证据才能翻盘；这就是「模型比较不客观」这句话的**精确版本**：客观的是 evidence 的增长率，主观的是起点。

抽掉这个认识会犯两个错：① 以为更大的 evidence 永远更强（忽略了 prior 的平移）；② 把 evidence ratio 当 likelihood ratio 用（前者含 Occam factor，后者不含）。

挂载：6.042J 全概率公式 $P(s\mid F)=\sum_H P(s\mid F,H)P(H)$ 是这里唯一用到的工具——$P(H_i)$ 就是那组权重；实分析里 log 的单调性保证「比例」与「log 差」同序。

坐标：§3.3.1（原书 p.53–54，PDF p.65–66），式 (3.17)–(3.21)；数值表在 Table 3.5（同页）。

> <span style="color:#00838f;">模型比较是怎么运转的：**一个模型的 evidence，通常就是先前那次 Bayesian 推断的归一化常数。**</span>

我们在 (3.12) 中算出了模型 $H_1$ 的归一化常数。模型 $H_0$ 的 evidence 非常简单，因为这个模型没有需要推断的参数。记 $p_0 = 1/6$，我们有

<span style="color:#1e8449;">**[译注]**</span> **Occam factor 的来历：evidence 是**对参数积分**，不是取最大 likelihood——那个积分自带体积惩罚 $\sigma_{\text{post}}/\sigma_{\text{prior}}$**

$$P(s\mid F,H_1)=\int P(s\mid F,p_a,H_1)\,P(p_a\mid H_1)\,\mathrm{d}p_a \approx P(s\mid F,\hat p_a,H_1)\times\frac{\sigma_{\text{post}}}{\sigma_{\text{prior}}}.$$

右端的两个因子各有名字：第一项是「最佳拟合」，第二项就是 **Occam factor**，它总小于 1，且**参数越多、先验越宽、后验越窄，罚得越狠**。机制：参数空间里只有一小片（宽度 $\sigma_{\text{post}}$）能解释数据，而先验把概率铺在宽度 $\sigma_{\text{prior}}$ 上，积分只捞回这一小片的比例。抽掉「积分」改成 $\max_{p_a}$，复杂模型永远赢（多一个参数，最大值只增不减，且总能拟合噪声）——这就是为什么最大 likelihood 不能用于模型比较，而 Bayesian 的 evidence 自动实现 Occam 剃刀，不需要外加正则项。

数字：弯曲硬币例子中，$H_1$ 有一个参数 $p_a$，$F$ 次投掷后后验宽度 $\sigma_{\text{post}}\sim 1/\sqrt F$，先验宽度 $O(1)$，于是 $\log$ Occam factor $\approx -\tfrac12\log F$。这解释了译文紧接着的那条习题结论：支持 $H_0$ 的 log evidence **最多以 $\log F$ 增长**，而支持 $H_1$ 的可以线性于 $F$ 增长——两条增长率的差，就是「证据积累速度」的定量版本。

挂载：这是「$\int$ 与 $\sup$ 的差就是惩罚」这一条实分析事实的直接后果（$\int f\,p\le \sup f$，等号仅在 $p$ 为点质量时成立）；6.042J 的计数直觉（可选集合的大小比 = 概率比）给出同一图像。

坐标：§3.3.1 Model comparison as inference（原书 p.53，PDF p.65），式 (3.17)–(3.21)；Occam 的系统讨论在 §28（原书 p.343，PDF p.355）。

```math
P(s \mid F, H_0) = p_0^{F_a}(1 - p_0)^{F_b}. \tag{3.20}
```

于是模型 $H_1$ 对模型 $H_0$ 的 posterior probability ratio 为

```math
\frac{P(H_1 \mid s, F)}{P(H_0 \mid s, F)} = \frac{P(s \mid F, H_1)\,P(H_1)}{P(s \mid F, H_0)\,P(H_0)} \tag{3.21}
```

```math
= \frac{F_a!\,F_b!}{(F_a+F_b+1)!} \Big/ p_0^{F_a}(1 - p_0)^{F_b}. \tag{3.22}
```

这个 posterior probability ratio 的一些数值列于表 3.5。前五行说明：有些结果偏向一个模型，有些偏向另一个。没有任何结果与两个模型**完全**不相容。data 量小的时候（比如说六次投掷），通常不会出现两个模型中有一个压倒性更可信的情况。但 data 多了以后，只要 $F_a:F_b$ 偏离 $1:5$，任何这样的数据集给出的、反对 $H_0$ 的 evidence 就会累积起来。你无法预先知道需要多少 data 才能相当确定哪个理论为真。这取决于 $p_a$ 是什么。

较简单的模型 $H_0$ 因为没有可调参数，能够以最大的幅度落败 —— 赔率可能达到成百上千比一而对其不利。较复杂的模型则永远不会以很大幅度落败；不存在一个在模型 $H_1$ 下真正极不可能出现的数据集。


> <span style="color:#7f8c8d;">p.66 ⇄ 书内 p.54</span>

| $F$ | Data $(F_a, F_b)$ | $P(H_1 \mid s, F) \big/ P(H_0 \mid s, F)$ | 反向读数 |
|:--:|:--:|:--:|:--:|
| 6 | (5, 1) | 222.2 | |
| 6 | (3, 3) | 2.67 | |
| 6 | (2, 4) | 0.71 | $= 1/1.4$ |
| 6 | (1, 5) | 0.356 | $= 1/2.8$ |
| 6 | (0, 6) | 0.427 | $= 1/2.3$ |
| 20 | (10, 10) | 96.5 | |
| 20 | (3, 17) | 0.2 | $= 1/5$ |
| 20 | (0, 20) | 1.83 | |

<span style="color:#7f8c8d;">Table 3.5 ── 「弯曲硬币」问题中模型 $H_1$ 与 $H_0$ 的比较结果。模型 $H_0$ 断言 $p_a = 1/6$、$p_b = 5/6$。（原书 Table 3.5；最后一列为原书在页边给出的倒数读法。）</span>

[Figure 3.6：bent coin 投掷在三种不同真实条件下累积时，「支持 $H_1$ 的 evidence」的典型行为（三列分别对应 $H_0$ 为真 $p_a = 1/6$、$H_1$ 为真 $p_a = 0.25$、$H_1$ 为真 $p_a = 0.5$）。横轴为投掷次数 $F$（0–200）；左侧纵轴为 $\ln\left[P(s \mid F, H_1) / P(s \mid F, H_0)\right]$，右侧纵轴给出对应的 $P(s \mid F, H_1)/P(s \mid F, H_0)$ 数值（$1/100$ 到 $1000/1$）。三行是不同的独立仿真实验]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.6. <span style="color:#7f8c8d;">[2]</span>

Show that after $F$ tosses have taken place, the biggest value that the log evidence ratio

```math
\log \frac{P(s \mid F, H_1)}{P(s \mid F, H_0)} \tag{3.23}
```

can have scales linearly with $F$ if $H_1$ is more probable, but the log evidence in favour of $H_0$ can grow at most as $\log F$.

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.7. <span style="color:#7f8c8d;">[3, p.60]</span>

Putting your sampling theory hat on, assuming $F_a$ has not yet been measured, compute a plausible range that the log evidence ratio might lie in, as a function of $F$ and the true value of $p_a$, and sketch it as a function of $F$ for $p_a = p_0 = 1/6$, $p_a = 0.25$, and $p_a = 1/2$. [Hint: sketch the log evidence as a function of the random variable $F_a$ and work out the mean and standard deviation of $F_a$.]

### Typical behaviour of the evidence（evidence 的典型行为）

图 3.6 画出了若干仿真实验中 log evidence ratio 作为投掷次数 $F$ 的函数。左侧的实验里 $H_0$ 为真；右侧的实验里 $H_1$ 为真，且 $p_a$ 取 0.25 或 0.5。

我们会在后面某一章进一步讨论模型比较。


> <span style="color:#7f8c8d;">p.67 ⇄ 书内 p.55</span>

## 3.4 An example of legal evidence（一个法庭证据的例子）

下面这个例子说明：Bayesian inference 里「priors」远不是全部。

> <span style="color:#00838f;">两个人在犯罪现场留下了各自的血迹。一名嫌疑人 Oliver 接受检验，发现是 'O' 型血。两处血迹的血型分别是 'O' 型（当地人群中的常见类型，频率 60%）与 'AB' 型（罕见类型，频率 1%）。这些 data（现场发现 'O' 型与 'AB' 型血）是否为「Oliver 是当时在场的两人之一」这一命题提供了证据？</span>

一个粗心的律师可能会声称：嫌疑人的血型出现在现场，就是「他在场」这一理论的正向证据。但事实并非如此。

把「嫌疑人与一名身份不明者曾在场」这一命题记为 $S$。与之对立的 $\bar{S}$ 表示「来自人群的两名身份不明者曾在场」。本题的 prior 是命题 $S$ 与 $\bar{S}$ 之间的先验概率比。这个量对最终判决很重要，应当基于本案中其他一切可得信息。我们这里的任务只是评估 data $D$ 带来的贡献，即 likelihood ratio $P(D \mid S, H)/P(D \mid \bar{S}, H)$。在我看来，陪审团的任务一般应当是：把每一件可采信的独立证据各自仔细评估出的 likelihood ratios 逐一相乘，再乘以一个同样仔细论证过的先验概率。〔这一观点为许多统计学家所认同，但博学的英国上诉法官们最近不同意 —— 他们实际上推翻了一次审判的裁决，理由是陪审员被教会用 Bayes' theorem 处理复杂的 DNA 证据。〕

给定 $S$ 时 data 的概率，等于「从人群中随机抽出的那一名身份不明者具有 AB 型血」的概率：

```math
P(D \mid S, H) = p_{AB} \tag{3.24}
```

（因为给定 $S$，我们已经知道其中一处血迹是 O 型）。给定 $\bar{S}$ 时 data 的概率，等于「从人群中随机抽出的两名身份不明者分别为 O 型与 AB 型」的概率：

```math
P(D \mid \bar{S}, H) = 2\,p_{O}\,p_{AB}. \tag{3.25}
```

这些式子里的 $H$ 表示一组假设：曾有两人在场并留下血迹；且「某种解释下身份不明者的血型概率分布」等于人群频率。

相除，得到 likelihood ratio：

```math
\frac{P(D \mid S, H)}{P(D \mid \bar{S}, H)} = \frac{1}{2 p_{O}} = \frac{1}{2 \times 0.6} = 0.83. \tag{3.26}
```

所以这些 data 实际上**弱弱地**构成了**反对**「Oliver 在场」这一设想的证据。

这个结果可能令人意外，让我们从几个角度来审它。先考虑另一名嫌疑人 Alberto，他是 AB 型血。直觉上，这些 data 确实为「该嫌疑人在场」这一理论 $S$（相对于零假设 $\bar{S}$）提供了证据。确实，此情形下的 likelihood ratio 是：


> <span style="color:#7f8c8d;">p.68 ⇄ 书内 p.56</span>

```math
\frac{P(D \mid S, H)}{P(D \mid \bar{S}, H)} = \frac{1}{2\,p_{AB}} = 50. \tag{3.27}
```

现在把情形微调一下：设想 99% 的人是 O 型血，其余是 AB 型血，人群中只有这两种血型。现场的 data 与之前相同。再考虑一次：这些 data 如何影响我们对 Oliver（O 型血嫌疑人）与 Alberto（AB 型血嫌疑人）的信念。直觉上，我们仍然相信罕见 AB 型血的出现是「Alberto 在场」的正向证据。但「现场检出 O 型血」这一事实，是否偏向「Oliver 在场」这一假设呢？如果是，那就意味着：无论嫌疑人是谁，这些 data 都让他更可能在场 —— 于是人群中的每个人都会受到更大的怀疑，这显然荒谬。这些 data 可以与任一血型的任何嫌疑人共存，但如果它们为某些理论提供了证据，就**必然**同时为另一些理论提供了反证。

换一种方式来想这件事：设想现场不是两处血迹而是十处；并且整个当地人群只有一百人，其中九十名是 O 型血嫌疑人、十名是 AB 型血嫌疑人。考虑某个特定的 O 型嫌疑人 Oliver：在没有任何其他信息、血检结果尚未到来之前，他在现场的机会是十分之一，因为我们知道一百名嫌疑人中有十人曾在场。现在我们拿到血检结果：十处血迹中有九处是 AB 型，一处是 O 型。这是否让「Oliver 曾在场」更可能了？不是 —— 现在他在场的机会只有九十分之一，因为我们知道在场者中只有一人是 O 型。

最后，写出一般情形的公式也许更有助于直觉：现场发现 $n_O$ 处 O 型血迹、$n_{AB}$ 处 AB 型血迹，共 $N$ 人；身份不明者来自一个频率为 $p_O$、$p_{AB}$ 的大人群（可能还有其他血型）。任务是评估两个假设的 likelihood ratio：$S$，「O 型嫌疑人（Oliver）与 $N-1$ 名身份不明者留下了 $N$ 处血迹」；以及 $\bar{S}$，「$N$ 名身份不明者留下了 $N$ 处血迹」。假设 $\bar{S}$ 下 data 的概率，就是「从人群中随机抽取 $N$ 人、恰好得到 $n_O$ 名 O 型与 $n_{AB}$ 名 AB 型」的概率：

```math
P(n_O, n_{AB} \mid \bar{S}) = \frac{N!}{n_O!\,n_{AB}!}\; p_O^{\,n_O}\, p_{AB}^{\,n_{AB}}. \tag{3.28}
```

而在假设 $S$ 下，我们需要的是其余 $N-1$ 人的分布：

```math
P(n_O, n_{AB} \mid S) = \frac{(N-1)!}{(n_O-1)!\,n_{AB}!}\; p_O^{\,n_O-1}\, p_{AB}^{\,n_{AB}}. \tag{3.29}
```

likelihood ratio 为：

```math
\frac{P(n_O, n_{AB} \mid S)}{P(n_O, n_{AB} \mid \bar{S})} = \frac{n_O/N}{p_O}. \tag{3.30}
```

这是一个有教益的结果。likelihood ratio —— 即这些 data 对「Oliver 是否在场」这一问题的贡献 —— 只取决于「他的血型在观测 data 中的频率」与「该血型在人群中的背景频率」之比。它与现场发现的其他血型的计数无关，也与它们在人群中的频率无关。


> <span style="color:#7f8c8d;">p.69 ⇄ 书内 p.57</span>

如果 O 型血迹的数目多于假设 $\bar{S}$ 下预期的平均数，那么 data 就为「Oliver 在场」提供了证据。反之，如果 O 型血迹的数目少于 $\bar{S}$ 下的预期数，那么 data 就降低了「他在场」这一假设的概率。在 $n_O/N = p_O$ 这一特殊情形下，无论 data 与假设 $S$ 多么相容，这些 data 都不为任何一方提供证据。

## 3.5 Exercises（习题）

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.8. <span style="color:#7f8c8d;">[2, p.60]</span>

The three doors, normal rules.（三扇门，常规规则）

On a game show, a contestant is told the rules as follows:

> <span style="color:#00838f;">There are three doors, labelled 1, 2, 3. A single prize has been hidden behind one of them. You get to select one door. Initially your chosen door will not be opened. Instead, the gameshow host will open one of the other two doors, and he will do so in such a way as not to reveal the prize. For example, if you first choose door 1, he will then open one of doors 2 and 3, and it is guaranteed that he will choose which one to open so that the prize will not be revealed.</span>
> <span style="color:#00838f;">At this point, you will be given a fresh choice of door: you can either stick with your first choice, or you can switch to the other closed door. All the doors will then be opened and you will receive whatever is behind your final choice of door.</span>

Imagine that the contestant chooses door 1 first; then the gameshow host opens door 3, revealing nothing behind the door, as promised. Should the contestant (a) stick with door 1, or (b) switch to door 2, or (c) does it make no difference?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.9. <span style="color:#7f8c8d;">[2, p.61]</span>

The three doors, earthquake scenario.（三扇门，地震情景）

Imagine that the game happens again and just as the gameshow host is about to open one of the doors a violent earthquake rattles the building and one of the three doors flies open. It happens to be door 3, and it happens not to have the prize behind it. The contestant had initially chosen door 1.

Repositioning his toupée, the host suggests, 'OK, since you chose door 1 initially, door 3 is a valid door for me to open, according to the rules of the game; I'll let door 3 stay open. Let's carry on as if nothing happened.'

Should the contestant stick with door 1, or switch to door 2, or does it make no difference? Assume that the prize was placed randomly, that the gameshow host does not know where it is, and that the door flew open because its latch was broken by the earthquake.

[A similar alternative scenario is a gameshow whose confused host forgets the rules, and where the prize is, and opens one of the unchosen doors at random. He opens door 3, and the prize is not revealed. Should the contestant choose what's behind door 1 or door 2? Does the optimal decision for the contestant depend on the contestant's beliefs about whether the gameshow host is confused or not?]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.10. <span style="color:#7f8c8d;">[2]</span>

Another example in which the emphasis is not on priors. You visit a family whose three children are all at the local school. You don't


> <span style="color:#7f8c8d;">p.70 ⇄ 书内 p.58</span>

know anything about the sexes of the children. While walking clumsily round the home, you stumble through one of the three unlabelled bedroom doors that you know belong, one each, to the three children, and find that the bedroom contains girlie stuff in sufficient quantities to convince you that the child who lives in that bedroom is a girl. Later, you sneak a look at a letter addressed to the parents, which reads 'From the Headmaster: we are sending this letter to all parents who have male children at the school to inform them about the following boyish matters. . . '.

These two sources of evidence establish that at least one of the three children is a girl, and that at least one of the children is a boy. What are the probabilities that there are (a) two girls and one boy; (b) two boys and one girl?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.11. <span style="color:#7f8c8d;">[2, p.61]</span>

Mrs S is found stabbed in her family garden. Mr S behaves strangely after her death and is considered as a suspect. On investigation of police and social records it is found that Mr S had beaten up his wife on at least nine previous occasions. The prosecution advances this data as evidence in favour of the hypothesis that Mr S is guilty of the murder. 'Ah no,' says Mr S's highly paid lawyer, 'statistically, only one in a thousand wife-beaters actually goes on to murder his wife. So the wife-beating is not strong evidence at all. In fact, given the wife-beating evidence alone, it's extremely unlikely that he would be the murderer of his wife – only a 1/1000 chance. You should therefore find him innocent.'

Is the lawyer right to imply that the history of wife-beating does not point to Mr S's being the murderer? Or is the lawyer a slimy trickster? If the latter, what is wrong with his argument?

[Having received an indignant letter from a lawyer about the preceding paragraph, I'd like to add an extra inference exercise at this point: Does my suggestion that Mr. S.'s lawyer may have been a slimy trickster imply that I believe all lawyers are slimy tricksters? (Answer: No.)]

> <span style="color:#7f8c8d;">脚注 1：在美国，估计每年有两百万名女性被伴侣虐待。1994 年有 4739 名女性成为凶杀受害者，其中 1326 名（28%）被丈夫或男友杀害。来源：`http://www.umn.edu/mincava/papers/factoid.htm`、`http://www.gunfree.inter.net/vpc/womenfs.htm`。</span>

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.12. <span style="color:#7f8c8d;">[2]</span>

A bag contains one counter, known to be either white or black. A white counter is put in, the bag is shaken, and a counter is drawn out, which proves to be white. What is now the chance of drawing a white counter? [Notice that the state of the bag, after the operations, is exactly identical to its state before.]

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.13. <span style="color:#7f8c8d;">[2, p.62]</span>

You move into a new house; the phone is connected, and you're pretty sure that the phone number is 740511, but not as sure as you would like to be. As an experiment, you pick up the phone and dial 740511; you obtain a 'busy' signal. Are you now more sure of your phone number? If so, how much?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.14. <span style="color:#7f8c8d;">[1]</span>

In a game, two coins are tossed. If either of the coins comes up heads, you have won a prize. To claim the prize, you must point to one of your coins that is a head and say 'look, that coin's a head, I've won'. You watch Fred play the game. He tosses the two coins, and he


> <span style="color:#7f8c8d;">p.71 ⇄ 书内 p.59（习题 3.14 续）</span>

points to a coin and says 'look, that coin's a head, I've won'. What is the probability that the other coin is a head?

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 3.15. <span style="color:#7f8c8d;">[2, p.63]</span>

A statistical statement appeared in *The Guardian* on Friday January 4, 2002:

> <span style="color:#00838f;">When spun on edge 250 times, a Belgian one-euro coin came up heads 140 times and tails 110. 'It looks very suspicious to me', said Barry Blight, a statistics lecturer at the London School of Economics. 'If the coin were unbiased the chance of getting a result as extreme as that would be less than 7%'.</span>

〔译：一枚比利时一欧元硬币以边缘为轴旋转 250 次，出现正面 140 次、反面 110 次。伦敦经济学院统计学讲师 Barry Blight 说：「在我看来这非常可疑。若这枚硬币是无偏的，得到如此极端结果的概率不足 7%。」〕

But do these data give evidence that the coin is biased rather than fair? [Hint: see equation (3.22).]

## 3.6 Solutions（解答）

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.1（习题 3.1 的解答，p.47）

设 data 为 $D$。假定先验概率相等，

```math
\frac{P(A \mid D)}{P(B \mid D)} = \frac{1}{2}\cdot\frac{3}{2}\cdot\frac{1}{1}\cdot\frac{3}{2}\cdot\frac{1}{2}\cdot\frac{2}{2}\cdot\frac{1}{2} = \frac{9}{32} \tag{3.31}
```

于是 $P(A \mid D) = 9/41$。

> <span style="color:#7f8c8d;">〔上述七项依次是 data $5, 3, 9, 3, 8, 4, 7$ 每次投掷的「A 的面数 / B 的面数」之比；两骰各 20 面，故公共因子 $1/20$ 相消。〕</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.2（习题 3.2 的解答，p.47）

在给定各假设时 data 的概率为：

```math
P(D \mid A) = \frac{3 \cdot 1 \cdot 2 \cdot 1 \cdot 3 \cdot 1 \cdot 1}{20^{7}} = \frac{18}{20^{7}} \tag{3.32}
```

```math
P(D \mid B) = \frac{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 1 \cdot 2}{20^{7}} = \frac{64}{20^{7}} \tag{3.33}
```

```math
P(D \mid C) = \frac{1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1}{20^{7}} = \frac{1}{20^{7}}. \tag{3.34}
```

所以

```math
P(A \mid D) = \frac{18}{18 + 64 + 1} = \frac{18}{83}; \quad P(B \mid D) = \frac{64}{83}; \quad P(C \mid D) = \frac{1}{83}. \tag{3.35}
```


> <span style="color:#7f8c8d;">p.72 ⇄ 书内 p.60</span>

[Figure 3.7：两种不同数据集下，弯曲硬币的 bias $p_a$ 的 posterior probability —— (a) $P(p_a \mid s = \mathrm{aba}, F = 3) \propto p_a^{2}(1 - p_a)$，横轴 $p_a$ 从 0 到 1；(b) $P(p_a \mid s = \mathrm{bbb}, F = 3) \propto (1 - p_a)^{3}$，横轴同一区间]

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.5（习题 3.5 的解答，p.52）

(a) $P(p_a \mid s = \mathrm{aba}, F = 3) \propto p_a^{2}(1 - p_a)$。$p_a$ 的最可能取值（即使 posterior probability density 最大的那个值）为 $2/3$。$p_a$ 的均值为 $3/5$。

见图 3.7a。

(b) $P(p_a \mid s = \mathrm{bbb}, F = 3) \propto (1 - p_a)^{3}$。$p_a$ 的最可能取值为 0。$p_a$ 的均值为 $1/5$。

见图 3.7b。

[Figure 3.8：支持 $H_1$ 的 log evidence 作为 $F$ 的函数时「可信取值范围」—— 三列分别对应 $H_0$ 为真（$p_a = 1/6$）、$H_1$ 为真（$p_a = 0.25$）、$H_1$ 为真（$p_a = 0.5$）。左侧纵轴为 $\log\left[P(s \mid F, H_1)/P(s \mid F, H_0)\right]$，右侧纵轴给出对应的比值数值。实线表示随机变量 $F_a$ 取其均值 $F_a = p_a F$ 时的 log evidence；点线（近似地）表示 $F_a$ 处于其第 2.5 或第 97.5 百分位时的 log evidence]

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.7（习题 3.7 的解答，p.54）

图 3.8 中的曲线是这样得到的：先求 $F_a$ 的均值与标准差，然后把 $F_a$ 取为「均值 ± 两倍标准差」以得到 $F_a$ 的 95% 可信取值范围，再算出三个对应的 log evidence ratio 值。

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.8（习题 3.8 的解答，p.57）

记 $H_i$ 为「奖品在第 $i$ 扇门后」这一假设。我们做如下假设：三个假设 $H_1, H_2, H_3$ 先验等概率，即

```math
P(H_1) = P(H_2) = P(H_3) = \frac{1}{3}. \tag{3.36}
```

在选门 1 之后，我们收到的 datum 是 $D = 3$ 或 $D = 2$ 之一（分别表示主持人打开了 3 号门或 2 号门）。我们假定这两种可能结果具有如下概率：若奖品在 1 号门后，主持人可以自由选择；此情形下我们假定他在 $D = 2$ 与 $D = 3$ 之间随机选取；否则主持人的选择是被迫的，概率为 0 与 1。

```math
\begin{aligned}
P(D = 2 \mid H_1) &= 1/2, & P(D = 2 \mid H_2) &= 0, & P(D = 2 \mid H_3) &= 1 \\
P(D = 3 \mid H_1) &= 1/2, & P(D = 3 \mid H_2) &= 1, & P(D = 3 \mid H_3) &= 0
\end{aligned} \tag{3.37}
```

现在用 Bayes' theorem 计算各假设的 posterior probabilities：

```math
P(H_i \mid D = 3) = \frac{P(D = 3 \mid H_i)\,P(H_i)}{P(D = 3)} \tag{3.38}
```

```math
P(H_1 \mid D = 3) = \frac{(1/2)(1/3)}{P(D = 3)}, \quad P(H_2 \mid D = 3) = \frac{(1)(1/3)}{P(D = 3)}, \quad P(H_3 \mid D = 3) = \frac{(0)(1/3)}{P(D = 3)}. \tag{3.39}
```

分母 $P(D = 3)$ 为 $(1/2)$，因为它就是这个 posterior distribution 的归一化常数。于是

```math
P(H_1 \mid D = 3) = 1/3, \quad P(H_2 \mid D = 3) = 2/3, \quad P(H_3 \mid D = 3) = 0. \tag{3.40}
```

所以，参赛者应当换到 2 号门，以获得最大的中奖机会。

许多人觉得这个结果令人意外。有两种办法让它更直观。一是和朋友玩三十次这个游戏，记录「换门就中奖」的频率。另一种是做一个思想实验：游戏用一百万扇门来玩。规则现在变成：参赛者选一扇门，然后主持人以 999 998 扇门的方式打开，绝不泄露奖品，留下参赛者所选的那扇门与另一扇门关着。参赛者此时可以坚持或换门。想象参赛者面对一百万扇门，其中 1 号门与 234 598 号门没被打开，而 1 号门是参赛者最初的选择。你认为奖品在哪里？


> <span style="color:#7f8c8d;">p.73 ⇄ 书内 p.61</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.9（习题 3.9 的解答，p.57）

若 3 号门是被地震打开的，推断结果就不一样了 —— 即使视觉上现场看起来一样。data 的性质变了，data 的概率也变了。可能出现的 data 结果，首先是「任何数量的门都可能被打开」：我们可以把八种可能结果标为 $d = (0,0,0), (0,0,1), (0,1,0), (1,0,0), (0,1,1), \ldots, (1,1,1)$。其次，还可能是「地震打开一扇或多扇门之后奖品变得可见」。所以 data $D$ 由 $d$ 的取值以及「奖品是否被揭露」这一陈述组成。要说出这些结果的概率是多少很难，因为它们取决于我们对门闩可靠性以及地震性质的信念；但我们可以在不指明每个 $d$ 的 $P(d \mid H_i)$ 数值的情况下，把所需的后验概率提取出来。唯一要紧的，是对实际发生的那个 $D$ 而言各量 $P(D \mid H_1)$、$P(D \mid H_2)$、$P(D \mid H_3)$ 的**相对**取值。〔这就是我们在 §2.3 遇到的 likelihood principle。〕实际发生的 $D$ 是「$d = (0,0,1)$，且奖品不可见」。首先，$P(D \mid H_3) = 0$ 显然成立，因为「奖品不可见」这一 datum 与 $H_3$ 不相容。其次，假定参赛者选了 1 号门，那么 $P(D \mid H_1)$ 与 $P(D \mid H_2)$ 相比如何？假定地震对游戏节目参赛者的决策并不敏感，则这两个量由对称性必然相等。我们不知道 3 号门脱铰的可能性有多大，但无论多大，在奖品位于 1 号门后与位于 2 号门后这两种情形下，它脱铰的可能性一样大。所以，既然 $P(D \mid H_1) = P(D \mid H_2)$，我们得到：

```math
P(H_1 \mid D) = \frac{P(D \mid H_1)(1/3)}{P(D)} = 1/2, \quad P(H_2 \mid D) = \frac{P(D \mid H_2)(1/3)}{P(D)} = 1/2, \quad P(H_3 \mid D) = \frac{P(D \mid H_3)(1/3)}{P(D)} = 0. \tag{3.41}
```

此时两个可能的假设等概率。

[Figure 3.9：第二个三扇门问题中「一切事物的概率」表 —— 假定地震刚刚发生。行是奖品所在（door 1 / door 2 / door 3），列是地震打开了哪些门（none / 1 / 2 / 3 / 1,2 / 1,3 / 2,3 / 1,2,3），格内为相应联合概率；$p_3$ 表示「只有 3 号门被地震打开」的概率]

如果我们进一步假定主持人知道奖品在哪里、并且可能在做欺骗性举动，答案可能还要修改，因为我们必须把主持人的话也当作 data 的一部分。

糊涂了？务必把这两个游戏节目问题弄清楚，非常值得。别担心 —— 我第一次遇到第二个问题时也栽了。

遇到一个令人困惑的概率问题时，有一条普遍规则极有帮助：

> <span style="color:#00838f;">Always write down the probability of everything.（永远把一切事物的概率写下来。）</span>
>
> <span style="color:#7f8c8d;">—— Steve Gull</span>

从这个联合概率出发，任何想要的推断都可以机械地得到（图 3.9）。

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.11（习题 3.11 的解答，p.58）

律师引用的那个统计量，指的是「随机抽取一名打妻子的人，他随后会谋杀妻子」的概率。而「在妻子已被谋杀的前提下，丈夫是凶手的概率」完全是另一个量。


> <span style="color:#7f8c8d;">p.74 ⇄ 书内 p.62</span>

要推出后者，我们需要对「妻子被他人谋杀」的概率追加假设。如果她住在一个随机凶杀频发的街区，那么这个概率很大，于是（在缺少其他证据时）「丈夫是凶手」的后验概率可能并不很高。但在更太平的地区，很可能的情况是：如果你被发现遭到谋杀，最可能谋杀你的就是你最亲近的亲属之一。

让我们借助 p.58 上的统计数字算出一些示例数值。令 $m = 1$ 表示「一名女性已被谋杀」这一命题；$h = 1$ 表示「是丈夫干的」；$b = 1$ 表示「他在谋杀发生前那一年里打过她」。命题「是别人干的」记为 $h = 0$。为计算 posterior probability $P(h = 1 \mid b = 1, m = 1)$，我们需要定义 $P(h \mid m = 1)$、$P(b \mid h = 1, m = 1)$ 与 $P(b = 1 \mid h = 0, m = 1)$。由统计数字可以读出 $P(h = 1 \mid m = 1) = 0.28$。又若一亿名女性中有两百万名被殴打，则 $P(b = 1 \mid h = 0, m = 1) = 0.02$。最后，我们需要 $P(b \mid h = 1, m = 1)$ 的取值：如果一个男人谋杀了妻子，那么这有多大可能是他第一次对她动手？我猜这相当不可能；所以也许 $P(b = 1 \mid h = 1, m = 1)$ 取 0.9 或更大。

于是由 Bayes' theorem，

```math
P(h = 1 \mid b = 1, m = 1) = \frac{0.9 \times 0.28}{0.9 \times 0.28 + 0.02 \times 0.72} \simeq 95\%. \tag{3.42}
```

要让 p.58 上那位律师的油滑之处显形，一个办法是构造出与他逻辑结构完全相同、却明显是错误的论证。例如，律师完全可以说：「S 夫人不仅被谋杀了，她还是在下午 4:02 到 4:03 之间被谋杀的。从统计上讲，每一百万名打妻子的人里只有一个真的会在下午 4:02 到 4:03 之间谋杀妻子。所以打妻子根本不是有力证据。事实上，仅凭打妻子的证据，他在这个时段以这种方式谋杀妻子的可能性极低 —— 只有百万分之一的机会。」

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.13（习题 3.13 的解答，p.58）

有两个假设。$H_0$：你的号码是 740511；$H_1$：它是别的号码。data $D$ 是「我拨 740511 时听到忙音」。给定各假设时 $D$ 的概率是多少？若你的号码就是 740511，那么我们预期必然听到忙音：

```math
P(D \mid H_0) = 1.
```

另一方面，若 $H_1$ 为真，那么所拨号码返回忙音的概率小于 1，因为还可能有别的结果（例如回铃音，或「号码不可达」信号）。这个概率 $P(D \mid H_1)$ 的取值，取决于「一个与你号码相近的随机电话号码是有效号码」的概率 $\alpha$，以及「你拨一个有效号码时得到忙音」的概率 $\beta$。

据我的电话簿规模估计，剑桥大约有 75 000 个有效号码，长度都是六位数字。所以随机一个六位数字号码有效的概率约为 $75\,000/10^{6} = 0.075$。若把以 0、1、9 开头的号码排除在随机选择之外，则概率 $\alpha$ 约为 $75\,000/700\,000 \simeq 0.1$。若假定电话号码是成簇分布的，那么记错的号码比随机号码更可能有效；所以在 $H_1$ 为真的前提下，我们猜的那个号码有效的概率 $\alpha$ 可能大于 0.1。无论如何，$\alpha$ 必定在 0.1 与 1 之间。我们可以把这个不确定性带着往下算，看它在最后到底有多要紧。

拨一个有效号码时得到忙音的概率 $\beta$，等于你认为「在你试着拨号的那一刻，处于占线或未挂好状态的话机」所占的比例。这个比例随城镇、随时段而变。在剑桥的白天，我猜大约 1% 的话机占线；凌晨四点则可能是 0.1% 或更低。

概率 $P(D \mid H_1)$ 是 $\alpha$ 与 $\beta$ 的乘积，即约为 $0.1 \times 0.01 = 10^{-3}$。按我们的估计，拨一个随机号码而得到忙音的机会约为千分之一；若有效号码成簇很强，则为百分之一；若在凌晨拨号，则为万分之一。

这些 data 如何影响你对自己号码的信念？后验概率比等于 likelihood ratio 乘先验概率比：

```math
\frac{P(H_0 \mid D)}{P(H_1 \mid D)} = \frac{P(D \mid H_0)}{P(D \mid H_1)}\,\frac{P(H_0)}{P(H_1)}. \tag{3.43}
```

likelihood ratio 约为 100 比 1 或 1000 比 1，所以后验概率比会朝有利于 $H_0$ 的方向摆动 100 或 1000 倍。若 $H_0$ 的先验概率是 0.5，则后验概率为

```math
P(H_0 \mid D) = \frac{P(H_0 \mid D)/P(H_1 \mid D)}{1 + P(H_0 \mid D)/P(H_1 \mid D)} \simeq 0.99 \ \text{or}\ 0.999. \tag{3.44}
```

> <span style="color:#7f8c8d;">〔式 (3.44) 的分子在扫描件中因排版丢失，此处按上下文（后验概率比 $R = P(H_0 \mid D)/P(H_1 \mid D)$，且 $P(H_0 \mid D) = R/(1+R)$）补回。〕</span>


> <span style="color:#7f8c8d;">p.75 ⇄ 书内 p.63</span>

#### <span style="color:#2471a3;">**[solution]**</span> Solution to exercise 3.15（习题 3.15 的解答，p.59）

我们比较模型 $H_0$（硬币公平）与 $H_1$（硬币有偏，其 bias 的先验取均匀分布 $P(p \mid H_1) = 1$）。〔在我看来，用均匀先验是合理的，因为我知道有些硬币 —— 比如美国的一分硬币 —— 以边缘为轴旋转时 bias 很严重；所以 $p = 0.01$、$p = 0.1$ 或 $p = 0.95$ 这些情形并不会让我意外。〕

当我提到 $H_0$（硬币公平）时，一个学究式的人会说：「竟然去考虑硬币公平，太荒谬了 —— 任何硬币必定在某种程度上是有偏的。」我当然同意。所以请学究们善意地把 $H_0$ 理解为「硬币在千分之一的精度内是公平的，即 $p \in 0.5 \pm 0.001$」。

likelihood ratio 为：

```math
\frac{P(D \mid H_1)}{P(D \mid H_0)} = \frac{140!\,110!}{251!} \Big/ 2^{-250} = 0.48. \tag{3.45}
```

[Figure 3.10：在两种假设下「正面个数」的概率分布 —— $H_0$ 表示硬币公平，$H_1$ 表示硬币有偏且其 bias 的先验为均匀分布。观测结果（$D = 140$ 次正面）给出的弱证据**支持** $H_0$，即「硬币公平」这一假设。横轴为 0 到 250 次正面，纵轴概率密度 0 到 0.05；图中标出 $H_0$（窄峰，位于 125 附近）与 $H_1$（宽分布）]

所以这些 data 几乎不为任何一方提供证据；事实上，它们提供了**弱**证据（二比一）支持 $H_0$！

「不，不」，相信有偏的人反驳道，「你那愚蠢的均匀 prior 并不代表我对有偏硬币的 bias 的先验信念 —— 我预期只有很小的 bias」。为了尽可能对 $H_1$ 宽厚，让我们看看若把 prior 设得「有先见之明」，它能表现得多好。我们允许形如

```math
P(p \mid H_1, \alpha) = \frac{1}{Z(\alpha)}\, p^{\alpha-1}(1-p)^{\alpha-1}, \quad \text{where } Z(\alpha) = \Gamma(\alpha)^{2}/\Gamma(2\alpha) \tag{3.46}
```

的 prior（这是 Beta distribution；原始的均匀 prior 由 $\alpha = 1$ 重现）。通过调整 $\alpha$，$H_1$ 相对 $H_0$ 的 likelihood ratio

```math
\frac{P(D \mid H_1, \alpha)}{P(D \mid H_0)} = \frac{\Gamma(140+\alpha)\,\Gamma(110+\alpha)\,\Gamma(2\alpha)\,2^{250}}{\Gamma(250+2\alpha)\,\Gamma(\alpha)^{2}}, \tag{3.47}
```


> <span style="color:#7f8c8d;">p.76 ⇄ 书内 p.64</span>

可以略微增大。图 3.11 给出了若干 $\alpha$ 取值下的结果。即使取最有利的 $\alpha$（$\alpha \simeq 50$），likelihood ratio 也只能达到约二比一，支持 $H_1$。

| $\alpha$ | $P(D \mid H_1, \alpha) \big/ P(D \mid H_0)$ |
|:--:|:--:|
| 0.37 | 0.25 |
| 1.0 | 0.48 |
| 2.7 | 0.82 |
| 7.4 | 1.3 |
| 20 | 1.8 |
| 55 | 1.9 |
| 148 | 1.7 |
| 403 | 1.3 |
| 1096 | 1.1 |

<span style="color:#7f8c8d;">Table / Figure 3.11 ── 对若干先验分布 hyperparameter $\alpha$ 取值的 likelihood ratio（data 为 250 次投掷中 140 次正面）。</span>

结论是：这些 data 并不「非常可疑」。它们最多只能被解释为「以二比一的强度支持两个假设中的某一个」。

这些软弱的 likelihood ratios 是 priors 过于拘束造成的吗？有没有办法得出「非常可疑」的结论？按 likelihood 的意义与 data 最匹配的 prior，是把 $p$ 以概率一钉在 $f \equiv 140/250$ 的那个 prior。我们把这个模型叫 $H^{*}$。其 likelihood ratio 为 $P(D \mid H^{*})/P(D \mid H_0) = 2^{250} f^{140}(1 - f)^{110} = 6.1$。所以，这些 data 对「不存在 bias」这一假设所能凑出的最强证据，是六比一。

| $\alpha$ | $P(D \mid H_1, \alpha) \big/ P(D \mid H_0)$ |
|:--:|:--:|
| 0.37 | 0.32 |
| 1.0 | 0.61 |
| 2.7 | 1.0 |
| 7.4 | 1.6 |
| 20 | 2.2 |
| 55 | 2.3 |
| 148 | 1.9 |
| 403 | 1.4 |
| 1096 | 1.2 |

<span style="color:#7f8c8d;">Table / Figure 3.12 ── 当 data 为 250 次试验中 141 次正面时，对若干 hyperparameter $\alpha$ 取值的 likelihood ratio。</span>

既然我们正在注意「抽样理论」统计学所产生的荒谬误导性答案（比如我们刚解完的那道题里 7% 的 p-value），那就再补一刀。如果对数据集做一点微小改动 —— 把 250 次投掷中的正面数从 140 增加到 141 —— 我们会发现 p-value 跌到那个神秘数值 0.05 以下（p-value 为 0.0497）。抽样理论统计学家会欣然尖叫：「得到像 141 次正面这样极端结果的概率小于 0.05 —— 因此我们在 5% 的 significance level 上拒绝零假设。」正确的答案由图 3.12 中若干 $\alpha$ 取值给出。此表中值得强调的数值有两个：一是 $H_1$ 使用标准均匀 prior 时的 likelihood ratio，它是 1:0.61，**支持**零假设 $H_0$；二是从 $H_1$ 角度看最有利的 $\alpha$ 取值，也只能给出约 2.3:1 的 likelihood ratio 支持 $H_1$。

**Be warned!（警告！）** p-value 为 0.05 常被解读为「赔率约以二十比一不利于零假设」。但此例的真相是：这些证据或者略微支持零假设，或者（依 prior 的选择）至多以 2.3 比一不利于它。

经典统计学的 p-values 与「significance levels」应当以极度审慎的态度对待。**避开它们！** 说教到此结束。


> <span style="color:#7f8c8d;">p.77 ⇄ 书内 p.65</span>

## Part I — Data Compression（第一编：数据压缩）


> <span style="color:#7f8c8d;">p.78 ⇄ 书内 p.66</span>

### About Chapter 4（关于第 4 章）

本章讨论如何度量一次随机实验结果的 information content。

本章有几处难点。若你觉得数学细节吃力，就粗略读过、继续前行 —— 即使不掌握本章的工具，你也能享受第 5、6 章。

在读第 4 章之前，你应当已读过第 2 章，并做过习题 2.21–2.25 与 2.16（pp.36–37），以及下面这道习题 4.1。

下面这道习题意在帮你思考「如何度量 information content」。

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 4.1. <span style="color:#7f8c8d;">[2, p.69]</span>

– Please work on this problem before reading Chapter 4.（请在第 4 章之前先做这道题。）

You are given 12 balls, all equal in weight except for one that is either heavier or lighter. You are also given a two-pan balance to use. In each use of the balance you may put any number of the 12 balls on the left pan, and the same number on the right pan, and push a button to initiate the weighing; there are three possible outcomes: either the weights are equal, or the balls on the left are heavier, or the balls on the left are lighter. Your task is to design a strategy to determine which is the odd ball and whether it is heavier or lighter than the others in as few uses of the balance as possible.

While thinking about this problem, you may find it helpful to consider the following questions:

> (a) How can one measure information?
>
> (b) When you have identified the odd ball and whether it is heavy or light, how much information have you gained?
>
> (c) Once you have designed a strategy, draw a tree showing, for each of the possible outcomes of a weighing, what weighing you perform next. At each node in the tree, how much information have the outcomes so far given you, and how much information remains to be gained?
>
> (d) How much information is gained when you learn (i) the state of a flipped coin; (ii) the states of two flipped coins; (iii) the outcome when a four-sided die is rolled?
>
> (e) How much information is gained on the first step of the weighing problem if 6 balls are weighed against the other 6? How much is gained if 4 are weighed against 4 on the first step, leaving out 4 balls?

> <span style="color:#7f8c8d;">[notation 边注] 记号一览：$x \in A$ 表示 $x$ 是集合 $A$ 的成员；$S \subset A$ 表示 $S$ 是 $A$ 的子集；$S \subseteq A$ 表示 $S$ 是 $A$ 的子集或等于 $A$；$V = B \cup A$ 表示 $V$ 是集合 $B$ 与 $A$ 的并集；$V = B \cap A$ 表示 $V$ 是 $B$ 与 $A$ 的交集；$|A|$ 表示集合 $A$ 中元素的个数。</span>


> <span style="color:#7f8c8d;">p.79 ⇄ 书内 p.67</span>

## 4 The Source Coding Theorem（信源编码定理）

### 4.1 How to measure the information content of a random variable?（如何度量一个随机变量的 information content？）

接下来几章我们要讨论概率分布与随机变量。绝大多数时候，用马虎点的记号就够了；但偶尔我们需要精确的记号。以下就是我们在第 2 章确立的记号。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Ensemble（系综）</span>

一个 **ensemble** $X$ 是一个三元组 $(x, \mathcal{A}_X, P_X)$，其中结果 $x$ 是某个随机变量的取值，该随机变量取遍一个可能值集合中的某一个，

```math
\mathcal{A}_X = \{a_1, a_2, \ldots, a_i, \ldots, a_I\},
```

各值具有概率

```math
P_X = \{p_1, p_2, \ldots, p_I\}, \quad \text{with } P(x = a_i) = p_i,\ p_i \ge 0 \text{ and } \sum_{a_i \in \mathcal{A}_X} P(x = a_i) = 1.
```

我们如何度量这样一个 ensemble 中结果 $x = a_i$ 的 information content？本章要考察两条主张：

1. **Shannon information content**

```math
h(x = a_i) \equiv \log_2 \frac{1}{p_i} \tag{4.1}
```

是结果 $x = a_i$ 的 information content 的一个合理度量；以及

2. **ensemble 的 entropy**

```math
H(X) = \sum_i p_i \log_2 \frac{1}{p_i} \tag{4.2}
```

是该 ensemble 的**平均** information content 的一个合理度量。

[Figure 4.1：Shannon information content $h(p) = \log_2 \frac{1}{p}$ 与 binary entropy function $H_2(p) = H(p, 1-p) = p \log_2 \frac{1}{p} + (1-p)\log_2 \frac{1}{1-p}$ 作为 $p$ 的函数图。左图 $h(p)$ 在 $p \to 0$ 时发散（$p=0.001$ 时 $h=10.0$；$p=0.01$ 时 6.6；$p=0.1$ 时 3.3；$p=0.2$ 时 2.3；$p=0.5$ 时 1.0），右图 $H_2(p)$ 呈帽形，$p=0.5$ 时取最大值 1]

图 4.1 给出了概率为 $p$ 的结果的 Shannon information content 作为 $p$ 的函数。一个结果越不可能，其 Shannon information content 越大。图 4.1 同时还给出了 **binary entropy function**（二元熵函数）

```math
H_2(p) = H(p, 1-p) = p \log_2 \frac{1}{p} + (1-p)\log_2 \frac{1}{1-p}, \tag{4.3}
```

它是字母表与概率分布为 $\mathcal{A}_X = \{\mathrm{a}, \mathrm{b}\}$、$P_X = \{p, 1-p\}$ 的那个 ensemble $X$ 的 entropy。


> <span style="color:#7f8c8d;">p.80 ⇄ 书内 p.68</span>

### Information content of independent random variables（独立随机变量的 information content）

为什么 $\log 1/p_i$ 会与 information content 有关？为什么不是 $p_i$ 的某个别的函数？这个问题我们稍后会详细探讨；但先注意函数 $h(x) = \log 1/p(x)$ 的这个漂亮性质。

设想你去了解两个**独立**随机变量 $x$ 与 $y$ 的取值。独立的定义是：概率分布可分解为乘积

```math
P(x, y) = P(x)P(y). \tag{4.4}
```

直觉上，我们可能希望任何「获得的信息量」的度量都具备**可加性** —— 也就是说，对于独立随机变量 $x$ 与 $y$，「同时得知 $x$ 与 $y$ 所得的信息」应当等于「只得知 $x$ 所得的信息」加上「只得知 $y$ 所得的信息」。

结果 $x, y$ 的 Shannon information content 是

```math
h(x, y) = \log \frac{1}{P(x, y)} = \log \frac{1}{P(x)P(y)} = \log \frac{1}{P(x)} + \log \frac{1}{P(y)}, \tag{4.5}
```

所以它确实满足

```math
h(x, y) = h(x) + h(y), \quad \text{if } x \text{ and } y \text{ are independent}. \tag{4.6}
```

#### <span style="color:#2471a3;">**[exercise]**</span> Exercise 4.2. <span style="color:#7f8c8d;">[1, p.86]</span>

Show that, if $x$ and $y$ are independent, the entropy of the outcome $x, y$ satisfies

```math
H(X, Y) = H(X) + H(Y). \tag{4.7}
```

用文字说：**对独立变量，entropy 是可加的。**

下面我们用一些例子来探讨这些想法；随后在 §4.4 以及第 5、6 章中，我们将证明 Shannon information content 与 entropy 同「描述一次实验结果所需的比特数」有关。

### The weighing problem: designing informative experiments（称球问题：设计有信息量的实验）

你解出称球问题（习题 4.1，p.66）了吗？确定吗？注意：三次使用天平（读数分别为「左重」「右重」「平衡」）时，可设想的结果数为 $3^{3} = 27$，而世界的可能状态数为 24：那个异球可以是十二个球中的任意一个，且它可能偏重或偏轻。所以原则上这个问题三次称量可解 —— 但两次不行，因为 $3^{2} < 24$。

若你已知道如何在三次称量中确定异球及其偏重偏轻，可以继续读下去。若你还没找到一种**总能**在三次内达成的策略，我鼓励你再想想习题 4.1。

你的策略为什么最优？你那一串称量究竟凭什么让有用的信息尽可能快地积累起来？答案是：在一个最优流程的每一步，三种结果（「左重」「右重」「平衡」）都尽可能接近等概率。一个最优解示于图 4.2。

[Figure 4.2：称球问题的最优策略树 —— 每个节点是一次称量，三条分支对应「左重 / 平衡 / 右重」，叶子标出异球的身份与偏重偏轻。原图印在下页（p.69），本切片（止于 p.68）只包含图号引用]

次优的策略 —— 例如第一步把 1–6 号球放在一盘、7–12 号球放在另一盘相称 —— 并不能让所有结果等概率：这两组球**永远不可能平衡**，所以只可能出现「左重」与「右重」两种结果。这样一个二元结果只能排除一半的可能假设，


<span style="color:#7f8c8d">书内 p069 ｜ 4.1: How to measure the information content of a random variable?</span>

[Figure 4.2：weighing problem（天平称重问题）的一个最优解。每一步有两个方框：左框显示哪些 hypothesis（假设）仍然可能；右框显示下一次称重要上秤的球。24 个 hypothesis 记作 1+, . . . , 12-，例如 1+ 表示 1 号球是 odd ball（异球）且它是 heavy（偏重）的。称重通过列出两侧盘上的球名来书写，两侧之间用一条线分开；例如在第一次称重中，球 1、2、3、4 放在左边，球 5、6、7、8 放在右边。在每一组三支箭头中，上方箭头指向左边更重的情形，中间箭头指向右边更重的情形，下方箭头指向两边 balanced（平衡）的情形。三个被标注的点对应 impossible（不可能）的结果。]

（承接上一页）于是，一个会用到这类结果的策略，有时必须花更长时间才能找到正确答案。

「结果应当尽可能接近 equiprobable（等概率）」这一洞见，使得寻找最优策略变得容易。第一次称重必须把 24 个可能 hypothesis 分成三组、每组八个。随后第二次称重的选法必须给出 hypothesis 的 3:3:2 划分。

于是我们或许可以这样下结论：

> 当结果上的 probability distribution（概率分布）是 uniform（均匀）时，一个随机实验的结果保证是信息量最大的。

这个结论与你在解 exercise 2.25（p.37）时证明过的 entropy（熵）的性质一致：如果所有结果等概率 $p_i = 1/|\mathcal{A}_X|$，那么 ensemble（系综）$X$ 的 entropy 最大。

#### Guessing games（猜数游戏）

在 twenty questions（二十问）游戏里，一个人心里想一个物体，另一个人通过问答案为 yes/no 的问题来猜这个物体是什么，例如「它是活的吗？」或「它是人吗？」。目标是用尽可能少的问题确定这个物体。玩这个游戏的最佳策略是什么？为简单起见，设想我们玩的是 twenty questions 里相当乏味的一种版本，叫做 sixty-three（六十三）。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 4.3（例 4.3）</span>

游戏 sixty-three。要用多少个 yes/no 问题，才能确定 0 到 63 之间的一个整数 $x$？

直觉上，最好的问题会接连把 64 种可能划分成大小相等的集合。六个问题就够了。一个合理的策略问下列问题：

```math
\begin{aligned}
1 &: \quad \text{is } x \ge 32?\\
2 &: \quad \text{is } x \bmod 32 \ge 16?\\
3 &: \quad \text{is } x \bmod 16 \ge 8?\\
4 &: \quad \text{is } x \bmod 8 \ge 4?\\
5 &: \quad \text{is } x \bmod 4 \ge 2?\\
6 &: \quad \text{is } x \bmod 2 = 1?
\end{aligned}
```

[记号 $x \bmod 32$ 读作「$x$ 模 32」，表示 $x$ 除以 32 之后的余数；例如 $35 \bmod 32 = 3$，$32 \bmod 32 = 0$。]

这些问题的答案，如果从 {yes, no} 翻译成 {1, 0}，就给出 $x$ 的 binary expansion（二进制展开），例如 $35 \to 100011$。$\square$


<span style="color:#7f8c8d">书内 p070 ｜ 4 -- The Source Coding Theorem</span>

这个例子里各结果的 Shannon information content（Shannon 信息量）是多少？如果我们假设 $x$ 的所有取值等可能，那么这些问题的答案是相互 independent（独立）的，每个答案的 Shannon information content 都是 $\log_2(1/0.5) = 1$ bit；获得的 Shannon information 总量总是六个 bit。此外，我们从这些问题中学到的数 $x$ 是一个六 bit 的二进制数。我们的提问策略定义了一种把随机变量 $x$ 编码成二进制文件的方式。

到此为止，Shannon information content 是说得通的：它度量的是一个编码 $x$ 的二进制文件的长度。然而，我们还没有研究结果概率不等的 ensemble。在那里，Shannon information content 是否仍然说得通？


<span style="color:#7f8c8d">书内 p071 ｜ 4.1: How to measure the information content of a random variable?</span>

[Figure 4.3：一局 submarine（潜艇）游戏。潜艇在第 49 次尝试时被击中。]

#### The game of submarine: how many bits can one bit convey?（submarine 游戏：一个 bit 能传递多少 bit？）

在 battleships（战舰）游戏里，每个玩家把一支舰队藏在用方格网表示的海域中。每一轮，一个玩家向对方海域的某一格开火，试图击中对方的船。对诸如「G3」这样被选中的格子，回应可能是「miss（未中）」、「hit（击中）」或「hit and destroyed（击中并击沉）」。

在 battleships 的一个乏味版本里，这个版本叫做 submarine，每个玩家只把一艘潜艇藏在 $8 \times 8$ 网格的某一格里。图 4.3 显示了游戏进行中的几幅画面：圆圈代表正在被开火的格子，而 $\cdot$ 表示结果为 miss 的格子，记作 $x = n$；潜艇在第 49 次尝试时被击中（结果 $x = y$，用符号 $\bullet$ 表示）。

玩家每打一枪都定义一个 ensemble。两个可能的结果是 $\{y, n\}$，分别对应 hit 与 miss，它们的概率取决于棋盘的状态。开始时，$P(y) = 1/64$，$P(n) = 63/64$。在第二次射击时，如果第一枪没中，$P(y) = 1/63$，$P(n) = 62/63$。在第三次射击时，如果前两枪都没中，$P(y) = 1/62$，$P(n) = 61/62$。

从一个结果 $x$ 获得的 Shannon information 是 $h(x) = \log(1/P(x))$。如果我们运气好，第一枪就击中潜艇，那么

```math
h(x) = h^{(1)}(y) = \log_2 64 = 6 \text{ bits}. \qquad (4.8)
```

现在看来，一个二值结果能够传达六个 bit，也许显得有点奇怪。但我们学到了藏身之处，它本来可以是 64 个格子中的任何一个；所以，靠一个幸运的二值问题，我们确实学到了六个 bit。

如果第一枪没中呢？从这个结果获得的 Shannon information 是

```math
h(x) = h^{(1)}(n) = \log_2 \frac{64}{63} = 0.0227 \text{ bits}. \qquad (4.9)
```

这说得通吗？并不那么显然。我们继续往下走。如果第二枪也没中，第二个结果的 Shannon information content 是

```math
h^{(2)}(n) = \log_2 \frac{63}{62} = 0.0230 \text{ bits}. \qquad (4.10)
```

如果我们连打三十二枪都没中（每次都打新格子），获得的 Shannon information 总量是

```math
\begin{aligned}
&\log_2 \frac{64}{63} + \log_2 \frac{63}{62} + \cdots + \log_2 \frac{33}{32}\\
&\quad = 0.0227 + 0.0230 + \cdots + 0.0430 = 1.0 \text{ bit}. \qquad (4.11)
\end{aligned}
```


<span style="color:#7f8c8d">书内 p072 ｜ 4 -- The Source Coding Theorem</span>

为什么是这个整数？那么，我们学到了什么？我们现在知道潜艇不在我们开过火的 32 个格子中的任何一个里；学到这个事实，就相当于玩一局 sixty-three（p.70），把「$x$ 是不是我打过的那三十二个格子对应的数字之一？」作为第一个问题，并收到答案「不是」。这个答案排除了 half of the hypotheses（一半假设），所以它给了我们一个 bit。

在 48 次不中之后，获得的信息是两个 bit：未知位置已经被缩小到原 hypothesis 空间（假设空间）的四分之一。

如果我们在第 49 枪击中潜艇，此时还剩 16 个格子呢？这个结果的 Shannon information content 是

```math
h^{(49)}(y) = \log_2 16 = 4.0 \text{ bits}. \qquad (4.12)
```

所有结果的 Shannon information content 总量是

```math
\begin{aligned}
&\log_2 \frac{64}{63} + \log_2 \frac{63}{62} + \cdots + \log_2 \frac{17}{16} + \log_2 \frac{16}{1}\\
&\quad = 0.0227 + 0.0230 + \cdots + 0.0874 + 4.0 = 6.0 \text{ bits}. \qquad (4.13)
\end{aligned}
```

所以一旦我们知道潜艇在哪里，获得的 Shannon information content 总量就是六个 bit。

这个结果与我们在潜艇还剩多少个格子可挑时击中它无关——在 (4.13) 式中是 16 个。如果击中时还剩 $n$ 个格子可挑，那么获得的信息总量是

```math
\begin{aligned}
&\log_2 \frac{64}{63} + \log_2 \frac{63}{62} + \cdots + \log_2 \frac{n+1}{n} + \log_2 \frac{n}{1}\\
&\quad = \log_2 \frac{64}{63} \cdot \frac{63}{62} \cdots \frac{n+1}{n} \cdot \frac{n}{1} = \log_2 \frac{64}{1} = 6 \text{ bits}. \qquad (4.14)
\end{aligned}
```

到目前这些例子教给我们什么？我认为 submarine 这个例子相当有说服力地支持了如下主张：Shannon information content 是信息量的一个合理度量。而 sixty-three 这个游戏表明，Shannon information content 可以与「编码一个随机实验结果的文件有多大」紧密相关，这就暗示了它与 data compression（数据压缩）之间可能的联系。

万一你还没被说服，我们再看一个例子。

#### The Wenglish language（Wenglish 语言）

Wenglish 是一门类似英语的语言。Wenglish 的句子由词组成，词从 Wenglish 词典中随机抽取；该词典含 $2^{15} = 32{,}768$ 个词，所有词长都是五个字符。词典中的每个词，都是按图 2.1 中 a. . . z 上的概率分布随机取五个字母构造出来的。

词典中的一些条目按字母顺序列在图 4.4 中。注意词典中的词数（32,768）远小于长度为五个字母的全部可能词数 $26^5 \simeq 12{,}000{,}000$。

由于字母 z 的概率约为 1/1000，词典中只有 32 个词以字母 z 开头。相比之下，字母 a 的概率约为 0.0625，有 2048 个词以字母 a 开头。在那 2048 个词中，有两个以 az 开头，有 128 个以 aa 开头。

[Figure 4.4：Wenglish 词典。]

设想我们正在读一份 Wenglish 文档，并随着字符一个个被我们获得，讨论它们的 Shannon information content。如果我们


<span style="color:#7f8c8d">书内 p073 ｜ 4.2: Data compression</span>

一次一个词地把文本拿到手，那么每个五字符词的 Shannon information content 是 $\log 32{,}768 = 15$ bits，因为 Wenglish 以等概率使用它所有的词。于是每个字符的平均 information content 是三个 bit。

现在我们看一次一个字符读这份文档时的 information content。比如说，如果一个词的首字母是 a，那么 Shannon information content 是 $\log_2 1/0.0625 = 4$ bits。如果首字母是 z，Shannon information content 是 $\log_2 1/0.001 \approx 10$ bits。因此在第一个字符上，information content 变化极大。然而一个词中五个字符的 information content 总量恰好是 15 bits；所以跟在首字母 z 之后的那些字母，每字符的平均 information content 低于跟在首字母 a 之后的字母。一个罕见的首字母（如 z）确实比一个常见的首字母传达了更多关于「这个词是什么」的信息。

同理，在英语里，如果罕见的字符出现在词首（例如 xyl. . .），那么我们往往能立即辨认出整个词；而以常见字符开头的词（例如 pro. . .）则需要更多字符才能辨认出来。

### 4.2 Data compression（数据压缩）

前面的例子支持了这个想法：一个结果的 Shannon information content 是它的信息量的一个自然度量。improbable（不大可能的）结果确实比 probable（可能的）结果传达更多信息。现在我们通过考察「描述一次实验的结果需要多少个 bit」来讨论一个 source（信源）的 information content。

如果我们能够证明，可以把来自某个特定 source 的数据压缩成一个文件，该文件每 source symbol（信源符号）占 $L$ 个 bit 且能可靠地恢复数据，那么我们就会说，该 source 的平均 information content 至多是每符号 $L$ 个 bit。

> <span style="color:#7f8c8d">[note] 这里我们使用「bit」一词的含义是「一个取两个值的符号」，不要把它与 information content 的单位混为一谈。</span>

#### Example: compression of text files（例：文本文件的压缩）

一个文件由一串 byte（字节）组成。一个 byte 由 8 个 bit 组成，它的十进制取值可以在 0 到 255 之间。一个典型的文本文件由 ASCII character set（ASCII 字符集）构成（十进制取值 0 到 127）。这个字符集只用到 byte 八个 bit 中的七个。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.4 [1, p.86]</span>

By how much could the size of a file be reduced given that it is an ASCII file? How would you achieve this reduction?


<span style="color:#7f8c8d">书内 p074 ｜ 4 -- The Source Coding Theorem</span>

直觉上，如下断言似乎是合理的：一个 ASCII 文件所含的信息量是同样大小的任意文件的 7/8，因为在我们还没看这个文件之前，八个 bit 里就已经有一个是已知的了。这是 redundancy（冗余）的一个简单例子。大多数数据 source 还有进一步的 redundancy：英语文本文件以不等的频率使用 ASCII 字符；某些字母对出现的概率高于其他字母对；而只要给定上下文和对文本的 semantic understanding（语义理解），整个词都可以预测出来。

#### 一些简单的 data compression 方法，它们定义了 information content 的度量

度量一个随机变量 information content 的一种方法，就是简单地去数可能结果的个数 $|\mathcal{A}_X|$。（集合 $A$ 中元素的个数记作 $|A|$。）如果我们给每个结果一个二进制名字，那么每个名字的长度就是 $\log_2 |\mathcal{A}_X|$ bit，前提是 $|\mathcal{A}_X|$ 恰好是 2 的幂。于是我们作如下定义。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：raw bit content（原始 bit 含量）</span>

<span style="color:#00838f">$X$ 的 raw bit content 是</span>

```math
H_0(X) = \log_2 |\mathcal{A}_X|. \qquad (4.15)
```

<span style="color:#00838f">$H_0(X)$ 是「总能把 ensemble $X$ 中的一个结果确定出来的二进制问题个数」的下界。它是一个 additive（可加的）量：有序对 $x, y$ 有 $|\mathcal{A}_X||\mathcal{A}_Y|$ 个可能结果，其 raw bit content 满足</span>

```math
H_0(X, Y) = H_0(X) + H_0(Y). \qquad (4.16)
```

这个 information content 的度量不包含任何 probabilistic（概率的）成分，与它对应的编码规则也不「压缩」source 数据，它只是把每个结果映射成一个定长的二进制串。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.5 [2, p.86]</span>

Could there be a compressor that maps an outcome x to a binary code c(x), and a decompressor that maps c back to x, such that every possible outcome is compressed into a binary code of length shorter than H0(X) bits?

尽管一个简单的计数论证就表明，不可能做出一个能让所有文件都变小的可逆压缩程序，业余压缩爱好者却经常宣称自己发明了这样的程序——甚至还宣称，把自己的压缩器反复作用于已压缩文件，就能进一步压缩它们。更奇怪的是，专利已经被授予这些当代炼金术士。进一步的阅读材料见 comp.compression 的 frequently asked questions（常见问题）。

一个「压缩器」要真正压缩文件，只有两条路：

1. lossy compressor（有损压缩器）压缩某些文件，但把某些文件映射到同一个编码。我们假定用户要求完美恢复 source 文件，所以一旦碰上这些 confusable files（可混淆文件）中的某一个，就导致失败（不过在 image compression 这类应用中，lossy compression 被视为可接受）。我们用 $\delta$ 记 source 串属于那些 confusable files 的概率，于是 lossy compressor 有一个 $\delta$ 的失败概率。如果 $\delta$ 可以做得非常小，那么 lossy compressor 在实践中可能是有用的。

2. lossless compressor（无损压缩器）把所有文件映射到不同的编码；如果它缩短了某些文件，就必然使另一些文件变长。我们设法设计压缩器，使得「文件被拉长」的概率很小，而「文件被缩短」的概率很大。

本章我们讨论一个简单的 lossy compressor。在随后的章节中我们讨论 lossless compression 方法。

### 4.3 Information content defined in terms of lossy compression（用 lossy compression 定义 information content）

无论构造哪一类压缩器，我们都需要想办法把不同结果的概率考虑进来。设想比较两个文本文件的 information content——一个文件里 128 个 ASCII 字符等概率使用，另一个文件里字符按它们在英语文本中的频率使用。我们能否定义一个 information content 的度量，把这两个文件区分开来？直觉上，后一个文件每字符所含的信息更少，因为它更可预测。


<span style="color:#7f8c8d">书内 p075 ｜ 4.3: Information content defined in terms of lossy compression</span>

利用「某些符号概率更小」这一知识，一种简单做法是：设想把观测值 recode（重新编码）到一个更小的 alphabet（字母表）上——从而失去编码某些不大可能符号的能力——然后度量新 alphabet 的 raw bit content。例如，在压缩英语文本时我们可以冒个险，猜最不频繁的字符不会出现，做一个缩减的 ASCII 码，略去字符 { !, @, #, %, ^, *, ~, <, >, /, \, _, {, }, [, ], | }，这样就把 alphabet 缩小了十七个。我们愿意承担的风险越大，最终得到的 alphabet 就越小。

我们引入一个参数 $\delta$ 来描述使用这种压缩方法时承担的风险：$\delta$ 是「结果 $x$ 没有名字」的概率。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 4.6（例 4.6）</span>

设

```math
\mathcal{A}_X = \{ a, b, c, d, e, f, g, h \}, \qquad (4.17)
```

以及 $P_X = \{\, \tfrac{1}{4}, \tfrac{1}{4}, \tfrac{1}{4}, \tfrac{3}{16}, \tfrac{1}{64}, \tfrac{1}{64}, \tfrac{1}{64}, \tfrac{1}{64} \,\}$。

这个 ensemble 的 raw bit content 是 3 bit，对应 8 个二进制名字。但注意 $P(x \in \{a, b, c, d\}) = 15/16$。所以如果我们愿意承担 $\delta = 1/16$ 的风险（即 $x$ 没有名字），那么四个名字就够了——是「每个 $x \in \mathcal{A}_X$ 都有名字」时所需名字数的一半。

Table 4.5 给出了在 $\delta = 0$ 与 $\delta = 1/16$ 两种情况下可以给各结果的二进制名字。当 $\delta = 0$ 时编码结果需要 3 bit；当 $\delta = 1/16$ 时只需 2 bit。

[Table 4.5：两种失败概率 $\delta$ 下给结果的二进制名字。

| $\delta = 0$ | | $\delta = 1/16$ | |
|---|---|---|---|
| $x$ | $c(x)$ | $x$ | $c(x)$ |
| a | 000 | a | 00 |
| b | 001 | b | 01 |
| c | 010 | c | 10 |
| d | 011 | d | 11 |
| e | 100 | e | – |
| f | 101 | f | – |
| g | 110 | g | – |
| h | 111 | h | – |]

现在把这个想法形式化。要做一个风险为 $\delta$ 的压缩策略，我们取尽可能小的子集 $S$，使得 $x$ 不在 $S$ 中的概率小于或等于 $\delta$，即 $P(x \in S) \ge 1 - \delta$。对每个 $\delta$ 的取值，我们于是可以定义一个新的 information content 度量——这个最小子集 $S$ 的大小之对数。[在若干元素概率相同的 ensemble 中，可能存在若干个包含不同元素的最小（同大小）子集，但重要的只是它们的大小（彼此相等），故我们不再纠缠这个歧义。]

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：smallest $\delta$-sufficient subset（最小 $\delta$-充分子集）</span>

<span style="color:#00838f">最小的 $\delta$-sufficient subset $S_\delta$ 是 $\mathcal{A}_X$ 的满足</span>

```math
P(x \in S_\delta) \ge 1 - \delta \qquad (4.18)
```

<span style="color:#00838f">的最小子集。子集 $S_\delta$ 可以这样构造：把 $\mathcal{A}_X$ 的元素按概率递减排序，从最可能的元素开始逐个加入，直到总概率达到 $(1-\delta)$。</span>

给最小 sufficient 子集的每个元素指派一个二进制名字，就得到一个 data compression code（数据压缩码）。这个压缩方案引出如下 information content 度量。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：essential bit content（本质 bit 含量）</span>

<span style="color:#00838f">$X$ 的 essential bit content 是</span>

```math
H_\delta(X) = \log_2 |S_\delta|. \qquad (4.19)
```

注意 $H_0(X)$ 是 $H_\delta(X)$ 在 $\delta = 0$ 时的特例（若对所有 $x \in \mathcal{A}_X$ 都有 $P(x) > 0$）。[当心：不要把 $H_0(X)$ 和 $H_\delta(X)$ 与图 4.1 展示的函数 $H_2(p)$ 混淆。]

图 4.6 把 Example 4.6 的 ensemble 的 $H_\delta(X)$ 作为 $\delta$ 的函数画了出来。


<span style="color:#7f8c8d">书内 p076 ｜ 4 -- The Source Coding Theorem</span>

[Figure 4.6：(a) $X$ 的结果（来自 Example 4.6（p.75）），按概率排序；(b) essential bit content $H_\delta(X)$。图上标注显示作为 $\delta$ 函数的最小 sufficient set。注意 $H_0(X) = 3$ bit 而 $H_{1/16}(X) = 2$ bit。图中阶梯依次为 $\{a,b,c,d,e,f,g,h\}$、$\{a,b,c,d,e,f,g\}$、$\{a,b,c,d,e,f\}$、$\{a,b,c,d,e\}$、$\{a,b,c,d\}$、$\{a,b,c\}$、$\{a,b\}$、$\{a\}$。]

#### Extended ensembles（扩展 ensemble）

如果我们压缩 source 的符号块，这个压缩方法会更有用吗？

我们现在转向这样的例子：结果 $x = (x_1, x_2, \ldots, x_N)$ 是来自同一个 ensemble $X$ 的 $N$ 个 independent identically distributed（独立同分布，i.i.d.）随机变量构成的串。我们把 ensemble $(X_1, X_2, \ldots, X_N)$ 记作 $X^N$。记住 entropy 对 independent 变量是可加的（exercise 4.2（p.68）），所以 $H(X^N) = N H(X)$。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 4.7（例 4.7）</span>

考虑 $N$ 次 bent coin（弯曲硬币）投掷构成的串，$x = (x_1, x_2, \ldots, x_N)$，其中 $x_n \in \{0, 1\}$，概率为 $p_0 = 0.9$、$p_1 = 0.1$。最可能的串 $x$ 是那些含 0 最多的串。如果 $r(x)$ 是 $x$ 中 1 的个数，那么

```math
P(x) = p_0^{N-r(x)}\, p_1^{r(x)}. \qquad (4.20)
```

要评估 $H_\delta(X^N)$，我们必须找到最小的 sufficient subset $S_\delta$。这个子集将包含所有满足 $r(x) = 0, 1, 2, \ldots$ 直到某个 $r_{\max}(\delta) - 1$ 的 $x$，以及满足 $r(x) = r_{\max}(\delta)$ 的那部分 $x$。图 4.7 和图 4.8 画出了 $N = 4$ 与 $N = 10$ 两种情况下 $H_\delta(X^N)$ 对 $\delta$ 的图形。那些台阶就是 $|S_\delta|$ 改变 1 的 $\delta$ 值，而阶梯斜率发生变化的尖点，正是 $r_{\max}$ 改变 1 的点。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.8 [2, p.86]</span>

What are the mathematical shapes of the curves between the cusps?

对于图 4.6–4.8 所示的例子，$H_\delta(X^N)$ 强烈依赖于 $\delta$ 的取值，所以它似乎不像一个基本的、有用的 information content 定义。但是我们要考察当 $N$（即 $X^N$ 中 independent 变量的个数）增大时会发生什么。我们将发现一个值得注意的结果：$H_\delta(X^N)$ 变得几乎与 $\delta$ 无关——而且对所有 $\delta$ 它都非常接近 $N H(X)$，其中 $H(X)$ 是其中一个随机变量的 entropy。

图 4.9 用 Example 4.7 的二值 ensemble 说明了这一 asymptotic（渐近的）趋势。随着 $N$ 增大，$\frac{1}{N} H_\delta(X^N)$ 成为一个越来越平坦的函数，


<span style="color:#7f8c8d">书内 p077 ｜ 4.3: Information content defined in terms of lossy compression</span>

[Figure 4.7：(a) 当 $p_1 = 0.1$ 时 ensemble $X^4$ 的十六个结果，按概率排序。(b) essential bit content $H_\delta(X^4)$。上方示意条用竖线长度（不成比例）标出各串的概率。图中标注的分组依次为 $1111$、$1101, 1011, \ldots$、$0110, 1010, \ldots$、$0010, 0001, \ldots$、$0000$。]

[Figure 4.8：$N = 10$ 个二值变量（$p_1 = 0.1$）时的 $H_\delta(X^{10})$。图中曲线标注 $N = 4$ 与 $N = 10$。]

[Figure 4.9：$N = 10, 2^{10}, \ldots, 10^{10}$ 个二值变量（$p_1 = 0.1$）时 $\frac{1}{N} H_\delta(X^N)$ 随 $\delta$ 的变化。$N$ 越大曲线越平。]


<span style="color:#7f8c8d">书内 p078 ｜ 4 -- The Source Coding Theorem</span>

除了靠近 $\delta = 0$ 与 $\delta = 1$ 的两条尾巴之外。只要我们被允许一个极小的 error probability（错误概率）$\delta$，压缩到 $N H$ bit 就是可能的。即使我们被允许一个大的 error probability，我们也仍然只能压缩到 $N H$ bit。这就是 source coding theorem（信源编码定理）。

[Figure 4.10：上面十五个串是从 $X^{100}$ 中取出的样本，其中 $p_1 = 0.1$、$p_0 = 0.9$。最下面两个串是这个 ensemble 中概率最大与概率最小的串。最后一列给出这些随机串的 log-probabilities（对数概率），可与 entropy $H(X^{100}) = 46.9$ bits 相比较。各样本的 $\log_2 P(x)$ 依次为 $-50.1$、$-37.3$、$-65.9$、$-56.4$、$-53.2$、$-43.7$、$-46.8$、$-56.4$、$-37.3$、$-43.7$、$-56.4$、$-37.3$、$-56.4$、$-59.5$、$-46.8$；全零串为 $-15.2$，全一串为 $-332.1$。]

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 4.1（定理 4.1）：Shannon's source coding theorem（Shannon 信源编码定理）</span>

设 $X$ 是一个 entropy 为 $H(X) = H$ bit 的 ensemble。给定 $\epsilon > 0$ 与 $0 < \delta < 1$，存在一个正整数 $N_0$，使得对所有 $N > N_0$ 有

```math
\left| \frac{1}{N} H_\delta(X^N) - H \right| < \epsilon. \qquad (4.21)
```

### 4.4 Typicality（典型性）

为什么增大 $N$ 有帮助？我们来考察来自 $X^N$ 的长串。Table 4.10 显示了 $N = 100$、$p_1 = 0.1$ 时来自 $X^N$ 的十五个样本。一个含有 $r$ 个 1 和 $N - r$ 个 0 的串 $x$，其概率为

```math
P(x) = p_1^{r} (1 - p_1)^{N-r}. \qquad (4.22)
```

含有 $r$ 个 1 的串的个数是

```math
n(r) = \binom{N}{r}. \qquad (4.23)
```

于是 1 的个数 $r$ 服从 binomial distribution（二项分布）：

```math
P(r) = \binom{N}{r} p_1^{r} (1 - p_1)^{N-r}. \qquad (4.24)
```

这些函数画在图 4.11 中。$r$ 的均值是 $N p_1$，其标准差是 $\sqrt{N p_1 (1 - p_1)}$（p.1）。如果 $N$ 是 100，那么

```math
r \simeq N p_1 \pm \sqrt{N p_1 (1 - p_1)} \simeq 10 \pm 3. \qquad (4.25)
```


<span style="color:#7f8c8d">书内 p079 ｜ 4.4: Typicality</span>

[Figure 4.11：typical set $T$ 的解剖。对 $p_1 = 0.1$ 以及 $N = 100$ 与 $N = 1000$，这些图分别显示：$n(r)$，即含 $r$ 个 1 的串的个数；单个含 $r$ 个 1 的串的概率 $P(x)$；同一概率的对数尺度；以及含 $r$ 个 1 的全部串的总概率 $n(r)P(x)$。横轴是 $r$。$\log_2 P(x)$ 那张图还用虚线标出 $\log_2 P(x)$ 的均值 $= -N H_2(p_1)$，当 $N = 100$ 时等于 $-46.9$，当 $N = 1000$ 时等于 $-469$。typical set 只包含 $\log_2 P(x)$ 接近这个值的串。标以 $T$ 的区间显示第 4.4 节定义的集合 $T_N$：左边是 $N = 100$、$\delta = 0.29$，右边是 $N = 1000$、$\delta = 0.09$。]


<span style="color:#7f8c8d">书内 p080 ｜ 4 -- The Source Coding Theorem</span>

如果 $N = 1000$，那么

```math
r \simeq 100 \pm 10. \qquad (4.26)
```

注意随着 $N$ 变大，$r$ 的 probability distribution 变得更集中，这里的含义是：虽然 $r$ 可能取值的范围以 $N$ 的速度增长，但 $r$ 的标准差只以 $\sqrt{N}$ 的速度增长。$r$ 最可能落在一个小范围的取值里，这又意味着结果 $x$ 也最可能落在一个相应的小结果子集中，我们把这个子集称为 typical set（典型集）。

#### Definition of the typical set（typical set 的定义）

让我们对具有 alphabet $\mathcal{A}_X$ 的任意 ensemble $X$ 定义 typicality（典型性）。我们对典型串的定义会用到串的概率。一个由 $N$ 个符号组成的长串，通常大约含有 $p_1 N$ 个第一个符号、$p_2 N$ 个第二个符号，等等。因此这个串的概率大致是

```math
P(x)_{\text{typ}} = P(x_1)P(x_2)P(x_3)\ldots P(x_N) \simeq p_1^{(p_1 N)} p_2^{(p_2 N)} \ldots p_I^{(p_I N)}, \qquad (4.27)
```

于是典型串的 information content 是

```math
\log_2 \frac{1}{P(x)} \simeq N \sum_i p_i \log_2 \frac{1}{p_i} = N H. \qquad (4.28)
```

所以随机变量 $\log_2 1/P(x)$（也就是 $x$ 的 information content）极可能取值接近 $N H$。我们把 typicality 的定义建立在这一观察之上。

<span style="color:#00838f">我们把 $\mathcal{A}_X^N$ 中的 typical elements 定义为那些概率接近 $2^{-NH}$ 的元素。</span>（注意 typical set 与 smallest sufficient subset 不同，它并不包含 $\mathcal{A}_X^N$ 中概率最大的那些元素；但我们将会证明，这些最可能的元素贡献的概率可以忽略。）

我们引入一个参数 $\delta$，用它来定义「概率必须多接近 $2^{-NH}$ 才算典型」。我们把典型元素构成的集合称为 typical set $T_N$：

<span style="color:#1e8449;">**[译注]**</span> **typical set 的定义故意不用「概率最大的那些串」——因为最大的那几个串合起来概率趋于 0**

定义 (4.29) 是 $\left|\frac1N\log_2\frac{1}{P(x)}-H\right|<\delta$，即**按 information content 的密度**筛选，而不是按 $P(x)$ 排序取前 $2^{NH}$ 个。机制：$P(x)$ 的最大值出现在最"偏"的串（如 $p_1=0.1$ 时的全 0 串，$P=0.9^{1000}\approx 10^{-46}$），但这些串只有极少数个，其总概率 $\to0$；反过来 typical 串每个概率都是 $2^{-NH\pm\delta}$，数量 $2^{NH}$（主导阶），且总概率 $\to1$。两条陈述合起来才是 AEP：**概率 $1$ 集中在体积占比 $\to 0$ 的集合上**。

抽掉这个定义方式（改用"取概率最大的串"）会怎样：压缩定理的证明立刻断——因为你无法保证被编码的集合覆盖几乎全部概率，$P_e\to0$ 的结论没有来源。这也解释了为什么 §4.5 里必须先证 $\Pr(x\in T_N)\to1$ 再证 $|T_N|\le 2^{N(H+\delta)}$（两条夹出压缩率）。

数字：$N=1000$、$p_1=0.1$ 时 $r\simeq 100\pm10$（译文式 (4.26)），典型串概率 $\approx 2^{-469}$，典型集大小 $\approx 2^{469+o(N)}$，而 $|\mathcal{A}^N|=2^{1000}$——占比 $2^{-531}$，却承载几乎全部概率。

挂载：大数定律在这里以 $\sqrt N$ 的形式出现（$r$ 的标准差 $\sqrt{Np(1-p)}$；6.042J 二项分布 + Thomson 的收敛概念）；「按密度筛 vs 按值排序」的区别，与 6.006 里「取 top-$k$ 大元素」和「取覆盖 99% 权重的最小子集」是两种不同问题同构。

坐标：§4.4（原书 p.79–81，PDF p.91–93），定义与式 (4.27)–(4.29)；两条性质的证明在 §4.5（原书 p.81–83，PDF p.93–95）。


```math
T_N \equiv \left\{ x \in \mathcal{A}_X^N : \left| \frac{1}{N} \log_2 \frac{1}{P(x)} - H \right| < \delta \right\}. \qquad (4.29)
```

我们将证明：无论我们选取什么样的 $\delta$ 值，随着 $N$ 增大，typical set 都包含几乎全部概率。

这个重要结果有时被称为「asymptotic equipartition」（渐近均分）原理。

#### <span style="color:#c0392b">`Asymptotic equipartition' principle（渐近均分原理）</span>

对由 $N$ 个 independent identically distributed（i.i.d.）随机变量 $X^N = (X_1, X_2, \ldots, X_N)$ 构成的 ensemble，当 $N$ 足够大时，结果 $x = (x_1, x_2, \ldots, x_N)$ 几乎必然属于 $\mathcal{A}_X^N$ 的一个子集，该子集只有 $2^{N H(X)}$ 个成员，每个成员的概率「接近」$2^{-N H(X)}$。

注意如果 $H(X) < H_0(X)$，那么 $2^{N H(X)}$ 只是可能结果总数 $|\mathcal{A}_X^N| = |\mathcal{A}_X|^N = 2^{N H_0(X)}$ 的一个极小部分。

> <span style="color:#1e8449">[note] 之所以选用 equipartition 一词，是想表达「typical set 的成员概率大致相等」这个意思。[这不应被理解得太字面，所以我在「asymptotic equipartition」上加了引号；见 p.83。]</span>

> <span style="color:#1e8449">[note] equipartition 的第二个含义来自热物理，指经典系统的每个自由度具有相同的平均能量 $\frac{1}{2} k_B T$。这里并不指这第二个含义。</span>


<span style="color:#7f8c8d">书内 p081 ｜ 4.5: Proofs</span>

[Figure 4.12：示意图，把 ensemble $X^N$ 中所有串按概率排序，并标出 typical set $T_N$。纵轴是 $\log_2 P(x)$，图中标出的串从全 1 串（如 $1111111111110\ldots11111110111$）一路到全 0 串（如 $0000000000000\ldots00000000000$）。]

「asymptotic equipartition」原理等价于下面这句话：

#### <span style="color:#c0392b">Shannon's source coding theorem（Shannon 信源编码定理，文字陈述）</span>

$N$ 个各有 entropy $H(X)$ 的 i.i.d. 随机变量，当 $N \to \infty$ 时，可以压缩到多于 $N H(X)$ 个 bit，而信息损失的风险可以忽略；反过来说，如果把它们压缩到少于 $N H(X)$ 个 bit，那么几乎必然会有信息损失。

这两个定理是等价的，因为我们可以定义一个压缩算法，给 typical set 中的每个 $x$ 指派一个长度为 $N H(X)$ bit 的独特名字。

<span style="color:#1e8449;">**[译注]**</span> **信源编码定理的证明只需一句话式的构造：给 typical set 的每个成员一个 $NH$ bit 的名字——剩下的全是计数**

抽掉这个构造，定理就只剩"AEP"这个定性陈述。合法性的三条算术：① $\Pr(x\in T_N)\to1$（所以漏掉的成员造成的错误概率 $\to0$）；② $|T_N|\le 2^{N(H+\delta)}$（所以 $N(H+\delta)$ bit 的名字足够，编号是 $1..|T_N|$）；③ 反过来若码率 $<H-\delta$，则长度为 $N(H-\delta)$ 的名字最多标出 $2^{N(H-\delta)}$ 个串，而 typical set 更大，必有一半以上的典型串无法区分，错误概率不趋于 0（counting 论证，也就是 converse）。

注意这个定理**不含任何算法**：它只说「存在」这样的映射（给典型集编号，非典型串随意映射），所以它是存在性定理，不是压缩算法——真正的算法要到第 5、6 章（Huffman、arithmetic）才出现，而它们必须付出 $\le 1$ bit/符号或有限精度区间的小损失。这条分工与 §1.3 的噪声信道定理完全同构。

挂载：这就是 6.006 里「判定问题 vs 构造问题」的差别（存在性证明用计数，不给出可执行算法）；计数本身是 6.042J 的 pigeonhole：$2^{N(H-\delta)}$ 个名字无法标出 $2^{NH}$ 个成员。

坐标：§4.4 末（原书 p.81，PDF p.93），信源编码定理的文字陈述；严格证明 §4.5（原书 p.81–85，PDF p.93–97），含 $\Pr(x\in T_N)\to1$ 的两步夹逼。


### 4.5 Proofs（证明）

如果觉得这一节难懂，可以跳过。

#### The law of large numbers（大数定律）

我们对 source coding theorem 的证明要用到大数定律。

一个实随机变量的 mean（均值）与 variance（方差）是

```math
E[u] = \bar{u} = \sum_u P(u)\, u
```

以及

```math
\operatorname{var}(u) = \sigma^2 = E[(u - \bar{u})^2] = \sum_u P(u)\, (u - \bar{u})^2.
```

> <span style="color:#1e8449">[note] 技术说明：严格说，我在这里假设 $u$ 是取自有限离散 ensemble $X$ 的样本 $x$ 的函数 $u(x)$。那么求和 $\sum_u P(u) f(u)$ 应当写成 $\sum_x P(x) f(u(x))$。这意味着 $P(u)$ 是一族有限个 delta 函数之和。这个限制保证了 $u$ 的 mean 与 variance 存在，而对一般的 $P(u)$ 未必如此。</span>

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Chebyshev's inequality 1（Chebyshev 不等式 1）</span>

设 $t$ 是一个非负实随机变量，设 $\alpha$ 是一个正实数。那么

```math
P(t \ge \alpha) \le \frac{\bar{t}}{\alpha}. \qquad (4.30)
```

[proof] *Proof（证明）：* $P(t \ge \alpha) = \sum_{t \ge \alpha} P(t)$。我们把每一项乘以 $t/\alpha \ge 1$，得到 $P(t \ge \alpha) \le \sum_{t \ge \alpha} P(t)\, t/\alpha$。再把（非负的）遗漏项加上去，得到 $P(t \ge \alpha) \le \sum_t P(t)\, t/\alpha = \bar{t}/\alpha$。$\square$


<span style="color:#7f8c8d">书内 p082 ｜ 4 -- The Source Coding Theorem</span>

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Chebyshev's inequality 2（Chebyshev 不等式 2）</span>

设 $x$ 是一个随机变量，设 $\alpha$ 是一个正实数。那么

```math
P\left( (x - \bar{x})^2 \ge \alpha \right) \le \sigma_x^2 / \alpha. \qquad (4.31)
```

[proof] *Proof（证明）：* 取 $t = (x - \bar{x})^2$，并应用上一个命题。$\square$

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Weak law of large numbers（弱大数定律）</span>

取 $x$ 为 $N$ 个 independent 随机变量 $h_1, \ldots, h_N$ 的平均，它们有共同的均值 $\bar{h}$ 与共同的方差 $\sigma_h^2$：$x \equiv \frac{1}{N} \sum_{n=1}^N h_n$。那么

```math
P\left( (x - \bar{h})^2 \ge \alpha \right) \le \sigma_h^2 / (N \alpha). \qquad (4.32)
```

[proof] *Proof（证明）：* 由证明 $\bar{x} = \bar{h}$ 以及 $\sigma_x^2 = \sigma_h^2/N$ 得到。$\square$

我们关心的是 $x$ 非常接近均值的情形（$\alpha$ 很小）。无论 $\sigma_h^2$ 有多大，无论要求的 $\alpha$ 有多小，也无论我们希望「$(x - \bar{h})^2 \ge \alpha$ 的概率」有多小，我们总可以通过取足够大的 $N$ 来达到它。

#### Proof of theorem 4.1（p.78）（定理 4.1 的证明）

我们把大数定律应用到随机变量 $\frac{1}{N} \log_2 \frac{1}{P(x)}$ 上，其中 $x$ 取自 ensemble $X^N$。这个随机变量可以写成 $N$ 个 information content $h_n = \log_2(1/P(x_n))$ 的平均，其中每一个都是均值为 $H = H(X)$、方差为 $\sigma^2 \equiv \operatorname{var}[\log_2(1/P(x_n))]$ 的随机变量。（每一项 $h_n$ 都是第 $n$ 个结果的 Shannon information content。）

我们再次用参数 $N$ 与 $\delta$ 定义 typical set：

```math
T_N = \left\{ x \in \mathcal{A}_X^N : \left| \frac{1}{N} \log_2 \frac{1}{P(x)} - H \right| < \delta \right\}. \qquad (4.33)
```

对所有 $x \in T_N$，$x$ 的概率满足

```math
2^{-N(H+\delta)} < P(x) < 2^{-N(H-\delta)}. \qquad (4.34)
```

而由大数定律，

```math
P(x \in T_N) \ge 1 - \frac{\sigma^2}{N \delta^2}. \qquad (4.35)
```

我们由此证明了「asymptotic equipartition」原理。随着 $N$ 增大，对任何 $\delta$，$x$ 落入 $T_N$ 的概率都趋近 1。这个结果与 source coding 有什么关系？

我们必须把 $T_N$ 与 $H_\delta(X^N)$ 联系起来。我们要证明：对任意给定的 $\epsilon$，存在足够大的 $N$，使得 $H_\delta(X^N) \simeq N H$。

**Part 1（第一部分）：** $\frac{1}{N} H_\delta(X^N) < H + \epsilon$。

集合 $T_N$ 并不是压缩的最佳子集。所以 $T_N$ 的大小给出 $H_\delta$ 的一个上界。我们通过计算 $T_N$ 最大可能有多大，来说明 $H_\delta(X^N)$ 必须多小。我们可以自由地把 $\delta$ 设成任何方便的值。$T_N$ 的成员所能具有的最小概率是 $2^{-N(H+\delta)}$，而 $T_N$ 包含的总概率不可能大于 1。所以

```math
|T_N|\, 2^{-N(H+\delta)} < 1, \qquad (4.36)
```

也就是说，typical set 的大小被界住：

```math
|T_N| < 2^{N(H+\delta)}. \qquad (4.37)
```

[Figure 4.13：定理两部分的示意图。给定任意 $\epsilon$ 与 $\delta$，我们证明：当 $N$ 足够大时，$\frac{1}{N} H_\delta(X^N)$ 落在 (1) 直线 $H + \epsilon$ 之下，(2) 直线 $H - \epsilon$ 之上。纵轴标出 $H+\epsilon$、$H$、$H-\epsilon$，横轴标 $\delta$ 从 0 到 1。]

如果我们取 $\delta = \epsilon$，并取 $N_0$ 使 $\frac{\sigma^2}{N_0 \delta^2} \le \delta$，那么 $P(T_N) \ge 1 - \delta$，于是集合 $T_N$ 就成了「$H_\delta(X^N) \le \log_2 |T_N| < N(H + \epsilon)$」这一事实的见证。


<span style="color:#7f8c8d">书内 p083 ｜ 4.6: Comments</span>

**Part 2（第二部分）：** $\frac{1}{N} H_\delta(X^N) > H - \epsilon$。

设想有人声称第二部分不成立——说对任意 $N$，最小的 $\delta$-sufficient subset $S_\delta$ 都比上述不等式所允许的更小。我们可以利用自己的 typical set 来表明他一定错了。记住我们可以自由地把 $\delta$ 设成自己选定的任何值。我们取 $\delta = \epsilon/2$，于是我们的任务是证明：一个满足 $|S_\delta| \le 2^{N(H-\epsilon/2)}$ 且达到 $P(x \in S_\delta) \ge 1 - \delta$ 的子集 $S_\delta$ 不可能存在（对大于某个待定的 $N_0$ 的 $N$ 而言）。

那么，让我们考虑落入这个更小的竞争子集 $S_\delta$ 的概率。该子集的概率是

```math
P(x \in S_\delta) = P(x \in S_\delta \cap T_N) + P(x \in S_\delta \cap \bar{T}_N), \qquad (4.38)
```

其中 $\bar{T}_N$ 表示补集 $\{x \notin T_N\}$。第一项的最大值出现在「$S_\delta \cap T_N$ 含有 $2^{N(H-\epsilon/2)}$ 个全取最大概率 $2^{-N(H-\delta)}$ 的结果」之时。第二项所能取的最大值是 $P(x \notin T_N)$。于是：

```math
P(x \in S_\delta) \le 2^{N(H-\epsilon/2)}\, 2^{-N(H-\delta)} + \frac{\sigma^2}{N\delta^2} = 2^{-N(\epsilon/2 - \delta)} + \frac{\sigma^2}{N\delta^2}. \qquad (4.39)
```

现在我们可以取 $\delta = \epsilon/2$，并取 $N_0$ 使 $P(x \in S_\delta) < 1 - \delta$，这就表明 $S_\delta$ 不可能满足 sufficient subset 的定义。因此任何大小为 $|S_\delta| \le 2^{N(H-\epsilon)}$ 的子集概率都小于 $1 - \delta$，于是按 $H_\delta$ 的定义，$H_\delta(X^N) > N(H - \epsilon)$。

因此对足够大的 $N$，函数 $\frac{1}{N} H_\delta(X^N)$ 在 $0 < \delta < 1$ 上基本上是 $\delta$ 的常函数，正如 图 4.9 与 图 4.13 所示。$\square$

### 4.6 Comments（评论）

source coding theorem（p.78）有两部分：$\frac{1}{N} H_\delta(X^N) < H + \epsilon$ 与 $\frac{1}{N} H_\delta(X^N) > H - \epsilon$。两个结果都很有意思。

第一部分告诉我们：即使 error probability $\delta$ 极小，为了以可忽略的错误概率指定一个长为 $N$ 个符号的串 $x$，每符号所需的 bit 数 $\frac{1}{N} H_\delta(X^N)$ 也不必超过 $H + \epsilon$ bit。我们只需对错误有极小的容忍度，所需 bit 数就从 $H_0(X)$ 显著降到 $(H + \epsilon)$。

如果我们对压缩错误更加宽容，会发生什么？第二部分告诉我们：即使 $\delta$ 非常接近 1，以至于大多数时候都会出错，指定 $x$ 所需的每符号平均 bit 数仍然必须至少是 $H - \epsilon$ bit。这两个极端告诉我们：无论我们对错误的具体容忍度是多少，指定 $x$ 所需的每符号 bit 数都是 $H$ bit；不多也不少。

#### Caveat regarding `asymptotic equipartition'（关于「asymptotic equipartition」的告诫）

我把「asymptotic equipartition」几个字加了引号，是因为重要的一点：不要以为 typical set $T_N$ 的元素真的彼此概率大致相同。它们的概率只在「$\log_2 \frac{1}{P(x)}$ 的值互相在 $2\delta N$ 之内」这个意义上相近。那么，随着 $\delta$ 减小，如果要保持对 typical set 质量的上界 $P(x \in T_N) \ge 1 - \frac{\sigma^2}{N\delta^2}$ 不变，$N$ 必须怎么增大？$N$ 必须按 $1/\delta^2$ 增长；所以，如果我们把 $\delta$ 写成 $c/\sqrt{N}$（$c$ 为某常数），那么


<span style="color:#7f8c8d">书内 p084 ｜ 4 -- The Source Coding Theorem</span>

typical set 中最可能的串，将比 typical set 中最不可能的串大约 $2^{c\sqrt{N}}$ 倍。随着 $\delta$ 减小，$N$ 增大，这个比值 $2^{c\sqrt{N}}$ 指数增长。所以我们只在弱意义上拥有「equipartition」！

#### Why did we introduce the typical set?（我们为什么要引入 typical set？）

块压缩的最佳子集（按定义）是 $S_\delta$，而不是某个 typical set。那么我们何苦引入 typical set？答案是：我们可以数 typical set。我们知道它的所有元素概率「几乎相同」（$2^{-NH}$），并且知道整个集合的概率几乎为 1，所以 typical set 必定大约有 $2^{NH}$ 个元素。没有 typical set 的帮助（它与 $S_\delta$ 非常相似），要数清 $S_\delta$ 里有多少元素是很困难的。

### 4.7 Exercises（习题）

#### Weighing problems（称重问题）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.9 [1]</span>

While some people, when they first encounter the weighing problem with 12 balls and the three-outcome balance (exercise 4.1 (p.66)), think that weighing six balls against six balls is a good first weighing, others say `no, weighing six against six conveys no information at all'. Explain to the second group why they are both right and wrong. Compute the information gained about which is the odd ball, and the information gained about which is the odd ball and whether it is heavy or light.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.10 [2]</span>

Solve the weighing problem for the case where there are 39 balls of which one is known to be odd.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.11 [2]</span>

You are given 16 balls, all of which are equal in weight except for one that is either heavier or lighter. You are also given a bizarre two-pan balance that can report only two outcomes: `the two sides balance' or `the two sides do not balance'. Design a strategy to determine which is the odd ball in as few uses of the balance as possible.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.12 [2]</span>

You have a two-pan balance; your job is to weigh out bags of flour with integer weights 1 to 40 pounds inclusive. How many weights do you need? [You are allowed to put weights on either pan. You're only allowed to put one flour bag on the balance at a time.]

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.13 [4, p.86]</span>

(a) Is it possible to solve exercise 4.1 (p.66) (the weighing problem with 12 balls and the three-outcome balance) using a sequence of three fixed weighings, such that the balls chosen for the second weighing do not depend on the outcome of the first, and the third weighing does not depend on the first or second?

(b) Find a solution to the general N-ball weighing problem in which exactly one of N balls is odd. Show that in W weighings, an odd ball can be identified from among N = (3^W - 3)/2 balls.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.14 [3]</span>

You are given 12 balls and the three-outcome balance of exercise 4.1; this time, two of the balls are odd; each odd ball may be heavy or light, and we don't know which. We want to identify the odd balls and in which direction they are odd.

(a) Estimate how many weighings are required by the optimal strategy. And what if there are three odd balls?

(b) How do your answers change if it is known that all the regular balls weigh 100 g, that light balls weigh 99 g, and heavy ones weigh 110 g?


<span style="color:#7f8c8d">书内 p085 ｜ 4.7: Exercises</span>

#### Source coding with a lossy compressor, with loss $\delta$（带损失 $\delta$ 的 lossy compressor 下的 source coding）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.15 [2, p.87]</span>

Let P_X = {0.2, 0.8}. Sketch (1/N)H_delta(X^N) as a function of delta for N = 1, 2 and 1000.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.16 [2]</span>

Let P_Y = {0.5, 0.5}. Sketch (1/N)H_delta(Y^N) as a function of delta for N = 1, 2, 3 and 100.

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.17 [2, p.87]</span>

(For physics students.) Discuss the relationship between the proof of the `asymptotic equipartition' principle and the equivalence (for large systems) of the Boltzmann entropy and the Gibbs entropy.

#### Distributions that don't obey the law of large numbers（不服从大数定律的分布）

我们在本章用到的 law of large numbers 表明：$N$ 个 i.i.d. 随机变量的均值，其 probability distribution 会随着 $N$ 增大而变窄，宽度按 $1/\sqrt{N}$ 缩小。然而我们只对离散随机变量证明了这个性质，也就是只对取有限个可能值的实数值证明了它。许多具有连续概率分布的随机变量也满足大数定律，但有一些重要的分布不满足。某些连续分布既没有 mean 也没有 variance。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.18 [3, p.88]</span>

Sketch the Cauchy distribution

```math
P(x) = \frac{1}{Z}\, \frac{1}{x^2 + 1}, \qquad x \in (-\infty, \infty). \qquad (4.40)
```

What is its normalizing constant Z? Can you evaluate its mean or variance?

Consider the sum z = x_1 + x_2, where x_1 and x_2 are independent random variables from a Cauchy distribution. What is P(z)? What is the probability distribution of the mean of x_1 and x_2, x_bar = (x_1 + x_2)/2? What is the probability distribution of the mean of N samples from this Cauchy distribution?

#### Other asymptotic properties（其他渐近性质）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.19 [3]</span>

Chernoff bound. We derived the weak law of large numbers from Chebyshev's inequality (4.30) by letting the random variable t in the inequality P(t >= alpha) <= t_bar/alpha be a function, t = (x - x_bar)^2, of the random variable x we were interested in.

Other useful inequalities can be obtained by using other functions. The Chernoff bound, which is useful for bounding the tails of a distribution, is obtained by letting t = exp(s x).

Show that

```math
P(x \ge a) \le e^{-s a} g(s), \quad \text{for any } s > 0 \qquad (4.41)
```

and

```math
P(x \le a) \le e^{-s a} g(s), \quad \text{for any } s < 0 \qquad (4.42)
```


<span style="color:#7f8c8d">书内 p086 ｜ 4 -- The Source Coding Theorem</span>

where g(s) is the moment-generating function of x,

```math
g(s) = \sum_x P(x)\, e^{s x}. \qquad (4.43)
```

#### Curious functions related to $p \log 1/p$（与 $p \log 1/p$ 有关的有趣函数）

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 4.20 [4, p.89]</span>

This exercise has no purpose at all; it's included for the enjoyment of those who like mathematical curiosities.

Sketch the function

```math
f(x) = x^{x^{x^{\cdots}}} \qquad (4.44)
```

for x >= 0. Hint: Work out the inverse function to f - that is, the function g(y) such that if x = g(y) then y = f(x) - it's closely related to p log 1/p.

### 4.8 Solutions（解答）

#### Solution to exercise 4.2（p.68）（exercise 4.2 的解答）

设 $P(x, y) = P(x)P(y)$。那么

```math
\begin{aligned}
H(X, Y) &= \sum_{xy} P(x)P(y) \log \frac{1}{P(x)P(y)} \qquad (4.45)\
&= \sum_{xy} P(x)P(y) \log \frac{1}{P(x)} + \sum_{xy} P(x)P(y) \log \frac{1}{P(y)} \qquad (4.46)\
&= \sum_x P(x) \log \frac{1}{P(x)} + \sum_y P(y) \log \frac{1}{P(y)} \qquad (4.47)\
&= H(X) + H(Y). \qquad (4.48)
\end{aligned}
```

#### Solution to exercise 4.4（p.73）

ASCII 文件的大小可以缩减为原来的 $7/8$。这个缩减可以通过块码实现：把 8 byte 的块映射成 7 byte 的块，做法是把 56 个携带信息的 bit 复制进 7 个 byte，并丢掉每个字符的最后一位。

#### Solution to exercise 4.5（p.74）

pigeon-hole principle（鸽笼原理）说的是：你不能把 16 只鸽子放进 15 个洞而不把某个洞用两次。

同理，你不能给 $\mathcal{A}_X$ 个结果指派长度 $l$ 短于 $\log_2 |\mathcal{A}_X|$ bit 的独特二进制名字，因为这样的二进制名字只有 $2^l$ 个，而 $l < \log_2 |\mathcal{A}_X|$ 蕴含 $2^l < |\mathcal{A}_X|$，所以压缩器至少有两个不同的输入会被压缩到同一个输出文件。

#### Solution to exercise 4.8（p.76）

在尖点之间，所有概率变化量都相等，而 $T_\delta$ 中元素个数在每一步改变 1。所以 $H_\delta$ 随 $(\delta - \delta_{\text{step}})$ 对数式变化。

#### Solution to exercise 4.13（p.84）

这个解由 Dyson 与 Lyness 在 1946 年找到，并由 John Conway 在 1999 年以下面这种优雅形式给出。请注意：符号 A、B、C 既用来给球命名，又用来给天平的盘命名，又用来给结果命名，还用来给 odd ball 的可能状态命名！

(a) 用下列序列给 12 个球编号：

```math
\text{AAB \quad ABA \quad ABB \quad ABC \quad BBC \quad BCA \quad BCB \quad BCC \quad CAA \quad CAB \quad CAC \quad CCA}
```

而在


<span style="color:#7f8c8d">书内 p087 ｜ 4.8: Solutions</span>

```math
\begin{aligned}
&\text{1st}\quad \text{AAB ABA ABB ABC} \;\big|\; \text{BBC BCA BCB BCC}\
&\text{2nd weighings put AAB CAA CAB CAC in pan A, ABA ABB ABC BBC in pan B.}\
&\text{3rd}\quad \text{ABA BCA CAA CCA} \;\big|\; \text{AAB ABB BCB CAB}
\end{aligned}
```

现在，在给定的一次称重中，一个盘最终会处于

- canonical position（C），即两边平衡时它所在的位置，或者

- 高于该位置（A），或者

- 低于该位置（B），

所以三次称重为每个盘确定了一个由这三个字母组成的三字母序列。

如果两个序列都是 CCC，那么就没有 odd ball。否则，恰好对一个盘而言，其序列在上述 12 个序列之中，这个序列就命名了 odd ball；而该球的重量是 Above 还是 Below 正常值，取决于该盘是 A 还是 B。

(b) 在 $W$ 次称重中，同样可以从

```math
N = (3^W - 3)/2 \qquad (4.49)
```

个球中找出 odd ball：用由 A、B、C 组成、第一个变化是 A 到 B、或 B 到 C、或 C 到 A 的全部非常量 $W$ 字母序列给球编号，并在第 $w$ 次称重时把那些第 $w$ 个字母为 A 的球放在盘 A，把那些第 $w$ 个字母为 B 的球放在盘 B。

#### Solution to exercise 4.15（p.85）

当 $N = 1, 2, 1000$ 时，$\frac{1}{N} H_\delta(X^N)$ 作为 $\delta$ 的函数的曲线画在图 4.14 中。注意 $H_2(0.2) = 0.72$ bit。

[Figure 4.14：纵轴为 $\frac{1}{N} H_\delta(X)$，横轴为 $\delta$，对象是 $N = 1, 2, 100$ 个概率 $p_1 = 0.4$ 的二值变量。图中标注的分段值：$N = 1$ 时 $\delta \in (0, 0.2]$ 给出 1，$\delta \in (0.2, 1]$ 给出 0；$N = 2$ 时 $\delta \in (0, 0.04]$ 给出 2，$\delta \in (0.04, 0.2]$ 给出 0.79，$\delta \in (0.2, 0.36]$ 给出 0.5，$\delta \in (0.36, 1]$ 给出 0。]

#### Solution to exercise 4.17（p.85）

Gibbs entropy 是 $k_B \sum_i p_i \ln \frac{1}{p_i}$，其中 $i$ 取遍系统的所有状态。这个 entropy 与 ensemble 的 Shannon entropy 等价（相差因子 $k_B$）。

Gibbs entropy 可以对任意 ensemble 定义，而 Boltzmann entropy 只对 microcanonical ensemble（微正则系综）定义，后者具有在一组可达状态上均匀的概率分布。Boltzmann entropy 定义为 $S_B = k_B \ln \Omega$，其中 $\Omega$ 是 microcanonical ensemble 的可达状态数。这与该受约束 ensemble 的 perfect information content $H_0$ 等价（相差因子 $k_B$）。microcanonical ensemble 的 Gibbs entropy 平凡地等于 Boltzmann entropy。


<span style="color:#7f8c8d">书内 p088 ｜ 4 -- The Source Coding Theorem</span>

现在考虑一个 thermal distribution（热分布，即 canonical ensemble，正则系综），其中状态 $x$ 的概率是

```math
P(x) = \frac{1}{Z} \exp\left( -\frac{E(x)}{k_B T} \right). \qquad (4.50)
```

借助这个 canonical ensemble，我们可以联系上一个相应的 microcanonical ensemble，即总能量被固定为该 canonical ensemble 平均能量（固定到某个精度 $\Delta$ 之内）的 ensemble。现在，把总能量固定到精度 $\Delta$，等价于把 $\ln 1/P(x)$ 的值固定到 $k_B T \Delta$ 之内。我们对 typical set $T_N$ 的定义恰恰是：它由所有那些 $\log P(x)$ 值非常接近 $\log P(x)$ 在 canonical ensemble 下均值 $-N H(X)$ 的元素构成。因此，microcanonical ensemble 等价于 canonical ensemble 的 typical set 上的均匀分布。

于是，我们对「asymptotic equipartition」原理的证明就（在系统能量可分离为若干 independent 项之和的情形下）证明了：如果把 microcanonical ensemble 的能量约束为等于 canonical ensemble 的平均能量，那么 microcanonical ensemble 的 Boltzmann entropy 非常接近（对大的 $N$ 而言）canonical ensemble 的 Gibbs entropy。

#### Solution to exercise 4.18（p.85）

Cauchy distribution 的归一化常数是

```math
Z = \int_{-\infty}^{\infty} \frac{dx}{x^2 + 1} = \Big[ \arctan x \Big]_{-\infty}^{\infty} = \frac{\pi}{2} + \frac{\pi}{2} = \pi, \qquad (4.51)
```

即 $P(x) = \frac{1}{\pi (x^2+1)}$。这个分布的 mean 与 variance 都是未定义的。（该分布关于零对称，但这并不意味着它的均值为零。均值是一个发散积分的值。）和 $z = x_1 + x_2$（其中 $x_1$ 与 $x_2$ 都服从 Cauchy distribution）的概率密度由 convolution（卷积）给出：

```math
P(z) = \frac{1}{\pi^2} \int_{-\infty}^{\infty} dx_1 \frac{1}{x_1^2 + 1} \cdot \frac{1}{(z - x_1)^2 + 1}, \qquad (4.52)
```

用标准方法经过一番不小的劳动后可得

```math
P(z) = \frac{1}{2\pi} \cdot \frac{4}{z^2 + 4} = \frac{2}{\pi (z^2 + 4)}, \qquad (4.53)
```

我们认出这是宽度参数为 2 的 Cauchy distribution（原分布的宽度参数为 1）。这意味着两点的均值 $\bar{x} = (x_1 + x_2)/2 = z/2$ 服从宽度参数为 1 的 Cauchy distribution。推广开来，从 Cauchy distribution 取 $N$ 个样本，其均值服从 Cauchy distribution，参数与单个样本相同。均值的 probability distribution 不会按 $1/\sqrt{N}$ 变窄。

central-limit theorem（中心极限定理）不适用于 Cauchy distribution，因为它没有有限的 variance。

另一种通往 (4.53) 式的巧妙方法，是利用 Cauchy distribution 的 Fourier transform，它是一个双指数 $e^{-|s|}$。实空间中的卷积对应 Fourier 空间中的乘法，所以 $z$ 的 Fourier transform 就是 $e^{-|2s|}$。做逆变换，我们得到 (4.53) 式。


<span style="color:#7f8c8d">书内 p089 ｜ 4.8: Solutions</span>

#### Solution to exercise 4.20（p.86）（exercise 4.20 的解答）

函数 $f(x)$ 有反函数

```math
g(y) = y^{1/y}. \qquad (4.54)
```

注意

```math
\log g(y) = \frac{1}{y} \log y. \qquad (4.55)
```

我通过以 $y$ 为纵轴、$g(y)$ 为横轴画 $g(y)$，得到了 $f(x)$ 的试探性图形。所得图形提示：$f(x)$ 在 $x \in (0, 1)$ 上单值，而且看上去出人意料地行为良好、相当平常；对 $x \in (1, e^{1/e})$，$f(x)$ 是双值的。$f(\sqrt{2})$ 同时等于 2 与 4。对 $x > e^{1/e}$（约 1.44），$f(x)$ 无穷大。不过也可以辩称，这种画 $f(x)$ 的方法只有部分有效——如果我们把 $f$ 定义为函数序列 $x, x^x, x^{x^x}, \ldots$ 的极限；由于在 $x = (1/e)^e$ 处出现 pitchfork bifurcation（叉式分岔），这个序列在 $0 < x \le (1/e)^e \simeq 0.07$ 上没有极限；而在 $x \in (1, e^{1/e})$ 上，序列的极限是单值的——即图中画出的两个值中较低的那个。

[Figure 4.15：$g(y) = y^{1/y}$ 的图形（上图），以及由它反推得到的 $f(x)$ 图形（下方两个小图）。纵轴范围约 0 到 50，横轴 0 到 1.4。]


<span style="color:#7f8c8d">书内 p090 ｜ 4.8: Solutions ／ 第 5 章开篇</span>

上一章我们看到了一条熵作为平均 information content 度量之基础地位的证明。我们定义了一个使用定长块码的 data compression 方案，并证明：随着 $N$ 增大，可以把 $N$ 个 i.i.d. 变量 $x = (x_1, \ldots, x_N)$ 编码成一个长为 $N(H(X) + \epsilon)$ bit 的块，且错误概率趋于零；而如果我们试图把 $X^N$ 编码成 $N(H(X) - \epsilon)$ bit，那么错误概率实际上就是 1。

我们由此验证了 data compression 的可能性，但证明中定义的块码并没有给出实用算法。本章与下一章我们研究实用的 data compression 算法。上一章的压缩方案使用大的定长块，并且是有损的；下一章我们讨论变长压缩方案，它们对小块尺寸实用，而且无损。

想象一只装满水的橡胶手套。如果我们挤压手套的两个指头，手套的其他某处就必然膨胀，因为水的总体积是常数。（水基本上不可压缩。）同理，如果方案无损，当我们缩短某些结果的 codeword（码字）时，必然有别的 codeword 变长。本章我们将找出「水的体积」在 information theory 中的对应物。

在读第 5 章之前，你应当已经做过 exercise 2.26（p.37）。我们将使用下列关于区间的记号：

- $x \in [1, 2)$ 表示 $x \ge 1$ 且 $x < 2$；
- $x \in (1, 2]$ 表示 $x > 1$ 且 $x \le 2$。

## 5 Symbol Codes（第 5 章 符号码）

本章讨论 variable-length symbol code（变长符号码），它一次编码一个 source symbol，而不是编码 $N$ 个 source symbol 组成的大串。这类码是 lossless（无损）的：与上一章的块码不同，它们保证压缩与解压都不出错；但码有时可能产生比原 source 串更长的编码串。

其思路是：把较短的编码指派给概率较大的结果、较长的编码指派给概率较小的结果，从而在平均意义上实现压缩。

关键问题是：

**symbol code 无损会带来什么后果？** 如果某些 codeword 被缩短，那么其他 codeword 必须加长多少？

**让压缩变得实用。** 我们如何保证一个 symbol code 容易 decoding（解码）？

**optimal symbol code。** 我们应当如何指派 codelength（码长）以取得最佳压缩，而最佳可达的压缩又是多少？

我们再次验证 Shannon information content 与 entropy 的基础地位，证明：

#### <span style="color:#c0392b">Source coding theorem（symbol codes）（symbol code 的信源编码定理）</span>

对 ensemble $X$，存在一种变长编码 $C$，使得一个被编码符号的平均长度 $L(C, X)$ 满足 $L(C, X) \in [H(X), H(X) + 1)$。平均长度等于 entropy $H(X)$ 当且仅当每个结果的 codelength 等于它的 Shannon information content。

我们还将定义一个构造性过程，即 Huffman coding algorithm（Huffman 编码算法），它产生 optimal symbol code。

#### Notation for alphabets（alphabet 的记号）

$\mathcal{A}^N$ 表示由集合 $\mathcal{A}$ 中元素组成的有序 $N$ 元组的集合，也就是所有长度为 $N$ 的串。符号 $\mathcal{A}^+$ 表示由集合 $\mathcal{A}$ 中元素组成的所有有限长度串的集合。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.1（例 5.1）</span>

$\{0, 1\}^3 = \{000, 001, 010, 011, 100, 101, 110, 111\}$。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.2（例 5.2）</span>

$\{0, 1\}^+ = \{0, 1, 00, 01, 10, 11, 000, 001, \ldots\}$。


<span style="color:#7f8c8d">书内 p091 ｜ 第 5 章章首页</span>

（书内 p091 为第 5 章章首页：整页只有章号「5」与标题「Symbol Codes」，没有其他正文段落，故本章标题已在上一块给出，此处只留页码锚点。）


<span style="color:#7f8c8d">书内 p092 ｜ 5 -- Symbol Codes</span>

### 5.1 Symbol codes（symbol code）

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：symbol code（符号码）</span>

<span style="color:#00838f">ensemble $X$ 的（二进制）symbol code $C$ 是从 $x$ 的取值范围 $\mathcal{A}_X = \{a_1, \ldots, a_I\}$ 到 $\{0, 1\}^+$ 的一个 mapping（映射）。$c(x)$ 记作与 $x$ 对应的 codeword，$l(x)$ 记作它的长度，$l_i = l(a_i)$。</span>

<span style="color:#00838f">extended code（扩展码）$C^+$ 是从 $\mathcal{A}_X^+$ 到 $\{0, 1\}^+$ 的一个 mapping，由相应的 codeword 不加标点地 concatenation（串接）得到：</span>

```math
c^+(x_1 x_2 \ldots x_N) = c(x_1)c(x_2)\ldots c(x_N). \qquad (5.1)
```

[这里「mapping」一词是「function」的同义词。]

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.3（例 5.3）</span>

设 ensemble $X$ 由

```math
\mathcal{A}_X = \{ a, b, c, d \}, \qquad P_X = \{ 1/2, 1/4, 1/8, 1/8 \}
```

定义，其 symbol code 为旁边列出的 $C_0$：

| $a_i$ | $c(a_i)$ | $l_i$ |
|---|---|---|
| a | 1000 | 4 |
| b | 0100 | 4 |
| c | 0010 | 4 |
| d | 0001 | 4 |

使用 extended code，我们可以把 $acdbac$ 编码为

```math
c^+(acdbac) = 100000100001010010000010.
```

一个有用的 symbol code 有三条基本要求。第一，任何编码串都必须有 unique decoding（唯一解码）。第二，symbol code 必须容易解码。第三，码应当取得尽可能多的压缩。

#### Any encoded string must have a unique decoding（任何编码串必须有唯一解码）

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：uniquely decodeable（唯一可译）</span>

<span style="color:#00838f">若在 extended code $C^+$ 下没有两个不同的串具有相同的编码，即</span>

```math
\forall x, y \in \mathcal{A}_X^+, \; x \ne y \Rightarrow c^+(x) \ne c^+(y), \qquad (5.4)
```

<span style="color:#00838f">则称码 $C(X)$ 是 uniquely decodeable 的。</span>

上面定义的码 $C_0$ 就是一个 uniquely decodeable 的码的例子。

#### The symbol code must be easy to decode（symbol code 必须容易解码）

如果一个 codeword 一到达就能立刻辨认出它的结束，那么这个 symbol code 是最容易解码的；这意味着任何 codeword 都不能是另一个 codeword 的 prefix（前缀）。[词 $c$ 是另一个词 $d$ 的 prefix，是指存在一个尾串 $t$，使串接 $ct$ 与 $d$ 相同。例如 1 是 101 的 prefix，10 也是。]

我们后面会证明，把 symbol code 限制为 prefix code 不会带来任何性能损失。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Definition（定义）：prefix code（前缀码）</span>

<span style="color:#00838f">若没有任何 codeword 是任何其他 codeword 的 prefix，则称该 symbol code 为 prefix code。</span>

<span style="color:#00838f">prefix code 也称为 instantaneous code（即时码）或 self-punctuating code（自定界码），因为编码串可以从左到右解码，不必向前窥视后续的 codeword。codeword 的结束可以立即辨认。prefix code 是 uniquely decodeable 的。</span>

> <span style="color:#7f8c8d">prefix code 也称为「prefix-free code」或「prefix condition code」。</span>

prefix code 对应于树，如下一页页边的插图所示。


<span style="color:#7f8c8d">书内 p093 ｜ 5.1: Symbol codes</span>

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.4（例 5.4）</span>

码 $C_1 = \{0, 101\}$ 是 prefix code，因为 0 不是 101 的 prefix，101 也不是 0 的 prefix。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.5（例 5.5）</span>

设 $C_2 = \{1, 101\}$。这个码不是 prefix code，因为 1 是 101 的 prefix。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.6（例 5.6）</span>

码 $C_3 = \{0, 10, 110, 111\}$ 是 prefix code。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.7（例 5.7）</span>

码 $C_4 = \{00, 01, 10, 11\}$ 是 prefix code。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.8 [1, p.104]</span>

Is C_2 uniquely decodeable?

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.9（例 5.9）</span>

考虑 exercise 4.1（p.66）与 figure 4.2（p.69）。任何能确定 odd ball 以及它是重是轻的称重策略，都可以看成给 24 个可能状态各指派一个 ternary code（三进制码）。这个码是 prefix code。

[页边插图：prefix code 的树形表示。$C_1$ 为 $0$ / $101$（不完备）；$C_3$ 为 $0$ / $10$ / $110$ / $111$；$C_4$ 为 $00$、$01$、$10$、$11$（完备）。]

> <span style="color:#7f8c8d">prefix code 可以在二叉树上表示。complete prefix code（完备前缀码）对应没有未使用分支的二叉树。$C_1$ 是不完备的码。</span>

#### The code should achieve as much compression as possible（码应当取得尽可能多的压缩）

ensemble $X$ 的 symbol code $C$ 的 expected length（期望长度）$L(C, X)$ 是

```math
L(C, X) = \sum_{x \in \mathcal{A}_X} P(x)\, l(x). \qquad (5.5)
```

我们也可以把这个量写成

```math
L(C, X) = \sum_{i=1}^{I} p_i l_i \qquad (5.6)
```

其中 $I = |\mathcal{A}_X|$。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.10（例 5.10）</span>

设

```math
\mathcal{A}_X = \{ a, b, c, d \}, \qquad P_X = \{ 1/2, 1/4, 1/8, 1/8 \}, \qquad (5.7)
```

并考虑码 $C_3$。$X$ 的 entropy 是 1.75 bit，而 $C_3$ 的 expected length $L(C_3, X)$ 也是 1.75 bit。符号序列 $x = (acdbac)$ 被编码为 $c^+(x) = 0110111100110$。$C_3$ 是 prefix code，因此是 uniquely decodeable 的。注意 codeword 长度满足 $l_i = \log_2(1/p_i)$，等价地 $p_i = 2^{-l_i}$。

| $a_i$ | $p_i$ | $h(p_i)$ | $l_i$ | $c(a_i)$ |
|---|---|---|---|---|
| a | 1/2 | 1.0 | 1 | 0 |
| b | 1/4 | 2.0 | 2 | 10 |
| c | 1/8 | 3.0 | 3 | 110 |
| d | 1/8 | 3.0 | 3 | 111 |

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.11（例 5.11）</span>

考虑同一个 ensemble $X$ 的定长码 $C_4$。expected length $L(C_4, X)$ 是 2 bit。

| $a_i$ | $c(a_i)$ | $a_i$ | $c(a_i)$ |
|---|---|---|---|
| a | 00 | a | 0 |
| b | 01 | b | 1 |
| c | 10 | c | 00 |
| d | 11 | d | 11 |

（上表左半为 $C_4$，右半为 $C_5$。）

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.12（例 5.12）</span>

考虑 $C_5$。expected length $L(C_5, X)$ 是 1.25 bit，小于 $H(X)$。但这个码不是 uniquely decodeable 的。序列 $x = (acdbac)$ 编码为 000111000，它也可以解码为 $(cabdca)$。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.13（例 5.13）</span>

考虑码 $C_6$。这个码的 expected length $L(C_6, X)$ 是 1.75 bit。符号序列 $x = (acdbac)$ 编码为 $c^+(x) = 0011111010011$。

$C_6$ 是 prefix code 吗？不是，因为 $c(a) = 0$ 同时是 $c(b)$ 与 $c(c)$ 的 prefix。

| $a_i$ | $c(a_i)$ | $p_i$ | $h(p_i)$ | $l_i$ |
|---|---|---|---|---|
| a | 0 | 1/2 | 1.0 | 1 |
| b | 01 | 1/4 | 2.0 | 2 |
| c | 011 | 1/8 | 3.0 | 3 |
| d | 111 | 1/8 | 3.0 | 3 |


<span style="color:#7f8c8d">书内 p094 ｜ 5 -- Symbol Codes</span>

$C_6$ 是 uniquely decodeable 的吗？这并不那么显然。如果你认为它可能不是 uniquely decodeable 的，就试着找一对串 $x$ 与 $y$ 具有相同编码，从而证明它不是。[uniquely decodeable 的定义见 (5.4) 式。]

$C_6$ 当然不易解码。当我们收到 `00` 时，$x$ 可能以 `aa`、`ab` 或 `ac` 开头。一旦收到 `001111`，第二个符号仍然有歧义，因为 $x$ 可能是 `abd. . .` 或 `acd. . .`。但最终，当编码流里出现下一个 0 时，唯一解码就成形了。

$C_6$ 事实上是 uniquely decodeable 的。与 prefix code $C_3$ 比较，我们看到 $C_6$ 的 codeword 是 $C_3$ 的倒序。$C_3$ 是 uniquely decodeable 的，这就证明了 $C_6$ 也是，因为来自 $C_6$ 的任何串都等同于一个来自 $C_3$ 的串倒过来读。

### 5.2 What limit is imposed by unique decodeability?（unique decodeability 施加了什么限制？）

现在我们问：给定一列正整数 $\{l_i\}$，是否存在一个以这些整数为 codeword 长度的 uniquely decodeable 码？在这个阶段，我们忽略不同符号的概率；一旦我们对 unique decodeability 理解得更好，我们再把概率引回来，讨论如何做出 optimal uniquely decodeable symbol code。

在上面那些例子里，我们已经观察到：如果我们取一个像 $\{00, 01, 10, 11\}$ 这样的码，并把其中一个 codeword 缩短，例如 $00 \to 0$，那么只有在把其他 codeword 加长的情况下，我们才能保持 unique decodeability。于是似乎存在一个受约束的预算（budget），我们可以把它花在 codeword 上，较短的 codeword 更贵。

让我们探索这个 budget 的性质。如果我们纯粹用长度为 $l = 3$ 的 codeword 构造一个码，最多能有多少个 codeword 同时保持 unique decodeability？答案是 $2^l = 8$ 个。一旦我们把这八个 codeword 全选完了，还有什么办法能给码再加上某个其他长度的 codeword 同时保持 unique decodeability 吗？看来没有。


<span style="color:#7f8c8d">书内 p095 ｜ 5.2: What limit is imposed by unique decodeability?</span>

如果我们做一个码，其中包含一个长度为一的 codeword「0」，其他 codeword 都是长度三，那会怎样？我们能有多少个长度为三的 codeword？如果只考虑 prefix code，那么我们只能有四个长度为三的 codeword，即 $\{100, 101, 110, 111\}$。其他码呢？还有别的选择长度 3 的 codeword 的办法能给出更多 codeword 吗？直觉上我们认为不太可能。一个长度为 3 的 codeword，其代价似乎是长度 1 的 codeword 的 $2^2 = 4$ 分之一。

我们定义一个总量为 1 的 budget，可以花在 codeword 上。如果我们把长度为 $l$ 的 codeword 的代价设为 $2^{-l}$，那么我们就有一个与上面讨论的例子相符的定价系统。长度为 3 的 codeword 每个花 1/8；长度为 1 的 codeword 每个花 1/2。我们可以把 budget 花在任何 codeword 上。如果我们超出 budget，那么这个码肯定不是 uniquely decodeable 的。反过来，如果

```math
\sum_i 2^{-l_i} \le 1, \qquad (5.8)
```

这个条件称为 Kraft inequality（Kraft 不等式），那么这个码就可能（虽然不必然）是 uniquely decodeable 的。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">The Kraft inequality（Kraft 不等式）</span>

<span style="color:#00838f">设 $C$ 是一个 uniquely decodeable 的码，其 codeword 长度为 $l_1, \ldots, l_I$。那么</span>

```math
\sum_i 2^{-l_i} \le 1. \qquad (5.9)
```

我们希望得到 uniquely decodeable 的码；prefix code 是 uniquely decodeable 的，而且容易解码。所以，如果我们能把注意力限制在 prefix code 上，日子会好过些。幸运的是，对任何 source 都存在一个同时是 prefix code 的 optimal symbol code。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Kraft inequality and prefix codes（Kraft 不等式与 prefix code）</span>

给定一组满足 Kraft 不等式的 codeword 长度，存在一个以这些长度为 codeword 长度的 uniquely decodeable prefix code。

Kraft 不等式也许更准确的叫法是 Kraft–McMillan inequality：Kraft 证明了若不等式成立，则存在具有给定长度的 prefix code。McMillan（1956）证明其逆命题：unique decodeability 蕴含该不等式成立。

<span style="color:#1e8449;">**[译注]**</span> **Kraft 不等式的力量全在"反向"那一半：给定长度表，它保证 prefix code 一定造得出来——这是整个第 5 章的可行域**

预算式 $\sum_i 2^{-l_i}\le 1$ 的经济学解释：长度 $l$ 的 codeword 占码空间 $2^{-l}$ 的份额，因为二叉树上一旦在某节点放码字，它的整棵子树（$2^{-l}$ 个叶位）全部被封死。正向（prefix code $\Rightarrow$ 不等式）只排除不可能的长度表；**反向（不等式 $\Rightarrow$ 存在 prefix code）才给出构造**：把长度按升序排，依次在「最左可用位置」放码字、封其子树，由于预算不超 1，永远不会走到树外。抽掉反向，Huffman 之后所有"最优码长是多少"的讨论都失去可行域——你只能说"这些长度不违反必要条件"，无法宣称"所以我能造出来"。

数字检验：长度表 $\{1,3,3,3,3\}$ 的预算 $=\frac12+4\cdot\frac18=1$，等号成立 $\Rightarrow$ 完备码，恰是 $\{0,100,101,110,111\}$；把其中一个 3 改成 2 得 $0.5+0.25+3\times0.125=1.125>1$，立刻不可实现。

挂载（真同构，不是术语对照）：Kraft 的"子树封死"就是 6.042J 的节点容量计数（深度 $l$ 的子树有 $2^{-l}$ 的叶位比例），与 Ch6 arithmetic coding 的**区间嵌套**是同一件事的二叉版与实数版：那里一个字串占 $[0,1)$ 里长度等于其概率的区间，这里一个码字占树上一个 $2^{-l}$ 的子树。

坐标：§5.2（原书 p.95，PDF p.107），式 (5.8)(5.9)；证明用 $\left(\sum 2^{-l_i}\right)^N$ 的计数论证（式 (5.10)），即把 $N$ 个码字并置后仍不能超过 $2^{N\max l}$ 个位置。

#### [proof] *Proof of the Kraft inequality（Kraft 不等式的证明）*

定义 $S = \sum_i 2^{-l_i}$。考虑量

```math
S_N = \left( \sum_i 2^{-l_i} \right)^N = \sum_{i_1=1}^{I} \sum_{i_2=1}^{I} \cdots \sum_{i_N=1}^{I} 2^{-(l_{i_1} + l_{i_2} + \cdots + l_{i_N})} . \qquad (5.10)
```

指数上的量 $(l_{i_1} + l_{i_2} + \cdots + l_{i_N})$ 就是串 $x = a_{i_1} a_{i_2} \ldots a_{i_N}$ 的编码长度。对每一个长度为 $N$ 的串 $x$，上面的和式中恰有一项。引入数组 $A_l$，它统计有多少个串 $x$ 的编码长度为 $l$。于是，定义 $l_{\min} = \min_i l_i$ 与 $l_{\max} = \max_i l_i$：

```math
S_N = \sum_{l = N l_{\min}}^{N l_{\max}} 2^{-l} A_l . \qquad (5.11)
```

现在假定 $C$ 是 uniquely decodeable 的，即对所有 $x \ne y$ 有 $c^+(x) \ne c^+(y)$。把注意力集中在编码长度为 $l$ 的那些 $x$ 上。长度为 $l$ 的二进制串总共有 $2^l$ 个，所以必然有 $A_l \le 2^l$。于是

```math
S_N = \sum_{l = N l_{\min}}^{N l_{\max}} 2^{-l} A_l \le \sum_{l = N l_{\min}}^{N l_{\max}} 1 = N l_{\max}. \qquad (5.12)
```

因此对所有 $N$ 都有 $S_N \le N l_{\max}$。现在，如果 $S$ 大于 1，那么随着 $N$ 增大，$S_N$ 会是一个指数增长函数，而对足够大的 $N$，指数函数总会超过像 $l_{\max} N$ 这样的多项式。但我们的结果（$S_N \le N l_{\max}$）对任何 $N$ 都成立。因此 $S \le 1$。$\square$

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.14 [3, p.104]</span>

Prove the result stated above, that for any set of codeword lengths {l_i} satisfying the Kraft inequality, there is a prefix code having those lengths.


<span style="color:#7f8c8d">书内 p096 ｜ 5 -- Symbol Codes</span>

[Figure 5.1：symbol coding budget（符号编码预算）。每个 codeword（长度为 $l$）的「代价」$2^{-l}$ 用它所写方框的大小表示。构造 uniquely decodeable 码时可用的总预算为 1。图中把 candidate codeword 按长度排列成货架：最长一行的方框标着 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111（各占 1/16 预算），上一行是 000, 001, 010, 011, 100, 101, 110, 111（各占 1/8），再上一行是 00, 01, 10, 11（各占 1/4），再上一行是 0, 1（各占 1/2）。你可以把这张图看作一个 codeword 超市：codeword 按长度排成过道，每个 codeword 的代价由它在货架上方框的大小表示。如果你取走的 codeword 代价之和超过预算，你的码就不是 uniquely decodeable 的。]

[Figure 5.2：5.1 节中 $C_0$、$C_3$、$C_4$、$C_6$ 各自选中的 codeword 集合。]

Kraft 不等式的一个图示视角可能有助于你解这道练习。想象我们正在挑选 codeword 以构造一个 symbol code。我们可以把所有候选 codeword 画在一个超市里，超市用方框面积显示 codeword 的「代价」（图 5.1）。可用的总预算——也就是 Kraft 不等式右端的那个「1」——画在一侧。5.1 节讨论过的某些码见图 5.2。注意那些 prefix code（$C_0$、$C_3$、$C_4$）具有这样的性质：在任何被选中的 codeword 的右侧，没有被选中的 codeword —— 因为 prefix code 对应树。注意 complete prefix code 对应没有未使用分支的完备树。

现在我们可以把符号的概率 $\{p_i\}$ 放回来了。给定一组符号概率（例如图 2.1 中的英语语言概率），我们如何做出最好的 symbol code，即 expected length $L(C, X)$ 尽可能小的那个？而那个最小可达的 expected length 又是多少？如何指派 codeword 长度并不显然。如果我们把短 codeword 给概率较大的符号，expected length 可能减小；另一方面，由 Kraft 不等式，缩短某些 codeword 必然导致其他 codeword 加长。


<span style="color:#7f8c8d">书内 p097 ｜ 5.3: What's the most compression that we can hope for?</span>

### 5.3 What's the most compression that we can hope for?（我们能期望的最大压缩是多少？）

我们希望最小化码的 expected length，

```math
L(C, X) = \sum_i p_i l_i . \qquad (5.13)
```

你可能已经猜到，entropy 作为码的 expected length 的下界出现。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Lower bound on expected length（expected length 的下界）</span>

uniquely decodeable 码的 expected length $L(C, X)$ 以 $H(X)$ 为下界。

#### [proof] *Proof（证明）*

我们定义 implicit probabilities（隐含概率）$q_i \equiv 2^{-l_i}/z$，其中 $z = \sum_i 2^{-l_i}$，于是 $l_i = \log \frac{1}{q_i} - \log z$。然后我们使用 Gibbs' inequality（Gibbs 不等式）$\sum_i p_i \log \frac{1}{q_i} \ge \sum_i p_i \log \frac{1}{p_i}$（等号成立当 $q_i = p_i$），以及 Kraft 不等式 $z \le 1$：

```math
\begin{aligned}
L(C, X) &= \sum_i p_i l_i = \sum_i p_i \log \frac{1}{q_i} - \log z \qquad (5.14)\
&\ge \sum_i p_i \log \frac{1}{p_i} - \log z \qquad (5.15)\
&\ge H(X). \qquad (5.16)
\end{aligned}
```

等式 $L(C, X) = H(X)$ 只有在 Kraft 等式 $z = 1$ 成立、并且 codelength 满足 $l_i = \log(1/p_i)$ 时才能达到。$\square$

这是一个重要的结果，所以我们再说一遍：

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Optimal source codelengths（最优的 source codelength）</span>

<span style="color:#00838f">expected length 只在 codelength 等于 Shannon information content 时才被最小化、并且等于 $H(X)$：</span>

```math
l_i = \log_2(1/p_i). \qquad (5.17)
```

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Implicit probabilities defined by codelengths（由 codelength 定义的隐含概率）</span>

<span style="color:#00838f">反过来，任何一组 codelength $\{l_i\}$ 都隐含地定义一个 probability distribution $\{q_i\}$，</span>

```math
q_i \equiv 2^{-l_i}/z, \qquad (5.18)
```

<span style="color:#00838f">对这些概率而言，那些 codelength 就是 optimal codelength。如果码是 complete 的，那么 $z = 1$，implicit probabilities 由 $q_i = 2^{-l_i}$ 给出。</span>


<span style="color:#7f8c8d">书内 p098 ｜ 5 -- Symbol Codes</span>

### 5.4 How much can we compress?（我们能压缩多少？）

所以，我们不能压缩到 entropy 之下。那么我们能期望多接近 entropy 呢？

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.1（定理 5.1）：Source coding theorem for symbol codes（symbol code 的信源编码定理）</span>

对 ensemble $X$，存在一个 prefix code $C$，其 expected length 满足

```math
H(X) \le L(C, X) < H(X) + 1. \qquad (5.19)
```

#### [proof] *Proof（证明）*

我们把这些 codelength 设成略大于最优长度的整数：

```math
l_i = \lceil \log_2(1/p_i) \rceil \qquad (5.20)
```

其中 $\lceil l \rceil$ 表示大于或等于 $l$ 的最小整数。[我们并不是断言 optimal code 必然使用这些长度，我们只是选择这些长度，因为它们可以用来证明定理。]

我们通过确认 Kraft 不等式成立，来检查存在具有这些长度的 prefix code。

```math
\sum_i 2^{-l_i} = \sum_i 2^{-\lceil \log_2(1/p_i) \rceil} \le \sum_i 2^{-\log_2(1/p_i)} = \sum_i p_i = 1. \qquad (5.21)
```

然后我们确认

```math
L(C, X) = \sum_i p_i \lceil \log(1/p_i) \rceil < \sum_i p_i \left( \log(1/p_i) + 1 \right) = H(X) + 1. \qquad (5.22)
```

$\square$

#### The cost of using the wrong codelengths（使用错误 codelength 的代价）

如果我们使用的码，其长度不等于 optimal codelength，那么平均消息长度会比 entropy 大。

如果真实概率是 $\{p_i\}$，而我们使用一个长度为 $l_i$ 的 complete code，那么可以把这些长度看作定义了 implicit probabilities $q_i = 2^{-l_i}$。从 (5.14) 式继续，平均长度是

```math
L(C, X) = H(X) + \sum_i p_i \log \frac{p_i}{q_i}, \qquad (5.23)
```

也就是说，它超出 entropy 的量正是 relative entropy $D_{KL}(p||q)$（定义见 p.34）。

[Figure 5.3：一个需要 symbol code 的 ensemble（英语单字母统计）。

| $x$ | $P(x)$ | $x$ | $P(x)$ | $x$ | $P(x)$ |
|---|---|---|---|---|---|
| a | 0.0575 | j | 0.0006 | s | 0.0567 |
| b | 0.0128 | k | 0.0084 | t | 0.0706 |
| c | 0.0263 | l | 0.0335 | u | 0.0334 |
| d | 0.0285 | m | 0.0235 | v | 0.0069 |
| e | 0.0913 | n | 0.0596 | w | 0.0119 |
| f | 0.0173 | o | 0.0689 | x | 0.0073 |
| g | 0.0133 | p | 0.0192 | y | 0.0164 |
| h | 0.0313 | q | 0.0008 | z | 0.0007 |
| i | 0.0599 | r | 0.0508 | 空格 | 0.1928 |]

### 5.5 Optimal source coding with symbol codes: Huffman coding（symbol code 的最优 source coding：Huffman coding）

给定一组概率 $P$，我们如何设计一个 optimal prefix code？例如，对图 5.3 所示的英语语言 ensemble，最好的 symbol code 是什么？当我们说「optimal」时，先假定我们的目标是最小化 expected length $L(C, X)$。

#### How not to do it（不要这样做）

人们可能试图把集合 $\mathcal{A}_X$ 大致分成两半，然后继续对子集二分，从而从根开始定义一个二叉树。这种构造的精神是对的，就像称重问题那样，但它不一定最优；它达到的是 $L(C, X) \le H(X) + 2$。

#### The Huffman coding algorithm（Huffman 编码算法）

现在我们给出一个漂亮而简单的算法，用来找 optimal prefix code。诀窍是反着构造码，从 codeword 的尾部开始；我们从叶节点开始构造这棵二叉树。

<span style="color:#1e8449;">**[译注]**</span> **Huffman 的最优性靠交换论证，不靠任何公式——抽掉它，你只剩 $L\le H+1$ 的 Shannon–Fano 上界**

算法本身（反复合并两个最小概率）只是一行代码；正确性在证明里：最优树中概率最小的两个符号**可以**被摆成最深的兄弟对（若不在，把它们与最深的一对交换，$L$ 不增——因为最深的码字最长，交换不会让短码字变长）。这一步成立后，合并后的问题与原问题的最优值满足同一递推，归纳即得。抽掉交换论证，"合并最小两者"就只是启发式：它仍会产出一个 prefix code，但你无法宣称它达到 $\min L$，也就无法把 §5.4 的界 $H\le L<H+1$ 收成一个**紧的**最优值陈述。

结构性代价必须记住：最优性只在 symbol code 类里成立。$H=0.01$ bit/符号的源，Huffman 仍要付 $\ge 1$ bit/符号（每个码字至少 1 bit），这不是算法差，是类的天花板——突破它必须上**块码或 arithmetic coding**（Ch6）。

挂载：6.006 里 greedy 正确性一律靠交换论证（区间调度、Huffman 本身是最标准的例子）；这个"证明套路在算法里通用"的连接比"贪心不一定最优"这种口号有用。

坐标：§5.5（原书 p.100–104，PDF p.112–116），Algorithm 5.4；下界 $L\ge H$ 在 §5.3 用 Gibbs 不等式给（原书 p.97–98），$L<H+1$ 在 §5.4（原书 p.99）。

> <span style="color:#7f8c8d">Algorithm 5.4（算法 5.4）：Huffman coding algorithm</span>

1. 取 alphabet 中概率最小的两个符号。这两个符号将得到最长的 codeword，且这两个 codeword 长度相等，只在最后一位上不同。

2. 把这两个符号合并成一个符号，并重复。

由于每一步都使 alphabet 的大小减一，所以在 $|\mathcal{A}_X| - 1$ 步之后，这个算法就给所有符号指派好了串。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.15（例 5.15）</span>

设 $\mathcal{A}_X = \{ a, b, c, d, e \}$，$P_X = \{ 0.25, 0.25, 0.2, 0.15, 0.15 \}$。

| $x$ | step 1 | step 2 | step 3 | step 4 |
|---|---|---|---|---|
| a | 0.25 | 0.25 | 0.25 | 0.55 $\to$ 1.0 |
| b | 0.25 | 0.25 | 0.45 | 0.45 |
| c | 0.2 | 0.2 | 0.3 | – |
| d | 0.15 | 0.3 | – | – |
| e | 0.15 | – | – | – |

codeword 则由把这些二进制数字倒序串接得到：$C = \{00, 10, 11, 010, 011\}$。Huffman 算法选出的 codelength（表 5.5 第 4 列）在某些情况下比理想 codelength（即 Shannon information content $\log_2 1/p_i$，第 3 列）更长，在另一些情况下更短。这个码的 expected length 是 $L = 2.30$ bit，而 entropy 是 $H = 2.2855$ bit。$\square$

| $a_i$ | $p_i$ | $h(p_i)$ | $l_i$ | $c(a_i)$ |
|---|---|---|---|---|
| a | 0.25 | 2.0 | 2 | 00 |
| b | 0.25 | 2.0 | 2 | 10 |
| c | 0.2 | 2.3 | 2 | 11 |
| d | 0.15 | 2.7 | 3 | 010 |
| e | 0.15 | 2.7 | 3 | 011 |

（上表为 Table 5.5：Huffman 算法产生的码。）

如果在某一步有不止一种方式选取概率最小的两个符号，那么可以任意选择——码的 expected length 不依赖于这个选择。

#### <span style="color:#2471a3;">**[exercise]**</span> <span style="color:#c0392b">Exercise 5.16 [3, p.105]</span>

Prove that there is no better symbol code for a source than the Huffman code.

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.17（例 5.17）</span>

我们可以对图 2.1 引入的 alphabet 上的 probability distribution 做一个 Huffman code。结果见图 5.6。这个码的 expected length 是 4.15 bit；该 ensemble 的 entropy 是 4.11 bit。注意所分配的 codelength 与理想 codelength $\log_2 1/p_i$ 之间的差异。

#### Constructing a binary tree top-down is suboptimal（自顶向下构造二叉树是次优的）

在前面几章我们研究过称重问题，其中我们构造 ternary 或 binary 树。我们注意到，balanced trees（平衡树）——在每一步、两个可能结果都尽可能接近 equiprobable 的树——似乎描述了最高效的实验。这为「entropy 是 information content 的度量」提供了直观动机。


<span style="color:#7f8c8d">书内 p099-p100 ｜ 5.5: Optimal source coding with symbol codes: Huffman coding</span>

[Figure 5.6：英语语言 ensemble（monogram statistics，单字母统计）的 Huffman code。表中列 $a_i$、$p_i$、$\log_2 1/p_i$、$l_i$、$c(a_i)$：

| $a_i$ | $p_i$ | $\log_2 1/p_i$ | $l_i$ | $c(a_i)$ |
|---|---|---|---|---|
| a | 0.0575 | 4.1 | 4 | 0000 |
| b | 0.0128 | 6.3 | 6 | 001000 |
| c | 0.0263 | 5.2 | 5 | 00101 |
| d | 0.0285 | 5.1 | 5 | 10000 |
| e | 0.0913 | 3.5 | 4 | 1100 |
| f | 0.0173 | 5.9 | 6 | 111000 |
| g | 0.0133 | 6.2 | 6 | 001001 |
| h | 0.0313 | 5.0 | 5 | 10001 |
| i | 0.0599 | 4.1 | 4 | 1001 |
| j | 0.0006 | 10.7 | 10 | 1101000000 |
| k | 0.0084 | 6.9 | 7 | 1010000 |
| l | 0.0335 | 4.9 | 5 | 11101 |
| m | 0.0235 | 5.4 | 6 | 110101 |
| n | 0.0596 | 4.1 | 4 | 0001 |
| o | 0.0689 | 3.9 | 4 | 1011 |
| p | 0.0192 | 5.7 | 6 | 111001 |
| q | 0.0008 | 10.3 | 9 | 110100001 |
| r | 0.0508 | 4.3 | 5 | 11011 |
| s | 0.0567 | 4.1 | 4 | 0011 |
| t | 0.0706 | 3.8 | 4 | 1111 |
| u | 0.0334 | 4.9 | 5 | 10101 |
| v | 0.0069 | 7.2 | 8 | 11010001 |
| w | 0.0119 | 6.4 | 7 | 1101001 |
| x | 0.0073 | 7.1 | 7 | 1010001 |
| y | 0.0164 | 5.9 | 6 | 101001 |
| z | 0.0007 | 10.4 | 10 | 1101000001 |
| 空格 | 0.1928 | 2.4 | 2 | 01 |]

然而，optimal code 并不总能通过贪心的自顶向下方法构造出来，即把 alphabet 接连划分成尽可能接近 equiprobable 的子集。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.18（例 5.18）</span>

求下面这个 ensemble 的 optimal binary symbol code：

```math
\mathcal{A}_X = \{ a, b, c, d, e, f, g \}, \qquad (5.24)
```

以及 $P_X = \{ 0.01, 0.24, 0.05, 0.20, 0.47, 0.01, 0.02 \}$。

注意贪心自顶向下方法可以把集合分成两个概率都是 $1/2$ 的子集 $\{a, b, c, d\}$ 与 $\{e, f, g\}$，而 $\{a, b, c, d\}$ 又可以分成概率为 $1/4$ 的子集 $\{a, b\}$ 与 $\{c, d\}$；所以贪心自顶向下方法给出的码是表 5.7 第三列所示，其 expected length 为 2.53。Huffman coding algorithm 给出的是第四列所示的码，其 expected length 为 1.97。$\square$

| $a_i$ | $p_i$ | Greedy（贪心） | Huffman |
|---|---|---|---|
| a | .01 | 000 | 000000 |
| b | .24 | 001 | 01 |
| c | .05 | 010 | 0001 |
| d | .20 | 011 | 001 |
| e | .47 | 10 | 1 |
| f | .01 | 110 | 000001 |
| g | .02 | 111 | 00001 |

（上表为 Table 5.7：贪心构造的码与 Huffman 码的对比。）

### 5.6 Disadvantages of the Huffman code（Huffman code 的缺点）

Huffman 算法为一个 ensemble 产生 optimal symbol code，但故事并未到此结束。「ensemble」一词与「symbol code」一语都需要仔细留意。

#### Changing ensemble（变化的 ensemble）

如果我们希望传达来自某个不变 ensemble 的一串结果，那么 Huffman code 可能很方便。但合适


<span style="color:#7f8c8d">书内 p101 ｜ 5 -- Symbol Codes</span>

的 ensemble 会变化。例如，如果我们压缩文本，那么符号频率会随上下文变化：在英语里，字母 u 跟在 q 之后的概率远高于跟在 e 之后（图 2.3）。而且，随着我们学到文本 source 的统计性质，我们对这些依赖上下文的符号频率的知识也会变化。

Huffman code 不能优雅地处理变化的 ensemble 概率。一种蛮力做法是：每当符号上的概率发生变化，就重算 Huffman code。另一种态度是放弃自适应的选项，转而事先把整个文件跑一遍，算出一个好的概率分布，然后在整个传输过程中固定使用它。在这种方案下，码本身也必须被传送。这样的技术不仅笨重且受限，而且次优，因为指定码的初始消息与文档本身有部分 redundancy。因此这种技术浪费 bit。

#### The extra bit（多出的那一个 bit）

Huffman code 的一个同样严重的问题，是那个看起来无害的、相对于理想平均长度 $H(X)$ 的「extra bit」——如定理 5.1 所证，Huffman code 达到的长度满足 $H(X) \le L(C, X) < H(X) + 1$。因此 Huffman code 每个符号产生 0 到 1 bit 的开销。如果 $H(X)$ 很大，那么这点开销只是不重要的分数级增加。但对许多应用而言，entropy 可能低到每符号一个 bit，甚至更小，于是开销 $L(C, X) - H(X)$ 可能主导编码后的文件长度。以英语文本为例：在某些上下文中，长的字符串可能高度可预测。例如在上下文 `strings_of_ch` 中，人们可能以每个 0.99 的概率预测接下来的九个符号是 `aracters_`。传统 Huffman code 被迫为每个字符至少用一个 bit，于是总代价是九 bit，而实际传达的信息几乎为零（准确地说，总共 0.13 bit）。给定好的模型时，英语的 entropy 约为每字符一个 bit（Shannon, 1948），所以 Huffman code 很可能效率很低。

对 Huffman code 的传统补救办法是用它们压缩符号块，例如我们在第 4 章讨论过的「extended sources」$X^N$。每个块的开销至多 1 bit，所以每符号开销至多 $1/N$ bit。对足够大的块，extra bit 问题可以消除——但代价是：(a) 失去简单 Huffman coding 优雅的 instantaneous decodeability；(b) 必须计算所有相关串的概率并构造相应的 Huffman 树。人们最终会显式地计算数量巨大的串的概率与码，而其中大多数串根本不会出现。（见 exercise 5.29（p.103）。）

#### Beyond symbol codes（超越 symbol code）

于是，Huffman code 虽然被广泛吹捧为「optimal」，在实践中却有许多缺陷。它们是 optimal symbol code，但就实用目的而言，我们并不想要一个 symbol code。

Huffman code 的这些缺陷由 arithmetic coding（算术编码）弥补，后者摆脱了「每个符号必须译成整数个 bit」这一限制。Arithmetic coding 是下一章的主题。
