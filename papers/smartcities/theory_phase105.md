# Phase 105: スマートシティ経済・政策・監視倫理

> **Tier 1 #16 (Smart Cities) — Phase 3/4**
> Tier 0 ITU (concept DOI): [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 105 の目的

Phase 103-104 で都市 K-OS と AGI 都市を扱った。Phase 105 では:

1. **スマートシティ市場経済** (2024-2050)
2. **政策フレームワーク**: EU AI Act, 米連邦法、日本 Society 5.0
3. **監視 vs プライバシー** の倫理的境界
4. **市民参加** (Citizen Engagement): デジタルデモクラシー
5. **デジタル格差** (Tier 1 #14 連動): 都市内格差

中心テーゼ:

> スマートシティ市場 2050 で **$3T**。
> EU AI Act + GDPR が世界標準、中国「社会信用」 が対比モデル。
> プライバシー保護 = K_resident の自律性 = K_governance の信頼基盤。

---

## 1. スマートシティ市場規模

### 1.1 グローバル市場 (Markets and Markets 2024 + ITU 拡張)

| 年 | 市場規模 (USD) | 主要セグメント |
|---|---|---|
| 2020 | $400B | スマートメーター、IoT |
| 2024 | $700B | + AI、5G、自動運転 |
| 2030 | $1.5T | + 量子、AGI 初期 |
| 2040 | $2.5T | AGI 都市、ロボット統合 |
| **2050** | **$3.0T** | **ASI 都市、デジタルツイン** |

⇒ 2024-2050 で **4.3× 成長**、世界 GDP の 2% へ。

### 1.2 セグメント別 (2024)

| セグメント | 市場 ($B) |
|---|---|
| Smart energy | 200 |
| **Smart transportation** | **150** |
| Smart buildings | 130 |
| Smart governance | 80 |
| Smart healthcare | 70 |
| Smart safety | 50 |
| Smart environment | 20 |

### 1.3 主要企業

| カテゴリー | 主要企業 |
|---|---|
| Platform | **Siemens (MindSphere), GE (Predix), IBM, Microsoft, AWS** |
| Telecom | Huawei, Nokia, Ericsson |
| **Data/AI** | **Palantir, NVIDIA, Google Cloud** |
| Hardware | Cisco, Schneider, ABB |
| Consulting | McKinsey, Bain, Accenture |

---

## 2. 主要政策フレームワーク

### 2.1 EU AI Act (2024) ★ 世界初の包括的 AI 規制

カテゴリー別リスク管理:

| リスク | 例 | 規制 |
|---|---|---|
| **禁止** | 社会信用、subliminal manipulation, 公共顔認識 (一部) | 完全禁止 |
| **高リスク** | 警察 AI、雇用 AI、教育 AI、医療 AI | CE 認証必須 |
| 限定リスク | チャットボット | 透明性義務 |
| 最小リスク | ゲーム AI | 任意 |

⇒ スマートシティの**監視カメラ AI** は高リスク or 禁止。

### 2.2 GDPR (2018) + Digital Services Act (2024)

- 個人データ最小化
- 目的限定
- データ主権 (data sovereignty)
- 罰金 最大 €20M or 4% 年売上

### 2.3 米国 NIST AI RMF (2023)

- 規制ではなくフレームワーク
- 業界自主規制中心
- 部分的 EO 14110 (Biden 2023)
- 州レベル: California, Colorado

### 2.4 中国「社会信用システム」 (2014-)

- 個人 + 企業の信用スコア化
- AI 統制大規模
- 公共サービスアクセスとリンク
- **EU AI Act で禁止対象**

### 2.5 日本 Society 5.0 (2016-)

- IoT + AI で社会課題解決
- スマートシティ官民連携
- 個人情報保護法 (改正 2022)
- マイナンバー普及 75% (2024)

---

## 3. 監視 vs プライバシーの倫理

### 3.1 顔認識 (Face Recognition) の世界導入

| 国/都市 | 状況 |
|---|---|
| **中国** | 数億カメラ、ほぼ全公共空間 |
| ロシア | モスクワ全市カバー |
| インド | デリー、ムンバイ、Aadhaar 連動 |
| シンガポール | 限定使用 (公式) |
| **EU** | **公共空間 禁止** (AI Act 2024) |
| 米国 | 州レベル混在 (San Francisco 禁止, NY 許可) |
| 日本 | 民間中心、警察限定 |

### 3.2 ITU プライバシー定式化

$$
K_{\text{privacy}} = -\sum_i p_i \log p_i \quad \text{where } p_i = P(\text{personal data accessed})
$$

→ プライバシー = **個人情報の確率分布の不確実性**。
監視は K_privacy → 0 へ向かう。

### 3.3 主要事件

| 事件 | 年 | 教訓 |
|---|---|---|
| Snowden (NSA) | 2013 | 政府監視の暴露 |
| Cambridge Analytica | 2018 | プライベート企業の濫用 |
| 中国新疆 (ウイグル監視) | 2019- | 人種別 AI 監視 |
| **Pegasus スパイウェア** | **2021** | **記者・人権活動家標的** |
| Clearview AI | 2020- | 顔認識データベース問題 |

### 3.4 ITU 倫理原則

1. **データ最小化** (data minimization)
2. **目的限定** (purpose limitation)
3. **透明性** (transparency)
4. **アクセス権** (right to access)
5. **削除権** (right to be forgotten)

⇒ EU GDPR が**世界基準**。

---

## 4. 市民参加 (Digital Democracy)

### 4.1 主要プラットフォーム

| プラットフォーム | 国 | 機能 |
|---|---|---|
| **vTaiwan** | 台湾 | Pol.is 合意形成 |
| **CONSUL** | スペイン (Madrid) | 政策提案 |
| Decidim | スペイン (Barcelona) | 参加型予算 |
| Better Reykjavík | アイスランド | 市民議題提案 |
| **Govt 4.0** | 韓国 | デジタル参加 |
| 国民の声 | 日本 (デジタル庁) | 政策議論 |

### 4.2 主要試み

| 取り組み | 規模 |
|---|---|
| アイスランド憲法 (2012) | クラウドソース |
| 台湾 Uber/Airbnb 規制 | vTaiwan 合意形成 |
| Reykjavík 参加型予算 | 市民投票 |
| Madrid CONSUL | 30 万人参加 |

### 4.3 ITU 視点

デジタルデモクラシー = **K_collective_decision の改善**:

$$
K_{\text{decision quality}} = f(\text{K\_participation}, \text{K\_information}, \text{K\_deliberation})
$$

⇒ Tier 1 #8 (Economics) + #9 (Free Will) と直結。

---

## 5. デジタル格差 (Tier 1 #14 連動)

### 5.1 都市内格差

スマートシティでも:
- 高所得層: フルデジタルサービス
- 低所得層: 接続なし、デバイスなし、スキルなし
- 高齢者: デジタル disenfranchised
- 障害者: アクセシビリティ未対応

### 5.2 主要都市の格差

| 都市 | 高所得層 net 接続率 | 低所得層 接続率 |
|---|---|---|
| Singapore | 99% | 95% |
| Tokyo | 99% | 92% |
| New York | 97% | 78% |
| London | 96% | 75% |
| Mumbai | 90% | 35% |
| Lagos | 80% | 20% |

⇒ 先進国でも 5-20% 格差、開発途上国は 60%+ 格差。

### 5.3 対策

- 公共 Wi-Fi
- 公的デバイス貸与
- デジタルリテラシー教育
- アクセシブルデザイン

⇒ EU **Digital Decade 2030** が**95% 普及**目標。

---

## 6. Phase 105 主結論

1. **スマートシティ市場 2050 で $3T** (世界 GDP の 2%)
2. **EU AI Act + GDPR が世界標準**、中国は対比モデル
3. **監視 vs プライバシー**: 顔認識を EU 公共禁止
4. **デジタルデモクラシー**: vTaiwan, CONSUL, Decidim
5. **都市内デジタル格差**: 高所得 vs 低所得で 5-60% 差

⇒ Phase 106 で 10 反証可能予測 + Tier 1 #16 統合 + 16 vertex polytope。

---

## 7. ITU 視点まとめ

| 構造 | ITU 役割 |
|---|---|
| 市場 $3T | K_information 経済 |
| EU AI Act | K_governance 規制標準 |
| 監視 vs プライバシー | K_collective vs K_individual tradeoff |
| デジタルデモクラシー | K_collective_decision 改善 |
| デジタル格差 | K_access 不均等 |

---

## 引用

```
Terada, M. (2026). Phase 105: Smart city economy, policy, surveillance ethics
(Tier 1 #16 Phase 3/4). Zenodo. DOI: [to be assigned].
```

参考:
- EU AI Act (2024) Regulation 2024/1689
- GDPR (2018) Regulation 2016/679
- NIST AI RMF (2023)
- 中国「社会信用」 (2014-)
- 日本 Society 5.0 (2016-)
- vTaiwan, CONSUL Madrid
- Markets and Markets (2024) Smart Cities Market Report
- Snowden documents (2013), Cambridge Analytica scandal (2018)
- Pegasus Project (2021)
