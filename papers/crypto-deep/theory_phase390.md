# Phase 390: Post-quantum migration roadmap (NIST 2024-30)

NIST が主導する **post-quantum migration** の roadmap を整理。

## NIST PQC timeline

```
2016: PQC competition launch
2017-19: Round 1, 2 (69 → 26 candidates)
2020-22: Round 3 (7 finalists + 8 alternates)
2022.7: First selection (Kyber, Dilithium, Falcon, SPHINCS+)
2024.8: FIPS 203, 204, 205 published
2024.3: HQC added as code-based backup
2024-2025: Falcon FIPS 206 expected
2030+: 主要 cryptographic infrastructure migration completed (goal)
```

## Government mandates

```
US (NSM-10, 2022.5):
  Federal systems migration to PQC by 2035

EU (Cyber Resilience Act, 2024):
  Critical infrastructure PQC mandatory

NSA Cybersecurity Information Sheet (2023):
  Migration prioritization
```

## Industry adoption

```
2024 announcements:
  Apple iMessage PQC (PQ3 protocol, 2024.2)
  Google Chrome Kyber (2024)
  Amazon AWS KMS post-quantum (planned)
  Microsoft Azure Key Vault PQC (in progress)

Cisco, Juniper, Fortinet: hybrid TLS deployment
```

## Migration challenges

```
1. Key/signature size increase:
   ML-DSA-87: 2.6KB pubkey, 4.6KB signature
   vs ECDSA: 64 bytes pubkey, 72 bytes signature
   → 30-60x increase, bandwidth + storage impact

2. Performance:
   Kyber faster than X25519 (ECDH)
   Dilithium slower than ECDSA
   → Mixed results

3. Hybrid deployment:
   Run classical + post-quantum simultaneously
   Defense-in-depth during transition
```

## Timeline 予測

```
2024-2026: Awareness + planning phase
2026-2028: Hybrid deployment widespread
2028-2030: PQC primary, classical backup
2030-2035: Full PQC migration
2035+: Classical cryptography deprecated
```

## ITU framework での migration

```
K_crypto inventory:
  各 protocol/system の K_crypto value 評価
  Migration priority: low K_crypto first

Per-system roadmap:
  TLS 1.3 → hybrid (Kyber + X25519)
  SSH → hybrid
  PKI → ML-DSA root + intermediate
  Database encryption → ML-KEM

Each transition tracked in OSF / NIST PQC migration database


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase390
