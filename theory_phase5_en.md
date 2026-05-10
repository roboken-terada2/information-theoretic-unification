# Phase 5: Holographic Quantum Error Correction and emergent bulk

## 1. Motivation

In Phases 1–4 spatial geometry, gravity, the hyperbolic bulk, and time-as-modular-flow all emerged from information structure. The final piece is the discovery that **the tensor-network representation of the bulk functions as a quantum error-correcting code (QECC) on the boundary CFT** (Almheiri–Dong–Harlow 2014).

This is the deepest quantum-information interpretation of AdS/CFT:
> Spacetime ≅ redundant encoding of a quantum state ≅ error-correcting code.

## 2. Sketch of the ADH theorem

In AdS/CFT, a bulk field $\phi(x)$ inside the entanglement wedge $\mathcal{E}_A$ of a boundary region $A$ can be **reconstructed as a boundary operator on $A$**:
$$\phi_{\text{bulk}}(x) \cong \mathcal{O}_A \in \text{Algebra}(A) \quad \text{if } x \in \mathcal{E}_A.$$

The redundancy that lets a single bulk operator be reconstructed from different boundary regions is exactly the defining feature of a QECC's logical operators.

**Petz recovery map**: an explicit quantum operation that recovers the original bulk state from the boundary state $\rho_A$ after errors.

## 3. The [[5,1,3]] perfect-tensor code

As the minimal model of holography we use the 5-qubit perfect code:
- 5 physical qubits = boundary points
- 1 logical qubit = a single bulk point
- Distance 3 = corrects any single-qubit error

Stabiliser generators:
$$g_1 = X Z Z X I,\quad g_2 = I X Z Z X,\quad g_3 = X I X Z Z,\quad g_4 = Z X I X Z.$$
Logical operators: $\bar X = X^{\otimes 5}, \bar Z = Z^{\otimes 5}$.

**Perfect-tensor property**: the 5-leg tensor $T_{ijklm}$ is an isometry under any 2-vs-3 bipartition. Consequently, any 2-qubit reduced state is maximally mixed $I/4$.

## 4. Emergent RT phase transition

Bell-pair the logical qubit with a reference $R$, then encode via [[5,1,3]]:
$$|\Phi\rangle_{LR} = \frac{1}{\sqrt 2}(|0\rangle_L|0\rangle_R + |1\rangle_L|1\rangle_R) \xrightarrow{\text{encode}} |\tilde\Phi\rangle = \frac{1}{\sqrt 2}(|\bar 0\rangle|0\rangle_R + |\bar 1\rangle|1\rangle_R).$$

For any boundary subset $A \subset \{1,...,5\}$, compute the mutual information:
$$I(A : R) = S(A) + S(R) - S(AR).$$

**Claim (= the numerical version of ADH)**:
$$I(A:R) = \begin{cases} 0 & \text{if } |A| \leq 2 \\ 2\log 2 & \text{if } |A| \geq 3. \end{cases}$$

This is the **discrete RT phase transition**: the bulk qubit lies in the entanglement wedge of "the larger half" of the boundary.
- $|A| \geq 3$ → bulk is in $A$'s wedge → decodable from $A$, correlated with $R$.
- $|A| \leq 2$ → bulk is in $A^c$'s wedge → no information on $A$, $I(A:R)=0$.

## 5. Existence of a Petz recovery map

Distance 3 ⇒ any 2-qubit error is detectable from the syndrome (or any 1-qubit error is correctable). Possessing only 3 qubits, one can fully recover the logical via the Petz map:
$$\mathcal{R}_A^{\sigma} \circ \mathcal{N}_{A^c}(\rho_L) = \rho_L \quad (|A| \geq 3).$$

Equivalently: **bulk operators $\bar X, \bar Z$ admit representations as operators on any 3-qubit subset.**

## 6. The big picture (link to ITU)

| Phase | What emerges | Encoding principle |
|---|---|---|
| 1 | Space ($S^1$) | mutual information = distance |
| 2 | Linearised Einstein | entanglement first law |
| 3 | Hyperbolic bulk (AdS$_3$) | MERA hierarchy = hyperbolic tiling |
| 4 | Time | modular flow $\sigma_t^\omega$ |
| 5 | **Bulk locality** | **boundary QECC redundancy** |

In the end, Phase 5 asserts:
> "Each spacetime point is implemented as a logical operator of the boundary quantum state."

This is the ultimate identification the **It from Qubit** programme aims for, and it **unifies** the emergent phenomena seen individually in Phases 1–4.

## 7. Simulation plan

1. Construct codewords $|\bar 0\rangle, |\bar 1\rangle$ for [[5,1,3]] (32-dimensional Hilbert space).
2. Build the logical-reference Bell pair $|\tilde\Phi\rangle$ on a 6-qubit system.
3. For all $2^5 = 32$ boundary subsets $A$, compute $I(A:R)$ and $S(A)$.
4. Confirm the **complete step function**: $I=0$ for $|A| \leq 2$, $I=2$ bits for $|A| \geq 3$.
5. Check perfect-tensor property: $S(A) = \min(|A|, 5-|A|) \log 2$ on the codeword.
6. Pentagonal geometric visualisation (bulk centre, 5 boundary vertices, entanglement wedges).
