# Phase 8: Real-world 4D extension — AdS₅/CFT₄ correspondence

## 1. Motivation

Phases 1–6 used 1D boundary (AdS$_3$/CFT$_2$); Phase 7 used 2D boundary (AdS$_4$/CFT$_3$).
**Our universe is 3+1-dimensional**, and the corresponding quantum gravity is AdS$_5$/CFT$_4$. This is the most-studied AdS/CFT correspondence — the most likely candidate for a realistic quantum gravity (Maldacena 1997).

In this Phase, we use a 3D cubic-lattice free fermion as the minimal model of a boundary CFT$_4$ and show numerically that the central proposition of Phases 1–7
$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)} \rho_A] \quad \forall A$$
extends to **real-world 4D physics**.

## 2. 3D cubic-lattice fermion

Nearest-neighbour hopping on the 3D cubic lattice:
$$H = -\sum_{\langle ij\rangle} (c_i^\dagger c_j + \mathrm{h.c.})$$

In Fourier transform with PBC, the dispersion is $\epsilon(\vec k) = -2(\cos k_x + \cos k_y + \cos k_z)$. At half filling ($\mu = 0$), the Fermi surface is the **2-dimensional surface** $\cos k_x + \cos k_y + \cos k_z = 0$ — a critical $d=3$ system.

## 3. The 3D Gioev–Klich formula

For $d$-dimensional free fermions whose Fermi surface has codimension 1 (= general Fermi liquid):
$$S(A) \sim L^{d-1} \log L$$

In three dimensions this gives $S(L^3) \sim L^2 \log L$ — the area law $L^{d-1}$ plus a logarithmic correction from the 1D Fermi surface.

Predicted $L^2 \log L$ ratios:
- $S(L=4) / S(L=2) \to 16 \log 4 / 4 \log 2 = 8$
- $S(L=3) / S(L=2) \to 9 \log 3 / 4 \log 2 \approx 3.56$

If the numerical ratios are in the 4–8 range, this is consistent.

## 4. 4D MERA for AdS₅

Binary MERA on a 3D boundary:
- Layer $k$: $(N/2^k)^3$ sites
- Within a layer: 6-neighbour connectivity (3D square lattice)
- Between layers: each higher-layer site contracts a $2 \times 2 \times 2 = 8$-block

For $8 \times 8 \times 8 = 512$ sites with 3 layers (512 → 64 → 8 → 1) the network has 585 nodes — a **4-dimensional structure** (3 spatial + 1 radial = energy scale).

**Prediction** (3D generalisation of Swingle 2012):
- Boundary graph distance $\sim 2 \log_2 |\vec r_1 - \vec r_2|$
- Same as the boundary-geodesic length in **AdS$_5$ hyperbolic geometry**

## 5. Brown–Henneaux generalisation and Newton's constant

In AdS$_{d+1}$/CFT$_d$, the Brown–Henneaux relation generalises to
$$\frac{R_{\rm AdS}^{d-1}}{G_N^{(d+1)}} \propto C_T$$

where $C_T$ is the CFT stress-tensor 2-point coefficient (higher-dimensional analogue of the central charge). For 4D CFT $C_T \sim N^2$ (= number of degrees of freedom for SU(N) $\mathcal{N}=4$ Yang–Mills).

## 6. Simulation plan

### Part A: 3D fermion ground state and area law
- Correlation matrix on $8 \times 8 \times 8 = 512$ sites
- Compute $S(L)$ for $L \times L \times L$ cubic regions ($L = 2, 3, 4$)
- Fit $S(L) = a L^2 \log L + b L^2 + c L + d$

### Part B: efficient MI computation
- Compute 130816 pair 2-site entropies **vectorised** (analytic 2×2 eigenvalues)
- Distance matrix and MDS to evaluate the dimensionality of information geometry

### Part C: 4D MERA graph distances
- Construct the 3D MERA (~ 585 nodes)
- BFS for all-boundary-pair graph distances
- Fit slope $d_{\rm graph} \sim a \log d_{\rm phys}$
- Compare with the AdS$_5$ prediction $a = 2/\log 2 \approx 2.885$

### Part D: philosophical implications
- If the numerics match the AdS$_5$ prediction, the Phase 1–6 framework applies to the actual 4D quantum gravity of our universe.

## 7. Expected accuracy

|  | 1D (Phase 3) | 2D (Phase 7) | 3D (Phase 8 expected) |
|---|---|---|---|
| Boundary site count | 64 | 256 | 512 |
| MERA nodes | 127 | 341 | 585 |
| Distance-slope precision | 0.4% | 5% | 5–15% |

Lattice effects are larger and short-distance finite-size corrections are more severe in 3D, so 1D-level precision is not expected; **the existence of the scaling law** is the main thing that should be visible.
