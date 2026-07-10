# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 39 done, 304 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 17 (next = Ch 18)**. **→ The planned chapters Ch 15–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 39 — Āyurveda opening cluster (2026-07-10)

### Startup reconcile
- Batches 1–38 fully committed. Audit CLEAN at start: 300 nodes, 1686 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked serially, one concept end-to-end then commit. Dedup gate (Glob) before writing each file — confirmed `ayurveda`/`sushruta`/`charaka`/`tridosha` all unclaimed; `dhanvantari.md` already existed and explicitly names Āyurveda/Suśruta as unclaimed forward-references.
- Cluster chosen autonomously (user directive: proceed without asking, assume reasonably) from progress.md's four suggested Batch-39 clusters: **Āyurveda**, the most self-contained. Mīmāṃsā/Advaita, the carried-over Vedic-figures cluster, and Eriugena/Psellos were left for a future batch.

### Batch 39 concepts — 4 / 4 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | ayurveda | converged | medium | the umbrella medical tradition; flagged the honest gap between the popular "5,000-year-old" claim and Wikipedia's sourced "first centuries CE" dating for the classical texts; scientific-critique material (doshas "fictional," no cancer-cure evidence, rasaśāstra heavy-metal toxicity) recorded as the external secular assessment, held separate from the internal doctrinal account |
| 2 | charaka | contested | medium | the internal-medicine Saṃhitā + its eponymous physician; three-layer redaction (Agniveśa → Charaka → Dṛḍhabala) surfaced; `status: contested` set specifically for Chattopadhyay's "lineage not person" thesis vs. the traditional individual-author reading; Britannica fetch blocked (HTTP 403) and flagged as a sourcing gap rather than papered over |
| 3 | sushruta | contested | medium | the surgery-centered Saṃhitā + its eponymous physician; Dhanvantari-vs-Divodāsa manuscript-framing split (oldest MSS attribute directly to Divodāsa); flagged a genuine rigor-divergence between Meulenbeld's philological caution (Wikipedia) and a peer-reviewed PMC medical-history source's flat, uncritical "~600 BCE" dating with no debate acknowledged at all |
| 4 | tridosha | converged | medium | vāta/pitta/kapha, each a mahābhūta-pairing; *duṣ*-root etymology (imbalance, not inherent harm); open item honestly flagged — two comparative-review PDFs (Charaka/Suśruta/Vāgbhaṭa treatment differences) could not be read (fetch tool returned unparseable binary/OCR), so that deeper cross-textual comparison is deferred |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **ayurveda**: the "5,000 years old" self-presentation vs. the textually-verifiable "first centuries CE" dating band — recorded as a real gap, not rounded away.
- **charaka**: Chattopadhyay's claim that "Charaka" names a lineage/sect rather than an individual, set against the traditional-author reading assumed by most popular medical-history literature — presented as contested, not resolved.
- **sushruta**: two internal-tradition attribution frames (printed editions: Dhanvantari teaching a group including Sushruta; oldest manuscripts: direct Divodāsa attribution) plus a cross-genre rigor gap — a peer-reviewed PMC piece asserts an unqualified "~600 BCE" date with zero historiographical caveat, while the Meulenbeld-sourced Wikipedia account treats the dating as a live, unresolved 2000 BCE–6th c. CE range.
- **tridosha**: an open item honestly logged rather than silently dropped — the intended three-way Charaka/Suśruta/Vāgbhaṭa comparative-elaboration content could not be sourced this round because both comparative-review PDFs returned as unreadable binary content via the fetch tool.
- Two Britannica fetches (charaka.md, ayurveda-adjacent) returned HTTP 403 and were recorded as sourcing gaps rather than silently substituted with an indirect citation.

### Cross-tradition honesty-layer edges added (new, this batch)
- `ayurveda often-conflated-with-NOT-equivalent prakriti-samkhya` (paired with `shares-vocabulary-with` on the same ordered pair, the one sanctioned two-type combination) — Āyurvedic *prakṛti* (individual dosha-constitution) vs. Sāṃkhya *prakṛti* (cosmic primal matter): same word, different tradition, not the same concept at different scales.
- `tridosha often-conflated-with-NOT-equivalent guna-samkhya` — the dosha (physiological) and guṇa (psychological, sattva/rajas/tamas) personality-classification layers are sometimes run together in popular wellness literature as one system; they are two distinct schemes over the same person.
- `charaka structurally-parallel-to sushruta` / `sushruta structurally-parallel-to charaka` (symmetric type, both directions written independently from each node's own vantage per §5's storage rule) — same core subjects, opposite emphasis (internal medicine vs. surgery), unresolved relative chronology.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- Single pass CLEAN: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE. (No orphans to resolve this batch — every new concept picked up an inbound edge naturally via the `structurally-parallel-to`/`shares-vocabulary-with` cluster above plus each `formalizes: ayurveda` edge.)
- `find_duplicates.py`: exit 0, 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Pre-existing DEVANAGARI/SPLIT groups (aḥiṃsā, vyāsa pairs) unchanged, not touched by this batch.
- Graph regenerated: **300 → 304 nodes, 1686 → 1700 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"` (Graphviz not on PATH this session — explicit binary path used, same as Batch 38); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed.

### Corpus milestone: 304 concepts across 39 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 40 (names only — no files written)
- **Mīmāṃsā/Advaita** (carried over, untouched this round): `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by `mandana-mishra`, `advaita-vedanta`), `varsaganya`.
- **Carried over from Batch 37/38:** `varuna` (Indra's Vedic-decline parallel, cited in `indra.md`), `atri` (RV 5.40 sage, cited in `svarbhanu.md`), `balarama` (cited in `varuni.md`), `prahlada` (Bali's grandfather, cited in `bali.md`), `vritra`/`verethragna` comparanda cluster (cited in `indra.md`); `eriugena` (cited in `pseudo-dionysius.md`); `psellos`/`michael-psellos` (cited in `chaldean-oracles.md`).
- **Newly opened by this batch:** a possible `vagbhata` node (Aṣṭāṅga Hṛdayam author, the third major classical Āyurveda authority alongside Charaka/Suśruta — named in `ayurveda.md` and `sushruta.md` but not yet a node); the Āyurveda cluster's own internal open item (a `dhatu`/`mala` node — the seven-tissue/waste-product framework mentioned in `ayurveda.md` but not yet broken out as its own concept).
