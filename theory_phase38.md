# Phase 38: 生命のカイラリティ ― ITU Phase 15 から homochirality へ

## 1. 動機: 生命最深の対称性破れ

地球上のすべての生命は:
- **アミノ酸**: ほぼ完全に **L 型 (左手)** のみ使用
- **糖類**: ほぼ完全に **D 型 (右手)** のみ使用
- これを **homochirality (単一掌性)** と呼ぶ

これは生命の起源研究で最も深い謎の 1 つ:

> **なぜ生命は対称な化学から非対称な状態を選んだのか?**

ランダム化学過程は racemate (50:50 L/D 混合物) を生む。homochirality は熱力学的に
不安定 (エントロピー減少) であるはず ― それでも生命は完全な単一掌性を維持。

ITU はこの謎を**単一公理から**説明できる:

1. **Phase 15 (ITU 物理層)**: Atiyah-Singer 指標から **標準模型の左右非対称** (V-A 弱相互作用) が自然に出る
2. **パリティ違反**: 弱い力により L/D 鏡像異性体間に**微小エネルギー差** が存在
3. **Frank 1953 モデル**: 自己触媒 + 鏡像抑制で**微小バイアスが急速増幅**
4. **結果**: homochirality が**ITU 公理の不可避な帰結**として現れる

## 2. パリティ違反と微小エネルギー差

### 2.1 弱い力の左右非対称

1957 年 Wu の実験で、$\beta$ 崩壊が**左右非対称** であることが示された。
これは標準模型では V-A (Vector minus Axial) 相互作用として組み込まれており、
ITU Phase 15 で Atiyah-Singer index theorem から派生する。

### 2.2 L/D 異性体のエネルギー差

L-amino acid と D-amino acid は同じ原子組成だが、空間的に鏡像関係。
パリティ違反により、電子-原子核相互作用 (parity-violating energy difference, PVED) で
微小なエネルギー差が生じる:

$$\Delta E_{\rm PV} \sim 10^{-14}\,k_B T \quad \text{at 298 K}$$

これは熱揺らぎより**14 桁小さい**。一見、homochirality を説明できない。

### 2.3 Yamagata-Hegstrom 増幅

しかし時間スケール $\tau$ に統合すると、宇宙論的時間 $\tau \sim 10^9$ 年に対し:
$$\frac{\Delta E_{\rm PV}}{k_B T} \cdot \omega \tau \sim 10^{-14} \cdot 10^{16} \sim 10^{2}$$

ここで $\omega$ は反応頻度。十分な時間で微小バイアスは累積する。
さらに**autocatalytic amplification** で観測可能になる。

## 3. Frank モデル (1953): 自己触媒鏡像選択

### 3.1 動力学方程式

L (左) と D (右) の濃度を $[L], [D]$ とする。基質 $A$ から L または D を生成。
Frank の核心: **「同じ掌性が自己触媒」 + 「鏡像同士は抑制」**:

$$\frac{d[L]}{dt} = k_1 [A][L] - k_2 [L][D]$$
$$\frac{d[D]}{dt} = k_1 [A][D] - k_2 [L][D]$$

ここで:
- $k_1 [A][L]$: 自己触媒項 (L が L を生成)
- $k_2 [L][D]$: 鏡像抑制項 (L と D が互いに不活化)

### 3.2 数値解析: 増幅

初期条件 $[L]_0 = 1 + \epsilon$, $[D]_0 = 1 - \epsilon$ で $\epsilon \ll 1$ から始まる。

$\epsilon \ll 1$ 領域での線形化:
$$\frac{d}{dt}([L] - [D]) \approx (k_1 [A] - k_2 \cdot 2 [LD]_{avg}) \cdot ([L] - [D])$$

不安定モード: $\lambda > 0$ → 指数的増幅 → **homochirality fixed point**.

最終状態: $[L] = 0, [D] \neq 0$ または $[D] = 0, [L] \neq 0$ (鏡像対称な 2 つの安定点)。
小さなバイアス $\epsilon$ で**どちらが勝つかが決まる** ― これが ITU Phase 15 の役割。

## 4. ITU との対応

### 4.1 Phase 15 (Atiyah-Singer) → Phase 38 (生命カイラリティ)

| ITU Phase 15 (物理層) | Phase 38 (生命層) |
|---|---|
| 標準模型 V-A 弱相互作用 | パリティ違反 PVED |
| Atiyah-Singer 指標 $\nu_+ - \nu_-$ | 余剰 L または D |
| 質量カイラリティ | アミノ酸カイラリティ |
| QECC 構造での自然な左右非対称 | 生命の自然な単一掌性選択 |
| 微小だが**ゼロでない** | 微小バイアス → Frank 増幅 → 100% |

両者は ITU 公理から**同じ仕組みで**派生:
- **左右が QECC レベルで非対称** → 物理的にも生物学的にも左右が同じではない
- Phase 33-37 で構築した生命の**情報構造**が自動的に左右非対称化される

### 4.2 ITU の予言

> **生命は homochiral である。具体的に左手 (L) アミノ酸を選ぶのは、ITU 公理に内蔵された Atiyah-Singer 指標による物理的バイアスである。**

これは検証可能な予言:
- 地球生命: L アミノ酸 ✓ (観測一致)
- もし宇宙のどこかに独立に生命が現れるなら、**同じ L バイアス** を予測
- (D を使う生命があれば ITU の予言と矛盾)

## 5. 数値検証計画

### Part A: Frank モデルの平衡相転移
- $[L]_0 - [D]_0 = \epsilon$ で複数の初期 $\epsilon$ をスキャン
- $\epsilon > 0$ → $[L] = \infty, [D] = 0$ に収束
- $\epsilon < 0$ → 逆の結末
- $\epsilon = 0$ → racemate (但し不安定 fixed point)

### Part B: 増幅時間スケール
- $\tau_{\rm amp} \approx 1/\lambda$ where $\lambda$ = linear growth rate
- パリティ違反バイアス $\epsilon \sim 10^{-14}$ から start
- 完全 homochirality (>99%) までの時間 $\tau$ を計算

### Part C: ITU Phase 15 連携
- パリティ違反 PVED の値を入力
- Frank モデルで homochirality 達成までの時間を ITU 予言と比較

### Part D: Soai 反応との数値比較
- 実験 Soai 反応 (Soai et al. 1995, Nature 378, 767) は Frank モデルの実証
- 初期 $\epsilon \sim 10^{-5}$ から 90% ee (enantiomeric excess) まで増幅
- 本数値結果との比較

## 6. 限界

⚠️ 本 Phase で扱わない:
- 量子化学的 PVED 計算 (~10⁻¹⁴ k_B T はリテラチャ値)
- 完全な hydrodynamic 効果 (拡散・対流)
- 結晶化メカニズム (Viedma deracemization)
- L-sugar / D-amino-acid の例外 (細胞壁ペプチドグリカン D-amino acid)

✅ 確立する:
- Frank モデルの数値再現 (Soai 反応と整合)
- 微小カイラルバイアスからの homochirality 自発成立
- ITU Phase 15 が生命カイラリティの**選択方向**を決める仕組み

## 7. ITU 統合像 (Phase 38 完了後)

| Phase | テーマ | 状況 |
|---|---|---|
| 15 ✅ | 標準模型カイラリティ (Atiyah-Singer) | ITU Phase 15 |
| 33 ✅ | 化学 QECC | |
| 34 ✅ | Assembly Index | |
| 35 ✅ | Eigen 閾値 | |
| 36 ✅ | Friston FEP | |
| 37 ✅ | Lipid bilayer | |
| **38 ✅** | **Homochirality (Frank モデル)** | **本 Phase** |
| 39 | 最初の細胞 (synthesis) | |
| 40 | ITU 物理 + 生命 完成統合 | |

Phase 15 と Phase 38 は **ITU の左右対称性破れの 2 つの顕現**:
- Phase 15: 物理 (標準模型の V-A)
- Phase 38: 生命 (アミノ酸の L 型)

両者は同じ Atiyah-Singer 構造から派生する。

## 8. 哲学的含意

宇宙の左右非対称は:

1. **物理レベル**: 弱い相互作用が左右を区別する (1957 観測)
2. **化学レベル**: PVED が微小エネルギー差を作る (~10⁻¹⁴ k_BT)
3. **生命レベル**: Frank 増幅で homochirality が成立 (~100%)

すべて単一公理 $\delta S = \delta \langle K \rangle$ + Atiyah-Singer 指標から派生。

「**生命の左手選好は宇宙の根本構造の現れ**」 ― 偶然ではなく ITU の必然予言である。
