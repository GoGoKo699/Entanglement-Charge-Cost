# Coherent extraction with charged buffers

A charge-respecting protocol must preserve the coherence between different
local particle numbers while changing the entanglement available inside each
number sector. The measurement outcomes can reveal which local conversion was
used unless their probabilities are synchronized. This page constructs a
finite LOCC instrument whose outcomes are uniformly distributed in every
retained sector. It includes both rank reduction and approximate embedding
when the source rank is too small.

The construction uses the charge-sector conversion methods of
[Schuch, Verstraete and Cirac, Secs. II–III.1](https://arxiv.org/html/quant-ph/0404079v1).
In particular, refining sector-dependent outcomes to a common distribution
and implementing definite charge shifts with charge eigenstate ancillas are
established methods. Here their charge shifts and joint catalyst–target
overlaps are kept explicit. The operational definitions are in
[the model](model.md); the matching bounds are in [the converse](converse.md).

## 1. Physical block states and target coordinates

Consider finite catalyst Hilbert spaces with local charge decompositions

```math
\mathcal H_A=\bigoplus_q\mathcal H_{A,q},\qquad
\mathcal H_B=\bigoplus_j\mathcal H_{B,j}.
```

Fix total catalyst charge $`N`$. Let $`\mathcal Q`$ be a finite set of charges,
$`p_q>0`$ on $`\mathcal Q`$, and $`\sum_qp_q=1`$. For each $`q\in\mathcal Q`$,
choose $`d_q`$ orthonormal vectors in each of
$`\mathcal H_{A,q}`$ and $`\mathcal H_{B,N-q}`$, so that

```math
1\le d_q\le
\min\{\dim\mathcal H_{A,q},\dim\mathcal H_{B,N-q}\}.
```

The known catalyst is

```math
|\Omega\rangle
=\sum_{q\in\mathcal Q}\sqrt{p_q}\,|\Phi_{d_q};q,N-q\rangle,
\qquad
|\Phi_{d_q};q,N-q\rangle
=\frac1{\sqrt{d_q}}\sum_{i=0}^{d_q-1}|q,i\rangle_A|N-q,i\rangle_B.
\tag{1}
```

Unwritten weights are zero. The target registers are neutral and initially
in a product state. In the ideal output
$`|\tau\rangle=|\Omega\rangle\otimes|\Phi_m\rangle`$, the component with
Alice catalyst charge $`q'`$ is maximally entangled of rank $`m d_{q'}`$.
Use the same flattening of the catalyst and target indices on both sides;
for example, $`\ell=m i+j`$. Denote this normalized component by
$`|\Theta_{q'}\rangle`$. Thus

```math
|\tau\rangle=\sum_{q'\in\mathcal Q}\sqrt{p_{q'}}\,|\Theta_{q'}\rangle.
\tag{2}
```

These are actual vectors in the physical Hilbert space, not formal Schmidt
lists. For the fixed-charge Haar application, the dimensions
$`a_q=\binom{L_A}{q}`$ need not fit inside Bob's sector at every extreme
charge. The reference (1) is therefore formed on the normalized linear
window of [the typical-state proof](typical_states.md), where
$`d_q=a_q\le b_q`$. No operation below assumes that the untruncated mean
marginal has a physical purification.

## 2. A fixed-shift fidelity bound

Use $`k=q_{\mathrm{out}}-q_{\mathrm{in}}`$. Fix an integer $`k`$ and a set
$`T\subseteq\mathcal Q`$ such that $`q+k\in\mathcal Q`$ for every $`q\in T`$.
The successful part of the protocol shifts Alice by $`k`$, Bob by $`-k`$,
and changes the local buffers by the opposite amounts. Define

```math
a_q=d_q,\qquad D_{q,k}=m d_{q+k},\qquad
c_{q,k}=\sqrt{\min\{1,a_q/D_{q,k}\}}.
\tag{3}
```

**Fixed-shift construction.** There is a charge-conserving LOCC implementation
with all net shifts in $`\{0,k\}`$ on Alice and $`\{0,-k\}`$ on Bob whose
unconditional root fidelity satisfies

```math
F(\rho_{\mathrm{out}},\tau)
\ge\sum_{q\in T}\sqrt{p_qp_{q+k}}\,c_{q,k}.
\tag{4}
```

Every measurement outcome is included. In particular, the probability of
the input lying outside $`T`$ is not divided out. The bound does not require
$`a_q\ge D_{q,k}`$: sectors with a rank deficit are retained with their exact
overlap factor in (3).

### Rank reduction in one sector

For positive integers $`a\ge b`$, Alice can reduce $`|\Phi_a\rangle`$ to
$`|\Phi_b\rangle`$ with the cyclic-subset Kraus operators

```math
K_j=\frac1{\sqrt b}
\sum_{\ell=0}^{b-1}|\ell\rangle
\langle j+\ell\pmod a|,
\qquad j=0,\ldots,a-1.
\tag{5}
```

Each input basis vector belongs to exactly $`b`$ cyclic subsets, so
$`\sum_jK_j^\dagger K_j=I_a`$. Given $`j`$, Bob maps
$`|j+\ell\pmod a\rangle`$ to $`|\ell\rangle`$ on the occupied subspace.
The unnormalized corrected vector is $`|\Phi_b\rangle/\sqrt a`$, and
every outcome has probability $`1/a`$.

This distribution depends on $`a`$, which is why applying (5) independently
in several charge sectors does not by itself establish a coherent protocol.

### A common outcome alphabet

Choose a positive integer $`R`$ divisible by every $`a_q`$ in a rank-reduction
sector $`q\in T`$. If there are no such sectors, $`R=1`$ is sufficient.
For $`r=0,\ldots,R-1`$, set $`j_q(r)=r\bmod a_q`$. When $`a_q\ge D_{q,k}`$, use

```math
K_{r,q}
=\sqrt{\frac{a_q}{R D_{q,k}}}
\sum_{\ell=0}^{D_{q,k}-1}
|q+k,\ell\rangle_{AA'}
\langle q,j_q(r)+\ell\pmod{a_q}|_A.
\tag{6}
```

The output ket uses the coordinates of the target block (2). Repeating each
cyclic subset $`R/a_q`$ times gives
$`\sum_rK_{r,q}^\dagger K_{r,q}=I_{a_q}`$. Bob's corrected vector is now
$`|\Theta_{q+k}\rangle/\sqrt R`$, independently of $`q`$.

If $`a_q<D_{q,k}`$, use instead

```math
K_{r,q}=\frac1{\sqrt R}
\sum_{i=0}^{a_q-1}|q+k,i\rangle_{AA'}\langle q,i|_A.
\tag{7}
```

Bob embeds the same $`a_q`$ basis vectors into the first $`a_q`$ coordinates
of the rank-$`D_{q,k}`$ target block. Let the resulting normalized vector be
$`|\chi_{q,k}\rangle`$. For a rank-reduction sector set
$`|\chi_{q,k}\rangle=|\Theta_{q+k}\rangle`$. In both cases,

```math
\langle\Theta_{q+k}|\chi_{q,k}\rangle=c_{q,k},
\qquad
(K_{r,q}\otimes V_{r,q})|\Phi_{a_q}\rangle
=\frac1{\sqrt R}|\chi_{q,k}\rangle.
\tag{8}
```

The vector in a deficit sector need not factor into a returned catalyst and
an entangled target. Its overlap with that complete product is precisely
what the joint return criterion measures.

Take Alice's direct-sum Kraus operator
$`K_r=\bigoplus_{q\in T}K_{r,q}`$. Different input charges have different
output charges because $`k`$ is fixed. Consequently the direct sum creates
no cross terms in $`K_r^\dagger K_r`$, and

```math
\sum_rK_r^\dagger K_r=\Pi_T,
\tag{9}
```

where $`\Pi_T`$ projects onto the selected Alice Schmidt subspaces. This
projector commutes with charge. An additional charge-preserving Kraus
operator $`J_A(I-\Pi_T)`$, where $`J_A`$ appends a product target register,
completes Alice's instrument on the full physical input space. This
complementary outcome is an ordinary retained failure outcome.

### Bob's correction is a complete physical channel

For each announced $`r`$, let $`P_{r,q}`$ project onto the Bob Schmidt
coordinates selected by (6), or onto all $`a_q`$ coordinates in (7).
The direct sum $`P_r=\bigoplus_{q\in T}P_{r,q}`$ commutes with Bob's charge.
The intended correction $`V_r`$ is the direct sum of the partial isometries
in (8). Its initial projection is

```math
V_r^\dagger V_r=P_r,
\tag{10}
```

and its charge shift is $`-k`$. There is enough output dimension because
the occupied rank is $`\min(a_q,D_{q,k})\le D_{q,k}`$, and $`|\Theta_{q+k}\rangle`$
already fits in the physical output sector.

It is unnecessary to assume that this partial isometry extends to a unitary
on the catalyst and target alone. Let $`J_B`$ append a product target register
without changing Bob's catalyst. The two Kraus operators

```math
V_r,\qquad C_r=J_B(I-P_r)
\tag{11}
```

define a trace-preserving channel, since their adjoint products sum to the
identity. The second has charge shift zero. On the selected block-flat input,
Alice's outcome $`r`$ leaves Bob entirely in $`P_r`$, including the coherent
superposition of its charge sectors. Thus $`C_r`$ has exactly zero probability
on this part of the input. If a unitary realization is desired, neutral local
work space can supply the complementary output dimensions in the dilation.
Neither construction measures the individual value of $`q`$.

### The unconditional overlap

For each successful $`r`$, the complete unnormalized output on the original
normalized input is

```math
|\Psi_{r,k}\rangle
=\frac1{\sqrt R}
\sum_{q\in T}\sqrt{p_q}\,|\chi_{q,k}\rangle.
\tag{12}
```

Each such outcome has probability $`p_T/R`$, where
$`p_T=\sum_{q\in T}p_q`$. Conditional on this part of the input, the outcome
distribution is uniform and carries no information about the charge sector.
Every normalized branch vector is identical. In particular, discarding the
classical record preserves the sector coherence.

Equations (2), (8), and (12) give

```math
\sum_{r=0}^{R-1}|\langle\tau|\Psi_{r,k}\rangle|^2
=\left(\sum_{q\in T}\sqrt{p_qp_{q+k}}\,c_{q,k}\right)^2.
\tag{13}
```

Other outcomes add nonnegative terms to the squared fidelity. Taking the
square root proves (4). A preliminary projection onto $`T`$, if used as a
separate implementation step, yields the same expression: its success
probability cancels the normalization of its conditional state.

## 3. Charge-conserving dilations and net exchange

Every successful Alice Kraus operator obeys

```math
Q_A^{\mathrm{out}}K_r-K_rQ_A^{\mathrm{in}}=kK_r.
\tag{14}
```

Bob's successful correction has the opposite mode. More generally, a
trace-preserving instrument with fixed-mode Kraus operators $`M_j`$ of
shifts $`k_j`$ has a charge-conserving isometric dilation

```math
W|\varphi\rangle|E\rangle_R
=\sum_j M_j|\varphi\rangle\,|E-k_j\rangle_R\,|j\rangle_C.
\tag{15}
```

The outcome register $`C`$ is neutral. Completeness makes $`W`$ an isometry;
the total charge of each term equals that of its input. Finite neutral
padding allows it to extend, charge sector by charge sector, to a unitary
on a larger local space. Measuring or discarding $`C`$ implements the
instrument. All buffer states in (15) are charge eigenstates. No coherent
phase reference is supplied.

For a protocol using both signs of $`k`$ with $`|k|\le S`$, the construction
can take $`E=S`$ and buffer charges $`0,\ldots,2S`$. For the favorable
single shift $`k=-s`$, $`0\le s\le S`$, Alice can start with buffer charge
zero and finish with $`s`$; Bob can start at $`S`$ and finish at $`S-s`$.
The roles reverse for a favorable positive shift. The successful buffer
outputs depend on the announced shift, but not on $`q`$ or the refined
outcome $`r`$, so they reveal no hidden sector label.

The buffers are changed resources. Their return is not part of the catalyst
return criterion. These examples show sufficient physical implementations;
the budget $`S`$ is the maximum supported absolute **net** shift, not a
general theorem about peak buffer occupation, total transport, or the
smallest possible reservoir.

## 4. Charge-dependent filtering and the finite optimum

The fixed-shift protocol also provides the lower bound for the
[exact finite optimization](finite_optimization.md). Let $`T_{kq}\ge0`$ satisfy
$`\sum_kT_{kq}=1`$ for every populated source charge, with $`|k|\le S`$ and
only physically allowed destinations assigned nonzero weight. Alice first
uses the charge-diagonal filter

```math
D_k=\bigoplus_{q\in\mathcal Q}\sqrt{T_{kq}}\,I_{d_q}.
\tag{16}
```

This first operation has zero charge shift. After announcing $`k`$, the
parties apply (6)–(11), with a common uniform outcome alphabet for this
value of $`k`$. The filter is allowed to reveal information about $`q`$;
the subsequent outcome refinement introduces no further loss of coherence.
Its full contribution to squared fidelity is

```math
\left(
\sum_q\sqrt{p_qp_{q+k}}
\sqrt{\min\left\{1,\frac{d_q}{m d_{q+k}}\right\}}
\sqrt{T_{kq}}
\right)^2.
\tag{17}
```

If a destination is physically present but has zero target weight,
$`p_{q+k}=0`$, its contribution in (17) is defined to be zero. One may
convert that source block coherently to any fixed product vector in the
destination sector by the rank-one version of (6), with the same outcome
refinement. This preserves the required branch probability without
inventing a target rank for an unpopulated sector. Physically absent
destinations are excluded. Unpopulated source inputs are completed by
charge-preserving operations, as in (9).

Summing (17) over the announced shifts counts every branch and gives the
finite program's achievable objective. All successful leaves have
$`(k_A,k_B)=(k,-k)`$; the complementary operations above satisfy the same
absolute bounds on each party. Thus the optimum is unchanged if both
laboratories, rather than only Alice, are constrained by $`S`$.

## 5. Application to typical fixed-charge states

For the physical reference of [the typical-state proof](typical_states.md),
choose a narrower source window and a favorable shift
$`k=-\operatorname{sgn}(\mu)s`$. Provided this window and its translate
remain inside the linear reference window, (4) applies with
$`d_q=\binom{L_A}{q}`$ and the normalized hypergeometric weights.

At fixed $`m,S`$, the rank factor tends to
$`\sqrt{\min\{1,e^{|\mu|S}/m\}}`$, while the charge-distribution overlap
tends to one. The hybrid construction therefore includes the equality
case $`m=e^{|\mu|S}`$, even when some individual finite-size sectors cannot
be converted exactly. At $`S=O(\sqrt L)`$, a subleading rank slack makes
all retained sectors rank-excess sectors; the remaining overlap is the
Gaussian shift overlap. The quantifiers and bounds are proved in
[the converse](converse.md) and [the asymptotic capacity analysis](asymptotics.md).

Finally, apply the same physical channel to the actual known Haar state,
using the charge-preserving alignment with its reference. Uniform
purified-distance continuity transfers the performance. The outcome
alphabet and local circuit description may be large: this is an existence
and capacity construction, with no efficient compilation claim.

Return to [the model](model.md), continue to [the converse](converse.md), or
use the construction in [the finite optimization](finite_optimization.md).
