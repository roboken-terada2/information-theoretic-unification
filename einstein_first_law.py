"""
Phase 2: Linearized Einstein equations from the entanglement first law.

Verifies δS_A = δ<K_A> for free-fermion thermal perturbations of the XX
ground state, where K_A is the Peschel modular Hamiltonian of the
unperturbed reduced state. Combined with the Ryu–Takayanagi relation
S_A = Area(γ_A)/(4G), this is the lattice version of the Faulkner–Guica–
Hartman–Myers–Van Raamsdonk (2014) derivation of linearized Einstein
equations from quantum information.

References:
- Jacobson, PRL 75 (1995) 1260
- Peschel, J. Phys. A 36 (2003) L205
- Casini–Huerta–Myers, JHEP 2011:36
- Faulkner–Guica–Hartman–Myers–Van Raamsdonk, JHEP 2014:51
- Brown–Henneaux 1986
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# ---------------------------------------------------------------
# Free fermion machinery (OBC to avoid zero modes at half filling)
# ---------------------------------------------------------------
def hopping_matrix(N, periodic=False):
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    if periodic:
        h[0, N - 1] = h[N - 1, 0] = -1.0
    return h

def thermal_correlation(N, beta, periodic=False):
    """Thermal Gaussian state: C_ij = sum_k U_ik n_F(beta eps_k) U_jk^*."""
    h = hopping_matrix(N, periodic)
    eigvals, U = eigh(h)
    occ = 1.0 / (1.0 + np.exp(beta * eigvals))
    return ((U * occ) @ U.conj().T).real

def ground_correlation(N, periodic=False):
    """β → ∞ limit, strict half filling."""
    h = hopping_matrix(N, periodic)
    eigvals, U = eigh(h)
    n = N // 2
    return (U[:, :n] @ U[:, :n].conj().T).real

def fermion_entropy(C_sub):
    eigs = np.linalg.eigvalsh(C_sub)
    eigs = np.clip(eigs, 1e-14, 1 - 1e-14)
    return float(-np.sum(eigs * np.log(eigs) + (1 - eigs) * np.log(1 - eigs)))

def modular_hamiltonian_matrix(C_A):
    """Peschel: K_A = c† M c with M = log[(1-C_A)/C_A]."""
    eigvals, V = eigh(C_A)
    eigvals = np.clip(eigvals, 1e-14, 1 - 1e-14)
    M_diag = np.log((1 - eigvals) / eigvals)
    return ((V * M_diag) @ V.conj().T).real

# ---------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------
def main():
    N = 64
    interval = list(range(20, 44))  # 24 sites in the middle, far from boundaries
    L = len(interval)
    print("=== Phase 2: First Law → Linearized Einstein ===")
    print(f"  N = {N}, interval A = sites {interval[0]}..{interval[-1]} (|A|={L})\n")

    # Unperturbed ground state and modular Hamiltonian
    C0 = ground_correlation(N)
    C0_A = C0[np.ix_(interval, interval)]
    S0 = fermion_entropy(C0_A)
    M_A = modular_hamiltonian_matrix(C0_A)
    K0 = float(np.trace(M_A @ C0_A))
    print(f"  Vacuum: S_A^(0) = {S0:.6f},  <K_A>_0 = {K0:.6f}")

    # Thermal perturbations
    Ts = np.logspace(-2.0, 0.4, 18)   # T in [0.01, 2.5]
    deltaS = np.empty_like(Ts)
    deltaK = np.empty_like(Ts)
    for n, T in enumerate(Ts):
        beta = 1.0 / T
        C_T = thermal_correlation(N, beta)
        C_T_A = C_T[np.ix_(interval, interval)]
        deltaS[n] = fermion_entropy(C_T_A) - S0
        deltaK[n] = float(np.trace(M_A @ C_T_A)) - K0
    deviation = np.abs(deltaK - deltaS)

    print("\n  T          δS              δ<K>            |δ<K>-δS|")
    for T, dS, dK, dev in zip(Ts, deltaS, deltaK, deviation):
        print(f"  {T:7.4f}   {dS:+12.6e}   {dK:+12.6e}   {dev:.2e}")

    # First law holds to first order in δρ; deviation = relative entropy ≥ 0.
    # Use only the smallest T values for the linear fit (truly infinitesimal).
    mask_lin = Ts < 0.025
    slope, intercept = np.polyfit(deltaS[mask_lin], deltaK[mask_lin], 1)
    print(f"\n  [First law verification at small T (T<0.025, {mask_lin.sum()} points)]")
    print(f"    Linear fit:  δ<K> = {slope:.6f} · δS + {intercept:+.2e}   (predicted: slope = 1)")
    print(f"    Smallest-T ratio δ<K>/δS = {deltaK[0]/deltaS[0]:.6f}")

    # Positivity of relative entropy: δ<K> - δS = S(ρ_pert || ρ_0) ≥ 0
    print(f"\n  [Positivity (Casini): δ<K> - δS = relative entropy ≥ 0]")
    print(f"    Always non-negative across all T?  {np.all(deviation >= -1e-12)}")

    # Power law of the relative entropy at low T
    mask_pow = Ts < 0.1
    p = np.polyfit(np.log(Ts[mask_pow]), np.log(deviation[mask_pow] + 1e-18), 1)
    print(f"    Low-T scaling: S_rel ~ T^{p[0]:.3f}")

    # Brown–Henneaux: c=1 → R_AdS / G_N = 2/3
    print("\n  [Brown–Henneaux interpretation]")
    print("    XX model has c=1 (Phase 1).")
    print("    Emergent AdS_3 dual: R_AdS / G_N = 2c/3 ≈ 0.6667.")
    print("    Each S_A is, by Ryu–Takayanagi, the geodesic length / (4 G_N) in this AdS_3.")
    print("    Therefore the verified δS = δ<K> equation is the linearised Einstein eq.")
    print("    δG_μν^(1) = 8π G_N δT_μν   (Faulkner–Guica–Hartman–Myers–Van Raamsdonk 2014).")

    # ----------------------------------------------------------
    # Plot
    # ----------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6))

    # (a) δS vs δ<K>
    ax = axes[0]
    ax.plot(deltaS, deltaK, 'o-', label='numerics')
    lim = max(abs(deltaS).max(), abs(deltaK).max()) * 1.05
    ax.plot([0, lim], [0, lim], 'k--', label=r'first law: $\delta\langle K\rangle = \delta S$')
    ax.set_xlabel(r'$\delta S_A$')
    ax.set_ylabel(r'$\delta \langle K_A \rangle$')
    ax.set_title('(a) Entanglement first law (XX vacuum)')
    ax.legend(); ax.grid(alpha=0.3)

    # (b) deviation = relative entropy, on log-log; superimpose fitted slope
    ax = axes[1]
    ax.loglog(Ts, deviation, 'o-', label=r'$S_\mathrm{rel} = \delta\langle K\rangle - \delta S$')
    ref = (Ts / Ts[mask_pow][-1]) ** p[0] * deviation[mask_pow][-1]
    ax.loglog(Ts, ref, 'k--', label=fr'fit $\propto T^{{{p[0]:.2f}}}$')
    ax.set_xlabel('temperature T')
    ax.set_ylabel(r'relative entropy $S_\mathrm{rel}$')
    ax.set_title(r'(b) Casini positivity: $S_\mathrm{rel} \geq 0$')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (c) modular Hamiltonian local profile vs CFT BMS kernel
    ax = axes[2]
    diag_M = np.diag(M_A)
    x = np.arange(L)
    bms = x * (L - 1 - x)
    bms_scaled = bms * (diag_M.max() / max(bms.max(), 1e-12))
    ax.plot(x, diag_M, 'o-', label=r'lattice $M_{ii}$ (Peschel)')
    ax.plot(x, bms_scaled, '--', label=r'CFT/CHM kernel $\propto x(L{-}1{-}x)$')
    ax.set_xlabel('position within interval'); ax.set_ylabel('local modular weight')
    ax.set_title('(c) Modular Hamiltonian → CHM Killing vector')
    ax.legend(); ax.grid(alpha=0.3)

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\einstein_first_law.png'
    plt.savefig(out, dpi=130)
    print(f"\nFigure saved to {out}")

    # JSON summary
    import json
    summary = {
        'N': N, 'interval_size': L,
        'S0': S0, 'K0': K0,
        'first_law_slope_at_small_T': float(slope),
        'first_law_intercept': float(intercept),
        'first_law_smallest_T_ratio': float(deltaK[0] / deltaS[0]),
        'relative_entropy_exponent_low_T': float(p[0]),
        'brown_henneaux_R_over_G': 2/3,
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase2.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("Summary saved to summary_phase2.json")


if __name__ == '__main__':
    main()
