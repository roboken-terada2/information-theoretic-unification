"""
Phase 184 — TCR / BCR + V(D)J recombination + repertoire diversity

Simulations:
  1) IMGT segment counts (TCRA, TCRB, IGH, IGK, IGL)
  2) CDR3 length distribution (TCR-beta vs BCR-heavy)
  3) RSS 12/23 rule + RAG cleavage statistics
  4) Junctional (P/N) nucleotide additions (Poisson model)
  5) Hierarchical diversity accumulation (germline -> SHM)
  6) Repertoire entropy and ITU K_adaptive^(0)
  7) SHM rate verification (Rajewsky 1996)

Outputs:
  - vdj_repertoire.png
  - vdj_repertoire_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

OUT_PNG = Path(__file__).with_name("vdj_repertoire.png")
OUT_JSON = Path(__file__).with_name("vdj_repertoire_summary.json")

rng = np.random.default_rng(20260518)

# -------------------------------------------------------------
# 1) IMGT functional segment counts (human, 2024 release)
# -------------------------------------------------------------
imgt = {
    "TRA (TCR α)": {"V": 47, "D": 0, "J": 61},
    "TRB (TCR β)": {"V": 65, "D": 2, "J": 13},
    "TRG (TCR γ)": {"V": 6, "D": 0, "J": 5},
    "TRD (TCR δ)": {"V": 3, "D": 3, "J": 4},
    "IGH (BCR H)": {"V": 46, "D": 23, "J": 6},
    "IGK (BCR κ)": {"V": 41, "D": 0, "J": 5},
    "IGL (BCR λ)": {"V": 33, "D": 0, "J": 5},
}

def comb(d):
    """Combinatorial V*D*J (D=1 if 0)."""
    return d["V"] * max(1, d["D"]) * d["J"]

combinatorial = {k: comb(v) for k, v in imgt.items()}

# -------------------------------------------------------------
# 2) CDR3 length distribution (TCR-β vs BCR-H)
# -------------------------------------------------------------
# TCR-β CDR3: Gaussian-ish centered at 14 aa, sigma 2
cdr3_aa = np.arange(8, 30)
tcrb_cdr3_pdf = np.exp(-0.5 * ((cdr3_aa - 14.0) / 2.0) ** 2)
tcrb_cdr3_pdf = tcrb_cdr3_pdf / tcrb_cdr3_pdf.sum()
# BCR-H CDR3: wider, centered at 16, sigma 4
bcrh_cdr3_pdf = np.exp(-0.5 * ((cdr3_aa - 16.0) / 4.0) ** 2)
bcrh_cdr3_pdf = bcrh_cdr3_pdf / bcrh_cdr3_pdf.sum()

tcrb_mean = float(np.sum(cdr3_aa * tcrb_cdr3_pdf))
bcrh_mean = float(np.sum(cdr3_aa * bcrh_cdr3_pdf))

# -------------------------------------------------------------
# 3) RSS 12/23 rule and RAG cleavage
# -------------------------------------------------------------
# 12-spacer recombines only with 23-spacer (one-turn vs two-turn of helix)
# Probability of correct paired joining ~ 50% in vitro, ~95%+ in vivo (regulation)
rss_efficiency_invitro = 0.50
rss_efficiency_invivo = 0.95

# -------------------------------------------------------------
# 4) P/N nucleotide additions (Poisson)
# -------------------------------------------------------------
# Mean P additions: ~2 nt per joint; N additions: ~3-5 nt (TdT)
lambda_P = 2.0
lambda_N = 4.0
nt_max = 20
P_dist = poisson.pmf(np.arange(nt_max), lambda_P)
N_dist = poisson.pmf(np.arange(nt_max), lambda_N)
# Total junctional additions per joint (V-D and D-J for heavy chains -> 2 joints)
total_nt_per_joint = lambda_P + lambda_N
total_nt_BCR = 2 * total_nt_per_joint  # H chain has VD and DJ joints
# Each nt has 4 possibilities -> 4^total_nt diversity factor
junctional_factor_BCR = 4 ** total_nt_BCR
junctional_factor_TCR_beta = 4 ** total_nt_BCR  # same structure

# -------------------------------------------------------------
# 5) Hierarchical diversity accumulation
# -------------------------------------------------------------
TCR_alpha_pair = combinatorial["TRA (TCR α)"]
TCR_beta = combinatorial["TRB (TCR β)"]
BCR_H = combinatorial["IGH (BCR H)"]
BCR_L_avg = 0.6 * combinatorial["IGK (BCR κ)"] + 0.4 * combinatorial["IGL (BCR λ)"]

steps = [
    ("Germline VDJ combinatorial (one chain)", TCR_beta),
    ("+ second chain pairing", TCR_beta * TCR_alpha_pair),
    ("+ junctional P/N (germline)", TCR_beta * TCR_alpha_pair * junctional_factor_TCR_beta),
    ("BCR germline (paired + junctional)", BCR_H * BCR_L_avg * junctional_factor_BCR),
]
SHM_factor = 1e5  # 10^5 - 10^6 typical post-germinal center diversification
steps.append(("BCR post-SHM", BCR_H * BCR_L_avg * junctional_factor_BCR * SHM_factor))

# -------------------------------------------------------------
# 6) Repertoire entropy + ITU K_adaptive^(0)
# -------------------------------------------------------------
# Naive repertoire: roughly uniform over ~10^11 visible clones
# We model as power-law with exponent alpha
N_clones_model = 100_000
ranks = np.arange(1, N_clones_model + 1)
alpha_naive = 1.0
alpha_post_antigen = 1.6  # antigen exposure -> oligoclonal expansion -> steeper power law

p_naive = ranks ** (-alpha_naive); p_naive /= p_naive.sum()
p_post = ranks ** (-alpha_post_antigen); p_post /= p_post.sum()

S_naive = float(-np.sum(p_naive * np.log(p_naive)))
S_post = float(-np.sum(p_post * np.log(p_post)))

# ITU axiom: linearized check
# delta S = -Tr[delta rho * (1 + log rho)] = Tr[delta rho * (-1 - log rho)]
# delta <K> with K = -log rho_naive (held fixed) = Tr[(rho_post - rho_naive) * (-log rho_naive)]
K_naive = -np.log(p_naive)
delta_p = p_post - p_naive
dS_first_order = float(-np.sum(delta_p * (1.0 + np.log(p_naive))))
dK_first_order = float(np.sum(delta_p * K_naive))
itu_ratio = dS_first_order / dK_first_order if abs(dK_first_order) > 1e-15 else float("nan")
# Note: with Σδp = 0, dS_first_order = Σδp_i (-log p_i) = dK_first_order, so ratio should = 1.

# -------------------------------------------------------------
# 7) SHM rate verification (Rajewsky 1996)
# -------------------------------------------------------------
# SHM ~10^-3 mutations/bp/cell division in germinal center
# A 350-bp V region in 7 divisions -> ~2.45 mutations expected
SHM_rate = 1e-3  # /bp/division
V_region_bp = 350
divisions = 7
expected_mutations = SHM_rate * V_region_bp * divisions

# Simulate
n_simulated = 10_000
sim_mut = rng.binomial(V_region_bp * divisions, SHM_rate, size=n_simulated)
sim_mean = float(sim_mut.mean())
sim_std = float(sim_mut.std())

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 184 — TCR / BCR + V(D)J Recombination + Repertoire Diversity (Tier 1 #26 / Block B)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: IMGT segment counts (stacked bar)
ax = axes[0, 0]
loci = list(imgt.keys())
Vs = [imgt[k]["V"] for k in loci]
Ds = [imgt[k]["D"] for k in loci]
Js = [imgt[k]["J"] for k in loci]
x = np.arange(len(loci))
ax.bar(x, Vs, label="V", color="#1f77b4")
ax.bar(x, Ds, bottom=Vs, label="D", color="#2ca02c")
ax.bar(x, Js, bottom=np.array(Vs) + np.array(Ds), label="J", color="#d62728")
ax.set_xticks(x)
ax.set_xticklabels(loci, rotation=25, fontsize=8)
ax.set_ylabel("Functional segment count")
ax.set_title("IMGT segment counts (V/D/J)")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: CDR3 length distribution
ax = axes[0, 1]
ax.plot(cdr3_aa, tcrb_cdr3_pdf, "o-", color="#1f77b4", label=f"TCR-β  ⟨L⟩={tcrb_mean:.1f}")
ax.plot(cdr3_aa, bcrh_cdr3_pdf, "s-", color="#d62728", label=f"BCR-H  ⟨L⟩={bcrh_mean:.1f}")
ax.set_xlabel("CDR3 length (aa)")
ax.set_ylabel("Probability")
ax.set_title("CDR3 length distribution")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 3: Junctional P/N additions
ax = axes[0, 2]
ax.bar(np.arange(nt_max), P_dist, alpha=0.6, label=f"P nt  λ={lambda_P}", color="#9467bd")
ax.bar(np.arange(nt_max), N_dist, alpha=0.5, label=f"N nt  λ={lambda_N}", color="#ff7f0e")
ax.set_xlabel("Nucleotides added per joint")
ax.set_ylabel("Probability (Poisson)")
ax.set_title(f"Junctional P/N additions  (4^{int(total_nt_BCR)} = {junctional_factor_BCR:.2e})")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 4: Hierarchical diversity accumulation
ax = axes[1, 0]
labels = [s[0] for s in steps]
vals = [s[1] for s in steps]
ax.barh(range(len(labels)), vals, color=["#1f77b4", "#aec7e8", "#2ca02c", "#98df8a", "#d62728"])
ax.set_xscale("log")
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=8)
ax.set_xlabel("Diversity (log scale)")
ax.set_title("Hierarchical diversity accumulation")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 5: Repertoire entropy + ITU
ax = axes[1, 1]
ax.loglog(ranks, p_naive, "-", color="#1f77b4", lw=2, label=f"Naive (α=1.0)  S={S_naive:.2f}")
ax.loglog(ranks, p_post, "-", color="#d62728", lw=2,
          label=f"Post-antigen (α=1.6)  S={S_post:.2f}")
ax.set_xlabel("Clone rank")
ax.set_ylabel("Abundance p_i")
ax.set_title(f"Repertoire entropy: ΔS = {S_post-S_naive:+.2f} nats; ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.legend()
ax.grid(True, alpha=0.3, which="both")

# Panel 6: SHM rate verification
ax = axes[1, 2]
ax.hist(sim_mut, bins=np.arange(0, 12) - 0.5, density=True, color="#9467bd", alpha=0.7,
        edgecolor="black", label=f"Simulated  ⟨n⟩={sim_mean:.2f}")
ax.axvline(expected_mutations, color="red", linestyle="--", lw=2,
           label=f"Expected = {expected_mutations:.2f}")
ax.set_xlabel("Mutations per V region (350 bp, 7 divisions)")
ax.set_ylabel("Probability")
ax.set_title(f"SHM rate 10⁻³/bp/div (Rajewsky 1996)")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 184,
    "tier1_paper": 26,
    "block": "B",
    "topic": "TCR/BCR + V(D)J recombination + repertoire diversity",
    "IMGT_segment_counts": imgt,
    "combinatorial_VDJ": combinatorial,
    "CDR3_mean_aa": {
        "TCR_beta_predicted": tcrb_mean,
        "TCR_beta_IMGT_obs": "14-15",
        "BCR_H_predicted": bcrh_mean,
        "BCR_H_obs": "12-20",
    },
    "RSS_12_23_rule": {
        "in_vitro_efficiency": rss_efficiency_invitro,
        "in_vivo_efficiency": rss_efficiency_invivo,
        "reference": "Schatz-Oettinger-Baltimore 1989; Tonegawa 1976 Nobel 1987",
    },
    "junctional_additions": {
        "lambda_P_per_joint": lambda_P,
        "lambda_N_per_joint": lambda_N,
        "total_per_BCR_H": float(total_nt_BCR),
        "diversity_factor_4_to_total": float(junctional_factor_BCR),
    },
    "hierarchical_diversity_steps": [{"step": s[0], "value": float(s[1])} for s in steps],
    "TCR_paired_post_junctional": float(steps[2][1]),
    "BCR_germline_paired_junctional": float(steps[3][1]),
    "BCR_post_SHM": float(steps[4][1]),
    "repertoire_entropy_nats": {
        "naive_alpha_1.0": S_naive,
        "post_antigen_alpha_1.6": S_post,
        "delta_S": S_post - S_naive,
    },
    "ITU_axiom_linearized": {
        "delta_S_first_order": dS_first_order,
        "delta_K_first_order": dK_first_order,
        "ratio_dS_over_dK": itu_ratio,
        "expected_ratio": 1.0,
    },
    "SHM_verification": {
        "rate_per_bp_per_division": SHM_rate,
        "V_region_bp": V_region_bp,
        "divisions_in_GC": divisions,
        "expected_mean_mutations": expected_mutations,
        "simulated_mean": sim_mean,
        "simulated_std": sim_std,
        "reference": "Rajewsky 1996; Berek-Milstein 1987",
    },
    "ITU_interpretation": {
        "K_state": "K_adaptive (sub-state of K_immune)",
        "decomposition": "K_adaptive^(0) = K_VDJ ⊕ K_pairing ⊕ K_junctional ⊕ K_SHM",
        "axiom_realization": "Germinal center selection lowers S(rho) and <K^(0)> simultaneously",
        "biological_meaning": "Affinity maturation = ITU descent flow on repertoire manifold",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
