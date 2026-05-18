# Phase 391: 実験プロトコル + Pass-2 budget

Tier 1+ #3 の **実験 roadmap** を Pass-2 で実行可能形に整理。

## Pass-2 三本柱

### 柱 1: PQC implementation benchmark (2026-2030)

```
NIST PQC algorithms の K_crypto measurement:
  - Reference implementations
  - Optimized (AVX-512, ARMv9 NEON)
  - Hardware (FPGA, ASIC)
  - Side-channel resistance

Effort: 1 yr × 2 engineers = $300K
Output: Open-source benchmark suite
```

### 柱 2: Lean Mathlib K_crypto formalization (2027-2030)

```
Lean types:
  structure CryptoSystem (security_param : ℕ)
  structure KeySpace H
  def K_crypto : DensityOp → Real
  theorem modular_hardness_conjecture
  theorem ITU_axiom_in_crypto

Mathlib PRs: 2027-2029
ICM 2029 submission target

Effort: 2 yr × 1 postdoc = $200K
```

### 柱 3: QKD experimental verification (2027-2030)

```
Toshiba twin-field QKD (already 600 km):
  → 1000 km record target 2027

Quantum Internet Wehner Stage 5:
  Distributed QC by 2045 (Phase 14)

ITU framework は QKD protocol design に応用:
  K_qubit fluctuation を direct measurement
  Eavesdropping detection threshold optimization

Partners: Toshiba Cambridge, ID Quantique, MIT QECC
Budget: ~$2M (collaboration funding)
```

## Total budget

```
Pillar 1 (PQC bench):    $300K
Pillar 2 (Lean):         $200K
Pillar 3 (QKD):          $2M (mostly via partner labs)
Total:                   ~$2.5M
```

## Year-by-year milestones

```
2026:
  - Tier 1+ #3 arXiv preprint
  - K_crypto Python library v0.1

2027:
  - NIST PQC benchmark with K_crypto metric
  - Lean Mathlib K_crypto types initial submission
  - QKD partnership (Toshiba or MIT)

2028:
  - K_crypto benchmark vs all NIST PQC
  - Side-channel K_side-channel measurements
  - Lean H_K1-H_K4 formal proofs

2029:
  - Modular Hardness Conjecture Lean proof attempt
  - Cryptanalysis competition with K_crypto metric
  - QKD 1000 km K_qubit verification

2030:
  - Tier 1+ #3 conclusive paper (Nature Crypto target)
  - Open-source benchmark widely adopted
  - PQC migration tracking via K_crypto database
```

## 反証期限

```
2027.6: NIST PQC benchmark, K_crypto distinguishability
2028.6: Side-channel K_side-channel quantification
2029.6: Modular Hardness Conjecture Lean partial proof
2030.6: Tier 1+ #3 conclusive analysis

各 deadline で OSF + Bayesian update


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase391
