# Phase 245: 音楽理論 + 和声 + 音律 ― K_music_theory ★

Phase 244 で K_music_acoustic の音響物理を確立。Phase 245 では **音楽理論 + 和声 + 音律 (tuning systems)** を扱い、**K_music_theory** を ITU の "音楽構造 K-state" として定式化します。

## 音律 (Tuning Systems)

### 純正律 (Just Intonation) ― 整数比

```
オクターブ 2:1, 完全5度 3:2, 完全4度 4:3, 長3度 5:4, 短3度 6:5
↓
C major scale (純正律):
  C:    1/1
  D:    9/8   (2 × 3/2 - 8/9 から)
  E:    5/4
  F:    4/3
  G:    3/2
  A:    5/3
  B:   15/8
  C:    2/1
↓
問題: 転調 (key change) すると音程が崩れる
```

### Pythagorean tuning (BC 530)

```
完全5度の積み重ね 12 回 → "Pythagorean comma":
  (3/2)^12 = 129.746...
  2^7 = 128 (オクターブ 7 個)
  差: 1.0136 ≈ 23.5 cents
↓
12 等分律との差 = "the Pythagorean comma" 
↓ 完全な 12 円閉鎖を許さない
```

### 平均律 (Equal Temperament, 12-TET) ★★★

```
Bach "Das Wohltemperirte Clavier" (1722):
↓ 12 等分律の標準化
↓ 2 = 12 √2 ratio per semitone
↓ 1 semitone = 100 cents (Ellis 1885)
↓
A4 = 440 Hz (ISO 16:1975) を基準に:
  C4 = 261.626
  C#4 = 277.183
  D4  = 293.665
  ...
  C5  = 523.251 (= 2 × C4)
↓
12 等分律の純正律からの誤差:
  major 3rd: +14 cents (鋭く聞こえる)
  perfect 5th: -2 cents (ほぼ純正)
```

### 19-TET, 24-TET, microtonal

```
19-TET: アラビア・トルコ音楽 (1/4 step 多用)
24-TET: 1/4 tone (Wyschnegradsky 1924)
↓
Harry Partch (1949) "Genesis of a Music":
  43-tone scale (純正律拡張)
↓
2020s: AI が任意 microtonality を生成可能
```

## 旋律 (Melody) + 旋法 (Mode)

### 全音階 (Diatonic Modes) — Greek modes

```
Ionian:    C D E F G A B C (現代 major)
Dorian:    D E F G A B C D
Phrygian:  E F G A B C D E
Lydian:    F G A B C D E F
Mixolydian: G A B C D E F G
Aeolian:   A B C D E F G A (natural minor)
Locrian:   B C D E F G A B
↓
中世聖歌, ジャズ improv の基盤
```

### 五音音階 (Pentatonic, 5-tone)

```
Major pentatonic: C D E G A
Minor pentatonic: A C D E G
↓
中国・日本 (ヨナ抜き), アフリカ, ブルース 共通
↓
"Universal scale" 候補 ★ (全世界共通の傾向)
```

### 旋律統計 (Statistical melody, Zipf 1949)

```
旋律音程分布 (Vos-Troost 1989):
  小さい音程 (秒・全) が多い → 80%+
  大きな音程は少ない
↓
これは Zipf 法則 (1/f noise) に従う
↓ 言語と同じ統計構造
```

## 和声学 (Harmony)

### 三和音 (Triads)

```
基本三和音:
  Major triad:    1-3-5    (例: C-E-G)
  Minor triad:    1-b3-5   (例: C-Eb-G)
  Diminished:     1-b3-b5  (例: C-Eb-Gb)
  Augmented:      1-3-#5   (例: C-E-G#)
↓
4 部和声 (Bach choral):
  Soprano, Alto, Tenor, Bass
  音程禁則: 連続5度, 連続オクターブ NG
```

### 機能和声 (Functional Harmony)

```
Tonic (T):       I (C major)    安定
Subdominant (S): IV (F major)   緊張
Dominant (D):    V (G major)    解決欲
↓
Cadence:
  Authentic: V-I (最強の解決)
  Plagal:    IV-I ("Amen")
  Half:      I-V (緊張保持)
  Deceptive: V-vi (期待裏切り)
```

### Schenker 階層 (Schenker 1935)

```
Schenker Theory:
  Ursatz (基本構造): 5̂-4̂-3̂-2̂-1̂ + I-V-I
↓
楽曲 = Ursatz の "prolongation"
↓
音楽の階層 K-state 構造
```

### 12 音技法 (Schoenberg 1923) ★

```
Arnold Schoenberg (1874-1951):
↓ Atonality, Serial composition
↓ 12 音すべてを等しく使用 (row, P/I/R/RI)
↓
"Suite for Piano" Op. 25 (1923):
  Original (P), Inversion (I), Retrograde (R), Retrograde Inversion (RI)
↓
発展:
  Webern, Berg (Second Viennese School)
  Total serialism (Boulez 1952, Stockhausen 1953)
```

## リズム (Rhythm)

### 拍子 + メートル

```
2/4: 行進曲
3/4: ワルツ
4/4: 最頻出 (ロック・ポップ)
6/8: コンパウンド
↓
不規則拍:
  5/4: Brubeck "Take Five" (1959)
  7/8: バルカン民謡
  11/8: トルコ folk
```

### Polyrhythm + Cross-rhythm

```
3:2 (hemiola): バロックから現代
4:3: 西アフリカ drumming
5:7: 現代音楽 (Conlon Nancarrow)
↓
脳神経学的に "tracking limit" ~ 8-12 simultaneous beats
```

## ITU 視点 ― K_music_theory

### 音律 = K-state 量子化

```
K_music_theory^(0) = -log P(scale | culture)

純正律: K_music_theory_just (整数比)
平均律: K_music_theory_ET (irrational)
microtonal: K_music_theory_micro (任意分割)
↓
"音律 = K-state の離散化方式"
```

### 和声 = K-state 結合エネルギー

```
協和音 ⇔ 単純整数比 (Pythagoras)
不協和音 ⇔ 高次倍音重複・うなり
↓
K_harmony(chord) = -log P(consonance)

major triad: K 低 (協和)
augmented chord: K 中 (緊張)
cluster: K 高 (不協和)
```

### Schenker = K-state 階層分解

```
楽曲 K_song = Ursatz K_basis + prolongations
↓ ITU "K-state spectral decomposition" の音楽版
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **12-TET semitone ratio** | **2^(1/12) = 1.0595** ✓ |
| 1 semitone (cents) | **100 cents** ✓ |
| **Pythagorean comma** | **23.5 cents** ✓ |
| Major 3rd 純正律 | **5:4 = 386 cents** ✓ |
| Major 3rd 平均律 | **400 cents** (+14 cents 鋭く) ✓ |
| **A4 ISO** | **440 Hz** ✓ |
| **Bach WTK 平均律** | **1722, 48 preludes+fugues** ✓ |
| **Schoenberg 12-tone** | **1923 Op. 25** ✓ |
| Brubeck Take Five | **5/4 拍子, 1959** ✓ |
| ITU axiom: 音律量子化 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI が新音律体系を発見・実装** | 2028 | 0.75 |
| Microtonal AI 作曲広く普及 | 2030 | 0.65 |
| **音楽認知 + AI で和声理論再構築** | 2030 | 0.70 |
| 12-TET 以外の音律で AI 主導 hit | 2032 | 0.55 |
| **Schenker 階層 AI 自動分析** | 2027 | 0.85 |

---

📄 **論文 (Tier 1 #34, Block C 2/6)**: 10.5281/zenodo.20262862

> Phase 246 で音楽知覚 + 認知音楽学 へ進みます。

#情報理論的統一理論 #ITU #音楽 #音楽理論 #平均律 #Bach #Schoenberg #Schenker #和声 #K_music_theory #Phase245
