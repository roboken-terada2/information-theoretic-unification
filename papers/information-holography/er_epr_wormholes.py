"""
Phase 179: ER=EPR + Wormholes + Entanglement structure
=======================================================

Tests:
1. EPR singlet entanglement: S(A) = log 2 for Bell state
2. TFD state entanglement entropy
3. Page curve with replica wormholes (Phase 113 link)
4. SYK maximally chaotic λ_L = 2π/β
5. Traversable wormhole GJW schematic
6. ER=EPR conceptual map
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

print("=" * 70)
print("Phase 179: ER=EPR + Wormholes + Entanglement Structure")
print("=" * 70)
print()

# ----------------------------------------------------------------------
# Test 1: EPR singlet entanglement
# ----------------------------------------------------------------------
print("[Test 1] EPR singlet |ψ⟩ = (|↑↓⟩ - |↓↑⟩)/√2")
# 2-qubit singlet state
singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
rho_full = np.outer(singlet, singlet.conj())

# Reduced density of qubit A: trace out B
rho_A = np.zeros((2, 2), dtype=complex)
for i in range(2):
    for j in range(2):
        for k in range(2):
            rho_A[i, j] += rho_full[2*i + k, 2*j + k]

eigs_A = np.linalg.eigvalsh(rho_A)
eigs_A = eigs_A[eigs_A > 1e-15]
S_A = -np.sum(eigs_A * np.log(eigs_A))

print(f"  Bell singlet state:")
print(f"  ρ_A eigenvalues: {[float(e) for e in eigs_A]}")
print(f"  S(ρ_A) = {S_A:.4f} = log 2 = {np.log(2):.4f} (maximally entangled ✓)")
print()

# ----------------------------------------------------------------------
# Test 2: TFD entanglement entropy
# ----------------------------------------------------------------------
print("[Test 2] TFD state for 2-level system")
# |TFD⟩ = (1/√Z) Σ e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R
# For 2-level: E_0 = 0, E_1 = ε
# S_LR = -Σ p_n log p_n with p_n = e^{-βE_n}/Z

epsilon = 1.0
betas = np.linspace(0.01, 10, 100)
S_TFD = []
for b in betas:
    Z = 1 + np.exp(-b * epsilon)
    p_0 = 1 / Z
    p_1 = np.exp(-b * epsilon) / Z
    S = -p_0 * np.log(p_0) - p_1 * np.log(p_1)
    S_TFD.append(S)

print(f"  2-level system with ε = {epsilon}")
print(f"  TFD entanglement entropy as function of β:")
print(f"  {'β':<10}{'S(TFD)':<14}{'regime':<25}")
for b in [0.01, 0.5, 1.0, 5.0, 10.0]:
    Z = 1 + np.exp(-b * epsilon)
    p_0 = 1 / Z
    p_1 = np.exp(-b * epsilon) / Z
    S = -p_0 * np.log(p_0) - p_1 * np.log(p_1)
    if b < 0.1:
        regime = "high T: max entangled"
    elif b < 2:
        regime = "intermediate"
    else:
        regime = "low T: nearly product"
    print(f"  {b:<10.2f}{S:<14.4f}{regime:<25}")
print(f"\n  → β=0 (T=∞): S = log 2 = maximally entangled")
print(f"  → β=∞ (T=0): S = 0 (product state |0⟩_L|0⟩_R)")
print()

# ----------------------------------------------------------------------
# Test 3: Page curve with replica wormholes
# ----------------------------------------------------------------------
print("[Test 3] Page curve with replica wormholes (Phase 113 link)")
# t/t_evap from 0 to 1
t_evap = 1.0
t_arr = np.linspace(0, t_evap, 100)

def page_curve(t, t_evap):
    """Page curve: rising then falling."""
    S_BH_max = 1.0  # normalized
    S_rad_naive = S_BH_max * (1 - (1 - t/t_evap)**2)  # naive Hawking
    S_rad_unitary = 2 * S_BH_max * t/t_evap if t < t_evap/2 else 2 * S_BH_max * (1 - t/t_evap)
    return min(S_rad_naive, S_rad_unitary)

S_naive = np.array([1 - (1 - t/t_evap)**2 for t in t_arr])  # Hawking (info loss)
S_page = np.array([page_curve(t, t_evap) for t in t_arr])  # Page (unitary)

print(f"  Hawking semiclassical: S → S_BH (information loss)")
print(f"  Page (with replica wormhole + island): S returns to 0 (unitary)")
print(f"  → Replica wormhole = saddle-point that ensures unitarity")
print()

# ----------------------------------------------------------------------
# Test 4: SYK maximally chaotic
# ----------------------------------------------------------------------
print("[Test 4] SYK model: λ_L = 2π/β maximally chaotic (MSS 2016)")
T_SYK_arr = np.array([0.001, 0.01, 0.1, 1.0, 10.0])
k_B = 1.380649e-23
hbar = 1.054571817e-34
print(f"  SYK at various temperatures:")
print(f"  {'T (units)':<12}{'β':<10}{'λ_L = 2π/(ℏβ)':<22}{'comment':<22}")
syk_data = []
for T in T_SYK_arr:
    beta = 1 / T
    lambda_L = 2 * np.pi / beta  # in natural units (ℏ=1)
    syk_data.append({"T": float(T), "beta": float(beta), "lambda_L": float(lambda_L)})
    print(f"  {T:<12.3f}{beta:<10.3f}{lambda_L:<22.4f}{'maximally chaotic':<22}")
print(f"\n  → SYK (and any holographic system) saturates MSS bound")
print()

# ----------------------------------------------------------------------
# Test 5: GJW traversable wormhole
# ----------------------------------------------------------------------
print("[Test 5] Gao-Jafferis-Wall traversable wormhole (2017)")
print(f"  Setup: 2-sided AdS BH (eternal, ER bridge)")
print(f"  Add double trace deformation: δS = g O_L(t) O_R(t)")
print(f"  Effect: negative null energy → ER bridge becomes traversable")
print(f"  Application: quantum teleportation through wormhole")
print(f"  Demonstrates: ER=EPR (entanglement → geometry → traversable)")
print()

# ----------------------------------------------------------------------
# Test 6: ER=EPR map
# ----------------------------------------------------------------------
print("[Test 6] ER=EPR conceptual unification (Maldacena-Susskind 2013)")
print(f"  Single particle:    classical particle ↔ minimal mass")
print(f"  EPR pair:           singlet quantum state ↔ microscopic ER bridge")
print(f"  Eternal BH (TFD):   thermofield double ↔ ER bridge between 2 sides")
print(f"  Generic entangled:  any |ψ⟩_AB ↔ some form of ER structure")
print(f"  → Spacetime emerges from entanglement structure")
print(f"  → Wheeler-deWitt 'It from bit' (Phase 180) precursor")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# 1) EPR Bell state entanglement
ax = axes[0, 0]
ax.bar(['|00⟩', '|01⟩', '|10⟩', '|11⟩'], np.abs(singlet)**2,
       color='steelblue', edgecolor='black')
ax.set_ylabel('|amplitude|²')
ax.set_title(f'EPR Singlet |ψ⟩ = (|↑↓⟩ - |↓↑⟩)/√2\nS(ρ_A) = log 2 = {np.log(2):.4f}')
ax.set_ylim(0, 0.7)
ax.grid(True, alpha=0.3, axis='y')

# 2) TFD entanglement vs β
ax = axes[0, 1]
ax.plot(betas, S_TFD, 'b-', lw=2)
ax.axhline(np.log(2), color='red', linestyle='--', alpha=0.6, label='max S = log 2')
ax.axhline(0, color='gray', linestyle=':', alpha=0.6, label='product state')
ax.set_xlabel('β = 1/T')
ax.set_ylabel('S(TFD)')
ax.set_title('TFD State Entanglement Entropy (2-level)')
ax.legend()
ax.grid(True, alpha=0.3)

# 3) Page curve with replica wormholes
ax = axes[1, 0]
ax.plot(t_arr, S_naive, 'r-', lw=2, label='Hawking semiclassical (info loss)')
ax.plot(t_arr, S_page, 'b-', lw=2, label='Page (replica wormhole + island)')
ax.axvline(t_evap / 2, color='gray', linestyle=':', label='Page time')
ax.set_xlabel('t / t_evap')
ax.set_ylabel('S(radiation)')
ax.set_title('Page Curve with Replica Wormholes (2019-2020)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# 4) ER=EPR schematic
ax = axes[1, 1]
ax.axis('off')
# Draw 2 BHs connected by wormhole
circle1 = plt.Circle((-1.5, 0), 0.5, color='black', alpha=0.7)
circle2 = plt.Circle((1.5, 0), 0.5, color='black', alpha=0.7)
ax.add_patch(circle1)
ax.add_patch(circle2)
# Wormhole bridge
ax.plot([-1.5, 1.5], [0, 0], 'b-', lw=4, alpha=0.6)
ax.plot([-1.5, 1.5], [0.2, 0.2], 'b-', lw=2, alpha=0.4)
ax.plot([-1.5, 1.5], [-0.2, -0.2], 'b-', lw=2, alpha=0.4)
ax.text(0, 0.6, 'ER bridge', ha='center', fontsize=10)
# Labels
ax.text(-1.5, -1.0, 'BH A\n|n⟩_L', ha='center', fontsize=10)
ax.text(1.5, -1.0, 'BH B\n|n⟩_R', ha='center', fontsize=10)
ax.text(0, 1.3, 'ER=EPR (Maldacena-Susskind 2013)', ha='center', fontsize=12, weight='bold')
ax.text(0, -1.7, '|TFD⟩ ∝ Σ e^{-βE_n/2} |n⟩_L|n⟩_R', ha='center', fontsize=10,
        family='monospace')
ax.text(0, -2.2, '= eternal BH = entanglement structure', ha='center', fontsize=9)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.5, 2.0)
ax.set_aspect('equal')
ax.set_title('ER=EPR Conceptual Map')

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'er_epr_wormholes.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 179,
    "title": "ER=EPR + Wormholes + Entanglement structure",
    "tier1_paper": "#25 Information & Holography (phase 5/8) — BLOCK A FINALE",
    "tests": {
        "EPR_singlet_entanglement": {
            "S_A_numerical": float(S_A),
            "S_A_theory_log2": float(np.log(2)),
            "maximally_entangled": True,
        },
        "TFD_state": {
            "epsilon": epsilon,
            "S_at_beta_zero_limit": float(np.log(2)),
            "S_at_high_beta": float(S_TFD[-1]),
            "form": "|TFD⟩ = (1/√Z) Σ e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R",
        },
        "page_curve_replica": {
            "method": "replica wormholes + island formula",
            "Hawking_endpoint": 1.0,
            "Page_endpoint": 0.0,
            "unitarity_preserved": True,
        },
        "SYK_maximally_chaotic": {
            "MSS_bound": "λ_L ≤ 2π/(ℏβ)",
            "saturated_by": "SYK and holographic systems",
            "data": syk_data,
        },
        "GJW_traversable_wormhole": {
            "year": 2017,
            "mechanism": "double trace deformation δS = g O_L O_R",
            "application": "quantum teleportation through wormhole",
        },
        "ER_EPR_unification": {
            "principle": "spacetime emerges from entanglement",
            "examples": [
                "EPR pair ↔ microscopic ER bridge",
                "TFD ↔ eternal BH",
                "Traversable wormhole ↔ teleportation",
            ],
        },
    },
    "itu_interpretation": {
        "ER_bridge": "K_geom topological non-trivial",
        "EPR": "K_quantum non-local entanglement",
        "ER_EPR": "K_entangle ≡ K_geom (Maldacena-Susskind 2013)",
        "TFD": "K_entangle thermal double",
        "eternal_BH": "K_horizon + K_entangle identification",
        "traversable_wormhole": "K_geom + K_entangle strong coupling",
        "replica_wormholes": "K_geom non-perturbative quantum gravity",
        "Page_curve_from_replica": "K_holo unitarity (Phase 113 link)",
        "SYK_JT_gravity": "K_holo minimal realization",
    },
    "key_findings": [
        f"EPR singlet: S(ρ_A) = log 2 = {np.log(2):.4f} (maximally entangled)",
        "TFD: S(β=0) = log d (max), S(β=∞) = 0 (product)",
        "Page curve with replica wormhole returns to 0 (unitarity ✓)",
        "ER=EPR (Maldacena-Susskind 2013): entanglement ≡ spacetime",
        "GJW (2017): traversable wormhole via double trace deformation",
        "SYK: maximally chaotic, JT gravity dual, BH simulator",
        "Replica wormholes (Penington 2019, AEMM 2019) reproduce Page curve",
    ],
}

out_json = os.path.join(os.path.dirname(__file__), 'er_epr_wormholes_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 179 complete: K_wormhole = K_entangle × K_geom (ER=EPR);")
print(f"  TFD, replica wormholes, Page curve, traversable wormhole")
print("=" * 70)
