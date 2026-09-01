# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 45 CLOSED — 362 concepts, 2198 edges** (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 35, 36 and 37**, written in one pass over the 21 uncovered nodes of Batches 44+45, plus `dhamma` folded into **Ch 12 §3.0**. **Chapter coverage is 362 / 362 and `KNOWN_UNCOVERED` is now EMPTY** — the first time the corpus has full coverage with no recorded excuses. Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (46) — see the end of the Batch 45 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false “340/340” stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **375 concepts across 46 batches; 39 chapters.** 2339 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 375/375 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---

## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` passes all three checks; chapter coverage is **375/375**
with no recorded excuses. There is no outstanding maintenance and no red gate. So the next unit of work is a
**new concept batch (47)** — see the suggestions at the end of the Batch 46 run-log below.

⚠ **Read this before opening Batch 47.** Batches 44, 45 and 46 each falsified their own queue premises
(`nrisimhasrama`, `candrata`, `vimuktatman`). The suggestions below are **leads, not facts** — every one is a
claim to *test*, and a batch that never falsifies its own queue is not checking it. Batch 46 also falsified
**three claims already committed to this corpus**; that is the standard to hold.

⚠ **Meulenbeld is local no longer** — the HIML volumes go to a session scratchpad and do not persist.
Re-download before any Āyurveda work. The method is recorded in `concepts/candrata.md` under **Note on
retrieval** and in `concepts/tisata.md`: take `server` and `dir` from `https://archive.org/metadata/Meulenbeld-HIML`,
then request from that host directly with `%20` for spaces. **Confirmed working twice** (Batches 45 and 46);
only the `HIML 1A ` filename actually needs the `%20`.

⚠ **Two published translations are already within reach and unused** — see follow-ups 1 and 2 below. Follow-up 2
needs no retrieval at all.

---

## Batch 46 — CLOSED (2026-09-01). 13/13 concepts; 362 → 375 nodes; 2198 → 2339 edges. Plus Ch 38 and Ch 39.

Theme: **close the Navya-Nyāya hole.** Every concept passed the §8 dedup gate against the live filesystem and was committed individually with its findings in the message. `git log` is the detail; this is the short form. **`python graph/check_all.py` → ALL CHECKS PASS**, chapter coverage **375/375**.

### The thirteen

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `navya-nyaya` | **contested** / medium | **A school with three different beginnings** — Gaṅgeśa's book (c. 1325), Udayana (c. 1025–1100), or the 11th–12th-c. Nyāya/Vaiśeṣika merger. They answer different questions; two of them converge on the 11th c. independently. |
| 2 | `gangesha` | **contested** / medium | **A date that drifted one way for a century**, with every stage still in circulation: one source at four ages, mistaken for corroboration. |
| 3 | `tattvacintamani` | converged / medium | **The object of study migrates upward** — 30 commentaries in 3 tiers, and by the 17th c. the live text is a commentary on a commentary. |
| 4 | `avacchedaka` | converged / **high** | The limitor, from **Matilal read at first hand**. The corpus's first high-confidence Navya-Nyāya node. Its ancestry is **grammatical, not logical**. |
| 5 | `abhava` | **contested** / medium | ⭐ **The seventh category was retrofitted** — and by Udayana, in the *Kiraṇāvalī*. |
| 6 | `raghunatha-siromani` | **contested** / medium | ⭐ **The school's best logician rejected the school's ontology** — including atoms. |
| 7 | `gadadhara` | **contested** / medium | Placing him **falsifies a dating synchronism Batch 45 adopted**. |
| 8 | `jayatirtha` | **contested** / medium | A Dvaitin **defines nonexistence in the Naiyāyika's own words**. |
| 9 | `vedanta-desika` | **contested** / medium | **A library of lost books**, and a school he partly authored. |
| 10 | `vimuktatman` | **contested** / medium | **The queued test was run and the claim failed** — on every available dating. |
| 11 | `tisata` | converged / medium | ⭐ **The text left a blank and the tradition filled it with a celebrity.** |
| 12 | `niscalakara` | **contested** / medium | **A commentary that is a bibliography** — ~50 of Cakrapāṇi's sources, many lost. |
| 13 | `vrnda` | **contested** / medium | **The one external anchor evaporates** on identification — and a proposed split that fails. |

*(#13 `abhava` was **added mid-batch**, on the Batch 45 precedent, when `avacchedaka` opened a `formalizes:` edge to it and it turned out to be the school's own seventh category with a Harvard monograph devoted to it.)*

### The engine findings

⭐ **Two major sources obtained and read at first hand, both new to the corpus:**
1. **B. K. Matilal, *The Navya-Nyāya Doctrine of Negation* (Harvard UP, 1968)** — from a full public scan. **Ingalls's Editor's Introduction came with it**, so Ingalls is now in the corpus at first hand rather than as a reported quotation. ⚠ **Its Parts II–III contain English translations of Gaṅgeśa's *Abhāva-vāda* and Raghunātha's *Nañvāda* with the Sanskrit appended — sampled, not worked through.** The corpus has a published scholarly translation of part of its primary text in hand and has not used it.
2. **Michael Williams (2020), *J. Indian Philos.* 49.2, open access** — **closes Batch 45's follow-up 3** naming him as the non-partisan corrective to `vyasatirtha.md`'s reliance on a Dvaita partisan.

Plus: **SEP's "Gaṅgeśa"** entry; **Elisa Freschi's IEP "Veṅkaṭanātha"**; and **Meulenbeld's HIML re-downloaded** by the method `candrata.md` recorded — **that method is now confirmed twice.**

⚠ **An independence correction that applies to the whole batch.** The article cited throughout as *"Ganeri, Navya-Nyāya"* (the Columbia/Pollock PDF) **is** the SEP entry *"Analytic Philosophy in Early Modern India."* **One source, two addresses; never count it twice.** It does **not** affect SEP's *"Gaṅgeśa"*, a different entry by a different author. Logged in `gadadhara.md`.

### What the batch falsified — in its own corpus

**A batch that never falsifies its own queue or its own corpus is not checking either.** This one did both, four times:

1. **`anandabodha.md`** — its charge that "Navya-nyāya style" was *anachronistic* does not survive: **the charge was itself resting on an unexamined periodisation.** Amended; the phrase is still declined, but as unargued rather than impossible.
2. **`madhusudana-sarasvati.md`** — Rajagopalan's **third** dating synchronism ("Gadādhara was his contemporary") is struck out: Gadādhara wrote c. 1640–60, ~140 years later, and the likely source is a **panegyric verse**. ⚠ The other three legs stand, and the inscription-anchored Appayya synchronism is untouched — **the conclusion survives, one of its four legs does not.** An uncomfortable consequence is recorded and **left open**.
3. **`vimuktatman`** — the queued discipleship claim fails on **every** combination of available datings. Stated as a **negative** result.
4. **`vaiseshika-sutra.md` / `prashastapada.md` / `kanada.md` / `paramanu-vaisheshika.md` / `jati.md`** — not falsified but **materially qualified**: the seventh category is a retrofit, and **Vaiśeṣika atomism was rejected by Raghunātha**, which gives `kanada.md`'s prime-directive warning a *historical* argument beside its conceptual one.

### What the batch confirmed from outside

- **`nathamuni.md`'s** 128/120/120 lifespan finding — the corpus's own arithmetic — is now **sourced**: Freschi, citing **Neevel 1977**, that the lifespans "have been **prolonged in order to connect them with each other**."
- **`jejjata.md`'s** derived rule that *a disputed date cannot anchor another date* — found in **Meulenbeld's own words** in a different section.
- **`vacaspati-mishra.md`'s** I/II collision — confirmed by a **second, unrelated route** (a commentary census).
- **`candrata.md`'s** Vāgbhaṭa-colophon finding — its **other half** located, one generation up.

### The recurring finding, and the chapter built on it

**Five name-collisions surfaced** (Vācaspati Miśra I/II; two Harirāma Tarkavāgīśas; two Vyāsatīrthas; the open Jñānottama question; and the **rejected** Vṛnda split) — and **three self-contradicting encyclopedia sources** (Gaṅgeśa's date across three Wikipedia strata; Jayatīrtha's "direct disciple"; Vimuktātman "c. 1200" in prose and "10th century" in the same article's own chronology).

**The generalisation, and it is the most practically useful thing the batch produced:** these sources are not unreliable in detail — **they are unreliable as a *set of witnesses*, because they do not check themselves across articles. Sampling several of them is not corroboration.**

⚠ **And the counterweight was deliberately built in.** Ch 39 §7 is the case where a distinguished scholar proposed a **split** (two Vṛndas) and Meulenbeld declined it. **The pattern is a reason to check, not a licence to split.**

### What the batch did to nodes it did not create

Twelve existing files changed: `anandabodha` · `udayana` · `vyapti` · `vacaspati-mishra` · `vaiseshika-sutra` · `prashastapada` · `kanada` · `paramanu-vaisheshika` · `jati` · `madhusudana-sarasvati` · `vyasatirtha` · `nathamuni` · `candrata` · `advaita-vedanta` · `vishishtadvaita`.

### The teaching layer

| ch | title | folder | nodes |
|---|---|---|---|
| **38** | The New Logic: What Navya-Nyāya Was Actually For | `hindu/darsana/` | 7 |
| **39** | Filling in the Blanks: How the Record Gets Made | `cross-tradition/` | 6 |

Ch 38 §7 is the chapter the batch most needed to write: **how to compare Navya-Nyāya with modern logic without inflating it.** Its result is a genuine convergence — **Matilal** (limitorship "definable in terms of the 'primitive' occurrence relation") and **Ganeri** (the *vyāpti* definitions analysing generality "only in terms of … co-location and absence"), independently, on different problems. **The school was not reaching for ∀ and missing; it was asking what ∀ is made of, in a metaphysics where the answer had to be made of things.** And the limit is Ingalls's own: "a hierarchy of abstractions rather than a hierarchy of classes," with "ultimate incompatibilities."

Ch 39 generalises Ch 35 from Āyurveda to four traditions: **six mechanisms by which a hole in the record gets filled.**

### ⚠ A convention settled mid-batch, and worth keeping

The `build_graph` audit caught **three** same-type bidirectional `expressed-by` edges that this batch introduced. Resolved by adopting one rule everywhere: **`expressed-by` points person → doctrine/work, never doctrine → person** — the idiom already committed in `udayana.md`. **Recommend adding this line to CLAUDE.md §5** as a clarification of the existing storage rule; **not done unilaterally, because §10 reserves charter edits.**

### Follow-ups carried into Batch 47

**New, and top of the list:**

1. ⭐ **S. Phillips, *Jewel of Reflection on the Truth about Epistemology*, 3 vols, Bloomsbury, 2020** — a **complete English translation of the *Tattvacintāmaṇi***. The single highest-value unread item in the corpus; would move four nodes from second-hand to sourced.
2. ⭐ **Matilal 1968 Parts II–III, already in hand** — the *Abhāva-vāda* and *Nañvāda* translations. **The cheapest high-value item in the corpus: no retrieval required.**
3. **Karl H. Potter, *Padārthatattvanirūpaṇa*, text and translation, Harvard-Yenching 17, 1957** — would settle what Raghunātha's "denies atoms" amounts to, and the number contradiction.
4. **Neevel 1977, pp. 14–16** — the argument that the ācāryas' lifespans were stretched. Wanted by two nodes.
5. **The *Ratnaprabhā*** and the ***Siddhayoga* with Śrīkaṇṭhadatta's *Vyākhyākusumāvalī*** — the corpus depends on these from **five** files and has never seen a line of either.
6. **P. V. Sharma** — met **four times this batch and always in rebuttal**. A corpus that only ever records one side of a dispute is not neutral.
7. **Ingalls, *Materials for the Study of Navya-Nyāya Logic* (1951)** — the source of the Frege comparison.
8. ⚠ **Is Meulenbeld's "D. Ch. Bhattacharyya" the "D. C. Bhattacharya" of `udayana.md` / `gangesha.md`?** If one man, the corpus leans on one philologist in two unrelated literatures.

**Carried from Batch 43/44/45, still open:** the Digvijaya dating tension in `shankara.md`; `karma-vargana.md` still the only `low`-confidence node; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; Prakāśātman's *bhāvarūpa* priority; which of Hemādri's works quotes Ḍalhaṇa; *Aṣṭāṅgahṛdaya* Ci. 19.98 in a critical edition; Grimes, *The Seven Great Untenables*; **Valerie Stoker** (Williams now read, Stoker not); Lance Nelson's *Bhaktirasāyana* ch. 1; a critical *Lakṣaṇāvalī*. **⚠ Ch 11 is now seven chapters out of date.**

### Suggested Batch 47 (names only — **leads to test, not facts**)

- **Structural holes this batch exposed:** **`bhartrhari`** and **`vakyapadiya`** — Ch 38 §4.1 shows Navya-Nyāya's signature device has **grammatical** ancestry and the corpus has **no node for the Sanskrit grammatical tradition at all**; **`madhava-nidana`** / **`madhavakara`** — the *Siddhayoga* is organised on it, Tīsaṭa is partly dated by not following it, and it has no node; **`vijayaraksita`** and **`srikanthadatta`** — both are hinges in Ch 39 and neither exists.
- **Opened by Batch 46:** `annambhatta` / `tarkasangraha` (the manual the school needed); `jagadisha-tarkalankara`; `vardhamana-upadhyaya`; `sridhara` / `nyayakandali`; `jayanta-bhatta` / `nyayamanjari`; `parasara-bhatta`; `yadavaprakasha`.
- **Maintenance:** carried follow-up — **Ch 11 predates the entire Advaita-lineage cluster and now also Chs 36–39.**

---

## ▶ Batch 47 — OPEN (2026-09-01). Theme: **the śāstra the corpus has been leaning on without a node — Vyākaraṇa.**

**Why this batch.** A grep of `concepts/` finds **20 files** that invoke "grammar / grammatical / Pāṇini / vyākaraṇa"
— and there is **not one node for the Sanskrit grammatical tradition.** Three specific debts:
- **Ch 38 §4.1** derives Navya-Nyāya's signature device (`avacchedaka`) from **grammatical** ancestry, citing a
  tradition the graph cannot show.
- **`patanjali.md` states the debt in its own prose:** *"No node exists for the grammarian; the caution is
  recorded here in prose since a typed edge needs a target."* This batch supplies the target.
- `sabda-pramana`, `apoha`, `mimamsa-pramana` all presuppose a theory of how words mean, sourced to no node.

**⚠ The queue is a set of leads to test, not facts.** Named tests carried in:
- **T1** — Is the Yoga-sūtra Patañjali the *Mahābhāṣya* Patañjali? `patanjali.md` says no (Renou; Bhojadeva ~10th c.).
  Test it against grammatical scholarship, not Yoga scholarship. A tradition-split node is only justified if it fails.
- **T2** — Is *sphoṭa* Bhartṛhari's invention? The corpus's prior is "yes"; the *Mahābhāṣya* may already have the word.
- **T3** — Does the `avacchedaka`-from-grammar claim in Ch 38 survive contact with an actual grammar source?
- **T4** — Is the "**munitraya**" (three sages: Pāṇini/Kātyāyana/Patañjali) a scholarly periodisation or a
  traditional one the corpus would be repeating uncritically?

| # | key | state | note |
|---|---|---|---|
| 1 | `vyakarana` | pending | the discipline; vedāṅga, not a darśana — check that claim |
| 2 | `panini` | pending | |
| 3 | `astadhyayi` | pending | |
| 4 | `katyayana` | pending | the vārttikakāra |
| 5 | `patanjali-grammarian` | pending | tradition-split from `patanjali` **only if T1 holds** |
| 6 | `mahabhashya` | pending | |
| 7 | `bhartrhari` | pending | |
| 8 | `vakyapadiya` | pending | |
| 9 | `sphota` | pending | T2 |
| 10 | `shabdabrahman` | pending | |
| 11 | `karaka` | pending | case-role theory — the likely real ancestor of relational analysis (T3) |

Additions mid-batch are allowed on the Batch 45/46 precedent when a node opens a required edge target.
