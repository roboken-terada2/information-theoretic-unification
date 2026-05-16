"""
Phase 99: ITU Infrastructure / Power Grid foundation
Tier 1 #15 — Phase 1/4

4 numerical experiments:
1. Global infrastructure capital stock by category (8 sectors)
2. Power consumption + grid inertia trends 1990-2050
3. Aging infrastructure: K_decay vs K_invest dynamics
4. ASCE 2021 USA infrastructure report card

Output: infrastructure_itu_foundation.png + infrastructure_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Global infrastructure capital stock
# ----------------------------------------------------------------------
def test1_capital_stock():
    sectors = [
        {"name": "Buildings",         "stock_T": 200, "renewal_T_yr": 5.0},
        {"name": "Roads & Bridges",   "stock_T": 50,  "renewal_T_yr": 2.0},
        {"name": "Power Grid",        "stock_T": 30,  "renewal_T_yr": 1.0},
        {"name": "Water & Sewage",    "stock_T": 25,  "renewal_T_yr": 0.8},
        {"name": "Rail",              "stock_T": 15,  "renewal_T_yr": 0.5},
        {"name": "Ports & Airports",  "stock_T": 10,  "renewal_T_yr": 0.4},
        {"name": "Telecom",           "stock_T": 5,   "renewal_T_yr": 0.3},
        {"name": "Gas & Pipelines",   "stock_T": 5,   "renewal_T_yr": 0.2},
    ]
    total_stock = sum(s["stock_T"] for s in sectors)
    total_renewal = sum(s["renewal_T_yr"] for s in sectors)
    for s in sectors:
        s["renewal_rate_pct"] = s["renewal_T_yr"] / s["stock_T"] * 100
    return {
        "sectors": sectors,
        "total_stock_T": total_stock,
        "total_renewal_T_yr": total_renewal,
        "world_GDP_2024_T": 105.0,
        "stock_to_GDP_ratio": total_stock / 105.0,
    }


# ----------------------------------------------------------------------
# Test 2: Power consumption + grid inertia
# ----------------------------------------------------------------------
def test2_power_inertia():
    timeline = [
        {"year": 1990, "power_TWh": 11800, "sync_share": 0.95, "inertia_H_s": 6.0},
        {"year": 2000, "power_TWh": 15500, "sync_share": 0.92, "inertia_H_s": 5.8},
        {"year": 2010, "power_TWh": 22000, "sync_share": 0.85, "inertia_H_s": 5.5},
        {"year": 2020, "power_TWh": 27000, "sync_share": 0.75, "inertia_H_s": 4.5},
        {"year": 2024, "power_TWh": 30000, "sync_share": 0.70, "inertia_H_s": 4.0},
        {"year": 2030, "power_TWh": 38000, "sync_share": 0.55, "inertia_H_s": 3.0},
        {"year": 2040, "power_TWh": 50000, "sync_share": 0.35, "inertia_H_s": 2.0},
        {"year": 2050, "power_TWh": 70000, "sync_share": 0.20, "inertia_H_s": 1.5},
    ]
    # Inertia danger threshold
    safe_threshold = 2.5  # seconds
    for t in timeline:
        t["below_safe"] = t["inertia_H_s"] < safe_threshold
    return {
        "timeline": timeline,
        "safe_threshold_s": safe_threshold,
        "power_2024_2050_ratio": 70000 / 30000,
    }


# ----------------------------------------------------------------------
# Test 3: K_decay vs K_invest dynamics
# ----------------------------------------------------------------------
def test3_decay_invest():
    """Simulate K_cap evolution with different investment rates."""
    decay_rate = 0.025  # 2.5%/yr natural decay
    initial_cap = 100.0
    years = np.arange(0, 51)

    scenarios = [
        {"name": "Maintained (3%)",    "invest_rate": 0.03,  "color": "#2ca02c"},
        {"name": "Sustainable (2.5%)", "invest_rate": 0.025, "color": "#1f77b4"},
        {"name": "USA actual (1.5%)",  "invest_rate": 0.015, "color": "#ff7f0e"},
        {"name": "Underfunded (1%)",   "invest_rate": 0.010, "color": "#d62728"},
    ]
    out = []
    for sc in scenarios:
        K = np.zeros(len(years))
        K[0] = initial_cap
        for i in range(1, len(years)):
            # dK/dt = invest * initial - decay * K (net constant investment)
            K[i] = K[i-1] + sc["invest_rate"] * initial_cap - decay_rate * K[i-1]
        out.append({
            "name": sc["name"],
            "color": sc["color"],
            "invest_rate": sc["invest_rate"],
            "K_curve": K.tolist(),
            "K_50yr": float(K[-1]),
            "decline_pct": float((1 - K[-1] / K[0]) * 100),
        })
    return {
        "years": years.tolist(),
        "scenarios": out,
        "decay_rate": decay_rate,
        "initial_cap": initial_cap,
    }


# ----------------------------------------------------------------------
# Test 4: ASCE 2021 report card
# ----------------------------------------------------------------------
def test4_asce_report():
    categories = [
        {"name": "Aviation",         "grade": "D+", "score": 1.3, "need_10yr_B": 76},
        {"name": "Bridges",          "grade": "C",  "score": 2.0, "need_10yr_B": 125},
        {"name": "Dams",             "grade": "D",  "score": 1.0, "need_10yr_B": 94},
        {"name": "Drinking Water",   "grade": "C-", "score": 1.7, "need_10yr_B": 470},
        {"name": "Energy",           "grade": "C-", "score": 1.7, "need_10yr_B": 200},
        {"name": "Hazardous Waste",  "grade": "D+", "score": 1.3, "need_10yr_B": 40},
        {"name": "Levees",           "grade": "D",  "score": 1.0, "need_10yr_B": 80},
        {"name": "Ports",            "grade": "B-", "score": 2.7, "need_10yr_B": 25},
        {"name": "Public Parks",     "grade": "D+", "score": 1.3, "need_10yr_B": 47},
        {"name": "Rail",             "grade": "B",  "score": 3.0, "need_10yr_B": 105},
        {"name": "Roads",            "grade": "D",  "score": 1.0, "need_10yr_B": 1000},
        {"name": "Schools",          "grade": "D+", "score": 1.3, "need_10yr_B": 380},
        {"name": "Stormwater",       "grade": "D",  "score": 1.0, "need_10yr_B": 21},
        {"name": "Transit",          "grade": "D-", "score": 0.7, "need_10yr_B": 176},
        {"name": "Wastewater",       "grade": "D+", "score": 1.3, "need_10yr_B": 271},
    ]
    total_need = sum(c["need_10yr_B"] for c in categories)
    avg_score = float(np.mean([c["score"] for c in categories]))
    return {
        "categories": categories,
        "total_need_10yr_B": total_need,
        "overall_grade": "D+",
        "avg_score": avg_score,
        "n_categories": len(categories),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Infrastructure capital stock
    ax = axes[0, 0]
    sectors = t1["sectors"]
    names = [s["name"] for s in sectors]
    stocks = [s["stock_T"] for s in sectors]
    y_pos = np.arange(len(sectors))
    ax.barh(y_pos, stocks, color="#1f77b4", alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, s in enumerate(sectors):
        ax.text(s["stock_T"] + 5, i, f"{s['renewal_rate_pct']:.1f}%/yr", va="center", fontsize=7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Capital stock (USD trillion)")
    ax.set_title(f"Global infrastructure: ${t1['total_stock_T']:.0f}T total = {t1['stock_to_GDP_ratio']:.1f}x GDP")
    ax.grid(alpha=0.3, axis="x")

    # Panel 2: Power + Inertia
    ax = axes[0, 1]
    years = [t["year"] for t in t2["timeline"]]
    power = [t["power_TWh"] for t in t2["timeline"]]
    inertia = [t["inertia_H_s"] for t in t2["timeline"]]
    ax.plot(years, power, "o-", color="#1f77b4", lw=2, markersize=8, label="Power TWh/yr")
    ax.set_xlabel("Year")
    ax.set_ylabel("Power (TWh/year)", color="#1f77b4")
    ax.tick_params(axis="y", labelcolor="#1f77b4")
    ax2 = ax.twinx()
    ax2.plot(years, inertia, "s-", color="#d62728", lw=2, markersize=8, label="Inertia H (s)")
    ax2.axhline(t2["safe_threshold_s"], ls="--", color="darkred", alpha=0.5, label="Safe threshold")
    ax2.set_ylabel("Grid inertia H (s)", color="#d62728")
    ax2.tick_params(axis="y", labelcolor="#d62728")
    ax.set_title(f"Power demand vs grid inertia: 2050 1.5s (DANGER) vs 1990 6.0s")
    ax.grid(alpha=0.3)

    # Panel 3: K_decay dynamics
    ax = axes[1, 0]
    years = np.array(t3["years"])
    for sc in t3["scenarios"]:
        ax.plot(years, sc["K_curve"], color=sc["color"], lw=2,
                label=f"{sc['name']} → {sc['decline_pct']:+.0f}%", alpha=0.85)
    ax.axhline(t3["initial_cap"], ls=":", color="black", alpha=0.5, label="Initial (100)")
    ax.set_xlabel("Year")
    ax.set_ylabel("K_cap (normalized)")
    ax.set_title(f"K_capital dynamics: decay {t3['decay_rate']*100:.1f}%/yr, invest 1-3%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4: ASCE report
    ax = axes[1, 1]
    cats = t4["categories"]
    names = [c["name"] for c in cats]
    needs = [c["need_10yr_B"] for c in cats]
    grades = [c["grade"] for c in cats]
    colors_grade = {"A": "#2ca02c", "B-": "#90EE90", "B": "#90EE90", "C-": "#FFD700",
                    "C": "#FFD700", "D-": "#FF6347", "D": "#FF6347", "D+": "#FF6347"}
    colors = [colors_grade.get(g, "gray") for g in grades]
    y_pos = np.arange(len(cats))
    ax.barh(y_pos, needs, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, c in enumerate(cats):
        ax.text(c["need_10yr_B"] + 20, i, c["grade"], va="center", fontsize=7, fontweight="bold")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel("10-year need ($B)")
    ax.set_title(f"ASCE 2021 USA report: D+ overall, ${t4['total_need_10yr_B']:.0f}B total need")
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 99: ITU × Infrastructure / Power Grid — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 99: ITU × Infrastructure / Power Grid — foundation")
    print("=" * 70)

    print("\n[Test 1] Global infrastructure capital stock")
    t1 = test1_capital_stock()
    for s in t1["sectors"]:
        print(f"  {s['name']:25s}  stock=${s['stock_T']:5.0f}T  renew=${s['renewal_T_yr']:.2f}T/yr ({s['renewal_rate_pct']:.1f}%)")
    print(f"  TOTAL: ${t1['total_stock_T']:.0f}T (= {t1['stock_to_GDP_ratio']:.1f}x world GDP)")
    print(f"  Annual renewal: ${t1['total_renewal_T_yr']:.1f}T")

    print("\n[Test 2] Power consumption + grid inertia")
    t2 = test2_power_inertia()
    for t in t2["timeline"]:
        flag = "⚠️" if t["below_safe"] else "✓"
        print(f"  {t['year']}: power={t['power_TWh']:6d} TWh, sync={t['sync_share']*100:.0f}%, H={t['inertia_H_s']:.1f}s {flag}")
    print(f"  Safe threshold: H >= {t2['safe_threshold_s']}s")
    print(f"  Power 2024→2050 growth: {t2['power_2024_2050_ratio']:.1f}x")

    print("\n[Test 3] K_decay vs K_invest dynamics")
    t3 = test3_decay_invest()
    for sc in t3["scenarios"]:
        print(f"  {sc['name']:25s}  invest={sc['invest_rate']*100:.1f}%  K(50yr)={sc['K_50yr']:.0f}  ({sc['decline_pct']:+.0f}%)")

    print("\n[Test 4] ASCE 2021 USA infrastructure report")
    t4 = test4_asce_report()
    for c in t4["categories"]:
        print(f"  {c['name']:20s}  grade={c['grade']:2s}  need=${c['need_10yr_B']:5.0f}B")
    print(f"  Total 10-year need: ${t4['total_need_10yr_B']:.0f}B = ${t4['total_need_10yr_B']/1000:.2f}T")
    print(f"  Overall grade: {t4['overall_grade']}, avg score: {t4['avg_score']:.2f}")

    out = {
        "phase": 99,
        "title": "ITU × Infrastructure / Power Grid — foundation",
        "test1_capital_stock": t1,
        "test2_power_inertia": t2,
        "test3_decay_invest": {
            "decay_rate": t3["decay_rate"],
            "scenarios_summary": [{"name": s["name"], "invest": s["invest_rate"],
                                  "K_50yr": s["K_50yr"], "decline_pct": s["decline_pct"]}
                                 for s in t3["scenarios"]],
        },
        "test4_asce": t4,
    }
    with open("infrastructure_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: infrastructure_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "infrastructure_itu_foundation.png")
    print("  ✓ Figure saved: infrastructure_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 99 complete: $340T global stock, 2050 inertia 1.5s (CRITICAL), ASCE D+")
    print("=" * 70)
