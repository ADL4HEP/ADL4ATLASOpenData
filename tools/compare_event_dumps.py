#!/usr/bin/env python3
"""Compare the events selected by ADL/CutLang and by the ATLAS Open Data framework.

Events are matched on (runNumber, eventNumber), sample by sample. The script prints how many
events both select, and every event that only one of them selects.

  CutLang:   <cutlang_dir>/<sample>/<cutlang_file>   (data_A ... data_D should be combined into "data" if needed)
  Open Data Framework: <framework_dir>/<sample>.csv            (data_A ... data_D should be combined into "data" if needed)

Usage:
  python3 compare_event_dumps.py <cutlang_dir> <cutlang_file> <framework_dir> [--out <prefix>]
"""
import argparse
import csv
import os
import sys

DROP = {"EventNo", "totalWeight"}  # not needed for the comparison


def read_dump(path):
    """Return (columns, {(run, event): row}) for one dump file; rows are lists of strings."""
    columns, rows = None, {}
    with open(path) as f:
        for line in f:
            fields = [x.strip() for x in line.strip().lstrip("#").split(",")]
            fields = [x for x in fields if x != ""]
            if not fields:
                continue
            if line.startswith("#"):
                columns = fields
                continue
            row = dict(zip(columns, fields))
            key = (int(row["runNumber"]), int(row["eventNumber"]))
            if key in rows:
                print(f"WARNING: duplicate event {key} in {path}", file=sys.stderr)
            rows[key] = [row[c] for c in columns if c not in DROP]
    return [c for c in columns if c not in DROP], rows


def cutlang_sample(sample):
    return "data" if sample.startswith("data_") else sample


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cutlang_dir")
    p.add_argument("cutlang_file")
    p.add_argument("framework_dir")
    p.add_argument("--out", help="write <prefix>_cutlang_only.csv and <prefix>_framework_only.csv")
    a = p.parse_args()

    cl, cl_cols = {}, None
    for d in sorted(os.listdir(a.cutlang_dir)):
        path = os.path.join(a.cutlang_dir, d, a.cutlang_file)
        if os.path.isfile(path):
            cl_cols, rows = read_dump(path)
            cl.setdefault(cutlang_sample(d), {}).update(rows)

    fw, fw_cols = {}, None
    for f in sorted(os.listdir(a.framework_dir)):
        if f.endswith(".csv"):
            fw_cols, fw[f[:-4]] = read_dump(os.path.join(a.framework_dir, f))

    only = {"cutlang": [], "framework": []}
    print(f"{'Sample':<24}{'Both':>10}{'CutLang only':>14}{'Open Data Framework only':>16}")
    for s in sorted(set(cl) | set(fw)):
        if s not in fw or s not in cl:
            print(f"{s:<24}  missing in {'framework' if s not in fw else 'CutLang'} output")
            continue
        c, f = cl[s], fw[s]
        print(f"{s:<24}{len(c.keys() & f.keys()):>10}{len(c.keys() - f.keys()):>14}{len(f.keys() - c.keys()):>16}")
        only["cutlang"] += [[s] + c[k] for k in sorted(c.keys() - f.keys())]
        only["framework"] += [[s] + f[k] for k in sorted(f.keys() - c.keys())]

    for side, cols in (("cutlang", cl_cols), ("framework", fw_cols)):
        if not only[side]:
            continue
        print(f"\nSelected by {side} only:")
        print("  " + ", ".join(["sample"] + cols))
        for row in only[side]:
            print("  " + ", ".join(row))
        if a.out:
            with open(f"{a.out}_{side}_only.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["sample"] + cols)
                w.writerows(only[side])


if __name__ == "__main__":
    main()
