> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l15 · 行内双语视觉转录版 · 原图见 fig/l15/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l15-p1](fig/l15/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程总览页，标题 Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）；左侧配一幅绿色的分形树状网络装饰图。右侧给出整门课程的地图：

- Source coding（信源编码）——即 Data compression（数据压缩）
- Noisy-channel coding（噪声信道编码）
- Inference + probabilistic methods（推断与概率方法）
  - 9–10 Inference（推断）
  - 11 Clustering（聚类）
  - 12 Monte Carlo methods（蒙特卡罗方法）
  - 13 Advanced Monte Carlo methods（高级蒙特卡罗方法）
  - 14 Variational methods（变分方法）
- Neural networks（神经网络）
  - 15 Introduction to feedforward neural networks（前馈神经网络导论）
  - 16 Content-addressable memories（内容寻址存储器）
- State-of-the-art error-correcting codes（最先进的纠错码）

页脚两个网址：www.inference.phy.cam.ac.uk/itprnn/ 与 www.inference.phy.cam.ac.uk/itila/（课程与教材主页）。

### p.2 〔Reading（阅读材料）〕

![l15-p2](fig/l15/mgp00002.png)

- Neural networks（神经网络）：Chs 38, 39, (& perhaps 41, 44), 42（第 38、39 章，或可加看第 41、44 章，以及第 42 章）——此行书名为红字强调。
- State-of-the-art error-correcting codes（最先进的纠错码）：Chs 47, (48, 49,) & 50（第 47 章，(第 48、49 章) 及第 50 章）。

### p.3 〔Brains（大脑）〕

![l15-p3](fig/l15/mgp00003.png)

<span style="color:#2471a3;">**[section]**</span> 过渡页：中央仅一个大标题 Brains（大脑），下方为一幅大脑照片（深蓝背景上脑回脑沟清晰的整脑俯视图）。〔本页为纯图示过渡页〕

### p.4 〔How to make a content-addressable memory?（如何构造一个内容寻址存储器？）〕

![l15-p4](fig/l15/mgp00004.png)

<span style="color:#2471a3;">**[section]**</span> 本页只有标题一行：How to make a content-addressable memory?（如何构造一个内容寻址存储器？），正文留白，由课堂口头展开。

### p.5 〔Content-addressable memory（内容寻址存储器）〕

![l15-p5](fig/l15/mgp00005.png)

<span style="color:#2471a3;">**[example]**</span> 内容寻址存储器（content-addressable memory，CAM）第 1 组例子——五张 James Bond 主题图片：

- 左上：007 式枪管旋转圆标，内有持枪人影剪影，下方金色数字 "049"（007 的戏仿）；
- 中上：低分辨率枪管圆标，配文字 "Shaken, not…"（"摇匀，不要……"，指经典台词 shaken, not stirred，故意只说半句）；
- 右上：Sean Connery 持小口径手枪的黑白剧照；
- 左下：另一张枪管圆标小图；
- 中下：Bond 举枪姿态的黑色剪影。

要点：凭残缺、带噪的线索（半个圆标、一句没说完的台词、一个剪影），你的脑立刻"对上了号"——这正是内容寻址的日常经验。

### p.6 〔Content-addressable memory（内容寻址存储器）〕

![l15-p6](fig/l15/mgp00006.png)

<span style="color:#2471a3;">**[example]**</span> 内容寻址存储器第 2 组例子，页面上两行文字线索：

- Oscar-nominated actress called Natalie P******（一位获奥斯卡提名的女演员，姓氏被掩去，写作 Natalie P******）
- Acted a senator in an amazingly good Lucas film（在一部"好得惊人"的 Lucas 影片里饰演一位参议员）

配图为她在星球大战前传中的剧照：白装持爆能枪，左侧竖排蓝字 "NATALIE PORTMAN"。仅凭两条文字线索，你的记忆系统就检索出了完整的身份与面孔——又一个内容寻址的实例。

### p.7 〔Content-addressable memory（内容寻址存储器）〕

![l15-p7](fig/l15/mgp00007.png)

<span style="color:#2471a3;">**[example]**</span> 内容寻址存储器第 3 组例子，页面左侧标注 An author（一位作者）：一幅书的封面被若干蓝色色块大面积遮挡——只露出开头的 "A" 与中段的 "OF" 两处字样，封面照片（一位坐在轮椅上的男士）的眼部也被蓝块盖住。测试：遮挡大半信息后，你仍能认出这是哪本书。

### p.8 〔Content-addressable memory（内容寻址存储器）〕

![l15-p8](fig/l15/mgp00008.png)

<span style="color:#2471a3;">**[example]**</span> 上一页揭晓：完整封面显示 A BRIEF HISTORY OF TIME（时间简史）——THE UPDATED AND EXPANDED TENTH ANNIVERSARY EDITION（更新扩充十周年纪念版）——STEPHEN HAWKING（作者 Stephen Hawking，人名不译）。你的"内部存储器"早已存有这个模式，只凭 "A … OF" 两个词与轮椅剪影就完成了匹配——这就是大脑式内容寻址检索的威力。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把"内容寻址"与你在 6.006 里学过的哈希表对照着看：哈希表是"按地址存取"，键先经哈希函数算出桶下标，再按下标精确读写，依赖键的均匀随机分布来摊平冲突；而 CAM 反过来"按内容检索"，查询键本身可以残缺、带噪，系统要在整个存储体上做全局匹配，输出最相近的完整模式。从 CSAPP 的视角，每条记忆就是一串定长二进制模式（一个位向量），检索相当于在超立方体上找离查询点最近的格点。哈希表里一次比特翻转就可能掉进完全不同的桶，而 CAM 的容错恰恰来自"相近模式聚成同一个吸引盆地"的几何结构。这也解释了为什么大脑记人脸不需要"指针"：模式自身的内在结构就是它的地址。下一页的鸽子实验与后面的动力学系统构造都会反复用到这一点。

### p.9 〔Content-addressable memory（内容寻址存储器）〕

![l15-p9](fig/l15/mgp00009.png)

内容寻址存储器小结页，两个问题：

- How to do it?（怎么做到？）
- How do brains do it?（大脑又是怎么做到的？）

配图为同 p.3 的大脑照片。本讲此后将分两路展开：先看大脑能做什么（下两页），再讲工程上如何逼近。

### p.10 〔Brains（大脑）〕

![l15-p10](fig/l15/mgp00010.png)

<span style="color:#2471a3;">**[example]**</span> 大脑的记忆能力实测（鸽子实验）：

- Shown 725 images（给鸽子看了 725 张图片）
- instructed to memorize labels "+/-"（要求它们把每张图记住并对应 "+/-" 标签）

配图：一只鸽子站在石头上的彩色照片；右侧为实验所用黑白图片样例——街景、行人等生活照片各一页，页面上有 "P" 标号，底部印有图注残句 "Experiment P (specific person), which were correctly"（实验 P（特定人物），其中被正确……）〔原文在页面上被截断，句子不完整〕与 "+" 记号。

页脚文献：Fersen, L. & Delius, J. D. (1989) Long-term retention of many visual patterns by pigeons. Ethology 82: 141-155.（鸽子对大量视觉模式的长时保持）。

### p.11 〔What is the difference between（鸽子与超级计算机的区别是什么？）〕

![l15-p11](fig/l15/mgp00011.png)

页面标题只写了半句：What is the difference between（……之间的区别是什么），底部补全设问：a pigeon and a supercomputer?（一只鸽子和一台超级计算机之间有什么区别？）。配图：左为鸽子照片，右为一台蓝色调的 Cray 风格超级计算机（环形机柜中央是圆柱形处理器阵列）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道设问可以从信息论的两条路径来答。其一是能耗与并行：超级计算机按地址逐比特精确存取，每一次比特搬运都要付能量账，而鸽子大脑只有瓦级功耗，靠大规模并行、统计式的计算就完成了检索与识别。其二是编码哲学：回忆概率课里由大数定律导出的渐近均分性（AEP）——长随机序列几乎必然落在典型集（typical set）里，信息集中在"典型骨架"上；大脑记 725 张图时同样只存可分辨的模式骨架，而不必逐比特复刻原图。换句话说，超级计算机做的是精确的比特拷贝（CSAPP 意义上的确定性数据通路），大脑做的是带容错的统计推断。这一对比正是后面用动力学吸引子做存储的出发点。

### p.12 〔Parallel Distributed Processing（并行分布式处理）〕

![l15-p12](fig/l15/mgp00012.png)

<span style="color:#2471a3;">**[section]**</span> 新章节标题页：Parallel Distributed Processing（并行分布式处理），副标题两行：Neural Networks, Part I:（神经网络·第一部分：）与 Feedforward Networks（前馈网络），下方红字标注对应教材 Chapters 39, 41, 44（第 39、41、44 章）。

### p.13 〔本页无英文标题（本部分三要点概览）〕

![l15-p13](fig/l15/mgp00013.png)

本页无大标题，列出前馈网络部分的三条主线，右侧各配一张演示缩略图：

- Single neuron as a binary classifier（单神经元作为二分类器）——缩略图为三维 sigmoid 曲面 $y(x_1,x_2;\mathbf{w})$，参数 $(w_0,w_1,w_2)=(-15,2,1)$；
- Multi-layer network for regression（多层网络用于回归）——缩略图为隐单元直线扇形叠加与拟合曲线；
- Probabilistic interpretation of learning（学习的概率论解释）——缩略图为散点云加绿色同心椭圆与青色轨迹。

### p.14 〔Learning for a Single Neuron（单个神经元的学习）〕

![l15-p14](fig/l15/mgp00014.png)

<span style="color:#2471a3;">**[example]**</span> 单神经元演示。图为三维网格曲面：顶部标注 $y(x_1,x_2;\mathbf{w})$：$(w_0,w_1,w_2)=(-15,2,1)$；两个输入轴 $x_1$、$x_2$ 范围 0–10，输出轴 0–1。曲面是标准的 sigmoid（S 形）阶跃面——即 $\sigma(w_0+w_1x_1+w_2x_2)$ 形式的单神经元输出，沿直线 $w_1x_1+w_2x_2=w_0$ 的方向从 0 平滑过渡到 1；曲面上叠有多条彩色水平等值线（蓝、青、绿、黄、橙），标出输出取 0.25、0.5、0.75 等值时的位置。

左下角给出课堂演示命令：cd itp/neuron（进入演示目录）；gnuplot（启动绘图程序）；load 'LDEMO'（加载演示脚本）。

### p.15 〔Q: What happens if all three weights are doubled?（问：若三个权重全部加倍会怎样？）〕

![l15-p15](fig/l15/mgp00015.png)

绿色设问 Q: What happens if all three weights are doubled?（问：如果三个权重全部翻倍，会发生什么？）。三幅图作答：

- 左上图：$x_1$-$x_2$ 平面（0–10），顶部标注 w = (-15.0,2.0,1.0)；图中两条品红色平行直线（对应输出取两个不同阈值的等值线）与一条横穿的橙色斜向箭头线；
- 左下图：同样布局，标注 w = (-30.0,4.0,2.0)（即全部翻倍）；两条品红平行直线方向不变，但相互靠得更近（过渡带变窄）；
- 右图：三维 sigmoid 曲面，标注 $y(x_1,x_2;\mathbf{w})$：$(w_0,w_1,w_2)=(-15,2,1)$——即翻倍前的原曲面，供与左图对照。

图形给出的答案：翻倍不移动决策边界的方向与位置，只把 sigmoid 的过渡坡变得更陡。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 用 Strang 线代的语言看这幅图最清楚：决策边界就是直线 $w_1x_1+w_2x_2=w_0$，其法向量 $(w_1,w_2)$ 完全决定直线的方向与朝向。把三个权重全部翻倍，相当于把方程两边同乘 2，解集（直线本身）一毫米都不动——这就是左上、左下两图里品红线方向不变的原因；真正改变的是 sigmoid $\sigma(a)$ 的陡峭度：过渡带从宽坡收窄成陡坎。这个现象在统计物理里有精确类比：Gibbs distribution / Boltzmann distribution（吉布斯分布/玻尔兹曼分布）$p \propto e^{-\beta E}$ 中的 $\beta$ 就扮演"权重尺度"的角色——$\beta$ 加大等价于降温，分布从平缓走向接近确定的阶跃。所以"权重加倍"不是移动分类面，而是把模型的"温度"调低、把输出的确定性调高；这也是后面把权重初始化尺度与先验方差联系起来的伏笔。

### p.16 〔Single Neuron for digit classification（用单个神经元做数字分类）〕

![l15-p16](fig/l15/mgp00016.png)

<span style="color:#2471a3;">**[example]**</span> 标题：Single Neuron for digit classification（用单个神经元做数字分类），副题：Trained to distinguish 2s from 3s（训练它区分手写数字 2 和 3）。

配图：两幅约 $16\times16$ 的二值像素点阵〔尺寸按图估计〕，左为手写体 "2"，右为手写体 "3"，黑格表示笔迹像素。每个像素即神经元的一个输入。

### p.17 〔Single Neuron for digit classification（用单个神经元做数字分类）〕

![l15-p17](fig/l15/mgp00017.png)

同标题与副题（Trained to distinguish 2s from 3s，训练区分 2 与 3）。本页展示学得的结果：整个权重向量被画成一幅同样大小的灰度像素图——大部分区域为黑色（负或近零权重），中部与下部混杂白色与灰色方块（正权重），若干带细边框的小方块表示权重接近零；灰度明暗对应权重大小。底部一行结论：Error rate: 10%（错误率：10%）。

### p.18 〔Capacity of a neuron（神经元的容量）〕

![l15-p18](fig/l15/mgp00018.png)

<span style="color:#2471a3;">**[definition]**</span> 蓝色小标题：Learning as communication（把学习看作通信）。框图：左端 $\{t_n\}_{n=1}^{N}$（目标标签序列）经箭头进入 Learning algorithm（学习算法），输出 $\mathbf{w}$（权重）；箭头再指向右端一个同样的 $\mathbf{w}$，由它产生 $\{\hat{t}_n\}_{n=1}^{N}$（重建的标签序列）；输入 $\{\mathbf{x}_n\}_{n=1}^{N}$ 从下方分别馈入左侧的学习算法与右侧的 $\mathbf{w}$。也就是说，学习算法把 $N$ 个标签"压缩"进权重 $\mathbf{w}$，而 $\mathbf{w}$ 加上输入要把标签"解码"回来。

- 设问（"bits" 红字强调）：How many bits can a neuron learn?（一个神经元能学进多少比特？）

<span style="color:#00838f;">**[definition]**</span> 结论（青字，出处 Chapter 40 第 40 章）：A single neuron with $K$ inputs can almost certainly memorize up to $N = 2K$ random binary labels.（一个有 $K$ 个输入的单神经元，几乎必然能记住多达 $N=2K$ 个随机的二进制标签。）

- 底部结论（红字）：So the capacity of a neuron is two bits per connection（所以神经元的容量是每连接 2 比特）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "每连接 2 比特"这个数字值得用概率课的语言拆开：随机二进制标签 $t_n$ 的熵是每标签 1 比特（熵=随机变量的对数信息取期望这一节），要记住 $N$ 个随机标签，系统必须区分 $2^N$ 种标法，即吸收约 $N$ 比特信息；而仅 $K$ 个连续取值的连接竟装下 $2K$ 比特，说明"模拟量"确实在携带信息。它的味道与信源编码定理（source coding theorem）一致：可达的记忆/压缩极限由信息量而非存储单元个数直接决定。也请与 6.006/CLRS 里比较排序下界 $\Omega(n\log n)$ 的证明对读：两者都是"每次二分判定至多获得 1 比特、区分 $2^N$ 种情形至少需要多少判定"的计数论证。最后注意措辞："几乎必然"是概率陈述——$N=2K$ 是对随机标签成立的容量结果，并不是对任意标签组合都能保证的构造性结论。

### p.19 〔Multi-layer network for regression（用于回归的多层网络）〕

![l15-p19](fig/l15/mgp00019.png)

<span style="color:#2471a3;">**[example]**</span> 标题：Multi-layer network for regression（用于回归的多层网络）。黑底演示图：横轴 -6–6，纵轴 -10–10，中央有白色十字轴线。上半部是一束从中央一点向两侧张开的直线扇——即各隐单元的输入-输出直线；图例三个色块（橙、品红、浅蓝）标注 in / bias / out（对应输入权、偏置、输出权三组参数）。下半部蓝色曲线：一条平缓起伏、另一条在 $x\approx1$ 处陡降，展示目标函数与网络当前的拟合曲线。

左下角演示命令：cd itp/neuron/net（进入网络演示目录）；octave（启动 Octave）；DEMO（运行演示）。

### p.20 〔Applications（应用）〕

![l15-p20](fig/l15/mgp00020.png)

<span style="color:#2471a3;">**[example]**</span> 标题：Applications（应用），列出四个真实案例（后续四页逐个给图）：

- Reading aloud - Nettalk（朗读文本——Nettalk 系统）：Sejnowski and Rosenberg（Sejnowski 与 Rosenberg）
- Handwriting recognition - LeNet（手写体识别——LeNet）：Yann LeCun（Yann LeCun，人名不译）
- Weld toughness（焊缝韧性预测）：Bhadeshia et al（Bhadeshia 等）
- Focussing multiple-mirror telescopes（多镜面望远镜聚焦）：Roger Angel（Roger Angel，人名不译）

### p.21 〔Applications（应用）〕

![l15-p21](fig/l15/mgp00021.png)

本页给 Nettalk 配上结构图：底部一行输入字符 "T h i s   i s   t h e"，一个四格滑动窗口套住中间的 [s][ ][i][s]（其中当前字符 "s" 深色高亮），行末标注 input（输入），行首一个向左的长箭头表示窗口随阅读推进逐字左移。窗口内每个字符格向上引出多条箭头，汇入 Hidden units（隐单元）方框；隐单元再向上汇入写有 \z\ 的方框，旁边标注 Output units (phoneme code)（输出单元——音素编码）。即：网络读入字母窗口，输出当前字母的读音音素。其余三条应用要点同 p.20。

### p.22 〔Applications（应用）〕

![l15-p22](fig/l15/mgp00022.png)

本页给 LeNet 配上演示截图：AT&T 面板，标题 "LeNet 5 RESEARCH"，红字 answer: 34（答案：34）；上方两行小字 "3 3　4 4 4" 与 "333551444" 为逐字符候选识别序列；中央大图是手写的 "34"（笔迹上还有横向贯穿的划痕）；左侧一列为网络各处理阶段的缩略图（原字符、边缘、杂乱特征图、逐级识别结果）。其余应用要点同上。这个例子展示了多层网络的实用性：即使输入被划痕污染，仍给出正确识别。

### p.23 〔Applications（应用）〕

![l15-p23](fig/l15/mgp00023.png)

本页给焊缝韧性案例配图：左下是成卷连续钢丝（焊丝）的照片；右侧大图为 Siemens arc welding facility（西门子电弧焊接车间），现场贴有三张黄色手写便签：

- "Here the electrodes from second arc being used ↓"（这里是第二电弧正在使用的电极 ↓）〔手写体，个别词难以辨认〕
- "These are the continuous wire electrodes (2 specifically) from second arc weld model"（这些是第二电弧焊模型所用的连续焊丝电极——具体为两根）〔手写体，部分词难以辨认〕
- "Components to be welded ↓"（待焊接的部件 ↓）

其余应用要点同上（其中手写识别一行本页写作 Handwriting recognition，作者仍是 Yann LeCun）。该案例（Bhadeshia 等）用神经网络由合金成分与工艺参数预测焊缝韧性。

### p.24 〔Applications（应用）〕

![l15-p24](fig/l15/mgp00024.png)

本页给最后一个案例配图：Roger Angel（人名不译）站在一块大型蜂窝状镜坯旁的照片——他的多镜面望远镜项目用神经网络实时调整各镜面，实现 Focussing multiple-mirror telescopes（多镜面望远镜聚焦）。其余三条应用要点同 p.20。

### p.25 〔Probabilistic interpretation of learning（学习的概率论解释）〕

![l15-p25](fig/l15/mgp00025.png)

<span style="color:#2471a3;">**[example]**</span> 标题：Probabilistic interpretation of learning（学习的概率论解释）。黑底演示图，顶部标注 Gaussian approximation c.f. Langevin（高斯近似 与 Langevin 方法对照）；横轴 0–6，纵轴 -3–5。黄色 "+" 点云密集在 $(1.5,1)$ 附近并向右下方向拖尾（这是某个损失面上按玻尔兹曼式分布采出的参数样本）；两个绿色同心椭圆是对该分布的高斯近似等值线；一条青色曲线是 Langevin 动力学的采样轨迹，从左下角爬升进入云团中心。图意：参数后验既可用高斯近似刻画，也可用随机动力学直接采样。

### p.26 〔本页无英文标题（数据量 N 增大时似然与参数后验的演化）〕

![l15-p26](fig/l15/mgp00026.png)

<span style="color:#2471a3;">**[example]**</span> 本页无标题，是一张三列对照表：Data set（数据集）、Likelihood（似然）、Probability of parameters（参数的概率），四行分别对应 $N=0,2,4,6$ 个数据点：

- $N=0$：似然为 (constant)（常数）；中列三维网格图是宽平的波包，右列等高线图是以原点为中心的同心圆（$w_1$、$w_2$ 轴均 -5–5）——即只有先验。
- $N=2$：左列散点图（$x_1$、$x_2$ 轴均 -10–10）给出 2 个数据点（□ 与 × 两种记号）；中列似然曲面沿一条脊线陡然隆起（纵轴刻度可见 0.5）；右列等高线贴着对角方向拉长成束——两个数据点只约束了参数的一个组合方向。
- $N=4$：4 个数据点；似然曲面收成尖峰（纵轴刻度可见 0.7 与 0.35）；等高线收缩为小椭圆。
- $N=6$：6 个数据点；尖峰更锐（纵轴刻度可见 0.05）；等高线几乎缩成一点。

整体趋势：数据越多，参数的概率分布越向真值集中，且集中发生在"被数据约束的方向"上。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这张表就是 Bayesian inference（贝叶斯推断）的可视化教科书：每行三列对应"数据 → 似然 $P(\{t\}\mid\mathbf{w})$ → 归一化后的参数后验"这条链，$N=0$ 行的同心圆就是先验（prior），之后每加一批数据，后验（posterior）都按"先验×似然（likelihood）"重新加权并进一步收缩。用 Strang 线代的话说，右列椭圆是后验协方差矩阵的等高线：长轴方向对应数据几乎没约束的参数线性组合（不确定度大），短轴方向是被数据钉死的组合，且 $N$ 增大时协方差大致按 $1/N$ 收缩——这与"典型子空间/投影"的直觉相通：数据把参数空间投影到一个小得多的高概率子区域。特别注意 $N=2$ 那一行：似然沿一条脊线呈高原状延伸，因为两个数据点只能给直线族提供一个约束，这正是欠定系统在几何上的样子。

### p.27 〔Langevin method（Langevin 方法）〕

![l15-p27](fig/l15/mgp00027.png)

<span style="color:#2471a3;">**[definition]**</span> 标题：Langevin method（Langevin 方法），要点：Simple version of Hamiltonian Monte Carlo（哈密顿蒙特卡罗的简化版本）。

右上配图：黑底轨迹图（横轴 -2–1，纵轴 -1.5–1），一条带星形标记的红色折线来回折返穿行，一条橙色直线段从左下延到右上（两端有黄色小方块标记），顶部一条红色箭头自上而下指向轨迹。〔图上无文字标注〕

下排三幅细长椭圆（$P^*(\mathbf{x})$ 的两条等高线）对比图：

- (a) Dumb Metropolis（笨 Metropolis）：当前点 $\mathbf{x}^{(1)}$，围绕它的虚线圆是提议分布 $Q(\mathbf{x};\mathbf{x}^{(1)})$，半径 $\epsilon$，圆内小箭头表示各方向等概率提议；
- (b) Gradient descent（梯度下降）：当前点带一个沿 $-\eta\mathbf{g}$（负梯度方向）的箭头，纯确定性下坡；
- (c) Langevin：当前点同样有半径 $\epsilon$ 的虚线提议圆，但小箭头整体偏向 $-\eta\mathbf{g}$ 方向——随机提议叠加了梯度偏置。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 三幅小图把三种"在目标分布 $P^*(\mathbf{x})$ 里游走"的策略放在一起对比。笨 Metropolis 在半径 $\epsilon$ 的球里均匀提议、再按 Metropolis 准则接受或拒绝：在细长分布里步子稍大就大量被拒，步子稍小又寸步难行；纯梯度下降只用 $-\eta\mathbf{g}$，会一头扎进最近的极大点并停死，根本采不到样；Langevin 方法把两者相加——提议中心偏向 $-\eta\mathbf{g}$、再保留随机扰动，恰能使马尔可夫链的平稳分布等于 $P^*$。你在概率课里见过"马尔可夫链收敛到平稳分布"的直觉，这里是它的连续态版本；再配大数定律（沿轨迹的时间平均收敛到期望，即遍历性），就得到用随机游走估计高维积分的合法性——这正是讲 12–13 蒙特卡罗方法（Monte Carlo methods）的地基。右上图的折返红线就是一条真实的采样路径。

### p.28 〔Feedforward neural networks（前馈神经网络）〕

![l15-p28](fig/l15/mgp00028.png)

<span style="color:#2471a3;">**[section]**</span> 标题：Feedforward neural networks（前馈神经网络），两行设问式要点：

- Just high-dimensional curve-fitting?（难道只是高维曲线拟合？）
- Brains do more（大脑做的远不止这些）

### p.29 〔Brains（大脑）〕

![l15-p29](fig/l15/mgp00029.png)

<span style="color:#2471a3;">**[example]**</span> 标题 Brains（大脑）。整页为一幅黑白二值化"噪点"图：满纸黑白碎块看似随机，但画面中央隐约藏着一只穿行于草木枝叶之间的大型猫科动物（豹）。〔本页为纯图示〕——多数人在被告知之前看不出，一旦看出便再也无法"看回噪声"。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页是对上一页"前馈网络只是高维曲线拟合吗"的直接回应：视觉识别不是从像素到标签的确定性函数拟合，而是推断。按贝叶斯框架拆解：先验——"草丛里可能有大型猫科动物"这类结构性预期；似然——黑白像素块的排布与"豹的轮廓"相容的程度；两者相乘归一化得到后验，后验一旦集中，你的感知就被"锁定"，甚至无法再看回噪声。这与本讲开头的 CAM 是同一枚硬币的两面：记忆与感知都是在带噪线索下检索/重构最相符的完整模式。另外注意信息论的细节：这幅图被二值化到每像素约 1 比特仍有极高可辨性，说明有效信息集中在少数结构性比特上——这正是后续章节讨论稀疏编码（sparse coding）时要去定量刻画的现象。

### p.30 〔Brains（大脑）〕

![l15-p30](fig/l15/mgp00030.png)

<span style="color:#2471a3;">**[example]**</span> 标题 Brains（大脑）。整页为一幅手绘图形：一个巨大的正六边形轮廓，内部均匀铺满密集的随机小点与小箭头/三角形纹理，无任何文字标注。〔本页为纯手绘图示〕可视为对"大量简单单元（点）组织成有序整体（六边形）"的隐喻，与并行分布式处理的主题呼应。

### p.31 〔How to make a content-addressable memory?（如何构造一个内容寻址存储器？）〕

![l15-p31](fig/l15/mgp00031.png)

<span style="color:#2471a3;">**[section]**</span> 回扣标题页：How to make a content-addressable memory?（如何构造一个内容寻址存储器？）。页面内容与 p.5 完全相同：五张 James Bond 图片——"049" 枪管圆标、低分辨率 "Shaken, not…" 枪管图、Sean Connery 剧照、小枪管图与 Bond 剪影。此时再问一次：我们能否造一个像你认出 Bond 那样、凭残缺内容自动补全的动力学系统？下一页给出工程指标。

### p.32 〔Content-addressable memory challenge（内容寻址存储器的挑战）〕

![l15-p32](fig/l15/mgp00032.png)

<span style="color:#2471a3;">**[definition]**</span> 标题：Content-addressable memory challenge（内容寻址存储器的挑战）。核心任务：Make a dynamical system（构造一个动力学系统），满足：

- 25 dynamical variables, 300 parameters (4-bit precision)（25 个动力学变量、300 个参数，精度 4 位）；
- that has attracting fixed points at desired memories（使各条期望记忆成为吸引不动点——"attracting fixed points" 红字强调）；
- such that noisy versions are automatically cleaned up（带噪的版本会被自动"清洗"回完整记忆）。

配图：左侧一条黑色竖带上排列着多幅 5×5 左右的点阵小图（待存储的记忆列表）；中央三对 5×5 点阵图，每对之间一个红色箭头：左边为带噪模式，右边为系统收敛后的干净模式——三组演示自动去噪。

底部两条追加要求：

- and such that new memories can be added incrementally（并且新记忆能够增量式地加入）；
- AND robust to corruption of more than half the parameters（而且即使超过一半的参数被破坏也依然稳健——"more than half the parameters" 紫红字强调）。

这两条正是把"如何构造 CAM"变成一个可检验的工程命题；后续讲次的 Hopfield 式方案将逐条对照这些指标。
