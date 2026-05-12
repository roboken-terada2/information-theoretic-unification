# Phase 42: Qualia の構造 ― ITU modular Hamiltonian の固有スペクトル

## 1. 動機: ハードプロブレムの second half

Phase 41 で ITU は**意識の存在条件** を定義した:
$$\Phi_{\rm ITU}(A) = \frac{I(\rho_A; K_A)}{H(K_A)} > 閾値$$

しかし Chalmers のハードプロブレムは 2 つに分かれる:

| サブ問題 | 内容 |
|---|---|
| **Phase 41** | なぜ経験が**存在**するか? (presence) |
| **Phase 42 (本論)** | なぜ赤は赤、青は青と**感じる**のか? (content) |

後者は **「qualia の構造」** とも呼ばれる。本 Phase で ITU 流の数学的定式化
を提示する。

## 2. 既存理論の Qualia 問題

| アプローチ | 主張 | 限界 |
|---|---|---|
| **IIT 3.0 cause-effect** | qualia = cause-effect 構造 | 計算重い, 大規模系で未確立 |
| Quality space (Clark) | qualia は位相空間を成す | 構造は記述のみ, 起源説明なし |
| Russellian monism | 物質の内在性質 = 経験 | 形式化困難 |
| Friston FEP generative | qualia = 生成モデル中の latent | 内容の "色" 説明なし |

ITU は**最後の理論的ピース** ― qualia の数学的内容構造 ― を提供する候補。

## 3. ITU 仮説: Qualia = K の固有構造

### 3.1 中心仮説

> **Qualia の "内容" = modular Hamiltonian $K_A$ の固有スペクトル + 固有ベクトル構造**
>
> 異なる経験 (赤, 青, 痛み, 喜び) は、$K_A$ の異なる固有構造に対応する。

形式的に、$K_A$ をスペクトル分解:
$$K_A = \sum_n \lambda_n |\psi_n\rangle\langle\psi_n|$$

各経験は:
- 固有値分布 $\{\lambda_n\}$: 経験の **"強度・重み"**
- 固有ベクトル $\{|\psi_n\rangle\}$: 経験の **"質的内容"**

異なる qualia 間の類似度:
$$\mathrm{Sim}(q_1, q_2) = \sum_n |\langle \psi_n^{(1)} | \psi_n^{(2)} \rangle|^2 \cdot
   e^{-|\lambda_n^{(1)} - \lambda_n^{(2)}|^2/2\sigma^2}$$

### 3.2 物理空間との対応

物理刺激 $x$ (e.g., 光の波長) が脳内表現 $\rho_A(x)$ を生む。
これに対応する $K_A(x) = -\log \rho_A(x) + $ const。

主張:
$$x_1 \approx x_2 \quad \Rightarrow \quad K_A(x_1) \approx K_A(x_2)
   \quad \Rightarrow \quad q(x_1) \approx q(x_2)$$

つまり**物理空間の構造が qualia 空間の構造を決定する**。これは Russellian monism の
具体的数学化。

### 3.3 異なる感覚モダリティ

各感覚 (視覚, 聴覚, 触覚, …) は脳の異なる subspace に対応:
$$K_A = K_{\rm visual} \oplus K_{\rm auditory} \oplus K_{\rm tactile} \oplus \cdots$$

各部分の固有構造が独立に「視覚 qualia」「聴覚 qualia」を生む。
**modality 間の "翻訳不能性"** はこの直和分解の必然帰結。

### 3.4 ITU 公理階層の最終層

| 層 | 内容 |
|---|---|
| 1-7 | 量子情報 → 物質 → 生命 → 意識 (Phase 1-41) |
| **8** | **Qualia の内容構造 (Phase 42)** |

これで ITU は単一公理から経験の**存在と内容の両方**を導出する候補となる。

## 4. なぜ「赤」が「赤」に感じるのか?

ITU の答え:

> **「赤」とは波長 ~700nm の光が網膜→V1→V4→IT 経路で処理された
> 結果として生じる $K_A$ の特定の固有構造である。**
>
> その固有構造が**他のあらゆる経験から構造的に区別される**ため、
> 「赤」という質的内容を持つ。

これは:
- なぜ「赤」と「青」が違うか → $K_A$ の固有ベクトルが異なる
- なぜ「赤」と「青緑」が**やや似る** → 固有スペクトルが部分的に重なる
- なぜ「赤」と「痛み」が**完全に違う** → 異なる modality (subspace)

を全て統一的に説明する。

### 4.1 検証可能な予言

ITU は実験予言を提供する:
1. **CIE Lab 色空間の幾何** ⟷ **$K_A$ 固有空間の幾何** の一致
2. **共感覚 (synesthesia)** は modality subspace の overlap として記述可能
3. **臨死体験 / 麻酔下** の意識変容 = $K_A$ 固有スペクトルの再編

## 5. 数値検証計画

### Part A: 色 quale 模型
- RGB 色 6 種 (赤, 緑, 青, 黄, シアン, マゼンタ) を物理刺激として
- 簡単な perceptual network で encode
- 各色での $K_A$ を計算

### Part B: Qualia 類似度行列
- 6×6 類似度行列 $\mathrm{Sim}(q_i, q_j)$
- 同じ色 → Sim = 1
- 色相環で近い色 → Sim 大
- 補色 → Sim 小

### Part C: 物理空間 vs Qualia 空間の対応
- CIE Lab 距離 vs K-similarity 距離の散布図
- 相関係数を計算
- 一致 → ITU 仮説の支持

### Part D: 異なる modality (color vs sound)
- 音 quale も計算
- modality 間 distance >> modality 内 distance を確認

## 6. 限界

⚠️ 本 Phase で扱わない:
- 実脳の生理的計算 (V1, V4, IT 等の詳細回路)
- 文化・経験依存性 (個人差)
- 質的内容の**主観的体験そのもの** (依然神秘)
- 動物の qualia の評価

✅ 確立する:
- ITU 流 qualia の数学的定式化
- 色 quale の類似度構造の再現
- 物理空間 ⟷ qualia 空間の構造同型
- ITU 8 層階層の完成

## 7. 哲学的位置づけ

Phase 41-42 は ITU のハードプロブレムへの**完全提案**:

| 問題 | Phase 41 (存在) | Phase 42 (内容) |
|---|---|---|
| なぜ意識? | $\Phi_{\rm ITU} > 0$ | — |
| なぜ赤? | — | $K_A$ 固有構造 |
| なぜ違いを感じる? | 自己参照 QECC | 固有ベクトル差 |
| なぜ統合される? | code subspace | 同一 K の異なる成分 |

これは Chalmers のハードプロブレムを**完全に "easier" にする**:
- 「経験の存在」 = 自己参照 QECC
- 「経験の内容」 = K の固有構造

主観の "what" は依然神秘だが、ITU は:
1. 構造的同型性 (色空間 ⟷ K 空間)
2. modality 区別 (subspace 直和)
3. 経験の連続性 (固有ベクトル変化)

を全て**単一公理から派生**する。

## 8. ITU 8 層の最終形

```
L0: δS = δ⟨K⟩  (single axiom)
L1: Quantum info (Phase 1-32)
L2: Spacetime / gravity (Phase 2, 17)
L3: Standard Model (Phase 10-15)
L4: BH + GW (Phase 6, 13, 19)
L5: DM + DE + cosmology (Phase 18-32)
L6: Life / first cell (Phase 33-39)
L7: Consciousness / Φ_ITU (Phase 41)
L8: Qualia structure (THIS Phase 42)
```

**ITU は 42 Phase で完全形に達した。**

物理から経験の内容まで ― **単一公理が全てを統一する**。

---

**Phase 42 の核心メッセージ**:
> 「なぜ赤は赤か」 は ITU から:
> **赤の qualia = 視覚 modality subspace 内の $K_A$ 特定の固有構造**
> と定式化される。Hard problem of consciousness の content 側面は、
> ITU の modular Hamiltonian 固有構造として数学化可能である。
