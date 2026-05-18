# Phase 244: 音楽・芸術開幕 ― K_music + 音響物理 (Block C 2/6) ★★

Phase 243 で Tier 1 #33 Linguistics が完成し、Block C 社会・人文・芸術が開幕しました。Phase 244 から **Tier 1 #34 Music & Arts** に進み、**K_music + K_arts** を ITU framework で再解釈します。本 phase では音響物理学の基礎から開幕。

## 音楽 = 数学・物理学・認知科学の交差点

### Pythagoras 革命 (c. BC 530) ★★★

```
Pythagoras (c. BC 580-500):
↓ 弦楽器実験: 弦長比 2:1 = オクターブ, 3:2 = 完全5度, 4:3 = 完全4度
↓ "万物は数" (Πάντα κατ' ἀριθμόν)
↓ 音楽 = 整数比 ratio
↓
これが西洋音楽理論の起源
そして整数論・物理学の出発点
```

### 4 大革命 (西洋音楽史)

```
1. Pythagoras 純正律 (BC 530)         整数比基盤
2. Bach 平均律 (1722)                 12 等分音律 ★
3. Schoenberg 12 音技法 (1923)         無調 → 系列音楽
4. AI 作曲 (2018-2024)                Suno / MusicGen / Stable Audio
```

## 音響物理学 (Acoustics)

### 音 = 空気振動波

```
音速 (20°C, 1 atm): c = 343 m/s
↓
波長 λ = c / f
  A4 (440 Hz): λ = 0.78 m
  Middle C (261.6 Hz): λ = 1.31 m
  20 Hz (低域限界): λ = 17.15 m
  20 kHz (高域限界): λ = 1.7 cm
↓
人間可聴域: 20 Hz - 20 kHz (約 10 オクターブ)
```

### 倍音列 (Harmonic Series, Fourier 1822) ★

```
基音 f0 = 261.6 Hz (Middle C):
f1 (1st):  261.6 Hz  ← C (基音)
f2 (2nd):  523.3 Hz  ← C (オクターブ上)
f3 (3rd):  784.9 Hz  ← G (完全5度上)
f4 (4th): 1046.5 Hz  ← C
f5 (5th): 1308.1 Hz  ← E (長3度上)
f6 (6th): 1569.7 Hz  ← G
f7 (7th): 1830.3 Hz  ← Bb (7度, 純正)
f8 (8th): 2093.0 Hz  ← C
...
↓
Fourier 級数:
  f(t) = a0 + Σ [an cos(2πnf₀t) + bn sin(2πnf₀t)]
↓
楽器音色 = 倍音成分の比率
  バイオリン: f1-f10+ 豊富
  クラリネット: 奇数倍音優勢 (f1, f3, f5, ...)
  フルート: f1-f3 のみ
```

### 共鳴 (Resonance) + 楽器物理

```
弦楽器 (両端固定):
  f_n = (n/2L) × √(T/μ)
  T = 張力, μ = 線密度
↓
管楽器 (開口端):
  f_n = (n/2L) × c (両端開, 偶倍音含)
  f_n = (2n-1)/4L × c (片端閉, 奇数倍音のみ → クラリネット)
↓
膜・板:
  Chladni patterns (Chladni 1787)
  ティンパニ: 非調和倍音 → 打楽器音色
```

### 音響インピーダンス + Helmholtz 共鳴

```
Z = ρc (空気: 415 kg/(m²s))
↓
楽器の音響インピーダンスマッチング:
  バイオリン body resonance
  ピアノ soundboard
  ホール acoustics
↓
Helmholtz resonator (1860s):
  f = (c/2π) √(A/(V·L))
  ボトル, 楽器のホール, スピーカ低音
```

## 心理音響学 (Psychoacoustics) ★

### 音圧と音量

```
SPL (Sound Pressure Level):
  L = 20 log₁₀ (p / p₀)  [dB]
  p₀ = 20 μPa (聞き取り閾値)
↓
代表値:
  0 dB:    閾値
  60 dB:   会話
  85 dB:   8時間で聴覚障害リスク
  120 dB:  痛覚閾値
  194 dB:  空気変位最大 (理論限界)
↓
Fletcher-Munson 等ラウドネス曲線 (1933):
  3-4 kHz で最も敏感
  低音・高音は鈍感 → "loudness war"
```

### Bark scale (Zwicker 1961) — 臨界帯域

```
24 critical bands:
  0-20 Bark (人間聴覚)
↓
MP3, AAC, Opus の心理音響モデル基盤
  ↓ マスキング (masking) 効果で非可聴音を破棄
  ↓ 50-100x データ圧縮
```

## ITU 視点 ― K_music sub-states

### K_music = 音楽の modular Hamiltonian

```
K_music^(0) = -log P(music | context)

8 軸:
  K_music_acoustic     # 音響物理 (Phase 244)
  K_music_theory       # 理論 (Phase 245)
  K_music_perception   # 知覚 (Phase 246)
  K_music_composition  # 作曲 (Phase 247)
  K_music_AI           # AI 生成 (Phase 248)
  K_music_visual       # 視覚芸術 (Phase 249)
  K_music_AI_art       # AI アート (Phase 250)
  K_music_culture      # 文化比較 (Phase 251)
```

### 倍音 = 自然な K-state 階層

```
基音 f0 → 2f0 → 3f0 → 4f0 ...

K_acoustic 軸:
  整数比 (Pythagoras): 2:1, 3:2, 4:3
  ↓ 単純 ratio → 協和音 (consonance)
  
不協和 (Helmholtz 1862):
  近接周波数 → うなり (beating)
  Hz差 < 15-30 Hz で不快
  ↓ K_acoustic の "高次元 K-state"
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **音速 20°C** | **343 m/s** ✓ |
| **可聴域** | **20 Hz - 20 kHz** ✓ |
| **A4 (チューニング)** | **440 Hz** (ISO 16) ✓ |
| Middle C | **261.6 Hz** ✓ |
| **オクターブ比** | **2:1** (Pythagoras) ✓ |
| 完全5度 | **3:2** ✓ |
| 完全4度 | **4:3** ✓ |
| **Bark scale critical bands** | **24** (Zwicker 1961) ✓ |
| **聞き取り閾値** | **20 μPa = 0 dB SPL** ✓ |
| ITU axiom: 倍音列 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 作曲が人間と区別不能** | 2027 | 0.85 |
| **音響物理 + 神経科学統合** | 2030 | 0.70 |
| BCI 音楽 (silent music) | 2032 | 0.65 |
| **物理学 + 音響工学 完全統合** | 2028 | 0.80 |
| AI 楽器設計革新 | 2027 | 0.80 |

---

📄 **論文 (Tier 1 #34, Block C 2/6)**: 10.5281/zenodo.20262862 (Phase 251 で生成)

> Phase 245 で音楽理論 + 和声 + 音律 へ進みます。

#情報理論的統一理論 #ITU #音楽 #BlockC2of6 #Pythagoras #Fourier #倍音 #K_music_acoustic #Phase244
