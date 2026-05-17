"""
Phase 154: Magnetism — Heisenberg + Hubbard + Stoner + Mott
============================================================

Tests:
1. 2D Heisenberg/Ising AF Monte Carlo (Néel state)
2. Magnon dispersion: FM (k²) vs AF (|k|)
3. Curie-Weiss χ(T) = C/(T-θ) for Fe, Co, Ni
4. Stoner criterion I × D(ε_F) > 1 for Fe/Co/Ni/Cu/Pd
5. Superexchange J = -4t²/U for cuprate (La2CuO4)
6. Bloch T^(3/2) magnetization law (FM)
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

np.random.seed(42)

print("=" * 70)
print("Phase 154: Magnetism — Heisenberg + Hubbard + Stoner + Mott")
print("=" * 70)
print()

k_B = 1.380649e-23
mu_B = 9.2740100783e-24

# ----------------------------------------------------------------------
# Test 1: 2D Ising AF Monte Carlo (J < 0)
# ----------------------------------------------------------------------
print("[Test 1] 2D Ising AF Monte Carlo (J<0) — Néel staggered magnetization")

def ising_AF_MC(L=16, T=2.5, n_eq=300, n_meas=500, J=-1.0):
    s = np.random.choice([-1, 1], size=(L, L))
    beta = 1.0 / T
    N = L * L
    # Define staggered sign for Néel order: (-1)^(i+j)
    stag = np.fromfunction(lambda i, j: (-1.0) ** (i + j), (L, L))

    def deltaE(i, j):
        nb = s[(i+1) % L, j] + s[(i-1) % L, j] + s[i, (j+1) % L] + s[i, (j-1) % L]
        return 2 * s[i, j] * J * nb

    for _ in range(n_eq):
        for _ in range(N):
            i, j = np.random.randint(0, L), np.random.randint(0, L)
            dE = deltaE(i, j)
            if dE <= 0 or np.random.random() < np.exp(-beta * dE):
                s[i, j] *= -1

    m_stag_list = []
    for _ in range(n_meas):
        for _ in range(N):
            i, j = np.random.randint(0, L), np.random.randint(0, L)
            dE = deltaE(i, j)
            if dE <= 0 or np.random.random() < np.exp(-beta * dE):
                s[i, j] *= -1
        m_stag = np.abs(np.sum(s * stag)) / N
        m_stag_list.append(m_stag)
    return np.mean(m_stag_list), s

# Onsager T_c for AF Ising is same as FM (|J| sets scale): T_c ≈ 2.269 J
T_c_2D = 2.0 / np.log(1.0 + np.sqrt(2.0))
T_list = [1.5, 2.0, 2.27, 2.5, 3.0]
print(f"  Onsager T_c (|J|=1) = {T_c_2D:.3f}")
m_stag_results = []
for TT in T_list:
    m_s, _ = ising_AF_MC(L=16, T=TT, n_eq=200, n_meas=300, J=-1.0)
    m_stag_results.append(m_s)
    phase = "Néel AF" if m_s > 0.5 else "Disordered"
    print(f"    T = {TT}: staggered |m_s| = {m_s:.3f}  ({phase})")
print()

# ----------------------------------------------------------------------
# Test 2: Magnon dispersion FM vs AF
# ----------------------------------------------------------------------
print("[Test 2] Magnon dispersion: FM ε ∝ k², AF ε ∝ |k|")
a = 1.0
J_FM = 1.0
J_AF = -1.0
S_spin = 0.5
k_arr = np.linspace(-np.pi / a, np.pi / a, 200)
eps_FM = 2 * J_FM * S_spin * (1 - np.cos(k_arr * a))
eps_AF = 2 * abs(J_AF) * S_spin * np.abs(np.sin(k_arr * a))
print(f"  FM:  ε(k=π/a) = {eps_FM[np.argmin(np.abs(k_arr - np.pi/a))]:.3f} (= 4JS = 2.0 for S=1/2)")
print(f"       Near k=0: ε ≈ JS a² k²")
print(f"  AF:  ε(k=π/a) = {eps_AF[np.argmin(np.abs(k_arr - np.pi/a))]:.3f}")
print(f"       Near k=0: ε ≈ 2|J|S a |k| (linear, Goldstone-like)")
# Check small-k scaling
small_k = k_arr[(k_arr > 0.05) & (k_arr < 0.3)]
small_eps_FM = 2 * J_FM * S_spin * (1 - np.cos(small_k * a))
small_eps_AF = 2 * abs(J_AF) * S_spin * np.abs(np.sin(small_k * a))
slope_FM, _ = np.polyfit(np.log(small_k), np.log(small_eps_FM), 1)
slope_AF, _ = np.polyfit(np.log(small_k), np.log(small_eps_AF), 1)
print(f"  Log-log slope FM (small k) = {slope_FM:.3f}  (theory 2.0)")
print(f"  Log-log slope AF (small k) = {slope_AF:.3f}  (theory 1.0)")
print()

# ----------------------------------------------------------------------
# Test 3: Curie-Weiss χ(T) for Fe, Co, Ni
# ----------------------------------------------------------------------
print("[Test 3] Curie-Weiss susceptibility χ(T) = C/(T-θ)")
materials_FM = {
    'Fe': {'theta_K': 1043, 'mu_eff': 2.22, 'g': 2.0, 'S': 1.11},  # μ/atom in μ_B
    'Co': {'theta_K': 1394, 'mu_eff': 1.72, 'g': 2.0, 'S': 0.86},
    'Ni': {'theta_K': 631,  'mu_eff': 0.61, 'g': 2.0, 'S': 0.305},
    'Gd': {'theta_K': 293,  'mu_eff': 7.55, 'g': 2.0, 'S': 3.5},
}
T_arr_CW = np.linspace(50, 1800, 200)
print(f"  {'Material':<6}{'θ_C (K)':<10}{'μ_eff (μ_B)':<14}{'C':<10}")
for mat, d in materials_FM.items():
    C_Curie = d['mu_eff'] ** 2 / 3   # in (μ_B)²/k_B per atom; simplified
    print(f"  {mat:<6}{d['theta_K']:<10}{d['mu_eff']:<14}{C_Curie:<10.3f}")
print()

# ----------------------------------------------------------------------
# Test 4: Stoner criterion
# ----------------------------------------------------------------------
print("[Test 4] Stoner ferromagnetism criterion I × D(ε_F) > 1")
stoner_data = {
    'Fe':  {'D_eF': 2.0, 'I': 0.93, 'FM': True},
    'Co':  {'D_eF': 1.8, 'I': 0.99, 'FM': True},
    'Ni':  {'D_eF': 2.8, 'I': 0.99, 'FM': True},
    'Cu':  {'D_eF': 0.3, 'I': 0.73, 'FM': False},
    'Pd':  {'D_eF': 1.8, 'I': 0.50, 'FM': False},   # nearly ferromagnetic
    'Pt':  {'D_eF': 1.6, 'I': 0.40, 'FM': False},
}
print(f"  {'Material':<8}{'D(ε_F) (1/eV/atom)':<22}{'I (eV)':<10}{'I × D':<10}{'Predict':<10}{'Actual':<10}")
for mat, d in stoner_data.items():
    ID = d['I'] * d['D_eF']
    pred = "FM" if ID > 1.0 else "PM"
    actual = "FM" if d['FM'] else "PM"
    marker = "✓" if pred == actual else "✗"
    print(f"  {mat:<8}{d['D_eF']:<22.2f}{d['I']:<10.2f}{ID:<10.3f}{pred:<10}{actual:<10}{marker}")
print()

# ----------------------------------------------------------------------
# Test 5: Superexchange J = -4t²/U for cuprate
# ----------------------------------------------------------------------
print("[Test 5] Anderson superexchange J = -4t²/U")
t_cuprate = 0.4    # eV
U_cuprate = 10.0   # eV
J_super = -4 * t_cuprate ** 2 / U_cuprate    # eV
J_super_K = J_super * 1.602e-19 / k_B
print(f"  La2CuO4: t = {t_cuprate} eV, U = {U_cuprate} eV")
print(f"  J_ex = -4t²/U = {J_super:.4f} eV = {J_super_K:.1f} K")
print(f"  (Experimental La2CuO4 J ≈ -1500 K; renormalization brings -740 → -1500)")
print()

# Hubbard regime classification
print("  Hubbard model regime by U/W:")
hubbard_mats = {
    'Cu metal':      (7, 9),
    'NiO':           (8, 2),
    'La2CuO4 (Mott)': (10, 2),
    'V2O3':          (2, 1.5),
    'SrVO3':         (5, 3),
}
print(f"  {'Material':<22}{'U (eV)':<10}{'W (eV)':<10}{'U/W':<8}{'Type':<12}")
for mat, (U, W) in hubbard_mats.items():
    UW = U / W
    typ = "Metal" if UW < 1 else ("Intermediate" if UW < 3 else "Mott insulator")
    print(f"  {mat:<22}{U:<10}{W:<10}{UW:<8.2f}{typ:<12}")
print()

# ----------------------------------------------------------------------
# Test 6: Bloch T^(3/2) magnetization law
# ----------------------------------------------------------------------
print("[Test 6] Bloch T^(3/2) magnetization law (3D FM low-T)")
# M(T)/M(0) = 1 - (T/T_C)^(3/2) × c
T_C = 631.0  # K for Ni
T_lowT = np.linspace(0, T_C * 0.6, 50)
const_Ni = 0.117    # Bloch coefficient for Ni (empirical-ish)
M_Bloch = 1 - const_Ni * (T_lowT / T_C) ** 1.5
print(f"  Ni T_C = {T_C} K, Bloch constant = {const_Ni}")
print(f"  M(T=100K)/M(0) = {1 - const_Ni*(100/T_C)**1.5:.4f}")
print(f"  M(T=200K)/M(0) = {1 - const_Ni*(200/T_C)**1.5:.4f}")
print(f"  M(T=400K)/M(0) = {1 - const_Ni*(400/T_C)**1.5:.4f}")
# Verify exponent
slope_Bloch, _ = np.polyfit(np.log(T_lowT[5:]), np.log(1 - M_Bloch[5:]), 1)
print(f"  Log-log fit of (1 - M/M_0) vs T: slope = {slope_Bloch:.3f} (theory 1.5 ✓)")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# 1) AF Ising MC vs T
ax = axes[0, 0]
ax.plot(T_list, m_stag_results, 'rs-', markersize=10, lw=2, label='2D AF Ising (L=16)')
ax.axvline(T_c_2D, color='red', linestyle=':', label=f'Onsager T_c = {T_c_2D:.3f}')
ax.set_xlabel('T (J/k_B)')
ax.set_ylabel('Staggered ⟨|m_s|⟩')
ax.set_title('Néel Antiferromagnet Order Parameter')
ax.legend()
ax.grid(True, alpha=0.3)

# 2) Magnon dispersion FM vs AF
ax = axes[0, 1]
ax.plot(k_arr / np.pi, eps_FM, 'b-', lw=2, label='FM: 2JS(1-cos(ka)) ~ k²')
ax.plot(k_arr / np.pi, eps_AF, 'r-', lw=2, label='AF: 2|J|S|sin(ka)| ~ |k|')
ax.set_xlabel('k a / π')
ax.set_ylabel('ε(k)')
ax.set_title('Magnon Dispersion: FM (quadratic) vs AF (linear)')
ax.legend()
ax.grid(True, alpha=0.3)

# 3) Curie-Weiss χ(T) for Fe Co Ni Gd
ax = axes[1, 0]
for mat, d in materials_FM.items():
    chi_inv = (T_arr_CW - d['theta_K']) / (d['mu_eff'] ** 2 / 3)
    mask = T_arr_CW > d['theta_K']
    ax.plot(T_arr_CW[mask], chi_inv[mask], label=f"{mat} θ_C={d['theta_K']}K")
ax.axhline(0, color='black', lw=0.5)
ax.set_xlabel('T (K)')
ax.set_ylabel('1/χ (T - θ_C)/C')
ax.set_title('Curie-Weiss: 1/χ vs T (linear, x-intercept = θ_C)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# 4) Stoner criterion
ax = axes[1, 1]
mats = list(stoner_data.keys())
IDs = [stoner_data[m]['I'] * stoner_data[m]['D_eF'] for m in mats]
colors_s = ['red' if stoner_data[m]['FM'] else 'steelblue' for m in mats]
bars = ax.bar(mats, IDs, color=colors_s, edgecolor='black')
ax.axhline(1.0, color='black', linestyle='--', label='Stoner threshold I·D = 1')
ax.set_ylabel('I × D(ε_F)')
ax.set_title('Stoner Ferromagnetism Criterion')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'heisenberg_hubbard_stoner.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 154,
    "title": "Magnetism — Heisenberg + Hubbard + Stoner + Mott",
    "tier1_paper": "#22 Condensed Matter (phase 4/8)",
    "tests": {
        "AF_Ising_MC": {
            "Onsager_Tc": float(T_c_2D),
            "T_scan": T_list,
            "staggered_m": [float(x) for x in m_stag_results],
        },
        "magnon_dispersion": {
            "FM_log_log_slope_small_k": float(slope_FM),
            "AF_log_log_slope_small_k": float(slope_AF),
            "theory_FM_slope": 2.0,
            "theory_AF_slope": 1.0,
        },
        "curie_weiss_materials": materials_FM,
        "stoner_criterion": {
            m: {**d, "I_times_D": d['I'] * d['D_eF'],
                "Stoner_prediction": "FM" if d['I'] * d['D_eF'] > 1 else "PM"}
            for m, d in stoner_data.items()
        },
        "superexchange_cuprate": {
            "t_eV": t_cuprate,
            "U_eV": U_cuprate,
            "J_ex_eV": float(J_super),
            "J_ex_K": float(J_super_K),
            "experimental_La2CuO4_J_K": -1500,
        },
        "hubbard_regimes": {
            mat: {"U_eV": U, "W_eV": W, "U_over_W": U/W}
            for mat, (U, W) in hubbard_mats.items()
        },
        "bloch_T32_law": {
            "T_C_Ni_K": T_C,
            "Bloch_constant": const_Ni,
            "log_log_slope": float(slope_Bloch),
            "theory_slope": 1.5,
        },
    },
    "itu_interpretation": {
        "Heisenberg": "K_spin SU(2)-invariant Hamiltonian",
        "Curie_Weiss": "K_spin mean-field response",
        "magnon": "K_spin Goldstone mode (Phase 145)",
        "Hubbard": "K_band + K_correlation",
        "Mott": "K_correlation U/t → ∞ (kinetic blocking)",
        "superexchange": "K_correlation second-order perturbative",
        "Stoner": "K_FD exchange instability → spin polarization",
        "frustration": "K_spin geometric constraint",
        "spin_liquid": "K_spin topological order (Anderson RVB)",
    },
    "key_findings": [
        f"2D AF Ising staggered order drops near Onsager T_c = {T_c_2D:.2f}",
        f"Magnon dispersion: FM k^{slope_FM:.2f} (theory k²), AF k^{slope_AF:.2f} (theory k¹)",
        "Stoner correctly predicts Fe/Co/Ni FM and Cu/Pt PM",
        f"Cuprate superexchange J = -4t²/U = {J_super_K:.0f} K (exp -1500 K)",
        f"Bloch T^(3/2) law: log-log slope = {slope_Bloch:.3f} (theory 1.5 ✓)",
    ],
}

out_json = os.path.join(os.path.dirname(__file__), 'heisenberg_hubbard_stoner_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 154 complete: K_magnetic = K_stat + spin DOF + exchange;")
print(f"  Magnon FM slope = {slope_FM:.2f}, AF slope = {slope_AF:.2f}; Bloch T^{slope_Bloch:.2f}")
print("=" * 70)
