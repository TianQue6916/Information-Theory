> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 l9 · 行内双语视觉转录版 · 原图见 fig/l9/</span>

### p.1 〔Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）〕

![l9-p1](fig/l9/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> 课程标题页：Information theory, pattern recognition, and neural networks（信息论、模式识别与神经网络）。页面左侧是一幅圆形分形树装饰图：绿色树干与分支自圆心向外生长，末梢挂着蓝、粉两色的小圆圈并向圆盘边缘递归细分〔本页左侧为纯手绘图示〕。右侧为本课程大纲（outline，大纲）：

- 1 噪声信道编码（Noisy-channel coding）
- <span style="color:#2471a3;">**[section]**</span> 信源编码（Source coding），即数据压缩（Data compression）：
  - 2 信息量（Information content）与熵（entropy）
  - 3 典型性（Typicality）与信源编码定理（source coding theorem）
  - 4 符号码（Symbol codes）
  - 5 符号码与算术编码（Arithmetic coding）
- <span style="color:#2471a3;">**[section]**</span> 噪声信道编码（Noisy-channel coding）：
  - 6 推断（Inference）与噪声信道的信息度量（Information measures for noisy channels）
  - 7 噪声信道的容量（Capacity of a noisy channel）
  - 8 噪声信道编码定理（The noisy-channel coding theorem）
- <span style="color:#2471a3;">**[section]**</span> 推断（Inference）：
  - 9 参数推断（Inference of parameters）

页底网址：www.inference.phy.cam.ac.uk/itprnn/

### p.2 〔Capacity（信道容量）〕

![l9-p2](fig/l9/mgp00002.png)

<span style="color:#2471a3;">**[definition]**</span> 一个信道（channel）的容量（Capacity）是：在所有输入分布（input distribution）$P(x)$ 上，互信息（mutual information）的最大值：

```math
C \;\equiv\; \max_{\mathcal{P}_X}\, I(X;Y)
```

达到该最大值的分布 $\mathcal{P}_X^*$ 称为最优输入分布（optimal input distribution）。

右侧配图两张：上图是二元对称信道（binary symmetric channel）示意，输入 $x\in\{0,1\}$、输出 $y\in\{0,1\}$，直通箭头 $0\to0$、$1\to1$ 标注 $1-f$，交叉箭头（翻转）标注 $f$；下图是一张大通道图，左右两列各排列字母 A–H、（竖排省略号）、Y、Z、− 共 27 个符号，两列之间画满交叉箭头表示噪声造成的符号混淆，其中 G→G 一条箭头加粗，示意"正确到达"的那个。

<span style="color:#2471a3;">**[theorem]**</span> Shannon 噪声信道编码定理（Shannon's noisy channel coding theorem）：可靠的（几乎无差错的，virtually error-free）通信（communication）在码率（rate）不超过 $C$ 时是可能的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 容量定义 $\max_{\mathcal{P}_X}I(X;Y)$ 可以完全用你熟悉的期望语言读懂：互信息是对数似然比 $\log\frac{P(y\mid x)}{P(y)}$ 在联合分布下的期望，正如熵（entropy）$H(X)=E[\log\frac{1}{P(x)}]$ 是自信息（self-information）的期望——"信息量＝随机变量函数的期望"，这是概率论处理信息量的统一姿势（锚点：概率论·熵=随机变量的期望）。最大化要遍历所有输入分布，是单纯形上的约束优化：对二元对称信道，把 $I$ 写成 $p_0$ 的函数后是凹函数（concave），一阶条件给出 $p_0=1/2$。判定凹性所用的工具，正是你在 Strang 线代里判断二次型正定/负定那套方法的推广，Jensen 不等式（Jensen inequality）在这类证明中反复出现。最后强调：容量只由信道矩阵 $Q$ 决定，与信源无关，它是信道自身的"物理常数"，后面的两条编码定理都围绕它展开。

### p.3 〔Binary erasure channel（二元擦除信道）〕

![l9-p3](fig/l9/mgp00003.png)

<span style="color:#2471a3;">**[example]**</span> 本页是一张信道图加一个矩阵：输入 $x\in\{0,1\}$，输出 $y\in\{0,?,1\}$，其中 $?$ 表示"擦除"。转移箭头标注：$0\xrightarrow{0.9}0$（以 0.9 正确传出 0）、$0\xrightarrow{0.1}?$、$1\xrightarrow{0.1}?$、$1\xrightarrow{0.9}1$。信道矩阵（channel matrix）为

```math
\mathbf{Q}=\begin{bmatrix}0.9 & 0\\ 0.1 & 0.1\\ 0 & 0.9\end{bmatrix}
```

（三行对应输出 0、?、1，两列对应输入 0、1。）页面中央大字提问：容量（capacity）是多少？（What is the capacity?）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 二元擦除信道（binary erasure channel）的关键是区分了"错"与"丢"：输出要么正确（概率 $1-f=0.9$），要么变成显式的 $?$（概率 $f=0.1$），接收方永远知道自己哪里没收到信息。它的容量可以当场算出：$C=1-f=0.9$ 比特/次使用，因为互信息 $I(X;Y)=H(X)-H(X\mid Y)$ 中被擦除的部分恰好以概率 $f$ 整体损失，不残留半点信息。用 CSAPP 的视角看，这里传输的就是原始比特（bit），擦除对应网络传输丢包（锚点：CSAPP·二进制表示与位运算）；若发 $k$ 个数据包再配 $r$ 个用异或（XOR）算出的校验包，只要丢失数不超过 $r$ 就能完全恢复——这正是奇偶校验码（parity-check code）的思想。对照 6.006 里哈希均匀随机的"以概率换确定性"，擦除模型把"不确定性"显式地摆在了输出字母表里，所以格外好分析。

### p.4 〔Feedback（反馈）〕

![l9-p4](fig/l9/mgp00004.png)

本页是两幅 Claude Shannon 的黑白照片：左为其年轻时的肖像照；右为晚年坐在黑板前、手持粉笔的照片，黑板上画着一条递减曲线，纵轴标注似为 $E(r)$，横轴标注〔无法辨认〕。照片下方是红色大字（模拟 Shannon 口吻的调侃）：

「反馈（Feedback）？哼，谁需要反馈？直接用随机码（random code）就行了！」

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这句红字其实是 Shannon 证明核心思想的漫画化：要证明"存在好码"，他从全体码本中均匀随机抽一个码本（random code），证明"平均意义上错误概率很小"，于是必然存在某个具体的好码本——这正是 6.006 里学过的概率方法（probabilistic method）：先证随机样本以正概率满足要求，再断言好结构存在。它与哈希（hash）的思想同构：逐个防范固定的"坏输入"很难，但换一个随机哈希函数，任意固定输入的碰撞概率都被压低，期望意义下一切变好（锚点：6.006·哈希与均匀随机）。至于反馈（feedback）本身：对无记忆信道，反馈并不能提高容量 $C$，它能做的是简化编解码器的实现，或在擦除类信道上用重传（ARQ）逼近容量。Shannon 的照片配这句话，是在提醒大家"随机码＋典型集译码"已经足够，不必迷信反馈。

### p.5 〔Inferring the parameters of a Gaussian（推断高斯分布的参数）〕

![l9-p5](fig/l9/mgp00005.png)

本页是一张黑底彩色曲线图：横轴从 $-6$ 到 $6$（间隔 2），纵轴从 $0$ 到 $0.8$（间隔 0.1）。图中共 7 条高斯（Gaussian）密度曲线，右上角图例（legend）以 $P(x\mid\mu,\sigma)$ 记法给出参数：

- $P(x\mid 3,\,1.6)$（红橙色，峰在 $x=3$，峰高约 $0.25$）
- $P(x\mid 2,\,0.5)$（橙色，峰在 $x=2$，峰高约 $0.8$，全图最高最窄）
- $P(x\mid 1,\,1.2)$（黄色，峰在 $x=1$，峰高约 $0.33$）
- $P(x\mid 0,\,0.8)$（绿色，峰在 $x=0$，峰高约 $0.5$）
- $P(x\mid -1,\,1.5)$（青色，峰在 $x=-1$，峰高约 $0.27$）
- $P(x\mid -2,\,0.7)$（蓝色，峰在 $x=-2$，峰高约 $0.57$）
- $P(x\mid -3,\,2)$（品红色，峰在 $x=-3$，峰高约 $0.2$，最矮最宽）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页把"推断（inference）"具象成一族候选模型：每条曲线是一个具体参数 $(\mu,\sigma)$ 下的高斯密度 $P(x\mid\mu,\sigma)$，共 7 个候选。你可以直接用概率论知识验证这张图：高斯密度的峰值是 $1/(\sigma\sqrt{2\pi})$，所以橙色（$\sigma=0.5$）峰高约 0.8、绿色（$\sigma=0.8$）约 0.5、品红（$\sigma=2$）约 0.2，与公式严格吻合；峰越宽必越矮，这正是密度归一化（曲线下面积恒为 1）的体现。拿到数据后，似然（likelihood）等于把每个观测点的密度值连乘，最大似然估计（maximum likelihood）就是挑出"最能解释数据"的那条曲线；而贝叶斯派会给参数一个先验（prior），用 Bayes 定理算后验（posterior）。你在 Bertsekas 概率课里学过的估计量一致性会告诉你：数据越多，似然峰越尖锐，两种哲学的答案渐趋重合。MacKay 用这张图预热下一页更真实的科研推断问题。

### p.6 〔cd itp/gaussian; gnuplot（切换到 itp/gaussian 目录并启动 gnuplot）〕

![l9-p6](fig/l9/mgp00006.png)

本页几乎全空，是现场演示（demo）占位页：底部大标题为命令 `cd itp/gaussian; gnuplot`，绿色分隔线下有一行小字 `load 'DEMO'`（加载演示脚本）。

### p.7 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l9-p7](fig/l9/mgp00007.png)

绿色提示：请思考这个问题（Please think about this question）（Exercise 3.3, page 47，教材第 47 页习题 3.3）。

图：黑底散点图（scatter plot），横轴刻度 $1$ 到 $20$，纵轴无标注；约两百余个青色小点，左端密集、向右逐渐稀疏（呈指数衰减式的散布）。

题目正文：一个源（source）发射粒子；粒子衰减（decay）的位置服从以长度尺度（lengthscale）$\lambda$ 为参数的指数分布（exponential distribution）。只有当位置落在窗口（window）$(x_{\min},x_{\max})=(a,b)=(1,20)$ 内时，衰减才能被观测到。观测到 $N$ 次衰减，位置为 $\{x_1,\ldots,x_N\}$。问：$\lambda$ 是多少？

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题最容易踩的坑是忽略"窗口（window）"：粒子位置服从指数分布，但你只能观测到落在 $(1,20)$ 内的衰减，所以单个观测的似然不是密度 $\frac{1}{\lambda}e^{-x/\lambda}$ 本身，而是条件密度 $\frac{e^{-x/\lambda}}{\lambda\,(e^{-1/\lambda}-e^{-20/\lambda})}$——分母来自条件概率 $P(1\le x\le 20)$ 的计算，这正是概率论里"截断/删失数据（censored data）"的标准处理（锚点：概率论·条件概率与截断分布）。另外别忘了 $N$（观测到的衰减总数）本身也携带 $\lambda$ 的信息：单位时间内衰减越多，$\lambda$ 越小。指数分布的无记忆性（memoryless property）你在概率论里证过，它意味着窗口起点不改变分布形状，只改归一化常数。MacKay 把它留作习题 3.3，希望你先对对数似然求导得到最大似然解，稍后再用贝叶斯方法重做一遍并比较两者。

### p.8 〔Inferring parameters in science experiments（科学实验中的参数推断）〕

![l9-p8](fig/l9/mgp00008.png)

绿色大字提问：Q:（问：）在你听说似然函数（likelihood function）与 Bayes 定理（Bayes' theorem）之前，你会怎么解决这个问题？

下方重复第 7 页的同一张黑底散点图（横轴 1–20，青点左密右疏）与同一段题目文字（源发射粒子、位置服从长度尺度 $\lambda$ 的指数分布、只可观测窗口 $(x_{\min},x_{\max})=(a,b)=(1,20)$ 内的衰减、观测到 $N$ 次衰减于 $\{x_1,\ldots,x_N\}$、求 $\lambda$）。

### p.9 〔Recommended homework（推荐作业）〕

![l9-p9](fig/l9/mgp00009.png)

- <span style="color:#2471a3;">**[section]**</span> 噪声信道（Noisy channels）——阅读第 8、9、10 章（第 10 章仅 10.1–10.4 节）：
  - 习题（Exercises）9.17（第 155 页）；10.12（第 172 页）；15.12（第 235 页）
  - 以及（想多练的话）15.11、15.13、15.15
- <span style="color:#2471a3;">**[section]**</span> 自己发明一个信道（channel）去考同学：「这个信道的容量（capacity）是多少？」

绿色文字：与本讲相关的阅读是第 3、21 章（尤其是 21.2 节），22 章（尤其是 22.1 节），以及 27 章。

蓝色粗体：其他推荐习题（Other recommended exercises）列在讲义材料 2（handout 2）上。

页底网址：www.inference.phy.cam.ac.uk/itprnn/

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这页作业设计值得说道：算信道容量通常分两步——先猜最优输入分布（optimal input distribution），再验证它确实最大。对称信道（如二元对称信道、二元擦除信道）凭对称性直接猜均匀分布即可；不对称信道（如 Z 信道）就要联立方程求解，验证工具是 $I$ 对输入分布的凹性（concavity）。这个"猜想＋证明"的双步结构与 6.006 里"设计算法＋论证正确性"完全同形，Jensen 不等式是这里最常用的引理（锚点：6.006·算法正确性论证）。"自己发明一个信道考同学"是极好的练习：你必须同时当出题人与审题人，检查信道矩阵每行和为 1、容量可算、答案干净。阅读部分覆盖第 3、21、22、27 章，与课程从信道编码转向推断的节奏对应。
