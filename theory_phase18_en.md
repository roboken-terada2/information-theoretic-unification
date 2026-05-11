# Phase 18: Dark matter — reproducing galactic rotation curves from emergent gravity

## 1. Motivation — the dark matter problem

Observational facts:
- Galactic **rotation curves are flat**: $V(r) \to$ const at large $r$ (Rubin 1970s)
- Newtonian gravity would predict $V \sim 1/\sqrt{r}$ (confirmed in solar system)
- Galaxy clusters, CMB also indicate missing mass ($\Omega_m \approx 0.27$ vs baryonic $\Omega_b \approx 0.05$)

Mainstream interpretation: about **5× more invisible matter (Cold Dark Matter)** exists
- Hypothetical particles (WIMPs, axions, ...) sought for 30+ years
- LHC / XENON / LUX have found **nothing**

Alternative: **modification of gravity in the low-acceleration limit** (MOND, Milgrom 1983)
- Gravity changes for $a < a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$
- Naturally explains flat rotation curves and Tully-Fisher relation at galactic scale
- No new particles

## 2. Verlinde 2017 — MOND from emergent gravity

Verlinde's claim: the **entanglement entropy of the de Sitter vacuum** generates dark gravity.

### 2.1 Key formula

de Sitter cosmological horizon entropy (Phase 13):
$$S_{\rm dS} = \frac{\pi}{G_N H^2}$$

Baryonic mass $M_B$ **displaces this vacuum entropy**:
$$\Delta S \propto M_B \times (\text{cosmological scale})$$

This entropy displacement generates **additional gravity** (extending Verlinde 2010):
$$a_D = \sqrt{\frac{a_B \cdot a_0}{6}}$$
where $a_B = G M_B / r^2$ is the Newtonian baryonic gravity.

### 2.2 Prediction for the acceleration scale $a_0$

Verlinde's analysis gives:
$$\boxed{\;\;a_0 = \frac{c H_0}{2\pi} \approx 1.14 \times 10^{-10}\,\mathrm{m/s^2}\;\;}$$

This **agrees within observational precision** with the empirical Milgrom value $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$!
- $a_0$ is **calculable from the cosmological Hubble constant**
- Not a free fitting parameter
- → A deep consequence: "the galactic-scale puzzle is connected to cosmological-scale physics"

## 3. MOND interpolation function

Relation between Newtonian acceleration $a_N$ and actual acceleration $a$:
$$\mu(a/a_0)\, a = a_N$$

For the simple interpolation $\mu(x) = x/(1+x)$:
$$a = \frac{a_N + \sqrt{a_N^2 + 4 a_0 a_N}}{2}$$

Limits:
- $a_N \gg a_0$ (solar system): $a \to a_N$ — usual Newton
- $a_N \ll a_0$ (galaxy outer): $a \to \sqrt{a_N a_0}$ — deep MOND

Rotation curve $V^2(r) = r \cdot a(r)$:
- In deep MOND: $V^2 = r \sqrt{G M a_0/r^2} = \sqrt{G M a_0}$
- → **$V$ does not depend on $r$ → flat rotation curve**
- → **Tully-Fisher relation**: $V_\infty^4 = G M a_0$

## 4. Position within ITU

Phase 13 showed:
- Observable universe's Hilbert dimension $\dim \mathcal{H} \sim \exp(S_{\rm dS})$
- $\Lambda \sim 1/R^2$ (holographic bound)

Verlinde's claim is a natural extension of Phase 13:
- Baryonic matter **deforms the Hilbert-space information structure**
- This deformation manifests as additional gravity (= dark-matter effect)
- $a_0 = cH/(2\pi)$ comes from the de Sitter entropy density

In the ITU framework, **dark matter is not virtual matter but the effect of information displacement**.

## 5. Limitations

⚠️ Regimes where MOND/Verlinde **struggles**:
- **Galaxy clusters** (Bullet Cluster etc.): the gravitational-lensing/X-ray offset is hard for MOND alone
- **CMB acoustic peaks**: ΛCDM matches Planck to remarkable precision
- **N-body large-scale structure**: unclear whether MOND alone can reproduce it

Current status: "at galactic scales MOND/Verlinde works astonishingly well; at cosmological scales CDM remains needed". Unified theory open.

## 6. Simulation plan

### Part A: Predicting the acceleration scale $a_0$
- From the observed Hubble $H_0 = 70$ km/s/Mpc compute $a_0^{\rm pred} = c H_0/(2\pi)$
- Compare with MOND empirical value $1.2 \times 10^{-10}\,\mathrm{m/s^2}$

### Part B: Galactic rotation curves
For representative galaxies (Milky Way, Andromeda, NGC 3198, dwarfs):
- Baryonic mass distribution (exponential disk): $\Sigma(R) = \Sigma_0 \exp(-R/R_d)$
- $V_{\rm Newton}(r)$ (ordinary Newton)
- $V_{\rm MOND}(r)$ (via interpolation function)
- Comparison with observed $V_{\rm obs}$

### Part C: Tully-Fisher relation
- For masses $M = 10^7 - 10^{12} M_\odot$, compute $V_\infty(M)$
- Log-log plot: confirm $V_\infty \propto M^{1/4}$

### Part D: Radial Acceleration Relation (RAR)
McGaugh et al. 2016's **universal relation**:
$$g_{\rm obs} = g_{\rm bar} + \sqrt{g_{\rm bar} a_0}$$
(or single universal curve via MOND interpolation). Verified empirically in 170 SPARC galaxies; our calculation should reproduce it.

## 7. What this Phase shows

✅ Demonstrable:
- $a_0 \sim cH/(2\pi)$ matches observation (NOT a free parameter)
- Galactic rotation curves flatten **without dark matter particles**
- Tully-Fisher ($V^4 \propto M$) reproduced
- Radial Acceleration Relation (RAR) naturally emerges

⚠️ Not demonstrable here:
- Precision fits of clusters and CMB
- N-body large-scale structure simulations
- Full Verlinde derivation (de Sitter modular flow → gravitational field equations)

Even so, demonstrating that "galactic rotation curves flatten without DM particles" within the ITU framework is significant.
