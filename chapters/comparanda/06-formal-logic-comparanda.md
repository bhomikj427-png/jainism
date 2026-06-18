# Chapter 06 — Many Options Are Not Many Truth-Values: Indian Predication vs Modern Non-Classical Logic

**Concepts covered:** catuṣkoṭi · many-valued-logic · paraconsistent-logic · fuzzy-logic
**Cross-referenced (primary-covered in Ch 02):** saptabhaṅgī · anekāntavāda
**Confidence:** all medium. The modern-logic material (Łukasiewicz, Priest's LP, Zadeh's fuzzy sets) is standard and very well attested via SEP/IEP; the catuṣkoṭi material rests on aggregated secondary sources (Priest 2010 and Schang's comparative paper were *not* directly fetched). The four "NOT-equivalent" verdicts are the corpus's own structural arguments, built from the concept files — they are reasoned, not quoted from a single authority.
**Source ceiling note:** No primary text was fetched this run. Nāgārjuna's MMK (the catuṣkoṭi-in-action chapters), Priest's "Logic of the Catuṣkoṭi," and Schang's "Two Indian Dialectical Logics" are all cited second-hand. Łukasiewicz 1920, Zadeh 1965, and the SEP/IEP entries on paraconsistent and fuzzy logic are standard references summarised, not re-derived.

---

## How to use this chapter

This is the chapter the whole project was built to make possible. Chapters 02 and 05 laid out the Indian schemes for saying more than a flat "true" or "false": the Jain **saptabhaṅgī** (sevenfold predication) and the Buddhist **catuṣkoṭi** (four corners). In the twentieth century, formal logicians built their own systems that also break out of two-valued logic: **many-valued**, **paraconsistent**, and **fuzzy** logic. The surface resemblance is irresistible — and almost every popular account gives in to it: *"The Jains invented many-valued logic 2,000 years before Łukasiewicz!"* *"Nāgārjuna was doing paraconsistent logic!"*

That move is exactly the prime-directive failure this corpus exists to prevent (CLAUDE.md §0). The schemes look alike because they share a *negative* feature — none is content with two options. But sharing a "no" does not make two systems the same system. This chapter does the careful work: lay both kinds of scheme on the table, then run four precise tests showing where the equivalence breaks. The goal is not to deny the parallels — they are real and interesting — but to label them as *parallels*, never identities.

You will get more from this chapter if you have met saptabhaṅgī (Ch 02 §6). Leave `> stuck` on its own line where you get lost; paste the teaching prompt; it will re-explain in place.

---

## 1. The temptation, stated precisely {#temptation}

Classical (two-valued, "bivalent") logic says every proposition is exactly one of True or False, and nothing can be both. Five systems in this chapter all refuse some part of that:

| scheme | tradition | refuses... | offers instead |
|---|---|---|---|
| saptabhaṅgī | Jain (Ch 02) | that one flat assertion captures a thing | seven *standpoint-qualified* assertions (*syāt* …) |
| catuṣkoṭi | Buddhist | that the answer is one of just two corners | four corners — and (Nāgārjuna) the escape from all four |
| many-valued logic | modern | bivalence (only T, F) | extra truth-*values* (e.g. Łukasiewicz's third value #) |
| paraconsistent logic | modern | explosion (that a contradiction makes *everything* true) | tolerance of a true contradiction without collapse |
| fuzzy logic | modern | that membership is all-or-nothing | *degrees* of truth across the interval [0, 1] |

Read the "refuses" column and the temptation is obvious: they all reject "just two." But read the "offers instead" column and the cracks already show. Three different things are being offered — qualified *assertions*, escape from a *schema*, and graded *values* — and they are not interchangeable. The rest of the chapter is that observation made rigorous.

---

## 2. The Buddhist four corners — *catuṣkoṭi* {#catuskoti}

*→ concept file: [catuskoti.md](../../concepts/catuskoti.md)*

The catuṣkoṭi ("four corners," tetralemma) enumerates every way a proposition could stand:

| corner | Sanskrit | predication |
|---|---|---|
| 1 | asti | it **is** |
| 2 | nāsti | it **is not** |
| 3 | asti ca nāsti ca | it **both is and is not** |
| 4 | na asti na nāsti | it **neither is nor is not** |

What makes it philosophically live is that it is used in **two opposite-spirited ways**:

- **Use 1 — the Buddha's silence (*avyākata*).** In the Pali Canon, certain questions ("Is the world eternal? not? both? neither?") get *all four corners declined*. The silence is not "I don't know"; it signals that the question is **malformed** — none of the four conceptual slots correctly applies, so the right response is to refuse the frame.
- **Use 2 — Nāgārjuna's *prasaṅga*.** In the *Mūlamadhyamakakārikā* (~2nd c.), Nāgārjuna takes any claim of inherent existence (*svabhāva*), walks it through all four corners, and shows each one collapses into absurdity. Escaping all four *is* the demonstration of emptiness (*śūnyatā*). The schema is a deconstruction engine, not a menu of answers.

Hold Use 2 firmly — it is what wrecks the paraconsistent reading in §5.4. Nāgārjuna's attitude to corner 3 ("both is and is not") is to **refute** it along with the rest, not to endorse it.

### 2.1 Catuṣkoṭi vs saptabhaṅgī — sibling schemes, opposite aims {#catuskoti-vs-saptabhangi}

Both are non-bivalent Indian predication schemes, and they get conflated with each other as readily as with modern logic. They are structurally analogous and philosophically opposite:

| dimension | catuṣkoṭi (Buddhist) | saptabhaṅgī (Jain) |
|---|---|---|
| number of forms | 4 | 7 |
| key operation | exhaustive enumeration → (Nāgārjuna) reject all | standpoint-parameterisation (*syāt*) → conditionally assert |
| the "both" form | corner 3, to be escaped | predication 3, true *from two standpoints in sequence* |
| relation to truth | seeks to escape all corners → śūnyatā | each of 7 is conditionally true from its standpoint |
| net purpose | **deconstruct** all views | **organise** partial truths (anekāntavāda) |

Same logical territory, opposite outcomes: catuṣkoṭi dismantles, saptabhaṅgī builds. They are analogous tools, not one tool.

---

## 3. The modern toolkit, in plain terms {#modern}

*→ concept files: [many-valued-logic.md](../../concepts/many-valued-logic.md) · [paraconsistent-logic.md](../../concepts/paraconsistent-logic.md) · [fuzzy-logic.md](../../concepts/fuzzy-logic.md)*

Three twentieth-century systems, each refusing bivalence for its *own* reason. The reasons matter more than the refusals.

**Many-valued logic (Łukasiewicz, 1920).** Add a third truth-*value* beyond True and False: **# (indeterminate)**. Łukasiewicz introduced it for a specific problem — *future contingents*. "There will be a sea-battle tomorrow" seems neither true nor false *yet*; # marks that temporal openness. Crucially, #, like T and F, is a genuine **truth-value** with defined truth-tables: every connective (and, or, not) has a fixed output for it.

**Fuzzy logic (Zadeh, 1965).** Replace the discrete value-set with the whole continuous interval **[0, 1]**. Truth comes in *degrees*: a 5'10" person has membership 0.7 in "tall." Its target problem is **vagueness** — the sorites paradox ("when does removing one grain stop it being a heap?"). Fuzzy logic is a *species* of many-valued logic (it just uses infinitely many values).

> **Fuzzy ≠ probability** — a distinction worth fixing now: fuzzy degree 0.7 means "tall" *applies partially* (a vague predicate); probability 0.7 means a *crisp* proposition is *likely* (uncertainty about a yes/no fact). Fuzzy degrees of A and ¬A need not sum to 1; probabilities must.

**Paraconsistent logic (Priest's LP).** Target a third, different problem: **explosion** (*ex contradictione quodlibet*). In classical logic, one true contradiction makes *every* proposition derivable — the theory goes trivially true-of-everything. A paraconsistent logic blocks that, so a theory can contain a contradiction and still be useful (Priest's example: Bohr's atom, internally contradictory yet scientific). Priest's **LP** adds a third value **B (both-true-and-false)** that is "designated" (inference-preserving). The cost is real: *modus ponens fails* in LP.

Note the genus/species tangle: fuzzy *is-a-type-of* many-valued; LP is *both* many-valued and paraconsistent; but neither of those properties entails the other. Already the modern systems don't reduce to each other — so they certainly won't all reduce to one ancient scheme.

---

## 4. The shape of the four tests {#tests-intro}

Each ancient scheme gets paired with the modern system it is most often confused with. In every case the method is the same: find the **mechanism** each system actually uses, and show the mechanisms are doing different jobs.

| # | the conflation | the one-line refutation |
|---|---|---|
| 5.1 | saptabhaṅgī = many-valued logic | predication-modes are not truth-values |
| 5.2 | saptabhaṅgī = paraconsistent logic | standpoint-relativization ≠ ECQ-rejection |
| 5.3 | anekāntavāda/saptabhaṅgī = fuzzy logic | binary-within-a-standpoint ≠ a single graded value |
| 5.4 | catuṣkoṭi = paraconsistent logic | a refutation schema ≠ a preserved "both" value |

---

## 5. The four tests {#tests}

### 5.1 saptabhaṅgī is not many-valued logic {#test-mvl}

*→ [many-valued-logic.md](../../concepts/many-valued-logic.md) · [saptabhangi.md](../../concepts/saptabhangi.md)*

The lure: saptabhaṅgī has seven forms, many-valued logic has several values — so the seven forms must be "seven truth-values."

> ⚠️ **Why it fails.** The seven *bhaṅgas* are **modes of assertion**, not **truth-values**. *"Syād asti"* is not a value a proposition *has*; it is the act "in-some-respect, it is." A truth-value (T, F, #) is an input to truth-tables — it composes: given the values of A and B, the value of "A and B" is fixed. Saptabhaṅgī has no such compositional calculus; it is a catalogue of seven *ways to make a standpoint-qualified claim*, not a function from values to values. And the third element, *avaktavya* (inexpressible), arises from a problem with **no analogue** in Łukasiewicz: the inability of linear language to assert *asti* and *nāsti* in the *same breath*. Łukasiewicz's # comes from temporal openness about the future — an entirely different motivation.

| | Łukasiewicz Ł3 | saptabhaṅgī |
|---|---|---|
| the "extra" item is a... | truth-value (#) | predication-mode (*syād avaktavya*) |
| where it comes from | future contingents (temporal indeterminacy) | simultaneous-assertion limit of language |
| composes via truth-tables? | yes | no |

As Fabien Schang notes, the apparent "irrationality" of saptabhaṅgī is an artefact of judging it by Aristotelian non-contradiction — which is not its operative framework.

### 5.2 saptabhaṅgī is not paraconsistent logic {#test-para}

*→ [paraconsistent-logic.md](../../concepts/paraconsistent-logic.md) · [saptabhangi.md](../../concepts/saptabhangi.md)*

The lure: both seem to let "A and not-A" stand together without disaster.

> ⚠️ **Why it fails — the mechanisms are orthogonal.** Paraconsistent logic tolerates a contradiction that is true **in the same context** (or context-free): it keeps (A ∧ ¬A) from exploding into triviality by rejecting ECQ. Saptabhaṅgī never has a single-context contradiction in the first place. *"Syāt asti"* and *"syāt nāsti"* are asserted from **different standpoints (nayas)** — different parameters. There is nothing to explode, because the two claims were never made under one description. Paraconsistency is a fix for contradictions you are stuck with; standpoint-relativization is a method that *prevents the contradiction from forming*. One rejects an inference rule (ECQ); the other relativises the assertion. They solve different problems with different machinery.

A sharp way to hold it: a paraconsistent logician says "A and ¬A can both be true here." The Jain says "A is true *there* and ¬A is true *elsewhere*; nowhere are both true together." Those are not the same tolerance.

### 5.3 anekāntavāda / saptabhaṅgī is not fuzzy logic {#test-fuzzy}

*→ [fuzzy-logic.md](../../concepts/fuzzy-logic.md) · [anekantavada.md](../../concepts/anekantavada.md)*

The lure: both deny that "is X permanent?" gets a flat yes/no.

> ⚠️ **Why it fails — degree vs standpoint.** Fuzzy logic answers "how permanent?" with a **single graded value in one context**: permanence = 0.5. Anekāntavāda answers with **two crisp binary assertions in two contexts**: X *is* permanent (from the substance-standpoint, dravyārthika-naya) **and** X *is* impermanent (from the mode-standpoint, paryāyārthika-naya) — each fully, not half. There is no "0.5." Within each standpoint the assertion is ordinary and binary; the richness comes from the *multiplicity of standpoints*, not from a softened truth-value. Fuzzy logic locates the complexity *inside a single assertion* (a degree); anekāntavāda locates it *across assertions* (standpoints). Encoding "permanence = 0.5" would actually **misdescribe** the Jain claim, which insists on full permanence and full impermanence, not half of each.

This also separates it cleanly from probability and from vagueness: the Jain is not unsure, and the predicate is not gradational — the object genuinely bears both aspects, fully, from different angles.

### 5.4 catuṣkoṭi is not paraconsistent logic {#test-catuskoti-para}

*→ [catuskoti.md](../../concepts/catuskoti.md) · [paraconsistent-logic.md](../../concepts/paraconsistent-logic.md)*

The lure (the most sophisticated one, and Graham Priest's actual proposal): catuṣkoṭi's third corner — "both is and is not" — looks exactly like LP's designated value **B (both-true-and-false)**. So model the tetralemma in paraconsistent logic.

> ⚠️ **Why it fails — reversed attitudes to the third corner.** This is the subtlest test because the *structures* really do line up: corner 3 ≈ value B. But the **methodological intent is reversed**. Priest's LP **preserves** B — it is a designated value you can validly reason from; "both" is a stable resting place. Nāgārjuna's prasaṅga **refutes** corner 3 along with corners 1, 2, and 4 — "both" is one more position to be dismantled on the road to śūnyatā, never a resting place. A logic that keeps "both" as a truth-value is doing the *opposite* of a method whose entire purpose is to leave you holding *none* of the four. Formal resemblance, antithetical use.

The honest qualifier, in fairness to Priest: a *paraconsistent semantics* can faithfully model the catuṣkoṭi as a **schema of four enumerated possibilities** (this is genuinely useful, and §6 credits it). What it cannot capture without distortion is Nāgārjuna's *deconstructive* deployment — the part where every corner, including the paraconsistent-looking one, is thrown away.

---

## 6. Where the modern tool genuinely earns its place {#fit}

The prime directive (CLAUDE.md §0) says *assert less*, not *deny everything*. So credit the real fit: Priest's paraconsistent reading is a legitimate **formal reconstruction of the catuṣkoṭi-as-schema** — it gives precise semantics to "all four corners are on the table, and corner 3 is not automatically incoherent." That is a real contribution and the concept file records it as `structurally-parallel-to`, not as a false equivalence.

The line the corpus draws is exactly here: a modern logic can *model a structure* an ancient scheme uses. It cannot thereby *become* the ancient philosophy, because the philosophy lives in the **use** — Nāgārjuna's escape from all corners, the Jain's standpoint-discipline — and the use is precisely what the formal model leaves out. Structure transfers; purpose does not. That is the whole difference between `structurally-parallel-to` and identity.

---

## 7. Why this matters {#why}

Every conflation in this chapter runs the same con: spot a shared "not just two," then quietly upgrade *parallel* to *identical*, and conclude that an ancient text "already had" a modern formal system. The upgrade always smuggles something in — truth-functional composition (5.1), ECQ-rejection (5.2), graded membership (5.3), a preserved contradiction (5.4) — that the ancient scheme never contained. Naming the smuggled item is the antidote, every time.

The reward for refusing the conflation is that the actual ideas get *sharper*, not duller. Saptabhaṅgī turns out to be a standpoint-epistemology, not a truth-table. The catuṣkoṭi turns out to be a ladder you kick away, not a four-valued algebra. You lose a flashy headline and gain the real philosophy.

---

## 8. Check yourself {#check}

**8.1** Saptabhaṅgī has seven forms; Łukasiewicz's logic has three truth-values. Why is "seven truth-values vs three" the wrong way to compare them? Say what a *bhaṅga* is, if it is not a truth-value.

**8.2** A paraconsistent logician and a Jain both seem happy to say "A and not-A." Restate each one's claim precisely enough that you can see they are *not* saying the same thing. (Hint: one word — *context*.)

**8.3** Fuzzy logic would render "the soul is permanent" as, say, 0.5. Why does a Jain reject that number outright — and what does anekāntavāda assert instead?

**8.4** Priest's paraconsistent model of the catuṣkoṭi is the *best* of the four comparisons — the structures genuinely align. So why is it still not an identity? Point to what Nāgārjuna does to corner 3 that LP refuses to do.

---

*Next: with epistemology (Ch 05) and the logic comparanda (Ch 06) complete, the natural next cluster is the atomism/physics comparison — paramāṇu · paramāṇu-vaiśeṣika · democritus-atom · modern-atom · quantum-complementarity — where the same `structurally-parallel-to` vs `NOT-equivalent` discipline meets the strongest "the ancients knew physics" temptation of all.*
