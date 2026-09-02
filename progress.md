# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 48 CLOSED — 397 concepts, 2473 edges** (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 42 and Ch 43** (and **Ch 40 patched in place** — its §2.2 superseded by Ch 42 §2). Previously Ch 40 and Ch 41, written over Batch 47's twelve grammar nodes and **deliberately split across two folders** (`hindu/shastra/` and `hindu/darsana/`) because the tradition itself changed category. **Chapter coverage is 397 / 397 and `KNOWN_UNCOVERED` is EMPTY.** Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (49) — see the end of the Batch 47 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false "340/340" stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **397 concepts across 48 batches; 43 chapters.** 2473 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 397/397 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---

## ▶ BATCH 49 — OPEN (2026-09-02). Theme: **the grammars that lost.**

**Why this batch.** Batch 48 named it the largest structural hole it opened: *"Batches 40–48 have treated 'Sanskrit grammar' as coextensive with the Pāṇinian tradition."* The dedup-gate grep confirms the shape that opened Batches 47 and 48 — **terms invoked across many committed files against zero nodes**:

| term | files invoking it | nodes |
|---|---|---|
| `Haradatta` | **9** (`astadhyayi`, `helaraja`, `kaiyata`, `kasika`, `madhva`, `nagesha-bhatta`, `panini`, `pratyahara`, `sphota`) | 0 |
| `Jinendrabuddhi` / `Nyāsa` | **8** | 0 |
| `paribhāṣā` | **6** (`astadhyayi`, `bhattoji-dikshita`, `indu`, `karaka`, `kasika`, `nagesha-bhatta`) | 0 |
| `Cāndra` / `Candragomin` | 3 (`kasika`, `mahabhashya`, `vararuci`) | 0 |
| `Kātantra` | 2 (`katyayana`, `vararuci`) | 0 |

⚠ **`Kātantra` scores 92 hits in Abhyankar and 2 in this corpus.** That ratio is the batch's premise in one number.

### The queue

| # | key | state | why |
|---|---|---|---|
| 1 | `katantra` | pending | the rival system — the most-used grammar in eastern India and Kashmir |
| 2 | `sarvavarman` | pending | its author |
| 3 | `candra-vyakarana` | pending | the **Buddhist** grammar; `kasika.md` already records the Kāśikā's awareness of it |
| 4 | `candragomin` | pending | its author. ⚠ dedup: **not** `candrata` (the Āyurvedic commentator, already written) |
| 5 | `jinendrabuddhi` | pending | ⭐⭐ **T2** — see below |
| 6 | `nyasa-vyakarana` | pending | the *Kāśikāvivaraṇapañjikā*. ⚠ tradition-suffixed: `nyāsa` is **also** a Jain/Pāṇinian technical term inside `nikshepa.md` |
| 7 | `haradatta` | pending | the *Padamañjarī*; Batch 48's named control case for Kaiyaṭa's hierarchy |
| 8 | `paribhasha` | pending | the metarule as a technical node — **T4** |
| 9 | `prakrta-prakasha` | pending | Vararuci's Prakrit grammar; the corpus has **no node for Prākṛt grammar at all** |
| 10 | `punyaraja` | pending | *Vākyapadīya* II's commentator; the third leg of the Helārāja/Puṇyarāja pair |

### The four named tests (⚠ **leads to test, not facts** — Batches 44–48 each falsified their own premises)

- **T1 — is the Kātantra a *rival* or a *simplification*?** Expectation: it competes in **use** and not in **theory** — i.e. it never contests Pāṇini's authority, only his pedagogy. If so, "the winner's account" is the wrong frame and the batch's own premise is falsified.
- **T2 — ⭐⭐ is the grammarian Jinendrabuddhi the same man as Dignāga's commentator?** The corpus **already carries both**, in `panini.md`/`kasika.md` (the 8th-c. Buddhist author of the *Nyāsa*) and in `pramana-samuccaya.md` (the *Ṭīkā* from which the lost Sanskrit is reconstructed) — **and has never noticed they share a name.** Either outcome is a result: one man = an unnoticed grammar↔pramāṇa edge; two men = name-collision **#9**, found inside the corpus rather than in a source.
- **T3 — does Haradatta's non-hierarchical reading of the three sages survive first-hand checking?** Deshpande used it to explain why Kaiyaṭa's ladder stops at Patañjali (Batch 48's best result). The corpus is currently holding one side of that contrast without a node for the other.
- **T4 — is *paribhāṣā* Pāṇinian property or shared technology?** The direct test of the batch premise: if the rival systems have their own paribhāṣā literatures, the metalinguistic layer is the discipline's, not one school's.

**Rules in force:** §8 dedup gate before every file · one concept at a time, commit each · Abhyankar re-downloaded and confirmed working (642 "Panini" hits) · Batch 47's source-weighting caution (**specialist = strong on internal knowledge, weak on chronology**) · Batch 48's §0 discipline on optimality/formal-systems claims.

---

## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` → **ALL CHECKS PASS**; chapter coverage **397/397** with an empty `KNOWN_UNCOVERED` table. No outstanding maintenance, no red gate. The next unit of work is a **new concept batch (49)** — suggestions at the end of the Batch 48 run-log below. ⭐ **Batch 48's largest opening is structural**: the corpus has treated "Sanskrit grammar" as coextensive with the Pāṇinian tradition for nine chapters, and has now met two rival systems (Kātantra, Cāndra-Vyākaraṇa) with no nodes for either.

⚠ **Read before opening Batch 49.** Batches 44–48 each falsified their own queue premises. **Batch 48 falsified two of its four named tests (T2, T4) — and T4's false premise was the corpus's own follow-up list.** It corrected or qualified **five** committed concept files and **patched a chapter in place**. The suggestions below are **leads to test, not facts**.

⚠ **A new standing caution on source-weighting, produced by Batch 47 and applying to every future batch:** **"read at first hand" and "specialist" are strong marks for what a discipline knows *internally*** — vocabulary, manuscript contents, which attributions the tradition itself doubts — **and weak for anything depending on outside scholarship that has moved, chronology above all.** Abhyankar (1961) is authoritative on *pratyāhāra* and out of date on Bhartṛhari's century, and both are true of the same book. See Ch 40 §8.2.

⚠ **Abhyankar's dictionary is a session-scratchpad download and does not persist.** Re-downloaded and confirmed working again 2026-09-02. Re-download before any further grammar work — the method is the Meulenbeld one: take `server` and `dir` from `https://archive.org/metadata/dictionary-of-sanskrit-grammar-abhyankar`, then request `DictionaryOfSanskritGrammar_abhyankar_djvu.txt` from that host directly. ⚠ **Use that item, NOT `a-dictionary-of-sanskrit-grammar-kv-abhyankar-1961-gos`** — the latter's OCR is unusable (Devanagari-mis-OCR'd; zero hits for "Panini"). **Confirmed working this batch.**

---

### ⭐ Trajectory: the four structural drifts are queued **separately**, in [`DRIFT.md`](DRIFT.md)

> **📄 [`DRIFT.md`](DRIFT.md) — read it when you want to work a drift, not a batch.** Four problems that are
> **not defects** (nothing there fails `check_all.py`) but that **get measurably worse every batch**: distance
> from primary sources · one-sided disputes · teaching-layer staleness · the follow-up backlog. They are a
> **different kind of work** from a concept batch — none of them produces new nodes — and they will keep
> degrading quietly if only new-node batches are ever run. **Self-contained: it needs only CLAUDE.md and
> itself.** Not loaded at startup, by design (§7), like `coverage.md` and `progress-archive.md`.
>
> **A detector shipped with it:** `python graph/check_staleness.py` — chapters whose covered concepts were
> edited later. **Advisory, deliberately NOT wired into `check_all.py`** (14 of 34 currently flagged; gating on
> it would turn the repo red for every session). See DRIFT.md D3 for why, and for what the test is *not*.

*(The summary below is kept short on purpose — the working detail is in `DRIFT.md`. Written by the Batch 46 session reviewing the corpus's direction across 44–47. It does not replace the Batch 48 suggestions below; it says what to do **with** them.)*

**The project is on track on every metric it measures, and drifting on the one thing it is *for*.** The evidence for "on track" is strong and is worth naming, because it is the machinery working as designed: **Ch 38 §4.1 (Batch 46) found that Navya-Nyāya's signature device had *grammatical* ancestry and recorded that the corpus had no node for Bhartṛhari or the *Vākyapadīya*. One batch later there are twelve grammar nodes.** The corpus told the next session what to build and it got built. Batch 47 then **qualified Batch 46's own generalisation** about reference sources rather than inheriting it. **Cross-session self-correction is the healthiest signal this project has.**

**The drift, in four measurable forms — each with a baseline and a first move in [`DRIFT.md`](DRIFT.md):**

| | drift | measured now |
|---|---|---|
| **D1** | Distance from **primary sources** is growing, not shrinking | 65 of 387 files carry an "identified but not read" list; ~8 added per batch, 1–2 closed |
| **D2** | The corpus records **one side** of several disputes | `P. V. Sharma` appears 4× in Batch 46, **always in rebuttal**, never read directly; 18 files flag single-sourcing |
| **D3** | The **teaching layer is write-once**, and its staleness was invisible to the gate | **14 of 34 chapters stale** (`python graph/check_staleness.py`) — Ch 11 untouched since 2026-06-23 |
| **D4** | The **follow-up debt** from Batches 43–46 is nearly untouched | ~11 items carried; Batch 46 closed 1 and opened 8 |

**Recommendation for Batch 48: spend it on depth and debt** — add new nodes only where a written chapter already depends on a node that does not exist. Growth resumes at 49. ⚠ But the drifts are **independent of any batch**: `DRIFT.md` is designed to be picked up in its own session, and does not need this file's run-logs.

---

## Batch 48 — CLOSED (2026-09-02). 10/10 concepts; 387 → 397 nodes; 2410 → 2473 edges. Plus Ch 42 and Ch 43, and a patch to Ch 40.

Theme: **the commentarial tiers below Pāṇini.** A grep found **19 files** invoking Kaiyaṭa / Kāśikā / Nāgeśa / Yāska / Bhaṭṭoji against **zero** nodes — the identical signal that opened Batch 47. **`python graph/check_all.py` → ALL CHECKS PASS**, chapter coverage **397/397**, structural + conformance audits **CLEAN**.

### The ten

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `kaiyata` | **contested** / medium | ⭐⭐ **T1 confirmed *and* bounded** — the maxim is real and cited (*Pradīpa* on M.Bh. on P. 1.1.29), and it **peaks at Patañjali**, one tier below its own author. |
| 2 | `kasika` | **contested** / medium | ⭐ **The only full commentary on Pāṇini is a beginners' gloss** — and Batch 47's source rule predicted *both* of Abhyankar's postures. |
| 3 | `helaraja` | **contested** / medium | ⭐⭐ **T3: reachable at first hand** (an open-access critical edition) — and reading him **qualified an edge the corpus had already drawn**. |
| 4 | `nagesha-bhatta` | **contested** / medium | ⭐ The tradition's terminus — and a **misparsed appositive** that turned a teaching lineage into a bloodline. |
| 5 | `bhattoji-dikshita` | converged / medium | ⭐ **The order Sanskrit grammar is taught in is not Pāṇini's.** |
| 6 | `kaundabhatta` | converged / medium | ⭐⭐ **The direction of borrowing reverses** — grammar restates its own semantics in Navya-Nyāya's idiom. |
| 7 | `yaska` | **contested** / medium | ⭐⭐ **Follow-up #3 closed at the primary level** — Kautsa's six objections and Yāska's six replies, in Sarup. |
| 8 | `vararuci` | **contested** / medium | ⭐⭐ **T2 falsified — four men**, and Abhyankar's entry is an argument, not a self-contradiction. |
| 9 | `pratyahara` | converged / medium | ⭐ **A theorem read at first hand, and four limits in the author's own words.** |
| 10 | `sphotasiddhi` | converged / medium | ⚠⚠ **T4 falsified — the gap was in the follow-up, not the corpus.** |

### The four named tests, and how they came back

| test | queued expectation | result |
|---|---|---|
| **T1** — is Kaiyaṭa's *yathottaraṃ* maxim real and his? | yes, hopefully verifiable | ✅ **Confirmed, with an address** — Deshpande's Gonda Lecture gives *Pradīpa* on M.Bh. on P. 1.1.29, Vol. I: 217. ⚠ **And bounded**: "it effectively peaks in Patañjali." **Two committed files corrected** (`mahabhashya.md`, `vyakarana.md`) **plus Ch 40 §2.2.** |
| **T2** — can a node hold the Vararuci split whole? | a two-way split | ❌ **Falsified twice over.** The split is **four-way**, numbered by Abhyankar himself — and reading the entry in **full** shows it is a **disambiguation that argues**, not the pathology Batch 47 diagnosed from two-thirds of it. Batch 46's *set-of-witnesses* generalisation survives; the stronger claim does not. |
| **T3** — is Helārāja reachable at first hand? | probably `blocked` (2 bare Abhyankar hits) | ✅ **Confirmed, better than expected** — Li's Cambridge PhD (2018) is an open-access critical edition **and translation**. ⭐ **A D1 result.** And it forced a caveat onto `avacchedaka.md`. |
| **T4** — does the *Sphoṭasiddhi* change `mandana-mishra.md`? | yes — "a node the corpus thought it knew has a second career" | ⚠⚠ **False premise.** `mandana-mishra.md` **already had it**, in front-matter *and* gloss. A §4-signal-4 grep would have closed the follow-up before it opened. |

### ⭐ The engine findings

**1. Who decides how big a text is.** The batch's governing question, and the answer is always *a commentator, invisibly*. Abhyankar: the Aṣṭādhyāyī's count is 3,983 "as commented upon by the writers of the **Kāśikā and the Siddhāntakaumudī**" — a 7th-c. beginners' gloss and a 17th-c. re-ordering, a millennium apart, cited as one canon. Of those, **Patañjali reclassifies 9 as Vārttikas and 2 as Gaṇasūtras**. Seventeen centuries later **Nāgeśa** reclassifies *Vārttikas* into two classes and Kātyāyana's corpus falls **~5,000 → ~1,400** — and "there are **some manuscript copies which give this reduced number**." ⭐ **The tradition's first great commentator and its last both resize a canon by reclassifying genre. Neither discovers anything.**

**2. ⭐⭐ The ladder's own rule installs a ceiling below the ladder's top.** Kaiyaṭa wrote a principle of *ascending* authority that stops at Patañjali — tier 3 — while himself standing on tier 4 and Nāgeśa on tier 5. Nāgeśa's empirical gloss (*uttarottarasya bahulakṣyadarśitvāt*, "the later has seen wider usage") **over-generates**: by his own reason he should outrank Patañjali, and he instead calls him *bhagavān*. **Deshpande's explanation is the batch's best single result:** Kaiyaṭa knew Patañjali-as-Śeṣa and *not* Pāṇini-taught-by-Śiva, while **Haradatta** knew the reverse and produced a *complementary*, non-hierarchical view. ⭐ **The ranking stops at Patañjali because the myth stops at Patañjali** — extending `patanjali.md`'s Batch 47 "theological motor" finding from the *conflation* to the *authority structure*. (Deshpande hedges with "perhaps"; recorded with his hedge.)

**3. ⭐⭐ The traffic between grammar and logic runs both ways.** Batches 46/47 established grammar → Navya-Nyāya (the *avacchedaka*'s ancestry). Batch 48 found the return leg: **Bhaṭṭoji and Kauṇḍabhaṭṭa "respond to Naiyāyikas and Mīmāṃsakas by reformulating" the speech-form/meaning relation "in terms of cognition."** Two separate transfers, five centuries apart, opposite directions, each sourced; **no net "influence" asserted.** Ch 38 had one leg of a two-way exchange.

**4. ⭐ The reading-apparatus mechanism caught on the corpus's own citation.** Li's critical edition shows **Helārāja reading five philosophical schools out of Bhartṛhari's five synonyms of *dravya*** — two of them Advaita, which Bronkhorst finds "conspicuously absent in listings of philosophical schools during Bhartṛhari's time." `avacchedaka.md`'s central claim reaches *Vākyapadīya* III **through Helārāja's gloss**. **Edge not withdrawn** — Li treats a *different* chapter, and the corpus checked — but the caveat is now on it: **the corpus has never seen those verses apart from the commentary.** This is `sphota.md`'s Batch 47 finding in a second literature, and the first time the corpus caught it operating on **itself**. ⚠ Batch 47's corollary applied throughout: **the mechanism is not corrupting, it is invisible.**

### ⚠ Six sources caught being wrong — five on chronology or genealogy, and the sixth is us

| # | source | failure |
|---|---|---|
| 1 | **Abhyankar** | Kaiyaṭa: a flat "11th century" where careful usage gives only a *pre-13th-c.* bound |
| 2 | Wikipedia, *Siddhāntakaumudī* | its author "lived during **1700–1800**" — ~150 years off — and an 1870 **print** date given as the work's date |
| 3 | Wikipedia, *Kāśikāvṛttī* | "c. the 7th century" with **no evidence offered at all** |
| 4 | **Hindupedia** | "Bhaṭṭoji Dīkṣita was his grandfather" (of Nāgeśa) — see below |
| 5 | search summaries | reproducing Abhyankar verbatim and reading as independent corroboration |
| 6 | ⚠ **this corpus** | Batch 47 follow-up #2 (T4) |

⭐ **#4 is worth keeping as a specimen.** Three sources say *"Nāgeśabhaṭṭa was a pupil of Haridīkṣita, **the grandson of Bhaṭṭojidīkṣita**."* Drop the teacher and the appositive re-attaches to Nāgeśa. **A relative clause changing which noun it modifies turns a teaching lineage into a blood one.** ⚠ **And the check reversed the blame**: the obvious inference was that the *summariser* misparsed; fetching Hindupedia directly showed **the page itself asserts it**. Hindupedia also names Nāgeśa's father as **Śiva Bhaṭṭa** — the entry carrying the material that sits badly with its own claim, which is **the Vararuci pattern in a crowd-sourced source**. The generalisation holds across both source types, as predicted.

⭐ **And #6 is the one that matters.** The corpus has spent two batches charging reference works with not checking themselves across their own entries. **`sphotasiddhi` is that defect, in this corpus.** Recorded rather than dropped: *a batch that reports only the tests it passes is not running tests.*

### §0 discipline — `pratyahara`, the batch's most exposed node

**Petersen 2004 (Proposition 4.2: "Pāṇini's Śivasūtras form an optimal S-alphabet") was read as a PDF, not through summaries** — deliberately, because it is the most inflatable claim in the grammar literature. The proof is real (Hasse-diagram planarity; a K₃,₃ minor; **249 K5-triples** forcing the doubled *h*). **Four limits taken from the author's own words**, including that optimal **explicitly does not mean shortest** — "provably the shortest possible alphabet" is **false**, and is the form the claim usually takes. **No formal-systems edge drawn**, on the `avacchedaka` precedent. ⭐ What *is* earned: the ordering is demonstrably fitted to the classes the grammar needs — and **Kiparsky (1991) reached the same result from inside Pāṇini's own economy principle**, sharing no premises. ⚠ Kiparsky unread.

### What the batch did to its own corpus

**Five committed files corrected or qualified, and one chapter patched in place:**

1. **`mahabhashya.md`** — the *yathottaraṃ* maxim gave "doctrinal warrant" to a five-tier climb it does not reach. Corrected; the parallel to `tattvacintamani` is now **closer**, not weaker — in both literatures the climb is unlicensed.
2. **`vyakarana.md`** — Batch 47's "unverified at first hand" caveat **discharged**, and its scope corrected.
3. **`katyayana.md`** — Batch 47's "pathology of the entry as a unit of writing" **narrowed** to the true defect: a missing cross-reference. Plus the *gotra*-name mechanism it did not have.
4. **`avacchedaka.md`** — the Helārāja caveat added to its central edge.
5. **`astadhyayi.md`**, **`panini.md`**, **`mandana-mishra.md`**, **`bhattoji-dikshita.md`** — new typed edges (the Kāśikā's full coverage against the Mahābhāṣya's 31%; the Pāṇini/Yāska shared roster; the *Sphoṭasiddhi*).
6. ⭐ **`chapters/hindu/shastra/40-what-grammar-was-for.md` patched in place** — §2.1's provenance flag marked RESOLVED, and **§2.2 given a SUPERSEDED banner** pointing at Ch 42 §2. **The first time a chapter in this corpus has been corrected by a later one rather than left to go quietly stale** (`DRIFT.md` D3).

### Name-collisions: two more, taking the running total to eight

**`Kāśikā`** — flagged by **Abhyankar himself** before the corpus could make it: the title is reused for unrelated commentaries "as possibly they were written at Kāśī" (Hari Dīkṣita's on the *Vaiyākaraṇabhūṣaṇasāra*; Vaidyanātha's on the *Paribhāṣenduśekhara*). **`Sphoṭavāda`** — Kauṇḍabhaṭṭa wrote one; per LinguIndic so did Nāgeśa; **neither read.** ⭐ **Three different generators now on record: a personal name (Vararuci, Patañjali, Kātyāyana), a place-name (Kāśikā), a doctrine-name (Sphoṭavāda).**

### The teaching layer

| ch | title | folder | nodes |
|---|---|---|---|
| **42** | The Ladder and the Boundary: Pāṇini's Commentators & the Size of a Text | `hindu/shastra/` | 7 |
| **43** | Meaning Read In: Helārāja, Kauṇḍabhaṭṭa & What Commentary Adds | `hindu/darsana/` | 3 |

The two-way split **repeats Ch 40/41's on purpose**: technique → śāstra, theory of meaning → darśana. Same batch, in two cases the same century, different category.

### Follow-ups carried into Batch 49

**New, from this batch:**

1. ⭐⭐ **The rival grammars.** Batches 40–48 have treated "Sanskrit grammar" as coextensive with the Pāṇinian tradition. This batch brushed against **two** rival systems: the **Kātantra** (Sarvavarman + Vararuci's 4th adhyāya) and the Buddhist **Cāndra-Vyākaraṇa**. **No node for either, or for Prākṛt grammar at all.** The largest structural hole the batch opened.
2. ⭐ **Kiparsky, "Economy and the Construction of the Śivasūtras" (1991)** — known through one sentence of Petersen's; the independent half of `pratyahara`'s strongest claim.
3. ⭐ **K. A. Subramania Iyer** would supply **two** unread primary texts at once: the *Sphoṭasiddhi* (1966, text + English translation) and *Vākyapadīya* III with Helārāja (Deccan College, 1963 — which contains the **Adhikaraṇasamuddeśa**, the one item that would settle the `avacchedaka` caveat either way).
4. **Vergiani, "Āgamārthānusāribhiḥ: Helārāja's use of quotations"** (*J. Indian Philos.* 2014) — directly on `helaraja`'s central question; paywalled.
5. **The Kāśikā's date.** Every source asserts the 7th century; the only evidence anyone cites is **Yijing** — the witness `bhartrhari.md` records the consensus as having **discredited**. **One sentence of one pilgrim, rejected where it dates Bhartṛhari and relied on where it dates Jayāditya.** Recorded as a tension; the primary scholarship is unread.
6. **Pascale Haag, *Studies in the Kāśikāvṛtti: The Section on Pratyāhāras*** — a critical edition of the passage where the tradition states the doctrine; would test `pratyahara`'s philological half at first hand.
7. **Kumārila's *Ślokavārttika* on sphoṭa** — the corpus holds the objection's *existence*, not its text. **Exactly the position Ch 40 §7 was in about Kautsa, which Ch 42 §7 fixed. The precedent says it is fixable.**
8. **The *Vaiyākaraṇabhūṣaṇasāra*** (ch. XIV, *Sphoṭanirṇaya*, separately translated) — the cheapest way to read Kauṇḍabhaṭṭa at all. And ⚠ **is Bhaṭṭoji's *Vaiyākaraṇasiddhāntakārikā* the same text as his *Vaiyākaraṇamatonmajjana*?** Very likely; unstated by any source consulted.
9. **Deshpande 1998** (*HEL* 20/1) — Persée serves metadata only and 403s on the PDF; ResearchGate 403'd in Batch 47. The 2018 lecture supersedes the need but not the argument.
10. **"Appayya Dīkṣita and the Lineage of Bhaṭṭoji Dīkṣita"** (*J. Indian Philos.* 2014) — would settle the genealogy that #4 above turns on.

**Carried from earlier batches, still open:** Phillips's *Tattvacintāmaṇi* translation; **Matilal 1968 Parts II–III, in hand and still unused — the cheapest high-value item in the corpus**; Potter's *Padārthatattvanirūpaṇa*; Neevel 1977; the *Ratnaprabhā* and *Siddhayoga*; **P. V. Sharma** (met four times in Batch 46, always in rebuttal); Ingalls 1951; the D. Ch./D. C. Bhattacharyya question; the Digvijaya dating tension in `shankara.md`; `karma-vargana.md` still the only `low`-confidence node; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; **Valerie Stoker**; Lance Nelson; a critical *Lakṣaṇāvalī*; the *Vākyapadīya*'s "635 verses"; Kaiyaṭa's fuller *Mahābhāṣyadīpikā*; **Renou, Woods (1914), Dasgupta (1922)**. ⚠ **Ch 11 is now eleven chapters out of date.**

⭐ **Batch 47 follow-ups CLOSED this batch:** #1 (the *yathottaraṃ* maxim — verified **and** bounded), #3 (the Kautsa controversy — Yāska's reply read in Sarup), #5 (the kāṇḍa I–II *Vṛtti* — narrowed, with Aklujkar named). #2 was **falsified as a false premise**.

### Suggested Batch 49 (names only — **leads to test, not facts**)

- ⭐ **Opened directly by this batch, and the structural hole:** `katantra` · `sarvavarman` · `candra-vyakarana` / `candragomin` · `prakrta-prakasha` — **the non-Pāṇinian grammars.** A batch here would test whether the corpus's picture of "Sanskrit grammar" has been the winner's account all along.
- **Also opened:** `haradatta` (whose *complementary* reading of the three sages is the control case for Kaiyaṭa's hierarchy) · `punyaraja` · `jinendrabuddhi` / `nyasa` · `vaidyanatha-payagunde` (tier 6) · `varadaraja` · `sesha-krsna` · `paribhasha` as a technical node.
- **Still open from Batches 46/47:** `madhava-nidana` / `madhavakara` · `vijayaraksita` · `srikanthadatta` · `annambhatta` / `tarkasangraha` · `jagadisha-tarkalankara` · `vardhamana-upadhyaya` · `sridhara` · `jayanta-bhatta` · `parasara-bhatta` · `yadavaprakasha`.
- **Maintenance:** ⚠ **Ch 11 predates the entire Advaita-lineage cluster and now also Chs 36–43.** ⭐ **Ch 40 shows the fix is cheap** — a SUPERSEDED banner and a pointer, not a rewrite.
