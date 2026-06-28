# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 36 done, 289 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 13 (next = Ch 14)**. **→ The planned chapters Ch 14–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 36 — daśāvatāra spine + churning-cluster finish (2026-06-28)

### Startup reconcile
- Batches 1–35 fully committed. Audit CLEAN at start: 278 nodes, 1585 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** (no scout agents). One concept end-to-end, then commit; dedup gate (Glob) before each.
- All 11 candidate filenames confirmed MISSING before writing. **Decision:** did NOT mint a separate `dashavatara` umbrella node — the existing `avatara-vedanta` already carries the daśāvatāra list; each new avatāra is `is-a-type-of: avatara-vedanta` (matching `kurma`).

### Batch 36 concepts — 11 / 11 done (0 blocked, 0 contested-as-status, 0 needs-opus-review)

**Cluster A — daśāvatāra spine (4; kurma/matsya already anchored it):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | matsya | done | medium | first avatāra, flood-fish; ŚB flood-fish → Brahmā (MBh) → Viṣṇu (Purāṇa) diachronic shift |
| 2 | varaha | done | medium | third avatāra, boar lifts earth, slays Hiraṇyākṣa; Vedic Emūṣa/Prajāpati → Viṣṇu |
| 3 | narasimha | done | medium | fourth avatāra, man-lion; the **boon-loophole** theology of the liminal; slays Hiraṇyakaśipu, saves Prahlāda |
| 4 | vamana | done | medium | fifth avatāra, dwarf/Trivikrama; grows from Viṣṇu's **own** Ṛgvedic three strides (NOT a Prajāpati reattribution) |

**Cluster B — churning-cluster finish (7):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 5 | halahala | done | medium | churning-poison (Kālakūṭa) Śiva drinks; etiology of Nīlakaṇṭha |
| 6 | mohini | done | medium | Viṣṇu's enchantress-form; distributes amṛta; occasions Rāhu's beheading; avatāra-vs-māyā recorded |
| 7 | rahu | done | medium | severed head of Svarbhānu, eclipse-demon & ascending lunar node |
| 8 | ketu | done | medium | severed body of Svarbhānu, descending lunar node & comet-stratum |
| 9 | airavata | done | medium | churning white elephant, Indra's mount |
| 10 | ucchaihshravas | done | medium | churning seven-headed horse; hinge of the Kadrū–Vinatā wager |
| 11 | parijata | done | medium | churning-tree & Kṛṣṇa–Satyabhāmā episode; the Pārijāta=Kalpavṛkṣa conflation mapped |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **The Prajāpati→Viṣṇu reattribution thread** (matsya/varaha, echoing kurma): the Vedic Brāhmaṇa cosmic animals (flood-fish, boar Emūṣa) were **Prajāpati/Brahmā**, later transferred to Viṣṇu as Vaiṣṇavism rose — recorded as a diachronic shift (image continuous, theology not), NOT a timeless avatāra. ŚB 14.1.2 explicitly harmonizes Emūṣa into Prajāpati.
- **vamana** is the deliberate contrast case: NOT a reattribution — the avatāra grows from **Viṣṇu's own** Ṛgvedic Trivikrama (1.154); but "neither Bali nor Vāmana appears in" the Vedic strides → the dwarf-frame is the later accretion. Two distinct kinds of Vedic continuity kept apart.
- **rahu/ketu** §0 case: the eclipse-by-swallowing **myth** is NOT an astronomical eclipse theory; classical siddhāntic astronomy gave the shadow/node account **separately**, and the node-points merely took the names Rāhu/Ketu. Mapped as **naming + correlation, not identity** — explicitly resisting "the ancients secretly knew the lunar nodes."
- **mohini** classification divergence: avatāra vs Viṣṇu's *māyā* — function stable, label contested; linked to avatara-vedanta as shares-vocabulary (not is-a-type-of) to honor the open classification.
- **parijata** §5 headline conflation: Pārijāta and Kalpavṛkṣa are **distinct named members** of the five celestial trees (pañca-vṛkṣa: Mandāra/Pārijāta/Santāna/Kalpavṛkṣa/Haricandana), yet "Kalpavṛkṣa" is **also** the class-name — so Pārijāta is "a kalpavṛkṣa" generically while ≠ the tree *named* Kalpavṛkṣa. Drawn as `shares-vocabulary-with` + `often-conflated-with-NOT-equivalent` (the sanctioned two-type pair).

### De-orphan inbounds relocated into existing hubs (established practice; pure-symmetric pairs, no hierarchy on those pairs, proven-clean)
`vishnu → shares-vocabulary-with → vamana` · `shiva → shares-vocabulary-with → halahala` · `kalpavriksha → shares-vocabulary-with / often-conflated-with-NOT-equivalent → parijata`. The other 8 new nodes self-anchored via intra-batch cluster edges (matsya↔varaha↔narasimha; mohini↔rahu↔ketu; airavata↔ucchaihshravas; ucchaihshravas→kadru/vinata/garuda) and existing hubs.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Existing DEVANAGARI/SPLIT ~groups (moksa, paramanu, pramana, skandha, etc.) are intended tradition-splits, unchanged.
- Graph regenerated: **278 → 289 nodes, 1585 → 1636 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 289 concepts across 36 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 37 (names only — no files written)
- **Daśāvatāra completion:** `parashurama` (sixth, the axe-wielding brahmin-warrior), `kalki` (tenth, the future apocalyptic avatāra) — `rama`, `krishna`, `buddha-avatara`/`balarama` already exist or are referenced; this would close the ten.
- **Churning loose ends:** `bali` (Mahābali — owner-variant of Uccaiḥśravas, Vāmana's foil, ties Onam), `indra` (conspicuously still unwritten despite many inbound refs — mount-owner of Airāvata/Uccaiḥśravas), `kaustubha`/`varuni` (remaining ratnas), `svarbhanu` (the pre-beheading asura — would resolve Rāhu/Ketu origin to one node).
- **Āyurveda** (dhanvantari opens it): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha).
- **Neoplatonic/Greek closure:** `simplicius`, `marinus`, `pseudo-dionysius`, `chaldean-oracles`.
- **Mīmāṃsā/Advaita:** `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya`.
