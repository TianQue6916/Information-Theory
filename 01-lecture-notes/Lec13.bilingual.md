> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l13 · 行内双语视觉转录版 · 原图见 fig/l13/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l13-p1](fig/l13/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程标题页。左侧是一张分形树图示：圆形边界内一棵绿色递归树，内部节点为绿色圆圈与方块，越靠外层分叉越密，末端挂着蓝、红、品红等彩色小环。右侧列出课程三大板块：

- Source coding (Data compression)（信源编码，即数据压缩）
- Noisy-channel coding（噪声信道编码）
- Inference + probabilistic methods（推断与概率方法），下辖：
  - 9–10 Inference（推断）
  - 11 Clustering（聚类）
  - 12 Monte Carlo methods（蒙特卡罗方法）
  - 13 Advanced Monte Carlo methods（高级蒙特卡罗方法）——即本讲
  - 14 Variational methods（变分方法）

页脚两行网址：`www.inference.phy.cam.ac.uk/itprnn/`（课程主页）与 `www.inference.phy.cam.ac.uk/itila/`（教材主页）。

### p.2 〔Overview（课程概览）〕

![l13-p2](fig/l13/mgp00002.png)

<span style="color:#2471a3;">**[section]**</span> 左侧课程内容清单：

- Data compression（数据压缩）——对应教材第 1–6、8–10、14 章
- Noisy-channel coding（噪声信道编码）
- Inference, data modelling（推断与数据建模）：clustering, pattern recognition（聚类、模式识别）——第 20、22 章
- Probability toolbox（概率工具箱）：
  - Monte Carlo methods（蒙特卡罗方法）——第 29、30、32 章
  - Variational methods（变分方法）——第 33 章
- Neural networks（神经网络）——第 38、39（或再加 41、44）、42 章
- State-of-the-art error-correcting codes（最先进的纠错码）

右侧 Recommended exercises（推荐习题）：习题 29.14、33.5、33.7、27.1、22.11、39.4、39.5；Handouts 2, 3 (on website)（讲义材料 2、3，见课程网站）；The 5 cards magic trick (15.6)（"五张牌"魔术，见 15.6 节），下方配四张扑克牌：8♦、2♥、10♣、9♦。

Additional reading（延伸阅读）：Laplace's method (Ch 27)（Laplace 方法，第 27 章）；Ising models (Ch 31)（Ising 模型，第 31 章）。

### p.3 〔The course / The book（课程网站与教材）〕

![l13-p3](fig/l13/mgp00003.png)

- The course（课程）：`www.inference.phy.cam.ac.uk/itprnn/`
- The book（教材）：`www.inference.phy.cam.ac.uk/itila/`

右侧为教材封面图：David J. C. MacKay《Information Theory, Inference, and Learning Algorithms》（《信息论、推断与学习算法》），封面为浅绿底、布满斜向纹理与粉紫色小块的图案。

### p.4 〔Monte Carlo methods（蒙特卡罗方法）〕

![l13-p4](fig/l13/mgp00004.png)

<span style="color:#2471a3;">**[section]**</span> 本讲提纲：

- Simple Monte Carlo methods（简单蒙特卡罗方法）：
  - Importance sampling（重要性采样）
  - Rejection sampling（拒绝采样）
- Markov-chain Monte Carlo methods（马尔可夫链蒙特卡罗方法）：
  - Metropolis method（Metropolis 方法）
  - Gibbs sampling（Gibbs 采样）
  - Slice sampling（切片采样）（该条位于一条红色分隔线之下）
- Reducing random-walk behaviour（减少随机游走行为）：
  - Hamiltonian Monte Carlo（哈密顿蒙特卡罗）
  - Overrelaxation（过松弛）
- Exact sampling（精确采样）

> <span style="color:#7f8c8d;">旁注：Exact sampling 条目下方有一行黄色小字 "itpvexact/hc RUNME"，是课上现场运行的演示程序名。</span>

右侧自上而下三幅黑底演示截图：

1. 上图：橙色曲线 $P^*(x)$（目标分布）与绿色曲线 $Q(x;x_t)$（随当前点 $x_t$ 移动的提议分布），各带一条竖直标记线；横轴约 −4 至 4，图底部散布几个青色样本点——"提议窗跟着当前点走"的示意。
2. 中图：橙色同心等高线的二维分布上一条品红/橙色随机轨迹（Metropolis 游走轨迹），横轴约 −0.5 至 2.5，右侧标到 1。
3. 下图：上半是标注 Current hypothesis（当前假设）与 Data（数据）的面板；下半为多峰橙色曲线 $P^*(x)$，品红竖线标 $x[t]$，绿色横线标 interval（区间），右侧图例与此一致——切片采样一次迭代的图解。

### p.5 〔Problems with standard Monte Carlo methods（标准蒙特卡罗方法的问题）〕

![l13-p5](fig/l13/mgp00005.png)

<span style="color:#2471a3;">**[section]**</span> 左侧红色大字列出标准方法的三大问题：

- Random walk behaviour（随机游走行为）
- Sensitivity to step size（对步长敏感）
- When to stop（何时停止）

右侧绿色大字给出本讲将对应介绍的三类解法：

- Efficient methods（高效方法）
- Slice sampling（切片采样）
- Exact sampling（精确采样）

左下角黑底图（标题 Gibbs sampling）：两条绿色平行斜线构成从 (−1,−1) 到 (1,1) 的极窄斜带，橙色 Gibbs 采样轨迹被夹在带内以直角小步折返——目标分布高度相关时，逐坐标更新的 Gibbs 采样几乎无法沿带方向移动。

### p.6 〔Random walk behaviour（随机游走行为）〕

![l13-p6](fig/l13/mgp00006.png)

标题 Random walk behaviour（随机游走行为）。黑底演示图（标题 Gibbs sampling）：绿色两条平行斜线构成一条贯穿 (−1,−1) 至 (1,1) 的窄斜带，橙色轨迹为 Gibbs 采样路径——它只能在水平、竖直两个坐标方向交替移动，因此在窄带内以锯齿形缓慢爬行，很难沿带方向前进。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张窄带图是理解"随机游走行为"最直观的一页：两条绿线之间的窄带就是两个高度相关变量（比如 $x_1\approx x_2$）的联合后验，而 Gibbs 采样每步只沿一个坐标轴动，于是只能在带内做直角折返。从概率论看，这是一条平稳分布为目标分布的马尔可夫链；单步位移均值为零、方差有限，因此 $t$ 步后离出发点的典型距离只有 $\sqrt{t}$ 量级——这正是概率论里对称随机游走"标准差 $=\sqrt{t}$"的直接体现。把窄带想成 6.006 里一条细长的链状图，随机游走覆盖它所需的时间对带宽是平方级的：带宽每缩小一半，推进同样纵向距离的步数约翻两番。所以相关性越强（带越窄），混合越慢，样本间自相关时间越长，有效样本数远小于迭代次数。后文的哈密顿蒙特卡罗与过松弛，本质都是让更新"带着方向"走，以打破这种 $\sqrt{t}$ 扩散标度。

### p.7 〔Terminal demo: ./demo.p, 20 iterations（终端演示：20 次迭代）〕

![l13-p7](fig/l13/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 一张终端窗口截图，菜单栏为 File/Edit/View/Terminal/Help，命令行提示符与命令为 `25:lewis:/home/mackay/itp/metrop> ./demo.p`（目录名 metrop 表明这是 Metropolis 演示）。屏幕主体是用 `*` 号逐行打印的一维直方图：星号组成一条竖直窄列，左右各一条竖直虚线作标尺；底部一行文字 `20 iterations`（20 次迭代）。此时随机游走刚从起点出发不久，样本仍集中在起点附近的窄峰内。

### p.8 〔560 iterations（560 次迭代时的直方图叠加）〕

![l13-p8](fig/l13/mgp00008.png)

<span style="color:#2471a3;">**[example]**</span> 黑底直方图叠放图，标题 560 iterations（560 次迭代）。横轴 0–20（一维格点），纵轴 0–45（计数）。右上角图例按迭代数配色：560 品红、520 蓝、480 青、440 绿、400 黄、360 橙、320 灰白。七条直方图轮廓叠在一起：越晚的迭代越宽、越平，但所有曲线都保留明显锯齿，相邻格点高低交错（奇偶格差异），尚未收敛到光滑形状。

### p.9 〔t=0（第 0 步：初始分布）〕

![l13-p9](fig/l13/mgp00009.png)

<span style="color:#2471a3;">**[example]**</span> 黑底折线图，标题 t=0。横轴 0–20（格点位置），纵轴 0–1（概率）。图例：x0 = 10（黄色）、x0 = 17（青色）。黄色曲线在 x=10 处一个高度 1 的尖峰，青色曲线在 x=17 处一个高度 1 的尖峰——两条独立的随机游走链分别从 10 与 17 出发，初始分布各退化为单点。

### p.10 〔t=1（第 1 步）〕

![l13-p10](fig/l13/mgp00010.png)

同前坐标与图例（黄：x0=10；青：x0=17）。t=1 时每个单点分布分裂为左右两峰：黄色在 x=9 与 x=11 各一个约 0.5 的峰，青色在 x=16 与 x=18 各一个约 0.5 的峰——每步以等概率左移或右移一格。

### p.11 〔t=2（第 2 步）〕

![l13-p11](fig/l13/mgp00011.png)

同前坐标与图例（纵轴上限 0.6）。黄色呈三峰：x=8 约 0.25、x=10 约 0.5、x=12 约 0.25；青色同样三峰：x=15 约 0.25、x=17 约 0.5、x=19 约 0.25——二项分布形状开始显现，中间格点概率最高。

### p.12 〔t=3（第 3 步）〕

![l13-p12](fig/l13/mgp00012.png)

同前坐标与图例。黄色四峰：x=7 约 0.125，x=9 与 x=11 各约 0.375，x=13 约 0.125；青色类似地铺开，两链的支撑区开始在 x≈13 附近相互接触。

### p.13 〔t=4（第 4 步）〕

![l13-p13](fig/l13/mgp00013.png)

同前坐标与图例。黄色峰位于偶数格点 6、8、10、12（约 0.06、0.25、0.375、0.25），最左小峰刚从 6 冒头；青色峰在 13、15、17、19（约 0.06、0.25、0.375、0.25），右缘 20 处略有抬升。偶数步时质量只落在偶数格点——周期性造成的锯齿依旧。

### p.14 〔t=5（第 5 步）〕

![l13-p14](fig/l13/mgp00014.png)

同前坐标与图例。黄色峰回到奇数格点 5、7、9、11、13、15（两端约 0.03、次高约 0.16、中央约 0.31）；青色峰在 12、14、16、18 与右缘 20，同样钟形，两链尾部已明显交叠。

### p.15 〔t=6（第 6 步）〕

![l13-p15](fig/l13/mgp00015.png)

同前坐标与图例。黄色主峰在 x=10（约 0.31），向两侧递减（8、12 约 0.23；6、14 约 0.09；最左端只剩刚能看见的小凸起）；青色主体在 14–20，且在 x≈11–13 出现小尾部与黄色交叠。

### p.16 〔t=25（第 25 步）〕

![l13-p16](fig/l13/mgp00016.png)

同前坐标与图例（纵轴上限 0.2）。两条分布都已大幅铺开但远未均匀：黄色质量偏向左半，主峰在 x=9–13（最高约 0.155 于 x=11），左端 0–6 留有小残迹；青色偏向右半，主峰在 x=15–20（约 0.15），右缘 20 处因边界挡回而偏高。奇偶锯齿仍然显著。

### p.17 〔t=50（第 50 步）〕

![l13-p17](fig/l13/mgp00017.png)

同前坐标与图例。两链分布进一步摊平：黄色主峰仍略偏左（约 0.11），青色偏右（约 0.11），曲线交错起伏，锯齿幅度比 t=25 减小，但离均匀值 0.05 仍有明显差距。

### p.18 〔t=75（第 75 步）〕

![l13-p18](fig/l13/mgp00018.png)

同前坐标与图例。黄色主峰约 0.09、青色主峰约 0.09，两链的峰谷开始互相咬合，整体轮廓更平，但奇偶交替的锯齿仍未消失。

### p.19 〔t=100（第 100 步）〕

![l13-p19](fig/l13/mgp00019.png)

同前坐标与图例。主峰高约 0.08，两曲线整体已接近彼此，仅剩交替的小峰谷差异。

### p.20 〔t=125（第 125 步）〕

![l13-p20](fig/l13/mgp00020.png)

同前坐标与图例。主峰高约 0.07，黄、青两曲线几乎逐点互补地交织在一起，起伏进一步变小。

### p.21 〔t=150（第 150 步）〕

![l13-p21](fig/l13/mgp00021.png)

同前坐标与图例。主峰高约 0.065，锯齿继续变浅，两条曲线都向 0.05 的均匀水平收拢。

### p.22 〔t=200（第 200 步）〕

![l13-p22](fig/l13/mgp00022.png)

同前坐标与图例。主峰高约 0.06，只剩细小的交替波纹；两链已难分彼此。

### p.23 〔t=300（第 300 步）〕

![l13-p23](fig/l13/mgp00023.png)

同前坐标与图例。两条曲线几乎重合，仅在 0.05 上下有极小的波纹——接近均匀分布。

### p.24 〔t=400（第 400 步）〕

![l13-p24](fig/l13/mgp00024.png)

同前坐标与图例。两条曲线完全叠平在 0.05（黄青重叠处呈绿色），即 20 个格点上的均匀分布——随机游走终于"忘记"了出发点。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把 p.9 到 p.24 连起来看就是一部"随机游走收敛编年史"：从 10 或 17 出发的 ±1 随机游走，$t$ 步后的分布是二项分布 $C(t,k)2^{-t}$，宽度按标准差 $\sqrt{t}$ 增长，所以 20 个格点要摊到接近均匀（0.05）竟花了约 400 步。这组图还暴露了马尔可夫链的一个经典隐患——周期性（periodicity，周期性）：每步必须移动一格，导致偶数步质量只落在偶数格点、奇数步只在奇数格点，于是图中长期保留奇偶锯齿，两条链要"错开半拍"才能重合。概率论中处理这类问题的标准药方是让链允许原地不动（惰性化，lazy chain）或加入自环，从而消除周期性。另外注意右边界 20 附近质量偏高，那是游走被边界挡回的堆积效应；实际 MCMC 中边界处理不当同样会悄悄扭曲目标分布。与 CSAPP 的视角呼应：若用整型状态做随机更新，$\pm 1$ 步进本质上就是在地址空间上的线性游走，其扩散规律与这里完全一致。

### p.25 〔Random walk behaviour（随机游走行为，重复页）〕

![l13-p25](fig/l13/mgp00025.png)

与 p.6 相同的标题页：Random walk behaviour（随机游走行为），黑底图（标题 Gibbs sampling）——绿色窄斜带与带内小幅折返的橙色 Gibbs 轨迹。放回这张图作小结：上面十几页的一维扩散演示，回答的正是"随机游走行为为什么是问题"。

### p.26 〔Efficient Monte Carlo methods（高效蒙特卡罗方法）〕

![l13-p26](fig/l13/mgp00026.png)

<span style="color:#2471a3;">**[section]**</span> 黑字标题 Efficient Monte Carlo methods（高效蒙特卡罗方法），下列两行蓝色大字：

- Hamiltonian Monte Carlo（哈密顿蒙特卡罗）
- Overrelaxation（过松弛）

### p.27 〔Narrow-band staircase trajectory（窄带上的阶梯轨迹图）〕

![l13-p27](fig/l13/mgp00027.png)

<span style="color:#2471a3;">**[example]**</span> 无标题纯图示页：黑底，两条橙色平行斜线构成从 (−1,−1) 到 (1,1) 的窄带（即 p.6 的同一目标分布）。一条由青色小方框首尾相连的阶梯状轨迹从左下角 (−1,−1) 附近出发（左下有一支白色箭头指示起点），沿窄带稳步向右上推进，至约 (0.55, 0.52) 处结束，轨迹上有两个黄色星号标记。与 p.6 中原地打转的普通 Gibbs 轨迹相比，这条轨迹沿带方向推进得多——直观展示抑制随机游走后的采样效率。〔本页为纯图示页〕

### p.28 〔Efficient Monte Carlo methods（高效蒙特卡罗方法，重复页）〕

![l13-p28](fig/l13/mgp00028.png)

与 p.26 相同的分节页：Efficient Monte Carlo methods（高效蒙特卡罗方法）——Hamiltonian Monte Carlo（哈密顿蒙特卡罗）与 Overrelaxation（过松弛）。

### p.29 〔Gibbs sampling（Gibbs 采样轨迹）〕

![l13-p29](fig/l13/mgp00029.png)

<span style="color:#2471a3;">**[example]**</span> 黑底图，白色标题 Gibbs sampling（Gibbs 采样）。绿色两条平行斜线构成 (−1,−1) 至 (1,1) 的窄带；橙色折线轨迹集中在带的中段（约 −0.3 至 0.4 之间）以直角小步折返，始终没有沿带方向走远——普通 Gibbs 采样随机游走行为的特写。

### p.30 〔Adler's Overrelaxation（Adler 过松弛）〕

![l13-p30](fig/l13/mgp00030.png)

<span style="color:#2471a3;">**[example]**</span> 黑底图，白色标题 Adler's Overrelaxation（Adler 过松弛）。同一条绿色窄带上，橙色轨迹从左下 (−1,−1) 一路沿带推进到右上约 (0.8, 0.85)，途中只有轻微回摆——与 p.29 对比，过松弛让每步更新都朝条件分布"另一侧"大幅跳跃，消除了随机游走行为。

### p.31 〔Adler's Overrelaxation（Adler 过松弛，放大图）〕

![l13-p31](fig/l13/mgp00031.png)

<span style="color:#2471a3;">**[example]**</span> 上一页的放大版：横轴约 −1 到 0.1，纵轴约 −1 到 0.1。绿色窄带下缘与红/橙色上缘清晰可见；橙色阶梯状轨迹从 (−1,−1) 出发，以水平—竖直交替的阶梯稳步爬升到约 (−0.1, 0.05)——每一步都跨过条件分布的大部分宽度，轨迹沿带方向近乎单调推进。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Adler 过松弛的核心思想一句话就能说清：不再"均匀随机地"从条件分布里抽下一点，而是系统性地抽到条件分布"另一侧"较远的位置。对二元变量这件事尤其直白：设当前位取 1 的条件概率为 $p$，普通 Gibbs 以概率 $p$ 保持 1，而过松弛则以很高的概率翻转到 0——这本质上是一次受控的位翻转，熟悉 CSAPP 的读者可以把它想成对状态字节做了一次有偏的 XOR 运算。妙处在于，Adler 证明了这种看似"粗暴"的更新在适当构造下仍保持目标分布不变（平稳性不被破坏），却把随机游走的扩散步换成了"定向跃迁"，混合速度大幅提升（p.29 与 p.30 的对比就是证据）。代价是该方法通常不可逆（不满足细致平衡），理论分析更难，而且对条件分布形状有较强假设（如条件 CDF 可逆）。这提示我们：马尔可夫链正确性的要求是"平稳分布正确"，而非"每步都必须随机"——系统性更新同样可以是合法的采样器。

### p.32 〔Robust Monte Carlo methods: Slice sampling（稳健蒙特卡罗方法：切片采样）〕

![l13-p32](fig/l13/mgp00032.png)

<span style="color:#2471a3;">**[section]**</span> 黑字标题 Robust Monte Carlo methods（稳健蒙特卡罗方法），下列一行蓝色大字：Slice sampling（切片采样）。

### p.33 〔25 samples（25 个样本：切片采样演示）〕

![l13-p33](fig/l13/mgp00033.png)

<span style="color:#2471a3;">**[example]**</span> 白底图，标题 25 samples（25 个样本）。橙色曲线 $P^*(x)$ 是主峰在 x≈−2（高约 3）、次峰在 x≈1（高约 1.1）的双峰分布；品红竖线标 $x(t)$（当前样本，位于 −2）；绿色横线标 interval（区间），高约 1.85，从约 −3 延伸到约 0.5，两端为绿色 ×；区间上黄色 × 位于 $x(t)$ 正上方，其右侧的青色小圈是本次在切片内试探的点。横轴底部沿 0 线撒着 25 个青色 ×（历次样本）：绝大多数挤在主峰附近，少数落在 0–2 的次峰区——切片采样凭"自动调宽的区间"无需步长参数即可在多峰间适度游走。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 切片采样引入了一个"辅助变量"技巧，学过概率论中联合分布与边缘分布的读者会立刻认出它的骨架：把单个变量 $x$ 扩充成 $(x,u)$，令联合密度在 $0<u<P^*(x)$ 上均匀，于是 $u$ 的边缘分布均匀、$x$ 的边缘分布恰为目标分布；交替对 $x$ 与 $u$ 做条件更新，就得到一条平稳分布正确的马尔可夫链。图中绿色横线正是给定 $u$ 后的"切片" $\{x: u<P^*(x)\}$——注意它在次峰上方也自动延伸出一段，因此算法天然有能力跳到次峰，而固定步长的 Metropolis 一旦步长设小就出不了主峰。与拒绝采样对照着看更有收获：两者都在"曲线下方面积"里做文章，拒绝采样要求全局上界包络（峰越高越难），切片采样只需逐点的局部高度，所以对 $P^*$ 的尺度不敏感。工程上它常嵌入 Gibbs 式框架使用（如 BUGS/JAGS 软件），这正是"稳健"二字的由来：几乎不用调步长参数。

### p.34 〔Self-terminating Monte Carlo methods: Exact sampling（自终止蒙特卡罗方法：精确采样）〕

![l13-p34](fig/l13/mgp00034.png)

<span style="color:#2471a3;">**[section]**</span> 黑字标题 Self-terminating Monte Carlo methods（自终止蒙特卡罗方法），下列一行蓝色大字：Exact sampling（精确采样）。

### p.35 〔Exact sampling: Hexagon（精确采样：六边形平铺，两条链）〕

![l13-p35](fig/l13/mgp00035.png)

<span style="color:#2471a3;">**[example]**</span> 页面标题 Exact sampling（精确采样），大字标题 Hexagon（六边形）。上半部分并排两幅红/绿/蓝三色菱形铺积（lozenge tiling，菱形铺积）的三维方块堆叠图：左图标 Height: 78，右图标 Height: 407，对应下方轨迹图中两条链在当前时刻各自的堆叠高度。下方轨迹图：纵轴从 −512 到 512，红色曲线自顶部 512 出发一路下行，蓝色曲线自底部 −512 出发一路上行（图左端另有一小段更早时刻的短轨迹），右段两线逐渐贴近中间水平线——这是"从过去耦合"演示中从最高、最低两个极端状态出发的两条链。

### p.36 〔Exact sampling: Hexagon（精确采样：六边形平铺，会合时刻）〕

![l13-p36](fig/l13/mgp00036.png)

同页结构：大字标题 Hexagon，上方单个红/绿/蓝菱形铺积方块堆叠，标注 Height: 313。下方轨迹图纵轴 −256 至 512、横轴 −256 至 0：红色曲线自左上 512 附近下行、蓝色曲线自底部上行，右端两线贴着中线会合——耦合在时刻 0 完成，输出的正是上方这个平铺样本。

### p.37 〔Exact sampling（精确采样：单个大平铺）〕

![l13-p37](fig/l13/mgp00037.png)

〔本页为纯图示页〕页面仅标题 Exact sampling（精确采样）与一幅大图：六边形区域的红/黄/蓝三色菱形铺积，三种朝向的菱形密铺满整个大六边形——精确采样得到的一个完整样本。

### p.38 〔Exact sampling（精确采样：多次平铺的叠加）〕

![l13-p38](fig/l13/mgp00038.png)

〔本页为纯图示页〕大六边形内叠印了大量平铺构型的边界细线（品红/蓝/黄密织成网）；六个角部区域按红、黄、蓝相间"冻结"（左、右两角红色，上侧两角分别为黄/蓝，下侧两角分别为黄/蓝），叠加的网格进不了角落、只能填满中央区域；左上角另有一个小六边形缩略图（单个样本）。

### p.39 〔Exact sampling（精确采样：叠加图局部放大）〕

![l13-p39](fig/l13/mgp00039.png)

〔本页为纯图示页〕p.38 中央区域的放大：密集的平铺边界线整体外缘勾出一道清晰的圆弧——即著名的"北极圈"（arctic circle，北极圈）现象：圆内是液态的随机区，圆外是冻结区（图中可见左上黄色、右上蓝色、右下红色冻块）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这组六边形平铺图演示的是 Propp 与 Wilson 的"从过去耦合"（coupling from the past，CFTP），它正面回答了 p.5 提出的"何时停止"：不再猜烧入期（burn-in）多长，而是让所有可能的初始状态同时演化，直到它们全部会合为同一状态，此时输出精确服从平稳分布——注意是"精确"，不是"近似"。对菱形铺积这类有偏序结构的系统，只需同时跟踪最大与最小两个状态即可代表全体（p.35、p.36 轨迹图中从 512 与 −512 出发的红、蓝两线正是这对极端链），这把指数多个初始状态压缩成两条链，堪称 6.006 意义上"带正确性证明的随机算法"的范例：运行时间随机，但输出分布无误。叠加图（p.38、p.39）里的圆弧边界是统计物理的"北极圈"现象：六边形中心如液态、边角被冻结，关联长度在临界附近发散。还需提醒：精确采样只对能构造可行耦合（如单调）的系统奏效，对一般后验仍是开放难题。

### p.40 〔Exact sampling for the Ising model（Ising 模型的精确采样）〕

![l13-p40](fig/l13/mgp00040.png)

<span style="color:#2471a3;">**[section]**</span> 一行蓝色大字标题：Exact sampling for the Ising model（Ising 模型的精确采样）。

### p.41 〔Exact sampling for the Ising model（Ising 模型的精确采样，重复页）〕

![l13-p41](fig/l13/mgp00041.png)

与 p.40 相同的一行蓝色大字标题：Exact sampling for the Ising model（Ising 模型的精确采样）——演示切换动画时的重复分节页。

### p.42 〔Introduction to the Ising model（Ising 模型入门）〕

![l13-p42](fig/l13/mgp00042.png)

> <span style="color:#7f8c8d;">旁注：页眉右上角绿字 "See Ising models (Ch 31)"（参见教材第 31 章 Ising 模型）。</span>

标题 Introduction to the Ising model（Ising 模型入门），主体为教材图 31.4 及其图注："Figure 31.4. Detail of Monte Carlo simulations of rectangular Ising models with J = 1. (a) Mean energy and fluctuations in energy as a function of temperature. (b) Fluctuations in energy (standard deviation). (c) Mean square magnetization. (d) Heat capacity."（图 31.4：$J=1$ 的矩形 Ising 模型蒙特卡罗模拟细节。(a) 平均能量及能量涨落随温度的变化；(b) 能量涨落（标准差）；(c) 平均平方磁化；(d) 热容。）

四幅小图（横轴均为温度 $T$，约 1.5–5；左上图另标注 N = 4096）：

- 左上 (a)：每自旋平均能量，纵轴 −2 至 0：低温处约 −2，在 T≈2.2–2.5 间陡升，之后缓慢升至约 −0.45。
- 左中 (b)：能量标准差，纵轴 0.015–0.05：在 T≈2.3 处出现尖峰（约 0.047）。
- 右中 (c)：平均平方磁化，纵轴 0–1：T≲2.2 时接近 0.9–1，在 T≈2.3–2.6 间骤降至 0。
- 右下 (d)：热容，纵轴 0–1.8：在 T≈2.3 处出现尖峰（约 1.7）。

三个"峰/骤降"都指向同一处温度——临界温度 $T_c$（critical temperature，临界温度）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Ising 模型是统计物理与机器学习的公共基石：$N$ 个格点自旋 $s_i\in\{\pm1\}$，能量正比于相邻同号对的数目（$-J\sum s_i s_j$），玻尔兹曼分布（Boltzmann distribution，玻尔兹曼分布）给每个构型的概率 $\propto e^{-E/T}$——这正是最大熵原理在"约束平均能量"条件下推出的吉布斯分布（Gibbs distribution，吉布斯分布），概率论视角下它就是"熵最大且能量期望固定"的那一个分布。图 31.4 的四幅小图合起来讲了一个相变故事：低温时相邻自旋抱团、平均能量接近 −2、平方磁化接近 1；升温到临界温度 $T_c\approx 2.27$（二维方形晶格）附近，能量标准差与热容同时出现尖峰、磁化骤降——热容尖峰意味着涨落巨大，"临界态"没有特征尺度，这与随后 p.43–p.46 的粗化对比直接呼应。用 Strang 线代的眼光看，相变对应转移矩阵主特征值与其余特征值差距拉大（关联长度变长即次特征值衰减变慢），这也是 MCMC 在 $T_c$ 附近混合极慢的根源。

### p.43 〔Exact sampling - Ising model at Tc（精确采样——临界温度下的 Ising 模型）〕

![l13-p43](fig/l13/mgp00043.png)

<span style="color:#2471a3;">**[example]**</span> 标题 Exact sampling - Ising model at Tc（精确采样——$T_c$ 处的 Ising 模型）。一幅大尺寸黑白方格构型：每个格点为黑（自旋一个方向）或白（另一方向），黑白团簇大小悬殊、边界曲折破碎，呈现临界态特有的分形面貌——既非低温的大块磁化，也非高温的细密噪声。

### p.44 〔Exact sampling - Ising model at Tc（精确采样——$T_c$ 处的 Ising 模型，粗化对比一）〕

![l13-p44](fig/l13/mgp00044.png)

<span style="color:#2471a3;">**[example]**</span> 同标题。左侧一幅细格点黑白构型（分辨率约与 p.43 相当），右侧一幅格点约放大 2 倍的黑白构型：团簇轮廓更粗、块面更大，整体统计面貌与左侧相似。

### p.45 〔Exact sampling - Ising model at Tc（精确采样——$T_c$ 处的 Ising 模型，粗化对比二）〕

![l13-p45](fig/l13/mgp00045.png)

<span style="color:#2471a3;">**[example]**</span> 同标题。左侧同一张细格点小图，右侧格点约放大 4 倍的构型：黑白块更大更疏，仍保持黑白面积大致均衡、团簇跨越多个尺度。

### p.46 〔Exact sampling - Ising model at Tc（精确采样——$T_c$ 处的 Ising 模型，粗化对比三）〕

![l13-p46](fig/l13/mgp00046.png)

<span style="color:#2471a3;">**[example]**</span> 同标题。左侧同一张细格点小图，右侧格点约放大 8 倍的粗粒化构型：只剩大块黑白斑块。四页连看即"临界态没有特征尺度"的直观演示：无论把分辨率放粗到哪一档，看到的统计结构都相似（自相似性）。

### p.47 〔Problems with standard Monte Carlo methods（标准蒙特卡罗方法的问题，完整版）〕

![l13-p47](fig/l13/mgp00047.png)

<span style="color:#2471a3;">**[section]**</span> p.5 的完整版。左侧红色列出三大问题：Random walk behaviour（随机游走行为）、Sensitivity to step size（对步长敏感）、When to stop（何时停止）；左下角仍是那张 Gibbs 采样窄带图。右侧绿色三行对应解法：Efficient methods（高效方法）、Slice sampling（切片采样）、Exact sampling（精确采样）。

页面下方新增红色条目：Not revealing the normalizing constant（不揭示归一化常数），其下绿色小字方法清单：

- Thermodynamic integration（热力学积分）
- Reversible-jump Markov chain Monte Carlo（可逆跳马尔可夫链蒙特卡罗）
- The acceptance ratio method（接受率方法）
- Umbrella sampling（伞形采样）
- Simulated tempering（模拟回火）
- Tempered transitions (Radford Neal)（回火转移，Radford Neal 提出）
- Annealed importance sampling (Radford Neal)（退火重要性采样，Radford Neal 提出）
- Linked importance sampling (Radford Neal)（链接重要性采样，Radford Neal 提出）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "不揭示归一化常数"是 MCMC 最容易被初学者忽略的短板：马尔可夫链只需知道 $P^*(x)$ 的相对形状即可采样，因此它对乘性常数 $Z=\int P^*(x)\,dx$ 完全盲目；但在贝叶斯推断（Bayesian inference，贝叶斯推断）里，这个 $Z$ 恰恰是证据（evidence，证据）$P(\text{data})$，是模型比较与贝叶斯奥卡姆剃刀的关键量。清单里各方法的共同思路是"沿一条路径积分"：热力学积分把 $\ln Z$ 写成对温度参数的积分；退火重要性采样从易采样的高温分布出发、沿一串中间分布"退火"到目标分布，用重要性权重累积出 $Z$ 的无偏估计；伞形采样与模拟回火则人为加大分布重叠、帮助游走跨越能量势垒。要注意重要性类方法虽"无偏"，权重方差可能大到不可用——这与 6.006/CLRS 中"随机化算法不仅要看期望、还要看方差集中度"的精神一致。评估一个 $Z$ 估计器时，永远追问：方差界在哪里？

### p.48 〔$P^*(\mathbf{x})$ iceberg（$P^*(\mathbf{x})$ 冰山示意图）〕

![l13-p48](fig/l13/mgp00048.png)

〔本页为纯图示页〕上下两幅线描图。上图：一块灰色平板状冰山悬浮在透视网格平面（状态空间 $\mathbf{x}$ 的网格）上方，一条弯曲箭头从右侧标注 $P^*(\mathbf{x})$ 指向冰山侧立面。下图：海面剖面图——一艘小船浮在蓝绿色水面线上，水面之下的冰体向下延伸出两根极深的窄"冰柱"。配合上一页"不揭示归一化常数"的主题：采样器在 $P^*(\mathbf{x})$ 上游走，只见到"水面以上"的形状，而分布的"总体积"（归一化常数）与深藏水下的尾部质量依然不可见。
