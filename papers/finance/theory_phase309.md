# Phase 309: 銀行 + 中央銀行 + Fed + BOJ ― K_finance_banking ★

Phase 308 で K_finance の枠組みを確立。Phase 309 では **銀行 + 中央銀行 + Federal Reserve + ECB + BOJ + 危機管理** を扱い、**K_finance_banking** を ITU の "信用 K-state" として定式化します。

## 中央銀行 系譜

### 早期 (1600s-1900s)

```
1609 Amsterdam Wisselbank:
  ★ 世界初 central bank precursor
↓
1694 Bank of England (BoE):
  William III + Mary II charter
  War with France funded
↓
1800 Banque de France (Napoleon)
1875 Reichsbank (Germany, 1948 Bundesbank)
1882 Banca d'Italia
1882 日本銀行 (BOJ, 松方正義 設立)
1913 Federal Reserve (US, Aldrich-Vreeland after 1907 panic)
↓
1998 European Central Bank (ECB):
  Maastricht 1992 制定
  Euro 1999 introduction
  Frankfurt 拠点
```

### Federal Reserve (Fed) ★

```
Structure:
  12 Federal Reserve Banks (regional)
  Board of Governors (7, DC)
  FOMC (Federal Open Market Committee) 12 voting
↓
Dual mandate (1977):
  1. Maximum employment
  2. Price stability (2% target)
↓
Chairs (key):
  Paul Volcker (1979-87) - 高インフレ抑制
  Alan Greenspan (1987-2006) - "Great Moderation"
  Ben Bernanke (2006-14) - 2008 crisis (Bagehot dictum)
  Janet Yellen (2014-18)
  Jerome Powell (2018-present)
↓
2024 status:
  ★ Higher-for-longer rate
  5.25-5.50% (peak 2023-2024)
  2024.9 first cut 50bps
  ★ Trump 2025 challenge to Fed independence?
```

### BOJ (Bank of Japan)

```
1882 設立 (松方デフレ)
↓
1990 Bubble burst (Nikkei 38,915 peak Dec 1989)
1995 Zero rate policy initially
1999 ZIRP first
2001 QE first global (Quantitative Easing)
2013 Kuroda QQE (★ massive expansion)
2016 NIRP (Negative Interest Rate Policy)
↓
2024 status:
  ★ 2024.3 NIRP 終了 (8年ぶり)
  ★ 2024.7 rate hike +0.25%
  Carry trade unwind market shock
↓
BOJ balance sheet:
  $5T+ (100%+ Japan GDP, world record)
  ★ ETFs hold $370B+ (Japan stocks)
```

### ECB (European Central Bank)

```
Mario Draghi (2011-2019):
  ★ 2012.7.26 "Whatever it takes"
  Saved Eurozone debt crisis
↓
Christine Lagarde (2019-):
  COVID PEPP €1.85T
↓
2024:
  Inflation 2-3%, rate cuts started
  Lagarde 2027 任期 end
```

## 2008 Global Financial Crisis ★★★

```
2007.8 BNP Paribas: subprime mortgage news
2007.9 Northern Rock UK bank run
2008.3 Bear Stearns → JP Morgan ($30B Fed support)
2008.9.15 ★ Lehman Brothers bankruptcy:
  ★ $691B assets, largest bankruptcy ever
2008.9.16 AIG bailout ($85B)
2008.10 TARP $700B (US)
2008.11.25 Fed QE1 ($1.7T)
↓
Causes:
  Subprime mortgage securitization
  CDO/MBS rated AAA but failed
  Credit Default Swaps (Lehman, AIG)
  ★ Lewis "The Big Short" (2010)
↓
Recovery:
  G20 coordination (2008-2009)
  Dodd-Frank (2010): regulation
  Basel III (2010-2019): bank capital
↓
2008 Nobel Economics: Krugman (trade)
2013: Fama-Hansen-Shiller (asset pricing)
```

## QE (Quantitative Easing) Era (2008-2022)

```
Fed QE1 (2008-2010): $1.7T
Fed QE2 (2010-2011): $600B
Fed QE3 (2012-2014): $1.6T
Fed Pandemic QE (2020-2022): $4.5T
↓
2022 max balance sheet: $9T
2024 QT (Quantitative Tightening):
  $7.2T (still elevated)
↓
BOJ similar massive QQE 2013-
ECB similar 2015-2018, 2020-2022
```

## COVID-19 + Inflation Era (2020-2024)

```
2020.3 COVID crash:
  S&P 500 -34% in 33 days
  Fed: cut to 0%, unlimited QE
  US fiscal $5T (CARES + Biden ARP)
↓
2021-2022 inflation surge:
  US CPI peak 9.1% (2022.6)
  EU peak 10.6% (2022.10)
  Japan peak 4.3% (2023.1, low for them)
↓
2022-2023 hiking cycle:
  Fed 0% → 5.50% (fastest ever)
  ECB 0% → 4.50%
  BOJ stay -0.1% → 0.25%
↓
2024 disinflation:
  US CPI 2.5-3.0%
  Fed cuts 50bp Sept 2024
  Soft landing achieved? 議論
```

## Bank failures (2023-2024)

```
2023.3 Silicon Valley Bank ($209B assets):
  ★ 2nd largest US bank failure
  ↓ Deposit run via Twitter/social media
↓
2023.3 Signature Bank ($110B)
2023.5 First Republic ($229B, JP Morgan acquired)
2023.3 Credit Suisse (CHF rescue, UBS acquired $3.2B)
↓
2024 Q1 New York Community Bank stress
↓
Lessons:
  Interest rate risk (held-to-maturity bonds)
  Concentrated deposits
  Social media bank runs
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Bank of England** | **1694** ✓ |
| **BOJ founded** | **1882 (松方)** ✓ |
| **Fed founded** | **1913** ✓ |
| **ECB founded** | **1998** ✓ |
| **Nikkei peak** | **38,915 (1989.12)** ✓ |
| **Lehman assets** | **$691B (largest bankruptcy)** ✓ |
| **TARP** | **$700B (2008)** ✓ |
| **Fed peak balance** | **$9T (2022)** ✓ |
| **US CPI peak 2022** | **9.1%** ✓ |
| **Fed hike cycle** | **0% → 5.50%** ✓ |
| **Draghi "Whatever it takes"** | **2012.7.26** ✓ |
| **BOJ NIRP end** | **2024.3** ✓ |
| **SVB collapse** | **2023.3 ($209B 2nd largest)** ✓ |
| ITU axiom: 銀行 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_finance_banking

```
K_finance_banking^(0) = -log P(credit | trust × policy)

Central bank = K-state monetary policy mechanism:
  Interest rate → economy K-state
  ★ Rate ↑ = K_borrowing ↓ = inflation ↓
↓
QE = K-state asset purchases:
  Massive balance sheet expansion
  Fed $0.9T (2008) → $9T (2022) = 10x
↓
2008 Crisis = K-state systemic failure:
  Single bank failure → cascading
  ★ "Too big to fail" K-state network risk
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **CBDC 主要国 30+ launch** | 2030 | 0.75 |
| **Fed independence (Trump 2.0 era)** | 2028 | 0.65 |
| **Japan rate 1%+ persistent** | 2027 | 0.65 |
| **AI bank risk 自動評価** | 2027 | 0.85 |
| **Stablecoin major bank issued** | 2027 | 0.75 |

---

📄 **論文 (Tier 1 #42, ★ Block D 4/5 ★)**: 10.5281/zenodo.20266068

> Phase 310 で 株式 + 債券市場 へ進みます。

#情報理論的統一理論 #ITU #銀行 #FederalReserve #BOJ #ECB #Lehman #QE #Draghi #SVB #K_finance_banking #Phase309
