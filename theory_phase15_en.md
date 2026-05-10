# Phase 15: Chirality — quantum anomalies and the Atiyah–Singer index theorem

## 1. Motivation

Non-trivial features of the Standard Model:
- Only **left-handed fermions** participate in SU(2)$_L$ weak interactions (Wu's experiment, 1956)
- Chirality ↔ the two 2-dimensional representations of $SL(2,\mathbb{C})$, the cover of the Lorentz group (left- and right-handed)
- The weak interaction **violates parity (P)**

Questions:
- Why only left-handed?
- Is it conserved at the quantum level? → **Quantum anomalies**
- Why is the SM consistent (= anomaly-free)?

**Key theorem (Atiyah–Singer 1963)**: the index of the Dirac operator $D$, $\mathrm{ind}\, D = \dim \ker D_+ - \dim \ker D_-$, is a topological invariant computable from topological data of the manifold:
$$\mathrm{ind}\, D = \int_M \hat{A}(M) \cdot \mathrm{ch}(F)$$

This is the strong claim "the number of chiral zero modes is a topological invariant", grounding the chiral structure of the Standard Model.

## 2. Quantum anomalies

### 2.1 Quantum breaking of classical symmetries

The chiral symmetry $\psi \to e^{i\alpha\gamma_5}\psi$ classically conserves the level equation:
$$\partial_\mu J^\mu_5 = 0 \quad (\text{classical})$$

But upon quantisation, Adler–Bell–Jackiw (1969):
$$\partial_\mu J^\mu_5 = \frac{e^2}{16\pi^2} F_{\mu\nu} \tilde F^{\mu\nu} \quad (\text{quantum})$$

This is the **chiral anomaly** or **ABJ anomaly**.

### 2.2 Anomaly freedom of the Standard Model

The fermion content of the Standard Model is carefully tuned so that **all anomalies cancel within each generation**:
$$\sum_{\rm gen} (Q_e + 3 Q_q + 0 + ...) = 0$$

This makes the gauge theory consistent. Why nature chooses this combination is a hint toward Grand Unified Theories (GUT).

## 3. The Su–Schrieffer–Heeger (SSH) model

A minimal model implementing chirality and the index theorem (Su, Schrieffer, Heeger 1979 — polyacetylene).

### 3.1 Hamiltonian

A 1D diatomic chain:
$$H = \sum_{i} \big(t_1\, c_{i,A}^\dagger c_{i,B} + t_2\, c_{i,B}^\dagger c_{i+1,A}\big) + \mathrm{h.c.}$$

- Unit cell $i$ contains A and B sublattice sites
- $t_1$: intracell hopping (A→B)
- $t_2$: intercell hopping (B → next A)

### 3.2 Chiral (sublattice) symmetry

For the sublattice operator $\Gamma = \sigma_z$ (+1 on A, -1 on B):
$$\Gamma H \Gamma^{-1} = -H$$

So the spectrum of $H$ has $\pm E$ pair symmetry. Zero modes ($E=0$) are **self-conjugate under chirality** and are localised entirely on one of A, B.

### 3.3 Bulk Bloch Hamiltonian and winding number

Fourier transforming on PBC:
$$H(k) = \begin{pmatrix} 0 & h(k) \\ h(k)^* & 0 \end{pmatrix}, \quad h(k) = -t_1 - t_2 e^{-ik}$$

Energy: $\epsilon_\pm(k) = \pm |h(k)|$.
Bulk gap: $\Delta_{\rm bulk} = 2|t_1 - t_2|$.

Winding number:
$$\nu = \frac{1}{2\pi} \oint dk\, \partial_k\, \arg h(k) = \begin{cases} 0 & |t_1| > |t_2|\;\;\text{(trivial)}\\ 1 & |t_1| < |t_2|\;\;\text{(topological)} \end{cases}$$

### 3.4 SSH version of the Atiyah–Singer theorem

**Claim**: with OBC the number of zero modes of $H$ is **2 × |ν|** (= one at each end).

Trivial phase ($\nu=0$): no zero modes, full gap.
Topological phase ($\nu=1$): **two zero modes** (at left and right ends, sublattice-polarised).

This is the minimal example of the Atiyah–Singer index theorem:
$$\#\{\text{zero modes}\} = \mathrm{ind}\, D = 2\nu$$

## 4. Structure of zero modes

In the topological phase $|t_1| < |t_2|$:
- **Left-edge zero mode**: polarised on the A sublattice only, decaying as $\propto (-t_1/t_2)^n$
- **Right-edge zero mode**: polarised on the B sublattice only, symmetric

These are "**chiral** zero modes" — localised on a single sublattice they have eigenvalues $\pm 1$ under the sublattice symmetry.

Physical meaning: "**a chiral degree of freedom appears at the edge**" — the minimal lattice implementation of Standard Model's chiral structure.

## 5. The Nielsen–Ninomiya theorem and the doubler problem

Nielsen, Ninomiya (1981):
> A **single Weyl fermion** cannot be realised on a regular lattice. Every lattice fermion has a doubler partner of opposite chirality, so left- and right-handed always come in pairs.

This places the strong constraint that "**the continuum limit of a regular lattice is necessarily non-chiral**".
Methods needed to lattice-discretise the SM:
- **Domain-wall fermions** (Kaplan 1992): extract chiral edge modes from a higher-dim bulk
- **Overlap fermions** (Neuberger 1998): use an appropriate sign function
- **Wilson fermions**: lift the doublers with a mass term

In all of these, the **Atiyah–Singer index theorem** plays a central role.

## 6. Position within ITU

In Phase 10 we showed the SM gauge group SU(3)×SU(2)×U(1), in Phase 11 the matter hierarchy, in Phase 12 EWSB. Phase 15 deals with the **chiral** part of this structure:

> The Standard Model's chirality is implemented as a chiral sublattice symmetry of the boundary CFT (one of Phase 10's flavour symmetries) together with its topological invariant (the Atiyah–Singer index).

This puts together:
- Phase 10: gauge groups
- Phase 11: mass hierarchy
- Phase 12: symmetry breaking
- **Phase 15: chirality + anomalies + index theorem**

four facets through which the Standard Model's structure is information-theoretically positioned.

## 7. Simulation plan

### Part A: SSH phase diagram
- Build the Hamiltonian for $t_1 \in [0, 2]$ (with $t_2 = 1$)
- Compute the spectrum
- Confirm bulk-gap closure at $t_1 = 1$

### Part B: winding-number computation
- Total winding of the angle of $h(k)$ in the bulk Bloch Hamiltonian $H(k)$
- Distinguish trivial and topological phases

### Part C: visualisation of zero modes
- For $t_1 = 0.5, t_2 = 1$ (topological), eigenstates with OBC
- Extract the two zero modes
- Show their sublattice polarisation (only A, or only B)
- Confirm exponential decay from the edges

### Part D: Atiyah–Singer verification
- For various $(t_1, t_2)$, compare # zero modes to the winding $\nu$
- Numerically verify $\#\{\text{zero modes}\} = 2|\nu|$

### Part E: spectral flow (anomaly)
- Slowly vary $t_1$ from $1.5 \to 0.5$
- Track eigenvalues that flow from the bulk to zero
- This is the dynamical version of the Atiyah–Singer index

## 8. What this Phase shows

✅:
- Minimal model of chiral (sublattice) symmetry
- Topological invariant = number of zero modes (Atiyah–Singer)
- Lattice implementation of Standard Model chirality

⚠️:
- The actual computation of SM anomaly cancellation (= evaluation of the triangle anomaly diagram)
- 4D gravitational anomalies (= coupling to the gravitational field)
- Refinement of chiral supersymmetry

These are addressed in Phase 16+ or in field-theory textbooks.
