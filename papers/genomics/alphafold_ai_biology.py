"""
Phase 217 — AlphaFold + Computational Biology + AI Drug Discovery (K_genome_AI)

Simulations:
  1) AlphaFold CASP performance history (1998-2020)
  2) AlphaFold DB growth (350K → 200M structures)
  3) Protein folding "Levinthal paradox" computational scale
  4) AI drug discovery pipeline acceleration
  5) Baker lab de novo proteins count
  6) AI startup landscape (Insilico, Exscientia, etc.)
  7) ITU K_genome_AI axiom check: sequence → structure

Outputs:
  - alphafold_ai_biology.png
  - alphafold_ai_biology_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("alphafold_ai_biology.png")
OUT_JSON = Path(__file__).with_name("alphafold_ai_biology_summary.json")

rng = np.random.default_rng(20260627)

# -------------------------------------------------------------
# 1) CASP performance (GDT_TS)
# -------------------------------------------------------------
casp_history = {
    "CASP3 (1998)":  35,
    "CASP5 (2002)":  40,
    "CASP7 (2006)":  45,
    "CASP9 (2010)":  55,
    "CASP11 (2014)": 60,
    "CASP12 (2016)": 65,
    "CASP13 (2018) - AF1 ★": 70,
    "CASP14 (2020) - AF2 ★★": 92.4,
    "CASP15 (2022) - AF3-era": 91,
}

# -------------------------------------------------------------
# 2) AlphaFold DB growth
# -------------------------------------------------------------
af_db_dates = {
    "2021-07": 0.35e6,
    "2021-11": 1.0e6,
    "2022-07": 200e6,
    "2024-01": 214e6,
    "2024-12": 250e6,
}

# -------------------------------------------------------------
# 3) Levinthal paradox computational scale
# -------------------------------------------------------------
# A 100-residue protein with 3 conformations per residue → 3^100 ≈ 5e47
# At 10^14 conformations/sec (femtosecond), still > 10^33 universe ages
n_residues_range = np.arange(20, 200, 10)
conformations = 3 ** n_residues_range
fold_time_universe_ages = conformations / (1e14 * 4.4e17)  # > 1 = unfeasible

# -------------------------------------------------------------
# 4) AI drug discovery pipeline
# -------------------------------------------------------------
classic_phases = {
    "Target ID":              4.0,
    "Hit discovery":          3.0,
    "Lead optimization":      2.5,
    "Preclinical":            1.5,
    "Phase I":                1.5,
    "Phase II":               2.5,
    "Phase III":              2.5,
    "FDA review":             1.0,
}
classic_total = sum(classic_phases.values())

ai_phases = {
    "Target ID":              1.0,   # AI accelerated
    "Hit discovery":          0.5,
    "Lead optimization":      0.5,
    "Preclinical":            1.0,
    "Phase I":                1.5,
    "Phase II":               2.5,
    "Phase III":              2.5,
    "FDA review":             1.0,
}
ai_total = sum(ai_phases.values())

# -------------------------------------------------------------
# 5) Baker lab de novo proteins
# -------------------------------------------------------------
baker_milestones = {
    "Top7 (2003)":               {"year": 2003, "type": "First de novo fold"},
    "Spy-Tag/SpyCatcher (2012)": {"year": 2012, "type": "Bio-conjugation"},
    "Influenza binders (2014)":  {"year": 2014, "type": "Binder design"},
    "Designed enzymes":          {"year": 2018, "type": "Enzyme design"},
    "COVID-19 vaccine (SpyTag)": {"year": 2020, "type": "Vaccine"},
    "ProteinMPNN":               {"year": 2022, "type": "Inverse folding"},
    "Snake venom designers":     {"year": 2024, "type": "Therapeutic binders"},
}

# -------------------------------------------------------------
# 6) AI drug companies
# -------------------------------------------------------------
ai_companies = {
    "Insilico Medicine\n(INS018_055)":    {"phase": "II",  "indication": "IPF"},
    "Exscientia\n(EXS-21546)":             {"phase": "I",   "indication": "Immuno-onc"},
    "BenevolentAI\n(BEN-2293)":             {"phase": "II",  "indication": "Atopic"},
    "Recursion\n(REC-994)":                {"phase": "III", "indication": "CCM"},
    "Atomwise":                            {"phase": "Pre", "indication": "Multiple"},
}

# -------------------------------------------------------------
# 7) ITU K_genome_AI axiom check
# -------------------------------------------------------------
# Pre-AlphaFold: sequence space large, structure unknown (high uncertainty)
# Post-AlphaFold: tight mapping sequence → structure (low uncertainty)
N_proteins = 5000
# Pre: broad p over structure candidates
log_fit_pre = np.zeros(N_proteins) + 0.5 * rng.standard_normal(N_proteins)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Post: AlphaFold collapses to single structure (high confidence)
log_fit_post = log_fit_pre.copy()
log_fit_post[2500] += 5.0  # AF prediction peak
p_post = np.exp(log_fit_post); p_post /= p_post.sum()
S_post = float(-np.sum(p_post * np.log(p_post)))

# AI-designed (Baker): inverse - sequence design for target structure
# Custom probability for chosen functional design
log_fit_design = log_fit_pre.copy()
log_fit_design[1500] += 4.0  # designed target
p_design = np.exp(log_fit_design); p_design /= p_design.sum()
S_design = float(-np.sum(p_design * np.log(p_design)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_post = itu_lin(p_pre, p_post)
ratio_pre_design = itu_lin(p_pre, p_design)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 217 — AlphaFold + Computational Biology + AI Drug Discovery (K_genome_AI)",
    fontsize=13, fontweight="bold",
)

# Panel 1: CASP history
ax = axes[0, 0]
casps = list(casp_history.keys())
gdt = list(casp_history.values())
colors_c = ["#d62728" if "AF" in c else "#1f77b4" for c in casps]
ax.bar(range(len(casps)), gdt, color=colors_c)
ax.axhline(90, color="green", linestyle="--", lw=2, label="Experimental accuracy ~90")
ax.set_xticks(range(len(casps)))
ax.set_xticklabels(casps, rotation=30, fontsize=7, ha="right")
ax.set_ylabel("GDT_TS")
ax.set_title("CASP history: AlphaFold solves 50-yr problem")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 2: AlphaFold DB growth
ax = axes[0, 1]
af_dates = list(af_db_dates.keys())
af_counts = list(af_db_dates.values())
ax.semilogy(range(len(af_dates)), af_counts, "o-", color="#9467bd", lw=2, markersize=10)
ax.set_xticks(range(len(af_dates)))
ax.set_xticklabels(af_dates, rotation=20, fontsize=8)
ax.set_ylabel("Structures (log)")
ax.set_title("AlphaFold DB: 350K → 250M in 3 years")
ax.grid(True, alpha=0.3, which="both")

# Panel 3: Levinthal paradox
ax = axes[0, 2]
ax.semilogy(n_residues_range, conformations, "-", color="#1f77b4", lw=2,
            label="Conformations (3^N)")
ax.axhline(4.4e17 * 1e14, color="red", linestyle="--",
           label="Universe age × 10^14/s")
ax.set_xlabel("Protein length (residues)")
ax.set_ylabel("Conformations (log)")
ax.set_title("Levinthal paradox: too many to sample (Levinthal 1969)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 4: Drug discovery: classic vs AI
ax = axes[1, 0]
phases = list(classic_phases.keys())
classic_yrs = list(classic_phases.values())
ai_yrs = list(ai_phases.values())
x = np.arange(len(phases))
width = 0.35
ax.bar(x - width/2, classic_yrs, width, color="#d62728", label=f"Classic (total {classic_total} yr)")
ax.bar(x + width/2, ai_yrs, width, color="#2ca02c", label=f"AI-accelerated (total {ai_total} yr)")
ax.set_xticks(x)
ax.set_xticklabels(phases, rotation=30, fontsize=7, ha="right")
ax.set_ylabel("Duration (years)")
ax.set_title(f"Drug discovery: {classic_total - ai_total:.1f} yr saved")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Baker timeline
ax = axes[1, 1]
b_names = list(baker_milestones.keys())
b_years = [baker_milestones[k]["year"] for k in b_names]
ax.barh(range(len(b_names)), b_years, color="#9467bd")
ax.set_yticks(range(len(b_names))); ax.set_yticklabels(b_names, fontsize=7)
ax.set_xlim(2002, 2026)
ax.set_title("Baker lab: 20 yr de novo protein design (Nobel 2024)")
ax.set_xlabel("Year")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ITU K_genome_AI
ax = axes[1, 2]
ax.bar(["Pre-AlphaFold\n(broad)", "Post-AF\nprediction", "Baker design\n(target)"],
       [S_pre, S_post, S_design], color=["#d62728", "#2ca02c", "#9467bd"])
ax.set_ylabel("Structure space entropy (nats)")
ax.set_title(f"K_genome_AI: Pre→AF={ratio_pre_post:.3f}, Pre→Design={ratio_pre_design:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 217,
    "tier1_paper": 30,
    "block": "B",
    "topic": "AlphaFold + Computational Biology + AI Drug Discovery (K_genome_AI)",
    "AlphaFold_history": {
        "AF1_2018_CASP13": "Top 1 in 43/90 targets, breakthrough",
        "AF2_2020_CASP14": "GDT_TS 92.4, atom-level accuracy",
        "AF3_2024_Nature": "Multi-molecular complexes (DNA/RNA/ligand)",
        "AlphaFold_DB_2022": "200 M structures (all life proteome)",
    },
    "CASP_history": casp_history,
    "AlphaFold_DB_growth": af_db_dates,
    "Nobel_Chemistry_2024": {
        "winners": ["David Baker", "Demis Hassabis", "John Jumper"],
        "topic": "Computational protein structure prediction + design",
        "Baker_contribution": "Rosetta + de novo design + ProteinMPNN",
        "Hassabis_Jumper_contribution": "AlphaFold 1/2/3",
    },
    "Levinthal_paradox_1969": {
        "statement": "Random folding would take longer than universe age",
        "resolution": "AlphaFold AI sidesteps brute force search",
        "implication": "ITU descent flow tractable via learned priors",
    },
    "Baker_lab_de_novo_proteins": baker_milestones,
    "AI_drug_discovery_timeline": {
        "classic_total_years": classic_total,
        "AI_accelerated_years": ai_total,
        "years_saved": classic_total - ai_total,
    },
    "AI_drug_companies_2024": ai_companies,
    "Insilico_INS018_055": {
        "AI_design_time_days": 21,
        "indication": "Idiopathic Pulmonary Fibrosis (IPF)",
        "phase_2024": "II",
        "significance": "First AI-designed AND AI-validated drug in clinical trial",
    },
    "ITU_K_genome_AI": {
        "N_proteins": N_proteins,
        "S_pre_AlphaFold_nats": S_pre,
        "S_post_AlphaFold_nats": S_post,
        "S_design_nats": S_design,
        "pre_to_post_ratio": ratio_pre_post,
        "pre_to_design_ratio": ratio_pre_design,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_genome_AI",
        "modular_Hamiltonian": "K_genome_AI^(0) = -log P(structure | sequence) with AI prior",
        "AlphaFold_meaning": "ITU descent acceleration via learned priors",
        "ProteinMPNN_meaning": "Inverse K-state mapping (structure → sequence)",
        "AI_drug_discovery_meaning": "K_drug-target interaction tractable via ML",
        "Nobel_2024_significance": "AI-augmented ITU enters Nobel-level science",
    },
    "predictions": [
        ("AlphaFold 4 / Boltz RNA + dynamics", 2027, 0.80, "Strong"),
        ("Insilico INS018_055 Phase III complete", 2028, 0.65, "Medium"),
        ("AI-designed antibody therapy approved", 2028, 0.75, "Strong"),
        ("Computational enzyme design industrialized", 2030, 0.70, "Strong"),
        ("De novo protein → new drug (FDA approved)", 2030, 0.65, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
