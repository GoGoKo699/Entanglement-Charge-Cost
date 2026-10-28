"""Direct Kraus-matrix checks, independent of the finite optimization solver."""

from __future__ import annotations

import math
import numpy as np


MATRIX_TOLERANCE = 3e-12


def _phi(indices, dimension):
    vector = np.zeros(dimension * dimension, dtype=complex)
    vector[np.asarray(indices) * dimension + np.asarray(indices)] = 1 / math.sqrt(len(indices))
    return vector


def _offsets(dimensions):
    return np.cumsum([0] + list(dimensions[:-1])).tolist()


def _local_pair(a, b, outcome, common_outcomes, active_output, block_output):
    """An Alice Kraus matrix and a complete Bob isometry for one sector."""
    output_dimension = len(block_output)
    lookup = {index: j for j, index in enumerate(block_output)}
    active = [lookup[index] for index in active_output]
    alice = np.zeros((output_dimension, a), complex)
    bob = np.zeros((output_dimension, a), complex)
    if a >= b:
        selected = [(outcome + ell) % a for ell in range(b)]
        remaining = [j for j in range(a) if j not in selected]
        spare = [j for j in range(output_dimension) if j not in active]
        if len(spare) < len(remaining):
            raise AssertionError("Neutral workspace does not fit Bob's isometry")
        for ell, source in enumerate(selected):
            alice[active[ell], source] = math.sqrt(a / (common_outcomes * b))
            bob[active[ell], source] = 1
        for dest, source in zip(spare, remaining):
            bob[dest, source] = 1
    else:
        for ell in range(a):
            alice[active[ell], ell] = 1 / math.sqrt(common_outcomes)
            bob[active[ell], ell] = 1
    return alice, bob


def _evaluate_channel(source, target, pairs, expected_branches, q_in, q_out, shifts):
    d_in, d_out = len(q_in), len(q_out)
    alice_tp = np.zeros((d_in, d_in), complex)
    global_tp = np.zeros((d_in**2, d_in**2), complex)
    rho = np.zeros((d_out**2, d_out**2), complex)
    errors = {"bob_isometry": 0.0, "branch_state": 0.0,
              "alice_charge_mode": 0.0, "bob_charge_mode": 0.0}
    branch_probabilities = []
    total_charge = 12
    for (alice, bob), expected, shift in zip(pairs, expected_branches, shifts):
        alice_tp += alice.conj().T @ alice
        errors["bob_isometry"] = max(errors["bob_isometry"], float(np.linalg.norm(
            bob.conj().T @ bob - np.eye(d_in))))
        errors["alice_charge_mode"] = max(errors["alice_charge_mode"], float(np.linalg.norm(
            q_out[:, None] * alice - alice * q_in[None, :] - shift * alice)))
        qb_in, qb_out = total_charge - q_in, total_charge - q_out
        errors["bob_charge_mode"] = max(errors["bob_charge_mode"], float(np.linalg.norm(
            qb_out[:, None] * bob - bob * qb_in[None, :] + shift * bob)))
        operator = np.kron(alice, bob)
        global_tp += operator.conj().T @ operator
        output = operator @ source
        branch_probabilities.append(float(np.vdot(output, output).real))
        errors["branch_state"] = max(errors["branch_state"], float(np.linalg.norm(output - expected)))
        rho += np.outer(output, output.conj())
    expected_rho = sum((np.outer(v, v.conj()) for v in expected_branches), np.zeros_like(rho))
    errors["alice_trace_preservation"] = float(np.linalg.norm(alice_tp - np.eye(d_in)))
    errors["global_trace_preservation"] = float(np.linalg.norm(global_tp - np.eye(d_in**2)))
    errors["full_output_state"] = float(np.linalg.norm(rho - expected_rho))
    errors["output_trace"] = abs(float(np.trace(rho).real) - 1)
    if max(errors.values()) > MATRIX_TOLERANCE:
        raise AssertionError(errors)
    return {
        "residuals": errors,
        "maximum_residual": max(errors.values()),
        "squared_fidelity": float(np.vdot(target, rho @ target).real),
        "output_purity": float(np.trace(rho @ rho).real),
        "branch_probabilities": branch_probabilities,
    }


def hybrid_component_check():
    """Both rank signs, one fixed shift, a literal neutral rank-two target."""
    a, catalyst_target_ranks = [3, 5], [1, 4]
    neutral_target_rank, workspace_dimension = 2, 2
    b = [neutral_target_rank * d for d in catalyst_target_ranks]
    probabilities = np.array([0.37, 0.63])
    source_charges, destination_charges = [4, 6], [3, 5]
    output_dimensions = [rank * workspace_dimension for rank in b]
    input_offsets, output_offsets = _offsets(a), _offsets(output_dimensions)
    d_in, d_out, outcomes = sum(a), sum(output_dimensions), math.lcm(*a)
    source = sum(math.sqrt(p) * _phi(range(offset, offset + rank), d_in)
                 for p, offset, rank in zip(probabilities, input_offsets, a))
    target = sum(math.sqrt(p) * _phi([offset + ell * workspace_dimension for ell in range(rank)], d_out)
                 for p, offset, rank in zip(probabilities, output_offsets, b))
    expected = sum(math.sqrt(probabilities[j]) * _phi(
        [output_offsets[j] + ell * workspace_dimension for ell in range(min(a[j], b[j]))], d_out)
        for j in range(len(a)))
    pairs = []
    for r in range(outcomes):
        alice = np.zeros((d_out, d_in), complex)
        bob = np.zeros((d_out, d_in), complex)
        for j in range(len(a)):
            oi, oo = input_offsets[j], output_offsets[j]
            active = [oo + ell * workspace_dimension for ell in range(b[j])]
            block = list(range(oo, oo + output_dimensions[j]))
            ac, bc = _local_pair(a[j], b[j], r, outcomes, active, block)
            alice[np.ix_(block, range(oi, oi + a[j]))] = ac
            bob[np.ix_(block, range(oi, oi + a[j]))] = bc
        pairs.append((alice, bob))
    q_in = np.repeat(source_charges, a)
    q_out = np.repeat(destination_charges, output_dimensions)
    report = _evaluate_channel(source, target, pairs, [expected / math.sqrt(outcomes)] * outcomes,
                               q_in, q_out, [-1] * outcomes)
    predicted = sum(probabilities[j] * math.sqrt(min(1, a[j] / b[j])) for j in range(len(a))) ** 2
    if abs(report["squared_fidelity"] - predicted) > MATRIX_TOLERANCE:
        raise AssertionError("Hybrid rank-overlap identity failed")
    if abs(report["output_purity"] - 1) > MATRIX_TOLERANCE:
        raise AssertionError("Uniform outcomes lost intersector coherence")
    report.update({
        "input_ranks": a, "target_sector_ranks_including_neutral_target": b,
        "neutral_target_rank": neutral_target_rank, "neutral_workspace_dimension": workspace_dimension,
        "common_outcomes": outcomes, "predicted_squared_fidelity": predicted,
        "model": "coherent two-sector conversion component, with both rank signs",
    })
    return report


def filtered_catalyst_check():
    """A catalytic channel complete on populated input support, with three shifts."""
    charges, ranks, probabilities = [2, 3], [1, 3], np.array([0.35, 0.65])
    physical_charges, physical_ranks = [1, 2, 3, 4], [1, 1, 3, 1]
    m, workspace = 2, 2
    shifts = [-1, 0, 1]
    allocation = np.array([[0, 0.55], [0.70, 0.45], [0.30, 0]])
    input_offsets = _offsets(ranks)
    dimensions_out = [d * m * workspace for d in physical_ranks]
    output_offsets = _offsets(dimensions_out)
    by_physical_charge = {q: j for j, q in enumerate(physical_charges)}
    by_source_charge = {q: j for j, q in enumerate(charges)}
    d_in, d_out, outcomes = sum(ranks), sum(dimensions_out), math.lcm(*ranks)
    source = sum(math.sqrt(p) * _phi(range(oi, oi + d), d_in)
                 for p, oi, d in zip(probabilities, input_offsets, ranks))
    target = np.zeros(d_out**2, complex)
    for q, d, p in zip(charges, ranks, probabilities):
        oo = output_offsets[by_physical_charge[q]]
        target += math.sqrt(p) * _phi([oo + ell * workspace for ell in range(m * d)], d_out)

    pairs, branch_vectors, branch_shifts = [], [], []
    predicted = 0.0
    for k_index, k in enumerate(shifts):
        coherent_output = np.zeros(d_out**2, complex)
        target_amplitude = 0.0
        for j, (q, a) in enumerate(zip(charges, ranks)):
            destination = by_physical_charge[q + k]
            target_j = by_source_charge.get(q + k)
            b = m * ranks[target_j] if target_j is not None else 1
            oo = output_offsets[destination]
            coherent_output += math.sqrt(probabilities[j] * allocation[k_index, j]) * _phi(
                [oo + ell * workspace for ell in range(min(a, b))], d_out)
            if target_j is not None:
                target_amplitude += math.sqrt(probabilities[j] * probabilities[target_j] *
                                              allocation[k_index, j] * min(1, a / b))
        predicted += target_amplitude**2
        for r in range(outcomes):
            alice = np.zeros((d_out, d_in), complex)
            bob = np.zeros((d_out, d_in), complex)
            for j, (q, a) in enumerate(zip(charges, ranks)):
                destination = by_physical_charge[q + k]
                target_j = by_source_charge.get(q + k)
                b = m * ranks[target_j] if target_j is not None else 1
                oi, oo = input_offsets[j], output_offsets[destination]
                block = list(range(oo, oo + dimensions_out[destination]))
                active = [oo + ell * workspace for ell in range(b)]
                ac, bc = _local_pair(a, b, r, outcomes, active, block)
                alice[np.ix_(block, range(oi, oi + a))] = math.sqrt(allocation[k_index, j]) * ac
                bob[np.ix_(block, range(oi, oi + a))] = bc
            pairs.append((alice, bob))
            branch_vectors.append(coherent_output / math.sqrt(outcomes))
            branch_shifts.append(k)
    report = _evaluate_channel(source, target, pairs, branch_vectors,
                               np.repeat(charges, ranks),
                               np.repeat(physical_charges, dimensions_out), branch_shifts)
    if abs(report["squared_fidelity"] - predicted) > MATRIX_TOLERANCE:
        raise AssertionError("Filtered-channel fidelity does not equal the primal objective")
    report.update({
        "source_charges": charges, "source_ranks": ranks,
        "physical_output_charges": physical_charges,
        "neutral_target_rank": m, "neutral_workspace_dimension": workspace,
        "shifts": shifts, "filter": allocation.tolist(),
        "common_outcomes_per_shift": outcomes,
        "predicted_squared_fidelity": predicted,
        "model": "filtered catalytic channel complete on populated input support, including zero-weight destinations",
        "full_unpopulated_input_extension": "proved in science/coherent_protocol.md, not matrix-enumerated here",
    })
    return report


def run_protocol_checks():
    return {"matrix_tolerance": MATRIX_TOLERANCE,
            "hybrid_component": hybrid_component_check(),
            "filtered_catalyst": filtered_catalyst_check()}


if __name__ == "__main__":
    import json
    print(json.dumps(run_protocol_checks(), indent=2))
