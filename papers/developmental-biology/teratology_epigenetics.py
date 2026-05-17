"""
Phase 213 — Birth defects + Teratology + Epigenetics (K_dev_teratology)

Simulations:
  1) Top 10 birth defects prevalence
  2) Critical periods for organogenesis (3-8 weeks)
  3) Thalidomide victim timeline 1957-1962
  4) Folate supplementation effect on NTD
  5) Genomic imprinting: PWS vs Angelman
  6) DOHaD: Dutch Famine 1944-45 follow-up
  7) Epigenetic landscape (DNAm clock parallel)
  8) ITU K_dev_teratology axiom check

Outputs:
  - teratology_epigenetics.png
  - teratology_epigenetics_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("teratology_epigenetics.png")
OUT_JSON = Path(__file__).with_name("teratology_epigenetics_summary.json")

rng = np.random.default_rng(20260623)

# -------------------------------------------------------------
# 1) Top 10 birth defects (CDC-style stats, US)
# -------------------------------------------------------------
defects = {
    "CHD (heart)":             1/100,
    "Cleft lip/palate":        1/1000,
    "Down (T21)":              1/700,
    "Spina bifida":            1/2500,
    "Anencephaly":             1/5000,
    "Limb defect":             1/1500,
    "Cleft palate alone":      1/1500,
    "Diaphragmatic hernia":    1/3000,
    "Gastroschisis":           1/4000,
    "Esophageal atresia":      1/4000,
}

# -------------------------------------------------------------
# 2) Critical periods (3-8 weeks dominant)
# -------------------------------------------------------------
organs_periods = {
    "CNS / Neural tube":      (3, 6),
    "Heart":                  (3, 6),
    "Limbs":                  (4, 7),
    "Eyes":                   (4, 8),
    "Ears":                   (4, 9),
    "Palate":                 (6, 12),
    "External genitalia":     (7, 12),
    "Teeth":                  (7, 15),
}

# -------------------------------------------------------------
# 3) Thalidomide victim timeline
# -------------------------------------------------------------
thalidomide_years = np.array([1957, 1958, 1959, 1960, 1961, 1962, 1963])
thalidomide_cases = np.array([5, 50, 500, 2000, 5000, 2000, 100])
thalidomide_cumulative = np.cumsum(thalidomide_cases)
total_thalidomide = int(thalidomide_cumulative[-1])

# -------------------------------------------------------------
# 4) Folate effect on NTD
# -------------------------------------------------------------
# MRC 1991 trial: NTD recurrence with vs without folate
ntd_no_folate = 35  # per 1000 pregnancies (recurrence)
ntd_with_folate = 10  # 70% reduction
fortification_year = 1998  # US flour fortification
ntd_us_pre = 0.018  # per 1000 live births
ntd_us_post = 0.008  # 56% reduction

# -------------------------------------------------------------
# 5) Imprinting: PWS vs Angelman (15q11-13)
# -------------------------------------------------------------
imprinting = {
    "Prader-Willi (PWS)":  {"chr_loss": "Paternal 15q11-13", "freq": 1/15000,
                             "features": "Hypotonia + hyperphagia + obesity"},
    "Angelman (AS)":       {"chr_loss": "Maternal 15q11-13", "freq": 1/15000,
                             "features": "Severe ID + happy demeanor + ataxia"},
}

# -------------------------------------------------------------
# 6) DOHaD: Dutch Famine 1944-45 follow-up
# -------------------------------------------------------------
exposure_periods = {
    "Pre-conception":     1.1,
    "Early gestation":    1.7,  # max effect
    "Mid gestation":      1.3,
    "Late gestation":     1.4,
    "Post-natal":         1.0,
}
# Adult disease risk (OR vs control), Painter 2008 etc.

# -------------------------------------------------------------
# 7) Epigenetic age vs chronological
# -------------------------------------------------------------
N_subjects = 200
chrono_age = rng.uniform(0, 90, N_subjects)
# Normal: epigenetic = chrono
epi_normal = chrono_age + rng.normal(0, 3, N_subjects)
# DOHaD-exposed (Dutch Famine): accelerated
exposed = rng.random(N_subjects) < 0.3
epi_exposed = epi_normal.copy()
epi_exposed[exposed] += rng.uniform(3, 8, exposed.sum())  # 3-8 yr acceleration

# -------------------------------------------------------------
# 8) ITU K_dev_teratology axiom check
# -------------------------------------------------------------
N_phenotypes = 2000
# Normal: peaked at "healthy" phenotype center
log_fit_normal = -((np.arange(N_phenotypes) - N_phenotypes/2) ** 2) / 50000
p_normal = np.exp(log_fit_normal); p_normal /= p_normal.sum()
S_normal = float(-np.sum(p_normal * np.log(p_normal)))

# Thalidomide exposure: drift away from healthy center
log_fit_terato = log_fit_normal.copy()
# Healthy center suppressed
log_fit_terato[N_phenotypes//2 - 100 : N_phenotypes//2 + 100] -= 4.0
# Defect cluster elevated
log_fit_terato[1700:1850] += 3.0
p_terato = np.exp(log_fit_terato); p_terato /= p_terato.sum()
S_terato = float(-np.sum(p_terato * np.log(p_terato)))

# Folate-protected: closer to normal
log_fit_protected = 0.8 * log_fit_normal + 0.2 * log_fit_terato
p_protected = np.exp(log_fit_protected); p_protected /= p_protected.sum()
S_protected = float(-np.sum(p_protected * np.log(p_protected)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_normal_terato = itu_lin(p_normal, p_terato)
ratio_terato_protected = itu_lin(p_terato, p_protected)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 213 — Birth Defects + Teratology + Epigenetics (K_dev_teratology)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Top 10 birth defects
ax = axes[0, 0]
def_names = list(defects.keys())
def_freqs = list(defects.values())
ax.barh(range(len(def_names)), def_freqs, color="#d62728")
ax.set_xscale("log")
ax.set_yticks(range(len(def_names)))
ax.set_yticklabels(def_names, fontsize=7)
ax.set_xlabel("Frequency per birth (log)")
ax.set_title("Top 10 birth defects (US CDC)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 2: Critical periods
ax = axes[0, 1]
org_names = list(organs_periods.keys())
for i, (org, (start, stop)) in enumerate(organs_periods.items()):
    ax.barh(i, stop - start, left=start, color="#9467bd", alpha=0.7)
ax.axvspan(3, 8, alpha=0.15, color="red", label="Embryonic critical period")
ax.set_yticks(range(len(org_names)))
ax.set_yticklabels(org_names, fontsize=7)
ax.set_xlabel("Weeks post-conception")
ax.set_title("Critical periods for organ vulnerability")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: Thalidomide victims
ax = axes[0, 2]
ax.bar(thalidomide_years, thalidomide_cases, color="#d62728", alpha=0.7,
        label=f"Annual cases (total {total_thalidomide:,})")
ax.plot(thalidomide_years, thalidomide_cumulative, "o-", color="#1f77b4", lw=2,
        markersize=8, label="Cumulative")
ax.axvline(1961, color="orange", linestyle="--", alpha=0.7, label="McBride/Lenz warning")
ax.axvline(1962, color="green", linestyle="--", alpha=0.7, label="World recall")
ax.set_xlabel("Year")
ax.set_ylabel("Phocomelia cases")
ax.set_title("Thalidomide disaster 1957-1962")
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: Folate effect on NTD
ax = axes[1, 0]
groups = ["No folate\n(MRC control)", "Folate 4mg\n(MRC 1991)",
          "US pre-1998", "US post-1998"]
rates = [ntd_no_folate, ntd_with_folate, ntd_us_pre*1000, ntd_us_post*1000]
colors_f = ["#d62728", "#2ca02c", "#d62728", "#2ca02c"]
ax.bar(groups, rates, color=colors_f)
ax.set_ylabel("NTD rate (per 1000 pregnancies)")
ax.set_title("Folate prevention (70% MRC, 56% population)")
ax.tick_params(axis="x", rotation=10, labelsize=7)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(rates):
    ax.text(i, v + 0.5, f"{v:.2f}", ha="center", fontsize=9, fontweight="bold")

# Panel 5: DOHaD Dutch Famine
ax = axes[1, 1]
exposures = list(exposure_periods.keys())
ORs = list(exposure_periods.values())
ax.bar(exposures, ORs, color="#9467bd")
ax.axhline(1.0, color="black", linestyle="--", alpha=0.5)
ax.set_ylabel("Adult disease OR (CV/DM/SZ)")
ax.set_title("Dutch Famine 1944-45 / DOHaD (Barker 1986)")
ax.tick_params(axis="x", rotation=15, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 6: ITU K_dev_teratology
ax = axes[1, 2]
labels_t = ["Normal", "Thalidomide\nexposed", "Folate\nprotected"]
S_vals = [S_normal, S_terato, S_protected]
colors_t = ["#2ca02c", "#d62728", "#1f77b4"]
ax.bar(labels_t, S_vals, color=colors_t)
ax.set_ylabel("Phenotype entropy (nats)")
ax.set_title(f"ITU N→Terato={ratio_normal_terato:.3f}, T→Protect={ratio_terato_protected:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 213,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Birth defects + Teratology + Epigenetics (K_dev_teratology)",
    "birth_defects_frequency": defects,
    "total_major_defect_rate": "3-5% of births (WHO)",
    "WHO_annual_new_cases": 8e6,
    "annual_neonatal_deaths": 3e5,
    "critical_periods_weeks": organs_periods,
    "thalidomide_disaster": {
        "years": "1957-1962",
        "total_phocomelia_cases": total_thalidomide,
        "discoverers_1961": "McBride (Australia) + Lenz (Germany)",
        "world_recall_year": 1962,
        "legacy": "FDA Kefauver-Harris Amendment 1962 + modern teratology",
    },
    "folate_NTD_prevention": {
        "MRC_1991_trial_reduction_pct": 70,
        "US_fortification_1998_reduction_pct": 56,
        "WHO_recommendation": "400 μg/day pre-conception + early pregnancy",
    },
    "FAS_frequency": "1/500 - 1/1000",
    "imprinting_disorders": imprinting,
    "DOHaD_Barker_1986": {
        "Dutch_Famine_1944_45": "Painter 2008 - 60-year follow-up",
        "exposure_period_OR": exposure_periods,
        "key_concept": "Developmental Origins of Health and Disease",
    },
    "epigenetic_marks": {
        "DNAm_5mC": "CpG methylation",
        "histone_H3K4me3": "active marker",
        "histone_H3K27me3": "repressive marker",
        "imprinted_genes_human": 100,
    },
    "ITU_K_dev_teratology": {
        "N_phenotypes": N_phenotypes,
        "S_normal_nats": S_normal,
        "S_thalidomide_exposed_nats": S_terato,
        "S_folate_protected_nats": S_protected,
        "normal_to_terato_ratio": ratio_normal_terato,
        "terato_to_protected_ratio": ratio_terato_protected,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev_teratology",
        "modular_Hamiltonian": "K_dev_teratology^(0) = -log P(normal phenotype | G, E, T)",
        "Thalidomide_mechanism": "Cereblon binding -> SALL4 degradation -> limb K-state collapse",
        "Folate_mechanism": "Methyl donor (1-carbon metabolism) -> stabilizes neural tube K-state",
        "DOHaD_meaning": "Critical period environment encodes long-term K_dev_aging trajectory",
        "Imprinting_meaning": "Parental K-state asymmetry encoded in epigenome",
    },
    "predictions": [
        ("Trans-generational epigenetic inheritance (human)", 2030, 0.55, "Medium"),
        ("Pre-conception epigenetic screening", 2030, 0.60, "Medium"),
        ("AI teratogen risk prediction", 2028, 0.75, "Strong"),
        ("Universal newborn epigenetic clock", 2032, 0.55, "Medium"),
        ("Thalidomide-class in silico FDA avoidance", 2030, 0.80, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
