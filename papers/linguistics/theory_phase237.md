# Phase 237: 音声学 + 音韻論 + 音響 ― K_lang_phonology ★

Phase 236 で K_lang の枠組みを確立。Phase 237 では **音声学 (Phonetics) + 音韻論 (Phonology) + 音響** を扱い、**K_lang_phonology** を ITU の "音声 K-state" として定式化します。

## 音声学 ― IPA + 調音 + 音響

### IPA (International Phonetic Alphabet, 1888-2020) ★

```
1886 IPA 創設 (Association Phonétique Internationale)
↓
2020 IPA chart 改訂:
  Consonants (pulmonic): 59 記号
  Consonants (non-pulmonic): 5 click + 4 implosive + ejective
  Vowels: 28 cardinal + secondary
  Suprasegmental: 韻律, トーン
  Diacritics: 31 補助記号
↓
全人類音素を表記可能 (理論上)
```

### 調音 (Articulation) ★

```
調音器官:
  - 唇 (lips): /p, b, m/
  - 歯 (teeth): /θ, ð/
  - 歯茎 (alveolar): /t, d, n, s/
  - 硬口蓋 (palatal): /j, ç/
  - 軟口蓋 (velar): /k, g, ŋ/
  - 口蓋垂 (uvular): /ʁ, q/
  - 咽頭 (pharyngeal): /ħ, ʕ/
  - 声門 (glottal): /h, ʔ/

調音方法:
  破裂 (stop): /p, t, k, b, d, g/
  摩擦 (fricative): /f, s, ʃ, h/
  破擦 (affricate): /ʧ, ʤ/
  鼻音 (nasal): /m, n, ŋ/
  接近 (approximant): /j, w, l/
  流音 (liquid): /l, r/
```

### 音響音声学 (Acoustic Phonetics)

```
音声 = 空気振動 (0-22 kHz, 聴覚帯域)
↓
スペクトログラム:
  Formants: F1 (口腔), F2 (前後舌位), F3 (唇丸め)
↓
母音 F1-F2 平面 (Peterson-Barney 1952):
  /i/ (英 see):    F1=270, F2=2290 Hz
  /u/ (英 boot):   F1=300, F2=870 Hz
  /a/ (英 father): F1=730, F2=1090 Hz
  ↓ 母音空間 = F1-F2 三角形
```

### 音響特徴の定量化

```
基本周波数 F0 (pitch):
  男性: ~125 Hz
  女性: ~210 Hz
  子供: ~300 Hz

声道長 17 cm (男性):
  共鳴周波数 (closed-open tube):
    F_n = (2n-1) c / (4L)
    F_1 = (1)(343)/(4×0.17) = 504 Hz (中性母音 schwa)
    F_2 = (3)(343)/(4×0.17) = 1513 Hz
    F_3 = (5)(343)/(4×0.17) = 2522 Hz
```

## 音韻論 (Phonology)

### 音素 (Phoneme) ― 機能的単位

```
音素 = 意味を区別する最小単位:
↓
ミニマルペア (minimal pair):
  英: pat /pæt/ vs bat /bæt/ → /p/ vs /b/ が音素
  英: pat /pæt/ vs pad /pæd/ → /t/ vs /d/ が音素
↓
異音 (allophone) = 同じ音素の変異:
  英 /p/ → [pʰ] in "pin", [p] in "spin", [p̚] in "stop"
  ↓ 環境による相補分布
```

### 言語別音素数 (Maddieson 1984, 451 言語)

| 言語 | 音素数 | 子音 | 母音 |
|---|---|---|---|
| **!Xóõ (Khoisan)** | **141** | 122 | 19 |
| Caucasian Ubykh | 84 | 78 | 6 |
| Korean | 40 | 22 | 18 |
| English | 44 | 24 | 20 |
| Japanese | 21 | 16 | 5 |
| Spanish | 24 | 19 | 5 |
| **Rotokas (PNG)** | **11** | **6** | 5 |

```
平均: 31 音素/言語 (Maddieson 1984)
中央値: 22 音素
分布: 11 (Rotokas) ~ 141 (!Xóõ) = 12.8x range
```

### 韻律 (Prosody) ― トーン + ストレス + リズム ★

```
トーン言語 (Tonal):
  Mandarin Chinese: 4 トーン + 軽声
    妈 mā (high) "mother"
    麻 má (rising) "hemp"
    马 mǎ (low) "horse"
    骂 mà (falling) "scold"
  Cantonese: 6 (9) トーン
  Yoruba: 3 トーン
↓
強勢 (Stress) 言語:
  英語: pérmit (n) vs permít (v)
  ロシア語: 強勢が複雑
↓
モーラ (Mora) 言語:
  日本語: 語頭強勢なし
  N (撥音), Q (促音) が独立モーラ
```

## 数値検証 ― Praat 風スペクトル解析

```python
# 母音 5 種 F1-F2 比較 (Hillenbrand 1995)
vowels = {
    'i (beet)':  (390, 2160),
    'I (bit)':   (520, 2000),
    'e (bet)':   (530, 1840),
    'æ (bat)':   (660, 1720),
    'A (father)':(730, 1090),
    'o (boat)':  (570, 840),
    'U (good)':  (440, 1020),
    'u (boot)':  (430, 1170),
}

# 声道共鳴周波数 (uniform tube model)
L = 0.17  # m (vocal tract length, adult male)
c = 343   # m/s (speed of sound)
F_n = lambda n: (2*n-1) * c / (4*L)
# F_1 = 504, F_2 = 1513, F_3 = 2522 Hz (schwa)
```

## ITU 視点 ― K_lang_phonology

### 音韻システム = 離散 K-state 量子化

```
K_lang_phonology^(0) = -log P(phoneme)

調音空間 (連続):
  口腔位置 ∈ [0, 1] (前後)
  口腔開度 ∈ [0, 1] (高低)
  唇形状 ∈ [0, 1] (丸め)
↓
音素 (離散):
  N(言語) 個のクラスター
  N = 11 (Rotokas) ~ 141 (!Xóõ)
↓
言語獲得 = 連続調音空間の離散化 (Werker-Tees 1984)
  6 ヶ月: 全言語の音素を区別
  12 ヶ月: 母語の音素のみに鋭敏化
```

### 音韻 K-state の情報量

```
Shannon entropy per phoneme:
  H = -Σ p_i log p_i

英語 (Bell Labs 1950s):
  音素レベル: H ≈ 4.5 bits/phoneme
  → ~22 distinct phonemes ≈ 4.5 bits
↓
日本語:
  H ≈ 4.4 bits/mora
  → ~21 distinct phonemes
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **IPA pulmonic consonants (2020)** | **59** ✓ |
| 平均音素数 (Maddieson 1984) | **31** ✓ |
| !Xóõ Khoisan 音素数 | **141** ✓ |
| Rotokas PNG 音素数 | **11** ✓ |
| 声道長 (男性) | **17 cm** ✓ |
| F_1 schwa (uniform tube) | **504 Hz** ✓ |
| F0 男性平均 | **125 Hz** ✓ |
| **Werker-Tees 臨界期** | **6-12 ヶ月** ✓ |
| ITU axiom: 音韻離散化 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 音声合成 完全自然** (Turing test通過) | 2027 | 0.90 |
| **危機言語 100+ AI 音声記録** | 2028 | 0.85 |
| 非ヒト動物発話の音韻記述 (鳥, クジラ) | 2030 | 0.65 |
| **音声 BCI (silent speech)** 実用化 | 2032 | 0.70 |
| AI が全言語 IPA 自動転写 | 2027 | 0.80 |

---

📄 **論文 (Tier 1 #33, Block C 1/6 開幕)**: 10.5281/zenodo.20258418

> Phase 238 で Morphology + Syntax + Chomsky へ進みます。

#情報理論的統一理論 #ITU #言語学 #音声学 #音韻論 #IPA #Maddieson #K_lang_phonology #Phase237
