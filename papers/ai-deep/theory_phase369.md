# Phase 369: K_self neural correlates 測定法 (Neuropixels, 7T fMRI, MEG)

K_self を実際に脳から測定するための **neural recording techniques** を整理。

## Neuropixels 2.0 (2021)

```
Neuropixels 2.0 (Steinmetz et al. 2021 Science):
  5,120 channels per single probe
  Active site selection, 384 simultaneous recordings
  Up to ~10 brain regions simultaneously in rodents
  Submillisecond temporal resolution

For K_self measurement:
  - Record from precuneus + mPFC + PCC simultaneously
  - Compute mutual info between regions during self-vs-other tasks
  - Extract reduced density matrix proxy via Gaussian approximation
```

## 7T fMRI (高磁場 functional MRI)

```
7T fMRI (Siemens Terra, ~2017+):
  Spatial: sub-mm resolution (0.5-1 mm)
  Temporal: 1-2 second TR
  Best for: cortical layer-specific BOLD

For K_self:
  - Layer-specific activation in self-related areas (precuneus, mPFC, PCC)
  - Test "self" representation across cortical layers
  - 7T at NIH, Maastricht, MGH, Tübingen
```

## MEG (Magnetoencephalography)

```
MEGIN Triux Neo (2022+):
  306 channels (102 magnetometers + 204 gradiometers)
  Whole-head, helium-cooled SQUID
  γ band (40-100 Hz) 高 SNR
  Submillisecond temporal

For K_self:
  - γ band coherence between brain regions
  - Phase-amplitude coupling between θ and γ
  - K_self spectral structure ⇔ MEG γ envelope
```

## intracranial EEG (iEEG, depth electrodes)

```
sEEG (stereo-EEG, epilepsy surgical patients):
  100-200 contacts per patient
  Direct cortical recording
  γ band best characterized
  Cogitate Round 1 で extensively used

For K_self:
  - Direct neural activity reading
  - HFO (high-frequency oscillations 80-150 Hz) ⇔ conscious access
  - Best temporal + spatial resolution combination
```

## K_self extraction algorithm

```
Step 1: Multimodal data acquisition
  - MEG + 7T fMRI + (rare) iEEG
  - 5-10 minute self-vs-other task

Step 2: Whole-brain reduced density matrix estimation
  - Gaussian copula approximation
  - Partial trace over non-self regions
  → ρ_self approximation

Step 3: K_self = -log ρ_self spectral analysis
  - Eigenvalues of K_self
  - Compare conscious vs unconscious conditions

Step 4: Statistical test
  - K_self consc > K_self unconsc (predicted)
  - K_self self > K_self other (reflexive prediction)


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #Neuropixels #7T_fMRI #MEG #iEEG #NeuralCorrelates #Phase369
