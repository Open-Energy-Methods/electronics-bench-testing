"""Offline integrity checks for the critical literature evidence register.

These checks establish *documentation structure*, NOT the correctness of any
source's scientific findings or a systematic-review / novelty clearance.
"""
from __future__ import annotations

import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "08_project_controls/fulltext_evidence_matrix_v0.3.csv"
LOG = ROOT / "08_project_controls/literature_search_log_v0.3.csv"
ALLOWED_GRADES = {"F-PDF", "F-HTML", "T", "A", "R"}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


class LiteratureEvidenceTests(unittest.TestCase):
    def test_sources_have_unique_ids_and_explicit_access_grades(self):
        rows = read_rows(MATRIX)
        self.assertGreaterEqual(len(rows), 14)
        ids = [r["source_id"] for r in rows]
        self.assertEqual(len(ids), len(set(ids)))
        for r in rows:
            with self.subTest(source=r["source_id"]):
                self.assertIn(r["access_grade"], ALLOWED_GRADES)
                self.assertTrue(r["authors_year"])
                self.assertTrue(r["short_title"])
                self.assertTrue(r["full_text_url"].startswith("https://"))
                self.assertTrue(r["actual_evidence_reviewed"])
                self.assertTrue(r["unresolved_method_info"])
                self.assertTrue(r["ebt_claim_consequence"])

    def test_search_log_evidence_is_traceable(self):
        rows = read_rows(MATRIX)
        entries = read_rows(LOG)
        self.assertGreaterEqual(len(entries), 14)
        logged = set()
        for entry in entries:
            self.assertTrue(entry["date_utc"])
            self.assertTrue(entry["access_outcome"])
            logged.update(x.strip() for x in entry["included_ids"].split(";") if x.strip())
        for item in rows:
            self.assertIn(item["source_id"], logged)

    def test_full_text_distinct_from_abstract(self):
        rows = read_rows(MATRIX)
        self.assertTrue(any(x["access_grade"] == "F-PDF" for x in rows))
        self.assertTrue(any(x["access_grade"] == "F-HTML" for x in rows))
        self.assertTrue(any(x["access_grade"] == "T" for x in rows))
        self.assertTrue(any(x["access_grade"] == "A" for x in rows))
        for entry in rows:
            if entry["access_grade"] == "A":
                self.assertNotIn("full original pdf inspected", entry["actual_evidence_reviewed"].lower())


if __name__ == "__main__":
    unittest.main()
