# Phase 132: CMB Polarization E/B-modes + LiteBIRD + Primordial GW + ITU K_tensor
# Tier 1 #19 Cosmology (Block A paper 3/9, phase 6/8)
# ITU concept DOI: 10.5281/zenodo.20109209
# Tier 0 v3.0: 10.5281/zenodo.20200156
# Author: Munehiro Terada (Roboken)

import json
import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("Phase 132: CMB Polarization (E/B-modes) + LiteBIRD + Primordial GW")
print("=" * 70)
print()


# ----------------------------------------------------------------------
# Test 1: E-mode and B-mode power spectra (toy)
# ----------------------------------------------------------------------
def test1_E_B_spectra():
    print("[Test 1] E-mode + B-mode power spectra (toy model)")
    ell = np.logspace(0.7, 3.5, 300)   # 5 < ell < 3000

    # E-mode: acoustic peaks at lower amplitude than T
    EE_amp = 40.0   # μK^2 at peak
    EE_peak_pos = [140, 380, 600, 820]
    EE_peak_widths = [70, 100, 130, 160]
    EE_peak_amps = [40, 20, 18, 12]
    EE = np.zeros_like(ell)
    for pos, w, amp in zip(EE_peak_pos, EE_peak_widths, EE_peak_amps):
        EE += amp * np.exp(-((ell - pos) / w)**2)
    # damping tail
    EE *= np.exp(-((ell / 1500)**2))

    # B-mode: primordial (low ell bump) + lensing (high ell)
    r_value = 0.05   # tensor-to-scalar ratio
    # Primordial B (reionization bump @ ℓ ~ 5-10, recombination bump @ ℓ ~ 100)
    BB_prim_reion = 0.04 * r_value * np.exp(-((ell - 5) / 5)**2)
    BB_prim_recomb = 0.1 * r_value * np.exp(-((ell - 90) / 30)**2)
    BB_prim = BB_prim_reion + BB_prim_recomb

    # Lensing B-mode (peak at ℓ ~ 1000)
    BB_lens = 0.5 * np.exp(-((ell - 1000) / 600)**2) * (ell / 1000)**1.5
    BB_lens *= np.exp(-((ell / 3000)**2))

    BB_total = BB_prim + BB_lens

    print(f"  r (tensor-to-scalar ratio) = {r_value}")
    print(f"  E-mode peak ~ 40 μK² at ℓ ~ 140 (acoustic)")
    print(f"  B-mode primordial bumps:")
    print(f"    Reionization bump:   ℓ ~ 5,    amplitude ~ {BB_prim_reion.max():.2e} μK²")
    print(f"    Recombination bump:  ℓ ~ 100,  amplitude ~ {BB_prim_recomb.max():.2e} μK²")
    print(f"  B-mode lensing peak: ℓ ~ 1000,  amplitude ~ {BB_lens.max():.2e} μK²")
    return {"ell": ell.tolist(),
            "EE": EE.tolist(),
            "BB_prim": BB_prim.tolist(),
            "BB_lens": BB_lens.tolist(),
            "BB_total": BB_total.tolist(),
            "r_value": r_value}


# ----------------------------------------------------------------------
# Test 2: r upper limit history (extended from Phase 128)
# ----------------------------------------------------------------------
def test2_r_history():
    print("\n[Test 2] r upper limit timeline (extended)")
    history = [
        ("COBE (1992)",                    1.000),
        ("WMAP-1 (2003)",                  0.40),
        ("WMAP-7 (2010)",                  0.20),
        ("Planck 2013",                    0.12),
        ("BICEP2 false claim (2014)",     0.20),
        ("Planck + BICEP2 (2015)",        0.10),
        ("Planck 2018",                   0.10),
        ("BICEP/Keck + Planck (2021)",    0.06),
        ("BICEP3 / Keck (2024 forecast)", 0.03),
        ("LiteBIRD (2034 target)",        0.001),
        ("CMB-S4 (2030s target)",         0.0005),
    ]
    print(f"  {'Experiment':<32}  {'r upper limit':>15}")
    rows = []
    for name, r in history:
        print(f"  {name:<32}  {r:>15.4f}")
        rows.append({"experiment": name, "r_upper": r})
    return rows


# ----------------------------------------------------------------------
# Test 3: LiteBIRD sensitivity vs r
# ----------------------------------------------------------------------
def test3_litebird_sensitivity():
    print("\n[Test 3] LiteBIRD sensitivity 1σ(r) vs realistic forecast")
    # LiteBIRD spec: σ(r) ≈ 0.001 (Yamada 2023)
    sigma_r = 0.001
    # Detection power: 5σ requires r ≥ 5 × σ(r) = 0.005
    # Strong evidence (3σ): r ≥ 3 × σ(r) = 0.003
    print(f"  LiteBIRD 1σ(r) = {sigma_r}")
    print(f"  3σ detection threshold: r ≥ {3*sigma_r}")
    print(f"  5σ detection threshold: r ≥ {5*sigma_r}")

    # Inflation models
    models = [
        ("V = (1/2) m²φ² (chaotic)",       0.13,  "excluded by BICEP/Keck"),
        ("V = λφ⁴ (chaotic)",              0.26,  "excluded"),
        ("Starobinsky R²",                 0.003, "5σ LiteBIRD detection borderline"),
        ("V = φ²/M_P (axion monodromy)",   0.07,  "excluded"),
        ("Higgs inflation",                0.003, "5σ LiteBIRD borderline"),
        ("Hilltop inflation",              1e-5,  "below LiteBIRD"),
        ("D-brane inflation",              1e-7,  "below CMB-S4"),
    ]
    print()
    print(f"  {'Inflation model':<32}  {'r prediction':>14}  {'LiteBIRD status'}")
    rows = []
    for name, r, status in models:
        print(f"  {name:<32}  {r:>14.3e}  {status}")
        rows.append({"model": name, "r_prediction": r, "litebird_status": status})
    return {"sigma_r": sigma_r, "models": rows}


# ----------------------------------------------------------------------
# Test 4: Inflation energy scale vs r
# ----------------------------------------------------------------------
def test4_inflation_scale():
    print("\n[Test 4] Inflation energy scale V^{1/4} vs r")
    r_arr = np.logspace(-7, -1, 100)
    # V^{1/4} = (r / 0.01)^{1/4} × 10^{16} GeV
    V_quarter_GeV = (r_arr / 0.01)**(1/4) * 1e16

    samples = [1e-6, 1e-5, 1e-4, 0.001, 0.01, 0.06, 0.1]
    print(f"  {'r':>10}  {'V^{1/4} (GeV)':>18}")
    rows = []
    for r in samples:
        V_q = (r / 0.01)**(1/4) * 1e16
        print(f"  {r:>10.3e}  {V_q:>18.4e}")
        rows.append({"r": float(r), "V_quarter_GeV": float(V_q)})
    print()
    print(f"  → GUT scale (10^16 GeV) corresponds to r ~ 0.01")
    print(f"  → r = 0.001 (LiteBIRD): V^{{1/4}} ~ 5.6 × 10^{{15}} GeV (near GUT)")
    return {"r_arr": r_arr.tolist(), "V_q_GeV": V_quarter_GeV.tolist(),
            "samples": rows}


# ----------------------------------------------------------------------
# Test 5: Foreground contamination
# ----------------------------------------------------------------------
def test5_foreground():
    print("\n[Test 5] CMB B-mode foregrounds")
    components = [
        ("Synchrotron",      "low freq < 100 GHz",   "polarized, B/T ~ 1%"),
        ("Thermal dust",     "high freq > 100 GHz",  "polarized, B/T ~ 5%"),
        ("Spinning dust",    "30-50 GHz",            "polarized, ~ negligible"),
        ("CO line emission", "115 GHz, 230 GHz",     "small, can mask"),
        ("Free-free",        "low freq",             "unpolarized"),
    ]
    print(f"  {'Component':<22}  {'Frequency range':<22}  {'Polarization'}")
    rows = []
    for name, freq, pol in components:
        print(f"  {name:<22}  {freq:<22}  {pol}")
        rows.append({"name": name, "freq_range": freq, "polarization": pol})
    print()
    print(f"  LiteBIRD 15 bands (40-402 GHz) separates components")
    print(f"  Component separation accuracy crucial for r ~ 0.001")
    return rows


# ----------------------------------------------------------------------
# Run all tests
# ----------------------------------------------------------------------
spectra = test1_E_B_spectra()
r_hist = test2_r_history()
litebird = test3_litebird_sensitivity()
v_scale = test4_inflation_scale()
fg = test5_foreground()


# ----------------------------------------------------------------------
# Figure: 4-panel
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: E + B power spectra
ax = axes[0, 0]
ell = np.array(spectra["ell"])
ax.loglog(ell, spectra["EE"], "-", color="#4c72b0", linewidth=2, label="E-mode (scalar)")
ax.loglog(ell, spectra["BB_prim"], "-", color="#c44e52", linewidth=2,
          label=f"B-mode primordial (r={spectra['r_value']})")
ax.loglog(ell, spectra["BB_lens"], "--", color="#dd8452", linewidth=2,
          label="B-mode lensing (secondary)")
ax.set_xlabel(r"Multipole $\ell$")
ax.set_ylabel(r"$C_\ell$ (μK²)")
ax.set_title("CMB polarization spectra: E + B-modes", fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")
ax.set_ylim(1e-5, 100)

# Panel 2: r history
ax = axes[0, 1]
exps = [r["experiment"] for r in r_hist]
r_lims = [r["r_upper"] for r in r_hist]
colors = ["red" if "false" in e else ("green" if "target" in e else "#4c72b0") for e in exps]
ax.barh(exps, r_lims, color=colors)
for i, v in enumerate(r_lims):
    ax.text(v * 1.1, i, f"{v}", va="center", fontsize=8)
ax.set_xscale("log")
ax.set_xlabel(r"r upper limit / target")
ax.set_title("Tensor-to-scalar ratio r: observational + target history", fontsize=11)
ax.grid(True, alpha=0.3, which="both", axis="x")
plt.setp(ax.get_yticklabels(), fontsize=7)
ax.invert_yaxis()

# Panel 3: V^{1/4} vs r (inflation scale)
ax = axes[1, 0]
r_arr = np.array(v_scale["r_arr"])
V_q = np.array(v_scale["V_q_GeV"])
ax.loglog(r_arr, V_q, "-", color="#4c72b0", linewidth=2)
ax.axvline(0.06, color="orange", linestyle="--", linewidth=1, label="P+BK 2021 limit")
ax.axvline(0.001, color="green", linestyle="--", linewidth=1, label="LiteBIRD target")
ax.axhline(1e16, color="gray", linestyle=":", linewidth=1, label="GUT scale 10^16 GeV")
# Annotate key models
models_keys = [("Starobinsky", 0.003, 5.6e15), ("φ² chaotic (excluded)", 0.13, 2e16)]
for name, r, V in models_keys:
    ax.scatter(r, V, marker="o", color="red", s=80, zorder=5)
    ax.annotate(name, (r, V), textcoords="offset points", xytext=(5, 5), fontsize=8)
ax.set_xlabel("r (tensor-to-scalar ratio)")
ax.set_ylabel(r"$V^{1/4}$ (GeV)")
ax.set_title(r"Inflation energy scale: $V^{1/4}$ = (r/0.01)$^{1/4}$ × 10$^{16}$ GeV", fontsize=11)
ax.legend(fontsize=9, loc="upper left")
ax.grid(True, alpha=0.3, which="both")

# Panel 4: LiteBIRD detection table + foregrounds
ax = axes[1, 1]
ax.axis("off")
ax.set_title("LiteBIRD inflation model discrimination", fontsize=12, fontweight="bold")
y = 0.92
ax.text(0.02, y, "Model", fontsize=9, fontweight="bold")
ax.text(0.45, y, "r prediction", fontsize=9, fontweight="bold")
ax.text(0.70, y, "LiteBIRD verdict", fontsize=9, fontweight="bold")
y -= 0.05
for m in litebird["models"][:7]:
    ax.text(0.02, y, m["model"], fontsize=8, color="#4c72b0")
    ax.text(0.45, y, f"{m['r_prediction']:.3e}", fontsize=8, fontfamily="monospace")
    ax.text(0.70, y, m["litebird_status"], fontsize=8, color="#c44e52")
    y -= 0.09
ax.text(0.02, 0.05, "Foreground separation crucial: 15 bands 40-402 GHz",
        fontsize=9, fontstyle="italic", color="#55a467")

fig.suptitle("Phase 132: CMB Polarization (E/B-modes) + LiteBIRD + Primordial GW",
             fontsize=13, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])

png_path = "cmb_polarization_litebird.png"
plt.savefig(png_path, dpi=120)
print(f"\n  Figure saved: {png_path}")


# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 132,
    "title": "CMB Polarization E/B-modes + LiteBIRD + Primordial GW",
    "tier1_id": 19,
    "tier1_name": "Cosmology",
    "block": "A (Physics/Math) — paper 3/9, phase 6/8",
    "E_B_spectra_toy": {
        "EE_peaks_ell": [140, 380, 600, 820],
        "BB_primordial_peaks_ell": [5, 90],
        "BB_lensing_peak_ell": 1000,
        "r_value_demo": spectra["r_value"],
    },
    "r_history": r_hist,
    "litebird_sensitivity": litebird,
    "inflation_scale": v_scale,
    "foregrounds": fg,
    "verdict": ("CMB B-mode = primordial GW = inflation K_tensor signature. "
                "LiteBIRD 2032 launch targets r ~ 0.001 (5σ), CMB-S4 r ~ 0.0005 (2030s). "
                "Starobinsky R² inflation (r ~ 0.003) detectable with 3σ. Foreground "
                "separation across 15 bands (40-402 GHz) crucial."),
}

json_path = "cmb_polarization_litebird_summary.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"  JSON saved: {json_path}")

print()
print("=" * 70)
print("Phase 132 complete: B-mode = K_tensor inflation signature;")
print(f"  LiteBIRD 2032 r ~ 0.001; CMB-S4 r ~ 0.0005; Starobinsky borderline")
print("=" * 70)
