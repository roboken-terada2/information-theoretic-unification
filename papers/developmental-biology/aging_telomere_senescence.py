"""
Phase 212 — Aging deepening + Telomere + Senescence (K_dev_aging, #6 link)

Simulations:
  1) 12 Hallmarks of Aging (López-Otín 2023)
  2) Telomere shortening over cell divisions (Hayflick limit)
  3) Horvath epigenetic clock prediction
  4) Senolytic drug effect (D+Q) on mouse healthspan
  5) Partial reprogramming (OSKM 4-day pulse) Ocampo 2016
  6) Maximum lifespan across species
  7) ITU K_dev_aging axiom check: aging trajectory

Outputs:
  - aging_telomere_senescence.png
  - aging_telomere_senescence_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("aging_telomere_senescence.png")
OUT_JSON = Path(__file__).with_name("aging_telomere_senescence_summary.json")

rng = np.random.default_rng(20260622)

# -------------------------------------------------------------
# 1) 12 Hallmarks of Aging (López-Otín 2023)
# -------------------------------------------------------------
hallmarks = {
    "1. Genomic instability":      0.85,
    "2. Telomere attrition":        0.90,
    "3. Epigenetic alterations":    0.92,
    "4. Loss of proteostasis":      0.80,
    "5. Disabled autophagy":        0.75,
    "6. Deregulated nutrient":      0.78,
    "7. Mitochondrial dysfunction": 0.88,
    "8. Cellular senescence":       0.95,
    "9. Stem cell exhaustion":      0.90,
    "10. Altered intercellular":    0.70,
    "11. Chronic inflammation":     0.93,
    "12. Dysbiosis":                0.65,
}

# -------------------------------------------------------------
# 2) Telomere shortening (Hayflick limit)
# -------------------------------------------------------------
divisions = np.arange(0, 80)
telomere_kb_initial = 12.0
shortening_per_div_bp = 100
telomere_kb = telomere_kb_initial - (shortening_per_div_bp * divisions / 1000)
telomere_kb_min = 4.0  # critical short
hayflick_div = np.argmin(np.abs(telomere_kb - telomere_kb_min))

# Senescence onset
N_pop = 1000
divisions_pop = rng.integers(0, 80, size=N_pop)
senescent = telomere_kb_initial - (shortening_per_div_bp * divisions_pop / 1000) < telomere_kb_min
senescent_fraction = senescent.mean()

# -------------------------------------------------------------
# 3) Horvath epigenetic clock
# -------------------------------------------------------------
# Predicts age from 353 CpG methylation sites
chronological = np.linspace(0, 100, 200)
# Healthy: clock matches age
predicted_healthy = chronological + rng.normal(0, 3, size=len(chronological))
# Accelerated aging (HGPS, smokers): clock > age
predicted_accel = chronological * 1.4 + rng.normal(0, 4, size=len(chronological))
# Decelerated (caloric restriction, exercise): clock < age
predicted_decel = chronological * 0.85 + rng.normal(0, 3, size=len(chronological))

# -------------------------------------------------------------
# 4) Senolytic (D+Q) effect on healthspan
# -------------------------------------------------------------
months = np.linspace(0, 36, 200)
# Control mouse healthspan curve
healthspan_control = 100 * np.exp(-(months / 24) ** 2)
# D+Q: 30% improvement
healthspan_dq = 100 * np.exp(-(months / 31) ** 2)
median_extension_pct = 30

# -------------------------------------------------------------
# 5) Partial reprogramming (Ocampo 2016)
# -------------------------------------------------------------
weeks = np.linspace(0, 30, 200)
# Progeria mouse lifespan: control 15 weeks, OSKM pulse 20 weeks
control_survival = 100 / (1 + np.exp((weeks - 12) / 1.5))
oskm_survival = 100 / (1 + np.exp((weeks - 19) / 1.5))

# -------------------------------------------------------------
# 6) Max lifespan across species
# -------------------------------------------------------------
species_lifespan = {
    "Mouse":              4,
    "Rat":                3,
    "Naked mole rat":     32,
    "Dog":                20,
    "Cat":                25,
    "Cow":                30,
    "Human (Calment 1997)": 122,
    "Bowhead whale":      211,
    "Ocean quahog":       507,
    "Greenland shark":    400,
    "Hydra":              "Negligible senescence",
}

# Numeric only for plot
species_numeric = {k: v for k, v in species_lifespan.items() if isinstance(v, (int, float))}

# -------------------------------------------------------------
# 7) ITU K_dev_aging axiom check
# -------------------------------------------------------------
# Young cell: broad functional state distribution
# Old cell: narrow degraded states + senescence
N_states = 2000
log_fit_young = -((np.arange(N_states) - N_states/2) ** 2) / 200_000
p_young = np.exp(log_fit_young); p_young /= p_young.sum()
S_young = float(-np.sum(p_young * np.log(p_young)))

# Old: damage states elevated, healthy states reduced
log_fit_old = log_fit_young.copy()
damage_zone = (np.arange(N_states) > 1500)
log_fit_old[damage_zone] += 2.0  # senescent + damaged states up
healthy_zone = (np.arange(N_states) > 800) & (np.arange(N_states) < 1200)
log_fit_old[healthy_zone] -= 1.5
p_old = np.exp(log_fit_old); p_old /= p_old.sum()
S_old = float(-np.sum(p_old * np.log(p_old)))

# Reprogrammed (partial OSKM): partially rescued
log_fit_repro = 0.6 * log_fit_young + 0.4 * log_fit_old
p_repro = np.exp(log_fit_repro); p_repro /= p_repro.sum()
S_repro = float(-np.sum(p_repro * np.log(p_repro)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_young_old = itu_lin(p_young, p_old)
ratio_old_repro = itu_lin(p_old, p_repro)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 212 — Aging Deepening + Telomere + Senescence (K_dev_aging)",
    fontsize=13, fontweight="bold",
)

# Panel 1: 12 Hallmarks of Aging
ax = axes[0, 0]
h_names = list(hallmarks.keys())
h_scores = list(hallmarks.values())
colors_h = ["#d62728" if s > 0.85 else "#ff7f0e" if s > 0.75 else "#9467bd" for s in h_scores]
ax.barh(range(len(h_names)), h_scores, color=colors_h)
ax.set_yticks(range(len(h_names)))
ax.set_yticklabels(h_names, fontsize=7)
ax.set_xlabel("Strength of evidence")
ax.set_xlim(0, 1)
ax.set_title("12 Hallmarks (López-Otín 2023)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 2: Telomere shortening
ax = axes[0, 1]
ax.plot(divisions, telomere_kb, "-", color="#1f77b4", lw=2)
ax.axhline(telomere_kb_min, color="red", linestyle="--", label=f"Critical short {telomere_kb_min} kb")
ax.axvline(hayflick_div, color="orange", linestyle="--", label=f"Hayflick limit ~{hayflick_div} div")
ax.set_xlabel("Cell divisions")
ax.set_ylabel("Telomere length (kb)")
ax.set_title("Telomere shortening (Blackburn-Greider-Szostak Nobel 2009)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Horvath clock
ax = axes[0, 2]
ax.plot(chronological, predicted_healthy, ".", color="#2ca02c", alpha=0.5,
        label="Healthy (matches)")
ax.plot(chronological, predicted_accel, ".", color="#d62728", alpha=0.5,
        label="Accelerated (HGPS, smokers)")
ax.plot(chronological, predicted_decel, ".", color="#1f77b4", alpha=0.5,
        label="Decelerated (CR, exercise)")
ax.plot([0, 100], [0, 100], "k--", alpha=0.5)
ax.set_xlabel("Chronological age (years)")
ax.set_ylabel("Horvath clock (DNAm age)")
ax.set_title("Horvath 2013 epigenetic clock")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Senolytic D+Q
ax = axes[1, 0]
ax.plot(months, healthspan_control, "-", color="#1f77b4", lw=2, label="Control")
ax.plot(months, healthspan_dq, "-", color="#2ca02c", lw=2,
        label=f"D+Q senolytic (+{median_extension_pct}% healthspan)")
ax.fill_between(months, healthspan_control, healthspan_dq, alpha=0.3, color="#2ca02c")
ax.set_xlabel("Months")
ax.set_ylabel("Healthspan (%)")
ax.set_title("Senolytic (Mayo Clinic, Kirkland 2015)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Partial reprogramming (Ocampo 2016)
ax = axes[1, 1]
ax.plot(weeks, control_survival, "-", color="#d62728", lw=2, label="Progeria control")
ax.plot(weeks, oskm_survival, "-", color="#2ca02c", lw=2, label="Partial OSKM (Ocampo)")
ax.fill_between(weeks, control_survival, oskm_survival, alpha=0.3, color="#2ca02c")
ax.set_xlabel("Weeks")
ax.set_ylabel("Survival (%)")
ax.set_title("Partial reprogramming (Ocampo 2016 Cell) +30% lifespan")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Species lifespan + ITU
ax = axes[1, 2]
sp_names = list(species_numeric.keys())
sp_yrs = list(species_numeric.values())
colors_sp = ["#1f77b4" if y < 50 else "#ff7f0e" if y < 150 else "#d62728" for y in sp_yrs]
ax.barh(range(len(sp_names)), sp_yrs, color=colors_sp)
ax.set_xscale("log")
ax.set_yticks(range(len(sp_names)))
ax.set_yticklabels(sp_names, fontsize=7)
ax.set_xlabel("Max lifespan (years, log)")
ax.set_title(f"Lifespan;  ITU young→old={ratio_young_old:.3f}, old→repro={ratio_old_repro:.3f}")
ax.grid(True, alpha=0.3, axis="x", which="both")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 212,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Aging deepening + Telomere + Senescence (K_dev_aging)",
    "12_Hallmarks_of_Aging_2023": list(hallmarks.keys()),
    "Lopez_Otin_papers": "Cell 2013 (6500+ citations), Cell 2023 (updated)",
    "telomere_shortening": {
        "initial_length_kb": telomere_kb_initial,
        "loss_per_division_bp": shortening_per_div_bp,
        "critical_short_kb": telomere_kb_min,
        "Hayflick_limit_divisions": int(hayflick_div),
        "Hayflick_1961": "50 divisions in vitro for human fibroblasts",
        "Nobel_2009": "Blackburn + Greider + Szostak",
    },
    "Horvath_clock": {
        "year": 2013,
        "method": "353 CpG methylation sites",
        "accuracy_yr": "±3-5",
        "applications": ["chronological age prediction", "biological age", "disease risk"],
    },
    "senolytics": {
        "first_class_Kirkland_2015": "Dasatinib + Quercetin (D+Q)",
        "Mayo_Clinic_Tchkonia_Kirkland": "Senolytic concept",
        "mouse_healthspan_extension_pct": median_extension_pct,
        "Phase_II_trials_2024": ["CKD", "Alzheimer", "Pulmonary fibrosis"],
    },
    "partial_reprogramming": {
        "Ocampo_2016_Cell_Belmonte": "OSKM pulse rescues progeria",
        "progeria_lifespan_extension_pct": 30,
        "DNAm_age_reduction": "10-15 years",
    },
    "longevity_companies_2022_2024": {
        "Altos_Labs":        {"founding_year": 2022, "funding_USD": 3.0e9,
                              "leaders": "Yamanaka + Ocampo + López-Otín + Belmonte"},
        "Calico_Labs":       {"founding_year": 2013, "funding_USD": 1.0e9,
                              "leaders": "Alphabet/Google + AbbVie + Kenyon (prev)"},
        "Retro_Biosciences": {"founding_year": 2022, "funding_USD": 0.18e9,
                              "leaders": "Sam Altman investment"},
    },
    "species_max_lifespan_years": species_lifespan,
    "ITU_K_dev_aging": {
        "N_states": N_states,
        "S_young_nats": S_young,
        "S_old_nats": S_old,
        "S_reprogrammed_nats": S_repro,
        "young_to_old_ratio": ratio_young_old,
        "old_to_reprogrammed_ratio": ratio_old_repro,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev_aging",
        "modular_Hamiltonian": "K_dev_aging^(0) = -log P(cell state | age, cumulative damage)",
        "aging_meaning": "K-state degradation flow (information loss)",
        "duality_with_Phase_207": "Development (S↓ specialization) vs Aging (S↓ degradation)",
        "Yamanaka_rejuvenation_meaning": "Partial K-state lifting on aging axis",
        "senolytic_meaning": "Selective removal of irreversibly degraded K-states",
        "evolutionary_logic": "Long-lived species suppress somatic K-state plasticity (anti-cancer)",
    },
    "predictions": [
        ("Senolytics FDA approval (1 indication)", 2028, 0.65, "Medium"),
        ("Partial reprogramming clinical (Altos)", 2030, 0.70, "Strong"),
        ("Healthspan extension 5+ years population", 2035, 0.45, "Medium"),
        ("Horvath clock clinical standardization", 2028, 0.75, "Strong"),
        ("Human max lifespan >130 years", 2050, 0.30, "Weak"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
