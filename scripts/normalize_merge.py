#!/usr/bin/env python3
"""Normalise per-sample CutLang outputs and merge them into plot groups.

Each MC sample is scaled by 1/(sumw*eff) from config/samples/<analysis>.yaml
(XSection and Lumi are already in the ADL event weight). Raw-count cutflow bins
(those before the first `weight` statement) are left untouched. Samples are
then summed into the groups listed in the config.

With --opendata the inputs are the ATLAS Open Data framework outputs
(Output_<analysis>/<sample>.root: histograms at the top level, per-event weights only).
Each MC sample is then scaled by Lumi*xsec/(sumw*eff), Lumi = 10064 pb^-1, as in the
framework's Plotting/Plotting.cxx; the unweighted cutflow hist_cutflow_unw is left
untouched. The hand-set normalisation factors of Plotting.cxx (e.g. ZZ x 1.3 in HZZ)
and its overflow handling are not applied. Data may be one file (data.root) or one
file per period (dataA.root ... dataD.root).

Usage:
  normalize_merge.py <analysis> --indir RUN/samples --outdir RUN/merged [--per-sample]
  normalize_merge.py <analysis> --opendata --indir Output_<analysis> --outdir RUN/opendata
"""
import argparse
import sys
from pathlib import Path

import ROOT

sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchlib import load_config, output_name, scale_factor, weight_labels  # noqa: E402

ROOT.TH1.AddDirectory(False)

OPENDATA_LUMI = 10064.0  # pb^-1, Plotting/Plotting.cxx: m->SetLumi(10064)
OPENDATA_UNWEIGHTED = {"hist_cutflow_unw"}  # event counts, never scaled
ROOT.gROOT.SetBatch(True)


def first_weighted_bin(h, labels):
    """1-based index of the first weighted cutflow bin (nbins+1 if none)."""
    for i in range(1, h.GetNbinsX() + 1):
        if h.GetXaxis().GetBinLabel(i) in labels:
            return i
    return h.GetNbinsX() + 1


def scaled_copy(h, factor, labels):
    out = h.Clone()
    if factor == 1.0:
        return out
    if h.GetName() != "cutflow":
        out.Scale(factor)
        return out
    first = first_weighted_bin(h, labels)
    # A labelled cutflow axis can extend: writing the overflow bin would make
    # ROOT double the axis. Freeze it while rescaling.
    can_extend = out.CanExtendAllAxes()
    out.SetCanExtend(ROOT.TH1.kNoAxis)
    for i in range(first, h.GetNbinsX() + 2):
        out.SetBinContent(i, h.GetBinContent(i) * factor)
        out.SetBinError(i, h.GetBinError(i) * factor)
    if can_extend:
        out.SetCanExtend(ROOT.TH1.kAllAxes)
    return out


def read_objects(path, factor, labels):
    """{dir/name: object} for every histogram (scaled) and TText in a CutLang output."""
    f = ROOT.TFile.Open(str(path))
    if not f or f.IsZombie():
        raise OSError(f"cannot open {path}")
    objs = {}
    for dkey in f.GetListOfKeys():
        d = dkey.ReadObj()
        if not d.InheritsFrom("TDirectory"):
            continue
        for key in d.GetListOfKeys():
            obj = key.ReadObj()
            name = f"{d.GetName()}/{key.GetName()}"
            if obj.InheritsFrom("TH1"):
                objs[name] = scaled_copy(obj, factor, labels)
            elif obj.InheritsFrom("TText"):
                objs[name] = obj.Clone()
            # TNtuple "rntuple" bookkeeping trees are not carried over
    f.Close()
    return objs


def add_into(acc, objs):
    for name, obj in objs.items():
        if name not in acc:
            acc[name] = obj
        elif obj.InheritsFrom("TH1"):
            acc[name].Add(obj)


def write(path, objs):
    path.parent.mkdir(parents=True, exist_ok=True)
    f = ROOT.TFile(str(path), "RECREATE")
    for name in objs:  # preserve directory order of the first input
        if "/" not in name:  # Open Data framework layout: top level
            f.cd()
            objs[name].Write(name)
            continue
        dname, oname = name.split("/", 1)
        d = f.GetDirectory(dname) or f.mkdir(dname)
        d.cd()
        objs[name].Write(oname)
    f.Close()


def opendata_factor(sample):
    """Plotting.cxx normalisation: Lumi*xsec/(sumw*eff) for MC, 1 for data."""
    if sample["type"] == "data":
        return 1.0
    return OPENDATA_LUMI * sample["xsec"] / (sample["sumw"] * sample.get("eff", 1.0))


def opendata_path(indir, key):
    """Framework output of a sample: <key>.root, or without '_' (data_A -> dataA.root)."""
    for name in (key, key.replace("_", "")):
        p = Path(indir) / f"{name}.root"
        if p.exists():
            return p
    return Path(indir) / f"{key}.root"


def read_opendata(path, factor):
    """{name: histogram} of a framework output, scaled (except the unweighted cutflow)."""
    f = ROOT.TFile.Open(str(path))
    if not f or f.IsZombie():
        raise OSError(f"cannot open {path}")
    objs = {}
    for key in f.GetListOfKeys():
        obj = key.ReadObj()
        if obj.InheritsFrom("TH1"):
            h = obj.Clone()
            if factor != 1.0 and key.GetName() not in OPENDATA_UNWEIGHTED:
                h.Scale(factor)
            objs[key.GetName()] = h
    f.Close()
    return objs


def opendata_inputs(cfg, keys, indir):
    """[(label, path, factor)] for one group; data periods may be merged in data.root."""
    found = [(k, opendata_path(indir, k)) for k in keys]
    samples = cfg["samples"]
    if all(samples[k]["type"] == "data" for k in keys) and not any(p.exists() for _, p in found):
        merged = Path(indir) / "data.root"
        if merged.exists():
            return [("data", merged, 1.0)], []
    present = [(k, p, opendata_factor(samples[k])) for k, p in found if p.exists()]
    return present, [k for k, p in found if not p.exists()]


def normalise_sample(cfg, key, indir, labels):
    sample = cfg["samples"][key]
    path = Path(indir) / output_name(sample)
    return read_objects(path, scale_factor(sample), labels)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis", help="analysis name or path to its samples YAML")
    ap.add_argument("--indir", required=True, help="directory with per-sample CutLang outputs")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--per-sample", action="store_true",
                    help="also write each normalised sample as <outdir>/samples/<key>.root")
    ap.add_argument("--allow-missing", action="store_true",
                    help="merge groups from the samples present (reduced runs)")
    ap.add_argument("--opendata", action="store_true",
                    help="inputs are ATLAS Open Data framework outputs (Output_<analysis>/<sample>.root)")
    args = ap.parse_args()

    cfg = load_config(args.analysis)
    if args.opendata:
        merge_opendata(cfg, args)
        return
    labels = weight_labels(cfg["adl_path"])
    outdir = Path(args.outdir)
    missing = []
    for group, keys in cfg["groups"].items():
        acc = {}
        n_empty = 0
        for key in keys:
            out = Path(args.indir) / output_name(cfg["samples"][key])
            if not out.exists():
                if out.with_name(out.name + ".empty").exists():  # 0-event ntuple, contributes nothing
                    n_empty += 1
                else:
                    missing.append(key)
                continue
            objs = normalise_sample(cfg, key, args.indir, labels)
            if args.per_sample:
                write(outdir / "samples" / f"{key}.root", objs)
            add_into(acc, objs)
        if acc:
            write(outdir / f"{group}.root", acc)
            used = len(keys) - n_empty - sum(k in missing for k in keys)
            print(f"{group}.root <- {used}/{len(keys)} samples" + (f" ({n_empty} empty)" if n_empty else ""))
    if missing:
        print(f"missing outputs for {len(missing)} samples: {', '.join(missing)}", file=sys.stderr)
        if not args.allow_missing:
            sys.exit(1)


def merge_opendata(cfg, args):
    outdir = Path(args.outdir)
    missing = []
    for group, keys in cfg["groups"].items():
        inputs, absent = opendata_inputs(cfg, keys, args.indir)
        missing += absent
        acc = {}
        for label, path, factor in inputs:
            objs = read_opendata(path, factor)
            if args.per_sample:
                write(outdir / "samples" / f"{label}.root", objs)
            add_into(acc, objs)
        if acc:
            write(outdir / f"{group}.root", acc)
            print(f"{group}.root <- {len(inputs)} file(s)" + (f", {len(absent)} missing" if absent else ""))
    if missing:
        print(f"missing framework outputs for {len(missing)} samples: {', '.join(missing)}", file=sys.stderr)
        if not args.allow_missing:
            sys.exit(1)


if __name__ == "__main__":
    main()
