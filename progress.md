# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 50 CLOSED — 410 concepts, 2564 edges** (a DEPTH batch: 3 nodes, 2 primary sources read, 4 committed files corrected) (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 46** (*Opening the Book*), and before it Ch 44 and Ch 45 (and **Ch 40 patched in place** — its §2.2 superseded by Ch 42 §2). Previously Ch 40 and Ch 41, written over Batch 47's twelve grammar nodes and **deliberately split across two folders** (`hindu/shastra/` and `hindu/darsana/`) because the tradition itself changed category. **Chapter coverage is 410 / 410 and `KNOWN_UNCOVERED` is EMPTY.** Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (51) — see the end of the Batch 50 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false "340/340" stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **410 concepts across 50 batches; 46 chapters.** 2564 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 410/410 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---


## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` → **ALL CHECKS PASS**; chapter coverage **410/410** with an empty `KNOWN_UNCOVERED` table. No outstanding maintenance, no red gate.

⭐⭐⭐ **Batch 50 was the corpus's first deliberate DEPTH batch, and it paid.** Three nodes and two books read at first hand **corrected four committed files, superseded one of the corpus's own proposed mechanisms, added a seventh collision generator, and turned up a §0 failure mode the charter does not name.** ⚠ **Ten shallow nodes would not have done any of that** — and `DRIFT.md` D1 says the shallow route is the one the corpus defaults to. **Consider running another depth batch before resuming growth.**

▶ **The next unit of work has an obvious shape: FINISH BATCH 50'S QUEUE.** ⚠ It was **cut short at the user's request** with **six of ten concepts unwritten** — `vyadi`, `maitreya-raksita`, `jainendra-vyakarana`, `devanandin`, `sakatayana`, `candrakirti`. All are still free keys, all still opened by Batch 49, and `vyadi` is referenced in five committed files and written in none. **Depth read D-C (*Vākyapadīya* II with Puṇyarāja) was also not attempted and remains the cheapest open item.**

⚠ **One question for the user, not decidable here (§10 fork).** Batch 50 finding 7 argues that **§0 should name inflation into modern *politics* alongside modern physics** — same mechanism, and a specialist aims it at this repository's own anchor tradition. **That is an edit to the prime directive, so it is left for you.**

⚠ **Read before opening Batch 51.** Batches 44–50 each falsified something they queued. **Batch 49 confirmed three of its four named tests, falsified the *frame* of the fourth, and then falsified its own headline finding two nodes after committing it.** It corrected or qualified **five** committed files, **two of them written inside the same batch**. The suggestions below are **leads to test, not facts**.

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

---

## Batch 50 — CLOSED (2026-09-02). **The corpus's first deliberate DEPTH batch.** 3 new nodes; 407 → 410; 2545 → 2564 edges. Plus Ch 46.

Theme: **read the sources this corpus had been describing at second hand.** ⚠ **Cut short of its ten-concept queue at the user's request** — six queued names stand unwritten, listed below. **`python graph/check_all.py` → ALL CHECKS PASS**; chapter coverage **410/410**, `KNOWN_UNCOVERED` empty, structural + conformance audits **CLEAN**, **0 orphans, 0 unwritten stubs**.

### The depth reads — the actual unit of work

| id | source | Batch 49 follow-up | result |
|---|---|---|---|
| **D-A** | **Cowell 1854**, the *Prākṛtaprakāśa* with Bhāmaha's *Manoramā* (archive.org `b30093016`) | **#2** | ⭐⭐⭐ **READ.** An 1854 critical edition from six collated MSS **with an English translation** — usable under §1 precisely because someone else did the translating |
| **D-A′** | **Andrew Ollett, *Language of the Snakes*** (archive.org `dli.doa.049`) | **#9** | ⭐⭐⭐⭐ **READ, and Batch 49's record of it CORRECTED.** Batch 49 filed it "located and NOT retrievable"; MUSE and the author's page are still dead, but the DOAB copy is on archive.org. **The corpus had recorded a dead end as a property of the book rather than of the route it tried.** |
| **D-B** | Kāśikāvṛtti with the *Padamañjarī* + *Nyāsa* | **#1 = T3** | ⚠ **ATTEMPTED, NOT DISCHARGED — and the follow-up turns out to have been mis-specified.** See below |
| **D-C** | ***Vākyapadīya* II with Puṇyarāja** | **#3** | ⚠ **NOT ATTEMPTED** — batch ended first. Still the cheapest open item |

### The three nodes

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `bhamaha` | contested / medium | ⭐⭐ **Collision #13 — and the corpus's own Batch 49 rule predicted the specialist's verdict in a case it had not seen.** |
| 2 | `sauraseni` | contested / medium | ⭐⭐⭐ **The same gap read twice**: Cowell's *loss* vs Ollett's *terminus*, decided by an 11th-c. witness. The corpus's first node for a Prākṛt **language**. |
| 3 | `durgasimha` | contested / **low** | ⭐⭐⭐ **An attribution caught happening between two manuscripts.** Four identity questions on one name; the corpus's third `low` node, for a third distinct reason. |

### ⭐ The engine findings

**1. ⭐⭐⭐⭐ The corpus's most interesting unsourced claim was true, and the finding built on it was the wrong size.** Batch 49 filed "8 chapters expanded to 12" as **terminal-module architecture**. Ollett proves it from **one word** — "Māhārāṣṭrī" appears in the expanded recension and not the older one, because the core text had nothing to contrast its subject with — and shows the addition was **ontological**: "a **pluralization of the category of 'Prakrit'**… Prakrit, now Māhārāṣṭrī, no longer stood **above** the other languages, but **alongside** them." ⭐ **Adding three chapters demoted the book's own subject from a genus to a species.** ⚠ The corpus had the shape of the event and none of its content **because it had read *about* the text and not *in* it** — `DRIFT.md` D1 as a worked example rather than a metric.

**2. ⭐⭐⭐ And the mechanism the corpus proposed is superseded.** Batch 49's "the organisation that makes a grammar teachable makes its parts detachable" is replaced, for **two of its three instances**, by a documented event: the threefold schema became **sixfold** (adding Śaurasenī, Māgadhī, Paiśācī) in **Rudraṭa, Kashmir, early 9th c.**; the "expanded" *Light* is listed among the multilingual grammars of that moment, and **Hemacandra's book 8 adopts the six languages as its organizing principle**. ⚠ **Untested for the third instance** (the Cāndra's Vedic chapters, *lost* rather than added). **Recorded as supersession, not refutation** — the earlier reasoning generalised from architecture when the evidence was about audience.

**3. ⭐⭐⭐ The same gap, read twice — and the corpus made the error too, inside this batch.** Cowell reads the missing Bhāmaha commentary on §XII as **loss** (and on that basis leaves it untranslated, the only such section). Ollett reads it as a **terminus**, with **Abhinavagupta** (11th c.) describing a Vararuci "**excluding regional languages such as Śaurasenī." ⚠⚠ `bhamaha.md` was **written and committed** taking Cowell at face value and building a Ch 45 illustration on it; `sauraseni` corrected it hours later. ⭐ **Batch 49 caught a transmission accident read as an authorial choice; this is the mirror — a redactional terminus read as a transmission accident.** Both sit at the **end** of a text, where "absent" and "lost" are hardest to tell apart.

**4. ⭐⭐⭐ A seventh collision generator, and unlike the six it is not confusion but WARRANT.** Ollett: "**Vararuci-Kātyāyana was the go-to sage for authorizing additions and interventions in these new non-Pāṇinian systems.**" ⭐ **The attributions are not errors; they are claims.** The corpus now separates *is this the same man?* (usually no) from *why was he named?* (usually a reason). ⭐⭐ And `durgasimha` supplies the mechanism as a **bare catalogue fact**: the Kātantra *Paribhāṣāvṛtti*'s **Poona MS is anonymous; the India Office copy names Durgasiṃha**. One text, two manuscripts, an author appearing in one of them.

**5. ⭐⭐ T4 confirmed in a stronger form than Batch 49 could reach.** Read at first hand in Cowell: **I.1 and II.1 are *adhikāra*s, IV.1 turns on a *pratyāhāra*, and Cowell glosses I.1 by citing Pāṇini I.1.70.** ⭐ **The shared metalanguage crosses the *language* boundary**, not merely the boundary between rival Sanskrit systems.

**6. ⭐⭐ The rule against arguments from silence is a scalpel, not a broom.** `bhamaha` discounted Ollett's Abhinavagupta point wholesale. Ollett draws **two** inferences from him and only one is from silence; the other is a **positive description of the text's contents** — and it is what overturns Cowell. ⚠ **Using Batch 49's rule as a broom cost the node a real fact for several hours.**

**7. ⚠⚠ A §0 failure mode the charter has no name for: inflation into modern POLITICS.** Pischel's **Jain Śaurasenī** is the **Digambara doctrinal language** — so `kundakunda` and `samayasara` are in it, which nothing in this repository previously said. ⚠ Ollett's warning travels with the fact: the "Prākṛt = popular = egalitarian Jainism" story is "**sentimental and indigenist**." ⭐ **Identical mechanism to the physics case §0 already guards against — a structural fact quietly mapped onto a flattering modern category — and aimed at the tradition this repository is anchored on.**

**8. ⭐⭐⭐ The mis-specified follow-up.** T3 was carried as "**cheap** — the text is free on archive.org." The download works (3.8 MB) and its OCR is garbled Devanagari — **but that is not the real obstacle.** The *Padamañjarī* is an **untranslated** Sanskrit commentary and **§1 forbids this corpus from translating it**; what T3 needs is a published translation or study, and a bounded search found none. ⭐ **"Free on archive.org" was never a reason to think T3 was cheap.** ⚠ **General lesson for the queue (D1): a *located* source is not a *read* one, and an *untranslated* located source may not be readable at all. A follow-up list that does not distinguish these overstates its own health.**

### ⚠ Sources caught being wrong — and three of the six are us

| # | source | failure |
|---|---|---|
| 1 | **Cowell 1854** | reads a **terminus as a loss** (§XII); dates **Hemacandra to the 13th c.** (he is 12th — corrected by Ollett *and* by this corpus's own node); and grounds the Vararuci=Kātyāyana identification on "**universal popular belief**… and the direct testimony of Somadeva" — ⭐ **the *Kathāsaritsāgara*, i.e. the exact evidential circle `sarvavarman` identified. He states it openly, which is what makes correction possible** |
| 2 | **Cowell 1854** | the **Kaccāyana inference**, made on the name alone — ⭐⭐ **and Batch 49's rule picks Ollett over him without knowing either.** Follow-up #12's Pali half answered; **the Dravidian half remains untested** |
| 3 | **Abhyankar** | prints **two unreconciled notices** of the *Kātantradhātuvṛtti* *Manoramā*'s author; **has no headword for this Bhāmaha at all** |
| 4 | ⚠ **this corpus** | `bhamaha.md` — the "lost commentary" reading, **corrected within the same batch** (finding 3) |
| 5 | ⚠ **this corpus** | `bhamaha.md` — the over-broad refusal of an argument from silence (finding 6) |
| 6 | ⚠ **this corpus** | `haradatta.md` cited **Wikipedia "Padamañjari" and "Haradatta" as two sources**; a fetch of the latter returns the former **verbatim**. ⭐ **Third instance in three batches of one text nearly counted as two — and the first the corpus did to itself, in the very node that flagged the wisdomlib=Abhyankar trap** |

⭐ **A seventh that is not a failure but is worth recording**: a web-search summary asked directly whether the two Bhāmahas are one man answered "**No**" — by explaining that the *Manoramā* and the *Kāvyālaṅkāra* are **different works**, which was never the question. **A confident right-shaped answer for the wrong reason**, and the corpus would have cited it as independent agreement with Ollett.

### The collision taxonomy: now seven generators and fifteen candidates

⭐ **New generator (7th): the name as WARRANT** — deliberate, not accidental (finding 4).
**New candidates:** **#13** Bhāmaha (grammarian / ālaṅkārika) — **split**, by Ollett *and*, independently and earlier, by **Ghosh**; **#14** Durgasiṃha / Durgācārya (Kātantra / *Nirukta* — two *vedāṅgas*), raised by Abhyankar and left open; **#15** Durgasiṃha = **Amarasiṃha**, "some scholars" holding the name to be **a title** — ⭐ the inverse form: one man, two designations, one of them not a name. Plus two flagged and undecided: **"Appayya Dīkṣita III"** and an **Utpaladeva** who commented on a lost *Prākṛtadīpikā*.

### What the batch did to its own corpus

**Four committed files corrected, two of them written inside this batch:**
1. **`prakrta-prakasha.md`** — rewritten on first-hand reading: the 8→12 claim confirmed *and reinterpreted*, the structure counted (521 sūtras, 12 sections), the four things it said it did not know answered, the `katantra` parallel **narrowed to method-not-content**, the `candra-vyakarana` parallel **corrected**.
2. **`bhamaha.md`** — twice (findings 3 and 6), hours after being committed.
3. **`haradatta.md`** — T3's mis-specification, collision #12 advanced **on non-name evidence for the first time**, the date question moved (a source from another śāstra independently lands beside the 13th-c. outlier), and the two-Wikipedias defect.
4. **`sauraseni.md`/`prakrta-prakasha.md`** — `part-of` replaced by **`aggregates-into`/`aggregates-from`** on purpose: ⭐ *it was not a part of the book, it became one.*

⭐ **And two edges were written and then removed rather than forced**: §5 has no type for "is the evidence for," and a person is not `part-of` a language. **Some real relations get no edge.**

### ⚠ What this batch did NOT do

- **Six queued concepts unwritten**: `vyadi`, `maitreya-raksita`, `jainendra-vyakarana`, `devanandin`, `sakatayana`, `candrakirti`. All still free keys; all still opened by Batch 49.
- **D-C not attempted** — the *Vākyapadīya* II / Puṇyarāja read that would close the Candrācārya question.
- **T3 not discharged** (finding 8) and **Olivelle not read** — now known to be **paywalled** (Springer 303 → auth endpoint; academia.edu 403; DOI lookup 404). ⭐ **The sharpest single D2 item the corpus holds: a specialist has answered collision #12 and the corpus cannot read the answer.**

### Follow-ups carried into Batch 51

1. ⭐⭐ **D-C: *Vākyapadīya* II.481–490** with Puṇyarāja's *Ṭkā*, or **Iyer's English kāṇḍa II** — unchanged from Batch 49, and now the **cheapest** open item.
2. ⭐⭐ **Nitti-Dolci, *Les grammairiens prakrits* (1938/1972)** — **new top D2 item**: the source of both the grammar-of-a-text thesis and the demonstration of the expansion, known to the corpus **only through Ollett**.
3. ⭐ **Ollett is downloaded and only ch. 5–6 were read.** ⚠ 941 KB, 1,920 "Prakrit" hits — chs. 1–4 and 7 are unread and bear directly on `sauraseni`, `digambara`, `kundakunda`.
4. **Ghosh's *Prākṛtakalpataru* introduction, pp. xvii–xviii** — the independent argument against the Bhāmaha identification.
5. **Eggeling 1876**, the Kātantra with Durgasiṃha's commentary — out of copyright, and ⭐ **the book through which the Kātantra actually reached modern scholarship**.
6. ⭐ **Abhyankar's *Paribhāṣāsaṃgraha* (B.O.R.I.)** — now with a **second** reason: he cites it for the Poona-vs-India-Office manuscript question.
7. **Olivelle (paywalled)**; **Pischel**; **Westergaard 1862** (nine Kātyāyanas); **Rudraṭa** and **Namisādhu (1069)**; the ***Nāṭyaśāstra*** — ⚠ **the corpus still has no node for it**; **Durgācārya on the *Nirukta*** (the other half of #14).
8. ⚠ **The Dravidian half of Batch 49 follow-up #12** — untouched.
9. ⚠ **`paribhasha.md` flagged**: its census row "Durgasiṃha, 65 maxims" rests on an attribution **its own source doubts**. The count survives; the attribution does not.
10. ⚠ **A charter question for the user (§10 fork, not decided here):** finding 7 suggests **§0 should name inflation into modern *politics* alongside modern physics.** That is an edit to the prime directive and is **not** a mechanical fix.

**Carried from earlier batches, still open:** Phillips's *Tattvacintāmaṇi*; **Matilal 1968 Parts II–III, in hand and still unused**; Potter; Neevel 1977; the *Ratnaprabhā* and *Siddhayoga*; **P. V. Sharma**; Ingalls 1951; the D. Ch./D. C. Bhattacharyya question; the Digvijaya dating in `shankara.md`; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; **Valerie Stoker**; Lance Nelson; Renou, Woods (1914), Dasgupta (1922); Vergiani 2014; Deshpande 1998; the *Vaiyākaraṇabhūṣaṇasāra*; **Kobayashi 1977**; **Aklujkar 1974/1972**; the *Asiatische Studien* 2018 paribhāṣā issue; Liebich 1919; Hoernle 1880. ⚠ **`durgasimha.md` becomes the corpus's third `low`-confidence node**, joining `karma-vargana` (thin sources) and `sarvavarman` (one source that is a fairy tale) — **for a third distinct reason: one good source that says four times over that it does not know.** ⚠ **Ch 11 is now fourteen chapters out of date.**

### Suggested Batch 51 (names only — **leads to test, not facts**)

- ⭐⭐ **Finish Batch 50's queue first** — six names, all still opened and unwritten: `vyadi` (pre-Patañjali; the first paribhāṣā writer; referenced in 5 files) · `maitreya-raksita` · `jainendra-vyakarana` / `devanandin` · `sakatayana` (⚠ two of them) · `candrakirti`.
- ⭐ **Opened by this batch:** `natyashastra` (⚠ a real hole — `chapters/INDEX.md` already reserves `hindu/shastra/` for it) · `maharastri` · `rudrata` · `nitti-dolci`? (no — people, not scholars) · `amarakosha` · `durgacarya` · `kavyalankara-bhamaha`.
- **Still open from 46–49:** `madhava-nidana` / `madhavakara` · `vijayaraksita` · `srikanthadatta` · `annambhatta` / `tarkasangraha` · `jagadisha-tarkalankara` · `vardhamana-upadhyaya` · `sridhara` · `jayanta-bhatta` · `parasara-bhatta` · `yadavaprakasha` · `vaidyanatha-payagunde` · `varadaraja` · `sesha-krsna` · `bhoja` / `sarasvatikanthabharana`.
- ⭐⭐⭐ **And the depth batch earned its keep — do it again.** Three nodes and two books corrected **four committed files, superseded one of the corpus's own mechanisms, added a collision generator, and found a §0 failure mode the charter does not name.** ⚠ **Ten shallow nodes would not have done any of that**, and `DRIFT.md` D1 says the shallow route is what the corpus defaults to.
