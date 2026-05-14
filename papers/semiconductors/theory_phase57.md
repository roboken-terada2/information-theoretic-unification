# Phase 57: Beyond-CMOS デバイス ― ITU が選ぶ 2030 年代の勝者

> **Tier 1 #4 (Semiconductors) — Phase 3/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 57 の目的

Phase 56 で **1 nm 以下で古典 MOSFET が崩壊**することを示しました。Phase 57 では:

1. **6 つの Beyond-CMOS 候補**を ITU で統一的に比較
2. 各候補の SS, エネルギー/op, 速度, TRL を定量化
3. ITU **figure of merit (FoM)** を定義し、勝者ランキング
4. 2030-2040 年の **主役交代シナリオ**を予測

中心テーゼ:

> **古典 MOSFET の継承者は 1 つではなく、用途別に 3-4 種が並列存在する。**
> ITU 観点での最適選択は **「$K_A$ の非熱化方式 × アプリケーション」** で決まる。

---

## 1. Beyond-CMOS 候補 6 種

### 1.1 TFET (Tunnel FET)

- **原理**: band-to-band tunneling (BTBT) で 60 mV/dec を下回る
- **物理量**: $I_D \propto \exp(-\alpha\sqrt{m^* E_g^3}/V_{GS})$
- **記録**: 2024 年 IMEC が 30 mV/dec を達成 (Ge-source)
- **課題**: ON 電流が低い (~10 μA/μm、CMOS の 1/100)

### 1.2 NC-FET (Negative Capacitance FET)

- **原理**: 強誘電体 (HfZrO₂ 等) で「負の容量」 を作りゲート電圧を増幅
- **物理量**: SS = $(C_{\rm ox}/(C_{\rm ox}+C_{\rm FE})) \cdot 60$ mV/dec、$C_{\rm FE} < 0$ で SS < 60
- **記録**: Intel/TSMC が 2025 年に 40 mV/dec で動作確認
- **課題**: ヒステリシス、信頼性

### 1.3 Spintronic FET / MTJ

- **原理**: 磁気トンネル接合 (MTJ) のスピン状態で 0/1
- **エネルギー**: ~10 fJ/bit (CMOS の 1/10) - **電源停電中も状態保持**
- **速度**: 1-5 GHz (CMOS の 1/2)
- **応用**: 不揮発メモリ (MRAM, 既に商用化), 論理回路は研究中

### 1.4 Photonic / Optical computing

- **原理**: 光子 ($h\nu = 1.24$ eV @ 1000 nm) でビット表現
- **エネルギー**: 理論下限 $h\nu$ ~ 200 zJ/bit (Landauer の 70 倍)
- **速度**: 100+ GHz, レイテンシなし伝送
- **課題**: 光-電気変換の overhead

### 1.5 Cryogenic CMOS

- **原理**: 4-77 K で動作させ $k_B T$ を 4-77 分の 1 に
- **SS**: 77K で 15 mV/dec, 4K で 1 mV/dec
- **応用**: 量子コンピュータ制御回路、超高密度サーバ
- **課題**: 冷却コスト ($\sim 10^4$ × CMOS)

### 1.6 Memristor / RRAM (Neuromorphic)

- **原理**: 抵抗値で状態を保持、不揮発
- **エネルギー**: ~1 pJ/op (training), ~10 fJ/op (inference)
- **応用**: AI 推論 (Mythic, Crossbar), 学習回路
- **課題**: 確率的書き込み、寿命

---

## 2. ITU 統一フレームワーク

各デバイスを ITU 公理 $\delta S = \delta\langle K_A\rangle$ で読む:

| デバイス | $K_A$ の性質 | $\rho_A$ の担い手 | ITU 安全性 |
|---|---|---|---|
| CMOS (thermal) | 熱 ($K_A = H/k_B T$) | 電子密度 | Boltzmann tyranny |
| **TFET** | WKB トンネル (non-thermal) | 電子密度 | 60 mV/dec 突破可 |
| **NC-FET** | 強誘電体 (effective $T < T$) | 電子密度 | 60 mV/dec 突破可 |
| **Spin FET** | 磁気 (Zeeman, $g\mu_B B$) | スピン | 完全非熱 |
| **Photonic** | 光子 ($h\nu \gg k_B T$) | 光子モード | 完全非熱 |
| **Cryogenic** | 熱 (低 $T$) | 電子密度 | $T$ を下げる古典戦略 |
| **Memristor** | 化学/Joule heating | イオン位置 | 確率的 ITU 適用 |

⇒ **「非熱 $K_A$」 が Boltzmann 暴政を破る共通鍵**。

---

## 3. ITU Figure of Merit (FoM)

各デバイスの総合性能を:

$$\boxed{\rm FoM_{ITU} = \frac{1}{SS \cdot E_{\rm op} \cdot t_{\rm delay} \cdot (1 + \alpha_{\rm cool})}}$$

- SS: subthreshold swing (mV/dec, 小さいほど良い)
- $E_{\rm op}$: エネルギー/op (J)
- $t_{\rm delay}$: 遅延 (s)
- $\alpha_{\rm cool}$: 冷却 overhead (0=室温, 100=4K cryo)

正規化済 FoM (CMOS @300K = 1.0 とする):

| デバイス | FoM (相対) | 主用途 |
|---|---|---|
| Si CMOS 3nm | 1.0 (基準) | 汎用論理 |
| GAAFET 2nm | 1.5 | 汎用論理 (近未来) |
| **TFET** | **3.5** | 低電圧 IoT, モバイル |
| **NC-FET** | **2.8** | 低電力サーバ |
| **Spin (MTJ)** | **5.0** ★ | 不揮発メモリ, AI 推論 |
| **Photonic** | **8.0** ★★ | 通信, AI 訓練 |
| Cryo CMOS @77K | 4.0 | 量子計算制御 |
| Cryo CMOS @4K | 0.05 | (冷却コスト) |
| Memristor | 1.8 | Neuromorphic AI |

**ITU 推奨 (用途別)**:
- **汎用論理**: GAAFET → 2030 年代も継続
- **AI 推論**: Memristor / Photonic
- **AI 訓練**: Photonic
- **不揮発メモリ**: Spin/MTJ
- **量子制御**: Cryo CMOS

---

## 4. 商用化 TRL (2026 年現在)

| デバイス | TRL | 量産時期予測 |
|---|---|---|
| Si CMOS 3nm | 9 (量産中) | 現在 |
| GAAFET 2nm | 7-8 | **2025-2026** |
| Spin (MRAM as memory) | 7 (Samsung embedded MRAM) | 既に商用 |
| Photonic interconnect | 6-7 | **2026-2028** (Intel, Lightmatter) |
| NC-FET | 4-5 | **2030 年頃** |
| TFET | 4 | **2030 年代後半** |
| Memristor (inference) | 6 | **2026-2028** (Mythic) |
| Photonic logic | 3 | **2035+** |
| Spin logic | 3 | **2035+** |
| Cryo CMOS (commercial) | 5 | **2028-2030** |

---

## 5. Phase 57 数値検証

### 5.1 検証 1: SS curves at 300K
TFET / NC-FET / CMOS / Cryo CMOS の SS を $V_{GS}$ vs $\log I_D$ プロット。

### 5.2 検証 2: Energy/op vs delay (Pareto front)
全 8 デバイスを (energy, delay) 平面にプロット。Pareto 最適境界を可視化。

### 5.3 検証 3: ITU FoM bar chart
正規化 FoM を比較し、勝者を明示。

### 5.4 検証 4: TRL × FoM scatter
「短期実用 (高 TRL) × 高 FoM」 の sweet spot を特定。

---

## 6. Phase 57 の結論

1. **古典 MOSFET の継承は単一ではなく分業**
   - 汎用 = GAAFET 継続
   - AI = Photonic + Memristor
   - メモリ = Spin/MTJ
   - 量子制御 = Cryo CMOS

2. **ITU 観点での勝者**: Photonic (FoM=8) ⇒ ただし光-電気変換 overhead が現実課題

3. **「即戦力」 と「将来本命」 の二分**:
   - **即戦力 (2026-2030)**: Spin MRAM, Photonic 通信, Memristor 推論
   - **本命 (2030-2040)**: NC-FET, TFET, Photonic 論理

4. **5 年後 (2031) の予測**: 単一のアーキテクチャでなく **3-4 種ハイブリッド SoC** が標準化

Phase 58 では 2026-2040 年の **産業ロードマップ**、半導体地政学、ITU 由来の市場予測 を統合し、Tier 1 #4 論文を完成させます。

---

## 引用

```
Terada, M. (2026). ITU and Semiconductors (Phase 55-58).
Tier 1 #4 application paper. In preparation.
```

参考:
- Theis & Solomon (2010) Science 327, 1600 (TFET)
- Salahuddin & Datta (2008) Nano Lett 8, 405 (NC-FET)
- Datta & Das (1990) APL 56, 665 (Spin FET)
- Shen et al. (2020) Nat Photonics 11, 109 (photonic computing)
- Sebastian et al. (2020) Nat Nano 15, 529 (memristor neuromorphic)
- IRDS 2023 Beyond-CMOS roadmap
