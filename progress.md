# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 43 IN PROGRESS — 332 concepts, 1939 edges** (audit CLEAN; 3 of 11 queued concepts done).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Chs 29–33 drafted — the teaching layer is COMPLETE for the current 329-node graph.** Batch 42 added 20 nodes and five chapters were written over them (29 transmission · 30 the locus of avidyā · 31 the Āyurvedic body · 32 the aghāti karmas · 33 the asura question). The roadmap was re-derived on 2026-08-26 and found **eight** genuine gaps, all of the *covered-in-prose-but-missing-a-row* kind — rows added, no chapter needed. Coverage now verified at **329 / 329**. **→ The next unit of work is to RESUME BATCH 43 here (see the IN-PROGRESS block immediately below the header), not a chapter.** Chapter coverage is complete at 332/332 — the three Batch-43 nodes were folded into Chs 18 and 33 rather than given a new chapter. Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠️ When re-deriving, diff on **chapter prose with diacritics**, not on bare keys — the index lists concepts by IAST display name, so a key-only diff reports false gaps. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## ▶ Batch 43 — IN PROGRESS (2026-08-26) — START HERE

**State: 3 of 11 done, working tree clean, audit CLEAN, everything pushed.** A maintenance pass ran first and is closed (below). Resume at the next `pending` row.

### Maintenance pass — DONE (closed follow-ups 1, 2, 3, 7 of Batch 42)
| # | item | outcome |
|---|---|---|
| 1 | `ajiva.md`'s `part-of: jiva` inverted its own partition | **fixed** — retyped `often-conflated-with-NOT-equivalent`; jīva and ajīva are exhaustive complements, and the note records why (no *complement-of* relation exists) |
| 2 | `many-valued-logic` tagged `tradition: Modern Physics` | **fixed** — now `Western (mathematical logic / philosophy of logic)`, matching its siblings |
| 3 | `atman-vedanta.md` / `brahman.md` queued a Vivekācūḍāmaṇi fetch *as Śaṅkara's* | **fixed** — re-scoped to *attributed to*, pointing at `shankara.md` and Ch 25 §3.1 |
| 7 | `dharmottara.md` vs `dharmottara-nyayabindu.md` suspected redundant | **resolved, no change** — a legitimate person/text split, correctly typed |

**Two findings from that pass, both worth carrying:**
- **A cross-type edge audit** (not implemented in `build_graph.py`, which only checks same-type) found **77 pairs** carrying directional edges in both directions. They are **complementary inverse pairs** — `part-of` ↔ `expressed-by` (50), `is-a-type-of` ↔ `expressed-by` (11), `formalizes` ↔ `expressed-by` (6), `formalizes` ↔ `part-of` (4), `aggregates-into` ↔ `aggregates-from` (3) — **not** contradictions. Same-type bidirectional edges: **zero**. ⚠️ **CLAUDE.md §5 was clarified to say so explicitly, in both the storage rule and the edge-type pairing rule, with an explicit “do not repair them”** — documentation of existing practice, not a policy change. `aggregates-from` was also added to §5's vocabulary list (used on 4 edges, present in `build_graph.py`, missing from the charter). **This is the one charter edit this session; revert it if unwanted.**
- **One genuine defect** the same audit found and fixed: `prakriti-samkhya.md` carried `is-a-type-of: guna-samkhya`, asserting prakṛti is a *sub-type* of guṇa — the reverse of its own note. Retyped `expressed-by`; the correct part→whole edge already existed on the other side.

### Batch 43 concepts

| # | concept | state | note |
|---|---|---|---|
| 1 | `abhinavagupta` | **done** — contested / medium | The *Tantrāloka*'s 37 chapters make “Kashmir Śaivism” one system; ~15 teachers including declared dualists. Key finding: ***rasāsvāda* resembles *brahmāsvāda* “but it is not a complete dissolution”** — the tradition draws the analogy/identity line itself, and its popularisers drop it. |
| 2 | `somananda` | **done** — contested / medium | Founder of a school named after a word he never uses. The *Śivadṛṣṭi* is largely polemic (Bhartṛhari, Śākta, Vijñānavāda, Advaita's ignorance-doctrine **by name**), and its decisive clause is “**not Māyā's illusion**.” |
| 3 | `ahura-mazda` | **done** — contested / medium | Second Iranian node. Ch 33's correspondence is now **three-term**: *ahura*/*asura*, *aṣ̃a*/*ṛta* (both ← PII *\*Hṛtá-*), and fire as the guardian of both. Haug 1884's monotheist reading recorded as datable and interested. |
| 4 | `sarvajnatman` | pending | the third holder of *pratibimbavāda* (Ch 30 §7) |
| 5 | `amalananda` | pending | Bhāmatī continuation, 13th c., *Kalpataru* |
| 6 | `appayya-dikshita` | pending | Bhāmatī continuation, 16th c., *Parimalā* |
| 7 | `rasesvara` | pending | the mercurial school — opened by `govinda-bhagavatpada`; note the dating conflict (Cowell & Gough put it at “the commencement of the Christian era” against a 9th-c. author) |
| 8 | `cakrapanidatta` | pending | Caraka's commentator, to whom the three *dhātu-poṣaṇa-nyāya*s are credited **on a single derivative source** (Ch 31 §4.2) |
| 9 | `dalhana` | pending | Suśruta's commentator |
| 10 | `hiranyakashipu` | pending | the boon and its failed disjunction (Ch 33 §5.3) |
| 11 | `hemacandra` | pending | the *Triṣaṣṭiśalākāpuruṣacaritra* — **Ch 33 §7's named upgrade path**; Helen Johnson's complete English translation exists |

### Also done this session
- **Chapter coverage kept complete**: the three new nodes were folded into **Ch 18 §Pratyabhijñā** (Somānanda given the founder's two paragraphs; Abhinavagupta's *rasa* sentence sharpened to the tradition's own qualification; his integrative role and the Ch 29 §6 transmission fact added) and **Ch 33 §4.1** (the three-term correspondence table). Three rows added to `chapters/INDEX.md`. **332 / 332 covered.**
- Graph rebuilt at each step; `graph.svg` rendered via the explicit Graphviz `dot.exe` path (still not on PATH). `find_duplicates.py` exit 0.

### ⚠️ Session note for whoever resumes
**`WebSearch` hit its session limit part-way through this batch** (`WebFetch` continued to work). The three completed nodes were finished on direct fetches plus corpus cross-check. If search is available again, the pending nodes will be much cheaper; if not, prefer nodes with an obvious Wikipedia/SEP/IEP URL to fetch directly.

### Open follow-ups carried into Batch 43
- **(4)** Ch 11 predates the whole Advaita-lineage cluster; re-read against Ch 25 §§3–6, Batch 41 and Ch 30.
- **(5)** The Digvijaya dating tension (`shankara.md` dates “Mādhava's Śaṅkaradigvijaya” to the 17th c.; Vidyāraṇya died 1391).
- **(6)** `karma-vargana.md` is still the Jain layer's one `low` node.
- **(8)** The **42-vs-93** *nāma*-karma discrepancy — needs the *Karma-grantha* / *Gommaṭhasāra Karmakāṇḍa* read directly.
- **(9)** Ch 23 §“A third authority” and Ch 26 §6.4 both now describe **closed** holes and should be rewritten when those chapters are next revised.

---

## Batch 42 — post-Śaṅkara Advaita, the Āyurvedic body, the Jain aghāti half, and the asura question (2026-08-26)

### Startup reconcile
- Batches 1–41 committed; working tree clean at start; audit CLEAN (309 nodes, 1733 edges).
- Took the **Suggested Batch 42** list from the Batch-41 run-log and worked it end to end, including every "carried over (again)" item.
- Dedup gate run for all twenty keys: `Glob concepts/<key>*.md` returned nothing for any of them, and a grep of all `## Links` targets confirmed none had been reserved.

### Batch 42 concepts — 20 / 20 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | the finding |
|---|---|---|---|---|
| 1 | prakasatman | contested | medium | *mūlāvidyā* as **positive (*bhāvarūpa*) beginningless** material cause — the doctrinal hinge of all later Advaita. Date **contested across three centuries** (10th c. per IEP/wisdomlib vs c. 1200–1300 per Wikipedia ×2 + Hindupedia), with **no source arguing** for a date. Adds the *pratibimba*/*avaccheda*/*ābhāsa* three-way table. |
| 2 | vacaspati-mishra | contested | medium | The Bhāmatī side of the locus split finally stated **by its own partisans**, and it matches what IEP said from the Vivaraṇa side. New: avidyā is **plural** in Bhāmatī ("plural since the jīvas are plural"). Date rests on one colophon reading **898** with the **era unstated** — Vikrama gives 840, Śaka 976. Records a **visible reference-work error** (Hindupedia gives him Śaṅkara's dates, 788–820). |
| 3 | govinda-bhagavatpada | contested | **low** | The lineage's load-bearing joint, attested only by the lineage. Four attributions tabulated with **four different reasons** each fails. The Narmada episode read for *what it does*: Śaṅkara supplies the doctrine **before** initiation. |
| 4 | utpaladeva | contested | medium | *pratyabhijñā* **does not occur in Somānanda's *Śivadṛṣṭi*** — the second man supplies the thesis. The lost *Vivṛti*'s largest fragment survives **in the margins of Abhinavagupta's *Vivṛtivimarśinī***; Śaṅkarakaṇṭha's 17th-c. notes date the decay. Journal-grade (Ratié ×2). |
| 5 | aghati-karma | converged | medium | **TS 8.11 enumerates 42** subdivisions of *nāma* against the systematised **93** — and every other count checkable against the sūtra matches, so the whole 148-vs-sūtra gap is inside *nāma* and equals **51**. Only visible because three sūtras were fetched directly. Also: *tīrthakaratva* is item 42. |
| 6 | iryapathika-asrava | converged | medium | **TS 6.4 fetched**, closing the sourcing gap `asrava.md` had flagged against itself. Guṇasthāna **11–13**; "the *īryāpatha* karmas do not have the power to bind." Stage 11 suppresses rather than destroys passion, so *akaṣāya* is **operational**, not biographical. |
| 7 | dhatu | contested | medium | Classical Āyurveda transmits **three incompatible nourishment mechanisms simultaneously** (*kṣīra-dadhi* / *kedārī-kulyā* / *khale-kapota*), each explaining what the others cannot. Contested **by design**, not by scholarly disagreement. |
| 8 | mala | converged | medium | The *dhātu-mala* of **rasa is kapha** and of **rakta is pitta** — two of the three doṣas appear as tissue wastes, reversing the standard picture. *Vāta* has **no row**, flagged. |
| 9 | agni-ayurveda | converged | medium | **§8 tradition-split** from the Vedic deity `agni`, with the sanctioned two-type edge. Four states of *jāṭharāgni* keyed to the doṣas — a **non-linear** model in which one pathology (*viṣamāgni*) is instability, not a quantity. |
| 10 | vagbhata | contested | medium | The AH **travelled** — Tibetan, Arabic, Persian. Authorship kept in **two** forms usually conflated: the traditional Elder/Junior harmonisation vs philology's merely **negative** verdict. The AS colophon is already a grandson explaining a homonym. |
| 11 | varsaganya | contested | **low** | Reconstructed **entirely out of Vācaspati Miśra's citations** (Frauwallner). Two literatures that **do not meet**: Wikipedia attributes the *Ṣaṣṭitantra* to Pañcaśikha and does not mention him at all. |
| 12 | psellos | contested | medium | The Oracles survive largely because an **11th-c. Christian** quoted them; his is "the most extensive surviving commentary" and the route back to Proclus's lost treatise. **des Places 1971 omits fragments he quotes** — the problem does not stop at antiquity. 1054 charge from the future Patriarch. |
| 13 | eriugena | contested | medium | Built a complete Neoplatonic system and **"did not have direct knowledge" of Plotinus or Proclus**. *nihil per excellentiam* typed **NOT-equiv** *śūnyatā* — a superlative predicated of a plenum vs an absence asserted to block any source. |
| 14 | prajnakaragupta | converged | medium | The name four corpus files already cited. Says what he **rejected** (Dharmottara's *niścaya-pratyaya*) and explicitly **not** what he proposed. Serves as the **control case** for evidence-vs-reading confidence. |
| 15 | vritra | contested | medium | Dragon or **obstruction**? Benveniste & Renou against the combat-myth reading, with the neuter-abstract morphology as the hinge. |
| 16 | verethragna | contested | medium | **The corpus's first Iranian node.** The *Bahrām Yašt*'s ten forms contain **no adversary** — the strongest datum for the abstract reading. Three-way dispute mapped (traditional / Benveniste-Renou / **Thieme's functional merger**). |
| 17 | varuna | contested | medium | *asura* at RV 5.63.3 is an **approving** title of the supreme moral god. The *pāśa*, the thousand-eyed spies, RV 7.86–88's confessions, the *Varuṇapraghāsa* wife's confession — a **conscience-religion that did not become the mainline**. Dumézil's Ouranos etymology recorded as **withdrawn**. |
| 18 | balarama | contested | medium | Jainism **enrols** both brothers among the 63 *śalākāpuruṣa*s and then **reverses the ranking**: Kṛṣṇa (ninth *Vāsudeva*) is reborn in hell for his violence, Balarāma (ninth *Baladeva*) is liberated directly. |
| 19 | prahlada | converged | medium | *navavidhā bhakti* (BhP 7.5.23–24) read **in order** as a progression of intimacy; and **portable** — the *Śiva Purāṇa* lists the same nine for Śiva. |
| 20 | atri | contested | medium | "Atri's eclipse": **three dates 391 years apart, two from the same authors**, from a hymn containing no date. The corpus **declines** the datings without asserting them false. |

### Chapters written over the new nodes — 5 (Chs 29–33)
- **Ch 29 — How Things Reach Us** (`cross-tradition/`): the transmission chapter. Four channel-types with the corpus's full inventory and each one's failure mode; the Chaldean Oracles' two filters; Prajñākaragupta as the control case; Atri's eclipse as the *reader's* filter. Primary: psellos · eriugena · vārṣagaṇya · govinda-bhagavatpāda · utpaladeva · prajñākaragupta · vāgbhaṭa · atri.
- **Ch 30 — Where Does Ignorance Live?** (`hindu/darsana/`): the *āśraya* dispute stated from both sides. Primary: prakāśātman · vācaspati-miśra.
- **Ch 31 — The Body as a Rate** (`hindu/shastra/`): closes Ch 23's named gap; argues Āyurveda is an **equilibrium theory, not a vitalist one**. Primary: agni-āyurveda · dhātu · mala.
- **Ch 32 — What Survives Omniscience** (`jain/`): closes Ch 26 §6.4. Primary: aghāti-karma · īryāpathika-āsrava.
- **Ch 33 — The Asura Question** (`cross-tradition/`): one word across four traditions. Primary: varuṇa · vṛtra · verethragna · prahlāda · balarāma.

### Findings that reach beyond their own nodes
- **A §0 case handled as a case.** `atri` separates *what is well-founded* (RV 5.40 describes solar obscuration by Svarbhānu; he heads a long line of eclipse-thinking) from *what is not* (a datable observation; the world's earliest record; a date for the Ṛgveda) — and phrases the negative claim as **not established by what the corpus has seen**, not as false.
- **Confidence levels now mean two different things, deliberately.** `varsaganya` is `low` because of *the evidence that exists*; `prajnakaragupta` is `medium` because of *the reading that was done*. Ch 29 §7 makes the distinction explicit.
- **A source used for its terms and refused for its editorialising.** Caraka-Saṃhitā-Online glosses *jāṭharāgni* as "amylolytic, proteolytic and lipolytic enzymes." Quoted in `dhatu.md` and Ch 31 §7, **not adopted** — §4's "take the term, leave the editorialising," applied by name.
- **Independent corroboration, achieved.** Batches 40–41 recorded the Bhāmatī position only through IEP's Vivaraṇa-side vantage. Batch 42 reached it through the Bhāmatī literature and **everything came back unchanged**.
- **Two chapter-flagged holes closed**: Ch 23's (`vagbhata`/`dhatu`/`mala`) and Ch 26 §6.4's (the *aghāti* four and the kevalin's residual influx). Both old notes left standing, struck through or annotated, so the hole and its closure are both visible.

### Honesty-layer edges added (selection)
- `agni-ayurveda` ↔ `agni`: `shares-vocabulary-with` **+** `often-conflated-with-NOT-equivalent` — a §8 tradition-split so the deity's prestige does not underwrite the physiology.
- `vritra` ↔ `verethragna`: same pair of types — same root, **inverted referent**.
- `verethragna` ↔ `avatara-vedanta`: same pair — drawn specifically so the coincidence of *ten forms* cannot be read as descent.
- `eriugena` → `sunyata`: NOT-equivalent — the same negation doing opposite structural jobs.
- `balarama` → `gita`: NOT-equivalent — bondage in the **intention** vs in the **act**.
- `prahlada` → `shaivism`: NOT-equivalent — the same nine devotional forms, a different addressee.
- `prakasatman` → `prakriti-samkhya`: parallel **+** NOT-equivalent — *mūlāvidyā* in prakṛti's job-slot.
- `prajnakaragupta` → `kevala-jnana`: parallel **+** NOT-equivalent — omniscience as an epistemological result, but not a property of a permanent jīva.
- `varuna` → `karma-vedic`: NOT-equivalent — a personal moral order with confession vs an impersonal mechanism.

### Audits
- Three de-orphaning passes, all fixed per §10 with **content-motivated** inbound edges written from their own node's vantage (never mechanical mirrors): `nirjara→iryapathika-asrava`, `vacaspati-mishra→prakasatman`, `vijnaptimatrata→utpaladeva`, `charaka→vagbhata`, `krishna→balarama`, `henosis→eriugena`, `santaraksita→prajnakaragupta`, `prakriti-samkhya→varsaganya`, `svarbhanu→atri`, `bhakti→prahlada`.
- Final: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0. One new expected DEVANAGARI group (`अग्नि : agni, agni-ayurveda`) — a typed split, edge verified.
- Graph: **309 → 329 nodes, 1733 → 1910 edges**; `graph.svg` rendered via the explicit Graphviz `dot.exe` path (still not on PATH — same workaround as Batches 38–41).
- **Chapter-coverage re-derivation**: 329 / 329 covered; eight rows added to `chapters/INDEX.md` (gauḍapāda, padmapāda, vidyāraṇya, jina, tīrthaṅkara, tattvārtha-sūtra, samyagdarśana, sarvajñatva) — all *covered-in-prose, missing-a-row*, none needing a chapter.

### Open follow-ups (carried, not acted on)
1. **`ajiva.md` stores `part-of: jiva`**, inverting its own partition. A schema question (no *complement-of* relation exists), not a typo. *(carried from Batch 41)*
2. **`many-valued-logic` carries `tradition: Modern Physics`** — it is formal logic, and the mis-tag mis-colours the node. *(carried)*
3. **`atman-vedanta.md` and `brahman.md` queue a Vivekacūḍāmaṇi fetch *as Śaṅkara's***; must be re-scoped to *attributed*. *(carried)*
4. **Ch 11 predates the whole Advaita-lineage cluster** and should be re-read against Ch 25 §§3–6, Batch 41, and now Ch 30. *(carried)*
5. **The Digvijaya dating tension** (`shankara.md` dates "Mādhava's Śaṅkaradigvijaya" to the 17th c.; Vidyāraṇya died 1391). *(carried)*
6. **`karma-vargana.md` remains the Jain layer's one `low` node.** *(carried from Ch 26)*
7. **NEW — `dharmottara.md` and `dharmottara-nyayabindu.md` both exist.** Not flagged by `find_duplicates.py` (keys and IAST differ), but the person/text split should be checked for redundancy. *(opened by Ch 29)*
8. **NEW — the 42-vs-93 *nāma*-karma discrepancy** is unresolved and needs the *Karma-grantha* / *Gommaṭasāra Karmakāṇḍa* read directly. *(opened by `aghati-karma`)*
9. **NEW — Ch 23's §"A third authority, and a gap in the graph" and Ch 26 §6.4** both now describe closed holes and should be rewritten when those chapters are next revised.

### Corpus milestone: **329 concepts across 42 batches; 33 chapters.** 0 orphans. 0 unwritten stubs. Audit CLEAN. Chapter coverage 329/329.

### Suggested Batch 43 (names only — no files written)
- **Opened by Batch 42:** `somananda` (the *Śivadṛṣṭi*; Utpaladeva's teacher, and the man who did **not** coin *pratyabhijñā*); `abhinavagupta` (named across Chs 18/27/29 and still unwritten — the grand-disciple whose manuscripts carry Utpaladeva); `rasesvara` (the mercurial school, opened by `govinda-bhagavatpada`); `amalananda` and `appayya-dikshita` (the Bhāmatī continuation); `sarvajnatman` (the third holder of *pratibimbavāda*).
- **Opened by Chs 29/31:** `cakrapanidatta` (Caraka's commentator, to whom the three *dhātu-poṣaṇa-nyāya*s are credited on a single derivative source) and `dalhana` (Suśruta's commentator).
- **Opened by Ch 33:** `ahura-mazda` (the corpus's second Iranian node, and the one that would let the *asura/ahura* + *ṛta/aša* correspondence be drawn from the Iranian side); `hiranyakashipu`; `hemacandra` (the *Triṣaṣṭiśalākāpuruṣacaritra*, whose Johnson translation is the named upgrade path for Ch 33 §7).
- **Structural/maintenance pass:** follow-ups 1, 2, 3 and 7 above — all four are §10-mechanical or near-mechanical, and none has been touched in three batches.
