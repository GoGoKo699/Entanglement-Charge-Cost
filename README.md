# Entanglement Charge Cost

**How much conserved charge must local operations exchange to borrow entanglement from a typical many-body state?** This project determines the optimal hard net exchange budget for typical fixed-particle-number pure states across an unequal bipartition.

Alice and Bob know the catalyst state and use charge-respecting local instruments, classical communication, and initially charge-incoherent local buffers. They borrow a neutral maximally entangled target while returning the **entire catalyst and target** close to their desired product state. Every outcome counts. The budget $`S`$ bounds the absolute net change of Alice's catalyst charge in each complete charge-resolved outcome; the constructions obey the same bound for Bob.

## Principal results

Take a fixed filling $`0<\nu<1`$, $`\nu\ne1/2`$, and an Alice fraction $`0<f<1/2`$. Put $`\mu=\ln[(1-\nu)/\nu]`$. For every fixed target dimension $`m`$ and integer budget $`S`$, the optimal squared fidelity of a typical fixed-charge Haar catalyst satisfies

```math
[F_L^\star(m,S)]^2
\longrightarrow
\min\left\{1,\frac{e^{|\mu|S}}{m}\right\}.
```

Convergence is in probability as the number of sites $`L`$ grows. The equality case $`m=e^{|\mu|S}`$ is included. At quarter filling, one unit of exchange permits a Bell pair or a maximally entangled qutrit pair with error tending to zero. With zero exchange, the limiting squared fidelity is only $`1/m`$.

For a fixed purified-error tolerance $`0<\epsilon<1`$ and $`S_L/\sqrt L\to\alpha\in[0,\infty]`$, the borrowable entanglement in ebits is

```math
B_{\epsilon,L}(S_L)
=\frac{|\mu|}{\ln2}
\min\left\{S_L,
2\sigma_L\sqrt{-\ln(1-\epsilon^2)}\right\}
+o(\sqrt L),
\qquad
\sigma_L^2=\frac{L_A(L-L_A)}{L-1}\nu(1-\nu).
```

This capacity convergence is also in probability over the Haar catalyst. The fluctuation-limited term is the **established unrestricted Gaussian borrowing law** of [Zhang, Liu and Chen](references/RELATED_WORK.md#zlc26). The exchange term and the charge-respecting attaining protocol identify the additional operational cost. General charge-respecting conversion methods and the existence of number-conserving embezzlement are also prior results, as detailed in [related work](references/RELATED_WORK.md).

| Regime | What is established |
|---|---|
| Exactly flat charge blocks, $`S=0`$ | Exact finite-size identity $`[F^\star(m,0)]^2=1/m`$. |
| Fixed $`S`$ and $`m`$ | The limiting fidelity above, including its threshold equality. |
| Diverging $`S=o(\sqrt L)`$ | Leading yield $`B_{\epsilon,L}(S)/S\to \lvert\mu\rvert/\ln2`$. |
| $`S`$ on the fluctuation scale | The minimum of the exchange-limited yield and the known unrestricted capacity. |
| General finite flat-block catalyst | Exact fidelity optimization and matching primal/dual certificates. |

## Read the science

Start with [the model and exact claims](science/model.md). The scientific account then follows two routes: the finite operational problem, and its application to typical many-body states.

| Question | Authoritative account |
|---|---|
| What is charged, returned, supplied, and optimized? | [Model](science/model.md) |
| How can the ideal flat comparison fit into a physical Haar catalyst? | [Typical states and charge-preserving alignment](science/typical_states.md) |
| How is sector coherence preserved during extraction? | [Coherent protocol](science/coherent_protocol.md) |
| Why can no adaptive protocol exceed the charge restriction? | [Complete-outcome converse](science/converse.md) |
| How is the finite optimum computed and certified? | [Finite optimization](science/finite_optimization.md) |
| How do the charge and fluctuation limits meet? | [Uniform asymptotics](science/asymptotics.md) |
| What does the result mean physically? | [Interpretation and resource accounting](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| What do the finite calculations verify? | [Reproducibility](verification/README.md) |

[The LLM reading guide](llms.txt) maps reader questions to these authoritative pages.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks compare a direct finite Kraus implementation with its predicted coherent output, certify finite fidelity values using feasible protocols and dual bounds, and evaluate representative finite-size asymptotic examples. The [verification guide](verification/README.md) gives the dependencies, commands, numerical tolerances, and actual expected outputs. These calculations test the implementation and finite consequences; the complete-outcome converse and the limiting laws are proved in the scientific pages.

## Scope

The catalyst is known, the target is locally neutral, and arbitrary local computation is allowed. Buffers can finish with changed definite charge; they are not returned catalysts. The budget is a bound on every complete net charge shift, not on its mean, total intermediate traffic, circuit complexity, or preparation cost. Half filling, equal cuts, efficient state learning, and unconditional dynamical growth are outside the proved claims.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
