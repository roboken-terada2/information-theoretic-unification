"""
Phase 157: Soft matter — liquid crystals + colloids + polymers + self-assembly
==============================================================================

Tests:
1. Maier-Saupe nematic order parameter S(T)
2. DLVO potential for charged colloids (vdW + screened Coulomb)
3. Debye length vs salt concentration
4. Self-avoiding walk Flory ν in 2D and 3D
5. Stokes-Einstein D = k_BT/(6πηR) for various sizes
6. Random close packing for hard spheres (φ_RCP ≈ 0.64)
7. Glass T_g database
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

np.random.seed(42)

print("=" * 70)
print("Phase 157: Soft Matter — Liquid Crystals + Colloids + Polymers")
print("=" * 70)
print()

# Constants
k_B = 1.380649e-23
e_chg = 1.602176634e-19
N_A = 6.02214076e23
eps_0 = 8.8541878128e-12
eps_r_water = 78.5

# ----------------------------------------------------------------------
# Test 1: Maier-Saupe nematic order parameter
# ----------------------------------------------------------------------
print("[Test 1] Maier-Saupe nematic order parameter S(T)")
# Self-consistency: S = ∫ (3 cos²θ - 1)/2 × P(θ) dθ
# P(θ) ∝ exp(λ S (3 cos²θ - 1)/2)
# λ = U_0 / (k_B T)

def maier_saupe_S(lambda_param, max_iter=100):
    """Solve for S self-consistently. λ = U_0/(k_B T) × n."""
    S = 0.5
    for _ in range(max_iter):
        # Numerical integration over θ
        theta = np.linspace(0, np.pi, 1000)
        x = (3 * np.cos(theta) ** 2 - 1) / 2
        weight = np.sin(theta)  # solid angle element
        exp_arg = lambda_param * S * x
        # Normalize to avoid overflow
        exp_arg_max = np.max(exp_arg)
        Z = np.trapezoid(weight * np.exp(exp_arg - exp_arg_max), theta)
        S_new = np.trapezoid(x * weight * np.exp(exp_arg - exp_arg_max), theta) / Z
        if abs(S_new - S) < 1e-8:
            return S_new
        S = S_new
    return S

# Maier-Saupe critical: lambda_c ≈ 4.541 (first-order N-I transition)
# S(T_NI-) ≈ 0.43 (Maier-Saupe)
lambdas = np.linspace(2.0, 8.0, 60)
S_arr = np.array([maier_saupe_S(l) for l in lambdas])
# Find jump
jump_idx = np.argmax(np.diff(S_arr))
lambda_c = lambdas[jump_idx + 1]
S_at_NI = S_arr[jump_idx + 1]
print(f"  Numerical critical λ_c ≈ {lambda_c:.2f}  (theory 4.541)")
print(f"  S(λ_c+) ≈ {S_at_NI:.3f}  (theory 0.43)")
print(f"  → λ ∝ 1/T: low T (high λ) → S ≈ 0.5-0.8 (nematic order)")
print()

# ----------------------------------------------------------------------
# Test 2: DLVO potential
# ----------------------------------------------------------------------
print("[Test 2] DLVO potential — vdW + screened Coulomb")
T = 298.0
R_col = 100e-9    # 100 nm colloid
A_Hamaker = 1e-20  # J (water/silica typical)
sigma_charge_per_m2 = 0.01  # C/m² (typical)

r_arr = np.linspace(1e-9, 50e-9, 500)
# vdW
U_vdW = -A_Hamaker * R_col / (12 * r_arr)
# Screened Coulomb: simplified for spheres
lambda_D_100mM = np.sqrt(eps_0 * eps_r_water * k_B * T / (2 * 0.1 * 1000 * N_A * e_chg ** 2))
psi_0 = 25e-3   # 25 mV typical surface potential
U_elec = 2 * np.pi * eps_0 * eps_r_water * R_col * psi_0 ** 2 * np.exp(-r_arr / lambda_D_100mM)
U_total = U_vdW + U_elec

# Find barrier
idx_max = np.argmax(U_total)
barrier = U_total[idx_max]
barrier_kT = barrier / (k_B * T)
print(f"  Colloid R = {R_col*1e9} nm, T = {T} K, [NaCl] = 100 mM")
print(f"  Hamaker A = {A_Hamaker:.0e} J")
print(f"  Debye length λ_D = {lambda_D_100mM*1e9:.2f} nm")
print(f"  Surface potential ψ_0 = {psi_0*1000} mV")
print(f"  DLVO barrier height: {barrier:.3e} J = {barrier_kT:.1f} k_B T")
print()

# ----------------------------------------------------------------------
# Test 3: Debye length vs salt concentration
# ----------------------------------------------------------------------
print("[Test 3] Debye length vs salt concentration")
salt_M = np.array([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 0.1, 0.15, 1.0])
lambda_D_arr = np.sqrt(eps_0 * eps_r_water * k_B * T / (2 * salt_M * 1000 * N_A * e_chg ** 2))
print(f"  {'[salt] (M)':<12}{'λ_D (nm)':<12}{'system':<25}")
labels_salt = ['ultrapure water', '', '', '', '', '', 'physiological', 'seawater']
for s, lD, lab in zip(salt_M, lambda_D_arr, labels_salt):
    print(f"  {s:<12.0e}{lD*1e9:<12.3f}{lab:<25}")
print()

# ----------------------------------------------------------------------
# Test 4: Self-avoiding walk (SAW) in 2D and 3D
# ----------------------------------------------------------------------
print("[Test 4] Self-avoiding walk — Flory ν exponent")
def SAW_2D(N, n_samples=200):
    """Try simple random self-avoiding walk on a 2D square lattice."""
    R_end = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for _ in range(n_samples):
        pos = (0, 0)
        visited = {(0, 0)}
        success = True
        for _ in range(N):
            np.random.shuffle(moves)
            placed = False
            for dx, dy in moves:
                new = (pos[0] + dx, pos[1] + dy)
                if new not in visited:
                    visited.add(new)
                    pos = new
                    placed = True
                    break
            if not placed:
                success = False
                break
        if success:
            R_end.append(np.sqrt(pos[0]**2 + pos[1]**2))
    return np.mean(R_end) if R_end else 0.0, len(R_end)

def SAW_3D(N, n_samples=200):
    R_end = []
    moves = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    for _ in range(n_samples):
        pos = (0,0,0)
        visited = {(0,0,0)}
        success = True
        for _ in range(N):
            np.random.shuffle(moves)
            placed = False
            for dx, dy, dz in moves:
                new = (pos[0]+dx, pos[1]+dy, pos[2]+dz)
                if new not in visited:
                    visited.add(new)
                    pos = new
                    placed = True
                    break
            if not placed:
                success = False
                break
        if success:
            R_end.append(np.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2))
    return np.mean(R_end) if R_end else 0.0, len(R_end)

N_chain = [10, 20, 40, 80, 160]
R_2D, R_3D = [], []
for N in N_chain:
    r2, _ = SAW_2D(N, n_samples=100)
    r3, _ = SAW_3D(N, n_samples=100)
    R_2D.append(r2)
    R_3D.append(r3)
    print(f"  N = {N:>4}: ⟨R⟩_2D = {r2:.2f}, ⟨R⟩_3D = {r3:.2f}")

# Fit ν
def fit_nu(N_list, R_list):
    valid = [(n, r) for n, r in zip(N_list, R_list) if r > 0]
    if len(valid) < 2:
        return float('nan')
    Ns, Rs = zip(*valid)
    nu, _ = np.polyfit(np.log(Ns), np.log(Rs), 1)
    return nu
nu_2D = fit_nu(N_chain, R_2D)
nu_3D = fit_nu(N_chain, R_3D)
print(f"\n  Flory ν (2D) = {nu_2D:.3f}  (theory exact 0.75)")
print(f"  Flory ν (3D) = {nu_3D:.3f}  (theory ~0.588)")
print()

# ----------------------------------------------------------------------
# Test 5: Stokes-Einstein diffusion
# ----------------------------------------------------------------------
print("[Test 5] Stokes-Einstein D = k_B T / (6πηR) — water @ 298 K")
eta_water = 1.0e-3   # Pa·s
sizes_nm = np.array([0.5, 1, 5, 10, 50, 100, 500, 1000])  # nm radius
D_SE = k_B * T / (6 * np.pi * eta_water * sizes_nm * 1e-9)
print(f"  {'R (nm)':<10}{'D (m²/s)':<14}{'system':<25}")
ex_systems = ['ion', 'small molecule', 'protein', 'protein', 'virus', 'colloid', 'large colloid', 'bacterium']
for s, d, ex in zip(sizes_nm, D_SE, ex_systems):
    print(f"  {s:<10}{d:<14.3e}{ex:<25}")
print()

# ----------------------------------------------------------------------
# Test 6: Random close packing
# ----------------------------------------------------------------------
print("[Test 6] Hard sphere packing fractions")
packings = {
    'Random Loose Packing (RLP)': 0.55,
    'Random Close Packing (RCP)': 0.64,
    'BCC': 0.68,
    'FCC / HCP (close-packed)': np.pi / (3 * np.sqrt(2)),
    'Glass transition (hard sphere)': 0.58,
}
print(f"  {'Type':<35}{'φ':<10}")
for name, phi in packings.items():
    print(f"  {name:<35}{phi:<10.4f}")
print()

# ----------------------------------------------------------------------
# Test 7: Glass T_g database
# ----------------------------------------------------------------------
print("[Test 7] Glass transition temperatures T_g")
glasses = {
    'Glycerol':         190,
    'Vitreous ice (H₂O)': 136,
    'Toluene':          117,
    'Polystyrene':      373,
    'PMMA (acrylic)':   378,
    'Polycarbonate':    420,
    'Selenium':         313,
    'B₂O₃':             528,
    'Pyrex 7740':       820,
    'Soda-lime glass':  830,
    'Fused silica (SiO₂)': 1473,
}
print(f"  {'Material':<28}{'T_g (K)':<10}{'T_g (°C)':<10}")
for mat, tg in glasses.items():
    print(f"  {mat:<28}{tg:<10}{tg-273.15:<10.0f}")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# 1) Maier-Saupe S(λ) order parameter jump
ax = axes[0, 0]
ax.plot(lambdas, S_arr, 'b-', lw=2)
ax.axvline(lambda_c, color='red', linestyle='--', label=f'λ_c ≈ {lambda_c:.2f}')
ax.axhline(0.43, color='gray', linestyle=':', alpha=0.6, label='S = 0.43 (theory)')
ax.set_xlabel('λ ∝ 1/T (Maier-Saupe coupling / k_BT)')
ax.set_ylabel('Nematic order parameter S')
ax.set_title('Maier-Saupe Nematic-Isotropic Transition')
ax.legend()
ax.grid(True, alpha=0.3)

# 2) DLVO potential
ax = axes[0, 1]
ax.plot(r_arr * 1e9, U_vdW / (k_B * T), 'b-', lw=1.5, label='vdW (attractive)')
ax.plot(r_arr * 1e9, U_elec / (k_B * T), 'g-', lw=1.5, label='Screened Coulomb (repulsive)')
ax.plot(r_arr * 1e9, U_total / (k_B * T), 'r-', lw=2, label='DLVO total')
ax.axhline(0, color='black', lw=0.5)
ax.set_xlabel('r (nm)')
ax.set_ylabel('U / k_B T')
ax.set_title(f'DLVO Colloid Potential (R=100nm, 100mM NaCl, λ_D={lambda_D_100mM*1e9:.1f}nm)')
ax.legend(fontsize=9)
ax.set_ylim(-50, 100)
ax.grid(True, alpha=0.3)

# 3) Debye length vs salt
ax = axes[1, 0]
ax.loglog(salt_M, lambda_D_arr * 1e9, 'bs-', markersize=8, lw=2)
ax.axhline(1e-9 * 1e9, color='gray', linestyle=':', alpha=0.5, label='1 nm scale')
for s, lD, lab in zip(salt_M, lambda_D_arr, labels_salt):
    if lab:
        ax.annotate(lab, xy=(s, lD*1e9), fontsize=7, alpha=0.7,
                    textcoords='offset points', xytext=(5, 5))
ax.set_xlabel('[Salt] (M)')
ax.set_ylabel('λ_D (nm)')
ax.set_title('Debye Screening Length vs Salt Concentration')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# 4) SAW ν exponent
ax = axes[1, 1]
valid_2D = [(n, r) for n, r in zip(N_chain, R_2D) if r > 0]
valid_3D = [(n, r) for n, r in zip(N_chain, R_3D) if r > 0]
if valid_2D:
    Ns2, Rs2 = zip(*valid_2D)
    ax.loglog(Ns2, Rs2, 'bo-', label=f'2D SAW: ν ≈ {nu_2D:.3f} (theory 0.75)')
if valid_3D:
    Ns3, Rs3 = zip(*valid_3D)
    ax.loglog(Ns3, Rs3, 'rs-', label=f'3D SAW: ν ≈ {nu_3D:.3f} (theory 0.59)')
ax.set_xlabel('N (chain length)')
ax.set_ylabel('⟨R⟩')
ax.set_title('Self-Avoiding Walk — Flory Scaling')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'soft_matter_liquid_crystal.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 157,
    "title": "Soft matter — liquid crystals + colloids + polymers + self-assembly",
    "tier1_paper": "#22 Condensed Matter (phase 7/8)",
    "tests": {
        "maier_saupe": {
            "lambda_c_numerical": float(lambda_c),
            "lambda_c_theory": 4.541,
            "S_at_NI_numerical": float(S_at_NI),
            "S_at_NI_theory": 0.43,
        },
        "DLVO_potential": {
            "colloid_R_nm": R_col * 1e9,
            "Hamaker_A_J": A_Hamaker,
            "salt_100mM_lambda_D_nm": float(lambda_D_100mM * 1e9),
            "surface_potential_mV": psi_0 * 1000,
            "barrier_height_kT": float(barrier_kT),
        },
        "debye_length_vs_salt": {
            f"{s:.0e}M": float(lD * 1e9) for s, lD in zip(salt_M, lambda_D_arr)
        },
        "SAW_Flory": {
            "N_chain": N_chain,
            "R_2D": [float(r) for r in R_2D],
            "R_3D": [float(r) for r in R_3D],
            "nu_2D_fit": float(nu_2D),
            "nu_3D_fit": float(nu_3D),
            "nu_2D_exact": 0.75,
            "nu_3D_accurate": 0.588,
        },
        "stokes_einstein": {
            "T_K": T, "viscosity_water_Pa_s": eta_water,
            "size_nm": sizes_nm.tolist(),
            "D_m2_per_s": D_SE.tolist(),
        },
        "packing_fractions": packings,
        "glass_Tg_K": glasses,
    },
    "itu_interpretation": {
        "nematic": "K_orientation only (K_position absent)",
        "DLVO": "K_attractive vdW + K_repulsive screened Coulomb",
        "Flory": "K_chain self-avoiding scaling",
        "reptation": "K_chain topological constraint dynamics",
        "self_assembly": "K_amphiphile minimum free energy",
        "lipid_bilayer": "K_membrane 2D fluid + bending elastic",
        "protein_folding": "K_polymer native attractor (Phase 149 K_complex)",
        "glass_transition": "K_stat dynamical arrest",
    },
    "key_findings": [
        f"Maier-Saupe λ_c ≈ {lambda_c:.2f} (theory 4.54), S(NI) ≈ {S_at_NI:.3f}",
        f"DLVO barrier {barrier_kT:.1f} k_BT for 100 nm colloid in 100 mM NaCl",
        f"Debye length: 1 μm (ultrapure) → 1 nm (100 mM) → 0.3 nm (1 M)",
        f"Flory ν: 2D = {nu_2D:.3f} (exact 0.75), 3D = {nu_3D:.3f} (best 0.588)",
        f"Stokes-Einstein: protein D ~ 10⁻¹⁰ m²/s, virus D ~ 10⁻¹² m²/s",
        f"Hard sphere RCP = 0.64, FCC = {np.pi/(3*np.sqrt(2)):.4f} (max possible)",
        "Glass T_g: vitreous ice 136 K → fused silica 1473 K (10× range)",
    ],
}

out_json = os.path.join(os.path.dirname(__file__), 'soft_matter_liquid_crystal_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 157 complete: K_soft = partial-order K_stat;")
print(f"  Maier-Saupe S({lambda_c:.2f})={S_at_NI:.2f}, Flory ν_2D={nu_2D:.3f} ν_3D={nu_3D:.3f}")
print("=" * 70)
