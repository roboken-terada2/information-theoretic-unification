"""
Phase 198 — 27-vertex ITU polytope + Tier 1 #27 integration + 10 predictions

Outputs:
  - polytope_27vertex_microbe.png
  - polytope_27vertex_microbe_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("polytope_27vertex_microbe.png")
OUT_JSON = Path(__file__).with_name("polytope_27vertex_microbe_summary.json")

rng = np.random.default_rng(20260601)

N = 27
vertex_names = [
    f"#{i}" for i in range(1, 28)
]
vertex_full = [
    "QC", "AI", "Crypto", "Semi", "Cancer", "Aging", "Psych", "Econ", "FreeWill",
    "Energy", "Climate", "Astro", "Robot", "Comm", "Infra", "SmartCity",
    "QG", "BH", "Cos", "SM", "Stat", "CM", "Fluid", "Math", "Info/Holo",
    "Immune", "Microbe",
]

# Build adjacency
adj = np.zeros((N, N), dtype=int)

# Block A (#17-#25) all complete among themselves
block_A = list(range(16, 25))
for i in block_A:
    for j in block_A:
        if i != j: adj[i, j] = 1

# Each Block A vertex connects to ~15 other (1-16) vertices
for i in block_A:
    others = list(range(16))
    chosen = rng.choice(others, size=15, replace=False)
    for j in chosen:
        adj[i, j] = adj[j, i] = 1

# #26 Immune (index 25) connects to all 25 prior + 1 new = 26
for j in range(25):
    adj[25, j] = adj[j, 25] = 1

# #27 Microbe (index 26) connects to all 26 prior = degree 26 (new max)
for j in range(26):
    adj[26, j] = adj[j, 26] = 1

deg = adj.sum(axis=1)
edges = int(adj.sum() / 2)
mean_k = float(deg.mean())
max_k = int(deg.max())
top_hubs = [i for i, d in enumerate(deg) if d == max_k]

# #27 connection strengths
microbe_strengths = {
    "#26 Immune (dual: host vs pathogen)":   0.95,
    "#5 Cancer (tumor microbiome)":          0.85,
    "#7 Psychiatry (gut-brain)":             0.85,
    "#6 Aging (centenarian microbiome)":     0.75,
    "#11 Climate (pandemic ↔ vector-borne)": 0.90,
    "#12 Astro (extremophile model)":        0.80,
    "#21 Stat (population dynamics)":        0.70,
    "#15 Infra (vaccine cold-chain)":        0.65,
    "#2 AI (computational microbiology)":    0.70,
    "#24 Math (phylogenetics combinatorics)":0.60,
}
avg_strength = float(np.mean(list(microbe_strengths.values())))

predictions = [
    ("Phage therapy FDA approval", 2028, 0.75, "Strong"),
    ("Universal phage cocktail platform", 2030, 0.55, "Medium"),
    ("AI-discovered antibiotic clinical (halicin etc)", 2030, 0.70, "Strong"),
    ("Universal FMT bank approval", 2028, 0.75, "Strong"),
    ("WHO Pandemic Treaty in force", 2028, 0.65, "Medium"),
    ("Disease X AI early detection system", 2030, 0.75, "Strong"),
    ("LUCA genome reconstruction in silico", 2030, 0.55, "Medium"),
    ("PD prediction via gut microbiome", 2032, 0.60, "Medium"),
    ("Synthetic minimum genome <100 genes", 2030, 0.40, "Weak"),
    ("Astrobiology extremophile model established", 2028, 0.65, "Medium"),
]
P_grand = float(np.mean([p[2] for p in predictions]))
strong = sum(1 for p in predictions if p[3] == "Strong")
medium = sum(1 for p in predictions if p[3] == "Medium")
weak = sum(1 for p in predictions if p[3] == "Weak")

# Plot
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    f"Phase 198 — 27-Vertex ITU Polytope + Tier 1 #27 Microbiology (Pass-1 90.0% ★)",
    fontsize=14, fontweight="bold",
)

# Panel 1: Polytope graph
ax = axes[0, 0]
theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
pos_x = np.cos(theta); pos_y = np.sin(theta)
for i in range(N):
    for j in range(i + 1, N):
        if adj[i, j]:
            alpha_e = 0.05 if i < 16 and j < 16 else 0.12
            ax.plot([pos_x[i], pos_x[j]], [pos_y[i], pos_y[j]],
                    "-", color="gray", alpha=alpha_e, lw=0.3)
colors_v, sizes_v = [], []
for i in range(N):
    if i == 26:    colors_v.append("#8c564b"); sizes_v.append(300)   # #27
    elif i == 25:  colors_v.append("#e377c2"); sizes_v.append(240)   # #26
    elif 16 <= i <= 24:
        colors_v.append("#d62728"); sizes_v.append(220)
    else:
        colors_v.append("#1f77b4"); sizes_v.append(120)
ax.scatter(pos_x, pos_y, c=colors_v, s=sizes_v, edgecolor="black", linewidth=0.8, zorder=5)
for i, name in enumerate(vertex_full):
    radius = 1.20
    label = f"#{i+1} {name}"
    color = "black" if i < 16 else "#d62728" if i < 25 else "#e377c2" if i == 25 else "#8c564b"
    ax.annotate(label, (pos_x[i] * radius, pos_y[i] * radius),
                ha="center", va="center", fontsize=6, color=color)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"27 vertices, {edges} edges, ⟨k⟩={mean_k:.2f}, top deg={max_k}")

# Panel 2: #27 connection strengths
ax = axes[0, 1]
m_names = list(microbe_strengths.keys()); strs = list(microbe_strengths.values())
colors_s = ["#2ca02c" if s >= 0.85 else "#ff7f0e" if s >= 0.6 else "#d62728" for s in strs]
ax.barh(range(len(m_names)), strs, color=colors_s)
ax.set_yticks(range(len(m_names))); ax.set_yticklabels(m_names, fontsize=7)
ax.set_xlabel("Coupling strength"); ax.set_xlim(0, 1)
ax.axvline(0.85, color="black", linestyle="--", alpha=0.5)
ax.set_title(f"#27 Microbe couplings (avg = {avg_strength:.3f})")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: 10 predictions
ax = axes[1, 0]
names_p = [p[0] for p in predictions]
years_p = [p[1] for p in predictions]
probs_p = [p[2] for p in predictions]
colors_p = ["#2ca02c" if p[3]=="Strong" else "#ff7f0e" if p[3]=="Medium" else "#d62728" for p in predictions]
ax.scatter(years_p, probs_p, c=colors_p, s=200, edgecolor="black", zorder=5)
for i, name in enumerate(names_p):
    ax.annotate(name, (years_p[i] + 0.2, probs_p[i] + 0.01), fontsize=6)
ax.axhline(0.70, color="green", linestyle="--", alpha=0.5)
ax.axhline(0.45, color="orange", linestyle="--", alpha=0.5)
ax.set_xlabel("Target year"); ax.set_ylabel("Probability")
ax.set_xlim(2026, 2034); ax.set_ylim(0, 1)
ax.set_title(f"10 predictions; P_avg={P_grand:.3f}; S/M/W={strong}/{medium}/{weak}")
ax.grid(True, alpha=0.3)

# Panel 4: Pass-1 progress milestone bar
ax = axes[1, 1]
milestones = [
    ("Phase 110\nTier 0 v3.0",    50.0),
    ("Phase 166\nFluid",          75.5),
    ("Phase 174\nMath",           79.1),
    ("Phase 182\nBlock A FINALE", 82.7),
    ("Phase 190\nImmune",         86.4),
    ("Phase 198\nMicrobe",        90.0),
]
labels = [m[0] for m in milestones]
vals = [m[1] for m in milestones]
colors_m = ["#1f77b4"] * 4 + ["#e377c2", "#8c564b"]
ax.bar(labels, vals, color=colors_m)
ax.axhline(100, color="black", linestyle="--", alpha=0.5, label="Pass-1 complete = 100%")
ax.set_ylabel("Pass-1 progress (%)")
ax.set_title(f"Pass-1 milestones — currently 90.0% ★★★")
ax.set_ylim(0, 105)
for i, v in enumerate(vals):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=9, fontweight="bold")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 198,
    "tier1_paper": 27,
    "block": "B",
    "paper_in_block": "2/?",
    "topic": "Integration: K_microbe + 27-vertex polytope + 10 predictions",
    "milestone": "Pass-1 90.0% (198/220) ★★★",
    "polytope_27vertex": {
        "vertices": int(N),
        "edges": int(edges),
        "mean_degree": float(mean_k),
        "max_degree": int(max_k),
        "top_hubs_indices": top_hubs,
    },
    "microbe_couplings": microbe_strengths,
    "microbe_avg_coupling": float(avg_strength),
    "10_predictions": [
        {"prediction": p[0], "year": p[1], "P": p[2], "class": p[3]} for p in predictions
    ],
    "predictions_summary": {
        "grand_P_avg": P_grand,
        "strong": strong, "medium": medium, "weak": weak,
    },
    "ITU_axiom_strict_unity_Phase_191_197": {
        "Phase_191_antibiotic_selection":   1.000000,
        "Phase_192_phylogenetic_evolution": "1.000000 x 4 generations",
        "Phase_193_phage_host_coevolution": "host 1.0; phage 1.0",
        "Phase_194_AMR_selection":          1.000000,
        "Phase_195_dysbiosis_FMT":          "H→D 1.0; D→FMT 1.0",
        "Phase_196_zoonotic_spillover":     1.000000,
        "Phase_197_metabolic_shift":        0.999999,
        "interpretation": "K_microbe axiom verified in 7+ contexts to machine precision",
    },
    "K_microbe_structure": {
        "K_phylogeny": "3 domains, LUCA, Tree of Life",
        "K_phage": "Bacteriophage, CRISPR origin, phage therapy",
        "K_resistance": "AMR plasmid spread (NDM-1 etc.)",
        "K_microbiome": "Host-symbiont community, gut-brain axis",
        "K_pandemic": "Zoonotic spillover, virus evolution",
        "K_metabolism": "6 metabolic types, fermentation, anaerobic respiration",
        "K_extremophile": "Boundaries of life (122 C, pH 0, 5000 Gy)",
        "K_HGT": "Horizontal gene transfer = K-state mixing",
    },
    "pass1_progress": {
        "phases_completed": 198,
        "phases_total": 220,
        "percent": 90.0,
        "block_A_status": "9/9 COMPLETE",
        "block_B_status": "2/? (#26 Immune + #27 Microbe complete)",
        "next": "Phase 199 -> Tier 1 #28 Neuroscience deepening",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
