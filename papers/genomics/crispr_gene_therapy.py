"""
Phase 216 — CRISPR + Gene Editing + Gene Therapy (K_genome_edit)

Simulations:
  1) CRISPR-Cas9 mechanism (sgRNA + PAM)
  2) NHEJ vs HDR efficiency
  3) CRISPR variants comparison (Cas9/Cas12/Cas13/BE/PE)
  4) Approved gene therapy timeline + prices
  5) Casgevy 2023 clinical efficacy
  6) Prime Editor pathogenic variant coverage
  7) ITU K_genome_edit axiom

Outputs:
  - crispr_gene_therapy.png
  - crispr_gene_therapy_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("crispr_gene_therapy.png")
OUT_JSON = Path(__file__).with_name("crispr_gene_therapy_summary.json")

rng = np.random.default_rng(20260626)

# -------------------------------------------------------------
# 1) CRISPR-Cas9 mechanism
# -------------------------------------------------------------
crispr_mechanism = {
    "sgRNA_target_length_bp": 20,
    "PAM_sequence": "NGG",
    "Cas9_source": "Streptococcus pyogenes",
    "cleavage_site": "3 bp upstream of PAM",
    "discoverers_2012": "Jinek, Doudna, Charpentier (Science)",
    "Nobel_Chemistry_2020": "Doudna + Charpentier",
}

# -------------------------------------------------------------
# 2) NHEJ vs HDR efficiency
# -------------------------------------------------------------
cell_types = ["Mouse ESC", "Human iPSC", "Primary T cell", "HSC", "Neuron",
              "Fibroblast", "Cardiomyocyte"]
nhej_eff = [85, 75, 70, 60, 30, 80, 25]
hdr_eff = [25, 15, 8, 5, 1, 12, 2]

# -------------------------------------------------------------
# 3) CRISPR variants
# -------------------------------------------------------------
crispr_variants = {
    "Cas9 (DSB)":           {"year": 2012, "DSB": True,  "edit_type": "indel/KO"},
    "Cas12 (Cpf1)":         {"year": 2015, "DSB": True,  "edit_type": "blunt cut"},
    "Cas13 (RNA)":          {"year": 2016, "DSB": False, "edit_type": "RNA degradation"},
    "Base Editor (BE)":     {"year": 2016, "DSB": False, "edit_type": "C→T / A→G"},
    "Prime Editor (PE)":    {"year": 2019, "DSB": False, "edit_type": "any small edit ★"},
    "dCas9 (CRISPRi/a)":    {"year": 2013, "DSB": False, "edit_type": "transcription mod"},
}

# -------------------------------------------------------------
# 4) Approved gene therapies (extended from Phase 215)
# -------------------------------------------------------------
gene_therapies = {
    "Glybera (2012, EU)":         {"year": 2012, "price_M": 1.0,  "tech": "AAV1"},
    "Luxturna (2017)":            {"year": 2017, "price_M": 0.85, "tech": "AAV2"},
    "Zolgensma (2019)":           {"year": 2019, "price_M": 2.1,  "tech": "AAV9"},
    "Hemgenix (2022)":            {"year": 2022, "price_M": 3.5,  "tech": "AAV5"},
    "Casgevy CRISPR (2023) ★":    {"year": 2023, "price_M": 2.2,  "tech": "CRISPR-Cas9"},
    "Lyfgenia (2023)":            {"year": 2023, "price_M": 3.1,  "tech": "Lentiviral"},
    "Roctavian (2023)":           {"year": 2023, "price_M": 2.9,  "tech": "AAV5"},
}

# -------------------------------------------------------------
# 5) Casgevy clinical efficacy (Phase III)
# -------------------------------------------------------------
casgevy_efficacy = {
    "Pain-free 1 year":      89,
    "Hospitalization free":  93,
    "Transfusion free":      96,
    "Adverse events G3+":    18,
}

# -------------------------------------------------------------
# 6) Prime Editor coverage
# -------------------------------------------------------------
variant_types = {
    "Substitutions": 60,    # % of pathogenic
    "Insertions <40bp": 21,
    "Deletions <40bp": 8,
    "Total PE-editable": 89,
    "PE non-editable (large SV)": 11,
}

# -------------------------------------------------------------
# 7) ITU K_genome_edit axiom
# -------------------------------------------------------------
N_genome_states = 5000
# Pre-edit: pathogenic variant fixed (peaked on disease state)
log_fit_disease = -((np.arange(N_genome_states) - 1500) ** 2) / 5000
p_disease = np.exp(log_fit_disease); p_disease /= p_disease.sum()
S_disease = float(-np.sum(p_disease * np.log(p_disease)))

# Post-edit (CRISPR-corrected): healthy state restored
log_fit_healthy = -((np.arange(N_genome_states) - 3500) ** 2) / 5000
p_healthy = np.exp(log_fit_healthy); p_healthy /= p_healthy.sum()
S_healthy = float(-np.sum(p_healthy * np.log(p_healthy)))

# Off-target / partial edit (mixed state)
log_fit_mixed = 0.3 * log_fit_disease + 0.7 * log_fit_healthy
p_mixed = np.exp(log_fit_mixed); p_mixed /= p_mixed.sum()
S_mixed = float(-np.sum(p_mixed * np.log(p_mixed)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_disease_healthy = itu_lin(p_disease, p_healthy)
ratio_disease_mixed = itu_lin(p_disease, p_mixed)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 216 — CRISPR + Gene Editing + Gene Therapy (K_genome_edit)",
    fontsize=13, fontweight="bold",
)

# Panel 1: CRISPR-Cas9 mechanism schematic (text-only)
ax = axes[0, 0]
ax.axis("off")
mech_text = [
    "CRISPR-Cas9 Mechanism",
    "",
    "1. sgRNA (20 bp) loaded into Cas9",
    "2. Cas9-sgRNA scans DNA for PAM",
    "3. PAM = NGG (3 bp)",
    "4. sgRNA-DNA matching (20 bp)",
    "5. Cas9 creates DSB",
    "6. NHEJ → indel (KO)",
    "   HDR → template repair (knock-in)",
    "",
    "Nobel Chemistry 2020:",
    "Doudna + Charpentier",
]
for i, line in enumerate(mech_text):
    ax.text(0.05, 0.95 - i * 0.075, line, fontsize=10, fontweight="bold" if i == 0 else "normal",
            color="#d62728" if "Nobel" in line else "black")

# Panel 2: NHEJ vs HDR efficiency
ax = axes[0, 1]
x = np.arange(len(cell_types))
width = 0.35
ax.bar(x - width/2, nhej_eff, width, color="#1f77b4", label="NHEJ %")
ax.bar(x + width/2, hdr_eff, width, color="#d62728", label="HDR %")
ax.set_xticks(x); ax.set_xticklabels(cell_types, rotation=30, fontsize=7, ha="right")
ax.set_ylabel("Efficiency (%)")
ax.set_title("DSB repair: NHEJ vs HDR by cell type")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: CRISPR variants timeline
ax = axes[0, 2]
v_names = list(crispr_variants.keys())
v_years = [crispr_variants[k]["year"] for k in v_names]
v_colors = ["#d62728" if crispr_variants[k]["DSB"] else "#2ca02c" for k in v_names]
ax.barh(range(len(v_names)), v_years, color=v_colors)
ax.set_yticks(range(len(v_names))); ax.set_yticklabels(v_names, fontsize=7)
ax.set_xlim(2011, 2024)
ax.set_xlabel("Year")
ax.set_title("CRISPR variants (red=DSB, green=no DSB)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: Gene therapy prices
ax = axes[1, 0]
gt_names = list(gene_therapies.keys())
gt_prices = [gene_therapies[k]["price_M"] for k in gt_names]
gt_colors = ["#d62728" if "CRISPR" in k else "#ff7f0e" if gt_prices[i] > 2.5 else "#2ca02c"
             for i, k in enumerate(gt_names)]
ax.barh(range(len(gt_names)), gt_prices, color=gt_colors)
ax.set_yticks(range(len(gt_names))); ax.set_yticklabels(gt_names, fontsize=7)
ax.set_xlabel("Price ($M / dose)")
ax.set_title("FDA-approved gene therapies + prices")
ax.grid(True, alpha=0.3, axis="x")

# Panel 5: Casgevy efficacy
ax = axes[1, 1]
metrics = list(casgevy_efficacy.keys())
vals = list(casgevy_efficacy.values())
colors_c = ["#2ca02c" if v > 80 else "#ff7f0e" if v > 40 else "#d62728" for v in vals]
ax.bar(metrics, vals, color=colors_c)
ax.set_ylabel("Patients (%)")
ax.set_title("Casgevy Phase III (CLIMB-121, 2023)")
ax.tick_params(axis="x", rotation=15, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(vals):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=10, fontweight="bold")

# Panel 6: ITU K_genome_edit
ax = axes[1, 2]
labels_g = ["Pre-edit\n(disease)", "Post-edit\n(healthy)", "Off-target\n(mixed)"]
S_vals = [S_disease, S_healthy, S_mixed]
ax.bar(labels_g, S_vals, color=["#d62728", "#2ca02c", "#ff7f0e"])
ax.set_ylabel("Genome state entropy (nats)")
ax.set_title(f"K_genome_edit: D→H={ratio_disease_healthy:.3f}, D→Mixed={ratio_disease_mixed:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 216,
    "tier1_paper": 30,
    "block": "B",
    "topic": "CRISPR + Gene editing + Gene therapy (K_genome_edit)",
    "CRISPR_mechanism": crispr_mechanism,
    "DSB_repair_efficiency": {
        "cell_types": cell_types,
        "NHEJ_pct": nhej_eff,
        "HDR_pct": hdr_eff,
        "NHEJ_dominance": "NHEJ ~10× HDR in most cells",
    },
    "CRISPR_variants": crispr_variants,
    "Prime_Editor_2019_Liu": {
        "paper": "Anzalone et al. 2019 Nature",
        "mechanism": "Nickase + reverse transcriptase",
        "DSB_free": True,
        "editable_pathogenic_variants_pct": 89,
    },
    "Casgevy_2023": {
        "UK_approval": "2023-11",
        "FDA_approval": "2023-12",
        "EMA_approval": "2024",
        "developer": "Vertex + CRISPR Therapeutics",
        "target": "BCL11A (HbF reactivation)",
        "Phase_III_CLIMB_121": casgevy_efficacy,
        "price_USD": 2.2e6,
        "significance": "First CRISPR-Cas9 therapy worldwide",
    },
    "gene_therapies_approved": gene_therapies,
    "He_Jiankui_2018": {
        "act": "First germline-edited CRISPR babies (Lulu + Nana)",
        "target": "CCR5 KO (HIV resistance)",
        "punishment": "3 years prison + $430K fine (China)",
        "international_consensus": "Germline editing = scientific misconduct",
    },
    "WHO_2023_framework": "Heritable editing tightly regulated; somatic accelerated",
    "ITU_K_genome_edit": {
        "N_genome_states": N_genome_states,
        "S_disease_nats": S_disease,
        "S_healthy_nats": S_healthy,
        "S_mixed_nats": S_mixed,
        "disease_to_healthy_ratio": ratio_disease_healthy,
        "disease_to_mixed_ratio": ratio_disease_mixed,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_genome_edit",
        "modular_Hamiltonian": "K_genome_edit^(0) = -log P(corrected genome | guide RNA, repair)",
        "CRISPR_meaning": "Direct K_genome operator with PAM specificity",
        "Base_Editor_meaning": "Subtle K-state shift (single nucleotide) without DSB",
        "Prime_Editor_meaning": "Programmable K-state operator (any small edit)",
        "Casgevy_significance": "First clinical-grade K_genome operator FDA-approved",
    },
    "predictions": [
        ("Prime Editor clinical (1 indication)", 2028, 0.75, "Strong"),
        ("In vivo CRISPR (mRNA-LNP)", 2028, 0.80, "Strong"),
        ("Heritable editing legal framework (international)", 2032, 0.45, "Medium"),
        ("CRISPR drug 10+ indications approved", 2030, 0.85, "Strong"),
        ("Synthetic yeast complete genome", 2028, 0.70, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
