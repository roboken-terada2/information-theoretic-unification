# Phase 247: 作曲 + 即興 + アルゴリズム作曲 ― K_music_composition ★

Phase 246 で K_music_perception の聴覚・神経基盤を確立。Phase 247 では **作曲 (Composition) + 即興 (Improvisation) + アルゴリズム作曲 (Algorithmic Composition)** を扱い、**K_music_composition** を ITU の "創造性 K-state" として定式化します。

## 作曲史 (西洋音楽史 + 世界音楽)

### バロック (1600-1750) ★

```
Monteverdi (1567-1643): オペラ誕生 (1607 "Orfeo")
Vivaldi (1678-1741): 協奏曲 ("Four Seasons" 1725)
Bach (1685-1750): ★
  - "Brandenburg Concertos" (1721)
  - "WTK Books I/II" (1722/1742) — 平均律確立
  - "Mass in B minor", "St Matthew Passion"
  ↓ Fugue: 対位法の頂点 (BWV 1080 Art of Fugue 1751)
Handel (1685-1759): "Messiah" (1741)
```

### 古典派 (1750-1820)

```
Haydn (1732-1809): 交響曲 ~104, 弦楽四重奏 ~68
Mozart (1756-1791): 626 作品, "Requiem" K.626 (1791)
Beethoven (1770-1827): ★
  - 交響曲 9 (1812: "9th Symphony Ode to Joy")
  - ピアノソナタ 32 (op.111 1822, 革新的)
  - 弦楽四重奏 op.131-135 (transcend tonality)
```

### ロマン派 (1820-1910)

```
Schubert (1797-1828): Lieder 600+, "Winterreise" (1827)
Chopin (1810-1849): ピアノ独自言語
Wagner (1813-1883): "Tristan und Isolde" (1859)
  ↓ Tristan chord = 機能和声を破壊
  ↓ Atonality への扉
Mahler (1860-1911): 交響曲 9, 巨大化
Debussy (1862-1918): 全音音階, 印象主義
```

### 20 世紀 → 21 世紀 ★

```
Stravinsky (1882-1971): "Le Sacre du Printemps" (1913)
  ↓ Polyrhythm + Polytonality, スキャンダル
Schoenberg (1874-1951): 12 音技法 (1923)
Bartók (1881-1945): 民俗 + 数理
Cage (1912-1992): "4'33"" (1952) ★ 沈黙
Reich (1936-): ミニマル (1965-)
Ligeti (1923-2006): "Atmosphères" (1961)
↓
2020s:
  AI 作曲 + マッシュアップ
  Hyperpop, AI vocaloid
```

## 即興 (Improvisation)

### ジャズ即興

```
ジャズ史 (1900-2024):
  Ragtime (1900s): Joplin
  Dixieland (1910s): NOLA
  Swing (1930s): Goodman, Ellington
  Bebop (1940s): Parker, Gillespie
  Cool (1950s): Davis "Birth of the Cool"
  Modal (1959): Davis "Kind of Blue"
  Free (1960s): Coleman, Coltrane
  Fusion (1970s): Davis "Bitches Brew"
↓
Bebop 即興:
  Chord changes に対し scale 即興
  ii-V-I 進行 (most common)
  Bird (Parker) - "Ko-Ko" 1945
```

### Charlie Parker の音符密度

```
Parker "Ko-Ko" (1945):
  300 bpm (very fast)
  16 分音符でほぼ連続
  ↓ 75 notes/秒 (脳神経処理限界近接)
↓
これは認知音楽学的に "near-maximum K-state flux"
```

### ヒンドゥスターニー古典即興

```
Raga + Tala system:
  Raga: 旋律・音階・装飾の体系 (200+ recognized)
  Tala: リズム周期 (3-128 拍)
↓
Ravi Shankar (1920-2012): sitar
↓
即興 = Alap (拍子なし) → Jor → Jhala (急速)
1-3 hour 持続即興 標準
```

## アルゴリズム作曲 ― 1957 から AI まで

### Pre-computer

```
Mozart "Musikalisches Würfelspiel" (1787):
  サイコロで小節 random combination
↓
Hiller-Isaacson "Illiac Suite" (1957) ★ 史上初コンピュータ作曲:
  ILLIAC I で生成
  Cantus firmus + counterpoint
```

### Algorithmic composition の進化

```
1958 Xenakis "Achorripsis" — stochastic / Poisson
1965 Boulez "Structures" — total serialism algorithmic
1970s Markov chains (Conway, Cohen)
1980s L-systems (Prusinkiewicz)
1990s Generative grammar (Lerdahl-Jackendoff)
2000s Cellular automata
2010s Neural networks
```

### Lerdahl-Jackendoff GTTM (1983)

```
"A Generative Theory of Tonal Music" (1983):
↓ Chomsky 統語論 + Schenker 階層を結合
↓ 音楽 = 木構造 (tree)
↓
4 階層:
  Grouping structure
  Metrical structure
  Time-span reduction
  Prolongational reduction
```

### Music21 + DeepBach (2017)

```
MIT Music21 toolkit (Cuthbert 2010):
  Python 音楽解析
↓
DeepBach (Hadjeres 2017 ICML):
  Bach choral 風 4 部和声を生成
  Sony CSL Lab
↓ Bach style 区別困難 (Turing test partial pass)
```

## ITU 視点 ― K_music_composition

### 作曲 = K-state path 最適化

```
K_composition^(0) = -log P(piece | constraints)

作曲過程:
  形式の選択 (sonata, fugue, song, ...)
  ↓ K_form (固定 prior)
  和声進行決定
  ↓ K_chord (機能和声 prior + creativity)
  旋律生成
  ↓ K_melody (motivic coherence + surprise)
↓
創造性 = 制約 (K_prior) + 違反 (K_surprise) のバランス
```

### 即興 = real-time K-state navigation

```
リアルタイム作曲:
  T = 100-300 ms decision window
  Chord change 1-2 secパスト
↓
ジャズ熟練度 = Δ K_chord prediction accuracy
↓ Bird = "K-state surfer"
```

### GTTM = K-state 階層分解

```
Lerdahl-Jackendoff = ITU 音楽版:
  楽曲 = 階層的 K-state decomposition
  Tonal hierarchy: I > V > IV > vi > ... (Krumhansl probe-tone)
↓
ITU axiom: δS_listening = δ⟨K_GTTM⟩
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Bach BWV** | **~1,128 cataloged** ✓ |
| Beethoven 交響曲 | **9** ✓ |
| Mozart 全作品 | **626** (Köchel) ✓ |
| Cage "4'33""** | **1952** ✓ |
| **史上初コンピュータ作曲** | **Hiller-Isaacson 1957 Illiac Suite** ✓ |
| **GTTM (Lerdahl-Jackendoff)** | **1983** ✓ |
| **DeepBach Turing partial pass** | **2017 ICML** ✓ |
| Parker "Ko-Ko" 速度 | **300 bpm** ✓ |
| Indian raga 認識数 | **200+** ✓ |
| ITU axiom: 作曲 K-state | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 即興演奏 (jazz) プロ並** | 2028 | 0.85 |
| **GTTM 自動解析全作品** | 2027 | 0.85 |
| 演奏家 K-state リアルタイム測定 | 2030 | 0.65 |
| **新作曲技法 AI 発見** | 2030 | 0.70 |
| Cage 哲学 + AI 統合 | 2032 | 0.55 |

---

📄 **論文 (Tier 1 #34, Block C 2/6)**: 10.5281/zenodo.20262862

> Phase 248 で AI 作曲 (Suno/Udio/MusicGen) へ進みます。

#情報理論的統一理論 #ITU #音楽 #作曲 #即興 #Bach #Beethoven #Mozart #Cage #Bird #Lerdahl #DeepBach #K_music_composition #Phase247
