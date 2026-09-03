# Chapter 47 — What a Name Can and Cannot Tell You

> **Primary concepts:** `vyāḍi` · `śākaṭāyana` · `śākaṭāyana (pālyakīrti, jain)` · `devanandin (pūjyapāda)` · `jainendra vyākaraṇa` · `candrakīrti` · `maitreya rakṣita`
> **Folder:** `cross-tradition/` — continuing [Ch 29](29-transmission.md), [Ch 34](34-the-commentator.md), [Ch 39](39-filling-in-the-blanks.md), [Ch 45](45-the-witness-problem.md) and [Ch 46](46-opening-the-book.md). The seven nodes span Brahminical grammar, Digambara and Yāpanīya Jainism, and Madhyamaka Buddhism; **what holds them together is not a tradition but a kind of evidence.**
> **Reads after:** [Ch 45](45-the-witness-problem.md) and [Ch 46](46-opening-the-book.md). It **corrects Ch 45's** picture of the eastern school, and it **corrects four concept files** outside this batch — including two Buddhist ones written in Batch 12.

---

## How to use this chapter

For eleven batches this corpus has been collecting **name collisions**: cases where one label turns out to cover several people. It has a taxonomy — seven generators, seventeen numbered candidates — and it has been getting steadily better at spotting them.

**This batch inverted the exercise.** Every one of its seven nodes turned on a name, and in four of them the corpus found that **it had been the one making the mistake**, not the tradition. So the chapter is not another catalogue entry. It is an attempt to say **what a name is actually evidence for**, and to be honest about how much of this corpus's own structure was built on inferences from names without saying so.

Six things to carry out:

1. **An eighth generator, and it is nobody's error.** A *patronymic* is a label whose normal semantics is that many people bear it. Two men called Śākaṭāyana are not a confusion — they are the word working correctly. (§1)
2. **The corpus's most-cited author had no node, because it did not recognise his name.** Fifty-eight files cite Pūjyapāda; two cite Devanandin; none joined them. **They are one man**, and the identity was printed in a book the corpus has read at first hand since Batch 47. (§2)
3. **How that happened, exactly — and it is not carelessness.** The two names were in a sentence the corpus *quoted*. Putting it in a table removed them. (§2.1)
4. ⚠⚠ **A religion inferred from a name**, by the corpus's principal modern grammar authority, hedged twice in one sentence — and the corpus had been repeating the conclusion without the hedge. (§4)
5. ⭐⭐⭐ **A school-name applied five hundred years late.** "Prāsaṅgika" and "Svātantrika" are twelfth-century **Tibetan** doxographic labels. This corpus has been teaching them as seventh-century Indian schools — **while already knowing better in a different file.** (§5)
6. ⭐ **And the one finding in the batch that is not about names**, kept here because it is the sharpest thing in it: a grammar that **keeps the whole metarule machinery and throws away every one of its words**. (§7)

---

## §1 The patronymic: the eighth generator, and it is nobody's mistake

The corpus's collision taxonomy, as it stood at the start of this batch, had seven generators. Six of them are **accidents** — a personal name, a place-name, a doctrine-name, a short form, a genre label, a title borrowed from another śāstra. Two things happen to share a label and a reader collapses them. The seventh, added in Batch 50 from Ollett, is **deliberate**: a prestigious ancient name is attached to a later work *on purpose*, to authorise it. Ollett's formulation is worth having in front of you again:

> "The fragile originary connection between a man and his work, moving forward through time, collides against the will to remember otherwise — to reach back into the past and overwrite it, to reassign identities, to constantly reauthorize the text."

**The eighth is neither.** Monier-Williams does not gloss *Śākaṭāyana* as a name at all. He glosses it as a **patronymic** — "*Patronymic* of an ancient grammarian… and of a modern grammarian… and of the author of a law-book" — and the Cologne *Purāṇa Index* has it as **"a *pravara* of the Bhārgavas,"** a lineage-name used in ritual invocation. Aufrecht's *Catalogus Catalogorum* enters an "ancient" and a "modern" Śākaṭāyana separately as a matter of course.

⭐ **A patronymic means "descendant of Śakaṭa." Its normal semantics is many-to-one.** Nobody is making an error at any point in the chain: not the man, not the tradition, not the lexicographer. **The structure of the naming system generates the collision.**

### §1.1 And it cuts backwards into the same batch

The corpus wrote `vyāḍi` first. That node records Abhyankar's argument for Vyāḍi's date:

> "the word *dākṣāyaṇa* indicates that Vyāḍi was a descendant of Dakṣa, and, as Pāṇini is called *dākṣīputra*, **critics say that Pāṇini and Vyāḍi were relatives**."

⚠⚠ ***Dākṣāyaṇa* is a patronymic.** The argument treats it as if it individuated a person — and a patronymic is precisely the kind of name that does not. ⭐ **The node written second weakened the node written first, and both stay standing with the tension recorded in each.** That is the machinery working: this corpus does not tidy away a result because it inconveniences an earlier one.

### §1.2 Where this leaves name-arguments generally

Set out as a scale, from what a name can support to what it cannot:

| a name can be evidence for | strength | example in this chapter |
|---|---|---|
| **What a text is called** — a title, a shelf | strong, and the tradition itself uses it | *Nyāsa* across five systems (Ch 45 §6) |
| **That two references are to the same work** when the form is distinctive and the context matches | moderate | *Tantrapradīpa* (§6) |
| **A cultural milieu** — that a name is at home in a tradition | weak, and it is a prior, not a finding | Abhyankar on *Maitreya Rakṣita* (§4) |
| **A person's identity, date or kin** | ⛔ very weak when the name is a **patronymic**, an **honorific** or a **short form** | Dākṣāyaṇa (§1.1); Pūjyapāda (§2); Candra (Ch 46) |
| **A doctrine** | ⛔ this is *jñāpaka* reasoning, and the tradition knows it is doing it | Haradatta on *Sphoṭāyana* (Ch 45) |

---

## §2 The node this corpus should have written fifty batches ago

Before writing anything, the batch ran three greps:

```
grep -l "Pūjyapāda"       concepts/*.md | wc -l   →  58
grep -l "Sarvārthasiddhi" concepts/*.md | wc -l   →  58
grep -l "Devanandin"      concepts/*.md | wc -l   →   2
files containing both                             →   0
```

**Fifty-eight concept files** read this corpus's own anchor text, the *Tattvārthasūtra*, through **Pūjyapāda's *Sarvārthasiddhi***. That is, by a wide margin, the most-cited author in the repository. **Two files** cite **Devanandin**, both as a *grammarian* — one of eight authors of post-Pāṇinian "different systems." **No file joins them.**

They are one man. *Pūjyapāda* — "worshipped feet" — is an **honorific**; the tradition glosses it by saying that gods came down to worship his feet. *Devanandi(n)* is the name. And the corpus's own translation source, Vijay K. Jain's 2018 Preface, adds two more:

> "Three other names of Ācārya Pūjyapāda find mention in Jaina literature: **Deva, Devanandi, and Jinendrabuddhi**."

⭐ **This is the inverse of every generator on the books.** All eight describe *one name covering several men*. This is **four names covering one man** — which [`durgasiṃha`](../../concepts/durgasimha.md) had already raised, as collision candidate **#15**, and left open for want of a resolved case. Here is the resolved case, and it is worse than #15, because one of the four names **belongs to somebody else as well** (§3).

### §2.1 How the corpus missed it, and why the answer matters

The identity is not obscure. It is in the **abbreviation list** of the dictionary this corpus has been reading at first hand since Batch 47:

> "**Jain., Jain. Vy. = Jainendra Vyākaraṇa by Pūjyapāda Devanandin.**"

And it is in the body, in the *Paribhāṣāsaṃgraha* census entry, item (ix): a gloss "on 108 Paribhāṣās or maxims noticeable in the **Mahāvṛtti of Abhayanandin on the Jainendra Vyākaraṇa of Pūjyapāda Devanandin**."

⭐⭐⭐ **The corpus read that sentence. `paribhāṣā`'s census tabulated it as:**

`| ix | gloss by Abhyankar himself, on maxims in Abhayanandin's Mahāvṛtti | 108 | Jainendra |`

**The two names were in the line that was quoted, and the act of putting it in a table removed them.**

⚠ **This is not a reading failure. It is a compression failure**, and it has a specific cause: a census keeps the **countable** columns — how many maxims, which system — and discards the nominal ones. *Who wrote the grammar the maxims belong to* was not a column, so it was not kept.

⭐⭐ **That is worth sitting with, because §2 of this repository's charter *prescribes* tabulation** — "for a **contested** concept, the divergence is presented as a **comparison table**… not prose." The instruction is right; the table is what makes a disagreement legible. **This chapter records its cost, once, in a case where it can be measured: a table is a lossy format, and what it loses is whatever is not one of its columns.**

---

## §3 Collision #17: two grammarians named Jinendrabuddhi, each with a *Nyāsa*

The corpus holds [`jinendrabuddhi`](../../concepts/jinendrabuddhi.md) for an **eighth-century Buddhist** grammarian of the "eastern school," author of the *Nyāsa* on the Kāśikā and — on the scholarly majority — of the *Viśālamalavatī* on Dignāga. Ch 45 is largely built on him.

Vijay K. Jain gives *Jinendrabuddhi* as a name of the **sixth-century Digambara** Pūjyapāda Devanandin.

⚠ **And Abhyankar prints both halves in one entry, one sentence apart:**

> "the commentary by **Devanandin on Jainendra grammar**… [is] named **Nyāsa**… In the same way, the learned commentary on the Kāśikāvṛtti by **Jinendrabuddhi**… is very widely known by the name **Nyāsa**."

**Two men. Both grammarians. Both named Jinendrabuddhi. Each with a work called *Nyāsa*. Two centuries and two religions apart. And the sentence that names them both calls one of them by his other name.**

⭐ Two generators are running at once: an **alternate name**, and the **genre label** *Nyāsa* that Ch 45 §6 identified as the fifth generator. ⚠ No source consulted says anyone has actually conflated them, and they cannot be one man. The typed `often-conflated-with-NOT-equivalent` edge is drawn anyway, in both files, because §5 of the charter makes the map's job **teaching the distinction** rather than waiting for someone to fall into it.

---

## §4 A religion read out of a name

Abhyankar, s.v. *Maitreya Rakṣita*:

> "**As it appears from the name Maitreya Rakṣita he appears to have been a Buddhist grammarian.**"

That is the whole of the evidence given. *Maitreya* is the future Buddha; *rakṣita* is a common Buddhist monastic ending. The inference is a reasonable one. **It is also the only one offered**, and Abhyankar hedges it twice in a single clause.

⭐⭐ **Batch 50 caught the identical move**, in Cowell: the **Kaccāyana** inference, "made on the name alone," which this corpus's own Batch-49 rule discounted without knowing either party. **This is the second instance, in a different reference work, and aimed at something larger — not an identity but a religious affiliation.**

### §4.1 The objection is in the same entry, and no source draws it

One sentence later, Abhyankar writes that later grammarians refer to him

> "by the name **Rakṣita alone**, as also by the name **Maitreya**, but **very rarely by the name Maitreya Rakṣita**."

⚠ **So the compound form — the entire basis of the inference — is the form his own citers avoided.** Taken singly, *Maitreya* and *Rakṣita* are each much weaker evidence than the compound is. *(This is the corpus's inference from two sentences of one source; no source makes it, and the corpus does not claim he was not a Buddhist. The affiliation is plausible. What is recorded is that the evidence for it is a name, and that the corpus had been repeating the conclusion without Abhyankar's hedge.)*

### §4.2 ⭐⭐⭐⭐ And the corpus's catalogue of this habit turns out to describe its own source

Ch 45 §4.1 records **Haradatta** reading a **doctrine** out of the proper name *Sphoṭāyana*. Ch 45 records **Jinendrabuddhi** reading a **biography** out of the proper name *Śalātura*. And [`paribhāṣā`](../../concepts/paribhasha.md) records that the technique has a **name** — *jñāpaka*, "indicator": reading a convention out of a text's incidental features — and that it is "not merely an error but a **licensed, named, technical procedure with its own vocabulary**."

⭐ **The third instance is a twentieth-century lexicographer, reading a religion out of a name.**

⚠ **This is not a gotcha and the chapter does not treat it as one.** Abhyankar marks his inference *as* an inference; that is more than either ancient grammarian did. The point is structural, and it is uncomfortable in the right way: **the corpus built a catalogue of a habit it was observing in its subject, and the catalogue turned out to fit its own principal modern authority.** A method that only ever finds the fault in the eleventh century is not a method.

---

## §5 The label that arrived five hundred years late

Everything above is about persons. **This section is the same problem at the scale of a school**, and it is the largest single correction in the batch.

[`madhyamaka`](../../concepts/madhyamaka.md), until this batch, said:

> "**Svātantrika sub-school** (Bhāvaviveka, ~500–570 CE) reformulates arguments as formal independent inferences… — rejected by **Prāsaṅgika** (Candrakīrti) as illegitimate."

[`prasaṅga`](../../concepts/prasanga-nagarjuna.md) said: "Later Madhyamaka **split** over whether prasaṅga is *sufficient*."

⚠⚠ **Both read as though two Indian schools existed under those names in the seventh century. They did not.**

- **SEP (Richard Hayes, 2010, rev. 2023):** the terms are "**not used by Indian Mādhyamikas themselves**," and were "assigned by Tibetan scholastics centuries later."
- **Wikipedia**, citing Vose, Lang, Thubten Jinpa, Thakchoe, Hayes, Dunne and Ruegg: "this doxographical categorization **only arose in Tibet during the 12th century**."

⭐ **What is Indian and real is a specific argument.** Candrakīrti defended **Buddhapālita** against Bhāvaviveka's criticism, on the ground that a Mādhyamika, having no thesis of his own, cannot supply the shared subject an autonomous inference requires. That argument is his, it is seventh-century, and Ch 20 and the `prasaṅga` node describe it correctly. **The school-names are a Tibetan organising scheme laid over it five hundred years later.**

### §5.1 The corpus already knew, in a different file

[`śāntarakṣita`](../../concepts/santaraksita.md) says, correctly and since Batch 12:

> "Later **Tibetan doxography** names the resulting school **Yogācāra-Svātantrika-Madhyamaka**."

⭐⭐ **The corpus knew the *Svātantrika* label was Tibetan in the node about the Svātantrika, and not in the node about the split.** That is a §4-signal-4 failure of exactly the kind the charter's internal-consistency sweep exists to catch, and it survived four years of the graph's growth because nothing ever required the two files to be read together.

### §5.2 What the correction costs the corpus's picture

The second half of the Candrakīrti node is harder than the first. On Wikipedia's own authorities, in India he

> "**does not seem to have been very influential during the 7th to 10th centuries**,"

his works were "**never translated into Chinese**," and he becomes influential only "by the 11th and 12th centuries… especially in **Kashmir** and in Tibet."

⚠ So the tidy lineage this corpus implies — Nāgārjuna → Buddhapālita → Bhāvaviveka → Candrakīrti as a settled succession of authority — **is a Tibetan retrospect.** The Indian Madhyamika who actually dominated the century *after* Candrakīrti is [`śāntarakṣita`](../../concepts/santaraksita.md) (725–788) — and he goes the other way, using precisely the autonomous inference Candrakīrti rejected, and he is the one who went to Tibet first.

⭐ **The corpus's two Madhyamaka nodes describe the winner of a Tibetan argument and the winner of an Indian one, and had no way of telling which was which.**

⚠ **This does not make the split unreal or the labels useless.** It makes them a **later scheme applied to a real earlier disagreement** — which is the third instance of one pattern in this corpus: [`raseśvara`](../../concepts/rasesvara.md) records the *Sarvadarśanasaṃgraha* manufacturing a "school" out of alchemical literature, and [`viśiṣṭādvaita`](../../concepts/vishishtadvaita.md) records that the school as described is partly Veṅkaṭanātha's retrospective systematisation. **A doxographer's category, read back as a thing that existed.**

### §5.3 A claim the batch went looking for and refused to make

A search summary offered something striking: that the *Mūlamadhyamakakārikā*'s Sanskrit survives **only** as embedded in Candrakīrti's *Prasannapadā*, which would be the only commentary on it surviving in Sanskrit at all. ⭐ If true, every Sanskrit MMK verse this corpus cites reaches it through Candrakīrti — and [`mūlamadhyamakakārikā`](../../concepts/mulamadhyamakakarika.md) does not say so.

⚠ **It is not confirmed.** SEP says only that the *Prasannapadā* "survives in Sanskrit as well as in Tibetan translation." Wikipedia's Candrakīrti article does not make the claim. Wikipedia's *MMK* article, **asked the question directly**, does not address the root text's survival at all.

⭐⭐ **Recorded as unverified, with the test named** — La Vallée Poussin's 1903–13 *Bibliotheca Buddhica* edition, and whether an independent Sanskrit MMK manuscript tradition exists. **Ch 46 §4.2 faulted the corpus for discounting a source wholesale; this is the same error in the other direction — adopting a summary wholesale because it was interesting.** Both are failures to ask what a particular sentence is evidence for.

---

## §6 Two texts known through their citers, eighteen centuries apart

**Vyāḍi's *Saṅgraha*** was a hundred thousand verses. It is gone. Abhyankar: "Some quotations only are found from the *Saṃgraha* in grammar works, but **the work is lost long ago**."

⭐⭐ And the loss is not merely a lexicographer's note. It is the **opening move of the *Vākyapadīya*'s epilogue**, which this corpus read at first hand this batch:

> *prāyeṇa saṃkṣeparucīn alpavidyāparigrahān | saṃprāpya vaiyākaraṇān **saṃgrahe 'stam upāgate***  (VP 2.480)

"**The *Saṅgraha* having gone to its setting**" — the loss of Vyāḍi's book is given as the *condition* that made grammarians fond of brevity and of little learning. Three verses later the *ārṣa* text is thrown into confusion *saṃgraha-pratikañcuke*. **Vyāḍi's book is named twice in ten verses as the thing whose absence defines the crisis.** ⚠ (Quoted as **wording read**, not translated: §1 of the charter forbids this corpus rendering it, and no published English of these verses proved obtainable — see §8.)

**Maitreya Rakṣita's *Tantrapradīpa***, a thousand years later, is described by Abhyankar in almost the same words: "**profusely quoted** by prominent grammarians after him," and "available only in a **fragmentary** manuscript form today."

⭐⭐⭐ **In 2007 it was published in full.** *Tantrapradīpa of Maitreyarakṣita (A Treatise on Kāśikā and Nyāsa)*, ed. Kanjilal, Sanskrit Pustak Bhandar, Kolkata, 267 pp. — from a manuscript **"hitherto unpublished," found in the Sāhitya Sabhā collection at Coochbehar**, running to **over 220 folios**.

⚠ **Abhyankar is not wrong. He is forty-six years old.** Batch 47 issued a standing caution that "read at first hand" and "specialist" are strong marks for what a discipline knows *internally* and weak for anything depending on outside scholarship that has moved — "**chronology above all**." ⭐ **This chapter extends it: a reference work's statements about *what survives* are exactly as perishable as its statements about dates, and for the same reason — a manuscript can be found.**

⭐ **And the pair is the lesson.** Two texts, both "known through their citers." One is genuinely gone. One was in a north-Bengal collection the whole time. **"Known through citations" is not a synonym for "lost," and the corpus has been treating it as one.**

### §6.1 The eastern school, drawn as a lineage for the first time

Ch 45 §4 established that "Pāṇinian grammar had **regions**" — eastern, southern, Benares — and [`jinendrabuddhi`](../../concepts/jinendrabuddhi.md) flagged "eastern school" as "a regional division of the Pāṇinian tradition the corpus has **not otherwise recorded**."

This chapter can now draw it:

| | | |
|---|---|---|
| **Jayāditya** (c. 650) | the *Kāśikā* | [Ch 42](../hindu/shastra/42-the-ladder-and-the-boundary.md) |
| **Jinendrabuddhi** (c. 800–850) | the *Nyāsa* on it | [Ch 45](45-the-witness-problem.md) |
| **Maitreya Rakṣita** (1075–1175) | the *Tantrapradīpa* on **that** | this chapter |
| ⚠ an unnamed fifth | a commentary on the *Tantrapradīpa*, which Abhyankar also has an entry for | **no node; the headword is OCR-lost** |

⭐ **Five tiers, one region, five centuries** — and at least two of the three named members held to have been Buddhists. Set that beside **Haradatta**, "a well-known **southern** scholar," working on the *same Nyāsa* in the same century from the other end of India, and Ch 45's regional claim stops being a remark and becomes a map.

---

## §7 The one finding here that is not about a name — and it is the sharpest

**Devanandin's *Jainendra Vyākaraṇa*.** The batch ran a grep over Abhyankar's scan and counted:

```
"in the Jainendra" in Abhyankar's Dictionary of Sanskrit Grammar   →  32 sentences
of the form "a technical/conventional term in the Jainendra
Vyākaraṇa for [Pāṇini's X]"                                        →  28
```

⭐⭐ **Essentially every mention of this grammar in the standard dictionary of Sanskrit grammar is a mention of a word it replaced.** The list, read off the Latin glosses: the accusative, the genitive affix, the locative, singular number, the second person, *dhātu*, *prātipadika*, *pratyaya*, *lopa*, *avyaya*, *dīrgha*, *hrasva*, the nasals, *abhyāsa*, *niṣṭhā*, *uttarapada*, *upasarjana*, the causal agent, the *ik* pratyāhāra, and the *guṇa*/*vṛddhi* pair.

⭐⭐⭐ **Including the term Pāṇini defines in his first sūtra.** Abhyankar: "a term used in the Jainendra Grammar **instead of the term *vṛddhi* of Pāṇini**… cf. **P. I.1.1**." The Aṣṭādhyāyī opens *vṛddhir ādaic*. **The Jainendra changes the word in it.**

### §7.1 This qualifies [Ch 44](../hindu/shastra/44-the-grammars-that-lost.md)'s T4 rather than confirming it

Batch 50 established at first hand, in Cowell, that the **metalanguage crosses system boundaries** — *adhikāra*, *pratyāhāra*, numbered *paribhāṣā*s, shared between rival systems and even across the Sanskrit/Prākṛt line. [`paribhāṣā`](../../concepts/paribhasha.md) carries the strong form: not merely shared maxims but "a shared **method for generating** them," each system running "the same inferential machinery over its own text."

⚠⚠ **The Jainendra is the counter-case.** It **keeps the machinery in full** — its own Paribhāṣāpāṭha, 108 maxims drawn from Abhayanandin's *Mahāvṛtti*, cited by Abhyankar as *Jain. Pari.* 20, 66, 85 like any other system's. **And it discards the vocabulary.**

⭐⭐ **So the corrected statement is: what crosses system boundaries is the *technique*, not the *terminology* — and the two are separable, because one system separated them.** The Batch-50 finding is not refuted; it is given its boundary.

### §7.2 The reading the chapter refuses

It is tempting to read the substitution as **sectarian** — a Jain grammar refusing Brahminical words. ⚠ **Nothing consulted supports that.** Abhyankar offers no motive. There are ordinary alternatives: several of the Jainendra's replacements are visibly **shorter** than Pāṇini's terms, and brevity is what the *sūtra* form rewards. **The corpus records the substitution as a fact and the motive as unknown**, and notes that its sources here are grammarians reporting equivalences, not historians explaining choices.

---

## §8 The sect whose entire surviving literature is four books by a grammarian

The second Śākaṭāyana — **Pālyakīrti**, c. 814–867, at the Rāṣṭrakūṭa court of **Amoghavarṣa I**, after whom he named his own commentary the *Amoghavṛtti* — is a grammarian, "a **Jaina Pāṇini** as it were" in Padmanabh Jaini's phrase.

He is also this:

> "the **only two extant texts of the Yāpanīya school**, namely the *Strīnirvāṇaprakaraṇa* and the *Kevalibhuktiprakaraṇa*, together with a commentary (*vṛtti*) on each, **all four works attributed to the same author, Śākaṭāyana**." *(Jaini 1991)*

⭐⭐⭐ **The entire surviving literature of a whole Jain sect is four works by one grammarian.**

And [`digambara`](../../concepts/digambara.md) in this corpus lists, as defining Digambara positions, that **women cannot attain liberation in a female body** and that **an omniscient being no longer takes food**. ⭐ **He wrote one treatise against each.** Jaini:

> "One would expect his opponents to be the **Śvetāmbaras**, who have traditionally held that view. Yet the earliest extant work dedicated to a systematic refutation of the Digambara position **does not originate in the Śvetāmbara camp**."

**The first sustained defence of women's capacity for liberation in Indian religious literature comes from the sect that no longer exists.**

### §8.1 Two sects, and each assigns the third to the other

| who | says the Yāpanīyas were | when |
|---|---|---|
| **Devasena**, a **Digambara** chronicler, *Darśanasāra* | "an offshoot of the **Śvetāmbaras**" | 10th c. |
| **Guṇaratna**, a **Śvetāmbara**, on the *Ṣaḍdarśanasamuccaya* | "a **Digambara** subdivision" | 15th c. |

⭐ **Each surviving sect assigns the third one to its rival.** Jaini's own account: naked male mendicants as with the Digambaras, but accepting the **Śvetāmbara canon** and holding nudity prohibited for women.

⚠ And the evidence for the man's own sect is **a colophon title** — *Śrutakevalideśīya-ācārya*, appearing at the end of every *pāda* of every *adhyāya*, which Upadhye (1974) reads as fixing his Karnataka Yāpanīya affiliation. His own *Amoghavṛtti* calls him only "the most venerable ācārya of the great saṅgha of the śramaṇas," which Jaini flags as "**a serious omission**," since a Jain ācārya heads exactly one group.

⭐⭐ **And Abhyankar records the same honorific from the other side of the desk** — "a term of a very great honour given to such Jain monks as have almost attained perfection… used in connection with **Pālyakīrti Śākaṭāyana, the Jain grammarian**" — with the headword itself lost to OCR. **A Sanskrit grammarian's lexicographer and a Berkeley Jainologist attach the same title to the same man, neither citing the other, and each supplies exactly what the other's evidence lacks.** That is §4 signal 1 at its strongest, and it happened by accident.

### §8.2 ⚠⚠ The §0 guard, taken from inside the source

There is an obvious and wrong thing to say about this node: that a ninth-century Jain monk was an early feminist, or that his sect represents a suppressed egalitarian India.

⭐ **The book supplying these facts warns against exactly that, in its own Foreword.** **Robert P. Goldman** traces how Orientalist romanticism, "picked up by exponents of the so-called Hindu Renaissance," was "developed into **a theory of ancient India as a place of social and gender equality**" that later foreign rule had supposedly spoiled.

And the argument does not have the shape a modern reader wants. Śākaṭāyana's move is technical: he "**rejected the very idea of distinguishing libido (*veda*) along the lines of biological gender**," inside a shared Jain framework in which sexuality of every kind is eliminated at the ninth [`guṇasthāna`](../../concepts/gunasthana.md) anyway. **It is an argument about karmic categories, made to win a scholastic dispute, and it is not less interesting for that.**

⭐⭐ **This is [Ch 46](46-opening-the-book.md) §6 arriving a second time from a different direction.** That chapter recorded a §0 failure mode the charter has no name for — inflation not into modern physics but into **modern politics** — warned against by Ollett, aimed at Jainism. **Here it is again: a different specialist, in a different decade, in a different discipline, warning against the same move, aimed at the same tradition.** ⚠ Batch 50 left a charter question for the user on the strength of one case. **It now has two.**

---

## §9 Sources caught being wrong — and four of the seven are us

| # | source | failure |
|---|---|---|
| 1 | **Abhyankar** | dates **Vyāḍi twice**, incompatibly: "a relative and contemporary of Pāṇini" (s.v. *Vyāḍi*) and "lived after Kātyāyana and before Patañjali" (s.v. *Paribhāṣāsūcana*) |
| 2 | **Abhyankar** | dates **Maitreya Rakṣita twice**: "beginning of the twelfth century" (s.v.) and "middle of the twelfth century" (s.v. *Dhātupradīpa*) |
| 3 | **Abhyankar** | ⭐ **out of date rather than wrong** — the *Tantrapradīpa* "available only in a fragmentary state," published in full in 2007 (§6) |
| 4 | **Wikipedia, "Chandrakirti"** | c. 600–650 in the lead, c. 600–670 in the infobox, unreconciled |
| 5 | ⚠ **this corpus** | `bodhisattva.md` attributed the ***Bodhi(sattva)caryāvatāra* to Candrakīrti**. It is **Śāntideva's** — and `bodhicitta.md` in this same repository has it right five times, with an `expressed-by: santideva` edge |
| 6 | ⚠⚠ **this corpus** | the same sentence claimed "**madhyamaka.md notes**" it. `madhyamaka.md` **does not mention the work at all.** ⭐ **A §4-signal-4 "corpus-internal" cross-check performed from memory rather than by reading the file it names — a wrong author and a false citation in one clause** |
| 7 | ⚠ **this corpus** | `paribhāṣā`'s census dropped the two names that would have identified Devanandin (§2.1) |
| 8 | ⚠ **this corpus** | `madhyamaka` and `prasaṅga` taught twelfth-century Tibetan labels as seventh-century Indian schools, **while `śāntarakṣita` had it right** (§5.1) |

⭐ **Item 6 is why the charter says, in §8: "Never recall a linked concept from memory — read its file."** This chapter is the first time the corpus has caught itself breaking that rule and can show the damage.

⭐ **And an eighth kind of source-failure, recorded because it is now a documented trap rather than a suspicion.** Batch 50 *inferred* that a reference aggregator was silently reproducing Abhyankar. This batch has the site's own attribution line — the Vyāḍi grammar entry is credited to "**Wikisource: *A dictionary of Sanskrit grammar* (K. V. Abhyankar)**," and its first sentence is verbatim the scan. **Anything that agrees with Abhyankar from that source is not a second signal.**

---

## §10 What the chapter leaves open

- ⚠ **No node for the Yāpanīyas**, whose entire literature §8 is about. The corpus has `digambara` and `śvetāmbara` and no third sect. ⭐ **Exactly the shape of the gap `candragomin` named when it observed that the corpus had `madhyamaka`, `nāgārjuna` and `yogācāra` and no Candrakīrti** — a gap this batch filled, and which promptly named a new one.
- ⚠ **No node for Āryadeva**, exposed by the Candrakīrti node the same way.
- ⚠ **No node for Śaraṇadeva or the *Durghaṭavṛtti***, although Abhyankar's abbreviation list treats it as a standing citation source and it carries the contemporary reference that dates Maitreya Rakṣita.
- ⭐⭐ **Jaini's Chapter II** — a complete published English translation of the *Strīnirvāṇaprakaraṇa* with its autocommentary, open access, already downloaded. **This chapter used its notes and not its translation.** It is the cheapest primary-source read the corpus currently has, and `DRIFT.md` D1 exists because items like it keep being listed instead of read.
- ⚠ **Whether the *Sarvārthasiddhi* uses Jainendra technical terms** where a Pāṇinian would use Pāṇini's. One man, two books, a mechanically checkable question, and it would say whether §7's substitution was a grammarian's device or a mind's habit.

---

*Next: the roadmap in [chapters/INDEX.md](../INDEX.md). ⚠ Note that this chapter corrects material in [Ch 20](../buddhist/20-buddhist-scholastics.md) and [Ch 45](45-the-witness-problem.md) as well as four concept files; the corrections are in the nodes and are summarised in §5 and §9 above.*
