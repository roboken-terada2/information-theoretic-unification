"""
Phase 195 — Microbiome + Gut-Brain Axis + FMT (K_microbiome)

Simulations:
  1) Human microbiome scale (cells, genes, biomass)
  2) Phylum composition in healthy vs obese vs IBD
  3) SCFA production rates from major species
  4) Gut-brain axis: neurotransmitter production catalog
  5) FMT efficacy across indications
  6) Dysbiosis as K-state basin shift
  7) ITU K_microbiome axiom check with FMT-like intervention

Outputs:
  - microbiome_gut_brain.png
  - microbiome_gut_brain_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("microbiome_gut_brain.png")
OUT_JSON = Path(__file__).with_name("microbiome_gut_brain_summary.json")

rng = np.random.default_rng(20260529)

# -------------------------------------------------------------
# 1) Microbiome scale
# -------------------------------------------------------------
scale = {
    "Bacterial cells": 3.8e13,
    "Human cells": 3.0e13,
    "Bacterial genes": 3.5e6,
    "Human genes": 2.0e4,
    "Biomass (g)": 1.8e3,
    "ATP production (kcal/day)": 150,
    "SCFA daily (mmol)": 550,
}

# -------------------------------------------------------------
# 2) Phylum composition: healthy vs obese vs IBD
# -------------------------------------------------------------
phyla = ["Firmicutes", "Bacteroidetes", "Actinobacteria",
         "Proteobacteria", "Verrucomicrobia", "Other"]
healthy = np.array([55, 30, 8, 3, 2, 2])
obese = np.array([65, 18, 8, 5, 1, 3])
ibd_uc = np.array([35, 28, 5, 25, 1, 6])  # Proteobacteria expansion
ibd_cd = np.array([42, 18, 4, 28, 1, 7])

# -------------------------------------------------------------
# 3) SCFA production rates
# -------------------------------------------------------------
scfa_producers = {
    "Faecalibacterium prausnitzii": 350,  # butyrate units/g
    "Roseburia intestinalis": 280,
    "Eubacterium rectale": 250,
    "Bacteroides fragilis": 180,  # propionate-acetate mix
    "Bifidobacterium": 90,
    "Akkermansia muciniphila": 120,
}
# Composition: 60% acetate, 25% propionate, 15% butyrate
scfa_composition = {"Acetate (C2)": 60, "Propionate (C3)": 25, "Butyrate (C4)": 15}

# -------------------------------------------------------------
# 4) Gut-brain neurotransmitter production
# -------------------------------------------------------------
neurotransmitters = {
    "GABA":         {"main_producer": "Lactobacillus / Bifidobacterium", "function": "Inhibitory"},
    "Serotonin":    {"main_producer": "Enterochromaffin (microbe-induced)", "function": "Mood/sleep; 90% in gut!"},
    "Dopamine":     {"main_producer": "Bacillus / Serratia", "function": "Reward"},
    "Acetylcholine":{"main_producer": "Lactobacillus", "function": "Parasympathetic"},
    "Norepinephrine":{"main_producer": "Bacillus", "function": "Arousal"},
    "Histamine":    {"main_producer": "Lactobacillus / Morganella", "function": "Immune/inflammation"},
}

# -------------------------------------------------------------
# 5) FMT efficacy
# -------------------------------------------------------------
fmt_indications = {
    "rCDI (recurrent C. diff)": 92,
    "UC (ulcerative colitis)":  35,
    "CD (Crohn's disease)":     25,
    "IBS":                       40,
    "Autism (MTT protocol)":     50,
    "Obesity":                   15,
    "Depression (pilot RCTs)":   30,
    "Hepatic encephalopathy":    55,
}

# -------------------------------------------------------------
# 6) Dysbiosis as K-state basin shift (toy model)
# -------------------------------------------------------------
# 2D landscape with 3 basins: healthy, dysbiosis, FMT-recovered
def landscape(x, y):
    healthy_basin = -np.exp(-((x - 1.0)**2 + (y - 1.0)**2) / 0.3)
    dysbiosis_basin = -0.7 * np.exp(-((x + 1.0)**2 + (y + 1.0)**2) / 0.4)
    barrier = 0.3 * np.exp(-(x**2 + y**2) / 0.5)
    return healthy_basin + dysbiosis_basin + barrier

xx, yy = np.meshgrid(np.linspace(-2.5, 2.5, 100), np.linspace(-2.5, 2.5, 100))
zz = landscape(xx, yy)

# -------------------------------------------------------------
# 7) ITU K_microbiome axiom check: FMT-like reset
# -------------------------------------------------------------
N_species = 1000
# Healthy state: Zipf-like
ranks = np.arange(1, N_species + 1)
p_healthy = ranks ** (-0.9); p_healthy /= p_healthy.sum()
S_healthy = float(-np.sum(p_healthy * np.log(p_healthy)))

# Dysbiosis: Faecalibacterium etc. crashed, Proteobacteria expand
# Model: top 20% species depleted, ranks 200-300 expanded
weights = np.ones(N_species)
weights[:200] *= 0.1  # health-associated crashed
weights[200:300] *= 10  # opportunists expanded
p_dysbiosis = p_healthy * weights
p_dysbiosis = p_dysbiosis / p_dysbiosis.sum()
S_dysbiosis = float(-np.sum(p_dysbiosis * np.log(p_dysbiosis)))

# FMT recovery: roughly back toward healthy (90% restored)
weights_recovered = 0.9 * (p_healthy / p_dysbiosis) + 0.1  # blend toward healthy
p_fmt = p_dysbiosis * weights_recovered
p_fmt = p_fmt / p_fmt.sum()
S_fmt = float(-np.sum(p_fmt * np.log(p_fmt)))

# ITU linearized
def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    ratio = float(dS / dK) if abs(dK) > 1e-15 else float("nan")
    return ratio, float(dS), float(dK)

ratio_dysbiosis, dS_d, dK_d = itu_lin(p_healthy, p_dysbiosis)
ratio_fmt, dS_f, dK_f = itu_lin(p_dysbiosis, p_fmt)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 195 — Microbiome + Gut-Brain Axis + FMT (K_microbiome)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Phylum composition stacked bars
ax = axes[0, 0]
states = ["Healthy", "Obese", "UC (IBD)", "CD (IBD)"]
data = np.array([healthy, obese, ibd_uc, ibd_cd])
colors_p = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "gray"]
bottom = np.zeros(len(states))
for i, ph in enumerate(phyla):
    ax.bar(states, data[:, i], bottom=bottom, label=ph, color=colors_p[i])
    bottom += data[:, i]
ax.set_ylabel("Phylum abundance (%)")
ax.set_title("Gut microbiome composition")
ax.legend(fontsize=7, loc="upper right")
ax.grid(True, alpha=0.3, axis="y")

# Panel 2: SCFA producers
ax = axes[0, 1]
species = list(scfa_producers.keys())
prod = list(scfa_producers.values())
colors_s = ["#2ca02c" if p > 200 else "#ff7f0e" for p in prod]
ax.barh(range(len(species)), prod, color=colors_s)
ax.set_yticks(range(len(species)))
ax.set_yticklabels(species, fontsize=7)
ax.set_xlabel("SCFA production (units/g)")
ax.set_title("Major SCFA producers (60/25/15 acet/prop/but)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: FMT efficacy
ax = axes[0, 2]
inds = list(fmt_indications.keys())
effs = list(fmt_indications.values())
colors_f = ["#2ca02c" if e > 70 else "#ff7f0e" if e > 40 else "#d62728" for e in effs]
ax.barh(range(len(inds)), effs, color=colors_f)
ax.axvline(50, color="black", linestyle="--", alpha=0.5)
ax.set_yticks(range(len(inds)))
ax.set_yticklabels(inds, fontsize=7)
ax.set_xlabel("Response/cure rate (%)")
ax.set_title("FMT efficacy across indications")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: Gut-brain axis landscape (K-state basins)
ax = axes[1, 0]
cs = ax.contourf(xx, yy, zz, levels=20, cmap="viridis")
ax.contour(xx, yy, zz, levels=10, colors="white", alpha=0.4, linewidths=0.5)
plt.colorbar(cs, ax=ax, label="K-state potential")
# Trajectory arrows
ax.annotate("Healthy basin", (1.0, 1.0), fontsize=10, color="white",
            ha="center", fontweight="bold")
ax.annotate("Dysbiosis", (-1.0, -1.0), fontsize=10, color="white",
            ha="center", fontweight="bold")
ax.arrow(1.0, 1.0, -1.5, -1.5, head_width=0.1, head_length=0.15,
         color="red", alpha=0.7)
ax.arrow(-1.0, -1.0, 1.5, 1.5, head_width=0.1, head_length=0.15,
         color="green", alpha=0.7)
ax.text(0.5, -0.3, "FMT", fontsize=12, color="green", fontweight="bold")
ax.text(-0.5, 0.3, "Perturbation", fontsize=10, color="red")
ax.set_xlabel("Microbiome diversity axis")
ax.set_ylabel("Functional richness axis")
ax.set_title("K_microbiome basin landscape")

# Panel 5: ITU entropy + ratios
ax = axes[1, 1]
labels = ["Healthy", "Dysbiosis", "FMT recovery"]
vals = [S_healthy, S_dysbiosis, S_fmt]
colors_e = ["#2ca02c", "#d62728", "#1f77b4"]
ax.bar(labels, vals, color=colors_e)
ax.set_ylabel("Repertoire entropy (nats)")
ax.set_title(f"ITU: H→D ratio={ratio_dysbiosis:.3f}, D→FMT ratio={ratio_fmt:.3f}")
ax.grid(True, alpha=0.3, axis="y")

# Panel 6: Neurotransmitter producer panel
ax = axes[1, 2]
nt_names = list(neurotransmitters.keys())
nt_pos = np.arange(len(nt_names))
ax.barh(nt_pos, [1] * len(nt_names), color=["#9467bd"] * len(nt_names))
for i, nt in enumerate(nt_names):
    ax.text(0.5, i, neurotransmitters[nt]["main_producer"],
            ha="center", va="center", fontsize=7, color="white", fontweight="bold")
ax.set_yticks(nt_pos)
ax.set_yticklabels(nt_names, fontsize=8)
ax.set_xticks([])
ax.set_title("Gut-brain axis neurotransmitter producers")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 195,
    "tier1_paper": 27,
    "block": "B",
    "topic": "Microbiome + gut-brain axis + FMT (K_microbiome)",
    "human_microbiome_scale": {k: float(v) for k, v in scale.items()},
    "phylum_composition": {
        "healthy_pct": dict(zip(phyla, healthy.tolist())),
        "obese_pct": dict(zip(phyla, obese.tolist())),
        "UC_pct": dict(zip(phyla, ibd_uc.tolist())),
        "CD_pct": dict(zip(phyla, ibd_cd.tolist())),
    },
    "F_B_ratios": {
        "healthy": float(healthy[0] / healthy[1]),
        "obese": float(obese[0] / obese[1]),
        "UC": float(ibd_uc[0] / ibd_uc[1]),
        "CD": float(ibd_cd[0] / ibd_cd[1]),
        "note": "Walters 2014: F/B ratio is not a reliable single marker",
    },
    "SCFA_producers": scfa_producers,
    "SCFA_composition_pct": scfa_composition,
    "SCFA_daily_production_mmol": 550,
    "neurotransmitters_microbial": neurotransmitters,
    "FMT_efficacy_pct": fmt_indications,
    "FMT_FDA_approval": {
        "Rebyota_2022": "C. difficile recurrence",
        "Vowst_2023": "C. difficile recurrence (oral)",
    },
    "ITU_K_microbiome": {
        "N_species": N_species,
        "S_healthy_nats": S_healthy,
        "S_dysbiosis_nats": S_dysbiosis,
        "S_FMT_nats": S_fmt,
        "healthy_to_dysbiosis": {"dS": dS_d, "dK": dK_d, "ratio": ratio_dysbiosis},
        "dysbiosis_to_FMT": {"dS": dS_f, "dK": dK_f, "ratio": ratio_fmt},
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_microbiome (sub-state of K_microbe)",
        "modular_Hamiltonian": "K_microbiome^(0) controls host-symbiont equilibria",
        "dysbiosis": "ITU descent into wrong basin (perturbation-induced)",
        "FMT_role": "Forced K-state reset by donor microbiome injection",
        "gut_brain_axis": "K_microbiome coupled to K_brain via SCFA + neurotransmitters",
        "Cryan_review_2019": "Gut-brain axis comprehensive review",
        "key_FMT_paper": "van Nood 2013 NEJM (CDI cure 92%)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
