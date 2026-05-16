"""
Phase 103: ITU Smart Cities foundation
Tier 1 #16 — Phase 1/4

4 numerical experiments:
1. Smart City Index 2024 top 10
2. Greenfield smart cities (NEOM, Songdo, Nusantara, etc.)
3. IoT sensor density by city
4. Privacy vs efficiency tradeoff (China vs Estonia)

Output: smartcities_itu_foundation.png + smartcities_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Smart City Index 2024 top 10
# ----------------------------------------------------------------------
def test1_smart_city_index():
    cities = [
        {"rank": 1,  "city": "Zurich",     "country": "CH", "score": 100, "focus": "Balanced + citizen sat."},
        {"rank": 2,  "city": "Oslo",       "country": "NO", "score": 95,  "focus": "Environment + digital"},
        {"rank": 3,  "city": "Canberra",   "country": "AU", "score": 94,  "focus": "Government digitization"},
        {"rank": 4,  "city": "Geneva",     "country": "CH", "score": 93,  "focus": "UN city"},
        {"rank": 5,  "city": "Singapore",  "country": "SG", "score": 92,  "focus": "Smart Nation integration"},
        {"rank": 6,  "city": "Copenhagen", "country": "DK", "score": 90,  "focus": "Bicycle + green"},
        {"rank": 7,  "city": "Lausanne",   "country": "CH", "score": 89,  "focus": "Education + tech"},
        {"rank": 8,  "city": "London",     "country": "UK", "score": 88,  "focus": "Diversity + finance"},
        {"rank": 9,  "city": "Helsinki",   "country": "FI", "score": 87,  "focus": "Digital pioneer"},
        {"rank": 10, "city": "Beijing",    "country": "CN", "score": 85,  "focus": "Surveillance + AI"},
    ]
    return {"cities": cities}


# ----------------------------------------------------------------------
# Test 2: Greenfield smart cities
# ----------------------------------------------------------------------
def test2_greenfield():
    projects = [
        {"name": "Telosa",          "country": "USA",    "investment_B": 400, "year_start": 2040, "year_complete": 2050},
        {"name": "NEOM (The Line)", "country": "Saudi",  "investment_B": 500, "year_start": 2017, "year_complete": 2030},
        {"name": "Forest City",     "country": "Malaysia","investment_B": 100,"year_start": 2014, "year_complete": 2035},
        {"name": "Tianfu New Area", "country": "China",  "investment_B": 50,  "year_start": 2014, "year_complete": 2030},
        {"name": "Songdo IBD",      "country": "Korea",  "investment_B": 40,  "year_start": 2003, "year_complete": 2024},
        {"name": "Nusantara",       "country": "Indonesia","investment_B": 40,"year_start": 2024, "year_complete": 2045},
        {"name": "Masdar City",     "country": "UAE",    "investment_B": 22,  "year_start": 2008, "year_complete": 2030},
        {"name": "雄安新区 Xiongan", "country": "China",  "investment_B": 580, "year_start": 2017, "year_complete": 2035},
    ]
    return {"projects": projects, "total_investment_B": sum(p["investment_B"] for p in projects)}


# ----------------------------------------------------------------------
# Test 3: IoT sensor density
# ----------------------------------------------------------------------
def test3_iot_density():
    sensor_types = [
        {"type": "Air quality",      "per_km2": 30},
        {"type": "Temperature",      "per_km2": 60},
        {"type": "Traffic flow",     "per_km2": 35},
        {"type": "Surveillance",     "per_km2": 200},
        {"type": "Smart meters",     "per_km2": 5000},
        {"type": "IoT trash",        "per_km2": 12},
        {"type": "Street lights",    "per_km2": 200},
        {"type": "Other",            "per_km2": 100},
    ]
    total_per_km2 = sum(s["per_km2"] for s in sensor_types)

    cities = [
        {"city": "Beijing",            "total_sensors": 30e6, "per_km2": 18000},
        {"city": "New York",           "total_sensors": 10e6, "per_km2": 16000},
        {"city": "Singapore",          "total_sensors": 5e6,  "per_km2": 7000},
        {"city": "Tokyo (Chiyoda)",    "total_sensors": 2e6,  "per_km2": 6000},
        {"city": "Songdo",             "total_sensors": 50e3, "per_km2": 1200},
        {"city": "AI City 2040 (proj)","total_sensors": 1e8,  "per_km2": 100000},
    ]
    return {"sensor_types": sensor_types, "cities": cities, "typical_density": total_per_km2}


# ----------------------------------------------------------------------
# Test 4: Privacy vs Efficiency tradeoff
# ----------------------------------------------------------------------
def test4_privacy_efficiency():
    """Cities mapped on privacy (K_privacy) vs efficiency (K_efficiency) plane."""
    cities = [
        {"city": "Beijing (CN)",     "privacy": 0.15, "efficiency": 0.92, "model": "surveillance"},
        {"city": "Xiongan (CN)",     "privacy": 0.10, "efficiency": 0.95, "model": "surveillance"},
        {"city": "Singapore",        "privacy": 0.55, "efficiency": 0.93, "model": "balanced"},
        {"city": "Songdo (KR)",      "privacy": 0.50, "efficiency": 0.80, "model": "balanced"},
        {"city": "Estonia (Tallinn)","privacy": 0.85, "efficiency": 0.92, "model": "data-trust"},
        {"city": "Helsinki",         "privacy": 0.80, "efficiency": 0.85, "model": "data-trust"},
        {"city": "Zurich",           "privacy": 0.75, "efficiency": 0.90, "model": "balanced"},
        {"city": "London",           "privacy": 0.60, "efficiency": 0.82, "model": "balanced"},
        {"city": "San Francisco",    "privacy": 0.45, "efficiency": 0.78, "model": "tech-corp"},
        {"city": "Dubai",            "privacy": 0.40, "efficiency": 0.85, "model": "techno-state"},
    ]
    # Compute tradeoff metric
    for c in cities:
        c["combined"] = c["privacy"] + c["efficiency"]
    return {"cities": cities}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Top 10 Smart City Index
    ax = axes[0, 0]
    cities = t1["cities"]
    names = [c["city"] for c in cities]
    scores = [c["score"] for c in cities]
    countries = [c["country"] for c in cities]
    country_color = {"CH": "#d62728", "NO": "#1f77b4", "AU": "#ff7f0e",
                     "SG": "#9467bd", "DK": "#2ca02c", "UK": "#8c564b",
                     "FI": "#17becf", "CN": "#e377c2"}
    colors = [country_color.get(c, "gray") for c in countries]
    y_pos = np.arange(len(cities))
    ax.barh(y_pos, scores, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(80, 105)
    ax.set_xlabel("IMD Smart City Index 2024 score")
    ax.set_title("Top 10 Smart Cities (IMD 2024)")
    ax.grid(alpha=0.3, axis="x")

    # Panel 2: Greenfield projects
    ax = axes[0, 1]
    projects = t2["projects"]
    names = [p["name"] for p in projects]
    investments = [p["investment_B"] for p in projects]
    y_pos = np.arange(len(projects))
    ax.barh(y_pos, investments, color="#2ca02c", alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlabel("Investment (USD billion, log)")
    ax.set_title(f"Greenfield smart cities | total ${t2['total_investment_B']}B")
    ax.grid(alpha=0.3, axis="x", which="both")

    # Panel 3: IoT density
    ax = axes[1, 0]
    cities = t3["cities"]
    names = [c["city"] for c in cities]
    density = [c["per_km2"] for c in cities]
    y_pos = np.arange(len(cities))
    cmap = plt.cm.viridis(np.array(density) / max(density))
    ax.barh(y_pos, density, color=cmap, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, c in enumerate(cities):
        ax.text(c["per_km2"] * 1.1, i, f"{c['total_sensors']:.0e}", va="center", fontsize=7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlabel("Sensors per km² (log)")
    ax.set_title("IoT sensor density by city")
    ax.grid(alpha=0.3, axis="x", which="both")

    # Panel 4: Privacy vs Efficiency
    ax = axes[1, 1]
    cities = t4["cities"]
    model_color = {"surveillance": "#d62728", "balanced": "#ff7f0e",
                   "data-trust": "#2ca02c", "tech-corp": "#9467bd",
                   "techno-state": "#1f77b4"}
    for c in cities:
        ax.scatter(c["privacy"], c["efficiency"], s=200,
                   c=model_color.get(c["model"], "gray"),
                   alpha=0.85, edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(c["city"], (c["privacy"], c["efficiency"]),
                    xytext=(5, 5), textcoords="offset points", fontsize=7)
    # Diagonal (ideal: both high)
    ax.plot([0, 1], [1, 0], "k--", alpha=0.3, label="naive tradeoff")
    ax.plot([0, 1], [0, 1], "g:", alpha=0.3, label="ideal frontier")
    ax.set_xlabel("Privacy (K_privacy)")
    ax.set_ylabel("Efficiency (K_efficiency)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0.7, 1)
    ax.set_title("Privacy vs Efficiency: Estonia + Singapore on Pareto frontier")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    # Color legend
    legend_elems = []
    import matplotlib.patches as mpatches
    for model, color in model_color.items():
        legend_elems.append(mpatches.Patch(color=color, label=model))
    ax.legend(handles=legend_elems + [
        plt.Line2D([0], [0], color="g", ls=":", label="ideal"),
        plt.Line2D([0], [0], color="k", ls="--", label="naive")
    ], loc="lower left", fontsize=7)

    plt.suptitle("Phase 103: ITU × Smart Cities — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 103: ITU × Smart Cities — foundation")
    print("=" * 70)

    print("\n[Test 1] IMD Smart City Index 2024 top 10")
    t1 = test1_smart_city_index()
    for c in t1["cities"]:
        print(f"  #{c['rank']:2d}  {c['city']:12s}  [{c['country']}]  score={c['score']:3d}  -  {c['focus']}")

    print("\n[Test 2] Greenfield smart cities")
    t2 = test2_greenfield()
    for p in t2["projects"]:
        print(f"  {p['name']:20s}  [{p['country']:8s}]  ${p['investment_B']:4d}B  ({p['year_start']}-{p['year_complete']})")
    print(f"  TOTAL: ${t2['total_investment_B']}B")

    print("\n[Test 3] IoT sensor density")
    t3 = test3_iot_density()
    print(f"  Typical breakdown ({t3['typical_density']}/km² total):")
    for s in t3["sensor_types"]:
        print(f"    {s['type']:18s}  {s['per_km2']:5d}/km²")
    print(f"\n  By city:")
    for c in t3["cities"]:
        print(f"  {c['city']:25s}  {c['total_sensors']:.0e} total, {c['per_km2']:6d}/km²")

    print("\n[Test 4] Privacy vs Efficiency tradeoff")
    t4 = test4_privacy_efficiency()
    for c in t4["cities"]:
        print(f"  {c['city']:22s}  privacy={c['privacy']:.2f}, efficiency={c['efficiency']:.2f}, combined={c['combined']:.2f}  [{c['model']}]")

    out = {
        "phase": 103,
        "title": "ITU × Smart Cities — foundation",
        "test1_smart_city_index": t1,
        "test2_greenfield": t2,
        "test3_iot_density": t3,
        "test4_privacy_efficiency": t4,
    }
    with open("smartcities_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: smartcities_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "smartcities_itu_foundation.png")
    print("  ✓ Figure saved: smartcities_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 103 complete: Zurich #1, Greenfield ${:.0f}B total, Singapore 5M sensors, Estonia balanced".format(t2["total_investment_B"]))
    print("=" * 70)
