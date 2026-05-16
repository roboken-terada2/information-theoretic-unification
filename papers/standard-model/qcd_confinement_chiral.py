# Phase 138: QCD + Confinement + QGP + Chiral SSB + Strong CP in ITU
# Tier 1 #20 Standard Model (Block A paper 4/9, phase 4/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 138: QCD + Confinement + QGP + Chiral SSB + Strong CP")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: Cornell potential (confinement)
#   V(r) = -α_eff/r + σ × r
# ----------------------------------------------------------------------
def test1_cornell_potential():
    print("[Test 1] Cornell confinement potential V(r)")
    alpha_eff = 0.3   # short-distance coupling
    sigma = 1.0       # string tension in GeV/fm
    r = np.linspace(0.05, 3.0, 200)  # in fm
    V_coulomb = -alpha_eff / r
    V_linear = sigma * r
    V_total = V_coulomb + V_linear

    # String breaking distance (qq̄ → 2 (qq̄))
    # When E_string = 2 m_proton ≈ 1876 MeV ≈ 1.88 GeV
    E_break = 2 * 0.938  # GeV
    r_break = (E_break + alpha_eff / 0.5) / sigma   # rough estimate
    print(f"  α_eff = {alpha_eff}, σ = {sigma} GeV/fm")
    print(f"  V(0.1 fm) = {-alpha_eff/0.1 + sigma*0.1:.3f} GeV  (Coulomb dominated)")
    print(f"  V(1.0 fm) = {-alpha_eff/1.0 + sigma*1.0:.3f} GeV  (linear dominated)")
    print(f"  V(2.0 fm) = {-alpha_eff/2.0 + sigma*2.0:.3f} GeV  (string regime)")
    print(f"  String breaking (E = 2 m_p): r ≈ {r_break:.2f} fm")
    return {"r_fm": r.tolist(), "V_total": V_total.tolist(),
            "V_coulomb": V_coulomb.tolist(), "V_linear": V_linear.tolist(),
            "alpha_eff": alpha_eff, "sigma_GeV_per_fm": sigma,
            "r_break_fm": float(r_break)}


# ----------------------------------------------------------------------
# Test 2: QCD running α_s(μ) (re-visited from Phase 135)
# ----------------------------------------------------------------------
def test2_running_alpha_s():
    print("\n[Test 2] QCD running α_s(μ) (Phase 135 review)")
    Lambda_QCD = 0.200   # GeV
    N_c, N_f = 3, 5
    b_0 = (11 * N_c - 2 * N_f) / 3.0

    mu_arr = np.logspace(-0.5, 4, 200)   # 0.3 GeV to 10 TeV
    alpha_s_arr = (4 * np.pi) / (b_0 * np.log((mu_arr / Lambda_QCD)**2))
    # Filter unphysical (when ln < 0)
    alpha_s_arr = np.where(mu_arr > Lambda_QCD, alpha_s_arr, np.nan)

    samples = [0.5, 1.0, 5.0, 91.188, 1000.0]
    print(f"  Λ_QCD = {Lambda_QCD} GeV, b_0 = {b_0:.3f}")
    print(f"  {'μ (GeV)':>10}  {'α_s(μ)':>10}  {'regime'}")
    for mu in samples:
        a = (4 * np.pi) / (b_0 * np.log((mu / Lambda_QCD)**2))
        regime = "non-perturbative" if a > 0.5 else "perturbative" if a < 0.2 else "intermediate"
        print(f"  {mu:>10.3f}  {a:>10.4f}  {regime}")
    return {"mu_arr": mu_arr.tolist(), "alpha_s_arr": alpha_s_arr.tolist(),
            "Lambda_QCD": Lambda_QCD, "b_0": float(b_0)}


# ----------------------------------------------------------------------
# Test 3: Proton mass decomposition (chiral SSB)
# ----------------------------------------------------------------------
def test3_proton_mass_decomp():
    print("\n[Test 3] Proton mass decomposition (chiral SSB → ~98% QCD)")
    m_p = 938.272   # MeV
    m_u = 2.16      # MeV (bare)
    m_d = 4.67      # MeV (bare)
    # Proton = uud, so 2 m_u + m_d
    bare_mass = 2 * m_u + m_d
    qcd_contribution = m_p - bare_mass
    bare_fraction = bare_mass / m_p * 100
    qcd_fraction = qcd_contribution / m_p * 100

    print(f"  m_p (proton)                      = {m_p:.2f} MeV")
    print(f"  Bare quarks (2 m_u + m_d)         = {bare_mass:.2f} MeV ({bare_fraction:.2f}%)")
    print(f"  QCD contribution (chiral SSB, etc) = {qcd_contribution:.2f} MeV ({qcd_fraction:.2f}%)")
    print(f"\n  → 98% of proton mass = QCD chiral SSB (gluons, condensate)")
    print(f"  → Mass of ordinary matter dominantly from QCD non-perturbative effects")
    return {"m_p_MeV": m_p, "bare_quark_mass_MeV": bare_mass,
            "qcd_contribution_MeV": qcd_contribution,
            "bare_fraction_pct": bare_fraction,
            "qcd_fraction_pct": qcd_fraction}


# ----------------------------------------------------------------------
# Test 4: QCD phase transition (T_c ≈ 155 MeV lattice)
# ----------------------------------------------------------------------
def test4_qcd_phase_transition():
    print("\n[Test 4] QCD phase transition: hadron → QGP at T_c ≈ 155 MeV")
    T_c = 155.0   # MeV
    T_arr = np.linspace(10, 400, 100)
    # Sigmoid-like transition for chiral condensate
    chiral_cond = 1 / (1 + np.exp((T_arr - T_c) / 10))
    # Step-like deconfinement (Polyakov loop)
    polyakov = 1 / (1 + np.exp(-(T_arr - T_c) / 15))

    print(f"  T_c (lattice, BMW/HotQCD): {T_c} MeV")
    print(f"  Order: crossover (mu_B = 0, lattice)")
    print(f"  At T = 0 (CMB-like): chiral broken, confined (hadron phase)")
    print(f"  At T > 200 MeV: chiral restored, deconfined (QGP)")
    print()
    print(f"  Cosmic timeline: QCD transition at t ≈ 10⁻⁵ s, after EW (10⁻¹¹ s)")
    print(f"  → All baryons formed after QCD transition")
    return {"T_arr_MeV": T_arr.tolist(),
            "chiral_condensate_normalized": chiral_cond.tolist(),
            "polyakov_loop_normalized": polyakov.tolist(),
            "T_c_MeV": T_c}


# ----------------------------------------------------------------------
# Test 5: Strong CP problem
# ----------------------------------------------------------------------
def test5_strong_cp():
    print("\n[Test 5] Strong CP problem: θ_QCD < 10⁻¹⁰ from neutron EDM")
    # Neutron EDM upper limit (PSI 2020)
    d_n_limit = 1.8e-26   # e·cm
    # d_n ≈ 1e-16 × θ (e·cm) for QCD CP violation
    theta_qcd_limit = d_n_limit / 1e-16

    print(f"  Neutron EDM upper limit (PSI 2020): |d_n| < {d_n_limit:.2e} e·cm")
    print(f"  QCD relation: d_n ≈ 10⁻¹⁶ × θ_QCD (e·cm)")
    print(f"  Implied θ_QCD upper limit: {theta_qcd_limit:.2e}")
    print(f"\n  Natural θ_QCD: O(1) (no symmetry forbids it)")
    print(f"  Observed θ_QCD: < {theta_qcd_limit:.2e}")
    print(f"  Fine-tuning: {1.0/theta_qcd_limit:.2e}-fold ★ 10 orders of magnitude")
    print()
    print(f"  Peccei-Quinn solution: Promote θ to dynamical axion field")
    print(f"  Axion mass: m_a ~ 10⁻⁶ - 10⁻³ eV → dark matter candidate (ADMX, IAXO)")
    return {"d_n_limit_ecm": d_n_limit,
            "theta_QCD_limit": float(theta_qcd_limit),
            "fine_tuning_orders": -np.log10(theta_qcd_limit)}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
cornell = test1_cornell_potential()
running = test2_running_alpha_s()
mass_dec = test3_proton_mass_decomp()
qgp = test4_qcd_phase_transition()
cp = test5_strong_cp()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Cornell potential
ax = axes[0, 0]
r = np.array(cornell["r_fm"])
ax.plot(r, cornell["V_coulomb"], "--", color="#dd8452", linewidth=1.5, label=r"$-\alpha/r$ (Coulomb)")
ax.plot(r, cornell["V_linear"], "--", color="#55a467", linewidth=1.5, label=r"$\sigma r$ (linear)")
ax.plot(r, cornell["V_total"], "-", color="#4c72b0", linewidth=2, label="V_total")
ax.axvline(cornell["r_break_fm"], color="red", linestyle=":", linewidth=1,
           label=f"string breaking ~{cornell['r_break_fm']:.2f} fm")
ax.axhline(0, color="gray", linewidth=0.5)
ax.set_xlabel("r (fm)")
ax.set_ylabel("V(r) (GeV)")
ax.set_title(f"Cornell potential (σ = {cornell['sigma_GeV_per_fm']} GeV/fm)", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(-3, 5)

# Panel 2: Running α_s
ax = axes[0, 1]
mu = np.array(running["mu_arr"])
alpha_s = np.array(running["alpha_s_arr"])
ax.semilogx(mu, alpha_s, "-", color="#4c72b0", linewidth=2)
ax.axhline(0.118, color="red", linestyle="--", linewidth=1, label="α_s(M_Z) = 0.118")
ax.axhline(0.5, color="orange", linestyle=":", linewidth=1, label="Non-perturbative boundary")
ax.axvline(running["Lambda_QCD"], color="gray", linestyle=":", linewidth=1,
           label=f"Λ_QCD = {running['Lambda_QCD']} GeV")
ax.set_xlabel("μ (GeV)")
ax.set_ylabel("α_s(μ)")
ax.set_title("QCD asymptotic freedom + confinement scale", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")
ax.set_ylim(0, 1.5)

# Panel 3: Proton mass decomposition
ax = axes[1, 0]
labels = ["Bare quark mass\n(2m_u + m_d)", "QCD chiral SSB\n(gluons, condensate)"]
values = [mass_dec["bare_quark_mass_MeV"], mass_dec["qcd_contribution_MeV"]]
colors_pm = ["#dd8452", "#4c72b0"]
ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors_pm,
       textprops={"fontsize": 11})
ax.set_title(f"Proton mass {mass_dec['m_p_MeV']} MeV decomposition\n(QCD chiral SSB = ~98%)",
             fontsize=11)

# Panel 4: QCD phase transition + Strong CP
ax = axes[1, 1]
T = np.array(qgp["T_arr_MeV"])
ax.plot(T, qgp["chiral_condensate_normalized"], "-", color="#4c72b0", linewidth=2,
        label="⟨q̄q⟩ / ⟨q̄q⟩₀ (chiral condensate)")
ax.plot(T, qgp["polyakov_loop_normalized"], "-", color="#c44e52", linewidth=2,
        label="L (Polyakov loop, deconfinement)")
ax.axvline(qgp["T_c_MeV"], color="orange", linestyle="--", linewidth=1.5,
           label=f"T_c = {qgp['T_c_MeV']} MeV")
ax.set_xlabel("T (MeV)")
ax.set_ylabel("Order parameter")
ax.set_title("QCD phase transition: hadron ↔ QGP", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.10)

fig.suptitle("Phase 138: QCD + Confinement + QGP + Chiral SSB + Strong CP",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "qcd_confinement_chiral.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 138,
    "title": "QCD + Confinement + QGP + Chiral SSB + Strong CP",
    "tier1_id": 20,
    "tier1_name": "Standard Model",
    "block": "A (Physics/Math) — paper 4/9, phase 4/8",
    "cornell_potential": cornell,
    "running_alpha_s": running,
    "proton_mass_decomposition": mass_dec,
    "qcd_phase_transition": qgp,
    "strong_cp": cp,
    "verdict": ("QCD = K_QCD strong K-flow with IR confinement (linear potential), "
                "UV asymptotic freedom (Phase 135). Chiral SSB explains 98% of proton mass. "
                "QGP at T > 155 MeV. Strong CP problem: θ < 10⁻¹⁰ (10-order fine-tuning); "
                "Peccei-Quinn axion = solution + DM candidate."),
}

json_path = "qcd_confinement_chiral_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 138 complete: QCD non-perturbative regime = K_QCD complexity;")
print(f"  Proton mass 98% from chiral SSB; θ_QCD < 10⁻¹⁰ fine-tuning")
print("=" * 70)
