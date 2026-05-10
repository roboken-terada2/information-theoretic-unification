# Information-Theoretic Unification: emergence of spacetime (Phase 1)

## 1. Problem setup

General Relativity (GR) presupposes a continuous spacetime manifold $(\mathcal{M}, g_{\mu\nu})$.
Quantum Mechanics (QM) presupposes unitary evolution on a Hilbert space $\mathcal{H}$.
To unify the two, one of these must be derived from the other.

**Information-theoretic unification hypothesis**: spacetime, metric, and dimension emerge from the **entanglement structure** of a quantum state in Hilbert space.

## 2. Lineage of existing research

| Year | Author | Claim |
|---|---|---|
| 1995 | Jacobson [1] | Einstein's equations follow from $T dS = \delta Q$ (thermodynamic GR) |
| 2006 | Ryu–Takayanagi | $S_A = \mathrm{Area}(\gamma_A)/(4 G_N)$ (area = entropy in AdS/CFT) |
| 2010 | Van Raamsdonk | "Building up spacetime with quantum entanglement" — cutting entanglement separates spacetime |
| 2011 | Verlinde | Entropic gravity |
| 2012 | Swingle | MERA tensor network = discrete AdS |
| 2013 | Maldacena–Susskind | ER = EPR (wormholes = entanglement) |
| 2017 | Cao–Carroll–Michalakis | "Space from Hilbert Space" — extracting distance and dimension from mutual information |
| 2020s | "It from Qubit" collaboration | Spacetime as a quantum error-correcting code |

## 3. Central idea (what this simulation implements)

### 3.1 Axioms

- **Axiom I**: the universe is described by a pure state $|\Psi\rangle \in \mathcal{H}$.
- **Axiom II**: there is a chosen factorisation $\mathcal{H} = \bigotimes_{i=1}^{N} \mathcal{H}_i$. Each factor is a "primitive information cell" (qubit/qudit/fermion mode).
- **Axiom III**: spatial structure (proximity, distance, dimension) is determined entirely by the induced entanglement distribution on $|\Psi\rangle$.

### 3.2 Construction of distance (information metric)

For arbitrary subsystems $A, B$, define the mutual information

$$I(A:B) = S(A) + S(B) - S(A \cup B), \quad S(X) = -\mathrm{Tr}\,\rho_X \log \rho_X.$$

$I \geq 0$, and $I = 0 \iff \rho_{AB} = \rho_A \otimes \rho_B$ (product state).

**Correlation bound theorem (Wolf–Verstraete–Hastings–Cirac 2008)**: for any operators $\mathcal{O}_A, \mathcal{O}_B$,
$$\frac{|\langle \mathcal{O}_A \mathcal{O}_B\rangle - \langle \mathcal{O}_A\rangle\langle \mathcal{O}_B\rangle|^2}{2\|\mathcal{O}_A\|^2 \|\mathcal{O}_B\|^2} \leq I(A:B).$$

Thus $I(A:B)$ is the universal scale that **bounds every physical correlation**. We adopt it as the unique candidate for "physical proximity":

$$d(A,B) := -\log\!\left(\frac{I(A:B)}{I_{\max}}\right), \quad I_{\max} = 2\min(S(A), S(B)).$$

### 3.3 Emergent geometry (embedding via MDS)

Diagonalising the doubly centred distance matrix $D_{ij} = d(i,j)^2$, $B = -\tfrac{1}{2} J D J$ ($J = I - \tfrac{1}{N}\mathbf{1}\mathbf{1}^\top$), the eigenvalue staircase $\{\lambda_k\}$ gives the **emergent dimension**:
- The top $d$ eigenvalues dominate → expressible as a $d$-dimensional manifold.
- Eigenvalues uniform → not geometrically interpretable (high-dimensional / fractal state).

## 4. Verifiable predictions (what this simulation demonstrates)

### Prediction A (CFT scaling)
For a 1D critical system with central charge $c$, Calabrese–Cardy gives
$$S_A(\ell) = \frac{c}{3} \log\!\left[\frac{N}{\pi}\sin\frac{\pi\ell}{N}\right] + \text{const}.$$
For the XX model (free fermion at half filling) $c = 1$.

### Prediction B (recovery of 1D spacetime)
For the XX-chain ground state, $d_{ij}$ should give MDS with 1–2 dominant eigenvalues, and points lie on a **circle** (PBC: even the topology is reproduced).

### Prediction C (contrast with non-geometric states)
For random Gaussian states the MDS eigenvalue spectrum flattens and low-dimensional embedding fails. "States whose information structure is non-geographical have no spacetime."

### Prediction D (power-law decay of mutual information)
For critical chains, $I(i:j) \sim |i-j|^{-2K}$ ($K=1$ for free fermion at half filling).
This is the discrete analog of "light-cone relics" in relativity, and is the starting point for taking the continuum limit of $g_{\mu\nu}$.

## 5. Scope and limitations

✅ Demonstrable:
- A 1-dimensional metric, dimension, and the precursor of the continuum limit are **numerically** recovered from the entanglement distribution alone.
- A clear contrast between "states without spacetime" and "states with spacetime".

⚠️ Not demonstrable (future tasks):
- The dynamical part of Einstein's equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ (the Jacobson 1995 argument needs to be merged in).
- Generalisation to a 4-dimensional Lorentzian manifold (the time direction must be derived from modular flow / Tomita–Takesaki).
- Dynamical spacetime evolution equations (Lloyd's computational notion of time / Page curve).

In other words, this simulation proves the one-way "**information → space** (static metric)" direction in the minimal model. A complete unification including the gravitational field equation requires geometrising the modular Hamiltonian, a separate step.
