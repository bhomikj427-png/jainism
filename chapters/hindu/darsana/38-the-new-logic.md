# Chapter 38 — The New Logic: What Navya-Nyāya Was Actually For

> **Primary concepts:** `navya-nyāya` · `gaṅgeśa` · `tattvacintāmaṇi` · `avacchedaka` · `abhāva` · `raghunātha-śiromaṇi` · `gadādhara`
> **Folder:** `hindu/darsana/` — this is one school, developing in one line, for four centuries.
> **Reads after:** [Ch 16 (Nyāya & Vaiśeṣika)](16-nyaya-vaisheshika.md), which ends with Praśastapāda, and [Ch 37 (The Dialecticians)](../../cross-tradition/37-the-dialecticians.md), whose §3 is Udayana — the man this chapter begins from.

---

## How to use this chapter

Until Batch 46 this corpus had a hole in exactly the shape of a school. It ran the old Nyāya line — Gautama → Vātsyāyana → Praśastapāda → Vācaspati Miśra → Udayana — and then stopped, at precisely the point the tradition itself calls a new beginning. Gaṅgeśa and "Navya-Nyāya" were named in **seven concept files and three chapters**, and `tarka.md` had *Tattvacintāmaṇi (Gaṅgeśa)* sitting in its front-matter as a source text. **There was no node anywhere.**

This chapter is that school. Four things to carry out of it:

1. **What was actually new** (§3) — and it is not a metaphysics. It is a *method of definition*, a seventh category, and a piece of notation.
2. **The limitor** (§4), which is the single idea you need in order to read anything this school wrote. If you take away one technical term from this corpus, take this one.
3. **The comparison with modern logic, drawn correctly** (§7). This is the chapter's most dangerous section and the reason it exists. The school is routinely called "a calculus," "Indian formal logic," "Frege before Frege." **One of those phrases is a quotation from Ingalls and the other two are wrong**, and the difference matters.
4. **What happened to it** (§8) — a school that priced itself out of its own tradition, measurably.

⚠ **A warning specific to this chapter.** Navya-Nyāya is the part of Indian philosophy that most tempts the failure mode §0 exists to prevent. It has abstract-noun operators, scope restrictions, a theory of negation, and expressions that look like formulae; it is genuinely a precision instrument; and it is easy — and flattering to everyone — to say it "anticipated" modern logic. The two scholars who founded the Western study of it, **Ingalls** and **Matilal**, both **translate it into quantifier notation and both warn you not to stop there.** We follow them, including in the warning.

---

## 1. The seven {#cast}

| # | what | when | the work | why it is here |
|---|---|---|---|---|
| 1 | **Navya-Nyāya** | begins 11th–14th c. — **three rival answers**, §2 | — | the school itself |
| 2 | **Gaṅgeśa Upādhyāya** | *fl.* c. 1325, Mithilā | *Tattvacintāmaṇi* | the founder on the majority reading |
| 3 | **the *Tattvacintāmaṇi*** | c. 1325 | four *khaṇḍa*s | one book; **thirty commentaries in three tiers** |
| 4 | ***avacchedaka*** | — | — | **the limitor** — the device the whole notation runs on |
| 5 | ***abhāva*** | retrofitted c. 991–1050 | — | **absence as the seventh category** — and it was added later than the tradition says |
| 6 | **Raghunātha Śiromaṇi** | 1477–1547, Navadvīpa | *Dīdhiti*; *Padārthatattvanirūpaṇa* | the school's best logician, who **rejected the school's ontology** |
| 7 | **Gadādhara Bhaṭṭācārya** | 17th c., writing c. 1640–60 | *Gādādharī*; *Vyutpattivāda*; *Śaktivāda* | the end, and the measure of the difficulty |

---

## 2. When does it begin? Three answers, and they are not really rivals {#three-beginnings}

The first thing you meet in this school is a disagreement about when it started, and it spans **two and a half centuries**.

| reading | who | the criterion |
|---|---|---|
| **c. 1325, with Gaṅgeśa's *Tattvacintāmaṇi*** | Wikipedia; the textbook line; Vidyābhūṣaṇa | the **book** |
| **c. 1025–1100, with Udayana** — "Prācīnanyāya ended with him. At the same time, Navyanyāya started with him" | Debabrata Deb, *The Navya-Nyāya Theory of Pakṣatā* | the **method** |
| **"at some point in the 11th or 12th century"**, when Nyāya and Vaiśeṣika merged into one school | **Jonardon Ganeri**, SEP | the **event** |

**They are answering different questions.** Reading 1 dates the canon; readings 2 and 3 date the formation. And note that **2 and 3 converge on the eleventh century from independent criteria** — because Udayana *is* the merger: his *Kiraṇāvalī* is a commentary on the Vaiśeṣika Praśastapāda and his *Ātmatattvaviveka* is Nyāya polemic. One man working both sides, in exactly Ganeri's window.

A fourth voice, and the most authoritative: **D. H. H. Ingalls**, introducing Matilal's monograph in 1968, writes that any student of Indian philosophy "**since the time of Udayana (eleventh century), or at the very least since the time of Gaṅgeśa**, must concern himself with Navya-nyāya." **He carries both datings in one sentence and does not choose.**

> **⚠ What this cost the corpus, and the correction is instructive.** `anandabodha.md` (Batch 45) rejected a description of an 11th–12th-c. Advaitin's works as written "in the Navya-nyāya style," calling it **anachronistic** on the ground that the school begins with Gaṅgeśa in the 14th century. On readings 2 and 3 that Advaitin is a **contemporary of the school's formation**. The phrase is still declined — the aggregators give no argument for it — but **the charge of anachronism was itself resting on an unexamined periodisation.** A confident correction can be wrong in the same way as the thing it corrects.

---

## 3. What was actually new {#what-was-new}

Ganeri is explicit that Navya-Nyāya "incorporates and develops classical Vaiśeṣika metaphysics as well as classical Nyāya epistemology." **The metaphysics is inherited.** What is new is the apparatus, and it has three parts.

### 3.1 A diagnostic theory of definition

The method is old — Vātsyāyana's threefold procedure, quoted from the *Bhāṣya* before *NS* 1.1.3: ***uddeśa*** (enumeration: naming the thing), ***lakṣaṇa*** (definition: citing a characteristic that distinguishes it), ***parīkṣā*** (examination: checking, with the *pramāṇa*s, that the characteristic really does distinguish it).

What Navya-Nyāya does is **sharpen the second and take the third seriously**. A definition is any characteristic **co-extensive** with the class defined. Ganeri: it "does not tell us what the essence of the class is — it merely supplies us with a syndrome or trait." A definition fails in exactly two ways:

- ***ativyāpti*** — **over-covering**: it catches things outside the definiendum;
- ***avyāpti*** — **under-covering**: it misses things inside.

In modern terms: **necessary and sufficient**. The Naiyāyikas have, as Ganeri puts it, "a **diagnostic** rather than an **essentialist** conception of definition."

> **This is why the school reads as an endless quarrel about definitions.** It is not pedantry. A definition, so conceived, is a **falsifiable object** — you can produce a counterexample and kill it — and *checking* it is a **named stage of the official method**. A tradition that builds refutation into its procedure will generate a literature that looks like nothing but refutation.

### 3.2 A seventh category — and it was added later than the tradition says

Vaiśeṣika classifies everything into ***padārtha***s, categories. Kaṇāda's list has **six**: substance (*dravya*), quality (*guṇa*), motion (*karma*), universal (*sāmānya*), particularity (*viśeṣa*), inherence (*samavāya*). Navya-Nyāya lists **seven**, adding ***abhāva*** — **absence**.

That is the standard account. Here is what Matilal found:

> "the early Vaiśeṣikas … did **not** speak of absence as a separate category. One might very well explain the *Vaiśeṣika-sūtras* 9.1.1–10 without assuming that **Kaṇāda** was speaking here of absence as a separate category. **Praśastapāda** also did not state whether absence should be considered a separate category. **Śrīdhara** (c. 991) … and **Udayana** (c. 1050) … tried to argue that although absence had **not been mentioned** by Praśastapāda (or by Kaṇāda) as a separate *padārtha*, it was nevertheless **so approved by them implicitly**."

**The seventh category is a retrofit** — argued for, by name, at a date. Three things follow:

1. **The corpus's Vaiśeṣika files were right.** `vaiseshika-sutra.md` gives six, read verbatim from *VS* 1.1.4 with Śaṅkara Miśra's *Upaskāra*. Six is correct for the root text. The retrofit **explains** an agreement the corpus already had rather than disturbing it.
2. **It is an argument, not a corruption.** Śrīdhara and Udayana did not smuggle the category in; they claimed their predecessors had approved it *implicitly*. That is a move you can assess.
3. ⭐ **Note who, and in which book.** The retrofitter is **Udayana**, in the ***Kiraṇāvalī*** — the same man and the same work that `jati.md` runs on for universals, that `paramanu-vaisheshika.md` credits with making Īśvara the director of atomic combination, and whom §2 above names as one of the three candidate starting-points of the school. **The seventh category is installed by the man at whom, on one respectable periodisation, the "new" Nyāya begins.**

⚠ One qualification Matilal himself supplies: **Candramati's *Daśapadārthaśāstra*** is expressly excepted — an early Vaiśeṣika work with **ten** categories that did treat absence. So the claim is about the mainline *sūtra*-and-*bhāṣya* tradition, not about every early text.

### 3.3 Why absence matters more than a list-entry should

Ingalls states the stakes better than a summary can:

> "The doctrine of negation in Navya-nyāya is like a **keystone** that holds in place the interlocking voussoirs of an arch. It is essential to Navya-nyāya **metaphysics**, which hypostatizes 'absence' into a category. It is the peculiar mark of Nyāya **epistemology**, for the Nyāya insisted, **against the opposition of all other schools, that one can *see* the absence of an object in a given place**. And it is a keystone of Navya-nyāya **logic**, for in this system which presents a hierarchy of abstractions rather than a hierarchy of classes it is only by the use of negation that universal laws can be framed."

Three claims, and the middle one is a minority report held against everybody: **you walk into a room and *perceive* that the pot is not there.** Not infer — perceive. Every other school found some other route.

The apparatus: every absence is specified by what it is an absence **of** — the ***pratiyogin***, the **counterpositive** — in a locus, the ***anuyogin***. And absences come in kinds, though the tradition never agreed how many: **two** (Jayanta, reducing six to prior absence and destruction, following *NS* 2.2.12), **four** (Śrīdhara: those two plus constant absence and mutual absence), or **six**. The organising cut is not the number but **transient vs eternal** — and the eternal ones took the heaviest fire, from Mīmāṃsā: *"Water does not acquire any extra property by being the locus of the eternal absence of fire in it."*

---

## 4. The limitor {#avacchedaka}

**This is the section to read twice.** *Avacchedaka* is the device the school's technical language runs on, and every strange-looking Navya-Nyāya expression is doing what this section describes.

### 4.1 The problem

Matilal sets it out as a failure of naïve formalisation. Take two ordinary sentences:

> (1) "There is oil in sesame seeds" (*tileṣu tailam*)
> (2) "There is fire on a mountain" (*parvate vahniḥ*)

Both rephrase as "**x is a locus of y**." Their negation, by Nyāya convention, is "x is a locus of an **absence** of y." So the two forms must be **contradictory** — for any x and y, if one holds the other does not.

For sesame and oil, they are. And then:

> "**the mountain can be a locus of fire as well as of the absence of fire**."

Fire on the slope; no fire on the summit. **Both statements true, of one locus, at one time.** The formalisation has manufactured a contradiction out of an ordinary fact.

⚠ **The diagnosis was not the logicians' — it was the grammarians'.** Matilal credits **Bhartṛhari, *Vākyapadīya* III, "Adhikaraṇādhikāra," verses 2–3**, with Helārāja's commentary, for the distinction between a **pervasive** (*abhivyāpaka*) and a **partitive** (*aikadeśika*) locus. The corresponding property-side terms are ***vyāpya-vṛtti*** (occurring throughout — cow-ness is in every part of every cow) and ***avyāpya-vṛtti*** (occurring partly). **The most characteristic device in Indian logic comes out of Sanskrit grammar.** *(And this corpus has no node for Bhartṛhari or the* Vākyapadīya *— a gap recorded rather than papered over.)*

### 4.2 The repair

Keep the schemata; change the rephrasing:

> **"The mountain *as delimited by the slope* is a locus of a body of fire"** — ***nitambāvacchedena parvate vahniḥ***

The delimited sentence is no longer structurally parallel to the sesame case, so the two never collapse into one schema and **the contradiction never forms**. A limitor of this original kind is simply **a spatial part of the locus**.

The canonical case is the **monkey in the tree**, and both of the corpus's independent specialists give it:

> ***śākhāvacchedena vṛkṣaḥ kapisaṃyogī, na tu mūlāvacchedena*** — "the tree, **as delimited by the branch**, is in contact with the monkey; **not as delimited by the root**."

Ganeri draws the consequence: "Nyāya avoids the threatened violation of the law of non-contradiction by **relativising the notion of occurrence**."

### 4.3 What it is really for

The spatial case is where the device came from, not what it became. Matilal's decisive example: a blue cup sits in front of you, and you may cognise —

> "The cup is blue" · "The utensil is blue" · "The cup is coloured" · "The substance is blue" · "The substance is coloured."

**The objects are identical in all five.** Same cup, same colour. Nyāya nonetheless holds these to be **five distinct cognitions**, and can say why *only* by appeal to limitors: the qualificand-ness is limited by cup-ness in the first and third, by utensil-ness in the second, by substance-ness in the fourth and fifth; the qualifier-ness by blue-ness in the first, second and fourth, by colour-ness in the third and fifth. **Different combination, different cognition.**

> **⭐ This is the sentence to remember about the whole school.** The limitor exists because Navya-Nyāya is analysing **cognitions**, not sentences. Its analysandum is a mental episode with a structure — a principal qualificand, one or more qualifiers, and a relation — and two episodes about the same objects can still differ. **Once you know that, the notation stops looking like formalism for its own sake.**

The device then extends: to **time** (a mango is green at t₁ and red at t₂ — "x as limited by time t₁ is a locus of y," and no contradiction), and to **relations** (two cognitions with the same limiting property but different limiting *relations* are also distinct).

### 4.4 And limitorship is itself disputed

*Avacchedakatva* is defined four different ways, and Matilal lists them:

| # | account | tag |
|---|---|---|
| (i) | a ***svarūpa*** relation — **unanalysable** | — |
| (ii) | not **narrower** in extension than what it limits | *anyūna-vṛtti* |
| (iii) | neither wider nor narrower | *anyūnānatirikta-vṛtti* |
| (iv) | not **wider** than what it limits | *anatirikta-vṛtti* |

**Raghunātha "largely favored" (i) and (iv)** — and wrote a treatise on the question, the *Avacchedakatva-nirukti*. ⚠ Note that (i) says the relation cannot be analysed and (iv) analyses it; that one man preferred both "in many contexts" is recorded as reported and **not** smoothed into a single position.

---

## 5. Gaṅgeśa and the book {#gangesa}

### 5.1 The man, and a lesson about sources

Little is known. SEP: he taught in **Mithilā**, taught **both Nyāya and Mīmāṃsā**, was styled ***jagad-guru*** ("roughly equivalent to 'Distinguished University Professor'"), and had a wife, three sons and a daughter, one being the Nyāya author Vardhamāna. "About the person little more is known." The tradition adds that he was illiterate as a youth and received mastery of logic as a boon from **Kālī** on a cremation ground — hagiography, and interesting only for what it presupposes: that the *Tattvacintāmaṇi*'s difficulty seemed to **need explaining**, and that the explanation reached for was a divine gift rather than long training.

⚠⚠ **His date is the corpus's best case study in a source-failure, and it belongs in a teaching chapter.** Four values are in circulation:

| date | where |
|---|---|
| "13th cent." | a **19th-century library catalogue** record for the 1888–1901 Calcutta edition |
| "late 12th century" | a **static mirror of an older Wikipedia revision** — still live, still indexed |
| c. 1200 | Hindupedia; a Wisdomlib study |
| **first half of the 14th c.**; **D. C. Bhattacharya's 1300–1350** | **SEP**; live Wikipedia; Deb |

**These are not four opinions. They are one date, revised later, with the earlier states of the revision still in circulation** — because mirrors and aggregators do not update when their source does. Live Wikipedia says "recent opinion now places him in the fourteenth century" while a mirror of its own older text still says the twelfth.

> **The lesson generalises past this school.** A reader who samples "several independent sources" here samples **the same source at four different ages** and mistakes it for corroboration. Independence has to be checked by *provenance*, not by counting URLs. And note that only the 14th-century position has an **argument** attached: Bhattacharya's dates, Maṇikaṇṭha Miśra (c. 1300) just before him, and Matilal's placing of Śaśadhara some 150 years earlier.

*(A smaller instance, same page: two Wikipedia articles give Gaṅgeśa's village as "19 km south-east of Darbhanga" and "twelve miles southeast of Darbhanga." Those look like two witnesses. 12 miles ≈ 19.3 km.)*

### 5.2 What the *Tattvacintāmaṇi* is

Four *khaṇḍa*s, one per Nyāya knowledge-source: **perception, inference, analogy, testimony**. Three things about its construction matter:

1. **It treats only the *pramāṇa*s, and deliberately not the *prameya*s.** The *Nyāyasūtra*'s sixteen categories open with those two; this book takes the first and drops the second. **A work that declines half its inherited subject-matter is making a claim about what philosophy now is** — epistemology first, ontology only as epistemology requires it. God and the self get argued *inside the inference chapter*.
2. **Its plan is borrowed from the opposition.** One section per knowledge-source is **Dignāga's** arrangement, "copied by Gaṅgeśa." The consolidating text of the anti-Buddhist school is laid out on a Buddhist logician's outline.
3. **Its method is serial demolition.** On the definition of *vyāpti* he states candidate definitions and refutes them one after another before giving his own. ⚠ **The two best sources disagree on the count** — SEP says twenty-four rejected; Ganeri says twenty-one rejected (the first five the famous *vyāpti-pañcaka*, two more the "Lion and Tiger" definitions of his predecessors) and seven accepted. Recorded, not reconciled.

⚠ **And a story about the book that may not be true.** Wikipedia has the *Tattvacintāmaṇi* written **in answer to Śrīharṣa's *Khaṇḍanakhaṇḍakhādya*** — Gaṅgeśa judging the attack unsuccessful but accepting the need to sharpen Nyāya's tools. **SEP's full, 2024-revised entry on Gaṅgeśa never mentions Śrīharṣa.** Neither account is adopted here. But it is worth noticing that **a widely repeated explanation of why the most important book in late Indian philosophy exists is missing from the best available treatment of it.**

### 5.3 What he held

- **Knowledge is reliably produced.** SEP calls it "a reliabilist theory of knowledge and justification, indeed a **super-reliabilism, an infallibilism for externalists**." The knowledge-sources are **factive** — genuine sources are inerrant — and error is reassigned to a ***pramāṇābhāsa***, an *apparent* source, a knowledge-imitator. Nothing goes wrong *inside* a *pramāṇa*; what happens is that something that was not one looked like one.
- **Presumptive, but defeasible, and certified separately.** Awarenesses are presumed veridical; **certification is a distinct cognitive act**, achieved through success in action and by identifying the source's merits (*guṇa*) and flaws (*doṣa*). This is an **extrinsicality** position held explicitly against Mīmāṃsā's *svataḥ-prāmāṇya*. One exception: things known by ***anuvyavasāya*** (apperception) are "known without the possibility of being wrong."
- **God.** *"Earth and the like have a conscious agent as an instrumental cause, since they are effects, like a pot and unlike an atom."* Its distinctive move is a **restriction on the domain**: nothing inside the subject-class may serve as example or counterexample, "since that would beg the question." The standard objection is an *upādhi* — that the real condition is *having-a-perceptible-body*, which a creator lacks — and he answers by defending "a bodiless Creator whose knowledge is appropriate to the material forming earth," on the model of a potter's knowledge of clay.

---

## 6. Raghunātha: the best logician the school produced rejected the school's ontology {#raghunatha}

Ingalls fixes him in one word. Introducing Matilal's translations of Gaṅgeśa's *Abhāva-vāda* alongside Raghunātha's *Nañvāda*, he calls the first "the **orthodox** wing" and the second "the **radical** wing, of the Navya-Nyāya school."

He wrote the ***Dīdhiti***, the commentary on the *Tattvacintāmaṇi* that displaced every rival — after him, Naiyāyikas commented on **him** rather than on Jayadeva's *Āloka*. And he wrote the ***Padārthatattvanirūpaṇa***, a short treatise that takes the category-scheme apart:

| move | effect |
|---|---|
| identifies **time, space and *ākāśa* with God** | three of the nine substances collapse into one |
| **eliminates *manas*** by reducing it to matter | the ninth substance goes |
| ⭐ **denies atoms (*paramāṇu*) and dyads (*dvyaṇuka*)** | **rejects Vaiśeṣika atomism outright** |
| dismisses ***viśeṣa*** as unproven | removes the category the school is **named after** |
| adds **eight new categories** | *śakti*, *svatva*, *kṣaṇa*, *kāraṇatva*, *kāryatva*, *saṃkhyā*, *vaiśiṣṭya*, *viṣayatā* |

> **⚠⚠ This is the most important correction Batch 46 pushed back into the corpus, and it is a §0 correction.** Vaiśeṣika atomism is presented across this corpus as *the* school's ontology. It is more precisely **Kaṇāda's, Praśastapāda's and Udayana's**. `kanada.md` has always warned that the *paramāṇu* doctrine is "routinely inflated into 'ancient Indian atomic theory = modern physics'," on **conceptual** grounds. It now has a **historical** argument beside it: **a doctrine that the tradition's own leading later thinker discarded on metaphysical grounds is not an empirical discovery being handed forward.** Physical theories are not abandoned by their best practitioners for finding the arguments unpersuasive; metaphysical posits are.

**He also attacked the theory of universals** the corpus took from Udayana. `jati.md` runs on Udayana's six *jāti-bādhaka* exclusion criteria. Ganeri: "Some Naiyāyikas, especially **Bhāsarvajña and Raghunātha**, reject the 'cross-connection' impediment, pointing out the problems … (e.g. redness and greenness overlap, as do pothood and goldhood). **Raghunātha suggests that consistent application of this principle would eliminate virtually all universals from the ontology.**" An internal *reductio*: apply the rule honestly and the furniture disappears.

**And a genuine philosophical invention, on number.** Consider:

> (1) "The table has wooden legs." (2) "The table has four legs."

(1) entails "each leg is wooden." (2) does **not** entail "each leg is four." So four-hood cannot inhere in the legs the way wooden-ness does. Raghunātha postulates a new relation, ***paryāpti*** — **"completion"** — relating the property to the four legs **jointly and not severally**, and calls it "a special kind of self-linking relation." His commentator **Jagadīśa** glosses: completion "relates the property two-hood **by delimiting it** as a property which resides in both pots. Otherwise, it would follow that there is no difference between saying 'These are two' and 'Each one possesses two-hood'."

⚠ **A loose end kept visible.** The reported lists have "number" among the things he **eliminates** *and* among the eight he **adds**. The likely reconciliation — he removes it from the *guṇa*s, where it would have to inhere severally, and reinstalls it as a *padārtha* related jointly by *paryāpti* — is supported by the *paryāpti* material but **stated by no source**. It is marked in `raghunatha-siromani.md` as a hypothesis. **Potter's 1957 translation would settle it in a page, and it was not read.**

---

## 7. The comparison with modern logic — how to draw it {#comparison}

This is the section the chapter exists for.

### 7.1 What is genuinely there

**Two specialists, decades apart, working on different technical problems, reach the same structural claim.**

- **Matilal**, on limitorship: accounts (ii)–(iv) hold that it is "**definable in terms of the 'primitive' occurrence relation**," while (i) holds it unanalysable. He then renders (ii)–(iv) in quantifier notation over a predicate *Oxy*, "x occurs in y."
- **Ganeri**, on Gaṅgeśa's definition of *vyāpti*, asks the obvious question — since pervasion just means "all H are S," why did the Naiyāyikas not simply use universal quantification? — and answers:

> "The answer, perhaps, is that they were in fact **trying to define this notion**, and to do so only in terms of certain other notions which they took to be primitive, especially the notion of **co-location and absence**."

> **⭐ This reframes everything.** The *vyāpti* literature is **not** a long, clumsy approach to a quantifier the Naiyāyikas lacked. It is an **analysis of that quantifier into two primitives** — being in the same locus, and not being there — chosen because a Nyāya ontology **contains loci and absences** and does **not** contain variables and binders. Where the lazy reading says "they were reaching for ∀ and kept missing," the accurate statement is: **they were asking what ∀ is made of, in a metaphysics where the answer had to be made of things.**

You can watch it work. To say *all* pots are absent from a place, Nyāya does not quantify; it **delimits an abstract**: ***ghaṭatvāvacchinna-pratiyogitā***, "a counterpositive-ness delimited by pot-ness." Matilal: "In this way, generality of statements was maintained." And it **scopes**: make the limitor pot-ness alone and the absence concerns all pots; add blue-colour and it concerns only blue pots. That is restricted quantification, performed by adding a limitor.

### 7.2 What is not there, in Ingalls's own words

> "in this system which presents a **hierarchy of abstractions rather than a hierarchy of classes** it is only by the use of negation that universal laws can be framed. **There is an absence of occurrence of humanity in such a locus as is not a locus of mortality. That is to say, all men are mortal.**"

**"All men are mortal" is not, here, a sentence about a class of men. It is a claim about a locus where a property fails to occur.** Ingalls's instruction to the expositor is to "translate from system to system" — to render arguments "phrased in an **intensional logic of abstractions**" into ones "phrased in an **extensional logic of classes and propositions**" — while insisting he "should warn the reader of **ultimate incompatibilities**."

So, precisely:

| claim | verdict |
|---|---|
| Navya-Nyāya is a **formal calculus** / a symbolic logic | **No.** No axioms, no derivation rules, no formal semantics. The one specialist assessment reaching this corpus **declines the word "calculus"** and offers "a precision logic" instead |
| It is **Indian formal logic**, comparable to the syllogistic | **No** — and the mismatch is deeper than notation. Syllogistic is about valid **forms of sentences**; this is about the structure of **cognitions**, which is why §4.3's five blue-cup awarenesses are five and not one |
| It is a **precision vocabulary** with genuine scope-management and a worked theory of negation | **Yes**, and that is a large claim, not a consolation prize |
| It anticipated **Frege** | Ingalls is quoted as calling it "the most precise calculus of properties produced before Frege." ⚠ **That quotation reaches this corpus only through a paper that quotes it in order to disagree with it**, and Ingalls's *Materials* was not read. Treat it as a reported assessment with its reporter's dissent attached |

### 7.3 The comparison that actually pays: the monkey and the contradiction

The *kapi-saṃyoga* case looks like the standard motivation for a **paraconsistent** logic: two apparently contradictory statements about one locus, both true.

**Navya-Nyāya's answer is the opposite of paraconsistency's.** A paraconsistent logic weakens *ex falso* so that a contradiction can be **tolerated** without explosion. Nyāya **denies that there is a contradiction** — the two occurrences carry different delimitors and were never about the same thing. **Non-contradiction is preserved, not relaxed.**

The same discipline applies to **many-valued** logic. *Avyāpya-vṛtti* — partial occurrence — is a fact about **where in an object a property sits**, not about how true a proposition is. There is no third value and no degree of truth. Reading one in is exactly the substitution §0 exists to prevent.

> **The rule to carry away**: when Navya-Nyāya meets a problem that modern logic also meets, note the shared problem and then **look at the repair**. The repairs are usually different, and the difference is the finding.

---

## 8. The end: a school that priced itself out {#the-end}

### 8.1 The object of study migrates upward

One book generated **thirty commentaries**, and they come in **tiers**:

| tier | commenting on | who |
|---|---|---|
| 1 | the *Tattvacintāmaṇi* | *Dīdhiti* (Raghunātha) · *Āloka* (Jayadeva/Pakṣadhara) · *Prakāśa* (**Vardhamāna, Gaṅgeśa's own son**) · Rucidatta · Śaṅkara Miśra · **Vācaspati Miśra** |
| 2 | the ***Dīdhiti*** | Mathurānātha · Jagadīśa (*Jāgadīśī*) · **Gadādhara** (*Gādādharī*) · Bhavānanda · Harirāma · Raghudeva |
| 3 | the ***Āloka*** | *Āloka-viveka* (Jayarāma), and others |

And the live front **moves up**: "after Raghunātha, many Navyanaiyāyikas commented on the *Dīdhiti* rather than Jayadeva's *Āloka*." **By the 17th century the text being argued over is a commentary on a commentary.**

*(⚠ A useful accident in that tier-1 list: an* Anumāna-khaṇḍa *commentary by "Vācaspati Miśra." A commentary on Gaṅgeśa cannot be by the* Bhāmatī *author, four centuries earlier. This independently confirms the **Vācaspati Miśra I / II** collision `vacaspati-mishra.md` logged in Batch 45 — from a commentary census that had never heard of the problem.)*

### 8.2 The measure

**Gadādhara Bhaṭṭācārya** (17th c., writing c. 1640–60, Bengal) is the last great systematiser. His *Gādādharī* is a commentary on Raghunātha's *Dīdhiti* — **tier 2**. His contributions "overshadowed those of the earlier Nyāya scholars Jagadīśa Tarkālaṅkāra and Bhavānanda." He is credited by tradition with 64 further books; five or six survive.

⚠ **Note where his two independent treatises point.** The *Vyutpattivāda* is on **sentence**-meaning and *saṃsargamaryādā*; the *Śaktivāda* on **word**-meaning — *pada*, *padārtha*, *padavṛtti*. **The school that narrowed for three centuries onto the inference chapter produced, at its end, its most sustained original work on semantics.**

And here is the measure of what had happened. By the 17th–18th centuries the idiom "made it increasingly inaccessible, and so … several manuals or compendia were written to explain in simplified language the basic tenets of the school." The most successful is Annaṃbhaṭṭa's *Tarkasaṅgraha*, and it was nicknamed:

> ***Bāla-gādādharī*** — "a sort of **'Beginner's Guide to Gadādhara'**."

> **A school whose introductory textbook is named after a third-tier commentator has made its own most recent master the thing one is introduced *to*.** That is the most precise available statement of what happened to this literature — and, read alongside §8.1, it is the same fact twice: the object of study kept climbing, until the bottom of the ladder had to be rebuilt.

---

## 9. What this chapter leaves open {#open}

Stated plainly, because the corpus's rule is that unread things are named:

1. **Not one line of Navya-Nyāya Sanskrit was read.** Everything here is exposition of exposition — with one partial exception: Matilal's 1968 monograph, read at first hand, **contains English translations of Gaṅgeśa's *Abhāva-vāda* and Raghunātha's *Nañvāda* with the Sanskrit appended**, and those were **sampled, not worked through**. The corpus has a published scholarly translation of part of its primary text within reach and has not yet used it.
2. **S. Phillips's complete English translation of the *Tattvacintāmaṇi*** (3 vols, Bloomsbury, 2020) exists and was not consulted. It is the single highest-value unread item in this layer.
3. **Potter's 1957 text-and-translation of the *Padārthatattvanirūpaṇa*** would settle what "denies atoms" actually amounts to, and the number contradiction in §6.
4. **Ingalls's *Materials* (1951)** — the source of the Frege comparison, reached here only through a paper that disputes it.
5. **A Bhartṛhari / *Vākyapadīya* node.** §4.1 shows the school's signature device has grammatical ancestry, and the corpus has no node for the grammatical tradition at all.
6. **D. C. Bhattacharyya, *History of Navya-Nyāya in Mithilā*** — wanted now by `udayana.md`, `gangesha.md` and `prashastapada.md`, and possibly by the Āyurveda layer too (Ch 39 §6).
