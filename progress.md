# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 43 COMPLETE — 340 concepts, 2022 edges** (audit CLEAN; 11/11 concepts done, pushed).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 34 — The Commentator** (`cross-tradition/`), written over seven of Batch 43's eight new nodes; the eighth (`hiraṇyakaśipu`) was folded into **Ch 33 §§5.3.1–5.3.2** rather than given a chapter of its own. **Chapter coverage is 339 / 340** — verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (44) — see the Suggested Batch 44 list at the end of the Batch 43 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false “340/340” stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **350 concepts across 44 batches; 34 chapters.** 0 orphans. 0 unwritten stubs. Structural + conformance audits CLEAN. ⚠ **Chapter coverage 340/350 — nine of Batch 44's ten nodes are UNCOVERED, plus the standing `dhamma` gap.** `check_chapters.py` is **red on purpose** until Ch 35 is written; that is the documented mid-batch state (§9: nodes first, then a chapter over them), not a defect to hunt.

---

## ▶ NEXT SESSION — start here, in this order

1. **Write Ch 35 over Batch 44's ten nodes.** This is the *only* thing standing between the repo and a green `check_all.py`. The batch has one obvious spine — **Ch 34 asked what a commentator does, and Batch 44 answered it five different ways** (see "The thread" below). Suggested home: `chapters/cross-tradition/`, as a direct sequel to Ch 34. ⚠ If the ten split more naturally into two chapters (a Vedānta/canon one and an Āyurveda-commentators one), that is a genuine fork — take it and number them 35 and 36. Add rows to `chapters/coverage.md`, then re-run `python graph/check_all.py`.
2. **Close the `dhamma` gap** — the standing `KNOWN-GAP` in `check_chapters.py`. The node exists (`converged` / `medium`, 7 links); no chapter teaches or links it. It belongs in **Ch 12 (The Buddhist Family)**, which already carries the whole Pali cluster: fold it in and add a `coverage.md` row rather than writing a chapter for one node. Then delete its entry from `KNOWN_UNCOVERED` in `check_chapters.py`.
3. **Then** open Batch 45 from the suggestions at the end of this log.

---

## Batch 44 — CLOSED (2026-08-27). 10/10 concepts; 340 → 350 nodes.

Every concept passed the §8 dedup gate against the live filesystem, transliteration twins included, and was committed individually with its findings in the message. `git log` is the detail; this is the short form.

### The ten

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `prasthanatrayi` | converged / medium | "Three" counts **slots, not books** — slot 1 is ten Upaniṣads with a soft edge and a disputed attribution sitting on it. **No source dates the term**; a promising *Vedāntasāra* lead was checked and **not confirmed**. |
| 2 | `mallisena` | converged / medium | Read **Dhruva's 1933 critical edition itself**. The colophon dates the work to the **weekday**. Corrected `hemacandra.md`'s six-school list, which came from a bookseller's blurb and is **unstable across the literature**. |
| 3 | `citsukha` | converged / medium | He glossed **both** Maṇḍana's *Brahmasiddhi* and Sureśvara's *Naiṣkarmyasiddhi* — texts this corpus deliberately keeps NOT-equivalent. **Aufrecht corroborates** the Amalānanda ← Sukhaprakāśa ← Citsukha chain Batch 43 assembled from web pages. |
| 4 | `nrisimhasrama` | converged / medium | **The claim that queued him did not survive.** Three sources with every occasion to link him to Appayya's *Parimala* do not mention the other man. Ch 34 and `appayya-dikshita.md` both qualified. |
| 5 | `shrikantha` | **contested** / medium | Five defensible readings, 3100 BCE → 15th c. McCrea's title says the invention of Śrīkaṇṭha's **Vedānta** — not of Śrīkaṇṭha. A popular source had already made that slide; logged as a specimen of the failure §0 exists to prevent. |
| 6 | `sivadvaita` | converged / medium | The founding mechanism is **exact**: Appayya reads Śrīkaṇṭha's *pariṇāmavāda* as *vivartavāda* (Duquette 2015). The corpus's Vedānta **taxonomy** turns out to be the **instrument** that made a school. |
| 7 | `arunadatta` | converged / medium | Dated by having been **contradicted about the structure of the eye** — a fourth dating method for `dalhana.md`'s table. Gode: **three** men of the name, merged by the popular literature into one polymath. |
| 8 | `hemadri` | converged / medium | Writing a cited-but-unwritten node **loosened a bracket it was holding up**: Ḍalhaṇa's upper bound moves from "early 13th c." to **c. 1309**, because 1260 was Hemādri's first year, not his medical work's date. |
| 9 | `jejjata` | **contested** / medium | Three dates for him are really three dates for **Vāgbhaṭa** — and `vagbhata.md` already records Vāgbhaṭa as at least two men. Both ends of the dating argument may be composite. |
| 10 | `gayadasa` | converged / medium | **One section, one manuscript** — yet known to have covered the whole *Suśrutasaṃhitā*, because Ḍalhaṇa quotes it throughout. Evidence for extent and evidence for wording come from different places. |

### What the batch did to nodes it did not create

Writing these ten **changed nine existing files** — the return on the "write the nodes you merely cite" principle:

- `dalhana.md` — **date-bracket loosened** (upper bound → c. 1309); **open hole closed**: the *Nibandhasaṅgraha*'s absorbed commentators are now named (Jejjaṭa, Gayadāsa), reframing it as the **archive** of Suśruta's commentators rather than another commentary on Suśruta.
- `hemacandra.md` — six-school claim qualified; gains `expressed-by: mallisena`.
- `syadvada.md`, `saptabhangi.md` — upgrade path sharpened from a book title to **stanzas XXI–XXX**; `saptabhangi`'s "key text for the scheme" flagged as resting on Wikipedia, **not** on the text.
- `appayya-dikshita.md` — the *Parimala* request-claim marked single-sourced and tested; gains the `shrikantha` edge and the McCrea/Duquette citations its standing "it is an exercise" reading had lacked.
- `amalananda.md` — lineage now corroborated from a manuscript catalogue.
- `upanishad.md`, `brahma-sutra.md`, `gita.md`, `vagbhata.md` — complementary inverse edges (§5).
- `chapters/cross-tradition/34-the-commentator.md` — §3 qualified.

### Engine

- **`check_all.py` was broken and is fixed.** It died with `UnicodeEncodeError` on the first Devanagari character `find_duplicates.py` printed: the child scripts reconfigure their own stdout to UTF-8, but the runner re-printed captured output on a cp1252 console. **The duplicate and chapter checks never ran at all** — and the traceback's non-zero exit merely looked like a failing check. Now reconfigured; all three run.
- `check_chapters.py` — the `prasthānatrayī` `KNOWN_UNRESOLVED` excuse **removed**, since the node exists and the row now resolves on its own.

### The thread running through the batch

Ch 34 asked what a commentator *does*. Batch 44 answered five ways, and they do not reduce to one: **define** what the school lacked (Citsukha); **transmit and add nothing**, and be called superb for it (Nṛsiṃhāśrama — *"has not put forward any new interpretation … yet as a commentator he is superb"*); **legislate** physiology the base text left open (Aruṇadatta, Ḍalhaṇa); **constitute** the position you claim to be explaining (Appayya on Śrīkaṇṭha); and — unplanned, out of the Āyurveda trio — **archive**: Ḍalhaṇa's compiling is the reason a century of Suśruta scholarship is recoverable at all, so compilation is a survival strategy rather than a failure of originality. That is Ch 35's spine.

### Follow-ups carried into Batch 45

**New, and top of the list:**

1. **⭐ Meulenbeld, *A History of Indian Medical Literature*** (Groningen Oriental Studies 15, 1999–2002) — the standard reference, **free full text** at Internet Archive item **`Meulenbeld-HIML`** (files `HIML 1A _djvu.txt`, `HIML_1B_djvu.txt`, `HIML_2A_djvu.txt`, `HIML_2B_djvu.txt`, `HIML_3_djvu.txt`). **Two download attempts failed on the literal spaces in the filenames**; neither `%20` nor `+` worked. Next attempt: pull the exact path from `archive.org/metadata/Meulenbeld-HIML` (which *did* return the file list), or try the BookReader search endpoint. Would upgrade **seven** nodes at once — `gayadasa`, `jejjata`, `dalhana`, `cakrapanidatta`, `arunadatta`, `hemadri`, `vagbhata`.
2. **McCrea 2016**, *JIP* 44:1, 81–94 — Springer, PhilPapers and ResearchGate all blocked. The only thing that would let `shrikantha` state the invention thesis rather than parse its title.
3. **Which of Hemādri's works quotes Ḍalhaṇa** — unidentified by any source; `dalhana.md`'s revised upper bound rests on the inference that it is his only medical work.
4. **Citsukha's *Abhiprāyaprakāśikā*** — would answer whose locus of avidyā he defends, having glossed both Maṇḍana and Sureśvara.
5. **Malliṣeṇa, stanzas XXI–XXX** — upgrades `syadvada` **and** `saptabhangi` together (upgrade path 1, now precise instead of a title).
6. **Fisher 2017** (*IJHS*) — whether Śivādvaita outlived Appayya; no source consulted says.
7. Two paywalled (HTTP 402) papers written on exactly their subjects: *JIMH* 27:1 (1997) on Aruṇadatta + Hemādri, PMID 12575692; *J. Ayurveda* 16:1 (2022) on Hemādri.

**Carried from Batch 43, still untouched — 1 and 2 are now five batches overdue:**

1. **Ch 11 predates the whole Advaita-lineage cluster** — re-read against Ch 25 §§3–6, Ch 30, Ch 34, and now `citsukha` / `nrisimhasrama` / `prasthanatrayi`. **Ch 11 §1 has a node under it for the first time.**
2. **Ch 23 §"A third authority", Ch 26 §6.4 and Ch 31 §4.2** all describe **closed** holes and should be rewritten. ⚠ **Ch 23's is now worse**: it says the third saṃhitā's commentator is a hole, and Batch 44 wrote him (`arunadatta`) *and* his colleague (`hemadri`).
3. The **Digvijaya dating tension** in `shankara.md` (Mādhava's *Śaṅkaravijaya* dated 17th c.; Vidyāraṇya d. 1391).
4. **`karma-vargana.md`** is still the Jain layer's one `low` node.
5. The **42-vs-93 *nāma*-karma discrepancy** — needs the *Karma-grantha* / *Gommaṭasāra Karmakāṇḍa* read directly.
6. **`dhatu.md`'s three-vs-four dispute** (Ch 34 §8.1) — settled by the *Āyurvedadīpikā* at Ci. 15:20. ⚠ `arunadatta` now sits **inside** this dispute, holding *eka-kāla*.
7. **`balarama.md`** still single-sourced; Johnson vol. 5 is the target.
8. **Prakāśātman's *bhāvarūpa* avidyā priority** — Dasgupta and Wikipedia's chronology invert it; no source addresses it.

### Suggested Batch 45 (names only — no files written)

- **Opened by Batch 44:** `sriharsa` (the *Khaṇḍanakhaṇḍakhādya* — Citsukha's model, and the corpus has **no** node for what its own sources call the most difficult work in Advaita); `anandabodha` (the *Nyāyamakaranda*, glossed by both Citsukha and Sukhaprakāśa); `madhusudana-sarasvati` (the *Advaitasiddhi* — the Advaita side of the dvaita–advaita debate, entirely absent); `candrata` (Vāgbhaṭa's grandson, the other witness to Jejjaṭa); `haricandra` (*Bhaṭṭāra Haricandra*, 5th c., the earliest Caraka commentator named in this batch's sources).
- **⚠ Structural, and now the Vedānta layer's largest single hole:** **`ramanuja` and `madhva` are named repeatedly across the corpus and have no nodes.** `vishishtadvaita` and `dvaita-vedanta` exist as schools without their founders. `prasthanatrayi` made this visible by naming both men as trayī-commentators, and `nrisimhasrama`'s *Bhedadhikkāra* and `sivadvaita`'s Madhva polemics both point at an absent node.
- **Maintenance:** carried follow-ups 1 and 2 above — untouched for five batches, and 2 is now three chapters wide and factually stale.
