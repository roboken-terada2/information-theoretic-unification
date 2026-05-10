"""
Emergent Spacetime from Quantum Information
============================================
Numerical demonstration that 1D spacetime geometry emerges from the entanglement
structure of a free-fermion (XX-model) ground state, while a generic random
Gaussian state has no geometric interpretation.

References:
- Peschel, J. Phys. A 36 (2003) L205  -- entanglement of free fermions
- Calabrese & Cardy, J. Stat. Mech. (2004) P06002  -- CFT entanglement scaling
- Cao, Carroll & Michalakis, Phys. Rev. D 95 (2017) 024031  -- space from Hilbert space
- Van Raamsdonk, GRG 42 (2010) 2323  -- spacetime from entanglement
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from itertools import combinations

# ----------------------------------------------------------------------
# 1. Free fermion ground state correlation matrix C_ij = <c_i^dag c_j>
# ----------------------------------------------------------------------
def xx_correlation(N, periodic=True):
    """XX-model (tight-binding) ground state at half filling."""
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    if periodic:
        h[0, N - 1] = h[N - 1, 0] = -1.0
    eigvals, U = eigh(h)
    n_occ = N // 2
    C = U[:, :n_occ] @ U[:, :n_occ].conj().T
    return C.real

def random_gaussian_correlation(N, seed=0):
    """Generic fermionic Gaussian state: random unitary basis, half-filled."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = (A + A.conj().T) / 2.0
    _, U = eigh(H)
    n_occ = N // 2
    C = U[:, :n_occ] @ U[:, :n_occ].conj().T
    return C.real

# ----------------------------------------------------------------------
# 2. Entanglement entropy from sub correlation matrix (Peschel 2003)
# ----------------------------------------------------------------------
def fermion_entropy(C_sub):
    eigs = np.linalg.eigvalsh(C_sub)
    eigs = np.clip(eigs, 1e-14, 1 - 1e-14)
    return float(-np.sum(eigs * np.log(eigs) + (1 - eigs) * np.log(1 - eigs)))

def interval_entropy(C, sites):
    sites = list(sites)
    return fermion_entropy(C[np.ix_(sites, sites)])

# ----------------------------------------------------------------------
# 3. Mutual information matrix
# ----------------------------------------------------------------------
def mutual_information_matrix(C):
    N = C.shape[0]
    S1 = np.array([interval_entropy(C, [i]) for i in range(N)])
    Imat = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            S2 = interval_entropy(C, [i, j])
            Imat[i, j] = S1[i] + S1[j] - S2
            Imat[j, i] = Imat[i, j]
    return Imat, S1

# ----------------------------------------------------------------------
# 4. Information distance and classical multidimensional scaling
# ----------------------------------------------------------------------
def info_distance_matrix(Imat, S1, eps=1e-10):
    N = Imat.shape[0]
    D = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            Imax = 2.0 * min(S1[i], S1[j]) + eps
            D[i, j] = -np.log(max(Imat[i, j], eps) / Imax)
    return D

def classical_mds(D, dim_max=8):
    """Return coordinates for the top dim_max dimensions and the full eigenvalue spectrum."""
    N = D.shape[0]
    D2 = D ** 2
    J = np.eye(N) - np.ones((N, N)) / N
    B = -0.5 * J @ D2 @ J
    eigvals, eigvecs = eigh(B)
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    pos = np.maximum(eigvals[:dim_max], 0.0)
    X = eigvecs[:, :dim_max] * np.sqrt(pos)
    return X, eigvals

# ----------------------------------------------------------------------
# 5. CFT scaling check for ground-state entanglement entropy
# ----------------------------------------------------------------------
def entropy_vs_interval_length(C, N):
    ells = np.arange(1, N // 2 + 1)
    S = np.array([interval_entropy(C, list(range(0, ell))) for ell in ells])
    return ells, S

def cft_curve(ells, N, c=1.0):
    """Calabrese–Cardy CFT prediction for PBC: S = (c/3) log[(N/pi) sin(pi*l/N)] + const."""
    chord = (N / np.pi) * np.sin(np.pi * ells / N)
    return (c / 3.0) * np.log(chord)

# ----------------------------------------------------------------------
# 6. Run the numerical experiment
# ----------------------------------------------------------------------
def main():
    N = 32
    print(f"=== Emergent Spacetime from Quantum Information (N = {N}) ===\n")

    # XX ground state (geometric)
    C_xx = xx_correlation(N, periodic=True)
    I_xx, S1_xx = mutual_information_matrix(C_xx)
    D_xx = info_distance_matrix(I_xx, S1_xx)
    X_xx, lam_xx = classical_mds(D_xx)

    # Random Gaussian state (non-geometric)
    C_rnd = random_gaussian_correlation(N, seed=1)
    I_rnd, S1_rnd = mutual_information_matrix(C_rnd)
    D_rnd = info_distance_matrix(I_rnd, S1_rnd)
    X_rnd, lam_rnd = classical_mds(D_rnd)

    # CFT scaling test on XX state
    ells, S_int = entropy_vs_interval_length(C_xx, N)
    S_cft = cft_curve(ells, N, c=1.0)
    offset = np.mean(S_int - S_cft)

    # ---- Console report -------------------------------------------------
    print("[Theorem A — Calabrese–Cardy CFT scaling]")
    print(f"  Fitted central charge (regression on chord variable):")
    chord = (N / np.pi) * np.sin(np.pi * ells / N)
    A = np.vstack([np.log(chord), np.ones_like(chord)]).T
    sol, *_ = np.linalg.lstsq(A, S_int, rcond=None)
    print(f"    c_fit = {3*sol[0]:.4f}    (exact: c = 1.0)")
    print(f"    constant offset = {sol[1]:.4f}\n")

    print("[Theorem B — Information geometry of XX ground state]")
    top5 = lam_xx[:5] / np.sum(np.maximum(lam_xx, 0))
    print(f"  Top-5 normalized MDS eigenvalues: {np.round(top5, 4)}")
    print(f"  Variance explained by 2D embedding: {top5[:2].sum()*100:.2f}%\n")

    print("[Theorem C — Random state has no geometry]")
    top5r = lam_rnd[:5] / np.sum(np.maximum(lam_rnd, 0))
    print(f"  Top-5 normalized MDS eigenvalues: {np.round(top5r, 4)}")
    print(f"  Variance explained by 2D embedding: {top5r[:2].sum()*100:.2f}%\n")

    print("[Theorem D — Power-law decay of mutual information]")
    # average I over all pairs at the same chord distance
    dists = []
    Ivals = []
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, N - (j - i))
            dists.append(d)
            Ivals.append(I_xx[i, j])
    dists = np.array(dists); Ivals = np.array(Ivals)
    # fit log I ~ -alpha log d for d >= 2
    mask = (dists >= 2)
    p = np.polyfit(np.log(dists[mask]), np.log(Ivals[mask]), 1)
    print(f"  I(d) ~ d^alpha   ->   alpha = {p[0]:.4f}    (CFT exact: alpha = -2)")
    print()

    # ---- Plots ---------------------------------------------------------
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    # (a) CFT scaling
    ax = axes[0, 0]
    ax.plot(ells, S_int, 'o', label='XX ground state (numerics)')
    ax.plot(ells, S_cft + offset, '-', label=f'CFT prediction (c=1)')
    ax.set_xlabel(r'interval length $\ell$')
    ax.set_ylabel(r'entanglement entropy $S(\ell)$')
    ax.set_title('(a) Calabrese–Cardy CFT scaling')
    ax.legend(); ax.grid(alpha=0.3)

    # (b) Mutual information vs distance (log-log)
    ax = axes[0, 1]
    uniq = sorted(set(dists.tolist()))
    avgI = [np.mean(Ivals[dists == d]) for d in uniq]
    ax.loglog(uniq, avgI, 'o-', label='XX ground state')
    # Random comparison
    Ivals_r = []
    dists_r = []
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, N - (j - i))
            dists_r.append(d); Ivals_r.append(I_rnd[i, j])
    Ivals_r = np.array(Ivals_r); dists_r = np.array(dists_r)
    avgI_r = [np.mean(Ivals_r[dists_r == d]) for d in uniq]
    ax.loglog(uniq, avgI_r, 's--', label='random Gaussian state', alpha=0.6)
    ref_d = np.array(uniq, dtype=float)
    ax.loglog(ref_d, avgI[0] * (ref_d / ref_d[0]) ** (-2.0), 'k:', label=r'$\propto d^{-2}$ (CFT)')
    ax.set_xlabel('chord distance d'); ax.set_ylabel('I(d)')
    ax.set_title('(b) Power-law MI in the geometric state')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (c) MDS spectra comparison
    ax = axes[0, 2]
    k = np.arange(1, 11)
    norm_xx = lam_xx[:10] / np.sum(np.maximum(lam_xx, 0))
    norm_rnd = lam_rnd[:10] / np.sum(np.maximum(lam_rnd, 0))
    ax.semilogy(k, np.maximum(norm_xx, 1e-6), 'o-', label='XX ground state')
    ax.semilogy(k, np.maximum(norm_rnd, 1e-6), 's--', label='random state')
    ax.set_xlabel('eigenvalue index'); ax.set_ylabel('normalized eigenvalue')
    ax.set_title('(c) Emergent dimension spectrum')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (d) Recovered geometry from XX state (2D MDS)
    ax = axes[1, 0]
    # Color by original lattice position to verify ordering
    colors = plt.cm.viridis(np.linspace(0, 1, N))
    for i in range(N):
        ax.scatter(X_xx[i, 0], X_xx[i, 1], color=colors[i], s=80, edgecolor='k')
        ax.annotate(str(i), (X_xx[i, 0], X_xx[i, 1]), fontsize=7)
    # Connect nearest neighbours to highlight the recovered ring
    for i in range(N):
        j = (i + 1) % N
        ax.plot([X_xx[i, 0], X_xx[j, 0]], [X_xx[i, 1], X_xx[j, 1]], 'k-', alpha=0.3)
    ax.set_aspect('equal'); ax.grid(alpha=0.3)
    ax.set_title('(d) Recovered geometry: XX state → ring (S^1)')

    # (e) Recovered "geometry" from random state
    ax = axes[1, 1]
    for i in range(N):
        ax.scatter(X_rnd[i, 0], X_rnd[i, 1], color=colors[i], s=80, edgecolor='k')
        ax.annotate(str(i), (X_rnd[i, 0], X_rnd[i, 1]), fontsize=7)
    ax.set_aspect('equal'); ax.grid(alpha=0.3)
    ax.set_title('(e) Random state → no geometry')

    # (f) Mutual information matrix (XX)
    ax = axes[1, 2]
    im = ax.imshow(np.log10(I_xx + 1e-12), cmap='magma')
    plt.colorbar(im, ax=ax, label=r'$\log_{10} I(i:j)$')
    ax.set_title('(f) MI matrix of XX ground state')
    ax.set_xlabel('site i'); ax.set_ylabel('site j')

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\emergent_spacetime.png'
    plt.savefig(out, dpi=130)
    print(f"Figure saved to: {out}")

    # Save summary
    summary = {
        'N': N,
        'central_charge_fit': float(3 * sol[0]),
        'mi_powerlaw_alpha': float(p[0]),
        'xx_top5_normalized_eigs': norm_xx[:5].tolist(),
        'rnd_top5_normalized_eigs': norm_rnd[:5].tolist(),
        'xx_2d_variance_explained': float(top5[:2].sum()),
        'rnd_2d_variance_explained': float(top5r[:2].sum()),
    }
    import json
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("Summary saved to summary.json")

if __name__ == '__main__':
    main()
