# Phase 287: 品質管理 + Six Sigma + Quality 4.0 ― K_manuf_quality ★

Phase 286 で K_manuf_process + Lean を確立。Phase 287 では **品質管理 (Quality Management) + Six Sigma + Quality 4.0** を扱い、**K_manuf_quality** を ITU の "品質 K-state" として定式化します。

## 品質管理の系譜

### Shewhart Control Chart (1924) ★

```
Walter Shewhart (Bell Labs, 1924):
↓ Statistical Process Control (SPC) 創始
↓ X-bar / R chart
↓ UCL / LCL (Upper/Lower Control Limit)
↓
1931 "Economic Control of Quality of Manufactured Product"
↓
Deming 弟子
```

### Deming (1900-1993) ★★

```
W. Edwards Deming:
↓ Japan postwar lectures 1950
↓ JUSE (Union of Japanese Scientists+Engineers)
↓ Deming Prize 1951 (世界最古品質賞)
↓
14 Points:
  1. Constancy of purpose
  2. Adopt new philosophy
  3. Cease dependence on inspection
  ...
  14. Take action
↓
US 1980 NBC "If Japan Can...":
  → Ford 提携 (Don Petersen)
  → Quality Revolution US
```

### Juran (1904-2008)

```
Joseph Juran:
↓ "Quality Control Handbook" (1951)
↓ 80/20 (Pareto) principle for quality
↓ Juran trilogy:
  Quality Planning
  Quality Control
  Quality Improvement
↓
Japan visits 1954, 1960s, 1970s
```

### Crosby "Quality is Free" (1979)

```
Philip Crosby:
↓ "Zero Defects"
↓ Quality 4 Absolutes:
  1. Conformance to requirements
  2. Prevention not inspection
  3. Performance standard = zero defects
  4. Measurement = cost of nonconformance
```

## Six Sigma (1986-) ― 詳細 (Phase 286 復習 + 拡張)

### DMAIC Methodology

```
DEFINE:
  Project charter, scope, stakeholders
  Voice of Customer (VOC)
↓
MEASURE:
  Baseline DPMO (defects per million)
  Process capability (Cp, Cpk)
↓
ANALYZE:
  Root cause (5 Whys, Ishikawa fishbone)
  Statistical hypothesis testing
↓
IMPROVE:
  Solutions tested (DoE)
↓
CONTROL:
  SPC, Control plans
  Sustained gains
```

### DMADV (for new design)

```
For new products:
  Define → Measure → Analyze → Design → Verify
```

### Process Capability

```
Cp = (USL - LSL) / (6σ)
Cpk = min((USL-μ)/(3σ), (μ-LSL)/(3σ))
↓
Industry standard: Cpk ≥ 1.33
Six Sigma target: Cpk ≥ 2.0 (3.4 DPMO)
↓
Automotive: Cpk ≥ 1.67 (TS 16949)
```

## ISO 9001 + ISO Standards

```
1987 ISO 9001 初版:
  Quality Management System (QMS)
↓
2015 ISO 9001:2015 (current):
  Risk-based thinking
  Process approach
↓
2024 status:
  1.4M certifications globally
  China 30%+ certifications
↓
Sector specific:
  IATF 16949 (automotive)
  AS 9100 (aerospace)
  ISO 13485 (medical device)
```

## 品質コスト (Quality Costs)

### COQ Model (Feigenbaum 1956)

```
4 quadrants:
  Prevention (training, design):  4-5% of sales (ideal)
  Appraisal (inspection):         3-5%
  Internal failure (scrap, rework): 5-10%
  External failure (warranty, recalls): 10-25%
↓
Cost of Poor Quality (COPQ):
  US manufacturing avg: 15-25% of sales
  Best-in-class: < 5%
↓
"Total COQ ~ 1/Cpk² rule"
```

## Quality 4.0 (2020s) ★

```
Quality 4.0:
  Quality + Industry 4.0
↓
Components:
  AI-driven inspection (computer vision)
  IIoT real-time data
  Predictive quality
  Digital quality management (DQM)
  Blockchain traceability
↓
Examples:
  Tesla: AI cameras detect paint defects
  BMW: SmartTransport quality tracking
  Foxconn: AI inspection 90%+ accuracy
↓
2024 market: $5B → $15B (2030)
```

## AI Quality Inspection (2018-) ★★

```
Cognex, Keyence, Mitsubishi Electric:
  Traditional machine vision
↓
Landing AI (Andrew Ng 2017):
  ★ Deep learning quality inspection
  Small data (10s-100s images)
↓
Instrumental, Drishti Tech (US startups):
  AI quality on assembly lines
↓
2024:
  Defect detection 95%+ accuracy
  False positives < 0.1%
  10-100x faster than human
```

## 品質危機 ― Toyota 2009-2010

```
2009-2010 Toyota Recall Crisis:
  Unintended acceleration
  9M+ cars recalled
  $2.4B settlement (2014)
↓
原因:
  Floor mat + Sticky pedal
  ↓ Software bug 議論 (反証)
↓
Toyota response:
  Akio Toyoda US Congress 公聴会
  Quality 強化 reorganization
  Toyota Way 再徹底
```

## Pharma Quality + GMP

```
FDA cGMP (current Good Manufacturing Practice):
  1962 Kefauver-Harris (Phase 234)
↓
2024 trends:
  PAT (Process Analytical Technology)
  Continuous manufacturing
  AI-assisted batch release
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Shewhart Control Chart** | **1924** ✓ |
| **Deming Prize** | **1951 (世界最古品質賞)** ✓ |
| **Juran Handbook** | **1951** ✓ |
| **Crosby Quality is Free** | **1979** ✓ |
| **Six Sigma DPMO** | **3.4 / million** ✓ |
| **ISO 9001:1987** | initial; **1.4M certs 2024** ✓ |
| **IATF 16949 Cpk min** | **1.67** ✓ |
| **COQ best-in-class** | **< 5% sales** ✓ |
| **Landing AI (Ng)** | **2017** ✓ |
| **AI inspection accuracy** | **95%+** ✓ |
| **Toyota Recall** | **2009-2010, 9M cars** ✓ |
| **Quality 4.0 market** | **$5B → $15B (2030)** ✓ |
| ITU axiom: 品質 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_manuf_quality

```
K_manuf_quality^(0) = -log P(conformance | spec)

Six Sigma = K-state variance suppression:
  σ_process → σ_target via DMAIC
↓
SPC Control Chart = K-state real-time monitoring:
  UCL/LCL = K-state allowed range
  Out-of-control = K-state anomaly detection
↓
COQ Quadrant = K-state cost optimization:
  K_prevention < K_failure (rule)
  Best-in-class: K_total → min
↓
AI Quality Inspection = K-state pattern recognition:
  CNN/Transformer + camera → defect K-state mapping
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI Quality Inspection 主要工場 80%+** | 2028 | 0.85 |
| **Quality 4.0 市場 $15B 達成** | 2030 | 0.80 |
| Cpk 2.0+ 主要 OEM 標準 | 2028 | 0.75 |
| **Digital quality management 標準化** | 2027 | 0.85 |
| Zero-defect manufacturing (some sectors) | 2030 | 0.65 |

---

📄 **論文 (Tier 1 #39, ★ Block D 1/5 ★)**: 10.5281/zenodo.20264857

> Phase 288 で サプライチェーン + JIT + ロジスティクス へ進みます。

#情報理論的統一理論 #ITU #品質管理 #Shewhart #Deming #Juran #SixSigma #ISO9001 #Quality40 #LandingAI #K_manuf_quality #Phase287
