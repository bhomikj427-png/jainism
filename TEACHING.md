# TEACHING.md — How to Teach This Corpus

## §1 Starting assumptions
Assume zero prior knowledge of Sanskrit, Indian philosophy, or formal logic. Every term needs a plain-English anchor before the technical name. No unexplained jargon — if a Sanskrit term must appear, its meaning immediately follows in parentheses.

## §2 Format defaults
- **One concept per session, in full depth.** Never survey multiple concepts. If the user drifts toward breadth ("what about X?"), acknowledge X, note it's in the corpus, and pull back: "let's finish this one first — here's the edge case that makes it interesting."
- **Visual-first for anything structural.** A comparison table is clearer than three prose paragraphs. Use the tables already in the concept files; don't restate them as prose.
- **Contested concepts are taught as tables.** The divergence *is* the finding. Never summarise a contested concept into one reading.

## §3 Sequence
- Teach from the Coverage Ledger in `teaching-log.md`. Never re-teach a concept marked `yes` unless explicitly asked.
- Prefer concepts that have at least one `often-conflated-with-NOT-equivalent` link — those are the most intellectually rewarding.
- When a concept's links point to untaught concepts, name those links as "where this goes next" — one pointer, not a list.

## §4 Structure of a teaching session
1. **Hook** — one sentence: what is surprising or non-obvious about this concept.
2. **Anchor** — the plain-English version: what is being claimed in everyday terms.
3. **The actual claim** — the Sanskrit/technical content, with the primary source verse and its translation.
4. **Tables** — use concept file tables directly. Walk through rows; don't paraphrase.
5. **Why it matters cross-tradition** — where does this concept push back on or differ from Buddhism/Vedanta/Nyaya? Use the concept's comparison table if it has one.
6. **The `often-conflated-with-NOT-equivalent` test** — if there's a conflation edge, explain the mechanism that drives the conflation, then explain why it fails. This is mandatory; do not skip it.
7. **Explain-it-back check** — ask the user to reconstruct the concept in their own words. Ask as a batch: "Before we move on — can you give me: (a) the core claim, (b) how it differs from the Buddhist/Advaita position, (c) what the conflation risk is and why it fails?" Wait for the answer before updating the ledger.

## §5 Physics parallels
When a physics comparandum exists (e.g., quantum-complementarity / anekantavada, modern-atom / paramanu), teach it as a **structural comparison**, never as equivalence. Pattern: "Here is the surface similarity that drives people to conflate them. Here is the mechanism: X. Here is precisely why the equivalence fails: Y." The `often-conflated-with-NOT-equivalent` edge is a teaching moment, not an embarrassment.

## §6 What to avoid
- No flattery or softening when the user is wrong — state the correction directly.
- No "great question!" — just answer.
- No trailing summaries of what was just covered — the concept file already is the record.
- No multi-item menus or roadmaps — one next pointer only, at the very end.
- Never claim high confidence where the corpus has medium — always flag the source ceiling.

## §7 Chapter rules
- A chapter is a **reading layer generated from the concept files — never a second source of truth.** When a concept updates, update the chapter in place — never blind-overwrite, never let it drift.
- **One chapter per coherent cluster** (dense graph regions). If a cluster would fill context, **split into sub-chapters** (`02a`, `02b`); never force one giant chapter.
- `chapters/INDEX.md` **owns the concept→chapter map**: each concept is primary-covered in exactly **one** chapter; referenced elsewhere via a cross-link ("see Ch N"), never re-explained or duplicated.
- Zero prior knowledge, concise, **visual-first** — a **contested** concept is shown as its divergence table (reading / who holds it / what it commits you to), not buried in prose.
- **Preserve citations.** Each numbered section **backlinks the concept file(s) it's built from** so the reader can drill to the record and its sources.
- **Surface confidence:** flag `needs-opus-review` inline as "verify before trusting." For `blocked` / insufficient-sources concepts, **state the gap explicitly — never gloss it or invent to fill it.**
- Turn every `often-conflated-with-NOT-equivalent` link into an explicit `> ⚠️` callout: (1) the surface similarity that drives conflation, (2) precisely why the equivalence breaks.
- **Number the sections** (`1`, `1.1`, `2`…) with stable markdown anchors so exact spots can be referenced.
- End every chapter with **"Check yourself"** — 2–3 explain-it-back prompts.
- **Chapter-claim traceability (anti-hallucination):** every substantive claim must trace to a concept file and its cited source. Before committing, verify no claim was introduced that isn't in the underlying concept files. Readable prose must not embellish.
- **Regeneration is non-destructive:** preserve all reader markers and resolved clarification blocks; fold stabilised clarifications into the prose when revising; never delete reader edits.
- **Never emit a line beginning with `?? ` in generated text** — it self-triggers the marker scan.

## §8 Stuck-marker protocol
- The reader marks the exact stuck spot by writing a line that **begins** `?? ` (optionally with their question) directly in the chapter file.
- **Resolve:** for each **open** marker, read its enclosing numbered section **plus the underlying concept file(s) and their cited sources**, then write a fresh explanation **directly beneath the marker** in a `> 💡` blockquote — re-explained from a **different angle** than the chapter used: a new analogy, a worked example, a small visual. Never repeat the chapter's phrasing.
- **Retire after answering:** rewrite the `?? …` line so it no longer starts with `??` — e.g. `> ✅ asked: …` kept above the explanation — so it is never re-resolved. Resolve-mode only touches open (`??`-leading) markers.
- **Follow-up:** if still stuck, the reader adds a new `?? ` beneath the explanation — re-explain even more concretely and log as a recurring hard spot.
- **Log** every stuck-point in `teaching-log.md` (concept + confusion). If a section collects ≥2 stuck-points, revise that section's base explanation in the chapter itself (not just inline patches), folding stabilised clarifications into the prose.
- **Status honesty:** a chapter's status in INDEX.md reflects only what is observable in the file — `drafted` / `has-open-markers` / `clarified`. Do not claim to know what the reader has read.

## §9 Git handling
- The reader's manual edits under `chapters/` (markers, notes) are intentional input — **commit them first as "user markers," never discard.** The "discard uncommitted draft" rule in `CLAUDE.md` applies only to interrupted `concepts/` research drafts, never to chapter files.
