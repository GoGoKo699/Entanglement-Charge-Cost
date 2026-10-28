# Reproducing the finite results

The analytical optimum and both dual formulations are proved in [finite_optimization.md](../science/finite_optimization.md). This directory checks their finite implementations, supplies explicit lower and upper certificates, and tests the coherent conversion directly as a quantum channel. The calculations do not establish an asymptotic limit or Haar concentration by themselves.

## Run

Use Python 3.10 or later, NumPy, and SciPy. CVXPY and external conic solvers are not required. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py --output verification/local_results.json
```

The committed [reference_results.json](reference_results.json) was generated with Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The expected terminal output has this form:

```text
PASS: charge modes, trace preservation, coherent conversion, and filtered catalytic fidelity
PASS: exact finite primal-dual certificates; largest gap 4.321e-08
PASS: physical-support rejection and zero-overlap completion
PASS: fixed-budget finite witnesses, including equality, and growing-budget certificates
Maximum direct-matrix residual: 1.506e-15
Complete record: verification/local_results.json
```

Solver iterations and the last digits can vary between supported numerical-library versions. Acceptance depends on the explicit certificates, not agreement with a stored decimal value or a solver's success flag.

The archived witnesses can also be checked without running an optimizer:

```bash
python verification/verify_saved.py verification/reference_results.json
```

The reference record contains 16 exact-model filter/dual witnesses. The replay reports `PASS` and zero endpoint discrepancy in the recorded environment. To inspect only the channel construction, run `python verification/verify_protocol.py`.

## What is checked

| Calculation | Mathematical issue checked |
|---|---|
| Explicit hybrid Kraus matrices | Rank reduction and rank-deficit embedding share uniform outcome probabilities and preserve intersector coherence. |
| Explicit filtered catalytic channel | A charge-diagonal filter followed by conditional conversion has the squared fidelity in the finite primal program. |
| Charge-mode and trace-preservation residuals | Both laboratories have the stated opposite charge modes, Bob's corrections are isometries, and the bipartite channel is trace preserving on the populated input support. |
| Zero-exchange example | The numerical interval contains the exact value $1/m$, including removal of zero-weight source columns. |
| Asymmetric and sparse-support examples | The optimizer handles unequal ranks and weights, both charge directions, missing destination sectors, and inactive shifts. |
| Independent two-sector solution | The interval contains $92/175$, obtained from explicit primal and dual analytical witnesses below. |
| Fixed $S=1$ at quarter filling | Finite intervals distinguish $m=2$, the equality case $m=3$, and the ceiling for $m=4$. |
| Growing budgets | Explicit finite lower and upper bounds are computed for increasing system size, target dimension, and supported charge exchange. |

The matrix calculations include a literal neutral target of rank two and a neutral workspace tensor factor. The component check uses source ranks $(3,5)$ and target sector ranks $(2,8)$, so both signs of the rank comparison occur. The filtered example uses three shifts and compares the full retained density matrix with the predicted mixture of coherent branches. Its zero-weight output sectors are included. The extension to unpopulated physical input sectors is proved in [coherent_protocol.md](../science/coherent_protocol.md); that larger input completion is not matrix-enumerated here.

The finite examples are physically valid direct sums of charge sectors. The hypergeometric examples use $L_A=N=L/4$. In that case

```math
\binom{3L/4}{L/4-q}\ge\binom{L/4}{L/4-q}
=\binom{L/4}{q},
```

so every Alice Schmidt rank fits Bob's original physical sector, including the tails. The constructor checks this property on the entire support and rejects an incompatible full mean-marginal purification. No undeclared neutral padding is used in these examples.

## Solver and certificate arithmetic

`finite_model.py` forms $A_{kq}^2$ exactly as rational numbers. The optimizer solves the concave simplex problem

```math
F^\star=\max_{\lambda\in\Delta}\sum_q
\sqrt{\sum_k\lambda_k A_{kq}^2}.
```

It reconstructs a feasible sector filter and a feasible dual point. A small zero-shift mixture keeps source columns positive during numerical optimization. If the resulting primal–dual interval remains too wide, a separate convex dual solve is attempted. Tiny boundary weights can make the simplex objective numerically insensitive while its raw dual multiplier remains inaccurate; this fallback resolves that observed failure mode.

The certificate evaluation then uses 70-digit `decimal` arithmetic with outward rounding:

1. Every saved filter entry is interpreted as an exact binary rational. Each source column is normalized exactly, so the lower bound belongs to an actual feasible filter.
2. The attained fidelity is evaluated downward. Each square root is enclosed by an adjacent decimal value, and subsequent positive sums and products are rounded downward.
3. Saved dual coordinates are interpreted exactly. Every constraint $\sum_q A_{kq}^2/x_q\le1$ is evaluated upward. A small initial inflation and, if necessary, a checked rescaling make the point feasible.
4. The dual objective is evaluated upward. The known upper bound one is also available.

Python documents the required correctly rounded operations and adjacent representable values in its [`decimal` reference](https://docs.python.org/3.12/library/decimal.html). The solver controls how narrow the interval becomes. The outward feasibility checks establish the validity of the reported endpoints for the exact rational finite model. The archived JSON includes the complete filter and dual coordinates; replay rechecks those witnesses without repairing their dual points.

The populated-support channel matrices use ordinary double precision, with a residual tolerance of $3\times10^{-12}$. Their largest recorded residual is approximately $1.51\times10^{-15}$. Optimized certificate intervals must have width at most $10^{-7}$ in squared fidelity; the largest recorded width is approximately $4.33\times10^{-8}$. These tolerances apply to different quantities and should not be conflated.

## Tail accounting

For the larger hypergeometric examples, source probabilities below $10^{-19}$ are omitted and the remaining state is normalized. The omitted weight $\eta$ is computed by exact binomial integer sums. Each report distinguishes the exact retained-model interval from the interval for the physical full flat state.

If $|\Psi_T\rangle$ is the normalized restriction, then $P(\Psi,\Psi_T)=\sqrt\eta$. Both the input catalyst and the ideal returned catalyst change, so fidelity continuity and channel contractivity give

```math
|F^\star(\Psi)-F^\star(\Psi_T)|\le2\sqrt\eta.
```

The code expands the interval at the root-fidelity level before squaring. Its report does not treat a numerically discarded tail as exactly absent from the physical full model.

## Representative output

For the independent two-sector example,

```math
p=(4/5,1/5),\quad d=(1,3),\quad m=2,\quad S=1,
```

the optimum is $F^2=92/175$. An exact shift-simplex witness is

```math
(\lambda_{-1},\lambda_0,\lambda_{+1})=(33/161,128/161,0).
```

It gives $z=(32,14)/\sqrt{4025}$. The dual point $x=(64/175,28/175)$ saturates the $k=-1,0$ constraints; the $k=+1$ constraint is $7/96$. Thus this value is independently checkable without an optimization package.

At quarter filling with $L=8192$ and $S=1$, the full-model squared-fidelity intervals are:

| Target rank | Certified interval, rounded outward for display | Analytical limiting value |
|---:|---:|---:|
| $2$ | $[0.9991323301,\ 0.9991323349]$ | $1$ |
| $3$ | $[0.9817524725,\ 0.9817524772]$ | $1$ |
| $4$ | $[0.7495933071,\ 0.7495933112]$ | $3/4$ |

These are finite witnesses. In particular, the equality case has a visible finite-size correction despite its limiting fidelity being one.

The growing-budget calculation chooses $m=\lfloor\exp(0.65S\ln3)\rfloor$:

| $L$ | $S$ | $m$ | Full-model squared-fidelity interval, rounded outward |
|---:|---:|---:|---:|
| $128$ | $3$ | $8$ | $[0.6537424325,\ 0.6537424776]$ |
| $512$ | $6$ | $72$ | $[0.6886772047,\ 0.6886772061]$ |
| $2048$ | $12$ | $5266$ | $[0.7453965019,\ 0.7453965052]$ |

The record also includes the unrestricted Gaussian asymptotic expression for orientation, explicitly labeled as an asymptotic reference rather than a finite upper bound.

## Files

- [finite_model.py](finite_model.py): exact rational kernels, simplex and dual optimization, feasible-filter reconstruction, directed-rounding certificates, and physical hypergeometric support checks.
- [verify_protocol.py](verify_protocol.py): direct Kraus matrices and coherent-output checks.
- [run_all.py](run_all.py): reproducible collection of the finite checks and certificates.
- [verify_saved.py](verify_saved.py): independent replay of the saved numerical witnesses without optimization.
- [reference_results.json](reference_results.json): full recorded results and witnesses.

For the analytical statements that these calculations support, see [finite optimization](../science/finite_optimization.md), [the coherent protocol](../science/coherent_protocol.md), [the converse](../science/converse.md), and [the asymptotic limits](../science/asymptotics.md).
