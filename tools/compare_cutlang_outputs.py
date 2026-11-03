#!/usr/bin/env python3
"""Compare CutLang output files histogram by histogram.

Histograms are compared bin by bin (including under/overflow) with a relative
tolerance. Cutflows are matched by bin label, so a cut present in only one file
(for instance an extra `weight` line) is reported but does not shift the rest.

Usage:
  compare_cutlang_outputs.py A.root B.root [--rtol 1e-6] [--atol 1e-9]
  compare_cutlang_outputs.py --ref REF_DIR --new NEW_DIR [--rtol 1e-6] [--atol 1e-9]

The directory mode compares every <name>.root in REF_DIR (e.g.
reference_results/<analysis>/CutLang) with the file of the same name in NEW_DIR
(e.g. run/<analysis>/merged). A file or histogram of the reference that is
missing from NEW_DIR is a failure.
Exit code 1 if anything differs.
"""
import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import uproot


@dataclass
class Comparison:
    compared: int = 0
    mismatches: list = field(default_factory=list)   # (name, detail)
    only_a: list = field(default_factory=list)
    only_b: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    max_rel: float = 0.0        # largest relative bin difference over all compared histograms
    max_rel_where: str = ""

    @property
    def ok(self):
        return not self.mismatches


def histograms(path):
    with uproot.open(path) as f:
        return {k.split(";")[0]: f[k] for k, c in f.classnames().items() if c.startswith("TH1")}


def bin_labels(h):
    """Axis labels by bin. Read fLabels directly: uproot's axis().labels()
    returns nothing for some PyROOT-written histograms. Each label's UniqueID
    is its (1-based) bin number."""
    labels = h.member("fXaxis").member("fLabels")
    if labels is None:
        return []
    out = [""] * len(h.values())
    for obj in labels:
        out[obj.member("@fUniqueID") - 1] = str(obj)
    if "" in out:
        raise ValueError(f"cutflow has {out.count('')} unlabelled bins of {len(out)}")
    return out


def cutflow_map(h):
    labels = bin_labels(h)
    if not labels:
        raise ValueError("cutflow histogram without bin labels")
    vals = h.values()
    out = {}
    for i, lab in enumerate(labels):  # repeated labels get an occurrence index
        n = sum(1 for k in out if k[0] == lab)
        out[(lab, n)] = vals[i]
    return out


def close(a, b, rtol, atol):
    return np.allclose(a, b, rtol=rtol, atol=atol)


def track_max_rel(res, name, a, b, where):
    """Keep the largest |a-b|/max(|a|,|b|) seen so far (bins where both are 0 are skipped)."""
    a, b = np.atleast_1d(np.asarray(a, float)), np.atleast_1d(np.asarray(b, float))
    denom = np.maximum(np.abs(a), np.abs(b))
    nz = denom > 0
    if not nz.any():
        return
    rel = np.abs(a - b)[nz] / denom[nz]
    i = int(np.argmax(rel))
    if rel[i] > res.max_rel:
        res.max_rel = float(rel[i])
        res.max_rel_where = f"{name} {where(np.flatnonzero(nz)[i])}"


def compare_files(path_a, path_b, rtol=1e-6, atol=1e-9):
    ha, hb = histograms(path_a), histograms(path_b)
    res = Comparison()
    res.only_a = sorted(set(ha) - set(hb))
    res.only_b = sorted(set(hb) - set(ha))
    for name in sorted(set(ha) & set(hb)):
        a, b = ha[name], hb[name]
        res.compared += 1
        if name.endswith("/cutflow"):
            ma, mb = cutflow_map(a), cutflow_map(b)
            extra = set(ma) ^ set(mb)
            if extra:
                res.notes.append((name, "cuts in one file only: "
                                  + ", ".join(f"{l!r}" for l, _ in sorted(extra))))
            for k in sorted(set(ma) & set(mb)):
                track_max_rel(res, name, ma[k], mb[k], lambda _i, k=k: f"bin {k[0]!r}")
                if not close(ma[k], mb[k], rtol, atol):
                    res.mismatches.append((name, f"bin {k[0]!r}: {ma[k]:.10g} vs {mb[k]:.10g}"))
            continue
        va, vb = a.values(flow=True), b.values(flow=True)
        if va.shape != vb.shape:
            res.mismatches.append((name, f"binning {va.shape} vs {vb.shape}"))
            continue
        track_max_rel(res, name, va, vb, lambda i: f"bin {i}")
        if not close(va, vb, rtol, atol):
            i = int(np.argmax(np.abs(va - vb)))
            res.mismatches.append((name, f"max diff at bin {i}: {va[i]:.10g} vs {vb[i]:.10g} "
                                         f"(sum {va.sum():.10g} vs {vb.sum():.10g})"))
    return res


def report(res, label_a="A", label_b="B", out=sys.stdout):
    print(f"compared {res.compared} histograms: "
          f"{'OK' if res.ok else f'{len(res.mismatches)} MISMATCHES'}", file=out)
    for name, d in res.mismatches:
        print(f"  MISMATCH {name}: {d}", file=out)
    for name, d in res.notes:
        print(f"  note {name}: {d}", file=out)
    if res.only_a:
        print(f"  only in {label_a}: {', '.join(res.only_a)}", file=out)
    if res.only_b:
        print(f"  only in {label_b}: {', '.join(res.only_b)}", file=out)


def compare_dirs(ref_dir, new_dir, rtol=1e-6, atol=1e-9, out=sys.stdout):
    """Compare every <name>.root of ref_dir with new_dir/<name>.root; return True if all match."""
    ref_dir, new_dir = Path(ref_dir), Path(new_dir)
    refs = sorted(ref_dir.glob("*.root"))
    if not refs:
        print(f"no .root files in {ref_dir}", file=out)
        return False
    n_ok, max_rel, max_where = 0, 0.0, ""
    for ref in refs:
        new = new_dir / ref.name
        if not new.exists():
            print(f"{ref.name:24s} FAIL  missing in {new_dir}", file=out)
            continue
        res = compare_files(ref, new, rtol, atol)
        ok = res.ok and not res.only_a      # a reference histogram must also exist in the new file
        n_ok += ok
        print(f"{ref.name:24s} {'OK  ' if ok else 'FAIL'}  ({res.compared} histograms, "
              f"max rel. diff {res.max_rel:.3g})", file=out)
        if not ok or res.notes or res.only_b:
            report(res, "reference", "new", out=out)
        if res.max_rel > max_rel:
            max_rel, max_where = res.max_rel, f"{ref.name}: {res.max_rel_where}"
    extra = sorted({p.name for p in new_dir.glob("*.root")} - {p.name for p in refs})
    if extra:
        print(f"note: not in the reference: {', '.join(extra)}", file=out)
    print(f"{n_ok}/{len(refs)} files match the reference (rtol {rtol:g}, atol {atol:g}); "
          f"max rel. diff {max_rel:.3g}" + (f" at {max_where}" if max_rel else ""), file=out)
    return n_ok == len(refs)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 epilog="Give either two files or --ref and --new.")
    ap.add_argument("files", nargs="*", metavar="FILE", help="two CutLang output files A.root B.root")
    ap.add_argument("--ref", metavar="DIR", help="directory with the reference outputs")
    ap.add_argument("--new", metavar="DIR", help="directory with the new outputs")
    ap.add_argument("--rtol", type=float, default=1e-6)
    ap.add_argument("--atol", type=float, default=1e-9)
    args = ap.parse_args()
    if args.ref or args.new:
        if not (args.ref and args.new) or args.files:
            ap.error("the directory mode needs --ref and --new and no file arguments")
        sys.exit(0 if compare_dirs(args.ref, args.new, args.rtol, args.atol) else 1)
    if len(args.files) != 2:
        ap.error("give two files, or --ref and --new")
    res = compare_files(args.files[0], args.files[1], args.rtol, args.atol)
    report(res, args.files[0], args.files[1])
    if res.compared:
        print(f"  max rel. diff {res.max_rel:.3g}" + (f" at {res.max_rel_where}" if res.max_rel else ""))
    sys.exit(0 if res.ok else 1)


if __name__ == "__main__":
    main()
