"""
Phase 183 — Innate + Adaptive immunity + K_immune introduction

Simulations:
  1) Innate immunity: PRR pattern recognition + cytokine cascade
  2) Adaptive immunity: V(D)J combinatorial diversity
  3) Affinity maturation toy model (somatic hypermutation + clonal selection)
  4) Basic reproduction number R_0 across major pathogens
  5) MHC class I/II peptide length distributions
  6) Cytokine storm dynamics (IL-6 in severe COVID-19 vs healthy)
  7) ITU K_immune^(0) modular Hamiltonian sanity check on synthetic repertoire ρ

Outputs:
  - innate_adaptive_immunity.png
  - innate_adaptive_immunity_summary.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("innate_adaptive_immunity.png")
OUT_JSON = Path(__file__).with_name("innate_adaptive_immunity_summary.json")

rng = np.random.default_rng(20260517)

# -------------------------------------------------------------
# 1) V(D)J combinatorial diversity (Tonegawa 1976, Nobel 1987)
# -------------------------------------------------------------
# Human TCR-beta: ~52 V, 2 D, 13 J segments + junctional diversity
# Human BCR heavy chain: ~38-46 V, ~23 D, 6 J + SHM
TCR_V, TCR_D, TCR_J = 52, 2, 13
BCR_V, BCR_D, BCR_J = 40, 23, 6

# Combinatorial baseline (no junctional, no pairing)
tcr_alpha_pairing_V, tcr_alpha_pairing_J = 70, 61  # TRA segments
bcr_light_V, bcr_light_J = 70, 5  # IGK/IGL

# Heavy chain combinatorial
tcr_beta_comb = TCR_V * TCR_D * TCR_J
bcr_heavy_comb = BCR_V * BCR_D * BCR_J

# αβ-paired TCR repertoire (germline)
tcr_paired_germline = (TCR_V * TCR_D * TCR_J) * (tcr_alpha_pairing_V * tcr_alpha_pairing_J)
# Heavy+Light BCR germline
bcr_paired_germline = (BCR_V * BCR_D * BCR_J) * (bcr_light_V * bcr_light_J)

# Junctional diversity (P/N nucleotide additions): ~10^7-10^9 multiplier
junctional_factor = 1e7

tcr_total = tcr_paired_germline * junctional_factor
bcr_total_germline = bcr_paired_germline * junctional_factor
# Somatic hypermutation (SHM): additional 10^3-10^7 diversification post-germinal center
shm_factor = 1e5
bcr_total_post_shm = bcr_total_germline * shm_factor

# -------------------------------------------------------------
# 2) Affinity maturation toy model
# -------------------------------------------------------------
# Iterative clonal selection: each round picks top fraction, mutates,
# Kd shrinks roughly geometrically by factor q per round
rounds = np.arange(0, 11)
Kd0 = 1e-4  # initial 100 μM (germline)
q = 0.4  # ~2.5× improvement per round
Kd = Kd0 * q**rounds  # final ~6 × 10^-9 M = nM

# -------------------------------------------------------------
# 3) Pathogen R_0
# -------------------------------------------------------------
pathogens = {
    "Measles": 15.0,
    "Pertussis": 13.0,
    "Mumps": 6.0,
    "Smallpox": 5.5,
    "SARS-CoV-2 (Omicron)": 9.5,
    "SARS-CoV-2 (Wild)": 3.0,
    "Influenza (1918)": 2.5,
    "Influenza (seasonal)": 1.3,
    "Ebola": 1.8,
    "MERS": 0.7,
}

# -------------------------------------------------------------
# 4) MHC peptide length distributions
# -------------------------------------------------------------
# MHC class I: 8-10 aa; MHC class II: 13-25 aa
mhc1_lengths = np.array([8, 9, 10])
mhc1_probs = np.array([0.10, 0.65, 0.25])  # peaked at 9
mhc2_lengths = np.arange(13, 26)
# Gaussian-like centered at 15-17
mhc2_probs_raw = np.exp(-0.5 * ((mhc2_lengths - 16) / 2.2) ** 2)
mhc2_probs = mhc2_probs_raw / mhc2_probs_raw.sum()

# -------------------------------------------------------------
# 5) Cytokine storm dynamics (IL-6, days post-infection severe COVID)
# -------------------------------------------------------------
days = np.linspace(0, 21, 200)
healthy_il6 = 2.0 + 1.5 * rng.standard_normal(len(days)) * 0.0  # ~2 pg/mL flat
# Severe COVID: ramp 0-7 days, peak 1500 pg/mL day 8-10, decline
severe_il6 = 5.0 + 1495 * np.exp(-((days - 9.0) ** 2) / (2 * 2.0**2))
mod_il6 = 5.0 + 80 * np.exp(-((days - 7.0) ** 2) / (2 * 3.0**2))

# -------------------------------------------------------------
# 6) ITU K_immune^(0) modular Hamiltonian sanity check
# -------------------------------------------------------------
# Synthetic repertoire density: 1000 clones with power-law abundance (Hill-like)
N_clones = 1000
ranks = np.arange(1, N_clones + 1)
alpha_pl = 1.2
p = ranks ** (-alpha_pl)
p = p / p.sum()
# Shannon entropy (nats)
S_repertoire = -np.sum(p * np.log(p))
# K^(0) per clone = -log p
K0 = -np.log(p)
mean_K0 = np.sum(p * K0)  # = S by construction
# Variation under p -> p + δp (normalized): δS ≈ δ<K^(0)>
delta_p = rng.standard_normal(N_clones) * 1e-4
delta_p = delta_p - delta_p.mean()  # keep sum 0
p_new = p + delta_p
# Project to simplex (clip and renormalize)
p_new = np.clip(p_new, 1e-12, None)
p_new = p_new / p_new.sum()
S_new = -np.sum(p_new * np.log(p_new))
dS = S_new - S_repertoire
dK = np.sum((p_new - p) * K0)
itu_ratio = dS / dK if abs(dK) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 183 — Innate + Adaptive Immunity + K_immune introduction (Tier 1 #26, Block B 1/?)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: V(D)J diversity bar chart
ax = axes[0, 0]
labels = [
    "TCRβ\ncombinatorial",
    "BCR-H\ncombinatorial",
    "TCR αβ\npaired+junctional",
    "BCR germline\npaired+junctional",
    "BCR post-SHM",
]
values = [tcr_beta_comb, bcr_heavy_comb, tcr_total, bcr_total_germline, bcr_total_post_shm]
ax.bar(range(len(labels)), values, color=["#1f77b4", "#aec7e8", "#2ca02c", "#98df8a", "#d62728"])
ax.set_yscale("log")
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=20, fontsize=8)
ax.set_ylabel("Repertoire diversity")
ax.set_title("V(D)J diversity (Tonegawa 1976, Nobel 1987)")
ax.grid(True, alpha=0.3, which="both")

# Panel 2: Affinity maturation Kd over rounds
ax = axes[0, 1]
ax.semilogy(rounds, Kd, "o-", color="#9467bd", lw=2)
ax.set_xlabel("Selection rounds")
ax.set_ylabel("Kd  (M)")
ax.set_title(f"Affinity maturation: Kd 10⁻⁴ → 10⁻{int(-np.log10(Kd[-1]))}")
ax.grid(True, alpha=0.3, which="both")

# Panel 3: R_0 by pathogen
ax = axes[0, 2]
names = list(pathogens.keys())
r0s = list(pathogens.values())
colors = ["#d62728" if r > 5 else "#ff7f0e" if r > 2 else "#2ca02c" for r in r0s]
ax.barh(range(len(names)), r0s, color=colors)
ax.axvline(1.0, color="black", linestyle="--", alpha=0.5, label="R₀ = 1")
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=8)
ax.set_xlabel("R₀  (basic reproduction number)")
ax.set_title("Pathogen R₀")
ax.legend(loc="lower right", fontsize=8)
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: MHC peptide lengths
ax = axes[1, 0]
ax.bar(mhc1_lengths, mhc1_probs, color="#1f77b4", alpha=0.8, label="MHC class I (CD8)")
ax.bar(mhc2_lengths, mhc2_probs, color="#ff7f0e", alpha=0.6, label="MHC class II (CD4)")
ax.set_xlabel("Peptide length (aa)")
ax.set_ylabel("Probability")
ax.set_title("MHC peptide length distributions")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Cytokine storm
ax = axes[1, 1]
ax.semilogy(days, np.full_like(days, 2.0), "-", color="#2ca02c", lw=2, label="Healthy ~2 pg/mL")
ax.semilogy(days, mod_il6, "-", color="#ff7f0e", lw=2, label="Moderate COVID-19")
ax.semilogy(days, severe_il6, "-", color="#d62728", lw=2, label="Severe COVID-19 (storm)")
ax.axhline(10, color="black", linestyle="--", alpha=0.4, label="Clinical threshold 10")
ax.set_xlabel("Days post-infection")
ax.set_ylabel("IL-6  (pg/mL, log)")
ax.set_title("Cytokine storm dynamics")
ax.legend(fontsize=8, loc="upper right")
ax.grid(True, alpha=0.3, which="both")

# Panel 6: K_immune^(0) repertoire + ITU check
ax = axes[1, 2]
ax.loglog(ranks, p, ".", color="#1f77b4", markersize=4, label="Clone abundance p_i ∝ r^-1.2")
ax2 = ax.twinx()
ax2.semilogx(ranks, K0, "-", color="#d62728", lw=1.5, label="K⁽⁰⁾ = -log p_i")
ax.set_xlabel("Clone rank")
ax.set_ylabel("Abundance p_i", color="#1f77b4")
ax2.set_ylabel("K⁽⁰⁾  (nats)", color="#d62728")
ax.set_title(f"K_immune⁽⁰⁾ + ITU axiom check: δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.grid(True, alpha=0.3, which="both")
ax.legend(loc="lower left", fontsize=8)
ax2.legend(loc="upper right", fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 183,
    "tier1_paper": 26,
    "block": "B",
    "paper_in_block": "1/?",
    "topic": "Immunology — innate + adaptive + K_immune introduction",
    "VDJ_diversity": {
        "TCR_beta_combinatorial": int(tcr_beta_comb),
        "BCR_heavy_combinatorial": int(bcr_heavy_comb),
        "TCR_alphabeta_paired_total": f"{tcr_total:.3e}",
        "BCR_germline_paired_total": f"{bcr_total_germline:.3e}",
        "BCR_post_SHM_total": f"{bcr_total_post_shm:.3e}",
        "expected_range_TCR": "10^15 - 10^18",
        "expected_range_BCR_post_SHM": "10^14 - 10^18",
    },
    "affinity_maturation": {
        "rounds": int(rounds[-1]),
        "Kd_initial_M": float(Kd0),
        "Kd_final_M": float(Kd[-1]),
        "improvement_factor": float(Kd0 / Kd[-1]),
    },
    "pathogen_R0": pathogens,
    "MHC_class_I_peak_aa": 9,
    "MHC_class_II_peak_aa": 16,
    "cytokine_storm_peak_IL6_pg_per_mL": float(severe_il6.max()),
    "cytokine_storm_healthy_baseline_pg_per_mL": 2.0,
    "K_immune_modular": {
        "N_clones": int(N_clones),
        "power_law_alpha": float(alpha_pl),
        "Shannon_S_nats": float(S_repertoire),
        "mean_K0_nats": float(mean_K0),
        "ITU_axiom_dS_over_dK": float(itu_ratio),
    },
    "ITU_interpretation": {
        "K_state": "K_immune",
        "sub_states": [
            "K_innate (PAMP/DAMP, PRR, complement, NK, cytokine storm)",
            "K_adaptive (TCR/BCR, V(D)J, affinity maturation)",
            "K_MHC (antigen presentation)",
            "K_memory (long-term B/T memory)",
            "K_tolerance (central/peripheral, AIRE, Tregs)",
            "K_vaccine (mRNA, adjuvant, prime-boost)",
            "K_tumor (immune checkpoint, CAR-T)",
            "K_infect (R0, epidemiology)",
        ],
        "axiom": "delta S(rho_immune) = delta Tr[K_immune^(0) rho_immune]",
        "modular_Hamiltonian": "K_immune^(0) = -log rho_immune",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
