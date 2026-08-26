# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 43 COMPLETE — 340 concepts, 2022 edges** (audit CLEAN; 11/11 concepts done, pushed).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 34 — The Commentator** (`cross-tradition/`), written over seven of Batch 43's eight new nodes; the eighth (`hiraṇyakaśipu`) was folded into **Ch 33 §§5.3.1–5.3.2** rather than given a chapter of its own. **Chapter coverage is COMPLETE at 340 / 340** — eight rows added to `chapters/INDEX.md`, one per new node. → **The next unit of work is a NEW BATCH (44) — see the Suggested Batch 44 list at the end of the Batch 43 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ When re-deriving, diff on **chapter prose with diacritics**, not on bare keys — the index lists concepts by IAST display name, so a key-only diff reports false gaps. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 43 — COMPLETE (2026-08-27) — post-Śaṅkara continuations, the Āyurvedic commentators, the mercurial school, and two named upgrade paths

### Startup reconcile
- Working tree clean; git and `progress.md` agreed; audit CLEAN at 332 nodes / 1939 edges; `find_duplicates.py` exit 0.
- Resumed at row 4 of the 11-concept queue (rows 1–3 and the maintenance pass had been committed in the previous session).
- `graph.svg` still requires the explicit `dot.exe` path — Graphviz is not on PATH (same workaround as Batches 38–42).
- **`WebSearch` was available again** (the previous session hit its limit), which is why the remaining eight nodes are better sourced than the first three.

### Concepts — 11 / 11 done (0 blocked, 0 needs-opus-review). Rows 4–11 written this session.

| # | concept | status | conf | the finding |
|---|---|---|---|---|
| 4 | sarvajñātman | contested | medium | ***dvāra***. He holds every Vivaraṇa-side doctrine and still denies avidyā is the world's **material cause** — "Brahman in association and jointly with ajñāna cannot be regarded as the material cause." So the *āśraya* axis and the material-cause axis are **independent**, and "the Vivaraṇa view" flattens them. Also the corpus's cleanest §4-signal-5 case: the **critical edition's own blurb** carries the Kāñchī succession claim, so *provenance on the text ≠ provenance on the biography*. Date spread ~1,400 years. And a fourth source has him saluting **Deveśvara**, not Sureśvara, as guru — so Dasgupta's computed c. 900 rests on a premise the text does not supply. |
| 5 | amalānanda | converged | medium | The Bhāmatī stack is **five storeys and the tradition names the set**: "*Vedānta Śāstra* means 'the five texts…'" — in that usage the discipline **is** the stack. Storey 5 exists because storey 4 was unreadable. He also wrote on the **rival** school (*Pañcapādikā-darpaṇa*): fact recorded, "early link between the schools" inference **declined**. The corpus's **control case for lineage claims** — three formulations that reconcile once *dīkṣā*- and *vidyā*-guru are distinguished. Plus a checkable reference-work error (the *Pañcapādikā* given to Vācaspati; it is Padmapāda's). |
| 6 | appayya-dīkṣita | contested | medium | **The opponent who leaves no trace in the titles.** He named books after Madhva and wrote nothing explicitly against Rāmānuja — yet Duquette (OUP 2021) has the Śaiva oeuvre "mainly directed against Viśiṣṭādvaita." Compatible, and the point: polemical targets are **not readable off a bibliography**. Three readings of his own allegiance tabulated, not settled. The *Siddhāntaleśasaṃgraha* drawn as a 16th-c. doxography of one school's internal splits — structurally what a `contested` node is — parting from §4 at exactly one commitment: it declares the sub-schools to converge. Typed ∥ + NOT-equiv against `anekāntavāda`. |
| 7 | raseśvara | contested | medium | Its chapter opens with an **objection to the other six darśanas**, not with metallurgy: liberation is deferred past death, so "a man should preserve that body by means of mercury." The alchemy is the argument's **second premise**. Dating: Cowell & Gough (1882) put the school at the "commencement of the Christian era" and Wikipedia repeats it **with attribution** — one source and its echo — against three literatures dating the root texts to the **10th–12th c.** So "Raseśvara *darśana*" is treated as partly a 14th-century classificatory artefact. Sharpest new honesty edge: **siddha** — perfected by having **no** body (Jain) vs an **indestructible** one. Mercury handled in both directions per §0. |
| 8 | cakrapāṇidatta | converged | medium | Ch 31 §4.2's caveat answered by reading a peer-reviewed review **in full with its endnotes** — and the picture corrected three ways: the *nyāya*s are **four** not three (the fourth, *eka-kāla*, is **Aruṇadatta's**); they are credited to **three different** authorities; and the numbered enumeration is footnoted to a **2017 textbook**, i.e. modern pedagogy over classical images. **§0's failure mode running backwards.** Also the **best-dated person in the corpus** — a regnal anchor (Nayapāla, r. 1040–1070). |
| 9 | ḍalhaṇa | converged | medium | ***Rakta* is a fourth doṣa — for surgery.** Because *śalyatantra* is about *vraṇa* and blood is the main constituent in wound pathogenesis. So the doṣa-count is **discipline-relative**, which the corpus declines to flatten into inconsistency. He also admits ***mala* as a *śalya***, and his three-part *pariṇāma* (*sūkṣma*/*mala*/*sthūla-bhāga*) is the mechanism `dhatu.md` needed: it makes transformation **partial** and answers the fasting objection. Dated by **citation-bracketing**. |
| 10 | hiraṇyakaśipu | converged | medium | The verses put under Ch 33 §5.3's paraphrase (*Bhāgavata* 7.3.35–38, Tagare). **He never asks for immortality**, and he asks for Brahmā's own station in the same breath. And the clause that fails first is the **first**: everything is fenced against beings "created by You" — by Brahmā, who is Viṣṇu's creature. Viṣṇu is not in the domain at all, so the dusk and the threshold are a **surplus**. Flagged as the corpus's own reading. Logic edges bounded hard: ∥ + NOT-equiv `catuṣkoṭi`, NOT-equiv `many-valued-logic`. |
| 11 | hemacandra | converged | medium | **Two of the corpus's own upgrade paths run through one author.** `syādvāda` and `saptabhaṅgī` both name Malliṣeṇa's *Syādvādamañjarī* as their unfetched upgrade — and it is a commentary on Hemacandra's **32-verse** *Anyayogavyavacchedadvātriṃśikā*. That is now the **cheapest high-value primary text visible to this corpus**. Also ***Ardhacakrin***: Johnson's class-term for the Vāsudevas is "half-cakravartin," so Jainism ranks Kṛṣṇa **in the category name**, before any verdict about hell. Fibonacci claim handled in both directions per §0. |

### Chapter written — Ch 34 (and one fold)
- **Ch 34 — The Commentator** (`cross-tradition/`), over seven of the eight. Positioned explicitly against its neighbours: **Ch 25** asks *who* the commentators were, **Ch 29** how texts survive, **Ch 34** what a commentary is as a *form* — and it is the first of the three to work **across traditions**, which is what makes §5's comparison possible.
- Two things it argues rather than reports: **(a)** how well a pre-modern Indian figure can be dated is mostly a fact about *what institution they stood next to* — court vs maṭha — not how much was written about them; **(b)** a scholar's real opponents are not readable off his tables of contents.
- Its **source ceiling is stated at the top and repeated where it bites**: *not one commentary was read.* That is why all seven nodes are `medium`.
- **`hiraṇyakaśipu` folded into Ch 33 §§5.3.1–5.3.2** rather than given a chapter.
- `chapters/INDEX.md`: Ch 34 row, Ch 33 row updated, **eight** concept rows. **Coverage 340 / 340.**

### Findings that reach beyond their own nodes
- **A dating-method triptych, assembled by accident.** Regnal anchor (Cakrapāṇi, 30-year window) · citation-bracketing (Ḍalhaṇa, 150-year bracket, needs nothing but texts) · lineage arithmetic (Sarvajñātman, and it broke). Ch 34 §5.
- **The doxographic turn**, in four genres deliberately **not** merged: compilation (Ḍalhaṇa) · refutation-doxography (Hemacandra) · ordering (Mādhava) · reconciling (Appayya). Offered as a pattern noticed, **not a thesis argued** — four cases across four centuries is a suggestion.
- **§0's failure mode has a mirror image.** `cakrapanidatta` found a *modern organising scheme mistaken for an old one* (the four-fold *nyāya* list, footnoted to 2017). Same mechanism, opposite direction, equally invisible from summaries.
- **Two sources used for their terms and refused for their editorialising**: the IJAM Ḍalhaṇa paper's western-surgical correlations, and Wikipedia's framing of mercury toxicology as refuting the Raseśvaras. §0 applies in the debunking direction too.
- **A carried follow-up advanced, not closed.** `govinda-bhagavatpada`'s Raseśvara attribution is now blocked from **both** ends by dating (1st c. too early for an 8th-c. guru; 10th–12th c. too late). Two men, one name.
- **A dispute opened rather than papered over.** `dhatu.md`'s "incompatible by design" reading now carries a flagged challenge from the Āyurvedic academic press ("a cohesive group… they do not conflict"). Neither retired, neither adopted, and the question neither source asks is named.

### Audits
- Final: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos. `find_duplicates.py` exit 0 throughout.
- De-orphaning passes, all §10-mechanical, all with **content-motivated** inbound edges written from the inbound node's own vantage: `prakasatman→sarvajnatman` (both sanctioned types), `vacaspati-mishra→amalananda`, `amalananda→appayya-dikshita`, `jivanmukti→rasesvara`, `govinda-bhagavatpada→rasesvara`, `cakrapanidatta→dalhana`, `narasimha→hiranyakashipu`, `prahlada→hiranyakashipu`, `balarama→hemacandra`, `syadvada→hemacandra`, `anekantavada→hemacandra`.
- Graph: **332 → 340 nodes, 1939 → 2022 edges.** `graph.svg` rendered via the explicit Graphviz path.

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
