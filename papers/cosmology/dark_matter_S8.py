# Phase 129: Dark Matter + Structure formation + S_8 tension + K_DM in ITU
# Tier 1 #19 Cosmology (Block A paper 3/9, phase 3/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 129: Dark Matter + Structure formation + S_8 tension")
print("=" * 70)
print()

# Constants
G_N = 6.67430e-11
M_SUN = 1.989e30
KPC = 3.0857e19   # 1 kpc in meters


# ----------------------------------------------------------------------
# Test 1: Galaxy rotation curve (Milky Way toy model)
# ----------------------------------------------------------------------
def test1_rotation_curve():
    print("[Test 1] Galaxy rotation curve (Milky Way toy model)")
    r_kpc = np.linspace(0.5, 50.0, 100)
    r = r_kpc * KPC

    # Visible mass distribution: exponential disk
    M_disk = 5e10 * M_SUN
    R_disk = 3 * KPC
    M_visible = M_disk * (1 - np.exp(-r / R_disk) * (1 + r / R_disk))

    # Visible-only Keplerian v_rot = sqrt(G M(<r) / r)
    v_visible = np.sqrt(G_N * M_visible / r) / 1000.0   # km/s

    # NFW DM halo
    M_DM_200 = 1.2e12 * M_SUN   # Milky Way halo mass
    r_200 = 200 * KPC
    c_NFW = 12.0   # concentration
    rs_NFW = r_200 / c_NFW
    # M_DM(<r) for NFW: M(r) = 4π ρ_s r_s³ [ln(1+r/r_s) - (r/r_s)/(1+r/r_s)]
    rho_s = M_DM_200 / (4 * np.pi * rs_NFW**3 * (np.log(1 + c_NFW) - c_NFW / (1 + c_NFW)))
    x = r / rs_NFW
    M_DM = 4 * np.pi * rho_s * rs_NFW**3 * (np.log(1 + x) - x / (1 + x))

    # Total rotation
    M_total = M_visible + M_DM
    v_total = np.sqrt(G_N * M_total / r) / 1000.0   # km/s

    # Reference: solar position
    r_solar_kpc = 8.2
    idx_solar = int(np.argmin(np.abs(r_kpc - r_solar_kpc)))
    v_solar = v_total[idx_solar]
    v_visible_solar = v_visible[idx_solar]

    print(f"  At r = {r_solar_kpc} kpc (solar position):")
    print(f"    v_visible (disk only) = {v_visible_solar:.1f} km/s")
    print(f"    v_total (disk + DM)    = {v_solar:.1f} km/s  (obs: ~220 km/s)")
    print(f"  DM contribution: ~{(v_solar - v_visible_solar):.1f} km/s")
    return {"r_kpc": r_kpc.tolist(),
            "v_visible_kms": v_visible.tolist(),
            "v_total_kms": v_total.tolist(),
            "v_solar_kms": float(v_solar),
            "v_visible_solar_kms": float(v_visible_solar)}


# ----------------------------------------------------------------------
# Test 2: DM candidate mass ranges
# ----------------------------------------------------------------------
def test2_dm_candidates():
    print("\n[Test 2] DM candidate mass ranges")
    candidates = [
        ("Fuzzy DM",         1e-22,    1e-19,   "ultralight scalar (string)"),
        ("QCD axion",        1e-6,     1e-3,    "Peccei-Quinn pseudoscalar"),
        ("Sterile neutrino", 1e3,      1e4,     "right-handed ν (keV)"),
        ("WIMP",             1e10,     1e13,    "thermal relic (GeV-TeV)"),
        ("Primordial BH",    1e17,     1e22,    "asteroid mass window"),
        ("MACHO",            1e29,     1e31,    "lunar-stellar mass"),
    ]
    print(f"  {'Candidate':<22}  {'m_min (eV)':>14}  {'m_max (eV)':>14}  {'Type'}")
    rows = []
    for name, mmin, mmax, t in candidates:
        print(f"  {name:<22}  {mmin:>14.2e}  {mmax:>14.2e}  {t}")
        rows.append({"name": name, "m_min_eV": mmin, "m_max_eV": mmax, "type": t})
    print(f"\n  Total mass range covered: 10^-22 - 10^31 eV = 53 orders of magnitude")
    return rows


# ----------------------------------------------------------------------
# Test 3: Matter power spectrum P(k)
# ----------------------------------------------------------------------
def test3_power_spectrum():
    print("\n[Test 3] Matter power spectrum P(k)")
    k = np.logspace(-3, 2, 500)   # h/Mpc
    n_s = 0.965
    # Toy P(k): turnover at matter-radiation equality k_eq ~ 0.01 h/Mpc
    k_eq = 0.01
    # Below k_eq: P(k) ∝ k^{n_s}
    # Above k_eq: P(k) ∝ k^{n_s - 4} (transfer function suppression)
    transfer = (1 + (k / k_eq)**2)**(-1)   # rough
    P = k**n_s * transfer**2

    # Normalize so that sigma_8 = 0.811 (Planck 2018)
    # Compute sigma_8 from the toy spectrum (in arbitrary units)
    R8_inv_Mpc = 1.0 / 8.0   # h Mpc^-1 → k=1/8 h/Mpc
    # Top-hat filter
    W = lambda kR: (3 / (kR)**3) * (np.sin(kR) - kR * np.cos(kR))
    kR_arr = k * 8.0
    W_arr = np.where(kR_arr > 0, (3 / kR_arr**3) * (np.sin(kR_arr) - kR_arr * np.cos(kR_arr)), 1.0)
    integrand = k**2 * P * W_arr**2
    sigma8_sq_unnorm = np.trapezoid(integrand, k)
    # Normalize so sigma_8 = 0.811
    sigma8_target = 0.811
    norm = sigma8_target**2 / sigma8_sq_unnorm
    P_normalized = P * norm

    print(f"  Toy P(k) ∝ k^n_s × T(k)^2, n_s = {n_s}")
    print(f"  k_eq (matter-radiation eq) = {k_eq} h/Mpc")
    print(f"  Normalized so σ_8 = 0.811 (Planck 2018)")
    return {"k_h_per_Mpc": k.tolist(),
            "P_k": P_normalized.tolist(),
            "n_s": n_s,
            "k_eq": k_eq,
            "sigma_8": sigma8_target}


# ----------------------------------------------------------------------
# Test 4: S_8 tension
# ----------------------------------------------------------------------
def test4_s8_tension():
    print("\n[Test 4] S_8 tension: CMB vs weak lensing")
    surveys = [
        ("Planck 2018 (CMB)",      0.834, 0.016),
        ("KiDS-1000 (2021)",       0.766, 0.020),
        ("DES Y3 (2022)",          0.776, 0.017),
        ("HSC Y3 (2023)",          0.776, 0.024),
    ]
    print(f"  {'Survey':<26}  {'S_8':>8}  {'σ':>8}")
    rows = []
    for name, s8, err in surveys:
        print(f"  {name:<26}  {s8:>8.3f}  ± {err:.3f}")
        rows.append({"survey": name, "S_8": s8, "sigma": err})

    # Compute tension Planck vs KiDS-DES-HSC average
    S_8_lensing = np.mean([0.766, 0.776, 0.776])
    err_lensing = np.sqrt(np.sum([0.020**2, 0.017**2, 0.024**2])) / 3
    S_8_Planck = 0.834
    err_Planck = 0.016
    diff = S_8_Planck - S_8_lensing
    combined_err = np.sqrt(err_lensing**2 + err_Planck**2)
    sigma_tension = diff / combined_err
    print(f"\n  Weak lensing avg: S_8 = {S_8_lensing:.3f} ± {err_lensing:.3f}")
    print(f"  Difference Planck vs lensing: {diff:.3f}")
    print(f"  Tension: {sigma_tension:.2f}σ")
    return {"surveys": rows, "tension_sigma": float(sigma_tension)}


# ----------------------------------------------------------------------
# Test 5: Linear growth factor D(a) in ΛCDM
# ----------------------------------------------------------------------
def test5_linear_growth():
    print("\n[Test 5] Linear growth factor D(a) in ΛCDM")
    Omega_m = 0.315
    Omega_L = 0.685

    def Omega_m_at_a(a):
        return Omega_m / a**3 / (Omega_m / a**3 + Omega_L)

    a_arr = np.logspace(-3, 0, 100)
    # Approximate growth function (Carroll-Press-Turner 1992)
    def g(a):
        Om = Omega_m_at_a(a)
        return 2.5 * Om / (Om**(4/7) - Omega_L * (1 - Omega_L * Om / 2.0) + (1 + Om/2))

    # Better: D(a) ≈ a × g(a) / g(1)  for matter-Λ universe
    # Use Heath 1977 approximation:
    g_arr = np.array([g(a) for a in a_arr])
    D_arr = a_arr * g_arr / g(1.0)

    samples = [0.001, 0.01, 0.1, 0.5, 1.0]
    print(f"  Ω_m = {Omega_m}, Ω_Λ = {Omega_L}")
    print(f"  {'a (1/(1+z))':<15}  {'z':>10}  {'D(a)':>10}")
    for a in samples:
        z = 1/a - 1
        idx = int(np.argmin(np.abs(a_arr - a)))
        D = D_arr[idx]
        print(f"  {a:<15.4f}  {z:>10.2f}  {D:>10.4f}")
    print(f"\n  D(0)=0, D(matter era) = a, D(now) = 1 (normalized).")
    return {"a": a_arr.tolist(), "D": D_arr.tolist()}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
rot = test1_rotation_curve()
dm = test2_dm_candidates()
power = test3_power_spectrum()
s8 = test4_s8_tension()
growth = test5_linear_growth()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Galaxy rotation curve
ax = axes[0, 0]
ax.plot(rot["r_kpc"], rot["v_visible_kms"], "--", color="#c44e52", linewidth=2,
        label="visible only (disk)")
ax.plot(rot["r_kpc"], rot["v_total_kms"], "-", color="#4c72b0", linewidth=2,
        label="visible + DM (NFW halo)")
ax.axvline(8.2, color="gray", linestyle=":", linewidth=1)
ax.axhline(220, color="green", linestyle=":", linewidth=1, label="observed Sun: 220 km/s")
ax.text(8.5, 100, "Sun", color="gray", fontsize=9)
ax.set_xlabel("r (kpc)")
ax.set_ylabel("v_rot (km/s)")
ax.set_title("Milky Way rotation curve: visible vs visible+DM", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 300)

# Panel 2: DM candidate mass ranges
ax = axes[0, 1]
names = [r["name"] for r in dm]
m_mins = [r["m_min_eV"] for r in dm]
m_maxs = [r["m_max_eV"] for r in dm]
colors = plt.cm.viridis(np.linspace(0, 1, len(names)))
y_pos = np.arange(len(names))
for i, (mmin, mmax) in enumerate(zip(m_mins, m_maxs)):
    ax.barh(i, np.log10(mmax) - np.log10(mmin), left=np.log10(mmin),
            color=colors[i], alpha=0.8)
    ax.text(np.log10(mmin) - 0.5, i, f"{np.log10(mmin):.0f}", ha="right", fontsize=7)
    ax.text(np.log10(mmax) + 0.5, i, f"{np.log10(mmax):.0f}", ha="left", fontsize=7)
ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=9)
ax.set_xlabel(r"$\log_{10}(m / eV)$")
ax.set_title("DM candidate mass ranges (53 orders of magnitude)", fontsize=12)
ax.grid(True, alpha=0.3, axis="x")
ax.invert_yaxis()

# Panel 3: Power spectrum
ax = axes[1, 0]
k = np.array(power["k_h_per_Mpc"])
P = np.array(power["P_k"])
ax.loglog(k, P, "-", color="#4c72b0", linewidth=2)
ax.axvline(power["k_eq"], color="red", linestyle="--", linewidth=1,
           label=f"k_eq = {power['k_eq']} h/Mpc")
ax.axvline(1.0 / 8.0, color="green", linestyle=":", linewidth=1,
           label="k = 1/(8 Mpc/h) (σ_8 scale)")
ax.set_xlabel("k (h/Mpc)")
ax.set_ylabel("P(k) (Mpc/h)³")
ax.set_title(f"Matter power spectrum (n_s={power['n_s']}, σ_8={power['sigma_8']})",
             fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")

# Panel 4: S_8 tension
ax = axes[1, 1]
labels = [r["survey"] for r in s8["surveys"]]
vals = [r["S_8"] for r in s8["surveys"]]
errs = [r["sigma"] for r in s8["surveys"]]
colors_s8 = ["#c44e52", "#4c72b0", "#4c72b0", "#4c72b0"]
ax.errorbar(vals, range(len(labels)), xerr=errs, fmt="o", capsize=5,
            markersize=10, color="black")
for i, (v, e, c) in enumerate(zip(vals, errs, colors_s8)):
    ax.scatter(v, i, s=200, color=c, edgecolor="black", zorder=3)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=9)
ax.axvline(np.mean([0.766, 0.776, 0.776]), color="blue", linestyle="--", linewidth=1,
           label=f"weak lensing avg ({s8['tension_sigma']:.2f}σ tension)")
ax.set_xlabel("S_8 = σ_8 √(Ω_m / 0.3)")
ax.set_title(f"S_8 tension: Planck vs weak lensing ({s8['tension_sigma']:.2f}σ)",
             fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis="x")
ax.invert_yaxis()

fig.suptitle("Phase 129: Dark Matter + Structure Formation + S_8 Tension + K_DM",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "dark_matter_S8.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 129,
    "title": "Dark matter + structure formation + S_8 tension + K_DM",
    "tier1_id": 19,
    "tier1_name": "Cosmology",
    "block": "A (Physics/Math) — paper 3/9, phase 3/8",
    "rotation_curve": {
        "v_solar_total_kms": rot["v_solar_kms"],
        "v_solar_visible_kms": rot["v_visible_solar_kms"],
        "DM_contribution_kms": rot["v_solar_kms"] - rot["v_visible_solar_kms"],
    },
    "dm_candidates": dm,
    "power_spectrum": {
        "n_s": power["n_s"],
        "k_eq_h_Mpc": power["k_eq"],
        "sigma_8": power["sigma_8"],
    },
    "s8_tension": s8,
    "linear_growth": {
        "Omega_m": 0.315, "Omega_L": 0.685,
        "D_at_a_0p001": growth["D"][0],
        "D_at_a_1": growth["D"][-1],
    },
    "verdict": ("Dark matter is required by 5σ-level observations (rotation curves, "
                "Bullet cluster, CMB peaks); ITU K_DM hypothesis encompasses WIMP/axion/PBH "
                "candidates; S_8 tension (2.5-3σ) may signal K_DM dynamical correction beyond ΛCDM."),
}

json_path = "dark_matter_S8_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 129 complete: DM evidence + K_DM hypothesis + S_8 tension;")
print(f"  Tension Planck vs weak lensing avg: {s8['tension_sigma']:.2f}σ.")
print("=" * 70)
