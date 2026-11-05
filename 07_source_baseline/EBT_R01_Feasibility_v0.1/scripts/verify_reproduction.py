#!/usr/bin/env python3
"""Verify the synthetic EBT feasibility reproduction against tracked results.

Numerical equivalence is assessed within declared, small tolerances, not by
bitwise equality across different NumPy/SciPy/BLAS versions. Original tracked
bytes are fetched from Git HEAD; generated SHA-256 checksums must still agree
exactly with regenerated files. This is NOT physical/experimental validation.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]  # repository root containing 07_source_baseline
FILES = (
    "data/synthetic/baseline_synthetic.csv",
    "data/synthetic/heldout_synthetic.csv",
    "results/metrics.json",
)
CSV_ABS_TOL = 1e-6  # degree Celsius for temperature columns; also numeric columns
CSV_REL_TOL = 1e-7
METRIC_ABS_TOL = 1e-9
METRIC_REL_TOL = 1e-7


def committed_bytes(path: str) -> bytes:
    path_in_git = (ROOT / path).relative_to(REPO_ROOT).as_posix()
    return subprocess.check_output(
        ["git", "show", f"HEAD:{path_in_git}"], cwd=REPO_ROOT
    )


def equal_number(a: float, b: float, *, atol: float, rtol: float) -> bool:
    return math.isfinite(a) and math.isfinite(b) and math.isclose(
        a, b, rel_tol=rtol, abs_tol=atol
    )


def verify_csv(path: str) -> int:
    a = list(csv.DictReader(io.StringIO(committed_bytes(path).decode("utf-8"))))
    b = list(csv.DictReader((ROOT / path).open(encoding="utf-8", newline="")))
    if not a or len(a) != len(b):
        raise AssertionError(f"{path}: changed row count ({len(a)} to {len(b)})")
    if a[0].keys() != b[0].keys():
        raise AssertionError(f"{path}: changed column names/order")
    count = 0
    for i, (ra, rb) in enumerate(zip(a, b, strict=True)):
        for column in ra:
            if not equal_number(float(ra[column]), float(rb[column]),
                                atol=CSV_ABS_TOL, rtol=CSV_REL_TOL):
                raise AssertionError(
                    f"{path}: row {i} col {column} differs: "
                    f"{ra[column]} versus {rb[column]}"
                )
            count += 1
    return count


def recursively_compare(a: object, b: object, where: str = "results") -> int:
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            raise AssertionError(f"{where}: JSON keys differ")
        return sum(recursively_compare(a[k], b[k], f"{where}.{k}") for k in a)
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise AssertionError(f"{where}: list length differs")
        return sum(recursively_compare(x, y, f"{where}[{i}]")
                   for i, (x, y) in enumerate(zip(a, b, strict=True)))
    if type(a) is not type(b):
        raise AssertionError(f"{where}: JSON value type differs")
    if isinstance(a, float):
        if not equal_number(a, b, atol=METRIC_ABS_TOL, rtol=METRIC_REL_TOL):
            raise AssertionError(f"{where}: {a} versus {b}")
    elif a != b:
        raise AssertionError(f"{where}: {a!r} versus {b!r}")
    return 1


def main() -> None:
    counts = {p: verify_csv(p) for p in FILES if p.endswith(".csv")}
    reference = json.loads(committed_bytes("results/metrics.json"))
    regenerated = json.loads((ROOT / "results/metrics.json").read_text())
    counts["results/metrics.json"] = recursively_compare(reference, regenerated)
    if "SYNTHETIC" not in regenerated["disclaimer"].upper():
        raise AssertionError("Synthetic-data disclaimer missing")

    hashes = json.loads((ROOT / "results/SHA256SUMS.json").read_text())
    if set(hashes) != set(FILES):
        raise AssertionError("Regenerated checksum manifest omits/adds files")
    for rel, digest in hashes.items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if digest != actual:
            raise AssertionError(f"SHA-256 mismatch for regenerated {rel}")

    print("PASS: synthetic benchmark reproduces within declared tolerances")
    print(f"CSV atol={CSV_ABS_TOL}, rtol={CSV_REL_TOL}; "
          f"JSON atol={METRIC_ABS_TOL}, rtol={METRIC_REL_TOL}")
    print("Numeric cells checked:", counts)
    print("PASS: exact regenerated-output SHA-256 internal integrity")
    print("LIMITATION: this does not establish real device validation or calibration")


if __name__ == "__main__":
    main()