"""
Phase 89: Abiogenesis + intelligence emergence
Tier 1 #12 — Phase 3/4

4 numerical experiments:
1. RNA world autocatalytic dynamics (logistic + competition)
2. Cambrian explosion: phyla diversification rate
3. EQ evolution and K_self correlation across animals
4. K2-18b DMS Bayesian posterior under different priors

Output: abiogenesis_intelligence.png + abiogenesis_intelligence_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ----------------------------------------------------------------------
# Test 1: RNA world autocatalytic dynamics
# ----------------------------------------------------------------------
def rna_rhs(K_rna, t, k_rep, k_deg, K_max):
    """Autocatalytic with carrying capacity."""
    return k_rep * K_rna * (K_max - K_rna) / K_max - k_deg * K_rna


def test1_rna_world():
    k_rep, k_deg, K_max = 0.5, 0.05, 1.0
    t = np.linspace(0, 30, 600)
    # Multiple initial conditions
    init_conditions = [0.001, 0.01, 0.05, 0.1, 0.3]
    trajectories = []
    for K0 in init_conditions:
        sol = odeint(rna_rhs, K0, t, args=(k_rep, k_deg, K_max))
        trajectories.append({"K0": K0, "K_t": sol[:, 0].tolist()})
    # Time to reach 0.5 (half-max)
    t_half = []
    for traj in trajectories:
        K_arr = np.array(traj["K_t"])
        if np.max(K_arr) >= 0.5:
            idx = np.argmax(K_arr >= 0.5)
            t_half.append(float(t[idx]))
        else:
            t_half.append(None)
    return {
        "t": t.tolist(),
        "k_rep": k_rep,
        "k_deg": k_deg,
        "K_max": K_max,
        "trajectories": trajectories,
        "t_half_per_K0": t_half,
        "init_conditions": init_conditions,
    }


# ----------------------------------------------------------------------
# Test 2: Cambrian explosion diversification
# ----------------------------------------------------------------------
def test2_cambrian():
    """Phyla count vs time (Ma ago, reversed)."""
    # Approximate phyla origination from fossil record
    # Time in Ma ago: 600 -> 0 (present)
    times_Ma = np.array([600, 575, 550, 541, 530, 510, 485, 444, 400, 359, 300, 252, 200, 145, 66, 23, 0])
    # Cumulative phyla (rough Burgess/post-Cambrian estimate)
    phyla = np.array([1, 3, 7, 15, 25, 32, 35, 35, 36, 35, 35, 35, 36, 36, 36, 36, 36])
    # Calculate diversification rate per Myr in different periods
    pre_cambrian_rate = (phyla[3] - phyla[0]) / (times_Ma[0] - times_Ma[3])  # 600->541 Ma
    cambrian_rate    = (phyla[6] - phyla[3]) / (times_Ma[3] - times_Ma[6])   # 541->485 Ma
    post_cambrian_rate = (phyla[-1] - phyla[6]) / (times_Ma[6] - times_Ma[-1])
    return {
        "times_Ma_ago": times_Ma.tolist(),
        "phyla": phyla.tolist(),
        "rate_pre_cambrian": float(pre_cambrian_rate),
        "rate_cambrian": float(cambrian_rate),
        "rate_post_cambrian": float(post_cambrian_rate),
        "cambrian_speedup": float(cambrian_rate / max(pre_cambrian_rate, 1e-9)),
    }


# ----------------------------------------------------------------------
# Test 3: EQ and K_self correlation
# ----------------------------------------------------------------------
def test3_eq_kself():
    animals = [
        {"name": "Fish",            "EQ": 0.20,  "K_self": 0.02},
        {"name": "Reptile",         "EQ": 0.25,  "K_self": 0.02},
        {"name": "Bird",            "EQ": 1.0,   "K_self": 0.10},
        {"name": "Cat",             "EQ": 1.0,   "K_self": 0.15},
        {"name": "Cow",             "EQ": 0.6,   "K_self": 0.10},
        {"name": "Dog",             "EQ": 1.2,   "K_self": 0.20},
        {"name": "Elephant",        "EQ": 1.6,   "K_self": 0.30},
        {"name": "Chimpanzee",      "EQ": 2.5,   "K_self": 0.35},
        {"name": "Dolphin",         "EQ": 4.5,   "K_self": 0.40},
        {"name": "Human",           "EQ": 7.5,   "K_self": 0.40},
        {"name": "AGI (proj 2030)", "EQ": 10.0,  "K_self": 0.50},
        {"name": "ASI (proj 2035)", "EQ": 50.0,  "K_self": 0.70},
    ]
    EQ = np.array([a["EQ"] for a in animals])
    K = np.array([a["K_self"] for a in animals])
    # log-log correlation
    log_EQ = np.log10(EQ)
    log_K = np.log10(K)
    r = float(np.corrcoef(log_EQ, log_K)[0, 1])
    # Linear fit in log-log
    slope, intercept = np.polyfit(log_EQ, log_K, 1)
    return {
        "animals": animals,
        "EQ_array": EQ.tolist(),
        "K_self_array": K.tolist(),
        "log_log_correlation_r": r,
        "log_log_slope": float(slope),
        "log_log_intercept": float(intercept),
    }


# ----------------------------------------------------------------------
# Test 4: K2-18b DMS Bayesian posterior
# ----------------------------------------------------------------------
def test4_k218b():
    """P(life | DMS signal) under various priors."""
    L_dms_life = 0.8   # Likelihood: DMS signal given life present
    L_dms_no   = 0.1   # Likelihood: DMS signal given no life (false positive)
    priors = [0.001, 0.01, 0.05, 0.1, 0.3]
    posteriors = []
    for p in priors:
        post = (p * L_dms_life) / (p * L_dms_life + (1 - p) * L_dms_no)
        posteriors.append(post)
    # Madhusudhan 2023: 2.4 sigma DMS tentative
    sigma_current = 2.4
    sigma_for_confirmation = 5.0
    # Effective likelihood: L scales with sigma confidence
    # P(signal real | sigma=2.4) ~ 1 - Phi(-2.4) ≈ 0.99 but noise allows false signal
    return {
        "priors": priors,
        "posteriors": posteriors,
        "prior_5pct_posterior": float(posteriors[2]),
        "L_dms_given_life": L_dms_life,
        "L_dms_given_no_life": L_dms_no,
        "current_sigma_K218b": sigma_current,
        "required_sigma_for_confirmation": sigma_for_confirmation,
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: RNA world dynamics
    ax = axes[0, 0]
    t = np.array(t1["t"])
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(t1["trajectories"])))
    for traj, c in zip(t1["trajectories"], colors):
        ax.plot(t, traj["K_t"], color=c, lw=2, label=f"K₀={traj['K0']}")
    ax.axhline(0.5, ls=":", color="black", alpha=0.5, label="K=0.5 (half-max)")
    ax.set_xlabel("Time (arbitrary units ~ Myr)")
    ax.set_ylabel("K_RNA (population)")
    ax.set_title(f"RNA world autocatalytic dynamics (k_rep={t1['k_rep']}, k_deg={t1['k_deg']})")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)

    # Panel 2: Cambrian explosion
    ax = axes[0, 1]
    times = np.array(t2["times_Ma_ago"])
    phyla = np.array(t2["phyla"])
    ax.plot(times, phyla, "o-", lw=2, color="#1f77b4", markersize=6)
    # Highlight Cambrian
    cambrian_mask = (times <= 541) & (times >= 485)
    ax.fill_between(times, 0, phyla, where=cambrian_mask,
                    color="red", alpha=0.3, label="Cambrian (541-485 Ma)")
    ax.set_xlabel("Million years ago")
    ax.set_ylabel("Cumulative number of phyla")
    ax.invert_xaxis()
    ax.set_title(f"Cambrian explosion | speedup factor = {t2['cambrian_speedup']:.0f}× over pre-Cambrian")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    # Annotate rates
    ax.text(0.55, 0.25, f"Pre-Cambrian: {t2['rate_pre_cambrian']:.3f} phyla/Myr\n"
                       f"Cambrian: {t2['rate_cambrian']:.3f} phyla/Myr\n"
                       f"Post-Cambrian: {t2['rate_post_cambrian']:.4f} phyla/Myr",
            transform=ax.transAxes, fontsize=7, bbox=dict(facecolor="white", alpha=0.7))

    # Panel 3: EQ vs K_self
    ax = axes[1, 0]
    animals = t3["animals"]
    EQ = np.array(t3["EQ_array"])
    K = np.array(t3["K_self_array"])
    colors = ["#1f77b4"] * 10 + ["#ff7f0e", "#d62728"]
    ax.loglog(EQ, K, "o", markersize=10, alpha=0.8)
    for a, c in zip(animals, colors):
        ax.scatter(a["EQ"], a["K_self"], s=200, color=c, alpha=0.85,
                   edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(a["name"], (a["EQ"], a["K_self"]), xytext=(5, 5),
                    textcoords="offset points", fontsize=7)
    # Fit line
    EQ_range = np.logspace(np.log10(0.1), np.log10(100), 50)
    K_fit = 10 ** (t3["log_log_slope"] * np.log10(EQ_range) + t3["log_log_intercept"])
    ax.loglog(EQ_range, K_fit, "k--", alpha=0.6, label=f"fit: slope={t3['log_log_slope']:.2f}")
    ax.set_xlabel("EQ (Encephalization Quotient)")
    ax.set_ylabel("K_self degree")
    ax.set_title(f"EQ vs K_self | log-log correlation r = {t3['log_log_correlation_r']:.3f}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # Panel 4: K2-18b Bayesian posterior
    ax = axes[1, 1]
    priors = np.array(t4["priors"])
    posteriors = np.array(t4["posteriors"])
    x_pos = np.arange(len(priors))
    width = 0.35
    ax.bar(x_pos - width/2, priors, width, color="#1f77b4", alpha=0.8,
           label="Prior P(life)", edgecolor="black", linewidth=0.5)
    ax.bar(x_pos + width/2, posteriors, width, color="#2ca02c", alpha=0.85,
           label="Posterior (after DMS signal)", edgecolor="black", linewidth=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f"{p:.1%}" if p >= 0.01 else f"{p*100:.1f}%" for p in priors])
    ax.set_xlabel("Prior P(life on K2-18b)")
    ax.set_ylabel("Probability")
    ax.set_title(f"K2-18b DMS Bayesian (Madhusudhan 2023, {t4['current_sigma_K218b']}σ tentative)\n"
                 f"Prior 5% → Posterior {t4['prior_5pct_posterior']*100:.0f}%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    plt.suptitle("Phase 89: Abiogenesis + intelligence emergence — K-state phase transitions",
                 fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 89: Abiogenesis + intelligence emergence")
    print("=" * 70)

    print("\n[Test 1] RNA world autocatalytic dynamics")
    t1 = test1_rna_world()
    for traj, t_half in zip(t1["trajectories"], t1["t_half_per_K0"]):
        t_str = f"{t_half:.2f}" if t_half is not None else "did not reach"
        print(f"  K_0={traj['K0']:.3f} → reaches K=0.5 at t={t_str}")

    print("\n[Test 2] Cambrian explosion")
    t2 = test2_cambrian()
    print(f"  Pre-Cambrian rate:   {t2['rate_pre_cambrian']:.3f} phyla/Myr")
    print(f"  Cambrian rate:       {t2['rate_cambrian']:.3f} phyla/Myr")
    print(f"  Post-Cambrian rate:  {t2['rate_post_cambrian']:.4f} phyla/Myr")
    print(f"  Cambrian speedup:    {t2['cambrian_speedup']:.0f}× over pre-Cambrian")

    print("\n[Test 3] EQ and K_self correlation")
    t3 = test3_eq_kself()
    for a in t3["animals"]:
        print(f"  {a['name']:20s}  EQ={a['EQ']:6.2f}  K_self={a['K_self']:.3f}")
    print(f"  log-log correlation r = {t3['log_log_correlation_r']:.3f}")
    print(f"  log-log slope:          {t3['log_log_slope']:.3f}")

    print("\n[Test 4] K2-18b DMS Bayesian posterior")
    t4 = test4_k218b()
    print(f"  L(DMS|life)={t4['L_dms_given_life']}, L(DMS|no life)={t4['L_dms_given_no_life']}")
    for p, post in zip(t4["priors"], t4["posteriors"]):
        print(f"  Prior {p*100:5.1f}% → Posterior {post*100:5.1f}%")
    print(f"  Current K2-18b: {t4['current_sigma_K218b']}σ (Madhusudhan 2023)")
    print(f"  Required for confirmation: {t4['required_sigma_for_confirmation']}σ")

    out = {
        "phase": 89,
        "title": "Abiogenesis + intelligence emergence — K-state phase transitions",
        "test1_rna_world": {
            "k_rep": t1["k_rep"], "k_deg": t1["k_deg"],
            "init_conditions": t1["init_conditions"],
            "t_half_per_K0": t1["t_half_per_K0"],
        },
        "test2_cambrian": t2,
        "test3_eq_kself": t3,
        "test4_k218b": t4,
    }
    with open("abiogenesis_intelligence_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: abiogenesis_intelligence_summary.json")

    make_figure(t1, t2, t3, t4, "abiogenesis_intelligence.png")
    print("  ✓ Figure saved: abiogenesis_intelligence.png")

    print("\n" + "=" * 70)
    print("Phase 89 complete: Cambrian speedup={:.0f}×, EQ-K_self r={:.2f}, K2-18b 5%->{:.0f}%"
          .format(t2["cambrian_speedup"], t3["log_log_correlation_r"], t4["prior_5pct_posterior"]*100))
    print("=" * 70)
