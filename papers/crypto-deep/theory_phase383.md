# Phase 383: NIST PQC standards (Kyber, Dilithium, Falcon, SPHINCS+, HQC)

NIST 標準化された PQC algorithms を ITU framework で統一。

## NIST PQC competition (2016-2024)

```
2016: Competition 開始
2017-19: Round 1, 2 (69 candidates → 26)
2020-22: Round 3 (7 finalists + 8 alternates)
2022.7: First selection
2024.8: FIPS standards 公表
  - ML-KEM (Kyber rename) FIPS 203
  - ML-DSA (Dilithium rename) FIPS 204
  - SLH-DSA (SPHINCS+ rename) FIPS 205
2024.3: HQC added as backup (code-based)
2024-: Falcon FIPS 206 (delayed)
```

## ML-KEM (Kyber) details

```
ML-KEM (Module-LWE based):
  Security levels: 512, 768, 1024 (bit security ~128, 192, 256)
  Public key: 800-1568 bytes
  Ciphertext: 768-1568 bytes

ITU view: K_crypto ≈ rank-2 Module-LWE noise space dimension
```

## ML-DSA (Dilithium) details

```
ML-DSA (signature, Module-LWE + SIS):
  ML-DSA-44, -65, -87 levels
  Public key: 1312-2592 bytes
  Signature: 2420-4595 bytes

ITU view: K_crypto = -log Pr[signature passing valid check | wrong key]
```

## Falcon details

```
Falcon (FFT lattice, NTRU):
  Smaller key/signature than ML-DSA
  But FFT floating-point implementation 注意 (Hawk extension)

ITU view: NTRU ring-based K_crypto
```

## SPHINCS+ details

```
SPHINCS+ (hash-based stateless signature):
  Forest of Random Subsets (FORS) + many-time hash
  Very large signatures (8-50 KB)
  But conservative security (only relies on hash collision resistance)

ITU view: K_crypto = Merkle tree path uncertainty
```

## HQC (code-based)

```
HQC (Hamming Quasi-Cyclic):
  NIST 2024.3 selected as backup
  Conservative alternative to lattice-based

ITU view: K_crypto = -log Pr[decode | public matrix]
```

## 統一 framework 主張

```
全 NIST PQC algorithms は ITU framework で:
  ρ_key|public は各 algorithm 固有
  K_crypto = -log ρ_key|public は universal definition
  Modular flow σ_t は各々の hardness reduction

これにより:
  Cross-algorithm hardness 比較が rigorous
  Hybrid construction の security proof が unified


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase383
