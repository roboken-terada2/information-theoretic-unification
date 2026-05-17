"""
Phase 224 — Optogenetics + Fluorescence + Super-Resolution (K_photon_bio)

Simulations:
  1) Fluorescent protein palette (BFP/CFP/GFP/YFP/mCherry/iRFP)
  2) Abbe diffraction limit vs super-resolution techniques
  3) Optogenetics tools (ChR2/NpHR/Arch)
  4) ChR2 action spectrum + neural firing
  5) Nobel Prizes 2008/2014/2017 timeline
  6) Cryo-EM + AlphaFold combination
  7) ITU K_photon_bio axiom check

Outputs:
  - optogenetics_microscopy.png
  - optogenetics_microscopy_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("optogenetics_microscopy.png")
OUT_JSON = Path(__file__).with_name("optogenetics_microscopy_summary.json")

rng = np.random.default_rng(20260705)

# -------------------------------------------------------------
# 1) Fluorescent proteins (excitation/emission)
# -------------------------------------------------------------
fluorescent_proteins = {
    "BFP":     {"ex": 380, "em": 440, "color": "#0033ff"},
    "CFP":     {"ex": 433, "em": 475, "color": "#00cccc"},
    "GFP":     {"ex": 488, "em": 509, "color": "#00ff00"},
    "YFP":     {"ex": 514, "em": 527, "color": "#ffff00"},
    "mCherry": {"ex": 587, "em": 610, "color": "#ff0000"},
    "mScarlet":{"ex": 569, "em": 594, "color": "#ff3300"},
    "iRFP670": {"ex": 643, "em": 670, "color": "#990033"},
}

# -------------------------------------------------------------
# 2) Abbe limit vs super-resolution
# -------------------------------------------------------------
techniques = {
    "Abbe limit (1873)":   {"resolution_nm": 200, "year": 1873},
    "Confocal":            {"resolution_nm": 150, "year": 1957},
    "STED (Hell 2000)":    {"resolution_nm": 50,  "year": 2000},
    "PALM (Betzig 2006)":  {"resolution_nm": 20,  "year": 2006},
    "STORM (Zhuang 2006)": {"resolution_nm": 20,  "year": 2006},
    "MINFLUX (Hell 2017)": {"resolution_nm": 2,   "year": 2017},
    "Cryo-EM atomic":      {"resolution_nm": 0.3, "year": 2013},
}

# -------------------------------------------------------------
# 3) Optogenetics tools
# -------------------------------------------------------------
opto_tools = {
    "ChR2 (excitation)":   {"wavelength_nm": 470, "effect": "Na+ influx",  "kinetics_ms": 1},
    "NpHR (inhibition)":   {"wavelength_nm": 580, "effect": "Cl- pump",    "kinetics_ms": 5},
    "Arch (inhibition)":   {"wavelength_nm": 575, "effect": "H+ pump",     "kinetics_ms": 8},
    "Chrimson (red)":      {"wavelength_nm": 590, "effect": "Na+ red-shifted", "kinetics_ms": 8},
    "ChR2-XXM":            {"wavelength_nm": 470, "effect": "fast variant", "kinetics_ms": 0.2},
    "bPAC (cAMP)":         {"wavelength_nm": 460, "effect": "cAMP up",     "kinetics_ms": 100},
}

# -------------------------------------------------------------
# 4) ChR2 action spectrum + neural firing simulation
# -------------------------------------------------------------
wavelengths = np.linspace(400, 600, 200)
chr2_response = np.exp(-((wavelengths - 470) / 30) ** 2)
nphr_response = np.exp(-((wavelengths - 580) / 25) ** 2)

# Simulated firing: 470 nm light pulse → spikes
t_ms = np.linspace(0, 200, 1000)
light_on = (t_ms > 50) & (t_ms < 150)
# Spike train when light on
spike_rate = 40  # Hz during light
n_spikes_expected = spike_rate * (150 - 50) / 1000
spike_times = []
t = 50
while t < 150:
    t += rng.exponential(1000 / spike_rate)
    if t < 150:
        spike_times.append(t)

# -------------------------------------------------------------
# 5) Nobel Prizes timeline
# -------------------------------------------------------------
nobel_optical = {
    "Photoelectric (Einstein)":      1921,
    "GFP (Shimomura-Chalfie-Tsien)": 2008,
    "Super-resolution (Betzig-Hell-Moerner)": 2014,
    "Cryo-EM (Henderson-Frank-Dubochet)":    2017,
    "Bell tests (Aspect-Clauser-Zeilinger)": 2022,
    "AlphaFold (Baker-Hassabis-Jumper)":     2024,
}

# -------------------------------------------------------------
# 6) ITU K_photon_bio axiom: optogenetic control
# -------------------------------------------------------------
N_neurons = 2000
# Pre-light: random activity
log_fit_pre = 0.1 * rng.standard_normal(N_neurons)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Light on: ChR2-expressing population (10%) activated
chr2_expressed = rng.random(N_neurons) < 0.1
log_fit_light = log_fit_pre.copy()
log_fit_light[chr2_expressed] += 4.0
p_light = np.exp(log_fit_light); p_light /= p_light.sum()
S_light = float(-np.sum(p_light * np.log(p_light)))

# Inhibition (NpHR + 580 nm): suppression
log_fit_inhib = log_fit_pre.copy()
nphr_expressed = rng.random(N_neurons) < 0.15
log_fit_inhib[nphr_expressed] -= 3.0
p_inhib = np.exp(log_fit_inhib); p_inhib /= p_inhib.sum()
S_inhib = float(-np.sum(p_inhib * np.log(p_inhib)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pre_light = itu_lin(p_pre, p_light)
ratio_pre_inhib = itu_lin(p_pre, p_inhib)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 224 — Optogenetics + Fluorescence + Super-Resolution (K_photon_bio)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Fluorescent protein palette
ax = axes[0, 0]
for name, p in fluorescent_proteins.items():
    ax.plot([p["ex"], p["em"]], [0, 1], "-", color=p["color"], lw=2, alpha=0.6)
    ax.scatter([p["ex"]], [0], s=100, color=p["color"], marker="o", edgecolor="black")
    ax.scatter([p["em"]], [1], s=100, color=p["color"], marker="^", edgecolor="black")
    ax.text(p["em"] + 5, 1.02, name, fontsize=7)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("0 = excite, 1 = emit")
ax.set_title("Fluorescent protein palette (Shimomura-Chalfie-Tsien Nobel 2008)")
ax.set_xlim(350, 700)
ax.grid(True, alpha=0.3)

# Panel 2: Resolution comparison
ax = axes[0, 1]
tech_names = list(techniques.keys())
res = [techniques[t]["resolution_nm"] for t in tech_names]
colors_r = ["#2ca02c" if r < 10 else "#ff7f0e" if r < 100 else "#d62728" for r in res]
ax.barh(range(len(tech_names)), res, color=colors_r)
ax.set_xscale("log")
ax.set_yticks(range(len(tech_names))); ax.set_yticklabels(tech_names, fontsize=8)
ax.set_xlabel("Resolution (nm, log)")
ax.set_title("Super-resolution: Abbe → MINFLUX (Nobel 2014/2017)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 3: Optogenetics action spectrum
ax = axes[0, 2]
ax.plot(wavelengths, chr2_response, "-", color="#1f77b4", lw=2,
        label="ChR2 (excitation 470 nm)")
ax.plot(wavelengths, nphr_response, "-", color="#ff7f0e", lw=2,
        label="NpHR (inhibition 580 nm)")
ax.axvline(470, color="blue", linestyle="--", alpha=0.5)
ax.axvline(580, color="orange", linestyle="--", alpha=0.5)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Response")
ax.set_title("Optogenetics tools (Boyden-Deisseroth 2005)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Light-driven neural firing
ax = axes[1, 0]
ax.fill_between(t_ms[light_on], 0, 1, alpha=0.2, color="#1f77b4", label="470 nm light")
for sp in spike_times:
    ax.axvline(sp, color="#d62728", lw=1.5)
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Neural firing")
ax.set_title(f"ChR2 light pulse → {len(spike_times)} spikes (~40 Hz)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Nobel Prizes timeline
ax = axes[1, 1]
prize_names = list(nobel_optical.keys())
prize_years = list(nobel_optical.values())
ax.scatter(prize_years, range(len(prize_names)), s=200, color="#d62728", zorder=5)
for i, name in enumerate(prize_names):
    ax.text(prize_years[i] + 1, i, name, fontsize=7, va="center")
ax.set_yticks(range(len(prize_names)))
ax.set_yticklabels([str(y) for y in prize_years], fontsize=8)
ax.set_xlim(1915, 2030)
ax.set_xlabel("Year")
ax.set_title("Optical-related Nobel Prizes")
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ITU optogenetic control
ax = axes[1, 2]
ax.bar(["Pre-light\n(random)", "ChR2 + 470 nm\n(excite 10%)", "NpHR + 580 nm\n(inhibit 15%)"],
       [S_pre, S_light, S_inhib], color=["#1f77b4", "#2ca02c", "#ff7f0e"])
ax.set_ylabel("Neural activity entropy (nats)")
ax.set_title(f"K_photon_bio: Pre→Light={ratio_pre_light:.3f}, Pre→Inhib={ratio_pre_inhib:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 224,
    "tier1_paper": 31,
    "topic": "Optogenetics + Fluorescence + Super-Resolution (K_photon_bio)",
    "fluorescent_proteins": fluorescent_proteins,
    "Shimomura_Chalfie_Tsien_Nobel_2008": "GFP discovery + multicolor + in vivo",
    "GFP_quantum_yield": 0.79,
    "super_resolution_techniques": techniques,
    "Abbe_limit_1873_nm": 200,
    "MINFLUX_resolution_nm": 2,
    "Betzig_Hell_Moerner_Nobel_2014": "Super-resolution fluorescence microscopy",
    "Cryo_EM_Nobel_2017": "Henderson + Frank + Dubochet (atomic resolution)",
    "optogenetics_tools": opto_tools,
    "Boyden_Deisseroth_2005": "Optogenetics founding paper (ChR2 + neurons)",
    "GenSight_RPE65_2021": "First optogenetic therapy in humans (partial vision recovery)",
    "ITU_K_photon_bio": {
        "N_neurons_simulated": N_neurons,
        "S_pre_light_nats": S_pre,
        "S_ChR2_light_nats": S_light,
        "S_NpHR_inhibition_nats": S_inhib,
        "pre_to_light_ratio": ratio_pre_light,
        "pre_to_inhib_ratio": ratio_pre_inhib,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon_bio",
        "modular_Hamiltonian": "K_photon_bio^(0) = -log P(biomolecule state | photon)",
        "optogenetics_meaning": "Light = direct K_neuro^(0) operator (control)",
        "GFP_meaning": "K_photon as readout of K_genome state",
        "MINFLUX_meaning": "Subcellular K-state imaging at 2 nm",
        "Cryo_EM_AlphaFold_synergy": "K_photon (e-beam) + K_genome_AI = structure determination",
    },
    "Nobel_count_optical": 6,
    "Nobel_optical_decades": list(nobel_optical.values()),
    "predictions": [
        ("Optogenetic neural prosthesis FDA", 2030, 0.65, "Medium"),
        ("All-optical brain imaging (mouse)", 2030, 0.70, "Strong"),
        ("Multi-photon all-optical interrogation", 2028, 0.75, "Strong"),
        ("MINFLUX subcellular real-time", 2028, 0.80, "Strong"),
        ("Adaptive optics in vivo human retina", 2030, 0.70, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
