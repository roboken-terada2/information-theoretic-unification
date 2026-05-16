"""
Phase 87: ITU Astrobiology / SETI foundation
Tier 1 #12 — Phase 1/4

4 numerical experiments:
1. K_life information content scale (virus -> AGI)
2. Drake equation Monte Carlo with ITU priors
3. Habitability Index for known exoplanets
4. Fermi paradox: 12 hypotheses with ITU probability weighting

Output: astrobiology_itu_foundation.png + astrobiology_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Test 1: K_life information content (life -> civilization scale)
# ----------------------------------------------------------------------
def test1_k_life_scale():
    organisms = [
        {"name": "Virus (HIV)",          "bits": 1.0e4,  "category": "virus"},
        {"name": "Bacteria (E.coli)",    "bits": 1.0e7,  "category": "single-cell"},
        {"name": "Fungi (yeast)",        "bits": 1.0e8,  "category": "single-cell"},
        {"name": "Plant (Arabidopsis)",  "bits": 3.0e8,  "category": "multi-cell"},
        {"name": "Fly (Drosophila)",     "bits": 5.0e8,  "category": "animal"},
        {"name": "Mouse",                "bits": 5.0e9,  "category": "animal"},
        {"name": "Human (DNA)",          "bits": 1.0e10, "category": "animal"},
        {"name": "Human (brain syn.)",   "bits": 1.0e15, "category": "neural"},
        {"name": "All human knowledge",  "bits": 1.0e22, "category": "civilization"},
        {"name": "AGI (2030)",           "bits": 1.0e24, "category": "AI"},
        {"name": "ASI (2035)",           "bits": 1.0e26, "category": "AI"},
    ]
    log_bits = [math.log10(o["bits"]) for o in organisms]
    return {
        "organisms": organisms,
        "log_bits": log_bits,
        "range_log10": float(max(log_bits) - min(log_bits)),
    }


# ----------------------------------------------------------------------
# Test 2: Drake equation Monte Carlo
# ----------------------------------------------------------------------
def test2_drake_monte_carlo():
    """ITU prior distributions for each Drake factor."""
    rng = np.random.default_rng(42)
    n = 100000
    # Star formation rate (per year) — Robitaille & Whitney 2010
    R_star = rng.lognormal(mean=math.log(2.0), sigma=0.3, size=n)
    # Fraction with planets — Kepler
    f_p = rng.beta(8, 2, size=n)  # ~0.8
    # Habitable planets per system — Petigura 2013
    n_e = rng.lognormal(mean=math.log(0.4), sigma=0.5, size=n)
    # Life origin probability — broadest range
    f_l = rng.lognormal(mean=math.log(0.01), sigma=2.0, size=n)
    f_l = np.clip(f_l, 1e-10, 1.0)
    # Intelligence emergence
    f_i = rng.lognormal(mean=math.log(0.1), sigma=1.5, size=n)
    f_i = np.clip(f_i, 1e-6, 1.0)
    # Communication
    f_c = rng.beta(2, 2, size=n)  # ~0.5
    # Civilization lifetime (years)
    L = rng.lognormal(mean=math.log(1000), sigma=1.5, size=n)
    # Drake equation
    N = R_star * f_p * n_e * f_l * f_i * f_c * L
    return {
        "n_samples": int(n),
        "N_median": float(np.median(N)),
        "N_mean": float(np.mean(N)),
        "N_16pct": float(np.percentile(N, 16)),
        "N_84pct": float(np.percentile(N, 84)),
        "N_1pct": float(np.percentile(N, 1)),
        "N_99pct": float(np.percentile(N, 99)),
        "frac_zero": float(np.mean(N < 1)),
        "factors_median": {
            "R_star": float(np.median(R_star)),
            "f_p": float(np.median(f_p)),
            "n_e": float(np.median(n_e)),
            "f_l": float(np.median(f_l)),
            "f_i": float(np.median(f_i)),
            "f_c": float(np.median(f_c)),
            "L": float(np.median(L)),
        },
        "N_samples_subset": np.log10(np.clip(N, 1e-6, 1e12))[:5000].tolist(),
    }


# ----------------------------------------------------------------------
# Test 3: Habitability Index for known exoplanets
# ----------------------------------------------------------------------
def habitability_index(T_eff, M_star_type, distance_au, mass_earth=1.0, atmosphere=True):
    """Simplified HI: combine temperature score, stellar score, mass."""
    # Temperature score (peak at 288 K)
    T_score = math.exp(-((T_eff - 288.0) / 80.0) ** 2)
    # Stellar score (G > K > M for life; M has flares but smaller habitable zone)
    star_scores = {"G": 1.0, "K": 0.85, "M": 0.60, "F": 0.75}
    S_score = star_scores.get(M_star_type, 0.5)
    # Mass score (Earth-like)
    log_mass = math.log10(mass_earth)
    M_score = math.exp(-(log_mass / 0.5) ** 2)
    # Atmosphere factor
    A_score = 1.0 if atmosphere else 0.3
    return float(T_score * S_score * M_score * A_score)


def test3_exoplanets():
    planets = [
        {"name": "Earth",         "T_eff": 288, "star": "G", "dist_au": 1.0,    "mass": 1.0,  "atm": True},
        {"name": "Mars",          "T_eff": 210, "star": "G", "dist_au": 1.52,   "mass": 0.11, "atm": False},
        {"name": "Venus",         "T_eff": 737, "star": "G", "dist_au": 0.72,   "mass": 0.82, "atm": True},
        {"name": "TRAPPIST-1e",   "T_eff": 246, "star": "M", "dist_au": 0.029,  "mass": 0.69, "atm": True},
        {"name": "Proxima b",     "T_eff": 234, "star": "M", "dist_au": 0.0485, "mass": 1.27, "atm": True},
        {"name": "Kepler-452b",   "T_eff": 265, "star": "G", "dist_au": 1.046,  "mass": 5.0,  "atm": True},
        {"name": "TOI-700d",      "T_eff": 268, "star": "M", "dist_au": 0.163,  "mass": 1.72, "atm": True},
        {"name": "K2-18b",        "T_eff": 270, "star": "M", "dist_au": 0.143,  "mass": 8.6,  "atm": True},
        {"name": "LHS 1140b",     "T_eff": 230, "star": "M", "dist_au": 0.0875, "mass": 5.6,  "atm": True},
        {"name": "Teegarden b",   "T_eff": 273, "star": "M", "dist_au": 0.0252, "mass": 1.05, "atm": True},
    ]
    out = []
    for p in planets:
        hi = habitability_index(p["T_eff"], p["star"], p["dist_au"], p["mass"], p["atm"])
        out.append({**p, "HI": hi})
    out_sorted = sorted(out, key=lambda x: -x["HI"])
    return {"planets": out, "ranked": out_sorted, "top3": out_sorted[:3]}


# ----------------------------------------------------------------------
# Test 4: Fermi paradox hypotheses with ITU weighting
# ----------------------------------------------------------------------
def test4_fermi():
    hypotheses = [
        {"id": 1,  "name": "Great Filter (past)",      "p": 0.40, "K_axis": "K_complexity threshold"},
        {"id": 2,  "name": "Great Filter (future)",    "p": 0.25, "K_axis": "K_self_destruction"},
        {"id": 3,  "name": "Rare Earth",                "p": 0.15, "K_axis": "K_nucleation rare"},
        {"id": 4,  "name": "Dark Forest",               "p": 0.08, "K_axis": "K_strategic silence"},
        {"id": 5,  "name": "Zoo Hypothesis",            "p": 0.03, "K_axis": "K_ethics constraint"},
        {"id": 6,  "name": "Detection limit below",     "p": 0.03, "K_axis": "K-flux insufficient"},
        {"id": 7,  "name": "Channel mismatch",          "p": 0.02, "K_axis": "K-signal channel"},
        {"id": 8,  "name": "Civilization short L",      "p": 0.01, "K_axis": "K_stability"},
        {"id": 9,  "name": "Already came & left",       "p": 0.01, "K_axis": "K_history"},
        {"id": 10, "name": "We are first",              "p": 0.01, "K_axis": "K_pioneer"},
        {"id": 11, "name": "Simulation inside",         "p": 0.005,"K_axis": "K_meta"},
        {"id": 12, "name": "Higher dimensions",         "p": 0.005,"K_axis": "K_higher_dim"},
    ]
    p_total = sum(h["p"] for h in hypotheses)
    p_filter = hypotheses[0]["p"] + hypotheses[1]["p"]
    return {
        "hypotheses": hypotheses,
        "p_total": float(p_total),
        "p_great_filter_combined": float(p_filter),
        "n_hypotheses": len(hypotheses),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: K_life information scale
    ax = axes[0, 0]
    names = [o["name"] for o in t1["organisms"]]
    log_bits = t1["log_bits"]
    cats = [o["category"] for o in t1["organisms"]]
    cat_color = {"virus": "#9467bd", "single-cell": "#1f77b4",
                 "multi-cell": "#2ca02c", "animal": "#ff7f0e",
                 "neural": "#d62728", "civilization": "#8c564b",
                 "AI": "#e377c2"}
    colors = [cat_color[c] for c in cats]
    y_pos = np.arange(len(names))
    ax.barh(y_pos, log_bits, color=colors, alpha=0.8, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("log10(bits)")
    ax.set_title(f"K_life information content | range = {t1['range_log10']:.1f} orders of magnitude")
    ax.grid(alpha=0.3, axis="x")

    # Panel 2: Drake equation Monte Carlo
    ax = axes[0, 1]
    log_N = np.array(t2["N_samples_subset"])
    ax.hist(log_N, bins=60, color="#1f77b4", alpha=0.7, edgecolor="black", linewidth=0.3)
    ax.axvline(math.log10(max(t2["N_median"], 1e-6)), color="red", ls="--", lw=2,
               label=f"median N={t2['N_median']:.1f}")
    ax.axvline(0, color="black", ls=":", lw=1, label="N=1 (single civ)")
    ax.set_xlabel("log10(N) — civilizations per galaxy")
    ax.set_ylabel("Count")
    ax.set_title(f"Drake Monte Carlo | N median={t2['N_median']:.1f}, P(N<1)={t2['frac_zero']*100:.0f}%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3: Habitability Index
    ax = axes[1, 0]
    planets = t3["ranked"]
    names = [p["name"] for p in planets]
    hi = [p["HI"] for p in planets]
    star_colors = {"G": "#ffd700", "K": "#ff8c00", "M": "#dc143c", "F": "#ffffff"}
    colors = [star_colors.get(p["star"], "gray") for p in planets]
    y_pos = np.arange(len(planets))
    bars = ax.barh(y_pos, hi, color=colors, alpha=0.85, edgecolor="black", linewidth=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Habitability Index (0-1)")
    ax.set_xlim(0, 1.0)
    top3 = ", ".join(p["name"] for p in t3["top3"])
    ax.set_title(f"HI for known exoplanets | Top 3 (excl. Earth): {top3.replace('Earth, ', '')}")
    ax.grid(alpha=0.3, axis="x")
    # Annotate stars
    for i, p in enumerate(planets):
        ax.text(hi[i] + 0.01, i, p["star"], fontsize=8, va="center")

    # Panel 4: Fermi paradox hypotheses
    ax = axes[1, 1]
    hyps = t4["hypotheses"]
    names = [h["name"] for h in hyps]
    probs = [h["p"] for h in hyps]
    colors = ["#d62728" if h["id"] <= 2 else "#ff7f0e" if h["id"] <= 4 else "#1f77b4" for h in hyps]
    y_pos = np.arange(len(hyps))
    ax.barh(y_pos, probs, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel("Probability (ITU prior)")
    ax.set_title(f"Fermi paradox solutions | Great Filter combined = {t4['p_great_filter_combined']*100:.0f}%")
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 87: ITU × Astrobiology / SETI — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 87: ITU × Astrobiology / SETI — foundation")
    print("=" * 70)

    print("\n[Test 1] K_life information content")
    t1 = test1_k_life_scale()
    for o, lb in zip(t1["organisms"], t1["log_bits"]):
        print(f"  {o['name']:30s}  log10(bits)={lb:5.1f}  [{o['category']}]")
    print(f"  Range: {t1['range_log10']:.1f} orders of magnitude")

    print("\n[Test 2] Drake equation Monte Carlo")
    t2 = test2_drake_monte_carlo()
    print(f"  N samples: {t2['n_samples']:,}")
    print(f"  N median:  {t2['N_median']:.2f}")
    print(f"  N mean:    {t2['N_mean']:.2f}")
    print(f"  N 16-84%:  [{t2['N_16pct']:.3f}, {t2['N_84pct']:.3f}]")
    print(f"  P(N < 1):  {t2['frac_zero']*100:.0f}%  (alone in galaxy)")
    print(f"  Factors (median):")
    for k, v in t2["factors_median"].items():
        print(f"    {k:8s} = {v:.4f}")

    print("\n[Test 3] Habitability Index — exoplanets")
    t3 = test3_exoplanets()
    for p in t3["ranked"]:
        print(f"  {p['name']:20s}  T={p['T_eff']:3d}K  star={p['star']}  mass={p['mass']:.2f}M_E  HI={p['HI']:.3f}")
    print(f"\n  Top 3 (excl. Earth): {[p['name'] for p in t3['top3'] if p['name'] != 'Earth'][:3]}")

    print("\n[Test 4] Fermi paradox — 12 hypotheses")
    t4 = test4_fermi()
    for h in t4["hypotheses"]:
        print(f"  H{h['id']:2d}: {h['name']:32s}  p={h['p']:.3f}  ({h['K_axis']})")
    print(f"  Great Filter combined: {t4['p_great_filter_combined']*100:.0f}%")

    out = {
        "phase": 87,
        "title": "ITU × Astrobiology / SETI — foundation",
        "test1_k_life": t1,
        "test2_drake": t2,
        "test3_habitability": t3,
        "test4_fermi": t4,
    }
    with open("astrobiology_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: astrobiology_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "astrobiology_itu_foundation.png")
    print("  ✓ Figure saved: astrobiology_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 87 complete: K_life={:.0f} orders, Drake N={:.1f}, top exoplanet HI={:.2f}, GreatFilter={:.0f}%"
          .format(t1["range_log10"], t2["N_median"],
                  max(p["HI"] for p in t3["planets"] if p["name"] != "Earth"),
                  t4["p_great_filter_combined"]*100))
    print("=" * 70)
