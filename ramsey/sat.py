# -*- coding: utf-8 -*-
"""SAT 编码：K_N 是否存在 (K,K)-Ramsey 染色。"""
import itertools
import signal
import time


def encode_ramsey_sat(N, K, sym=False):
    from pysat.formula import CNF
    cnf = CNF()
    nvars = N * (N - 1) // 2

    def vid(i, j):
        return i * N + j + 1 if i < j else j * N + i + 1

    for combo in itertools.combinations(range(N), K):
        vs = [vid(combo[i], combo[j]) for i in range(K) for j in range(i + 1, K)]
        cnf.append([-v for v in vs])   # 不全红
        cnf.append(vs)                 # 不全蓝
    if sym:
        need = (N - 1 + 1) // 2
        edges0 = [vid(0, j) for j in range(1, N)]
        from pysat.card import CardEnc, EncType
        cards = CardEnc.atleast(lits=edges0, bound=need, top_id=nvars,
                                encoding=EncType.seqcounter)
        for cl in cards.clauses:
            cnf.append(cl)
        nvars = max(nvars, cards.nv)
    return cnf, nvars


class _Timeout(BaseException):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def solve(N, K, timeout=300, solver_name="glucose42", sym=False):
    from pysat.solvers import Solver
    cnf, nvars = encode_ramsey_sat(N, K, sym=sym)
    print("[info] K_%d (K=%d): %d 变量, %d 子句, %s" % (
        N, K, nvars, len(cnf.clauses), solver_name), flush=True)
    t0 = time.time()
    old = signal.signal(signal.SIGALRM, _alarm)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    res = "timeout"
    dt = timeout
    model = None
    try:
        with Solver(name=solver_name, bootstrap_with=cnf.clauses) as s:
            r = s.solve()
            dt = time.time() - t0
            if r is None:
                res = None
            else:
                res = r
                model = list(s.get_model()) if r else None
    except _Timeout:
        res = None
        dt = timeout
    finally:
        signal.signal(signal.SIGALRM, old)
        signal.setitimer(signal.ITIMER_REAL, 0)
    return res, dt, model

