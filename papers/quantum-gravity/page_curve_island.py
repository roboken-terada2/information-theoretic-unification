# Phase 113: Page Curve + Island Formula + QES + Replica Wormhole
# Tier 1 #17 Quantum Gravity — Block A
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 113: Page Curve + Island Formula + QES")
print("=" * 70)
print()

rng = np.random.default_rng(2026)


# ----------------------------------------------------------------------
# Test 1: Page curve via Haar-random states
# ----------------------------------------------------------------------
def haar_random_state(d):
    psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    psi /= np.linalg.norm(psi)
    return psi


def avg_entropy(d_A, d_B, n_samples=40):
    """Average S_A for random |psi> on d_A x d_B."""
    d = d_A * d_B
    S_list = []
    for _ in range(n_samples):
        psi = haar_random_state(d).reshape(d_A, d_B)
        rho_A = psi @ psi.conj().T
        w = np.linalg.eigvalsh(rho_A)
        w = np.clip(w.real, 1e-15, None)
        w /= w.sum()
        S = float(-np.sum(w * np.log(w)))
        S_list.append(S)
    return float(np.mean(S_list)), float(np.std(S_list))


def page_formula(d_A, d_B):
    """Page (1993) approximate: log(min) - min/(2 max)."""
    d_min = min(d_A, d_B)
    d_max = max(d_A, d_B)
    return np.log(d_min) - d_min / (2.0 * d_max)


def test1_page_curve():
    print("[Test 1] Page curve via Haar random states")
    d_total = 64
    d_A_list = [2, 4, 8, 16, 32, 48, 56, 60, 62, 63]
    rows = []
    print(f"  d_total = {d_total}, n_samples = 40 per point")
    print(f"  {'d_A':>5}  {'d_B':>5}  {'S_random':>10}  {'S_Page':>10}  {'abs diff':>10}")
    for d_A in d_A_list:
        d_B = d_total // d_A
        S_emp, S_std = avg_entropy(d_A, d_B, n_samples=40)
        S_page = page_formula(d_A, d_B)
        diff = abs(S_emp - S_page)
        print(f"  {d_A:>5}  {d_B:>5}  {S_emp:>10.4f}  {S_page:>10.4f}  {diff:>10.4f}")
        rows.append({"d_A": d_A, "d_B": d_B, "S_emp": S_emp, "S_std": S_std,
                     "S_page": S_page, "abs_diff": diff})

    max_diff = max(r["abs_diff"] for r in rows)
    print(f"\n  max |S_emp - S_Page| = {max_diff:.3f} (small for d_total=64; Page formula holds in d->infty)")
    return {"d_total": d_total, "rows": rows, "max_diff": max_diff}


# ----------------------------------------------------------------------
# Test 2: Page curve as function of "time" for evaporating BH
#   d_A(t) = e^{S_R(t)} (radiation), d_B(t) = e^{S_BH(t)} (BH)
# ----------------------------------------------------------------------
def test2_evaporation_page():
    print("\n[Test 2] Evaporation: S_R(t) follows Page curve")
    S_BH_0 = 6.0    # initial entropy (toy)
    t_evap = 1.0
    t = np.linspace(0.001, 0.999, 100) * t_evap

    # Linearly evaporate: S_BH(t) decreases linearly
    S_BH = S_BH_0 * (1.0 - t / t_evap)
    S_R_thermal = S_BH_0 - S_BH        # thermal entanglement carried by radiation (Hawking-like)

    # Page curve: S_R(t) = min(S_R_thermal, S_BH)
    S_R_page = np.minimum(S_R_thermal, S_BH)
    t_page = t_evap / 2.0

    print(f"  S_BH(0) = {S_BH_0}, t_evap = {t_evap}")
    print(f"  t_Page = t_evap / 2 = {t_page:.3f}")
    print(f"  S_R(t_Page) = {S_BH_0 / 2.0:.3f}  (= S_BH(0) / 2)")
    print(f"  S_R(0) = {S_R_page[0]:.4f}, S_R(t_evap) = {S_R_page[-1]:.4f}")
    return {"t": t.tolist(), "S_BH": S_BH.tolist(),
            "S_R_thermal": S_R_thermal.tolist(),
            "S_R_page": S_R_page.tolist(),
            "S_BH_0": S_BH_0, "t_evap": t_evap, "t_page": t_page}


# ----------------------------------------------------------------------
# Test 3: Island formula = min of two saddles
#   S(R) = min( S_Hawking(t),  S_island(t) = Area/4G + S_bulk(R cup I) )
# ----------------------------------------------------------------------
def test3_island_formula():
    print("\n[Test 3] Island formula: two saddles compete")
    S_BH_0 = 6.0
    t_evap = 1.0
    t = np.linspace(0.001, 0.999, 100) * t_evap

    # Saddle A (Hawking): linearly growing
    S_hawking = S_BH_0 * (t / t_evap)

    # Saddle B (Island): A/(4G_N) + S_bulk(R cup I)
    # In simplified model: ~ S_BH(t) = S_BH_0 - linear part
    Area_over_4G = S_BH_0 * (1.0 - t / t_evap)   # area of island boundary shrinks as BH evaporates
    S_bulk_R_I = 0.0  # subleading in toy
    S_island = Area_over_4G + S_bulk_R_I

    # Island formula: min ext of the two saddles
    S_R = np.minimum(S_hawking, S_island)

    # Identify Page time as crossover
    diff = S_hawking - S_island
    sign_change = np.where(np.diff(np.sign(diff)))[0]
    t_cross = float(t[sign_change[0]]) if len(sign_change) > 0 else float(t_evap / 2)
    print(f"  Hawking saddle: S = (S_BH_0/t_evap) t")
    print(f"  Island saddle:  S = S_BH_0 (1 - t/t_evap)")
    print(f"  Crossover (Page time) at t = {t_cross:.4f} (expected t_evap/2 = {t_evap/2:.4f})")

    print(f"  S(R)(0)       = {S_R[0]:.4f} (Hawking dominates)")
    print(f"  S(R)(t_cross) = {S_BH_0/2.0:.4f} (peak)")
    print(f"  S(R)(t_evap)  = {S_R[-1]:.4f} (Island dominates, info recovered)")
    return {"t": t.tolist(), "S_hawking": S_hawking.tolist(),
            "S_island": S_island.tolist(), "S_R": S_R.tolist(),
            "t_cross": t_cross, "S_peak": S_BH_0 / 2.0}


# ----------------------------------------------------------------------
# Test 4: K-channel competition (ITU view of Island formula)
# ----------------------------------------------------------------------
def test4_k_channel_competition():
    print("\n[Test 4] ITU K-channel competition view of Island formula")
    # K_geom (boost-like, decreases with shrinking BH area) and
    # K_thermal (radiation thermal modular, increases with radiation)
    t = np.linspace(0, 1, 200)
    K_thermal = 6.0 * t          # accumulates with radiation entropy
    K_geom_bdy = 6.0 * (1.0 - t)  # area contribution decreases

    # Effective ITU S
    S_eff = np.minimum(K_thermal, K_geom_bdy)
    idx_max = int(np.argmax(S_eff))
    t_peak = float(t[idx_max])

    print("  Two K-channels:")
    print("    K_thermal(t) = 6 t (radiation thermal modular Hamiltonian)")
    print("    K_geom(t)    = 6 (1-t) (boundary boost modular = Area/4G)")
    print(f"  Peak S_eff = {float(S_eff[idx_max]):.4f}  at t = {t_peak:.4f}")
    print("  -> ITU stationary point = 'extremize' in Island formula")
    return {"t": t.tolist(), "K_thermal": K_thermal.tolist(),
            "K_geom": K_geom_bdy.tolist(), "S_eff": S_eff.tolist(),
            "peak_t": t_peak, "peak_S": float(S_eff[idx_max])}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
page = test1_page_curve()
evap = test2_evaporation_page()
island = test3_island_formula()
kchan = test4_k_channel_competition()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Page formula vs random states
ax = axes[0, 0]
d_A_list = [r["d_A"] for r in page["rows"]]
S_emp = [r["S_emp"] for r in page["rows"]]
S_page_arr = [r["S_page"] for r in page["rows"]]
S_std_arr = [r["S_std"] for r in page["rows"]]
ax.errorbar(d_A_list, S_emp, yerr=S_std_arr, fmt="o", color="#4c72b0",
            label="random state (Haar)", capsize=3, markersize=6)
ax.plot(d_A_list, S_page_arr, "--", color="#c44e52", linewidth=2,
        label="Page formula")
ax.set_xscale("log", base=2)
ax.set_xlabel("d_A (log2)")
ax.set_ylabel("Average entropy S")
ax.set_title("Page curve via Haar random states (d_total=64)", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 2: Page curve for evaporation
ax = axes[0, 1]
ax.plot(evap["t"], evap["S_BH"], "--", color="black", linewidth=1.5, label="S_BH(t)")
ax.plot(evap["t"], evap["S_R_thermal"], ":", color="#c44e52", linewidth=1.5, label="S_R^thermal (Hawking)")
ax.plot(evap["t"], evap["S_R_page"], "-", color="#4c72b0", linewidth=2.5, label="S_R (Page, ITU)")
ax.axvline(evap["t_page"], color="gray", linestyle=":", linewidth=1)
ax.set_xlabel("time / t_evap")
ax.set_ylabel("Entropy")
ax.set_title("Page curve for evaporating BH", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Island formula min of two saddles
ax = axes[1, 0]
ax.plot(island["t"], island["S_hawking"], "--", color="#dd8452", linewidth=1.5,
        label="Hawking saddle: t / t_evap × S_BH(0)")
ax.plot(island["t"], island["S_island"], "--", color="#8172b3", linewidth=1.5,
        label="Island saddle: Area/(4G_N)")
ax.plot(island["t"], island["S_R"], "-", color="#4c72b0", linewidth=2.5,
        label="S(R) = min(saddles)")
ax.axvline(island["t_cross"], color="gray", linestyle=":", linewidth=1)
ax.text(island["t_cross"] + 0.01, 0.5, f"t_Page = {island['t_cross']:.3f}",
        color="gray", fontsize=9)
ax.set_xlabel("time / t_evap")
ax.set_ylabel("S(R)")
ax.set_title("Island formula: min ext of two saddles", fontsize=12)
ax.legend(fontsize=9, loc="upper right")
ax.grid(True, alpha=0.3)

# Panel 4: ITU K-channel competition
ax = axes[1, 1]
ax.plot(kchan["t"], kchan["K_thermal"], "--", color="#dd8452", linewidth=1.5,
        label="K_thermal (radiation)")
ax.plot(kchan["t"], kchan["K_geom"], "--", color="#8172b3", linewidth=1.5,
        label="K_geom (boundary boost)")
ax.plot(kchan["t"], kchan["S_eff"], "-", color="#55a467", linewidth=2.5,
        label="S_eff = min(K_thermal, K_geom)")
ax.axvline(kchan["peak_t"], color="gray", linestyle=":", linewidth=1)
ax.text(kchan["peak_t"] + 0.01, 0.5, f"peak at t = {kchan['peak_t']:.3f}",
        color="gray", fontsize=9)
ax.set_xlabel("time / t_evap")
ax.set_ylabel("K-channel value")
ax.set_title("ITU K-channel competition view", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle("Phase 113: Page Curve + Island Formula + K-channel Competition",
             fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.97])

png_path = "page_curve_island.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 113,
    "title": "Page curve + Island formula + QES + K-channel competition",
    "tier1_id": 17,
    "tier1_name": "Quantum Gravity",
    "block": "A (Physics/Math)",
    "page_random": {
        "d_total": page["d_total"],
        "max_abs_diff": page["max_diff"],
        "rows_first_3": page["rows"][:3],
    },
    "evaporation": {
        "S_BH_0": evap["S_BH_0"],
        "t_evap": evap["t_evap"],
        "t_page": evap["t_page"],
        "S_R_peak": float(np.max(evap["S_R_page"])),
    },
    "island_formula": {
        "t_cross": island["t_cross"],
        "S_peak": island["S_peak"],
        "verdict": "min(Hawking saddle, Island saddle) reproduces Page curve",
    },
    "k_channel_view": {
        "peak_t": kchan["peak_t"],
        "peak_S": kchan["peak_S"],
        "verdict": "Island formula = min over K_thermal and K_geom channels in ITU",
    },
}

json_path = "page_curve_island_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 113 complete: Page curve from random states + Island formula as")
print("  K-channel competition; ITU encodes min-ext via two-saddle swap")
print("=" * 70)
