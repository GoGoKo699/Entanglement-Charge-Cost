# Uniform charge shifts and the asymptotic borrowing capacity

This note proves the charge-distribution and rank estimates used by the
[coherent protocol](coherent_protocol.md) and combines them with the
[all-protocol converse](converse.md). The unrestricted Gaussian upper bound is
an input from Zhang, Liu and Chen,
[arXiv:2609.26362v1](https://arxiv.org/html/2609.26362v1), Eqs. (6)–(7) and
Supplemental Secs. II–III. Its coefficient is not a new result here.

## 1. Definitions and limiting conventions

Fix $0<f<1/2$, $0<\nu<1$, and $\nu\ne1/2$. The model uses
integer-compatible sequences $n_L=fL$, $N_L=\nu L$.
The proof also covers the optional rounded extension
$n_L=\lfloor fL\rfloor$, $N_L=\lfloor\nu L\rfloor$.
Keeping $\nu_L=N_L/L$ throughout treats both conventions. Define

```math
a_{L,q}=\binom{n_L}{q},\qquad
p_{L,q}=
\frac{\binom{n_L}{q}\binom{L-n_L}{N_L-q}}{\binom{L}{N_L}},
\tag{1}
```

with $p_{L,q}=0$ outside its hypergeometric support, and

```math
\begin{split}
\bar q_L&=n_L\nu_L,\\
\sigma_L^2
&=n_L\nu_L(1-\nu_L)\frac{L-n_L}{L-1}
=vL+O(1),\\
v&=f(1-f)\nu(1-\nu),\\
\mu_L&=\ln\frac{1-\nu_L}{\nu_L},\qquad
\mu=\ln\frac{1-\nu}{\nu},\qquad \gamma=|\mu|>0.
\end{split}
\tag{2}
```

The shift convention is $k=q_{\mathrm{out}}-q_{\mathrm{in}}$. A favorable
shift of magnitude $s$ has $k=-\operatorname{sgn}(\mu)s$. Particle-hole
conjugation reduces proofs of achievability to $\mu>0$.

The coherent ideal catalyst is formed from maximally entangled charge blocks
with ranks $a_{L,q}$ and weights $p_{L,q}$. As explained in
[typical states](typical_states.md), it is normalized on a fixed linear
window about $\bar q_L$, where Bob's sector dimension exceeds $a_{L,q}$.
The excluded mass is exponentially small. All estimates below first use the
full hypergeometric distribution; this truncation changes the relevant root
overlaps by $o(1)$. For $O(\sqrt L)$ shifts, every smaller window used
below and its translate lie inside the physical linear window.

Write $F_L(m,S)$ for the supremum root fidelity with the joint
catalyst–$\Phi_m$ target under the hard branchwise net-exchange budget $S$.
The output may be mixed, and every outcome is included. For fixed
$0<\epsilon<1$, set

```math
B_{\epsilon,L}(S)=
\sup\{\log_2m:m\in\mathbb N,\ F_L(m,S)^2\ge1-\epsilon^2\}.
\tag{3}
```

Limits for the ideal comparison family are deterministic. Through the
charge-preserving typicality transfer, the same limits for a Haar random
fixed-charge catalyst hold in probability. The protocol may depend on the
known catalyst. No circuit complexity bound is imposed.

## 2. Uniform binomial rank ratios

**Lemma 1.** If $w_L+K_L=o(L)$, then uniformly for
$|q-\bar q_L|\le w_L$ and integer $|k|\le K_L$,

```math
\ln\frac{a_{L,q}}{a_{L,q+k}}
=-\mu_L k+
O\!\left(
\frac{|k|(|q-\bar q_L|+|k|+1)}{L}
\right).
\tag{4}
```

The constant is uniform once $f,\nu$ are fixed in the stated open ranges.

**Proof.** For an integer $u$ in these interior windows,

```math
\ln a_{L,u+1}-\ln a_{L,u}
=\ln\frac{n_L-u}{u+1}
=\mu_L+
O\!\left(\frac{|u-\bar q_L|+1}{L}\right).
```

Sum this identity over the $|k|$ adjacent steps from $q$ to $q+k$,
reversing its sign for $k<0$. This proves (4). In particular no asymptotic
approximation to a factorial is needed for this lemma. $\square$

Two choices of window will be useful.

1. If $K_L\le C\sqrt L$, take $w_L=\sqrt L\log L$. The error in (4) is
   $O_C(\log L)$, while the omitted mass is $o(1)$, for example by
   Chebyshev's inequality.
2. If $S_L=o(\sqrt L)$, take $w_L=M_L\sqrt L$, where
   $M_L\to\infty$, $M_L=o(\sqrt L)$, and
   $S_LM_L/\sqrt L\to0$. One explicit choice is
   ```math
   M_L=\min\left\{L^{1/8},
   \left(\frac{\sqrt L}{S_L+1}\right)^{1/2}\right\}.
   ```
   The error is then $o(1)$, uniformly over every $|k|\le S_L$.
   The omitted mass is $O(M_L^{-2})=o(1)$.

Since $\mu_L-\mu=O(L^{-1})$, $\mu_L$ can be replaced by $\mu$ in
these uniform statements without changing their respective error orders.

## 3. A uniform hypergeometric shift-overlap limit

Define the root overlap between the charge law and its integer translate by

```math
H_L(s)=\sum_{q\in\mathbb Z}\sqrt{p_{L,q}p_{L,q-s}}.
\tag{5}
```

**Lemma 2.** Uniformly over all integer shifts,

```math
\sup_{s\in\mathbb Z}
\left|H_L(s)-
\exp\!\left[-\frac{s^2}{8\sigma_L^2}\right]\right|
\longrightarrow0.
\tag{6}
```

This is an absolute-error statement. It does not assert a relative error
estimate when either overlap is exponentially small.

**Proof.** Introduce the histogram density

```math
f_L(x)=\sigma_Lp_{L,q}
\quad\text{for}\quad
x\in
\left[\frac{q-\bar q_L}{\sigma_L},
\frac{q+1-\bar q_L}{\sigma_L}\right).
\tag{7}
```

It integrates to one. The usual central expansion follows directly by
applying Stirling's formula to the three binomial coefficients in (1):
for each fixed $R<\infty$, uniformly on $|x|\le R$,
$\sigma_L p_{L,\lfloor\bar q_L+\sigma_Lx\rfloor}\to\phi(x)$,
where $\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}$. The quadratic term is
$-(q-\bar q_L)^2/(2\sigma_L^2)$; the cubic remainder is
$O_R(L^{-1/2})$, and the prefactor is
$(2\pi\sigma_L^2)^{-1/2}(1+o(1))$.

Consequently $f_L\to\phi$ in $L^1(\mathbb R)$. This follows either from
the compact convergence and the variance bound on the remaining tails, or
from Scheffé's lemma, since both are probability densities. Thus

```math
d_L:=\|\sqrt{f_L}-\sqrt\phi\|_2\longrightarrow0,
\qquad d_L^2\le\|f_L-\phi\|_1.
\tag{8}
```

For $h=s/\sigma_L$, the cells in (7) align exactly after translation, so

```math
H_L(s)=\langle\sqrt{f_L},T_h\sqrt{f_L}\rangle,
\qquad (T_hg)(x)=g(x-h).
```

Translation is an $L^2$ isometry. Cauchy-Schwarz therefore gives, for every
real $h$,

```math
\left|
\langle\sqrt{f_L},T_h\sqrt{f_L}\rangle
-\langle\sqrt\phi,T_h\sqrt\phi\rangle
\right|\le2d_L.
```

The Gaussian inner product equals $e^{-h^2/8}$, proving the asserted
uniformity. $\square$

In particular, $s_L=o(\sqrt L)$ implies $H_L(s_L)\to1$, while
$s_L/\sqrt L\to t$ gives $H_L(s_L)\to e^{-t^2/(8v)}$.
Removing source or target sectors of total mass $\eta_L$ changes the
overlap sum by at most $2\sqrt{\eta_L}$, before an additional vanishing
normalization correction.

## 4. The unrestricted bound includes mixed outputs

The unrestricted benchmark used here is

```math
\ln m_L/\sqrt L\to b\ge0
\quad\Longrightarrow\quad
F_L^{\mathrm{unres}}(m_L)
\longrightarrow
\exp\!\left[-\frac{b^2}{8\gamma^2v}\right].
\tag{9}
```

This is the Gaussian conversion law of
[Zhang, Liu and Chen](https://arxiv.org/html/2609.26362v1), applied to the
present mean spectrum and then to typical fixed-charge states. Their
definition already optimizes over the complete LOCC output. For clarity,
the reduction to a pure output has the following standard proof, consistent
with [Vidal, Jonathan and Nielsen, Sec. III](https://arxiv.org/pdf/quant-ph/9910099v2).

Let $\lambda$ and $v$ be the sorted Schmidt probability vectors of a
pure source and a pure target, in a common padded dimension. Refine an LOCC
output into a pure ensemble $\{w_r,|\chi_r\rangle\}$, with sorted Schmidt
vectors $r^{(r)}$. Ensemble majorization gives
$\lambda\prec\bar r:=\sum_rw_rr^{(r)}$. The vector $\bar r$ is sorted,
and Nielsen's theorem makes it deterministically reachable.
For each branch, Schmidt-basis alignment bounds its squared target overlap by

```math
g(r)=\left(\sum_i\sqrt{v_ir_i}\right)^2.
```

The function $g$ is concave: after expanding the square, its off-diagonal
terms are positive multiples of the concave geometric means
$\sqrt{r_ir_j}$. Thus

```math
\sum_rw_r|\langle\mathrm{target}|\chi_r\rangle|^2
\le\sum_rw_rg(r^{(r)})\le g(\bar r).
\tag{10}
```

The last value is attainable by a deterministically reachable pure state
aligned with the target. Refining discarded local systems gives the same
argument for mixed outputs and arbitrarily many classical outcomes.
Taking limits also covers the closure of finite-round LOCC.

This is only a justification of the **unrestricted upper bound**. We do not
assert that the replacing pure-state protocol obeys a prescribed charge
budget.

Fidelity is nonincreasing with target dimension $m$: a maximally entangled
state of rank $m$ can be converted deterministically to one of any smaller
rank by operations on the neutral target registers, without changing the
catalyst budget. Equation (9) and this monotonicity also bound dimensions
whose logarithms grow faster than $\sqrt L$.

## 5. Capacity for all $\sqrt L$-scaled budget sequences

Put

```math
t_\epsilon=2\sqrt{-\ln(1-\epsilon^2)}.
\tag{11}
```

**Theorem 3.** For any integer budgets $S_L\ge0$ such that
$S_L/\sqrt L\to\alpha\in[0,\infty]$,

```math
\lim_{L\to\infty}\frac{B_{\epsilon,L}(S_L)}{\sqrt L}
=
\frac{\gamma}{\ln2}
\min\{\alpha,\sqrt v\,t_\epsilon\}.
\tag{12}
```

Equivalently, along each such sequence,

```math
B_{\epsilon,L}(S_L)
=\frac{\gamma}{\ln2}
\min\{S_L,\sigma_Lt_\epsilon\}+o(\sqrt L).
\tag{13}
```

For Haar catalysts the displayed convergence is in probability and the
remainder is $o_{\mathbb P}(\sqrt L)$.

### Upper bound

First suppose $\alpha<\infty$, so $S_L\le C\sqrt L$ eventually.
On the window $|q-\bar q_L|\le\sqrt L\log L$, Lemma 1 gives

```math
\sup_{|k|\le S_L}
\ln\frac{a_{L,q}}{a_{L,q+k}}
\le\gamma S_L+O_C(\log L).
\tag{14}
```

The rank-overlap bound in [the converse](converse.md), summed over all
charge-resolved leaves, yields

```math
F_L(m,S_L)\le
\sqrt{\min\{1,e^{\gamma S_L+O_C(\log L)}/m\}}+o(1).
\tag{15}
```

The last term includes the norm of the excluded input tail and does not
depend on the number of Kraus leaves. If
$\ln m_L\ge b\sqrt L$ with $b>\gamma\alpha$, the first term tends to
zero. Hence
$\limsup B_{\epsilon,L}(S_L)/\sqrt L\le\gamma\alpha/\ln2$.
This argument includes $\alpha=0$.

Independently, take any $b>\gamma\sqrt v\,t_\epsilon$. The right-hand side
of (9), squared, is strictly below $1-\epsilon^2$. By monotonicity in
$m$, all targets with $\ln m\ge b\sqrt L$ are therefore excluded
eventually. This gives the fluctuation upper bound for every $\alpha$,
including $\alpha=\infty$. Taking the smaller bound proves the limsup
part of (12).

### Lower bound and an explicit rank slack

If $\alpha=0$, the lower bound in (12) follows from $m=1$.
Otherwise, fix any

```math
0<b<\gamma\min\{\alpha,\sqrt v\,t_\epsilon\}.
\tag{16}
```

Choose $m_L=\lfloor e^{b\sqrt L}\rfloor$ and, after particle-hole
conjugation if needed, set

```math
s_L=
\left\lceil
\frac{\ln m_L}{|\mu_L|}+(\log L)^2
\right\rceil.
\tag{17}
```

The slack diverges and is $o(\sqrt L)$.
Since $s_L/\sqrt L\to b/\gamma<\alpha$, it respects $s_L\le S_L$
for all sufficiently large $L$. On
$|q-\bar q_L|\le\sqrt L\log L$, its rank surplus satisfies

```math
\ln\frac{a_{L,q}}
{m_La_{L,q-\operatorname{sgn}(\mu)s_L}}
\ge |\mu_L|(\log L)^2-O(\log L)
\longrightarrow+\infty.
\tag{18}
```

All these sectors therefore admit exact rank reduction to the desired
shifted catalyst block tensor $\Phi_{m_L}$. The coherent protocol has
root overlap at least the charge overlap on this window; its omitted
contribution vanishes. Lemma 2 gives

```math
\liminf F_L(m_L,S_L)
\ge\exp\!\left[-\frac{b^2}{8\gamma^2v}\right]
>\sqrt{1-\epsilon^2}.
\tag{19}
```

Thus $m_L$ is feasible eventually. Letting $b$ approach the right
endpoint of (16) proves the liminf part.

The proof deliberately approaches the boundary through strict inequalities.
It makes no claim that choosing exactly the Gaussian threshold at finite
$L$, or adding a specified constant to it, is feasible. A subleading
boundary expansion would require further estimates.

## 6. Fixed budgets and budgets smaller than $\sqrt L$

The $\alpha=0$ case of (12) only states that the yield is
$o(\sqrt L)$. It does not describe its smaller scale.

The sharper transition in [the converse](converse.md), together with the
hybrid rank-reduction/embedding protocol, says that for
$S_L=o(\sqrt L)$ and integer $m_L$ with

```math
\ln m_L-\gamma S_L\longrightarrow c\in\mathbb R,
```

one has

```math
F_L(m_L,S_L)^2\longrightarrow \min\{1,e^{-c}\}.
\tag{20}
```

Lemma 1 with the adaptive $M_L$ window gives the uniformly accurate rank
factor, and Lemma 2 gives $H_L(S_L)\to1$. For fixed $S,m$, (20) is

```math
F_L(m,S)^2\longrightarrow
\min\{1,e^{\gamma S}/m\}.
\tag{21}
```

For an exactly charge-block-flat catalyst at $S=0$, the identity
$F_L(m,0)^2=1/m$ holds before taking the limit. For a typical Haar
catalyst it is a limiting identity.

If $S_L\to\infty$ while $S_L=o(\sqrt L)$, then for every fixed
$0<\epsilon<1$,

```math
\frac{B_{\epsilon,L}(S_L)}{S_L}
\longrightarrow\frac{\gamma}{\ln2}.
\tag{22}
```

Indeed, a favorable shift $s_L=S_L$ and
$\ln m_L=(\gamma-\delta)S_L+o(1)$ give fidelity tending to one for
every $0<\delta<\gamma$. The all-leaf upper bound excludes
$\ln m_L\ge(\gamma+\delta)S_L$, with fidelity tending to zero.
The adaptive window makes the rank error $o(1)$, even when $S_L$
diverges more slowly than $(\log L)^2$; no fixed slack of that size is
used in this regime.

At a fixed integer budget, target dimensions remain discrete. A limiting
fidelity exactly equal to $1-\epsilon^2$ does not alone decide eventual
finite-$L$ feasibility. Equations (20)–(21) state fidelity limits rather
than silently imposing a rounding rule at such equalities.

## 7. What the theorem does not assume

The budget counts the supported **net** catalyst charge change of each
complete charge-resolved branch. It is not an average-cost constraint or a
bound on intermediate charge excursion. Local buffers change their final
definite charges and are not returned unchanged. The target is neutral or
encoded at fixed local charge, and no coherent phase reference is supplied.
The result concerns known states and permits large local operations and
classical outcome alphabets. Equal cuts, half filling, efficient gate
compilation, and a dynamical random-circuit theorem are separate questions.
