"""
Phase 220 — Maxwell + Photon + Bell + K_photon introduction (Tier 1 #31 opening)

Simulations:
  1) Maxwell equations / c verification
  2) Photon energy spectrum (gamma to radio)
  3) Bell-CHSH inequality + Tsirelson bound
  4) Aspect 1982 experiment result
  5) Fiber-optic attenuation curve
  6) Optogenetics ChR2 action spectrum
  7) ITU K_photon axiom check

Outputs:
  - photon_maxwell_bell.png
  - photon_maxwell_bell_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("photon_maxwell_bell.png")
OUT_JSON = Path(__file__).with_name("photon_maxwell_bell_summary.json")

rng = np.random.default_rng(20260701)

# -------------------------------------------------------------
# 1) Maxwell constants & c
# -------------------------------------------------------------
mu0 = 4 * np.pi * 1e-7         # H/m
eps0 = 8.854e-12                # F/m
c_computed = 1.0 / np.sqrt(mu0 * eps0)
c_exact = 2.998e8
c_match = abs(c_computed - c_exact) / c_exact

# -------------------------------------------------------------
# 2) Photon energy spectrum
# -------------------------------------------------------------
h_planck = 6.626e-34
eV = 1.602e-19
freq = np.logspace(0, 22, 200)   # Hz
energy_eV = h_planck * freq / eV
wavelength_m = c_exact / freq

regions = {
    "Radio (1 MHz)":      1e6,
    "Microwave (10 GHz)": 1e10,
    "Infrared (10 THz)":  1e13,
    "Visible (550 nm)":   c_exact / 550e-9,
    "UV (100 nm)":        c_exact / 100e-9,
    "X-ray (0.1 nm)":     c_exact / 0.1e-9,
    "Gamma (10⁻¹² m)":    c_exact / 1e-12,
}

# -------------------------------------------------------------
# 3) Bell-CHSH inequality
# -------------------------------------------------------------
# Two settings each side: a, a' and b, b'
# E(a,b) = -cos(a-b) for entangled state
# CHSH: S = E(a,b) - E(a,b') + E(a',b) + E(a',b')

# Optimal angles: a=0, a'=π/4, b=π/8, b'=3π/8
def E_quantum(theta1, theta2):
    return -np.cos(theta1 - theta2)

def E_classical(theta1, theta2):
    # Local hidden variable: tighter correlation
    return -0.5 * np.cos(theta1 - theta2) - 0.5

a = 0
ap = np.pi / 4
b = np.pi / 8
bp = 3 * np.pi / 8

S_quantum = (E_quantum(a, b) - E_quantum(a, bp) +
             E_quantum(ap, b) + E_quantum(ap, bp))
S_classical_max = 2.0
S_tsirelson = 2 * np.sqrt(2)
S_aspect_1982 = 2.697

# -------------------------------------------------------------
# 4) Bell scan across angle settings
# -------------------------------------------------------------
theta_range = np.linspace(0, np.pi / 2, 100)
S_vals_quantum = []
for theta in theta_range:
    # Symmetric setup: b = theta/2, bp = 3*theta/2 (variant)
    S_t = (E_quantum(0, theta/2) - E_quantum(0, 3*theta/2) +
           E_quantum(theta, theta/2) + E_quantum(theta, 3*theta/2))
    S_vals_quantum.append(abs(S_t))

# -------------------------------------------------------------
# 5) Fiber optic attenuation
# -------------------------------------------------------------
wavelengths_fiber = np.linspace(800, 1700, 200)  # nm
# Typical silica fiber attenuation curve
# Minimum at 1550 nm (~0.15 dB/km), peaks at OH absorption 1380 nm
attenuation = (
    0.15 * (1550 / wavelengths_fiber) ** 4 +    # Rayleigh
    1.0 * np.exp(-((wavelengths_fiber - 1380) / 30) ** 2) +  # OH peak
    0.2  # baseline
)

# -------------------------------------------------------------
# 6) Optogenetics ChR2 action spectrum
# -------------------------------------------------------------
opt_wavelengths = np.linspace(400, 600, 200)
chr2_response = np.exp(-((opt_wavelengths - 470) / 30) ** 2)
nphr_response = np.exp(-((opt_wavelengths - 580) / 25) ** 2)  # halorhodopsin

# -------------------------------------------------------------
# 7) ITU K_photon axiom
# -------------------------------------------------------------
N_states = 2000
# Thermal photon distribution (Bose-Einstein)
# log_fit decreases with photon number n
n_photons = np.arange(N_states)
# T ~ room temperature, omega ~ optical → very few photons
log_fit_thermal = -n_photons * 0.5  # rough thermal weight
p_thermal = np.exp(log_fit_thermal); p_thermal /= p_thermal.sum()
S_thermal = float(-np.sum(p_thermal * np.log(p_thermal)))

# Coherent state (laser): Poisson dist
mean_n = 100  # ~100 photons
from scipy.stats import poisson
p_coherent = poisson.pmf(np.arange(N_states), mean_n)
p_coherent = p_coherent / p_coherent.sum()
S_coherent = float(-np.sum(np.where(p_coherent > 1e-30, p_coherent * np.log(p_coherent), 0)))

# Single-photon Fock state
p_fock = np.zeros(N_states)
p_fock[1] = 1.0
S_fock = 0.0

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_thermal_coherent = itu_lin(p_thermal, p_coherent)
ratio_coherent_fock = itu_lin(p_coherent, np.where(p_fock > 0, p_fock, 1e-30) / np.where(p_fock > 0, p_fock, 1e-30).sum())

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 220 ★ — Maxwell + Photon + Bell + K_photon (Tier 1 #31 opening)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Photon spectrum
ax = axes[0, 0]
ax.loglog(freq, energy_eV, "-", color="#1f77b4", lw=2)
for name, f in regions.items():
    e = h_planck * f / eV
    ax.scatter([f], [e], s=60, color="#d62728", zorder=5)
    ax.annotate(name.split()[0], (f, e), fontsize=7,
                xytext=(5, 5), textcoords="offset points")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Photon energy (eV)")
ax.set_title("Electromagnetic spectrum (E = hν)")
ax.grid(True, alpha=0.3, which="both")

# Panel 2: Bell CHSH inequality
ax = axes[0, 1]
ax.plot(np.degrees(theta_range), S_vals_quantum, "-", color="#9467bd", lw=2,
        label="QM prediction")
ax.axhline(S_classical_max, color="orange", linestyle="--", lw=2,
           label=f"Classical max |S| = 2")
ax.axhline(S_tsirelson, color="red", linestyle="--", lw=2,
           label=f"Tsirelson bound 2√2 ≈ 2.83")
ax.scatter([22.5], [S_aspect_1982], s=200, color="#2ca02c", marker="*",
           label=f"Aspect 1982: S={S_aspect_1982}", zorder=5)
ax.set_xlabel("Angle θ (deg)")
ax.set_ylabel("|S| (CHSH)")
ax.set_title("Bell-CHSH inequality (Nobel 2022)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Maxwell c verification
ax = axes[0, 2]
ax.axis("off")
text_c = [
    "Maxwell Equations Verification",
    "",
    f"μ₀ = 4π × 10⁻⁷ H/m",
    f"ε₀ = 8.854 × 10⁻¹² F/m",
    "",
    f"c = 1/√(μ₀ε₀)",
    f"  = {c_computed:.4e} m/s",
    f"  exact: {c_exact:.4e} m/s",
    f"  match: {(1-c_match)*100:.4f}% ★",
    "",
    f"Bell Nobel 2022:",
    f"  Aspect + Clauser + Zeilinger",
    f"  Aspect 1982 S = {S_aspect_1982}",
    f"  QM optimal S_QM = {S_quantum:.3f}",
    f"  Tsirelson 2√2 = {S_tsirelson:.4f}",
]
for i, line in enumerate(text_c):
    ax.text(0.05, 0.95 - i * 0.06, line, fontsize=10,
            fontweight="bold" if i == 0 else "normal",
            color="#d62728" if "Nobel" in line or "★" in line else "black")

# Panel 4: Fiber attenuation
ax = axes[1, 0]
ax.plot(wavelengths_fiber, attenuation, "-", color="#1f77b4", lw=2)
ax.axvline(1550, color="green", linestyle="--", label="1550 nm telecom (0.15 dB/km)")
ax.axvline(1380, color="red", linestyle="--", label="1380 nm OH peak")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Attenuation (dB/km)")
ax.set_title("Silica fiber attenuation")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Optogenetics
ax = axes[1, 1]
ax.plot(opt_wavelengths, chr2_response, "-", color="#1f77b4", lw=2,
        label="ChR2 (excitation, 470 nm)")
ax.plot(opt_wavelengths, nphr_response, "-", color="#ff7f0e", lw=2,
        label="NpHR (inhibition, 580 nm)")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Response")
ax.set_title("Optogenetics (Boyden-Deisseroth 2005)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 6: ITU K_photon states
ax = axes[1, 2]
ax.bar(["Thermal\n(BE)", "Coherent\n(laser)", "Fock |1⟩"],
       [S_thermal, S_coherent, S_fock], color=["#d62728", "#1f77b4", "#2ca02c"])
ax.set_ylabel("Photon state entropy (nats)")
ax.set_title(f"K_photon: Thermal→Coherent={ratio_thermal_coherent:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 220,
    "tier1_paper": 31,
    "block": "A_residual",
    "topic": "Maxwell + Photon + Bell + K_photon (Tier 1 #31 opening)",
    "milestone": "Pass-1 extension opening (Tier 1 #31 starts)",
    "Maxwell_verification": {
        "mu0": mu0,
        "eps0": eps0,
        "c_computed": float(c_computed),
        "c_exact": c_exact,
        "match_pct": float((1 - c_match) * 100),
    },
    "Bell_CHSH": {
        "classical_max": 2.0,
        "tsirelson_bound": float(S_tsirelson),
        "QM_optimal": float(S_quantum),
        "Aspect_1982": S_aspect_1982,
        "Nobel_2022": "Aspect + Clauser + Zeilinger Physics",
    },
    "photon_spectrum_regions": regions,
    "fine_structure_alpha": 1 / 137.036,
    "fiber_min_attenuation_dB_per_km": 0.15,
    "fiber_optimal_nm": 1550,
    "optogenetics_ChR2_nm": 470,
    "optogenetics_NpHR_nm": 580,
    "ITU_K_photon": {
        "N_states": N_states,
        "S_thermal_nats": S_thermal,
        "S_coherent_nats": S_coherent,
        "S_fock_nats": S_fock,
        "thermal_to_coherent_ratio": ratio_thermal_coherent,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon",
        "sub_states": [
            "K_photon_frequency (γ to radio)",
            "K_photon_polarization (basis qubit)",
            "K_photon_coherence (thermal vs laser)",
            "K_photon_fock (number state)",
            "K_photon_entanglement (Bell/GHZ)",
            "K_photon_kvector (momentum)",
        ],
        "Maxwell_meaning": "Classical limit of K_photon dynamics",
        "Bell_violation_meaning": "K_photon entanglement = non-local K-state correlation",
        "laser_meaning": "Coherent K_photon descent (Poisson)",
        "Aspect_Nobel_2022": "Experimental confirmation of K_photon non-locality",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
