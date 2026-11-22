> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l10 · 行内双语视觉转录版 · 原图见 fig/l10/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l10-p1](fig/l10/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程总览页。标题：Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）。左侧是一幅绿色分形树插图（圆形轮廓内的树状分形，枝头缀着红蓝小圈）。右侧列出课程板块与各讲目录（绿色大圆点为板块标记）：

- 1 Noisy-channel coding（噪声信道编码）
- Source coding (Data compression)（信源编码＝数据压缩）：2 Information content, entropy（信息量与熵）；3 Typicality and the source coding theorem（典型性与信源编码定理）；4 Symbol codes（符号码）；5 Symbol codes and Arithmetic coding（符号码与算术编码）
- Noisy-channel coding（噪声信道编码）：6 Inference and Information measures for noisy channels（推断与噪声信道的信息度量）；7 Capacity of a noisy channel（噪声信道的容量）；8 The noisy-channel coding theorem（噪声信道编码定理）
- Inference（推断）：9 Inference of parameters（参数推断）；10 Inference of parameters and models（参数与模型的推断）

左下角网址：www.inference.phy.cam.ac.uk/itprnn/

### p.2 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l10-p2](fig/l10/mgp00002.png)

<span style="color:#2471a3;">**[example]**</span> 例题引入页。绿色提示语：Please think about this question（请思考这道题）（Exercise 3.3, page 47（习题 3.3，第 47 页））。

上方黑底插图：一条水平观察窗，窗内散布大量青色小点（粒子衰变位置示意），横轴刻度从 1 到 20。

题目文字（彩色排印）转录：A source emits particles; they decay at locations exponentially distributed with lengthscale λ.（一个源发射粒子，粒子衰变的位置服从以 λ 为 lengthscale（尺度参数）的 exponential distribution（指数分布）。）Decays can be observed only if the location falls in a window $(x_{\min}, x_{\max}) = (a, b) = (1, 20)$.（只有当位置落在窗口 $(x_{\min},x_{\max})=(a,b)=(1,20)$ 内时，衰变才能被观测到。）$N$ decays are observed at locations $\{x_1,\ldots,x_N\}$. What is λ?（在位置 $\{x_1,\ldots,x_N\}$ 处观测到 $N$ 次衰变。λ 是多少？）

### p.3 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l10-p3](fig/l10/mgp00003.png)

同一例题页，顶部新增一行绿色设问：**Q:** How would you have solved this problem before you heard about likelihood functions and Bayes' theorem?（在你听说过 likelihood function（似然函数）与 Bayes' theorem（贝叶斯定理）之前，你会怎么解这道题？）

下方重复同一幅黑底衰变点图（横轴 1–20）与同一段题目文字：粒子位置服从尺度为 λ 的指数分布；只有落在窗口 $(a,b)=(1,20)$ 内的衰变可被观测；现于 $\{x_1,\ldots,x_N\}$ 观测到 $N$ 次衰变，求 λ。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题的关键陷阱在于"观测偏差"：指数分布的样本被硬性截断在窗口 (1,20) 内，直接拿样本均值当尺度参数会系统性偏大。在 Bertsekas 概率论里，指数分布是无记忆性的连续分布，密度既可写成速率型 $p(x)=\lambda e^{-\lambda x}$，也可写成尺度型 $p(x)=e^{-x/\lambda}/\lambda$——本讲义用后者，λ 是"尺度"而非"速率"，看图时务必换算清楚。likelihood function（似然函数）与概率密度用的是同一个公式 $p(x\mid\lambda)$，但角色互换：把函数看成参数 λ 的函数、数据视为固定，才叫似然。这也解释了为什么窗口截断必须写进似然：截断归一化因子 $Z(\lambda)=e^{-a/\lambda}-e^{-b/\lambda}$ 随 λ 变化，携带了"有多少概率质量漏出窗外"的信息。后面贝叶斯与最大似然两条路线都会反复用到这一点。

### p.4 〔Put data in bins, make histogram（把数据分箱，画直方图）〕

![l10-p4](fig/l10/mgp00004.png)

本页展示"前贝叶斯时代"朴素做法的第一步：把数据装进 bins（分箱）并画 histogram（直方图）。页面为两张黑底橙红色直方图：

- 左下图：横轴 0–22（数据位置），纵轴 0–90（计数），箱宽约 2。第一箱最高（按纵轴读约 80），第二箱约 50，第三箱约 57（略有回升），随后逐级下降到 20 附近的个位数。
- 右上图：同样横轴 0–22，但箱宽约 0.5，纵轴 0–20。直方图参差不齐，整体仍呈下降趋势，最高一箱约 19（位于 x≈2–3），末段出现一排高度为 1 的细箱。

〔本页为纯图示页：两张直方图截图，无其他文字〕

### p.5 〔Put data in bins, make histogram, and take log（分箱、画直方图，再取对数）〕

![l10-p5](fig/l10/mgp00005.png)

朴素做法第二步：对直方图取对数。两张黑底对数直方图：

- 左下图：纵轴为对数刻度（1 到 100），箱宽约 2；阶梯自约 80 逐级下降，末箱在 x=20 处竖直落到底。
- 右上图：纵轴对数刻度 1–100，箱宽约 0.5；曲线参差下降，右段（x≳10）出现大量落到底部的零计数箱（锯齿状竖线），横轴标注 10–22。

右下角两行文字：then 'fit a straight line'（然后"拟合一条直线"）；红色小字：(how do we handle zero counts?)（那零计数的箱怎么办？）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "分箱—取对数—拟合直线"本质上是手工作业的 maximum likelihood（最大似然）：对指数分布 $\log p(x)=-x/\lambda-\log\lambda+\text{常数}$，对数密度是一条斜率为 $-1/\lambda$ 的直线，读出斜率就得到估计。页面上红字点出的 zero counts（零计数）问题是这条流水线的痛点：$\log 0=-\infty$，无论丢弃、加 0.5 还是并箱，都是引入人为偏好的补丁，而且结果会随 bin（分箱）宽度改变。用 Bertsekas 概率论里的大数定律来看，每箱的频率依概率收敛到真实概率，但箱宽大了平滑过头、箱宽小了方差爆炸——典型的偏差—方差权衡。贝叶斯路线则完全绕开分箱：直接对全部原始数据点连乘似然，没有任何需要手调的自由参数，也天然回答了"各点该占多大权重"的问题。

### p.6 〔Other ideas（其他想法）〕

![l10-p6](fig/l10/mgp00006.png)

继续罗列"传统路线"能想到的办法（四个圆点条目）：

- Chi-squared（卡方）：minimize with respect to lambda（对 λ 求最小化）；also depends on bins（而且结果也依赖于分箱方式）
- Other measure of 'error' between theory and data（理论与数据之间"误差"的其他度量）
- Find how the data-mean is expected to vary with lambda（考察 data-mean（数据均值）在期望上如何随 λ 变化）
- Other 'estimators', depending on other data-properties（依赖数据其他性质的种种 estimator（估计量））

### p.7 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p7](fig/l10/mgp00007.png)

<span style="color:#2471a3;">**[definition]**</span> 贝叶斯答案第一页。先写出参数 λ 的 posterior（后验分布）：

$P(\lambda \mid \{x_n\}_{n=1}^{N}) = \dfrac{P(\{x_n\}_{n=1}^{N}\mid \lambda)\,P(\lambda)}{P(\{x_n\}_{n=1}^{N})}$

Or, making explicit the underlying assumptions -（或者，把底层假设显式写出来——）

```math
P(\lambda \mid \{x_n\}_{n=1}^{N}, \mathcal{H}_1)
  = \frac{P(\{x_n\}_{n=1}^{N}\mid \lambda, \mathcal{H}_1)\,P(\lambda\mid \mathcal{H}_1)}
         {P(\{x_n\}_{n=1}^{N}\mid \mathcal{H}_1)}
```

随后用大字排印给出四要素对照（原文以颜色标注各部分名称）：

```math
P(\text{Parameters}\mid \text{Data}, \mathcal{H}_1)
 = \frac{P(\text{Data}\mid \text{Parameters}, \mathcal{H}_1)\,P(\text{Parameters}\mid \mathcal{H}_1)}
        {P(\text{Data}\mid \mathcal{H}_1)}
```

其中左侧标注 POSTERIOR（后验），分子第一项标注 LIKELIHOOD（似然），分子第二项标注 PRIOR（先验），分母标注 EVIDENCE FOR $\mathcal{H}_1$（$\mathcal{H}_1$ 的 evidence（证据））。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页把贝叶斯定理的四件套一次性摆齐，值得用条件概率定义（你在 Bertsekas 概率论第一章学过的 $P(A\mid B)=P(A\cap B)/P(B)$）亲手推一遍：分子两项相乘恰是联合概率 $P(\text{Data},\text{Parameters}\mid\mathcal{H}_1)$，除以分母即完成归一化。evidence（证据）$P(\text{Data}\mid\mathcal{H}_1)$ 在"单一模型内推断参数"时只是让积分等于 1 的常数，可以不管；但本讲稍后做模型比较时，它恰恰是评分核心——因为它是在先验分布下对似然的平均。注意 MacKay 显式写出 $\mathcal{H}_1$：所有概率都以"模型假设"为条件，换一个假设（比如"分布是双指数混合"），整页公式形式不变、内容全变。这种"把假设写进条件里"的记账习惯，是贝叶斯方法可反驳、可审计的关键。

### p.8 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p8](fig/l10/mgp00008.png)

本页为现场演示用的空白页，仅右下角有两行黄色等宽字命令：

```text
cd ltp/octave/decay ; gnuplot
load 'gnu3'
```

（含义：进入目录 ltp/octave/decay 并启动 gnuplot，随后加载脚本 gnu3。）

### p.9 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p9](fig/l10/mgp00009.png)

右侧是一张编辑器截图（菜单栏 Buffers Files Tools Edit Search Mule Help），内容为 gnuplot 脚本，要点逐行转录：

- 注释：gnuplot commands to illustrate how simple Bayesian inference is（用 gnuplot 命令演示贝叶斯推断有多简单）
- 定义密度 P(x|lambda)：`p(x,λ) = exp(-x/λ) / Z(λ) / λ`，其中 `Z(λ) = exp(-a/λ) - exp(-b/λ)`，`a=1`，`b=20`（截断窗口内归一化的指数密度）
- 注释：The first plot illustrates the predictive distributions for different values of lambda（第一幅图画不同 λ 下的 predictive distribution（预测分布））：`plot [1:20][0:0.25] p(x,2) t 'P(x|lambda=2)', p(x,5) t 'P(x|lambda=5)', p(x,10) t 'P(x|lambda=10)'`
- 注释：Now imagine we receive data {x} = {3, 5, 12}（现在假设收到数据 {x} = {3, 5, 12}）；This is the definition of the likelihood function（这就是 likelihood function（似然函数）的定义）：`like(x) = p(3,x) * p(5,x) * p(12,x)`（变量 x 在此代表参数 λ）
- 注释：The next plot shows the three factors, P(x_n|lambda), in the likelihood function（下一幅图画似然函数中的三个因子）：`set logscale x`；`set xlabel "lambda"`；`plot [0.3:140] p(3,x) t "P(x=3|lambda)", p(5,x) t "P(x=5|lambda)", p(12,x) t "P(x=12|lambda)"`
- 注释：Finally, plot the likelihood（最后画出似然函数本身）：`plot [0.3:140] like(x) t 'P({x|lambda}' w l 5`

状态栏：gnu4b （Perl）--L35--All--；Wrote /home/mackay/ltp/octave/decay/gnu4b。

下方手绘示意图：一条横线代表观察窗，线上画三个蓝色小方块，位置分别标注 3、5、12；左端红字 a=1，右端红字 b=20。

> <span style="color:#7f8c8d;">旁注：手绘部分是 MacKay 在投影上补画的观察窗示意——窗口 [a,b]=[1,20]，三个观测衰变位于 x=3, 5, 12。</span>

### p.10 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p10](fig/l10/mgp00010.png)

同一 gnuplot 演示，左上叠加出第一幅运行结果：黑底曲线图，图例为 P(x|lambda=2)（红）、P(x|lambda=5)（橙）、P(x|lambda=10)（黄），横轴 x 为 2–20，纵轴 0–0.5。三条截断指数密度都在 x=0 处最高并按指数衰减：λ 越小衰减越快（λ=2 最陡），λ 越大尾部越平缓。右侧 gnuplot 脚本截图不变；下方仍是手绘窗口示意（三个方块标 3、5、12；a=1；b=20）。

### p.11 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p11](fig/l10/mgp00011.png)

继续同一演示：在三条预测分布曲线上叠加三条竖直线，标出数据点位置：x=3（青色竖线）、x=5（蓝色竖线）、x=12（品红竖线）。这样能直观看到"数据点落在哪个 λ 的分布之下更可能"。右下角仍是手绘窗口示意（a=1；b=20；三个观测 3、5、12）与 gnuplot 脚本截图。

### p.12 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p12](fig/l10/mgp00012.png)

第二幅运行结果：似然函数的三个因子。黑底图，横轴为对数刻度的 lambda（1、10、100），纵轴 0–0.2：

- P(x=3|lambda)（青色）：先升后降的单峰，峰值约 0.18，峰位在 λ≈2–3；
- P(x=5|lambda)（蓝色）：峰值约 0.095，峰位约 λ≈5；
- P(x=12|lambda)（品红）：随 λ 增大单调上升并趋于约 0.05 的平台——数据点 12 相对越大，越"偏爱"大的 λ。

图中另有两条竖直参考线（黄/橙色，约在 λ=3 与 λ=5 处）。

### p.13 〔The answer using Bayes's theorem（用贝叶斯定理给出的答案）〕

![l10-p13](fig/l10/mgp00013.png)

第三幅结果（左上）：三个因子改用暖色画在同一幅图里，横轴 lambda 为对数刻度（1、10、100），纵轴 0–0.2：P(x=3|lambda)（红橙，峰约 0.18）、P(x=5|lambda)（橙，峰约 0.09）、P(x=12|lambda)（黄，缓慢升到约 0.055 的平台）。

第四幅结果（左下）：似然函数本身 P({x}|lambda)（青色）：单峰曲线，峰值约 0.0003，峰位在 λ≈3–4——它正是上面三个因子在同一 λ 处的乘积。横轴仍为对数 lambda。

右侧 gnuplot 脚本截图与手绘窗口示意（3、5、12；a=1；b=20）保持不变。

### p.14 〔Bayesian answer, alternate data set（贝叶斯答案：换一组数据）〕

![l10-p14](fig/l10/mgp00014.png)

换一组更小的数据 {x} = {1.7, 1.5, 2.0}（三个点都挤在窗口左端）。左侧两幅图：

- 上图：P({x}|lambda)（青色），横轴 lambda 对数刻度 0.1–100；单峰，峰值约 0.125，峰位约 λ≈1。
- 下图：同一似然，纵轴改为对数刻度（1e-14 到 1），显示似然跨越十几个数量级：λ→0.1 处骤降到 1e-14 以下，大 λ 处缓慢衰减。

右侧红色手写：{x} = {1.7, 1.5, 2.0}；窗口横线上三个蓝色小方块挤在左端；a=1（左）、b=20（右）。下方 gnuplot 片段：`set title "{x} = {1.7, 1.5, 2.0}"`；注释 # This is the definition of the likelihood function（这是似然函数的定义）；`like(x) = p(1.7,x) * p(1.5,x) * p(2,x)`。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 对比第 13 页与第 14 页能看出数据如何塑造不确定性：数据 {3,5,12} 三个点张得开，似然峰宽、且偏向较小的 λ；数据 {1.7,1.5,2.0} 挤在一起，似然峰反而又高又窄地压在 λ≈1。这不是巧合——N 个独立同分布样本的对数似然是 N 项之和，按 Bertsekas 概率论里的大数定律，其随机涨落相对均值按 $1/\sqrt{N}$ 缩小，峰随 N 增大而变窄（这也是 AEP（渐近均分性）的连续版直觉：典型样本越来越集中在同一形态附近）。贝叶斯的输出是整个后验分布而非单点估计：三个点都远离 b=20 一端时，"概率质量漏出右边界"的可能性自动压低了大的 λ，所以峰位比朴素样本均值更小。若只报告一个数，就把"我们到底有多确定"这层信息全丢掉了。

### p.15 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l10-p15](fig/l10/mgp00015.png)

回到最初的例题页：同一幅黑底衰变点图（横轴 1–20）与同一段题目文字（粒子位置服从尺度 λ 的指数分布；仅窗口 $(a,b)=(1,20)$ 内可观测；于 $\{x_1,\ldots,x_N\}$ 观测到 $N$ 次衰变；求 λ）。

底部新增一行绿色大字：+ What about the possibility that the distribution is a mixture of two exponentials?（那么，分布有没有可能是两个指数分布的 mixture（混合）呢？）——由此引出接下来的混合模型演示。

### p.16 〔（无标题的现场演示页）〕

![l10-p16](fig/l10/mgp00016.png)

<span style="color:#2471a3;">**[example]**</span> 现场演示页：页面大部分空白，底部为黑色粗体命令与说明文字：

cd /home/mackay/inference（进入演示目录）
octave2.1（启动 Octave 2.1）
RUNME（运行脚本 RUNME）
32x32x256 hypotheses（32×32×256 个假设）

> <span style="color:#7f8c8d;">旁注：本页之后十几幅图即为该 octave 脚本逐幅画出的输出；结合下文，"32×32×256"对应两个对数参数各扫 32 格 × 256 种 8 位标签串（推断）。</span>

### p.17 〔Data（数据）〕

![l10-p17](fig/l10/mgp00017.png)

演示第一幅图：标题 Data（数据）。黑底白框坐标图，横轴 x 为 0–1.6；四个青色 × 号贴在横轴上：约 x=0.2、0.9、1.05、1.5（纵轴无标注——这是一维数据，位置即全部信息）。

### p.18 〔likelihood function（似然函数）〕

![l10-p18](fig/l10/mgp00018.png)

第二幅图：标题 likelihood function（似然函数）。黄绿色单峰曲线：横轴 lambda 为 0–10，纵轴 0–0.03；峰值约 0.025，峰位约 λ≈1（单指数模型对这 4 个点拟合的结果），右侧长尾缓慢衰减。

### p.19 〔likelihood function（似然函数）〕

![l10-p19](fig/l10/mgp00019.png)

同一似然函数改画在对数横轴上：lambda 从 0.01 到 100（刻度 0.01、0.1、1、10、100），纵轴仍 0–0.03。峰值约 0.025 位于 λ≈1；λ<0.1 区域似然迅速降到 0，λ>10 后缓慢趋零——对数轴同时展示了峰两侧"宽度"的量级。

### p.20 〔maximum likelihood distribution（最大似然分布）〕

![l10-p20](fig/l10/mgp00020.png)

第三幅图：标题 maximum likelihood distribution（最大似然分布）。绿色曲线是代入最大似然 λ 后的指数密度（在 x=0 处约 1.1，随后按指数衰减，x≈7 后贴近 0），横轴 x 为 0–16；四个青色 × 为原数据点（约 0.2、0.9、1.05、1.5），都落在曲线下方的低处。

### p.21 〔maximum likelihood distribution（最大似然分布）〕

![l10-p21](fig/l10/mgp00021.png)

同一最大似然曲线（绿色，x=0 处约 1.1）上叠加一个蓝色矩形：箱 [0,2]、高 0.5——即把 4 个数据点全放进一个宽 2 的箱时的经验直方图；箱内还有两条竖直蓝线（约 x=0.7 与 0.75，为备选的箱边界）。青色 × 数据点贴在横轴上。

### p.22 〔maximum likelihood distribution（最大似然分布）〕

![l10-p22](fig/l10/mgp00022.png)

换用更大的数据集再演示：绿色最大似然曲线起点降到约 0.57（对应更大的 λ），横轴 x 仍为 0–16、纵轴 0–0.6。叠加蓝色直方图（箱宽 1）：可见箱高约 0.167、0.1、0.135、0.033、0.033，远处 [11,12] 箱约 0.033。大量青色 × 数据点密集在 0–3，另有一个离群点约 x≈11.5。直方图与绿色曲线明显错位——单指数模型在这种数据上力不从心。

### p.23 〔Data（数据）〕

![l10-p23](fig/l10/mgp00023.png)

标题 Data（数据）。黑底白框坐标图，横轴 x 为 0–8；八个青色 ×（其中几个在 0–0.2 内重叠）：约 0.02、0.05、0.1、0.15、0.55、2.2、3.05、7.1。这就是第 35 页列出的"数据集 3——8 个点"。

### p.24 〔likelihood function（似然函数）〕

![l10-p24](fig/l10/mgp00024.png)

标题 likelihood function（似然函数）。黄色单峰曲线：横轴 lambda 为 0–10，纵轴 0–6e-06（刻度间隔 1e-06）；峰值约 5.6e-06，峰位 λ≈1.6，右侧长尾衰减。数值极小是因为 8 个密度值（各小于 1）连乘。

### p.25 〔likelihood function（似然函数）〕

![l10-p25](fig/l10/mgp00025.png)

同一似然函数改画在对数横轴上：lambda 从 0.01 到 100，纵轴仍 0–6e-06。峰值约 5.6e-06 位于 λ≈1.6，两侧对称地在对数尺度上收窄——峰的宽度正是参数不确定度的直观体现。

### p.26 〔maximum likelihood distribution（最大似然分布）〕

![l10-p26](fig/l10/mgp00026.png)

标题 maximum likelihood distribution（最大似然分布）。绿色曲线在 x=0 处约 0.6（对应 λ̂≈1.66 的指数密度，与第 35 页 optimized lambda = 1.6637 一致），随 x 指数衰减，x≈10 后贴近 0；八个青色 × 数据点位于底部。

### p.27 〔maximum likelihood distribution（最大似然分布）〕

![l10-p27](fig/l10/mgp00027.png)

同一页叠加蓝色直方图（箱宽 1）：[0,1] 箱高约 0.625（5 个点），[2,3] 箱约 0.125（1 个点），[3,4] 箱约 0.125（1 个点），[7,8] 箱约 0.125（1 个点）。绿色最大似然曲线叠加其上：曲线在 [0,1] 箱处明显低于直方图，在 1–2 处又偏高——单指数模型拟合不佳的直观证据。

### p.28 〔P(Data | lambda1, lambda2, k1..kN = 00000111)（给定标签串 00000111 时数据的条件概率）〕

![l10-p28](fig/l10/mgp00028.png)

三维线框曲面图：标题 P(Data | lambda1, lambda2, k1..kN = 00000111)。两条水平轴分别为 log(lambda1) 与 log(lambda2)，范围均为 −5 到 5；竖轴刻度 0 到 4e-05。黄色曲面上只有一个尖锐高峰（位于平面中部偏右），其余区域近乎平坦。k1..kN = 00000111 是 8 个数据点的 component label（分量标签）串：一个 8 位的 0/1 串（含 5 个 0、3 个 1），约定每个点归入哪个指数分量。

### p.29 〔P(Data | lambda1, lambda2, k1..kN = 11111111)（给定标签串 11111111 时数据的条件概率）〕

![l10-p29](fig/l10/mgp00029.png)

同样式的三维线框曲面：标题中 k1..kN = 11111111（8 位全 1）。竖轴 0 到 6e-06。曲面沿某一参数方向整体抬成"平台/山脊"状，并在 log(lambda1)≈0 附近出现一道深槽（绿色陡壁）。与上一页对比：全 1 标签串的概率峰值（约 6e-06）远小于 00000111 的峰值（约 4e-05）；且标签全归一个分量时，似然对另一个分量参数几乎不敏感，于是沿该方向形成平台。

### p.30 〔Marginal likelihood of lambda1 and lambda2 - P(Data | lambda1,lambda2)（λ1 与 λ2 的边缘似然）〕

![l10-p30](fig/l10/mgp00030.png)

三维线框曲面：标题 Marginal likelihood of lambda1 and lambda2 - P(Data | lambda1,lambda2)——即对 256 种标签串求和后、只剩两个连续参数的 marginal likelihood（边缘似然）。竖轴 0 到 0.0003，两轴仍为 log(lambda1)、log(lambda2)（−5..5）。黄色曲面出现两个并排的尖峰（较高者约 0.0003），其余区域近平：两个峰对应"小点归陡分量、大点归缓分量"的两种等价标记方式。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第 28–30 页展示了"标签串"如何进入计算：8 个数据点各有 0/1 两种归属，共 $2^8=256$ 种标签串——MacKay 把它们当作二进制整数枚举，这正是你在 CSAPP 第 2 章学的位向量表示：一个 8 位串就是一个 0–255 的整数，第 16 页的 "32x32x256 hypotheses" 即两个对数参数各扫 32 格 × 256 种标签。对每个固定标签串，似然只是"两组数据各自 fit 一个指数"的乘积（第 28 页单峰；全 1 串退化成单分量、对另一个 λ 形成山脊，第 29 页）。把 256 个曲面逐点相加，就得到第 30 页的双峰 marginal likelihood（边缘似然）——混合模型等于"考虑了所有分法"再加权。注意枚举是指数复杂度 $2^N$，与你在 6.006 里分析子集枚举的结论一致；N 大时必须改用 EM 等近似算法，精确求和只在小 N 时可行。

### p.31 〔（纯图形页：双峰彩色曲面）〕

![l10-p31](fig/l10/mgp00031.png)

一张三维彩色网格曲面（无文字、无坐标标注）：深蓝色的平坦基面上耸立两座尖峰，峰顶为红色，向下经黄、绿过渡到蓝；两峰一大一小、左右并排。〔本页为纯图示页（无文字内容）〕

### p.32 〔（纯图形页：双峰等高线图）〕

![l10-p32](fig/l10/mgp00032.png)

一张黑底等高线图（无坐标轴标注）：两组同心等高线环——左上一组、右下一组，颜色由外向内从蓝经青、绿、黄、橙过渡到红色中心，表示曲面两个局部极大的"山顶"。〔本页为纯图示页（无文字内容）〕

### p.33 〔Posterior distribution of the labels（各标签串的后验分布）〕

![l10-p33](fig/l10/mgp00033.png)

标题 Posterior distribution of the labels（标签串的后验分布）。散点图：横轴 k1..kN 为 0–250（把 8 位标签串读作二进制整数），纵轴 P(k1..kN | Data) 为 0–0.25。绿色方点：最高两个点约 0.22；第二梯队若干点约 0.08；其余大量方点贴着 0（≤0.02）。后验质量高度集中在极少数标签串上——数据几乎自己"分好了组"。

### p.34 〔ML model with two lambda's（带两个 λ 的最大似然模型）〕

![l10-p34](fig/l10/mgp00034.png)

标题 ML model with two lambda's（用两个 λ 的最大似然模型拟合）。纵轴标注 P(x | lambda1*, lambda2*)，横轴 x 为 0–16。图中：绿色混合密度曲线（x=0 处超过 1，长尾衰减到 x≈10 处贴近 0）；品红色陡峭分量曲线（低 λ 分量，在 x≈2 内衰减殆尽）；x<0.3 处另有一小段白色直线元素。青色 × 数据点位于底部（约 0.05–0.2 挤在一起、0.55、2.2、2.9、7.0）。

### p.35 〔Data set 3 - 8 points（数据集 3 —— 8 个点）〕

![l10-p35](fig/l10/mgp00035.png)

<span style="color:#2471a3;">**[example]**</span> 数值结果汇总页。Data = 0.64 0.016 0.100 0.050 3.09 2.14 0.200 7.10（8 个数据点）。

- Model 1（模型 1，单指数）：optimized lambda = 1.6637（优化的 λ）；ML_model1 = 5.6254e-06（最大似然值）；Evidence1 = 5.4555e-07（证据）。
- Model 2（模型 2，双指数混合）：Evidence2 = 1.3994e-05（证据）；ML = 2.5026e-04（最大似然值）；tau1ml = 0.080025 ; tau2ml = 2.8289（两个分量的最大似然 τ）；k1..kN optimized (optimal labels) = 01110010（优化的 8 位标签串，即 optimal labels（最优标签））；EvidenceRatio = 25.651（证据比）；PosteriorProbOfH2 = 0.96248（H2 的后验概率）；PosteriorProbOfH1 = 0.037522（H1 的后验概率）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页数字值得逐行读。模型 1 里 ML=5.6254e-06 而 Evidence1=5.4555e-07，差约一个数量级：证据是对 λ 的先验平均，后验峰的宽度（即 Occam factor（奥卡姆因子））决定它比最大似然小多少——参数不确定性越大，惩罚越重。模型 2 的 ML 约是模型 1 的 44 倍（2.5e-04 对 5.6e-06），但证据只高出 25.651 倍，同样是复杂度惩罚在起作用。由于两个模型先验各取 0.5，后验概率比就等于证据比：0.96248 对 0.037522，恰是 25.651:1 的归一化。于是"该不该用两个指数"不再靠拍脑袋，而是一个可计算的贝叶斯模型比较；你在 Strang 线代里见过的"用子空间维数衡量模型自由度"，在这里对应"参数体积决定奥卡姆因子"。最优标签串 01110010 把 8 个点分成两组：小点归 τ≈0.08 的陡分量，大点归 τ≈2.83 的缓分量。

### p.36 〔Montage of demo outputs（演示输出汇总拼图，本页无总标题）〕

![l10-p36](fig/l10/mgp00036.png)

一页汇总截图（五幅小图拼贴；注意本页参数记号改用 tau）：

- 左上小图：maximum likelihood distribution（最大似然分布）——绿色衰减曲线与青色 × 数据点（同第 26 页）。
- 左中小图：ML model with two tau's（双 τ 最大似然模型）——绿色混合曲线、品红陡分量与青色 × 数据点（同第 34 页）。
- 左下小图：Posterior distribution of the labels（标签串后验分布）——横轴 0–300，绿色方点，最高的两点约 0.21。
- 右上曲面：P(Data|tau1, tau2, c1..cN = 00000111)——黄色单峰线框曲面（同第 28 页，两轴 −5..5）。
- 右下曲面：Marginal likelihood of tau1 and tau2 - P(Data|tau1,tau2)——橙红色双峰线框曲面（同第 30 页）。

### p.37 〔Clustering（聚类）〕

![l10-p37](fig/l10/mgp00037.png)

<span style="color:#2471a3;">**[section]**</span> 新话题：Clustering（聚类）。子图标题 K means clustering（K 均值聚类）。黑底散点图，横轴 0–10，纵轴 0–8，数据分为四簇，每簇中心用带圈星号标出：

- 白色星号中心（约 (2, 2.4)），周围是白色 × 号点簇；
- 绿色星号中心（约 (3, 4.9)），周围是绿色 + 号点簇；
- 蓝色星号中心（约 (7.1, 7.4)），周围是蓝色方框点簇；
- 橙色星号中心（约 (7.6, 3.5)），周围是橙色菱形点簇。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> K-means（K 均值）可以看成上一节概率混合模型的"硬分配"极限：每个点被强行归给最近的中心（相当于令标签后验只能取 0/1），然后中心更新为簇内均值，两步交替即 Lloyd 算法。用 6.006/CLRS 的眼光看，它是一个局部搜索式迭代算法：每轮目标函数（簇内平方误差）单调不增，但只保证收敛到局部极小，初值不同结果可能不同，所以实践中要多次随机重启。与第 33 页对比很有启发：贝叶斯版允许标签"软"分配（一个点按概率属于两个分量），并通过 evidence（证据）自动惩罚过多的分量；K 均值则必须事先指定 K，且平方误差会放大离群点的影响。聚类数未知时，贝叶斯模型比较提供了一种原则化的选 K 方式，这正是本讲把聚类放在贝叶斯推断之后讲的原因。

### p.38 〔Clustering（聚类）〕

![l10-p38](fig/l10/mgp00038.png)

继续聚类话题：两栏各 12 幅小 spectrogram（语谱图）。每幅小图横轴 Time (s)（时间，秒）0–0.5，纵轴 Frequency (kHz)（频率，千赫兹）0–6；图中黄–红–蓝表示能量强弱（红为强）。左栏 12 幅旁有红色大字 One（"1"），右栏 12 幅旁有绿色大字 Zero（"0"）——分别是说单词 "one" 与 "zero" 的 12 次录音的语谱图。页面下方中间另放两幅较大的示例语谱图。聚类算法的目标正是把这些"长得像"的语谱图自动归到同一个词。

### p.39 〔Recommended homework（推荐课后作业）〕

![l10-p39](fig/l10/mgp00039.png)

- Noisy channels - Chapters 8, 9, 10 (10.1-10.4 only)（噪声信道——第 8、9、10 章，仅 10.1–10.4 节）
  - Exercises 9.17 (p155); 10.12 (172); 15.12 (235)（习题 9.17（第 155 页）、10.12（172）、15.12（235））
  - and (if you want more practice) 15.11, 15.13, 15.15（以及（如果想多练）15.11、15.13、15.15）
- Invent a channel to pose to your colleagues:（自己发明一个信道考考同学：）'what's the capacity of _this_?'（"这个信道的 capacity（容量）是多少？"）

绿色居中文字：The reading associated with the current lectures is Chapters 3, 21 (especially sec 21.2), and 22 (especially sec 22.1), and 27.（与本讲相关的阅读材料为第 3、21（尤其 21.2 节）、22（尤其 22.1 节）与 27 章。）

蓝色粗体：Other recommended exercises are listed on handout 2.（其他推荐习题见讲义发件 2。）

底部蓝色等宽网址：www.inference.phy.cam.ac.uk/itprnn/



