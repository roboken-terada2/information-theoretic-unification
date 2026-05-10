# Phase 11: Matter hierarchy — three generations, Yukawa hierarchies, and CKM/PMNS mixing

## 1. Motivation

In Phase 10 we showed that the Standard Model gauge group SU(3)$\times$SU(2)$\times$U(1)$_Y$ emerges as the flavour symmetry of the boundary CFT.
The Standard Model has **three generations** (u/d/e/$\nu_e$, c/s/$\mu$/$\nu_\mu$, t/b/$\tau$/$\nu_\tau$), each with very different masses:

| Particle | Mass (GeV) | Ratio (gen 3 / gen 1) |
|---|---|---|
| u | $2.2 \times 10^{-3}$ | — |
| c | 1.27 | 580 |
| t | 173 | $7.9 \times 10^4$ |
| | | |
| e | $5.1 \times 10^{-4}$ | — |
| $\mu$ | 0.106 | 207 |
| $\tau$ | 1.78 | 3490 |

In addition the **CKM matrix** (quark mixing) and **PMNS matrix** (lepton mixing) describe the quantum superposition between generations. Their origin is unexplained in the Standard Model (~ 20 free parameters).

This Phase reconstructs the **Froggatt–Nielsen 1979** mechanism within ITU and demonstrates the appearance of generation hierarchy and mixing matrices numerically.

## 2. The Froggatt–Nielsen mechanism

### 2.1 A new U(1)$_F$ flavour symmetry

Postulate an additional global U(1)$_F$ symmetry on the SM. Each fermion has an integer charge $q$:

| Generation | $Q_L$ | $u_R$ | $d_R$ | $L_L$ | $e_R$ |
|---|---|---|---|---|---|
| 1 | $q^Q_1$ | $q^u_1$ | $q^d_1$ | $q^L_1$ | $q^e_1$ |
| 2 | $q^Q_2$ | $q^u_2$ | $q^d_2$ | $q^L_2$ | $q^e_2$ |
| 3 | $q^Q_3$ | $q^u_3$ | $q^d_3$ | $q^L_3$ | $q^e_3$ |

The Higgs $H$ has charge 0. For the Yukawa $\bar Q_L^i Y^u_{ij} u_R^j H$ to be U(1)$_F$ invariant, the coupling would have to vanish (charge conservation forbids it).

### 2.2 The flavon

As source of the breaking, introduce a **flavon** $\Phi$ of charge $-1$. $\Phi$ acquires a vacuum expectation value $\langle\Phi\rangle = \epsilon \Lambda$ ($\epsilon \ll 1$), breaking U(1)$_F$.

The Yukawa coupling then appears as:
$$Y^u_{ij} \sim c_{ij} \left(\frac{\langle\Phi\rangle}{\Lambda}\right)^{q^Q_i + q^u_j} = c_{ij}\, \epsilon^{q^Q_i + q^u_j}$$
with $c_{ij} = O(1)$.

### 2.3 Emergence of hierarchy

Singular-value-decomposing the mass matrix $M^u = v \cdot Y^u$ ($v$ the Higgs VEV), the singular values (= masses) are determined by the diagonal pairs $q^Q_i + q^u_i$:
$$m_i \sim v\, \epsilon^{q^Q_i + q^u_i}$$

With $q^Q = (3,2,0)$, $q^u = (3,2,0)$, $\epsilon = 0.22$ (Cabibbo angle):
- $m_u \sim v \epsilon^6 \approx v \cdot 1.1 \times 10^{-4}$
- $m_c \sim v \epsilon^4 \approx v \cdot 2.3 \times 10^{-3}$
- $m_t \sim v \epsilon^0 = v$

Compared with experiment ($v = 246$ GeV):
- Prediction: $m_u : m_c : m_t \approx 1.1 \times 10^{-4} : 2.3 \times 10^{-3} : 1$
- Experiment: $9 \times 10^{-6} : 5.2 \times 10^{-3} : 0.70$ → orders of magnitude match.

### 2.4 Mixing matrix

The CKM matrix is the product of left-rotation matrices for up-type and down-type:
$$V_{\rm CKM} = U^u_L\, (U^d_L)^\dagger$$

In FN textures:
$$V^{ij}_{\rm CKM} \sim \epsilon^{|q^Q_i - q^Q_j|}$$

For $q^Q = (3, 2, 0)$:
- $V_{us} \sim \epsilon^1 \approx 0.22$ (experiment 0.226 ✓)
- $V_{cb} \sim \epsilon^2 \approx 0.048$ (experiment 0.041 ✓)
- $V_{ub} \sim \epsilon^3 \approx 0.011$ (experiment 0.004)

Order-of-magnitude agreement.

## 3. Lepton hierarchy and PMNS matrix

The same applies to leptons, except neutrino masses come from the see-saw mechanism: $m_\nu \sim v^2/M_R$ ($M_R$ = right-handed neutrino mass).
The PMNS matrix has **large mixing angles** ($\theta_{12} \approx 33°$, $\theta_{23} \approx 49°$), unlike CKM.

This is interpretable as "**neutrinos are anarchic** (FN charges nearly equal)".
With lepton FN charges e.g. $q^L = (0,0,0)$, $q^e = (3,2,0)$:
- $m_e : m_\mu : m_\tau \sim \epsilon^3 : \epsilon^2 : 1$ (charged-lepton hierarchy)
- Neutrino Majorana mass $m^\nu_{ij} \sim \epsilon^{q^L_i + q^L_j} = \epsilon^0 = 1$ → all entries $O(1)$ → large mixing.

This naturally explains the contrast between large PMNS and small CKM mixing.

## 4. Position within ITU

As shown in Phase 10, gauge groups $G$ appear as flavour symmetries of the boundary CFT.
This Phase claims:

> **U(1)$_F$ is also a global U(1) symmetry of the boundary CFT, sitting in the same framework as the U(1)$_Y$ of Phase 10.**
> **Its hierarchical spontaneous breaking (the flavon VEV) generates the matter mass hierarchy and the mixing matrices.**

So with no extra physical assumptions, the FN mechanism operates within the Phase-10 framework. The number of generations (= 3) is a separate question (Phase 12+), but **given that the generations exist, the mass hierarchy and mixing structure are determined by the U(1)$_F$ charge assignment** — the content this Phase demonstrates.

## 5. Simulation plan

### Part A: construction of Yukawa matrices
- $\epsilon = 0.22$ (Cabibbo)
- Charge assignment: $q^Q = (3, 2, 0)$, $q^u = (3, 2, 0)$, $q^d = (3, 2, 2)$ (typical)
- $Y^u_{ij} = c_{ij}\, \epsilon^{q^Q_i + q^u_j}$, $c_{ij}$ Haar-like O(1) random.

### Part B: SVD for masses and mixing
- $Y^u = U^u_L \Sigma^u U^{u\dagger}_R$, $Y^d = U^d_L \Sigma^d U^{d\dagger}_R$
- Singular values = masses (modulo signs)
- CKM $V = U^u_L (U^d_L)^\dagger$

### Part C: comparison with experiment
- Compare with PDG 2024 masses and CKM values
- Verify order-of-magnitude agreement

### Part D: lepton sector
- Reproduce the charged-lepton (e, $\mu$, $\tau$) hierarchy
- Show that neutrino anarchy → naturally gives large PMNS angles

### Part E: statistical ensemble
- Average over 1000 samples of the random $c_{ij}$
- Compare median and variance of mass ratios with experiment
