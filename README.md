# ATLAS Open Data ADL Benchmark Suite

**ADL4ATLASOpenData** contains nine physics analyses of the ATLAS Open Data
13 TeV release (2020, 10 fb⁻¹), written in the Analysis Description Language
(ADL), together with what is needed to run them with the
[CutLang](https://github.com/unelg/CutLang) interpreter and reproduce the
results of the accompanying article:

- one ADL file per analysis, used for all data and simulated samples;
- per-analysis sample configurations: input files, cross-sections, sums of weights, merge groups;
- scripts to run CutLang over the samples, normalise the simulated samples and merge them into each process category, such as Z+jets, Single top;
- tools to compare outputs bin by bin.

The analyses reproduce the educational analyses of the
[ATLAS Open Data 13 TeV C++ framework](https://github.com/atlas-outreach-data-tools/atlas-outreach-cpp-framework-13tev)
at tag **`10fb-legacy`** (commit `688d73f`). That tag corresponds to the 2020
10 fb⁻¹ release; the main branch of the framework repository now targets newer
ATLAS Open Data releases and is **not** the reference for this suite.

> Status: pre-release. Planned for v1.0.0: container image, reference outputs
> and automated comparison tests, plotting scripts for the article figures.

## Analyses

| Analysis | ADL | Input stream | Files | Input size | Merge groups |
|---|---|---|---|---|---|
| Z boson → ℓℓ | `analyses/ZBosonAnalysis/` | 2lep | 29 | 16.7 GB | data, Zjets, Wjets, stop, ttbar, diboson |
| W boson → ℓν | `analyses/WBosonAnalysis/` | 1lep | 65 | 69.9 GB | data, Wjets, Zjets, stop, ttbar, diboson |
| Single top (t-channel) | `analyses/SingleTopAnalysis/` | 1lep | 65 | 69.9 GB | data, stop_tchan, stop_tWtb, ZVV, Wjets |
| tt̄ (lepton + jets) | `analyses/TTbarAnalysis/` | 1lep | 29 | 50.5 GB | data, ttbar, stop, V, diboson |
| WZ → ℓνℓℓ | `analyses/WZDiBosonAnalysis/` | 3lep | 29 | 0.9 GB | data, WZ, VV, V, top |
| ZZ → 4ℓ | `analyses/ZZDiBosonAnalysis/` | 4lep, 2lep | 29 | 0.6 GB | data, ZZ, WWZ, topV |
| H → ZZ* → 4ℓ | `analyses/HZZAnalysis/` | 4lep | 33 | 0.3 GB | data, Higgs, ZZ, V |
| Slepton search (2ℓ + E_T^miss) | `analyses/SUSYAnalysis/` | 2lep | 105 | 19.6 GB | data, signal, ttbar, stop, diboson, Wjets, Zjets |
| Z′ → tt̄ (boosted) | `analyses/ZPrimeBoostedAnalysis/` | 1largeRjet1lep | 64 | 4.5 GB | data, signal, ttbar, stop, V, diboson |

In total, the nine analyses read 311 files (112.5 GB). The files do not have to
be downloaded: CutLang streams them over XRootD from `eospublic.cern.ch`. With a
slow connection, download them once and run from disk with `--input-dir`; see
[`docs/download.md`](docs/download.md) for per-analysis download lists,
commands and SHA-256 checksums to check the downloaded files. The complete list of files, cross-sections and sums of weights is in
[`docs/samples.md`](docs/samples.md).

## Requirements

| Software | Version used for the article | Notes |
|---|---|---|
| CutLang | v2.16.0 (`1f880fc`) | needs ROOT, flex and bison to build |
| ROOT | 6.36.12 | with PyROOT and XRootD (for streaming the samples) |
| Python | 3.9 or newer | packages: `pyyaml`, `numpy`, `uproot` |
| OS | Linux or macOS | tested on Linux RHEL9 and macOS 26 (arm64) |

Streaming the samples needs ROOT built with XRootD (`root-config --has-xrootd` should
print `yes`). The configs stream from
`root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22`.
The same files are also served over HTTP at
`http://opendata.cern.ch/eos/opendata/atlas/OutreachDatasets/2020-01-22`, which needs ROOT
built with Davix (`root-config --has-davix`) and was less reliable for long reads in our
tests (stalled streams). Without XRootD, set `ntuple_base_url` to the HTTP address or
download the files (`docs/download.md`).

## Installation

```bash
# 1. CutLang at the release used for the article
git clone https://github.com/unelg/CutLang.git
cd CutLang && git checkout v2.16.0
cd CLA && make -j4 && cd ../..        # requires ROOT (root-config in PATH), flex, bison
export CUTLANG_DIR=$PWD/CutLang

# 2. This repository and its Python dependencies
git clone https://github.com/ahmetcansansar/ADL4ATLASOpenData.git
cd ADL4ATLASOpenData
python3 -m pip install pyyaml numpy uproot
python3 -c "import ROOT"              # check that PyROOT is available
```

## Quick start (a few minutes)

Run the Z boson analysis inside the main directory (ADL4ATLASOpenData) on three small samples and the first 20 000 events of
one data period, then normalise and merge:

```bash
python3 scripts/run_analysis.py ZBosonAnalysis --outdir run/Zboson/samples \
    --samples data_A,Wminustaunu,single_top_schan --events 20000 --jobs 3

python3 scripts/normalize_merge.py ZBosonAnalysis \
    --indir run/Zboson/samples --outdir run/Zboson/merged --allow-missing
```

`--allow-missing` lets the merge proceed with only part of the samples.

## Running a full analysis

```bash
python3 scripts/run_analysis.py TTbarAnalysis --outdir run/TTbar/samples --jobs 4
python3 scripts/normalize_merge.py TTbarAnalysis --indir run/TTbar/samples --outdir run/TTbar/merged
```

The analysis name is the directory name under `analyses/`. The run is
resumable: samples whose output already exists are skipped, unless `--force`
is given. While samples run, a status block shows events processed, rate and
estimated time per sample. In a terminal the block is redrawn in place;
when the output goes to a file it is appended every `--progress-interval`
seconds. To run only the data, for example:

```bash
python3 scripts/run_analysis.py WZDiBosonAnalysis --outdir run/WZ/samples \
    --samples data_A,data_B,data_C,data_D --jobs 4
```

### `run_analysis.py` options

| Option | Meaning |
|---|---|
| `--outdir DIR` | where per-sample outputs (`histoOut-<file>.root`) and logs (`logs/<sample>.log`) go |
| `--samples a,b,...` | sample keys from `config/samples/<analysis>.yaml` (default: all) |
| `--jobs N` | number of samples processed at the same time |
| `--cutlang-parallel M` | split each sample into M CutLang processes over event ranges (`CLA.sh -j M`; multi-process, merged with `hadd`). `--jobs N` with `--cutlang-parallel M` starts N×M processes |
| `--events N` | process only the first N events of each sample (for tests) |
| `--input-dir DIR` | read ntuples from a local copy with the same directory layout instead of streaming |
| `--cutlang DIR` | CutLang checkout (default: `$CUTLANG_DIR`) |
| `--progress-interval SEC` | status update interval (default 5; 0 disables it) |
| `--force` | re-run samples whose output exists |

### `normalize_merge.py` options

| Option | Meaning |
|---|---|
| `--indir DIR` | per-sample outputs from `run_analysis.py` |
| `--outdir DIR` | where the merged `<group>.root` files go |
| `--per-sample` | also write each normalised sample to `<outdir>/samples/<sample>.root` |
| `--allow-missing` | merge groups from the samples that are present |

## Outputs

```
run/<analysis>/samples/histoOut-<ntuple>.root   one CutLang output per sample (unnormalised MC)
run/<analysis>/samples/logs/<sample>.log        CutLang log per sample
run/<analysis>/merged/<group>.root              normalised and merged, one file per group
```

Each output file has one directory per ADL `region`, containing the region's
histograms and its `cutflow` histogram (one bin per selection, labelled with
the ADL statement).

## Event weights and normalisation

- **Data:** weight = 1.
- **Simulation:** each event is weighted by `XSection × Lumi × scale factors × mcWeight`
  in the ADL (`Lumi` = 10064 pb⁻¹). After the run, each sample is scaled by
  `1/(sumw × eff)`, using the sums of weights and efficiencies of the reference
  framework (`Plotting/inputfiles/Files_*.txt` at tag `10fb-legacy`). These values
  are recorded per sample in `config/samples/<analysis>.yaml`. This is the
  same normalisation the reference framework applies.
- **Single-top samples** (DSID 410011–410026) use the sign of `mcWeight`, not the actual value and their sum
  of weights is the number of generated events, as in the reference framework.
- **Data vs simulation** is decided in the ADL by `channelNumber`, which holds
  the run number for data (< 310000). The Z′ signal (DSID 301325) is excluded
  from this test explicitly.
- **Raw-count cutflow bins** (those before the first `weight` statement) are not rescaled.

## Validation

`scripts/compare_outputs.py A.root B.root` compares two CutLang outputs
histogram by histogram, and cutflows bin by bin by label.

- The single-ADL workflow with post-run normalisation was checked against the
  per-sample-ADL workflow used for the article: data, simulated and single-top
  samples of the Z′ and Z boson analyses, and the Z′ signal. All histograms and
  cutflow bins agree within a relative difference of 10⁻⁶.
- Splitting a sample into several CutLang processes (`--cutlang-parallel`) gives
  identical outputs to a single process.

## Performance benchmark

`benchmark/bench_Zee.C` replaces `run.sh` and `main_ZBosonAnalysis.C` of the Open Data
framework's Z boson analysis and processes only the Z → ee sample. Copy it into
`Analysis/ZBosonAnalysis/` of the framework at tag `10fb-legacy` and run it from there:

```bash
root -l -b -q 'bench_Zee.C("<path>/mc_361106.Zee.2lep.root", N)'
```

N = 1 runs sequentially; N > 1 uses N PROOF-Lite workers. An optional third argument sets
the PROOF-Lite sandbox directory, and a fourth limits the number of events.

## Configuration files

`config/samples/<analysis>.yaml`:

```yaml
analysis: TTbarAnalysis
adl: analyses/TTbarAnalysis/TTbarAnalysis.adl
ntuple_base_url: root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22
samples:
  ttbar_lep:
    type: mc
    dsid: 410000
    file: 1lep/MC/mc_410000.ttbar_lep.1lep.root   # relative to ntuple_base_url
    xsec: 452.693559                               # pb
    sumw: 49386600.0
    eff: 1.0
groups:                                            # merged output files <group>.root
  ttbar: [ttbar_lep]
```

`docs/samples.md` lists all samples in readable form.

## Repository layout

```
analyses/<A>/<A>.adl        one ADL per analysis, used for every sample
config/samples/<A>.yaml     input files, cross-sections, sums of weights, merge groups
scripts/run_analysis.py     run CutLang over the samples of an analysis
scripts/normalize_merge.py  normalise MC by 1/(sumw*eff) and merge into groups
scripts/compare_outputs.py  bin-by-bin comparison of two CutLang output files
scripts/plot_all.py         plotting the merged outputs
docs/                       samples.md, download.md (+ download/<A>.txt URL lists, <A>.sha256 checksums)
benchmark/bench_Zee.C       Running the Open Data framework for performance benchmark (Z boson analysis, Z→ee only)
```

## Citing

If you use this suite, please cite the article [TBD: reference] and the
release used ([TBD: Zenodo DOI]). The ADL files build on the
[ADL4LHCOpenData](https://github.com/ADL4HEP/ADL4LHCOpenData) collection.

## Licence

[TBD]
