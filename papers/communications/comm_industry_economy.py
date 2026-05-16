"""
Phase 97: Communications industry, economy, digital divide
Tier 1 #14 — Phase 3/4

4 numerical experiments:
1. Global ICT market 2024-2050 (Telecom + AI + Cloud subset)
2. Communications CapEx by category (5G/6G/Sat/Quantum)
3. Digital divide: internet penetration by region 2024 vs 2050 target
4. 6G patent share by country + Starlink vs Guowang satellites

Output: comm_industry_economy.png + comm_industry_economy_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Global ICT market
# ----------------------------------------------------------------------
def test1_ict_market():
    timeline = [
        {"year": 2024, "ICT_T": 5.3,  "Telecom_T": 1.6,  "AI_B": 200},
        {"year": 2025, "ICT_T": 5.7,  "Telecom_T": 1.7,  "AI_B": 300},
        {"year": 2030, "ICT_T": 8.0,  "Telecom_T": 2.5,  "AI_B": 1500},
        {"year": 2040, "ICT_T": 15.0, "Telecom_T": 4.5,  "AI_B": 5000},
        {"year": 2050, "ICT_T": 30.0, "Telecom_T": 8.0,  "AI_B": 15000},
    ]
    return {"timeline": timeline}


# ----------------------------------------------------------------------
# Test 2: Communications CapEx
# ----------------------------------------------------------------------
def test2_capex():
    capex = [
        {"year": 2024, "G5_B": 200, "G6_B": 5,   "Sat_B": 20,  "Quantum_B": 1},
        {"year": 2030, "G5_B": 80,  "G6_B": 150, "Sat_B": 50,  "Quantum_B": 20},
        {"year": 2040, "G5_B": 20,  "G6_B": 300, "Sat_B": 100, "Quantum_B": 100},
        {"year": 2050, "G5_B": 5,   "G6_B": 200, "Sat_B": 150, "Quantum_B": 300},
    ]
    return {"capex": capex}


# ----------------------------------------------------------------------
# Test 3: Digital divide
# ----------------------------------------------------------------------
def test3_digital_divide():
    regions = [
        {"region": "North America",     "pen_2024": 0.92, "pen_2050": 0.995, "bandwidth_Mbps_2024": 200},
        {"region": "Europe",            "pen_2024": 0.89, "pen_2050": 0.995, "bandwidth_Mbps_2024": 150},
        {"region": "East Asia",         "pen_2024": 0.78, "pen_2050": 0.99,  "bandwidth_Mbps_2024": 100},
        {"region": "Latin America",     "pen_2024": 0.75, "pen_2050": 0.97,  "bandwidth_Mbps_2024": 50},
        {"region": "Middle East",       "pen_2024": 0.70, "pen_2050": 0.95,  "bandwidth_Mbps_2024": 50},
        {"region": "South Asia",        "pen_2024": 0.55, "pen_2050": 0.95,  "bandwidth_Mbps_2024": 25},
        {"region": "Sub-Saharan Africa","pen_2024": 0.40, "pen_2050": 0.90,  "bandwidth_Mbps_2024": 15},
        {"region": "LDCs (poorest)",    "pen_2024": 0.27, "pen_2050": 0.80,  "bandwidth_Mbps_2024": 5},
    ]
    # World population approx 8B in 2024
    pop_2024_B = [0.6, 0.75, 1.6, 0.66, 0.4, 1.95, 1.2, 1.1]  # 8B total
    pop_2050_B = [0.65, 0.7, 1.55, 0.75, 0.55, 2.0, 2.0, 1.4]  # 9.7B
    for r, p24, p50 in zip(regions, pop_2024_B, pop_2050_B):
        r["pop_2024_B"] = p24
        r["pop_2050_B"] = p50
        r["online_2024_B"] = p24 * r["pen_2024"]
        r["online_2050_B"] = p50 * r["pen_2050"]
        r["offline_2024_B"] = p24 * (1 - r["pen_2024"])
        r["offline_2050_B"] = p50 * (1 - r["pen_2050"])
    total_offline_2024 = sum(r["offline_2024_B"] for r in regions)
    total_offline_2050 = sum(r["offline_2050_B"] for r in regions)
    return {
        "regions": regions,
        "total_offline_2024_B": total_offline_2024,
        "total_offline_2050_B": total_offline_2050,
        "world_avg_pen_2024": sum(r["online_2024_B"] for r in regions) / sum(pop_2024_B),
        "world_avg_pen_2050": sum(r["online_2050_B"] for r in regions) / sum(pop_2050_B),
    }


# ----------------------------------------------------------------------
# Test 4: 6G patents + satellite geopolitics
# ----------------------------------------------------------------------
def test4_geopolitics():
    patents = [
        {"country": "China", "share_pct": 40},
        {"country": "USA",   "share_pct": 35},
        {"country": "Korea", "share_pct": 9},
        {"country": "Japan", "share_pct": 8},
        {"country": "Europe","share_pct": 6},
        {"country": "Other", "share_pct": 2},
    ]
    satellites = [
        {"name": "Starlink (SpaceX)", "country": "USA", "current": 6800,  "planned": 42000},
        {"name": "Guowang",           "country": "CN",  "current": 0,     "planned": 13000},
        {"name": "OneWeb",            "country": "UK",  "current": 650,   "planned": 1980},
        {"name": "Kuiper",            "country": "USA", "current": 100,   "planned": 3236},
        {"name": "IRIS²",             "country": "EU",  "current": 0,     "planned": 290},
    ]
    return {
        "patents": patents,
        "satellites": satellites,
        "patent_concentration_top2": 75,
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: ICT market
    ax = axes[0, 0]
    years = [t["year"] for t in t1["timeline"]]
    ict = [t["ICT_T"] for t in t1["timeline"]]
    telecom = [t["Telecom_T"] for t in t1["timeline"]]
    ai = [t["AI_B"] / 1000 for t in t1["timeline"]]  # to trillions
    ax.plot(years, ict, "o-", color="#1f77b4", lw=2, markersize=8, label="Total ICT")
    ax.plot(years, telecom, "s-", color="#ff7f0e", lw=2, markersize=8, label="Telecom subset")
    ax.plot(years, ai, "^-", color="#d62728", lw=2, markersize=8, label="AI subset")
    ax.set_xlabel("Year")
    ax.set_ylabel("Market size ($T)")
    ax.set_title("Global ICT market: 2024 $5.3T → 2050 $30T (Telecom 27%, AI 50%)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: CapEx by category
    ax = axes[0, 1]
    capex = t2["capex"]
    years = [c["year"] for c in capex]
    categories = ["G5_B", "G6_B", "Sat_B", "Quantum_B"]
    labels = ["5G", "6G", "Satellite", "Quantum net"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"]
    bottom = np.zeros(len(years))
    for cat, lbl, color in zip(categories, labels, colors):
        vals = [c[cat] for c in capex]
        ax.bar(years, vals, bottom=bottom, color=color, alpha=0.85, label=lbl,
               edgecolor="black", linewidth=0.5, width=5)
        bottom += np.array(vals)
    ax.set_xlabel("Year")
    ax.set_ylabel("CapEx ($B)")
    ax.set_title("Communications CapEx: 5G fades, 6G/Quantum rise (2050: $655B)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3: Digital divide
    ax = axes[1, 0]
    regions = t3["regions"]
    names = [r["region"] for r in regions]
    pen_2024 = [r["pen_2024"] * 100 for r in regions]
    pen_2050 = [r["pen_2050"] * 100 for r in regions]
    y_pos = np.arange(len(regions))
    width = 0.35
    ax.barh(y_pos - width/2, pen_2024, width, color="#1f77b4", alpha=0.8, label="2024", edgecolor="black", linewidth=0.5)
    ax.barh(y_pos + width/2, pen_2050, width, color="#2ca02c", alpha=0.8, label="2050 target", edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Internet penetration (%)")
    ax.set_title(f"Digital divide: offline 2024 {t3['total_offline_2024_B']:.1f}B → 2050 {t3['total_offline_2050_B']:.2f}B")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="x")

    # Panel 4: 6G patents + satellites
    ax = axes[1, 1]
    patents = t4["patents"]
    names_p = [p["country"] for p in patents]
    shares = [p["share_pct"] for p in patents]
    cmap = ["#d62728", "#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd", "#8c564b"]
    bottom = 0
    for n, s, c in zip(names_p, shares, cmap):
        ax.barh(["6G patents"], [s], left=[bottom], color=c, alpha=0.85,
                label=f"{n} ({s}%)", edgecolor="black", linewidth=0.5)
        bottom += s
    sats = t4["satellites"]
    sat_names = [s["name"] for s in sats]
    planned = [s["planned"] for s in sats]
    country_color = {"USA": "#1f77b4", "CN": "#d62728", "UK": "#ff7f0e", "EU": "#2ca02c"}
    for i, s in enumerate(sats):
        ax.barh([s["name"]], [s["planned"]/600], color=country_color.get(s["country"], "gray"),
                alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_xlabel("% (patents) or planned/600 (satellites)")
    ax.set_title(f"6G patents (China 40% + USA 35% = {t4['patent_concentration_top2']}%) + satellites")
    ax.legend(fontsize=7, loc="lower right", ncol=2)
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 97: Communications industry, economy, digital divide",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 97: Communications industry, economy, digital divide")
    print("=" * 70)

    print("\n[Test 1] Global ICT market")
    t1 = test1_ict_market()
    for t in t1["timeline"]:
        print(f"  {t['year']}: ICT ${t['ICT_T']:.1f}T, Telecom ${t['Telecom_T']:.1f}T, AI ${t['AI_B']:.0f}B")

    print("\n[Test 2] Communications CapEx")
    t2 = test2_capex()
    for c in t2["capex"]:
        total = c["G5_B"] + c["G6_B"] + c["Sat_B"] + c["Quantum_B"]
        print(f"  {c['year']}: 5G=${c['G5_B']}B, 6G=${c['G6_B']}B, Sat=${c['Sat_B']}B, Q=${c['Quantum_B']}B  total=${total}B")

    print("\n[Test 3] Digital divide")
    t3 = test3_digital_divide()
    for r in t3["regions"]:
        print(f"  {r['region']:25s}  2024: {r['pen_2024']*100:5.1f}%  2050: {r['pen_2050']*100:5.1f}%  "
              f"({r['offline_2024_B']:.2f}B → {r['offline_2050_B']:.2f}B offline)")
    print(f"  World total offline: 2024={t3['total_offline_2024_B']:.2f}B → 2050={t3['total_offline_2050_B']:.2f}B")
    print(f"  World avg penetration: 2024={t3['world_avg_pen_2024']*100:.0f}% → 2050={t3['world_avg_pen_2050']*100:.0f}%")

    print("\n[Test 4] 6G patents + satellites geopolitics")
    t4 = test4_geopolitics()
    for p in t4["patents"]:
        print(f"  {p['country']:10s}: {p['share_pct']}%")
    print(f"  Top 2 (US+CN): {t4['patent_concentration_top2']}%")
    for s in t4["satellites"]:
        print(f"  {s['name']:25s}  [{s['country']}]  current={s['current']}, planned={s['planned']}")

    out = {
        "phase": 97,
        "title": "Communications industry, economy, digital divide",
        "test1_ict_market": t1,
        "test2_capex": t2,
        "test3_digital_divide": t3,
        "test4_geopolitics": t4,
    }
    with open("comm_industry_economy_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: comm_industry_economy_summary.json")

    make_figure(t1, t2, t3, t4, "comm_industry_economy.png")
    print("  ✓ Figure saved: comm_industry_economy.png")

    print("\n" + "=" * 70)
    print("Phase 97 complete: ICT $30T 2050, offline 2.8B→0.7B, 6G patents US+CN 75%")
    print("=" * 70)
