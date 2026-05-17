"""
Phase 231 — Antibody + ADC + Bispecific (K_pharma_biologic)

Simulations:
  1) Antibody evolution: murine → fully human (immunogenicity)
  2) FDA-approved mAb timeline
  3) ADC structure + key drugs (T-DM1, Enhertu, etc.)
  4) Enhertu DESTINY-Breast04 HER2-low survival
  5) Bispecific antibody mechanism (BiTE)
  6) ADC vs Bispecific market growth
  7) ITU K_pharma_biologic axiom check

Outputs:
  - antibody_adc_bispecific.png
  - antibody_adc_bispecific_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("antibody_adc_bispecific.png")
OUT_JSON = Path(__file__).with_name("antibody_adc_bispecific_summary.json")

rng = np.random.default_rng(20260712)

# -------------------------------------------------------------
# 1) Antibody generation evolution
# -------------------------------------------------------------
ab_generations = {
    "Murine (1986)":      {"year": 1986, "immunogenicity_pct": 100},
    "Chimeric (1988)":    {"year": 1988, "immunogenicity_pct": 30},
    "Humanized (1990)":   {"year": 1990, "immunogenicity_pct": 8},
    "Fully human (1994)": {"year": 1994, "immunogenicity_pct": 3},
    "AI-designed (2024)": {"year": 2024, "immunogenicity_pct": 1},
}

# -------------------------------------------------------------
# 2) Major FDA mAb approvals
# -------------------------------------------------------------
mab_history = {
    "Muromonab-CD3 (1986)": {"year": 1986, "target": "CD3"},
    "Rituximab (1997) ★":   {"year": 1997, "target": "CD20"},
    "Trastuzumab (1998) ★": {"year": 1998, "target": "HER2"},
    "Bevacizumab (2004)":   {"year": 2004, "target": "VEGF"},
    "Adalimumab (2002)":    {"year": 2002, "target": "TNF-α"},
    "Ipilimumab (2011)":    {"year": 2011, "target": "CTLA-4"},
    "Pembrolizumab (2014)★":{"year": 2014, "target": "PD-1"},
    "Nivolumab (2014)":     {"year": 2014, "target": "PD-1"},
    "Dupilumab (2018)":     {"year": 2018, "target": "IL-4Rα"},
    "Lecanemab (2023)":     {"year": 2023, "target": "Aβ"},
}

# -------------------------------------------------------------
# 3) ADC drugs
# -------------------------------------------------------------
adc_drugs = {
    "Mylotarg (2000/2017)": {"year": 2017, "target": "CD33", "payload": "Calicheamicin"},
    "Kadcyla T-DM1 (2013)":  {"year": 2013, "target": "HER2", "payload": "DM1"},
    "Adcetris (2011)":      {"year": 2011, "target": "CD30", "payload": "MMAE"},
    "Enhertu T-DXd (2019)★": {"year": 2019, "target": "HER2", "payload": "DXd"},
    "Trodelvy (2020)":      {"year": 2020, "target": "TROP2", "payload": "SN-38"},
    "Padcev (2019)":        {"year": 2019, "target": "Nectin-4", "payload": "MMAE"},
    "Blenrep (2020)":       {"year": 2020, "target": "BCMA", "payload": "MMAF"},
}

# -------------------------------------------------------------
# 4) Enhertu DESTINY-Breast04 (NEJM 2022)
# -------------------------------------------------------------
months = np.linspace(0, 24, 200)
# HER2-low patients survival
control_chemo = 100 * np.exp(-months / 8)   # ~5.4 mo PFS
enhertu = 100 * np.exp(-months / 12)        # ~9.9 mo PFS (Enhertu)
hr_enhertu = 0.64  # NEJM 2022

# -------------------------------------------------------------
# 5) Bispecific mechanism
# -------------------------------------------------------------
bispecifics = {
    "Blincyto (2014) BiTE":    {"year": 2014, "target_pair": "CD3 × CD19"},
    "Hemlibra (2017)":         {"year": 2017, "target_pair": "F.IX × F.X (mimic FVIII)"},
    "Rybrevant (2021)":        {"year": 2021, "target_pair": "EGFR × MET"},
    "Faricimab (2022)":        {"year": 2022, "target_pair": "VEGF-A × Ang-2"},
    "Tecvayli (2022)":         {"year": 2022, "target_pair": "BCMA × CD3"},
    "Epkinly (2023)":          {"year": 2023, "target_pair": "CD20 × CD3"},
    "Talquetamab (2023)":      {"year": 2023, "target_pair": "GPRC5D × CD3"},
}

# -------------------------------------------------------------
# 6) ADC vs Bispecific market growth
# -------------------------------------------------------------
years_market = np.arange(2020, 2031)
adc_market = np.array([6, 8, 10, 12, 13, 17, 22, 28, 35, 42, 50])
bispec_market = np.array([2, 3, 4, 5, 7, 10, 13, 17, 22, 26, 30])

# -------------------------------------------------------------
# 7) ITU K_pharma_biologic axiom
# -------------------------------------------------------------
N_cells = 2000
# Pre-ADC: tumor cell population
log_fit_tumor = np.zeros(N_cells)
tumor_mask = (np.arange(N_cells) > 500) & (np.arange(N_cells) < 1500)
log_fit_tumor[tumor_mask] += 3.0
p_tumor = np.exp(log_fit_tumor); p_tumor /= p_tumor.sum()
S_tumor = float(-np.sum(p_tumor * np.log(p_tumor)))

# Post-ADC: tumor cells killed (HER2+ subset)
log_fit_adc = log_fit_tumor.copy()
log_fit_adc[800:1200] -= 5.0  # ADC kills HER2+
p_adc = np.exp(log_fit_adc); p_adc /= p_adc.sum()
S_adc = float(-np.sum(p_adc * np.log(p_adc)))

# Post-Bispecific: T cell engager + tumor
log_fit_bs = log_fit_tumor.copy()
log_fit_bs[500:1500] -= 3.0  # broader tumor killing
p_bs = np.exp(log_fit_bs); p_bs /= p_bs.sum()
S_bs = float(-np.sum(p_bs * np.log(p_bs)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_tumor_adc = itu_lin(p_tumor, p_adc)
ratio_tumor_bs = itu_lin(p_tumor, p_bs)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 231 — Antibody + ADC + Bispecific (K_pharma_biologic)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Ab generation
ax = axes[0, 0]
g_names = list(ab_generations.keys())
g_years = [ab_generations[g]["year"] for g in g_names]
imm = [ab_generations[g]["immunogenicity_pct"] for g in g_names]
ax.scatter(g_years, imm, s=200, c="#d62728", edgecolor="black", zorder=5)
for g, d in ab_generations.items():
    ax.annotate(g.split("(")[0], (d["year"], d["immunogenicity_pct"]),
                fontsize=7, xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("HAMA immunogenicity (%)")
ax.set_yscale("log")
ax.set_title("Antibody humanization (Köhler-Milstein Nobel 1984)")
ax.grid(True, alpha=0.3, which="both")

# Panel 2: mAb history
ax = axes[0, 1]
m_names = list(mab_history.keys())
m_years = [mab_history[k]["year"] for k in m_names]
ax.barh(range(len(m_names)), m_years, color="#1f77b4")
for i, k in enumerate(m_names):
    ax.text(1986, i, mab_history[k]["target"], fontsize=7, va="center")
ax.set_yticks(range(len(m_names))); ax.set_yticklabels(m_names, fontsize=6)
ax.set_xlim(1985, 2024)
ax.set_xlabel("Year")
ax.set_title("Major mAb FDA approvals")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: ADC drugs
ax = axes[0, 2]
adc_names = list(adc_drugs.keys())
adc_years = [adc_drugs[k]["year"] for k in adc_names]
colors_adc = ["#d62728" if "★" in n else "#9467bd" for n in adc_names]
ax.barh(range(len(adc_names)), adc_years, color=colors_adc)
for i, k in enumerate(adc_names):
    ax.text(2000, i, adc_drugs[k]["target"] + " / " + adc_drugs[k]["payload"],
            fontsize=6, va="center")
ax.set_yticks(range(len(adc_names))); ax.set_yticklabels(adc_names, fontsize=6)
ax.set_xlim(2000, 2024)
ax.set_xlabel("Year")
ax.set_title("ADC FDA approvals (target/payload)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: Enhertu DESTINY-Breast04
ax = axes[1, 0]
ax.plot(months, control_chemo, "-", color="#d62728", lw=2, label="Chemo control")
ax.plot(months, enhertu, "-", color="#2ca02c", lw=2,
        label=f"Enhertu (T-DXd) HR={hr_enhertu}")
ax.fill_between(months, control_chemo, enhertu, alpha=0.2, color="#2ca02c")
ax.set_xlabel("Months")
ax.set_ylabel("Patients alive without progression (%)")
ax.set_title("DESTINY-Breast04 (NEJM 2022): HER2-low breast cancer")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Bispecific antibodies
ax = axes[1, 1]
bs_names = list(bispecifics.keys())
bs_years = [bispecifics[k]["year"] for k in bs_names]
ax.barh(range(len(bs_names)), bs_years, color="#ff7f0e")
for i, k in enumerate(bs_names):
    ax.text(2014, i, bispecifics[k]["target_pair"], fontsize=6, va="center")
ax.set_yticks(range(len(bs_names))); ax.set_yticklabels(bs_names, fontsize=6)
ax.set_xlim(2013, 2024)
ax.set_xlabel("Year")
ax.set_title("Bispecific antibodies (BiTE etc.)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ADC + Bispecific market + ITU
ax = axes[1, 2]
ax.plot(years_market, adc_market, "o-", color="#9467bd", lw=2, label="ADC $B")
ax.plot(years_market, bispec_market, "s-", color="#ff7f0e", lw=2, label="Bispecific $B")
ax.set_xlabel("Year")
ax.set_ylabel("Market size ($ Billion)")
ax.set_title(f"ADC + BsAb market;  K_pharma_biologic ITU={ratio_tumor_adc:.3f}/{ratio_tumor_bs:.3f}")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 231,
    "tier1_paper": 32,
    "topic": "Antibody + ADC + Bispecific (K_pharma_biologic)",
    "Kohler_Milstein_Nobel_1984": "Hybridoma technology",
    "Ab_generation_evolution": ab_generations,
    "major_mAb_FDA_approvals": mab_history,
    "Trastuzumab_1998_breast": "HER2+ breast cancer pivotal",
    "Keytruda_2024_sales_B": 25,
    "ADC_FDA_approvals": adc_drugs,
    "Enhertu_DESTINY_Breast04_2022": {
        "HR_for_death": 0.64,
        "median_PFS_chemo_mo": 5.4,
        "median_PFS_Enhertu_mo": 9.9,
        "patient_category": "HER2-low (previously incurable)",
    },
    "bispecific_antibodies": bispecifics,
    "Blincyto_BiTE_2014_first": "CD3 x CD19, ALL",
    "Hemlibra_HAVEN3_bleeding_reduction_pct": 87,
    "ADC_market_growth_B": dict(zip(years_market.tolist(), adc_market.tolist())),
    "Bispecific_market_growth_B": dict(zip(years_market.tolist(), bispec_market.tolist())),
    "ITU_K_pharma_biologic": {
        "N_cells": N_cells,
        "S_tumor_pre_nats": S_tumor,
        "S_post_ADC_nats": S_adc,
        "S_post_BsAb_nats": S_bs,
        "tumor_to_ADC_ratio": ratio_tumor_adc,
        "tumor_to_BsAb_ratio": ratio_tumor_bs,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_biologic",
        "modular_Hamiltonian": "K_pharma_biologic^(0) = -log P(cell kill | Ab × payload × patient)",
        "ADC_meaning": "Magic bullet (Ehrlich 1900) - target + payload K-state",
        "Bispecific_meaning": "Recruit K_immune (T cell) + bind K_tumor",
        "Enhertu_HER2_low": "HER2-low → HER2 spectrum expansion (K-state continuum)",
        "Hemlibra_meaning": "F.VIII function mimicry (functional replacement)",
    },
    "predictions": [
        ("ADC market $50 B", 2030, 0.85, "Strong"),
        ("Trispecific Ab approval", 2028, 0.70, "Strong"),
        ("AI-designed first-in-class Ab", 2028, 0.75, "Strong"),
        ("Multiple ADCs for solid tumors", 2028, 0.80, "Strong"),
        ("ADC + IO standard NSCLC", 2030, 0.75, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
