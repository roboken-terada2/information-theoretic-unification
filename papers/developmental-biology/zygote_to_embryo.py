"""
Phase 207 — Zygote → Embryo + K_dev introduction (Block B 4/?)

Simulations:
  1) Cell count exponential growth (zygote -> 128 blastocyst -> 10^13 adult)
  2) Cell division count (~45 doublings)
  3) 3 germ layers (ectoderm/mesoderm/endoderm) by derived tissues
  4) Cell potency hierarchy (toti/pluri/multi/oligo/uni)
  5) Developmental timeline (day post-fertilization to organogenesis)
  6) Cell type count: human estimate (broad 200, fine 700)
  7) ITU K_dev axiom check: potency descent (zygote -> differentiated)

Outputs:
  - zygote_to_embryo.png
  - zygote_to_embryo_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("zygote_to_embryo.png")
OUT_JSON = Path(__file__).with_name("zygote_to_embryo_summary.json")

rng = np.random.default_rng(20260617)

# -------------------------------------------------------------
# 1) Cell count exponential growth
# -------------------------------------------------------------
# Stages: zygote (1), 8-cell (3 div), morula (~16), blastocyst (128), gastrulation (10^4),
# week 8 (10^9), birth (10^12), adult (3.7e13)
stages_growth = [
    ("Zygote (D0)",    1),
    ("8-cell (D3)",    8),
    ("Morula (D4)",    32),
    ("Blastocyst (D6)", 128),
    ("Gastrulation (D14)", 1e4),
    ("Week 8 organogenesis", 1e9),
    ("Birth (W38)",    1e12),
    ("Adult",          3.7e13),
]

# Doublings (log2 of cell count)
doublings = [np.log2(c) for _, c in stages_growth]

# -------------------------------------------------------------
# 2) 3 germ layers and tissue derivatives
# -------------------------------------------------------------
germ_layers = {
    "Ectoderm (外胚葉)": ["Nervous system", "Epidermis", "Sensory organs", "Tooth enamel"],
    "Mesoderm (中胚葉)": ["Muscle", "Bone", "Cardiovascular", "Kidney", "Gonads", "Connective"],
    "Endoderm (内胚葉)": ["GI tract", "Lung", "Liver", "Pancreas", "Thyroid", "Bladder"],
}

# -------------------------------------------------------------
# 3) Cell potency hierarchy
# -------------------------------------------------------------
potency = {
    "Totipotent":    {"capability": "All cells incl. placenta",  "examples": "Zygote, 2-cell"},
    "Pluripotent":   {"capability": "All 3 germ layers",          "examples": "ICM, ES, iPS"},
    "Multipotent":   {"capability": "1 lineage",                  "examples": "HSC, NSC"},
    "Oligopotent":   {"capability": "Few cell types",             "examples": "Myeloid progenitor"},
    "Unipotent":     {"capability": "Single cell type",           "examples": "Satellite, spermatogonia"},
}

# Information content of each potency level (rough # cell types reachable)
potency_reach = {"Totipotent": 220, "Pluripotent": 200, "Multipotent": 30,
                  "Oligopotent": 5, "Unipotent": 1}

# -------------------------------------------------------------
# 4) Developmental timeline (days post-fertilization)
# -------------------------------------------------------------
events = {
    "Fertilization":           0,
    "Cleavage (2-cell)":       1,
    "Morula":                  4,
    "Blastocyst":              5,
    "Implantation":            7,
    "Gastrulation":            14,
    "Neural tube":             22,
    "Heart beat":              22,
    "Limb buds":               28,
    "Organogenesis complete":  56,
    "Fetal period start":      63,
    "Lung surfactant":         168,
    "Birth":                   266,
}

# -------------------------------------------------------------
# 5) Cell type counts (human)
# -------------------------------------------------------------
cell_types = {
    "Classical broad (Alberts)":     200,
    "Human Cell Atlas v1 (2024)":    400,
    "Single-cell RNA seq (fine)":    700,
}

# -------------------------------------------------------------
# 6) ITU K_dev axiom check: potency descent
# -------------------------------------------------------------
# Model: cell population in a potency state
# Pluripotent: broad distribution over 200 fates
# Final differentiated: peaked on 1 fate
N_fates = 200
log_fit_pluri = np.zeros(N_fates)   # uniform
log_fit_pluri += 0.01 * rng.standard_normal(N_fates)
p_pluri = np.exp(log_fit_pluri); p_pluri /= p_pluri.sum()
S_pluri = float(-np.sum(p_pluri * np.log(p_pluri)))

# Multipotent (HSC): one lineage cluster (10 fates) elevated
log_fit_multi = log_fit_pluri.copy()
log_fit_multi[50:60] += 3.0
p_multi = np.exp(log_fit_multi); p_multi /= p_multi.sum()
S_multi = float(-np.sum(p_multi * np.log(p_multi)))

# Unipotent: 1 fate dominant
log_fit_uni = log_fit_pluri.copy()
log_fit_uni[55] += 8.0
p_uni = np.exp(log_fit_uni); p_uni /= p_uni.sum()
S_uni = float(-np.sum(p_uni * np.log(p_uni)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pluri_multi = itu_lin(p_pluri, p_multi)
ratio_multi_uni = itu_lin(p_multi, p_uni)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 207 — Zygote → Embryo + K_dev Introduction (Block B 4/?)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Cell count exponential growth
ax = axes[0, 0]
labels = [s[0] for s in stages_growth]
counts = [s[1] for s in stages_growth]
ax.semilogy(range(len(labels)), counts, "o-", color="#1f77b4", lw=2, markersize=10)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=30, fontsize=7, ha="right")
ax.set_ylabel("Cell count (log)")
ax.set_title(f"1 zygote → 3.7e13 cells (~{max(doublings):.0f} doublings)")
ax.grid(True, alpha=0.3, which="both")

# Panel 2: 3 germ layers
ax = axes[0, 1]
colors_g = ["#1f77b4", "#ff7f0e", "#2ca02c"]
y_pos = 0
for i, (layer, tissues) in enumerate(germ_layers.items()):
    ax.barh(i, len(tissues), color=colors_g[i], alpha=0.7)
    ax.text(0.2, i, ", ".join(tissues), va="center", fontsize=7, color="white", fontweight="bold")
ax.set_yticks(range(len(germ_layers)))
ax.set_yticklabels(list(germ_layers.keys()), fontsize=9)
ax.set_xticks([])
ax.set_xlim(0, 8)
ax.set_title("3 germ layers (gastrulation D14)")

# Panel 3: Cell potency hierarchy
ax = axes[0, 2]
p_names = list(potency_reach.keys())
reaches = list(potency_reach.values())
colors_p = ["#d62728", "#ff7f0e", "#9467bd", "#1f77b4", "#2ca02c"]
ax.barh(range(len(p_names)), reaches, color=colors_p)
ax.set_xscale("log")
ax.set_yticks(range(len(p_names)))
ax.set_yticklabels(p_names, fontsize=9)
ax.set_xlabel("Reachable cell types (log)")
ax.set_title("Cell potency hierarchy")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: Developmental timeline
ax = axes[1, 0]
event_names = list(events.keys())
event_days = list(events.values())
ax.barh(range(len(event_names)), event_days, color="#9467bd")
ax.set_xscale("symlog", linthresh=1)
ax.set_yticks(range(len(event_names)))
ax.set_yticklabels(event_names, fontsize=7)
ax.set_xlabel("Days post-fertilization (symlog)")
ax.set_title("Human developmental timeline")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 5: Cell type count estimates
ax = axes[1, 1]
ct_names = list(cell_types.keys())
ct_vals = list(cell_types.values())
ax.bar(ct_names, ct_vals, color=["#1f77b4", "#ff7f0e", "#d62728"])
ax.set_ylabel("Cell type count")
ax.set_title("Human cell type estimates")
ax.tick_params(axis="x", rotation=15, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(ct_vals):
    ax.text(i, v + 10, str(v), ha="center", fontsize=10, fontweight="bold")

# Panel 6: K_dev ITU descent
ax = axes[1, 2]
states = ["Pluripotent", "Multipotent", "Unipotent"]
S_vals = [S_pluri, S_multi, S_uni]
ax.bar(states, S_vals, color=["#d62728", "#9467bd", "#2ca02c"])
ax.set_ylabel("Lineage entropy (nats)")
ax.set_title(f"K_dev descent: Pluri→Multi={ratio_pluri_multi:.3f}, Multi→Uni={ratio_multi_uni:.3f}")
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(S_vals):
    ax.text(i, v + 0.1, f"{v:.2f}", ha="center", fontsize=10, fontweight="bold")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 207,
    "tier1_paper": 29,
    "block": "B",
    "paper_in_block": "4/?",
    "topic": "Zygote -> Embryo + K_dev introduction",
    "cell_count_growth": {s[0]: float(s[1]) for s in stages_growth},
    "total_doublings_zygote_to_adult": float(max(doublings)),
    "germ_layers_3": {k: v for k, v in germ_layers.items()},
    "cell_potency": potency,
    "potency_reach_estimates": potency_reach,
    "developmental_timeline_days": events,
    "human_cell_type_counts": cell_types,
    "pregnancy_duration_days": 266,
    "adult_cell_count_Bianconi_2013": 3.7e13,
    "ITU_K_dev_potency_descent": {
        "N_fates": N_fates,
        "S_pluripotent_nats": S_pluri,
        "S_multipotent_nats": S_multi,
        "S_unipotent_nats": S_uni,
        "pluri_to_multi_ratio": ratio_pluri_multi,
        "multi_to_uni_ratio": ratio_multi_uni,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev",
        "sub_states": [
            "K_dev_temporal (timing)",
            "K_dev_spatial (body axes)",
            "K_dev_lineage (Waddington)",
            "K_dev_morphogen (gradients)",
            "K_dev_stem (potency)",
            "K_dev_organoid (in vitro)",
            "K_dev_aging (life cycle close)",
            "K_dev_teratology (defects)",
        ],
        "axiom": "delta S(rho_lineage) = delta Tr[K_dev^(0) rho_lineage]",
        "modular_Hamiltonian": "K_dev^(0) = -log P(cell type | spatiotemporal coord, genotype)",
        "cell_differentiation_meaning": "ITU descent flow on lineage manifold (S monotonic decrease)",
        "duality_with_aging": "Block B #6 Aging is the temporal reversal/closure of K_dev",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
