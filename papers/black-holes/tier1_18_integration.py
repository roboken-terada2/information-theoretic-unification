# Phase 126: Tier 1 #18 Black Holes — Final integration + 18-vertex polytope + 10 predictions
# Tier 1 #18 Black Holes (Block A paper 2/9, phase 8/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Tier 1 #17 (QG): 10.5281/zenodo.20230667
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 126: Tier 1 #18 Black Holes — Integration + 18-vertex polytope")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: Phase 119-125 integration table
# ----------------------------------------------------------------------
def test1_phase_integration():
    print("[Test 1] Phase 119-125 integration table")
    phases = [
        (119, "Schwarzschild + Kerr + No-hair",      "r_ISCO, Penrose 29.29%",          "K_geom stationary points"),
        (120, "BH 4 laws + Hawking radiation",       "dMc^2 = T_H dS rel diff 8.4e-4",  "dS = d<K_geom> embedded"),
        (121, "Page curve rigorous + QECC",          "t_Page = 0.643, I(R:B)=1.00",     "Page-Yang QECC"),
        (122, "Info paradox resolutions",            "7 resolutions under K-axiom",     "Fuzzball/SoftHair/MM/etc."),
        (123, "AdS/CFT + Bekenstein + Complexity",   "T_HP=0.4775, Bek saturated",      "K-state phase transition"),
        (124, "Maxwell demon + Q-BH simulation",     "I(R_i:R_j) spike at t_Page",      "K_info conservation"),
        (125, "PBH + higher corr + merger stats",    "f_PBH <~10%, scrambling bound",   "K-flow chaos"),
    ]
    print(f"  {'Phase':>5}  {'Theme':<32}  {'Key result':<32}  {'ITU axiom check':<28}")
    print("  " + "-" * 102)
    for p, theme, key, axiom in phases:
        print(f"  {p:>5}  {theme:<32}  {key:<32}  {axiom:<28}")
    print()
    print("  Common backbone: K_horizon = K_geom restricted to BH horizon")
    return [{"phase": p, "theme": t, "key": k, "axiom": a} for p, t, k, a in phases]


# ----------------------------------------------------------------------
# Test 2: 18-vertex polytope coupling
# ----------------------------------------------------------------------
def test2_polytope_coupling():
    print("\n[Test 2] 18-vertex polytope: Tier 1 #18 coupling to #1-#17")
    couplings = [
        (17, "QG",            "K_geom (parent)", 1.00),
        (1,  "QC",            "K_compute (QECC)", 0.85),
        (2,  "AI/ASI",        "K_mind", 0.40),
        (3,  "Crypto",        "K_secure", 0.45),
        (4,  "Semi",          "K_substrate", 0.30),
        (5,  "Cancer",        "K_bio", 0.10),
        (6,  "Aging",         "K_organism", 0.10),
        (7,  "Psychiatry",    "K_self", 0.10),
        (8,  "Economics",     "K_society", 0.10),
        (9,  "FreeWill",      "K_agency", 0.15),
        (10, "Energy",        "K_energy", 0.85),
        (11, "Climate",       "K_atm", 0.50),
        (12, "Astrobio",      "K_life", 0.40),
        (13, "Robotics",      "K_action", 0.20),
        (14, "Comm",          "K_channel", 0.70),
        (15, "Infra",         "K_capital", 0.15),
        (16, "SC",            "K_city", 0.15),
    ]
    n = len(couplings)
    avg = sum(c for _, _, _, c in couplings) / n
    strong = [c[1] for c in couplings if c[3] >= 0.75]
    medium = [c[1] for c in couplings if 0.5 <= c[3] < 0.75]
    weak = [c[1] for c in couplings if c[3] < 0.5]
    print(f"  Average coupling: {avg:.3f}")
    print(f"  Strong (>=0.75): {strong}")
    print(f"  Medium (0.5-0.75): {medium}")
    print(f"  Weak (<0.5): {weak}")

    # 18-vertex polytope statistics
    n_vertices = 18
    n_edges_existing = 76
    n_edges_new = 17   # #18 connects to all 17 existing
    n_edges_18 = n_edges_existing + n_edges_new
    avg_degree = 2 * n_edges_18 / n_vertices
    print()
    print(f"  18-vertex polytope:")
    print(f"    Vertices: {n_vertices}")
    print(f"    Edges:    {n_edges_18}")
    print(f"    Average degree <k>: {avg_degree:.2f}")
    print(f"    Tier 1 #18 degree = 17 (new max, K-horizon hub)")
    return {"couplings": couplings, "avg_coupling": avg,
            "n_vertices": n_vertices, "n_edges": n_edges_18, "avg_degree": avg_degree}


# ----------------------------------------------------------------------
# Test 3: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test3_predictions():
    print("\n[Test 3] 10 falsifiable predictions for Tier 1 #18 (2026-2050)")
    preds = [
        ( 1, "EHT M87* shadow refined to 5 uas",         2030, 0.90, "Strong",  "#14 Comm"),
        ( 2, "GWTC-5 catalog 300+ BBH (LIGO O5)",        2030, 0.85, "Strong",  "#14 Comm"),
        ( 3, "Sgr A* Kerr deviation < 1%",               2035, 0.75, "Strong",  "#17 QG"),
        ( 4, "LISA IMBH (10^2-10^5 M_sun) detected",     2038, 0.70, "Strong",  "#17 QG"),
        ( 5, "Pair-instability gap 45-80 M_sun verified", 2032, 0.65, "Strong",  "stellar evolution"),
        ( 6, "PBH asteroid-mass window constrained",      2038, 0.55, "Medium",  "#1 QC"),
        ( 7, "Quantum-computer 100-qubit BH simulation",  2032, 0.70, "Strong",  "#1 QC"),
        ( 8, "BMV gravitational entanglement detected",   2032, 0.65, "Strong",  "#17 QG"),
        ( 9, "Hawking-Page transition CFT realized",     2040, 0.40, "Medium",  "AdS/CFT"),
        (10, "SMBH origin (DC vs PBH) resolved",         2045, 0.45, "Medium",  "#11 Climate"),
    ]
    P_list = [p[3] for p in preds]
    P_avg = float(np.mean(P_list))
    strong_count = sum(1 for p in preds if p[4] == "Strong")
    medium_count = sum(1 for p in preds if p[4] == "Medium")
    print(f"  {'#':>2}  {'Prediction':<48}  {'Year':>5}  {'P':>5}  {'Verifiability':<12}")
    print("  " + "-" * 90)
    for n, name, year, P, ver, _ in preds:
        print(f"  {n:>2}  {name:<48}  {year:>5}  {P:>5.2f}  {ver:<12}")
    print()
    print(f"  Grand P_avg = {P_avg:.3f}")
    print(f"  Falsifiability: Strong = {strong_count}, Medium = {medium_count}")
    return {"predictions": [{"id": n, "name": name, "year": y, "P": p, "ver": v, "tag": tag}
                            for n, name, y, p, v, tag in preds],
            "P_avg": P_avg, "strong_count": strong_count, "medium_count": medium_count}


# ----------------------------------------------------------------------
# Test 4: Meta-comparison Tier 1 #1-#16 vs #17 vs #18
# ----------------------------------------------------------------------
def test4_meta_comparison():
    print("\n[Test 4] Meta-comparison Tier 1 #1-#16 vs #17 vs #18")
    cases = [
        ("Tier 1 #1-#16 (avg)",  0.590, 0.50, "10-16 (range)"),
        ("Tier 1 #17 Quantum Gravity", 0.625, 0.60, "16"),
        ("Tier 1 #18 Black Holes",     0.660, 0.70, "17 (new max)"),
    ]
    print(f"  {'Tier 1':<26}  {'P_avg':>8}  {'Strong %':>10}  {'Degree':<14}")
    print("  " + "-" * 65)
    for c in cases:
        print(f"  {c[0]:<26}  {c[1]:>8.3f}  {c[2]*100:>9.0f}%   {c[3]:<14}")
    print()
    pass1_progress = 126 / 220 * 100
    print(f"  Pass-1 progress: 126 / 220 = {pass1_progress:.1f} %")
    return {"comparison": cases,
            "pass1_progress_pct": pass1_progress}


# ----------------------------------------------------------------------
# Test 5: #17 ↔ #18 specialization mapping
# ----------------------------------------------------------------------
def test5_specialization_mapping():
    print("\n[Test 5] #17 QG (general) ↔ #18 BH (horizon specialization)")
    mapping = [
        ("Phase 111 (AdS/CFT + RT)",          "Phase 119 (Schwarzschild + Kerr)"),
        ("Phase 112 (ER=EPR + TFD)",          "Phase 120 (BH 4 laws + Hawking)"),
        ("Phase 113 (Page curve + Island)",   "Phase 121 (Page curve rigorous + QECC)"),
        ("Phase 114 (Firewall + Planck)",     "Phase 122 (Info paradox resolutions)"),
        ("Phase 115 (LQG + area spectrum)",   "Phase 123 (AdS/CFT BH + complexity)"),
        ("Phase 116 (String + Strominger-Vafa)", "Phase 124 (Maxwell + Q-BH sim)"),
        ("Phase 117 (QG experiments)",        "Phase 125 (PBH + merger stats)"),
        ("Phase 118 (17-vertex integration)",  "Phase 126 (18-vertex integration)"),
    ]
    print(f"  {'Tier 1 #17 (general)':<40}  {'Tier 1 #18 (BH horizon special.)':<42}")
    print("  " + "-" * 86)
    for a, b in mapping:
        print(f"  {a:<40}  {b:<42}")
    print()
    print("  → Symmetric pair: #17 and #18 mirror each other phase-by-phase")
    return {"mapping": [{"tier17": a, "tier18": b} for a, b in mapping]}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
phases = test1_phase_integration()
polytope = test2_polytope_coupling()
preds = test3_predictions()
meta = test4_meta_comparison()
specialization = test5_specialization_mapping()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Phase 119-126 integration timeline
ax = axes[0, 0]
ax.axis("off")
ax.set_title("Tier 1 #18 — Phase 119-125 integration", fontsize=12, fontweight="bold")
y = 0.92
for ph in phases:
    ax.text(0.02, y, f"P{ph['phase']}", fontsize=11, fontweight="bold", color="#4c72b0")
    ax.text(0.10, y, ph["theme"], fontsize=9, color="black")
    ax.text(0.55, y, ph["key"], fontsize=8, color="gray", fontfamily="monospace")
    y -= 0.12
ax.text(0.02, 0.03, "Common backbone: K_horizon (K_geom restricted to BH horizon)",
        fontsize=10, fontstyle="italic", color="#55a467")

# Panel 2: 18-vertex polytope coupling
ax = axes[0, 1]
labels = [f"#{c[0]} {c[1]}" for c in polytope["couplings"]]
values = [c[3] for c in polytope["couplings"]]
colors_q = plt.cm.viridis(np.linspace(0, 1, len(labels)))
y_pos = np.arange(len(labels))
ax.barh(y_pos, values, color=colors_q)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=7)
ax.set_xlabel("Coupling to Tier 1 #18 (K_horizon)")
ax.axvline(polytope["avg_coupling"], color="red", linestyle="--", linewidth=1,
           label=f"avg = {polytope['avg_coupling']:.2f}")
ax.set_xlim(0, 1.05)
ax.invert_yaxis()
ax.set_title(f"18-vertex polytope: #18 K-horizon hub (deg 17 new max)", fontsize=11)
ax.legend(fontsize=9, loc="lower right")

# Panel 3: 10 predictions
ax = axes[1, 0]
pred_ids = [p["id"] for p in preds["predictions"]]
P_vals = [p["P"] for p in preds["predictions"]]
years = [p["year"] for p in preds["predictions"]]
ver_colors = {"Strong": "#55a467", "Medium": "#dd8452", "Weak": "#c44e52"}
colors_ver = [ver_colors[p["ver"]] for p in preds["predictions"]]
bars = ax.bar([str(i) for i in pred_ids], P_vals, color=colors_ver)
for i, (b, y, p) in enumerate(zip(bars, years, P_vals)):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.02,
            f"{y}", ha="center", fontsize=8, color="black")
ax.axhline(preds["P_avg"], color="red", linestyle="--", linewidth=1,
           label=f"P_avg = {preds['P_avg']:.3f}")
ax.set_xlabel("Prediction #")
ax.set_ylabel("Probability P")
ax.set_title(f"10 falsifiable predictions (Strong: {preds['strong_count']}, Medium: {preds['medium_count']})",
             fontsize=12)
ax.set_ylim(0, 1.0)
ax.legend(fontsize=9, loc="upper right")
ax.grid(True, alpha=0.3, axis="y")

# Panel 4: Meta-comparison + Pass-1 progress
ax = axes[1, 1]
ax.axis("off")
ax.set_title("Tier 1 #18 meta-comparison", fontsize=12, fontweight="bold")
y = 0.92
lines = [
    ("Tier 1 #1-#16 grand P_avg",         "0.590"),
    ("Tier 1 #17 (QG) P_avg",             "0.625"),
    ("Tier 1 #18 (BH) P_avg",             f"{preds['P_avg']:.3f}"),
    ("Difference (#18 - #17)",            f"+{preds['P_avg'] - 0.625:.3f}"),
    ("", ""),
    ("Polytope degree:",                  ""),
    ("  #16 Smart Cities (URBAN hub)",    "15"),
    ("  #17 Quantum Gravity (K-skel.)",   "16"),
    ("  #18 Black Holes (K-horizon)",     "17  ← NEW MAX"),
    ("", ""),
    ("Pass-1 progress",                   f"126 / 220 = {meta['pass1_progress_pct']:.1f} %"),
]
y = 0.94
for k, v in lines:
    if k:
        ax.text(0.02, y, k, fontsize=10, color="#4c72b0")
        ax.text(0.66, y, v, fontsize=10, fontfamily="monospace", color="#c44e52")
    y -= 0.085
ax.text(0.02, 0.04,
        "Block A 2/9 complete → next: Tier 1 #19 Cosmology (Phase 127-)",
        fontsize=10, fontstyle="italic", color="#55a467")

fig.suptitle("Phase 126: Tier 1 #18 Black Holes — Integration + 18-vertex polytope + 10 predictions",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "tier1_18_integration.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 126,
    "title": "Tier 1 #18 Black Holes integration + 18-vertex polytope + 10 predictions",
    "tier1_id": 18,
    "tier1_name": "Black Holes",
    "block": "A (Physics/Math) — paper 2/9 COMPLETE",
    "phase_integration": phases,
    "polytope_18": polytope,
    "predictions": preds,
    "meta_comparison": meta,
    "specialization_mapping_17_to_18": specialization,
    "completion_status": {
        "phases_completed": [119, 120, 121, 122, 123, 124, 125, 126],
        "all_phases_done": True,
        "block_A_papers_done": 2,
        "block_A_papers_total": 9,
    },
    "verdict": ("Tier 1 #18 Black Holes complete: 8 phases, 10 predictions "
                "(P_avg = 0.660), polytope extended to 18 vertices with #18 as "
                "K-horizon hub (degree 17, new max). Pass-1 progress 126/220 = 57.3 %."),
}

json_path = "tier1_18_integration_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 126 complete: Tier 1 #18 Black Holes finished;")
print(f"  10 predictions P_avg = {preds['P_avg']:.3f}; Pass-1 progress = {meta['pass1_progress_pct']:.1f} %")
print("=" * 70)
