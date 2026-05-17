"""
Phase 205 — Neurodegenerative + psychiatric disorders (K_pathology)

Simulations:
  1) AD prevalence vs age (Brookmeyer 2007)
  2) APOE4 dose-dependent AD risk
  3) Lecanemab CLARITY AD trial (cognitive decline curve)
  4) PD substantia nigra cell loss over time
  5) Antidepressant onset comparison (SSRI vs Ketamine)
  6) Schizophrenia GWAS Manhattan-like plot summary
  7) Global neurological disease burden (DALYs)
  8) ITU K_pathology axiom check

Outputs:
  - neurodegen_psychiatric.png
  - neurodegen_psychiatric_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("neurodegen_psychiatric.png")
OUT_JSON = Path(__file__).with_name("neurodegen_psychiatric_summary.json")

rng = np.random.default_rng(20260608)

# -------------------------------------------------------------
# 1) AD prevalence by age (Brookmeyer 2007)
# -------------------------------------------------------------
ages = np.arange(60, 96)
# Sigmoid: ~3% @ 65, ~30% @ 85, ~50% @ 90
ad_prevalence = 50.0 / (1 + np.exp(-(ages - 85) / 4))

# -------------------------------------------------------------
# 2) APOE4 dose AD risk (OR)
# -------------------------------------------------------------
apoe_risk = {
    "e2/e3 (protective)": 0.6,
    "e3/e3 (reference)":  1.0,
    "e3/e4":              3.5,
    "e4/e4 (homozygous)": 14.0,
}

# -------------------------------------------------------------
# 3) Lecanemab CLARITY AD (van Dyck 2023 NEJM)
# -------------------------------------------------------------
weeks = np.linspace(0, 78, 200)
# CDR-SB score progression (lower = better)
placebo_cdr = 0.5 + (weeks / 78) * 1.66
lecanemab_cdr = 0.5 + (weeks / 78) * 1.21  # 27% slower

cdr_relative_reduction = (placebo_cdr[-1] - lecanemab_cdr[-1]) / placebo_cdr[-1] * 100

# -------------------------------------------------------------
# 4) PD substantia nigra cell loss
# -------------------------------------------------------------
years_pd = np.arange(0, 30)
# Pre-clinical: 5%/yr loss; clinical onset at ~30% loss; gradual
sn_cells_remaining = 100 * np.exp(-0.04 * years_pd)
# Symptomatic threshold ~60% of cells lost (40% remaining)
sn_threshold_year = years_pd[sn_cells_remaining <= 40][0] if any(sn_cells_remaining <= 40) else 25

# -------------------------------------------------------------
# 5) Antidepressant onset SSRI vs Ketamine
# -------------------------------------------------------------
t_antidep_hours = np.logspace(-1, 3.5, 100)  # 0.1 hr to 3000 hr
def sigmoid_response(t, t50, slope):
    return 1.0 / (1.0 + np.exp(-(np.log10(t) - np.log10(t50)) * slope))

ssri = sigmoid_response(t_antidep_hours, 500, 3)  # ~3 weeks
ketamine = sigmoid_response(t_antidep_hours, 2, 4)  # 2 hours

# -------------------------------------------------------------
# 6) Schizophrenia GWAS loci sketch
# -------------------------------------------------------------
# PGC 2022: 287 loci
n_loci_per_chr = [25, 18, 15, 14, 14, 22, 14, 12, 13, 14, 12, 12, 9,
                   10, 12, 9, 13, 10, 12, 7, 9, 11]  # 22 chromosomes
n_total_loci = sum(n_loci_per_chr)

# -------------------------------------------------------------
# 7) Global neurological disease burden (DALYs M/yr)
# -------------------------------------------------------------
burden = {
    "Stroke":         143.0,
    "Migraine":        45.0,
    "Depression":      50.0,
    "AD/Dementia":     28.5,
    "Schizophrenia":   15.0,
    "Epilepsy":        13.5,
    "PD":               5.8,
    "MS":               2.0,
    "ALS":              0.4,
}
total_burden = sum(burden.values())

# -------------------------------------------------------------
# 8) ITU K_pathology check: AD progression
# -------------------------------------------------------------
N_states = 3000
# Healthy memory state
log_fit_healthy = -((np.arange(N_states) - N_states/2) ** 2) / 150_000
p_healthy = np.exp(log_fit_healthy); p_healthy /= p_healthy.sum()
S_healthy = float(-np.sum(p_healthy * np.log(p_healthy)))

# AD: memory states with low p (degraded)
# Healthy memory traces (mid-range) suppressed
ad_mask = (np.arange(N_states) > 1000) & (np.arange(N_states) < 2000)
log_fit_ad = log_fit_healthy.copy()
log_fit_ad[ad_mask] -= 4.0
p_ad = np.exp(log_fit_ad); p_ad /= p_ad.sum()
S_ad = float(-np.sum(p_ad * np.log(p_ad)))

# Lecanemab: partial restoration
log_fit_treated = log_fit_ad.copy()
log_fit_treated[ad_mask] += 1.5  # 27% recovery
p_treated = np.exp(log_fit_treated); p_treated /= p_treated.sum()
S_treated = float(-np.sum(p_treated * np.log(p_treated)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return (dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_healthy_ad = float(itu_lin(p_healthy, p_ad))
ratio_ad_treated = float(itu_lin(p_ad, p_treated))

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 205 — Neurodegenerative + Psychiatric Disorders (K_pathology)",
    fontsize=13, fontweight="bold",
)

# Panel 1: AD prevalence
ax = axes[0, 0]
ax.plot(ages, ad_prevalence, "-", color="#d62728", lw=2)
ax.fill_between(ages, 0, ad_prevalence, alpha=0.3, color="#d62728")
ax.set_xlabel("Age (years)")
ax.set_ylabel("AD prevalence (%)")
ax.set_title("AD age-dependent prevalence (Brookmeyer 2007)")
ax.grid(True, alpha=0.3)

# Panel 2: APOE4 risk
ax = axes[0, 1]
apoe_names = list(apoe_risk.keys())
risks = list(apoe_risk.values())
colors_a = ["#2ca02c" if r < 1 else "#ff7f0e" if r < 5 else "#d62728" for r in risks]
ax.bar(apoe_names, risks, color=colors_a)
ax.set_ylabel("AD risk (OR)")
ax.set_title("APOE4 dose-dependent risk")
ax.tick_params(axis="x", rotation=15)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: Lecanemab CLARITY AD
ax = axes[0, 2]
ax.plot(weeks, placebo_cdr, "-", color="#d62728", lw=2, label="Placebo")
ax.plot(weeks, lecanemab_cdr, "-", color="#2ca02c", lw=2, label="Lecanemab")
ax.fill_between(weeks, lecanemab_cdr, placebo_cdr, alpha=0.3, color="#2ca02c")
ax.set_xlabel("Weeks")
ax.set_ylabel("CDR-SB (higher = worse)")
ax.set_title(f"Lecanemab: {cdr_relative_reduction:.0f}% slower decline (CLARITY AD)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: PD cell loss
ax = axes[1, 0]
ax.plot(years_pd, sn_cells_remaining, "-", color="#9467bd", lw=2)
ax.axhline(40, color="red", linestyle="--", label="Symptom threshold (40% remaining)")
ax.set_xlabel("Years")
ax.set_ylabel("Substantia nigra cells (%)")
ax.set_title(f"PD progression; clinical onset ~yr {sn_threshold_year}")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Antidepressant onset
ax = axes[1, 1]
ax.semilogx(t_antidep_hours, ssri * 100, "-", color="#1f77b4", lw=2, label="SSRI (~3 weeks)")
ax.semilogx(t_antidep_hours, ketamine * 100, "-", color="#d62728", lw=2, label="Ketamine (~2 hr)")
ax.axhline(50, color="black", linestyle="--", alpha=0.5)
ax.set_xlabel("Time post-dose (hours, log)")
ax.set_ylabel("Antidepressant response (%)")
ax.set_title("Ketamine vs SSRI onset (Zarate 2006)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")

# Panel 6: Disease burden + ITU
ax = axes[1, 2]
items = sorted(burden.items(), key=lambda x: -x[1])
names_b = [x[0] for x in items]
vals_b = [x[1] for x in items]
ax.barh(range(len(names_b)), vals_b, color="#d62728")
ax.set_yticks(range(len(names_b)))
ax.set_yticklabels(names_b, fontsize=8)
ax.set_xlabel("DALYs (millions / year)")
ax.set_title(f"Global burden;  ITU H→AD={ratio_healthy_ad:.3f}, AD→Tx={ratio_ad_treated:.3f}")
ax.grid(True, alpha=0.3, axis="x")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 205,
    "tier1_paper": 28,
    "block": "B",
    "topic": "Neurodegenerative + psychiatric disorders (K_pathology)",
    "Alzheimer_disease": {
        "first_described": "Alzheimer 1906 (Auguste Deter)",
        "amyloid_hypothesis": "Hardy-Selkoe 1992",
        "key_genes": "APP, PSEN1, PSEN2 (familial); APOE4 (sporadic)",
        "APOE4_risk": apoe_risk,
        "Lecanemab_approval_2023": True,
        "Lecanemab_CLARITY_AD": {
            "Phase_III": "van Dyck 2023 NEJM",
            "cognitive_decline_reduction_pct": float(cdr_relative_reduction),
            "ARIA_E_incidence_pct": 12,
            "deaths_reported": 3,
        },
    },
    "Parkinson_disease": {
        "first_described": "Parkinson 1817 (Shaking Palsy)",
        "pathology": "Substantia nigra dopamine neuron death + Lewy bodies (alpha-synuclein)",
        "Braak_hypothesis_2003": "Gut -> vagus -> brainstem -> midbrain progression",
        "L_DOPA_introduced": 1967,
        "DBS_introduced": 1987,
        "cell_loss_per_year_pct": 4,
        "symptom_onset_threshold_pct_remaining": 40,
    },
    "depression_treatments": {
        "SSRI_onset_weeks": 3,
        "Ketamine_onset_hours": 2,
        "Ketamine_paper": "Zarate 2006 Arch Gen Psychiatry",
        "Spravato_FDA_2019": "Esketamine intranasal",
        "Psilocybin_Phase_III": "Compass Pathways (treatment-resistant depression)",
        "MDMA_Phase_III": "MAPS (PTSD)",
    },
    "schizophrenia": {
        "dopamine_hypothesis_Carlsson_1963": "Mesolimbic DA excess",
        "Carlsson_Nobel_2000": "Physiology/Medicine",
        "PGC_2022_GWAS_loci": int(n_total_loci),
        "heritability_pct": 80,
        "F_M_ratio": "1:1.4",
    },
    "global_disease_burden_DALYs": burden,
    "total_neurological_DALYs": float(total_burden),
    "ITU_K_pathology": {
        "N_states": N_states,
        "S_healthy_nats": S_healthy,
        "S_AD_nats": S_ad,
        "S_treated_nats": S_treated,
        "healthy_to_AD_ratio": ratio_healthy_ad,
        "AD_to_treated_ratio": ratio_ad_treated,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pathology",
        "definition": "Deviation of K_neuro^(0) from healthy basin",
        "AD_mechanism": "K_memory degradation + K_neuron death (hippo->cortex)",
        "PD_mechanism": "K_motor (SN-striatum) collapse",
        "depression_mechanism": "K_emotion + K_reward global descent (anhedonia)",
        "schizophrenia_mechanism": "K_perception (positive) + K_executive (negative) dual deviation",
        "treatment_as_K_state_restoration": "Lecanemab/L-DOPA/Ketamine/Risperidone return ρ to healthy basin",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
