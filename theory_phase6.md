# Phase 6: Page 曲線 — ブラックホール情報問題の量子情報理論的解決

## 1. 問題

Hawking 1976：ブラックホール (BH) は熱輻射する。輻射が放出されるにつれて BH は蒸発するが、輻射のエントロピーは単調増加する → 最終状態は混合状態 → **ユニタリ性違反**。

これは GR と QM の最も鋭い矛盾。Phase 1-5 で構築した情報理論的枠組みでこれが解決できるか。

## 2. Page の予言 (1993)

ユニタリ進化が成立するなら、輻射のフォン・ノイマンエントロピーは:
- 蒸発初期：輻射量子数 $|R| \ll |B|$ → $S_R \approx |R| \log 2$ (熱的)
- **Page 時間 $t_P$** ($|R| \approx |B|$): $S_R$ がピーク
- 後期：$|R| \gg |B|$ → $S_R \approx |B| \log 2$ (BH側のエントロピー、減少)
- 最終：BH 完全蒸発 → $S_R = 0$ (純粋に戻る)

この**逆 V 字**が **Page 曲線**。Hawking の単調増加曲線 vs Page の V 字 — 何が正しいか?

## 3. 島公式 (2019-2020)

Penington 2019, Almheiri-Engelhardt-Marolf-Maxfield 2020 (AEMM)：
$$S_R = \min_{\text{islands } I}\!\left[ \frac{\text{Area}(\partial I)}{4 G_N} + S_{\text{matter}}(R \cup I)\right]$$

Page 時間以前は island = 空集合 → $S_R = $ matter entropy of $R$ (Hawking の答え, 増加)。
Page 時間以後は island = BH 内部を一部含む集合 → 競合する candidate が勝つ → $S_R$ が減少。

これは Phase 2 の **Ryu-Takayanagi 公式の量子拡張**であり、Phase 1-5 の枠組みの直接的帰結。

## 4. 数値モデル — Hayden-Preskill 風

完全蒸発 BH をモデル化するのに、ランダムユニタリ + Bell ペアモデルを使う。

**設定**:
1. 全系 = $|B|$ 量子ビット (BH 内部) + $|R|$ 量子ビット (輻射)。
2. 初期状態 = (BH と参照 Bell ペアでまずエンタングル) → 全 BH 量子ビット を Haar ランダムユニタリで進化 → 一部の量子ビット を「輻射」として外部に放出。
3. 各「時刻」(= 放出された量子ビット数) で $S_R$ を計算。

**Page の主張 (1993)**：高次元 Haar 乱数集合で平均すると
$$\langle S_R \rangle \approx \min(|R|, |B|+|N|-|R|) \log 2$$
ここで $|N|$ は最初に BH と参照を結ぶ Bell ペア数 (ニュートラル設定では $|N|=0$)。

これがちょうど **三角の Page 曲線** で、Hawking 曲線 (単調増加) との違いがユニタリ性の数値的証拠。

## 5. 実装方針

1. 全系 $n_{\text{tot}} = 2k$ 量子ビット (例 12)、Haar ランダム純粋状態 $|\psi\rangle$ を生成
2. 各分割 $|R| = 1, 2, ..., n_{\text{tot}}-1$ で reduced state $\rho_R$ を計算、$S_R$ を測る
3. 多数の Haar 乱数集団で平均
4. **平均曲線**を Page 曲線と Hawking 曲線でフィット
5. 結果：Page 曲線が成立 → 情報は失われない

オプション：少量の qubit を「内部 BH」として保持しつつ、Bell ペアで参照と結ぶことで、より物理的な「蒸発する BH」設定を模擬。

## 6. 情報理論的統一理論内での意義

Phase 5 で示した「バルク = 境界 QECC」という観点から、ブラックホール内部はホログラフィックに境界で復号可能。
Page 時間以前：BH 内部は輻射の wedge に入っていない
Page 時間以後：相転移により BH 内部が輻射の wedge に入る → 情報回収

これは Phase 1-5 で構築した枠組みの**動的応用**であり、ブラックホール情報問題は QECC の RT 相転移として解ける。
