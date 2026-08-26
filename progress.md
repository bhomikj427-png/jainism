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

### Corpus milestone: **340 concepts across 43 batches; 34 chapters.** 0 orphans. 0 unwritten stubs. Audit CLEAN. Chapter coverage **339/340** (corrected from “340/340” by the maintenance pass below — it had never been machine-checked).

---

## Maintenance pass — engine health (2026-08-27, post-Batch-43)

Requested as a standalone “check the engine for leaks” pass; no concepts written, no batch advanced.

### Fixed (§10-mechanical — deterministic, one correct form, verified by re-running the audit)
1. **The rendered graph had stopped drawing the honesty layer.** `EDGE_STYLES` was defined in `build_graph.py` and *never read* — all 2022 edges rendered as one undifferentiated grey, in **both** the SVG and the HTML (which never received the edge type at all). §6 promises `style = link type` and §5 says the map must *teach* the not-equivalent distinction; it could not. Now solid/dashed/dotted + per-layer colour and opacity in `graph.svg`, `graph.dot` and `graph.html` (with a link-type legend). Verified: 733 solid / 961 dashed / 328 dotted = 2022.
2. **`graph.svg` could freeze silently.** Graphviz is installed but not on PATH, so the render failed, the script continued, and the audit still printed CLEAN — a stale tracked artifact could ship unnoticed. `dot` is now resolved from the standard install locations, the failure is loud, and `check_svg_freshness()` compares the SVG's node count to the corpus.
3. **`graph.dot` was only written when the render *failed*,** so on success the tracked intermediate went stale. Now always regenerated.
4. **Nothing validated the controlled vocabularies.** A typo'd link type, `status` or `confidence` became a real edge / node state silently. `build_graph.py` now audits link types, `status`, `confidence` and required front-matter against §3/§5, and fails the run. Regression-tested by injecting four defects.
5. **`quantum-complementarity.md` had `term_iast: (modern physics)`** — a tradition annotation in the canonical-key field. Now `quantum complementarity`, matching its four Modern/Western siblings. Caught by check 4.
6. **`chapters/INDEX.md` had 6 duplicate rows** (`sat`, `dravya`, `ahiṃsā`, `pramāṇa`, `loka-jain`, `trimurti`), two of them asserting *different* primary chapters for one concept, against the file's own “primary-covered in exactly one chapter” rule. In every pair the later row was the considered one (richer cross-refs; where they conflicted it explicitly demoted the other chapter to a cross-ref). Superseded rows dropped, `dravya`'s cross-refs unioned.
7. **5 written concepts had no row in the concept→chapter map** — `dukkha`, `sunyata`, `bodhisattva`, `yogacara` (Ch 12) and `maya-advaita` (Ch 11). Each was *verified* to be treated in the chapter prose and already linked from it, so the rows record an existing fact rather than asserting a new one.
8. **The startup-set size guard pointed at the wrong file.** §7 nagged on `progress.md` (15 KB) while `chapters/INDEX.md` — also loaded every session, and 54 KB — had no ceiling at all. Both are now nagged, plus a combined budget (currently 91 KB / 120 KB).
9. **`CLAUDE.md` §6 described an engine that no longer existed** — `graph.html` called “Cytoscape” (it is the vendored force-graph), `find_duplicates.py` called four classes (it reports six). Corrected.

### Added
- **`graph/check_chapters.py`** — the missing checker. “Chapter coverage N/N” was the one structural claim in this repo asserted by hand rather than proven, because `chapters/INDEX.md` keys its concept column by *display term* (`kaṣāya`) while a concept's canonical key is its **filename** (`kashaya`) — the two sets do not join. On first run it found 1 unresolved row, 6 uncovered concepts and 6 duplicates. Now: 339/340, exit 1 on the one remaining gap.

### Open — genuine content gaps, deliberately NOT invented
1. **`dhamma` is taught by no chapter.** The concept file exists; no chapter links to it or treats it. A real hole in the teaching layer; needs chapter prose, which is out of scope for a maintenance pass.
2. **`prasthānatrayī` is taught but has no concept file.** Ch 11 (3 mentions) and Ch 19 (4) treat it and `chapters/INDEX.md` gives it a row, but no node exists. A concept worth writing — a candidate for Batch 44, not something to fabricate here.

### Open — needs a human decision (§10a forks; see the pass's closing report)
- **`graph.svg` churn.** `fdp` in Graphviz 15 lays the graph out differently on every run — verified: the *same* `graph.dot` rendered twice differs, under `overlap=prism`/`scale`/`false` alike, and a fixed `start=1` seed does not help. So the tracked SVG rewrites ~12k lines per commit carrying no information. `graph.dot` **is** byte-stable. Options: accept the churn, or untrack `graph.svg` and render on demand from `graph.dot` (§6 currently calls the build “idempotent”, which is true of every output except the SVG).
- **`chapters/INDEX.md` key convention.** 216 of 341 rows are keyed in diacritic IAST, 125 in canonical filename keys. `check_chapters.py` currently bridges the gap with a reviewed 18-entry alias table. Normalising the column to filename keys would remove the alias table entirely, at the cost of diacritics in that column.
- **Four dormant tracked files** predating the current three-track structure: `TEACHING.md` + `teaching-log.md` (an abandoned interactive-teaching track; the log still says “Taught 0 of 75 concepts” and carries a hand-maintained 75-row status table that duplicates `MANIFEST.tsv`'s job), and `link-candidates.md` + `.linker-state` (a June linker pass whose recorded policy **quotes a superseded §5** — see the SUPERSEDED banners added to both files).

### Open follow-ups carried into Batch 44
1. **Ch 11 predates the whole Advaita-lineage cluster** — re-read against Ch 25 §§3–6, Ch 30 and now Ch 34 §§1–2. *(carried since Batch 42)*
2. **The Digvijaya dating tension** (`shankara.md` dates "Mādhava's Śaṅkaravijaya" to the 17th c.; Vidyāraṇya died 1391). *(carried)*
3. **`karma-vargana.md` is still the Jain layer's one `low` node.** *(carried)*
4. **The 42-vs-93 *nāma*-karma discrepancy** — needs the *Karma-grantha* / *Gommaṭasāra Karmakāṇḍa* read directly. *(carried)*
5. **Ch 23 §"A third authority" and Ch 26 §6.4** both describe **closed** holes and should be rewritten when next revised. *(carried)* — **and Ch 31 §4.2 now joins them**, since `cakrapanidatta` answered its caveat.
6. **NEW — `dhatu.md` carries an unresolved three-vs-four dispute** (Ch 34 §8.1). Settled only by reading the *Āyurvedadīpikā* at Ci. 15:20.
7. **NEW — `balarama.md`'s central claim is still single-sourced.** Johnson's translation was fetched and the Vāsudeva-hell passage **was not found** in the opening material; vol. 5 is the target. Flag deliberately left open.
8. **NEW — the *Nibandhasaṅgraha*'s preserved commentators are unrecorded.** No source consulted names *which* lost commentaries Ḍalhaṇa absorbed.
9. **NEW — Prakāśātman's "first to propound *bhāvarūpa* avidyā" is in question.** Dasgupta has Sarvajñātman holding it at c. 900; on Wikipedia's own chronology the priority inverts. No source addresses it.

### Named upgrade paths, cheapest first (the most actionable list this batch produced)
1. **Hemacandra's *Anyayogavyavacchedadvātriṃśikā* — 32 verses.** Upgrades `syādvāda` **and** `saptabhaṅgī` at once (Dhruva 1933 ed., printed with Malliṣeṇa).
2. **Cakrapāṇi's *Āyurvedadīpikā*, Ci. 15:20 + the Grahaṇī chapter.** Settles follow-up 6.
3. **Johnson's *Triṣaṣṭiśalākāpuruṣacaritra* vol. 5.** Settles follow-up 7.
4. Veezhinathan's *Saṃkṣepaśārīraka* (1985); Duquette 2021 in full (403 on fetch); White, *The Alchemical Body*; Śrīdhara Svāmin's *Bhāvārthadīpikā* on BhP Canto 7.

### Suggested Batch 44 (names only — no files written)
- **Opened by Batch 43:** `arunadatta` (the *Sarvāṅgasundarā*, and author of the fourth *nyāya* — the one commentator of the three saṃhitās this corpus now lacks); `hemadri` (the *Āyurvedarasāyana*, and the *terminus ante quem* of Ḍalhaṇa's date); `citsukha` (the *Tattvapradīpikā*; Amalānanda's grand-teacher); `mallisena` (the *Syādvādamañjarī*, 1292 — and see upgrade path 1); `shrikantha` (the *Brahmamīmāṃsābhāṣya*, without which Appayya's Śaiva project has no base text); `sivadvaita` (the school itself, currently visible only through `appayya-dikshita`).
- **Opened by Ch 34:** `nrisimhasrama` (who commissioned the *Parimala*); `jejjata` or `gayadasa` (the lost Suśruta commentators — *if* follow-up 8 can be sourced at all).
- **Structural/maintenance pass:** follow-ups 1, 2 and 5 — none touched in four batches, and 5 is now three chapters wide.
