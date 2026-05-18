# Phase 354: H1 厳密化 — Lindblad 定常状態の一意性 (Davies-Frigerio) 

H1 (Phase 347): "Open quantum system has unique steady state ρ_∞"
は **Davies 1974 / Frigerio 1977-1978** の定理で形式化できる。

## Lindblad 半群の基礎

Open quantum system は Lindblad master equation:
```
dρ/dt = L(ρ) := -i[H, ρ] + Σ_k γ_k (L_k ρ L_k† - 1/2 {L_k† L_k, ρ})
```
ここで `L` (Lindbladian) は **completely positive trace-preserving** semigroup の生成子。

## Davies (1974, CMP) 定理

```
Theorem (Davies 1974):
 weakly-coupled system + heat bath (Born-Markov approximation) で
 reduced dynamics は Lindblad form を取り、 KMS state は steady state。
```

これは **物理的 derivation**: 弱結合極限で Lindblad 等式が出る。

## Frigerio (1977/1978) 一意性定理

 **本論文の H1 を厳密に確立する核心定理** 

```
Theorem (Frigerio 1977, CMP 63):
 Lindbladian L が faithful normal stationary state ρ_∞ を持ち、
 {H, L_k, L_k†} の commutant が C·I (即ち 全 algebra を生成) ならば、
 ρ_∞ は唯一の steady state。

Theorem (Frigerio 1978, Rep. Math. Phys.):
 全 ρ for which L(ρ)=0 が一次元 ⇔ Lindblad semigroup が relaxing
 (即ち lim_{t→∞} e^{tL}(ρ) = ρ_∞ for all initial ρ)
```

## H1 の formal version

```
H1 (formal):
 Lindbladian L が以下を満たすとき K_QC^(0) は well-defined:
 (a) Faithful normal stationary state ρ_∞ ∈ S(H) が存在
 (b) {H, L_k}_{k=1}^N の生成する algebra が B(H) (i.e., irreducible)
 (c) Det(ρ_∞) > 0 (full rank)
 
 ⇒ K_QC^(0) ≡ -log ρ_∞ ∈ B_sa(H) は有界自己共役、唯一
```

## Lindbladian spectrum と spectral gap

```
σ(L) ⊂ {λ ∈ ℂ: Re λ ≤ 0}
ρ_∞ ⟺ eigenvalue 0 (kernel)
spectral gap δ := -max{Re λ: λ ∈ σ(L) \ {0}}

Relaxation time: τ_relax = 1/δ
Convergence: ||e^{tL}(ρ) - ρ_∞||_1 ≤ C e^{-δt}
```

### 重要観察

```
spectral gap δ(L) が **mKQEC threshold** に直接効く
 (Phase 359 で証明)
 
Surface code (depolarizing): δ(L_depol) = γ (decoherence rate)
Biased noise: δ(L_biased) = γ_Z + δ_X (multi-scale)
Erasure: δ(L_erasure) = γ_erase

⇒ mKQEC threshold ∝ δ(L) / max eigenvalue of K_QC^(0)
```

## 既知 noise model の Lindbladian spectrum

| Noise | Lindbladian | Gap δ | K_QC^(0) structure |
|---|---|---|---|
| Depolarizing (rate γ) | Σ_α γ/3 ρ_α (Pauli) | γ | trivial (I) |
| Amplitude damping (rate Γ) | Γ σ_- σ_+ | Γ/2 | Z-biased |
| Phase damping (rate γ_φ) | γ_φ/2 (Z ρ Z - ρ) | γ_φ | Z-strong bias |
| T1/T2 noise | combined Γ + γ_φ | min(Γ/2, γ_φ) | mixed bias |
| Erasure (rate ε) | ε (|0⟩⟨e| ⊗ |e⟩⟨0|) | ε | photon-bias |

各 noise model に対し:
1. ρ_∞ 解析的 (small system) or numerical (large) で計算
2. K_QC^(0) = -log ρ_∞ 構築
3. Commutant + MASA で stabilizer 抽出

## 既存文献接続

```
Lindblad G. (1976) CMP 48: master equation 公理化
Davies E.B. (1974) CMP 39: weak coupling derivation
Frigerio A. (1977, 1978): 一意性定理 本論文の core
Alicki R. (1976) Rep. Math. Phys.: detailed balance
Spohn H. (1976): irreversibility
Kossakowski A. (1972): semigroups
Gorini-Kossakowski-Sudarshan (1976) JMP: GKS master equation

最近:
 Cubitt-Lucia-Michalakis-Pérez-García (2015) Nat Comm:
 spectral gap 計算可能性 (Turing 不可決定 in general)
 Kastoryano-Temme (2013) JMP:
 Lindbladian で entropy production rates
```

## 反証可能性

```
H1 反証シナリオ:
 (a) 不在: Lindbladian が steady state を持たない (escaping system)
 → ρ_∞ 未定義 → K_QC^(0) 未定義 → mKQEC 構成不可
 
 (b) 非一意: 多重 steady state (glassy phase, dark state subspace)
 → 各 steady state で異なる K_QC^(0)
 → mKQEC は dark state 内に閉じ込められる
 
 (c) 縮退: ρ_∞ が rank-deficient (det = 0)
 → K_QC^(0) 発散
 → modular flow ill-defined

実際の物理系で (a)-(c) のいずれが起きるか:
 - Cavity QED (Jaynes-Cummings) → ρ_∞ unique typically OK
 - 多体局在 (MBL) → 非一意可能 → mKQEC 制限
 - Decoherence-free subspaces → 縮退、care needed
```

## H1 結論

```
H1 (rigorous):
 Frigerio 1977-78 定理により、weakly-coupled Lindblad system では
 unique faithful steady state ρ_∞ が普通の物理系で存在し、
 K_QC^(0) = -log ρ_∞ は well-defined operator。
 
 Pass-2 で各実機 (Quantinuum, PsiQuantum 等) の Lindbladian を
 experimentally 同定し、ρ_∞ を測定 → K_QC^(0) を再構成。
 
 H1 反証パスウェイ明確 (dark state, MBL 等).
```

 H1 は数学的に堅牢、物理的に検証可能。

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #QC #mKQEC #H1rigorous #Davies #Frigerio #LindbladSemigroup #Phase354
