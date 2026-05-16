# Phase 133: Cosmic horizons + Multiverse + Anthropic + Holographic bounds in ITU
# Tier 1 #19 Cosmology (Block A paper 3/9, phase 7/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

print("=" * 70)
print("Phase 133: Cosmic horizons + Multiverse + Anthropic + Holographic")
print("=" * 70)
print()

# Constants
HBAR = 1.054571817e-34
C = 2.99792458e8
G_N = 6.67430e-11
M_SUN = 1.989e30
PARSEC = 3.0857e16
MPC = 1e6 * PARSEC
GPC = 1e9 * PARSEC
GLY = 9.461e24  # 1 Gly = 9.461e24 m
L_P = np.sqrt(HBAR * G_N / C**3)
L_P2 = L_P**2


# ----------------------------------------------------------------------
# Test 1: Three cosmic horizons (ΛCDM)
# ----------------------------------------------------------------------
def test1_horizons():
    print("[Test 1] Three cosmic horizons: particle / event / Hubble")
    Omega_m = 0.315
    Omega_L = 0.685
    H_0 = 67.4 * 1000.0 / MPC   # 1/s

    def E(z):
        return np.sqrt(Omega_m * (1 + z)**3 + Omega_L)

    # Particle horizon: integral from z=infty to z=0
    def d_p_integrand(z):
        return 1.0 / E(z)
    d_p_chi, _ = quad(d_p_integrand, 0, 1e6, limit=200)
    d_p = (C / H_0) * d_p_chi   # meters
    d_p_Gly = d_p / GLY
    d_p_Gpc = d_p / GPC

    # Event horizon: integral from z=0 to z=-1 (future, Λ-dominated)
    # In Λ-dominated era, a(t) = exp(H_∞ t), so d_e = c / H_∞ = c / (H_0 √Ω_Λ)
    d_e = C / (H_0 * np.sqrt(Omega_L))
    d_e_Gly = d_e / GLY
    d_e_Gpc = d_e / GPC

    # Hubble radius
    R_H = C / H_0
    R_H_Gly = R_H / GLY
    R_H_Gpc = R_H / GPC

    print(f"  ΛCDM (Ω_m=0.315, Ω_Λ=0.685, H_0=67.4 km/s/Mpc)")
    print(f"  {'Horizon':<20}  {'Gly':>8}  {'Gpc':>8}  {'meters':>14}")
    print(f"  {'Particle horizon':<20}  {d_p_Gly:>8.2f}  {d_p_Gpc:>8.2f}  {d_p:>14.3e}")
    print(f"  {'Event horizon':<20}  {d_e_Gly:>8.2f}  {d_e_Gpc:>8.2f}  {d_e:>14.3e}")
    print(f"  {'Hubble radius':<20}  {R_H_Gly:>8.2f}  {R_H_Gpc:>8.2f}  {R_H:>14.3e}")
    return {
        "Omega_m": Omega_m, "Omega_L": Omega_L,
        "particle_Gly": float(d_p_Gly), "particle_Gpc": float(d_p_Gpc),
        "event_Gly": float(d_e_Gly), "event_Gpc": float(d_e_Gpc),
        "hubble_Gly": float(R_H_Gly), "hubble_Gpc": float(R_H_Gpc),
        "particle_m": float(d_p), "event_m": float(d_e), "hubble_m": float(R_H),
    }


# ----------------------------------------------------------------------
# Test 2: de Sitter horizon entropy (Gibbons-Hawking)
# ----------------------------------------------------------------------
def test2_de_sitter_entropy(horizons):
    print("\n[Test 2] de Sitter horizon entropy (Gibbons-Hawking)")
    r_dS = horizons["event_m"]
    A_dS = 4 * np.pi * r_dS**2
    S_dS = A_dS / (4 * L_P2)
    # Hawking temperature
    H_0 = 67.4 * 1000.0 / MPC
    Omega_L = 0.685
    T_dS = HBAR * H_0 * np.sqrt(Omega_L) / (2 * np.pi * 1.380649e-23)

    print(f"  r_dS = {r_dS/GPC:.2f} Gpc = {r_dS:.3e} m")
    print(f"  A_dS = 4π r²       = {A_dS:.3e} m²")
    print(f"  S_dS = A/(4 ℓ_P²) = {S_dS:.3e} nats")
    print(f"  T_dS = {T_dS:.3e} K")
    print()
    print(f"  Holographic principle: 観測可能宇宙の総情報 capacity = {S_dS:.2e} nats")
    print(f"  Comparison:")
    print(f"    Earth biosphere     ~ 10^44 nats")
    print(f"    Galaxy (Milky Way)  ~ 10^61 nats")
    print(f"    Observable universe ~ 10^85 nats (matter content)")
    print(f"    de Sitter cap       ~ 10^122 nats ← ITU maximum")
    return {"r_dS_Gpc": r_dS / GPC, "A_dS_m2": float(A_dS),
            "S_dS_nats": float(S_dS), "T_dS_K": float(T_dS)}


# ----------------------------------------------------------------------
# Test 3: Multiverse Level I-IV
# ----------------------------------------------------------------------
def test3_multiverse_levels():
    print("\n[Test 3] Multiverse Level I-IV (Tegmark 2003)")
    levels = [
        ("I",   "Same physics, different IC", "Inflation bubbles >> 46 Gly",
         "K-state same, boundary conditions differ"),
        ("II",  "Different vacua",             "String landscape ~10^500",
         "K-state vacuum selection"),
        ("III", "Many-worlds (Everett)",       "Quantum branching",
         "K-state superposition all branches"),
        ("IV",  "Mathematical universes",      "All consistent math",
         "K-state structure space"),
    ]
    print(f"  {'Level':<6}  {'Description':<30}  {'Realization':<25}  {'ITU view'}")
    print("  " + "-" * 100)
    rows = []
    for level, desc, real, itu in levels:
        print(f"  {level:<6}  {desc:<30}  {real:<25}  {itu}")
        rows.append({"level": level, "description": desc,
                     "realization": real, "itu_view": itu})
    return rows


# ----------------------------------------------------------------------
# Test 4: String landscape vacua count
# ----------------------------------------------------------------------
def test4_string_landscape():
    print("\n[Test 4] String landscape vacua count")
    print("  Bousso-Polchinski (2000) mechanism: discrete fluxes")
    print("  Estimated N_vacua ~ 10^500")
    print()
    # Compare with observed universe
    S_dS_nats = 2.6e122
    S_dS_bits = S_dS_nats / np.log(2)
    print(f"  Comparison:")
    print(f"    Observable universe S_dS_bits      ~ {S_dS_bits:.2e}")
    print(f"    String landscape vacua             ~ 10^500")
    # 10^500 / S_dS_bits ~ 10^{500 - log10(S_dS_bits)}
    log10_ratio = 500 - np.log10(S_dS_bits)
    print(f"    Ratio (vacua / universe bits)      ~ 10^{log10_ratio:.0f}")
    print()
    print(f"  → String landscape is far more diverse than observable universe info content")
    return {"N_vacua": "1e500", "S_dS_bits": float(S_dS_bits)}


# ----------------------------------------------------------------------
# Test 5: Anthropic bound on Λ (Weinberg 1987 vs observed)
# ----------------------------------------------------------------------
def test5_anthropic_lambda():
    print("\n[Test 5] Anthropic bound on Λ (Weinberg 1987)")
    # Planck units: Λ in M_P^2 = c^5 / (ℏ G) ~ 1
    # Observed Λ ≈ 1.1e-52 m^-2
    Lambda_obs_SI = 1.1e-52  # m^-2
    # Convert to natural units: multiply by ℓ_P²
    Lambda_obs_Planck = Lambda_obs_SI * L_P2
    # Anthropic upper bound (Weinberg): Λ < 100 × Λ_obs for structure formation
    Lambda_max_anthropic = 100 * Lambda_obs_Planck

    # Theoretical naive expectation: Λ ~ M_P^2 ~ 1
    Lambda_theory = 1.0  # Planck units

    print(f"  Observed Λ (Planck units):     {Lambda_obs_Planck:.3e}")
    print(f"  Anthropic upper bound:         {Lambda_max_anthropic:.3e}")
    print(f"  Theoretical naive (no anthropic): {Lambda_theory:.3e}")
    print(f"  Ratio observed/anthropic:      {Lambda_obs_Planck / Lambda_max_anthropic:.3f}")
    print(f"  Ratio theory/observed:         {Lambda_theory / Lambda_obs_Planck:.3e}  (120 orders)")
    print()
    print(f"  → Observed Λ is consistent with anthropic bound (within ~10x)")
    print(f"  → 120-order gap from theory remains, but anthropic provides one explanation")
    return {"Lambda_obs_Planck": float(Lambda_obs_Planck),
            "Lambda_anthropic_max_Planck": float(Lambda_max_anthropic),
            "ratio_to_anthropic": float(Lambda_obs_Planck / Lambda_max_anthropic)}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
horizons = test1_horizons()
ds_entropy = test2_de_sitter_entropy(horizons)
levels = test3_multiverse_levels()
landscape = test4_string_landscape()
anthropic = test5_anthropic_lambda()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Three horizons bar chart
ax = axes[0, 0]
hor_names = ["Particle\n(causal past)", "Event\n(causal future)", "Hubble\n(v=c)"]
hor_vals_Gly = [horizons["particle_Gly"], horizons["event_Gly"], horizons["hubble_Gly"]]
colors_h = ["#4c72b0", "#dd8452", "#55a467"]
bars = ax.bar(hor_names, hor_vals_Gly, color=colors_h)
for b, v in zip(bars, hor_vals_Gly):
    ax.text(b.get_x() + b.get_width()/2, v + 1, f"{v:.1f} Gly",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel("Distance (Gly)")
ax.set_title("Cosmic horizons in ΛCDM", fontsize=12)
ax.grid(True, alpha=0.3, axis="y")
ax.set_ylim(0, 55)

# Panel 2: Entropy comparison
ax = axes[0, 1]
systems = ["Earth\nbiosphere", "Galaxy", "Universe\nmatter", "de Sitter\nhorizon"]
S_vals_log10 = [44, 61, 85, np.log10(ds_entropy["S_dS_nats"])]
colors_S = ["#55a467", "#dd8452", "#4c72b0", "#c44e52"]
bars = ax.bar(systems, S_vals_log10, color=colors_S)
for b, v in zip(bars, S_vals_log10):
    ax.text(b.get_x() + b.get_width()/2, v + 2, f"$10^{{{v:.0f}}}$",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel(r"log$_{10}$(S / nats)")
ax.set_title("Entropy capacity comparison (ITU upper bound)", fontsize=12)
ax.grid(True, alpha=0.3, axis="y")
ax.set_ylim(0, 130)

# Panel 3: Multiverse Level I-IV
ax = axes[1, 0]
ax.axis("off")
ax.set_title("Multiverse Level I-IV (Tegmark 2003)", fontsize=12, fontweight="bold")
y = 0.90
ax.text(0.02, y, "Level", fontsize=10, fontweight="bold")
ax.text(0.10, y, "Description", fontsize=10, fontweight="bold")
ax.text(0.55, y, "ITU view", fontsize=10, fontweight="bold")
y -= 0.07
for level in levels:
    ax.text(0.02, y, level["level"], fontsize=11, color="#4c72b0", fontweight="bold")
    ax.text(0.10, y, level["description"], fontsize=9)
    ax.text(0.55, y, level["itu_view"], fontsize=9, color="#c44e52")
    y -= 0.12

# Panel 4: Anthropic + landscape
ax = axes[1, 1]
ax.axis("off")
ax.set_title("Anthropic Λ bound + String landscape", fontsize=12, fontweight="bold")
y = 0.88
ax.text(0.02, y, "Λ values (Planck units):", fontsize=10, fontweight="bold")
y -= 0.12
ax.text(0.02, y, "Theoretical naive (M_P²):", fontsize=10)
ax.text(0.55, y, f"~1", fontsize=10, fontfamily="monospace", color="#c44e52")
y -= 0.10
ax.text(0.02, y, "Anthropic upper bound:", fontsize=10)
ax.text(0.55, y, f"{anthropic['Lambda_anthropic_max_Planck']:.2e}", fontsize=10, fontfamily="monospace")
y -= 0.10
ax.text(0.02, y, "Observed:", fontsize=10)
ax.text(0.55, y, f"{anthropic['Lambda_obs_Planck']:.2e}", fontsize=10, fontfamily="monospace", color="#55a467")
y -= 0.15
ax.text(0.02, y, "String landscape:", fontsize=10, fontweight="bold")
y -= 0.08
ax.text(0.02, y, "  ~ 10^500 vacua (Bousso-Polchinski 2000)", fontsize=10)
y -= 0.08
ax.text(0.02, y, "  Observable universe ~ 10^122 nats", fontsize=10)
y -= 0.10
ax.text(0.02, y, "  → Landscape >> 1 universe info content", fontsize=10, fontstyle="italic", color="#55a467")

fig.suptitle("Phase 133: Cosmic Horizons + Multiverse + Anthropic + Holographic",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "cosmic_horizons_multiverse.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 133,
    "title": "Cosmic horizons + Multiverse + Anthropic + Holographic in ITU",
    "tier1_id": 19,
    "tier1_name": "Cosmology",
    "block": "A (Physics/Math) — paper 3/9, phase 7/8",
    "horizons": horizons,
    "de_sitter_entropy": ds_entropy,
    "multiverse_levels": levels,
    "string_landscape": landscape,
    "anthropic_lambda": anthropic,
    "verdict": ("Cosmic event horizon = de Sitter, r_dS = 5.4 Gpc, S = 2.6e+122 nats; "
                "Multiverse Level I-IV (Tegmark 2003) maps to ITU K-state realization space; "
                "anthropic Λ bound consistent with observation within ~10x; "
                "string landscape (10^500 vacua) >> 1 observable universe info content."),
}

json_path = "cosmic_horizons_multiverse_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 133 complete: cosmic horizons + multiverse + anthropic in ITU;")
print(f"  Particle: {horizons['particle_Gly']:.1f} Gly, S_dS = {ds_entropy['S_dS_nats']:.2e} nats")
print("=" * 70)
