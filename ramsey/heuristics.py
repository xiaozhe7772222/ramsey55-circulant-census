# -*- coding: utf-8 -*-
"""启发式搜索：(K,K)-Ramsey 图构造器（模拟退火）。"""
import random, time
from .clique import has_k


def random_graph(N, p=0.5, seed=None):
    rng = random.Random(seed)
    masks = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if rng.random() < p:
                masks[i] |= 1 << j
                masks[j] |= 1 << i
    return masks


def cost(masks, N, K):
    if has_k(masks, N, K):
        return 1
    full = (1 << N) - 1
    comp = [full ^ masks[v] & full ^ (1 << v) for v in range(N)]
    if has_k(comp, N, K):
        return 1
    return 0


def flip(masks, i, j):
    masks[i] ^= 1 << j
    masks[j] ^= 1 << i


def anneal(N, K, budget_s=300, seed=None, p0=0.5, T0=2.0, cool=0.9999,
           restarts=8, on_solution=None):
    rng = random.Random(seed)
    t_end = time.time() + budget_s
    attempt = 0
    while time.time() < t_end and attempt < restarts:
        attempt += 1
        masks = random_graph(N, p=p0, seed=rng.getrandbits(64))
        T = T0
        best_cost = cost(masks, N, K)
        if best_cost == 0:
            if on_solution:
                on_solution(masks)
            return masks, attempt
        while time.time() < t_end and T > 1e-3:
            i = rng.randrange(N); j = rng.randrange(N)
            if i == j:
                continue
            flip(masks, i, j)
            nc = cost(masks, N, K)
            if nc == 0:
                if on_solution:
                    on_solution(masks)
                return masks, attempt
            if nc <= best_cost or rng.random() < T / 2.0:
                best_cost = nc
            else:
                flip(masks, i, j)
            T *= cool
    return None, attempt

