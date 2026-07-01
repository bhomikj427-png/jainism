# Jain Translation Reading-Room — driver + work queue

> **FRESH SESSION: start here.** This is a THIRD track, separate from concept-batches (`progress.md`) and
> teaching-chapters (`chapters/INDEX.md`). If the user says **"build the next thing"** (or "next translation"),
> open this file, take the **lowest-numbered `pending` unit** in the Work Queue below, and build it to the
> **File Format spec** using the **Method** — nothing else. One unit end-to-end, then commit. Do not batch units.

---

## §A Why this exists (read before building — this is the guardrail)

The user wants to *understand the Jain texts word-by-word*, not just read one translator's finished English.
Fine — but the method has a hard firewall, and violating it defeats the whole point:

- We do **NOT** produce an original translation off the Sanskrit/Prakrit. (CLAUDE.md §1 — "librarian, not translator-from-scratch.")
- Each **word-gloss** comes from a **published lexicon / word-index** (Monier-Williams, cited edition glossaries) — never from memory or guessing.
- **Which sense wins is decided by the COMMENTARY** (mūla + bhāṣya + ṭīkā / Sarvārthasiddhi) **and internal consistency** — NOT by "which reading sounds scientific." (CLAUDE.md §0.)
- **Modern science lives ONLY in a quarantined, labelled "Modern comparison" box.** It is typed as `structurally-parallel-to`
  or `often-conflated-with-NOT-equivalent`, it is a *comparison* not an identity, and it is **never allowed to feed back
  into the disambiguation.** For devotional/poetic texts this box is almost always **N/A** — and that is correct; we do
  not hunt for physics in a praise-hymn.
- If a word can't be sourced to a published lexicon, **flag it — do not invent a gloss.**
- Both recensions matter: **Digambara** (Pūjyapāda's *Sarvārthasiddhi*, ~357 sūtras) vs **Śvetāmbara** (Umāsvāti's
  *Svopajña-bhāṣya*, ~344 sūtras) differ in numbering and some readings. Record divergence, don't smooth it.

## §B Sourcing bar (per unit — same discipline as §4 of the charter)

1. **Base text** (IAST + Devanāgarī if in source) from a citable edition — state which recension.
2. **Lexical range** for each key word from Monier-Williams and/or the edition's own word-index — cited.
3. **Commentary** for disambiguation — *Sarvārthasiddhi* (Dig.) and/or Umāsvāti's *bhāṣya* (Śvet.); Tatia's notes.
4. **≥2 published translations** quoted for the comparison panel (Tatia 1994; Jacobi SBE; others) — check they're
   genuinely independent, not reworkings of one source.
5. If <2 independent sources are findable after ~5 fetches → mark the unit `blocked` with what's missing, commit, move on.

## §C File format — per verse/sūtra (copy this skeleton)

Doctrinal and devotional share the skeleton; devotional adds **Meter** and defaults **Modern comparison** to N/A.

```
## <ref, e.g. TS 5.1>   |   <recension used>

**Text (IAST):** <from cited edition>
**Devanāgarī:** <only if verified from a source; omit otherwise>
**Meter:** <devotional only — e.g. Vasantatilakā>

**Padaccheda — word-split & lexical range** (each row cited to a published lexicon/word-index):
| word | grammatical form | attested meaning-range | lexical source |
|------|------------------|------------------------|----------------|
| ...  | ...              | ...                    | MW p.___ / ... |

**Disambiguation (from commentary):** <which sense of each contested word wins, and WHY, per bhāṣya /
Sarvārthasiddhi / ṭīkā — cited. This is the reading that governs.>

**Assembled reading:** <the resulting plain-English sense, grounded strictly in the rows + disambiguation
above. Not a stylistic flourish, not a from-scratch translation.>

**Published translations (comparison only):**
- Tatia (1994): "<≤ ~one line>"
- Jacobi (SBE): "<...>"
- <divergence noted if they disagree>

**Modern comparison (QUARANTINED — labelled, never feeds disambiguation):** <N/A for most verses. If a real
structural parallel exists, state it as `structurally-parallel-to` / `often-conflated-with-NOT-equivalent`,
with the NOT-identity spelled out.>

**Links to concept nodes:** [[dravya]] [[pudgala]] ...   (existing graph nodes in concepts/)

**Sources:** <author/edition + URL; mark critical-edition vs website>
```

Header of each chapter-file: front-note stating text, author, recension, edition(s) used, and status
(`in-progress | drafted | blocked`).

## §D Structure (already created)

```
chapters/jain/translations/
    INDEX.md                     ← this driver
    doctrinal/
        tattvartha/              ← Tattvārtha Sūtra, one file per adhyāya
    devotional/
        bhaktamar/               ← Bhaktāmar Stotra, verse ranges per file
```

---

## §E WORK QUEUE  — build the lowest-numbered `pending`, one at a time

| # | unit | file to create | status | notes |
|---|------|----------------|--------|-------|
| 1 | **PROTOTYPE — TS 5.1 (single sūtra)** | `doctrinal/tattvartha/05-substances.md` (start it with 5.1 only) | pending | Prove the doctrinal format on the hardest case. **STOP after 5.1 and show the user for approval before continuing the chapter.** |
| 2 | **PROTOTYPE — Bhaktāmar v1 (single verse)** | `devotional/bhaktamar/01-bhaktamar.md` (verse 1 only) | pending | Prove the devotional format (meter; Modern-comparison = N/A). **STOP after v1 for approval.** |
| 3 | TS Adhyāya 5 — remainder (5.2 → end) | `doctrinal/tattvartha/05-substances.md` | pending | The substances: ajīva, dravya, pudgala, paramāṇu, skandha, dharma/adharma/ākāśa/kāla. Only after #1 approved. |
| 4 | TS Adhyāya 1 — knowledge & means | `doctrinal/tattvartha/01-knowledge.md` | pending | 5 jñānas, naya, pramāṇa, nikṣepa. |
| 5 | Bhaktāmar — remaining verses | `devotional/bhaktamar/…` | pending | Split into verse-range files (~8–11 verses each) once v1 format is approved. |
| 6 | TS Adhyāya 2 (jīva) | `doctrinal/tattvartha/02-soul.md` | pending | |
| 7 | TS Adhyāya 6 (āsrava) | `doctrinal/tattvartha/06-influx.md` | pending | |
| 8 | TS Adhyāya 8 (bandha) | `doctrinal/tattvartha/08-bondage.md` | pending | |
| 9 | TS Adhyāya 9 (saṃvara/nirjarā) | `doctrinal/tattvartha/09-stoppage-shedding.md` | pending | |
| 10 | TS Adhyāya 7 (vratas) | `doctrinal/tattvartha/07-vows.md` | pending | |
| 11 | TS Adhyāya 3 (lower/middle worlds) | `doctrinal/tattvartha/03-worlds.md` | pending | |
| 12 | TS Adhyāya 4 (celestial beings) | `doctrinal/tattvartha/04-celestials.md` | pending | |
| 13 | TS Adhyāya 10 (mokṣa) | `doctrinal/tattvartha/10-liberation.md` | pending | Shortest chapter; natural closer for the TS. |
| — | Kalyāṇa Mandira Stotra | `devotional/…` | later | To Pārśvanātha; sister-hymn to Bhaktāmar. Queue after TS core + Bhaktāmar. |
| — | Ṇamokāra / Navkār Mantra | `devotional/…` | later | Links back to existing node `ṇamokāra-mantra`. |
| — | Kalyāṇa/Chattāri/Ratnākara etc. | `devotional/…` | later | Confirm citable published translations exist before queuing. |

## §F Open sub-decisions (ask the user only if it changes what to build)

- **Meri Bhāvanā & other modern Hindi devotionals:** default = **include later as a clearly labelled "modern" category**,
  sourced differently from classical Sanskrit/Prakrit texts; **not** in the core queue. User may flip to "classical only."
- **Bhaktāmar recension** (44 Śvetāmbara vs 48 Digambara): decide per the edition we can best source; record the split.

## §G Done-log (append as units complete)

- (none yet)
