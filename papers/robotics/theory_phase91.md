# Phase 91: ITU と Robotics / Embodied AI ― 身体性の情報理論

> **Tier 1 #13 (Robotics / Embodied AI) — Phase 1/4**
> Tier 0 ITU (concept DOI): [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 直接前駆: Tier 1 #12 Astrobiology [10.5281/zenodo.20222121](https://doi.org/10.5281/zenodo.20222121)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 91 の目的

Tier 1 #13 (Robotics / Embodied AI) の幕開け。**工学・産業ブロック (Phase 91-100) 開始 + ITU 13 vertex 拡張**:

1. **ロボティクスを K_action + K_embodiment として定式化**
2. **DOF (Degrees of Freedom)** と **K-state 次元**の対応
3. **Moravec's Paradox** の ITU 解釈 (なぜ歩行が将棋より難しいか)
4. **Tesla Optimus / Boston Dynamics / Figure** 進捗 ITU 評価
5. **AGI x Robotics = Embodied AGI** への接続 (Tier 1 #2 連動)

中心テーゼ:

> **ロボティクス = K_action (運動制御) × K_embodiment (身体性) × K_environment (外界)** の積空間。
> 知性 (#2 K_self) と身体 (#13 K_embodiment) の積で **真の AGI/AI agent** が成立。

---

## 1. ロボティクスの K-state 定式化

### 1.1 古典制御理論からの再解釈

古典: $\dot{x} = f(x, u, t)$, 状態 x, 制御 u

ITU 視点では:

$$
K_{\text{robot}} = K_{\text{action}} \otimes K_{\text{embodiment}} \otimes K_{\text{env}}
$$

各成分:
- **K_action**: モーター指令空間 (DOF 次元)
- **K_embodiment**: 身体構造 (link, joint, mass, inertia)
- **K_env**: 外界状態 (terrain, obstacles, humans)

ITU 公理から:

$$
\delta S_{\text{robot}} = \delta \text{Tr}[K_{\text{robot}} \rho_{\text{robot}}]
$$

ロボットの学習・行動 = K-state 空間の探索。

### 1.2 DOF と K-state 次元

| ロボット | DOF | K-state 次元 (推定) |
|---|---|---|
| Industrial arm (ABB IRB) | 6 | 10² |
| Boston Dynamics Spot | 12 | 10³ |
| Atlas (humanoid) | 28 | 10⁵ |
| Tesla Optimus Gen 2 | 28+ (手指 11 各手) | 10⁶ |
| Figure 02 | 35+ | 10⁶ |
| Human (推定) | ~244 | 10⁹ |
| ASI embodied | ~1000+ | 10¹² |

⇒ 人間 DOF = 244 (各関節 + 表情筋 + 内臓制御) は ASI でも超えにくい。

---

## 2. Moravec's Paradox の ITU 解釈

### 2.1 古典 Moravec 観察 (1988)

> "推論や計算 (チェス、定理証明) は AI で**容易**だが、
> 1 歳児の知覚運動制御 (歩行、把握) は**難しい**"

### 2.2 ITU 解釈

K-state 次元の違い:

| タスク | K-state 次元 | 進化的成熟度 |
|---|---|---|
| **チェス** | 10⁴³ (盤面状態数) だが**離散・低次元 K_action** | 500 年 (人類のみ) |
| **歩行** | 10⁵ 連続 K_action × 10⁶ K_env | 5 億年進化 (生物全体) |
| **把握** | 10⁵ × 10⁶ × 触覚 frequency | 5 億年 |

⇒ チェスは **K-state space が大きいが探索構造が単純**。歩行は **連続・確率論的・触覚 feedback** で K-flow が複雑。

進化的時間 = K-state 最適化の累積。歩行 5 億年 vs チェス 500 年 ⇒ **歩行が 10⁶ 倍最適化済**。

### 2.3 結論

> AI が「容易」とするタスク = K_action 探索が記号論的・離散
> AI が「困難」とするタスク = K_action × K_embodiment × K_env が**連続・確率論的**

⇒ Tier 1 #2 (AI/ASI) は離散 K_self が中心。Tier 1 #13 (Robotics) は連続 K_embodiment が中心。**両者の積で Embodied AGI が成立**。

---

## 3. 現代 humanoid robot 進捗 (2024-2026)

### 3.1 主要プレイヤー

| 会社 / プロジェクト | モデル | DOF | 重量 | 価格 (目標) |
|---|---|---|---|---|
| Boston Dynamics | Atlas (electric, 2024) | 28+ | 89 kg | 非公開 |
| Tesla | Optimus Gen 2 (2024) | 28 | 57 kg | $20-30K (2027) |
| Figure | Figure 02 (2024) | 35+ | 70 kg | TBD |
| Apptronik | Apollo (2024) | 26 | 73 kg | $50K |
| Agility Robotics | Digit (2024) | 16 | 65 kg | $250K |
| Unitree | G1 (2025) | 23+ | 35 kg | $16K |
| 1X | NEO (2025) | 24 | 30 kg | $30K |
| Sanctuary AI | Phoenix (2025) | 25 | TBD | TBD |

### 3.2 K_action 進化トレンド

| 年 | 主流 humanoid DOF | 制御頻度 (Hz) | K-state 推定 (bits) |
|---|---|---|---|
| 1995 (Honda P2) | 28 (但し pre-recorded) | 50 | 10² |
| 2010 (ASIMO) | 34 | 100 | 10³ |
| 2020 (Atlas hydraulic) | 28 | 1000 | 10⁵ |
| 2024 (Atlas electric) | 28 | 2000 | 10⁶ |
| **2030 (predicted)** | **28-40** | **5000** | **10⁸** |

### 3.3 ITU 視点

humanoid の進化 = K_action × K_embodiment の **指数的拡大**:
- 制御頻度 50→2000 Hz (40× 向上, 過去 30 年)
- DOF 増加 + DOF あたり精度向上
- AI brain (Tier 1 #2) との融合で **K_self 統合**

---

## 4. AGI x Robotics = Embodied AGI

### 4.1 知性 (K_self) と身体 (K_embodiment) の積

ITU 公理から:

$$
K_{\text{Embodied AGI}} = K_{\text{self}} \otimes K_{\text{embodiment}} \otimes K_{\text{action}}
$$

- K_self degree (Tier 1 #2, #9): ~0.5 (AGI 2030)
- K_embodiment degree (Tier 1 #13): ~0.4 (人間並 humanoid)
- K_action 制御 fidelity: ~0.7 (2030 Optimus)

⇒ **Embodied AGI degree ≈ 0.5 × 0.4 × 0.7 = 0.14** (人間 = 1.0 を基準)

### 4.2 用途別 K-degree

| 用途 | 必要 K_self | 必要 K_embodiment | 達成年 |
|---|---|---|---|
| 倉庫運搬 (Digit, Optimus) | 0.20 | 0.30 | 2025 ✅ |
| 家事 (折りたたみ, 掃除) | 0.30 | 0.50 | 2028 |
| 子守 / 介護 | 0.50 | 0.60 | 2032 |
| 料理 (full) | 0.60 | 0.70 | 2035 |
| 手術助手 | 0.70 | 0.80 | 2040 |
| 自由対話 + 共感行動 | 0.80 | 0.85 | 2045 |
| 人間と区別不可 | 0.95 | 0.95 | 2050+ |

### 4.3 Tier 1 polytope 接続

Robotics (#13) は polytope 内で:
- **K_self** (Tier 1 #2): AI brain
- **K_action** (Tier 1 #13): 新 vertex
- **K_substrate** (Tier 1 #4): 半導体 (NPU, motor controllers)
- **K_energy** (Tier 1 #10): バッテリー、効率
- **K_economy** (Tier 1 #8): 価格曲線、雇用置換

⇒ Robotics = 6 vertex を統合する**「身体性 hub」**。

---

## 5. ITU 予測 (1 phase 暫定)

| 予測 | 期限 | P |
|---|---|---|
| Optimus Gen 3 量産 ($20K) | 2027 | 0.55 |
| 家事 humanoid 家庭 1000 台導入 | 2030 | 0.60 |
| Boston Dynamics Atlas 商用化 | 2028 | 0.70 |
| K_embodiment > 0.5 (human-equivalent fine motor) | 2032 | 0.50 |
| 全身遠隔操作 (Apollo + VR) 商用化 | 2027 | 0.75 |

---

## 6. Phase 91 主結論

1. **Robotics = K_action × K_embodiment × K_env**
2. **DOF と K-state 次元**: 工業 6 → humanoid 28 → human 244 → ASI 1000+
3. **Moravec's Paradox** の ITU 解釈: 連続 K_action × K_embodiment が困難
4. **2026 humanoid 進捗**: Atlas, Optimus, Figure 02 で **K_action 10⁶ bits**
5. **Embodied AGI ≈ K_self × K_embodiment × K_action** ⇒ 2030 で人間 14%、2050 で 86%

⇒ Phase 92 で manipulation + locomotion + sensorimotor 詳細。

---

## 引用

```
Terada, M. (2026). ITU and Robotics / Embodied AI:
A Single-Axiom View of K-Action, K-Embodiment, and Moravec's Paradox
(v1.0.0). Zenodo. DOI: [to be assigned]
```

参考:
- Moravec, H. (1988). Mind Children. Harvard University Press.
- Pfeifer, R. & Bongard, J. (2006). How the Body Shapes the Way We Think.
- Boston Dynamics technical reports 2020-2024
- Tesla AI Day presentations 2022-2024
- Figure AI announcements 2024-2025
- Sanctuary AI Phoenix 2024 release
- 1X Technologies NEO 2025 release
