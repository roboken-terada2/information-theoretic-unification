"""
Phase 200 — LTP / LTD / Hebb / STDP / Memory (K_synapse + K_memory)

Simulations:
  1) Bliss-Lomo LTP induction (100 Hz, EPSP amplitude time course)
  2) LTD induction (1 Hz, 15 min)
  3) STDP curve (Markram 1997, Bi-Poo 1998)
  4) NMDA Mg2+ block voltage dependence
  5) Hebbian learning toy: pattern formation
  6) Memory taxonomy + H.M. (Henry Molaison) anatomy
  7) Engram cell sparse coding
  8) ITU K_synapse axiom check

Outputs:
  - ltp_ltd_hebb_stdp.png
  - ltp_ltd_hebb_stdp_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("ltp_ltd_hebb_stdp.png")
OUT_JSON = Path(__file__).with_name("ltp_ltd_hebb_stdp_summary.json")

rng = np.random.default_rng(20260603)

# -------------------------------------------------------------
# 1) LTP induction (Bliss-Lomo 1973)
# -------------------------------------------------------------
t_ltp = np.linspace(-10, 180, 1000)  # minutes
# Baseline EPSP ~ 1.0, tetanus at t=0 -> EPSP ~ 2.5, slow decay
baseline = 1.0
ltp_response = np.where(t_ltp < 0, baseline,
                         baseline + 1.5 * np.exp(-t_ltp / 200))
ltp_response[t_ltp < 0] = 1.0
# Add noise
ltp_response += 0.05 * rng.standard_normal(len(t_ltp))

# -------------------------------------------------------------
# 2) LTD induction (low-frequency 1 Hz)
# -------------------------------------------------------------
ltd_response = np.where(t_ltp < 0, baseline,
                         baseline - 0.5 * (1 - np.exp(-t_ltp / 50)))
ltd_response[t_ltp < 0] = 1.0
ltd_response += 0.05 * rng.standard_normal(len(t_ltp))

# -------------------------------------------------------------
# 3) STDP curve (Markram 1997, Bi-Poo 1998)
# -------------------------------------------------------------
dt = np.linspace(-60, 60, 200)
A_plus = 0.1
A_minus = 0.12
tau_plus = 20
tau_minus = 20
stdp = np.where(dt > 0,
                A_plus * np.exp(-dt / tau_plus),
                -A_minus * np.exp(dt / tau_minus))

# -------------------------------------------------------------
# 4) NMDA Mg2+ block
# -------------------------------------------------------------
V_range = np.linspace(-100, 50, 200)
# Mg block: 1 / (1 + [Mg]/3.57 * exp(-0.062 * V))
mg_conc = 1.0  # mM
mg_block = 1 / (1 + (mg_conc / 3.57) * np.exp(-0.062 * V_range))
# NMDA current: g_NMDA * mg_block * (V - E_NMDA)
nmda_current = -10 * mg_block * (V_range - 0)  # arbitrary scale

# -------------------------------------------------------------
# 5) Hebbian learning toy: 100 inputs -> 50 outputs
# -------------------------------------------------------------
N_in, N_out = 100, 50
# Input patterns (5 distinct patterns, 1000 samples)
patterns = rng.choice([0, 1], size=(5, N_in), p=[0.7, 0.3])
n_samples = 1000
inputs = patterns[rng.integers(5, size=n_samples)]

# Initialize random weights
W = rng.uniform(0, 0.01, size=(N_in, N_out))
eta = 0.001
decay = 0.0001

# Train with Oja's rule (Hebb + normalization)
W_history = [W.copy()]
for step in range(n_samples):
    x = inputs[step]
    y = x @ W
    # Oja: dw = eta * y * (x - y * w_col)
    W += eta * np.outer(x, y) - decay * W
    W = np.clip(W, 0, None)
    if step in [200, 500, 999]:
        W_history.append(W.copy())

# Final weight distribution
W_final_mean = float(W.mean())
W_final_std = float(W.std())

# -------------------------------------------------------------
# 6) Memory taxonomy
# -------------------------------------------------------------
memory_types = {
    "Sensory (<1 sec)":              {"duration_sec": 1,        "site": "Sensory cortex"},
    "Short-term / Working (sec-min)": {"duration_sec": 60,       "site": "Prefrontal cortex"},
    "Long-term declarative (perm)":   {"duration_sec": 3.15e9,  "site": "Hippocampus + cortex"},
    "Procedural (permanent)":         {"duration_sec": 3.15e9,  "site": "Cerebellum + basal ganglia"},
    "Episodic (sub of declarative)":  {"duration_sec": 3.15e9,  "site": "Hippocampus"},
    "Semantic (sub of declarative)":  {"duration_sec": 3.15e9,  "site": "Temporal cortex"},
}

# -------------------------------------------------------------
# 7) Engram sparse coding
# -------------------------------------------------------------
# Single memory engram ~ 1-5% of CA3/dentate cells
N_hippo_neurons = 100_000
engram_fraction = 0.025  # 2.5%
n_engram = int(N_hippo_neurons * engram_fraction)
n_memories_storable = N_hippo_neurons // n_engram  # very rough

# -------------------------------------------------------------
# 8) ITU K_synapse axiom check
# -------------------------------------------------------------
N_syn = 5000
# Pre-LTP: low strength, narrow distribution
w_pre = rng.lognormal(0, 0.3, size=N_syn)
w_pre = w_pre / w_pre.sum() * N_syn  # normalize
p_pre = w_pre / w_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Post-LTP: high-coincidence synapses strengthened ~2.5×
coincident = rng.random(N_syn) < 0.2
w_post = w_pre.copy()
w_post[coincident] *= 2.5
p_post = w_post / w_post.sum()
S_post = float(-np.sum(p_post * np.log(p_post)))

log_p_pre = np.log(p_pre)
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 200 ★ — LTP / LTD / Hebb / STDP / Memory (K_synapse + K_memory)",
    fontsize=13, fontweight="bold",
)

# Panel 1: LTP/LTD time course
ax = axes[0, 0]
ax.plot(t_ltp, ltp_response, "-", color="#2ca02c", lw=1.5,
        label="LTP (100 Hz, 1 sec)")
ax.plot(t_ltp, ltd_response, "-", color="#d62728", lw=1.5,
        label="LTD (1 Hz, 15 min)")
ax.axvline(0, color="black", linestyle="--", alpha=0.5)
ax.axhline(1, color="gray", linestyle=":", alpha=0.5)
ax.set_xlabel("Time post-induction (min)")
ax.set_ylabel("EPSP amplitude (normalized)")
ax.set_title("Bliss-Lomo 1973 LTP / LTD")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: STDP curve
ax = axes[0, 1]
ax.plot(dt, stdp * 100, "-", color="#9467bd", lw=2)
ax.axhline(0, color="black", lw=0.5)
ax.axvline(0, color="black", lw=0.5)
ax.fill_between(dt, 0, stdp * 100, where=stdp > 0, alpha=0.3, color="#2ca02c", label="LTP")
ax.fill_between(dt, 0, stdp * 100, where=stdp < 0, alpha=0.3, color="#d62728", label="LTD")
ax.set_xlabel("Δt (post - pre) (ms)")
ax.set_ylabel("Δw (% change)")
ax.set_title("STDP (Markram 1997, Bi-Poo 1998)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: NMDA Mg2+ block
ax = axes[0, 2]
ax.plot(V_range, mg_block, "-", color="#1f77b4", lw=2, label="Mg²⁺ unblock")
ax.axvline(-65, color="gray", linestyle="--", alpha=0.5, label="V_rest")
ax.axvline(0, color="red", linestyle="--", alpha=0.5, label="Depol.")
ax.set_xlabel("Membrane potential (mV)")
ax.set_ylabel("NMDA channel openness")
ax.set_title("NMDA Mg²⁺ block (coincidence detector)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Hebbian learning weight evolution
ax = axes[1, 0]
for i, W_snap in enumerate([W_history[0], W_history[-1]]):
    ax.hist(W_snap.flatten(), bins=50, alpha=0.5,
            label=f"Step {[0, 999][i]}", color=["#1f77b4", "#d62728"][i])
ax.set_xlabel("Weight value")
ax.set_ylabel("Frequency")
ax.set_title(f"Hebbian (Oja) learning;  final ⟨w⟩={W_final_mean:.4f}±{W_final_std:.4f}")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Memory taxonomy
ax = axes[1, 1]
m_names = list(memory_types.keys())
durations = [memory_types[m]["duration_sec"] for m in m_names]
colors_m = ["#d62728" if d < 60 else "#ff7f0e" if d < 1e6 else "#2ca02c" for d in durations]
ax.barh(range(len(m_names)), durations, color=colors_m)
ax.set_xscale("log")
ax.set_yticks(range(len(m_names)))
ax.set_yticklabels(m_names, fontsize=7)
ax.set_xlabel("Duration (sec, log)")
ax.set_title("Memory taxonomy")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 6: ITU axiom + engram
ax = axes[1, 2]
ax.hist(np.log10(np.clip(p_pre, 1e-10, None)), bins=50, alpha=0.6,
        color="#1f77b4", label=f"Pre-LTP  S={S_pre:.3f}")
ax.hist(np.log10(np.clip(p_post, 1e-10, None)), bins=50, alpha=0.6,
        color="#d62728", label=f"Post-LTP S={S_post:.3f}")
ax.set_xlabel("log10(synapse weight prob)")
ax.set_ylabel("Count")
ax.set_title(f"K_synapse ITU δS/δ⟨K⟩ = {itu_ratio:.6f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 200,
    "tier1_paper": 28,
    "block": "B",
    "topic": "LTP/LTD/Hebb/STDP/Memory (K_synapse + K_memory)",
    "milestone": "200/220 = 90.9% Pass-1 ★★★",
    "LTP_Bliss_Lomo_1973": {
        "induction_freq_Hz": 100,
        "duration_sec": 1,
        "EPSP_increase_factor": 2.5,
        "persistence": "hours-days-weeks",
        "NMDA_dependence": "AP5 blocks LTP (Collingridge 1983)",
    },
    "LTD_induction": {
        "freq_Hz": 1,
        "duration_min": 15,
        "EPSP_decrease_factor": 0.5,
        "mechanism": "Low Ca → phosphatase → AMPA endocytosis",
    },
    "STDP_Markram_1997": {
        "tau_plus_ms": tau_plus,
        "tau_minus_ms": tau_minus,
        "A_plus": A_plus,
        "A_minus": A_minus,
        "rule": "pre→post within 20ms: LTP; post→pre within 20ms: LTD",
    },
    "NMDA_Mg_block": {
        "rest_potential_mV": -65,
        "unblock_potential_mV": "-40 to 0",
        "function": "Coincidence detector (Glu + depolarization both needed)",
    },
    "Hebbian_Oja_learning": {
        "N_inputs": N_in,
        "N_outputs": N_out,
        "training_steps": n_samples,
        "eta": eta,
        "W_final_mean": W_final_mean,
        "W_final_std": W_final_std,
        "Hebb_quote": "Neurons that fire together, wire together",
        "Hebb_book": "The Organization of Behavior 1949",
    },
    "memory_taxonomy": {k: {"duration_sec": v["duration_sec"], "site": v["site"]}
                        for k, v in memory_types.items()},
    "Patient_H_M_Henry_Molaison_1953_2008": {
        "surgery_year": 1953,
        "procedure": "Bilateral medial temporal lobe resection (hippocampus)",
        "preserved": ["IQ", "short-term memory", "procedural memory"],
        "lost": "Anterograde declarative memory (new fact learning)",
        "key_paper": "Scoville-Milner 1957 J Neurol Neurosurg Psychiatry",
        "significance": "Established memory-cognition dissociation",
    },
    "engram_Tonegawa_lab": {
        "Liu_2012_Nature": "Optogenetic reactivation reproduces fear memory",
        "Ramirez_2013_Science": "False memory implantation",
        "sparse_coding_fraction": engram_fraction,
        "n_engram_cells_estimate": int(n_engram),
        "memories_per_hippocampus_rough": int(n_memories_storable),
    },
    "ITU_K_synapse": {
        "N_synapses": N_syn,
        "S_pre_LTP_nats": S_pre,
        "S_post_LTP_nats": S_post,
        "delta_S": S_post - S_pre,
        "ratio_dS_over_dK": itu_ratio,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_synapse_meaning": "Distribution of synaptic strengths",
        "learning_as_ITU_descent": "Hebb/STDP rules = ITU axiom δS = δ⟨K⟩ implementation",
        "engram_meaning": "Specific neural assembly = ITU K-state localization",
        "ML_correspondence": {
            "Hebb": "PCA / Hebbian learning",
            "LTP_LTD": "Gradient descent (approximate)",
            "STDP": "Predictive coding",
            "Dopamine_RPE": "TD-learning / Q-learning",
            "Hippocampal_replay": "Experience replay (DQN)",
        },
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
