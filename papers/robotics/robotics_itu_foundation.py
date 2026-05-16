"""
Phase 91: ITU Robotics / Embodied AI foundation
Tier 1 #13 — Phase 1/4

4 numerical experiments:
1. DOF and K-state dimension scaling (robot families)
2. Humanoid evolution: control freq and K-state bits over time
3. Embodied AGI degree = K_self x K_embodiment x K_action (use case analysis)
4. Moravec's paradox quantitative: chess vs walking K-space comparison

Output: robotics_itu_foundation.png + robotics_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: DOF and K-state dimension
# ----------------------------------------------------------------------
def test1_dof_kstate():
    robots = [
        {"name": "Industrial arm (ABB)", "DOF": 6,   "K_dim_log10": 2.0, "category": "industrial"},
        {"name": "Spot (BD quadruped)",  "DOF": 12,  "K_dim_log10": 3.0, "category": "quadruped"},
        {"name": "Digit (Agility)",      "DOF": 16,  "K_dim_log10": 4.0, "category": "humanoid"},
        {"name": "ASIMO (Honda 2010)",   "DOF": 34,  "K_dim_log10": 4.5, "category": "humanoid"},
        {"name": "Atlas (BD electric)",  "DOF": 28,  "K_dim_log10": 5.5, "category": "humanoid"},
        {"name": "Optimus Gen 2",        "DOF": 28,  "K_dim_log10": 5.7, "category": "humanoid"},
        {"name": "Figure 02",            "DOF": 35,  "K_dim_log10": 6.0, "category": "humanoid"},
        {"name": "Human (estimated)",    "DOF": 244, "K_dim_log10": 9.0, "category": "biological"},
        {"name": "ASI embodied (proj)",  "DOF": 1000,"K_dim_log10": 12.0,"category": "ASI"},
    ]
    return {
        "robots": robots,
        "DOF_range": [min(r["DOF"] for r in robots), max(r["DOF"] for r in robots)],
        "K_dim_range_log10": [
            min(r["K_dim_log10"] for r in robots),
            max(r["K_dim_log10"] for r in robots)
        ],
    }


# ----------------------------------------------------------------------
# Test 2: Humanoid evolution timeline
# ----------------------------------------------------------------------
def test2_humanoid_evolution():
    timeline = [
        {"year": 1995, "name": "Honda P2",         "DOF": 28, "control_Hz": 50,   "K_bits_log10": 2.0},
        {"year": 2000, "name": "ASIMO v1",         "DOF": 26, "control_Hz": 100,  "K_bits_log10": 2.5},
        {"year": 2005, "name": "ASIMO v2",         "DOF": 34, "control_Hz": 200,  "K_bits_log10": 3.0},
        {"year": 2010, "name": "ASIMO 2010",       "DOF": 34, "control_Hz": 100,  "K_bits_log10": 3.0},
        {"year": 2013, "name": "Atlas v1",         "DOF": 28, "control_Hz": 500,  "K_bits_log10": 4.0},
        {"year": 2016, "name": "Atlas v2",         "DOF": 28, "control_Hz": 1000, "K_bits_log10": 4.5},
        {"year": 2020, "name": "Atlas hydraulic",  "DOF": 28, "control_Hz": 1000, "K_bits_log10": 5.0},
        {"year": 2022, "name": "Optimus Bumblebee","DOF": 28, "control_Hz": 1000, "K_bits_log10": 5.0},
        {"year": 2024, "name": "Atlas electric",   "DOF": 28, "control_Hz": 2000, "K_bits_log10": 6.0},
        {"year": 2024, "name": "Optimus Gen 2",    "DOF": 28, "control_Hz": 2000, "K_bits_log10": 5.7},
        {"year": 2024, "name": "Figure 02",        "DOF": 35, "control_Hz": 1500, "K_bits_log10": 6.0},
        {"year": 2025, "name": "Unitree G1",       "DOF": 23, "control_Hz": 1000, "K_bits_log10": 5.0},
        {"year": 2028, "name": "Optimus Gen 4 (proj)", "DOF": 35, "control_Hz": 5000, "K_bits_log10": 7.5},
        {"year": 2030, "name": "Embodied AGI (proj)",  "DOF": 40, "control_Hz": 10000, "K_bits_log10": 8.5},
    ]
    years = [t["year"] for t in timeline]
    K_log = [t["K_bits_log10"] for t in timeline]
    Hz = [t["control_Hz"] for t in timeline]
    # Linear fit on K_log vs year
    slope, intercept = np.polyfit(years, K_log, 1)
    return {
        "timeline": timeline,
        "K_growth_per_year_orders": float(slope),
        "K_doubling_period_yr": float(math.log10(2.0) / slope) if slope > 0 else None,
        "control_freq_2024_vs_1995_ratio": float(2000 / 50),
        "K_bits_2024_vs_1995_ratio": float(10 ** (6.0 - 2.0)),
    }


# ----------------------------------------------------------------------
# Test 3: Embodied AGI degree per use case
# ----------------------------------------------------------------------
def test3_embodied_agi():
    use_cases = [
        {"name": "Warehouse logistics (Optimus, Digit)", "K_self": 0.20, "K_embodiment": 0.30, "K_action": 0.50, "year": 2025},
        {"name": "Housekeeping (laundry, dish)",          "K_self": 0.30, "K_embodiment": 0.50, "K_action": 0.60, "year": 2028},
        {"name": "Childcare / eldercare assistance",      "K_self": 0.50, "K_embodiment": 0.60, "K_action": 0.65, "year": 2032},
        {"name": "Full cooking (gourmet)",                "K_self": 0.60, "K_embodiment": 0.70, "K_action": 0.70, "year": 2035},
        {"name": "Surgical assistant",                    "K_self": 0.70, "K_embodiment": 0.80, "K_action": 0.85, "year": 2040},
        {"name": "Free dialogue + empathetic action",     "K_self": 0.80, "K_embodiment": 0.85, "K_action": 0.85, "year": 2045},
        {"name": "Human-indistinguishable (Turing+phys)", "K_self": 0.95, "K_embodiment": 0.95, "K_action": 0.95, "year": 2050},
    ]
    for uc in use_cases:
        uc["embodied_AGI_degree"] = uc["K_self"] * uc["K_embodiment"] * uc["K_action"]
    return {
        "use_cases": use_cases,
        "max_degree": float(max(u["embodied_AGI_degree"] for u in use_cases)),
    }


# ----------------------------------------------------------------------
# Test 4: Moravec's paradox quantitative
# ----------------------------------------------------------------------
def test4_moravec():
    tasks = [
        {"name": "Chess",         "K_action_log10": 4.0, "K_env_log10": 4.0, "continuous": False, "evol_yr": 500},
        {"name": "Go",            "K_action_log10": 5.7, "K_env_log10": 5.7, "continuous": False, "evol_yr": 4000},
        {"name": "Theorem proof", "K_action_log10": 6.0, "K_env_log10": 1.0, "continuous": False, "evol_yr": 2500},
        {"name": "Walking",       "K_action_log10": 5.0, "K_env_log10": 6.0, "continuous": True,  "evol_yr": 5e8},
        {"name": "Grasping",      "K_action_log10": 5.0, "K_env_log10": 6.0, "continuous": True,  "evol_yr": 5e8},
        {"name": "Driving",       "K_action_log10": 4.0, "K_env_log10": 7.0, "continuous": True,  "evol_yr": 100},  # human-novel
        {"name": "Conversation",  "K_action_log10": 4.0, "K_env_log10": 5.0, "continuous": False, "evol_yr": 1e5},
    ]
    for t in tasks:
        # Total K dimension
        t["K_total_log10"] = t["K_action_log10"] + t["K_env_log10"]
        # Difficulty for AI = K_total * continuous penalty (continuous = 10x harder)
        t["AI_difficulty_log10"] = t["K_total_log10"] + (1.0 if t["continuous"] else 0.0)
        # Evolutionary optimization (log years)
        t["evol_log10_yr"] = math.log10(max(t["evol_yr"], 1))
        # Net "Moravec gap" = how AI sees it vs how evolution optimized it
        t["moravec_gap"] = t["AI_difficulty_log10"] - t["evol_log10_yr"]
    return {"tasks": tasks}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: DOF vs K-state dimension
    ax = axes[0, 0]
    cat_color = {"industrial": "#1f77b4", "quadruped": "#ff7f0e",
                 "humanoid": "#2ca02c", "biological": "#d62728", "ASI": "#9467bd"}
    for r in t1["robots"]:
        ax.scatter(r["DOF"], r["K_dim_log10"], s=200, c=cat_color[r["category"]],
                   alpha=0.85, edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(r["name"], (r["DOF"], r["K_dim_log10"]), xytext=(7, 3),
                    textcoords="offset points", fontsize=7)
    ax.set_xscale("log")
    ax.set_xlabel("DOF (Degrees of Freedom)")
    ax.set_ylabel("log10(K-state dimension)")
    ax.set_title("DOF vs K-state dimension across robot families")
    ax.grid(alpha=0.3, which="both")

    # Panel 2: Humanoid evolution timeline
    ax = axes[0, 1]
    years = [t["year"] for t in t2["timeline"]]
    K_log = [t["K_bits_log10"] for t in t2["timeline"]]
    ax.plot(years, K_log, "o-", color="#1f77b4", lw=2, markersize=8, alpha=0.85)
    for t in t2["timeline"][::2]:
        ax.annotate(t["name"], (t["year"], t["K_bits_log10"]),
                    xytext=(3, 5), textcoords="offset points", fontsize=6, rotation=15)
    ax.set_xlabel("Year")
    ax.set_ylabel("log10(K-state bits)")
    ax.set_title(f"Humanoid K-state evolution | doubling = {t2['K_doubling_period_yr']:.1f} yr")
    ax.grid(alpha=0.3)

    # Panel 3: Embodied AGI degree per use case
    ax = axes[1, 0]
    use_cases = t3["use_cases"]
    names = [u["name"][:30] for u in use_cases]
    degrees = [u["embodied_AGI_degree"] for u in use_cases]
    years = [u["year"] for u in use_cases]
    colors = plt.cm.RdYlGn(np.array(degrees))
    y_pos = np.arange(len(use_cases))
    bars = ax.barh(y_pos, degrees, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, (uc, deg, yr) in enumerate(zip(use_cases, degrees, years)):
        ax.text(deg + 0.01, i, f"{yr}", fontsize=8, va="center")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Embodied AGI degree (K_self × K_embodiment × K_action)")
    ax.set_xlim(0, 1.0)
    ax.set_title(f"Embodied AGI degree progression (2025-2050)")
    ax.grid(alpha=0.3, axis="x")

    # Panel 4: Moravec's paradox
    ax = axes[1, 1]
    tasks = t4["tasks"]
    names = [t["name"] for t in tasks]
    difficulty = [t["AI_difficulty_log10"] for t in tasks]
    evol = [t["evol_log10_yr"] for t in tasks]
    colors = ["#d62728" if t["continuous"] else "#1f77b4" for t in tasks]
    x_pos = np.arange(len(tasks))
    width = 0.4
    ax.bar(x_pos - width/2, difficulty, width, color=colors, alpha=0.8,
           label="AI difficulty log10", edgecolor="black", linewidth=0.5)
    ax.bar(x_pos + width/2, evol, width, color="green", alpha=0.5,
           label="Evolution years log10", edgecolor="black", linewidth=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(names, rotation=20, fontsize=8)
    ax.set_ylabel("log10")
    ax.set_title("Moravec's paradox: continuous tasks (red) optimized over 5e8 years")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    plt.suptitle("Phase 91: ITU × Robotics / Embodied AI — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 91: ITU × Robotics / Embodied AI — foundation")
    print("=" * 70)

    print("\n[Test 1] DOF and K-state dimension")
    t1 = test1_dof_kstate()
    for r in t1["robots"]:
        print(f"  {r['name']:30s}  DOF={r['DOF']:4d}  log10(K_dim)={r['K_dim_log10']:.1f}  [{r['category']}]")
    print(f"  Range: DOF {t1['DOF_range']}, log10 K_dim {t1['K_dim_range_log10']}")

    print("\n[Test 2] Humanoid evolution")
    t2 = test2_humanoid_evolution()
    for t in t2["timeline"][:5]:
        print(f"  {t['year']}: {t['name']:25s} DOF={t['DOF']} Hz={t['control_Hz']:5d} log10(K)={t['K_bits_log10']:.1f}")
    print(f"  ...")
    for t in t2["timeline"][-3:]:
        print(f"  {t['year']}: {t['name']:25s} DOF={t['DOF']} Hz={t['control_Hz']:5d} log10(K)={t['K_bits_log10']:.1f}")
    print(f"  K-state doubling period: {t2['K_doubling_period_yr']:.1f} years")
    print(f"  Control freq 2024 / 1995: {t2['control_freq_2024_vs_1995_ratio']:.0f}x")
    print(f"  K-bits 2024 / 1995:       {t2['K_bits_2024_vs_1995_ratio']:.0f}x")

    print("\n[Test 3] Embodied AGI degree per use case")
    t3 = test3_embodied_agi()
    for u in t3["use_cases"]:
        print(f"  {u['name']:48s}  AGI_deg={u['embodied_AGI_degree']:.3f}  ({u['year']})")
    print(f"  Max: {t3['max_degree']:.3f}")

    print("\n[Test 4] Moravec's paradox quantitative")
    t4 = test4_moravec()
    for tk in t4["tasks"]:
        cont = "CONTINUOUS" if tk["continuous"] else "discrete"
        print(f"  {tk['name']:18s}  K_tot={tk['K_total_log10']:.1f}  AI_diff={tk['AI_difficulty_log10']:.1f}  evol_log_yr={tk['evol_log10_yr']:.1f}  [{cont}]")

    out = {
        "phase": 91,
        "title": "ITU × Robotics / Embodied AI — foundation",
        "test1_dof_kstate": t1,
        "test2_humanoid_evolution": t2,
        "test3_embodied_agi": t3,
        "test4_moravec": t4,
    }
    with open("robotics_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: robotics_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "robotics_itu_foundation.png")
    print("  ✓ Figure saved: robotics_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 91 complete: max DOF=1000 (ASI proj), K-state 2x per {:.1f}yr, Embodied AGI 2050={:.2f}"
          .format(t2["K_doubling_period_yr"], t3["max_degree"]))
    print("=" * 70)
