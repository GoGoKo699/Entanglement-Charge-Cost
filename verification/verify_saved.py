"""Recheck archived primal/dual witnesses without rerunning an optimizer."""

import argparse
import json
from pathlib import Path

import numpy as np

from finite_model import FlatModel, hypergeometric_model, make_kernel, certify


def check_record(record):
    reports = (record["finite_checks"]["optimized_examples"]
               + record["fixed_exchange_finite_witnesses"]
               + record["growing_exchange_certificates"])
    maximum_difference = 0.0
    for report in reports:
        spec = report["model_spec"]
        if spec["kind"] == "flat":
            model = FlatModel.from_weights(spec["name"], spec["charges"], spec["weights"], spec["ranks"])
        elif spec["kind"] == "hypergeometric":
            model = hypergeometric_model(spec["length"], spec["alice_sites"], spec["total_charge"],
                                         float(spec["tail_probability_cutoff"]))
        else:
            raise ValueError(f"Unknown model kind: {spec['kind']}")
        kernel = make_kernel(model, report["target_rank"], report["charge_budget"])
        witness = report["witness"]
        checked = certify(kernel, np.array(witness["filter"]),
                          np.array(witness["dual_coordinates"]), repair_dual=False)
        for key in ["lower_squared", "upper_squared", "max_dual_constraint_upper",
                    "full_model_lower_squared", "full_model_upper_squared"]:
            difference = abs(checked[key] - report[key])
            maximum_difference = max(maximum_difference, difference)
            if difference > 2e-14:
                raise AssertionError((report["name"], key, checked[key], report[key]))
    return len(reports), maximum_difference


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    count, difference = check_record(json.loads(args.record.read_text()))
    print(f"PASS: {count} archived exact-model witnesses, without optimization")
    print(f"Maximum endpoint/constraint difference: {difference:.3e}")
