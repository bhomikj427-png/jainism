# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 45 CLOSED — 362 concepts, 2198 edges** (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 35, 36 and 37**, written in one pass over the 21 uncovered nodes of Batches 44+45, plus `dhamma` folded into **Ch 12 §3.0**. **Chapter coverage is 362 / 362 and `KNOWN_UNCOVERED` is now EMPTY** — the first time the corpus has full coverage with no recorded excuses. Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (46) — see the end of the Batch 45 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false “340/340” stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **362 concepts across 45 batches; 37 chapters.** 2198 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 362/362 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---

## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` passes all three checks; there is no outstanding
maintenance and no red gate. So the next unit of work is a **new concept batch (46)** — see the suggestions
at the end of the Batch 45 run-log below.

⚠ **Read this before opening Batch 46.** Batch 45 falsified **two** of its own queue premises (`candrata`,
`nrisimhasrama` in Batch 44 before it). The suggestions below are **leads, not facts** — every one of them is
a claim to *test*, and a batch that never falsifies its own queue is not checking it.

⚠ **Meulenbeld is local no longer.** The five HIML volumes were downloaded to a *session scratchpad*, which
does not persist. Re-download before any Āyurveda work — the method that works is recorded in
`concepts/candrata.md` under **Note on retrieval** and in Ch 35 §11: take `server` and `dir` from
`https://archive.org/metadata/Meulenbeld-HIML`, then request from that host directly with `%20` for the
spaces. Plain spaces and `+` both fail against archive.org's front door; this cost two batches before it
was solved.

---

## Batch 45 — CLOSED (2026-08-31). 12/12 concepts; 350 → 362 nodes; 2099 → 2198 edges. Plus Ch 35, 36, 37.

Every concept passed the §8 dedup gate against the live filesystem and was committed individually with its
findings in the message. `git log` is the detail; this is the short form.

### The twelve

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `ramanuja` | **contested** / medium | The doctrine converges, the man does not — three separate disputes. `vishishtadvaita.md` had stood 40+ batches as a school with no founder. |
| 2 | `madhva` | **contested** / medium | **One 16th-c. charge that reads as two independent findings**: Appayya → Mesquita "without verification" → Wikipedia in two paragraphs. Written from encyclopedias alone it would have recorded convergence and been wrong. |
| 3 | `yamunacarya` | **contested** / medium | A quotation that **inverts when read in position** — "we do not regard Brahmins as a distinct species" is the *pūrvapakṣa* his book exists to defeat. |
| 4 | `nathamuni` | **contested** / medium | **Three consecutive ācāryas, three impossible lifespans** (128 / 120 / 120 years). A convention, not three observations. |
| 5 | `sriharsa` | **contested** / medium | A book of pure refutation **has no thesis to read off** — which is why four scholarly readings of his affiliation are all defensible. Two tempting labels declined. |
| 6 | `udayana` | **contested** / medium | **The verse that settled his date sits in one manuscript** — and one syllable's emendation moves it seventy years. Neither date adopted. |
| 7 | `anandabodha` | converged / medium | "Most of Ānandabodha's arguments were borrowed by the later writers of the Vedānta school." Deliberately **converged** — marking everything contested would be its own failure. |
| 8 | `vyasatirtha` | converged / medium | A controversy that has run **five hundred years** and may not be over. The *Nyāyāmṛta*'s method is **collection**, doubly sourced. |
| 9 | `madhusudana-sarasvati` | **contested** / medium | **Devotion after liberation** — duality *elected* by the liberated. Widely admired and, on the leading specialist's account, **rarely examined**. |
| 10 | `candrata` | converged / medium | **The claim that queued him did not survive**: "Vāgbhaṭa's grandson" rests on colophons Meulenbeld calls untrustworthy, and Tisaṭa's own authority-list omits Vāgbhaṭa. |
| 11 | `haricandra` | converged / medium | The earliest Caraka commentator, surviving in **a fragment and a reputation** — and his doctrines reach us through people **disagreeing** with him. |
| 12 | `indu` | **contested** / medium | **A commentary that shows another commentary censoring its text** — Ci. 19.98, Jina/Jinasuta vs Śiva/Śivasuta. |

*(#11 `nathamuni` and #12 `udayana` were written out of queue order, to close dangling stubs that
`yamunacarya` and `sriharsa` opened. Both turned out to be structural holes in their own right — Udayana was
already cited in five concept files and two chapters with no node.)*

### The engine finding

⭐ **Meulenbeld's *A History of Indian Medical Literature* was finally obtained** — Batch 44's top follow-up,
after two failed attempts. All five volumes, 13.3 MB. **The fix is the `%20`-on-the-direct-host method**
recorded above. It upgraded the whole Āyurveda layer and supplied three nodes outright.

### What the batch did to nodes it did not create

Fourteen existing files changed:

- `arunadatta.md` — gains a **third commentarial act**. Written up as a commentator who *legislates* and is
  *dated by being contradicted*; he also **edits**, replacing Jina/Jinasuta with Śiva/Śivasuta.
- `jejjata.md` — a **fourth date** (Meulenbeld, 7th–8th c.), and the first not routed through Vāgbhaṭa. Plus
  the rule it yields: *a disputed date cannot anchor another date*, but a contested figure can still **order**
  others around himself.
- `citsukha.md` — **both** standing "(unwritten)" rows closed (`sriharsa`, `anandabodha`), and a real
  independent corroboration recorded: Dasgupta 1932 and Das/SEP 2018 agree on his dependence on Śrīharṣa.
- `appayya-dikshita.md` — we now know what is **inside** one of the titled polemics, and it cuts against that
  file's own "titles are the shallow attack" reading.
- `hemadri.md` — recruited as a 13th-c. witness in a modern authenticity dispute.
- `vacaspati-mishra.md` — **name collision** logged: there are two Vācaspati Miśras, five centuries apart.
- `vishishtadvaita.md`, `dvaita-vedanta.md` — flat date-claims qualified.
- `yamunacarya.md`, `sriharsa.md` — strengthened mid-batch by findings from nodes written after them.
- `chapters/hindu/shastra/23-ayurveda.md` — §"A third authority" **rewritten**; it had been flagged stale
  since Batch 42 and left standing. (Carried follow-up 2, partially closed.)
- `chapters/buddhist/12-buddhist.md` — new §3.0/§3.0.1 on `dhamma`.
- `graph/check_chapters.py` — `KNOWN_UNCOVERED` emptied.

### The teaching layer

Three chapters, written over **all 21** uncovered nodes of Batches 44+45 — the fork `progress.md` sanctioned,
taken as a three-way split rather than two:

| ch | title | folder | nodes |
|---|---|---|---|
| **35** | Dating a Literature Without Dates: The Āyurvedic Commentators | `hindu/shastra/` | 7 |
| **36** | Founders and the Lineages That Made Them | `hindu/darsana/` | 6 |
| **37** | The Dialecticians: What Refutation Is For | `cross-tradition/` | 8 |

They share a spine the batch did not plan: **an entire literature dates itself by who quotes whom, and
citation evidence is ordinal, not cardinal.** Every absolute year in Ch 35 entered from outside the medical
literature. Ch 36 finds the same structure under the Śrī Vaiṣṇava *munitraya*. Ch 37 finds the same
compilation-as-survival result in a fourth literature — and Malliṣeṇa's colophon, which names the **weekday**,
shows that the vagueness is a fact about *what survived*, not about how these authors wrote.

### Follow-ups carried into Batch 46

**New, and top of the list:**

1. ***Aṣṭāṅgahṛdaya* Ci. 19.98 in a critical edition with apparatus** — the cheapest high-value test in the
   corpus. Settles whether Indu preserved or restored the Buddhist reading, and what the manuscripts say.
2. **John A. Grimes, *The Seven Great Untenables*** (Motilal Banarsidass, 1990) — the **only** clean route to
   enumerating the *saptavidhā anupapatti*. Six of seven heads are currently recorded as *unverified* in
   `ramanuja.md` on listserv/blog authority.
3. **Valerie Stoker** and **Michael Williams** on Vyāsatīrtha — the two modern non-partisan specialists;
   everything in `vyasatirtha.md` currently leans on a committed Dvaita partisan.
4. **Lance Nelson's translation of *Bhaktirasāyana* ch. 1** — already in English at the same site as his study.
5. **Any critical edition of Udayana's *Lakṣaṇāvalī* with apparatus** — settles whether the dating verse has
   one witness or many.
6. Sydnor 2012 and Carman, *The Theology of Rāmānuja* (1974); Mesquita's monograph; **McCrea 2016** (three
   fetch routes refused).
7. **N. S. Mooss** on Indu's 119 *paribhāṣā* verses — edited, translated and annotated already.

**Carried from Batch 43/44, still open:**

1. ~~Ch 23 §"A third authority"~~ — **CLOSED**. Ch 26 §6.4 and Ch 31 §4.2 still describe holes that may have
   closed; **Ch 11 still predates the whole Advaita-lineage cluster** and now also predates Chs 36–37.
2. The **Digvijaya dating tension** in `shankara.md` (Mādhava's *Śaṅkaravijaya* dated 17th c.; Vidyāraṇya d. 1391).
3. **`karma-vargana.md`** is still the corpus's only `low`-confidence node.
4. The **42-vs-93 *nāma*-karma discrepancy** — needs the *Karma-grantha* / *Gommaṭasāra* read directly.
5. **`dhatu.md`'s three-vs-four dispute**, with `arunadatta` inside it holding *eka-kāla*.
6. **`balarama.md`** still single-sourced (Johnson vol. 5).
7. **Prakāśātman's *bhāvarūpa* avidyā priority** — Dasgupta and Wikipedia invert the chronology.
8. **Which of Hemādri's works quotes Ḍalhaṇa** — still unidentified by any source; `dalhana.md`'s c. 1309
   upper bound rests on an inference.

### Suggested Batch 46 (names only — no files written; **leads to test, not facts**)

- **Opened by Batch 45, Vedānta side:** `jayatirtha` (Madhva's standardiser, "the crystallization of Dvaita
  thought," named repeatedly in `vyasatirtha.md` and `madhva.md` with no node); `vedanta-desika` /
  `venkatanatha` (44 citations of the lost *Nyāyatattva*, and Śrī Vaiṣṇavism's other great systematiser);
  `gangesha` (Navya-Nyāya's founder — named in `sriharsa.md` and `udayana.md`, and the corpus has **no**
  Navya-Nyāya node at all); `vimuktatman` (Ānandabodha's alleged teacher — **single-sourced**, so writing him
  is also the test); `padmapada` (already linked from `nrisimhasrama.md`).
- **Opened by Batch 45, Āyurveda side:** `tisata` (the *Cikitsākalikā*; Candraṭa's father, and the man whose
  authority-list omits Vāgbhaṭa); `niscalakara` (the *Ratnaprabhā* — a witness in **four** Batch 44/45 nodes
  and the man who refuted the *Aṣṭāṅgahṛdaya* attribution); `vrnda` (the *Siddhayoga*); `srikanthadatta`.
- **⚠ Structural:** **Navya-Nyāya is a complete hole.** `gangesha` is named in two nodes and two chapters;
  Ch 37 §2.1 lists eight of his successors by name. The corpus has Old Nyāya (Gautama → Vātsyāyana →
  Praśastapāda → Udayana) and then stops at exactly the point the tradition itself calls a new beginning.
- **Maintenance:** carried follow-up 1 — **Ch 11 is now five chapters out of date.**
