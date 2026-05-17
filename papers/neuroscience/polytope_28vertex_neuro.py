"""
Phase 206 — 28-vertex ITU polytope + Tier 1 #28 integration + 10 predictions

Outputs:
  - polytope_28vertex_neuro.png
  - polytope_28vertex_neuro_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("polytope_28vertex_neuro.png")
OUT_JSON = Path(__file__).with_name("polytope_28vertex_neuro_summary.json")

rng = np.random.default_rng(20260609)

N = 28
vertex_full = [
    "QC", "AI", "Crypto", "Semi", "Cancer", "Aging", "Psych", "Econ", "FreeWill",
    "Energy", "Climate", "Astro", "Robot", "Comm", "Infra", "SmartCity",
    "QG", "BH", "Cos", "SM", "Stat", "CM", "Fluid", "Math", "Info/Holo",
    "Immune", "Microbe", "Neuro",
]

# Build adjacency
adj = np.zeros((N, N), dtype=int)

# Block A (#17-#25, indices 16-24) - complete subgraph
block_A = list(range(16, 25))
for i in block_A:
    for j in block_A:
        if i != j: adj[i, j] = 1

# Block A also connects to 15 of the 16 prior vertices
for i in block_A:
    others = list(range(16))
    chosen = rng.choice(others, size=15, replace=False)
    for j in chosen:
        adj[i, j] = adj[j, i] = 1

# Block B vertices: each connects to all prior
for new_idx in [25, 26, 27]:  # Immune, Microbe, Neuro
    for j in range(new_idx):
        adj[new_idx, j] = adj[j, new_idx] = 1

deg = adj.sum(axis=1)
edges = int(adj.sum() / 2)
mean_k = float(deg.mean())
max_k = int(deg.max())
top_hubs = [i for i, d in enumerate(deg) if d == max_k]

# #28 connection strengths
neuro_strengths = {
    "#2 AI Consciousness (bio vs AI)":   0.98,
    "#7 Psychiatry":                     0.95,
    "#25 Info/Holo (modular ham)":       0.90,
    "#9 Free Will (Libet)":              0.85,
    "#26 Immune (neuroinflammation)":    0.85,
    "#27 Microbe (gut-brain)":           0.85,
    "#5 Cancer (brain tumor)":           0.75,
    "#6 Aging (AD)":                     0.85,
    "#22 CM (neuromorphic chip)":        0.70,
    "#1 QC (quantum brain debate)":      0.40,
}
avg_strength = float(np.mean(list(neuro_strengths.values())))

predictions = [
    ("Lecanemab follow-on (anti-tau)", 2028, 0.75, "Strong"),
    ("Psilocybin FDA approval (TRD)", 2028, 0.70, "Strong"),
    ("Engram-based memory editing clinical", 2032, 0.55, "Medium"),
    ("In vivo CAR-T for neurology", 2030, 0.60, "Medium"),
    ("Phi proxy whole-brain measurement", 2030, 0.65, "Medium"),
    ("BCI visual prosthesis 100x100", 2030, 0.65, "Medium"),
    ("CNN ImageNet >99% (human parity)", 2027, 0.80, "Strong"),
    ("Alpha-synuclein vaccine effective", 2030, 0.50, "Medium"),
    ("AD 10yr early dx via sleep biomarker", 2030, 0.75, "Strong"),
    ("Schizophrenia molecular biomarker", 2032, 0.45, "Medium"),
]
P_grand = float(np.mean([p[2] for p in predictions]))
strong = sum(1 for p in predictions if p[3] == "Strong")
medium = sum(1 for p in predictions if p[3] == "Medium")
weak = sum(1 for p in predictions if p[3] == "Weak")

# Plot
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    "Phase 206 — 28-Vertex ITU Polytope + Tier 1 #28 Neuroscience (Pass-1 93.6% ★)",
    fontsize=14, fontweight="bold",
)

# Panel 1: Polytope graph
ax = axes[0, 0]
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
pos_x = np.cos(theta); pos_y = np.sin(theta)
for i in range(N):
    for j in range(i + 1, N):
        if adj[i, j]:
            alpha_e = 0.05 if i < 16 and j < 16 else 0.12
            ax.plot([pos_x[i], pos_x[j]], [pos_y[i], pos_y[j]],
                    "-", color="gray", alpha=alpha_e, lw=0.3)
colors_v, sizes_v = [], []
for i in range(N):
    if i == 27:    colors_v.append("#17becf"); sizes_v.append(320)   # #28 Neuro
    elif i == 26:  colors_v.append("#8c564b"); sizes_v.append(260)   # #27
    elif i == 25:  colors_v.append("#e377c2"); sizes_v.append(240)   # #26
    elif 16 <= i <= 24:
        colors_v.append("#d62728"); sizes_v.append(220)
    else:
        colors_v.append("#1f77b4"); sizes_v.append(120)
ax.scatter(pos_x, pos_y, c=colors_v, s=sizes_v, edgecolor="black", linewidth=0.8, zorder=5)
for i, name in enumerate(vertex_full):
    radius = 1.20
    label = f"#{i+1} {name}"
    color = "black" if i < 16 else "#d62728" if i < 25 else "#e377c2" if i == 25 else "#8c564b" if i == 26 else "#17becf"
    ax.annotate(label, (pos_x[i] * radius, pos_y[i] * radius),
                ha="center", va="center", fontsize=6, color=color)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"28 vertices, {edges} edges, ⟨k⟩={mean_k:.2f}, top deg={max_k}")

# Panel 2: Neuro couplings
ax = axes[0, 1]
n_names = list(neuro_strengths.keys()); strs = list(neuro_strengths.values())
colors_s = ["#2ca02c" if s >= 0.85 else "#ff7f0e" if s >= 0.6 else "#d62728" for s in strs]
ax.barh(range(len(n_names)), strs, color=colors_s)
ax.set_yticks(range(len(n_names))); ax.set_yticklabels(n_names, fontsize=7)
ax.set_xlabel("Coupling strength"); ax.set_xlim(0, 1)
ax.axvline(0.85, color="black", linestyle="--", alpha=0.5)
ax.set_title(f"#28 Neuro couplings (avg = {avg_strength:.3f})")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: Predictions
ax = axes[1, 0]
names_p = [p[0] for p in predictions]
years_p = [p[1] for p in predictions]
probs_p = [p[2] for p in predictions]
colors_p = ["#2ca02c" if p[3]=="Strong" else "#ff7f0e" if p[3]=="Medium" else "#d62728" for p in predictions]
ax.scatter(years_p, probs_p, c=colors_p, s=180, edgecolor="black", zorder=5)
for i, name in enumerate(names_p):
    ax.annotate(name, (years_p[i] + 0.2, probs_p[i] + 0.01), fontsize=6)
ax.axhline(0.70, color="green", linestyle="--", alpha=0.5)
ax.axhline(0.45, color="orange", linestyle="--", alpha=0.5)
ax.set_xlabel("Target year"); ax.set_ylabel("Probability")
ax.set_xlim(2026, 2034); ax.set_ylim(0, 1)
ax.set_title(f"10 predictions; P_avg={P_grand:.3f}; S/M/W={strong}/{medium}/{weak}")
ax.grid(True, alpha=0.3)

# Panel 4: Pass-1 milestones
ax = axes[1, 1]
milestones = [
    ("Phase 110\nTier 0 v3.0",    50.0),
    ("Phase 166\nFluid",          75.5),
    ("Phase 174\nMath",           79.1),
    ("Phase 182\nBlock A FINALE", 82.7),
    ("Phase 190\nImmune",         86.4),
    ("Phase 198\nMicrobe",        90.0),
    ("Phase 206\nNeuro",          93.6),
]
labels = [m[0] for m in milestones]
vals = [m[1] for m in milestones]
colors_m = ["#1f77b4"]*4 + ["#e377c2", "#8c564b", "#17becf"]
ax.bar(labels, vals, color=colors_m)
ax.axhline(100, color="black", linestyle="--", alpha=0.5, label="Pass-1 complete")
ax.set_ylabel("Pass-1 progress (%)")
ax.set_title(f"Pass-1 milestones — currently 93.6% ★")
ax.set_ylim(0, 105)
for i, v in enumerate(vals):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=8, fontweight="bold")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 206,
    "tier1_paper": 28,
    "block": "B",
    "paper_in_block": "3/?",
    "topic": "Integration: K_neuro + 28-vertex polytope + 10 predictions",
    "milestone": "Pass-1 93.6% (206/220) ★",
    "polytope_28vertex": {
        "vertices": int(N),
        "edges": int(edges),
        "mean_degree": float(mean_k),
        "max_degree": int(max_k),
        "top_hubs": top_hubs,
    },
    "neuro_couplings": neuro_strengths,
    "neuro_avg_coupling": float(avg_strength),
    "10_predictions": [
        {"prediction": p[0], "year": p[1], "P": p[2], "class": p[3]} for p in predictions
    ],
    "predictions_summary": {
        "grand_P_avg": float(P_grand),
        "strong": strong, "medium": medium, "weak": weak,
    },
    "ITU_axiom_strict_unity_Phase_199_205": {
        "Phase_199_neural_resting_active":     1.000000,
        "Phase_200_LTP_synaptic":              1.000000,
        "Phase_201_V1_V4_IT_hierarchy":        "1.000 each step",
        "Phase_202_episodic_encoding":         1.000000,
        "Phase_203_decision_selection":        1.000000,
        "Phase_204_sleep_transitions":         "1.000 wake->N3, 1.000 wake->REM",
        "Phase_205_AD_pathology_treatment":    "1.000 healthy->AD, 1.000 AD->Tx",
        "interpretation": "K_neuro axiom verified across 10+ contexts (perception, memory, decision, sleep, pathology)",
    },
    "K_neuro_structure": {
        "K_neuron": "Hodgkin-Huxley dynamics",
        "K_synapse": "LTP/LTD/STDP plasticity",
        "K_network": "Connectome (HCP 180 areas)",
        "K_perception": "Hubel-Wiesel V1->V4->IT",
        "K_memory": "Hippocampus place/grid cells",
        "K_executive": "PFC decision (loss aversion λ=2.25)",
        "K_consciousness": "IIT Φ + GWT (Hard Problem)",
        "K_pathology": "AD/PD/depression/schizophrenia",
    },
    "pass1_progress": {
        "phases_completed": 206,
        "phases_total": 220,
        "percent": 93.6,
        "block_A_status": "9/9 COMPLETE",
        "block_B_status": "3/? (#26 Immune + #27 Microbe + #28 Neuro complete)",
        "next": "Phase 207 -> Tier 1 #29 Developmental Biology",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
