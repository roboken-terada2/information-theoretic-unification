"""
Phase 17: Nonlinear Einstein equations from second-order relative entropy.

We extend Phase 2 (linearised Einstein) to the next order by demonstrating
that the relative entropy obeys

    S_rel(rho_lambda || rho^(0)) = (1/2) g_F · lambda^2 + O(lambda^3)

where g_F is the quantum Fisher information, which for the vacuum modular
Hamiltonian K^(0) equals Var(K^(0))_rho^(0).

This is the bulk-side dual of the leading nonlinear correction to Einstein
equations (Faulkner et al. 2017, "Nonlinear gravity from entanglement").

Numerical verification on the XX chain:
 (A) Analytically compute Var(K_A^vac) via Gaussian Wick.
 (B) Numerically compute S_rel(T) for small T, fit quadratic coefficient.
 (C) Compare: 2 × coefficient should equal Var(K_A^vac).
 (D) Higher-order (cubic) deviations indicate the next nonlinear correction.

References:
- Lashkari, Van Raamsdonk, JHEP 2016:153 — Fisher information from entropy
- Faulkner, Haehl, Hijano, Parrikar, Rabideau, Van Raamsdonk, JHEP 2017 — second-order
- Casini, NPB 2008 — relative entropy positivity
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
import time as _time

# ---------------------------------------------------------------
def hopping_chain(N, periodic=True):
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i+1] = h[i+1, i] = -1.0
    if periodic:
        h[0, N-1] = h[N-1, 0] = -1.0
    return h

def ground_correlation(N, periodic=False):
    # OBC to avoid zero-mode degeneracy
    h = hopping_chain(N, periodic)
    _, U = eigh(h)
    n = N // 2
    return (U[:, :n] @ U[:, :n].conj().T).real

def thermal_correlation(N, beta, periodic=False):
    # OBC: chemical potential at midgap, no zero modes
    h = hopping_chain(N, periodic)
    eigvals, U = eigh(h)
    occ = 1.0 / (1.0 + np.exp(beta * eigvals))
    return ((U * occ) @ U.conj().T).real

def fermion_entropy(C_sub):
    eigs = np.linalg.eigvalsh(C_sub)
    eigs = np.clip(eigs, 1e-14, 1 - 1e-14)
    return float(-np.sum(eigs * np.log(eigs) + (1-eigs) * np.log(1-eigs)))

def modular_M(C_A):
    eigvals, V = eigh(C_A)
    eigvals = np.clip(eigvals, 1e-14, 1 - 1e-14)
    return ((V * np.log((1 - eigvals)/eigvals)) @ V.conj().T).real

def variance_K(M, C):
    """Variance of K = sum_ij M_ij c_i† c_j in Gaussian state with correlator C.
       Var(K) = Tr(M² C) - Tr(M C M C^T)  (derived via Wick)."""
    M2C = M @ M @ C
    MCMCT = M @ C @ M @ C.T
    return float(np.trace(M2C) - np.trace(MCMCT))

def mean_K(M, C):
    return float(np.trace(M @ C))

# ---------------------------------------------------------------
def main():
    N = 64
    print("=== Phase 17: Nonlinear Einstein from second-order relative entropy ===\n")
    a, b = 16, 48
    interval = list(range(a, b))
    L_A = len(interval)
    print(f"  XX chain N={N}, interval A=[{a},{b}) (|A|={L_A})\n")

    # --- (A) Vacuum and modular Hamiltonian ---
    C_vac_full = ground_correlation(N)
    C_vac = C_vac_full[np.ix_(interval, interval)]
    M_A = modular_M(C_vac)
    S_vac = fermion_entropy(C_vac)
    K_vac = mean_K(M_A, C_vac)
    Var_K_vac = variance_K(M_A, C_vac)
    print(f"[Result A — Modular structure of the vacuum]")
    print(f"  S(A)_vac      = {S_vac:.4f}")
    print(f"  <K_A>_vac     = {K_vac:.4f}")
    print(f"  Var(K_A)_vac  = {Var_K_vac:.4f}    ← quantum Fisher information\n")

    # --- (B) Modular-temperature perturbation: ρ(ε) = e^{-(1+ε)K} / Z ---
    # The proper "tangent direction" at the vacuum for which the Fisher
    # information equals Var(K) is to scale the modular Hamiltonian by (1+ε).
    # This corresponds to changing the entanglement temperature of A.
    def C_at_modular_shift(M, eps):
        eigvals_M, V_M = eigh(M)
        # Occupation under shifted modular: n(ε) = 1/(1 + e^{(1+ε)·M_eig})
        occ = 1.0 / (1.0 + np.exp((1 + eps) * eigvals_M))
        return ((V_M * occ) @ V_M.conj().T).real

    eps_list = np.logspace(-4, -0.5, 24)
    S_rel_vals = []
    delta_K_vals = []
    delta_S_vals = []
    for eps in eps_list:
        C_eps = C_at_modular_shift(M_A, eps)
        S_eps = fermion_entropy(C_eps)
        K_mean_eps = mean_K(M_A, C_eps)
        delta_K = K_mean_eps - K_vac
        delta_S = S_eps - S_vac
        S_rel_vals.append(delta_K - delta_S)
        delta_K_vals.append(delta_K)
        delta_S_vals.append(delta_S)
    S_rel_vals = np.array(S_rel_vals)
    delta_K_vals = np.array(delta_K_vals)
    delta_S_vals = np.array(delta_S_vals)

    # --- (C) Power-law fit ---
    fit_mask = eps_list < 0.01
    log_eps = np.log(eps_list[fit_mask])
    log_Srel = np.log(np.abs(S_rel_vals[fit_mask]) + 1e-30)
    p_fit, c_fit = np.polyfit(log_eps, log_Srel, 1)
    coeff = np.exp(c_fit)
    print(f"[Result B — Power-law fit at small ε (modular-temperature shift)]")
    print(f"  S_rel(ε) ~ {coeff:.4f} · ε^{p_fit:.3f}")
    print(f"  Predicted exponent: 2  (quantum Fisher information)")
    print(f"  Predicted coefficient: (1/2) Var(K) = {Var_K_vac/2:.4f}")
    print(f"  Numerical / predicted ratio: {coeff/(Var_K_vac/2):.4f}\n")

    # --- (D) S_rel / ε² convergence ---
    print(f"[Result C — Coefficient asymptote S_rel/ε² as ε → 0]")
    print(f"  ε            S_rel          S_rel / ε²       (1/2) Var(K)")
    for e_, Sr in zip(eps_list[:12], S_rel_vals[:12]):
        print(f"  {e_:9.6f}    {Sr:10.4e}    {Sr/e_**2:10.6f}       {Var_K_vac/2:.4f}")
    asymptote = (S_rel_vals[:5] / eps_list[:5]**2).mean()
    print(f"\n  Asymptote (smallest 5 ε): {asymptote:.4f}")
    print(f"  (1/2) Var(K):              {Var_K_vac/2:.4f}")
    print(f"  Ratio: {asymptote / (Var_K_vac/2):.4f}\n")

    # --- (E) Cubic residual ---
    cubic_part = S_rel_vals - 0.5 * Var_K_vac * eps_list**2
    nz = (np.abs(cubic_part) > 1e-14) & (eps_list < 0.2)
    if nz.sum() >= 4:
        p3, c3 = np.polyfit(np.log(eps_list[nz]), np.log(np.abs(cubic_part[nz])), 1)
        print(f"[Result D — Cubic correction]")
        print(f"  Residual: S_rel - (1/2)Var(K)ε² ~ ε^{p3:.3f}")
        print(f"  Predicted: ε³ (next-order Einstein correction)\n")

    # ============================================================
    # Plots
    # ============================================================
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

    # (1) S_rel vs ε (log-log)
    ax = axes[0]
    ax.loglog(eps_list, S_rel_vals, 'o', ms=6, label='numerical')
    ax.loglog(eps_list, 0.5 * Var_K_vac * eps_list**2, '--',
              label=fr'$\frac{{1}}{{2}}$Var($K$)$\varepsilon^2 = {Var_K_vac/2:.3f}\,\varepsilon^2$')
    ax.set_xlabel(r'modular shift $\varepsilon$'); ax.set_ylabel(r'$S_\mathrm{rel}$')
    ax.set_title('(A) Quadratic Fisher-info dominance')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (2) S_rel / ε² (should plateau at (1/2)Var(K))
    ax = axes[1]
    ax.semilogx(eps_list, S_rel_vals / eps_list**2, 'o-', ms=5,
                label=r'$S_\mathrm{rel}/\varepsilon^2$')
    ax.axhline(Var_K_vac / 2, color='red', linestyle='--',
               label=fr'(1/2) Var($K$) = {Var_K_vac/2:.3f}')
    ax.set_xlabel(r'$\varepsilon$'); ax.set_ylabel(r'$S_\mathrm{rel}/\varepsilon^2$')
    ax.set_title('(B) Asymptote = quantum Fisher information')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (3) δ⟨K⟩ vs δS
    ax = axes[2]
    ax.plot(delta_S_vals, delta_K_vals, 'o-', label='numerical')
    ref = np.array([0, max(delta_S_vals)])
    ax.plot(ref, ref, 'k--', label=r'first law: $\delta\langle K\rangle = \delta S$')
    ax.set_xlabel(r'$\delta S$'); ax.set_ylabel(r'$\delta\langle K\rangle$')
    ax.set_title('(C) Curvature beyond first law')
    ax.legend(); ax.grid(alpha=0.3)

    plt.suptitle('Phase 17: Nonlinear Einstein from second-order entanglement law', fontsize=12)
    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\nonlinear_einstein.png'
    plt.savefig(out, dpi=130, bbox_inches='tight')
    print(f"Figure saved to {out}")

    import json
    summary = {
        'N': N, 'L_A': L_A,
        'S_vac': S_vac, 'K_vac_mean': K_vac,
        'Var_K_vac': Var_K_vac,
        'half_Var_K_vac': Var_K_vac / 2,
        'fitted_power_law_exponent': float(p_fit),
        'fitted_coefficient': float(coeff),
        'predicted_coefficient_half_Var_K': float(Var_K_vac / 2),
        'coefficient_ratio': float(coeff / (Var_K_vac / 2)) if not np.isnan(coeff) else None,
        'asymptote_smallest_eps': float(asymptote),
        'asymptote_ratio_to_half_Var_K': float(asymptote / (Var_K_vac / 2)),
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase17.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print('Summary saved.')

if __name__ == '__main__':
    main()
