"""Run the finite mathematical and channel-level reproducibility checks."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy

from finite_model import (
    FlatModel, make_kernel, optimize, hypergeometric_model,
    fixed_shift_certificate, complete_allocation, primal_value,
)
from verify_protocol import run_protocol_checks


OPTIMIZATION_GAP_TOLERANCE = 1e-7


def _contains(report, exact_value):
    if not report["lower_squared"] <= exact_value <= report["upper_squared"]:
        raise AssertionError((report, exact_value))


def finite_checks():
    examples = [
        (FlatModel.from_weights("zero_exchange_with_zero_weight_columns", [0, 1, 2, 3],
                                [0, 1, 2, 0], [2, 3, 5, 1]), 7, 0, Fraction(1, 7)),
        (FlatModel.from_weights("two_sector_asymmetric", [0, 1], [8, 2], [1, 3]),
         2, 1, Fraction(92, 175)),
        (FlatModel.from_weights("three_sector_asymmetric", [0, 1, 2], [6, 3, 1], [1, 3, 8]),
         2, 1, None),
        (FlatModel.from_weights("sparse_charge_support", [0, 2, 3], [2, 3, 5], [1, 4, 2]),
         2, 1, None),
    ]
    reports = []
    for model, target_rank, budget, exact in examples:
        result = optimize(make_kernel(model, target_rank, budget), OPTIMIZATION_GAP_TOLERANCE)
        result["charges"] = list(model.charges)
        result["source_weights_exact"] = [str(p) for p in model.probabilities]
        result["source_ranks"] = list(model.ranks)
        result["model_spec"] = {
            "kind": "flat", "name": model.name, "charges": list(model.charges),
            "weights": [str(p) for p in model.probabilities], "ranks": list(model.ranks),
        }
        if exact is not None:
            _contains(result, float(exact))
            result["independent_exact_squared_fidelity"] = str(exact)
        reports.append(result)

    # An impossible destination contributes zero. Completing that allocation
    # at zero shift must not reduce the objective, including an entire column.
    kernel = make_kernel(examples[2][0], 2, 1)
    allocation = np.zeros_like(kernel.squared)
    allocation[kernel.zero_index] = 1
    allocation[kernel.zero_index, -1] = 0
    allocation[-1, -1] = 1
    before = primal_value(kernel, allocation)
    after_allocation = complete_allocation(kernel, allocation)
    after = primal_value(kernel, after_allocation)
    if after + 1e-14 < before or not np.allclose(after_allocation.sum(axis=0), 1):
        raise AssertionError("Zero-overlap completion failed")

    rejected = False
    try:
        hypergeometric_model(12, 4, 2)
    except ValueError as error:
        rejected = "does not fit Bob" in str(error)
    if not rejected:
        raise AssertionError("An unphysical full mean-marginal purification was accepted")

    return {
        "optimized_examples": reports,
        "zero_overlap_completion": {"before_squared": before, "after_squared": after},
        "unphysical_full_flat_reference_rejected": rejected,
    }


def fixed_exchange_checks():
    reports = []
    final_by_rank = {}
    for length in [128, 512, 8192]:
        model = hypergeometric_model(length, length // 4, length // 4)
        for rank in [2, 3, 4]:
            result = fixed_shift_certificate(make_kernel(model, rank, 1), -1)
            result["length"] = length
            result["model_spec"] = {
                "kind": "hypergeometric", "length": length, "alice_sites": length // 4,
                "total_charge": length // 4, "tail_probability_cutoff": "1e-19",
            }
            result["asymptotic_squared_fidelity"] = min(1, 3 / rank)
            reports.append(result)
            if length == 8192:
                final_by_rank[rank] = result
    # These are stated finite witnesses, not a substitute for proving a limit.
    if final_by_rank[2]["full_model_lower_squared"] <= 0.999:
        raise AssertionError("The below-threshold Bell-pair witness is unexpectedly weak")
    if final_by_rank[3]["full_model_lower_squared"] <= 0.98:
        raise AssertionError("The equality-boundary qutrit witness is unexpectedly weak")
    if not (0.749 < final_by_rank[4]["full_model_lower_squared"]
            <= final_by_rank[4]["full_model_upper_squared"] < 0.751):
        raise AssertionError("The rank-four interval does not resolve the predicted ceiling")
    return reports


def growing_exchange_checks():
    reports = []
    for length, budget in [(128, 3), (512, 6), (2048, 12)]:
        model = hypergeometric_model(length, length // 4, length // 4)
        rank = int(math.exp(0.65 * budget * math.log(3)))
        result = optimize(make_kernel(model, rank, budget), OPTIMIZATION_GAP_TOLERANCE)
        result["length"] = length
        result["alice_sites"] = length // 4
        result["total_charge"] = length // 4
        result["model_spec"] = {
            "kind": "hypergeometric", "length": length, "alice_sites": length // 4,
            "total_charge": length // 4, "tail_probability_cutoff": "1e-19",
        }
        result["target_selection"] = "floor(exp(0.65*S*ln(3)))"
        variance = (length // 4) * (3 * length // 4) * 0.25 * 0.75 / (length - 1)
        scaled_log_rank = math.log(rank) / (math.log(3) * math.sqrt(variance))
        result["unrestricted_gaussian_asymptotic_squared_reference"] = math.exp(-scaled_log_rank**2 / 4)
        result["gaussian_reference_is_finite_bound"] = False
        reports.append(result)
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the complete JSON record to this path")
    args = parser.parse_args()
    protocol = run_protocol_checks()
    finite = finite_checks()
    fixed = fixed_exchange_checks()
    growing = growing_exchange_checks()
    reports = finite["optimized_examples"] + growing
    maximum_gap = max(r["primal_dual_gap"] for r in reports)
    matrix_residual = max(protocol[name]["maximum_residual"]
                          for name in ["hybrid_component", "filtered_catalyst"])
    record = {
        "status": "PASS",
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__, "cvxpy_required": False},
        "optimization_gap_tolerance": OPTIMIZATION_GAP_TOLERANCE,
        "maximum_optimized_primal_dual_gap": maximum_gap,
        "maximum_matrix_residual": matrix_residual,
        "protocol_checks": protocol,
        "finite_checks": finite,
        "fixed_exchange_finite_witnesses": fixed,
        "growing_exchange_certificates": growing,
        "scope": "Finite channel checks and interval certificates; asymptotic claims require analytical proofs.",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    print("PASS: charge modes, trace preservation, coherent conversion, and filtered catalytic fidelity")
    print(f"PASS: exact finite primal-dual certificates; largest gap {maximum_gap:.3e}")
    print("PASS: physical-support rejection and zero-overlap completion")
    print("PASS: fixed-budget finite witnesses, including equality, and growing-budget certificates")
    print(f"Maximum direct-matrix residual: {matrix_residual:.3e}")
    if args.output:
        print(f"Complete record: {args.output}")


if __name__ == "__main__":
    main()
