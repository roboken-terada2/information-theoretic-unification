"""
Phase 199 — Neuron + Synapse + Connectome (K_neuro introduction)

Simulations:
  1) Hodgkin-Huxley action potential
  2) Brain cell count census (Herculano-Houzel 2009)
  3) Neurotransmitter classification
  4) EEG frequency bands
  5) Small-world network: Watts-Strogatz vs random
  6) Cortical connectome 180 areas (HCP-like) summary statistics
  7) ITU K_neuro axiom check

Outputs:
  - neuron_synapse_connectome.png
  - neuron_synapse_connectome_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

OUT_PNG = Path(__file__).with_name("neuron_synapse_connectome.png")
OUT_JSON = Path(__file__).with_name("neuron_synapse_connectome_summary.json")

rng = np.random.default_rng(20260602)

# -------------------------------------------------------------
# 1) Hodgkin-Huxley action potential
# -------------------------------------------------------------
# Parameters (Hodgkin-Huxley 1952, squid axon)
C_m = 1.0      # uF/cm^2
g_Na = 120.0   # mS/cm^2
g_K = 36.0
g_L = 0.3
E_Na = 50.0    # mV
E_K = -77.0
E_L = -54.387
V_rest = -65.0

def alpha_m(V): return 0.1 * (V + 40) / (1 - np.exp(-(V + 40)/10))
def beta_m(V):  return 4.0 * np.exp(-(V + 65)/18)
def alpha_h(V): return 0.07 * np.exp(-(V + 65)/20)
def beta_h(V):  return 1.0 / (1 + np.exp(-(V + 35)/10))
def alpha_n(V): return 0.01 * (V + 55) / (1 - np.exp(-(V + 55)/10))
def beta_n(V):  return 0.125 * np.exp(-(V + 65)/80)

def HH(y, t):
    V, m, h, n = y
    # Stimulus: 10 uA/cm^2 between 5-15 ms, then 30-40 ms
    I_ext = 0.0
    if 5 <= t <= 6: I_ext = 10
    if 30 <= t <= 31: I_ext = 10
    if 55 <= t <= 56: I_ext = 10
    I_Na = g_Na * m**3 * h * (V - E_Na)
    I_K = g_K * n**4 * (V - E_K)
    I_L = g_L * (V - E_L)
    dV = (I_ext - I_Na - I_K - I_L) / C_m
    dm = alpha_m(V) * (1 - m) - beta_m(V) * m
    dh = alpha_h(V) * (1 - h) - beta_h(V) * h
    dn = alpha_n(V) * (1 - n) - beta_n(V) * n
    return [dV, dm, dh, dn]

t_HH = np.linspace(0, 80, 8000)
y0_HH = [V_rest, alpha_m(V_rest)/(alpha_m(V_rest)+beta_m(V_rest)),
         alpha_h(V_rest)/(alpha_h(V_rest)+beta_h(V_rest)),
         alpha_n(V_rest)/(alpha_n(V_rest)+beta_n(V_rest))]
sol_HH = odeint(HH, y0_HH, t_HH)
V_trace = sol_HH[:, 0]
peak_voltage = float(V_trace.max())
spike_count = int(np.sum((V_trace[1:] > 0) & (V_trace[:-1] <= 0)))

# -------------------------------------------------------------
# 2) Brain cell census (Herculano-Houzel 2009)
# -------------------------------------------------------------
cell_census = {
    "Cerebral cortex neurons":       16e9,
    "Cerebellar neurons":            69e9,  # MORE than cerebral!
    "Other regions neurons":         1e9,
    "Total neurons":                 86e9,
    "Glia cells":                    85e9,
    "Total brain cells":             171e9,
    "Synapses":                      1.5e14,
}

# -------------------------------------------------------------
# 3) Neurotransmitters classification
# -------------------------------------------------------------
neurotransmitters = {
    "Glutamate":   {"type": "Excitatory",  "pct_synapses": 80},
    "GABA":        {"type": "Inhibitory",  "pct_synapses": 15},
    "Acetylcholine":{"type": "Excitatory", "pct_synapses": 1},
    "Dopamine":    {"type": "Modulatory",  "pct_synapses": 0.5},
    "Serotonin":   {"type": "Modulatory",  "pct_synapses": 0.3},
    "Norepinephrine":{"type": "Modulatory","pct_synapses": 0.2},
    "Histamine":   {"type": "Modulatory",  "pct_synapses": 0.1},
    "Endorphin":   {"type": "Modulatory",  "pct_synapses": 0.1},
}

# -------------------------------------------------------------
# 4) EEG bands
# -------------------------------------------------------------
eeg_bands = {
    "δ delta (0.5-4 Hz)":   {"state": "Deep sleep"},
    "θ theta (4-8 Hz)":     {"state": "Memory, meditation"},
    "α alpha (8-13 Hz)":    {"state": "Resting wakefulness"},
    "β beta (13-30 Hz)":    {"state": "Attention, cognition"},
    "γ gamma (30-100 Hz)":  {"state": "Consciousness binding (Crick-Koch 1990)"},
}

# Simulate composite EEG
t_eeg = np.linspace(0, 5, 2500)
eeg_signal = (np.sin(2*np.pi*2*t_eeg) +
              0.7*np.sin(2*np.pi*6*t_eeg) +
              1.2*np.sin(2*np.pi*10*t_eeg) +
              0.5*np.sin(2*np.pi*20*t_eeg) +
              0.4*np.sin(2*np.pi*40*t_eeg)) + 0.3*rng.standard_normal(len(t_eeg))

# -------------------------------------------------------------
# 5) Small-world network (Watts-Strogatz)
# -------------------------------------------------------------
N_nodes = 100
k_nn = 6   # average degree
# Ring lattice with rewiring probability p
def ws_clustering_path(p, N=N_nodes, k=k_nn, n_samples=10):
    """Approximate clustering coefficient and path length."""
    C_vals, L_vals = [], []
    for _ in range(n_samples):
        # Initialize ring lattice
        A = np.zeros((N, N))
        for i in range(N):
            for j in range(1, k//2 + 1):
                A[i, (i+j) % N] = 1
                A[i, (i-j) % N] = 1
        # Rewire
        for i in range(N):
            for j in range(1, k//2 + 1):
                if rng.random() < p:
                    A[i, (i+j) % N] = 0
                    new_j = rng.integers(N)
                    while new_j == i or A[i, new_j]:
                        new_j = rng.integers(N)
                    A[i, new_j] = 1
                    A[new_j, i] = 1
        # Compute average clustering
        C_local = []
        for i in range(N):
            neighbors = np.where(A[i] > 0)[0]
            kk = len(neighbors)
            if kk < 2: continue
            edges = 0
            for n1 in neighbors:
                for n2 in neighbors:
                    if n1 != n2 and A[n1, n2] > 0: edges += 1
            C_local.append(edges / (kk * (kk - 1)))
        C_vals.append(np.mean(C_local))
        # Approximate path length: BFS from random nodes
        L_local = []
        for _ in range(5):
            src = rng.integers(N)
            visited = {src: 0}
            queue = [src]
            while queue:
                u = queue.pop(0)
                for v in np.where(A[u] > 0)[0]:
                    if v not in visited:
                        visited[v] = visited[u] + 1
                        queue.append(v)
            L_local.append(np.mean(list(visited.values())))
        L_vals.append(np.mean(L_local))
    return np.mean(C_vals), np.mean(L_vals)

p_grid = [0, 0.01, 0.1, 0.5, 1.0]
C_results = []
L_results = []
for p in p_grid:
    C, L = ws_clustering_path(p, n_samples=3)
    C_results.append(C)
    L_results.append(L)

# -------------------------------------------------------------
# 6) Connectome 180 areas summary
# -------------------------------------------------------------
hcp_summary = {
    "Total cortical areas (180/hemi)":     360,
    "Old (Brodmann 1909)":                  52,
    "Functional connections per area":      "20-50",
    "Rich-club hubs":                       ["Precuneus", "Insula", "Anterior cingulate",
                                             "Dorsolateral PFC"],
    "Reference":                            "Glasser 2016 Nature",
}

# -------------------------------------------------------------
# 7) ITU K_neuro axiom check
# -------------------------------------------------------------
N_states = 2000
# Resting state: broad distribution
log_fit_rest = -((np.arange(N_states) - N_states/2) ** 2) / 100_000
p_rest = np.exp(log_fit_rest); p_rest /= p_rest.sum()
S_rest = float(-np.sum(p_rest * np.log(p_rest)))

# Active state (e.g., during task): some neural assemblies fire strongly
active_mask = (np.arange(N_states) > 1500) & (np.arange(N_states) < 1700)
log_fit_active = log_fit_rest.copy()
log_fit_active[active_mask] += 3.0
p_active = np.exp(log_fit_active); p_active /= p_active.sum()
S_active = float(-np.sum(p_active * np.log(p_active)))

log_p_rest = np.log(np.clip(p_rest, 1e-30, None))
dp = p_active - p_rest
dS_lin = -np.sum(dp * (1.0 + log_p_rest))
dK_lin = -np.sum(dp * log_p_rest)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 199 — Neuron + Synapse + Connectome (K_neuro)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Hodgkin-Huxley action potential
ax = axes[0, 0]
ax.plot(t_HH, V_trace, "-", color="#1f77b4", lw=1.5)
ax.axhline(0, color="black", linestyle="--", alpha=0.3)
ax.axhline(V_rest, color="gray", linestyle=":", alpha=0.5, label="V_rest")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Membrane potential (mV)")
ax.set_title(f"Hodgkin-Huxley (1952, Nobel 1963); peak={peak_voltage:.1f} mV, {spike_count} spikes")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Brain cell census
ax = axes[0, 1]
items = list(cell_census.keys())
vals = list(cell_census.values())
colors_c = ["#1f77b4" if "neuron" in s.lower() else "#ff7f0e" if "glia" in s.lower() else "#2ca02c"
            for s in items]
ax.barh(range(len(items)), vals, color=colors_c)
ax.set_xscale("log")
ax.set_yticks(range(len(items)))
ax.set_yticklabels(items, fontsize=7)
ax.set_xlabel("Cell count (log)")
ax.set_title("Brain census (Herculano-Houzel 2009)")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 3: Neurotransmitters
ax = axes[0, 2]
nt_names = list(neurotransmitters.keys())
nt_pcts = [neurotransmitters[n]["pct_synapses"] for n in nt_names]
nt_colors = ["#d62728" if neurotransmitters[n]["type"] == "Excitatory" else
             "#1f77b4" if neurotransmitters[n]["type"] == "Inhibitory" else "#2ca02c"
             for n in nt_names]
ax.barh(range(len(nt_names)), nt_pcts, color=nt_colors)
ax.set_xscale("log")
ax.set_yticks(range(len(nt_names)))
ax.set_yticklabels(nt_names, fontsize=8)
ax.set_xlabel("Synapse fraction (%, log)")
ax.set_title("Neurotransmitters: Glu 80%, GABA 15%")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: EEG composite signal
ax = axes[1, 0]
ax.plot(t_eeg, eeg_signal, "-", color="#9467bd", lw=0.8)
ax.set_xlabel("Time (sec)")
ax.set_ylabel("Amplitude")
ax.set_title("Composite EEG (δ θ α β γ bands)")
ax.grid(True, alpha=0.3)

# Panel 5: Small-world (Watts-Strogatz)
ax = axes[1, 1]
ax.plot(p_grid, np.array(C_results)/C_results[0], "o-", color="#1f77b4",
        lw=2, label="C(p)/C(0)")
ax.plot(p_grid, np.array(L_results)/L_results[0], "s-", color="#d62728",
        lw=2, label="L(p)/L(0)")
ax.axvspan(0.001, 0.1, alpha=0.2, color="green", label="Small-world regime")
ax.set_xscale("log")
ax.set_xlabel("Rewiring probability p")
ax.set_ylabel("Normalized")
ax.set_title("Watts-Strogatz small-world (1998)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: K_neuro ITU axiom
ax = axes[1, 2]
ax.plot(np.arange(N_states), p_rest, "-", color="#1f77b4", lw=1.5,
        label=f"Resting  S={S_rest:.3f}")
ax.plot(np.arange(N_states), p_active, "-", color="#d62728", lw=1.5,
        label=f"Active   S={S_active:.3f}")
ax.set_xlabel("Neural state index")
ax.set_ylabel("Probability")
ax.set_title(f"K_neuro: ITU δS/δ⟨K⟩ = {itu_ratio:.6f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 199,
    "tier1_paper": 28,
    "block": "B",
    "paper_in_block": "3/?",
    "topic": "Neuron + synapse + connectome (K_neuro introduction)",
    "Hodgkin_Huxley_1952_Nobel_1963": {
        "C_m_uF_per_cm2": C_m,
        "g_Na": g_Na, "g_K": g_K, "g_L": g_L,
        "E_Na_mV": E_Na, "E_K_mV": E_K, "E_L_mV": E_L,
        "peak_voltage_mV": peak_voltage,
        "spike_count_in_80ms": spike_count,
    },
    "brain_cell_census_Herculano_Houzel_2009": {k: float(v) for k, v in cell_census.items()},
    "neurotransmitters_pct_synapses": neurotransmitters,
    "EEG_bands": eeg_bands,
    "small_world_Watts_Strogatz_1998": {
        "p_grid": p_grid,
        "C_normalized": [float(c / C_results[0]) for c in C_results],
        "L_normalized": [float(l / L_results[0]) for l in L_results],
        "small_world_regime": "p ~ 0.001 - 0.1",
    },
    "HCP_connectome": hcp_summary,
    "ITU_K_neuro": {
        "N_states": int(N_states),
        "S_resting_nats": S_rest,
        "S_active_nats": S_active,
        "delta_S": S_active - S_rest,
        "delta_S_first_order": float(dS_lin),
        "delta_K_first_order": float(dK_lin),
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_neuro",
        "sub_states": [
            "K_neuron (Hodgkin-Huxley dynamics)",
            "K_synapse (LTP, LTD, neurotransmitters)",
            "K_network (connectome, small-world)",
            "K_oscillation (EEG bands)",
            "K_perception (Hubel-Wiesel)",
            "K_memory (hippocampus, place cells)",
            "K_executive (prefrontal)",
            "K_consciousness (Hard Problem)",
        ],
        "axiom": "delta S(rho_neural) = delta Tr[K_neuro^(0) rho_neural]",
        "learning_meaning": "Synaptic plasticity = ITU descent flow",
        "consciousness_hypothesis": "K_neuro global integration state",
    },
    "key_facts": {
        "neurons_total": "86 billion (cortex 16B, cerebellum 69B!)",
        "synapses": "10^14 - 10^15",
        "axon_total_length_km": 170000,
        "brain_power_W": 20,
        "HCP_cortical_areas_per_hemi": 180,
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
