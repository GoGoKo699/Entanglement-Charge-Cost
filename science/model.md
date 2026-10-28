# Entanglement borrowing with a charge budget

Entanglement embezzlement asks whether local operations can extract an entangled target while returning the shared resource state nearly unchanged. A state may have a favorable Schmidt spectrum even when the operations that exploit it exchange a conserved quantity with local reservoirs. This project determines that exchange requirement for typical pure states at fixed particle number.

The unrestricted Gaussian borrowing law for this ensemble is established by Zhang, Liu and Chen [ZLC26](../references/RELATED_WORK.md). The question here is how much of that resource remains accessible when each complete local outcome has a bounded charge shift. The proofs use established superselection-rule conversion methods, with the charge budget retained explicitly throughout the protocol.

## Physical systems and the return criterion

There are $L$ occupation qubits with total charge

```math
Q=\sum_{i=1}^{L}|1\rangle\langle1|_i.
```

Alice holds $L_A=fL$ qubits and Bob holds $L_B=L-L_A$. Take fixed $0<f<1/2$ and $0<\nu<1$ with $\nu\ne1/2$, along sequences for which $L_A$ and $N=\nu L$ are integers. The catalyst $|\psi_L\rangle$ is drawn uniformly from the total-charge-$N$ subspace. The state is known to the parties: their operations may depend on its full description.

The target registers start in a product state and have trivial local charge. The desired target is

```math
|\Phi_m\rangle=m^{-1/2}\sum_{j=1}^{m}|j\rangle_A|j\rangle_B,
\qquad m\in\mathbb N.
```

An encoding with the same definite local charge before and after the operation is equivalent. Targets with fluctuating local charge require a different accounting and are outside the statements below.

Use root fidelity $F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1$ and purified distance $P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}$. Accuracy compares the **entire catalyst and target** with the pure product reference:

```math
P\!\left(\rho_{\mathrm{out}},
 |\psi_L\rangle\langle\psi_L|\otimes
 |\Phi_m\rangle\langle\Phi_m|\right)\le\epsilon.
```

Thus catalyst disturbance, target error, residual correlations, and the probabilities of failure outcomes all enter the same criterion. Returned catalyst marginals alone would define a different task. Local work registers, classical records, and charge buffers are traced out at the end; their return is not required.

## Allowed operations and the hard budget

The parties use local operations and classical communication (LOCC). Each local instrument has a charge-conserving dilation with initially charge-incoherent, unentangled ancillary systems. No shared entanglement or coherent phase reference is supplied in those ancillas. Degenerate charge sectors may contain arbitrarily large neutral work spaces.

Resolve an implementation into complete Kraus leaves, including the initial classical ancilla labels and final environment charge labels. Each local leaf has a definite mode:

```math
Q_A^{\mathrm{out}}A_r-A_rQ_A^{\mathrm{in}}=k_{A,r}A_r,
\qquad
Q_B^{\mathrm{out}}B_r-B_rQ_B^{\mathrm{in}}=k_{B,r}B_r.
```

Here the charges on the retained systems are the catalyst charges, because the target is neutral. The **hard net exchange budget** is

```math
|k_{A,r}|\le S
\quad\text{for every complete charge-resolved leaf }r,
\qquad S\in\mathbb Z_{\ge0}.
```

Only leaves with $k_{B,r}=-k_{A,r}$ can overlap the target reference, whose catalyst has total charge $N$. Other leaves remain part of the output and contribute zero to the fidelity. All optima established here are unchanged if the same bound $|k_{B,r}|\le S$ is imposed on Bob as well: the upper bounds already hold with only Alice constrained, and the attaining constructions respect both bounds.

This is a restriction on implementations by locally covariant instruments, with the specified charge-resolved support. Merely requiring the average bipartite channel to be covariant does not specify this class. The budget bounds neither the expected charge change alone nor the sum of intermediate changes. It also imposes no gate-count, run-time, interaction-range, or state-description constraint. Suprema include limits of finite-round LOCC protocols.

For a favorable shift of size $s\le S$ at $\nu<1/2$, Alice's catalyst loses $s$ particles and Bob's gains $s$. Alice may start with an empty buffer of charge range $0,\ldots,S$; Bob starts with charge $S$ in a buffer of the same range. They end with charges $s$ and $S-s$, respectively. The protocol communicates classical outcomes, not particles between laboratories. A protocol using both signs can instead start each buffer at charge $S$ in a range $0,\ldots,2S$. These implementations demonstrate sufficient reservoirs; the theorem's resource is the maximum absolute net shift, not a universal statement about minimum reservoir size.

## Fidelity and capacity

Let $F_L^\star(m,S;\psi_L)$ be the supremum of root fidelity over these protocols. Define the borrowing capacity at fixed $0<\epsilon<1$ by

```math
B_{\epsilon,L}(S;\psi_L)=
\max\left\{\log_2m:
 [F_L^\star(m,S;\psi_L)]^2\ge1-\epsilon^2\right\}.
```

One ebit corresponds to a Bell pair. Restricting $m$ to powers of two changes the capacity by at most one ebit: a neutral maximally entangled target of larger dimension can be converted deterministically to any smaller one by LOCC.

The charge-sector dimensions and mean weights are

```math
a_q=\binom{L_A}{q},\qquad
b_q=\binom{L_B}{N-q},\qquad
D=\binom{L}{N},\qquad
p_q=\frac{a_qb_q}{D}.
```

The physical support is $\max(0,N-L_B)\le q\le\min(L_A,N)$. Set

```math
\mu=\ln\frac{1-\nu}{\nu},\qquad
\sigma_L^2=\operatorname{Var}(Q_A)
=\frac{L_A L_B}{L-1}\nu(1-\nu).
```

The coefficient $|\mu|$ is the local logarithmic slope of the sector rank. Moving one charge in the favorable direction makes approximately $e^{|\mu|}$ more source Schmidt dimensions available per returned catalyst dimension.

## Main results and their proof route

### Fixed exchange

For every fixed integer $S\ge0$ and $m\ge1$, with probability tending to one over the Haar catalyst,

```math
[F_L^\star(m,S;\psi_L)]^2
\longrightarrow
\min\left\{1,\frac{e^{|\mu|S}}{m}\right\}.
```

The equality boundary $m=e^{|\mu|S}$ is included. For an exactly flat charge-block catalyst, the zero-exchange identity $[F^\star(m,0)]^2=1/m$ holds already at finite size. The typical Haar statement converges to this identity; it is not an exact finite-size statement about individual Haar samples.

The [complete-outcome converse](converse.md) bounds every adaptive protocol by the available rank in each shifted charge sector. The [coherent construction](coherent_protocol.md) synchronizes the measurement outcome probabilities across sectors and attains the bound asymptotically, including sectors with a rank deficit. The [typical-state transfer](typical_states.md) supplies the physical Haar result.

At quarter filling, $e^{|\mu|}=3$. One unit of allowed exchange can therefore borrow a Bell pair, or a maximally entangled qutrit pair, with error tending to zero. With no exchange, their limiting squared fidelities are $1/2$ and $1/3$, respectively. A four-dimensional target with $S=1$ has limiting squared fidelity $3/4$.

### Fluctuation-scale exchange

For fixed $0<\epsilon<1$ and any integer sequence $S_L$ such that $S_L/\sqrt L\to\alpha\in[0,\infty]$, the capacity obeys, in probability,

```math
B_{\epsilon,L}(S_L;\psi_L)
=\frac{|\mu|}{\ln2}
\min\left\{S_L,
2\sigma_L\sqrt{-\ln(1-\epsilon^2)}\right\}
+o(\sqrt L).
```

The first term is the charge-budget restriction. The second is the unrestricted Gaussian borrowing limit from [ZLC26](../references/RELATED_WORK.md). A charge-respecting protocol reaches their minimum at leading order. At $S_L$ of order $\sqrt L$, the lower bound uses a subleading safety margin; this formula asserts no exact constant-order correction at the boundary. The [asymptotic proof](asymptotics.md) explains the order of limits and also treats diverging budgets below $\sqrt L$.

### Exact finite catalysts

For a finite physically valid coherent sum of flat charge blocks, the [finite optimization](finite_optimization.md) gives the exact optimal squared fidelity as a concave program, together with a convex dual certificate. This includes arbitrary charge weights and finite boundaries. It identifies the finite problem underlying both asymptotic laws; the Haar transfer is a separate approximation theorem.

## What the results establish

The ideal spectral resource and the operations needed to access it are different ingredients. Typical unequal-cut fixed-charge states contain a growing borrowing resource, but a strictly zero-exchange implementation cannot use that resource with high fidelity for a nontrivial target. A finite exchange opens a finite target dimension, and a fluctuation-scale exchange recovers the known unrestricted leading capacity.

All claims are existence and optimality statements with unrestricted local computation on a known catalyst. The construction can require a very large classical outcome alphabet. Half filling, equal bipartitions, unknown-catalyst learning, efficient circuit synthesis, an average-only exchange budget, and an unconditional dynamical growth theorem are not covered. The [physical interpretation](interpretation.md) and [related work](../references/RELATED_WORK.md) locate these boundaries.

Continue with [typical states](typical_states.md) for the ensemble reduction, or with [finite optimization](finite_optimization.md) for the exact operational problem. [Verification](../verification/README.md) explains what the finite calculations check.
