# What the charge cost measures

The results identify the charge exchange needed to access the known borrowing resource of typical fixed-charge states. Three ingredients have separate roles: the local rank slope fixes how much target entanglement a shift can supply, the charge distribution fixes how well the catalyst returns after that shift, and the allowed instruments determine whether the conversion can preserve coherence.

## Rank gained per exchanged particle

At filling $`\nu`$, the number of Alice states in a sector is $`a_q=\binom{L_A}{q}`$. Near its typical charge, a shift $`k`$ changes its logarithm by

```math
\ln a_q-\ln a_{q+k}=-\mu k+\text{subleading terms},
\qquad \mu=\ln\frac{1-\nu}{\nu}.
```

For $`\nu<1/2`$, moving Alice's catalyst from $`q`$ to $`q-s`$ reduces the rank that must be returned. Approximately $`e^{\mu s}`$ source dimensions become available per returned catalyst dimension. They can supply a neutral maximally entangled target of dimension $`m\lesssim e^{\mu s}`$. Particle-hole conjugation reverses the favorable direction when $`\nu>1/2`$.

This argument suggests the charge cost, but it is not by itself a protocol or a converse. The [construction](coherent_protocol.md) prevents the classical measurement record from revealing the sector. The [converse](converse.md) sums the rank restriction over every complete outcome without multiplying the error by the number of outcomes. Both steps are necessary because the catalyst is coherent across charge sectors.

## Why zero exchange remains restrictive

A flat block of rank $`d_q`$ cannot become a maximally entangled vector of rank $`m d_q`$ by LOCC. Its maximal squared overlap is $`1/m`$. At zero shift this factor is the same in every sector, and no adaptive combination of outcomes improves it. The [exact finite result](finite_optimization.md) is therefore

```math
[F^\star(m,0)]^2=1/m.
```

Appending a product target attains the bound. For example, the overlap of $`|00\rangle`$ with a Bell pair is $`1/\sqrt2`$, so the optimal squared fidelity is $`1/2`$. This example also explains why a loose error convention may assign a nonzero numerical capacity even at zero exchange. A target with $`m>1`$ cannot have error tending to zero in this regime.

The catalyst can still contain extensive ordinary entanglement. The obstruction concerns borrowing additional entanglement while returning the joint catalyst-target state close to its specified product reference. Consuming the catalyst would define a different task.

## Return error from translating the charge distribution

The typical subsystem charge has width $`\sigma_L=\Theta(\sqrt L)`$. The overlap of its hypergeometric law with a shift by $`s`$ is asymptotically

```math
\sum_q\sqrt{p_qp_{q-s}}
=\exp\!\left(-\frac{s^2}{8\sigma_L^2}\right)+o(1).
```

When $`s=o(\sqrt L)`$, the charge distribution returns with vanishing error. For $`s`$ comparable to $`\sqrt L`$, the displacement becomes visible at finite error. Combining the rank supplied by a shift with this return condition gives

```math
\ln m\le |\mu|\min\left\{S,
2\sigma_L\sqrt{-\ln(1-\epsilon^2)}\right\}
+o(\sqrt L).
```

The [asymptotic theorem](asymptotics.md) makes this reasoning precise. The fluctuation-limited term is inherited from the unrestricted optimum of [Zhang, Liu and Chen](../references/RELATED_WORK.md); the constrained construction reaches it once enough exchange is allowed. No additional leading loss arises from imposing charge-respecting instruments in this model.

At the boundary $`\ln m=|\mu|S+O(1)`$ with $`S=\Theta(\sqrt L)`$, individual rank ratios retain order-one variation across the charge distribution. The leading capacity law does not specify the resulting constant-order crossover. For fixed $`S`$, those variations vanish, which is why the fixed-budget theorem can include the equality case exactly in the limit.

## A fixed-budget example

At quarter filling, $`|\mu|=\ln3`$. For a fixed target dimension and $`S=1`$, the limiting squared fidelity is $`\min\{1,3/m\}`$:

| Target | No exchange, $`S=0`$ | One unit, $`S=1`$ |
|---|---:|---:|
| Bell pair, $`m=2`$ | $`1/2`$ | $`1`$ |
| Maximally entangled qutrit pair, $`m=3`$ | $`1/3`$ | $`1`$ |
| Two Bell pairs, $`m=4`$ | $`1/4`$ | $`3/4`$ |

The entries are large-system limits for typical Haar catalysts, with exact values for the flat zero-exchange case. They do not promise these fidelities at a chosen small system size. The finite optimizer and explicit matrix implementation are documented in [verification](../verification/README.md).

## Resource accounting

| Resource or condition | Status in the model |
|---|---|
| Shared catalyst | One known pure state at fixed total charge; returned jointly close to itself and the target. |
| Extra shared entanglement | None supplied. |
| Coherent phase reference | None supplied in the local ancillas. |
| Local charge buffers | Initially definite charge in the construction; final charge may change and need not be restored. |
| Charged communication | None between laboratories; local buffers absorb opposite catalyst changes. |
| Exchange budget | Maximum absolute net catalyst charge shift in every complete resolved outcome. |
| Neutral target and work space | Target size is the output; local neutral ancillas and computation are otherwise unrestricted. |
| Classical communication | Allowed; all measurement outcomes are counted. |
| Catalyst description and compilation | Available in principle; no efficient learning or gate synthesis theorem. |

Returning the buffers would add a new catalytic requirement. Counting peak charge storage, total traffic, charge variance, or only the expected shift would also change the constrained problem. The existing theorem should not be relabeled as one of those costs.

## Relation to other embezzling systems

Number-conserving entanglement embezzlement already occurs in other families, including Gaussian fermionic constructions. The contribution here is the optimal hard exchange requirement for the typical fixed-charge ensemble and the precise neutral-target task. The [related-work account](../references/RELATED_WORK.md) separates the established symmetry machinery, the unrestricted Gaussian capacity, and the constrained result.

For a dynamical state, a broad charge distribution alone does not imply the required borrowing capacity. Its charge-block Schmidt spectra must also satisfy suitable approximation conditions. A future application to a diffusive circuit would have to establish those conditions and control the joint return error; the equilibrium Haar theorem does not supply that dynamical proof.

Return to [the exact model and results](model.md), or inspect the [finite optimality certificates](finite_optimization.md).
