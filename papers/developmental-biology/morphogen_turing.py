"""
Phase 210 — Morphogen gradients + Turing pattern + Organogenesis (K_dev_morphogen)

Simulations:
  1) Bicoid exponential gradient (Drosophila)
  2) French flag model (1 morphogen, 2 thresholds → 3 fates)
  3) Turing reaction-diffusion: activator-inhibitor stripes
  4) Major morphogen pathway list
  5) Organogenesis timeline (human)
  6) Lung branching morphogenesis (23 generations)
  7) ITU K_dev_morphogen axiom check

Outputs:
  - morphogen_turing.png
  - morphogen_turing_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("morphogen_turing.png")
OUT_JSON = Path(__file__).with_name("morphogen_turing_summary.json")

rng = np.random.default_rng(20260620)

# -------------------------------------------------------------
# 1) Bicoid gradient
# -------------------------------------------------------------
# Driever-Nüsslein-Volhard 1988
x = np.linspace(0, 500, 200)  # μm (Drosophila egg)
lambda_bicoid = 100  # μm
c_0 = 100
bicoid = c_0 * np.exp(-x / lambda_bicoid)

# -------------------------------------------------------------
# 2) French flag model
# -------------------------------------------------------------
thresh_high = 60
thresh_low = 20
flag = np.where(bicoid > thresh_high, 2,    # red (high)
                np.where(bicoid > thresh_low, 1, 0))  # white (med), blue (low)

# -------------------------------------------------------------
# 3) Turing pattern (activator-inhibitor, Kondo-Asai 1995)
# -------------------------------------------------------------
# Gray-Scott model (Pearson 1993)
N = 100
dx = 1.0
dt = 1.0
Du = 0.16
Dv = 0.08
F = 0.035
k = 0.065

u = np.ones((N, N))
v = np.zeros((N, N))
# Seed at center
r = 5
cx, cy = N//2, N//2
u[cx-r:cx+r, cy-r:cy+r] = 0.5
v[cx-r:cx+r, cy-r:cy+r] = 0.25
u += 0.05 * rng.standard_normal((N, N))
v += 0.05 * rng.standard_normal((N, N))

def laplacian(z):
    return (np.roll(z, 1, 0) + np.roll(z, -1, 0) +
            np.roll(z, 1, 1) + np.roll(z, -1, 1) - 4 * z) / (dx ** 2)

# Run for many iterations
for _ in range(2500):
    Lu = laplacian(u)
    Lv = laplacian(v)
    uvv = u * v * v
    u += dt * (Du * Lu - uvv + F * (1 - u))
    v += dt * (Dv * Lv + uvv - (F + k) * v)

# -------------------------------------------------------------
# 4) Major morphogen pathways
# -------------------------------------------------------------
morphogens = {
    "Sonic Hedgehog (Shh)": {"pathway": "Hedgehog", "role": "Neural tube ventral, limb AP"},
    "BMP":                   {"pathway": "TGF-β",   "role": "DV axis, bone"},
    "Wnt":                   {"pathway": "Wnt/β-cat", "role": "AP axis, gastrulation"},
    "FGF":                   {"pathway": "RTK",     "role": "Limb outgrowth, lung branching"},
    "Retinoic Acid":         {"pathway": "Nuclear receptor", "role": "Hindbrain, limb"},
    "Notch":                 {"pathway": "Notch",   "role": "Lateral inhibition, neurogenesis"},
}

# -------------------------------------------------------------
# 5) Organogenesis timeline (days post-fertilization)
# -------------------------------------------------------------
organo_timeline = {
    "Neural plate":           18,
    "Cardiac progenitor":     17,
    "Heart beat":             22,
    "Neural tube closure":    22,
    "Optic vesicle":          24,
    "Limb buds":              28,
    "Liver primordium":       30,
    "Kidney primordium":      35,
    "Lung branching start":   35,
    "Organogenesis complete": 56,
}

# -------------------------------------------------------------
# 6) Lung branching morphogenesis (23 generations)
# -------------------------------------------------------------
generations = np.arange(0, 24)
n_airways = 2 ** generations  # 2^23 ≈ 8 million terminal bronchioles
total_terminal = int(n_airways[-1])
total_alveoli = 5e8  # 500 million

# -------------------------------------------------------------
# 7) ITU K_dev_morphogen axiom check
# -------------------------------------------------------------
N_cells = 1000
# Pre-morphogen: uniform
log_fit_pre = np.zeros(N_cells)
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Post-morphogen with French flag (3 fates)
positions_1d = np.linspace(0, 500, N_cells)
bicoid_field = c_0 * np.exp(-positions_1d / lambda_bicoid)
# 3 zones with different K
log_fit_post = np.zeros(N_cells)
log_fit_post[bicoid_field > thresh_high] += 3.0
log_fit_post[(bicoid_field > thresh_low) & (bicoid_field <= thresh_high)] += 1.0
p_post = np.exp(log_fit_post); p_post /= p_post.sum()
S_post = float(-np.sum(p_post * np.log(p_post)))

log_p_pre = np.log(np.clip(p_pre, 1e-30, None))
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
# Uniform prior: ratio undefined (both 0), use direct ratio
ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else "uniform_prior_NA"

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 210 — Morphogen Gradients + Turing + Organogenesis (K_dev_morphogen)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Bicoid gradient + French flag
ax = axes[0, 0]
ax.plot(x, bicoid, "-", color="#9467bd", lw=2, label="Bicoid concentration")
ax.axhline(thresh_high, color="red", linestyle="--", alpha=0.5, label=f"High threshold {thresh_high}")
ax.axhline(thresh_low, color="blue", linestyle="--", alpha=0.5, label=f"Low threshold {thresh_low}")
ax.fill_between(x, 0, 110, where=flag == 2, alpha=0.2, color="red", label="Fate A")
ax.fill_between(x, 0, 110, where=flag == 1, alpha=0.2, color="white", edgecolor="gray")
ax.fill_between(x, 0, 110, where=flag == 0, alpha=0.2, color="blue", label="Fate C")
ax.set_xlabel("Position x (μm)")
ax.set_ylabel("Bicoid concentration")
ax.set_title(f"Bicoid gradient + French flag (λ={lambda_bicoid}μm)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Turing pattern (final state)
ax = axes[0, 1]
im = ax.imshow(u, cmap="RdBu", aspect="auto", vmin=0.3, vmax=1.0)
plt.colorbar(im, ax=ax, label="Activator (u)")
ax.set_title("Turing pattern (Gray-Scott, ~Kondo-Asai 1995)")
ax.axis("off")

# Panel 3: Morphogen pathways
ax = axes[0, 2]
m_names = list(morphogens.keys())
y_pos = np.arange(len(m_names))
ax.barh(y_pos, [1] * len(m_names), color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"])
for i, name in enumerate(m_names):
    ax.text(0.5, i, morphogens[name]["pathway"] + " | " + morphogens[name]["role"][:30],
            va="center", ha="center", fontsize=7, color="white", fontweight="bold")
ax.set_yticks(y_pos)
ax.set_yticklabels(m_names, fontsize=8)
ax.set_xticks([])
ax.set_title("6 major morphogen pathways")

# Panel 4: Organogenesis timeline
ax = axes[1, 0]
o_names = list(organo_timeline.keys())
o_days = list(organo_timeline.values())
ax.barh(range(len(o_names)), o_days, color="#9467bd")
ax.set_yticks(range(len(o_names)))
ax.set_yticklabels(o_names, fontsize=7)
ax.set_xlabel("Days post-fertilization")
ax.set_title("Organogenesis timeline (human)")
ax.grid(True, alpha=0.3, axis="x")

# Panel 5: Lung branching (23 generations)
ax = axes[1, 1]
ax.semilogy(generations, n_airways, "o-", color="#1f77b4", lw=2, markersize=6)
ax.axhline(total_alveoli, color="red", linestyle="--", lw=2, label=f"Alveoli ~5e8")
ax.set_xlabel("Branching generation")
ax.set_ylabel("Airway count (log)")
ax.set_title(f"Lung branching: 23 gens → {total_terminal:,} terminal")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")

# Panel 6: ITU K_dev_morphogen
ax = axes[1, 2]
ax.bar(["Pre-morphogen", "Post-morphogen\n(French flag)"], [S_pre, S_post],
       color=["#d62728", "#2ca02c"])
ax.set_ylabel("Entropy (nats)")
title = f"ITU δS={S_post-S_pre:+.3f} nats"
if isinstance(ratio, float):
    title += f", ratio={ratio:.3f}"
else:
    title += " (uniform prior)"
ax.set_title(title)
ax.grid(True, alpha=0.3, axis="y")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 210,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Morphogen gradients + Turing + Organogenesis (K_dev_morphogen)",
    "Wolpert_1969_French_flag": "Positional information via morphogen + thresholds",
    "Bicoid_gradient": {
        "discoverer": "Driever-Nüsslein-Volhard 1988 Cell",
        "lambda_um": int(lambda_bicoid),
        "diffusion_coefficient_um2_per_s": 0.3,
        "half_life_min": 50,
    },
    "Turing_1952": "The Chemical Basis of Morphogenesis (Phil Trans R Soc B)",
    "Turing_pattern_biological": {
        "Kondo_Asai_1995": "Zebrafish stripes",
        "fingerprints": "Predicted human",
        "limb_digit": "Sheth 2012 Science",
        "Gray_Scott_simulation_iterations": 2500,
    },
    "morphogen_pathways_6": morphogens,
    "organogenesis_timeline_days": organo_timeline,
    "lung_branching": {
        "generations": 23,
        "terminal_bronchioles": int(total_terminal),
        "alveoli_per_lung": int(total_alveoli),
        "mechanism": "FGF10 + Shh feedback (fractal-like)",
    },
    "folate_NTD_prevention": "70% reduction (MRC 1991)",
    "ITU_K_dev_morphogen": {
        "N_cells": N_cells,
        "S_pre_nats": S_pre,
        "S_post_nats": S_post,
        "delta_S": S_post - S_pre,
        "ratio_dS_over_dK": ratio if isinstance(ratio, float) else None,
        "note": "Uniform prior: linearization gives 0/0 NaN; direct ΔS shown",
    },
    "ITU_interpretation": {
        "K_state": "K_dev_morphogen",
        "modular_Hamiltonian": "K_dev_morphogen^(0) = -log P(fate | morphogen concentration)",
        "Wolpert_meaning": "Threshold response = K-state quantization",
        "Turing_meaning": "Diffusion-driven instability = K-state spontaneous symmetry breaking",
        "Reaction_diffusion": "ITU dynamic spatial expansion (∂ρ/∂t = D∇²ρ + f(ρ, K))",
    },
    "predictions": [
        ("3D organoid kidney/heart/lung functional", 2030, 0.70, "Strong"),
        ("Synthetic morphogen system in iPS", 2028, 0.65, "Medium"),
        ("Limb regeneration via Turing patch (mammals)", 2035, 0.30, "Weak"),
        ("Fingerprint mathematical prediction validated", 2028, 0.75, "Strong"),
        ("Synthetic bilaterian gastruloid", 2030, 0.65, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
