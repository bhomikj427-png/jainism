---
term_iast: fuzzy-logic
tradition: Western (mathematical logic / artificial intelligence)
source_text: Lotfi A. Zadeh, "Fuzzy Sets," *Information and Control* 8(3): 338–353, 1965
status: converged
confidence: medium
---

## Gloss

A formal logic in which truth values are **degrees in the continuous interval [0, 1]** rather than the binary {true, false}. Introduced by Lotfi A. Zadeh in his 1965 paper "Fuzzy Sets" (*Information and Control* 8(3): 338–353). A fuzzy set assigns a *degree of membership* to each element: a person 5'10" might have membership 0.7 in the set "tall people." The logic generalises classical connectives: min(a, b) for conjunction, max(a, b) for disjunction, 1-a for negation.

**Primary motivation — the sorites paradox** ("paradox of the heap"): 10,000 grains = a heap; remove one grain at a time: at what point is it no longer a heap? Classical bivalence offers no non-arbitrary threshold. Fuzzy logic responds by making heap-ness a matter of degree — "is a heap" = 0.95 at 10,000 grains, gradually declining.

**Fuzzy logic ≠ probability theory**: this distinction is precise and important.

| feature | fuzzy logic | probability |
|---|---|---|
| what it models | vagueness — how *imprecisely* a term applies | uncertainty / ignorance — how *likely* a proposition is true |
| nature of proposition | the proposition is vague (gradational) | the proposition is crisp (binary); we just don't know which |
| example | "tall" applied to someone 5'10": degree 0.7 | "it will rain tomorrow": P = 0.7 |
| sum constraint | no: A and ¬A degrees need not sum to 1 | yes: P(A) + P(¬A) = 1 |

**Fuzzy logic and many-valued logic**: fuzzy logic is a *species* of many-valued logic (it uses the continuous [0,1] instead of a discrete finite set). Łukasiewicz 3-valued logic ({T, F, ½}) is many-valued but not fuzzy; all fuzzy logic is many-valued.

## Reasoning across signals

**Signal 1** (SEP "Logic, Fuzzy"): Zadeh 1965 cited with full reference; [0,1] degree-of-membership semantics; truth-functional connectives over the continuum documented. **Signal 2** (Wikipedia "Fuzzy logic" + arxiv survey): fuzzy-vs-probability distinction precisely stated ("vagueness vs. ignorance"); sorites paradox as primary motivation; Zadeh's own caveat that "fuzziness is not vagueness" noted. Two independent editorial sources, both tracing to Zadeh 1965. Medium confidence: Zadeh 1965 primary paper not independently fetched; standard doctrine extremely well-attested.

## Sources

- "Logic, Fuzzy," *Stanford Encyclopedia of Philosophy*, https://plato.stanford.edu/entries/logic-fuzzy/ — Zadeh 1965 citation; [0,1] semantics; truth-functional connectives.
- "Fuzzy Logic," *Wikipedia*, https://en.wikipedia.org/wiki/Fuzzy_logic — fuzzy vs probability (vagueness vs ignorance); sorites paradox motivation.

## Links

- is-a-type-of: many-valued-logic | fuzzy logic is the continuous-[0,1] species of many-valued logic; many-valued logic is the broader genus (includes discrete systems like Łukasiewicz 3-valued)
- often-conflated-with-NOT-equivalent: saptabhangi | both address the inadequacy of binary yes/no predication; but saptabhaṅgī's seven modes use *syāt* as a perspectival qualifier (assertion is binary within each standpoint; complexity arises from standpoint-multiplicity); fuzzy logic gives a single assertion-context a degree in [0,1] — orthogonal mechanisms
- structurally-parallel-to: saptabhangi | both propose that "A applies to X" cannot always be answered with a simple yes or no; the surface motivation overlaps even though the formal solutions are incompatible
- often-conflated-with-NOT-equivalent: anekantavada | anekāntavāda says X IS permanent (from dravya-naya) AND IS impermanent (from paryāya-naya) — two binary assertions from different standpoints, not a single assertion with degree 0.5; fuzzy logic would encode "X's permanence = 0.5" in a single context
- often-conflated-with-NOT-equivalent: paraconsistent-logic | both go beyond classical bivalence; fuzzy logic addresses *vagueness* (gradation); paraconsistent logic addresses *contradiction* (ECQ-rejection); neither entails the other — a fuzzy logic may or may not be paraconsistent
- shares-vocabulary-with: many-valued-logic | fuzzy logic was historically often presented as "many-valued," but the continuous [0,1] structure and the sorites-vagueness motivation distinguish it from discrete many-valued systems
