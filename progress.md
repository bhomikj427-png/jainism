# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 41 done, 309 concepts, 1733 edges** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 28 drafted — the teaching layer is COMPLETE for the current 306-node graph.** The roadmap was exhausted at Ch 24, re-derived on 2026-08-25 (rows 25–28), and those four are now all drafted. The final re-derivation (2026-08-26) found every concept covered: its only two apparent gaps, `naigama-naya` and `saṃgraha-naya`, were already covered in Ch 02 §4 and needed index rows, not a chapter. **→ The next unit of work is a CONCEPT BATCH here (Suggested Batch 41, below), not a chapter.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠️ When re-deriving, diff on **chapter prose with diacritics**, not on bare keys — the index lists concepts by IAST display name, so a key-only diff reports false gaps. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 41 — the Advaita lineage completed (2026-08-26)

### Startup reconcile
- Batches 1–40 committed; working tree clean at start; audit CLEAN (306 nodes, 1711 edges).
- Session began on the **chapter** track and exhausted it: Chapters 24–28 drafted (see below), after which the re-derived roadmap came back empty and the standing rule sent work to the concept track.
- Cluster chosen from the Batch-41 suggestions: the three **Advaita lineage** keys opened by Batch 40 and leaned on hard by Ch 25 — `gaudapada`, `padmapada`, `vidyaranya`. All three are named in existing files' prose and none had a node.
- Dedup gate for each: `Glob concepts/<key>*.md` returned nothing; grep confirmed no `## Links` target had reserved any of the three keys.

### Batch 41 concepts — 3 / 3 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | gaudapada | contested | medium | Wikipedia + IEP, independently authored, agree **exactly** on the Māṇḍūkya-kārikā's 215 verses / four chapters (29·38·48·100), ajātivāda, turīya, asparśa-yoga and the paramaguru relation — and **disagree on the dating**, with the two Buddhist arguments running in opposite directions (dated by who cites him vs by whom he cites; 4th–7th c. spread). Three live disputes recorded as findings: the date, chapter 4's authorship (six positions tabulated — Murti, King, Bhattacārya, Sarma, Nikhilananda, Mayeda; with the hard datum that later Advaitins quote only chs. 1–3), and IEP's explicit **"multiple Gauḍapāda-s."** |
| 2 | padmapada | converged | medium | mid-8th c., direct disciple; the Pañcapādikā surviving as a gloss on the **first four aphorisms** only; Prakāśātman's 10th-c. Vivaraṇa naming the school; *pratibimbavāda*. The substance is the Vivaraṇa/Bhāmatī locus-of-avidyā split, which **independently corroborates Batch 40** from a different source-set — the founding generation divides into two camps, not four positions, with Padmapāda and Sureśvara on the same side. Records Satchidānandendra Sarasvatī's dissent that the whole locus debate misconstrues Śaṅkara, who held avidyā beginningless and its origin fruitless to seek. |
| 3 | vidyaranya | contested | medium | 1296–1391, Śṛṅgeri jagadguru; the other end of `shankara.md`'s fame-construction claim. Three open identifications (Mādhava/Vidyāraṇya; the SDS's authorship, with Cannibhaṭṭa named against tradition; the Digvijaya) and the Vijayanagara foundation story judged **legendary** — no contemporary inscriptions, "imagined probably at least 200 years afterward," a political foundation myth. Confidence honestly capped because signal 2 is a second article on the **same platform**. |

### Findings that reach beyond their own nodes
- **A near-miss the dedup gate caught.** `samkhya-karika.md` already listed a "Gauḍapāda-bhāṣya" among its commentaries, so the corpus was one edge away from silently merging the Advaitin with the Sāṃkhya commentator. IEP's "multiple Gauḍapāda-s" is now stored as an explicit `often-conflated-with-NOT-equivalent` so the map teaches the doubt.
- **A fourth interested-channel case.** The *Sarva-darśana-saṅgraha* is one of very few surviving sources on Cārvāka and ranks it lowest by design, in a hierarchy built to end at Advaita. That joins the Chaldean Oracles (Ch 24 §4.4), Vindhyavāsin (Ch 25 §8) and Makkhali Gosāla (Ch 27 §8).
- **An internal tension flagged, not smoothed.** `shankara.md` and Ch 25 §3.2 date "Mādhava's Śaṅkaradigvijaya" to the **17th century**; Vidyāraṇya died in **1391**. Reconcilable only if the attribution is pseudepigraphic — which is what "attribution disputed" would mean — but no source states that reconciliation, so it is recorded in `vidyaranya.md` as the likely explanation and **not** as a finding. **Whoever next upgrades either node must resolve this first.**

### Honesty-layer edges added
- `gaudapada often-conflated-with-NOT-equivalent samkhya-karika` — the multiple-Gauḍapādas problem, so the Advaitin is not silently merged with the Sāṃkhya commentator.
- `gaudapada shares-vocabulary-with madhyamaka` **and** `often-conflated-with-NOT-equivalent madhyamaka` — the §5 sanctioned two-type pattern: the Yogācāra/Mādhyamika borrowing is real and extensive, and a positive unborn Ātman-Brahman is still what Madhyamaka denies.
- `shankara historically-influenced-by gaudapada` added to `shankara.md`, which named him in prose but carried no edge.
- `vidyaranya structurally-parallel-to marinus` and `structurally-parallel-to simplicius` — the successor-hagiographer and the interested-transmission-channel patterns, drawn across traditions.

### Audits
- Build pass 1 flagged **orphans: padmapada, vidyaranya** -> fixed per §10 with two **content-motivated** symmetric mirrors, each written from its own node's vantage (not mechanical mirroring): `sureshvara -> shares-vocabulary-with -> padmapada` (the two disciples, the two lineages, the same side of the locus question) and `marinus -> structurally-parallel-to -> vidyaranya` (with the disanalogy stated in the note). Re-run: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0; pre-existing DEVANAGARI/SPLIT groups unchanged.
- Graph: **306 -> 309 nodes, 1711 -> 1733 edges**; `graph.svg` rendered via the explicit `"C:\Program Files\Graphviz\bin\dot.exe"` path (Graphviz still not on PATH — same workaround as Batches 38–40); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` regenerated.

### Also completed this session (chapter track, committed separately)
- **Chapters 24–28 drafted, closing the teaching layer.** Ch 24 (Later Neoplatonists), Ch 25 (the commentators and the identity problems), Ch 26 (the Jain karma machinery), Ch 27 (Buddhist process + two adversaries), Ch 28 (the modern-physics comparanda — the §0 chapter). The roadmap was re-derived twice and is now **complete**: every one of the 306 nodes then in `concepts/` has a chapter home.

### Open follow-ups (not acted on — deliberately left for a maintenance pass)
1. **`ajiva.md` stores `part-of: jiva`**, which inverts the partition its own note describes. The controlled vocabulary has no **complement-of** relation, so this is a schema question, not a typo (Ch 26 §2.3).
2. **`many-valued-logic` carries `tradition: Modern Physics`** — it is formal logic, and the mis-tag mis-colours the node in the rendered graph (Ch 28 §5).
3. **`atman-vedanta.md` and `brahman.md` both queue a Vivekacūḍāmaṇi fetch *as Śaṅkara's***; per Ch 25 §3.1 it must be re-scoped to *attributed*.
4. **Ch 11 predates `shankara`/`sureshvara`/`mandana-mishra`/`gaudapada`/`padmapada`** and should be re-read against Ch 25 §§3–6 and this batch.
5. The **Digvijaya dating tension** above.

### Corpus milestone: 309 concepts across 41 batches; 28 chapters. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 42 (names only — no files written)
- **Opened by this batch:** `prakasatman` (the Vivaraṇa school's namesake, 10th c.); `vacaspati-mishra` (the Bhāmatī school's namesake — the corpus now describes the split from only one side); `govinda-bhagavatpada` (the missing link between Gauḍapāda and Śaṅkara).
- **Opened by Chs 24/27:** `psellos` (the separate Byzantine transmission line for the Chaldean Oracle fragments); `prajnakaragupta` (who challenged Dharmottara's *niścaya-pratyaya*); `utpaladeva` (Pratyabhijñā — named across Ch 18 and Ch 27 and still unwritten).
- **Opened by Ch 26:** the four ***aghāti* karmas** — the corpus has no node for them at all, and Ch 26 §6.4 flags the residual *yoga*-driven influx in a kevalin as a genuine hole.
- **Carried over (again):** `varsaganya`; the Vedic-figures cluster (`varuna`, `atri`, `balarama`, `prahlada`, `vritra`/`verethragna`); `eriugena`; and the Āyurveda continuation `vagbhata`, `dhatu`/`mala` — the last of which Ch 23 calls "a hole in the chapter."
