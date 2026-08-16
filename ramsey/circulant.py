# -*- coding: utf-8 -*-
"""循环图 (circulant) Ramsey 穷举扫描。"""
from .clique import has_k

def scan_circulant(N, K, dmin=0, dmax=None, progress_every=200000, show_progress=True):
    if dmax is None:
        dmax = N - 1
    pairs = [(s, N - s) for s in range(1, (N - 1) // 2 + 1)]
    P = len(pairs)
    full = (1 << N) - 1
    found = []
    checked = skipped = 0
    for m in range(1 << P):
        S = []
        for i, (s, sn) in enumerate(pairs):
            if m & (1 << i):
                S.extend((s, sn))
        d = len(S)
        if d < dmin or d > dmax:
            skipped += 1
            continue
        checked += 1
        if show_progress and checked % progress_every == 0:
            print("  ...checked %s" % ("{:,}".format(checked)), flush=True)
        masks = [0] * N
        for v in range(N):
            lo = 0
            for s in S:
                lo |= 1 << ((v + s) % N)
                lo |= 1 << ((v - s + N) % N)
            masks[v] = lo
        if has_k(masks, N, K):
            continue
        comp = [full ^ masks[v] & full ^ (1 << v) for v in range(N)]
        if has_k(comp, N, K):
            continue
        found.append(tuple(sorted(S)))
    return found, checked, skipped

