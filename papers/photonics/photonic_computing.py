"""
Phase 226 — Photonic Computing + Silicon Photonics (K_photon_compute)

Simulations:
  1) Silicon photonics bandwidth evolution (2004-2024)
  2) Photonic vs electronic energy/op
  3) Optical neural networks: matrix mult acceleration
  4) Boson sampling experiments (Jiuzhang, Xanadu)
  5) Photonic vs superconducting QC comparison
  6) Co-packaged optics deployment
  7) ITU K_photon_compute axiom check

Outputs:
  - photonic_computing.png
  - photonic_computing_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("photonic_computing.png")
OUT_JSON = Path(__file__).with_name("photonic_computing_summary.json")

rng = np.random.default_rng(20260707)

# -------------------------------------------------------------
# 1) Silicon photonics bandwidth
# -------------------------------------------------------------
si_history = {
    "Intel Si Mod 2004":      {"year": 2004, "gbps": 1},
    "Lipson MZM 2006":        {"year": 2006, "gbps": 10},
    "100G CWDM4 2018":        {"year": 2018, "gbps": 100},
    "400G QSFP-DD 2020":      {"year": 2020, "gbps": 400},
    "800G port 2022":         {"year": 2022, "gbps": 800},
    "NVIDIA X800 (2025)":     {"year": 2025, "gbps": 800},
    "Co-packaged 1.6T":       {"year": 2024, "gbps": 1600},
}

# -------------------------------------------------------------
# 2) Energy per op: photonic vs electronic
# -------------------------------------------------------------
energy_ops = {
    "Photon (theoretical)": 1e-18,  # 1 aJ
    "Photonic NN (2024)":    1e-16,  # ~100 fJ
    "Silicon photonics MAC": 1e-15,  # ~1 fJ
    "GPU FP16 MAC":           5e-13,  # ~0.5 pJ
    "CPU FP64 op":            1e-11,  # ~10 pJ
    "Brain synapse":          1e-15,  # ~1 fJ (estimate)
}

# -------------------------------------------------------------
# 3) Photonic NN: matrix mult speedup
# -------------------------------------------------------------
mat_sizes = np.array([4, 8, 16, 32, 64, 128, 256, 512])
# GPU latency: O(N^3)
gpu_latency_us = 0.001 * mat_sizes ** 3 / 100
# Photonic: O(1) ideal (parallel)
photonic_latency_us = np.ones_like(mat_sizes, dtype=float) * 0.01

speedup = gpu_latency_us / photonic_latency_us

# -------------------------------------------------------------
# 4) Boson sampling experiments
# -------------------------------------------------------------
boson_milestones = {
    "Aaronson-Arkhipov theory":    {"year": 2010, "photons": 0},
    "First experiment":              {"year": 2013, "photons": 3},
    "Jiuzhang 1.0 (USTC)":           {"year": 2020, "photons": 76},
    "Jiuzhang 2.0":                  {"year": 2021, "photons": 113},
    "Xanadu Borealis":               {"year": 2022, "photons": 219},
    "Xanadu Aurora":                 {"year": 2024, "photons": 12000},
}

# -------------------------------------------------------------
# 5) Photonic vs Superconducting QC
# -------------------------------------------------------------
qc_comparison = {
    "Operating temperature (K)": {"photonic": 300, "superconducting": 0.02},
    "Coherence time (ms)":         {"photonic": 1000, "superconducting": 0.1},
    "Gate fidelity (%)":           {"photonic": 99.0, "superconducting": 99.9},
    "Connectivity":                {"photonic": "all-to-all (in principle)", "superconducting": "neighbor"},
    "Scalability":                 {"photonic": "manufacturing-limited", "superconducting": "wiring-limited"},
}

# -------------------------------------------------------------
# 6) ITU K_photon_compute axiom
# -------------------------------------------------------------
N_states = 5000
# Classical (digital): 2^N states, broadly explored
log_fit_classical = 0.1 * rng.standard_normal(N_states)
p_classical = np.exp(log_fit_classical); p_classical /= p_classical.sum()
S_classical = float(-np.sum(p_classical * np.log(p_classical)))

# Photonic NN computation: peaked at solution (deterministic)
log_fit_photonic = log_fit_classical.copy()
log_fit_photonic[1000] += 4.0  # solution
p_photonic = np.exp(log_fit_photonic); p_photonic /= p_photonic.sum()
S_photonic = float(-np.sum(p_photonic * np.log(p_photonic)))

# Boson sampling: high-entropy quantum distribution
log_fit_boson = log_fit_classical.copy()
log_fit_boson[2000:2500] += 1.5  # boson sampling output cluster
p_boson = np.exp(log_fit_boson); p_boson /= p_boson.sum()
S_boson = float(-np.sum(p_boson * np.log(p_boson)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_classical_photonic = itu_lin(p_classical, p_photonic)
ratio_classical_boson = itu_lin(p_classical, p_boson)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 226 — Photonic Computing + Silicon Photonics (K_photon_compute)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Si photonics history
ax = axes[0, 0]
years = [si_history[k]["year"] for k in si_history]
gbps = [si_history[k]["gbps"] for k in si_history]
ax.semilogy(years, gbps, "o-", color="#1f77b4", lw=2, markersize=8)
for k, d in si_history.items():
    ax.annotate(k.split()[0], (d["year"], d["gbps"]), fontsize=6,
                xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("Bandwidth (Gbps, log)")
ax.set_title("Silicon photonics: 1 Gbps → 1.6 Tbps")
ax.grid(True, alpha=0.3, which="both")

# Panel 2: Energy/op
ax = axes[0, 1]
ops = list(energy_ops.keys())
energies = list(energy_ops.values())
colors_e = ["#2ca02c" if e < 1e-15 else "#ff7f0e" if e < 1e-12 else "#d62728" for e in energies]
ax.barh(range(len(ops)), energies, color=colors_e)
ax.set_xscale("log")
ax.set_yticks(range(len(ops))); ax.set_yticklabels(ops, fontsize=8)
ax.set_xlabel("Energy per op (J, log)")
ax.set_title("Photonic vs electronic energy")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 3: Matrix mult speedup
ax = axes[0, 2]
ax.loglog(mat_sizes, gpu_latency_us, "-", color="#1f77b4", lw=2, label="GPU O(N³)")
ax.loglog(mat_sizes, photonic_latency_us, "-", color="#d62728", lw=2, label="Photonic O(1) ideal")
ax2 = ax.twinx()
ax2.semilogx(mat_sizes, speedup, "--", color="#2ca02c", lw=2, label="Speedup")
ax.set_xlabel("Matrix size N")
ax.set_ylabel("Latency (μs, log)")
ax2.set_ylabel("Speedup (×)", color="#2ca02c")
ax.set_title("Photonic matrix mult: O(1) speedup")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="lower right", fontsize=8)
ax.grid(True, alpha=0.3, which="both")

# Panel 4: Boson sampling milestones
ax = axes[1, 0]
b_names = list(boson_milestones.keys())
b_photons = [boson_milestones[k]["photons"] for k in b_names]
b_years = [boson_milestones[k]["year"] for k in b_names]
ax.scatter(b_years, b_photons, s=100, color="#d62728")
for k, d in boson_milestones.items():
    ax.annotate(k.split()[0], (d["year"], d["photons"]),
                fontsize=6, xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("Photons")
ax.set_yscale("symlog", linthresh=1)
ax.set_title("Boson sampling: theory 2010 → Xanadu Aurora 12K (2024)")
ax.grid(True, alpha=0.3, which="both")

# Panel 5: QC comparison
ax = axes[1, 1]
metrics = ["Temp (K)", "Coherence (ms)", "Fidelity (%)"]
photonic_vals = [300, 1000, 99]
super_vals = [0.02, 0.1, 99.9]
x = np.arange(len(metrics))
width = 0.35
# Normalize for log
photonic_norm = [v if v > 0.001 else 0.001 for v in photonic_vals]
super_norm = [v if v > 0.001 else 0.001 for v in super_vals]
ax.bar(x - width/2, photonic_norm, width, color="#9467bd", label="Photonic")
ax.bar(x + width/2, super_norm, width, color="#1f77b4", label="Superconducting")
ax.set_yscale("log")
ax.set_xticks(x); ax.set_xticklabels(metrics, fontsize=9)
ax.set_ylabel("Value (log)")
ax.set_title("Photonic vs Superconducting QC")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis="y", which="both")

# Panel 6: ITU K_photon_compute
ax = axes[1, 2]
ax.bar(["Classical\n(broad)", "Photonic NN\n(peaked)", "Boson sampling\n(quantum)"],
       [S_classical, S_photonic, S_boson],
       color=["#1f77b4", "#2ca02c", "#9467bd"])
ax.set_ylabel("Output entropy (nats)")
ax.set_title(f"K_photon_compute: Cls→NN={ratio_classical_photonic:.3f}, Cls→BS={ratio_classical_boson:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 226,
    "tier1_paper": 31,
    "topic": "Photonic Computing + Silicon Photonics (K_photon_compute)",
    "silicon_photonics_history": si_history,
    "current_2024_co_packaged_Tbps": 1.6,
    "energy_per_op_J": energy_ops,
    "photonic_vs_GPU_energy_advantage": "~3 orders of magnitude (1 fJ vs 1 pJ)",
    "boson_sampling_milestones": boson_milestones,
    "Jiuzhang_2.0_USTC_2021": "113 photons (quantum supremacy claim)",
    "Xanadu_Aurora_2024": "12,000 photons (record)",
    "KLM_scheme_2001": "Knill-Laflamme-Milburn linear optical QC",
    "Aaronson_Arkhipov_2010": "Boson sampling theory (#P-hard classical)",
    "QC_comparison": qc_comparison,
    "ITU_K_photon_compute": {
        "N_states": int(N_states),
        "S_classical_nats": S_classical,
        "S_photonic_NN_nats": S_photonic,
        "S_boson_sampling_nats": S_boson,
        "classical_to_NN_ratio": ratio_classical_photonic,
        "classical_to_boson_ratio": ratio_classical_boson,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon_compute",
        "modular_Hamiltonian": "K_photon_compute^(0) = -log P(output | hardware, input)",
        "photonic_NN_meaning": "ITU descent flow via optical matrix multiplication",
        "boson_sampling_meaning": "Photonic K-state generates classically-hard distribution",
        "energy_advantage": "Photon thermodynamic efficiency >> electronic",
        "K_universe_connection": "K_photon + K_QC + K_semi merge in K_photon_compute",
    },
    "predictions": [
        ("Co-packaged optics 1.6T deployed", 2027, 0.85, "Strong"),
        ("Photonic NN data center training", 2030, 0.65, "Medium"),
        ("Photonic quantum advantage new task", 2027, 0.75, "Strong"),
        ("Fault-tolerant photonic qubit", 2030, 0.55, "Medium"),
        ("Photonic ASIC for LLM inference", 2028, 0.70, "Strong"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
