"""
Phase 202 — Hippocampus + Place Cell + Grid Cell + Episodic Memory (K_memory)

Simulations:
  1) Place cell place fields in 2D arena
  2) Grid cell hexagonal firing pattern
  3) Theta phase precession
  4) Sharp-wave ripples (SWR) replay at 10-20x speed
  5) Tulving episodic vs semantic memory
  6) Hippocampal trisynaptic circuit
  7) ITU K_memory axiom check during episodic encoding

Outputs:
  - hippocampus_place_grid.png
  - hippocampus_place_grid_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("hippocampus_place_grid.png")
OUT_JSON = Path(__file__).with_name("hippocampus_place_grid_summary.json")

rng = np.random.default_rng(20260605)

# -------------------------------------------------------------
# 1) Place cells in 2D arena
# -------------------------------------------------------------
arena_size = 100  # cm
xs = np.linspace(0, arena_size, 50)
ys = np.linspace(0, arena_size, 50)
XX, YY = np.meshgrid(xs, ys)

# 5 place cells at different locations
place_centers = [(25, 25), (75, 25), (50, 50), (25, 75), (75, 75)]
place_sigma = 12  # cm, field radius
place_fields = []
for cx, cy in place_centers:
    field = np.exp(-((XX - cx)**2 + (YY - cy)**2) / (2 * place_sigma**2))
    place_fields.append(field)
# Combined map
combined_place = np.maximum.reduce(place_fields)

# -------------------------------------------------------------
# 2) Grid cell hexagonal pattern
# -------------------------------------------------------------
def grid_cell(x, y, spacing=30, theta=0, x0=0, y0=0):
    """Sum of 3 cosines at 60° angles -> hexagonal pattern."""
    angles = [theta, theta + np.pi/3, theta + 2*np.pi/3]
    out = np.zeros_like(x)
    for a in angles:
        kx = np.cos(a) * (2 * np.pi / spacing)
        ky = np.sin(a) * (2 * np.pi / spacing)
        out += np.cos(kx * (x - x0) + ky * (y - y0))
    return out / 3.0

grid_30 = grid_cell(XX, YY, spacing=30)
grid_50 = grid_cell(XX, YY, spacing=50)

# -------------------------------------------------------------
# 3) Theta phase precession
# -------------------------------------------------------------
# Position trajectory through place field
positions = np.linspace(-1.5, 1.5, 200) * place_sigma  # σ units
theta_phase_grid = np.linspace(0, 2*np.pi, 100)

# Phase precession: spike phase advances as position progresses
# Skaggs 1996: phase = 360° - (position relative shift) * scale
spike_positions = np.linspace(-1.0, 1.0, 50) * place_sigma
spike_phases = 2*np.pi - (spike_positions / place_sigma) * np.pi  # advances as moves forward

# -------------------------------------------------------------
# 4) SWR replay
# -------------------------------------------------------------
# During movement: place cells fire in sequence at ~8 Hz theta
# During SWR: same sequence at 10-20x compressed
t_awake = np.linspace(0, 5, 500)
n_cells = 10
cell_centers_t = np.linspace(0.5, 4.5, n_cells)
awake_spikes = []
for c in cell_centers_t:
    spikes_t = c + 0.05 * rng.standard_normal(20)
    awake_spikes.append(spikes_t)

# Replay: same order, 15x faster
t_replay_start = 2.0
replay_duration = (4.5 - 0.5) / 15
cell_centers_r = np.linspace(t_replay_start,
                              t_replay_start + replay_duration, n_cells)
replay_spikes = []
for c in cell_centers_r:
    spikes_r = c + 0.003 * rng.standard_normal(8)
    replay_spikes.append(spikes_r)

# -------------------------------------------------------------
# 5) Episodic vs Semantic memory
# -------------------------------------------------------------
memory_features = {
    "Episodic": {"autonoetic": True, "context": True, "time_specific": True,
                  "site": "Hippocampus + frontal", "example": "Last summer in Paris"},
    "Semantic": {"autonoetic": False, "context": False, "time_specific": False,
                  "site": "Temporal cortex", "example": "Paris = capital of France"},
}

# -------------------------------------------------------------
# 6) Trisynaptic circuit
# -------------------------------------------------------------
trisynaptic = ["Entorhinal Cortex layer II",
                "Dentate Gyrus",
                "CA3",
                "CA1",
                "Subiculum",
                "Entorhinal Cortex layer V"]

# -------------------------------------------------------------
# 7) ITU K_memory axiom check
# -------------------------------------------------------------
N_traces = 2000
# Pre-encoding: broad neural state distribution
log_fit_pre = -((np.arange(N_traces) - N_traces/2) ** 2) / 100_000
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Encoding: specific assembly recruited for new episode (sparse 2.5%)
encoded_mask = (np.arange(N_traces) > 1900) | (np.arange(N_traces) < 50)  # ~5% sparse
log_fit_post = log_fit_pre.copy()
log_fit_post[encoded_mask] += 3.0
p_post = np.exp(log_fit_post); p_post /= p_post.sum()
S_post = float(-np.sum(p_post * np.log(p_post)))

log_p_pre = np.log(np.clip(p_pre, 1e-30, None))
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 202 — Hippocampus + Place + Grid + Episodic Memory (K_memory)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Place cells
ax = axes[0, 0]
im = ax.imshow(combined_place, extent=[0, arena_size, 0, arena_size],
                origin="lower", cmap="hot", aspect="auto")
for cx, cy in place_centers:
    ax.plot(cx, cy, "w+", markersize=10, markeredgewidth=2)
plt.colorbar(im, ax=ax, label="Firing rate")
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.set_title("Place cell place fields (O'Keefe 1971, Nobel 2014)")

# Panel 2: Grid cell hexagonal
ax = axes[0, 1]
im = ax.imshow(grid_30, extent=[0, arena_size, 0, arena_size],
                origin="lower", cmap="viridis", aspect="auto")
plt.colorbar(im, ax=ax, label="Firing rate")
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.set_title("Grid cell hex pattern (Moser 2005, Nobel 2014)")

# Panel 3: Theta phase precession
ax = axes[0, 2]
ax.scatter(spike_positions, np.degrees(spike_phases), s=20, color="#1f77b4")
ax.set_xlabel("Position in place field (cm)")
ax.set_ylabel("Theta phase (deg)")
ax.set_title("Theta phase precession (Skaggs 1996)")
ax.grid(True, alpha=0.3)

# Panel 4: SWR replay
ax = axes[1, 0]
for i, sp in enumerate(awake_spikes):
    ax.scatter(sp, [i]*len(sp), s=15, color="#1f77b4", label="Awake" if i == 0 else None)
for i, sp in enumerate(replay_spikes):
    ax.scatter(sp, [i]*len(sp), s=25, color="#d62728", marker="*",
                label="SWR replay (15×)" if i == 0 else None)
ax.set_xlabel("Time (sec)")
ax.set_ylabel("Place cell ID")
ax.set_title("Hippocampal replay (Wilson-McNaughton 1994)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Trisynaptic circuit
ax = axes[1, 1]
y_pos = np.arange(len(trisynaptic), 0, -1)
ax.barh(y_pos, [1]*len(trisynaptic), color="#9467bd", alpha=0.7)
for i, name in enumerate(trisynaptic):
    ax.text(0.5, y_pos[i], name, ha="center", va="center",
            fontsize=9, fontweight="bold", color="white")
ax.set_yticks([])
ax.set_xticks([])
ax.set_title("Hippocampal trisynaptic circuit")

# Panel 6: ITU K_memory
ax = axes[1, 2]
ax.plot(np.arange(N_traces), p_pre, "-", color="#1f77b4", lw=1.5,
        label=f"Pre-encoding  S={S_pre:.3f}")
ax.plot(np.arange(N_traces), p_post, "-", color="#d62728", lw=1.5,
        label=f"Post-encoding S={S_post:.3f}")
ax.set_xlabel("Neural trace index")
ax.set_ylabel("Probability")
ax.set_title(f"Episodic encoding;  ITU δS/δ⟨K⟩ = {itu_ratio:.6f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 202,
    "tier1_paper": 28,
    "block": "B",
    "topic": "Hippocampus + place/grid cells + episodic memory (K_memory)",
    "Nobel_2014_OKeefe_Moser": {
        "OKeefe_1971": "Place cell discovery in CA1",
        "Moser_couple_2005": "Grid cell discovery in MEC",
        "Nobel_year": 2014,
        "category": "Physiology/Medicine",
    },
    "place_cell_properties": {
        "field_diameter_cm": "20-50",
        "coding_fraction_per_env": "30-40%",
        "remapping_time_hr": "1-2",
    },
    "grid_cell_properties": {
        "spacing_range_cm": "30 to several m",
        "hex_symmetry_deg": 60,
        "modules": "5-10 discrete spacing levels",
        "MEC_location": "Medial entorhinal cortex",
    },
    "other_spatial_cells": {
        "head_direction": "Anterodorsal thalamus",
        "border_cell": "MEC + subiculum",
        "object_vector": "MEC + subiculum",
        "time_cell": "CA1 (MacDonald 2011)",
        "speed_cell": "MEC",
    },
    "episodic_vs_semantic": memory_features,
    "Tulving_mental_time_travel": "Tulving 2002 - autonoetic consciousness",
    "trisynaptic_circuit": trisynaptic,
    "SWR_replay": {
        "speed_compression": "10-20×",
        "Wilson_McNaughton_1994": "Hippocampal replay during slow-wave sleep",
        "consolidation_role": "Hippocampus -> cortex transfer (Marr 1971)",
    },
    "ITU_K_memory": {
        "N_traces": int(N_traces),
        "S_pre_encoding_nats": S_pre,
        "S_post_encoding_nats": S_post,
        "delta_S": S_post - S_pre,
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_memory (sub-state of K_neuro)",
        "modular_Hamiltonian": "K_memory^(0) = -log P(experience | reactivation)",
        "decomposition": "K_episodic = K_space ⊗ K_time ⊗ K_what",
        "place_grid_meaning": "Discrete K-state index over spatial manifold",
        "consolidation_meaning": "Slow K-state transfer hippocampus -> cortex",
        "replay_meaning": "Accelerated ITU descent flow during SWR",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
