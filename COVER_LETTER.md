# Cover Letter

**Title:** Circulant Ramsey(5,5) Colorings: Maximum Order 41 and the Exclusion Band 42–46
**Author:** Xiao Zhe

## To the Editor / arXiv readers

This note reports an exhaustive, fully reproducible computational determination of the
circulant subclass of the famous open diagonal Ramsey number R(5,5):

- The complete spectrum c(n) of circulant Ramsey(5,5) colorings for 5 ≤ n ≤ 46 is computed,
  with no such census previously published.
- The maximum order is 41, attained by exactly 20 generating sets (10 up to complementation);
  the extremal objects are listed explicitly.
- No circulant Ramsey(5,5) coloring exists for 42 ≤ n ≤ 46; hence every circulant 2-coloring
  of K_n, n ≥ 42, contains a monochromatic K_5, so circulant constructions cannot witness
  R(5,5) ≥ 43. The exclusions for n = 44, 45 are new; n = 42, 43 agree with
  Ivanov (2026), which we cite.
- A methodological observation: forcing is not monotone in the circulant class (c(39) = 0
  but c(40), c(41) > 0), which bears on the definitional conventions of circulant Ramsey
  numbers.

All results were produced by two independent implementations (JavaScript and Python) agreeing
set-by-set, and cross-validated against R(3,3)=6, R(4,4)=18, Paley(17), the 328 published
Ramsey(5,5;42)-graphs, and Ivanov (2026). Code and data are released with this repository.

We believe this fills a small but clean gap in the computational Ramsey theory of circulant
graphs and complements the recent upper bound R(5,5) ≤ 46 of Angeltveit–McKay.

Sincerely,
Xiao Zhe

