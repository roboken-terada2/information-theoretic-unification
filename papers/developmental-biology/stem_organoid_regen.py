"""
Phase 211 — Stem cells + Organoids + Regeneration (K_dev_stem)

Simulations:
  1) Adult stem cell catalog (HSC/NSC/MSC/ISC/Satellite/Skin)
  2) Lgr5+ ISC turnover dynamics (Clevers 2007)
  3) Organoid history milestones
  4) Regeneration capacity across species
  5) Axolotl limb regeneration stages
  6) Liver regeneration kinetics
  7) ITU K_dev_stem axiom: 1 cell -> organoid self-organization

Outputs:
  - stem_organoid_regen.png
  - stem_organoid_regen_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("stem_organoid_regen.png")
OUT_JSON = Path(__file__).with_name("stem_organoid_regen_summary.json")

rng = np.random.default_rng(20260621)

# -------------------------------------------------------------
# 1) Adult stem cells
# -------------------------------------------------------------
adult_stem = {
    "HSC (骨髄)":       {"fraction": 1e-4,  "turnover_days": 30,   "potency": "Multipotent"},
    "NSC (SVZ+DG)":     {"fraction": 1e-3,  "turnover_days": 60,   "potency": "Multipotent"},
    "MSC (骨髄+脂肪)":   {"fraction": 1e-3,  "turnover_days": 30,   "potency": "Multipotent"},
    "ISC (Lgr5+ crypt)": {"fraction": 5e-5,  "turnover_days": 5,    "potency": "Multipotent"},
    "Satellite (筋)":   {"fraction": 1e-2,  "turnover_days": 365,  "potency": "Unipotent"},
    "Skin (basal)":     {"fraction": 1e-3,  "turnover_days": 30,   "potency": "Multipotent"},
}

# -------------------------------------------------------------
# 2) Lgr5+ ISC turnover (Clevers 2007)
# -------------------------------------------------------------
days = np.linspace(0, 14, 200)
# Crypt has ~5 Lgr5+ cells; produces ~250 epithelial cells via TA daughters
N_Lgr5 = 5
N_total_epithelial = 250
N_turnover_days = 5
# Exponential replacement
intact_fraction = np.exp(-days / N_turnover_days * np.log(2))

# -------------------------------------------------------------
# 3) Organoid history
# -------------------------------------------------------------
organoid_history = {
    "Sato intestinal (Clevers)":  {"year": 2009, "tissue": "Intestine"},
    "Lancaster cerebral":          {"year": 2013, "tissue": "Brain"},
    "Takebe liver":                {"year": 2014, "tissue": "Liver"},
    "Kim kidney":                  {"year": 2015, "tissue": "Kidney"},
    "Hofer pancreas":              {"year": 2017, "tissue": "Pancreas"},
    "Lung organoid":               {"year": 2019, "tissue": "Lung"},
    "COVID lung infection model":  {"year": 2020, "tissue": "Lung/COVID"},
    "Cerebral + EEG-like":         {"year": 2024, "tissue": "Brain consciousness debate"},
}

# -------------------------------------------------------------
# 4) Regeneration capacity by species
# -------------------------------------------------------------
species_regen = {
    "Planaria":        {"score": 100, "capacity": "Whole-body"},
    "Hydra":           {"score": 95,  "capacity": "Whole-body"},
    "Axolotl":         {"score": 90,  "capacity": "Limb+heart+spinal cord"},
    "Zebrafish":       {"score": 75,  "capacity": "Heart+fin+optic"},
    "Lizard":          {"score": 40,  "capacity": "Tail only"},
    "Mouse":           {"score": 25,  "capacity": "Liver+skin+blood"},
    "Human":           {"score": 25,  "capacity": "Liver+skin+blood"},
}

# -------------------------------------------------------------
# 5) Axolotl limb regeneration stages
# -------------------------------------------------------------
axolotl_stages = {
    "Amputation":              0,
    "Wound epithelium":        1.5,
    "Blastema initiation":     5,
    "AEC + blastema growth":   10,
    "Pattern restoration":     17,
    "Re-differentiation":      24,
    "Complete limb":           30,
}

# -------------------------------------------------------------
# 6) Liver regeneration kinetics
# -------------------------------------------------------------
days_liver = np.linspace(0, 21, 200)
# 75% hepatectomy: remaining 25% expands to 100% in 14 days
liver_mass_pct = 25 + 75 * (1 - np.exp(-days_liver / 4))

# -------------------------------------------------------------
# 7) ITU K_dev_stem axiom: 1 cell -> organoid
# -------------------------------------------------------------
N_cells_organoid = 1000
# Start: 1 ISC (Lgr5+, peaked distribution)
log_fit_start = -np.linspace(0, 10, N_cells_organoid) ** 2
p_start = np.exp(log_fit_start); p_start /= p_start.sum()
S_start = float(-np.sum(p_start * np.log(p_start)))

# After organoid maturation: multiple lineages emerge (Paneth, enteroendocrine, goblet, enterocyte, Lgr5+ stem)
# 5 cell types distributed
log_fit_org = -((np.arange(N_cells_organoid) - 500) ** 2) / 50000
# Add 5 lineage peaks
for i in [100, 300, 500, 700, 900]:
    log_fit_org += -((np.arange(N_cells_organoid) - i) ** 2) / 5000 * (-0.5)
p_org = np.exp(log_fit_org); p_org /= p_org.sum()
S_org = float(-np.sum(p_org * np.log(p_org)))

log_p_start = np.log(np.clip(p_start, 1e-30, None))
dp = p_org - p_start
dS_lin = -np.sum(dp * (1.0 + log_p_start))
dK_lin = -np.sum(dp * log_p_start)
ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 211 — Stem Cells + Organoids + Regeneration (K_dev_stem)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Adult stem cells
ax = axes[0, 0]
sc_names = list(adult_stem.keys())
fractions = [adult_stem[s]["fraction"] for s in sc_names]
turnover = [adult_stem[s]["turnover_days"] for s in sc_names]
x = np.arange(len(sc_names))
width = 0.4
ax.bar(x - width/2, fractions, width, color="#1f77b4", label="Fraction", log=True)
ax2 = ax.twinx()
ax2.bar(x + width/2, turnover, width, color="#d62728", label="Turnover (days)")
ax.set_xticks(x); ax.set_xticklabels(sc_names, fontsize=7, rotation=15)
ax.set_ylabel("Stem fraction (log)", color="#1f77b4")
ax2.set_ylabel("Turnover days", color="#d62728")
ax.set_title("Adult stem cell catalog")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="upper right", fontsize=8)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 2: Lgr5+ ISC turnover
ax = axes[0, 1]
ax.plot(days, intact_fraction * 100, "-", color="#2ca02c", lw=2)
ax.axvline(N_turnover_days, color="red", linestyle="--", label=f"5-day half-life")
ax.set_xlabel("Days")
ax.set_ylabel("Initial epithelium remaining (%)")
ax.set_title(f"Lgr5+ ISC turnover (Clevers 2007); 5 cells/crypt → {N_total_epithelial} epithelial")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Organoid history
ax = axes[0, 2]
years = [d["year"] for d in organoid_history.values()]
labels_org = [k.split(" ")[0] + "\n" + d["tissue"] for k, d in organoid_history.items()]
ax.barh(range(len(years)), years, color="#9467bd")
ax.set_yticks(range(len(years)))
ax.set_yticklabels(labels_org, fontsize=6)
ax.set_xlim(2008, 2026)
ax.set_xlabel("Year")
ax.set_title("Organoid revolution timeline")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: Regeneration species comparison
ax = axes[1, 0]
sp_names = list(species_regen.keys())
sp_scores = [species_regen[s]["score"] for s in sp_names]
colors_sp = ["#2ca02c" if s > 80 else "#ff7f0e" if s > 40 else "#d62728" for s in sp_scores]
ax.barh(range(len(sp_names)), sp_scores, color=colors_sp)
ax.set_yticks(range(len(sp_names)))
ax.set_yticklabels(sp_names, fontsize=8)
ax.set_xlabel("Regeneration capacity score (0-100)")
ax.set_title("Evolution lost regeneration")
ax.grid(True, alpha=0.3, axis="x")

# Panel 5: Axolotl + Liver regeneration
ax = axes[1, 1]
ax.plot(days_liver, liver_mass_pct, "-", color="#1f77b4", lw=2, label="Liver (75% hepatectomy)")
ax.set_xlabel("Days post-injury")
ax.set_ylabel("Tissue mass (%)")
ax.set_title("Liver regeneration: 14-day complete recovery")
ax.axhline(100, color="black", linestyle="--", alpha=0.3)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 6: ITU organoid self-organization
ax = axes[1, 2]
ax.plot(np.arange(N_cells_organoid), p_start, "-", color="#d62728", lw=1.5,
        label=f"Start (1 ISC)  S={S_start:.3f}")
ax.plot(np.arange(N_cells_organoid), p_org, "-", color="#2ca02c", lw=1.5,
        label=f"Mature organoid S={S_org:.3f}")
ax.set_xlabel("Cell state index")
ax.set_ylabel("Probability")
ax.set_title(f"K_dev_stem self-organization;  ITU δS/δ⟨K⟩ = {ratio:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 211,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Stem cells + Organoids + Regeneration (K_dev_stem)",
    "adult_stem_cells": adult_stem,
    "Lgr5_ISC_Clevers_2007": {
        "cells_per_crypt": N_Lgr5,
        "epithelial_cells_per_crypt": N_total_epithelial,
        "turnover_days": N_turnover_days,
        "Sato_intestinal_organoid_2009": "1 Lgr5+ cell -> mini-gut in vitro",
    },
    "organoid_history": organoid_history,
    "Lancaster_cerebral_organoid_2013": {
        "size_mm_max": 4.5,
        "structure": "Cortical layers + cerebral hemispheres",
        "disease_model": "Microcephaly (CDK5RAP2)",
        "ethics_debate_2024": "EEG-like activity raises consciousness questions",
    },
    "regeneration_capacity_by_species": species_regen,
    "axolotl_limb_regeneration_days": axolotl_stages,
    "liver_regeneration": {
        "75pct_hepatectomy_recovery_days": 14,
        "mechanism": "Mature hepatocyte re-entry + LPC activation",
    },
    "planaria_minimum_fragment": "1/300 body fragment regenerates whole",
    "ITU_K_dev_stem": {
        "N_cells": N_cells_organoid,
        "S_start_1_ISC_nats": S_start,
        "S_mature_organoid_nats": S_org,
        "delta_S": S_org - S_start,
        "ratio_dS_over_dK": ratio,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev_stem",
        "modular_Hamiltonian": "K_dev_stem^(0) = -log P(progeny | stem state, niche)",
        "organoid_meaning": "Self-organization from 1 stem cell = ITU pattern generation",
        "regeneration_meaning": "K_dev_stem reactivation + K_dev_morphogen reuse",
        "axolotl_meaning": "Conserved K_dev programs reactivated post-injury",
        "evolution_loss": "Mammals lost K_dev_stem accessibility (cost: regeneration vs cancer trade-off)",
    },
    "predictions": [
        ("Functional kidney organoid transplant", 2032, 0.55, "Medium"),
        ("Pancreas β-cell organoid for T1D", 2030, 0.70, "Strong"),
        ("Cerebral organoid + EEG consciousness debate", 2028, 0.80, "Strong"),
        ("Mammalian limb regen via blastema engineering", 2035, 0.30, "Weak"),
        ("iPS oocyte/sperm clinical (infertility)", 2030, 0.45, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
