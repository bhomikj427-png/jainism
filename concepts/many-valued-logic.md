---
term_iast: many-valued logic
term_devanagari: (no Sanskrit equivalent)
tradition: Western (mathematical logic / philosophy of logic)
source_text: Jan Łukasiewicz (1920), *On Three-Valued Logic*; modern formal logic
status: converged
confidence: medium
---

## Gloss / Divergence map

Many-valued logic is **formal logic extended beyond the classical two truth-values (True/False)** to allow additional values. The most influential version is Jan Łukasiewicz's three-valued logic (1920), which adds a third value to handle propositions that are neither definitely true nor definitely false.

**Łukasiewicz's three-valued logic (Ł3):**
- **True (T)** — the proposition is true
- **False (F)** — the proposition is false
- **Indeterminate (#)** — the proposition is neither true nor false

Łukasiewicz introduced # for **philosophical reasons**: to account for contingent future statements ("there will be a sea-battle tomorrow" — not yet true, not yet false). The third value represents temporal indeterminacy. If a proposition has value #, its negation also has value #.

**Many-valued logics generally** include Kleene's three-valued logic, Priest's LP (Logic of Paradox), Belnap's four-valued logic, fuzzy logics (infinite-valued), etc. What they share: each truth-value behaves predictably under the logical connectives (a truth-table is definable for each).

## Why saptabhaṅgī is NOT a many-valued logic

This is the `often-conflated-with-NOT-equivalent` claim from saptabhangi.md. The three key structural differences:

| dimension | Łukasiewicz Ł3 / many-valued logics | Jain saptabhaṅgī |
|---|---|---|
| What is it? | a system of truth-values with defined connectives | a system of **syāt-qualified predication modes** (seven ways of asserting something from standpoints) |
| Are the "values" truth-values? | YES — T, F, # are truth-functional | NO — the seven forms are *types of assertion*, not truth-values; "syād asti" is not a truth-value, it is "in-some-respect it is" |
| Third value origin | temporal indeterminacy (future contingents) | *avaktavya* arises from the simultaneous-assertion problem — "asti AND nāsti asserted at once, which language cannot express in one breath" |
| Compositionality | truth-tables define output for any connective | saptabhaṅgī gives 7 assertion-modes; not a compositional calculus of truth-values |
| Context | modern propositional/modal logic | ancient Jain standpoint-epistemology |

**Schang's comparative work** (Fabien Schang, "Two Indian Dialectical Logics: saptabhaṅgī and catuṣkoṭi," cited in PhilPapers/Semantic Scholar): Schang has done the most systematic formal analysis of saptabhaṅgī. His approach is to reconstruct the logical structure without claiming it is equivalent to Western many-valued logics. Key point: "The irrationality currently imputed to these logics relies on philosophical preconceptions inherited from Aristotelian metaphysics" — the Aristotelian non-contradiction law is not the operative framework in saptabhaṅgī.

**The wider lesson:** The seven predicates of saptabhaṅgī look formally like "seven truth-values" because they are seven distinct predication modes. But this surface resemblance is misleading — saptabhaṅgī is a theory of *standpoint-qualified assertions*, not a theory of *truth-functional operators*. Equating them flattens both.

## Reasoning across signals

**Signal 1 — Wikipedia "Three-valued logic":** Łukasiewicz system; T/F/# values; future contingents as motivation. Fetched from earlier search context. Medium provenance.

**Signal 2 — Search result aggregation (Schang PhilPapers, Semantic Scholar, saptabhaṅgī Wikipedia):** Schang's comparative work; "predication scheme not truth-values" distinction; non-Aristotelian assumption note. Consistent.

**Independence:** Signal 1 is standard mathematical logic (widely confirmed). Signal 2 references Schang's work, not directly fetched. Confidence medium: Schang's paper not fetched; the structural distinction argument is based on understanding of both systems from prior concept files.

## Sources

1. Wikipedia, "Three-valued logic," accessed June 2026. https://en.wikipedia.org/wiki/Three-valued_logic — Łukasiewicz; T/F/#; future contingents.

2. Fabien Schang, "Two Indian Dialectical Logics: saptabhaṅgī and catuṣkoṭi," cited in PhilPapers/Semantic Scholar. Not directly fetched. https://philpapers.org/rec/SCHTID-9

3. **Not yet fetched (confidence upgrade):** Schang's actual paper; Bimal Matilal, *The Central Philosophy of Jainism* (1981), Chapter on logical structure of saptabhaṅgī.

## Links

- often-conflated-with-NOT-equivalent: saptabhangi | many-valued logics use defined truth-values with connectives; saptabhaṅgī is a syāt-qualified predication scheme — surface similarity (seven forms vs. multiple values) masks deep structural difference
- often-conflated-with-NOT-equivalent: quantum-complementarity | quantum probabilities are physical amplitudes, not Łukasiewicz truth-values; the non-bivalence of quantum measurement is about physical exclusivity of outcomes, not semantics
