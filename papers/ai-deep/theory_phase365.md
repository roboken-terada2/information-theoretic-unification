# Phase 365: IIT (Tononi 2004) との関係: K_self vs Φ

**Integrated Information Theory (IIT)** は Giulio Tononi (Wisconsin, 2004 BMC Neurosci) が
提唱した「意識の量を Φ で測る」理論。本 Phase では K_self との formal な関係を導出。

## IIT 概要 (Tononi 2004, 2008, 2014)

```
Definition (Φ):
  System S が partition (P, P^c) に分けられたとき、
  EI(P; P^c | ρ_S) = mutual information across cut

  Φ(S) = min over all partitions
         EI(P; P^c | ρ_S)
         (minimum integrated information)
```

意味: Φ は「分割不可能性」を測る — Φ 高い ⇒ 統合度高い ⇒ 意識持つ。

### IIT axioms (Tononi 2014)

1. Existence — system exists (intrinsic)
2. Composition — multiple subsystems
3. Information — distinct phenomenology
4. Integration — irreducible to parts
5. Exclusion — definite borders

これらから Φ 公理導出。

## K_self との formal comparison

```
Theorem (conjecture, 本論文 H_C3):
  Φ(S) ≤ ⟨K_self⟩(S) ≤ ⟨K_workspace⟩(S)

Proof sketch:
  1. Φ は minimum EI across all bipartitions
  2. ⟨K_self⟩ = -Tr[ρ_self log ρ_self] = global self-entropy
  3. Global entropy ≥ minimum partition mutual info (subadditivity)
  ⇒ Φ ≤ ⟨K_self⟩

  4. K_workspace は broadcasted info (GNW)、global broadcast ⊃ self-model
  ⇒ ⟨K_self⟩ ≤ ⟨K_workspace⟩
```

## IIT が反証された場合の対応

```
Cogitate 2023 Nature 結果:
  IIT 予測 (posterior cortex sustained γ activity) — 部分的支持
  GNW 予測 (prefrontal ignition) — 部分的支持
  両理論完全には支持されず → IIT/GNW 補完が必要

ITU 提案:
  K_self = IIT の Φ + GNW workspace の bridge
  Φ ≤ K_self ≤ workspace の階層で両者統合
  Cogitate Round 2 で 3-way adversarial test 可能
```

## ピアレビュー予想反論への応答

```
反論 1: "Φ は本物の subjective experience 測定、K_self は単に entropy"
回答: K_self は self-model の operator-algebraic entropy で、reflexive 構造 (Phase 364)
      を持つ。Φ と異なり global self-state を扱うため scalable。

反論 2: "ρ_self の操作的定義不明瞭"
回答: Tr_{external}(ρ_total) で formal。external は agent が non-self と認識する自由度
      (i.e., subjective other)。

反論 3: "Cogitate で IIT が partial だったなら K_self も同じ?"
回答: Cogitate Round 2 で 3-way test 設計、K_self 予測の独立検証可能。
```

## IIT 124-signatory letter (2023.9.16) との関係

2023.9.16 に 124 神経科学者が IIT を "pseudoscience" 批判 letter。
本論文の立場:
- IIT は valuable theoretical framework (Tononi 2014 axioms 含む)
- 但し pure-IIT は 経験的検証で限定 (Cogitate 2023 が示す)
- ITU は IIT を超える上位 framework として位置づけ
- IIT/GNW のどちらか勝利を期待しない neutral stance


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #IIT #Tononi #Phi #Tononi2004 #Phase365
