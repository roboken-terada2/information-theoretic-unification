"""
Phase 229 — GPCR + Ion channel + Structural pharmacology (K_pharma_target)

Simulations:
  1) GPCR Class A/B/C/F distribution
  2) Major Nav/Kv/Cav/GABA ion channels
  3) GLP-1 weight loss comparison (semaglutide, tirzepatide)
  4) Kinase inhibitor history (Imatinib 2001 → modern)
  5) K+ vs Na+ selectivity (MacKinnon 1998)
  6) Biased agonism vs orthosteric
  7) ITU K_pharma_target axiom check

Outputs:
  - gpcr_ion_channel_pharma.png
  - gpcr_ion_channel_pharma_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("gpcr_ion_channel_pharma.png")
OUT_JSON = Path(__file__).with_name("gpcr_ion_channel_pharma_summary.json")

rng = np.random.default_rng(20260710)

# -------------------------------------------------------------
# 1) GPCR Class distribution
# -------------------------------------------------------------
gpcr_classes = {
    "Class A (rhodopsin-like)":  640,
    "Class B (secretin)":         33,
    "Class C (glutamate)":        22,
    "Class F (frizzled)":         11,
    "Adhesion":                   33,
    "Taste/Olfactory":            61,
}
total_gpcr = sum(gpcr_classes.values())

# -------------------------------------------------------------
# 2) Ion channel drugs
# -------------------------------------------------------------
ion_channel_drugs = {
    "Lidocaine (Nav)":      {"channel": "Nav", "use": "Local anesthetic"},
    "Carbamazepine (Nav)":  {"channel": "Nav", "use": "Antiepileptic"},
    "Amiodarone (Kv)":      {"channel": "Kv",  "use": "Antiarrhythmic"},
    "Amlodipine (Cav L)":   {"channel": "Cav", "use": "Hypertension"},
    "Verapamil (Cav L)":    {"channel": "Cav", "use": "Arrhythmia"},
    "Ziconotide (Cav N)":   {"channel": "Cav", "use": "Chronic pain"},
    "Diazepam (GABA-A)":    {"channel": "GABA","use": "Anxiety"},
    "Varenicline (nAChR)":  {"channel": "nAChR","use": "Smoking cessation"},
    "Capsaicin (TRPV1)":    {"channel": "TRP", "use": "Pain (topical)"},
}

# -------------------------------------------------------------
# 3) GLP-1 weight loss
# -------------------------------------------------------------
glp1_drugs = {
    "Exenatide (2005)":     {"weight_loss_pct": 4, "year": 2005},
    "Liraglutide (Saxenda)": {"weight_loss_pct": 6, "year": 2014},
    "Semaglutide (Ozempic)": {"weight_loss_pct": 12, "year": 2017},
    "Semaglutide (Wegovy)":  {"weight_loss_pct": 15, "year": 2021},
    "Tirzepatide (Mounjaro)": {"weight_loss_pct": 22, "year": 2022},
    "Retatrutide (trial)":   {"weight_loss_pct": 24, "year": 2024},
}

# -------------------------------------------------------------
# 4) Kinase inhibitor history
# -------------------------------------------------------------
kinase_drugs = {
    "Imatinib (Gleevec)":    {"year": 2001, "target": "BCR-ABL", "cancer": "CML"},
    "Erlotinib":             {"year": 2004, "target": "EGFR",    "cancer": "NSCLC"},
    "Sunitinib":             {"year": 2006, "target": "VEGFR",   "cancer": "RCC"},
    "Crizotinib":            {"year": 2011, "target": "ALK",     "cancer": "NSCLC"},
    "Vemurafenib":           {"year": 2011, "target": "BRAF",    "cancer": "Melanoma"},
    "Ibrutinib":             {"year": 2013, "target": "BTK",     "cancer": "CLL"},
    "Palbociclib":           {"year": 2015, "target": "CDK4/6",  "cancer": "Breast"},
    "Osimertinib":           {"year": 2015, "target": "EGFR T790M", "cancer": "NSCLC"},
    "Alpelisib":             {"year": 2019, "target": "PI3Kα",   "cancer": "Breast"},
    "Sotorasib":             {"year": 2021, "target": "KRAS G12C", "cancer": "NSCLC"},
}

# -------------------------------------------------------------
# 5) K+/Na+ selectivity (MacKinnon 1998)
# -------------------------------------------------------------
ions = {"K+": 1.33, "Na+": 0.95, "Rb+": 1.48, "Cs+": 1.67, "Li+": 0.60}  # ionic radius A
# KcsA selectivity (relative permeability)
selectivity = {"K+": 1.0, "Na+": 1e-4, "Rb+": 0.7, "Cs+": 0.2, "Li+": 1e-4}
K_Na_ratio = selectivity["K+"] / selectivity["Na+"]

# -------------------------------------------------------------
# 6) Biased agonism schematic
# -------------------------------------------------------------
agonist_types = {
    "Full agonist (balanced)":     {"G_protein": 1.0, "beta_arrestin": 1.0},
    "Partial agonist":             {"G_protein": 0.5, "beta_arrestin": 0.5},
    "G-biased (TRV130 oliceridine)":{"G_protein": 0.8, "beta_arrestin": 0.1},
    "β-arrestin biased":            {"G_protein": 0.1, "beta_arrestin": 0.8},
    "Antagonist":                  {"G_protein": 0.0, "beta_arrestin": 0.0},
    "Inverse agonist":             {"G_protein": -0.3, "beta_arrestin": -0.3},
}

# -------------------------------------------------------------
# 7) ITU K_pharma_target axiom
# -------------------------------------------------------------
N_pathways = 2000
# Apo (no drug): random low activity
log_fit_apo = -0.5 * np.ones(N_pathways) + 0.1 * rng.standard_normal(N_pathways)
p_apo = np.exp(log_fit_apo); p_apo /= p_apo.sum()
S_apo = float(-np.sum(p_apo * np.log(p_apo)))

# Full agonist: peaked at G + β-arrestin pathway
log_fit_full = log_fit_apo.copy()
log_fit_full[500:600] += 3.0  # G pathway
log_fit_full[1500:1600] += 3.0  # β-arrestin
p_full = np.exp(log_fit_full); p_full /= p_full.sum()
S_full = float(-np.sum(p_full * np.log(p_full)))

# Biased agonist: only G pathway
log_fit_biased = log_fit_apo.copy()
log_fit_biased[500:600] += 4.0  # G pathway strongly
log_fit_biased[1500:1600] += 0.5  # β-arrestin minimal
p_biased = np.exp(log_fit_biased); p_biased /= p_biased.sum()
S_biased = float(-np.sum(p_biased * np.log(p_biased)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_apo_full = itu_lin(p_apo, p_full)
ratio_apo_biased = itu_lin(p_apo, p_biased)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 229 — GPCR + Ion Channel + Structural Pharmacology (K_pharma_target)",
    fontsize=13, fontweight="bold",
)

# Panel 1: GPCR class
ax = axes[0, 0]
classes = list(gpcr_classes.keys())
counts = list(gpcr_classes.values())
colors_c = ["#d62728", "#ff7f0e", "#2ca02c", "#1f77b4", "#9467bd", "#8c564b"]
ax.pie(counts, labels=classes, autopct="%1.0f%%", colors=colors_c, textprops={"fontsize": 7})
ax.set_title(f"GPCR classes ({total_gpcr} human total) - Class A 80%")

# Panel 2: GLP-1 weight loss
ax = axes[0, 1]
glp1_names = list(glp1_drugs.keys())
wl = [glp1_drugs[g]["weight_loss_pct"] for g in glp1_names]
yrs = [glp1_drugs[g]["year"] for g in glp1_names]
ax.scatter(yrs, wl, s=150, c="#9467bd", edgecolor="black", zorder=5)
for g, d in glp1_drugs.items():
    ax.annotate(g.split("(")[0], (d["year"], d["weight_loss_pct"]),
                fontsize=7, xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("Weight loss (%)")
ax.set_title("GLP-1 evolution: 4% → 24% weight loss")
ax.grid(True, alpha=0.3)

# Panel 3: Kinase inhibitors
ax = axes[0, 2]
k_names = list(kinase_drugs.keys())
k_years = [kinase_drugs[k]["year"] for k in k_names]
ax.barh(range(len(k_names)), k_years, color="#1f77b4")
for i, k in enumerate(k_names):
    ax.text(2002, i, kinase_drugs[k]["target"], fontsize=7, va="center")
ax.set_yticks(range(len(k_names))); ax.set_yticklabels(k_names, fontsize=6)
ax.set_xlim(2000, 2024)
ax.set_xlabel("Year")
ax.set_title("Kinase inhibitors 2001-2024 (10 examples)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: K+/Na+ selectivity
ax = axes[1, 0]
ion_names = list(selectivity.keys())
sel_vals = list(selectivity.values())
colors_i = ["#2ca02c" if s > 0.5 else "#d62728" for s in sel_vals]
ax.bar(ion_names, sel_vals, color=colors_i)
ax.set_yscale("log")
ax.set_ylabel("Relative permeability (log)")
ax.set_title(f"KcsA selectivity (MacKinnon Nobel 2003); K/Na = {K_Na_ratio:.0e}")
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 5: Biased agonism
ax = axes[1, 1]
a_names = list(agonist_types.keys())
g_vals = [agonist_types[a]["G_protein"] for a in a_names]
ba_vals = [agonist_types[a]["beta_arrestin"] for a in a_names]
x = np.arange(len(a_names))
width = 0.35
ax.bar(x - width/2, g_vals, width, color="#1f77b4", label="G protein")
ax.bar(x + width/2, ba_vals, width, color="#d62728", label="β-arrestin")
ax.set_xticks(x); ax.set_xticklabels(a_names, rotation=15, fontsize=6, ha="right")
ax.set_ylabel("Response")
ax.set_title("Biased agonism (Lefkowitz 2007)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 6: ITU K_pharma_target
ax = axes[1, 2]
ax.bar(["Apo\n(no drug)", "Full agonist\n(balanced)", "Biased agonist\n(G only)"],
       [S_apo, S_full, S_biased], color=["#1f77b4", "#d62728", "#9467bd"])
ax.set_ylabel("Pathway entropy (nats)")
ax.set_title(f"K_pharma_target: Apo→Full={ratio_apo_full:.3f}, Apo→Biased={ratio_apo_biased:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 229,
    "tier1_paper": 32,
    "topic": "GPCR + Ion channel + Structural pharmacology (K_pharma_target)",
    "GPCR_classes": gpcr_classes,
    "GPCR_total_human": total_gpcr,
    "Lefkowitz_Kobilka_Nobel_2012": "β2-AR + Gs complex structure",
    "GPCR_crystallized_2024": "200+ (of 800)",
    "ion_channel_drugs": ion_channel_drugs,
    "MacKinnon_Nobel_2003": "KcsA K+ channel + selectivity filter",
    "K_Na_selectivity_ratio": float(K_Na_ratio),
    "GLP1_evolution": glp1_drugs,
    "GLP1_max_weight_loss_pct_2024": 24,
    "kinase_inhibitors_2001_2024": kinase_drugs,
    "Imatinib_2001_first_targeted_therapy": "CML 5y survival 5% -> 90%",
    "agonist_types": agonist_types,
    "biased_agonism_first_clinical": "TRV130 oliceridine FDA 2020",
    "ITU_K_pharma_target": {
        "N_pathways": N_pathways,
        "S_apo_nats": S_apo,
        "S_full_agonist_nats": S_full,
        "S_biased_agonist_nats": S_biased,
        "apo_to_full_ratio": ratio_apo_full,
        "apo_to_biased_ratio": ratio_apo_biased,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_target",
        "modular_Hamiltonian": "K_pharma_target^(0) = -log P(downstream | binding mode)",
        "biased_agonism_meaning": "Drug selects which K-state to activate (precision)",
        "GLP1_meaning": "Single GPCR + 24% weight loss = ITU K-state powerful operator",
        "Imatinib_meaning": "Targeted kinase inhibition = K-state cancer reversal",
        "allosteric_meaning": "Modulator at non-orthosteric site (selectivity advantage)",
    },
    "predictions": [
        ("All 800 GPCR cryo-EM structures", 2028, 0.80, "Strong"),
        ("GLP-1 5+ adaptations (CV/AD/addiction)", 2030, 0.85, "Strong"),
        ("Allosteric drug 10+ new FDA approvals", 2030, 0.75, "Strong"),
        ("Biased agonist mainstream class", 2028, 0.70, "Strong"),
        ("AI-designed allosteric drugs", 2028, 0.75, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
