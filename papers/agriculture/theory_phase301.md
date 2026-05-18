# Phase 301: 作物 + Green Revolution + Borlaug + ハイブリッド ― K_agri_crops ★★

Phase 300 で K_agri 枠組みを確立。Phase 301 では **作物育種 + Green Revolution + Borlaug + ハイブリッド** を扱い、**K_agri_crops** を ITU の "作物 K-state" として定式化します。

## 古典育種

### Mendel (1865) ★

```
Gregor Mendel (1822-1884):
↓ Brno (Czech) monastery
↓ Pea experiments 1856-1863
↓ 28,000 plants
↓ 1865 "Versuche über Pflanzenhybriden":
  Mendel's 2 Laws
  ★ Foundation of genetics (Phase 217)
↓
1900 Mendel rediscovered (de Vries, Correns, Tschermak)
```

### Hybrid corn (1920s-) ★

```
1908 George Shull (Cold Spring Harbor):
  Hybrid vigor (heterosis)
↓
1933 hybrid corn 1% of US acreage
1965 95% hybrid (US)
↓
Yield doubling 1933-2024:
  1930: 30 bu/acre
  1960: 60 bu/acre
  2024: 180 bu/acre (★ 6x in 90 yr)
```

## Green Revolution ― 詳細 (Phase 300 拡張)

### Borlaug Mexico (1944-1963)

```
1944 Borlaug arrives Mexico (CIMMYT predecessor)
↓ Stem rust resistance breeding
↓ Sonora 64, Lerma Rojo (semi-dwarf)
↓ Mexico self-sufficient in wheat 1956
↓
1962 Pakistan + India intro
1965-67 famine averted
1970 Borlaug Nobel Peace ★
```

### IRRI Rice (Philippines)

```
1960 IRRI 設立 (Philippines):
↓ International Rice Research Institute
↓ IR8 "Miracle Rice" (1966):
  Semi-dwarf, high tillering
  Yield 5-10x traditional varieties
↓
1970s-1980s: India + Indonesia + Philippines self-sufficient
2024: IRRI 200+ rice varieties released
```

### Asia Wheat + Rice (1960-1990)

```
India:
  1965 wheat: 12.3 Mt
  1990: 49.9 Mt (4x)
  2024: 110 Mt (#1 world by tonnage some years)
↓
China:
  1960 grain: 195 Mt
  2024: 700 Mt (cereal)
↓
Population fed:
  Asia: ~3B fed via Green Revolution
  ★ Famine essentially eliminated in non-conflict Asia
```

## Green Revolution 批判

### Environmental + Social Issues

```
Pesticides:
  US 1945: 4M kg
  US 1980: 350M kg
  ↓ DDT, Atrazine, Glyphosate (Roundup)
↓
Water depletion:
  India Punjab groundwater -1 m/yr
  Ogallala Aquifer (US): 30% depleted
↓
Biodiversity:
  ★ Monoculture (only ~12 crops feed humanity)
  Heirloom varieties lost (FAO 1996: 75% loss)
↓
Vandana Shiva (1990s-):
  Critique: ★ corporate seed control
  Bhopal disaster (Union Carbide 1984, India)
```

## 主要作物 (2024)

### Top 10 by tonnage

```
1. Maize (corn):  1.2 Gt
2. Wheat:         800 Mt
3. Rice:          520 Mt
4. Sugarcane:     1.9 Gt (sugar 175 Mt)
5. Potato:        375 Mt
6. Soybean:       400 Mt
7. Cassava:       330 Mt
8. Sweet potato:  90 Mt
9. Sorghum:       60 Mt
10. Yam:          70 Mt
```

### Productivity (yield t/ha)

```
US corn:    11 t/ha
EU wheat:   5.5 t/ha
China rice: 7.0 t/ha
↓
Tropical Africa cereal:
  1-1.5 t/ha (大半 ★ "yield gap")
↓
Yield gap = K-state inefficiency
  Africa potential 5-10 t/ha (if irrigated + fertilized)
```

## CIMMYT + CGIAR 国際センター

```
1960 IRRI (rice)
1966 CIMMYT (wheat + corn, Mexico)
1967 IITA (Africa crops, Nigeria)
1969 ICRISAT (semi-arid, India)
1973 IFPRI (food policy, Washington)
... 15 CGIAR centers total
↓
Annual budget: $1B+ (CGIAR System 2024)
Public goods research
```

## Heirloom + Seed Vaults

```
Norway Svalbard Global Seed Vault (2008-):
  ★ "Doomsday Vault"
  Permafrost storage
  1.2M+ seed samples (2024)
↓
2015 Syria withdraw (Aleppo ICARDA destroyed)
↓
Slow Food (Carlo Petrini 1986):
  Ark of Taste catalogue
  Heirloom seed preservation
```

## 2024 課題

```
World food prices:
  FAO Food Price Index 2024 100 (vs 2014-2016 = 100)
  Above 2020 levels (post-COVID + Ukraine)
↓
Russia-Ukraine impact:
  Combined 30% wheat exports (pre-war)
  Black Sea grain deal 2022-2023 (suspended)
  2024 fragile food security
↓
Climate:
  2023-2024 El Niño
  Brazil drought (coffee)
  India heat (rice export restrictions)
  ★ Volatility ↑
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Mendel** | **1865 (Brno)** ✓ |
| **Shull hybrid corn** | **1908** ✓ |
| **US corn yield growth** | **30 → 180 bu/acre (6x)** ✓ |
| **Borlaug Nobel** | **1970 Peace** ✓ |
| **IR8 Miracle Rice** | **1966 IRRI** ✓ |
| **India wheat 1965-1990** | **12.3 → 49.9 Mt (4x)** ✓ |
| **Heirloom 75% loss** | **FAO 1996** ✓ |
| **Top crop maize** | **1.2 Gt (2024)** ✓ |
| **Svalbard Vault** | **2008 (1.2M samples)** ✓ |
| **Russia-Ukraine wheat** | **30% exports pre-war** ✓ |
| ITU axiom: 作物 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_agri_crops

```
K_agri_crops^(0) = -log P(yield | genotype × environment × management)

Green Revolution = K-state yield phase transition:
  Traditional varieties (K_low) → semi-dwarf hybrid (K_high)
  ★ 4-10x yield in 1 decade
↓
Hybrid vigor (heterosis) = K-state genetic combination:
  F1 heterozygous > inbred parents
↓
Yield gap = K-state global asymmetry:
  Africa K_yield << Asia/America potential
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **CRISPR crops 5+ commercial** | 2028 | 0.85 |
| **Africa yield 2x (smallholder)** | 2030 | 0.65 |
| **Russia-Ukraine grain stable** | 2027 | 0.65 |
| **Heirloom revival 1M+ active users** | 2030 | 0.55 |
| **Climate-adapted varieties 50%+** | 2030 | 0.75 |

---

📄 **論文 (Tier 1 #41, ★ Block D 3/5 ★)**: 10.5281/zenodo.20265556

> Phase 302 で 畜産 + 代替タンパク へ進みます。

#情報理論的統一理論 #ITU #農業 #Mendel #GreenRevolution #Borlaug #Nobel1970 #IRRI #CIMMYT #Svalbard #K_agri_crops #Phase301
