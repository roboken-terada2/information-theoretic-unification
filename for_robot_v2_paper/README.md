# ITU Tier 1+ #13 Robotics — Pass-1.5 Deep Dive

**K_robot = -log ρ_robot** — Operator-algebraic embodied-agent modular Hamiltonian.

## Contents

- `paper_tier1plus_13_robotics.md` — main paper (16 phases)
- `theory_phase539.md` ... `theory_phase554.md` — per-phase notes
- `polytope_45vertex_robot_deep.py` — ITU verifications + foundation-model sample-efficiency sim + polytope refresh
- `REFERENCES.md` — short bibliography
- `CITATION.cff` — citation file
- `zenodo_metadata.json` — Zenodo deposit metadata

## Numerical headline

Foundation-model fine-tune vs RL from scratch (toy 32-action manipulation):

```
H_max = log(32) = 3.466 nats
RL from scratch    : tau_RL = 30,000 episodes
Foundation fine-tune: tau_FM = 80    episodes
Collapse-rate ratio: 375x   (consistent with RT-2/OpenVLA 100-1000x reports)
```

ITU view: K_policy exponential collapse via pretrained prior; foundation robotics shifts the starting distribution onto the task-relevant manifold.

## Run

```bash
python -X utf8 polytope_45vertex_robot_deep.py
```

## License

CC-BY-4.0
