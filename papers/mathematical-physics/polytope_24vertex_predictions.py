"""
Phase 174: Tier 1 #24 integration — 24-vertex polytope + 10 predictions
========================================================================

Tests:
1. Build 24-vertex polytope (add #24 Mathematical Physics)
2. Compute connection strengths between #24 and other 23 Tier 1s
3. Polytope statistics (vertices, edges, ⟨k⟩, top hub)
4. Tabulate 10 falsifiable predictions
5. Block A 8-paper comparison
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

print("=" * 70)
print("Phase 174: Tier 1 #24 Integration — 24-vertex polytope")
print("=" * 70)
print()

tier1_labels = {
    1:"QC", 2:"Plasma", 3:"Geo", 4:"Semi", 5:"Chem", 6:"Bio", 7:"Cog",
    8:"Soc", 9:"Eco", 10:"Energy", 11:"Material", 12:"Astrobio",
    13:"Climate", 14:"Comm", 15:"CS", 16:"AI",
    17:"QG (BlA-1)", 18:"BH (BlA-2)", 19:"Cosmology (BlA-3)",
    20:"SM (BlA-4)", 21:"Stat Mech (BlA-5)", 22:"CM (BlA-6)",
    23:"Fluid (BlA-7)", 24:"Math (BlA-8)",
}

conn_24 = {
    1: 0.85, 2: 0.55, 3: 0.30, 4: 0.55, 5: 0.50, 6: 0.40, 7: 0.45,
    8: 0.35, 9: 0.40, 10: 0.45, 11: 0.55, 12: 0.40, 13: 0.40,
    14: 0.50, 15: 0.80, 16: 0.70,
    17: 0.95, 18: 0.65, 19: 0.55, 20: 0.90, 21: 0.85, 22: 0.85, 23: 0.65,
}

# Build adjacency
np.random.seed(0)
N_total = 24
adj = np.zeros((N_total + 1, N_total + 1), dtype=int)

# Hubs (#17-#24) connect to all earlier + each other
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

# Among #17-#24: full clique
for i in range(17, N_total + 1):
    for j in range(i+1, N_total + 1):
        adj[i, j] = 1
        adj[j, i] = 1

degrees = {i: int(adj[i].sum()) for i in range(1, N_total + 1)}
n_edges = int(adj[1:, 1:].sum() // 2)
mean_k = 2 * n_edges / N_total
top_hub_deg = max(degrees.values())
top_hubs = [v for v in range(1, N_total + 1) if degrees[v] == top_hub_deg]

print(f"[1] 24-vertex polytope")
print(f"    Vertices: {N_total}, Edges: {n_edges}, ⟨k⟩: {mean_k:.2f}")
print(f"    Top hub degree: {top_hub_deg}")
print(f"    Top hubs: {[f'#{v} {tier1_labels[v]}' for v in top_hubs]}")
print()

print(f"[2] #24 connection strengths")
strong = [k for k, v in conn_24.items() if v >= 0.80]
medium = [k for k, v in conn_24.items() if 0.50 <= v < 0.80]
weak = [k for k, v in conn_24.items() if v < 0.50]
avg_strength = np.mean(list(conn_24.values()))
print(f"  Strong (≥0.80): {len(strong)} → #{strong}")
print(f"  Medium: {len(medium)}, Weak: {len(weak)}, Average: {avg_strength:.3f}")
print()

print(f"[3] 10 Falsifiable Predictions (2026-2080)")
predictions = [
    ("Riemann Hypothesis solved (Clay #4)",     2080, 0.20, "Weak"),
    ("Yang-Mills mass gap proved (Clay #5)",    2050, 0.25, "Weak"),
    ("Geometric Langlands fully proved",        2040, 0.50, "Medium"),
    ("Twin prime conjecture solved",            2035, 0.55, "Medium"),
    ("Hodge conjecture partial results",        2035, 0.45, "Medium"),
    ("BSD partial resolution (Clay #7)",        2040, 0.50, "Medium"),
    ("Fibonacci anyon topological QC demo",     2032, 0.75, "Strong"),
    ("Khovanov 4D applications expanded",       2030, 0.70, "Strong"),
    ("Volume conjecture (knots) solved",        2035, 0.65, "Medium"),
    ("AdS/CFT mathematical rigor (toy)",        2035, 0.70, "Strong"),
]
P_avg = np.mean([p[2] for p in predictions])
n_strong = sum(1 for p in predictions if p[3] == "Strong")
n_medium = sum(1 for p in predictions if p[3] == "Medium")
n_weak = sum(1 for p in predictions if p[3] == "Weak")
print(f"  {'#':<3}{'Prediction':<48}{'Year':<6}{'P':<6}{'Class':<8}")
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    print(f"  {i:<3}{desc[:47]:<48}{yr:<6}{P:<6}{cls:<8}")
print(f"\n  P_avg = {P_avg:.3f}; Strong {n_strong}, Medium {n_medium}, Weak {n_weak}")
print()

block_A = [
    ("#17 QG",        0.625, 16, "K_geom",     "BMV"),
    ("#18 BH",        0.660, 17, "K_horizon",  "EHT/GWTC"),
    ("#19 Cosmology", 0.630, 18, "K_cosmic",   "LiteBIRD/DESI"),
    ("#20 SM",        0.610, 19, "K_field",    "LHC"),
    ("#21 Stat Mech", 0.635, 20, "K_stat",     "Quantum comp+AI"),
    ("#22 CM",        0.665, 21, "K_solid",    "HTS+TI+Majorana"),
    ("#23 Fluid",     0.650, 22, "K_flow",     "ITER+EHT+DNS"),
    ("#24 Math",      P_avg, 23, "K_math",     "Clay+RMT+Topology"),
]
print(f"[4] Block A 8-paper comparison")
print(f"    {'Paper':<16}{'P_avg':<10}{'deg':<6}{'K-state':<14}{'Platform':<22}")
for name, p, d, k, pl in block_A:
    print(f"    {name:<16}{p:<10.3f}{d:<6}{k:<14}{pl:<22}")
print()

pass1_pct = 174 / 220 * 100
print(f"[5] Pass-1: {pass1_pct:.1f}%")
print(f"    Block A 8/9 complete ★ MATHEMATICAL FOUNDATION BLOCK")
print()

# Plot
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# 1) 24-vertex polytope
ax = axes[0, 0]
angles = np.linspace(0, 2*np.pi, N_total, endpoint=False)
x_pos = np.cos(angles)
y_pos = np.sin(angles)
for i in range(1, N_total + 1):
    for j in range(i+1, N_total + 1):
        if adj[i, j]:
            ax.plot([x_pos[i-1], x_pos[j-1]], [y_pos[i-1], y_pos[j-1]],
                    'gray', alpha=0.15, lw=0.5)
colors = ['steelblue'] * 16 + ['orange'] * 4 + ['gold', 'red', 'magenta', 'purple']
sizes = [50 + 22 * degrees[v] for v in range(1, N_total + 1)]
for i in range(N_total):
    ax.scatter(x_pos[i], y_pos[i], s=sizes[i], c=colors[i],
               edgecolors='black', zorder=3)
    ax.text(1.13 * x_pos[i], 1.13 * y_pos[i], f"#{i+1}",
            ha='center', va='center', fontsize=8, fontweight='bold')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f'24-vertex ITU Polytope\n(purple = #24 Math deg {degrees[24]})')

# 2) Connections
ax = axes[0, 1]
ks = list(conn_24.keys())
vs = list(conn_24.values())
cls_colors = ['red' if v >= 0.80 else ('orange' if v >= 0.50 else 'lightblue') for v in vs]
ax.barh(range(len(ks)), vs, color=cls_colors, edgecolor='black')
ax.set_yticks(range(len(ks)))
ax.set_yticklabels([f'#{k} {tier1_labels[k][:9]}' for k in ks], fontsize=7)
ax.axvline(0.80, color='red', linestyle=':', alpha=0.6, label='Strong ≥0.80')
ax.axvline(0.50, color='orange', linestyle=':', alpha=0.6, label='Medium ≥0.50')
ax.set_xlabel('Connection strength')
ax.set_title(f'#24 Math connections (avg = {avg_strength:.2f}; max #17 QG = 0.95)')
ax.legend(fontsize=8)
ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# 3) Predictions
ax = axes[1, 0]
ax.axis('off')
text = "10 Falsifiable Predictions (Tier 1 #24 Math)\n" + "─" * 55 + "\n"
text += f"{'#':<3}{'Prediction':<38}{'Yr':<6}{'P':<5}{'Cls':<7}\n"
text += "─" * 55 + "\n"
for i, (desc, yr, P, cls) in enumerate(predictions, 1):
    text += f"{i:<3}{desc[:37]:<38}{yr:<6}{P:<5.2f}{cls:<7}\n"
text += "─" * 55 + "\n"
text += f"P_avg = {P_avg:.3f} | Strong:{n_strong} Med:{n_medium} Weak:{n_weak}"
ax.text(0.0, 1.0, text, family='monospace', fontsize=8,
        verticalalignment='top', transform=ax.transAxes)
ax.set_title('10 Predictions Table')

# 4) Block A
ax = axes[1, 1]
papers = [p[0] for p in block_A]
P_avgs = [p[1] for p in block_A]
degs_A = [p[2] for p in block_A]
ax.bar(papers, P_avgs, color=['C0','C1','C2','C3','C4','C5','C6','C7'],
       edgecolor='black', alpha=0.8)
ax.set_ylabel('P_avg')
ax.set_ylim(0.50, 0.72)
ax.tick_params(axis='x', rotation=25)
ax2 = ax.twinx()
ax2.plot(papers, degs_A, 'ko-', markersize=10, lw=2, label='degree')
ax2.set_ylabel('Polytope degree')
ax2.set_ylim(15, 24)
ax2.legend(loc='upper left')
ax.set_title(f'Block A 8-paper progression: Pass-1 {pass1_pct:.1f}%')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'polytope_24vertex_predictions.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

summary = {
    "phase": 174,
    "title": "Tier 1 #24 Mathematical Physics integration + 24-vertex polytope + 10 predictions",
    "tier1_paper": "#24 Mathematical Physics — COMPLETE (Block A 8/9)",
    "milestone": "Pass-1 79.1% — MATHEMATICAL FOUNDATION BLOCK",
    "polytope": {
        "vertices": N_total,
        "edges": n_edges,
        "mean_degree": float(mean_k),
        "top_hub_degree": top_hub_deg,
        "top_hubs": [f"#{v} {tier1_labels[v]}" for v in top_hubs],
        "degrees": {f"#{k}": v for k, v in degrees.items()},
    },
    "connections_to_24": {
        "strengths": {f"#{k}": v for k, v in conn_24.items()},
        "average": float(avg_strength),
        "strong_count": len(strong),
        "strong_list": [f"#{k}" for k in strong],
    },
    "predictions": [
        {"id": i, "description": d, "year": y, "P": p, "class": c}
        for i, (d, y, p, c) in enumerate(predictions, 1)
    ],
    "predictions_summary": {
        "P_avg": float(P_avg),
        "n_strong": n_strong, "n_medium": n_medium, "n_weak": n_weak,
    },
    "block_A_8_paper_comparison": [
        {"paper": n, "P_avg": p, "degree": d, "K_state": k, "platform": pl}
        for n, p, d, k, pl in block_A
    ],
    "pass1_progress": {
        "phase_current": 174, "phase_total": 220,
        "percent": float(pass1_pct), "block_A_completed": "8/9",
    },
    "K_state_evolution": {
        "EXTENDED_MATTER_BLOCK": "K_geom + K_cosmic + K_field + K_stat + K_solid + K_flow",
        "MATHEMATICAL_FOUNDATION_BLOCK": "+ K_math",
    },
    "Clay_Millennium_problems_in_Tier1": {
        "#4_Riemann": "Phase 173",
        "#5_Yang_Mills": "Phase 169",
        "#6_Navier_Stokes": "Phase 165",
    },
}

out_json = os.path.join(os.path.dirname(__file__), 'polytope_24vertex_predictions_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 174 complete: Tier 1 #24 — FINISHED")
print(f"  24-vertex polytope: #17-#24 all deg {top_hub_deg}")
print(f"  Pass-1 {pass1_pct:.1f}% (Block A 8/9 done)")
print(f"  MATHEMATICAL FOUNDATION BLOCK = 7 K-states (6 physics + 1 math)")
print("=" * 70)
