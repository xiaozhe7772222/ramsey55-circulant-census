# CR(5,5) 数据包（配套论文：Circulant Ramsey(5,5) colorings: maximum order 41）

## counts.csv
三列: n, 候选 generating sets 数, c(n)（circulant Ramsey(5,5) 染色数）
取值: n=5..46。

## sets_nXX.txt
每个 n 的 circulant Ramsey(5,5) 染色对应的 generating sets S（距离对展开，逗号分隔）。
含 n=17 (102), 40 (12), 41 (20)。其他 n 为 0，无文件。

## 复现
- JS 穷举扫描器: scan_v5.js （计数）与 scan_dump.js （导出解集）
  node scan_v5.js <N> 5 0 99
- Python 独立实现: ramsey/circulant.py + clique.py（位掩码）
  python run_ramsey.py circulant 41 5
- 独立验证某解集: python run_ramsey.py verify results/<found.json>
- 多进程 Python 穷举: xcheck3.py

## 校准（与已知值一致）
- R(3,3)=6：c_2(5)>0, c_2(6)=0
- R(4,4)=18：c_4(17)=2（含 Paley(17)）, c_4(18)=0
- McKay 公开数据 328 个 Ramsey(5,5;42) 图全部验证通过
- 与 Ivanov (2026) 的 Z_42 / Z_43 排除结果一致

