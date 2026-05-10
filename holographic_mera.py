"""
Phase 3: Holography — emergent hyperbolic AdS_3 from MERA tensor network.

Demonstrates that:
  (i)  the graph distance through a binary MERA between two boundary
       points scales as 2 log_2 |i - j|, the AdS geodesic law.
  (ii) the minimal cut through MERA bounding a boundary interval of
       length L has bond count ~2 log_2 L, and the resulting Ryu–
       Takayanagi entropy matches the Calabrese–Cardy CFT scaling
       S_A = (c/3) log L of the underlying XX-model ground state.
  (iii) the network embeds visibly as a Poincaré-disk realisation of
       AdS_3 with explicit RT surfaces.

References:
- Vidal, PRL 99 (2007) 220405 -- MERA
- Swingle, PRD 86 (2012) 065007 -- entanglement renormalisation as holography
- Pastawski, Yoshida, Harlow, Preskill, JHEP 2015:149 -- HaPPY code
- Calabrese, Cardy, J. Stat. Mech. (2004) -- CFT entanglement scaling
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import deque
from scipy.linalg import eigh

# -----------------------------------------------------------------------
# 1. Build a binary MERA graph (cylinder topology).
# -----------------------------------------------------------------------
def build_mera(N):
    """Return (nodes, edges) for a binary MERA over N=2^L boundary sites.

    Each level k has N/2^k sites arranged in a ring. Each site at level k
    connects to 2 children at level k-1 (isometry) and to its 2 ring
    neighbours at the same level (disentanglers)."""
    L = int(round(np.log2(N)))
    assert 2 ** L == N, "N must be a power of 2"
    nodes = []
    for k in range(L + 1):
        nl = N // (2 ** k)
        for m in range(nl):
            nodes.append((k, m))
    edges = []
    for k in range(L + 1):
        nl = N // (2 ** k)
        for m in range(nl):
            if nl > 1:
                edges.append(((k, m), (k, (m + 1) % nl)))
        if k < L:
            for m in range(nl // 2):
                edges.append(((k + 1, m), (k, 2 * m)))
                edges.append(((k + 1, m), (k, 2 * m + 1)))
    return nodes, edges, L

def all_pairs_bfs(nodes, edges):
    n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[idx[a]].append(idx[b])
        adj[idx[b]].append(idx[a])
    D = -np.ones((n, n), dtype=int)
    for s in range(n):
        D[s, s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s, v] < 0:
                    D[s, v] = D[s, u] + 1
                    q.append(v)
    return D, idx, adj

# -----------------------------------------------------------------------
# 2. Minimum cut for an interval (= Ryu–Takayanagi surface)
# -----------------------------------------------------------------------
def min_cut_interval(nodes, edges, N, a, b):
    """Edge connectivity (min cut) between boundary set [a, b) and complement.
    Uses Ford–Fulkerson with BFS augmenting paths on unit-capacity graph."""
    idx = {v: i for i, v in enumerate(nodes)}
    n = len(nodes)
    # Source = super node 'S' connected to boundary sites in A;
    # Sink   = super node 'T' connected to boundary sites in complement.
    S = n; T = n + 1
    cap = {}
    def add_edge(u, v, c):
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)

    for (u, v) in edges:
        iu, iv = idx[u], idx[v]
        add_edge(iu, iv, 1); add_edge(iv, iu, 1)

    A = set()
    for m in range(a, b):
        A.add(idx[(0, m % N)])
    notA = {idx[(0, m)] for m in range(N) if m not in {x % N for x in range(a, b)}}
    INF = 10 ** 9
    for v in A:
        add_edge(S, v, INF)
    for v in notA:
        add_edge(v, T, INF)

    # BFS-augmenting path
    flow = 0
    while True:
        parent = {S: None}
        q = deque([S])
        while q and T not in parent:
            u = q.popleft()
            for w in [k[1] for k in cap if k[0] == u]:
                if w not in parent and cap[(u, w)] > 0:
                    parent[w] = u
                    q.append(w)
        if T not in parent:
            break
        # find bottleneck
        path = []
        cur = T
        while parent[cur] is not None:
            path.append((parent[cur], cur))
            cur = parent[cur]
        bottleneck = min(cap[e] for e in path)
        for u, v in path:
            cap[(u, v)] -= bottleneck
            cap[(v, u)] += bottleneck
        flow += bottleneck
    return flow

# -----------------------------------------------------------------------
# 3. Reference: actual XX entanglement entropy (PBC, half filling)
# -----------------------------------------------------------------------
def xx_entropy_curve(N):
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    h[0, N - 1] = h[N - 1, 0] = -1.0
    eigvals, U = eigh(h)
    n = N // 2
    C = (U[:, :n] @ U[:, :n].conj().T).real
    Ss = []
    for L in range(1, N // 2 + 1):
        sub = list(range(L))
        Csub = C[np.ix_(sub, sub)]
        eigs = np.linalg.eigvalsh(Csub)
        eigs = np.clip(eigs, 1e-14, 1 - 1e-14)
        Ss.append(-np.sum(eigs * np.log(eigs) + (1 - eigs) * np.log(1 - eigs)))
    return np.arange(1, N // 2 + 1), np.array(Ss)

# -----------------------------------------------------------------------
# 4. Poincaré disk embedding
# -----------------------------------------------------------------------
def poincare_position(node, N, total_levels, dpho=0.85):
    """Place boundary on the unit circle (r close to 1) and bulk inward."""
    k, m = node
    nl = N // (2 ** k)
    theta = 2 * np.pi * (m + 0.5) / nl
    rho = (total_levels - k) * dpho        # hyperbolic radius
    r = np.tanh(rho / 2)                    # Poincaré radius
    return r * np.cos(theta), r * np.sin(theta)

# -----------------------------------------------------------------------
# 5. Main
# -----------------------------------------------------------------------
def main():
    N = 64
    nodes, edges, L = build_mera(N)
    print(f"=== Phase 3: Holographic MERA (N = {N}, levels = {L}) ===")
    print(f"  total nodes = {len(nodes)},  total edges = {len(edges)}\n")

    D, idx, adj = all_pairs_bfs(nodes, edges)

    # (i) Boundary geodesic distance vs log(physical separation)
    boundary = [(0, m) for m in range(N)]
    seps = []; gdists = []
    for i in range(N):
        for j in range(i + 1, N):
            d_phys = min(j - i, N - (j - i))
            d_graph = D[idx[(0, i)], idx[(0, j)]]
            seps.append(d_phys); gdists.append(d_graph)
    seps = np.array(seps); gdists = np.array(gdists)
    # average over pairs at the same physical separation
    uniq = np.array(sorted(set(seps.tolist())))
    avg_g = np.array([gdists[seps == s].mean() for s in uniq])
    p = np.polyfit(np.log(uniq[uniq >= 2]), avg_g[uniq >= 2], 1)
    print("[Result A — graph distance scales as AdS geodesic]")
    print(f"  d_MERA(i,j) ≈ {p[0]:.4f} · log|i-j| + {p[1]:.3f}")
    print(f"  prediction (binary tree): coefficient = 2/log(2) = {2/np.log(2):.4f}\n")

    # (ii) Ryu–Takayanagi: min-cut for interval of length L
    Ls = np.arange(1, N // 2 + 1)
    cuts = np.array([min_cut_interval(nodes, edges, N, 0, L_) for L_ in Ls])
    print("[Result B — Ryu–Takayanagi: min cut vs interval length]")
    p2 = np.polyfit(np.log(Ls[Ls >= 2]), cuts[Ls >= 2], 1)
    print(f"  |γ_A|(L) ≈ {p2[0]:.4f} · log L + {p2[1]:.3f}\n")

    # XX entropy comparison
    L_xx, S_xx = xx_entropy_curve(N)
    # rescale the cut to match (one free constant: 1/(4G))
    # fit: S_xx = alpha * cuts + const
    A = np.vstack([cuts.astype(float), np.ones_like(cuts, dtype=float)]).T
    sol, *_ = np.linalg.lstsq(A, S_xx, rcond=None)
    alpha = sol[0]
    G_eff = 1.0 / (4 * alpha)
    print("[Result C — Brown–Henneaux from numerics]")
    print(f"  S_A^XX = α · |γ_A| + const,   α = 1/(4G_eff) = {alpha:.4f}")
    print(f"  → effective Newton constant G_eff = {G_eff:.4f}")
    print(f"  → c_eff = 3 R_AdS / (2 G_eff)  (Brown–Henneaux); for R_AdS = 1/log 2,")
    print(f"     c_eff = {3/(2*G_eff*np.log(2)):.4f}    (XX exact: c = 1)\n")

    # ----------------------------------------------------------------
    # Plot
    # ----------------------------------------------------------------
    fig = plt.figure(figsize=(15.5, 10))
    gs = fig.add_gridspec(2, 3)

    ax = fig.add_subplot(gs[0, 0])
    ax.plot(uniq, avg_g, 'o-', label=r'MERA graph dist.')
    fit = p[0] * np.log(uniq) + p[1]
    ax.plot(uniq, fit, 'k--', label=fr'fit ${p[0]:.3f}\log d {p[1]:+.2f}$')
    ax.set_xscale('log')
    ax.set_xlabel(r'physical separation $|i-j|$')
    ax.set_ylabel(r'graph distance $d_\mathrm{MERA}$')
    ax.set_title('(a) Boundary distance is hyperbolic')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    ax = fig.add_subplot(gs[0, 1])
    ax.plot(Ls, cuts, 'o-', label='MERA min-cut |γ_A|')
    ax.set_xscale('log')
    ax.set_xlabel('interval length L'); ax.set_ylabel('|γ_A|')
    ax.set_title('(b) RT: min cut grows as log L')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    ax = fig.add_subplot(gs[0, 2])
    ax.plot(L_xx, S_xx, 'o', label='XX numerical S_A')
    ax.plot(L_xx, alpha * cuts + sol[1], '-', label=fr'$\alpha\,|\gamma_A|+$const')
    ax.set_xscale('log')
    ax.set_xlabel('interval length L'); ax.set_ylabel('entropy')
    ax.set_title('(c) Brown–Henneaux: CFT entropy = RT prediction')
    ax.legend(); ax.grid(alpha=0.3, which='both')

    # (d) Poincaré disk visualisation of MERA
    ax = fig.add_subplot(gs[1, :2])
    pos = {v: poincare_position(v, N, L, dpho=1.1) for v in nodes}
    boundary_circle = plt.Circle((0, 0), 1, fill=False, color='k', lw=1.0)
    ax.add_patch(boundary_circle)
    for u, v in edges:
        x1, y1 = pos[u]; x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='gray', lw=0.4, alpha=0.6)
    # color nodes by level
    cmap = plt.cm.plasma
    for v in nodes:
        x, y = pos[v]
        c = cmap(v[0] / max(L, 1))
        ax.scatter([x], [y], color=c, s=18, zorder=3, edgecolor='k', linewidth=0.3)
    # Highlight an example RT surface for interval [0, L_demo)
    L_demo = 16
    boundary_indices = list(range(0, L_demo))
    ax.scatter([pos[(0, m)][0] for m in boundary_indices],
               [pos[(0, m)][1] for m in boundary_indices],
               s=70, facecolor='none', edgecolor='red', linewidths=1.6, zorder=4,
               label=fr'interval $A$ (L={L_demo})')

    # Find an RT surface = simple bulk path connecting endpoints
    # use BFS shortest path between (0, 0) and (0, L_demo % N)
    src = idx[(0, 0)]; dst = idx[(0, L_demo % N)]
    parent = {src: None}; q = deque([src])
    while q and dst not in parent:
        u = q.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u; q.append(v)
    path = [dst]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path = path[::-1]
    px = [pos[nodes[i]][0] for i in path]
    py = [pos[nodes[i]][1] for i in path]
    ax.plot(px, py, color='red', lw=2.0, zorder=5,
            label='RT surface (geodesic in bulk)')
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('(d) MERA as Poincaré disk: emergent AdS$_3$')
    ax.legend(loc='upper right', fontsize=8)

    # (e) Explanation panel: holographic dictionary
    ax = fig.add_subplot(gs[1, 2])
    ax.axis('off')
    text = (
        "Holographic dictionary realised here\n\n"
        "Boundary CFT (1D)        ↔   Bulk geometry (2D AdS_3)\n"
        "----------------------------------------------------\n"
        "physical site i           ↔   point on conformal\n"
        "                                boundary\n"
        "block of length L         ↔   interval whose RT\n"
        "                                surface is a bulk\n"
        "                                geodesic\n"
        "S_A = (c/3) log L         ↔   |γ_A|/(4 G_N) = log L\n"
        "                                (Ryu–Takayanagi)\n"
        "δS_A = δ⟨K_A⟩            ↔   linearised Einstein\n"
        "                                δG_μν = 8πG δT_μν\n"
        "                                (Phase 2)\n"
        "MERA layer k              ↔   AdS radial coordinate z\n"
        "RG flow ↑                 ↔   move away from boundary\n"
    )
    ax.text(0, 1, text, fontfamily='monospace', va='top', fontsize=8.5)

    plt.tight_layout()
    out = r'C:\Users\TeradaMunehiro\quantum_gravity_info\holographic_mera.png'
    plt.savefig(out, dpi=130)
    print(f"Figure saved to {out}")

    import json
    summary = {
        'N': N, 'levels': L,
        'graph_distance_log_slope': float(p[0]),
        'graph_distance_log_slope_predicted': 2 / np.log(2),
        'mincut_log_slope': float(p2[0]),
        'alpha_eq_1_over_4G_eff': float(alpha),
        'G_eff': float(G_eff),
        'central_charge_from_brown_henneaux': float(3 / (2 * G_eff * np.log(2))),
    }
    with open(r'C:\Users\TeradaMunehiro\quantum_gravity_info\summary_phase3.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("Summary saved.")


if __name__ == '__main__':
    main()
