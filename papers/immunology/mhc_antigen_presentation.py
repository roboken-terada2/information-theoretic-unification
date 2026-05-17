"""
Phase 185 — MHC + antigen presentation + peptide-MHC binding

Simulations:
  1) Class I vs Class II peptide length distributions
  2) HLA allelic diversity (IPD-IMGT 2024)
  3) Binding affinity Kd distribution (NetMHCpan-like log-normal)
  4) Anchor residue contribution to binding energy
  5) Class I antigen processing: chymotryptic cleavage C-terminus
  6) Peptide-MHC half-life vs Kd
  7) ITU K_MHC^(0) check on synthetic HLA peptidome
  8) HLA disease association odds-ratio sketch

Outputs:
  - mhc_antigen_presentation.png
  - mhc_antigen_presentation_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("mhc_antigen_presentation.png")
OUT_JSON = Path(__file__).with_name("mhc_antigen_presentation_summary.json")

rng = np.random.default_rng(20260519)

# -------------------------------------------------------------
# 1) Class I vs Class II peptide length
# -------------------------------------------------------------
class_I_aa = np.arange(7, 13)
class_I_pdf = np.array([0.02, 0.10, 0.65, 0.20, 0.02, 0.01])  # peaked at 9
class_II_aa = np.arange(11, 28)
class_II_pdf_raw = np.exp(-0.5 * ((class_II_aa - 16.0) / 3.0) ** 2)
class_II_pdf = class_II_pdf_raw / class_II_pdf_raw.sum()

# -------------------------------------------------------------
# 2) HLA allelic diversity (IPD-IMGT/HLA 2024 release)
# -------------------------------------------------------------
hla = {
    "HLA-A": 8500,
    "HLA-B": 10500,
    "HLA-C": 8000,
    "HLA-DRB1": 4500,
    "HLA-DQB1": 2800,
    "HLA-DPB1": 1500,
}
hla_total = sum(hla.values())

# -------------------------------------------------------------
# 3) Binding affinity Kd log-normal (NetMHCpan-like)
# -------------------------------------------------------------
# Strong binders: 1-50 nM; weak: 50-500 nM; non: > 500 nM
log10_Kd_nM = rng.normal(loc=2.8, scale=1.2, size=100_000)  # mean ~600 nM, sigma 1.2 decades
Kd_nM = 10 ** log10_Kd_nM

strong = (Kd_nM < 50)
weak = (Kd_nM >= 50) & (Kd_nM < 500)
non = (Kd_nM >= 500)

strong_frac = float(strong.mean())
weak_frac = float(weak.mean())
non_frac = float(non.mean())

# Estimate: 0.5-1% of all 9mers from a typical proteome bind a given HLA
# Human proteome ~20,000 proteins x ~350 aa avg = 7e6 unique 9mers
human_proteome_9mers = 7_000_000
binding_per_HLA = int(human_proteome_9mers * strong_frac)

# -------------------------------------------------------------
# 4) Anchor residue contributions (kcal/mol)
# -------------------------------------------------------------
# Position-specific contributions for HLA-A*02:01 9mer:
# P2 (Leu/Met preferred): -3.5 kcal/mol
# P9 (Val/Leu/Ile preferred): -3.0 kcal/mol
# Center positions: -0.5 to -1.5 each
positions = np.arange(1, 10)
A0201_contrib = np.array([-1.0, -3.5, -0.8, -0.5, -1.0, -0.8, -1.0, -0.5, -3.0])
total_dG = float(A0201_contrib.sum())
# Kd from ΔG = -RT ln Ka => Kd ~ exp(ΔG / RT)
RT_kcal = 0.593  # kcal/mol at 298 K
Kd_predicted_M = np.exp(total_dG / RT_kcal)

# -------------------------------------------------------------
# 5) Class I cleavage C-terminus residue frequencies (proteasome)
# -------------------------------------------------------------
aa_labels = list("ARNDCEQGHILKMFPSTWYV")
# Chymotryptic preference: F/W/Y/L > others
C_term_freqs = {a: 0.04 for a in aa_labels}
C_term_freqs["L"] = 0.18
C_term_freqs["F"] = 0.12
C_term_freqs["Y"] = 0.10
C_term_freqs["W"] = 0.06
C_term_freqs["V"] = 0.10
C_term_freqs["I"] = 0.08
# Normalize
s = sum(C_term_freqs.values())
C_term_freqs = {a: f / s for a, f in C_term_freqs.items()}

# -------------------------------------------------------------
# 6) Peptide-MHC half-life vs Kd
# -------------------------------------------------------------
# Empirical relation: t_1/2 ~ k * (1 / k_off)
# Strong binder Kd 5 nM -> t_1/2 ~ 24 hr; weak Kd 5 μM -> t_1/2 ~ 30 sec
Kd_grid_nM = np.logspace(0, 4, 50)
# log10(t_1/2 in sec) approx 5.5 - 1.2 * log10(Kd nM)
t_half_sec = 10 ** (5.5 - 1.2 * np.log10(Kd_grid_nM))

# -------------------------------------------------------------
# 7) ITU K_MHC^(0) — synthetic peptidome
# -------------------------------------------------------------
# Sample N peptides with affinities log-normal
N = 50_000
log_Kd = rng.normal(2.5, 1.0, size=N)  # mean ~316 nM
# Binding probability ~ exp(-Kd / Kd_ref)
Kd_ref_nM = 100
prob_bind = np.exp(-(10 ** log_Kd) / Kd_ref_nM)
prob_bind = prob_bind / prob_bind.sum()

S_MHC = float(-np.sum(prob_bind * np.log(prob_bind)))
K_MHC = -np.log(prob_bind)
mean_K_MHC = float(np.sum(prob_bind * K_MHC))
# Check: should equal S_MHC
itu_consistency = abs(mean_K_MHC - S_MHC) / S_MHC

# Negative selection: zero out 5% (self peptides)
self_mask = rng.random(N) < 0.05
prob_post_select = prob_bind.copy()
prob_post_select[self_mask] = 0
prob_post_select = prob_post_select / prob_post_select.sum()
S_post = float(-np.sum(np.where(prob_post_select > 0, prob_post_select * np.log(prob_post_select), 0)))

# ITU linearized check
K0_fixed = -np.log(np.clip(prob_bind, 1e-30, None))
delta_p = prob_post_select - prob_bind
dS_1 = float(-np.sum(np.where(prob_bind > 0, delta_p * (1.0 + np.log(prob_bind)), 0)))
dK_1 = float(np.sum(delta_p * K0_fixed))
itu_ratio = dS_1 / dK_1 if abs(dK_1) > 1e-15 else float("nan")

# -------------------------------------------------------------
# 8) HLA disease association odds ratios
# -------------------------------------------------------------
disease_assoc = {
    "HLA-B*51 / HIV slow progression": 0.4,
    "HLA-B*53 / Malaria protection": 0.6,
    "HLA-DRB1*15:01 / Multiple sclerosis": 3.0,
    "HLA-DR2 / SLE": 2.5,
    "HLA-B*27 / Ankylosing spondylitis": 87.0,
    "HLA-DQ2/DQ8 / Celiac disease": 19.0,
}

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 185 — MHC + Antigen Presentation + Peptide-MHC Binding (K_MHC)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Class I vs II peptide length
ax = axes[0, 0]
ax.bar(class_I_aa, class_I_pdf, color="#1f77b4", alpha=0.8, label="MHC I (CD8)  8-10 aa")
ax.bar(class_II_aa, class_II_pdf, color="#ff7f0e", alpha=0.7, label="MHC II (CD4)  13-25 aa")
ax.set_xlabel("Peptide length (aa)")
ax.set_ylabel("Probability")
ax.set_title("Class I (closed) vs Class II (open) peptide grooves")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: HLA allelic diversity (IPD-IMGT 2024)
ax = axes[0, 1]
labels = list(hla.keys())
counts = list(hla.values())
colors = ["#1f77b4", "#aec7e8", "#a6cee3", "#ff7f0e", "#ffbb78", "#fdd0a2"]
ax.bar(labels, counts, color=colors)
ax.set_ylabel("Allele count (IPD-IMGT 2024)")
ax.set_title(f"HLA allelic diversity — total {hla_total:,}")
ax.tick_params(axis="x", rotation=20)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: Kd distribution
ax = axes[0, 2]
ax.hist(np.log10(Kd_nM), bins=60, color="#9467bd", alpha=0.7, edgecolor="black")
ax.axvline(np.log10(50), color="green", linestyle="--", lw=2,
           label=f"Strong ≤ 50 nM ({strong_frac*100:.1f}%)")
ax.axvline(np.log10(500), color="orange", linestyle="--", lw=2,
           label=f"Weak ≤ 500 nM ({weak_frac*100:.1f}%)")
ax.set_xlabel("log10(Kd / nM)")
ax.set_ylabel("Peptide count")
ax.set_title("Peptide-MHC binding affinity (NetMHCpan-like)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Anchor residue contributions
ax = axes[1, 0]
colors_p = ["#d62728" if c < -2 else "#1f77b4" for c in A0201_contrib]
ax.bar(positions, A0201_contrib, color=colors_p)
ax.axhline(0, color="black", lw=0.5)
ax.set_xlabel("Peptide position (HLA-A*02:01 9mer)")
ax.set_ylabel("ΔG contribution (kcal/mol)")
ax.set_title(f"Anchor residues: P2 + P9 ; Σ ΔG = {total_dG:.1f}; Kd≈{Kd_predicted_M*1e9:.1f} nM")
ax.set_xticks(positions)
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Peptide-MHC half-life
ax = axes[1, 1]
ax.loglog(Kd_grid_nM, t_half_sec, "-", color="#2ca02c", lw=2)
ax.axhline(60, color="orange", linestyle="--", alpha=0.5, label="1 min")
ax.axhline(3600, color="red", linestyle="--", alpha=0.5, label="1 hr")
ax.axhline(86400, color="purple", linestyle="--", alpha=0.5, label="1 day")
ax.set_xlabel("Kd (nM)")
ax.set_ylabel("t_1/2 (sec)")
ax.set_title("Peptide-MHC dissociation half-life")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 6: ITU K_MHC + Disease OR
ax = axes[1, 2]
diseases = list(disease_assoc.keys())
ors = list(disease_assoc.values())
colors_d = ["#2ca02c" if o < 1 else "#d62728" for o in ors]
ax.barh(range(len(diseases)), ors, color=colors_d)
ax.axvline(1.0, color="black", linestyle="--", alpha=0.5, label="OR = 1")
ax.set_xscale("log")
ax.set_yticks(range(len(diseases)))
ax.set_yticklabels(diseases, fontsize=7)
ax.set_xlabel("Odds ratio (log scale)")
ax.set_title(f"HLA disease assoc.;  K_MHC ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.legend(fontsize=8, loc="lower right")
ax.grid(True, alpha=0.3, axis="x", which="both")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 185,
    "tier1_paper": 26,
    "block": "B",
    "topic": "MHC + antigen presentation + peptide-MHC binding (K_MHC)",
    "class_I": {
        "peptide_length_range": "8-10 aa",
        "peak_aa": 9,
        "binding_pocket": "closed groove (both termini fixed)",
        "T_cell": "CD8+ cytotoxic",
        "processing": "proteasome + TAP transporter",
    },
    "class_II": {
        "peptide_length_range": "13-25 aa",
        "peak_aa": 16,
        "binding_pocket": "open groove (termini overhang)",
        "T_cell": "CD4+ helper",
        "processing": "endosomal + cathepsin + HLA-DM",
    },
    "HLA_alleles_IPD_IMGT_2024": hla,
    "HLA_total_alleles": int(hla_total),
    "binding_affinity_distribution": {
        "strong_pct": strong_frac * 100,
        "weak_pct": weak_frac * 100,
        "non_pct": non_frac * 100,
        "strong_threshold_nM": 50,
        "weak_threshold_nM": 500,
        "human_proteome_9mers": int(human_proteome_9mers),
        "estimated_binders_per_HLA": int(binding_per_HLA),
    },
    "anchor_residues_A0201_9mer": {
        "positions_kcal_per_mol": A0201_contrib.tolist(),
        "total_dG_kcal_per_mol": total_dG,
        "predicted_Kd_nM": Kd_predicted_M * 1e9,
        "P2_anchor_kcal": -3.5,
        "P9_anchor_kcal": -3.0,
    },
    "C_terminus_cleavage_freq": C_term_freqs,
    "half_life_example_nM_to_sec": {
        "Kd_5_nM_strong": float(10 ** (5.5 - 1.2 * np.log10(5))),
        "Kd_5000_nM_weak": float(10 ** (5.5 - 1.2 * np.log10(5000))),
    },
    "ITU_K_MHC": {
        "N_peptides": N,
        "Shannon_S_nats": S_MHC,
        "mean_K_MHC_nats": mean_K_MHC,
        "S_K_consistency": float(itu_consistency),
        "S_after_negative_selection": S_post,
        "delta_S_first_order": dS_1,
        "delta_K_first_order": dK_1,
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "HLA_disease_associations": disease_assoc,
    "ITU_interpretation": {
        "K_state": "K_MHC (sub-state of K_immune)",
        "modular_Hamiltonian": "K_MHC^(0) = -log P(peptide | HLA)",
        "negative_selection": "Thymic deletion of self-pMHC reactive T cells = local zero set",
        "HLA_heterozygosity": "Multi-dimensional K_MHC^(0) → multi-pathogen coverage",
        "holes_in_repertoire": "Per-individual K_MHC zero-measure subset = immune blind spots",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
