"""
Phase 218 — Population Genetics + Evolution + Coalescent (K_genome_evolution)

Simulations:
  1) Hardy-Weinberg equilibrium verification
  2) Wright-Fisher genetic drift simulation
  3) Coalescent MRCA time
  4) PSMC-style Ne(t) inference (Out-of-Africa bottleneck)
  5) Neanderthal/Denisovan admixture %
  6) Adaptive sweep simulation
  7) ITU K_genome_evolution axiom

Outputs:
  - popgen_evolution.png
  - popgen_evolution_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("popgen_evolution.png")
OUT_JSON = Path(__file__).with_name("popgen_evolution_summary.json")

rng = np.random.default_rng(20260628)

# -------------------------------------------------------------
# 1) Hardy-Weinberg
# -------------------------------------------------------------
p_vals = np.linspace(0, 1, 100)
q_vals = 1 - p_vals
AA = p_vals ** 2
Aa = 2 * p_vals * q_vals
aa = q_vals ** 2

# -------------------------------------------------------------
# 2) Wright-Fisher drift
# -------------------------------------------------------------
def wf_drift(N, p0, generations, n_traj=10):
    """Simulate WF drift trajectories."""
    trajs = []
    for _ in range(n_traj):
        p = p0
        history = [p]
        for _ in range(generations):
            count = rng.binomial(2 * N, p)
            p = count / (2 * N)
            history.append(p)
        trajs.append(history)
    return np.array(trajs)

generations = 200
N_pop = 100
p0 = 0.5
trajs = wf_drift(N_pop, p0, generations, n_traj=15)

# Fixation probability theory: 1/(2N) for neutral allele
fixation_prob_theory = 1 / (2 * N_pop)

# -------------------------------------------------------------
# 3) Coalescent MRCA expected time
# -------------------------------------------------------------
n_samples = np.arange(2, 50)
mrca_time_in_2N = 2 * (1 - 1.0 / n_samples)  # in units of 2N generations
# n → ∞: 2N (2 - 2/n) → 4N for n large, approaches 2 × 2N

# -------------------------------------------------------------
# 4) PSMC-style Ne(t) for humans (Out-of-Africa bottleneck)
# -------------------------------------------------------------
ka = np.linspace(0, 500, 200)  # kya
# Ancestral large pop, bottleneck ~60-70 kya, recovery
Ne = 15000 * np.ones_like(ka)
mask_bottleneck = (ka > 50) & (ka < 80)
Ne[mask_bottleneck] = 2000  # bottleneck (Out-of-Africa)
mask_ancient = ka > 200
Ne[mask_ancient] = 25000  # ancient large pop
# Smooth transitions
from scipy.ndimage import gaussian_filter1d
Ne = gaussian_filter1d(Ne, sigma=5)

# -------------------------------------------------------------
# 5) Neanderthal/Denisovan admixture
# -------------------------------------------------------------
populations = {
    "African":                {"Neanderthal_pct": 0.3, "Denisovan_pct": 0.0},
    "European":               {"Neanderthal_pct": 2.0, "Denisovan_pct": 0.0},
    "East Asian":             {"Neanderthal_pct": 2.5, "Denisovan_pct": 0.2},
    "Melanesian":             {"Neanderthal_pct": 1.9, "Denisovan_pct": 5.0},
    "Aboriginal Australian":  {"Neanderthal_pct": 2.0, "Denisovan_pct": 4.5},
    "Tibetan (EPAS1)":        {"Neanderthal_pct": 2.0, "Denisovan_pct": 0.1},  # EPAS1 Denisovan origin
}

# -------------------------------------------------------------
# 6) Adaptive sweep simulation
# -------------------------------------------------------------
def adaptive_sweep(N, p0, s, generations):
    """Allele freq under selection with drift."""
    p = p0
    history = [p]
    for _ in range(generations):
        # Selection
        p_new = p * (1 + s) / (1 + s * p)
        # Drift (binomial)
        count = rng.binomial(2 * N, p_new)
        p = count / (2 * N)
        history.append(p)
    return history

sweep_neutral = adaptive_sweep(1000, 0.01, 0.0, 500)
sweep_s001 = adaptive_sweep(1000, 0.01, 0.01, 500)
sweep_s01 = adaptive_sweep(1000, 0.01, 0.1, 500)

# -------------------------------------------------------------
# 7) ITU K_genome_evolution axiom
# -------------------------------------------------------------
N_alleles = 1000
# Pre-selection: uniform-ish allele distribution
log_fit_pre = 0.1 * rng.standard_normal(N_alleles)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Post-sweep: one allele fixed
log_fit_sweep = log_fit_pre.copy()
log_fit_sweep[500] += 5.0
p_sweep = np.exp(log_fit_sweep); p_sweep /= p_sweep.sum()
S_sweep = float(-np.sum(p_sweep * np.log(p_sweep)))

# After admixture: 2-3 alleles mixed
log_fit_admix = log_fit_pre.copy()
log_fit_admix[500] += 2.0
log_fit_admix[300] += 1.5
log_fit_admix[700] += 1.5
p_admix = np.exp(log_fit_admix); p_admix /= p_admix.sum()
S_admix = float(-np.sum(p_admix * np.log(p_admix)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_sweep = itu_lin(p_pre, p_sweep)
ratio_pre_admix = itu_lin(p_pre, p_admix)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 218 — Population Genetics + Evolution + Coalescent (K_genome_evolution)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Hardy-Weinberg
ax = axes[0, 0]
ax.plot(p_vals, AA, "-", color="#1f77b4", lw=2, label="AA (p²)")
ax.plot(p_vals, Aa, "-", color="#2ca02c", lw=2, label="Aa (2pq)")
ax.plot(p_vals, aa, "-", color="#d62728", lw=2, label="aa (q²)")
ax.set_xlabel("Allele frequency p")
ax.set_ylabel("Genotype frequency")
ax.set_title("Hardy-Weinberg (1908)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: WF drift trajectories
ax = axes[0, 1]
for i, traj in enumerate(trajs):
    ax.plot(traj, lw=0.8, alpha=0.6)
ax.axhline(0, color="black", linestyle="--", alpha=0.5, label="Loss")
ax.axhline(1, color="black", linestyle="--", alpha=0.5, label="Fixation")
ax.set_xlabel("Generation")
ax.set_ylabel("Allele frequency p")
ax.set_title(f"Wright-Fisher drift (N={N_pop}, p₀={p0})")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Coalescent MRCA time
ax = axes[0, 2]
ax.plot(n_samples, mrca_time_in_2N, "o-", color="#9467bd", lw=2, markersize=5)
ax.axhline(2, color="red", linestyle="--", label="Asymptote: 2 × 2N = 4N")
ax.set_xlabel("Sample size n")
ax.set_ylabel("E[T_MRCA] / 2N generations")
ax.set_title("Coalescent (Kingman 1982)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: PSMC Ne(t)
ax = axes[1, 0]
ax.plot(ka, Ne, "-", color="#1f77b4", lw=2)
ax.fill_between(ka, 0, Ne, alpha=0.3, color="#1f77b4")
ax.axvspan(50, 80, alpha=0.3, color="red", label="Out-of-Africa bottleneck")
ax.set_xlabel("Time (kya)")
ax.set_ylabel("Effective population size N_e")
ax.set_title("PSMC-like Ne(t) (Li-Durbin 2011)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Neanderthal/Denisovan admixture
ax = axes[1, 1]
pop_names = list(populations.keys())
nean = [populations[p]["Neanderthal_pct"] for p in pop_names]
deni = [populations[p]["Denisovan_pct"] for p in pop_names]
x = np.arange(len(pop_names))
width = 0.35
ax.bar(x - width/2, nean, width, color="#d62728", label="Neanderthal %")
ax.bar(x + width/2, deni, width, color="#9467bd", label="Denisovan %")
ax.set_xticks(x); ax.set_xticklabels(pop_names, fontsize=7, rotation=20, ha="right")
ax.set_ylabel("Admixture %")
ax.set_title("Pääbo Nobel 2022 - Archaic admixture")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 6: ITU K_genome_evolution
ax = axes[1, 2]
ax.bar(["Pre-event", "Adaptive sweep", "Admixture"],
       [S_pre, S_sweep, S_admix], color=["#1f77b4", "#d62728", "#9467bd"])
ax.set_ylabel("Allele distribution entropy (nats)")
ax.set_title(f"K_genome_evolution: P→Sweep={ratio_pre_sweep:.3f}, P→Admix={ratio_pre_admix:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 218,
    "tier1_paper": 30,
    "block": "B",
    "topic": "Population genetics + Evolution + Coalescent (K_genome_evolution)",
    "Hardy_Weinberg_1908": "p² + 2pq + q² = 1 (no selection/migration/mutation/drift)",
    "Wright_Fisher_1930s": {
        "model": "Binomial sampling, 2N gametes",
        "fixation_prob_neutral": f"1/(2N) = {fixation_prob_theory:.4f}",
    },
    "Coalescent_Kingman_1982": {
        "MRCA_2_lineages": "2N generations",
        "MRCA_n_inf": "4N generations",
        "PSMC_Li_Durbin_2011": "Single genome → Ne(t) inference",
    },
    "human_Ne_estimates": {
        "effective_N_modern": 10000,
        "chimpanzee_Ne": 20000,
        "gorilla_Ne": 25000,
        "bonobo_Ne": 30000,
        "interpretation": "Humans have lowest primate diversity due to bottleneck",
    },
    "Out_of_Africa": {
        "bottleneck_kya": "60-70",
        "mtDNA_Eve_kya": "150-200",
        "Y_Adam_kya": "200",
        "evidence": "Cann-Stoneking 1987 mtDNA + ancient DNA confirmation",
    },
    "Paabo_2022_Nobel": {
        "category": "Physiology/Medicine",
        "achievements": [
            "Neanderthal genome 2010 Science",
            "Denisovan genome 2010 Nature",
            "Denisovan-Neanderthal hybrid 2018",
            "Ust'-Ishim 45 kya genome 2014",
        ],
        "founding_field": "Paleogenomics",
    },
    "archaic_admixture_pct": populations,
    "1000_Genomes_2015": {
        "populations": 26,
        "individuals": 2504,
        "SNVs_per_individual_M": 3.5,
        "total_human_SNPs_M": 88,
    },
    "key_SNPs": {
        "LCT_lactase_persistence": "Northern European 80%, ~7500 ya emergence",
        "EPAS1_Tibetan": "High altitude adaptation, Denisovan introgression",
        "DARC_Duffy_negative": "Malaria resistance, African",
        "ALDH2_504K": "East Asian alcohol intolerance ~40%",
    },
    "ITU_K_genome_evolution": {
        "N_alleles": N_alleles,
        "S_pre_event_nats": S_pre,
        "S_post_sweep_nats": S_sweep,
        "S_post_admixture_nats": S_admix,
        "pre_to_sweep_ratio": ratio_pre_sweep,
        "pre_to_admix_ratio": ratio_pre_admix,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_genome_evolution",
        "modular_Hamiltonian": "K_genome_evolution^(0) = -log P(genome | population, time, env)",
        "Coalescent_meaning": "K-state past-directed ITU descent (time-reversed)",
        "Selection_meaning": "K-state biased descent under fitness gradient",
        "Drift_meaning": "K-state stochastic fluctuation in finite N",
        "Admixture_meaning": "K-state population mixing (ITU tensor product)",
        "Paabo_Nobel_meaning": "Paleogenomics = ITU descent flow archaeology",
    },
    "predictions": [
        ("All living humans WGS (1e9 genomes)", 2030, 0.70, "Strong"),
        ("1M+ ancient genomes", 2030, 0.80, "Strong"),
        ("Polygenic risk score clinical full", 2030, 0.75, "Strong"),
        ("AI global selection sweeps map", 2028, 0.70, "Strong"),
        ("New archaic human identified", 2030, 0.55, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
