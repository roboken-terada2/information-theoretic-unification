"""
Phase 232 — Vaccines + Immunotherapy deep (K_pharma_immune)

Simulations:
  1) Vaccine generations 1-6 (efficacy + dev time)
  2) COVID vaccine cumulative doses + lives saved
  3) Keytruda + Yervoy + Opdivo melanoma 5y survival
  4) CAR-T product CR rates
  5) TIL therapy: Lifileucel 2024 FDA
  6) Cancer vaccine spectrum
  7) ITU K_pharma_immune axiom check

Outputs:
  - vaccine_immunotherapy_deep.png
  - vaccine_immunotherapy_deep_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("vaccine_immunotherapy_deep.png")
OUT_JSON = Path(__file__).with_name("vaccine_immunotherapy_deep_summary.json")

rng = np.random.default_rng(20260713)

# -------------------------------------------------------------
# 1) Vaccine generations
# -------------------------------------------------------------
vaccine_gens = {
    "1G Live attenuated (1796)": {"efficacy_pct": 95, "dev_months": 60, "year": 1796},
    "2G Inactivated":            {"efficacy_pct": 60, "dev_months": 18, "year": 1950},
    "3G Subunit":                {"efficacy_pct": 90, "dev_months": 12, "year": 1986},
    "4G Vector (Adeno)":         {"efficacy_pct": 70, "dev_months": 6,  "year": 2010},
    "5G mRNA ★":                  {"efficacy_pct": 95, "dev_months": 0.5,"year": 2020},
    "6G saRNA":                  {"efficacy_pct": 90, "dev_months": 0.3,"year": 2025},
}

# -------------------------------------------------------------
# 2) COVID vaccine doses (2020-2024)
# -------------------------------------------------------------
years_covid = np.array([2020, 2021, 2022, 2023, 2024])
doses_B = np.array([0.3, 9.0, 11.5, 12.8, 13.0])
lives_saved_M = np.array([1.0, 11.0, 16.5, 18.0, 19.0])

# -------------------------------------------------------------
# 3) Melanoma 5y survival evolution
# -------------------------------------------------------------
periods = ["1990s\nchemo", "2011\nipilimumab", "2014-15\nnivolumab",
           "2015-16\nipi+nivo", "2022\ntriplet"]
survival_5y = [5, 18, 34, 52, 60]

# -------------------------------------------------------------
# 4) CAR-T products + CR rates
# -------------------------------------------------------------
cart_products = {
    "Kymriah (CD19, pALL) 2017":    {"CR_pct": 83, "year": 2017},
    "Yescarta (CD19, DLBCL) 2017":  {"CR_pct": 51, "year": 2017},
    "Brexucabtagene (CD19, MCL) 2020":{"CR_pct": 65, "year": 2020},
    "Liso-cel (CD19, DLBCL) 2021":  {"CR_pct": 53, "year": 2021},
    "Abecma (BCMA, MM) 2021":       {"CR_pct": 33, "year": 2021},
    "Carvykti (BCMA, MM) 2022":     {"CR_pct": 67, "year": 2022},
    "Lifileucel TIL (melanoma) 2024": {"CR_pct": 31, "year": 2024},
}

# -------------------------------------------------------------
# 5) mRNA cancer vaccine pipeline
# -------------------------------------------------------------
cancer_vaccine_pipeline = {
    "Provenge (Sipuleucel)":  {"approved": True, "year": 2010, "cancer": "Prostate (1st gen)"},
    "T-VEC (Imlygic)":         {"approved": True, "year": 2015, "cancer": "Melanoma (oncolytic)"},
    "mRNA-4157 (Moderna)":     {"approved": False, "year": 2025, "cancer": "Melanoma (Phase III)"},
    "BNT122 (BioNTech)":       {"approved": False, "year": 2025, "cancer": "Melanoma + colorectal"},
    "INO-4800 (Inovio)":       {"approved": False, "year": 2026, "cancer": "Various (DNA)"},
}

# -------------------------------------------------------------
# 6) Karikó-Weissman timeline
# -------------------------------------------------------------
kariko_timeline = {
    "Karikó moves UPenn":  1985,
    "Karikó UPenn assistant prof": 1989,
    "Demoted at UPenn":    1995,
    "Meets Weissman":      1997,
    "Pseudouridine paper": 2005,
    "BioNTech co-founded": 2008,
    "BNT162b2 FDA approval": 2020,
    "Nobel Physiology/Medicine": 2023,
}

# -------------------------------------------------------------
# 7) ITU K_pharma_immune axiom
# -------------------------------------------------------------
N_states = 2500
# Naive immune (broad uniform-like)
log_fit_naive = 0.1 * rng.standard_normal(N_states)
p_naive = np.exp(log_fit_naive); p_naive /= p_naive.sum()
S_naive = float(-np.sum(p_naive * np.log(p_naive)))

# Post-vaccine memory: peaked at antigen-specific
log_fit_vaccine = log_fit_naive.copy()
log_fit_vaccine[1000:1100] += 3.5  # B/T cell memory clone
p_vaccine = np.exp(log_fit_vaccine); p_vaccine /= p_vaccine.sum()
S_vaccine = float(-np.sum(p_vaccine * np.log(p_vaccine)))

# Post-checkpoint inhibitor: T cell exhausted -> rescued
log_fit_io = log_fit_naive.copy()
log_fit_io[1800:2200] += 2.0  # rescued T cells active
p_io = np.exp(log_fit_io); p_io /= p_io.sum()
S_io = float(-np.sum(p_io * np.log(p_io)))

# Post-CAR-T: 1000 fold expansion of CAR+ T cells
log_fit_cart = log_fit_naive.copy()
log_fit_cart[200:300] += 5.0  # CAR-T massive expansion
p_cart = np.exp(log_fit_cart); p_cart /= p_cart.sum()
S_cart = float(-np.sum(p_cart * np.log(p_cart)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_naive_vacc = itu_lin(p_naive, p_vaccine)
ratio_naive_io = itu_lin(p_naive, p_io)
ratio_naive_cart = itu_lin(p_naive, p_cart)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 232 — Vaccines + Immunotherapy Deep (K_pharma_immune)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Vaccine generations
ax = axes[0, 0]
gen_names = list(vaccine_gens.keys())
months = [vaccine_gens[g]["dev_months"] for g in gen_names]
effs = [vaccine_gens[g]["efficacy_pct"] for g in gen_names]
x = np.arange(len(gen_names))
width = 0.35
ax.bar(x - width/2, months, width, color="#1f77b4", label="Dev time (months)")
ax2 = ax.twinx()
ax2.bar(x + width/2, effs, width, color="#2ca02c", label="Efficacy %")
ax.set_xticks(x); ax.set_xticklabels(gen_names, rotation=20, fontsize=6)
ax.set_yscale("log")
ax.set_ylabel("Dev time (months, log)", color="#1f77b4")
ax2.set_ylabel("Efficacy %", color="#2ca02c")
ax.set_title("Vaccine 6 generations: 60 mo → 2 weeks")
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 2: COVID vaccine doses + lives saved
ax = axes[0, 1]
ax.bar(years_covid, doses_B, color="#9467bd", alpha=0.7, label="Doses (B)")
ax2 = ax.twinx()
ax2.plot(years_covid, lives_saved_M, "o-", color="#d62728", lw=2,
         markersize=10, label="Lives saved (M)")
ax.set_xlabel("Year")
ax.set_ylabel("Cumulative doses (Billion)", color="#9467bd")
ax2.set_ylabel("Lives saved (Million)", color="#d62728")
ax.set_title(f"COVID vaccines (13B doses; ~19M lives saved)")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="lower right", fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Melanoma 5y survival
ax = axes[0, 2]
colors_m = ["#d62728", "#ff7f0e", "#ffbb78", "#98df8a", "#2ca02c"]
ax.bar(periods, survival_5y, color=colors_m)
ax.set_ylabel("5y survival (%)")
ax.set_title("Melanoma: 5% → 60% (Allison-Honjo Nobel 2018)")
ax.tick_params(axis="x", rotation=10, labelsize=8)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(survival_5y):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=10, fontweight="bold")

# Panel 4: CAR-T + TIL CR
ax = axes[1, 0]
cart_names = list(cart_products.keys())
crs = [cart_products[k]["CR_pct"] for k in cart_names]
colors_c = ["#2ca02c" if c > 60 else "#ff7f0e" if c > 40 else "#d62728" for c in crs]
ax.barh(range(len(cart_names)), crs, color=colors_c)
ax.set_yticks(range(len(cart_names))); ax.set_yticklabels(cart_names, fontsize=6)
ax.set_xlabel("CR rate (%)")
ax.set_title("CAR-T + TIL (2017-2024)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 5: Karikó-Weissman timeline
ax = axes[1, 1]
k_events = list(kariko_timeline.keys())
k_years = list(kariko_timeline.values())
ax.barh(range(len(k_events)), k_years, color="#9467bd")
ax.set_yticks(range(len(k_events))); ax.set_yticklabels(k_events, fontsize=7)
ax.set_xlim(1984, 2025)
ax.set_xlabel("Year")
ax.set_title("Karikó-Weissman 38-year journey (Nobel 2023)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ITU K_pharma_immune
ax = axes[1, 2]
ax.bar(["Naive", "Post-vaccine\n(memory)", "Post-checkpoint\n(rescued)", "Post-CAR-T\n(expansion)"],
       [S_naive, S_vaccine, S_io, S_cart],
       color=["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728"])
ax.set_ylabel("Immune state entropy (nats)")
ax.set_title(f"K_pharma_immune: V={ratio_naive_vacc:.3f}, IO={ratio_naive_io:.3f}, CAR-T={ratio_naive_cart:.3f}")
ax.tick_params(axis="x", labelsize=7)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 232,
    "tier1_paper": 32,
    "topic": "Vaccines + Immunotherapy deep (K_pharma_immune)",
    "vaccine_generations": vaccine_gens,
    "COVID_vaccine_2020_2024": {
        "doses_B_per_year": dict(zip(years_covid.tolist(), doses_B.tolist())),
        "lives_saved_M_per_year": dict(zip(years_covid.tolist(), lives_saved_M.tolist())),
        "total_doses_B": 13.0,
        "Watson_2022_Lancet_lives_saved_M_range": "14.4-19.8",
    },
    "Kariko_Weissman_journey": kariko_timeline,
    "Kariko_Weissman_Nobel_2023": "Physiology/Medicine - pseudouridine mRNA",
    "Allison_Honjo_Nobel_2018": "Physiology/Medicine - checkpoint inhibitors",
    "melanoma_5y_survival_evolution": dict(zip(periods, survival_5y)),
    "CART_TIL_products": cart_products,
    "Lifileucel_2024_first_TIL": "FDA approval Feb 2024",
    "cancer_vaccine_pipeline": cancer_vaccine_pipeline,
    "ITU_K_pharma_immune": {
        "N_states": int(N_states),
        "S_naive_nats": S_naive,
        "S_vaccine_nats": S_vaccine,
        "S_checkpoint_nats": S_io,
        "S_CART_nats": S_cart,
        "naive_to_vaccine_ratio": ratio_naive_vacc,
        "naive_to_checkpoint_ratio": ratio_naive_io,
        "naive_to_CART_ratio": ratio_naive_cart,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_pharma_immune",
        "modular_Hamiltonian": "K_pharma_immune^(0) = -log P(immune state | therapy × patient)",
        "vaccine_meaning": "ITU K-state descent: naive → memory (Phase 188 prime-boost)",
        "checkpoint_meaning": "K-state rescue: exhausted T cells reactivated",
        "CART_meaning": "Massive K-state expansion (CAR+ T cell 1000-fold)",
        "lives_saved": "COVID mRNA saved ~19M lives (Watson 2022 Lancet)",
    },
    "predictions": [
        ("Universal flu vaccine FDA", 2030, 0.55, "Medium"),
        ("HIV mRNA vaccine >70% efficacy", 2032, 0.40, "Weak"),
        ("Cancer neoantigen mRNA standard", 2028, 0.80, "Strong"),
        ("CAR-T solid tumor first FDA", 2028, 0.70, "Strong"),
        ("Universal cancer vaccine", 2032, 0.45, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
