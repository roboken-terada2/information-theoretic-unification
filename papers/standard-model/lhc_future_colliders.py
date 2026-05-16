# Phase 141: LHC + Future colliders + Particle Cosmology + ITU verification platform
# Tier 1 #20 Standard Model (Block A paper 4/9, phase 7/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 141: LHC + Future Colliders + Particle Cosmology + ITU")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: LHC Runs history
# ----------------------------------------------------------------------
def test1_lhc_runs():
    print("[Test 1] LHC Runs history")
    runs = [
        ("Run 1",      "2010-2013",  "7-8 TeV",      30,      "Higgs discovery (2012)"),
        ("Run 2",      "2015-2018",  "13 TeV",       140,     "Higgs precision + BSM"),
        ("Run 3",      "2022-2025",  "13.6 TeV",     300,     "Ongoing, target 2025"),
        ("HL-LHC",     "2030-2041",  "14 TeV",       3000,    "Higgs λ_3 first measure"),
    ]
    print(f"  {'Run':<10}  {'Period':<14}  {'√s':<10}  {'L_int (fb^-1)':>14}  {'Highlights'}")
    rows = []
    for r, p, s, L, h in runs:
        print(f"  {r:<10}  {p:<14}  {s:<10}  {L:>14}  {h}")
        rows.append({"run": r, "period": p, "sqrt_s": s,
                     "integrated_luminosity_fbinv": L, "highlights": h})
    return rows


# ----------------------------------------------------------------------
# Test 2: Higgs self-coupling λ_3 precision evolution
# ----------------------------------------------------------------------
def test2_higgs_self_coupling():
    print("\n[Test 2] Higgs self-coupling κ_λ precision evolution")
    measurements = [
        ("Run 2 ATLAS+CMS (2022)",        "-0.4 to 6.3",   "95% CL, di-Higgs"),
        ("Run 3 (2025 projected)",        "0.1 to 4.5",    "improved precision"),
        ("HL-LHC ATLAS+CMS (2041)",       "1 ± 0.5",       "first 50% measure"),
        ("FCC-ee (2065)",                 "1 ± 0.10",      "indirect via Z H"),
        ("FCC-hh (2100)",                 "1 ± 0.05",      "direct di-Higgs"),
        ("Muon Collider 10 TeV",          "1 ± 0.05",      "competitive with FCC"),
    ]
    print(f"  {'Experiment':<32}  {'κ_λ range/precision':<22}  {'Notes'}")
    rows = []
    for name, p, note in measurements:
        print(f"  {name:<32}  {p:<22}  {note}")
        rows.append({"experiment": name, "kappa_lambda": p, "note": note})
    print(f"\n  → HL-LHC (2041) first significant measurement of κ_λ")
    print(f"  → FCC-hh / Muon Collider (2100): 5% precision = K_Higgs structure direct test")
    return rows


# ----------------------------------------------------------------------
# Test 3: Future collider comparison
# ----------------------------------------------------------------------
def test3_future_colliders():
    print("\n[Test 3] Future collider comparison")
    colliders = [
        ("FCC-ee",          "CERN",        365,    "Higgs+Z+top precision (e⁺e⁻)",   "2045-2065"),
        ("FCC-hh",          "CERN",        100000, "Direct BSM up to 50 TeV (pp)",   "2070-2100"),
        ("CEPC + SppC",     "China",       100000, "Higgs factory + pp",             "2030s+"),
        ("ILC",             "Japan",       500,    "Higgs precision (e⁺e⁻)",         "TBD"),
        ("Muon Collider",   "TBD",         10000,  "Higgs+BSM (μ⁺μ⁻, low synch)",   "2040+"),
        ("CLIC",            "CERN",        3000,   "e⁺e⁻ multi-TeV alternative",     "Backup"),
    ]
    print(f"  {'Collider':<18}  {'Location':<10}  {'√s (GeV)':>10}  {'Purpose':<36}  {'Era'}")
    rows = []
    for name, loc, E, purpose, era in colliders:
        print(f"  {name:<18}  {loc:<10}  {E:>10}  {purpose:<36}  {era}")
        rows.append({"collider": name, "location": loc, "sqrt_s_GeV": E,
                     "purpose": purpose, "era": era})
    return rows


# ----------------------------------------------------------------------
# Test 4: BSM reach by collider energy
# ----------------------------------------------------------------------
def test4_bsm_reach():
    print("\n[Test 4] BSM reach by collider energy (gluino mass limit)")
    # Rough rule: gluino mass limit ~ √s / 5 for hadron colliders
    colliders = [
        ("LHC Run 2 (13 TeV)",       13.0,      2300),
        ("HL-LHC (14 TeV)",          14.0,      3000),
        ("FCC-hh (100 TeV)",         100.0,     20000),
        ("Muon Collider (10 TeV)",   10.0,      None),
    ]
    print(f"  {'Collider':<28}  {'√s (TeV)':>10}  {'Gluino reach (GeV)':>20}")
    rows = []
    for name, sqrts, m_gluino in colliders:
        m_str = f"~{m_gluino}" if m_gluino else "N/A (lepton)"
        print(f"  {name:<28}  {sqrts:>10}  {m_str:>20}")
        rows.append({"collider": name, "sqrt_s_TeV": sqrts,
                     "gluino_reach_GeV": m_gluino})
    return rows


# ----------------------------------------------------------------------
# Test 5: ITU verification priority map (9 experiments across Block A)
# ----------------------------------------------------------------------
def test5_itu_verification_priority():
    print("\n[Test 5] ITU verification priority map (Block A #17-#20)")
    experiments = [
        ("BMV (Bose 2017)",            "#17 QG K_geom",     2032, 0.65, "Strong"),
        ("LiteBIRD r ~ 0.001",         "#19 K_tensor",      2034, 0.85, "Strong"),
        ("EHT M87* 5 μas",             "#18 K_horizon",     2030, 0.90, "Strong"),
        ("DESI Y3 evolving DE",        "#19 K_Λ(t)",        2027, 0.75, "Strong"),
        ("HL-LHC Higgs λ_3",           "#20 K_Higgs",       2035, 0.85, "Strong"),
        ("FCC-hh BSM",                 "#20 K_BSM 5 TeV",   2070, 0.30, "Weak"),
        ("Muon g-2 Fermilab",          "#20 K_μ 4.2σ",      2025, 0.55, "Medium"),
        ("KamLAND-Zen 0νββ",           "#20 K_lepton",      2030, 0.40, "Medium"),
        ("IceCube cosmic ν",           "#20 K_ν_astro",     2025, 0.85, "Strong"),
    ]
    print(f"  {'Experiment':<30}  {'ITU target':<22}  {'Year':>5}  {'P':>5}  {'Verifiability'}")
    print("  " + "-" * 96)
    rows = []
    P_total = 0
    for name, target, year, P, ver in experiments:
        print(f"  {name:<30}  {target:<22}  {year:>5}  {P:>5.2f}  {ver}")
        rows.append({"experiment": name, "itu_target": target, "year": year,
                     "P": P, "verifiability": ver})
        P_total += P
    P_avg = P_total / len(experiments)
    print(f"\n  Block A 9-experiment verification P_avg = {P_avg:.3f}")
    return {"experiments": rows, "P_avg": P_avg}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
lhc = test1_lhc_runs()
self_coup = test2_higgs_self_coupling()
future = test3_future_colliders()
bsm = test4_bsm_reach()
priority = test5_itu_verification_priority()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: LHC integrated luminosity timeline
ax = axes[0, 0]
runs = [r["run"] for r in lhc]
L_vals = [r["integrated_luminosity_fbinv"] for r in lhc]
colors_lhc = ["#4c72b0", "#dd8452", "#55a467", "#c44e52"]
bars = ax.bar(runs, L_vals, color=colors_lhc)
for b, v in zip(bars, L_vals):
    ax.text(b.get_x() + b.get_width()/2, v + 50, f"{v} fb⁻¹",
            ha="center", fontsize=10, fontweight="bold")
ax.set_yscale("log")
ax.set_ylabel(r"Integrated luminosity (fb⁻¹)")
ax.set_title("LHC integrated luminosity per Run (HL-LHC ~ 100× Run 1)", fontsize=12)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 2: Future collider energies
ax = axes[0, 1]
names = [f["collider"] for f in future]
E_vals = [f["sqrt_s_GeV"] for f in future]
colors_fut = ["#4c72b0", "#c44e52", "#dd8452", "#55a467", "#8172b3", "#000000"]
ax.barh(names, E_vals, color=colors_fut[:len(names)])
for i, v in enumerate(E_vals):
    if v >= 1000:
        label = f"{v/1000:.0f} TeV"
    else:
        label = f"{v} GeV"
    ax.text(v * 1.2, i, label, va="center", fontsize=9)
ax.set_xscale("log")
ax.set_xlabel(r"√s (GeV)")
ax.set_title("Future collider center-of-mass energies", fontsize=12)
ax.grid(True, alpha=0.3, axis="x", which="both")
ax.invert_yaxis()

# Panel 3: BSM reach (gluino mass)
ax = axes[1, 0]
colliders_bsm = [b["collider"] for b in bsm if b["gluino_reach_GeV"]]
reach_vals = [b["gluino_reach_GeV"] for b in bsm if b["gluino_reach_GeV"]]
bars = ax.bar(colliders_bsm, reach_vals, color="#4c72b0")
for b, v in zip(bars, reach_vals):
    ax.text(b.get_x() + b.get_width()/2, v + 500, f"{v}",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel("Gluino mass reach (GeV)")
ax.set_title("BSM reach: gluino mass limit by collider", fontsize=12)
ax.grid(True, alpha=0.3, axis="y")
plt.setp(ax.get_xticklabels(), rotation=15, fontsize=9)

# Panel 4: ITU verification priority
ax = axes[1, 1]
exp_names = [e["experiment"] for e in priority["experiments"]]
P_vals = [e["P"] for e in priority["experiments"]]
ver = [e["verifiability"] for e in priority["experiments"]]
ver_colors = {"Strong": "#55a467", "Medium": "#dd8452", "Weak": "#c44e52"}
colors_v = [ver_colors[v] for v in ver]
ax.barh(exp_names, P_vals, color=colors_v)
for i, v in enumerate(P_vals):
    ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
ax.axvline(priority["P_avg"], color="red", linestyle="--", linewidth=1,
           label=f"P_avg = {priority['P_avg']:.3f}")
ax.set_xlabel("Verification probability P")
ax.set_xlim(0, 1.05)
ax.set_title("ITU verification priority (Block A #17-#20, 9 experiments)", fontsize=11)
ax.legend(fontsize=9, loc="lower right")
ax.grid(True, alpha=0.3, axis="x")
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.invert_yaxis()

fig.suptitle("Phase 141: LHC + Future Colliders + ITU Verification Platform",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "lhc_future_colliders.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 141,
    "title": "LHC + Future colliders + Particle Cosmology + ITU verification",
    "tier1_id": 20,
    "tier1_name": "Standard Model",
    "block": "A (Physics/Math) — paper 4/9, phase 7/8",
    "lhc_runs": lhc,
    "higgs_self_coupling_evolution": self_coup,
    "future_colliders": future,
    "bsm_reach": bsm,
    "itu_verification_priority": priority,
    "verdict": ("LHC Run 3 (2025) + HL-LHC (2041) = K_field mid-energy verification; "
                "FCC-hh (2100) + Muon Collider = 100 TeV K_BSM reach; "
                "Block A #17-#20 9 verification experiments with P_avg = "
                f"{priority['P_avg']:.3f}."),
}

json_path = "lhc_future_colliders_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 141 complete: LHC + future colliders = ITU verification platform;")
print(f"  Block A 9-experiment P_avg = {priority['P_avg']:.3f}")
print("=" * 70)
