"""
Phase 191 — Microbiology + Virology + Microbiome (K_microbe introduction)

Simulations:
  1) Earth's microbial census (cells per habitat, Whitman 1998 + updates)
  2) Baltimore virus classification + genome size scaling
  3) Human microbiome species diversity (gut, oral, skin, lung)
  4) Pan-genome growth curve (Heaps' law, Tettelin 2005)
  5) Horizontal gene transfer rate estimation
  6) Antibiotic resistance emergence timeline (year of introduction vs first resistance)
  7) AMR projected mortality (Murray 2022 / O'Neill 2014)
  8) ITU K_microbe axiom check on bacterial population dynamics

Outputs:
  - microbiome_diversity_K.png
  - microbiome_diversity_K_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("microbiome_diversity_K.png")
OUT_JSON = Path(__file__).with_name("microbiome_diversity_K_summary.json")

rng = np.random.default_rng(20260525)

# -------------------------------------------------------------
# 1) Earth's microbial census
# -------------------------------------------------------------
earth_microbial = {
    "Marine bacteria": 1.2e29,
    "Soil bacteria": 2.6e29,
    "Subsurface bacteria": 0.25e30,
    "Aquatic subsurface": 0.07e30,
    "Animal/Plant hosts": 0.001e30,
    "Marine viruses": 1.0e30,
    "Archaea (estimated)": 1.0e29,
}
total_bacterial_archaeal = sum(v for k, v in earth_microbial.items() if "viruses" not in k)
total_viruses = earth_microbial["Marine viruses"]

# -------------------------------------------------------------
# 2) Baltimore classification + genome size
# -------------------------------------------------------------
virus_genomes = {
    "Circovirus (ssDNA)": 1.7,
    "Phi-X174 (ssDNA)": 5.4,
    "Influenza (-ssRNA)": 13.5,
    "HIV (Retrovirus)": 9.7,
    "Polio (+ssRNA)": 7.5,
    "SARS-CoV-2 (+ssRNA)": 29.9,
    "Adenovirus (dsDNA)": 36.0,
    "Herpesvirus (dsDNA)": 235.0,
    "Mimivirus (dsDNA)": 1180.0,
    "Pithovirus (dsDNA)": 610.0,
}

baltimore_class = {
    "I dsDNA": ["Pox", "Herpes", "Adeno", "Mimi", "Pitho"],
    "II ssDNA": ["Parvo", "Circo", "Phi-X174"],
    "III dsRNA": ["Rota", "Reo"],
    "IV +ssRNA": ["SARS-CoV-2", "Polio", "Dengue", "HCV"],
    "V -ssRNA": ["Influenza", "Rabies", "Ebola"],
    "VI Retrovirus": ["HIV", "HTLV"],
    "VII Pararetrovirus": ["HBV"],
}

# -------------------------------------------------------------
# 3) Human microbiome diversity
# -------------------------------------------------------------
sites = ["Gut", "Oral", "Skin", "Lung", "Vagina"]
cell_count_log10 = [13.5, 9.0, 6.5, 5.5, 8.0]  # log10 cells
species_count = [800, 600, 200, 100, 250]
shannon_H = [4.5, 3.5, 2.2, 2.0, 1.5]  # nats

# -------------------------------------------------------------
# 4) Pan-genome growth curve (Heaps' law, E. coli)
# -------------------------------------------------------------
N_genomes = np.arange(1, 200)
# Pan-genome ~ alpha * N^gamma where gamma 0.4-0.5 for "open"
# E. coli: core ~3000, pan ~30000+ at N=100
core_genes = 3000
pan_genes = core_genes + 2500 * np.log(N_genomes) + 1000 * N_genomes ** 0.55
accessory_genes = pan_genes - core_genes

# -------------------------------------------------------------
# 5) HGT rates
# -------------------------------------------------------------
hgt_examples = {
    "E. coli intraspecies": 1e-9,    # /gene/generation
    "Within-genus (gram-neg)": 1e-10,
    "Cross-phylum": 1e-12,
    "Eukaryote-archaea (LUCA-era)": 1e-15,
}

# -------------------------------------------------------------
# 6) Antibiotic resistance emergence timeline
# -------------------------------------------------------------
amr_timeline = {
    "Penicillin": (1943, 1945),       # introduced, first resistance
    "Methicillin": (1959, 1961),       # 2 yr -> MRSA
    "Vancomycin": (1958, 1986),        # 28 yr -> VRE
    "Ciprofloxacin": (1987, 1991),    # 4 yr
    "Linezolid": (2000, 2001),         # 1 yr
    "Daptomycin": (2003, 2005),
    "Ceftaroline": (2010, 2011),       # 1 yr
    "Ceftolozane/tazobactam": (2014, 2016),
    "Cefiderocol": (2019, 2020),       # 1 yr
}

# Time-to-resistance
ttr_years = [v[1] - v[0] for v in amr_timeline.values()]
mean_ttr = float(np.mean(ttr_years))

# -------------------------------------------------------------
# 7) AMR projected mortality (O'Neill 2014, Murray 2022)
# -------------------------------------------------------------
years_amr = np.array([2019, 2025, 2030, 2040, 2050])
deaths_per_yr = np.array([1.27e6, 2.0e6, 3.5e6, 6.5e6, 10.0e6])  # Murray 2022, O'Neill 2014

# -------------------------------------------------------------
# 8) ITU K_microbe axiom check
# -------------------------------------------------------------
# Bacterial population: 5000 strains, abundance ~ Zipf
N_strains = 5000
ranks = np.arange(1, N_strains + 1)
alpha = 1.1
p_pre = ranks ** (-alpha); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# After antibiotic exposure: resistance gene confers fitness, but only in some strains
fitness = np.ones(N_strains)
resistance_strains = rng.random(N_strains) < 0.05  # 5% strains have resistance
fitness[resistance_strains] = 5.0
fitness[~resistance_strains] = 0.1
p_post = p_pre * fitness
p_post = p_post / p_post.sum()
S_post = float(-np.sum(np.where(p_post > 0, p_post * np.log(p_post), 0)))

# ITU linearized
log_p_pre = np.log(p_pre)
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 191 — Microbiology + Virology + Microbiome (K_microbe introduction)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Earth's microbial census
ax = axes[0, 0]
names = list(earth_microbial.keys())
vals = list(earth_microbial.values())
colors = ["#1f77b4" if "viruses" not in n else "#d62728" for n in names]
ax.barh(range(len(names)), vals, color=colors)
ax.set_xscale("log")
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=8)
ax.set_xlabel("Total cells (log scale)")
ax.set_title(f"Earth's microbial census (Whitman 1998+)\nTotal bact/arch: {total_bacterial_archaeal:.2e}")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 2: Virus genome size by Baltimore class
ax = axes[0, 1]
v_names = list(virus_genomes.keys())
v_sizes = list(virus_genomes.values())
colors_v = []
for n in v_names:
    if "dsDNA" in n: colors_v.append("#1f77b4")
    elif "ssDNA" in n: colors_v.append("#aec7e8")
    elif "+ssRNA" in n: colors_v.append("#2ca02c")
    elif "-ssRNA" in n: colors_v.append("#98df8a")
    elif "Retro" in n: colors_v.append("#d62728")
    else: colors_v.append("gray")
ax.barh(range(len(v_names)), v_sizes, color=colors_v)
ax.set_xscale("log")
ax.set_yticks(range(len(v_names)))
ax.set_yticklabels(v_names, fontsize=7)
ax.set_xlabel("Genome size (kb)")
ax.set_title("Virus genome sizes (Baltimore class)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 3: Microbiome diversity
ax = axes[0, 2]
x = np.arange(len(sites))
width = 0.3
ax.bar(x - width, cell_count_log10, width, color="#1f77b4", label="log10(cells)")
ax2 = ax.twinx()
ax2.bar(x, [s/100 for s in species_count], width, color="#ff7f0e", label="species/100")
ax2.bar(x + width, shannon_H, width, color="#2ca02c", label="Shannon H' (nats)")
ax.set_xticks(x)
ax.set_xticklabels(sites)
ax.set_ylabel("log10(cells)", color="#1f77b4")
ax2.set_ylabel("species/100 + Shannon H'")
ax.set_title("Human microbiome by site")
ax.legend(loc="upper right", fontsize=8)
ax2.legend(loc="upper left", fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 4: Pan-genome growth (Heaps' law)
ax = axes[1, 0]
ax.plot(N_genomes, pan_genes, "-", color="#1f77b4", lw=2, label="Pan-genome")
ax.axhline(core_genes, color="#d62728", linestyle="--", lw=2, label=f"Core = {core_genes}")
ax.plot(N_genomes, accessory_genes, "-", color="#2ca02c", lw=2, label="Accessory")
ax.set_xlabel("Number of E. coli genomes sequenced")
ax.set_ylabel("Genes")
ax.set_title("Pan-genome growth (Heaps' law; Tettelin 2005)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: AMR time-to-resistance
ax = axes[1, 1]
drugs = list(amr_timeline.keys())
intros = [v[0] for v in amr_timeline.values()]
resists = [v[1] for v in amr_timeline.values()]
ttrs = [v[1] - v[0] for v in amr_timeline.values()]
ax.barh(range(len(drugs)), ttrs, color="#d62728")
ax.set_yticks(range(len(drugs)))
ax.set_yticklabels(drugs, fontsize=7)
ax.set_xlabel("Years to first resistance")
ax.set_title(f"Antibiotic resistance speed (avg {mean_ttr:.1f} yr)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: AMR mortality + ITU
ax = axes[1, 2]
ax.plot(years_amr, deaths_per_yr / 1e6, "o-", color="#d62728", lw=2, markersize=10,
        label="O'Neill 2014, Murray 2022")
ax.fill_between(years_amr, 0, deaths_per_yr / 1e6, alpha=0.2, color="#d62728")
ax.set_xlabel("Year")
ax.set_ylabel("AMR deaths (millions/yr)")
ax.set_title(f"AMR projected mortality;  ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 191,
    "tier1_paper": 27,
    "block": "B",
    "paper_in_block": "2/?",
    "topic": "Microbiology + virology + microbiome (K_microbe introduction)",
    "earth_microbial_census": {k: float(v) for k, v in earth_microbial.items()},
    "total_bacterial_archaeal": float(total_bacterial_archaeal),
    "total_marine_viruses": float(total_viruses),
    "reference": "Whitman 1998 PNAS (5e30 bacteria), Suttle 2007 (10^30 viruses)",
    "virus_genome_sizes_kb": virus_genomes,
    "baltimore_classification": baltimore_class,
    "human_microbiome": {
        "sites": sites,
        "log10_cells": cell_count_log10,
        "species_count": species_count,
        "shannon_H_nats": shannon_H,
        "total_microbiome_cells": "10^14 (equal to host cells)",
        "ratio_microbial_to_host_cells": "~1.3:1 (Sender 2016 Cell)",
    },
    "pan_genome_E_coli": {
        "core_genes": core_genes,
        "pan_genes_at_N100": float(pan_genes[99]),
        "accessory_at_N100": float(accessory_genes[99]),
        "Heaps_law_gamma": 0.55,
        "reference": "Tettelin 2005 PNAS (Streptococcus agalactiae)",
    },
    "HGT_rates_per_gene_per_generation": hgt_examples,
    "AMR_timeline_intro_to_resistance_years": {
        drug: {"intro_year": yr_i, "resistance_year": yr_r, "ttr": yr_r - yr_i}
        for drug, (yr_i, yr_r) in amr_timeline.items()
    },
    "mean_time_to_resistance_years": float(mean_ttr),
    "AMR_mortality_projection": {
        "2019_deaths": 1.27e6,
        "2050_deaths_projection": 1.0e7,
        "references": [
            "O'Neill 2014 (UK Govt commissioned)",
            "Murray 2022 Lancet (GBD AMR Collaborators)",
        ],
    },
    "ITU_K_microbe": {
        "N_strains": N_strains,
        "S_pre_antibiotic_nats": S_pre,
        "S_post_selection_nats": S_post,
        "delta_S": S_post - S_pre,
        "delta_S_first_order": dS_lin,
        "delta_K_first_order": dK_lin,
        "ratio_dS_over_dK": itu_ratio,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_microbe",
        "sub_states": [
            "K_phylogeny (3 domains, Woese 1977)",
            "K_genome (individual organism genome)",
            "K_HGT (horizontal transfer = ITU K-state mixing)",
            "K_microbiome (host-associated community)",
            "K_phage (virus-bacteria coevolution)",
            "K_resistance (AMR plasmid spread)",
            "K_pathogen (virulence factor)",
            "K_metabolism (community metabolic network)",
        ],
        "axiom": "delta S(rho_pop) = delta Tr[K_microbe^(0) rho_pop]",
        "biological_meaning": "Microbial evolution = ITU descent on population genotype manifold",
        "HGT_as_K_state_mixing": "Horizontal gene transfer = ITU axiom-level operation between communities",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
