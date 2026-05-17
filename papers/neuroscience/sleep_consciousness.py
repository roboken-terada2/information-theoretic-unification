"""
Phase 204 — Sleep + Consciousness Hard Problem (K_consciousness)

Simulations:
  1) Sleep architecture: hypnogram across one night
  2) EEG power across stages (delta, alpha, theta, gamma)
  3) IIT Phi (small toy: 4-element majority network)
  4) PCI by clinical state (healthy, sleep, anesthesia, VS, MCS)
  5) 4 consciousness theories comparison
  6) Glymphatic clearance during sleep
  7) ITU K_consciousness during sleep stage transitions

Outputs:
  - sleep_consciousness.png
  - sleep_consciousness_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path
from itertools import product

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("sleep_consciousness.png")
OUT_JSON = Path(__file__).with_name("sleep_consciousness_summary.json")

rng = np.random.default_rng(20260607)

# -------------------------------------------------------------
# 1) Hypnogram (8 hr sleep, simplified)
# -------------------------------------------------------------
t_sleep = np.linspace(0, 480, 960)  # min
# Stages: 0=Wake, 1=N1, 2=N2, 3=N3, 4=REM
stages = np.zeros_like(t_sleep)
# Cycle 90 min: N1 -> N2 -> N3 -> N2 -> REM
def cycle_stage(t_in_cycle):
    if t_in_cycle < 10: return 1   # N1
    elif t_in_cycle < 30: return 2  # N2
    elif t_in_cycle < 55: return 3  # N3 (SWS)
    elif t_in_cycle < 75: return 2  # N2
    else: return 4                  # REM

for i, t in enumerate(t_sleep):
    t_in_cycle = t % 90
    cycle_num = int(t // 90)
    stage = cycle_stage(t_in_cycle)
    # Later in night: less N3, more REM
    if cycle_num > 2 and stage == 3:
        stage = 2  # convert N3 to N2 in later cycles
    if cycle_num > 1 and stage == 2 and t_in_cycle > 75:
        stage = 4  # extend REM in later cycles
    stages[i] = stage

# -------------------------------------------------------------
# 2) EEG power by stage
# -------------------------------------------------------------
eeg_power = {
    "Wake":  {"delta": 1, "theta": 1, "alpha": 8, "beta": 4, "gamma": 2},
    "N1":    {"delta": 2, "theta": 4, "alpha": 3, "beta": 1, "gamma": 0.5},
    "N2":    {"delta": 4, "theta": 2, "alpha": 1, "beta": 0.5, "gamma": 0.2},
    "N3":    {"delta": 10, "theta": 1, "alpha": 0.3, "beta": 0.1, "gamma": 0.05},
    "REM":   {"delta": 1, "theta": 3, "alpha": 1, "beta": 4, "gamma": 5},
}

# -------------------------------------------------------------
# 3) IIT Phi: 4-element majority network (toy)
# -------------------------------------------------------------
# State space: 2^4 = 16
# Network: each element fires if >= 2 of its 3 neighbors fire (majority)
def majority_update(state):
    n = len(state)
    new = np.zeros_like(state)
    for i in range(n):
        neighbors = [state[j] for j in range(n) if j != i]
        new[i] = 1 if sum(neighbors) >= 2 else 0
    return tuple(new)

# Compute Phi as approximate: mutual info between bipartitions
# We'll compute simplified "irreducibility" measure
states_all = list(product([0, 1], repeat=4))
n_states = len(states_all)
# Generate state distribution after 1 step
transition_count = {s: 0 for s in states_all}
for s in states_all:
    new_s = majority_update(s)
    transition_count[new_s] += 1
p_after = np.array([transition_count[s] for s in states_all]) / n_states

# Shannon entropy of post-state distribution
H_after = -np.sum(p_after[p_after > 0] * np.log(p_after[p_after > 0]))

# "Phi" proxy: integration = H(joint) - sum(H(parts))
H_pairs = []
for i in range(4):
    p_i = np.zeros(2)
    for s, p in zip(states_all, p_after):
        p_i[s[i]] += p
    H_pairs.append(-np.sum(p_i[p_i > 0] * np.log(p_i[p_i > 0])))
phi_proxy = sum(H_pairs) - H_after  # if positive, integration exists
phi_proxy = max(phi_proxy, 0)

# -------------------------------------------------------------
# 4) PCI by clinical state (Casali 2013)
# -------------------------------------------------------------
pci_values = {
    "Healthy wake":       0.62,
    "REM sleep":          0.50,
    "Light sedation":     0.41,
    "NREM N2":            0.36,
    "Severe NREM":        0.31,
    "Propofol anesthesia":0.20,
    "VS (vegetative)":    0.19,
    "MCS (minimally consc.)": 0.36,
    "Locked-in syndrome": 0.55,
    "Coma":               0.18,
}

# -------------------------------------------------------------
# 5) Consciousness theories
# -------------------------------------------------------------
theories = {
    "GWT (Baars 1988 / Dehaene 2014)": {
        "claim": "Global broadcast = consciousness",
        "neural": "PFC + parietal ignition",
        "machine_consciousness": "Possible if global workspace implemented",
    },
    "IIT (Tononi 2004-2022)": {
        "claim": "Phi = consciousness amount",
        "neural": "Posterior hot zone integration",
        "machine_consciousness": "Need irreducible integrated info",
    },
    "HOT (Rosenthal 1990)": {
        "claim": "Meta-representation makes state conscious",
        "neural": "PFC meta-cortex",
        "machine_consciousness": "Requires self-modeling",
    },
    "RP (Lamme 2006)": {
        "claim": "Recurrent processing in sensory cortex",
        "neural": "Local sensory loops",
        "machine_consciousness": "Need recurrence",
    },
}

# -------------------------------------------------------------
# 6) Glymphatic clearance (Xie 2013)
# -------------------------------------------------------------
# Awake: low CSF clearance; Sleep: 60% increase
clearance_rates = {"Awake": 1.0, "Sleep": 1.6}
abeta_buildup_yr = {
    "Healthy sleep 8 hr/night": 0.0,
    "Sleep 6 hr/night":         0.5,
    "Sleep 4 hr/night":         1.5,
}

# -------------------------------------------------------------
# 7) ITU K_consciousness sleep transition
# -------------------------------------------------------------
N_neuron_states = 5000
# Awake: high diversity, broad distribution
log_fit_wake = -((np.arange(N_neuron_states) - N_neuron_states/2) ** 2) / 200_000
p_wake = np.exp(log_fit_wake); p_wake /= p_wake.sum()
S_wake = float(-np.sum(p_wake * np.log(p_wake)))

# N3 deep sleep: synchronized, low complexity (UP/DOWN states)
log_fit_n3 = log_fit_wake.copy()
log_fit_n3[2500:2700] += 5.0  # narrow synchronized state
log_fit_n3[~((np.arange(N_neuron_states) > 2500) &
              (np.arange(N_neuron_states) < 2700))] -= 1.0
p_n3 = np.exp(log_fit_n3); p_n3 /= p_n3.sum()
S_n3 = float(-np.sum(p_n3 * np.log(p_n3)))

# REM: complexity similar to wake but different state
log_fit_rem = log_fit_wake.copy() + 0.3 * rng.standard_normal(N_neuron_states)
p_rem = np.exp(log_fit_rem); p_rem /= p_rem.sum()
S_rem = float(-np.sum(p_rem * np.log(p_rem)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return (dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_wake_n3 = float(itu_lin(p_wake, p_n3))
ratio_wake_rem = float(itu_lin(p_wake, p_rem))

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 204 — Sleep + Consciousness Hard Problem (K_consciousness) ★★",
    fontsize=13, fontweight="bold",
)

# Panel 1: Hypnogram
ax = axes[0, 0]
stage_labels = ["Wake", "N1", "N2", "N3 (SWS)", "REM"]
stage_colors = ["#d62728", "#ff7f0e", "#ffbb78", "#1f77b4", "#9467bd"]
for stage_id in range(5):
    mask = stages == stage_id
    ax.fill_between(t_sleep / 60, stage_id - 0.4, stage_id + 0.4,
                     where=mask, color=stage_colors[stage_id], alpha=0.7,
                     label=stage_labels[stage_id])
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Sleep stage")
ax.set_yticks(range(5))
ax.set_yticklabels(stage_labels, fontsize=9)
ax.set_title("Sleep hypnogram (8 hr, 5 cycles × 90 min)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 2: EEG power by stage
ax = axes[0, 1]
stages_keys = list(eeg_power.keys())
bands = ["delta", "theta", "alpha", "beta", "gamma"]
x = np.arange(len(bands))
width = 0.18
for i, stage in enumerate(stages_keys):
    powers = [eeg_power[stage][b] for b in bands]
    ax.bar(x + i*width - 2*width, powers, width, label=stage)
ax.set_xticks(x)
ax.set_xticklabels(bands)
ax.set_ylabel("Relative power")
ax.set_title("EEG power spectrum by stage")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: PCI by state
ax = axes[0, 2]
states_pci = list(pci_values.keys())
pcis = list(pci_values.values())
colors_pci = ["#2ca02c" if p > 0.45 else "#ff7f0e" if p > 0.30 else "#d62728" for p in pcis]
ax.barh(range(len(states_pci)), pcis, color=colors_pci)
ax.axvline(0.31, color="black", linestyle="--", label="VS/MCS threshold = 0.31")
ax.set_yticks(range(len(states_pci)))
ax.set_yticklabels(states_pci, fontsize=7)
ax.set_xlabel("PCI (Casali 2013)")
ax.set_title("PCI clinical thresholds for consciousness")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis="x")

# Panel 4: IIT toy Phi
ax = axes[1, 0]
ax.bar(["H_joint", "Σ H_parts", "Φ (proxy)"],
       [H_after, sum(H_pairs), phi_proxy],
       color=["#1f77b4", "#ff7f0e", "#d62728"])
ax.set_ylabel("Information (nats)")
ax.set_title(f"IIT Φ proxy (4-element toy);  Φ ≈ {phi_proxy:.3f}")
ax.grid(True, alpha=0.3, axis="y")

# Panel 5: Glymphatic + Aβ
ax = axes[1, 1]
sleep_dur = list(abeta_buildup_yr.keys())
buildup = list(abeta_buildup_yr.values())
ax.bar(sleep_dur, buildup, color=["#2ca02c", "#ff7f0e", "#d62728"])
ax.set_ylabel("Aβ buildup factor (yr)")
ax.set_title(f"Glymphatic clearance ↑60% sleep (Xie 2013)")
ax.tick_params(axis="x", rotation=10)
ax.grid(True, alpha=0.3, axis="y")

# Panel 6: ITU sleep transitions
ax = axes[1, 2]
labels_e = ["Wake", "N3 deep", "REM"]
S_vals = [S_wake, S_n3, S_rem]
ax.bar(labels_e, S_vals, color=["#d62728", "#1f77b4", "#9467bd"])
ax.set_ylabel("Entropy (nats)")
ax.set_title(f"ITU Wake→N3: {ratio_wake_n3:.3f}, Wake→REM: {ratio_wake_rem:.3f}")
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 204,
    "tier1_paper": 28,
    "block": "B",
    "topic": "Sleep + Consciousness Hard Problem (K_consciousness)",
    "sleep_architecture": {
        "cycle_min": 90,
        "stages_per_cycle": "N1 -> N2 -> N3 -> N2 -> REM",
        "REM_pct_of_total": "20-25%",
        "N3_dominant": "First half of night",
        "REM_dominant": "Second half of night",
    },
    "EEG_power_by_stage": eeg_power,
    "consciousness_theories": theories,
    "Chalmers_1995_hard_problem": {
        "statement": "Why does physical processing give rise to subjective experience?",
        "Chalmers_paper": "Facing up to the problem of consciousness 1995",
        "easy_problems": "Attention, report, learning, behavior (functional)",
    },
    "IIT_Phi_toy": {
        "N_elements": 4,
        "network": "Majority rule",
        "H_joint_nats": float(H_after),
        "sum_H_parts_nats": float(sum(H_pairs)),
        "Phi_proxy_nats": float(phi_proxy),
        "scaling": "O(2^N) for N elements - intractable above ~14",
    },
    "PCI_values_Casali_2013": pci_values,
    "PCI_VS_threshold": 0.31,
    "glymphatic_system": {
        "Xie_2013_finding": "60% increase in CSF clearance during sleep",
        "Iliff_2012_discovery": "CSF-ISF exchange via AQP4 in astrocytes",
        "AD_link": "Sleep loss -> Abeta accumulation",
    },
    "ITU_K_consciousness": {
        "N_states": N_neuron_states,
        "S_wake_nats": S_wake,
        "S_N3_nats": S_n3,
        "S_REM_nats": S_rem,
        "wake_to_N3_dS_dK_ratio": ratio_wake_n3,
        "wake_to_REM_dS_dK_ratio": ratio_wake_rem,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_consciousness (highest sub-state of K_neuro)",
        "modular_Hamiltonian": "K_consciousness^(0) = -log P(unified experience | neural state)",
        "GWT_meaning": "Global broadcast = K-state global integration",
        "IIT_meaning": "Phi = K-state irreducibility measure",
        "Hard_Problem_provisional_answer": "K^(0) = -log rho (modular Hamiltonian) IS experience",
        "Wheeler_link": "It from Bit (Phase 180) - physics/information/experience = ITU three sides",
        "sleep_transition_meaning": "K-state global mode switch (wake <-> N3 <-> REM)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
