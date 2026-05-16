# Phase 128: Inflation + CMB anisotropies + Inflaton K-state in ITU
# Tier 1 #19 Cosmology (Block A paper 3/9, phase 2/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 128: Inflation + CMB anisotropies + Inflaton K-state")
print("=" * 70)
print()

# Reduced Planck mass (in Planck units, M_Pl = 1)
M_PL = 1.0


# ----------------------------------------------------------------------
# Test 1: Slow-roll parameters for V(phi) = (1/2) m^2 phi^2 (chaotic inflation)
# ----------------------------------------------------------------------
def slow_roll_phi_squared(phi):
    """For V = (1/2) m^2 phi^2 in reduced Planck units."""
    epsilon = 2.0 * (M_PL / phi)**2
    eta = 2.0 * (M_PL / phi)**2
    return epsilon, eta


def test1_slow_roll():
    print("[Test 1] Slow-roll parameters: V = (1/2) m² φ² chaotic inflation")
    phi_values = [15.0, 13.0, 12.0, 11.0, 10.0, 8.0, 5.0, 3.0, 2.0]
    rows = []
    print(f"  {'φ (M_Pl)':<12}  {'ε':>10}  {'η':>10}  {'n_s = 1-6ε+2η':>16}  {'r = 16ε':>12}")
    for phi in phi_values:
        eps, eta = slow_roll_phi_squared(phi)
        n_s = 1.0 - 6.0 * eps + 2.0 * eta
        r = 16.0 * eps
        print(f"  {phi:<12.2f}  {eps:>10.4f}  {eta:>10.4f}  {n_s:>16.4f}  {r:>12.4f}")
        rows.append({"phi_Mpl": phi, "epsilon": float(eps), "eta": float(eta),
                     "n_s": float(n_s), "r": float(r)})

    # Find phi where n_s = 0.965 (observed)
    target_ns = 0.965
    phi_dense = np.linspace(1.0, 20.0, 1000)
    eps_arr = 2.0 * (M_PL / phi_dense)**2
    eta_arr = 2.0 * (M_PL / phi_dense)**2
    n_s_arr = 1.0 - 6.0 * eps_arr + 2.0 * eta_arr
    idx = int(np.argmin(np.abs(n_s_arr - target_ns)))
    phi_match = phi_dense[idx]
    r_match = 16.0 * eps_arr[idx]
    print()
    print(f"  Match Planck 2018 n_s = {target_ns}: φ ≈ {phi_match:.3f} M_Pl")
    print(f"  Predicted r ≈ {r_match:.4f}  (Planck+BICEP/Keck 2021 limit: r < 0.06)")
    return {"rows": rows, "phi_match_n_s": float(phi_match), "r_predicted": float(r_match)}


# ----------------------------------------------------------------------
# Test 2: e-folds N(phi) = phi^2 / 4 - 1/2 (for chaotic V = m^2 phi^2 / 2)
# ----------------------------------------------------------------------
def test2_e_folds():
    print("\n[Test 2] e-folds N(φ) for chaotic inflation V = (1/2) m² φ²")
    # End of inflation: epsilon = 1 -> phi_end = sqrt(2) M_Pl
    phi_end = np.sqrt(2.0)
    phi_start_values = [12.0, 14.0, 15.5, 17.5]
    rows = []
    print(f"  φ_end (ε=1) = √2 ≈ {phi_end:.4f} M_Pl")
    print(f"  {'φ_start (M_Pl)':<15}  {'N e-folds':>12}")
    for phi_s in phi_start_values:
        N = (phi_s**2 - phi_end**2) / 4.0
        print(f"  {phi_s:<15.2f}  {N:>12.2f}")
        rows.append({"phi_start_Mpl": phi_s, "N_efolds": float(N)})

    print(f"\n  Target N ≈ 50-60 for solving horizon/flatness problems")
    print(f"  -> φ_start ≈ 14-15.5 M_Pl gives natural N = 50-60")
    return rows


# ----------------------------------------------------------------------
# Test 3: CMB power spectrum C_ℓ (toy 5 peaks)
# ----------------------------------------------------------------------
def test3_cmb_power_spectrum():
    print("\n[Test 3] CMB power spectrum C_ℓ (5 acoustic peaks)")
    ell_arr = np.linspace(2, 2500, 500)

    # Sachs-Wolfe plateau at low ℓ
    SW_plateau = 1100 * (10.0 / ell_arr)**0.0
    SW_plateau = np.where(ell_arr < 30, 1100.0, SW_plateau)

    # Acoustic peaks (rough sin² model with damping)
    peak_pos = [220, 540, 810, 1140, 1450]
    peak_amp = [5800, 2500, 2500, 1400, 800]
    peak_width = [100, 110, 130, 150, 180]
    C_ell = np.zeros_like(ell_arr)
    for ip, pos in enumerate(peak_pos):
        gaussian = peak_amp[ip] * np.exp(-((ell_arr - pos) / peak_width[ip])**2)
        C_ell += gaussian

    # Add Sachs-Wolfe at low ℓ
    low_ell_mask = ell_arr < 30
    C_ell[low_ell_mask] = SW_plateau[low_ell_mask]
    # Smooth transition
    transition = np.exp(-((ell_arr - 50)**2 / 30**2))
    C_ell += 800 * transition

    # Damping tail at high ℓ
    C_ell *= np.exp(-((ell_arr - 1500) / 800)**2 / 2)
    C_ell[ell_arr < 1500] /= np.exp(-((ell_arr[ell_arr < 1500] - 1500) / 800)**2 / 2)

    print(f"  Toy model with peaks at ℓ = {peak_pos}")
    print(f"  Peak amplitudes (μK²): {peak_amp}")
    print(f"  C_ℓ max (1st peak): {peak_amp[0]} μK²")
    return {"ell": ell_arr.tolist(), "C_ell": C_ell.tolist(),
            "peak_pos": peak_pos, "peak_amp": peak_amp}


# ----------------------------------------------------------------------
# Test 4: r upper limit history (observation chain)
# ----------------------------------------------------------------------
def test4_r_history():
    print("\n[Test 4] Tensor-to-scalar ratio r upper limit history")
    history = [
        ("COBE (1992)",                    1.0),
        ("WMAP (2009)",                    0.20),
        ("Planck (2013)",                  0.12),
        ("Planck (2018)",                  0.10),
        ("Planck + BICEP/Keck (2021)",     0.06),
        ("LiteBIRD target (2032+)",        0.001),
        ("CMB-S4 target (2030s)",          0.0005),
    ]
    print(f"  {'Experiment':<32}  {'r upper limit':>15}")
    rows = []
    for name, r in history:
        print(f"  {name:<32}  {r:>15.4f}")
        rows.append({"experiment": name, "r_upper": r})
    return rows


# ----------------------------------------------------------------------
# Test 5: Inflaton potential examples
# ----------------------------------------------------------------------
def test5_inflaton_potentials():
    print("\n[Test 5] Inflaton potential V(φ) examples")
    phi_arr = np.linspace(0.01, 20, 200)
    # 4 potentials
    V_phi2 = 0.5 * phi_arr**2   # chaotic phi^2
    V_phi4 = 0.25 * phi_arr**4  # chaotic phi^4
    # Starobinsky-like: V ∝ (1 - e^{-sqrt(2/3) phi})^2 (R^2 inflation)
    V_starobinsky = (1 - np.exp(-np.sqrt(2.0/3.0) * phi_arr))**2 * 50
    # New inflation: V ∝ -m^2 phi^2 + lambda phi^4 (hilltop)
    V_hilltop = 100 - 0.5 * phi_arr**2 + 0.05 * phi_arr**4
    V_hilltop = np.where(V_hilltop > 0, V_hilltop, 0)

    potentials = {
        "phi^2 (chaotic)": V_phi2,
        "phi^4 (chaotic)": V_phi4,
        "Starobinsky R²": V_starobinsky,
        "Hilltop": V_hilltop,
    }

    print("  Common inflaton models:")
    print("    V(φ) = (1/2) m² φ² (chaotic, predicted r ≈ 0.13)")
    print("    V(φ) = λ φ⁴ (chaotic, excluded by Planck+BICEP)")
    print("    V(φ) = (1 - e^{-√(2/3)φ})² (Starobinsky R², r ≈ 0.003)")
    print("    V(φ) = V_0 - (1/2)m²φ² + λφ⁴ (hilltop, very small r)")
    return {"phi": phi_arr.tolist(),
            "V_phi2": V_phi2.tolist(),
            "V_phi4": V_phi4.tolist(),
            "V_starobinsky": V_starobinsky.tolist(),
            "V_hilltop": V_hilltop.tolist()}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
slow_roll = test1_slow_roll()
efolds = test2_e_folds()
cmb = test3_cmb_power_spectrum()
r_hist = test4_r_history()
potentials = test5_inflaton_potentials()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Slow-roll: n_s vs r plot
ax = axes[0, 0]
phi_vals = [r["phi_Mpl"] for r in slow_roll["rows"]]
n_s_vals = [r["n_s"] for r in slow_roll["rows"]]
r_vals = [r["r"] for r in slow_roll["rows"]]
ax.scatter(n_s_vals, r_vals, c=phi_vals, cmap="viridis", s=100, edgecolor="black")
for r in slow_roll["rows"]:
    ax.annotate(f"φ={r['phi_Mpl']:.0f}", (r["n_s"], r["r"]),
                textcoords="offset points", xytext=(5, 5), fontsize=8)
ax.axvline(0.965, color="red", linestyle="--", linewidth=1, label="Planck n_s=0.965")
ax.axhline(0.06, color="orange", linestyle="--", linewidth=1, label="r=0.06 (P+BK)")
ax.axhline(0.001, color="green", linestyle=":", linewidth=1, label="r=0.001 (LiteBIRD)")
ax.set_xlabel("n_s (scalar spectral index)")
ax.set_ylabel("r (tensor-to-scalar)")
ax.set_yscale("log")
ax.set_title("Slow-roll: V=(1/2)m²φ² inflaton", fontsize=12)
ax.legend(fontsize=9, loc="upper left")
ax.grid(True, alpha=0.3)

# Panel 2: e-folds N(phi)
ax = axes[0, 1]
phi_arr = np.linspace(np.sqrt(2), 20, 100)
N_arr = (phi_arr**2 - 2.0) / 4.0
ax.plot(phi_arr, N_arr, "-", color="#4c72b0", linewidth=2)
ax.axhspan(50, 60, color="green", alpha=0.2, label="Target N=50-60")
ax.set_xlabel(r"$\phi_{start}$ (M$_{Pl}$)")
ax.set_ylabel("N (e-folds)")
ax.set_title("e-folds vs starting field (chaotic V=m²φ²/2)", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: CMB power spectrum
ax = axes[1, 0]
ell = np.array(cmb["ell"])
C_ell_norm = np.array(cmb["C_ell"]) * ell * (ell + 1) / (2 * np.pi) / 1000  # rescale
ax.plot(ell, C_ell_norm, "-", color="#4c72b0", linewidth=2)
for ip, pos in enumerate(cmb["peak_pos"]):
    ax.axvline(pos, color="red", linestyle=":", linewidth=0.8, alpha=0.6)
    ax.text(pos, ax.get_ylim()[1] * 0.85 - ip * 0.1 * ax.get_ylim()[1],
            f"ℓ={pos}", color="red", fontsize=8, ha="center")
ax.set_xlabel(r"Multipole $\ell$")
ax.set_ylabel(r"$\ell(\ell+1) C_\ell / 2\pi$ (a.u.)")
ax.set_title("CMB temperature power spectrum (toy 5 peaks)", fontsize=12)
ax.set_xscale("log")
ax.grid(True, alpha=0.3, which="both")

# Panel 4: r upper limit history
ax = axes[1, 1]
exps = [r["experiment"] for r in r_hist]
r_lims = [r["r_upper"] for r in r_hist]
colors = plt.cm.viridis(np.linspace(0, 1, len(exps)))
ax.barh(exps, r_lims, color=colors)
for i, v in enumerate(r_lims):
    ax.text(v * 1.1, i, f"{v}", va="center", fontsize=9)
ax.set_xscale("log")
ax.set_xlabel(r"r upper limit")
ax.set_title("Tensor-to-scalar ratio r: observational history", fontsize=12)
ax.grid(True, alpha=0.3, which="both", axis="x")
plt.setp(ax.get_yticklabels(), fontsize=8)

fig.suptitle("Phase 128: Inflation + CMB Anisotropies + Inflaton K-state",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "inflation_cmb.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 128,
    "title": "Inflation + CMB anisotropies + Inflaton K-state",
    "tier1_id": 19,
    "tier1_name": "Cosmology",
    "block": "A (Physics/Math) — paper 3/9, phase 2/8",
    "slow_roll_parameters": slow_roll,
    "e_folds_chaotic": efolds,
    "cmb_power_spectrum_peaks": {
        "peak_positions_ell": cmb["peak_pos"],
        "peak_amplitudes_uK2": cmb["peak_amp"],
    },
    "r_history": r_hist,
    "inflaton_models": [
        "phi^2 (chaotic)", "phi^4 (chaotic, excluded)",
        "Starobinsky R^2", "Hilltop"
    ],
    "verdict": ("Inflation = ITU axiom dS = d<K> earliest cosmic realization; "
                "inflaton phi K-state's quantum fluctuations imprint CMB anisotropies; "
                "LiteBIRD 2032+ targets r ~ 0.001 to detect primordial GW."),
}

json_path = "inflation_cmb_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 128 complete: inflation + CMB + inflaton K-state in ITU;")
print(f"  Match n_s=0.965 at φ ≈ {slow_roll['phi_match_n_s']:.2f} M_Pl, r ≈ {slow_roll['r_predicted']:.4f}")
print("=" * 70)
