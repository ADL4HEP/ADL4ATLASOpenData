#!/usr/bin/env python3
"""Write download lists for the ntuples of every analysis.

  docs/download/<analysis>.txt  one URL per line (for wget -i / curl)
  docs/download/all.txt         all files of all analyses, without duplicates
  docs/download.md              instructions and per-analysis sizes

The SHA-256 checksum files docs/download/*.sha256 are not written by this script: they were
computed once on lxplus from /eos/opendata/atlas/OutreachDatasets/2020-01-22/.

Sizes are obtained with HTTP HEAD requests (nothing is downloaded); use
--no-sizes to skip them when offline.
"""
import argparse
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import REPO, load_config  # noqa: E402

# the configs stream over XRootD; downloads use the HTTP address of the same EOS directory
DOWNLOAD_BASE = "http://opendata.cern.ch/eos/opendata/atlas/OutreachDatasets/2020-01-22"

GUIDE = """\
# Downloading the input samples

By default `scripts/run_analysis.py` streams the ntuples over XRootD from
`eospublic.cern.ch`. With a slow or unstable connection it is faster to download
the files once (over HTTP, with the lists below) and run from disk with `--input-dir`.

## Download lists

`docs/download/` has one URL list per analysis, and `all.txt` with every file
needed by the nine analyses (files shared by several analyses appear once).

| Analysis | List | Files | Size |
|---|---|---|---|
{rows}

Several analyses read the same stream: TTbar, W boson and single top all use
`1lep`, so one download serves all three.

## Directory layout

`--input-dir DIR` expects the same layout as on the server below
`{base}/`, i.e. `DIR/<stream>/Data/...` and `DIR/<stream>/MC/...`:

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
  rel=${{url#{base}/}}
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
`/eos/opendata/atlas/OutreachDatasets/2020-01-22/`, the copies used for the reference
results. The CERN Open Data portal records of the 2020 release point to the copies in
`OutreachDatasets/2020-08-19/`, which are not identical byte by byte and do not pass this
check: download from the lists above. Streamed input is not checked.

## Running from the local copy

```bash
python3 scripts/run_analysis.py TTbarAnalysis --outdir run/TTbar/samples \\
    --input-dir ~/atlas-opendata --jobs 4
```

Everything else (normalisation, merging, outputs) is the same as for streamed input.
"""


def head_size(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, method="HEAD")
            return int(urllib.request.urlopen(req, timeout=60).headers["Content-Length"])
        except Exception:
            time.sleep(2 + 2 * attempt)
    return None


def human(n):
    return "?" if n is None else f"{n / 1e9:.1f} GB" if n >= 1e9 else f"{n / 1e6:.0f} MB"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-sizes", action="store_true", help="do not query file sizes")
    args = ap.parse_args()

    outdir = REPO / "docs" / "download"
    outdir.mkdir(parents=True, exist_ok=True)
    per_analysis = {}
    for path in sorted((REPO / "config" / "samples").glob("*.yaml")):
        cfg = load_config(path)
        urls = sorted({f"{DOWNLOAD_BASE}/{s['file']}" for s in cfg["samples"].values()})
        per_analysis[cfg["analysis"]] = urls
        (outdir / f"{cfg['analysis']}.txt").write_text("\n".join(urls) + "\n")
    all_urls = sorted({u for urls in per_analysis.values() for u in urls})
    (outdir / "all.txt").write_text("\n".join(all_urls) + "\n")

    sizes = {}
    if not args.no_sizes:
        with ThreadPoolExecutor(4) as pool:
            sizes = dict(zip(all_urls, pool.map(head_size, all_urls)))

    def total(urls):
        if args.no_sizes or any(sizes.get(u) is None for u in urls):
            return "?"
        return human(sum(sizes[u] for u in urls))

    rows = [f"| {a} | [`download/{a}.txt`](download/{a}.txt) | {len(u)} | {total(u)} |"
            for a, u in per_analysis.items()]
    rows.append(f"| **all analyses** | [`download/all.txt`](download/all.txt) | {len(all_urls)} | {total(all_urls)} |")
    (REPO / "docs" / "download.md").write_text(GUIDE.format(rows="\n".join(rows), base=DOWNLOAD_BASE))
    missing = [u for u in all_urls if not args.no_sizes and sizes.get(u) is None]
    print(f"wrote docs/download.md and {len(per_analysis) + 1} lists in docs/download/ "
          f"({len(all_urls)} files" + (f", {len(missing)} without size" if missing else "") + ")")


if __name__ == "__main__":
    main()
