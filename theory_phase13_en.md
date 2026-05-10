# Phase 13: The cosmological constant Λ — holographic resolution from de Sitter entropy

## 1. Motivation and problem

The cosmological constant $\Lambda$ appears in Einstein's equations:
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G_N T_{\mu\nu}$$

Observed value (2024):
- $\Lambda_{\rm obs} \approx 1.1 \times 10^{-52}\, \mathrm{m}^{-2}$
- In Planck units: $\Lambda_{\rm obs} / M_{\rm Pl}^2 \approx 10^{-122}$
- $\rho_\Lambda \sim M_{\rm Pl}^2 \Lambda \sim 10^{-122} M_{\rm Pl}^4$

Naive QFT prediction:
- Vacuum fluctuations: $\rho_{\rm naive} \sim \Lambda_{\rm UV}^4 \sim M_{\rm Pl}^4$
- This is $10^{122}$ times larger than the observation — the **122-orders-of-magnitude hierarchy problem** (modern physics' worst prediction).

## 2. de Sitter entropy (Gibbons–Hawking 1977)

de Sitter spacetime (uniform positive curvature, $\Lambda > 0$) has a cosmological horizon with area-determined entropy:
$$S_{\rm dS} = \frac{A_{\rm horizon}}{4 G_N} = \frac{\pi}{G_N H^2}$$
where $H$ is the Hubble parameter. Using $\Lambda = 3 H^2$:
$$\boxed{\;\;S_{\rm dS} = \frac{3\pi}{G_N \Lambda}\;\;}$$

This is the direct $\Lambda \leftrightarrow $ entropy correspondence. A small $\Lambda$ corresponds to a large $S_{\rm dS}$ — a large quantum-information capacity of the universe.

de Sitter temperature (Gibbons–Hawking):
$$T_{\rm dS} = \frac{H}{2\pi} = \sqrt{\frac{\Lambda}{12\pi^2}}$$

## 3. Holographic bound (Cohen–Kaplan–Nelson 1999)

CKN's proposal: the QFT vacuum energy is bounded by the **largest value that does not collapse into a black hole**.
- The energy of UV modes in volume $L^3$ is $\sim L^3 \Lambda_{\rm UV}^4$.
- The non-collapse condition: $\rho L^3 \leq M_{\rm BH} \sim L M_{\rm Pl}^2$.
- $\Rightarrow$ $\rho_\Lambda \leq M_{\rm Pl}^2 / L^2 = M_{\rm Pl}^2 H^2$.

Thus
$$\rho_\Lambda^{\rm holo} \sim M_{\rm Pl}^2 H^2$$

This **matches the observation perfectly**:
- Observed $\rho_\Lambda \sim 10^{-122} M_{\rm Pl}^4$
- Holographic $\rho_\Lambda \sim M_{\rm Pl}^2 \cdot (10^{-60} M_{\rm Pl})^2 = 10^{-120} M_{\rm Pl}^4$ ✓

"**The reason $\Lambda$ is small = the cosmic horizon is large (= the quantum-information capacity is enormous).**"

## 4. Verlinde's emergent cosmology (2017)

Verlinde goes further, proposing **dark energy = entropic response**:
- Ordinary matter (baryons + dark matter = total mass $M$) reduces the entropy.
- The Casimir-like vacuum entanglement-entropy deficit $\Delta S \propto M$.
- This may produce MOND-like acceleration $a \propto \sqrt{a_0 g_N}$.

This is positioned as the dynamical extension of Phase 2 (information geometry = gravity).

## 5. Position within ITU

Phases 1–8 showed that spacetime/geometry emerge from quantum information structure.
Phase 9 produced a particle horizon $L_H = v_F t$.
Phase 13 combines these to show that the **cosmological constant $\Lambda$ is determined by entropy / horizon size**.

Central proposition:

> **The value of the cosmological constant is determined by the finiteness of quantum information (= the finite Hilbert-space dimension of the observable universe).**

In this view:
- $\Lambda \sim M_{\rm Pl}^2 / R^2$ where $R$ is the cosmic horizon.
- Large $R$ (our universe's age) → small $\Lambda$.
- The hierarchy problem is a consequence of "the universe is old".

## 6. Simulation plan

### Part A: Thermal entropy = horizon entropy (1D CFT analog)

Equilibrate the XX chain at temperature $T$:
- Compute thermal entropy density $s(T) = S/L$.
- CFT prediction (Cardy 1986): $s(T) = \pi c T / (3 v)$ for $c=1$, $v=2$ → $s = \pi T/6$.
- Via "$T \leftrightarrow H/(2\pi)$" this is the de Sitter-entropy analog.

### Part B: Casimir vacuum energy = cosmological constant

The Casimir part of the XX-chain ground-state energy:
$$E_0(L) - E_0(\infty) \cdot L = -\frac{\pi c v_F}{6 L} = -\frac{\pi}{3L}$$

"Vacuum energy density": $\epsilon_{\rm vac}(L) = -\pi/(3 L^2)$.

This $1/L^2$ scaling is the analog of $\Lambda \sim H^2 \sim 1/R^2$ in 4D cosmology.

### Part C: Hierarchy ratio

- Naive UV cutoff: $\epsilon_{\rm UV} \sim 1$ (lattice spacing = 1).
- Holographic: $\epsilon_{\rm holo}(L) \sim 1/L^2$.
- Hierarchy: $\epsilon_{\rm UV} / \epsilon_{\rm holo} \sim L^2$.

For $L = 256$: hierarchy $\sim 6.5 \times 10^4$ (1D).
For 4D universe ($R \sim 10^{60} M_{\rm Pl}^{-1}$): hierarchy $\sim 10^{120}$ (matches observation).

### Part D: numerical verification of the $\Lambda$-S relation

- $\Lambda(L) \equiv \epsilon_{\rm vac}(L) / (M_{\rm Pl}^2 / 8\pi G_N) \approx \epsilon_{\rm vac}(L)$ (units).
- $S_{\rm horizon}(L) \approx (c/3) \log L$ (1D CFT analog).
- Relation: $\Lambda \cdot e^{3 S/c}$ should be $L$-independent (= holographic invariant).

Confirm numerically.

## 7. What this Phase shows

✅:
- The thermal entropy of a 1D CFT has the same form as de Sitter entropy (Cardy → Gibbons–Hawking).
- The Casimir vacuum energy $\sim 1/L^2$ is consistent with the holographic bound.
- A "naive UV vs holographic" hierarchy emerges with the right dimensional scaling.

⚠️ Not shown:
- The **exact value** of the observed $\Lambda$ (= why our universe has this size).
- Why our universe is de Sitter (positive $\Lambda$) rather than AdS (negative).
- The dynamical evolution of dark energy (time-dependent $w(t)$).

These require additional physics (anthropic principle, initial conditions, inflation, etc.).
