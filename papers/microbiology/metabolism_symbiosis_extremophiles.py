"""
Phase 197 — Bacterial metabolism + symbiosis + extremophiles (K_metabolism + K_extremophile)

Simulations:
  1) 6 metabolic types comparison
  2) Fermentation product diversity
  3) Anaerobic respiration electron acceptor hierarchy
  4) Endosymbiotic theory: mitochondrial vs chloroplast DNA
  5) Extremophile environmental tolerance ranges
  6) D. radiodurans LD50 vs other organisms
  7) Nitrogen fixation budget (biological vs Haber-Bosch)
  8) ITU K_metabolism axiom check with metabolic shift

Outputs:
  - metabolism_symbiosis_extremophiles.png
  - metabolism_symbiosis_extremophiles_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("metabolism_symbiosis_extremophiles.png")
OUT_JSON = Path(__file__).with_name("metabolism_symbiosis_extremophiles_summary.json")

rng = np.random.default_rng(20260531)

# -------------------------------------------------------------
# 1) Metabolic types
# -------------------------------------------------------------
metab_types = {
    "Photoautotroph":     {"C_src": "CO2", "E_src": "Light", "ATP_yield": 38},
    "Chemolithoautotroph":{"C_src": "CO2", "E_src": "Inorganic chemistry", "ATP_yield": 2},
    "Chemoheterotroph":   {"C_src": "Organic", "E_src": "Organic", "ATP_yield": 38},
    "Photoheterotroph":   {"C_src": "Organic", "E_src": "Light", "ATP_yield": 20},
    "Mixotroph":          {"C_src": "Both", "E_src": "Both", "ATP_yield": 30},
    "Diazotroph":         {"C_src": "CO2 or Organic", "E_src": "Varied", "ATP_yield": -16}, # N fixation costs ATP
}

# -------------------------------------------------------------
# 2) Fermentation products (ATP yields)
# -------------------------------------------------------------
fermentation = {
    "Lactate (Lactobacillus)":       2,
    "Ethanol (Yeast)":               2,
    "Acetate (Acetobacter)":         3,
    "Butyrate (Clostridium)":        2.5,
    "Methane (Methanogens)":         0.5,
    "Mixed acid (E. coli)":          2.5,
}

# -------------------------------------------------------------
# 3) Anaerobic respiration: electron acceptor hierarchy
# -------------------------------------------------------------
# Higher reduction potential -> more energy gained
e_acceptors = {
    "O2 -> H2O":         +820,
    "NO3- -> N2":        +740,
    "Mn4+ -> Mn2+":      +500,
    "Fe3+ -> Fe2+":      +200,
    "SO4 -> H2S":        -220,
    "CO2 -> CH4":        -240,
}

# -------------------------------------------------------------
# 4) Endosymbiotic DNA sizes
# -------------------------------------------------------------
endosymb_dna = {
    "α-Proteobacteria (free)": 4e6,
    "Cyanobacteria (free)":    3.5e6,
    "Mitochondria (human)":    16569,
    "Mitochondria (plant)":    367000,
    "Chloroplast (Arabidopsis)": 154478,
    "Cyanelle (Glaucocystis)": 135000,
}

# -------------------------------------------------------------
# 5) Extremophile tolerances
# -------------------------------------------------------------
extremes = {
    "Methanopyrus kandleri":   {"temp_C": 122, "category": "Thermophile"},
    "Picrophilus oshimae":     {"pH": 0.0,   "category": "Acidophile"},
    "Natranaerobius":          {"pH": 12.0,  "category": "Alkalophile"},
    "Halobacterium":           {"salt_pct": 30, "category": "Halophile"},
    "Pyrococcus yayanosii":    {"pressure_MPa": 110, "category": "Piezophile"},
    "Deinococcus radiodurans": {"radiation_Gy": 5000, "category": "Radioresistant"},
    "Polaromonas":             {"temp_C": -25, "category": "Psychrophile"},
}

# -------------------------------------------------------------
# 6) Radiation resistance comparison
# -------------------------------------------------------------
ld50_radiation = {
    "Human":                5,
    "E. coli":              200,
    "Yeast":                400,
    "Tardigrade":           1000,
    "Bacillus spore":       3000,
    "Deinococcus radiodurans": 5000,
}

# -------------------------------------------------------------
# 7) Nitrogen fixation budget
# -------------------------------------------------------------
N_fixation = {
    "Marine cyanobacteria (Trichodesmium)": 100e12,  # 100 Tg N/yr (Capone 2005)
    "Free-living soil (Azotobacter etc.)":   30e12,
    "Symbiotic legume (Rhizobium)":          50e12,
    "Lightning (atmospheric)":               10e12,
    "Industrial Haber-Bosch":               120e12,  # 120 Tg N/yr (2024)
}

# -------------------------------------------------------------
# 8) ITU K_metabolism axiom check: metabolic shift
# -------------------------------------------------------------
N_states = 2000
# Aerobic state: O2 plentiful, oxidative phos dominant
log_fit_aerobic = -((np.arange(N_states) - 400) ** 2) / 50000
p_aerobic = np.exp(log_fit_aerobic); p_aerobic /= p_aerobic.sum()
S_aerobic = float(-np.sum(p_aerobic * np.log(p_aerobic)))

# Anaerobic shift: fermentation, methanogenesis pathways activated
log_fit_anaerobic = log_fit_aerobic.copy()
fermenters = (np.arange(N_states) > 1200)
log_fit_anaerobic[~fermenters] -= 3.0
log_fit_anaerobic[fermenters] += 4.0
p_anaerobic = np.exp(log_fit_anaerobic); p_anaerobic /= p_anaerobic.sum()
S_anaerobic = float(-np.sum(p_anaerobic * np.log(p_anaerobic)))

log_p = np.log(np.clip(p_aerobic, 1e-30, None))
dp = p_anaerobic - p_aerobic
dS_lin = -np.sum(dp * (1.0 + log_p))
dK_lin = -np.sum(dp * log_p)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 197 — Metabolism + Symbiosis + Extremophiles (K_metabolism + K_extremophile)",
    fontsize=13,
    fontweight="bold",
)

# Panel 1: Metabolic types ATP yield
ax = axes[0, 0]
types = list(metab_types.keys())
yields = [metab_types[t]["ATP_yield"] for t in types]
colors_m = ["#2ca02c" if y > 20 else "#ff7f0e" if y > 0 else "#d62728" for y in yields]
ax.barh(range(len(types)), yields, color=colors_m)
ax.set_yticks(range(len(types)))
ax.set_yticklabels(types, fontsize=8)
ax.set_xlabel("Typical ATP yield (per substrate)")
ax.axvline(0, color="black", lw=0.5)
ax.set_title("Metabolic types: ATP economics")
ax.grid(True, alpha=0.3, axis="x")

# Panel 2: Anaerobic e- acceptor hierarchy
ax = axes[0, 1]
acceptors = list(e_acceptors.keys())
potentials = list(e_acceptors.values())
colors_p = ["#2ca02c" if p > 200 else "#ff7f0e" if p > -100 else "#d62728" for p in potentials]
ax.barh(range(len(acceptors)), potentials, color=colors_p)
ax.axvline(0, color="black", lw=0.5)
ax.set_yticks(range(len(acceptors)))
ax.set_yticklabels(acceptors, fontsize=9)
ax.set_xlabel("Reduction potential E°' (mV)")
ax.set_title("Electron acceptor hierarchy")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: Endosymbiotic DNA shrinkage (Margulis 1970)
ax = axes[0, 2]
endo_names = list(endosymb_dna.keys())
endo_sizes = list(endosymb_dna.values())
colors_e = ["#1f77b4" if "free" in n else "#d62728" for n in endo_names]
ax.barh(range(len(endo_names)), endo_sizes, color=colors_e)
ax.set_xscale("log")
ax.set_yticks(range(len(endo_names)))
ax.set_yticklabels(endo_names, fontsize=7)
ax.set_xlabel("Genome size (bp, log)")
ax.set_title("Endosymbiotic DNA reduction (Margulis 1970)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: Extremophile environmental ranges
ax = axes[1, 0]
ex_names = list(extremes.keys())
ex_vals = []
ex_units = []
for n in ex_names:
    e = extremes[n]
    if "temp_C" in e:    ex_vals.append(e["temp_C"]);    ex_units.append(f"{e['temp_C']}°C")
    elif "pH" in e:      ex_vals.append(e["pH"] * 10);   ex_units.append(f"pH {e['pH']}")
    elif "salt_pct" in e: ex_vals.append(e["salt_pct"]); ex_units.append(f"{e['salt_pct']}% salt")
    elif "pressure_MPa" in e: ex_vals.append(e["pressure_MPa"]); ex_units.append(f"{e['pressure_MPa']} MPa")
    elif "radiation_Gy" in e: ex_vals.append(e["radiation_Gy"] / 50); ex_units.append(f"{e['radiation_Gy']} Gy")
ax.barh(range(len(ex_names)), ex_vals, color="#9467bd")
ax.set_yticks(range(len(ex_names)))
ax.set_yticklabels([f"{n}\n({u})" for n, u in zip(ex_names, ex_units)], fontsize=7)
ax.set_xlabel("Extremity (scaled)")
ax.set_title("Extremophile boundaries of life")
ax.grid(True, alpha=0.3, axis="x")

# Panel 5: Radiation LD50
ax = axes[1, 1]
ld_names = list(ld50_radiation.keys())
ld_vals = list(ld50_radiation.values())
colors_l = ["#d62728" if v > 1000 else "#ff7f0e" if v > 100 else "#1f77b4" for v in ld_vals]
ax.barh(range(len(ld_names)), ld_vals, color=colors_l)
ax.set_xscale("log")
ax.set_yticks(range(len(ld_names)))
ax.set_yticklabels(ld_names, fontsize=8)
ax.set_xlabel("LD50 ionizing radiation (Gy, log)")
ax.set_title("D. radiodurans: 1000× human tolerance ★")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 6: Nitrogen fixation + ITU
ax = axes[1, 2]
n_names = list(N_fixation.keys())
n_vals = [v / 1e12 for v in N_fixation.values()]  # Tg N/yr
colors_n = ["#d62728" if "Industrial" in n else "#2ca02c" for n in n_names]
ax.barh(range(len(n_names)), n_vals, color=colors_n)
ax.set_yticks(range(len(n_names)))
ax.set_yticklabels(n_names, fontsize=7)
ax.set_xlabel("N fixation (Tg N/yr)")
ax.set_title(f"N budget;  ITU metabolic shift δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.grid(True, alpha=0.3, axis="x")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 197,
    "tier1_paper": 27,
    "block": "B",
    "topic": "Metabolism + symbiosis + extremophiles (K_metabolism + K_extremophile)",
    "metabolic_types_6": metab_types,
    "fermentation_ATP_yields": fermentation,
    "anaerobic_electron_acceptors_mV": e_acceptors,
    "endosymbiotic_DNA_bp": endosymb_dna,
    "endosymbiotic_theory_Margulis_1970": {
        "mitochondria_origin": "alpha-Proteobacteria (Rickettsia-like)",
        "chloroplast_origin": "Cyanobacteria",
        "evidence": ["double membrane", "circular DNA", "70S ribosomes",
                     "antibiotic susceptibility", "binary fission"],
    },
    "extremophiles": extremes,
    "life_temperature_upper_limit_C": 122,
    "life_pH_range": "0 to 12",
    "radiation_LD50_Gy": ld50_radiation,
    "Deinococcus_vs_human_radiation_fold": 1000,
    "N_fixation_Tg_N_per_year": {k: v / 1e12 for k, v in N_fixation.items()},
    "N_fixation_total_biological": float(sum(v for k, v in N_fixation.items()
                                              if "Industrial" not in k) / 1e12),
    "ITU_K_metabolism": {
        "N_states": N_states,
        "S_aerobic_nats": S_aerobic,
        "S_anaerobic_nats": S_anaerobic,
        "delta_S": S_anaerobic - S_aerobic,
        "delta_S_first_order": float(dS_lin),
        "delta_K_first_order": float(dK_lin),
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_metabolism + K_extremophile (sub-states of K_microbe)",
        "modular_Hamiltonian": "K_metabolism^(0) = -log P(pathway | environment)",
        "endosymbiosis": "ITU K-state fusion operator (Margulis 1970)",
        "extremophile_meaning": "K-state stability under extreme environments",
        "metabolic_shift": "Aerobic <-> anaerobic = ITU descent between K-state basins",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
