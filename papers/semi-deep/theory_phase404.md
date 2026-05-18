# Phase 404: AI accelerators (Cerebras WSE-3, Tesla Dojo, NVIDIA Blackwell)

**AI accelerator chips** は K_semi の specialized variant。

## NVIDIA Blackwell B200 (2024.3)

```
Process: TSMC 4NP (custom 4nm)
Transistors: 208 billion (dual die)
Memory: 192 GB HBM3e
Performance: 20 PFLOPS (FP4)
Price: $30-40K per GPU

GB200 NVL72 rack (72 GPUs + 36 CPUs):
  $3M, 130 TB/s NVLink
  Used in OpenAI, Microsoft, Google datacenters
```

## Cerebras WSE-3 (2024.3)

```
Wafer-Scale Engine 3:
  4 trillion transistors (largest chip ever)
  900,000 AI cores
  44 GB on-chip SRAM
  Process: TSMC 5nm
  Size: 46,225 mm² (single wafer-sized chip)

vs Blackwell: 0.6 PFLOPS per WSE-3 module
Better for sparse workloads
```

## Tesla Dojo D1 (2024)

```
Custom AI training chip for FSD (Full Self-Driving)
Architecture: training tile (25 D1 chips)
Production: limited deployment 2024

Targeted at autonomous driving + humanoid robotics
```

## Google TPU v5e/v5p

```
TPU v5p (2023): inference, 459 TFLOPS BF16
TPU v6 Trillium (2024): 4.7x v5e performance

Used for Gemini training, PaLM 2
```

## ITU view: AI accelerators

```
Specialized K_semi: matmul + tensor ops dominant
⟨K_AI_chip⟩ < ⟨K_general_CPU⟩ for arbitrary workload
但し specific tasks で K_AI_chip >> K_CPU

ITU "modular dedication":
  K_total = K_specialized + K_general_overhead


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Semi #K_semi #Phase404
