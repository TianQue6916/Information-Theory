# <span style="color:#c0392b;">MacKay《Information Theory, Inference, and Learning Algorithms》第 2 章 概率、熵与推断</span>

> <span style="color:#7f8c8d;">Source: 教材/book.pdf · Chapter 2, 书页 pp.22–40 (PDF p.34–52) · 行内双语翻译版 · 译者：ZCode（bilingual-translator 铁律）· 含正文与习题题面；习题解答见随书页码（部分解答待续译）</span>

本章我们讨论 probability（概率）的两种用途，介绍 probability theory（概率论）的规则，定义 entropy（熵）与相关函数，并介绍 convex functions（凸函数）与 Jensen's inequality（Jensen 不等式）。

## <span style="color:#c0392b;">2.1 概率与系综（Probabilities and ensembles）</span>

ensemble（系综）$\mathcal{A}_X$ 的 outcomes（结果）为 $x$，取值于

$$
\mathcal{A}_X=\{a_1,a_2,\dots,a_I\},
$$

具有 probability distribution（概率分布）$\{p_1,p_2,\dots,p_I\}$，其中 $p_i=P(x=a_i)$ 且 $p_i\ge0$、$\sum_{\mathcal{A}_X}P(x)=1$。

图 2.1 用白色方块的面积展示了英语文档中随机选取字母的 27 个结果的概率分布（由《The Frequently Asked Questions Manual for Linux》估计）。

> <span style="color:#2471a3;">**[译者注｜记号]** 缩写：有时使用更简的记号，例如 $P(x=a_i)$ 可写作 $P(a_i)$ 或 $P(x)$。子集的概率：若 $T$ 是 $\mathcal{A}_X$ 的子集，则

$$
P(T)=P(x\in T)=\sum_{a_i\in T}P(x=a_i). \tag{2.1}
$$

例如若定义 $V$ 为图 2.1 中的元音字母 $V=\{a,e,i,o,u\}$，则

$$
P(V)=0.06+0.09+0.06+0.07+0.03=0.31. \tag{2.2}
$$

</span>

joint ensemble（联合系综）$XY$ 是每个结果为有序对 $x,y$（$x\in\mathcal{A}_X=\{a_1,\dots,a_I\}$，$y\in\mathcal{A}_Y=\{b_1,\dots,b_J\}$）的系综。我们称 $P(x,y)$ 为 $x$ 与 $y$ 的 joint probability（联合概率）。写有序对时逗号可省略：$xy \Leftrightarrow x,y$。

> <span style="color:#2471a3;">**[译者注｜注意]** 在联合系综 $XY$ 中，两个变量未必 independent（独立）。

**边缘概率（Marginal probability）。** 可以由联合概率 $P(x,y)$ 通过求和得到边缘概率 $P(x)$：

$$
P(x=a_i)\equiv\sum_{y\in\mathcal{A}_Y}P(x=a_i,\ y). \tag{2.3}
$$

类似地，用更简的记号，$y$ 的边缘概率为

$$
P(y)\equiv\sum_{x\in\mathcal{A}_X}P(x,y). \tag{2.4}
$$

**条件概率（Conditional probability）。**

$$
P(x=a_i \mid y=b_j)\equiv\frac{P(x=a_i,\ y=b_j)}{P(y=b_j)}\qquad \text{（若 } P(y=b_j)\neq0\text{）}. \tag{2.5}
$$

[若 $P(y=b_j)=0$，则 $P(x=a_i\mid y=b_j)$ 无定义。]我们读 $P(x=a_i\mid y=b_j)$ 为「在 $y$ 等于 $b_j$ 的条件下，$x$ 等于 $a_i$ 的概率」。

</span>

<span style="color:#00838f;">**[例 2.1]** 联合系综的一个例子是英语文档中两个相继字母构成的有序对 $XY$。可能结果是有序对如 $aa,ab,ac,\dots,zz$；其中 $ab$ 与 $ac$ 似乎比 $aa$ 与 $zz$ 更可能。图 2.2 图示了相邻字符对联合概率分布的估计。这个联合系综有特殊性质：两个边缘分布 $P(x)$ 与 $P(y)$ 相同，都等于图 2.1 的 monogram distribution（单字母分布）。

<!-- p.35/36 -->

从这个联合分布 $P(x,y)$ 可以通过分别归一化行与列得到条件分布 $P(y\mid x)$ 与 $P(x\mid y)$（图 2.3）。概率 $P(y\mid x=q)$ 是「给定第一个字母是 $q$」时第二个字母的概率分布。如图 2.3a，给定首字母 $x=q$，第二字母 $y$ 最可能的两个值是 $u$ 与 $-$（空格）。（$q$ 后空格常见，因为源文档大量使用单词 FAQ。）概率 $P(x\mid y=u)$ 是「给定第二个字母是 $u$」时第一个字母 $x$ 的概率分布。如图 2.3b，给定 $y=u$，$x$ 最可能的两个值是 $n$ 与 $o$。

比起直接写下联合概率，我们常用一组条件概率来定义系综。以下概率论规则将很有用。（$H$ 表示概率所基于的假设。）

**乘积规则（Product rule）**——由条件概率的定义得到：

$$
P(x,y\mid H)=P(x\mid y,H)P(y\mid H)=P(y\mid x,H)P(x\mid H). \tag{2.6}
$$

此规则也称 chain rule（链式法则）。

**求和规则（Sum rule）**——边缘概率定义的改写：

$$
\begin{aligned}
P(x\mid H)&=\sum_yP(x,y\mid H) \tag{2.7}\\
&=\sum_yP(x\mid y,H)P(y\mid H). \tag{2.8}
\end{aligned}
$$

**贝叶斯定理（Bayes' theorem）**——由乘积规则得到：

$$
P(y\mid x,H)=\frac{P(x\mid y,H)P(y\mid H)}{P(x\mid H)} \tag{2.9}
$$

$$
=\frac{P(x\mid y,H)P(y\mid H)}{\sum_{y'}P(x\mid y',H)P(y'\mid H)}. \tag{2.10}
$$

**独立性（Independence）。** 两个随机变量 $X,Y$ independent（独立）（有时写作 $X\perp Y$）当且仅当

$$
P(x,y)=P(x)P(y). \tag{2.11}
$$

<span style="color:#00838f;">**[习题 2.2]** [1, p.40] 图 2.2 的联合系综中随机变量 $X$ 与 $Y$ 独立吗？

<!-- p.37 -->

我说过我们常用一组条件概率定义系综。下面的例子说明这一想法。

<span style="color:#00838f;">**[例 2.3]** Jo 做了一种恶性疾病的检测。用变量 $a$ 表示 Jo 的健康状况、$b$ 表示检测结果：

$$
\begin{aligned}
a=1&\quad \text{Jo 有病}\\
a=0&\quad \text{Jo 无病}. \tag{2.12}
\end{aligned}
$$

检测结果为「阳性」（$b=1$）或「阴性」（$b=0$）；检测 95% 可靠：真正有病的人 95% 的情形返回阳性，无病的人 95% 的情形得到阴性。最后一条背景信息：Jo 这个年龄与背景的人群 1% 有病。

好——Jo 检测了，结果是阳性。Jo 有病的概率是多少？

**解。** 写下所有给定的概率。检测的可靠性给出给定 $a$ 时 $b$ 的条件概率：

$$
\begin{aligned}
P(b=1\mid a=1)&=0.95 & P(b=1\mid a=0)&=0.05\\
P(b=0\mid a=1)&=0.05 & P(b=0\mid a=0)&=0.95;
\end{aligned} \tag{2.13}
$$

疾病的流行率告诉我们 $a$ 的边缘概率：

$$
P(a=1)=0.01,\qquad P(a=0)=0.99. \tag{2.14}
$$

由边缘 $P(a)$ 与条件概率 $P(b\mid a)$ 可推出联合概率 $P(a,b)=P(a)P(b\mid a)$ 以及我们感兴趣的任何其他概率。例如由求和规则，$b=1$ 的边缘概率——得到阳性结果的概率——是

$$
P(b=1)=P(b=1\mid a=1)P(a=1)+P(b=1\mid a=0)P(a=0). \tag{2.15}
$$

<!-- p.37/38 -->

Jo 收到了阳性结果 $b=1$，想知道她有病（即 $a=1$）有多 plausible（可信）。街上的路人可能被「检测 95% 可靠，所以 Jo 的阳性结果意味着 Jo 有 95% 的概率有病」这句话骗到，但这是不对的。推断问题的正确解法要用 Bayes' theorem（贝叶斯定理）：

$$
P(a=1\mid b=1)=\frac{P(b=1\mid a=1)P(a=1)}{P(b=1\mid a=1)P(a=1)+P(b=1\mid a=0)P(a=0)} \tag{2.16}
$$

$$
=\frac{0.95\times0.01}{0.95\times0.01+0.05\times0.99} \tag{2.17}
$$

$$
=0.16. \tag{2.18}
$$

所以尽管结果阳性，Jo 有病的概率只有 16%。

## <span style="color:#c0392b;">2.2 概率的含义（The meaning of probability）</span>

概率有两种用法。

概率可以描述随机实验结果的 frequency（频率）——但给「频率」与「随机」非循环的定义是个挑战：说「抛硬币正面朝上的频率是 1/2」是什么意思？若说这个频率是长序列中正面的平均比例，就得定义「平均」；而不借助与概率同义的词很难定义「平均」。我不打算去解这个哲学死结。

<!-- p.37/38 -->

概率也可以更一般地用来描述对不涉及随机变量的 proposition（命题）的 degrees of belief（信念程度）——例如「给定证据，S 先生是 S 夫人凶手的概率」（他要么是要么不是，评估他有多可能是陪审团的工作）；「托马斯·杰斐逊有一个奴隶孩子的概率」；「莎士比亚戏剧由弗朗西斯·培根所写的概率」；或者举一个现代的例子：「某支票上的某个签名是真实的概率」。

街上的路人乐于用这两种方式使用概率，但一些概率书把概率限制为只指可重复随机实验结果的频率。

<!-- p.38 -->

尽管如此，若信念满足简单的相容性规则——即 Cox axioms（Cox 公理，Cox 1946）（框 2.4）——就可以把信念程度映射到概率上。于是概率可以用来描述 assumptions（假设），并描述在这些假设下的 inferences（推断）。概率规则保证：若两个人做相同的假设、收到相同的数据，就会得出相同的结论。这种用概率量化信念的更一般用法称为 Bayesian viewpoint（贝叶斯观点），也称概率的 subjective interpretation（主观解释），因为概率依赖假设。贝叶斯数据建模与 pattern recognition（模式识别）方法的倡导者并不把这种主观性视为缺陷，因为在他们看来：

> 不做假设就无法做推断。

本书会不时地把「贝叶斯方法说得通」当作理所当然，但提醒读者这还不是全球共识——20 世纪大部分时间统计学界由 non-Bayesian methods（非贝叶斯方法）主导，那里只允许概率描述随机变量。两种方法的大差别是：贝叶斯学派也用概率描述推断。

> <span style="color:#00838f;">**[框 2.4]** **Cox 公理。** 若一组信念满足这些公理，则它们可以映射到满足 $P(\mathrm{false})=0$、$P(\mathrm{true})=1$、$0\le P(x)\le1$ 及概率规则的概率：$P(x)=1-P(x)$ 与 $P(x,y)=P(x\mid y)P(y)$。
> **记号**：设「命题 $x$ 的信念程度」记为 $B(x)$；$x$ 的 negation（否定，非 $x$）写作 $\bar{x}$；「假设命题 $y$ 为真时 $x$ 的条件命题」的信念程度记为 $B(x\mid y)$。
> **公理 1**：信念程度可以排序；若 $B(x)$「大于」$B(y)$ 且 $B(y)$「大于」$B(z)$，则 $B(x)$「大于」$B(z)$。[推论：信念可以映射到实数。]
> **公理 2**：命题 $x$ 与其否定 $\bar{x}$ 的信念程度相关：存在函数 $f$ 使 $B(\bar{x})=f[B(x)]$。
> **公理 3**：命题合取 $x,y$（$x$ 且 $y$）的信念程度与条件命题 $x\mid y$ 及命题 $y$ 的信念程度相关：存在函数 $g$ 使 $B(x,y)=g[B(x\mid y),B(y)]$。</span>

<!-- p.39 -->

## <span style="color:#c0392b;">2.3 正向概率与逆向概率（Forward probabilities and inverse probabilities）</span>

概率计算常落入两类：forward probability（正向概率）与 inverse probability（逆向概率）。下面是一个正向概率问题：

<span style="color:#00838f;">**[习题 2.4]** [2, p.40] 一个 urn（瓮）中有 $K$ 个球，$B$ 个黑球、$W=K-B$ 个白球。Fred 从瓮中随机摸球并放回，共 $N$ 次。
(a) 摸到黑球次数 $n_B$ 的概率分布是什么？
(b) $n_B$ 的 expectation（期望）是多少？方差是多少？标准差是多少？对 $N=5$ 与 $N=400$（$B=2$、$K=10$）给出数值答案。

正向概率问题涉及一个 generative model（生成模型），它描述假定产生某些数据的过程；任务是计算依赖数据的某个量的概率分布或期望。另一个正向概率问题：

<span style="color:#00838f;">**[习题 2.5]** [2, p.40] 一个瓮中有 $K$ 个球，$B$ 个黑球、$W=K-B$ 个白球。定义比例 $f_B\equiv B/K$。Fred 按习题 2.4 的方式摸 $N$ 次，得 $n_B$ 个黑球，并计算量

$$
z=\frac{(n_B-f_BN)^2}{Nf_B(1-f_B)}. \tag{2.19}
$$

$z$ 的期望是多少？$N=5$、$f_B=1/5$ 时 $z$ 的概率分布是什么？$z<1$ 的概率是多少？[提示：把 $z$ 与上一习题计算的量比较。]

<!-- p.39/40 -->

与正向概率问题一样，逆向概率问题也涉及过程的生成模型，但不是计算过程产生的某个量的概率分布，而是计算：给定已观察到的变量，过程中一个或多个未观察变量的 conditional probability（条件概率）。这总是需要使用 Bayes' theorem（贝叶斯定理）。

<span style="color:#00838f;">**[例 2.6]** 有十一个瓮，标号 $u\in\{0,1,2,\dots,10\}$，各含十个球。瓮 $u$ 含 $u$ 个黑球与 $10-u$ 个白球。Fred 随机选一个瓮 $u$，从该瓮中有放回地摸 $N$ 次，得 $n_B$ 个黑球与 $N-n_B$ 个白球。Fred 的朋友 Bill 在旁观。若 $N=10$ 次摸球后 $n_B=3$ 个黑球，从 Bill 的观点看，Fred 所用的瓮是瓮 $u$ 的概率是多少？（Bill 不知道 $u$ 的值。）

**解。** 随机变量 $u$ 与 $n_B$ 的联合概率分布可写为

$$
P(u,n_B\mid N)=P(n_B\mid u,N)P(u). \tag{2.20}
$$

由 $u$ 与 $n_B$ 的联合概率，可得给定 $n_B$ 时 $u$ 的条件分布：

$$
P(u\mid n_B,N)=\frac{P(u,n_B\mid N)}{P(n_B\mid N)} \tag{2.21}
$$

$$
=\frac{P(n_B\mid u,N)P(u)}{P(n_B\mid N)}. \tag{2.22}
$$

<!-- p.40 -->

图 2.5 展示 $N=10$ 次摸球后 Bill 与 Fred 瓮问题的 $u$ 与 $n_B$ 联合概率。$u$ 的边缘概率 $P(u)=\frac{1}{11}$（对所有 $u$）。给定 $u$ 与 $N$ 时 $n_B$ 的概率 $P(n_B\mid u,N)$ 你在解习题 2.4（p.27）时已写出。[你在做那些强烈推荐的习题，对吧？]若定义 $f_u\equiv u/10$，则

$$
P(n_B\mid u,N)=\binom{N}{n_B}f_u^{\,n_B}(1-f_u)^{N-n_B}. \tag{2.23}
$$

那分母 $P(n_B\mid N)$ 呢？这是 $n_B$ 的边缘概率，可用求和规则得到：

$$
P(n_B\mid N)=\sum_uP(u,n_B\mid N)=\sum_uP(u)P(n_B\mid u,N). \tag{2.24}
$$

所以给定 $n_B$ 时 $u$ 的条件概率为

$$
P(u\mid n_B,N)=\frac{P(u)P(n_B\mid u,N)}{P(n_B\mid N)} \tag{2.25}
$$

$$
=\frac{1}{P(n_B\mid N)}\cdot\frac{1}{11}\binom{N}{n_B}f_u^{\,n_B}(1-f_u)^{N-n_B}. \tag{2.26}
$$

<!-- p.41 -->

这个条件分布可以通过归一化图 2.5 的第 3 列得到，见图 2.6。归一化常数——$n_B$ 的边缘概率——是 $P(n_B=3\mid N=10)=0.083$。后验概率 (2.26) 对所有 $u$ 正确，包括端点 $u=0$ 与 $u=10$（那里 $f_u=0$ 与 $f_u=1$）。给定 $n_B=3$ 时 $u=0$ 的后验概率为零：因为若 Fred 从瓮 0 摸球，不可能摸到任何黑球。$u=10$ 的后验概率也为零：那个瓮没有白球。其他假设 $u=1,\dots,u=9$ 的后验概率都非零。

**逆向概率的术语。** 在逆向概率问题中，给贝叶斯定理中出现的概率起名字很方便。在方程 (2.25) 中，我们把边缘概率 $P(u)$ 称为 $u$ 的 prior probability（先验概率），$P(n_B\mid u,N)$ 称为 $u$ 的 likelihood（似然）。重要：术语 likelihood（似然）与 probability（概率）不是同义词。量 $P(n_B\mid u,N)$ 同时是 $n_B$ 与 $u$ 的函数：固定 $u$，$P(n_B\mid u,N)$ 定义 $n_B$ 上的一个概率；固定 $n_B$，$P(n_B\mid u,N)$ 定义 $u$ 的似然。

> <span style="color:#2471a3;">**[译者注｜边框警告]** 永远不要说「the likelihood of the data（数据的似然）」。永远要说「the likelihood of the parameters（参数的似然）」。似然函数不是概率分布。（若想提及似然函数关联的数据，可以说「给定数据时参数的似然」。）

条件概率 $P(u\mid n_B,N)$ 称为给定 $n_B$ 时 $u$ 的 posterior probability（后验概率）。归一化常数 $P(n_B\mid N)$ 不依赖 $u$，若只想评估各候选假设 $u$ 的相对概率，它的值不重要。但在任何有一定复杂度的数据建模问题中，这个量变得重要，它有各种名字：$P(n_B\mid N)$ 称为 evidence（证据）或 marginal likelihood（边缘似然）。若 $\theta$ 表示未知参数、$D$ 表示数据、$H$ 表示整个假设空间，一般方程

$$
P(\theta\mid D,H)=\frac{P(D\mid\theta,H)P(\theta\mid H)}{P(D\mid H)} \tag{2.27}
$$

写作：

$$
\text{posterior 后验}=\frac{\text{likelihood 似然}\times\text{prior 先验}}{\text{evidence 证据}}. \tag{2.28}
$$

**逆向概率与预测。** 例 2.6（续）。再假设 Bill 已观察到 $N=10$ 次摸球中 $n_B=3$ 个黑球，让 Fred 从同一瓮再摸一个球。下一个球是黑球的概率是多少？[应利用图 2.6 的后验概率。]

**解。** 由求和规则，

$$
P(\mathrm{ball}_{N+1}\text{ is black}\mid n_B,N)=\sum_uP(\mathrm{ball}_{N+1}\text{ is black}\mid u,n_B,N)P(u\mid n_B,N). \tag{2.29}
$$

<!-- p.41/42 -->

由于球是从所选瓮中有放回地摸的，$P(\mathrm{ball}_{N+1}\text{ is black}\mid u,n_B,N)$ 就是 $f_u=u/10$，无论 $n_B$ 与 $N$ 是什么。所以

$$
P(\mathrm{ball}_{N+1}\text{ is black}\mid n_B,N)=\sum_uf_uP(u\mid n_B,N). \tag{2.30}
$$

用图 2.6 给出的 $P(u\mid n_B,N)$ 值，得

$$
P(\mathrm{ball}_{N+1}\text{ is black}\mid n_B=3,N=10)=0.333. \tag{2.31}
$$

<!-- p.42 -->

**评注。** 注意用概率论得到的这个预测与统计学中流行的做法的差别：先选出最可信的假设（这里是瓮 $u=3$）、再假设该假设为真做预测（那会给出下一球为黑的概率 0.3）。正确的预测是把不确定性纳入考虑——对假设 $u$ 的可能值 marginalizing（边缘化）。边缘化在这里产生略微更 moderate（温和）、不那么极端的预测。

**作为逆向概率的推断（Inference as inverse probability）。** 现在考虑下面这道习题，它具有简单科学考察的性质。

<span style="color:#00838f;">**[例 2.7]** Bill 抛一枚 bent coin（不对称硬币）$N$ 次，得到正面与反面的序列。设硬币正面朝上的概率为 $f_H$；我们不知道 $f_H$。若 $N$ 次抛掷中出现 $n_H$ 次正面，$f_H$ 的概率分布是什么？（例如 $N$ 可能是 10、$n_H$ 可能是 3；或抛了很多次后，$N=300$、$n_H=29$。）给定 $N$ 次抛掷 $n_H$ 次正面，第 $N+1$ 次结果为正面的概率是多少？

与例 2.6（p.27）不同，这个问题有 subjective（主观）成分。给定「概率是随机变量的频率」这一受限定义，本例与十一瓮问题不同：瓮 $u$ 是随机变量，而硬币的 bias（偏倚）$f_H$ 通常不叫随机变量——它只是一个我们感兴趣的固定但未知的 parameter（参数）。但例 2.6 与 2.7 难道不是本质相似吗？[尤其当 $N=10$、$n_H=3$ 时！]

> <span style="color:#2471a3;">**[译者注]** 原书边注：这里 $P(f)$ 表示 probability density（概率密度），而非概率分布。

要解例 2.7，必须对硬币偏倚 $f_H$ 可能是什么做假设。$f_H$ 上的这个先验概率分布 $P(f_H)$ 对应十一瓮问题中对 $u$ 的先验。那个例子里，贴心的题面规定了 $P(u)$。现实中，我们必须做假设才能指定先验；这些假设是主观的，我们的答案将依赖它们。生成模型中的其他概率也一样：例如我们假设球是从瓮中独立摸出的；但 Fred 摸球的动作并非完全随机时，序列中会不会有 correlations（相关性）？确实可能有，所以我们用的似然函数也依赖假设。真实数据建模问题中，先验是主观的，似然也是。

<!-- p.42/43 -->

我们现在用 $P(\cdot)$ 同时表示连续变量的概率密度、离散变量的概率与逻辑命题的概率。连续变量 $v$ 落在 $a$ 与 $b$ 之间（$b>a$）的概率定义为 $\int_a^b\mathrm{d}v\,P(v)$。$P(v)\,\mathrm{d}v$ 无量纲。密度 $P(v)$ 是有量纲的量，量纲与 $v$ 相反——与无量纲的离散概率不同。看到大于 1 的概率密度不要惊讶：这很正常，没有任何问题，只要对任何区间 $(a,b)$ 有 $\int_a^b\mathrm{d}v\,P(v)\le1$。条件与联合概率密度定义方式与条件、联合概率完全一样。

> <span style="color:#00838f;">**[习题 2.8]** [2] 假设 $f_H$ 上均匀先验 $P(f_H)=1$，求解例 2.7（p.30）提出的问题。画出 $f_H$ 的后验分布草图，并计算第 $N+1$ 次结果为正面的概率，针对：(a) $N=3$，$n_H=0$；(b) $N=3$，$n_H=2$；(c) $N=10$，$n_H=3$；(d) $N=300$，$n_H=29$。beta integral（贝塔积分）会很有用：

$$
\int_0^1\mathrm{d}p_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!\,F_b!}{(F_a+F_b+1)!}. \tag{2.32}
$$

</span>

<!-- p.43 -->

回看例 2.6（p.27）与方程 (2.31) 也许有启发。人们有时把「给未知参数（如 $f_H$）指派先验分布」与「对参数值做初始猜测」混淆。但 $f_H$ 上的先验 $P(f_H)$ 不是「一开始我猜 $f_H=1/2$」这样的简单陈述：先验是 $f_H$ 上的概率密度，它规定「$f_H$ 落在任何区间 $(f,f+\delta f)$」的先验信念程度。很可能我们对 $f_H$ 的先验关于 1/2 对称，使先验下 $f_H$ 的均值为 1/2。此时第一次抛掷 $x_1$ 的 predictive distribution（预测分布）确实是

$$
P(x_1=\text{head})=\int\mathrm{d}f_H\,P(f_H)P(x_1=\text{head}\mid f_H)=\int\mathrm{d}f_H\,P(f_H)f_H=1/2. \tag{2.33}
$$

但后续抛掷的预测将依赖整个先验分布，而不只是它的均值。

**数据压缩与逆向概率。** 考虑以下任务。

<span style="color:#00838f;">**[例 2.9]** 编写一个能压缩如下二进制文件的计算机程序：

```
0000000000000000000010010001000000100000010000000000000000000000000000000000001010000000000000110000
1000000000010000100000000010000000000000000000000100000000000000000100000000011000001000000011000100
0000000001001000000000010001000000000000000011000000000000000000000000000010000000000000000100000000
```

所示字符串含 $n_1=29$ 个 1 与 $n_0=271$ 个 0。直观上，压缩利用文件的可预测性。此例中，文件的源似乎更可能发出 0 而不是 1。压缩这个文件的数据压缩程序必须（隐式或显式地）处理这样的问题：「这个文件的下一个字符是 1 的概率是多少？」你不觉得这个问题与例 2.7（p.30）性质相似吗？我觉得像。本书的主题之一就是：data compression（数据压缩）与 data modelling（数据建模）是一回事，都应当像例 2.6 的瓮一样用逆向概率处理。例 2.9 在第 6 章求解。

<!-- p.43/44 -->

**似然原理（The likelihood principle）。** 请解以下两道习题。

<span style="color:#00838f;">**[例 2.10]** 瓮 A 含三个球：一黑二白；瓮 B 含三个球：二黑一白。随机选一个瓮并摸一个球。球是黑的。所选瓮是瓮 A 的概率是多少？

<span style="color:#00838f;">**[例 2.11]** 瓮 A 含五个球：一黑、二白、一绿、一粉；瓮 B 含五百个球：二百黑、一百白、五十黄、四十青、三十赭、二十五绿、二十五银、二十金、十紫。[A 的球五分之一是黑的；B 的是五分之二。]随机选一个瓮并摸一个球。球是黑的。瓮是瓮 A 的概率是多少？

<!-- p.44 -->

你注意到解的什么特点？每个答案依赖各瓮内容的细节吗？其他可能结果及其概率的细节是无关的。唯一要紧的是：在不同假设下，实际发生的结果（这里是摸到黑球）的概率。我们只需要知道 likelihood（似然），即发生的数据的概率如何随假设变化。这个关于推断的简单规则称为 likelihood principle（似然原理）：

> **似然原理**：给定数据 $d$ 关于参数 $\theta$ 的生成模型 $P(d\mid\theta)$，观察到特定结果 $d_1$ 后，所有推断与预测应只依赖函数 $P(d_1\mid\theta)$。

尽管这个原理很简单，许多经典统计方法违反它。

<!-- p.44/45 -->

## <span style="color:#c0392b;">2.4 熵及相关函数的定义（Definition of entropy and related functions）</span>

结果 $x$ 的 Shannon information content（香农信息含量）定义为

$$
h(x)=\log_2\frac{1}{P(x)}. \tag{2.34}
$$

它以 bits（比特）度量。[「bit」一词也用来指取值为 0 或 1 的变量；希望上下文总能说清用的是哪一种含义。]

接下来几章我们将确立：香农信息含量 $h(a_i)$ 确实是事件 $x=a_i$ 信息含量的自然度量。到那时我们将把这个量的名字简称为「信息含量」。

表 2.9 第四列展示从英语文档随机选字符时 27 个可能结果的香农信息含量：结果 $x=z$ 的香农信息含量为 10.4 比特，$x=e$ 的为 3.5 比特。

> <span style="color:#00838f;">**[表 2.9]** 字母 a–z 及空格的香农信息含量（$p_i$ 概率、$h(p_i)$ 信息含量，单位比特）：a: .0575/4.1，b: .0128/6.3，c: .0263/5.2，d: .0285/5.1，e: .0913/3.5，f: .0173/5.9，g: .0133/6.2，h: .0313/5.0，i: .0599/4.1，j: .0006/10.7，k: .0084/6.9，l: .0335/4.9，m: .0235/5.4，n: .0596/4.1，o: .0689/3.9，p: .0192/5.7，q: .0008/10.3，r: .0508/4.3，s: .0567/4.1，t: .0706/3.8，u: .0334/4.9，v: .0069/7.2，w: .0119/6.4，x: .0073/7.1，y: .0164/5.9，z: .0007/10.4，空格(-): .1928/2.4。加权平均 $\sum_i p_i\log_2\frac{1}{p_i}=4.1$ 比特。</span>

<!-- p.45 -->

系综 $X$ 的 entropy（熵）定义为一个结果的平均香农信息含量：

$$
H(X)\equiv\sum_{x\in\mathcal{A}_X}P(x)\log\frac{1}{P(x)}, \tag{2.35}
$$

对 $P(x)=0$ 的约定是 $0\times\log\frac{1}{0}\equiv0$，因为 $\lim_{\theta\to0^+}\theta\log\frac{1}{\theta}=0$。与信息含量一样，熵以比特度量。方便时我们也可把 $H(X)$ 写作 $H(p)$，$p$ 是向量 $(p_1,p_2,\dots,p_I)$。$X$ 的熵的另一个名字是 $X$ 的 uncertainty（不确定性）。

<span style="color:#00838f;">**[例 2.12]** 从英语文档随机选一个字母的熵约为 4.11 比特（假设其概率如表 2.9 给出）。这个数是在分布 $p_i$（第三列）下对 $\log\frac{1}{p_i}$（第四列）取平均得到的。

我们现在注意熵函数的一些性质：

- $H(X)\ge0$，等号成立当且仅当某个 $p_i=1$。[「iff」即「当且仅当」。]
- $p$ 均匀时熵最大：

$$
H(X)\le\log(|\mathcal{A}_X|),\quad \text{等号当且仅当 } p_i=1/|\mathcal{A}_X| \text{（所有 } i\text{）}. \tag{2.36}
$$

> <span style="color:#2471a3;">**[译者注｜记号]** 竖线「$|\cdot|$」有两种含义：$\mathcal{A}_X$ 是集合时，$|\mathcal{A}_X|$ 表示 $\mathcal{A}_X$ 中元素的个数；$x$ 是数时，$|x|$ 是绝对值。</span>

<!-- p.45 -->

The redundancy（冗余度）度量 $H(X)$ 与其最大可能值 $\log(|\mathcal{A}_X|)$ 之间的相对差。$X$ 的冗余度为

$$
1-\frac{H(X)}{\log|\mathcal{A}_X|}. \tag{2.37}
$$

本书不会用到「冗余度」，所以没有给它分配符号。

$X,Y$ 的 joint entropy（联合熵）为

$$
H(X,Y)=\sum_{xy\in\mathcal{A}_X\mathcal{A}_Y}P(x,y)\log\frac{1}{P(x,y)}. \tag{2.38}
$$

对独立随机变量熵具有可加性：

$$
H(X,Y)=H(X)+H(Y) \quad \text{iff } P(x,y)=P(x)P(y). \tag{2.39}
$$

我们目前的信息含量定义只适用于有限集合 $\mathcal{A}_X$ 上的离散概率分布。定义可以扩展到无限集，不过熵那时可能无穷。连续集合上概率密度的情形在第 11.3 节处理。与熵有关的更多重要定义与习题见第 8.1 节。

<!-- p.45/46 -->

## <span style="color:#c0392b;">2.5 熵的可分解性（Decomposability of the entropy）</span>

熵函数满足一个递归性质，计算熵时非常有用。为方便，我们扩展记号，把 $H(X)$ 写作 $H(p)$，$p$ 是与系综 $X$ 相关联的概率向量。

先用例子说明。设想随机变量 $x\in\{0,1,2\}$ 的产生方式：先抛一枚均匀硬币决定是否 $x=0$；若 $x\neq0$，再抛一次均匀硬币决定 $x$ 是 1 还是 2。$x$ 的概率分布为

$$
P(x=0)=\frac{1}{2};\qquad P(x=1)=\frac{1}{4};\qquad P(x=2)=\frac{1}{4}. \tag{2.40}
$$

$X$ 的熵是多少？可以暴力计算：

$$
H(X)=\frac{1}{2}\log2+\frac{1}{4}\log4+\frac{1}{4}\log4=1.5; \tag{2.41}
$$

<!-- p.46 -->

也可以用如下分解——$x$ 的值被逐渐揭示。设想先得知是否 $x=0$，然后若 $x\neq0$，再得知是哪个非零值。「是否 $x=0$」的揭示等价于揭示一个分布为 $\{1/2,1/2\}$ 的二元变量，其熵为 $H(1/2,1/2)=\frac{1}{2}\log2+\frac{1}{2}\log2=1$ 比特。若 $x\neq0$，我们得知第二次抛硬币的值——这也是分布 $\{1/2,1/2\}$ 的二元变量，熵 1 比特。但我们只有一半时间会经历第二次揭示，所以熵可写为：

$$
H(X)=H(1/2,1/2)+\frac{1}{2}H(1/2,1/2). \tag{2.42}
$$

推广之，关于任何概率分布 $p=\{p_1,p_2,\dots,p_I\}$ 熵的观察是：

$$
H(p)=H(p_1,\,1-p_1)+(1-p_1)\,H\Bigl(\frac{p_2}{1-p_1},\frac{p_3}{1-p_1},\dots,\frac{p_I}{1-p_1}\Bigr). \tag{2.43}
$$

写成公式时这个性质遗憾地显得丑陋；但它是个简单的性质，应当用起来。进一步推广，熵对任何 $m$ 满足：

$$
\begin{aligned}
H(p)=&\ H[(p_1+p_2+\cdots+p_m),\,(p_{m+1}+p_{m+2}+\cdots+p_I)]\\
&+(p_1+\cdots+p_m)\,H\Bigl(\frac{p_1}{p_1+\cdots+p_m},\dots,\frac{p_m}{p_1+\cdots+p_m}\Bigr)\\
&+(p_{m+1}+\cdots+p_I)\,H\Bigl(\frac{p_{m+1}}{p_{m+1}+\cdots+p_I},\dots,\frac{p_I}{p_{m+1}+\cdots+p_I}\Bigr).
\end{aligned} \tag{2.44}
$$

<span style="color:#00838f;">**[例 2.13]** 一个源从字母表 $\mathcal{A}=\{0,1,\dots,9,a,b,\dots,z\}$ 产生字符 $x$：以概率 1/3，$x$ 是数字（0–9）；以概率 1/3，$x$ 是元音（a,e,i,o,u）；以概率 1/3，$x$ 是 21 个辅音之一。所有数字等概率，元音与辅音亦然。估计 $X$ 的熵。

**解。** $\log 3+\frac{1}{3}(\log10+\log5+\log21)=\log3+\frac{1}{3}\log1050\simeq\log30$ 比特。

<!-- p.46/47 -->

## <span style="color:#c0392b;">2.6 Gibbs 不等式（Gibbs' inequality）</span>

> <span style="color:#2471a3;">**[译者注]** 原书边注：Leibler 中的「ei」与 heist 中的发音相同（/aɪ/）。

定义在同一字母表 $\mathcal{A}_X$ 上的两个概率分布 $P(x)$ 与 $Q(x)$ 之间的 relative entropy（相对熵）或 Kullback–Leibler divergence（Kullback–Leibler 散度）为

$$
D_{\mathrm{KL}}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}. \tag{2.45}
$$

相对熵满足 Gibbs' inequality（Gibbs 不等式）：

$$
D_{\mathrm{KL}}(P\|Q)\ge0, \tag{2.46}
$$

等号仅当 $P=Q$。注意一般情形相对熵在交换分布 $P$ 与 $Q$ 时不对称：一般 $D_{\mathrm{KL}}(P\|Q)\neq D_{\mathrm{KL}}(Q\|P)$，所以 $D_{\mathrm{KL}}$ 虽然有时被称为「KL 距离」，严格来说不是 distance（距离）。相对熵在 pattern recognition（模式识别）与 neural networks（神经网络）中以及在信息论中都重要。

Gibbs 不等式大概是本书中最重要的不等式。它与其他许多不等式可以用 convexity（凸性）概念证明。

<!-- p.47 -->

## <span style="color:#c0392b;">2.7 凸函数的 Jensen 不等式（Jensen's inequality for convex functions）</span>

> <span style="color:#2471a3;">**[译者注]** 「convex ⌣」与「concave ⌢」可读作「convex-smile（凸-微笑）」与「concave-frown（凹-皱眉）」。这个术语有用冗余：一个人可能忘记 convex 与 concave 哪边朝上，但很难把微笑与皱眉搞混。

**Convex ⌣ 函数（凸函数）。** 若函数 $f(x)$ 的每一条 chord（弦）都位于函数上方（图 2.10），即对所有 $x_1,x_2\in(a,b)$ 与 $0\le\lambda\le1$，

$$
f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2), \tag{2.47}
$$

则称 $f(x)$ 在 $(a,b)$ 上 convex ⌣（凸）。若对所有 $x_1,x_2\in(a,b)$，等号只在 $\lambda=0$ 与 $\lambda=1$ 成立，则 $f$ strictly convex ⌣（严格凸）。concave ⌢（凹）与 strictly concave ⌢（严格凹）函数有类似定义。

一些严格凸 ⌣ 函数：

- 对所有 $x$：$x^2$、$e^x$、$e^{-x}$；
- 对 $x>0$：$\log(1/x)$ 与 $x\log x$。

（图 2.11：$x^2$、$e^{-x}$、$\log\frac{1}{x}$、$x\log x$ 的图像。）

**Jensen's inequality（Jensen 不等式）。** 若 $f$ 是凸 ⌣ 函数且 $x$ 是随机变量，则：

$$
\mathbb{E}[f(x)]\ge f(\mathbb{E}[x]), \tag{2.48}
$$

$\mathbb{E}$ 表示 expectation（期望）。若 $f$ 严格凸 ⌣ 且 $\mathbb{E}[f(x)]=f(\mathbb{E}[x])$，则随机变量 $x$ 是常数。

对凹 ⌢ 函数，Jensen 不等式也可以重写，不等号方向反转。

<!-- p.47/48 -->

Jensen 不等式的物理版本如下。

> <span style="color:#00838f;">**[重心（Centre of gravity）]** 若把质量 $p_i$ 放在凸 ⌣ 曲线 $f(x)$ 上的位置 $(x_i,f(x_i))$，则这些质量的 centre of gravity（重心）——位于 $(\mathbb{E}[x],\mathbb{E}[f(x)])$——位于曲线上方。若这不能说服你，请随意做下面这道习题。</span>

<span style="color:#00838f;">**[习题 2.14]** [2, p.41] 证明 Jensen 不等式。

<span style="color:#00838f;">**[例 2.15]** 三个正方形的平均面积 $\bar{A}=100\ \mathrm{m}^2$。它们的边长平均值 $\bar{l}=10\ \mathrm{m}$。关于三个正方形中最大一个的大小能说什么？[用 Jensen 不等式。]

**解。** 设 $x$ 为正方形边长，$x$ 在三个长度 $l_1,l_2,l_3$ 上的概率为 $1/3,1/3,1/3$。于是我们拥有的信息是 $\mathbb{E}[x]=10$ 与 $\mathbb{E}[f(x)]=100$，其中 $f(x)=x^2$ 是从长度到面积的映射。这是严格凸 ⌣ 函数。注意到 $\mathbb{E}[f(x)]=f(\mathbb{E}[x])$ 成立，因此 $x$ 是常数，三个长度必全相等。最大正方形的面积是 $100\ \mathrm{m}^2$。

<!-- p.48 -->

**凸性与凹性也和最大化有关。** 若 $f(x)$ 凹 ⌢ 且存在一点使

$$
\frac{\partial f}{\partial x_k}=0 \text{ 对所有 } k, \tag{2.49}
$$

则 $f(x)$ 在该点取最大值。逆命题不成立：若凹 ⌢ 函数 $f(x)$ 在某 $x$ 处最大化，未必有 $\nabla f(x)=0$。例如 $f(x)=-|x|$ 在 $x=0$ 处最大化，但导数在 $x=0$ 处无定义；$f(p)=\log(p)$（$p\in(0,1)$ 的概率）在范围边界 $p=1$ 处最大化，那里 $\mathrm{d}f(p)/\mathrm{d}p=1$。

## <span style="color:#c0392b;">2.8 习题（Exercises）</span>

**随机变量之和。**

<span style="color:#00838f;">**[习题 2.16]** [3, p.41] (a) 掷两枚普通骰子（面标 1–6）。点数之和的概率分布是什么？两枚点数之差的绝对值的概率分布是什么？
(b) 掷一百枚普通骰子。点数之和的概率分布大致是什么？画出概率分布草图并估计其均值与标准差。
(c) 如何用数字 $\{0,1,2,3,4,5,6\}$ 给两枚立方骰子标号，使两枚骰子掷出后其点数之和在整数 1–12 上具有均匀概率分布？
(d) 一百枚骰子有没有办法用整数标号，使掷出后点数之和在整数上接近均匀分布？

> <span style="color:#2471a3;">**[译者注｜边框说明]** 这道习题意在帮你思考 central-limit theorem（中心极限定理）：若独立随机变量 $x_1,x_2,\dots,x_N$ 有均值 $\mu_n$ 与有限方差 $\sigma_n^2$，则当 $N$ 大时，和 $\sum_nx_n$ 的分布趋于 normal (Gaussian) distribution（正态/高斯分布），均值 $\sum_n\mu_n$、方差 $\sum_n\sigma_n^2$。</span>

> <span style="color:#2471a3;">**[译者注｜跨课程连接]** 本章与你的两门课同时接轨：§2.1–2.3 就是 6.431 概率论的贝叶斯入门（Jo 检测病例、十一瓮、似然原理），而 §2.4–2.6 的熵与 KL 散度正是凸优化 Boyd 书例 3.19 的负熵/相对熵的「信息论正身」。看到 $D_{\mathrm{KL}}\ge0$（Gibbs 不等式）时，回想 Boyd 书「Gibbs 不等式可以由凸性证明」——Jensen 不等式（§2.7）就是那把钥匙，两本书在这里完全咬合。</span>

---

> <span style="color:#7f8c8d;">§2.1–2.8 正文与习题题面翻译完毕。习题解答（书页 pp.40–41 起）暂未翻译。下一章：mackay_ch03（More about Inference，再谈推断，PDF p.60–78）。</span>
