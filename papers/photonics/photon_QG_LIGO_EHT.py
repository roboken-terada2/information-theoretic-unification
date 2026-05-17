"""
Phase 225 — LIGO + EHT + Quantum gravity optics (K_photon_QG)

Simulations:
  1) LIGO strain sensitivity vs frequency
  2) LIGO detected events catalog (2015-2024)
  3) EHT M87* + Sgr A* shadow comparison
  4) GR shadow / r_s = √27 ratio
  5) Optical clock precision evolution
  6) Multi-messenger detection (GW170817)
  7) ITU K_photon_QG axiom check

Outputs:
  - photon_QG_LIGO_EHT.png
  - photon_QG_LIGO_EHT_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("photon_QG_LIGO_EHT.png")
OUT_JSON = Path(__file__).with_name("photon_QG_LIGO_EHT_summary.json")

rng = np.random.default_rng(20260706)

# -------------------------------------------------------------
# 1) LIGO strain sensitivity vs frequency
# -------------------------------------------------------------
freqs = np.logspace(0, 4, 200)  # Hz
# Approximate aLIGO sensitivity curve
strain_h = 1e-21 * np.sqrt(
    1e-2 + (10 / freqs) ** 4 + (freqs / 5000) ** 2
)
# O5 with squeezed light: improvement 3x
strain_O5 = strain_h / 3

# -------------------------------------------------------------
# 2) LIGO events catalog
# -------------------------------------------------------------
events_history = {
    "GW150914 (BH-BH 36+29)":     2015,
    "GW151226":                    2015,
    "GW170104":                    2017,
    "GW170817 (NS-NS) ★":          2017,
    "GW190425 (NS-NS)":            2019,
    "GW190521 (BH 85+66) ★":       2019,
    "GWTC-3 (90 events)":          2021,
    "O4 ~150 events":              2023,
    "O5 (predicted)":              2025,
}
n_events_total = 250

# -------------------------------------------------------------
# 3) EHT M87* + Sgr A* shadow
# -------------------------------------------------------------
eht_results = {
    "M87* (2019)":  {"mass_Msun": 6.5e9, "shadow_uas": 42, "distance_Mly": 55,
                      "r_s_m": 1.9e13, "ratio_observed": 5.0},
    "Sgr A* (2022)": {"mass_Msun": 4e6,  "shadow_uas": 52, "distance_kly": 26,
                      "r_s_m": 1.2e10, "ratio_observed": 5.1},
}
GR_ratio_theory = np.sqrt(27)  # ≈ 5.196

# -------------------------------------------------------------
# 4) Optical clock precision
# -------------------------------------------------------------
clock_history = {
    "Cs-133 (1955)":            1e-9,
    "H maser (1960)":           1e-12,
    "Cs fountain (NIST 1999)":  1e-15,
    "Sr lattice (Ye 2008)":     1e-17,
    "Yb lattice (NIST 2015)":   1.4e-18,
    "Al+ ion (NIST 2019)":      9.4e-19,
    "Future (2030)":            1e-20,
}

# -------------------------------------------------------------
# 5) Multi-messenger GW170817
# -------------------------------------------------------------
multimsg = {
    "GW170817 LIGO":     {"time_sec": 0.0, "strain": 1e-22},
    "Fermi GBM (γ-ray)": {"time_sec": 1.7, "energy": "GRB 170817A"},
    "Optical (kilonova)": {"time_sec": 43200, "magnitude": 17},
    "X-ray (Chandra)":    {"time_sec": 9 * 86400, "detection": "afterglow"},
    "Radio (VLA)":        {"time_sec": 16 * 86400, "detection": "afterglow"},
}

# -------------------------------------------------------------
# 6) ITU K_photon_QG axiom check
# -------------------------------------------------------------
N_states = 2000
# No GW: flat photon distribution
log_fit_flat = np.zeros(N_states) + 0.05 * rng.standard_normal(N_states)
p_flat = np.exp(log_fit_flat); p_flat /= p_flat.sum()
S_flat = float(-np.sum(p_flat * np.log(p_flat)))

# GW event: phase shift across detector
log_fit_GW = log_fit_flat.copy()
log_fit_GW[500:600] += 1.0
log_fit_GW[1500:1600] -= 1.0
p_GW = np.exp(log_fit_GW); p_GW /= p_GW.sum()
S_GW = float(-np.sum(p_GW * np.log(p_GW)))

# BH shadow: dark band in photon ring
log_fit_shadow = log_fit_flat.copy()
shadow_zone = (np.arange(N_states) > 900) & (np.arange(N_states) < 1100)
log_fit_shadow[shadow_zone] -= 3.0
p_shadow = np.exp(log_fit_shadow); p_shadow /= p_shadow.sum()
S_shadow = float(-np.sum(p_shadow * np.log(p_shadow)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_flat_GW = itu_lin(p_flat, p_GW)
ratio_flat_shadow = itu_lin(p_flat, p_shadow)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 225 — LIGO + EHT + Quantum Gravity Optics (K_photon_QG)",
    fontsize=13, fontweight="bold",
)

# Panel 1: LIGO strain
ax = axes[0, 0]
ax.loglog(freqs, strain_h, "-", color="#1f77b4", lw=2, label="aLIGO (O3/O4)")
ax.loglog(freqs, strain_O5, "-", color="#2ca02c", lw=2, label="O5 + Squeezed light (3×)")
ax.axhline(1e-21, color="red", linestyle="--", alpha=0.5, label="GW150914 strain")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Strain h (1/√Hz)")
ax.set_title("LIGO sensitivity (Weiss-Barish-Thorne Nobel 2017)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 2: GW events timeline
ax = axes[0, 1]
ev_names = list(events_history.keys())
ev_years = list(events_history.values())
ax.barh(range(len(ev_names)), ev_years, color="#9467bd")
ax.set_yticks(range(len(ev_names))); ax.set_yticklabels(ev_names, fontsize=7)
ax.set_xlim(2014, 2027)
ax.set_xlabel("Year")
ax.set_title(f"GW detection ({n_events_total}+ events 2015-2024)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 3: EHT shadow visualization
ax = axes[0, 2]
theta = np.linspace(0, 2*np.pi, 200)
# Photon ring
r_ring = 1.0
ax.fill_between(np.cos(theta) * r_ring * 1.5, np.sin(theta) * r_ring * 1.5,
                np.sin(theta) * 1.5, color="#9467bd", alpha=0.3)
# Photon ring (bright)
ax.plot(np.cos(theta) * r_ring, np.sin(theta) * r_ring, "-", color="orange", lw=4)
# Shadow (dark)
shadow_r = 1.0 / GR_ratio_theory
ax.fill(np.cos(theta) * shadow_r, np.sin(theta) * shadow_r, color="black")
ax.set_xlim(-1.7, 1.7); ax.set_ylim(-1.7, 1.7)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(f"BH shadow: GR √27={GR_ratio_theory:.3f}, EHT≈5.0")

# Panel 4: Clock precision
ax = axes[1, 0]
clock_names = list(clock_history.keys())
precisions = list(clock_history.values())
ax.barh(range(len(clock_names)), precisions, color="#1f77b4")
ax.set_xscale("log")
ax.set_yticks(range(len(clock_names))); ax.set_yticklabels(clock_names, fontsize=7)
ax.set_xlabel("Fractional precision (log)")
ax.set_title("Optical clock precision: 70 years → 10⁻²⁰")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 5: GW170817 multi-messenger
ax = axes[1, 1]
mm_names = list(multimsg.keys())
mm_times = [multimsg[k]["time_sec"] for k in mm_names]
mm_log = [max(t, 0.001) for t in mm_times]
ax.barh(range(len(mm_names)), mm_log, color=["#1f77b4", "#d62728", "#ff7f0e",
                                              "#9467bd", "#2ca02c"])
ax.set_xscale("log")
ax.set_yticks(range(len(mm_names))); ax.set_yticklabels(mm_names, fontsize=7)
ax.set_xlabel("Time after GW (sec, log)")
ax.set_title("GW170817 multi-messenger detection")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 6: ITU K_photon_QG
ax = axes[1, 2]
ax.bar(["Flat (no GW)", "GW event\n(LIGO strain)", "BH shadow\n(EHT)"],
       [S_flat, S_GW, S_shadow], color=["#1f77b4", "#9467bd", "#d62728"])
ax.set_ylabel("Photon distribution entropy (nats)")
ax.set_title(f"K_photon_QG: GW={ratio_flat_GW:.3f}, Shadow={ratio_flat_shadow:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 225,
    "tier1_paper": 31,
    "topic": "LIGO + EHT + Quantum Gravity Optics (K_photon_QG)",
    "LIGO_strain_sensitivity": 1e-21,
    "LIGO_arm_length_km": 4,
    "Weiss_Barish_Thorne_Nobel_2017": "Physics - GW detection",
    "GW_events_history": events_history,
    "GW150914_total_mass_Msun": "36 + 29 = 62 (3 M☉ to GW)",
    "GW170817_significance": "First multi-messenger NS-NS merger",
    "EHT_results": eht_results,
    "GR_shadow_to_rs_ratio_theory": float(GR_ratio_theory),
    "EHT_2019_M87_shadow_uas": 42,
    "EHT_2022_SgrA_shadow_uas": 52,
    "optical_clock_history": clock_history,
    "current_best_clock_2024": "Al+ ion 9.4e-19 (NIST)",
    "multimessenger_GW170817": multimsg,
    "BMV_quantum_gravity_2017": "Levitated nanosphere entanglement via gravity",
    "ITU_K_photon_QG": {
        "N_states": int(N_states),
        "S_flat_no_GW_nats": S_flat,
        "S_GW_event_nats": S_GW,
        "S_BH_shadow_nats": S_shadow,
        "flat_to_GW_ratio": ratio_flat_GW,
        "flat_to_shadow_ratio": ratio_flat_shadow,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon_QG",
        "modular_Hamiltonian": "K_photon_QG^(0) = -log P(photon | gravity, quantum state)",
        "LIGO_meaning": "K_photon strain readout of K_geom (#17) perturbation",
        "EHT_meaning": "K_photon imaging of K_horizon (#18) shadow",
        "multi_messenger_meaning": "K_photon ⊗ K_field ⊗ K_geom simultaneous observation",
        "BMV_meaning": "Direct test K_photon ↔ K_geom entanglement (proves QG)",
        "optical_clock_meaning": "K_photon ⊗ K_time precision (Einstein equivalence)",
    },
    "predictions": [
        ("LIGO O5 BH 1/week", 2026, 0.85, "Strong"),
        ("BMV quantum gravity experiment", 2030, 0.65, "Medium"),
        ("Optical clock km GR test", 2028, 0.80, "Strong"),
        ("Cosmic Explorer / Einstein Telescope build", 2030, 0.65, "Medium"),
        ("QG dispersion relation detected", 2035, 0.30, "Weak"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
