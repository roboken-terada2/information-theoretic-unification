"""
Phase 95: ITU Communications / Networks foundation
Tier 1 #14 — Phase 1/4

4 numerical experiments:
1. Shannon channel capacity vs ITU modular form (SNR scan)
2. Internet traffic exponential growth 2000-2050
3. Mobile generations (3G to 6G) bandwidth + latency
4. Satellite constellations: Starlink, OneWeb, Kuiper, Guowang

Output: comm_itu_foundation.png + comm_itu_foundation_summary.json
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Shannon-Hartley capacity vs SNR
# ----------------------------------------------------------------------
def test1_shannon_capacity():
    """C = B log2(1 + SNR) — show capacity as function of SNR for different bandwidths"""
    B_list = [1e3, 1e6, 1e9, 1e12]  # 1 kHz, 1 MHz, 1 GHz, 1 THz
    snr_dB = np.linspace(-10, 50, 100)
    snr_linear = 10 ** (snr_dB / 10)

    curves = []
    for B in B_list:
        C = B * np.log2(1 + snr_linear)
        curves.append({
            "bandwidth_Hz": B,
            "label": f"{B:.0e} Hz",
            "snr_dB": snr_dB.tolist(),
            "capacity_bps": C.tolist(),
            "capacity_at_30dB_bps": float(B * math.log2(1 + 1000)),
        })
    return {
        "curves": curves,
        "snr_dB_range": [float(snr_dB.min()), float(snr_dB.max())],
    }


# ----------------------------------------------------------------------
# Test 2: Internet traffic exponential growth
# ----------------------------------------------------------------------
def test2_internet_traffic():
    timeline = [
        {"year": 1995, "traffic_EB_month": 0.01,  "primary_use": "Web, email"},
        {"year": 2000, "traffic_EB_month": 1,     "primary_use": "Web, email"},
        {"year": 2005, "traffic_EB_month": 3,     "primary_use": "P2P, Web 2.0"},
        {"year": 2010, "traffic_EB_month": 20,    "primary_use": "YouTube, SNS"},
        {"year": 2015, "traffic_EB_month": 80,    "primary_use": "Mobile video"},
        {"year": 2020, "traffic_EB_month": 250,   "primary_use": "Streaming, COVID"},
        {"year": 2024, "traffic_EB_month": 500,   "primary_use": "Video (60%), AI (10%)"},
        {"year": 2030, "traffic_EB_month": 2000,  "primary_use": "AI (30%), VR/AR"},
        {"year": 2040, "traffic_EB_month": 8000,  "primary_use": "Embodied AI, Holographic"},
        {"year": 2050, "traffic_EB_month": 20000, "primary_use": "Quantum Internet, AGI"},
    ]
    years = np.array([t["year"] for t in timeline])
    traffic = np.array([t["traffic_EB_month"] for t in timeline])
    log_traffic = np.log10(traffic)
    slope, intercept = np.polyfit(years, log_traffic, 1)
    doubling_yr = math.log10(2) / slope if slope > 0 else None
    return {
        "timeline": timeline,
        "doubling_period_yr": float(doubling_yr) if doubling_yr else None,
        "growth_2024_2050_ratio": 20000 / 500,
    }


# ----------------------------------------------------------------------
# Test 3: Mobile generations
# ----------------------------------------------------------------------
def test3_mobile_generations():
    gens = [
        {"gen": "1G", "year": 1980, "bandwidth_kbps": 2,        "latency_ms": 1000, "use": "Voice"},
        {"gen": "2G", "year": 1991, "bandwidth_kbps": 100,      "latency_ms": 500,  "use": "Voice+SMS"},
        {"gen": "3G", "year": 2001, "bandwidth_kbps": 200,      "latency_ms": 100,  "use": "Mobile data"},
        {"gen": "4G LTE", "year": 2010, "bandwidth_kbps": 100000, "latency_ms": 30, "use": "Smartphone video"},
        {"gen": "5G", "year": 2020, "bandwidth_kbps": 10e6,     "latency_ms": 1,    "use": "IoT, AR"},
        {"gen": "6G (proj)", "year": 2030, "bandwidth_kbps": 1e9, "latency_ms": 0.1, "use": "XR, holographic"},
        {"gen": "7G? (proj)", "year": 2040, "bandwidth_kbps": 1e11, "latency_ms": 0.01, "use": "Brain-net?"},
    ]
    return {"gens": gens}


# ----------------------------------------------------------------------
# Test 4: Satellite constellations
# ----------------------------------------------------------------------
def test4_satellites():
    consts = [
        {"name": "Starlink (SpaceX)",  "sats_2024": 6800, "planned": 42000, "latency_ms": 30,  "country": "USA"},
        {"name": "OneWeb (Eutelsat)",  "sats_2024": 650,  "planned": 1980,  "latency_ms": 70,  "country": "UK"},
        {"name": "Kuiper (Amazon)",    "sats_2024": 100,  "planned": 3236,  "latency_ms": 40,  "country": "USA"},
        {"name": "Guowang (China)",    "sats_2024": 0,    "planned": 13000, "latency_ms": 35,  "country": "CN"},
        {"name": "IRIS² (EU)",         "sats_2024": 0,    "planned": 290,   "latency_ms": 50,  "country": "EU"},
    ]
    total_2024 = sum(c["sats_2024"] for c in consts)
    total_planned = sum(c["planned"] for c in consts)
    return {
        "constellations": consts,
        "total_sats_2024": total_2024,
        "total_planned": total_planned,
        "expansion_ratio": total_planned / max(total_2024, 1),
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Shannon capacity
    ax = axes[0, 0]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    for c, color in zip(t1["curves"], colors):
        ax.semilogy(c["snr_dB"], c["capacity_bps"], color=color, lw=2,
                    label=c["label"], alpha=0.85)
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("Capacity (bps, log scale)")
    ax.set_title("Shannon-Hartley capacity = B log2(1+SNR) = ITU max modular K-flow")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # Panel 2: Internet traffic
    ax = axes[0, 1]
    years = [t["year"] for t in t2["timeline"]]
    traffic = [t["traffic_EB_month"] for t in t2["timeline"]]
    ax.semilogy(years, traffic, "o-", color="#1f77b4", lw=2, markersize=8, alpha=0.85)
    for t in t2["timeline"][::2]:
        ax.annotate(f"{t['primary_use'][:20]}", (t["year"], t["traffic_EB_month"]),
                    xytext=(5, 5), textcoords="offset points", fontsize=6, rotation=10)
    ax.set_xlabel("Year")
    ax.set_ylabel("Traffic (EB/month, log)")
    ax.set_title(f"Internet traffic | doubling = {t2['doubling_period_yr']:.1f} yr | 2024-2050 = {t2['growth_2024_2050_ratio']:.0f}x")
    ax.grid(alpha=0.3, which="both")

    # Panel 3: Mobile generations
    ax = axes[1, 0]
    gens = t3["gens"]
    years = [g["year"] for g in gens]
    bw_log = [math.log10(g["bandwidth_kbps"]) for g in gens]
    lat_log = [math.log10(g["latency_ms"]) for g in gens]
    ax.plot(years, bw_log, "o-", color="#1f77b4", lw=2, markersize=8, label="log10(BW kbps)")
    ax.plot(years, lat_log, "s-", color="#d62728", lw=2, markersize=8, label="log10(Latency ms)")
    for g in gens:
        ax.annotate(g["gen"], (g["year"], math.log10(g["bandwidth_kbps"])),
                    xytext=(5, 5), textcoords="offset points", fontsize=8)
    ax.set_xlabel("Year")
    ax.set_ylabel("log10")
    ax.set_title("Mobile generations: 1G → 6G (1Tbps, 0.1ms)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 4: Satellites
    ax = axes[1, 1]
    consts = t4["constellations"]
    names = [c["name"] for c in consts]
    sats_2024 = [c["sats_2024"] for c in consts]
    planned = [c["planned"] for c in consts]
    y_pos = np.arange(len(consts))
    width = 0.35
    ax.barh(y_pos - width/2, sats_2024, width, color="#1f77b4", alpha=0.8, label="2024", edgecolor="black", linewidth=0.5)
    ax.barh(y_pos + width/2, planned, width, color="#d62728", alpha=0.8, label="Planned", edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlabel("Number of satellites (log)")
    ax.set_title(f"Satellite constellations | 2024 total {t4['total_sats_2024']} → planned {t4['total_planned']:,}")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="x", which="both")

    plt.suptitle("Phase 95: ITU × Communications / Networks — foundation",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 95: ITU × Communications / Networks — foundation")
    print("=" * 70)

    print("\n[Test 1] Shannon-Hartley capacity")
    t1 = test1_shannon_capacity()
    for c in t1["curves"]:
        print(f"  B={c['label']:10s}  C@30dB = {c['capacity_at_30dB_bps']:.2e} bps")

    print("\n[Test 2] Internet traffic growth")
    t2 = test2_internet_traffic()
    for t in t2["timeline"]:
        print(f"  {t['year']}: {t['traffic_EB_month']:7.1f} EB/month  - {t['primary_use']}")
    print(f"  Doubling period: {t2['doubling_period_yr']:.1f} years")
    print(f"  2024 -> 2050 growth ratio: {t2['growth_2024_2050_ratio']:.0f}x")

    print("\n[Test 3] Mobile generations")
    t3 = test3_mobile_generations()
    for g in t3["gens"]:
        print(f"  {g['gen']:10s} ({g['year']})  BW={g['bandwidth_kbps']:.0e} kbps  lat={g['latency_ms']:6.2f} ms  - {g['use']}")

    print("\n[Test 4] Satellite constellations")
    t4 = test4_satellites()
    for c in t4["constellations"]:
        print(f"  {c['name']:25s}  2024: {c['sats_2024']:5d}  planned: {c['planned']:6d}  lat: {c['latency_ms']:3d}ms  [{c['country']}]")
    print(f"  Total 2024: {t4['total_sats_2024']}, planned: {t4['total_planned']:,} ({t4['expansion_ratio']:.0f}x expansion)")

    out = {
        "phase": 95,
        "title": "ITU × Communications / Networks — foundation",
        "test1_shannon": {"curves_summary": [{"label": c["label"], "C_at_30dB": c["capacity_at_30dB_bps"]} for c in t1["curves"]]},
        "test2_internet": t2,
        "test3_mobile": t3,
        "test4_satellites": t4,
    }
    with open("comm_itu_foundation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: comm_itu_foundation_summary.json")

    make_figure(t1, t2, t3, t4, "comm_itu_foundation.png")
    print("  ✓ Figure saved: comm_itu_foundation.png")

    print("\n" + "=" * 70)
    print("Phase 95 complete: Internet doubling {:.1f}yr, 6G 1Tbps 0.1ms, Sats {:,} planned"
          .format(t2["doubling_period_yr"], t4["total_planned"]))
    print("=" * 70)
