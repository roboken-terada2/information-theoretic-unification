# Phase 350: Google Willow 2024 vs mKQEC 

## Google Willow (2024.12 Nature) — Pass-1 で扱った範囲

```
Google Quantum AI (Hartmut Neven 主導):
 チップ: Willow
 Qubits: 105 superconducting transmons
 Code: distance-3, -5, -7 surface code
 Result: 各 step で logical error 2.14× reduction (below threshold!)
 Achievement: "exponential error suppression"
 Year: 2024.12.9 announcement, Nature publication
 
Significance: 
 - First demonstration of surface code beating physical qubit error
 - Threshold definitively reached
 - Scaling path to fault tolerant quantum computer (FTQC) opened
```

## mKQEC との直接比較 (predicted)

### Setup 1: Google Willow noise model (superconducting transmon)

```
Noise characteristics:
 T1 ≈ 100 μs (relaxation)
 T2 ≈ 100 μs (dephasing)
 Gate error ≈ 10^-3 per 2-qubit
 Asymmetry: small (T1 ≈ T2)

mKQEC prediction:
 非対称性小 ⇒ surface code に近い performance
 改善余地: 5-10% (marginal)
```

### Setup 2: Quantinuum trapped-ion (T1/T2 highly asymmetric)

```
Noise characteristics:
 T1 ≈ 60 sec (very long relaxation)
 T2 ≈ 1-2 sec (much shorter coherence)
 Gate error ≈ 10^-3 per 2-qubit
 Asymmetry: T1/T2 ≈ 30-60 (highly biased)

mKQEC prediction:
 非対称性大 ⇒ Z-biased mKQEC が surface code を 30-50% 超越
 Quantinuum H2 (2024, 56 qubits) で実証 candidate
```

### Setup 3: PsiQuantum photonic (erasure dominant)

```
Noise characteristics:
 Photon loss (erasure with known position)
 Erasure rate ≈ 1-5% per gate
 Computational basis errors << erasure

mKQEC prediction:
 Erasure-aware mKQEC が surface code を 2-3x 超越 (theoretical)
 PsiQuantum Omega chip (2025+) で実証 candidate
```

## 実装ハードウェア・タイムライン (predicted)

| Year | Platform | mKQEC demo | Comparison metric | 期待結果 |
|---|---|---|---|---|
| 2026 | Stim simulator | 数値検証 | Logical error vs surface | 30-50% improvement (biased) |
| 2027 | Quantinuum H3 | First hardware | Z-biased mKQEC d=3,5 | 30%+ over surface |
| 2028 | PsiQuantum | Photonic mKQEC | Erasure-aware code | 2-3x over surface |
| 2029 | IBM Heron | Superconducting mKQEC | Threshold scaling | 5-15% improvement |
| 2030 | Microsoft Majorana | Topological + mKQEC | Combined approach | Speculative |

## ITU vs 現状の brick-and-mortar QC theory

```
現状 (2024):
 - Surface code dominant (Google, IBM, Quantinuum 採用)
 - XZZX biased variant 部分的採用 (Tuckett 2020)
 - 各 noise に対し ad-hoc code 設計 (経験的)
 
ITU (mKQEC) 仮説:
 - Noise model から code を **構成的に導出**
 - 統一 framework: 単一 K_QC^(0) operator から全 code 派生
 - Fault-tolerant era 2-3 yr 前倒し possible
```

## 高インパクト査読論文 / Turing Award への path

```
主要査読論文 (実証時):
 1. mKQEC theoretical paper (PRX 2027)
 2. 数値検証 (PRX 2027 Q3)
 3. Hardware demo (Quantinuum/PsiQuantum 2027-28)
 4. 30%+ over surface code 確認 (2028-29)
 5. Fault-tolerant logical qubit demonstration (2030-32)
 6. wider review window 2032-2035

Turing Award (実装時):
 - 実用 FTQC コンパイラ (2030-2035)
 - Industry 採用 (Google/IBM/Microsoft)
 - Practical advantage demonstrated
 - Award opportunity 2035-2040
```

## 関連実装企業 (2024-25 status)

```
Google Quantum AI: Willow 105 qubits (2024.12)
IBM Quantum: Heron 156 qubits (2024)
Quantinuum: H2 56 trapped-ion qubits (2024)
Microsoft: Majorana-1 topological (2024 Nature)
PsiQuantum: Photonic, Omega chip 2025
IonQ: Forte 32+ trapped-ion qubits
Atom Computing: Neutral atom 1180 qubits (2024.10)
Rigetti: Ankaa-3 (2024)
QuEra: Aquila 256 neutral atom
日本: 富岳量子 (理研), NEC, NTT, 富士通
中国: Pan Jianwei 祖冲之 (Zuchongzhi-2)
```

## 直接的 industry collaboration 戦略 (Pass-1.5 #1 派生)

```
mKQEC で接触するべき企業:
 Google Quantum AI: Surface code 改善需要、Willow extension
 Quantinuum: Trapped-ion biased noise 既存
 PsiQuantum: Erasure-dominant photonic
 Microsoft Azure Quantum: Cross-platform compiler 興味
 
学術: 
 Caltech (Preskill), MIT (Chuang), Yale (Devoret), Delft (Kouwenhoven)
 IQOQI (Briegel), 慶應 (Yamamoto), CQC (RIKEN)
```

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #QC #mKQEC #GoogleWillow #Quantinuum #PsiQuantum #Microsoft #IBM #Phase350
