# progress.md — Work Queue & Run Log

> **⚠️ ORIENTATION — read this before acting (kept short on purpose; loaded on every startup — closed run-logs are rotated to `progress-archive.md`).**
> This project has **two parallel structures**, and they are NOT interchangeable:
> 1. **Concepts / batches** → `concepts/*.md`, the graph nodes. Work is queued in "**batches**" here in `progress.md`. Latest: **Batch 51 CLOSED — 417 concepts, 2631 edges** (the second DEPTH batch: 7 nodes, and **15 committed files corrected or amended**) (`check_all.py`: ALL CHECKS PASS).
> 2. **Chapters** → `chapters/*.md`, the human-readable **teaching layer** (prose reading-views, NOT graph nodes; `build_graph.py` ignores them). Indexed in **`chapters/INDEX.md`**. Latest: **Ch 47** (*What a Name Can and Cannot Tell You*), and before it **Ch 46** (*Opening the Book*), and before it Ch 44 and Ch 45 (and **Ch 40 patched in place** — its §2.2 superseded by Ch 42 §2). Previously Ch 40 and Ch 41, written over Batch 47's twelve grammar nodes and **deliberately split across two folders** (`hindu/shastra/` and `hindu/darsana/`) because the tradition itself changed category. **Chapter coverage is 417 / 417 and `KNOWN_UNCOVERED` is EMPTY.** Verify with `python graph/check_chapters.py`, never by hand. → **The next unit of work is a NEW BATCH (52) — see NEXT SESSION and the end of the Batch 51 run-log below.** Write new nodes first, then a chapter over them, then re-derive the roadmap in `chapters/INDEX.md` by the method recorded there. ⚠ Do NOT re-derive coverage by hand-diffing — that is what let a false "340/340" stand for 43 batches. Run **`python graph/check_chapters.py`**: it joins the index to `concepts/` (handling the IAST-vs-filename key split) and exits non-zero on any real gap. NOTE: `hindu/` has a **second level** (`darsana/`, `devotional/`, `scripture/`, `shastra/`) — see `chapters/INDEX.md` header for what goes where.
>
> **"chapter" ≠ "batch."** If the user says "chapter," they mean a file in `chapters/` — open `chapters/INDEX.md` for the next number; do NOT answer with a "Suggested Batch" from this file. (This mistake has recurred across sessions — see `chapter-vs-batch` memory.)

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.


> **🗂  Run-log rotation (token discipline, CLAUDE.md §7/§9).** Closed run-logs older than the current run live in **`progress-archive.md`** (append-only; git is the canonical history). This file keeps only the orientation header, the anchor text, and the **most recent activity** so startup stays cheap. When you finish a batch: append the new run-summary here, then move the *previously* newest run-log block into `progress-archive.md`. Full history: `progress-archive.md` or `git log`.

### Corpus milestone: **417 concepts across 51 batches; 47 chapters.** 2631 edges. 0 orphans. 0 unwritten stubs. **`python graph/check_all.py` → ALL CHECKS PASS**: structural + conformance audits CLEAN, no duplicate/phantom groups, and **chapter coverage 417/417 with an empty `KNOWN_UNCOVERED` table.** Nothing is red and nothing is excused.

---


## ▶ NEXT SESSION — start here

**The repo is fully green.** `python graph/check_all.py` → **ALL CHECKS PASS**; chapter coverage **417/417** with an empty `KNOWN_UNCOVERED` table; 417 nodes, 2631 edges, 0 orphans, 0 dangling stubs, 0 duplicate groups. No outstanding maintenance, no red gate.

⭐⭐⭐ **Batches 50 and 51 were both DEPTH batches and both paid, in the same currency: they corrected far more than they added.** Batch 50 — 3 nodes, 4 committed files corrected. **Batch 51 — 7 nodes, and FIFTEEN committed files corrected or amended.** ⚠ **Neither result was reachable by adding shallow nodes**, and `DRIFT.md` D1 says the shallow route is the one the corpus defaults to. **A third depth batch is the recommendation, and Batch 51's follow-ups 1–3 are already free, located and open-access.**

▶ **Batch 51 finished Batch 50's cut-short queue in full** — all six queued names written (as seven nodes, because `sakatayana` turned out to be a typed split), plus **depth read D-C**, which closes the **Candrācārya follow-up carried since Batch 47**. Nothing from that queue is outstanding.

▶ **The next unit of work: three gaps this batch NAMED and deliberately did not fill** (§8 scope-lock), each argued for by the node that found it:
- **`yapaniya`** — the third Jain sect. The corpus has `digambara` and `svetambara`, and `sakatayana-jain` establishes that **the sect's entire surviving literature is four works by one grammarian**.
- **`aryadeva`** — exposed by `candrakirti` exactly as `candragomin` exposed `candrakirti` one batch earlier.
- **`saranadeva` / `durghata-vrtti`** — Abhyankar's abbreviation list treats it as a standing citation source, and it carries the contemporary reference that dates `maitreya-raksita`.

⚠ **One question for the user, not decidable here (§10 fork) — and it now rests on TWO cases, not one.** Batch 50 finding 7 argued that **§0 should name inflation into modern *politics* alongside modern physics.** Batch 51 finding 8 is a second, independent instance: **Goldman's Foreword to Jaini 1991** names "a theory of ancient India as a place of **social and gender equality**" as an Orientalist / Hindu-Renaissance construction — aimed at the same tradition, from a different specialist, decade and discipline. **That is an edit to the prime directive, so it is left for you.**

⚠ **Read before opening Batch 52.** Batches 44–51 have each falsified something they queued. **Batch 51 falsified four of its own committed files, two of them Buddhist nodes written in Batch 12, and one of its own findings was weakened by the node written immediately after it.** The suggestions below are **leads to test, not facts**.

⚠ **Two standing cautions on source-weighting, the second new in Batch 51:**
1. **(Batch 47)** "read at first hand" and "specialist" are strong marks for what a discipline knows *internally* — vocabulary, manuscript contents, which attributions the tradition itself doubts — **and weak for anything depending on outside scholarship that has moved, chronology above all.**
2. ⭐ **(Batch 51)** **Extend that past chronology: a reference work's statements about *what survives* are exactly as perishable as its statements about dates, because a manuscript can be found.** Abhyankar (1961) calls the *Tantrapradīpa* "available only in a fragmentary state"; it was **printed in full in 2007** from a 220-folio manuscript. ⚠ **"Known through its citers" is not a synonym for "lost."**

⚠ **Abhyankar's dictionary is a session-scratchpad download and does not persist.** Re-downloaded and confirmed working again 2026-09-03. The method: take `server` and `dir` from `https://archive.org/metadata/dictionary-of-sanskrit-grammar-abhyankar`, then request `DictionaryOfSanskritGrammar_abhyankar_djvu.txt` from that host directly. ⚠ **Use that item, NOT `a-dictionary-of-sanskrit-grammar-kv-abhyankar-1961-gos`** — the latter's OCR is unusable. ⚠⚠ **And Batch 51 caught him contradicting himself twice more** (Vyāḍi's date; Maitreya Rakṣita's date). **He is the corpus's best grammar source and he is a 1961 compilation of a tradition's own reports; treat unreconciled notices as the tradition's disagreement, not as his error.**

⭐ **A retrieval method worth reusing, found in Batch 51:** when a publisher blocks an article page (De Gruyter 405, academia.edu 403, institutional IRIS 403), **`https://api.crossref.org/works/<DOI>` will usually still hand over the authors, pagination and the full abstract.** That is how the *Asiatische Studien* paribhāṣā follow-up, dead for two batches, was part-discharged.

---

### ⭐ Trajectory: the four structural drifts are queued **separately**, in [`DRIFT.md`](DRIFT.md)

> **📄 [`DRIFT.md`](DRIFT.md) — read it when you want to work a drift, not a batch.** Four problems that are
> **not defects** (nothing there fails `check_all.py`) but that **get measurably worse every batch**: distance
> from primary sources · one-sided disputes · teaching-layer staleness · the follow-up backlog. They are a
> **different kind of work** from a concept batch — none of them produces new nodes — and they will keep
> degrading quietly if only new-node batches are ever run. **Self-contained: it needs only CLAUDE.md and
> itself.** Not loaded at startup, by design (§7), like `coverage.md` and `progress-archive.md`.
>
> **A detector shipped with it:** `python graph/check_staleness.py` — chapters whose covered concepts were
> edited later. **Advisory, deliberately NOT wired into `check_all.py`** (14 of 34 currently flagged; gating on
> it would turn the repo red for every session). See DRIFT.md D3 for why, and for what the test is *not*.

*(The summary below is kept short on purpose — the working detail is in `DRIFT.md`. Written by the Batch 46 session reviewing the corpus's direction across 44–47. It does not replace the Batch 48 suggestions below; it says what to do **with** them.)*

**The project is on track on every metric it measures, and drifting on the one thing it is *for*.** The evidence for "on track" is strong and is worth naming, because it is the machinery working as designed: **Ch 38 §4.1 (Batch 46) found that Navya-Nyāya's signature device had *grammatical* ancestry and recorded that the corpus had no node for Bhartṛhari or the *Vākyapadīya*. One batch later there are twelve grammar nodes.** The corpus told the next session what to build and it got built. Batch 47 then **qualified Batch 46's own generalisation** about reference sources rather than inheriting it. **Cross-session self-correction is the healthiest signal this project has.**

**The drift, in four measurable forms — each with a baseline and a first move in [`DRIFT.md`](DRIFT.md):**

| | drift | measured now |
|---|---|---|
| **D1** | Distance from **primary sources** is growing, not shrinking | 65 of 387 files carry an "identified but not read" list; ~8 added per batch, 1–2 closed |
| **D2** | The corpus records **one side** of several disputes | `P. V. Sharma` appears 4× in Batch 46, **always in rebuttal**, never read directly; 18 files flag single-sourcing |
| **D3** | The **teaching layer is write-once**, and its staleness was invisible to the gate | **14 of 34 chapters stale** (`python graph/check_staleness.py`) — Ch 11 untouched since 2026-06-23 |
| **D4** | The **follow-up debt** from Batches 43–46 is nearly untouched | ~11 items carried; Batch 46 closed 1 and opened 8 |

**Recommendation for Batch 48: spend it on depth and debt** — add new nodes only where a written chapter already depends on a node that does not exist. Growth resumes at 49. ⚠ But the drifts are **independent of any batch**: `DRIFT.md` is designed to be picked up in its own session, and does not need this file's run-logs.

---

---

## Batch 51 — CLOSED (2026-09-03). **Finished Batch 50's queue and took its unattempted depth read.** 6 queued names → **7 new nodes**; 410 → **417**; 2564 → **2631 edges**. Plus **Ch 47**.

Theme, discovered rather than planned: **every node turned on a name — and in four of seven, the corpus was the party making the mistake.** **`python graph/check_all.py` → ALL CHECKS PASS**; chapter coverage **417/417**, `KNOWN_UNCOVERED` empty, structural + conformance audits **CLEAN**, **0 orphans, 0 dangling stubs, 0 duplicate groups**.

### The depth read — D-C, carried unattempted from Batches 49 and 50, now CLOSED

| id | source | result |
|---|---|---|
| **D-C** | ***Vākyapadīya* kāṇḍa II, 2.480–2.486** — **GRETIL** scholarly e-text + **Ashok Aklujkar, "Interpreting Vākyapadīya 2.486 Historically" (AOS, Toronto, 1978)**, pp. 1–11 | ⭐⭐⭐ **READ. The Candrācārya follow-up carried since Batch 47 is CLOSED — hypothesis confirmed and its arithmetic refuted in the same move.** |
| ⚠ | **Iyer's English kāṇḍa II**, both archive.org identifiers | ⛔ **DEAD — garbled Devanāgarī OCR, zero Latin hits.** `DRIFT.md` D1's rule again; recorded so it is not re-spent |

### The seven nodes

| # | key | status / conf | the one-line finding |
|---|---|---|---|
| 1 | `vyadi` | contested / medium | ⭐⭐ Referenced in 5 files, written in none. **Abhyankar dates him twice, incompatibly** — and Aufrecht and MW already say there are **four Vyāḍis** |
| 2 | `sakatayana` | contested / medium | ⭐⭐⭐ **The eighth collision generator: the PATRONYMIC**, and it is nobody's error |
| 3 | `sakatayana-jain` | contested / medium | ⭐⭐⭐ **The entire surviving literature of the Yāpanīya sect is four works by one grammarian** |
| 4 | `devanandin` | contested / medium | ⭐⭐⭐⭐ **58 files cite Pūjyapāda, 2 cite Devanandin, 0 join them. They are one man.** |
| 5 | `jainendra-vyakarana` | contested / medium | ⭐⭐⭐ **28 of 32 Abhyankar mentions are a Pāṇinian term it REPLACED** — including *vṛddhi*, the term of P. I.1.1 |
| 6 | `candrakirti` | contested / medium | ⭐⭐⭐ **"Prāsaṅgika" is a 12th-c. Tibetan label and the corpus taught it as a 7th-c. Indian school** |
| 7 | `maitreya-raksita` | contested / medium | ⭐⭐⭐ **A religion inferred from a name — and a source out of date rather than wrong** |

### ⭐ The engine findings

**1. ⭐⭐⭐⭐ The corpus's most-cited author had no node because it did not recognise his name.** `grep -l "Pūjyapāda" concepts/*.md | wc -l` → **58**; `Devanandin` → **2**; both → **0**. ⭐ **And the *how* is the finding, not the *what*.** The identity is in the abbreviation list of the dictionary the corpus has read at first hand since Batch 47, and `paribhasha.md` **quoted the sentence containing both names** and tabulated it as "gloss by Abhyankar himself, on maxims in Abhayanandin's *Mahāvṛtti*." ⚠ **Not a reading failure — a compression failure: a census keeps the countable columns and drops the nominal ones.** ⭐⭐ §2 of the charter *prescribes* tabulation for contested material. **This is that instruction's cost, observed once and measurable.**

**2. ⭐⭐⭐ An eighth collision generator, and it is neither accident nor device.** The six from Batch 49 are accidents; Batch 50's seventh (name-as-warrant) is deliberate. **A patronymic is structural** — Monier-Williams glosses *Śākaṭāyana* as a *patronymic*, the *Purāṇa Index* as "a *pravara* of the Bhārgavas." Many bearers is the word working correctly. ⚠⚠ **And it cuts backwards inside the batch**: `vyadi`'s Dākṣāyaṇa argument dates the man by treating a patronymic as individuating. **The second node weakened the first and both stand.**

**3. ⭐⭐⭐ The corpus has been teaching a Tibetan map as an Indian one.** SEP (Hayes): Svātantrika/Prāsaṅgika are "**not used by Indian Mādhyamikas themselves**"; Wikipedia: the categorisation "only arose in **Tibet during the 12th century**." ⚠⚠ **And `santaraksita.md` already said the Svātantrika label was "later Tibetan doxography" — the corpus knew it in one file and not in the other, since Batch 12.** ⭐ Third instance of one pattern (`rasesvara`, `vishishtadvaita`): **a doxographer's category read back as a thing that existed.**

**4. ⭐⭐⭐⭐ The corpus's catalogue of a habit turned out to describe its own principal modern source.** It had recorded Haradatta reading a **doctrine** out of *Sphoṭāyana* and Jinendrabuddhi reading a **biography** out of *Śalātura*, and `paribhasha.md` records that the technique (*jñāpaka*) is named and institutionalised. **The third instance is Abhyankar reading a RELIGION out of "Maitreya Rakṣita"** — hedged twice by him, and repeated unhedged by this corpus. ⚠ **A method that only ever finds the fault in the eleventh century is not a method.**

**5. ⭐⭐⭐ A source out of date rather than wrong — a NEW CATEGORY for Batch 47's standing caution.** Abhyankar (1961): the *Tantrapradīpa* is "available only in a fragmentary state at present." **It was published in full in 2007** (ed. Kanjilal, Kolkata, 267 pp.) from a **220-folio manuscript in the Sāhitya Sabhā collection, Coochbehar**. ⭐ Batch 47 said a specialist is weak wherever outside scholarship has moved, "chronology above all." **Extend it: statements about *what survives* are exactly as perishable as dates, because a manuscript can be found.** ⚠ **"Known through its citers" is not a synonym for "lost"** — Vyāḍi's *Saṅgraha* is gone; this one was in north Bengal the whole time.

**6. ⭐⭐⭐ D-C closed, and the correction is sharper than the confirmation.** The blame-verse and the credit-verse are different verses with different names — **confirmed**. ⚠⚠ **But "five verses later" was arithmetic across two editions' numbering.** On one scale the gap is **two**: GRETIL 2.483/2.485, Aklujkar 2.484/2.486, Abhyankar's II.489 a third scale. ⭐ **And the text supplies the reason the corpus could only guess at**: *śuṣka-tarkānusāribhiḥ* against *bhāṣya-bījānusāribhiḥ* — **a deliberate antithesis on matched compounds, not a stray name.** ⚠ **Cost: Aklujkar holds the ten epilogue verses to be a pupil's, not Bhartṛhari's.**

**7. ⭐⭐ A Batch-50 finding QUALIFIED, not confirmed.** T4 held that the metalanguage crosses system boundaries. **The Jainendra keeps the whole paribhāṣā machinery (108 maxims) and discards the vocabulary.** ⭐ **What crosses is the *technique*, not the *terminology* — and they are separable because one system separated them.** ⚠ The sectarian reading of the substitution is **flagged and refused**: no source gives a motive, and brevity is an ordinary alternative.

**8. ⚠⚠ Batch 50's §0 charter question now has TWO cases.** Finding 7 of that batch (inflation into modern **politics**) reappears here from a different specialist, decade and discipline, aimed at the same tradition: **Goldman's Foreword to Jaini 1991** names "a theory of ancient India as a place of **social and gender equality**" as an Orientalist / Hindu-Renaissance construction — precisely the reading `sakatayana-jain` invites. **Still a §10 fork for the user; it now rests on two independent instances rather than one.**

**9. ⭐⭐ Two claims the batch went looking for and REFUSED.** (a) That the MMK's Sanskrit survives only inside the *Prasannapadā* — ⚠ **unverified**; SEP confirms only that the commentary survives in Sanskrit, and Wikipedia's MMK article, **asked directly**, does not address the root text. (b) The wisdomlib "Vyādi = Bhalipā" entry — **a dental-*d* word folded into a retroflex-*ḍ* lemma by a search index.** ⭐ Both are collisions **generated by modern retrieval rather than by ancient scribes.**

**10. ⭐ The wisdomlib = Abhyankar trap is now PROVEN, not inferred.** Batch 50 deduced it from a collision. The site **credits him by name** — "Wikisource: *A dictionary of Sanskrit grammar* (K. V. Abhyankar)" — and its first sentence is verbatim the scan. **Anything agreeing with Abhyankar from that source is not a second signal.**

### ⚠ Sources caught being wrong — and FOUR of eight are us

| # | source | failure |
|---|---|---|
| 1 | **Abhyankar** | dates **Vyāḍi** twice, incompatibly (contemporary of Pāṇini / after Kātyāyana, before Patañjali) |
| 2 | **Abhyankar** | dates **Maitreya Rakṣita** twice (beginning / middle of the 12th c.) |
| 3 | **Abhyankar** | ⭐ **out of date rather than wrong** — the "fragmentary" *Tantrapradīpa*, printed in full in 2007 |
| 4 | **Wikipedia, "Chandrakirti"** | c. 600–650 in the lead, c. 600–670 in the infobox |
| 5 | ⚠ **this corpus** | `bodhisattva.md` gave the ***Bodhicaryāvatāra* to Candrakīrti**; it is **Śāntideva's**, and `bodhicitta.md` has it right five times |
| 6 | ⚠⚠ **this corpus** | the same sentence claimed "`madhyamaka.md` notes" it. **It does not mention the work at all.** ⭐ **A §4-signal-4 corpus-internal check done from memory — wrong author and false citation in one clause. This is what §8's "never recall a linked concept from memory" is for.** |
| 7 | ⚠ **this corpus** | `paribhasha.md`'s census dropped the names that would have identified Devanandin |
| 8 | ⚠ **this corpus** | `madhyamaka.md` / `prasanga-nagarjuna.md` taught 12th-c. Tibetan labels as 7th-c. Indian schools |

### What the batch did to its own corpus

**Fifteen committed files corrected or amended**: `candra-vyakarana` · `mahabhashya` · `punyaraja` · `vakyapadiya` (the D-C read) · `paribhasha` (census row restored; the *Asiatische Studien* follow-up part-discharged) · `bhartrhari` · `tattvartha-sutra` · `jinendrabuddhi` (collision #17 + the 2007 edition) · `madhyamaka` · `prasanga-nagarjuna` · `mulamadhyamakakarika` · `bodhisattva` · `haradatta` · `candragomin` · `pramana-samuccaya`.

⭐ **One follow-up part-discharged by a method worth reusing**: the *Asiatische Studien* paribhāṣā article returned **405** for two batches. **Crossref's API handed over the authors, pagination and the full abstract** — Candotti & Pontillo, 72.2 (2018), 515–566 — and the abstract alone puts Vyāḍi's collection **after** Patañjali, against Abhyankar. **When a publisher blocks the page, Crossref usually still has the metadata.**

⭐ **Three edges drafted and struck rather than forced** (`vyadi` → `rasesvara`; the four-Vyāḍis conflation; a mistyped dating edge), and **two inbound edges written from their own nodes' vantage rather than mirrored** to clear the orphan check.

### Follow-ups carried into Batch 52

1. ⭐⭐⭐ **Jaini 1991 Chapter II** — a complete published English translation of the *Strīnirvāṇaprakaraṇa* with autocommentary, **open access and already downloaded**; this batch used its notes and not its translation. **The cheapest primary-source read the corpus currently holds.**
2. ⭐⭐ **Kanjilal's 2007 *Tantrapradīpa*** — a text the corpus's own authority called fragmentary, printed in full, with an English component.
3. ⭐⭐ **The mechanically checkable question**: does the *Sarvārthasiddhi* use **Jainendra** technical terms where a Pāṇinian would use Pāṇini's? One man, two books.
4. ⭐ **La Vallée Poussin 1903–13** — settles the MMK Sanskrit-survival question **and** the verse-numbering problem for the *Prasannapadā*.
5. **Aklujkar pp. 12–21 and his Parts 2–3**; **Rau's critical edition** (the only thing that fixes VP numbering).
6. **Abhyankar's *Paribhāṣāsaṃgraha*** — it *prints* Vyāḍi's *Paribhāṣāsūcana*; wanted by `vyadi` and `paribhasha` both.
7. **Candotti & Pontillo in full** (De Gruyter 405 / academia.edu 403 / Pisa IRIS 403 — all dead).
8. ***Nirukta* I.8 and I.12–13 in Sarup** — the two Śākaṭāyana/Gārgya disputes, in a translation the corpus already has a route to.
9. ⭐ **Aufrecht's *Catalogus Catalogorum* at first hand** — the source of the four-Vyāḍis split.
10. ⚠ **A lead not pursued (§8 scope-lock):** Jaini describes the ***nokarma-vargaṇā***, "the most auspicious kind of karmic matter… which ordinarily accounts for the involuntary biological functions suitable to the nature of each species" — ⭐ **directly relevant to `karma-vargana.md`, from a specialist source that node has never seen.**

**Carried from earlier batches, still open:** Matilal 1968 Parts II–III (in hand, still unused); Phillips's *Tattvacintāmaṇi*; Potter; Neevel 1977; the *Ratnaprabhā* and *Siddhayoga*; **P. V. Sharma**; Ingalls 1951; Nitti-Dolci; Ollett chs. 1–4 and 7; Ghosh's *Prākṛtakalpataru*; Eggeling 1876; Olivelle (paywalled); the *Nāṭyaśāstra* (still no node); the Dravidian half of Batch 49 follow-up #12; the D. Ch./D. C. Bhattacharyya question; the Digvijaya dating in `shankara.md`; the 42-vs-93 *nāma*-karma discrepancy; `dhatu.md`'s three-vs-four dispute; `balarama.md` single-sourced; Valerie Stoker.

### Suggested Batch 52 (names only — **leads to test, not facts**)

- ⭐⭐⭐ **Three gaps this batch NAMED and did not fill**, each argued for by its own node: **`yapaniya`** (the third Jain sect — the corpus has `digambara` and `svetambara`, and the sect's entire surviving literature is now a node) · **`aryadeva`** (exposed by `candrakirti` exactly as `candragomin` exposed `candrakirti`) · **`saranadeva` / `durghata-vrtti`** (Abhyankar treats it as a standing citation source, and it dates `maitreya-raksita`).
- ⭐⭐ **Another DEPTH batch.** Batches 50 and 51 both spent their value on reading rather than adding, and both corrected more committed files than they created nodes (4 and 15). Follow-ups 1–3 above are **free, located, and each closes a named test at the primary level.**
- ⭐ **Opened by this batch:** `abhayanandin` · `sarvarthasiddhi` (⚠ or keep it inside `devanandin`) · `prabhacandra` (⚠ **two of them — the Śākaṭāyana commentator and the Digambara logician who quotes Śākaṭāyana; a live collision**) · `natyashastra` (still a real hole) · `maharastri` · `rudrata` · `amarakosha` · `durgacarya` · `kavyalankara-bhamaha`.
- **Still open from 46–50:** `madhava-nidana` / `madhavakara` · `vijayaraksita` · `srikanthadatta` · `annambhatta` / `tarkasangraha` · `jagadisha-tarkalankara` · `vardhamana-upadhyaya` · `sridhara` · `jayanta-bhatta` · `parasara-bhatta` · `yadavaprakasha` · `vaidyanatha-payagunde` · `varadaraja` · `sesha-krsna` · `bhoja` / `sarasvatikanthabharana`.

---

