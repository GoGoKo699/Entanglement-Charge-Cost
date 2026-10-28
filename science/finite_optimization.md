# Exact optimization for finite flat-sector catalysts

This section gives an exact finite-dimensional optimum, including adaptive LOCC, filters, and unsuccessful outcomes. Its numerical evaluation is separate from the asymptotic statements in [asymptotics.md](asymptotics.md) and the approximation of typical Haar states in [typical_states.md](typical_states.md).

## State and operational assumptions

Let $\mathcal Q$ be the finite support of a probability distribution $p_q>0$. The known catalyst is

```math
|\Psi\rangle=\sum_{q\in\mathcal Q}\sqrt{p_q}
 |\Phi_{d_q};q,N-q\rangle,
\qquad d_q\in\mathbb N.
```

Each indicated maximally entangled vector must fit the actual Alice and Bob charge sectors. In particular, a mean marginal is not automatically the marginal of a pure state in the original physical Hilbert space. A typical-sector restriction or explicit neutral padding must be stated when needed.

The desired output is $|\Psi\rangle\otimes|\Phi_m\rangle$, where the target is locally charge neutral and its input is a product state. We use the complete-output root fidelity and the implementation class of [model.md](model.md). A complete local Kraus leaf has definite catalyst shifts $k_A,k_B$. Alice's hard budget is $|k_A|\le S$. Only $k_B=-k_A$ leaves can overlap the target. The same optimum is attainable with both local shifts bounded by $S$.

Neutral local workspace, initially unentangled across the laboratories, can have arbitrary finite dimension and need not be returned. It allows corrections defined on a selected Schmidt subspace to extend to physical local channels. It supplies no entanglement or coherent charge reference. The support budget is a net exchange constraint, not a peak buffer occupation, cumulative throughput, or circuit cost.

Write $\mathcal K=\{-S,\ldots,S\}$ and set

```math
A_{kq}=\begin{cases}
\sqrt{p_qp_{q+k}}
\sqrt{\min\{1,d_q/(m d_{q+k})\}},&q+k\in\mathcal Q,\\
0,&q+k\notin\mathcal Q.
\end{cases}
```

Every nonzero entry describes a physically existing target sector. Source sectors of zero weight are removed. In particular,

```math
A_{0q}=p_q/\sqrt m>0.
```

Allocating probability to a destination outside the target support cannot improve the objective. Such allocation can be reassigned to $k=0$ without decreasing any term that contains a nonzero coefficient. Consequently the formulas may use the full rectangular array $\mathcal K\times\mathcal Q$, with zero coefficients for missing destinations. An attaining protocol chooses zero allocation on physically impossible destinations. A zero-overlap but physically existing destination may instead be retained as an ordinary failure outcome.

## The finite primal problem

**Theorem.** The optimal squared fidelity is

```math
[F^\star(m,S;\Psi)]^2
=\max_{\substack{T_{kq}\ge0\\\sum_kT_{kq}=1\ \forall q}}
\sum_{k\in\mathcal K}
\left(\sum_{q\in\mathcal Q}A_{kq}\sqrt{T_{kq}}\right)^2.
\tag{1}
```

The maximum exists. An optimum is attained by a finite-round, one-way LOCC protocol consisting of a charge-diagonal filter and coherent sector conversion.

### Upper bound, including failures

Refine a protocol into complete product Kraus leaves $r$. On the normalized source sector define

```math
t_{rq}=\|(A_r\otimes B_r)|\Phi_{d_q};q,N-q\rangle\|^2.
```

Trace preservation gives $\sum_r t_{rq}=1$ for each $q$. A product Kraus operator cannot increase the Schmidt rank $d_q$. Therefore a leaf with opposite shifts $(k,-k)$ has target amplitude bounded by

```math
|z_r|\le\sum_q A_{kq}\sqrt{t_{rq}}.
\tag{2}
```

This is the rank bound in [converse.md](converse.md). It also bounds a leaf with additional local environment labels, since those labels are included in the Kraus refinement.

Group overlap-bearing leaves by their shift and put $T_{kq}=\sum_{r:k_r=k}t_{rq}$. The triangle inequality for Euclidean vectors indexed by the leaves yields

```math
\sum_{r:k_r=k}\left(\sum_qA_{kq}\sqrt{t_{rq}}\right)^2
\le\left(\sum_qA_{kq}\sqrt{T_{kq}}\right)^2.
\tag{3}
```

Leaves whose total shift is nonzero have zero overlap, but their probabilities must not be silently discarded. Before completing the columns, $\sum_kT_{kq}\le1$. Assign each column's residual to $T_{0q}$. All coefficients are nonnegative, so this only increases the right-hand side of (3). Summing (3) proves the upper bound in (1). The bound also holds for limits of finite-round protocols by continuity of the fidelity.

### Attaining a feasible filter

Take a feasible $T$. Reassign its allocations on missing target sectors to $k=0$ if necessary. Alice applies the charge-diagonal instrument

```math
C_k=\bigoplus_{q\in\mathcal Q}\sqrt{T_{kq}}\,I_{d_q}
```

and announces $k$. These operators have charge mode zero and satisfy $\sum_kC_k^\dagger C_k=I$ on the occupied support. On the input state the unnormalized branch is

```math
\sum_q\sqrt{p_qT_{kq}}\,|\Phi_{d_q};q,N-q\rangle.
```

For a destination $q+k$, let $b_q=m d_{q+k}$. Apply the coherent conversion of [coherent_protocol.md](coherent_protocol.md):

- If $d_q\ge b_q$, reduce the maximally entangled rank deterministically from $d_q$ to $b_q$.
- If $d_q<b_q$, embed the $d_q$ Schmidt vectors isometrically into the $b_q$ target vectors.

In both cases the output normalized sector state has overlap $\sqrt{\min\{1,d_q/b_q\}}$ with the sector target. The second case need not factor into a returned catalyst and a perfect target. The task scores their joint fidelity.

Here is the trace-preservation check that makes the two cases compatible. Choose $R$ divisible by all occupied source ranks. For a sector of ranks $a\ge b$, Alice's refined operators are

```math
K_{r}^{(a,b)}=
\sqrt{\frac{a}{Rb}}\sum_{\ell=0}^{b-1}
|\ell\rangle\langle(r+\ell)\bmod a|,
\qquad r=0,\ldots,R-1.
\tag{4}
```

Each source basis vector occurs in exactly $Rb/a$ selected subsets, so $\sum_r K_r^\dagger K_r=I_a$. Every outcome has probability $1/R$ on $\Phi_a$. Bob relabels the selected vectors and extends that correction to an isometry using neutral workspace. For $a<b$, use the fixed embedding $V$ with Alice's operators $V/\sqrt R$ and Bob's fixed embedding. Again the instrument is trace preserving and every outcome has probability $1/R$.

Taking the direct sum over charge sectors makes the same refined outcome uniform in every sector. Bob's correction is also controlled by his charge sector. Thus no measurement record reveals $q$ within a fixed $k$ branch. The retained branch is the same coherent superposition for every refined outcome, multiplied by $1/\sqrt R$. Its target amplitude is precisely

```math
\sum_q A_{kq}\sqrt{T_{kq}}.
```

After summing the probabilities of all $k$ branches, the fidelity equals (1). The local shifts of the retained systems are $(k,-k)$. Fixed-charge buffers implement them as specified in [model.md](model.md).

The construction has so far been stated on the occupied Schmidt support. Additional input vectors are completed by local channels, with neutral orthogonal flags if useful, and zero shift where a specified shifted destination does not exist. Their joint action on the scored source is zero. Such completion introduces no extra fidelity or uncounted postselection. It can respect the same hard bound on both laboratories.

The objective in (1) is concave: its expansion is a sum of linear terms and nonnegative multiples of $\sqrt{T_{kq}T_{kq'}}$. This fact does not assert efficient physical implementation. The common outcome number can be large.

## Convex dual and its boundary

An exact dual is

```math
[F^\star]^2=
\min_{x_q>0}\left\{\sum_qx_q:
\sum_q\frac{A_{kq}^2}{x_q}\le1
\quad\forall k\in\mathcal K\right\}.
\tag{5}
```

Weighted Cauchy–Schwarz proves every feasible dual upper bound:

```math
\left(\sum_qA_{kq}\sqrt{T_{kq}}\right)^2
\le\left(\sum_q\frac{A_{kq}^2}{x_q}\right)
\left(\sum_qx_qT_{kq}\right).
```

Sum over $k$ and use the column normalization. For equality, form the Lagrangian of (1) with multipliers $x_q$. A row can grow without bound unless

```math
(A_k^\mathsf T z)^2\le\sum_qx_qz_q^2
\quad\text{for all }z_q\ge0.
```

When $x_q>0$, this condition is equivalent to $\sum_qA_{kq}^2/x_q\le1$. If it fails, the nonnegative vector $z_q=A_{kq}/x_q$ is already a violating direction. The simplex constraints have a relative-interior feasible point, and the objective is finite and continuous. Finite-dimensional convex strong duality therefore gives (5).

There is no unresolved zero-denominator convention in the actual catalytic problem. The $k=0$ constraint implies $x_q\ge A_{0q}^2=p_q^2/m>0$ separately for every source column. The choice $x_q=p_q$ is feasible because

```math
\sum_q A_{kq}^2/p_q
=\sum_{q:q+k\in\mathcal Q}
p_{q+k}\min\{1,d_q/(m d_{q+k})\}\le1.
```

An optimizing sequence can thus be restricted to a compact set bounded away from zero, and the minimum is attained. Zero-weight source columns should be deleted before solving the problem. Missing-destination entries have numerator zero and contribute zero. For a more general nonnegative matrix lacking the $k=0$ row, an all-zero column can be removed and assigned dual value zero; that extra convention is not needed here.

## Equivalent optimization over charge shifts

There is a smaller exact program. Let $\lambda$ be a probability distribution on the allowed shifts and define

```math
G(\lambda)=\sum_q z_q(\lambda),\qquad
z_q(\lambda)=\sqrt{\sum_k\lambda_k A_{kq}^2}.
```

Then

```math
F^\star=\max_{\lambda_k\ge0,\ \sum_k\lambda_k=1}G(\lambda).
\tag{6}
```

To prove this, put $u_{kq}=\sqrt{T_{kq}}$. Each source column has Euclidean norm one. The square root of (1) is the norm of the nonnegative vector with components $\sum_qA_{kq}u_{kq}$. Express that norm as a maximum over nonnegative unit vectors $v_k$, interchange the two compact maxima, and maximize each source column separately. Its value is $\sqrt{\sum_kv_k^2A_{kq}^2}$. Setting $\lambda_k=v_k^2$ gives (6). The function $G$ is concave, and the number of variables is the number of allowed shifts.

For any $\lambda$ with every $z_q>0$, define

```math
T_{kq}=\frac{\lambda_k A_{kq}^2}{z_q^2},\qquad
D_k=\sum_q\frac{A_{kq}^2}{z_q},\qquad
D_{\max}=\max_kD_k.
\tag{7}
```

These give an explicit feasible filter and an explicit feasible dual point $x_q=D_{\max}z_q$. Thus

```math
\underbrace{\sum_k\lambda_kD_k^2}_{\text{attained squared fidelity}}
\le [F^\star]^2
\le\underbrace{D_{\max}G(\lambda)}_{\text{dual objective}}.
\tag{8}
```

The identity $\sum_k\lambda_kD_k=G(\lambda)$ is useful for checking the calculation. At a maximizer, the simplex optimality conditions give $D_k=G$ on active shifts and $D_k\le G$ on inactive shifts. Both sides of (8) then equal $G^2$.

At an optimum no $z_q$ can vanish. If one vanished, mixing a small amount of the zero-shift row into $\lambda$ would yield a positive square-root-order gain from that source column, while the loss in columns with positive $z_q$ is only first order. This contradicts maximality. Numerical solvers can nevertheless encounter such boundary points before convergence. The implementation mixes in a small zero-shift component and verifies the resulting bounds instead of trusting a solver termination flag.

## Exact checks and finite certificates

For $S=0$, (1) gives $F^2=1/m$, and $x_q=p_q/m$ is an exact matching dual point. For a fixed shift, the coherent construction gives the lower bound $(\sum_qA_{kq})^2$. Another simple dual uses $a_q=\max_k A_{kq}$ and $x_q=a_q\sum_{q'}a_{q'}$, giving $F^2\le(\sum_q a_q)^2$. These are useful checks independent of the numerical optimizer.

[Verification](../verification/README.md) constructs the actual small Kraus matrices, solves (6), and reports attained primal values and feasible dual values. Rational model inputs and outward-rounded decimal evaluation certify the reported finite lower and upper bounds. Solver accuracy affects the width of the interval, not the validity of its endpoints. Calculations for large hypergeometric models explicitly account for discarded tail weight; they do not stand in for the analytical asymptotic proof.
