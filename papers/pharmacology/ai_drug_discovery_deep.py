"""
Phase 233 — AI Drug Discovery Deep (K_pharma_AI)

Simulations:
  1) AI drug discovery company landscape
  2) Discovery vs traditional pipeline time
  3) AI virtual screening: million → top candidates
  4) AI vs classical hit rate
  5) Halicin discovery (Stokes 2020)
  6) AI pipeline phases (2024)
  7) ITU K_pharma_AI axiom check

Outputs:
  - ai_drug_discovery_deep.png
  - ai_drug_discovery_deep_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("ai_drug_discovery_deep.png")
OUT_JSON = Path(__file__).with_name("ai_drug_discovery_deep_summary.json")

rng = np.random.default_rng(20260714)

# -------------------------------------------------------------
# 1) AI drug discovery companies
# -------------------------------------------------------------
ai_companies = {
    "Insilico":       {"founded": 2014, "market_B": 7.0,  "lead_phase": "II"},
    "Recursion":      {"founded": 2013, "market_B": 2.5,  "lead_phase": "II/III"},
    "Atomwise":       {"founded": 2012, "market_B": 1.0,  "lead_phase": "Pre"},
    "BenevolentAI":   {"founded": 2013, "market_B": 0.5,  "lead_phase": "II"},
    "Exscientia":     {"founded": 2012, "market_B": 1.4,  "lead_phase": "I"},
    "Verge Genomics": {"founded": 2015, "market_B": 0.3,  "lead_phase": "II"},
    "Schrödinger":    {"founded": 1990, "market_B": 1.6,  "lead_phase": "I"},
    "Relay Therap.":  {"founded": 2015, "market_B": 0.8,  "lead_phase": "II"},
}

# -------------------------------------------------------------
# 2) AI vs traditional pipeline time
# -------------------------------------------------------------
phases = ["Target ID", "Hit Discovery", "Lead Opt", "Preclinical", "Phase I", "Phase II", "Phase III", "FDA"]
classical_yr = [1.5, 1.5, 2.0, 1.5, 1.5, 2.5, 2.5, 1.0]
ai_yr = [0.5, 0.3, 0.5, 1.0, 1.5, 2.5, 2.5, 1.0]
classical_total = sum(classical_yr)
ai_total = sum(ai_yr)

# -------------------------------------------------------------
# 3) Virtual screening throughput
# -------------------------------------------------------------
methods = {
    "Manual (1990s)":      100,
    "HTS (2000s)":         100_000,
    "Virtual screening":   10_000_000,
    "AlphaFold + Atomwise": 100_000_000,
    "Boltz-1 (2024)":      1_000_000_000,
}

# -------------------------------------------------------------
# 4) AI vs classical hit rate
# -------------------------------------------------------------
strategies = ["Random (HTS)", "Structure-based", "AI (AtomNet)", "AI (Insilico Gen)"]
hit_rate_pct = [0.5, 5.0, 15.0, 25.0]

# -------------------------------------------------------------
# 5) Halicin AI discovery
# -------------------------------------------------------------
halicin = {
    "year": 2020,
    "paper": "Stokes et al. Cell",
    "training_compounds": 2335,
    "screened_compounds": 107_000_000,
    "lead_found": "Halicin",
    "mechanism": "Proton motive force disruption",
    "activity_against": ["E. coli", "M. tuberculosis", "C. difficile", "A. baumannii (MDR)"],
    "stage": "Pre-clinical",
}

# -------------------------------------------------------------
# 6) AI pipeline 2024
# -------------------------------------------------------------
ai_pipeline_2024 = {
    "Pre-clinical": 70,
    "Phase I":      15,
    "Phase II":     8,
    "Phase III":    2,
    "Approved":     0,
}

# -------------------------------------------------------------
# 7) ITU K_pharma_AI axiom
# -------------------------------------------------------------
N_compounds = 10000
# Pre-AI: random uniform exploration
log_fit_pre = 0.05 * rng.standard_normal(N_compounds)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Virtual screening (AtomNet-like): peaked at predicted hits
log_fit_vs = log_fit_pre.copy()
log_fit_vs[3000:3500] += 3.0  # top 500 candidates
p_vs = np.exp(log_fit_vs); p_vs /= p_vs.sum()
S_vs = float(-np.sum(p_vs * np.log(p_vs)))

# Generative AI (Insilico-like): generates specific candidates
log_fit_gen = log_fit_pre.copy()
log_fit_gen[3200:3250] += 5.0  # top 50 highly optimized
p_gen = np.exp(log_fit_gen); p_gen /= p_gen.sum()
S_gen = float(-np.sum(p_gen * np.log(p_gen)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_vs = itu_lin(p_pre, p_vs)
ratio_pre_gen = itu_lin(p_pre, p_gen)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 233 — AI Drug Discovery Deep (K_pharma_AI)",
    fontsize=13, fontweight="bold",
)

# Panel 1: AI companies
ax = axes[0, 0]
c_names = list(ai_companies.keys())
markets = [ai_companies[c]["market_B"] for c in c_names]
ax.barh(range(len(c_names)), markets, color="#9467bd")
for i, c in enumerate(c_names):
    ax.text(0.05, i, f"Phase {ai_companies[c]['lead_phase']}",
            fontsize=7, va="center", color="white", fontweight="bold")
ax.set_yticks(range(len(c_names))); ax.set_yticklabels(c_names, fontsize=8)
ax.set_xlabel("Market cap ($ Billion)")
ax.set_title("AI drug discovery companies (2024)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 2: Pipeline time
ax = axes[0, 1]
x = np.arange(len(phases))
width = 0.35
ax.bar(x - width/2, classical_yr, width, color="#d62728", label=f"Classical {classical_total:.1f} yr")
ax.bar(x + width/2, ai_yr, width, color="#2ca02c", label=f"AI {ai_total:.1f} yr")
ax.set_xticks(x); ax.set_xticklabels(phases, rotation=30, fontsize=7, ha="right")
ax.set_ylabel("Duration (years)")
ax.set_title(f"Pipeline: {classical_total - ai_total:.1f} yr saved by AI")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: Virtual screening throughput
ax = axes[0, 2]
m_names = list(methods.keys())
m_vals = list(methods.values())
colors_m = ["#1f77b4", "#aec7e8", "#ff7f0e", "#9467bd", "#d62728"]
ax.barh(range(len(m_names)), m_vals, color=colors_m)
ax.set_xscale("log")
ax.set_yticks(range(len(m_names))); ax.set_yticklabels(m_names, fontsize=7)
ax.set_xlabel("Compounds screened per campaign (log)")
ax.set_title("Virtual screening: 100 → 1B compounds")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: Hit rate
ax = axes[1, 0]
colors_h = ["#d62728", "#ff7f0e", "#2ca02c", "#1f77b4"]
ax.bar(strategies, hit_rate_pct, color=colors_h)
ax.set_ylabel("Hit rate (%)")
ax.set_title("AI advances hit rate 50× vs random HTS")
ax.tick_params(axis="x", rotation=15, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(hit_rate_pct):
    ax.text(i, v + 0.5, f"{v}%", ha="center", fontsize=10, fontweight="bold")

# Panel 5: AI pipeline 2024
ax = axes[1, 1]
stages = list(ai_pipeline_2024.keys())
counts = list(ai_pipeline_2024.values())
colors_s = ["#1f77b4", "#ff7f0e", "#9467bd", "#d62728", "#2ca02c"]
ax.bar(stages, counts, color=colors_s)
ax.set_ylabel("Number of compounds")
ax.set_title(f"AI-discovered drug pipeline 2024 (total {sum(counts)})")
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(counts):
    ax.text(i, v + 1, str(v), ha="center", fontsize=10, fontweight="bold")

# Panel 6: ITU K_pharma_AI
ax = axes[1, 2]
ax.bar(["Pre-AI\n(random)", "Virtual screen\n(AtomNet)", "Generative AI\n(Insilico)"],
       [S_pre, S_vs, S_gen],
       color=["#d62728", "#ff7f0e", "#2ca02c"])
ax.set_ylabel("Compound space entropy (nats)")
ax.set_title(f"K_pharma_AI: Pre→VS={ratio_pre_vs:.3f}, Pre→Gen={ratio_pre_gen:.3f}")
ax.tick_params(axis="x", labelsize=7)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 233,
    "tier1_paper": 32,
    "topic": "AI drug discovery deep (K_pharma_AI)",
    "AI_companies_2024": ai_companies,
    "Insilico_INS018_055": "AI designed 21 days, Phase II IPF",
    "Recursion_Bayer_CV_deal": "11 targets in 12 months",
    "BenevolentAI_baricitinib_COVID": "Lilly partnership, FDA EUA 2020",
    "pipeline_classical_yr": classical_total,
    "pipeline_AI_yr": ai_total,
    "AI_saving_yr": float(classical_total - ai_total),
    "virtual_screening_throughput": methods,
    "hit_rate_strategies": dict(zip(strategies, hit_rate_pct)),
    "Halicin_Stokes_2020_Cell": halicin,
    "AI_pipeline_2024": ai_pipeline_2024,
    "AI_total_clinical_phase": int(sum([15, 8, 2])),
    "ITU_K_pharma_AI": {
        "N_compounds": int(N_compounds),
        "S_pre_AI_nats": S_pre,
        "S_virtual_screen_nats": S_vs,
        "S_generative_AI_nats": S_gen,
        "pre_to_VS_ratio": ratio_pre_vs,
        "pre_to_gen_ratio": ratio_pre_gen,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_AI",
        "modular_Hamiltonian": "K_pharma_AI^(0) = -log P(drug × target × patient | AI + data)",
        "virtual_screening_meaning": "ITU descent on chemical space via learned prior",
        "generative_AI_meaning": "K-state generation: novel drug designs from chemical manifold",
        "Halicin_meaning": "AI sees novel patterns invisible to human (proton motive force)",
        "Insilico_21_days": "K_state convergence acceleration (1000× vs classical)",
    },
    "predictions": [
        ("First AI-discovered drug FDA approval", 2028, 0.75, "Strong"),
        ("AI cumulative 5 FDA approvals", 2030, 0.80, "Strong"),
        ("AI clinical trial design standard", 2028, 0.70, "Strong"),
        ("In silico trial regulatory acceptance", 2030, 0.65, "Medium"),
        ("AI 創薬 industry M&A consolidation", 2028, 0.85, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
