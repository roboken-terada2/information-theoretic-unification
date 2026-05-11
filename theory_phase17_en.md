# Phase 17: Nonlinear Einstein equations — entanglement second law and quantum Fisher information

## 1. Motivation

In Phase 2 we derived the linearised Einstein equation $\delta G_{\mu\nu}^{(1)} = 8\pi G_N \delta T_{\mu\nu}$ from the entanglement first law $\delta S = \delta\langle K\rangle$.

But the observationally important phenomena (BH mergers, gravitational waves, cosmological evolution) require the **nonlinear** Einstein equations
$$G_{\mu\nu} = 8\pi G_N T_{\mu\nu}.$$
This Phase provides the numerical foothold for deriving these from an **entanglement second law** — the quadratic expansion of relative entropy.

## 2. Expansion to second order

For any one-parameter family $\rho(\lambda) = \rho^{(0)} + \lambda\,\delta\rho + \tfrac{1}{2}\lambda^2 \delta^2\rho + \cdots$:

### 2.1 First law (Phase 2)
$$\delta S = \delta\langle K\rangle \quad \text{(first order)}$$

### 2.2 Second law (this Phase)
Taylor-expanding the relative entropy:
$$S(\rho_\lambda \| \rho^{(0)}) = \frac{1}{2}\, g_F^{(0)}\, \lambda^2 + O(\lambda^3)$$

where $g_F^{(0)}$ is the **quantum Fisher information** (Bures metric):
$$g_F^{(0)} = \mathrm{Var}(K^{(0)})_{\rho^{(0)}} = \langle (K^{(0)})^2\rangle - \langle K^{(0)}\rangle^2$$
— the **variance of the modular Hamiltonian**.

### 2.3 Casini reformulation
Using $S_{\rm rel} = \delta\langle K\rangle - \delta S$ (Phase 2), the expansion is
$$S_{\rm rel}(\lambda) = \frac{1}{2}\mathrm{Var}(K) \lambda^2 + \frac{1}{6} S_3 \lambda^3 + \cdots$$
where $S_3$ is the third cumulant.

**Key point**: the $\lambda^2$ coefficient is the **Riemannian metric on Hilbert space** and fully determines the bulk nonlinear gravitational structure.

## 3. Bulk dual (Faulkner et al. 2017)

Holographic interpretation:
- $\mathrm{Var}(K_A)$ = integral of the CFT stress-tensor 2-point function $\langle T_{\mu\nu}(x) T_{\rho\sigma}(y)\rangle$
- This corresponds directly to **graviton–graviton interactions in the bulk** (at 3-point level)
- Summing all orders → **complete nonlinear Einstein equation** $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$

$$\boxed{\;\;\text{All-orders entanglement expansion} \;=\; \text{full Einstein equation}\;\;}$$

## 4. Computation on free fermions

For a Gaussian state $\rho^{(0)}$ with $K = \sum_{ij} M_{ij} c_i^\dagger c_j$ (Peschel):

**Mean**: $\langle K\rangle = \mathrm{Tr}(MC)$.

**Variance** (from Wick's theorem):
$$\mathrm{Var}(K) = \sum_{ijkl} M_{ij} M_{kl} C_{il}(\delta_{jk} - C_{kj}) = \mathrm{Tr}(M^2 C) - \mathrm{Tr}(M C M C^T)$$

— this is numerically computable.

## 5. Verification program

1. XX-model ground state $\rho^{(0)}$ on interval $A$
2. From $M_A$, $C_A$, **analytically compute** $\mathrm{Var}(K_A^{\rm vac})$
3. Build a perturbation $\rho(\varepsilon) = e^{-(1+\varepsilon)K_A}/Z(\varepsilon)$ — modular-temperature shift
4. Compute $S_{\rm rel}(\varepsilon)$ at multiple $\varepsilon$
5. Fit power law and confirm $S_{\rm rel}(\varepsilon)/\varepsilon^p$ gives $p = 2$ with coefficient $\tfrac{1}{2}\mathrm{Var}(K_A)$
6. Conclude: "the second-order Einstein correction emerges correctly from information structure"

## 6. Relation to Phase 2

| Phase | Order | Relation | Physics |
|---|---|---|---|
| 2 | 1 | $\delta S = \delta\langle K\rangle$ | Linearised Einstein $\delta G = 8\pi G \delta T$ |
| **17** | **2** | $S_{\rm rel} = \tfrac{1}{2}\mathrm{Var}(K)\lambda^2$ | **Nonlinear Einstein 2nd-order correction** |
| 18+ (TBD) | 3+ | Higher cumulants | Graviton self-interaction all orders |

## 7. Limitations

- The $n\to\infty$ limit of $n$-th order relative entropy is the true nonlinear Einstein equation
- This Phase verifies up to 2nd order numerically
- 3rd order and higher are only partially shown in Faulkner et al. 2017; full proof remains open

Even so, confirming the **second order** is the first significant step beyond the linearised regime.
