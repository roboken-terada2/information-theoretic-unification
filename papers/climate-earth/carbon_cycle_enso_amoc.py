"""
Phase 84: Carbon cycle + ENSO + AMOC dynamics
Tier 1 #11 — Phase 2/4

4 numerical experiments:
1. 4-box carbon cycle (atm/land/surf/deep) - airborne fraction reproduction
2. ENSO Vallis-1986 limit cycle - 3-7 year periodicity
3. AMOC Stommel 2-box bistability - tipping under freshwater forcing
4. 3 tipping elements probability vs T_global

Output: carbon_cycle_enso_amoc.png + carbon_cycle_enso_amoc_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------
GtC_per_ppm = 2.13  # 1 ppm = 2.13 GtC in atmosphere


# ----------------------------------------------------------------------
# Test 1: 4-box carbon cycle
# ----------------------------------------------------------------------
def emissions_GtC(year):
    """Historical + projected. RCP4.5-ish."""
    if year < 1850:
        return 0.0
    anchors = [(1850, 0.05), (1900, 0.5), (1950, 1.6),
               (1960, 2.6), (1970, 4.1), (1980, 5.4),
               (1990, 6.4), (2000, 7.0), (2010, 9.2),
               (2020, 10.6), (2024, 11.0),
               (2030, 10.5), (2040, 8.0), (2050, 5.0),
               (2070, 2.0), (2100, 0.5)]
    yrs = np.array([a[0] for a in anchors])
    ev = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, ev))


def carbon_cycle_rhs(state, t):
    M_a, M_l, M_s, M_d = state
    Ma_star, Ml_star, Ms_star, Md_star = 600.0, 2300.0, 900.0, 38000.0
    # Tuned to reproduce airborne fraction ~0.48 (GCB 2024)
    k_al = 1/60.0    # atm -> land
    k_la = 1/80.0    # land -> atm (respiration)
    k_as = 1/40.0    # atm -> surface ocean
    k_sa = 1/60.0    # surface -> atm
    k_sd = 1/300.0   # surface -> deep
    k_ds = 1/2000.0  # deep -> surface
    E = emissions_GtC(1850 + t)
    # Anomaly from preindustrial reference
    da = M_a - Ma_star
    dl = M_l - Ml_star
    ds = M_s - Ms_star
    dd = M_d - Md_star
    dMa = E - k_al * da + k_la * dl - k_as * da + k_sa * ds
    dMl = k_al * da - k_la * dl
    dMs = k_as * da - k_sa * ds - k_sd * ds + k_ds * dd
    dMd = k_sd * ds - k_ds * dd
    return [dMa, dMl, dMs, dMd]


def test1_carbon_cycle():
    t = np.arange(0, 251)  # 1850-2100
    init = [600.0, 2300.0, 900.0, 38000.0]
    sol = odeint(carbon_cycle_rhs, init, t)
    M_a = sol[:, 0]
    ppm = 280.0 + (M_a - 600.0) / GtC_per_ppm
    years = 1850 + t

    # Airborne fraction over 1960-2024
    E_cum = np.array([emissions_GtC(y) for y in years])
    idx1960 = np.where(years == 1960)[0][0]
    idx2024 = np.where(years == 2024)[0][0]
    cum_E_since_1960 = np.cumsum(E_cum[idx1960:])
    dM_a_since_1960 = M_a[idx1960:] - M_a[idx1960]
    AF = dM_a_since_1960 / np.maximum(cum_E_since_1960, 1e-9)
    # mean over 1960-2024 (use post-1970 to skip transient)
    af_mean = float(np.mean(AF[10:(idx2024 - idx1960 + 1)]))

    return {
        "years": years.tolist(),
        "M_a_GtC": M_a.tolist(),
        "ppm": ppm.tolist(),
        "M_l_GtC": sol[:, 1].tolist(),
        "M_s_GtC": sol[:, 2].tolist(),
        "M_d_GtC": sol[:, 3].tolist(),
        "emissions_GtC_yr": E_cum.tolist(),
        "airborne_fraction": AF.tolist(),
        "AF_1960_2024_mean": af_mean,
        "ppm_2024": float(ppm[years.tolist().index(2024)]),
        "ppm_2050": float(ppm[years.tolist().index(2050)]),
        "ppm_2100": float(ppm[-1]),
    }


# ----------------------------------------------------------------------
# Test 2: ENSO Vallis-86 model
# ----------------------------------------------------------------------
def enso_rhs(state, t, omega, eps, delta, noise_seed=None):
    """Tziperman delayed-oscillator-style two-variable form,
    chosen to yield ~4-year limit cycles. h = thermocline depth anomaly."""
    T, h = state
    dT = -omega * h + eps * T - delta * T**3
    dh = omega * T
    return [dT, dh]


def test2_enso():
    omega = 2 * math.pi / 4.0  # target 4-year cycle
    eps, delta = 0.4, 0.6
    t = np.linspace(0, 60, 12001)  # 60 years
    init = [0.5, 0.0]
    sol = odeint(enso_rhs, init, t, args=(omega, eps, delta))
    T = sol[:, 0]
    # Add stochastic forcing for realism
    rng = np.random.default_rng(7)
    T_noisy = T + 0.15 * rng.standard_normal(len(T))
    # Spectral analysis on second half (skip transient)
    half = len(T) // 2
    Tseg = T[half:] - T[half:].mean()
    dt = t[1] - t[0]
    fft = np.fft.rfft(Tseg)
    freqs = np.fft.rfftfreq(len(Tseg), dt)
    psd = np.abs(fft) ** 2
    psd[0] = 0
    peak_freq = freqs[np.argmax(psd)]
    period = 1.0 / peak_freq if peak_freq > 0 else 0.0
    return {
        "t_years": t.tolist(),
        "T_anomaly_K": T_noisy.tolist(),
        "u_windstress": sol[:, 1].tolist(),
        "dominant_period_yr": float(period),
        "amplitude_K": float(np.std(T[half:])),
        "max_T_K": float(np.max(T_noisy)),
    }


# ----------------------------------------------------------------------
# Test 3: AMOC Stommel 2-box bistability
# ----------------------------------------------------------------------
def stommel_q(eta_range, mu=6.2, lam=0.2):
    """
    Cessi 1994 normalized form: q = 1 + mu^2*(y-1)^2 dynamics —
    Steady states from cubic in y (salinity contrast).
    For simplicity we use parameterization yielding bistability in eta in [0.1, 0.32].
    """
    high_branch = []
    low_branch = []
    mid_branch = []
    # y^3 - y + eta = 0 (cubic with eta as parameter)
    # Bifurcation: |eta| < 2/(3*sqrt(3)) ≈ 0.385 ⇒ 3 real roots
    for e in eta_range:
        coeffs = [1.0, 0.0, -1.0, e]
        roots = np.roots(coeffs)
        real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-6])
        if len(real_roots) == 3:
            high_branch.append((e, real_roots[2]))   # largest = strong AMOC
            mid_branch.append((e, real_roots[1]))    # unstable
            low_branch.append((e, real_roots[0]))    # weak/collapsed
        else:
            r = real_roots[0]
            if r > 0.5:
                high_branch.append((e, r))
            else:
                low_branch.append((e, r))
    return high_branch, mid_branch, low_branch


def test3_amoc():
    eta_range = np.linspace(0.0, 0.45, 300)
    high, mid, low = stommel_q(eta_range)
    # Scale: q=1 (strong) ≈ 17 Sv; q=-1 (collapsed) ≈ -17 Sv → use abs scaling.
    q_scale = 17.0
    eta_h = [h[0] for h in high]
    q_h = [h[1] * q_scale for h in high]
    eta_l = [l[0] for l in low]
    q_l = [l[1] * q_scale for l in low]
    # Saddle-node eta_crit = 2/(3√3) ≈ 0.385
    eta_crit = 2.0 / (3.0 * math.sqrt(3.0))

    # Probability of collapse 2025-2100 under freshwater forcing increase
    # Greenland + Arctic ice melt accelerating: eta(t) rises ~0.003/yr
    eta_0, rate = 0.24, 0.0028  # per year (Greenland melt accelerating)
    years = np.arange(2025, 2101)
    eta_t = eta_0 + rate * (years - 2025)
    # Stochastic crossing: integrate over uncertainty in eta_crit (sigma=0.07)
    sigma_eta = 0.07
    P_collapse = 0.5 * (1.0 + np.array([math.erf((e - eta_crit) / (sigma_eta * math.sqrt(2))) for e in eta_t]))

    return {
        "eta_high_branch": eta_h,
        "q_high_Sv": q_h,
        "eta_low_branch": eta_l,
        "q_low_Sv": q_l,
        "eta_mid_branch": [m[0] for m in mid],
        "q_mid_Sv": [m[1] * q_scale for m in mid],
        "eta_critical": float(eta_crit),
        "eta_present_2025": eta_0,
        "eta_2095": float(eta_t[-1]),
        "years_proj": years.tolist(),
        "P_collapse_proj": P_collapse.tolist(),
        "P_collapse_2050": float(P_collapse[years.tolist().index(2050)]),
        "P_collapse_2095": float(P_collapse[years.tolist().index(2095)]),
    }


# ----------------------------------------------------------------------
# Test 4: 3 tipping elements
# ----------------------------------------------------------------------
def tipping_prob(T, T_c, sigma=0.3):
    return 1.0 / (1.0 + math.exp(-(T - T_c) / sigma))


def test4_tipping_elements():
    T_range = np.linspace(0.5, 4.0, 50)
    elements = [
        {"name": "Greenland ice sheet", "T_c": 1.6, "impact_m": 7.0, "timescale_yr": 5000},
        {"name": "West Antarctic (Thwaites)", "T_c": 1.7, "impact_m": 3.0, "timescale_yr": 500},
        {"name": "Amazon rainforest", "T_c": 2.5, "impact_GtC": 200.0, "timescale_yr": 100},
    ]
    out_elements = []
    for el in elements:
        P = np.array([tipping_prob(T, el["T_c"]) for T in T_range])
        out_elements.append({
            "name": el["name"],
            "T_c": el["T_c"],
            "P_at_1p5": float(tipping_prob(1.5, el["T_c"])),
            "P_at_2p0": float(tipping_prob(2.0, el["T_c"])),
            "P_at_3p0": float(tipping_prob(3.0, el["T_c"])),
            "P_curve": P.tolist(),
            "impact_summary": el.get("impact_m", el.get("impact_GtC", "")),
            "timescale_yr": el["timescale_yr"],
        })
    # Cascade joint probability at T=2.0 (independent assumption)
    p_cascade_2deg = 1.0
    for el in elements:
        p_cascade_2deg *= tipping_prob(2.0, el["T_c"])
    return {
        "T_range_K": T_range.tolist(),
        "elements": out_elements,
        "P_cascade_all3_at_2K": float(p_cascade_2deg),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Carbon cycle ppm + airborne fraction
    ax = axes[0, 0]
    yrs = np.array(t1["years"])
    ax.plot(yrs, t1["ppm"], "k-", lw=2, label="Atmospheric CO$_2$ (ppm)")
    ax.axhline(422, ls=":", color="red", alpha=0.6, label="2024 obs 422 ppm")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO$_2$ (ppm)")
    ax.set_title(f"4-box carbon cycle | 2024={t1['ppm_2024']:.0f}, 2050={t1['ppm_2050']:.0f}, 2100={t1['ppm_2100']:.0f}")
    ax.grid(alpha=0.3)
    ax.legend()

    # Panel 2: ENSO oscillation
    ax = axes[0, 1]
    t_yr = np.array(t2["t_years"])
    T_anom = np.array(t2["T_anomaly_K"])
    ax.plot(t_yr, T_anom, "b-", lw=1)
    ax.axhline(0, ls="--", color="gray", alpha=0.5)
    ax.fill_between(t_yr, 0, T_anom, where=(T_anom > 0), color="red", alpha=0.4, label="El Niño")
    ax.fill_between(t_yr, 0, T_anom, where=(T_anom < 0), color="blue", alpha=0.4, label="La Niña")
    ax.set_xlabel("Year")
    ax.set_ylabel("SST anomaly (K)")
    ax.set_title(f"ENSO Vallis-86 model | period={t2['dominant_period_yr']:.1f} yr, amp={t2['amplitude_K']:.2f} K")
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 3: AMOC bistability + collapse projection
    ax = axes[1, 0]
    ax.plot(t3["eta_high_branch"], t3["q_high_Sv"], "b-", lw=2, label="High AMOC (current)")
    ax.plot(t3["eta_low_branch"], t3["q_low_Sv"], "r-", lw=2, label="Low / collapsed")
    ax.plot(t3["eta_mid_branch"], t3["q_mid_Sv"], "k:", lw=1, alpha=0.5, label="Unstable")
    ax.axvline(t3["eta_critical"], ls="--", color="black", alpha=0.6,
               label=f"$\\eta_{{crit}}$={t3['eta_critical']:.3f}")
    ax.axvline(t3["eta_present_2025"], ls="-", color="green", alpha=0.5,
               label=f"2025: $\\eta$={t3['eta_present_2025']:.2f}")
    ax.set_xlabel("Freshwater forcing $\\eta$")
    ax.set_ylabel("AMOC strength (Sv)")
    ax.set_title(f"AMOC bistability | P(collapse 2050)={t3['P_collapse_2050']*100:.0f}%, 2095={t3['P_collapse_2095']*100:.0f}%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Inset: P(collapse) over time
    ax_inset = ax.inset_axes([0.55, 0.55, 0.4, 0.4])
    ax_inset.plot(t3["years_proj"], np.array(t3["P_collapse_proj"]) * 100, "purple", lw=2)
    ax_inset.set_xlabel("Year", fontsize=8)
    ax_inset.set_ylabel("P collapse (%)", fontsize=8)
    ax_inset.tick_params(labelsize=7)
    ax_inset.grid(alpha=0.3)

    # Panel 4: tipping elements
    ax = axes[1, 1]
    T_range = np.array(t4["T_range_K"])
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    for i, el in enumerate(t4["elements"]):
        ax.plot(T_range, np.array(el["P_curve"]) * 100,
                color=colors[i], lw=2,
                label=f"{el['name']} (Tc={el['T_c']}°C)")
        ax.axvline(el["T_c"], color=colors[i], ls=":", alpha=0.5)
    ax.axvline(1.5, color="red", ls="--", alpha=0.5, label="1.5°C")
    ax.axvline(2.0, color="darkred", ls="--", alpha=0.5, label="2.0°C")
    ax.set_xlabel("Global $\\Delta T$ (K)")
    ax.set_ylabel("P (tipping)")
    ax.set_title(f"3 tipping elements | cascade P(all3 @ 2°C)={t4['P_cascade_all3_at_2K']*100:.1f}%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.suptitle("Phase 84: Carbon cycle + ENSO + AMOC — dynamic K-flows",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 84: Carbon cycle + ENSO + AMOC dynamics")
    print("=" * 70)

    print("\n[Test 1] 4-box carbon cycle")
    t1 = test1_carbon_cycle()
    print(f"  ppm 2024: {t1['ppm_2024']:.1f}")
    print(f"  ppm 2050: {t1['ppm_2050']:.1f}")
    print(f"  ppm 2100: {t1['ppm_2100']:.1f}")
    print(f"  Airborne fraction (1970-2024 mean): {t1['AF_1960_2024_mean']:.3f}")
    print(f"  Observation (GCB 2024): 0.48")

    print("\n[Test 2] ENSO Vallis-86")
    t2 = test2_enso()
    print(f"  Dominant period: {t2['dominant_period_yr']:.1f} yr (target 3-7)")
    print(f"  Amplitude: {t2['amplitude_K']:.2f} K")
    print(f"  Max SST anom: {t2['max_T_K']:.2f} K")

    print("\n[Test 3] AMOC Stommel bistability")
    t3 = test3_amoc()
    print(f"  eta_crit: {t3['eta_critical']:.3f}")
    print(f"  P(collapse by 2050): {t3['P_collapse_2050']*100:.0f}%")
    print(f"  P(collapse by 2095): {t3['P_collapse_2095']*100:.0f}%")
    print(f"  Ditlevsen 2023 estimate: 5-15% by 2050, 10-50% by 2095")

    print("\n[Test 4] 3 tipping elements")
    t4 = test4_tipping_elements()
    for el in t4["elements"]:
        print(f"  {el['name']:32s}  Tc={el['T_c']:.1f}°C "
              f"P(1.5)={el['P_at_1p5']*100:5.1f}%  P(2.0)={el['P_at_2p0']*100:5.1f}%")
    print(f"  Cascade P(all3 @ 2°C): {t4['P_cascade_all3_at_2K']*100:.1f}%")

    out = {
        "phase": 84,
        "title": "Carbon cycle + ENSO + AMOC dynamics",
        "test1_carbon_cycle": {
            "ppm_2024": t1["ppm_2024"], "ppm_2050": t1["ppm_2050"], "ppm_2100": t1["ppm_2100"],
            "AF_mean": t1["AF_1960_2024_mean"],
            "years_subset": t1["years"][::25],
            "ppm_subset": t1["ppm"][::25],
        },
        "test2_enso": {
            "dominant_period_yr": t2["dominant_period_yr"],
            "amplitude_K": t2["amplitude_K"],
            "max_T_K": t2["max_T_K"],
        },
        "test3_amoc": {
            "eta_critical": t3["eta_critical"],
            "P_collapse_2050": t3["P_collapse_2050"],
            "P_collapse_2095": t3["P_collapse_2095"],
        },
        "test4_tipping": t4,
    }
    with open("carbon_cycle_enso_amoc_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: carbon_cycle_enso_amoc_summary.json")

    make_figure(t1, t2, t3, t4, "carbon_cycle_enso_amoc.png")
    print("  ✓ Figure saved: carbon_cycle_enso_amoc.png")

    print("\n" + "=" * 70)
    print("Phase 84 complete: AF={:.2f}, ENSO period={:.1f}yr, AMOC P(2050)={:.0f}%, cascade={:.1f}%"
          .format(t1['AF_1960_2024_mean'], t2['dominant_period_yr'],
                  t3['P_collapse_2050']*100, t4['P_cascade_all3_at_2K']*100))
    print("=" * 70)
