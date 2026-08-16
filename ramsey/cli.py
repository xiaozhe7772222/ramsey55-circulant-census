# -*- coding: utf-8 -*-
"""命令行入口：python -m ramsey.cli <command> ..."""
import argparse, json, os, sys, time
from . import circulant, sat, heuristics
from .clique import has_k, build_masks


def cmd_circulant(args):
    t0 = time.time()
    found, checked, skipped = circulant.scan_circulant(args.N, args.K, args.dmin, args.dmax)
    dt = time.time() - t0
    print("[circulant] N=%d K=%d 候选 %s（跳过 %d）耗时 %.1fs" % (
        args.N, args.K, "{:,}".format(checked), skipped, dt))
    if found:
        print("[circulant] 找到 %d 个 (K,K)-Ramsey 循环图（R(K,K) 下界构造!）" % len(found))
        for S in found[:10]:
            print("   S =", S)
    else:
        print("[circulant] 无 (K,K)-Ramsey 循环图于 N=%d（该族本层关闭）" % args.N)


def cmd_sat(args):
    try:
        res, dt, model = sat.solve(args.N, args.K, timeout=args.timeout,
                                   solver_name=args.solver, sym=args.sym)
    except ImportError as e:
        print("[sat] 需要安装: pip install python-sat  (%s)" % e)
        sys.exit(2)
    if res is True:
        print("[sat] SAT! 存在 K_%d 的无单色 K_%d 染色 => R(%d,%d) > %d（下界提升！）" % (
            args.N, args.K, args.K, args.K, args.N))
        print("[sat] 模型（1=红,0=蓝）前 60 个:", model[:60])
    elif res is False:
        print("[sat] UNSAT: K_%d 必含单色 K_%d => R(%d,%d) <= %d（上界收紧！）" % (
            args.N, args.K, args.K, args.K, args.N))
    else:
        print("[sat] %.0fs 超时，未决（该问题常态）" % args.timeout)
    print("[sat] 求解耗时 %.1fs" % dt)


def cmd_search(args):
    def on_sol(masks):
        fn = os.path.join(args.outdir, "found.json")
        with open(fn, "w") as f:
            json.dump({
                "N": args.N, "K": args.K,
                "adj": [[1 if masks[i] >> j & 1 else 0 for j in range(args.N)]
                        for i in range(args.N)]
            }, f)
        print("[search] ★ 找到 (K,K)-Ramsey 图于 N=%d -> 已存 %s" % (args.N, fn))
    os.makedirs(args.outdir, exist_ok=True)
    print("[search] 模拟退火：N=%d K=%d 预算 %.0fs" % (args.N, args.K, args.timeout), flush=True)
    sol, attempts = heuristics.anneal(args.N, args.K, budget_s=args.timeout,
                                      seed=args.seed, restarts=args.restarts,
                                      on_solution=on_sol)
    if sol is None:
        print("[search] %.0fs 内未找到（%d 次重启）；困难符合预期，不代表不存在。" % (
            args.timeout, attempts))


def cmd_verify(args):
    data = json.load(open(args.file, encoding="utf-8"))
    N, K = data["N"], data["K"]
    adj = data["adj"]
    masks = build_masks(adj)
    hasg = has_k(masks, N, K)
    full = (1 << N) - 1
    comp = [full ^ masks[v] & full ^ (1 << v) for v in range(N)]
    hasc = has_k(comp, N, K)
    if not hasg and not hasc:
        print("[verify] OK：N=%d 染色无单色 K_%d（G 与补图）。若 N>=44 即新下界！" % (N, K))
    else:
        print("[verify] FAIL：G 含 K_%d：%s；补图含 K_%d：%s" % (K, hasg, K, hasc))


def main():
    ap = argparse.ArgumentParser(prog="ramsey", description="R(K,K) 计算工具箱")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("circulant", help="穷举循环图族")
    p.add_argument("N", type=int); p.add_argument("K", type=int)
    p.add_argument("--dmin", type=int, default=0)
    p.add_argument("--dmax", type=int, default=None)
    p.set_defaults(fn=cmd_circulant)
    p = sub.add_parser("sat", help="SAT 求解 K_N 无单色 K_K")
    p.add_argument("N", type=int); p.add_argument("K", type=int)
    p.add_argument("--timeout", type=float, default=300)
    p.add_argument("--solver", default="glucose42")
    p.add_argument("--sym", action="store_true")
    p.set_defaults(fn=cmd_sat)
    p = sub.add_parser("search", help="模拟退火找 (K,K)-Ramsey 图")
    p.add_argument("N", type=int); p.add_argument("K", type=int)
    p.add_argument("--timeout", type=float, default=300)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--restarts", type=int, default=8)
    p.add_argument("--outdir", default="results")
    p.set_defaults(fn=cmd_search)
    p = sub.add_parser("verify", help="验证染色文件(found.json)")
    p.add_argument("file")
    p.set_defaults(fn=cmd_verify)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

