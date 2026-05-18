# Phase 386: 既存 hardness assumptions (LWE, SIS, RingLWE) との接続

LWE 以外の post-quantum hardness assumptions を ITU framework に整合させる。

## Short Integer Solution (SIS)

```
Ajtai 1996 LATIN:
  Given: random A ∈ Z_q^{n×m} (n < m)
  Find: small vector x ∈ Z^m \ {0} with Ax = 0 mod q

Hardness reduction: SVP に reduction (Ajtai 1996)
```

## RingLWE (Lyubashevsky-Peikert-Regev 2010 Eurocrypt)

```
Ring R = Z[x] / (x^n + 1) for power of 2 n
LWE in ring R (more compact than plain LWE)

CRYSTALS-Kyber, Dilithium のベース
```

## Module-LWE (Langlois-Stehlé 2015)

```
LWE と RingLWE を一般化
Module rank d を可変 (d=1 = RingLWE, d=n = plain LWE)

Security tunable for performance/security trade-off
```

## ITU 統一 framework

```
全 lattice-based hardness は K_crypto framework で:
  ρ_key|public は lattice 上の short vector distribution
  K_crypto は lattice basis reduction の computational depth に比例
  Modular flow σ_t は BKZ-2.0 (Chen-Nguyen 2011) reduction process

Security parameter λ:
  ⟨K_crypto⟩ ≈ O(λ)
  τ_mix ≈ 2^O(λ)
```

## Hardness graph

```
Plain LWE ⊆ RingLWE ⊆ Module-LWE ⊆ ?
              ↓
            BKZ-2.0 attack (Chen-Nguyen 2011)
              ↓
            CryptDeep 2023 (NIST Phase 4 attack discussion)
```

## 攻撃進化との追従

```
2017: Sieving for SVP (Becker-Ducas-Gama-Laarhoven)
2020: NIST Round 3 cryptanalysis
2023: Castryck-Decru SIDH attack (alternative hardness broken)
2024: Falcon side-channel analyses

ITU view: 各攻撃は σ_t mixing time を polynomial に縮める発見
         全攻撃を ITU framework で記述可能 (とすれば unified resistance benchmark)


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase386
