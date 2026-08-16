# full_census.py - complete independent Python census of circulant Ramsey(5,5) colorings
# usage: python3 full_census.py   (multiprocessing; compares against counts.csv)
import io, os, time
from multiprocessing import Pool

def has_k(masks, n):
    for a in range(n - 2):
        Ma = masks[a]
        for b in range(a + 1, n - 1):
            if not (Ma >> b) & 1: continue
            Mb = masks[b]; Mab = Ma & Mb
            for c in range(b + 1, n):
                if not (Mab >> c) & 1: continue
                T = Mab & masks[c]
                if T.bit_count() < 2: continue
                x = T
                while x:
                    low = x & -x; u = low.bit_length() - 1
                    if (T & masks[u]) != 0: return True
                    x &= x - 1
    return False

def worker(args):
    N, m0, m1 = args
    pairs = [(s, N - s) for s in range(1, (N - 1) // 2 + 1)]
    full = (1 << N) - 1
    found = []
    for m in range(m0, m1):
        S = []
        for i, (s, sn) in enumerate(pairs):
            if m & (1 << i): S.append(s); S.append(sn)
        masks = [0] * N
        for v in range(N):
            lo = 0
            for s in S:
                lo |= 1 << ((v + s) % N); lo |= 1 << ((v - s + N) % N)
            masks[v] = lo
        if has_k(masks, N): continue
        comp = [full ^ masks[v] & full ^ (1 << v) for v in range(N)]
        if has_k(comp, N): continue
        found.append(tuple(sorted(S)))
    return found

def scan(N, W=8):
    P = (N - 1) // 2
    total = 1 << P
    step = max(1, total // W)
    edges = [(N, m0, min(total, m0 + step)) for m0 in range(0, total, step)]
    t0 = time.time()
    with Pool(W) as pool:
        parts = pool.map(worker, edges)
    cnt = sum(len(x) for x in parts)
    print("PY n=%d found=%d time=%.1fs" % (N, cnt, time.time() - t0), flush=True)
    return cnt

csv = {}
for ln in io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "CR55", "counts.csv")):
    n, chk, c = ln.strip().split(","); csv[int(n)] = int(c)

mism = []
for N in range(5, 47):
    c = scan(N)
    if csv.get(N) != c:
        mism.append(N)
print("PY FULL CENSUS done. mismatches:", mism if mism else "NONE (all 42 n agree with JS)")

