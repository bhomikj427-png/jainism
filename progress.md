# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 40 done, 306 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 26 drafted; next = Ch 27.** The roadmap was exhausted at Ch 24 and **re-derived** on 2026-08-25 — rows **26 (Jain remainder), 27 (Buddhist singletons), 28 (modern-physics comparanda)** are queued in the `## Chapter roadmap` table in `chapters/INDEX.md`; a fresh session takes the lowest-numbered `planned` row. ⚠️ When re-deriving, diff on **chapter prose with diacritics**, not on bare keys — the index lists concepts by IAST display name, so a key-only diff reports false gaps. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 40 — Advaita founders pair (2026-07-10)

### Startup reconcile
- Batches 1–39 fully committed; working tree clean; audit CLEAN at start (304 nodes, 1700 edges).
- Cluster chosen autonomously from Batch-40 suggestions (user directive: extended autonomous session): the **twice-carried-over Mīmāṃsā/Advaita pair `shankara` + `sureshvara`** — the most-referenced unwritten keys in the corpus (`advaita-vedanta`, `atman-vedanta`, `brahman`, `maya-advaita`, `mandana-mishra` all cite Śaṅkara). `varsaganya`, the Vedic-figures cluster, Eriugena/Psellos, and the newly-opened `vagbhata`/`dhatu` items remain for a future batch.
- Dedup gate: Glob confirmed neither `shankara*` nor `*sureshvara*` existed; grep confirmed no `## Links` target had yet reserved either key; canonical key `shankara` chosen (matches the corpus founder-file convention — kanada, kapila, patanjali — and every existing file's prose usage) with Ādi Śaṅkara as in-file alias.

### Batch 40 concepts — 2 / 2 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | shankara | converged | medium | SEP + Wikipedia independently agree on the authentic-works list (Brahmasūtra-bhāṣya, ten Upaniṣad bhāṣyas, Gītā-bhāṣya, Upadeśasāhasrī) against the 300+-text attribution problem (Vivekacūḍāmaṇi "mostly rejected" — flagged because two existing files list it as a future fetch *as Śaṅkara's*); the honest headline is the **history-vs-hagiography gap**: "relatively unknown during his life-time," overshadowed by Maṇḍana Miśra, unmentioned for centuries, fame constructed in the 14th-c. Vijayanagara period (Vidyāraṇya) and amplified by Neo-Vedānta — recorded as a two-layer evidential standing, not smoothed |
| 2 | sureshvara | converged | medium | the Vārttikakāra disciple; Naiṣkarmyasiddhi (423 vv.) + the two great vārttikas; signature avidyā-locus doctrine (in **Brahman**, vs Maṇḍana's jīva — āśraya/viṣaya distinction recorded); the **Maṇḍana=Sureśvara identity left contested** (Kuppuswami Sastri: distinct; Balasubramanian: unproven) convergent with the existing mandana-mishra.md's independent record; a dating tension (9th-c. claim vs direct-disciple status under a 700–750 Śaṅkara) flagged rather than resolved |

### Honesty-layer edges added
- `shankara often-conflated-with-NOT-equivalent shiva` — the philosopher is not the god whose name he shares; devotional literature exploits the pun; the map now teaches the name-collision.
- `shankara structurally-parallel-to kundakunda` — each tradition's most authoritative philosopher-monk whose attributed corpus far exceeds the authentic one and whose biography is hagiographic accretion.
- `sureshvara often-conflated-with-NOT-equivalent mandana-mishra` (stored both directions per §5 symmetric-storage rule; the mirror edge in mandana-mishra.md also resolved this batch's one audit defect — sureshvara orphanhood) — the debate-conversion legend vs the doctrinal oppositions (locus of avidyā; role of meditation).

### Audits
- First build pass flagged **orphan: sureshvara** → fixed per §10 by adding the mirror symmetric edge in mandana-mishra.md (content-motivated, not a mechanical mirror — written from Maṇḍana's vantage). Re-run: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0; pre-existing DEVANAGARI/SPLIT groups unchanged.
- Graph: **304 → 306 nodes, 1700 → 1711 edges**; `graph.svg` rendered via explicit `"C:\Program Files\Graphviz\bin\dot.exe"` (Graphviz still not on PATH — same workaround as Batches 38/39); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` regenerated.

### Also completed this session (other two tracks, committed separately)
- **Chapters 16 (Nyāya & Vaiśeṣika) and 17 (Mīmāṃsā & Cārvāka)** drafted — the six āstika darśanas are now all covered in the teaching layer; next planned chapter is **Ch 18 (Hindu Deities)**.
- **Translation reading-room units #10–13 (TS Adhyāyas 7, 3, 4, 10)** — **the Tattvārtha Sūtra is now complete in the reading room: all ten adhyāyas, both recensions, first pass.** Headline finds logged in `chapters/jain/translations/INDEX.md` (the "block promotion" fork type at sizes 5/21/1; the 26-vs-39 heavens divergence; the strīmokṣa split living in commentary on a shared sūtra).

### Corpus milestone: 306 concepts across 40 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 41 (names only — no files written)
- **Carried over (again):** `varsaganya` (Sāṃkhya teacher, cited in `samkhya-karika`-adjacent material); `varuna`, `atri`, `balarama`, `prahlada`, `vritra`/`verethragna` (Vedic-figures cluster); `eriugena`; `psellos`/`michael-psellos`.
- **Āyurveda continuation:** `vagbhata`; `dhatu`/`mala`.
- **Newly opened by Batch 40:** `padmapada` (Śaṅkara's other direct disciple, named in `sureshvara.md` — the Vivaraṇa-prasthāna counterpart to the Vārttika school); `gaudapada` (Śaṅkara's parama-guru, Māṇḍūkya-kārikā author — named in `advaita-vedanta.md` and `shankara.md` but not yet a node); `vidyaranya` (the 14th-c. fame-constructor, named in `shankara.md`).
