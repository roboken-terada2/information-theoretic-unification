# References — Tier 1+ #1 QC Deep Dive (mKQEC) — Deep-Applied 16-Phase Edition

## Quantum error correction foundations

1. Shor, P. W. (1995). Scheme for reducing decoherence in quantum computer memory. *Phys. Rev. A* 52, R2493.
2. Steane, A. M. (1996). Error correcting codes in quantum theory. *Phys. Rev. Lett.* 77, 793.
3. Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. *Ann. Phys.* 303, 2-30 (orig. 1997 preprint).
4. Aharonov, D. & Ben-Or, M. (1997). Fault-tolerant quantum computation with constant error. *STOC* 1997.
5. Knill, E., Laflamme, R. & Zurek, W. H. (1998). Resilient quantum computation. *Science* 279, 342-345.
6. Fowler, A. G., Mariantoni, M., Martinis, J. M. & Cleland, A. N. (2012). Surface codes: towards practical large-scale quantum computation. *Phys. Rev. A* 86, 032324.
7. Bravyi, S. & Kitaev, A. (2005). Universal quantum computation with ideal Clifford gates and noisy ancillas. *Phys. Rev. A* 71, 022316. (Magic state distillation.)
8. Horsman, C., Fowler, A. G., Devitt, S. & Van Meter, R. (2012). Surface code quantum computing by lattice surgery. *New J. Phys.* 14, 123011.
9. Yoder, T. J., Takagi, R. & Chuang, I. L. (2016). Universal fault-tolerant gates on concatenated stabilizer codes. *Phys. Rev. X* 6, 031039.

## Biased-noise codes (mKQEC precursors)

10. Tuckett, D. K., Bartlett, S. D. & Flammia, S. T. (2018). Ultrahigh error threshold for surface codes with biased noise. *Phys. Rev. X* 8, 021046.
11. Tuckett, D. K. et al. (2020). The XZZX surface code. *Nature Communications* 11, 2172.
12. Vlastakis, B. et al. (2013). Deterministically encoding quantum information using 100-photon Schrödinger cat states. *Science* 342, 607-610.
13. Aliferis, P. & Cross, A. W. (2007). Subsystem fault tolerance with the Bacon-Shor code. *Phys. Rev. Lett.* 98, 220502.

## Hardware platforms (2024-2025)

14. Google Quantum AI (2024). Quantum error correction below the surface code threshold (Willow). *Nature* (2024.12, 105 qubits, distance-3/5/7).
15. Quantinuum (2024). H2 racetrack ion trap quantum computer (56 qubits, T1≈60s, T2≈1s).
16. PsiQuantum (2025). Omega photonic chip (erasure-dominated noise).
17. Microsoft (2024). Interferometric single-shot parity measurement (Majorana-1). *Nature* 638, 651-655.
18. IBM Quantum (2024). Heron 156 qubits.

## Open quantum systems & operator-algebraic foundation

19. Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Commun. Math. Phys.* 48, 119-130.
20. Gorini, V., Kossakowski, A. & Sudarshan, E. C. G. (1976). Completely positive dynamical semigroups of N-level systems. *J. Math. Phys.* 17, 821.
21. Davies, E. B. (1974). Markovian master equations. *Commun. Math. Phys.* 39, 91-110.
22. Frigerio, A. (1977). Quantum dynamical semigroups and approach to equilibrium. *Commun. Math. Phys.* 63, 269-276.
23. Frigerio, A. (1978). Stationary states of quantum dynamical semigroups. *Rep. Math. Phys.* 19, 197-238.
24. Alicki, R. (1976). On the detailed balance condition for non-Hamiltonian systems. *Rep. Math. Phys.* 10, 249-258.
25. Spohn, H. (1978). Entropy production for quantum dynamical semigroups. *J. Math. Phys.* 19, 1227-1230.
26. Lebowitz, J. L. & Spohn, H. (1978). Irreversible thermodynamics for quantum systems weakly coupled to thermal reservoirs. *Adv. Chem. Phys.* 38, 109-142.
27. Cubitt, T., Lucia, A., Michalakis, S. & Pérez-García, D. (2015). Stability of local quantum dissipative systems. *Nature Communications* 6, 6720.

## Modular theory & relative entropy

28. Tomita, M. (1967). Standard forms of von Neumann algebras. *V-th Functional Analysis Sympos.*, Sendai.
29. Takesaki, M. (1970). *Tomita's Theory of Modular Hilbert Algebras and its Applications*. LNM 128, Springer.
30. Araki, H. (1976). Relative entropy of states of von Neumann algebras. *Publ. RIMS Kyoto* 11, 809-833.
31. Uhlmann, A. (1977). Relative entropy and the Wigner-Yanase-Dyson-Lieb concavity. *Commun. Math. Phys.* 54, 21-32.
32. Connes, A. (1973). Une classification des facteurs de type III. *Ann. Sci. ENS* 6, 133-252. (Fields Medal 1982.)
33. Faulkner, T., Guica, M., Hartman, T., Myers, R. C. & Van Raamsdonk, M. (2014). Gravitation from entanglement in holographic CFTs. *JHEP* 03, 051. (FLM first law.)
34. Maldacena, J. (1998). The large-N limit of superconformal field theories and supergravity. *Adv. Theor. Math. Phys.* 2, 231-252. (Breakthrough Prize 2012.)

## Simulation tools & decoders

35. Gidney, C. (2021). Stim: a fast stabilizer circuit simulator. *Quantum* 5, 497.
36. IBM Quantum (2024). Qiskit Aer simulator. (Open source.)
37. Higgott, O. (2022). PyMatching: A Python package for decoding quantum codes with minimum-weight perfect matching. *ACM Transactions on Quantum Computing*.
38. Edmonds, J. (1965). Paths, trees, and flowers. *Canad. J. Math.* 17, 449-467. (Minimum-weight matching.)
39. Krastanov, S. & Jiang, L. (2017). Deep neural network probabilistic decoder for stabilizer codes. *Sci. Rep.* 7, 11003.
40. DeepMind / Google QAI (2024). AlphaQubit: a recurrent neural network for quantum error correction. *Nature* (2024.12).

## Lean Mathlib formalization

41. de Moura, L. et al. (2015, 2021). The Lean theorem prover (Lean 4). *CADE*.
42. The mathlib Community (2020). The Lean Mathematical Library. *CPP*.
43. Buzzard, K. (2022). The Liquid Tensor Experiment formalization in Lean.
44. Tao, T. et al. (2024). Formalizing the Polynomial Freiman-Ruzsa conjecture in Lean (3 weeks).
45. Hales, T. C. et al. (2017). A formal proof of the Kepler conjecture. *Forum Math. Pi* 5, e2.

## Recent operator-algebraic / information-theoretic progress

46. Bardet, I. et al. (2019). Group transference techniques for the estimation of the decoherence times and capacities of quantum Markov semigroups. *J. Math. Phys.*
47. Junge, M. & LaRacuente, N. (2021). Improved efficient methods for spectral gap estimation. (Operator-algebraic Lindbladian bounds.)
48. Kastoryano, M. J. & Temme, K. (2013). Quantum logarithmic Sobolev inequalities and rapid mixing. *J. Math. Phys.* 54, 052202.

## ITU programme

49. Terada, M. (2026). *Tier 0 v4.0 Pass-1 FINALE*. Zenodo, doi:10.5281/zenodo.20267445.
50. Terada, M. (2025). *Tier 1 #1 Fault-Tolerant Quantum Computing*. Zenodo, doi:10.5281/zenodo.20139391.
51. Terada, M. (2026). *Tier 1 #44 ITU Mathematical Rigor*. Zenodo, doi:10.5281/zenodo.20266828.
52. Terada, M. (2026). *Tier 1 #45 ITU Falsification Experiments*. Zenodo, doi:10.5281/zenodo.20267212.

(Full 52 references; ~3x the Pass-1 #1 paper's reference count, reflecting deep dive scope.)
