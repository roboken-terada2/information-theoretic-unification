# Phase 396: EUV lithography operator-algebraic view

**ASML EUV (Extreme Ultraviolet, 13.5 nm wavelength)** が現代 semiconductor 製造の中核。

## EUV 基礎

```
Wavelength: 13.5 nm (vs DUV 193 nm)
Source: laser-produced plasma (Sn droplet + CO2 laser)
Optics: all-reflective (multilayer Mo/Si mirrors)
NA (numerical aperture): 0.33 (standard) → 0.55 (high-NA, 2024+)

Rayleigh resolution: R = k_1 × λ / NA
  k_1 ~ 0.3-0.4 (optimized)
  → R ~ 13 nm (standard EUV)
  → R ~ 8 nm (high-NA)
```

## ITU 解釈

```
Lithography process は ρ_lithography over wafer feature distributions:
  ρ_lithography = density over (x, y) positions for each device

EUV resolution R は K_semi の granularity:
  ⟨K_semi⟩ ≤ log(wafer_area / R²) ≈ 30+ bits per device

High-NA で R 縮小 → K_semi capacity 増加
```

## ASML High-NA shipment 2024-2025

```
2024.1: Intel に初出荷 (Twinscan EXE:5000)
2024.7: Intel 18A pilot production
2024-25: TSMC, Samsung 採用予定

Pricing: ~$400M per machine
Throughput: 220 wafers/hour
Annual capacity: ~50 systems

ITU view: High-NA は K_semi extension の technological enabler


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Semi #K_semi #Phase396
