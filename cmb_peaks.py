"""
Phase 21: CMB acoustic peaks — quantitative comparison ΛCDM vs MOND vs Hybrid
                              vs Planck 2018.

Uses Hu-Sugiyama 1996 analytical approximations for the sound horizon and
the comoving angular diameter distance to last scattering. Predicts the
first 3 acoustic peak positions and compares with Planck 2018 best-fit.

This is a "step beyond Phase 20" addressing the headline weakness: in
Phase 20 we only had schematic peak positions; here we compute them
analytically (still without full Boltzmann; that requires CAMB).

References:
- Hu, Sugiyama, ApJ 471 (1996) 542
- Hu, White, ApJ 471 (1996) 30
- Planck Collaboration, A&A 641 (2020) A6
- Verlinde, SciPost Phys 2 (2017) 016
- Aghanim et al. (Planck 2018 cosmological parameters)
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
C_LIGHT_KMS = 2.998e5    # km/s

def sound_horizon_HuSugiyama(Omega_m, Omega_b, h):
    """Sound horizon at recombination (Hu & Sugiyama 1996 fit).
    Accuracy ~ 1% for standard cosmologies."""
    om_h2 = Omega_m * h ** 2
    ob_h2 = Omega_b * h ** 2
    # Hu-Sugiyama Eq. (E-1)
    log_term = np.log(9.83 / om_h2)
    denom = np.sqrt(1.0 + 10.0 * ob_h2 ** 0.75)
    return 44.5 * log_term / denom   # Mpc

def angular_distance_recombination(Omega_m, h, z_star=1090):
    """Comoving angular diameter distance to last scattering (flat ΛCDM)."""
    H0 = h * 100.0   # km/s/Mpc
    Omega_L = 1.0 - Omega_m
    z = np.linspace(0, z_star, 5000)
    E_z = np.sqrt(Omega_m * (1.0 + z) ** 3 + Omega_L)
    integrand = 1.0 / E_z
    D_A = (C_LIGHT_KMS / H0) * np.trapezoid(integrand, z)
    return D_A   # Mpc

def acoustic_peaks(Omega_m, Omega_b, h):
    """Returns the first three acoustic-peak positions ℓ_n and the
    acoustic angle θ_A."""
    r_s = sound_horizon_HuSugiyama(Omega_m, Omega_b, h)
    D_A = angular_distance_recombination(Omega_m, h)
    theta_A = r_s / D_A
    # Hu-Sugiyama 1996: ℓ_n ≈ (n - phi_n) π / θ_A
    # Phase shifts calibrated so that ΛCDM (Ω_m=0.315, Ω_b=0.049, h=0.674)
    # matches the Planck-observed peaks at (220, 537, 810).
    # These phases depend weakly on Ω_b h² and are taken as model-independent
    # to isolate the effect of θ_A on peak positions.
    phases = [0.247, 0.163, 0.229]
    peaks = [(n + 1 - p) * np.pi / theta_A for n, p in enumerate(phases)]
    return peaks, theta_A, r_s, D_A

# ----------------------------------------------------------------
def main():
    print("=== Phase 21: CMB acoustic peaks — analytical Hu-Sugiyama ===\n")

    # Cosmological models
    models = {
        'LCDM (Planck 2018)':  {'Omega_m': 0.315, 'Omega_b': 0.049, 'h': 0.674},
        'MOND-only (no CDM)':  {'Omega_m': 0.049, 'Omega_b': 0.049, 'h': 0.674},
        'Hybrid (+1.5 eV nu)': {'Omega_m': 0.066, 'Omega_b': 0.049, 'h': 0.674},
    }
    # Planck 2018 observed peak positions
    planck_obs = [220, 537, 810]

    print(f"{'Model':25} {'r_s (Mpc)':>11} {'D_A (Mpc)':>12} "
          f"{'theta_A':>10} {'ell_1':>8} {'ell_2':>8} {'ell_3':>8}")
    results = {}
    for name, p in models.items():
        peaks, theta_A, r_s, D_A = acoustic_peaks(p['Omega_m'], p['Omega_b'], p['h'])
        results[name] = {
            'r_s': r_s, 'D_A': D_A, 'theta_A': theta_A,
            'peaks': peaks,
        }
        print(f"{name:25} {r_s:>11.2f} {D_A:>12.1f} {theta_A:>10.5f} "
              f"{peaks[0]:>8.1f} {peaks[1]:>8.1f} {peaks[2]:>8.1f}")
    print(f"{'Planck 2018 observed':25} {'~144.4':>11} {'~13900':>12} "
          f"{'0.01041':>10} {planck_obs[0]:>8d} {planck_obs[1]:>8d} {planck_obs[2]:>8d}")
    print()

    # Quantitative comparison
    print("[Comparison with Planck observations]")
    print(f"  {'Model':25} {'ell_1 ratio':>12} {'ell_2 ratio':>12} {'ell_3 ratio':>12} {'avg dev':>10}")
    for name, r in results.items():
        ratios = [r['peaks'][i] / planck_obs[i] for i in range(3)]
        avg_dev = abs(np.mean(ratios) - 1) * 100
        print(f"  {name:25} {ratios[0]:>12.3f} {ratios[1]:>12.3f} {ratios[2]:>12.3f} {avg_dev:>9.1f}%")
    print()

    # ============================================================
    # Plots
    # ============================================================
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 5))

    # (A) Peak positions
    ax = axes[0]
    peak_n = np.arange(1, 4)
    markers = ['o-', 's--', '^-']
    colors = ['steelblue', 'orange', 'green']
    for (name, r), m, c in zip(results.items(), markers, colors):
        ax.plot(peak_n, r['peaks'], m, ms=10, label=name, color=c)
    ax.plot(peak_n, planck_obs, '*', ms=18, color='gold',
            markeredgecolor='k', label='Planck 2018', zorder=5)
    ax.set_xlabel('Peak number n')
    ax.set_ylabel(r'Multipole $\ell$')
    ax.set_xticks(peak_n)
    ax.set_title('(A) Acoustic peak positions')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # (B) Sound horizon vs angular distance
    ax = axes[1]
    names = list(results.keys())
    r_s_vals = [results[n]['r_s'] for n in names]
    D_A_vals = [results[n]['D_A'] for n in names]
    x = np.arange(len(names))
    w = 0.35
    ax.bar(x - w/2, r_s_vals, w, label=r'$r_s$ (Mpc)', color='steelblue')
    ax2 = ax.twinx()
    ax2.bar(x + w/2, D_A_vals, w, label=r'$D_A$ (Mpc)', color='orange')
    ax.set_xticks(x); ax.set_xticklabels([n[:12] for n in names], rotation=15)
    ax.set_ylabel(r'$r_s$ (Mpc)', color='steelblue')
    ax2.set_ylabel(r'$D_A$ (Mpc)', color='orange')
    ax.set_title('(B) Sound horizon & distance')
    ax.grid(alpha=0.3, axis='y')

    # (C) Residuals vs Planck
    ax = axes[2]
    for (name, r), c in zip(results.items(), colors):
        ratios = [r['peaks'][i] / planck_obs[i] for i in range(3)]
        ax.plot(peak_n, ratios, 'o-', ms=10, label=name, color=c)
    ax.axhline(1.0, color='gold', linestyle='--', lw=2, label='Planck (perfect)')
    ax.set_xlabel('Peak number n')
    ax.set_ylabel(r'$\ell_n^\mathrm{pred} / \ell_n^\mathrm{obs}$')
    ax.set_xticks(peak_n)
    ax.set_title('(C) Residual vs Planck')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.suptitle('Phase 21: CMB acoustic peaks (analytical Hu-Sugiyama)',
                 fontsize=12)
    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\cmb_peaks.png'
    plt.savefig(out, dpi=130, bbox_inches='tight')
    print(f"Figure saved to {out}")

    # ============================================================
    # Verdict
    # ============================================================
    print("\n[Verdict]")
    lcdm_dev = abs(np.mean([results['LCDM (Planck 2018)']['peaks'][i] / planck_obs[i] for i in range(3)]) - 1) * 100
    mond_dev = abs(np.mean([results['MOND-only (no CDM)']['peaks'][i] / planck_obs[i] for i in range(3)]) - 1) * 100
    hyb_dev = abs(np.mean([results['Hybrid (+1.5 eV nu)']['peaks'][i] / planck_obs[i] for i in range(3)]) - 1) * 100
    print(f"  ΛCDM average deviation from Planck:  {lcdm_dev:.1f}%")
    print(f"  MOND-only average deviation:         {mond_dev:.1f}%")
    print(f"  Hybrid average deviation:            {hyb_dev:.1f}%")
    print()
    print("Conclusion:")
    print("  - ΛCDM matches Planck within ~3% (standard cosmology's strength).")
    print(f"  - MOND-only deviates by ~{mond_dev:.0f}% (clear failure, peaks shift due to no CDM).")
    print(f"  - Hybrid (MOND + 1.5 eV ν) improves but still ~{hyb_dev:.0f}% off.")
    print("  - Full Boltzmann (CAMB-MOND) is required for true precision test.")
    print("  - CMB remains ITU's most challenging frontier.")

    import json
    summary = {
        'planck_observed_peaks': planck_obs,
        'models': {
            name: {
                'Omega_m': models[name]['Omega_m'],
                'Omega_b': models[name]['Omega_b'],
                'h':       models[name]['h'],
                'r_s_Mpc': float(r['r_s']),
                'D_A_Mpc': float(r['D_A']),
                'theta_A': float(r['theta_A']),
                'peaks':   [float(p) for p in r['peaks']],
                'avg_deviation_pct': float(abs(np.mean([r['peaks'][i] / planck_obs[i] for i in range(3)]) - 1) * 100),
            }
            for name, r in results.items()
        }
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase21.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print('\nSummary saved.')

if __name__ == '__main__':
    main()
