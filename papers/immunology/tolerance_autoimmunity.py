"""
Phase 187 — Tolerance + autoimmunity (AIRE + Tregs + SLE/RA + K_tolerance)

Simulations:
  1) Thymic negative selection: 10^9 thymocytes -> 1-5% survival
  2) AIRE function: TSA expression in mTEC
  3) Treg suppression dynamics
  4) Autoimmune disease prevalence + sex ratios
  5) HLA-disease OR (RA: DRB1*04, T1D: DQ2/DQ8)
  6) ITU K_tolerance^(0) forbidden subset modeling
  7) Self-vs-foreign discrimination breakdown -> AID-mediated leakage

Outputs:
  - tolerance_autoimmunity.png
  - tolerance_autoimmunity_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("tolerance_autoimmunity.png")
OUT_JSON = Path(__file__).with_name("tolerance_autoimmunity_summary.json")

rng = np.random.default_rng(20260521)

# -------------------------------------------------------------
# 1) Thymic negative selection
# -------------------------------------------------------------
N_thymocytes = 1_000_000  # 10^6 simulation; biology is 10^9/day
# Reactivity drawn from log-normal
reactivity = rng.lognormal(mean=0, sigma=1.2, size=N_thymocytes)
threshold_strong = np.percentile(reactivity, 95)  # strongest 5% deleted
threshold_weak = np.percentile(reactivity, 50)    # weakest 50% don't get positive selection

# Selection logic
n_total = N_thymocytes
n_death_by_neglect = np.sum(reactivity < threshold_weak * 0.5)  # die by neglect
n_neg_selected = np.sum(reactivity > threshold_strong)  # negative selection
n_treg = np.sum((reactivity >= threshold_strong * 0.7) & (reactivity <= threshold_strong))
n_survivors_to_periphery = n_total - n_death_by_neglect - n_neg_selected
survival_pct = 100 * n_survivors_to_periphery / n_total

# -------------------------------------------------------------
# 2) AIRE - tissue-specific antigen (TSA) expression
# -------------------------------------------------------------
# AIRE +/+ vs AIRE -/- TSA expression
n_TSAs = 1500  # typical number of tissue-specific antigens
mTEC_expression_AIRE_pos = rng.uniform(0.3, 1.0, size=n_TSAs)
mTEC_expression_AIRE_neg = rng.uniform(0.0, 0.15, size=n_TSAs)

# Fraction of self-reactive T cells that escape thymic selection
fraction_escape_WT = 0.001  # 0.1% (background rate)
fraction_escape_AIRE_KO = 0.15  # 15%
fold_increase_AIRE_KO = fraction_escape_AIRE_KO / fraction_escape_WT

# -------------------------------------------------------------
# 3) Treg dynamics: time course post-immunization
# -------------------------------------------------------------
days = np.linspace(0, 60, 200)
# Treg expansion peaks ~day 7-14 after antigen, then contraction
treg_response = 5 + 10 * np.exp(-((days - 10) / 7.0) ** 2) + \
                3 * np.exp(-((days - 30) / 15.0) ** 2)
effector_response = 5 + 25 * np.exp(-((days - 7) / 5.0) ** 2) * (1 - 0.05 * days/60)
# Treg/Effector ratio: critical for tolerance vs immunity
treg_eff_ratio = treg_response / effector_response

# -------------------------------------------------------------
# 4) Autoimmune disease prevalence + F:M
# -------------------------------------------------------------
diseases = {
    "SLE": {"prev_pct": 0.05, "F_to_M": 9.0},
    "RA": {"prev_pct": 0.75, "F_to_M": 3.0},
    "T1D": {"prev_pct": 0.40, "F_to_M": 1.0},
    "MS": {"prev_pct": 0.10, "F_to_M": 2.5},
    "Hashimoto": {"prev_pct": 1.50, "F_to_M": 8.0},
    "Graves": {"prev_pct": 0.50, "F_to_M": 7.0},
    "Sjögren": {"prev_pct": 0.50, "F_to_M": 9.0},
    "Psoriasis": {"prev_pct": 2.00, "F_to_M": 1.0},
    "IBD": {"prev_pct": 0.30, "F_to_M": 1.2},
}

# -------------------------------------------------------------
# 5) HLA disease OR
# -------------------------------------------------------------
hla_or = {
    "DRB1*04 (shared epitope) / RA": 4.0,
    "DRB1*15:01 / MS": 3.0,
    "DR2 / SLE": 2.5,
    "DQ2/DQ8 / T1D": 7.0,
    "DQ2/DQ8 / Celiac": 19.0,
    "B27 / AS": 87.0,
    "B57 / drug hypersensitivity": 100.0,
}

# -------------------------------------------------------------
# 6) ITU K_tolerance^(0) forbidden subset
# -------------------------------------------------------------
# Model: clone fitness with self-tolerance constraint
N_clones = 10_000
log_aff_self = rng.normal(0, 1.5, size=N_clones)  # affinity to self-pMHC
log_aff_foreign = rng.normal(0, 1.5, size=N_clones)  # affinity to foreign pMHC

# Pre-selection clone distribution: uniform
p_pre = np.ones(N_clones) / N_clones
S_pre = -np.sum(p_pre * np.log(p_pre))

# Post-thymic selection: clones with self-affinity > threshold are deleted
self_threshold = 1.0  # log-affinity threshold
allowed = log_aff_self < self_threshold
p_post = np.where(allowed, 1.0, 0.0)
p_post = p_post / p_post.sum()
S_post = -np.sum(np.where(p_post > 0, p_post * np.log(p_post), 0))
fraction_allowed = float(allowed.mean())

# K_tolerance^(0) "forbidden subset" — clones with self affinity above threshold
# Their K-cost goes to +infinity (forbidden); allowed clones have K = -log(p_pre) = log(N)
K_allowed = -np.log(p_pre[0])
forbidden_count = int(np.sum(~allowed))

# ITU axiom for tolerance: linearized at p_pre
dp = p_post - p_pre
log_p_pre = np.log(p_pre)
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# Autoimmune disease: small fraction of "leaky" clones escape tolerance
autoimmune_leak_rate = 0.02
p_leaky = p_pre.copy()
leaky_mask = (~allowed) & (rng.random(N_clones) < autoimmune_leak_rate)
# These get small but nonzero probability
n_leaky = int(leaky_mask.sum())

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 187 — Tolerance + Autoimmunity (K_tolerance forbidden subset)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Thymic selection histogram
ax = axes[0, 0]
ax.hist(np.log10(reactivity), bins=60, color="#1f77b4", alpha=0.6, label="All thymocytes")
ax.axvline(np.log10(threshold_strong), color="red", linestyle="--", lw=2,
           label=f"Neg selection threshold\n(top 5% = {n_neg_selected:,})")
ax.axvline(np.log10(threshold_weak * 0.5), color="orange", linestyle="--", lw=2,
           label=f"Death-by-neglect")
ax.set_xlabel("log10(self-reactivity)")
ax.set_ylabel("Thymocyte count")
ax.set_title(f"Thymic selection: {survival_pct:.1f}% → periphery")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: AIRE TSA expression
ax = axes[0, 1]
ax.hist(mTEC_expression_AIRE_pos, bins=30, alpha=0.6, color="#2ca02c",
        label=f"AIRE +/+ (escape {fraction_escape_WT*100:.1f}%)")
ax.hist(mTEC_expression_AIRE_neg, bins=30, alpha=0.6, color="#d62728",
        label=f"AIRE -/- (escape {fraction_escape_AIRE_KO*100:.0f}%)\n→ APECED")
ax.set_xlabel("TSA expression level (a.u.)")
ax.set_ylabel("Number of TSAs")
ax.set_title(f"AIRE function: {fold_increase_AIRE_KO:.0f}× escape in KO")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Treg dynamics
ax = axes[0, 2]
ax.plot(days, treg_response, "-", color="#9467bd", lw=2, label="Treg (FoxP3+)")
ax.plot(days, effector_response, "-", color="#d62728", lw=2, label="Effector T cells")
ax2 = ax.twinx()
ax2.plot(days, treg_eff_ratio, "--", color="#1f77b4", lw=1.5, label="Treg/Effector")
ax.set_xlabel("Days post-immunization")
ax.set_ylabel("Cell count (% of CD4+)")
ax2.set_ylabel("Treg/Effector ratio", color="#1f77b4")
ax.set_title("Treg dynamics (Sakaguchi 1995)")
ax.legend(fontsize=8, loc="upper right")
ax2.legend(fontsize=8, loc="lower right")
ax.grid(True, alpha=0.3)

# Panel 4: Autoimmune prevalence + F:M
ax = axes[1, 0]
names = list(diseases.keys())
prevs = [diseases[d]["prev_pct"] for d in names]
fm = [diseases[d]["F_to_M"] for d in names]
x = np.arange(len(names))
ax.bar(x, prevs, color="#1f77b4", alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(names, rotation=30, fontsize=8)
ax.set_ylabel("Prevalence (%)", color="#1f77b4")
ax2 = ax.twinx()
ax2.plot(x, fm, "o-", color="#d62728", lw=2, markersize=8)
ax2.set_ylabel("F:M ratio", color="#d62728")
ax.set_title("Autoimmune disease burden (5-10% population)")
ax.grid(True, alpha=0.3)

# Panel 5: HLA disease OR
ax = axes[1, 1]
hla_names = list(hla_or.keys())
ors = list(hla_or.values())
ax.barh(range(len(hla_names)), ors, color="#d62728")
ax.axvline(1.0, color="black", linestyle="--", alpha=0.5)
ax.set_xscale("log")
ax.set_yticks(range(len(hla_names)))
ax.set_yticklabels(hla_names, fontsize=7)
ax.set_xlabel("Odds ratio (log)")
ax.set_title("HLA autoimmune associations")
ax.grid(True, alpha=0.3, which="both")

# Panel 6: ITU K_tolerance forbidden subset
ax = axes[1, 2]
# Show clones in (self-aff, foreign-aff) space
ax.scatter(log_aff_self[allowed], log_aff_foreign[allowed], s=2, alpha=0.3,
           color="#2ca02c", label=f"Allowed ({allowed.sum():,})")
ax.scatter(log_aff_self[~allowed], log_aff_foreign[~allowed], s=2, alpha=0.3,
           color="#d62728", label=f"Forbidden ({(~allowed).sum():,})")
ax.scatter(log_aff_self[leaky_mask], log_aff_foreign[leaky_mask], s=20, alpha=0.9,
           color="#ff7f0e", label=f"Leaky (autoimmune, {n_leaky})")
ax.axvline(self_threshold, color="black", linestyle="--", lw=2)
ax.set_xlabel("log(affinity to self)")
ax.set_ylabel("log(affinity to foreign)")
ax.set_title(f"K_tolerance forbidden subset: ITU δS/δ⟨K⟩={itu_ratio:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 187,
    "tier1_paper": 26,
    "block": "B",
    "topic": "Tolerance + autoimmunity + K_tolerance",
    "thymic_selection": {
        "N_thymocytes_simulated": int(N_thymocytes),
        "biology_N_per_day": "10^9",
        "negative_selection_pct": float(100 * n_neg_selected / N_thymocytes),
        "death_by_neglect_pct": float(100 * n_death_by_neglect / N_thymocytes),
        "survival_to_periphery_pct": float(survival_pct),
        "expected_survival_pct": "1-5",
    },
    "AIRE_function": {
        "TSAs_expressed_in_mTEC": int(n_TSAs),
        "fraction_escape_AIRE_WT": fraction_escape_WT,
        "fraction_escape_AIRE_KO": fraction_escape_AIRE_KO,
        "fold_increase_in_KO": fold_increase_AIRE_KO,
        "loss_of_function_disease": "APECED (1/9,000 Finns)",
        "reference": "Anderson 2002 Science; AIRE 1997",
    },
    "Treg_dynamics": {
        "discovery": "Sakaguchi 1995 (CD4+CD25+)",
        "transcription_factor": "FoxP3 (Brunkow 2001)",
        "fraction_of_CD4_T": "5-10%",
        "loss_of_function_disease": "IPEX (X-linked, FoxP3 mutation)",
        "scurfy_mouse_lethality_weeks": "3-4 (multi-organ autoimmune)",
    },
    "autoimmune_diseases": diseases,
    "HLA_disease_OR": hla_or,
    "ITU_K_tolerance": {
        "N_clones": int(N_clones),
        "S_pre_selection_nats": float(S_pre),
        "S_post_selection_nats": float(S_post),
        "delta_S": float(S_post - S_pre),
        "fraction_allowed": fraction_allowed,
        "forbidden_count": int(forbidden_count),
        "leaky_count": int(n_leaky),
        "delta_S_linear": float(dS_lin),
        "delta_K_linear": float(dK_lin),
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_tolerance (sub-state of K_immune)",
        "modular_Hamiltonian": "K_tolerance^(0) = forbidden-subset operator",
        "central_tolerance": "Thymic deletion = global zero-set on repertoire manifold",
        "peripheral_tolerance": "Treg + anergy + AICD = local damping field",
        "autoimmune_disease": "Leakage in K_tolerance^(0) forbidden subset",
        "AIRE_role": "Promiscuous TSA expression extends thymic deletion to peripheral antigens",
        "loss_diseases": ["APECED (AIRE)", "IPEX (FoxP3)", "ALPS (Fas/FasL)"],
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
