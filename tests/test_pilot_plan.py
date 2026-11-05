"""Check Q0 plan completeness, determinism, and explicit non-authorization."""
import unittest
from collections import Counter

from scripts.make_pilot_plan import generate_plan, ASSEMBLY, COOLING, POWER, FIELDS


class PilotPlanTests(unittest.TestCase):
    def test_full_factorial_in_each_independent_assembly_block(self):
        plan = generate_plan()
        self.assertEqual(len(plan), 12)
        self.assertEqual(len({p["run_id"] for p in plan}), 12)
        for assembly in ASSEMBLY:
            pairs = {(p["cooling"], p["power_label"])
                     for p in plan if p["assembly_id"] == assembly}
            self.assertEqual(pairs, {(c, w) for c in COOLING for w in POWER})

    def test_reproducible_order_and_multiple_block_counts(self):
        self.assertEqual(generate_plan(), generate_plan())
        self.assertNotEqual(generate_plan(seed=1), generate_plan(seed=2))
        self.assertEqual(Counter(x["assembly_id"] for x in generate_plan()),
                         {assembly: 4 for assembly in ASSEMBLY})

    def test_explicit_unauthorized_planning_rows(self):
        rows = generate_plan()
        self.assertTrue(all(set(x) == set(FIELDS) for x in rows))
        self.assertTrue(all(x["planned_status"] == "NOT_AUTHORIZED" for x in rows))
        self.assertTrue(all("power_W" not in x and "voltage_V" not in x for x in rows))
        self.assertEqual([int(x["sequence"]) for x in rows], list(range(1, 13)))


if __name__ == "__main__":
    unittest.main()
