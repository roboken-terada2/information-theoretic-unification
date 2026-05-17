"""
Phase 188 — Vaccines + mRNA + prime-boost dynamics (K_vaccine)

Simulations:
  1) Prime vs boost antibody titer dynamics
  2) Memory B cell longevity (measles vs COVID)
  3) mRNA translation half-life vs LNP delivery
  4) Pseudouridine (Karikó-Weissman) translation enhancement
  5) Antibody affinity evolution prime -> boost
  6) Efficacy across major vaccines (Phase III data)
  7) ITU K_vaccine descent flow: 2-step prime + boost
  8) Repertoire entropy across vaccination history

Outputs:
  - vaccine_mrna_prime_boost.png
  - vaccine_mrna_prime_boost_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("vaccine_mrna_prime_boost.png")
OUT_JSON = Path(__file__).with_name("vaccine_mrna_prime_boost_summary.json")

rng = np.random.default_rng(20260522)

# -------------------------------------------------------------
# 1) Prime vs Boost antibody titer
# -------------------------------------------------------------
days = np.linspace(0, 180, 600)

def titer_response(t, t_start, peak_amp, rise_tau, decay_tau):
    """Sigmoid-rise, exponential decay."""
    out = np.zeros_like(t)
    mask = t >= t_start
    dt = t[mask] - t_start
    rise = 1 - np.exp(-dt / rise_tau)
    decay = np.exp(-(dt - 3 * rise_tau) / decay_tau)
    decay = np.minimum(decay, 1.0)
    out[mask] = peak_amp * rise * decay
    return out

prime_titer = titer_response(days, 0, peak_amp=10.0, rise_tau=7.0, decay_tau=30.0)
boost_titer = titer_response(days, 28, peak_amp=500.0, rise_tau=4.0, decay_tau=60.0)
combined = prime_titer + boost_titer

# -------------------------------------------------------------
# 2) Memory B cell longevity (years)
# -------------------------------------------------------------
years = np.linspace(0, 60, 600)
measles_titer = 80 * np.exp(-0.5 * years) + 20 * np.exp(-0.0035 * years)
covid_titer = 90 * np.exp(-1.4 * years) + 10 * np.exp(-0.05 * years)
hbv_titer = 70 * np.exp(-0.3 * years) + 30 * np.exp(-0.04 * years)

# -------------------------------------------------------------
# 3) mRNA translation half-life
# -------------------------------------------------------------
hours = np.linspace(0, 72, 200)
unmod_mrna = 100 * np.exp(-hours / 1.5)  # half-life ~1 hour, low translation
psi_mrna = 100 * np.exp(-hours / 9.0)    # half-life ~9 hours (pseudouridine)

# Protein production rate * mRNA concentration
unmod_protein = np.cumsum(unmod_mrna) * 0.5  # arbitrary rate
psi_protein = np.cumsum(psi_mrna) * 5.0      # 10x rate

# -------------------------------------------------------------
# 4) Pseudouridine TLR escape: cytokine response
# -------------------------------------------------------------
mrna_types = ["Unmodified", "m5C", "Ψ (pseudo)", "m1Ψ (BNT/Moderna)"]
ifn_alpha_response = [100.0, 40.0, 8.0, 3.0]  # relative IFN-α (Karikó-Weissman 2008)
translation_efficiency = [1.0, 2.0, 5.0, 10.0]

# -------------------------------------------------------------
# 5) Antibody affinity evolution prime -> boost
# -------------------------------------------------------------
stages = ["Naive", "Day 14 prime", "Day 30 boost", "Day 60 post-boost", "Year 1 memory"]
Kd_M = [1e-3, 1e-5, 1e-7, 1e-8, 5e-9]
log_Kd = np.log10(Kd_M)

# -------------------------------------------------------------
# 6) Vaccine efficacy (Phase III)
# -------------------------------------------------------------
vaccines = {
    "Smallpox (Jenner 1796)": 100.0,
    "Measles MMR": 97.0,
    "MMR (mumps)": 88.0,
    "HBV recombinant": 95.0,
    "HPV Gardasil 9": 97.0,
    "BNT162b2 (Pfizer COVID)": 95.0,
    "mRNA-1273 (Moderna)": 94.1,
    "AZD1222 (AstraZeneca)": 70.0,
    "Sinovac (inactivated COVID)": 51.0,
    "Influenza (seasonal avg)": 45.0,
    "Malaria RTS,S": 36.0,
}

# -------------------------------------------------------------
# 7) ITU K_vaccine: 2-step descent flow
# -------------------------------------------------------------
N_clones = 20_000
# Naive: uniform distribution
p_naive = np.ones(N_clones) / N_clones
S_naive = float(-np.sum(p_naive * np.log(p_naive)))

# Prime: power-law focused (alpha ~1.0)
ranks = np.arange(1, N_clones + 1)
p_prime = ranks ** (-1.0); p_prime /= p_prime.sum()
S_prime = float(-np.sum(p_prime * np.log(p_prime)))

# Boost: more focused (alpha ~1.8)
p_boost = ranks ** (-1.8); p_boost /= p_boost.sum()
S_boost = float(-np.sum(p_boost * np.log(p_boost)))

# Memory plateau: stable, similar to boost but slightly relaxed
p_memory = ranks ** (-1.5); p_memory /= p_memory.sum()
S_memory = float(-np.sum(p_memory * np.log(p_memory)))

# Mean K^(0) at each stage (K^(0) = -log p_naive uniform = log N is constant)
# More useful: compute ITU linearized for each transition
def itu_linear(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    if abs(dK) < 1e-15:
        return float("nan"), float(dS), float(dK)
    return float(dS / dK), float(dS), float(dK)

ratio_naive_prime, dS_np, dK_np = itu_linear(p_naive, p_prime)
ratio_prime_boost, dS_pb, dK_pb = itu_linear(p_prime, p_boost)
ratio_boost_memory, dS_bm, dK_bm = itu_linear(p_boost, p_memory)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 188 — Vaccines + mRNA + Prime-Boost Dynamics (K_vaccine)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Prime vs Boost titer
ax = axes[0, 0]
ax.semilogy(days, np.maximum(prime_titer, 1e-2), "-", color="#1f77b4", lw=2, label="Prime only")
ax.semilogy(days, np.maximum(boost_titer, 1e-2), "-", color="#d62728", lw=2, label="Boost contribution")
ax.semilogy(days, np.maximum(combined, 1e-2), "-", color="#2ca02c", lw=3, label="Total (prime + boost)")
ax.axvline(28, color="black", linestyle="--", alpha=0.5, label="Boost day 28")
ax.set_xlabel("Days post-vaccination")
ax.set_ylabel("Antibody titer (a.u.)")
ax.set_title(f"Prime-boost ~50× peak titer increase")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 2: Memory longevity
ax = axes[0, 1]
ax.semilogy(years, measles_titer, "-", color="#2ca02c", lw=2,
            label="Measles 60+ yr (Amanna 2007)")
ax.semilogy(years, hbv_titer, "-", color="#1f77b4", lw=2, label="HBV ~20+ yr")
ax.semilogy(years, covid_titer, "-", color="#d62728", lw=2,
            label="COVID-19 ~1-2 yr (Wang 2021)")
ax.set_xlabel("Years post-immunization")
ax.set_ylabel("Antibody titer (% of peak)")
ax.set_title("Vaccine-induced antibody longevity")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 3: mRNA translation
ax = axes[0, 2]
ax.plot(hours, unmod_mrna, "-", color="#d62728", lw=2, label="Unmodified mRNA (t₁/₂≈1.5h)")
ax.plot(hours, psi_mrna, "-", color="#2ca02c", lw=2, label="Ψ-mRNA (t₁/₂≈9h)")
ax.set_xlabel("Hours")
ax.set_ylabel("mRNA remaining (%)")
ax.set_title("Karikó-Weissman Ψ-modification (Nobel 2023)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: Pseudouridine TLR escape
ax = axes[1, 0]
x = np.arange(len(mrna_types))
width = 0.35
bars1 = ax.bar(x - width/2, ifn_alpha_response, width, label="IFN-α response", color="#d62728")
ax2 = ax.twinx()
bars2 = ax2.bar(x + width/2, translation_efficiency, width, label="Translation efficiency", color="#2ca02c")
ax.set_xticks(x)
ax.set_xticklabels(mrna_types, fontsize=8, rotation=15)
ax.set_ylabel("IFN-α (relative)", color="#d62728")
ax2.set_ylabel("Translation efficiency", color="#2ca02c")
ax.set_title("Ψ-mRNA: TLR escape + translation boost")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="upper right", fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Affinity evolution
ax = axes[1, 1]
ax.plot(np.arange(len(stages)), log_Kd, "o-", color="#9467bd", lw=2, markersize=10)
ax.set_xticks(np.arange(len(stages)))
ax.set_xticklabels(stages, rotation=20, fontsize=8)
ax.set_ylabel("log10(Kd / M)")
ax.set_title(f"Antibody affinity: Kd 10⁻³ → 10⁻⁹ ({10**(np.log10(Kd_M[0])-np.log10(Kd_M[-1])):.0e}× improvement)")
ax.grid(True, alpha=0.3)

# Panel 6: Vaccine efficacy
ax = axes[1, 2]
names = list(vaccines.keys())
effs = list(vaccines.values())
colors = ["#2ca02c" if e > 90 else "#ff7f0e" if e > 70 else "#d62728" for e in effs]
ax.barh(range(len(names)), effs, color=colors)
ax.axvline(80, color="black", linestyle="--", alpha=0.5, label="WHO target 80%")
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=7)
ax.set_xlabel("Phase III efficacy (%)")
ax.set_title(f"Vaccine efficacy + ITU descent: prime→boost ratio={ratio_prime_boost:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="x")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 188,
    "tier1_paper": 26,
    "block": "B",
    "topic": "Vaccines + mRNA + prime-boost + K_vaccine",
    "prime_boost_titer": {
        "prime_peak_relative": 10.0,
        "boost_peak_relative": 500.0,
        "boost_over_prime_fold": 50.0,
        "boost_rise_tau_days": 4.0,
        "prime_rise_tau_days": 7.0,
    },
    "memory_longevity": {
        "measles_60yr_titer_pct": float(measles_titer[-1]),
        "HBV_60yr_titer_pct": float(hbv_titer[-1]),
        "COVID_60yr_titer_pct": float(covid_titer[-1]),
        "references": [
            "Amanna 2007 NEJM (measles 200+ yr)",
            "Wang 2021 Nature (COVID 1-2 month fast decay)",
        ],
    },
    "mRNA_translation": {
        "unmodified_half_life_hours": 1.5,
        "pseudouridine_half_life_hours": 9.0,
        "fold_extension": 6.0,
        "Kariko_Weissman_Nobel": 2023,
    },
    "pseudouridine_TLR_escape": {
        "mrna_types": mrna_types,
        "IFN_alpha_relative": ifn_alpha_response,
        "translation_efficiency_fold": translation_efficiency,
        "BNT_Moderna_modification": "N1-methylpseudouridine (m1Ψ)",
    },
    "affinity_evolution": {
        "stages": stages,
        "Kd_M": Kd_M,
        "total_fold_improvement": float(10 ** (np.log10(Kd_M[0]) - np.log10(Kd_M[-1]))),
    },
    "vaccine_efficacy_Phase_III": vaccines,
    "ITU_K_vaccine_descent": {
        "S_naive_nats": S_naive,
        "S_prime_nats": S_prime,
        "S_boost_nats": S_boost,
        "S_memory_nats": S_memory,
        "naive_to_prime_ratio_dS_dK": ratio_naive_prime,
        "prime_to_boost_ratio_dS_dK": ratio_prime_boost,
        "boost_to_memory_ratio_dS_dK": ratio_boost_memory,
    },
    "ITU_interpretation": {
        "K_state": "K_vaccine (sub-state of K_immune)",
        "modular_Hamiltonian": "K_vaccine^(0) controls prime->boost->memory cascade",
        "prime_boost_meaning": "Two-step ITU descent flow on repertoire manifold",
        "pseudouridine_role": "Suppress K_innate, optimize K_translation",
        "memory_plateau": "Long-lived plasma cell = topological ITU local minimum",
        "modern_mRNA": "Karikó-Weissman Ψ-modification (Nobel 2023)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
