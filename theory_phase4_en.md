# Phase 4: emergence of time — modular flow and the thermal time hypothesis

## 1. Motivation

In Phases 1–3, spatial geometry, the linearised Einstein equation, and the hyperbolic bulk all emerged from information structure. But nowhere does a **time direction** appear. Everything is at an instant ($t=0$ slice).

Connes–Rovelli (1994) "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories" claimed:
> Time is not a classical background but is derived from the quantum state (von Neumann algebra + state) as a modular automorphism.

This is the **thermal time hypothesis**, which we verify numerically in this Phase.

## 2. The essential statement of Tomita–Takesaki modular theory

From a von Neumann algebra $\mathcal{M}$ and a (faithful, normal) state $\omega$, a unique one-parameter family of automorphisms
$$\sigma_t^\omega : \mathcal{M} \to \mathcal{M}, \quad t \in \mathbb{R}$$
is defined (Tomita 1957, Takesaki 1970). This is the **modular flow**.

Concretely: writing $\rho_\omega = e^{-K}/Z$,
$$\sigma_t(O) = e^{i K t}\, O\, e^{-i K t}.$$

Physical interpretation (Bisognano–Wichmann): for the right Rindler wedge in 4D Minkowski vacuum $|\Omega\rangle$, $\sigma_t$ is a Lorentz boost by $2\pi t$:
$$K_{\text{Rindler}} = 2\pi \int_0^\infty x\, T_{00}(x, 0)\, dx \quad \Rightarrow \quad \sigma_t = \text{Boost}(2\pi t).$$

That is, for the Rindler observer, **modular time $t$ = Lorentz boost parameter $\times 1/2\pi$**.

## 3. CHM generalisation (Casini–Huerta–Myers 2011)

For a ball region $A = \{|\vec x| < R\}$, the vacuum modular flow has
$$K_A = 2\pi \int_A \frac{R^2 - |\vec x|^2}{2R}\, T_{00}\, d^{d-1}x.$$

Trajectories of points $\vec x$ under $\sigma_t$ are slow near the boundary $|\vec x|=R$ and fast at the centre. They form a **clock confined to the ball** = a conformal Killing flow.

## 4. Thermal time hypothesis (Connes–Rovelli)

As an automorphism of $\mathcal{M}$, $\sigma_t^\omega$ depends **only on the state $\omega$**. The clock is not an externally placed absolute time; it is determined by the state of what is being observed.

→ A different state $\omega'$ has a different time $\sigma_t^{\omega'}$. This re-reads "the origin of time = the entanglement structure of the state".

## 5. Implementation on a 1D free-fermion chain

From the one-point matrix $M_A = \log[(1-C_A)/C_A]$, the single-particle modular flow is
$$\sigma_t(c_i) = \sum_j [e^{-iM_A t}]_{ij}\, c_j.$$

Verification quantities:
1. **Bisognano–Wichmann half-line**: for $A = [0, \infty)$, $M$ is the boost generator. Eigenmodes are Rindler modes.
2. **CHM interval**: for $A=[0, L)$, the local weight (= diagonal) of $M$ follows $x(L-x)/L$ (verified in Phase 2).
3. **Position-dependent modular velocity**: the immediate spreading rate of a single-site initial state
   $$v(x_0)^2 := \langle x_0 | M_A^2 | x_0 \rangle - \langle x_0 | M_A | x_0 \rangle^2$$
   follows the squared CHM Killing kernel $\propto (R^2 - (x-x_0)^2)^2$.
4. **State dependence of thermal time**: for ground state and thermal state, $M_A^{\text{vac}}$ and $M_A^{\text{therm}}$ differ → different time flows.

These four numerical demonstrations constitute the minimal proof of "time = modular flow of a state".
