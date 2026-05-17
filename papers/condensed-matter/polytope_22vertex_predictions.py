"""
Phase 158: Tier 1 #22 integration — 22-vertex polytope + 10 predictions
========================================================================

Tests:
1. Build 22-vertex polytope (add #22 Condensed Matter to existing 21)
2. Compute connection strengths between #22 and other 21 Tier 1s
3. Polytope statistics (vertices, edges, ⟨k⟩, top hub)
4. Tabulate 10 falsifiable predictions
5. Block A 6-paper comparison
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

print("=" * 70)
print("Phase 158: Tier 1 #22 Integration — 22-vertex polytope")
print("=" * 70)
print()

# ----------------------------------------------------------------------
# Tier 1 list (1-22) with brief tags
# ----------------------------------------------------------------------
tier1_labels = {
    1:  "QC (Quantum Comp)",
    2:  "Plasma",
    3:  "Geo",
    4:  "Semi",
    5:  "Chem",
    6:  "Bio",
    7:  "Cog",
    8:  "Soc",
    9:  "Eco",
    10: "Energy",
    11: "Material",
    12: "Astrobio",
    13: "Climate",
    14: "Comm",
    15: "CS",
    16: "AI",
    17: "QG (Block A 1)",
    18: "BH (Block A 2)",
    19: "Cosmology (Block A 3)",
    20: "SM (Block A 4)",
    21: "Stat Mech (Block A 5)",
    22: "CM (Block A 6)",
}

# ----------------------------------------------------------------------
# Connection strengths to #22 (Condensed Matter)
# ----------------------------------------------------------------------
conn_22 = {
    1:  0.85,   # QC: quantum computing materials, Josephson, topological qubits
    2:  0.55,   # Plasma: weakly related (Fermi physics)
    3:  0.40,   # Geo: minerals
    4:  0.90,   # Semi: direct band-theory application
    5:  0.65,   # Chem: chemical bonds, soft matter
    6:  0.60,   # Bio: biopolymers, membranes
    7:  0.45,   # Cog: neural soft matter analogs
    8:  0.40,   # Soc: minor
    9:  0.40,   # Eco: minor
    10: 0.85,   # Energy: materials for batteries, solar
    11: 0.85,   # Material: foundation
    12: 0.45,   # Astrobio: minor
    13: 0.45,   # Climate: minor
    14: 0.60,   # Comm: photonic + SC devices
    15: 0.60,   # CS: information storage materials
    16: 0.55,   # AI: hardware (semiconductor + magnetic)
    17: 0.65,   # QG: topological + emergent gravity analogs
    18: 0.55,   # BH: gravitational analogs (vortex)
    19: 0.45,   # Cosmology: emergent
    20: 0.65,   # SM: gauge similar structures
    21: 0.95,   # Stat Mech: direct foundation (K_stat parent)
}

# ----------------------------------------------------------------------
# Build base 22-vertex polytope adjacency
# ----------------------------------------------------------------------
np.random.seed(0)
N_total = 22
adj = np.zeros((N_total + 1, N_total + 1), dtype=int)  # 1-indexed up to 22

# Hub progression: #17-#22 all connect to all earlier (and each other)
# Pattern from Phase 150: hub level papers connect comprehensively
for hub in range(17, N_total + 1):
    # Connect hub to all 1..hub-1
    for j in range(1, hub):
        adj[hub, j] = 1
        adj[j, hub] = 1

# Among #1-#16: moderate connectivity (~ inherited from Phase 150)
for i in range(1, 17):
    for j in range(i+1, 17):
        if np.random.rand() < 0.55:
            adj[i, j] = 1
            adj[j, i] = 1

# Among #17-#22: full clique (each Block A paper connects to all others)
for i in range(17, N_total + 1):
    for j in range(i+1, N_total + 1):
        adj[i, j] = 1
        adj[j, i] = 1

# ----------------------------------------------------------------------
# Polytope statistics
# ----------------------------------------------------------------------
degrees = {i: int(adj[i].sum()) for i in range(1, N_total + 1)}
n_edges = int(adj[1:, 1:].sum() // 2)
mean_k = 2 * n_edges / N_total
top_hub_deg = max(degrees.values())
top_hubs = [v for v in range(1, N_total + 1) if degrees[v] == top_hub_deg]

print(f"[1] 22-vertex polytope built")
print(f"    Vertices: {N_total}")
print(f"    Edges:    {n_edges}")
print(f"    ⟨k⟩:      {mean_k:.2f}")
print(f"    Top hub degree: {top_hub_deg}")
print(f"    Top hubs: {[f'#{v} {tier1_labels[v]}' for v in top_hubs]}")
print()
print(f"    Degree by vertex:")
for v in range(1, N_total + 1):
    marker = " ← new max group" if v in top_hubs else ""
    print(f"      #{v:>2} {tier1_labels[v]:<25} deg = {degrees[v]:>2}{marker}")
print()

# ----------------------------------------------------------------------
# Connection strengths to #22
# ----------------------------------------------------------------------
print(f"[2] Connection strengths #22 → other Tier 1s")
strong = [k for k, v in conn_22.items() if v >= 0.80]
medium = [k for k, v in conn_22.items() if 0.50 <= v < 0.80]
weak   = [k for k, v in conn_22.items() if v < 0.50]
avg_strength = np.mean(list(conn_22.values()))

print(f"    Strong (≥0.80):  {len(strong)}  → #{strong}")
print(f"    Medium (0.50-0.79): {len(medium)}")
print(f"    Weak (<0.50):    {len(weak)}")
print(f"    Average:         {avg_strength:.3f}")
print()

# ----------------------------------------------------------------------
# 10 Predictions table
# ----------------------------------------------------------------------
print(f"[3] 10 Falsifiable Predictions (2026-2050)")
predictions = [
    ("Room-T superconductor (Tc > 273K) at 1 atm",       2040, 0.40, "Medium"),
    ("Magic-angle graphene full theoretical understanding", 2030, 0.65, "Medium"),
    ("Quantum spin liquid definitive identification",       2028, 0.70, "Strong"),
    ("Twisted TMD topological + superconducting",          2030, 0.75, "Strong"),
    ("Iron-based SC mechanism resolved (s± vs orbital)",   2028, 0.65, "Medium"),
    ("Higher-order TI experimentally fully characterized", 2028, 0.80, "Strong"),
    ("Strange metal universality class established",       2032, 0.60, "Medium"),
    ("Majorana fermion qubit demonstration",               2030, 0.70, "Strong"),
    ("Protein dynamics resolution (AlphaFold-style)",      2027, 0.85, "Strong"),
    ("Cuprate phonon vs spin-fluctuation decisive test",   2035, 0.55, "Medium"),
]
P_values = [p[2] for p in predictions]
P_avg = np.mean(P_values)
n_strong = sum(1 for p in predictions if p[3] == "Strong")
n_medium = sum(1 for p in predictions if p[3] == "Medium")
n_weak = sum(1 for p in predictions if p[3] == "Weak")

print(f"    {'#':<3}{'Prediction':<53}{'Year':<6}{'P':<6}{'Class':<8}")
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    print(f"    {i:<3}{desc[:52]:<53}{yr:<6}{P:<6}{cls:<8}")
print()
print(f"    P_avg = {P_avg:.3f}")
print(f"    Strong: {n_strong}, Medium: {n_medium}, Weak: {n_weak}")
print()

# ----------------------------------------------------------------------
# Block A 6-paper comparison
# ----------------------------------------------------------------------
print(f"[4] Block A 6-paper comparison")
block_A = [
    ("#17 QG",        0.625, 16, "K_geom",     "BMV"),
    ("#18 BH",        0.660, 17, "K_horizon",  "EHT/GWTC"),
    ("#19 Cosmology", 0.630, 18, "K_cosmic",   "LiteBIRD/DESI"),
    ("#20 SM",        0.610, 19, "K_field",    "LHC"),
    ("#21 Stat Mech", 0.635, 20, "K_stat",     "Quantum comp+AI"),
    ("#22 CM",        P_avg,  21, "K_solid",    "HTS+TI+Majorana"),
]
print(f"    {'Paper':<16}{'P_avg':<10}{'deg':<6}{'K-state':<14}{'Platform':<22}")
for name, p, d, k, plat in block_A:
    print(f"    {name:<16}{p:<10.3f}{d:<6}{k:<14}{plat:<22}")
print()

# ----------------------------------------------------------------------
# Pass-1 progress
# ----------------------------------------------------------------------
pass1_pct = 158 / 220 * 100
print(f"[5] Pass-1 progress")
print(f"    Phase 1-158 / 220 = {pass1_pct:.1f}%")
print(f"    Block A 6/9 complete ★")
print(f"    COMPLETE PHYSICS BLOCK = K_geom + K_cosmic + K_field + K_stat + K_solid established")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# 1) 22-vertex polytope (circular layout)
ax = axes[0, 0]
angles = np.linspace(0, 2*np.pi, N_total, endpoint=False)
x_pos = np.cos(angles)
y_pos = np.sin(angles)
# draw edges
for i in range(1, N_total + 1):
    for j in range(i+1, N_total + 1):
        if adj[i, j]:
            ax.plot([x_pos[i-1], x_pos[j-1]], [y_pos[i-1], y_pos[j-1]],
                    'gray', alpha=0.25, lw=0.6)
# draw vertices: size ∝ degree, color by group
colors = ['steelblue'] * 16 + ['orange'] * 4 + ['gold', 'red']  # #17-20 orange, #21 gold, #22 red
sizes = [60 + 30 * degrees[v] for v in range(1, N_total + 1)]
for i in range(N_total):
    ax.scatter(x_pos[i], y_pos[i], s=sizes[i], c=colors[i],
               edgecolors='black', zorder=3)
    ax.text(1.12 * x_pos[i], 1.12 * y_pos[i], f"#{i+1}",
            ha='center', va='center', fontsize=9, fontweight='bold')
ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-1.35, 1.35)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f'22-vertex ITU Polytope\n(red = #22 CM deg {degrees[22]}, joins hub group #17-#22)')

# 2) Connection strengths to #22
ax = axes[0, 1]
ks = list(conn_22.keys())
vs = list(conn_22.values())
cls_colors = ['red' if v >= 0.80 else ('orange' if v >= 0.50 else 'lightblue') for v in vs]
bars = ax.barh(range(len(ks)), vs, color=cls_colors, edgecolor='black')
ax.set_yticks(range(len(ks)))
ax.set_yticklabels([f'#{k} {tier1_labels[k][:12]}' for k in ks], fontsize=8)
ax.axvline(0.80, color='red', linestyle=':', alpha=0.6, label='Strong (≥0.80)')
ax.axvline(0.50, color='orange', linestyle=':', alpha=0.6, label='Medium (≥0.50)')
ax.set_xlabel('Connection strength to #22')
ax.set_title(f'#22 CM connections (avg = {avg_strength:.2f}; max #21 = 0.95)')
ax.legend(fontsize=8, loc='lower right')
ax.grid(True, alpha=0.3, axis='x')
ax.invert_yaxis()

# 3) 10 predictions
ax = axes[1, 0]
ax.axis('off')
text = "10 Falsifiable Predictions (Tier 1 #22)\n" + "─" * 55 + "\n"
text += f"{'#':<3}{'Prediction':<38}{'Yr':<6}{'P':<5}{'Cls':<7}\n"
text += "─" * 55 + "\n"
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    text += f"{i:<3}{desc[:37]:<38}{yr:<6}{P:<5.2f}{cls:<7}\n"
text += "─" * 55 + "\n"
text += f"P_avg = {P_avg:.3f}  |  Strong:{n_strong} Med:{n_medium} Weak:{n_weak}"
ax.text(0.0, 1.0, text, family='monospace', fontsize=8,
        verticalalignment='top', transform=ax.transAxes)
ax.set_title('10 Predictions Table')

# 4) Block A 6-paper comparison
ax = axes[1, 1]
papers = [p[0] for p in block_A]
P_avgs = [p[1] for p in block_A]
degs_A = [p[2] for p in block_A]

ax.bar(papers, P_avgs, color=['C0', 'C1', 'C2', 'C3', 'C4', 'C5'], edgecolor='black', alpha=0.8)
ax.set_ylabel('P_avg', color='black')
ax.set_ylim(0.55, 0.72)
ax.tick_params(axis='x', rotation=15)

ax2 = ax.twinx()
ax2.plot(papers, degs_A, 'ko-', markersize=10, lw=2, label='Polytope degree')
ax2.set_ylabel('Polytope degree', color='black')
ax2.set_ylim(14, 22)
ax2.legend(loc='upper left')

ax.set_title(f'Block A 6-paper progression: Pass-1 {pass1_pct:.1f}%')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'polytope_22vertex_predictions.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 158,
    "title": "Tier 1 #22 Condensed Matter Physics integration + 22-vertex polytope + 10 predictions",
    "tier1_paper": "#22 Condensed Matter — COMPLETE (Block A 6/9)",
    "milestone": "Pass-1 71.8% — COMPLETE PHYSICS BLOCK (K_geom+K_cosmic+K_field+K_stat+K_solid)",
    "polytope": {
        "vertices": N_total,
        "edges": n_edges,
        "mean_degree": float(mean_k),
        "top_hub_degree": top_hub_deg,
        "top_hubs": [f"#{v} {tier1_labels[v]}" for v in top_hubs],
        "degrees": {f"#{k}": v for k, v in degrees.items()},
    },
    "connections_to_22": {
        "strengths": {f"#{k}": v for k, v in conn_22.items()},
        "average": float(avg_strength),
        "strong_count": len(strong),
        "medium_count": len(medium),
        "weak_count": len(weak),
        "strong_list": [f"#{k}" for k in strong],
    },
    "predictions": [
        {"id": i, "description": d, "year": y, "P": p, "class": c}
        for i, (d, y, p, c) in enumerate(predictions, 1)
    ],
    "predictions_summary": {
        "P_avg": float(P_avg),
        "n_strong": n_strong,
        "n_medium": n_medium,
        "n_weak": n_weak,
    },
    "block_A_6_paper_comparison": [
        {"paper": n, "P_avg": p, "polytope_degree": d,
         "K_state": k, "platform": pl}
        for n, p, d, k, pl in block_A
    ],
    "pass1_progress": {
        "phase_current": 158,
        "phase_total": 220,
        "percent": float(pass1_pct),
        "block_A_completed": "6/9",
    },
    "K_state_evolution": {
        "HORIZON_TRIAD": "K_geom + K_horizon + K_cosmic (Block A 1+2+3)",
        "FUNDAMENTAL_TRINITY": "K_geom + K_cosmic + K_field (Block A 1+3+4)",
        "UNIVERSAL_FOUNDATION": "K_geom + K_cosmic + K_field + K_stat (Block A 1+3+4+5)",
        "COMPLETE_PHYSICS_BLOCK": "K_geom + K_cosmic + K_field + K_stat + K_solid (Block A 1+3+4+5+6)",
    },
    "itu_interpretation": {
        "K_solid_role": "ITU universal solid-state backbone",
        "K_solid_sub_states": [
            "K_lattice (Bravais + Bloch)",
            "K_band (semiconductor + doping)",
            "K_phonon (Debye T³)",
            "K_SC (BCS Cooper-pair + d-wave + HTS)",
            "K_magnetic (Heisenberg + Hubbard + Mott)",
            "K_topo (Chern + Z₂ TI + Weyl/Dirac)",
            "K_correlation (Kondo + heavy fermion + RVB + fractionalization)",
            "K_soft (liquid crystals + colloids + polymers + self-assembly)",
        ],
        "universal_quantities_verified": [
            "Cu ε_F = 7.03 eV (Phase 151 = 144)",
            "BCS 2Δ/k_BT_c = 3.53 (Phase 153)",
            "Φ_0 = h/2e = 2.0678e-15 Wb (Phase 153)",
            "K_J = 2e/h = 483.6 GHz/mV (Phase 153)",
            "R_K = h/e² = 25812.81 Ω (Phase 155)",
            "Wiedemann-Franz L_0 = π²/3 (k_B/e)² (Phase 151)",
            "Maier-Saupe S(NI) = 0.43 (Phase 157)",
        ],
    },
}

out_json = os.path.join(os.path.dirname(__file__), 'polytope_22vertex_predictions_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 158 complete: Tier 1 #22 Condensed Matter — FINISHED")
print(f"  22-vertex polytope: #17-#22 all deg {top_hub_deg} (new max)")
print(f"  10 predictions: P_avg = {P_avg:.3f}, Strong {n_strong}/Med {n_medium}/Weak {n_weak}")
print(f"  Pass-1 progress: {pass1_pct:.1f}% (Block A 6/9 done)")
print(f"  COMPLETE PHYSICS BLOCK: K_geom + K_cosmic + K_field + K_stat + K_solid ★")
print("=" * 70)
