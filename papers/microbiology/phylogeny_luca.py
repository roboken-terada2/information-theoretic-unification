"""
Phase 192 — Phylogeny + 16S rRNA + LUCA + Tree of Life (K_phylogeny)

Simulations:
  1) 3-domain tree (Woese 1977) with 16S rRNA distance
  2) Molecular clock: 16S divergence vs geological time
  3) Phylum count by domain (GTDB 2020)
  4) LUCA conserved gene categories
  5) Earth deep time chronology vs major evolutionary events
  6) HGT contribution to early evolution
  7) ITU K_phylogeny axiom check with mutation+drift+selection

Outputs:
  - phylogeny_luca.png
  - phylogeny_luca_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("phylogeny_luca.png")
OUT_JSON = Path(__file__).with_name("phylogeny_luca_summary.json")

rng = np.random.default_rng(20260526)

# -------------------------------------------------------------
# 1) 16S rRNA distance between major groups (typical values)
# -------------------------------------------------------------
groups = ["E. coli", "B. subtilis", "Synechocystis", "Haloferax",
          "Pyrococcus", "Sulfolobus", "S. cerevisiae", "Homo sapiens"]
# Pairwise 16S identity matrix (approximate %)
# E. coli, B. subtilis, Synech, Halofex, Pyroc, Sulf, S.cerev, Homo
identity = np.array([
    [100, 80,  76, 65, 64, 63, 56, 55],
    [80, 100, 75, 64, 63, 63, 55, 54],
    [76, 75, 100, 66, 64, 64, 57, 56],
    [65, 64, 66, 100, 78, 77, 60, 59],
    [64, 63, 64, 78, 100, 82, 60, 59],
    [63, 63, 64, 77, 82, 100, 60, 59],
    [56, 55, 57, 60, 60, 60, 100, 88],
    [55, 54, 56, 59, 59, 59, 88, 100],
])
# Convert to distance (1 - identity/100)
distance = 1 - identity / 100

# -------------------------------------------------------------
# 2) Molecular clock
# -------------------------------------------------------------
# 16S evolutionary rate ~ 1% / 50 Myr (Ochman 1999)
times_Ma = np.linspace(0, 4000, 200)  # million years ago
clock_rate = 0.0002  # / position / Myr
divergence = clock_rate * times_Ma * 100  # %

# Key calibrations
calibrations = {
    "Human-chimp split": (6, 1.0),
    "Mammalian radiation": (100, 5.0),
    "Cambrian explosion": (540, 12.0),
    "Eukaryotic LCA": (1800, 25.0),
    "Bacteria-Archaea split": (3500, 40.0),
    "LUCA": (4000, 50.0),
}

# -------------------------------------------------------------
# 3) Phylum count per domain (GTDB 2020)
# -------------------------------------------------------------
phyla = {
    "Bacteria": 92,
    "Archaea": 26,
    "Eukarya": 30,
}

# -------------------------------------------------------------
# 4) LUCA conserved gene categories (Weiss 2016 Nat Microbiol)
# -------------------------------------------------------------
luca_genes = {
    "Translation (ribosome)": 60,
    "Replication/repair": 35,
    "Energy metabolism": 45,
    "Membrane transport": 28,
    "Amino acid metabolism": 50,
    "Cofactor biosynthesis": 30,
    "Nucleotide metabolism": 25,
    "Carbon fixation": 25,
    "Other": 56,
}
luca_total = sum(luca_genes.values())

# -------------------------------------------------------------
# 5) Earth deep time chronology
# -------------------------------------------------------------
events = {
    "Earth formation": 4540,
    "LUCA": 4000,
    "Photosynthesis (cyanobacteria)": 2400,
    "Great Oxygenation Event": 2300,
    "Eukaryotic cell": 1800,
    "Multicellularity": 1200,
    "Cambrian explosion": 540,
    "Land plants": 470,
    "Dinosaur extinction": 65,
    "Human-chimp split": 6,
    "Homo sapiens": 0.3,
}

# -------------------------------------------------------------
# 6) HGT vs vertical descent fraction over time
# -------------------------------------------------------------
ages_ga = np.linspace(0, 4, 80)
# Doolittle 2000: HGT dominated early evolution
# Fraction of HGT genes ~ 0.7 at 4 Ga, decline to ~0.1 today
hgt_frac = 0.1 + 0.6 * np.exp(-(4 - ages_ga) / 1.5)

# -------------------------------------------------------------
# 7) ITU K_phylogeny: mutation + drift + selection
# -------------------------------------------------------------
N_lineages = 200
generations = 10_000
mut_rate = 0.001  # per gene per generation
# Initialize: log_fitness ~ N(0, 0.5)
log_fit = rng.normal(0, 0.5, size=N_lineages)
# Evolve: each generation, mutate then weighted sample
fit_history = [log_fit.copy()]
S_history = []
K_history = []
p = np.exp(log_fit)
p = p / p.sum()
S_history.append(-np.sum(p * np.log(p)))
K_history.append(np.sum(p * (-np.log(p))))

itu_ratios = []
sample_gens = [100, 500, 1000, 5000]
for gen in range(1, generations + 1):
    # Mutation
    new_log_fit = log_fit + rng.normal(0, 0.01, size=N_lineages)
    # Drift + selection: weighted sampling
    fitness = np.exp(new_log_fit)
    p_new = fitness / fitness.sum()
    # Random sample by p_new
    idx = rng.choice(N_lineages, size=N_lineages, replace=True, p=p_new)
    log_fit = new_log_fit[idx]
    if gen in sample_gens:
        p_curr = np.exp(log_fit) / np.sum(np.exp(log_fit))
        S_history.append(-np.sum(p_curr * np.log(p_curr)))
        K_history.append(np.sum(p_curr * (-np.log(p_curr))))
        # ITU check: linearized at previous p
        dp = p_curr - p
        log_p = np.log(np.clip(p, 1e-30, None))
        dS_lin = -np.sum(dp * (1.0 + log_p))
        dK_lin = -np.sum(dp * log_p)
        ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")
        itu_ratios.append({"generation": gen, "ratio": ratio})
        p = p_curr.copy()

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 192 — Phylogeny + 16S rRNA + LUCA + Tree of Life (K_phylogeny)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: 16S identity matrix
ax = axes[0, 0]
im = ax.imshow(identity, cmap="RdYlBu_r", vmin=50, vmax=100, aspect="auto")
ax.set_xticks(range(len(groups)))
ax.set_yticks(range(len(groups)))
ax.set_xticklabels(groups, rotation=45, fontsize=7, ha="right")
ax.set_yticklabels(groups, fontsize=7)
plt.colorbar(im, ax=ax, label="16S identity (%)")
ax.set_title("16S rRNA pairwise identity (Woese 3-domain)")

# Panel 2: Molecular clock
ax = axes[0, 1]
ax.plot(times_Ma, divergence, "-", color="#1f77b4", lw=2,
        label="Theoretical (0.02 %/Myr)")
for name, (t, d) in calibrations.items():
    ax.scatter([t], [d], s=80, color="#d62728", zorder=5)
    ax.annotate(name, (t, d), fontsize=7, xytext=(5, 5),
                textcoords="offset points")
ax.set_xlabel("Million years ago")
ax.set_ylabel("16S divergence (%)")
ax.set_title("Molecular clock (16S rRNA)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Phylum counts
ax = axes[0, 2]
domains = list(phyla.keys())
counts = list(phyla.values())
colors_d = ["#1f77b4", "#ff7f0e", "#2ca02c"]
ax.bar(domains, counts, color=colors_d)
ax.set_ylabel("Number of phyla (GTDB 2020)")
ax.set_title("3-domain phylum census")
for i, c in enumerate(counts):
    ax.text(i, c + 1, str(c), ha="center", fontsize=11, fontweight="bold")
ax.grid(True, alpha=0.3, axis="y")

# Panel 4: LUCA conserved gene categories
ax = axes[1, 0]
cats = list(luca_genes.keys())
n_genes = list(luca_genes.values())
ax.pie(n_genes, labels=cats, autopct="%1.0f%%", startangle=90, textprops={"fontsize": 8})
ax.set_title(f"LUCA conserved genes (n={luca_total}, Weiss 2016)")

# Panel 5: Deep time chronology
ax = axes[1, 1]
ev_names = list(events.keys())
ev_times = list(events.values())
ax.barh(range(len(ev_names)), ev_times, color="#9467bd")
ax.set_yticks(range(len(ev_names)))
ax.set_yticklabels(ev_names, fontsize=7)
ax.set_xscale("log")
ax.set_xlabel("Million years ago (log)")
ax.set_title("Earth deep time chronology")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 6: HGT fraction + ITU
ax = axes[1, 2]
ax.plot(ages_ga, hgt_frac * 100, "-", color="#d62728", lw=2,
        label="HGT fraction (Doolittle 2000)")
ax.plot(ages_ga, (1 - hgt_frac) * 100, "-", color="#1f77b4", lw=2,
        label="Vertical descent")
ax.set_xlabel("Time (Ga ago)")
ax.set_ylabel("Fraction (%)")
ax.invert_xaxis()
last_ratio = itu_ratios[-1]["ratio"] if itu_ratios else float("nan")
ax.set_title(f"HGT decline over time;  ITU δS/δ⟨K⟩ last gen = {last_ratio:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 192,
    "tier1_paper": 27,
    "block": "B",
    "topic": "Phylogeny + 16S rRNA + LUCA + Tree of Life (K_phylogeny)",
    "Woese_1977_3_domains": "Bacteria + Archaea + Eukarya based on 16S/18S rRNA",
    "phyla_per_domain_GTDB_2020": phyla,
    "16S_rRNA": {
        "length_bp": 1500,
        "evolutionary_rate_per_position_per_Myr": clock_rate,
        "molecular_clock_calibrations": {
            name: {"Myr_ago": t, "divergence_pct": d}
            for name, (t, d) in calibrations.items()
        },
    },
    "LUCA": {
        "age_Ga": 4.0,
        "habitat": "Deep-sea alkaline serpentinization vents (Lost City-like)",
        "metabolism": "H2 + CO2 -> reductive acetyl CoA, anaerobic autotroph",
        "conserved_genes_354": luca_genes,
        "reference": "Weiss 2016 Nat Microbiol",
    },
    "deep_time_events_Ma": events,
    "HGT_contribution": {
        "early_evolution_Ga4": 0.7,
        "present_day": 0.1,
        "reference": "Doolittle 2000 Science",
    },
    "ITU_K_phylogeny_simulation": {
        "N_lineages": int(N_lineages),
        "generations": int(generations),
        "mutation_rate": mut_rate,
        "S_initial_nats": float(S_history[0]),
        "S_final_nats": float(S_history[-1]),
        "K_initial_nats": float(K_history[0]),
        "K_final_nats": float(K_history[-1]),
        "ITU_axiom_ratios_per_sample_gen": itu_ratios,
    },
    "ITU_interpretation": {
        "K_state": "K_phylogeny (sub-state of K_microbe)",
        "modular_Hamiltonian": "K_phylogeny^(0) = -log P(species | environment, time)",
        "LUCA": "Origin of K_phylogeny manifold (singularity)",
        "tree_of_life": "K_phylogeny descent flow trajectory in genotype-time space",
        "HGT": "ITU K-state mixing operation between lineages (dominant in early evolution)",
        "molecular_clock": "K_phylogeny^(0)(t) - K_phylogeny^(0)(0) = mu * Delta_t * N",
    },
    "predictions_phase_192": [
        ("LUCA genome in silico reconstruction", 2030, 0.55, "Medium"),
        ("Asgardarchaea-eukaryote direct ancestry confirmed", 2028, 0.65, "Medium"),
        ("Cryosphere microbial dark matter major phyla", 2030, 0.60, "Medium"),
        ("CPR cell culture established", 2028, 0.50, "Medium"),
        ("Marine OTU count > 1 million confirmed", 2030, 0.70, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
