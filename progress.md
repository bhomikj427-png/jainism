# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 35 done, 278 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 13 (next = Ch 14)**. **→ The planned chapters Ch 14–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 35 — churning-of-the-ocean cluster + darśana author-anchors + Neoplatonic/Greek depth (2026-06-26)

### Startup reconcile
- Batches 1–34 fully committed. Audit CLEAN at start: 266 nodes, 1541 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** (no scout agents this run — user did not request them). One concept end-to-end, then commit; dedup gate before each.
- All 12 candidate filenames confirmed MISSING before writing (Glob check). `naga` is NOT a node (the glob `naga*` matched `nagarjuna` only) → no nāga-class parent edge minted (would have been a dangling stub).

### Batch 35 concepts — 12 / 12 done (0 blocked, 2 contested, 0 needs-opus-review)

**Cluster A — darśana author/source anchors (3):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | prashastapada | done | medium | author of *Padārthadharmasaṃgraha*; the bhāṣya that overshadowed Kaṇāda's sūtra |
| 2 | mandana-mishra | done | medium | **contested** — Mīmāṃsā→Advaita bridge; the doubtful Maṇḍana=Sureśvara identity |
| 3 | vindhyavasin | done | **low** | Sāṃkhya reformer known only via Paramārtha's *Life of Vasubandhu* + Frauwallner; no extant work |

**Cluster B — Neoplatonic/Greek depth (4):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 4 | syrianus | done | **high** | Proclus's teacher; likely *originator* of the henads (resolves the contested origin to a node) |
| 5 | theurgy | done | **high** | salvation by ritual means (Iamblichus); the contemplation-vs-ritual break |
| 6 | damascius | done | **high** | last Athenian scholarch; the Ineffable (*arrhēton*) beyond the One |
| 7 | liber-de-causis | done | **high** | Proclus-derived "Book of the Pure Good"; long mistaken for Aristotle; Aquinas corrected it |

**Cluster C — Hindu churning cluster (5):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 8 | samudra-manthana | done | medium | the churning episode — apparatus + ratna-cluster anchor |
| 9 | vasuki | done | medium | king of nāgas; churning-cord; Śiva's neck-serpent; Kadrū's son |
| 10 | kurma | done | medium | **contested** — tortoise avatāra / churning-pivot; Vedic Prajāpati-tortoise reattributed to Viṣṇu |
| 11 | amrita | done | medium | nectar of immortality; IE cognate of Greek *ambrosia*; Buddhist *amata* reuse |
| 12 | dhanvantari | done | medium | physician of the gods; rises with the amṛta-pot; deity of Āyurveda |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **kurma** `contested`: the churning-pivot role converges, but the deeper identity splits diachronically — the **Śatapatha Brāhmaṇa cosmic tortoise = Prajāpati/Brahmā**, later *transferred* to Viṣṇu as Vaiṣṇavism rose. Mapped as a reading table; the Vedic→Vaiṣṇava shift is the finding, not a single timeless avatāra.
- **mandana-mishra** `contested`: Mīmāṃsā→Advaita bridge + Brahmasiddhi authorship converge, but the **Maṇḍana = Sureśvara** identification is "doubtful" and the debate-legend's subordination to Śaṅkara is questioned (he may have been the dominant Advaitin for a century). Two-question divergence table.
- **vindhyavasin** low conf: known **only at second hand** through a hostile Buddhist biography (Paramārtha) + Frauwallner's reconstruction (weak independence), **no extant work**; dates/king (Vikramāditya = Candragupta II?) contested. The batch-plan's "alternate Yogabhāṣya attribution" was **NOT supported by any source consulted** → explicitly dropped, not asserted.
- **amrita**: the Greek *ambrosia* cognate (PIE *\*n̥-mr̥-tós*) recorded as a **linguistic/structural** parallel, never an identity of myths; Buddhist *amata* = "the deathless" flagged as a reuse for a *different referent* (state, not nectar).
- **prashastapada**: the §4 commentary-tradition inversion noted — the most influential "bhāṣya" is really an independent compendium that **overshadowed the mūla-sūtra** (Vaiśeṣika doctrine anchored on the bhāṣya, not the sūtra).
- **liber-de-causis**: the headline *often-conflated-with-NOT-equivalent* case — a Proclan (Neoplatonic) text long worn as an **Aristotelian** mask until Aquinas (1272, via Moerbeke's Proclus) exposed it. Drawn as the conflation edge to `aristotle-substance`.
- **syrianus**: resolves the Batch-34 proclus-henad **origin** crux — SEP: the henads were "probably introduced by Syrianus himself," making him the likelier of the two candidates (vs Iamblichus); both candidate-origin edges now point to nodes.

### De-orphan inbounds relocated into existing hubs (established de-orphan practice; all purely-symmetric pairs, proven-clean)
`vishnu → shares-vocabulary-with → kurma` · `shiva → shares-vocabulary-with → vasuki` · `paramanu-vaisheshika → shares-vocabulary-with → prashastapada` · `advaita-vedanta → shares-vocabulary-with → mandana-mishra` · `vasubandhu → shares-vocabulary-with → vindhyavasin` · `plotinus-one → shares-vocabulary-with → damascius` · `plotinus-one → shares-vocabulary-with → liber-de-causis`.
Directional edges added to existing files: `proclus → historically-influenced-by → syrianus` (his actual teacher, previously missing) · `iamblichus → formalizes → theurgy` · `proclus-henad → historically-influenced-by → syrianus` (the second/likelier henad-origin candidate). The remaining new nodes (samudra-manthana, amrita, dhanvantari, syrianus, theurgy) self-anchored via cluster edges.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups; manifest in sync. Existing DEVANAGARI/SPLIT flags (ahimsa, vyasa, dravya, karma, moksa, paramanu, pramana, skandha) are the intended tradition-splits, unchanged.
- Graph regenerated: **266 → 278 nodes, 1541 → 1585 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 278 concepts across 35 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 36 (names only — no files written)
- **Churning cluster finish:** `halahala` (the poison Śiva drinks — Nīlakaṇṭha), `mohini` (Viṣṇu's enchantress who distributes the amṛta; the asura-trick), `rahu`/`ketu` (the beheaded asura → eclipse-demon), `parijata` (the churning-tree conflated with kalpavṛkṣa), `airavata`/`ucchaihshravas` (the churning steed and elephant), `lakshmi` already exists.
- **Daśāvatāra spine** (kurma now anchors it): `matsya` (first avatāra, the flood-fish — Manu/Noah parallel), `varaha` (boar, lifts the earth), `narasimha`, `vamana` (the three steps — ties to Bali of the churning frame).
- **Āyurveda** (dhanvantari opens it): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha) — a whole proto-medicine sub-graph.
- **Neoplatonic/Greek closure:** `simplicius` (Damascius's pupil, the great commentator), `marinus` (Proclus's successor), `pseudo-dionysius` (the Christian channel for Proclus — pairs with liber-de-causis as the *other* transmission line), `chaldean-oracles` (theurgy's source-text).
- **Mīmāṃsā/Advaita:** `sureshvara` (would let the Maṇḍana-identity edge resolve), `shankara`/`adi-shankara` (conspicuously still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya` (Vindhyavāsin's teacher).
