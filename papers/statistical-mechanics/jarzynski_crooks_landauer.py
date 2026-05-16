"""
Phase 147: Fluctuation Theorems — Jarzynski + Crooks + Landauer
================================================================

Tests:
1. Jarzynski equality: ⟨e^{-βW}⟩ = e^{-βΔF}  (harmonic spring shift)
2. Crooks relation:    P_F(W) / P_R(-W) = e^{β(W - ΔF)}
3. Second-law violations: P(W < ΔF) > 0 visible in tails
4. Integral FT: ⟨e^{-σ}⟩ = 1
5. Landauer limit: k_B T ln 2 per erased bit
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import os

np.random.seed(42)

print("=" * 70)
print("Phase 147: Fluctuation Theorems (Jarzynski + Crooks + Landauer)")
print("=" * 70)
print()

k_B = 1.380649e-23  # J/K

# ----------------------------------------------------------------------
# Setup: harmonic oscillator with shifted center, isothermal switching
# ----------------------------------------------------------------------
# U_λ(x) = (1/2) k (x - λ)²
# Protocol: λ(t) from 0 to λ_f over time τ, T = const.
# ΔF = 0 (Gaussian, both ensembles same partition function)
# W along trajectory: W = ∫ ∂U/∂λ dλ̇ dt = -∫ k (x - λ) dλ
# We use overdamped Langevin: γ dx/dt = -k(x - λ(t)) + ξ(t)
# ⟨ξ ξ⟩ = 2 γ k_B T δ.

print("[Setup] Harmonic oscillator U_λ(x) = (1/2) k (x - λ)²")
print("  Protocol: λ(t) = λ_f × (t/τ) — linear ramp from 0 to λ_f")
print("  Overdamped Langevin in reduced units (k_B T = 1, γ = 1, k = 1)")
print("  Since U is harmonic with shifted center, ΔF = 0 exactly.")
print()

beta = 1.0      # k_B T = 1
k_sp = 1.0      # spring constant
gamma_l = 1.0
T_red = 1.0 / beta

lambda_f = 2.0   # final λ shift
tau = 1.0        # protocol time
n_steps = 200
dt = tau / n_steps
n_traj = 5000   # forward trajectories

def run_protocol(n_traj, lam_start, lam_end, n_steps, dt, beta, k_sp, gamma_l, reverse=False):
    """Run an ensemble of overdamped Langevin trajectories with linear λ(t).
       Returns work distribution.
    """
    # Initial equilibrium at lam_start: x ~ N(lam_start, 1/(beta k))
    sigma_eq = np.sqrt(1.0 / (beta * k_sp))
    x = np.random.randn(n_traj) * sigma_eq + lam_start

    W_arr = np.zeros(n_traj)
    lam_prev = lam_start
    dlam = (lam_end - lam_start) / n_steps
    sqrt_2D_dt = np.sqrt(2.0 / (beta * gamma_l) * dt)

    for step in range(n_steps):
        lam_curr = lam_start + (step + 1) * dlam
        # Work increment: dW = ∂U/∂λ × dλ = -k (x - λ) × dλ  (evaluated at current x)
        dW = -k_sp * (x - lam_prev) * (lam_curr - lam_prev)
        W_arr += dW
        # Force at lam_curr: F = -∂U/∂x = -k (x - lam_curr)
        force = -k_sp * (x - lam_curr)
        # Overdamped: dx = (F/γ) dt + sqrt(2 D) dW_brownian
        x = x + (force / gamma_l) * dt + sqrt_2D_dt * np.random.randn(n_traj)
        lam_prev = lam_curr

    return W_arr

print(f"[Test 1+2+3] Jarzynski + Crooks (n_traj = {n_traj}, n_steps = {n_steps}, τ = {tau})")
W_F = run_protocol(n_traj, 0.0, lambda_f, n_steps, dt, beta, k_sp, gamma_l)
W_R = run_protocol(n_traj, lambda_f, 0.0, n_steps, dt, beta, k_sp, gamma_l)

# Jarzynski estimate of ΔF
exp_term = np.exp(-beta * W_F)
DeltaF_jarz = -np.log(np.mean(exp_term)) / beta
DeltaF_true = 0.0  # harmonic with shifted center, exact
DeltaF_naive = np.mean(W_F)   # ⟨W⟩ ≥ ΔF (Jensen)

print(f"  ΔF (true, harmonic) = 0")
print(f"  ⟨W_F⟩ (naive)       = {DeltaF_naive:.4f}   (second-law: ≥ ΔF = 0 ✓)")
print(f"  Jarzynski estimate  = -ln⟨e^(-βW)⟩/β = {DeltaF_jarz:.4f}  (should be ≈ 0)")
print(f"  ⟨W_R⟩ (reverse)     = {np.mean(W_R):.4f}   (reverse: ≥ -ΔF = 0 ✓)")

# Second-law "violations"
frac_violate = np.sum(W_F < DeltaF_true) / n_traj
print(f"  Trajectories with W < ΔF: {frac_violate*100:.1f}% (microscopic 'violation', allowed)")
print(f"  min W_F = {W_F.min():.4f}, max W_F = {W_F.max():.4f}")
print()

# Crooks: compare histograms
print("[Test 2 detail] Crooks: P_F(W) / P_R(-W) = e^(β(W - ΔF))")
bins = np.linspace(-1.0, 4.0, 41)
hF, edges = np.histogram(W_F, bins=bins, density=True)
hR, _ = np.histogram(-W_R, bins=bins, density=True)
centers = 0.5 * (edges[1:] + edges[:-1])
# Avoid division by zero
mask = (hF > 1e-3) & (hR > 1e-3)
ratio = np.zeros_like(hF)
ratio[mask] = hF[mask] / hR[mask]
expected = np.exp(beta * (centers - DeltaF_true))
print(f"  Crossing point (where P_F = P_R(-)): expect W ≈ ΔF = 0")
W_cross_idx = np.argmin(np.abs(hF - hR))
print(f"  Numerical crossing W ≈ {centers[W_cross_idx]:.3f}")
print()

# ----------------------------------------------------------------------
# Test 4: Integral FT ⟨e^{-σ}⟩ = 1
# ----------------------------------------------------------------------
print("[Test 4] Integral fluctuation theorem ⟨e^(-σ_tot)⟩ = 1")
# For this protocol, σ_tot = β(W - ΔF)
sigma_tot = beta * (W_F - DeltaF_true)
exp_minus_sigma = np.mean(np.exp(-sigma_tot))
print(f"  σ_tot = β(W - ΔF), ⟨σ_tot⟩ = {np.mean(sigma_tot):.4f} (≥ 0, second law)")
print(f"  ⟨e^(-σ_tot)⟩ = {exp_minus_sigma:.4f} (should be 1)")
print()

# ----------------------------------------------------------------------
# Test 5: Landauer limit
# ----------------------------------------------------------------------
print("[Test 5] Landauer limit — W_erase ≥ k_B T ln 2 per bit")
T_room = 300.0
W_land = k_B * T_room * np.log(2)
W_land_meV = W_land / 1.602e-19 * 1000.0
print(f"  T = {T_room} K, k_B T ln 2 = {W_land:.3e} J/bit")
print(f"                       = {W_land_meV:.2f} meV/bit")
print(f"  (= {W_land/k_B:.3f} kT-units per bit ≈ {np.log(2):.3f} = ln 2)")
print(f"  Bérut et al. 2012: experimentally verified within experimental precision.")
print()

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# 1) Forward / reverse work distributions
ax = axes[0, 0]
ax.hist(W_F, bins=bins, density=True, alpha=0.5, color='C0', label=f'P_F(W), ⟨W⟩={np.mean(W_F):.2f}')
ax.hist(-W_R, bins=bins, density=True, alpha=0.5, color='C1', label=f'P_R(-W), ⟨W⟩={-np.mean(W_R):.2f}')
ax.axvline(DeltaF_true, color='red', linestyle='--', label=f'ΔF = 0')
ax.axvline(DeltaF_jarz, color='green', linestyle=':', label=f'ΔF_Jarz = {DeltaF_jarz:.3f}')
ax.set_xlabel('W')
ax.set_ylabel('P(W)')
ax.set_title('Crooks: P_F(W) ↔ P_R(-W) crossing at ΔF')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# 2) Crooks ratio test
ax = axes[0, 1]
ax.semilogy(centers[mask], ratio[mask], 'o', label='P_F(W) / P_R(-W)')
ax.semilogy(centers, expected, 'r-', label=f'e^(β(W-ΔF))')
ax.set_xlabel('W')
ax.set_ylabel('Ratio (log)')
ax.set_title('Crooks Detailed Fluctuation Theorem')
ax.legend()
ax.grid(True, alpha=0.3)

# 3) Jarzynski convergence
ax = axes[1, 0]
n_samples_arr = np.logspace(1, np.log10(n_traj), 30, dtype=int)
DF_estimates = []
for n_s in n_samples_arr:
    est = -np.log(np.mean(np.exp(-beta * W_F[:n_s]))) / beta
    DF_estimates.append(est)
ax.semilogx(n_samples_arr, DF_estimates, 'o-', label='Jarzynski ΔF estimate')
ax.axhline(DeltaF_true, color='red', linestyle='--', label='True ΔF = 0')
ax.axhline(DeltaF_naive, color='gray', linestyle=':', label=f'Naive ⟨W⟩ = {DeltaF_naive:.3f}')
ax.set_xlabel('Number of trajectories')
ax.set_ylabel('ΔF estimate')
ax.set_title('Jarzynski Convergence ⟨e^(-βW)⟩ → e^(-βΔF)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# 4) σ_tot distribution and integral FT
ax = axes[1, 1]
ax.hist(sigma_tot, bins=40, density=True, color='C2', alpha=0.6, label=f'P(σ_tot)')
ax.axvline(0, color='red', linestyle='--', label='σ = 0')
ax.axvline(np.mean(sigma_tot), color='green', linestyle=':', label=f'⟨σ⟩ = {np.mean(sigma_tot):.3f}')
ax.text(0.05, 0.95, f'⟨e^(-σ)⟩ = {exp_minus_sigma:.4f}\n(theory: 1.000)',
        transform=ax.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))
ax.set_xlabel('σ_tot = β(W - ΔF)')
ax.set_ylabel('P(σ_tot)')
ax.set_title('Integral FT: ⟨e^(-σ)⟩ = 1')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
out_png = os.path.join(os.path.dirname(__file__), 'jarzynski_crooks_landauer.png')
plt.savefig(out_png, dpi=130)
print(f"  Figure saved: {os.path.basename(out_png)}")

# ----------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------
summary = {
    "phase": 147,
    "title": "Fluctuation theorems — Jarzynski + Crooks + Landauer",
    "tier1_paper": "#21 Statistical Mechanics (phase 5/8)",
    "setup": {
        "potential": "U_λ(x) = (1/2) k (x - λ)^2",
        "protocol": f"linear ramp λ: 0 → {lambda_f}, time τ = {tau}",
        "dynamics": "overdamped Langevin",
        "n_trajectories": n_traj,
        "n_steps": n_steps,
        "k_B_T": 1.0 / beta,
    },
    "tests": {
        "jarzynski": {
            "DeltaF_true": float(DeltaF_true),
            "DeltaF_jarzynski_estimate": float(DeltaF_jarz),
            "mean_W_forward": float(np.mean(W_F)),
            "mean_W_reverse": float(np.mean(W_R)),
            "fraction_W_less_than_DF": float(frac_violate),
        },
        "crooks_crossing_W": float(centers[W_cross_idx]),
        "integral_FT": {
            "mean_sigma_tot": float(np.mean(sigma_tot)),
            "exp_minus_sigma_mean": float(exp_minus_sigma),
            "theory_value": 1.0,
        },
        "landauer": {
            "T_K": T_room,
            "W_min_J_per_bit": float(W_land),
            "W_min_meV_per_bit": float(W_land_meV),
            "kT_units": float(np.log(2)),
            "experimental_verification": "Bérut et al. Nature 483, 187 (2012)",
        },
    },
    "itu_interpretation": {
        "jarzynski": "K_stat path-space exp moment = K_eq boundary contraction",
        "crooks": "K_stat path probability time-reversal duality",
        "second_law": "Jensen inequality corollary of Jarzynski equality",
        "landauer": "K_info ↔ K_thermo minimal conversion cost (1 bit = k_B T ln 2)",
    },
    "key_findings": [
        f"Jarzynski ΔF = {DeltaF_jarz:.3f} (truth 0, naive ⟨W⟩ = {DeltaF_naive:.3f})",
        f"{frac_violate*100:.1f}% trajectories have W < ΔF (allowed microscopic 'violations')",
        f"Crooks crossing point ≈ {centers[W_cross_idx]:.3f} (theory ΔF = 0)",
        f"Integral FT: ⟨e^(-σ)⟩ = {exp_minus_sigma:.4f} (theory 1.000)",
        f"Landauer limit: {W_land:.2e} J/bit = {W_land_meV:.2f} meV/bit at 300 K",
    ],
}

out_json = os.path.join(os.path.dirname(__file__), 'jarzynski_crooks_landauer_summary.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"  JSON saved: {os.path.basename(out_json)}")

print()
print("=" * 70)
print(f"Phase 147 complete: fluctuation theorems = K_stat path-space duality;")
print(f"  Jarzynski ΔF = {DeltaF_jarz:.3f} (true 0); ⟨e^(-σ)⟩ = {exp_minus_sigma:.3f}")
print("=" * 70)
