# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 38 done, 300 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 14 (next = Ch 15)**. **→ The planned chapters Ch 15–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 38 — Neoplatonic/Greek closure (2026-07-10)

### Startup reconcile
- Batches 1–37 fully committed. Audit CLEAN at start: 296 nodes, 1669 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked serially, one concept end-to-end then commit. Dedup gate (Glob) before writing each file.
- Cluster chosen via user forced-choice (§10 genuine fork among 4 suggested Batch-38 clusters): **Neoplatonic/Greek closure**, 4 concepts, closing out the Ch.13 Neoplatonism cluster.

### Batch 38 concepts — 4 / 4 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | simplicius | converged | medium | last-generation Athenian Neoplatonist commentator; sole preserver of ~2/3 of all surviving verbatim Presocratic fragments via his Aristotle commentaries; 529 CE Academy closure + Persian exile with Damascius; SEP/Wikipedia death-date discrepancy (560 vs 540) surfaced, not silently resolved |
| 2 | marinus | converged | medium | Proclus's student, successor as scholarch, and biographer; *Life of Proclus* (*On Happiness*) flagged explicitly as advocacy (virtue-ascent argument for Proclus's eudaimonia), not neutral biography, even though it's the primary source; destroyed his own *Philebus* commentary |
| 3 | pseudo-dionysius | contested | medium | Christian Neoplatonist writing under a false 1st-c. apostolic name; real Proclan borrowing (procession/return, hierarchy) re-grounded in Trinitarian love and direct divine-creature dependence; genuine three-way contested identity (SEP's "unknown pupil of Proclus" / Peter-the-Iberian / a proposed **Damascius**-identification) presented as a comparison table, none endorsed |
| 4 | chaldean-oracles | converged | medium | 2nd-c. theurgic verse-fragments (Julian the Chaldean/Theurgist), source of the word *theourgia* itself; "Bible of the Neoplatonists" — Proclus/Damascius/Iamblichus treated it as authoritative; flagged provenance problem: surviving fragments are filtered entirely through the same school being asked to treat them as scripture |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **simplicius**: SEP gives his death as ca. 560, Wikipedia as ca. 540 — a real, unresolved discrepancy between two independent reference works, recorded rather than averaged or silently picked.
- **marinus**: the *Life of Proclus* is simultaneously the primary historical source for Proclus's biography *and* explicit hagiographic advocacy (structured to prove Proclus attained eudaimonia, "unmistakably hostile to Christianity") — both facts held together rather than treating the source as neutral testimony.
- **pseudo-dionysius**: the central finding is the corpus's identity itself is genuinely unresolved among scholars — three non-converging candidates (anonymous Proclus-pupil / Peter the Iberian / Damascius) captured as a comparison table per CLAUDE.md §4, with `status: contested` set at the file level specifically for the identity question (doctrine and dating are convergent).
- **chaldean-oracles**: flagged an independence problem one level deeper than usual — not just "are the modern secondary sources independent" (they are) but "is the ancient evidentiary base itself independent of its interpreters" (it is not: every surviving fragment comes via Proclus, Damascius, or Psellos, the very school treating it as scripture).
- A Grokipedia (AI-generated tertiary) hit was again excluded during chaldean-oracles research, continuing the recurring, deliberate exclusion practice from Batches 36–37 (bali, svarbhanu).

### De-orphan / correct-direction edges added to existing files (established practice)
- `damascius → historically-influenced-by → marinus` (Damascius's own file already narrated studying under Marinus in prose but lacked the typed edge).
- `iamblichus → historically-influenced-by → chaldean-oracles` and `proclus → historically-influenced-by → chaldean-oracles` (correct direction: the Oracles are the earlier source; both files already discussed this in prose without a typed edge).
- `henosis → structurally-parallel-to → pseudo-dionysius` and `damascius → structurally-parallel-to → simplicius` (symmetric-type mirror edges, added specifically to de-orphan the two new nodes that otherwise had only outbound edges — same technique as Batch 37's hub-inbound de-orphaning).

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **First pass found 2 orphans** (pseudo-dionysius, simplicius — written but not yet a target of any edge) — resolved by the two symmetric-mirror edges above; **second pass CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Existing DEVANAGARI/SPLIT groups unchanged (aḥiṃsā, vyāsa pairs — pre-existing, not from this batch).
- Graph regenerated: **296 → 300 nodes, 1669 → 1686 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 300 concepts across 38 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 39 (names only — no files written)
- **Āyurveda** (dhanvantari opens it, still unclaimed): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha).
- **Mīmāṃsā/Advaita:** `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya`.
- **Newly opened, carried over from Batch 37:** `varuna` (Indra's Vedic-decline parallel, cited in indra.md but unwritten), `atri` (the RV 5.40 sage who restores the sun, cited in svarbhanu.md but unwritten), `balarama` (Kṛṣṇa's brother, cited in varuni.md but unwritten), `prahlada` (Bali's grandfather, cited in bali.md but unwritten), `vritra`/`verethragna` comparanda cluster (Indo-European dragon-slaying, flagged in indra.md, not yet a node).
- **Newly opened by this batch:** a possible `eriugena` node (John Scottus Eriugena, who translated the Corpus Areopagiticum into Latin and transmitted it to the medieval Christian West — cited in pseudo-dionysius.md but unwritten); `psellos`/`michael-psellos` (the alternate Byzantine transmission line for the Chaldean Oracles fragments, cited in chaldean-oracles.md but unwritten).
