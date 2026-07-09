# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 37 done, 296 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 13 (next = Ch 14)**. **→ The planned chapters Ch 14–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 37 — daśāvatāra completion + churning loose ends (2026-07-09)

### Startup reconcile
- Batches 1–36 fully committed. Audit CLEAN at start: 289 nodes, 1636 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** with a research fork per concept (one concept in progress at a time; each fork's findings synthesized and written by the primary agent, never delegated wholesale). Dedup gate (Glob) before writing.
- Cluster chosen via user forced-choice (§10 genuine fork — "what to build next" among 4 suggested clusters from Batch 36's suggestion list): **daśāvatāra + churning loose ends**, 7 concepts.

### Batch 37 concepts — 7 / 7 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | parashurama | converged | medium | sixth daśāvatāra; unique avatāra-to-avatāra overlap — meets Rāma directly in Rāmāyaṇa Bāla Kāṇḍa 74–76; daśāvatāra list-instability caveat (Balarāma/Buddha swap doesn't touch his slot) |
| 2 | kalki | converged | medium | tenth/future daśāvatāra; two-tier confidence split (cosmological core high, Puranic biographical chain medium — Viṣṇu Purāṇa→Bhāgavata→Kalki Purāṇa is textual inheritance, not triangulation); Vāyu Purāṇa's rival Pramīti noted; Kālacakra vocabulary-borrowing flagged, not equated |
| 3 | bali | contested | medium | Mahābali, Vāmana's foil; TWO distinct contested splits mapped: grace-vs-punishment (Sutala-as-elevation vs Garuḍa-drags-him-down) and devotional-vs-Dravidian-historiographical readings of Onam |
| 4 | indra | contested | medium | hub node closing 7 prior dangling inbound refs (airavata, ucchaihshravas, vamana, bali, samudra-manthana, krishna, agni); Doniger-sourced Vedic-supremacy→Puranic-demotion divergence as central finding; etymology deliberately left unresolved |
| 5 | kaustubha | converged | medium | churning-gem on Viṣṇu's chest; uncontested member of the variable 14-ratnas list; continuous into Kṛṣṇa's iconography |
| 6 | varuni | contested | medium | churning-wine-goddess; Rāmāyaṇa (devas accept) directly contradicts Bhāgavata Purāṇa 8.8.30 (asuras take her); sura/asura wordplay flagged as folk/narrative etymology, NOT the scholarly Proto-Indo-Iranian derivation |
| 7 | svarbhanu | contested | medium | pre-beheading whole resolving Rāhu/Ketu origin; genuine two-layer finding — independent Ṛgveda 5.40 Atri-restores-the-sun eclipse myth vs. the Puranic churning-beheading myth, linked by name-continuity not plot-continuity; identity (Sāyaṇa) vs whole-then-split (Wikipedia) contested via the sanctioned shares-vocabulary + conflated-NOT-equivalent edge pair |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **kalki**: explicitly separated a high-confidence cosmological-role tier from a medium-confidence biographical tier, because the biographical detail (village, parents, horse-name) traces a Viṣṇu Purāṇa→Bhāgavata→Kalki Purāṇa elaboration chain — exactly the "copies are not confirmation" trap in §4 signal 1.
- **bali**: two independent contested axes on the same figure (theological grace/punishment; cultural devotional/Dravidian-historiographical) kept as two separate tables rather than merged into one, since they split along different source-clusters.
- **indra**: the demotion arc (Ahalyā curse, Govardhana humbling, Bali's conquest) is the central finding — Indra's Vedic supremacy is not a static fact carried into the epics/Purāṇas but a documented decline (Doniger, *Encyclopedia of Religion*), paralleling Varuṇa's decline (no `varuna.md` yet — flagged, not linked).
- **varuni**: a direct textual contradiction between two primary sources (Rāmāyaṇa vs Bhāgavata Purāṇa) on who accepts her — recorded as genuine contestation, not resolved by picking the "more authoritative" text.
- **svarbhanu**: the load-bearing finding is that "Svarbhānu" names two textually unconnected myths (Vedic eclipse-etiology vs. Puranic amṛta-theft) sharing only a name — the file explicitly resists reading the older Vedic layer as a proto-version of the churning story.
- A Grokipedia (AI-generated tertiary) hit was explicitly excluded as a source during svarbhanu research, consistent with the same exclusion made during bali research — noted as a recurring, correct discipline, not a one-off.

### De-orphan inbounds relocated into existing hubs (established practice; pure-symmetric pairs, no hierarchy on those pairs, proven-clean)
`vishnu → shares-vocabulary-with → parashurama` · `vishnu → shares-vocabulary-with → kalki` · `samudra-manthana → shares-vocabulary-with → kaustubha` · `samudra-manthana → shares-vocabulary-with → varuni` · `rahu ↔ svarbhanu` (shares-vocabulary-with + often-conflated-with-NOT-equivalent, the sanctioned two-type pair) · `ketu → shares-vocabulary-with → svarbhanu`. `bali` and `indra` self-anchored via dense intra-batch/existing-hub cross-links (narasimha, vamana, krishna, airavata, ucchaihshravas, agni).

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **First pass found 4 orphans** (kalki, kaustubha, parashurama, varuni — written but not yet a target of any edge) — resolved by adding the hub-inbound edges above; **second pass CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Existing DEVANAGARI/SPLIT groups unchanged.
- Graph regenerated: **289 → 296 nodes, 1636 → 1669 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 296 concepts across 37 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 38 (names only — no files written)
- **Āyurveda** (dhanvantari opens it, still unclaimed): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha).
- **Neoplatonic/Greek closure:** `simplicius`, `marinus`, `pseudo-dionysius`, `chaldean-oracles`.
- **Mīmāṃsā/Advaita:** `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya`.
- **Newly opened by this batch:** `varuna` (Indra's Vedic-decline parallel, cited in indra.md but unwritten), `atri` (the RV 5.40 sage who restores the sun, cited in svarbhanu.md but unwritten), `balarama` (Kṛṣṇa's brother, cited in varuni.md but unwritten), `prahlada` (Bali's grandfather, cited in bali.md but unwritten), `vritra`/`verethragna` comparanda cluster (Indo-European dragon-slaying — flagged in indra.md as a future structurally-parallel-to candidate, not yet a node).
