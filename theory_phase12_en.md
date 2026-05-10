# Phase 12: Electroweak symmetry breaking — the dynamical picture of the Higgs mechanism

## 1. Motivation

In Phase 10 we showed that the Standard Model gauge group SU(3)$\times$SU(2)$\times$U(1)$_Y$ appears as the flavour symmetry of the boundary CFT.
But in nature, SU(2)$_L$ × U(1)$_Y$ is not exactly conserved; it is **spontaneously broken to U(1)$_{\rm em}$**:
- Weak bosons $W^\pm, Z$ have masses 80, 91 GeV
- The photon $\gamma$ is massless
- Fermions also acquire masses (= via Yukawa coupling to the Higgs)

This **electroweak symmetry breaking (EWSB)** is explained by the **Higgs mechanism** (Anderson 1963, Brout–Englert 1964, Higgs 1964). This Phase implements EWSB within ITU and demonstrates it numerically.

## 2. Essence of the Higgs mechanism

### 2.1 The Mexican-hat potential

The potential of a scalar (Higgs) field $\phi$:
$$V(\phi) = -\mu^2 |\phi|^2 + \lambda |\phi|^4, \quad \mu^2, \lambda > 0$$

The minimum is at $|\phi|^2 = \mu^2/(2\lambda) \equiv v^2/2$ ($v$ = Higgs VEV); $\phi = 0$ is an unstable maximum.

### 2.2 Goldstone–Higgs modes

A continuous symmetry $G$ spontaneously breaks to a subgroup $H$ (the coset $G/H$):
- **Goldstone modes**: $\dim(G/H)$ massless fields (= $\phi$ fluctuations along the broken generators)
- **Higgs modes**: $\dim(G) - \dim(G/H)$ massive fields (= amplitude fluctuations)

In gauge theories, Goldstones are "eaten" by gauge fields → gauge-boson masses.

### 2.3 Gauge-boson masses (Anderson–Higgs)

In the gauge theory, $\phi$ couples to gauge fields via the covariant derivative $D_\mu \phi = (\partial_\mu - i g A_\mu^a T^a)\phi$:
$$|D_\mu\langle\phi\rangle|^2 = g^2 v^2 (T^a A_\mu^a)(T^b A^{b\mu}) \to m_W^2 = g^2 v^2/4$$

For electroweak:
- $m_W = gv/2 \approx 80$ GeV
- $m_Z = \sqrt{g^2+g'^2}\,v/2 \approx 91$ GeV
- The photon corresponds to the unbroken U(1)$_{\rm em}$ and is massless.

### 2.4 Fermion masses

The Yukawa coupling $y \bar\psi_L \phi \psi_R$ in the broken phase:
$$y \bar\psi_L \phi \psi_R \to y v\, \bar\psi_L \psi_R = m_\psi \bar\psi\psi$$
giving fermion mass $m_\psi = y v$ — connecting back to Phase 11's Yukawa hierarchy.

## 3. Minimal lattice implementation

### 3.1 1D free fermion + Dirac mass

The simplest implementation is a **1D chain with staggered mass**:
$$H = -t \sum_i (c_i^\dagger c_{i+1} + \mathrm{h.c.}) + m \sum_i (-1)^i\, c_i^\dagger c_i$$

This has a discrete chiral symmetry (the Dirac massless limit). $m$ corresponds to "Higgs VEV $\times$ Yukawa".

### 3.2 Bloch Hamiltonian on a 2-site unit cell

For PBC and even $N$, taking the (even, odd) unit cell:
$$H(k) = -2t\cos(k/2)\,\sigma_x - m\,\sigma_z$$

Energy eigenvalues:
$$\epsilon_\pm(k) = \pm\sqrt{4t^2\cos^2(k/2) + m^2}$$

### 3.3 Automatic gap opening

- $m = 0$: $\epsilon(k=\pi) = 0$ → **gapless** (= critical = symmetry preserved)
- $m > 0$: $\epsilon_\pm(k=\pi) = \pm m$ → **gap $= 2m$ opens** (= mass acquired)

A minimal model of "**Higgs VEV → fermion mass**".

## 4. Verifiable structures

### 4.1 Gap $\propto$ mass

$\Delta_{\rm gap}(m) = 2m$ — confirm linearity numerically.

### 4.2 Phase transition in entanglement

- $m = 0$ (critical): $S(L) = (c/3)\log L$ (Calabrese–Cardy, $c=1$)
- $m > 0$ (gapped): $S(L) \to S_\infty$ (saturation, area law)

Their sharp contrast is the quantum-information signature of EWSB.

### 4.3 Mexican Hat → spontaneous breaking

Add an external Higgs potential $V(\Delta) = -\mu^2 \Delta^2 + \lambda \Delta^4$. Minimise the total energy
$$F(\Delta) = E_{\rm kinetic}(\Delta) + V(\Delta)$$
over $\Delta$. For $\mu^2 > 0$, $\Delta_{\min} \neq 0$ — **spontaneous breaking** (= EWSB).

Prediction: $\Delta_{\rm VEV} = \sqrt{\mu^2/(2\lambda)}$ (analytic minimum of the Mexican hat).

## 5. Position within ITU

In Phases 10 and 11 we derived the SM gauge group and matter hierarchy. Phase 12 adds:

> **The spontaneous breaking of the boundary CFT's flavour symmetry is a natural property of any system with appropriate interaction (or external potential). The Mexican hat is the minimal form of Higgs self-interaction, and is naturally allowed within the ITU framework (Phase 10's global symmetry).**

That is, **the Higgs mechanism itself is a standard QFT phenomenon, and it operates within ITU in the same way**. This Phase confirms that EWSB is **fully expressible within Phases 1–11**.

This gives us:
- Phases 1–3, 7, 8: spacetime, geometry
- Phases 4, 9: time, cosmology
- Phases 5, 6: holography, BH information
- Phase 10: gauge groups
- Phase 11: matter hierarchy
- **Phase 12: electroweak symmetry breaking + fermion masses** ← this Phase

all from a single information-theoretic axiom $\delta S = \delta\langle K\rangle$ + the structure of a boundary CFT.

## 6. Limitations

⚠️ This Phase does **not** show:
- Why $\mu^2$ in the Mexican hat has its observed value (the hierarchy problem)
- Vacuum stability (the RG flow of the Higgs coupling)
- The dynamical origin of symmetry breaking (technicolor or composite Higgs)
- Chirality (only left-handed in weak interaction) — addressed in Phase 15

These have candidate explanations (supersymmetry, technicolor, additional symmetries, etc.) but lie outside the scope of this Phase.
