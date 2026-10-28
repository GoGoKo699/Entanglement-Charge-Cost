# From Watrous to entanglement borrowing with a charge budget

Alice and Bob share an entangled state and want an additional entangled pair while returning the shared state almost unchanged. A mathematical conversion may use local operations that change particle number. This project asks how much net charge exchange those operations require, and whether they can preserve the coherence of the returned state.

The single educational anchor is **John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), Cambridge University Press, 2018**. Section and theorem numbers below refer to the author's linked 2018 standard-layout draft, identified in its front matter as a pre-publication manuscript. The [author's contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) identify the sections; the chapter links give direct access to the source. The book supplies the quantum-information foundations. The charge-constrained model and the steps developed below are supplied by this repository and its attributed research dependencies.

Use this bridge alongside the [30-milestone map](MILESTONES.md). The map specifies the understanding targets; this page explains how the textbook tools enter the scientific argument. The exact assumptions and claims remain in [the model](../science/model.md), with complete proofs in the linked science pages.

## 1. A focused route through the anchor

There is no need to read the entire book before entering the project. The following sections can be consulted when their objects first appear.

| Watrous source | Foundation to use | Where it enters this project |
|---|---|---|
| [§1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Singular values, Schmidt decompositions, and operator norms | Rank inside a charge sector and the rank-overlap bound |
| [§§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density operators, reduced states, and purification | The joint catalyst–target reference and physical flat-sector comparison |
| [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Channels, Kraus representations, and dilations | Complete instruments, charge-resolved leaves, and buffer implementations |
| [§§3.2.1–3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Fidelity, purification overlap, and channel monotonicity | Unconditional scoring and transfer from a comparison state to a Haar state |
| [§4.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) and [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Majorization and pure-state entanglement conversion | Deterministic rank reduction within a sector |
| [§6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Local operations and classical communication | Product Kraus operators at complete adaptive leaves |
| [§§7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Uniform random vectors and invariant averages | Haar moments on the fixed-total-charge subspace |
| [§§1.2.1 and 1.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Convexity and primal–dual reasoning | The project-specific finite optimization and certificates |

The finite program here is derived in [finite optimization](../science/finite_optimization.md). It is not one of the book's semidefinite programs. Likewise, the textbook's general LOCC model does not impose this project's charge modes, hard support budget, or catalyst-return criterion.

## 2. Notation and the return criterion

Watrous often writes a pure vector as $`u`$, its density operator as $`uu^*`$, and an adjoint as $`A^*`$. This repository uses $`|\psi\rangle`$, $`|\psi\rangle\langle\psi|`$, and $`A^\dagger`$. The objects are the same. A textbook Schmidt coefficient $`s_j`$ corresponds to $`\sqrt{\lambda_j}`$ when $`\lambda_j`$ denotes an eigenvalue of a reduced density operator. Squaring the coefficient is essential when forming probabilities.

We usually call a channel $`\Lambda`$ to leave $`|\Phi_m\rangle`$ for the neutral maximally entangled target:

```math
|\Phi_m\rangle=\frac{1}{\sqrt m}\sum_{j=1}^{m}|j\rangle_{A'}|j\rangle_{B'}.
```

The target registers initially contain a product state. Their local charges are trivial, or equivalently fixed to the same value before and after the operation. Adding target entanglement therefore increases the required Schmidt rank without changing the retained catalyst's charge labels.

Watrous's Definition 3.11 uses the same **root fidelity** as this project:

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1.
```

Our objective is its square, and our error measure for normalized states is

```math
P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}.
```

This definition of $`P`$ is stated here for the project; it should not be inferred from a convention in a different source. Accuracy compares the complete retained output with

```math
|\tau\rangle=|\psi\rangle_{AB}\otimes|\Phi_m\rangle_{A'B'}.
```

Thus a good catalyst marginal alone is insufficient. Correlations between the returned catalyst and an imperfect target can lower the joint fidelity.

The pure-reference formula in Watrous's Proposition 3.13 gives a useful operational identity. If $`M_r`$ are the complete Kraus leaves, including all environment labels, then

```math
\rho_{\rm out}=\sum_r M_r|\psi\rangle\langle\psi|M_r^\dagger,
\qquad
F(\rho_{\rm out},\tau)^2
=\sum_r|\langle\tau|M_r|\psi\rangle|^2.
```

The initial product target is absorbed into the maps. A branch contributes its unnormalized amplitude, so its probability is already counted. For example, a protocol that produces the exact target with probability $`r`$ and a state orthogonal to it otherwise has $`F^2=r`$ and $`P^2=1-r`$. Keeping only the successful runs would change the problem.

## 3. Charge sectors refine the Schmidt description

For occupation qubits, each occupied site contributes one unit of charge. Fix the total number $`N`$. Alice's local charge $`q`$ then determines Bob's local charge $`N-q`$. A physically valid flat-sector catalyst has the form

```math
|\Omega\rangle
=\sum_{q\in\mathcal Q}\sqrt{p_q}\,|\Phi_{d_q};q,N-q\rangle,
\qquad
|\Phi_{d_q};q,N-q\rangle
=\frac{1}{\sqrt{d_q}}\sum_{i=1}^{d_q}|q,i\rangle_A|N-q,i\rangle_B.
```

Here $`p_q>0`$ is a probability distribution and $`d_q`$ must fit both physical charge sectors. Inside the charge-$`q`$ block, Alice's reduced-state eigenvalue is $`p_q/d_q`$, repeated $`d_q`$ times. The global vector is coherent across $`q`$, although Alice's reduced density operator is block diagonal. Measuring and forgetting $`q`$ would replace that vector by a different, dephased state.

In the ideal returned catalyst and target, the sector with Alice charge $`q'`$ has Schmidt rank $`m d_{q'}`$. A branch that shifts the catalyst charge from $`q`$ to $`q+k`$ must therefore turn an input rank $`d_q`$ into a vector close to rank $`m d_{q+k}`$. This is the point where the textbook's Schmidt analysis becomes a charge-cost calculation.

The notation $`d_q`$ is used for an arbitrary finite flat-sector model. In the typical-state application it becomes $`a_q=\binom{L_A}{q}`$ on a window where Bob has enough dimensions. The symbols $`p_q`$ remain charge probabilities, not individual Schmidt eigenvalues.

## 4. From channels to charge-respecting implementations

The Kraus and dilation descriptions in Watrous §2.2.2 allow the output record and discarded systems to be retained explicitly. The additional physical condition here is local charge conservation with initially charge-incoherent, unentangled ancillas. Resolving their initial and final charge labels gives definite-mode local operators:

```math
Q_A^{\rm out}A_r-A_rQ_A^{\rm in}=k_{A,r}A_r,
\qquad
Q_B^{\rm out}B_r-B_rQ_B^{\rm in}=k_{B,r}B_r.
```

At every complete LOCC leaf the bipartite operator is $`A_r\otimes B_r`$. The hard budget requires $`|k_{A,r}|\le S`$ for every such leaf. It constrains net charge change after the complete branch. An expectation value of the shift, or a bound on a single intermediate step, would not specify this resource.

Because the desired catalyst still has total charge $`N`$ and the target is neutral, a leaf can overlap it only when $`k_{B,r}=-k_{A,r}`$. Other leaves have zero target overlap but remain in the trace-preserving output.

A definite-mode instrument can be implemented with a charge eigenstate buffer. If $`M_j`$ has mode $`k_j`$ and $`\sum_jM_j^\dagger M_j=I`$, the local isometry

```math
W|\varphi\rangle|E\rangle_R
=\sum_j M_j|\varphi\rangle\,|E-k_j\rangle_R\,|j\rangle_C
```

conserves the sum of system and buffer charges. The record $`C`$ is neutral. Within a fixed shift, its buffer output depends on $`k_j`$, not on the unknown coherent sector label $`q`$. The initially definite charge supplies no coherent phase reference. Appropriate finite neutral workspace completes the isometry to a physical unitary dilation.

The buffer changes and need not be returned. Alice and Bob exchange classical records; particles are absorbed or supplied locally. The scientific cost is the supported absolute net shift, so these constructions do not establish a universal minimum buffer capacity or a circuit-complexity bound. The [model](../science/model.md#allowed-operations-and-the-hard-budget) states the complete implementation class.

## 5. Rank conversion must preserve sector coherence

Watrous's Theorem 6.33 relates deterministic pure-state LOCC conversion to majorization. For uniform Schmidt spectra, a rank-$`a`$ maximally entangled vector can be converted to rank $`b\le a`$. When $`a<b`$, a local embedding instead reaches root overlap $`\sqrt{a/b}`$ with the larger maximally entangled target. Together, the attainable factor is

```math
c_{q,k}=\sqrt{\min\left\{1,\frac{d_q}{m d_{q+k}}\right\}}.
```

An independent conversion in each sector is not yet a coherent conversion of their superposition. Its announced outcome could reveal the sector. The construction must synchronize those probabilities.

Consider a rank-four input and rank-two output as a conversion component. Alice uses four operators

```math
K_j=\frac{1}{\sqrt2}
\left(|0\rangle\langle j|+|1\rangle\langle j+1\pmod4|\right),
\qquad j=0,1,2,3.
```

Every input basis vector occurs twice, so $`\sum_jK_j^\dagger K_j=I_4`$. After Alice announces $`j`$, Bob relabels the two selected coordinates. The unnormalized output is $`|\Phi_2\rangle/2`$, and each outcome has probability $`1/4`$.

A different sector with input rank six would naturally have six outcomes with probabilities $`1/6`$. To combine the two sectors coherently, refine both alphabets to twelve outcomes: split each rank-four outcome into three equal suboutcomes and each rank-six outcome into two. The announced label is now uniform with probability $`1/12`$ in both sectors. Bob's correction makes the corrected vector independent of that label. Discarding it therefore preserves the relative sector amplitudes.

For arbitrary finitely many sectors, choose a common multiple $`R`$ of the relevant ranks. Rank-deficit sectors use their fixed embeddings divided by $`\sqrt R`$. The same argument gives the hybrid factor $`c_{q,k}`$ without omitting deficient sectors. Bob's correction is defined on the occupied subspace and completed by a separate charge-preserving channel on its complement; a unitary extension on the catalyst alone is not assumed.

For a fixed shift, the resulting unconditional root-fidelity contribution is

```math
\sum_q\sqrt{p_qp_{q+k}}\,c_{q,k},
```

with only physically valid destinations retained in that construction. The square roots multiply because one amplitude comes from the source sector and another from the corresponding sector of the desired returned state. The established sector-synchronization methods are credited to Schuch, Verstraete, and Cirac in [the complete construction](../science/coherent_protocol.md). The charge accounting and joint overlap must remain explicit when those methods are applied here.

## 6. Why adaptation and failure branches cannot beat the bound

The construction is only one protocol. Optimality requires a statement about every allowed protocol, including arbitrary filtering and classical adaptation.

Let $`t_{r,q}`$ be the probability of complete leaf $`r`$ on the normalized input block $`q`$. Trace preservation says $`\sum_rt_{r,q}=1`$. A product Kraus map cannot increase the Schmidt rank of that input block. If a vector has squared norm $`t`$ and rank at most $`d`$, its overlap with a rank-$`D`$ maximally entangled vector is at most

```math
\sqrt t\,\sqrt{\min\{1,d/D\}}.
```

One way to see this is to write the vector as a coefficient matrix. Its overlap is a normalized trace; the trace norm is bounded by the square root of the rank times the Hilbert–Schmidt norm. The ordinary norm bound supplies the cap at one.

Set

```math
A_{kq}=\sqrt{p_qp_{q+k}}\,c_{q,k}.
```

These $`A_{kq}`$ are scalar overlap coefficients, distinct from the local Kraus operators $`A_r`$. A leaf with opposite shifts $`(k,-k)`$ satisfies

```math
|\langle\tau|M_r|\Omega\rangle|
\le\sum_q A_{kq}\sqrt{t_{r,q}}.
```

The crucial step is to sum the squared branch amplitudes using $`\sum_rt_{r,q}=1`$. Bounding each branch separately by a constant and multiplying by the number of branches would lose the result. In [the converse](../science/converse.md), Cauchy–Schwarz and the complete-output isometry perform the sum without an outcome-count factor. An input tail of probability $`\eta`$ adds at most $`\sqrt\eta`$ to root fidelity in that argument. Its effect is controlled before squaring.

At zero exchange, $`c_{q,0}=1/\sqrt m`$ in every occupied flat block. The upper bound is attained by leaving the catalyst alone and appending a product target. Consequently $`F_\star^2=1/m`$ exactly for every physically valid finite flat-sector catalyst. This is a statement about borrowing with joint return; the catalyst may contain much ordinary entanglement.

## 7. The finite optimization and a complete small example

Group the branch probabilities by their charge shift. The resulting variables $`T_{kq}`$ are nonnegative and satisfy $`\sum_kT_{kq}=1`$. For a finite flat-sector catalyst, the optimum is exactly

```math
F_\star^2
=\max_{T\ge0,\ \sum_kT_{kq}=1}
\sum_{k=-S}^{S}
\left(\sum_q A_{kq}\sqrt{T_{kq}}\right)^2.
```

For attainment, Alice first applies the charge-diagonal filter $`C_k=\bigoplus_q\sqrt{T_{kq}}I_{d_q}`$ and announces $`k`$. The common-outcome construction then converts each selected sector. The first filter may reveal information about $`q`$; its effect is already included in the displayed objective. Synchronizing the subsequent refinement prevents additional leakage.

For the converse, group all overlap-bearing leaves and assign any residual column mass to $`k=0`$. This increases the nonnegative objective and accounts for leaves with the wrong total charge. Missing target sectors have $`A_{kq}=0`$; assigning their mass to zero shift cannot hurt, so an optimizer never needs a physically nonexistent destination.

A complementary upper certificate is

```math
F_\star^2
=\min_{x_q>0}\left\{\sum_qx_q:
\sum_q\frac{A_{kq}^2}{x_q}\le1\quad\text{for every }k\right\}.
```

For any feasible $`x`$, weighted Cauchy–Schwarz bounds the primal objective by $`\sum_qx_q`$. The full duality proof also establishes attainment. In particular, the zero-shift coefficient $`A_{0q}=p_q/\sqrt m>0`$ keeps every dual coordinate away from zero. A solver's convergence flag is therefore replaceable by explicit feasible lower and upper witnesses.

### Two populated sectors

Take $`q=0,1`$, $`p=(4/5,1/5)`$, $`d=(1,3)`$, a neutral Bell target $`m=2`$, and $`S=1`$. The sector ranks are assumed physically available, as required by the finite model. In row order $`k=-1,0,+1`$ and column order $`q=0,1`$, the squared overlap coefficients are

```math
(A_{kq}^2)=
\begin{pmatrix}
0&4/25\\
8/25&1/50\\
2/75&0
\end{pmatrix}.
```

Choose the filter

```math
T=
\begin{pmatrix}
0&33/49\\
1&16/49\\
0&0
\end{pmatrix}.
```

Each column sums to one. The shift $`-1`$ branch converts source rank three to target-sector rank two. The zero-shift branch embeds each source into the larger rank required by the Bell target. Their squared-fidelity contributions are

```math
\left(\frac25\sqrt{\frac{33}{49}}\right)^2
=\frac{132}{1225},
\qquad
\left(\sqrt{\frac8{25}}+
\sqrt{\frac1{50}}\sqrt{\frac{16}{49}}\right)^2
=\frac{512}{1225}.
```

The complete output therefore attains $`F^2=92/175`$. No branch is conditioned away. The dual choice $`x=(64/175,28/175)`$ has sum $`92/175`$. Its three constraints evaluate to $`1,1,7/96`$, so the attained value is optimal. This is the analytical example reproduced in [verification](../verification/README.md#representative-output).

The example connects the operational and optimization descriptions: a column of $`T`$ specifies a physical instrument on that source sector; coherent conversion determines its overlap; the dual rules out every more elaborate admissible protocol. Numerical optimization is useful for finding witnesses, while feasibility and their matching values establish the conclusion.

## 8. From random physical states to flat sectors

The ensemble uses a Haar-uniform vector in the fixed-total-charge-$`N`$ subspace, with $`N=\nu L`$. It is not a Haar vector on the entire $`2^L`$-dimensional space. The dimensions are

```math
a_q=\binom{L_A}{q},\qquad
b_q=\binom{L_B}{N-q},\qquad
D=\binom{L}{N},\qquad
p_q=\frac{a_qb_q}{D}.
```

The last expression is a hypergeometric charge distribution: it counts configurations with Alice charge $`q`$ and divides by the total number of configurations. Watrous §7.2 supplies the invariant-measure framework. The fixed-charge contraction of its second moment is worked out in [typical states](../science/typical_states.md).

For a fixed Alice fraction $`0<f=L_A/L<1/2`$, Bob's sector dimension exceeds Alice's exponentially near the mean charge. A central window can therefore support a maximally entangled rank-$`a_q`$ vector on both sides. Extreme sectors need not satisfy $`a_q\le b_q`$; the construction discards an exponentially small tail and normalizes the retained weights before defining the physical comparison state.

The moment estimate controls the unnormalized reduced block:

```math
\mathbb E\left\|\rho_{A,q}-\frac{b_q}{D}I_{a_q}\right\|_1
\le p_q\sqrt{\frac{a_q}{b_q}}.
```

It includes charge-weight fluctuations as well as the spectrum inside each block. Summing this estimate on the central window and controlling the tail makes the actual reduced state close to the flat comparison marginal.

Purification overlap is the bridge from that marginal estimate back to a physical bipartite vector. Here it must be realized **sector by sector**: use the actual Schmidt bases within each charge sector and flatten their coefficients. These basis changes commute with local charge. An arbitrary global purification-alignment unitary could mix Bob's charge sectors and would not supply the required allowed operation.

If the resulting comparison state is $`|\Omega_L\rangle`$ and $`\zeta_L=P(\psi_L,\Omega_L)`$, channel continuity controls both occurrences of the catalyst, as input and as the desired returned state:

```math
\left|F_L^\star(m,S;\psi_L)-F_L^\star(m,S;\Omega_L)\right|
\le2\zeta_L.
```

The bound is uniform in $`m`$ and $`S`$. This is why the flat-sector operational results can transfer even when the target dimension grows. The parties may tailor their protocol to the known state; the argument does not construct one decoder for unknown Haar samples.

## 9. Rank slope, distribution overlap, and the two scales

Near $`q=\nu L_A`$, adjacent binomial ranks obey

```math
\frac{a_q}{a_{q-1}}=\frac{L_A-q+1}{q}
\longrightarrow\frac{1-\nu}{\nu}=e^\mu,
\qquad \mu=\ln\frac{1-\nu}{\nu}.
```

For $`\nu<1/2`$, a favorable shift is $`k=-s`$: Alice returns a sector of smaller rank, freeing approximately $`e^{\mu s}`$ source dimensions per returned catalyst dimension. For $`\nu>1/2`$, the favorable direction reverses. The relevant coefficient is $`|\mu|`$.

At fixed $`m`$ and $`S`$, the rank factor becomes constant across the typical region, while a fixed translation of the broad charge distribution has overlap tending to one. The construction and converse then meet at

```math
F_L^\star(m,S;\psi_L)^2
\longrightarrow\min\left\{1,\frac{e^{|\mu|S}}{m}\right\}
```

in probability over the Haar catalyst. Keeping rank-deficit sectors is what permits the equality case $`m=e^{|\mu|S}`$; their small finite-size deficits vanish without a strict asymptotic rank surplus. At quarter filling, one unit of exchange has limiting squared fidelity $`\min\{1,3/m\}`$. A Bell target and a qutrit target approach fidelity one, while a rank-four target approaches squared fidelity $`3/4`$.

When the shift is comparable to the charge width, the returned distribution becomes distinguishably displaced. Its variance is

```math
\sigma_L^2=\frac{L_A L_B}{L-1}\nu(1-\nu),
```

and the translated-distribution root overlap has the Gaussian form

```math
\sum_q\sqrt{p_qp_{q-s}}
=\exp\left(-\frac{s^2}{8\sigma_L^2}\right)+o(1).
```

Squaring this expression and imposing $`F^2\ge1-\epsilon^2`$ produces the scale $`2\sigma_L\sqrt{-\ln(1-\epsilon^2)}`$. The logarithmic rank gain converts an allowed shift into target size through $`\log_2m\simeq|\mu|s/\ln2`$.

The precise leading law, for fixed $`0<\epsilon<1`$ and $`S_L/\sqrt L\to\alpha\in[0,\infty]`$, is

```math
B_{\epsilon,L}(S_L)
=\frac{|\mu|}{\ln2}
\min\left\{S_L,2\sigma_L\sqrt{-\ln(1-\epsilon^2)}\right\}
+o_{\mathbb P}(\sqrt L).
```

Here $`o_{\mathbb P}(\sqrt L)`$ means that the remainder divided by $`\sqrt L`$ tends to zero in probability. The unrestricted Gaussian cap is the established result of [Zhang, Liu, and Chen](../references/RELATED_WORK.md); it does not follow from computing one shifted protocol's overlap alone. The complete argument combines that cap, the hard-budget converse, and a charge-respecting construction with subleading rank slack. It gives no exact constant-order crossover when $`S_L=\Theta(\sqrt L)`$. For diverging $`S_L=o(\sqrt L)`$, the stronger project result identifies $`|\mu|/\ln2`$ as the asymptotic ebits per unit of supported net exchange. See [the asymptotic proof](../science/asymptotics.md) for the distinct limits.

## 10. Reading the conclusion at its proved scope

Three quantities now have separate roles. Sector-rank variation supplies the target's Schmidt dimensions. Charge-distribution overlap controls the catalyst's return. A synchronized charge-respecting instrument makes the conversion physically admissible without revealing the coherent sector label in its refinement record.

The result concerns a known catalyst, a neutral target, and unrestricted local computation with initially unentangled, charge-incoherent ancillas. Charge buffers are changed resources. The theorem does not cover half filling, an equal bipartition, a requirement to restore the buffers, an average-only exchange budget, or efficient circuit synthesis. Broad charge fluctuations in a dynamical state would also need suitable block spectra before the equilibrium Haar result could be applied.

Watrous supplies one coherent foundation for the state, channel, fidelity, entanglement, and probability tools. The symmetry machinery and unrestricted borrowing law retain their primary research attribution in [related work](../references/RELATED_WORK.md). The new constrained argument is documented in the project's canonical proofs. Neither the educational route nor finite numerical checks replace those proof obligations.

For a compact conceptual route, return to the [milestone map](MILESTONES.md). For specialist reading, follow [the model](../science/model.md), [coherent extraction](../science/coherent_protocol.md), [the converse](../science/converse.md), and [finite optimization](../science/finite_optimization.md), then use [typical states](../science/typical_states.md) and [asymptotics](../science/asymptotics.md) to reach the Haar results. [Verification](../verification/README.md) provides executable channel checks and finite certificates, with their scope stated explicitly.
