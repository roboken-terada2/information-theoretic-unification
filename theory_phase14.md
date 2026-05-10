# Phase 14: 動的時空の厳密版 — Witten 2022 の type II 代数と crossed product

## 1. 動機と背景

Phase 4 でモジュラーフロー $\sigma_t^\omega$ が状態 $\omega$ 依存的時間として機能することを示した。
しかし数学的に厳密な意味で、量子重力の代数的構造はもう一段深い:

**問題**：場の量子論で、空間領域 $A$ の局所代数 $\mathcal{A}(A)$ は **Type III_1 von Neumann 代数** (Buchholz-Wichmann 1986)。これは:
- 密度行列を持たない (= $\rho_A$ が定義できない)
- エントロピーが本質的に発散 ("$\infty - \infty$")
- pure state や trace state を持たない

これでは「重力理論におけるエントロピー」が定義できない。

**Witten の解答 (2022)**：
> 観測者の時計を加えて **crossed product** を取ると、Type III_1 → Type II に変換される。Type II は密度行列を持ち、エントロピーが**有限になる**。

これが「重力理論におけるエントロピーとは何か」への厳密な解答。

## 2. von Neumann 代数の分類 (Murray-von Neumann 1936)

### 2.1 Type I
標準的な量子力学。テンソル積に分解可能。trace 存在。
- Type I_n: 有限次元 ($n$ qubit など)
- Type I_∞: 無限次元、可分

### 2.2 Type II
trace 存在するが pure state に分解できない。
- **Type II_1**: 有限 trace (closed system with **finite** entropy)
- **Type II_∞**: 無限 trace

### 2.3 Type III
trace なし、pure state なし。
- **Type III_λ** ($0 < λ < 1$): 「modular spectrum」が λ だけ離散
- **Type III_1**: 連続 modular spectrum (これが QFT 局所代数!)
- Type III_0: 病理的、QFT には現れない

**重要事実**：QFT の任意の有界開領域 $\mathcal{O}$ の局所代数 $\mathcal{A}(\mathcal{O})$ は **Type III_1** (Driessler-Buchholz-Wichmann)。

## 3. Tomita-Takesaki 理論 (再訪)

任意の von Neumann 代数 $\mathcal{M}$ + 状態 $\omega$ から、**modular automorphism** $\sigma_t^\omega$ が一意に定義される (Phase 4)。
$$\sigma_t^\omega: \mathcal{M} \to \mathcal{M}, \quad t \in \mathbb{R}$$

これは Type に依存せず存在する。Type III_1 の場合、$\sigma_t$ は**外部自己準同型** (= 内部対応する Hamiltonian がない) となり、ここに crossed product を構成する余地が生まれる。

## 4. Crossed Product の定義

### 4.1 一般的定義

von Neumann 代数 $\mathcal{M}$ と作用 $\alpha: G \to \mathrm{Aut}(\mathcal{M})$ ($G$ は群) に対し、crossed product
$$\mathcal{M} \rtimes_\alpha G$$
は次のように構成される:
- 新しいヒルベルト空間 $\hat{\mathcal{H}} = \mathcal{H} \otimes L^2(G)$
- 新しい代数生成子: $\pi(a)$ ($a \in \mathcal{M}$) と $u(g)$ ($g \in G$) の関係:
  $$u(g) \pi(a) u(g)^{-1} = \pi(\alpha_g(a))$$

### 4.2 modular flow との crossed product

$G = \mathbb{R}$, $\alpha = \sigma^\omega$ (modular flow) のとき:
$$\hat{\mathcal{M}} = \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$$

これは「時計を持つ観測者の代数」として解釈される:
- $\pi(a)$: 観測対象 $a \in \mathcal{M}$
- $u(t)$: 観測者の時間並進
- 関係式: 時計の動きが $a$ をモジュラーフローで進める

**Connes の定理 (1973)**：
$$\mathcal{M} \text{ が Type III}_1 \;\Longrightarrow\; \mathcal{M} \rtimes_{\sigma} \mathbb{R} \text{ が Type II}_\infty$$

つまり**crossed product は型を III から II へ変換する**。

### 4.3 重力との繋がり (Chandrasekaran-Penington-Witten 2022)

重力の semiclassical 描像で、観測者の Hamiltonian $H_{\rm obs}$ が $\sigma_t^\omega$ を生成する modular Hamiltonian と同一視できる。
すると重力理論における観測者を含む代数は自動的に
$$\mathcal{A}(\mathcal{O}) \rtimes \mathbb{R}_{\rm time}$$
となり、Type II となる。これにより**密度行列とエントロピーが定義可能に**なる。

## 5. de Sitter との関係 (Phase 13 とのリンク)

de Sitter 観測者の半分宇宙領域代数は:
- 厳密には Type III_1 (gravity を入れない時の QFT)
- 観測者の時計を含めると Type II_1 (有限 trace!)

**Type II_1 の重要性**：
- Trace state $\tau$ が存在 → 「最大混合状態」が定義できる
- エントロピー $S(\rho) = -\tau(\rho \log \rho)$ が**有限値**
- $S$ は最大値 $\log(\dim) = $ Bekenstein-Hawking エントロピー $S_{\rm dS} = 3\pi/(G_N \Lambda)$ で抑えられる

これが Phase 13 で示した「**Λ が小さい = エントロピー容量が大きい**」の数学的厳密化。

## 6. 数値的に示せること

完全な Type III_1 → II 変換は無限次元代数の話だが、有限格子上で**Type III-like UV 発散**と**Type II-like 有限性**の signature を見ることができる:

### Demo A: UV 発散 (Type III の signature)
1+1D CFT 領域 $A$ のエンタングルメントエントロピー:
$$S(A) = \frac{c}{3}\log\frac{L_A}{a} + \mathrm{const}$$
$a \to 0$ (= 格子間隔ゼロ、連続極限) で発散。

数値検証：固定 $L_A/L = $ const で $N$ を増やすと $S \sim (c/3) \log N$ 発散。

### Demo B: 相対エントロピーの UV 有限性 (Type II safe)
Casini 正値性 (Phase 2):
$$S_{\rm rel}(\rho || \sigma) = \delta\langle K_\sigma\rangle - \delta S \geq 0$$
$S_{\rm rel}$ は Type に依らず**任意の Type で有限**。物理的・観測者独立な Type II 観測量。

数値検証：固定 $L_A/L$ で、$S_{\rm rel}(\rho_{\rm thermal} || \rho_{\rm vacuum})$ が $N \to \infty$ で有限値に収束。

### Demo C: 観測者時計による正則化
観測者を有限次元 Hilbert ($D_{\rm obs}$) として加える。エントロピー $\leq \log D_{\rm obs}$ で抑えられる。

これは crossed product の結果として「Type III 発散が観測者 Hilbert で抑えられる」ことの最小モデル。

### Demo D: Type II 1 結合エントロピー
"system + observer" の合成系のエントロピーは
$$S_{\rm total} = S_{\rm sys + obs} \leq \min(S_{\rm sys, naive}, \log D_{\rm obs})$$

これは Type II_1 の有限性を直接実装。

## 7. 情報理論的統一理論内の位置づけ

Phase 1-13 で時空・重力・物質・対称性破れ・宇宙論的進化・Λ を量子情報構造から導いた。
Phase 14 はこの全体構造に**数学的厳密性の最終仕上げ**を与える:

> 重力理論におけるエントロピーは Type III_1 で本質的に発散だが、**観測者** (= modular flow の crossed product) を加えることで Type II_1 になり**有限化される**。これが量子重力エントロピーの数学的に厳密な定義。

これにより:
- Phase 4: 時間 = モジュラーフロー
- Phase 13: Λ = 1/(エントロピー容量)
- Phase 14: 観測者依存性 = type 変換 (III → II)

の三位一体が完成。

## 8. 限界と今後

✅ 示せる (本 Phase):
- Type III の発散 signature (UV dependent S)
- Type II の有限 signature (UV-finite relative entropy)
- 観測者による正則化の最小モデル

⚠️ 示せない (未解決):
- 完全 Type III_1 構造 (無限次元代数)
- 動的観測者との完全 crossed product
- 観測者の主観的経験との関係 (= 量子測定の解釈問題)

これらは現代物理学・哲学の最先端で進行中。
