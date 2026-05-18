# Phase 360: 数値 simulation protocol — Stim + Qiskit 

mKQEC threshold conjecture (Phase 349, 359) を **数値で検証する具体プロトコル**。
2026-2027 Q1 実行可能。

## Stim (Gidney 2021) を使った最小例

Stim は Craig Gidney (Google QAI) 開発の高速 stabilizer simulator (Quantum 5, 497).

### Simulation 構造

```python
# Pseudo-code (Phase 360 main contribution)
import stim
import numpy as np

def simulate_mkqec_threshold(noise_model, distances=[3, 5, 7], shots=10_000):
 """
 Compare mKQEC threshold with standard surface code under given noise.
 
 noise_model:
 'depolarizing': symmetric (Surface code optimal)
 'biased_z': η = γ_Z / γ_X large
 'erasure': photonic erasure
 """
 thresholds = {}
 
 for d in distances:
 # Generate stabilizer circuit
 if noise_model == 'depolarizing':
 circ = stim.Circuit.generated(
 'surface_code:rotated_memory_z',
 distance=d, rounds=d,
 after_clifford_depolarization=0.01, # depolar rate
 )
 elif noise_model == 'biased_z':
 # Custom mKQEC circuit for biased noise
 circ = generate_mkqec_circuit(d, bias=100)
 elif noise_model == 'erasure':
 circ = generate_mkqec_erasure_circuit(d, erasure_rate=0.01)
 
 # Sample errors
 sampler = circ.compile_detector_sampler
 detections, observations = sampler.sample(shots, separate_observables=True)
 
 # Decode (using minimum-weight matching)
 decoder = stim.compile_matching(...)
 predictions = decoder(detections)
 
 # Compare with truth
 logical_errors = np.sum(predictions != observations) / shots
 thresholds[d] = logical_errors
 
 return thresholds


def generate_mkqec_circuit(distance, bias):
 """
 Construct mKQEC stabilizer circuit for biased noise (Phase 356).
 
 Generators (3x3 example for d=3):
 g_1..g_6: X-row/col parities (detect Z errors)
 g_7, g_8: Z chains (detect X errors, fewer)
 """
 # ... full implementation ~200 lines
 pass

# Expected output (from theoretical predictions):
# {'depolarizing': {3: 0.045, 5: 0.012, 7: 0.0028}} ← surface code, threshold ~1%
# {'biased_z': {3: 0.043, 5: 0.0095, 7: 0.0019}} ← mKQEC, threshold ~1.4-1.5%
# {'erasure': {3: 0.020, 5: 0.0030, 7: 0.00045}} ← mKQEC erasure-aware, ~2.5x better
```

### 結果解釈

```
Threshold extraction (Fowler 2012 method):
 1. plot logical_error vs physical_error for distance d=3,5,7
 2. lines cross at p_threshold
 3. compare across noise models

Expected results (consistent with Phase 357 XZZX comparison):

Surface code (depolarizing): p* ≈ 1.00%
XZZX (biased η=100): p* ≈ 5.00% (Z-only error)
mKQEC biased (η=100): p* ≈ 1.3-1.5% (mixed errors)
mKQEC erasure (ε=10%): p* ≈ 50% (erasure threshold)
```

## Qiskit Aer (IBM) 代替 simulation

```python
from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit

def qiskit_mkqec_check(distance, noise_model_qiskit):
 """
 Verify mKQEC on Qiskit Aer (slower but more flexible).
 """
 qc = QuantumCircuit(distance**2, distance**2)
 # ... build stabilizer code
 
 backend = AerSimulator(method='statevector', noise_model=noise_model_qiskit)
 result = backend.run(qc, shots=1000).result
 return result.get_counts
```

Qiskit は biased noise model 自然に表現可能 (T1/T2 直接指定).

## OpenQASM + Q# (Microsoft Azure)

```
For Quantinuum hardware integration:
 - OpenQASM 3 export from Stim/Qiskit
 - Quantinuum API submission
 - Run on H2/H3 trapped-ion hardware (2027)
 
Estimated cost: $50-100K for ~100 circuit-hours (2027 pricing)
```

## Decoder algorithm

```
Minimum-Weight Perfect Matching (MWPM):
 Standard surface code decoder (Edmonds 1965 matching algorithm)
 PyMatching library (Higgott 2022)
 O(n³) time complexity
 
mKQEC adapted decoder:
 Biased noise: use bias info to weight edges
 Erasure: use known erasure positions (much faster)
 
Recent: 
 Neural network decoders (Torlai 2017, Krastanov-Jiang 2017)
 AlphaQubit (DeepMind 2024 Nature): RNN-based 
 → mKQEC で AlphaQubit-like decoder 設計 (Pass-2 続編)
```

## Concrete simulation roadmap

```
2026 Q3:
 □ Stim setup, generate_mkqec_circuit implementation
 □ Distance-3 mKQEC simulation, depolarizing baseline
 □ First numerical threshold estimate
 Effort: 1 person-month
 
2026 Q4:
 □ Biased noise (η=10, 100, 1000) systematic study
 □ Compare with XZZX (Tuckett 2018 reproduce)
 □ mKQEC threshold confirmed 30%+ over surface
 Effort: 2 person-months
 
2027 Q1:
 □ Erasure noise study
 □ PsiQuantum-relevant erasure rate study
 □ 2.5-3x improvement confirmed
 Effort: 2 person-months
 
2027 Q2:
 □ Distance-5, 7, 9 scaling
 □ Logical error rate exponential suppression demonstrate
 □ arXiv paper draft
 Effort: 1-2 person-months
 
2027 Q3:
 □ Hardware-relevant simulation (Quantinuum H3 noise model)
 □ Practical resource estimate
 □ Industry collaboration outreach
 Effort: 2 person-months

合計 effort: 8-10 person-months (1 postdoc 1 yr)
合計 cost: $150-200K
```

## Open-source code release

```
mKQEC simulation framework:
 Repository: github.com/munehiroterada/mkqec
 License: MIT (or Apache-2.0)
 Documentation: ReadTheDocs
 
Modules:
 mkqec.lindblad: Lindbladian → K_QC^(0) construction
 mkqec.stabilizer: MASA computation, stabilizer matrix
 mkqec.circuit: Stim circuit generation
 mkqec.decoder: MWPM + biased adaptation
 mkqec.benchmark: Threshold extraction utility
 
Targets:
 Pull request to PyMatching (decoder integration)
 Stim ecosystem contribution
 Demonstrate at QIP 2027 / IEEE QCE 2027
```

## Comparison with existing simulations

```
Tuckett 2018 PRX: XZZX threshold 5% (η=100, Stim) — reference
Bravyi-Cross-Gambetta-Gosset 2020 PRX: surface code threshold ~1%
Google Willow 2024.12 Nature: distance-3,5,7 surface, below threshold demonstrated

mKQEC simulations (本論文 expected output):
- Reproduce all above as special cases
- 新規結果: biased mKQEC 1.3-1.5% threshold (predicted)
- 新規結果: erasure mKQEC ~50% threshold (predicted)
- 新規結果: scalable noise model variation framework
```

## 数値結果と Pass-2 接続

```
2027 数値 simulation 完了 (本論文 prediction P=0.65 達成):
 → ITU principle が QC で predictive value あり
 → mKQEC framework hardware で testable proposition
 → Pass-2 Pillar 1 priority 1 (Phase 351)

2028 Quantinuum H3 first demo (本論文 prediction P=0.55):
 → Numerical threshold 検証 with実機
 → 30%+ improvement 確認 ⇒ evidence 強化
 → <0% ⇒ ITU 公理 QC limited, Pass-1 で部分反証

2029 distance-7 fault-tolerant (P=0.40):
 → 実用 fault-tolerant logical qubit 達成
 → Industry impact 明確化

2030 Nature/Science paper (P=0.45):
 → Tier 1+ #1 logical conclusion
 → Pass-3 (社会実装) 経路明確
```

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #QC #mKQEC #Stim #Qiskit #PyMatching #NumericalSimulation #AlphaQubit #Phase360
