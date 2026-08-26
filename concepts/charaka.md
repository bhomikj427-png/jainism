---
term_iast: Caraka
term_devanagari: चरक
tradition: Hindu (Āyurveda)
source_text: Caraka Saṃhitā
status: contested
confidence: medium
---

## Gloss / Divergence map

"**Charaka**" names both a semi-legendary physician and the sprawling, multi-layered internal-medicine compendium (*Caraka Saṃhitā*) that bears his name — one of Āyurveda's two foundational Saṃhitās (with `sushruta.md`). The text itself records its own redaction history rather than presenting as a single-author original:

| layer | who | what happened |
|---|---|---|
| 1 | Agniveśa (under Ātreya's teaching) | composed the original *Agniveśa Saṃhitā* |
| 2 | Charaka | revised and renamed it the *Caraka Saṃhitā*, ca. 100 BCE–200 CE (Meulenbeld's range) |
| 3 | Dṛḍhabala | ca. 6th c. CE, rewrote a lost one-third of the book and re-wrote the last part; added all 17 chapters of the closing Cikitsā section plus the entire Kalpa and Siddhi sthānas |

The surviving text depends entirely on Dṛḍhabala's recension — no earlier manuscript layer survives independently, which is why "Charaka" cannot straightforwardly mean "the one author of this book."

**Contested: is "Charaka" a person at all?** Scholar Chattopadhyay's position, reported via Wikipedia, is that "charaka does not refer to one person but a lineage or sect of people" — the word *caraka* has an independent Sanskrit sense of "wandering (physician/ascetic)." This is set against the traditional reading (and the bulk of popular/medical-history literature) that treats Charaka as an individual physician, "Father of Indian Medicine," flourishing in a fairly narrow window (Meulenbeld: not later than ~150–200 CE, not much earlier than ~100 BCE). `status: contested` is set at the file level specifically for this authorship question; the text's structure and dating band are comparatively convergent.

**Structure.** Eight *sthānas* (books), 120 chapters: Sūtra (30, general principles/prevention), Nidāna (8, etiology), Vimāna (8, physician training/ethics/diet), Śarīra (8, anatomy/embryology), Indriya (12, diagnosis/prognosis), Cikitsā (30, therapeutics), Kalpa (12, pharmaceutics/toxicology), Siddhi (12, treatment success/hygiene).

**Content emphasis vs. Suśruta.** Charaka centers internal medicine and physiological/pathological theory — it is the text where the tridosha framework is given its most systematic doctrinal treatment (`tridosha.md`) — and treats surgery only briefly, the mirror-image emphasis of the surgery-centered `sushruta.md`. Their relative chronological priority is unresolved in the sources consulted.

## Reasoning across signals

1. **Wikipedia, "Charaka Samhita"** — three-layer redaction (Agniveśa/Charaka/Dṛḍhabala), Meulenbeld's dating range, Chattopadhyay's "lineage not person" thesis, eight-sthāna structure with chapter counts, Chakrapāṇidatta's 11th-c. commentary as the base for the modern Sanskrit edition, P. V. Sharma's 1981–1994 English translation.
2. **WebSearch aggregation (Kerala Tourism/keralatourism.org, Britannica-derived secondary summaries, Wikipedia "Charaka")** — independently confirms "Father of Indian Medicine" epithet, the 2nd-c. BCE–2nd-c. CE flourishing window, and Charaka Samhita's status as one of Āyurveda's two foundational texts. Britannica's own pages (britannica.com/topic/Charaka-Samhita, britannica.com/biography/Charaka) returned HTTP 403 on direct fetch and could not be quoted directly — noted as a sourcing gap rather than silently substituted.
3. **Corpus-internal** (`ayurveda.md`, this batch) — confirms the two-Saṃhitā structure and dating-band consistency.

Two independently-fetched signals (Wikipedia's dedicated Charaka Samhita article, and the aggregated secondary web material) converge on the redaction history and dating band → **converged** on those points. But the same Wikipedia article itself reports a genuine internal scholarly split (person vs. lineage) that neither signal resolves → **contested** on authorship specifically, recorded as a table above rather than silently picking the traditional reading. Confidence **medium**: Meulenbeld's *History of Indian Medical Literature* (the authoritative academic source underlying the dating claims) was cited via Wikipedia's summary, not independently fetched and read.

## Sources

- "Charaka Samhita," *Wikipedia*, https://en.wikipedia.org/wiki/Charaka_Samhita — **encyclopedia, sourced to Meulenbeld**: redaction layers, dating range, Chattopadhyay lineage thesis, structure, commentary/translation history.
- Britannica, "Charaka" and "Charaka Samhita" — **attempted, blocked (HTTP 403)**; not directly quoted. Flagged as an unresolved sourcing gap rather than papered over with an indirect citation.
- WebSearch aggregation (keralatourism.org, amargranth.com, byjus.com) — secondary popular-history sources, cross-checked against Wikipedia for the epithet and flourishing window; treated as corroborating, not independent-grade, evidence given their derivative character.

## Links

- formalizes: ayurveda | the Caraka Saṃhitā is one of the two foundational codifications of the Āyurvedic medical system (internal-medicine branch)
- formalizes: tridosha | the Caraka Saṃhitā's Sūtrasthāna gives the tridosha theory its earliest systematic textual treatment
- structurally-parallel-to: sushruta | both are foundational, multi-redactor Āyurvedic Saṃhitās with the same core subjects (pathology, diagnosis, therapeutics, pharmaceutics) but opposite emphasis — internal medicine (Charaka) vs. surgery (Suśruta) — and an unresolved relative chronology
- shares-vocabulary-with: guna-samkhya | Charaka's constitutional-personality typology classifies individuals by dominance of the same sattva/rajas/tamas triad Sāṃkhya uses for prakṛti's universal constituents — a psychological application of Sāṃkhya-style vocabulary, not the Sāṃkhya metaphysical claim itself
- formalizes: dhatu | the thirteen-agni scheme and the dhātu-nourishment doctrine are transmitted through the Caraka Saṃhitā's Cikitsā Sthāna, and the three *dhātu-poṣaṇa-nyāya*s through Cakrapāṇidatta's commentary on it
- formalizes: mala | the Caraka Saṃhitā supplies the tri-mala, the seven dhātu-mala correspondences, and the doctrine that a certain quantity of waste is required for the body to function
- formalizes: agni-ayurveda | the four states of *jāṭharāgni* and the *mandāgni*-as-disease-cause claim (Ci. 15/51) are Caraka's; Ci. 15/3 makes ojas, tejas and prāṇa depend on agni's status
- structurally-parallel-to: vagbhata | the third member of the *bṛhat-trayī* and the same evidentiary shape again — a definite compendium behind an uncertain person; Vāgbhaṭa is also a successor who synthesises this text, so the two relations are not in competition
