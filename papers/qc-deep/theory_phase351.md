# Phase 351: 実験ロードマップ + 予算 + 反証期限 

mKQEC validation の **具体的 3-5 yr 実験ロードマップ**。Pass-2 first conclusive experiment 候補。

## Year-by-year roadmap

### 2026 (Q1-Q4): 理論基盤と simulation

```
Q1 (2026.5-7):
 - mKQEC theoretical paper drafting
 - K_QC^(0) numerical computation for 5 noise models
 - Initial Python/Qiskit simulation framework
 - Code repository (GitHub) public
 Budget: $0 (academic effort)
 
Q2 (2026.8-10):
 - arXiv preprint submission
 - 数値 simulation 確証 (Stim, Qiskit)
 - 比較: surface code vs mKQEC under various noise
 - Open Science: OSF pre-registration of predictions
 Budget: $0-5K (compute)
 
Q3 (2026.11-2027.1):
 - PRA / PRL submission
 - Community feedback iteration
 - Collaboration outreach (Google, Quantinuum, PsiQuantum)
 Budget: $10K (conference travel)
 
Q4 (2027.2-4):
 - First responses, revision
 - Tier 1+ #1 publication ready
 Budget: minimal
```

### 2027: 数値検証 + initial hardware

```
Q1-Q2 (2027.1-6):
 - Extensive Stim simulation: 1000+ noise model combinations
 - Quantinuum H3 (~64 qubits trapped-ion) collaboration
 - Distance-3 mKQEC Z-biased実装
 - First hardware demo target: 10% over surface
 Budget: $50K (compute) + $100K (Quantinuum cloud access)
 
Q3-Q4 (2027.7-12):
 - First hardware result presented
 - PsiQuantum Omega chip access discussion
 - Erasure-aware mKQEC simulation
 - 2nd publication: hardware demo paper
 Budget: $100K (compute + travel + Quantinuum)
```

### 2028: Scaling + multiplatform

```
Q1-Q2 (2028.1-6):
 - Quantinuum H3/H4 distance-5,7 mKQEC
 - 30%+ improvement target achieved (or refuted)
 - PsiQuantum photonic mKQEC first demo
 Budget: $300K (Quantinuum + PsiQuantum)

Q3-Q4 (2028.7-12):
 - Google Willow follow-up: mKQEC on superconducting
 - IBM Heron mKQEC: 156 qubits
 - Cross-platform consistency check
 - Threshold confirmation paper (Nature target)
 Budget: $500K (multi-platform)
```

### 2029-2030: Fault-tolerant demonstration

```
2029:
 - Distance-9, -11 mKQEC on best platform
 - Logical qubit beating physical by 100x
 - Multiple logical qubits + entangling gate
 Budget: $1M (intensive)

2030:
 - Fault-tolerant logical qubit (10^-9 logical error)
 - 商用 prototype 接続
 - Tier 1+ #1 conclusive paper (Nature/Science)
 Budget: $2-3M
```

## Total budget estimate (5 yr)

```
理論・simulation: $200K
Quantinuum access: $500K (3-yr collaboration)
PsiQuantum access: $300K
Google/IBM access: $500K
Travel/conferences: $100K
Postdocs (2 yr × 2): $400K
Total: ~$2M

Funding sources:
 - JST CREST quantum
 - NEDO 量子
 - JST Moonshot R&D
 - NSF Quantum Leap
 - DOE ASCR
 - EU Quantum Flagship
 - Industry partnership
```

## Risk-adjusted milestones

```
Best case (P=0.30): mKQEC threshold 50% over surface in 2027
 → further development 2032-2035 candidate
 
Base case (P=0.45): mKQEC threshold 20-30% over surface in 2028-29
 → Major paper (Nature/Science), strong impact
 
Conservative (P=0.20): mKQEC matches surface, no improvement
 → ITU framework provides unifying principle, no superiority claim
 → Theoretical paper (PRA) still publishable
 
Refutation (P=0.05): mKQEC underperforms or H1-H4 fails
 → ITU axiom partially refuted in QC context
 → Important negative result, Popperian progress
```

## 反証期限 (concrete dates)

```
2027.6 deadline: Numerical simulation (Stim) 結果
2028.6 deadline: Quantinuum first hardware demo
2029.6 deadline: 30%+ over surface confirmed or refuted
2030.6 deadline: Fault-tolerant scaling demonstrated

各 deadline で OSF database 更新、Bayesian P_post 反映
```

## Pass-2 第1柱 (Experimental) における位置づけ

```
Pass-2 Pillar 1 experimental priorities:
 1. BMV table-top QG (2030, ITU 公理直接検証)
 2. **mKQEC実証 (2027-29, ITU 公理 + 実用 inset)** ← 本論文
 3. Cogitate IIT/GNW (2027, 意識)
 4. LISA SMBH (2035, 重力 + ITU)
 5. JWST/Euclid (2025-30, 宇宙論)

mKQEC は最も早期に投資収益が見える Pass-2 priority。
```

## Industry partnership 戦略

```
Letter of Intent (LOI) candidates:
 Quantinuum (UK + Honeywell, US): trapped-ion biased noise dominant
 → First choice for Phase 1 implementation
 PsiQuantum (US): photonic erasure
 → Phase 2 (2028) target
 Google Quantum AI: superconducting Willow
 → Phase 3 (2028-29), cross-validation
 
Initial 接触:
 - arXiv preprint で attention 喚起
 - 2026.10 NeurIPS / QIP 2027 で発表
 - Direct outreach to Google QAI / Quantinuum CTO
```

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #QC #mKQEC #ExperimentalRoadmap #Quantinuum #PsiQuantum #Pass2Pillar1 #Phase351
