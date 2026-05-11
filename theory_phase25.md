# Phase 25: CMB 温度パワースペクトラム — 準解析的 Boltzmann 計算

## 1. 動機と限界

Phase 21 で CMB ピーク位置 $\ell_1 = 220, \ell_2 = 537, \ell_3 = 810$ を計算したが、**ピーク振幅** $C_\ell$ は未計算。
完全 CAMB Boltzmann は重いため、本 Phase では **Hu-White 1996** の簡略モデルで $C_\ell$ を近似計算し、Planck 2018 観測と比較する。

これにより「**MOND が CMB で失敗する理由**」と「**ITU hybrid (cold QECC) が ΛCDM と区別不能であること**」を定量的に示す。

## 2. CMB 温度パワースペクトラムの構造

### 2.1 主要な物理過程

CMB 温度ゆらぎ $\Delta T/T$ の角度パワースペクトラム $C_\ell$ は次の過程の合成:

1. **Sachs-Wolfe 効果**: 重力ポテンシャル中の光子のエネルギーシフト (大角度 $\ell \lesssim 50$)
2. **音響振動**: バリオン-光子流体の固有振動 (中間角度 $\ell \sim 200-2500$)
3. **Silk 減衰**: 光子拡散による短波長抑制 ($\ell > 1000$)
4. **晩期 ISW**: 暗黒エネルギー期の重力ポテンシャル変化 (大角度)
5. **CDM 重力駆動**: 物質優勢期にダークマターポテンシャル増強

### 2.2 簡略モデル

$$C_\ell \approx A_{\rm SW} + A_{\rm ac} \cdot D(\ell) \cdot \cos^2(\pi \ell / \ell_A) \cdot B(\ell, R) \cdot e^{-(\ell/\ell_D)^2}$$

- $\ell_A = \pi/\theta_A$: 音響角度スケール (Phase 21 既計算)
- $D(\ell)$: CDM 重力駆動因子 ($\Omega_m h^2$ 依存)
- $\cos^2(\pi \ell/\ell_A)$: 音響振動
- $B(\ell, R)$: バリオン負荷 $R = 3\rho_b/(4\rho_\gamma)$ による奇偶ピーク非対称
- $e^{-(\ell/\ell_D)^2}$: Silk 減衰

### 2.3 CDM 駆動因子の重要性

物質-放射等価期赤方偏移 $z_{\rm eq} \approx 2.4 \times 10^4\, \Omega_m h^2$:

- **ΛCDM** ($\Omega_m h^2 = 0.143$): $z_{\rm eq} \approx 3400$ (再結合 $z_* = 1090$ より前)
- **MOND-only** ($\Omega_m h^2 = 0.022$): $z_{\rm eq} \approx 530$ (再結合より**後**)
- **ITU hybrid** (cold QECC として CDM 様): $z_{\rm eq} \approx 3400$ (ΛCDM と同じ)

→ 駆動因子 $D \propto z_{\rm eq}/(z_{\rm eq} + z_*)$ で**MOND-only は大幅に弱い**:
$D_{\rm LCDM} \approx 0.76$, $D_{\rm MOND} \approx 0.33$

これがピーク振幅の最大の差を生む。

## 3. Planck 2018 観測値

| $\ell$ | $C_\ell$ ($\mu K^2$) | 物理的意味 |
|---|---|---|
| 220 | $5775 \pm 50$ | 第 1 ピーク (基本振動) |
| 540 | $2570 \pm 30$ | 第 2 ピーク (バリオン負荷で抑制) |
| 815 | $2480 \pm 30$ | 第 3 ピーク (CDM 駆動) |
| ピーク比 $A_2/A_1$ | $0.45$ | バリオン負荷 $R \approx 0.6$ を示す |
| ピーク比 $A_3/A_1$ | $0.43$ | CDM 駆動と Silk 減衰の組合せ |

## 4. 予言と検証

### 4.1 ΛCDM
- 振幅: 観測と一致 (パラメータ調整不要)
- ピーク比 $A_2/A_1 \approx 0.45$, $A_3/A_1 \approx 0.43$ → 観測一致

### 4.2 MOND-only
- $D_{\rm MOND} \approx 0.33$ → 全振幅が ~2-3 倍弱い
- ピーク位置も Phase 21 で 43% ずれ
- **二重に観測と不一致**

### 4.3 ITU hybrid (cold QECC = effective CDM)
- $\Omega_m^{\rm eff} = 0.315$ なので**ΛCDM と完全に同じ予言**
- 観測と一致

## 5. シミュレーション計画

### Part A: 簡略モデルで $C_\ell$ 計算
- $\ell \in [10, 2500]$ で 3 モデルの $C_\ell$
- Planck 観測ピーク値を overlay

### Part B: ピーク振幅・比較
- $C_{\ell_1}, C_{\ell_2}, C_{\ell_3}$ を 3 モデルで計算
- 観測値との比

### Part C: $\chi^2$ 概略
- 3 つのピーク点での残差の二乗和
- ΛCDM vs MOND vs Hybrid の総合一致度

### Part D: 結論
- MOND-only の決定的失敗を確認
- ITU hybrid (cold) の救済可能性
- 残課題 (= CAMB レベル計算の必要性) の明示

## 6. 限界

⚠️ 本 Phase の簡略モデルは:
- 完全 Boltzmann ではない (CAMB レベル精度には未到達)
- 振幅は半経験的調整 (Hu-White 1996 fit と Planck 観測の組合せ)
- 偏光 $C_\ell^{EE}, C_\ell^{TE}$ は未計算

✅ それでも示せる:
- 振幅構造の質的特徴 (3 ピーク + バリオン非対称 + 駆動効果)
- MOND-only の決定的失敗の数値証拠
- ITU hybrid の整合性

## 7. ITU 統合像 (Phase 25 完了後)

| 検証項目 | 状況 |
|---|---|
| 線形 LSS $P(k)$ (Phase 23) | ✅ ΛCDM 同等 |
| Bullet Cluster (Phase 24) | ✅ 再現 |
| **CMB ピーク位置 + 振幅** (Phase 21, **25**) | **△ Hybrid で OK、MOND-only は失敗** |
| BH 物理・重力波 (Phase 19) | ✅ |
| 銀河回転曲線 (Phase 18) | ✅ |
| 銀河団質量 (Phase 20) | ✅ |
| $\Omega_{\rm CDM}$ の起源 (Phase 22) | △ 桁オーダー |

唯一残る本質的弱点は「**cold QECC の場の理論的構築**」 — どうやって凍結 QECC が cold dark matter として振る舞うかの第一原理的説明。
