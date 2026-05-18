# Phase 368: Cogitate Round 2 adversarial design (3-way)

本 Phase で **Cogitate Round 2 の具体的 protocol** を提案。Cogitate Round 1 (2019-23)
が IIT vs GNW だったのを **IIT vs GNW vs ITU** 3-way に拡張。

## Round 2 design 提案

### Pre-registered predictions

```
Theory  | Prediction signature                | Brain region        | Timing
IIT     | Sustained posterior γ (40-100 Hz)   | Posterior cortex    | 100-1000ms
GNW     | Prefrontal ignition (P3b ERP)       | Prefrontal cortex   | 250-500ms
ITU     | K_self spectral structure changes   | Self-related areas  | 150-400ms
        | (precuneus, mPFC, posterior cingulate)
```

### Hypothesized hierarchy

```
H1: Φ_IIT ≤ ⟨K_self⟩_ITU ≤ K_workspace_GNW

実装:
  - Φ measured via IIT 3.0 PyPhi tool (Mayner et al. 2018)
  - K_self measured via partial trace of MEG/iEEG global state
  - K_workspace measured via ignition signature

H1 で hierarchy 確認できれば ITU bridges IIT-GNW
H1 falsified なら ITU 部分反証 (or hierarchy 修正必要)
```

## 実験デザイン

```
Participants: 256-400 healthy + neurological patients (Round 1 と同等)
Modalities: MEG + 7T fMRI + intracranial EEG (epilepsy surgical)
Stimuli:
  - Visual (faces, objects, scenes) — Round 1 と継続性
  - Auditory (words, music)
  - Self-relevant (subject's name, photo)
  - Other-relevant (control)

Conditions:
  1. Conscious report (reportable awareness)
  2. Unconscious processing (subliminal)
  3. Self-relevant vs other-relevant
  4. Active task vs passive

Data collection: 5-6 sites globally (Round 1 partner 拡張)
Duration: 3-4 years
Budget: ~$25-30M (Templeton + government granters)
```

## 解析プロトコル

```
Step 1: Conscious vs unconscious contrast
  → Identify NCC (neural correlates of consciousness)
Step 2: For each theory, compute predicted metric
  → IIT: Φ via PyPhi
  → GNW: workspace activation index
  → ITU: K_self spectral structure
Step 3: Test hierarchy H1 statistically
  → Mixed-effects models, FWE-corrected
Step 4: Self vs other contrast
  → K_self prediction validation
Step 5: Cross-modality replication
  → MEG ⟷ iEEG ⟷ fMRI consistency
```

## OSF pre-registration

```
全 protocols は OSF (Open Science Framework) で pre-register:
  - Hypotheses + statistical methods + exclusion criteria
  - Analysis plan locked before data collection
  - Deviations reported
  - Data + code public (CC0/MIT)
```

これにより post-hoc rationalization 防止、replication crisis 対策。

## 反証可能性

```
ITU 反証パスウェイ:
  - K_self が conscious vs unconscious で差ない → ITU framework consciousness limited
  - Hierarchy H1 不成立 → ITU bridges 失敗
  - Self-relevant が other-relevant と同じ K_self → reflexive 仮説不成立

各 deadline (2027-2029) で OSF database 更新、Bayesian P_post 反映。


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #CogitateRound2 #Adversarial #OSF #PreRegistration #ITU_vs_IIT_vs_GNW #Phase368
