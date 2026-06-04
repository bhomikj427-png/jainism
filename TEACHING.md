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
- A chapter is a **reading layer generated from the concept files — never a second source of truth.** If a concept updates, regenerate the chapter; don't duplicate or let it drift.
- **One chapter per coherent cluster**, using the dense regions of the graph (e.g. a "Jain ontology" chapter over `sat, dravya, paryaya`; a "Jain epistemology" chapter over `anekantavada, syadvada, saptabhangi, naya`).
- Written for **zero prior knowledge**, concise, visual-first — a **contested** concept is shown as its comparison table (reading / who holds it / what it commits you to), not buried in prose.
- **Preserve citations**: every claim references its TS verse number and edition. Flag anything with confidence: low inline; `needs-opus-review` as "⚠️ verify before trusting."
- Turn every `often-conflated-with-NOT-equivalent` link into an explicit **"Conflation alert"** callout (`> ⚠️`), explaining: (1) the surface similarity that drives the conflation, (2) the precise difference that breaks it.
- **Number the sections** (`1`, `1.1`, `2`…) so exact spots can be referenced. Give each section a stable markdown anchor.
- End every chapter with a short **"Check yourself"** section — 2–3 explain-it-back prompts. The success metric is that the reader can reconstruct the cluster without the chapter.

## §8 Stuck-marker protocol
- The reader marks the exact spot they are stuck by writing a line beginning `?? ` (optionally with their question) directly in the chapter file, then saving.
- To resolve: for **each** marker, read the surrounding chapter text **plus the underlying concept file(s)**, then write a fresh explanation **directly beneath the marker** in a `> 💡` blockquote that starts with the reader's question and adds the explanation from a **different angle** — a new analogy, a worked example, a small visual. Never just repeat the chapter's phrasing.
- Log each stuck-point in `teaching-log.md` (concept, question, resolution). Recurring stuck-points flag a weak chapter explanation to improve.
- After resolving all markers, tell the reader which chapters still have open markers (if any).
