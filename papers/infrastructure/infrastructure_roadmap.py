"""
Phase 102: Infrastructure roadmap 2026-2050 + Tier 1 #15 completion
Tier 1 #15 — Phase 4/4 (final)

4 numerical experiments:
1. 2026-2050 milestone timeline
2. 10 falsifiable predictions
3. ITU 15-vertex polytope connectivity map
4. Tier 1 #15 cross-paper integration

Output: infrastructure_roadmap.png + infrastructure_roadmap_summary.json
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# ----------------------------------------------------------------------
# Test 1: Roadmap milestones
# ----------------------------------------------------------------------
def test1_roadmap():
    milestones = [
        {"year": 2024, "label": "Global investment 3.15T (China 1.5T)",     "category": "obs",       "status": "done"},
        {"year": 2025, "label": "EU NextGenEU midterm review",              "category": "policy",    "status": "planned"},
        {"year": 2026, "label": "China Xinjianjie Phase 2 begins",          "category": "policy",    "status": "predicted"},
        {"year": 2026, "label": "IIJA half spent, Build America Buy America","category": "policy",   "status": "predicted"},
        {"year": 2028, "label": "Grid inertia crisis (renewable countries)","category": "grid",      "status": "predicted"},
        {"year": 2030, "label": "Smart meters 40% global",                  "category": "smart",     "status": "predicted"},
        {"year": 2030, "label": "EU NextGenEU complete",                    "category": "policy",    "status": "predicted"},
        {"year": 2031, "label": "IIJA ends, Round 2 debated",               "category": "policy",    "status": "predicted"},
        {"year": 2032, "label": "MOSE expansion + Tokyo basin complete",    "category": "climate",   "status": "predicted"},
        {"year": 2035, "label": "Smart meters 75%, V2G commercial",         "category": "smart",     "status": "predicted"},
        {"year": 2035, "label": "Rooftop solar 1500 GW",                    "category": "DERMS",     "status": "predicted"},
        {"year": 2038, "label": "Grid-forming batteries 50%",               "category": "grid",      "status": "predicted"},
        {"year": 2040, "label": "DERMS 5000 GW (0.7x central gen)",         "category": "DERMS",     "status": "predicted"},
        {"year": 2040, "label": "Big U NY + Delta Works complete",          "category": "climate",   "status": "predicted"},
        {"year": 2045, "label": "AGI infrastructure management",            "category": "AI",        "status": "predicted"},
        {"year": 2048, "label": "Singapore coastal Phase 1 complete",       "category": "climate",   "status": "predicted"},
        {"year": 2050, "label": "Smart meters 95% (10B units)",             "category": "smart",     "status": "predicted"},
        {"year": 2050, "label": "DERMS 8500 GW (>central gen)",             "category": "DERMS",     "status": "predicted"},
        {"year": 2050, "label": "Climate adaptation 4.5T cumulative",       "category": "climate",   "status": "predicted"},
    ]
    return {"milestones": milestones, "n_total": len(milestones)}


# ----------------------------------------------------------------------
# Test 2: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test2_predictions():
    predictions = [
        {"id": 1,  "year": 2026, "claim": "China Xinjianjie Phase 2 begins", "p": 0.80},
        {"id": 2,  "year": 2031, "claim": "US IIJA Round 2 legislation",   "p": 0.55},
        {"id": 3,  "year": 2030, "claim": "Smart meters 40% global",        "p": 0.70},
        {"id": 4,  "year": 2028, "claim": "Major grid inertia outage by 2028", "p": 0.60},
        {"id": 5,  "year": 2032, "claim": "MOSE ext + Tokyo basin complete", "p": 0.50},
        {"id": 6,  "year": 2035, "claim": "V2G commercialized (major markets)", "p": 0.55},
        {"id": 7,  "year": 2050, "claim": "DERMS > central generation",    "p": 0.50},
        {"id": 8,  "year": 2045, "claim": "AGI infrastructure management", "p": 0.40},
        {"id": 9,  "year": 2050, "claim": "Climate adaptation 4.5T spent",  "p": 0.50},
        {"id": 10, "year": 2035, "claim": "ASCE USA grade improves to C+",  "p": 0.45},
    ]
    p_avg = float(np.mean([p["p"] for p in predictions]))
    return {"predictions": predictions, "p_avg": p_avg, "n_total": len(predictions)}


# ----------------------------------------------------------------------
# Test 3: ITU 15-vertex polytope
# ----------------------------------------------------------------------
def test3_polytope():
    vertices = [
        {"id": 1,  "name": "Quantum Compute (#1)",     "block": "engineering", "x": 1, "y": 0},
        {"id": 2,  "name": "AI/ASI (#2)",               "block": "engineering", "x": 0, "y": 1},
        {"id": 3,  "name": "Cryptography (#3)",         "block": "engineering", "x": 2, "y": 1},
        {"id": 4,  "name": "Semiconductors (#4)",       "block": "engineering", "x": 2, "y": 0},
        {"id": 5,  "name": "Cancer (#5)",               "block": "medicine",    "x": -1, "y": 3},
        {"id": 6,  "name": "Aging (#6)",                "block": "medicine",    "x": -2, "y": 2},
        {"id": 7,  "name": "Psychiatry (#7)",           "block": "medicine",    "x": 0, "y": 2.5},
        {"id": 8,  "name": "Economics (#8)",            "block": "social",      "x": 3, "y": 3},
        {"id": 9,  "name": "Free Will (#9)",            "block": "philosophy",  "x": 4, "y": 2},
        {"id": 10, "name": "Energy / Materials (#10)",  "block": "engineering", "x": 3, "y": 0},
        {"id": 11, "name": "Climate / Earth (#11)",     "block": "biosphere",   "x": 4, "y": 1},
        {"id": 12, "name": "Astrobiology / SETI (#12)", "block": "cosmic",      "x": 5, "y": 0},
        {"id": 13, "name": "Robotics (#13)",            "block": "embodiment",  "x": 1, "y": -1},
        {"id": 14, "name": "Communications (#14)",      "block": "communication","x": 3, "y": -1},
        {"id": 15, "name": "Infrastructure (#15)",      "block": "skeleton",    "x": 2, "y": -2},
    ]
    edges = [
        # Engineering rectangle + pentagon
        (1, 2), (1, 4), (2, 3), (3, 4),
        (4, 10), (10, 1), (10, 11),
        # Medicine triangle
        (5, 6), (6, 7), (7, 5),
        # Climate super-hub
        (11, 10), (11, 8), (11, 2), (11, 5), (11, 9),
        # Social-philosophy
        (8, 9), (8, 10),
        # AI-medicine
        (2, 5), (2, 7),
        # Cosmic axis
        (12, 11), (12, 2), (12, 6), (12, 9),
        # Embodiment axis
        (13, 2), (13, 4), (13, 8), (13, 9), (13, 10), (13, 11),
        # Communications K-channel
        (14, 1), (14, 2), (14, 3), (14, 4), (14, 8), (14, 10), (14, 11), (14, 12), (14, 13),
        # Infrastructure K-skeleton (NEW)
        (15, 2), (15, 4), (15, 8), (15, 10), (15, 11), (15, 13), (15, 14),
    ]
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
# Test 4: Tier 1 #15 integration
# ----------------------------------------------------------------------
def test4_integration():
    phases = {
        "Phase 99": {
            "title": "ITU foundation",
            "key_values": {"Global stock T$": 340, "Annual renewal T$": 10,
                           "Grid inertia 2050 s": 1.5, "ASCE 2021 grade": "D+",
                           "ASCE 10yr need T$": 3.1},
        },
        "Phase 100": {
            "title": "Smart grid + AI + resilience",
            "key_values": {"Smart meters 2050 B": 10, "DERMS 2050 GW": 8500,
                           "AI predictive accuracy": 0.90, "Cost reduction": 0.50,
                           "Downtime reduction": 0.94},
        },
        "Phase 101": {
            "title": "Industry + policy + intl",
            "key_values": {"China investment T$/yr": 1.5, "USA IIJA T$": 1.2,
                           "PPP 2050 B$": 600, "Climate adapt T$": 4.5},
        },
        "Phase 102": {
            "title": "Roadmap + polytope",
            "key_values": {"milestones": 19, "n_predictions": 10,
                           "polytope vertices": 15, "Pass-1 progress %": 46.4},
        },
    }
    crosscuts = {
        "Tier 1 #2 (AI/ASI)":      "Smart grid AI control, predictive maintenance",
        "Tier 1 #4 (Semi)":         "SCADA, sensors, PLCs",
        "Tier 1 #8 (Economics)":    "$340T capital stock, GDP multiplier 2-3",
        "Tier 1 #10 (Energy)":      "Power grid shared infrastructure",
        "Tier 1 #11 (Climate)":     "Climate adaptation $4.5T",
        "Tier 1 #13 (Robotics)":    "Infrastructure maintenance robots",
        "Tier 1 #14 (Comm)":        "Smart grid communications",
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
    cat_color = {"obs": "#1f77b4", "policy": "#9467bd", "smart": "#ff7f0e",
                 "grid": "#d62728", "DERMS": "#2ca02c", "climate": "#17becf",
                 "AI": "#8c564b"}
    cat_y = {"obs": 1, "policy": 2, "smart": 3, "grid": 4,
             "DERMS": 5, "climate": 6, "AI": 7}
    for m in t1["milestones"]:
        y = cat_y.get(m["category"], 1)
        marker = "o" if m["status"] == "done" else ("^" if m["status"] == "planned" else "*")
        ax1.scatter(m["year"], y, s=140, c=cat_color.get(m["category"], "gray"),
                    marker=marker, edgecolors="black", linewidths=0.8,
                    alpha=0.85, zorder=3)
        ax1.annotate(m["label"][:50], (m["year"], y), xytext=(2, 7),
                     textcoords="offset points", fontsize=6.5,
                     rotation=18, ha="left")
    ax1.set_yticks(list(cat_y.values()))
    ax1.set_yticklabels(list(cat_y.keys()))
    ax1.set_xlim(2023, 2055)
    ax1.set_ylim(0.5, 8.5)
    ax1.set_xlabel("Year")
    ax1.set_title("Phase 102: Infrastructure roadmap 2026-2050 - ITU 15-vertex polytope",
                  fontsize=12, fontweight="bold")
    ax1.grid(alpha=0.3, axis="x")
    legend_elems = [mpatches.Patch(color=cat_color[c], label=c) for c in cat_y.keys()]
    ax1.legend(handles=legend_elems, loc="upper right", fontsize=8)

    # Panel 2: 10 predictions
    ax2 = fig.add_subplot(gs[1, 0])
    preds = t2["predictions"]
    probs = [p["p"] for p in preds]
    claims = [f"{p['id']}. {p['claim'][:42]} ({p['year']})" for p in preds]
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

    # Panel 3: 15-vertex polytope
    ax3 = fig.add_subplot(gs[1, 1])
    block_color = {"engineering": "#1f77b4", "medicine": "#d62728",
                   "social": "#9467bd", "philosophy": "#8c564b",
                   "biosphere": "#2ca02c", "cosmic": "#000080",
                   "embodiment": "#ff1493", "communication": "#00ced1",
                   "skeleton": "#a0522d"}
    pos = {v["id"]: (v["x"], v["y"]) for v in t3["vertices"]}
    for a, b in t3["edges"]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        is_inf = 15 in (a, b)
        ax3.plot([xa, xb], [ya, yb],
                 "#a0522d" if is_inf else "gray",
                 lw=3 if is_inf else 0.6,
                 alpha=0.85 if is_inf else 0.4,
                 zorder=1)
    for v in t3["vertices"]:
        deg = t3["degree"][v["id"]]
        size = 350 + deg * 60
        color = block_color[v["block"]]
        edgecolor = "red" if v["id"] == 15 else "black"
        edge_lw = 2.5 if v["id"] == 15 else 1.0
        ax3.scatter(v["x"], v["y"], s=size, c=color, edgecolors=edgecolor,
                    linewidths=edge_lw, alpha=0.85, zorder=3)
        ax3.annotate(f"#{v['id']}", (v["x"], v["y"]), fontsize=9,
                     ha="center", va="center", fontweight="bold", color="white", zorder=4)
        ax3.annotate(v["name"].split("(")[0].strip(), (v["x"], v["y"]),
                     xytext=(0, -22), textcoords="offset points",
                     fontsize=6, ha="center", color="black")
    ax3.set_xlim(-3, 6.5)
    ax3.set_ylim(-3, 4)
    ax3.set_aspect("equal")
    ax3.set_title(f"ITU 15-vertex polytope (K-skeleton axis added) | edges={t3['n_edges']} | hub: #{t3['max_degree_vertex'][0]} (deg={t3['max_degree_vertex'][1]})")
    ax3.axis("off")
    legend_elems = [mpatches.Patch(color=c, label=b) for b, c in block_color.items()]
    ax3.legend(handles=legend_elems, loc="lower left", fontsize=6)

    plt.suptitle("Phase 102: Tier 1 #15 (Infrastructure / Power Grid) - final integration",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.savefig(path, dpi=110, bbox_inches="tight")
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 102: Infrastructure roadmap + Tier 1 #15 completion")
    print("=" * 70)

    print("\n[Test 1] 2026-2050 roadmap milestones")
    t1 = test1_roadmap()
    print(f"  Total milestones: {t1['n_total']}")
    for m in t1["milestones"][:5]:
        print(f"    {m['year']} | {m['category']:9s} | {m['label']}")
    print(f"    ... ({t1['n_total'] - 5} more)")

    print("\n[Test 2] 10 falsifiable predictions")
    t2 = test2_predictions()
    print(f"  Average probability: {t2['p_avg']:.2f}")
    for p in t2["predictions"]:
        print(f"    P{p['id']:2d} ({p['year']}): {p['claim']:42s}  p={p['p']:.2f}")

    print("\n[Test 3] ITU 15-vertex polytope")
    t3 = test3_polytope()
    print(f"  Vertices: {t3['n_vertices']}")
    print(f"  Edges:    {t3['n_edges']}")
    print(f"  Max-degree vertex: #{t3['max_degree_vertex'][0]} (degree={t3['max_degree_vertex'][1]})")
    for vid, deg in sorted(t3["degree"].items(), key=lambda x: -x[1])[:7]:
        v = next(v for v in t3["vertices"] if v["id"] == vid)
        print(f"    #{vid:2d} {v['name']:32s}  degree={deg}")

    print("\n[Test 4] Tier 1 #15 cross-paper integration")
    t4 = test4_integration()
    for ph, data in t4["phases"].items():
        print(f"  {ph}: {data['title']}")
        for k, v in data["key_values"].items():
            print(f"    {k}: {v}")
    print(f"\n  Cross-cuts with other Tier 1 papers:")
    for k, v in t4["crosscuts"].items():
        print(f"    {k:28s} : {v}")

    out = {
        "phase": 102,
        "title": "Infrastructure roadmap 2026-2050 + Tier 1 #15 completion",
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
    with open("infrastructure_roadmap_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: infrastructure_roadmap_summary.json")

    make_figure(t1, t2, t3, t4, "infrastructure_roadmap.png")
    print("  ✓ Figure saved: infrastructure_roadmap.png")

    print("\n" + "=" * 70)
    print("Phase 102 COMPLETE — Tier 1 #15 done | ITU 15-vertex polytope achieved | "
          "Pass-1 102/220 (46.4%)")
    print("=" * 70)
