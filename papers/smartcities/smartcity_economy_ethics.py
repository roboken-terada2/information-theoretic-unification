"""
Phase 105: Smart city economy, policy, surveillance ethics
Tier 1 #16 — Phase 3/4

4 numerical experiments:
1. Smart city market 2020-2050 + segments
2. EU AI Act risk categories
3. Surveillance vs privacy by country
4. Digital divide within cities (income tiers)

Output: smartcity_economy_ethics.png + smartcity_economy_ethics_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Smart city market
# ----------------------------------------------------------------------
def test1_market():
    timeline = [
        {"year": 2020, "market_B": 400,  "main": "Smart meters, IoT"},
        {"year": 2024, "market_B": 700,  "main": "+ AI, 5G, autonomous"},
        {"year": 2030, "market_B": 1500, "main": "+ Quantum, early AGI"},
        {"year": 2040, "market_B": 2500, "main": "AGI city, robotics"},
        {"year": 2050, "market_B": 3000, "main": "ASI city, digital twins"},
    ]
    segments_2024 = [
        {"name": "Smart energy",         "value_B": 200},
        {"name": "Smart transportation", "value_B": 150},
        {"name": "Smart buildings",      "value_B": 130},
        {"name": "Smart governance",     "value_B": 80},
        {"name": "Smart healthcare",     "value_B": 70},
        {"name": "Smart safety",         "value_B": 50},
        {"name": "Smart environment",    "value_B": 20},
    ]
    return {"timeline": timeline, "segments_2024": segments_2024, "growth_2024_2050": 3000/700}


# ----------------------------------------------------------------------
# Test 2: EU AI Act risk categories
# ----------------------------------------------------------------------
def test2_eu_ai_act():
    categories = [
        {"level": "Prohibited",     "examples": "Social scoring, mass face rec.", "n_use_cases": 8,  "compliance_cost": 0,    "color": "#d62728"},
        {"level": "High risk",      "examples": "Police, hiring, education, medical", "n_use_cases": 40, "compliance_cost": 500_000, "color": "#ff7f0e"},
        {"level": "Limited risk",   "examples": "Chatbots, deepfakes",          "n_use_cases": 30, "compliance_cost": 50_000,  "color": "#ffcc00"},
        {"level": "Minimal risk",   "examples": "Games, simple AI",              "n_use_cases": 200,"compliance_cost": 0,       "color": "#2ca02c"},
    ]
    return {"categories": categories}


# ----------------------------------------------------------------------
# Test 3: Surveillance vs privacy
# ----------------------------------------------------------------------
def test3_surveillance():
    countries = [
        {"country": "China",       "surveillance": 0.95, "privacy": 0.05, "policy": "Social Credit"},
        {"country": "Russia",      "surveillance": 0.85, "privacy": 0.10, "policy": "Sovereign Internet"},
        {"country": "India",       "surveillance": 0.65, "privacy": 0.30, "policy": "Aadhaar + lax"},
        {"country": "USA",         "surveillance": 0.55, "privacy": 0.45, "policy": "State-level mix"},
        {"country": "Singapore",   "surveillance": 0.50, "privacy": 0.55, "policy": "Limited use"},
        {"country": "UK",          "surveillance": 0.55, "privacy": 0.50, "policy": "CCTV heavy"},
        {"country": "Japan",       "surveillance": 0.30, "privacy": 0.70, "policy": "Private only"},
        {"country": "Germany",     "surveillance": 0.25, "privacy": 0.80, "policy": "GDPR + strict"},
        {"country": "EU avg",      "surveillance": 0.20, "privacy": 0.85, "policy": "GDPR + AI Act"},
        {"country": "Estonia",     "surveillance": 0.20, "privacy": 0.90, "policy": "Data trust"},
    ]
    return {"countries": countries}


# ----------------------------------------------------------------------
# Test 4: Digital divide within cities
# ----------------------------------------------------------------------
def test4_digital_divide():
    cities = [
        {"city": "Singapore",  "high_income": 99, "mid_income": 98, "low_income": 95},
        {"city": "Tokyo",      "high_income": 99, "mid_income": 97, "low_income": 92},
        {"city": "Zurich",     "high_income": 99, "mid_income": 95, "low_income": 90},
        {"city": "New York",   "high_income": 97, "mid_income": 88, "low_income": 78},
        {"city": "London",     "high_income": 96, "mid_income": 85, "low_income": 75},
        {"city": "São Paulo",  "high_income": 95, "mid_income": 70, "low_income": 50},
        {"city": "Mumbai",     "high_income": 90, "mid_income": 60, "low_income": 35},
        {"city": "Lagos",      "high_income": 80, "mid_income": 50, "low_income": 20},
        {"city": "Kinshasa",   "high_income": 70, "mid_income": 30, "low_income": 10},
    ]
    for c in cities:
        c["divide"] = c["high_income"] - c["low_income"]
    return {"cities": cities}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Market
    ax = axes[0, 0]
    timeline = t1["timeline"]
    years = [t["year"] for t in timeline]
    market = [t["market_B"] for t in timeline]
    ax.plot(years, market, "o-", color="#1f77b4", lw=2.5, markersize=10, alpha=0.85)
    ax.fill_between(years, 0, market, color="#1f77b4", alpha=0.2)
    for t in timeline:
        ax.annotate(t["main"][:25], (t["year"], t["market_B"]),
                    xytext=(5, 5), textcoords="offset points", fontsize=7, rotation=10)
    ax.set_xlabel("Year")
    ax.set_ylabel("Market size ($B)")
    ax.set_title(f"Smart city market: 2024 $700B → 2050 $3.0T ({t1['growth_2024_2050']:.1f}x)")
    ax.grid(alpha=0.3)

    # Panel 2: EU AI Act
    ax = axes[0, 1]
    cats = t2["categories"]
    names = [c["level"] for c in cats]
    use_cases = [c["n_use_cases"] for c in cats]
    colors = [c["color"] for c in cats]
    ax.bar(names, use_cases, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, c in enumerate(cats):
        cost_str = f"${c['compliance_cost']/1000:.0f}K" if c["compliance_cost"] > 0 else "—"
        ax.text(i, c["n_use_cases"] + 5, f"cost={cost_str}", ha="center", fontsize=8)
    ax.set_ylabel("Number of use cases")
    ax.set_title("EU AI Act 2024: risk categorization (compliance cost varies)")
    ax.grid(alpha=0.3, axis="y")
    plt.setp(ax.get_xticklabels(), rotation=10, ha="right")

    # Panel 3: Surveillance vs privacy
    ax = axes[1, 0]
    countries = t3["countries"]
    for c in countries:
        ax.scatter(c["surveillance"], c["privacy"], s=200, alpha=0.85,
                   edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(c["country"], (c["surveillance"], c["privacy"]),
                    xytext=(5, 5), textcoords="offset points", fontsize=8)
    # Pareto frontier (low surveillance + high privacy)
    ax.plot([0, 1], [1, 0], "k--", alpha=0.3, label="naive tradeoff")
    ax.plot([0.2, 0.55], [0.85, 0.55], "g-", lw=2, alpha=0.5, label="GDPR/EU model")
    ax.plot([0.85, 0.95], [0.10, 0.05], "r-", lw=2, alpha=0.5, label="Surveillance state")
    ax.set_xlabel("Surveillance level (K_surveillance)")
    ax.set_ylabel("Privacy protection (K_privacy)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Surveillance vs Privacy: countries cluster into 2 camps")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4: Digital divide
    ax = axes[1, 1]
    cities = t4["cities"]
    names = [c["city"] for c in cities]
    high = [c["high_income"] for c in cities]
    mid = [c["mid_income"] for c in cities]
    low = [c["low_income"] for c in cities]
    y_pos = np.arange(len(cities))
    width = 0.25
    ax.barh(y_pos - width, high, width, color="#2ca02c", alpha=0.8, label="High income")
    ax.barh(y_pos, mid, width, color="#ff7f0e", alpha=0.8, label="Mid income")
    ax.barh(y_pos + width, low, width, color="#d62728", alpha=0.8, label="Low income")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Internet access (%)")
    ax.set_title("Digital divide within cities (high vs low income gap)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 105: Smart city economy, policy, surveillance ethics",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 105: Smart city economy, policy, surveillance ethics")
    print("=" * 70)

    print("\n[Test 1] Smart city market")
    t1 = test1_market()
    for t in t1["timeline"]:
        print(f"  {t['year']}: ${t['market_B']:5d}B  -  {t['main']}")
    print(f"  Growth 2024-2050: {t1['growth_2024_2050']:.1f}x")
    print(f"\n  Segments (2024 $700B total):")
    for s in t1["segments_2024"]:
        print(f"    {s['name']:25s}  ${s['value_B']:4d}B  ({s['value_B']/700*100:.0f}%)")

    print("\n[Test 2] EU AI Act 2024 risk categories")
    t2 = test2_eu_ai_act()
    for c in t2["categories"]:
        cost_str = f"${c['compliance_cost']/1000:.0f}K" if c["compliance_cost"] > 0 else "—"
        print(f"  {c['level']:15s}  {c['n_use_cases']:3d} use cases  cost={cost_str}  -  {c['examples']}")

    print("\n[Test 3] Surveillance vs Privacy")
    t3 = test3_surveillance()
    for c in t3["countries"]:
        print(f"  {c['country']:12s}  surveillance={c['surveillance']:.2f}, privacy={c['privacy']:.2f}  -  {c['policy']}")

    print("\n[Test 4] Digital divide within cities")
    t4 = test4_digital_divide()
    for c in t4["cities"]:
        print(f"  {c['city']:15s}  high={c['high_income']:3d}%  mid={c['mid_income']:3d}%  low={c['low_income']:3d}%  divide={c['divide']:3d}%")

    out = {
        "phase": 105,
        "title": "Smart city economy, policy, surveillance ethics",
        "test1_market": t1,
        "test2_eu_ai_act": t2,
        "test3_surveillance": t3,
        "test4_digital_divide": t4,
    }
    with open("smartcity_economy_ethics_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: smartcity_economy_ethics_summary.json")

    make_figure(t1, t2, t3, t4, "smartcity_economy_ethics.png")
    print("  ✓ Figure saved: smartcity_economy_ethics.png")

    print("\n" + "=" * 70)
    print("Phase 105 complete: $3T market by 2050, EU AI Act 8 prohibited, surveillance polarized")
    print("=" * 70)
