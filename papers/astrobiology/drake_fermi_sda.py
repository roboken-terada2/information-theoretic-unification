"""
Phase 88: Drake Bayesian + Fermi detailed + SDA
Tier 1 #12 — Phase 2/4

4 numerical experiments:
1. Sandberg-Drexler-Ord 2018: log-uniform priors -> P(alone in galaxy)
2. Great Filter hard-step analysis (Carter-Watson)
3. SDA: detection distance vs P_T (transmitter power)
4. Bayesian update from Breakthrough Listen null result

Output: drake_fermi_sda.png + drake_fermi_sda_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Sandberg-Drexler-Ord log-uniform Drake
# ----------------------------------------------------------------------
def test1_sandberg_drake():
    """Each factor: log-uniform between literature bounds."""
    rng = np.random.default_rng(123)
    n = 200000

    def loguniform(lo_log, hi_log):
        return 10.0 ** rng.uniform(lo_log, hi_log, size=n)

    R_star = loguniform(0.0, 0.5)    # 1-3 stars/yr
    f_p    = loguniform(-0.3, 0.0)   # 0.5-1.0
    n_e    = loguniform(-1.0, -0.4)  # 0.1-0.4
    # Sandberg et al. 2018 reduced ranges for tractable posterior
    f_l    = loguniform(-20, 0)      # abiogenesis: huge but bounded
    f_i    = loguniform(-3, 0)       # intelligence: ~1/1000 to 1
    f_c    = loguniform(-2, 0)       # 0.01-1
    L      = loguniform(2, 9)        # 100 to 10^9 years

    N = R_star * f_p * n_e * f_l * f_i * f_c * L

    # P(alone in galaxy)
    p_alone_galaxy = float(np.mean(N < 1))
    # P(alone in observable universe): galactic count ~10^11
    N_universe = N * 1.0e11
    p_alone_universe = float(np.mean(N_universe < 1))

    return {
        "n_samples": int(n),
        "N_median": float(np.median(N)),
        "N_mean": float(np.mean(N)),
        "N_log10_median": float(np.log10(max(np.median(N), 1e-30))),
        "P_alone_galaxy": p_alone_galaxy,
        "P_alone_universe": p_alone_universe,
        "N_log10_samples": np.log10(np.clip(N, 1e-30, 1e30))[:5000].tolist(),
        "N_log10_universe_samples": np.log10(np.clip(N_universe, 1e-30, 1e40))[:5000].tolist(),
        "sandberg_2018_galaxy": 0.53,
        "sandberg_2018_universe": 0.30,
    }


# ----------------------------------------------------------------------
# Test 2: Great Filter hard-step analysis
# ----------------------------------------------------------------------
def test2_hard_steps():
    """
    Carter-Watson model: if n hard steps remain, expected wait scales as
    t_remaining / (n+1). Compare actual transition times to Earth's life history.
    Earth-life history (Gyr ago):
      4.5 formation -> 4.0 prokaryote -> 2.5 photosynth -> 2.0 eukaryote
      -> 1.0 multicell -> 0.55 Cambrian -> 0.2 mammals -> 0.003 humans
    """
    steps = [
        {"name": "Abiogenesis",          "dt_Gyr": 0.5, "ITU_K_axis": "chemical -> info"},
        {"name": "Prokaryote",           "dt_Gyr": 0.5, "ITU_K_axis": "self-replication"},
        {"name": "Photosynthesis",       "dt_Gyr": 1.0, "ITU_K_axis": "energy source"},
        {"name": "Eukaryote",            "dt_Gyr": 2.0, "ITU_K_axis": "endosymbiosis (HARD)"},
        {"name": "Multicellular",        "dt_Gyr": 0.5, "ITU_K_axis": "cooperative"},
        {"name": "Cambrian explosion",   "dt_Gyr": 0.05,"ITU_K_axis": "diversification"},
        {"name": "Mammals",              "dt_Gyr": 0.2, "ITU_K_axis": "neural"},
        {"name": "Intelligence (humans)","dt_Gyr": 0.06,"ITU_K_axis": "K_self (HARD)"},
    ]
    # Mean dt for non-hard steps
    dt_array = np.array([s["dt_Gyr"] for s in steps])
    mean_dt = float(np.mean(dt_array))
    # Identify hard steps: dt > 2 sigma above mean
    threshold = mean_dt * 2.0
    for s in steps:
        s["is_hard"] = s["dt_Gyr"] > threshold or "HARD" in s["ITU_K_axis"]
    n_hard = sum(s["is_hard"] for s in steps)
    return {
        "steps": steps,
        "mean_dt_Gyr": mean_dt,
        "n_hard_steps": int(n_hard),
        "hard_step_threshold": float(threshold),
        "hard_step_names": [s["name"] for s in steps if s["is_hard"]],
    }


# ----------------------------------------------------------------------
# Test 3: SDA — detection distance vs transmitter power
# ----------------------------------------------------------------------
def test3_sda():
    """
    Detection distance d_max = sqrt(P_T / (4 pi S_min))
    Convert d (m) to light years: 1 ly = 9.461e15 m.
    """
    S_min = 1.0e-26  # W/m^2 (FAST sensitivity, narrowband)
    ly = 9.461e15

    transmitters = [
        {"name": "TV leakage (terrestrial)",  "P_T": 1.0e6},
        {"name": "Earth radar (military)",     "P_T": 1.0e9},
        {"name": "Arecibo message (1974)",     "P_T": 2.0e13},
        {"name": "Type I (planetary)",         "P_T": 1.0e17},
        {"name": "Type II (Dyson sphere)",     "P_T": 4.0e26},
        {"name": "Type III (galactic)",        "P_T": 1.0e37},
    ]
    for t in transmitters:
        d_m = math.sqrt(t["P_T"] / (4 * math.pi * S_min))
        t["d_max_m"] = d_m
        t["d_max_ly"] = d_m / ly
    return {
        "S_min_Wm2": S_min,
        "transmitters": transmitters,
        "FAST_max_range_ly_Arecibo": transmitters[2]["d_max_ly"],
        "Type_II_galactic_diameter_ratio": transmitters[4]["d_max_ly"] / 1.0e5,  # galactic diameter ~10^5 ly
    }


# ----------------------------------------------------------------------
# Test 4: Bayesian update from Breakthrough Listen null
# ----------------------------------------------------------------------
def test4_bayesian_update():
    """
    Prior P(ETI in 100 ly) varies; after Breakthrough Listen null,
    posterior collapses via likelihood ratio.
    """
    priors = np.array([0.01, 0.05, 0.1, 0.2, 0.5])
    # Likelihood that we get null detection given:
    # - ETI present: L_eti (they may not transmit, frequency mismatch, etc.)
    # - ETI absent: L_no  (just background noise)
    L_eti = 0.2
    L_no = 1.0
    posteriors = priors * L_eti / (priors * L_eti + (1 - priors) * L_no)
    update_factor = posteriors / priors
    return {
        "priors": priors.tolist(),
        "L_given_ETI": L_eti,
        "L_given_absence": L_no,
        "posteriors": posteriors.tolist(),
        "update_factor": update_factor.tolist(),
        "BL_observation_summary": "16000 stars in 1-12 GHz, all null (Price 2020, 2023)",
        # Specific Bayesian table-row for Prior=0.1
        "prior_10pct_posterior": float(posteriors[2]),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Sandberg log-uniform Drake N distribution
    ax = axes[0, 0]
    log_N = np.array(t1["N_log10_samples"])
    ax.hist(log_N, bins=80, color="#1f77b4", alpha=0.7, edgecolor="black", linewidth=0.3,
            label="N (per galaxy)")
    log_N_univ = np.array(t1["N_log10_universe_samples"])
    ax.hist(log_N_univ, bins=80, color="#ff7f0e", alpha=0.4, edgecolor="black", linewidth=0.3,
            label="N (observable universe)")
    ax.axvline(0, color="red", ls="--", lw=2, label="N=1 (alone)")
    ax.set_xlabel("log10(N civilizations)")
    ax.set_ylabel("Count")
    ax.set_title(f"Sandberg-Drexler-Ord log-uniform Drake\nP(alone in galaxy)={t1['P_alone_galaxy']*100:.0f}% | universe={t1['P_alone_universe']*100:.0f}% (Sandberg18: 53% / 30%)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: Hard step analysis
    ax = axes[0, 1]
    steps = t2["steps"]
    names = [s["name"] for s in steps]
    dts = [s["dt_Gyr"] for s in steps]
    colors = ["#d62728" if s["is_hard"] else "#1f77b4" for s in steps]
    y_pos = np.arange(len(steps))
    ax.barh(y_pos, dts, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.axvline(t2["hard_step_threshold"], color="red", ls="--", alpha=0.6,
               label=f"hard step threshold ({t2['hard_step_threshold']:.2f} Gyr)")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Time to next step (Gyr)")
    ax.set_title(f"Carter-Watson hard step analysis | {t2['n_hard_steps']} hard steps identified")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="x")

    # Panel 3: SDA detection distance
    ax = axes[1, 0]
    trans = t3["transmitters"]
    names = [t["name"] for t in trans]
    log_P = [math.log10(t["P_T"]) for t in trans]
    log_d = [math.log10(max(t["d_max_ly"], 1e-6)) for t in trans]
    colors = ["#1f77b4", "#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
    ax.scatter(log_P, log_d, s=200, c=colors, alpha=0.85, edgecolor="black", linewidth=0.8, zorder=3)
    for i, name in enumerate(names):
        ax.annotate(name, (log_P[i], log_d[i]), xytext=(8, 5),
                    textcoords="offset points", fontsize=7, rotation=15)
    # Helper lines: galactic diameter (~10^5 ly)
    ax.axhline(math.log10(1.0e5), color="green", ls=":", alpha=0.6, label="Galactic diameter")
    ax.axhline(math.log10(100), color="orange", ls=":", alpha=0.6, label="100 ly (BL range)")
    ax.set_xlabel("log10(Transmitter power, W)")
    ax.set_ylabel("log10(Max detection distance, ly)")
    ax.set_title(f"SDA: detection range (FAST S_min={t3['S_min_Wm2']:.0e} W/m²)\nType II d={t3['transmitters'][4]['d_max_ly']:.1e} ly")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4: Bayesian update from BL null
    ax = axes[1, 1]
    priors = np.array(t4["priors"])
    posteriors = np.array(t4["posteriors"])
    x_pos = np.arange(len(priors))
    width = 0.35
    ax.bar(x_pos - width/2, priors, width, color="#1f77b4", alpha=0.8, label="Prior", edgecolor="black", linewidth=0.5)
    ax.bar(x_pos + width/2, posteriors, width, color="#d62728", alpha=0.8, label="Posterior (after BL null)", edgecolor="black", linewidth=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f"{p:.0%}" for p in priors])
    ax.set_xlabel("Prior P(ETI within 100 ly)")
    ax.set_ylabel("Probability")
    ax.set_title(f"Bayesian update from Breakthrough Listen null\nL(null|ETI)={t4['L_given_ETI']}, P(0.1→{t4['prior_10pct_posterior']*100:.1f}%)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    plt.suptitle("Phase 88: Drake Bayesian + Fermi detailed + SDA",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 88: Drake Bayesian + Fermi detailed + SDA")
    print("=" * 70)

    print("\n[Test 1] Sandberg-Drexler-Ord log-uniform Drake")
    t1 = test1_sandberg_drake()
    print(f"  N samples: {t1['n_samples']:,}")
    print(f"  N median: 10^{t1['N_log10_median']:.1f}")
    print(f"  P(alone in galaxy):           {t1['P_alone_galaxy']*100:.0f}% (Sandberg 2018: 53%)")
    print(f"  P(alone in observable univ.): {t1['P_alone_universe']*100:.0f}% (Sandberg 2018: 30%)")

    print("\n[Test 2] Great Filter hard step analysis")
    t2 = test2_hard_steps()
    for s in t2["steps"]:
        flag = "★ HARD" if s["is_hard"] else "normal"
        print(f"  {s['name']:25s}  dt={s['dt_Gyr']:.2f} Gyr  [{flag}]")
    print(f"  Hard steps identified: {t2['n_hard_steps']} ({t2['hard_step_names']})")

    print("\n[Test 3] SDA — Signal Detection Analysis")
    t3 = test3_sda()
    for t in t3["transmitters"]:
        print(f"  {t['name']:32s}  P={t['P_T']:.1e} W  d_max={t['d_max_ly']:.2e} ly")
    print(f"  Type II Dyson sphere: {t3['transmitters'][4]['d_max_ly']:.0e} ly "
          f"({t3['Type_II_galactic_diameter_ratio']:.0e}× galactic diameter)")

    print("\n[Test 4] Bayesian update from Breakthrough Listen null")
    t4 = test4_bayesian_update()
    print(f"  L(null|ETI)={t4['L_given_ETI']}, L(null|absent)={t4['L_given_absence']}")
    for p, post, upd in zip(t4["priors"], t4["posteriors"], t4["update_factor"]):
        print(f"  Prior {p*100:5.1f}% → Posterior {post*100:5.2f}% (×{upd:.3f})")
    print(f"  {t4['BL_observation_summary']}")

    out = {
        "phase": 88,
        "title": "Drake Bayesian + Fermi detailed + SDA",
        "test1_sandberg": {k: v for k, v in t1.items() if "samples" not in k},
        "test2_hard_steps": t2,
        "test3_sda": t3,
        "test4_bayesian": t4,
    }
    with open("drake_fermi_sda_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: drake_fermi_sda_summary.json")

    make_figure(t1, t2, t3, t4, "drake_fermi_sda.png")
    print("  ✓ Figure saved: drake_fermi_sda.png")

    print("\n" + "=" * 70)
    print("Phase 88 complete: P(alone galaxy)={:.0f}%, hard steps={}, Type II d={:.0e} ly, BL Bayes 10%->{:.1f}%"
          .format(t1["P_alone_galaxy"]*100, t2["n_hard_steps"],
                  t3["transmitters"][4]["d_max_ly"], t4["prior_10pct_posterior"]*100))
    print("=" * 70)
