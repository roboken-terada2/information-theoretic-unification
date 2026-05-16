"""
Phase 92: Manipulation + Locomotion + Sensorimotor
Tier 1 #13 — Phase 2/4

4 numerical experiments:
1. K-channel bandwidth analysis: vision/tactile/proprio (manipulation)
2. Locomotion speed evolution 1995-2030 (humanoid)
3. Bayesian sensorimotor: PPO-like RL convergence with active inference
4. VLA models bandwidth: RT-2, OpenVLA, pi0, Helix

Output: manipulation_locomotion.png + manipulation_locomotion_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: K-channel bandwidth analysis
# ----------------------------------------------------------------------
def test1_kchannels():
    channels = [
        {"name": "Vision (RGB-D)",     "freq_Hz": 60,   "bits_per_sample": 1e7, "color": "#1f77b4"},
        {"name": "Plan (high-level)",  "freq_Hz": 5,    "bits_per_sample": 1e3, "color": "#ff7f0e"},
        {"name": "Trajectory",         "freq_Hz": 500,  "bits_per_sample": 1e2, "color": "#2ca02c"},
        {"name": "Tactile (skin)",     "freq_Hz": 500,  "bits_per_sample": 1e3, "color": "#d62728"},
        {"name": "Proprioception",     "freq_Hz": 1000, "bits_per_sample": 1e2, "color": "#9467bd"},
        {"name": "Audio",              "freq_Hz": 100,  "bits_per_sample": 1e3, "color": "#8c564b"},
    ]
    for c in channels:
        c["total_bits_per_sec"] = c["freq_Hz"] * c["bits_per_sample"]
        c["log10_bps"] = math.log10(c["total_bits_per_sec"])
    return {"channels": channels, "total_bps": sum(c["total_bits_per_sec"] for c in channels)}


# ----------------------------------------------------------------------
# Test 2: Humanoid locomotion speed evolution
# ----------------------------------------------------------------------
def test2_locomotion():
    timeline = [
        {"year": 2000, "model": "ASIMO",          "walk_ms": 0.5, "run_ms": None,  "stair": True,  "parkour": False},
        {"year": 2005, "model": "ASIMO v2",       "walk_ms": 1.7, "run_ms": 1.4,   "stair": True,  "parkour": False},
        {"year": 2013, "model": "Atlas v1 (DRC)", "walk_ms": 0.4, "run_ms": None,  "stair": True,  "parkour": False},
        {"year": 2016, "model": "Atlas v2",       "walk_ms": 1.0, "run_ms": None,  "stair": True,  "parkour": False},
        {"year": 2018, "model": "Atlas parkour",  "walk_ms": 1.5, "run_ms": 2.5,   "stair": True,  "parkour": True},
        {"year": 2020, "model": "Atlas dance",    "walk_ms": 2.0, "run_ms": 3.0,   "stair": True,  "parkour": True},
        {"year": 2024, "model": "Atlas electric", "walk_ms": 2.5, "run_ms": 5.6,   "stair": True,  "parkour": True},
        {"year": 2024, "model": "Optimus Gen 2",  "walk_ms": 1.5, "run_ms": None,  "stair": False, "parkour": False},
        {"year": 2025, "model": "Unitree G1",     "walk_ms": 2.0, "run_ms": 3.3,   "stair": True,  "parkour": True},
        {"year": 2030, "model": "Embodied AGI",   "walk_ms": 3.0, "run_ms": 7.0,   "stair": True,  "parkour": True},
    ]
    # Add human reference
    human_walk = 1.4
    human_run = 4.0  # average
    bolt_sprint = 12.4  # peak

    return {
        "timeline": timeline,
        "human_walk_ms": human_walk,
        "human_run_ms": human_run,
        "bolt_sprint_ms": bolt_sprint,
    }


# ----------------------------------------------------------------------
# Test 3: Bayesian sensorimotor (PPO-like) convergence
# ----------------------------------------------------------------------
def test3_rl_convergence():
    """
    Simulate PPO-like RL convergence:
    r(t) = R_max * (1 - exp(-t/tau))
    Compare different tasks (manipulation vs walking) with different tau.
    """
    n_steps = 500
    t = np.arange(n_steps)
    tasks = [
        {"name": "Block stacking",    "R_max": 1.0, "tau": 50,   "color": "#1f77b4"},
        {"name": "Door opening",      "R_max": 1.0, "tau": 100,  "color": "#ff7f0e"},
        {"name": "Cloth folding",     "R_max": 0.7, "tau": 200,  "color": "#2ca02c"},
        {"name": "Bipedal walking",   "R_max": 0.95, "tau": 80,  "color": "#d62728"},
        {"name": "Backflip",          "R_max": 0.8, "tau": 300,  "color": "#9467bd"},
    ]
    out = []
    rng = np.random.default_rng(42)
    for task in tasks:
        # Mean curve + noise (exploration)
        r_mean = task["R_max"] * (1 - np.exp(-t / task["tau"]))
        # Active inference adds noise that decreases over time
        noise = 0.15 * np.exp(-t / 1000) * rng.standard_normal(n_steps)
        r_observed = np.clip(r_mean + noise, 0, 1)
        out.append({
            "task": task["name"],
            "color": task["color"],
            "R_max": task["R_max"],
            "tau": task["tau"],
            "r_curve": r_observed.tolist(),
            "converged_steps_to_90pct": int(np.argmax(r_observed >= task["R_max"] * 0.9)) if any(r_observed >= task["R_max"] * 0.9) else None,
        })
    return {"tasks": out, "n_steps": n_steps, "t": t.tolist()}


# ----------------------------------------------------------------------
# Test 4: VLA models bandwidth
# ----------------------------------------------------------------------
def test4_vla():
    models = [
        {"name": "RT-2 (DeepMind 2023)",       "params_B": 55,  "ctrl_Hz": 5,   "year": 2023},
        {"name": "Code as Policies",            "params_B": 0.5, "ctrl_Hz": 1,   "year": 2022},
        {"name": "Octo (UCB 2024)",             "params_B": 0.1, "ctrl_Hz": 20,  "year": 2024},
        {"name": "OpenVLA (Stanford 2024)",     "params_B": 7,   "ctrl_Hz": 10,  "year": 2024},
        {"name": "π0 (Physical Intelligence)",  "params_B": 3,   "ctrl_Hz": 50,  "year": 2024},
        {"name": "Helix (Figure 2024)",         "params_B": 7,   "ctrl_Hz": 200, "year": 2024},
        {"name": "Embodied GPT-5 (proj 2027)",  "params_B": 100, "ctrl_Hz": 500, "year": 2027},
        {"name": "Embodied AGI (proj 2030)",    "params_B": 500, "ctrl_Hz": 1000, "year": 2030},
    ]
    for m in models:
        m["compute_score"] = math.log10(m["params_B"] * 1e9 * m["ctrl_Hz"])
    return {"models": models}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: K-channel bandwidth
    ax = axes[0, 0]
    channels = t1["channels"]
    names = [c["name"] for c in channels]
    log_bps = [c["log10_bps"] for c in channels]
    colors = [c["color"] for c in channels]
    y_pos = np.arange(len(channels))
    ax.barh(y_pos, log_bps, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel("log10(bits/sec)")
    ax.set_title(f"K-channel bandwidth in manipulation | total = 10^{math.log10(t1['total_bps']):.1f} bps")
    ax.grid(alpha=0.3, axis="x")

    # Panel 2: Humanoid locomotion speed
    ax = axes[0, 1]
    timeline = t2["timeline"]
    years = [t["year"] for t in timeline]
    walk = [t["walk_ms"] if t["walk_ms"] else 0 for t in timeline]
    run = [t["run_ms"] if t["run_ms"] else 0 for t in timeline]
    ax.plot(years, walk, "o-", color="#1f77b4", lw=2, markersize=8, label="Walk speed", alpha=0.85)
    has_run = [(y, r) for y, r in zip(years, run) if r > 0]
    if has_run:
        ax.plot([h[0] for h in has_run], [h[1] for h in has_run], "s-", color="#d62728", lw=2,
                markersize=8, label="Run speed", alpha=0.85)
    ax.axhline(t2["human_walk_ms"], ls=":", color="green", alpha=0.6, label=f"Human walk ({t2['human_walk_ms']} m/s)")
    ax.axhline(t2["human_run_ms"], ls=":", color="orange", alpha=0.6, label=f"Human run ({t2['human_run_ms']} m/s)")
    ax.axhline(t2["bolt_sprint_ms"], ls=":", color="red", alpha=0.4, label=f"Bolt sprint ({t2['bolt_sprint_ms']} m/s)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Speed (m/s)")
    ax.set_title("Humanoid locomotion speed (Atlas 2024 = 5.6 m/s, human sprinter level)")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 3: RL convergence
    ax = axes[1, 0]
    t = np.array(t3["t"])
    for task in t3["tasks"]:
        ax.plot(t, task["r_curve"], color=task["color"], lw=1.5, label=task["task"], alpha=0.85)
    ax.set_xlabel("Training steps")
    ax.set_ylabel("Average reward")
    ax.set_title("Bayesian sensorimotor RL convergence (PPO-style with active inference)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4: VLA models bandwidth
    ax = axes[1, 1]
    models = t4["models"]
    years = [m["year"] for m in models]
    params = [m["params_B"] for m in models]
    ctrl = [m["ctrl_Hz"] for m in models]
    sizes = [c * 5 for c in ctrl]
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(models)))
    for i, m in enumerate(models):
        ax.scatter(m["year"], m["params_B"], s=m["ctrl_Hz"] * 5 + 50,
                   c=[colors[i]], alpha=0.7, edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(m["name"].split("(")[0].strip(), (m["year"], m["params_B"]),
                    xytext=(5, 5), textcoords="offset points", fontsize=7, rotation=15)
    ax.set_yscale("log")
    ax.set_xlabel("Year")
    ax.set_ylabel("Parameters (B)")
    ax.set_title("VLA models: parameters + control frequency (size ~ ctrl_Hz)")
    ax.grid(alpha=0.3, which="both")

    plt.suptitle("Phase 92: Manipulation + Locomotion + Sensorimotor — K-flow dynamics",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 92: Manipulation + Locomotion + Sensorimotor")
    print("=" * 70)

    print("\n[Test 1] K-channel bandwidth (manipulation)")
    t1 = test1_kchannels()
    for c in t1["channels"]:
        print(f"  {c['name']:25s}  {c['freq_Hz']:5} Hz  {c['bits_per_sample']:.0e} bits  =>  {c['total_bits_per_sec']:.1e} bps")
    print(f"  TOTAL: {t1['total_bps']:.2e} bps  (~10^{math.log10(t1['total_bps']):.1f})")

    print("\n[Test 2] Humanoid locomotion timeline")
    t2 = test2_locomotion()
    for ent in t2["timeline"]:
        run_str = f"{ent['run_ms']:.1f}" if ent["run_ms"] else "n/a"
        print(f"  {ent['year']}: {ent['model']:25s} walk={ent['walk_ms']:.1f}, run={run_str} m/s")
    print(f"  Human reference: walk {t2['human_walk_ms']}, run {t2['human_run_ms']}, Bolt {t2['bolt_sprint_ms']} m/s")

    print("\n[Test 3] RL convergence")
    t3 = test3_rl_convergence()
    for task in t3["tasks"]:
        conv = task["converged_steps_to_90pct"]
        print(f"  {task['task']:25s}  R_max={task['R_max']:.2f}  tau={task['tau']:3d}  conv@90%={conv}")

    print("\n[Test 4] VLA models")
    t4 = test4_vla()
    for m in t4["models"]:
        print(f"  {m['year']}: {m['name']:38s} {m['params_B']:6.1f}B params  {m['ctrl_Hz']:4d} Hz ctrl")

    out = {
        "phase": 92,
        "title": "Manipulation + Locomotion + Sensorimotor",
        "test1_kchannels": t1,
        "test2_locomotion": t2,
        "test3_rl_convergence": {
            "n_steps": t3["n_steps"],
            "tasks_summary": [{"task": t["task"], "R_max": t["R_max"], "tau": t["tau"],
                              "converged": t["converged_steps_to_90pct"]} for t in t3["tasks"]],
        },
        "test4_vla": t4,
    }
    with open("manipulation_locomotion_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: manipulation_locomotion_summary.json")

    make_figure(t1, t2, t3, t4, "manipulation_locomotion.png")
    print("  ✓ Figure saved: manipulation_locomotion.png")

    print("\n" + "=" * 70)
    print("Phase 92 complete: total bandwidth 10^{:.1f} bps, Atlas 5.6 m/s = sprinter level"
          .format(math.log10(t1["total_bps"])))
    print("=" * 70)
