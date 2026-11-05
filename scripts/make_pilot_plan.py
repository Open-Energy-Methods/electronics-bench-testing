#!/usr/bin/env python3
"""Generate a deterministic *unpowered planning* matrix for EBT-Q0.

No electrical power, current, temperature setpoint, or permission is defined.
The generated CSV is NOT an authorized test or an experimental dataset.
"""
from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path

FIELDS = ("sequence", "run_id", "assembly_id", "cooling", "power_label", "planned_status")
COOLING = ("NAT", "FAN")
POWER = ("P1", "P2")
ASSEMBLY = ("A01", "A02", "A03")


def generate_plan(seed: int = 20261105) -> list[dict[str, str]]:
    rng = random.Random(seed)
    plan: list[dict[str, str]] = []
    seq = 1
    for assembly in ASSEMBLY:
        cases = [(c, p) for c in COOLING for p in POWER]
        rng.shuffle(cases)
        for cooling, power in cases:
            plan.append({
                "sequence": str(seq),
                "run_id": f"Q0-{assembly}-{cooling}-{power}",
                "assembly_id": assembly,
                "cooling": cooling,
                "power_label": power,
                "planned_status": "NOT_AUTHORIZED",
            })
            seq += 1
    return plan


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261105)
    parser.add_argument("--out", type=Path, required=True)
    opts = parser.parse_args()
    opts.out.parent.mkdir(parents=True, exist_ok=True)
    with opts.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(generate_plan(seed=opts.seed))
    print(f"Wrote 12 PLANNING-ONLY rows to {opts.out}")


if __name__ == "__main__":
    main()
