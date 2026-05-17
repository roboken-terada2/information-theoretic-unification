"""
Phase 196 — Virus evolution + pandemic + zoonotic spillover (K_pandemic)

Simulations:
  1) RNA/DNA virus mutation rate comparison
  2) Quasispecies cloud (Eigen 1971)
  3) SIR pandemic dynamics for SARS-CoV-2 variants
  4) Pandemic history mortality
  5) Spillover 5-stage cascade (Plowright 2017)
  6) Herd immunity threshold by R0
  7) ITU K_pandemic axiom check during spillover

Outputs:
  - pandemic_spillover.png
  - pandemic_spillover_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

OUT_PNG = Path(__file__).with_name("pandemic_spillover.png")
OUT_JSON = Path(__file__).with_name("pandemic_spillover_summary.json")

rng = np.random.default_rng(20260530)

# -------------------------------------------------------------
# 1) Mutation rate comparison
# -------------------------------------------------------------
mutation_rates = {
    "DNA repair host":     1e-9,
    "Bacteria":            1e-9,
    "DNA virus (Pox)":     1e-7,
    "Retrovirus (HIV RT)": 1e-5,
    "Influenza (RdRp)":    1.5e-4,
    "Other RNA virus":     1e-3,
    "SARS-CoV-2 (nsp14 proof-reading)": 1e-6,
}

# -------------------------------------------------------------
# 2) Quasispecies cloud (Eigen 1971)
# -------------------------------------------------------------
# Master sequence + mutant cloud
# Error threshold: μ*L*(1-1/σ) > 1 -> error catastrophe
seq_length = 30000  # SARS-CoV-2 genome
sigma = 1.5  # fitness ratio master vs mutants
mu_grid = np.logspace(-7, -2, 50)
error_threshold_violated = mu_grid * seq_length * (1 - 1 / sigma) > 1
# Quasispecies entropy proxy (Hamming distance distribution)
mu_picked = np.array([1e-6, 1e-4, 1e-3, 5e-3, 1e-2])
n_variants = mu_picked * seq_length * 3  # 3 possible substitutions per site

# -------------------------------------------------------------
# 3) SIR for SARS-CoV-2 variants
# -------------------------------------------------------------
def sir(y, t, beta, gamma):
    S, I, R = y
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

t = np.linspace(0, 120, 400)
N_pop = 1.0
y0 = [N_pop - 1e-6, 1e-6, 0]
gamma_rec = 1/7  # recovery time 7 days

variants = {
    "Wild (R₀=2.5)":    {"R0": 2.5, "color": "#1f77b4"},
    "Alpha (R₀=4.5)":   {"R0": 4.5, "color": "#2ca02c"},
    "Delta (R₀=6)":     {"R0": 6.0, "color": "#ff7f0e"},
    "Omicron (R₀=9)":   {"R0": 9.0, "color": "#d62728"},
}

sir_results = {}
for name, v in variants.items():
    beta = v["R0"] * gamma_rec
    sol = odeint(sir, y0, t, args=(beta, gamma_rec))
    sir_results[name] = sol[:, 1]  # I curve

# -------------------------------------------------------------
# 4) Pandemic history mortality
# -------------------------------------------------------------
pandemics = {
    "1918 H1N1": 50.0,
    "HIV/AIDS (1981-)": 40.0,
    "COVID-19 (2020-23 excess)": 24.0,
    "1957 H2N2": 1.1,
    "1968 H3N2": 1.0,
    "2009 H1N1": 0.4,
    "Ebola 2014-16": 0.011,
    "SARS 2003": 0.0008,
    "MERS 2012-": 0.001,
}

# -------------------------------------------------------------
# 5) Spillover 5-stage cascade probabilities (Plowright 2017)
# -------------------------------------------------------------
stages = ["1. Reservoir\nabundance", "2. Pathogen\nprevalence",
          "3. Release\n(shedding)", "4. Exposure\n(contact)",
          "5. Susceptibility\n(barrier)"]
typical_probs = [0.8, 0.3, 0.1, 0.05, 0.01]  # cumulative product gives spillover rate
cumulative = np.cumprod(typical_probs)

# -------------------------------------------------------------
# 6) Herd immunity threshold
# -------------------------------------------------------------
R0_grid = np.linspace(1, 18, 100)
herd_threshold = (1 - 1 / R0_grid) * 100

named_R0 = {"Measles": 15.0, "Pertussis": 13.0, "SARS-CoV-2 Wild": 3.0,
            "SARS-CoV-2 Omicron": 9.0, "Smallpox": 5.5, "Flu seasonal": 1.3,
            "Polio": 6.0, "Ebola": 1.8}

# -------------------------------------------------------------
# 7) ITU K_pandemic axiom check: zoonotic spillover
# -------------------------------------------------------------
# Model: virus distribution in animal reservoir vs human host
N_variants = 10_000
# Animal reservoir: K-state distribution (master + cloud)
log_fit_animal = -((np.arange(N_variants) - N_variants//2) / 1000) ** 2  # bell shape
p_animal = np.exp(log_fit_animal); p_animal /= p_animal.sum()
S_animal = float(-np.sum(p_animal * np.log(p_animal)))

# Spillover: human-adaptive variants gain massive fitness, others crash
human_adaptive = (np.arange(N_variants) - N_variants//2) < -2000  # left tail
log_fit_human = log_fit_animal.copy()
log_fit_human[human_adaptive] += 8.0
log_fit_human[~human_adaptive] -= 4.0
p_human = np.exp(log_fit_human); p_human /= p_human.sum()
S_human = float(-np.sum(p_human * np.log(p_human)))

# ITU linearized
log_p_animal = np.log(np.clip(p_animal, 1e-30, None))
dp = p_human - p_animal
dS_lin = -np.sum(dp * (1.0 + log_p_animal))
dK_lin = -np.sum(dp * log_p_animal)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 196 — Virus Evolution + Pandemic + Zoonotic Spillover (K_pandemic)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Mutation rates
ax = axes[0, 0]
groups = list(mutation_rates.keys())
rates = list(mutation_rates.values())
colors = ["#1f77b4" if "DNA" in g or "Bacteria" in g else "#d62728"
          for g in groups]
ax.barh(range(len(groups)), rates, color=colors)
ax.set_xscale("log")
ax.set_yticks(range(len(groups)))
ax.set_yticklabels(groups, fontsize=8)
ax.set_xlabel("Mutation rate (/bp/replication, log)")
ax.set_title("RNA virus = 10⁵× DNA host mutation rate")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 2: Error catastrophe (Eigen 1971)
ax = axes[0, 1]
ax.semilogx(mu_grid, mu_grid * seq_length * (1 - 1/sigma), "-", color="#9467bd", lw=2,
            label="μ·L·(1-1/σ)")
ax.axhline(1, color="red", linestyle="--", lw=2, label="Error threshold")
ax.fill_between(mu_grid, 0, mu_grid * seq_length * (1 - 1/sigma),
                where=error_threshold_violated, color="red", alpha=0.2)
ax.set_xlabel("Mutation rate μ /bp")
ax.set_ylabel("Quasispecies viability")
ax.set_title(f"Eigen quasispecies (L={seq_length})")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: SIR dynamics for variants
ax = axes[0, 2]
for name, I_curve in sir_results.items():
    ax.plot(t, I_curve * 100, "-", color=variants[name]["color"], lw=2, label=name)
ax.set_xlabel("Days")
ax.set_ylabel("Infected (% population)")
ax.set_title("SIR pandemic dynamics by R₀ variant")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Pandemic history mortality
ax = axes[1, 0]
pandemics_sorted = dict(sorted(pandemics.items(), key=lambda x: -x[1]))
names_p = list(pandemics_sorted.keys())
deaths_M = list(pandemics_sorted.values())
ax.barh(range(len(names_p)), deaths_M, color="#d62728")
ax.set_xscale("log")
ax.set_yticks(range(len(names_p)))
ax.set_yticklabels(names_p, fontsize=8)
ax.set_xlabel("Deaths (millions, log)")
ax.set_title("Major pandemic mortality 1918-2023")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 5: Spillover 5-stage cascade
ax = axes[1, 1]
x = np.arange(len(stages))
ax.bar(x, typical_probs, color="#1f77b4", alpha=0.7, label="Stage probability")
ax.plot(x, cumulative, "o-", color="#d62728", lw=2, markersize=8, label="Cumulative")
ax.set_xticks(x)
ax.set_xticklabels(stages, fontsize=7)
ax.set_yscale("log")
ax.set_ylabel("Probability (log)")
ax.set_title(f"Spillover cascade (Plowright 2017); final ≈ {cumulative[-1]:.4f}")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 6: Herd immunity + ITU
ax = axes[1, 2]
ax.plot(R0_grid, herd_threshold, "-", color="#1f77b4", lw=2)
for name, r0 in named_R0.items():
    ax.scatter([r0], [(1 - 1/r0)*100], s=80, color="#d62728", zorder=5)
    ax.annotate(name, (r0, (1 - 1/r0)*100), fontsize=7,
                xytext=(5, -5), textcoords="offset points")
ax.set_xlabel("R₀")
ax.set_ylabel("Herd immunity threshold (%)")
ax.set_title(f"Herd immunity = 1 - 1/R₀;  ITU spillover δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 196,
    "tier1_paper": 27,
    "block": "B",
    "topic": "Virus evolution + pandemic + zoonotic spillover (K_pandemic)",
    "mutation_rates_per_bp_per_replication": mutation_rates,
    "quasispecies_theory": {
        "discoverer": "Manfred Eigen 1971",
        "error_threshold_formula": "mu * L * (1 - 1/sigma) > 1",
        "SARS-CoV-2_length_bp": seq_length,
        "drug_strategy": "Favipiravir increases mu past threshold -> error catastrophe",
    },
    "SARS_CoV_2_R0_variants": {name: v["R0"] for name, v in variants.items()},
    "pandemic_mortality_M": pandemics,
    "spillover_5_stages_Plowright_2017": dict(zip(stages, typical_probs)),
    "spillover_cumulative_probability": float(cumulative[-1]),
    "herd_immunity_thresholds_pct": {
        name: float((1 - 1/r) * 100) for name, r in named_R0.items()
    },
    "ITU_K_pandemic_axiom": {
        "N_variants": N_variants,
        "S_animal_reservoir_nats": S_animal,
        "S_human_adapted_nats": S_human,
        "delta_S": S_human - S_animal,
        "delta_S_first_order": float(dS_lin),
        "delta_K_first_order": float(dK_lin),
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pandemic (sub-state of K_microbe)",
        "modular_Hamiltonian": "K_pandemic^(0) = -log P(virus state | host, environment)",
        "spillover_meaning": "ITU K-state inter-species jump (Plowright cascade)",
        "Quasispecies_role": "Cloud of variants samples K-state manifold",
        "Disease_X_concept": "WHO 2018: unknown next pandemic = K_pandemic dark zero set",
        "One_Health_view": "K_human ⊗ K_animal ⊗ K_environment integrated",
        "COVID_excess_deaths": "WHO 2023: 18-30 million globally",
    },
    "predictions": [
        ("Next major pandemic (CFR>0.5%)", 2030, 0.55, "Medium"),
        ("WHO Pandemic Treaty in force", 2028, 0.65, "Medium"),
        ("Universal coronavirus vaccine", 2028, 0.70, "Strong"),
        ("Disease X AI early detection system", 2030, 0.75, "Strong"),
        ("Spillover prediction model accuracy >80%", 2032, 0.50, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
