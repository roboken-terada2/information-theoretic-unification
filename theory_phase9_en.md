# Phase 9: Dynamical spacetime — cosmological evolution from quench dynamics

## 1. Motivation

Phases 1–8 dealt with static spacetime structures. Phase 4 showed that modular flow $\sigma_t^\omega$ functions as a state-dependent time, but the connection with cosmological time (= the time experienced by an expanding universe) was incomplete.

Here we use **quantum quench dynamics** as a minimal model of "post-Big-Bang cosmic evolution":

- "Big Bang" = high-energy initial state (Néel state)
- "Cosmic evolution" = Heisenberg evolution under a free-fermion Hamiltonian
- "Particle horizon" = entanglement light cone (Lieb–Robinson velocity $v_F$)
- "Thermal equilibration" = Calabrese–Cardy entropy saturation = thermal history of the universe

## 2. Quench setup

### 2.1 Initial state (Big Bang)

$$|\psi_0\rangle = c_0^\dagger c_2^\dagger c_4^\dagger \cdots |0\rangle$$

This is the Néel (antiferromagnetic) state. The correlation matrix is $C_{ij}(0) = \delta_{ij}\,\delta_{i \bmod 2, 0}$.

### 2.2 Time evolution

Under the XX Hamiltonian $H = -\sum_i (c_i^\dagger c_{i+1} + \mathrm{h.c.})$:
$$|\psi(t)\rangle = e^{-iHt}|\psi_0\rangle, \qquad C(t) = e^{iht}C(0)e^{-iht},$$
where $h$ is the single-particle hopping matrix.

## 3. Main predictions

### 3.1 Calabrese–Cardy entropy growth (2005)

For an interval $A$ of length $L$, post-quench entanglement growth:
$$S_A(t) \approx \begin{cases} \alpha\, v_F\, t & t < L/(2 v_F) \quad \text{(linear growth phase)}\\ \beta\, L & t > L/(2 v_F) \quad \text{(saturation phase)} \end{cases}$$
where $v_F = 2$ is the Fermi velocity of the XX chain, and $\alpha, \beta$ are constants depending on the effective initial-state temperature.
This is the manifestation of "**ballistic propagation of information**" derived from the Lieb–Robinson 1972 causality bound.

### 3.2 Light-cone structure

The mutual information $I(i, j; t)$ between any two sites:
- $|i - j| > 2 v_F t$: causally disconnected, $I \approx 0$.
- $|i - j| \lesssim 2 v_F t$: finite.

A "light cone" appears in the $|i-j|$ vs. $t$ plane — this is the **causal structure** that was missing from the static spacetimes of Phases 1–8.

### 3.3 Cosmological interpretation

Correspondence between quench-dynamics quantities and FRW cosmology:

| Quench | FRW cosmology |
|---|---|
| Time $t$ | Cosmic age $t$ |
| Light-cone speed $v_F$ | Speed of light $c$ |
| Particle horizon $L_H(t) = v_F t$ | Particle horizon $L_H(t) \sim t$ |
| $H_{\rm eff}(t) \equiv \dot L_H/L_H = 1/t$ | Hubble rate $H \sim 1/t$ (radiation dominated) |
| Linear growth of $S_A(t)$ | Entropy production (away from equilibrium) |
| Saturation of $S_A$ | Thermal equilibrium |
| Néel initial state | Big Bang (low entropy) |

This is a "**quench dynamics of a finite system locally simulates FRW cosmology**" picture (in the spirit of Hayden–Preskill).

### 3.4 Modular thermalisation

Phase 4's Peschel modular Hamiltonian $M_A(t)$ also evolves:
- $t = 0$: Néel initial state → $C_A(0)$ diagonal → $M_A(0)$ a simple diagonal matrix.
- $t \to \infty$: thermalisation → $C_A(\infty)$ close to thermal state → $M_A(\infty)$ converges to the CHM Killing kernel.

Numerical demonstration of "**the specialness of the initial state disappears, and the state moves toward modular equilibrium**".
This is the dynamical version of the Connes–Rovelli thermal-time hypothesis.

## 4. Simulation plan

### Part A: quench dynamics
- $N = 64$, OBC chain, Néel initial state.
- Compute $C(t) = e^{iht}C(0)e^{-iht}$ rapidly via eigendecomposition of $h$.
- 80 time points in $t \in [0, 30]$.

### Part B: Calabrese–Cardy fit
- $S_A(t)$ on the central interval $A = [N/4, 3N/4)$ ($|A| = 32$).
- Slope of the linear regime ($t < L/4$) → $\alpha v_F$.
- Average of saturation values → entropy density.

### Part C: light-cone heatmap
- $I(i_0, j; t)$ from the central site $i_0 = N/2$ to every other site $j$.
- Colour map on the (distance × time) plane.
- Confirm the causal cone $|j - i_0| = 2 v_F t$.

### Part D: effective Hubble parameter
- "Light-cone radius" $L_H(t) \equiv$ max distance with $\{I > $ threshold$\}$.
- $H_{\rm eff}(t) = \dot L_H / L_H$.
- Confirm $L_H(t) \sim t$, $H \sim 1/t$.

### Part E: thermalisation of the modular Hamiltonian
- Compute $M_A(t)$ at $t = 0$, $L/(4 v_F)$, $L/(2 v_F)$.
- Time evolution of the diagonal profile $M_{ii}(t)$.
- See the convergence (as $t \to \infty$) to the CHM kernel $\propto x(L-x)/L$.

## 5. Expected results and limitations

✅ Expected:
- Quantitative confirmation of Calabrese–Cardy linear-then-saturation behaviour
- Vivid light-cone visualisation (= emergent causal structure)
- $L_H \propto t$ confirmation (= minimal "expanding universe" model)

⚠️ Limitations:
- A true FRW cosmology requires **geometric expansion** ($a(t) \sim t^{2/3}$ etc.), which cannot come purely from a Hamiltonian — a time-dependent metric setup is needed.
- Our "expansion" here is **informational expansion** (growth of the causally connected region), not **metric expansion** (stretching of space itself).
- A true dynamical spacetime requires Phase 9+1, working with Witten 2022's type II algebra + crossed product.

Even so, this is a strong demonstration of cosmological time evolution within an information-theoretic framework, as a minimal model.
