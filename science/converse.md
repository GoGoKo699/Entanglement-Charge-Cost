# Converse for arbitrary charged LOCC

The charge cost comes from a local rank restriction: a branch cannot create
more Schmidt dimensions inside its shifted output sector than were present
in the corresponding input sector. The restriction survives arbitrary
filtering, classical communication, and adaptive choices. The proof below
keeps all complete outcomes and bounds their summed fidelity without a
factor depending on the number of branches.

The [model](model.md) defines the implementation class and the hard net
budget. The [coherent protocol](coherent_protocol.md) supplies matching
constructions, including sectors with a rank deficit. The symmetry
framework is standard: definite-mode Kraus representations and
charge-eigenstate auxiliary implementations are described by
[Schuch, Verstraete and Cirac](https://arxiv.org/html/quant-ph/0404079v1)
and [Gour and Spekkens, Lemma 2](https://arxiv.org/html/0711.0043v2).

## 1. Complete charge-resolved leaves

Work first with a physically valid block-flat catalyst

```math
|\Omega\rangle
=\sum_{q\in\mathcal Q}\sqrt{p_q}\,|\Phi_{d_q};q,N-q\rangle,
\qquad p_q>0,\quad\sum_qp_q=1,
\tag{1}
```

with the dimension and basis conventions of
[coherent extraction](coherent_protocol.md). The target is
$|\tau\rangle=|\Omega\rangle\otimes|\Phi_m\rangle$. Its charge-$q$
component is a maximally entangled vector $|\Theta_q\rangle$ of rank
$m d_q$, with amplitude $\sqrt{p_q}$.

Resolve every local instrument using its charge-conserving dilation.
A charge-incoherent initial ancilla can be diagonalized inside each of its
charge sectors. Its initial labels may be included in a refinement of the
classical record. Resolving the final environment in a charge eigenbasis
then gives local Kraus operators with a definite charge difference between
output and input. Discarded local work systems are included in this
refinement. No experimenter needs to observe these additional labels; a
Kraus refinement leaves the reduced output density operator unchanged.

Conditioning on all earlier classical outcomes, compose the local Kraus
operators along each complete leaf $r$. Its operator on the two input
catalysts is a product

```math
M_r=A_r\otimes B_r,
\qquad
\sum_r M_r^\dagger M_r=I.
\tag{2}
```

Preparation of the neutral target registers is absorbed into $A_r,B_r$.
Their charge shifts add along the leaf, so

```math
Q_A^{\rm out}A_r-A_rQ_A^{\rm in}=k_{A,r}A_r,
\qquad
Q_B^{\rm out}B_r-B_rQ_B^{\rm in}=k_{B,r}B_r.
\tag{3}
```

The hard budget is $|k_{A,r}|\le S$ on every complete leaf. It is a
constraint on the net shift (3); intermediate shifts need not individually
obey it. The proof places no bound on the number of rounds, the number of
Kraus operators, or the intermediate ancilla dimension.

A leaf with $k_{A,r}+k_{B,r}\ne0$ has retained total charge different
from $N$, and hence zero overlap with $|\tau\rangle$. Its probability
is still included in (2) and in the output. For an overlap-bearing leaf
write $k_r=k_{A,r}=-k_{B,r}$. Finite or countable sums below also cover
classical randomization and almost-surely terminating adaptive protocols.
The inequalities are continuous in the reduced channel and therefore hold
for the limits of finite-round admissible protocols included in the model.

## 2. Sector rank bounds the amplitude of every leaf

For each normalized source block define

```math
t_{r,q}=\|M_r|\Phi_{d_q};q,N-q\rangle\|^2.
\tag{4}
```

These numbers are defined for all leaves, including those whose total shift
is incompatible with the target. Trace preservation gives

```math
\sum_r t_{r,q}=1\qquad(q\in\mathcal Q).
\tag{5}
```

**Rank-overlap bound.** If an unnormalized bipartite vector has Schmidt rank
at most $d$, squared norm $t$, and is compared with a normalized
maximally entangled vector of rank $D$, its overlap has modulus at most

```math
\sqrt{t}\,\sqrt{\min\{1,d/D\}}.
\tag{6}
```

To prove (6), project the vector onto the local supports of the target and
write its coefficient matrix as $X$. Projection cannot increase its rank
or Hilbert–Schmidt norm. The target overlap is
$\operatorname{Tr}X/\sqrt D$, up to conjugation of the chosen bases.
The nuclear-norm inequality
$|\operatorname{Tr}X|\le\|X\|_*\le\sqrt d\,\|X\|_2$, together with
the ordinary Cauchy–Schwarz bound $\sqrt t$, proves the claim.

A product Kraus operator cannot increase the Schmidt rank of the input
block. In an overlap-bearing leaf the block with input charge $q$ can
overlap only the target block $q+k_r$. Define

```math
c_{q,k}=\sqrt{\min\left\{1,\frac{d_q}{m d_{q+k}}\right\}}
\quad\text{if }p_{q+k}>0,
\tag{7}
```

and set its weighted contribution to zero when $p_{q+k}=0$. Equation
(6) and the triangle inequality give the complete branch-amplitude bound

```math
|z_r|:=|\langle\tau|M_r|\Omega\rangle|
\le\sum_{q\in\mathcal Q}
\sqrt{p_qp_{q+k_r}}\,c_{q,k_r}\sqrt{t_{r,q}}.
\tag{8}
```

This already allows arbitrary charge-dependent filtering: its effect is
contained in $t_{r,q}$, which need not be independent of $q$. Because
the reference target is pure, the complete output satisfies

```math
F(\rho_{\rm out},\tau)^2=\sum_r|z_r|^2.
\tag{9}
```

No conditional success probability is removed from (9).

## 3. A uniform bound with an input tail

Let $G\subseteq\mathcal Q$ have probability $1-\eta$. Suppose a
constant $c_G\in[0,1]$ bounds $c_{q,k}$ for every $q\in G$ and
every allowed $|k|\le S$ with nonzero target weight. Then every admissible
protocol obeys

```math
F(\rho_{\rm out},\tau)
\le c_G\sqrt{1-\eta}+\sqrt\eta
\le c_G+\sqrt\eta.
\tag{10}
```

An overall upper bound of one may of course be imposed as well.

For the proof, first keep only the source terms in $G$. For each
overlap-bearing leaf, Cauchy–Schwarz in (8) yields

```math
|z_r^{G}|^2
\le c_G^2
\left(\sum_{q\in G}p_q t_{r,q}\right)
\left(\sum_{q\in G}p_{q+k_r}\right)
\le c_G^2\sum_{q\in G}p_qt_{r,q}.
\tag{11}
```

Sum over leaves and use (5). This bounds the Euclidean norm of the vector
$(z_r^G)_r$ by $c_G\sqrt{1-\eta}$.

For the source tail, use the isometry
$V=\sum_rM_r\otimes|r\rangle$ supplied by (2). The tail vector in (1)
has norm $\sqrt\eta$. Applying $V$, and then the contraction
$\langle\tau|\otimes I$, shows that the Euclidean norm of its branch
amplitudes is at most $\sqrt\eta$. The triangle inequality for these
two vectors gives (10). The argument works with any number of leaves and
does not multiply the tail by an outcome count.

### Exact zero-exchange identity

At $S=0$, every overlap-bearing leaf has $k_r=0$, so
$c_{q,0}=1/\sqrt m$ for every populated block. Choose $G=\mathcal Q$
in (10). This proves

```math
[F^\star(m,0;\Omega)]^2\le\frac1m.
```

Doing nothing to the catalyst and leaving the target in a product basis
state attains overlap $1/\sqrt m$. Therefore

```math
\boxed{[F^\star(m,0;\Omega)]^2=\frac1m.}
\tag{12}
```

This is exact for every finite physically valid block-flat catalyst. It
becomes a limit for typical Haar catalysts through
[the charge-preserving approximation](typical_states.md). It does not
assert that all pure states have the same zero-exchange ceiling.

## 4. Grouping all leaves gives the finite optimization

Define the nonnegative overlap coefficients

```math
A_{kq}=\sqrt{p_qp_{q+k}}\,c_{q,k},
\tag{13}
```

with $A_{kq}=0$ if the target weight vanishes. For each shift $k$, group
the overlap-bearing leaves and set

```math
T_{kq}=\sum_{r:\,(k_{A,r},k_{B,r})=(k,-k)}t_{r,q}.
```

Minkowski's inequality applied to the vector of amplitudes within this
group gives

```math
\left(\sum_{r:\,(k,-k)}|z_r|^2\right)^{1/2}
\le\sum_q A_{kq}\sqrt{T_{kq}}.
\tag{14}
```

The columns initially satisfy $\sum_kT_{kq}\le1$, rather than necessarily
equality: leaves with the wrong total charge have zero fidelity but can
have nonzero probability. Add the missing column mass to $k=0$, which
is always physically possible. Nonnegativity of every coefficient means
this cannot decrease the right-hand side of the resulting objective.
Thus every protocol is bounded by

```math
\max_{T\ge0,\ \sum_kT_{kq}=1}
\sum_k\left(\sum_q A_{kq}\sqrt{T_{kq}}\right)^2,
\tag{15}
```

with physically absent output sectors excluded from the variables. This
completion is a mathematical upper-bound step, not a removal or
renormalization of failure outcomes. The filter followed by coherent
conversion in [the construction](coherent_protocol.md) attains the
objective, establishing the exact finite characterization. Its dual and
compressed formulation are developed in [finite optimization](finite_optimization.md).

## 5. Uniform rank ratios for the Haar comparison family

Use the fixed parameters and integer sequences of
[the asymptotic analysis](asymptotics.md):
$n_L=\lfloor fL\rfloor$, $N_L=\lfloor\nu L\rfloor$,
$\nu_L=N_L/L$, $\bar q_L=n_L\nu_L$, and

```math
a_{L,q}=\binom{n_L}{q},\qquad
\mu_L=\ln\frac{1-\nu_L}{\nu_L},\qquad
\mu=\ln\frac{1-\nu}{\nu},\qquad\gamma=|\mu|>0.
\tag{16}
```

Exact integer-compatible sequences are a special case. The physical
comparison state is normalized on the fixed linear window from
[typical states](typical_states.md), with $d_q=a_{L,q}$. In the smaller
windows used below, both $q$ and every considered $q+k$ lie inside
that physical window for sufficiently large $L$.

The adjacent-binomial identity

```math
\ln a_{L,u+1}-\ln a_{L,u}
=\ln\frac{n_L-u}{u+1}
```

gives, uniformly whenever $|q-\bar q_L|+|k|=o(L)$,

```math
\ln\frac{a_{L,q}}{a_{L,q+k}}
=-\mu_L k+
O\!\left(\frac{|k|(|q-\bar q_L|+|k|+1)}L\right).
\tag{17}
```

The constant depends only on the fixed interior parameters. This estimate
is proved by summing adjacent logarithmic ratios in
[Lemma 1 of the asymptotic analysis](asymptotics.md). The normalized
truncation changes charge probabilities by an exponentially small amount;
it does not change the ranks in (17).

### The budget strong converse at scale $\sqrt L$

For each fixed $C<\infty$, consider all integer budgets
$0\le S\le C\sqrt L$. On
$G_L=\{q:|q-\bar q_L|\le\sqrt L\log L\}$, equation (17) implies,
uniformly over all $|k|\le S$,

```math
\ln\frac{a_{L,q}}{a_{L,q+k}}
\le\gamma S+C_1\log L
\tag{18}
```

for some $C_1$ depending on $C,f,\nu$. The charge variance is $O(L)$,
so the omitted mass is $O((\log L)^{-2})$, even using only Chebyshev's
inequality. Equation (10) therefore yields constants $C_1,C_2$ for which

```math
F_L^\star(m,S;\Omega_L)
\le
\sqrt{\min\left\{1,
\frac{e^{\gamma S+C_1\log L}}m\right\}}
+\frac{C_2}{\log L},
\tag{19}
```

for all $m\ge1$, all $0\le S\le C\sqrt L$, and sufficiently large
$L$. The bound is uniform over the implementation and target dimension.

In particular, for every $c>0$,

```math
\ln m_L\ge\gamma S_L+c\sqrt L,
\qquad S_L=O(\sqrt L)
\quad\Longrightarrow\quad
F_L^\star(m_L,S_L;\Omega_L)\longrightarrow0.
\tag{20}
```

This is the charge-budget part of the leading capacity converse. It does
not assume that the protocol itself uses a deterministic shift, or that
all its branches have the same probability. The Gaussian upper bound for
unrestricted LOCC supplies the independent fluctuation cap; its application
to mixed outputs and the combination of both caps are given in
[the capacity proof](asymptotics.md).

## 6. Fixed budgets and the full sub-$\sqrt L$ transition

For fixed budgets the $O(\log L)$ error in (18) is too coarse. Use instead
an adaptive window

```math
G_L=\{q:|q-\bar q_L|\le M_L\sqrt L\},
\quad M_L\to\infty,\quad M_L=o(\sqrt L),\quad
\frac{S_LM_L}{\sqrt L}\to0.
\tag{21}
```

Such a choice exists whenever $S_L=o(\sqrt L)$; for example use the
minimum of $L^{1/8}$ and $(\sqrt L/(S_L+1))^{1/2}$. Its omitted
probability is $O(M_L^{-2})=o(1)$. Equation (17) becomes

```math
\ln\frac{a_{L,q}}{a_{L,q+k}}
=-\mu k+o(1),
\tag{22}
```

uniformly for $q\in G_L$ and all $|k|\le S_L$. Here
$\mu_L-\mu=O(L^{-1})$, so replacing $\mu_L$ is harmless.

**Sub-fluctuation transition.** Suppose
$S_L=o(\sqrt L)$ and the positive integer target dimensions satisfy

```math
\ln m_L-\gamma S_L\longrightarrow c\in\mathbb R.
\tag{23}
```

Then

```math
\boxed{
[F_L^\star(m_L,S_L;\Omega_L)]^2
\longrightarrow\min\{1,e^{-c}\}.}
\tag{24}
```

For the upper bound, (22) bounds every allowed ratio in (7) by
$\exp(\gamma S_L-\ln m_L+o(1))$. The constant $c_G$ in (10) can
therefore be chosen as
$\sqrt{\min\{1,\exp(-c+o(1))\}}$. The tail term vanishes.

For the lower bound, choose the favorable deterministic shift
$k_L=-\operatorname{sgn}(\mu)S_L$ and the same window $G_L$.
The ratio now has equality in its leading exponent, uniformly:

```math
\frac{a_{L,q}}{m_La_{L,q+k_L}}
=\exp(-c+o(1)).
\tag{25}
```

The hybrid construction's rank factor consequently tends uniformly to
$\sqrt{\min\{1,e^{-c}\}}$. The hypergeometric shift-overlap estimate
in [Lemma 2 of the asymptotic analysis](asymptotics.md) gives

```math
\sum_q\sqrt{p_{L,q}p_{L,q+k_L}}\longrightarrow1
\qquad\text{when }k_L=o(\sqrt L).
\tag{26}
```

Removing the source tail of (21) changes this sum by at most
$\sqrt{\Pr(Q_A\notin G_L)}$, by Cauchy–Schwarz. The physical linear
truncation changes it by another vanishing amount. Thus (4) of
[the construction](coherent_protocol.md) proves the matching lower bound.

In particular, for fixed integers $m\ge1$ and $S\ge0$, set
$c=\ln m-\gamma S$ to obtain

```math
\boxed{
[F_L^\star(m,S;\Omega_L)]^2
\longrightarrow\min\{1,e^{\gamma S}/m\}.}
\tag{27}
```

When $m=e^{\gamma S}$, the exponent in (25) tends to zero from either
side depending on the sector. Its minimum-with-one rank factor still
tends uniformly to one. This proves the equality boundary without
requiring exact rank reduction in every finite-size sector. It is the
reason the rank-deficit part of the construction is needed.

The same upper and lower arguments give fidelity limits zero or one when
the expression on the left of (23) tends respectively to $+\infty$ or
$-\infty$. This observation yields the smaller-scale capacity limit for
diverging $S_L=o(\sqrt L)$ stated in [the asymptotic analysis](asymptotics.md).

## 7. Transfer to actual Haar catalysts

The physically truncated flat state $|\Omega_L\rangle$ is aligned with
the actual Haar state $|\psi_L\rangle$ using charge-resolved Schmidt
bases. As proved in [typical states](typical_states.md), with probability
tending to one its purified distance
$\zeta_L=P(\psi_L,\Omega_L)$ is exponentially small. Uniformly in
$m,S$,

```math
\left|
F_L^\star(m,S;\psi_L)-F_L^\star(m,S;\Omega_L)
\right|\le2\zeta_L.
\tag{28}
```

Thus (20), (24), and (27) hold for typical Haar catalysts in probability.
In particular, the zero-exchange limit is $1/m$, although the exact
finite-size identity (12) applies only to the flat reference. All fixed
budget and growing-budget claims use the complete catalyst–target return
criterion, the hard support constraint on net exchange, and known input
states. They do not apply without modification to a mean-only cost or to
targets that themselves carry fluctuating local charge.

Return to [the model](model.md), examine the attaining
[coherent protocol](coherent_protocol.md), or continue to
[finite optimization](finite_optimization.md) and
[the asymptotic capacity](asymptotics.md).
