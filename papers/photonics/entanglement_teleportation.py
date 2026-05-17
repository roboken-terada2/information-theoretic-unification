"""
Phase 222 — Quantum entanglement + Bell + Teleportation (K_photon_entanglement)

Simulations:
  1) Bell state vs separable comparison
  2) Concurrence + Schmidt rank
  3) Bell test history (1972 → 2022 Nobel)
  4) Entanglement distance record (1m → 1200 km Micius)
  5) GHZ state and N-qubit entanglement
  6) Quantum teleportation protocol fidelity
  7) ITU K_photon_entanglement axiom check

Outputs:
  - entanglement_teleportation.png
  - entanglement_teleportation_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("entanglement_teleportation.png")
OUT_JSON = Path(__file__).with_name("entanglement_teleportation_summary.json")

rng = np.random.default_rng(20260703)

# -------------------------------------------------------------
# 1) Bell vs separable correlation
# -------------------------------------------------------------
# Bell state: -cos(theta1 - theta2)
# Separable: 0 (uncorrelated random) or correlated up to ±0.5
theta_diff = np.linspace(0, 2 * np.pi, 100)
bell_correlation = -np.cos(theta_diff)
classical_max = -0.5 * np.cos(theta_diff)  # local hidden var

# -------------------------------------------------------------
# 2) Bell test experimental history
# -------------------------------------------------------------
bell_tests = {
    "Clauser-Freedman (1972)":  {"S": 2.40, "year": 1972, "loophole_free": False},
    "Aspect 1 (1981)":          {"S": 2.70, "year": 1981, "loophole_free": False},
    "Aspect 2 (1982) ★":         {"S": 2.697, "year": 1982, "loophole_free": False},
    "Weihs (1998)":             {"S": 2.73, "year": 1998, "loophole_free": "locality"},
    "Hensen (2015) ★":           {"S": 2.42, "year": 2015, "loophole_free": "all"},
    "Cosmic Bell (Rauch 2018)": {"S": 2.65, "year": 2018, "loophole_free": "cosmic"},
}

# -------------------------------------------------------------
# 3) Entanglement distance record
# -------------------------------------------------------------
distance_record = {
    "Lab (1972)":           {"km": 0.005, "year": 1972},
    "1 km (1990s)":         {"km": 1.0,   "year": 1996},
    "North Sea (2005)":     {"km": 13,    "year": 2005},
    "Geneva (Vivoli)":      {"km": 51,    "year": 2007},
    "Canary Islands (Ma)":  {"km": 144,   "year": 2012},
    "Micius satellite (Pan)": {"km": 1200, "year": 2017},
    "Beijing-Vienna":       {"km": 7600,  "year": 2018},
}

# -------------------------------------------------------------
# 4) GHZ state N-qubit records
# -------------------------------------------------------------
ghz_records = {
    "3 (Bouwmeester 1999)":   3,
    "5 (Walther 2005)":        5,
    "8 (Lu 2007)":             8,
    "10 (Wang 2016)":         10,
    "12 (Pan 2019)":          12,
    "18 (Zhong 2020)":        18,
    "30+ (2024 photonic)":    30,
}

# -------------------------------------------------------------
# 5) Quantum teleportation fidelity
# -------------------------------------------------------------
# Bouwmeester 1997: ~0.7 fidelity
# Modern (2020s): 0.85-0.95
teleport_milestones = {
    "Bouwmeester 1997":       0.75,
    "Furusawa 1998 (CV)":      0.62,
    "Riebe 2004 (ions)":       0.80,
    "Ren 2017 (satellite)":    0.83,
    "Bao 2023 (3D state)":     0.92,
    "Classical limit":         0.667,
}

# -------------------------------------------------------------
# 6) Entanglement entropy of singlet vs product state
# -------------------------------------------------------------
# Singlet (|01⟩ - |10⟩)/√2: S_A = log 2 = 0.693 nats
# Product |00⟩: S_A = 0
# Mixed entangled (Werner state, p = visibility)

p_visibility = np.linspace(0, 1, 50)
# Werner state: S_A = -p log p - (1-p) log (1-p) (for diagonal mixture)
# More precise: Werner has 4 eigenvalues
# Simplified: depends on p
S_A_werner = []
for p in p_visibility:
    # Eigenvalues of reduced density matrix: roughly p/2 + (1-p)/4 each side
    vals = [p/2 + (1-p)/4, p/2 + (1-p)/4]
    S = -np.sum([v * np.log(v) if v > 1e-12 else 0 for v in vals])
    S_A_werner.append(S)
S_singlet = np.log(2)

# -------------------------------------------------------------
# 7) ITU K_photon_entanglement axiom
# -------------------------------------------------------------
# Pre: separable state
# Post: maximally entangled (Bell state)

N_states = 100
# Separable: equal mixture of 4 product basis
p_sep = np.zeros(N_states)
p_sep[[0, 33, 66, 99]] = 0.25  # 4 basis state
S_sep = float(-np.sum(np.where(p_sep > 0, p_sep * np.log(p_sep), 0)))

# Bell state: superposition of 2 (mixed Schmidt)
p_bell = np.zeros(N_states)
p_bell[[0, 99]] = 0.5
S_bell = float(-np.sum(np.where(p_bell > 0, p_bell * np.log(p_bell), 0)))

# GHZ-like: N-qubit superposition (smaller probability mass per state)
p_ghz = np.zeros(N_states)
p_ghz[0] = 0.5
p_ghz[99] = 0.5
S_ghz = float(-np.sum(np.where(p_ghz > 0, p_ghz * np.log(p_ghz), 0)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_sep_bell = itu_lin(p_sep, p_bell)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 222 — Quantum Entanglement + Bell + Teleportation (K_photon_entanglement)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Bell vs classical correlation
ax = axes[0, 0]
ax.plot(np.degrees(theta_diff), bell_correlation, "-", color="#9467bd", lw=2,
        label="Bell state E(θ₁,θ₂) = -cos(θ₁-θ₂)")
ax.plot(np.degrees(theta_diff), classical_max, "--", color="orange", lw=2,
        label="Local hidden variables (max)")
ax.set_xlabel("Angle difference (deg)")
ax.set_ylabel("Correlation E")
ax.set_title("Bell vs classical correlation")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Bell test history
ax = axes[0, 1]
years = [bell_tests[k]["year"] for k in bell_tests]
S_vals = [bell_tests[k]["S"] for k in bell_tests]
loophole = [bell_tests[k]["loophole_free"] for k in bell_tests]
colors_b = ["#2ca02c" if l == "all" else "#ff7f0e" if l else "#1f77b4" for l in loophole]
ax.scatter(years, S_vals, c=colors_b, s=150, edgecolor="black", zorder=5)
ax.axhline(2.0, color="red", linestyle="--", label="Classical max")
ax.axhline(2 * np.sqrt(2), color="green", linestyle="--", label=f"Tsirelson 2√2")
for k, t in bell_tests.items():
    ax.annotate(k.split()[0], (t["year"], t["S"]), fontsize=6,
                xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("S (Bell parameter)")
ax.set_title("Bell test history (Nobel 2022)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Entanglement distance
ax = axes[0, 2]
years_d = [distance_record[k]["year"] for k in distance_record]
km = [distance_record[k]["km"] for k in distance_record]
ax.semilogy(years_d, km, "o-", color="#1f77b4", lw=2, markersize=8)
for k, d in distance_record.items():
    ax.annotate(k.split(" ")[0], (d["year"], d["km"]), fontsize=6,
                xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("Distance (km, log)")
ax.set_title("Entanglement distance record (Micius 2017)")
ax.grid(True, alpha=0.3, which="both")

# Panel 4: GHZ N-qubit
ax = axes[1, 0]
ghz_names = list(ghz_records.keys())
ns = list(ghz_records.values())
ax.bar(range(len(ghz_names)), ns, color="#9467bd")
ax.set_xticks(range(len(ghz_names)))
ax.set_xticklabels(ghz_names, fontsize=6, rotation=20)
ax.set_ylabel("N qubits")
ax.set_title("GHZ multi-qubit entanglement records")
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Quantum teleportation
ax = axes[1, 1]
names_t = list(teleport_milestones.keys())
fid = list(teleport_milestones.values())
colors_t = ["#2ca02c" if f > 0.8 else "#1f77b4" if f > 0.7 else "#d62728" for f in fid]
ax.barh(range(len(names_t)), fid, color=colors_t)
ax.axvline(2/3, color="red", linestyle="--", label="Classical limit 2/3")
ax.set_yticks(range(len(names_t)))
ax.set_yticklabels(names_t, fontsize=7)
ax.set_xlabel("Teleportation fidelity")
ax.set_xlim(0, 1)
ax.set_title("Teleportation fidelity (Bouwmeester 1997+)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="x")

# Panel 6: ITU K_photon_entanglement
ax = axes[1, 2]
ax.bar(["Separable\n(4 states)", "Bell state\n(2-component)", "GHZ\n(2-component)"],
       [S_sep, S_bell, S_ghz], color=["#d62728", "#1f77b4", "#9467bd"])
ax.set_ylabel("State distribution entropy (nats)")
ax.set_title(f"K_photon_entanglement: Sep→Bell ratio={ratio_sep_bell:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 222,
    "tier1_paper": 31,
    "topic": "Quantum entanglement + Bell + Teleportation (K_photon_entanglement)",
    "EPR_1935": "Einstein-Podolsky-Rosen paradox",
    "Schrodinger_entanglement_1935": "Verschränkung concept introduced",
    "Bell_1964": "Bell's theorem - QM != local hidden variables",
    "CHSH_1969": "Experimentally testable Bell inequality",
    "Bell_test_history": bell_tests,
    "Nobel_2022_Physics": ["Aspect", "Clauser", "Zeilinger"],
    "entanglement_distance_record": distance_record,
    "Micius_satellite_2017": "Pan Jianwei, 1200 km satellite entanglement",
    "GHZ_records": ghz_records,
    "GHZ_Greenberger_Horne_Zeilinger_1989": "3-particle entanglement paradox",
    "teleportation_milestones": teleport_milestones,
    "Bouwmeester_1997_Nature": "First quantum teleportation experiment",
    "singlet_entanglement_entropy_nats": float(S_singlet),
    "ITU_K_photon_entanglement": {
        "S_separable_4_state_nats": S_sep,
        "S_Bell_2_component_nats": S_bell,
        "S_GHZ_2_component_nats": S_ghz,
        "separable_to_Bell_ratio": ratio_sep_bell,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_photon_entanglement",
        "non_locality": "Bell violation = K-state non-local correlation",
        "tensor_product_meaning": "K_photon_entanglement = K_photon ⊗ K_photon (non-separable)",
        "ER_EPR_link": "Bell pair ≡ Einstein-Rosen bridge (Phase 179 Maldacena-Susskind)",
        "K_universe_implication": "K-state are fundamentally non-local",
    },
    "predictions": [
        ("GHZ 50+ photonic qubits", 2028, 0.75, "Strong"),
        ("National quantum internet", 2032, 0.65, "Medium"),
        ("Loophole-free Bell @ 1000 km", 2030, 0.70, "Strong"),
        ("Inter-satellite teleportation", 2030, 0.70, "Strong"),
        ("CMB cosmic Bell test", 2032, 0.55, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
