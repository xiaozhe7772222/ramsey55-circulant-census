# Originality statement (原创性声明)

Checked against the literature (Tavily multi-keyword search, EN + ZH; OEIS; arXiv;
Zenodo; MathOverflow; journal sources) on 2026-08-16. **No published source was found
that performs the full census c(n) of circulant Ramsey(5,5) colorings, the exact counts,
the order-41 maximum, or the n = 44, 45 exclusions.**

## What is new (this work)

| # | New item | Evidence in repo |
|---|----------|------------------|
| 1 | Full spectrum c(n), n = 5..46 (exact counts, 42 values) | results/CR55/counts.csv; three independent runs |
| 2 | Maximum order 41; exactly 20 generating sets = 10 complement pairs | results/CR55/sets_n41.txt; paper Theorem 1 |
| 3 | Exclusions c(n) = 0 for n = 44, 45 (new) and 42, 43 (agree with Ivanov 2026), 46 (by R(5,5) ≤ 46) | paper Theorem 2 |
| 4 | Determinative conclusion: no circulant Ramsey(5,5) coloring for all n ≥ 42 | paper Theorem 2 |
| 5 | Non-monotonicity of forcing in the circulant class (c(39) = 0 < c(40), c(41) > 0) | paper Remark |
| 6 | Fully reproducible double-implementation pipeline + verification audit | scripts/, results/VERIFICATION_REPORT.md |

## What is borrowed / used (fully acknowledged)

| Item | Source (borrowed from) | Role in this work |
|------|------------------------|-------------------|
| Concept "Ramsey numbers for circulant colorings" | Harborth & Krause, Congr. Numer. 161 (2003) — treated the triangle-free (3,n) diagonal family (OEIS A000789) | We adopt their framing for the (5,5) diagonal; we do NOT reproduce their (3,n) table |
| Circulant-based Ramsey lower-bound constructions (technique) | Kalbfleisch (1965); Exoo (construction lists, cs.indstate.edu/ge/RAMSEY); Goedgebeur & Van Overberghe (2021, circulant section); Ljubic (bilevel optimization on circulants) | Motivation and method heritage; our census is exhaustive over all circulant graphs, not a search |
| Lower bound R(5,5) ≥ 43 (42-vertex witness) | Exoo (1989); 656 graphs: McKay–Radziszowski; conjecture R(5,5) = 43 | Context for Theorem 2 (we do not improve it) |
| Upper bound R(5,5) ≤ 46 | Angeltveit & McKay (2024/2025), JGT | Used in Theorem 2 / completeness remark (n ≥ 47) |
| Exclusion of circulant Ramsey(5,5) on Z_42, Z_43 | Ivanov (2026), Zenodo 10.5281/zenodo.20781786 | Our c(42) = c(43) = 0 reproduce his Theorems 1 & 3; cited in paper |
| Paley graphs / quadratic-residue circulants | Greenwood–Gleason; standard | Calibration target: Paley(17), Paley(41) family |
| 328 (5,5;42)-graphs data (graph6) | McKay's Ramsey data page | Validation artifact (results/validation/r55_42.g6) |
| graph6 format | nauty / McKay | Data encoding |
| Bitmask clique detection | standard technique | Implementation detail |
| OEIS A000789 | Harborth–Krause / Kalbfleisch | Cited as the analogous (3,n) sequence |
| R(5,5) as a formal conjecture | Google DeepMind formal-conjectures issue #2364 | Context only |

## Coverage of the search performed
- English: "circulant Ramsey(5,5) census/maximum order/counts", "CR(5,5)", "circulant Ramsey
  graph 41 vertices", "no circulant ... 44 45", "Harborth Krause", "Exoo constructions",
  "Goedgebeur circulant", "Ljubic circulant Ramsey".
- Chinese: "circulant 拉姆齐数 R(5,5) 循环图 普查 计数", "循环拉姆齐染色 43 顶点 circulant 不存在".
- Databases hit: arXiv, OEIS, Zenodo, MathOverflow, ScienceDirect, Semantic Scholar,
  MathWorld, Wikipedia/Zh-Wikipedia, Exoo's site, McKay's site.

**Vetting:** see NOVELTY_VETTING.md for the row-by-row reconciliation of the
reviewer critique (several of its 'already known' attributions are not corroborated;
we keep our claims measured accordingly). $\;$
**Conclusion:** the census, counts, extremal order-41 objects, and the n = 44, 45
exclusions appear to be original; everything else rests on the cited literature above.
We will finalize this statement after the definitive pre-publication search.



---

## 完整参考清单（带地址）— 借鉴/引用来源全录

1. H. Harborth, S. Krause, *Ramsey numbers for circulant colorings*, Congressus Numerantium 161 (2003) 139-150.
2. J. G. Kalbfleisch, *Construction of special edge-chromatic graphs*, Canad. Math. Bull. 8 (1965) 575-584. DOI: 10.4153/CMB-1965-041-7.
3. G. Giraud, *Sur le probleme de Goodman pour les quadrangles*, C. R. Acad. Sci. Paris Ser. A-B 266 (1968) A1024-A1026.
4. F. R. K. Chung, *On triangular and cyclic Ramsey numbers with k colors*, in Graphs and Combinatorics, LNM 406, Springer (1974) 236-242.
5. G. Exoo, *A lower bound for R(5,5)*, J. Graph Theory 13 (1989) 97-98. DOI: 10.1002/JGT.3190130113.
6. B. D. McKay, Ramsey graphs data (656 order-42 graphs; R(5,5)=43 conjecture with Radziszowski). URL: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
7. S. P. Radziszowski, *Small Ramsey Numbers*, E-JC Dynamic Survey DS1 (DS1.17, 2024). URL: https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1
8. V. Angeltveit, B. D. McKay, *R(5,5) <= 46*, J. Graph Theory (2025). DOI: 10.1002/jgt.70029; arXiv:2409.15709.
9. V. Ivanov, *No valid Ramsey(5,5;42) coloring is circulant on Z_42...*, Zenodo (2026). DOI: 10.5281/zenodo.20781786. URL: https://zenodo.org/records/20781786
10. G. Exoo, M. Tatarevic, *New lower bounds for 28 classical Ramsey numbers*, E-JC 22(2) (2015) P2.15; arXiv:1504.02403.
11. J. Goedgebeur, S. Van Overberghe, *New bounds for Ramsey numbers R(K_k-e, K_l-e)*, Discrete Applied Mathematics (2021/22); arXiv:2107.04460; URL: https://www.sciencedirect.com/science/article/pii/S0166218X21004522
12. I. Ljubic, *Lower bounds for Ramsey numbers on circulant graphs: a bilevel optimization approach* (talk). URL: https://www.youtube.com/watch?v=ybVCkWYWEGQ
13. R. E. Greenwood, A. M. Gleason, *Combinatorial relations and chromatic graphs*, Canad. J. Math. 7 (1955) 1-7.
14. B. D. McKay, A. Piperno, *Practical graph isomorphism, II* (graph6), J. Symbolic Computation 60 (2014) 94-112. DOI: 10.1016/j.jsc.2013.09.003.
15. OEIS A000789. URL: https://oeis.org/A000789
16. Google DeepMind, formal-conjectures issue on R(5,5). URL: https://github.com/google-deepmind/formal-conjectures/issues/2364
17. G. Exoo, *On some small classical Ramsey numbers*, E-JC 20(1) (2013) P68.
