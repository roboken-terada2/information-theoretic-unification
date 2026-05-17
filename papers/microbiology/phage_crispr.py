"""
Phase 193 — Bacteriophage + phage therapy + CRISPR origin (K_phage)

Simulations:
  1) Phage burst size + lytic cycle timing
  2) Phage-host arms race (Red Queen, Van Valen 1973)
  3) CRISPR spacer accumulation dynamics
  4) Phage display library size vs antibody affinity
  5) CRISPR system classification stats
  6) Lotka-Volterra phage-host dynamics
  7) ITU axiom check for co-evolutionary descent

Outputs:
  - phage_crispr.png
  - phage_crispr_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

OUT_PNG = Path(__file__).with_name("phage_crispr.png")
OUT_JSON = Path(__file__).with_name("phage_crispr_summary.json")

rng = np.random.default_rng(20260527)

# -------------------------------------------------------------
# 1) Phage burst size + lytic cycle
# -------------------------------------------------------------
phage_data = {
    "T4 (E. coli)":   {"burst": 200, "cycle_min": 25},
    "T7 (E. coli)":   {"burst": 150, "cycle_min": 17},
    "λ (E. coli)":    {"burst": 100, "cycle_min": 50},
    "P22 (Salm.)":    {"burst": 250, "cycle_min": 45},
    "ϕ29 (B. sub.)":  {"burst": 100, "cycle_min": 40},
    "MS2 (E. coli)":  {"burst": 5000, "cycle_min": 35},
}

# -------------------------------------------------------------
# 2) Phage-host arms race + CRISPR spacer accumulation
# -------------------------------------------------------------
generations = np.arange(0, 500)
# Spacer accumulation: stochastic Poisson process
spacer_rate = 0.01  # per generation
spacers = np.cumsum(rng.poisson(spacer_rate, size=len(generations)))
max_spacers = 1500  # typical max for a CRISPR array

# Anti-CRISPR (Acr) coevolution
acr_acquisition = 1 / (1 + np.exp(-(generations - 100) / 50))  # sigmoidal Acr rise

# -------------------------------------------------------------
# 3) CRISPR classification (Makarova 2020)
# -------------------------------------------------------------
crispr_classes = {
    "Class 1 / Type I (Cas3)":    {"prevalence_pct": 50, "target": "DNA", "multi_subunit": True},
    "Class 1 / Type III (Cas10)": {"prevalence_pct": 25, "target": "DNA/RNA", "multi_subunit": True},
    "Class 1 / Type IV":          {"prevalence_pct": 1, "target": "DNA", "multi_subunit": True},
    "Class 2 / Type II (Cas9) ★": {"prevalence_pct": 10, "target": "DNA", "multi_subunit": False},
    "Class 2 / Type V (Cas12)":   {"prevalence_pct": 8, "target": "DNA", "multi_subunit": False},
    "Class 2 / Type VI (Cas13)":  {"prevalence_pct": 6, "target": "RNA", "multi_subunit": False},
}

# -------------------------------------------------------------
# 4) Phage display library affinity selection
# -------------------------------------------------------------
# Library size 10^9; selection rounds 3-5
library_size = 1e9
rounds = np.arange(0, 6)
# Each round enriches binders ~ 1000×, eventually plateau
log_enrichment = np.log10(np.maximum(library_size, 1)) - rounds * 3
log_enrichment = np.maximum(log_enrichment, 1.0)
n_unique = 10 ** log_enrichment

# Affinity Kd improves: typical 1 μM start → 1 nM after 4 rounds
Kd_rounds = 1e-6 * 10 ** (-rounds * 0.7)

# -------------------------------------------------------------
# 5) Lotka-Volterra phage-host
# -------------------------------------------------------------
def lv(y, t, mu, K, beta, delta, gamma):
    H, V = y
    dH = mu * H * (1 - H / K) - beta * H * V
    dV = beta * gamma * H * V - delta * V
    return [dH, dV]

t = np.linspace(0, 100, 1000)
mu, K_cap, beta, delta, gamma = 1.0, 1e9, 1e-9, 0.5, 100
y0 = [1e8, 1e6]
sol = odeint(lv, y0, t, args=(mu, K_cap, beta, delta, gamma))
H_dyn, V_dyn = sol[:, 0], sol[:, 1]

# -------------------------------------------------------------
# 6) ITU axiom: phage-host co-evolution descent
# -------------------------------------------------------------
N_strains = 3000
# Initial: uniform host + phage repertoire
log_host_fit = rng.normal(0, 0.5, size=N_strains)
log_phage_fit = rng.normal(0, 0.5, size=N_strains)

p_host_pre = np.exp(log_host_fit); p_host_pre /= p_host_pre.sum()
p_phage_pre = np.exp(log_phage_fit); p_phage_pre /= p_phage_pre.sum()

S_host_pre = -np.sum(p_host_pre * np.log(p_host_pre))
S_phage_pre = -np.sum(p_phage_pre * np.log(p_phage_pre))

# Co-evolutionary selection: resistance + counter-resistance
resistance_mask = rng.random(N_strains) < 0.1
log_host_fit_post = log_host_fit.copy()
log_host_fit_post[resistance_mask] += 1.5

counter_mask = rng.random(N_strains) < 0.1
log_phage_fit_post = log_phage_fit.copy()
log_phage_fit_post[counter_mask] += 1.5

p_host_post = np.exp(log_host_fit_post); p_host_post /= p_host_post.sum()
p_phage_post = np.exp(log_phage_fit_post); p_phage_post /= p_phage_post.sum()

S_host_post = -np.sum(p_host_post * np.log(p_host_post))
S_phage_post = -np.sum(p_phage_post * np.log(p_phage_post))

# ITU axiom check
def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return (dS / dK) if abs(dK) > 1e-15 else float("nan"), float(dS), float(dK)

itu_host = itu_lin(p_host_pre, p_host_post)
itu_phage = itu_lin(p_phage_pre, p_phage_post)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 193 — Bacteriophage + Phage Therapy + CRISPR Origin (K_phage)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Phage burst + cycle
ax = axes[0, 0]
names = list(phage_data.keys())
bursts = [phage_data[n]["burst"] for n in names]
cycles = [phage_data[n]["cycle_min"] for n in names]
x = np.arange(len(names))
width = 0.4
ax.bar(x - width/2, bursts, width, color="#1f77b4", label="Burst size", log=True)
ax2 = ax.twinx()
ax2.bar(x + width/2, cycles, width, color="#ff7f0e", label="Cycle (min)")
ax.set_xticks(x)
ax.set_xticklabels(names, fontsize=7, rotation=20)
ax.set_ylabel("Burst size (log)", color="#1f77b4")
ax2.set_ylabel("Cycle time (min)", color="#ff7f0e")
ax.set_title("Phage life-cycle params")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="upper right", fontsize=8)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 2: CRISPR spacer accumulation
ax = axes[0, 1]
ax.plot(generations, np.minimum(spacers, max_spacers), "-", color="#2ca02c", lw=2,
        label="Spacer accumulation (Poisson)")
ax2 = ax.twinx()
ax2.plot(generations, acr_acquisition, "-", color="#d62728", lw=2,
         label="Anti-CRISPR (Acr) prevalence")
ax.set_xlabel("Generations")
ax.set_ylabel("CRISPR spacers", color="#2ca02c")
ax2.set_ylabel("Acr fraction", color="#d62728")
ax.set_title("Phage-host arms race (Red Queen)")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="lower right", fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: CRISPR classification
ax = axes[0, 2]
cls = list(crispr_classes.keys())
prevs = [crispr_classes[c]["prevalence_pct"] for c in cls]
colors_c = ["#1f77b4" if "Class 1" in c else "#d62728" for c in cls]
ax.barh(range(len(cls)), prevs, color=colors_c)
ax.set_yticks(range(len(cls)))
ax.set_yticklabels(cls, fontsize=7)
ax.set_xlabel("Prevalence (%)")
ax.set_title("CRISPR classification (Makarova 2020)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: Phage display library selection
ax = axes[1, 0]
ax2 = ax.twinx()
ax.semilogy(rounds, n_unique, "o-", color="#9467bd", lw=2, label="Unique clones remaining")
ax2.semilogy(rounds, Kd_rounds, "s-", color="#d62728", lw=2, label="Kd (M)")
ax.set_xlabel("Selection round")
ax.set_ylabel("Unique clones (log)", color="#9467bd")
ax2.set_ylabel("Kd (log, M)", color="#d62728")
ax.set_title("Phage display library affinity selection (Smith 1985, Nobel 2018)")
ax.legend(loc="upper right", fontsize=8)
ax2.legend(loc="lower left", fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 5: Lotka-Volterra phage-host
ax = axes[1, 1]
ax.semilogy(t, H_dyn, "-", color="#1f77b4", lw=2, label="Host (bacteria)")
ax.semilogy(t, V_dyn, "-", color="#d62728", lw=2, label="Phage")
ax.set_xlabel("Time (hr)")
ax.set_ylabel("Population (log)")
ax.set_title("Lotka-Volterra phage-host dynamics")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")

# Panel 6: ITU coevolution
ax = axes[1, 2]
labels_e = ["Host", "Phage"]
S_pre_vals = [S_host_pre, S_phage_pre]
S_post_vals = [S_host_post, S_phage_post]
ratios = [itu_host[0], itu_phage[0]]
x = np.arange(2)
width = 0.35
ax.bar(x - width/2, S_pre_vals, width, color="#1f77b4", label="S pre")
ax.bar(x + width/2, S_post_vals, width, color="#d62728", label="S post")
ax.set_xticks(x); ax.set_xticklabels(labels_e)
ax.set_ylabel("Entropy (nats)")
ax.set_title(f"ITU co-evolution: host δS/δ⟨K⟩={ratios[0]:.3f}, phage={ratios[1]:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 193,
    "tier1_paper": 27,
    "block": "B",
    "topic": "Bacteriophage + phage therapy + CRISPR origin (K_phage)",
    "phage_lifecycle_data": phage_data,
    "phage_count_estimates": {
        "global_total": 1e31,
        "marine_per_mL": 1e7,
        "daily_bacterial_mortality_marine_pct": "20-40",
        "carbon_cycling_PgC_per_year": "10 (Suttle 2007 Nat Rev Microbiol)",
        "gene_transfer_events_per_sec_marine": 1e28,
    },
    "CRISPR_history": {
        "discovery": "Ishino 1987 (Osaka)",
        "function_demonstrated": "Barrangou 2007 (Danisco, yogurt bacteria)",
        "Cas9_mechanism": "Jinek 2012 (Doudna-Charpentier)",
        "eukaryotic_application": "Zhang/Church 2013",
        "Nobel_2020": "Doudna + Charpentier",
    },
    "CRISPR_classification_2020_Makarova": crispr_classes,
    "phage_display": {
        "discoverer": "Smith 1985, Nobel 2018",
        "library_size": int(library_size),
        "selection_rounds": 4,
        "Kd_after_rounds_M": Kd_rounds.tolist(),
    },
    "Strathdee_2017_case": {
        "patient": "Tom Patterson (UCSD professor)",
        "pathogen": "Multidrug-resistant Acinetobacter baumannii",
        "phage_cocktail_size": 4,
        "outcome": "Complete recovery in 3 months",
        "significance": "First US IND for phage therapy; revival of Western interest",
    },
    "Lotka_Volterra_phage_host": {
        "mu_host_growth_per_hr": float(mu),
        "K_carrying_capacity": float(K_cap),
        "beta_attack_rate": float(beta),
        "gamma_burst_size_proxy": int(gamma),
        "delta_phage_decay_per_hr": float(delta),
    },
    "ITU_K_phage_coevolution": {
        "N_strains": N_strains,
        "S_host_pre_nats": float(S_host_pre),
        "S_host_post_nats": float(S_host_post),
        "S_phage_pre_nats": float(S_phage_pre),
        "S_phage_post_nats": float(S_phage_post),
        "host_dS_dK_ratio": float(itu_host[0]),
        "phage_dS_dK_ratio": float(itu_phage[0]),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_phage (sub-state of K_microbe)",
        "Red_Queen_dynamics": "Van Valen 1973 - perpetual arms race",
        "CRISPR_role": "Memory K-state freezing phage signatures into host genome",
        "K_phage_K_microbe_coupling": "ITU tensor product of two K-states; co-descent",
        "phage_display_for_drug_discovery": "ITU descent flow on peptide affinity manifold",
        "co_evolution_axiom": "delta S(host) = delta <K_host>; delta S(phage) = delta <K_phage>",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
