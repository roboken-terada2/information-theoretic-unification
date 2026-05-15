"""
Phase 85: Climate mitigation — renewables, CDR, SRM
Tier 1 #11 — Phase 3/4

4 numerical experiments:
1. Renewable share trajectory (2024-2050) + LCOE curves
2. CDR portfolio buildup (DAC + BECCS + reforestation + ocean alkalinity)
3. SRM forcing patch + termination shock simulation
4. 4-scenario temperature pathway (BAU / NZE / NZE+CDR / NZE+CDR+SRM)

Output: climate_mitigation.png + climate_mitigation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------
GtC_per_ppm = 2.13
DF_2X = 3.93
LAMBDA = 1.3  # W/m^2/K feedback parameter
C_OCEAN = 8.0  # W*yr/m^2/K effective ocean heat capacity


# ----------------------------------------------------------------------
# Test 1: Renewables trajectory + LCOE
# ----------------------------------------------------------------------
def renewable_share(year, scenario="NZE"):
    """Combined solar+wind share of global electricity."""
    if scenario == "BAU":
        anchors = [(2024, 14), (2030, 22), (2040, 35), (2050, 45)]
    elif scenario == "NZE":
        anchors = [(2024, 14), (2030, 31), (2040, 57), (2050, 72)]
    else:
        anchors = [(2024, 14), (2030, 40), (2040, 65), (2050, 80)]
    yrs = np.array([a[0] for a in anchors])
    sh = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, sh))


def lcoe_solar(year):
    """Wright's law: ~22%/doubling cost decline, anchored at $40/MWh in 2024."""
    if year < 2024:
        return 40 * (1.10) ** (2024 - year)
    return 40 * (0.97) ** (year - 2024)


def lcoe_coal(year):
    """Coal stays roughly flat with carbon price burden later."""
    base = 108
    carbon_burden = 0.0
    if year > 2024:
        carbon_burden = (year - 2024) * 3.5  # gradual carbon price impact
    return base + carbon_burden


def test1_renewables():
    years = np.arange(2024, 2051)
    sh_nze = np.array([renewable_share(y, "NZE") for y in years])
    sh_bau = np.array([renewable_share(y, "BAU") for y in years])
    lcoe_s = np.array([lcoe_solar(y) for y in years])
    lcoe_c = np.array([lcoe_coal(y) for y in years])
    return {
        "years": years.tolist(),
        "share_NZE": sh_nze.tolist(),
        "share_BAU": sh_bau.tolist(),
        "lcoe_solar": lcoe_s.tolist(),
        "lcoe_coal": lcoe_c.tolist(),
        "lcoe_solar_2050": float(lcoe_s[-1]),
        "lcoe_coal_2050": float(lcoe_c[-1]),
        "share_NZE_2050": float(sh_nze[-1]),
    }


# ----------------------------------------------------------------------
# Test 2: CDR portfolio
# ----------------------------------------------------------------------
def cdr_capacity_Mt(year, tech):
    """Returns capacity in MtCO2/yr for given tech."""
    if tech == "DAC":
        anchors = [(2024, 0.01), (2030, 5), (2040, 100), (2050, 1000)]
    elif tech == "BECCS":
        anchors = [(2024, 2), (2030, 100), (2040, 1000), (2050, 3000)]
    elif tech == "Reforestation":
        anchors = [(2024, 1000), (2030, 2500), (2040, 4000), (2050, 5000)]
    elif tech == "Ocean alkalinity":
        anchors = [(2024, 0), (2030, 1), (2040, 100), (2050, 500)]
    else:
        return 0.0
    yrs = np.array([a[0] for a in anchors])
    cap = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, cap))


def cdr_cost(year, tech):
    """Cost in $/tCO2."""
    curves = {
        "DAC":           [(2024, 600), (2030, 300), (2040, 150), (2050, 50)],
        "BECCS":         [(2024, 100), (2030, 80),  (2040, 60),  (2050, 50)],
        "Reforestation": [(2024, 30),  (2030, 25),  (2040, 22),  (2050, 20)],
        "Ocean alkalinity": [(2024, 200), (2030, 180), (2040, 130), (2050, 100)],
    }
    anchors = curves.get(tech, [(2024, 0), (2050, 0)])
    yrs = np.array([a[0] for a in anchors])
    cv = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, cv))


def test2_cdr():
    years = np.arange(2024, 2051)
    techs = ["DAC", "BECCS", "Reforestation", "Ocean alkalinity"]
    out = {}
    total = np.zeros(len(years))
    total_cost = np.zeros(len(years))
    for tech in techs:
        cap = np.array([cdr_capacity_Mt(y, tech) for y in years])
        cost = np.array([cdr_cost(y, tech) for y in years])
        out[tech] = {
            "capacity_Mt_yr": cap.tolist(),
            "cost_USD_t": cost.tolist(),
        }
        total += cap
        total_cost += cap * cost  # MtCO2 * $/t
    return {
        "years": years.tolist(),
        "techs": out,
        "total_capacity_Mt_yr": total.tolist(),
        "total_capacity_Gt_2050": float(total[-1] / 1000),
        "iea_nze_target_Gt": 10.0,
        "annual_cost_billion_USD_2050": float(total_cost[-1] / 1000),  # M$ -> B$
    }


# ----------------------------------------------------------------------
# Test 3: SRM forcing + termination shock
# ----------------------------------------------------------------------
def srm_forcing(year, start=2035, stop=2080, peak_F=2.0):
    """Returns negative forcing (W/m^2) from stratospheric aerosol injection."""
    if year < start or year > stop:
        return 0.0
    # Ramp up over 10 years, plateau, then continue until stop
    if year < start + 10:
        return -peak_F * (year - start) / 10.0
    return -peak_F


def test3_srm():
    years = np.arange(2025, 2110)
    F_srm = np.array([srm_forcing(y) for y in years])
    # Termination shock simulation
    # Assume CO2 forcing keeps ~3.5 W/m^2 in 2080. After SRM stops, net forcing jumps
    F_co2 = 3.5  # constant for illustration
    F_net = F_co2 + F_srm
    # EBM:
    T0 = 1.3  # starting K above preindustrial
    T = [T0]
    dt = 1.0
    for i in range(1, len(years)):
        dT = (F_net[i] - LAMBDA * T[-1]) / C_OCEAN
        T.append(T[-1] + dT * dt)
    T = np.array(T)
    # Termination shock magnitude: rise over 10 yr after 2080
    idx_2080 = np.where(years == 2080)[0][0]
    idx_2090 = np.where(years == 2090)[0][0]
    shock_K = float(T[idx_2090] - T[idx_2080])
    return {
        "years": years.tolist(),
        "F_srm_Wm2": F_srm.tolist(),
        "F_net_Wm2": F_net.tolist(),
        "T_K": T.tolist(),
        "termination_shock_K_over_10yr": shock_K,
        "T_during_SRM_2070": float(T[np.where(years == 2070)[0][0]]),
        "T_after_2090": float(T[idx_2090]),
    }


# ----------------------------------------------------------------------
# Test 4: 4-scenario temperature pathway
# ----------------------------------------------------------------------
def emissions_path(year, scenario):
    """GtC/yr emissions."""
    if scenario == "BAU":
        anchors = [(2024, 11), (2030, 12), (2050, 13), (2080, 13), (2100, 12)]
    elif scenario == "NZE":
        anchors = [(2024, 11), (2030, 9), (2040, 5), (2050, 1.5), (2070, 0.5), (2100, 0.3)]
    elif scenario in ("NZE_CDR", "NZE_CDR_SRM"):
        # Same emissions but CDR offsets later
        anchors = [(2024, 11), (2030, 9), (2040, 5), (2050, 1.5), (2070, 0.5), (2100, 0.3)]
    else:
        anchors = [(2024, 11), (2100, 11)]
    yrs = np.array([a[0] for a in anchors])
    ev = np.array([a[1] for a in anchors])
    return float(np.interp(year, yrs, ev))


def cdr_total_GtC(year):
    """Convert CDR portfolio (Mt CO2) -> GtC equivalent."""
    techs = ["DAC", "BECCS", "Reforestation", "Ocean alkalinity"]
    total_Mt = sum(cdr_capacity_Mt(year, t) for t in techs)
    # 1 GtCO2 = 0.273 GtC
    return total_Mt / 1000.0 * 0.273


def simulate_temperature(scenario):
    """Simple EBM with CO2-driven forcing + optional CDR/SRM."""
    years = np.arange(2024, 2101)
    M_a = 880.0  # GtC current
    T = [1.3]
    ppm_list = [422.0]
    for i, y in enumerate(years[1:], 1):
        E = emissions_path(y, scenario)
        CDR = cdr_total_GtC(y) if "CDR" in scenario else 0.0
        net_E = E - CDR
        # Natural sinks remove ~50% of net positive emissions
        if net_E > 0:
            sinks = 0.50 * net_E
        else:
            sinks = 0.30 * net_E  # 30% re-emitted when negative
        M_a = M_a + (net_E - sinks)
        ppm = 280.0 + (M_a - 600.0) / GtC_per_ppm
        F_co2 = 5.35 * math.log(ppm / 280.0)
        # SRM patch
        F_srm = srm_forcing(y) if "SRM" in scenario else 0.0
        F_net = F_co2 + F_srm
        dT = (F_net - LAMBDA * T[-1]) / C_OCEAN
        T.append(T[-1] + dT)
        ppm_list.append(ppm)
    return years.tolist(), np.array(T).tolist(), ppm_list


def test4_scenarios():
    scenarios = ["BAU", "NZE", "NZE_CDR", "NZE_CDR_SRM"]
    out = {}
    for sc in scenarios:
        years, T, ppm = simulate_temperature(sc)
        out[sc] = {
            "years": years,
            "T_K": T,
            "ppm": ppm,
            "T_2050_K": T[years.index(2050)],
            "T_2100_K": T[-1],
            "ppm_2050": ppm[years.index(2050)],
            "ppm_2100": ppm[-1],
        }
    # Cascade tipping probability at T_2100
    def tipping_prob(T, Tc, sigma=0.3):
        return 1.0 / (1.0 + math.exp(-(T - Tc) / sigma))
    Tc_list = [1.6, 1.7, 2.5]
    for sc in scenarios:
        T_peak = max(out[sc]["T_K"])
        p_cascade = 1.0
        for Tc in Tc_list:
            p_cascade *= tipping_prob(T_peak, Tc)
        out[sc]["T_peak_K"] = float(T_peak)
        out[sc]["P_cascade"] = float(p_cascade)
    return out


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: renewables share + LCOE
    ax = axes[0, 0]
    yrs = np.array(t1["years"])
    ax.plot(yrs, t1["share_NZE"], "g-", lw=2.5, label="NZE share %")
    ax.plot(yrs, t1["share_BAU"], "gray", lw=1.5, label="BAU share %")
    ax.set_xlabel("Year")
    ax.set_ylabel("Solar+Wind share (%)", color="g")
    ax2 = ax.twinx()
    ax2.plot(yrs, t1["lcoe_solar"], "orange", lw=2, label="Solar LCOE $/MWh")
    ax2.plot(yrs, t1["lcoe_coal"], "k", lw=1.5, label="Coal LCOE $/MWh")
    ax2.set_ylabel("LCOE ($/MWh)")
    ax.set_title(f"Renewables: NZE 2050 = {t1['share_NZE_2050']:.0f}% | Solar $/MWh: 40 → {t1['lcoe_solar_2050']:.0f}")
    ax.legend(loc="upper left")
    ax2.legend(loc="lower right", fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: CDR portfolio
    ax = axes[0, 1]
    yrs = np.array(t2["years"])
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"]
    bottom = np.zeros(len(yrs))
    for i, (tech, data) in enumerate(t2["techs"].items()):
        cap_Gt = np.array(data["capacity_Mt_yr"]) / 1000.0
        ax.fill_between(yrs, bottom, bottom + cap_Gt, color=colors[i],
                        alpha=0.7, label=tech)
        bottom += cap_Gt
    ax.axhline(t2["iea_nze_target_Gt"], color="red", ls="--",
               label=f"IEA NZE target {t2['iea_nze_target_Gt']:.0f} GtCO2/yr")
    ax.set_xlabel("Year")
    ax.set_ylabel("CDR capacity (GtCO$_2$/yr)")
    ax.set_title(f"CDR portfolio | 2050 total = {t2['total_capacity_Gt_2050']:.1f} GtCO2/yr | Cost $/yr: ${t2['annual_cost_billion_USD_2050']:.0f}B")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 3: SRM forcing + termination shock
    ax = axes[1, 0]
    yrs = np.array(t3["years"])
    ax.plot(yrs, t3["F_srm_Wm2"], "b-", lw=2, label="SRM forcing")
    ax.plot(yrs, t3["F_net_Wm2"], "r-", lw=2, label="Net forcing (CO$_2$+SRM)")
    ax.axhline(0, ls=":", color="black")
    ax.axvspan(2035, 2080, alpha=0.15, color="blue", label="SRM active")
    ax.set_xlabel("Year")
    ax.set_ylabel("Forcing (W/m$^2$)")
    ax.set_title(f"SRM patch | termination shock 2080-90: +{t3['termination_shock_K_over_10yr']:.2f} K/decade")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    ax_inset = ax.inset_axes([0.55, 0.15, 0.4, 0.35])
    ax_inset.plot(yrs, t3["T_K"], "purple", lw=2)
    ax_inset.axvline(2080, ls=":", color="red")
    ax_inset.set_xlabel("Year", fontsize=8)
    ax_inset.set_ylabel("ΔT (K)", fontsize=8)
    ax_inset.tick_params(labelsize=7)
    ax_inset.grid(alpha=0.3)

    # Panel 4: 4-scenario temperature pathway
    ax = axes[1, 1]
    cmap = {"BAU": "#d62728", "NZE": "#ff7f0e",
            "NZE_CDR": "#2ca02c", "NZE_CDR_SRM": "#1f77b4"}
    labels = {"BAU": "BAU", "NZE": "NZE only",
              "NZE_CDR": "NZE+CDR", "NZE_CDR_SRM": "NZE+CDR+SRM"}
    for sc, data in t4.items():
        ax.plot(data["years"], data["T_K"], color=cmap[sc], lw=2.5,
                label=f"{labels[sc]}  2100: {data['T_2100_K']:.2f}K  P_casc={data['P_cascade']*100:.1f}%")
    ax.axhline(1.5, ls="--", color="red", alpha=0.5, label="1.5°C")
    ax.axhline(2.0, ls=":", color="darkred", alpha=0.5, label="2.0°C")
    ax.set_xlabel("Year")
    ax.set_ylabel("ΔT global (K)")
    ax.set_title("4-scenario pathway: BAU vs NZE vs NZE+CDR vs NZE+CDR+SRM")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(alpha=0.3)

    plt.suptitle("Phase 85: Climate mitigation — renewables + CDR + SRM as K-current corrections",
                 fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 85: Climate mitigation — renewables + CDR + SRM")
    print("=" * 70)

    print("\n[Test 1] Renewables trajectory")
    t1 = test1_renewables()
    print(f"  Share NZE 2050:     {t1['share_NZE_2050']:.0f}%")
    print(f"  Solar LCOE 2050:    ${t1['lcoe_solar_2050']:.0f}/MWh")
    print(f"  Coal LCOE 2050:     ${t1['lcoe_coal_2050']:.0f}/MWh")

    print("\n[Test 2] CDR portfolio")
    t2 = test2_cdr()
    print(f"  Total 2050 CDR:     {t2['total_capacity_Gt_2050']:.1f} GtCO2/yr")
    print(f"  IEA NZE target:     {t2['iea_nze_target_Gt']:.0f} GtCO2/yr")
    print(f"  Annual cost 2050:   ${t2['annual_cost_billion_USD_2050']:.0f}B")

    print("\n[Test 3] SRM forcing + termination shock")
    t3 = test3_srm()
    print(f"  T during SRM 2070:  {t3['T_during_SRM_2070']:.2f} K")
    print(f"  T after stop 2090:  {t3['T_after_2090']:.2f} K")
    print(f"  Shock over 10 yr:   +{t3['termination_shock_K_over_10yr']:.2f} K")

    print("\n[Test 4] 4-scenario temperature pathway")
    t4 = test4_scenarios()
    for sc, data in t4.items():
        print(f"  {sc:14s} T2050={data['T_2050_K']:.2f}K  T2100={data['T_2100_K']:.2f}K  "
              f"T_peak={data['T_peak_K']:.2f}K  P_casc={data['P_cascade']*100:.1f}%")

    out = {
        "phase": 85,
        "title": "Climate mitigation — renewables + CDR + SRM",
        "test1_renewables": t1,
        "test2_cdr": {
            "total_capacity_Gt_2050": t2["total_capacity_Gt_2050"],
            "iea_nze_target_Gt": t2["iea_nze_target_Gt"],
            "annual_cost_billion_USD_2050": t2["annual_cost_billion_USD_2050"],
            "years": t2["years"][::4],
        },
        "test3_srm": {
            "termination_shock_K_over_10yr": t3["termination_shock_K_over_10yr"],
            "T_during_SRM_2070": t3["T_during_SRM_2070"],
            "T_after_2090": t3["T_after_2090"],
        },
        "test4_scenarios": {
            sc: {
                "T_2050_K": d["T_2050_K"],
                "T_2100_K": d["T_2100_K"],
                "T_peak_K": d["T_peak_K"],
                "ppm_2050": d["ppm_2050"],
                "ppm_2100": d["ppm_2100"],
                "P_cascade": d["P_cascade"],
            } for sc, d in t4.items()
        },
    }
    with open("climate_mitigation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: climate_mitigation_summary.json")

    make_figure(t1, t2, t3, t4, "climate_mitigation.png")
    print("  ✓ Figure saved: climate_mitigation.png")

    print("\n" + "=" * 70)
    print("Phase 85 complete: Best path NZE+CDR+SRM peaks {:.2f}K, cascade P={:.1f}%"
          .format(t4["NZE_CDR_SRM"]["T_peak_K"], t4["NZE_CDR_SRM"]["P_cascade"]*100))
    print("=" * 70)
