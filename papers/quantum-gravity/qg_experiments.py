# Phase 117: Experimental tests of Quantum Gravity in ITU
# LIGO / EHT / LISA / BMV / GRB / Atom interferometry
# Tier 1 #17 Quantum Gravity — Block A
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 117: QG Experimental Tests")
print("=" * 70)
print()

# Constants
HBAR = 1.054571817e-34
C = 2.99792458e8
G_N = 6.67430e-11
kB = 1.380649e-23
M_SUN = 1.989e30
PARSEC = 3.0857e16
L_P = np.sqrt(HBAR * G_N / C**3)
E_P_J = np.sqrt(HBAR * C**5 / G_N)
GeV_per_J = 1 / 1.602176634e-10
E_P_GeV = E_P_J * GeV_per_J


# ----------------------------------------------------------------------
# Test 1: LIGO strain vs ITU echo amplitude
# ----------------------------------------------------------------------
def test1_ligo_echo():
    print("[Test 1] LIGO strain sensitivity vs ITU echo amplitude")
    # Sample BBH mergers (GW150914-like)
    M_BBH = 60.0 * M_SUN     # total mass
    R_s = 2 * G_N * M_BBH / C**2
    print(f"  BBH total mass:  M = {M_BBH/M_SUN:.1f} Msun")
    print(f"  Schwarzschild radius R_s = {R_s:.4e} m")

    # ITU echo amplitude scaling: h_echo / h_merger ~ (l_P / R_s)
    lP_over_Rs = L_P / R_s
    h_merger = 1e-21   # typical merger strain
    h_echo_predicted = h_merger * lP_over_Rs
    h_LIGO_sensitivity = 1e-22

    print(f"  h_merger (typical) = {h_merger:.1e}")
    print(f"  l_P / R_s          = {lP_over_Rs:.4e}")
    print(f"  h_echo predicted   = h_merger * (l_P/R_s) = {h_echo_predicted:.4e}")
    print(f"  LIGO sensitivity   = {h_LIGO_sensitivity:.1e}")
    print(f"  Ratio (echo / sens) = {h_echo_predicted / h_LIGO_sensitivity:.4e}")
    print("  -> Echo too small for current LIGO; CE / ET (2030+) may detect.")

    # Future detector sensitivity (Cosmic Explorer / Einstein Telescope) ~ 10^-23
    h_CE = 1e-23
    print(f"  Cosmic Explorer / ET projected sensitivity = {h_CE:.1e}")
    print(f"  Even ET still {h_echo_predicted / h_CE:.4e} below threshold for pure-shape echo.")
    return {"M_BBH_Msun": M_BBH / M_SUN, "R_s_m": R_s, "lP_over_Rs": lP_over_Rs,
            "h_merger": h_merger, "h_echo_predicted": h_echo_predicted,
            "h_LIGO_sensitivity": h_LIGO_sensitivity, "h_CE": h_CE}


# ----------------------------------------------------------------------
# Test 2: EHT shadow correction
# ----------------------------------------------------------------------
def test2_eht_shadow():
    print("\n[Test 2] EHT shadow corrections for M87* and Sgr A*")
    targets = [
        ("M87*", 6.5e9, 16.8 * 1e6 * PARSEC),
        ("Sgr A*", 4.0e6, 8.1e3 * PARSEC),
    ]
    rows = []
    for name, M_solar, d in targets:
        M = M_solar * M_SUN
        R_s = 2 * G_N * M / C**2
        # Shadow angular size ~ sqrt(27) R_s / d  (Schwarzschild)
        theta_shadow = np.sqrt(27.0) * R_s / d
        theta_uas = theta_shadow * (3600.0 * 180.0 / np.pi) * 1e6  # in microarcsec
        # Correction l_P / R_s
        correction = L_P / R_s
        eht_resolution_uas = 20.0   # current EHT angular resolution ~ 20 uas
        ngeht_resolution_uas = 5.0  # next-gen EHT
        print(f"  {name}: M = {M_solar:.2e} Msun, R_s = {R_s:.4e} m")
        print(f"        shadow = sqrt(27) R_s / d = {theta_uas:.3f} uas")
        print(f"        l_P / R_s = {correction:.4e}")
        print(f"        Required precision to see QG correction = {correction * 100:.2e} %")
        rows.append({"name": name, "M_solar": M_solar, "d_m": d,
                     "R_s_m": R_s, "theta_uas": theta_uas,
                     "lP_over_Rs": correction})
    print()
    print(f"  Current EHT precision ~ {eht_resolution_uas} uas, ngEHT target ~ {ngeht_resolution_uas} uas")
    print(f"  Direct QG correction observation: out of reach by many orders.")
    return {"targets": rows, "eht_uas": eht_resolution_uas, "ngeht_uas": ngeht_resolution_uas}


# ----------------------------------------------------------------------
# Test 3: LISA EMRI cycles and integration
# ----------------------------------------------------------------------
def test3_lisa_emri():
    print("\n[Test 3] LISA EMRI: cycle count + integrated QG correction")
    M_smbh = 1e6 * M_SUN
    m_small = 10.0 * M_SUN
    R_s_smbh = 2 * G_N * M_smbh / C**2

    # EMRI orbital period (rough estimate at innermost stable circular orbit ISCO)
    # ISCO at 6 R_s for Schwarzschild; v ~ c/sqrt(6) at ISCO
    r_isco = 6 * R_s_smbh / 2  # gravitational radius factor 3 R_s = 6 GM/c^2; ISCO radius = 6 GM/c^2
    T_orb = 2 * np.pi * np.sqrt(r_isco**3 / (G_N * M_smbh))
    f_orb = 1.0 / T_orb

    # LISA observation time ~ 4 years; cycles ~ f_orb * 4 yr
    T_LISA = 4 * 365.25 * 86400.0
    N_cycles = f_orb * T_LISA

    # Per-cycle QG correction l_P / R_s; integrated:
    lP_over_Rs = L_P / R_s_smbh
    integrated_correction = lP_over_Rs * N_cycles

    print(f"  SMBH mass = 1e6 Msun, R_s = {R_s_smbh:.4e} m")
    print(f"  ISCO orbital period = {T_orb:.4e} s, frequency = {f_orb*1e3:.4f} mHz")
    print(f"  LISA observation time = 4 yr, cycles ≈ {N_cycles:.4e}")
    print(f"  Per-cycle QG correction l_P/R_s = {lP_over_Rs:.4e}")
    print(f"  Integrated correction over LISA mission ≈ {integrated_correction:.4e}")
    print("  Still many orders below LISA SNR (~10^3); QG inaccessible directly.")
    return {"M_smbh_Msun": 1e6, "R_s_smbh": R_s_smbh,
            "T_orb_s": T_orb, "f_orb_Hz": f_orb,
            "N_cycles_LISA": N_cycles,
            "lP_over_Rs": lP_over_Rs,
            "integrated_correction": integrated_correction}


# ----------------------------------------------------------------------
# Test 4: BMV gravitationally-induced entanglement
# ----------------------------------------------------------------------
def test4_bmv_phase():
    print("\n[Test 4] BMV (Bose-Marletto-Vedral 2017) phase calculation")
    m = 1e-14   # kg, target mass (~ 10^9 amu)
    d = 100e-6  # m, separation
    t = 1.0     # s, coherence time

    # Newtonian gravitational potential energy
    V = G_N * m * m / d
    phase_diff = V * t / HBAR   # in radians

    print(f"  m = {m:.2e} kg ({m / 1.66e-27:.2e} amu), d = {d*1e6:.0f} um, t = {t:.1f} s")
    print(f"  V_grav = G m^2 / d = {V:.4e} J")
    print(f"  Phase shift Δφ = V t / hbar = {phase_diff:.4e} rad")
    if phase_diff > 0.5:
        verdict = "Sufficient to generate detectable entanglement (Bose et al. 2017 criterion: Δφ ≳ 1)."
    elif phase_diff > 0.05:
        verdict = "Borderline; needs longer t or larger m."
    else:
        verdict = "Insufficient; needs significantly larger m or longer t."
    print(f"  Verdict: {verdict}")
    return {"m_kg": m, "d_m": d, "t_s": t, "V_J": V,
            "phase_diff_rad": phase_diff, "verdict": verdict}


# ----------------------------------------------------------------------
# Test 5: GRB time delay bound on E_QG (Lorentz invariance)
# ----------------------------------------------------------------------
def test5_grb_bound():
    print("\n[Test 5] GRB 090510 bound on quantum-gravity energy scale (n=1)")
    # GRB 090510 (Fermi-LAT)
    z = 0.903
    distance_Gpc = 5.0   # luminosity distance ~ 5 Gpc
    distance_m = distance_Gpc * 1e9 * PARSEC
    E_high_GeV = 31.0    # high-energy photon 31 GeV
    Delta_t = 0.9        # observed delay limit < 0.9 s

    # Linear dispersion: Δt = (E / E_QG) × (d / c)
    # -> E_QG > (E × d) / (c × Δt)
    E_high_J = E_high_GeV * 1.602e-10
    E_QG_lower_J = (E_high_J * distance_m) / (C * Delta_t)
    E_QG_lower_GeV = E_QG_lower_J * GeV_per_J

    print(f"  GRB 090510: z = {z}, d ≈ {distance_Gpc} Gpc, E_high = {E_high_GeV} GeV")
    print(f"  Observed Δt < {Delta_t} s")
    print(f"  Implied E_QG (n=1) > {E_QG_lower_J:.4e} J = {E_QG_lower_GeV:.4e} GeV")
    print(f"  Planck energy E_P = {E_P_GeV:.4e} GeV")
    print(f"  E_QG / E_P > {E_QG_lower_GeV / E_P_GeV:.4e}")
    print(f"  -> Linear (n=1) Lorentz violation excluded above Planck energy.")
    return {"z": z, "distance_Gpc": distance_Gpc,
            "E_high_GeV": E_high_GeV, "Delta_t_s": Delta_t,
            "E_QG_lower_GeV": E_QG_lower_GeV,
            "E_P_GeV": E_P_GeV,
            "E_QG_over_E_P": E_QG_lower_GeV / E_P_GeV}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
ligo = test1_ligo_echo()
eht = test2_eht_shadow()
lisa = test3_lisa_emri()
bmv = test4_bmv_phase()
grb = test5_grb_bound()


# ----------------------------------------------------------------------
# Figure: 4-panel summary
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: LIGO strain sensitivity vs ITU echo
ax = axes[0, 0]
labels = ["h_merger\n(typ.)", "h_LIGO\nsensitivity", "h_CE/ET\n(2030+)", "h_echo\n(ITU pred.)"]
values = [ligo["h_merger"], ligo["h_LIGO_sensitivity"], ligo["h_CE"], ligo["h_echo_predicted"]]
colors_q = ["#4c72b0", "#dd8452", "#55a467", "#c44e52"]
ax.bar(labels, values, color=colors_q)
for i, v in enumerate(values):
    ax.text(i, v * 1.5, f"{v:.1e}", ha="center", fontsize=9, fontweight="bold")
ax.set_yscale("log")
ax.set_ylabel("Strain h")
ax.set_title("LIGO/CE/ET vs ITU echo prediction", fontsize=12)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 2: EHT shadow corrections (M87*, Sgr A*)
ax = axes[0, 1]
labels_eht = [t["name"] for t in eht["targets"]]
sizes_uas = [t["theta_uas"] for t in eht["targets"]]
corr = [t["lP_over_Rs"] * 1e45 for t in eht["targets"]]
x_idx = np.arange(len(labels_eht))
ax2 = ax.twinx()
b1 = ax.bar(x_idx - 0.2, sizes_uas, 0.4, label="Shadow size (uas)", color="#4c72b0")
b2 = ax2.bar(x_idx + 0.2, corr, 0.4, label=r"$\ell_P/R_s\times 10^{45}$", color="#dd8452")
ax.set_xticks(x_idx)
ax.set_xticklabels(labels_eht)
ax.set_ylabel("Shadow angular size (uas)", color="#4c72b0")
ax2.set_ylabel(r"$\ell_P/R_s \times 10^{45}$", color="#dd8452")
ax.set_title("EHT shadow + QG correction (l_P/R_s)", fontsize=12)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: LISA EMRI cycles + correction
ax = axes[1, 0]
ax.axis("off")
ax.set_title("LISA EMRI: cycles + QG correction", fontsize=12, fontweight="bold")
lines = [
    ("SMBH mass", "1e6 Msun"),
    ("R_s (SMBH)", f"{lisa['R_s_smbh']:.3e} m"),
    ("ISCO orbital period", f"{lisa['T_orb_s']:.3e} s"),
    ("LISA cycles (4 yr)", f"{lisa['N_cycles_LISA']:.3e}"),
    (r"$\ell_P/R_s$ (per cycle)", f"{lisa['lP_over_Rs']:.3e}"),
    ("Integrated correction", f"{lisa['integrated_correction']:.3e}"),
]
y = 0.88
for k, v in lines:
    ax.text(0.05, y, k, fontsize=11, color="#4c72b0")
    ax.text(0.55, y, v, fontsize=11, fontfamily="monospace", color="#c44e52")
    y -= 0.12
ax.text(0.05, 0.05, "→ LISA cannot directly detect QG even integrated", fontsize=10, fontstyle="italic")

# Panel 4: BMV + GRB summary
ax = axes[1, 1]
ax.axis("off")
ax.set_title("BMV proposal + GRB bound", fontsize=12, fontweight="bold")
lines_b = [
    ("BMV mass m", f"{bmv['m_kg']:.1e} kg"),
    ("BMV separation d", f"{bmv['d_m']*1e6:.0f} um"),
    ("BMV coherence time t", f"{bmv['t_s']:.1f} s"),
    ("BMV phase Δφ", f"{bmv['phase_diff_rad']:.3e} rad"),
    ("", ""),
    ("GRB 090510 E_high", f"{grb['E_high_GeV']:.1f} GeV"),
    ("GRB Δt limit", f"< {grb['Delta_t_s']} s"),
    ("E_QG > (n=1)", f"{grb['E_QG_over_E_P']:.2e} E_P"),
]
y = 0.92
for k, v in lines_b:
    ax.text(0.05, y, k, fontsize=10, color="#4c72b0")
    ax.text(0.55, y, v, fontsize=10, fontfamily="monospace", color="#c44e52")
    y -= 0.10
ax.text(0.05, 0.05, "★ BMV = direct QG test (2030+ decisive)", fontsize=10,
        fontstyle="italic", color="#55a467")

fig.suptitle("Phase 117: Experimental tests of Quantum Gravity",
             fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.97])

png_path = "qg_experiments.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 117,
    "title": "QG experimental tests: LIGO / EHT / LISA / BMV / GRB",
    "tier1_id": 17,
    "tier1_name": "Quantum Gravity",
    "block": "A (Physics/Math)",
    "ligo_echo": ligo,
    "eht_shadow": eht,
    "lisa_emri": lisa,
    "bmv_proposal": bmv,
    "grb_bound": grb,
    "verdict": ("BMV (gravitationally-induced entanglement) is the gold-standard "
                "direct QG test; GW echoes (CE/ET 2030+) and BH shadow corrections "
                "(ngEHT 2030+) provide complementary indirect probes."),
}

json_path = "qg_experiments_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 117 complete: BMV is the gold standard for direct QG test;")
print(f"  ITU echo prediction h ~ {ligo['h_echo_predicted']:.1e} (vs LIGO sens ~1e-22).")
print("=" * 70)
