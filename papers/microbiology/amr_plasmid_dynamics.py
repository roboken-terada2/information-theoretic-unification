"""
Phase 194 — Antibiotic resistance + plasmid + AMR mechanisms (K_resistance)

Simulations:
  1) Antibiotic discovery timeline 1940-2024 (golden age decline)
  2) Resistance mechanism classification (4 categories)
  3) Plasmid Inc-groups + carried resistance genes
  4) Conjugation kinetics (Lederberg 1946) — population spread
  5) ESKAPE pathogen MDR profile
  6) Selection-resistance emergence dynamics
  7) NDM-1 global spread timeline 2008-2024
  8) ITU K_resistance axiom check

Outputs:
  - amr_plasmid_dynamics.png
  - amr_plasmid_dynamics_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("amr_plasmid_dynamics.png")
OUT_JSON = Path(__file__).with_name("amr_plasmid_dynamics_summary.json")

rng = np.random.default_rng(20260528)

# -------------------------------------------------------------
# 1) Antibiotic discovery timeline
# -------------------------------------------------------------
# Approvals per decade
decades = np.array([1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
new_classes = np.array([5, 11, 13, 6, 3, 2, 0, 2, 1])  # rough new-class counts

# -------------------------------------------------------------
# 2) Resistance mechanism distribution
# -------------------------------------------------------------
mechanisms = {
    "Drug degradation (β-lactamase)": 35,
    "Drug modification (AAC/APH/ANT)": 18,
    "Target alteration (PBP2a, VanA)": 25,
    "Efflux pumps + porin loss": 22,
}

# -------------------------------------------------------------
# 3) Plasmid Inc-groups
# -------------------------------------------------------------
inc_groups = {
    "IncF (CTX-M-15 ESBL)": {"global_prevalence_pct": 40, "host_range": "Enterobacteriaceae"},
    "IncH (NDM, KPC)": {"global_prevalence_pct": 20, "host_range": "Broad gram-neg"},
    "IncN (KPC)": {"global_prevalence_pct": 10, "host_range": "Enterobacteriaceae"},
    "IncP (multi-resistance)": {"global_prevalence_pct": 8, "host_range": "Very broad"},
    "ColE1 (mobilizable)": {"global_prevalence_pct": 22, "host_range": "Gram-neg"},
}

# -------------------------------------------------------------
# 4) Conjugation kinetics
# -------------------------------------------------------------
# Population: N0 donors, M0 recipients
# dD/dt = mu*D*(1-N/K), dR/dt = mu*R*(1-N/K), dT/dt = c*D*R/N
hours = np.linspace(0, 24, 400)
mu = 0.7  # doubling per hr
N0_d = 1e6  # donors
N0_r = 1e8  # recipients
c_conj = 3e-9  # transconjugant rate constant
K_cap = 1e10

D = np.zeros_like(hours)
R = np.zeros_like(hours)
T_pop = np.zeros_like(hours)
D[0] = N0_d
R[0] = N0_r
dt = hours[1] - hours[0]
for i in range(1, len(hours)):
    N_tot = D[i-1] + R[i-1] + T_pop[i-1]
    growth_factor = 1 - N_tot / K_cap
    transfers = c_conj * D[i-1] * R[i-1] * dt
    D[i] = D[i-1] + mu * D[i-1] * growth_factor * dt
    R[i] = R[i-1] + mu * R[i-1] * growth_factor * dt - transfers
    T_pop[i] = T_pop[i-1] + mu * T_pop[i-1] * growth_factor * dt + transfers

# -------------------------------------------------------------
# 5) ESKAPE pathogen MDR profile
# -------------------------------------------------------------
eskape = {
    "E. faecium (VRE)": {"VRE_pct": 30, "WHO_priority": "Medium"},
    "S. aureus (MRSA)": {"MRSA_pct": 22, "WHO_priority": "High"},
    "K. pneumoniae (CRE)": {"CRE_pct": 15, "WHO_priority": "Critical"},
    "A. baumannii (CRAB)": {"CRAB_pct": 56, "WHO_priority": "Critical"},
    "P. aeruginosa (CRPA)": {"CRPA_pct": 25, "WHO_priority": "Critical"},
    "Enterobacter (ESBL/CRE)": {"ESBL_pct": 35, "WHO_priority": "Critical"},
}

# -------------------------------------------------------------
# 6) Resistance emergence dynamics (logistic)
# -------------------------------------------------------------
years_em = np.linspace(0, 30, 200)
# Cefiderocol case: very fast emergence
def emerge(t, t_em, tau):
    return 1 / (1 + np.exp(-(t - t_em) / tau))

cefiderocol = 100 * emerge(years_em, 1.0, 0.5)
vancomycin = 100 * emerge(years_em, 28, 4.0)
ciprofloxacin = 100 * emerge(years_em, 4, 1.5)
linezolid = 100 * emerge(years_em, 1.0, 1.5)

# -------------------------------------------------------------
# 7) NDM-1 global spread
# -------------------------------------------------------------
ndm_years = np.arange(2008, 2025)
# 1 country (India) -> 5 (2010) -> 30 (2015) -> 70+ (2024)
ndm_countries = np.array([1, 2, 5, 15, 25, 40, 50, 55, 60, 65, 68, 70, 72, 75, 78, 80, 82])

# -------------------------------------------------------------
# 8) ITU K_resistance axiom check
# -------------------------------------------------------------
N_strains = 5000
# Initial: 0.1% with resistance gene (rare baseline)
log_fit = rng.normal(0, 0.3, size=N_strains)
resistance_strain = rng.random(N_strains) < 0.001  # rare R
log_fit[resistance_strain] += 0.1  # tiny fitness benefit baseline

p_pre = np.exp(log_fit); p_pre /= p_pre.sum()
S_pre = -np.sum(p_pre * np.log(p_pre))

# Antibiotic selection: R strains gain massive fitness
log_fit_post = log_fit.copy()
log_fit_post[resistance_strain] += 5.0  # huge selective advantage
log_fit_post[~resistance_strain] -= 2.0
p_post = np.exp(log_fit_post); p_post /= p_post.sum()
S_post = -np.sum(p_post * np.log(p_post))

# Linearized
log_p_pre = np.log(p_pre)
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# After selection R strain frequency
R_frac_pre = float(p_pre[resistance_strain].sum())
R_frac_post = float(p_post[resistance_strain].sum())

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 194 — Antibiotic Resistance + Plasmid + AMR (K_resistance)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Antibiotic discovery timeline
ax = axes[0, 0]
colors_t = ["#2ca02c" if x >= 5 else "#ff7f0e" if x >= 2 else "#d62728" for x in new_classes]
ax.bar(decades, new_classes, width=8, color=colors_t)
ax.set_xlabel("Decade")
ax.set_ylabel("New antibiotic classes")
ax.set_title("Discovery void: golden age (1950s-60s) → 2000s drought")
ax.grid(True, alpha=0.3, axis="y")

# Panel 2: Resistance mechanisms
ax = axes[0, 1]
mech = list(mechanisms.keys())
mech_pct = list(mechanisms.values())
ax.pie(mech_pct, labels=mech, autopct="%1.0f%%", textprops={"fontsize": 8})
ax.set_title("Resistance mechanisms")

# Panel 3: Conjugation kinetics
ax = axes[0, 2]
ax.semilogy(hours, D, "-", color="#1f77b4", lw=2, label="Donor (R+)")
ax.semilogy(hours, R, "-", color="#2ca02c", lw=2, label="Recipient (R-)")
ax.semilogy(hours, T_pop, "-", color="#d62728", lw=2, label="Transconjugant")
ax.set_xlabel("Hours")
ax.set_ylabel("CFU/mL (log)")
ax.set_title("Plasmid conjugation kinetics (Lederberg 1946)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 4: Resistance emergence speed
ax = axes[1, 0]
ax.plot(years_em, vancomycin, "-", color="#1f77b4", lw=2, label="Vancomycin (28 yr)")
ax.plot(years_em, ciprofloxacin, "-", color="#2ca02c", lw=2, label="Ciprofloxacin (4 yr)")
ax.plot(years_em, linezolid, "-", color="#ff7f0e", lw=2, label="Linezolid (1 yr)")
ax.plot(years_em, cefiderocol, "-", color="#d62728", lw=2, label="Cefiderocol (1 yr) ★")
ax.set_xlabel("Years after introduction")
ax.set_ylabel("Resistance prevalence (%)")
ax.set_title("Time-to-resistance: acceleration over decades")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: ESKAPE MDR rates
ax = axes[1, 1]
names_e = list(eskape.keys())
rates_e = [list(eskape[n].values())[0] for n in names_e]
priorities = [eskape[n]["WHO_priority"] for n in names_e]
colors_e = ["#d62728" if p == "Critical" else "#ff7f0e" if p == "High" else "#2ca02c"
            for p in priorities]
ax.barh(range(len(names_e)), rates_e, color=colors_e)
ax.set_yticks(range(len(names_e)))
ax.set_yticklabels(names_e, fontsize=7)
ax.set_xlabel("MDR phenotype prevalence (%)")
ax.set_title("ESKAPE pathogens (WHO Priority 2024)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: NDM-1 global spread + ITU
ax = axes[1, 2]
ax.plot(ndm_years, ndm_countries, "o-", color="#d62728", lw=2, markersize=8)
ax.set_xlabel("Year")
ax.set_ylabel("Countries with NDM-1 detection")
ax.set_title(f"NDM-1 global spread; ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 194,
    "tier1_paper": 27,
    "block": "B",
    "topic": "AMR + plasmid + resistance mechanisms (K_resistance)",
    "antibiotic_discovery_timeline": {
        "decades": decades.tolist(),
        "new_classes_per_decade": new_classes.tolist(),
        "trend": "Golden age 1950s-60s, void 2000s+",
    },
    "resistance_mechanisms_pct": mechanisms,
    "plasmid_Inc_groups": inc_groups,
    "NDM_1_history": {
        "discovery": "2008 New Delhi (Yong 2009 AAC)",
        "spread": "1 country -> 80+ countries by 2024",
        "type": "Class B metallo-β-lactamase, Zn-dependent",
        "ESKAPE_member_carrying": ["K. pneumoniae", "A. baumannii", "E. coli", "P. aeruginosa"],
    },
    "conjugation_kinetics_simulation": {
        "donor_initial_CFU": float(N0_d),
        "recipient_initial_CFU": float(N0_r),
        "transconjugant_24h_CFU": float(T_pop[-1]),
        "transfer_efficiency": float(T_pop[-1] / N0_r),
        "Lederberg_year": 1946,
    },
    "ESKAPE_pathogens_2024": eskape,
    "time_to_resistance_years": {
        "Cefiderocol": 1,
        "Linezolid": 1,
        "Ciprofloxacin": 4,
        "Vancomycin": 28,
        "Penicillin": 2,
        "trend": "acceleration: 28 -> 1 year over 50 years",
    },
    "NDM_global_spread_year_country_pairs": dict(zip(ndm_years.tolist(),
                                                     ndm_countries.tolist())),
    "ITU_K_resistance": {
        "N_strains": int(N_strains),
        "R_initial_pct": float(R_frac_pre * 100),
        "R_post_antibiotic_pct": float(R_frac_post * 100),
        "enrichment_factor": float(R_frac_post / R_frac_pre) if R_frac_pre > 0 else float("inf"),
        "S_pre_nats": float(S_pre),
        "S_post_nats": float(S_post),
        "delta_S_first_order": float(dS_lin),
        "delta_K_first_order": float(dK_lin),
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "AMR_mortality_2019_Murray_Lancet_per_year": 1.27e6,
    "AMR_2050_projection_ONeill_per_year": 1.0e7,
    "ITU_interpretation": {
        "K_state": "K_resistance (sub-state of K_microbe)",
        "modular_Hamiltonian": "K_resistance^(0) = -log P(resistant | exposure context)",
        "selection_dynamics": "Antibiotic exposure → ITU descent into R-enriched repertoire",
        "HGT_role": "Plasmid spread = K-state jumps between communities (fastest ITU mixing)",
        "Cefiderocol_lesson": "Designer antibiotic, 1-year resistance = ITU rapid descent saturation",
        "consequence": "AMR = accelerating ITU descent on global K_microbe manifold",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
