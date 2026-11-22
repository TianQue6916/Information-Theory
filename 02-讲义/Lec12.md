> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l12 · 行内双语视觉转录版 · 原图见 fig/l12/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l12-p1](fig/l12/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程总大纲页：左侧一幅绿色双曲树状图（大圆盘内以圆、方、三角等节点经直线相连、层层向外分支，圆盘边缘密布彩色小节点），右侧为本课程全部讲次的目录：

- 1 Noisy-channel coding（噪声信道编码）
- **Source coding (Data compression)**（信源编码，即数据压缩）：
  - 2 Information content, entropy（信息量、熵）
  - 3 Typicality and the source coding theorem（典型性与信源编码定理）
  - 4 Symbol codes（符号码）
  - 5 Symbol codes and Arithmetic coding（符号码与算术编码）
- **Noisy-channel coding**（噪声信道编码）：
  - 6 Information measures for noisy channels（噪声信道的信息度量）
  - 7 Capacity of a noisy channel（噪声信道的容量）
  - 8 The noisy-channel coding theorem（噪声信道编码定理）
- **Inference + probabilistic methods**（推断与概率方法）：
  - 9–10 Inference（推断）
  - 11 Clustering（聚类）
  - 12–13 Monte Carlo methods（蒙特卡罗方法）
  - 14 Variational methods（变分方法）

> <span style="color:#7f8c8d;">旁注：左下角两个网址 www.inference.phy.cam.ac.uk/itprnn/ 与 www.inference.phy.cam.ac.uk/itila/。列表首行"1 Noisy-channel coding"在幻灯片上独立出现在 Source coding 之前，照原样转录。</span>

### p.2 〔The course / The book（课程与教材）〕

![l12-p2](fig/l12/mgp00002.png)

- The course（课程）：www.inference.phy.cam.ac.uk/itprnn/
- 右侧为教材封面：David J. C. MacKay《Information Theory, Inference, and Learning Algorithms》（浅绿色封面，带斜条纹纹理与散布的紫红色小方块，右下角 Cambridge 出版社标识）
- The book（书）：www.inference.phy.cam.ac.uk/itila/

### p.3 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p3](fig/l12/mgp00003.png)

<span style="color:#2471a3;">**[section]**</span> 本讲大纲（打印体幻灯片）：

- **Simple Monte Carlo methods**（简单蒙特卡罗方法）：
  - Importance sampling（重要性采样）
  - Rejection sampling（拒绝采样）
- **Markov-chain Monte Carlo methods**（马尔可夫链蒙特卡罗方法，MCMC）：
  - Metropolis method（Metropolis 方法）
  - Gibbs sampling（Gibbs 采样）
  - Slice sampling（切片采样）
- **Reducing random-walk behaviour**（减少随机走行为）：
  - Hamiltonian Monte Carlo（哈密顿蒙特卡罗）
  - Overrelaxation（超松弛）
- **Exact sampling**（精确采样）

> <span style="color:#7f8c8d;">旁注（Exact sampling 下的黄色小字，无法完全辨认）：〔无法辨认〕，似为 "exact: RUNME"。</span>

右侧黑底终端风格配图共三幅：

- 上图标注 "estimate of ⟨φ⟩"（⟨φ⟩ 的估计）：一条品红色曲线，横轴 number of samples（样本数）0–50，纵轴 0–3；曲线从约 2 起快速下坠、在样本数约 10 之后平稳于约 0.8–1 之间。
- 中图：三条曲线叠画，横轴 0–50、轴下一排黄色短刻度标记样本位置；图例 P*(x)（红色，峰约 3 位于 15 附近的尖峰，其后带肩部）、phi(x)（绿色，宽缓曲线，峰约 2 位于 30 附近）、Q(x)（青色，从 0 缓慢上升的直线，右端约 2.2）。
- 下图标题 "50 samples, 19 accepted"（50 个样本，19 个被接受）：横轴 −4 到 4，纵轴 0–4；绿色包络曲线 Q(x)（宽钟形，峰约 4）、红色目标曲线 P*(x)（双峰，主峰约 3、次峰约 1）；rejected（被拒绝）样本为灰色 × 点散布在上部，accepted（被接受）样本为青色点集中在底部横线附近。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 蒙特卡罗方法的合法性直接建立在你在大二概率论里学过的大数定律（law of large numbers）之上：若 $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(R)}$ 独立同分布地采自 $P$，则样本平均 $\frac{1}{R}\sum_r \phi(\mathbf{x}^{(r)})$ 依概率收敛到期望 $\Phi=\sum_{\mathbf{x}}\phi(\mathbf{x})P(\mathbf{x})$——"熵是随机变量自信息的期望"与"估计量是函数的期望"，在概率论里是同一套期望语言。右上图那条 estimate of ⟨φ⟩ 曲线先剧烈抖动、后趋于平稳，正是有限样本下方差的真实表现：估计的标准误按 $1/\sqrt{R}$ 下降，这与 6.042 里用切比雪夫不等式证大数定律的路径一致——只要方差有限，均值就向期望集中。另请留意中图里 $Q(x)$（青色直线）才是实际可采样的分布，$P^*(x)$（红色）是目标分布，二者不重合时必须靠权重修正，这正是下一节 importance sampling 要解决的问题。把目标定为"估计期望"而非"枚举全部状态"，是蒙特卡罗在状态空间指数膨胀时仍可行的根本原因。

### p.4 〔Lecture 11 / 12 / 13（第 11、12、13 讲）〕

![l12-p4](fig/l12/mgp00004.png)

- Lecture 11　Clustering（第 11 讲：聚类）
- Lecture 12　Monte Carlo methods（第 12 讲：蒙特卡罗方法）
- Lecture 13　Advanced Monte Carlo methods（第 13 讲：高等蒙特卡罗方法）

### p.5 〔Clustering（聚类）〕

![l12-p5](fig/l12/mgp00005.png)

页标题 Clustering（聚类）。图为打印体图题 "K means clustering"（K 均值聚类）下的黑底散点图：横轴 0–10，纵轴 0–8（刻度 0, 2, 4, 6, 8）。四簇数据分别以不同符号绘制：白色 × 簇（左下，中心约 (2, 2.4)）、绿色 + 簇（中部偏左，中心约 (3, 4.8)）、蓝色 □ 簇（右上，中心约 (6.8, 7.3)）、黄/橙 ◇ 簇（右下，中心约 (7.3, 3.5)）；每簇中心用同色圈住的星号标出，即 K 均值收敛后的簇中心。图中有少量"错位"点（如绿色 + 中偏右一颗约 (5, 6)、蓝色 □ 中偏左一颗约 (5.2, 6.6)），显示分配按最近中心进行而非按视觉归属。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> K 均值的 Assign（指派）步本质上是对每个数据点做一次最近邻查询：把点归给距离最近的簇中心，这正是 6.006 里最近邻搜索的应用场景（用 k-d 树平均 $O(\log n)$ 即可完成一次查询）；指派完成后，整个空间被隐式划分成以各中心为种子的 Voronoi（沃罗诺伊）区域。Update（更新）步则把每个中心移到该簇点的均值上。从概率论角度看，K 均值最小化的"簇内平方误差和"恰等于各簇方差乘以簇内点数再求和——均值是使平方和最小的点，一维情形求导即得，多维情形按坐标分解同理，这就是 Update 公式长得像样本均值的原因。还要记住 Lloyd 迭代（Assign 与 Update 交替）只保证目标函数单调不增、收敛到局部最优：初值不同结果可能不同，图中那几颗"错位"点正提示了硬分配对噪声的敏感，这也是随后引入 soft K means 的动机。

### p.6 〔Clustering（聚类）〕

![l12-p6](fig/l12/mgp00006.png)

<span style="color:#2471a3;">**[section]**</span> 聚类部分大纲（打印体幻灯片）：

- **K means clustering**（K 均值聚类）：
  - Assign（指派）
  - Update（更新）
- **Soft K means clustering**（软 K 均值聚类）：
  - Assign（指派）
  - Update（更新）

### p.7 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p7](fig/l12/mgp00007.png)

<span style="color:#2471a3;">**[section]**</span> 大纲页再次显示，红色分隔线移到 **Slice sampling** 之上，表示当前讲到切片采样：

- **Simple Monte Carlo methods**（简单蒙特卡罗方法）：Importance sampling（重要性采样）、Rejection sampling（拒绝采样）
- **Markov-chain Monte Carlo methods**（马尔可夫链蒙特卡罗方法）：Metropolis method（Metropolis 方法）、Gibbs sampling（Gibbs 采样）、Slice sampling（切片采样）← 当前节
- **Reducing random-walk behaviour**（减少随机走行为）：Hamiltonian Monte Carlo（哈密顿蒙特卡罗）、Overrelaxation（超松弛）
- **Exact sampling**（精确采样）

> <span style="color:#7f8c8d;">旁注（Exact sampling 下的黄色小字，无法完全辨认）：〔无法辨认〕，似为 "exact: RUNME"。</span>

右侧黑底终端风格配图（自上而下四幅，演示 slice sampling）：

- 顶图：图例 P*(x)（红色，左偏双峰，主峰约 3 位于 −2 附近）、Q(x|x_t)（绿色，中心约 1 的宽峰，峰约 2）；一条橙色竖线（当前点 $x_t$，约 −1）与一条品红竖线（约 1）；横轴 −4 到 4，轴下有青色点刻度。
- 第二幅：橙色二维等高线（同心闭合曲线，中心约 (0.9, 0.7)，右侧纵轴标注 1；横轴 −0.5 到 2.5），其上部叠有一条品红色方块折线路径，在等高线上方水平往返并逐层下移。
- 第三幅：左标 Current hypothesis（当前假设）的黄色单峰曲线（内部画竖线与半高横线示意切片区间），下行 Data（数据）为若干青色点。
- 底图：图例 P*(x)（红色多峰曲线，主峰约 3）、x(t)（品红竖线，位于约 1.8 处）、interval（绿色水平线段，约从 0.9 延伸到 1.8、高度约 0.6）；横轴约 −4 到 4，纵轴 0–3，底部有青色点刻度。

### p.8 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p8](fig/l12/mgp00008.png)

本页为打印体正文页（衬线字体）：

- Interested in（我们关心的是）　$P(\mathbf{x}) = \frac{1}{Z} P^*(\mathbf{x}) = \frac{1}{Z} e^{-E(\mathbf{x})}$。
- Can evaluate（可逐点计算）　$E(\mathbf{x})$ at any $\mathbf{x}$（在任意 $\mathbf{x}$ 处的能量）。
- **Problem 1**（问题 1）　Make samples（产生样本）　$\mathbf{x}^{(r)} \sim P$
- **Problem 2**（问题 2）　Estimate expectations（估计期望）

```math
\Phi \equiv \sum_{\mathbf{x}} \phi(\mathbf{x})\, P(\mathbf{x})
```

<span style="color:#2471a3;">**[note]**</span> **What we're not trying to do**（我们**并非**要做的）：

- We're not trying to find the most probable state.（我们并不试图找出最可能的状态。）
- We're not trying to visit all typical states.（我们并不试图访问**所有**典型状态。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本页定义了后续一切采样方法的对象：目标分布 $P(\mathbf{x})=\frac{1}{Z}P^*(\mathbf{x})=\frac{1}{Z}e^{-E(\mathbf{x})}$。这个形式在统计物理里叫玻尔兹曼分布（Boltzmann distribution），$E(\mathbf{x})$ 是能量，$Z$ 是配分函数（归一化常数）。关键困难在于：$E(\mathbf{x})$ 逐点可算，但 $Z=\sum_{\mathbf{x}}e^{-E(\mathbf{x})}$ 要对全部状态求和，而状态数往往是指数级的（$N$ 个自旋有 $2^N$ 个状态）——这与 6.042 里组合计数的爆炸式增长是同一类困难，所以必须绕开 $Z$ 直接采样，这正是蒙特卡罗的价值所在。MacKay 强调的"What we're not trying to do"与第 3 讲的典型集（typical set）思想一脉相承：高维分布的质量集中在典型集里，估计期望只需按正确频率从典型集中抽样本即可，既不必找单个"最优"成员，也不必遍历所有成员。可以类比比较排序的下界 $\Omega(n\log n)$：枚举状态的下限是指数时间，而采样把任务降为"按分布抽典型样本"，这是复杂度层面的本质跨越。

### p.9 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p9](fig/l12/mgp00009.png)

本页与 p.3 版面完全相同（讲义放映时重复显示的大纲页）。<span style="color:#2471a3;">**[section]**</span> 大纲：Simple Monte Carlo methods（简单蒙特卡罗方法：Importance sampling 重要性采样、Rejection sampling 拒绝采样）；Markov-chain Monte Carlo methods（马尔可夫链蒙特卡罗方法：Metropolis method、Gibbs sampling、Slice sampling）；Reducing random-walk behaviour（减少随机走行为：Hamiltonian Monte Carlo、Overrelaxation 超松弛）；Exact sampling（精确采样）。

> <span style="color:#7f8c8d;">旁注（Exact sampling 下的黄色小字）：〔无法辨认〕，似为 "exact: RUNME"。</span>

右侧黑底配图同 p.3：上图 "estimate of ⟨φ⟩"（品红曲线，横轴 number of samples 0–50，纵轴 0–3，先降后平稳于约 0.8–1）；中图 P*(x)（红）、phi(x)（绿）、Q(x)（青色上升直线）叠画，轴下黄色样本刻度；下图 "50 samples, 19 accepted"（50 个样本，19 个被接受）：绿包络 Q(x)、红目标 P*(x)、rejected 灰 × 点、accepted 青点，横轴 −4 到 4。

### p.10 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p10](fig/l12/mgp00010.png)

本页与 p.7 版面完全相同：大纲页重复显示，红色分隔线仍位于 **Slice sampling** 之上（当前节：切片采样）。四组条目同前：Simple Monte Carlo methods（Importance sampling、Rejection sampling）；Markov-chain Monte Carlo methods（Metropolis method、Gibbs sampling、Slice sampling ← 当前）；Reducing random-walk behaviour（Hamiltonian Monte Carlo、Overrelaxation）；Exact sampling。

> <span style="color:#7f8c8d;">旁注（Exact sampling 下的黄色小字）：〔无法辨认〕，似为 "exact: RUNME"。</span>

右侧黑底配图同 p.7（slice sampling 演示）：顶图 P*(x)（红，左偏双峰）与 Q(x|x_t)（绿，宽峰）及橙、品红两条竖线；第二幅橙色二维等高线（中心约 (0.9, 0.7)，横轴 −0.5 到 2.5）上的品红方块折线路径；第三幅 Current hypothesis（黄色单峰曲线带竖线与半高横线）与 Data（青色点）；底图 P*(x)（红多峰）、x(t)（品红竖线约 1.8）、interval（绿色横线段）。

### p.11 〔Gibbs sampling（Gibbs 采样）〕

![l12-p11](fig/l12/mgp00011.png)

页标题 Gibbs sampling（Gibbs 采样）。本页为黑底演示图（打印体图形，无手写正文）：

- 上图：二维橙红色等高线图（约 4–5 层同心闭合曲线，中心约 (0.9, 0.7)，整体向左上方拖尾），横轴 −0.5 到 2.5，右侧纵轴处标注 1。其上叠一条品红色方框折线路径（Gibbs 采样的移动轨迹）：起点为黄色星号（约 (−0.15, 1.0)），水平右移至约 (0.8, 1.0)（空心小方块），再竖直下移至约 (0.8, 0.65)，随后水平移到约 (0.95, 0.65) 处（黄色星号终点）——每一步都平行于某一坐标轴。
- 下图：左标 Current hypothesis（当前假设）：一条黄色钟形曲线（峰约在 0.9 处），曲线内画一条过峰的竖线与一条半高横线，示意"固定其他变量后的条件分布及其切片区间"；其下 Data（数据）一行有 6 个青色星号（横轴约 −0.3、0.3、0.55、0.85、1.15、1.45 附近）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Gibbs 采样的思想是坐标轮换：每次固定其余坐标，从该坐标在给定其余变量下的条件分布重采一个值。图中品红折线就是这种"横平竖直"的轨迹——先水平（重采 $x_1$），再竖直（重采 $x_2$）。这里用的是概率论中条件分布与边缘分布的区别：$P(x_1\mid x_2)$ 一般不等于边缘 $P(x_1)$，下方 Current hypothesis 画的就是固定数据后关于当前那个坐标的条件分布。从 Strang 线代的角度看二维等高线最有启发：把协方差矩阵对角化，等高线主轴就是特征向量方向，而 Gibbs 只沿坐标基方向 $e_1,e_2$ 走；当两变量强相关（协方差矩阵非对角占优、条件数大）时，等高线成细长斜椭圆，坐标方向与谷底方向近乎垂直，每步只能横向挪一小段——这正是本讲末尾 p.16 "随机走行为"的几何根源。补救思路与梯度下降做预条件/坐标变换类似：把坐标系旋转到主轴方向（如超松弛），或改用沿谷底推进的方法（如哈密顿蒙特卡罗）。

### p.12 〔Clustering（聚类）〕

![l12-p12](fig/l12/mgp00012.png)

<span style="color:#2471a3;">**[section]**</span> 聚类部分大纲（第三版，新增第三项；打印体幻灯片）：

- **K means clustering**（K 均值聚类）：
  - Assign（指派）
  - Update（更新）
- **Soft K means clustering**（软 K 均值聚类）：
  - Assign（指派）
  - Update（更新）
- **Clustering by Gibbs sampling**（用 Gibbs 采样做聚类）：
  - Assign（指派）
  - Update（更新）

### p.13 〔Gibbs sampling for clustering（用 Gibbs 采样做聚类）〕

![l12-p13](fig/l12/mgp00013.png)

页标题 Gibbs sampling for clustering（用 Gibbs 采样做聚类）。本页配图与 p.11 完全相同（黑底演示图）：

- 上图：二维橙红色等高线（约 4–5 层同心闭合曲线，中心约 (0.9, 0.7)，向左上拖尾；横轴 −0.5 到 2.5，右侧标注 1），叠品红色方框折线的 Gibbs 轨迹：黄色星号起点约 (−0.15, 1.0) → 水平至约 (0.8, 1.0) → 竖直下移至约 (0.8, 0.65) → 水平至终点黄色星号约 (0.95, 0.65)。
- 下图：Current hypothesis（当前假设）为黄色钟形曲线（峰约 0.9，带过峰竖线与半高横线）；Data（数据）一行 6 个青色星号。

此处把 p.11 的通用 Gibbs 演示重新解读为聚类语境：等高线是"参数（如簇中心位置）的后验"，下方钟形曲线是给定数据与其他参数时某单变量的条件分布，Data 行是观测点。

### p.14 〔Gibbs sampling for clustering（用 Gibbs 采样做聚类）〕

![l12-p14](fig/l12/mgp00014.png)

页标题同前。本页为黑底演示图（打印体图形）：

- Current hypothesis（当前假设）区：三条曲线叠画——品红色曲线为两分量之和（预测的观测分布：左段宽而低、右段高而窄的叠加，整体呈右高双肩形）；黄色窄高分量（峰约在 0.9 处，内部画过峰竖线与半高横线，表示该分量的当前参数）；橙色宽低分量（低矮、横向延展覆盖大部分横轴）。
- Data（数据）区：最下一行约 13 个青色星号（观测点，右中部约 0.9–1.1 处密集）；其上方一行约 10 个橙色方块（横轴位置与部分星号对齐，表示被指派到宽分量）；方块行与星号行之间另有 4 个黄色小圆圈（位于约 0.7–1.0 之间，表示被指派到窄高分量）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页把 Gibbs 采样用于上一讲的聚类：Data 行青色星号是观测点，其上的橙色方块与黄色圆圈是当前抽样给出的簇分配，三条曲线分别是预测分布（品红，两分量混合）、窄高分量（黄）与宽低分量（橙）。对比三种分配观：K 均值做硬分配（每点唯一归属，对应图中确定的方块/圆圈）；soft K 均值给出"责任"（responsibility，即后验概率）；Gibbs 聚类更进一步——分配本身是随机变量，算法在"给定分配更新参数"与"给定参数重采分配"之间交替，这正是贝叶斯推断的框架：后验 $\propto$ 似然 $\times$ 先验，Assign 步取 $P(\text{分配}\mid\text{数据},\text{参数})$，Update 步从 $P(\text{参数}\mid\text{数据},\text{分配})$ 抽样。你在 Bertsekas 概率里熟悉的链式分解 $P(a,b)=P(a)\,P(b\mid a)$ 正是被反着用：已知一部分，从另一部分的条件分布抽样。这种"参数–隐变量交替"结构也是第 11 讲 EM 算法 E 步/M 步的随机化对应物。

### p.15 〔Monte Carlo methods（蒙特卡罗方法）〕

![l12-p15](fig/l12/mgp00015.png)

本页与 p.7 / p.10 版面完全相同：大纲页第三次显示，红色分隔线仍位于 **Slice sampling** 之上（当前节：切片采样）。条目：Simple Monte Carlo methods（Importance sampling、Rejection sampling）；Markov-chain Monte Carlo methods（Metropolis method、Gibbs sampling、Slice sampling ← 当前）；Reducing random-walk behaviour（Hamiltonian Monte Carlo、Overrelaxation）；Exact sampling。

> <span style="color:#7f8c8d;">旁注（Exact sampling 下的黄色小字）：〔无法辨认〕，似为 "exact: RUNME"。</span>

右侧黑底配图同 p.7（slice sampling 演示四幅）：顶图 P*(x)（红）与 Q(x|x_t)（绿）加橙、品红两条竖线；第二幅橙色等高线上的品红方块折线；第三幅 Current hypothesis（黄曲线）与 Data（青点）；底图 P*(x)（红多峰）、x(t)（品红竖线）、interval（绿色横线段）。

### p.16 〔Problems with standard Monte Carlo methods（标准蒙特卡罗方法的问题）〕

![l12-p16](fig/l12/mgp00016.png)

<span style="color:#2471a3;">**[section]**</span> 标准蒙特卡罗方法的三大问题（左列红色）与对应出路（右列绿色）：

- Random walk behaviour（随机走行为） → Efficient methods（高效方法）
- Sensitivity to step size（对步长的敏感性） → Slice sampling（切片采样）
- When to stop（何时停止） → Exact sampling（精确采样）

左下角黑底小图，图题 "Gibbs sampling"：横轴约 −1 到 1，纵轴 −1 到 1（刻度 1、0.5、0、−0.5、−1）。目标分布集中在两条近乎平行的对角线之间的细长带内（绿色，从左下角 (−1,−1) 贯穿到右上角 (1,1)）；一条橙色锯齿折线轨迹被限制在带内 (0, 0) 附近的一小段里来回跳动——直观展示强相关目标分布下 Gibbs 采样沿坐标轴移动极其缓慢。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本页总结标准蒙特卡罗的三大痛点，左下小图是最直观的证据：目标分布在细长对角带内，Gibbs 的橙色轨迹却只在 $(0,0)$ 附近打转。"随机走行为"的代价可用 6.006 图上游走的直觉估算：一维对称随机走走 $R$ 步的典型位移仅 $\sqrt{R}$ 量级，要穿越长度为 $L$ 的"峡谷"需 $L^2$ 步，混合时间被平方放大；这与 6.006/CLRS 分析随机化算法时"独立性带来快速收敛、相关性带来拖延"的经验一致。"对步长敏感"则像调学习率的梯度下降：步长太小走得慢，太大则在 Metropolis 中拒绝率飙升、原地不动。"何时停止"更微妙——马尔可夫链样本相关，不能像独立样本那样直接用 $1/\sqrt{R}$ 估计误差，也没有可靠的内在收敛信号，这正是右列三项技术的动机：Efficient methods 消减随机走、Slice sampling 自适应消除步长选择、Exact sampling 从理论上保证样本恰来自平稳分布。带着这三个问题进入第 13 讲，就能看清每种 advanced 方法分别对症下药于哪一点。
