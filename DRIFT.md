# DRIFT.md — the four structural drifts, queued as independent work

> **What this file is.** Four problems that are **not** defects — nothing here fails `check_all.py`, and the repo
> is green — but that are getting **worse by a measurable amount every batch**. They are queued separately
> from `progress.md`'s batch suggestions **because they are a different kind of work**: none of them produces
> new nodes, and all four will keep degrading quietly if only new-node batches are ever run.
>
> **Not loaded at startup**, by design (CLAUDE.md §7) — same convention as `chapters/coverage.md` and
> `progress-archive.md`. `progress.md` carries a one-line pointer here.
>
> **Written at:** 387 concepts · 2410 edges · 41 chapters · after Batch 47 closed (2026-09-02).
> **Author:** the Batch 46 session, reviewing the corpus's direction across Batches 44–47.

---

## Before you start — the 90-second orientation

You do **not** need to read `progress.md`'s run-logs to work this file. You need:

1. **CLAUDE.md** — the charter. §0 (prime directive), §4 (the five signals), §8 (startup reconcile + dedup gate).
2. **This file.**
3. The **startup reconcile still applies** (CLAUDE.md §8): `git status` and `git log --oneline` **first**.
   ⚠ This matters more than usual here. **Multiple sessions work this repo on the same day** — Batches 46 and 47
   closed within ~24 hours of each other, in different sessions. The Batch 46 session began an edit on stale
   assumptions and was saved only by an assertion failing. **Reconcile before you touch anything.**

**Pick ONE item below and work it to a commit.** They are independent; there is no required order. Each is
sized to be worth a session on its own, and D3 and D4 can be done in slices.

**The one rule that applies to all four:** these are *corrections to how the corpus knows things*. Under §8, if
you cannot close an item, **record what you tried and what was missing** and commit that. A recorded failure is
a result here — see D1's log of dead retrieval routes, which exists because two batches burned effort on them.

---

## D1 — The corpus is drifting *away* from primary sources

### The claim
CLAUDE.md §1 says work from **published critical editions and existing scholarly translations**. In practice
Batches 44–47 worked from **reference works *about* those texts**. The corpus is accumulating very
well-documented **second-hand** knowledge. That is honest — every file says so — but it is not the target, and
the gap is widening.

### Measured baseline (re-runnable)
```
grep -l "Identified but not read" concepts/*.md | wc -l     # 65 of 387 files carry an unread-list
```
The lists grow by roughly **8 items per batch and close 1–2**. Batch 46 closed one (Williams) and opened eight.

### The evidence it is real
- Batch 46's only `high`-confidence node, `avacchedaka`, rests on **Matilal-on-Gaṅgeśa, not Gaṅgeśa**.
- **Not one line of Navya-Nyāya Sanskrit was read** in the batch that built the Navya-Nyāya layer.
- Both of the last two batches hit **unreadable OCR on a located critical edition**.

### First move — and it needs no retrieval
⭐ **`Matilal 1968, Parts II–III`.** *The Navya-Nyāya Doctrine of Negation* (Harvard UP) contains **English
translations of Gaṅgeśa's *Abhāva-vāda* and Raghunātha's *Nañvāda*, with the Sanskrit in Appendices A and B.**
Batch 46 downloaded it, read Part I at first hand, **sampled Parts II–III and never worked through them.**

**This is the cheapest high-value item in the corpus.** It is a published scholarly translation of part of the
primary text — exactly what §1 asks for — and it upgrades **four** nodes at once: `abhava`,
`raghunatha-siromani`, `tattvacintamani`, `avacchedaka`.

Retrieval (confirmed working, Batch 46):
```
https://ia802904.us.archive.org/9/items/navyanyayadoctrineofnegationbkmatilal_202003_524_y/Navya-Nyaya-Doctrine-of-Negation-B%20K%20Matilal.pdf
# then: pdftotext -layout matilal.pdf matilal.txt   (OCR is GOOD — Latin text, usable)
```

### Then, in value order
| item | closes |
|---|---|
| **Potter, *Padārthatattvanirūpaṇa*, Harvard-Yenching 17, 1957** | What Raghunātha's "denies atoms" **actually amounts to**, and the number-eliminated/number-added contradiction that `raghunatha-siromani.md` currently papers with a hypothesis **of the corpus's own** |
| **Neevel 1977, pp. 14–16** | The argument that the ācāryas' lifespans were stretched. Wanted by `nathamuni` and `vedanta-desika`; held now only as Freschi's *report* plus the corpus's own arithmetic |
| **The *Ratnaprabhā*; the *Siddhayoga* with Śrīkaṇṭhadatta's *Vyākhyākusumāvalī*** | **Five files depend on these and none has seen a line of either** |
| **Phillips, *Jewel of Reflection…*, 3 vols, Bloomsbury 2020** | The complete *Tattvacintāmaṇi* in English. Highest value, hardest to get |
| **Ingalls, *Materials* (1951)** | The Frege comparison, currently reaching the corpus only through a paper that **disputes** it |

### ⚠ Known-dead routes — do not re-spend on these
- **Britannica** → HTTP 403 (three pages, three attempts).
- **`link.springer.com/rwe/...`** → redirects to an auth endpoint.
- **Uno 1958** at `echo-lab.ddo.jp` → connection refused.
- **Hiriyanna's *Iṣṭasiddhi*** (archive.org `Ista-Siddhi`) and the **1888–1901 *Tattvacintāmaṇi***
  (`tattvachipt403ganguoft`) → downloaded in full; **OCR is garbled Devanāgarī with no Latin at all**, so not
  even the editors' English introductions are recoverable.
- **General rule earned the hard way:** *for pre-war Indological editions, archive.org reliably supplies the
  **provenance** and reliably fails to supply the **text**.* Budget for page-images or a library copy, **not**
  for OCR. (Meulenbeld's HIML and Matilal 1968 are the exceptions — both have good Latin OCR.)

### Definition of done
At least one node moves from *exposition-of-exposition* to *text*, with the reading recorded in its Sources
block and its confidence re-justified. **Closing one item properly beats listing five.**

---

## D2 — The corpus records one side of several disputes

### The claim
Distinct from D1. D1 is about *primacy*; this is about **balance**. Several nodes rest on a single modern
authority, and in a few cases the corpus knows a scholar **only through the person rebutting him**.

### The evidence
- ⚠ **`P. V. Sharma` appears four times in Batch 46 and every time in rebuttal.** Meulenbeld rejects his
  positions on Tīsaṭa's sources (twice), on Vṛnda's date, on the two-Vṛndas split, and on Nāradatta. **The
  corpus has never read him directly.** A file that only ever records one side of a dispute is not neutral,
  however good the source doing the rebutting.
- **`tisata`, `niscalakara`, `vrnda` are one scholar deep** (Meulenbeld), and each says so explicitly.
- 18 files carry an explicit single-source or single-sourced flag:
```
grep -il "single-source dependence\|one scholar deep\|single-sourced" concepts/*.md
```

### What is *not* wrong here
Meulenbeld is the reference work for that literature and **reports his evidence rather than his conclusions**,
so his reasoning is visible and checkable — and in these very passages he argues against *named* scholars, so
the disagreement is on the page. **The problem is not that he is wrong. It is that the corpus cannot tell.**

### First move
Read **P. V. Sharma** on any one of the four disputes and write the other side into the relevant node — even if
the outcome is "Meulenbeld is still right." **The point is that the corpus should be able to say why.**

### Definition of done
At least one dispute in `tisata` / `vrnda` / `niscalakara` has both sides sourced, and the node says which it
follows **and on what grounds** rather than inheriting a verdict.

---

## D3 — The teaching layer is write-once, and its staleness was invisible

### The claim
Chapters are drafted over a batch's new nodes and then **never revisited**, while the nodes underneath them
keep being corrected. `check_chapters.py` proves every concept **has** a chapter row — *coverage*. **Nothing
proved the chapter still says what the concept says — *freshness*.**

### Measured baseline — a detector now exists
```
python graph/check_staleness.py
# baseline at the time of writing: 14 of 34 chapters stale
```
⚠ **It is ADVISORY and deliberately NOT wired into `check_all.py`.** With 14 of 34 flagged, gating on it would
turn the repo red for every session and block unrelated work. **If you drive the count to zero, wiring it in is
then worth doing** — from that point it costs one chapter-edit per batch to stay green.

⚠ **What the detector is not.** A git-history heuristic, not a semantic check. It flags a chapter when a
covered concept was edited later — which can mean a typo fix — and **misses** a chapter that is wrong while
nothing underneath it changed. **A flag means "go look," never "this is wrong."** A clean result is weak
evidence of anything.

### A confirmed, concrete instance — use this to calibrate
**Ch 15 (Sāṃkhya & Yoga)**, last touched **2026-07-10**. Batch 47 then edited `patanjali.md` on **2026-09-01**
and, in its own words, made *"two corrections… (1) **The date here was wrong by a century**"* — plus a finding
that the Patañjali conflation is **three-way, not two-way** (grammarian, yogin **and** physician), and a new
`often-conflated-with-NOT-equivalent: patanjali-grammarian` edge. **Ch 15 still teaches the superseded
account.** That is not a typo-flag; that is the teaching layer contradicting the graph.

### First move
⭐ **Ch 11 (The Vedānta Family).** Last touched **2026-06-23** — **nine chapters** have been written since, and
it predates the entire Advaita-lineage cluster and Chs 36–41. Highest-value single fix. When revising, note
that `vishishtadvaita.md` now carries a Batch 46 caution that the school as described **is partly
Veṅkaṭanātha's retrospective systematisation**, not a pre-existing consensus — Ch 11 does not know this.

Then **Ch 15** (the confirmed case above), then work down the detector's oldest rows.

### Definition of done
One chapter re-read against every concept it primary-covers, corrected where they disagree, committed — and
the staleness count drops. **Do not** rewrite a chapter wholesale; amend it, the way Batch 46 amended
`anandabodha.md`, so the correction and its reason both stay visible.

---

## D4 — The follow-up debt from Batches 43–46 is nearly untouched

### The claim
Each batch generates follow-ups and closes almost none. Batch 46 closed one (Michael Williams, which had been
carried since 45) out of a carried list of eight-plus, and added eight more.

### The carried list, oldest first
- **`karma-vargana.md`** — still the corpus's **only** `low`-confidence node. *(Verify:
  `grep -l "confidence: low" concepts/*.md`)*
- The **42-vs-93 *nāma*-karma discrepancy** — needs the *Karma-grantha* / *Gommaṭasāra* read directly.
- **`dhatu.md`'s three-vs-four dispute**, with `arunadatta` inside it holding *eka-kāla*.
- **`balarama.md`** — still single-sourced (Johnson vol. 5).
- The **Digvijaya dating tension** in `shankara.md` — Mādhava's *Śaṅkaravijaya* dated 17th c.; Vidyāraṇya d. 1391.
- **Prakāśātman's *bhāvarūpa* avidyā priority** — Dasgupta and Wikipedia invert the chronology.
- **Which of Hemādri's works quotes Ḍalhaṇa** — `dalhana.md`'s c. 1309 upper bound rests on an inference.
- ***Aṣṭāṅgahṛdaya* Ci. 19.98 in a critical edition** — settles whether Indu preserved or restored the
  Buddhist reading (Jina/Jinasuta vs Śiva/Śivasuta).
- **Grimes, *The Seven Great Untenables*** — six of the seven *saptavidhā anupapatti* heads are still marked
  **unverified** in `ramanuja.md`, on listserv/blog authority.
- **Valerie Stoker**, *Polemics and Patronage in the City of Victory* — Williams is now read; Stoker is not.
- ⚠ **Is Meulenbeld's "D. Ch. Bhattacharyya" the "D. C. Bhattacharya" of `udayana.md` / `gangesha.md`?**
  If one man, the corpus leans on a single philologist across **two unrelated literatures** and should say so.

### First move
**`karma-vargana.md`** — one node, and it removes the corpus's last `low`-confidence entry. Small, closeable,
and visible in `MANIFEST.tsv`.

### Definition of done
Three items closed or explicitly re-classified as `blocked` **with the reason recorded in-file** (§8). ⚠ An
item that cannot be closed should be **moved to `blocked` and struck from this list**, not silently re-carried
— **re-carrying without progress is what produced this backlog.**

---

## How to leave this file for the next session

- **Strike what you closed**, and say in the commit message which item and what closed it.
- **Add nothing here that belongs in a batch queue.** This file is for drifts — problems that worsen on their
  own. New-node ideas go in `progress.md`.
- **Update the measured baselines** at the top of D1 and D3 by re-running the commands, so the next session can
  see movement rather than take a claim on trust. **That is the whole point of having numbers here.**
- If a drift is genuinely resolved, **delete its section** and note the deletion in `progress.md`'s run-log.
