# Phase 6: The Page Curve and the Quantum-Information-Theoretic Resolution of the Black-Hole Information Paradox

## 1. The problem

Hawking 1976: a black hole (BH) radiates thermally. As the radiation is emitted the BH evaporates, but the radiation entropy increases monotonically → final state is mixed → **violation of unitarity**.

This is the sharpest contradiction between GR and QM. Can our information-theoretic framework resolve it?

## 2. Page's 1993 prediction

If unitary evolution holds, the von Neumann entropy of the radiation must follow:
- Early evaporation: radiation qubit count $|R| \ll |B|$ → $S_R \approx |R| \log 2$ (thermal-like)
- **Page time $t_P$** ($|R| \approx |B|$): $S_R$ peaks
- Late: $|R| \gg |B|$ → $S_R \approx |B| \log 2$ (BH-side entropy, decreasing)
- Final: BH fully evaporated → $S_R = 0$ (returns to a pure state)

This **inverted-V** is the **Page curve**. Hawking's monotone-increasing curve vs. Page's V-shape — which is right?

## 3. The island formula (2019–2020)

Penington 2019, Almheiri–Engelhardt–Marolf–Maxfield (AEMM) 2020:
$$S_R = \min_{\text{islands } I}\!\left[ \frac{\text{Area}(\partial I)}{4 G_N} + S_{\text{matter}}(R \cup I)\right]$$

Before the Page time: island = empty set → $S_R$ = matter entropy of $R$ (Hawking's answer, increasing).
After the Page time: island = a piece of the BH interior → the competing candidate wins → $S_R$ decreases.

This is the **quantum extension of Phase 2's Ryu–Takayanagi formula** and is a direct consequence of the Phase 1–5 framework.

## 4. Numerical model — Hayden–Preskill style

Model a fully evaporating BH using random unitaries + Bell-pair bookkeeping.

**Setup**:
1. Total system = $|B|$ qubits (BH interior) + $|R|$ qubits (radiation).
2. Initial state = (BH first Bell-paired with reference) → all BH qubits scrambled by a Haar-random unitary → some qubits "emitted" as radiation.
3. At each "time" (= number of qubits emitted), compute $S_R$.

**Page's claim (1993)**: averaged over a high-dimensional Haar ensemble,
$$\langle S_R \rangle \approx \min(|R|, |B|+|N|-|R|) \log 2$$
where $|N|$ is the number of Bell pairs initially connecting BH with reference (in the neutral setup $|N|=0$).

This is exactly the **triangular Page curve**, and its difference from the Hawking curve (monotonically increasing) is the numerical evidence for unitarity.

## 5. Implementation strategy

1. Total system $n_{\text{tot}} = 2k$ qubits (e.g. 12), generate Haar-random pure states $|\psi\rangle$.
2. For each split $|R| = 1, 2, ..., n_{\text{tot}}-1$, compute the reduced state $\rho_R$ and $S_R$.
3. Average over many Haar random samples.
4. Fit the **average curve** to Page and Hawking curves.
5. Result: Page curve holds → information is not lost.

Optionally: keep a small number of qubits as the "BH interior" while bound to a reference via Bell pairs, to mimic a more physical "evaporating BH" setup.

## 6. Significance within ITU

From Phase 5's "bulk = boundary QECC" perspective, the BH interior is holographically decodable on the boundary.
Before the Page time: the BH interior is not in the wedge of the radiation.
After the Page time: a phase transition brings the BH interior into the radiation's wedge → information is recovered.

This is a **dynamical application** of the Phase 1–5 framework, and the BH information paradox is solved as an RT phase transition of the QECC.
