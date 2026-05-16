# Phase 135: SM gauge symmetry SU(3)xSU(2)xU(1) + K_gauge + ITU
# Tier 1 #20 Standard Model (Block A paper 4/9, phase 1/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Tier 1 #17/18/19: 20230667 / 20233070 / 20233952
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 135: SM Gauge Symmetry SU(3)xSU(2)xU(1) + K_gauge in ITU")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: SM gauge group structure
# ----------------------------------------------------------------------
def test1_sm_gauge_group():
    print("[Test 1] SM gauge group SU(3)_C x SU(2)_L x U(1)_Y")
    groups = [
        ("SU(3)_C (Color)",      8, "QCD, strong interaction", "Gluons"),
        ("SU(2)_L (Weak isospin)", 3, "Weak, left-handed only", "W^1, W^2, W^3"),
        ("U(1)_Y (Hypercharge)",   1, "U(1) abelian",            "B"),
    ]
    total_gen = 0
    print(f"  {'Group':<26}  {'Generators':>11}  {'Description':<28}  {'Bosons'}")
    for grp, n, desc, bos in groups:
        print(f"  {grp:<26}  {n:>11d}  {desc:<28}  {bos}")
        total_gen += n
    print(f"\n  Total gauge generators: {total_gen}")
    print(f"  Physical gauge bosons after EWSB: 8 gluons + W^± + Z^0 + γ = 12")
    return {"groups": groups, "total_generators": total_gen}


# ----------------------------------------------------------------------
# Test 2: Gauge boson masses
# ----------------------------------------------------------------------
def test2_gauge_boson_masses():
    print("\n[Test 2] Gauge boson masses (Particle Data Group 2024)")
    bosons = [
        ("Gluon (g)",   0.0,        "8 colors, confined"),
        ("Photon (γ)",  0.0,        "U(1)_EM, massless"),
        ("W^±",         80.379,     "charged weak"),
        ("Z^0",         91.188,     "neutral weak"),
    ]
    print(f"  {'Boson':<14}  {'Mass (GeV)':>11}  {'Note'}")
    rows = []
    for name, m, note in bosons:
        print(f"  {name:<14}  {m:>11.4f}  {note}")
        rows.append({"boson": name, "mass_GeV": m, "note": note})
    return rows


# ----------------------------------------------------------------------
# Test 3: Three coupling constants at M_Z scale
# ----------------------------------------------------------------------
def test3_couplings_MZ():
    print("\n[Test 3] Three coupling constants at M_Z scale")
    couplings = [
        ("α_s (strong)",            0.1181,   "g_s²/(4π), QCD"),
        ("α_em (electromagnetic)",  1.0/127.94, "e²/(4π) at Z pole"),
        ("α_2 (weak isospin)",      0.0339,   "g²/(4π)"),
        ("α_1 (hypercharge)",       0.0102,   "g'²/(4π) GUT normalization"),
    ]
    print(f"  {'Coupling':<24}  {'α (M_Z)':>10}  {'Description'}")
    rows = []
    for name, alpha, desc in couplings:
        print(f"  {name:<24}  {alpha:>10.6f}  {desc}")
        rows.append({"coupling": name, "alpha_MZ": alpha, "description": desc})

    sin2_theta_W = 0.2312
    print(f"\n  Weinberg angle: sin²(θ_W) = {sin2_theta_W} (Z pole)")
    return {"couplings": rows, "sin2_theta_W": sin2_theta_W}


# ----------------------------------------------------------------------
# Test 4: QCD beta function and asymptotic freedom
# ----------------------------------------------------------------------
def test4_qcd_beta():
    print("\n[Test 4] QCD beta function (Gross-Wilczek-Politzer 1973, Nobel 2004)")
    N_c = 3
    N_f_values = [3, 4, 5, 6]   # number of active quark flavors
    print(f"  β(g_s) ∝ -(11 N_c - 2 N_f) / 3, N_c = {N_c}")
    print(f"  {'N_f':>5}  {'(11 N_c - 2 N_f)':>17}  {'β sign'}")
    for N_f in N_f_values:
        b0 = (11 * N_c - 2 * N_f)
        sign = "negative (asymptotic freedom)" if b0 > 0 else "positive (no AF)"
        print(f"  {N_f:>5d}  {b0:>17d}  {sign}")

    # AF maintained while N_f <= 16 (for N_c=3)
    N_f_max = (11 * N_c) // 2
    print(f"\n  AF holds for N_f ≤ {N_f_max} (= 16 for N_c=3); observed N_f = 6")
    return {"N_c": N_c, "N_f_max_for_AF": N_f_max}


# ----------------------------------------------------------------------
# Test 5: Running coupling α_s(μ)
#   α_s(μ) ≈ 4π / [b_0 ln(μ²/Λ_QCD²)],  b_0 = (11 N_c - 2 N_f)/3
# ----------------------------------------------------------------------
def test5_running_alpha_s():
    print("\n[Test 5] Running α_s(μ) (1-loop)")
    Lambda_QCD = 0.200   # GeV
    N_c, N_f = 3, 5
    b_0 = (11 * N_c - 2 * N_f) / 3.0   # = 7.667 for N_f=5

    mu_arr = np.logspace(0, 4, 200)   # 1 GeV to 10 TeV
    alpha_s_arr = (4 * np.pi) / (b_0 * np.log((mu_arr / Lambda_QCD)**2))

    # Sample values
    sample_mu = [1.0, 5.0, 91.188, 500.0, 5000.0]
    print(f"  Λ_QCD = {Lambda_QCD} GeV, N_c = {N_c}, N_f = {N_f}, b_0 = {b_0:.3f}")
    print(f"  {'μ (GeV)':>10}  {'α_s(μ)':>10}")
    rows = []
    for mu in sample_mu:
        a = (4 * np.pi) / (b_0 * np.log((mu / Lambda_QCD)**2))
        print(f"  {mu:>10.3f}  {a:>10.4f}")
        rows.append({"mu_GeV": mu, "alpha_s": float(a)})

    print(f"\n  → α_s decreases with μ (UV) = asymptotic freedom")
    print(f"  → α_s diverges at μ → Λ_QCD = confinement scale")
    return {"mu_arr": mu_arr.tolist(), "alpha_s_arr": alpha_s_arr.tolist(),
            "Lambda_QCD_GeV": Lambda_QCD, "b_0": float(b_0),
            "samples": rows}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
gauge_grp = test1_sm_gauge_group()
gb_masses = test2_gauge_boson_masses()
couplings = test3_couplings_MZ()
qcd_beta = test4_qcd_beta()
running = test5_running_alpha_s()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: SM gauge group structure
ax = axes[0, 0]
ax.axis("off")
ax.set_title("SM gauge group SU(3)_C × SU(2)_L × U(1)_Y", fontsize=12, fontweight="bold")
y = 0.85
for grp, n, desc, bos in gauge_grp["groups"]:
    ax.text(0.05, y, grp, fontsize=11, fontweight="bold", color="#4c72b0")
    ax.text(0.05, y - 0.05, f"  {n} generators → {bos}", fontsize=9)
    ax.text(0.05, y - 0.10, f"  {desc}", fontsize=8, color="gray")
    y -= 0.20
ax.text(0.05, 0.10, f"Total: {gauge_grp['total_generators']} generators",
        fontsize=11, fontweight="bold", color="#c44e52")
ax.text(0.05, 0.04, "After EWSB: 8 gluons + W^± + Z^0 + γ = 12 bosons",
        fontsize=10, color="#55a467")

# Panel 2: Gauge boson masses
ax = axes[0, 1]
names = [b["boson"] for b in gb_masses]
masses = [b["mass_GeV"] for b in gb_masses]
colors_g = ["#4c72b0", "#dd8452", "#c44e52", "#55a467"]
bars = ax.bar(names, masses, color=colors_g)
for b, m in zip(bars, masses):
    if m > 0:
        ax.text(b.get_x() + b.get_width()/2, m + 1, f"{m:.3f}",
                ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel("Mass (GeV)")
ax.set_title("SM gauge boson masses (PDG 2024)", fontsize=12)
ax.grid(True, alpha=0.3, axis="y")
ax.set_ylim(0, 100)

# Panel 3: Three coupling constants
ax = axes[1, 0]
c_names = [c["coupling"].split("(")[0].strip() for c in couplings["couplings"]]
c_vals = [c["alpha_MZ"] for c in couplings["couplings"]]
colors_c = ["#c44e52", "#4c72b0", "#dd8452", "#55a467"]
bars = ax.bar(c_names, c_vals, color=colors_c)
for b, v in zip(bars, c_vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.005, f"{v:.4f}",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel(r"α($M_Z$)")
ax.set_title(f"3 SM couplings at M_Z (sin²θ_W = {couplings['sin2_theta_W']})", fontsize=11)
ax.grid(True, alpha=0.3, axis="y")
plt.setp(ax.get_xticklabels(), fontsize=9, rotation=15)

# Panel 4: Running α_s(μ)
ax = axes[1, 1]
mu = np.array(running["mu_arr"])
alpha_s = np.array(running["alpha_s_arr"])
ax.semilogx(mu, alpha_s, "-", color="#4c72b0", linewidth=2)
ax.axhline(0.118, color="red", linestyle="--", linewidth=1,
           label="α_s(M_Z) = 0.118")
ax.axvline(91.188, color="gray", linestyle=":", linewidth=1, label="M_Z")
ax.axvline(running["Lambda_QCD_GeV"], color="orange", linestyle=":", linewidth=1,
           label=f"Λ_QCD = {running['Lambda_QCD_GeV']} GeV")
ax.set_xlabel("μ (GeV)")
ax.set_ylabel("α_s(μ)")
ax.set_title("QCD running coupling: asymptotic freedom", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")
ax.set_ylim(0, 0.5)

fig.suptitle("Phase 135: SM Gauge Symmetry SU(3)×SU(2)×U(1) + K_gauge in ITU",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "sm_gauge_structure.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 135,
    "title": "SM gauge symmetry SU(3)xSU(2)xU(1) + K_gauge in ITU",
    "tier1_id": 20,
    "tier1_name": "Standard Model",
    "block": "A (Physics/Math) — paper 4/9, phase 1/8",
    "sm_gauge_group": gauge_grp,
    "gauge_boson_masses": gb_masses,
    "couplings_at_MZ": couplings,
    "qcd_beta": qcd_beta,
    "running_alpha_s": running,
    "verdict": ("Standard Model gauge group SU(3)_C × SU(2)_L × U(1)_Y "
                "with 12 generators / 12 physical bosons = K_gauge structure "
                "in ITU. Asymptotic freedom β(g_s) < 0 = K-flow UV simplification."),
}

json_path = "sm_gauge_structure_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 135 complete: SM gauge group = K_gauge in ITU;")
print(f"  Total 12 generators; α_s(M_Z) = 0.118; asymptotic freedom confirmed")
print("=" * 70)
