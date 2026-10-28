# Thirty milestones for understanding entanglement charge cost

This map follows the scientific question: how much local charge exchange is needed to borrow a neutral entangled target while returning a known many-body catalyst? Its thirty understanding targets connect the physical task, an exact finite optimization, and the limiting laws for typical fixed-charge states.

The single educational anchor is John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/) (2018). The [Watrous bridge](WATROUS_BRIDGE.md) selects the relevant foundations, translates conventions, and develops the additional charge-specific steps. Chapter links and section numbers below refer to the author-hosted draft linked from the book's page. The book supplies the foundations; the linked scientific pages supply the model, constructions, proofs, and research attribution particular to this project.

## How the map is organized

**Background and preliminaries, M01–M12**, assemble three kinds of preparation: finite-dimensional quantum information, operations constrained by charge, and probability and optimization tools. The phase ends by putting those ingredients into one operational problem. **Narrative and innovation, M13–M30**, move from the physical flat-sector comparison through coherent extraction and optimality to the fixed-budget and growing-budget laws. This allocation gives the operational construction and its converse their own connected route, while keeping the Haar approximation and numerical certificates distinct from the results they support.

Dependencies identify earlier milestones whose ideas a target uses. They describe the logical structure of the science. The map covers the project's global meaning and its load-bearing arguments; the canonical scientific pages retain the full technical details.

| Milestones | Place in the story |
|---|---|
| M01–M05 | States, entanglement, operations, and joint return accuracy. |
| M06–M08 | Charge sectors, physical instruments, and the exchange budget. |
| M09–M12 | Random fixed-charge states, limiting statements, certificates, and the complete task. |
| M13–M15 | A physical flat-sector reference and transfer back to a typical Haar catalyst. |
| M16–M20 | Coherent implementation and a bound on every complete protocol. |
| M21–M23 | Exact finite optimization and independently checkable numerical witnesses. |
| M24–M28 | Rank slopes, charge-distribution overlap, and the limiting borrowing laws. |
| M29–M30 | Physical meaning, attribution, evidence, and the complete proof route. |

## Phase I: background and preliminaries

<a id="m01"></a>

### M01. States, partitions, and reduced descriptions

**Central question.** What information is retained when a shared quantum state is described from only one laboratory?

**Understanding target.** Explain pure and mixed states, the Alice–Bob tensor-product split, and partial trace. Distinguish a coherent global state from its reduced local density operator.

**Dependencies and story role.** None within the map. This establishes the objects on which every later operation and accuracy statement acts.

**Conceptual connection.** A local marginal can be block diagonal in charge even when the global catalyst contains coherence between different local charges. The global state therefore matters to its return criterion.

**Sources.** Watrous [§2.1.3, reductions and purifications](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [physical systems and return criterion](../science/model.md#physical-systems-and-the-return-criterion).

<a id="m02"></a>

### M02. Schmidt rank and an entangled target

**Central question.** What does a maximally entangled target of dimension $`m`$ require from its source?

**Understanding target.** Relate the Schmidt coefficients of a pure bipartite state to its reduced spectrum. Explain Schmidt rank, the vector $`\Phi_m`$, and why tensoring a rank-$`d`$ flat catalyst block with that target requires rank $`md`$.

**Dependencies and story role.** [M01](#m01). This gives a concrete measure of the dimensions involved in extraction.

**Conceptual connection.** The later charge cost arises because changing charge changes the rank of the catalyst block that must be returned.

**Sources.** Watrous [§1.1.3, operator decompositions and norms](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), and [§6.2.1, entanglement transformation](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [physical block states and target coordinates](../science/coherent_protocol.md#1-physical-block-states-and-target-coordinates).

<a id="m03"></a>

### M03. Channels, instruments, and complete outcomes

**Central question.** How does an operation with a classical outcome act on the quantum state when all outcomes are retained?

**Understanding target.** Read Kraus completeness as trace preservation. Explain subnormalized branch vectors, probabilities, and the output obtained after a classical record or environment is discarded.

**Dependencies and story role.** [M01](#m01). This supplies the language needed to distinguish a physical channel from an incomplete successful branch.

**Conceptual connection.** An overlap computed after conditioning must be combined with its outcome probability before it contributes to the project's unconditional fidelity.

**Sources.** Watrous [§§2.2.1–2.2.2, quantum channels, and §2.3, measurements](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [complete charge-resolved leaves](../science/converse.md#1-complete-charge-resolved-leaves).

<a id="m04"></a>

### M04. Local conversion and majorization

**Central question.** Which entanglement transformations can local operations and classical communication perform?

**Understanding target.** Explain why a complete LOCC branch has a product Kraus operator and cannot increase the Schmidt rank of a pure input. Relate deterministic conversion between flat ranks to majorization. Recognize that a product-Kraus upper bound does not by itself construct an LOCC implementation.

**Dependencies and story role.** [M02](#m02), [M03](#m03). This separates the tools for proving attainability from those for ruling out better protocols.

**Conceptual connection.** The project uses local rank conversion inside each charge sector and product-branch rank bounds in its converse.

**Sources.** Watrous [§4.3.1, majorization of real vectors](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf), and [§§6.1.2 and 6.2.1, LOCC and entanglement transformation](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [rank reduction in one sector](../science/coherent_protocol.md#rank-reduction-in-one-sector).

<a id="m05"></a>

### M05. Borrowing requires joint return accuracy

**Central question.** What makes extraction catalytic when the output may be imperfect or correlated?

**Understanding target.** Use root fidelity $`F`$, squared fidelity $`F^2`$, and purified distance $`P=\sqrt{1-F^2}`$ consistently. Explain why the reference is the product of the original catalyst and the desired target, and why returning only the catalyst marginal would leave part of the task unchecked.

**Dependencies and story role.** [M01](#m01), [M02](#m02), [M03](#m03). This fixes the accuracy convention before discussing resources.

**Conceptual connection.** Catalyst disturbance, target error, correlations, and failure probabilities enter a single comparison with a pure product reference.

**Sources.** Watrous [§3.2, fidelity](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [physical systems and return criterion](../science/model.md#physical-systems-and-the-return-criterion), and [fidelity and capacity](../science/model.md#fidelity-and-capacity).

<a id="m06"></a>

### M06. Charge sectors and global coherence

**Central question.** How can a state have fixed total charge while coherently involving several local charges?

**Understanding target.** Read the direct-sum decomposition into Alice charge $`q`$ and Bob charge $`N-q`$. Distinguish a coherent sum of paired sectors from a classical mixture of the same sector weights, and explain how an outcome record can distinguish those sectors.

**Dependencies and story role.** [M01](#m01), [M02](#m02), [M03](#m03). This introduces the physical structure that ordinary sector-by-sector conversion must preserve.

**Conceptual connection.** A protocol can transform every individual sector correctly yet disturb their superposition if its records reveal the sector label.

**Sources.** Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) supplies the reduced-state framework; [physical block states](../science/coherent_protocol.md#1-physical-block-states-and-target-coordinates) supplies the charge decomposition.

<a id="m07"></a>

### M07. Definite charge modes and physical dilations

**Central question.** How can a charge-conserving laboratory change its retained catalyst charge?

**Understanding target.** Interpret a definite-mode Kraus operator as shifting retained charge by one specified integer. Explain how the opposite buffer shift preserves total local charge, and how resolving an environment in charge sectors supplies complete definite-mode leaves.

**Dependencies and story role.** [M03](#m03), [M06](#m06). This connects the operational notation to a physical implementation.

**Conceptual connection.** Local charge-incoherent ancillas allow fixed shifts without supplying a coherent phase reference. The specified instrument model carries more information than covariance of an average bipartite channel alone.

**Sources.** Watrous [§2.2.2, channel representations](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [allowed operations](../science/model.md#allowed-operations-and-the-hard-budget), and [charge-conserving dilations](../science/coherent_protocol.md#3-charge-conserving-dilations-and-net-exchange).

<a id="m08"></a>

### M08. The resource ledger and the hard budget

**Central question.** What is charged to the protocol, and which systems must be returned?

**Understanding target.** State that $`S`$ bounds the absolute net catalyst shift of every complete charge-resolved leaf. Identify the neutral target, initially unentangled local buffers, unrestricted neutral workspace, known catalyst description, and classical communication. Explain that buffers may finish with changed charges.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M05](#m05), [M07](#m07). This assembles the resources into a testable operational contract.

**Conceptual connection.** Net supported exchange, expected exchange, intermediate traffic, reservoir capacity, and circuit complexity answer different resource questions.

**Sources.** Watrous [§6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) supplies the LOCC background; [allowed operations and hard budget](../science/model.md#allowed-operations-and-the-hard-budget), and [resource accounting](../science/interpretation.md#resource-accounting) define this project's cost.

<a id="m09"></a>

### M09. The fixed-charge Haar ensemble

**Central question.** What does a typical catalyst mean in this many-body setting?

**Understanding target.** Explain uniform sampling within the total-charge-$`N`$ subspace, sector dimensions $`a_q,b_q`$, and hypergeometric mean weights $`p_q=a_qb_q/\binom LN`$. Identify the physical support and the unequal-cut condition $`0<f<1/2`$.

**Dependencies and story role.** [M01](#m01), [M02](#m02), [M06](#m06). This connects the operational problem to a concrete state family.

**Conceptual connection.** The sector weights determine how a charge shift affects return accuracy, while the sector dimensions determine how much target rank it can supply.

**Sources.** Watrous [§7.2.1, uniform spherical and Haar measures](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf); [fidelity and capacity](../science/model.md#fidelity-and-capacity), and [typical-state comparison](../science/typical_states.md).

<a id="m10"></a>

### M10. Finite statements and limiting statements

**Central question.** What must an approximation control before it can support a capacity claim?

**Understanding target.** Distinguish an exact finite identity, a deterministic limit for comparison states, and convergence in probability for Haar states. Explain why uniform bounds are needed when shifts and target dimensions vary, and why a small omitted probability produces a square-root contribution to a state-vector norm.

**Dependencies and story role.** [M05](#m05), [M09](#m09). This prepares the logical use of approximation without presuming a finite-size equality.

**Conceptual connection.** Fixed exchange and exchange on the $`\sqrt L`$ fluctuation scale need different error estimates.

**Sources.** Watrous [§1.2.2, probability theory](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [definitions and limiting conventions](../science/asymptotics.md#1-definitions-and-limiting-conventions), and [uniform transfer of operational fidelity](../science/typical_states.md#uniform-transfer-of-operational-fidelity).

<a id="m11"></a>

### M11. Optimization and certificates

**Central question.** How can a computation certify an optimum rather than merely suggest a value?

**Understanding target.** Explain feasible points, objective values, concavity, and dual upper bounds. Distinguish an attainable lower bound from a constraint-verified upper bound, and explain what their gap establishes.

**Dependencies and story role.** [M03](#m03), [M05](#m05). This supplies the language for the finite characterization and its numerical evidence.

**Conceptual connection.** A feasible filter corresponds to an actual protocol; a feasible dual point constrains every allowed protocol. Solver termination alone supplies neither physical interpretation nor a valid bound.

**Sources.** Watrous [§1.2.1, convexity, and §1.2.3, semidefinite programming](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) supply optimization background; [finite primal and dual](../science/finite_optimization.md) give the project's particular concave program.

<a id="m12"></a>

### M12. Assemble the complete borrowing problem

**Central question.** How do the state, operations, resource constraint, and accuracy criterion define one optimization problem?

**Understanding target.** State the task in one connected account: a known pure catalyst, a neutral product target input, charge-respecting LOCC with hard budget $`S`$, and joint output fidelity. Explain how maximizing $`F^\star(m,S)`$ differs from maximizing target size at fixed error, and distinguish a finite flat catalyst from a typical Haar catalyst.

**Dependencies and story role.** [M04](#m04), [M05](#m05), [M08](#m08), [M09](#m09), [M10](#m10), [M11](#m11). This integrates the background phase.

**Conceptual connection.** An operational theorem needs both a physical attaining construction and a bound over the same implementation class.

**Sources.** Watrous [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) and [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [model and exact claims](../science/model.md), with the [notation bridge](WATROUS_BRIDGE.md).

## Phase II: narrative and innovation

<a id="m13"></a>

### M13. Make the flat comparison state physical

**Central question.** When does a proposed flat marginal have a purification inside the actual catalyst Hilbert space?

**Understanding target.** Explain why an Alice block of rank $`a_q`$ requires at least $`a_q`$ Bob dimensions. Identify why extreme sectors can violate this condition, and how a fixed linear window around the mean retains exponentially high weight while satisfying $`b_q\ge a_q`$.

**Dependencies and story role.** [M02](#m02), [M09](#m09), [M10](#m10), [M12](#m12). This constructs a legitimate reference before using its spectrum.

**Conceptual connection.** A close formal eigenvalue list is insufficient if its purification requires undeclared Hilbert-space resources.

**Sources.** Watrous [§2.1.3, purifications](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [a window that admits the comparison state](../science/typical_states.md#a-window-that-admits-the-comparison-state).

<a id="m14"></a>

### M14. Control the whole random marginal

**Central question.** Why is a typical unequal-cut Haar catalyst close to the physical flat reference?

**Understanding target.** Explain the roles of the Haar second moment, the trace-norm bound within each sector, and the exponentially small tail. Identify that both random sector weights and the spectra inside the sectors are controlled.

**Dependencies and story role.** [M01](#m01), [M09](#m09), [M10](#m10), [M13](#m13). This turns the reference into a high-probability approximation to the actual ensemble.

**Conceptual connection.** The unequal cut creates an exponential local dimension separation, which makes marginal fluctuations small enough to transfer operational claims.

**Sources.** Watrous [§§7.2.1–7.2.2, Haar measures and applications](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf); [Haar moments and marginal error](../science/typical_states.md#haar-moments-give-an-exponentially-small-marginal-error).

<a id="m15"></a>

### M15. Transfer optimal fidelity without spending charge

**Central question.** How can a proof for the flat reference become a theorem about the known Haar state?

**Understanding target.** Explain sectorwise Schmidt alignment, why it respects charge, and why both the input and the desired returned catalyst change in the comparison. Interpret the uniform bound $`\lvert F^\star(\psi)-F^\star(\Omega)\rvert\le2P(\psi,\Omega)`$ for every target dimension and budget.

**Dependencies and story role.** [M05](#m05), [M07](#m07), [M14](#m14). This completes the bridge between the finite operational model and the Haar ensemble.

**Conceptual connection.** An unrestricted purification alignment would not establish an allowed zero-exchange change of basis; the sector structure provides that missing step.

**Sources.** Watrous [§§3.2.2–3.2.3, fidelity characterizations and further properties](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [charge-respecting alignment](../science/typical_states.md#alignment-respects-charge), and [uniform fidelity transfer](../science/typical_states.md#uniform-transfer-of-operational-fidelity).

<a id="m16"></a>

### M16. Convert a sector with excess or deficient rank

**Central question.** What can a shifted source sector contribute when it has too many or too few Schmidt dimensions?

**Understanding target.** Explain exact rank reduction when $`d_q\ge m d_{q+k}`$ and embedding when the inequality reverses. Read their common overlap factor $`\sqrt{\min\{1,d_q/(m d_{q+k})\}}`$, including why a deficient-rank output need not factor into a perfect catalyst and target.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M05](#m05), [M06](#m06), [M12](#m12). This gives the local conversion used by both finite and asymptotic attainability.

**Conceptual connection.** Keeping deficient sectors is essential at a limiting equality boundary where their finite-size rank ratios can approach one from either side.

**Sources.** Watrous [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [fixed-shift construction](../science/coherent_protocol.md#2-a-fixed-shift-fidelity-bound).

<a id="m17"></a>

### M17. Preserve coherence through a common outcome distribution

**Central question.** How can local rank conversions avoid recording which charge sector was present?

**Understanding target.** Explain why the naive cyclic-subset outcome probabilities depend on source rank, and how refinement to a common alphabet makes every conversion outcome have the same probability in every retained sector. Identify the resulting coherent branch vector after correction.

**Dependencies and story role.** [M03](#m03), [M06](#m06), [M16](#m16). This joins the individual conversions into a coherent operation.

**Conceptual connection.** The common refinement preserves coherence within a fixed announced shift; a preliminary charge-dependent filter may still reveal information, and its effect must be scored separately.

**Sources.** Watrous [§2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) supply instrument and LOCC foundations; [common outcome alphabet](../science/coherent_protocol.md#a-common-outcome-alphabet) supplies the coherent construction and its primary attribution.

<a id="m18"></a>

### M18. Complete the physical protocol and its resource accounting

**Central question.** What turns the desired action on occupied Schmidt vectors into a complete admissible channel?

**Understanding target.** Explain the complementary Kraus maps for unused inputs, Bob's partial-isometry correction, and the charge-conserving buffer dilation. Check why complementary outcomes remain counted and why the buffers reveal the announced shift without revealing an additional sector label.

**Dependencies and story role.** [M03](#m03), [M07](#m07), [M08](#m08), [M17](#m17). This closes the physical attainability argument for a fixed shift.

**Conceptual connection.** An isometry on the populated support and a complete physical channel have different proof obligations; neutral workspace and zero-shift complements meet the latter without supplied entanglement.

**Sources.** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Bob's complete correction](../science/coherent_protocol.md#bobs-correction-is-a-complete-physical-channel), [unconditional overlap](../science/coherent_protocol.md#the-unconditional-overlap), and [buffer dilation](../science/coherent_protocol.md#3-charge-conserving-dilations-and-net-exchange).

<a id="m19"></a>

### M19. Bound every complete branch by its available rank

**Central question.** Why can adaptive choices and filtering not evade the rank cost within a shifted sector?

**Understanding target.** Explain the rank-overlap bound for an unnormalized vector, how a product Kraus leaf preserves its rank ceiling, and why the target block must have charge $`q+k`$. Retain charge-dependent branch probabilities and give zero overlap to leaves with the wrong total charge.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M07](#m07), [M12](#m12), [M16](#m16). This supplies a local bound for every permitted implementation.

**Conceptual connection.** The same rank factor appears in the attaining construction and in the converse, but the converse allows arbitrary adaptive branching.

**Sources.** Watrous [§1.1.3, operator norms](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), and [§6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [sector rank and leaf amplitudes](../science/converse.md#2-sector-rank-bounds-the-amplitude-of-every-leaf).

<a id="m20"></a>

### M20. Sum all branches and close the zero-exchange case

**Central question.** How can a sector bound constrain an entire protocol with arbitrarily many outcomes?

**Understanding target.** Explain how trace preservation and vector Cauchy–Schwarz control the summed squared overlaps without an outcome-count factor. Track an omitted input tail at the root-fidelity level, and derive the exact finite flat-catalyst identity $`[F^\star(m,0)]^2=1/m`$ with its product-target attaining strategy.

**Dependencies and story role.** [M03](#m03), [M05](#m05), [M10](#m10), [M19](#m19). This converts the branchwise obstruction into a full operational converse and a first matching optimum.

**Conceptual connection.** Extensive entanglement in a catalyst does not imply high-fidelity borrowing at zero allowed exchange. For Haar catalysts, the same value is a limit through [M15](#m15).

**Sources.** Watrous [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [uniform bound with an input tail](../science/converse.md#3-a-uniform-bound-with-an-input-tail), and [exact zero-exchange identity](../science/converse.md#exact-zero-exchange-identity).

<a id="m21"></a>

### M21. Identify the exact finite filter problem

**Central question.** Which finite variables represent everything that a general protocol can gain?

**Understanding target.** Interpret $`T_{kq}`$ as source-sector allocation to a shift, and $`A_{kq}`$ as the charge-weight and rank-overlap coefficient. Explain grouping complete leaves into the primal upper bound, completion of missing probability at zero shift, and attainment by a charge-diagonal filter followed by coherent conversion.

**Dependencies and story role.** [M11](#m11), [M17](#m17), [M18](#m18), [M20](#m20). This joins construction and converse into an exact finite characterization.

**Conceptual connection.** Physically absent destinations and existing destinations with zero target overlap require correct treatment; neither permits renormalizing away failures.

**Sources.** Watrous [§1.2.1, convexity](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [finite primal problem](../science/finite_optimization.md#the-finite-primal-problem), and [charge-dependent filtering](../science/coherent_protocol.md#4-charge-dependent-filtering-and-the-finite-optimum).

<a id="m22"></a>

### M22. Certify the optimum through duality and a shift simplex

**Central question.** How can the finite optimum be bounded from above and represented with fewer variables?

**Understanding target.** Explain why each feasible positive dual vector bounds every filter, why the zero-shift row keeps dual coordinates away from zero, and how the equivalent shift-simplex program reconstructs both a feasible filter and a feasible dual point.

**Dependencies and story role.** [M11](#m11), [M21](#m21). This turns an operational characterization into a certifiable calculation.

**Conceptual connection.** Convex duality closes the mathematical optimum; the explicit reconstruction makes a computed value interpretable as an attainable lower bound and a universal upper bound.

**Sources.** Watrous [§§1.2.1 and 1.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) supply convex optimization background; [convex dual and its boundary](../science/finite_optimization.md#convex-dual-and-its-boundary), and [optimization over charge shifts](../science/finite_optimization.md#equivalent-optimization-over-charge-shifts) prove the specific formulations.

<a id="m23"></a>

### M23. Read finite verification as mathematical evidence

**Central question.** What do the stored channel checks and numerical certificates establish?

**Understanding target.** Interpret the independent two-sector value $`92/175`$, feasible filter and dual witnesses, outward rounding, and root-fidelity tail expansion. Distinguish direct matrices on populated support, written completion on unused inputs, and certificate replay without optimization.

**Dependencies and story role.** [M05](#m05), [M10](#m10), [M18](#m18), [M22](#m22). This connects the finite theory to reproducible evidence.

**Conceptual connection.** A narrow valid interval controls a finite model. It does not prove Haar concentration or an asymptotic law, and replay of stored witnesses is distinct from an independently implemented arithmetic verifier.

**Sources.** Watrous [§1.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) supplies the certificate perspective; [verification scope](../verification/README.md#what-is-checked), [certificate arithmetic](../verification/README.md#solver-and-certificate-arithmetic), [tail accounting](../verification/README.md#tail-accounting), and [representative output](../verification/README.md#representative-output).

<a id="m24"></a>

### M24. Turn a charge shift into a rank advantage

**Central question.** Why does the filling determine the entanglement available per unit of exchange?

**Understanding target.** Read the adjacent-binomial ratio as a local slope, with $`\mu=\ln[(1-\nu)/\nu]`$. Explain the favorable shift direction and the uniform approximation $`\ln(a_q/a_{q+k})=-\mu k+\text{error}`$, including why the error depends on both the charge window and the shift range.

**Dependencies and story role.** [M09](#m09), [M10](#m10), [M13](#m13), [M16](#m16). This extracts the quantitative exchange scale from the many-body sector dimensions.

**Conceptual connection.** The rank slope controls target size; it does not determine whether the translated catalyst returns accurately.

**Sources.** Watrous [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) supplies rank-conversion background; [uniform binomial rank ratios](../science/asymptotics.md#2-uniform-binomial-rank-ratios), and [rank gained per exchanged particle](../science/interpretation.md#rank-gained-per-exchanged-particle).

<a id="m25"></a>

### M25. Measure return error through translated charge weights

**Central question.** When is a shift small enough to remain hidden within the catalyst's charge distribution?

**Understanding target.** Interpret the root overlap $`\sum_q\sqrt{p_qp_{q-s}}`$ and its Gaussian limit $`\exp[-s^2/(8\sigma_L^2)]`$. Explain why shifts below $`\sqrt L`$ have vanishing distributional disturbance, and why the proved uniform approximation is an absolute-error statement.

**Dependencies and story role.** [M05](#m05), [M09](#m09), [M10](#m10), [M13](#m13). This provides the return-accuracy scale to accompany the rank advantage.

**Conceptual connection.** Root fidelity must be squared when enforcing the purified-distance threshold; this changes the exponent and fixes the capacity coefficient.

**Sources.** Watrous [§3.2.1, elementary fidelity properties](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [uniform hypergeometric shift-overlap limit](../science/asymptotics.md#3-a-uniform-hypergeometric-shift-overlap-limit), and [return error from translating the charge distribution](../science/interpretation.md#return-error-from-translating-the-charge-distribution).

<a id="m26"></a>

### M26. Close the fixed-budget law, including equality

**Central question.** How do construction and converse meet for fixed target dimension and fixed exchange?

**Understanding target.** Combine the uniform rank factor, vanishing translation error, complete-outcome bound, and Haar transfer to obtain $`[F_L^\star(m,S)]^2\to\min\{1,e^{\lvert\mu\rvert S}/m\}`$. Explain why the rank-deficit construction includes the equality case, and interpret the quarter-filling targets $`m=2,3,4`$.

**Dependencies and story role.** [M15](#m15), [M16](#m16), [M18](#m18), [M20](#m20), [M24](#m24), [M25](#m25). This is the first full many-body cost theorem.

**Conceptual connection.** Limiting fidelity one at equality does not require every finite-size sector to allow exact conversion, and it does not assert exact finite-size fidelity one.

**Sources.** Watrous [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) and [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [fixed-exchange theorem](../science/model.md#fixed-exchange), [complete converse](../science/converse.md), and [quarter-filling example](../science/interpretation.md#a-fixed-budget-example).

<a id="m27"></a>

### M27. Resolve budgets below the fluctuation scale

**Central question.** What remains visible when the exchange grows but stays smaller than $`\sqrt L`$?

**Understanding target.** Explain the transition determined by $`\ln m_L-\lvert\mu\rvert S_L\to c`$, with limiting squared fidelity $`\min\{1,e^{-c}\}`$. Deduce the leading yield per exchange for diverging $`S_L=o(\sqrt L)`$, and explain why an adaptive charge window is needed for an $`o(1)`$ rank error.

**Dependencies and story role.** [M10](#m10), [M24](#m24), [M25](#m25), [M26](#m26). This resolves a scale that the leading $`\sqrt L`$ capacity alone cannot describe.

**Conceptual connection.** A lower-order remainder on one scale can overwhelm the entire answer on a smaller scale; the sharper estimate preserves the actual exchange dependence.

**Sources.** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) supplies probability background; [sub-fluctuation transition](../science/converse.md) and [smaller-budget capacity analysis](../science/asymptotics.md) provide the precise sequences and error estimates.

<a id="m28"></a>

### M28. Combine the charge limit and the Gaussian capacity limit

**Central question.** What fixes the leading borrowable entanglement when the budget reaches or exceeds the fluctuation scale?

**Understanding target.** Explain why the capacity is the smaller of the charge-budget bound and the established unrestricted Gaussian bound. Identify why that unrestricted bound covers mixed outputs, how a charge-respecting protocol approaches the same leading value with subleading rank slack, and why the result leaves constant-order boundary corrections unspecified.

**Dependencies and story role.** [M04](#m04), [M15](#m15), [M18](#m18), [M20](#m20), [M24](#m24), [M25](#m25), [M27](#m27). This integrates the growing-budget theorem.

**Conceptual connection.** Replacing a mixed output by a pure one justifies an unrestricted upper relaxation. The separate charged construction establishes attainability under the budget.

**Sources.** Watrous [§4.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) and [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [mixed-output unrestricted bound](../science/asymptotics.md#4-the-unrestricted-bound-includes-mixed-outputs), [capacity proof](../science/asymptotics.md), and [Zhang–Liu–Chen attribution](../references/RELATED_WORK.md#zlc26).

<a id="m29"></a>

### M29. Interpret the cost and locate the contribution

**Central question.** What physical capability does the optimal exchange law add to the known borrowing resource?

**Understanding target.** Connect rank gained per favorable shift, disturbance of the charge distribution, and preservation of coherence. Explain how the theorem identifies the accessible fraction of the known many-body resource, while crediting the unrestricted Gaussian law and established symmetry-respecting conversion methods.

**Dependencies and story role.** [M08](#m08), [M18](#m18), [M23](#m23), [M26](#m26), [M28](#m28). This gives the proved formulas a unified operational meaning.

**Conceptual connection.** Changed charge buffers, known catalyst descriptions, and potentially large local operations remain part of the accounting. Charge optimality does not establish an efficient circuit or an exactly returned auxiliary resource.

**Sources.** Watrous [§6.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) supplies the entanglement-conversion setting; [physical interpretation](../science/interpretation.md) and [precise contribution statement](../references/RELATED_WORK.md#7-precise-contribution-statement) locate the added result and its inherited ingredients.

<a id="m30"></a>

### M30. Reconstruct the complete argument and its boundaries

**Central question.** How do the physical model, exact finite theory, and asymptotic analysis support the headline claims together?

**Understanding target.** Trace a connected route from the stated resources to a physical flat reference, coherent attainment, the complete-outcome converse, finite certificates, and transfer of the fixed and growing laws to Haar catalysts. Identify where unequal cuts, non-half filling, known states, neutral targets, and the hard net budget enter that route.

**Dependencies and story role.** [M12](#m12), [M15](#m15), [M23](#m23), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). This integrates the entire project.

**Conceptual connection.** A broad charge distribution, a numerical trend, or extensive ordinary entanglement alone does not supply the full theorem. The conclusion requires the specified spectra, admissible implementation, joint accuracy criterion, and matching upper bound.

**Sources.** The selected foundations are collected in the [Watrous bridge](WATROUS_BRIDGE.md). The authoritative synthesis is [model and claims](../science/model.md), [physical interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), and [verification scope](../verification/README.md#what-is-checked).

Return to the [repository overview](../README.md), follow the [Watrous bridge](WATROUS_BRIDGE.md), or enter the [scientific account](../science/model.md).
