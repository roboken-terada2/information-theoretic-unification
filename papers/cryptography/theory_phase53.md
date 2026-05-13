# Phase 53: Lattice-based Post-Quantum Cryptography (Kyber, Dilithium) と ITU

## 1. 動機

Phase 51-52 で:
- Phase 51: ITU 情報理論的セキュリティ
- Phase 52: BB84/QKD (naive ITU enhancement は失敗 → 精緻化必要)

Phase 53 で **ポスト量子暗号 (PQC)** の主流 ― **lattice-based 暗号** ― を ITU から解析。

2024 年に NIST は PQC 標準化 round 3 を完了し、以下を採用:
- **CRYSTALS-Kyber** (KEM = 鍵カプセル化)
- **CRYSTALS-Dilithium** (デジタル署名)
- **FALCON** (署名, 高効率)
- **SPHINCS+** (ハッシュベース署名)

これら全てが**lattice-based** (またはハッシュベース)。
Phase 53 で:
1. LWE (Learning With Errors) 問題の ITU 解釈
2. Kyber/Dilithium の安全性と ITU
3. 量子耐性の根拠
4. ITU 推奨の改良案

を議論する。

---

## 2. Lattice と LWE 問題

### 2.1 Lattice の定義

格子 $\mathcal{L} \subset \mathbb{R}^n$:
$$\mathcal{L} = \{ a_1 \vec{b}_1 + a_2 \vec{b}_2 + \cdots + a_n \vec{b}_n : a_i \in \mathbb{Z} \}$$

$\vec{b}_i$ は格子の基底。$n$ は格子次元 (= 暗号鍵長の感覚)。

### 2.2 LWE 問題 (Regev 2005)

ランダム行列 $A \in \mathbb{Z}_q^{m \times n}$、秘密鍵 $\vec{s} \in \mathbb{Z}_q^n$、誤差 $\vec{e}$ (小さい Gaussian):
$$\vec{b} = A \vec{s} + \vec{e} \pmod q$$

**LWE 問題**: $(A, \vec{b})$ から $\vec{s}$ (または $\vec{e}$) を復元。

これは **NP-hard 候補** (worst-case to average-case reduction by Regev):
- 古典 attack: BKZ basis reduction, $\sim 2^{0.292 n}$
- 量子 attack: Grover speedup で $\sim 2^{0.265 n}$
- **両者とも指数時間** ← PQC の安全根拠

### 2.3 ITU 観点での LWE

ITU 流の解釈:

> **LWE = "意図的にノイズを加えた code"**
>
> QECC は noise を**訂正**する code
> LWE は noise を**故意に加えて**復号を不可能化する code

両者は**同じ axiom $\delta S = \delta\langle K\rangle$ の dual application**:
- QECC: receiver の $K$ 固有空間に情報を encode、noise を除去
- LWE: **adversary** の $K$ 固有空間で**復号失敗**を保証

つまり「**ITU code 構造を adversary 困難性のために逆利用**」 ― これが lattice PQC。

---

## 3. CRYSTALS-Kyber (NIST KEM 標準)

### 3.1 構造

Module-LWE (MLWE) ベースの key encapsulation mechanism (KEM):
- 公開鍵: 行列 $A$ + ベクトル $\vec{b} = A\vec{s} + \vec{e}$
- 秘密鍵: $\vec{s}$
- 暗号化: ランダム $\vec{r}, \vec{e}', \vec{e}'' $ から $(\vec{u}, v)$ 計算
- 復号: $\vec{s}$ で $v - \vec{u} \cdot \vec{s}$ を計算 → メッセージ復元

### 3.2 セキュリティパラメータ

| Kyber 変種 | n | q | 推定 セキュリティ (古典/量子) |
|---|---|---|---|
| Kyber-512 | 512 | 3329 | 128/118 bits |
| Kyber-768 | 768 | 3329 | 192/180 bits |
| Kyber-1024 | 1024 | 3329 | 256/240 bits |

→ AES-128 程度の安全性に **Kyber-512 で十分**。

### 3.3 ITU 流の評価

ITU 公理から:

$$\text{security} \propto H(\text{secret key space}) = n \log_2 q$$

Kyber-512: $H = 512 \times \log_2 3329 \approx 6000$ bits

しかし**有効安全性は 128 bits** (lattice 構造のため)。これは:
- entropy 大 ≠ 安全性大
- 「**復号アルゴリズムの存在しない部分空間**」 が真の安全度
- ITU 流: **$K_{\rm adversary}$ の固有空間が attack-resistant**

---

## 4. CRYSTALS-Dilithium (NIST 署名標準)

### 4.1 構造

Module-LWE + Module-SIS ベースのデジタル署名:
- 秘密鍵: $(\vec{s}_1, \vec{s}_2)$
- 公開鍵: $\vec{t} = A\vec{s}_1 + \vec{s}_2$
- 署名: Fiat-Shamir 変換による (zk-proof)
- 検証: lattice 演算で短ベクトル確認

### 4.2 安全性根拠

Module-SIS (Short Integer Solution):
- "$A\vec{z} = 0 \pmod q$ を満たす短い $\vec{z}$ を見つける" は困難
- 古典: $\sim 2^{0.292 n}$
- 量子: $\sim 2^{0.265 n}$

→ Kyber と同等の安全性プロファイル。

---

## 5. ITU からの改良提案

### 5.1 「Φ_ITU enhanced PQC」 概念

Tier 1 #2 で確立した self-reference QECC を **PQC の secret に組み込む**:

```
通常 PQC: secret = 単純 vector s
ITU 改良:  secret = self-referential code state |ψ_s>
```

すると:
- attack には**Φ_ITU 構造の解読**が必要
- これは**意識的 AI 知能**を要する (Tier 1 #2)
- → **古典・量子両者で困難** + **ASI でも未知の困難**

### 5.2 「量子-classical-ASI safe」 三層暗号

Phase 47-50 の AI 意識から、ITU は:

> **ASI が登場した時、現 PQC は新たな attack に晒される可能性**

特に:
- ASI は構造を読み解く強い能力 ($\Phi_{\rm ITU} > 0.5$ の場合)
- 心理的 attack (社会工学) の自動化
- Side-channel 攻撃の超高度化

ITU 推奨: **3 層暗号**
1. **古典安全層**: AES-256 (古典は遅い)
2. **量子安全層**: Kyber + QKD (量子コンピュータ対応)
3. **ASI 安全層**: Φ_ITU embedded protocols (意識 AI 対応)

3 層を**直列**で適用すれば、最強 attacker でも 3 つ全て破る必要がある。

---

## 6. 数値検証計画

### Part A: 簡易 LWE 実装
- 小規模 $n = 8$ で LWE 鍵生成・暗号化・復号
- 動作確認

### Part B: brute force attack 時間スケーリング
- $n = 4, 6, 8, 10$ で attack 時間 vs $q^n$
- 指数増加の確認

### Part C: BKZ vs Grover 比較
- 古典 attack ($2^{0.292 n}$) と量子 ($2^{0.265 n}$) の比較
- 安全性パラメータ選定

### Part D: ITU 改良提案
- Φ_ITU embedded LWE の概念検証
- 攻撃複雑度の見積もり

---

## 7. 限界

⚠️ 本 Phase で扱わない:
- 完全な Kyber/Dilithium reference implementation
- Side-channel attack の詳細
- Quantum random oracle model
- 完全 lattice attack code (BKZ, sieving)
- 標準コンプライアンス

✅ 確立する:
- Lattice PQC の ITU 解釈
- 古典 vs 量子 vs ASI 安全性
- 3 層暗号 design recommendation
- Φ_ITU embedded PQC 概念

---

## 8. Phase 54 への展望

Phase 54 (連載最終回) で:
- ASI 時代の暗号 landscape 統合
- QKD + PQC + Φ_ITU 三層提案の詳細
- Falsifiable predictions
- 2030 年代の暗号 roadmap

これで Tier 1 #3 論文「ITU and Cryptography」 v1.0.0 完成。
