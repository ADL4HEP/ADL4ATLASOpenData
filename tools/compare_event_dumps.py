#!/usr/bin/env python3
"""Compare the events selected by ADL/CutLang and by the ATLAS Open Data framework.

Events of the two dump files are matched on (runNumber, eventNumber). The script prints how
many events both select, and every event that only one of them selects.

A dump file can hold one sample or a merged group: for a group, concatenate the per-sample
files first, e.g. `cat data_A.csv data_B.csv data_C.csv data_D.csv > data.csv`. Within a
file every (runNumber, eventNumber) must be unique; simulated samples all have the same
runNumber, so duplicates are reported when MC samples are merged.

Usage:
  python3 compare_event_dumps.py --files <cutlang.csv> <framework.csv> [--out <prefix>]
"""
import argparse
import csv
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


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--files", nargs=2, required=True, metavar=("CUTLANG_CSV", "FRAMEWORK_CSV"))
    p.add_argument("--out", help="write <prefix>_cutlang_only.csv and <prefix>_framework_only.csv")
    a = p.parse_args()

    cl_cols, cl = read_dump(a.files[0])
    fw_cols, fw = read_dump(a.files[1])

    print(f"{'Both':>10}{'CutLang only':>16}{'Open Data Framework only':>28}")
    print(f"{len(cl.keys() & fw.keys()):>10}{len(cl.keys() - fw.keys()):>16}{len(fw.keys() - cl.keys()):>28}")

    for side, cols, mine, other in (("cutlang", cl_cols, cl, fw), ("framework", fw_cols, fw, cl)):
        only = [mine[k] for k in sorted(mine.keys() - other.keys())]
        if not only:
            continue
        if a.out:  # written before printing, so a cut-off terminal output does not lose it
            with open(f"{a.out}_{side}_only.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(cols)
                w.writerows(only)
        print(f"\nSelected by {side} only:")
        print("  " + ", ".join(cols))
        for row in only:
            print("  " + ", ".join(row))


if __name__ == "__main__":
    main()
