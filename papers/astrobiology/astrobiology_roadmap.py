"""
Phase 90: Astrobiology / SETI roadmap 2026-2100 + Tier 1 #12 summary
Tier 1 #12 — Phase 4/4 (final)

4 numerical experiments:
1. 2026-2100 milestone timeline
2. 10 falsifiable predictions
3. ITU 12-vertex polytope connectivity map
4. Tier 1 #12 cross-paper integration

Output: astrobiology_roadmap.png + astrobiology_roadmap_summary.json
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
        {"year": 2024, "label": "DMS @ K2-18b 2.4 sigma (Madhusudhan)", "category": "obs", "status": "done"},
        {"year": 2025, "label": "JWST cycle 4 K2-18b followup", "category": "obs", "status": "planned"},
        {"year": 2027, "label": "K2-18b DMS 5 sigma confirm/deny", "category": "obs", "status": "predicted"},
        {"year": 2028, "label": "ELT first light", "category": "obs", "status": "planned"},
        {"year": 2030, "label": "GMT first light", "category": "obs", "status": "planned"},
        {"year": 2032, "label": "TMT first light", "category": "obs", "status": "planned"},
        {"year": 2032, "label": "Breakthrough Listen phase 2 end", "category": "SETI", "status": "planned"},
        {"year": 2035, "label": "AGI accelerates SETI 1000x", "category": "tech", "status": "predicted"},
        {"year": 2040, "label": "HWO launch", "category": "obs", "status": "predicted"},
        {"year": 2042, "label": "HWO 50+ exoplanet atmospheres", "category": "obs", "status": "predicted"},
        {"year": 2045, "label": "First confirmed biosignature (P=0.4)", "category": "milestone", "status": "predicted"},
        {"year": 2050, "label": "UN ETI contact protocol (Rio scale)", "category": "policy", "status": "predicted"},
        {"year": 2055, "label": "Proxima b flyby (Starshot)", "category": "exploration", "status": "predicted"},
        {"year": 2060, "label": "ALH84001-Mars reassessment", "category": "obs", "status": "predicted"},
        {"year": 2070, "label": "LISA-X civilization GW search", "category": "obs", "status": "predicted"},
        {"year": 2080, "label": "TRAPPIST-1 direct mission", "category": "exploration", "status": "predicted"},
        {"year": 2100, "label": "Fermi paradox: resolved or continued", "category": "milestone", "status": "predicted"},
    ]
    return {"milestones": milestones, "n_total": len(milestones)}


# ----------------------------------------------------------------------
# Test 2: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test2_predictions():
    predictions = [
        {"id": 1,  "year": 2027, "claim": "K2-18b DMS 5 sigma confirm", "p": 0.35},
        {"id": 2,  "year": 2030, "claim": "JWST 2nd DMS candidate", "p": 0.40},
        {"id": 3,  "year": 2040, "claim": "HWO launches on schedule", "p": 0.65},
        {"id": 4,  "year": 2045, "claim": "HWO spectra 5+ Earth-like atms", "p": 0.70},
        {"id": 5,  "year": 2045, "claim": "First confirmed biosignature", "p": 0.40},
        {"id": 6,  "year": 2030, "claim": "Breakthrough Listen still null", "p": 0.85},
        {"id": 7,  "year": 2050, "claim": "Type II Kardashev absent in galaxy", "p": 0.85},
        {"id": 8,  "year": 2035, "claim": "EQ-K_self confirmed in fossil record", "p": 0.65},
        {"id": 9,  "year": 2030, "claim": "RNA self-replication synthesized", "p": 0.55},
        {"id": 10, "year": 2100, "claim": "No definite ETI contact by 2100", "p": 0.75},
    ]
    p_avg = float(np.mean([p["p"] for p in predictions]))
    return {"predictions": predictions, "p_avg": p_avg, "n_total": len(predictions)}


# ----------------------------------------------------------------------
# Test 3: ITU 12-vertex polytope
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
    ]
    edges = [
        (1, 2), (1, 4), (2, 3), (3, 4),         # engineering rectangle
        (4, 10), (10, 1), (10, 11),             # pentagon extension
        (5, 6), (6, 7), (7, 5),                 # medicine triangle
        (11, 10), (11, 8), (11, 2), (11, 5), (11, 9),  # climate super-hub
        (8, 9), (8, 10),                         # social-philosophy connection
        (2, 5), (2, 7),                          # AI-medicine
        (12, 11), (12, 2), (12, 6), (12, 9),    # cosmic axis connections
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
# Test 4: Tier 1 #12 integration
# ----------------------------------------------------------------------
def test4_integration():
    phases = {
        "Phase 87": {
            "title": "ITU foundation",
            "key_values": {"K_life range orders": 22, "Drake N median": 0.27,
                           "PB-style top exoplanet HI (Teegarden b)": 0.58,
                           "Great Filter combined": "65%"},
        },
        "Phase 88": {
            "title": "Drake Bayesian + SDA",
            "key_values": {"P(alone in galaxy)": "87%", "P(alone in universe)": "33%",
                           "hard steps": 2, "Type II detection ly": "6e9",
                           "BL Bayes 10pct->": "2.2%"},
        },
        "Phase 89": {
            "title": "Abiogenesis + intelligence",
            "key_values": {"Cambrian speedup": "2x",
                           "EQ-K_self r": 0.90,
                           "K2-18b prior 5pct -> posterior": "30%"},
        },
        "Phase 90": {
            "title": "Roadmap + polytope",
            "key_values": {"milestones": 17, "n_predictions": 10,
                           "polytope vertices": 12, "Pass-1 progress %": 40.9},
        },
    }
    crosscuts = {
        "Tier 1 #11 (Climate)":   "Earth habitability = self Great Filter candidate",
        "Tier 1 #2 (AI/ASI)":     "ASI alignment failure = future Great Filter",
        "Tier 1 #6 (Aging)":      "Civilization lifetime L physics",
        "Tier 1 #9 (Free Will)":  "Alien ethics, contact governance",
        "Tier 0 (Phase 30-35)":   "Life self-organization foundation",
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
                 "exploration": "#d62728", "milestone": "#2ca02c", "SETI": "#8c564b"}
    cat_y = {"obs": 1, "tech": 2, "policy": 3, "exploration": 4, "milestone": 5, "SETI": 6}
    for m in t1["milestones"]:
        y = cat_y[m["category"]]
        marker = "o" if m["status"] == "done" else ("^" if m["status"] == "planned" else "*")
        ax1.scatter(m["year"], y, s=140, c=cat_color[m["category"]],
                    marker=marker, edgecolors="black", linewidths=0.8,
                    alpha=0.85, zorder=3)
        ax1.annotate(m["label"], (m["year"], y), xytext=(2, 7),
                     textcoords="offset points", fontsize=6.5,
                     rotation=22, ha="left")
    ax1.set_yticks(list(cat_y.values()))
    ax1.set_yticklabels(list(cat_y.keys()))
    ax1.set_xlim(2023, 2110)
    ax1.set_ylim(0.5, 7.5)
    ax1.set_xlabel("Year")
    ax1.set_title("Phase 90: Astrobiology / SETI roadmap 2026-2100 - ITU 12-vertex polytope completion",
                  fontsize=12, fontweight="bold")
    ax1.grid(alpha=0.3, axis="x")
    legend_elems = [mpatches.Patch(color=cat_color[c], label=c) for c in cat_y.keys()]
    ax1.legend(handles=legend_elems, loc="upper right", fontsize=8)

    # Panel 2: 10 predictions bar
    ax2 = fig.add_subplot(gs[1, 0])
    preds = t2["predictions"]
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

    # Panel 3: 12-vertex polytope
    ax3 = fig.add_subplot(gs[1, 1])
    block_color = {"engineering": "#1f77b4", "medicine": "#d62728",
                   "social": "#9467bd", "philosophy": "#8c564b",
                   "biosphere": "#2ca02c", "cosmic": "#000080"}
    pos = {v["id"]: (v["x"], v["y"]) for v in t3["vertices"]}
    for a, b in t3["edges"]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        is_cosmic = 12 in (a, b)
        ax3.plot([xa, xb], [ya, yb],
                 "navy" if is_cosmic else "gray",
                 lw=3 if is_cosmic else 0.8,
                 alpha=0.8 if is_cosmic else 0.4,
                 zorder=1)
    for v in t3["vertices"]:
        deg = t3["degree"][v["id"]]
        size = 350 + deg * 90
        color = block_color[v["block"]]
        edgecolor = "red" if v["id"] == 12 else "black"
        edge_lw = 2.5 if v["id"] == 12 else 1.0
        ax3.scatter(v["x"], v["y"], s=size, c=color, edgecolors=edgecolor,
                    linewidths=edge_lw, alpha=0.85, zorder=3)
        text_color = "white" if v["block"] != "cosmic" else "yellow"
        ax3.annotate(f"#{v['id']}", (v["x"], v["y"]), fontsize=9,
                     ha="center", va="center", fontweight="bold", color=text_color, zorder=4)
        ax3.annotate(v["name"].split("(")[0].strip(), (v["x"], v["y"]),
                     xytext=(0, -22), textcoords="offset points",
                     fontsize=6.5, ha="center", color="black")
    ax3.set_xlim(-3, 6.5)
    ax3.set_ylim(-1, 4)
    ax3.set_aspect("equal")
    ax3.set_title(f"ITU 12-vertex polytope (cosmic axis added) | edges={t3['n_edges']} | hub: #{t3['max_degree_vertex'][0]} (deg={t3['max_degree_vertex'][1]})")
    ax3.axis("off")
    legend_elems = [mpatches.Patch(color=c, label=b) for b, c in block_color.items()]
    ax3.legend(handles=legend_elems, loc="lower left", fontsize=7)

    plt.suptitle("Phase 90: Tier 1 #12 (Astrobiology / SETI) - final integration, cosmic axis",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.savefig(path, dpi=110, bbox_inches="tight")
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 90: Astrobiology / SETI roadmap + Tier 1 #12 completion")
    print("=" * 70)

    print("\n[Test 1] 2026-2100 roadmap milestones")
    t1 = test1_roadmap()
    print(f"  Total milestones: {t1['n_total']}")
    for m in t1["milestones"][:5]:
        print(f"    {m['year']} | {m['category']:11s} | {m['label']}")
    print(f"    ... ({t1['n_total'] - 5} more)")

    print("\n[Test 2] 10 falsifiable predictions")
    t2 = test2_predictions()
    print(f"  Average probability: {t2['p_avg']:.2f}")
    for p in t2["predictions"]:
        print(f"    P{p['id']:2d} ({p['year']}): {p['claim']:42s}  p={p['p']:.2f}")

    print("\n[Test 3] ITU 12-vertex polytope")
    t3 = test3_polytope()
    print(f"  Vertices: {t3['n_vertices']}")
    print(f"  Edges:    {t3['n_edges']}")
    print(f"  Max-degree vertex: #{t3['max_degree_vertex'][0]} (degree={t3['max_degree_vertex'][1]})")
    for vid, deg in sorted(t3["degree"].items(), key=lambda x: -x[1])[:5]:
        v = next(v for v in t3["vertices"] if v["id"] == vid)
        print(f"    #{vid:2d} {v['name']:32s}  degree={deg}")

    print("\n[Test 4] Tier 1 #12 cross-paper integration")
    t4 = test4_integration()
    for ph, data in t4["phases"].items():
        print(f"  {ph}: {data['title']}")
        for k, v in data["key_values"].items():
            print(f"    {k}: {v}")
    print(f"\n  Cross-cuts with other Tier 1 papers:")
    for k, v in t4["crosscuts"].items():
        print(f"    {k:28s} : {v}")

    out = {
        "phase": 90,
        "title": "Astrobiology / SETI roadmap 2026-2100 + Tier 1 #12 completion",
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
    with open("astrobiology_roadmap_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: astrobiology_roadmap_summary.json")

    make_figure(t1, t2, t3, t4, "astrobiology_roadmap.png")
    print("  ✓ Figure saved: astrobiology_roadmap.png")

    print("\n" + "=" * 70)
    print("Phase 90 COMPLETE — Tier 1 #12 done | ITU 12-vertex polytope achieved | "
          "Pass-1 90/220 (40.9%)")
    print("=" * 70)
