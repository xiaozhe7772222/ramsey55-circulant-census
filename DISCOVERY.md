# How these results were discovered (research narrative)

A faithful record of the workflow behind
*Circulant Ramsey(5,5) Colorings: Maximum Order 41 and the Exclusion Band 42–46*.
Every claim below is backed by files in this repository.

## 1. The starting question
We began from the open bounds
    43 ≤ R(5,5) ≤ 46            (Exoo 1989 lower; Angeltveit–McKay 2024 upper)
and asked the restricted, exactly-answerable question: *where do circulant (cyclic)
2-colorings stop avoiding a monochromatic K5?* Circulant graphs are the standard raw
material of Ramsey lower-bound constructions (Kalbfleisch; Harborth–Krause 2003, who
treated the triangle-free (3,n) family — OEIS A000789), so knowing the circulant frontier
has independent value beyond R(5,5) itself.

## 2. The enumerable object
A circulant graph C(n,S) is fixed by one bit per inverse pair {s, n−s}; there are exactly
2^⌊(n−1)/2⌋ graphs, and the complement of a circulant graph is circulant. So "what is the
largest n with a circulant Ramsey(5,5) coloring, and how many are there?" is a finite
enumeration problem with a clean answer.

## 3. Method built in two independent ways
Two independent codebases were written for the K5-free test:
  JS (scripts/scan_v5.js) and Python (scripts/full_census.py).
The detection uses the criterion: *G contains a K5 iff some triangle has a common
neighborhood containing an edge*, implemented with bitmasks. Full proofs are in
paper.tex (Lemma on detection, Lemma on complement).

## 4. Calibration before production
The detector was first checked against known exact values:
  c3(5)=2, c3(6)=0     → R(3,3)=6
  c4(17)=2 (incl. Paley(17)), c4(18)=0  → R(4,4)=18,
and against the 328 published Ramsey(5,5;42) graphs (r55_42.g6) — all verified.

## 5. Production and cross-checks
The census ran in JS; the full spectrum was then re-run in Python and agreed on all 42
values (results/VERIFICATION_REPORT.md); a third full JS re-run agreed as well. For n=41
the two implementations return the same twenty generating sets, set by set.

## 6. What fell out
- c(41) = 20 is the maximum: the largest circulant Ramsey(5,5) colorings have 41 vertices.
- c(n) = 0 for every 42 ≤ n ≤ 46 — so circulant constructions cannot witness R(5,5) ≥ 43.
- An initially surprising wrinkle: c(39) = 0 while c(40), c(41) > 0 — forcing is not
  monotone in the circulant class. Kept as a feature, and double-checked with a third run.
- The 20 extremal generating sets form exactly 10 complement pairs.

## 7. Errors found by our own audit (and fixed)
- Early per-n solution files for n = 5..38 (except 17) were generated from a truncated
  output (first 5 sets + "..."). Caught during a full audit, re-generated completely with
  scan_dump.js, and re-verified: 4329 sets, all valid, counts matching counts.csv.
- A text error ("three vertices below 42" → "one vertex below") was corrected in both
  paper.tex and paper.md.
- Checksums were regenerated after every data change (results/SHA256SUMS, verifiable with
  sha256sum -c).

## 8. Honest scope
This repository does not determine R(5,5) (still 43 ≤ R(5,5) ≤ 46). It determines the
circulant subclass completely:
  - the full spectrum c(n), n = 5..46  (new),
  - the order-41 extremal objects, 20 sets / 10 complement pairs  (new),
  - exclusions for n = 44, 45 (new); n = 42, 43 agree with Ivanov (2026),
  - and the observation that forcing is non-monotone in the circulant class.

Everything can be reproduced in under 20 minutes on a laptop; see README.md and
results/VERIFICATION_REPORT.md.

