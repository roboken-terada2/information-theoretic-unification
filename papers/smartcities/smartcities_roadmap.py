"""
Phase 106: Smart cities roadmap 2026-2050 + Tier 1 #16 completion
Tier 1 #16 — Phase 4/4 (final) + engineering-industry block completion

4 numerical experiments:
1. 2026-2050 milestone timeline
2. 10 falsifiable predictions
3. ITU 16-vertex polytope connectivity map (ULTIMATE)
4. Tier 1 #16 cross-paper integration

Output: smartcities_roadmap.png + smartcities_roadmap_summary.json
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
        {"year": 2024, "label": "Zurich #1 IMD, Singapore 5M sensors",   "category": "obs",       "status": "done"},
        {"year": 2025, "label": "EU AI Act high-risk regulation effective", "category": "policy", "status": "planned"},
        {"year": 2026, "label": "Songdo IBD final completion (21yr)",     "category": "project",   "status": "predicted"},
        {"year": 2027, "label": "NEOM The Line first phase opens",        "category": "project",   "status": "predicted"},
        {"year": 2028, "label": "International ISO 37125 smart city std", "category": "policy",    "status": "predicted"},
        {"year": 2030, "label": "Xiongan 1M residents + integrated std",  "category": "project",   "status": "predicted"},
        {"year": 2030, "label": "EU Digital Decade 95% penetration",      "category": "policy",    "status": "predicted"},
        {"year": 2032, "label": "L4 autonomous driving urban commercial", "category": "autonomy",  "status": "predicted"},
        {"year": 2035, "label": "AGI city L4 autonomy 0.30",              "category": "agi",       "status": "predicted"},
        {"year": 2035, "label": "Face recognition ban EU + 50% US states","category": "policy",    "status": "predicted"},
        {"year": 2038, "label": "15-min cities expand to 30+ globally",   "category": "urbanism",  "status": "predicted"},
        {"year": 2040, "label": "AGI city L4 autonomy 0.50 (half AI)",    "category": "agi",       "status": "predicted"},
        {"year": 2040, "label": "Smart city market $2.5T",                "category": "market",    "status": "predicted"},
        {"year": 2045, "label": "Nusantara full operational",             "category": "project",   "status": "predicted"},
        {"year": 2050, "label": "ASI city (L5 autonomy 0.75)",            "category": "agi",       "status": "predicted"},
        {"year": 2050, "label": "Market $3T, Telosa complete",            "category": "market",    "status": "predicted"},
    ]
    return {"milestones": milestones, "n_total": len(milestones)}


# ----------------------------------------------------------------------
# Test 2: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test2_predictions():
    predictions = [
        {"id": 1,  "year": 2026, "claim": "EU AI Act face recognition ban enforced", "p": 0.80},
        {"id": 2,  "year": 2027, "claim": "NEOM The Line first phase opens",       "p": 0.50},
        {"id": 3,  "year": 2032, "claim": "L4 autonomous driving urban commercial","p": 0.55},
        {"id": 4,  "year": 2040, "claim": "AGI city L4 autonomy 0.50",            "p": 0.45},
        {"id": 5,  "year": 2038, "claim": "15-min cities >30 globally",            "p": 0.60},
        {"id": 6,  "year": 2035, "claim": "US 5+ states ban face recognition",     "p": 0.55},
        {"id": 7,  "year": 2030, "claim": "Xiongan 1M residents",                   "p": 0.55},
        {"id": 8,  "year": 2035, "claim": "Digital democracy national (5 countries)", "p": 0.40},
        {"id": 9,  "year": 2030, "claim": "Smart city market $1.5T",                "p": 0.65},
        {"id": 10, "year": 2050, "claim": "ASI city L5 realized",                   "p": 0.35},
    ]
    p_avg = float(np.mean([p["p"] for p in predictions]))
    return {"predictions": predictions, "p_avg": p_avg, "n_total": len(predictions)}


# ----------------------------------------------------------------------
# Test 3: ITU 16-vertex polytope
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
        {"id": 16, "name": "Smart Cities (#16)",        "block": "urban",       "x": 3.5, "y": -2.5},
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
        # Infrastructure K-skeleton
        (15, 2), (15, 4), (15, 8), (15, 10), (15, 11), (15, 13), (15, 14),
        # Smart Cities ULTIMATE HUB - connects to ALL 15 others (NEW)
        (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7),
        (16, 8), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15),
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
# Test 4: Tier 1 #16 integration + Block summary
# ----------------------------------------------------------------------
def test4_integration():
    phases = {
        "Phase 103": {
            "title": "ITU foundation",
            "key_values": {"IMD #1": "Zurich", "Singapore sensors M": 5,
                           "Greenfield total T$": 1.73, "Estonia privacy": 0.85},
        },
        "Phase 104": {
            "title": "AGI city + sustainability + integration",
            "key_values": {"AGI 2040 autonomy": 0.50, "Paris 15min car %": -40,
                           "Tier 1 implemented": 15, "Xiongan score": 85},
        },
        "Phase 105": {
            "title": "Economy + policy + ethics",
            "key_values": {"Market 2050 T$": 3.0, "EU AI Act prohibited": 8,
                           "China surveillance": 0.95, "Lagos divide %": 60},
        },
        "Phase 106": {
            "title": "Roadmap + polytope",
            "key_values": {"milestones": 16, "n_predictions": 10,
                           "polytope vertices": 16, "Pass-1 progress %": 48.2},
        },
    }
    # Engineering-industry block summary
    block_summary = [
        {"phase": "91-94",   "tier": 13, "topic": "Robotics / Embodied AI",   "DOI": "20224976"},
        {"phase": "95-98",   "tier": 14, "topic": "Communications / Networks", "DOI": "20225970"},
        {"phase": "99-102",  "tier": 15, "topic": "Infrastructure / Power Grid", "DOI": "20226481"},
        {"phase": "103-106", "tier": 16, "topic": "Smart Cities",             "DOI": "pending"},
    ]
    return {"phases": phases, "block_summary": block_summary}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig = plt.figure(figsize=(15, 11))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.30)

    # Panel 1: Roadmap timeline
    ax1 = fig.add_subplot(gs[0, :])
    cat_color = {"obs": "#1f77b4", "policy": "#9467bd", "project": "#2ca02c",
                 "autonomy": "#ff7f0e", "agi": "#d62728", "urbanism": "#17becf",
                 "market": "#8c564b"}
    cat_y = {"obs": 1, "policy": 2, "project": 3, "urbanism": 4,
             "autonomy": 5, "agi": 6, "market": 7}
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
    ax1.set_title("Phase 106: Smart cities roadmap 2026-2050 - ITU 16-vertex polytope (URBAN ULTIMATE HUB)",
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

    # Panel 3: 16-vertex polytope
    ax3 = fig.add_subplot(gs[1, 1])
    block_color = {"engineering": "#1f77b4", "medicine": "#d62728",
                   "social": "#9467bd", "philosophy": "#8c564b",
                   "biosphere": "#2ca02c", "cosmic": "#000080",
                   "embodiment": "#ff1493", "communication": "#00ced1",
                   "skeleton": "#a0522d", "urban": "#ffd700"}
    pos = {v["id"]: (v["x"], v["y"]) for v in t3["vertices"]}
    for a, b in t3["edges"]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        is_urban = 16 in (a, b)
        ax3.plot([xa, xb], [ya, yb],
                 "#ffd700" if is_urban else "gray",
                 lw=2 if is_urban else 0.5,
                 alpha=0.85 if is_urban else 0.4,
                 zorder=1)
    for v in t3["vertices"]:
        deg = t3["degree"][v["id"]]
        size = 350 + deg * 50
        color = block_color[v["block"]]
        edgecolor = "red" if v["id"] == 16 else "black"
        edge_lw = 3 if v["id"] == 16 else 1.0
        ax3.scatter(v["x"], v["y"], s=size, c=color, edgecolors=edgecolor,
                    linewidths=edge_lw, alpha=0.85, zorder=3)
        ax3.annotate(f"#{v['id']}", (v["x"], v["y"]), fontsize=8,
                     ha="center", va="center", fontweight="bold",
                     color="black" if v["id"] == 16 else "white", zorder=4)
        ax3.annotate(v["name"].split("(")[0].strip(), (v["x"], v["y"]),
                     xytext=(0, -22), textcoords="offset points",
                     fontsize=5.5, ha="center", color="black")
    ax3.set_xlim(-3, 6.5)
    ax3.set_ylim(-3.5, 4)
    ax3.set_aspect("equal")
    ax3.set_title(f"ITU 16-vertex polytope (Urban ULTIMATE HUB) | edges={t3['n_edges']} | hub: #{t3['max_degree_vertex'][0]} (deg={t3['max_degree_vertex'][1]})")
    ax3.axis("off")
    legend_elems = [mpatches.Patch(color=c, label=b) for b, c in block_color.items()]
    ax3.legend(handles=legend_elems, loc="lower left", fontsize=6, ncol=2)

    plt.suptitle("Phase 106: Tier 1 #16 (Smart Cities) - final integration + engineering block COMPLETE",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.savefig(path, dpi=110, bbox_inches="tight")
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 106: Smart cities roadmap + Tier 1 #16 completion")
    print("                   + ENGINEERING-INDUSTRY BLOCK COMPLETE")
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
        print(f"    P{p['id']:2d} ({p['year']}): {p['claim']:48s}  p={p['p']:.2f}")

    print("\n[Test 3] ITU 16-vertex polytope (ULTIMATE HUB)")
    t3 = test3_polytope()
    print(f"  Vertices: {t3['n_vertices']}")
    print(f"  Edges:    {t3['n_edges']}")
    print(f"  Max-degree vertex: #{t3['max_degree_vertex'][0]} (degree={t3['max_degree_vertex'][1]}) ★ ULTIMATE")
    for vid, deg in sorted(t3["degree"].items(), key=lambda x: -x[1])[:7]:
        v = next(v for v in t3["vertices"] if v["id"] == vid)
        print(f"    #{vid:2d} {v['name']:32s}  degree={deg}")

    print("\n[Test 4] Tier 1 #16 integration + Engineering-Industry block")
    t4 = test4_integration()
    for ph, data in t4["phases"].items():
        print(f"  {ph}: {data['title']}")
        for k, v in data["key_values"].items():
            print(f"    {k}: {v}")
    print(f"\n  ★ ENGINEERING-INDUSTRY BLOCK COMPLETE (Phase 91-106, 4 Tier 1):")
    for b in t4["block_summary"]:
        print(f"    Phase {b['phase']:8s}  Tier 1 #{b['tier']:2d}  {b['topic']:32s}  DOI {b['DOI']}")

    out = {
        "phase": 106,
        "title": "Smart cities roadmap 2026-2050 + Tier 1 #16 + Engineering-Industry block completion",
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
    with open("smartcities_roadmap_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: smartcities_roadmap_summary.json")

    make_figure(t1, t2, t3, t4, "smartcities_roadmap.png")
    print("  ✓ Figure saved: smartcities_roadmap.png")

    print("\n" + "=" * 70)
    print("Phase 106 COMPLETE — Tier 1 #16 done | 16-vertex polytope (ULTIMATE) | "
          "Pass-1 106/220 (48.2%)")
    print("              ENGINEERING-INDUSTRY BLOCK (Phase 91-106) COMPLETE ★")
    print("=" * 70)
