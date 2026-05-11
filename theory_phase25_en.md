# Phase 25: CMB temperature power spectrum — semi-analytical Boltzmann

## 1. Motivation and scope

Phase 21 computed the CMB acoustic peak *positions* (ℓ₁ = 220, ℓ₂ = 537, ℓ₃ = 810)
analytically via Hu–Sugiyama. The **peak amplitudes** $C_\ell$ were not addressed.
A full CAMB Boltzmann solve is too heavy here, so this phase uses the simplified
**Hu–White 1996** model to compute $C_\ell$ approximately and compare with
Planck 2018.

The goal is to demonstrate quantitatively:

1. **Why MOND-only fails** at the CMB (both peak positions *and* amplitudes),
2. **Why ITU hybrid (cold QECC) is indistinguishable** from ΛCDM at the linear
   acoustic level.

## 2. Structure of the temperature power spectrum

### 2.1 Physical contributions

The angular power spectrum $D_\ell \equiv \ell(\ell+1) C_\ell / 2\pi$ combines

1. **Sachs–Wolfe effect**: gravitational redshift at last scattering (large angles, $\ell \lesssim 50$).
2. **Acoustic oscillations**: baryon–photon fluid eigenmodes ($\ell \sim 200$–$2500$).
3. **Silk damping**: photon diffusion erases small-scale anisotropy ($\ell \gtrsim 1000$).
4. **Late-time ISW**: dark-energy era potential decay (large angles).
5. **CDM gravitational driving**: matter-dominated potentials boost compression peaks.

### 2.2 Simplified template

$$
D_\ell \approx D_\ell^{\rm SW} + A_0 \cdot D_{\rm drive} \cdot \cos^2\!\left(\frac{\pi (\ell - \ell_1)}{\ell_A}\right) \cdot W_{\rm peak}(\ell) \cdot e^{-(\ell/\ell_D)^{1.8}}
$$

where
- $\ell_A \approx 297$: acoustic angular scale (from Phase 21),
- $D_{\rm drive}(\Omega_m h^2) = z_{\rm eq}/(z_{\rm eq} + z_*)$: CDM driving factor,
- $W_{\rm peak}(\ell)$: per-peak baryon-loading weight (compression vs rarefaction),
- $e^{-(\ell/\ell_D)^{1.8}}$: Silk damping.

### 2.3 The decisive CDM driving factor

Matter–radiation equality redshift $z_{\rm eq} \approx 2.4 \times 10^4 \, \Omega_m h^2$:

| Model | $\Omega_m h^2$ | $z_{\rm eq}$ | $D_{\rm drive}$ |
|---|---|---|---|
| ΛCDM | 0.143 | 3430 | **0.76** |
| MOND-only | 0.022 | 540 | **0.33** |
| ITU hybrid (cold QECC) | 0.143 | 3430 | **0.76** |

For MOND-only, $z_{\rm eq} < z_* = 1090$: matter–radiation equality occurs
*after* recombination, so radiation pressure has already washed out gravitational
potentials. Peaks are roughly **half** as tall.

## 3. Planck 2018 reference

| $\ell$ | $D_\ell$ ($\mu K^2$) | Physical meaning |
|---|---|---|
| 220 | $5775 \pm 50$ | 1st peak (fundamental compression) |
| 540 | $2570 \pm 30$ | 2nd peak (rarefaction, suppressed by R) |
| 815 | $2480 \pm 30$ | 3rd peak (compression, Silk-damped) |
| $A_2/A_1$ | 0.445 | Baryon loading $R \approx 0.7$ |
| $A_3/A_1$ | 0.429 | Drive + Silk combination |

## 4. Numerical results (this phase)

After calibrating ΛCDM to Planck:

| $\ell$ | Planck | ΛCDM | MOND-only | ITU hybrid (cold) |
|---|---|---|---|---|
| 220 | 5775 | **5779** | 2825 | **5779** |
| 540 | 2570 | **2550** | 1040 | **2550** |
| 815 | 2480 | **2449** | 919 | **2449** |
| $A_2/A_1$ | 0.445 | 0.441 | 0.368 | 0.441 |
| $A_3/A_1$ | 0.429 | 0.424 | 0.325 | 0.424 |

**Chi-squared at the three peaks** ($\sigma \approx 40\,\mu K^2$):

| Model | $\chi^2$ | Verdict |
|---|---|---|
| ΛCDM | **0.9** | excellent |
| MOND-only | **8426** | decisively excluded |
| ITU hybrid (cold) | **0.9** | excellent |

The MOND-only first-peak amplitude is $0.49\times$ ΛCDM, consistent with the
driving-factor ratio $0.33/0.76 \approx 0.43$.

## 5. Interpretation in the ITU framework

### 5.1 The cold-QECC hypothesis

If frozen QECC information (Phase 22) behaves as a **pressureless, collisionless**
fluid (equation of state $w = 0$), then it gravitates identically to standard
CDM at linear order. The CMB cannot distinguish ITU hybrid from ΛCDM by
temperature anisotropies alone — same $\Omega_m h^2$, same $D_{\rm drive}$,
same acoustic structure.

This is consistent with the Phase 23 (matter power spectrum) and Phase 24
(Bullet Cluster) results, both of which were also satisfied by cold QECC.

### 5.2 MOND-only is doubly excluded

MOND-only fails CMB on **two independent grounds**:

1. **Peak positions** shift by ~43% because the sound horizon at recombination
   is different (Phase 21).
2. **Peak amplitudes** are ~half as large because the gravitational driving
   factor $D \approx 0.33$ instead of $0.76$ (this phase).

No single parameter adjustment within MOND can fix both simultaneously.

## 6. Caveats

⚠️ This phase does **not** provide:
- Full CAMB-level Boltzmann precision,
- Polarisation spectra $C_\ell^{EE}, C_\ell^{TE}$,
- Lensing reconstruction $C_\ell^{\phi\phi}$,
- Independent baryon density from D/H ratio.

✅ What is established:
- Qualitative three-peak structure with correct relative amplitudes,
- MOND-only's decisive failure quantified ($\chi^2 \approx 8400$),
- ITU hybrid (cold) is **observationally indistinguishable** from ΛCDM.

## 7. ITU status after Phase 25

| Test | Status |
|---|---|
| Linear LSS $P(k)$ (Phase 23) | ✅ ΛCDM-equivalent for ITU hybrid (cold) |
| Bullet Cluster offset (Phase 24) | ✅ Reproduced |
| **CMB peak positions** (Phase 21) | ✅ ΛCDM ≡ hybrid; MOND-only excluded |
| **CMB peak amplitudes** (Phase 25) | ✅ ΛCDM ≡ hybrid; MOND-only excluded |
| BH physics & GW ringdown (Phase 19) | ✅ Match LIGO within 9% |
| Galaxy rotation curves (Phase 18) | ✅ Tully–Fisher reproduced |
| Cluster mass profiles (Phase 20) | ✅ Hybrid required, gap closes to 1% |
| Origin of $\Omega_{\rm CDM}$ (Phase 22) | △ Order-of-magnitude only |

The single remaining theoretical gap is a **first-principles field-theoretic
construction** of frozen QECC as a cold pressureless dust. That is what would
turn the ITU framework into a fully predictive Theory of Everything at the
cosmological level.
