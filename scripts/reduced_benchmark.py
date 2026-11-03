#!/usr/bin/env python3
"""Reduced benchmark: run all nine analyses on the test skims and compare with the reference.

Every ADL in analyses/ is run with CutLang on its 5000-event skim in tests/skims/ (local files,
no network). Each output is compared bin by bin, cutflows by label, with the reference output in
tests/reference/<analysis>/ (tools/compare_cutlang_outputs.py, relative tolerance 1e-6).
The outputs are raw CutLang outputs: the normalisation in config/samples/ refers to the full
samples and is not applied.

Usage:
  reduced_benchmark.py [--outdir run/reduced] [--jobs N] [--cutlang DIR] [--reference DIR]
  reduced_benchmark.py --make-reference [--jobs N] [--cutlang DIR] [--reference DIR]

Exit code 1 if any analysis fails to run or differs from the reference.
"""
import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
from compare_cutlang_outputs import compare_dirs  # noqa: E402

SKIMS = REPO / "tests" / "skims"
REFERENCE = REPO / "tests" / "reference"

# analysis -> skim in tests/skims/ (see tests/skims/README.md)
SKIM_OF = {
    "ZBosonAnalysis": "mc_363490.llll.2lep.5000evt.root",
    "WBosonAnalysis": "mc_410000.ttbar_lep.1lep.5000evt.root",
    "SingleTopAnalysis": "mc_410011.single_top_tchan.1lep.5000evt.root",
    "ZPrimeBoostedAnalysis": "mc_301325.ZPrime1000_tt.1largeRjet1lep.5000evt.root",
    "HZZAnalysis": "mc_345060.ggH125_ZZ4lep.4lep.5000evt.root",
    "ZZDiBosonAnalysis": "mc_363490.llll.4lep.5000evt.root",
    "WZDiBosonAnalysis": "mc_363491.lllv.3lep.5000evt.root",
    "TTbarAnalysis": "mc_410000.ttbar_lep.1lep.5000evt.root",
    "SUSYAnalysis": "mc_392985.SlepSlep_direct_600p0_300p0_2L8.2lep.5000evt.root",
}


def run_cutlang(analysis, target_dir, log, cutlang):
    """Run one ADL on its skim; return (ok, message). Output: <target_dir>/histoOut-<skim>."""
    skim = SKIM_OF[analysis]
    adl = REPO / "analyses" / analysis / f"{analysis}.adl"
    target_dir.mkdir(parents=True, exist_ok=True)
    log.parent.mkdir(parents=True, exist_ok=True)
    cmd = [str(cutlang / "runs" / "CLA.sh"), str(SKIMS / skim), "ATLASODR2", "-i", str(adl)]
    with tempfile.TemporaryDirectory(prefix=f"reduced_{analysis}_") as work:
        with open(log, "w") as fh:
            rc = subprocess.run(cmd, cwd=work, stdout=fh, stderr=subprocess.STDOUT).returncode
        produced = Path(work) / f"histoOut-{analysis}.root"
        if rc != 0 or not produced.exists():
            return False, f"CutLang failed (rc={rc}), see {log}"
        shutil.move(str(produced), target_dir / f"histoOut-{skim}")
    return True, ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--outdir", default=str(REPO / "run" / "reduced"),
                    help="where the outputs and logs go (default: run/reduced)")
    ap.add_argument("--jobs", type=int, default=1, help="analyses run at the same time")
    ap.add_argument("--cutlang", default=os.environ.get("CUTLANG_DIR", "CutLang"),
                    help="CutLang checkout (default: $CUTLANG_DIR)")
    ap.add_argument("--reference", default=str(REFERENCE),
                    help="reference outputs, one directory per analysis (default: tests/reference)")
    ap.add_argument("--make-reference", action="store_true",
                    help="write the outputs to the reference directory instead of comparing")
    args = ap.parse_args()

    cutlang = Path(args.cutlang).resolve()
    if not (cutlang / "runs" / "CLA.sh").exists():
        sys.exit(f"no CutLang at {cutlang}: set $CUTLANG_DIR or give --cutlang")
    outdir, reference = Path(args.outdir).resolve(), Path(args.reference).resolve()
    results = reference if args.make_reference else outdir   # where the .root outputs go

    analyses = list(SKIM_OF)
    print(f"Running {len(analyses)} analyses on the test skims with {cutlang} ...", flush=True)
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        runs = dict(zip(analyses, pool.map(
            lambda a: run_cutlang(a, results / a, outdir / a / "logs" / f"{a}.log", cutlang), analyses)))

    if args.make_reference:
        for a, (ok, msg) in runs.items():
            print(f"{a:24s} {'written to ' + str(reference / a) if ok else 'FAIL  ' + msg}")
        sys.exit(0 if all(ok for ok, _ in runs.values()) else 1)

    n_ok = 0
    for a, (ok, msg) in runs.items():
        if not ok:
            print(f"{a:24s} FAIL  {msg}")
            continue
        text = io.StringIO()
        ok = compare_dirs(reference / a, outdir / a, out=text)
        n_ok += ok
        last = text.getvalue().strip().splitlines()[-1]   # "<n>/<m> files match ...; max rel. diff x"
        print(f"{a:24s} {'OK  ' if ok else 'FAIL'}  max rel. diff {last.rsplit('max rel. diff ', 1)[-1]}")
        if not ok:
            print("    " + text.getvalue().strip().replace("\n", "\n    "))
    print(f"Reduced benchmark: {n_ok}/{len(analyses)} analyses reproduce the reference outputs"
          f" (outputs in {outdir})")
    sys.exit(0 if n_ok == len(analyses) else 1)


if __name__ == "__main__":
    main()
