"""
Phase 98: Communications roadmap 2026-2050 + Tier 1 #14 completion
Tier 1 #14 — Phase 4/4 (final)

4 numerical experiments:
1. 2026-2050 milestone timeline
2. 10 falsifiable predictions
3. ITU 14-vertex polytope connectivity map
4. Tier 1 #14 cross-paper integration

Output: comm_roadmap.png + comm_roadmap_summary.json
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
        {"year": 2024, "label": "Internet 500 EB/mo, 5G commercial, Starlink 6800 sats", "category": "obs", "status": "done"},
        {"year": 2025, "label": "NIST PQC standards effective, Kuiper 100 sats", "category": "security", "status": "planned"},
        {"year": 2026, "label": "Guowang first launch (China)", "category": "satellite", "status": "predicted"},
        {"year": 2028, "label": "IMT-2030 6G spec finalized (ITU-R)", "category": "standard", "status": "predicted"},
        {"year": 2030, "label": "6G commercial launch (major countries)", "category": "6G", "status": "predicted"},
        {"year": 2030, "label": "Entanglement distribution commercial (Wehner Stage 2)", "category": "quantum", "status": "predicted"},
        {"year": 2030, "label": "UN SDG: 90% Internet penetration", "category": "policy", "status": "predicted"},
        {"year": 2032, "label": "Starlink 42,000 sats complete", "category": "satellite", "status": "predicted"},
        {"year": 2035, "label": "Quantum memory network commercial (Stage 3)", "category": "quantum", "status": "predicted"},
        {"year": 2035, "label": "6G users 3 billion", "category": "6G", "status": "predicted"},
        {"year": 2038, "label": "Fault-tolerant quantum communication (Stage 4)", "category": "quantum", "status": "predicted"},
        {"year": 2040, "label": "6G full deployment (97% population)", "category": "6G", "status": "predicted"},
        {"year": 2040, "label": "Telecom market $4.5T", "category": "economy", "status": "predicted"},
        {"year": 2045, "label": "Distributed quantum computing network (Stage 5)", "category": "quantum", "status": "predicted"},
        {"year": 2050, "label": "Penetration 99.5% (offline only 50M)", "category": "policy", "status": "predicted"},
        {"year": 2050, "label": "Telecom $8T, quantum net $300B/yr", "category": "economy", "status": "predicted"},
    ]
    return {"milestones": milestones, "n_total": len(milestones)}


# ----------------------------------------------------------------------
# Test 2: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test2_predictions():
    predictions = [
        {"id": 1,  "year": 2028, "claim": "6G IMT-2030 spec finalized", "p": 0.75},
        {"id": 2,  "year": 2030, "claim": "6G commercial launch", "p": 0.65},
        {"id": 3,  "year": 2030, "claim": "Quantum entanglement distribution commercial", "p": 0.55},
        {"id": 4,  "year": 2032, "claim": "Starlink 42,000 sats complete", "p": 0.50},
        {"id": 5,  "year": 2030, "claim": "Internet penetration 90%", "p": 0.65},
        {"id": 6,  "year": 2035, "claim": "6G users 3 billion", "p": 0.50},
        {"id": 7,  "year": 2035, "claim": "Quantum memory network commercial", "p": 0.45},
        {"id": 8,  "year": 2050, "claim": "Digital divide reduced 90%", "p": 0.55},
        {"id": 9,  "year": 2030, "claim": "China 6G patent share > 35%", "p": 0.70},
        {"id": 10, "year": 2045, "claim": "Distributed quantum compute net commercial", "p": 0.40},
    ]
    p_avg = float(np.mean([p["p"] for p in predictions]))
    return {"predictions": predictions, "p_avg": p_avg, "n_total": len(predictions)}


# ----------------------------------------------------------------------
# Test 3: ITU 14-vertex polytope
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
        # Communications K-channel axis (NEW)
        (14, 1), (14, 2), (14, 3), (14, 4), (14, 8), (14, 10), (14, 11), (14, 12), (14, 13),
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
# Test 4: Tier 1 #14 integration
# ----------------------------------------------------------------------
def test4_integration():
    phases = {
        "Phase 95": {
            "title": "ITU foundation",
            "key_values": {"Shannon = ITU special case": True,
                           "Internet doubling yr": 2.9,
                           "Internet 2024 EB/mo": 500,
                           "Total sats planned": 60506},
        },
        "Phase 96": {
            "title": "6G + Q-internet + FL",
            "key_values": {"6G peak Gbps": 1000, "6G latency ms": 0.1,
                           "Q-internet Stage 5 year": 2045,
                           "FL final accuracy": 0.98},
        },
        "Phase 97": {
            "title": "Industry + economy + divide",
            "key_values": {"ICT 2050 T$": 30, "Telecom 2050 T$": 8,
                           "Offline 2050 B": 0.65, "US+CN 6G patent share": 0.75},
        },
        "Phase 98": {
            "title": "Roadmap + polytope",
            "key_values": {"milestones": 16, "n_predictions": 10,
                           "polytope vertices": 14, "Pass-1 progress %": 44.5},
        },
    }
    crosscuts = {
        "Tier 1 #1 (QC)":           "Quantum Internet = QC extension",
        "Tier 1 #2 (AI/ASI)":       "Federated learning, Edge AI",
        "Tier 1 #3 (Crypto)":       "QKD + PQC security",
        "Tier 1 #4 (Semi)":         "RF, photonic ICs",
        "Tier 1 #8 (Economics)":    "$8T market, digital divide",
        "Tier 1 #10 (Energy)":      "Data center consumption",
        "Tier 1 #11 (Climate)":     "Satellite observation",
        "Tier 1 #12 (Astrobiology)":"SETI communication",
        "Tier 1 #13 (Robotics)":    "Edge AI for sensorimotor",
        "Tier 0":                   "Quantum communication = ITU axiom realization",
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
    cat_color = {"obs": "#1f77b4", "6G": "#ff7f0e", "quantum": "#9467bd",
                 "satellite": "#d62728", "security": "#2ca02c", "standard": "#17becf",
                 "policy": "#8c564b", "economy": "#e377c2"}
    cat_y = {"obs": 1, "standard": 2, "6G": 3, "quantum": 4,
             "satellite": 5, "security": 6, "policy": 7, "economy": 8}
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
    ax1.set_ylim(0.5, 9.5)
    ax1.set_xlabel("Year")
    ax1.set_title("Phase 98: Communications roadmap 2026-2050 - ITU 14-vertex polytope",
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

    # Panel 3: 14-vertex polytope
    ax3 = fig.add_subplot(gs[1, 1])
    block_color = {"engineering": "#1f77b4", "medicine": "#d62728",
                   "social": "#9467bd", "philosophy": "#8c564b",
                   "biosphere": "#2ca02c", "cosmic": "#000080",
                   "embodiment": "#ff1493", "communication": "#00ced1"}
    pos = {v["id"]: (v["x"], v["y"]) for v in t3["vertices"]}
    for a, b in t3["edges"]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        is_comm = 14 in (a, b)
        ax3.plot([xa, xb], [ya, yb],
                 "#00ced1" if is_comm else "gray",
                 lw=3 if is_comm else 0.8,
                 alpha=0.85 if is_comm else 0.4,
                 zorder=1)
    for v in t3["vertices"]:
        deg = t3["degree"][v["id"]]
        size = 350 + deg * 70
        color = block_color[v["block"]]
        edgecolor = "red" if v["id"] == 14 else "black"
        edge_lw = 2.5 if v["id"] == 14 else 1.0
        ax3.scatter(v["x"], v["y"], s=size, c=color, edgecolors=edgecolor,
                    linewidths=edge_lw, alpha=0.85, zorder=3)
        ax3.annotate(f"#{v['id']}", (v["x"], v["y"]), fontsize=9,
                     ha="center", va="center", fontweight="bold", color="white", zorder=4)
        ax3.annotate(v["name"].split("(")[0].strip(), (v["x"], v["y"]),
                     xytext=(0, -22), textcoords="offset points",
                     fontsize=6, ha="center", color="black")
    ax3.set_xlim(-3, 6.5)
    ax3.set_ylim(-2, 4)
    ax3.set_aspect("equal")
    ax3.set_title(f"ITU 14-vertex polytope (K-channel axis added) | edges={t3['n_edges']} | hub: #{t3['max_degree_vertex'][0]} (deg={t3['max_degree_vertex'][1]})")
    ax3.axis("off")
    legend_elems = [mpatches.Patch(color=c, label=b) for b, c in block_color.items()]
    ax3.legend(handles=legend_elems, loc="lower left", fontsize=6)

    plt.suptitle("Phase 98: Tier 1 #14 (Communications / Networks) - final integration",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.savefig(path, dpi=110, bbox_inches="tight")
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 98: Communications roadmap + Tier 1 #14 completion")
    print("=" * 70)

    print("\n[Test 1] 2026-2050 roadmap milestones")
    t1 = test1_roadmap()
    print(f"  Total milestones: {t1['n_total']}")
    for m in t1["milestones"][:5]:
        print(f"    {m['year']} | {m['category']:11s} | {m['label']}")
    print(f"    ... ({t1['n_total'] - 5} more)")

    print("\n[Test 2] 10 falsifiable predictions")
    t2 = test2_predictions()
    print(f"  Average probability: {t2['p_avg']:.2f}")
    for p in t2["predictions"]:
        print(f"    P{p['id']:2d} ({p['year']}): {p['claim']:48s}  p={p['p']:.2f}")

    print("\n[Test 3] ITU 14-vertex polytope")
    t3 = test3_polytope()
    print(f"  Vertices: {t3['n_vertices']}")
    print(f"  Edges:    {t3['n_edges']}")
    print(f"  Max-degree vertex: #{t3['max_degree_vertex'][0]} (degree={t3['max_degree_vertex'][1]})")
    for vid, deg in sorted(t3["degree"].items(), key=lambda x: -x[1])[:6]:
        v = next(v for v in t3["vertices"] if v["id"] == vid)
        print(f"    #{vid:2d} {v['name']:32s}  degree={deg}")

    print("\n[Test 4] Tier 1 #14 cross-paper integration")
    t4 = test4_integration()
    for ph, data in t4["phases"].items():
        print(f"  {ph}: {data['title']}")
        for k, v in data["key_values"].items():
            print(f"    {k}: {v}")
    print(f"\n  Cross-cuts with other Tier 1 papers:")
    for k, v in t4["crosscuts"].items():
        print(f"    {k:28s} : {v}")

    out = {
        "phase": 98,
        "title": "Communications roadmap 2026-2050 + Tier 1 #14 completion",
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
    with open("comm_roadmap_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: comm_roadmap_summary.json")

    make_figure(t1, t2, t3, t4, "comm_roadmap.png")
    print("  ✓ Figure saved: comm_roadmap.png")

    print("\n" + "=" * 70)
    print("Phase 98 COMPLETE — Tier 1 #14 done | ITU 14-vertex polytope achieved | "
          "Pass-1 98/220 (44.5%)")
    print("=" * 70)
