# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 49 CLOSED — 407 concepts, 2545 edges** (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 44 and Ch 45** (and **Ch 40 patched in place** — its §2.2 superseded by Ch 42 §2). Previously Ch 40 and Ch 41, written over Batch 47's twelve grammar nodes and **deliberately split across two folders** (`hindu/shastra/` and `hindu/darsana/`) because the tradition itself changed category. **Chapter coverage is 407 / 407 and `KNOWN_UNCOVERED` is EMPTY.** Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (49) — see the end of the Batch 47 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false "340/340" stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **407 concepts across 49 batches; 45 chapters.** 2545 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 397/397 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---


## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` → **ALL CHECKS PASS**; chapter coverage **407/407** with an empty `KNOWN_UNCOVERED` table. No outstanding maintenance, no red gate. The next unit of work is a **new concept batch (50)** — suggestions at the end of the Batch 49 run-log below. ⭐ **But read the last bullet there first: Batch 49 argues for a DEPTH batch instead**, and names three free, located primary sources that would each close a named test. ✅ **Batch 48's largest opening — the rival grammars — was CLOSED by Batch 49**, which wrote both systems, both authors, the corpus's first Prākṛt-grammar node, and the shared metalanguage. ⭐ **Batch 49's own largest opening is different in kind: it is DEBT, not coverage.**

⚠ **Read before opening Batch 50.** Batches 44–49 each falsified something they queued. **Batch 49 confirmed three of its four named tests, falsified the *frame* of the fourth, and then falsified its own headline finding two nodes after committing it.** It corrected or qualified **five** committed files, **two of them written inside the same batch**. The suggestions below are **leads to test, not facts**.

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

## Batch 50 — OPEN (2026-09-02). **The DEPTH batch the corpus asked for.**

Theme: **read the primary sources this corpus has been describing at second hand.** Batch 49 closed by arguing
that follow-ups 1–3 were free, located, and would each close a named test. This batch takes that advice.

### Depth reads (each discharges a named Batch 49 follow-up)

| id | source | follow-up | state |
|---|---|---|---|
| **D-A** | **Cowell 1854**, *The Prākṛta-prakāśa … with the Commentary (Manoramā) of Bhāmaha* (archive.org `b30093016`, 390 KB djvu.txt, clean OCR) | **#2** | **READ** |
| **D-B** | **Kāśikāvṛtti with the *Padamañjarī* and the *Nyāsa*** (archive.org `wssi_kasika-vritti-part-1-…`) | **#1 = T3** | pending |
| **D-C** | ***Vākyapadīya* II with Puṇyarāja's *Ṭīkā*** / Iyer's English kāṇḍa II | **#3** | pending |

### The queue

| # | key | state | why |
|---|---|---|---|
| 1 | `bhamaha` | pending | opened by D-A — the Manoramā's commentator, and **collision candidate #13** (grammarian vs. the *Kāvyālaṅkāra*'s ālaṅkārika) |
| 2 | `sauraseni` | pending | opened by D-A — ⭐ the dialect that is *prakṛti* to two others **and whose commentary is lost** |
| 3 | `vyadi` | pending | pre-Patañjali; the first paribhāṣā writer. Referenced in 5 files, written in none |
| 4 | `durgasimha` | pending | the Kātantra's commentator; a live 8th-vs-9th/10th-c. split |
| 5 | `maitreya-raksita` | pending | the *Tantrapradīpa* — the text Batch 49's OCR defect misattributed |
| 6 | `jainendra-vyakarana` | pending | the Jain Sanskrit grammar |
| 7 | `devanandin` | pending | its author |
| 8 | `sakatayana` | pending | ⚠ two of them — another collision |
| 9 | `candrakirti` | pending | "the clearest hole" (Batch 49) |
| 10 | *(reserved)* | pending | to be set by whichever of D-B / D-C opens the most |

⚠ **Scope-lock (§8).** Work only these, in order, one at a time, committing each. Typed links to unwritten
nodes are allowed; writing those files this run is not.

---

## Batch 49 — CLOSED (2026-09-02). 10/10 concepts; 397 → 407 nodes; 2473 → 2545 edges. Plus Ch 44 and Ch 45.

Theme: **the grammars that lost.** **`python graph/check_all.py` → ALL CHECKS PASS**; chapter coverage **407/407**, `KNOWN_UNCOVERED` empty, structural + conformance audits **CLEAN**, **0 orphans, 0 unwritten stubs**.

### The ten

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `katantra` | contested / medium | ⭐⭐ **T1: the batch's own premise was the wrong shape.** It didn't lose — it won classrooms while Pāṇini won prestige. |
| 2 | `sarvavarman` | contested / **low** | ⭐⭐⭐ **The evidential circle closes**: the sole witness to his date is a text whose own existence that same episode explains. |
| 3 | `candra-vyakarana` | contested / medium | ⭐⭐⭐ **A transmission accident read as an authorial choice — and this corpus made it too.** |
| 4 | `candragomin` | contested / medium | ⭐⭐ **Collision #10, the first a specialist had already split — and the split did not propagate.** |
| 5 | `jinendrabuddhi` | contested / medium | ⭐⭐⭐ **T2 confirmed, and the collision was inside this corpus.** |
| 6 | `nyasa-vyakarana` | converged / medium | ⭐⭐⭐ **"Manuscripts in India last no more than about five hundred years."** Read at first hand. |
| 7 | `haradatta` | contested / medium | ⭐⭐ **T3 answered in the honest negative — and Pāṇinian grammar turns out to have regions.** |
| 8 | `paribhasha` | converged / medium | ⭐⭐⭐ **T4 confirmed with a census: nine systems, fifteen collections, 500+ maxims.** |
| 9 | `prakrta-prakasha` | contested / medium | ⭐⭐ The corpus's **first Prākṛt-grammar node**, and the terminal module's third instance. |
| 10 | `punyaraja` | contested / medium | ⭐⭐ The batch closes on **the apparatus its own open question must be read through.** |

### The four named tests

| test | queued expectation | result |
|---|---|---|
| **T1** — rival or simplification? | "competes in use, not in theory" | ✅ **Confirmed — and the *frame* falsified.** "The winner's account" is the wrong shape: the Kātantra "attained… a very prominent place among text-books… in Behar, Bengal and Gujarat," has a large unpublished commentarial literature, and (⚠ single-sourced) shaped **Kaccāyana and the Dravidian grammarians**. **Prestige was mistaken for reach.** |
| **T2** — is the grammarian Jinendrabuddhi Dignāga's commentator? | either outcome is a result | ✅ **Affirmative in the mainstream** (Hayes 1983, Funayama 1999, Steinkellner 2005; **Kobayashi 1977** dissenting). ⭐ **The corpus held both halves in separate files and had never noticed.** |
| **T3** — does Haradatta's non-hierarchical reading survive first-hand checking? | hopefully yes | ⚠ **NOT DISCHARGED, and the node says so.** Deshpande was read at first hand in Batch 48, so the corpus is one remove from Haradatta rather than two — but **the *Padamañjarī* was not opened, and it is free on archive.org bound with the *Nyāsa*. Not blocked; not done.** |
| **T4** — is *paribhāṣā* Pāṇinian property or shared technology? | shared, probably | ✅✅ **Confirmed in its strongest form, with a census** — and larger than the question: *paribhāṣā* is shared across **śāstra**, not just across the grammatical systems. |

### ⭐ The engine findings

**1. ⭐⭐⭐ The corpus falsified its own headline finding, two nodes after committing it.** `katantra` was built on Abhyankar's preface — "**the special feature of all these grammars was that they entirely omitted the Vedic peculiarities and accents**" — and drew the conclusion that what makes a grammar "a different system" is that it stops being a **vedāṅga**, which is Ch 40's thesis. **Ramhari Timalsina (Heidelberg) falsifies the strong form**: the Cāndravyākaraṇa had **eight** chapters — 7 Vedic, 8 svara — placed **at the end** rather than distributed as Pāṇini does, and **they were lost**. Abhyankar describes the *received* text and misreports the *composed* one. ⭐ **The surviving claim is weaker and better**, and is now stated in both files. ⚠ **Abhyankar is not shown wrong; his class-level generalisation is shown to be assembled from received texts** — the third time in three batches that a reference work's general statement outruns what its own entries license.

**2. ⭐⭐ The terminal module, and three fates.** The correction opened a real structural finding: **Pāṇini interleaves; the rivals modularise.** Cāndra (Vedic + svara + 86 paribhāṣās at the end) → **lost**. Hemacandra (book 8 = Prākṛt) → **detached and became the famous part**. *Prākṛtaprakāśa* (3 dialect chapters) → **accreted, 8 chapters to 12**. And it is the same fact as the pedagogy: **the organisation that makes a grammar teachable makes its parts detachable.** ⚠ Three instances, offered as a pattern, not a law; and the corpus deliberately does **not** now re-read the Kātantra's omission as a loss.

**3. ⭐⭐⭐ "Manuscripts in India last no more than about five hundred years."** Ajotikar, Ajotikar & Scharf, **read at first hand** (the fetch tool could not parse the PDF; extracted locally with `pypdf`). The oldest readable Kāśikāvṛtti manuscript is **early 15th c.**; its first commentator wrote in the **8th or 9th**. ⭐ **The commentaries are not a later layer on the text — they are the older evidence.** This **relocates** the Batch 48 caveat rather than withdrawing it: mediation is not avoidable, it is **universal**, so the discipline is to say **which commentary you stand on**. Second time in three batches a chapter has been answered by a later one rather than left to go stale (D3).

**4. ⭐⭐ The argument from silence, stated technically.** Same source: a critical edition may treat a manuscript's silence as support, but "**subcommentaries as a rule specifically mention only a small proportion of the words in the base text… one cannot assume that silence regarding a reading in the base text indicates support.**" ⚠ **Direct consequence for this corpus**: wherever a file says *the commentator does not dispute X*, that is worth **zero**. **Recorded as an un-audited exposure, not as cleared.** And their coverage-measurement problem is the same instrument that produces `mahabhashya.md`'s 1,228-of-3,981.

**5. ⭐⭐ T4's census.** Abhyankar states it — "**many Paribhāṣās are common, with their wordings quite similar or sometimes identical in the different systems**"… the total "**may well-nigh exceed 500**" — and **compiled the collection himself**: fifteen works, nine systems, counts 62–140. ⭐ **At the level where grammar reasons about itself there was no winner and no loser; there was one discipline.** Stronger still, the systems shared a **method**: each "drew similar Jñāpakas from the wording of the Sūtras **in their systems**." ⚠ And that method is reading doctrine out of a text's incidental features — the Sphoṭāyana/Śalātura move — **licensed, named, and institutionalised.**

**6. ⭐⭐ Pāṇinian grammar had regions, and the corpus did not know.** **Eastern** (Jinendrabuddhi), **Southern** (Haradatta), **Benares** — which "follow [the *Padamañjarī*] more than… the *Nyāsa*." And the Benares school is the Varanasi household Batch 48 reconstructed. ⚠ **The theological inference is explicitly refused**: Buddhist vs Śaiva vs Brahminical writes itself, Abhyankar gives no reason, and **three other explanations sit on the same page.**

### ⚠ Sources caught being wrong — and two of the six are us

| # | source | failure |
|---|---|---|
| 1 | **Abhyankar** | the class-level Vedic-omission claim (finding 1) — and, separately, printing the *Kathāsaritsāgara* as biography under *Sarvavarman* while calling it "very little historical value" under *Pāṇini* |
| 2 | **wisdomlib "Vyakarana glossary"** | ⚠ **is Abhyankar reprinted verbatim** — caught at first hand, and caught **twice** in this batch (`katantra`, `haradatta`). **Standing rule: never count them as two.** |
| 3 | **Wikipedia, "Chandragomin"** | merges two figures a specialist separated, **and does not mention the grammar at all** |
| 4 | **Wikipedia, "Haradatta"** | gives him the Āpastamba and Gautama *Dharmasūtra* commentaries with **no argument and no doubt raised** |
| 5 | ⚠ **this corpus** | the vedāṅga generalisation (finding 1) — falsified two nodes later, in the same batch |
| 6 | ⚠ **this corpus** | an **OCR gap reattached a relative clause to the wrong noun**: the *Nyāsa* reported as "fragmentary" when the clause belongs to Maitreya Rakṣita's *Tantrapradīpa*. ⭐ **The Batch 48 Hindupedia appositive defect by a different road** — caught by an independent source, not by re-reading |

⭐ **A seventh entry that is not a failure**: the WebFetch summariser reported EAST's host institution as "**Anthropic**." Corrected from the URL (IKGA / Austrian Academy of Sciences) and noted in-file.

### The collision taxonomy, now at six generators

| generator | instance |
|---|---|
| a **personal name** | Vararuci, Patañjali, Kātyāyana |
| a **place-name** | *Kāśikā* |
| a **doctrine-name** | *Sphoṭavāda* |
| a **short form** | **Candra** — a Prākṛt grammarian, and Candrācārya |
| ⭐ a **genre label** | ***Nyāsa*** (5 systems), ***Paribhāṣāvṛtti*** (4) |
| ⭐ a **title in another śāstra** | **Haradatta** — grammar/dharma. ⚠ **Undiagnosed on purpose** |

⭐ **And the inverse, which the corpus had never met: one man, two names, self-reported** — Puṇyarāja "identified himself as **Rājānakaśūravarma**." **Name-*difference* is equally weak evidence.**

⭐ **The rule was sharpened rather than broken.** Steinkellner's ground as summarised — "identical author-name in the colophons" — is *in form* the inference the corpus distrusts, and applied naively would put it on Kobayashi's side against three later specialists. **The load is carried by Hayes's and Funayama's style-and-citation evidence, not the name.** So: **distrust identifications that rest on the name *alone*.** That is exactly what Vararuci never had.

### What the batch did to its own corpus

**Five committed files corrected or qualified, three of them written inside this same batch:**

1. **`katantra.md`** — the vedāṅga generalisation **corrected in place** (by `candra-vyakarana`), and its origin-myth **seniority assumption qualified** (by `haradatta`). ⭐ **Two corrections, from two different later nodes, to one file, inside one batch.**
2. **`jinendrabuddhi.md`** — the "fragmentary state" **misattribution corrected in four places** (by `nyasa-vyakarana`).
3. **`mahabhashya.md`** — the Batch 47 Candrācārya contradiction **narrowed, explicitly not closed**, with both verse addresses supplied.
4. **`vararuci.md`** — the recorded gap ("no node for the Kātantra, Sarvavarman, or Prākṛt grammar at all") **DISCHARGED**, with the sentence left standing as the record of the gap being found.
5. **`kasika.md`** — wired to **both** its commentators, and its Jinendrabuddhi note updated with the Dignāga result.

### Follow-ups carried into Batch 50

**New, and the first three are cheap:**

1. ⭐⭐ **The *Padamañjarī* and the *Nyāsa*** — the Kāśikāvṛtti with **both** is free on archive.org. **This is T3, and it was not blocked, only not done.**
2. ⭐⭐ **Cowell 1854** — the *Prākṛtaprakāśa* with an **English translation** and Bhāmaha's *Manoramā*, out of copyright for a century. The corpus has described a Prākṛt grammar it has not opened.
3. ⭐⭐ ***Vākyapadīya* II.481–490** — Benares Sanskrit Series 1884 with Puṇyarāja's *Ṭīkā*, or **Iyer's English kāṇḍa II**. **Would close the Candrācārya question outright.**
4. ⭐ **Ramhari Timalsina**, *The Vedic and Svara Chapters of the Cāndravyākaraṇa* — ⚠ **the load-bearing source of this batch's biggest correction, and it was not read** (publisher returned Access-Denied).
5. **Abhyankar's own *Paribhāṣāsaṃgraha*** (15 texts in one volume) and **Kielhorn's *Paribhāṣenduśekhara*** (text + English translation).
6. ⚠ **Kobayashi 1977** — a **D2 case**: the corpus knows the dissenting position only as a negative sign in someone else's bibliography. Also **Steinkellner 2005 pp. xl–xlii**, **Hayes 1983**, **Funayama 1999**.
7. **Aklujkar 1974**, "The Authorship of the *Vākya-kāṇḍa-ṭīkā*" — new to the corpus; and **Aklujkar 1972** (Batch 47's follow-up #5, now dated).
8. **Patrick Olivelle (2005), pp. 301 ff.** — the only cited authority on collision candidate #12.
9. **Andrew Ollett, *Language of the Snakes*** (OA, MUSE) — the named authority on how the grammarians constituted Prākṛt; located, not retrievable.
10. **The *Asiatische Studien* 2018 paribhāṣā issue** (405/403) — directly on where paribhāṣās come from.
11. **Liebich 1919** on the Kātantra; the **Kātantrasūtras** (Calcutta 1927 / Saini 1987); **Hoernle 1880** on Caṇḍa; **Pischel**.
12. ⚠ **Is the Kaccāyana/Dravidian influence claim true?** Single-sourced, and if it holds, T1's correction is much larger than stated.
13. ⚠ **An un-audited exposure**: every place a file argues from a commentator's silence (engine finding 4).
14. ⭐ **`candrakirti` has no node** — the corpus has `madhyamaka`, `nagarjuna`, `yogacara`. Opened by `candragomin`.

**Carried from earlier batches, still open:** Phillips's *Tattvacintāmaṇi*; **Matilal 1968 Parts II–III, in hand and still unused**; Potter; Neevel 1977; the *Ratnaprabhā* and *Siddhayoga*; **P. V. Sharma**; Ingalls 1951; the D. Ch./D. C. Bhattacharyya question; the Digvijaya dating in `shankara.md`; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; **Valerie Stoker**; Lance Nelson; Renou, Woods (1914), Dasgupta (1922); Vergiani 2014; Deshpande 1998; the *Vaiyākaraṇabhūṣaṇasāra*. ⚠ **`karma-vargana.md` is no longer the only `low`-confidence node — `sarvavarman.md` joins it, and for a different reason: not thin sources but one source that is a fairy tale.** ⚠ **Ch 11 is now thirteen chapters out of date.**

### Suggested Batch 50 (names only — **leads to test, not facts**)

- ⭐ **Opened directly by this batch:** `candrakirti` (the clearest hole) · `durgasimha` (the Kātantra's commentator, and a live 8th-vs-9th/10th-century split) · `jainendra-vyakarana` / `devanandin` · `sakatayana` · `maitreya-raksita` · `vyadi` (pre-Patañjali, and the first paribhāṣā writer) · `bhoja` / `sarasvatikanthabharana`.
- **Still open from 46–48:** `madhava-nidana` / `madhavakara` · `vijayaraksita` · `srikanthadatta` · `annambhatta` / `tarkasangraha` · `jagadisha-tarkalankara` · `vardhamana-upadhyaya` · `sridhara` · `jayanta-bhatta` · `parasara-bhatta` · `yadavaprakasha` · `vaidyanatha-payagunde` · `varadaraja` · `sesha-krsna`.
- ⭐⭐ **A different kind of batch, and this one has earned it: a DEPTH batch.** Follow-ups 1–3 above are all **free, located, and would each close a named test at the primary level.** Batches 44–49 have each opened more primary-source debt than they closed (`DRIFT.md` D1). **Three reads would discharge T3, give the corpus its first Prākṛt text at first hand, and close the Candrācārya question.**
