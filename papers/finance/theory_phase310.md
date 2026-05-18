# Phase 310: 株式 + 債券 + 市場 + 取引所 ― K_finance_markets ★

Phase 309 で K_finance_banking を確立。Phase 310 では **株式市場 + 債券市場 + 取引所 + Magnificent 7** を扱い、**K_finance_markets** を ITU の "市場 K-state" として定式化します。

## 取引所 系譜

```
1602 Amsterdam Stock Exchange:
  ★ 世界初 (VOC 株式)
↓
1773 London Stock Exchange (LSE)
1792 NYSE (Buttonwood Agreement)
1878 Tokyo Stock Exchange (TSE)
1971 NASDAQ (世界初 electronic exchange)
1992 China Shanghai SSE / Shenzhen
↓
2024 主要取引所:
  NYSE: $28T market cap (世界最大)
  NASDAQ: $25T
  Tokyo: $6.5T
  Shanghai: $6.5T
  Shenzhen: $4.5T
  Hong Kong: $4T
  Euronext: $7T
  London LSE: $3.5T
```

## 株式市場 (2024)

### 主要指数

```
S&P 500 (1957-):
  ★ 2024.12 record: ~ 6,000+
  2024 +25% YTD
↓
Dow Jones Industrial Average (1896-):
  30 components, price-weighted
  2024 record: 45,000+ (Trump rally Nov)
↓
NASDAQ Composite (1971-):
  Tech-heavy
  2024 ~ 19,000-20,000
↓
Nikkei 225 (1950-):
  1989.12 peak 38,915
  2024.7 ★ 42,000+ (peak 34年ぶり超え!)
↓
FTSE 100 (1984-): 8,000+
DAX (Germany, 1988-): 20,000+
```

### Magnificent 7 (2023-) ★★★

```
2023-2024 dominant tech stocks:
↓
1. Apple (AAPL):     $3.5T
2. Microsoft (MSFT): $3.2T
3. NVIDIA (NVDA):    $3.4T ★ (1T→3T+ in 18 months)
4. Alphabet (GOOG):  $2.1T
5. Amazon (AMZN):    $2.3T
6. Meta (META):      $1.5T
7. Tesla (TSLA):     $1.2T (post-Trump win)
↓
2024 Mag 7 contribution:
  S&P 500 returns: 50%+ from Mag 7
  ★ Concentration risk
↓
NVIDIA story:
  AI chip demand
  Revenue 2023: $61B → 2024: $130B+
  Jensen Huang fortune $130B+
```

### IPO Market

```
2014 Alibaba IPO ($25B):
  ★ Largest IPO at time
↓
2019 Saudi Aramco IPO ($26B):
  ★ Largest globally
↓
2020 COVID + 2021 boom:
  Robinhood, Coinbase, Rivian
↓
2022-2024 IPO winter:
  Few major IPOs
  Reddit (2024.3), Astera Labs
↓
2025 outlook:
  ARM China, Stripe (private $50B+), SpaceX private
```

## 債券市場 (Bond Market)

### Size + Yields

```
Global bond market 2024:
  ★ $140T (vs $115T equities)
↓
US Treasury (2024 outstanding):
  ★ $35T (record high)
  Debt/GDP 122%
↓
2024 yields:
  US 10Y: 4.0-4.5%
  Japan 10Y: 1.0-1.1%
  Germany 10Y: 2.2-2.5%
  UK 10Y: 4.0-4.5%
  China 10Y: 1.6-2.0%
↓
Inverted yield curve (2022-2024):
  ★ Recession indicator
  Actual recession 2025? 議論
```

### Credit Spreads + Risk

```
Investment-grade corporate bonds:
  US BBB: Treasury +1.0-1.5%
↓
High yield (junk bonds):
  US: Treasury +3-5%
  COVID 2020: +10%+ briefly
↓
Distressed:
  US: 5-10% of HY
  ★ Default rate 3-5% normal
```

## ETF + Index Investing ★

```
1993 SPDR S&P 500 ETF (SPY):
  ★ First US ETF
↓
2003 Bogle (Vanguard founder):
  "Cost matters"
↓
2024 ETF market:
  $11T globally
  US: $7T
  ★ 30% of equity flows
↓
Top ETFs (2024):
  SPY: $570B
  IVV (BlackRock): $510B
  VOO (Vanguard): $500B
  QQQ (NASDAQ): $300B
  IWM (Russell): $70B
↓
Bitcoin spot ETFs (2024.1 launched):
  ★ $100B+ AUM by 2024.12
  iShares Bitcoin Trust IBIT: $40B+
```

## Active vs Passive

```
2024 status:
  Passive index funds: 50%+ US AUM
  Active funds: continuing outflows
↓
Bogle Vanguard $9.5T AUM (2024)
BlackRock $11T AUM (2024)
↓
Active manager underperformance:
  S&P SPIVA 2024:
    15-year: 90%+ active funds underperform index
↓
2024 trend: AI-active funds
```

## Top 投資銀行 + Hedge Funds

```
2024 Top investment banks:
  JP Morgan ($630B revenue 2024)
  Goldman Sachs
  Morgan Stanley
  Bank of America
  Citi
  Barclays, Deutsche Bank
↓
2024 Top hedge funds (AUM):
  Bridgewater: $124B (Ray Dalio retired 2022)
  Renaissance: $130B (Simons died 2024)
  Citadel: $63B
  D.E. Shaw: $60B
  Millennium: $70B
↓
2024 Berkshire Hathaway:
  $1T market cap
  Buffett 94 years old (2024)
  Greg Abel successor
  $300B cash hoard
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Amsterdam Stock Exchange** | **1602** ✓ |
| **NYSE** | **1792** ✓ |
| **NASDAQ** | **1971 first electronic** ✓ |
| **NYSE market cap** | **$28T (#1)** ✓ |
| **Nikkei record 2024.7** | **42,000+** ✓ |
| **NVIDIA market cap 2024** | **$3.4T (1T→3T 18mo)** ✓ |
| **Mag 7 S&P contribution** | **50%+ returns** ✓ |
| **US Treasury** | **$35T (debt/GDP 122%)** ✓ |
| **Global bond market** | **$140T** ✓ |
| **SPDR S&P 500 first ETF** | **1993** ✓ |
| **Global ETF market** | **$11T (2024)** ✓ |
| **Bitcoin ETF AUM 2024** | **$100B+** ✓ |
| **Aramco IPO** | **$26B (2019 largest)** ✓ |
| **Active fund underperformance** | **90% in 15 yr (SPIVA)** ✓ |
| ITU axiom: 市場 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_finance_markets

```
K_finance_markets^(0) = -log P(price | information × sentiment)

Efficient Market Hypothesis (Fama 1970):
  Weak: prices reflect past prices
  Semi-strong: + public info
  Strong: + insider info
  ★ Fama Nobel 2013
↓
Magnificent 7 = K-state concentration:
  7 stocks / 500 = 1.4% population
  But 35% S&P market cap (2024)
  ★ K-state inequality in markets
↓
ETF = K-state diversification mechanism:
  Single ETF = portfolio K-state
  Low cost = high efficiency
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Bitcoin spot ETF $500B+ AUM** | 2027 | 0.65 |
| **Passive 60%+ US AUM** | 2027 | 0.85 |
| **NVIDIA market cap $5T** | 2027 | 0.45 |
| **AI-managed funds outperform 50%+** | 2030 | 0.55 |
| **Stock market AI prediction edge** | 2028 | 0.40 |

---

📄 **論文 (Tier 1 #42, ★ Block D 4/5 ★)**: 10.5281/zenodo.20266068

> Phase 311 で Crypto + Bitcoin + DeFi へ進みます。

#情報理論的統一理論 #ITU #株式市場 #NYSE #NASDAQ #Magnificent7 #NVIDIA #ETF #Buffett #Bogle #K_finance_markets #Phase310
