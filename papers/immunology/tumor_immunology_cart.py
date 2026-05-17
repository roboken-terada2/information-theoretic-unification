"""
Phase 189 — Tumor immunology + checkpoint + CAR-T (K_tumor)

Simulations:
  1) Cancer immunoediting 3E (Elimination -> Equilibrium -> Escape)
  2) Checkpoint inhibitor response: melanoma 5y survival 5% -> 34%
  3) CAR-T CR rates across approved products
  4) CRS (Cytokine Release Syndrome) IL-6 dynamics + Tocilizumab rescue
  5) Tumor mutational burden (TMB) vs checkpoint response
  6) PD-L1 expression vs response rate
  7) ITU K_tumor descent: exhausted T cell -> rescued

Outputs:
  - tumor_immunology_cart.png
  - tumor_immunology_cart_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("tumor_immunology_cart.png")
OUT_JSON = Path(__file__).with_name("tumor_immunology_cart_summary.json")

rng = np.random.default_rng(20260523)

# -------------------------------------------------------------
# 1) Cancer immunoediting 3E model
# -------------------------------------------------------------
years = np.linspace(0, 30, 400)
# Elimination: tumor cells suppressed (0-3 yr)
# Equilibrium: stable dormancy (3-15 yr)
# Escape: tumor breakout (15+ yr)
elim_phase = np.exp(-2.0 * years)
equil_phase = 0.05 * np.exp(-((years - 9) / 5.0) ** 2)
escape_phase = 1 / (1 + np.exp(-(years - 18) / 2.0))
total_tumor = elim_phase + equil_phase + escape_phase

# -------------------------------------------------------------
# 2) Melanoma 5-year survival: historical vs PD-1 era
# -------------------------------------------------------------
periods = ["Pre-2011\n(chemo)", "Ipilimumab\n(2011)", "Anti-PD-1\n(2014-)",
           "Combination\nIpi+Nivo (2015)", "Triplet incl.\nLAG3 (2022)"]
five_yr_surv = [5, 18, 34, 52, 60]  # %
ORR = [10, 11, 44, 58, 65]

# -------------------------------------------------------------
# 3) CAR-T CR rates
# -------------------------------------------------------------
cart_products = {
    "Tisagenlec (CD19, pALL)": 83,
    "Axi-cel (CD19, DLBCL)": 51,
    "Brexu-cel (CD19, MCL)": 65,
    "Liso-cel (CD19, DLBCL)": 53,
    "Ide-cel (BCMA, MM)": 33,
    "Cilta-cel (BCMA, MM)": 67,
}

# -------------------------------------------------------------
# 4) CRS IL-6 dynamics + tocilizumab rescue
# -------------------------------------------------------------
days = np.linspace(0, 21, 300)
# Without intervention: peak IL-6 ~ 1500 pg/mL day 7
il6_no_intervention = 5 + 1500 * np.exp(-((days - 7) / 1.5) ** 2)
# With tocilizumab on day 6 (anti-IL-6R)
il6_with_toci = il6_no_intervention.copy()
mask = days >= 6
il6_with_toci[mask] = 5 + (il6_no_intervention[mask] - 5) * np.exp(-(days[mask] - 6) / 0.5)

# -------------------------------------------------------------
# 5) TMB vs checkpoint response (CheckMate-227 / KN-158)
# -------------------------------------------------------------
TMB_bins = np.array([1, 5, 10, 20, 50, 100, 300])  # mut/Mb
response_rate = np.array([10, 18, 25, 35, 50, 58, 65])  # %
# Saturating logistic
# Show as bar+curve

# -------------------------------------------------------------
# 6) PD-L1 vs response (NSCLC pembro)
# -------------------------------------------------------------
PDL1_bins = ["<1%", "1-49%", "50-89%", "≥90%"]
PDL1_resp = [11, 19, 45, 50]  # %

# -------------------------------------------------------------
# 7) ITU K_tumor descent: exhausted T cell -> rescued
# -------------------------------------------------------------
# State: T cell repertoire (anti-tumor + exhausted)
N_clones = 5000
# Pre-treatment: dominated by exhausted clones with low effector probability
log_aff = rng.normal(0, 1.0, size=N_clones)
exhausted_fraction = 0.7
exhausted_mask = rng.random(N_clones) < exhausted_fraction

# Pre: exhausted clones suppressed (low p)
p_pre = np.where(exhausted_mask, 0.01, 1.0)
p_pre = p_pre / p_pre.sum()
S_pre = -np.sum(np.where(p_pre > 0, p_pre * np.log(p_pre), 0))

# Post checkpoint blockade: rescued exhausted clones
p_post = np.where(exhausted_mask, 0.5, 1.0)
p_post = p_post / p_post.sum()
S_post = -np.sum(np.where(p_post > 0, p_post * np.log(p_post), 0))

# CAR-T: artificial clone injection (bypass MHC, 1000 specific clones added)
p_cart = p_pre.copy()
n_cart_clones = 1000
cart_indices = rng.choice(N_clones, size=n_cart_clones, replace=False)
p_cart[cart_indices] *= 10
p_cart = p_cart / p_cart.sum()
S_cart = -np.sum(np.where(p_cart > 0, p_cart * np.log(p_cart), 0))

# ITU linearized for descent
log_p_pre = np.log(np.clip(p_pre, 1e-30, None))
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# CAR-T ITU
dp_cart = p_cart - p_pre
dS_cart_lin = -np.sum(dp_cart * (1.0 + log_p_pre))
dK_cart_lin = -np.sum(dp_cart * log_p_pre)
itu_ratio_cart = float(dS_cart_lin / dK_cart_lin) if abs(dK_cart_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 189 — Tumor Immunology + Checkpoint + CAR-T (K_tumor)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: 3E immunoediting
ax = axes[0, 0]
ax.plot(years, elim_phase, "-", color="#2ca02c", lw=2, label="Elimination (Burnet)")
ax.plot(years, equil_phase, "-", color="#ff7f0e", lw=2, label="Equilibrium (dormancy)")
ax.plot(years, escape_phase, "-", color="#d62728", lw=2, label="Escape (clinical cancer)")
ax.plot(years, total_tumor, "k--", lw=2, label="Total tumor burden")
ax.set_xlabel("Years after initial transformation")
ax.set_ylabel("Tumor burden / probability")
ax.set_title("3E model (Schreiber 2002)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Melanoma 5y survival evolution
ax = axes[0, 1]
x = np.arange(len(periods))
width = 0.35
ax.bar(x - width/2, five_yr_surv, width, color="#1f77b4", label="5-yr survival (%)")
ax.bar(x + width/2, ORR, width, color="#d62728", label="ORR (%)")
ax.set_xticks(x)
ax.set_xticklabels(periods, fontsize=8)
ax.set_ylabel("Percent (%)")
ax.set_title("Melanoma: 5% → 60% in a decade (Allison-Honjo 2018 Nobel)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: CAR-T CR rates
ax = axes[0, 2]
products = list(cart_products.keys())
crs = list(cart_products.values())
colors = ["#2ca02c" if c > 60 else "#ff7f0e" if c > 40 else "#d62728" for c in crs]
ax.barh(range(len(products)), crs, color=colors)
ax.set_yticks(range(len(products)))
ax.set_yticklabels(products, fontsize=8)
ax.set_xlabel("Complete response rate (%)")
ax.set_title("FDA-approved CAR-T products")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: CRS dynamics + tocilizumab rescue
ax = axes[1, 0]
ax.semilogy(days, il6_no_intervention, "-", color="#d62728", lw=2,
            label="No intervention (peak ~1500 pg/mL)")
ax.semilogy(days, il6_with_toci, "-", color="#2ca02c", lw=2,
            label="+ Tocilizumab day 6")
ax.axhline(10, color="black", linestyle="--", alpha=0.5, label="Normal <10")
ax.axvline(6, color="orange", linestyle=":", lw=2, label="Toci infusion")
ax.set_xlabel("Days post-CAR-T infusion")
ax.set_ylabel("IL-6 (pg/mL, log)")
ax.set_title("CRS rescue (anti-IL-6R)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 5: TMB vs response
ax = axes[1, 1]
ax.semilogx(TMB_bins, response_rate, "o-", color="#9467bd", lw=2, markersize=10)
ax.set_xlabel("TMB (mut / Mb)")
ax.set_ylabel("Response rate (%)")
ax.set_title("Tumor mutational burden (CheckMate-227)")
ax.grid(True, alpha=0.3, which="both")

# Panel 6: PD-L1 stratification + ITU
ax = axes[1, 2]
ax.bar(PDL1_bins, PDL1_resp, color=["#1f77b4", "#aec7e8", "#ff7f0e", "#d62728"])
ax.set_xlabel("PD-L1 TPS (%)")
ax.set_ylabel("ORR (%)")
ax.set_title(f"PD-L1 stratification (NSCLC pembro);  ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 189,
    "tier1_paper": 26,
    "block": "B",
    "topic": "Tumor immunology + checkpoint + CAR-T (K_tumor)",
    "cancer_immunoediting_3E": {
        "model": "Schreiber 2002 (Elimination, Equilibrium, Escape)",
        "Burnet_immunosurveillance": "1957",
        "evidence": "10× cancer rate in immunosuppressed transplant patients",
    },
    "melanoma_5yr_survival": {
        "periods": periods,
        "five_yr_pct": five_yr_surv,
        "ORR_pct": ORR,
        "fold_increase_2011_to_2022": float(five_yr_surv[-1] / five_yr_surv[0]),
        "Allison_Honjo_Nobel": 2018,
    },
    "CAR_T_products": cart_products,
    "Tisagenlecleucel_CR": 83,
    "BCMA_CART_avg_CR": 50,
    "CRS_dynamics": {
        "peak_IL6_no_intervention_pg_per_mL": 1500,
        "tocilizumab_rescue_hours_to_normal": "24-48 hours",
        "drug": "Anti-IL-6R (Tocilizumab)",
    },
    "TMB_response": {
        "TMB_mut_per_Mb": TMB_bins.tolist(),
        "response_pct": response_rate.tolist(),
        "threshold_high_TMB": 10,
        "reference": "CheckMate-227, KN-158 (Marabelle 2020)",
    },
    "PDL1_stratification": dict(zip(PDL1_bins, PDL1_resp)),
    "TIL_Lifileucel_ORR": 31,
    "Blinatumomab_ALL_CR": 44,
    "ITU_K_tumor": {
        "N_clones": N_clones,
        "S_pre_checkpoint_nats": float(S_pre),
        "S_post_checkpoint_nats": float(S_post),
        "S_CAR_T_nats": float(S_cart),
        "checkpoint_dS_dK_ratio": float(itu_ratio),
        "CAR_T_dS_dK_ratio": float(itu_ratio_cart),
        "exhausted_fraction": exhausted_fraction,
    },
    "ITU_interpretation": {
        "K_state": "K_tumor (sub-state of K_immune)",
        "tumor_escape": "K_tumor^(0) = inverse(K_tolerance) local inversion",
        "checkpoint_inhibitor": "Reopens forbidden region of K_tumor^(0)",
        "CAR_T": "Bypasses K_tumor via artificial K_state injection (non-MHC)",
        "neoantigen_vaccine": "ITU descent flow targeted at K_tumor specific subset",
        "Allison_Honjo_Nobel": "2018 (Physiology/Medicine)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
