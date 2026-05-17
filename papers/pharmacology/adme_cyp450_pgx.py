"""
Phase 230 — ADME + CYP450 + Pharmacogenomics (K_pharma_PK)

Simulations:
  1) 1-compartment vs 2-compartment PK
  2) CYP450 drug coverage
  3) Drug-drug interaction (DDI): grapefruit + statin
  4) PGx phenotypes (CYP2D6: PM/IM/EM/UM)
  5) HLA-B*5701 / abacavir hypersensitivity
  6) Personalized dosing example (warfarin VKORC1+CYP2C9)
  7) ITU K_pharma_PK axiom check

Outputs:
  - adme_cyp450_pgx.png
  - adme_cyp450_pgx_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("adme_cyp450_pgx.png")
OUT_JSON = Path(__file__).with_name("adme_cyp450_pgx_summary.json")

rng = np.random.default_rng(20260711)

# -------------------------------------------------------------
# 1) 1-compartment vs 2-compartment PK
# -------------------------------------------------------------
t = np.linspace(0, 24, 200)
# Oral dose, F=0.8, ka=2/hr, ke=0.1/hr
F = 0.8
dose = 100  # mg
ka = 2.0
ke = 0.1
Vd = 30   # L
# Bateman equation
C_1comp = (F * dose / Vd) * (ka / (ka - ke)) * (np.exp(-ke * t) - np.exp(-ka * t))

# 2-compartment
alpha = 1.0
beta = 0.08
A = 2.0
B = 1.0
C_2comp = A * np.exp(-alpha * t) + B * np.exp(-beta * t)

t_half_1 = np.log(2) / ke
Cmax_1 = float(np.max(C_1comp))
AUC_1 = float(np.trapz(C_1comp, t))

# -------------------------------------------------------------
# 2) CYP coverage
# -------------------------------------------------------------
cyp_coverage = {
    "CYP3A4":  50,
    "CYP2D6":  25,
    "CYP2C9":  15,
    "CYP2C19": 10,
    "CYP1A2":   5,
    "CYP2E1":   4,
    "CYP2B6":   3,
    "Other":    3,
}

# -------------------------------------------------------------
# 3) DDI: Grapefruit + Statin
# -------------------------------------------------------------
# Simvastatin AUC enhanced by grapefruit (CYP3A4 inhibition)
ddi_data = {
    "Simvastatin alone":          1.0,
    "+ Grapefruit (250 mL)":      3.0,
    "+ Itraconazole":             19.0,
    "+ Erythromycin":             6.0,
    "+ Rifampin (CYP3A induce)":  0.1,
}

# -------------------------------------------------------------
# 4) CYP2D6 phenotypes
# -------------------------------------------------------------
cyp2d6_phenotypes = {
    "Poor Metabolizer (PM)":         {"freq_pct": 7,  "metab_rate": 0.1},
    "Intermediate Metabolizer (IM)": {"freq_pct": 23, "metab_rate": 0.6},
    "Extensive Metabolizer (EM)":     {"freq_pct": 65, "metab_rate": 1.0},
    "Ultra-rapid Metabolizer (UM)":   {"freq_pct": 5,  "metab_rate": 2.5},
}

# -------------------------------------------------------------
# 5) HLA-B*5701 + abacavir hypersensitivity
# -------------------------------------------------------------
populations = ["Caucasian", "African", "Asian", "Hispanic"]
hla_b5701_freq = [6, 1, 0.5, 4]  # %

# -------------------------------------------------------------
# 6) Warfarin VKORC1+CYP2C9 dosing
# -------------------------------------------------------------
genotypes = ["VKORC1 GG\nCYP2C9 *1/*1", "VKORC1 GA\nCYP2C9 *1/*2",
              "VKORC1 GA\nCYP2C9 *1/*3", "VKORC1 AA\nCYP2C9 *2/*3"]
dose_mg_week = [49, 35, 25, 14]

# -------------------------------------------------------------
# 7) ITU K_pharma_PK axiom
# -------------------------------------------------------------
N_concentrations = 2000
# Pre-drug: baseline (low everywhere)
log_fit_pre = -2.0 * np.ones(N_concentrations) + 0.1 * rng.standard_normal(N_concentrations)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Normal metabolizer (EM): peaked at target concentration
log_fit_em = -((np.arange(N_concentrations) - 1000) ** 2) / 30000
p_em = np.exp(log_fit_em); p_em /= p_em.sum()
S_em = float(-np.sum(p_em * np.log(p_em)))

# Poor metabolizer: peaked at high concentration (drug accumulates)
log_fit_pm = -((np.arange(N_concentrations) - 1700) ** 2) / 50000
p_pm = np.exp(log_fit_pm); p_pm /= p_pm.sum()
S_pm = float(-np.sum(p_pm * np.log(p_pm)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_em = itu_lin(p_pre, p_em)
ratio_em_pm = itu_lin(p_em, p_pm)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 230 — ADME + CYP450 + Pharmacogenomics (K_pharma_PK)",
    fontsize=13, fontweight="bold",
)

# Panel 1: PK curves
ax = axes[0, 0]
ax.plot(t, C_1comp, "-", color="#1f77b4", lw=2,
        label=f"1-compartment (t½={t_half_1:.1f}h)")
ax.plot(t, C_2comp, "-", color="#d62728", lw=2, label="2-compartment")
ax.set_xlabel("Time (hr)")
ax.set_ylabel("Concentration (mg/L)")
ax.set_title(f"Oral PK: Cmax={Cmax_1:.2f}, AUC={AUC_1:.1f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: CYP coverage
ax = axes[0, 1]
cyp_names = list(cyp_coverage.keys())
cyp_pcts = list(cyp_coverage.values())
colors_c = ["#d62728" if p > 30 else "#ff7f0e" if p > 10 else "#1f77b4" for p in cyp_pcts]
ax.bar(cyp_names, cyp_pcts, color=colors_c)
ax.set_ylabel("% of drugs metabolized")
ax.set_title("CYP450 drug coverage")
ax.tick_params(axis="x", rotation=20, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: DDI grapefruit
ax = axes[0, 2]
ddi_names = list(ddi_data.keys())
ddi_aucs = list(ddi_data.values())
colors_d = ["#2ca02c" if a < 0.5 else "#1f77b4" if a < 2 else "#d62728" for a in ddi_aucs]
ax.barh(range(len(ddi_names)), ddi_aucs, color=colors_d)
ax.set_yticks(range(len(ddi_names))); ax.set_yticklabels(ddi_names, fontsize=8)
ax.set_xscale("log")
ax.set_xlabel("Simvastatin AUC fold change (log)")
ax.set_title("CYP3A4 DDI")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: CYP2D6 phenotypes
ax = axes[1, 0]
p_names = list(cyp2d6_phenotypes.keys())
freqs = [cyp2d6_phenotypes[p]["freq_pct"] for p in p_names]
rates = [cyp2d6_phenotypes[p]["metab_rate"] for p in p_names]
x = np.arange(len(p_names))
width = 0.35
ax.bar(x - width/2, freqs, width, color="#1f77b4", label="Frequency %")
ax2 = ax.twinx()
ax2.bar(x + width/2, rates, width, color="#d62728", label="Metab rate")
ax.set_xticks(x); ax.set_xticklabels(p_names, rotation=15, fontsize=7)
ax.set_ylabel("Frequency (%)", color="#1f77b4")
ax2.set_ylabel("Relative metab rate", color="#d62728")
ax.set_title("CYP2D6 phenotypes (Caucasian)")
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: HLA-B*5701 frequencies
ax = axes[1, 1]
colors_h = ["#d62728" if f > 5 else "#ff7f0e" if f > 1 else "#2ca02c" for f in hla_b5701_freq]
ax.bar(populations, hla_b5701_freq, color=colors_h)
ax.set_ylabel("HLA-B*5701 frequency (%)")
ax.set_title("HLA-B*5701 / Abacavir hypersensitivity")
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(hla_b5701_freq):
    ax.text(i, v + 0.2, f"{v}%", ha="center", fontsize=10, fontweight="bold")

# Panel 6: ITU K_pharma_PK
ax = axes[1, 2]
ax.bar(["Pre-drug\n(baseline)", "Normal (EM)\n(target conc)", "Poor metab (PM)\n(accumulated)"],
       [S_pre, S_em, S_pm], color=["#1f77b4", "#2ca02c", "#d62728"])
ax.set_ylabel("Concentration distribution entropy (nats)")
ax.set_title(f"K_pharma_PK: Pre→EM={ratio_pre_em:.3f}, EM→PM={ratio_em_pm:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 230,
    "tier1_paper": 32,
    "topic": "ADME + CYP450 + Pharmacogenomics (K_pharma_PK)",
    "PK_parameters": {
        "F_bioavailability": F,
        "Ka": ka, "Ke": ke, "Vd_L": Vd,
        "t_half_hr": float(t_half_1),
        "Cmax": Cmax_1,
        "AUC": AUC_1,
    },
    "CYP_drug_coverage": cyp_coverage,
    "CYP3A4_pct_of_all_drugs": 50,
    "DDI_grapefruit_simvastatin": ddi_data,
    "CYP2D6_phenotypes": cyp2d6_phenotypes,
    "HLA_B5701_population_freq_pct": dict(zip(populations, hla_b5701_freq)),
    "CPIC_gene_drug_pairs": 100,
    "PGx_examples": {
        "CYP2C19_clopidogrel": "PM = no activation, increased CV events",
        "TPMT_thiopurine": "PM = severe myelosuppression",
        "HLA_B5701_abacavir": "Carrier = severe hypersensitivity",
        "HLA_B1502_carbamazepine": "Asian carrier = SJS/TEN risk",
        "DPYD_5FU": "Variant = severe toxicity",
    },
    "warfarin_dosing_mg_per_week": dict(zip(genotypes, dose_mg_week)),
    "annual_US_ADR_deaths": 100000,
    "PGx_potential_reduction_pct": 30,
    "ITU_K_pharma_PK": {
        "N_concentrations": N_concentrations,
        "S_pre_drug_nats": S_pre,
        "S_EM_normal_nats": S_em,
        "S_PM_accumulated_nats": S_pm,
        "pre_to_EM_ratio": ratio_pre_em,
        "EM_to_PM_ratio": ratio_em_pm,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_PK",
        "modular_Hamiltonian": "K_pharma_PK^(0) = -log P(drug conc | genome, dose, time)",
        "PGx_meaning": "Personalized dosing via K_genome (CYP, HLA, VKORC1)",
        "DDI_meaning": "K-state interference: one drug modulates another's K_pharma_PK",
        "CYP3A4_central": "50% drugs share single metabolic K-state operator",
    },
    "predictions": [
        ("All hospitals PGx routine testing", 2030, 0.70, "Strong"),
        ("Annual ADR deaths 50% reduction", 2032, 0.65, "Medium"),
        ("All 1B humans genotyped", 2035, 0.55, "Medium"),
        ("PGx algorithms for 50+ drugs", 2028, 0.80, "Strong"),
        ("Universal newborn PGx panel", 2030, 0.75, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
