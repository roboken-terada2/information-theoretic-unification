"""
Phase 93: Embodied AGI — industry, economics, ethics
Tier 1 #13 — Phase 3/4

4 numerical experiments:
1. Embodied AGI 5-level adoption (L1-L6) + cumulative deployment 2025-2050
2. Humanoid price curve (Wright's Law) and market size
3. Industry-by-industry automation rate (2030 vs 2050)
4. Ethics: K_self degree thresholds for moral agency

Output: embodied_agi_industry.png + embodied_agi_industry_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: 5-level adoption + cumulative deployment
# ----------------------------------------------------------------------
def test1_adoption():
    levels = [
        {"level": "L1 Simple automation",   "period": "2024-2027", "K_degree": 0.03, "year_start": 2024},
        {"level": "L2 Structured tasks",    "period": "2027-2030", "K_degree": 0.10, "year_start": 2027},
        {"level": "L3 Household help",      "period": "2030-2034", "K_degree": 0.20, "year_start": 2030},
        {"level": "L4 Care + dialogue",     "period": "2034-2040", "K_degree": 0.50, "year_start": 2034},
        {"level": "L5 Professional",        "period": "2040-2050", "K_degree": 0.80, "year_start": 2040},
        {"level": "L6 Human-indistinguishable", "period": "2050+", "K_degree": 0.95, "year_start": 2050},
    ]
    # Cumulative deployment forecast
    years = np.arange(2025, 2051)
    deployment_anchors = [(2025, 1e5), (2027, 1e6), (2030, 1e7),
                          (2035, 1e8), (2040, 5e8), (2045, 1e9), (2050, 2e9)]
    yr_a = np.array([a[0] for a in deployment_anchors])
    dep_a = np.log10(np.array([a[1] for a in deployment_anchors]))
    log_dep = np.interp(years, yr_a, dep_a)
    deployment = 10 ** log_dep
    return {
        "levels": levels,
        "years": years.tolist(),
        "deployment_cumulative": deployment.tolist(),
        "deployment_2050": float(deployment[-1]),
        "per_capita_2050_humans": float(8e9 / deployment[-1]),
    }


# ----------------------------------------------------------------------
# Test 2: Price curve (Wright's Law) and market size
# ----------------------------------------------------------------------
def test2_price_market():
    """Wright's Law: cost ~ Q^(-0.32) (20% per doubling)"""
    years = np.arange(2024, 2051)
    # Cumulative production anchors
    prod_anchors = [(2024, 1e3), (2027, 1e5), (2030, 1e6),
                    (2035, 1e7), (2040, 1e8), (2050, 5e8)]
    yr_a = np.array([a[0] for a in prod_anchors])
    log_prod = np.interp(years, yr_a, np.log10([a[1] for a in prod_anchors]))
    prod = 10 ** log_prod
    # Price model: P0 = $200K at Q=1000. Wright slope -0.32
    P0 = 200000.0
    Q0 = 1000.0
    price = P0 * (prod / Q0) ** (-0.32)
    # Market size (annual production = derivative of cumulative)
    annual_production = np.diff(prod, prepend=prod[0])
    market_size = annual_production * price
    return {
        "years": years.tolist(),
        "cumulative_production": prod.tolist(),
        "price_USD": price.tolist(),
        "market_size_USD": market_size.tolist(),
        "price_2024": float(price[0]),
        "price_2030": float(price[np.where(years == 2030)[0][0]]),
        "price_2040": float(price[np.where(years == 2040)[0][0]]),
        "price_2050": float(price[-1]),
        "market_2030_B": float(market_size[np.where(years == 2030)[0][0]] / 1e9),
        "market_2040_B": float(market_size[np.where(years == 2040)[0][0]] / 1e9),
        "market_2050_B": float(market_size[-1] / 1e9),
    }


# ----------------------------------------------------------------------
# Test 3: Industry-by-industry automation
# ----------------------------------------------------------------------
def test3_automation_by_industry():
    industries = [
        {"name": "Warehouse/logistics", "auto_2030": 0.40, "auto_2050": 0.90, "workers_M_2024": 50},
        {"name": "Manufacturing",        "auto_2030": 0.30, "auto_2050": 0.80, "workers_M_2024": 400},
        {"name": "Trucking",             "auto_2030": 0.20, "auto_2050": 0.70, "workers_M_2024": 30},
        {"name": "Eldercare",            "auto_2030": 0.05, "auto_2050": 0.50, "workers_M_2024": 30},
        {"name": "Food service",         "auto_2030": 0.10, "auto_2050": 0.60, "workers_M_2024": 100},
        {"name": "Cleaning",             "auto_2030": 0.15, "auto_2050": 0.70, "workers_M_2024": 60},
        {"name": "Security",             "auto_2030": 0.25, "auto_2050": 0.65, "workers_M_2024": 20},
        {"name": "Banking (teller)",     "auto_2030": 0.60, "auto_2050": 0.95, "workers_M_2024": 10},
        {"name": "Surgery (assist)",     "auto_2030": 0.05, "auto_2050": 0.30, "workers_M_2024": 5},
        {"name": "Education (teacher)",  "auto_2030": 0.05, "auto_2050": 0.20, "workers_M_2024": 80},
    ]
    for ind in industries:
        ind["jobs_replaced_2030_M"] = ind["workers_M_2024"] * ind["auto_2030"]
        ind["jobs_replaced_2050_M"] = ind["workers_M_2024"] * ind["auto_2050"]
    total_2030 = sum(i["jobs_replaced_2030_M"] for i in industries)
    total_2050 = sum(i["jobs_replaced_2050_M"] for i in industries)
    total_workers = sum(i["workers_M_2024"] for i in industries)
    return {
        "industries": industries,
        "total_workers_2024_M": total_workers,
        "total_replaced_2030_M": total_2030,
        "total_replaced_2050_M": total_2050,
        "replacement_rate_2030": total_2030 / total_workers,
        "replacement_rate_2050": total_2050 / total_workers,
    }


# ----------------------------------------------------------------------
# Test 4: Ethics — K_self moral agency thresholds
# ----------------------------------------------------------------------
def test4_ethics_kself():
    """Robot rights and moral agency by K_self degree."""
    thresholds = [
        {"K_self": 0.05, "rights_level": "Property (machine)",   "year": 2024, "examples": "Industrial robots"},
        {"K_self": 0.20, "rights_level": "Animal welfare-like",  "year": 2030, "examples": "Advanced humanoid"},
        {"K_self": 0.40, "rights_level": "Partial personhood",   "year": 2040, "examples": "Embodied AGI"},
        {"K_self": 0.60, "rights_level": "Full personhood",      "year": 2050, "examples": "Embodied ASI"},
        {"K_self": 0.85, "rights_level": "Super-personhood",     "year": 2060, "examples": "Future ASI"},
    ]
    # Liability assignment by K_self
    def liability_share(K_self):
        if K_self < 0.2:
            return {"manufacturer": 0.8, "owner": 0.2, "robot": 0.0}
        elif K_self < 0.5:
            return {"manufacturer": 0.4, "owner": 0.4, "robot": 0.2}
        elif K_self < 0.8:
            return {"manufacturer": 0.2, "owner": 0.3, "robot": 0.5}
        else:
            return {"manufacturer": 0.1, "owner": 0.1, "robot": 0.8}

    liability_table = []
    for K in [0.05, 0.2, 0.4, 0.6, 0.85]:
        l = liability_share(K)
        l["K_self"] = K
        liability_table.append(l)
    return {
        "thresholds": thresholds,
        "liability_by_K_self": liability_table,
        "moral_agency_threshold_K_self": 0.5,
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Cumulative deployment + L1-L6 levels
    ax = axes[0, 0]
    years = np.array(t1["years"])
    deployment = np.array(t1["deployment_cumulative"])
    ax.semilogy(years, deployment, "b-", lw=2.5, alpha=0.85)
    ax.fill_between(years, 1, deployment, color="blue", alpha=0.15)
    # Mark levels
    for lvl in t1["levels"]:
        if lvl["year_start"] >= 2025 and lvl["year_start"] <= 2050:
            idx = np.where(years == lvl["year_start"])[0]
            if len(idx) > 0:
                y_val = deployment[idx[0]]
                ax.scatter(lvl["year_start"], y_val, s=120, c="red", marker="*", zorder=5)
                ax.annotate(f"{lvl['level'].split()[0]} (deg={lvl['K_degree']})",
                            (lvl["year_start"], y_val),
                            xytext=(5, 5), textcoords="offset points", fontsize=7)
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative humanoid deployment (log)")
    ax.set_title(f"Embodied AGI deployment | 2050 = {t1['deployment_2050']/1e9:.1f}B units = 1 per {t1['per_capita_2050_humans']:.1f} humans")
    ax.grid(alpha=0.3, which="both")

    # Panel 2: Price curve + market size
    ax = axes[0, 1]
    years = np.array(t2["years"])
    price = np.array(t2["price_USD"])
    market = np.array(t2["market_size_USD"])
    ax.semilogy(years, price, "g-", lw=2, label="Unit price ($)", alpha=0.85)
    ax.set_xlabel("Year")
    ax.set_ylabel("Unit price ($)", color="green")
    ax.tick_params(axis="y", labelcolor="green")
    ax2 = ax.twinx()
    ax2.semilogy(years, market / 1e9, "r-", lw=2, label="Market size ($B/yr)", alpha=0.85)
    ax2.set_ylabel("Market size ($B/yr)", color="red")
    ax2.tick_params(axis="y", labelcolor="red")
    ax.set_title(f"Wright's Law | 2024 $200K → 2050 ${t2['price_2050']:.0f} | Market 2050 ${t2['market_2050_B']:.0f}B")
    ax.grid(alpha=0.3, which="both")

    # Panel 3: Industry automation
    ax = axes[1, 0]
    industries = t3["industries"]
    names = [i["name"] for i in industries]
    auto_2030 = [i["auto_2030"] for i in industries]
    auto_2050 = [i["auto_2050"] for i in industries]
    y_pos = np.arange(len(industries))
    width = 0.35
    ax.barh(y_pos - width/2, auto_2030, width, color="#1f77b4", alpha=0.8, label="2030", edgecolor="black", linewidth=0.5)
    ax.barh(y_pos + width/2, auto_2050, width, color="#d62728", alpha=0.8, label="2050", edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Automation rate")
    ax.set_title(f"Industry automation | 2030 avg {t3['replacement_rate_2030']*100:.0f}%, 2050 avg {t3['replacement_rate_2050']*100:.0f}%")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="x")

    # Panel 4: Ethics — K_self thresholds
    ax = axes[1, 1]
    thresholds = t4["thresholds"]
    K_vals = [t["K_self"] for t in thresholds]
    years_t = [t["year"] for t in thresholds]
    labels = [t["rights_level"] for t in thresholds]
    cmap = plt.cm.viridis(np.linspace(0.1, 0.9, len(thresholds)))
    for i, (K, yr, lbl) in enumerate(zip(K_vals, years_t, labels)):
        ax.scatter(yr, K, s=300, c=[cmap[i]], alpha=0.85, edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(lbl, (yr, K), xytext=(7, 5), textcoords="offset points", fontsize=8)
    ax.axhline(t4["moral_agency_threshold_K_self"], ls="--", color="red", alpha=0.6,
               label=f"Moral agency threshold (K_self = {t4['moral_agency_threshold_K_self']})")
    ax.set_xlabel("Year")
    ax.set_ylabel("K_self degree")
    ax.set_ylim(0, 1.0)
    ax.set_title("Ethics: K_self thresholds → robot rights levels")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.suptitle("Phase 93: Embodied AGI — industry, economics, ethics",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 93: Embodied AGI — industry, economics, ethics")
    print("=" * 70)

    print("\n[Test 1] 5-level adoption + deployment")
    t1 = test1_adoption()
    for lvl in t1["levels"]:
        print(f"  {lvl['level']:32s}  {lvl['period']}  K_deg={lvl['K_degree']:.2f}")
    print(f"  Cumulative 2050: {t1['deployment_2050']/1e9:.2f}B units (1 per {t1['per_capita_2050_humans']:.1f} humans)")

    print("\n[Test 2] Price curve + market")
    t2 = test2_price_market()
    print(f"  Price 2024: ${t2['price_2024']:,.0f}")
    print(f"  Price 2030: ${t2['price_2030']:,.0f}")
    print(f"  Price 2040: ${t2['price_2040']:,.0f}")
    print(f"  Price 2050: ${t2['price_2050']:,.0f}")
    print(f"  Market 2030: ${t2['market_2030_B']:.1f}B")
    print(f"  Market 2040: ${t2['market_2040_B']:.1f}B")
    print(f"  Market 2050: ${t2['market_2050_B']:.0f}B")

    print("\n[Test 3] Industry automation")
    t3 = test3_automation_by_industry()
    for ind in t3["industries"]:
        print(f"  {ind['name']:25s}  workers={ind['workers_M_2024']:4d}M  auto 2030={ind['auto_2030']*100:3.0f}%  2050={ind['auto_2050']*100:3.0f}%")
    print(f"  Total workers (covered):    {t3['total_workers_2024_M']:.0f}M")
    print(f"  Jobs replaced 2030: {t3['total_replaced_2030_M']:.0f}M ({t3['replacement_rate_2030']*100:.0f}%)")
    print(f"  Jobs replaced 2050: {t3['total_replaced_2050_M']:.0f}M ({t3['replacement_rate_2050']*100:.0f}%)")

    print("\n[Test 4] Ethics K_self thresholds")
    t4 = test4_ethics_kself()
    for th in t4["thresholds"]:
        print(f"  K_self={th['K_self']:.2f}  {th['rights_level']:25s}  ({th['year']}, {th['examples']})")
    print(f"  Moral agency threshold: K_self = {t4['moral_agency_threshold_K_self']}")
    print(f"\n  Liability share by K_self:")
    for l in t4["liability_by_K_self"]:
        print(f"    K_self={l['K_self']:.2f}: manuf={l['manufacturer']*100:.0f}%, owner={l['owner']*100:.0f}%, robot={l['robot']*100:.0f}%")

    out = {
        "phase": 93,
        "title": "Embodied AGI — industry, economics, ethics",
        "test1_adoption": t1,
        "test2_price_market": {
            "price_2030": t2["price_2030"], "price_2050": t2["price_2050"],
            "market_2030_B": t2["market_2030_B"], "market_2050_B": t2["market_2050_B"],
            "years_subset": t2["years"][::5],
            "price_subset": t2["price_USD"][::5],
        },
        "test3_automation": t3,
        "test4_ethics": t4,
    }
    with open("embodied_agi_industry_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: embodied_agi_industry_summary.json")

    make_figure(t1, t2, t3, t4, "embodied_agi_industry.png")
    print("  ✓ Figure saved: embodied_agi_industry.png")

    print("\n" + "=" * 70)
    print("Phase 93 complete: 2050 deployment={:.1f}B units, market ${:.0f}B/yr, jobs replaced {:.0f}%"
          .format(t1["deployment_2050"]/1e9, t2["market_2050_B"], t3["replacement_rate_2050"]*100))
    print("=" * 70)
