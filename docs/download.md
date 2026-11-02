# Downloading the input samples

By default `scripts/run_analysis.py` streams the ntuples over XRootD from
`eospublic.cern.ch`. With a slow or unstable connection it is faster to download
the files once (over HTTP, with the lists below) and run from disk with `--input-dir`.

## Download lists

`docs/download/` has one URL list per analysis, and `all.txt` with every file
needed by the nine analyses (files shared by several analyses appear once).

| Analysis | List | Files | Size |
|---|---|---|---|
| HZZAnalysis | [`download/HZZAnalysis.txt`](download/HZZAnalysis.txt) | 33 | 306 MB |
| SUSYAnalysis | [`download/SUSYAnalysis.txt`](download/SUSYAnalysis.txt) | 105 | 19.6 GB |
| SingleTopAnalysis | [`download/SingleTopAnalysis.txt`](download/SingleTopAnalysis.txt) | 65 | 69.9 GB |
| TTbarAnalysis | [`download/TTbarAnalysis.txt`](download/TTbarAnalysis.txt) | 29 | 50.5 GB |
| WBosonAnalysis | [`download/WBosonAnalysis.txt`](download/WBosonAnalysis.txt) | 65 | 69.9 GB |
| WZDiBosonAnalysis | [`download/WZDiBosonAnalysis.txt`](download/WZDiBosonAnalysis.txt) | 29 | 924 MB |
| ZBosonAnalysis | [`download/ZBosonAnalysis.txt`](download/ZBosonAnalysis.txt) | 29 | 16.7 GB |
| ZPrimeBoostedAnalysis | [`download/ZPrimeBoostedAnalysis.txt`](download/ZPrimeBoostedAnalysis.txt) | 64 | 4.5 GB |
| ZZDiBosonAnalysis | [`download/ZZDiBosonAnalysis.txt`](download/ZZDiBosonAnalysis.txt) | 29 | 593 MB |
| **all analyses** | [`download/all.txt`](download/all.txt) | 311 | 112.5 GB |

Several analyses read the same stream: TTbar, W boson and single top all use
`1lep`, so one download serves all three.

## Directory layout

`--input-dir DIR` expects the same layout as on the server below
`http://opendata.cern.ch/eos/opendata/atlas/OutreachDatasets/2020-01-22/`, i.e. `DIR/<stream>/Data/...` and `DIR/<stream>/MC/...`:

```
DIR/1lep/Data/data_A.1lep.root
DIR/1lep/MC/mc_410000.ttbar_lep.1lep.root
...
```

## Downloading

With `wget` (`-x -nH --cut-dirs=5` recreates exactly that layout; `-c`
resumes interrupted downloads):

```bash
mkdir -p ~/atlas-opendata && cd ~/atlas-opendata
wget -c -x -nH --cut-dirs=5 -i /path/to/ADL4ATLASOpenData/docs/download/TTbarAnalysis.txt
```

With `curl` (available by default on macOS):

```bash
mkdir -p ~/atlas-opendata && cd ~/atlas-opendata
while read -r url; do
  # path below the base URL, e.g. 1lep/MC/mc_410000.ttbar_lep.1lep.root
  rel=${url#http://opendata.cern.ch/eos/opendata/atlas/OutreachDatasets/2020-01-22/}
  mkdir -p "$(dirname "$rel")"
  curl -fL --retry 5 -C - -o "$rel" "$url"
done < /path/to/ADL4ATLASOpenData/docs/download/TTbarAnalysis.txt
```

## Checking the downloaded files

Next to every list, `docs/download/<analysis>.sha256` (and `all.sha256`) holds the
SHA-256 checksums of its files, with paths relative to the download directory.
Run the check from that directory; every file should print `OK`:

```bash
cd ~/atlas-opendata
sha256sum -c /path/to/ADL4ATLASOpenData/docs/download/TTbarAnalysis.sha256
# macOS: shasum -a 256 -c /path/to/ADL4ATLASOpenData/docs/download/TTbarAnalysis.sha256
```

The checksums were computed on lxplus in November 2026 from the files in
`/eos/opendata/atlas/OutreachDatasets/2020-01-22/` 

## Running from the local copy

```bash
python3 scripts/run_analysis.py TTbarAnalysis --outdir run/TTbar/samples \
    --input-dir ~/atlas-opendata --jobs 4
```

Everything else (normalisation, merging, outputs) is the same as for streamed input.
