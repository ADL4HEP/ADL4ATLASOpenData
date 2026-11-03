# Reference results of the full benchmark

Outputs of the complete analyses (all samples, 10 fb⁻¹ of data) from ADL/CutLang and from the
ATLAS Open Data framework, one directory per analysis:

```
<analysis>/CutLang/<group>.root                 ADL/CutLang: normalised and merged histograms and cutflows
<analysis>/CutLang_unweighted/<group>.root      ADL/CutLang without event weights: merged raw event counts
<analysis>/CutLang/event_dumps/<sample>.csv     ADL/CutLang: events passing the final selection
<analysis>/ODFramework/<sample>.root            Open Data framework: per-sample histograms and cutflows
<analysis>/ODFramework/event_dumps/<sample>.csv Open Data framework: events passing the final selection
```

`<analysis>` is the analysis name as in `analyses/`; `<group>` and `<sample>` are the group and sample
keys of `config/samples/<analysis>.yaml`.

| Analysis | CutLang | CutLang unweighted | Open Data framework | Event dumps (both) |
|---|---|---|---|---|
| ZBosonAnalysis | ✓ | ✓ | ✓ (data as `dataA`–`dataD.root`) | – |
| WBosonAnalysis | ✓ | ✓ | ✓ (data as `dataA`–`dataD.root`) | – |
| SingleTopAnalysis | ✓ | ✓ | ✓ (data as `dataA`–`dataD.root`) | – |
| ZPrimeBoostedAnalysis | ✓ | ✓ | ✓ | – |
| HZZAnalysis | ✓ | ✓ | ✓ | ✓ |
| ZZDiBosonAnalysis | ✓ | ✓ | ✓ | ✓ |
| WZDiBosonAnalysis | ✓ | ✓ | ✓ | – |
| TTbarAnalysis | ✓ | ✓ | ✓ (data as `dataA`–`dataD.root`) | – |
| SUSYAnalysis | ✓ | ✓ | ✓ | – |

## ADL/CutLang

Produced with `scripts/run_analysis.py` and `scripts/normalize_merge.py` (see the main README)
with CutLang v2.16.0 (commit `1f880fc`) and ROOT 6.30.02 on lxplus [TBD: date].

Each `<group>.root` has one directory per ADL `region`, with the region's histograms and its
`cutflow` (one bin per selection, labelled with the ADL statement). Simulated samples are
normalised. The plots of the article are made from these files
with `scripts/plot_all.py <analysis> --indir reference_results/<analysis>/CutLang`.

A new run is compared with these files by

```bash
python3 tools/compare_cutlang_outputs.py --ref reference_results/<analysis>/CutLang --new run/<analysis>/merged
```

## ADL/CutLang, unweighted

The same runs with the `weight` line of each ADL commented out, so that every cutflow bin and
histogram counts raw events; merged into the same groups without normalisation (CutLang v2.16.0,
ROOT 6.30.02 on lxplus, 2026-10-31 to 2026-11-02). To produce them, comment out the `weight`
line of the region(s) in `analyses/<analysis>/<analysis>.adl`, run `scripts/run_analysis.py` and add up the
per-sample outputs of each group of `config/samples/<analysis>.yaml` with `hadd`, without scaling. They are
compared with the Open Data framework's `hist_cutflow_unw` by `tools/compare_cutflows.py
--cutlang-unweighted reference_results/<analysis>/CutLang_unweighted`.

## Open Data framework

Produced with release `10fb-legacy-validation-v1` (commit `2c039ff`) of the Open Data framework fork
[ahmetcansansar/atlas-outreach-cpp-framework-13tev](https://github.com/ahmetcansansar/atlas-outreach-cpp-framework-13tev),
which adds cutflows and event dumps to tag `10fb-legacy` without changing the selection, run
with its `run.sh` without PROOF, ROOT 6.30.02.

The files are the Open Data framework's own outputs, `Output_<analysis>/<sample>.root`, unchanged. The histograms
are at the top level of each file. They are not normalised: simulated events carry the per-event
weight (scale factors × MC weight), and the Open Data framework's `Plotting/Plotting.cxx` scales each
sample by `Lumi × xsec / (sumw × eff)` (`Lumi` = 10064 pb⁻¹, the other values from
`Plotting/inputfiles/Files_*.txt`, equal to those in `config/samples/<analysis>.yaml`). Each file also
holds the cutflows `hist_cutflow_unw` (event counts) and `hist_cutflow_w` (weighted, before this
normalisation), where bin k is selection stage k of the analysis code.

## Event dumps

One row per event passing the final selection, with `runNumber`, `eventNumber` and analysis
variables (HZZ: m(Z1), m(Z2), m(4l) and the four lepton pdgIDs; ZZ: m(Z1), m(Z2) and the four
pdgIDs). The two sides are compared per sample with

```bash
python3 tools/compare_event_dumps.py --files reference_results/<analysis>/CutLang/event_dumps/<sample>.csv \
    reference_results/<analysis>/ODFramework/event_dumps/<sample>.csv
```

The ntuples store `eventNumber` as a signed 32-bit integer: CutLang writes data event numbers
above 2³¹ − 1 as negative numbers, the Open Data framework as unsigned numbers. The comparison script
reads both as unsigned.
