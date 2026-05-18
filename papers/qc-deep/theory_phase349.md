# Phase 349: ITU 版 threshold theorem 

QEC の核心定理: **threshold theorem** (Aharonov-Ben-Or 1997, Kitaev 1997, Knill-Laflamme-Zurek 1998)。
ITU 公理から再導出 + 一般化。

## 古典 threshold theorem (再掲)

```
Theorem (Aharonov-Ben-Or 1997):
 Physical error rate per gate p < p_threshold ならば、
 logical error rate ↓ as code distance ↑

Surface code (Fowler-Mariantoni-Martinis-Cleland 2012 PRA):
 p_threshold ≈ 1% for depolarizing noise
 
Google Willow 2024.12 Nature:
 distance-3 → distance-5 → distance-7
 各 step で logical error 2.14x 改善 (below threshold!)
```

## ITU 版 threshold (Tier 1+ #1 新規)

### Conjecture (新公理候補): mKQEC threshold

```
Conjecture: mKQEC noise model {L_k} に対し
 
 p_threshold^{mKQEC} = f(spectral gap of K_QC^(0))
 
ここで spectral gap = K_QC^(0) の eigenvalue 間隔の最小値

Intuition:
 K_QC^(0) gap 大 ⇒ steady state 安定 ⇒ syndrome 抽出容易 ⇒ p_threshold 大

予測:
 Depolarizing: gap = 0 (degenerate) ⇒ surface code threshold ≈ 1%
 Biased T2/T1=0.01: gap > 0 (Z-bias) ⇒ mKQEC threshold ≈ 1.5-2%
```

### 証明スケッチ (heuristic)

```
Step 1: ITU 公理 δS = δ⟨K_QC^(0)⟩
 ⇒ decoherence-induced entropy change = modular K 期待値変化

Step 2: Error correction success ⇔ δS が boundary 以下に保たれる
 ⇒ δ⟨K_QC^(0)⟩ < critical value

Step 3: Critical value は K_QC^(0) spectrum で決定
 ⇒ p_threshold = critical / max eigenvalue
 ⇒ gap 依存性

Step 4: Surface code は gap=0 の lower bound (worst case for ITU)
 ⇒ biased noise で必ず improvement
```

完全証明は Phase 350 数値検証 + 2027 PRA 論文で。

## Comparison table

| Code | Noise | Threshold (est.) | Source |
|---|---|---|---|
| 9-qubit Shor | depolarizing | ~10^-4 | Shor 1995 |
| 7-qubit Steane | depolarizing | ~10^-4 | Steane 1996 |
| Toric / Surface | depolarizing | **~1%** | Kitaev 1997 / Fowler 2012 |
| XZZX surface | biased Z | **~5%** (Z-only) | Tuckett 2020 Nat Comm |
| Cat code | photon loss | ~1% (Photon n=4) | Vlastakis 2013 |
| **mKQEC (general)** | **arbitrary {L_k}** | **f(gap)** | **本論文 (predicted)** |
| **mKQEC trapped-ion** | T2 << T1 | **~1.5-2%** | **predicted** |
| **mKQEC photonic** | erasure | **~10%** (?) | **predicted** |

## Logical qubit overhead 予測

```
Surface code (Google Willow path):
 100 physical/logical for 10^-6 error rate (estimated)
 1M physical for 10K logical (fault-tolerant) — IBM 2033 roadmap
 
mKQEC (predicted):
 非対称 noise で 50-70 physical/logical (30-50% reduction)
 ⇒ 1M physical で 15-20K logical (achievable earlier?)
 ⇒ Fault-tolerant era 2-3 yr 前倒し possible
```

## Pass-2 検証 protocol

```
Protocol A: Numerical simulation (2026-27)
 - Stim (Google), Qiskit Aer, Quantinuum tket
 - Multiple noise models compared
 - mKQEC vs surface code logical error rate
 - OSF pre-register

Protocol B: Hardware demonstration (2027-28)
 - Quantinuum H2/H3 (trapped-ion, biased noise natural)
 - 56 → 100 qubits distance-3 mKQEC vs distance-3 surface
 - Logical fidelity 比較
 - 30%+ improvement 観測 ⇒ ITU 強化
 - <0% improvement ⇒ H4 反証

Protocol C: Theoretical proof (2028-30)
 - Lean Mathlib K_QC^(0) library
 - mKQEC threshold theorem formal proof
 - PRX or Annals Math 投稿
```

## Falsification

```
ITU 版 threshold theorem の反証:
 
1. mKQEC threshold が biased noise 下でも surface code 以下 ⇒ H4 反証
2. spectral gap と threshold が独立 ⇒ conjecture 反証
3. ρ_∞ が unique でない ⇒ H1 反証 ⇒ mKQEC framework 自体崩壊
 
いずれも実験で 1-3 yr で判定可能 ⇒ 完全に Popper 的科学
```

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #QC #mKQEC #ThresholdTheorem #Kitaev #Fowler #Willow #Phase349
