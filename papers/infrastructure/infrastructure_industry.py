"""
Phase 101: Infrastructure industry, policy, international comparison
Tier 1 #15 — Phase 3/4

4 numerical experiments:
1. G7 + BRICS infrastructure investment 2024
2. Major policy frameworks (IIJA, IRA, NextGenEU, Xinjianjie)
3. PPP global market evolution
4. Climate adaptation costs by category (IPCC AR6)

Output: infrastructure_industry.png + infrastructure_industry_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: International infrastructure investment
# ----------------------------------------------------------------------
def test1_intl_investment():
    countries = [
        {"name": "China",   "investment_B": 1500, "GDP_T": 18.5, "focus": "新基建 + 一帯一路"},
        {"name": "USA",     "investment_B": 600,  "GDP_T": 25.0, "focus": "IIJA + IRA"},
        {"name": "Japan",   "investment_B": 300,  "GDP_T": 5.0,  "focus": "国土強靭化"},
        {"name": "India",   "investment_B": 250,  "GDP_T": 3.5,  "focus": "NIP, smart cities"},
        {"name": "Germany", "investment_B": 150,  "GDP_T": 4.5,  "focus": "Energy transition"},
        {"name": "UK",      "investment_B": 100,  "GDP_T": 3.0,  "focus": "National Infrastructure"},
        {"name": "France",  "investment_B": 80,   "GDP_T": 3.0,  "focus": "Green transition"},
        {"name": "Korea",   "investment_B": 80,   "GDP_T": 2.0,  "focus": "Smart cities, KNet"},
        {"name": "Brazil",  "investment_B": 50,   "GDP_T": 2.1,  "focus": "PAC + 新北部廊"},
        {"name": "Russia",  "investment_B": 40,   "GDP_T": 1.8,  "focus": "Eastern corridor"},
    ]
    for c in countries:
        c["GDP_pct"] = c["investment_B"] / (c["GDP_T"] * 1000) * 100
    total = sum(c["investment_B"] for c in countries)
    return {"countries": countries, "total_B": total}


# ----------------------------------------------------------------------
# Test 2: Policy framework budgets
# ----------------------------------------------------------------------
def test2_policies():
    policies = [
        {"name": "China 新基建 (2020-2025)",     "country": "CN", "budget_B": 1400, "years": 5,  "category": "New infrastructure"},
        {"name": "US IIJA (2021-2031)",           "country": "USA","budget_B": 1200, "years": 10, "category": "Traditional infra"},
        {"name": "EU NextGenerationEU",           "country": "EU", "budget_B": 800,  "years": 5,  "category": "Recovery + green"},
        {"name": "US IRA Clean Energy",           "country": "USA","budget_B": 369,  "years": 10, "category": "Climate"},
        {"name": "EU RePowerEU",                  "country": "EU", "budget_B": 320,  "years": 4,  "category": "Energy independence"},
        {"name": "Japan 国土強靭化 (5yr)",          "country": "JP", "budget_B": 100,  "years": 5,  "category": "Disaster + aging"},
        {"name": "India NIP",                     "country": "IN", "budget_B": 1300, "years": 5,  "category": "All sectors"},
        {"name": "UK National Infrastructure",    "country": "UK", "budget_B": 650,  "years": 10, "category": "Comprehensive"},
    ]
    return {"policies": policies}


# ----------------------------------------------------------------------
# Test 3: PPP global market
# ----------------------------------------------------------------------
def test3_ppp():
    timeline = [
        {"year": 2000, "investment_B": 20,  "projects": 50},
        {"year": 2005, "investment_B": 50,  "projects": 100},
        {"year": 2010, "investment_B": 100, "projects": 200},
        {"year": 2015, "investment_B": 130, "projects": 270},
        {"year": 2020, "investment_B": 150, "projects": 350},
        {"year": 2024, "investment_B": 200, "projects": 400},
        {"year": 2030, "investment_B": 300, "projects": 600},
        {"year": 2040, "investment_B": 450, "projects": 900},
        {"year": 2050, "investment_B": 600, "projects": 1200},
    ]
    return {"timeline": timeline}


# ----------------------------------------------------------------------
# Test 4: Climate adaptation costs (IPCC AR6)
# ----------------------------------------------------------------------
def test4_climate_adaptation():
    categories = [
        {"name": "Sea-level defense",    "cost_T": 1.0,  "examples": "Venice MOSE, Delta Works"},
        {"name": "Flood protection",     "cost_T": 0.8,  "examples": "River works, retention basins"},
        {"name": "Heat wave response",   "cost_T": 0.5,  "examples": "Urban cooling, greenery"},
        {"name": "Drought response",     "cost_T": 0.7,  "examples": "Desalination, conservation"},
        {"name": "Wildfire response",    "cost_T": 0.3,  "examples": "Firebreaks, suppression"},
        {"name": "Ecosystem restoration","cost_T": 0.4,  "examples": "Wetlands, reefs"},
        {"name": "Agriculture adaption", "cost_T": 0.6,  "examples": "Heat-tolerant crops, irrigation"},
        {"name": "Health systems",       "cost_T": 0.2,  "examples": "Heat response, vector control"},
    ]
    total_T = sum(c["cost_T"] for c in categories)
    # Major city projects
    cities = [
        {"city": "Singapore",     "project": "Coastal defense + Coastal Park", "B": 100, "year": 2100},
        {"city": "Tokyo",         "project": "Super levee + underground basin", "B": 30,  "year": 2030},
        {"city": "New York",      "project": "The Big U",                      "B": 20,  "year": 2050},
        {"city": "Netherlands",   "project": "Delta Works expansion",          "B": 15,  "year": 2050},
        {"city": "Venice",        "project": "MOSE",                           "B": 7,   "year": 2024},
        {"city": "Jakarta",       "project": "Nusantara new capital",          "B": 40,  "year": 2045},
    ]
    return {
        "categories": categories,
        "total_T": total_T,
        "cities": cities,
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: International investment
    ax = axes[0, 0]
    countries = t1["countries"]
    names = [c["name"] for c in countries]
    inv = [c["investment_B"] for c in countries]
    gdp_pct = [c["GDP_pct"] for c in countries]
    y_pos = np.arange(len(countries))
    cmap = plt.cm.viridis(np.array(gdp_pct) / max(gdp_pct))
    ax.barh(y_pos, inv, color=cmap, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, c in enumerate(countries):
        ax.text(c["investment_B"] + 20, i, f"{c['GDP_pct']:.1f}%", va="center", fontsize=8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Investment ($B/yr)")
    ax.set_title(f"2024 Infrastructure investment | China \\$1.5T (8% GDP), total \\${t1['total_B']:,}B")
    ax.grid(alpha=0.3, axis="x")

    # Panel 2: Policy frameworks
    ax = axes[0, 1]
    policies = t2["policies"]
    names = [p["name"][:30] for p in policies]
    budgets = [p["budget_B"] for p in policies]
    country_color = {"USA": "#1f77b4", "CN": "#d62728", "EU": "#2ca02c",
                     "JP": "#ff7f0e", "IN": "#9467bd", "UK": "#8c564b"}
    colors = [country_color.get(p["country"], "gray") for p in policies]
    y_pos = np.arange(len(policies))
    ax.barh(y_pos, budgets, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel("Total budget ($B)")
    ax.set_title("Major infrastructure policy frameworks (cumulative budgets)")
    ax.grid(alpha=0.3, axis="x")

    # Panel 3: PPP evolution
    ax = axes[1, 0]
    timeline = t3["timeline"]
    years = [t["year"] for t in timeline]
    inv_B = [t["investment_B"] for t in timeline]
    proj = [t["projects"] for t in timeline]
    ax.plot(years, inv_B, "o-", color="#1f77b4", lw=2, markersize=8, label="Investment ($B)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Investment ($B)", color="#1f77b4")
    ax.tick_params(axis="y", labelcolor="#1f77b4")
    ax2 = ax.twinx()
    ax2.plot(years, proj, "s-", color="#d62728", lw=2, markersize=8, label="Projects")
    ax2.set_ylabel("Projects", color="#d62728")
    ax2.tick_params(axis="y", labelcolor="#d62728")
    ax.set_title("PPP global market: $20B (2000) → $600B (2050)")
    ax.grid(alpha=0.3)

    # Panel 4: Climate adaptation costs
    ax = axes[1, 1]
    cats = t4["categories"]
    names = [c["name"] for c in cats]
    costs = [c["cost_T"] for c in cats]
    y_pos = np.arange(len(cats))
    cmap = plt.cm.plasma(np.array(costs) / max(costs))
    ax.barh(y_pos, costs, color=cmap, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Cumulative cost 2050 ($T)")
    ax.set_title(f"Climate adaptation: ${t4['total_T']:.1f}T total (IPCC AR6)")
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 101: Infrastructure industry, policy, international comparison",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 101: Infrastructure industry, policy, international comparison")
    print("=" * 70)

    print("\n[Test 1] International infrastructure investment")
    t1 = test1_intl_investment()
    for c in t1["countries"]:
        print(f"  {c['name']:10s}  ${c['investment_B']:5d}B  ({c['GDP_pct']:.1f}% GDP)  -  {c['focus']}")
    print(f"  TOTAL: ${t1['total_B']:,}B")

    print("\n[Test 2] Major policy frameworks")
    t2 = test2_policies()
    for p in t2["policies"]:
        print(f"  {p['name']:35s}  [{p['country']:3s}]  ${p['budget_B']:5d}B  ({p['years']}yr)  -  {p['category']}")

    print("\n[Test 3] PPP global market")
    t3 = test3_ppp()
    for t in t3["timeline"]:
        print(f"  {t['year']}: ${t['investment_B']:4d}B  {t['projects']:5d} projects")

    print("\n[Test 4] Climate adaptation (IPCC AR6)")
    t4 = test4_climate_adaptation()
    for c in t4["categories"]:
        print(f"  {c['name']:30s}  ${c['cost_T']:.1f}T  -  {c['examples']}")
    print(f"  TOTAL: ${t4['total_T']:.1f}T")
    print(f"\n  Major city projects:")
    for city in t4["cities"]:
        print(f"  {city['city']:15s}  {city['project']:38s}  ${city['B']:4d}B  ({city['year']})")

    out = {
        "phase": 101,
        "title": "Infrastructure industry, policy, international comparison",
        "test1_intl_investment": t1,
        "test2_policies": t2,
        "test3_ppp": t3,
        "test4_climate_adaptation": t4,
    }
    with open("infrastructure_industry_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: infrastructure_industry_summary.json")

    make_figure(t1, t2, t3, t4, "infrastructure_industry.png")
    print("  ✓ Figure saved: infrastructure_industry.png")

    print("\n" + "=" * 70)
    print("Phase 101 complete: China $1.5T/yr leads, PPP $600B by 2050, climate adapt $4.5T")
    print("=" * 70)
