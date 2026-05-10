"""
Phase 4: Time emerging from modular flow.

What we verify cleanly on the lattice:

(A) Casini–Huerta–Myers Killing kernel.  For an interval A in the XX
    vacuum on a periodic chain, |M_{i,i+1}| (the off-diagonal hopping
    of the Peschel modular matrix; on the lattice diag(M)≡0 since
    C_ii=1/2) is the geometric realisation of the local energy-density
    coupling.  Its envelope tracks the conformal Killing kernel
        w(x) = α · (R² − (x − x_c)²)/R
    that vanishes at the interval endpoints.

(B) Wave-packet flow under exp(-i M t).  The single-particle modular
    flow is non-trivial unitary dynamics derived from the entanglement
    structure alone, with no external Hamiltonian.

(C) Connes–Rovelli thermal time hypothesis.  For two states ω₁, ω₂
    (vacuum vs thermal) the modular Hamiltonians M(ω₁), M(ω₂) differ,
    so the flows σ_t^{ω_j} differ — each entanglement state defines its
    own emergent time.

(D) State-dependent wave-packet trajectories.  The same initial wave
    packet, evolved under M_vacuum vs M_thermal, traces visibly
    different "world-lines", concretely realising "time depends on the
    state of the universe".

References:
- Tomita 1957; Takesaki 1970
- Bisognano, Wichmann, J. Math. Phys. 17 (1976) 303
- Casini, Huerta, Myers, JHEP 2011:36
- Connes, Rovelli, Class. Quantum Grav. 11 (1994) 2899
- Eisler, Peschel, J. Stat. Mech. (2017) 053108
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def hopping(N, periodic=True):
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    if periodic:
        h[0, N - 1] = h[N - 1, 0] = -1.0
    return h

def ground_corr(N, periodic=True):
    h = hopping(N, periodic)
    _, U = eigh(h)
    n = N // 2
    return (U[:, :n] @ U[:, :n].conj().T).real

def thermal_corr(N, beta, periodic=True):
    h = hopping(N, periodic)
    eigvals, U = eigh(h)
    occ = 1.0 / (1.0 + np.exp(beta * eigvals))
    return ((U * occ) @ U.conj().T).real

def modular_M(C_A):
    eigvals, V = eigh(C_A)
    eigvals = np.clip(eigvals, 1e-14, 1 - 1e-14)
    return ((V * np.log((1 - eigvals) / eigvals)) @ V.conj().T).real

def hopping_kernel(M):
    L = M.shape[0]
    return np.array([M[i, i + 1] for i in range(L - 1)])

def main():
    print("=== Phase 4: Time from Modular Flow ===\n")

    # ---------- (A) CHM kernel ----------
    N = 128
    a, b = 32, 96
    interval = list(range(a, b))
    L = len(interval)
    R = (L - 1) / 2.0
    x_c = R

    C_full = ground_corr(N)
    M_int = modular_M(C_full[np.ix_(interval, interval)])
    hop = np.abs(hopping_kernel(M_int))
    x_mid = np.arange(L - 1) + 0.5
    chm = (R ** 2 - (x_mid - x_c) ** 2) / R
    bulk = (x_mid > 6) & (x_mid < L - 7)
    alpha = np.sum(hop[bulk] * chm[bulk]) / np.sum(chm[bulk] ** 2)
    print("[Result A — Casini–Huerta–Myers kernel envelope]")
    print(f"  |M_{{i,i+1}}| ~ α · (R² − (x − x_c)²) / R, fit α = {alpha:.4f}")
    print(f"  CFT prediction α = π/2 = {np.pi/2:.4f},  ratio = {alpha/(np.pi/2):.4f}")
    print(f"  Endpoints: |M_{{0,1}}|={hop[0]:.3f}, |M_{{L-2,L-1}}|={hop[-1]:.3f}")
    print(f"  Peak: |M|_max = {hop.max():.3f}  at x = {x_mid[np.argmax(hop)]:.1f}\n")

    # ---------- (B) Wave-packet flow under vacuum modular flow ----------
    sigma = 2.5
    times = np.linspace(0, 6.0, 80)
    x_local = np.arange(L)
    psi0 = np.exp(-(x_local - x_c) ** 2 / (2 * sigma ** 2))
    psi0 = psi0 / np.linalg.norm(psi0)

    def evolve(psi0, M, ts):
        eigM, V = eigh(M)
        c = V.conj().T @ psi0
        rho = np.zeros((len(ts), len(psi0)))
        avg = np.zeros(len(ts)); var = np.zeros(len(ts))
        for ti, t in enumerate(ts):
            psi_t = V @ (c * np.exp(-1j * eigM * t))
            rho[ti] = np.abs(psi_t) ** 2
            avg[ti] = np.sum(np.arange(len(psi0)) * rho[ti])
            var[ti] = np.sum((np.arange(len(psi0)) - avg[ti]) ** 2 * rho[ti])
        return rho, avg, np.sqrt(var)

    rho_vac, avg_vac, sig_vac = evolve(psi0, M_int, times)
    print("[Result B — wave-packet evolution under vacuum modular flow]")
    print(f"  Initial centre x={avg_vac[0]:.3f}, width σ={sig_vac[0]:.3f}")
    print(f"  Final modular t={times[-1]:.2f}: x={avg_vac[-1]:.3f}, σ={sig_vac[-1]:.3f}\n")

    # ---------- (C) Thermal vs vacuum spectra ----------
    beta = 4.0
    C_th = thermal_corr(N, beta)
    M_th = modular_M(C_th[np.ix_(interval, interval)])
    rel_diff = np.linalg.norm(M_th - M_int) / np.linalg.norm(M_int)
    eig_vac = np.sort(np.linalg.eigvalsh(M_int))
    eig_th = np.sort(np.linalg.eigvalsh(M_th))
    print("[Result C — Connes–Rovelli thermal time]")
    print(f"  ‖M_thermal − M_vacuum‖ / ‖M_vacuum‖ = {rel_diff:.4f}")
    print(f"  Vacuum spectrum range:  [{eig_vac[0]:+.2f}, {eig_vac[-1]:+.2f}]")
    print(f"  Thermal spectrum range: [{eig_th[0]:+.2f}, {eig_th[-1]:+.2f}]\n")

    # ---------- (D) Same packet, two flows ----------
    rho_th, avg_th, sig_th = evolve(psi0, M_th, times)
    trajectory_diff = np.sqrt(np.mean((avg_vac - avg_th) ** 2 + (sig_vac - sig_th) ** 2))
    print("[Result D — Distinct emergent times]")
    print(f"  Mean trajectory deviation in (⟨x⟩, σ_x) = {trajectory_diff:.4f}")
    print(f"  Vacuum final width σ = {sig_vac[-1]:.3f}")
    print(f"  Thermal final width σ = {sig_th[-1]:.3f}\n")

    # ============================================================
    # Plots
    # ============================================================
    fig = plt.figure(figsize=(15.5, 9.5))
    gs = fig.add_gridspec(2, 3)

    ax = fig.add_subplot(gs[0, 0])
    ax.plot(x_mid, hop, 'o', ms=4, label=r'numerical $|M_{i,i+1}|$')
    ax.plot(x_mid, alpha * chm, '--',
            label=fr'fit $\alpha\,(R^2-(x-x_c)^2)/R$, $\alpha={alpha:.3f}$')
    ax.plot(x_mid, (np.pi / 2) * chm, ':', alpha=0.6,
            label=r'CFT exact $\pi/2$')
    ax.set_xlabel('position in interval'); ax.set_ylabel(r'$|M_{i,i+1}|$')
    ax.set_title('(A) Casini–Huerta–Myers kernel emerges')
    ax.legend(); ax.grid(alpha=0.3)

    ax = fig.add_subplot(gs[0, 1])
    ax.hist(eig_vac, bins=40, alpha=0.5, label='vacuum')
    ax.hist(eig_th, bins=40, alpha=0.5, label=fr'thermal $\beta={beta}$')
    ax.set_xlabel('modular eigenvalue ε'); ax.set_ylabel('count')
    ax.set_title('(B) Modular spectrum is state-dependent')
    ax.legend(); ax.grid(alpha=0.3)

    ax = fig.add_subplot(gs[0, 2])
    im = ax.imshow(rho_vac.T, aspect='auto', origin='lower', cmap='magma',
                   extent=[times[0], times[-1], 0, L])
    ax.set_xlabel('modular time t'); ax.set_ylabel('position')
    ax.set_title(r'(C) $|\psi(x,t)|^2$ under vacuum flow')
    plt.colorbar(im, ax=ax)

    ax = fig.add_subplot(gs[1, 0])
    im = ax.imshow(rho_th.T, aspect='auto', origin='lower', cmap='magma',
                   extent=[times[0], times[-1], 0, L])
    ax.set_xlabel('modular time t'); ax.set_ylabel('position')
    ax.set_title(fr'(D) $|\psi(x,t)|^2$ under thermal $\beta={beta}$ flow')
    plt.colorbar(im, ax=ax)

    ax = fig.add_subplot(gs[1, 1])
    ax.plot(times, sig_vac, label='vacuum σ_x(t)')
    ax.plot(times, sig_th, label=fr'thermal $\beta={beta}$ σ_x(t)')
    ax.set_xlabel('modular time t'); ax.set_ylabel('packet width σ_x')
    ax.set_title('(E) State-dependent expansion: emergent time')
    ax.legend(); ax.grid(alpha=0.3)

    ax = fig.add_subplot(gs[1, 2])
    ax.plot(avg_vac, sig_vac, '-', label='vacuum trajectory')
    ax.plot(avg_th, sig_th, '-', label=fr'thermal $\beta={beta}$ trajectory')
    ax.scatter([avg_vac[0]], [sig_vac[0]], s=80, color='C0', marker='*', zorder=5)
    ax.scatter([avg_vac[-1]], [sig_vac[-1]], s=80, color='C0', marker='o', zorder=5)
    ax.scatter([avg_th[0]], [sig_th[0]], s=80, color='C1', marker='*', zorder=5)
    ax.scatter([avg_th[-1]], [sig_th[-1]], s=80, color='C1', marker='o', zorder=5)
    ax.set_xlabel(r'$\langle x \rangle (t)$'); ax.set_ylabel(r'$\sigma_x(t)$')
    ax.set_title('(F) Trajectories in moment space')
    ax.legend(); ax.grid(alpha=0.3)

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\modular_flow_time.png'
    plt.savefig(out, dpi=130)
    print(f"Figure saved to {out}")

    import json
    summary = {
        'CHM_alpha_fit': float(alpha),
        'CHM_alpha_predicted': np.pi / 2,
        'CHM_ratio': float(alpha / (np.pi / 2)),
        'CHM_endpoint_left': float(hop[0]),
        'CHM_endpoint_right': float(hop[-1]),
        'CHM_peak_value': float(hop.max()),
        'wavepacket_initial_sigma': float(sig_vac[0]),
        'wavepacket_final_sigma_vacuum': float(sig_vac[-1]),
        'wavepacket_final_sigma_thermal': float(sig_th[-1]),
        'thermal_M_relative_diff': float(rel_diff),
        'trajectory_deviation_vac_vs_thermal': float(trajectory_diff),
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase4.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print('Summary saved.')

if __name__ == '__main__':
    main()
