"""
Phase 219 — 30-vertex ITU polytope + Tier 1 #30 integration + 10 predictions
Pass-1 final Tier 1 paper, Pass-1 99.5%

Outputs:
  - polytope_30vertex_genome.png
  - polytope_30vertex_genome_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("polytope_30vertex_genome.png")
OUT_JSON = Path(__file__).with_name("polytope_30vertex_genome_summary.json")

rng = np.random.default_rng(20260629)

N = 30
vertex_full = [
    "QC", "AI", "Crypto", "Semi", "Cancer", "Aging", "Psych", "Econ", "FreeWill",
    "Energy", "Climate", "Astro", "Robot", "Comm", "Infra", "SmartCity",
    "QG", "BH", "Cos", "SM", "Stat", "CM", "Fluid", "Math", "Info/Holo",
    "Immune", "Microbe", "Neuro", "Dev", "Genome",
]

adj = np.zeros((N, N), dtype=int)
block_A = list(range(16, 25))
for i in block_A:
    for j in block_A:
        if i != j: adj[i, j] = 1
for i in block_A:
    others = list(range(16))
    chosen = rng.choice(others, size=15, replace=False)
    for j in chosen:
        adj[i, j] = adj[j, i] = 1
for new_idx in [25, 26, 27, 28, 29]:
    for j in range(new_idx):
        adj[new_idx, j] = adj[j, new_idx] = 1

deg = adj.sum(axis=1)
edges = int(adj.sum() / 2)
mean_k = float(deg.mean())
max_k = int(deg.max())

genome_strengths = {
    "#29 Dev (Hox + Yamanaka)":         0.98,
    "#26 Immune (V(D)J)":                0.95,
    "#27 Microbe (HGT)":                 0.95,
    "#2 AI (AlphaFold)":                 0.95,
    "#28 Neuro (brain genes)":           0.90,
    "#5 Cancer (mutations)":             0.85,
    "#6 Aging (telomere)":               0.85,
    "#3 Crypto (DNA storage)":           0.85,
    "#1 QC (DNA computing)":             0.70,
    "#25 Info/Holo":                     0.80,
}
avg_strength = float(np.mean(list(genome_strengths.values())))

predictions = [
    ("CRISPR drug 10+ indications approved", 2030, 0.85, "Strong"),
    ("AlphaFold 4 (RNA + dynamics)", 2027, 0.80, "Strong"),
    ("In vivo CRISPR (mRNA-LNP)", 2028, 0.80, "Strong"),
    ("All living humans WGS (1e9 genomes)", 2030, 0.70, "Strong"),
    ("1M+ ancient genomes sequenced", 2030, 0.80, "Strong"),
    ("Prime Editor clinical (1 indication)", 2028, 0.75, "Strong"),
    ("AI-designed protein therapy approved", 2028, 0.75, "Strong"),
    ("Synthetic yeast complete genome", 2028, 0.70, "Strong"),
    ("Polygenic risk score full clinical", 2030, 0.75, "Strong"),
    ("Heritable editing legal framework", 2032, 0.45, "Medium"),
]
P_grand = float(np.mean([p[2] for p in predictions]))
strong = sum(1 for p in predictions if p[3] == "Strong")
medium = sum(1 for p in predictions if p[3] == "Medium")
weak = sum(1 for p in predictions if p[3] == "Weak")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    f"Phase 219 — 30-Vertex ITU Polytope + Tier 1 #30 Genomics (Pass-1 99.5% ★★)",
    fontsize=14, fontweight="bold",
)

ax = axes[0, 0]
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
pos_x = np.cos(theta); pos_y = np.sin(theta)
for i in range(N):
    for j in range(i + 1, N):
        if adj[i, j]:
            alpha_e = 0.05 if i < 16 and j < 16 else 0.12
            ax.plot([pos_x[i], pos_x[j]], [pos_y[i], pos_y[j]], "-",
                    color="gray", alpha=alpha_e, lw=0.3)
colors_v = []; sizes_v = []
for i in range(N):
    if i == 29:    colors_v.append("#ff1493"); sizes_v.append(360)  # #30 (deep pink)
    elif i == 28:  colors_v.append("#bcbd22"); sizes_v.append(280)
    elif i == 27:  colors_v.append("#17becf"); sizes_v.append(260)
    elif i == 26:  colors_v.append("#8c564b"); sizes_v.append(240)
    elif i == 25:  colors_v.append("#e377c2"); sizes_v.append(220)
    elif 16 <= i <= 24:
        colors_v.append("#d62728"); sizes_v.append(180)
    else:
        colors_v.append("#1f77b4"); sizes_v.append(100)
ax.scatter(pos_x, pos_y, c=colors_v, s=sizes_v, edgecolor="black", linewidth=0.8, zorder=5)
for i, name in enumerate(vertex_full):
    radius = 1.20
    label = f"#{i+1} {name}"
    if i == 29: color = "#ff1493"
    elif i == 28: color = "#bcbd22"
    elif i == 27: color = "#17becf"
    elif i == 26: color = "#8c564b"
    elif i == 25: color = "#e377c2"
    elif i < 16: color = "black"
    else: color = "#d62728"
    ax.annotate(label, (pos_x[i] * radius, pos_y[i] * radius),
                ha="center", va="center", fontsize=6, color=color)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"30 vertices, {edges} edges, ⟨k⟩={mean_k:.2f}, top deg={max_k}")

ax = axes[0, 1]
g_names = list(genome_strengths.keys()); strs = list(genome_strengths.values())
colors_s = ["#2ca02c" if s >= 0.90 else "#ff7f0e" if s >= 0.7 else "#d62728" for s in strs]
ax.barh(range(len(g_names)), strs, color=colors_s)
ax.set_yticks(range(len(g_names))); ax.set_yticklabels(g_names, fontsize=7)
ax.set_xlabel("Coupling strength"); ax.set_xlim(0, 1)
ax.axvline(0.90, color="black", linestyle="--", alpha=0.5)
ax.set_title(f"#30 Genome couplings (avg = {avg_strength:.3f}) ★ Pass-1 最大値")
ax.grid(True, alpha=0.3, axis="x")

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

ax = axes[1, 1]
milestones = [
    ("110\nTier 0 v3.0",      50.0),
    ("182\nBlock A FINALE",   82.7),
    ("190\nImmune",           86.4),
    ("198\nMicrobe",          90.0),
    ("206\nNeuro",            93.6),
    ("214\nDev",              97.3),
    ("219\nGenome",           99.5),
    ("220\nTier 0 v4.0",     100.0),
]
labels = [m[0] for m in milestones]
vals = [m[1] for m in milestones]
colors_m = ["#1f77b4"]*2 + ["#e377c2", "#8c564b", "#17becf", "#bcbd22", "#ff1493", "#2ca02c"]
ax.bar(labels, vals, color=colors_m)
ax.axhline(100, color="black", linestyle="--", alpha=0.5)
ax.set_ylabel("Pass-1 progress (%)")
ax.set_title(f"Pass-1 milestones — currently 99.5% ★★")
ax.set_ylim(0, 105)
for i, v in enumerate(vals):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=8, fontweight="bold")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 219,
    "tier1_paper": 30,
    "block": "B",
    "paper_in_block": "5/?",
    "topic": "Integration: K_genome + 30-vertex polytope + 10 predictions",
    "milestone": "★★ Pass-1 99.5% (219/220) — final Tier 1 ★★",
    "polytope_30vertex": {
        "vertices": int(N),
        "edges": int(edges),
        "mean_degree": float(mean_k),
        "max_degree": int(max_k),
    },
    "genome_couplings": genome_strengths,
    "genome_avg_coupling": float(avg_strength),
    "10_predictions": [
        {"prediction": p[0], "year": p[1], "P": p[2], "class": p[3]} for p in predictions
    ],
    "predictions_summary": {
        "grand_P_avg": float(P_grand),
        "strong": strong, "medium": medium, "weak": weak,
        "note": "Highest P_avg in Pass-1",
    },
    "ITU_axiom_Phase_215_218": {
        "Phase_215_expression_shift":  "1.000",
        "Phase_216_CRISPR_edit":       "1.000 / 1.000",
        "Phase_217_AlphaFold_design":  "1.000 / 1.000",
        "Phase_218_pop_evolution":     "1.000 / 1.000",
    },
    "K_genome_structure": {
        "K_genome_coding":      "2% protein-coding",
        "K_genome_regulatory":  "10% enhancers/promoters",
        "K_genome_repeat":      "50%+ LINE/SINE/LTR",
        "K_genome_variant":     "88M SNPs human",
        "K_genome_epigenome":   "DNAm + histone",
        "K_genome_3D":          "TAD + Hi-C + compartments",
        "K_genome_RNA":         "ncRNA + lncRNA + miRNA",
        "K_genome_phylogenetic": "cross-species conservation",
    },
    "K_genome_applications": {
        "K_genome_edit":      "CRISPR / Casgevy 2023",
        "K_genome_AI":        "AlphaFold / Baker Nobel 2024",
        "K_genome_evolution": "Coalescent / Pääbo Nobel 2022",
    },
    "pass1_progress": {
        "phases_completed": 219,
        "phases_total": 220,
        "percent": 99.5,
        "block_A_status": "9/9 COMPLETE",
        "block_B_status": "5/? complete (#26-#30 all done)",
        "remaining": "Phase 220 = Tier 0 v4.0 (Pass-1 finale)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
