# Phase 21: CMB acoustic peak positions in ITU

## 1. Motivation

The CMB acoustic peak positions ($\ell_1 \approx 220$, $\ell_2 \approx 540$,
$\ell_3 \approx 815$) are among the most precisely measured numbers in
cosmology (Planck 2018, sub-percent). They depend on the sound horizon at
recombination and the angular diameter distance back to $z_* = 1090$:
$\ell_n = n \pi / \theta_*$ with $\theta_* = r_s / D_A$.

Pure MOND fails this test because without CDM, $z_{\rm eq}$ is shifted to
$\sim 530 < z_*$, mis-locating peaks by ~43%. ITU must therefore either
include dark matter or modify the sound horizon.

## 2. Hu-Sugiyama 1996 analytical computation

The sound horizon
$$r_s = \int_0^{a_*} \frac{c_s\, da}{a^2 H(a)}, \quad
c_s = \frac{c}{\sqrt{3(1 + R)}}, \quad R = \frac{3 \rho_b}{4 \rho_\gamma}.$$

Angular diameter distance $D_A = \frac{1}{1+z_*} \int_0^{z_*} c\, dz / H(z)$.

## 3. Three models compared

| Model | $\Omega_m h^2$ | $\ell_1$ | $\ell_2$ | $\ell_3$ | error vs Planck |
|---|---|---|---|---|---|
| ΛCDM | 0.143 | 220 | 537 | 810 | ~0% (calibrated) |
| MOND-only | 0.022 | 314 | 770 | 1160 | **42.5%** ❌ |
| ITU hybrid (cold QECC) | 0.143 | 220 | 537 | 810 | ~0% ✅ |

Calibrated phase shifts: $\phi_n = 0.247, 0.163, 0.229$ to match Planck exactly
under ΛCDM. ITU hybrid (heavy QECC behaving as cold DM) is indistinguishable
from ΛCDM at the peak-position level.

## 4. Verdict

- ΛCDM and ITU hybrid: both match Planck within calibration.
- MOND-only: decisively excluded by ~43% peak-position offset.

This phase establishes the necessity of a cold dark-matter component
in ITU and motivates the frozen-QECC hypothesis developed in Phase 22.
