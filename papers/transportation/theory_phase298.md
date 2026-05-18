# Phase 298: 自動運転車 (AV) + Waymo + Tesla FSD ― K_transport_AV ★★★

Phase 297 で K_transport_EV を確立。Phase 298 では **自動運転車 (Autonomous Vehicles) + Waymo + Tesla FSD + 2024 robotaxi 革命** を扱い、**K_transport_AV** を ITU の "自律運転 K-state" として定式化します。

## SAE Levels (J3016, 2014-)

```
Level 0: No automation
Level 1: Driver assistance (cruise control)
Level 2: Partial (Tesla Autopilot, GM Super Cruise)
Level 3: Conditional (Audi A8 2017, Mercedes Drive Pilot 2022)
Level 4: High (Waymo, Cruise) - 地理 limited
Level 5: Full automation (everywhere) - まだ無
↓
2024 status:
  L2: Most premium cars
  L3: Limited (Mercedes, Honda Legend, BMW 7)
  L4: Robotaxi (Waymo Phoenix, Bay Area)
  L5: ✗ (まだ research)
```

## DARPA Grand Challenge (2004-2007) ★

```
2004 DARPA Grand Challenge (Mojave):
  ★ ALL 15 vehicles failed (max 7.4 mi/240 mi)
↓
2005 DARPA:
  ★ Stanford "Stanley" (Thrun) 1位
  CMU "Sandstorm" 2位
↓
2007 DARPA Urban Challenge:
  CMU "Boss" 1位
  ↓ 6 of 11 finished
↓
影響: Sebastian Thrun → Google Self-Driving 2009
```

## Waymo (2009-) ★★★

```
2009 Google Self-Driving Car (Thrun, Levandowski)
2016 Waymo spinoff
↓
2017 Waymo One launch (Phoenix, safety driver)
2018 Phoenix公開 limited test
2020 Phoenix fully driverless start
2022 Phoenix expanded
2023 San Francisco public service
2024:
  ★ 150K+ paid rides/week
  Phoenix, SF, LA, Austin
  ↓ 50% YoY growth
↓
Tech:
  LIDAR + Radar + Cameras (12+ sensors)
  Custom Waymo Driver hardware
  $200K+ per vehicle
```

## Cruise (GM 2016-2024) ★

```
2016 GM acquired ($1B+)
2020 Cruise Origin (purpose-built)
2022 SF night service
2023.10 ★ Pedestrian dragged 6m (Oct 2)
  → California DMV permit suspension
↓
2023.11 全米 service suspension
2024.6 limited Phoenix restart
2024.9 ★ Honda partnership announced
2024.10 GM ceases Cruise robotaxi business ($10B+ losses)
↓
Lesson: Safety + PR are critical
```

## Tesla FSD (Full Self-Driving) ★

```
2014 Autopilot launch (L2)
2015 Highway L2
2016.10 Hardware 2 (8 cameras)
2018 Autopilot v9
↓
2020.10 FSD Beta (city streets, L2 supervised)
2024.3 FSD v12 (end-to-end neural net):
  ★ "Vision-only" (no LIDAR, no HD map)
  ★ Single neural net (vs 300K lines old)
↓
2024.10 We, Robot event (Hollywood):
  Cybercab (no steering wheel)
  Robotaxi launch 2026 target (Tesla California)
↓
Robotaxi competition:
  Waymo (operational L4)
  Tesla (Beta L2 expanding)
  Zoox (Amazon)
  Pony.ai, WeRide (China)
```

## 中国 robotaxi 競争

```
Baidu Apollo (2017-):
  Wuhan 全市 robotaxi 2024
  ★ 全球最大 robotaxi fleet (500+ vehicles)
↓
Pony.ai (2016-):
  Beijing, Guangzhou L4
↓
WeRide (2017-): NASDAQ IPO 2024
↓
2024 status:
  China: 5+ cities with L4 robotaxi
  US: Waymo dominant
  EU: Mercedes L3 only
```

## Trucking AV

```
Aurora Innovation (2017-):
  Phoenix-El Paso 2024.12 commercial start
  ★ World's first commercial autonomous trucking
↓
Plus.ai, TuSimple (struggles):
  TuSimple 2023 China focus
↓
Waymo Via (paused 2023)
Embark (2023 closed)
↓
2024 reality: harder than passenger
```

## 安全 + 統計

```
2024 Waymo safety report:
  22M miles autonomous (no human)
  vs human 600K miles per fatality (US avg)
  ★ Waymo claim 88% fewer airbag events
  3 minor injuries (2023)
↓
2023 Cruise pedestrian incident:
  ★ Confidence loss
↓
NHTSA report (2024):
  Tesla Autopilot 956 crashes (Jan 2018-Aug 2023)
  46 死亡 (45 vehicles)
  ↓ FSD beta included
↓
比較:
  Human: ~ 1.4 deaths/100M miles (US)
  Waymo: 0 deaths/22M miles (none yet)
```

## ADAS (Advanced Driver-Assistance Systems)

```
L2 ADAS market 2024:
  Tesla Autopilot
  GM Super Cruise (hands-free, 2017-)
  Ford BlueCruise (2021-)
  Honda SENSING / Toyota Safety Sense
↓
L3:
  Mercedes Drive Pilot (60 km/h highway)
  Honda Legend SENSING Elite (2021, 100 units only)
  BMW 7 Series L3 (2024)
↓
2024 trend:
  Eyes-off driving in select conditions
  ↓ Insurance + legal frameworks slow
```

## V2X (Vehicle-to-Everything)

```
V2V (Vehicle-to-Vehicle):
  US DSRC 5.9 GHz mandate 2014 (revoked 2017)
  China C-V2X mandate
↓
V2I (Vehicle-to-Infrastructure):
  Smart traffic lights
  Highway communication
↓
V2X 2024:
  China leads deployment
  US/EU slow (technology choice fragmented)
```

## 倫理 + 法的問題

```
Trolley Problem 議論:
  MIT Moral Machine experiment (2018 Nature)
  ★ 40M decisions from 233 countries
↓
2024 法的責任:
  L3+: Manufacturer liable (theoretically)
  L2: Driver liable (Tesla FSD Beta)
↓
Insurance:
  Munich Re, Tesla Insurance (2019-)
  Geico AV programs
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **DARPA Grand Challenge** | **2004-2007** ✓ |
| **Stanford Stanley (Thrun)** | **2005 1位** ✓ |
| **Waymo founded** | **2009 Google, 2016 spinoff** ✓ |
| **Waymo 2024 rides/wk** | **150K+ (paid)** ✓ |
| **Cruise pedestrian 2023.10** | **6m dragged → suspension** ✓ |
| **Cruise GM ceased** | **2024.10 ($10B+ losses)** ✓ |
| **Tesla FSD v12** | **2024.3 end-to-end neural** ✓ |
| **Tesla Cybercab** | **2024.10 launch event** ✓ |
| **Baidu Apollo Wuhan** | **500+ vehicles 2024** ✓ |
| **Aurora trucking** | **2024.12 Phoenix-El Paso** ✓ |
| **Mercedes Drive Pilot** | **2022 L3 (60 km/h)** ✓ |
| **Waymo miles autonomous** | **22M (no human)** ✓ |
| **MIT Moral Machine** | **2018 Nature, 233 国** ✓ |
| ITU axiom: AV K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_transport_AV

```
K_transport_AV^(0) = -log P(decision | road_state)

SAE Level scaling = K-state autonomy increase:
  L0 (manual) → L5 (full)
  Each level = K_human-AI division shift
↓
Waymo vs Tesla = K-state architecture divergence:
  Waymo: K_HDmap + K_LIDAR + K_geofenced
  Tesla: K_vision-only + K_neural-net + K_global
↓
2024 robotaxi = K-state real-world deployment:
  150K rides/wk = K-state social proof
  ★ But Cruise crash = K-state risk realized
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Waymo expand to 10+ US cities** | 2027 | 0.85 |
| **Tesla robotaxi commercial** | 2027 | 0.65 |
| **Aurora trucking 主要 corridor** | 2027 | 0.80 |
| **L4 robotaxi 5+ major cities globally** | 2028 | 0.85 |
| **L5 (fully general) achieved** | 2032 | 0.45 |
| **AV fatality rate < human** | 2027 | 0.75 |

---

📄 **論文 (Tier 1 #40, ★ Block D 2/5 ★)**: 10.5281/zenodo.20265252

> Phase 299 で 40-vertex polytope 統合 + 10 予測 へ進みます。

#情報理論的統一理論 #ITU #自動運転 #AV #Waymo #Tesla #FSD #Cybercab #Aurora #Cruise #Baidu #Apollo #K_transport_AV #Phase298
