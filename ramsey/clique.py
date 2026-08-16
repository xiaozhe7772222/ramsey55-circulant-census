# -*- coding: utf-8 -*-
"""位掩码团检测：判断图是否存在 K(K) 团。"""

def has_clique_in_set(masks, S, t):
    if t <= 0:
        return True
    if S == 0:
        return False
    if bin(S).count("1") < t:
        return False
    x = S
    while x:
        low = x & -x
        u = low.bit_length() - 1
        if has_clique_in_set(masks, S & masks[u], t - 1):
            return True
        x &= x - 1
    return False


def build_masks(adj):
    n = len(adj)
    masks = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j]:
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    return masks


def has_k(masks, n, K):
    """G 含 K-团？ masks[v] 为邻居位掩码。"""
    for a in range(n - 2):
        Ma = masks[a]
        for b in range(a + 1, n - 1):
            if not (Ma >> b) & 1:
                continue
            Mb = masks[b]
            Mab = Ma & Mb
            for c in range(b + 1, n):
                if not (Mab >> c) & 1:
                    continue        # 严格三角形 a~b, a~c, b~c
                if K == 3:
                    return True     # 三角形即 K3
                T = Mab & masks[c]
                if bin(T).count("1") < K - 3:
                    continue
                if has_clique_in_set(masks, T, K - 3):
                    return True
    return False


def no_mono_k(masks, n, K):
    if has_k(masks, n, K):
        return (False, False)
    full = (1 << n) - 1
    comp = [full ^ masks[v] & full ^ (1 << v) for v in range(n)]
    if has_k(comp, n, K):
        return (False, True)
    return (True, False)

