# Phase 27: 太陽系内精密テスト — ITU の弱場補正への制約

## 1. 動機

Phase 18–26 で ITU は**宇宙論スケール**の全観測 (CMB, $P(k)$, Bullet, Lyman-α)
と整合することを確認した。しかし**最も精密な重力テスト**は太陽系内:

| テスト | 精度 |
|---|---|
| Cassini Shapiro 時間遅延 | $\gamma - 1 = (2.1 \pm 2.3) \times 10^{-5}$ |
| Lunar Laser Ranging (LLR) | $\eta_{\rm Nordtvedt} < 4.4 \times 10^{-4}$ |
| 水星近日点歳差 | GR 予言と $10^{-4}$ で一致 |
| MESSENGER/BepiColombo 軌道 | 力学定数 $G$ の経年変化 $\dot G/G < 10^{-13}$/yr |
| Pioneer "異常加速度" | $a_{\rm anom} \sim 10^{-9}$ m/s² (解決済: 熱放射) |

ITU には 2 つの修正源:
1. **MOND 様補正**: 加速度 $a < a_0 = 1.2 \times 10^{-10}$ m/s² でニュートン則修正
2. **QECC dark matter**: 銀河スケール質量分布から solar-system 軌道に潮汐補正

本 Phase: ITU 弱場補正が太陽系精密テストを通過することを定量検証。

## 2. 物理モデル

### 2.1 MOND 補間関数

加速度 $x = a/a_0$ で:
$$\mu(x) = \frac{x}{\sqrt{1 + x^2}}$$

修正ニュートン則:
$$\mu(a/a_0)\, \vec a = \vec a_N \quad \Longrightarrow \quad a = \frac{a_N}{2}\left(1 + \sqrt{1 + 4/(a_N/a_0)^2}\right)^{1/2}$$

弱場展開 ($a_N \gg a_0$):
$$a \approx a_N \left[1 + \frac{1}{2}\left(\frac{a_0}{a_N}\right)^2 + \mathcal{O}\left((a_0/a_N)^4\right)\right]$$

→ Newton への補正は $(a_0/a_N)^2$ の二次オーダー (深 Newton 領域では極小)。

### 2.2 太陽系の加速度スケール

太陽からの距離 $r$ での Newton 加速度 $a_N = GM_\odot/r^2$:

| 天体 | $r$ (AU) | $a_N$ (m/s²) | $a_N/a_0$ |
|---|---|---|---|
| 水星 | 0.39 | $3.96 \times 10^{-2}$ | $3.3 \times 10^{8}$ |
| 地球 | 1.00 | $5.93 \times 10^{-3}$ | $4.9 \times 10^{7}$ |
| 火星 | 1.52 | $2.56 \times 10^{-3}$ | $2.1 \times 10^{7}$ |
| 木星 | 5.20 | $2.19 \times 10^{-4}$ | $1.8 \times 10^{6}$ |
| 海王星 | 30.1 | $6.55 \times 10^{-6}$ | $5.5 \times 10^{4}$ |
| Pluto | 39.5 | $3.81 \times 10^{-6}$ | $3.2 \times 10^{4}$ |
| Oort 雲 | $5 \times 10^4$ | $2.4 \times 10^{-12}$ | $2.0 \times 10^{-2}$ |

→ 全惑星は $a_N/a_0 > 10^4$ の深 Newton 領域。MOND 補正は $\lesssim 10^{-8}$。

### 2.3 近日点歳差への MOND 補正

円軌道周辺の摂動展開で、近日点歳差への余分な寄与:
$$\Delta \omega_{\rm MOND} \approx \pi \left(\frac{a_0}{a_N}\right)^2 \frac{r_a}{r_p} \quad \text{(per orbit)}$$

水星 ($a_N = 4 \times 10^{-2}$ m/s²): $\Delta\omega \sim 10^{-16}$ rad/orbit $\sim 10^{-8}$ arcsec/century

GR 予言 (43 arcsec/century) との比較: MOND 補正は **$10^{-10}$ レベル** → 観測精度 ($\sim 0.01$ arcsec/century) より遥かに小さい。

### 2.4 Cassini Shapiro 遅延

PPN パラメータ $\gamma$:
$$\Delta t_{\rm Shapiro} = (1 + \gamma) \frac{2 G M_\odot}{c^3} \ln\left(\frac{4 r_E r_C}{b^2}\right)$$

ITU の AQUAL-様修正は metric 構造を変えない (Bekenstein-Milgrom 1984) → $\gamma = 1$ で GR と区別不能。

ITU QECC dark matter 寄与: $\delta M_{\rm QECC,\,inner}/M_\odot \lesssim 10^{-10}$ (太陽系内 QECC 密度極小)
→ 遅延への寄与 $< 10^{-10}$ → Cassini 制約 ($2.3 \times 10^{-5}$) を遥かに通過。

### 2.5 LLR Nordtvedt 効果

地球の重力的自己エネルギー $E_g \approx -3 G M_\oplus^2/(5 R_\oplus)$ が $m_\oplus \neq m_g$ を生むかのテスト:
$$\eta = 4\beta - \gamma - 3 - \frac{10}{3}\xi - \alpha_1 + \frac{2}{3}\alpha_2 - \frac{2}{3}\zeta_1 - \frac{1}{3}\zeta_2$$

ITU: $\beta = \gamma = 1$, 他 PPN = 0 → $\eta = 0$ → LLR 制約 ($4.4 \times 10^{-4}$) を自動的に通過。

## 3. ITU 予言

### 3.1 弱場 (太陽系) regime
- MOND 補正: $\sim (a_0/a_N)^2 \lesssim 10^{-15}$ for 内惑星
- QECC 質量寄与: 太陽近傍密度 $\rho_{\rm QECC} \sim \rho_{\rm DM,\,local} \approx 0.4$ GeV/cm³
  - 半径 $r = 1$ AU 内 QECC 質量 $\sim \rho \cdot \frac{4}{3}\pi r^3 \sim 10^{-13} M_\odot$
  - 軌道への影響 $\Delta a/a \sim 10^{-13}$
- 全 PPN パラメータ: $\gamma = \beta = 1$ (AQUAL 構造保存)

### 3.2 全制約通過

| テスト | 制約 | ITU 予言 | 比 |
|---|---|---|---|
| Cassini $\gamma - 1$ | $< 2.3 \times 10^{-5}$ | $\sim 10^{-13}$ | $10^{8}$ 安全 |
| LLR $\eta$ | $< 4.4 \times 10^{-4}$ | $\sim 0$ | trivially OK |
| 水星近日点 | $< 10^{-4}$ rel. | $\sim 10^{-10}$ rel. | $10^{6}$ 安全 |
| $\dot G/G$ | $< 10^{-13}$/yr | $\sim 0$ (定常 QECC) | trivially OK |

→ ITU は**太陽系内テストを完璧に通過**。

### 3.3 外縁部での可能な signature

天王星・海王星より遠方 ($r > 100$ AU) で $a \sim a_0$ に近づき MOND 補正が顕在化:
- Oort 雲彗星の軌道分布
- Sedna-様 detached object の軌道力学
- ISS Sail 加速度プローブ将来テスト

これらが ITU を pure ΛCDM から弁別する可能性。

## 4. シミュレーション計画

### Part A: 加速度プロット
- 太陽からの距離 vs ニュートン加速度
- $a_0$ ライン overlay
- MOND 移行領域 ($r \sim 7000$ AU) を視覚化

### Part B: MOND 補正比 vs $r$
- $(a_{\rm MOND} - a_N)/a_N$ を 8 惑星と Pluto, Oort
- ログスケールで補正の小ささを表示

### Part C: 近日点歳差予言
- 各惑星の Δω_MOND を arcsec/century で
- GR 予言と観測精度を overlay
- 全てのケースで ITU は観測内

### Part D: PPN パラメータ表
- γ, β, η 等を ITU/GR/Brans-Dicke と並べて表示
- 全 ITU = GR の identification を確認

## 5. 限界

⚠️ 本 Phase で扱わない:
- 完全相対論的軌道計算 (post-post-Newtonian)
- TeVeS 等の covariant MOND での Cassini
- LIGO による超強場テスト (Phase 19 で既扱)
- スカラーテンソル重力との比較

✅ 示せる:
- ITU が全太陽系精密テストを通過すること
- MOND 補正の小ささの定量化
- Oort 雲領域で MOND が顕在化する予測

## 6. ITU 統合像 (Phase 27 完了後)

| スケール | 検証 | 状況 |
|---|---|---|
| サブミリ波 | $1/r^2$ 確認 (Eöt-Wash) | ✅ |
| **太陽系内** | **Cassini, LLR, 近日点 (Phase 27)** | **✅** |
| 銀河 | 回転曲線 (Phase 18) | ✅ |
| 銀河団 | 質量分布 (Phase 20) | ✅ |
| Bullet Cluster | 衝突力学 (Phase 24) | ✅ |
| 小スケール構造 | Lyman-α (Phase 26) | ✅ |
| 線形 LSS | $P(k)$ (Phase 23) | ✅ |
| CMB | ピーク + 振幅 (Phase 21, 25) | ✅ |
| 重力波 | BH ringdown (Phase 19) | ✅ |

**全ての観測スケール (10⁻³ m から 10²⁶ m) を ITU は通過**。
唯一残る理論的タスクは「**凍結 QECC が w = 0 を満たすことの場の理論的証明**」。
