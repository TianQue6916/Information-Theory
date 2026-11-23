# Information Theory · MacKay ITILA

剑桥大学 David J.C. MacKay（1967–2016）《Information Theory, Pattern Recognition, and Neural Networks》课程的双语学习资料库。

- 教材：MacKay《Information Theory, Inference, and Learning Algorithms》(ITILA)
- 课程：16 讲 + 1 Bonus；官方页面 https://inference.org.uk/itprnn_lectures/
- 视频本体（11.26 GB）与 Snapshot 板书快照见 `04-snapshots/`

## 目录结构

| 目录 | 内容 |
|---|---|
| `01-lecture-notes/` | 讲义逐句双语翻译 `Lec01`–`Lec16` + `prufer` |
| `02-slides/` | 官方 MagicPoint 讲义（`l1`–`l16`，HTML + PNG，356 页） |
| `03-textbook/` | 教材 `book.pdf` / `book.epub` + 逐章双语翻译 `mackay_ch01`–`ch06` + 原文抽取稿 |
| `04-snapshots/` | 各讲板书快照 PDF + 视频下载清单 |

## 双语规范

正文以中文为主体，英文术语以 `English term（中文）` 形式行内嵌入；公式与 LaTeX 环境保留英文原样。

## 学习定位

对应方舟计划大二上「信息论」辅助线（P1）。MacKay 的路径比 Cover 更偏 inference 与机器学习：第 12–13 讲 Monte Carlo 衔接 100B 实分析与概率论，第 15–16 讲神经网络衔接 Strang 18.065。
---

> 图片已按技能铁律 42 base64 内嵌进 md；`02-讲义/fig/` 为源资产备份，勿删。

## 目录结构

> 本节为 2026-11 目录归一化后的结构，取代上表；上表是归一化前的历史记录，按原样保留。

| 目录 | 内容 |
|---|---|
| `01-教材/` | 原书 PDF/EPUB（`mackay_ch01.pdf`、`book.epub`）+ 逐章切片双语译文 `mackay_ch01_p015-033.md`–`mackay_ch06_p122-143.md` + 各章 exercises 抽取稿，平铺无子目录 |
| `02-讲义/` | 讲义逐句双语译文 `Lec01`–`Lec16`、`prufer.md`；官方 MagicPoint 讲义原文 `l1`–`l16`、`prufer`（HTML + PNG）；`fig/` 配图源资产 |
| `02-讲义/板书快照/` | 各讲板书快照 PDF `00_mackay.pdf`–`16_mackay.pdf` + 下载清单（原 `04-snapshots/`） |
| `03-已处理文件/` | 疑问驱动的 AI 资料（原 `06-笔记/`：`PROGRESS.md`、`来源与课程说明.md`） |
| `04-题目/` | 官方题目原文与译本，下设 `作业/`、`考试/`、`题解/`（本仓暂无此类文件） |
| `05-代码/` | 课程附带代码与自写代码（本仓暂无此类文件） |
| `06-工具/` | 脚本、Lean 验证、给模型读的索引（`llms.txt`） |
| `视频/` | 视频字幕与转写稿（`.srt`/`.vtt`/transcript/转录），顶层独立目录（本仓暂无此类文件） |
| `_superseded/` | 历史版本存档，本轮未改动 |

字幕与转录稿统一放**顶层** `视频/` 目录（本仓当前无字幕文件，故无此目录）。
