# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 47 CLOSED — 387 concepts, 2410 edges** (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 40 and Ch 41**, written over Batch 47's twelve grammar nodes and **deliberately split across two folders** (`hindu/shastra/` and `hindu/darsana/`) because the tradition itself changed category. **Chapter coverage is 387 / 387 and `KNOWN_UNCOVERED` is EMPTY.** Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (48) — see the end of the Batch 47 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false "340/340" stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **387 concepts across 47 batches; 41 chapters.** 2410 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 387/387 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---

## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` → **ALL CHECKS PASS**; chapter coverage **387/387** with an empty `KNOWN_UNCOVERED` table. No outstanding maintenance, no red gate. The next unit of work is a **new concept batch (48)** — suggestions at the end of the Batch 47 run-log below.

⚠ **Read before opening Batch 48.** Batches 44–47 each falsified their own queue premises. Batch 47 falsified **two of its own four named tests** (T2 and T4 both came back different from what the queue expected) and **corrected two already-committed corpus files**. The suggestions below are **leads to test, not facts**.

⚠ **A new standing caution on source-weighting, produced by Batch 47 and applying to every future batch:** **"read at first hand" and "specialist" are strong marks for what a discipline knows *internally*** — vocabulary, manuscript contents, which attributions the tradition itself doubts — **and weak for anything depending on outside scholarship that has moved, chronology above all.** Abhyankar (1961) is authoritative on *pratyāhāra* and out of date on Bhartṛhari's century, and both are true of the same book. See Ch 40 §8.2.

⚠ **Abhyankar's dictionary is a session-scratchpad download and does not persist.** Re-download before any further grammar work — the method is the Meulenbeld one: take `server` and `dir` from `https://archive.org/metadata/dictionary-of-sanskrit-grammar-abhyankar`, then request `DictionaryOfSanskritGrammar_abhyankar_djvu.txt` from that host directly. ⚠ **Use that item, NOT `a-dictionary-of-sanskrit-grammar-kv-abhyankar-1961-gos`** — the latter's OCR is unusable (Devanagari-mis-OCR'd; zero hits for "Panini"). **Confirmed working this batch.**

---

### ⭐ A trajectory note, added after Batch 47 closed — **make Batch 48 a DEPTH batch, not a widening one**

*(Written by the Batch 46 session reviewing the corpus's direction across 44–47. It does not replace the Batch 48 suggestions below; it says what to do **with** them.)*

**The project is on track on every metric it measures, and drifting on the one thing it is *for*.** The evidence for "on track" is strong and is worth naming, because it is the machinery working as designed: **Ch 38 §4.1 (Batch 46) found that Navya-Nyāya's signature device had *grammatical* ancestry and recorded that the corpus had no node for Bhartṛhari or the *Vākyapadīya*. One batch later there are twelve grammar nodes.** The corpus told the next session what to build and it got built. Batch 47 then **qualified Batch 46's own generalisation** about reference sources rather than inheriting it. **Cross-session self-correction is the healthiest signal this project has.**

**The drift, in three measurable forms:**

1. **Distance from primary sources is growing, not shrinking.** §1 says work from critical editions and existing scholarly translations; in practice Batches 44–47 worked from **reference works *about* those texts**. Both of the last two batches hit unreadable OCR on a located edition. **The "identified but not read" lists are compounding: each batch adds ~8 and closes 1–2.**
2. **Teaching-layer staleness is accelerating.** Ch 11 was seven chapters out of date at the close of Batch 46 and is **nine** now. Chapters are write-once and never revisited, so this grows by one per batch until someone stops it.
3. **The follow-up debt from Batches 43–46 is almost entirely untouched.**

**So: spend Batch 48 on depth and debt, and add new nodes only where a written chapter already depends on a node that does not exist.** Growth resumes at 49.

**Part A — read what is already in hand or cheap.** ⭐ **`Matilal 1968 Parts II–III`** — his English translations of Gaṅgeśa's ***Abhāva-vāda*** and Raghunātha's ***Nañvāda*** with the Sanskrit appended. **Still the cheapest high-value item in the corpus**: a published scholarly translation of part of the primary text, downloadable by a known-good route, sampled in Batch 46 and never worked through. Upgrades four nodes from exposition-of-exposition to text.

**Part B — the standing external items**: Potter's *Padārthatattvanirūpaṇa* (1957) — settles what Raghunātha's "denies atoms" amounts to, and the number-eliminated/number-added contradiction that currently carries a hypothesis of the corpus's own; **Neevel 1977 pp. 14–16**; the *Ratnaprabhā* and the *Siddhayoga* with Śrīkaṇṭhadatta (**five files depend on these and none has seen a line**); Phillips's *Tattvacintāmaṇi*; Ingalls 1951.

⚠ **Part C — a fairness item, not a gap. `P. V. Sharma` appears four times in Batch 46 and always in rebuttal**, and the corpus has never read him directly. **A file that only ever records one side of a dispute is not neutral**, however good the source doing the rebutting.

**Part D — maintenance.** ⭐ **Revise Ch 11.** Nine chapters out of date is now the largest staleness in the corpus. Also check whether **Ch 26 §6.4** and **Ch 31 §4.2** still describe holes that have since closed.

---

## Batch 47 — CLOSED (2026-09-01). 12/12 concepts; 375 → 387 nodes; 2339 → 2410 edges. Plus Ch 40 and Ch 41.

Theme: **the śāstra the corpus had been leaning on without a node — Vyākaraṇa.** A grep found **20 files** invoking "grammar / Pāṇini / vyākaraṇa" against **zero** nodes for the Sanskrit grammatical tradition. **`python graph/check_all.py` → ALL CHECKS PASS**, chapter coverage **387/387**, structural audit **CLEAN**.

### The twelve

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `vyakarana` | **contested** / medium | **A vedāṅga that argued its way toward darśana status** — and the argument was Bhartṛhari's, not Pāṇini's. Three sources, three positions. |
| 2 | `panini` | **contested** / medium | ⭐ **A date that moved 350 years** — and drifted with the *kind* of evidence: linguistic impression vs. datable coins. |
| 3 | `astadhyayi` | **contested** / medium | ⭐ **Five sūtra counts** for the best-transmitted text in antiquity. The text is stable; its **boundary** is a judgement. |
| 4 | `katyayana` | **contested** / medium | ⭐ **A specialist lexicon holding both sides of the Vararuci question in two entries, without cross-reference.** |
| 5 | `patanjali-grammarian` | converged / medium | ⭐ **The commentator is dated better than his author** — mid-2nd c. BCE, triply attested, against Pāṇini's open 350 years. |
| 6 | `mahabhashya` | converged / medium | **The Great Commentary covers 31% of its own text**; and the commentarial stack runs **five tiers** deep. |
| 7 | `bhartrhari` | **contested** / medium | **Four sources, four centuries** — and the modern consensus rests on *discrediting* the only external witness, not replacing him. |
| 8 | `vakyapadiya` | **contested** / medium | ⭐ **A book about words structured as a book about what there is** — kāṇḍa III's samuddeśas are the Vaiśeṣika category list. |
| 9 | `sphota` | **contested** / medium | ⭐⭐ **The antiquity is an artefact of the reading apparatus.** |
| 10 | `sabdabrahman` | **contested** / medium | ***Pariṇāma*, not *vivarta*** — two monisms that disagree about whether the world happened. |
| 11 | `karaka` | converged / medium | **Meaning → role → ending**: a mediating level of representation, whose middle term Pāṇini never defines. |
| 12 | `nirukta` | **contested** / medium | ⭐ **Kautsa: the Vedic mantras are meaningless** — an attack on the premise of the entire vedāṅga programme. |

*(#12 `nirukta` was **added mid-batch** on the Batch 45/46 precedent, when `vyakarana` and `panini` opened required edges to it and a dangling stub would have failed the gate.)*

### The four named tests, and how they came back

| test | queued expectation | result |
|---|---|---|
| **T1** — is the Yoga-sūtra Patañjali the *Mahābhāṣya* Patañjali? | no | ✅ **Holds**, re-derived rather than inherited. The best argument is a **datable silence**: no text conflates them before **Bhoja, 11th c.** A medieval innovation, not an old tradition. |
| **T2** — did Bhartṛhari invent *sphoṭa*? | a yes/no | ❌ **Wrong question.** He did not invent the *term* (Patañjali did) and did invent the *doctrine*. Four candidate origins, answering different questions. |
| **T3** — does the `avacchedaka`-from-grammar claim survive? | uncertain | ✅ **Confirmed at first hand** — Matilal cites *Vākyapadīya* III with Helārāja. Edge now drawn. |
| **T4** — is *munitraya* scholarly or traditional? | expected a caution | ⚠ **Traditional — and it carries a *rule*.** Kaiyaṭa's *yathottaraṃ hi munitrayasya prāmāṇyam*: **the later sage has the greater authority.** ⚠ Secondary report only; **unverified** (403), and **not in Abhyankar** under *yathottara* — checked directly. Load-bearing and open. |

### ⭐ The engine finding: a source obtained, and a mechanism caught three ways

**K. V. Abhyankar, *A Dictionary of Sanskrit Grammar* (GOS)** — a full working scan, **read at first hand**, and the batch's lexical hard constraint (§4 signal 3). It is the grammarians' **own** reference work, and it repeatedly beat the encyclopedias: the *pratyāhāra* result, the sūtra counts, the Vārttika counts, the Vararuci argument, the Sphoṭāyana rejection, the Prātiśākhya retrojection, and a sixth name-collision.

**The recurring mechanism — Ch 39's subject, in a literature Ch 39 never touched, three times inside Pāṇini's own text.** Pāṇini **states operations, not definitions**:

1. ***pratyāhāra*** — "The term is **not actually used by Pāṇini**… he has not given any definition… he has simply given the *method*… and has profusely used them."
2. ***kāraka*** — A 1.4.23 is a **heading**; *kriyānvayitvaṃ kārakatvam* is the commentators'.
3. **Pāṇini's own biography** — Jinendrabuddhi reads "the man from Śalātura" out of A 4.3.94.

⭐ **And the corollary is the most useful thing the batch produced.** Ch 39 treated these as *failure modes*. Batch 47 forces a correction: Haradatta reading the sphoṭa doctrine out of the **name** Sphoṭāyana produces **false history**; the tradition supplying a name and definition for *pratyāhāra* produces **a perfectly good analysis**. **The mechanism is not inherently corrupting — it is inherently *invisible*.** Noticing that it operated is the job; assuming the result is wrong is not.

⭐ **Its sharpest form, in `sphota`:** "The word *sphoṭa* is **not actually found in the Prātiśākhya works**. However, **commentators** on them **have introduced it in their explanations**." The Prātiśākhyas predate Pāṇini and lack the word; their commentaries have it. Anyone reading them as the tradition reads everything — *with* commentary, as one object — finds sphoṭa in the oldest phonetic literature and concludes it is primordial. **The antiquity is an artefact of the reading apparatus.**

### What the batch did to its own corpus

**Two committed files corrected, and one long-standing debt paid twice:**

1. **`patanjali.md`** — dated Bhoja's *Rājamārtaṇḍa* to "**~10th c.**" **while citing the source that says 11th.** Off by a century; corrected — and the correction *strengthens* the argument. It also gained the typed edge it had said it could not draw, plus the fact that the conflation is **three-way** (grammarian + yogin + physician) with a **theological motor**: Patañjali as an avatar of Ādi Śeṣa, for whom mastering three sciences is a consequence of the premise rather than a confusion.
2. **`avacchedaka.md`** — had recorded "no node for Bhartṛhari and none for the *Vākyapadīya*… recorded as a gap rather than smoothed over with a loose link." **That refusal was right, and the gap is now closed.**
3. **`vyakarana.md`** — four doctrine→person `expressed-by` edges caught and fixed against the convention Batch 46 settled and the `shankara → advaita-vedanta` idiom.

⭐ **And a qualification of the corpus's own Batch 46 generalisation.** Batch 46 concluded that reference sources "are unreliable **as a set of witnesses**, because they do not check themselves across articles" — said of Wikipedia strata. **It holds inside a single-author scholarly dictionary**: Abhyankar's *Vararuci* entry supplies the evidence refuting the claim its own opening sentence calls "very likely," while his *Kātyāyana* entry reports the identification without the refutation. **The pathology is a property of the entry as a unit of writing, not of crowd-sourcing.**

### §0 discipline — the batch's most exposed nodes

Two nodes sit directly on the prime directive, and **both declined to draw an edge**:

- **`karaka`** — there is a **live** "Pāṇinian Grammar Framework" in computational linguistics. Recorded, with the limit: usability shows the analysis is *general*, not that Pāṇini held a theory of argument structure.
- **`sabdabrahman`** — "reality is made of language" invites *it-from-bit*. **Four explicit limits stated**, including that "it from bit" is itself a **speculative programme, not a result** — so comparing an ancient metaphysics to a modern speculation and calling the pair a convergence is **doubly unearned**.

**Neither drew a physics or modern-linguistics edge**, on the precedent `avacchedaka.md` set. And `astadhyayi` carries the Post/BNF/Turing/Chomsky comparisons **with Cardona's brake**: of Saussure's work, "it shows **no direct influence** of Pāṇinian grammar… on occasion, Saussure follows a path that is **contrary**." **The resemblance is real and the descent is not.**

### Name-collisions: six, all flagged, none merged

Vararuci (two men) · Patañjali (three attributions) · Kātyāyana (vārttikakāra / Prātiśākhya / Śulbasūtra / Buddhist) · Sphoṭāyana (a name, not a doctrine) · **Cakrapāṇi-Śeṣa** (17th-c. grammarian) vs the corpus's **Cakrapāṇidatta** (11th-c. Āyurvedic commentator) — **flagged pre-emptively, before it could be made** · and the Śeṣa *family* of grammarians vs Patañjali-as-Ādiśeṣa.

### The teaching layer

| ch | title | folder | nodes |
|---|---|---|---|
| **40** | What Grammar Was For: Pāṇini and the Ancillary Sciences | `hindu/shastra/` | 8 |
| **41** | The Word as the World: Bhartṛhari and Grammar's Claim to Be a Darśana | `hindu/darsana/` | 4 |

⭐ **The split across two folders is itself the finding.** One tradition, two chapters, because the tradition **changed category** — and the change was contested. Ch 40 §9 is the corpus's fullest prime-directive treatment to date; Ch 41 §5 deliberately contrasts its own restraint with Ch 38 §7, where the modern comparison **earned** its place because Matilal and Ganeri independently converged. **The difference is evidence, not squeamishness.**

### Follow-ups carried into Batch 48

**New, from this batch:**

1. ⭐ **Kaiyaṭa's *yathottaraṃ* maxim** — load-bearing for Ch 40 §2 and **unverified**. *Evolution of the Notion of Authority (Prāmāṇya) in the Pāṇinian Tradition* returned **403**.
2. ⭐ **Maṇḍana Miśra wrote a *Sphoṭasiddhi*** — absent from `mandana-mishra.md`, which holds him purely as Mīmāṃsaka-turned-Advaitin and Śaṅkara's rival. **A node the corpus thought it knew has a second career.**
3. **The Kautsa controversy** — *J. Indian Philos.* (Springer, 2021) on *Nirukta* 1.15–16, **paywalled**. The corpus has the objection and **not Yāska's answer**.
4. **The *Vākyapadīya*'s "635 verses"** — challenged on internal-consistency grounds; needs an edition to settle.
5. **Is the *Vṛtti* on kāṇḍas I–II by Bhartṛhari?** Queued, and untestable from the sources consulted.
6. **The śabda-as-Brahman lead** — M.Bh. Āhnika 2 end, per Abhyankar. Would push `sabdabrahman` back to Patañjali.
7. **Vākyapadīya II on Candrācārya** — the available accounts **contradict each other** on whether he is blamed for the Mahābhāṣya's neglect or credited with its revival. Both weak provenance; no claim made.
8. **Renou, Woods (1914), Dasgupta (1922)** — T1's positions are known, **their arguments are not**.

**Carried from earlier batches, still open:** Phillips's *Tattvacintāmaṇi* translation (3 vols, Bloomsbury 2020); **Matilal 1968 Parts II–III, already in hand and still unused — the cheapest high-value item in the corpus**; Potter's *Padārthatattvanirūpaṇa*; Neevel 1977; the *Ratnaprabhā* and the *Siddhayoga*; **P. V. Sharma** (met four times in Batch 46, always in rebuttal); Ingalls 1951; the D. Ch./D. C. Bhattacharyya question; the Digvijaya dating tension in `shankara.md`; `karma-vargana.md` still the only `low`-confidence node; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; **Valerie Stoker**; Lance Nelson; a critical *Lakṣaṇāvalī*. ⚠ **Ch 11 is now nine chapters out of date.**

### Suggested Batch 48 (names only — **leads to test, not facts**)

- **Opened directly by this batch:** `kaiyata` (whose maxim Ch 40 leans on unverified) · `nagesha-bhatta` (18th c., tier 5, and he *redefined* what a Vārttika is) · `helaraja` (the corpus reaches both Bhartṛhari and `avacchedaka` through him) · `kasika` · `yaska` as a person distinct from `nirukta` · `kaundabhatta` · `pratyahara` or `anubandha` as a technical node · `vararuci` (to hold the split Abhyankar argues for).
- **Still open from Batch 46:** `madhava-nidana` / `madhavakara` · `vijayaraksita` · `srikanthadatta` · `annambhatta` / `tarkasangraha` · `jagadisha-tarkalankara` · `vardhamana-upadhyaya` · `sridhara` · `jayanta-bhatta` · `parasara-bhatta` · `yadavaprakasha`.
- **Maintenance:** **Ch 11 predates the entire Advaita-lineage cluster and now also Chs 36–41.**
