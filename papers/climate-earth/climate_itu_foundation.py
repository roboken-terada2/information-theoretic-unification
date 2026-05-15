"""
Phase 83: ITU Climate / Earth Systems foundation
Tier 1 #11 — Phase 1/4

4 numerical experiments:
1. CO2 ppm history (1750-2024) + radiative forcing ΔF(t)
2. Earth Energy Imbalance (EEI) 1970-2024 ⇒ heat accumulation
3. ECS posterior: observation vs IPCC AR6 prior
4. Planetary Boundaries 9-axis state (radar-style summary)

Output: climate_itu_foundation.png + climate_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Physical constants
# ----------------------------------------------------------------------
S0 = 1361.0  # solar constant W/m^2
ALPHA_BOND = 0.293  # Bond albedo
A_EARTH = 5.1e14  # m^2
SIGMA_SB = 5.670374419e-8  # Stefan-Boltzmann
CO2_PRE = 280.0  # ppm pre-industrial
DF_2XCO2 = 3.93  # W/m^2 IPCC AR6 (2x CO2)


# ----------------------------------------------------------------------
# Test 1: CO2 history + radiative forcing
# ----------------------------------------------------------------------
def co2_ppm(year):
    """Mauna Loa / ice-core merged record approximation."""
    if year < 1750:
        return 278.0
    # Logistic ramp 1750-2024
    anchors = [
        (1750, 278), (1850, 285), (1900, 295), (1950, 311),
        (1960, 317), (1970, 326), (1980, 339), (1990, 354),
        (2000, 369), (2010, 389), (2020, 414), (2024, 422),
    ]
    yrs = np.array([a[0] for a in anchors])
    pp = np.array([a[1] for a in anchors])
    if year >= 2024:
        return 422.0
    return float(np.interp(year, yrs, pp))


def radiative_forcing_co2(ppm):
    """IPCC AR6 simplified: dF = 5.35 * ln(C/C0)"""
    return 5.35 * math.log(ppm / CO2_PRE)


def test1_co2_history():
    years = np.arange(1750, 2025)
    ppm = np.array([co2_ppm(y) for y in years])
    df = np.array([radiative_forcing_co2(p) for p in ppm])
    return {
        "years": years.tolist(),
        "ppm": ppm.tolist(),
        "df_Wm2": df.tolist(),
        "ppm_2024": float(ppm[-1]),
        "df_2024_Wm2": float(df[-1]),
        "df_2xCO2_IPCC_AR6_Wm2": DF_2XCO2,
    }


# ----------------------------------------------------------------------
# Test 2: Earth Energy Imbalance 1970-2024
# ----------------------------------------------------------------------
def eei_history(year):
    """EEI in W/m^2, approximation from von Schuckmann et al. (2023) + CERES."""
    # Roughly linear ramp 1970(0.2) -> 1990(0.5) -> 2010(0.8) -> 2024(1.0)
    anchors = [(1970, 0.20), (1980, 0.32), (1990, 0.50),
               (2000, 0.65), (2010, 0.82), (2020, 0.95), (2024, 1.00)]
    yrs = np.array([a[0] for a in anchors])
    ev = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, ev))


def test2_eei():
    years = np.arange(1970, 2025)
    eei = np.array([eei_history(y) for y in years])
    # Total power gained (TW)
    power_TW = eei * A_EARTH / 1e12
    # Cumulative heat ZJ (1 ZJ = 1e21 J), assume 1 yr = 3.156e7 s
    dt = 3.156e7
    cum_J = np.cumsum(eei * A_EARTH * dt)
    cum_ZJ = cum_J / 1e21
    return {
        "years": years.tolist(),
        "eei_Wm2": eei.tolist(),
        "power_TW": power_TW.tolist(),
        "cumulative_heat_ZJ": cum_ZJ.tolist(),
        "eei_2024_Wm2": float(eei[-1]),
        "power_2024_TW": float(power_TW[-1]),
        "cumulative_ZJ_2024": float(cum_ZJ[-1]),
        "human_primary_energy_TW_2024": 18.0,
        "earth_to_human_ratio": float(power_TW[-1] / 18.0),
    }


# ----------------------------------------------------------------------
# Test 3: ECS posterior from observation
# ----------------------------------------------------------------------
def test3_ecs_posterior():
    """
    Naive estimator: ECS = ΔT_obs / ΔF_obs * ΔF_2xCO2 * efficacy.
    With T(1970-2024) = +1.3 K, ΔF(1970-2024) ≈ F(2024)-F(1970).
    """
    dT_obs = 1.3  # K
    df_1970 = radiative_forcing_co2(co2_ppm(1970))
    df_2024 = radiative_forcing_co2(co2_ppm(2024))
    # Include non-CO2 contributions ~1.0 W/m^2 over the period
    df_total = (df_2024 - df_1970) + 1.0
    # Heat going into ocean ⇒ effective forcing for atmosphere ≈ df_total - eei_avg
    eei_avg = 0.6
    df_eff = df_total - eei_avg
    lam = df_eff / dT_obs  # W/m^2/K
    ecs_obs = DF_2XCO2 / lam

    # IPCC AR6 prior: lognormal ~3 K, [2.5, 4.0]_66%
    rng = np.random.default_rng(42)
    prior = rng.lognormal(mean=math.log(3.0), sigma=0.18, size=10000)
    # Observation likelihood centered on ecs_obs ± 0.5 K
    weights = np.exp(-0.5 * ((prior - ecs_obs) / 0.6) ** 2)
    weights /= weights.sum()
    posterior = rng.choice(prior, size=10000, p=weights, replace=True)
    p16, p50, p84 = np.percentile(posterior, [16, 50, 84])
    return {
        "dT_obs_K": dT_obs,
        "df_total_Wm2": float(df_total),
        "eei_avg_Wm2": eei_avg,
        "lambda_Wm2_K": float(lam),
        "ecs_observation_estimate_K": float(ecs_obs),
        "ipcc_ar6_central_K": 3.0,
        "ipcc_ar6_66pct_K": [2.5, 4.0],
        "posterior_median_K": float(p50),
        "posterior_66pct_K": [float(p16), float(p84)],
        "prior_samples": prior.tolist()[:200],
        "posterior_samples": posterior.tolist()[:200],
    }


# ----------------------------------------------------------------------
# Test 4: Planetary Boundaries radar
# ----------------------------------------------------------------------
def test4_planetary_boundaries():
    """
    Each axis: normalized severity ratio (>=1.0 means breach).
    Rockström 2009 + 2023 update.
    """
    boundaries = [
        {"name": "Climate change",          "ratio": 422 / 350, "breached": True},
        {"name": "Biosphere integrity",     "ratio": 100 / 10,  "breached": True},
        {"name": "Biogeochemical N",        "ratio": 120 / 62,  "breached": True},
        {"name": "Biogeochemical P",        "ratio": 14 / 6,    "breached": True},
        {"name": "Land-system change",      "ratio": (100 - 60) / (100 - 75), "breached": True},
        {"name": "Freshwater (blue+green)", "ratio": 1.2,       "breached": True},
        {"name": "Ocean acidification",     "ratio": 0.10 / 0.20, "breached": False},
        {"name": "Ozone depletion",         "ratio": 0.30,      "breached": False},
        {"name": "Atmospheric aerosols",    "ratio": 0.85,      "breached": False},
        {"name": "Novel entities (PFAS+)",  "ratio": 1.8,       "breached": True},
    ]
    n_breached = sum(1 for b in boundaries if b["breached"])
    return {
        "boundaries": boundaries,
        "n_total": len(boundaries),
        "n_breached": n_breached,
        "fraction_breached": n_breached / len(boundaries),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # Panel 1: CO2 + ΔF
    ax = axes[0, 0]
    yrs = np.array(t1["years"])
    ax.plot(yrs, t1["ppm"], "k-", lw=2, label="CO$_2$ ppm")
    ax.axhline(350, ls="--", color="red", alpha=0.6, label="Planetary boundary (350 ppm)")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO$_2$ (ppm)")
    ax.set_title(f"CO$_2$ history: 278 → {t1['ppm_2024']:.0f} ppm | $\\Delta F$={t1['df_2024_Wm2']:.2f} W/m$^2$")
    ax2 = ax.twinx()
    ax2.plot(yrs, t1["df_Wm2"], "orange", lw=1.5, alpha=0.7, label="$\\Delta F$ W/m$^2$")
    ax2.set_ylabel("$\\Delta F$ (W/m$^2$)", color="orange")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 2: EEI + cumulative heat
    ax = axes[0, 1]
    yrs = np.array(t2["years"])
    ax.plot(yrs, t2["eei_Wm2"], "b-", lw=2, label="EEI (W/m$^2$)")
    ax.set_xlabel("Year")
    ax.set_ylabel("EEI (W/m$^2$)", color="b")
    ax.set_ylim(0, 1.2)
    ax.set_title(f"EEI: 0.2 → {t2['eei_2024_Wm2']:.2f} W/m$^2$ | {t2['power_2024_TW']:.0f} TW (= {t2['earth_to_human_ratio']:.0f}× humans)")
    ax3 = ax.twinx()
    ax3.fill_between(yrs, t2["cumulative_heat_ZJ"], color="red", alpha=0.3, label="Cumulative ZJ")
    ax3.set_ylabel("Cumulative heat (ZJ)", color="red")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")

    # Panel 3: ECS posterior
    ax = axes[1, 0]
    bins = np.linspace(1, 6, 50)
    ax.hist(np.array(t3["prior_samples"]), bins=bins, alpha=0.4, color="gray",
            label="Prior (IPCC AR6)", density=True)
    ax.hist(np.array(t3["posterior_samples"]), bins=bins, alpha=0.6, color="green",
            label="Posterior (obs.)", density=True)
    ax.axvline(t3["ecs_observation_estimate_K"], color="red", ls="--",
               label=f"Obs. estimate {t3['ecs_observation_estimate_K']:.2f} K")
    ax.axvline(3.0, color="black", ls=":", label="IPCC central 3.0 K")
    ax.set_xlabel("ECS (K per 2×CO$_2$)")
    ax.set_ylabel("Density")
    ax.set_title(f"ECS posterior: median={t3['posterior_median_K']:.2f} K | $\\lambda$={t3['lambda_Wm2_K']:.2f} W/m$^2$/K")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4: Planetary Boundaries bar
    ax = axes[1, 1]
    names = [b["name"] for b in t4["boundaries"]]
    ratios = [b["ratio"] for b in t4["boundaries"]]
    colors = ["#d62728" if b["breached"] else "#2ca02c" for b in t4["boundaries"]]
    y = np.arange(len(names))
    ax.barh(y, ratios, color=colors, alpha=0.8)
    ax.axvline(1.0, color="black", ls="--", label="Boundary")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel("Severity ratio (current / safe)")
    ax.set_title(f"Planetary boundaries: {t4['n_breached']}/{t4['n_total']} breached (2023)")
    ax.invert_yaxis()
    ax.legend(loc="lower right")
    ax.grid(axis="x", alpha=0.3)

    plt.suptitle("Phase 83: ITU × Climate / Earth Systems — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 83: ITU × Climate / Earth Systems — foundation")
    print("=" * 70)

    print("\n[Test 1] CO2 history + radiative forcing")
    t1 = test1_co2_history()
    print(f"  CO2 2024: {t1['ppm_2024']:.1f} ppm")
    print(f"  ΔF 2024:  {t1['df_2024_Wm2']:.2f} W/m^2")
    print(f"  ΔF 2×CO2 (IPCC AR6): {t1['df_2xCO2_IPCC_AR6_Wm2']:.2f} W/m^2")

    print("\n[Test 2] Earth Energy Imbalance")
    t2 = test2_eei()
    print(f"  EEI 2024:  {t2['eei_2024_Wm2']:.2f} W/m^2")
    print(f"  Power:     {t2['power_2024_TW']:.0f} TW")
    print(f"  Cumulative heat (1970-2024): {t2['cumulative_ZJ_2024']:.0f} ZJ")
    print(f"  Earth / Human consumption ratio: {t2['earth_to_human_ratio']:.0f}×")

    print("\n[Test 3] ECS posterior from observation")
    t3 = test3_ecs_posterior()
    print(f"  λ (feedback):        {t3['lambda_Wm2_K']:.2f} W/m^2/K")
    print(f"  ECS observation:     {t3['ecs_observation_estimate_K']:.2f} K")
    print(f"  Posterior median:    {t3['posterior_median_K']:.2f} K")
    print(f"  Posterior 66% CI:    {t3['posterior_66pct_K']}")
    print(f"  IPCC AR6 central:    3.00 K (66% CI [2.5, 4.0])")

    print("\n[Test 4] Planetary Boundaries")
    t4 = test4_planetary_boundaries()
    for b in t4["boundaries"]:
        flag = "✗ BREACHED" if b["breached"] else "✓ safe"
        print(f"  {b['name']:32s}  ratio={b['ratio']:.2f}  [{flag}]")
    print(f"  TOTAL: {t4['n_breached']}/{t4['n_total']} breached "
          f"({t4['fraction_breached']*100:.0f}%)")

    out = {
        "phase": 83,
        "title": "ITU × Climate / Earth Systems — foundation",
        "test1_co2_forcing": t1,
        "test2_eei": t2,
        "test3_ecs": t3,
        "test4_planetary_boundaries": t4,
    }
    with open("climate_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: climate_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "climate_itu_foundation.png")
    print("  ✓ Figure saved: climate_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 83 complete: CO2={:.0f}ppm, EEI={:.2f}W/m^2 ({:.0f}TW), ECS≈{:.1f}K, {}/9 boundaries breached"
          .format(t1["ppm_2024"], t2["eei_2024_Wm2"], t2["power_2024_TW"],
                  t3["posterior_median_K"], t4["n_breached"]))
    print("=" * 70)
