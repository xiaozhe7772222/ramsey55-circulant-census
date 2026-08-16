// scan_dump.js - same enumeration; prints ALL solution generating sets (one per line 'S:')
// usage: node scan_dump.js <N> [K]
'use strict';
const N = +process.argv[2] || 41;
const K = +process.argv[3] || 5;
// ...复用 v5 逻辑，但打印全部解
const pc = new Uint8Array(65536);
for (let i = 1; i < 65536; i++) pc[i] = pc[i >> 1] + (i & 1);
const pop = (lo, hi) => pc[lo & 0xffff] + pc[(lo >>> 16) & 0xffff] + pc[hi & 0xffff] + pc[(hi >>> 16) & 0xffff];
const pairs = []; for (let s = 1; s <= Math.floor((N - 1) / 2); s++) pairs.push([s, N - s]);
const P = pairs.length;
function masksFor(S) {
  const M = new Array(N);
  for (let v = 0; v < N; v++) {
    let lo = 0, hi = 0;
    for (const s of S) { let t = (v + s) % N; if (t < 32) lo |= 1 << t; else hi |= 1 << (t - 32); t = (v - s + N) % N; if (t < 32) lo |= 1 << t; else hi |= 1 << (t - 32); }
    M[v] = [lo >>> 0, hi >>> 0];
  }
  return M;
}
const fullLo = (N >= 32) ? 0xFFFFFFFF >>> 0 : ((1 << N) - 1) >>> 0;
const fullHi = (N > 32) ? ((1 << (N - 32)) - 1) >>> 0 : 0;
function comp(M) {
  const C = new Array(N);
  for (let v = 0; v < N; v++) { let lo = (fullLo ^ M[v][0]) >>> 0, hi = (fullHi ^ M[v][1]) >>> 0; if (v < 32) lo &= ~(1 << v); else hi &= ~(1 << (v - 32)); C[v] = [lo >>> 0, hi >>> 0]; }
  return C;
}
const AND = (a, b) => [a[0] & b[0], a[1] & b[1]];
const AND3 = (a, b, c) => [a[0] & b[0] & c[0], a[1] & b[1] & c[1]];
function hasBit(mask, x) { return x < 32 ? (mask[0] & (1 << x)) !== 0 : (mask[1] & (1 << (x - 32))) !== 0; }
function edgeIn(M, T) {
  let lo = T[0], hi = T[1];
  while (lo !== 0 || hi !== 0) {
    let idx; if (lo !== 0) idx = 31 - Math.clz32(lo & -lo); else idx = 32 + 31 - Math.clz32(hi & -hi);
    if (idx >= N) break;
    const bit = idx < 32 ? (lo & -lo) : (hi & -hi);
    if (pop(AND(T, M[idx])[0], AND(T, M[idx])[1]) >= 1) return true;
    if (lo !== 0) lo &= ~bit; else hi &= ~bit;
  }
  return false;
}
function hasKk(M) {
  for (let a = 0; a < N - 2; a++) {
    const Ma = M[a];
    for (let b = a + 1; b < N - 1; b++) { if (!hasBit(Ma, b)) continue; const Mb = M[b]; const Mab = AND(Ma, Mb);
      for (let c = b + 1; c < N; c++) { if (!hasBit(Mab, c)) continue; if (K === 3) return true; const T = AND3(M[a], M[b], M[c]); if (pop(T[0], T[1]) < K - 3) continue; if (K === 4) return true; if (K === 5 && edgeIn(M, T)) return true; if (K === 6 && false) return true; } }
  }
  return false;
}
let found = [], checked = 0;
const t0 = Date.now();
for (let m = 0; m < (1 << P); m++) {
  const S = [];
  for (let i = 0; i < P; i++) if (m & (1 << i)) { S.push(pairs[i][0]); S.push(pairs[i][1]); }
  checked++;
  const M = masksFor(S);
  if (hasKk(M)) continue;
  const CM = comp(M);
  if (hasKk(CM)) continue;
  found.push(S.join(","));
}
const secs = ((Date.now() - t0) / 1000).toFixed(1);
console.log("N=" + N + " found=" + found.length + " time=" + secs + "s");
found.forEach(f => console.log("S:", f));

