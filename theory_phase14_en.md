# Phase 14: Rigorous version of dynamical spacetime — Witten 2022's Type II algebras and the crossed product

## 1. Motivation and background

In Phase 4 we showed that modular flow $\sigma_t^\omega$ functions as a state-dependent emergent time.
But mathematically rigorously, the algebraic structure of quantum gravity is one level deeper:

**Problem**: in QFT, the local algebra $\mathcal{A}(A)$ of a spatial region $A$ is a **Type III$_1$ von Neumann algebra** (Buchholz–Wichmann 1986). This means:
- It has no density matrix (= $\rho_A$ cannot be defined).
- The entropy is essentially divergent ("$\infty - \infty$").
- It has no pure state or trace state.

This makes "entropy in a gravitational theory" undefinable.

**Witten's resolution (2022)**:
> Adding the observer's clock, i.e. taking the **crossed product** with the modular flow, converts Type III$_1$ → Type II. Type II algebras have density matrices and **finite** entropies.

This is the rigorous answer to "what is entropy in gravity?".

## 2. Classification of von Neumann algebras (Murray–von Neumann 1936)

### 2.1 Type I
Standard QM. Decomposable into tensor products. Has a trace.
- Type I$_n$: finite-dimensional ($n$ qubits etc.)
- Type I$_\infty$: infinite-dimensional, separable

### 2.2 Type II
Has a trace, but cannot be decomposed into pure states.
- **Type II$_1$**: finite trace (closed system with **finite** entropy)
- **Type II$_\infty$**: infinite trace

### 2.3 Type III
No trace, no pure states.
- **Type III$_\lambda$** ($0 < \lambda < 1$): "modular spectrum" discrete with ratio $\lambda$
- **Type III$_1$**: continuous modular spectrum (this is the QFT local algebra!)
- Type III$_0$: pathological, does not appear in QFT

**Important fact**: any bounded open region $\mathcal{O}$ in QFT has a local algebra $\mathcal{A}(\mathcal{O})$ of **Type III$_1$** (Driessler–Buchholz–Wichmann).

## 3. Tomita–Takesaki theory (revisited)

For any von Neumann algebra $\mathcal{M}$ + state $\omega$, a unique **modular automorphism** $\sigma_t^\omega$ is defined (Phase 4).
$$\sigma_t^\omega: \mathcal{M} \to \mathcal{M}, \quad t \in \mathbb{R}$$

This exists independently of the type. In Type III$_1$, $\sigma_t$ is an **outer automorphism** (= no internal Hamiltonian generator) — and this leaves room to construct a crossed product.

## 4. Definition of the crossed product

### 4.1 General definition

For a von Neumann algebra $\mathcal{M}$ and an action $\alpha: G \to \mathrm{Aut}(\mathcal{M})$ ($G$ a group), the crossed product
$$\mathcal{M} \rtimes_\alpha G$$
is constructed as follows:
- New Hilbert space $\hat{\mathcal{H}} = \mathcal{H} \otimes L^2(G)$
- New algebra generators: $\pi(a)$ ($a \in \mathcal{M}$) and $u(g)$ ($g \in G$), with the relation
  $$u(g) \pi(a) u(g)^{-1} = \pi(\alpha_g(a))$$

### 4.2 Crossed product with the modular flow

For $G = \mathbb{R}$ and $\alpha = \sigma^\omega$ (modular flow):
$$\hat{\mathcal{M}} = \mathcal{M} \rtimes_{\sigma^\omega} \mathbb{R}$$

This is interpreted as the "algebra of an observer with a clock":
- $\pi(a)$: observable $a \in \mathcal{M}$
- $u(t)$: time translation of the observer
- The relation: motion of the clock advances $a$ along the modular flow

**Connes' theorem (1973)**:
$$\mathcal{M} \text{ is Type III}_1 \;\Longrightarrow\; \mathcal{M} \rtimes_{\sigma} \mathbb{R} \text{ is Type II}_\infty$$

Thus **the crossed product converts the type from III to II**.

### 4.3 Connection to gravity (Chandrasekaran–Penington–Witten 2022)

In the semiclassical picture of gravity, the observer's Hamiltonian $H_{\rm obs}$ can be identified with the modular Hamiltonian generating $\sigma_t^\omega$. Then the algebra of observers in a gravitational theory is automatically
$$\mathcal{A}(\mathcal{O}) \rtimes \mathbb{R}_{\rm time}$$
which is Type II. This makes **density matrices and entropies definable**.

## 5. Relation to de Sitter (link with Phase 13)

The half-universe region algebra of a de Sitter observer is:
- Strictly Type III$_1$ (the QFT without gravity)
- Once the observer's clock is included, Type II$_1$ (finite trace!)

**Why Type II$_1$ matters**:
- A trace state $\tau$ exists → "maximally mixed state" is definable.
- Entropy $S(\rho) = -\tau(\rho \log \rho)$ has **finite values**.
- $S$ is bounded by its maximum $\log(\dim) = $ Bekenstein–Hawking entropy $S_{\rm dS} = 3\pi/(G_N \Lambda)$.

This is the mathematically rigorous version of Phase 13's "**$\Lambda$ small ⇔ entropy capacity large**".

## 6. What can be shown numerically

The full Type III$_1$ → II conversion is an infinite-dimensional algebraic story, but on a finite lattice we can see the **signatures of Type-III-like UV divergence and Type-II-like finiteness**:

### Demo A: UV divergence (Type III signature)
The 1+1D CFT subregion entanglement entropy
$$S(A) = \frac{c}{3}\log\frac{L_A}{a} + \mathrm{const}$$
diverges as $a \to 0$ (= lattice spacing zero, continuum limit).

Numerical check: at fixed $L_A/L = $ const, increasing $N$ gives $S \sim (c/3) \log N$ divergence.

### Demo B: UV-finiteness of relative entropy (Type II safe)
Casini positivity (Phase 2):
$$S_{\rm rel}(\rho || \sigma) = \delta\langle K_\sigma\rangle - \delta S \geq 0$$
$S_{\rm rel}$ is **finite in every type**. A physical, observer-independent Type II observable.

Numerical check: at fixed $L_A/L$, $I(A:B)$ for two fixed disjoint intervals saturates as $N \to \infty$.

### Demo C: regularisation by an observer's clock
Add a finite-dim observer ($D_{\rm obs}$). Entropy is bounded by $\log D_{\rm obs}$.

This is the minimal-model implementation of "Type III divergence regulated by the observer's Hilbert space" via crossed product.

### Demo D: Type II$_1$ joint entropy
The combined entropy of "system + observer" is
$$S_{\rm total} = S_{\rm sys + obs} \leq \min(S_{\rm sys, naive}, \log D_{\rm obs})$$

This directly implements the finiteness of Type II$_1$.

## 7. Position within ITU

In Phases 1–13 we derived spacetime, gravity, matter, symmetry breaking, cosmological evolution, $\Lambda$ from quantum information structure.
Phase 14 adds the **final mathematical-rigour upgrade** to the whole construction:

> Gravitational entropy is essentially divergent in Type III$_1$, but adding an **observer** (= crossed product with modular flow) makes it Type II$_1$ and **finite**. This is the mathematically rigorous definition of quantum-gravity entropy.

Together this gives the trinity:
- Phase 4: time = modular flow
- Phase 13: $\Lambda$ = 1/(entropy capacity)
- Phase 14: observer dependence = type conversion (III → II)

## 8. Limitations and future tasks

✅ Demonstrable (this Phase):
- Type III divergence signature (UV-dependent $S$)
- Type II finiteness signature (UV-finite mutual information / relative entropy)
- Minimal model of regularisation by an observer

⚠️ Not demonstrable (open):
- Full Type III$_1$ structure (infinite-dimensional algebra)
- Full crossed product with a dynamical observer
- Relation to the observer's subjective experience (= the interpretation problem of quantum measurement)

These are at the cutting edge of contemporary physics and philosophy.
