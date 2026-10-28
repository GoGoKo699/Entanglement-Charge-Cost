# Related work and the contribution of the charge budget

The quantity studied here is the maximum joint catalyst–target fidelity under
a **hard bound on net local catalyst charge exchange in every complete
charge-resolved branch**. The auxiliary buffers start locally in
charge-incoherent states and need not return to their initial charges.
The target is neutral or encoded at fixed local charge. These choices
distinguish the present question from unrestricted embezzlement, a phase
reference resource, an entanglement battery, and a circuit complexity cost.

The main result is the optimal exchange-budget law for the fixed-charge
many-body family:

```math
F_{\max}^2(m,S)\longrightarrow
\min\{1,e^{|\mu|S}/m\},
\qquad \mu=\ln[(1-\nu)/\nu],
```
for fixed $`S,m`$, together with the leading growing-budget capacity.
The [asymptotic note](../science/asymptotics.md) states the limits and their
precise scope. This document identifies which ingredients are established
results and which operational statement is added here.

<a id="zlc26"></a>

## 1. ZLC26: the same fixed-charge state family and the unrestricted optimum

**Shi-Xin Zhang, Shuo Liu and Yu-Qin Chen,
“Entanglement Embezzlement from Diffusive Hydrodynamics,”
[arXiv:2609.26362v1](https://arxiv.org/html/2609.26362v1),
22 September 2026.**
DOI: [10.48550/arXiv.2609.26362](https://doi.org/10.48550/arXiv.2609.26362).

This is the closest state-family comparator. Its Eqs. (4)–(7) and
Supplemental Sec. III give the unequal-cut fixed-charge Haar spectrum,
typicality reduction, charge-bias slope, and unrestricted Gaussian fidelity
and borrowing yield. The final discussion explicitly leaves charge-respecting
extraction open.

The present result supplies the optimal supported charge exchange and a
matching extraction protocol. The $`\sqrt L`$ resource, its unrestricted
Gaussian coefficient, and its hydrodynamic interpretation are credited to
that work. We prove no dynamical circuit theorem here.

## 2. Superselection rules: shifts and coherent sector conversion

**Norbert Schuch, Frank Verstraete and J. Ignacio Cirac,
“Quantum entanglement theory in the presence of superselection rules,”
Physical Review A 70, 042310 (2004).**
DOI: [10.1103/PhysRevA.70.042310](https://doi.org/10.1103/PhysRevA.70.042310).
Primary preprint inspected:
[quant-ph/0404079v1](https://arxiv.org/pdf/quant-ph/0404079v1),
13 April 2004.

Section II explicitly permits fixed-number ancillas whose removal or
measurement produces definite-number-shift Kraus operators. Section III.A
establishes sectorwise majorization and describes refinement of outcomes
across sectors so that a measurement record need not reveal the sector.
The asymptotic discussion also treats Gaussian charge fluctuations and
shifts of their mean.

Our coherent rank conversion uses these established tools. Their first-order
pure-state conversion theory does not formulate the hard exchange-budget
embezzlement fidelity for the present catalyst. The contribution is the
matching physical cost and converse, rather than a new conversion
instrument or a new version of majorization.

**Gilad Gour and Robert W. Spekkens,
“The resource theory of quantum reference frames: manipulations and
monotones,” New Journal of Physics 10, 033023 (2008).**
DOI: [10.1088/1367-2630/10/3/033023](https://doi.org/10.1088/1367-2630/10/3/033023).
Primary version inspected:
[arXiv:0711.0043v2](https://arxiv.org/pdf/0711.0043v2),
18 March 2008.

Their U(1) theory gives fixed-shift Kraus decompositions, charge-distribution
conversion conditions, and frameness monotones. In particular, Lemma 2 and
the deterministic-conversion discussion make the shift structure standard
symmetry machinery. The present resource is the support of the allowed
shift in each complete branch; it is not a new definition of U(1)
covariance or an externally supplied coherent phase reference.

## 3. Number-conserving Gaussian and critical-fermion embezzlement

**Alessia Kera, Lauritz van Luijk, Alexander Stottmeister and Henrik Wilming,
“Gaussian fermionic embezzlement of entanglement,”
[arXiv:2509.15749v2](https://arxiv.org/html/2509.15749v2),
5 March 2026.**
DOI: [10.48550/arXiv.2509.15749](https://doi.org/10.48550/arXiv.2509.15749).
The original preprint appeared on 19 September 2025.

The passive Gaussian setting in Secs. 2–3 uses local Gaussian unitaries
that conserve the combined particle number of catalyst and target in each
laboratory. Theorem 1 provides an approximate-embezzlement criterion based
on a dense one-particle covariance spectrum. Section 4.2 explicitly explains
how a broad number distribution can hide a finite change in its mean.

Thus number-conserving embezzlement, and the compatibility of broad
charge distributions with finite shifts, are established phenomena.
The typical Haar marginal considered here has approximately constant
one-particle covariance $`\nu I`$, so its mechanism is not an application
of the dense-covariance criterion. The question here is an optimal hard
charge budget for the full many-body spectrum.

Their Sec. 4.1 extension to arbitrary target states allows general
non-Gaussian unitaries and explicitly discusses parity encoding. We do not
reinterpret that paragraph as a theorem for every neutral-target U(1)
protocol under the budget imposed here.

**Lauritz van Luijk, Alexander Stottmeister and Henrik Wilming,
“Critical fermions are universal embezzlers,”
Nature Physics 21, 1141–1146 (2025).**
DOI: [10.1038/s41567-025-02921-w](https://doi.org/10.1038/s41567-025-02921-w).
Published 27 May 2025.
Primary preprint inspected:
[arXiv:2406.11747v2](https://arxiv.org/html/2406.11747v2),
2 August 2024.

This work establishes universal embezzlement in natural critical
free-fermion ground-state families, with a treatment of fermion parity.
It already supplies the many-body existence phenomenon. Our fixed-charge
Haar family, local U(1) exchange budget, and finite-budget fidelity question
are different; we make no claim to introduce natural many-body embezzlers.

## 4. Entanglement batteries and the role of the local charge buffers

**Álvaro M. Alhambra, Lluis Masanes, Jonathan Oppenheim and Christopher Perry,
“Entanglement fluctuation theorems,”
Physical Review A 100, 012317 (2019).**
DOI: [10.1103/PhysRevA.100.012317](https://doi.org/10.1103/PhysRevA.100.012317).
Primary version inspected:
[arXiv:1709.06139v2](https://arxiv.org/pdf/1709.06139v2),
19 July 2019.

Their battery stores entanglement in a coherent collection of levels with
different numbers of ebits. Translations of this battery permit coherent
entanglement exchange and lead to exact fluctuation constraints for pure-state
transformations.

There is a useful structural analogy with coherent shifts of a broad
distribution. The charged auxiliary buffers here are, however, local product
states of definite particle number. They supply charge capacity, while the
entanglement is borrowed from the specified many-body catalyst. Their final
charges change. This does not amount to returning all auxiliary resources
unchanged, nor to supplying an entanglement battery for free.

## 5. Circuit complexity is a separate physical cost

**Tal Schwartzman, “Complexity of entanglement embezzlement,”
Physical Review A 112, 012415 (2025).**
DOI: [10.1103/pfyl-hwf2](https://doi.org/10.1103/pfyl-hwf2).
Published 15 July 2025.
Primary preprint inspected:
[arXiv:2410.19051v2](https://arxiv.org/abs/2410.19051v2),
20 April 2025, titled “The complexity of entanglement embezzlement.”

This work derives circuit complexity lower bounds that grow with accuracy
and borrowed entanglement, including a critical-system example.
The present protocol may use a very large outcome alphabet and large local
operations. We bound charge exchange, not its gate count, execution time,
spatial locality, or learning cost. The charge-budget theorem therefore
does not establish an efficient extraction procedure.

## 6. General embezzlement and the fidelity framework

The original phenomenon is due to Wim van Dam and Patrick Hayden,
“Universal entanglement transformations without communication,”
Physical Review A 67, 060302(R) (2003),
DOI [10.1103/PhysRevA.67.060302](https://doi.org/10.1103/PhysRevA.67.060302).
The primary preprint is
[quant-ph/0201041v1](https://arxiv.org/abs/quant-ph/0201041v1),
10 January 2002, under the title “Embezzling Entangled Quantum States.”

Elia Zanoni, Thomas Theurer and Gilad Gour,
“Complete Characterization of Entanglement Embezzlement,”
[Quantum 8, 1368 (2024)](https://quantum-journal.org/papers/q-2024-06-13-1368/),
DOI [10.22331/q-2024-06-13-1368](https://doi.org/10.22331/q-2024-06-13-1368),
characterize unrestricted universal embezzling families and pure-to-mixed
LOCC conversion. The publisher identifies arXiv:2303.17749v3 as the
associated preprint. These unrestricted characterizations do not charge
the physical U(1) shift budget introduced here.

The conversion arguments rest on M. A. Nielsen's majorization theorem,
“Conditions for a class of entanglement transformations,”
Physical Review Letters 83, 436–439 (1999),
DOI [10.1103/PhysRevLett.83.436](https://doi.org/10.1103/PhysRevLett.83.436),
and the approximate-conversion theory of Guifré Vidal, Daniel Jonathan and
M. A. Nielsen, “Approximate transformations and robust manipulation of
bipartite pure-state entanglement,” Physical Review A 62, 012304 (2000),
DOI [10.1103/PhysRevA.62.012304](https://doi.org/10.1103/PhysRevA.62.012304).
The latter's Sec. III includes general mixed outputs. A short
ensemble-majorization proof in the asymptotic note explains why the
unrestricted Gaussian upper bound applies to them. That reduction is used
as an upper relaxation, without claiming that it preserves a charge budget.

## 7. Precise contribution statement

The result adds an optimal operational charge cost for a specified
many-body catalyst. It identifies the fidelity obtainable at a fixed
integer exchange budget and the leading yield when the budget grows.
The converse permits arbitrary adaptive protocols in the stated instrument
model; the construction uses fixed-charge buffers and synchronizes the
classical outcomes so that the record does not reveal the catalyst charge.

The Gaussian envelope, generic symmetry-respecting instruments, coherence
preservation by outcome refinement, and generic number-conserving
embezzlement are established ingredients. No claim is made for an
expected-charge budget, exactly returned buffers, unrestricted charged
targets, or efficient implementation.

Bibliographic entries, including the versions actually used, are in
[references.bib](references.bib). Metadata were checked against the linked
primary preprints and publisher records on 28 October 2026.
