"""
Phase 6: Page curve and the resolution of the black-hole information paradox.

Demonstrates numerically that for Haar-random pure states of n qubits, the
entanglement entropy of a subsystem of size k follows the Page formula
   ⟨S(k)⟩ ≈ min(k, n-k) log 2 − (correction)
which is the discrete analog of the Page curve, contradicting Hawking's
monotonically-increasing radiation entropy.

We also model an evaporating BH coupled to a reference R via a Bell pair
that purifies the bulk: the encoded radiation entropy traces a
characteristic "island formula" curve identical to the Page curve.

References:
- Page, PRL 71 (1993) 1291  -- average entropy of subsystems
- Hayden, Preskill, JHEP 2007:120  -- BH as a fast scrambler
- Penington, JHEP 2020:002  -- replica wormholes / island formula
- Almheiri, Engelhardt, Marolf, Maxfield, JHEP 2020:13  -- entropy of Hawking radiation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import qr

# ----------------------------------------------------------------
def haar_random_pure(d, rng):
    """Sample a Haar-random pure state in C^d (uniform on the sphere)."""
    psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    return psi / np.linalg.norm(psi)

def vn_entropy_bits(rho):
    eigs = np.linalg.eigvalsh(rho)
    eigs = eigs[eigs > 1e-12]
    return float(-np.sum(eigs * np.log2(eigs)))

def entropy_from_pure_svd(psi, k_keep, n):
    """Schmidt-decomposition entropy: O(min(d_A, d_B)^2 max).  Much faster
    than building the d_A × d_A reduced density matrix."""
    M = psi.reshape((2 ** k_keep, 2 ** (n - k_keep)))
    s = np.linalg.svd(M, compute_uv=False)
    p = s ** 2
    p = p[p > 1e-12]
    return float(-np.sum(p * np.log2(p)))

def reduced_density_from_pure(psi, k_keep, n):
    """psi: pure state on n qubits.  Trace out the LAST n-k_keep qubits."""
    psi_t = psi.reshape((2 ** k_keep, 2 ** (n - k_keep)))
    return psi_t @ psi_t.conj().T

def page_average(k, n):
    """Page's exact average entropy in nats (1993):
       <S> = sum_{j=d_A+1}^{d_A d_B} 1/j  − (d_A − 1)/(2 d_B), with d_A ≤ d_B."""
    dA = 2 ** k
    dB = 2 ** (n - k)
    if dA > dB:
        dA, dB = dB, dA
    s_nats = 0.0
    for j in range(dB + 1, dA * dB + 1):
        s_nats += 1.0 / j
    s_nats -= (dA - 1) / (2 * dB)
    return s_nats / np.log(2)         # convert to bits

# ----------------------------------------------------------------
def main():
    print("=== Phase 6: Page Curve from Haar-Random Pure States ===\n")
    n = 12
    n_samples = 60
    rng = np.random.default_rng(42)

    # Sample many Haar pure states; for each, compute S(k) for k=0..n.
    print(f"  System size n = {n} qubits, samples = {n_samples}")
    Ss_all = np.zeros((n_samples, n + 1))
    for s in range(n_samples):
        psi = haar_random_pure(2 ** n, rng)
        for k in range(n + 1):
            if k == 0 or k == n:
                Ss_all[s, k] = 0.0
            else:
                Ss_all[s, k] = entropy_from_pure_svd(psi, k, n)

    S_mean = Ss_all.mean(axis=0)
    S_std = Ss_all.std(axis=0)

    # Page exact prediction
    page_pred = np.array([page_average(k, n) for k in range(n + 1)])
    # Hawking's incorrect "thermal" prediction (monotonic linear up to n)
    hawking_pred = np.minimum(np.arange(n + 1), n) * 1.0  # k bits up to n

    # Print results
    print("\n[Result A — Page curve from Haar-random ensemble]")
    print(" k | <S(k)> num. | Page exact | Hawking | dev.(num−Page) ")
    for k in range(n + 1):
        print(f" {k:2d} | {S_mean[k]:7.4f}    | {page_pred[k]:7.4f}    "
              f"| {hawking_pred[k]:5.2f}  | {S_mean[k]-page_pred[k]:+.4f}")

    # Page time: where the curve is maximum
    page_time = np.argmax(S_mean)
    print(f"\n  Page time (peak of S(k)): k = {page_time}  (predicted: n/2 = {n/2})")
    print(f"  Peak entropy = {S_mean[page_time]:.3f} bits")
    print(f"  Hawking would predict a monotonic curve reaching {n} bits at k={n}.")
    print(f"  → Information is recovered after the Page time.\n")

    # =============================================================
    # Now the *evaporating BH* model with a reference qubit
    # =============================================================
    # n_b BH qubits, n_R radiation slots (= n - n_b).
    # An auxiliary reference R is Bell-paired with one BH qubit.
    # We then evolve via Haar random unitaries on (BH+R-bell).
    n_total = 10
    n_ref = 1
    rng2 = np.random.default_rng(7)
    samples = 80
    radiation_curve = np.zeros(n_total + 1)
    radiation_std = np.zeros(n_total + 1)

    # initial state: (Bell pair between BH qubit 0 and R) ⊗ |0...0> on remaining BH qubits
    # = Bell on (q0, qR) with the other qubits in |0⟩.
    bell = (np.kron([1, 0], [1, 0]) + np.kron([0, 1], [0, 1])) / np.sqrt(2)
    init_other = np.zeros(2 ** (n_total - 1)); init_other[0] = 1.0
    # Order qubits: (q0, q1, ..., q_{n_total-1}, R)
    psi0 = np.kron(bell[:2 * 2:2].reshape(-1), init_other)  # rough, fix below
    # Build properly: psi_full(i_R, i_0, i_1, ..., i_{n_total-1}) with bell on (i_0, i_R)
    # Simpler: tensor the Bell state on (q0, qR) and identity-like |0> on rest.
    # Index ordering: q0, q1, ..., q_{n-1}, qR
    # Then bell relates q0 and qR; q1..q_{n-1} are |0⟩.
    psi_full = np.zeros((2,) * n_total + (2,), dtype=complex)
    # bell coefficient on (q0=0, qR=0) and (q0=1, qR=1); other qubits = 0
    idx0 = (0,) * (n_total) + (0,)
    psi_full[idx0] = 1 / np.sqrt(2)
    idx1 = (1,) + (0,) * (n_total - 1) + (1,)
    psi_full[idx1] = 1 / np.sqrt(2)
    psi_init = psi_full.reshape(2 ** (n_total + 1))

    Ss_evap = np.zeros((samples, n_total + 1))
    for s in range(samples):
        U_bh = haar_random_unitary(2 ** n_total, rng2)
        U_full = np.kron(U_bh, np.eye(2))
        psi = U_full @ psi_init
        # "Radiation" = first k qubits of BH after scrambling are emitted.
        # Bipartition: kept = (q_0..q_{k-1}, R), traced = (q_k..q_{n-1}).
        for k in range(n_total + 1):
            keep = list(range(0, k)) + [n_total]
            traced = list(range(k, n_total))
            psi_t = psi.reshape((2,) * (n_total + 1))
            order = keep + traced
            psi_t = np.transpose(psi_t, order)
            M = psi_t.reshape((2 ** len(keep), 2 ** len(traced)))
            s_vals = np.linalg.svd(M, compute_uv=False)
            p = s_vals ** 2
            p = p[p > 1e-12]
            Ss_evap[s, k] = float(-np.sum(p * np.log2(p)))
    S_evap_mean = Ss_evap.mean(axis=0)
    S_evap_std = Ss_evap.std(axis=0)

    print("[Result B — Evaporating-BH model with reference R]")
    print(" k=|radiation| | <S_R(k)> | island prediction min(k+1, n_total+1-k) ")
    for k in range(n_total + 1):
        pred = min(k + 1, n_total + 1 - k)
        print(f"   {k:2d}        | {S_evap_mean[k]:6.3f}   | {pred}")
    page_time_2 = int(np.argmax(S_evap_mean))
    print(f"\n  Page time of evaporation = {page_time_2}\n")

    # ------------------------------------------------------------
    # Plots
    # ------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    ax = axes[0]
    ax.errorbar(range(n + 1), S_mean, yerr=S_std, fmt='o', ms=5, capsize=3,
                label=f'Haar avg (samples={n_samples})')
    ax.plot(range(n + 1), page_pred, '-', label='Page exact')
    ax.plot(range(n + 1), hawking_pred, '--', color='red', label="Hawking (monotonic)")
    ax.set_xlabel('|R| (radiation qubits)')
    ax.set_ylabel('S(R) [bits]')
    ax.set_title(f'(A) Page curve, n = {n}')
    ax.legend(); ax.grid(alpha=0.3)

    ax = axes[1]
    ax.errorbar(range(n_total + 1), S_evap_mean, yerr=S_evap_std,
                fmt='o', ms=5, capsize=3,
                label=f'numerics (samples={samples})')
    pred_curve = [min(k + 1, n_total + 1 - k) for k in range(n_total + 1)]
    ax.plot(range(n_total + 1), pred_curve, '-', label='island prediction')
    hawk = list(range(n_total + 1))  # would-be monotonic
    hawk[0] = 1  # since the reference is already entangled
    ax.plot(range(n_total + 1), hawk, '--', color='red', label='Hawking')
    ax.set_xlabel('# qubits emitted')
    ax.set_ylabel(r'$S(R \cup \text{emitted})$ [bits]')
    ax.set_title('(B) Evaporating BH with reference qubit (island formula)')
    ax.legend(); ax.grid(alpha=0.3)

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\page_curve.png'
    plt.savefig(out, dpi=130)
    print(f"Figure saved to {out}")

    import json
    summary = {
        'n_qubits': n,
        'samples_haar': n_samples,
        'page_peak_k': int(page_time),
        'page_peak_S_bits': float(S_mean[page_time]),
        'page_predicted_peak_S_bits': float(page_pred[page_time]),
        'hawking_predicted_peak': float(hawking_pred[-1]),
        'evap_n_total': n_total,
        'evap_samples': samples,
        'evap_page_time': int(page_time_2),
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase6.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print('Summary saved.')


def haar_random_unitary(d, rng):
    """Haar-random unitary in U(d)."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = qr(A)
    D = np.diag(np.diag(R) / np.abs(np.diag(R)))
    return Q @ D


if __name__ == '__main__':
    main()
