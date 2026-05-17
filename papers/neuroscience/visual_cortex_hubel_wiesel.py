"""
Phase 201 — Visual cortex + Hubel-Wiesel + perception (K_perception)

Simulations:
  1) Gabor filters simulating V1 simple cell receptive fields
  2) Visual hierarchy: V1 -> V2 -> V4 -> IT receptive field size scaling
  3) Orientation column tuning curves
  4) Ventral vs dorsal stream comparison
  5) CNN history (Neocognitron -> AlexNet -> ResNet -> ViT)
  6) Predictive coding (Rao-Ballard 1999) toy
  7) ITU K_perception axiom check (V1 -> IT descent flow)

Outputs:
  - visual_cortex_hubel_wiesel.png
  - visual_cortex_hubel_wiesel_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("visual_cortex_hubel_wiesel.png")
OUT_JSON = Path(__file__).with_name("visual_cortex_hubel_wiesel_summary.json")

rng = np.random.default_rng(20260604)

# -------------------------------------------------------------
# 1) Gabor filters (V1 simple cell receptive fields)
# -------------------------------------------------------------
def gabor(x, y, theta, sigma=2.0, lambd=4.0, psi=0):
    x_theta = x * np.cos(theta) + y * np.sin(theta)
    y_theta = -x * np.sin(theta) + y * np.cos(theta)
    gauss = np.exp(-(x_theta**2 + y_theta**2) / (2 * sigma**2))
    return gauss * np.cos(2 * np.pi * x_theta / lambd + psi)

X, Y = np.meshgrid(np.linspace(-5, 5, 64), np.linspace(-5, 5, 64))
orientations = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4])
gabor_filters = [gabor(X, Y, t) for t in orientations]

# -------------------------------------------------------------
# 2) Visual hierarchy RF size
# -------------------------------------------------------------
hierarchy = {
    "Retina":   0.05,
    "LGN":      0.1,
    "V1":       0.3,
    "V2":       0.8,
    "V4":       2.0,
    "PIT (post IT)": 6.0,
    "AIT (ant IT)":  15.0,
}

# -------------------------------------------------------------
# 3) Orientation tuning curve
# -------------------------------------------------------------
orient_grid = np.linspace(-90, 90, 200)
preferred = 0  # degrees
sigma_orient = 20  # tuning width
tuning = np.exp(-((orient_grid - preferred) ** 2) / (2 * sigma_orient ** 2))
# Multiple cells with different preferences
multi_tuning = []
preferences = [-60, -30, 0, 30, 60]
for p in preferences:
    multi_tuning.append(np.exp(-((orient_grid - p) ** 2) / (2 * sigma_orient ** 2)))

# -------------------------------------------------------------
# 4) Ventral vs dorsal stream
# -------------------------------------------------------------
ventral_path = ["V1", "V2", "V4", "PIT", "AIT", "Perirhinal", "Hippocampus"]
dorsal_path  = ["V1", "V2", "MT", "MST", "Parietal", "Premotor", "Motor"]

# -------------------------------------------------------------
# 5) CNN history
# -------------------------------------------------------------
cnn_history = {
    "Neocognitron (Fukushima 1980)": {"err_pct": np.nan, "params": 1e4, "year": 1980},
    "LeNet-5 (LeCun 1998)":          {"err_pct": 0.7,   "params": 60e3, "year": 1998},
    "AlexNet (Krizhevsky 2012)":     {"err_pct": 16.4,  "params": 60e6, "year": 2012},
    "VGG-16 (2014)":                 {"err_pct": 7.3,   "params": 138e6, "year": 2014},
    "GoogLeNet (2014)":              {"err_pct": 6.7,   "params": 7e6, "year": 2014},
    "ResNet-152 (He 2015)":          {"err_pct": 3.57,  "params": 60e6, "year": 2015},
    "ViT-Large (2020)":              {"err_pct": 3.5,   "params": 304e6, "year": 2020},
    "CLIP (2021)":                   {"err_pct": 3.5,   "params": 400e6, "year": 2021},
    "Human estimate":                {"err_pct": 5.1,   "params": np.nan, "year": np.nan},
}

# -------------------------------------------------------------
# 6) Predictive coding toy (Rao-Ballard)
# -------------------------------------------------------------
N_input = 100
n_steps = 200
# True latent (slowly varying)
z_true = np.cumsum(rng.normal(0, 0.05, size=n_steps))
W_true = rng.normal(0, 1, size=N_input)
# Observations
y_obs = np.outer(z_true, W_true) + rng.normal(0, 0.5, size=(n_steps, N_input))

# Predictive coding inference
z_est = np.zeros(n_steps)
W_est = rng.normal(0, 0.1, size=N_input)
err_history = []
lr_z = 0.05
lr_W = 0.001
for t in range(1, n_steps):
    # Predict
    y_hat = z_est[t-1] * W_est
    err = y_obs[t] - y_hat
    err_history.append(np.linalg.norm(err))
    # Update z (latent inference)
    z_est[t] = z_est[t-1] + lr_z * np.dot(err, W_est) / (np.linalg.norm(W_est) + 1e-9)
    # Update W (slow learning)
    W_est += lr_W * z_est[t] * err

# -------------------------------------------------------------
# 7) ITU K_perception: V1 -> V4 -> IT descent
# -------------------------------------------------------------
N_states = 2000
# V1: dense edge filter responses
log_fit_v1 = -((np.arange(N_states) - N_states/2) ** 2) / 200_000
p_v1 = np.exp(log_fit_v1); p_v1 /= p_v1.sum()
S_v1 = float(-np.sum(p_v1 * np.log(p_v1)))

# V4: medium-level features (more selective)
log_fit_v4 = log_fit_v1.copy()
log_fit_v4[800:1200] += 2.0
p_v4 = np.exp(log_fit_v4); p_v4 /= p_v4.sum()
S_v4 = float(-np.sum(p_v4 * np.log(p_v4)))

# IT: highly selective (concept cells)
log_fit_it = log_fit_v1.copy()
log_fit_it[900:1100] += 4.0
p_it = np.exp(log_fit_it); p_it /= p_it.sum()
S_it = float(-np.sum(p_it * np.log(p_it)))

# ITU axiom for V1 -> V4 -> IT
def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_v1_v4 = itu_lin(p_v1, p_v4)
ratio_v4_it = itu_lin(p_v4, p_it)

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 201 — Visual Cortex + Hubel-Wiesel + Perception (K_perception)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Gabor filters (V1 simple cells)
ax = axes[0, 0]
combined = np.hstack([g for g in gabor_filters])
ax.imshow(combined, cmap="RdBu_r", aspect="auto")
ax.set_title("V1 simple cell Gabor filters (4 orientations)")
ax.axis("off")

# Panel 2: RF size hierarchy
ax = axes[0, 1]
layers = list(hierarchy.keys())
rfs = list(hierarchy.values())
ax.bar(layers, rfs, color=["#1f77b4", "#aec7e8", "#2ca02c", "#98df8a",
                           "#ff7f0e", "#ffbb78", "#d62728"])
ax.set_ylabel("Receptive field (degrees)")
ax.set_title("Visual hierarchy: 50× RF expansion")
ax.tick_params(axis="x", rotation=20)
ax.grid(True, alpha=0.3, axis="y")

# Panel 3: Orientation tuning
ax = axes[0, 2]
for i, mt in enumerate(multi_tuning):
    ax.plot(orient_grid, mt, "-", lw=1.5, label=f"pref {preferences[i]}°")
ax.set_xlabel("Stimulus orientation (deg)")
ax.set_ylabel("Normalized firing rate")
ax.set_title("Orientation tuning (V1 simple cells)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: CNN history
ax = axes[1, 0]
names_c = [k for k, v in cnn_history.items() if not np.isnan(v["err_pct"])]
errs_c = [cnn_history[k]["err_pct"] for k in names_c]
years_c = [cnn_history[k]["year"] for k in names_c if not np.isnan(cnn_history[k]["year"])]
errs_year = [cnn_history[k]["err_pct"] for k in names_c if not np.isnan(cnn_history[k]["year"])]
ax.scatter(years_c, errs_year, s=100, color="#1f77b4", zorder=5)
human_err = cnn_history["Human estimate"]["err_pct"]
ax.axhline(human_err, color="red", linestyle="--", lw=2,
           label=f"Human ~{human_err}%")
for i, name in enumerate(names_c):
    if np.isnan(cnn_history[name]["year"]): continue
    ax.annotate(name.split("(")[0], (cnn_history[name]["year"], cnn_history[name]["err_pct"]),
                fontsize=6, xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("Year")
ax.set_ylabel("ImageNet top-5 error (%)")
ax.set_title("CNN history (Fukushima 1980 → ViT 2020)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Predictive coding
ax = axes[1, 1]
ax.plot(np.arange(len(z_true)), z_true, "-", color="#1f77b4", lw=2, label="True latent")
ax.plot(np.arange(len(z_est)), z_est, "-", color="#d62728", lw=2, label="Estimated")
ax2 = ax.twinx()
ax2.plot(np.arange(len(err_history)), err_history, "-", color="#2ca02c",
         lw=1, alpha=0.5, label="Prediction error")
ax.set_xlabel("Time step")
ax.set_ylabel("Latent value")
ax2.set_ylabel("Error norm", color="#2ca02c")
ax.set_title("Predictive coding (Rao-Ballard 1999)")
ax.legend(loc="upper left", fontsize=8)
ax2.legend(loc="upper right", fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: ITU V1 -> IT descent
ax = axes[1, 2]
ax.plot(np.arange(N_states), p_v1, "-", color="#1f77b4", lw=1.5,
        label=f"V1   S={S_v1:.3f}")
ax.plot(np.arange(N_states), p_v4, "-", color="#ff7f0e", lw=1.5,
        label=f"V4   S={S_v4:.3f}")
ax.plot(np.arange(N_states), p_it, "-", color="#d62728", lw=1.5,
        label=f"IT   S={S_it:.3f}")
ax.set_xlabel("Representation state index")
ax.set_ylabel("Probability")
ax.set_title(f"Hierarchy: V1→V4 ratio={ratio_v1_v4:.3f}, V4→IT={ratio_v4_it:.3f}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 201,
    "tier1_paper": 28,
    "block": "B",
    "topic": "Visual cortex + Hubel-Wiesel + perception (K_perception)",
    "Hubel_Wiesel_1959_Nobel_1981": {
        "discoverer": "David Hubel + Torsten Wiesel",
        "species": "Cat striate cortex (V1)",
        "discovery": "Orientation-selective simple cells",
        "hierarchy": "Simple -> Complex -> Hypercomplex",
        "Nobel_year": 1981,
    },
    "visual_hierarchy_RF_degrees": hierarchy,
    "ventral_what_stream": ventral_path,
    "dorsal_where_stream": dorsal_path,
    "CNN_history": {k: {"err_pct": v["err_pct"], "params": v["params"], "year": v["year"]}
                     for k, v in cnn_history.items()},
    "key_milestones": {
        "Fukushima_Neocognitron_1980": "First Hubel-Wiesel inspired NN",
        "LeCun_LeNet_1998":            "CNN with backprop",
        "Krizhevsky_AlexNet_2012":     "ImageNet breakthrough (16.4% top-5)",
        "He_ResNet_2015":              "Sub-human performance (3.57%)",
        "ViT_2020":                    "Transformer for vision",
    },
    "concept_cells_Quiroga_2005": {
        "discovery": "Jennifer Aniston neuron",
        "site": "Medial temporal lobe (hippocampus + IT)",
        "abstraction": "Single neuron responds to identity across formats",
    },
    "face_patches_Tsao": {
        "n_patches_macaque_IT": 6,
        "hierarchy": "ML/MF (low) -> AL (mid) -> AM (high invariance)",
        "Chang_Tsao_2017_Cell": "200 neurons can reconstruct face identity",
    },
    "predictive_coding": {
        "Rao_Ballard_1999": "Hierarchical predictive coding",
        "Friston_FEP": "Free energy principle (2010)",
        "simulation_final_error": float(err_history[-1]),
        "simulation_initial_error": float(err_history[0]),
    },
    "ITU_K_perception_hierarchy": {
        "S_V1_nats": S_v1,
        "S_V4_nats": S_v4,
        "S_IT_nats": S_it,
        "V1_to_V4_ratio": ratio_v1_v4,
        "V4_to_IT_ratio": ratio_v4_it,
        "expected_ratio": 1.0,
        "interpretation": "Each hierarchy layer = ITU descent step",
    },
    "ITU_interpretation": {
        "K_state": "K_perception (sub-state of K_neuro)",
        "modular_Hamiltonian": "K_perception^(0) = -log P(stimulus | response)",
        "Hubel_Wiesel_meaning": "Hierarchy of K-states from edges to concepts",
        "CNN_correspondence": "Neocognitron-AlexNet-ResNet = Hubel-Wiesel implementation",
        "predictive_coding_meaning": "Top-down K^(0) + bottom-up error = ITU descent",
        "free_energy_principle": "Friston FEP = ITU variational form (Phase 175 link)",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
