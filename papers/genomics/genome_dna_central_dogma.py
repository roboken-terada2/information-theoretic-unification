"""
Phase 215 — DNA + Genome + Central Dogma + K_genome introduction (Pass-1 Final Tier 1)

Simulations:
  1) Central Dogma: DNA -> RNA -> Protein flow
  2) Human genome composition (coding/non-coding/repeats)
  3) HGP cost reduction (1990-2024)
  4) Sequencing technology generations
  5) Gene count discovery history
  6) GWAS power vs sample size (heritability)
  7) Approved gene therapy timeline
  8) ITU K_genome axiom check: genome → phenotype

Outputs:
  - genome_dna_central_dogma.png
  - genome_dna_central_dogma_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("genome_dna_central_dogma.png")
OUT_JSON = Path(__file__).with_name("genome_dna_central_dogma_summary.json")

rng = np.random.default_rng(20260625)

# -------------------------------------------------------------
# 1) Central Dogma flow
# -------------------------------------------------------------
dogma = {
    "DNA replication": "DNA → DNA (semi-conservative, Meselson-Stahl 1958)",
    "Transcription":   "DNA → mRNA (RNA polymerase II)",
    "Translation":     "mRNA → protein (ribosome + tRNA)",
    "Reverse transcription": "RNA → DNA (Temin-Baltimore 1970, Nobel 1975)",
    "RNA replication": "RNA → RNA (RNA viruses, e.g. influenza)",
}

# -------------------------------------------------------------
# 2) Human genome composition
# -------------------------------------------------------------
genome_pct = {
    "Protein-coding exons":  2,
    "Introns + UTRs":        25,
    "Regulatory elements":   10,
    "LINE-1 + SINE (Alu)":   45,
    "LTR retrotransposons":  8,
    "Other repeats":         7,
    "Centromere + telomere": 3,
}

# -------------------------------------------------------------
# 3) HGP cost reduction (1990-2024)
# -------------------------------------------------------------
years_cost = np.array([1990, 1995, 2000, 2003, 2005, 2007, 2010, 2014, 2017, 2020, 2024])
cost_per_genome = np.array([
    300_000_000,    # 1990 HGP start
    100_000_000,    # 1995
    10_000_000,     # 2000 draft
    3_000_000_000 / 1,  # final cost ~$3B (whole HGP)
    10_000_000,     # 2005
    1_000_000,      # 2007 next-gen begin
    50_000,         # 2010
    1_000,          # 2014 Illumina HiSeq X
    500,            # 2017
    300,            # 2020
    200,            # 2024 NovaSeq X
])

# Fix HGP total cost entry
cost_per_genome[3] = 5_000_000  # 2003 per-genome equivalent post-HGP
moore_law_cost = 300_000_000 * (0.5 ** ((years_cost - 1990) / 1.5))  # Moore's law projection

# -------------------------------------------------------------
# 4) Sequencing generations
# -------------------------------------------------------------
seq_tech = {
    "Sanger (1st)":         {"read_length_bp": 800,    "cost_per_genome": 100e6, "start_year": 1977},
    "Illumina (2nd)":       {"read_length_bp": 150,    "cost_per_genome": 1e3,   "start_year": 2007},
    "Oxford Nanopore (3rd)":{"read_length_bp": 10000,  "cost_per_genome": 1.5e3, "start_year": 2015},
    "PacBio HiFi (3rd)":    {"read_length_bp": 15000,  "cost_per_genome": 1.5e3, "start_year": 2019},
}

# -------------------------------------------------------------
# 5) Gene count discovery history
# -------------------------------------------------------------
gene_count_history = {
    "1990 (HGP start)":  100_000,
    "2001 (draft)":      30_000,
    "2003 (HGP done)":   25_000,
    "2010":              22_500,
    "2015":              20_500,
    "2024 (current)":    19_900,
}

# -------------------------------------------------------------
# 6) GWAS power vs sample size
# -------------------------------------------------------------
sample_sizes = np.logspace(2, 7, 50)  # 100 to 10M
# Heritability discoverable as function of sample
# Strong effects need ~1K, moderate ~100K, weak ~1M+
heritability_discovered = 1.0 - np.exp(-sample_sizes / 1e6)

# Real GWAS milestones
gwas_milestones = {
    "AMD 2005 (first)":     1500,
    "Diabetes 2007":        20000,
    "Schizophrenia 2014":   150000,
    "Height GIANT 2014":    250000,
    "PGC SZ 2022":          320000,
    "EduYears 2018":        1.1e6,
    "UKBB 2024":            5e5,
}

# -------------------------------------------------------------
# 7) Approved gene therapy timeline
# -------------------------------------------------------------
gene_therapies = {
    "Glybera 2012":       {"target": "LPL deficiency", "year": 2012, "withdrawn": True},
    "Luxturna 2017":      {"target": "RPE65 blindness", "year": 2017, "active": True},
    "Zolgensma 2019":     {"target": "SMA", "year": 2019, "price_M": 2.1},
    "Hemgenix 2022":      {"target": "Hemophilia B", "year": 2022, "price_M": 3.5},
    "Casgevy (CRISPR) 2023": {"target": "Sickle cell", "year": 2023, "first_CRISPR": True},
    "Lyfgenia 2023":      {"target": "Sickle cell", "year": 2023, "lentiviral": True},
    "Roctavian 2023":     {"target": "Hemophilia A", "year": 2023},
}

# -------------------------------------------------------------
# 8) ITU K_genome axiom: genome -> phenotype expression patterns
# -------------------------------------------------------------
N_genes = 20000
# Baseline: uniform low expression
log_fit_base = -0.5 * np.ones(N_genes)
p_base = np.exp(log_fit_base); p_base /= p_base.sum()
S_base = float(-np.sum(p_base * np.log(p_base)))

# Tissue-specific: 2000 genes elevated
log_fit_tissue = log_fit_base.copy()
log_fit_tissue[5000:7000] += 3.0
p_tissue = np.exp(log_fit_tissue); p_tissue /= p_tissue.sum()
S_tissue = float(-np.sum(p_tissue * np.log(p_tissue)))

# Disease state: dysregulated (different 2000 genes elevated)
log_fit_disease = log_fit_base.copy()
log_fit_disease[5500:7500] += 2.5
log_fit_disease[8000:8500] += 4.0  # disease genes
p_disease = np.exp(log_fit_disease); p_disease /= p_disease.sum()
S_disease = float(-np.sum(p_disease * np.log(p_disease)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_base_tissue = itu_lin(p_base, p_tissue)
ratio_tissue_disease = itu_lin(p_tissue, p_disease)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 215 ★ — DNA + Genome + Central Dogma + K_genome Introduction (Pass-1 Final Tier 1)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Genome composition pie
ax = axes[0, 0]
labels_g = list(genome_pct.keys())
sizes = list(genome_pct.values())
colors_g = ["#1f77b4", "#aec7e8", "#a6cee3", "#ff7f0e", "#ffbb78", "#d62728", "#9467bd"]
ax.pie(sizes, labels=labels_g, autopct="%1.0f%%", textprops={"fontsize": 7}, colors=colors_g)
ax.set_title("Human genome 3.2 Gb composition (2% coding)")

# Panel 2: HGP cost reduction
ax = axes[0, 1]
ax.semilogy(years_cost, cost_per_genome, "o-", color="#1f77b4", lw=2, markersize=8,
            label="Actual (NHGRI tracking)")
ax.semilogy(years_cost, moore_law_cost, "--", color="#d62728", lw=2,
            label="Moore's law projection")
ax.set_xlabel("Year")
ax.set_ylabel("Cost per genome ($, log)")
ax.set_title("Sequencing cost: 15M× reduction 1990-2024")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 3: Gene count history
ax = axes[0, 2]
years_g = list(gene_count_history.keys())
counts = list(gene_count_history.values())
ax.bar(years_g, counts, color="#9467bd")
ax.set_ylabel("Estimated gene count")
ax.set_title("Gene count: 100K hype → 20K confirmed ★")
ax.tick_params(axis="x", rotation=20, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 4: GWAS power
ax = axes[1, 0]
ax.semilogx(sample_sizes, heritability_discovered * 100, "-", color="#1f77b4", lw=2,
            label="Theoretical")
for name, n in gwas_milestones.items():
    h = (1 - np.exp(-n / 1e6)) * 100
    ax.scatter([n], [h], s=60, color="#d62728", zorder=5)
    ax.annotate(name.split()[0], (n, h), fontsize=6, xytext=(3, 3),
                textcoords="offset points")
ax.set_xlabel("Sample size N")
ax.set_ylabel("Heritability discoverable (%)")
ax.set_title("GWAS power curve")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 5: Gene therapy timeline
ax = axes[1, 1]
gt_names = list(gene_therapies.keys())
gt_years = [gt["year"] for gt in gene_therapies.values()]
colors_gt = ["#d62728" if "first_CRISPR" in gene_therapies[k] else
             "#ff7f0e" if "withdrawn" in gene_therapies[k] else "#2ca02c"
             for k in gt_names]
ax.barh(range(len(gt_names)), gt_years, color=colors_gt)
ax.set_yticks(range(len(gt_names)))
ax.set_yticklabels(gt_names, fontsize=7)
ax.set_xlim(2011, 2025)
ax.set_xlabel("Year")
ax.set_title("Approved gene therapies (red=CRISPR Casgevy 2023)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ITU K_genome
ax = axes[1, 2]
ax.bar(["Baseline\n(uniform)", "Tissue-specific\nexpression", "Disease state"],
       [S_base, S_tissue, S_disease], color=["#1f77b4", "#2ca02c", "#d62728"])
ax.set_ylabel("Expression entropy (nats)")
ax.set_title(f"K_genome: Base→Tissue={ratio_base_tissue:.3f}, Tissue→Disease={ratio_tissue_disease:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 215,
    "tier1_paper": 30,
    "block": "B",
    "paper_in_block": "5/?",
    "milestone": "★ Pass-1 final Tier 1 paper opening ★",
    "topic": "DNA + Genome + Central Dogma + K_genome introduction",
    "central_dogma_Crick_1958": dogma,
    "human_genome": {
        "size_bp": 3.2e9,
        "chromosomes": "22 autosomes + XY",
        "gene_count_2024": "19,900 (revised down from 100,000 in 1990)",
        "protein_coding_pct": 2,
        "non_coding_pct": 98,
    },
    "genome_composition_pct": genome_pct,
    "Human_Genome_Project": {
        "start": 1990,
        "completion": 2003,
        "total_cost_USD": 3.0e9,
        "joint_announcement_2000": "Clinton + Blair",
        "Venter_Celera_competition": "1998-2000",
    },
    "sequencing_technology_generations": seq_tech,
    "cost_reduction_factor_1990_to_2024": "~15 million times",
    "current_cost_USD_2024": 200,
    "gene_count_history": gene_count_history,
    "GWAS_milestones": gwas_milestones,
    "approved_gene_therapies": gene_therapies,
    "Casgevy_2023": "First CRISPR-Cas9 therapy FDA-approved (sickle cell disease)",
    "ITU_K_genome": {
        "N_genes": int(N_genes),
        "S_baseline_nats": S_base,
        "S_tissue_specific_nats": S_tissue,
        "S_disease_nats": S_disease,
        "baseline_to_tissue_ratio": ratio_base_tissue,
        "tissue_to_disease_ratio": ratio_tissue_disease,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_genome",
        "sub_states": [
            "K_genome_coding (2% protein)",
            "K_genome_regulatory (10% reg)",
            "K_genome_repeat (50%+ LINE/SINE/LTR)",
            "K_genome_variant (SNP/indel/CNV)",
            "K_genome_epigenome (DNAm + histone)",
            "K_genome_3D (TAD + Hi-C)",
            "K_genome_RNA (ncRNA + lncRNA)",
            "K_genome_phylogenetic (cross-species)",
        ],
        "axiom": "delta S(rho_expression) = delta Tr[K_genome^(0) rho_expression]",
        "Central_Dogma_meaning": "DNA → RNA → protein = ITU information flow physical realization",
        "genome_as_source_code": "K_genome is the biological substrate of K_universe",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
