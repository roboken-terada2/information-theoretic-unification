# Phase 7: 4D extension — 2D boundary CFT and AdS₄ bulk

## 1. Motivation

Phases 1–6 were carried out entirely in 1+1D CFT (XX chain). The corresponding bulk is 2+1D AdS$_3$.
Our actual universe is 3+1D, and the corresponding quantum gravity is AdS$_5$/CFT$_4$ or AdS$_4$/CFT$_3$.

In this Phase we extend to **2D boundary CFT**, dual to the AdS$_4$ boundary, providing the minimal model of 3+1D gravity. We aim to show that the framework established in 1D
$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)}\rho_A] \quad \forall A$$
also holds in higher dimensions.

## 2. 2D free-fermion ground state

Nearest-neighbour hopping on a 2D square lattice $N_x \times N_y$:
$$H = -t\sum_{\langle i,j\rangle} (c_i^\dagger c_j + \mathrm{h.c.})$$

In Fourier transform with PBC, the dispersion is $\epsilon(\vec k) = -2t(\cos k_x + \cos k_y)$. At half filling ($\mu=0$), the Fermi surface is the square $\cos k_x + \cos k_y = 0$, i.e. $|k_x| + |k_y| = \pi$.

**Gapless / critical system**: as in 1D, the Fermi-surface set being a 1D curve in 2D BZ produces logarithmic enhancement of entanglement.

## 3. Gioev–Klich formula (log correction to area law)

Gioev–Klich 2006 / Wolf 2006: for the ground state of $d$-dimensional free fermions, the entanglement entropy of a region $A$ ($\partial A$ being $(d-1)$-dimensional) is
$$S(A) \sim \frac{1}{12} \frac{1}{(2\pi)^{d-1}} L^{d-1} \log L \cdot \left(\int_{\partial \Omega_A} d\sigma_x\right)\left(\int_{\partial F} |n_x\cdot n_k|\, d\sigma_k\right)$$

For 2D square lattice at half filling ($d=2$, $L\times L$ region):
$$S(L) \approx c_1 L \log L + c_2 L + c_3$$
where $c_1$ is determined by Fermi-surface geometry.

This is the "log violation of the area law" characteristic of critical systems — a higher-dimensional analogue of the 1D CFT's $S \sim (c/3) \log L$ from Phase 1.

## 4. 2D MI matrix and geometry recovery (generalisation of Phase 1)

For each pair of sites $(i,j)$ compute the mutual information $I(i:j)$. Use the same Cao–Carroll–Michalakis-style distance
$$d(i,j) = -\log\!\left(\frac{I(i:j)}{2\min(S_i, S_j)}\right)$$
and embed in 2D via classical MDS.

**Prediction**: the top 2 MDS eigenvalues should dominate, recovering the original 2D lattice geometry.

This is the higher-dimensional extension of Phase 1: "the spatial structure emerging from information is 2D".

## 5. 3D MERA and the AdS₄ bulk

2D MERA (Vidal 2009):
- Layer $k$: $(N_x/2^k) \times (N_y/2^k)$ lattice
- Within each layer, disentanglers on the 4 nearest neighbours
- Between layers, an isometry that contracts a $2\times 2$ block of the lower layer

Total node count $\sum_{k=0}^{\log_2 N} N^2/4^k \approx (4/3) N^2$. The graph is a **3D structure** (2 spatial directions + 1 energy-scale = AdS radial direction).

**Prediction (2D generalisation of Swingle 2012)**:
- Boundary graph distance $\sim 2 \log_2 |i-j|$
- This matches the geodesic length of an **AdS$_4$ hyperbolic geometry** between boundary points

**Brown–Henneaux generalisation (4D gravity)**:
$$\frac{R_{\rm AdS}^2}{G_{N,4}} \propto C_T$$
where $C_T$ is the stress-tensor 2-point coefficient (higher-dimensional analogue of the central charge) of the 2D CFT.

## 6. 4-dimensionalisation of Ryu–Takayanagi

For a 2D boundary region $A$, the minimal 2D surface $\gamma_A$ in the AdS$_4$ bulk gives
$$S_A = \frac{\mathrm{Area}(\gamma_A)}{4 G_{N,4}}.$$

The minimum cut on the 3D MERA (= the smallest set of edges separating $A$ from its complement) realises the discrete version of this.

## 7. Simulation plan

### Part A: 2D free-fermion ground state
- $16 \times 16$ square lattice with PBC, half filling.
- Diagonalise the hopping matrix to get the correlation matrix $C$ (256×256).
- For central $L \times L$ regions ($L = 2,...,7$), compute $S(L)$.
- Fit $S(L) = a L\log L + b L + c$; check coefficient $a$ against Gioev–Klich prediction.

### Part B: 2D MI geometry
- All 256×255/2 pair MI values.
- Distance matrix → MDS → 2D embedding.
- Compare with original lattice coordinates $(x, y)$ — evaluate via $R^2$ score.

### Part C: 3D MERA and AdS₄
- Build a 16×16 binary MERA graph (5 layers, 341 nodes).
- All-pairs graph distance via BFS.
- Verify scaling $d_{\rm graph}$ vs $\log|i-j|$ for boundary pairs.
- Compare slope to $2/\log 2$.

## 8. Expected accuracy and limitations

- 0.4% accuracy in 1D is hard to attain in 2D (more complex Fermi surface, larger finite-size effects).
- Still: (i) seeing the log correction confirms criticality, (ii) MDS recovering 2D confirms the 2D info→space picture, (iii) AdS$_4$ distance log scaling confirms hyperbolicity — all qualitative successes are expected.
- Numerical evidence that the framework of Phases 1–6 is **dimension-independent**.
