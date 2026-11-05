# EBT v0.7 — physical-readiness and experimental-identity gate

**STATUS: DOCUMENTED PREDESIGN / AUTHORIZATION NOT GRANTED / NO REAL MEASUREMENTS.** This is not a build release, electrical SOP, calibration record or completed Q0 campaign.

This stage targets the highest-leverage unknowns from v0.5 and the v0.6 spatial analysis: actual sink geometry, the adapter plate's heat-path confounding, where each sensor really measures temperature, and whether the facility provides defensible instrument evidence.

## New evidence and decisions

- [SK 92 source-grade assessment](evidence/EBT-MEC-007_manufacturer_profile_review.md) — series-family drawing establishes **nominal 10 mm base thickness**, while flat contact geometry and drilling permissions remain unverified.
- [Fixture alternatives](docs/EBT-MEC-007_fixture_architecture_decision.md) — direct-to-sink prioritized **for review**; the proposed 4 mm adapter plate remains an explicit alternative. No manufacturing coordinates are released.
- [Illustrative thermal mass calculator](thermal_mass.py) — 100 × 100 × 4 mm Al under assumed density/cp adds about 97.2 J/K; not measured or a predicted time constant.
- [Inspection register](facility/EBT-G2-007_inspection_register.csv) — 23 site, mechanical, electrical, metrology, reproducibility and rights checks; all require real evidence, none marked completed.
- [Pilot source/site crossover and data firewall](protocol/EBT-Q0-007_crossover_and_holdout.md) — independent remounts, QUAL/CAL/HOLD separation, controlled failure gates; zero physical runs.
- [Evidence completeness checker](validate_g2.py) + [intentionally incomplete record](templates/EBT-GATE-007_record_UNFILLED.json) and [tests](tests/test_readiness.py).

## Run offline

From this directory, Python 3.11+ (no third-party packages required):

    python -m unittest discover -s tests -p 'test_*.py' -v
    python thermal_mass.py
    python validate_g2.py templates/EBT-GATE-007_record_UNFILLED.json

The last command **must exit code 2** and show stages as BLOCKED; this is the correct outcome for a laboratory that has not yet been inspected or authorized. A structurally filled record remains HUMAN_REVIEW_REQUIRED, never SAFE or GO.

## Next physical evidence

1. Complete the KTH Student Workshop Canvas/induction for mechanical fabrication if access is actually granted.
2. Locate a separately authorized powered-testing laboratory and obtain a named supervisor and written scope.
3. Inspect real SK 92 sink/mount hardware and thermometry, record actual part serial/geometry, and choose **one** reviewable fixture architecture.
4. Only then make an approved as-built wiring and machining release, real sensor-lag/uncertainty plan and Q0 operating envelope.

Draft PR #11 contains the separate v0.6 numerical spatial test; this v0.7 package is written independently on the v0.5 base to avoid treating that draft numerical model as physical proof.
