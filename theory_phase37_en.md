# Phase 37: Lipid bilayer self-assembly — physical Markov blanket

## 1. Motivation

The Markov blanket of Phase 36 is abstract. Living systems require a
**physical** boundary separating self from environment. This boundary is the
**cell membrane** — and Phase 37 shows it self-assembles thermodynamically
from amphiphilic molecules under the same ITU principle.

## 2. Model

Coarse-grained 2D Monte Carlo: $N$ amphiphilic dimers (head + tail bead),
periodic boundary, Lennard-Jones tail-tail attraction + head-tail repulsion,
Metropolis dynamics at temperature $T$.

## 3. Results

| Quantity | Result |
|---|---|
| Largest cluster | **50/60 amphiphiles (83%)** ✓ |
| Total clusters | 2 (50 + 10) |
| Energy descent | $+0 \to -226$ (LJ minimisation) ✓ |
| Spatial segregation | $0.50 \to 0.67$ (**1.34× increase**) ✓ |
| Cluster verdict | **macro-aggregate (bilayer/vesicle)** |

Hydrophobic effect alone drives spontaneous self-organisation into a
bilayer-like aggregate.

## 4. ITU correspondence

| Phase 5 (Bulk locality = QECC) | Phase 37 (Bilayer = Markov blanket) |
|---|---|
| Code space | Cell interior |
| Physical errors | Environmental fluctuations |
| Stabiliser measurement | Membrane protein signalling |
| Bulk-boundary separation | Cell-environment separation |

Both are **information-protecting boundary** structures arising from the
same principle.

## 5. 5-layer ITU hierarchy (after Phase 37)

| Layer | Phase | Substance |
|---|---|---|
| 1 | 1-32 | Quantum information |
| 2 | 33 | Chemical QECC |
| 3 | 35 | Eigen replication |
| 4 | 36 | Cognitive FEP |
| **5** | **37** | **Spatial Markov blanket (bilayer)** |

## 6. Verdict

- Amphiphilic molecules self-assemble spontaneously under hydrophobic
  interaction alone,
- The resulting macro-aggregate creates a physical interior/exterior split,
- This is the spatial realisation of the same QECC-style information
  separation principle that governs spacetime.

Phase 37 thus completes the **spatial self** — a necessary precursor to the
first cell (Phase 39).
