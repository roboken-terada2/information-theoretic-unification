# ITU Tier 1+ #14 Communications — Pass-1.5 Deep Dive

**K_comm = -log ρ_comm** — Operator-algebraic Shannon channel modular Hamiltonian.

## Contents

- `paper_tier1plus_14_communications.md` — main paper (16 phases)
- `theory_phase555.md` ... `theory_phase570.md` — per-phase notes
- `polytope_45vertex_comm_deep.py` — ITU verifications + Shannon-MIMO scaling sim + polytope refresh
- `REFERENCES.md` — short bibliography
- `CITATION.cff` — citation file
- `zenodo_metadata.json` — Zenodo deposit metadata

## Numerical headline

Shannon-MIMO capacity scaling, B = 100 MHz, SNR = 10 dB:

```
Single antenna:        C = 345.9 Mbps
N = 16 antennas:       C = 1,120.7 Mbps (3.24x SISO gain)
N = 512 antennas:      C = 1,428.8 Mbps (4.13x SISO gain)
Log-log fit:           C_MIMO ~ N^0.17  (saturation regime SNR << N)
dK_comm per doubling:  +0.40 nats (N=1->2) decaying to +0.01 nats (N=256->512)
```

Generation peak rates: 4G ~1 Gbps → 5G ~100 Gbps → 6G IMT-2030 ~1 Tbps (10× per gen).

## Run

```bash
python -X utf8 polytope_45vertex_comm_deep.py
```

## License

CC-BY-4.0
