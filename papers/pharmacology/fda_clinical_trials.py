"""
Phase 234 — FDA + Clinical trials + Regulation (K_pharma_regulatory)

Simulations:
  1) FDA milestones timeline
  2) Phase I-IV success rate breakdown
  3) FDA approval pathways comparison
  4) Global regulatory agencies (FDA/EMA/PMDA/NMPA/MHRA)
  5) Master protocol & adaptive trials
  6) In silico trial concept
  7) ITU K_pharma_regulatory axiom check

Outputs:
  - fda_clinical_trials.png
  - fda_clinical_trials_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("fda_clinical_trials.png")
OUT_JSON = Path(__file__).with_name("fda_clinical_trials_summary.json")

rng = np.random.default_rng(20260715)

# -------------------------------------------------------------
# 1) FDA milestones
# -------------------------------------------------------------
fda_history = {
    "Pure Food and Drug Act":   1906,
    "Sulfanilamide tragedy":     1937,
    "FDCA":                      1938,
    "Kefauver-Harris (Thalidomide)": 1962,
    "Orphan Drug Act":           1983,
    "PDUFA":                     1992,
    "Accelerated approval":      1997,
    "Breakthrough therapy":      2012,
    "COVID EUA (BNT162b2)":      2020,
    "AI/ML guidance":            2024,
}

# -------------------------------------------------------------
# 2) Phase success rates
# -------------------------------------------------------------
phase_rates = {
    "Discovery → Preclinical": 0.25,
    "Preclinical → Phase I":   0.65,
    "Phase I → II":             0.63,
    "Phase II → III":           0.30,  # bottleneck
    "Phase III → FDA":          0.58,
    "FDA → Approval":           0.85,
}
overall_success = 1.0
for r in phase_rates.values():
    overall_success *= r

# -------------------------------------------------------------
# 3) FDA approval pathways
# -------------------------------------------------------------
pathways = {
    "Standard":           {"review_months": 10, "drugs_pct": 60},
    "Priority Review":    {"review_months": 6,  "drugs_pct": 25},
    "Accelerated":        {"review_months": 6,  "drugs_pct": 10},
    "Breakthrough":       {"review_months": 6,  "drugs_pct": 30},  # can combine
    "Orphan Drug":        {"review_months": 8,  "drugs_pct": 35},
}

# -------------------------------------------------------------
# 4) Global regulatory agencies (market share + drugs approved 2024)
# -------------------------------------------------------------
agencies = {
    "FDA (US)":         {"market_pct": 45, "drugs_2024": 55},
    "EMA (EU)":         {"market_pct": 22, "drugs_2024": 40},
    "PMDA (JP)":        {"market_pct": 8,  "drugs_2024": 30},
    "NMPA (CN)":        {"market_pct": 11, "drugs_2024": 45},
    "MHRA (UK)":        {"market_pct": 4,  "drugs_2024": 25},
    "Others":           {"market_pct": 10, "drugs_2024": 100},
}

# -------------------------------------------------------------
# 5) Trial types
# -------------------------------------------------------------
trial_types = {
    "Single-arm Phase I":     {"patients": 50,    "duration_yr": 1.5},
    "Phase II open-label":    {"patients": 200,   "duration_yr": 2.5},
    "Phase III RCT":          {"patients": 2000,  "duration_yr": 2.5},
    "Master protocol":        {"patients": 5000,  "duration_yr": 3.0},
    "RECOVERY (COVID)":       {"patients": 50000, "duration_yr": 0.5},
    "All of Us cohort":       {"patients": 1000000,"duration_yr": 10},
}

# -------------------------------------------------------------
# 6) In silico trial concept (cohort sizes)
# -------------------------------------------------------------
silico_paradigms = {
    "Heart-on-Chip":     {"virtual_cohort": 10000,  "year": 2017},
    "AI cancer twin":     {"virtual_cohort": 50000,  "year": 2023},
    "Alzheimer model":    {"virtual_cohort": 100000, "year": 2024},
    "Synthetic control":  {"virtual_cohort": 5000,   "year": 2024},
}

# -------------------------------------------------------------
# 7) ITU K_pharma_regulatory axiom
# -------------------------------------------------------------
N_decisions = 2000
# Pre-trial: regulator unaware (broad prior)
log_fit_pre = 0.1 * rng.standard_normal(N_decisions)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Approve: peaked at approval region
log_fit_appr = log_fit_pre.copy()
log_fit_appr[1500:1600] += 4.0
p_appr = np.exp(log_fit_appr); p_appr /= p_appr.sum()
S_appr = float(-np.sum(p_appr * np.log(p_appr)))

# Reject: peaked at rejection region
log_fit_rej = log_fit_pre.copy()
log_fit_rej[300:400] += 4.0
p_rej = np.exp(log_fit_rej); p_rej /= p_rej.sum()
S_rej = float(-np.sum(p_rej * np.log(p_rej)))

# Accelerated (conditional)
log_fit_acc = log_fit_pre.copy()
log_fit_acc[1200:1300] += 3.0
p_acc = np.exp(log_fit_acc); p_acc /= p_acc.sum()
S_acc = float(-np.sum(p_acc * np.log(p_acc)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_appr = itu_lin(p_pre, p_appr)
ratio_pre_rej = itu_lin(p_pre, p_rej)
ratio_pre_acc = itu_lin(p_pre, p_acc)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 234 — FDA + Clinical Trials + Regulation (K_pharma_regulatory)",
    fontsize=13, fontweight="bold",
)

# Panel 1: FDA history
ax = axes[0, 0]
events = list(fda_history.keys())
years = list(fda_history.values())
ax.barh(range(len(events)), years, color="#9467bd")
ax.set_yticks(range(len(events))); ax.set_yticklabels(events, fontsize=7)
ax.set_xlim(1900, 2025)
ax.set_xlabel("Year")
ax.set_title("FDA history milestones")
ax.grid(True, alpha=0.3, axis="x")

# Panel 2: Phase success rates
ax = axes[0, 1]
ph_names = list(phase_rates.keys())
rates = list(phase_rates.values())
colors_p = ["#2ca02c" if r > 0.5 else "#ff7f0e" if r > 0.3 else "#d62728" for r in rates]
ax.barh(range(len(ph_names)), rates, color=colors_p)
ax.set_yticks(range(len(ph_names))); ax.set_yticklabels(ph_names, fontsize=8)
ax.set_xlabel("Success rate")
ax.set_xlim(0, 1)
ax.set_title(f"Pipeline success rates (overall {overall_success*100:.1f}%)")
ax.grid(True, alpha=0.3, axis="x")
for i, r in enumerate(rates):
    ax.text(r + 0.02, i, f"{r*100:.0f}%", va="center", fontsize=8)

# Panel 3: Approval pathways
ax = axes[0, 2]
path_names = list(pathways.keys())
months = [pathways[p]["review_months"] for p in path_names]
ax.bar(path_names, months, color="#1f77b4")
ax.set_ylabel("Review time (months)")
ax.set_title("FDA approval pathways")
ax.tick_params(axis="x", rotation=15, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, m in enumerate(months):
    ax.text(i, m + 0.3, f"{m}mo", ha="center", fontsize=9, fontweight="bold")

# Panel 4: Global agencies
ax = axes[1, 0]
ag_names = list(agencies.keys())
mkt = [agencies[a]["market_pct"] for a in ag_names]
drugs = [agencies[a]["drugs_2024"] for a in ag_names]
x = np.arange(len(ag_names))
width = 0.35
ax.bar(x - width/2, mkt, width, color="#1f77b4", label="Market %")
ax.bar(x + width/2, drugs, width, color="#d62728", label="Drugs approved 2024")
ax.set_xticks(x); ax.set_xticklabels(ag_names, rotation=15, fontsize=7)
ax.set_ylabel("Percent / Count")
ax.set_title("Global regulatory agencies (2024)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Trial types
ax = axes[1, 1]
t_names = list(trial_types.keys())
p_counts = [trial_types[t]["patients"] for t in t_names]
ax.barh(range(len(t_names)), p_counts, color="#ff7f0e")
ax.set_xscale("log")
ax.set_yticks(range(len(t_names))); ax.set_yticklabels(t_names, fontsize=7)
ax.set_xlabel("Patients enrolled (log)")
ax.set_title("Trial types: 50 → 1M patients")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 6: ITU K_pharma_regulatory
ax = axes[1, 2]
ax.bar(["Pre-trial\n(broad)", "Approve\n(decided)", "Reject", "Accelerated\n(conditional)"],
       [S_pre, S_appr, S_rej, S_acc],
       color=["#1f77b4", "#2ca02c", "#d62728", "#ff7f0e"])
ax.set_ylabel("Decision space entropy (nats)")
ax.set_title(f"K_pharma_regulatory: Appr={ratio_pre_appr:.3f}, Rej={ratio_pre_rej:.3f}, Acc={ratio_pre_acc:.3f}")
ax.tick_params(axis="x", labelsize=8)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 234,
    "tier1_paper": 32,
    "topic": "FDA + Clinical trials + Regulation (K_pharma_regulatory)",
    "FDA_milestones": fda_history,
    "phase_success_rates": phase_rates,
    "overall_success_rate_pct": float(overall_success * 100),
    "Phase_II_to_III_bottleneck": 0.30,
    "FDA_approval_pathways": pathways,
    "global_agencies": agencies,
    "trial_types": trial_types,
    "RECOVERY_2020_dexamethasone": "Mortality reduction 35% in COVID severe",
    "All_of_Us_2018_cohort": "1M+ individuals (genome + EHR)",
    "ICH_harmonization": {
        "founded": 1990,
        "members": 17,
        "observers": 33,
        "guidelines": ["Q (Quality)", "S (Safety)", "E (Efficacy)", "M (Multi)"],
    },
    "in_silico_trials": silico_paradigms,
    "ITU_K_pharma_regulatory": {
        "N_decisions": N_decisions,
        "S_pre_trial_nats": S_pre,
        "S_approve_nats": S_appr,
        "S_reject_nats": S_rej,
        "S_accelerated_nats": S_acc,
        "pre_to_approve_ratio": ratio_pre_appr,
        "pre_to_reject_ratio": ratio_pre_rej,
        "pre_to_accelerated_ratio": ratio_pre_acc,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_regulatory",
        "modular_Hamiltonian": "K_pharma_regulatory^(0) = -log P(approval | trial data + risk-benefit)",
        "Phase_II_meaning": "Bottleneck = max K-state uncertainty reduction needed",
        "Master_protocol_meaning": "K-state evidence flow optimization",
        "RECOVERY_2020_significance": "Largest-ever adaptive trial demonstrating speed",
    },
    "predictions": [
        ("FDA AI/ML drug regulatory framework", 2027, 0.80, "Strong"),
        ("Digital twin clinical trial regulatory approval", 2030, 0.65, "Medium"),
        ("Master protocol become standard", 2028, 0.85, "Strong"),
        ("FDA accelerated approval reform", 2026, 0.70, "Strong"),
        ("Global ICH harmonization 30+ members", 2030, 0.75, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
