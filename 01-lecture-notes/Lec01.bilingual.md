> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l1 · 行内双语视觉转录版 · 原图见 fig/l1/</span>

### p.1 〔Information theory, pattern recognition, and neural networks — Lecture 1: Introduction to Information Theory（信息论、模式识别与神经网络——第 1 讲：信息论导论）〕

![l1-p1](fig/l1/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 本页是课程标题页。页面右侧紫色大字为课程名 Information Theory, Pattern Recognition, and Neural Networks（信息论、模式识别与神经网络），其下黑色粗体为本次讲座标题：Lecture 1: Introduction to Information Theory（第 1 讲：信息论导论）。页面左侧是一幅圆形装饰图案：绿色圆形与方形节点自中心层层分叉、彼此连线，构成网络状分形结构，圆周边缘环绕着粉色与蓝色的小图形——即 MacKay 教材封面上的标志性图案。

### p.2 〔Lecture notes - Chapter 1（课程讲义——第 1 章）〕

![l1-p2](fig/l1/mgp00002.png)

<span style="color:#2471a3;">**[note]**</span>（课程与教材信息）页面左侧展示教材封面：作者 David J. C. MacKay，书名 Information Theory, Inference, and Learning Algorithms（《信息论、推断与学习算法》），青绿色封面带草叶状装饰图案。右侧三条要点：由 Cambridge University Press（剑桥大学出版社）出版；全书 640 pages（640 页），售价约 ~ 35 pounds（35 英镑）；也可 free online（免费在线）获取（红色强调）。页面底部以蓝色等宽字体给出网址：www.inference.phy.cam.ac.uk/mackay/itila/。

### p.3 〔This lecture uses the blackboard（本讲使用黑板）〕

![l1-p3](fig/l1/mgp00003.png)

<span style="color:#2471a3;">**[note]**</span>（过场提示）整页为纯黑背景，仅顶部居中一行红色文字：This lecture uses the blackboard（本讲使用黑板）。意为本讲的主体推演将在黑板上进行，幻灯片只作辅助；黑板上的具体推导内容不包含在本扫描件中。〔本页为纯文字提示页，无其他图形内容〕

### p.4 〔Redundant glass & noisy channel, f = 0.1（"冗余的玻璃杯"与噪声信道，f = 0.1）〕

![l1-p4](fig/l1/mgp00004.png)

<span style="color:#2471a3;">**[example]**</span>（含噪信道演示）页面为三联图。左：一幅 Dilbert 风格漫画，人物举着一只玻璃杯，气泡中写着 REDUNDANT GLASS.（"冗余的玻璃杯"；图中尾字母被气泡边缘裁去）。中：二元对称信道示意图——上行箭头 $0 \to 0$ 标注 $(1-f)$；两条交叉箭头 $0 \to 1$ 与 $1 \to 0$ 共同标注 $f$；下行箭头 $1 \to 1$ 标注 $(1-f)$。右：同一幅漫画经过该信道后的版本——每个像素以概率 $f$ 被翻转成黑白噪点，画面与文字均被侵蚀，气泡文字已难以辨认〔无法辨认〕。页面底部红色大字：$f = 0.1$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张信道图在概率论里就是一个条件概率表：给定输入 $x$，输出 $y=x$ 的概率是 $1-f$，$y=1-x$ 的概率是 $f$，这正是你在 Bertsekas 概率课里学过的条件概率与条件分布的具体化，MacKay 后续会把它写成信道矩阵 $P(y\mid x)$。从 CSAPP 的视角看，磁盘上的每个比特就是 0/1 位，信道噪声无非是"某些位被意外取反"，即位翻转（bit flip）；红字 $f=0.1$ 意味着平均每 10 位就错 1 位，对裸数据是灾难性的。左侧漫画本身就是双关：一只"多余/备份"的玻璃杯，对应右半幅被噪点糟蹋得面目全非的图像，直观展示了不加冗余时信息的脆弱。请记住这幅三联图，本讲接下来所有编码方案都要在这条信道上接受检验。

### p.5 〔Q: How many bits are flipped?（问：有多少位被翻转？）〕

![l1-p5](fig/l1/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span>（问题 1）顶部三联图与上一页相同：漫画原图、二元对称信道示意图、被噪点污染的漫画。下方以绿色 Q 引出问题（红色数字）：A file of $N = 10\,000$ bits is stored on this disc drive (with $f = 0.1$), then read. Roughly how many bits are flipped?（一个 $N=10\,000$ 位的文件存入这块磁盘（$f=0.1$），然后读出，大约有多少位被翻转？）问题下方画了两个绿色空心矩形框，中间夹一个 ± 号，供填写「大约值 ± 波动范围」。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把每个比特的翻转看作一次伯努利试验，$N=10\,000$ 个独立比特的翻转总数服从二项分布：期望 $Nf=1000$，方差 $Nf(1-f)=900$，标准差约 $30$。所以答案是「约 $1000$ ± $30$」——幻灯片上两个空框夹一个 ± 号，正是要你按「期望 ± 标准差」作答。这是你在概率课（Bertsekas）里期望与方差计算的直接应用；大数定律保证当 $N$ 很大时，实际翻转比例会高度集中在 $f$ 附近。进一步看，标准差与期望之比约为 $\sqrt{Nf(1-f)}/(Nf)\approx 3\%$，即相对涨落按 $1/\sqrt{N}$ 收缩——$N$ 越大，「平均每 10 位错 1 位」就越从统计涨落变成铁定的确定值。这个"大量独立试验涨落被平均掉"的图像，整门课还会反复出现。

### p.6 〔Q: How small does f need to be?（问：f 需要多小？）〕

![l1-p6](fig/l1/mgp00006.png)

<span style="color:#2471a3;">**[example]**</span>（问题 2）顶部三联图同前（漫画原图、二元对称信道示意图、受噪漫画）。下方绿色 Q（$f$ 为红色）：To make a successful business selling 1 Gigabyte disc drives, how small does the flip probability $f$ need to be?（要想靠出售 1 Gigabyte（1 吉字节）磁盘驱动器做成一门成功的生意，翻转概率（flip probability）$f$ 需要多小？）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 直觉上的"生意成功"标准是整块盘读写几乎不出错，即期望错误位数 $Nf \ll 1$；1 GB 约含 $8\times 10^9$ 个比特，于是需要 $f \lesssim 10^{-10}$ 量级。这解释了为什么工业界要为磁盘设定极苛刻的误码率指标：靠把物理信道本身做到近乎完美，代价会随可靠度要求急剧上升。Shannon 接下来要展示的思路正相反——接受一个便宜的、$f$ 并不小的物理信道，在其上用编码人为添加冗余（redundancy），把有效错误率压到任意低。这是本讲乃至整门课的核心转折点：从"消灭噪声"转向"与噪声共处"。带着这个问题看下一页的重复码，你会更体会到最后那张容量图的分量。

### p.7 〔Repetition code 'R3'（重复码 'R3'）〕

![l1-p7](fig/l1/mgp00007.png)

<span style="color:#2471a3;">**[section]**</span> 标题行：Repetition code 'R3'（重复码 R3）。页面主体是一张三阶段流程图，各阶段上方标注记号：源图 s —— ENCODER（编码器）→ 传输图 t —— CHANNEL（信道），$f = 10\%$ → 接收图 r。具体地：s 是那幅 REDUNDANT GLASS 漫画原图；编码器把它原样重复 3 份、纵向叠放得到 t（三份完全相同的漫画）；信道对每一份独立施加翻转概率 10% 的像素噪声，得到三份噪点各不相同的受损副本 r。这就是重复码（repetition code）R3：每个比特连发 3 次。

### p.8 〔Repetition code 'R3'（重复码 'R3'：含译码器）〕

![l1-p8](fig/l1/mgp00008.png)

<span style="color:#2471a3;">**[section]**</span> 标题同上页：Repetition code 'R3'（重复码 R3）。流程图扩为四段：s —— ENCODER（编码器）→ t —— CHANNEL（信道），$f = 10\%$ → r —— DECODER（译码器）→ $\hat s$。前三段与上页一致：一幅漫画、三份重复副本、三份各自带噪点的副本。译码器将三份受损副本逐位对照，输出估计图 $\hat s$（读作 "s hat"，即译码器对 s 的最佳猜测）：一幅基本恢复干净、仅在气泡边缘残留少量噪点的漫画。译码规则即多数表决（majority vote）：同一位置三票中取多数。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 译码器这里用的是逐位多数表决：三份副本中同一位置至少有两份相同就采信谁。在独立性假设下，表决后的单比特错误率是"至少错两份"的概率 $P=\binom{3}{2}f^2(1-f)+f^3=3f^2-2f^3$，代入 $f=0.1$ 得约 $0.028$——这正是下一页图中 R3 那个点的来历。注意代价：码率（rate）从 1 降到 $1/3$，同样一张图要花三倍空间，可靠性与效率的权衡从第一个编码就登场了。概率课里的独立性（independence）在这里是关键假设：若三份副本的噪声彼此相关（例如同一道划痕划过同一位置），表决的好处会大打折扣，这也提示"重复时应打乱位置/交错存放"的直觉。

### p.9 〔Performance of repetition codes（重复码的性能）〕

![l1-p9](fig/l1/mgp00009.png)

<span style="color:#2471a3;">**[section]**</span> 标题：Performance of repetition codes（重复码的性能）。左右两张散点图共享横轴 Rate（码率，0 到 1）：左图纵轴为线性刻度，从 0 到 0.1（步长 0.02）；右图纵轴为对数刻度，记作 $p_{\mathrm b}$（比特错误率），刻度自 1e-15 到 0.1。图中的方块点标注为：R1 位于右上角码率 1、错误率 0.1 处（不编码，错误率就是信道本身的 $f$）；R3 位于码率约 $1/3$ 处、错误率约 0.03；R5 位于码率 $1/5$，更靠左下；R61（连发 61 次）几乎贴着纵轴，右图中其点已落到 $10^{-15}$ 附近的图底。一条虚线自 R61 经 R5、R3 连向 R1；另有一条带箭头的斜线指向右下方，标注 more useful codes（更有用的码）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这两张图是本讲的第一个核心图像：横轴 Rate（码率，信息比特占传输比特的比例），纵轴是比特错误率；R1（不编码）在右上角，R3、R5、R61 沿虚线滑向左下角——越重复越可靠，但码率越趋近 0，右图对数纵轴显示 R61 能把错误率压到 $10^{-15}$ 以下。这与你在 6.006/CLRS 里见过的比较排序下界论证精神相同：先用一个简单的计数/信息论论证划出"任何方案都逃不掉的界"，再看具体算法离界有多远。重复码就是那个"离界很远"的朴素算法。图中指向右下的箭头 more useful codes 预告存在既快又可靠的编码；请把「右上不行、左下太慢」这个困局记住，它正是 Shannon 定理要一举解决的。

### p.10 〔What's achievable?（究竟什么是可达的？）〕

![l1-p10](fig/l1/mgp00010.png)

<span style="color:#2471a3;">**[section]**</span> 无标题续页：两张图与上页完全同轴、同布局（左线性、右对数，横轴 Rate，右图纵轴 $p_{\mathrm b}$），但在重复码的方块点之外，新加入一批以 + 号标出的真实编码方案的数据点，标注有：H(7,4)（即 (7,4) 汉明码（Hamming code））、BCH(31,16)、BCH(15,7)、BCH(511,76)、BCH(1023,101)（BCH 码一族，括号内为「码长, 信息位数」）。这些 + 点大多位于重复码虚线的右上方：同等错误率下码率明显更高，但距「高码率又零错误」的理想角仍远。页面底部一行红色大字：What's achievable?（究竟什么才是可达的？）

### p.11 〔Shannon's noisy-channel coding theorem（Shannon 噪声信道编码定理）〕

![l1-p11](fig/l1/mgp00011.png)

<span style="color:#2471a3;">**[theorem]**</span> 标题：Shannon's noisy-channel coding theorem（Shannon 噪声信道编码定理）。两张图沿用前页的坐标与数据点（方块为重复码 R1/R3/R5/R61，+ 为 H(7,4) 与各 BCH 码），并新增一条实线分界曲线：曲线左下方区域标注 achievable（可达），右上方标注 not achievable（不可达）；分界曲线与横轴的交点标注 $C$，即该信道的信道容量（channel capacity）。左图（线性坐标）中分界线自 $C$（约 0.5）升向右上角的 R1 点；右图（对数坐标）中分界曲线在 $C$ 之后近乎竖直跌落至图底——码率一旦越过 $C$，错误率便无从谈起。图下两行红色公式给出容量表达式：

```math
C_{\text{BSC}}(f) = 1 - H_2(f)
```

```math
H_2(f) = f \log_2 \frac{1}{f} + (1-f) \log_2 \frac{1}{1-f}
```

即：二元对称信道的容量 $C_{\text{BSC}}(f)$ 等于 1 减去二元熵（binary entropy）$H_2(f)$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 红字公式给出二元对称信道的信道容量 $C_{\text{BSC}}(f)=1-H_2(f)$：$f=0$（无噪声）时 $C=1$，每比特能传 1 比特信息；$f=1/2$（输出与输入完全无关）时 $H_2=1$、$C=0$，信道彻底报废；$f$ 接近 1 时容量又回到 1（把输出全部取反即可）。图中分界曲线的交点即 $C$：Shannon 噪声信道编码定理断言，只要码率小于 $C$，就存在错误率可任意小的码；一旦超过 $C$，无论怎么编码都不可能可靠。$H_2$ 的凹性与"熵不超过 1"这类不等式，可以用你在 Strang 线代课上学过的凸函数图像与 Jensen 论证来严格化（KL 散度非负性同理）。曲线在 $C$ 处近乎竖直跌落，意味着"差一点到容量"与"刚超容量"是天壤之别。

### p.12 〔Lecture notes - Chapter 1（课程讲义——第 1 章：阅读任务）〕

![l1-p12](fig/l1/mgp00012.png)

<span style="color:#2471a3;">**[note]**</span>（课程信息：阅读任务）教材信息页再次出现：左侧为 Information Theory, Inference, and Learning Algorithms 封面图。右侧要点：由 Cambridge University Press（剑桥大学出版社）出版；640 pages, ~ 35 pounds（640 页，约 35 英镑）；Also available free online（也可免费在线获取，红色强调）；新增一条要点：Reading: Chapter 2（课前阅读：第 2 章）。页面底部蓝色等宽字体网址：www.inference.phy.cam.ac.uk/itprnn/。

### p.13 〔Course outline（课程大纲）〕

![l1-p13](fig/l1/mgp00013.png)

<span style="color:#2471a3;">**[section]**</span> 标题：Course outline（课程大纲）。左侧仍为教材封面。右侧两级要点列表：

- Information Theory（信息论）
  - Source coding (Data compression)（信源编码，即数据压缩）
  - Noisy-channel coding（噪声信道编码）
- Data modelling, pattern recognition, learning & memory（数据建模、模式识别、学习与记忆）
  - Tools（工具）
    - Exact inference methods（精确推断方法）
    - Monte Carlo methods（蒙特卡罗方法）
    - Variational methods（变分方法）
  - Neural networks（神经网络）

页面底部蓝色等宽字体网址：www.inference.phy.cam.ac.uk/itprnn/。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这份大纲其实是两条主线：前半程的信息论关心"信息有多少、怎么压、怎么在噪声里可靠地传"，后半程的推断关心"给定数据如何反推模型"。贯穿两者的骨架是贝叶斯推断（Bayesian inference）：写下先验（prior）与似然（likelihood），用乘法与归一化得到后验（posterior），分母上的证据（evidence）则衡量一个模型的解释力。大纲列出的三类工具——精确推断、Monte Carlo 方法、变分方法——本质上都是在算同一个后验：小模型可以精确求和；高维时用随机采样近似；再不行就用可优化的代理分布去逼近。你刚在概率课里学过的期望与条件分布，马上都会变成这些算法里的基本操作。

### p.14 〔The weighing problem（称球问题）〕

![l1-p14](fig/l1/mgp00014.png)

<span style="color:#2471a3;">**[example]**</span>（称球问题）页面上方是一幅红色线条画的天平：横梁向右倾斜，左盘翘起、右盘下沉，两个盘中各放 2 个青绿色小球（示意一次 2 对 2 的称量），底座旁的地面另散放 8 个小球，合计 12 只。正文：You are given 12 balls, all equal in weight except for one that is either heavier or lighter.（给你 12 只球，除了一只球的重量或偏重或偏轻外，其余全部等重。）Design a strategy to determine which is the odd ball and whether it is heavier or lighter, in as few uses of the balance as possible.（请设计一种策略，判定哪一只是异常球（odd ball）、它偏重还是偏轻，并且尽可能少地使用天平。）其中连词 and 为绿色强调，in as few uses of the balance as possible 为红色强调。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道称球题是下一讲的信息论热身。先做计数：异常球有 12 种选择，偏重或偏轻 2 种可能，共 $12\times 2=24$ 种情形；一次称量只有左沉、右沉、平衡 3 种结果，$k$ 次称量的决策树至多有 $3^k$ 片叶子，故至少需要 $\lceil\log_3 24\rceil=3$ 次才可能区分所有情形。这与你熟悉的比较排序下界（6.006/CLRS 的决策树论证，$\log_2(n!)$ 次比较）是同一招，只是每次称量的"分支因子"是 3 而不是 2。换成信息的语言：每次称量至多提供 $\log_2 3$ 比特信息，而问题本身带有约 $\log_2 24$ 比特的不确定性。至于 3 次是否真能做到（还要小心"判定不出异常"的边界情形），留给你自己推演——这正是信息论"先数一数"威力的第一次实战。

### p.15 〔Lecture notes - Chapter 1（课程讲义——第 1 章：购书信息）〕

![l1-p15](fig/l1/mgp00015.png)

<span style="color:#2471a3;">**[note]**</span>（课程信息：购书方式）教材信息页（收尾版）最后一次出现：左侧为 Information Theory, Inference, and Learning Algorithms 封面图。右侧要点：由 Cambridge University Press（剑桥大学出版社）出版；640 pages, 35-40 pounds（640 页，35–40 英镑）；28-32 pounds at CUP bookshop（在 CUP 书店购价为 28–32 英镑）；borrow from me (24 pounds deposit)（可向授课人借阅，押金 24 英镑，绿色强调）；Also available free online（也可免费在线获取，红色强调）；间隔之后一条：Reading: Chapter 2（课前阅读：第 2 章）。页面底部蓝色等宽字体网址：www.inference.phy.cam.ac.uk/itprnn/。
