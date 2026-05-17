"""
Phase 221 — Laser + Coherence + BEC (K_photon_coherence)

Simulations:
  1) Photon statistics: thermal vs coherent vs Fock
  2) g²(0) correlation function discrimination
  3) Laser history timeline (1954-2024)
  4) BEC critical temperature for various atoms
  5) Photon BEC (Klaers-Weitz 2010)
  6) Glauber coherent state |alpha⟩ distribution
  7) ITU K_photon_coherence axiom check

Outputs:
  - laser_coherence_bec.png
  - laser_coherence_bec_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson, geom

OUT_PNG = Path(__file__).with_name("laser_coherence_bec.png")
OUT_JSON = Path(__file__).with_name("laser_coherence_bec_summary.json")

rng = np.random.default_rng(20260702)

# -------------------------------------------------------------
# 1) Photon statistics: 3 distributions
# -------------------------------------------------------------
mean_n = 10
n_max = 40
n_arr = np.arange(n_max)

# Thermal (Bose-Einstein): geometric-like
p_thermal_n = (mean_n / (1 + mean_n)) ** n_arr / (1 + mean_n)
# Coherent: Poisson
p_coherent_n = poisson.pmf(n_arr, mean_n)
# Fock state |10⟩: delta
p_fock_n = np.zeros(n_max)
p_fock_n[10] = 1.0

# g²(0) values
g2_thermal = 2.0
g2_coherent = 1.0
g2_fock_n = 1 - 1/mean_n if mean_n > 1 else 0  # for |n⟩: 1-1/n
g2_single = 0.0

# Standard deviation comparison
std_thermal = np.sqrt(mean_n * (1 + mean_n))
std_coherent = np.sqrt(mean_n)
std_fock = 0.0

# -------------------------------------------------------------
# 2) Laser history timeline
# -------------------------------------------------------------
laser_history = {
    "Maser (Townes 1954)":       {"year": 1954, "wavelength_nm": 12_700_000},  # NH3 maser
    "Ruby laser (Maiman 1960)":  {"year": 1960, "wavelength_nm": 694},
    "He-Ne laser (1960)":        {"year": 1960, "wavelength_nm": 632.8},
    "Semiconductor 1962":        {"year": 1962, "wavelength_nm": 850},
    "Continuous DH 1970":        {"year": 1970, "wavelength_nm": 850},
    "Blue InGaN (Nakamura 1996)":{"year": 1996, "wavelength_nm": 450},
    "Fiber laser":               {"year": 1985, "wavelength_nm": 1064},
    "Petawatt CPA":              {"year": 2018, "wavelength_nm": 800},
}

# -------------------------------------------------------------
# 3) BEC critical temperatures
# -------------------------------------------------------------
bec_atoms = {
    "H (atomic)":     {"T_c_nK": 50,    "year": 1998, "lab": "MIT"},
    "Li-7":           {"T_c_nK": 100,   "year": 1995, "lab": "Rice"},
    "Na-23":          {"T_c_nK": 200,   "year": 1995, "lab": "MIT (Ketterle) ★"},
    "Rb-87":          {"T_c_nK": 170,   "year": 1995, "lab": "JILA (Wieman-Cornell) ★"},
    "K-40":           {"T_c_nK": 100,   "year": 2001, "lab": "JILA fermi"},
    "Sr-88":          {"T_c_nK": 1000,  "year": 2009, "lab": "Innsbruck"},
    "Photon (Klaers-Weitz 2010)": {"T_c_nK": 3e11, "year": 2010, "lab": "Bonn"},
}

# -------------------------------------------------------------
# 4) Coherent state |alpha⟩ for various alpha
# -------------------------------------------------------------
alphas = [1, 2, 3, 5, 10]
alpha_distributions = {}
n_grid = np.arange(20)
for a in alphas:
    # |⟨n|α⟩|² = e^(-|α|²) |α|^(2n) / n!
    pn = poisson.pmf(n_grid, a ** 2)
    alpha_distributions[a] = pn

# -------------------------------------------------------------
# 5) ITU K_photon_coherence axiom
# -------------------------------------------------------------
# Use full distribution (extend Fock to broad for valid log)
N_states = 200
p_thermal_full = np.zeros(N_states)
p_thermal_full[:n_max] = p_thermal_n
p_thermal_full = p_thermal_full / p_thermal_full.sum()
S_thermal = float(-np.sum(np.where(p_thermal_full > 1e-30, p_thermal_full * np.log(p_thermal_full), 0)))

p_coherent_full = np.zeros(N_states)
p_coherent_full[:n_max] = p_coherent_n
p_coherent_full = p_coherent_full / p_coherent_full.sum()
S_coherent = float(-np.sum(np.where(p_coherent_full > 1e-30, p_coherent_full * np.log(p_coherent_full), 0)))

# Fock |10⟩: spread slightly for log-defined entropy
p_fock_full = np.zeros(N_states) + 1e-10
p_fock_full[10] = 1.0
p_fock_full = p_fock_full / p_fock_full.sum()
S_fock = float(-np.sum(p_fock_full * np.log(p_fock_full)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_thermal_coherent = itu_lin(p_thermal_full, p_coherent_full)
ratio_coherent_fock = itu_lin(p_coherent_full, p_fock_full)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 221 — Laser + Coherence + BEC (K_photon_coherence)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Photon statistics
ax = axes[0, 0]
ax.plot(n_arr, p_thermal_n, "o-", color="#d62728", lw=2, label=f"Thermal g²=2")
ax.plot(n_arr, p_coherent_n, "s-", color="#1f77b4", lw=2, label=f"Coherent g²=1")
ax.bar([10], [1.0], width=0.5, color="#2ca02c", alpha=0.5, label=f"Fock |10⟩ g²={g2_fock_n:.2f}")
ax.set_xlabel("Photon number n")
ax.set_ylabel("P(n)")
ax.set_title(f"Photon statistics (⟨n⟩={mean_n})")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: g²(0) comparison
ax = axes[0, 1]
g2_states = ["Single photon\n|1⟩", "Sub-Poisson\nantibunching", "Coherent\n(laser)", "Thermal\n(chaotic)"]
g2_vals = [0.0, 0.5, 1.0, 2.0]
colors_g = ["#2ca02c", "#1f77b4", "#ff7f0e", "#d62728"]
ax.bar(g2_states, g2_vals, color=colors_g)
ax.axhline(1.0, color="black", linestyle="--", alpha=0.5)
ax.set_ylabel("g²(0)")
ax.set_title("g²(0) discriminates quantum states")
ax.tick_params(axis="x", rotation=10, labelsize=9)
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(g2_vals):
    ax.text(i, v + 0.05, f"{v:.1f}", ha="center", fontsize=10, fontweight="bold")

# Panel 3: Laser history
ax = axes[0, 2]
names = list(laser_history.keys())
years = [laser_history[k]["year"] for k in names]
wls = [laser_history[k]["wavelength_nm"] for k in names]
colors_l = ["#d62728" if "Nakamura" in n or "Maiman" in n or "Mourou" in n else "#1f77b4" for n in names]
ax.scatter(years, wls, c=colors_l, s=80)
for i, n in enumerate(names):
    ax.annotate(n.split("(")[0], (years[i], wls[i]), fontsize=6,
                xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("Wavelength (nm, log)")
ax.set_yscale("log")
ax.set_title("Laser history (1954-2018)")
ax.grid(True, alpha=0.3, which="both")

# Panel 4: BEC atoms
ax = axes[1, 0]
atoms = list(bec_atoms.keys())
tcs = [bec_atoms[a]["T_c_nK"] for a in atoms]
colors_b = ["#d62728" if "★" in bec_atoms[a]["lab"] else
            "#9467bd" if "Photon" in a else "#1f77b4" for a in atoms]
ax.barh(range(len(atoms)), tcs, color=colors_b)
ax.set_xscale("log")
ax.set_yticks(range(len(atoms))); ax.set_yticklabels(atoms, fontsize=7)
ax.set_xlabel("T_c (nK, log)")
ax.set_title("BEC critical temperatures (Nobel 2001)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 5: Coherent state |alpha⟩
ax = axes[1, 1]
for a, pn in alpha_distributions.items():
    ax.plot(n_grid, pn, "o-", lw=1.5, label=f"|α|={a}  ⟨n⟩={a**2}")
ax.set_xlabel("Photon number n")
ax.set_ylabel("|⟨n|α⟩|²")
ax.set_title("Glauber coherent state |α⟩ (Nobel 2005)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: ITU K_photon_coherence
ax = axes[1, 2]
ax.bar(["Thermal", "Coherent", "Fock |10⟩"], [S_thermal, S_coherent, S_fock],
       color=["#d62728", "#1f77b4", "#2ca02c"])
ax.set_ylabel("Photon state entropy (nats)")
ax.set_title(f"ITU Thermal→Coherent={ratio_thermal_coherent:.3f}, Coh→Fock={ratio_coherent_fock:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 221,
    "tier1_paper": 31,
    "topic": "Laser + Coherence + BEC (K_photon_coherence)",
    "photon_statistics": {
        "thermal_g2": g2_thermal,
        "coherent_g2": g2_coherent,
        "fock_g2_n10": float(g2_fock_n),
        "single_photon_g2": g2_single,
        "thermal_std": float(std_thermal),
        "coherent_std": float(std_coherent),
    },
    "laser_history": laser_history,
    "BEC_atoms": bec_atoms,
    "Wieman_Cornell_Ketterle_Nobel_2001": "Physics",
    "Glauber_Hänsch_Hall_Nobel_2005": "Physics",
    "Nakamura_blue_LED_laser_Nobel_2014": "Physics",
    "Mourou_Strickland_CPA_Nobel_2018": "Physics",
    "Klaers_Weitz_Photon_BEC_2010": "Bonn (Nature)",
    "ITU_K_photon_coherence": {
        "S_thermal_nats": S_thermal,
        "S_coherent_nats": S_coherent,
        "S_fock_10_nats": S_fock,
        "thermal_to_coherent_ratio": ratio_thermal_coherent,
        "coherent_to_fock_ratio": ratio_coherent_fock,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon_coherence",
        "modular_Hamiltonian": "K_photon_coherence^(0) = -log P(photon dist | coherence)",
        "laser_meaning": "ITU descent from thermal to coherent (Poisson) state",
        "BEC_meaning": "Atomic K-state coherence (same ITU descent as laser)",
        "Photon_BEC_2010": "K_photon and K_atom share ITU coherence descent",
        "Glauber_coherent_state": "ITU canonical descent endpoint for bosonic field",
    },
    "predictions": [
        ("Room-temp atomic BEC practical", 2030, 0.55, "Medium"),
        ("Atom interferometer GPS-free", 2028, 0.75, "Strong"),
        ("Petawatt laser fusion application", 2030, 0.65, "Medium"),
        ("Photon BEC computer", 2032, 0.45, "Medium"),
        ("GHZ photon 100+ qubits", 2028, 0.70, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
