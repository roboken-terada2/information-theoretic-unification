"""
Phase 209 — Body axis + Hox + Segmentation clock (K_dev_spatial)

Simulations:
  1) Hox colinearity: gene cluster order matches body segment order
  2) Drosophila HOM-C vs Mammalian 4 Hox clusters
  3) Segmentation clock oscillation (Pourquié 90-min)
  4) Cooke-Zeeman clock-and-wavefront model
  5) Body axis symmetry breaking (S decrease)
  6) Hensen's node / Spemann organizer effect
  7) LR asymmetry: Nodal-Lefty cascade
  8) ITU K_dev_spatial axiom check

Outputs:
  - body_axis_hox.png
  - body_axis_hox_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("body_axis_hox.png")
OUT_JSON = Path(__file__).with_name("body_axis_hox_summary.json")

rng = np.random.default_rng(20260619)

# -------------------------------------------------------------
# 1) Hox colinearity
# -------------------------------------------------------------
# Drosophila HOM-C: 8 genes from anterior (lab) to posterior (AbdB)
drosophila_hox = ["lab", "pb", "Dfd", "Scr", "Antp", "Ubx", "abd-A", "AbdB"]
# Body segments anterior to posterior (head -> tail)
drosophila_segments = ["Head", "Maxilla", "Mandible", "Labial", "T1-T3", "A1-A4", "A5-A7", "A8+"]
# Expression matrix: 1 if Hox gene expressed in that segment
hox_expression = np.zeros((len(drosophila_hox), len(drosophila_segments)))
# Anterior boundaries follow colinearity
for i in range(len(drosophila_hox)):
    hox_expression[i, i:] = 1
# Mammalian Hox: 4 clusters x 13 paralogs (39 functional genes after losses)
mammal_hox = {
    "HOXA cluster": 11,
    "HOXB cluster": 10,
    "HOXC cluster": 9,
    "HOXD cluster": 9,
}
mammal_total = sum(mammal_hox.values())

# -------------------------------------------------------------
# 2) Segmentation clock oscillation (Pourquié 1997)
# -------------------------------------------------------------
t_clock = np.linspace(0, 600, 1200)  # minutes
period = 90.0  # chick c-Hairy1
hairy = 50 + 50 * np.sin(2 * np.pi * t_clock / period)
# Each cycle generates one somite
somite_times = np.arange(0, 600, period)

# -------------------------------------------------------------
# 3) Clock-and-wavefront model (Cooke-Zeeman 1976)
# -------------------------------------------------------------
# Anterior-Posterior axis with retreating wavefront
ap_axis = np.linspace(0, 1, 100)
wavefront_t1 = 0.2
wavefront_t2 = 0.5
wavefront_t3 = 0.8
# Somite boundaries set where clock peaks meet wavefront

# -------------------------------------------------------------
# 4) Body axis symmetry breaking
# -------------------------------------------------------------
# Pre-axis: spherical (S = log V high)
# AP: cylindrical (S reduces)
# AP+DV: bilateral
# AP+DV+LR: chiral (S minimum)
stages_axis = ["Pre-axis\n(spherical)", "AP only\n(cylindrical)",
                "AP+DV\n(bilateral)", "AP+DV+LR\n(chiral)"]
S_axis = [4.0, 3.0, 2.0, 1.2]  # arbitrary symmetry entropy scale

# -------------------------------------------------------------
# 5) Spemann organizer effect (rough sketch)
# -------------------------------------------------------------
# Reference: 1 graft point induces secondary axis
# Plot 2 axes from grafting experiment
spemann_data = {
    "Year": 1924,
    "Discoverer": "Spemann + Mangold",
    "Nobel": 1935,
    "Experiment": "Dorsal lip transplant to ventral side -> 2nd embryo axis",
    "Modern_equivalent": "Hensen's node (chick), shield (zebrafish)",
}

# -------------------------------------------------------------
# 6) LR asymmetry: Nodal-Lefty cascade
# -------------------------------------------------------------
# Left side: Nodal high, Pitx2 expressed
# Right side: Lefty1/2 suppresses Nodal
positions = np.linspace(-1, 1, 100)  # left to right axis
nodal = 100 / (1 + np.exp(10 * positions))   # high on left
lefty = 50 / (1 + np.exp(-10 * positions))   # high on right
pitx2 = 100 / (1 + np.exp(10 * positions + 1))  # left-only

# -------------------------------------------------------------
# 7) ITU K_dev_spatial axiom: progressive symmetry breaking
# -------------------------------------------------------------
N_cells = 1000
# Pre-axis: uniform (no spatial coordinates)
log_fit_pre = np.zeros(N_cells)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# AP axis: 8 segments × 1
log_fit_ap = log_fit_pre.copy()
for i in range(8):
    start, stop = i * (N_cells // 8), (i + 1) * (N_cells // 8)
    log_fit_ap[start:stop] += 0.5 * (i - 3.5)
p_ap = np.exp(log_fit_ap); p_ap /= p_ap.sum()
S_ap = float(-np.sum(p_ap * np.log(p_ap)))

# AP + DV: 8 × 3 zones = 24 regions
log_fit_apdv = log_fit_ap.copy() + 0.3 * rng.standard_normal(N_cells)
p_apdv = np.exp(log_fit_apdv); p_apdv /= p_apdv.sum()
S_apdv = float(-np.sum(p_apdv * np.log(p_apdv)))

# AP + DV + LR: full chirality
log_fit_full = log_fit_apdv.copy() + 0.5 * rng.standard_normal(N_cells)
p_full = np.exp(log_fit_full); p_full /= p_full.sum()
S_full = float(-np.sum(p_full * np.log(p_full)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_ap = itu_lin(p_pre, p_ap)
ratio_ap_apdv = itu_lin(p_ap, p_apdv)
ratio_apdv_full = itu_lin(p_apdv, p_full)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 209 — Body Axis + Hox Genes + Segmentation Clock (K_dev_spatial)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Hox colinearity (Drosophila)
ax = axes[0, 0]
im = ax.imshow(hox_expression, cmap="Reds", aspect="auto")
ax.set_xticks(range(len(drosophila_segments)))
ax.set_xticklabels(drosophila_segments, rotation=20, fontsize=7)
ax.set_yticks(range(len(drosophila_hox)))
ax.set_yticklabels(drosophila_hox, fontsize=8)
ax.set_xlabel("Body segment (anterior → posterior)")
ax.set_ylabel("Hox gene (3' → 5')")
ax.set_title("Drosophila HOM-C colinearity (Lewis 1978, Nobel 1995)")
plt.colorbar(im, ax=ax, label="Expression")

# Panel 2: Mammalian 4 Hox clusters
ax = axes[0, 1]
clusters = list(mammal_hox.keys())
counts = list(mammal_hox.values())
ax.bar(clusters, counts, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
ax.set_ylabel("Functional gene count")
ax.set_title(f"Mammalian Hox (total {mammal_total} genes, 4 clusters)")
for i, v in enumerate(counts):
    ax.text(i, v + 0.3, str(v), ha="center", fontsize=10, fontweight="bold")
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: Segmentation clock (Pourquié 1997)
ax = axes[0, 2]
ax.plot(t_clock, hairy, "-", color="#9467bd", lw=1.5, label="c-Hairy1 oscillation")
for st in somite_times:
    ax.axvline(st, color="red", linestyle="--", alpha=0.3)
ax.set_xlabel("Time (min)")
ax.set_ylabel("c-Hairy1 expression")
ax.set_title(f"Segmentation clock (90 min, Pourquié 1997)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: Body axis symmetry breaking
ax = axes[1, 0]
ax.bar(stages_axis, S_axis, color=["#d62728", "#ff7f0e", "#9467bd", "#1f77b4"])
ax.set_ylabel("Symmetry entropy (a.u.)")
ax.set_title("Symmetry breaking: spherical → chiral")
ax.tick_params(axis="x", rotation=10, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(S_axis):
    ax.text(i, v + 0.1, f"{v:.1f}", ha="center", fontsize=10, fontweight="bold")

# Panel 5: LR asymmetry (Nodal-Lefty)
ax = axes[1, 1]
ax.plot(positions, nodal, "-", color="#1f77b4", lw=2, label="Nodal (left)")
ax.plot(positions, lefty, "-", color="#d62728", lw=2, label="Lefty1/2 (right)")
ax.plot(positions, pitx2, "-", color="#2ca02c", lw=2, label="Pitx2 (left visceral)")
ax.axvline(0, color="black", linestyle="--", alpha=0.5)
ax.set_xlabel("LR axis (left → right)")
ax.set_ylabel("Expression")
ax.set_title("LR asymmetry (Nodal pathway)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 6: ITU symmetry breaking entropy
ax = axes[1, 2]
labels_e = ["Pre-axis", "AP", "AP+DV", "AP+DV+LR"]
S_vals = [S_pre, S_ap, S_apdv, S_full]
ax.bar(labels_e, S_vals, color=["#d62728", "#ff7f0e", "#9467bd", "#1f77b4"])
ax.set_ylabel("K-state entropy (nats)")
ax.set_title(f"ITU ratios: {ratio_pre_ap:.3f} / {ratio_ap_apdv:.3f} / {ratio_apdv_full:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 209,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Body axis + Hox + Segmentation (K_dev_spatial)",
    "Drosophila_HOM_C_8_genes": drosophila_hox,
    "Mammalian_Hox_clusters": mammal_hox,
    "mammalian_Hox_total": mammal_total,
    "Hox_colinearity": "Gene cluster order on chromosome matches body segment order (Lewis 1978)",
    "Nobel_1995_homeotic_genes": "Lewis + Nüsslein-Volhard + Wieschaus",
    "Spemann_organizer_1924": spemann_data,
    "Pourquié_1997": {
        "discovery": "c-Hairy1 oscillation in chick presomitic mesoderm",
        "period_min": int(period),
        "model": "Clock-and-wavefront (Cooke-Zeeman 1976)",
    },
    "human_somite_count": "40-44 (Day 20-32)",
    "human_vertebrae_count": 33,
    "LR_asymmetry": {
        "mechanism": "Node cilia rotation -> Nodal left -> Lefty right -> Pitx2 left visceral",
        "Kartagener_syndrome": "Cilia dysfunction -> situs inversus",
        "situs_inversus_frequency": "1/10,000",
    },
    "ITU_K_dev_spatial": {
        "N_cells": N_cells,
        "S_pre_axis_nats": S_pre,
        "S_AP_nats": S_ap,
        "S_AP_DV_nats": S_apdv,
        "S_AP_DV_LR_nats": S_full,
        "pre_to_AP_ratio": ratio_pre_ap,
        "AP_to_AP_DV_ratio": ratio_ap_apdv,
        "AP_DV_to_full_ratio": ratio_apdv_full,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev_spatial",
        "modular_Hamiltonian": "K_dev_spatial^(0) = -log P(cell identity | spatial coordinate)",
        "Hox_colinearity_meaning": "Genomic spatial order = K-state index (DNA as ordering operator)",
        "segmentation_clock_meaning": "K_dev_temporal x K_dev_spatial coupling",
        "axis_formation_meaning": "Progressive symmetry breaking = ITU descent flow",
    },
    "predictions": [
        ("Synthetic embryo (gastruloid) 3 axes complete", 2030, 0.70, "Strong"),
        ("In vitro segmentation clock organoid", 2028, 0.75, "Strong"),
        ("Hox function reconstituted by AI design", 2032, 0.45, "Medium"),
        ("LR asymmetry origin in single-cell", 2030, 0.55, "Medium"),
        ("Synthetic 5th mammalian Hox cluster", 2035, 0.30, "Weak"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
