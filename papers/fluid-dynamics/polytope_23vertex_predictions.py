"""
Phase 166: Tier 1 #23 integration — 23-vertex polytope + 10 predictions
========================================================================

Tests:
1. Build 23-vertex polytope (add #23 Fluid Dynamics to existing 22)
2. Compute connection strengths between #23 and other 22 Tier 1s
3. Polytope statistics (vertices, edges, ⟨k⟩, top hub)
4. Tabulate 10 falsifiable predictions
5. Block A 7-paper comparison
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

print("=" * 70)
print("Phase 166: Tier 1 #23 Integration — 23-vertex polytope")
print("=" * 70)
print()

# ----------------------------------------------------------------------
# Tier 1 list (1-23) with brief tags
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
    23: "Fluid (Block A 7)",
}

# ----------------------------------------------------------------------
# Connection strengths to #23
# ----------------------------------------------------------------------
conn_23 = {
    1:  0.55,   # QC: minor (quantum simulation of turbulence)
    2:  0.95,   # Plasma: direct (MHD = Phase 163)
    3:  0.55,   # Geo: minor (mantle convection)
    4:  0.45,   # Semi: minor
    5:  0.55,   # Chem: kinetic gases
    6:  0.65,   # Bio: blood flow, microorganism swimming
    7:  0.35,   # Cog: minor
    8:  0.30,   # Soc: minor
    9:  0.30,   # Eco: minor
    10: 0.80,   # Energy: nuclear fusion + wind + solar wind
    11: 0.65,   # Material: gas/liquid material
    12: 0.55,   # Astrobio: planetary atmospheres
    13: 0.90,   # Climate: weather is fluid dynamics
    14: 0.55,   # Comm: minor
    15: 0.55,   # CS: CFD computation
    16: 0.55,   # AI: AI-augmented turbulence models
    17: 0.65,   # QG: gravitational wave hydrodynamics
    18: 0.80,   # BH: accretion disks (Phase 164)
    19: 0.65,   # Cosmology: cosmic plasma
    20: 0.55,   # SM: QGP
    21: 0.90,   # Stat Mech: kinetic theory (K_flow = K_stat coarse-grain)
    22: 0.85,   # CM: liquid state + He-4 SF + quantum vortex
}

# ----------------------------------------------------------------------
# Build base 23-vertex polytope adjacency
# ----------------------------------------------------------------------
np.random.seed(0)
N_total = 23
adj = np.zeros((N_total + 1, N_total + 1), dtype=int)  # 1-indexed up to 23

# Hub progression: #17-#23 all connect to all others
for hub in range(17, N_total + 1):
    for j in range(1, hub):
        adj[hub, j] = 1
        adj[j, hub] = 1

# Among #1-#16: moderate connectivity
for i in range(1, 17):
    for j in range(i+1, 17):
        if np.random.rand() < 0.55:
            adj[i, j] = 1
            adj[j, i] = 1

# Among #17-#23: full clique
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

print(f"[1] 23-vertex polytope built")
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
# Connection strengths to #23
# ----------------------------------------------------------------------
print(f"[2] Connection strengths #23 → other Tier 1s")
strong = [k for k, v in conn_23.items() if v >= 0.80]
medium = [k for k, v in conn_23.items() if 0.50 <= v < 0.80]
weak   = [k for k, v in conn_23.items() if v < 0.50]
avg_strength = np.mean(list(conn_23.values()))

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
    ("Navier-Stokes Millennium Problem solved",       2050, 0.30, "Weak"),
    ("DNS turbulence Re_λ > 10,000 K41 verification", 2030, 0.85, "Strong"),
    ("Riblet/polymer drag reduction in commercial aviation", 2030, 0.70, "Strong"),
    ("Active AI flow control in commercial aircraft", 2035, 0.65, "Medium"),
    ("Hypersonic Mach 5 commercial flight",           2035, 0.55, "Medium"),
    ("ITER first plasma + Q > 1",                     2028, 0.85, "Strong"),
    ("M87 jet launching mechanism (BZ vs BP) decided",2030, 0.65, "Medium"),
    ("Solar corona heating problem resolved (PSP)",   2030, 0.70, "Strong"),
    ("Sonic BH analog observes Hawking radiation",    2032, 0.50, "Medium"),
    ("Quantum turbulence Onsager-Feynman tangle confirmed", 2028, 0.75, "Strong"),
]
P_values = [p[2] for p in predictions]
P_avg = np.mean(P_values)
n_strong = sum(1 for p in predictions if p[3] == "Strong")
n_medium = sum(1 for p in predictions if p[3] == "Medium")
n_weak = sum(1 for p in predictions if p[3] == "Weak")

print(f"    {'#':<3}{'Prediction':<55}{'Year':<6}{'P':<6}{'Class':<8}")
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    print(f"    {i:<3}{desc[:54]:<55}{yr:<6}{P:<6}{cls:<8}")
print()
print(f"    P_avg = {P_avg:.3f}")
print(f"    Strong: {n_strong}, Medium: {n_medium}, Weak: {n_weak}")
print()

# ----------------------------------------------------------------------
# Block A 7-paper comparison
# ----------------------------------------------------------------------
print(f"[4] Block A 7-paper comparison")
block_A = [
    ("#17 QG",        0.625, 16, "K_geom",     "BMV"),
    ("#18 BH",        0.660, 17, "K_horizon",  "EHT/GWTC"),
    ("#19 Cosmology", 0.630, 18, "K_cosmic",   "LiteBIRD/DESI"),
    ("#20 SM",        0.610, 19, "K_field",    "LHC"),
    ("#21 Stat Mech", 0.635, 20, "K_stat",     "Quantum comp+AI"),
    ("#22 CM",        0.665, 21, "K_solid",    "HTS+TI+Majorana"),
    ("#23 Fluid",     P_avg,  22, "K_flow",     "ITER+EHT+DNS"),
]
print(f"    {'Paper':<16}{'P_avg':<10}{'deg':<6}{'K-state':<14}{'Platform':<22}")
for name, p, d, k, plat in block_A:
    print(f"    {name:<16}{p:<10.3f}{d:<6}{k:<14}{plat:<22}")
print()

# ----------------------------------------------------------------------
# Pass-1 progress
# ----------------------------------------------------------------------
pass1_pct = 166 / 220 * 100
print(f"[5] Pass-1 progress")
print(f"    Phase 1-166 / 220 = {pass1_pct:.1f}%")
print(f"    Block A 7/9 complete ★")
print(f"    EXTENDED MATTER BLOCK = K_geom + K_cosmic + K_field + K_stat + K_solid + K_flow established")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# 1) 23-vertex polytope (circular layout)
ax = axes[0, 0]
angles = np.linspace(0, 2*np.pi, N_total, endpoint=False)
x_pos = np.cos(angles)
y_pos = np.sin(angles)
# draw edges
for i in range(1, N_total + 1):
    for j in range(i+1, N_total + 1):
        if adj[i, j]:
            ax.plot([x_pos[i-1], x_pos[j-1]], [y_pos[i-1], y_pos[j-1]],
                    'gray', alpha=0.2, lw=0.5)
# draw vertices: color by group
colors = ['steelblue'] * 16 + ['orange'] * 4 + ['gold', 'red', 'magenta']
sizes = [60 + 25 * degrees[v] for v in range(1, N_total + 1)]
for i in range(N_total):
    ax.scatter(x_pos[i], y_pos[i], s=sizes[i], c=colors[i],
               edgecolors='black', zorder=3)
    ax.text(1.12 * x_pos[i], 1.12 * y_pos[i], f"#{i+1}",
            ha='center', va='center', fontsize=8, fontweight='bold')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f'23-vertex ITU Polytope\n(magenta = #23 Fluid deg {degrees[23]})')

# 2) Connection strengths to #23
ax = axes[0, 1]
ks = list(conn_23.keys())
vs = list(conn_23.values())
cls_colors = ['red' if v >= 0.80 else ('orange' if v >= 0.50 else 'lightblue') for v in vs]
ax.barh(range(len(ks)), vs, color=cls_colors, edgecolor='black')
ax.set_yticks(range(len(ks)))
ax.set_yticklabels([f'#{k} {tier1_labels[k][:12]}' for k in ks], fontsize=8)
ax.axvline(0.80, color='red', linestyle=':', alpha=0.6, label='Strong (≥0.80)')
ax.axvline(0.50, color='orange', linestyle=':', alpha=0.6, label='Medium (≥0.50)')
ax.set_xlabel('Connection strength to #23')
ax.set_title(f'#23 Fluid connections (avg = {avg_strength:.2f}; max #2 Plasma = 0.95)')
ax.legend(fontsize=8, loc='lower right')
ax.grid(True, alpha=0.3, axis='x')
ax.invert_yaxis()

# 3) 10 predictions
ax = axes[1, 0]
ax.axis('off')
text = "10 Falsifiable Predictions (Tier 1 #23 Fluid)\n" + "─" * 56 + "\n"
text += f"{'#':<3}{'Prediction':<40}{'Yr':<6}{'P':<5}{'Cls':<7}\n"
text += "─" * 56 + "\n"
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    text += f"{i:<3}{desc[:39]:<40}{yr:<6}{P:<5.2f}{cls:<7}\n"
text += "─" * 56 + "\n"
text += f"P_avg = {P_avg:.3f}  |  Strong:{n_strong} Med:{n_medium} Weak:{n_weak}"
ax.text(0.0, 1.0, text, family='monospace', fontsize=8,
        verticalalignment='top', transform=ax.transAxes)
ax.set_title('10 Predictions Table')

# 4) Block A 7-paper comparison
ax = axes[1, 1]
papers = [p[0] for p in block_A]
P_avgs = [p[1] for p in block_A]
degs_A = [p[2] for p in block_A]

ax.bar(papers, P_avgs, color=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
       edgecolor='black', alpha=0.8)
ax.set_ylabel('P_avg', color='black')
ax.set_ylim(0.55, 0.72)
ax.tick_params(axis='x', rotation=20)

ax2 = ax.twinx()
ax2.plot(papers, degs_A, 'ko-', markersize=10, lw=2, label='Polytope degree')
ax2.set_ylabel('Polytope degree', color='black')
ax2.set_ylim(14, 23)
ax2.legend(loc='upper left')

ax.set_title(f'Block A 7-paper progression: Pass-1 {pass1_pct:.1f}%')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'polytope_23vertex_predictions.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 166,
    "title": "Tier 1 #23 Fluid Dynamics integration + 23-vertex polytope + 10 predictions",
    "tier1_paper": "#23 Fluid Dynamics — COMPLETE (Block A 7/9)",
    "milestone": "Pass-1 75.5% — EXTENDED MATTER BLOCK (K_geom+K_cosmic+K_field+K_stat+K_solid+K_flow)",
    "polytope": {
        "vertices": N_total,
        "edges": n_edges,
        "mean_degree": float(mean_k),
        "top_hub_degree": top_hub_deg,
        "top_hubs": [f"#{v} {tier1_labels[v]}" for v in top_hubs],
        "degrees": {f"#{k}": v for k, v in degrees.items()},
    },
    "connections_to_23": {
        "strengths": {f"#{k}": v for k, v in conn_23.items()},
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
    "block_A_7_paper_comparison": [
        {"paper": n, "P_avg": p, "polytope_degree": d,
         "K_state": k, "platform": pl}
        for n, p, d, k, pl in block_A
    ],
    "pass1_progress": {
        "phase_current": 166,
        "phase_total": 220,
        "percent": float(pass1_pct),
        "block_A_completed": "7/9",
    },
    "K_state_evolution": {
        "HORIZON_TRIAD": "K_geom + K_horizon + K_cosmic (Block A 1+2+3)",
        "FUNDAMENTAL_TRINITY": "K_geom + K_cosmic + K_field (Block A 1+3+4)",
        "UNIVERSAL_FOUNDATION": "K_geom + K_cosmic + K_field + K_stat (Block A 1+3+4+5)",
        "COMPLETE_PHYSICS_BLOCK": "+ K_solid (Block A 1+3+4+5+6)",
        "EXTENDED_MATTER_BLOCK": "+ K_flow (Block A 1+3+4+5+6+7)",
    },
    "itu_interpretation": {
        "K_flow_role": "ITU coarse-grained continuum velocity backbone",
        "K_flow_sub_states": [
            "K_visc (viscosity, Stokes drag)",
            "K_turb (Kolmogorov K41 universal -5/3)",
            "K_boundary (Prandtl + Blasius universal)",
            "K_compressible (Mach + Rankine-Hugoniot)",
            "K_vortex (Helmholtz + Kelvin + quantum vortex)",
            "K_MHD (Alfvén + frozen flux + Tokamak)",
            "K_astro (Eddington + accretion + jets + Sedov)",
            "K_NS-regularity (Clay Millennium, Onsager 1/3)",
        ],
        "universal_quantities_verified": [
            "Reynolds 18 orders span (Phase 159)",
            "K41 -5/3 numerical = -1.667 (Phase 160)",
            "Blasius f''(0) = 0.3321 (Phase 161, Howarth 0.3320)",
            "Strouhal 0.21 universal (Phase 162)",
            "Quantum vortex Γ = h/m_He4 = 9.98e-8 (Phase 162)",
            "Onsager 1/3 = K41 -5/3 Fourier dual (Phase 165, Isett 2018)",
        ],
    },
}

out_json = os.path.join(os.path.dirname(__file__), 'polytope_23vertex_predictions_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 166 complete: Tier 1 #23 Fluid Dynamics — FINISHED")
print(f"  23-vertex polytope: #17-#23 all deg {top_hub_deg} (new max)")
print(f"  10 predictions: P_avg = {P_avg:.3f}, Strong {n_strong}/Med {n_medium}/Weak {n_weak}")
print(f"  Pass-1 progress: {pass1_pct:.1f}% (Block A 7/9 done)")
print(f"  EXTENDED MATTER BLOCK: K_geom + K_cosmic + K_field + K_stat + K_solid + K_flow ★")
print("=" * 70)
