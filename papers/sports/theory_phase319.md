# Phase 319: 栄養 + スポーツ科学 + 補給 ― K_sports_nutrition ★

Phase 318 で K_sports_training を確立。Phase 319 では **スポーツ栄養 + supplements + 補給** を扱い、**K_sports_nutrition** を ITU の "栄養 K-state" として定式化します。

## マクロ栄養素 (Macronutrients)

### Carbohydrate

```
Endurance athlete:
  8-10 g/kg body weight/day (heavy training)
  Glycogen stores: 500g muscle + 100g liver
↓
Marathon: 60-90 g/hr carb during race
  ★ Bonking = glycogen depletion (mile 20)
↓
Carb loading (1967 Saltin):
  ★ 7-10 day protocol (depletion + super-compensation)
  Modern: 36-48 hr high-carb pre-race
```

### Protein

```
Strength athletes:
  ★ 1.6-2.2 g/kg/day
↓
Endurance: 1.2-1.6 g/kg
Sedentary: 0.8 g/kg (RDA)
↓
Distribution:
  20-40 g/meal × 4-5 meals
  Whey faster, casein slower
```

### Fat

```
20-30% energy
Omega-3 (EPA + DHA):
  Anti-inflammatory
  Fish, algae sources
↓
Saturated fat: <10%
Trans fat: avoid
```

## Hydration ★

```
Sweat rates:
  Marathon Kipchoge ~ 2 L/hr (high)
  Average athlete ~ 1 L/hr
↓
Sodium loss:
  ~ 1 g/L sweat
↓
Hyponatremia:
  Over-hydration with water only
  ★ Marathon deaths (Cynthia Lucero 2002)
↓
2024 guidelines (Asker Jeukendrup):
  Drink to thirst
  Sodium 300-700 mg/L sports drink
```

## Sports Drinks + Gels

```
Gatorade (1965):
  ★ Univ of Florida (Robert Cade)
  Florida Gators → "Gatorade"
↓
PepsiCo acquired 2001 ($1.4B)
2024 revenue: $7B+ (sports drinks market)
↓
2024 alternatives:
  Liquid IV (Unilever 2020)
  Tailwind (endurance)
  Maurten (gel, Kipchoge sponsor)
```

## Performance Enhancers (Legal)

### Caffeine

```
Most studied ergogenic aid:
  3-6 mg/kg pre-event
  ★ +3-5% performance (endurance)
↓
2004 WADA removed from prohibited list
↓
2024 standard practice
```

### Beetroot (NO3-)

```
Nitric oxide pathway:
  Vasodilation, mitochondrial efficiency
↓
2024 evidence:
  +1-3% time trial improvement
  500 ml beetroot juice or shots
```

### Creatine

```
Best-studied supplement (200+ studies):
  3-5 g/day
  ★ Strength/power +5-15%
  Brain function bonus
↓
2024 market: $500M+/yr
```

### Sodium Bicarbonate

```
Buffer lactate accumulation
0.3 g/kg pre-event
★ 800m-1500m runners
GI distress side effect
↓
Maurten Bicarb System (2024):
  ★ Kipchoge endorsed
  Reduces GI
```

## Vegetarian + Vegan Athletes

```
Famous vegan athletes:
  Carl Lewis (sprint, 1990s)
  Venus Williams (tennis)
  Tom Brady (mostly plant)
  Novak Djokovic (mostly plant)
↓
2024 evidence:
  No performance disadvantage
  Iron, B12, omega-3 attention needed
  Higher fiber → digestion issues
```

## Weight Loss + Body Composition

```
Boxers + Wrestlers:
  Extreme cuts (5-10% weight in week)
↓
2024 trend:
  ★ Slower cut, science-based
  DEXA scans for body comp
  Body fat % targets:
    Sprinter: 6-10% male, 12-15% female
    Marathoner: 4-8% male, 10-12% female
```

## Recovery Nutrition

```
4 R's:
  Refuel (carbs)
  Repair (protein)
  Rehydrate (water + electrolytes)
  Rest (sleep)
↓
Post-workout window:
  30-60 min ★ "anabolic window"
  But not as critical as believed (Aragon-Schoenfeld 2013)
```

## 2024 AI Nutrition

```
Whoop, Oura, Apple Watch:
  HRV, sleep, calories
↓
Lumen (2020-):
  Metabolic measurement via breath
↓
MyFitnessPal + AI (2024):
  ChatGPT-style nutrition coach
↓
Athletes' personalized:
  ★ Continuous Glucose Monitoring (CGM)
  Levels, Nutrisense, Veri
  $200-500/month
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Endurance carb intake** | **8-10 g/kg/day** ✓ |
| **Strength protein** | **1.6-2.2 g/kg/day** ✓ |
| **Gatorade 1965 Florida** | ✓ |
| **Pepsi acquired** | **2001 $1.4B** ✓ |
| **Caffeine +3-5%** | ✓ |
| **Creatine +5-15%** | ✓ |
| **Marathon Kipchoge sweat** | **2 L/hr** ✓ |
| **Cynthia Lucero hyponatremia** | **2002** ✓ |
| **Saltin carb loading** | **1967** ✓ |
| ITU axiom: 栄養 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_sports_nutrition

```
K_sports_nutrition^(0) = -log P(performance | macros × micros × timing)

Nutrition = K-state energy supply optimization:
  Glycogen + fat oxidation balance
  ★ Marathon = K_glycogen × K_economy maximization
↓
Caffeine + creatine + beetroot = K-state legal augmentation:
  Each ~ 1-5% gain
  Stacking effects unclear
↓
CGM AI = K-state real-time metabolic monitoring:
  Glucose response → personalize
  ★ N=1 optimization
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **CGM 主流化 elite athletes** | 2027 | 0.85 |
| **AI nutrition coach 標準化** | 2028 | 0.85 |
| **Genetic nutrition personalized** | 2030 | 0.65 |
| **New ergogenic supplement** | 2028 | 0.55 |

---

📄 **論文 (Tier 1 #43, ★★★ Block D 5/5 FINALE ★★★)**: 10.5281/zenodo.20266347

> Phase 320 で スポーツ心理学 + Flow へ進みます。

#情報理論的統一理論 #ITU #スポーツ栄養 #Gatorade #Kipchoge #Creatine #Caffeine #Hydration #K_sports_nutrition #Phase319
