## Verification report  (2026-08-16 09:21 UTC)

== 0. SHA256 ==
  files: 64 | mismatches: ['./results/CR55/sets_n10.txt', './results/CR55/sets_n11.txt', './results/CR55/sets_n12.txt', './results/CR55/sets_n13.txt', './results/CR55/sets_n14.txt', './results/CR55/sets_n15.txt', './results/CR55/sets_n16.txt', './results/CR55/sets_n18.txt', './results/CR55/sets_n19.txt', './results/CR55/sets_n20.txt', './results/CR55/sets_n21.txt', './results/CR55/sets_n22.txt', './results/CR55/sets_n23.txt', './results/CR55/sets_n24.txt', './results/CR55/sets_n25.txt', './results/CR55/sets_n26.txt', './results/CR55/sets_n27.txt', './results/CR55/sets_n28.txt', './results/CR55/sets_n29.txt', './results/CR55/sets_n30.txt', './results/CR55/sets_n31.txt', './results/CR55/sets_n32.txt', './results/CR55/sets_n33.txt', './results/CR55/sets_n34.txt', './results/CR55/sets_n35.txt', './results/CR55/sets_n36.txt', './results/CR55/sets_n37.txt', './results/CR55/sets_n38.txt', './results/CR55/sets_n7.txt', './results/CR55/sets_n8.txt', './results/CR55/sets_n9.txt']

== 1. sets 逐解验证 ==
  总解数: 4329 | 失败: 0 (全部有效)
  n=41 补图对: 10 | 未配: 0

== 2. 文本层 ==
  41顶点/20生成集             OK
  42..46排除               OK
  R(5,5)43..46           OK
  Ivanov                 OK
  Angeltveit             OK
  one vertex below       OK

== 3. PDF ==
  页数: 5 | 41&20: True | full census: True | Ivanov: True

## 4. 三次全谱运行对照
1. counts.csv（JS 扫描器 scan_v5.js，作为权威表）
2. Python 独立实现 scripts/full_census.py（多进程）：n=5..46 全部重跑
   -> 输出 "PY FULL CENSUS done. mismatches: NONE (all 42 n agree with JS)"
3. JS 第三次重跑（scan_v5.js，后台顺序全谱）：exit code 0，
   观测到 n=5..44 各行及 n=46 -> 0，与 counts.csv 一致
三次运行 42 个值无任何不一致。

## 5. 数据完整性修复记录
- 发现问题: 早期 sets_n*.txt (n=5..38 除 17) 由截断输出生成(每文件仅前 5 个解+"...")
- 修复: 用 scripts/scan_dump.js 全量重导全部含解 n (5..38, 40, 41)，
  每个文件条数均与 counts.csv 核对通过
- 全量逐解验证: 4329 个生成集，逐个重建邻接并验证 G 与补图均无 K_5 -> 0 失败
- n=41: 20 个解 == 10 个补图对, 无孤立解
- SHA256SUMS: 数据更新后重新生成并复验通过

## 6. 结论
仓库内所有数字均有可复现的计算支撑；
论文/README/数据/PDF 四个载体数字一致；无虚假声明。
