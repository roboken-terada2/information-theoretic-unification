# Phase 136: SM fermion content + 3 generations + Yukawa + CKM/PMNS + K_fermion
# Tier 1 #20 Standard Model (Block A paper 4/9, phase 2/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 136: SM Fermion Content + 3 Generations + Yukawa + CKM/PMNS")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: 3 generations of fermions (PDG 2024)
# ----------------------------------------------------------------------
def test1_three_generations():
    print("[Test 1] 3 generations of SM fermions (PDG 2024)")
    fermions = [
        # (name, type, generation, charge, mass_GeV, mass_unit)
        # Generation 1
        ("up (u)",       "quark",    1, "+2/3", 2.16e-3),
        ("down (d)",     "quark",    1, "-1/3", 4.67e-3),
        ("electron (e)", "lepton",   1, "-1",   5.11e-4),
        ("nu_e",         "neutrino", 1, "0",    1e-9),
        # Generation 2
        ("charm (c)",    "quark",    2, "+2/3", 1.27),
        ("strange (s)",  "quark",    2, "-1/3", 9.3e-2),
        ("muon (μ)",     "lepton",   2, "-1",   0.10566),
        ("nu_mu",        "neutrino", 2, "0",    1e-9),
        # Generation 3
        ("top (t)",      "quark",    3, "+2/3", 172.5),
        ("bottom (b)",   "quark",    3, "-1/3", 4.18),
        ("tau (τ)",      "lepton",   3, "-1",   1.77686),
        ("nu_tau",       "neutrino", 3, "0",    1e-9),
    ]
    print(f"  {'Particle':<14}  {'Type':<10}  {'Gen':>4}  {'Q':>6}  {'Mass (GeV)':>14}")
    rows = []
    for name, t, g, q, m in fermions:
        print(f"  {name:<14}  {t:<10}  {g:>4d}  {q:>6}  {m:>14.4e}")
        rows.append({"name": name, "type": t, "generation": g, "charge": q, "mass_GeV": m})

    m_t = 172.5
    m_e = 5.11e-4
    m_nu = 1e-9
    print(f"\n  Mass hierarchy:")
    print(f"    m_t / m_e   = {m_t/m_e:.4e}  (~ 10^5 within charged)")
    print(f"    m_t / m_nu  = {m_t/m_nu:.4e}  (~ 10^{{11}} if ν~1 eV)")
    return {"fermions": rows,
            "m_t_over_m_e": m_t / m_e,
            "m_t_over_m_nu": m_t / m_nu}


# ----------------------------------------------------------------------
# Test 2: Yukawa couplings y_f = m_f √2 / v
# ----------------------------------------------------------------------
def test2_yukawa_couplings():
    print("\n[Test 2] Yukawa couplings y_f = m_f √2 / v  (v = 246 GeV)")
    v_higgs = 246.22  # GeV (Higgs VEV)
    masses = [
        ("electron", 5.11e-4),
        ("up",       2.16e-3),
        ("down",     4.67e-3),
        ("strange",  9.3e-2),
        ("charm",    1.27),
        ("muon",     0.10566),
        ("bottom",   4.18),
        ("tau",      1.77686),
        ("top",      172.5),
    ]
    print(f"  v (Higgs VEV) = {v_higgs} GeV")
    print(f"  {'Fermion':<12}  {'m (GeV)':>14}  {'y_f = m √2 / v':>16}")
    rows = []
    for name, m in masses:
        y = m * np.sqrt(2) / v_higgs
        print(f"  {name:<12}  {m:>14.4e}  {y:>16.4e}")
        rows.append({"fermion": name, "mass_GeV": m, "yukawa": float(y)})

    print(f"\n  Top quark Yukawa ≈ 1 (O(1))")
    print(f"  Other fermion Yukawas << 1 (5+ orders of magnitude hierarchy)")
    return rows


# ----------------------------------------------------------------------
# Test 3: CKM matrix (Wolfenstein parameterization)
# ----------------------------------------------------------------------
def test3_ckm_matrix():
    print("\n[Test 3] CKM matrix (Wolfenstein parameterization, PDG 2024)")
    lam = 0.22500
    A_param = 0.832
    rho_bar = 0.159
    eta_bar = 0.348

    # Wolfenstein to standard form
    V_ud = 1 - lam**2 / 2
    V_us = lam
    V_ub = A_param * lam**3 * (rho_bar - 1j*eta_bar)
    V_cd = -lam
    V_cs = 1 - lam**2 / 2
    V_cb = A_param * lam**2
    V_td = A_param * lam**3 * (1 - rho_bar - 1j*eta_bar)
    V_ts = -A_param * lam**2
    V_tb = 1.0

    V_CKM = np.array([
        [V_ud, V_us, V_ub],
        [V_cd, V_cs, V_cb],
        [V_td, V_ts, V_tb]
    ])

    print(f"  Wolfenstein params: λ = {lam}, A = {A_param}, ρ̄ = {rho_bar}, η̄ = {eta_bar}")
    print(f"  |V_CKM|:")
    for i, row in enumerate(np.abs(V_CKM)):
        print(f"    [{row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}]")

    # Cabibbo angle
    theta_C = np.degrees(np.arcsin(lam))
    print(f"\n  Cabibbo angle (sin θ_C = λ): θ_C ≈ {theta_C:.2f}°")

    # Unitarity check
    unitarity = np.abs(V_CKM @ V_CKM.conj().T - np.eye(3)).max()
    print(f"  Unitarity (|V V† - I|_max): {unitarity:.4e}")

    return {"lambda_wolf": lam, "A_wolf": A_param, "rho_bar": rho_bar, "eta_bar": eta_bar,
            "Cabibbo_angle_deg": float(theta_C),
            "V_CKM_abs": np.abs(V_CKM).tolist(),
            "unitarity_max_dev": float(unitarity)}


# ----------------------------------------------------------------------
# Test 4: PMNS matrix angles (NuFIT 2024)
# ----------------------------------------------------------------------
def test4_pmns():
    print("\n[Test 4] PMNS matrix angles (NuFIT 2024)")
    theta_12 = 33.41   # solar
    theta_23 = 49.1    # atmospheric
    theta_13 = 8.54    # reactor

    s12, c12 = np.sin(np.radians(theta_12)), np.cos(np.radians(theta_12))
    s23, c23 = np.sin(np.radians(theta_23)), np.cos(np.radians(theta_23))
    s13, c13 = np.sin(np.radians(theta_13)), np.cos(np.radians(theta_13))

    U23 = np.array([[1,0,0],[0,c23,s23],[0,-s23,c23]])
    U13 = np.array([[c13,0,s13],[0,1,0],[-s13,0,c13]])
    U12 = np.array([[c12,s12,0],[-s12,c12,0],[0,0,1]])
    V_PMNS = U23 @ U13 @ U12

    print(f"  θ_12 (solar)         = {theta_12}°")
    print(f"  θ_23 (atmospheric)   = {theta_23}°")
    print(f"  θ_13 (reactor)       = {theta_13}°")
    print(f"\n  |V_PMNS|:")
    for row in np.abs(V_PMNS):
        print(f"    [{row[0]:.4f}  {row[1]:.4f}  {row[2]:.4f}]")

    print(f"\n  Comparison: CKM θ_max ≈ 13° (Cabibbo) vs PMNS θ_max ≈ 49° (atmos)")
    print(f"  → PMNS has much larger mixing than CKM")

    # Δm² values
    dm2_21 = 7.41e-5   # eV^2
    dm2_31 = 2.51e-3   # eV^2
    print(f"\n  Δm²_21 = {dm2_21} eV²  (solar)")
    print(f"  |Δm²_31| = {dm2_31} eV²  (atmospheric)")
    return {"theta_12_deg": theta_12, "theta_23_deg": theta_23, "theta_13_deg": theta_13,
            "V_PMNS_abs": np.abs(V_PMNS).tolist(),
            "dm2_21_eV2": dm2_21, "dm2_31_eV2": dm2_31}


# ----------------------------------------------------------------------
# Test 5: Number of light neutrino flavors (LEP)
# ----------------------------------------------------------------------
def test5_neutrino_flavors():
    print("\n[Test 5] Number of light neutrino flavors (LEP precision)")
    N_nu_measured = 2.9963
    N_nu_err = 0.0074
    print(f"  N_ν (LEP 1989-2000): {N_nu_measured} ± {N_nu_err}")
    print(f"  = exactly 3 generations (within 0.5%)")
    print(f"  → SM fermion content fixed at 3 generations")

    # ITU view: anomaly cancellation
    print(f"\n  ITU: anomaly cancellation Σ Y³ = 0 (Q-quark + Q-lepton)")
    Y_quark_left = 1/3
    Y_quark_right_up = 4/3
    Y_quark_right_down = -2/3
    Y_lepton_left = -1
    Y_lepton_right = -2

    # SU(2)^2 U(1) anomaly
    n_gen = 3
    anomaly_SU2sq_U1 = n_gen * (3 * Y_quark_left + Y_lepton_left)  # × N_color × n_doublet
    # 簡略: actually 各世代で sum_doublets Y = 3*(1/3) + (-1) = 0 per generation
    sum_per_gen = 3 * Y_quark_left + Y_lepton_left
    print(f"  Per-generation Σ Y (SU(2)² U(1)) = 3×(1/3) + (-1) = {sum_per_gen}")
    print(f"  → Anomaly cancellation automatic per generation")
    return {"N_nu_LEP": N_nu_measured, "N_nu_err": N_nu_err,
            "anomaly_per_gen": float(sum_per_gen)}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
gens = test1_three_generations()
yukawas = test2_yukawa_couplings()
ckm = test3_ckm_matrix()
pmns = test4_pmns()
neutrinos = test5_neutrino_flavors()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Mass hierarchy (log scale)
ax = axes[0, 0]
fermion_names = [f["name"] for f in gens["fermions"]]
masses = [f["mass_GeV"] for f in gens["fermions"]]
gens_color = ["#4c72b0", "#dd8452", "#c44e52"]
colors = []
for f in gens["fermions"]:
    colors.append(gens_color[f["generation"] - 1])
ax.barh(fermion_names, masses, color=colors)
for i, (m, name) in enumerate(zip(masses, fermion_names)):
    ax.text(m * 1.5, i, f"{m:.2e}", va="center", fontsize=7)
ax.set_xscale("log")
ax.set_xlabel("Mass (GeV)")
ax.set_title("3 generations SM fermion masses (11 orders!)", fontsize=12)
ax.grid(True, alpha=0.3, which="both", axis="x")
ax.invert_yaxis()

# Panel 2: Yukawa couplings
ax = axes[0, 1]
y_names = [y["fermion"] for y in yukawas]
y_vals = [y["yukawa"] for y in yukawas]
ax.barh(y_names, y_vals, color="#4c72b0")
for i, v in enumerate(y_vals):
    ax.text(v * 1.5, i, f"{v:.2e}", va="center", fontsize=8)
ax.set_xscale("log")
ax.set_xlabel(r"$y_f$ (Yukawa coupling)")
ax.axvline(1.0, color="red", linestyle="--", linewidth=1, label="O(1)")
ax.set_title("Yukawa couplings: top ≈ 1, others << 1", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, which="both", axis="x")
ax.invert_yaxis()

# Panel 3: CKM vs PMNS matrices
ax = axes[1, 0]
im = ax.imshow(np.log10(np.array(ckm["V_CKM_abs"]) + 1e-6), cmap="viridis", aspect="auto")
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["d", "s", "b"])
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(["u", "c", "t"])
for i in range(3):
    for j in range(3):
        v = ckm["V_CKM_abs"][i][j]
        ax.text(j, i, f"{v:.4f}", ha="center", va="center", color="white", fontsize=9)
plt.colorbar(im, ax=ax, label=r"$\log_{10}|V|$")
ax.set_title(f"CKM matrix (Cabibbo θ_C = {ckm['Cabibbo_angle_deg']:.1f}°)", fontsize=12)

# Panel 4: PMNS matrix
ax = axes[1, 1]
im = ax.imshow(np.array(pmns["V_PMNS_abs"]), cmap="viridis", aspect="auto", vmin=0, vmax=1)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels([r"$\nu_1$", r"$\nu_2$", r"$\nu_3$"])
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(["e", "μ", "τ"])
for i in range(3):
    for j in range(3):
        v = pmns["V_PMNS_abs"][i][j]
        ax.text(j, i, f"{v:.3f}", ha="center", va="center", color="white", fontsize=10)
plt.colorbar(im, ax=ax, label="|U|")
ax.set_title(f"PMNS matrix (θ_12={pmns['theta_12_deg']}°, θ_23={pmns['theta_23_deg']}°, θ_13={pmns['theta_13_deg']}°)",
             fontsize=11)

fig.suptitle("Phase 136: SM Fermion Content + 3 Generations + Yukawa + CKM/PMNS",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "fermion_3gen_yukawa.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 136,
    "title": "SM fermion 3 generations + Yukawa + CKM/PMNS in ITU",
    "tier1_id": 20,
    "tier1_name": "Standard Model",
    "block": "A (Physics/Math) — paper 4/9, phase 2/8",
    "three_generations": gens,
    "yukawa_couplings": yukawas,
    "ckm_matrix": ckm,
    "pmns_matrix": pmns,
    "neutrino_flavors_LEP": neutrinos,
    "verdict": ("SM 3-generation fermion structure with 11-order mass hierarchy, "
                "top Yukawa ≈ 1, others << 1. CKM Cabibbo ≈ 13°, PMNS angles much "
                "larger (33°/49°/9°). N_ν = 3 fixed by LEP. ITU: K_fermion 3-fold "
                "repetition + anomaly cancellation per generation."),
}

json_path = "fermion_3gen_yukawa_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 136 complete: 3-gen fermions + Yukawa hierarchy + CKM/PMNS;")
print(f"  N_ν = 3 (LEP); top y = 1, e y = 3e-6 (5 orders)")
print("=" * 70)
