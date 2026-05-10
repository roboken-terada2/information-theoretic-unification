# Phase 3: Holography — emergent AdS₃ from MERA tensor network

## 1. Motivation and history

In Phase 1, a 1D boundary ($S^1$) emerged from information distance. In Phase 2, the entanglement variation of the boundary CFT became the linearised Einstein equation. Here we show that **the bulk hyperbolic geometry (AdS$_3$) also emerges from information structure**. The key is MERA (Multi-scale Entanglement Renormalization Ansatz, Vidal 2007).

Swingle 2012's claim: the geometric structure of MERA is **discrete AdS space**.

## 2. MERA construction

Coarse-grain a 1D critical state on $N$ sites in a hierarchy of $\log_2 N$ layers:
- **Layer 0**: $N$ sites = physical boundary
- **Layer $k$**: $N/2^k$ sites (1 site = entangled coarse-graining of 2 old sites)
- **Layer $\log_2 N$**: 1 site = integral of the whole system

Within each layer there are **disentanglers** (unitaries between adjacent sites); between layers there are **isometries** (2→1 contraction). The connectivity graph is a binary tree on a cylinder.

## 3. Emergent hyperbolic geometry

The shortest-path length on the MERA graph between boundary points $i, j$ satisfies
$$d_G(i, j) \approx 2 \log_2 |i - j| + \text{const}.$$
This is the same scaling as the boundary geodesic length in the hyperbolic metric
$$ds^2_{\text{AdS}_3} = R^2\!\left(\frac{-dt^2 + dz^2 + dx^2}{z^2}\right)$$
where $L = 2R \log\!\left(|x_1 - x_2|/\epsilon\right)$. Here $z$ is the MERA layer number = the emergent **radial direction (energy scale)**.

## 4. MERA version of Ryu–Takayanagi

Take an interval $A$ of length $L$ on the boundary, and let $|\gamma_A|$ be the number of edges in the minimal cut on the MERA graph that disconnects $A$:
$$S_A^{\text{RT}} = \frac{|\gamma_A|}{4 G_N}.$$
The minimal cut "climbs from each end of $A$ up to layer $k = \log_2 L$ and crosses horizontally at that layer", giving
$$|\gamma_A| \sim 2 \log_2 L.$$

Comparing with the CFT result $S_A = \frac{c}{3} \log L$:
$$\frac{2}{4 G_N \log 2} = \frac{c}{3} \implies \frac{1}{G_N} = \frac{2 c \log 2}{3}.$$
This is the lattice version of Brown–Henneaux $c = 3 R_{\text{AdS}}/(2 G_N)$ (with appropriate units).

## 5. Embedding into the Poincaré disk

Each MERA node $(k, m)$ is placed on the Poincaré disk at
$$r_k = \tanh(k \, \Delta\rho/2), \qquad \theta_m = 2\pi (m + 0.5)/(N/2^k)$$
($\Delta\rho$ is the hyperbolic distance per layer). The boundary ($k=0$) is placed at $r \to 1$, not at $r=0$ (Lobachevsky inner-time = MERA-up convention).

## 6. Simulation plan

### (i) Pure-graph verification (MERA geometry independent of state)
- Construct the binary-tree MERA graph.
- Compute all-pairs shortest distance via BFS.
- For boundary points $(i, j)$, plot $d_G(i, j)$ vs $|i - j|$ on log-log. Slope $\approx 2$ (consistent with $2 \log_2 |i-j|$).

### (ii) RT-formula verification
- For each interval of length $L$ on the boundary, compute $|\gamma_A|$ on the MERA graph.
- Check $\sim 2 \log_2 L$.
- Compare to the actual $S_A(L)$ of the XX-model ground state and confirm **shape agreement** (numerical verification of Brown–Henneaux).

### (iii) Poincaré disk visualisation
- Embed MERA into the hyperbolic disk and visually confirm it is a time slice of AdS$_3$.
- Draw an RT surface (bulk geodesic) for one boundary interval.

This **completely reconstructs the bulk 2D hyperbolic spacetime from the 1D boundary's quantum information structure**.
