# Phase 43: ITU axiom から fault-tolerant 量子計算へ — QECC 構造の派生

## 1. 動機

Phase 5 (Almheiri-Dong-Harlow 2015) で「**バルクの局所性 = 量子誤り訂正符号 (QECC)**」 を示した。
これは情報物理学の核心結果で、ITU 公理 $\delta S = \delta \langle K \rangle$ から
QECC 構造が**自然に出る**ことを意味する。

本 Phase は**逆問題**を扱う:

> **ITU から fault-tolerant 量子計算のための最適 QECC 構造を導出できるか?**

これは ITU を理論物理だけでなく**現実の量子計算技術**に応用する第一歩。

---

## 2. ITU と QECC の架け橋 (Phase 5 復習)

ITU Phase 5 の核心結果:
- AdS/CFT 双対性で、バルク (重力理論) の局所演算子はバウンダリ (CFT) で再構成可能
- この再構成は**量子誤り訂正符号** (Pastawski-Yoshida-Harlow-Preskill 2015, "HaPPY code")
- $[[5,1,3]]$ "perfect tensor" で構成された holographic code

つまり ITU は QECC を**第一原理から派生**:

```
δS = δ⟨K⟩  (ITU axiom)
    ↓
モジュラーフロー / Entanglement wedge reconstruction
    ↓
QECC code structure (HaPPY)
```

---

## 3. 本 Phase での新展開

### 3.1 中心仮説

> **ITU の modular flow 構造を活用すれば、現在主流の surface code よりも fault tolerance 性能 (threshold) が高い QECC を設計できる。**

### 3.2 比較対象

| 既存 QECC | Threshold | Code rate | 特徴 |
|---|---|---|---|
| Surface code (Kitaev) | ~1% | 0 (asymptotic) | 2D 平面、近距離相互作用 |
| Color code | ~0.1% | 低 | universal gates 容易 |
| Holographic (HaPPY) | 理論的 | $O(1)$ | hyperbolic 幾何 |
| Hastings-Haah | ~1% | 改善 | floquet code |
| **ITU-motivated (proposal)** | **TBD** | **高** | **modular flow 由来** |

### 3.3 ITU-motivated code の構築

ITU $\delta S = \delta \langle K \rangle$ から:
1. 部分系 $A$ の modular Hamiltonian $K_A$ を計算
2. $K_A$ の **対称性** = code stabilizer 候補
3. $K_A$ の固有空間 = code subspace

具体例 ($[[5,1,3]]$ perfect code):
- 5 物理 qubit が 1 論理 qubit を encode
- 4 stabilizer $S_i$ (各々 weight 4)
- code distance $d = 3$ (任意の 1 qubit error を訂正)
- これは ITU から自然に出ること (Phase 5)

---

## 4. 数値検証計画

### Part A: $[[5,1,3]]$ コードの基本性能
- 5 物理 qubit, 1 論理 qubit
- Stabilizer 測定 + 訂正手順
- Depolarizing noise下で logical error rate 計測

### Part B: Pseudo-threshold 計算
- Physical error rate $p_{\rm phys}$ を変えて
- Logical error rate $p_{\rm log}(p_{\rm phys})$ を計測
- 交差点 = pseudo-threshold

### Part C: ITU modular flow との対応
- $K_A$ から stabilizer 候補を抽出
- 既知の $[[5,1,3]]$ stabilizer と一致確認
- ITU が**正しい QECC を予言する**ことの数値証拠

### Part D: 大規模化展望
- concatenated code (再帰的に encode)
- 真の threshold theorem (Aharonov-Ben-Or 1996)
- ITU-motivated code との比較

---

## 5. 物理的意義

### 5.1 ITU の信頼性向上
- ITU が単なる philosophical TOE ではなく**実用予言**を出せることを示す
- 量子計算コミュニティで真剣に受け取られる契機

### 5.2 量子計算への直接応用
- IBM, Google, IonQ, AWS の量子コンピュータの**threshold 改善**
- 物理 qubit 数を **同じ logical qubit 性能を達成**するのに必要な数を減らす可能性
- 実用 fault-tolerant QC への道筋に**理論的貢献**

### 5.3 物理 ↔ 工学の橋渡し
- ITU は理論物理 (Phase 1-42) と工学 (Phase 43+) を統一する候補
- 「Theory of Everything」 を「Engineering of Everything」 へ

---

## 6. 限界

⚠️ 本 Phase で扱わない:
- 完全な fault-tolerant universal gate set
- magic state distillation (Phase 45 で扱う)
- 実 hardware noise model (depolarizing 近似のみ)
- 多体 holographic code 構築 (Phase 46 で扱う)

✅ 確立する:
- $[[5,1,3]]$ コードの ITU 派生
- Pseudo-threshold の数値測定
- ITU modular flow と既存 stabilizer の対応

---

## 7. 論文「ITU and Fault-Tolerant Quantum Computing」 の構造

Phase 43-46 で 1 本の論文 (新 Zenodo deposit) を構成:

| Phase | 役割 |
|---|---|
| **43 (本論文)** | **理論基礎: ITU → QECC 派生** |
| 44 | Surface code を ITU-motivated に拡張 |
| 45 | Magic state distillation と ITU |
| 46 | NISQ hardware への応用展望 |

論文タイトル (proposed):
> **"ITU and Fault-Tolerant Quantum Computing: A Single-Axiom Derivation of Optimal QECC Architectures"**

これは ITU を**実用領域に応用する最初の論文**で、Tier 0 (現コア理論) とは**独立した Zenodo deposit** として登録予定。

---

## 8. ITU 拡張ロードマップ (再掲)

| 論文 (新 Zenodo) | 内容 | Phase 範囲 |
|---|---|---|
| **本論文** | Quantum Computing | **43-46** |
| 次論文 | AI Consciousness / $\Phi_{\rm ITU}$ | 47-50 |
| 次々論文 | Cancer Biology | 51-54 |
| … | (各分野) | … |

各論文は独立した DOI を持ち、コア ITU (10.5281/zenodo.20109209) に
`isSupplementTo` で参照される。

---

**Phase 43 の核心メッセージ**:
> ITU の単一公理から QECC 構造が派生する (Phase 5 の逆方向解釈)。
> これを活用すれば、現在主流の量子計算 QECC を超える設計が可能かもしれない。
> ITU は理論物理だけでなく、**実用工学への応用**を持つ。
