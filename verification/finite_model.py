"""Finite flat-sector fidelity, feasible filters, and outward-rounded bounds.

The optimizer uses floating point. Its reported lower and upper certificates are
reevaluated for the exact rational model with directed decimal rounding.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
import math
from typing import Sequence

import numpy as np
from scipy.optimize import minimize


DECIMAL_PRECISION = 70
DUAL_SAFETY = 2e-11
ZERO_SHIFT_MIX = 1e-16


@dataclass(frozen=True)
class FlatModel:
    name: str
    charges: tuple[int, ...]
    probabilities: tuple[Fraction, ...]
    ranks: tuple[int, ...]
    discarded_mass: Fraction = Fraction(0)

    @classmethod
    def from_weights(
        cls, name: str, charges: Sequence[int], weights: Sequence,
        ranks: Sequence[int], discarded_mass: Fraction = Fraction(0),
    ) -> "FlatModel":
        if not (len(charges) == len(weights) == len(ranks)):
            raise ValueError("Charges, weights, and ranks must have equal length")
        if len(set(charges)) != len(charges):
            raise ValueError("Charge labels must be distinct")
        rows = []
        for q, w, d in zip(charges, weights, ranks):
            w = Fraction(str(w)) if isinstance(w, float) else Fraction(w)
            if w < 0 or int(d) != d or d < 1:
                raise ValueError("Weights must be nonnegative and ranks positive integers")
            if w:
                rows.append((int(q), w, int(d)))
        if not rows:
            raise ValueError("At least one source weight must be positive")
        rows.sort()
        total = sum((row[1] for row in rows), Fraction(0))
        return cls(
            name, tuple(row[0] for row in rows),
            tuple(row[1] / total for row in rows),
            tuple(row[2] for row in rows), Fraction(discarded_mass),
        )

    @property
    def p(self) -> np.ndarray:
        return np.array([float(p) for p in self.probabilities])


def hypergeometric_model(
    length: int, alice_sites: int, total_charge: int,
    tail_probability_cutoff: float = 1e-19,
) -> FlatModel:
    """A physically valid flat purification with an exactly charged tail.

    No hidden Bob padding is used. Every full-support Alice rank is explicitly
    checked against Bob's physical charge-sector dimension. The discarded mass
    is evaluated by exact integer binomial sums, not by a Gaussian estimate.
    """
    if not 0 < alice_sites < length or not 0 <= total_charge <= length:
        raise ValueError("Invalid spin-system dimensions or charge")
    bob_sites = length - alice_sites
    denominator = math.comb(length, total_charge)
    cutoff = Fraction(str(tail_probability_cutoff))
    lo, hi = max(0, total_charge - bob_sites), min(alice_sites, total_charge)
    kept = []
    total_weight = 0
    for q in range(lo, hi + 1):
        a = math.comb(alice_sites, q)
        b = math.comb(bob_sites, total_charge - q)
        weight = a * b
        total_weight += weight
        if b < a:
            raise ValueError(
                "The full mean block does not fit Bob's physical sector; "
                "this routine requires a physical full flat purification"
            )
        if weight * cutoff.denominator >= denominator * cutoff.numerator:
            kept.append((q, weight, a))
    if total_weight != denominator:
        raise AssertionError("Vandermonde normalization failed")
    if not kept:
        raise ValueError("Tail cutoff removed the whole state")
    kept_weight = sum(row[1] for row in kept)
    return FlatModel.from_weights(
        f"hypergeometric_L{length}_A{alice_sites}_N{total_charge}",
        [row[0] for row in kept], [row[1] for row in kept],
        [row[2] for row in kept],
        Fraction(denominator - kept_weight, denominator),
    )


@dataclass
class Kernel:
    model: FlatModel
    target_rank: int
    budget: int
    shifts: np.ndarray
    exact_squared: list[list[Fraction]]
    squared: np.ndarray
    amplitudes: np.ndarray

    @property
    def zero_index(self) -> int:
        return self.budget


def make_kernel(model: FlatModel, target_rank: int, budget: int) -> Kernel:
    if int(target_rank) != target_rank or target_rank < 1:
        raise ValueError("The target rank must be a positive integer")
    if int(budget) != budget or budget < 0:
        raise ValueError("The budget must be a nonnegative integer")
    target_rank, budget = int(target_rank), int(budget)
    by_charge = {q: j for j, q in enumerate(model.charges)}
    shifts = np.arange(-budget, budget + 1, dtype=int)
    rows = []
    for k in shifts:
        row = []
        for j, q in enumerate(model.charges):
            dest = by_charge.get(q + int(k))
            if dest is None:
                row.append(Fraction(0))
            else:
                rank_factor = min(
                    Fraction(1),
                    Fraction(model.ranks[j], target_rank * model.ranks[dest]),
                )
                row.append(model.probabilities[j] * model.probabilities[dest] * rank_factor)
        rows.append(row)
    squared = np.array([[float(a) for a in row] for row in rows])
    if np.any(squared[budget] <= 0):
        raise ValueError("Numerical underflow in a source column; restrict and charge its tail")
    return Kernel(model, target_rank, budget, shifts, rows, squared, np.sqrt(squared))


def primal_value(kernel: Kernel, allocation: np.ndarray) -> float:
    return float(np.sum(np.sum(kernel.amplitudes * np.sqrt(allocation), axis=1) ** 2))


def complete_allocation(kernel: Kernel, allocation: np.ndarray) -> np.ndarray:
    """Remove zero-overlap allocations and restore each column at zero shift."""
    allocation = np.maximum(np.asarray(allocation, dtype=float), 0).copy()
    allocation[kernel.squared == 0] = 0
    sums = allocation.sum(axis=0)
    if np.any(sums > 1 + 1e-10):
        raise ValueError("Allocation exceeds unit mass in a source column")
    allocation[kernel.zero_index] += np.maximum(0, 1 - sums)
    allocation /= allocation.sum(axis=0)
    return allocation


def _from_simplex(kernel: Kernel, lambdas: np.ndarray):
    z_squared = lambdas @ kernel.squared
    if np.any(z_squared <= 0):
        raise ValueError("A positive zero-shift mixture is required at this boundary")
    z = np.sqrt(z_squared)
    allocation = lambdas[:, None] * kernel.squared / z_squared[None, :]
    allocation /= allocation.sum(axis=0)
    derivatives = np.sum(kernel.squared / z[None, :], axis=1)
    x = float(np.max(derivatives)) * z
    return allocation, x, z, derivatives


def _fraction_decimal(value: Fraction, rounding: str) -> Decimal:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        context.rounding = rounding
        return Decimal(value.numerator) / Decimal(value.denominator)


def _float_outward(value: Decimal, upper: bool) -> float:
    result = float(value)
    represented = Decimal.from_float(result)
    if (upper and represented < value) or (not upper and represented > value):
        result = math.nextafter(result, math.inf if upper else -math.inf)
    return result


def _sqrt_outward(value: Decimal, upper: bool) -> Decimal:
    if not value:
        return Decimal(0)
    # Decimal.sqrt is correctly rounded to nearest. One adjacent decimal value
    # in the requested direction therefore provides an outward enclosure.
    root = value.sqrt()
    return root.next_plus() if upper else root.next_minus()


def certify(kernel: Kernel, allocation: np.ndarray, x: np.ndarray, repair_dual: bool = True) -> dict:
    """Certify one exact rational filter and one outward-checked dual point.

    Float filter entries are interpreted as exact binary rationals and each
    column is normalized exactly. Float dual coordinates are also interpreted
    exactly; directed rounding only enlarges their constraint left sides.
    """
    nrows, ncols = kernel.squared.shape
    rational_t = [[Fraction(0) for _ in range(ncols)] for _ in range(nrows)]
    for q in range(ncols):
        column = [Fraction.from_float(float(max(0, allocation[k, q]))) for k in range(nrows)]
        for k in range(nrows):
            if not kernel.exact_squared[k][q]:
                column[k] = Fraction(0)
        mass = sum(column, Fraction(0))
        if not mass:
            column[kernel.zero_index] = Fraction(1)
            mass = Fraction(1)
        for k in range(nrows):
            rational_t[k][q] = column[k] / mass

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        context.rounding = ROUND_FLOOR
        lower = Decimal(0)
        for k in range(nrows):
            amplitude = Decimal(0)
            for q in range(ncols):
                radicand = kernel.exact_squared[k][q] * rational_t[k][q]
                value = _fraction_decimal(radicand, ROUND_FLOOR)
                amplitude += _sqrt_outward(value, upper=False)
            lower += amplitude * amplitude

    x = np.asarray(x, dtype=float).copy()
    if np.any(~np.isfinite(x)) or np.any(x <= 0):
        raise ValueError("Dual coordinates must be positive and finite")
    if repair_dual:
        x *= 1 + DUAL_SAFETY
    max_constraint = Decimal("Infinity")
    for _ in range(3 if repair_dual else 1):
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            context.rounding = ROUND_CEILING
            max_constraint = Decimal(0)
            for row in kernel.exact_squared:
                value = Decimal(0)
                for aq2, xq in zip(row, x):
                    value += _fraction_decimal(aq2, ROUND_CEILING) / Decimal.from_float(float(xq))
                max_constraint = max(max_constraint, value)
            if max_constraint <= 1:
                upper = sum((Decimal.from_float(float(xq)) for xq in x), Decimal(0))
                break
        if repair_dual:
            x *= _float_outward(max_constraint, upper=True) * (1 + DUAL_SAFETY)
    else:
        raise AssertionError("Could not produce an outward-verified dual certificate")

    upper = min(Decimal(1), upper)
    if lower > upper:
        raise AssertionError("Primal certificate exceeds dual certificate")

    # The input and ideal returned catalyst both change under truncation.
    # Contractivity and fidelity continuity give |F_full-F_kept| <= 2 sqrt(eta).
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        context.rounding = ROUND_CEILING
        eta_upper = _fraction_decimal(kernel.model.discarded_mass, ROUND_CEILING)
        root_tail_upper = _sqrt_outward(eta_upper, upper=True)
        twice_tail_upper = 2 * root_tail_upper
        root_upper = min(Decimal(1), _sqrt_outward(upper, upper=True) + twice_tail_upper)
        full_upper = root_upper * root_upper
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        context.rounding = ROUND_FLOOR
        root_lower = max(Decimal(0), _sqrt_outward(lower, upper=False) - twice_tail_upper)
        full_lower = root_lower * root_lower

    lo, hi = _float_outward(lower, False), _float_outward(upper, True)
    return {
        "lower_squared": lo,
        "upper_squared": hi,
        "primal_dual_gap": hi - lo,
        "max_dual_constraint_upper": _float_outward(max_constraint, True),
        "exact_filter_columns_normalized": True,
        "decimal_precision": DECIMAL_PRECISION,
        "discarded_mass_upper": _float_outward(eta_upper, True),
        "full_model_lower_squared": _float_outward(full_lower, False),
        "full_model_upper_squared": _float_outward(full_upper, True),
        "witness": {
            "filter": np.asarray(allocation, dtype=float).tolist(),
            "dual_coordinates": x.tolist(),
        },
    }


def optimize(kernel: Kernel, requested_gap: float = 1e-7) -> dict:
    rows, _ = kernel.squared.shape
    zero = np.zeros(rows)
    zero[kernel.zero_index] = 1

    def mix(u):
        return (1 - ZERO_SHIFT_MIX) * u + ZERO_SHIFT_MIX * zero

    def objective(u):
        z = np.sqrt(mix(u) @ kernel.squared)
        value = -float(np.sum(z))
        gradient = -(1 - ZERO_SHIFT_MIX) * np.sum(kernel.squared / z[None, :], axis=1) / 2
        return value, gradient

    if rows == 1:
        lambdas = np.ones(1)
        solver = {"method": "analytic_single_shift", "success": True, "iterations": 0}
    else:
        result = minimize(
            objective, np.full(rows, 1 / rows), jac=True, method="SLSQP",
            bounds=[(0, 1)] * rows,
            constraints={"type": "eq", "fun": lambda u: np.sum(u) - 1,
                         "jac": lambda u: np.ones(rows)},
            options={"ftol": 2e-13, "maxiter": 1500, "disp": False},
        )
        u = np.maximum(result.x, 0)
        u /= u.sum()
        lambdas = mix(u)
        solver = {"method": "SLSQP_simplex", "success": bool(result.success),
                  "status": int(result.status), "message": str(result.message),
                  "iterations": int(result.nit)}

    allocation, x, z, derivatives = _from_simplex(kernel, lambdas)
    report = certify(kernel, allocation, x)
    # Tiny source-boundary weights can make the simplex objective insensitive
    # to a poorly determined inactive coordinate. A direct dual solve resolves
    # that issue without requiring the primal optimizer to resolve tiny gains.
    if report["primal_dual_gap"] > requested_gap:
        weights = kernel.model.p
        coefficients = kernel.squared / weights[None, :]

        def dual_constraint(y):
            return 1 - np.sum(coefficients / y[None, :], axis=1)

        def dual_jacobian(y):
            return coefficients / y[None, :] ** 2

        dual_result = minimize(
            lambda y: (float(np.dot(weights, y)), weights),
            x / weights, jac=True, method="SLSQP",
            bounds=[(1e-15, None)] * len(weights),
            constraints={"type": "ineq", "fun": dual_constraint, "jac": dual_jacobian},
            options={"ftol": 2e-13, "maxiter": 1500, "disp": False},
        )
        dual_x = weights * np.maximum(dual_result.x, 1e-15)
        alternate = certify(kernel, allocation, dual_x)
        solver["dual_fallback"] = {
            "method": "SLSQP_direct_convex_dual",
            "success": bool(dual_result.success),
            "status": int(dual_result.status),
            "iterations": int(dual_result.nit),
        }
        if alternate["upper_squared"] < report["upper_squared"]:
            report = alternate
            solver["dual_point"] = "direct_convex_dual"

    # A second, analytic feasible family provides an inexpensive cross-check.
    if report["primal_dual_gap"] > requested_gap:
        envelope = np.max(kernel.amplitudes, axis=0)
        alternate_x = envelope * float(np.sum(envelope))
        alternate = certify(kernel, allocation, alternate_x)
        if alternate["upper_squared"] < report["upper_squared"]:
            report = alternate
            solver["dual_point"] = "pointwise_amplitude_envelope"

    report.update({
        "name": kernel.model.name,
        "source_sectors": len(kernel.model.charges),
        "target_rank": kernel.target_rank,
        "charge_budget": kernel.budget,
        "shifts": kernel.shifts.tolist(),
        "shift_simplex": lambdas.tolist(),
        "simplex_root_objective": float(np.sum(z)),
        "reconstructed_primal_squared": primal_value(kernel, allocation),
        "max_filter_column_residual": float(np.max(np.abs(allocation.sum(axis=0) - 1))),
        "weighted_gradient_identity_residual": float(abs(np.dot(lambdas, derivatives) - np.sum(z))),
        "solver": solver,
    })
    if report["primal_dual_gap"] > requested_gap:
        raise AssertionError(f"Unresolved primal-dual gap: {report}")
    return report


def fixed_shift_certificate(kernel: Kernel, shift: int) -> dict:
    index = int(shift + kernel.budget)
    if not 0 <= index < len(kernel.shifts):
        raise ValueError("Shift is outside the budget")
    allocation = np.zeros_like(kernel.squared)
    allocation[index] = 1
    allocation = complete_allocation(kernel, allocation)
    envelope = np.max(kernel.amplitudes, axis=0)
    x = envelope * float(np.sum(envelope))
    report = certify(kernel, allocation, x)
    report.update({
        "name": kernel.model.name,
        "source_sectors": len(kernel.model.charges),
        "target_rank": kernel.target_rank,
        "charge_budget": kernel.budget,
        "shift": shift,
        "uncompleted_shift_lower_squared": float(np.sum(kernel.amplitudes[index]) ** 2),
    })
    return report
