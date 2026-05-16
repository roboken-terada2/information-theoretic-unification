# Phase 134: Tier 1 #19 Cosmology — Final integration + 19-vertex polytope + 10 predictions
# Tier 1 #19 Cosmology (Block A paper 3/9, phase 8/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Tier 1 #17 (QG): 10.5281/zenodo.20230667
# Tier 1 #18 (BH): 10.5281/zenodo.20233070
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 134: Tier 1 #19 Cosmology — Integration + 19-vertex polytope")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: Phase 127-133 integration table
# ----------------------------------------------------------------------
def test1_phase_integration():
    print("[Test 1] Phase 127-133 integration table")
    phases = [
        (127, "Big Bang + ΛCDM + Friedmann",            "Age 13.80 Gyr",                "dS = d<K_cosmic>"),
        (128, "Inflation + CMB + Inflaton",             "n_s=0.965, r ≈ 0.14 (φ²)",     "K_inflaton fluctuations"),
        (129, "DM + structure + S_8 tension",           "Ω_DM=0.265, S_8 3.7σ",         "K_DM hypothesis"),
        (130, "DE + Λ + DESI 2024",                     "Λ problem 120 orders",         "K_Λ vacuum"),
        (131, "Hubble + S_8 tensions",                  "Hubble 6.3σ, EDE+IDM compound", "K-superposition"),
        (132, "CMB B-mode + LiteBIRD",                  "r < 0.06, target 0.001",       "K_tensor inflation"),
        (133, "Cosmic horizons + Multiverse",           "S_dS=3.3e+122, Level I-IV",     "K-state realization space"),
    ]
    print(f"  {'Phase':>5}  {'Theme':<32}  {'Key result':<32}  {'ITU axiom check':<28}")
    print("  " + "-" * 105)
    for p, theme, key, axiom in phases:
        print(f"  {p:>5}  {theme:<32}  {key:<32}  {axiom:<28}")
    print()
    print("  Common backbone: K_cosmic (cosmic-scale modular Hamiltonian)")
    return [{"phase": p, "theme": t, "key": k, "axiom": a} for p, t, k, a in phases]


# ----------------------------------------------------------------------
# Test 2: 19-vertex polytope coupling
# ----------------------------------------------------------------------
def test2_polytope_coupling():
    print("\n[Test 2] 19-vertex polytope: Tier 1 #19 coupling to #1-#18")
    couplings = [
        (17, "QG",            "K_geom (parent)",       0.95),
        (18, "BH",            "K_horizon (dual)",      0.85),
        (10, "Energy",        "K_energy",              0.80),
        (12, "Astrobio",      "K_life",                0.65),
        (14, "Comm",          "K_channel",             0.60),
        (11, "Climate",       "K_atm",                 0.55),
        (1,  "QC",            "K_compute",             0.45),
        (2,  "AI/ASI",        "K_mind",                0.35),
        (9,  "FreeWill",      "K_agency",              0.30),
        (3,  "Crypto",        "K_secure",              0.30),
        (4,  "Semi",          "K_substrate",           0.30),
        (8,  "Economics",     "K_society",             0.20),
        (7,  "Psychiatry",    "K_self",                0.20),
        (5,  "Cancer",        "K_bio",                 0.15),
        (6,  "Aging",         "K_organism",            0.15),
        (16, "SC",            "K_city",                0.15),
        (13, "Robotics",      "K_action",              0.15),
        (15, "Infra",         "K_capital",             0.10),
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

    n_vertices = 19
    n_edges_existing = 93
    n_edges_new = 18
    n_edges_19 = n_edges_existing + n_edges_new
    avg_degree = 2 * n_edges_19 / n_vertices
    print()
    print(f"  19-vertex polytope:")
    print(f"    Vertices: {n_vertices}")
    print(f"    Edges:    {n_edges_19}")
    print(f"    Average degree <k>: {avg_degree:.2f}")
    print(f"    Tier 1 #19 degree = 18 (new max, K_cosmic hub)")
    return {"couplings": couplings, "avg_coupling": avg,
            "n_vertices": n_vertices, "n_edges": n_edges_19, "avg_degree": avg_degree}


# ----------------------------------------------------------------------
# Test 3: 10 falsifiable predictions
# ----------------------------------------------------------------------
def test3_predictions():
    print("\n[Test 3] 10 falsifiable predictions for Tier 1 #19 (2026-2050)")
    preds = [
        ( 1, "LiteBIRD r ~ 0.001 detected (5σ)",         2034, 0.85, "Strong",  "#17 QG / K_tensor"),
        ( 2, "Hubble tension >6σ confirmed",             2027, 0.80, "Strong",  "K_inflaton vs K_Λ"),
        ( 3, "DESI evolving DE w_0 ≠ -1 (>4σ)",         2027, 0.75, "Strong",  "K_Λ(t)"),
        ( 4, "S_8 tension >4σ",                          2030, 0.70, "Strong",  "#18 BH / K_DM"),
        ( 5, "CMB-S4 r ~ 0.0005 (Starobinsky test)",     2035, 0.60, "Strong",  "K_tensor inflation"),
        ( 6, "PBH asteroid window 100% DM test",         2038, 0.55, "Medium",  "#18 BH / K_DM"),
        ( 7, "EDE + IDM compound replacement of ΛCDM",   2035, 0.55, "Medium",  "K-superposition"),
        ( 8, "Anthropic Λ constraint tightening",        2040, 0.45, "Medium",  "K_observer"),
        ( 9, "LiteBIRD τ ~ 0.060 precision",             2034, 0.75, "Strong",  "K_reion"),
        (10, "Multiverse Level II indirect signature",   2050, 0.30, "Weak",    "K-vacuum landscape"),
    ]
    P_list = [p[3] for p in preds]
    P_avg = float(np.mean(P_list))
    strong = sum(1 for p in preds if p[4] == "Strong")
    medium = sum(1 for p in preds if p[4] == "Medium")
    weak = sum(1 for p in preds if p[4] == "Weak")
    print(f"  {'#':>2}  {'Prediction':<48}  {'Year':>5}  {'P':>5}  {'Verifiability':<12}")
    print("  " + "-" * 92)
    for n, name, year, P, ver, _ in preds:
        print(f"  {n:>2}  {name:<48}  {year:>5}  {P:>5.2f}  {ver:<12}")
    print()
    print(f"  Grand P_avg = {P_avg:.3f}")
    print(f"  Falsifiability: Strong = {strong}, Medium = {medium}, Weak = {weak}")
    return {"predictions": [{"id": n, "name": name, "year": y, "P": p, "ver": v, "tag": tag}
                            for n, name, y, p, v, tag in preds],
            "P_avg": P_avg, "strong_count": strong, "medium_count": medium, "weak_count": weak}


# ----------------------------------------------------------------------
# Test 4: Meta-comparison
# ----------------------------------------------------------------------
def test4_meta_comparison():
    print("\n[Test 4] Meta-comparison Tier 1 #1-#16 vs #17 vs #18 vs #19")
    cases = [
        ("Tier 1 #1-#16 (avg)",          0.590, 0.50, "10-16 (range)", "various K-states"),
        ("Tier 1 #17 Quantum Gravity",   0.625, 0.60, "16",            "K_geom (general)"),
        ("Tier 1 #18 Black Holes",       0.660, 0.70, "17 (new max)",  "K_horizon (BH inside)"),
        ("Tier 1 #19 Cosmology",         0.630, 0.60, "18 (new max)",  "K_cosmic (observer inside)"),
    ]
    print(f"  {'Tier 1':<32}  {'P_avg':>8}  {'Strong':>8}  {'Degree':<14}  {'K-state'}")
    print("  " + "-" * 90)
    for c in cases:
        print(f"  {c[0]:<32}  {c[1]:>8.3f}  {c[2]*100:>6.0f}%   {c[3]:<14}  {c[4]}")
    pass1_progress = 134 / 220 * 100
    print()
    print(f"  Pass-1 progress: 134 / 220 = {pass1_progress:.1f} %")
    return {"comparison": cases, "pass1_progress_pct": pass1_progress}


# ----------------------------------------------------------------------
# Test 5: Triadic horizon structure (#17, #18, #19)
# ----------------------------------------------------------------------
def test5_triadic_horizon():
    print("\n[Test 5] Triadic horizon structure: #17 (general) ↔ #18 (BH) / #19 (cosmic)")
    triad = [
        ("Tier 1 #17 Quantum Gravity",       "K_geom (general spacetime)",
         "Phase 111-118", "Block A 1/9"),
        ("Tier 1 #18 Black Holes",           "K_horizon (BH inside, observer OUTSIDE)",
         "Phase 119-126", "Block A 2/9 (specialization)"),
        ("Tier 1 #19 Cosmology",             "K_cosmic (de Sitter, observer INSIDE)",
         "Phase 127-134", "Block A 3/9 (dual specialization)"),
    ]
    print(f"  {'Paper':<34}  {'K-state':<42}  {'Phases'}")
    print("  " + "-" * 95)
    rows = []
    for name, k, phases, block in triad:
        print(f"  {name:<34}  {k:<42}  {phases}")
        rows.append({"paper": name, "k_state": k, "phases": phases, "block": block})
    print()
    print("  → #17 = general theory; #18 & #19 = inside/outside dual specializations.")
    print("  → Three papers form a horizon TRIAD anchoring Block A.")
    return {"triad": rows}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
phases = test1_phase_integration()
polytope = test2_polytope_coupling()
preds = test3_predictions()
meta = test4_meta_comparison()
triad = test5_triadic_horizon()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Phase 127-133 integration timeline
ax = axes[0, 0]
ax.axis("off")
ax.set_title("Tier 1 #19 — Phase 127-133 integration", fontsize=12, fontweight="bold")
y = 0.92
for ph in phases:
    ax.text(0.02, y, f"P{ph['phase']}", fontsize=11, fontweight="bold", color="#4c72b0")
    ax.text(0.10, y, ph["theme"], fontsize=9, color="black")
    ax.text(0.50, y, ph["key"], fontsize=8, color="gray", fontfamily="monospace")
    y -= 0.12
ax.text(0.02, 0.03, "Common backbone: K_cosmic (cosmic-scale modular Hamiltonian)",
        fontsize=10, fontstyle="italic", color="#55a467")

# Panel 2: 19-vertex polytope coupling
ax = axes[0, 1]
labels = [f"#{c[0]} {c[1]}" for c in polytope["couplings"]]
values = [c[3] for c in polytope["couplings"]]
colors_q = plt.cm.viridis(np.linspace(0, 1, len(labels)))
y_pos = np.arange(len(labels))
ax.barh(y_pos, values, color=colors_q)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=7)
ax.set_xlabel("Coupling to Tier 1 #19 (K_cosmic)")
ax.axvline(polytope["avg_coupling"], color="red", linestyle="--", linewidth=1,
           label=f"avg = {polytope['avg_coupling']:.2f}")
ax.set_xlim(0, 1.05)
ax.invert_yaxis()
ax.set_title(f"19-vertex polytope: #19 K_cosmic hub (deg 18 new max)", fontsize=11)
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
ax.set_title(f"10 falsifiable predictions (Strong: {preds['strong_count']}, Med: {preds['medium_count']}, Weak: {preds['weak_count']})",
             fontsize=11)
ax.set_ylim(0, 1.0)
ax.legend(fontsize=9, loc="upper right")
ax.grid(True, alpha=0.3, axis="y")

# Panel 4: Triadic horizon structure
ax = axes[1, 1]
ax.axis("off")
ax.set_title("Horizon TRIADIC structure (#17, #18, #19)", fontsize=12, fontweight="bold")
y = 0.88
for r in triad["triad"]:
    ax.text(0.02, y, r["paper"], fontsize=10, fontweight="bold", color="#4c72b0")
    y -= 0.08
    ax.text(0.05, y, r["k_state"], fontsize=9, color="#c44e52", fontfamily="monospace")
    y -= 0.08
    ax.text(0.05, y, f"{r['phases']}  |  {r['block']}", fontsize=8, color="gray")
    y -= 0.14
ax.text(0.02, 0.10, "★ #17 = general; #18 = BH inside; #19 = cosmic inside (dual)",
        fontsize=10, fontstyle="italic", color="#55a467")
ax.text(0.02, 0.04, f"★ Pass-1 progress: 134 / 220 = {meta['pass1_progress_pct']:.1f} %",
        fontsize=10, fontstyle="italic", color="#55a467", fontweight="bold")

fig.suptitle("Phase 134: Tier 1 #19 Cosmology — Integration + 19-vertex polytope + 10 predictions",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "tier1_19_integration.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 134,
    "title": "Tier 1 #19 Cosmology integration + 19-vertex polytope + 10 predictions",
    "tier1_id": 19,
    "tier1_name": "Cosmology",
    "block": "A (Physics/Math) — paper 3/9 COMPLETE",
    "phase_integration": phases,
    "polytope_19": polytope,
    "predictions": preds,
    "meta_comparison": meta,
    "triadic_horizon": triad,
    "completion_status": {
        "phases_completed": [127, 128, 129, 130, 131, 132, 133, 134],
        "all_phases_done": True,
        "block_A_papers_done": 3,
        "block_A_papers_total": 9,
    },
    "verdict": ("Tier 1 #19 Cosmology complete: 8 phases, 10 predictions "
                "(P_avg = 0.630), polytope extended to 19 vertices with #19 "
                "as K_cosmic hub (degree 18, new max). Horizon TRIAD #17/#18/#19. "
                "Pass-1 progress 134/220 = 60.9 %."),
}

json_path = "tier1_19_integration_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 134 complete: Tier 1 #19 Cosmology finished;")
print(f"  10 predictions P_avg = {preds['P_avg']:.3f}; Pass-1 progress = {meta['pass1_progress_pct']:.1f} %")
print("=" * 70)
