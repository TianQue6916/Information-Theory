> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l6 · 行内双语视觉转录版 · 原图见 fig/l6/</span>



<span style="color:#2471a3;">**[lecture]**</span> **第 6 讲：推断与噪声信道的信息度量（Inference and Information Measures for Noisy Channels）**。本讲前半段收束数据压缩（Data compression）话题：算术编码（arithmetic coding）、预测器与 PPM、Dasher 输入法、随机数基准；后半段开启新主题——噪声信道（noisy channel）上的贝叶斯推断与信息度量（互信息 mutual information）。



### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕



![l6-p1](fig/l6/mgp00001.png)



课程封面与大纲页。左侧是一幅圆盘内的分形树装饰图：绿色圆/方节点自圆心向外生长，越靠圆盘边缘节点越小越密，颜色渐变为蓝、红、品红的小环——〔本页左侧为纯装饰图示〕。



课程路线图（编号为讲次）：

- 讲次 1：噪声信道编码（Noisy-channel coding）；

- **信源编码（Source coding，即数据压缩 Data compression）**（青色圆点强调）：

  - 讲次 2：信息量（information content）与熵（entropy）；

  - 讲次 3：典型性（typicality）与信源编码定理（source coding theorem）；

  - 讲次 4：符号码（symbol codes）；

  - 讲次 5：符号码与算术编码（Arithmetic coding）；

- **噪声信道编码（Noisy-channel coding）**（青色圆点强调）：

  - 讲次 6：推断（inference）与噪声信道的信息度量（information measures for noisy channels）——即本讲。



### p.2 〔Q:（问题：）〕



![l6-p2](fig/l6/mgp00002.png)



<span style="color:#2471a3;">**[example]**</span> **问（Q）：** 若用符号码（symbol code）对如下系综（ensemble）编码：

$\mathcal{A}_X = \{\mathsf{a},\mathsf{b},\mathsf{c},\mathsf{d}\}$，$\mathcal{P}_X = \{1/2,\,1/4,\,1/8,\,1/8\}$，

$\mathcal{C} = \{0,\,10,\,110,\,111\}$，

那么从编码后的比特流中随机抽取一个比特，它是 $1$ 的概率「$p_1$」是多少？

- A：$p_1 < \tfrac{1}{2}$

- B：$p_1 = \tfrac{1}{2}$

- C：$p_1 > \tfrac{1}{2}$



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题的答案选 A，但比答案更有价值的是「随机抽一个 bit（比特）」这句话到底在抽什么：它是一个必须先钉死采样机制、否则连概率都无定义的问题。给定的 symbol code（符号码）$\mathcal{C}=\{0,10,110,111\}$ 给四个符号分别花掉 $1,2,3,3$ 个 bit（比特），平均码长 $L=1.75$ bit（比特）；而四个 codeword（码字）里 $1$ 的占比分别是 $0$、$1/2$、$2/3$、$1$。把这三个数摆在一起就能看出分歧的来源：抽样粒度一变，权重就从概率换成了长度。
>
> 机制要拆成两步试验才成立。第一步按 $\mathcal{P}_X$ 抽一个符号，第二步在该符号的 codeword（码字）内均匀抽一位；于是抽到 $1$ 的概率是「码字内 $1$ 的占比」对符号分布取期望，即 $p_1=\sum_i p_i\,n_i^{(1)}/l_i$，其中 $n_i^{(1)}$ 是第 $i$ 个 codeword（码字）里 $1$ 的个数、$l_i$ 是它的长度。这一步用的正是概率论里的 law of total expectation（全期望公式）：先把指示变量条件在符号上，再对符号求期望。为什么必须这样拆？因为编码后比特流的长度是随机的，只有给定符号之后「第几位」才是均匀的；在整条流上谈「均匀抽一位」，得先有一个长度分布，那是额外的一层模型。换句话说，抽样机制不是题目的附属细节，它就是概率空间的一部分——这就是这道题真正的考点，不是算一个分数。
>
> 把两种读法都算一遍，它们分别落在 A 和 B 上，这才是这道单选题的设计意图。读法一（先抽符号、再抽位）：$p_1=\frac12\cdot 0+\frac14\cdot\frac12+\frac18\cdot\frac23+\frac18\cdot 1=\frac{3}{24}+\frac{2}{24}+\frac{3}{24}=\frac{8}{24}=\frac13$。读法二（在足够长的比特流上按位置均匀抽）：每个符号平均贡献给 $1$ 的个数是 $0+\frac14+\frac{2}{8}+\frac{3}{8}=0.875$，平均长度是 $1.75$，故比值为 $0.875/1.75=1/2$。也就是说，把「均匀」放在位置这一层，答案恰好是 $1/2$；把它放在符号这一层，答案是 $1/3$。课程取读法一，因为要考察的是「符号层最优是否带来比特层均匀」这个问题；读法二的答案虽然算出来也是定值，但它回答的是另一个问题（长消息里 $1$ 的平均占比），作为反例不干净。能自己手算发现这个 $1/2$，才算真的读懂了题干。
>
> 顺带得到一个必须记住的结论：这份码已经是最优的。它的熵 $H=1.75$ bit（比特），平均码长 $L=1.75$ bit（比特），与 Shannon 限（香农极限）取等，但它的比特边际仍然停在 $1/3$ 而不是 $1/2$。所以「压到熵」与「输出看起来像均匀随机数」是两件事：前者说的是期望长度，后者说的是边际分布。只有当码长固定（例如四个符号各 $2$ bit（比特））时，$p_1$ 才必然等于 $1/2$，因为定长切断了长度与符号之间的耦合。
>
> 跨课程连接有两处值得对上。其一是 6.042J 里期望的线性性：那里的期望通常一层求和就算完，而这里需要「先条件、再求期望」的两层结构，这正是后文 mutual information（互信息）用到的计算范式——先条件掉一层，再对另一层取期望。其二是 CSAPP 第 2 章的二进制表示与第 6 章的 cache（高速缓存）位切分：CSAPP 里一个地址被切成 tag（标记）、index（索引）、offset（偏移）三段，每段的位统计由 ISA（指令集体系结构）固定，读者不需要为「某一位是 $1$ 的概率」操心；这里的位布局由概率分布决定，于是位的统计量本身成了需要计算的量。区别在于来源：前者是硬件给定的约定，后者是压缩器设计者要论证的目标。
>
> 收束回正文：$p_1=1/3$ 说明 symbol code（符号码）只在符号这一层对齐了熵，bit（比特）层仍留着信源的偏斜；第 19 页起进入噪声信道时，被反复利用的就是这层残余结构。


### p.3 〔Last time - symbol codes（上次课：符号码）〕



![l6-p3](fig/l6/mgp00003.png)



<span style="color:#2471a3;">**[section]**</span> 回顾上次课的符号码结论：

- 理想码长（ideal codelengths）$l_i^*$ 就是信息量（information contents）：

```math

l_i^* = \log \frac{1}{p_i}

```

- 最优符号码的期望长度（expected length）$L$ 满足：

```math

H(X) \le L < H(X) + 1

```



- 那么，压缩到此就完结了吗（Does that wrap up compression?）？最优符号码与 Shannon 极限（Shannon limit）的差距在每字符 1 比特（one bit per character）以内。

- 同卵双胞胎（identical twins）可以帮助构造压缩器。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $H(X)\le L<H(X)+1$ 这个夹逼式的关键不在数字，而在「$+1$ 是逐符号取整的代价，因此只能靠分组摊薄」。把它抽成一个可复用的模板：block-and-dilute（分组摊薄法）。三步是：先把每个符号的理想码长 $l_i^*=\log_2(1/p_i)$ 向上取整得 $l_i=\lceil l_i^*\rceil$，逐项放缩得 $L<H+1$；再把 $N$ 个符号捆成一个超级符号，其概率为 $P(\mathbf{x})$，对超级符号取整的误差仍小于 $1$ bit（比特），但摊到 $N$ 个符号上就是小于 $1/N$ bit（比特）；最后令 $N\to\infty$，得每符号 $H$ bit（比特）可达。同一个模板在别处反复出现：把一次性固定开销搬到更大的计量单位上去摊。
>
> 两个不等式各自怎么来，才看得出「$1$」为什么压不下去。上界是纯放缩：取整满足 $\lceil x\rceil<x+1$，代入 $x=\log_2(1/p_i)$ 后 $L=\sum_i p_i\lceil\log_2(1/p_i)\rceil<\sum_i p_i\big(\log_2(1/p_i)+1\big)=H+1$。下界不是放缩而是约束：任何 prefix-free（前缀无关）的 symbol code（符号码）都要满足 Kraft inequality（Kraft 不等式）$\sum_i 2^{-l_i}\le 1$；把 $2^{-l_i}$ 与 $p_i$ 逐项用对数不等式 $\ln z\le z-1$ 比较，就得到 $L\ge H$。这个下界与码的具体构造无关，只与「码字长度是否可行」有关，所以它不可突破；上界只是某一种构造（取整构法）的成本，换个构造就能变好。
>
> 「identical twins（同卵双胞胎）」的比喻落在这里：把相邻两个符号绑成一对，取整误差由两个符号分摊。用具体数字看差距。取二元信源 $P(0)=0.9$、$P(1)=0.1$，熵 $H=0.1\times\log_2 10+0.9\times\log_2(1/0.9)=0.1\times 3.3219+0.9\times 0.1520=0.3322+0.1368=0.4690$ bit（比特）。逐符号 Huffman coding（哈夫曼编码）对二元信源只能给每个符号 $1$ bit（比特），故 $L=1$，亏 $1-0.469=0.531$ bit（比特），已经用掉了「$+1$」这条上界的大半。改成两个一组：四个符号对的概率是 $0.81,0.09,0.09,0.01$，Huffman coding（哈夫曼编码）的合并顺序是 $0.01+0.09\to 0.10$、$0.09+0.10\to 0.19$、$0.19+0.81\to 1$，给出码长 $1,2,3,3$，于是每个符号对的期望长度 $0.81\times 1+0.09\times 2+0.09\times 3+0.01\times 3=0.81+0.18+0.27+0.03=1.29$ bit（比特），折合每符号 $0.645$ bit（比特），亏 $0.645-0.469=0.176$ bit（比特）。若改用取整构法，四个符号对的码长是 $1,4,4,7$，期望长度 $0.81+0.36+0.36+0.07=1.60$ bit（比特）、每符号 $0.80$ bit（比特），亏 $0.331$ bit（比特）——仍在 $1/2$ 以内，且四个一组时按取整构法的保证是每符号亏小于 $1/4$ bit（比特）。数字对比说明「$+1$」不是理论下界，它只是「不分组」的代价。
>
> 还有一步必须交代：为什么不能让「码长取分数」来直接消掉取整误差？因为信道一次只搬整数个 bit（比特），一个符号不可能占 $2.32$ bit（比特），这是离散性带来的硬约束。分组摊薄的物理实现正是如此：arithmetic coding（算术编码）把码长做成实数，但最终输出的仍是整数 bit（比特），只不过这一次取整由整条消息共同承担，不再逐符号分配。typicality（典型性）给出这套做法的定量骨架：长度 $N$ 的 typical set（典型序列）约有 $2^{NH}$ 条，占全部 $2^N$ 条序列的比例约为 $2^{-N(1-H)}$；取 $H=0.4690$、$N=100$ 时是 $2^{46.9}$ 条，占 $2^{100}$ 的 $2^{-53.1}$。既然只需要区分这么少的序列，给它们统一分配 $47$ bit（比特）的等长码字就够，折合每符号 $0.47$ bit（比特），与熵 $0.4690$ bit（比特）只差 $0.001$ bit（比特）。误差是被 $N$ 除掉的，不是被某个更聪明的逐符号规则消掉的——这就是 AEP（asymptotic equipartition property，渐进均分性）在计数上的全部意思。
>
> 跨课程连接取 CSAPP 第 6 章的 cache（高速缓存）。一个 cache line（缓存行）带一次 tag（标记）比较，tag（标记）的开销按行固定，所以把 line 从 $64$ 字节放大到 $512$ 字节，tag（标记）摊到每字节的开销就缩到八分之一——与「把 $N$ 个符号捆成超级符号再摊取整误差」是同一笔算术。区别在摊薄的对象与代价：cache（高速缓存）摊的是地址位，代价是放大 line 牺牲空间局部性的粒度；压缩摊的是取整浪费的 bit（比特），代价是超级符号的 alphabet（字母表）按 $K^N$ 指数膨胀。摊薄从来不是免费的，两端都得付一笔别的账。
>
> 收束回正文：source coding theorem（信源编码定理）把这个 $N\to\infty$ 的极限说成可达，而 arithmetic coding（算术编码）的实用做法等价于把 $N$ 取成整个文件，于是取整误差被摊到只剩一个常数项——这正是下一页那个 $+2$ 的来源。


### p.4 〔Arithmetic coding（算术编码）〕



![l6-p4](fig/l6/mgp00004.png)



本页为 MacKay 的算术编码演示程序（applet）截图，直观展示算术编码的区间剖分。顶栏选项：uniform（均匀）、bounded（有界）、at_mouse（在鼠标处）、at_cross（在十字处）、Colors: 28、Truncate: 6、At: < > 6、Slide: < > -2。

- 左面板：单位区间按概率切成彩色区块：上方淡蓝大区块、右侧粉色区块标 `:a`，下方品红区块标 `:b`，右下角还有更小的深紫色小区块——对应已输入串 `:ba` 之后的细分。

- 右面板：区间按二进制剖分，标出 `:0`、`:00`、`:01`（右上角一小块绿色）与 `:1`——即以二进制前缀划分码区间。

- 底部控制条：Reset、magnfn: 0、width: 1.0、centre: 0.5、区间刻度 0.0–1.0；左侧模型设置 english1 / english2 / jack、Alphabet 3、adaptive 0.43 0.43 0.14；右侧 Alphabet 2、adaptive 0.5 0.9；Active、Pushiness 1、ps；Clean、VariableL、DelDisRel、Reinstate；状态行 `:ba`（2）与 `:01`（2）；按钮 Quit、Hide、Show（灰置）、OneCanvas、Dump、Mousepad、Help。



〔本页为软件截图型图示页〕



### p.5 〔Arithmetic coding（算术编码）〕



![l6-p5](fig/l6/mgp00005.png)



<span style="color:#2471a3;">**[theorem]**</span> 算术编码 achieves（达到）：

```math

l(\mathbf{x}) \le \log_2 \frac{1}{P(\mathbf{x})} + 2

```

其中 $\mathbf{x}$ 是整个文件（whole file）$x_1 x_2 \ldots x_N$。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个不等式要回答的设计问题是：既然逐符号编码的取整代价是每符号 $1$ bit（比特），为什么换成 arithmetic coding（算术编码）之后整条消息只剩一个常数代价？答案是它不再为每个符号分配码字，而是为整条消息维护一个 interval（区间），最后只输出一个能唯一指向该 interval（区间）的最短二进制前缀。
>
> 机制分三步，每一步都要看清它替掉了什么。第一步，模型给出 cumulative distribution（累积分布）：把单位区间按 $P(x_1)$ 切给第一个符号，再在当前区间内按 $P(x_2\mid x_1)$ 切第二个，如此下去，$N$ 个符号走完剩下的一段，其长度恰好是 $P(\mathbf{x})=\prod_{t}P(x_t\mid x_{<t})$。第二步，编码器只需输出落在该 interval（区间）里的一个二进制数，长度只要够区分这条消息与其余所有消息。第三步，长度记账：区间长 $\ell=P(\mathbf{x})$，要指认它至少需要 $\log_2(1/\ell)$ bit（比特）；实现上再把两件小事各记一位——向上取整到整数 bit（比特）算一位，避开码值落在区间端点上（解码时闭区间与开区间的差别会造成歧义）算一位——于是得到 $+2$。两项都是「每条消息一次」的常数，与 $N$ 无关，这是全部要点。
>
> 换成数字看量级。设信源 $P(a)=0.75$、$P(b)=0.25$，熵 $H=0.75\times\log_2(1/0.75)+0.25\times\log_2(1/0.25)=0.75\times 0.4150+0.25\times 2=0.3113+0.5=0.8113$ bit（比特）。文件长 $N=1000$ 个符号时，理想信息量是 $811.3$ bit（比特）。逐符号 Huffman coding（哈夫曼编码）对二元信源只能给 $1$ bit（比特）/符号，输出 $1000$ bit（比特），比理想多 $188.7$ bit（比特）——这 $188.7$ bit（比特）就是 $1000$ 次取整的累积。arithmetic coding（算术编码）的上界是 $811.3+2=813.3$ bit（比特），浪费不超过 $2$ bit（比特）。把文件放大到 $1$ GB（约 $8\times 10^9$ bit（比特））：Huffman coding（哈夫曼编码）的浪费约为 $(1-0.8113)\times 8\times 10^9=1.51\times 10^9$ bit（比特），约 $189$ MB；arithmetic coding（算术编码）仍然只浪费 $2$ bit（比特）。常数开销与线性开销在这里的比值是 $7.5$ 亿比 $1$。
>
> 还要看清上界的方向：它是「小于等于」，既保证最坏情况不超，也不保证达到下界 $\log_2(1/P)$。真正的压缩率由模型 $P$ 决定——若 $P$ 与真实分布差得远，$\log_2(1/P(\mathbf{x}))$ 本身就比真实熵大，$+2$ 根本不是瓶颈。所以压缩器被干净地切成两层：model（模型）负责产出 $P$，coder（编码器）负责把 $P$ 转成 bit（比特）；本讲的 PPM（prediction by partial match，部分匹配预测）与 six-gram（六元语法）都属于第一层。这也解释了算术编码为什么推广得动：换模型不用动编码器。
>
> 跨课程连接取 CLRS 的 binary search（二分搜索）。解码时手上有一个码值 $c\in[0,1)$，要从 $[0,1)$ 出发一路细分：把 $c$ 与累积分布的切点比较，落在第 $k$ 段就输出第 $k$ 个符号，再把区间收缩到那一段——这正是在一张每步重建的有序切点表上做二分下降，每步把候选区间乘上 $P(x_t\mid x_{<t})$。区别在于：CLRS 的 binary search（二分搜索）面对的是静态数组，比较次数 $O(\log n)$ 由数组长度决定；这里的「数组」由模型每步重算，收缩比例由概率决定，所以解码代价与 $\log_2(1/P)$ 同阶，正确性还依赖解码器与编码器用同一份模型（任何一点数值差异都会让两条路径分叉）。第二个连接是 CSAPP 第 2 章的浮点表示：算术编码要的「区间内最短二进制前缀」与 IEEE 754 尾数截断在形式上同源，都是把实数用有限位二进制近似；区别在目标——浮点要保住数值精度，arithmetic coding（算术编码）只要保住「落在哪个区间」这一位信息，因此它用比浮点数更短的位串就能完成任务。
>
> 收束：$+2$ 是 coder（编码器）这一侧的账，模型那一侧的账要由 $P$ 的准确度来付；下一节 PPM（prediction by partial match，部分匹配预测）与 six-gram（六元语法）讨论的正是怎么把 $P$ 做得更准。


### p.6 〔Data compression（数据压缩）〕



![l6-p6](fig/l6/mgp00006.png)



<span style="color:#2471a3;">**[section]**</span> 一个示例预测器（an example predictor）：

```math

P(x_t \mid x_1 x_2 x_3 \ldots x_{t-1})

```

演示文本（一段英语小说文字，用于现场演示「根据上文预测下一个字符」）：

`I'm afraid I don't know one,' said Harriet, rather alarmed at the pro…（「……『恐怕我不知道一个，』Harriet 说道，对这 pro……颇为惊慌」——模型此刻正要预测 "pro" 之后的字符。）



> <span style="color:#7f8c8d;">旁注：本页文本为等宽打字机字体，是课堂互动用的「猜下一字母」素材；结尾停在单词前缀 pro 处。</span>



### p.7 〔Data compression（数据压缩）〕



![l6-p7](fig/l6/mgp00007.png)



同一示例预测器 $P(x_t \mid x_1 x_2 x_3 \ldots x_{t-1})$。文本 `I'm afraid I don't know one,' said Harriet, rather alarmed at the_pro——本页把 "the pro" 的结尾以红色下划线标为 the_pro，表示模型刚读到哪里、正要预测下一字符。

红色大字：**PPM - 'prediction by partial match'**（PPM——「按部分匹配预测」算法）。



> <span style="color:#7f8c8d;">旁注：图中 the 之后红色的 pro 与红色下划线 _ 是幻灯片动画逐步标出的预测位置。</span>



### p.8 〔Six-gram model（六元语法模型）〕



![l6-p8](fig/l6/mgp00008.png)



五行预测演示（取自简·奥斯汀风格文本，每行的 `_` 与其后彩色字母标出模型对下一字符的逐位补全）：

- to her to be secure of a comfortable_provision,（……以确保一份舒适的供给（provision），）

- and be_proved in the right, when so many people said（并且被证明（proved）是对的，当那么多人说……）

- was an irresistible_proof of his great good sense,（是他极有见识的无可抗拒的证明（proof），）

- "Mrs. Bates, let me_propose your venturing on one of（「Bates 太太，请允许我提议（propose）你试一试其中之一……）

- was so great a personage in Highbury, that the_prospect（在 Highbury 是如此了不得的大人物，以致这前景（prospect）……）



黑色文字：Predictions proportional to frequencies (in this context)（预测与该语境下的频次（frequencies）成正比）。

大字标题：**Six-gram model**（六元语法模型）。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> six-gram（六元语法）模型的核心假设是把 $P(x_t\mid x_1\ldots x_{t-1})$ 截断成只依赖前 $5$ 个字符的 $P(x_t\mid x_{t-5}\ldots x_{t-1})$，再用语料里的条件频次 $c(wx)/c(w)$ 当概率。这个替换只在三个前提下成立：stationarity（平稳性，语言统计不随时间变）、$5$ 阶 Markov 性（只依赖前 $5$ 个字符）、以及每个上下文出现次数足够多。三者中最容易破的是第三条，它破得快，是因为上下文数目随长度指数增长。
>
> 把指数说清。设 alphabet（字母表）大小 $K=27$（$26$ 个字母加空格），长度 $m$ 的上下文有 $27^m$ 种：$m=1$ 时 $27$ 种，$m=3$ 时 $19683$ 种，$m=5$ 时 $27^5=14348907$ 种。若语料只有 $10^6$ 个字符，每个 $5$ 元上下文平均只被看到 $10^6/14348907\approx 0.070$ 次——绝大多数 $5$ 元上下文出现 $0$ 次或 $1$ 次。这不是「估计不够准」的程度问题，而是结构问题：在出现 $0$ 次的上下文上，maximum likelihood estimate（最大似然估计）给所有下一个字符概率 $0$，一旦真实字符出现，码长 $\log_2(1/0)$ 就是无穷大，整条消息编码失败。所以任何可用的 $n$-gram（$n$ 元语法）模型都必须给未见事件预留概率质量，这是 smoothing（平滑）与 escape（逃逸）机制存在的理由，不是事后修补。
>
> 用 add-one smoothing（加一平滑）看账单。设上下文 `pro` 在语料里出现 $3$ 次，后接字符是 `s`、`o`、`n`；maximum likelihood estimate（最大似然估计）给这三个各 $1/3$、其余 $24$ 个字符 $0$。add-one smoothing（加一平滑）改成 $\hat P=(c+1)/(n+K)=(c+1)/30$：见过的三个得 $4/30=0.1333$，没见过的得 $1/30=0.0333$。代价可以精确算：若真实后接 `s`，理想码长 $\log_2 3=1.585$ bit（比特），平滑后码长 $\log_2(1/0.1333)=\log_2 7.5=2.907$ bit（比特），多花 $1.32$ bit（比特）。这就是「留概率给未见事件」的价格：每遇一个真实符号多付约 $1.3$ bit（比特），换来不出无穷大。PPM（prediction by partial match，部分匹配预测）的做法更省：只在需要时才 escape（逃逸）到更短的上下文，不必一次性把所有未见字符抬起来，这就是 p.9 那串 `e_pro`、`_pro`、`pro`、`ro`、`o` 的逐级退化。
>
> 还有一层必须说清：为什么不能只用最长上下文？因为估计精度由样本数决定，而样本数随上下文变长按指数下降，于是形成 bias-variance trade-off（偏差-方差权衡）：短上下文样本多、估计稳但偏差大（丢掉长程依赖），长上下文偏差小但方差大（一次观测就决定概率）。PPM（prediction by partial match，部分匹配预测）的混合是让每一层各出一份预测、再按可靠度加权，短上下文兜底、长上下文求准。
>
> 跨课程连接取 CS144 的 RTT（round-trip time，往返时延）估计。TCP 用 exponentially weighted moving average（指数加权移动平均）从历史 RTT 样本估计未来 RTT，同样是「用历史样本当未来概率」，同样依赖平稳性——链路状况突变时估计会滞后，与语料风格突然切换时 $n$-gram（$n$ 元语法）失效是同一类错误。区别在估计对象：TCP 只估一个标量并在线即时更新，$n$-gram（$n$ 元语法）要估一个高维分布且通常离线更新。第二个连接取 6.006 的 hash table（哈希表）：以 $m$ 元上下文为键存计数是最直接的做法，但键的分布高度偏斜（少数上下文极热、多数极冷），与 6.006 证明期望 $O(1)$ 所依赖的均匀哈希假设差得很远；工程上改用 trie（前缀树）复用共享前缀，树根到叶的路径恰好就是上下文从短到长的退化序列，与 PPM（prediction by partial match，部分匹配预测）的结构一一对应。
>
> 收束：p.8 那五行 `provision`、`proved`、`proof`、`propose`、`prospect` 的补全，展示上下文够热时这套频次估计确实有效；p.9 的逐级退化，展示上下文不够热时它必须退到哪一层。


### p.9 〔Data compression - An example predictor（数据压缩·示例预测器）〕



![l6-p9](fig/l6/mgp00009.png)



示例预测器 $P(x_t \mid x_1 x_2 x_3 \ldots x_{t-1})$。文本 `I'm afraid I don't know one,' said Harriet, rather alarmed at the_pro（"e_pro" 以红色标出，为当前上下文）。

右侧蓝色小字自上而下列出逐渐变短的上下文（PPM 按不同长度分别做预测）：

- e_pro（上下文 "…e_pro"）

- _pro（上下文 "_pro"）

- pro（上下文 "pro"）

- ro（上下文 "ro"）

- o（上下文 "o"）



即：从最长上下文 "e_pro" 开始，逐级退化为 "_pro"、"pro"、"ro"、"o"——这是 PPM 多模型混合（blend）的直观展示：各长度上下文各自给出一份对下一字符的预测，再按权重混合。



### p.10 〔Other uses for arithmetic coding（算术编码的其他用途）〕



![l6-p10](fig/l6/mgp00010.png)



<span style="color:#2471a3;">**[section]**</span> 算术编码的其他用途：

- 高效书写（Efficient writing）——右上角为 Dasher 软件标志：两个小方格内含字母 a、b，旁书 **Dasher: Information-Efficient Text Entry**（Dasher：信息高效的文本输入）。

- 压缩（Compression）：文本（Text）⟶ 比特串（Bit string）（最好短，preferably short）。

- 书写（Writing）：文本（Text）⟵ 手势（Gesture）（最好简短，preferably brief）。



即：压缩是把文本变成一串尽量短的比特；书写是把一串尽量简短的手势（如鼠标轨迹）翻译回文本——两者互为逆过程，都可由同一个预测模型驱动。



### p.11 〔Dasher（Dasher 输入界面）〕



![l6-p11](fig/l6/mgp00011.png)



Dasher 软件界面截图：顶部为文本编辑框（已输出文本显示于右上角，呈浅色点线状，〔无法辨认〕）；主显示区为绿色背景、中央黄色大矩形，黑色十字准线位于中心，一条红色直线自准线指向右上方；字母 A–Z 沿右缘排成一列彩色矩形块（底部另有一个绿色小块与标点符号框），块的高度正比于当前语言模型给出的字符概率，随指针推进字母块向准线方向放大，指针进入哪个字母的方块即输出该字母。底部 Speed（速度）滑杆，示值 2.8。左下蓝色链接：www.inference.phy.cam.ac.uk/dasher/。



〔本页为软件截图型图示页〕



### p.12 〔Other uses for arithmetic coding（算术编码的其他用途）〕



![l6-p12](fig/l6/mgp00012.png)



内容与 p.10 相同（Dasher 标志；压缩：文本 ⟶ 比特串（最好短）；书写：文本 ⟵ 手势（最好简短）），本页追加一条：

- 随机样本的高效生成（Efficient generation of random samples）。



### p.13 〔The Marsaglia Random Number CDROM（Marsaglia 随机数光盘）〕



![l6-p13](fig/l6/mgp00013.png)



一张装在盒中的 CD 实物照片，盘面印字转录如下：THE MARSAGLIA RANDOM NUMBER CDROM including the DIEHARD BATTERY OF TESTS OF RANDOMNESS（Marsaglia 随机数光盘，附 Diehard 随机性测试套件）；Research Sponsored by THE NATIONAL SCIENCE FOUNDATION Grants DMS-8807976、DMS-9216972（研究由美国国家科学基金会资助，基金号 DMS-8807976、DMS-9216972）；DEPARTMENT OF STATISTICS and SUPERCOMPUTER COMPUTATIONS RESEARCH INSTITUTE（统计系与超级计算研究所）；© 1995 George Marsaglia All rights reserved；Professor George Marsaglia，geo@stat.fsu.edu；Florida State University（佛罗里达州立大学）。



〔本页为实物照片页〕



### p.14 〔Index of /pub/diehard/cdrom（/pub/diehard/cdrom 目录索引）〕



![l6-p14](fig/l6/mgp00014.png)



左侧重复 Marsaglia 光盘标签图（内容同 p.13），右侧为浏览器截图：目录页 Index of /pub/diehard/cdrom，表头 Name / Last modified / Size / Description，列出 Parent Directory 及 bits.01 至 bits.09（每文件 9.5M，修改日期均为 09-Dec-1995）。

页面下方文字：Marsaglia 随机数光盘（The Marsaglia Random Number CD-ROM）包含 50 亿（5 billion）个随机比特，分成 60 个 10 兆字节的文件。它由美国国家科学基金会基金 DMS-8807976 与 DMS-9206972 资助，在佛罗里达州立大学开发并发行。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页放「随机数光盘」，要立的是一把尺子：如果一段数据真的是随机 bit（比特），那它就压不动；反过来说，任何能把它压短的算法都证明了它不随机。这句话不是修辞，它有计数上的硬内容——随机的东西是少数，能压的东西是多数，而「压不动」的理由纯粹是短串不够多。
>
> 计数论证可以自己推。固定长度 $n$ 的 bit string（比特串）共 $2^n$ 条；要把一条压短，就要把它映到某条更短的 bit string（比特串）上并且能还原，所以压缩器必须是 injection（单射）。长度不超过 $n-k$ 的 bit string（比特串）总数是 $\sum_{j=0}^{n-k}2^j=2^{n-k+1}-1$，在 $2^n$ 里占的比例小于 $2^{1-k}$。取 $k=6$ 得到：能被压短 $6$ bit（比特）以上的串占比不到 $2^{-5}=3.125\%$。换句话说，随便取一条 $n$ 位的串，它有 $97\%$ 以上的把握压不动 $6$ bit（比特）——不是压缩算法不够好，是短串装不下这么多长串。这是「随机等于不可压」的第一性原理版本，也是 Kolmogorov complexity（柯尔莫哥洛夫复杂度）的直观起点：最短描述长度就是随机性的度量，它不可计算，所以工程上退回到用一批统计检验去尝试否定随机性。
>
> 检验的可算形式给一个。Diehard 套件里最基础的是 frequency test（频次检验）：$N=5\times 10^9$ 个独立等概率的 bit（比特），$1$ 的个数服从 binomial distribution（二项分布），期望 $N/2=2.5\times 10^9$，标准差 $\sqrt{N\cdot\frac12\cdot\frac12}=\frac12\sqrt{5\times 10^9}=\frac{70710.7}{2}=35355.3$。三倍标准差是 $106066$，相对偏差 $106066/(2.5\times 10^9)=4.2\times 10^{-5}$。也就是说，光盘上 $50$ 亿个 bit（比特）里 $1$ 的个数只要偏离期望超过约 $10.6$ 万个，就足以在 $99.7\%$ 的置信水平上被判为不随机。这个量级说明随机性为什么可以「验」：样本大到 $5\times 10^9$ 时，统计量对极小偏差也敏感；反过来，一张随机数光盘的价值不在于「看起来乱」，而在于它经受住了这么细的检验。
>
> 再给一个极端对照，让压缩比这个指标有意义。若把这 $50$ 亿个 bit（比特）换成全 $0$，任何压缩器都能压到几百字节，压缩比接近 $10^7:1$；随机光盘的最优压缩比则是 $1:1$。所以压缩比在两端都有内容：它既度量结构的有无，也给出随机性的操作定义。p.25 作业里那个 bent coin（弯币）文件 0010000…… 是这种对照的简化版——它的位频偏离 $1/2$ 不远，逐符号模型几乎压不动，会看模式的模型却能压，专门用来测「压缩器是不是只学了位频」。
>
> 跨课程连接两条。其一是 6.006 的随机化算法：randomized quicksort（随机化快速排序）的期望 $O(n\log n)$ 依赖 pivot（枢轴）均匀随机，而实际拿到的是 PRNG（pseudo-random number generator，伪随机数生成器）的输出，例如 Mersenne Twister（梅森旋转）的 MT19937 周期为 $2^{19937}-1$、内部状态是 $624$ 个 $32$ bit（比特）字。它通过大量统计检验，却是确定性的：把种子写下来就能还原整条流，因此它在信息意义上可压，而真随机 bit（比特）没有这样的短描述。这就是「统计上像随机」与「信息上不可压」的分野，恰好落在本讲两条主线的交汇点上。其二是 CSAPP 第 3 章的过程与栈：PRNG（pseudo-random number generator，伪随机数生成器）的状态就是一块内存，种子放在哪、谁读谁写，决定并行程序里的随机流会不会重复，这是「随机性是一种需要维护的资源」的工程版本。区别在抽象层次：CSAPP 关心状态落在哪个寄存器或栈槽，信息论关心这段状态能生成多少 bit（比特）的不可预测输出。
>
> 收束：p.15 到 p.18 的三张卡片问题展示的是另一端的失败——人脑对「看起来随机」的判断同样会出错，而修正它靠的还是同一套工具：写出完整的生成模型，再算概率。


### p.15 〔Three cards（三张卡片）〕



![l6-p15](fig/l6/mgp00015.png)



标题：Three cards（三张卡片）。页面几乎全白；右缘有三行被裁切的黄色小字，依稀可辨为 `white - 1〔无法辨认〕`、`brown - 2〔无法辨认〕`、`red - 3〔无法辨认〕`，应是对三张卡片的编号标注（卡片各面涂有白 white、棕 brown、红 red 三种颜色，具体每张卡片两面的配色在扫描中未显示）〔无法辨认〕。



### p.16 〔Three cards（三张卡片）〕



![l6-p16](fig/l6/mgp00016.png)



<span style="color:#2471a3;">**[example]**</span> 绿色 **Q**：你当前看到的一面是白色（white），那么另一面也是白色的概率是多少？



### p.17 〔Three cards（三张卡片）〕



![l6-p17](fig/l6/mgp00017.png)



绿色 **Q**：你当前看到的一面是棕色（brown），那么另一面也是棕色的概率是多少？



### p.18 〔Three cards（三张卡片）〕



![l6-p18](fig/l6/mgp00018.png)



绿色 **Q**：你当前看到的一面是红色（red），那么另一面也是红色的概率是多少？



### p.19 〔Communication over noisy channels（通过噪声信道的通信）〕



![l6-p19](fig/l6/mgp00019.png)



<span style="color:#2471a3;">**[section]**</span> 本讲新主题：噪声信道（Noisy channels）：

- 推断（inference）；

- 信息度量（information measures）。



右上小图：二元对称信道（binary symmetric channel）示意——输入 $x$（左侧红字 0、1），输出 $y$（右侧红字 0、1）；水平箭头标 $1-f$（不变），交叉箭头标 $f$（翻转）。

右下图：一个更复杂的信道图——左列字母 A–H、竖点省略号、Y、Z 以及符号 –，右列为同样的字母表，两列之间画出大量交叉箭头；其中 G 行的箭头最粗最密（G 几乎与所有输出相连），相邻的 F、H 也较强，其余字母箭头细疏——表示「几乎每个输入都可能被错传成任何输出」的强噪声信道。



### p.20 〔The rules - Three doors（游戏规则·三扇门）〕



![l6-p20](fig/l6/mgp00020.png)



手写页。右上角红字：The rules（规则）。左上画着三扇门，编号 1、2、3（门 1 被蓝绿色圆圈圈出；门 3 前有一个简笔小人，旁有一个字母记号〔无法辨认〕）。手写规则（品红笔为主）：

- 游戏节目主持人（gameshow host）把奖品藏在某扇门后。

- 主持人打开另一扇门，并承诺打开的门后没有奖品（promising the prize will not be revealed）。

- 参赛者选择 stick（坚持）或 switch（换门）（二字为红笔强调），即要么拿自己原门后的东西，要么拿另一扇仍关着的门后的东西。

- 参赛者先选择一扇门，例如门 1（"eg door 1" 为青绿笔）。



> <span style="color:#7f8c8d;">旁注：这是美国游戏节目式的「三扇门」场景；规则的每一条（主持人知情、必开一扇空门、绝不 reveal 奖品）都会影响下面的概率推断。</span>



### p.21 〔Q（问题：坚持还是换门？）〕



![l6-p21](fig/l6/mgp00021.png)



<span style="color:#2471a3;">**[example]**</span> 标题 **Q**。情境：

- 参赛者选择了门 1。

- 主持人打开门 3，如约什么也没露出来。

图中画有门 1、2、3：门 1 被青色圆圈圈出、下方红字 STICK?（坚持？）；门 2 下方红字 SWITCH?（换门？）；门 3 画成开着的样子。选项：

- A：应该坚持（should stick）；

- B：应该换门（should switch）；

- C：没区别（makes no difference）；

- Z：不知道（don't know）。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 三扇门的答案选 B（应当换门），但真正该记住的是机制：这道题里独立的随机性只有「奖品在哪扇门」这一处，其余全部由主持人的行为规则决定。所以 $2/3$ 不是普适真理，而是「主持人必须开一扇你没选的空门，且在两扇可选门之间等概率挑」这条规则下的后验。把规则换掉，答案就换掉——这是第一性原理层面的要点：Bayesian inference（贝叶斯推断）需要一个完整的 generative model（生成模型），prior（先验）只是它的一部分。
>
> 机制逐句展开。设选手选门 1、主持人开门 3。奖品位置有三条互斥假设，prior（先验）各 $1/3$。likelihood（似然）由规则给出：若奖品在门 1，主持人只能在门 2、门 3 里挑一扇空的，按等概率规则他开门 3 的概率是 $1/2$；若奖品在门 2，门 3 是唯一可开的空门，概率是 $1$；若奖品在门 3，他绝不可能开门 3（那会露出奖品），概率是 $0$。于是 $P(\text{门}1\mid\text{开}3)\propto\frac13\cdot\frac12=\frac16$，$P(\text{门}2\mid\text{开}3)\propto\frac13\cdot 1=\frac13$，$P(\text{门}3\mid\text{开}3)=0$；归一化（除以 $\frac16+\frac13=\frac12$）得 $\frac13,\frac23,0$。换门等于押「奖品不在门 1」，胜率 $2/3$。
>
> 换规则看答案怎么变，这一步不能省。规则改成「主持人总开编号最小的空门」：奖品在门 1 时他必开门 2，在门 2 时必开门 3，在门 3 时必开门 2。观察到「开门 3」时只可能是奖品在门 2，posterior（后验）是 $(0,1,0)$，换门胜率 $1$。规则再改成「主持人不知道奖品在哪、随机开门，恰好开到空门」：三种情形下开到门 3 的概率都是 $1/2$，posterior（后验）回到 $(1/3,1/3,1/3)$，换与不换都是 $1/2$。三种规则、三个答案（$2/3$、$1$、$1/2$），差别全部来自 likelihood（似然）表——这正是 p.20 那页「The rules（规则）」要逐条写清的原因：主持人是否知情、是否必开空门、在可选门之间怎么挑，每一条都改写 likelihood（似然）。
>
> 「极限情形检验」这个模板可以把结论变得显然。把 $3$ 扇门扩成 $100$ 扇：你选门 1，主持人按规则打开 $2$ 到 $99$ 号门中 $98$ 扇空的，只留门 $100$ 关着。你最初选中的概率是 $1/100$，而「奖品在我没选的 $99$ 扇里」的概率是 $99/100$；主持人开门不改变这 $99$ 扇的整体概率，只是把其中 $98$ 扇的概率全部搬到剩下那一扇上，所以换门胜率 $99/100$。一般结论是 $(N-1)/N$。直觉在 $N=3$ 时失灵，是因为 $2/3$ 与 $1/2$ 离得太近，人眼分不出「条件化之后的概率」与「剩下两个选项各一半」。
>
> 还有一个本课程特有的视角：主持人的开门是一条消息，可以量它的信息量。开门前的不确定性是 $\log_2 3=1.585$ bit（比特）；开门后的 posterior（后验）是 $(\frac13,\frac23)$，entropy（熵）$H_b(\frac13)=\frac13\log_2 3+\frac23\log_2\frac32=0.5283+0.3900=0.9183$ bit（比特），信息增益 $1.585-0.918=0.667$ bit（比特）。注意它严格小于 $1$ bit（比特）：主持人给出的确实是一个三选一的结果，但这个结果被规则扭曲了（他绝不会说「奖品在门 3」），所以 $1.585$ bit（比特）的不确定性消不干净。这与本讲后面 $I(X;Y)=H(X)-H(X\mid Y)$ 的记账方式完全一致：噪声信道里「收到 $y$ 之后 $x$ 还剩多少不确定性」就是这里的 $H(X\mid Y)$，而 Monty Hall 只是一个 $H(X\mid Y)=0.918$ bit（比特）的极小信道。
>
> 跨课程连接取 6.042J 的 three prisoners problem（三囚徒问题）：三个囚徒里有一个被赦免，狱警说出一个必被处死的人的名字，结构与 Monty Hall 完全相同——都是「一个知情者按规则透露部分信息，然后问后验」。区别在于：三囚徒只问 posterior（后验），Monty Hall 多了「选手可以在两个动作之间选择」这一层，于是 posterior（后验）直接变成决策（stick 与 switch 的期望收益比较）。第二个连接是概率论（Bertsekas）的 total probability formula（全概率公式）：把 $P(\text{开}3)$ 写成 $\sum_j P(\text{开}3\mid\text{门}j)P(\text{门}j)$，就是归一化那一步的一般形式；Bayes' formula（贝叶斯公式）把它反过来用，从「给定假设看数据」推到「给定数据看假设」。
>
> 收束回正文：p.21 的四个选项里 C（没区别）之所以诱人，是因为只更新了「剩余选项数」而没有更新「规则带来的 likelihood（似然）」；本讲接下来把同样的记账方式搬到噪声信道上，$P(y\mid x)$ 就是那里的规则表。


### p.22 〔Information measures（信息度量）〕



![l6-p22](fig/l6/mgp00022.png)



一排嵌套矩形框示意各信息度量的包含关系（「信息圆」图）：

- 最上层大框：$H(X,Y)$（联合熵 joint entropy）；

- 第二层框：$H(X)$（熵）；其下第三层右侧框：$H(Y)$；

- 最下层三框：$H(X \mid Y)$（条件熵 conditional entropy）、$I(X;Y)$（互信息 mutual information）、$H(Y \mid X)$（条件熵）。



直观读法：$H(X)$ 与 $H(Y)$ 是 $H(X,Y)$ 的两个「子块」，$I(X;Y)$ 是二者的「交叠」，$H(X\mid Y)$、$H(Y\mid X)$ 是各自的「独有部分」。



### p.23 〔Inference for channels（信道上的推断）〕



![l6-p23](fig/l6/mgp00023.png)



- 信道（channel）$Q$ 定义条件概率（conditional probabilities）$P(y \mid x)$。

- 若再选定一个输入分布（input distribution）$P(x)$，就得到联合分布（joint distribution）：

```math

P(x,y) = P(x)\, P(y \mid x)

```

- 有了联合分布，我们就可以做推断（inference）。



右侧为 p.19 的两张信道图（二元对称信道 $x\in\{0,1\}\to y\in\{0,1\}$，翻转概率 $f$、保持概率 $1-f$；以及 A–Z 字母信道，G 行箭头最粗最密）。



### p.24 〔Information measures for noisy channels（噪声信道的信息度量）〕



![l6-p24](fig/l6/mgp00024.png)



- 信道 $Q$ 定义条件概率 $P(y \mid x)$。

- 选定输入分布 $P(x)$，得联合分布 $P(x,y) = P(x)\,P(y \mid x)$。

- 对它我们可以计算互信息（mutual information）：

```math

I(X;Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X)

```

- 下方仍为 p.22 的嵌套框图：$H(X,Y)$；$H(X)$；$H(Y)$；$H(X\mid Y)$、$I(X;Y)$、$H(Y\mid X)$。

右侧为同前两张信道示意图。



> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> p.22 这张嵌套框图容易被当成记忆图，其实它只是两条恒等式的可视化，而这两条恒等式各有各的证明手法，都可以抽成模板复用。第一条是 chain rule（链式法则）$H(X,Y)=H(X)+H(Y\mid X)$，模板可以叫「先拆概率再拆对数」：把 joint entropy（联合熵）写成期望 $\mathbb{E}[\log_2\frac{1}{P(X,Y)}]$，用 $P(x,y)=P(x)P(y\mid x)$ 把倒数拆成两个因子相乘，对数随之变成两项之和，再由期望的线性性逐项求期望，就得到两个 entropy（熵）相加。凡是「联合量与边缘量」的关系都能照这三步走，$I(X;Y)=H(X)-H(X\mid Y)$ 只是把同一个式子移项。
>
> 第二条是 mutual information（互信息）的 KL（Kullback-Leibler divergence，相对熵）形式：$I(X;Y)=\sum_{x,y}P(x,y)\log_2\frac{P(x,y)}{P(x)P(y)}=D_{\mathrm{KL}}\big(P(x,y)\,\|\,P(x)P(y)\big)$。这个写法把互信息翻译成一句可操作的话：它度量 joint distribution（联合分布）与「边缘乘积」之间的距离，而边缘乘积恰好就是「$X$ 与 $Y$ 独立」的那个分布；于是「互信息为零」等价于「独立」，非负性也就是「距离非负」。证明用一步 Jensen's inequality（Jensen 不等式）：$\log$ 是凹函数（二阶导数为负，图像落在任意两点连线的上方），凹函数满足 $\mathbb{E}[\log Z]\le\log\mathbb{E}[Z]$；取 $Z=\frac{P(x)P(y)}{P(x,y)}$ 代入，得 $\sum_{x,y}P(x,y)\log\frac{P(x)P(y)}{P(x,y)}\le\log\sum_{x,y}P(x)P(y)=\log 1=0$，符号翻回来就是 $I\ge 0$。这个模板可以命名为「Jensen 一步法」：把待证的「某期望非负」写成 $\mathbb{E}[\log(\cdot)]$，用凹性换成 $\log\mathbb{E}[\cdot]$，再对期望项做归一化。
>
> 这里要对原注的一处说法做修正：把互信息说成「到独立集合的投影距离」在直觉上成立，但「投影」这个词在最小二乘里带着正交性，而 KL（相对熵）不对称（$D(P\|Q)\ne D(Q\|P)$），没有勾股定理可用，所以严格的说法只能是「在所有独立分布里使 KL（相对熵）最小的那一个」。这个最小化有闭式解：对 $Q(x,y)=q(x)q(y)$ 极小化，目标函数关于 $q(x)$ 与 $q(y)$ 可以分开处理，最优解正是边缘 $P_X$ 与 $P_Y$，最小值正是 $I(X;Y)$。用线性代数的语言说，把 $P(x,y)$ 看成一个矩阵，独立分布就是秩 $1$ 矩阵那一族，互信息是这个矩阵离秩 $1$ 族有多远——这个说法只需要矩阵秩与联合分布的定义，不需要更高级的几何工具。
>
> 用 BSC（binary symmetric channel，二元对称信道）把这套恒等式变成可算的数字。信道给的是 $P(y\mid x)$：以概率 $f$ 翻转、以 $1-f$ 保持。给定 $x$，$Y$ 的不确定性就是 $H_b(f)$，所以 $H(Y\mid X)=H_b(f)$ 与输入分布无关；于是 $I(X;Y)=H(Y)-H_b(f)$，要最大化它只需最大化 $H(Y)$，而二元分布的最大 entropy（熵）是 $1$ bit（比特），在 $P(X=0)=1/2$ 时取到。所以 channel capacity（信道容量）$C=1-H_b(f)$ bit（比特）/信道使用。代数字：$f=0.1$ 时 $H_b(0.1)=0.1\times 3.3219+0.9\times 0.1520=0.3322+0.1368=0.4690$，$C=0.531$ bit（比特）；$f=0.11$ 时 $H_b(0.11)=0.11\times 3.1844+0.89\times 0.1681=0.3503+0.1496=0.4999$，$C=0.500$ bit（比特）。翻转概率只涨 $0.01$，容量掉了 $0.031$ bit（比特），与导数 $-\log_2\frac{1-f}{f}=-3.016$ 乘 $0.01$ 得到的 $0.030$ 对得上，可以互相验算；$f=0.11$ 时容量约等于 $1/2$，意味着平均每两次信道使用才能可靠送出 $1$ bit（比特）。再看两端：$f=0.5$ 时 $C=0$，$f=0$ 时 $C=1$。
>
> 输入分布不最优时代价多少，也能算。取 $f=0.11$、$P(X=0)=0.7$，则 $P(Y=1)=0.7\times 0.11+0.3\times 0.89=0.077+0.267=0.344$，$H(Y)=H_b(0.344)=0.344\times 1.5406+0.656\times 0.6074=0.5300+0.3984=0.9284$ bit（比特），故 $I=0.9284-0.4999=0.4285$ bit（比特），比 channel capacity（信道容量）$0.500$ 少 $0.0715$ bit（比特）。对 BSC（binary symmetric channel，二元对称信道）而言这个损失可以用 $P(X=0)=\frac12$ 完全避免，这正是「channel capacity（信道容量）是对输入分布取最大值」这个定义的实际含义，也说明容量是信道本身的属性，而不是某一组 $(P(X),P(y\mid x))$ 的属性。
>
> 跨课程连接有三处，区别都要讲清。其一，6.042J 的容斥原理 $|A\cap B|=|A|+|B|-|A\cup B|$ 与 $I=H(X)+H(Y)-H(X,Y)$ 形状完全一样，但容斥是集合基数的恒等式，不需要任何凸性；信息论的这条式子要靠概率结构才得到「非负」这个结论——容斥不给非负性，$I\ge 0$ 是新信息。其二，Strang 的最小二乘投影与这里「在独立分布族里找 KL（相对熵）最近点」同形：独立分布是秩 $1$ 矩阵族，最近点就是边缘乘积。区别在距离：最小二乘用平方距离，误差与子空间正交、有勾股定理；KL（相对熵）不对称，没有正交分解，只能说「最小化」而不能说「投影」。其三，概率论（Bertsekas）里独立性的定义是 $P(x,y)=P(x)P(y)$，是一个是或否的判定；mutual information（互信息）把这个定义量化成偏离量，两个随机变量「弱相关」从此有了具体数值。
>
> 收束回正文：$I(X;Y)$ 对输入分布取最大值得到 channel capacity（信道容量），p.24 只给了定义；channel coding theorem（信道编码定理）要证明这个上界可达，那是下一讲的内容。


### p.25 〔Recommended homework（推荐作业）〕



![l6-p25](fig/l6/mgp00025.png)



- 阅读（Reading）：第 1–6 章；预习（Advance reading）：第 8、9、10 章。

- 更多推荐习题见网站上的 handout 2（讲义 2）（蓝字链接）。

  - Huffman 程序 `huffman.p`、`huffman.py` 已挂在网站上（红字标出文件名）。

  - 另有一个「弯币（bent coin）」文件 0010000……作为压缩基准（compression benchmark）。
