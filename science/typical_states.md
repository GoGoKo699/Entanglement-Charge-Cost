# From physical Haar states to flat charge blocks

The operational proofs become transparent when each charge sector is maximally entangled. This page proves that such a comparison is valid for a typical unequal-cut fixed-charge Haar state. It also resolves a dimensional issue: some extreme sectors have fewer Bob dimensions than Alice dimensions, so the untruncated mean marginal cannot always be purified inside the original fixed-charge Hilbert space.

The ensemble and notation are defined in [the model](model.md). The concentration and Gaussian spectral use of this ensemble are established in [ZLC26, Supplemental Sec. III](https://arxiv.org/html/2609.26362v1). The direct moment argument below makes the physical truncation and charge-preserving alignment explicit.

## A window that admits the comparison state

Let $h(x)=-x\ln x-(1-x)\ln(1-x)$. At the mean charge $q=\nu L_A$, Stirling's formula gives

```math
\ln\frac{a_q}{b_q}
=-(1-2f)Lh(\nu)+O(\ln L).
```

Because $f<1/2$ and $0<\nu<1$, the leading coefficient is strictly negative. Choose a fixed sufficiently small $\delta>0$ and define

```math
\mathcal T_L=
\{q:\ |q-\nu L_A|\le\delta L\}
\cap\operatorname{supp}(p).
```

Continuity of the binary entropy gives constants $c_1>0$ and $L_0$ such that $a_q/b_q\le e^{-c_1L}$ for every $q\in\mathcal T_L$ and $L\ge L_0$. The same choice keeps all sectors in this window away from the endpoints of the binomial factors. A hypergeometric large-deviation bound gives

```math
\eta_L:=\sum_{q\notin\mathcal T_L}p_q\le C e^{-c_2 L}
```

for constants $C,c_2>0$. To see the exponential tail directly, put $x=q/L$. The logarithm of $p_q$, divided by $L$, has leading term

```math
g(x)=f h(x/f)+(1-f)h((\nu-x)/(1-f))-h(\nu).
```

This strictly concave function has its unique maximum $g(f\nu)=0$. On the compact physical support outside $|x-f\nu|<\delta$, its maximum is strictly negative. The polynomial factors in the binomial estimates and the at most $L+1$ summands are absorbed by a smaller positive exponential rate. Only exponential decay, not the best exponent, is used here.

Normalize $p_q^{\mathcal T}=p_q/(1-\eta_L)$ on $\mathcal T_L$ and set it to zero elsewhere. Since $b_q\ge a_q$ on this window, a physical reference state exists:

```math
|\Omega_L\rangle
=\sum_{q\in\mathcal T_L}\sqrt{p_q^{\mathcal T}}
|\Phi_{a_q};q,N-q\rangle.
```

Each maximally entangled vector uses $a_q$ orthonormal vectors on each side within the indicated physical sectors. No enlargement of the catalyst's Hilbert space is needed. Its Alice marginal is

```math
\bar\rho_A^{\mathcal T}
=\bigoplus_{q\in\mathcal T_L}\frac{p_q^{\mathcal T}}{a_q}I_{a_q}.
```

The same linear window can be used throughout; narrower central windows are convenient only for the later rank estimates. Any shifts used to attain the capacity are $O(\sqrt L)$, well inside the linear window except on exponentially unlikely boundary sectors.

## Haar moments give an exponentially small marginal error

Write $\rho_{A,q}$ for the unnormalized charge-$q$ block of Alice's reduced state. The mean is

```math
\mathbb E\rho_{A,q}=\frac{b_q}{D}I_{a_q}.
```

The second moment of a Haar vector in the $D$-dimensional fixed-charge subspace is $(I+\mathrm{Swap})/[D(D+1)]$. Contracting its indices within one charge block yields

```math
\mathbb E\operatorname{Tr}\rho_{A,q}^2
=\frac{a_qb_q(a_q+b_q)}{D(D+1)},
```

and consequently

```math
\mathbb E\operatorname{Tr}
\left(\rho_{A,q}-\frac{b_q}{D}I_{a_q}\right)^2
=\frac{a_qb_q(a_qD-b_q)}{D^2(D+1)}
\le\frac{a_q^2b_q}{D(D+1)}.
```

Apply $\|X\|_1\le\sqrt{a_q}\|X\|_2$ and Jensen's inequality:

```math
\mathbb E\left\|\rho_{A,q}-\frac{b_q}{D}I_{a_q}\right\|_1
\le p_q\sqrt{\frac{a_q}{b_q}}.
```

On the complement of $\mathcal T_L$, positivity bounds the expected trace-norm deviation by twice its mean probability. Summing the block norms and then normalizing the retained mean gives

```math
\mathbb E\|\rho_A-\bar\rho_A\|_1
\le e^{-c_1L/2}+2\eta_L,
\qquad
\|\bar\rho_A-\bar\rho_A^{\mathcal T}\|_1=2\eta_L,
```

where $\bar\rho_A=\bigoplus_q(b_q/D)I_{a_q}$. Hence, for some $c,C'>0$ depending only on $f,\nu$,

```math
\mathbb E\|\rho_A-\bar\rho_A^{\mathcal T}\|_1
\le C'e^{-cL}.
```

Markov's inequality makes this a high-probability statement, for example

```math
\Pr\!\left[\|\rho_A-\bar\rho_A^{\mathcal T}\|_1
>e^{-cL/2}\right]\le C'e^{-cL/2}.
```

These estimates include fluctuations of the sector weights as well as the spectra within sectors. A statement about typical block spectra with fixed weights would not by itself supply this conclusion.

## Alignment respects charge

Write a Schmidt decomposition of the actual state separately in each charge sector. In every retained sector replace its Schmidt coefficients by the uniform coefficients of $|\Omega_L\rangle$, using the same Schmidt bases. There is room for all $a_q$ vectors on Bob's side because $b_q\ge a_q$. Then

```math
\langle\psi_L|\Omega_L\rangle
=F(\rho_A,\bar\rho_A^{\mathcal T}).
```

The reference is allowed to depend on the known state. All changes from a fixed canonical choice of these bases are block diagonal in local charge and therefore allowed at zero exchange. This construction is the sectorwise form of purification alignment. An unrestricted Uhlmann unitary mixing different Bob charge sectors would not be an admissible substitute.

The fidelity/trace-distance inequalities imply

```math
P(\psi_L,\Omega_L)^2
\le\|\rho_A-\bar\rho_A^{\mathcal T}\|_1.
```

Thus the purified distance is exponentially small with probability tending to one exponentially fast. This proves a physical flat-block approximation, not merely closeness of two formal lists of eigenvalues.

## Uniform transfer of operational fidelity

Let $\zeta_L=P(\psi_L,\Omega_L)$. For any allowed channel $\Lambda$ and any target dimension $m$, contractivity of purified distance gives

```math
P(\Lambda(\psi_L\otimes00),\Lambda(\Omega_L\otimes00))
\le\zeta_L,
\qquad
P(\psi_L\otimes\Phi_m,\Omega_L\otimes\Phi_m)=\zeta_L.
```

The fidelity angle $\arccos F$ is a metric. Its triangle inequality bounds the change of the angle by $2\arcsin\zeta_L$, and therefore bounds the change of root fidelity by $2\zeta_L$. Taking suprema over the same implementation class on both inputs yields

```math
\left|F_L^\star(m,S;\psi_L)-F_L^\star(m,S;\Omega_L)\right|
\le2\zeta_L.
```

The bound is uniform in $m$ and $S$. Protocols can be optimized for their known input state; no universal decoder is assumed. Free charge-preserving changes of Schmidt bases make the optimum for $\Omega_L$ depend only on its ranks and weights.

The [fixed-budget limit](converse.md) therefore transfers immediately. For the [capacity law](asymptotics.md), first take rates strictly inside or outside the limiting boundary at fixed $\epsilon$. The vanishing fidelity perturbation does not cross the resulting strict margin; continuity in the limiting rate then gives the boundary capacity. This avoids assuming that a finite-size optimizer has a nonzero margin at an exact threshold.

## Dependencies and limits

The required ingredients are the standard Haar second moment, a hypergeometric exponential tail, and fidelity continuity. The failure at $f=1/2$ is concrete: the exponential dimension separation used above disappears. At $\nu=1/2$ the flat approximation remains valid for an unequal cut, but the rank slope $\mu$ vanishes and the stated growing borrowing law no longer supplies a nonzero leading resource.

Return to [the model](model.md), continue to [coherent extraction](coherent_protocol.md), or inspect [the finite optimum](finite_optimization.md).
