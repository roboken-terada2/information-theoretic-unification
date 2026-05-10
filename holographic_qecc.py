"""
Phase 5: Holographic quantum error correction with the [[5,1,3]] code.

Demonstrates the Almheiri–Dong–Harlow (2014) picture: the holographic
bulk is a quantum error-correcting code on the boundary, where
  • a logical bulk qubit is recoverable from any boundary subset that
    falls inside its entanglement wedge,
  • the mutual information I(A : R) between boundary subset A and a
    reference R purifying the bulk shows a SHARP RYU–TAKAYANAGI-LIKE
    PHASE TRANSITION.

For [[5,1,3]] (distance 3, perfect tensor):
        I(A : R) = 0      for |A| ≤ 2
        I(A : R) = 2 bits for |A| ≥ 3
The transition is the discrete analog of the Ryu–Takayanagi minimal
surface jumping from the A side to the A^c side as |A| crosses 5/2.

References:
- Bennett, DiVincenzo, Smolin, Wootters, PRA 54 (1996) 3824
- Almheiri, Dong, Harlow, JHEP 2015:163
- Pastawski, Yoshida, Harlow, Preskill, JHEP 2015:149
- Hayden, Penington, Walter, JHEP 2016:09
"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def kron(*ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out

# ---------------------------------------------------------------
# [[5,1,3]] stabilizers and logical operators
# ---------------------------------------------------------------
g1 = kron(X, Z, Z, X, I2)
g2 = kron(I2, X, Z, Z, X)
g3 = kron(X, I2, X, Z, Z)
g4 = kron(Z, X, I2, X, Z)
LX = kron(X, X, X, X, X)
LZ = kron(Z, Z, Z, Z, Z)

def code_projector():
    P = np.eye(32, dtype=complex)
    for g in (g1, g2, g3, g4):
        P = P @ ((np.eye(32) + g) / 2)
    return P

# ---------------------------------------------------------------
# Density-matrix utilities
# ---------------------------------------------------------------
def vn_entropy_bits(rho):
    eigs = np.linalg.eigvalsh(rho)
    eigs = eigs[eigs > 1e-12]
    return float(-np.sum(eigs * np.log2(eigs)))

def partial_trace(rho, traced_qubits, n):
    """Trace out qubits in `traced_qubits` from a 2^n × 2^n density matrix.
    Qubits indexed 0..n-1, with qubit 0 the leftmost in our kron convention."""
    if not traced_qubits:
        return rho.copy()
    keep = [i for i in range(n) if i not in traced_qubits]
    rho_t = rho.reshape([2] * (2 * n))
    chars = 'abcdefghijklmnopqrstuvwxyz'
    bra = chars[:n]
    ket = chars[n:2 * n]
    in_str = bra + ''.join(bra[i] if i in traced_qubits else ket[i] for i in range(n))
    out_str = ''.join(bra[i] for i in keep) + ''.join(ket[i] for i in keep)
    return np.einsum(in_str + '->' + out_str, rho_t).reshape(
        (2 ** len(keep), 2 ** len(keep)))

# ---------------------------------------------------------------
# Build the encoded Bell pair on (5 boundary) ⊗ R
# ---------------------------------------------------------------
def build_state():
    P = code_projector()
    phi0 = np.zeros(32, dtype=complex); phi0[0] = 1.0
    psi0L = P @ phi0
    psi0L /= np.linalg.norm(psi0L)
    psi1L = P @ (LX @ phi0)
    psi1L /= np.linalg.norm(psi1L)

    # Joint state (boundary ⊗ R), R = qubit 5
    psi = np.zeros((32, 2), dtype=complex)
    psi[:, 0] = psi0L / np.sqrt(2)
    psi[:, 1] = psi1L / np.sqrt(2)
    psi = psi.reshape(64)
    rho = np.outer(psi, psi.conj())
    return rho, psi0L, psi1L

# ---------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------
def main():
    print("=== Phase 5: Holographic Quantum Error Correction ===\n")
    rho_full, psi0L, psi1L = build_state()
    print(f"<0_L|0_L>={abs(np.vdot(psi0L,psi0L)):.4f}, "
          f"<1_L|1_L>={abs(np.vdot(psi1L,psi1L)):.4f}, "
          f"<0_L|1_L>={abs(np.vdot(psi0L,psi1L)):.2e}\n")

    # Reduced state of R alone
    rho_R = partial_trace(rho_full, list(range(5)), 6)
    S_R = vn_entropy_bits(rho_R)
    print(f"S(R) = {S_R:.4f} bits  (expected 1 bit for max-entangled bulk)\n")

    # ---- I(A : R) phase transition ----
    print("[Result A — I(A : R) phase transition]")
    print(" |A|  | I(A:R) min  | I(A:R) max  | RT prediction")
    Acc_results = []
    for k in range(0, 6):
        Is = []
        Ss = []
        for A in combinations(range(5), k):
            traced_for_A = [i for i in range(6) if i not in A]
            traced_for_AR = [i for i in range(6) if i not in (list(A) + [5])]
            rho_A = partial_trace(rho_full, traced_for_A, 6)
            rho_AR = partial_trace(rho_full, traced_for_AR, 6)
            S_A = vn_entropy_bits(rho_A) if A else 0.0
            S_AR = vn_entropy_bits(rho_AR)
            I_AR = S_A + S_R - S_AR
            Is.append(I_AR); Ss.append(S_A)
            Acc_results.append({'k': k, 'A': A, 'S_A': S_A, 'I_AR': I_AR})
        if Is:
            pred = 0.0 if k <= 2 else 2.0
            print(f"  {k}   |  {min(Is):.4f}   |  {max(Is):.4f}   |   {pred} bits")
    print()

    # ---- Boundary entanglement entropy S(A) ----
    rho_bound = partial_trace(rho_full, [5], 6)
    print("[Result B — Boundary entanglement S(A)]")
    print(" |A|  | S(A) min | S(A) max | perfect-tensor prediction")
    boundary_S = []
    for k in range(0, 6):
        Ss = []
        for A in combinations(range(5), k):
            traced = [i for i in range(5) if i not in A]
            rho_A = partial_trace(rho_bound, traced, 5) if A else np.array([[1.0]])
            S_A = vn_entropy_bits(rho_A) if A else 0.0
            Ss.append(S_A)
        # perfect-tensor part of the codeword: min(k, 5-k)
        # mixed-bulk adds an extra purifying qubit; for our state
        # the prediction is min(k, 6-k) by purity over (boundary+R)
        pred = min(k, 6 - k)
        boundary_S.append((k, np.array(Ss)))
        if Ss:
            print(f"  {k}   | {min(Ss):.4f} | {max(Ss):.4f} | {pred} bits")
    print()

    # ---- Bulk operator reconstruction in 3-subsets (Petz-recovery flavour) ----
    print("[Result C — Bulk operators reconstructed from 3-subsets]")
    # If any 3-subset A can recover the logical, then there exists O_A ∈ Alg(A)
    # such that O_A acts on |0_L⟩, |1_L⟩ as Pauli X.  We verify this by checking
    # that for every 3-subset A, the reduced overlap structure preserves
    # distinguishability of |0_L⟩ vs |1_L⟩.
    rho_0 = np.outer(psi0L, psi0L.conj())
    rho_1 = np.outer(psi1L, psi1L.conj())
    print("  Trace distance between codeword reductions (1 bit ≡ perfect distinguishability):")
    print("  |A|  | min ‖ρ_A^{|0⟩} − ρ_A^{|1⟩}‖_1/2 | max ‖…‖_1/2")
    for k in range(0, 6):
        ds = []
        for A in combinations(range(5), k):
            traced = [i for i in range(5) if i not in A]
            r0 = partial_trace(rho_0, traced, 5) if A else np.array([[1.0]])
            r1 = partial_trace(rho_1, traced, 5) if A else np.array([[1.0]])
            d = 0.5 * np.sum(np.abs(np.linalg.eigvalsh(r0 - r1)))
            ds.append(d)
        if ds:
            tag = '← bulk recoverable' if min(ds) > 0.99 else (
                  '← bulk hidden' if max(ds) < 1e-6 else '')
            print(f"  {k}   |  {min(ds):.4f}                       |  {max(ds):.4f}   {tag}")
    print()

    # =========================================================
    # Plots
    # =========================================================
    fig = plt.figure(figsize=(15.5, 9.5))
    gs = fig.add_gridspec(2, 3)

    # (A) I(A:R) vs |A|
    ax = fig.add_subplot(gs[0, 0])
    ks = [r['k'] for r in Acc_results]
    Is = [r['I_AR'] for r in Acc_results]
    rng = np.random.default_rng(0)
    jitter = rng.uniform(-0.13, 0.13, size=len(ks))
    ax.scatter(np.array(ks) + jitter, Is, alpha=0.6, s=30, label='all subsets A')
    ax.step([0, 2, 3, 5], [0, 0, 2, 2], 'k--', where='post', label='RT prediction')
    ax.set_xticks(range(6))
    ax.set_xlabel('|A| (boundary subset size)'); ax.set_ylabel('I(A:R)  [bits]')
    ax.set_title('(A) Holographic phase transition I(A:R)')
    ax.legend(); ax.grid(alpha=0.3)

    # (B) S(A) vs |A|
    ax = fig.add_subplot(gs[0, 1])
    for k, Ss in boundary_S:
        ax.scatter([k] * len(Ss), Ss, alpha=0.6, s=30, color='C1')
    pred_x = list(range(6))
    pred_y = [min(k, 6 - k) for k in pred_x]
    ax.plot(pred_x, pred_y, 'k--', label='min(|A|, 6-|A|) bits (RT)')
    ax.set_xticks(range(6))
    ax.set_xlabel('|A|'); ax.set_ylabel('S(A) [bits]')
    ax.set_title('(B) Boundary entanglement entropy')
    ax.legend(); ax.grid(alpha=0.3)

    # (C) Pentagon visualisation
    ax = fig.add_subplot(gs[0, 2])
    angles = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, 6)[:-1]
    bx = np.cos(angles); by = np.sin(angles)
    bulk_x, bulk_y = 0.0, 0.0
    # Edge connections
    for i in range(5):
        ax.plot([bx[i], bx[(i + 1) % 5]], [by[i], by[(i + 1) % 5]], 'k-', alpha=0.3)
    for i in range(5):
        ax.plot([bulk_x, bx[i]], [bulk_y, by[i]], 'gray', alpha=0.4, lw=0.6)
    # Highlight an example 3-subset (entanglement wedge)
    A_demo = [0, 1, 2]
    ax.fill([bx[i] for i in A_demo] + [bulk_x], [by[i] for i in A_demo] + [bulk_y],
            alpha=0.2, color='C2', label=f'wedge of A={tuple(A_demo)}')
    for i in range(5):
        col = 'C2' if i in A_demo else 'C3'
        ax.scatter([bx[i]], [by[i]], s=200, color=col, edgecolor='k', zorder=4)
        ax.annotate(f'{i}', (bx[i] * 1.18, by[i] * 1.18), ha='center',
                    fontsize=11, fontweight='bold')
    ax.scatter([bulk_x], [bulk_y], s=300, color='gold', edgecolor='k',
               marker='*', zorder=5, label='bulk qubit')
    ax.set_aspect('equal')
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
    ax.axis('off')
    ax.set_title('(C) Pentagon: bulk in 3-wedge')
    ax.legend(loc='lower center', fontsize=8)

    # (D) Distinguishability of codewords vs |A|
    ax = fig.add_subplot(gs[1, 0])
    dists_by_k = {}
    for k in range(6):
        ds = []
        for A in combinations(range(5), k):
            traced = [i for i in range(5) if i not in A]
            r0 = partial_trace(rho_0, traced, 5) if A else np.array([[1.0]])
            r1 = partial_trace(rho_1, traced, 5) if A else np.array([[1.0]])
            ds.append(0.5 * np.sum(np.abs(np.linalg.eigvalsh(r0 - r1))))
        dists_by_k[k] = ds
        if ds:
            ax.scatter([k] * len(ds), ds, alpha=0.6, s=30, color='C0')
    ax.step([0, 2, 3, 5], [0, 0, 1, 1], 'k--', where='post',
            label='predicted: 0 for |A|≤2, 1 for |A|≥3')
    ax.set_xticks(range(6))
    ax.set_xlabel('|A|')
    ax.set_ylabel(r'$\frac{1}{2}\,\|\rho_A^{|0_L\rangle} - \rho_A^{|1_L\rangle}\|_1$')
    ax.set_title('(D) Codeword distinguishability — bulk recoverability')
    ax.legend(); ax.grid(alpha=0.3)

    # (E) Mutual info heatmap over all 32 subsets
    ax = fig.add_subplot(gs[1, 1])
    subset_codes = []
    Is_all = []
    for k in range(6):
        for A in combinations(range(5), k):
            mask = sum(1 << i for i in A)
            subset_codes.append(mask)
            traced_for_A = [i for i in range(6) if i not in A]
            traced_for_AR = [i for i in range(6) if i not in (list(A) + [5])]
            rho_A = partial_trace(rho_full, traced_for_A, 6)
            rho_AR = partial_trace(rho_full, traced_for_AR, 6)
            S_A = vn_entropy_bits(rho_A) if A else 0.0
            S_AR = vn_entropy_bits(rho_AR)
            Is_all.append(S_A + S_R - S_AR)
    order = np.argsort(subset_codes)
    Is_all = np.array(Is_all)[order]
    subset_codes = np.array(subset_codes)[order]
    ax.bar(range(32), Is_all,
           color=['C2' if v > 1.0 else 'C3' for v in Is_all])
    ax.set_xlabel('subset index (5-bit binary)')
    ax.set_ylabel('I(A:R) [bits]')
    ax.set_title('(E) All 2⁵ subsets — sharp binary classification')
    ax.grid(alpha=0.3, axis='y')

    # (F) Summary text
    ax = fig.add_subplot(gs[1, 2])
    ax.axis('off')
    ax.text(0, 1, """The Almheiri–Dong–Harlow picture realised here:

  bulk locality  ⇔  redundant boundary
                    encoding  ⇔  QECC

[[5,1,3]] is the minimal perfect-tensor
holographic code:
  • 1 bulk qubit
  • 5 boundary qubits
  • distance 3

Entanglement-wedge reconstruction:
  bulk qubit recoverable from any
  boundary subset of size 3 or larger.

Phase transition at |A| = 5/2 is the
discrete RT minimal surface jump.

Same structure as MERA in Phase 3,
holographic shadows of Phase 1 geometry,
gravitational dynamics from Phase 2,
modular time of Phase 4 — all
unified by the QECC view.""",
            fontfamily='monospace', fontsize=8.5, va='top')

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\holographic_qecc.png'
    plt.savefig(out, dpi=130)
    print(f"Figure saved to {out}")

    import json
    summary = {
        'code': '[[5,1,3]]',
        'phase_transition_predicted': {'|A|<=2': 0.0, '|A|>=3': 2.0},
        'I_AR_by_subset_size': {
            str(k): {
                'min': float(min(r['I_AR'] for r in Acc_results if r['k'] == k)),
                'max': float(max(r['I_AR'] for r in Acc_results if r['k'] == k)),
            }
            for k in range(6)
        },
        'codeword_trace_distance_by_k': {
            str(k): {'min': float(min(ds)), 'max': float(max(ds))}
            for k, ds in dists_by_k.items() if ds
        },
        'S_R_bits': float(S_R),
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase5.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print('Summary saved.')

if __name__ == '__main__':
    main()
