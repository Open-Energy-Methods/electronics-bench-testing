import unittest
from research_models.run import evaluate

class FailureModes(unittest.TestCase):
    @staticmethod
    def forced_error(result,model):
        return next(x["package_transient_rmse_C"] for x in result["holdout"]
                    if x["run"]=="HO-FAN-5W" and x["model"]==model)

    def test_independent_boundary_is_useful_only_if_valid(self):
        ideal=evaluate(mode="ideal")
        mismatch=evaluate(mode="mismatched")
        self.assertLess(self.forced_error(ideal,"B3"),self.forced_error(ideal,"B2"))
        self.assertGreater(self.forced_error(mismatch,"B3"),self.forced_error(mismatch,"B2"))

    def test_unmodelled_bypass_invalidates_boundary_parameter(self):
        bypass=evaluate(mode="bypass")
        self.assertGreater(abs(bypass["qualification"]["NAT"]["mean_k_w"]-2.8),.25)
        self.assertGreater(bypass["fitted"]["B3"]["jacobian_log_condition_number"],100.)

if __name__=="__main__":
    unittest.main()
