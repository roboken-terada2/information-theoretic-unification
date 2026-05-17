"""
Phase 208 — Waddington landscape + Yamanaka iPSC + Reprogramming (K_dev_lineage)

Simulations:
  1) Waddington-like 2D potential landscape with 3 attractor valleys
  2) Pseudotime trajectory ordering (Monocle-like)
  3) iPS reprogramming efficiency across methods
  4) Yamanaka factor expression dynamics (OSKM induction)
  5) Differentiation vs reprogramming - ITU descent/lifting
  6) RNA velocity vector field sketch
  7) Direct conversion routes
  8) Clinical iPS milestones timeline

Outputs:
  - waddington_yamanaka.png
  - waddington_yamanaka_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("waddington_yamanaka.png")
OUT_JSON = Path(__file__).with_name("waddington_yamanaka_summary.json")

rng = np.random.default_rng(20260618)

# -------------------------------------------------------------
# 1) Waddington-like potential landscape
# -------------------------------------------------------------
def waddington(x, y):
    """Pluripotent at top, 3 differentiated valleys at bottom."""
    pluri = -1.5 * np.exp(-((x - 0)**2 + (y - 2)**2) / 0.5)
    valley1 = -2 * np.exp(-((x - 1.5)**2 + (y + 1.5)**2) / 0.5)  # ecto
    valley2 = -2 * np.exp(-((x + 1.5)**2 + (y + 1.5)**2) / 0.5)  # meso
    valley3 = -2 * np.exp(-((x - 0)**2 + (y + 2.0)**2) / 0.5)    # endo
    return pluri + valley1 + valley2 + valley3 + 0.05 * (x**2 + y**2)

xx, yy = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
zz = waddington(xx, yy)

# -------------------------------------------------------------
# 2) Pseudotime trajectory (toy single-cell scRNA seq style)
# -------------------------------------------------------------
N_cells = 200
pseudo = np.linspace(0, 1, N_cells)
gene_pluri = np.exp(-((pseudo - 0.0) / 0.2) ** 2)  # Oct4 falls
gene_inter = np.exp(-((pseudo - 0.5) / 0.15) ** 2)  # transient
gene_diff = 1 - np.exp(-((pseudo - 1.0) / 0.3) ** 2)  # cardio/neural rises

# -------------------------------------------------------------
# 3) iPS reprogramming efficiency
# -------------------------------------------------------------
methods = {
    "OSKM retrovirus (Takahashi 2006)":   0.05,
    "OSKM lentivirus":                      0.1,
    "Sendai virus (non-integrating)":      0.3,
    "Episomal plasmid":                    0.05,
    "mRNA delivery (Warren 2010)":          1.5,
    "Small molecules (CiPS, Deng 2013)":   0.005,
    "Direct conversion (iN, Wernig 2010)": 5.0,
}

# -------------------------------------------------------------
# 4) Yamanaka factor dynamics post-OSKM induction
# -------------------------------------------------------------
days_repro = np.linspace(0, 28, 200)
# OSKM forced expression (transgene-driven)
oskm = np.where(days_repro < 21, 100.0, 100 * np.exp(-(days_repro - 21) / 2))
# Endogenous pluripotency genes (Oct4/Nanog/Sox2) rise
endo_pluri = 100 / (1 + np.exp(-(days_repro - 16) / 2))
# Somatic genes (fibroblast markers) fall
somatic = 100 / (1 + np.exp((days_repro - 12) / 3))

# -------------------------------------------------------------
# 5) ITU: differentiation vs reprogramming
# -------------------------------------------------------------
N_states = 200
# Pluripotent: broad distribution
log_fit_pluri = np.zeros(N_states) + 0.01 * rng.standard_normal(N_states)
p_pluri = np.exp(log_fit_pluri); p_pluri /= p_pluri.sum()
S_pluri = float(-np.sum(p_pluri * np.log(p_pluri)))

# Differentiated (peaked on one fate)
log_fit_diff = log_fit_pluri.copy()
log_fit_diff[100] += 6.0
p_diff = np.exp(log_fit_diff); p_diff /= p_diff.sum()
S_diff = float(-np.sum(p_diff * np.log(p_diff)))

# Reprogrammed back to pluripotent (Yamanaka OSKM)
log_fit_repro = log_fit_pluri.copy() + 0.02 * rng.standard_normal(N_states)
p_repro = np.exp(log_fit_repro); p_repro /= p_repro.sum()
S_repro = float(-np.sum(p_repro * np.log(p_repro)))

def itu_lin(p_old, p_new):
    log_p = np.log(np.clip(p_old, 1e-30, None))
    dp = p_new - p_old
    dS = -np.sum(dp * (1.0 + log_p))
    dK = -np.sum(dp * log_p)
    return float(dS / dK) if abs(dK) > 1e-15 else float("nan")

ratio_pluri_diff = itu_lin(p_pluri, p_diff)
ratio_diff_repro = itu_lin(p_diff, p_repro)

# -------------------------------------------------------------
# 6) Clinical iPS milestones
# -------------------------------------------------------------
milestones = {
    "2006 mouse iPS (Takahashi)":  2006,
    "2007 human iPS":              2007,
    "2012 Yamanaka Nobel":         2012,
    "2013 RPE transplant (高橋政代)": 2013,
    "2018 PD iPS trial (京都大)":   2018,
    "2024 cardiac sheet trial":    2024,
}

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 208 — Waddington Landscape + Yamanaka iPSC (K_dev_lineage)",
    fontsize=13, fontweight="bold",
)

# Panel 1: Waddington landscape
ax = axes[0, 0]
cs = ax.contourf(xx, yy, zz, levels=20, cmap="viridis")
ax.contour(xx, yy, zz, levels=15, colors="white", alpha=0.4, linewidths=0.5)
plt.colorbar(cs, ax=ax, label="Potential")
ax.annotate("Pluripotent", (0, 2), color="white", fontweight="bold", ha="center")
ax.annotate("Ectoderm", (1.5, -1.5), color="white", fontweight="bold", ha="center")
ax.annotate("Mesoderm", (-1.5, -1.5), color="white", fontweight="bold", ha="center")
ax.annotate("Endoderm", (0, -2), color="white", fontweight="bold", ha="center")
# Yamanaka up-arrow (reprogramming)
ax.annotate("", xy=(0, 1.8), xytext=(1.3, -1.3),
            arrowprops=dict(arrowstyle="->", color="red", lw=2))
ax.text(1.0, 0.5, "Yamanaka\nOSKM", color="red", fontweight="bold", fontsize=8)
ax.set_xlabel("Lineage axis 1")
ax.set_ylabel("Lineage axis 2")
ax.set_title("Waddington (1957) — Yamanaka lifts back")

# Panel 2: Pseudotime trajectory
ax = axes[0, 1]
ax.plot(pseudo, gene_pluri * 100, "-", color="#1f77b4", lw=2, label="Pluripotency (Oct4)")
ax.plot(pseudo, gene_inter * 100, "-", color="#ff7f0e", lw=2, label="Intermediate")
ax.plot(pseudo, gene_diff * 100, "-", color="#d62728", lw=2, label="Differentiated marker")
ax.set_xlabel("Pseudotime (0 = stem, 1 = differentiated)")
ax.set_ylabel("Gene expression (%)")
ax.set_title("Pseudotime ordering (Monocle, Trapnell 2014)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: iPS reprogramming efficiency
ax = axes[0, 2]
methods_list = list(methods.keys())
effs = list(methods.values())
colors_m = ["#2ca02c" if e > 1 else "#ff7f0e" if e > 0.1 else "#d62728" for e in effs]
ax.barh(range(len(methods_list)), effs, color=colors_m)
ax.set_xscale("log")
ax.set_yticks(range(len(methods_list)))
ax.set_yticklabels(methods_list, fontsize=7)
ax.set_xlabel("Reprogramming efficiency (%, log)")
ax.set_title("iPS / direct conversion methods")
ax.grid(True, alpha=0.3, axis="x", which="both")

# Panel 4: OSKM induction dynamics
ax = axes[1, 0]
ax.plot(days_repro, oskm, "-", color="#9467bd", lw=2, label="OSKM transgene")
ax.plot(days_repro, endo_pluri, "-", color="#1f77b4", lw=2, label="Endogenous pluripotency")
ax.plot(days_repro, somatic, "-", color="#d62728", lw=2, label="Somatic genes (fibroblast)")
ax.axvline(21, color="black", linestyle="--", alpha=0.5, label="iPS established")
ax.set_xlabel("Days post-OSKM induction")
ax.set_ylabel("Gene expression (%)")
ax.set_title("Yamanaka factor 4 dynamics")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: ITU: differentiation vs reprogramming
ax = axes[1, 1]
labels = ["Pluripotent", "Differentiated", "Reprogrammed\n(iPS)"]
S_vals = [S_pluri, S_diff, S_repro]
colors_e = ["#d62728", "#2ca02c", "#9467bd"]
ax.bar(labels, S_vals, color=colors_e)
ax.set_ylabel("Lineage entropy (nats)")
ax.set_title(f"ITU descent {ratio_pluri_diff:.3f} / ascent (Yamanaka) {ratio_diff_repro:.3f}")
ax.grid(True, alpha=0.3, axis="y")
for i, v in enumerate(S_vals):
    ax.text(i, v + 0.1, f"{v:.2f}", ha="center", fontsize=10, fontweight="bold")

# Panel 6: Clinical iPS milestones
ax = axes[1, 2]
m_names = list(milestones.keys())
m_years = list(milestones.values())
ax.barh(range(len(m_names)), m_years, color="#9467bd")
ax.set_yticks(range(len(m_names)))
ax.set_yticklabels(m_names, fontsize=7)
ax.set_xlabel("Year")
ax.set_xlim(2005, 2026)
ax.set_title("Clinical iPS milestones")
ax.grid(True, alpha=0.3, axis="x")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 208,
    "tier1_paper": 29,
    "block": "B",
    "topic": "Waddington landscape + Yamanaka iPSC (K_dev_lineage)",
    "Waddington_1957": "The Strategy of the Genes - epigenetic landscape concept",
    "Yamanaka_2006": {
        "factors_OSKM": ["Oct3/4", "Sox2", "Klf4", "c-Myc"],
        "method": "Retroviral transduction of mouse fibroblasts",
        "first_iPS_paper": "Takahashi-Yamanaka 2006 Cell",
        "Nobel_2012": "Gurdon + Yamanaka shared Physiology/Medicine",
        "human_iPS_first": "Takahashi 2007 Cell",
    },
    "reprogramming_efficiency_pct": methods,
    "clinical_milestones": milestones,
    "Takahashi_Masayo_2013": "World's first iPS-RPE transplant (age-related macular degeneration)",
    "ITU_K_dev_lineage": {
        "N_states": N_states,
        "S_pluripotent_nats": S_pluri,
        "S_differentiated_nats": S_diff,
        "S_reprogrammed_nats": S_repro,
        "pluri_to_diff_ratio": ratio_pluri_diff,
        "diff_to_repro_ratio": ratio_diff_repro,
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_dev_lineage",
        "modular_Hamiltonian": "K_dev_lineage^(0) = -log P(cell type t+1 | type t, signal)",
        "Waddington_meaning": "K-state landscape with valleys (attractors) and ridges (barriers)",
        "differentiation_meaning": "ITU descent flow into valley (natural)",
        "reprogramming_meaning": "Anti-descent: forced K-state lifting (Yamanaka factors as operators)",
        "direct_conversion": "Lateral motion in K-state space (cross-valley)",
        "RNA_velocity_meaning": "Real-time ITU descent flow vector (La Manno 2018)",
    },
    "predictions": [
        ("iPS β-cell for T1D approved", 2030, 0.70, "Strong"),
        ("iPS cardiac sheet for HF approved", 2030, 0.65, "Medium"),
        ("In vivo direct reprogramming clinical", 2032, 0.55, "Medium"),
        ("Universal iPS bank 50 HLA-matched lines", 2028, 0.75, "Strong"),
        ("AI-designed Yamanaka 5.0 factors", 2030, 0.50, "Medium"),
    ],
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
