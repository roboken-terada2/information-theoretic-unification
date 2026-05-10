# Phase 2: Entanglement First Law and Linearised Einstein Equations

## 1. Modular Hamiltonian

Writing $\rho_A = e^{-K_A}/Z_A$, the operator $K_A = -\log\rho_A$ is the **modular Hamiltonian**. It plays the role of the "thermodynamic energy as seen from subsystem $A$".

**Important fact 1 (Bisognano–Wichmann)**: in 1+1D CFT vacuum with half-line $A = (0,\infty)$,
$$K_A = 2\pi \int_0^\infty x\, T_{00}(x)\, dx.$$
$K_A$ is **local** and equals $2\pi$ times the Rindler observer's Hamiltonian.

**Important fact 2 (Casini–Huerta–Myers 2011)**: in $d$-dimensional CFT vacuum with a ball region $A$ (radius $R$, centre $\vec x_0$):
$$K_A = 2\pi \int_A \frac{R^2 - |\vec x - \vec x_0|^2}{2R}\, T_{00}(\vec x)\, d^{d-1}x.$$
This is also local, weighted by a conformal Killing vector.

**Important fact 3 (Peschel 2003)**: for a free fermion (Gaussian) state,
$$K_A = \sum_{i,j \in A} M_{ij}\, c_i^\dagger c_j, \qquad M_A = \log\!\left(\frac{1 - C_A}{C_A}\right),$$
where $C_A$ is the two-point correlator restricted to $A$. $K_A$ is purely quadratic.

## 2. Entanglement first law

For any one-parameter family $\rho(\lambda) = \rho^{(0)} + \lambda\,\delta\rho + O(\lambda^2)$ (with $\mathrm{Tr}\,\delta\rho = 0$), the first-order variation of the von Neumann entropy is
$$\delta S(A) = -\mathrm{Tr}[\delta\rho_A \log\rho_A^{(0)}] = \mathrm{Tr}[\delta\rho_A K_A^{(0)}] = \delta\langle K_A^{(0)} \rangle.$$

This is the **entanglement version of the first law of thermodynamics**:
$$\boxed{\delta S_A = \delta \langle K_A \rangle}$$

If $K_A$ is the Hamiltonian of a Rindler observer at inverse temperature $1/2\pi$, this is just Clausius' law $\delta Q = T\, \delta S$.

## 3. Derivation of linearised Einstein equations (FGHMR 2014)

In holography (AdS/CFT), Ryu–Takayanagi gives
$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}.$$

Perturbing both sides:
$$\underbrace{\delta S_A}_{\text{quantum info}} = \underbrace{\frac{\delta \text{Area}(\gamma_A)}{4 G_N}}_{\text{geometry}}.$$

Combining with the first law $\delta S_A = \delta\langle K_A\rangle$ and the CHM form for ball regions:
$$\frac{\delta \text{Area}(\gamma_A)}{4 G_N} = 2\pi \int_A \frac{R^2 - r^2}{2R}\, \delta\langle T_{00}\rangle\, d^{d-1}x.$$

**The FGHMR result**: this equation holding for **all ball regions $A$** is equivalent to the linearised Einstein equation in the bulk
$$\delta G_{\mu\nu}^{(1)} = 8\pi G_N\, \delta T_{\mu\nu}$$
in the AdS vacuum vicinity.

That is, "first law + RT formula" ⇔ "linearised Einstein equations".

## 4. Brown–Henneaux relation (CFT parameters → gravity parameters)

For a 1+1D CFT with central charge $c$ and AdS$_3$ radius $R_{\rm AdS}$, Newton constant $G_N$:
$$c = \frac{3 R_{\rm AdS}}{2 G_N} \iff \frac{R_{\rm AdS}}{G_N} = \frac{2c}{3}.$$

The XX model has $c \approx 1$ (verified numerically in Phase 1) → emergent AdS$_3$ with $R/G = 2/3$.
This determines the entanglement entropy as $1/(4 G_N)$ times a geodesic length in the emergent hyperbolic geometry.

## 5. Simulation strategy

1. Adopt the free-fermion ground state $\rho^{(0)}$ (XX model) as the "vacuum".
2. Compute the matrix $M$ in $K_A^{(0)} = \sum M_{ij} c_i^\dagger c_j$ via Peschel.
3. As perturbation, use a finite-temperature thermal state $\rho(T)$:
   $C_{ij}(T) = \sum_k U_{ik}\, n_F(\epsilon_k/T)\, U_{jk}^*$.
4. For each $T$:
   - $\delta S_A(T) = S(\rho_A(T)) - S(\rho_A^{(0)})$ computed directly.
   - $\delta\langle K_A\rangle(T) = \mathrm{Tr}_A[M_A \cdot (C_A(T) - C_A^{(0)})]$.
5. Plot both, confirm exact agreement at $T \to 0$ (first order) and quadratic deviation $O(T^2)$ at finite $T$ (higher-order $\delta\rho^2$ corrections).

This is a verification of the linearised Einstein equations (combined with the Phase-1 RT relation), giving numerical evidence that **the gravitational field equations are a consequence of quantum-information laws**.
