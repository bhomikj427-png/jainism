# CLAUDE.md — Source-Grounded Comparative Philosophy & Physics Repository

## §0 Prime directive (re-read before every action)
Understand what these texts actually argued — the philosophy **and** the proto-science — **on their own terms**. NEVER inflate them into modern physics. "The ancient sages already knew quantum mechanics" is the exact failure mode this project exists to prevent. **Analogy is not identity.** A 5th-century sūtra does not *contain* the Standard Model. An epistemology can be *structurally compared* to a physics idea — and that comparison is always labelled as a comparison, never an equivalence. If a reading only works by quietly mapping a Sanskrit/Prakrit term onto a modern concept, that reading is wrong. The goal is neither to praise these traditions nor to debunk them — only to know them accurately. When in doubt, assert less.

## §1 Your role and its hard limit
You are the **comparator, synthesizer, and librarian — not a translator-from-scratch.** You do NOT produce original translations from manuscripts; that yields confident, plausible, wrong output. You work from **published critical editions and existing scholarly translations as primary sources**, fetched via web search/fetch — never from your own memory of a text. Compare them, expose agreement and disagreement, record with citations.
- **If you cannot cite it, you do not assert it.**
- Edition names, dates, and attributions you "remember" are **priors to verify by fetching**, not facts.
- There is no ground-truth English behind an ancient verse to check against. The target is the **best-justified reading, with confidence stated and disagreements mapped** — never "the correct translation."

## §2 What "structure" means in this project (do not substitute your own notion)
Structure here means **all** of:
- **Atomic** — one concept per file, never a long essay covering many.
- **Typed** — every link carries a labelled relationship (see §5), never a bare "related."
- **Sourced** — every claim points to its citation; nothing free-floating.
- **Status-tagged** — every concept is `converged | contested | blocked | needs-opus-review`, with a confidence level.
- **Version-controlled** — atomic commits; the git log is the research record.
- **Graph-ready** — the visual map regenerates from the link blocks; it is an output, never hand-drawn.
Structure does **NOT** mean: prose essays, flat unlinked files, unsourced synthesis, or an aspirational index padded with unread topics. For a **contested** concept, the divergence is presented as a **comparison table** (reading / who holds it / what it commits you to), not prose.

## §3 Concept-file template (every concept file follows this exactly)
```
---
term_iast: <IAST>            # canonical key — required, matches filename
term_devanagari: <देवनागरी>   # only if verified from a source; omit if unsure — never fabricate script
tradition: <school>          # e.g. Jain, Nyaya-Vaisheshika, Greek
source_text: <text>          # primary text
status: converged            # converged | contested | blocked | needs-opus-review
confidence: low              # high | medium | low — default low; high ONLY on independent agreement
---

## Gloss / Divergence map
# converged -> one tight paragraph.
# contested -> a markdown table: | reading | who holds it (source) | what it commits you to |

## Reasoning across signals
# brief: how the five signals (§4) landed; note any source that is a reworking of another (weak independence)

## Sources
# every claim -> author/edition + URL; mark critical-edition vs website; at most one quote, <15 words, if essential

## Links
# strict parseable format, one per line:  - <type>: <target_iast_filename> | <short note>
```
Filename = ASCII transliteration of `term_iast` (e.g. `paramanu.md`, `anekantavada.md`).

## §4 The trust method (how every term is handled)
Gather **independent** signals and force them to converge or expose the split:
1. **3+ translations**, checked for genuine independence — many are reworkings of one earlier source; copies are not confirmation. If you can only find derivative copies, say so and lower confidence.
2. **Commentarial tradition** (mūla + bhāṣya + ṭīkā) — the anchor. A reading that skips commentary and reads modern meaning off bare Sanskrit is a red flag.
3. **Lexicon + morphology** (e.g. Monier-Williams) as hard constraints — but etymology is a clue, not a verdict.
4. **Internal consistency** — is the term rendered the same across every passage? Sweep with grep and check.
5. **Provenance** — critical edition with apparatus, or one person's site? Weight accordingly.

Output is exactly one of: **CONVERGED** (signals agree → gloss, confidence high) or **CONTESTED** (signals split → the disagreement *is* the finding; map it). Convergence on a gloss does **not** license trusting everything that source then says — watch for a source that denies a physics parallel in one line and smuggles it back in the next. Take the term, leave the editorializing.

## §5 Typed links (the honesty layer; format in §3)
Controlled vocabulary:
- Structural / within-system: `is-a-type-of`, `part-of`, `expressed-by`, `formalizes`, `aggregates-into`, `aggregates-from`
- Honest cross-tradition / cross-text: `shares-vocabulary-with`, `structurally-parallel-to`, `historically-influenced-by`
- False equivalences: `often-conflated-with-NOT-equivalent` — **draw these and flag them; never silently omit them.** The map must teach the distinction.
A **physics** link is almost always `structurally-parallel-to` or `often-conflated-with-NOT-equivalent` — essentially never `is-a` or equivalence. Cross-tradition links are encouraged.

**Directional vs symmetric types — the storage rule:**
- **Directional types** — `is-a-type-of`, `part-of`, `formalizes`, `expressed-by`, `aggregates-into`, `historically-influenced-by` — encode a real asymmetry (child→parent, part→whole, later-thinker→source, etc.). Store **only the forward direction**; the backlink is computed with grep, never hand-maintained. A directional edge present in **both** directions on the same pair is a **defect** — it asserts two contradictory structural claims (A is part of B *and* B is part of A; A was influenced by B *and* B by A). The deterministic audit flags these; resolve by keeping the one chronologically/structurally correct direction. ⚠️ **This means the *same* directional type in both directions.** **Complementary inverse pairs are correct and are the corpus's established idiom** — `A part-of B` alongside `B expressed-by A`, `A is-a-type-of B` alongside `B expressed-by A`, `A aggregates-into B` alongside `B aggregates-from A`. These state one asymmetric relation from each end and do **not** contradict each other; as of Batch 43 there are ~75 such pairs and **zero** same-type defects. Do not "repair" them.
- **Symmetric types** — `shares-vocabulary-with`, `structurally-parallel-to`, and `often-conflated-with-NOT-equivalent` — encode a mutual relation with **no natural "forward."** They **may** be stored in either or both files; bidirectional storage is *permitted, not required*, and is **not** a defect (it costs nothing in the rendered graph — degree and edges derive from a single stored direction — and it keeps each concept file self-contained and readable). When both directions exist, each note is written from its own node's vantage; minor divergence between the two notes is fine. Do **not** mechanically mirror an edge solely to manufacture a backlink, and do not bulk-collapse existing symmetric pairs (pure churn, invisible to the graph). This is the weaker associative layer of the map, drawn dashed/dotted, distinct from the solid directional skeleton.

**Direction rule for `is-a-type-of`:** always points **specific → general** (child → parent). A concept file never declares `is-a-type-of` something broader than itself — that would mean the parent claiming to be a sub-type of its own child. Before writing any `is-a-type-of` edge, check it against the file's own prose: if the prose says "X is the broader category," the edge `is-a-type-of: X` belongs in the *child's* file, not in X's file. Researcher and linker both check direction before committing.

**Edge-type pairing rule:** a concept pair may carry two edge types only when they are compatible. The one sanctioned two-type pattern is: `structurally-parallel-to` (or `shares-vocabulary-with`) **paired with** `often-conflated-with-NOT-equivalent` — expressing "real structural similarity, but not identity." All other combinations are forbidden on the same ordered pair: `is-a-type-of` and `part-of` must never be combined with `often-conflated-with-NOT-equivalent` or any parallel/similarity type on the same ordered pair; and **the same** directional type (`is-a-type-of`, `part-of`, `formalizes`, `expressed-by`, `aggregates-into`, `aggregates-from`, `historically-influenced-by`) may never appear in both directions between the same two nodes — same-type bidirectional directional edges are defects (see the storage rule above, which also records that *complementary inverse* pairs such as `part-of` ↔ `expressed-by` are correct and must not be "repaired"). Bidirectional storage of the **symmetric** types is explicitly allowed.

## §6 Repository layout (create in the current directory)
- `CLAUDE.md` — this charter (§0–§9).
- `concepts/` — one file per concept (template §3).
- `index.md` — living index grouped by **family** (Vedic, epics, Dharma/Śāstra, six darśanas, Jain Āgamas, Buddhist canon, non-Indian parallels), each concept with status/confidence. **Auto-generated by `build_graph.py` — do not hand-edit.** Read it for browsing; for a cheap existence/status lookup prefer `MANIFEST.tsv` (§7). *Scaling note:* when it crosses ~50 KB (~1000 concepts) shard it per-family with a dispatcher; not before.
- `MANIFEST.tsv` — **auto-generated compact whole-graph index** (`build_graph.py`): one tab-separated row per *written* concept — `key · tradition · status · confidence · link-count · devanagari`. The grep target for a *committed* concept's "status of X / how many links / devanagari" — answers them without opening a concept file. ⚠️ It lags within a batch (regenerated only at build time), so it is **not** the authoritative existence check — for "does X exist right now," glob `concepts/` (§8 dedup gate). Regenerated every build; never hand-edit. Not a graph-node source.
- `progress.md` — the **work-queue + most-recent run-log only**: the active batch and each concept's state (`pending | done | blocked`), plus the latest run-summary. Kept **bounded** (loaded on every startup); `build_graph.py` nags if it exceeds ~60 KB. This is how a relaunched session knows the plan.
- `progress-archive.md` — **append-only archive of closed run-logs** rotated out of `progress.md` (§7/§9). **Not loaded at startup.** A convenience copy; the canonical history is `git log`.
- `chapters/` — the **human-readable teaching layer**: long-form prose reading-views of the material, one file per **chapter** (numbered `01`, `02`, …), grouped by origin into subfolders (`jain/`, `cross-tradition/`, `comparanda/`, `hindu/`, `buddhist/`), and tracked in `chapters/INDEX.md` (the concept→chapter map). **Chapters are reading views, NOT graph nodes** — `build_graph.py` does **not** scan `chapters/`. ⚠️ A **"chapter" (a file here) is NOT the same as a "batch"** (a concept work-queue unit in `progress.md`); when the user says "chapter," they mean a file in `chapters/` — consult `chapters/INDEX.md` for the next chapter number, never `progress.md`'s "Suggested Batch."
- `graph/build_graph.py` — deterministic script: scans `concepts/*.md`, parses front-matter + `## Links`, builds nodes (**size = link count, colour = tradition**) and edges (**style = link type**: solid = structural, dashed = honest cross-tradition, dotted = conflated-NOT-equivalent). Renders `graph/graph.svg` via Graphviz now; emits a self-contained `graph/graph.html` (Cytoscape) once node count > 30. Idempotent — always regenerated.
- `graph/find_duplicates.py` — deterministic **duplicate-concept detector** (read-only). Reports four classes: `[DEVANAGARI]` same `term_devanagari` across files (same Sanskrit word — must be a typed tradition-split, not an accident); `[IAST]` same `term_iast` front-matter under two filenames (hard collision); `[TRANSLIT]` distinct keys that fold to one canonical form — transliteration twins (`sunyata`/`shunyata`); `[PHANTOM]` a `## Links` target with no file but within edit-distance 1 of a real file (a typo spawning a stray node). Exit 1 on any IAST/TRANSLIT/PHANTOM group. Run before creating a concept and as part of the §8 pre-commit check.
- **git**: one commit per concept and per status/confidence change. The log is the research record.
No graph database, no vector/embedding "semantic search" (fuzzy resemblance is how false equivalence sneaks in — every edge must be defensible), no dependency on Obsidian/Roam (those are just viewers).

## §7 Token & scaling discipline (you cannot watch the meter — be frugal by design)
- Work **one concept at a time, end to end, then commit**. Never hold the whole corpus in context.
- **Only one concept in progress at any moment** — never start the next before committing the current.
- For "what links to X" or any whole-graph question, use **grep / the graph script** — never load every file. For a *committed* concept's "status / how many links / devanagari," grep **`MANIFEST.tsv`** (one line per concept) — do **not** load `index.md` wholesale or open the concept file. For "does X exist right now" (e.g. mid-batch), glob `concepts/` instead — the manifest lags until the next build.
- **Keep the startup set bounded.** Only `CLAUDE.md` + `progress.md` + `chapters/INDEX.md` (+ `MANIFEST.tsv` on demand) load every session; the per-concept loop is O(1), so the only thing that grows unboundedly is these always-loaded files. `progress.md` holds the active queue + the latest run-log only — closed run-logs live in `progress-archive.md` (rotate at end of batch, §9). Never let `progress.md` accrete history; `build_graph.py` nags past ~60 KB.
- Don't re-read the whole repo each turn; read `CLAUDE.md`, `progress.md`, and only the files the current task needs.
- Fetch each source **once**, distill into the file, then rely on the file — don't re-fetch.
- **Default model Sonnet.** If a concept needs deeper interpretive judgement than you can give cleanly, mark `status: needs-opus-review` and move on — do **not** attempt to switch models mid-run.
- If `/context` is filling, finish-and-commit the current concept, then continue fresh rather than dragging bloated context forward.

## §8 Unattended operation & FAIL-SAFE (the part that makes running out harmless)
**Startup reconcile — do this first, every session, before any new work:**
1. Read `CLAUDE.md`, `progress.md` (now bounded — active queue + latest run-log only; older history is in `progress-archive.md`, which you do **not** read at startup), **and `chapters/INDEX.md`** (the latter so the teaching-layer chapters are always in view, not just the concept batches). Do **not** load `index.md` or the whole corpus at startup; grep `MANIFEST.tsv` when you need a concept's existence/status. Remember: **"chapter" ≠ "batch"** — a chapter is a prose file under `chapters/`; a batch is a concept work-queue unit in `progress.md`. If the user's request mentions a "chapter," resolve it against `chapters/INDEX.md` before acting.
2. Run `git status` and `git log --oneline`; identify committed concepts (these are truth).
3. If `git status` shows any uncommitted/modified concept file (an interrupted draft) → **delete/reset it.** Never trust or continue partial work; it will be redone from scratch.
4. Reconcile `progress.md` to git (git wins on any mismatch).
5. Find the next `pending` concept in the batch and resume there. Never re-do a committed concept. Never recall a linked concept from memory — read its file.

**Dedup gate — BEFORE creating any concept file (the filename is the unique key; a duplicate key silently forks the graph):**
1. **Existence check against the live filesystem — `Glob concepts/<key>*.md`** (authoritative; never trust the manifest for this). A match → the concept exists; do **not** create — add typed links to it instead. The glob also surfaces the **tradition-suffix family** (`ahimsa`, `ahimsa-vedic`, `ahimsa-buddhist`) so you don't mint a third copy of a word that's already split. ⚠️ Do **not** use `grep MANIFEST.tsv` as the existence check: the manifest is only regenerated by `build_graph.py` (end of batch), so a concept you created earlier *in the same batch* is not in it yet — grepping the manifest would false-clear an in-batch duplicate. Use the manifest only for *committed* concepts' status/links/devanagari, never for "does it exist right now."
2. **Grep `concepts/` for the term and its transliteration variants** (`sunyata`/`shunyata`, `nibbana`/`nirvana`) and for existing `## Links` targets — a concept may already live under a *different* key. If many files already link `-> X`, `X` is canonical; a near-spelling is a duplicate, not a new node.
3. **Check `progress.md`** — a `pending` queue entry reserves a key that has no file yet.
- **Decision rule:** exact key exists → reuse it. Same word, *genuinely different tradition* → create with a tradition suffix **and** add an `often-conflated-with-NOT-equivalent` or `shares-vocabulary-with` edge between the pair (§5 — the map must teach the split). Same concept, different spelling → reuse the canonical key, note the alias in that file; never mint a variant node.
- After any bulk work, run `python graph/find_duplicates.py`; a non-zero exit (IAST/TRANSLIT/PHANTOM group) is a defect to resolve under §10 before pushing.

**Definition-of-done + pre-commit self-check (run before every commit):**
- Every claim cited? (no uncited assertions)
- New concept passed the **dedup gate** above — key is unique, or the reuse/typed-split decision is recorded?
- No from-scratch translation presented as authoritative?
- `status` and `confidence` set, and confidence justified (high only on independent agreement)?
- Links use the controlled vocabulary and parseable format? Physics links typed as parallel/conflated, never identity?
- Front-matter and all template sections present?
If all pass → commit. If a concept can't pass (e.g. sources unavailable) → set `status: blocked` (or `needs-opus-review`) with the reason recorded in-file, commit **that**, and move on. **Never commit silently-incomplete work. Never fabricate to pass the check.**

**Unresolvable / stuck:** if after a bounded effort (~5 searches/fetches) you can't find ≥2 genuinely independent sources → `status: blocked` with what you tried and what's missing, commit, next concept. Never loop, never stall, never invent.

**Scope-lock:** work ONLY the batch concepts, in order. You MAY add typed links to not-yet-written concepts (creating referenced-but-unwritten nodes) but do **NOT** write those files this run. Do not expand the index beyond the batch, do not start other texts or traditions, do not produce a roadmap.

## §9 End-of-batch behaviour
When the batch is complete (or you hit the token wall): **run `python graph/build_graph.py`** (regenerates `graph.*`, `index.md`, and `MANIFEST.tsv`, and runs the structural audit + the progress.md size-nag), then append a run-summary to `progress.md` — concepts completed (count + list with status), anything `blocked`/`needs-opus-review`, and a suggested next batch (names only, unwritten) — final commit, then **halt**.

**Run-log rotation (keeps the startup set bounded — do this whenever you add a run-summary, and always if the size-nag fires):** `progress.md` holds only the active queue + the **latest** run-log. After writing the new summary, move the *previously* newest run-log block down into `progress-archive.md` (append at the bottom; git is the canonical history regardless). Never let `progress.md` accumulate closed run-logs — it loads on every startup. The archive is never read at startup.

## §10 Gate policy (when to act autonomously vs. stop and ask)
- **Mechanical/structural defects** that `build_graph.py` (or a grep audit) can verify deterministically — cycles, orphans, mistyped edges with one §3-correct form: fix per §3 vocab, re-run the audit to **prove** it's resolved, atomic commit + push, log in `progress.md`, and **continue**. Do not stop to ask.
- **STOP and ask ONLY for:** (a) genuine forks — more than one defensible choice (direction, slicing, what-to-build-next); (b) destructive/irreversible actions — history rewrites, deletions beyond a single mistyped edge, anything not recoverable via `git revert`.
- Everything done autonomously goes in the end-of-batch report — auditable after the fact, not before.
