# Phase 124: Maxwell demon + Landauer + BH info observable + quantum BH simulation
# Tier 1 #18 Black Holes (Block A paper 2/9, phase 6/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 124: Maxwell demon + Landauer + BH info observable + Q-BH sim")
print("=" * 70)
print()

# Constants
HBAR = 1.054571817e-34
C = 2.99792458e8
G_N = 6.67430e-11
kB = 1.380649e-23
M_SUN = 1.989e30
L_P = np.sqrt(HBAR * G_N / C**3)
L_P2 = L_P**2


# ----------------------------------------------------------------------
# Test 1: Landauer's bound at various temperatures
# ----------------------------------------------------------------------
def test1_landauer():
    print("[Test 1] Landauer's bound: ΔE = k_B T ln 2 per bit erasure")
    temps_K = [
        ("Room T (300 K)",        300.0),
        ("LN2 cooling (77 K)",    77.0),
        ("Cryo (4.2 K, He)",      4.2),
        ("Q-computer (0.01 K)",   0.01),
        ("CMB (2.725 K)",         2.725),
    ]
    rows = []
    print(f"  {'Environment':<22}  {'T (K)':>10}  {'ΔE_min (J)':>14}  {'ΔE_min (eV)':>14}")
    for label, T in temps_K:
        dE = kB * T * np.log(2)
        dE_eV = dE / 1.602e-19
        print(f"  {label:<22}  {T:>10.4f}  {dE:>14.4e}  {dE_eV:>14.4e}")
        rows.append({"env": label, "T_K": T, "dE_J": float(dE), "dE_eV": float(dE_eV)})
    return rows


# ----------------------------------------------------------------------
# Test 2: BH as Maxwell demon — Landauer + Bekenstein-Hawking
#   dE = T_H * dS where dS = k_B ln 2 per bit
# ----------------------------------------------------------------------
def test2_bh_demon():
    print("\n[Test 2] BH as Maxwell demon: ΔE_min per bit = k_B T_H ln 2")
    Ms_solar = [1.0, 10.0, 1e6, 6.5e9]
    rows = []
    print(f"  {'M (M_sun)':<12}  {'T_H (K)':>14}  {'ΔE/bit (J)':>14}  {'ΔE/bit (eV)':>14}")
    for M_sol in Ms_solar:
        M = M_sol * M_SUN
        T_H = HBAR * C**3 / (8 * np.pi * G_N * M * kB)
        dE = kB * T_H * np.log(2)
        dE_eV = dE / 1.602e-19
        print(f"  {M_sol:<12.3e}  {T_H:>14.4e}  {dE:>14.4e}  {dE_eV:>14.4e}")
        rows.append({"M_sol": M_sol, "T_H_K": T_H, "dE_per_bit_J": float(dE),
                     "dE_per_bit_eV": float(dE_eV)})
    print()
    print("  → BH stores info at the absolute minimum thermodynamic cost.")
    return rows


# ----------------------------------------------------------------------
# Test 3: Hawking radiation mutual information (Page-like model)
#   I(R_i : R_j) increases past Page time
# ----------------------------------------------------------------------
def test3_radiation_mutual_info():
    print("\n[Test 3] Hawking radiation mutual info I(R_i : R_j) vs time")
    t = np.linspace(0.001, 0.999, 200)
    # S_BH(t) = S_BH(0) * (1 - t)^{2/3}, S_R^thermal = 1 - S_BH(t)
    S_BH_t = (1.0 - t) ** (2.0/3.0)
    S_R_thermal = 1.0 - S_BH_t
    S_R_page = np.minimum(S_R_thermal, S_BH_t)

    # Pairwise mutual info between two radiation quanta:
    # I(R_1 : R_2) ≈ 0 before Page time (thermal independent),
    # ≈ 2 S(per quantum) after Page time (entangled via island)
    I_pair = np.where(S_R_thermal < S_BH_t, 0.0, 2.0 * (S_R_thermal - S_BH_t))

    t_page_idx = int(np.argmin(np.abs(S_R_thermal - S_BH_t)))
    t_page = t[t_page_idx]

    print(f"  t_Page ≈ {t_page:.3f} (from S_R^thermal = S_BH crossing)")
    print(f"  I(R_i : R_j) at t = 0.1: {I_pair[20]:.4f}")
    print(f"  I(R_i : R_j) at t = 0.5: {I_pair[100]:.4f}")
    print(f"  I(R_i : R_j) at t = 0.9: {I_pair[180]:.4f}")
    print(f"  → Mutual info spike after Page time = signature of info recovery")
    return {"t": t.tolist(), "S_BH": S_BH_t.tolist(),
            "S_R_thermal": S_R_thermal.tolist(),
            "S_R_page": S_R_page.tolist(),
            "I_pair": I_pair.tolist(), "t_page": float(t_page)}


# ----------------------------------------------------------------------
# Test 4: Petz map decoder fidelity (toy model)
# ----------------------------------------------------------------------
def test4_petz_fidelity():
    print("\n[Test 4] Petz map decoder fidelity vs time")
    t = np.linspace(0.001, 0.999, 200)
    S_BH_t = (1.0 - t) ** (2.0/3.0)
    S_R_thermal = 1.0 - S_BH_t

    # Toy: fidelity rises sigmoidally around t_Page
    # F = 1 / (1 + exp(-k (t - t_Page)))
    diff = S_R_thermal - S_BH_t
    sign_change = np.where(np.diff(np.sign(diff)))[0]
    t_page = float(t[sign_change[0]]) if len(sign_change) > 0 else 0.5
    k_steep = 30.0
    F = 1.0 / (1.0 + np.exp(-k_steep * (t - t_page)))

    print(f"  Toy sigmoid: F(t) = 1 / (1 + exp(-30 (t - t_Page)))")
    print(f"  t_Page ≈ {t_page:.3f}")
    print(f"  F at t = 0.1: {F[20]:.4f}")
    print(f"  F at t = t_Page: {F[sign_change[0]]:.4f}")
    print(f"  F at t = 0.95: {F[-10]:.4f}")
    print(f"  → Petz decoder fidelity rises sharply at t_Page (Hayden-Preskill).")
    return {"t": t.tolist(), "fidelity": F.tolist(), "t_page": t_page}


# ----------------------------------------------------------------------
# Test 5: SYK / JT gravity Hilbert dim and qubit simulation feasibility
# ----------------------------------------------------------------------
def test5_qcomputer_simulation():
    print("\n[Test 5] Quantum computer simulation feasibility")
    # SYK with N Majorana fermions: Hilbert dim 2^(N/2)
    Ns = [10, 20, 30, 40, 50, 60, 100]
    rows = []
    print(f"  {'N (Majorana)':<14}  {'Hilbert dim 2^(N/2)':>20}  {'Qubits needed':>16}")
    for N in Ns:
        dim = 2 ** (N // 2)
        qubits_needed = N // 2
        print(f"  {N:<14d}  {dim:>20.4e}  {qubits_needed:>16d}")
        rows.append({"N_majorana": N, "hilbert_dim": dim,
                     "qubits_needed": qubits_needed})

    print()
    qpus = [
        ("IBM Eagle (2021)",       127),
        ("IBM Condor (2023)",      1121),
        ("Google Sycamore (2019)", 53),
        ("Atom Computing (2024)",  1180),
    ]
    print(f"  {'QPU':<30}  {'Qubits':>8}  {'Max SYK N':>10}")
    for name, q in qpus:
        max_N = q * 2
        print(f"  {name:<30}  {q:>8d}  {max_N:>10d}")
    print()
    print("  → 100-1000 qubit QPUs can simulate SYK / JT gravity directly.")
    print("  → Page curve observable on quantum simulators (Niezgoda et al. 2022).")
    return {"syk_table": rows, "qpus": qpus}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
landauer = test1_landauer()
bh_demon = test2_bh_demon()
mut_info = test3_radiation_mutual_info()
petz = test4_petz_fidelity()
sim_table = test5_qcomputer_simulation()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Landauer at various T
ax = axes[0, 0]
labels = [r["env"].split("(")[0].strip() for r in landauer]
T_vals = [r["T_K"] for r in landauer]
dE_vals = [r["dE_eV"] for r in landauer]
ax.barh(labels, dE_vals, color="#4c72b0")
for i, (T, dE) in enumerate(zip(T_vals, dE_vals)):
    ax.text(dE * 1.1, i, f"{dE:.2e} eV", va="center", fontsize=8)
ax.set_xlabel(r"$\Delta E_{min}$ per bit (eV)")
ax.set_xscale("log")
ax.set_title("Landauer's bound: $\\Delta E = k_B T \\ln 2$ per bit", fontsize=12)
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 2: BH as Maxwell demon — ΔE per bit
ax = axes[0, 1]
Ms = [r["M_sol"] for r in bh_demon]
dEs = [r["dE_per_bit_eV"] for r in bh_demon]
ax.loglog(Ms, dEs, "o-", color="#4c72b0", linewidth=2, markersize=8)
for r in bh_demon:
    ax.annotate(f"{r['M_sol']:.0e}", (r["M_sol"], r["dE_per_bit_eV"]),
                textcoords="offset points", xytext=(5, 5), fontsize=8)
ax.set_xlabel(r"BH mass (M$_\odot$)")
ax.set_ylabel(r"$\Delta E$ per bit (eV)")
ax.set_title("BH as Maxwell demon: $\\Delta E = k_B T_H \\ln 2$", fontsize=12)
ax.grid(True, alpha=0.3, which="both")

# Panel 3: Hawking radiation mutual info
ax = axes[1, 0]
ax.plot(mut_info["t"], mut_info["I_pair"], "-", color="#4c72b0", linewidth=2,
        label="I(R$_i$ : R$_j$)")
ax.plot(mut_info["t"], mut_info["S_R_page"], "--", color="#c44e52", linewidth=1.5,
        label="S$_R$ (Page)")
ax.axvline(mut_info["t_page"], color="gray", linestyle=":", linewidth=1)
ax.text(mut_info["t_page"] + 0.01, 0.05, f"t$_{{Page}}$ = {mut_info['t_page']:.3f}",
        color="gray", fontsize=9)
ax.set_xlabel("t / t$_{evap}$")
ax.set_ylabel("Information")
ax.set_title("Hawking radiation mutual info I(R$_i$ : R$_j$)", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 4: Petz fidelity + QPU table
ax = axes[1, 1]
ax.plot(petz["t"], petz["fidelity"], "-", color="#4c72b0", linewidth=2,
        label="Petz decoder fidelity F(t)")
ax.axvline(petz["t_page"], color="gray", linestyle=":", linewidth=1)
ax.axhline(0.5, color="red", linestyle="--", linewidth=1, label="F = 0.5 threshold")
ax.set_xlabel("t / t$_{evap}$")
ax.set_ylabel("Decoder fidelity F")
ax.set_title("Petz map fidelity (sigmoid toy)", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.05)

fig.suptitle("Phase 124: Maxwell demon + BH info observable + Quantum BH simulation",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "maxwell_bh_quantum_sim.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 124,
    "title": "Maxwell demon + Landauer + BH info observable + Q-BH simulation",
    "tier1_id": 18,
    "tier1_name": "Black Holes",
    "block": "A (Physics/Math) — paper 2/9, phase 6/8",
    "landauer_bound": landauer,
    "bh_as_demon": bh_demon,
    "radiation_mutual_info": {
        "t_page": mut_info["t_page"],
        "I_pair_max": float(np.max(mut_info["I_pair"])),
    },
    "petz_fidelity": {
        "t_page": petz["t_page"],
        "F_at_0p1": petz["fidelity"][20],
        "F_at_t_page": petz["fidelity"][int(np.argmin(np.abs(np.array(petz["t"]) - petz["t_page"])))],
    },
    "qpu_simulation": sim_table,
    "verdict": ("BH = ultimate Maxwell demon at k_B T_H ln 2 / bit; "
                "Hawking radiation mutual info I(R_i:R_j) spikes after Page time; "
                "Petz fidelity rises at t_Page; SYK/JT gravity tractable on 100-1000 qubit QPUs."),
}

json_path = "maxwell_bh_quantum_sim_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 124 complete: BH = extreme Maxwell demon under ITU;")
print(f"  Hawking mutual info I(R_i:R_j) spike at t_Page = {mut_info['t_page']:.3f}.")
print("=" * 70)
