# Phase 34: Assembly Theory と ITU ― 生命を測る情報量

## 1. 動機

Phase 33 で「生命 = 化学的 QECC」 という ITU 延長仮説を確立した。
しかし1つの未解決問題が残る:

**実際の分子を見て「これは生命由来か?」を判定できる量はあるか?**

2023 年に Sharma, Liu, Jirasek, Cronin, Walker らが Nature に発表した
**Assembly Theory (AT)** がこの問題に直接答える: 分子の **Assembly Index (AI)**
が一定値を超えると、その分子は**自己複製・選択を経た生命由来**だと統計的に
区別できる。

本 Phase で AT と ITU を統合し、AI = QECC depth の対応を確立する。

## 2. Assembly Theory の核心

### 2.1 Assembly Index (AI)

分子 $O$ の Assembly Index $a(O)$ は:

> **$O$ を初等構成要素から作るのに必要な最小の "結合操作" 回数**

各結合操作で生成された中間物は再利用可能 (= memory)。

例 (文字列):
- `"ABC"` (3 文字、全て異なる) → AI = 2 (A+B=AB, AB+C=ABC)
- `"AAAA"` (反復) → AI = 2 (A+A=AA, AA+AA=AAAA) ※ AA を再利用
- `"ABCABCABC"` (反復) → AI = 4 (A+B=AB, AB+C=ABC, ABC+ABC=ABCABC, ABCABC+ABC=ABCABCABC)

### 2.2 Assembly 方程式

$N$ コピーの分子が存在する場合の**全体アセンブリ量** $A$:
$$A = e^{a(O)} \cdot N$$

これは「**この複雑性レベルの分子が偶然に $N$ 個存在する確率**」と対応。

### 2.3 生命の閾値

実験データ (Cronin lab の mass spec.):
- ランダム化学プロセス: $a < 8$ がほぼ全て
- 既知の生命由来分子: $a > 15$ を含む
- **閾値: $a \approx 15$** が「生命の signature」

これは情報理論的に深い意味を持つ: 高 AI は**情報のリピートと再利用** ―
つまり**コーディング** ― を示唆する。

## 3. ITU との対応

### 3.1 AI ⟷ QECC depth

ITU では QECC コード $[[n, k, d]]$ の depth $d$ が code の**訂正能力**を測る:
- $d$ stabilizers が commute する → 状態を保護
- 大きい $d$ → 多くの誤りを訂正できる強い code

Assembly Index も同様の構造を持つ:
- 高 AI → 多くの "再利用される building block" を含む
- 偶然には作れない情報パターン
- 自己複製と選択を通じて初めて維持される

**主張: AI ≈ QECC depth, with the same information-theoretic role.**

### 3.2 ITU 公理の AT 翻訳

物理層 (Phase 1-32):
$$\delta S(\rho_A) = \delta \mathrm{Tr}[K_A^{(0)} \rho_A]$$

生命層 (Phase 33-40):
$$\delta \log A(\mathcal{O}) = \delta \log[e^{a(\mathcal{O})} N(\mathcal{O})] = \delta a + \delta \log N$$

ここで $a$ は AI (構造的情報), $N$ はコピー数 (個体数)。

**生命方程式**: 進化過程で
$$\delta a > 0 \quad \text{かつ} \quad \delta \log N \geq 0$$

つまり「**構造を保ちつつ増殖する**」ものが生命。これは Phase 28 の misalignment
機構 ($\rho \propto a^{-3}$ の凍結) を生物学的に翻訳したもの:

| 物理層 (Phase 28) | 生命層 (Phase 34) |
|---|---|
| Cold DM 場 $\phi$ が振動 | 分子が複製 |
| $\rho_\phi \propto a^{-3}$ で凍結 | 高 AI の分子が再利用される |
| QECC スタビライザ凍結 | Assembly memory として保存 |

### 3.3 生命の閾値の ITU 解釈

なぜ $a = 15$ が閾値か?

ITU からの予想:
- ランダム化学プロセスのエントロピー生成率 $\sim k_B \ln(\text{反応数})$
- 偶然に AI = 15 の分子が現れる確率 $\sim e^{-15} \approx 3 \times 10^{-7}$
- 観測量 (galaxy 全体の化学量 $\sim N_{\rm A} \times 10^{50}$ kg)で
  なお significant に存在するには $a \leq 15$ 程度が限界

→ **$a > 15$ なら "情報の memory" がない過程では物理的に説明不能**

これが Walker-Cronin の「**生命のシグナル**」 ― ITU 流に解釈すれば「**コーディング (QECC) が存在しないと作れない情報量**」。

## 4. 数値検証

### Part A: 文字列 AI の計算
- ランダム文字列 vs 反復構造を持つ文字列
- AI 分布を比較

### Part B: 自己触媒選択下の AI 進化
- Phase 33 の autocatalytic set 出力をシミュレート
- "複製してマッチする" 文字列が選ばれる過程で AI が増えるか確認

### Part C: AI 閾値 (~15) の数値再現
- ランダム化学 vs 選択化学
- $a_{\rm max}^{\rm random}$ と $a_{\rm max}^{\rm select}$ の比較

### Part D: QECC depth 対応
- 各文字列に対応する単純 stabilizer code を構築
- AI と code distance の相関

## 5. 限界

⚠️ 本 Phase で扱わない:
- 完全な 3D 分子構造 (mass spec 適用は将来 phase)
- 量子化学 (結合エネルギー考慮なし)
- 立体異性体 (chirality は Phase 38 で)
- 完全な進化動力学 (selection coefficient なし)

✅ 確立する:
- AI と QECC depth が情報理論的に同じ役割
- 自己触媒過程が高 AI 分子を選別する
- 「生命の閾値 $a \sim 15$」 は ITU から自然に出る

## 6. Phase 35 への橋渡し

Phase 35 では **RNA world** に進む:
- リボザイム (catalytic RNA) は AI ≈ 20-30
- 自己複製能力を持つ → AT/ITU の予言と整合
- "情報を持つ触媒" の最小単位

その後 Phase 36 (Free Energy Principle), 37 (lipid bilayer), 38 (chirality),
39 (first cell), 40 (synthesis) と進む予定。

---

**核心メッセージ**:
> Assembly Theory の「**生命を測る量 AI**」は、ITU の「**情報を保護する量 QECC depth**」と
> 同じものを別の角度から測っている。両者は単一公理 $\delta S = \delta \langle K \rangle$
> のもとで自然に統合できる。
