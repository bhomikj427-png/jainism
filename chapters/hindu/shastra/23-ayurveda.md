# Chapter 23 — Āyurveda: Two Compendia, Two Missing Authors, and a Contested Age

**Concepts covered:** āyurveda · caraka · suśruta · tridoṣa · with dhanvantari (primary in Ch. 21) and pañcamahābhūta · guṇa-sāṃkhya · prakṛti-sāṃkhya cross-referenced
**Confidence:** medium throughout, with the corpus's own sourcing weaknesses recorded per-node rather than averaged. The umbrella file [ayurveda.md](../../../concepts/ayurveda.md) notes that **all its signals trace back to one platform** (three separately-maintained Wikipedia articles citing different primaries) and that **Meulenbeld's *History of Indian Medical Literature* — the authoritative academic source underlying the dating claims — was cited through summaries, never fetched.** [charaka.md](../../../concepts/charaka.md) records that **Britannica returned HTTP 403** on both relevant pages and was not silently substituted. [tridosha.md](../../../concepts/tridosha.md) records **two comparative-scholarship PDFs that could not be read** (unparseable binary via the fetch tool), so the promised cross-textual comparison of how Charaka, Suśruta, and Vāgbhaṭa each elaborate the doctrine **was not achieved** and is flagged as an open item.
**Two of the four files are `contested`** — [charaka.md](../../../concepts/charaka.md) and [suśruta.md](../../../concepts/sushruta.md) — and in both cases the contest is about **whether the named author is a person at all.**

---

## How to use this chapter

This is the first chapter in `hindu/shastra/`, a sub-folder added for it. Āyurveda fits none of the three existing ones: **the Saṃhitās are texts but not scripture, the system is systematic but not a *darśana*, and Dhanvantari's patronage is a religious framing laid over a medical tradition rather than the tradition itself.** Rather than force it into `scripture/`, the corpus added a fourth level for technical *śāstra* — which will also hold *jyotiṣa*, *Arthaśāstra*, *Nāṭyaśāstra* and the like if they are ever written.

**Remit note.** **Dhanvantari** is primary-covered in **Ch. 21 §5** as a churning-*ratna*; he appears here only in his medical role. The ***pañcamahābhūta*** element scheme is **Ch. 16 §6**; ***prakṛti*** and ***guṇa*** as Sāṃkhya metaphysics are **Ch. 15**. This chapter uses all three and re-derives none.

**The organising question.** Every other chapter in this corpus deals with traditions that make claims about liberation, or about what can be known, or about who the supreme being is — claims that no external discipline is positioned to adjudicate. **Āyurveda is different: it makes claims about bodies, and medicine is a field where an external verdict exists and is unfavourable.** That creates a specific methodological problem for a project whose §0 directive is to understand traditions *on their own terms*, and §7 is about how the corpus handles it. The short version, in the concept file's own words: **"§0's 'analogy is not identity' cuts both ways: neither smuggling in a physics validation nor smuggling in a debunking as if it settled what the doctrine *says*."**

---

## 1. How old is it? {#dating}

*→ concept file: [ayurveda.md](../../../concepts/ayurveda.md)*

**Āyurveda** (*āyus*, "life, longevity" + *veda*, "knowledge") is the traditional Indian system of medicine. And the first thing the corpus records about it is a gap between two answers to a simple question.

| claim | source |
|---|---|
| **~5,000 years old**, traceable to the Vedas — particularly scattered plant and disease references in the **Atharvaveda** | popular and promotional literature, routinely |
| ayurvedic **terminology and concepts** appear in the **Buddhist Canon** from the mid-1st millennium BCE onward, but **"the main classical ayurveda texts are datable in their present form to the first centuries CE"** — roughly **2,000 years** | the sourced encyclopedic account |

The corpus's verdict is worth quoting because of what it declines to do: this is *"a real gap between the tradition's own self-presentation and the verifiable textual record, and it is recorded here rather than smoothed into the rounder, more marketable number."*

Two things about that gap are worth being precise on, because the crude version of this correction is also wrong.

**It is not a claim that nothing is old.** Medical terminology and concepts *do* appear in the mid-1st-millennium-BCE Buddhist Canon; the Atharvaveda *does* contain plant and disease material; and Ch. 22 §5 records that the Suśruta Saṃhitā's medical exception to *ahiṃsā* was live by ~600 CE and that the Kapiṣṭhala Kaṭha Saṃhitā carries early *paśu-ahiṃsā* material. **What is datable to the first centuries CE is the *classical texts in their present form*** — which is a claim about redaction, not about when anyone first treated an illness.

**And the distinction between "a practice is old" and "this text is old" is the same one Ch. 21 §5 had to make about the Kumbha Melā**, where a possibly-ancient festival carries a demonstrably later etiology. The recurring discipline: *the age of a tradition and the age of its account of itself are separate questions, and conflating them is how five thousand years gets asserted on the strength of a two-thousand-year-old manuscript.*

---

## 2. The two Saṃhitās {#samhitas}

*→ concept files: [charaka.md](../../../concepts/charaka.md) · [sushruta.md](../../../concepts/sushruta.md)*

Āyurveda's classical base is two large compendia with **opposite centres of gravity**, plus a later synthesis.

| | **Caraka Saṃhitā** | **Suśruta Saṃhitā** |
|---|---|---|
| emphasis | **internal medicine**; physiological and pathological theory | **surgery** |
| structure | **8 *sthānas*, 120 chapters** | **186 chapters** across six sections (five *sthānas* + the *Uttaratantra*) |
| signature content | the **tridoṣa** framework's earliest systematic treatment | 1,120 diseases, 700 medicinal plants, 64 mineral preparations, **101 blunt and 20 sharp instruments** |
| treats the other branch | surgery, **briefly** | — |

**Charaka's eight *sthānas*:** Sūtra (30 chapters — general principles, prevention), Nidāna (8 — etiology), Vimāna (8 — physician training, ethics, diet), Śarīra (8 — anatomy, embryology), Indriya (12 — diagnosis, prognosis), Cikitsā (30 — therapeutics), Kalpa (12 — pharmaceutics, toxicology), Siddhi (12 — treatment success, hygiene). Note **Vimāna**: a whole book on *physician training, ethics, and diet* sits in the middle of the compendium, which tells you the text understands itself as forming practitioners and not only cataloguing remedies.

**Suśruta's signature is surgical technique**, and it is the part of Āyurveda with the strongest external afterlife: **cadaveric dissection practice** (on gourds, dead animals, and — per one secondary source — infant cadavers submerged in river water for controlled decomposition), and **reconstructive procedures including the forehead-flap and cheek-flap rhinoplasty methods still cited as ancestral to modern plastic surgery.** That lineage claim is one of the few in this corpus where a traditional Indian technique has a documented, uncontested modern descendant.

**A third authority — the gap, and its closure.** **Vāgbhaṭa's *Aṣṭāṅga Hṛdayam*** is frequently cited alongside the two Saṃhitās as the third classical authority. When this chapter was drafted, ***vagbhata* was not a written concept node**, nor were `dhatu` and `mala`, and the chapter said so rather than writing around the absence.

✅ **All of that is now closed, and then some.** `vagbhata` is primary-covered in [Ch 29 §5.3](../../cross-tradition/29-transmission.md), where his authorship question is treated as a transmission problem — the *Aṣṭāṅgasaṅgraha*'s own colophon has one Vāgbhaṭa saying he bears his **grandfather's** name, so the tradition itself asserts at least two men. `dhatu`, `mala` and `agni-ayurveda` are primary-covered in [Ch 31](31-the-ayurvedic-body.md).

And the *commentators* have since been built out completely. The corpus now holds a named commentator for **each** of the three saṃhitās, and for the *Aṣṭāṅgahṛdaya* **both** of them — Haricandra and Jejjaṭa on Caraka, Jejjaṭa, Gayadāsa and Ḍalhaṇa on Suśruta, Aruṇadatta, Hemādri and Indu on Vāgbhaṭa, with Candraṭa alongside. They are the subject of **[Ch 35 — Dating a Literature Without Dates](35-dating-a-literature-without-dates.md)**, which also shows why this chapter's picture of the saṃhitās as stable objects needs one qualification: they are stable **as printed**, and at *Aṣṭāṅgahṛdaya* Ci. 19.98 two commentators print **different deities**.

**An unresolved internal disagreement, recorded and not adjudicated:** **Suśruta enumerates 300 bones; Charaka enumerates 360.** A flat numerical contradiction between the tradition's two foundational texts, unresolved in the sources consulted. Ch. 21's churning-*ratna* lists varied by text; here two anatomies do. It is the same evidential situation and deserves the same treatment — **record the divergence, do not average it.**

**Their relative chronology is unresolved.** Neither file will say which came first.

---

## 3. Two authorship problems, two different shapes {#authorship}

Both name-files are `contested`, and the contests are **not the same contest** — which makes them a useful pair.

### 3.1 Charaka — a person, or a lineage? {#charaka}

The *Caraka Saṃhitā* **records its own redaction history**, which is unusual and useful:

| layer | who | what happened |
|---|---|---|
| 1 | **Agniveśa**, under Ātreya's teaching | composed the original *Agniveśa Saṃhitā* |
| 2 | **Charaka** | revised and renamed it, **ca. 100 BCE–200 CE** (Meulenbeld's range) |
| 3 | **Dṛḍhabala**, ca. **6th c. CE** | rewrote a lost third of the book; **added all 17 chapters of the closing Cikitsā section plus the entire Kalpa and Siddhi sthānas** |

**And the surviving text depends entirely on Dṛḍhabala's recension — no earlier manuscript layer survives independently.** Which is precisely why *"Charaka' cannot straightforwardly mean 'the one author of this book.'"* A sixth-century redactor supplied a large fraction of what we read, and there is no earlier witness to check him against.

**The contest proper:** Chattopadhyay's position, reported through the sources, is that ***"charaka does not refer to one person but a lineage or sect of people"*** — and the word *caraka* has an independent Sanskrit sense of **"wandering (physician or ascetic)."** Against that stands the traditional reading, which the bulk of popular and medical-history literature follows: Charaka as an individual, the **"Father of Indian Medicine,"** flourishing in a narrow window (Meulenbeld: not later than ~150–200 CE, not much earlier than ~100 BCE).

Note the shape: **an occupational common noun that may have hardened into a proper name.** Compare Ch. 21 §6.2's restraint on *bali* — attested as "offering, gift" before it names a king, with the direction of derivation left unconfirmed. The same discipline applies here, and the corpus applies it.

### 3.2 Suśruta — a tradition-name, and a frame the oldest manuscripts lack {#sushruta}

Meulenbeld's assessment is blunt: ***"the text of the Suśrutasaṃhitā does not warrant that the one who composed it was a Sushruta."*** The proposed resolution is that **"Sushruta" functions as a tradition-name, comparable to "Hippocrates,"** rather than as a single historical author — a compiler organised earlier material and attributed it.

**And the manuscripts themselves disagree about to whom:**

| framing | which manuscripts |
|---|---|
| the work is **Dhanvantari's** teaching to a group of physicians including Sushruta | **printed editions** |
| the work is ascribed **directly to King Divodāsa** | **the oldest manuscripts, which omit the Dhanvantari frame entirely** |

**The divine attribution is the later layer.** The printed editions everyone reads carry a frame the earliest witnesses do not have — which is exactly the stratigraphic situation Ch. 19 §6.2 found in the Rāmāyaṇa, where **Rāma's identification as Viṣṇu is concentrated in the two interpolated kāṇḍas.** In both cases a text acquired a divine frame it did not originally carry, and in both cases the modern reader meets the framed version by default. (Ch. 21 §5 records the Dhanvantari/Divodāsa relation from the deity's side, where the open question is whether the Kāśī king *is* the descended god or a separate figure in his lineage.)

**Dating is genuinely wide** — proposals *"ranging from 2000 BCE to the sixth century CE"* — with the **3rd–4th centuries CE** as the most widely accepted modern consensus for the final recension. Meulenbeld's layered analysis (1999–2002) puts the **earliest layers in the last pre-Christian centuries**, with a later redactor adding the closing *Uttaratantra* — **structurally the same multi-layer pattern as Charaka, with different layers and different redactor names.**

### 3.3 The pattern, and where this corpus has met it before {#pattern}

Set the two beside Ch. 19 §7:

| figure | the corpus's verdict |
|---|---|
| **Vyāsa** | a **role-title** for the Veda-compiler, discharged across ages and editors — the tradition says so itself |
| **Vālmīki** | a **founding-poet figure**; datable text-stages, undatable person |
| **Bādarāyaṇa** | authorship converged, **identity contested**; anchors a text redacted across ~650 years |
| **Charaka** | possibly **a lineage or sect**, not a person; the surviving text is a 6th-c. recension |
| **Suśruta** | a **tradition-name, "comparable to Hippocrates"**; the oldest manuscripts attribute the work elsewhere |

**Five great attributions, five dissolutions, across two completely different genres.** Ch. 19 found the pattern in scripture and epic and explained it by the status of authorlessness in that textual culture: where *apauruṣeyatva* is the highest credential, an attributed name marks **lineage and authority**, not composition.

**Āyurveda has no *apauruṣeya* doctrine — and the pattern holds anyway.** That is worth noticing, because it means the explanation cannot be purely theological. A **medical** tradition, with no stake in scriptural authorlessness, produced the same phenomenon: multi-century redacted compendia carrying the name of a founder-figure who functions as a **school-marker**. Which suggests the driver is at least partly the *transmission mechanics* of long compiled technical literature — the same conditions that made the Brahmasūtra's ~555 sūtras a school-generating surface (Ch. 19 §5) — rather than a doctrine about revelation.

---

## 4. Tridoṣa — the doctrine itself {#tridosha}

*→ concept file: [tridosha.md](../../../concepts/tridosha.md)*

**Tridoṣa** ("three *doṣas*") is Āyurveda's central physiological doctrine: bodily and mental function is governed by three humour-like principles, **each a combination of two of the five *mahābhūtas*** (Ch. 16 §6):

| doṣa | elements | qualities | governs |
|---|---|---|---|
| **Vāta** | ākāśa (space) + vāyu (air) | dry, light, cold, rough, subtle, **mobile** | **movement**, communication |
| **Pitta** | tejas/agni (fire) + ap (water) | hot, sharp, light, liquid, oily | **digestion, metabolism, transformation** |
| **Kapha** | ap (water) + pṛthvī (earth) | heavy, slow, cool, dense, soft, **stable** | **structure, cohesion, lubrication** |

> **The etymology corrects the standard mistranslation, and it matters.** *Doṣa* derives from the root ***duṣ*, "to become disturbed, spoiled."** The doṣas are named **for their capacity to go *out* of balance — not for being intrinsically harmful.** In balance they are *the very principles that sustain the body*. So rendering *tridoṣa* as "the three humours" or, worse, "the three faults" imports a pathology into a term that names three **constitutive** functions under the aspect of their liability to disturbance. Movement, transformation, and structure are not defects.
>
> The concept file adds the lexical caution this corpus applies everywhere: Monier-Williams glosses the individual terms consistently (*kapha* as "phlegm, watery froth"), **but the technical tridoṣa-as-system sense is an Āyurveda-specific narrowing beyond the lexicon's bare entries** — "the same lexicon-vs-commentary pattern seen throughout this corpus's Sanskrit terms" (charter §4, signal 3: etymology is a clue, not a verdict).

**Textual home.** The theory *"follows from the first chapter of the earliest text on Ayurveda, the Charaka Samhita"* — the Sūtrasthāna gives it its earliest and most systematic treatment. The Suśruta Saṃhitā and Vāgbhaṭa's *Aṣṭāṅga Hṛdayam* also expound it, **with detailed variation across the three in emphasis and elaboration.**

> ⚠️ **An open item, stated because it was promised and not delivered.** That three-way comparison — how Charaka, Suśruta, and Vāgbhaṭa each elaborate tridoṣa — is *"its own subject of scholarly study,"* and the corpus **located two comparative review papers and could not read either**: both returned unparseable binary content through the fetch tool. So **this chapter cannot tell you how the three classical authorities differ on the doctrine**, only that they do and that specialists treat the difference as substantive. A future session with working PDF extraction could close it.

**Prakṛti — the individual constitution.** An individual's **fixed doṣa-ratio at conception** is their ***prakṛti***; their fluctuating current state is ***vikṛti***. Diagnosis and treatment aim to keep the second in equilibrium with the first. That is the clinical core of the system: **the target is not a universal norm but *this patient's* baseline.**

---

## 5. Two conflations that Sāṃkhya vocabulary generates {#conflations}

Āyurveda borrows heavily from Sāṃkhya's technical vocabulary (Ch. 15) — the *mahābhūtas*, *prakṛti*, the three *guṇas* — and the borrowing produces two standing confusions, both typed in the corpus.

> ⚠️ **Āyurvedic *prakṛti* ≠ Sāṃkhya *prakṛti*.** Same Sanskrit word, two entirely different referents:
>
> | | Āyurvedic *prakṛti* | Sāṃkhya *prakṛti* |
> |---|---|---|
> | what it is | **an individual's fixed doṣa-constitution**, set at conception | **primal cosmic matter**, the source of all manifestation |
> | scale | one person | the universe |
> | discipline | clinical typology | the metaphysical first principle of a *darśana* |
>
> The concept file names the failure mode exactly: *"popular yoga/wellness literature frequently blurs 'your Ayurvedic constitution' into 'cosmic Prakṛti' as though they were the same concept at different scales."* **They are not the same concept at different scales.** They are two uses of one word — and the blur is attractive precisely because it promises that a questionnaire about your digestion tells you something about the structure of reality.

> ⚠️ **The doṣa scheme ≠ the guṇa scheme — there are *two* classificatory layers, not one.** Charaka and Suśruta additionally classify individuals into **seven types by *guṇa*-dominance** (sattva / rajas / tamas), layering a **second** Sāṃkhya-vocabulary scheme over the doṣa-based one. Popular wellness literature runs them together as a single system. The corpus's formulation: *"two distinct classificatory layers over the same person, one physiological (doṣa) and one psychological (guṇa)."*
>
> And Charaka's use of sattva/rajas/tamas for **personality typing** is *"a psychological application of Sāṃkhya-style vocabulary, not the Sāṃkhya metaphysical claim itself"* — the guṇas in Sāṃkhya are the universal constituents of prakṛti (Ch. 15), not a temperament chart.

**Both conflations run the same way**: a term with a precise clinical sense is inflated into the cosmological sense of the same word from a neighbouring system. That is the §0 failure mode operating *inside* Indian thought rather than between it and modern physics — which is worth registering, because it shows the failure is not specifically a Western or a modern one. **It is what happens whenever two systems share vocabulary and one of them is grander.**

---

## 6. Dhanvantari — a religious frame, correctly labelled {#dhanvantari}

*→ concept file: [dhanvantari.md](../../../concepts/dhanvantari.md) — primary in Ch. 21 §5*

**Dhanvantari** is venerated as Āyurveda's patron and founding deity: the physician of the gods who **rises last from the churning of the ocean bearing the pot of *amṛta*** (Ch. 21 §5), and who has a parallel earthly tradition as **a king of Kāśī, ancestor of Divodāsa** — the same Divodāsa to whom the oldest Suśruta manuscripts attribute the surgical compendium (§3.2).

The corpus's label on this is exactly right and worth stating plainly: it is *"a mythic-religious framing, not a claim about textual authorship or historical origin."*

**This is a small point that does a lot of work.** A tradition can have a patron deity, a founding myth, and a divine attribution frame **without any of that bearing on when its texts were compiled or by whom.** Keeping the two registers apart is what lets §1's dating discussion and §3's authorship discussion proceed without either insulting the tradition's self-understanding or being captured by it. The god is real *as a religious fact about Āyurveda*; he is not evidence *about the Saṃhitās*.

---

## 7. The method problem: where the sources disagree about how careful to be {#rigor}

This is the most methodologically interesting thing in the cluster, and the corpus caught it by accident.

Researching Suśruta produced **two peer-reviewed-adjacent sources that flatly disagree — not about facts, but about how much uncertainty to acknowledge:**

| source | what it says |
|---|---|
| the **Meulenbeld-sourced philological account** | attribution unwarranted; "Sushruta" likely a tradition-name; dating proposals span 2000 BCE–6th c. CE; consensus 3rd–4th c. CE for the final recension |
| a **PMC medical-history article** | Sushruta at **"~600 BCE," flatly, with no historiographical caveat** — and **no mention of the person-vs-tradition-name question at all** |

The PMC piece is peer-reviewed and **independently corroborates the technical content** — the rhinoplasty, otoplasty, and cheiloplasty procedures, the instrument counts. On surgery it is a good source. On history it asserts a date and a person that the specialist literature does not support, and does not signal that anything is in dispute.

**What the corpus did with it is the point.** It did **not** discard the less careful source, and it did **not** average the two into a middle date. It **recorded the divergence itself as a finding**: *"a genuine split between medical-history popularization and Indological philology, not smoothed over"* — and used the PMC article *"specifically to document the divergence from the philological consensus, not as an independent confirmation of the date."*

**Three lessons generalise well beyond Āyurveda.**

**First: peer review is domain-specific.** A surgical journal reviews surgical claims. Its reviewers are not positioned to catch an unsupported dating claim about a Sanskrit manuscript tradition, and there is no reason they should be. **"Peer-reviewed" is not a single quality level** — it is a claim about scrutiny *within a field*, and a paper can be simultaneously authoritative on its subject and careless outside it.

**Second: a source's *rigor profile* is itself data.** That the "600 BCE, real individual" framing is *"common in medical/surgical literature and coexists uneasily with the philological consensus"* is a fact about how this tradition is transmitted into modern professional discourse — and it explains, in part, where the popular certainty about Āyurveda's antiquity (§1) is maintained.

**Third: this is the two-signal convergence rule doing real work.** Charter §4 requires signals to be *genuinely independent* and warns that copies are not confirmation. Here the danger was subtler than copying: two sources genuinely independent, agreeing on content, **and differing in epistemic standards.** Treating that as convergence would have laundered an uncaveated date through the corroboration of an unrelated claim. The corpus's rule — take the term, leave the editorialising (§4) — extends to: **take the surgery, leave the chronology.**

---

## 8. The external verdict, and how this project holds it {#modern}

Āyurveda is the one tradition in this corpus about which a modern empirical discipline has a direct, unfavourable, and well-evidenced verdict. The corpus records it without softening:

- contemporary critics hold that the doṣas **"are not real, but are a fictional concept"**;
- **there is no evidence Āyurveda can treat or cure cancer**;
- some ***rasaśāstra*** (mineral- and metal-based) preparations **have been found to contain toxic levels of lead, mercury, and arsenic**;
- Harriet Hall's comparison of **doṣa-typing to horoscopes** is quoted directly in the source material.

The third item is not a philosophical objection — it is a live safety finding about products sold now, and it belongs in any honest account.

**And then the corpus does something careful with all of it.** The scientific assessment is recorded as *"the mainstream secular-scholarly assessment, distinct from and not overriding the internal, source-grounded account of what the tridoṣa theory *claims*."* The full formulation, from [tridosha.md](../../../concepts/tridosha.md), is the sentence this chapter was organised around:

> ***"§0's 'analogy is not identity' cuts both ways: neither smuggling in a physics validation nor smuggling in a debunking as if it settled what the doctrine says."***

**Two distinct questions, kept apart:**

| question | who answers it | this corpus's job |
|---|---|---|
| **What does tridoṣa theory claim?** | the Saṃhitās and their commentators | **to state it accurately** — §4 |
| **Is it true of bodies?** | clinical evidence | **to report the verdict, not to adjudicate it** — this section |

This is the same discipline the corpus applied to **Naṭarāja and CERN** (Ch. 18 §4.2), and it is worth seeing that it runs in *both* directions. There the failure mode was **inflation** — reading particle physics into a Śaiva icon. Here the available failure mode is **deflation** — letting "the doṣas aren't real" stand in for an account of what the doṣas were held to *do*, and thereby never learning the system at all.

**Both failures share a structure: they let a modern verdict substitute for a description.** §0 exists to prevent the first. It equally prevents the second — and Āyurveda is the chapter where that becomes visible, because it is the only tradition here where the modern verdict is negative rather than irrelevant.

---

## 9. Transmission — and how little of it has been read {#transmission}

The Suśruta Saṃhitā travelled unusually far:

- **Arabic**, in early **8th-century Baghdad** under **Barmakid patronage** — the *Kitāb Shāh Shūn al-Hindī*;
- into **Tibetan** medical literature;
- known to the Cambodian king **Yaśovarman I** (r. 889–900 CE);
- first complete **English** translation: **Kaviraj Kunja Lal Bhishagratna**, three volumes, **1907–1916** — later judged limited in its medical-terminology choices; **P. V. Sharma** produced an alternative in 1999.

For Charaka: the modern Sanskrit edition rests on **Chakrapāṇidatta's 11th-c. commentary**, with **P. V. Sharma's English translation (1981–1994)**.

> **One statistic deserves to end this section.** **Printed editions of the Suśruta Saṃhitā have historically drawn on only about 10% of the 230+ surviving manuscripts.**
>
> Take that seriously alongside §3.2. The **Dhanvantari frame is in the printed editions and absent from the oldest manuscripts** — and the printed editions represent a tenth of what survives. So the text that circulates, gets translated, and is cited in medical-history papers is a **narrow and demonstrably non-earliest selection** from a large manuscript tradition that has mostly not been collated. Ch. 19's sourcing notes recorded that the BORI and Baroda critical editions **exist and were not fetched**; here the situation is a stage worse — **for Suśruta, the critical work itself is largely undone.** Any confidence about this text's contents should be sized to that.

---

## 10. Flags {#flags}

| flag | why the resemblance is tempting | why it fails |
|---|---|---|
| **Āyurvedic *prakṛti* ≠ Sāṃkhya *prakṛti*** | identical word; both are "your nature"/"nature" | **an individual's clinical doṣa-baseline** vs **primal cosmic matter**, the first principle of a different darśana |
| **doṣa scheme ≠ guṇa scheme** | both classify persons, both in Sāṃkhya vocabulary | **two distinct layers** over the same person — physiological (doṣa) and psychological (guṇa) |
| **Charaka's guṇa-typology ≠ Sāṃkhya's guṇas** | same sattva/rajas/tamas triad | a **psychological application of the vocabulary**, not the metaphysical claim that guṇas constitute prakṛti |
| ***tridoṣa* ≠ "the three faults"** | *duṣ* means "spoiled" | named for the **capacity to be disturbed**; in balance they are what **sustains** the body |
| **"5,000 years old" ≠ the textual record** | Vedic plant/disease references are genuinely ancient | the **classical texts in their present form** date to the first centuries CE — practice-age and text-age are different questions |
| **Dhanvantari's patronage ≠ evidence about the texts** | he is Āyurveda's founding deity | **a mythic-religious framing**, not a claim about authorship or date |
| **"Sushruta" and "Charaka" ≠ authors** *(contested)* | the texts bear their names | **a tradition-name "comparable to Hippocrates"**; and possibly **a lineage or sect**, not a person |
| **peer-reviewed ≠ uniformly reliable** | the PMC article is peer-reviewed and correct on surgery | **domain-specific scrutiny** — it asserts an uncaveated date the philological literature does not support |
| **printed Suśruta ≠ the manuscript tradition** | printed editions are what everyone reads | **~10% of 230+ manuscripts**, and the Dhanvantari frame they carry is **absent from the oldest** |
| **a negative modern verdict ≠ a description** | the clinical assessment is real and unfavourable | it answers *"is it true?"*, not *"what does it claim?"* — **the debunking no more settles the doctrine's content than a validation would** |

---

## 11. Check yourself {#check}

1. Give both answers to "how old is Āyurveda," and state precisely what *is* datable to the first centuries CE. Why is "the practice is old" compatible with "the texts are not"?
2. Contrast the two Saṃhitās on emphasis and structure. What does the presence of the **Vimāna sthāna** tell you about how the Caraka Saṃhitā understands its own purpose?
3. Suśruta says 300 bones; Charaka says 360. What is the right treatment of that in a corpus like this, and why is averaging wrong?
4. Set out Charaka's three redaction layers. Why does Dṛḍhabala's role make "Charaka wrote this book" untenable even before Chattopadhyay's thesis?
5. State Chattopadhyay's "lineage not person" argument, including the lexical point about *caraka*. What comparable restraint did Ch. 21 apply to the name *bali*?
6. The oldest Suśruta manuscripts omit the Dhanvantari frame. Name the earlier chapter that found the identical stratigraphic pattern in a different text, and say what both cases have in common.
7. Ch. 19 explained the Vyāsa/Vālmīki/Bādarāyaṇa pattern by the status of authorlessness in scriptural culture. Āyurveda has no *apauruṣeya* doctrine and shows the same pattern. **What does that do to the explanation?**
8. Why does the *duṣ* etymology make "the three faults" a mistranslation? What does it get wrong about what the doṣas *are*?
9. Distinguish *prakṛti* from *vikṛti* in Āyurvedic diagnosis. Why does that make the clinical target patient-relative rather than a universal norm?
10. Explain why "your Ayurvedic constitution is cosmic Prakṛti at a smaller scale" is wrong — and why the error is *attractive*.
11. The two Sāṃkhya-vocabulary conflations in §5 run inside Indian thought, not between it and modern science. What does that show about the §0 failure mode?
12. A peer-reviewed medical article gives an uncaveated 600 BCE date. The corpus neither discarded it nor averaged it. What did it do, and why is that the right move?
13. "Peer-reviewed is not a single quality level." Unpack that using the PMC case. What was the source good for, and what was it not good for?
14. Give the corpus's formulation of how §0 "cuts both ways." Then state the two questions it separates, and who answers each.
15. Compare this chapter's method problem with Ch. 18 §4.2's Naṭarāja/CERN flag. What structure do inflation and deflation share?
16. Printed Suśruta editions draw on ~10% of surviving manuscripts, and carry a frame the oldest ones lack. What does that imply about the confidence any claim about this text's contents can carry?
17. In one paragraph: this chapter reports a negative external verdict on the tradition it describes. How can a project whose directive is to understand traditions *on their own terms* do that without either endorsing or debunking?

---

*Medium confidence throughout, with the gaps named rather than averaged: **Meulenbeld's *History of Indian Medical Literature* was never fetched** (all dating claims run through summaries of it), **Britannica returned HTTP 403** on both Charaka pages, **two comparative tridoṣa review papers were unreadable**, and the umbrella file's signals all trace to one platform. For the deepest treatments: the 5,000-vs-2,000-year gap, the *prakṛti* conflation, and the modern scientific assessment → [ayurveda.md](../../../concepts/ayurveda.md); the three redaction layers, Chattopadhyay's lineage thesis, and the eight *sthānas* → [charaka.md](../../../concepts/charaka.md); Meulenbeld's attribution verdict, the Dhanvantari/Divodāsa manuscript split, the surgical content, and the PMC rigor-divergence → [sushruta.md](../../../concepts/sushruta.md); the *duṣ* etymology, the elemental pairings, and the unread comparative sources → [tridosha.md](../../../concepts/tridosha.md); the patron deity in his churning role → [dhanvantari.md](../../../concepts/dhanvantari.md) (Ch. 21 §5). The *pañcamahābhūta* scheme → Ch. 16 §6; Sāṃkhya *prakṛti* and the guṇas → Ch. 15; the authorship pattern this chapter extends → Ch. 19 §7.*

*~~`vagbhata` and `dhatu`/`mala` are **unwritten concept nodes**~~ — **CLOSED (Batch 42); §2 above rewritten to point at them (Batch 45).** All three now exist, plus `agni-ayurveda` as a §8 tradition-split from the Vedic deity. **`dhatu`, `mala` and `agni-ayurveda` are primary-covered in [Ch 31, The Body as a Rate](31-the-ayurvedic-body.md)**, and **`vagbhata` in [Ch 29 §5.3](../../cross-tradition/29-transmission.md)**, where his authorship question is treated as a transmission problem. §"A third authority" above has now been rewritten accordingly (Batch 45), and additionally points at Ch 35, which covers the seven commentators.*

*Next: **Ch. 24 — The Later Neoplatonists** (`comparanda/`), the last cluster of written nodes without a chapter home.*
