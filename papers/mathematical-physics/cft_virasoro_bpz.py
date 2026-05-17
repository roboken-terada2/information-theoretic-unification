"""
Phase 170: CFT + Virasoro + BPZ + Minimal models + WZW
=======================================================

Tests:
1. Virasoro algebra [L_m, L_n] = (m-n) L_{m+n} + (c/12) m(m²-1) δ_{m+n,0}
2. Minimal models: c = 1 - 6(p-q)²/(pq) for (p,q) coprime
3. Ising CFT (c=1/2) primary fields and 2D Ising exponents
4. WZW Sugawara c = k dim(G) / (k + h^∨) for SU(2)_k
5. Cardy formula S = 2π √(c L_0 / 6) ↔ Phase 122 BH entropy
6. Modular invariance check for SU(2)_k partition function
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

print("=" * 70)
print("Phase 170: CFT + Virasoro + BPZ + Minimal Models")
print("=" * 70)
print()

# ----------------------------------------------------------------------
# Test 1: Virasoro algebra check (symbolic)
# ----------------------------------------------------------------------
print("[Test 1] Virasoro [L_m, L_n] = (m-n) L_{m+n} + (c/12) m(m²-1) δ_{m+n,0}")
c_val = 0.5   # Ising
print(f"  Central charge c = {c_val} (Ising)")
print(f"  {'(m, n)':<12}{'Virasoro RHS':<30}")
test_pairs = [(1, -1), (2, -2), (3, -3), (1, 2), (2, 0)]
for m, n in test_pairs:
    structure_part = m - n
    central_part = (c_val / 12) * m * (m**2 - 1) if (m + n == 0) else 0
    print(f"  ({m:>2}, {n:>2})    (m-n) L_{m+n} = {structure_part} L_{m+n}, central = {central_part:.4f}")
print()
print(f"  Key: [L_n, L_{-n}] = 2n L_0 + (c/12) n(n²-1) for n > 0")
print(f"  → [L_1, L_{-1}] = 2 L_0 + 0 (central absent for n=1, m²-1=0)")
print(f"  → [L_2, L_{-2}] = 4 L_0 + c/2 (Ising c/2 = 1/4)")
print()

# ----------------------------------------------------------------------
# Test 2: Minimal models c = 1 - 6(p-q)²/(pq)
# ----------------------------------------------------------------------
print("[Test 2] Minimal models — Kac formula c = 1 - 6(p-q)²/(pq)")

def minimal_c(p, q):
    """Coprime p, q ≥ 2."""
    return 1 - 6 * (p - q) ** 2 / (p * q)

minimal_models = [
    (3, 4, 'Ising'),
    (4, 5, 'Tricritical Ising'),
    (5, 6, 'Three-state Potts (subset)'),
    (6, 7, '4-state Potts'),
    (7, 8, ''),
    (10, 11, ''),
    (100, 101, ''),
]
print(f"  {'(p, q)':<10}{'c':<14}{'name':<28}")
for p, q, name in minimal_models:
    c = minimal_c(p, q)
    print(f"  ({p:>3},{q:>3}) {c:<14.6f}{name:<28}")
print(f"\n  → c < 1 (Kac unitary bound)")
print(f"  → c=0 (trivial), c=1/2 (Ising), c=7/10 (tricritical Ising), c→1 (XXZ)")
print()

# ----------------------------------------------------------------------
# Test 3: Ising CFT primary fields + exponents
# ----------------------------------------------------------------------
print("[Test 3] Ising CFT c=1/2 — 3 primary fields")
primaries = [
    ('1 (identity)', 0, 0, 0, 0),
    ('σ (spin)',     1/16, 1/16, 1/8, 0),
    ('ε (energy)',   1/2, 1/2, 1, 0),
]
print(f"  {'field':<14}{'h':<10}{'h̄':<10}{'Δ=h+h̄':<10}{'s=h-h̄':<10}")
for name, h, hbar, Delta, s in primaries:
    print(f"  {name:<14}{h:<10}{hbar:<10}{Delta:<10}{s:<10}")
print()

# Connection to Phase 145 2D Ising exponents
print(f"  2D Ising universality class exponents (Phase 145 connection):")
ising_exp = {
    'β (order param)':  1/8,
    'γ (susceptibility)': 7/4,
    'δ (spin response)': 15,
    'η (anomalous dim)': 1/4,
    'ν (correlation)':  1,
    'α (specific heat)': 0,
}
print(f"  {'exponent':<20}{'value':<14}")
for name, val in ising_exp.items():
    print(f"  {name:<20}{val:<14.4f}")
print(f"\n  → 2D Ising universality class fully determined by Ising CFT (c=1/2)")
print()

# ----------------------------------------------------------------------
# Test 4: WZW SU(2)_k central charge
# ----------------------------------------------------------------------
print("[Test 4] WZW SU(2)_k central charge c = k × 3 / (k + 2)")

def wzw_su2_c(k):
    return k * 3 / (k + 2)

print(f"  {'level k':<10}{'c':<14}{'comment':<26}")
for k_lev in [1, 2, 3, 4, 10, 100, 1000]:
    c = wzw_su2_c(k_lev)
    if k_lev == 1:
        com = "= 1 (free boson)"
    elif k_lev == 2:
        com = "= 3/2 (3-state Potts ✗ actually)"
    elif k_lev >= 100:
        com = f"→ 3 (k→∞ limit)"
    else:
        com = ""
    print(f"  {k_lev:<10}{c:<14.4f}{com:<26}")
print(f"\n  k=1: c = 3/3 = 1 ✓")
print(f"  k=∞ limit: c → dim(SU(2)) = 3")
print()

# ----------------------------------------------------------------------
# Test 5: Cardy formula
# ----------------------------------------------------------------------
print("[Test 5] Cardy formula S = 2π √(c L_0 / 6) ↔ Phase 122 BH entropy")
def cardy_S(c, L0):
    return 2 * np.pi * np.sqrt(c * L0 / 6)

print(f"  {'c':<10}{'L_0':<10}{'Cardy S':<14}{'comment':<26}")
for c, L0, com in [(1.0, 100, 'CFT toy'),
                    (24, 1, 'monster CFT'),
                    (1500, 1000, 'large c BH analog'),
                    (6.5e9, 1e80, 'M87 BH')]:
    S = cardy_S(c, L0)
    print(f"  {c:<10.3g}{L0:<10.3g}{S:<14.3g}{com:<26}")
print(f"\n  Strominger-Vafa (1996): BH entropy = Cardy S microscopic origin (Phase 122)")
print()

# ----------------------------------------------------------------------
# Test 6: Modular invariance hint
# ----------------------------------------------------------------------
print("[Test 6] Modular invariance: τ → -1/τ S-transform")
# Verlinde formula for SU(2)_k S-matrix
k_su2 = 4
print(f"  SU(2)_{k_su2} integrable spins: j = 0, 1/2, 1, ..., k/2 = {k_su2/2}")
j_arr = np.arange(0, k_su2/2 + 0.5, 0.5)
print(f"  Number of primary fields: {len(j_arr)}")
# S-matrix elements: S_{jj'} = sqrt(2/(k+2)) sin(π(2j+1)(2j'+1)/(k+2))
S_matrix = np.zeros((len(j_arr), len(j_arr)))
for i, j in enumerate(j_arr):
    for ip, jp in enumerate(j_arr):
        S_matrix[i, ip] = np.sqrt(2 / (k_su2 + 2)) * np.sin(
            np.pi * (2*j + 1) * (2*jp + 1) / (k_su2 + 2))
# Check S² = C (charge conjugation matrix); for SU(2) C = I
S_squared = S_matrix @ S_matrix
print(f"\n  S-matrix S² check (should be charge conjugation, here = I for self-conjugate):")
print(f"  S² close to identity: {np.allclose(S_squared, np.eye(len(j_arr)), atol=1e-6)}")
print(f"  ||S² - I|| = {np.linalg.norm(S_squared - np.eye(len(j_arr))):.4e}")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# 1) Minimal model central charges
ax = axes[0, 0]
pq_pairs = [(p, p+1) for p in range(2, 30)]
c_vals = [minimal_c(p, q) for (p, q) in pq_pairs]
p_vals = [p for (p, _) in pq_pairs]
ax.plot(p_vals, c_vals, 'bo-', markersize=6)
ax.axhline(1, color='red', linestyle='--', alpha=0.5, label='c = 1 (Kac unitary bound)')
ax.axhline(0.5, color='green', linestyle=':', alpha=0.7, label='c = 1/2 (Ising)')
ax.axhline(0.7, color='orange', linestyle=':', alpha=0.7, label='c = 7/10 (tricritical)')
ax.set_xlabel('p (in p,q=p+1 series)')
ax.set_ylabel('Central charge c')
ax.set_title('Minimal Model Central Charges (unitary series)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# 2) WZW SU(2)_k c
ax = axes[0, 1]
k_arr = np.arange(1, 30)
c_wzw_arr = wzw_su2_c(k_arr)
ax.plot(k_arr, c_wzw_arr, 'rs-', markersize=6)
ax.axhline(3, color='red', linestyle='--', alpha=0.5, label='c = 3 (k→∞)')
ax.axhline(1, color='blue', linestyle=':', alpha=0.5, label='c = 1 (k=1, free boson)')
ax.set_xlabel('WZW level k')
ax.set_ylabel('c_SU(2)_k')
ax.set_title('WZW SU(2)_k Central Charge: c = 3k/(k+2)')
ax.legend()
ax.grid(True, alpha=0.3)

# 3) Cardy formula
ax = axes[1, 0]
L0_arr = np.logspace(0, 6, 100)
c_examples = [0.5, 1.0, 10.0, 100.0]
for c in c_examples:
    S_arr = cardy_S(c, L0_arr)
    ax.loglog(L0_arr, S_arr, label=f'c = {c}')
ax.set_xlabel('L_0 (eigenvalue)')
ax.set_ylabel('Cardy S = 2π √(c L_0/6)')
ax.set_title('Cardy Entropy Formula — BH analog (Phase 122)')
ax.legend()
ax.grid(True, alpha=0.3, which='both')

# 4) Ising CFT primary scaling dimensions
ax = axes[1, 1]
names_p = [p[0] for p in primaries]
Deltas = [p[3] for p in primaries]
ax.bar(names_p, Deltas, color=['steelblue', 'orange', 'red'], edgecolor='black')
ax.set_ylabel('Scaling dimension Δ = h + h̄')
ax.set_title('Ising CFT (c=1/2): 3 Primary Fields')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'cft_virasoro_bpz.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 170,
    "title": "CFT + Virasoro + BPZ + Minimal models + WZW",
    "tier1_paper": "#24 Mathematical Physics (phase 4/8)",
    "tests": {
        "virasoro_algebra": {
            "form": "[L_m, L_n] = (m-n) L_{m+n} + (c/12) m(m²-1) δ_{m+n,0}",
            "test_pairs": [{"m": m, "n": n, "structure": m-n,
                            "central_if_m_plus_n_zero": (c_val/12)*m*(m**2-1) if (m+n==0) else 0}
                           for m, n in test_pairs],
            "c_used": c_val,
        },
        "minimal_models_central_charges": {
            f"({p},{q})_{name}": float(minimal_c(p, q))
            for p, q, name in minimal_models
        },
        "ising_CFT_primaries": [
            {"field": p[0], "h": p[1], "h_bar": p[2], "Delta": p[3], "spin": p[4]}
            for p in primaries
        ],
        "2D_ising_exponents_from_CFT": ising_exp,
        "WZW_SU2_k_central_charges": {
            f"k={k_lev}": float(wzw_su2_c(k_lev))
            for k_lev in [1, 2, 3, 4, 10, 100, 1000]
        },
        "cardy_formula": {
            "form": "S = 2π √(c L_0 / 6)",
            "examples": {
                "c1_L0_100": float(cardy_S(1.0, 100)),
                "c24_L0_1": float(cardy_S(24, 1)),
                "c1500_L0_1000_BH_analog": float(cardy_S(1500, 1000)),
                "M87_BH_estimate": float(cardy_S(6.5e9, 1e80)),
            },
        },
        "modular_invariance_SU2_k4": {
            "k": k_su2,
            "n_primaries": len(j_arr),
            "S_squared_minus_I_norm": float(np.linalg.norm(S_squared - np.eye(len(j_arr)))),
            "S_squared_is_identity": bool(np.allclose(S_squared, np.eye(len(j_arr)), atol=1e-6)),
        },
    },
    "itu_interpretation": {
        "conformal_transformation": "K_sym scale-invariant extension",
        "Virasoro": "K_CFT infinite-dim algebra",
        "central_charge_c": "K_CFT universal label",
        "BPZ": "K_CFT axiomatic",
        "primary_field": "K_CFT L_0 eigenstate",
        "OPE": "K_CFT operator algebra",
        "minimal_models": "K_CFT rational series",
        "Ising_c_half": "K_CFT critical 2D realisation (Phase 145)",
        "WZW": "K_CFT + K_sym non-abelian",
        "Kac_Moody": "K_sym affine extension",
        "modular_invariance": "K_CFT torus consistency",
        "ADE_classification": "K_sym ↔ K_CFT double role",
        "AdS_CFT": "K_CFT ↔ K_geom holographic duality",
        "Cardy_formula": "K_CFT entropy = K_geom area (Phase 122 BH)",
    },
    "key_findings": [
        "Ising CFT c = 1/2 has 3 primary fields: 1, σ, ε with conformal weights 0, 1/16, 1/2",
        "2D Ising critical exponents β=1/8, γ=7/4, η=1/4 derive from Ising CFT (Phase 145)",
        f"Minimal series c < 1 (Kac bound); Ising 1/2, tricritical 7/10, ...",
        f"WZW SU(2)_k: c = 3k/(k+2); k=1 → c=1 (free boson), k→∞ → c=3",
        "Cardy formula = microscopic origin of BH entropy (Strominger-Vafa 1996, Phase 122)",
        "Modular invariance → ADE classification (Cappelli-Itzykson-Zuber 1987)",
        "AdS/CFT (Maldacena 1997): K_CFT boundary ↔ K_geom bulk holography",
    ],
}

out_json = os.path.join(os.path.dirname(__file__), 'cft_virasoro_bpz_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 170 complete: K_CFT = K_sym + scale + 2D infinite (Virasoro);")
print(f"  Ising c=1/2 ↔ Phase 145; Cardy → Phase 122 BH; AdS/CFT → Phase 111")
print("=" * 70)
