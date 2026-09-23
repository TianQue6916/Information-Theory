> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l11 · 行内双语视觉转录版 · 原图见 fig/l11/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l11-p1](fig/l11/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程标题页。左侧仍是那幅圆形分形树装饰图：绿色树干与分支自圆心向外生长，末梢挂着蓝、粉两色的小圆圈并向圆盘边缘递归细分〔本页左侧为纯手绘图示〕。右侧课程大纲（outline，大纲）：

- 1 噪声信道编码（Noisy-channel coding）
- <span style="color:#2471a3;">**[section]**</span> 信源编码（Source coding），即数据压缩（Data compression）：
  - 2 信息量（Information content）与熵（entropy）
  - 3 典型性（Typicality）与信源编码定理（source coding theorem）
  - 4 符号码（Symbol codes）
  - 5 符号码与算术编码（Arithmetic coding）
- <span style="color:#2471a3;">**[section]**</span> 噪声信道编码（Noisy-channel coding）：
  - 6 噪声信道的信息度量（Information measures for noisy channels）
  - 7 噪声信道的容量（Capacity of a noisy channel）
  - 8 噪声信道编码定理（The noisy-channel coding theorem）
- <span style="color:#2471a3;">**[section]**</span> 推断与概率方法（Inference + probabilistic methods）：
  - 9–10 推断（Inference）
  - 11 聚类（Clustering）
  - 12–13 蒙特卡罗方法（Monte Carlo methods）
  - 14 变分方法（Variational methods）

页底两行网址：www.inference.phy.cam.ac.uk/itprnn/ 与 www.inference.phy.cam.ac.uk/itila/

### p.2 〔The course（课程与教材）〕

![l11-p2](fig/l11/mgp00002.png)

- 课程（The course）：www.inference.phy.cam.ac.uk/itprnn/
- 页面右侧是教材封面：作者 David J. C. MacKay，书名 Information Theory, Inference, and Learning Algorithms（信息论、推断与学习算法），Cambridge（剑桥大学出版社）出版；封面为青绿色调的草地图案，散布紫红色小屋与浅色小树。
- 教材（The book）：www.inference.phy.cam.ac.uk/itila/

### p.3 〔Monte Carlo methods（蒙特卡罗方法）〕

![l11-p3](fig/l11/mgp00003.png)

<span style="color:#2471a3;">**[lecture]**</span> 本讲方法总览，分四大板块：

- <span style="color:#2471a3;">**[section]**</span> 简单蒙特卡罗方法（Simple Monte Carlo methods）：
  - 重要性采样（Importance sampling）
  - 拒绝采样（Rejection sampling）
- <span style="color:#2471a3;">**[section]**</span> 马尔可夫链蒙特卡罗方法（Markov-chain Monte Carlo methods）：
  - Metropolis 方法（Metropolis method）
  - Gibbs 采样（Gibbs sampling）
  - 切片采样（Slice sampling）
- <span style="color:#2471a3;">**[section]**</span> 减少随机游走行为（Reducing random-walk behaviour）：
  - 哈密顿蒙特卡罗（Hamiltonian Monte Carlo）
  - 过松弛（Overrelaxation）
- <span style="color:#2471a3;">**[section]**</span> 精确采样（Exact sampling）

页面左下有一行黄色小字：`itp/exactmc RUNME`〔图上小字，目录名拼写无法完全确认〕。

右栏是三幅黑底 gnuplot 演示图：

- 右上：标题 estimate of ⟨φ⟩（$\phi$ 的估计值），横轴 number of samples（样本数）0–50，纵轴 0–3；品红色曲线从约 2 骤降、小幅振荡后稳定在 1 附近——展示估计量随样本数收敛。
- 右中：图例 $P(x)$〔?〕（红）、phi(x)（绿）、Q(x)（青）；红色双峰曲线（左峰约 3、右峰较矮）、绿色单峰宽曲线（峰约 2）、青色近直线上升；图底部有一排黄色短竖线，标记采样落点；横轴刻度 0–50。
- 右下：标题 50 samples, 19 accepted（50 个样本，接受 19 个），图例 $P(x)$〔?〕（红）、Q(x)（绿）、rejected（拒绝，灰 ×）、accepted（接受，青点）；红色双峰外罩绿色宽包络，灰色 × 多落在两峰之间的低概率区，青色点集中在峰附近；横轴 −4 到 4，纵轴 0–4。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 蒙特卡罗（Monte Carlo）方法的根基就是你在概率论里学过的大数定律：想算期望 $E[\phi(x)]$，就抽 $N$ 个样本用平均 $\frac{1}{N}\sum_i\phi(x_i)$ 来估，右上小图的品红曲线正是这个估计随样本数增加而收敛的过程（锚点：概率论·期望与大数定律）。重要性采样（importance sampling）换一个好抽的分布 $Q$ 抽样，再按权重 $P(x)/Q(x)$ 加权修正，估计仍无偏，但权重方差可能爆炸；拒绝采样（rejection sampling）则要求 $Q$ 处处罩住 $P$，按面积比接受——右下图标题"50 samples, 19 accepted"就是说接受率不到四成。两者在高维时会同时失效：维数一高，$Q$ 很难既好抽又贴合 $P$，这正是中栏转向马尔可夫链蒙特卡罗（MCMC）的动机。类比 6.006 里"期望运行时间"的分析方式，你会发现蒙特卡罗同样是在跟"样本数 × 单样本代价"做预算权衡。

### p.4 〔Lecture 11 / 12 / 13（第 11–13 讲的主题安排）〕

![l11-p4](fig/l11/mgp00004.png)

- Lecture 11（第 11 讲）：Clustering（聚类）
- Lecture 12（第 12 讲）：Monte Carlo methods（蒙特卡罗方法）
- Lecture 13（第 13 讲）：Advanced Monte Carlo methods（高级蒙特卡罗方法）

### p.5 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l11-p5](fig/l11/mgp00005.png)

图：黑底散点图，横轴刻度 $1$ 到 $20$，纵轴无标注，青色小点左密右疏。

题目正文：一个源（source）发射粒子；粒子衰减（decay）的位置服从以长度尺度（lengthscale）$\lambda$ 为参数的指数分布（exponential distribution）。只有当位置落在窗口（window）$(x_{\min},x_{\max})=(a,b)=(1,20)$ 内时，衰减才能被观测到。观测到 $N$ 次衰减，位置为 $\{x_1,\ldots,x_N\}$。问：$\lambda$ 是多少？

绿色补充提问：+ 若这个分布其实是两个指数分布的混合（mixture of two exponentials），又当如何？（+ What about the possibility that the distribution is a mixture of two exponentials?）

### p.6 〔maximum likelihood distribution（最大似然分布——双指数混合推断演示图）〕

![l11-p6](fig/l11/mgp00006.png)

本页是一幅黑底 gnuplot 演示截图（无统一页面标题），共五块子图：

- 左上：标题 maximum likelihood distribution（最大似然分布）；纵轴 0–0.6；一条绿色曲线从约 0.6 快速指数式衰减至 0，曲线上叠有若干青色 × 号（数据点）；其下文字 ML model with two tau's（带两个 τ 的最大似然模型），横轴刻度被遮挡〔无法辨认〕。
- 左中：纵轴 0–1（间隔 0.2）、横轴 0–16；绿色与紫色两条快速衰减曲线，左端有青色 × 点；此图无可见标题〔无法辨认〕。
- 左下：标题 Posterior distribution of the labels（标签的后验分布）；纵轴 0–0.25、横轴 0–300；散布绿色空心方点，多数贴近 0，少数跳到 0.07–0.22。
- 右上：黄色网格 3D 曲面，标题 P(Data|tau1, tau2, c1..cN = 00000111)（固定标签串时的数据似然 $P(\mathrm{Data}\mid\tau_1,\tau_2,c_{1..N})$）；竖轴刻度自 0 至 4.5e-05；两个水平轴（$\tau$ 方向）刻度均为 −5 到 5；曲面整体平坦，仅一角隆起一个尖峰。
- 中部一行文字：Marginal likelihood of tau1 and tau2 – P(Data|tau1,tau2)（$\tau_1,\tau_2$ 的边缘似然）。
- 右下：橙红色网格 3D 曲面；竖轴刻度 .0003、.00025、.0002、.00015、.0001、5e-05、0；两水平轴刻度 −5 到 5；平坦底座上并立两个尖峰。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页演示把上一页"双指数混合"问题做成了数值实验：右上黄色曲面是固定标签串 $c_{1..N}=00000111$ 时的似然 $P(\mathrm{Data}\mid\tau_1,\tau_2,\mathbf{c})$，右下橙色曲面是把标签边缘化（对全部 $2^N$ 种分配求和）后的边缘似然（marginal likelihood）$P(\mathrm{Data}\mid\tau_1,\tau_2)$——注意两图纵轴量级不同（4.5e-05 对 3e-04），且橙面峰形更宽，这正是"对隐变量求和摊薄了证据"的直观体现（锚点：概率论·全概率公式与边缘化）。左下"标签的后验分布"图中每个方点对应一个数据点的归属概率，绝大多数点几乎确定地属于某一簇。边缘似然是贝叶斯模型比较的通用货币：谁给数据更高的 $P(\mathrm{Data}\mid\mathrm{model})$ 谁胜出，而它自带奥卡姆剃刀——更灵活的模型会把概率质量摊到更大的参数空间上而受罚。这个 $2^N$ 求和在精确计算不可行时就要靠 MCMC 或变分近似，本讲后续内容都是为它服务的。

### p.7 〔Q（问题）〕

![l11-p7](fig/l11/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 一个信道（channel）有二元输入（binary input）$x\in\{1,2\}$ 与实值输出（real output）$y$：

$P(x=1)=\pi_1$

```math
P(y\mid x)=\frac{1}{\sqrt{2\pi\sigma^2}}\;e^{-\frac{(y-m_x)^2}{2\sigma^2}}
```

你观测到 $y$，问 $x$ 是什么？（You see $y$. What is $x$?）

试把 $P(x=1\mid y)$ 写成如下形式（Write $P(x=1\mid y)$ in the form）：

```math
P(x=1\mid y)=\frac{1}{1+\exp\left(-\,\text{something elegant}\right)}
```

（something elegant，即"某个优雅的量"。）

右侧小插图：黑底图中两条钟形曲线，橙色为 P(y|x=1)（中心 $m1$）、绿色为 P(y|x=2)（中心 $m2$），横轴标注 $m1$、$m2$，两峰部分重叠。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题的"优雅答案"值得当场推一遍：把 $P(y\mid x=1)\pi_1$ 与 $P(y\mid x=2)(1-\pi_1)$ 代入 Bayes 定理，分子分母同除分子，得 $P(x=1\mid y)=\frac{1}{1+\exp(-a)}$，其中 $a=\log\frac{\pi_1}{1-\pi_1}+\frac{(y-m_2)^2-(y-m_1)^2}{2\sigma^2}$ 是 $y$ 的线性（仿射）函数——展开平方差时 $y^2$ 项恰好抵消（锚点：概率论·贝叶斯推断与对数似然比）。这个 $a$ 叫对数几率（log-odds），S 型函数（sigmoid）把整条实轴压进 $(0,1)$，它正是后来逻辑回归与神经网络 sigmoid 单元的源头。从信道视角看，这是"离散输入＋连续高斯噪声输出"的信道，两个均值 $m_1,m_2$ 相距越远、方差 $\sigma^2$ 越小，可传递的信息越多——这为噪声信道容量一讲埋下伏笔。判决规则也很直观：$a>0$ 判 1，先验均衡时等价于 $y$ 离 $m_1$ 更近。

### p.8 〔Clustering（聚类）〕

![l11-p8](fig/l11/mgp00008.png)

本页是两块谱图（spectrogram）阵列加两幅放大样例：左右各一组 3 列 × 4 行共 12 幅小谱图（合计 24 幅），每幅横轴 Time (s)（时间）0–0.5、纵轴 Frequency (kHz)（频率）0–6，彩虹配色表示能量（红＝强、蓝＝弱）；多数谱图底部有横向红色条带（低频强能量），部分条带呈斜向弯曲的轨迹。下方居中是两幅放大谱图：左幅旁有红色大字 One（"一"），右幅旁有绿色大字 Zero（"零"）——它们是人朗读数字 "one" 与 "zero" 的语谱图。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 谱图（spectrogram）是"时间 × 频率"的二维能量图，由短时傅里叶变换得到：把信号切窗、逐窗做频谱，颜色编码能量强弱。图中元音部分表现为几条平行的深红水平条带（共振峰 formant），辅音与音渡则呈斜向轨迹，这就是为什么同一个人两次读 "one" 的谱图肉眼可见地相似，而 "one" 与 "zero" 截然不同。聚类（clustering）的设定由此引入：我们手里没有"这是哪个词"的标签，只有 24 个样本及其相似性，要让算法自动把 24 幅谱图分成自然的组（锚点：6.006·聚类与无监督学习）。工程上先要把每幅二维谱图压成一个特征向量（比如取若干频带的平均能量），聚类结果高度依赖这个表示的选择——这也是"特征工程/表示学习"与聚类算法本身耦合的原因。语音识别、说话人分离等应用都从这里起步。

### p.9 〔Clustering（聚类）〕

![l11-p9](fig/l11/mgp00009.png)

本页是一幅黑底散点图，图内顶部标注 K means clustering（K 均值聚类），横纵轴刻度均为 0–10。四团数据点各成一簇：左下是白色 ×（约在 $(2,2.5)$ 一带）；中部偏左是绿色 +（约在 $(3,5)$ 一带）；右上是蓝色小方块（约在 $(7,7.5)$ 一带，其中有离群点）；右中是橙色小菱形（约在 $(7.5,4)$ 一带）。每簇中心画有一个带同色圆圈的星号（表示迭代收敛后的簇中心 mean），数据点整体围绕各自中心分布。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 图中是 K 均值（K-means）收敛后的状态：白 ×、绿 +、蓝方块、橙菱形四团点各归其簇，四个带圈星号是学到的中心，右上方那个偏远的蓝点也被划给了蓝色簇——它的归属对中心位置影响很大。算法只有两步循环：分配（Assign）把每个点划给最近中心，相当于按 Voronoi 图切分平面；更新（Update）把每个中心移到本簇点的均值——均值正是最小化簇内平方距离和的解，这与 Strang 线代里"最小二乘投影"是同一件事（锚点：Strang·投影与最小二乘）。目标函数（簇内平方误差和）随迭代单调不增，故算法必收敛，但只收敛到局部最优：初始化不同，结果可能不同，实践中要多次重启取最优（6.006 里分析的正是这类迭代启发式的保证边界）。图中星号即"质心（centroid）"，硬分配下它就是簇内点的算术平均。

### p.10 〔Clustering（聚类）〕

![l11-p10](fig/l11/mgp00010.png)

- <span style="color:#2471a3;">**[section]**</span> K 均值聚类（K means clustering）：
  - 分配（Assign）
  - 更新（Update）
- <span style="color:#2471a3;">**[section]**</span> 软 K 均值聚类（Soft K means clustering）：
  - 分配（Assign）
  - 更新（Update）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 软 K 均值与硬 K 均值只在"分配"一步不同：不再把点硬判给唯一中心，而是计算责任（responsibility）$r_{ik}=P(c_i=k\mid x_i)$——用 Bayes 公式把"到各中心的距离"翻译成概率并归一化，形式上与上一页 Q 题的后验完全同构（锚点：概率论·后验概率与归一化）。更新（Update）步随之改为加权平均：每个新中心是全体点按 $r_{ik}$ 加权的均值，而不是只平均"自己人"。这样改的动机很自然：当两簇交叠、样本介于两者之间时，硬分配会粗暴丢弃"不确定"这一信息，而软分配保留了它。加上温度参数与方差参数后，这套两步循环就是期望最大化（EM, Expectation-Maximization）算法在混合模型上的特例，后续讲次会完整推导。悬而未决的仍是 K 的选取与初始化——这是所有聚类方法的共同软肋。
