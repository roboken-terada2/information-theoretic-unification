"""
Phase 86: Climate roadmap 2026-2100 + Tier 1 #11 summary
Tier 1 #11 — Phase 4/4 (final)

4 numerical experiments:
1. Integrated 2026-2100 roadmap timeline visualization
2. 10 falsifiable predictions with probabilities
3. ITU 11-vertex polytope connectivity map
4. Tier 1 #11 cross-paper integration metrics

Output: climate_roadmap.png + climate_roadmap_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

# ----------------------------------------------------------------------
# Test 1: Roadmap milestones
# ----------------------------------------------------------------------
def test1_roadmap():
    milestones = [
        {"year": 2024, "label": "CO2 422 ppm", "category": "obs", "status": "done"},
        {"year": 2024, "label": "EEI 1.0 W/m²", "category": "obs", "status": "done"},
        {"year": 2025, "label": "TRUTHS satellite", "category": "obs", "status": "planned"},
        {"year": 2026, "label": "COP31 emissions peak check", "category": "policy", "status": "planned"},
        {"year": 2028, "label": "DAC 100 kt CO2/yr", "category": "tech", "status": "planned"},
        {"year": 2030, "label": "Global emissions peak ⏳", "category": "milestone", "status": "predicted"},
        {"year": 2030, "label": "Renewables 31% share", "category": "milestone", "status": "predicted"},
        {"year": 2032, "label": "AMOC EWS strengthened", "category": "obs", "status": "predicted"},
        {"year": 2035, "label": "AGI → climate model 1000×", "category": "tech", "status": "predicted"},
        {"year": 2035, "label": "Solar LCOE $20/MWh", "category": "tech", "status": "predicted"},
        {"year": 2040, "label": "CO2 peak 480-500 ppm", "category": "milestone", "status": "predicted"},
        {"year": 2040, "label": "DAC 1 GtCO2/yr commercial", "category": "tech", "status": "predicted"},
        {"year": 2045, "label": "Greenland EWS detectable", "category": "tipping", "status": "predicted"},
        {"year": 2050, "label": "NZE major countries ★", "category": "milestone", "status": "predicted"},
        {"year": 2050, "label": "CDR 10 GtCO2/yr (target)", "category": "tech", "status": "predicted"},
        {"year": 2060, "label": "CO2 declining phase", "category": "milestone", "status": "predicted"},
        {"year": 2070, "label": "EEI = 0.5 W/m² (halved)", "category": "obs", "status": "predicted"},
        {"year": 2080, "label": "ΔT peak +1.5-1.8°C", "category": "milestone", "status": "predicted"},
        {"year": 2100, "label": "CO2 < 400 ppm (NZE+CDR)", "category": "milestone", "status": "predicted"},
    ]
    return {"milestones": milestones, "n_total": len(milestones)}


# ----------------------------------------------------------------------
# Test 2: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test2_predictions():
    predictions = [
        {"id": 1, "year": 2030, "claim": "World CO2 emissions peak", "p": 0.70},
        {"id": 2, "year": 2030, "claim": "Solar+wind share 30%", "p": 0.85},
        {"id": 3, "year": 2035, "claim": "Solar LCOE $20/MWh", "p": 0.80},
        {"id": 4, "year": 2040, "claim": "DAC commercial 1 GtCO2/yr", "p": 0.55},
        {"id": 5, "year": 2050, "claim": "NZE major countries", "p": 0.50},
        {"id": 6, "year": 2040, "claim": "AMOC strength -25%", "p": 0.65},
        {"id": 7, "year": 2080, "claim": "Temperature peak +1.8C (NZE+CDR)", "p": 0.50},
        {"id": 8, "year": 2060, "claim": "Amazon savanna 30%", "p": 0.40},
        {"id": 9, "year": 2040, "claim": "DAC cost $100/t", "p": 0.55},
        {"id": 10, "year": 2032, "claim": "EU carbon price $200/t", "p": 0.65},
    ]
    p_avg = float(np.mean([p["p"] for p in predictions]))
    return {"predictions": predictions, "p_avg": p_avg, "n_total": len(predictions)}


# ----------------------------------------------------------------------
# Test 3: ITU 11-vertex polytope connectivity
# ----------------------------------------------------------------------
def test3_polytope():
    vertices = [
        {"id": 1,  "name": "Quantum Compute (#1)",      "block": "engineering", "x": 1, "y": 0},
        {"id": 2,  "name": "AI/ASI (#2)",                "block": "engineering", "x": 0, "y": 1},
        {"id": 3,  "name": "Cryptography (#3)",          "block": "engineering", "x": 2, "y": 1},
        {"id": 4,  "name": "Semiconductors (#4)",        "block": "engineering", "x": 2, "y": 0},
        {"id": 5,  "name": "Cancer (#5)",                "block": "medicine",    "x": -1, "y": 3},
        {"id": 6,  "name": "Aging (#6)",                 "block": "medicine",    "x": -2, "y": 2},
        {"id": 7,  "name": "Psychiatry (#7)",            "block": "medicine",    "x": 0, "y": 2.5},
        {"id": 8,  "name": "Economics (#8)",             "block": "social",      "x": 3, "y": 3},
        {"id": 9,  "name": "Free Will (#9)",             "block": "philosophy",  "x": 4, "y": 2},
        {"id": 10, "name": "Energy / Materials (#10)",   "block": "engineering", "x": 3, "y": 0},
        {"id": 11, "name": "Climate / Earth (#11)",      "block": "biosphere",   "x": 4, "y": 1},
    ]
    edges = [
        (1, 2), (1, 4), (2, 3), (3, 4),      # engineering rectangle
        (4, 10), (10, 1), (10, 11),          # pentagon extension
        (5, 6), (6, 7), (7, 5),              # medicine triangle
        (11, 10), (11, 8), (11, 2), (11, 5), (11, 9),  # climate hub
        (8, 9), (8, 10),                     # social-philosophy connection
        (2, 5), (2, 7),                      # AI-medicine
    ]
    # Connectivity degree
    degree = {v["id"]: 0 for v in vertices}
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    return {
        "vertices": vertices,
        "edges": edges,
        "n_vertices": len(vertices),
        "n_edges": len(edges),
        "degree": degree,
        "max_degree_vertex": max(degree.items(), key=lambda x: x[1]),
    }


# ----------------------------------------------------------------------
# Test 4: Tier 1 #11 cross-paper metrics
# ----------------------------------------------------------------------
def test4_integration():
    # Per-phase summary
    phases = {
        "Phase 83": {
            "title": "ITU foundation",
            "key_values": {"CO2 ppm 2024": 422, "EEI W/m2": 1.0, "ECS K": 2.91, "PB breached": "7/10"},
        },
        "Phase 84": {
            "title": "Dynamic K-flows",
            "key_values": {"airborne fraction": 0.50, "ENSO period yr": 4.3,
                           "AMOC P(2050)": 0.14, "cascade P": 0.092},
        },
        "Phase 85": {
            "title": "Mitigation",
            "key_values": {"NZE share 2050 %": 72, "CDR Gt 2050": 9.5,
                           "T peak NZE+CDR+SRM K": 1.68, "cascade P min": 0.016},
        },
        "Phase 86": {
            "title": "Roadmap + polytope",
            "key_values": {"n_predictions": 10, "polytope vertices": 11,
                           "Pass-1 progress %": 39.1},
        },
    }
    # Cross-cuts with other Tier 1 papers
    crosscuts = {
        "Tier 1 #10 (Energy)": "Renewables transition + MOF for DAC",
        "Tier 1 #8 (Economics)": "Carbon pricing + investment $200T",
        "Tier 1 #2 (AI/ASI)":   "AGI accelerates climate models + materials discovery",
        "Tier 1 #5-#7 (medicine)": "Heat waves, vector-borne disease, climate anxiety",
        "Tier 0 (Phase 30-35)": "Life self-organization entropy",
        "Tier 1 #9 (philosophy)": "Intergenerational ethics, climate justice",
    }
    return {"phases": phases, "crosscuts": crosscuts}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig = plt.figure(figsize=(15, 11))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.30)

    # Panel 1: Roadmap timeline
    ax1 = fig.add_subplot(gs[0, :])
    cat_color = {"obs": "#1f77b4", "tech": "#ff7f0e", "policy": "#9467bd",
                 "tipping": "#d62728", "milestone": "#2ca02c"}
    cat_y = {"obs": 1, "tech": 2, "policy": 3, "tipping": 4, "milestone": 5}
    for m in t1["milestones"]:
        y = cat_y[m["category"]]
        marker = "o" if m["status"] == "done" else ("^" if m["status"] == "planned" else "*")
        ax1.scatter(m["year"], y, s=140, c=cat_color[m["category"]],
                    marker=marker, edgecolors="black", linewidths=0.8,
                    alpha=0.85, zorder=3)
        ax1.annotate(m["label"], (m["year"], y), xytext=(2, 7),
                     textcoords="offset points", fontsize=7,
                     rotation=22, ha="left")
    ax1.set_yticks(list(cat_y.values()))
    ax1.set_yticklabels(list(cat_y.keys()))
    ax1.set_xlim(2023, 2105)
    ax1.set_ylim(0.5, 5.8)
    ax1.set_xlabel("Year")
    ax1.set_title("Phase 86: Climate roadmap 2026-2100 ★ ITU 11-vertex polytope completion",
                  fontsize=12, fontweight="bold")
    ax1.grid(alpha=0.3, axis="x")
    legend_elems = [
        mpatches.Patch(color=cat_color[c], label=c) for c in cat_y.keys()
    ]
    ax1.legend(handles=legend_elems, loc="upper right", fontsize=8)

    # Panel 2: 10 predictions bar
    ax2 = fig.add_subplot(gs[1, 0])
    preds = t2["predictions"]
    ids = [p["id"] for p in preds]
    probs = [p["p"] for p in preds]
    claims = [f"{p['id']}. {p['claim'][:40]} ({p['year']})" for p in preds]
    colors = ["#2ca02c" if p >= 0.7 else "#ff7f0e" if p >= 0.5 else "#d62728" for p in probs]
    y_pos = np.arange(len(preds))
    ax2.barh(y_pos, probs, color=colors, alpha=0.8, edgecolor="black", linewidth=0.5)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(claims, fontsize=7)
    ax2.invert_yaxis()
    ax2.set_xlim(0, 1.0)
    ax2.axvline(0.5, ls="--", color="black", alpha=0.5)
    ax2.set_xlabel("Probability")
    ax2.set_title(f"10 falsifiable predictions (P_avg = {t2['p_avg']:.2f})")
    ax2.grid(alpha=0.3, axis="x")

    # Panel 3: 11-vertex polytope
    ax3 = fig.add_subplot(gs[1, 1])
    block_color = {"engineering": "#1f77b4", "medicine": "#d62728",
                   "social": "#9467bd", "philosophy": "#8c564b",
                   "biosphere": "#2ca02c"}
    # Draw edges first
    pos = {v["id"]: (v["x"], v["y"]) for v in t3["vertices"]}
    for a, b in t3["edges"]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        is_climate = 11 in (a, b)
        ax3.plot([xa, xb], [ya, yb],
                 "g-" if is_climate else "gray",
                 lw=2.5 if is_climate else 0.8,
                 alpha=0.7 if is_climate else 0.4,
                 zorder=1)
    # Draw vertices
    for v in t3["vertices"]:
        deg = t3["degree"][v["id"]]
        size = 350 + deg * 90
        color = block_color[v["block"]]
        edgecolor = "red" if v["id"] == 11 else "black"
        edge_lw = 2.5 if v["id"] == 11 else 1.0
        ax3.scatter(v["x"], v["y"], s=size, c=color, edgecolors=edgecolor,
                    linewidths=edge_lw, alpha=0.85, zorder=3)
        ax3.annotate(f"#{v['id']}", (v["x"], v["y"]), fontsize=9,
                     ha="center", va="center", fontweight="bold", color="white", zorder=4)
        ax3.annotate(v["name"].split("(")[0].strip(), (v["x"], v["y"]),
                     xytext=(0, -22), textcoords="offset points",
                     fontsize=6.5, ha="center", color="black")
    ax3.set_xlim(-3, 5.5)
    ax3.set_ylim(-1, 4)
    ax3.set_aspect("equal")
    ax3.set_title(f"ITU 11-vertex polytope | edges={t3['n_edges']} | hub: #{t3['max_degree_vertex'][0]} (deg={t3['max_degree_vertex'][1]})")
    ax3.axis("off")
    legend_elems = [
        mpatches.Patch(color=c, label=b) for b, c in block_color.items()
    ]
    ax3.legend(handles=legend_elems, loc="lower left", fontsize=7)

    plt.suptitle("Phase 86: Tier 1 #11 (Climate / Earth Systems) — final integration",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.savefig(path, dpi=110, bbox_inches="tight")
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 86: Climate roadmap + Tier 1 #11 completion")
    print("=" * 70)

    print("\n[Test 1] 2026-2100 roadmap milestones")
    t1 = test1_roadmap()
    print(f"  Total milestones: {t1['n_total']}")
    for m in t1["milestones"][:5]:
        print(f"    {m['year']} | {m['category']:9s} | {m['label']}")
    print(f"    ... ({t1['n_total'] - 5} more)")

    print("\n[Test 2] 10 falsifiable predictions")
    t2 = test2_predictions()
    print(f"  Average probability: {t2['p_avg']:.2f}")
    for p in t2["predictions"]:
        print(f"    P{p['id']:2d} ({p['year']}): {p['claim']:50s}  p={p['p']:.2f}")

    print("\n[Test 3] ITU 11-vertex polytope")
    t3 = test3_polytope()
    print(f"  Vertices: {t3['n_vertices']}")
    print(f"  Edges:    {t3['n_edges']}")
    print(f"  Max-degree vertex: #{t3['max_degree_vertex'][0]} (degree={t3['max_degree_vertex'][1]})")
    for vid, deg in sorted(t3["degree"].items(), key=lambda x: -x[1])[:5]:
        v = next(v for v in t3["vertices"] if v["id"] == vid)
        print(f"    #{vid:2d} {v['name']:32s}  degree={deg}")

    print("\n[Test 4] Tier 1 #11 cross-paper integration")
    t4 = test4_integration()
    for ph, data in t4["phases"].items():
        print(f"  {ph}: {data['title']}")
        for k, v in data["key_values"].items():
            print(f"    {k}: {v}")
    print(f"\n  Cross-cuts with other Tier 1 papers:")
    for k, v in t4["crosscuts"].items():
        print(f"    {k:28s} : {v}")

    out = {
        "phase": 86,
        "title": "Climate roadmap 2026-2100 + Tier 1 #11 completion",
        "test1_roadmap": t1,
        "test2_predictions": t2,
        "test3_polytope": {
            "n_vertices": t3["n_vertices"],
            "n_edges": t3["n_edges"],
            "max_degree_vertex_id": t3["max_degree_vertex"][0],
            "max_degree": t3["max_degree_vertex"][1],
            "degree": t3["degree"],
        },
        "test4_integration": t4,
    }
    with open("climate_roadmap_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: climate_roadmap_summary.json")

    make_figure(t1, t2, t3, t4, "climate_roadmap.png")
    print("  ✓ Figure saved: climate_roadmap.png")

    print("\n" + "=" * 70)
    print("Phase 86 COMPLETE — Tier 1 #11 done | ITU 11-vertex polytope achieved | "
          "Pass-1 86/220 (39.1%)")
    print("=" * 70)
