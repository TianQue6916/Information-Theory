> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l4 · 行内双语视觉转录版 · 原图见 fig/l4/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l4-p1](fig/l4/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程标题页：**Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）**。左侧是一幅由绿、蓝、品红色圆圈与方块组成的分形网络装饰图。

课程议程（当前讲的分支以绿色圆点高亮）：

- 1 Noisy-channel coding（噪声信道编码）
- **Source coding (Data compression)（信源编码（数据压缩））**——绿色圆点高亮，即本讲主题
  - 2 Information content, entropy（信息量、熵）
  - 3 Typicality and the source coding theorem（典型性与信源编码定理）
  - 4 Symbol codes（符号码）

页底网址：www.inference.phy.cam.ac.uk/itprnn/

### p.2 〔How to compress a redundant file?（如何压缩一个冗余文件？）〕

![l4-p2](fig/l4/mgp00002.png)

<span style="color:#2471a3;">**[example]**</span> 页面主体是一大块 0/1 比特串（共 12 行、合计约 1000 比特；其中 1 十分稀疏，绝大多数位置是 0，1 呈零星散布）〔比特串不逐位转录〕。

底部打印体说明：e.g., $N = 1000$ tosses of a bent coin with $p_1 = 0.1$（例如：掷一枚 bent coin（弯曲硬币）$N=1000$ 次，出现 1 的概率 $p_1=0.1$）。

### p.3 〔How to measure information content?（如何度量信息量？）〕

![l4-p3](fig/l4/mgp00003.png)

<span style="color:#2471a3;">**[definition]**</span> Claims:（断言：）

1. 某个 outcome（结果）的 Shannon information content（Shannon 信息量）

   $h(x=a_i) = \log_2 \dfrac{1}{P(x=a_i)}$

   是信息量的一种合理度量（a sensible measure of information content）。

2. entropy（熵）

   $H(X) = \sum_x P(x) \log_2 \dfrac{1}{P(x)}$

   是期望信息量（expected information content）的一种合理度量。

3. Source coding theorem（信源编码定理）——来自信源（source）$X$ 的 $N$ 个结果可以被压缩进大约 $NH(X)$ 个比特。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这三条"断言"其实是一条自底向上的主线：先给单个结果定义 self information（自信息）$h(x)=\log_2 1/p(x)$，再按分布取期望就得到熵。从你熟悉的概率论（Bertsekas）视角看，熵毫不神秘——它就是随机变量 $h(x)$ 的期望 $H(X)=E[h(x)]$，正如 $E[X]$ 由分布唯一决定一样。于是"期望"的语言可以直接搬过来：后面用大数定律讨论 $\frac{1}{N}\log \frac{1}{p(x_1\cdots x_N)}$ 收敛到 $H(X)$（即渐近均分性 AEP），套路与"样本均值收敛到期望"完全相同。对数取 2 为底使单位是比特，这与 CSAPP 里"信息由 0/1 串承载"的视角天然衔接：$N$ 个符号的理论压缩极限 $NH(X)$，恰是"给典型串编号需要多少个二进制位"。还要注意 $h$ 的取值随 $p$ 指数变化、波动很大，这正是后面"典型集"方法要处理的对象。

### p.4 〔Source coding theorem（信源编码定理——典型集证明思路）〕

![l4-p4](fig/l4/mgp00004.png)

<span style="color:#2471a3;">**[theorem]**</span> （接上页第 3 条）Source coding theorem（信源编码定理）——来自信源 $X$ 的 $N$ 个结果可以被压缩进大约 $NH(X)$ 个比特。

证明思路：Proved by counting the typical set（通过数一数 typical set（典型集）的大小来证明）。

方框内容：当信源 $X$ 产生 $N$ 个独立的结果

$\mathbf{x} = x_1 x_2 \ldots x_N$

时，这个串极有可能属于约 $2^{NH(X)}$ 个 typical（典型）结果之一，而其中每一个结果的概率都约为 $2^{-NH(X)}$。

### p.5 〔Example: the bent coin（例子：弯曲硬币）〕

![l4-p5](fig/l4/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span> 与 p.2 相同的那一大块 0/1 比特串整页再次展示（12 行、约 1000 比特，1 稀疏分布）〔比特串不逐位转录〕。本页除标题外无其他文字。

### p.6 〔How we won the bent coin lottery（我们是这样赢下"弯曲硬币彩票"的）〕

![l4-p6](fig/l4/mgp00006.png)

<span style="color:#2471a3;">**[example]**</span> 右上角打印体注记：Probability of '1' = f（"1" 出现的概率 = $f$）。

打印体正文：To have a 99.99% chance of winning, we bought all the **typical** tickets（为了有 99.99% 的中奖把握，我们买下了所有 typical（典型）的彩票）。

手绘图示：一个红色线条画出的彩票摇号罐（大瓮），罐中散落着许多浅青色空白小票；其中两张深蓝色小票上写着成串的 0/1（即 0、1 兼有、比例接近 $f$ 的串），一只黑色空心箭头从右侧的手写注释指向这两张"典型票"。

手写注释（蓝色 + 绿色笔迹）：Number of tickets in 'typical set'（"典型集"里的票数）

$|T| \simeq 2^{N H_2(f)}$

（公式右上另有一处小"+"记号，〔无法辨认〕其含义，按 $2^{NH_2(f)}$ 转录。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页把典型集（typical set）思想演成"买彩票"：把每个长度为 $N$ 的 0/1 串看作一张彩票，只要买下全部"典型票"，就能以 99.99% 的概率覆盖源的真实输出。背后的引擎是大数定律：掷 $N$ 次正面概率为 $f$ 的硬币，1 的个数以高概率落在 $Nf$ 附近，这样的串约有 $\binom{N}{Nf}\simeq 2^{NH_2(f)}$ 张，其中 $H_2(f)=-f\log_2 f-(1-f)\log_2(1-f)$ 就是手写公式里的二元熵。每张典型票被抽中的概率约为 $2^{-NH_2(f)}$，"张数 × 每张概率"约为 1——这正是渐近均分性（AEP）的雏形。用 Strang 线代的语言类比：整个 $2^N$ 大小的串空间里，概率质量集中在一个维数只有约 $NH_2(f)$ 的"典型子空间"附近，压缩的本质就是给这个低维子空间里的元素编号。对 $N=1000$、$f=0.1$ 算一下：$H_2(0.1)\approx 0.469$ 比特，故只需约 469 比特而非 1000 比特就能存下这份文件。

### p.7 〔Example: the bent coin（例子：弯曲硬币——典型窗口有多宽？）〕

![l4-p7](fig/l4/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 上半页：与 p.2/p.5 相同的 0/1 比特串（12 行、约 1000 比特）〔不逐位转录〕。

下半页左侧：一张高斯分布密度曲线图（黑底）：横轴从 $-4$ 到 $4$（以 $\sigma$ 为单位），纵轴从 $0$ 到 $0.4$，峰位于 $0$ 处、高约 $0.4$；曲线下方 $1\sigma$ 到 $2\sigma$ 区间为橙色阴影，$2\sigma$ 以右为黄色阴影。

下半页右侧文字：Gaussian distribution（高斯分布）：

- $P(x > 1\sigma)$ = 16%
- $P(x > 2\sigma)$ = 2.3%
- $P(x > 2.3\sigma)$ = 1%
- $P(x > 3\sigma)$ = 0.13%

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本页回答 p.6 的 99.99% 从何而来：典型不是一个精确的位置，而是一个宽度为若干 σ 的窗口。$N$ 次掷币中 1 的个数近似服从均值为 $Nf$、方差为 $Nf(1-f)$ 的正态分布（二项分布的正态近似，是概率课的标准内容），图中给出高斯尾部的常用数值：1σ 之外 16%、2σ 之外 2.3%、2.3σ 之外 1%、3σ 之外 0.13%。因此把"1 的个数在 $Nf\pm 2.3\sigma$ 之内"的串都算作典型票，漏票概率就压到 1% 量级；想再往下降，把窗口放宽到 3σ 之外也只多 0.13%，代价几乎不变。这种"集合稍放宽、失败概率快速下降"的权衡，正是后面信道编码定理中错误概率随块长增大而衰减的直觉来源。

### p.8 〔How to compress a redundant file, practically?（如何"在实际操作上"压缩一个冗余文件？）〕

![l4-p8](fig/l4/mgp00008.png)

页首标题下方以红色大字强调：practically?（"实际操作上"呢？）。其下再次展示同一份 0/1 比特串（12 行、约 1000 比特，1 稀疏）〔不逐位转录〕。本页除标题、红色问句与比特串外无其他内容。

### p.9 〔Symbol codes（符号码）〕

![l4-p9](fig/l4/mgp00009.png)

<span style="color:#2471a3;">**[section]**</span> 小节标题页，正文空白：Symbol codes（符号码）——从本页起进入"实用压缩"部分。

### p.10 〔《Emma》开篇选段（无幻灯片标题）〕

![l4-p10](fig/l4/mgp00010.png)

页面为浅黄底、打字机字体的英文段落，即 Jane Austen 小说《Emma（爱玛）》的开篇（作为英文文本压缩的示例语料）。行内双语转录（原文末行在 "very" 处截断）：

爱玛·伍德豪斯（Emma Woodhouse），俊俏、聪明、富有，有一个舒适的家和开朗的天性，仿佛把人间几样最大的福气聚于一身；她已在世上生活了近二十一年，极少有什么事能让她苦恼或烦心。她是一位最慈爱、最纵容的父亲两个女儿中最小的一个；由于姐姐出嫁，她很小就成了父亲家里的女主人。母亲去世得太早，她对母亲的抚爱只剩模糊的记忆；母亲的空位由一位极好的家庭女教师（governess）填补，论慈爱几乎不亚于一位母亲。Taylor 小姐在伍德豪斯家已经待了十六年，与其说是家庭教师，不如说是朋友，非常……（原文在此截断）

### p.11 〔英文 27 符号的频率表（无幻灯片标题）〕

![l4-p11](fig/l4/mgp00011.png)

<span style="color:#2471a3;">**[example]**</span> 左侧为一张三列表格：$i$（编号）、$a_i$（符号）、$p_i$（概率），覆盖 26 个小写字母与空格（表中以 "–" 表示；即对《Emma》一类英文文本统计出的符号频率）：

| $i$ | $a_i$ | $p_i$ |
|----|-------|-------|
| 1 | a | 0.0575 |
| 2 | b | 0.0128 |
| 3 | c | 0.0263 |
| 4 | d | 0.0285 |
| 5 | e | 0.0913 |
| 6 | f | 0.0173 |
| 7 | g | 0.0133 |
| 8 | h | 0.0313 |
| 9 | i | 0.0599 |
| 10 | j | 0.0006 |
| 11 | k | 0.0084 |
| 12 | l | 0.0335 |
| 13 | m | 0.0235 |
| 14 | n | 0.0596 |
| 15 | o | 0.0689 |
| 16 | p | 0.0192 |
| 17 | q | 0.0008 |
| 18 | r | 0.0508 |
| 19 | s | 0.0567 |
| 20 | t | 0.0706 |
| 21 | u | 0.0334 |
| 22 | v | 0.0069 |
| 23 | w | 0.0119 |
| 24 | x | 0.0073 |
| 25 | y | 0.0164 |
| 26 | z | 0.0007 |
| 27 | –（空格） | 0.1928 |

右侧：一条黑色竖带上画着 27 个白色方块，每个符号对应一个，方块面积与 $p_i$ 成正比——空格与 e 的方块最大，j、q、z 只剩小点。〔本页为纯统计图表页〕

### p.12 〔上表 27 符号的一个符号码（哈夫曼编码码表）〕

![l4-p12](fig/l4/mgp00012.png)

<span style="color:#2471a3;">**[example]**</span> 左侧同样给出 $i$、$a_i$、$p_i$ 三列（同 p.11），随后是符号与黑带方块图，最右为一个黑底白字的码字（codeword）列。完整码表（符号 → 码字）如下：

| $i$ | $a_i$ | $p_i$ | 码字 |
|----|-------|-------|------|
| 1 | a | 0.0575 | 0000 |
| 2 | b | 0.0128 | 0010000 |
| 3 | c | 0.0263 | 00101 |
| 4 | d | 0.0285 | 10000 |
| 5 | e | 0.0913 | 1100 |
| 6 | f | 0.0173 | 111000 |
| 7 | g | 0.0133 | 001001 |
| 8 | h | 0.0313 | 10001 |
| 9 | i | 0.0599 | 1001 |
| 10 | j | 0.0006 | 1101000000 |
| 11 | k | 0.0084 | 1010000 |
| 12 | l | 0.0335 | 11101 |
| 13 | m | 0.0235 | 110101 |
| 14 | n | 0.0596 | 0001 |
| 15 | o | 0.0689 | 1011 |
| 16 | p | 0.0192 | 111001 |
| 17 | q | 0.0008 | 1101000001 |
| 18 | r | 0.0508 | 11011 |
| 19 | s | 0.0567 | 0011 |
| 20 | t | 0.0706 | 1111 |
| 21 | u | 0.0334 | 10101 |
| 22 | v | 0.0069 | 11010001 |
| 23 | w | 0.0119 | 1101001 |
| 24 | x | 0.0073 | 1010001 |
| 25 | y | 0.0164 | 101001 |
| 26 | z | 0.0007 | 11010000001 |
| 27 | –（空格） | 0.1928 | 01 |

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这两页是本讲唯一"真刀真枪"的实例：语料取自 Jane Austen 的《Emma》（p.10），统计出 27 个符号的频率——空格以 0.1928 高居榜首，e 以 0.0913 领先所有字母，而 j、q、z 都在 0.001 以下。把高频符号配短码、低频符号配长码，就得到这张码表（p.28 将说明这就是最优的哈夫曼编码）。关键性质是 prefix code（前缀码）：任何码字都不是另一个码字的前缀，因此译码器从左到右逐位扫描，一旦匹配即可立即输出，无需分隔符或回溯——用 CSAPP 里移位、掩码一类的位运算就能高效实现。直观感受"高频配短码"的划算之处：空格的码字 01 只花 2 比特却承载约 0.19 的概率质量，而 z 要花 11 个比特也只占 0.0007，两者在总预算里各得其所。

### p.13 〔What we want from a symbol code:（我们想从符号码得到什么？）〕

![l4-p13](fig/l4/mgp00013.png)

三条要求：

- Guaranteed to be **uniquely decodeable**（保证可唯一译码（uniquely decodeable））——绿色高亮；
- Easy to decode（易于译码）；
- Small expected length（期望码字长度（expected codeword length）要小）。

### p.14 〔The symbol-code supermarket（符号码超市）〕

![l4-p14](fig/l4/mgp00014.png)

本页只有标题 The symbol-code supermarket（符号码超市），正文空白（为动画序列的首帧）。

> <span style="color:#7f8c8d;">旁注：p.15–p.26 为同一标题下的逐步动画帧，逐页只多出高亮或新增栏目。</span>

### p.15 〔The symbol-code supermarket（符号码超市：全部候选码字）〕

![l4-p15](fig/l4/mgp00015.png)

一张嵌套表格（等价于一棵深度为 4 的完整二叉树）：最左列把所有二进制串按首位分成 0 与 1 两大块；第二层为 00、01、10、11（2 位串）；第三层为 000、001、010、011、100、101、110、111（3 位串）；最右层为 0000、0001、……、1111（16 个 4 位串）。〔本页为纯图示页，无其他文字〕

### p.16 〔The symbol-code supermarket（超市选购演示一：四个 4 位码字）〕

![l4-p16](fig/l4/mgp00016.png)

在 p.15 的表格上，以红色圆角框圈出四个 4 位串：0001、0010、0100、1000（即"买下"这四个码字）。其余部分无变化，无其他文字。

### p.17 〔The symbol-code supermarket（超市选购演示二：再买四个 2 位码字）〕

![l4-p17](fig/l4/mgp00017.png)

在 p.16 的基础上，另以粉红色圆角框圈出四个 2 位串：00、01、10、11；四个 4 位码字（0001、0010、0100、1000）的红框仍在。本页无其他文字。

### p.18 〔The symbol-code supermarket（超市选购演示三：链状码字 1、01、001、0001）〕

![l4-p18](fig/l4/mgp00018.png)

改以青色粗框圈出一组新的码字：1、01、001、0001——它们排成一条"逐位添 0"的链；右列中 0001 处被青框覆盖（原红框），0010、0100、1000 的红框仍在。本页无其他文字。

### p.19 〔The symbol-code supermarket（超市选购演示四：1、00、10、010）〕

![l4-p19](fig/l4/mgp00019.png)

以紫色实心填充标出码字 1、00、10、010；01、11 改为浅粉描边（未选购的弱化样式）；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

### p.20 〔The symbol-code supermarket（超市选购演示五：1、01、000、001）〕

![l4-p20](fig/l4/mgp00020.png)

以蓝色粗框圈出码字 1、01、000、001；00、10、11 为浅粉描边；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

### p.21 〔The symbol-code supermarket（超市选购演示六：1、10、100、000）〕

![l4-p21](fig/l4/mgp00021.png)

以绿色实心填充标出码字 1、10、100、000；00、01、11 为浅粉描边；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

### p.22 〔The symbol-code supermarket（符号码超市：引入"总预算"）〕

![l4-p22](fig/l4/mgp00022.png)

同一张二叉树表格，本页无任何高亮；表格右侧新增一个竖排文字的窄框：The total symbol code budget（符号码总预算）——为把 Kraft 不等式讲成"预算约束"做铺垫。

### p.23 〔The symbol-code supermarket（预算视图下的选购三：1、01、001、0001）〕

![l4-p23](fig/l4/mgp00023.png)

p.18 的青色选购（1、01、001、0001，其中 0001 为青框覆盖）在右侧带"总预算"框的版式中重放；0010、0100、1000 的红框仍在。本页无其他文字。

### p.24 〔The symbol-code supermarket（预算视图下的选购四：1、00、10、010）〕

![l4-p24](fig/l4/mgp00024.png)

p.19 的紫色选购（1、00、10、010）在带"总预算"框的版式中重放；01、11 为浅粉描边；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

### p.25 〔The symbol-code supermarket（预算视图下的选购五：1、01、000、001）〕

![l4-p25](fig/l4/mgp00025.png)

p.20 的蓝色选购（1、01、000、001）在带"总预算"框的版式中重放；00、10、11 为浅粉描边；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

### p.26 〔The symbol-code supermarket（预算视图下的选购六：1、10、100、000）〕

![l4-p26](fig/l4/mgp00026.png)

p.21 的绿色选购（1、10、100、000）在带"总预算"框的版式中重放；00、01、11 为浅粉描边；红框的 0001、0010、0100、1000 仍可见。本页无其他文字。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这十二页动画值得连起来看：超市把长度为 $l$ 的码字定价 $2^{-l}$，右侧"总预算"恒为 1，这正是 Kraft 不等式 $\sum_i 2^{-l_i}\le 1$ 的具象化。四轮"购物篮"各有玄机：{1, 01, 001, 0001} 与 {1, 01, 000, 001} 中任何码字都不是别的码字的前缀，是合法的前缀码；而 {1, 00, 10, 010} 里 1 是 10 的前缀，歧义立现——串 1010 既能译成 (1, 010) 也能译成 (10, 10)；{1, 10, 100, 000} 同样因 1 前缀于 10、10 前缀于 100 出歧义，例如串 100000 既可译成 (1, 000, 000) 又可译成 (100, 000)。可见"不超预算"只是必要条件，"互不为前缀"才是可直接安全译码的设计；反过来，只要一组长度满足 Kraft 不等式，就总能重新构造出前缀码。这与 6.006 中 trie（前缀树）的管理规则同构：一个叶子被占用后，其全部祖先结点就不能再作叶子——超市里"花钱"买下的正是树上一整条路径。

### p.27 〔Gibbs inequality（吉布斯不等式）〕

![l4-p27](fig/l4/mgp00027.png)

<span style="color:#2471a3;">**[theorem]**</span>

```math
\sum_i p_i \log \frac{p_i}{q_i} \ge 0
```

[equality only if **q** = **p**]（[仅当 $\mathbf{q} = \mathbf{p}$ 时取等号]）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这就是相对熵 / KL 散度（KL divergence）的非负性，也叫 Gibbs 不等式，取等当且仅当两个分布相同。证明只需要 log 的凹性与 Jensen 不等式：$\sum_i p_i\log(q_i/p_i)\le \log\bigl(\sum_i p_i\cdot\frac{q_i}{p_i}\bigr)=\log\sum_i q_i\le \log 1=0$，两边取负即得结论。你在 Strang 线代里积累的凸性直觉在这里完全兑现：KL 散度像一种"距离"，但不对称、也不满足三角不等式，本质是由凸性保证的散度而非度量。它是信息论几乎所有"下界"的发动机：本讲的信源编码定理、后面的信道容量，以及最大熵原理导出 Gibbs/Boltzmann 分布，全靠这一条不等式。顺带一提，取 q 为均匀分布时它退化为 $H\le \log_2|\mathcal{A}|$，即"熵不超过字母表大小的对数"。

### p.28 〔Symbol code summary（符号码小结）〕

![l4-p28](fig/l4/mgp00028.png)

- unique decodeability（唯一可译性）——requires（要求）

  ```math
  \sum_i 2^{-l_i} \le 1
  ```

  这就是 Kraft inequality（Kraft 不等式）；[if equality holds, the code is 'complete']（[若取等号，则称该码是"完备的"（complete）]）。

- prefix codes（前缀码）▸ and binary trees（以及二叉树）。

- whenever a code achieved L=H, it had codelengths $l_i^*$ equal to the information contents（凡达到 $L=H$ 的码，其码长 $l_i^*$ 都恰等于信息量）：

  ```math
  l_i^* = \log \frac{1}{p_i}
  ```

- optimal symbol codes（最优符号码）：The optimal symbol code's expected length $L$ satisfies（最优符号码的期望长度 $L$ 满足）

  ```math
  H(X) \le L < H(X) + 1
  ```

- Huffman algorithm（Huffman 算法）。

页边右侧有三幅手绘小二叉树：第一棵叶子标为 0、10、110、111；第二棵叶子标为 00、01、10、11；第三棵可见叶标 0 与 101，其余小字〔无法辨认〕。

### p.29 〔Results stated without proof (see Chapter 5)（未经证明而陈述的结果（见教材第 5 章））〕

![l4-p29](fig/l4/mgp00029.png)

- Kraft inequality（Kraft 不等式）：$\sum_i 2^{-l_i} \le 1$
- Gibbs inequality（吉布斯不等式）：$\sum_i p_i \log \dfrac{p_i}{q_i} \ge 0$
- Right hand side of the symbol-code source coding theorem（符号码版信源编码定理的右半段）：$H(X) \le L(C,X) < H(X)+1$（图上 $L(C,X)$ 上方画有一个大括号强调）。
- Huffman coding is optimal（哈夫曼编码是最优的）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把 $H(X)\le L(C,X)\lt H(X)+1$ 读作"逐符号编码时，每符号平均至多多付 1 比特"。直觉来自最优码长 $l_i^*=\log_2(1/p_i)$ 往上取整：$\lceil \log_2 1/p_i\rceil$ 与理想值至多差 1，而 Kraft 不等式保证这样一组取整长度确实能实现成前缀码。这 1 比特的固定损失正是后面算术编码（arithmetic coding）的动机——把许多符号连成一整块一起编码后，每符号的摊销损失趋于零，压缩率逼近 $H$。另一个方向的类比是 6.006/CLRS 里比较排序的 Ω(n log n) 下界：决策树需要 $n!$ 片叶子、深度至少 $\log_2 n!$，与"给 $2^{NH}$ 张典型票编号至少要 $NH$ 比特"是同一套计数论证。看到这里应当体会到：信息论的下界从不玄妙，就是"给多少对象编号至少要多少位"的数数。

### p.30 〔Project（课程课题与阅读任务）〕

![l4-p30](fig/l4/mgp00030.png)

Project:（课题：）为一个源文件发明 compressor（压缩器）与 uncompressor（解压器）：文件长 $N = 10{,}000$ 比特，每一位以 $f = 0.01$ 的概率为 1。实现它们和/或估计你的方法效果如何。

- Other recommended exercises: 5.22, 5.26, 5.27（其他推荐习题：教材习题 5.22、5.26、5.27）
- Reading: Chapters 1, 2, 4, 5.（阅读：第 1、2、4、5 章）
- Advance reading: Chapters 8, 9, 10（预习：第 8、9、10 章）

右侧为教材封面缩略图（David J. C. MacKay, Information Theory, Inference, and Learning Algorithms）。底部两行：Information Theory, Inference, and Learning Algorithms — Cambridge University Press (2003). Available free online（《信息论、推断与学习算法》，剑桥大学出版社 2003 年版，可在网上免费获取）。
