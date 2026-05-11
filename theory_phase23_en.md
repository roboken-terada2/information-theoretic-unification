# Phase 23: Linear matter power spectrum $P(k)$ in ITU

## 1. Motivation

The galaxy power spectrum from SDSS/BOSS/DESI measures $P(k)$ to ~1% on
scales $0.01 \lesssim k \lesssim 1\, h/{\rm Mpc}$, with a turnover near
$k_{\rm eq} \approx 0.015\, h/{\rm Mpc}$ set by matter-radiation equality.
ITU must reproduce this curve to be a viable cosmology.

## 2. BBKS transfer function

Linear $P(k) = A \, k^{n_s} T^2(k)$ with $n_s \approx 0.965$ and the
Bardeen-Bond-Kaiser-Szalay 1986 transfer function

$$T(q) = \frac{\ln(1 + 2.34 q)}{2.34 q}
   \left[1 + 3.89 q + (16.1 q)^2 + (5.46 q)^3 + (6.71 q)^4\right]^{-1/4}$$

with $q = k / \Gamma$ and shape parameter $\Gamma = \Omega_m h$ (with the
Sugiyama 1995 baryon correction).

## 3. Three models compared

Normalised to $\sigma_8 = 0.811$ (Planck):

| Model | $\Omega_m$ | $k_{\rm peak}$ (h/Mpc) | $A_{\rm norm}$ | Verdict |
|---|---|---|---|---|
| ΛCDM | 0.315 | 0.015 | reference | ✅ matches SDSS |
| MOND-only | 0.049 | 0.002 | ~50× too large | ❌ excluded |
| **ITU hybrid (cold)** | 0.315 | 0.015 | = ΛCDM | **✅ indistinguishable** |

## 4. Verdict

- **ΛCDM**: matches observed $P(k)$ and $\sigma_8$ exactly.
- **MOND-only**: requires unphysically large primordial amplitude; turnover
  position incompatible with SDSS.
- **ITU hybrid (cold QECC)**: identical to ΛCDM if the frozen QECC is
  effectively cold ($w = 0$).

This is the second cosmological test (after CMB peaks, Phase 21) that ITU
must pass by adopting the cold-QECC hypothesis. The combined evidence from
Phases 21 and 23 makes the cold-QECC mechanism essentially required.

## 5. Caveats

Linear $P(k)$ only; non-linear structure formation (N-body), BAO peak
positions, and weak-lensing $P(k)$ are addressed in subsequent phases.
