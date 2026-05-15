# Phase 79: エネルギー・材料の ITU 基礎 ― 情報がエネルギーである時代

> **Tier 1 #10 (Energy/Materials) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> Tier 1 #4 (Semiconductors): [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 79 の目的

ITU 工学軸拡張、Tier 1 #4 (半導体) を超えてエネルギーと材料一般へ:

1. **エネルギー** = ITU の $K$ が物理スケールで行う仕事
2. **材料** = $K_{\rm structure}$ が原子レベルで自己組織化した結果
3. **情報-エネルギー等価性**: Maxwell's demon, Landauer 1961 (Tier 1 #4 で触れた)
4. **再生可能エネルギー** の ITU 解釈
5. **電池技術** とエネルギー保存
6. **臨界材料** (リチウム, レアアース) と地政学
7. Phase 80-82 への基盤

中心テーゼ:

> **エネルギーと情報は同一物**: $E = k_B T \ln 2$ per bit (Landauer)。
> 21 世紀の電池革命 = $K_{\rm energy}$ 密度の指数的増加。
> 材料科学 = $K_{\rm structure}$ の原子精密制御。

---

## 1. ITU 視点でのエネルギーと情報

### 1.1 Landauer 1961 (再掲)

1 bit 消去に最低 $E_{\rm min} = k_B T \ln 2$ のエネルギー:
- T = 300K: 2.87 × 10⁻²¹ J/bit ≈ 17.9 meV
- T = 77K (cryo): 4.6 meV
- T = 4K (希釈冷凍): 0.24 meV

ITU 公理: $\delta S = \delta\langle K\rangle$ ⇒ 情報の reorganization は K-work を要求。

### 1.2 Maxwell's demon (1867) と ITU

Maxwell の悪魔: 分子をふるい分け、エントロピーを減らす (一見、第二法則違反)。

解決 (Bennett 1982): **悪魔も情報処理時にエネルギーを消費**:
- 分子の状態を測定 (記憶) ⇒ 情報蓄積
- 記憶を消去 (Landauer) ⇒ k_B T ln 2 per bit のエネルギー消費

⇒ **第二法則は救われ、情報-エネルギー等価が確立**。

ITU 翻訳: 悪魔 = K_demon が S を一時的に下げるが、最終的に $\delta\langle K\rangle$ を要求 ⇒ 公理が常に維持。

### 1.3 21 世紀の情報革命

| 年 | 計算機 1 op エネルギー |
|---|---|
| 1950 (vacuum tube) | 10⁻³ J |
| 1980 | 10⁻⁸ J |
| 2000 | 10⁻¹⁴ J |
| 2024 (GAAFET 3nm) | 10⁻¹⁷ J |
| **Landauer 極限 (300K)** | **2.87 × 10⁻²¹ J** |

⇒ 計算機は **Landauer の 10⁴ 倍** で動作中、まだ ~4 桁の改善余地 (Tier 1 #4 Phase 55-58)。

---

## 2. エネルギー貯蔵技術 ― $K_{\rm energy}$ density 競争

### 2.1 主要技術比較

| 技術 | エネルギー密度 (Wh/kg) | コスト ($/kWh) | 寿命 (cycles) | 商用化 |
|---|---|---|---|---|
| 鉛電池 | 30 | 100 | 500 | 1860+ |
| Ni-Cd | 50 | 800 | 2,000 | 1900+ |
| Ni-MH | 90 | 600 | 1,000 | 1990s |
| **Li-ion (NMC/NCA)** | **250** | **140** | 1,500 | **2008+** |
| Li-ion (LFP) | 200 | 100 | 3,000 | 2010+ |
| **Solid-state (predicted)** | **400-500** | **80** | **>5,000** | **2027-30 予測** |
| **Li-air (theoretical)** | **3500** | TBD | TBD | 2035+ |
| **Hydrogen fuel cell** | 33,000 (H₂) | $5/kg | n/a | 2010+ |
| ガソリン (参考) | 12,200 | ~ | n/a | 1900+ |

### 2.2 ITU 解釈

電池進化 = **$K_{\rm energy\_storage}$ density の指数的増加**:
- 1970 鉛: 30 Wh/kg
- 2008 NMC: 250 Wh/kg ⇒ **8x 改善** in 38 年
- 2030 solid-state 予測: 500 Wh/kg
- 2050 Li-air 実用化?: 1500 Wh/kg

「Wright の法則」: 累積生産量倍増ごとに **コスト 20-25% 低下**。
Li-ion は 1991 年 $7,500/kWh → 2024 年 $140/kWh ⇒ **53x 削減** in 33 年。

### 2.3 グリッドスケール

| 技術 | 用途 | 課題 |
|---|---|---|
| Li-ion (Tesla Megapack) | 1-4 時間 peak shaving | 火災リスク, 資源 |
| Flow batteries (V, Zn-Br) | 4-12 時間 | 容量低い、コスト |
| Pumped hydro | 8-24 時間 | 立地制限 |
| Compressed air | 12-48 時間 | 効率 50-70% |
| **Iron-air (Form Energy)** | **100 時間** | 商用化中 |
| 水素 + 燃料電池 | 季節貯蔵 | 効率 30% |

---

## 3. 太陽光と Shockley-Queisser 限界

### 3.1 単接合シリコン太陽電池

Shockley-Queisser (1961): 単接合 (E_g = 1.1 eV) の理論最大効率 = **33.7%**。

| 世代 | 効率 (2024 ベスト) |
|---|---|
| 第 1: c-Si | 26.8% (LONGi, 2023) |
| 第 2: thin-film (CIGS, CdTe) | 23% |
| 第 3: tandem (Si+perovskite) | **33.9%** (LONGi/Trina 2024) |
| 第 3: triple-junction | **47.6%** (集光) |
| 第 4: quantum dot | 18% (実験) |

### 3.2 ITU 視点

太陽電池 = **太陽の $K_{\rm photon}$ を電子の $K_{\rm electron}$ に変換するエンジン**:
- 効率 = $\delta\langle K_{\rm electron}\rangle / \delta\langle K_{\rm photon}\rangle$
- Shockley-Queisser = 単接合での ITU 最大変換率
- Multi-junction でこの限界を破る (異なる E_g で異なるスペクトル領域を捕捉)

### 3.3 価格動向 (Swanson's Law)

太陽電池モジュール価格:
- 1975: $100/W
- 2010: $1.5/W
- 2024: **$0.10/W** ⇒ **1000x 削減**
- 2030 (予測): $0.05/W

⇒ 太陽光が地球上で最も**安価なエネルギー源**となった (2024 IEA 報告)。

---

## 4. 臨界材料 (Critical Materials) と地政学

### 4.1 重要 17 元素 (米国 DOE)

| 元素 | 用途 | 主要供給国 | 集中度 |
|---|---|---|---|
| **リチウム** | EV 電池 | チリ (35%), オーストラリア (50%) | 中 |
| **コバルト** | NMC 電池 | コンゴ (60%) | **高 ⚠️** |
| **ニッケル** | NMC 電池 | インドネシア (40%) | 中 |
| **レアアース 17 種** | 永久磁石, 光学 | 中国 (60-90%) | **超高 ⚠️⚠️** |
| **ガリウム** | パワー半導体 | 中国 (98%) | **超高** |
| **ゲルマニウム** | 光ファイバ, IR | 中国 (60%) | 高 |
| **シリコン** (高純度) | 半導体, 太陽電池 | 中国 (80%) | 高 |
| **グラファイト** | Li 負極 | 中国 (70%) | 高 |
| **ウラン** | 原発 | カザフスタン (40%), カナダ (20%) | 中 |

### 4.2 中国の優位

- レアアース: 中国が採掘 + 精製を独占
- ガリウム・ゲルマニウム: 2023 年中国が輸出規制
- ⇒ **西側諸国の供給リスク**: 米 CHIPS Act, EU CRMA (Critical Raw Materials Act)

### 4.3 ITU 視点

材料の集中 = **K_resource の地理的偏在** ⇒ 経済 + 軍事に直結 (Tier 1 #8 と整合)。
代替材料 + 都市鉱山 + リサイクルが 21 世紀の戦略的課題。

---

## 5. 材料設計の新時代 ― AI × 量子計算

### 5.1 従来の限界

新材料開発:
- 平均 10-20 年, $10-100M コスト
- 100,000 候補のうち 1 つ商用化 (Edisonian アプローチ)

### 5.2 AI 駆動材料発見

| 手法 | ブレイクスルー |
|---|---|
| **DFT (密度汎関数法)** | 1960s-, 計算 1 分子/日 |
| **Materials Project** (MIT) | 2010s-, 150,000+ 材料の DB |
| **DeepMind GNoME** (2023) | 220 万の新結晶を予測 (Nature) |
| **Microsoft MatterGen** (2024) | 生成モデルで新材料設計 |
| **Tier 1 #1 量子計算** | DFT 完全代替 (2030+ 予測) |

### 5.3 ITU 視点

材料設計 = K_structure の状態空間探索:
- 古典: 莫大な K-state space を Edisonian に探索
- AI: 既知 K-structure の latent space から外挿
- **量子計算 (#1)**: K-electron correlation を直接シミュレート
- ⇒ 「**設計 → 合成 → 試験**」 サイクルが 10 年 → 1 年に短縮 (2030 予測)

---

## 6. Phase 79 数値検証

### 6.1 検証 1: Landauer 極限 vs 現代計算機

### 6.2 検証 2: 電池技術 cost-density Pareto

### 6.3 検証 3: 太陽電池効率推移 (Shockley-Queisser 限界)

### 6.4 検証 4: 臨界材料 供給集中度 (Herfindahl-Hirschman index)

---

## 7. Phase 79 の結論

1. **エネルギー = K-work**, 情報 = K-bit, 両者は Landauer 関係で等価
2. **Li-ion 進化**: 30 Wh/kg (鉛) → 250 (NMC) → 500 (solid-state 2030)
3. **太陽電池**: $0.10/W = 史上最安エネルギー、tandem で 34% 効率
4. **臨界材料**: 中国のレアアース 60-90% シェア ⇒ 地政学リスク
5. **AI × 量子計算**: 材料発見サイクル 10x 加速予測

Phase 80 では **再生可能エネルギー** ― 太陽 + 風力 + 水力 + 原子力 + 核融合の ITU 統合解析。

---

## 引用

```
Terada, M. (2026). ITU and Energy / Materials (Phase 79-82).
Tier 1 #10 application paper. In preparation.
```

参考:
- Landauer (1961) IBM J Res Dev 5, 183
- Bennett (1982) Int J Theor Phys 21, 905 (Maxwell demon resolution)
- Shockley & Queisser (1961) J Appl Phys 32, 510
- IEA (2024) World Energy Outlook
- US DOE (2023) Critical Materials Assessment
- Merchant et al. (2023) Nature 624, 80 (GNoME 220万結晶)
- BNEF (2024) Battery Price Survey
- Wright (1936) J Aeronaut Sci 3, 122 (Wright's Law)
- Swanson (2006) IEEE Electron Device Lett 27, 1
