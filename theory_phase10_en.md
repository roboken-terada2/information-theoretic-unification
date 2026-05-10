# Phase 10: Emergence of matter fields — the Standard Model gauge group SU(3)×SU(2)×U(1)_Y

## 1. Motivation

Through Phases 1–9 we have derived spacetime, gravity, time, and cosmological evolution from quantum information structure. The remaining major task is the **emergence of matter (elementary particles)** — where do the gauge groups of the Standard Model come from?

Central idea (Maldacena–Witten 1998 [hep-th/9803131]):
> **Any global symmetry $G$ of a boundary CFT is dual to a bulk gauge group $G$.**

The boundary's conserved currents $J^\mu_a$ ($a$ a group index) are in 1-to-1 correspondence with bulk gauge fields $A^\mu_a$.

The aim here is therefore: **construct, within the information-theoretic framework, a boundary CFT whose global symmetry is the Standard Model gauge group**.

## 2. Six-flavour free fermion = the left-handed quark doublet QL

In the Standard Model, the left-handed quark doublet QL transforms as $(3, 2, 1/6)$:
- SU(3)$_c$ **triplet** (3 colours: r, g, b)
- SU(2)$_L$ **doublet** (up-type u, down-type d)
- U(1)$_Y$ **hypercharge** $Y = 1/6$

Total internal degrees of freedom $3 \times 2 = 6$. We implement this as a **six-flavour free fermion**:

$$H = -\sum_{i,\alpha} (c_{i,\alpha}^\dagger c_{i+1,\alpha} + \mathrm{h.c.}), \quad \alpha = (\text{colour}, \text{isospin}) \in \{1,...,6\}.$$

## 3. Construction of the gauge generators

On the 6-dimensional flavour space = 3 colours $\otimes$ 2 isospin, the SM generators are:

### 3.1 SU(3)$_c$ (8 of them)

Using Gell-Mann matrices $\lambda^A$ ($A = 1,...,8$, $\mathrm{Tr}\,\lambda^A \lambda^B = 2\delta^{AB}$):
$$T^A_{\rm color} = \frac{\lambda^A}{2} \otimes \mathbb{1}_2, \quad A = 1,...,8.$$

### 3.2 SU(2)$_L$ (3 of them)

Using Pauli matrices $\sigma^a$ ($a = 1, 2, 3$):
$$T^a_{\rm weak} = \mathbb{1}_3 \otimes \frac{\sigma^a}{2}, \quad a = 1, 2, 3.$$

### 3.3 U(1)$_Y$ (1 of them)

Hypercharge:
$$T^Y = \frac{1}{6} \mathbb{1}_6.$$

A total of $8 + 3 + 1 = 12$ generators. They span the 12-dimensional Lie algebra $\mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)$.

### 3.4 Trace normalisation

With normalisation $\mathrm{Tr}(T^A T^B) = \delta_{AB}$ within each group and 0 between groups:

| | SU(3) | SU(2) | U(1)$_Y$ |
|---|---|---|---|
| SU(3) | $\delta_{AB}$ | 0 | 0 |
| SU(2) | 0 | $\delta_{ab}$ | 0 |
| U(1)$_Y$ | 0 | 0 | $1/6$ |

This is the matrix realisation of "**the SM gauge group is block-diagonal**".

## 4. Conserved currents and 2-point functions

Lattice SU(N) current density:
$$J^A(i) = \sum_{\alpha,\beta} (T^A)_{\alpha\beta}\, c_{i,\alpha}^\dagger c_{i,\beta}.$$

For SU generators with $\mathrm{Tr}\,T^A = 0$, $\langle J^A(i)\rangle = 0$ in the vacuum.

By Wick's theorem the connected 2-point function is:
$$\langle J^A(x) J^B(0)\rangle_c = -\mathrm{Tr}(T^A T^B) \cdot |c_{x0}|^2$$
where $c_{x0} = \langle c_x^\dagger c_0\rangle$ is the single-flavour 2-point function (equal across flavours by flavour symmetry).

### 4.1 Verifiable structure

(a) **Group block diagonality**:
$$\langle J^A_{\rm color}(x) J^a_{\rm weak}(0)\rangle_c = 0$$
SU(3) and SU(2) cross terms vanish exactly — numerical evidence that the two groups act independently.

(b) **CFT scaling** (Calabrese–Cardy):
For a 1+1D free fermion, $|c_{x0}|^2 \sim 1/(\pi^2 x^2)$ at large $|x|$. Thus
$$\langle J^A(x) J^A(0)\rangle_c \sim -\frac{1}{\pi^2 x^2}.$$
This is the CFT prediction for **SU(N) currents at Kac–Moody level $k = 1$** (Knizhnik–Zamolodchikov 1984; Affleck 1989).

(c) **Current conservation**: $\partial_\mu J^\mu_a = 0$ is automatic from symmetry.

## 5. AdS/CFT bulk-dual connection

Maldacena–Witten 1998 in our setting:
> The boundary CFT$_2$ (= 1+1D, our chain) having global symmetry SU(3)$\times$SU(2)$\times$U(1)$_Y$ ⇔ the bulk AdS$_3$ contains corresponding gauge fields $A^{\mu(c)}_A, A^{\mu(w)}_a, A^{\mu(Y)}$.

Geometric picture of matter and gauge fields:
- Boundary current $J^A$ → bulk-propagating gauge field $A^A$
- Current 2-point function → Witten-diagram propagator with both ends on the boundary
- Chiral anomaly → Chern–Simons term in the bulk

In this way the **Standard-Model gauge fields (photon, W/Z, gluons) appear as bulk geometric structures**.

## 6. Simulation plan

### Part A: construction of generators
- Build the 6×6 matrices $T^A_{\rm color}, T^a_{\rm weak}, T^Y$.
- Compute the trace matrix $\mathrm{Tr}(T^A T^B)$.
- Numerically verify block diagonality.

### Part B: single-flavour 2-point function
- $N = 64$ site 1D chain, half filling.
- Compute $c_{ij}$ (= XX-model ground-state correlation).

### Part C: 2-point functions of all 12 currents
- All 144 combinations $\langle J^A(x) J^B(0)\rangle$.
- In matrix form: $-\mathrm{Tr}(T^A T^B) \times |c_{x0}|^2$.

### Part D: CFT scaling check
- Plot $\log|\langle J^A J^B\rangle|$ vs $\log x$.
- Confirm slope $\approx -2$ (CFT prediction).
- Extract Kac–Moody level $k$.

### Part E: visualisation of block diagonality
- 12×12 heatmap of $\mathrm{Tr}(T^A T^B)$.
- 12×12 heatmap of $\langle J^A J^B\rangle$ at fixed distance.
- Confirm both have the same block structure.

## 7. What this Phase shows

- The Standard Model gauge group structure SU(3)×SU(2)×U(1) **emerges naturally as the flavour symmetry of a boundary CFT**.
- The currents of each group are conserved independently and uncorrelated with each other (= group-theoretic block diagonality).
- The bulk dual contains 12 gauge fields — analogous to photons + W/Z + gluons in a 4D internal structure.
- Why our universe has SU(3)×SU(2)×U(1) is **not explained** (the origin of flavour count $N=6$ is a separate question), but **the framework naturally accommodates the Standard Model**.

## 8. Limitations and future tasks

⚠️ What this Phase does **not** show:
- Why there are "3 generations" (this is separate physics)
- The mass hierarchy ($m_e \ll m_t$) origin
- The Higgs mechanism (= dynamical SU(2) breaking)
- Chirality (only left-handed fermions in weak interaction)

These are addressed in **Phases 11+ on emergence of matter detail**.
