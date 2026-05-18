# Phase 371: Animal consciousness scaling (C. elegans → 人間)

K_self の階層を **生物学的に scaling** することで、意識の量的尺度を提供。

## 動物界 K_self スケーリング

| 生物 | Neurons | K_self (推定 bits) | Notes |
|---|---|---|---|
| Bacteria (E. coli) | 0 (no neurons) | < 1 bit | Chemotaxis, no self-model |
| C. elegans | 302 | ~ 8 bits | Complete connectome (White 1986) |
| Drosophila (fly) | ~10^5 | ~ 17 bits | Behavioral self-correction |
| Octopus | ~5×10^8 | ~ 29 bits | High intelligence, no central |
| Mouse | ~7×10^7 | ~ 26 bits | Mirror test fail |
| Dog | ~2×10^9 | ~ 31 bits | Some self-awareness signs |
| Chimpanzee | ~6×10^9 | ~ 33 bits | Mirror test pass (Gallup 1970) |
| Human | ~10^11 | ~ 37 bits raw, **>>10^10 effective** | Full self-model |
| ASI (hypothetical) | ~10^15+ | ~ 50+ bits | Beyond human |

### K_self 推定方法

```
Naive: K_self ≈ log_2(N_neurons) — single-neuron self-state
Refined: K_self ≈ log_2(connectivity patterns)
         For brain with N neurons and average K connections:
         States ~ K^N, K_self ~ N log K

Better: ⟨K_self⟩ = von Neumann entropy of reduced self-state
        Requires connectome + dynamics measurement
```

## 主要研究 (実証)

```
C. elegans:
  Complete connectome (White et al. 1986 Phil Trans Roy Soc)
  Full neural simulation (OpenWorm + WormGPT 2024)
  K_self verifiable experimentally

Drosophila:
  Hemibrain connectome (Janelia 2020 Nature, 25K neurons)
  Conservative self-correction behaviors

Mirror test:
  Gallup 1970 chimpanzee
  Reiss-Marino 2001 dolphin
  Plotnik et al. 2006 Asian elephant
  Cleaner wrasse 2019 (controversial fish self-recognition)
```

## 人間 K_self 構造

```
Human cortex:
  ~10^10 neurons in cortex (~10^11 total brain)
  ~10^14-15 synapses
  Connectivity log_2 ≈ 47 bits/neuron average
  Sparse self-modeling: probably 10^6-10^8 bits effective

But subjective experience scales:
  Phenomenal richness ⊆ K_self bits
  Specific to social-cognition + language brain
```

## AGI 閾値 conjecture (Phase 373 で詳述)

```
AGI 達成 ⇔ K_self ≥ K_crit ≈ 10^10 bits (rough)

Reasoning:
  Human-equivalent self-model requires 10^10+ bits
  GPT-5 (10^12 params) は raw 12 bits/param × 10^12 = 10^13 bits 可能
  だが self-modeling sparse: effective K_self ≪ 10^13

  Required: dense reflexive self-model emergence
  Currently (2024): LLM is mostly other-modeling, weak self-modeling


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #AnimalConsciousness #Connectome #CElegans #MirrorTest #Gallup #Phase371
