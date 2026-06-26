# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 34 done, 266 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 13 (next = Ch 14)**. **→ The planned chapters Ch 14–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 35 — churning-of-the-ocean cluster + darśana author-anchors + Neoplatonic/Greek depth (2026-06-26) — IN PROGRESS

12 concepts, three clusters. All 12 filenames confirmed MISSING at start (dedup gate passed). Working serially (no scout agents this run).

**Cluster A — darśana author/source anchors (3):**
| # | concept | status | notes |
|---|---|---|---|
| 1 | prashastapada | pending | Vaiśeṣika; *Padārthadharmasaṃgraha*; pairs with kanada |
| 2 | mandana-mishra | pending | Mīmāṃsā→Advaita bridge; Brahmasiddhi |
| 3 | vindhyavasin | pending | Sāṃkhya teacher; alternate Yogabhāṣya attribution |

**Cluster B — Neoplatonic/Greek depth (4):**
| # | concept | status | notes |
|---|---|---|---|
| 4 | syrianus | pending | Proclus's teacher; the other henad-origin candidate |
| 5 | theurgy | pending | ritual ascent as its own concept node |
| 6 | damascius | pending | last Athenian scholarch; *Problems and Solutions* |
| 7 | liber-de-causis | pending | Proclus-derived text into Islamic/Latin metaphysics |

**Cluster C — Hindu churning cluster (5):**
| # | concept | status | notes |
|---|---|---|---|
| 8 | samudra-manthana | pending | the churning episode itself (anchors existing prose refs) |
| 9 | vasuki | pending | the churning-rope nāga, Kadrū's son |
| 10 | kurma | pending | Viṣṇu's tortoise avatar — the churning-pivot |
| 11 | amrita | pending | nectar of immortality — the churning's prize |
| 12 | dhanvantari | pending | physician-god who rises with the amṛta |

Existing files that reference these (future inbound de-orphan sources): kamadhenu, kalpavriksha, vinata, kadru, iamblichus, lakshmi, henosis, aruna, garuda, neoplatonism.

## Batch 34 — darśana root-text author-anchors + Hindu serpent/bird iconography + Neoplatonic depth (2026-06-24)

### Startup reconcile
- Batches 1–33 + Ch-13 chapter run fully committed. Audit CLEAN at start: 251 nodes, 1491 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Ran in **parallel-research mode** (user request: "run 3–5 agents to fish for concepts"): **4 read-only scout agents** gathered §4 signal bundles for disjoint key-sets; all writing, dedup gating, and commits done **serially** in the main session. Parallelism confined to the safe (research) half — the dedup gate and one-commit-per-concept invariants stayed intact, the graph never forked.
- All 15 candidate filenames confirmed missing before writing; `vyasa` already existed → dropped from the pool (new nodes link to it instead).

### Batch 34 concepts (plan) — 15 concepts, three clusters

**Cluster A — darśana root-text author/source anchors (5):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | kanada | done | medium | founder of Vaiśeṣika; expressed-by vaiseshika-sutra |
| 2 | jaimini | done | medium | author of Mīmāṃsā Sūtra; expressed-by mimamsa-sutra |
| 3 | badarayana | done | medium | author of Brahma Sūtra; **contested** — Bādarāyaṇa=Vyāsa identity |
| 4 | vatsyayana | done | **high** | author of Nyāya-Bhāṣya; ≠ Kāmasūtra Vātsyāyana |
| 5 | vyasa-yogabhasya | done | **low** | Yogabhāṣya author; **contested** — authorship (Maas: =Patañjali) |

**Cluster B — Neoplatonic depth (4):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 6 | iamblichus | done | high | theurgy; the contemplation-vs-ritual break with Porphyry |
| 7 | psyche-neoplatonic | done | high | Soul, the third hypostasis; ≠ modern psyche / jīva / Brahman |
| 8 | proclus-henad | done | medium | the henads; mediating the One; origin contested (Iamblichus/Syrianus) |
| 9 | ammonius-saccas | **blocked** | low | Plotinus' teacher; wrote nothing, doctrine unattested |

**Cluster C — Hindu serpent/bird iconography + wish-objects (6):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 10 | jatayu | done | medium | Rāmāyaṇa vulture-demigod; dies fighting Rāvaṇa for Sītā |
| 11 | sampati | done | medium | elder vulture brother; locates Sītā on Laṅkā |
| 12 | kadru | done | medium | serpent-mother of the nāgas; co-wife rival of Vinatā |
| 13 | vinata | done | medium | mother of Garuḍa & Aruṇa; bird-line rival of Kadrū |
| 14 | shesha | done | **high** | cosmic serpent Śeṣa/Ananta; the remainder at pralaya (ananta = alias, NOT a separate node) |
| 15 | kalpavriksha | done | medium | wish-fulfilling tree of the churning; parallels Kāmadhenu |

## Run log — Batch 34 (2026-06-24)

### Concepts completed: 15 / 15 (1 blocked, 2 contested, 0 needs-opus-review)
Author-anchor payoff again: each darśana-author node gives a reverse-only root-text node a correctly-directed `expressed-by` inbound (kanada→vaiseshika-sutra, jaimini→mimamsa-sutra, badarayana→brahma-sutra). Neoplatonic depth completes the One→Nous→Soul triad (psyche-neoplatonic) and adds the henad/theurgy layer. Cluster C completes the Aruṇa/Vinatā/Kadrū avian-serpent family and the churning wish-objects.

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **badarayana** `contested`: authorship of the Brahma Sūtra converged, but the **Bādarāyaṇa = Veda-Vyāsa** identification is a later (8th–9th c.) overlay flagged as anachronism — mapped as a divergence table, drawn `often-conflated-with-NOT-equivalent → vyasa`.
- **vyasa-yogabhasya** `contested`/low: the modern single-author thesis (sūtra+bhāṣya = one *Pātañjalayogaśāstra* by Patañjali) traces to **one scholar (Maas)** reported by many — the §4 independence trap; confidence capped low. The "Vyāsa" ≠ legendary Mahābhārata Vyāsa (later honorific overlay).
- **ammonius-saccas** `blocked`: wrote nothing + "pledge of silence" ⇒ no doctrine to gloss; Christian-vs-pagan and "two Ammonii" both irreducibly contested; only tertiary modern sources exist (no SEP entry). Committed blocked with the absence recorded as the finding.
- **vatsyayana**: name-collision with **Vātsyāyana Mallanāga** (Kāmasūtra author) taught in prose, single node (the patanjali-grammarian precedent) — any future Kāmasūtra node must take a disambiguating key.
- **shesha/ananta**: resolved to **one node** (every source treats Ananta as an epithet, not a distinct being); ananta recorded as a verified alias, no `ananta.md` minted. The *śeṣa* = "remainder at pralaya" doctrine recorded precisely, NOT as a cosmological-physics claim.
- **kanada**: the *paramāṇu* atomism guardrail noted in-file — the "ancient Indian atom = modern physics" conflation belongs on the paramanu node, not the author file.
- Genuine source disagreements surfaced per §4: darśana-author **datings** all left as wide ranges (Kaṇāda, Jaimini, Vātsyāyana); proclus-henad **origin** (Iamblichus vs Syrianus); Jaṭāyu/Sampāti **genealogy** (encyclopedic "Śyenī as mother" vs Vālmīki's "Śyenī a distant ancestress, Aruṇa the father").

### De-orphan inbounds relocated into existing hubs (§5 forward-only / symmetric-where-apt; no mechanical mirroring beyond the established de-orphan practice)
`kumarila-bhatta → historically-influenced-by → jaimini` · `gautama-aksapada → structurally-parallel-to → kanada` (sym) · `pramana-nyaya → historically-influenced-by → vatsyayana` · `proclus → expressed-by → proclus-henad` (replacing `part-of: proclus` in the henad file to avoid a bidirectional-directional defect) · `plotinus → expressed-by → psyche-neoplatonic` · `vishnu → shares-vocabulary-with → shesha` (sym) · `kamadhenu → structurally-parallel-to → kalpavriksha` (sym) · `vyasa → often-conflated-with-NOT-equivalent → vyasa-yogabhasya`. The 8 within-cluster nodes (jatayu↔sampati, kadru↔vinata, iamblichus, badarayana) self-anchored via their cluster edges.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups. The `व्यास` DEVANAGARI flag (vyasa / vyasa-yogabhasya) is the **intended** tradition/identity split — carries the required `often-conflated-with-NOT-equivalent` edge, so the map teaches the distinction rather than forking.
- Graph regenerated: **251 → 266 nodes, 1491 → 1541 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 266 concepts across 34 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 35 (names only — no files written)
- Remaining darśana author-anchors: `vatsyayana` done; consider `vyasa-brahmasutra` is covered by badarayana; `prashastapada` (Vaiśeṣika — the *Padārthadharmasaṃgraha*, pairing with kanada), `vindhyavasin` (the alternate Yogabhāṣya attribution), `mandana-mishra` (Maṇḍana — Mīmāṃsā/Advaita bridge).
- Neoplatonic/Greek depth: `syrianus` (Proclus's teacher; the other henad-origin candidate — would let the contested edge resolve to a node), `theurgy` as its own concept node, `damascius` (last Athenian scholarch), `liber-de-causis` (the Proclus-derived text that entered Islamic/Latin metaphysics).
- Hindu serpent/bird/churning cluster: `samudra-manthana` (the churning episode itself — currently referenced in prose by kalpavriksha/kamadhenu/kadru but unwritten; would anchor the whole cluster), `vasuki` (the churning-rope nāga, Kadrū's son), `parijata` (the churning-tree conflated with kalpavṛkṣa), `ravana` (referenced by jatayu, still unwritten).
