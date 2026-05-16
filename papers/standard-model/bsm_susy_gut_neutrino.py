# Phase 140: BSM — SUSY + GUT + Neutrino mass + Leptogenesis + ITU K_BSM
# Tier 1 #20 Standard Model (Block A paper 4/9, phase 6/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 140: BSM — SUSY + GUT + Neutrino Mass + ITU K_BSM")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: SUSY mass limits from LHC 2024
# ----------------------------------------------------------------------
def test1_susy_limits():
    print("[Test 1] SUSY mass limits from LHC 2024")
    limits = [
        ("Gluino (g̃)",      2300,  "strong"),
        ("Squark (q̃)",      1900,  "strong"),
        ("Stop (t̃)",        1200,  "third gen"),
        ("Sbottom (b̃)",     1300,  "third gen"),
        ("Chargino (χ̃⁺)",   900,   "EW"),
        ("Slepton (ℓ̃)",     700,   "EW"),
        ("Neutralino LSP",   100,   "DM candidate"),
    ]
    print(f"  {'SUSY particle':<22}  {'Lower limit (GeV)':>18}  {'Category'}")
    rows = []
    for name, m_lim, cat in limits:
        print(f"  {name:<22}  {m_lim:>18}  {cat}")
        rows.append({"particle": name, "lower_limit_GeV": m_lim, "category": cat})
    print(f"\n  → Natural SUSY (m_SUSY ~ 100 GeV-1 TeV) excluded for strongly-coupled")
    print(f"  → Higher-scale SUSY (10 TeV+) only partially solves hierarchy")
    return rows


# ----------------------------------------------------------------------
# Test 2: Proton decay (Super-K vs theoretical predictions)
# ----------------------------------------------------------------------
def test2_proton_decay():
    print("\n[Test 2] Proton decay lifetime")
    predictions = [
        ("Minimal SU(5)",        "p → e⁺ π⁰",  1e30,  1e32,  "EXCLUDED"),
        ("SUSY-SU(5)",           "p → e⁺ π⁰",  1e34,  1e36,  "limit reached"),
        ("Minimal SO(10)",       "p → e⁺ π⁰",  1e34,  1e36,  "limit reached"),
        ("Flipped SU(5)",        "various",     1e35,  1e37,  "above current limit"),
        ("Pati-Salam (no GUT)",  "no decay",   1e40,  1e45,  "very long"),
    ]
    Super_K_2020_limit = 2.4e34   # τ_p > 2.4e34 yr for p → e⁺ π⁰

    print(f"  {'Theory':<22}  {'Mode':<14}  {'τ_p (yr)':<24}  {'Status'}")
    rows = []
    for name, mode, t_min, t_max, status in predictions:
        if t_min < Super_K_2020_limit < t_max:
            note = "PARTIAL EXCLUDED"
        elif t_max < Super_K_2020_limit:
            note = "EXCLUDED"
        else:
            note = "ALIVE"
        print(f"  {name:<22}  {mode:<14}  {t_min:>9.0e}-{t_max:>9.0e}  {note}")
        rows.append({"theory": name, "mode": mode,
                     "tau_p_min_yr": t_min, "tau_p_max_yr": t_max,
                     "status": note})
    print(f"\n  Super-K 2020 limit (p → e⁺ π⁰): τ_p > {Super_K_2020_limit:.1e} yr")
    print(f"  → Minimal SU(5) excluded; SO(10) + SUSY-SU(5) still viable")
    return {"predictions": rows, "Super_K_limit_yr": Super_K_2020_limit}


# ----------------------------------------------------------------------
# Test 3: Neutrino mass mechanisms
# ----------------------------------------------------------------------
def test3_neutrino_mass():
    print("\n[Test 3] Neutrino mass mechanisms")

    # Dirac mass via tiny Yukawa
    v_higgs = 246.22   # GeV
    m_nu_target = 0.1e-9  # 0.1 eV in GeV
    y_nu_Dirac = m_nu_target * np.sqrt(2) / v_higgs
    y_e = 2.94e-6   # electron Yukawa
    ratio_y = y_e / y_nu_Dirac

    print(f"  Dirac mass approach: m_ν = y_ν × v/√2")
    print(f"    For m_ν = 0.1 eV: y_ν = {y_nu_Dirac:.2e}")
    print(f"    Electron Yukawa: y_e = {y_e:.2e}")
    print(f"    y_e / y_ν = {ratio_y:.2e} (Yukawa hierarchy worsens by ~6 orders)")

    # See-saw mechanism
    m_D = 100.0   # GeV (Dirac mass ~ top mass)
    M_R = 1e14    # GeV (Majorana mass at GUT scale)
    m_nu_seesaw = m_D**2 / M_R * 1e9   # in eV
    print(f"\n  See-saw mechanism: m_ν = m_D² / M_R")
    print(f"    m_D ~ {m_D} GeV (electroweak)")
    print(f"    M_R ~ {M_R:.0e} GeV (GUT scale Majorana)")
    print(f"    m_ν = {m_nu_seesaw:.4f} eV  ← natural for ~0.1 eV")
    return {
        "Dirac_yukawa": float(y_nu_Dirac),
        "y_e_to_y_nu_ratio": float(ratio_y),
        "seesaw_m_D_GeV": m_D, "seesaw_M_R_GeV": M_R,
        "seesaw_m_nu_eV": float(m_nu_seesaw),
    }


# ----------------------------------------------------------------------
# Test 4: Neutrino mass observational limits
# ----------------------------------------------------------------------
def test4_neutrino_limits():
    print("\n[Test 4] Neutrino mass observational constraints")
    limits = [
        ("KATRIN 2022 (β decay)",         "m_ν^β",     0.8,    "eV"),
        ("Planck 2018 (cosmology)",       "Σ m_ν",     0.12,   "eV"),
        ("KamLAND-Zen 2024 (0νββ)",       "m_ν^{Maj}", 0.036,  "eV (lower edge)"),
        ("LEGEND-200 (planned 2027)",     "m_ν^{Maj}", 0.020,  "eV target"),
        ("LEGEND-1000 (planned 2030+)",   "m_ν^{Maj}", 0.010,  "eV target"),
    ]
    print(f"  {'Experiment':<30}  {'Observable':<14}  {'Limit/Target'}")
    rows = []
    for name, obs, lim, unit in limits:
        print(f"  {name:<30}  {obs:<14}  < {lim} {unit}")
        rows.append({"experiment": name, "observable": obs,
                     "limit_or_target": lim, "unit": unit})

    print(f"\n  → m_ν likely O(10-100) meV per state")
    print(f"  → Δm² values fix differences but not absolute scale")
    return rows


# ----------------------------------------------------------------------
# Test 5: Baryon asymmetry η_B and leptogenesis
# ----------------------------------------------------------------------
def test5_baryon_asymmetry():
    print("\n[Test 5] Baryon asymmetry of the universe")
    eta_B_obs = 6.0e-10   # n_B / n_γ
    print(f"  η_B = (n_B - n_B̄) / n_γ = {eta_B_obs}")
    print(f"\n  Sakharov conditions (1967):")
    print(f"    1. Baryon number violation")
    print(f"    2. C and CP violation")
    print(f"    3. Out of thermal equilibrium")
    print()
    print(f"  Mechanisms:")
    candidates = [
        ("Electroweak Baryogenesis",  "EW phase transition (1st order)", "SM + extra Higgs/SUSY"),
        ("Leptogenesis",              "Heavy ν_R decay → lepton asymmetry → sphaleron",
         "Natural with See-saw + Majorana neutrinos"),
        ("GUT Baryogenesis",          "X, Y gauge boson decays (10¹⁶ GeV)",
         "Requires SU(5)/SO(10)"),
    ]
    print(f"  {'Mechanism':<26}  {'Process':<40}  {'Requirement'}")
    for name, proc, req in candidates:
        print(f"  {name:<26}  {proc:<40}  {req}")
    print()
    print(f"  → Leptogenesis = preferred (connects neutrino mass + baryon asymmetry)")
    return {"eta_B": eta_B_obs, "mechanisms": [
        {"name": n, "process": p, "requirement": r} for n, p, r in candidates
    ]}


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
susy = test1_susy_limits()
proton = test2_proton_decay()
nu_mech = test3_neutrino_mass()
nu_limits = test4_neutrino_limits()
baryon = test5_baryon_asymmetry()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: SUSY mass limits
ax = axes[0, 0]
names = [s["particle"] for s in susy]
limits = [s["lower_limit_GeV"] for s in susy]
cats = [s["category"] for s in susy]
cat_colors = {"strong": "#c44e52", "third gen": "#dd8452", "EW": "#4c72b0", "DM candidate": "#55a467"}
colors = [cat_colors[c] for c in cats]
ax.barh(names, limits, color=colors)
for i, v in enumerate(limits):
    ax.text(v + 50, i, f"{v}", va="center", fontsize=9)
ax.set_xlabel("Lower mass limit (GeV)")
ax.set_title("SUSY mass limits (LHC 2024)", fontsize=12)
ax.grid(True, alpha=0.3, axis="x")
ax.invert_yaxis()

# Panel 2: Proton decay
ax = axes[0, 1]
theories = [p["theory"] for p in proton["predictions"]]
t_mins = [p["tau_p_min_yr"] for p in proton["predictions"]]
t_maxs = [p["tau_p_max_yr"] for p in proton["predictions"]]
y_pos = np.arange(len(theories))
for i, (tmin, tmax) in enumerate(zip(t_mins, t_maxs)):
    ax.barh(i, np.log10(tmax) - np.log10(tmin), left=np.log10(tmin), color="#4c72b0", alpha=0.7)
    ax.text(np.log10(tmin) - 0.5, i, f"{np.log10(tmin):.0f}", ha="right", fontsize=8)
    ax.text(np.log10(tmax) + 0.5, i, f"{np.log10(tmax):.0f}", ha="left", fontsize=8)
ax.axvline(np.log10(proton["Super_K_limit_yr"]), color="red", linestyle="--", linewidth=1.5,
           label=f"Super-K 2020 ({proton['Super_K_limit_yr']:.1e} yr)")
ax.set_yticks(y_pos)
ax.set_yticklabels(theories, fontsize=9)
ax.set_xlabel(r"$\log_{10}(\tau_p / yr)$")
ax.set_title("Proton decay τ_p: theory vs Super-K limit", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis="x")
ax.invert_yaxis()

# Panel 3: See-saw mechanism diagram
ax = axes[1, 0]
ax.axis("off")
ax.set_title("See-saw mechanism: tiny m_ν from heavy M_R", fontsize=12, fontweight="bold")
y = 0.85
ax.text(0.02, y, "Dirac approach (SM + ν_R):", fontsize=11, fontweight="bold", color="#c44e52")
ax.text(0.05, y - 0.08, f"  m_ν = y_ν × v / √2", fontsize=10, fontfamily="monospace")
ax.text(0.05, y - 0.16, f"  For m_ν = 0.1 eV: y_ν = {nu_mech['Dirac_yukawa']:.2e}", fontsize=10)
ax.text(0.05, y - 0.24, f"  y_e / y_ν = {nu_mech['y_e_to_y_nu_ratio']:.2e}", fontsize=10, color="#c44e52")

y = 0.45
ax.text(0.02, y, "See-saw approach:", fontsize=11, fontweight="bold", color="#55a467")
ax.text(0.05, y - 0.08, f"  m_ν = m_D² / M_R", fontsize=10, fontfamily="monospace")
ax.text(0.05, y - 0.16, f"  m_D = {nu_mech['seesaw_m_D_GeV']} GeV (electroweak)", fontsize=10)
ax.text(0.05, y - 0.24, f"  M_R = {nu_mech['seesaw_M_R_GeV']:.0e} GeV (GUT Majorana)", fontsize=10)
ax.text(0.05, y - 0.32, f"  → m_ν = {nu_mech['seesaw_m_nu_eV']:.3f} eV ✓",
        fontsize=11, fontweight="bold", color="#55a467")

# Panel 4: Neutrino mass limits
ax = axes[1, 1]
experiments = [n["experiment"] for n in nu_limits]
m_lims = [n["limit_or_target"] for n in nu_limits]
ax.barh(experiments, m_lims, color="#4c72b0")
for i, v in enumerate(m_lims):
    ax.text(v * 1.5, i, f"{v} eV", va="center", fontsize=9)
ax.set_xlabel("m_ν limit / target (eV)")
ax.set_xscale("log")
ax.set_title("Neutrino mass upper limits/targets", fontsize=12)
ax.grid(True, alpha=0.3, which="both", axis="x")
ax.invert_yaxis()

fig.suptitle("Phase 140: BSM — SUSY + GUT + Neutrino Mass + Leptogenesis",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "bsm_susy_gut_neutrino.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 140,
    "title": "BSM — SUSY + GUT + Neutrino Mass + Leptogenesis + ITU K_BSM",
    "tier1_id": 20,
    "tier1_name": "Standard Model",
    "block": "A (Physics/Math) — paper 4/9, phase 6/8",
    "susy_limits_LHC2024": susy,
    "proton_decay": proton,
    "neutrino_mechanisms": nu_mech,
    "neutrino_mass_limits": nu_limits,
    "baryon_asymmetry": baryon,
    "verdict": ("BSM candidates: SUSY (LHC pushed to TeV+, natural fine-tuning hurt); "
                "GUT (minimal SU(5) excluded by τ_p, SO(10)/SUSY-SU(5) viable); "
                "Neutrino See-saw natural with M_R ~ GUT scale and m_ν ~ 0.1 eV; "
                "Leptogenesis ties neutrino mass + baryon asymmetry η_B = 6e-10."),
}

json_path = "bsm_susy_gut_neutrino_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 140 complete: BSM = K_BSM hypothesis space in ITU;")
print(f"  See-saw m_ν = 0.1 eV; Leptogenesis ties to η_B = {baryon['eta_B']:.1e}")
print("=" * 70)
