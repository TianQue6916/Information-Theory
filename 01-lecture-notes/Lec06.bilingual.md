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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题的答案是 A。随机抽一个比特等价于两步试验：先按 $\mathcal{P}_X$ 抽一个符号，再在它的码字内均匀抽一位，于是 $p_1$ 就是「码字中含 1 的比例」按长度加权的期望：$p_1=\frac12\cdot 0+\frac14\cdot\frac12+\frac18\cdot\frac23+\frac18\cdot 1=\frac13<\frac12$。注意它并不等于 $1/2$：符号码只对「符号」这一层最优，并不保证输出的比特流是均匀随机的。这正是概率论中「期望 = 取值按概率加权平均」的直接应用——信息量 $\log(1/p_i)$ 本身也是一个随机变量，它的期望就是熵。对熟悉 CSAPP 二进制表示的同学，可以把码字看成变长位串：位串的统计结构里仍带着信源的剩余结构，而这种统计结构随后（第 19 页起）会在噪声信道里被再次利用。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $H(X)\le L < H(X)+1$ 里的「+1」是符号码逐符号编码的固有代价：每个符号必须分派整数个比特，最坏的符号要向上取整，平均摊到每符号至多多 1 比特。「identical twins（同卵双胞胎）」是 MacKay 的课堂比喻：把相邻两个符号绑成一对再编码，取整损失由两个符号分摊，每符号开销降到约 $1/2$ 比特；推广到 $N$ 个符号一组，开销 $O(1)/N$ 趋于零——这正是信源编码定理的思路，其证明依赖概率论的大数定律与渐近均分性（AEP）：长度 $N$ 的典型序列（typical set）约有 $2^{NH(X)}$ 个，故每符号 $H(X)$ 比特足矣。Strang 线代课中「典型子空间」的投影几何是同一件事的连续版本。本讲的算术编码就是把「成组编码」推到极限的实用算法。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 不等式 $l(\mathbf{x})\le\log_2\frac{1}{P(\mathbf{x})}+2$ 是算术编码的核心保证：整条消息的码长不超过其理想信息量加 2 比特。与符号码「每符号最多亏 1 比特」对比：逐符号的 Huffman 编码无论文件多长都要为取整付每符号级的代价，而算术编码把全部开销封顶在 2 比特，摊到每符号是 $2/N$，当 $N\to\infty$ 时消失，因此能逼近熵率——这正是信源编码定理所承诺的。「+2」来自最终区间端点的二进制表示与截断。要真正逼近该界，前提是有一台好的预测器 $P$（如下文 PPM）：模型 $P$ 越贴近真实分布，$\log_2\frac{1}{P(\mathbf{x})}$ 越接近真实熵。这把数据压缩干净地分解为「概率建模 + 算术编码」两件事，是现代通用压缩器的框架。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 六元语法（six-gram）模型把 $P(x_t\mid x_1\ldots x_{t-1})$ 近似为只依赖前 5 个字符的条件频率，五行示例都是在 `_` 处给出补全。用频率当概率是频率学派的标准操作，大数定律保证当同一上下文出现足够多次时频率收敛于真实概率；但上下文越长、样本越稀疏，估计越不可靠——很多 5 字上下文在语料里只见过一两次。工程上常用哈希表存 n-gram 计数：以字符串为键、计数为值，正是 6.006 中「哈希与均匀随机」一章的用武之地。图中的彩色字母只是把整个预测分布可视化的一种方式，压缩器实际会把这份分布交给算术编码使用。上下文稀疏化问题正是下一页 PPM「多长度上下文混合」的动机。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 为什么讲座要专门放一页「随机比特光盘」？因为在压缩、密码学与仿真中，「真正随机」是一个可检验的统计断言：Marsaglia 的 Diehard 套件对光盘上 50 亿比特做大量检验（频次、游程、间隔、扑克检验等），任何隐藏规律都会让某项检验报警。信息论视角下，最随机的序列就是熵最大的序列，它应当不可被任何压缩器压短——这为「压缩即发现结构」提供了极端对照基准。对算法课同学：6.006/CLRS 里随机化算法与哈希所假设的均匀随机位，在现实中由确定性种子驱动的伪随机数生成器（PRNG）近似产生，只有统计意义上的随机。下一页起的三张卡片问题，则展示「看似随机」如何欺骗人类直觉。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这就是著名的 Monty Hall（三门）问题，正确答案是 B：应当换门。用贝叶斯推断的语言写：奖品在门 1/2/3 的先验（prior）各为 $1/3$；「主持人必开一扇无奖且非你所选的门」这一规则决定似然（likelihood）：若奖品在门 1，主持人开 3 的概率是 $1/2$；若奖品在门 2，他必开 3，概率为 $1$。观察到「开了门 3」后，由贝叶斯公式得后验（posterior）$P(1)\propto\frac13\cdot\frac12=\frac16$、$P(2)\propto\frac13\cdot 1=\frac13$，归一化后换门中奖概率 $2/3$。直觉错误多源于忽略「主持人的行为携带信息」——他绝不打开有奖的门。这与 6.042 条件概率一节的三囚徒、三卡片等悖论同源：更新信念必须使用完整的环境条件模型。

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本页框图常被称作「信息圆」：$H(X,Y)$ 是全集，$H(X)$、$H(Y)$ 是两个子集，$I(X;Y)$ 是交集，$H(X\mid Y)$、$H(Y\mid X)$ 是各自独有部分。恒等式 $I(X;Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)$ 与 6.042 集合论里 $|A\cap B|=|A|+|B|-|A\cup B|$ 的容斥思想同构。更现代的写法是 $I(X;Y)=D_{\mathrm{KL}}\big(P(x,y)\,\|\,P(x)P(y)\big)$：它度量联合分布偏离「独立假设」的程度，非负性可由 KL 散度的凸性结合 Jensen 不等式证明——Strang 课中「散度=到独立流形的投影距离」是同一思想的几何化。对固定信道，噪声越大互信息越小；把它对输入分布取最大值就得到信道容量（channel capacity），随后的信道编码定理将证明该值可达。

### p.25 〔Recommended homework（推荐作业）〕

![l6-p25](fig/l6/mgp00025.png)

- 阅读（Reading）：第 1–6 章；预习（Advance reading）：第 8、9、10 章。
- 更多推荐习题见网站上的 handout 2（讲义 2）（蓝字链接）。
  - Huffman 程序 `huffman.p`、`huffman.py` 已挂在网站上（红字标出文件名）。
  - 另有一个「弯币（bent coin）」文件 0010000……作为压缩基准（compression benchmark）。
