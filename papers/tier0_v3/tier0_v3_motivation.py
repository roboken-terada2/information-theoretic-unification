"""
Phase 107: Tier 0 v3.0 intermediate integration — motivation and structure
Tier 0 v3.0 Phase 1/4

4 numerical experiments:
1. Tier 0 version evolution v1.0 to v5.0
2. v2.0.0 vertical structure (8 layers) coverage
3. 16 Tier 1 papers categorical breakdown
4. v3.0 chapter plan + new content (Part IV-VI)

Output: tier0_v3_motivation.png + tier0_v3_motivation_summary.json
"""

import json
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Test 1: Tier 0 version evolution
# ----------------------------------------------------------------------
def test1_version_evolution():
    versions = [
        {"version": "v1.0.0", "year": 2026, "phases": 16,  "title": "GR + QM Unification (16 phases)", "DOI": "20109210"},
        {"version": "v2.0.0", "year": 2026, "phases": 42,  "title": "Physics + Life + Consciousness (42 phases)", "DOI": "20133709"},
        {"version": "v3.0.0", "year": 2026, "phases": 106, "title": "+ 16 Tier 1 polytope integration", "DOI": "TBD"},
        {"version": "v4.0",   "year": 2030, "phases": 220, "title": "Full Pass-1 synthesis", "DOI": "future"},
        {"version": "v5.0",   "year": 2032, "phases": 250, "title": "Pass-2 predictions added", "DOI": "future"},
    ]
    for v in versions:
        v["growth_from_v1"] = v["phases"] / 16
    return {"versions": versions}


# ----------------------------------------------------------------------
# Test 2: v2.0.0 vertical structure
# ----------------------------------------------------------------------
def test2_v2_structure():
    layers = [
        {"layer": "L0", "name": "Math + Axiom",      "phases": 5,  "phase_range": "1-5"},
        {"layer": "L1", "name": "Quantum Info + K",   "phases": 5,  "phase_range": "6-10"},
        {"layer": "L2", "name": "Spacetime + Gravity","phases": 5,  "phase_range": "11-15"},
        {"layer": "L3", "name": "Standard Model",     "phases": 5,  "phase_range": "16-20"},
        {"layer": "L4", "name": "Black Holes + GW",   "phases": 5,  "phase_range": "21-25"},
        {"layer": "L5", "name": "Dark Sector",        "phases": 5,  "phase_range": "26-30"},
        {"layer": "L6", "name": "Life",               "phases": 5,  "phase_range": "31-35"},
        {"layer": "L7", "name": "Consciousness",      "phases": 5,  "phase_range": "36-40"},
        {"layer": "L8", "name": "Qualia",             "phases": 2,  "phase_range": "41-42"},
    ]
    total = sum(l["phases"] for l in layers)
    return {"layers": layers, "total_phases": total}


# ----------------------------------------------------------------------
# Test 3: 16 Tier 1 categorical breakdown
# ----------------------------------------------------------------------
def test3_tier1_categories():
    tier1 = [
        {"id": 1,  "topic": "Quantum Computing",      "category": "engineering"},
        {"id": 2,  "topic": "AI/ASI",                  "category": "engineering"},
        {"id": 3,  "topic": "Cryptography",            "category": "engineering"},
        {"id": 4,  "topic": "Semiconductors",          "category": "engineering"},
        {"id": 5,  "topic": "Cancer",                  "category": "medicine"},
        {"id": 6,  "topic": "Aging",                   "category": "medicine"},
        {"id": 7,  "topic": "Psychiatry",              "category": "medicine"},
        {"id": 8,  "topic": "Economics",               "category": "social"},
        {"id": 9,  "topic": "Free Will/Ethics",        "category": "philosophy"},
        {"id": 10, "topic": "Energy/Materials",        "category": "engineering"},
        {"id": 11, "topic": "Climate/Earth",           "category": "biosphere"},
        {"id": 12, "topic": "Astrobiology/SETI",       "category": "cosmic"},
        {"id": 13, "topic": "Robotics",                "category": "embodiment"},
        {"id": 14, "topic": "Communications",          "category": "K-channel"},
        {"id": 15, "topic": "Infrastructure",          "category": "K-skeleton"},
        {"id": 16, "topic": "Smart Cities",            "category": "urban"},
    ]
    # Category counts
    categories = {}
    for t in tier1:
        c = t["category"]
        categories[c] = categories.get(c, 0) + 1
    return {"tier1": tier1, "categories": categories}


# ----------------------------------------------------------------------
# Test 4: v3.0 chapter plan
# ----------------------------------------------------------------------
def test4_chapter_plan():
    parts = [
        {"part": "Part I",   "title": "Axiom and Foundation",     "chapters": 5,  "new": False, "phases": "1-15 revised"},
        {"part": "Part II",  "title": "Physical World",            "chapters": 4,  "new": False, "phases": "16-30 revised"},
        {"part": "Part III", "title": "Life and Mind",             "chapters": 3,  "new": False, "phases": "31-42 revised"},
        {"part": "Part IV",  "title": "16-Vertex Polytope",       "chapters": 7,  "new": True,  "phases": "Polytope graph theory + 4 blocks"},
        {"part": "Part V",   "title": "Predictions and Pass-2",   "chapters": 3,  "new": True,  "phases": "160→50 predictions + framework"},
        {"part": "Part VI",  "title": "Outlook",                   "chapters": 2,  "new": True,  "phases": "Block A roadmap + v4.0 path"},
    ]
    total_chapters = sum(p["chapters"] for p in parts)
    new_chapters = sum(p["chapters"] for p in parts if p["new"])
    return {"parts": parts, "total_chapters": total_chapters, "new_chapters": new_chapters,
            "new_pct": new_chapters / total_chapters * 100}


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Version evolution
    ax = axes[0, 0]
    versions = t1["versions"]
    names = [v["version"] for v in versions]
    phases = [v["phases"] for v in versions]
    years = [v["year"] for v in versions]
    colors = ["#1f77b4" if v["DOI"] not in ["TBD", "future"] else "#2ca02c" if v["DOI"] == "TBD" else "#ff7f0e"
              for v in versions]
    ax.bar(names, phases, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, v in enumerate(versions):
        ax.text(i, v["phases"] + 10, f"{v['phases']}", ha="center", fontsize=9)
        ax.text(i, -15, f"{v['year']}", ha="center", fontsize=8, color="gray")
    ax.set_ylabel("Number of phases")
    ax.set_ylim(-20, 280)
    ax.set_title("Tier 0 version evolution: v1.0 → v3.0 (NOW) → v5.0")
    ax.grid(alpha=0.3, axis="y")

    # Panel 2: v2.0.0 vertical structure
    ax = axes[0, 1]
    layers = t2["layers"]
    names = [f"{l['layer']} {l['name']}" for l in layers]
    phases = [l["phases"] for l in layers]
    y_pos = np.arange(len(layers))
    cmap = plt.cm.viridis(np.linspace(0.2, 0.9, len(layers)))
    ax.barh(y_pos, phases, color=cmap, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, l in enumerate(layers):
        ax.text(l["phases"] + 0.2, i, f"{l['phase_range']}", va="center", fontsize=8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Phases per layer")
    ax.set_title(f"v2.0.0 vertical structure: 9 layers (L0-L8), {t2['total_phases']} phases total")
    ax.grid(alpha=0.3, axis="x")

    # Panel 3: 16 Tier 1 categories
    ax = axes[1, 0]
    cats = t3["categories"]
    cat_names = list(cats.keys())
    cat_counts = list(cats.values())
    colors_cat = {"engineering": "#1f77b4", "medicine": "#d62728", "social": "#9467bd",
                  "philosophy": "#8c564b", "biosphere": "#2ca02c", "cosmic": "#000080",
                  "embodiment": "#ff1493", "K-channel": "#00ced1", "K-skeleton": "#a0522d",
                  "urban": "#ffd700"}
    colors = [colors_cat.get(c, "gray") for c in cat_names]
    ax.bar(cat_names, cat_counts, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, (c, n) in enumerate(cats.items()):
        ax.text(i, n + 0.1, f"{n}", ha="center", fontsize=9)
    ax.set_ylabel("Number of Tier 1 papers")
    ax.set_title("16 Tier 1 papers by category (engineering most common = 5)")
    ax.grid(alpha=0.3, axis="y")
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right", fontsize=8)

    # Panel 4: v3.0 chapter plan
    ax = axes[1, 1]
    parts = t4["parts"]
    names = [f"{p['part']}: {p['title'][:25]}" for p in parts]
    chapters = [p["chapters"] for p in parts]
    new_flags = [p["new"] for p in parts]
    colors = ["#d62728" if new else "#1f77b4" for new in new_flags]
    y_pos = np.arange(len(parts))
    ax.barh(y_pos, chapters, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
    for i, p in enumerate(parts):
        tag = " (NEW)" if p["new"] else ""
        ax.text(p["chapters"] + 0.1, i, tag, va="center", fontsize=8, color="red")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Chapters")
    ax.set_title(f"v3.0 plan: {t4['total_chapters']} chapters, {t4['new_chapters']} new ({t4['new_pct']:.0f}%)")
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle("Phase 107: Tier 0 v3.0 motivation + structure",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 107: Tier 0 v3.0 intermediate integration — motivation")
    print("=" * 70)

    print("\n[Test 1] Tier 0 version evolution")
    t1 = test1_version_evolution()
    for v in t1["versions"]:
        print(f"  {v['version']:10s} ({v['year']})  {v['phases']:3d} phases  ({v['growth_from_v1']:.1f}x v1)  -  {v['title']}")

    print("\n[Test 2] v2.0.0 vertical structure")
    t2 = test2_v2_structure()
    for l in t2["layers"]:
        print(f"  {l['layer']:3s} {l['name']:25s}  {l['phases']:2d} phases (Phase {l['phase_range']})")
    print(f"  Total: {t2['total_phases']} phases (Tier 0 v2.0.0)")

    print("\n[Test 3] 16 Tier 1 categorical breakdown")
    t3 = test3_tier1_categories()
    for t in t3["tier1"]:
        print(f"  #{t['id']:2d}  {t['topic']:25s}  [{t['category']}]")
    print(f"\n  Categories:")
    for c, n in t3["categories"].items():
        print(f"    {c:15s}  {n}")

    print("\n[Test 4] v3.0 chapter plan")
    t4 = test4_chapter_plan()
    for p in t4["parts"]:
        tag = " (NEW)" if p["new"] else ""
        print(f"  {p['part']:8s} {p['title']:30s}  {p['chapters']:2d} chapters{tag}  -  {p['phases']}")
    print(f"  Total: {t4['total_chapters']} chapters, {t4['new_chapters']} new ({t4['new_pct']:.0f}%)")

    out = {
        "phase": 107,
        "title": "Tier 0 v3.0 intermediate integration — motivation",
        "test1_version_evolution": t1,
        "test2_v2_structure": t2,
        "test3_tier1_categories": t3,
        "test4_chapter_plan": t4,
    }
    with open("tier0_v3_motivation_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: tier0_v3_motivation_summary.json")

    make_figure(t1, t2, t3, t4, "tier0_v3_motivation.png")
    print("  ✓ Figure saved: tier0_v3_motivation.png")

    print("\n" + "=" * 70)
    print("Phase 107 complete: v3.0 plan = 24 chapters, 12 new (50%), polytope integration")
    print("=" * 70)
