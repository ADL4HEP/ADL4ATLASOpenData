#!/usr/bin/env python3
"""Compare CutLang and ATLAS Open Data framework cutflows at their synchronisation points.

The framework fills one cutflow bin per selection stage of its C++ code (bin k+1 = stage k);
CutLang fills one bin per ADL statement, in the ADL order. The two are compared only where
the same set of cuts has been applied, as listed in the `opendata_cutflow` stage map of
config/samples/<analysis>.yaml. Stages without a CutLang equivalent are skipped.

Inputs, merged into the same groups (scripts/normalize_merge.py):
  --cutlang DIR             weighted, normalised CutLang outputs (<group>.root)
  --cutlang-unweighted DIR  CutLang outputs of the ADL without its `weight` line (raw counts)
  --opendata DIR            framework outputs merged with `normalize_merge.py --opendata`
Weighted: CutLang cutflow vs hist_cutflow_w; stage ALL is the CutLang `weight` bin.
Unweighted: CutLang raw-count cutflow vs hist_cutflow_unw; must agree exactly.
Weighted values agree if |a-b| <= rtol*max(|a|,|b|) (default 1e-5: the framework's per-event
weight is single precision); data groups must agree exactly.

Usage:
  compare_cutflows.py <analysis> --opendata DIR [--cutlang DIR] [--cutlang-unweighted DIR]
                      [--rtol 1e-5] [--csv FILE]
Output: one table per mode, cuts as rows (CutLang and Open Data line), groups as columns;
where the values differ beyond the tolerance, "Δ" gives CutLang - Open Data.
Exit code 1 if any synchronisation point differs.
"""
import argparse
import csv
import sys
from pathlib import Path

import ROOT

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from benchlib import load_config, weight_labels  # noqa: E402

ROOT.gROOT.SetBatch(True)
ROOT.TH1.AddDirectory(False)


def read_hist(path, name):
    f = ROOT.TFile.Open(str(path))
    if not f or f.IsZombie():
        raise OSError(f"cannot open {path}")
    h = f.Get(name)
    if not h:
        raise KeyError(f"{name} not found in {path}")
    h = h.Clone()
    f.Close()
    return h


def bins_by_label(h):
    out = {}
    for i in range(1, h.GetNbinsX() + 1):
        lab = h.GetXaxis().GetBinLabel(i)
        if lab and lab not in out:
            out[lab] = i
    return out


def cutlang_bin(labels, stage_label, weighted, weight_bins):
    """Bin index of a stage-map label in a CutLang cutflow."""
    if stage_label == "ALL":
        if weighted:  # the first bin with the event weight applied
            for lab in weight_bins:
                if lab in labels:
                    return labels[lab]
        for lab in ("ALL", "all Events"):
            if lab in labels:
                return labels[lab]
    return labels.get(stage_label)


def compare(cfg, mode, cl_dir, od_dir, rtol, rows):
    smap = cfg["opendata_cutflow"]
    weighted = mode == "weighted"
    od_name = "hist_cutflow_w" if weighted else "hist_cutflow_unw"
    weight_bins = sorted(weight_labels(cfg["adl_path"]))
    n_ok = n_all = 0
    worst = (0.0, "")
    print(f"== {cfg['analysis']}: {mode} cutflows, CutLang {cl_dir} vs Open Data {od_dir}")
    if smap.get("note"):
        print(f"   note: {smap['note']}")
    stages = [st for st in smap["stages"] if st["cutlang"] is not None]
    table, skipped = [], []  # table: (group, [cell per stage])
    for group, keys in cfg["groups"].items():
        cl_path, od_path = Path(cl_dir) / f"{group}.root", Path(od_dir) / f"{group}.root"
        if not cl_path.exists() or not od_path.exists():
            skipped.append(f"{group} (no {'CutLang' if not cl_path.exists() else 'Open Data'} file)")
            continue
        is_data = all(cfg["samples"][k]["type"] == "data" for k in keys)
        exact = is_data or not weighted
        od = read_hist(od_path, od_name)
        cl_cache = {}
        cells = []
        for st in stages:
            k, label = st["stage"], st["cutlang"]
            region = st.get("region", smap["region"])
            if region not in cl_cache:
                h = read_hist(cl_path, f"{region}/cutflow")
                cl_cache[region] = (h, bins_by_label(h))
            h, labels = cl_cache[region]
            i = cutlang_bin(labels, label, weighted, weight_bins)
            if i is None:
                raise KeyError(f"stage {k}: no CutLang cutflow bin '{label}' in {cl_path}:{region}")
            a, b = h.GetBinContent(i), od.GetBinContent(k + 1)
            diff = a - b
            rel = abs(diff) / max(abs(a), abs(b)) if (a or b) else 0.0
            ok = abs(diff) < 0.5 if exact else rel <= rtol
            n_all += 1
            n_ok += ok
            if rel > worst[0]:
                worst = (rel, f"{group}, {label}")
            fmt = "{:.0f}" if exact else "{:.2f}"
            mark = "" if ok else " Δ" + ("{:+.0f}" if exact else "{:+.2f}").format(diff)
            cells.append((fmt.format(a), fmt.format(b) + mark))
            rows.append([cfg["analysis"], mode, group, k, st["opendata"], label, region,
                         f"{a:.6f}", f"{b:.6f}", f"{diff:.6f}", f"{rel:.3e}", "agree" if ok else "differ"])
        table.append((group, cells))
    print_table([st["cutlang"] for st in stages], table)
    for s in skipped:
        print(f"   skipped: {s}")
    tol = "exact for counts" if not weighted else f"rtol {rtol:g} for weighted MC, exact for data"
    print(f"   Δ = CutLang - Open Data where they differ ({tol}); {n_ok}/{n_all} agree; "
          f"max rel. diff {worst[0]:.2e}" + (f" ({worst[1]})" if worst[1] else ""))
    return n_ok == n_all


def print_table(cuts, table):
    """Cuts as rows (a CutLang and an Open Data line each), groups as columns."""
    groups = [g for g, _ in table]
    w_cut = max(map(len, cuts + ["Cut"]))
    w_src = len("Open Data")
    widths = [max([len(g)] + [max(len(c[0]), len(c[1])) for c in cells]) for g, cells in table]

    def line(cut, src, values):
        cols = [cut.ljust(w_cut), src.ljust(w_src)] + [v.ljust(w) for v, w in zip(values, widths)]
        print("   " + " | ".join(cols).rstrip())

    rule = "   " + "-+-".join("-" * w for w in [w_cut, w_src] + widths)
    line("Cut", "", groups)
    print(rule)
    for j, cut in enumerate(cuts):
        line(cut, "CutLang", [cells[j][0] for _, cells in table])
        line("", "Open Data", [cells[j][1] for _, cells in table])
        print(rule)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis", help="analysis name or path to its samples YAML")
    ap.add_argument("--opendata", required=True, help="framework outputs merged with normalize_merge.py --opendata")
    ap.add_argument("--cutlang", help="weighted, normalised CutLang <group>.root files")
    ap.add_argument("--cutlang-unweighted", help="CutLang <group>.root files of the unweighted ADL")
    ap.add_argument("--rtol", type=float, default=1e-5, help="relative tolerance for weighted MC (default 1e-5)")
    ap.add_argument("--csv", help="also write every synchronisation point to this CSV file")
    args = ap.parse_args()
    if not args.cutlang and not args.cutlang_unweighted:
        ap.error("give --cutlang and/or --cutlang-unweighted")

    cfg = load_config(args.analysis)
    if "opendata_cutflow" not in cfg:
        sys.exit(f"no opendata_cutflow stage map in the config of {args.analysis}")
    rows, ok = [], True
    if args.cutlang:
        ok &= compare(cfg, "weighted", args.cutlang, args.opendata, args.rtol, rows)
    if args.cutlang_unweighted:
        ok &= compare(cfg, "unweighted", args.cutlang_unweighted, args.opendata, args.rtol, rows)
    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["analysis", "mode", "group", "stage", "opendata_stage", "cutlang_label", "region",
                        "cutlang", "opendata", "diff", "rel_diff", "status"])
            w.writerows(rows)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
