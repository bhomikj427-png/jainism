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

## ACTIVE QUEUE — Batch 44 (opened 2026-08-27)

Ten keys, dedup-gated against the live filesystem before opening (all ten free; no
transliteration twins: `chitsukha`/`srikantha`/`shivadvaita`/`nrsimhasrama`/`mallishena`
all return zero). Worked in this order — most-connected first, the speculative pair last.

| # | key | why it is queued | state |
|---|---|---|---|
| 1 | `prasthanatrayi` | taught by Ch 11 and Ch 19 with **no node** — the one open coverage inversion | **done** (converged/medium) |
| 2 | `mallisena` | the *Syādvādamañjarī* (1292); named upgrade path 1 for `syadvada` + `saptabhangi` | **done** (converged/medium) |
| 3 | `citsukha` | the *Tattvapradīpikā*; Amalānanda's grand-teacher — closes an Advaita-lineage hop | **done** (converged/medium) |
| 4 | `nrisimhasrama` | commissioned the *Parimala*; opened by Ch 34 | **done** (converged/medium; the commission claim did NOT survive checking) |
| 5 | `shrikantha` | the *Brahmamīmāṃsābhāṣya* — Appayya's Śaiva project has no base text without it | **done** (**contested**/medium) |
| 6 | `sivadvaita` | the school itself, currently visible only through `appayya-dikshita` | **done** (converged/medium) |
| 7 | `arunadatta` | the *Sarvāṅgasundarā* — the one commentator of the three saṃhitās this corpus lacks | **done** (converged/medium) |
| 8 | `hemadri` | the *Āyurvedarasāyana*; the *terminus ante quem* of Ḍalhaṇa's date | pending |
| 9 | `jejjata` | lost Suśruta/Caraka commentator — follow-up 8; **may end `blocked`** | pending |
| 10 | `gayadasa` | the *Nyāyacandrikā* on the Nidānasthāna — follow-up 8; **may end `blocked`** | pending |

**Not in this batch, and not a concept at all:** `dhamma`. The node already exists
(`converged` / `medium` / 7 links); what is missing is **chapter prose** — no chapter
teaches or links it. It is a teaching-layer gap, tracked as a `KNOWN-GAP` in
`check_chapters.py`, and is closed by writing prose, not by writing a node.

---

### Corpus milestone: **340 concepts across 43 batches; 34 chapters.** 0 orphans. 0 unwritten stubs. Audit CLEAN. Chapter coverage **339/340** (corrected from “340/340” by the maintenance pass below — it had never been machine-checked).

---

## Maintenance pass — engine health (2026-08-27, post-Batch-43)

Standalone “check the engine for leaks” pass. **No concepts written, no batch advanced** — 340 nodes / 2022 edges throughout. Full detail is in `git log`; this is the short form.

### The two that mattered
1. **The audit was never a gate.** `build_graph.py` printed “DEFECTS PRESENT” and **exited 0** — `main()` dropped `audit_graph()`'s verdict. Everything it has ever checked (orphans, stubs, bidirectional directional edges, forbidden combos) was advisory, while §8/§9 treated it as a gate. Found only by injecting a defect and watching the runner report PASS. Now exits 1.
2. **The map had stopped drawing the honesty layer.** `EDGE_STYLES` was defined and never read — all 2022 edges rendered one grey, in both SVG and HTML (which never got the edge type at all), against §6's `style = link type` and §5's “the map must teach the distinction.” Now 733 solid / 961 dashed / 328 dotted, with a legend.

### Also fixed
`graph.svg` could freeze silently (Graphviz installed but off PATH; render failed, run continued, audit still said CLEAN) — `dot` is now located, the failure is loud, freshness is checked · `graph.dot` was only written when the render *failed* · nothing validated the controlled vocabularies — link types, `status`, `confidence` and front-matter are now audited (this caught `quantum-complementarity.md`'s `term_iast: (modern physics)`) · 6 duplicate rows and 5 missing rows in the concept→chapter map, and a false “340/340” that had never been machine-checked (real: 339/340) · the startup-set size guard watched the wrong file · §6 described an engine that no longer existed.

### Added
- **`graph/check_all.py`** — the single gate for §8/§9. Runs all three checks, always all three, exits non-zero if any fails. **Use this, not the scripts individually.**
- **`graph/check_chapters.py`** — proves chapter coverage instead of asserting it. Coverage was the one structural claim in the repo maintained by hand, and it was wrong.

### Efficiency (measured, not estimated)
- **Startup set 91.1 KB → 52.5 KB (‑42%).** Rotated Batch 43's closed run-log to the archive per §9, and split the 342-row concept→chapter lookup table out of `chapters/INDEX.md` into **`chapters/coverage.md`** — grepped on demand, never loaded at startup (the same move §7 already made for `index.md`/`MANIFEST.tsv`).
- **Build parsed every concept file twice** (680 parses for 340 files); `write_index()` now reuses the parsed nodes. 0.215s → 0.116s, `index.md` byte-identical.
- **`graph.svg` untracked.** `fdp` relays out on every run even with a fixed seed and identical input, so it rewrote ~12k lines / 1.1 MB per commit across 78 commits for no information. `graph.dot` and `graph.html` are byte-stable (verified) and still tracked; render the SVG on demand.

### Open — genuine content gaps, deliberately NOT invented
1. **`dhamma` is taught by no chapter.** The node exists; no chapter links to or treats it. Needs chapter prose. Recorded as a `KNOWN-GAP` in `check_chapters.py` so it stays visible without keeping the check permanently red.
2. **`prasthānatrayī` is taught but has no node.** Ch 11 and Ch 19 treat it and it has a coverage row. A candidate for Batch 44 — not something to fabricate here.

### Decided this pass (no longer open)
- **`chapters/INDEX.md` key convention — left alone, with evidence.** 216 rows are diacritic IAST, 125 canonical keys. Tested the checker's fold across all 340 keys: **340 distinct folds, 0 collisions**, and an ambiguous fold already fails *safe* (returns UNRESOLVED rather than guessing). Rewriting 216 rows would be churn with no measurable gain.
- **Four dormant tracked files** (`TEACHING.md`, `teaching-log.md`, `link-candidates.md`, `.linker-state`) carry **SUPERSEDED/DORMANT banners** rather than deletion — none is in the startup set, so they cost nothing, and the banners remove the hazard. `link-candidates.md` was the live one: it quotes a §5 that no longer reads that way and could have led a session to bulk-collapse symmetric pairs §5 now calls correct. Deleting them is still yours to call.

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
