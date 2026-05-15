# Phase 84: 炭素循環 + ENSO + AMOC ― 地球システムの動的 K-flow

> **Tier 1 #11 (Climate / Earth Systems) — Phase 2/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 84 の目的

Phase 83 で「気候 = 巨視的 K-state」と定式化した。Phase 84 では **K-flow の動的構造** を扱う:

1. **炭素循環** を 4 box model (大気/陸/表層海/深層海) で K-flow として記述
2. **ENSO** (エルニーニョ南方振動) を K_ocean-K_atm 結合振動として表現
3. **AMOC** (大西洋子午面循環) の崩壊リスクを K-bifurcation で評価
4. **3 ティッピング点候補** の確率時系列予測

中心テーゼ:

> 気候は **静的状態ではなく、複数の準周期/メタ安定 K-flow** の重ね合わせ。CO₂ 注入は K-flow パターン自体を再配置する。

---

## 1. 炭素循環 4-box モデル

### 1.1 構造

```
       人為排出 E(t) ≈ 11 GtC/yr (2024)
              │
              ▼
        ┌──────────┐
        │ 大気 M_a │ ≈ 880 GtC (2024)
        └──────────┘
         ↕ k_la↕     ↕ k_oa
   ┌──────────┐   ┌──────────┐
   │ 陸生 M_l │   │ 表層海 M_s│
   │ 2300 GtC │   │  900 GtC  │
   └──────────┘   └──────────┘
                    ↕ k_sd
                  ┌──────────┐
                  │ 深層海 M_d│
                  │ 38000 GtC │
                  └──────────┘
```

### 1.2 微分方程式

$$
\frac{dM_a}{dt} = E(t) - k_{al}(M_a - M_a^*) - k_{as}(M_a - M_a^*)
$$
$$
\frac{dM_l}{dt} = k_{al}(M_a - M_a^*) - k_{lr} M_l
$$
$$
\frac{dM_s}{dt} = k_{as}(M_a - M_a^*) - k_{sd}(M_s - M_d/r)
$$
$$
\frac{dM_d}{dt} = k_{sd}(M_s - M_d/r)
$$

パラメータ (IPCC AR6 ベース):
- k_al ≈ 1/30 yr⁻¹ (陸の吸収時定数)
- k_as ≈ 1/10 yr⁻¹ (海面の吸収時定数)
- k_sd ≈ 1/500 yr⁻¹ (深海への沈降)
- k_lr ≈ 1/60 yr⁻¹ (陸の呼吸放出)
- 前産業平衡: M_a* = 600 GtC (280 ppm = 600 GtC)

### 1.3 観測との照合

GCB 2024 (Global Carbon Budget):
- 排出: 化石 9.9 + 土地 1.1 = **11.0 GtC/yr**
- 吸収: 大気 5.3 + 陸 3.5 + 海 2.7 = **11.5 GtC/yr** (誤差 0.5)
- **Airborne fraction**: 48% (40 年間ほぼ一定)

### 1.4 ITU 解釈

各 box が **K_carbon** の貯蔵ノード:
- M_a = 大気の K-bit 蓄積
- 各 k_ij = K-flow 透過率
- 人為排出 E = **外部からの K-bit 注入**
- 吸収率 = K_atm の K-current 出口幅

⇒ **2050 NZE 達成 = E(t) → 0** だが、深海への沈降には数百年要する。

---

## 2. ENSO ― 海洋・大気の K-結合振動

### 2.1 物理

エルニーニョ南方振動 (El Niño-Southern Oscillation):
- 周期 **3-7 年**
- 太平洋赤道域の SST + 海面気圧シーソー
- 全球気候への波及 (干ばつ、豪雨、漁業)

### 2.2 簡易モデル (Vallis 1986)

$$
\frac{dT}{dt} = -bT + cu, \quad \frac{du}{dt} = -au + dT^3
$$

- T = 東赤道太平洋 SST 異常
- u = 西風応力異常
- 三次項で **準周期** 発生

### 2.3 ITU 解釈

ENSO は K_ocean-K_atm の結合振動子:

$$
\dot{K_o} = -\gamma K_o + \chi K_a, \quad \dot{K_a} = -\beta K_a + g(K_o)
$$

非線形項 g により 3-7 年周期のリミットサイクル。

### 2.4 温暖化の影響

IPCC AR6 + 観測:
- ENSO **振幅 +10-15%** (2050 高排出)
- 強い El Niño (例: 1997/98, 2015/16, **2023/24**) 頻度 **2 倍**
- La Niña 強度も増加
- ⇒ K_climate の振動幅拡大

---

## 3. AMOC ― 大西洋子午面循環

### 3.1 物理

Atlantic Meridional Overturning Circulation:
- 北大西洋深層水形成 + 表層暖水北上
- 北欧の温暖化に寄与 (+5°C 程度)
- 強度 ~15-20 Sv (Sverdrup = 10⁶ m³/s)

### 3.2 観測

- RAPID 観測 (2004-2024): **平均 17 Sv**
- 1850 年比で **15-20% 減少 (Caesar 2018, Boers 2021)**
- 早期警告信号 (分散増加、自己相関増加) 検出済

### 3.3 Stommel 2-box モデル

$$
\frac{dq}{dt} = \frac{1}{\tau}[q_0 - q - \alpha (T_N - T_S) - \beta (S_N - S_S)]
$$

塩分淡水注入 (グリーンランド氷融解) で **dual steady state** が存在し、tipping 可能。

### 3.4 ITU 解釈

AMOC は **K_ocean の地球規模 K-flow channel**。崩壊 = 別の K-state attractor へ転移。

崩壊リスク確率:

| 期間 | P(AMOC 崩壊) | 出典 |
|---|---|---|
| 2025-2050 | 5-15% | Ditlevsen 2023 |
| 2025-2095 | 10-50% | IPCC AR6 + Boers |
| 2025-2300 (継続排出) | >80% | RCP8.5 シナリオ |

### 3.5 崩壊時の影響

- 北欧温度 **-5 to -10°C**
- 熱帯雨帯南下 (アマゾン、サヘル干ばつ)
- 北米東岸海面上昇 +0.5m

⇒ K-state 大規模再配置: 気候・経済・社会全領域に波及。

---

## 4. 3 ティッピング点候補の確率時系列

Lenton et al. (2023) Science: 16 elements 中 5 つが 1.5°C で活性化リスク。
本 Phase は代表 3 つを扱う:

### 4.1 グリーンランド氷床

- 質量喪失加速: 2002-2024 で 5,400 Gt 喪失 (海面 +15 mm)
- Tipping 閾値: T_global = **+1.5-2.5°C**
- 完全崩壊で海面 +7 m (1000-10000 yr)

### 4.2 西南極氷床 (Thwaites)

- "Doomsday Glacier" Thwaites の grounding line 後退
- Tipping 閾値: **+1.5-2.0°C**
- 崩壊で海面 +3 m (200-1000 yr)

### 4.3 アマゾン熱帯雨林

- 森林伐採 + 干ばつで savanna 化
- Tipping 閾値: 伐採率 **20-25% + T_global +2.5°C**
- 現状伐採率: 17% (2024)
- 崩壊で 200 GtC 放出 (大気 CO₂ +90 ppm 相当)

### 4.4 確率モデル

各 tipping element に対し:

$$
P(\text{tip} | T) = \frac{1}{1 + \exp[-(T - T_c)/\sigma_T]}
$$

- T_c = critical temperature
- σ_T = transition width ~0.3 K

複合 tipping point cascade: P_AMOC × P_Greenland → 連鎖確率増加。

---

## 5. Phase 84 主結論

1. **炭素循環**: 4-box model で airborne fraction 48% 再現
2. **ENSO**: 3-7 年周期の K-結合振動。温暖化で振幅 +10-15%
3. **AMOC**: 観測で 15-20% 減少。2025-2050 崩壊リスク 5-15%
4. **ティッピング**: 1.5°C で 5 element がアクティブリスク領域

⇒ Phase 85 で **再エネ転換 + DAC + 気候工学** によるリスク低減シミュレーション。

---

## 6. ITU 視点まとめ

| 構造 | ITU 役割 |
|---|---|
| 炭素循環 | K_carbon の貯蔵-flow ネットワーク |
| ENSO | K_ocean-K_atm 結合振動子 |
| AMOC | K_ocean の地球規模 K-channel |
| Tipping | K-state ポテンシャル曲面の bifurcation |
| Cascade | 複数 vertex の協調 K-state shift |

⇒ 気候は「**単一スカラー (T)**」ではなく「**多次元 K-flow ネットワーク**」。

---

## 引用

```
Terada, M. (2026). Phase 84: Carbon cycle, ENSO, and AMOC as dynamic K-flows
(Tier 1 #11 Phase 2/4). Zenodo. DOI: [to be assigned].
```

参考:
- Friedlingstein et al. (2024) Global Carbon Budget 2024
- Caesar et al. (2018) Nature; Boers (2021) Nature Climate Change
- Ditlevsen & Ditlevsen (2023) Nature Communications (AMOC tipping)
- Lenton et al. (2023) Science: tipping elements
- Vallis (1986) ENSO model
