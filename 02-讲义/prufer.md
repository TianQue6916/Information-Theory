> <span style="color:#7f8c8d;">Source: MacKay《Information Theory, Inference, and Learning Algorithms》课程手写讲义 prufer 补充材料 · 行内双语视觉转录版 · 原图见 fig/prufer/</span>

### p.1 〔Counting Trees（计数树）〕

![prufer-p1](fig/prufer/mgp00001.png)

<span style="color:#2471a3;">**[lecture]**</span> <span style="color:#c0392b;">**Counting Trees（计数树）**</span>

署名：David MacKay FRS（英国皇家学会会士 David MacKay），Department of Physics（物理系），University of Cambridge（剑桥大学）。

课程网址：`www.inference.phy.cam.ac.uk`

页面左侧配图：一幅装饰性图形——一张由绿色节点与绿色边构成的大型 tree（树）状网络，节点交替画成圆形与方形，整棵树从中心向四周不断分叉，被整体收拢在一个圆盘之内；圆盘边缘由粉红色与蓝色的小圆圈层层递归堆叠成 fractal（分形）状边界，视觉上像把一棵"永远分叉不完"的树压缩进了圆盘。〔本页为标题页，其余区域为空白；本页配图为纯图示，无正文数据〕

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这份补充材料的主题是"给树计数"。你在 6.042J 里已经学过 tree（树）的定义——连通且无环的图，也见过 spanning tree（生成树）与双射（bijection）计数技巧。现在把问题提明确：$n$ 个带标号的顶点，总共能连出多少棵结构不同的树？答案是 $n^{n-2}$，即著名的 Cayley formula（Cayley 公式），这正是后面两页三位数学家先后独立得到的结果。它与信息论的关系并非牵强附会：信源编码定理的本质是"给典型集 $2^{nH}$ 里的序列编号"，而要无损传输或存储一棵树这类组合对象，同样归结为"在所有可能的树构成的空间里给对象编号"。做一个粗略的信息量估计：由 $\log_2 n^{n-2} = (n-2)\log_2 n$ 可知，描述一棵 $n$ 节点标号树至少需要约 $(n-2)\log_2 n$ 比特，这就把"计数"直接换算成了"比特数"，与熵的定义 $\log_2(\text{等可能结果数})$ 一脉相承。

### p.2 〔Carl Borchardt 1860 · Arthur Cayley 1889 · Heinz Prufer 1918（树计数公式的三位独立发现者）〕

![prufer-p2](fig/prufer/mgp00002.png)

<span style="color:#2471a3;">**[section]**</span> 本页为三张黑白肖像照片并排，无正文，仅在各照片下方以红色文字标注人名与年份：

- 左：侧脸、留络腮胡的男子肖像，下方标注 **Carl Borchardt 1860**（Carl Borchardt，1860 年）。
- 中：正面坐姿、一手扶着太阳穴的男子肖像，下方标注 **Arthur Cayley 1889**（Arthur Cayley，1889 年）。
- 右：头戴礼帽、佩戴眼镜的男子肖像（照片较模糊、画质偏旧），下方标注 **Heinz Prufer 1918**（Heinz Prüfer，1918 年）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页看似只是三张照片，实际上是 MacKay 在做一次"学术史纠错"。公式 $n^{n-2}$ 在教科书里几乎总被叫作 Cayley 公式，但本页的时间线提醒我们：Borchardt 在 1860 年就已发表该结果，Cayley 于 1889 年独立地重新发现，而 Prüfer 到 1918 年才给出基于编码的构造性证明。这种"名字安错了人"的现象在数学史上屡见不鲜，甚至有一句调侃式的 Stigler 定律："科学发现从不以其真正发现者命名"。对学习者而言，真正值得记住的是 Prüfer 的贡献方式：他把一个纯粹的计数问题转化为一个编码问题——树与序列之间的 bijection（双射）。这正是整门信息论课反复出现的思维方式：先承认对象空间很大，再找到一种无歧义的编号办法。MacKay 把这页放在补充材料里，意在提示"数得清"与"编得出码"是同一件事的两面。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把 Prüfer code（Prüfer 编码）的机制展开说清楚，Cayley 公式就变成了几行算术。编码时，对一棵 $n$ 个标号顶点的树重复 $n-2$ 次：找到当前标号最小的 leaf（叶子，即度数为 1 的顶点），写下它唯一邻居的标号，然后把这片叶子删掉；最终得到一个长度为 $n-2$、每个位置取值于 $\{1,\dots,n\}$ 的序列。解码时按相反顺序重建：先由序列统计每个标号的出现次数加一得到各顶点度数，再逐位恢复被删除的叶子。因为这是一一对应，树的数目恰好等于序列的数目 $n^{n-2}$，公式得证——这比直接做递推计数优雅得多。从 6.006 的算法视角看：朴素实现用 min-heap（最小堆）每轮取最小叶子是 $O(n\log n)$，而用指针标记技巧可以做到 $O(n)$。从信息论视角看，这就是 enumerative coding（枚举编码）的雏形：既然树与序列一一对应，传输一棵树只需传输它的编码序列，配合算术编码可逼近 $(n-2)\log_2 n$ 比特的极限——与你已经学过的"给序列编号"的思想完全同源。
