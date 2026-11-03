#!/usr/bin/env python3
"""Compare two CutLang output files histogram by histogram.

Histograms are compared bin by bin (including under/overflow) with a relative
tolerance. Cutflows are matched by bin label, so a cut present in only one file
(for instance an extra `weight` line) is reported but does not shift the rest.

Usage: compare_cutlang_outputs.py A.root B.root [--rtol 1e-6] [--atol 1e-9]
Exit code 1 if any common histogram differs.
"""
import argparse
import sys
from dataclasses import dataclass, field

import numpy as np
import uproot


@dataclass
class Comparison:
    compared: int = 0
    mismatches: list = field(default_factory=list)   # (name, detail)
    only_a: list = field(default_factory=list)
    only_b: list = field(default_factory=list)
    notes: list = field(default_factory=list)

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
                if not close(ma[k], mb[k], rtol, atol):
                    res.mismatches.append((name, f"bin {k[0]!r}: {ma[k]:.10g} vs {mb[k]:.10g}"))
            continue
        va, vb = a.values(flow=True), b.values(flow=True)
        if va.shape != vb.shape:
            res.mismatches.append((name, f"binning {va.shape} vs {vb.shape}"))
        elif not close(va, vb, rtol, atol):
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--rtol", type=float, default=1e-6)
    ap.add_argument("--atol", type=float, default=1e-9)
    args = ap.parse_args()
    res = compare_files(args.a, args.b, args.rtol, args.atol)
    report(res, args.a, args.b)
    sys.exit(0 if res.ok else 1)


if __name__ == "__main__":
    main()
