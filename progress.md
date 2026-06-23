# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 33 done, 251 concepts** (audit CLEAN).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 13 (next = Ch 14)**. **→ The planned chapters Ch 14–20 are listed in the `## Chapter roadmap` table in `chapters/INDEX.md`** — a fresh session picks the lowest-numbered `planned` row. NOTE: `hindu/` now has a **second level** (`darsana/`, `devotional/`, `scripture/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

## Batch 32 — author anchors + Hindu iconography (2026-06-22)

### Startup reconcile
- Batches 1–31 + linker passes + directional-edge integrity pass fully committed. Audit CLEAN: 230 nodes, 1401 edges, 0 orphans, 0 stubs, 0 bidirectional-directional, 0 forbidden combos. Working tree clean — no interrupted draft.
- All 8 Batch-32 candidate filenames confirmed missing (non-breaking to write).

### Batch 32 concepts (plan)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `asanga.md` | done | Yogācāra co-founder; anchors cluster from Vasubandhu's other side |
| 2 | `dharmakirti.md` | done | anchors pramanavarttika; Dignāga's great successor |
| 3 | `makkhali-gosala.md` | done | anchors ajivika; niyati/fatalism |
| 4 | `plotinus.md` | done | anchors neoplatonism; the One/emanation |
| 5 | `nataraja.md` | done | Śiva's cosmic dance; creation/dissolution cycle |
| 6 | `kartikeya.md` | done | Skanda/Murugan; Pārvatī's other son; completes family |
| 7 | `surya.md` | done | Vedic sun deity |
| 8 | `nandi.md` | done | Śiva's bull-mount/gatekeeper |

## Run log — Batch 32 (2026-06-22)

### Concepts completed: 8 / 8 (0 blocked, 0 needs-opus-review)
All converged, confidence medium. Four author/source anchors (which convert low-degree reverse-only nodes into properly-anchored hubs) + four Hindu deity/iconography nodes (completing the Śaiva household).

| concept | status | conf | key source(s) | signal independence |
|---|---|---|---|---|
| asanga | converged | medium | Wikipedia + Encyclopedia of Buddhism/EBSCO + corpus | 2 independent refs + corpus |
| dharmakirti | converged | medium | Wikipedia + **SEP** (disagree on dates — surfaced) + corpus | 2 independent refs + corpus |
| makkhali-gosala | converged | medium | Wikipedia ×2 (related pages, weak independence — flagged) + corpus | sources ultimately = 2 hostile non-Ājīvika texts; held at medium |
| plotinus | converged | medium | **SEP** + Wikipedia + corpus | 2 independent refs + corpus |
| nataraja | converged | medium | Wikipedia + corpus (Britannica 403) | 1 ref + corpus cluster |
| kartikeya | converged | medium | Wikipedia + corpus deity cluster | 1 ref + corpus cluster |
| surya | converged | medium | Wikipedia + **World History Enc.** + corpus | 2 independent refs + corpus |
| nandi | converged | medium | Wikipedia + corpus (shiva/lingam/jiva/hanuman) | 1 ref + corpus cluster |

### Anchor payoff (the point of the author nodes)
Each of the four person/source nodes converts a previously low-degree, "reverse-only" node into an anchored hub by giving it a correctly-directed inbound from its author/founder:
- `asanga → formalizes → yogacara`, `→ expressed-by → alaya-vijnana/trisvabhava`; inbound `vasubandhu → historically-influenced-by → asanga` (Asaṅga converted his younger half-brother).
- `dharmakirti → expressed-by → pramanavarttika` (anchors the text to its author), `→ historically-influenced-by → dignaga-pramana`; inbound `dharmottara → historically-influenced-by → dharmakirti`.
- `makkhali-gosala → formalizes → ajivika`; inbound `mahavira → shares-vocabulary-with → makkhali-gosala`.
- `plotinus → formalizes → neoplatonism`, `→ expressed-by → plotinus-one`; inbound `moksha-advaita → structurally-parallel-to → plotinus` (henōsis ∥ ātman-return).

### Prime-directive payoff this batch
`nataraja` carries the explicit `often-conflated-with-NOT-equivalent → modern-atom` edge for the **Capra/CERN "cosmic dance = modern physics"** claim (2004 CERN gift + plaque). Framed precisely: Naṭarāja is a Śaiva Siddhānta soteriological icon (pañcakṛtya — creation/preservation/destruction/concealment/grace, the freeing of souls from māyā), NOT a depiction of subatomic pair-creation; the physics reading is a 20th-c. analogy imposed from outside. Drawn dotted so the map teaches the distinction (§0/§5).

### Honest-divergence findings recorded (not smoothed over)
- **dharmakirti dating** is genuinely contested (Frauwallner 600–660 vs Krasser mid-6th vs Balcerowicz 550–610) — surfaced as a table per §4, not collapsed to a single date.
- **makkhali-gosala** has **no surviving Ājīvika scripture**; the entire portrait comes from two hostile rival sources (Jain *Bhagavatī*, Buddhist *Sāmaññaphala*). Independence explicitly downgraded; confidence held at medium for that reason.
- **kartikeya** birth myths are deliberately plural (six Kṛttikā-sparks vs Agni/Gaṅgā) — recorded as variants, not reconciled.

### Inbound edges relocated into existing hubs (to keep new all-outbound nodes non-orphan, §5 forward-only / no mechanical mirroring)
`vasubandhu→asanga`, `dharmottara→dharmakirti`, `mahavira→makkhali-gosala`, `moksha-advaita→plotinus`, `shaivism→nataraja`, `agni→surya`, `shiva→kartikeya`, `shiva→nandi`.

### Audits (deterministic, via build_graph audit_graph)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `is-a-type-of` directions checked specific→general: `nataraja → shiva` (Naṭarāja is a form of the broader deity Śiva). No bidirectional symmetric pairs introduced for the 8 new nodes (each symmetric edge stored once).
- Graph regenerated: **230 → 238 nodes, 1401 → 1439 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md` refreshed.

### Corpus milestone: 238 concepts across 32 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 33 (names only — no files written)
- Remaining author/source anchors: `dharmakirti` done; consider `kumarila-bhatta` / `prabhakara` (anchor mimamsa-pramana from the author side), `patanjali` (anchor yoga-darshana), `kapila` (anchor samkhya), `gautama-aksapada` (anchor nyaya-sutra).
- Hindu iconography/family completion: `trimurti` already exists; consider `garuda` (Viṣṇu's vāhana, parallels Nandi/Hanumān attendant pattern), `kamadhenu`, `aruna`, `kala-bhairava`.
- Greek/Neoplatonic depth now that `plotinus` exists: `proclus` / `porphyry` (anchor the post-Plotinus school), `plotinus-one` is written — consider `nous` and `henosis` as their own nodes if forward-linked.

---

## Batch 33 — three chapters: darśana author-anchors + Hindu iconography + Neoplatonic depth (2026-06-22)

### Startup reconcile
- Batches 1–32 fully committed. Audit CLEAN at HEAD `ea6a9e5`: 238 nodes, 1439 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- All 13 Batch-33 candidate filenames confirmed missing (non-breaking to write).

### Batch 33 concepts (plan) — three chapters, 13 concepts

**Chapter A — darśana author/source anchors (5):**

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `kapila.md` | done | legendary founder of Sāṃkhya; anchors samkhya-karika lineage |
| 2 | `patanjali.md` | done | author of Yoga Sūtra; anchors yoga-darshana |
| 3 | `gautama-aksapada.md` | done | author of Nyāyasūtra; anchors nyaya-sutra |
| 4 | `kumarila-bhatta.md` | done | Bhāṭṭa Mīmāṃsā founder; anchors mimamsa-pramana |
| 5 | `prabhakara.md` | done | Prābhākara Mīmāṃsā founder; rival sub-school |

**Chapter B — Hindu iconography / vāhana + family completion (4):**

| # | concept (filename) | status | notes |
|---|---|---|---|
| 6 | `garuda.md` | done | Viṣṇu's eagle vāhana; parallels Nandi attendant pattern |
| 7 | `kamadhenu.md` | done | wish-fulfilling cow; sacred-cow iconography |
| 8 | `aruna.md` | done | Sūrya's charioteer (dawn); inbound to surya |
| 9 | `kala-bhairava.md` | done | fierce form of Śiva; is-a-type-of shiva |

**Chapter C — Greek / Neoplatonic depth (4):**

| # | concept (filename) | status | notes |
|---|---|---|---|
| 10 | `porphyry.md` | done | Plotinus's student/editor of the Enneads; Isagoge |
| 11 | `proclus.md` | done | late systematizer; henads; Elements of Theology |
| 12 | `nous.md` | done | the Intellect, second hypostasis |
| 13 | `henosis.md` | done | mystical union with the One; the goal of return |

## Run log — Batch 33 (2026-06-22)

### Concepts completed: 13 / 13 (0 blocked, 0 needs-opus-review)
All converged, confidence medium. Three chapters: 5 darśana author/source-anchors + 4 Hindu iconography nodes + 4 Neoplatonic-depth nodes. Same anchor payoff as Batch 32 — each author/founder node gives an existing reverse-only darśana/text node a correctly-directed inbound, converting it into an anchored hub.

| # | concept | chapter | status | conf | key source(s) | signal independence |
|---|---|---|---|---|---|---|
| 1 | kapila | A | converged | medium | Wikipedia + World History Enc. + corpus | 2 independent refs + corpus |
| 2 | patanjali | A | converged | medium | Wikipedia + **IEP** + corpus | 2 independent refs + corpus |
| 3 | gautama-aksapada | A | converged | medium | Wikipedia + corpus (nyaya-sutra: Wiki+IEP) | 2 independent streams |
| 4 | kumarila-bhatta | A | converged | medium | Wikipedia + **SEP** + corpus | 2 independent refs + corpus |
| 5 | prabhakara | A | converged | medium | Wikipedia + IGNOU/Britannica/studyphilo cluster | 2 independent streams |
| 6 | garuda | B | converged | medium | Wikipedia + World History Enc. | 2 independent refs |
| 7 | kamadhenu | B | converged | medium | Wikipedia + devotional cluster (weak provenance) + corpus | 2 streams, provenance caveat |
| 8 | aruna | B | converged | medium | Wikipedia + mythology cluster (weak provenance) | 2 streams, provenance caveat |
| 9 | kala-bhairava | B | converged | medium | Wikipedia + temple/devotional cluster + corpus | 2 streams + corpus |
| 10 | porphyry | C | converged | medium | **SEP** + Wikipedia | 2 authoritative refs (strong agreement) |
| 11 | proclus | C | converged | medium | **SEP** + Wikipedia (disagree on prop-count 211/217 — surfaced) | 2 authoritative refs |
| 12 | nous | C | converged | medium | Wikipedia + corpus (SEP-grounded) | ref + corpus |
| 13 | henosis | C | converged | medium | Wikipedia + corpus (SEP-grounded) | ref + corpus |

### Anchor payoff (Chapter A)
- `kapila → expressed-by → prakriti-samkhya/purusha-samkhya`; inbound `samkhya-karika → historically-influenced-by → kapila` (the kārikā traces its lineage to the legendary founder).
- `patanjali → formalizes → yoga-darshana`, `→ expressed-by → citta-vritti`, `→ historically-influenced-by → kapila` ("seśvara Sāṃkhya").
- `gautama-aksapada → expressed-by → nyaya-sutra` (author→root-text, the dharmakīrti→pramanavarttika pattern).
- `kumarila-bhatta → expressed-by → mimamsa-pramana`, `→ historically-influenced-by → mimamsa-sutra`; the Dignāga duel drawn (`shares-vocabulary` + `often-conflated`).
- `prabhakara → expressed-by → mimamsa-pramana`, `→ historically-influenced-by → mimamsa-sutra`; rival of Kumārila (`structurally-parallel` + `often-conflated`).

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **Two Kapilas** flagged NOT-equivalent: the atheistic (*nirīśvara*) Sāṃkhya founder vs the Purāṇic Viṣṇu-avatāra preaching bhakti — same name, opposed doctrine.
- **Patañjali grammarian-conflation** (Yoga-sūtra author ≠ Mahābhāṣya grammarian; first equated by Bhojadeva ~10th c.) and **Gautama name-collisions** (≠ Gautama Buddha's clan name; ≠ the Dharmasūtra Gautama) recorded in prose (no target nodes for typed edges).
- **Kāla Bhairava ↔ kala-dravya** NOT-equivalent: personified Hindu time/death-deity vs impersonal Jain time-substance — shared word *kāla*, opposite ontology.
- **Nous ↔ Brahman** NOT-equivalent: Advaita's Brahman-as-*cit* maps onto the Neoplatonic **second** hypostasis (Nous), not the supra-conscious One — "the Advaita highest is the Neoplatonic second-highest."
- **henōsis ↔ mokṣa-advaita** NOT-equivalent: achieved merger with a supra-conscious source vs removal of ignorance about a pre-existing non-duality.
- Genuine source disagreements surfaced per §4: Prabhākara/Kumārila **teacher-student chronology** (Jhā reverses it); Proclus **proposition count** (211 vs 217); Kapila/Gautama **historicity** (legendary anchors).

### Inbound edges relocated into existing hubs (§5 forward-only / no mechanical mirroring; symmetric bidirectional where appropriate)
`samkhya-karika→kapila`, `vishnu→garuda`, `kapila→patanjali`(sym), `prabhakara→kumarila-bhatta`(sym), `kapila→gautama-aksapada`(sym), `surya→aruna`(sym), `shiva→kala-bhairava`(sym), `lakshmi→kamadhenu`(sym), `proclus↔porphyry`(sym, both directions), `plotinus→nous`, `plotinus→henosis`.

### Audits (deterministic, via build_graph audit_graph)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `is-a-type-of` direction checked specific→general: `kala-bhairava → shiva` (Bhairava is a form of the broader deity Śiva). New symmetric pairs stored once except `proclus↔porphyry` (stored both directions, each note from its own vantage, §5-permitted).
- Graph regenerated: **238 → 251 nodes, 1439 → 1491 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md` refreshed.

### Corpus milestone: 251 concepts across 33 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 34 (names only — no files written)
- Remaining darśana author-anchors: `kanada` (anchor vaiseshika-sutra from the author side, pairing with gautama-aksapada), `jaimini` (anchor mimamsa-sutra from its author — currently reverse-only), `badarayana`/`vyasa` (anchor brahma-sutra), `vatsyayana` (Nyāyabhāṣya commentator), `vyasa-yogabhasya`.
- Neoplatonic/Greek depth: `iamblichus` (theurgy; the contemplation-vs-ritual split with Plotinus/Porphyry), `psyche-neoplatonic` (the Soul, third hypostasis — completes One/Nous/Soul triad), `proclus-henad` (the henads as their own node), `ammonius-saccas`.
- Hindu iconography: `sampati-jatayu` (Aruṇa's vulture sons; Rāmāyaṇa), `kadru` / `vinata` (the serpent/​bird co-wives), `kalpavriksha` (wish-tree, parallels Kāmadhenu), `shesha`/`ananta` (Viṣṇu's serpent-couch, pairs with Garuḍa).

---

## Chapter run — Ch 13 Neoplatonism + hindu/ sub-folder reorg (2026-06-23)

**Task:** "make the next chapter and put it into the right sub-folder" + "isn't hindu subfolder too big to just be one head folder? … make sub folders in hindu itself." Chose the **closest-to-finishing** cluster (user's instruction): the 7 already-written, tightly-bound Neoplatonic concepts — a complete self-contained mini-arc that a single chapter closes with **no dangling concepts**.

### Chapter authored (in chapters/comparanda/ — non-Indian parallel, matching Ch 06)
- **Ch 13 — Neoplatonism: "The One Above Thought"** → `chapters/comparanda/13-neoplatonism.md`.
- Primary concepts (7, all pre-written graph nodes; chapter is a reading-view, no new nodes): `neoplatonism` · `plotinus` · `plotinus-one` · `nous` · `henosis` · `porphyry` · `proclus`.
- Cross-refs: `plato-forms`/`plato-soul` (Greek comparanda), `brahman`/`advaita-vedanta`/`moksha-advaita` (Ch 11), `sunyata`/`nirvana-buddhist` (Ch 12).
- **Prime-directive payoff (§7):** draws the real `structurally-parallel-to` Advaita (emanation→return architecture) then the precise `NOT-equivalent`: the One is *beyond* consciousness, so Brahman-as-*cit* maps to **Nous (2nd hypostasis), not the One** — "the Advaita highest is the Neoplatonic second-highest"; plus real-emanation vs māyā-appearance, and henōsis (achieved merger) vs mokṣa (removal of ignorance). §8 adds One≠śūnyatā (plenum-source vs absence-of-essence) and One≠nirvāṇa (generative vs cessation). Source disagreements surfaced not smoothed (birth-year 204/5; *Elements* prop-count 211 vs 217).

### hindu/ sub-folder reorganisation (user request — anticipating growth)
- `hindu/` was a flat head-folder; Hindu material spans 3 genuinely different domains. Introduced a **second level**:
  - `hindu/darsana/` — philosophical systems (āstika darśanas). **Moved `11-vedanta.md` → `hindu/darsana/11-vedanta.md`** via `git mv`.
  - `hindu/devotional/` — deities/iconography/bhakti (README placement-note committed to hold the dir + document the convention).
  - `hindu/scripture/` — epics/canonical texts (README placement-note).
- `chapters/INDEX.md` updated: subfolder-scheme header rewritten (now documents hindu/'s 2nd level + buddhist/, which were missing); Ch 11 path fixed to `hindu/darsana/`; **Ch 13 row added**; 7 Ch-13 concept→chapter mappings added.

### No graph impact
Chapters are NOT graph nodes — `build_graph.py` ignores `chapters/`. Corpus unchanged at **251 nodes / 1491 edges**, audit still CLEAN. No graph regen needed. (progress.md run-logs referencing the old `hindu/11-vedanta.md` path are left as historical record; only the live INDEX was repathed.)

### Suggested next chapter (Ch 14) — now a full roadmap
A standing **`## Chapter roadmap`** table (Ch 14–20) was added to **`chapters/INDEX.md`**; a fresh session should pick the lowest-numbered `planned` row there. Ch 14 = **Greek & Hellenistic Foundation** (`comparanda/`). Subsequent planned: 15 Sāṃkhya & Yoga, 16 Nyāya & Vaiśeṣika, 17 Mīmāṃsā & Cārvāka (all `hindu/darsana/`), 18 Hindu Deities (`hindu/devotional/`), 19 Hindu Epics & Scripture (`hindu/scripture/`), 20 Buddhist Scholastics & Logicians (`buddhist/`). All listed concepts already exist as nodes — chapters add no graph nodes.
