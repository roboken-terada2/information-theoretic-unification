# Phase 92: Manipulation + Locomotion + Sensorimotor ― K-flow 動力学

> **Tier 1 #13 (Robotics / Embodied AI) — Phase 2/4**
> Tier 0 ITU (concept DOI): [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 92 の目的

Phase 91 で「Robotics = K_action × K_embodiment × K_env」と定式化した。Phase 92 では:

1. **Manipulation** (把握・操作) の K_action-K_tactile 結合
2. **Locomotion** (歩行・走行) の動的安定性 (ZMP, MPC)
3. **Sensorimotor** ループの ITU 視点 (Bayesian feedback)
4. **End-to-end neural policy** (RL, VLA models) の K-flow 制約
5. **触覚・視覚・本体感覚** の multi-modal K-fusion

中心テーゼ:

> ロボティクスは **knowing (K_self) + doing (K_action)** の閉ループ。
> Sensorimotor = ITU の δS = δ⟨K⟩ を**実時間制御**として具現化。
> 認知 (推論 100ms) と制御 (1ms) は**異なる K-time scale**で動く。

---

## 1. Manipulation の K-flow 動力学

### 1.1 把握タスクの分解

把握 (grasping):
1. 視覚で物体検出 (object detection) → K_vision
2. 物体の grasp 候補生成 → K_plan
3. アーム軌道計画 → K_trajectory
4. 把握実行 + 触覚 feedback → K_tactile
5. 状態確認 + 失敗時リトライ → K_loop

### 1.2 K-channel 構造

$$
K_{\text{manipulation}} = K_{\text{vision}} \oplus K_{\text{plan}} \oplus K_{\text{trajectory}} \oplus K_{\text{tactile}} \oplus K_{\text{loop}}
$$

各成分の bandwidth (情報量):

| K-channel | 周波数 (Hz) | bits/sample | total bits/sec |
|---|---|---|---|
| Vision (RGB-D) | 30-60 | 10⁷ | 3×10⁸ |
| Plan (high-level) | 1-10 | 10³ | 10⁴ |
| Trajectory (low-level) | 100-1000 | 10² | 10⁵ |
| **Tactile (skin)** | **100-1000** | **10³** | **10⁶** |
| Proprioception | 1000 | 10² | 10⁵ |

⇒ 触覚は **歴史的に最も遅れた modality** だが、把握の**根幹**。Manipulation の K-bottleneck は触覚。

### 1.3 現代ロボットハンド進捗

| ハンド | 指数 | DoF/hand | 触覚センサ | 進歩年 |
|---|---|---|---|---|
| Shadow Hand (2010s) | 5 | 24 | ~100 触覚点 | 2014 |
| Stretch (Hello Robot) | 1 | 1 (gripper) | なし | 2020 |
| **Tesla Optimus hand (Gen 2)** | **5** | **11** | **触覚 + 圧力** | **2024** |
| **Figure 02 hand** | **5** | **16** | **fingertip touch** | **2024** |
| Sanctuary Phoenix hand | 5 | 20+ | TacTip-based | 2024 |
| Human hand | 5 | ~27 | 10,000+ メカノレセプター | (進化) |

⇒ 人間の触覚解像度は **100×** 残存 (各指の表面に 1000 受容器)。

---

## 2. Locomotion の動的安定性

### 2.1 ZMP (Zero Moment Point) 制御

ASIMO (2000s) の根幹:

$$
\text{ZMP}: \text{接触面内に重心投影} \Rightarrow \text{安定歩行}
$$

ITU 視点:
- ZMP = K_balance の不動点
- 歩行 = K_state を ZMP 集合内に保つ動的制御

### 2.2 MPC (Model Predictive Control) + RL

Atlas (BD electric, 2024):
- **Whole-body MPC**: 28 DOF を 1000+ Hz で全体最適化
- **Pre-trained RL** policy: simulation で 10⁸ 歩学習
- リアル世界では fine-tuning のみ

### 2.3 K-time scale 階層

| 階層 | 制御頻度 | K-action 例 |
|---|---|---|
| Reflex (脊髄反射) | 1-10 ms | 関節角度フィードバック |
| Motor control | 10-50 ms | 関節トルク調整 |
| Local planning | 100 ms | 着地点選択 |
| Path planning | 1 s | 経路全体 |
| **Cognitive** | **>10 s** | **タスク選択** |

⇒ AI brain (Tier 1 #2) は cognitive 層で動作。Robotics K_action は motor 層が中心。

### 2.4 数値: humanoid 歩行進歩

| 年 | プラットフォーム | 歩行速度 (m/s) | 段差対応 | 走行 |
|---|---|---|---|---|
| 2000 | ASIMO | 0.5 | 階段 | × |
| 2013 | Atlas v1 (DRC) | 0.4 | 不整地 | × |
| 2018 | Atlas (Parkour) | 1.5 | パルクール | jogging |
| 2020 | Atlas (dance) | 2.0 | back flip | sprinting |
| **2024** | **Atlas electric** | **2.5** | **complex** | **5.6 m/s 走行** |
| 2030 (proj) | Embodied AGI | 4.0 | human-level | human-level |
| Human (avg) | — | 1.4 (walk), 3-4 (run) | natural | (進化) |

---

## 3. Sensorimotor Loop の ITU 定式化

### 3.1 Bayesian sensorimotor (Körding & Wolpert 2004)

人間の運動制御は **Bayesian 推論**として記述可能:

$$
P(\text{action}|\text{state}) \propto P(\text{state}|\text{action}) \cdot P(\text{action})
$$

### 3.2 ITU 視点

ITU では K_self が **予測 K_predict** と **観測 K_observed** を比較し、誤差を最小化:

$$
\frac{dK_{\text{action}}}{dt} = -\gamma (K_{\text{predict}} - K_{\text{observed}})
$$

⇒ Active Inference (Friston, Tier 1 #7 連動) と整合。

### 3.3 RL 学習による K-policy 形成

PPO / SAC / GRPO 等の RL:

$$
\pi_\theta(a|s) = \arg\max_\theta E[\sum_t \gamma^t r_t]
$$

ITU 視点:
- π = K_action policy
- r = K_reward signal (タスク特化)
- ⇒ RL = **K-action 空間の最適化 K-flow**

### 3.4 RT-2, OpenVLA, π0: VLA models

最近 (2023-2024) の **Vision-Language-Action (VLA)** モデル:

| モデル | パラメータ | 訓練データ | 制御 freq |
|---|---|---|---|
| RT-2 (DeepMind 2023) | 12-55B | Web + robot | 1-10 Hz |
| OpenVLA (Stanford 2024) | 7B | 1M robot trajectories | 5-10 Hz |
| **π0 (Physical Intelligence 2024)** | **3B** | **10K hr robot** | **50 Hz** |
| Helix (Figure 2024) | TBD | TBD | hierarchical |

⇒ VLA = **Language brain (K_self) + Action (K_action) の融合**。
Tier 1 #2 (LLM) と Tier 1 #13 (Robotics) の**直接接続**。

---

## 4. Multi-modal K-fusion

### 4.1 人間の感覚情報量

| 感覚 | 帯域 (bits/sec) | 受容器数 |
|---|---|---|
| 視覚 | 10⁷ | 1.3×10⁸ |
| 聴覚 | 10⁵ | 1.5×10⁴ |
| 触覚 | 10⁵ | 10⁶ |
| 嗅覚 | 10² | 10⁷ (低帯域) |
| 味覚 | 10¹ | 10⁵ |
| 本体感覚 | 10⁴ | 10⁵ |
| **意識帯域 (Norretranders)** | **~50** | — |

⇒ 感覚入力 10⁷ bits/sec → 意識アクセス 50 bits/sec。**情報圧縮率 10⁵**。

### 4.2 ロボット sensor fusion

| ロボット | 視覚 | 触覚 | LIDAR | IMU | total bits/sec |
|---|---|---|---|---|---|
| Tesla Optimus | 8 cameras 60Hz | 簡易 | × | あり | 5×10⁸ |
| Figure 02 | 多眼 | finger tip | × | あり | 5×10⁸ |
| Atlas electric | stereo | 限定 | あり | あり | 10⁹ |
| 人間 | 2 eye | 全身皮膚 | × | 全身 | 10⁷ |

⇒ ロボットの sensor bandwidth は **人間 100× 上回る**が、それを**統合**できる K_self は AGI 待ち。

---

## 5. Phase 92 主結論

1. **Manipulation の K-bottleneck = 触覚** (人間 100× 残存)
2. **Locomotion**: Atlas electric 2024 で 5.6 m/s 走行 (人間 sprinter 並)
3. **Sensorimotor**: Bayesian + RL = ITU active inference の実装
4. **VLA models** (RT-2, π0): Tier 1 #2 ↔ #13 を直接接続
5. **Sensor bandwidth**: ロボット 5×10⁸ bits/sec (人間 10⁷ の 50× ) — 統合は K_self 待ち

⇒ Phase 93 で AGI 統合 + 産業展開 + 経済・倫理影響。

---

## 6. ITU 視点まとめ

| 構造 | ITU 役割 |
|---|---|
| Manipulation | K_vision ⊕ K_plan ⊕ K_tactile fusion |
| Locomotion | K_balance 不動点 + 多階層 K-time scale |
| Sensorimotor | Bayesian δS = δ⟨K⟩ 実時間版 |
| VLA model | K_self (LLM) ⊗ K_action (motor) |
| Multi-modal | K-channel 統合、人間意識 50 bps への圧縮 |

⇒ ロボティクスは **Tier 1 #2, #7 (FEP/Friston), #4 (Semi), #10 (Energy)** の交差点。

---

## 引用

```
Terada, M. (2026). Phase 92: Manipulation, locomotion, and sensorimotor
as K-flow dynamics (Tier 1 #13 Phase 2/4). Zenodo. DOI: [to be assigned].
```

参考:
- Vukobratović, M. & Stepanenko, J. (1972). Six-legged walking robot.
- Körding, K. & Wolpert, D. (2004). Bayesian integration in sensorimotor learning. Nature 427, 244.
- Friston, K. (2010). The free-energy principle: a unified brain theory? Nat. Rev. Neurosci. 11, 127.
- Rao, B. et al. (2023). RT-2: Vision-Language-Action Models. DeepMind.
- Kim et al. (2024). OpenVLA: An Open-Source Vision-Language-Action Model.
- Physical Intelligence (2024). π0: A Vision-Language-Action Flow Model.
- Boston Dynamics technical reports 2018-2024 (Atlas parkour, electric).
- Norretranders, T. (1998). The User Illusion (consciousness bandwidth).
