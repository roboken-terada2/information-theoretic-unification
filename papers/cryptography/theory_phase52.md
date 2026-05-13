# Phase 52: BB84 + 量子鍵配送 (QKD) の ITU 詳細解析

## 1. 動機

Phase 51 で **ITU 情報理論的セキュリティの基礎**を確立した。本 Phase で
量子鍵配送 (Quantum Key Distribution, QKD) の最も重要な protocol **BB84** を
詳細に解析し、ITU 由来の改善案を提示する。

QKD の実用化は急速に進んでおり (2020 年代に商用 QKD 衛星, fiber 網):
- 中国: Micius 衛星 + Beijing-Shanghai QKD 網 (>2000 km)
- 欧州: EuroQCI (European Quantum Communication Infrastructure)
- 米国: 各種 R&D + DARPA QKD network
- 日本: NICT Tokyo QKD network

**Phase 52 の核心**: ITU 公理から派生する **「QECC-enhanced QKD」** が
従来 BB84 を 2-5× 上回る性能を出せるか検証。

---

## 2. BB84 の現代的実装

### 2.1 標準 BB84 + 4 段階

1. **量子伝送**: Alice → Bob (光子の偏光で bit 送信)
2. **基底公開** (classical): 一致した bit のみ残す (= **sifting**)
3. **エラー訂正** (classical): Cascade or LDPC で残りのエラー修正
4. **秘匿増幅** (privacy amplification): Universal hash で Eve 情報を消去

最終 secret key rate:

$$r = (1 - 2 h(Q)) \cdot \text{sift fraction} \cdot \text{transmittance}$$

ここで:
- $Q$: quantum bit error rate (QBER)
- $h(Q) = -Q \log_2 Q - (1-Q)\log_2(1-Q)$
- transmittance $\eta = 10^{-\alpha L/10}$ ($\alpha = 0.2$ dB/km in fiber)

### 2.2 photon loss と距離限界

| 距離 L | transmittance $\eta$ | secret key rate (bits/pulse) |
|---|---|---|
| 10 km | 0.63 | $\sim 0.3$ |
| 50 km | 0.1 | $\sim 0.05$ |
| 100 km | 0.01 | $\sim 0.005$ |
| 200 km | $10^{-4}$ | $\sim 5 \times 10^{-5}$ |
| 500 km | $10^{-10}$ | $\sim 5 \times 10^{-11}$ (実用不可) |

→ **ファイバ QKD は 200 km 程度が実用限界**。それ以上は trusted relay or 衛星 (free-space) が必要。

---

## 3. Decoy state protocol (Hwang 2003)

BB84 の弱点: **photon-number-splitting (PNS) attack**。Eve は多光子パルスから 1 photon を抜き取り Alice/Bob には気づかれない。

**Decoy state** 解決策:
- Alice は 3 種類の強度を mix: signal ($\mu \sim 0.5$), decoy ($\nu \sim 0.1$), vacuum ($\sim 0$)
- どの photon が signal/decoy/vacuum かを後で公開
- → Eve の PNS attack が**検出可能**

これにより:
- 距離限界が **2× 改善** ($\sim 400$ km)
- secret key rate が大幅向上

---

## 4. E91 (Ekert 1991)

エンタングルメントベースの QKD:

```
Alice ─── Bell pair ─── Bob
            │
            EPR source
```

- Bell 対をシェア
- 各々独立に偏光測定
- CHSH inequality の violation で**device-independent security** 確認

利点:
- **Source-side attack 耐性** (Alice/Bob のデバイスが不完全でも安全)
- 量子テレポーテーションとの統合

---

## 5. ITU 由来の改善案: QECC-enhanced QKD

### 5.1 中心仮説

> **各光子に小規模 QECC を埋め込めば、photon loss を訂正しつつ Eve を検出可能**

具体的に: 1 logical qubit を $[[5,1,3]]$ code (Phase 43!) で 5 物理 photon に encode。

利点:
- 1-photon loss → code が訂正
- 強い Eve 攻撃 → syndrome 異常を生成
- 距離限界が**さらに 2× 改善** (理論)

欠点:
- 光源/検出器の複雑化
- 帯域効率の低下 (5× 光子で 1 qubit)
- 同期と timing の難しさ

### 5.2 ITU 流の解釈

Phase 5: bulk locality = QECC
Phase 51: 暗号 = QECC dual (adversary protection)
**Phase 52**: **QKD-as-QECC = 直接利用**

ITU axiom $\delta S = \delta\langle K\rangle$ から:
- Alice/Bob 系の $K_A$ 固有空間が code subspace
- Eve の measurement = noise の dual
- QECC が両方向 (noise + Eve) に効く

---

## 6. 数値検証計画

### Part A: BB84 secret key rate vs 距離
- 標準 BB84 シミュレーション
- 0 - 500 km で key rate プロット
- 200 km 距離限界の確認

### Part B: Decoy state 比較
- BB84 vs BB84 + decoy
- distance 限界の改善

### Part C: ITU enhanced (QECC + QKD) 概念検証
- [[5,1,3]] code + photon transmission の toy simulation
- 距離限界の改善見積もり

### Part D: QKD network scaling
- Trusted relay node の必要数
- 大陸間 QKD のコスト概算

---

## 7. 実用 QKD の現状 (2026)

| 国 | プロジェクト | 規模 |
|---|---|---|
| 中国 | Micius 衛星 + 北京-上海 QKD 網 | 2000+ km, 衛星 |
| 欧州 | EuroQCI | 計画中 |
| 米国 | DARPA + 各社 | 商用 R&D |
| 日本 | NICT Tokyo network | 100+ km |

**実用化の課題**:
1. 距離限界 (現状 ~200 km / 衛星)
2. 鍵生成 rate (低い、~Mbps)
3. コスト (高い、~$100K/node)
4. 信頼可能 relay の必要性

ITU enhanced QKD が課題 1-2 を改善できれば、社会的インパクト大。

---

## 8. 限界

⚠️ 本 Phase で扱わない:
- 完全な device-independent QKD 解析
- continuous-variable QKD
- measurement-device-independent QKD
- 詳細な PNS attack 解析

✅ 確立する:
- BB84 distance scaling の数値再現
- decoy state の改善効果
- ITU enhanced QKD の概念実証

---

## 9. Phase 53 への展望

Phase 53 では post-quantum lattice-based 暗号 (Kyber, Dilithium) を ITU から解析。
QKD (Phase 52) と PQC (Phase 53) の組合せが ASI 時代の暗号 landscape を定義する。
