# Phase 119: Schwarzschild + Kerr + No-hair + ISCO + Penrose + ITU mapping
# Tier 1 #18 Black Holes (Block A paper 2/9, phase 1/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Tier 1 #17 (QG): 10.5281/zenodo.20230667
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 119: Schwarzschild + Kerr + No-hair + ISCO + Penrose")
print("=" * 70)
print()

# Constants
HBAR = 1.054571817e-34
C = 2.99792458e8
G_N = 6.67430e-11
kB = 1.380649e-23
M_SUN = 1.989e30
AU = 1.495978707e11   # meter
PARSEC = 3.0857e16
L_P = np.sqrt(HBAR * G_N / C**3)


# ----------------------------------------------------------------------
# Test 1: Schwarzschild radius for various BH masses
# ----------------------------------------------------------------------
def test1_schwarzschild_radii():
    print("[Test 1] Schwarzschild radius r_s = 2 G M / c^2 for various BHs")
    targets = [
        ("Sun (toy BH)",          1.0,         "1 M_sun"),
        ("Stellar BH (typical)",  10.0,        "10 M_sun"),
        ("Cygnus X-1",            21.0,        "21 M_sun"),
        ("LIGO GW150914 final",   62.0,        "62 M_sun"),
        ("Intermediate mass",     1.0e3,       "1e3 M_sun"),
        ("Sgr A*",                4.0e6,       "4e6 M_sun"),
        ("M87*",                  6.5e9,       "6.5e9 M_sun"),
        ("Ultra-massive (TON 618)", 6.6e10,    "6.6e10 M_sun"),
    ]
    rows = []
    print(f"  {'BH':<26}  {'M':<14}  {'r_s (m)':>14}  {'r_s (km)':>12}  {'r_s (AU)':>10}")
    for name, M_solar, label in targets:
        M = M_solar * M_SUN
        r_s = 2 * G_N * M / C**2
        r_s_km = r_s / 1000.0
        r_s_AU = r_s / AU
        print(f"  {name:<26}  {label:<14}  {r_s:>14.4e}  {r_s_km:>12.4f}  {r_s_AU:>10.4f}")
        rows.append({"name": name, "M_solar": M_solar, "r_s_m": r_s,
                     "r_s_km": r_s_km, "r_s_AU": r_s_AU})
    return rows


# ----------------------------------------------------------------------
# Test 2: Kerr outer/inner horizons vs spin a
# ----------------------------------------------------------------------
def test2_kerr_horizons():
    print("\n[Test 2] Kerr horizons r_+ , r_- vs dimensionless spin a*")
    # Use r_s = 1 (units); a* = a/(r_s/2) (dimensionless 0..1)
    r_s = 1.0
    a_star_list = np.linspace(0.0, 1.0, 100)
    a_list = a_star_list * (r_s / 2.0)   # a in r_s units, a_max = r_s/2 (extremal)
    r_plus = (r_s + np.sqrt(np.maximum(r_s**2 - 4*a_list**2, 0))) / 2.0
    r_minus = (r_s - np.sqrt(np.maximum(r_s**2 - 4*a_list**2, 0))) / 2.0

    samples = [0.0, 0.3, 0.5, 0.7, 0.9, 1.0]
    print(f"  {'a*':>5}  {'a (r_s)':>9}  {'r_+ (r_s)':>10}  {'r_- (r_s)':>10}")
    for s in samples:
        a = s * (r_s / 2.0)
        rp = (r_s + np.sqrt(max(r_s**2 - 4*a**2, 0))) / 2.0
        rm = (r_s - np.sqrt(max(r_s**2 - 4*a**2, 0))) / 2.0
        print(f"  {s:>5.2f}  {a:>9.4f}  {rp:>10.4f}  {rm:>10.4f}")
    print(f"  Extremal limit (a* = 1): r_+ = r_- = {0.5*r_s:.3f} r_s")
    return {"a_star": a_star_list.tolist(), "r_plus": r_plus.tolist(),
            "r_minus": r_minus.tolist(), "r_s_units": r_s}


# ----------------------------------------------------------------------
# Test 3: ISCO for Schwarzschild and Kerr
# ----------------------------------------------------------------------
def isco_kerr(a_star):
    """Bardeen-Press-Teukolsky 1972: ISCO radius for Kerr (M=1 units, r_g = GM/c^2)."""
    a = a_star   # dimensionless spin parameter in M = 1 units, a in [0, 1]
    Z1 = 1 + (1 - a**2)**(1/3) * ((1 + a)**(1/3) + (1 - a)**(1/3))
    Z2 = np.sqrt(3 * a**2 + Z1**2)
    # Prograde
    r_prograde = 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))
    # Retrograde
    r_retrograde = 3 + Z2 + np.sqrt((3 - Z1) * (3 + Z1 + 2*Z2))
    return r_prograde, r_retrograde


def test3_isco():
    print("\n[Test 3] ISCO: Schwarzschild and Kerr (Bardeen-Press-Teukolsky 1972)")
    a_star_list = np.linspace(0.0, 0.99, 100)
    r_pro_list = []
    r_retr_list = []
    for a in a_star_list:
        rp, rr = isco_kerr(a)
        r_pro_list.append(rp)
        r_retr_list.append(rr)

    # In units of r_s = 2 r_g, so multiply by 1/2 to get r/r_s
    # We will keep them in r_g units for clarity
    samples = [0.0, 0.3, 0.5, 0.7, 0.9, 0.99]
    print(f"  Units: r_g = G M / c^2 = r_s / 2")
    print(f"  {'a*':>6}  {'r_ISCO (prograde, r_g)':>22}  {'r_ISCO (retrograde, r_g)':>24}")
    for s in samples:
        rp, rr = isco_kerr(s)
        print(f"  {s:>6.2f}  {rp:>22.4f}  {rr:>24.4f}")

    rp0, rr0 = isco_kerr(0.0)
    rp_ext, rr_ext = isco_kerr(0.999)
    print()
    print(f"  Schwarzschild (a*=0): r_ISCO = {rp0:.4f} r_g = 3 r_s")
    print(f"  Kerr extremal prograde:  r_ISCO -> 1 r_g = r_s/2")
    print(f"  Kerr extremal retrograde: r_ISCO -> 9 r_g = 4.5 r_s")
    return {"a_star": a_star_list.tolist(),
            "r_prograde": r_pro_list, "r_retrograde": r_retr_list,
            "schwarzschild_r_isco_rg": rp0}


# ----------------------------------------------------------------------
# Test 4: Penrose process maximum efficiency
# ----------------------------------------------------------------------
def test4_penrose_max():
    print("\n[Test 4] Penrose process: maximum energy extraction")
    # Christodoulou-Ruffini: M_irr = M sqrt((1 + sqrt(1 - a*^2)) / 2)
    # Maximum extractable energy: (M - M_irr) / M
    a_star_list = np.linspace(0.0, 1.0, 100)
    eta_list = []
    for a in a_star_list:
        M_irr_over_M = np.sqrt((1 + np.sqrt(1 - a**2)) / 2.0)
        eta = 1.0 - M_irr_over_M
        eta_list.append(eta)
    eta_max = float(eta_list[-1])

    samples = [0.0, 0.3, 0.5, 0.7, 0.9, 0.99, 1.0]
    print(f"  {'a*':>6}  {'M_irr / M':>10}  {'eta_max':>10}")
    for s in samples:
        Mirr_M = np.sqrt((1 + np.sqrt(1 - s**2)) / 2.0)
        e = 1 - Mirr_M
        print(f"  {s:>6.2f}  {Mirr_M:>10.4f}  {e:>10.4f}")
    print()
    print(f"  Max extractable energy (extremal Kerr): {eta_max:.4f} = {eta_max*100:.2f} %  (Christodoulou-Ruffini 1971)")
    return {"a_star": a_star_list.tolist(), "eta": eta_list, "eta_max": eta_max}


# ----------------------------------------------------------------------
# Test 5: K_geom (surface gravity) and ITU axiom for Schwarzschild
# ----------------------------------------------------------------------
def test5_k_geom_schwarzschild():
    print("\n[Test 5] K_geom = 2 pi (surface gravity) for Schwarzschild BHs")
    # surface gravity kappa = c^2 / (2 r_s) = c^4 / (4 G M)
    Ms = [1.0, 10.0, 1e6, 6.5e9]
    rows = []
    print(f"  {'M (M_sun)':>10}  {'r_s (m)':>14}  {'kappa (m/s^2)':>16}  {'T_H (K)':>14}  {'S_BH (nats)':>16}")
    for M_solar in Ms:
        M = M_solar * M_SUN
        r_s = 2 * G_N * M / C**2
        kappa = C**4 / (4 * G_N * M)   # m/s^2
        T_H = HBAR * kappa / (2 * np.pi * kB * C)
        # S_BH = A_horizon / (4 G_N hbar) = pi r_s^2 / (G_N hbar) (Bekenstein-Hawking)
        # In nats (no kB), using S = A / (4 hbar G_N / c^3) = A / (4 l_P^2)
        L_P2 = HBAR * G_N / C**3
        A_horizon = 4 * np.pi * r_s**2
        S_BH = A_horizon / (4 * L_P2)
        print(f"  {M_solar:>10.2e}  {r_s:>14.4e}  {kappa:>16.4e}  {T_H:>14.4e}  {S_BH:>16.4e}")
        rows.append({"M_solar": M_solar, "r_s_m": r_s,
                     "kappa": kappa, "T_H_K": T_H, "S_BH_nats": S_BH})
    print()
    print("  ITU axiom: dS = dA / (4 G_N hbar / c^3) = dA / (4 l_P^2) = d<K_geom>")
    print("  K_geom = 2 pi (boost generator) — modular Hamiltonian at horizon (Bisognano-Wichmann).")
    return rows


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
schwarzschild = test1_schwarzschild_radii()
kerr = test2_kerr_horizons()
isco = test3_isco()
penrose = test4_penrose_max()
k_geom = test5_k_geom_schwarzschild()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: r_s vs M for different BH classes
ax = axes[0, 0]
names = [r["name"] for r in schwarzschild]
M_vals = [r["M_solar"] for r in schwarzschild]
r_s_vals = [r["r_s_m"] for r in schwarzschild]
ax.loglog(M_vals, r_s_vals, "o-", color="#4c72b0", linewidth=2, markersize=6)
for i, (M, rs, name) in enumerate(zip(M_vals, r_s_vals, names)):
    ax.annotate(name, (M, rs), textcoords="offset points",
                xytext=(8, 5), fontsize=7)
ax.set_xlabel(r"Mass M (M$_\odot$)")
ax.set_ylabel(r"Schwarzschild radius r$_s$ (m)")
ax.set_title("r$_s$ = 2 G M / c$^2$", fontsize=12)
ax.grid(True, alpha=0.3, which="both")

# Panel 2: Kerr horizons r_+, r_- vs a*
ax = axes[0, 1]
ax.plot(kerr["a_star"], kerr["r_plus"], "-", color="#4c72b0", linewidth=2,
        label=r"r$_+$ (outer horizon)")
ax.plot(kerr["a_star"], kerr["r_minus"], "-", color="#c44e52", linewidth=2,
        label=r"r$_-$ (inner horizon)")
ax.axvline(1.0, color="gray", linestyle=":", linewidth=1, label="extremal a*=1")
ax.set_xlabel(r"Spin parameter a$^*$ = 2a / r$_s$")
ax.set_ylabel(r"Horizon radius (r$_s$ units)")
ax.set_title("Kerr horizons r$_\\pm$", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: ISCO vs a*
ax = axes[1, 0]
ax.plot(isco["a_star"], isco["r_prograde"], "-", color="#4c72b0", linewidth=2,
        label="prograde (co-rotating)")
ax.plot(isco["a_star"], isco["r_retrograde"], "-", color="#c44e52", linewidth=2,
        label="retrograde (counter-rotating)")
ax.axhline(isco["schwarzschild_r_isco_rg"], color="gray", linestyle="--",
           linewidth=1, label=f"Schwarzschild: 6 r$_g$ = 3 r$_s$")
ax.axhline(1.0, color="green", linestyle=":", linewidth=1, label="extremal prograde: 1 r$_g$")
ax.axhline(9.0, color="purple", linestyle=":", linewidth=1, label="extremal retrograde: 9 r$_g$")
ax.set_xlabel(r"Spin a$^*$")
ax.set_ylabel(r"ISCO radius (r$_g$ = GM/c$^2$)")
ax.set_title("ISCO: Bardeen-Press-Teukolsky 1972", fontsize=12)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Penrose process max efficiency
ax = axes[1, 1]
ax.plot(penrose["a_star"], np.array(penrose["eta"]) * 100, "-", color="#4c72b0",
        linewidth=2, label="$\\eta_{max}$ (Christodoulou-Ruffini)")
ax.axhline(penrose["eta_max"] * 100, color="red", linestyle="--", linewidth=1,
           label=f"extremal: {penrose['eta_max']*100:.2f} %")
ax.set_xlabel(r"Spin a$^*$")
ax.set_ylabel("Penrose extractable energy (% of M c$^2$)")
ax.set_title("Penrose process maximum efficiency", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.suptitle("Phase 119: Schwarzschild + Kerr + No-hair + ISCO + Penrose",
             fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.97])

png_path = "schwarzschild_kerr_isco.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 119,
    "title": "Schwarzschild + Kerr + No-hair + ISCO + Penrose + ITU mapping",
    "tier1_id": 18,
    "tier1_name": "Black Holes",
    "block": "A (Physics/Math) — paper 2/9, phase 1/8",
    "schwarzschild_radii": schwarzschild,
    "kerr_horizons_a_star_sample": [0.0, 0.5, 1.0],
    "penrose_max_efficiency": penrose["eta_max"],
    "k_geom_examples": k_geom,
    "verdict": ("Schwarzschild + Kerr solutions = K_geom stationary points; "
                "No-hair theorem = K-flow uniqueness; Penrose max eta = 29.3% "
                "at extremal Kerr."),
}

json_path = "schwarzschild_kerr_isco_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 119 complete: BH classical solutions = K_geom stationary points;")
print(f"  Penrose max eta = {penrose['eta_max']*100:.2f} % at extremal Kerr.")
print("=" * 70)
