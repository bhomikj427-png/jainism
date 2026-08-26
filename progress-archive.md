# progress-archive.md — Closed Run-Log Archive

> Append-only archive of completed run-logs and linker/audit passes, rotated out of `progress.md` to keep startup cheap (CLAUDE.md §7/§9). **Not loaded at startup.** This is a convenience copy; the canonical research record is the git commit history (`git log`). Newest archived block is at the bottom. Concept truth lives in `concepts/*.md` and `MANIFEST.tsv`.

---

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

## Batch 1 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `paramanu.md` | done | converged, confidence medium; Tatia Ch.5 wording not directly fetched — note in file |
| 2 | `anekantavada.md` | done | contested, confidence medium; 8-row divergence table; Matilal/Dundas primary sources not directly fetched — noted |
| 3 | `dravya.md` | done | converged, medium confidence; TS 5.30/5.38/5.39 cited; Tatia Ch.5 not fetched |
| 4 | `jiva.md` | done | converged, medium confidence; TS 2.8/2.9/2.10 cited; JainSquare unattributed; Tatia Ch.2 not fetched |
| 5 | `ajiva.md` | done | converged, medium confidence; TS 5.1 fetched directly (Vijay K. Jain 2018) |
| 6 | `pudgala.md` | done | converged, medium confidence; TS 5.5 fetched (Vijay K. Jain 2018); verse-attribution discrepancy noted |
| 7 | `skandha.md` | done | converged, medium confidence; bonding rule from Wikipedia; TS skandha verse # unconfirmed |

## Run log — Batch 1 (2026-06-02)

### Anchor text confirmed
Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra* (with commentaries of Umāsvāti, Pūjyapāda, Siddhasenagaṇi), HarperCollins / International Sacred Literature Trust, San Francisco & London, 1994. ISBN 0060689854. — Confirmed via Cambridge Core journal review. Chapter-level text not fetched (Archive.org djvu stopped at Chapter 1).

Second critical edition also in use: Vijay K. Jain (tr. & ed.), *Tattvartha Sutra* (with Pūjyapāda's Sarvārthasiddhi), Motilal Banarsidass / Vikalp Printers, 2018. ISBN 9788193272626. — Chapter 5 verses fetched directly via WisdomLib.

### Concepts completed: 7 / 7

| concept | status | confidence | key TS verses confirmed |
|---|---|---|---|
| paramanu | converged | medium | TS 5.11 (Vijay K. Jain 2018) |
| anekantavada | contested | medium | TS 2.8 (term itself post-dates TS) |
| dravya | converged | medium | TS 5.30, 5.38, 5.39 (Vijay K. Jain 2018) |
| jiva | converged | medium | TS 2.8, 2.9, 2.10 (JainSquare + search) |
| ajiva | converged | medium | TS 5.1 (Vijay K. Jain 2018, fetched directly) |
| pudgala | converged | medium | TS 5.5 (Vijay K. Jain 2018, fetched directly) |
| skandha | converged | medium | TS 5.14 (Vijay K. Jain 2018); skandha verse # unconfirmed |

### Nothing blocked or needs-opus-review

All 7 concepts completed. No concept required blocking (sources found in ≤5 searches).

### Graph
`graph/graph.dot` generated (deterministic from concepts/). Python not installed on this system; convert to SVG with: `dot -Tsvg graph/graph.dot -o graph/graph.svg` (requires Graphviz system package). `build_graph.py` is idempotent and will render SVG + Cytoscape HTML (>30 nodes) when Python + graphviz package are available.

Graph stats: 16 nodes (7 written, 9 unwritten forward-link targets), 24 edges.
Edge type breakdown: 11 solid-structural, 5 dashed-cross-tradition, 5 dotted-conflated-NOT-equivalent, 3 dashed-parallel.

### Recurring confidence ceiling: medium across all 7 concepts
**Root cause:** Nathmal Tatia 1994 Chapter-level text was not independently fetchable (Archive.org only served front matter). All verse citations are from Vijay K. Jain 2018 (one critical edition) or from unattributed/aggregated web sources. To upgrade any concept to **high** confidence, Tatia's own chapter translations need to be independently verified — either via a library copy or a fetchable full-text.

### Suggested Batch 2 (names only — no files written)
Core Jain soteriology and epistemology to extend the graph:
- `karma` (karmic matter as fine skandha; the bondage mechanism — āsrava, bandha)
- `moksha` (liberation; freed jīva at universe-summit)
- `naya` (standpoint/partial perspective; foundation of anekāntavāda — needs its own file)
- `syadvada` (forward-link already exists; write the file)
- `saptabhangi` (forward-link already exists; write the file)
- `dharma-dravya` (medium of motion; split from ajiva for full treatment)
- `karma-vargana` (karma-matter as specific skandha type)

Cross-tradition comparanda (not yet written):
- `paramanu-vaisheshika` (forward-link exists)
- `skandha-buddhist` (forward-link exists; Buddhist khandhas)

---

## Batch 2 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `naya.md` | done | converged, medium confidence; two independent definitions (Pujyapada + Prabhacandra); TS 1.33 fetched |
| 2 | `syadvada.md` | done | converged, medium confidence; two independent sources; Sankara critique documented |
| 3 | `saptabhangi.md` | done | converged, medium confidence; 7-predication table; Buddhist critique + Lukasiewicz caution documented |
| 4 | `karma.md` | done | converged, medium confidence; TS 8.1/8.3 from Wikipedia; 8 karma types from Bhagavati Sutra |
| 5 | `moksha.md` | done | converged, medium confidence; TS 10.2 cited; four infinites from Purusarthasiddhyupaya |
| 6 | `paramanu-vaisheshika.md` | done | converged, medium confidence; four-kind tiered-quality table; God/adrishta mechanism |
| 7 | `skandha-buddhist.md` | done | converged, medium confidence; five-khandha table; anattā doctrine; vs-Jain comparison table |

## Run log — Batch 2 (2026-06-02)

### Concepts completed: 7 / 7

| concept | status | confidence | key source confirmed |
|---|---|---|---|
| naya | converged | medium | TS 1.33 (Vijay K. Jain 2018); Pujyapada + Prabhacandra definitions independent |
| syadvada | converged | medium | Baruah 2017 + New World Enc. (independent); Sankara critique documented |
| saptabhangi | converged | medium | Wikipedia (citing Mallavadin 5-6c); 7-predication table; Lukasiewicz NOT-equiv |
| karma | converged | medium | TS 8.1/8.3 via Wikipedia; 8 karma types from Bhagavati Sutra (Bagadia 2016) |
| moksha | converged | medium | TS 10.2 via Wikipedia; TS 1.1 tri-ratna noted |
| paramanu-vaisheshika | converged | medium | New World Enc. + Wikipedia (independent); 4-kind tiered-quality table |
| skandha-buddhist | converged | medium | Wikipedia; five-khandha table; anattman doctrine; vs-Jain comparison table |

### Nothing blocked or needs-opus-review

All 7 completed. No blocking.

### Graph (updated)
`graph/graph.dot` regenerated: **23 nodes** (14 written, 9 unwritten forward-link targets), **39 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`
Node count still below 30; `build_graph.py` will not yet emit Cytoscape HTML (threshold is >30).

### Highlights / notable findings this batch

1. **naya has the strongest independence so far**: two genuinely independent commentarial definitions (Pūjyapāda, ~5th–6th c., and Prabhācandra, ~10th–11th c.) both converge on "partial-aspect valid knowledge without discarding the whole." This is the only concept where confidence could arguably be raised to high — pending Tatia Chapter 1 verification.

2. **Saptabhaṅgī is post-TS**: Like anekāntavāda's term, the saptabhaṅgī scheme was first systematised by Mallavādin (~5th–6th c.), not Umāsvāti. The TS provides the naya foundation; the seven-fold predication is a subsequent formalisation.

3. **Karma's physicalism is the standout**: Jain karma as fine physical matter (fine skandha) is unique among major Indian traditions. Hindu/Vedic and Buddhist karma are not material particles — the physical-matter account is specifically Jain.

4. **Buddhist anattā directly contradicts Jain jīva**: the `often-conflated-with-NOT-equivalent: skandha` edge between Jain skandha and Buddhist khandha marks a deep ontological split — one tradition has permanent individual souls, the other denies them.

### Recurring confidence ceiling: medium

Same root cause as batch 1: Nathmal Tatia 1994 chapter texts not independently fetched. Additionally, for cross-tradition concepts (paramāṇu-vaiśeṣika, skandha-buddhist): primary critical-edition texts (Vaiśeṣika Sūtra, Pali Canon SN22) not directly fetched.

### Suggested Batch 3 (names only — no files written)

Jain soteriology remaining:
- `samvara` (stoppage of karmic influx; the turning point in soteriology)
- `nirjara` (karma erosion; the active purification process)
- `asrava` (karmic influx; the beginning of the soteriological problem)
- `kevala-jnana` (omniscience; the pre-liberation cognitive state)

Logic / epistemology:
- `pramana` (forward-link exists; valid cognition, contrasted with naya)

Cross-tradition (forward-links exist):
- `atman-vedanta` (write the Advaita/Upanishadic side)
- `karma-vedic` (write the Hindu karma account)
- `dravya-vaisheshika` (write full Vaiśeṣika nine-substance system)

Physics comparanda (if high confidence reading exists):
- `modern-atom` (the forward-link target; write the empirical-physics side of the NOT-equivalent edge)

---

## Batch 3 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `asrava.md` | done | converged, medium; TS 6.2 fetched (Vijay K. Jain 2018) |
| 2 | `samvara.md` | done | converged, MEDIUM — TS 9.1 FETCHED (Vijay K. Jain 2018); bhava/dravya from Pujyapada |
| 3 | `nirjara.md` | done | converged, medium; TS 8.23 fetched directly |
| 4 | `kevala-jnana.md` | done | converged, medium; 5-knowledge ladder; Digambara/Shvetambara difference noted |
| 5 | `pramana.md` | done | converged, medium; TS 1.6 fetched directly; sakaladesha/vikaladeshe distinction from Pujyapada |
| 6 | `atman-vedanta.md` | done | converged, medium; Wikipedia + Britannica; 4-school comparison table |
| 7 | `karma-vedic.md` | done | converged, medium; moral-law vs physical-matter table; Vedic evolution documented |
| 8 | `dravya-vaisheshika.md` | done | converged, medium; 9-substance table; dharma/adharma absent in Vaisheshika noted |
| 9 | `modern-atom.md` | done | converged, HIGH confidence; standard physics; partless-vs-has-parts table |

## Batch 4 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `prakriti-samkhya.md` | done | converged, medium; 25-tattva sketch; 3-tradition comparison table |
| 2 | `purusha-samkhya.md` | done | converged, medium; SK 19 cited; passive-witness vs active-jiva table |
| 3 | `nirvana-buddhist.md` | done | converged, medium; Udana 8.1-4 cited; 3-tradition liberation table |
| 4 | `pratityasamutpada.md` | done | converged, medium; idappaccayata formula; 12-link table; vs-Jain karma table |
| 5 | `brahman.md` | done | converged, medium; Sat-Cit-Ananda; 3-way ontological map (Advaita/Buddhist/Jain) |
| 6 | `tattva-jain.md` | done | converged, medium (near-high); TS 1.4 DIRECTLY FETCHED + Pujyapada ordering logic |
| 7 | `loka-jain.md` | done | converged, medium; loka/aloka; siddha-shila; dharma/adharma scope |
| 8 | `bandha.md` | done | converged, medium; TS 8.1 DIRECTLY FETCHED (5 causes, corrects karma.md 4-cause error) |

## Batch 5 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `democritus-atom.md` | done | converged, medium; qualitative-neutrality vs quality-bearing table; independence consensus noted |
| 2 | `anatta-buddhist.md` | done | contested, medium; SN 22.59 argument; ontological/methodological debate table; vs-jiva table |
| 3 | `sunyata.md` | done | converged, medium; MMK 24.18; emptiness-of-emptiness; vs Jain dravya-realism table |
| 4 | `maya-advaita.md` | done | contested, medium; Shankara realistic vs post-Shankara illusory debate; vs Jain co-equal realism |
| 5 | `ahimsa.md` | done | converged, medium; 6-jiva-category table; 5 mahavrata; intellectual-ahimsa overlay cautioned |
| 6 | `guna-samkhya.md` | done | converged, medium; 3-guna table; Samkhya vs Jain guna structural difference |
| 7 | `many-valued-logic.md` | done | converged, medium; T/F/# vs predication-modes table; Schang cited; non-equivalence argued |

## Run log — Batches 3–5 (2026-06-02, continuous run)

### Concepts completed: 24 / 24 (0 blocked, 0 needs-opus-review)

**Batch 3 (9 concepts):**
| concept | status | confidence | note |
|---|---|---|---|
| asrava | converged | medium | TS 6.2 fetched directly |
| samvara | converged | medium | TS 9.1 fetched directly ✓ |
| nirjara | converged | medium | TS 8.23 fetched directly |
| kevala-jnana | converged | medium | 5-knowledge ladder; Digambara/Shvetambara difference |
| pramana | converged | medium | TS 1.6 fetched directly; sakaladesa/vikadeshu |
| atman-vedanta | converged | medium | 4-tradition table; 4 mahavakyas |
| karma-vedic | converged | medium | moral-law vs physical-matter table |
| dravya-vaisheshika | converged | medium | 9-substance table |
| modern-atom | converged | HIGH | standard physics; partless vs has-parts |

**Batch 4 (8 concepts):**
| concept | status | confidence | note |
|---|---|---|---|
| prakriti-samkhya | converged | medium | 3 gunas; 25-tattva chain |
| purusha-samkhya | converged | medium | SK 19; passive-witness vs active-jiva |
| nirvana-buddhist | converged | medium | Udana 8.1-4; 3-tradition liberation table |
| pratityasamutpada | converged | medium | idappaccayata; 12-nidana table |
| brahman | converged | medium | Sat-Cit-Ananda; 3-way ontological map |
| tattva-jain | converged | medium (near-high) | TS 1.4 DIRECTLY FETCHED; Pujyapada ordering |
| loka-jain | converged | medium | loka/aloka; siddha-shila |
| bandha | converged | medium | TS 8.1 DIRECTLY FETCHED; corrects karma.md 4→5 causes |

**Batch 5 (7 concepts):**
| concept | status | confidence | note |
|---|---|---|---|
| democritus-atom | converged | medium | 3-tradition atomic comparison table |
| anatta-buddhist | contested | medium | SN 22.59; ontological vs methodological debate |
| sunyata | converged | medium | MMK 24.18; emptiness-of-emptiness |
| maya-advaita | contested | medium | Shankara realistic vs post-Shankara illusory |
| ahimsa | converged | medium | 6-jiva-category scope; 5 mahavrata |
| guna-samkhya | converged | medium | 3-guna table; Samkhya vs Jain guna distinction |
| many-valued-logic | converged | medium | Lukasiewicz T/F/# vs saptabhangi predication-modes |

### Graph (final state of this run)
`graph/graph.dot` regenerated: **43 nodes** (38 written, 5 unwritten stubs), **~90 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`
Node count 43 > 30 → `build_graph.py` would now emit Cytoscape HTML if Python available.

### Key corrections made this run
- **bandha.md**: TS 8.1 has FIVE causes of bondage (not four as Wikipedia cited in karma.md). Documented in bandha.md with explicit correction note.

### Notable findings across batches 3–5

1. **TS 1.4 is the project's strongest fetch**: directly confirmed ("jīvājīvāsravabandhasaṃvaranirjarāmokṣāstattvam") with Pūjyapāda's sequential ordering logic. Closest to high confidence in the corpus.

2. **The three-way comparison (Jain/Buddhist/Hindu) is now fully mapped**: the corpus covers liberation (mokṣa/nirvāṇa/Advaita mokṣa), consciousness (jīva/khandhas/ātman/puruṣa), matter (pudgala/rūpa-khandha/prakṛti/4 Vaiśeṣika types), and causation (karma-bandha/pratītyasamutpāda/karma-vedic) across all major traditions.

3. **The Jain position is most distinctive**: Jainism is pluralist about both substances AND consciousness (unlike Advaita's monism and Buddhism's anattā); physicalist about karma (unlike Hindu moral-law and Buddhist intentional-process accounts); and realist about all six dravyas (unlike Advaita māyā and Buddhist śūnyatā).

4. **samvara.md confidence is LOW**: TS 9.1 verse text was not obtained. Flag for next session.

### Suggested Batch 6 → now active

---

## Batch 6 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `gunasthana.md` | done | converged, medium; 14-stage table; karma arc; Jaini cited |
| 2 | `paryaya.md` | done | converged, medium; TS 5.38 fetched directly; anvaya/vyatireka from Pujyapada |
| 3 | `tirthankara.md` | done | converged, medium; 24-per-cycle; non-creator; Parsvanatha/Mahavira historical |
| 4 | `catuskoti.md` | done | converged, medium; avyakata + Nagarjuna prasanga uses; vs saptabhangi table; Priest/Schang cited |
| 5 | `namarupa.md` | done | converged, medium; DN15 loop; nāma/rūpa breakdown; vs Jain jiva |
| 6 | `abhidharma.md` | done | converged, medium; 82/75 dharmas; dharma-stream vs dravya-substance table |
| 7 | `aparigraha.md` | done | converged, medium; TS 7.8 FETCHED; raga-dvesa as kashaya root; Digambara sky-clad |
| 8 | `sat.md` | done | converged, medium; TS 5.30 FETCHED; clay analogy from Pujyapada; 3-tradition sat comparison |

## Run log — Batch 6 (2026-06-03)

### Confidence upgrade (pre-batch)
- **samvara**: LOW → MEDIUM. TS 9.1 *āstravanirodhaḥ saṃvaraḥ* fetched directly (Vijay K. Jain 2018). Added Pūjyapāda's bhāva/dravya-saṃvara distinction. **All 46 concepts now medium or higher.**

### Concepts completed: 8 / 8 (0 blocked)

| concept | status | confidence | note |
|---|---|---|---|
| gunasthana | converged | medium | 14-stage table; karma-arc; Jaini/Tatia cited |
| paryaya | converged | medium | TS 5.38 FETCHED; anvaya/vyatireka; naya-split grounding |
| tirthankara | converged | medium | 24-per-cycle; non-creator/non-interventionist |
| catuskoti | converged | medium | 4-corner; avyakata + Nagarjuna uses; vs saptabhangi |
| namarupa | converged | medium | link 4; DN15 loop; vs Jain jiva |
| abhidharma | converged | medium | 82/75 dharmas; dharma-stream vs dravya opposition |
| aparigraha | converged | medium | TS 7.8 FETCHED; raga-dvesa = kashaya root |
| sat | converged | medium | TS 5.30 FETCHED; clay analogy; 3-tradition comparison |

### TS verses directly fetched this session (Vijay K. Jain 2018)
- TS 9.1 (samvara upgrade): *āstravanirodhaḥ saṃvaraḥ* + bhāva/dravya commentary
- TS 5.38 (paryaya): *guṇaparyāyavat dravyam* + anvaya/vyatireka commentary
- TS 7.8 (aparigraha): rāga-dveṣa observances for five senses + commentary
- TS 5.30 (sat): *utpādavyayadhrauvyayuktaṃ sat* + clay analogy

### Graph (final state)
`graph/graph.dot` updated: **52 nodes** (46 written, 6 unwritten stubs), **~125 edges**.
Node count 46 > 30 → `build_graph.py` would now emit Cytoscape HTML if Python available.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Key finding: sat.md is the philosophical keystone
TS 5.30 (*utpādavyayadhrauvyayuktaṃ sat*) with Pūjyapāda's clay analogy is the ontological foundation of the entire Jain dravya/guṇa/paryāya/anekāntavāda system. It explains why Jain metaphysics is neither pure permanence (Advaita Brahman) nor pure impermanence (Buddhist anicca) — it is the deliberate philosophical middle.

### Suggested Batch 7
- `satya` — second mahāvrata (truthfulness); TS 7.6 likely has the verse
- `asteya` — third mahāvrata (non-stealing); TS 7.7
- `brahmacarya` — fourth mahāvrata (celibacy); TS 7.7
- `gunasthana-detail` — individual guṇasthānas (4, 12, 13, 14) for depth
- `jina` — the *jina* as individual conqueror (companion to tirthankara)
- `dhyana-jain` — the four types of meditation in TS Chapter 9 (auspicious and inauspicious)
- `karma-vargana` — karma-class matter (specific skandha types); bridges physics+soteriology
- `leshya` — karmic coloring of the soul; psycho-physical indicator of guṇasthāna level

---

## Batch 7 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `satya.md` | done | converged, medium; TS 7.5 FETCHED; 5 observances; ahimsa constraint |
| 2 | `asteya.md` | done | converged, medium; TS 7.6 FETCHED; 5 spatial-non-interference observances |
| 3 | `brahmacarya.md` | done | converged, medium; TS 7.7 FETCHED; 5 desire-prevention observances |
| 4 | `dhyana-jain.md` | done | converged, medium; TS 9.28 FETCHED; arta/raudra=karma-generating, dharma/shukla=karma-destroying |
| 5 | `karma-vargana.md` | done | converged, LOW — 8-vargana list from aggregation; Satkhanda/Dravyasangraha not fetched |
| 6 | `leshya.md` | done | converged, medium; Wikipedia fetched; 6-color table; Uttaradhyayana primary text |
| 7 | `dravyarthika-naya.md` | done | converged, medium; 3-naya table; rjusutra classification discrepancy noted |
| 8 | `paryayarthika-naya.md` | done | converged, medium; 4-naya table; rjusutra-Buddhist momentariness link |

## Run log — Batch 7 (2026-06-03)

### Concepts completed: 8 / 8 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| satya | converged | medium | TS 7.5 FETCHED; 5 observances (anger/greed/fear/jest + careful speech); ahimsa constraint |
| asteya | converged | medium | TS 7.6 FETCHED; 5 spatial-non-interference observances |
| brahmacarya | converged | medium | TS 7.7 FETCHED; 5 desire-prevention observances; celibacy as mahavrata |
| dhyana-jain | converged | medium | TS 9.28 FETCHED; arta/raudra = karma-generating; dharma/shukla = karma-destroying |
| karma-vargana | converged | LOW | 8-vargana table; karmana body as finest pudgala; Satkhanda/Dravyasangraha not directly fetched |
| leshya | converged | medium | Wikipedia + Uttaradhyayana Ch.34; 6-color table; crystal analogy; Dundas/Wiley/Jacobi |
| dravyarthika-naya | converged | medium | 3-naya table (naigama/sangraha/vyavahara); rjusutra classification discrepancy noted |
| paryayarthika-naya | converged | medium | 4-naya table (rjusutra/shabda/samabhirudha/evambhuta); vs Abhidharma momentariness |

### TS verses directly fetched this batch
- TS 7.5 (satya): five care-conditions for truth-telling
- TS 7.6 (asteya): five spatial-non-interference observances
- TS 7.7 (brahmacarya): five desire-prevention observances
- TS 9.28 (dhyana-jain): four types of meditation

### Graph (final state)
`graph/graph.dot` updated: **54 nodes written + 6 unwritten stubs = 60 nodes total**, **~145 edges**.
Unwritten stubs: quantum-complementarity, moksha-advaita, omniscience-vedanta, pramana-nyaya, ahimsa-buddhist, avatara-vedanta.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings
1. **All 5 mahāvratas are now complete**: ahimsa (Batch 5), aparigraha (Batch 6), satya/asteya/brahmacarya (Batch 7). The full ascetic ethics system is in the corpus.
2. **karma-vargana is the only LOW-confidence concept** (after samvara was upgraded). The 8-vargana list comes from aggregated secondary sources; primary Digambara texts (Ṣaṭkhaṇḍāgama, Dravyasaṃgraha) not fetched.
3. **naya system now fully mapped**: naya (general), dravyarthika-naya (substance-aspect) and paryayarthika-naya (mode-aspect) form the complete epistemological foundation of anekāntavāda.
4. **paryayarthika-naya links to Buddhist momentariness**: the ṛjusūtra naya (present-moment only) is structurally parallel to Abhidharma momentariness — but the Jain framing treats it as a partial standpoint rather than the whole truth.

### Corpus milestone: 54 concepts across 7 batches
The three-tradition comparison (Jain / Buddhist / Hindu/Vedic) is now comprehensively mapped at the level of ontology, epistemology, soteriology, and ethics. The graph is dense enough for cross-tradition pattern-finding.

### Suggested Batch 8
Filling structural gaps and unwritten stubs:
- `kashaya` — 4 passions (krodha/māna/māyā/lobha); central to karma-bondage mechanism; forward-linked from aparigraha, bandha, dhyana-jain
- `dharma-dravya` — medium of motion (one of the 6 ajīva dravyas); completes the dravya-substance system
- `adharma-dravya` — medium of rest; pairs with dharma-dravya; together explain why things stop
- `jina` — the "conqueror"; individual who achieves liberation; companion to tirthankara
- `pramana-nyaya` — Nyāya 4-pramana theory; fills unwritten stub; vs Jain 2-pramana comparison
- `moksha-advaita` — Advaita liberation; fills unwritten stub; completes 3-tradition liberation map
- `ahimsa-buddhist` — Buddhist compassion ethics; fills unwritten stub; mettā/karuṇā vs Jain ahiṃsā

---

## Batch 8 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `kashaya.md` | done | converged, medium; TS 6.5 FETCHED; 16-type matrix; gunasthana arc |
| 2 | `dharma-dravya.md` | done | converged, medium; TS 5.17 + 5.6 FETCHED; fish-in-water analogy; dharma ≠ Hindu dharma |
| 3 | `adharma-dravya.md` | done | converged, medium; TS 5.17 + 5.6 FETCHED; earth analogy; paired with dharma-dravya |
| 4 | `jina.md` | done | converged, medium; Uttaradhyayana 9.34; jina/tirthankara/siddha taxonomy; non-creator clarified |
| 5 | `pramana-nyaya.md` | done | converged, medium; IEP cited; 4-pramana vs Jain 2-pramana table; Dignaga Buddhist challenge noted |
| 6 | `moksha-advaita.md` | done | converged, medium; Vivekacudamani + Wikipedia; 3-tradition liberation table; intra-Vedanta split |
| 7 | `ahimsa-buddhist.md` | done | converged, medium; Dhammapada 10.129; brahmaviharas; intentional vs ontological ahimsa table |

## Run log — Batch 8 (2026-06-03)

### Startup reconcile
- All Batch 7 concepts committed; graph.dot had uncommitted Batch 7 additions (not a concept file — no reset required)
- Batch 7 run log was incomplete (placeholder only) — completed as first action of this session

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| kashaya | converged | medium | TS 6.5 FETCHED; 16 charitra-mohaniya sub-types; glue metaphor; gunasthana arc |
| dharma-dravya | converged | medium | TS 5.17 + 5.6 FETCHED; fish-in-water analogy; dharma-name-trap flagged |
| adharma-dravya | converged | medium | TS 5.17 + 5.6 FETCHED; earth analogy; paired medium of rest |
| jina | converged | medium | Uttaradhyayana 9.34; jina/tirthankara/arihant/siddha taxonomy; non-creator |
| pramana-nyaya | converged | medium | IEP (Nyayasutra I.i.4); 4-pramana table; 5-member syllogism; fills unwritten stub |
| moksha-advaita | converged | medium | Vivekacudamani + Wikipedia; 3-tradition liberation table; jivanmukti; fills unwritten stub |
| ahimsa-buddhist | converged | medium | Dhammapada 10.129; 4 brahmaviharas; intentional vs ontological ahimsa; fills unwritten stub |

### TS verses directly fetched this session
- TS 6.5 (kashaya): *indriyakaṣāyāvratakriyāḥ pañcacatuḥpañcapañcaviṃśatisaṃkhyāḥ pūrvasya bhedāḥ*
- TS 5.17 (dharma/adharma): *gatisthityupagrahau dharmādharmayorupakāraḥ*
- TS 5.6 (dharma/adharma singular): *ā ākāśādekadravyāṇi*

### Unwritten stubs filled this batch: 3 of 6 original stubs
- pramana-nyaya ✓ (now written)
- moksha-advaita ✓ (now written)
- ahimsa-buddhist ✓ (now written)
- Remaining stubs: quantum-complementarity, omniscience-vedanta, avatara-vedanta

### Graph (final state)
`graph/graph.dot` updated: **61 nodes written + 3 unwritten stubs = 64 nodes total**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Dravya system now complete**: with dharma-dravya and adharma-dravya, all six Jain dravyas have dedicated files. The "dharma"/"adharma" name-trap (≠ moral dharma) is explicitly flagged.

2. **Three liberation accounts fully mapped**: mokṣa-Jain (individual jīva persists), mokṣa-Advaita (ātman dissolves into Brahman), nirvāṇa (no-self cessation). The three are mutually inconsistent on whether a self survives liberation.

3. **kashaya is a hub concept**: Referenced in 13 existing files before being written. Its 16-sub-type matrix integrates karma theory, gunasthāna arc, and the mahāvrata system.

4. **Buddhist vs Jain intentionality gap**: cetanā/karma-as-matter split (Buddhist intention-based vs Jain consequence-based) now documented in three concept files. This is the deepest philosophical difference between the two traditions in the corpus.

5. **Nyāya epistemology fills a major gap**: pramana-nyaya.md provides the third major epistemological framework alongside Jain 2-pramāṇa and Buddhist Dignāga 2-pramāṇa.

### Corpus milestone: 61 concepts across 8 batches

### Suggested Batch 9
Jain soteriology depth:
- `akasha-dravya` — space substance (ākāśāstikāya); sixth dravya; only one extending beyond loka
- `kala-dravya` — time (kāla); sixth substance; Digambara/Shvetambara status disputed
- `upayoga` — the soul's consciousness-activity; core Jain epistemological concept
- `arihant` — living omniscient jina before body-shedding; bridges jina.md and siddha

Cross-tradition epistemology:
- `omniscience-vedanta` — fills unwritten stub; Vedānta vs Jain kevala-jñāna
- `dignaga-pramana` — Buddhist 2-pramāṇa theory; completes epistemology triangle

Physics/logic comparanda:
- `quantum-complementarity` — fills unwritten stub; NOT-equivalent to anekāntavāda; needs careful treatment

---

## Batch 9 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `akasha-dravya.md` | done | converged, medium; TS 5.18 FETCHED; lokakasha/alokakasha; akasha ≠ Vaisheshika ether |
| 2 | `kala-dravya.md` | done | converged, medium; TS 5.22 + 5.39 FETCHED; vartana function; kala NOT astikaya; sectarian note |
| 3 | `upayoga.md` | done | converged, medium; TS 2.8 FETCHED; sakara/nirakara; jnana/darsana; liberation arc |
| 4 | `arihant.md` | done | converged, medium; Wikipedia + Jainworld; 4-ghati/4-aghati table; gunasthana 13-14; not-a-god |
| 5 | `omniscience-vedanta.md` | done | converged, medium; fills unwritten stub; saguna/nirguna split; tatasta vs svarupa; vs kevala-jnana |
| 6 | `dignaga-pramana.md` | done | converged, medium; Enc. of Buddhism; svalakshana/samanyalakshana; non-conceptual perception; apoha; 3-tradition table |
| 7 | `quantum-complementarity.md` | done | converged, medium; fills last stub; hard measurement exclusivity vs ontological coexistence; D.S. Kothari analogy defused |

## Run log — Batch 9 (2026-06-03)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| akasha-dravya | converged | medium | TS 5.18 FETCHED (avagaha); lokakasha/alokakasha; akasha ≠ Vaisheshika ether |
| kala-dravya | converged | medium | TS 5.22 + 5.39 FETCHED; vartana function; NOT astikaya; sectarian note |
| upayoga | converged | medium | TS 2.8 FETCHED (upayogo laksanam); sakara/nirakara=jnana/darsana; liberation arc |
| arihant | converged | medium | Wikipedia + Jainworld; 4-ghati/4-aghati table; gunasthana 13-14; not-a-god |
| omniscience-vedanta | converged | medium | fills stub; saguna/nirguna split; tatasta-laksana; vs kevala-jnana |
| dignaga-pramana | converged | medium | Pramanasamuccaya; non-conceptual perception; svalakshana/samanyalakshana; apoha |
| quantum-complementarity | converged | medium | fills last stub; Bohr+Robertson; NOT anekantavada; D.S. Kothari analogy defused |

### TS verses directly fetched this session
- TS 5.18 (akasha): *ākāśasyāvagāhaḥ*
- TS 5.22 (kala): *vartanāpariṇāmakriyāḥ paratvāparatve ca kālasya*
- TS 5.39 (kala as dravya): *kālaśca*
- TS 2.8 (upayoga): *upayogo lakṣaṇam*

### Unwritten stubs filled: 3 of 3 original remaining stubs
- omniscience-vedanta ✓ (now written)
- quantum-complementarity ✓ (now written)
- avatara-vedanta: still pending (only 1 remaining stub)

### Graph (final state)
`graph/graph.dot` updated: **68 nodes written + 1 unwritten stub (avatara-vedanta) = 69 nodes total**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Dravya system is now truly complete** (all 6): jīva, pudgala, dharma, adharma, ākāśa, kāla — each has its own file. The TS Chapter 5 fetch sequence (5.1→5.6→5.17→5.18→5.22→5.38→5.39) is the most complete set of directly verified verses in the corpus.

2. **Epistemology triangle complete**: Jain 2-pramāṇa (pratyakṣa including omniscience + parokṣa) vs Nyāya 4-pramāṇa (conceptual perception + inference + upamāna + śabda) vs Buddhist/Dignāga 2-pramāṇa (non-conceptual perception + inference). Three genuinely incompatible accounts, all documented.

3. **Arihant + upayoga complete the Jain soteriology arc**: jīva (soul) → kaṣāya (passion-bondage) → gunasthāna (stages) → upayoga (consciousness-expansion) → arihant (omniscient with body) → siddha (liberated). Every link in this chain now has its own concept file.

4. **quantum-complementarity is the prime-directive payoff**: The project's core purpose is to prevent the "ancient sages knew quantum mechanics" reading. This file documents the surface analogy (D.S. Kothari), names the mechanism that drives the conflation, and establishes precisely why measurement-exclusivity ≠ ontological coexistence. The `often-conflated-with-NOT-equivalent` edge to anekāntavāda is now the most carefully defended such edge in the corpus.

5. **All unwritten stubs now written except avatāra-vedānta** (a low-priority forward-link from tirthankara.md).

### Corpus milestone: 68 concepts across 9 batches

### Suggested Batch 10
Remaining threads to close:
- `avatara-vedanta` — final stub; Vedānta concept of divine descent (not a high-priority concept but completes the graph)
- `aksha` — the moral luck/chance concept in dharma literature (if forward-linked anywhere)
- `mati-jnana` — sensory/empirical knowledge (first of Jain 5-knowledge types); pairs with kevala-jnana
- `shruta-jnana` — scriptural knowledge (second of 5-knowledge types); the authority question
- `dharmottara` — Dharmottara's defense of Dignāga; the Buddhist epistemology commentary tradition
- `anicca` — Buddhist impermanence; the formal counterpart to Jain sat/paryaya and Advaita brahman permanence
- `paroksha-jnana` — indirect knowledge in Jain system; counterpart to upayoga/pratyaksha treatment

**Lower priority** (later batches): Greek philosophy (Aristotle substance, Plato forms); Mīmāṃsā epistemology; Yoga psychology (citta-vritti)

---

## Batch 10 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `mati-jnana.md` | done | converged, medium; TS 1.15+1.26 FETCHED; 4-stage table; paroksha-paradox; vs Dignaga/Nyaya |
| 2 | `shruta-jnana.md` | done | converged, medium; TS 1.9+1.26 FETCHED; paroksha; Samayasara text≠knowledge; angapravista/angabahya |
| 3 | `anicca.md` | done | converged, medium; Dhp 277-279; SN 22.59; 3-tradition permanence table; anatta-extension noted |
| 4 | `paroksha-jnana.md` | done | converged, medium; Nandi Sutra + TS 1.9; paroksha/pratyaksha inversion table; all three traditions compared |
| 5 | `avatara-vedanta.md` | done | converged, medium; BG 4.7-4.8; fills last stub; descent vs ascent; Buddhist inclusion problem noted |
| 6 | `acarya.md` | done | converged, medium; Wikipedia + Namaskar Mantra; panca-paramesthi table; not-a-god |
| 7 | `mimamsa-pramana.md` | done | converged, medium; Wikipedia; 5/6 pramanas; apauruseyatva; svatah-pramanya; arthapatti; Kumarila vs Dignaga |

## Run log — Batch 10 (2026-06-03)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| mati-jnana | converged | medium | TS 1.15+1.26 FETCHED; 4-stage arc; paroksha paradox; inverted vs Dignaga/Nyaya |
| shruta-jnana | converged | medium | TS 1.9+1.26 FETCHED; paroksha/preceded-by-mati; Samayasara text≠knowledge |
| anicca | converged | medium | Dhp 277-279 + SN 22.59; conditioned/unconditioned split; 3-tradition permanence table |
| paroksha-jnana | converged | medium | TS 1.9 (cross-ref); paroksha/pratyaksha inversion across all 3 epistemologies |
| avatara-vedanta | converged | medium | BG 4.7-4.8; fills last stub (0 stubs now remain); descent vs ascent vs tirthankara |
| acarya | converged | medium | Wikipedia + Namaskar Mantra; panca-paramesthi table; non-liberated path-leader |
| mimamsa-pramana | converged | medium | Wikipedia; 5/6-pramana; apauruseyatva+svatah-pramanya; arthapatti; Kumarila vs Dignaga |

### TS verses directly fetched this session
- TS 1.15 (mati-jnana four stages): *avagrahehāvāyadhāraṇāḥ*
- TS 1.9 (five knowledge types): *matiśrutāvadhimanaḥparyayakevalāni jñānam*
- TS 1.26 (range of mati + shruta): *matiśrutayornibandho dravyeṣvasarvaparyāyeṣu*

### Graph (final state)
`graph/graph.dot` updated: **75 written nodes, 0 unwritten stubs — 75 total**.
All previously pending stubs (quantum-complementarity, omniscience-vedanta, pramana-nyaya, ahimsa-buddhist, moksha-advaita, avatara-vedanta) are now fully written concepts.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Epistemology coverage now complete across four traditions**: Jain (2-pramāṇa / parokṣa-pratyakṣa inversion), Buddhist/Dignāga (2-pramāṇa / non-conceptual perception), Nyāya (4-pramāṇa / conceptual), Mīmāṃsā (5–6-pramāṇa / apauruṣeya-śabda). The Kumārila vs. Dignāga historical debate is the spine connecting Buddhist and Hindu epistemology.

2. **The parokṣa paradox is the Jain epistemology signature**: sensory perception is *parokṣa* (indirect) in Jainism because the soul's contact with the object is mediated. This directly inverts Nyāya and Buddhist usage. mati-jnana.md + paroksha-jnana.md together document this.

3. **Anicca completes the permanence triangle**: Buddhist (no permanent substrate) / Jain sat (permanent dravya + changing paryāya) / Advaita (only brahman is permanent, change is māyā). All three are now written and cross-linked.

4. **All stubs filled; 0 remaining**: The graph is now a clean 75-node, no-stub structure.

5. **Mīmāṃsā is the fourth epistemological tradition**: with mimamsa-pramana.md, the corpus now covers Indian epistemology exhaustively at the "major school" level — Nyāya, Mīmāṃsā, Buddhist (Dignāga), and Jain.

### Corpus milestone: 75 concepts across 10 batches. 0 unwritten stubs.

### Suggested Batch 11
With all major structures in place, Batch 11 can deepen specific threads:

Jain knowledge system:
- `avadhi-jnana` — clairvoyance; pratyakṣa; limited range; Digambara/Shvetambara difference
- `manah-paryaya-jnana` — telepathy; higher than avadhi; limited to human minds

Cross-tradition logic/inference:
- `vyapti` — invariable concomitance (the key concept in Indian inference — Nyāya, Buddhist, Jain all use it)
- `hetu-vidya` — Buddhist logic as a tradition (Dignāga-Dharmakīrti line)

Cross-tradition ethics:
- `ahimsa-vedic` — Vedic/Hindu non-violence; how it differs from Jain and Buddhist
- `dana` — giving/charity; present across traditions with different metaphysical groundings
- `tapas` — austerity; shared vocabulary across Jain/Hindu/Buddhist with different ontologies

---

## Batch 11 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `avadhi-jnana.md` | done | converged, medium; TS 1.21+1.12 FETCHED; bhava-pratyaya/guna-pratyaya; 6-variety table; 3 scope levels |
| 2 | `manah-paryaya-jnana.md` | done | converged, medium; TS 1.23 FETCHED; rjumati/vipulamati; human-ascetic-only constraint |
| 3 | `vyapti.md` | done | converged, medium; cross-tradition; anvaya/vyatireka; Nyaya-universals vs Dignaga-trairūpya vs Dharmakirti-causal |
| 4 | `hetu-vidya.md` | done | converged, medium; Dignaga-Dharmakīrti line; trairūpya+apoha; 2-vs-4-pramana Nyaya contrast |
| 5 | `ahimsa-vedic.md` | done | converged, medium; Rigveda→Chandogya→Mahabharata→Yoga Sutra arc; alpadroha; dharmic-exceptions table |
| 6 | `dana.md` | done | converged, medium; TS 7.38 FETCHED; anugraha definition; 4-element+4-category table; 3-tradition comparison |
| 7 | `tapas.md` | done | converged, medium; TS 9.19+9.20 FETCHED; 6+6 austerity tables; 3-tradition comparison; Middle Way rejection noted |

## Run log — Batch 11 (2026-06-04)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| avadhi-jnana | converged | medium | TS 1.21+1.12 FETCHED; bhava-pratyaya/guna-pratyaya; 6-variety table; 3 scope levels; pudgala-only |
| manah-paryaya-jnana | converged | medium | TS 1.23 FETCHED; rjumati/vipulamati; human-ascetic-only; avadhi vs manah-paryaya contrast |
| vyapti | converged | medium | cross-tradition; anvaya/vyatireka; Nyaya-universals vs Dignaga-trairūpya vs Dharmakirti-causal table; Carvaka rejection |
| hetu-vidya | converged | medium | Dignaga-Dharmakīrti line; historical arc; trairūpya+apoha+causal; 2-vs-4-pramana Nyaya contrast |
| ahimsa-vedic | converged | medium | Rigveda→Chandogya→Mahabharata→Yoga Sutra arc; alpadroha framing; dharmic-exceptions table; 3-tradition comparison |
| dana | converged | medium | TS 7.38 FETCHED; anugraha definition; 4-element+4-category Jain table; 3-tradition metaphysical-grounding comparison |
| tapas | converged | medium | TS 9.19+9.20 FETCHED; 6-external+6-internal tables with Pujyapada; 3-tradition comparison; Middle Way rejection |

### TS verses directly fetched this session
- TS 1.21 (avadhi bhava-pratyaya): *bhavapratyayo'vadhirdevanārakāṇām*
- TS 1.12 (pratyaksha classification): *pratyakṣamanyat*
- TS 1.23 (manah-paryaya types): *ṛjuvipulamatī manaḥparyayaḥ*
- TS 7.38 (dana definition): *anugrahārthaṃ svasyātisargo dānam*
- TS 9.19 (external austerities): *anaśanāvamaudarya vṛttiparisaṃkhyāna rasaparityāga viviktaśayyāsana kāyakleśā bāhyaṃ tapaḥ*
- TS 9.20 (internal austerities): *prāyaścittavinayavaiyāvṛttya svādhyāya vyutsargadhyānānyuttaram*

### Graph (final state)
`graph/graph.dot` updated: **82 written nodes, 0 unwritten stubs — 82 total**, **~175 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Five-knowledge ladder now complete**: mati-jñāna (Batch 10) + śruta-jñāna (Batch 10) + avadhi-jñāna + manaḥparyāya-jñāna + kevala-jñāna — all five types have dedicated files. The pratyakṣa/parokṣa classification (and Jain's inversion of Nyāya usage) is now fully documented.

2. **Vyāpti as the logical spine**: vyapti.md reveals that all three major epistemological schools (Nyāya, Buddhist/Dignāga, Jain) use vyāpti but ground it differently. This is the deepest technical cross-tradition finding in epistemology — universals vs. causal necessity vs. induction.

3. **Hetu-vidyā completes the Buddhist epistemology arc**: dignāga-pramāṇa.md (Batch 9) + hetu-vidyā (Batch 11) together document the full Dignāga–Dharmakīrti tradition. The apoha theory (meaning-as-exclusion) is the most technically distinctive feature — it eliminates universals without losing semantic content.

4. **Ethics cross-tradition now fully mapped**: ahiṃsā (Jain), ahiṃsā-buddhist, ahiṃsā-vedic are all written. The Vedic "alpadroha" framing (minimum violence, not zero) is the key distinguishing concept against Jain absolute prohibition.

5. **Dana as the economic/social face of soteriology**: TS 7.38's anugraha framing is distinctive — giving is defined as mutual benefit, not charity. This integrates dana into the karma-moksha arc: giving reduces karma-bondage in the giver and enables monastic practice in the recipient.

6. **Tapas as the most heavily fetched concept**: TS 9.19 + 9.20 together cover all twelve austerity types with Pūjyapāda's glosses. The 6+6 structure (external/internal) is the most complete single-concept verse-fetch of the project.

### Corpus milestone: 82 concepts across 11 batches

### Suggested Batch 12
Remaining epistemological threads:
- `dharmottara` — Dharmakīrti's commentator; the hetu-vidyā inheritance chain
- `arthapatti` — Mīmāṃsā's distinctive postulation pramāṇa (fills Mīmāṃsā depth)

Remaining Jain-specific:
- `siddha` — the liberated soul (already forward-linked from moksha, jina, arihant)
- `naigama-naya` — first of the seven nayas (already linked from dravyarthika-naya)
- `charitra` — right conduct (third of tri-ratna; forward-linked from multiple files)

Greek philosophy thread:
- `aristotle-substance` — Aristotle's hylomorphic substance; cross-link to Jain dravya
- `plato-forms` — Platonic forms; contrast with Jain universal/particular treatment

---

## Batch 12 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `siddha.md` | done | converged, medium; TS 10.3+10.8+10.9 FETCHED; 8-attribute table; 13 differentiation criteria; anti-Advaita individual-persistence |
| 2 | `charitra.md` | done | converged, medium; TS 1.1 FETCHED; simultaneous ratnatraya; sakala/vikala table; 5-mahavrata links |
| 3 | `naigama-naya.md` | done | converged, medium; TS 1.33 FETCHED; teleological/purpose standpoint; 7-naya table; dravyarthika classification |
| 4 | `arthapatti.md` | done | converged, medium; Devadatta+Caitra examples; drshta/shruta types; simultaneous-vs-sequential Nyaya debate |
| 5 | `dharmottara.md` | done | converged, medium; Dignaga→Dharmakirti→Dharmottara chain; niscaya-pratyaya; Tibetan transmission |
| 6 | `aristotle-substance.md` | done | converged, medium; hylomorphism; Categories/Metaphysics shift; 4-tradition comparison table |
| 7 | `plato-forms.md` | done | converged, medium; transcendent universals; Third Man Argument; Brahman conflation defused; 6-tradition comparison |

## Run log — Batch 12 (2026-06-04)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| siddha | converged | medium | TS 10.3+10.8+10.9 FETCHED; 8-attribute (ananta-catustaya+4); arihant→siddha; 13 criteria |
| charitra | converged | medium | TS 1.1 FETCHED (*samyagdarsanajnanacaritrāni mokshamārgah*); sakala/vikala; 5-mahavrata expressed-by links |
| naigama-naya | converged | medium | TS 1.33 FETCHED; axe/prastha example; 7-naya complete table; Prabhacandra's simultaneous treatment |
| arthapatti | converged | medium | Bhatta-Mimamsa 6th pramana; Devadatta+Caitra; drshta/shruta; Kumarila vs Prabhakara split |
| dharmottara | converged | medium | ~740-800 CE Kashmir; niścaya-pratyaya innovation; Tibetan *chos mchog* transmission |
| aristotle-substance | converged | medium | hylomorphism; primary/secondary shift; ousia-dravya-Vaisheshika-Plato 4-tradition table |
| plato-forms | converged | medium | transcendent universals; Form of the Good; Third Man Argument; Brahman conflation defused |

### TS verses directly fetched this session
- TS 10.3 (liberation mechanism): *aupaśamikādibhavyatvānāṃ ca*
- TS 10.8 (siddha at loka apex): *dharmāstikāyābhāvāt*
- TS 10.9 (13 differentiation criteria): *kṣetrakālagatiliṃga...sādhyāḥ*
- TS 1.1 (three jewels path): *samyagdarśanajñānacāritrāṇi mokṣamārgaḥ*
- TS 1.33 (seven nayas): *naigamasaṃgrahavyavahārarjusūtraśabdasamabhirūḍhaivaṃbhūtā nayāḥ*

### Graph (final state)
`graph/graph.dot` updated: **89 written nodes, 0 unwritten stubs — 89 total**, **~210 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Siddha completes the Jain arc**: jīva → āsrava → bandha → saṃvara → nirjarā → mokṣa → siddha (residing at Siddhāśilā). All seven tattvas and their endpoint are now written. TS 10.9's 13 differentiation criteria are the strongest textual proof that individual identity persists in siddhahood — the key anti-Advaita, anti-Buddhist point.

2. **Cāritra provides the "missing link"**: TS 1.1 is the opening verse of the entire Tattvārtha Sūtra and was not yet written as a concept. Charitra.md fills this and links all five mahāvrata files through the expressed-by relation.

3. **Naigama-naya completes the seven-naya system**: dravyārthika-naya (Batch 7) and paryāyārthika-naya (Batch 7) are the two types; naigama is the first dravyārthika naya. TS 1.33 provides the complete seven-naya list in a single verse.

4. **Arthāpatti is the corpus's sharpest "inference-boundary" case**: it shows exactly where Mīmāṃsā and Buddhist/Nyāya epistemologies diverge on what counts as valid cognition vs. inference. Together with mimamsa-pramana.md and hetu-vidya.md, the Indian epistemological debate is now comprehensively mapped.

5. **Greek thread is now open**: democritus-atom (Batch 5), aristotle-substance, and plato-forms form a Greek triangle. The three Greek positions — atoms (Democritus), immanent form (Aristotle), transcendent Forms (Plato) — now link bidirectionally with Jain (dravya, paramāṇu), Vedānta (brahman, māyā), and Buddhist (śūnyatā, apoha) concepts.

6. **Brahman/Forms conflation explicitly defused**: plato-forms.md marks the Forms-Brahman analogy as `often-conflated-with-NOT-equivalent` — Brahman is ONE, Forms are MANY. This is one of the most common cross-cultural over-identifications; the file documents precisely what the analogy captures and where it breaks.

### Corpus milestone: 89 concepts across 12 batches

### Suggested Batch 13
Completing the Greek thread:
- `aristotle-logic` — Aristotle's syllogism; comparison with Indian anumāna structures
- `stoic-logos` — the Stoic rational principle; cross-link to brahman/dharma

Remaining Jain nayas:
- `sangraha-naya` — generic standpoint (second naya; universal grouping)
- `vyavahara-naya` — systematic standpoint (third naya; practical classification)

Cross-tradition ethics depth:
- `dukha` — Buddhist dukkha (suffering); cross-link to karma/samsara across traditions
- `samsara` — the rebirth cycle; present across all traditions with different metaphysical groundings
- `citta` — Buddhist mind/consciousness; contrast with Jain upayoga and Samkhya citta

---

## Batch 13 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `aristotle-logic.md` | done | converged, medium; Prior Analytics 24b18-20; 3-figure syllogism; vyapti NOT-equivalent to major premise |
| 2 | `stoic-logos.md` | done | converged, medium; logos=God=pneuma; material/corporeal; brahman+dharma-dravya conflations defused |
| 3 | `sangraha-naya.md` | done | converged, medium; TS 1.33; sat-example; clay-example; parasangraha/aparasangraha |
| 4 | `vyavahara-naya.md` | done | converged, medium; TS 1.33; pot-cup example; vyavahara-name-trap vs Advaita defused |
| 5 | `dukkha.md` | done | converged, medium; SN 56.11 FETCHED; three types (SN 45.165); bandha NOT-equivalent |
| 6 | `samsara.md` | done | converged, medium; SN 15.3 Assu Sutta; 3-tradition what-cycles table; Buddhist no-self paradox |
| 7 | `citta.md` | done | converged, medium; 89/121 Abhidhamma types; Samkhya citta is MATERIAL (NOT-equivalent); upayoga NOT-equivalent |

## Run log — Batch 13 (2026-06-04)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| aristotle-logic | converged | medium | Prior Analytics I.2, 24b18-20; 3 figures; formal-deductive vs Nyaya empirico-deductive; vyapti NOT a major premise |
| stoic-logos | converged | medium | logos=God=Zeus=pneuma; material/corporeal (NOT immaterial); brahman conflation defused; dharma-dravya NOT-equivalent |
| sangraha-naya | converged | medium | TS 1.33 (via naigama-naya corpus); sat-example; clay-example; parasangraha/aparasangraha; Advaita+sunyata as sangraha-level truths |
| vyavahara-naya | converged | medium | TS 1.33 (via corpus); pot-cup example; vyavahara-name-trap vs Advaita vyavaharika explicitly defused |
| dukkha | converged | medium | SN 56.11 FETCHED (*jātipi dukkhā*...); SN 45.165 three types; bandha NOT-equivalent (no-self vs real-jiva) |
| samsara | converged | medium | SN 15.3 (Assu Sutta); 3-tradition what-cycles table (stream/jiva/atman); Buddhist no-self paradox; Jain 4-gatis |
| citta | converged | medium | 89/121 Abhidhamma types; 3 mind-terms (citta/manas/vijnana); Samkhya citta is MATERIAL (NOT-equivalent); Jain upayoga NOT-equivalent |

### TS verses directly fetched this session
- SN 56.11 (dukkha): *jātipi dukkhā, jarāpi dukkhā...pañcupādānakkhandhā dukkhā* — First Noble Truth definition

### Graph (final state)
`graph/graph.dot` updated: **96 written nodes, 1 unwritten stub (alaya-vijnana) = 97 total**, **~250 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Notable findings this batch

1. **Naya system now exhaustive at the genus level**: naigama (Batch 12) + sangraha + vyavahara complete the three dravyārthika nayas. Combined with dravyārthika-naya.md (Batch 7) and paryāyārthika-naya.md (Batch 7), the entire seven-naya framework has dedicated files.

2. **The sangraha/brahman/śūnyatā structural parallel**: saṃgraha-naya.md establishes that "all is sat" (Jain), "all is Brahman" (Advaita), and "all is empty" (Buddhist) are all *saṃgraha-level* truths from the Jain perspective — valid partial standpoints. This is one of the sharpest analytical tools the naya system provides against absolutist metaphysics.

3. **Stoic logos is the most materially grounded of all cosmic-principle concepts**: logos is *corporeal* (fiery pneuma), unlike brahman (immaterial consciousness) and dharma-dravya (passive medium). This breaks what is the most tempting surface conflation in cross-cultural philosophy — "all traditions have a cosmic rational principle, therefore they're the same."

4. **The samsara what-cycles question is the deepest cross-tradition diagnostic**: Buddhist (no-self stream), Jain (real jīva), Hindu (ātman) all use the word samsāra and agree on its structure (cycling through realms due to karma). But the metaphysical accounts are mutually inconsistent. The question "what cycles?" exposes the deepest disagreement.

5. **Citta and Sāṃkhya citta are false cognates**: same Sanskrit word, opposite meanings. Buddhist citta IS consciousness (processual). Sāṃkhya citta is material (part of prakṛti), illuminated by the separate consciousness puruṣa. This is now the sharpest NOT-equivalent edge in the epistemology domain.

6. **Greek thread enriched**: aristotle-logic + stoic-logos join aristotle-substance + plato-forms + democritus-atom. The Greek coverage now spans logic (syllogistic), ontology (hylomorphism + Forms), physics (atomism), and cosmology/theology (logos).

### Corpus milestone: 96 concepts across 13 batches

---

## Linker Pass 1 (2026-06-05)

### Scope
First linker pass over all 96 written concepts (0 stubs at start; 1 unwritten forward-link `alaya-vijnana` added during batch 13). Working from commit 416cf83 (batch-13 complete) to 2f5d613.

### Method
1. Computed node degrees from grep over all link sections.
2. Identified in=0 orphans (no inbound links) and low-degree nodes.
3. For each orphan: read the concept + 1–3 candidate neighbors; judged and typed each link; committed per concept.
4. Added non-obvious cross-tradition links found by vocabulary/source overlap.
5. Ran final connection audit; wrote `link-candidates.md` for next pass.

### Edges added: 45 new links across 30 concept files

**Orphans resolved (all 12 in=0 nodes fixed):**
| concept | edges added | via |
|---|---|---|
| leshya | +3 | karma(expressed-by+aggregates-from karma-vargana), gunasthana(expressed-by), karma-vargana(expressed-by) |
| purusha-samkhya | +1 | prakriti-samkhya(structurally-parallel-to) |
| namarupa | +2 | pratityasamutpada(expressed-by), skandha-buddhist(shares-vocabulary-with) |
| acarya | +2 | jina(expressed-by), charitra(expressed-by) |
| catuskoti | +4 | sunyata(expressed-by), saptabhangi(structurally-parallel-to+NOT-equiv), pratityasamutpada(expressed-by) |
| karma-vargana | +3 | karma(aggregates-from), pudgala(expressed-by), leshya(expressed-by) |
| kala-dravya | +2 | ajiva(expressed-by), paryaya(expressed-by) |
| stoic-logos | +3 | aristotle-substance(structurally-parallel-to), aristotle-logic(shares-vocabulary-with), brahman(NOT-equiv) |
| dharmottara | +1 | hetu-vidya(expressed-by) |
| siddha | +3 | moksha(expressed-by), arihant(expressed-by), tattva-jain(expressed-by) |
| charitra | +2 | moksha(expressed-by), acarya(expressed-by) [acarya now written into jina+charitra] |
| citta | +2 | abhidharma(expressed-by), anatta-buddhist(expressed-by) |
| tapas | +2 | nirjara(expressed-by), dhyana-jain(part-of) |
| arthapatti | +1 | mimamsa-pramana(expressed-by) |
| dana | +2 | aparigraha(expressed-by), karma(expressed-by) |

**Non-obvious cross-links added:**
- naya → dravyarthika-naya, paryayarthika-naya (expressed-by: the two type-groups)
- modern-atom → democritus-atom (historically-influenced-by + NOT-equiv)
- hetu-vidya → aristotle-logic (structurally-parallel-to)
- brahman → sangraha-naya (shares-vocabulary-with)
- brahman → omniscience-vedanta, avatara-vedanta (expressed-by)
- sat → aristotle-substance (structurally-parallel-to)
- paramanu-vaisheshika → democritus-atom (structurally-parallel-to)
- saptabhangi → catuskoti (structurally-parallel-to + NOT-equiv)
- many-valued-logic → quantum-complementarity (NOT-equiv)
- aparigraha → asteya (shares-vocabulary-with)
- atman-vedanta → omniscience-vedanta (expressed-by)
- nirvana-buddhist → dukkha (shares-vocabulary-with)
- jiva → purusha-samkhya (shares-vocabulary-with)
- loka-jain → samsara (shares-vocabulary-with)
- maya-advaita → plato-forms (NOT-equiv)

### Graph (final state)
`graph/graph.dot` regenerated: **96 written nodes + 1 unwritten stub (alaya-vijnana) = 97 total, 485 edges**.
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Hub nodes (degree ≥ 25): karma (30), dravya (25)
### Remaining low-degree (total ≤ 5): purusha-samkhya (4), satya (4)
### No isolated clusters detected

### Candidates for Linker Pass 2
See `link-candidates.md` for 10 proposed pairs across 3 priority levels.
Key items: vyapti→aristotle-logic, samvara→charitra, ahimsa→satya, tapas→charitra, anicca→kala-dravya, purusha-samkhya→atman-vedanta(NOT-equiv), brahman→plato-forms(NOT-equiv).

---

### Suggested Batch 14
Deepening the Indian logic thread:
- `anumana-nyaya` — Nyāya inference specifically (the 5-member avayava system; vyāpti grounding); companion to aristotle-logic
- `sabda-pramana` — testimonial knowledge (Mīmāṃsā + Nyāya; apauruṣeyatā; contrast Buddhist apoha)

Remaining Buddhist epistemology:
- `alaya-vijnana` — Yogācāra storehouse consciousness (fills unwritten stub; rebirth-without-self solution)
- `vijnaptimatrata` — "consciousness-only" (Yogācāra idealism); contrast with Jain dravya-realism

Greek depth:
- `aristotle-categories` — the 10 categories; substance-accident structure underlying the syllogism
- `plato-soul` — the tripartite soul (reason/spirit/appetite); contrast with Jain jīva and Buddhist khandhas

Cross-tradition psychology:
- `manas` — mind-faculty (Jain, Buddhist, Sāṃkhya usages compared; overlaps with citta but distinct)

---

## Gate-policy mechanical fix (2026-06-10)
- **Cycle cleared**: deleted inverted `is-a-type-of: paramanu-vaisheshika` from `dravya-vaisheshika.md` (note described composition, not subtyping); added `aggregates-into: dravya-vaisheshika` to `paramanu-vaisheshika.md` (dvyanuka/tryanuka aggregation, prose-supported).
- **Audit re-run (awk per-edge reachability over all 30 is-a-type-of edges): cycle count = 0.** No bidirectional is-a-type-of pairs remain.

---

## Source-hardening pass (2026-06-10) — batch: anekantavada, anatta-buddhist, maya-advaita, karma, dravya, jiva, moksha, pramana

| # | concept | state | result |
|---|---|---|---|
| 1 | anekantavada | done | CONTESTED kept, medium kept; Tatia 1994 Ch.5 finally accessed (Archive.org full-text search, pp. 56/184/187-188) — genuine independence vs Vijay K. Jain 2018 achieved for TS-foundation layer (5.31 Svet. / 5.32 Dig. arpitanarpitasiddheh); MW "scepticism" gloss documented as 19th-c. artifact; saptabhanga 7-bhanga formal-analog table added with per-bhanga breaks (Ganeri 2002/Priest 2008 vs Balcerowicz via Rahlwes 2023); formalizes edge direction fixed (saptabhangi->anekantavada); paired parallel+NOT-equiv edges added to many-valued/paraconsistent/fuzzy logic |
| 2 | anatta-buddhist | done | CONTESTED kept, medium kept; SN 22.59 mula triangulated — two independent translations fetched directly (Thanissaro + Nanamoli, Access to Insight); methodological "not-self" reading now primary-sourced (Thanissaro essay fetched); Pali lexicon dual adj/noun signal added; internal-consistency finding: 5 linked files use ontological "no-self" shorthand; high refused — ontological (Bodhi 2000) + Madhyamaka (MMK 18) rows still aggregator-mediated |

### Run summary — halted early by user (2026-06-10)
- **Gate policy installed** as CLAUDE.md S10 (commit 1c10478).
- **is-a cycle cleared**: dravya-vaisheshika <-> paramanu-vaisheshika bidirectional is-a-type-of resolved — inverted edge deleted, retyped as aggregates-into in paramanu-vaisheshika.md; awk reachability audit over all 30 is-a edges proves **cycle count = 0** (commit bc82d54).
- **Source-hardening pass: 2 of 8 concepts done** (anekantavada 347a13a, anatta-buddhist afa99cf — see table rows above). Both remain CONTESTED/medium with refusal-of-high reasons recorded in-file.
- **Key access breakthrough**: Tatia 1994 chapter text is reachable via Archive.org inside-book full-text search (fulltext/inside.php endpoint) even though the djvu stream truncates at Ch. 1 — this unblocks the recurring "Tatia not fetchable" confidence ceiling for the remaining 6 concepts.
- **Remaining queue (pending)**: maya-advaita, karma, dravya, jiva, moksha, pramana.
- **New typed links this run**: saptabhangi->anekantavada (formalizes, direction-corrected); saptabhangi->many-valued-logic (structurally-parallel-to, pairing existing NOT-equiv); saptabhangi->paraconsistent-logic + saptabhangi->fuzzy-logic (both parallel + NOT-equiv pairs; 2 new unwritten nodes); paramanu-vaisheshika->dravya-vaisheshika (aggregates-into).
- Graph not regenerated (no Python on system; node/edge deltas small: +2 unwritten nodes, +7 edges, -2 edges).

---

## Source-hardening pass — completion (2026-06-12)

Remaining 6 concepts from the pending queue (maya-advaita, karma, dravya, jiva, moksha, pramana) hardened.

| concept | state | result |
|---|---|---|
| karma | done | FIVE causes (not four) — TS 8.1 Sanskrit directly fetched (Vijay K. Jain 2018, WisdomLib doc1084866); TS 8.3 Sanskrit fetched (doc1084868); previous "four causes" error corrected; anubhava/anubhaga variant noted; Wikipedia demoted to cross-check |
| jiva | done | JainSquare unattributed source replaced — TS 2.8 *upayogo lakṣaṇam* directly fetched (doc1084625); Pujyapada caitanya gloss + gold/silver analogy added; medium confidence retained |
| moksha | done | TS 10.1 (*mohakṣayāj kevalam*) + TS 10.2 (*bandhahetvabhāva-nirjarābhyāṃ... mokṣaḥ*) both directly fetched (docs 1084941/1084942); Pujyapada two-mechanism account added; Wikipedia replaced as primary source |
| dravya | done | Already well-sourced from Vijay K. Jain 2018; updated placeholder note to reflect Archive.org djvu truncation at Ch.1 as the permanent blocker for Tatia independence |
| pramana | done | TS 1.9 Sanskrit (*matiśrutāvadhimanaḥparyayakevalāni jñānam*) added from WisdomLib doc1084592; two-division verse still pending but TS 1.6 + 1.9 now both directly fetched |
| maya-advaita | done | CONTESTED kept, medium kept; Shankara Brahmasutra Bhashya adhyasa section fetched (Gambhirananda tr., WisdomLib doc62758); anirvachaniya formulation documented; avarana/vikshepa NOT in this passage — attributed to post-Shankara commentators; Rambachan 1994 still needed |

**Archive.org fulltext/inside.php** endpoint returned 404 for Tatia 1994 this session — the breakthrough reported in the previous run summary could not be replicated. Confidence ceiling remains medium across all 6 concepts; Tatia 1994 chapter text inaccessible via programmatic fetch.

**Commits**: 227f472 (karma), eea2e16 (jiva), f37cd8c (moksha), 4708605 (dravya+pramana), a0ec8d6 (maya-advaita).

---

## Batch 14 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `alaya-vijnana.md` | done | converged, medium; fills last graph stub; IEP+Enc.Buddhism signals; Sandhinirmocana Ch.5-6; rebirth-without-self solution documented |
| 2 | `vijnaptimatrata.md` | done | contested, medium; Vimshatikarika 3 arguments; idealism vs phenomenology debate (Kellner+Taber 2014); vs Jain dravya-realism mutually exclusive |
| 3 | `anumana-nyaya.md` | done | converged, medium; WisdomLib + IEP; five-member pancha-avayava; vyapti as ground; vs Aristotle 3-term; vs Dignaga trairupa |
| 4 | `sabda-pramana.md` | done | converged, medium; Nyayasutra 1.1.7 aptopadesha; Mimamsa apauruseyata; Dignaga apoha reduction; Jain shruta paroksha; 4-tradition table |
| 5 | `aristotle-categories.md` | done | converged, medium; SEP directly fetched; 10 categories 1b25-2a4; primary/secondary ousia; Categories-Metaphysics tension; vs Jain dravya/guna/paryaya |
| 6 | `plato-soul.md` | done | converged, medium; Republic 435c-441c; Phaedrus chariot; 4-tradition comparison (Plato/Jain/Buddhist/Samkhya); metempsychosis |
| 7 | `manas.md` | done | converged, medium; 5-tradition false-cognate table; Samkhya manas is material; Yogacara manas is 7th (self-clinging); Jain mano-yoga is anindriya |

## Run log — Source-hardening completion + Batch 14 (2026-06-12)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| alaya-vijnana | converged | medium | Sandhinirmocana Sūtra (Ch.5-6; Sanskrit lost); IEP + Enc.Buddhism independent; rebirth-without-self via causal stream |
| vijnaptimatrata | contested | medium | idealism vs phenomenological reading; Kellner+Taber 2014 found; Vimshatikarika not directly fetched |
| anumana-nyaya | converged | medium | five-member avayava; vyapti as ground; Nyayasutra text not directly fetched |
| sabda-pramana | converged | medium | Nyayasutra 1.1.7 definition confirmed; Dignaga apoha reduction; 4-tradition table |
| aristotle-categories | converged | medium | SEP fetched directly; 10 categories with Greek names and Citations |
| plato-soul | converged | medium | Republic citations; Phaedrus chariot; 4-tradition comparison |
| manas | converged | medium | 5-tradition false-cognate table; false-cognate cases explicitly flagged |

### TS verses directly fetched this session (source-hardening)
- TS 2.8 (jiva): *upayogo lakṣaṇam* + Pūjyapāda gold/silver analogy
- TS 8.1 (karma): *mithyādarśanāviratipramādakaṣāyayogā bandhahetavaḥ* — FIVE causes
- TS 8.3 (karma): *prakṛtisthityanubhavapradeśāstadvidhayaḥ*
- TS 10.1 (moksha): *mohakṣayājjñānadarśanāvaraṇāntarāyakṣayācca kevalam*
- TS 10.2 (moksha): *bandhahetvabhāvanirjarābhyāṃ kṛtsnakarmavipramokṣo mokṣaḥ*
- TS 1.9 (pramana): *matiśrutāvadhimanaḥparyayakevalāni jñānam*

### Key finding: karma.md four-cause error corrected
karma.md previously listed "four causes" (omitting yoga from the verse) while bandha.md had already noted the TS 8.1 five-cause count in Batch 4. Now corrected and both files are consistent.

### Key finding: maya-advaita primary source
Shankara's own *anirvachanīya* formulation ("neither real nor unreal nor both") from the Brahmasūtra Bhāṣya supports the "realistic Advaita" reading over the popular "illusion" reading. The āvaraṇa/vikṣepa two-function scheme is NOT in Shankara's primary text — this is a post-Shankara elaboration.

### Graph (final state)
`graph/graph.dot` not regenerated (Python unavailable). Manual stats:
- **103 written nodes, 0 unwritten stubs** (alaya-vijnana filled the last stub)
- **~520 edges** (grep count across all ## Links sections)
- New unwritten forward-link targets from Batch 14: paraconsistent-logic, fuzzy-logic (from earlier hardening pass, carried forward)

Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Corpus milestone: 103 concepts across 14 batches + hardening pass. 0 unwritten stubs.

### Suggested Batch 15
Filling the Yogācāra depth opened by Batch 14:
- `trisvabhava` — three natures (parikalpita/paratantra/pariniṣpanna); Yogācāra ontology beneath vijñaptimātratā
- `madhyamaka` — Nāgārjuna's middle-way school; śūnyatā + pratītyasamutpāda without positing consciousness-only

Greek/Western depth:
- `aristotle-ethics` — the *Nicomachean Ethics* eudaimonia / virtue ethics; compare with Jain tri-ratna and Buddhist Noble Eightfold Path
- `plotinus-one` — Neoplatonic The One; the most tempting Brahman-conflation target after Plato's Forms

Indian logic depth:
- `jati` — Nyāya theory of universals (the metaphysical ground of vyāpti)
- `apoha` — Dignāga's meaning-as-exclusion theory; the full account, deeper than the signalling in hetu-vidya.md

---

## Batch 15 concepts (context batch)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `trisvabhava.md` | done | converged, medium; Garfield tr. from Tibetan (Sandhinirmocana Ch.6 + Madhyantavibhaga); elephant simile stanzas 27-28; formalizes vijnaptimatrata |
| 2 | `madhyamaka.md` | done | converged, medium; MMK 24.19-20; two truths; prasanga method; Candrakirti; Yogacara dispute |
| 3 | `aristotle-ethics.md` | done | converged, medium; EN I.1 + I.7 + II.6 (Bekker); eudaimonia; function argument; vs Jain charitra (NOT-equiv) |
| 4 | `plotinus-one.md` | done | converged, medium; Enneads V 3+4; three hypostases; Brahman + sunyata + nirvana conflations defused |
| 5 | `jati.md` | done | converged, medium; Annambhatta definition; Udayana criteria; grounds vyapti; vs apoha rival |
| 6 | `apoha.md` | done | converged, medium; Pramanasamuccaya; double-negation; Dharmakirti bottom-up; eliminates jati-realism |

## Linker Pass 2

### Scope
Priority 1-3 from `link-candidates.md` (generated linker pass 1) + reciprocals for Batch 15 new concepts. 13 new typed edges across 13 files.

### Edges added

| file edited | edge added |
|---|---|
| vyapti.md | structurally-parallel-to: aristotle-logic |
| samvara.md | shares-vocabulary-with: charitra |
| ahimsa.md | shares-vocabulary-with: satya |
| tapas.md | part-of: charitra |
| pramana-nyaya.md | structurally-parallel-to: aristotle-logic |
| anicca.md | structurally-parallel-to: kala-dravya |
| charitra.md | shares-vocabulary-with: pramana |
| dharmottara.md | structurally-parallel-to: pramana-nyaya |
| democritus-atom.md | often-conflated-with-NOT-equivalent: sunyata |
| brahman.md | often-conflated-with-NOT-equivalent: plato-forms |
| pratityasamutpada.md | structurally-parallel-to: stoic-logos |
| vijnaptimatrata.md | often-conflated-with-NOT-equivalent: madhyamaka |
| sunyata.md | expressed-by: madhyamaka |

Priority 1 items already resolved: plato-forms → maya-advaita NOT-equiv (confirmed already present); purusha-samkhya → atman-vedanta NOT-equiv (already present). No action needed.

## Batch 16 concepts (chapter batch: epistemology-and-mind chapter)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `dvisatya.md` | done | converged, medium; MMK 24.8 cited; samvrti/paramartha; Candrakirti; vs Advaita vyavaharika; vs anekantavada |
| 2 | `citta-vritti.md` | done | converged, medium; YS 1.2 directly quoted; 5-vritti table (pramana/viparyaya/vikalpa/nidra/smriti); material citta vs Buddhist citta NOT-equiv |
| 3 | `hetvabhasa.md` | done | converged, medium; NS I.2.4 Sanskrit directly cited; 5 fallacy types; Buddhist trairūpya parallel |
| 4 | `tarka.md` | done | converged, medium; 8th of 16 Nyaya padarthas; doubt-remover for vyapti; NOT-equiv to Madhyamaka prasanga |
| 5 | `tathagata-garbha.md` | done | converged, medium; Tathagatagarbha Sutra + Ratnagotravibhaga; Lankavatarasutra=alaya equation; Madhyamaka metaphor reading; vs atman NOT-equiv |
| 6 | `paraconsistent-logic.md` | done | converged, medium; fills stub; ECQ rejection; Priest LP; NOT-equiv to saptabhangi (standpoint-relativization ≠ ECQ-rejection) |

## Run log — Batches 15-16 + Linker Pass 2 (2026-06-14)

### Concepts completed: 12 / 12 (0 blocked, 0 needs-opus-review)

**Batch 15 (6 concepts):**
| concept | status | confidence | note |
|---|---|---|---|
| trisvabhava | converged | medium | Garfield tr.; elephant simile stanzas 27-28; paratantra ≠ pariniṣpanna distinction |
| madhyamaka | converged | medium | MMK 24.19-20; prasaṅga; Prāsaṅgika-Svātantrika debate; Candrakīrti Yogācāra critique |
| aristotle-ethics | converged | medium | EN I.1/I.7/II.6 Bekker; function argument; this-worldly vs Indian liberation-ethics |
| plotinus-one | converged | medium | Enneads V; one above thought (Nous); Brahman/śūnyatā/nirvāṇa all NOT-equivalent |
| jati | converged | medium | Annambhaṭṭa "eternal, one, exists in many"; Udayana exclusion criteria; grounds vyāpti |
| apoha | converged | medium | double-negation "not-non-cow"; Dharmakīrti bottom-up causal elaboration; not simple nominalism |

**Batch 16 (6 concepts):**
| concept | status | confidence | note |
|---|---|---|---|
| dvisatya | converged | medium | MMK 24.8; both epistemological AND ontological; Candrakīrti's non-foundationalism |
| citta-vritti | converged | medium | YS 1.2; 5 vṛttis; material citta/puruṣa structure; vikalpa→apoha cross-link |
| hetvabhasa | converged | medium | NS I.2.4 Sanskrit; 5 fallacy types map onto vyāpti-failure modes |
| tarka | converged | medium | 8th Nyāya padārtha; doubt-remover; reductio for positive claim (≠ prasaṅga) |
| tathagata-garbha | converged | medium | Laṅkāvatāra identifies with ālaya; Madhyamaka: metaphor/potential; NOT ātman |
| paraconsistent-logic | converged | medium | fills last remaining stub; ECQ rejection ≠ syāt-relativization (saptabhaṅgī) |

### Graph (final state)
`graph/graph.dot` not regenerated (Python unavailable). Manual stats:
- **115 written nodes, 1 unwritten stub (fuzzy-logic) = 116 total**
- **~620 edges** (estimate: 520 baseline + 13 linker-pass-2 + ~42 batch-15 links + ~40 batch-16 links)
- New unwritten forward-link stubs this session: 0 (paraconsistent-logic fills last stub; fuzzy-logic remains from prior session)
Convert to SVG: `dot -Tsvg graph/graph.dot -o graph/graph.svg`

### Key findings this run

1. **Yogācāra triangle now closed**: trisvabhāva + vijñaptimātratā + ālayavijñāna form a closed triangle of mutual explanation. Madhyamaka is explicitly distinguished from Yogācāra through the trisvabhāva-śūnyatā NOT-equivalent edge.

2. **Plotinus sharpens the Brahman comparison**: The One is ABOVE consciousness (Nous); Brahman IS consciousness. This inverts the standard conflation — the Neoplatonist hierarchy places awareness at the SECOND level, not the highest.

3. **Two-truths fills a structural gap**: dvisatya.md was missing despite madhyamaka.md and sunyata.md both referencing it. It is now the hub linking Madhyamaka method (madhyamaka.md) to its ontological content (sunyata.md) and cross-tradition parallels (maya-advaita).

4. **YS 1.2 vikalpa links to apoha**: the Yoga vṛtti-schema independently identifies "conceptual construction without referent" (vikalpa) as the level at which language operates. Dignāga's apoha operates at exactly this level — independent convergence from opposite soteriological frameworks.

5. **Paraconsistent logic closes the logic chain**: saptabhaṅgī → paraconsistent-logic (NOT-equivalent) is now the clearest formulation of why Jain logic is NOT modern paraconsistent logic. The mechanism difference (standpoint-relativization vs ECQ-rejection) is now explicit.

6. **Tarka-prasaṅga distinction is the sharpest new analytic finding**: same logical form (reductio), opposite methodological intent. Tarka confirms a positive conclusion; prasaṅga refutes all positions without endorsing any. This is the deepest difference between Nyāya and Madhyamaka methodology.

### Corpus milestone: 115 concepts across 16 batches + 2 linker passes. 1 unwritten stub (fuzzy-logic).

---

## fuzzy-logic — standalone stub fix (post-Batch 16)

| concept | status | confidence | notes |
|---|---|---|---|
| `fuzzy-logic.md` | done | medium | fills last stub; Zadeh 1965; [0,1] degree-of-membership; vagueness ≠ probability; NOT-equiv saptabhaṅgī + anekāntavāda; is-a-type-of many-valued-logic |

**Corpus milestone: 116 written nodes, 0 unwritten stubs.**

---

### Suggested Batch 17
Completing the Western logic thread (stub now filled; batch focuses on next priorities):

Yogācāra-Madhyamaka depth:
- `santaraksita` — Śāntarakṣita's Yogācāra-Madhyamaka synthesis (Tattvasaṅgraha); the school that tried to merge both
- `prasanga-nagarjuna` — Nāgārjuna's prasaṅga method in detail; distinct from tarka

Jain soteriology depth:
- `nishcaya-vyavahara` — absolute vs conventional standpoints in Jain naya theory (different from the 7-naya schema; Kundakunda's usage in Samayasāra)
- `samyak-darshana` — right faith (first jewel of tri-ratna; companion to charitra and jñāna)

Indian philosophy remaining:
- `vaiseshika-sutra` — the Vaiśeṣika Sūtra (Kaṇāda) as primary text; fills the primary-text gap in dravya-vaisheshika
- `carvaka` — materialist/sceptical school; completes the six-darśana map; denied vyāpti and karma

---

## Chapter accuracy check-up (2026-06-15)

Read all six chapters (01–06) + INDEX end-to-end and re-verified the highest-risk factual claims against live sources (Wikipedia, WisdomLib, JainSquare). Verified accurate (no change needed): TS 5.30 *sat* definition; saptabhaṅgī first systematised by Mallavadin 5th–6th c. (matches Wikipedia exactly); the six skandha types (Niyamasāra); the four mahāvākyas and their Upaniṣad loci; the Nyāya five-fallacy list (NS 1.2.4: savyabhicāra/viruddha/prakaraṇasama/sādhyasama/kālātīta=bādhita); Dignāga/Dharmakīrti/Dharmottara dates; Łukasiewicz 1920 / Zadeh 1965 / Priest LP. All 50 chapter→concept links resolve; no open `??` stuck-markers.

**Corrections made:**
1. **Ch 01 §6.1 (paramāṇu bonding rule)** — was: "bind iff degrees differ by ≥2," with a 3+3 example wrongly explained as "same polarity." Now cites **TS 5.33–5.37** and adds the two missing conditions: the lowest-degree (one-point, *jaghanya*) atom never bonds (TS 5.34), and equal-degree-same-quality atoms don't bond (TS 5.35). The old "iff ≥2" rule was actually wrong — a 1-and-3 pair differs by 2 yet does not bond.
2. **Ch 04 §2.4 + `moksha-advaita.md`** — *Vivekacūḍāmaṇi* was attributed flatly to Śaṅkara; added the modern-scholarship caveat (Comans: attribution "most probably erroneous"). Doctrine stands; authorship flagged as disputed.

**Known limitation (not fixable here):** Python + Graphviz are not installed on this machine, so `graph/graph.svg`/`graph.html` cannot be regenerated. (Correction logged in pass 3 below: `graph/graph.dot` is itself stale, not current.) Run `python graph/build_graph.py` where Python is available.

---

## Linker pass 3 (2026-06-16) — orphan sweep + reciprocity policy

Baseline: HEAD 311c29f. Python unavailable, so the `build_graph.py` edge parser was
re-implemented in awk to audit deterministically (extraction command preserved in the
git history of this commit). Edges parsed: 612 → 621 after fixes.

**Full audit results (before fixes):** 0 duplicate edges, 0 self-loops, 0 invalid edge
types, 0 bidirectional `is-a-type-of`, **0 edge-pairing violations** (all 41 multi-type
ordered pairs are the sanctioned `parallel`/`shares-vocab` + `NOT-equivalent` combo).
The only real defect class: **7 orphan nodes (in-degree 0)** — unreachable on forward
traversal.

**Orphans fixed (7):** one inbound forward edge each, reciprocating a relationship the
orphan's own file already asserts, sourced from a hub node:
`aristotle-logic→aristotle-categories` (shares-vocab), `aristotle-substance→aristotle-ethics`
(shares-vocab), `citta→citta-vritti` (NOT-equiv), `anekantavada→dvisatya` (parallel +
NOT-equiv), `plato-forms→plato-soul` (shares-vocab), `brahman→plotinus-one` (parallel +
NOT-equiv), `alaya-vijnana→tathagata-garbha` (shares-vocab). Post-fix audit: **0 orphans,
0 sinks, 0 stubs, 0 duplicates, 0 pairing violations.** Proven clean.

**Policy decision (recorded in link-candidates.md):** the audit also found ~210 symmetric
edges that exist in only one direction. Under CLAUDE.md §5 ("only forward links are
stored; backlinks are computed with grep") these are **by design, not a backlog** — they
were deliberately NOT mass-reciprocated. The next linker pass should fix only real
connectivity/pairing/direction defects and integrate new concepts, never blanket-add
reciprocals.

**Stale artifact flagged:** `graph/graph.dot` is from ~batch 12 (97 nodes / 485 edges) and
does not reflect the current 116 nodes / 621 edges. It cannot be faithfully regenerated
without Python (hand-writing it would violate §6's "deterministic output, never
hand-drawn"). Left as-is with this flag; regenerate via `python graph/build_graph.py`.

`.linker-state` updated to baseline 311c29f.

---

## Batch 17 concepts (active — started 2026-06-16)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `santaraksita.md` | done | converged, medium; SEP+Enc.Buddhism; MA 1/61-62/91/92; ladder + neither-one-nor-many; conventional Yogācāra/ultimate emptiness |
| 2 | `prasanga-nagarjuna.md` | done | converged, medium; Wikipedia+IEP; VV 29 no-thesis; Prāsaṅgika/Svātantrika split; NOT-equiv tarka |
| 3 | `nishcaya-vyavahara.md` | done | converged, medium; Kundakunda Samayasāra gāthā 11 (bhūtārtha/abhūtārtha); ladder soteriology; anekāntavāda-tension noted; ≠ 7-naya vyavahāra; +1 inbound from naya |
| 4 | `samyak-darshana.md` | done | converged, medium; TS 1.2 + 1.3 Sanskrit FETCHED; tattvārtha-śraddhāna; nisarga/adhigama; gunasthāna 4; +1 inbound from charitra |
| 5 | `vaiseshika-sutra.md` | done | converged, medium; VS 1.1.4 (six padārthas) FETCHED verbatim (Nandalal Sinha); VS 1.1.1-1.1.2 dharma framing; fills primary-text gap; +1 inbound from dravya-vaisheshika |
| 6 | `carvaka.md` | done | converged, medium; IEP+Philosophy Institute; four elements + consciousness-from-matter; vyāpti-rejection + upādhi objection; perception-only; +1 inbound from atman-vedanta |

## Run log — Batch 17 (2026-06-16)

### Startup reconcile
- Working tree clean at start (HEAD fbac9fb, after linker pass 3). No interrupted drafts to reset. progress.md reconciled to git: Batch 16 + fuzzy-logic + linker pass 3 all committed; next queued = suggested Batch 17 (no table existed yet → created it).

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | key source / fetch |
|---|---|---|---|
| santaraksita | converged | medium | SEP + Enc.Buddhism; MA 1/61-62/91/92; ladder (Sautrāntika→Yogācāra→Madhyamaka); neither-one-nor-many; conventional cittamātra / ultimate emptiness |
| prasanga-nagarjuna | converged | medium | Wikipedia (Svātantrika–Prāsaṅgika) + IEP Nāgārjuna; VV 29 "no thesis"; Buddhapālita/Bhāvaviveka/Candrakīrti split |
| nishcaya-vyavahara | converged | medium | Arihanta + JainGPT + gāthā 11/12 translation + Springer 2025 (title/abstract); bhūtārtha/abhūtārtha; ladder soteriology; anekāntavāda-tension noted |
| samyak-darshana | converged | medium | TS 1.2 (*tattvārthaśraddhānaṃ samyagdarśanam*) + TS 1.3 (*tan nisargād adhigamād vā*) FETCHED verbatim (Vijay K. Jain 2018) |
| vaiseshika-sutra | converged | medium | VS 1.1.4 (six padārthas) FETCHED verbatim (Nandalal Sinha 1923) + Wikipedia; dharma = abhyudaya + niḥśreyasa (VS 1.1.1-1.1.2); fills primary-text gap behind dravya-vaisheshika |
| carvaka | converged | medium | IEP + Philosophy Institute; four bhūtas, consciousness-from-matter; vyāpti-impossibility + upādhi objection; perception-only; soul/karma/afterlife denied |

### Verses / primary text directly fetched this batch
- TS 1.2: *तत्त्वार्थश्रद्धानं सम्यग्दर्शनम्* (samyak-darshana)
- TS 1.3: *तन्निसर्गादधिगमाद्वा* (samyak-darshana)
- VS 1.1.4: *dharmaviśeṣaprasūtāt dravyaguṇakarmasāmānyaviśeṣasamavāyānāṃ padārthānāṃ sādharmyavaidharmyābhyāṃ tattvajñānānniḥśreyasam* (vaiseshika-sutra — Nandalal Sinha tr.)
- Samayasāra gāthā 11/12: vyavahāra-naya = abhūtārtha, śuddha/niścaya-naya = bhūtārtha (via translation/commentary, not critical Prakrit edition)

### Integration (no orphans introduced)
Each new node received ≥1 inbound forward edge from an existing hub, reciprocating a relation its own file asserts:
`madhyamaka → santaraksita` (expressed-by); `madhyamaka → prasanga-nagarjuna` (expressed-by);
`naya → nishcaya-vyavahara` (expressed-by); `charitra → samyak-darshana` (shares-vocabulary-with);
`dravya-vaisheshika → vaiseshika-sutra` (part-of); `atman-vedanta → carvaka` (shares-vocabulary-with).

### Mechanical audit (§10)
Awk audit over the 6 new files: **0 edge-pairing violations** — all 12 multi-type ordered pairs are the sanctioned (`structurally-parallel-to`|`shares-vocabulary-with`) + `often-conflated-with-NOT-equivalent` combo. One violation was found and fixed mid-batch: `santaraksita → vijnaptimatrata` carried `historically-influenced-by` + `often-conflated-with-NOT-equivalent` (not sanctioned) → dropped the influence edge (the NOT-equivalent edge already records conventional adoption). No new is-a-type-of cycles, no bidirectional is-a, no new unwritten-stub targets (every edge target is a written file).

### Graph
`graph/graph.dot` NOT regenerated — Python + Graphviz remain unavailable on this machine (flagged since the 2026-06-15 check-up; graph.dot is stale at ~batch 12). Manual stats: **122 written nodes, 0 unwritten stubs**; **668 edges** (grep count over all `## Links`). Regenerate with `python graph/build_graph.py` where Python is available.

### Corpus milestone: 122 concepts across 17 batches + 3 linker passes. 0 unwritten stubs.

### Notable findings
1. **Madhyamaka method-and-school layer now complete**: prasanga-nagarjuna (the Prāsaṅgika method) + santaraksita (the Yogācāra-Svātantrika synthesis) sit on opposite sides of the Prāsaṅgika/Svātantrika divide — both now linked to `madhyamaka`, `tarka`, and each other (parallel + NOT-equivalent). The tarka↔prasaṅga "same form, opposite aim" finding (Batch 16) is now anchored by a dedicated prasaṅga node.
2. **Two-truths structures triangulated across traditions**: nishcaya-vyavahara (Jain/Kundakunda) is now explicitly mapped against dvisatya (Madhyamaka) and maya-advaita (Advaita vyāvahārika/pāramārthika) — parallel two-level *form*, three incompatible ontologies underneath (real pure soul / emptiness / sublatable māyā).
3. **Primary-text gaps closed**: vaiseshika-sutra gives Vaiśeṣika its own Kaṇāda-text anchor (VS 1.1.4 verbatim) behind the previously secondary dravya-vaisheshika/paramanu-vaisheshika files; samyak-darshana completes the ratnatraya (right faith / knowledge-via-jñāna-files / right conduct=charitra) with TS 1.2-1.3 fetched.
4. **Cārvāka is the corpus's epistemic floor**: the only school admitting perception alone and denying vyāpti outright — the negative limit against which Nyāya, Buddhist, Jain, and Mīmāṃsā inference-theories are all defined. Structural-parallel-but-NOT-equivalent to Democritus (materialism that *reasons to* atoms vs materialism that *rejects* inference) is the sharpest new cross-tradition contrast.

### Suggested Batch 18 (names only — no files written)
Western/Greek depth:
- `epicurus-atom` — Epicurean atomism + swerve (clinamen); the materialist-ethics counterpart to Cārvāka and Democritus
- `pyrrhonism` — Greek scepticism; structural parallel to Cārvāka's anti-inference and to Madhyamaka no-thesis (Sextus Empiricus)

Indian remaining:
- `kamalasila` — Śāntarakṣita's student; the *Madhyamakāloka* + Bhāvanākrama; completes the Yogācāra-Svātantrika lineage
- `yoga-darshana` — Patañjali's Yoga as a darśana (aṣṭāṅga); pairs with citta-vritti to complete the Sāṃkhya–Yoga family
- `samkhya-karika` — Īśvarakṛṣṇa's primary text; the Sāṃkhya counterpart to the vaiseshika-sutra primary-text anchor
- `praman-samuccaya` / `pramanavarttika` — primary-text anchors for Dignāga / Dharmakīrti behind dignaga-pramana + hetu-vidya

Linker pass 4:
- Re-run the full awk audit over all 122 files (orphans / pairing / duplicates / is-a direction); integrate Batch 17 nodes' reciprocity only where a real connectivity defect exists; update `.linker-state` to the new baseline HEAD.

---

## Batch 18 concepts (active — started 2026-06-17)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `epicurus-atom.md` | done | converged, medium; SEP+IEP+Wiki(Clinamen); weight + swerve(clinamen) as additions beyond Democritus; swerve not in Epicurus's own surviving texts; +1 inbound from democritus-atom |
| 2 | `pyrrhonism.md` | done | converged, medium; SEP(Sextus)+SEP(Pyrrho); epochē/isostheneia/ataraxia; Ten+Five Modes; Aristocles "no more" tetralemma-formula; vs Academic scepticism; +1 inbound from prasanga-nagarjuna; India-influence claim deliberately not used |
| 3 | `samkhya-karika.md` | done | converged, medium; Wikipedia+IEP; Īśvarakṛṣṇa ~350 CE, 72 vv, Paramārtha 569 CE terminus; 3 pramāṇas; satkāryavāda; 25 tattvas; nirīśvara; kaivalya; +1 inbound from vaiseshika-sutra (satkārya vs asatkārya contrast) |
| 4 | `yoga-darshana.md` | done | converged, medium; Wiki(Yoga Sūtras)+Wiki(Ashtanga); 196 sūtras/4 pādas; YS 1.2; seśvara-Sāṃkhya + Īśvara; aṣṭāṅga (YS 2.29); 5 yamas = 5 Jain mahāvratas (shares-vocab NOT-equiv); +1 inbound from samkhya-karika |
| 5 | `epicurus-ethics.md` | done | converged, medium; SEP+IEP; refined hedonism = ataraxia/aponia (katastematic>kinetic); 3-way desire classification; tetrapharmakos; "death is nothing to us"; vs Aristotle eudaimonia, vs nirvāṇa, vs Pyrrhonist ataraxia; +1 inbound from epicurus-atom |
| 6 | `kamalasila.md` | done | converged, medium; Wiki(Kamalaśīla)+Wiki(Bhāvanākrama); c.740-795; Śāntarakṣita's student; 3 Bhāvanākrama + Madhyamakāloka + Tattvasaṃgrahapañjikā; Samye Debate gradual-vs-sudden (vs Moheyan); +1 inbound from santaraksita |

## Run log — Batch 18 (2026-06-17)

### Startup reconcile
- Working tree clean at start (HEAD b1d52b6, after the graph-rendering commits). No interrupted drafts. progress.md reconciled to git: Batch 17 + 3 linker passes + graph-toolchain work all committed; next queued = suggested Batch 18 (table created at session start).
- **Python relocated:** the winget user-scope interpreter is at `C:\Users\bhomi\AppData\Local\Programs\Python\Python312\python.exe` (the bare `python`/`py` commands are shadowed by the Windows Store app-execution alias and fail). Graphviz `dot` is at `C:\Program Files\Graphviz\bin\dot.exe` (not on PATH). Use the full paths to regenerate.

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | key source / fetch |
|---|---|---|---|
| epicurus-atom | converged | medium | SEP "Epicurus" + IEP "Epicurus" + Wikipedia "Clinamen"; weight + swerve as additions beyond Democritus; swerve only in Lucretius/Cicero |
| pyrrhonism | converged | medium | SEP "Sextus Empiricus" + SEP "Pyrrho"; epochē/isostheneia/ataraxia; Ten+Five Modes; Aristocles "no more" formula; vs Academic scepticism |
| samkhya-karika | converged | medium | Wikipedia "Sāṃkhyakārikā" + IEP "Sāṃkhya"; Īśvarakṛṣṇa ~350 CE; 72 vv; Paramārtha 569 CE terminus; 3 pramāṇas; satkāryavāda; 25 tattvas; nirīśvara; kaivalya |
| yoga-darshana | converged | medium | Wikipedia "Yoga Sūtras of Patañjali" + "Ashtanga"; 196 sūtras/4 pādas; seśvara-Sāṃkhya + Īśvara; aṣṭāṅga (YS 2.29); 5 yamas = 5 mahāvratas |
| epicurus-ethics | converged | medium | SEP + IEP "Epicurus"; ataraxia/aponia, katastematic>kinetic; 3-way desire classification; tetrapharmakos; death-is-nothing |
| kamalasila | converged | medium | Wikipedia "Kamalaśīla" + "Bhāvanākrama"; Śāntarakṣita's student; Bhāvanākrama/Madhyamakāloka/Tattvasaṃgrahapañjikā; Samye Debate gradual-vs-sudden |

### Integration (no orphans introduced)
Each new node received ≥1 inbound forward edge from an existing hub, reciprocating a relation its own file asserts:
`democritus-atom → epicurus-atom` (parallel + NOT-equiv); `prasanga-nagarjuna → pyrrhonism` (parallel + NOT-equiv);
`vaiseshika-sutra → samkhya-karika` (parallel + NOT-equiv, satkārya vs asatkārya); `samkhya-karika → yoga-darshana` (shares-vocab + NOT-equiv);
`epicurus-atom → epicurus-ethics` (shares-vocab); `santaraksita → kamalasila` (structurally-parallel-to).

### Mechanical audit (§10)
- Edge-type tally over the 6 new files: only valid §5 types (expressed-by, historically-influenced-by, part-of, shares-vocabulary-with, structurally-parallel-to, often-conflated-with-NOT-equivalent).
- All multi-type ordered pairs are the sanctioned (`structurally-parallel-to`|`shares-vocabulary-with`) + `often-conflated-with-NOT-equivalent` combo; no is-a-type-of used in the new files (so no direction/cycle risk); `part-of: madhyamaka` (kamalasila) stands alone.
- **0 unwritten stubs**: build_graph.py reports 128 nodes = 128 concept files, so every edge target resolves to a written file.

### Graph (regenerated — toolchain now working)
`python graph/build_graph.py` ran clean: **128 nodes, 727 edges**. Wrote `graph/graph.dot`, `graph/graph.html` (interactive force-graph). `graph/graph.svg` rendered via `dot.exe` (361 KB). All three artifacts now current at the Batch-18 state.

### Corpus milestone: 128 concepts across 18 batches + 3 linker passes. 0 unwritten stubs.

### Notable findings
1. **Greek Hellenistic ethics triangulated against Indian liberation**: epicurus-ethics's *ataraxia* (tranquillity within one mortal life, soul dispersing at death) is now mapped as structurally-parallel-but-NOT-equivalent to both nirvāṇa (cessation of *rebirth* under anattā) and Pyrrhonist ataraxia (same goal, opposite method — correct-doctrine vs suspend-all-doctrine). The tetrapharmakos ↔ Four Noble Truths "diagnose-and-cure" parallel is drawn and explicitly bounded.
2. **The two Greek atomisms are now distinct nodes**: epicurus-atom vs democritus-atom split exactly on *weight* and the *swerve* (clinamen) — the swerve converting Democritean determinism to indeterminism, and routinely (wrongly) read as anticipating quantum randomness (flagged in prose, not as an edge, to keep the graph stub-free).
3. **Sāṃkhya and Yoga now have their primary-text anchors**: samkhya-karika (Īśvarakṛṣṇa) behind prakriti/purusha/guna-samkhya, and yoga-darshana (Patañjali) behind citta-vritti — paralleling the vaiseshika-sutra anchor from Batch 17. The satkāryavāda (Sāṃkhya) vs asatkāryavāda/ārambhavāda (Vaiśeṣika) causal split is the sharpest new intra-āstika contrast; the 5-yama = 5-mahāvrata terminological identity (NOT doctrinal) is the sharpest new cross-tradition false-cognate guard.
4. **Yogācāra-Svātantrika-Madhyamaka lineage completed**: kamalasila joins santaraksita; the Samye Debate (gradual vs sudden) is documented with its contested historiography (Tibetan vs Chinese sources disagree on the victor) rather than asserting an outcome.

### Suggested Batch 19 (names only — no files written)
Indian primary-text anchors (continuing the Batch 17–18 anchor programme):
- `nyaya-sutra` — Gautama's Nyāya Sūtra as primary text behind pramana-nyaya / anumana-nyaya / hetvabhasa / tarka
- `pramana-samuccaya` — Dignāga's primary text behind dignaga-pramana + apoha
- `pramanavarttika` — Dharmakīrti's primary text behind hetu-vidya + dharmottara
- `yogasutra` — Patañjali's text as a *primary-text* node distinct from the yoga-darshana school overview (if warranted), or `mimamsa-sutra` (Jaimini) behind mimamsa-pramana

Greek/Hellenistic depth:
- `stoicism` — the Stoa as a school (physics/logic/ethics) behind the existing stoic-logos node; oikeiōsis, apatheia (vs Epicurean ataraxia)
- `plato-forms` is written; consider `aristotle-substance` companions already done — `parmenides-being` (the eternal One/Being; tempting Brahman/sat conflation target)

Linker pass 4:
- Full awk/parser audit over all 128 files (orphans / pairing / duplicates / is-a direction); integrate Batch 18 reciprocity only where a real connectivity defect exists; update `.linker-state`.

---

## Batch 19 concepts (active — started 2026-06-17)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `nyaya-sutra.md` | done | converged, medium; Wikipedia+IEP; Gautama/Akṣapāda ~200 CE; 5 adhyāyas; 16 padārthas; 4 pramāṇas; 5-member syllogism; vāda/jalpa/vitaṇḍā; apavarga; +1 inbound from pramana-nyaya |
| 2 | `pramana-samuccaya.md` | done | converged, medium; EoB+Tibetan Buddhist Enc.+EoB(Dignāga); Dignāga c.480-540; 6 chapters; 2 pramāṇas/2 objects; kalpanāpoḍha; trairūpya; apoha; Tibetan reconstruction; +1 inbound from dignaga-pramana |
| 3 | `pramanavarttika.md` | done | converged, medium; Wikipedia+SEP(Dharmakīrti); c.600-660; commentary on Pramāṇasamuccaya; 4 chapters; arthakriyā/causal-efficacy criterion; momentariness; trairūpya; causal apoha; Sautrāntika→Yogācāra; +1 inbound from dharmottara |
| 4 | `stoicism.md` | done | converged, medium; SEP+IEP; Zeno/Chrysippus; logic-physics-ethics; pneuma/logos + fate + ekpyrosis; virtue-only good, indifferents, apatheia; apatheia(engagement) vs ataraxia(withdrawal); +1 inbound from stoic-logos |
| 5 | `parmenides-being.md` | done | converged, medium; SEP+Wikipedia; c.515-450 BCE; On Nature, Truth/Opinion; "it is and cannot not be"; sēmata of to eon; change/plurality illusory; Eleatics; vs brahman + vs sat (permanence vs permanence-in-change); +1 inbound from plato-forms |
| 6 | `mimamsa-sutra.md` | done | converged, medium; Wikipedia+darśana-site aggregation; Jaimini ~300-200 BCE; 12 adhyāyas/60 pādas; MS 1.1.2 codanā-lakṣaṇo dharmaḥ; apauruṣeyatva; śabda-nityatva; apūrva; Śābara-bhāṣya; +1 inbound from mimamsa-pramana |

## Run log — Batch 19 (2026-06-17, continuous with Batch 18)

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | key source / fetch |
|---|---|---|---|
| nyaya-sutra | converged | medium | Wikipedia "Nyaya Sutras" + IEP "Nyāya"; Gautama/Akṣapāda ~200 CE; 16 padārthas; 4 pramāṇas; 5-member syllogism; apavarga |
| pramana-samuccaya | converged | medium | EoB "Pramāṇasamuccaya" + Tibetan Buddhist Enc. + EoB "Dignāga"; Dignāga c.480-540; 6 chapters; 2 pramāṇas/2 objects; trairūpya; apoha; Sanskrit reconstructed from Tibetan |
| pramanavarttika | converged | medium | Wikipedia "Pramanavarttika" + SEP "Dharmakīrti"; c.600-660; commentary on Pramāṇasamuccaya; arthakriyā; momentariness; causal apoha; Sautrāntika→Yogācāra |
| stoicism | converged | medium | SEP + IEP "Stoicism"; Zeno/Chrysippus; logic-physics-ethics; pneuma/logos + fate + ekpyrosis; virtue-only; apatheia(engagement) vs ataraxia(withdrawal) |
| parmenides-being | converged | medium | SEP "Parmenides" + Wikipedia; c.515-450 BCE; Truth/Opinion; "it is and cannot not be"; sēmata; change/plurality illusory; Eleatics |
| mimamsa-sutra | converged | medium | Wikipedia "Purva Mimamsa Sutras" + darśana-site aggregation; Jaimini ~300-200 BCE; 12 adhyāyas; MS 1.1.2; apauruṣeyatva; apūrva; Śābara-bhāṣya |

### Primary-text anchor programme (the spine of Batches 17–19)
With this batch, every major Indian darśana in the corpus now has its own primary-text node behind the doctrine files:
**Nyāya → nyaya-sutra**, **Vaiśeṣika → vaiseshika-sutra** (B17), **Sāṃkhya → samkhya-karika** (B18), **Yoga → yoga-darshana** (B18), **Mīmāṃsā → mimamsa-sutra**, **Buddhist pramāṇavāda → pramana-samuccaya (Dignāga) + pramanavarttika (Dharmakīrti)**. Each anchor uses `expressed-by:` toward its worked-out doctrine files and receives one reciprocal inbound (`part-of:` or `historically-influenced-by:`) so no orphan is introduced.

### Integration (no orphans introduced)
`pramana-nyaya → nyaya-sutra` (part-of); `dignaga-pramana → pramana-samuccaya` (part-of); `dharmottara → pramanavarttika` (historically-influenced-by); `stoic-logos → stoicism` (part-of); `plato-forms → parmenides-being` (historically-influenced-by); `mimamsa-pramana → mimamsa-sutra` (part-of).

### Mechanical audit (§10)
- Only valid §5 edge types in the 6 new files (expressed-by, historically-influenced-by, part-of, shares-vocabulary-with, structurally-parallel-to, often-conflated-with-NOT-equivalent).
- Multi-type ordered pairs all the sanctioned (parallel|shares-vocab) + NOT-equivalent combo; no is-a-type-of used in the new files; `part-of` and `expressed-by` between an anchor and its doctrine file run in *opposite* ordered directions (different ordered pairs), so no pairing violation.
- **0 unwritten stubs**: build_graph.py reports **134 nodes = 134 concept files**; every edge target resolves.

### Graph (regenerated)
`python graph/build_graph.py` clean: **134 nodes, 768 edges**. graph.dot + graph.html refreshed; graph.svg rendered via dot.exe (381 KB).

### Corpus milestone: 134 concepts across 19 batches + 3 linker passes. 0 unwritten stubs.

### Notable findings
1. **The pramāṇa-tradition rivalry is now anchored at the root-text level**: nyaya-sutra (4 pramāṇas, realist about universals) vs pramana-samuccaya/pramanavarttika (2 pramāṇas, apoha-nominalist) vs mimamsa-sutra (apauruṣeya śabda, svataḥ-prāmāṇya). The Buddhist two-text lineage (Dignāga → Dharmakīrti, historically-influenced-by) and the Dharmakīrti → Dharmottara commentary chain are now explicit edges.
2. **Greek "being/tranquillity" comparanda sharpened against India**: parmenides-being is the strongest Brahman-analogue in the Greek corpus, but split from both Brahman (Being is deduced, not realised consciousness/ātman) and Jain sat (Being excludes change vs sat = permanence-in-change). stoicism completes the Hellenistic ethics pair — apatheia (engagement/virtue) vs Epicurean ataraxia (withdrawal/pleasure) — both now distinct nodes.
3. **mimamsa-sutra's apauruṣeyatva is the unique scripture-ontology in the corpus**: an authorless, eternal, self-validating Veda needing no divine author — contrasted at the root-text level with Nyāya's reliable-speaker/God-grounded śabda.

### Suggested Batch 20 (names only — no files written)
- `samkhya-karika` is done; consider `ishvarakrishna` only if a person-node is warranted (probably not — fold into samkhya-karika).
- `epicurus-atom`/`epicurus-ethics` done; Hellenistic remainder: `cynicism` (Diogenes; the ascetic-freedom school behind Stoicism) or `neoplatonism` (Proclus/Iamblichus behind plotinus-one).
- Indian primary-text anchors remaining: `brahma-sutra` (Bādarāyaṇa, behind brahman / atman-vedanta / the Vedānta sub-schools); `yogasutra-text` only if distinct from yoga-darshana (likely fold in).
- Buddhist: `mulamadhyamakakarika` (Nāgārjuna's root text behind madhyamaka / sunyata / catuskoti / dvisatya) — a major missing primary-text anchor.
- Linker pass 4: full audit over all 134 files; update `.linker-state`.

---

## Batch 20 concepts (active — started 2026-06-17, continuous)

Primary-text anchors for the remaining keystone texts (the entire Jain corpus rests on the Tattvārtha Sūtra yet had no node; MMK/Brahmasūtra/Abhidharmakośa anchor large existing clusters).

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `tattvartha-sutra.md` | done | converged, medium; Wikipedia+Jainpedia/aggregation+corpus TS verses; Umāsvāti 2nd-5th c.; first Sanskrit Jain text; both sects; 10 chapters; TS 1.1 ratnatraya; TS 1.4 tattvas; Sarvārthasiddhi/Tattvārthabhāṣya; +1 inbound from tattva-jain |
| 2 | `mulamadhyamakakarika.md` | done | converged, medium; Wikipedia+SEP(Nāgārjuna); c.150-250 CE; ~450 vv/27 chapters; svabhāva-refutation via prasaṅga+catuṣkoṭi; 8 negations; MMK 24.18; two truths; +1 inbound from sunyata |
| 3 | `brahma-sutra.md` | done | converged, medium; Wikipedia+Vedānta-site aggregation; Bādarāyaṇa; 555 sūtras/4 adhyāyas; BS 1.1.1/1.1.2; prasthānatrayī; one text → Advaita/Viśiṣṭādvaita/Dvaita; parallel-but-opposite to mimamsa-sutra (uttara vs purva); +1 inbound from brahman |
| 4 | `abhidharmakosa.md` | done | converged, medium; Wikipedia+EoB; Vasubandhu 4th-5th c.; karika(8ch/~600vv Vaibhasika)+bhasya(Sautrantika critique; 9th ch refutes pudgala); 75 dharmas; Paramartha/Xuanzang+Tibetan; +1 inbound (part-of) from abhidharma |

## Batch 21 concepts (active — started 2026-06-17, continuous)

School-anchor completion: the three Vedānta sub-schools behind `brahma-sutra`, plus school-overview nodes behind already-written doctrine files (Yogācāra behind alaya-vijnana/tathagata-garbha; the two Greek schools behind stoicism/plotinus-one).

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `advaita-vedanta.md` | done | converged, medium; SEP(Śaṅkara)+Wiki; Śaṅkara c.700-750 systematiser; Brahman alone real/maya-avidya; atman=Brahman; 3 truths; nirguna/saguna; moksha=epistemic shift via mahavakyas; jivanmukti; crypto-Buddhist charge; historically-influenced-by brahma-sutra |
| 2 | `vishishtadvaita.md` | done | converged, medium; Wiki(Vishishtadvaita)+Wiki(Ramanuja); Rāmānuja c.1017-1137; qualified non-dualism; 3 reals Isvara/cit/acit; sarira-saririn; rejects maya; moksha=participation via bhakti+prapatti; weak independence (2 Wiki) noted |
| 3 | `dvaita-vedanta.md` | done | converged, medium; Wiki+NewWorldEnc; Madhva 1238-1317; Tattvavada dualism; svatantra/paratantra; panca-bheda; bimba/pratibimba; 3 soul-classes incl. eternal damnation; structurally-parallel-to+NOT-equiv jiva |
| 4 | `yogacara.md` | done | converged, medium; Wiki+EoB; Maitreya/Asanga/Vasubandhu; school-overview distinct from vijnaptimatrata doctrine node; 8 consciousnesses/trisvabhava/asraya-paravrtti; historically-influenced-by abhidharmakosa; vs madhyamaka |
| 5 | `cynicism.md` | done | converged, medium; IEP+Wiki; Antisthenes/Diogenes(c.412-323)/Crates; virtue-only/kata physin/autarkeia; Crates taught Zeno; parallel+NOT-equiv stoicism + aparigraha; +1 inbound added to stoicism |
| 6 | `neoplatonism.md` | done | converged, medium; Wiki+SEP(Plotinus); Plotinus 204-270; Enneads/Porphyry/Iamblichus/Proclus; 3 hypostases One/Nous/Soul; emanation+return+henosis; expressed-by plotinus-one; vs advaita-vedanta |

## Run log — Batch 21 (2026-06-17, continuous with Batch 20)

### Startup reconcile
- Working tree clean at start (HEAD 2af2456, after the Batch-20 anchor commits). No interrupted drafts. progress.md reconciled to git: Batch 20 had `abhidharmakosa` still **pending** → completed as the first action of this session (commit f1e1de7), closing Batch 20. Then opened Batch 21.
- Discovery: `vijnaptimatrata`, `alaya-vijnana`, `tathagata-garbha`, `plotinus-one` already existed as **doctrine** nodes; their parent **school-overview** nodes (`yogacara`, `neoplatonism`) did not — confirming the school-vs-doctrine split as the Batch-21 theme.

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review) — plus Batch-20 closeout (abhidharmakosa)

| concept | status | confidence | key source / fetch |
|---|---|---|---|
| advaita-vedanta | converged | medium | SEP "Śaṅkara" + Wikipedia "Advaita Vedanta"; 8th-c. systematiser; māyā/avidyā; ātman=Brahman; 3 truths; nirguṇa/saguṇa; mokṣa=epistemic; jīvanmukti; māyāvāda/crypto-Buddhist charge |
| vishishtadvaita | converged | medium | Wikipedia "Vishishtadvaita" + "Ramanuja" (weakly independent — same platform; corroborated by brahma-sutra.md); Śrī Bhāṣya; cit/acit as body of Brahman; bhakti/prapatti |
| dvaita-vedanta | converged | medium | Wikipedia "Dvaita Vedanta" + New World Enc. "Madhva"; svatantra/paratantra; pañca-bheda; bimba/pratibimba; eternal damnation; vs Jain jīva pluralism |
| yogacara | converged | medium | Wikipedia "Yogachara" + Encyclopedia of Buddhism "Yogachara"; Maitreya/Asaṅga/Vasubandhu; 8 consciousnesses; trisvabhāva; āśraya-parāvṛtti; vs Madhyamaka |
| cynicism | converged | medium | IEP "Cynics" + Wikipedia "Cynicism"; Diogenes c.412-323; autarkeia/askēsis/anaideia/parrhēsia; Crates→Zeno; vs Stoicism + aparigraha |
| neoplatonism | converged | medium | Wikipedia "Neoplatonism" + SEP "Plotinus"; Enneads/Porphyry; One/Nous/Soul; proodos/epistrophē/henosis; vs Advaita emanation/return |

### Integration (no orphans; reciprocal inbounds added)
- Three Vedānta sub-schools each `historically-influenced-by: brahma-sutra`; interlinked by the sanctioned `structurally-parallel-to` + `often-conflated-with-NOT-equivalent` pair (advaita↔vishishtadvaita↔dvaita); dvaita cross-links to Jain `jiva` (pluralism, theistic-dependent vs non-theistic-independent).
- `yogacara` `expressed-by: vijnaptimatrata` + `alaya-vijnana`; `historically-influenced-by: abhidharmakosa` (same author Vasubandhu — reciprocates the Batch-20 anchor); parallel+NOT-equiv `madhyamaka`.
- `cynicism`: parallel+NOT-equiv `stoicism` + `aparigraha`; reciprocal inbound `stoicism → cynicism` (historically-influenced-by) added to stoicism.md.
- `neoplatonism` `expressed-by: plotinus-one`; `historically-influenced-by: plato-forms`; parallel+NOT-equiv `advaita-vedanta` (links the two batch clusters).

### Mechanical audit (§10)
- Only valid §5 edge types in all new files (expressed-by, historically-influenced-by, part-of, structurally-parallel-to, often-conflated-with-NOT-equivalent). No `is-a-type-of` used → no direction/cycle risk. All multi-type ordered pairs are the sanctioned (parallel|shares-vocab)+NOT-equivalent combo.
- One stub introduced mid-draft (`sarvastivada-time` in abhidharmakosa) was caught and removed before commit to preserve the **0-stub** invariant.
- **0 unwritten stubs**: build_graph.py reports **144 nodes = 144 concept files**; every edge target resolves.

### Graph (regenerated)
`python graph/build_graph.py` clean: **144 nodes, 825 edges**. graph.dot + graph.html refreshed; graph.svg rendered via dot.exe (411 KB).

### Corpus milestone: 144 concepts across 21 batches + 3 linker passes. 0 unwritten stubs.

### Notable findings
1. **The three Vedānta sub-schools are now a complete, mapped triad** behind `brahma-sutra`: one root text → Advaita (only nirguṇa Brahman real; world = māyā; mokṣa = identity) → Viśiṣṭādvaita (souls/matter real *modes* of Brahman; mokṣa = participation) → Dvaita (five eternal differences; souls eternally *distinct & dependent*; mokṣa = service). The corpus's clearest case of one authority generating mutually exclusive readings — now drawn as parallel+NOT-equivalent edges rather than asserted in prose.
2. **Dvaita is the closest Vedānta analogue to Jain pluralism** (real, eternal, graded plurality of distinct souls) — but the NOT-equivalent guard is sharp: Madhva's souls are eternally God-dependent (svatantra/paratantra), Jain jīvas independent in a creator-less cosmos. A new, defensible Vedānta↔Jain cross-edge.
3. **The two great Mahāyāna schools are now both anchored**: madhyamaka (root text mulamadhyamakakarika, B20) and yogacara (this batch), with the "real exists/conventional doesn't" vs "real doesn't/conventional does" contrast and the Śāntarakṣita synthesis. `yogacara` was kept strictly to the *school* layer (lineage, eight consciousnesses, trisvabhāva) to avoid duplicating the existing `vijnaptimatrata` doctrine node.
4. **The Greek school layer deepened**: `cynicism` supplies Stoicism's missing ancestor (Crates→Zeno) and a genuine — but carefully bounded — parallel to Jain aparigraha; `neoplatonism` supplies the school behind the existing `plotinus-one` and links the Greek and Advaita clusters via the emanation/return ≈ Brahman/māyā parallel.

### Suggested Batch 22 (names only — no files written)
Vedānta depth (now that the three schools exist):
- `vivarta` vs `parinama` — the appearance-transformation vs real-transformation theories of causation dividing Advaita from Viśiṣṭādvaita/Sāṃkhya
- `nimbarka` / `vallabha` — the remaining bhedābheda Vedānta sub-schools (Dvaitādvaita / Śuddhādvaita), if warranted
- `bhakti` — devotion as a soteriological path (central to Viśiṣṭādvaita + Dvaita; contrast jñāna-mārga and karma-mārga)
Buddhist depth:
- `trisvabhava` — the three-natures doctrine as its own node (forward-referenced in yogacara prose)
- `santaraksita` is written; consider `madhyamakalankara` (his text) or the `bodhisattva` ideal
Greek/Hellenistic remainder:
- `aristotle-substance` companions: `actuality-potentiality` or `four-causes`; or `pyrrhonism` is done — consider `academic-skepticism`
- Linker pass 4: full audit over all 144 files (orphans / pairing / duplicates / is-a direction); update `.linker-state`.

---

## Batch 22 concepts (active — started 2026-06-17, continuous)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `vivartavada.md` | done | contested, medium; rope-snake analogy; Nakamura/Hacker/Nicholson attribution debate; inbound from advaita-vedanta |
| 2 | `parinamavada.md` | done | converged, medium; BS 2.2.26; 3-variant table; satkāryavāda base; inbound from vishishtadvaita |
| 3 | `bhakti.md` | done | converged, medium; ŚvetUp 6.23; three mārgas; Rāmānuja vs Madhva; Jain pūjā NOT-equiv; inbound from vishishtadvaita+dvaita-vedanta |
| 4 | `bodhisattva.md` | done | converged, medium; bodhicitta; 6 pāramitās; arhat contrast; inbound from yogacara |
| 5 | `four-causes.md` | done | converged, medium; Physics II.3 / Metaphysics V.2; telos NOT in pratītyasamutpāda; inbound from aristotle-substance |
| 6 | `academic-skepticism.md` | done | converged, medium; Arcesilaus epochē + Carneades pithanon; 266-90 BCE; vs pyrrhonism NOT-equiv; inbound from pyrrhonism |

## Run log — Batch 22 (2026-06-17, continuous)

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | key source / note |
|---|---|---|---|
| vivartavada | contested | medium | Nakamura/Hacker/Nicholson: post-Śaṅkara; rope-snake analogy; paired with parinamavada |
| parinamavada | converged | medium | BS 2.2.26; 3-variant table (Sāṃkhya/Viśiṣṭādvaita/Śaiva Siddhānta); satkāryavāda base |
| bhakti | converged | medium | ŚvetUp 6.23; three mārgas; Rāmānuja bhakti+prapatti vs Madhva grace; Jain pūjā NOT-equiv |
| bodhisattva | converged | medium | bodhicitta; 6 pāramitās; Theravāda/Mahāyāna scope difference; arhat contrast |
| four-causes | converged | medium | Physics II.3 / Metaphysics V.2; hyle/morphe/efficient/telos; telos absent from pratītyasamutpāda |
| academic-skepticism | converged | medium | Arcesilaus epochē + Carneades pithanon; 266-90 BCE; Academics vs Pyrrhonists NOT-equiv |

### Graph: 150 nodes, 867 edges (regenerated)

---

## Batch 23 concepts (complete — 2026-06-17, continuous session)

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `satkaryavada.md` | done | converged, medium; SK 9 Sanskrit directly fetched; 5-argument table; pariṇāma+vivarta sub-variants; inbound from samkhya-karika |
| 2 | `asatkaryavada.md` | done | converged, medium; ārambhavāda; 3 causal conditions; pot/clay contrast; Buddhist NOT-in-either; inbound from nyaya-sutra |
| 3 | `jnana-marga.md` | done | converged, medium; BG 4.38; śravaṇa/manana/nididhyāsana (BṛU 4); three-path table; Advaita priority; inbound from advaita-vedanta |
| 4 | `karma-marga.md` | done | converged, medium; BG 2.47-49 + 3.19; nishkama karma; karma-in-path ≠ karma-as-binding; inbound from avatara-vedanta |
| 5 | `pancha-mahabhuta.md` | done | converged, medium; TU 2.1-2.5 emergence sequence; 5/4/4-element cross-tradition table; mahābhūta≠paramāṇu; inbound from prakriti-samkhya |
| 6 | `theravada.md` | done | converged, medium; Tipitaka 3-basket structure; arhat ideal; Vibhajjavāda; 5-column Mahāyāna contrast table; inbound from abhidharma |

## Run log — Batch 23 (2026-06-17, continuous)

### Startup reconcile
Context resumed mid-batch: satkaryavada.md and asatkaryavada.md were written but uncommitted. Hub files (samkhya-karika.md, nyaya-sutra.md) were read at end of prior context. Committed all 4 files first, then continued with #3-6.

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | key source / note |
|---|---|---|---|
| satkaryavada | converged | medium | SK 9 Sanskrit (*asadakaraṇāt...satkāryam*) fetched directly; 5-argument pañca-kāraṇa; pariṇāma/vivarta sub-variants; ChU 6.2.1 precursor |
| asatkaryavada | converged | medium | ārambhavāda; Nyāya 3 conditions (antecedence/invariability/unconditionality); Buddhist neither-satkāryavāda-nor-asatkāryavāda noted |
| jnana-marga | converged | medium | BG 4.38; śravaṇa/manana/nididhyāsana rooted in BṛU 4; Śaṅkara's priority; "most difficult" characterisation |
| karma-marga | converged | medium | BG 2.47-49 + 3.19; nishkama karma; karma-mārga vs karma-as-binding-force distinction flagged explicitly |
| pancha-mahabhuta | converged | medium | TU 2.1-2.5 emergence sequence (ākāśa→vāyu→agni→ap→pṛthvī); Buddhist four-element divergence (MN 140 Dhātuvibhaṅga); mahābhūta≠paramāṇu distinction |
| theravada | converged | medium | Tipitaka (Vinaya/Sutta/Abhidhamma); arhat vs bodhisattva divide; Vibhajjavāda origin (3rd c. BCE Sri Lanka); 5-column Mahāyāna contrast table |

### Orphan prevention: all 6 concepts received ≥1 inbound forward edge from an existing hub before commit.

### Graph (regenerated after Batch 23)
`python graph/build_graph.py` → **156 nodes, 909 edges** (SVG rendered via dot.exe). +6 new nodes, +42 new edges vs Batch 22 (150/867).

### Notable findings
1. **Causal-theory cluster complete**: satkāryavāda (effect pre-exists) + asatkāryavāda (effect is new) + pratītyasamutpāda (neither) now form a three-way cross-tradition comparison on the single deepest question of Indian causal theory. The Buddhist "neither" position is the clearest example of a philosophical middle-path that is neither simple pre-existentism nor simple novelty.
2. **The three Hindu soteriological paths are complete**: bhakti (Batch 22) + jñāna-mārga + karma-mārga together form the classical triad. All three are now cross-linked and contrasted in each file's table.
3. **pancha-mahabhuta exposes a genuine 5-vs-4 divergence**: the Hindu/Buddhist element-count difference is not terminological but substantive — ākāśa's status (primary vs derived) reflects a deep difference in cosmological ontology. This is the kind of structural difference the corpus exists to document.
4. **theravada completes the Buddhist school layer**: yogācāra (Mahāyāna; Batch 21) + madhyamaka + theravada now form the Buddhist triad. The arhat/bodhisattva divide is the deepest structural difference and is now documented with a five-column contrast table.

### Corpus milestone: 156 concepts across 23 batches + 3 linker passes. 0 unwritten stubs.

---

## Linker Pass 4 (2026-06-18)

### Baseline
HEAD ab68a53 (Batch 23 close). Edges parsed via awk: **909**.

### Audit (before fixes)
- 0 duplicate edges, 0 self-loops, 0 invalid edge types, 0 bidirectional is-a-type-of, 0 edge-pairing violations
- **1 orphan** (in-degree 0): `neoplatonism` — Batch 21 added it with only out-edges
- **8 low-in-degree nodes (in-degree 1)**: mulamadhyamakakarika, theravada, trisvabhava, four-causes, pancha-mahabhuta, parmenides-being, adharma-dravya (not fixed — single is a legitimate hub minimum), naigama-naya (ditto)
- 2 sanctioned-pair completions needed: sabda-pramana had `often-conflated-NOT-equiv: shruta-jnana` without the partner `structurally-parallel-to`

### Edges added: 26 new edges across 20 files

**Orphan fixed:**
| file | edge added |
|---|---|
| plotinus-one | part-of: neoplatonism |

**Low-in-degree nodes raised:**
| node | before | after | via |
|---|---|---|---|
| mulamadhyamakakarika | 1 | 3 | madhyamaka + prasanga-nagarjuna both part-of MMK |
| theravada | 1 | 3 | anatta-buddhist + nirvana-buddhist both part-of theravada |
| trisvabhava | 1 | 3 | vijnaptimatrata part-of + yogacara expressed-by trisvabhava |
| four-causes | 1 | 3 | aristotle-ethics expressed-by + aristotle-logic shares-vocab |
| pancha-mahabhuta | 1 | 5 | akasha-dravya + pudgala each: shares-vocab + NOT-equiv |
| parmenides-being | 1 | 5 | brahman + sat each: structurally-parallel + NOT-equiv |
| tattvartha-sutra | 2 | 4 | bandha + asrava both part-of tattvartha-sutra |
| satkaryavada | 2 | 4 | parinamavada + vivartavada both is-a-type-of satkaryavada |

**Cross-tradition additions:**
- sabda-pramana: structurally-parallel-to shruta-jnana (completes the NOT-equiv pair)
- cynicism: structurally-parallel-to + NOT-equiv tapas (Greek askēsis ≈ Jain austerity, but one-lifetime-secular vs multi-life-soteriological)
- stoicism: structurally-parallel-to + NOT-equiv yoga-darshana (both disciplined practice for freedom-from-passion, different metaphysics and scope)

### Post-fix audit
0 orphans, 0 duplicates, 0 bidir is-a, 0 pairing violations. Proven clean.

### Graph (regenerated)
`python graph/build_graph.py` + `dot.exe` clean: **156 nodes, 935 edges**. graph.dot/html/svg refreshed.

`.linker-state` updated to baseline ab68a53.

---

### Suggested Batch 24 (names only — no files written)
Filling doctrinal and tradition gaps revealed by Batch 23:
- `upanishad` — school-overview for the Upaniṣads as a textual tradition (presently cited but not written as a node)
- `vaishnavism` — Vaiṣṇava bhakti tradition (connects Viśiṣṭādvaita, Dvaita, avatāra, bhakti into one umbrella)
- `shaivism` — Śaiva tradition (Śaiva Siddhānta; pariṇāmavāda variant; connects to advaita-vedanta)
- `dhamma` — the Pali *dhamma* (Theravāda usage) vs Sanskrit *dharma* (Hindu/Jain) — same word, very different semantic fields
- `arhat` — the Theravāda arhat ideal as its own node (forward-referenced in bodhisattva.md and theravada.md)
- `tanha` — Pali craving/thirst; the second Noble Truth's mechanism; links dukkha → samsara → nibbana

---

## Batch 24 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `upanishad.md` | done | converged, medium; Olivelle 1998 + Radhakrishnan 1953; 12 mukhya, 4 mahāvākyas, 4 Vedānta sub-schools |
| 2 | `vaishnavism.md` | done | converged, medium; 4+1 sampradāyas; avatāra doctrine; bhakti; NOT-equiv Advaita |
| 3 | `shaivism.md` | done | converged, medium; 4 schools; pariṇāmavāda; Śakti; NOT-equiv Advaita māyāvāda |
| 4 | `dhamma.md` | done | converged, medium; 4-sense table; NOT-equiv dharma-dravya; anattā grounding |
| 5 | `arhat.md` | done | converged, medium; SN 22.110 FETCHED; 4-stage ladder, 10-fetter table; NOT-equiv bodhisattva |
| 6 | `tanha.md` | done | converged, medium; SN 56.11 (corpus-prior fetch); 3-type table; 12-nidāna position; parallel kaṣāya/āsrava |

## Run log — Batch 24 (2026-06-18)

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| upanishad | converged | medium | Olivelle 1998 OUP + Radhakrishnan 1953; 12 mukhya by Veda; 4 mahāvākyas with texts; 4 Vedānta sub-schools table |
| vaishnavism | converged | medium | Wikipedia "Vaishnavism" + "Gaudiya Vaishnavism" + "Pancharatra"; 4+1 sampradāyas; avatāra; NOT-equiv Advaita |
| shaivism | converged | medium | Wikipedia + IEP "Kashmiri Shaiva Philosophy"; 4 schools; pariṇāmavāda (Śaiva Siddhānta); NOT-equiv Advaita māyāvāda |
| dhamma | converged | medium | Wisdom Library + Wikipedia + JustBuddha; 4-sense table; NOT-equiv dharma-dravya; vibhava-taṇhā as aversion |
| arhat | converged | medium | SN 22.110 FETCHED (Access to Insight); 4-stage ladder; 10-fetter table; NOT-equiv bodhisattva; parallel siddha |
| tanha | converged | medium | SN 56.11 (corpus-prior fetch; dukkha.md); Wikipedia "Taṇhā"; 3-type table; 12-nidāna 8th link; parallel kaṣāya/āsrava |

### Notable findings this batch

1. **Hindu tradition layer now structurally complete**: upanishad.md (scriptural foundation) + brahma-sutra.md (systematization) + advaita-vedanta / vishishtadvaita / dvaita-vedanta + vaishnavism + shaivism — the entire āstika doctrinal pyramid is now covered. The Upaniṣad → Brahmasūtra → three Vedānta schools → two major devotional traditions is a legible chain across concept files.

2. **The Advaita NOT-equivalent cluster is now fully mapped**: advaita-vedanta.md + maya-advaita.md + vivartavada.md on one side; vaishnavism.md + shaivism.md + parinamavada.md on the other. Three separate traditions (Jain, Vaiṣṇava, Śaiva) each explicitly reject Advaita māyāvāda for overlapping but distinct reasons — now all documented.

3. **Dhamma 4-sense disambiguation is the sharpest polysemy case in the corpus**: the single word "dhamma / dharma" covers (a) Buddhist teaching, (b) natural law, (c) mental phenomena (Abhidhamma), (d) medium of motion (Jain) — four completely different semantic fields under one root. The NOT-equivalent edge to dharma-dravya is now the most striking "same word, utterly different thing" edge in the graph.

4. **Buddhist path now fully threaded**: dukkha (1st Noble Truth) → tanha (2nd Noble Truth / 8th nidāna) → pratityasamutpada (12-link chain) → arhat (goal of Eightfold Path) → nirvana-buddhist / theravada. Every node in this chain has a dedicated file.

5. **SN 22.110 fetch**: canonical arahant definition directly retrieved from Access to Insight (Pali text + Walshe translation). This is the most authoritative source in the corpus for the arhat concept.

### Graph (final state of this run)
`python graph/build_graph.py` clean: **162 nodes, 969 edges**.
`"C:\Program Files\Graphviz\bin\dot.exe" -Tsvg graph/graph.dot -o graph/graph.svg` — SVG rendered.
graph.dot / graph.html / graph.svg all refreshed.

### Suggested Batch 25 (names only — no files written)
Filling remaining tradition and doctrinal gaps:

Buddhist depth:
- `four-noble-truths` — explicit file for the core Buddhist doctrinal structure (presently distributed across dukkha.md, tanha.md, arhat.md)
- `nibbana-theravada` — Theravāda's specific Pali account of nibbāna (vs the Sanskrit nirvāṇa in nirvana-buddhist.md, which covers all schools)
- `paticcasamuppada-pali` — Pali-specific treatment of dependent origination with Pali nidāna names and SN 12 citations

Hindu / Vedic:
- `rta` — Vedic cosmic order/truth; precursor to dharma in both Hindu and Buddhist senses
- `shakti` — Śaiva/Śākta divine power; fills the Śakti concept that shaivism.md references but does not write
- `lingam` — the Śiva symbol; Liṅgāyat theology; connects shaivism to soteriology

Cross-tradition:
- `ahimsa-jain-buddhist` — systematic comparison now that all three ahiṃsā files (Jain, Buddhist, Vedic) are written
- `liberation-comparison` — or let the graph do the work via existing links (prefer the latter)

## Batch 25 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `four-noble-truths.md` | done | converged, medium; SN 56.11 + MN 141 FETCHED; 4-truth table, 12-aspect analysis, cross-tradition diagnostic comparison |
| 2 | `nibbana-theravada.md` | done | converged, medium; Ud 8.1 formula; two-type table (sa-/anupādisesa), extinction vs. unconditioned-dhamma debate |
| 3 | `paticcasamuppada-pali.md` | done | converged, medium; imasmiṃ sati formula; 12-nidāna Pali table; three-lifetime structure; Theravāda vs. Madhyamaka |
| 4 | `rta.md` | done | converged, medium; PIE etymology; 3-domain table; Varuṇa guardian; ṛta→dharma transition; cross-cultural parallels |
| 5 | `shakti.md` | done | converged, medium; Devī Māhātmya; Śiva-Śakti 4-school table; NOT-equiv Sāṃkhya-prakṛti and Advaita-māyā |
| 6 | `lingam.md` | done | converged, medium; jyotirliṅga cosmogony; 5-level table; Liṅgāyat iṣṭaliṅga reform; NOT-equiv Brahman |

## Run log — Batch 25 (2026-06-18)

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| four-noble-truths | converged | medium | SN 56.11 + MN 141 FETCHED; 4-truth table + 12-aspect analysis; action-per-truth prescription; cross-tradition diagnostic comparison |
| nibbana-theravada | converged | medium | Ud 8.1 formula (*ajātaṃ abhūtaṃ akataṃ asaṅkhataṃ*); Iti 43-44 two-type table; extinction vs. asaṅkhata-dhamma debate; Theravāda vs. Mahāyāna split |
| paticcasamuppada-pali | converged | medium | *imasmiṃ sati idaṃ hoti* formula; 12 Pali nidāna table (avijjā→jarāmaraṇa); three-lifetime structure; cessation chain = nibbāna; Theravāda vs. Madhyamaka |
| rta | converged | medium | PIE etymology; ~390 RV occurrences; 3-domain scope (cosmic/moral/ritual); Varuṇa as guardian; ṛta→dharma transition; parallel Asha/Logos/Dao |
| shakti | converged | medium | Devī Māhātmya (~5th–6th c. CE); Śiva-Śakti 4-school table (Kashmir Śaivism/Śaiva Siddhānta/Śāktism/Purāṇic); NOT-equiv prakṛti; NOT-equiv māyā-advaita |
| lingam | converged | medium | jyotirliṅga cosmogony (Śiva Purāṇa); 5-level table (cosmogonic/metaphysical/cosmological/soteriological/devotional); Liṅgāyat iṣṭaliṅga reform (Basavaṇṇa); NOT-equiv Brahman |

### Texts directly fetched this session

- SN 56.11 (*Dhammacakkappavattana Sutta*), Access to Insight — 4 noble truths defined; 3-round parivatta analysis
- MN 141 (*Saccavibhaṅga Sutta*), Access to Insight — Sāriputta's analysis; 4-action prescriptions (pariññeyya etc.)
- Udāna 8.1, Access to Insight — nibbāna unconditioned formula (*ajātaṃ abhūtaṃ akataṃ asaṅkhataṃ*)
- Wikipedia "Nirvana (Buddhism)" — two-type distinction; Buddhaghosa; Mahāyāna vs. Theravāda
- Wikipedia "Pratītyasamutpāda" — Pali conditional formula; 12 nidānas; three-lifetime structure
- Wikipedia "Rta" — PIE etymology; RV occurrence count; Varuṇa; transition to dharma; cross-cultural parallels
- Wikipedia "Shakti" — Śiva-Śakti; three goddesses; Devī Māhātmya; māyā role; Śākta schools
- Wikipedia "Lingam" — etymology; symbolic vs. phallic debate; colonial distortion; jyotirliṅga; iṣṭaliṅga

### Graph (final state)

`python graph/build_graph.py` clean: **168 nodes, 1007 edges**.
`"C:\Program Files\Graphviz\bin\dot.exe" -Tsvg graph/graph.dot -o graph/graph.svg` — SVG rendered.
graph.dot / graph.html / graph.svg all refreshed.

**Milestone: 1000+ edges.** The graph crossed 1,007 edges this batch — the density of cross-tradition links is now greater than 6 edges per node on average.

### Notable findings this batch

1. **Buddhist soteriological arc now fully threaded in Pali**: dukkha.md (1st Noble Truth) → tanha.md (2nd) → four-noble-truths.md (framework) → paticcasamuppada-pali.md (causal machinery) → nibbana-theravada.md (3rd Noble Truth content) → arhat.md (the achieved goal). Every link in the Theravāda liberation chain has a dedicated file.

2. **four-noble-truths action-prescription is the sharpest doctrinal distinction**: each truth does not merely describe a fact but prescribes an action (pariññeyya / pahātabba / sacchikātabba / bhāvetabba). No other tradition's equivalent framework (Jain 7 tattvas, Advaita avidyā-jñāna) has this explicit per-truth praxis assignment. This is now documented.

3. **nibbāna's unconditioned formula (Ud 8.1) defuses the "mere extinction" reading**: the argument structure (*"if there were no unconditioned, there would be no escape from the conditioned"*) logically implies nibbāna is not mere negation. The file captures both the formula and the ongoing scholarly debate (Stcherbatsky vs. Bhikkhu Bodhi), avoiding false resolution.

4. **paticcasamuppada-pali fills the primary-Pali gap in pratityasamutpada.md**: the earlier file (Batch 4) acknowledged "SN 12 not directly fetched." The new file directly fetches the *imasmiṃ sati* formula and provides the three-lifetime structure as Abhidhamma orthodoxy alongside the minority moment-to-moment reading.

5. **Vedic section opened with ṛta**: the first concept in the "Vedic" index section. ṛta as the cosmological predecessor to both dharma (Hindu) and dhamma (Buddhist natural law) creates new cross-tradition edges that were previously missing. The Varuṇa-as-guardian pattern (gods obey ṛta rather than commanding it) is structurally unique in ancient religious thought.

6. **Śakti resolves the shaivism.md forward-reference**: shaivism.md (Batch 24) referenced Śakti as Śiva's creative power without writing the concept. shakti.md fills this and adds the critical NOT-equivalent edges to both Sāṃkhya-prakṛti and Advaita-māyā — the most important doctrinal distinctions in Śaiva/Śākta theology.

7. **lingam-liṅgāyat connects symbol to soteriology**: the Liṅgāyat *iṣṭaliṅga* reform (Basavaṇṇa, 12th c.) is the most radical anti-caste, anti-Brahmin, body-as-temple application of Śaiva theology in the corpus. It shows how an abstract doctrinal claim (Śiva = nirguṇa absolute) generates a concrete social reform (no intermediaries; every body sacred).

### Corpus milestone: 168 concepts across 25 batches

### Suggested Batch 26 (names only — no files written)

Buddhist epistemology depth:
- `dharmottara-nyayabindu` — Dharmakīrti's *Nyāyabindu* with Dharmottara's commentary; fills the Kashmir Śaivism / Buddhist epistemology interface
- `pratyaksha-buddhist` — Buddhist perception theory specifically (vs. Jain pratyakṣa and Nyāya pratyakṣa); fills the perception gap across all three epistemologies

Hindu theology:
- `vishnu` — Viṣṇu as supreme deity in Vaiṣṇavism; fills the vaishnavism.md forward reference
- `brahma` — Brahma (the creator god) as distinct from Brahman (Advaita absolute) and from the Jain non-creator cosmology

Logic / philosophy:
- `pramana-comparison` — systematic comparison table across Nyāya (4), Mīmāṃsā (5-6), Jain (2), Buddhist/Dignāga (2) — or let the graph do it via existing links
- `inference-comparison` — or let the graph handle it

Vedic:
- `yajna` — Vedic sacrifice; the ritual underpinning of ṛta; Mīmāṃsā's apauruṣeyatva claim depends on yajna being primary
- `agni` — Vedic fire deity; the ritual mediator; structurally parallel to the Jain dharma-dravya as enabler

---

## Batch 26 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `vishnu.md` | done | converged, medium; BhP 1.2.11 triple-designation; ṣaḍ-bhaga; 3-school Brahman-relation table; avatāra doctrine |
| 2 | `brahma.md` | done | converged, medium; Muṇḍaka Up 1.1.1; Hiraṇyagarbha myth; Brahmā≠Brahman 3-row table; 2 temples; Prajāpati succession |
| 3 | `yajna.md` | done | converged, medium; BG 3.11 Sanskrit quoted; 3-layer table (Brāhmaṇa/Upaniṣadic/BG); Mīmāṃsā apauruṣeya; ahiṃsā conflict |
| 4 | `agni.md` | done | converged, medium; RV 1.1 + 1.164.46; 3-function table (Havyavāhana/hotṛ/ṛtasya-gopā); 3 cosmic forms; dharma-dravya parallel noted weak |
| 5 | `pratyaksha-buddhist.md` | done | converged, medium; PS 3 + NB 1.4 Sanskrit quoted; 4-type table; 3-tradition comparison; NOT-equiv Jain+Nyāya |
| 6 | `dharmottara-nyayabindu.md` | done | converged, medium; 3-chapter table; NB/ṭīkā Sanskrit survival; Kashmir Śaivism Pratyabhijñā interface table; svalakṣaṇa vs self-recognition debate |

## Run log — Batch 26 (2026-06-19)

### Concepts completed: 6 / 6 (0 blocked, 0 needs-opus-review)

| concept | status | confidence | note |
|---|---|---|---|
| vishnu | converged | medium | BhP 1.2.11 triple-designation; ṣaḍ-bhaga; 3-school Brahman-relation table (Advaita/Viśiṣṭādvaita/Dvaita); NOT-equiv Brahman |
| brahma | converged | medium | Muṇḍaka Up 1.1.1; Hiraṇyagarbha myth; Brahmā≠Brahman/Brāhmaṇa 3-term table; Bhṛgu + Śiva curse; 2 temples; Prajāpati succession |
| yajna | converged | medium | BG 3.11 Sanskrit; 3-layer table (Brāhmaṇa/Upaniṣadic/BG); Mīmāṃsā apauruṣeya; ṛta connection; ahiṃsā conflict |
| agni | converged | medium | RV 1.1 + 1.164.46; 3-function table (Havyavāhana/hotṛ/ṛtasya-gopā); 3 cosmic forms; dharma-dravya parallel noted weak |
| pratyaksha-buddhist | converged | medium | PS 3 + NB 1.4 Sanskrit; 4-type table; 3-tradition comparison table; NOT-equiv Nyāya savikalpaka + Jain unmediated scope |
| dharmottara-nyayabindu | converged | medium | 3-chapter table; NB/ṭīkā Sanskrit survival; Kashmir Śaivism Pratyabhijñā interface table (4 issues); Yogācāra reading |

### Linkage pass (post-batch)
- Fixed incorrect `is-a-type-of: vaishnavism` → `part-of: vaishnavism` in vishnu.md (direction rule)
- Added forward links to Batch 26 concepts in 8 existing files: vaishnavism, rta, mimamsa-pramana, dharmottara, dignaga-pramana, pramanavarttika, vishishtadvaita, dvaita-vedanta

### Graph (final state)
`python graph/build_graph.py` clean: **174 nodes, 1050 edges**.
SVG rendered with `"C:\Program Files\Graphviz\bin\dot.exe" -Tsvg graph/graph.dot -o graph/graph.svg`.
graph.dot / graph.html / graph.svg all refreshed.

### Notable findings this batch

1. **Hindu Trinity now fully mapped**: Brahmā (creator, brahma.md), Viṣṇu (preserver, vishnu.md), Śiva (lingam.md, shaivism.md) each have dedicated files. The Trimurti concept connects them; but only Viṣṇu and Śiva sustain major devotional worship — Brahmā's marginality is documented with its textual explanation.

2. **Brahmā≠Brahman is the corpus's most common confusion target**: the same Sanskrit root *bṛh* produces three distinct terms (Brahmā/Brahman/Brāhmaṇa); brahma.md documents all three levels explicitly with a 3-row disambiguation table.

3. **Yajña is the operational spine of the Vedic/Mīmāṃsā/ṛta cluster**: yajna.md connects rta.md (cosmic order), agni.md (ritual mediator), mimamsa-pramana.md (apauruṣeya grounding), and karma-marga.md (BG reinterpretation) in a single concept. Four existing files now link to it.

4. **Buddhist pratyakṣa definitions now primary-text grounded**: PS 3 and NB 1.4 quoted with Sanskrit. This is the first time perception theory in the corpus has verse-level textual grounding comparable to the Jain TS fetches.

5. **Kashmir Śaivism / Buddhist epistemology interface documented**: dharmottara-nyayabindu.md maps the Pratyabhijñā–Buddhist debate on four philosophical issues (self, perception, universals, consciousness). This is the only place in the corpus where the two traditions' direct historical confrontation is systematically documented.

### Suggested Batch 27 (names only — no files written)

Hindu theology completing the Trimurti/Vedic cluster:
- `sarasvati` — goddess of knowledge, arts, wisdom; paired with Brahmā; one of the Tridevi
- `lakshmi` — goddess of prosperity; Viṣṇu's śakti/consort; named in vaishnavism.md but not yet written
- `trimurti` — the Brahmā/Viṣṇu/Śiva triad as a cosmological schema; is it original or a later synthesis?

Kashmir Śaivism depth:
- `pratyabhijna` — the Recognition (Pratyabhijñā) school of Utpaladeva/Abhinavagupta; fills the interface dharmottara-nyayabindu.md opens
- `spanda` — the "vibration" doctrine (another key Kashmir Śaiva concept, alongside Pratyabhijñā)

Remaining Buddhist concepts:
- `bodhicitta` — the awakening mind; central to Mahāyāna ethics (referenced in bodhisattva.md)
- `madhyamaka-logic` — the Prāsaṅga method as a distinct logical technique (distinguished from standard anumāna)

---

## Graph toolchain installed + rendered (2026-06-16)

The long-standing "Python + Graphviz not on this machine" blocker is **resolved**. Installed
via winget: **Python 3.12.10** (user scope) + **Graphviz 15.0.0** + the `graphviz` pip package.
`graph/build_graph.py` now renders successfully:
- `graph/graph.svg` — static Graphviz render (rankdir=LR; node colour = tradition family, size = degree; edge style = link type: solid structural / dashed cross-tradition / dotted NOT-equivalent).
- `graph/graph.html` — **interactive Cytoscape** view (force-directed cose layout; the recommended way to explore 122 nodes). Self-contained; opens in any browser.
- `graph/graph.dot` — refreshed deterministic intermediate (was stale at ~batch 12 / 97 nodes; now current at **122 nodes, 670 edges**). Supersedes the "graph.dot is stale" flag from linker pass 3.

**Authoritative counts: 122 nodes, 670 edges** (build_graph.py's own parser; the earlier 668
figure was a grep alternation under-count).

### Two real defects fixed in build_graph.py (deterministic, idempotent preserved)
1. **Front-matter parser bug (`YAML_FIELD_RE`)**: used `\s*`, and `\s` matches newlines, so any
   concept with an empty field (e.g. a blank `term_devanagari:`) immediately above a populated
   one would *swallow the next line's value*. This silently blanked `tradition` on
   aristotle-logic / aristotle-categories / plato-soul / stoic-logos. Fixed to `[ \t]*`.
2. **Tradition→colour mapping (§6 "colour = tradition")**: the old exact-match dict keyed on
   `"Jain"`, `"Greek"` etc. matched almost nothing, because front-matter values carry diacritics
   and parentheticals (`"Nyāya-Vaiśeṣika"`, `"Buddhist (Madhyamaka / Prāsaṅgika)"`,
   `"cross-tradition (...)"`). Replaced with a diacritic-folding keyword classifier
   (`tradition_family`) covering 10 families + cross-tradition. **Post-fix: 0 nodes fall through
   to default white** (verified). Family counts: Jain 55, Buddhist 24, Vedānta 9, Greek 9,
   Nyāya-Vaiśeṣika 7, cross-tradition 7, Modern/Western 5, Sāṃkhya-Yoga 4, Mīmāṃsā 1, Cārvāka 1.

To regenerate anywhere: `python graph/build_graph.py` (needs the `graphviz` pip pkg for SVG; the
HTML render needs only Python). High-res PNG on demand: `dot -Tpng graph/graph.dot -o out.png`
(PNGs are gitignored — they run to tens of MB at full resolution).

### Render style switched to Obsidian-like force-graph (2026-06-16, per user request)
The boxed-cluster Cytoscape view was rejected. `graph.html` now uses **vasturiano/force-graph**
(d3-force on canvas): dark background, small dots that cluster organically by link density,
colour = tradition (vivid dark-bg palette), size = degree, labels under nodes that fade with
zoom, thin grey links, hover highlights a node's neighbourhood. `graph.svg` switched to a
matching force-directed dark render (no boxes). `render_cytoscape` replaced by `render_force_graph`.

**Tradition grouping added (2026-06-17):** per-tradition foci on a ring drive a d3
clustered-force layout (forceX/forceY toward each family's focus + forceManyBody + forceCollide),
so same-tradition dots gather into their own neat circular cluster while edges still cross between
them — Obsidian look, now spatially grouped. Labels are always-on with a dark halo (strokeText)
for readability. SVG mirrors this via **fdp + invisible per-tradition clusters** (grouped regions,
no visible boxes); graph.dot uses `layout=fdp`.

**Blank-screen fix (self-contained HTML):** the CDN `d3-force@3/dist/d3-force.min.js` is NOT a
self-contained bundle — it `require`s d3-quadtree/d3-dispatch/d3-timer, so `forceManyBody`/
`forceCollide` threw in-browser → blank page. Fixed by (a) **vendoring force-graph locally** at
`graph/vendor/force-graph.min.js` (referenced relatively, no CDN), and (b) replacing the d3 foci
forces with a **plain-JS custom cluster force** that uses only force-graph's bundled charge/link
forces. The HTML is now fully offline-safe; an on-page error message shows if the vendored lib is
ever missing. `graph/vendor/` is committed so the repo renders anywhere.

**Label readability (2026-06-17):** added a plain-JS **collision force** with a label-aware
spacing radius (`SPACE(n) = max(dotRadius+6, 7 + name.length*3.4)`) so dots never sit closer than
their labels are wide; eased the cluster pull (0.32) and widened the focus ring so collision can
spread them. Because constant-size labels can never *all* fit non-overlapping at a full zoom-to-fit
of 122 nodes (the fit-zoom cancels any extra graph-space spacing), labels now behave like Obsidian:
hub labels (degree > 11) always show; the rest appear once you **zoom in** past ~1.15× or on hover.
SVG `sep` bumped to `+18` for matching static spacing.

---

## Teaching-layer run — Chapter 07 (2026-06-19)

**Task:** Complete Jain coverage in the human-readable `chapters/` teaching layer. This run did **Ch 07 only**, end-to-end (per scope-lock in the task brief). Chapters are reading views, NOT graph nodes — `build_graph.py` does not scan `chapters/`.

### New atomic concept files written (each: own commit + graph regen)
| concept | status | confidence | key source |
|---|---|---|---|
| `ratnatraya` | converged | medium | TS 1.1 FETCHED (Vijay K. Jain 2018 + Pūjyapāda); singular-mārga + simultaneity; Wikipedia + Jainpedia independent confirm; Buddhist triratna flagged as false-friend |
| `nikshepa` | converged | medium | TS 1.5 FETCHED (*nāmasthāpanādravyabhāvatastannyāsaḥ*); Pūjyapāda jīva/tīrthaṅkara examples; WisdomLib defs page 2nd signal; distinguished from naya |

Graph: **174 → 176 nodes** (1050 → 1061 edges). `build_graph.py` ran clean (Graphviz `dot` not on PATH, so `graph.dot`/`graph.html` regenerated, `graph.svg` unchanged — same as prior batches).

### Chapter authored
- `chapters/07-jain-knowledge.md` — "How the Soul Knows: The Five Jñānas." Sections: ratnatraya frame (which jewel) → pramāṇa/upayoga instruments → TS 1.9 five-fold ladder → **the parokṣa/pratyakṣa inversion (§4, the chapter spine)** → mati / śruta / avadhi / manaḥparyāya / kevala, each with its fetched verse → nikṣepa disambiguation layer → summary visual → Check yourself. Matches Ch 03 format (per-concept `→ concept file` links, fetched-verse quotes w/ citations, ⚠️ Conflation alerts, `{#anchor}` tags, How-to-use intro, Check-yourself close, medium-ceiling source note).
- Conflation alerts drawn: ratnatraya ≠ Buddhist triratna; Jain pratyakṣa ≠ Nyāya ≠ Dignāga; mati-jñāna ≠ Dignāga pratyakṣa; avadhi ≠ kevala; manaḥparyāya ≠ avadhi; kevala-jñāna ≠ Vedānta sarvajñatva.
- `chapters/INDEX.md` updated: Ch 07 row + 9 new primary concept mappings (+ pramāṇa cross-ref to Ch 07).

### Nothing blocked or needs-opus-review. All cited; no from-scratch translations.

### Plan for Ch 08–10 (one line each; NOT started this run)
- **Ch 08 — Jain Ethics & Ascetic Practice:** recap mahāvratas; new files `anuvrata`, `sallekhana` (flag contested), and `samayika`/`pratikramana`/`shad-avashyaka` (write only if ≥2 independent sources, else `blocked`).
- **Ch 09 — The Jain Cosmos & Six Substances in Full:** new files `astikaya`, `utsarpini-avasarpini`; give the four table-row dravyas (dharma/adharma/ākāśa/kāla) real sections.
- **Ch 10 — Jain Holy Beings, Sects, Texts & History:** new files `namokara` (+`upadhyaya`,`sadhu`), `mahavira`, `parshvanatha`, `digambara`, `svetambara`, `samayasara`+`kundakunda`, `nishchaya-vyavahara`, `punya`+`papa`, 8 karma-prakṛtis detail node, `ajivika`.

---

## Teaching-layer run — Chapters 08 & 09 (2026-06-19)

**Task:** "make the next two chapters and make sure they land on the right sub folders." Both Ch 08 and Ch 09 are Jain-tradition → authored in **`chapters/jain/`** (the correct origin subfolder), matching the Ch 01/02/03/07 placement. Executed the repo's own Ch 08–10 plan for the first two chapters, end-to-end, each concept committed separately + graph regenerated (Ch 07 precedent).

### New atomic concept files written (each: own commit + graph regen)
| concept | status | confidence | key source |
|---|---|---|---|
| `anuvrata` | converged | medium | TS 7.1 Sanskrit FETCHED + TS 7.2 (partial/total) English; 12-vow śrāvaka scheme (5 aṇuvrata+3 guṇavrata+4 śikṣāvrata); Wikipedia/Britannica 2nd signal |
| `sallekhana` | **contested** | medium | TS 7.22 Sanskrit+English FETCHED (*māraṇāntikī sallekhanāṃ joṣitā*); sallekhanā≠suicide divergence table (Jain doctrine / Rajasthan HC 2015 ban / SC stay) |
| `shad-avashyaka` | converged | medium | Āvaśyaka Sūtra six (sāmāyika/caturviṃśati-stava/vandana/pratikramaṇa/kāyotsarga/pratyākhyāna); Śvetāmbara rite-list vs Digambara lay ṣaṭ-karma |
| `astikaya` | converged | medium | TS 5.1 Sanskrit + Pūjyapāda on *kāya*=manifoldness-of-pradeśa FETCHED; pañcāstikāya; kāla=anastikāya; Dravyasaṃgraha+Pañcāstikāyasāra signals |
| `utsarpini-avasarpini` | converged | medium | kālacakra: 2 half-cycles × 6 aras; 24 Tīrthaṅkaras/half (Ṛṣabha ara3, Mahāvīra ara4); present 5th ara; karma-bhūmi scope |

Decision: the daily-practice trio (sāmāyika/pratikramaṇa/shad-avashyaka) was written as **one** umbrella file `shad-avashyaka` (sāmāyika + pratikramaṇa covered as members) rather than three thin files — atomic per the six-fold scheme, and avoids stubby duplication.

### Linkage pass (post-astikaya)
Added correct child→parent `is-a-type-of: astikaya` edges to the five extended substances (jīva/pudgala/dharma-dravya/adharma-dravya/ākāśa) — direction rule respected (edge lives in the child's file). Fixed two mistyped `loka`→`loka-jain` link targets (removed a phantom stub node; 182→181).

### Chapters authored (both in chapters/jain/)
- `chapters/jain/08-jain-ethics.md` — "Living the Vows." Spine: **ethics is physics** (every vow is a move in the karma economy). §§: cāritra frame → five vows (TS 7.1) → mahāvrata/aṇuvrata two-intensities + 12 lay vows (TS 7.2) → kaṣāya→saṃvara/nirjarā mechanism (TS 6.5) → tapas (TS 9.19) + dhyāna (TS 9.28) → ṣaḍāvaśyaka daily loop → sallekhanā (TS 7.22). Conflation alerts: ahiṃsā cross-tradition; **Jain tapas ≠ Hindu tapas** (empties vs fills); **sallekhanā ≠ suicide**.
- `chapters/jain/09-jain-cosmos.md` — "The Architecture of the Real." §§: dravya (TS 5.38) → sat as being=change-in-permanence (TS 5.30) → **forces anekāntavāda** → astikāya property-cut (TS 5.1; 6≠5 count) → six substances one-by-one (TS 5.17/5.18/5.22/5.39) → loka-puruṣa + siddha-śilā as mokṣa's literal address → kālacakra (6 aras / 24 Tīrthaṅkaras). Conflation alerts: 6 dravya ≠ 5 astikāya; **dharma-dravya ≠ physics field/ether/spacetime** (prime-directive payoff); ākāśa ≠ Vaiśeṣika ether; kālacakra ≠ yuga/avatāra.
- `chapters/INDEX.md` updated: Ch 08 + Ch 09 rows; new primary-concept mappings + cross-refs.

### Graph
`build_graph.py` clean: **176 → 181 nodes** (1061 → 1097 edges). SVG re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`. graph.dot/html/svg refreshed each concept.

### Nothing blocked or needs-opus-review. All cited; TS verses fetched where available; no from-scratch translations.

### Plan for Ch 10 (unchanged — NOT started this run)
- **Ch 10 — Jain Holy Beings, Sects, Texts & History:** `namokara` (+`upadhyaya`,`sadhu`), `mahavira`, `parshvanatha`, `digambara`, `svetambara`, `samayasara`+`kundakunda`, `nishchaya-vyavahara`, `punya`+`papa`, 8 karma-prakṛtis detail, `ajivika`.

---

## Teaching-layer run — Chapter 10 (2026-06-19)

**Task:** "go ahead with the next chapter." Executed the repo's own Ch 10 plan end-to-end: 14 new atomic concept files (each its own commit + graph regen), then the chapter authored in **`chapters/jain/`** (Jain-tradition → correct origin subfolder, matching Ch 01/02/03/07/08/09), then INDEX + graph + this log. This **completes the Jain chapter arc (Ch 01–10)**.

### New atomic concept files written (each: own commit + graph regen)
| concept | status | confidence | key source |
|---|---|---|---|
| `namokara` | converged | medium | Ṇamokāra/pañca-namaskāra mantra; 5 lines + cūlikā; names no individual/god (aspirational); Hāthīgumphā + 200–100 BCE inscriptions (Wiki + Jainworld/CulturalSamvaad) |
| `upadhyaya` | converged | medium | 4th parameṣṭhī; āgama-teacher; 25 qualities; 108-attribute mālā sum (Wiki + Jainsite + JCGB) |
| `sadhu` | converged | medium | 5th/broadest parameṣṭhī; mahāvrata threshold; 27/28 mūla-guṇa (sect diff) (Wiki + Jainsite + Digambara-monk) |
| `parshvanatha` | converged | medium | 23rd tīrthaṅkara; earliest historically-accepted; cāturyāma 4-vow (Wiki + Britannica) |
| `mahavira` | converged | medium | 24th/last; reformer NOT founder; contested-dating table; Nigaṇṭha Nātaputta attestation (Wiki + Britannica) |
| `digambara` | converged | medium | sky-clad; aparigraha-root → 5 differences; Bhadrabāhu famine-migration; contested origin (Wiki + Britannica + MDPI) |
| `svetambara` | converged | medium | white-clad; softer aparigraha → 5 mirror-positions; Pāṭaliputra+Valabhī canon; Mallinātha female (Wiki + history + Jainpedia) |
| `kundakunda` | converged | medium | foundational Digambara philosopher-monk; contested dating; niścaya/vyavāhara device; 4 -sāra works (Wiki + Jainpedia + Vijay K. Jain ed.) |
| `samayasara` | converged | medium | Kundakunda's chief text; 439 gāthās, 10 chapters; gold/iron-chain puṇya-pāpa; same-soul-two-standpoints (Wiki + Vijay K. Jain ed.) |
| `nishchaya-vyavahara` | **contested** | medium | two-standpoints; co-equal-realism vs niścaya-privileging table; NOT-equiv Buddhist/Advaita two-truths — prime-directive (Wiki + JainGPT + SEP) |
| `punya` | converged | medium | merit/śubha karma; āsrava+bandha subtype; gold-chain; 7-vs-9 tattva (Wiki + Jainsite + hinduwebsite) |
| `papa` | converged | medium | demerit/aśubha karma; iron-chain; mahāvrata-violation sources + kaṣāya root (Wiki + Jainsite + hinduwebsite) |
| `karma-prakriti` | converged | medium | 8 mūla-prakṛti; **TS 8.4 Sanskrit FETCHED** (Vijay K. Jain 2018); 4 ghāti/4 aghāti; mohanīya linchpin; 148-subtype flagged traditional |
| `ajivika` | converged | medium | Gosāla's niyati fatalism; precise inverse of Jain agency (niyati-alone vs 1-of-5-samavāya); hostile-source caveat (Wiki + Britannica/UPSC) |

### TS verse directly fetched this batch
- **TS 8.4** (karma-prakṛti): *ādyo jñānadarśanāvaraṇavedanīyamohanīyāyurnāma gotrāntarāyāḥ* — the eight nature-bondages (Vijay K. Jain 2018 / WisdomLib)

### Chapter authored (in chapters/jain/)
- `chapters/jain/10-jain-holy-beings.md` — "Holy Beings, Sects, Texts & History." Thread: **Jainism is non-theistic and its history is human effort, not divine intervention.** §§: pañca-parameṣṭhī via the Ṇamokāra mantra → Pārśva/Mahāvīra (reformer-not-founder) → Digambara/Śvetāmbara schism (one root: does aparigraha require nudity? → 5 consequences) → Kundakunda/Samayasāra/niścaya-vyavāhara → puṇya/pāpa + 8 karma-prakṛti (TS 8.4) → Ājīvika (niyati vs puruṣārtha). Conflation alerts: parameṣṭhī ≠ gods/petition; Mahāvīra ≠ founder; sect-breakaway direction; **niścaya/vyavāhara ≠ Buddhist/Advaita two-truths (prime-directive)**; karma ≠ scoreboard/ledger; Jain ≠ fatalist + Ājīvika-as-enemies'-caricature.
- `chapters/INDEX.md` updated: Ch 10 row + 18 primary/cross-ref concept mappings.

### Graph
`build_graph.py` clean: **181 → 196 nodes** (1097 → 1187 edges). +15 nodes = 14 new concepts + 1 new unwritten stub (`mohaniya`, forward-linked from karma-prakriti). SVG re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; graph.dot/html/svg refreshed each concept.

### Edge-typing self-corrections made during the run (per §5)
- mahavira→parshvanatha: dropped a non-sanctioned `historically-influenced-by` + `often-conflated-with-NOT-equivalent` double-edge; kept `historically-influenced-by` (conflation already carried from parshvanatha's side).
- digambara→samayasara: removed wrong-direction `part-of` (a sect is not part of a text) → `shares-vocabulary-with: kundakunda`.
- samayasara→punya: re-typed mis-applied `often-conflated-with-NOT-equivalent` → `shares-vocabulary-with`.
- karma-prakriti→karma-vargana: re-typed awkward `aggregates-into` → `shares-vocabulary-with`.

### Nothing blocked or needs-opus-review. All cited; one TS verse fetched; no from-scratch translations.

### Jain arc complete (Ch 01–10)
Ontology (01) · epistemology (02) · soteriology (03) · cross-tradition (04–06, comparative) · knowledge/five jñānas (07) · ethics (08) · cosmos (09) · holy beings/sects/texts/history (10). The Jain teaching layer is now end-to-end.

### Suggested next (NOT started)
- **Ch 11 — The Vedānta family** (cross-tradition deep-dive): brahman · ātman-vedānta · māyā-advaita · mokṣa-advaita · the Advaita/Viśiṣṭādvaita/Dvaita split · avatāra-vedānta. Most files already exist; this is a chapter-authoring run, not a concept run.
- **Ch 12 — The Buddhist family**: pratītyasamutpāda · anattā · anicca · śūnyatā · nirvāṇa · abhidharma · the two-truths (saṃvṛti/paramārtha). Again mostly authoring.
- Optional concept gap-fill: `mohaniya` (only new unwritten stub), `siddha` cross-check, the Karma-grantha 148-subtype enumeration if a primary source becomes fetchable (would lift karma-prakriti toward high).

---

## Batch 27 — stub fill + Hindu/Buddhist concept layer + Chapters 11 & 12 (2026-06-20)

### Scope of this run
1. **Stub fill** — `mohaniya.md` (the only unwritten stub from Ch 10 run; forward-linked from karma-prakriti)
2. **Batch 27 concepts** (6 new files): `sarasvati`, `lakshmi`, `trimurti`, `pratyabhijna`, `spanda`, `bodhicitta`
3. **Chapter 11** — The Vedānta Family (`chapters/hindu/11-vedanta.md`)
4. **Chapter 12** — The Buddhist Family (`chapters/buddhist/12-buddhist.md`)
5. **Graph regeneration**, **INDEX update**, **progress.md update**, **push to GitHub**

### Stub fill

| concept | status | confidence | note |
|---|---|---|---|
| mohaniya | converged | medium | TS 8.9 Sanskrit FETCHED (Vijay K. Jain 2018 / WisdomLib doc1084874); 28 sub-types (3 darśana-mohanīya + 16 kaṣāya-vedanīya + 9 no-kaṣāya-vedanīya); gunasthāna arc documented; Wikipedia "Types of Karma (Jainism)" 2nd signal. 0 unwritten stubs after this commit. |

### Batch 27 concepts

| # | concept (filename) | status | confidence | key source |
|---|---|---|---|---|
| 1 | `sarasvati.md` | converged | medium | EBSCO Research Starters + Wikipedia "Saraswati"; RV 6.61 + 7.95-96 + 2.41.16 (best of mothers/rivers/goddesses); Tridevi Sattva-guṇa; Śāradā/Bhāratī epithets |
| 2 | `lakshmi.md` | converged | medium | Wikipedia "Lakshmi" + ExoticIndiaArt; VS 31.22 Śrī-Lakṣmī pairing; Śrī Sūkta (15 vv.; RV appendix); Samudramanthana; 4-arm = 4-puruṣārthas; Tridevi Rajas; VP prose; NOT-equiv prakṛti-sāṃkhya (Lakṣmī is cit; Prakṛti is acit) |
| 3 | `trimurti.md` | converged | medium | Wikipedia "Trimurti" + Basham *The Wonder That Was India*; VP 1.2.66 + Maitri Up. 4.5; NOT ancient Vedic (Purāṇic synthesis); Vaiṣṇava/Śaiva rejection; Śākta feminisation; Smārta pañcāyatana; Christian Trinity NOT-equivalent |
| 4 | `pratyabhijna.md` | converged | medium | IEP "Kashmiri Shaiva Philosophy" + Wikipedia "Utpaladeva" + WisdomLib; IPK c.950 CE; prati+abhi+√jñā etymology; liberation = recovery of Śiva-identity not new knowledge; IPK anti-kṣaṇavāda argument; Advaita comparison table (world REAL/world māyā; Śiva has Śakti/Brahman nirguṇa) |
| 5 | `spanda.md` | converged | medium | Wikipedia "Kashmir Shaivism" + IEP + Sanskrit-TrikaShaivism; Vasugupta Śiva Sūtras (~9th c.) + Kallata Spandakārikā; non-illusionist ābhāsa (world REAL, NOT māyā); svātantrya; Kṣemarāja quote; NOT-equiv prakṛti-sāṃkhya (Spanda IS consciousness; Sāṃkhya Prakṛti is NOT) |
| 6 | `bodhicitta.md` | converged | medium | Wikipedia "Bodhicitta" + Tricycle; Śāntideva Bodhicaryāvatāra (8th c.) + Asaṅga Bodhisattvabhūmi; bodhipraṇidhicitta/bodhiprasthānacitta two-type; relative (compassion) / absolute (śūnyatā) bodhicitta; 6 pāramitās; NOT-equiv cāritra (bodhicitta delays liberation for others; Jain cāritra is self-directed) |

### Hub-file edits (orphan prevention — inbound forward edges added)
- `brahma.md`: `part-of: trimurti` + `shares-vocabulary-with: sarasvati`
- `vaishnavism.md`: `expressed-by: lakshmi`
- `shaivism.md`: `expressed-by: pratyabhijna` + `expressed-by: spanda`
- `bodhisattva.md`: `expressed-by: bodhicitta`

### TS verse fetched this batch
- **TS 8.9** (mohanīya sub-types): *anantānubandhyapratyākhyānapratyākhyānasaṃjvalana vikalpāścaikaśaḥ krodhamānamāyālobhāḥ* (Vijay K. Jain 2018)

### Chapters authored

| chapter | file | primary concepts | status |
|---|---|---|---|
| Ch 11 — The Vedānta Family | `chapters/hindu/11-vedanta.md` | prasthānatrayī · brahman · ātman-vedānta · māyā-advaita · mokṣa-advaita · advaita-vedanta · vishishtadvaita · dvaita-vedanta · vivartavāda · pariṇāmavāda · bhakti · jñāna-mārga · karma-mārga · trimurti · avatāra-vedānta · sarasvatī · lakṣmī | drafted |
| Ch 12 — The Buddhist Family | `chapters/buddhist/12-buddhist.md` | four-noble-truths · dukkha · tanha · paticcasamuppada-pali · nibbana-theravada · anatta-buddhist · anicca · theravada · arhat · skandha-buddhist · abhidharma · sunyata · bodhicitta · bodhisattva · madhyamaka · dvisatya · yogacara · vijnaptimatrata · alaya-vijnana · tathagata-garbha | drafted |

### Primary texts fetched for Ch 11/12
- SN 56.11 (*Dhammacakkappavattana Sutta*), MN 141 (*Saccavibhaṅga Sutta*) — Four Noble Truths (corpus-prior)
- Ud 8.1 — nibbāna unconditioned formula (corpus-prior)
- SN 12.21 (*Cetanā Sutta*) — *imasmiṃ sati* formula (corpus-prior)
- SN 22.59 (*Anattalakkhaṇa Sutta*) — anattā argument (corpus-prior)
- MMK 24.18 — emptiness = dependent arising (corpus-prior)

### Graph (final state)
`build_graph.py` clean: **202 nodes, 1237 edges** (post Batch-27 + mohaniya; chapters are not graph nodes).
`"C:\Program Files\Graphviz\bin\dot.exe" -Tsvg graph/graph.dot -o graph/graph.svg` — SVG rendered.
graph.dot / graph.html / graph.svg all refreshed.

### Nothing blocked or needs-opus-review. All cited; TS 8.9 directly fetched; chapters cite corpus-prior fetches with file references.

### Corpus milestone: 202 concepts across 27 batches + 4 linker passes. 0 unwritten stubs.

### Suggested Batch 28 (names only — no files written)

**Hindu theology depth:**
- `vishnu-sahasranama` — the 1000 names of Viṣṇu as a theological text; connects vishnu.md to devotional practice
- `gita` — the Bhagavad Gītā as a primary text node (presently cited but no dedicated file); the most cross-tradition Indian text

**Buddhist philosophy remaining:**
- `nagarjuna` — person-node for Nāgārjuna; anchor behind madhyamaka/mulamadhyamakakarika/sunyata/prasanga-nagarjuna
- `santideva` — person-node for Śāntideva; anchor behind bodhicitta/bodhisattva (Bodhicaryāvatāra)
- `nirvana-mahayana` — Mahāyāna nirvāṇa (deliberately not entered parinirvāṇa; different from Theravāda account)

**Linker pass 5:**
- Full audit over all 202 files; integrate Batch 27 reciprocity only where a real connectivity defect exists; check mohaniya + 6 new Batch-27 nodes for any remaining orphans; update `.linker-state`.

---

## Batch 28 — New concepts + Linker Pass 5 (2026-06-21)

### Startup reconcile
- Discovered and removed duplicate `nishcaya-vyavahara.md` (the canonical file is `nishchaya-vyavahara.md` with 'chaya'); fixed `naya.md` stale link; 201 nodes before batch.

### Batch 28 concepts

| # | concept (filename) | status | confidence | key source |
|---|---|---|---|---|
| 1 | `gita.md` | contested | medium | IEP "Bhagavad Gita" + prasthānatrayī student resource; 3-school reading table (Śaṅkara/Rāmānuja/Madhva); charama-śloka BG 18.66 |
| 2 | `nagarjuna.md` | converged | medium | IEP "Nagarjuna" + Britannica; ~150-250 CE; MMK 27-ch; prasaṅga reductio; well-attested vs disputed works |
| 3 | `santideva.md` | converged | medium | Ency. of Buddhism + Philopedia; ~685-763 CE Nalanda; BCA 10 ch/~1000 vv; ch6 patience + ch9 sunyata; 108 Indian commentaries |
| 4 | `nirvana-mahayana.md` | converged | medium | Study Buddhism + Wikipedia (Buswell-Lopez); apratiṣṭhita-nirvāṇa; Theravāda vs Mahāyāna comparison table |
| 5 | `vishnu-sahasranama.md` | converged | medium | Wikipedia + ExoticIndiaArt; Mbh. Anuśāsanaparva 13.149; 108 vv / 1000 names; Bhīṣma frame; 4-school commentary table |

### Linker Pass 5
- Full orphan audit of all 206 nodes after Batch 28
- Pre-fix orphans found: `gita`, `nirvana-mahayana`, `vishnu-sahasranama` (new concepts), plus legacy orphans `lingam`, `nikshepa`, `paticcasamuppada-pali`
- Also fixed: `gita.md` had wrong `part-of: brahma-sutra` / `part-of: upanishad` edges → corrected to `shares-vocabulary-with` (they are co-members of prasthānatrayī, not child nodes)
- Post-fix: **0 orphans** across all 206 nodes
- Hub files edited: brahma-sutra, karma-marga, bhakti, avatara-vedanta, vishnu, vaishnavism, bodhisattva, nirvana-buddhist, bodhicitta, shaivism, naya, pratityasamutpada

### Graph (final state)
`build_graph.py` clean: **206 nodes, 1275 edges**. 0 unwritten stubs. 0 orphans.
`graph/graph.svg` rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`.

### Notable findings this batch

1. **Gita.md is now the prasthānatrayī hub**: The three co-equal canonical text files (upanishad.md, brahma-sutra.md, gita.md) are now all written and cross-linked via `shares-vocabulary-with`. The Advaita/Viśiṣṭādvaita/Dvaita interpretive split is documented in the contested-status comparison table.

2. **Nāgārjuna and Śāntideva complete the Madhyamaka person-node layer**: Both are now person-nodes with links to their texts. The chain Nāgārjuna (MMK/prasaṅga/śūnyatā) → Śāntideva (BCA/bodhicitta/pāramitā) is now explicit.

3. **Apratiṣṭhita-nirvāṇa fills the critical Mahāyāna gap**: The corpus had nibbāna-Theravāda and nirvāṇa-Buddhist (general), but the specifically Mahāyāna non-abiding Buddhahood was missing. Now written and connected.

4. **Viṣṇusahasranāma documents the cross-school commentary pattern**: Four incompatible schools (Advaita/Viśiṣṭādvaita/Dvaita/Acintya-bhedābheda) all claim the same devotional text as their proof-text — a paradigmatic case of how divergent metaphysics inhabit a shared textual tradition.

5. **Duplicate node removed**: `nishcaya-vyavahara.md` was a stale duplicate of `nishchaya-vyavahara.md`. The contested (better) version is canonical.

### Corpus milestone: 206 concepts across 28 batches + 5 linker passes. 0 orphans. 0 unwritten stubs.

### Suggested Batch 29 (names only — no files written)

**Remaining Buddhist concepts:**
- `madhyamaka-logic` — Prāsaṅga method as a distinct logical technique; companion to prasanga-nagarjuna.md and aristotle-logic.md
- `yogacara-logic` — Dignāga-Dharmakīrti school's specific logical contribution (already partly in hetu-vidya.md; may need a dedicated file)
- `two-truths-analysis` — cross-tradition comparison of two-truths schemes (Jain niścaya/vyavāhara vs Buddhist saṃvṛti/paramārtha vs Advaita vyāvahārika/pāramārthika) — could be a cross-tradition synthesis file

**Hindu deity/text nodes:**
- `mahabharata` — as a primary text node (the Viṣṇusahasranāma and Gītā both live inside it; adds context)
- `ramayana` — primary text node; bhakti/avatāra literature

**Cross-tradition ethics remaining:**
- `metta` — loving-kindness (Pali); the foundational brahmavihāra; companion to ahimsa-buddhist.md
- `karuna` — compassion (Pali); second brahmavihāra; grounds bodhicitta

---

## Batch 29 — Epic text/author nodes + the four Brahmavihāras (2026-06-21)

### Startup reconcile
- Batch 28 fully committed (206 nodes, 1275 edges, 0 orphans, 0 stubs). Only uncommitted item was the generated `graph/graph` graphviz intermediate — not a concept draft, so no §8 reset required.

### Scope decision (deviation from the literal suggested Batch 29 — documented per §10)
The suggested Batch 29 list named `madhyamaka-logic`, `yogacara-logic`, and `two-truths-analysis`. On inspection these would **violate §2 (atomic / no duplicates / no synthesis essays)**:
- `madhyamaka-logic` duplicates the existing **`prasanga-nagarjuna.md`** (which already covers prasaṅga as a logical technique, Prāsaṅgika/Svātantrika, vs Nyāya tarka).
- `yogacara-logic` duplicates the existing **`hetu-vidya.md`** (Dignāga–Dharmakīrti logic: trairūpya, apoha, 2-pramāṇa). The suggestion itself flagged it as "already partly in hetu-vidya.md."
- `two-truths-analysis` would be a cross-tradition **synthesis essay**; §2 forbids these, and the comparison already lives in typed `often-conflated-with-NOT-equivalent` edges between `nishchaya-vyavahara`, `dvisatya`, and the Advaita two-truths.

Substituted a full 8-concept batch of genuinely-new, non-duplicative nodes: the two **itihāsa** epic text-nodes + their traditional author-sages (paralleling Batch 28's Nāgārjuna/Śāntideva person-nodes), and the complete set of **four brahmavihāras**.

### Concepts completed: 8 / 8 (0 blocked, 0 needs-opus-review)

| # | concept | status | confidence | key source |
|---|---|---|---|---|
| 1 | `mahabharata` | converged | medium | Wikipedia + World History Enc.; ~400 BCE–400 CE; *Jaya*/*Bhārata*/*Mahābhārata* 3-stage redaction; 18 parvas/~100k ślokas; container for gita + vishnu-sahasranama; *smṛti*≠*śruti* "fifth Veda" caution |
| 2 | `ramayana` | converged | medium | Wikipedia + World History Enc.; *ādikāvya*; ~5th–4th c. BCE core (Bks 2–6) + Bāla/Uttara interpolations; 24k ślokas/7 kāṇḍas; Rāma=7th Viṣṇu-avatāra concentrated in later framing books |
| 3 | `vyasa` | converged | medium | Wikipedia + WisdomLib; Veda-Vyāsa (divider of the one Veda into four); Mbh/18 Purāṇas; **identified-with Bādarāyaṇa as a conflation**; aṃśāvatāra + chiranjīvī; "Vyāsa as role-title" historicity caution |
| 4 | `valmiki` | converged | medium | Wikipedia + WisdomLib; *ādikavi*; krauñca-bird grief→first śloka (*śoka*→*śloka*); *valmīka*/anthill etymology; robber-redemption (*nāma-japa* bhakti motif); shelters Sītā, teaches Lava/Kuśa |
| 5 | `metta` | converged | medium | Wikipedia (Maitrī/Brahmavihara) + Nyanaponika; loving-kindness; 1st brahmavihāra/*appamaññā*/pāramī; Karaṇīya Mettā Sutta Sn 1.8; far enemy *vyāpāda/dosa*, near enemy *rāga*; ≠ romantic love |
| 6 | `karuna` | converged | medium | Wikipedia + Nyanaponika; compassion; 2nd brahmavihāra; far enemy cruelty/indifference, near enemy sentimental pity; Mahāyāna *mahākaruṇā*→bodhicitta |
| 7 | `mudita` | converged | medium | Wikipedia + Nyanaponika; sympathetic/altruistic joy; 3rd brahmavihāra; far enemy envy, near enemy conditional pleasure; Jain *pramoda* parallel noted |
| 8 | `upekkha` | converged | medium | Wikipedia + Nyanaponika; equanimity; 4th/culminating brahmavihāra; balance "rooted in insight" (anattā); far enemy agitation, near enemy indifference; also *upekkhā-bojjhaṅga* |

### Linker pass (integration into the established graph)
Added inbound edges so the new cluster connects to the existing graph (not just to itself):
- **`gita` part-of `mahabharata`** + `gita`→`vyasa` (correctness: the Gītā is a section of the Bhīṣma Parva)
- **`vishnu-sahasranama` part-of `mahabharata`** (correctness: Anuśāsana Parva 13.149)
- `ahimsa-buddhist`→`metta`/`karuna`; `bodhicitta`→`karuna`
- `vishnu`→`ramayana`; `avatara-vedanta`→`ramayana`/`mahabharata`

### Audits (deterministic)
- **0 orphans** (every node has ≥1 inbound; audit regex corrected to allow uppercase in `often-conflated-with-NOT-equivalent`).
- **0 edges to nonexistent nodes** (no new unwritten stubs created).
- Graph regenerated: **206 → 214 nodes, 1275 → 1313 edges**. `graph.svg` rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html` refreshed. Dropped the graphviz cleanup intermediate `graph/graph` from tracking (the script deletes it on each render).

### Notable findings this batch
1. **The itihāsa layer is now anchored**: the corpus had `gita` and `vishnu-sahasranama` floating without their containing text; both are now correctly `part-of` `mahabharata`, and the two epics + their author-sages (Vyāsa, Vālmīki) form a coherent Hindu narrative-text family — previously an empty index family.
2. **Two documented conflations added**: Vyāsa≡Bādarāyaṇa (probably distinct figures merged), and "Vyāsa"/"Vālmīki" as role-title vs historical individual — both flagged rather than asserted.
3. **The four brahmavihāras are complete as a set**, each defined by its near/far enemy (the Visuddhimagga diagnostic), with the upekkhā≠indifference and mettā≠attachment near-enemy distinctions made explicit. Cross-tradition equanimity/joy parallels (Yoga-Sūtra 1.33; Jain *pramoda*/*mādhyasthya*; Gītā *samatva*) are noted as **parallels, not identities** (prime-directive discipline) without creating speculative stub nodes.

### Corpus milestone: 214 concepts across 29 batches. 0 orphans. 0 unwritten stubs.

### Suggested Batch 30 (names only — no files written)
- `dukkha`-adjacent / already done; consider Hindu deity nodes: `shiva`, `krishna`, `rama` (currently referenced only in prose) — would let the epic/avatāra edges point at the deities directly.
- `samatva` / `sthitaprajna` — the Gītā's equanimity ideal as its own node (would give upekkhā a real cross-tradition `structurally-parallel-to` target instead of a prose note).
- Jain four-bhāvanā set (`maitri-jain`, `pramoda`, `karunya`, `madhyasthya`) — the structural counterpart to the brahmavihāras; would let the parallels become typed edges.
- **Index reconciliation pass**: root `index.md`/`INDEX.md` lag well behind the corpus (~40 concepts missing before this batch); a dedicated pass should rebuild it from front-matter, or a generator added to `build_graph.py`.

---

## Batch 30 — Hindu deity nodes + Gītā equanimity + the four Jain bhāvanās (2026-06-21)

### Startup reconcile
- Batch 29 fully committed (214 nodes, 1313 edges, 0 orphans, 0 stubs). Working tree clean. No interrupted draft to reset.
- Graph re-run before work (the "before" snapshot): **214 nodes, 1313 edges** — matches the committed state.

### Scope
A "batch of everything" spanning all three threads of the suggested Batch 30 at once: the Hindu **deity nodes** the epic/avatāra edges had only referenced in prose, the **Gītā equanimity ideal** as its own pair of nodes, and the **four Jain bhāvanās** (TS 7.11) — the structural counterpart to the Batch-29 brahmavihāras, which lets the prior prose parallels become typed edges.

### Concepts completed: 9 / 9 (0 blocked, 0 needs-opus-review)

| # | concept | status | confidence | key source |
|---|---|---|---|---|
| 1 | `shiva` | converged | medium | Wikipedia "Shiva" + corpus shaivism.md (IEP); Rudra→Śiva; Trimūrti destroyer; liṅga; Śakti; dualist/monist school table; Śiva≠nirguṇa-Brahman NOT-equiv |
| 2 | `krishna` | **contested** | medium | Wikipedia "Krishna" + corpus gita/avatara-vedanta/vishnu; 3-reading table (8th avatāra / svayaṃ bhagavān BhP 1.3.28 / saguṇa Brahman); avatāra-vs-source-of-Viṣṇu NOT-equiv |
| 3 | `rama` | converged | medium | Wikipedia "Rama" + corpus ramayana/valmiki/avatara-vedanta; 7th avatāra; maryādā puruṣottama; Rāmānandī/Tulsīdās; avatāra-identification concentrated in later kāṇḍas |
| 4 | `samatva` | converged | medium | BG 2.48 *samatvaṁ yoga ucyate* (Mukundananda, cross-checked 3 hosts) + corpus upekkha.md; equanimity = the Gītā's definition of yoga |
| 5 | `sthitaprajna` | converged | medium | BG 2.54–55 (*prajahāti yadā kāmān…*) + BG 2.54–72; the realized-sage portrait; perfected samatva; vs jīvanmukta |
| 6 | `maitri-jain` | converged | medium | **TS 7.11 FETCHED** (Jainworld); benevolence toward all beings; Sarvārthasiddhi gloss; ground of ahiṃsā; ≠ Buddhist mettā (parallel) |
| 7 | `pramoda` | converged | medium | TS 7.11; joy at the virtuous (*guṇādhika*); antidote to māna/envy; ∥ muditā, NOT-equiv |
| 8 | `karunya` | converged | medium | TS 7.11; compassion for the afflicted (*kliśyamāna*); ∥ Buddhist karuṇā (same root), NOT-equiv (jīva-ontology vs intention) |
| 9 | `madhyasthya` | converged | medium | TS 7.11; tolerance toward the ill-behaved (*avineya*); internal non-attachment vs rāga-dveṣa; ∥ upekkhā/samatva |

### TS verse directly fetched this batch
- **TS 7.11** (the four right sentiments): *maitrī-pramoda-kāruṇya-mādhyasthāni ca sattva-guṇādhika-kliśyamānāvineyeṣu* (Jainworld translation; Sarvārthasiddhi glosses via Wikipedia "Maitrī").

### Linker integration (inbound edges added so the new cluster is not self-isolated)
- **Deities:** `shaivism` expressed-by `shiva`; `trimurti` shares-vocab `shiva`; `ramayana` shares-vocab `rama`; `mahabharata` shares-vocab `krishna`; `avatara-vedanta` shares-vocab `krishna`/`rama`; `gita` shares-vocab `krishna`.
- **Gītā ideals:** `gita` expressed-by `samatva` + expressed-by `sthitaprajna`.
- **Jain bhāvanās ↔ brahmavihāras:** `metta` shares-vocab `maitri-jain`; `karuna` shares-vocab `karunya`; `mudita` ∥ `pramoda`; `upekkha` ∥ `madhyasthya`. The Batch-29 prose parallels are now typed edges.

### Audits (deterministic)
- **0 dangling stubs** (every edge target has a file) and **0 orphans** (every node has ≥1 inbound) across all 223 nodes.
- §5 two-type pairs verified sanctioned: shiva→brahman (shares-vocab + NOT-equiv), krishna→vishnu (parallel + NOT-equiv), karunya→karuna (shares-vocab + NOT-equiv), pramoda→mudita (parallel + NOT-equiv). `is-a-type-of` directions (krishna/rama → avatara-vedanta) are specific→general; no bidirectional is-a-type-of.
- Graph regenerated: **214 → 223 nodes, 1313 → 1373 edges**. `graph.svg` rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md` refreshed.

### Notable findings this batch
1. **The avatāra edges now point at real deities.** Before this batch `avatara-vedanta`/`ramayana`/`mahabharata` referred to Rāma and Kṛṣṇa only in prose; the deity nodes now exist, so "seventh/eighth avatāra" is a typed `is-a-type-of` edge rather than a sentence.
2. **`krishna` is contested, not converged.** The deity-profile is agreed, but the avatāra-of-Viṣṇu vs svayaṃ-bhagavān (source-of-Viṣṇu, Gauḍīya) status is a genuine fork — recorded as the §3 divergence table, with the NOT-equivalent edge to `vishnu`.
3. **The brahmavihāra ∥ bhāvanā parallel is now a typed bridge, not a footnote.** Each Jain bhāvanā links to its Buddhist counterpart with the prime-directive discipline intact: same vocabulary (maitrī/mettā, kāruṇya/karuṇā literally cognate) marked `shares-vocabulary-with`, but `often-conflated-with-NOT-equivalent` where the soteriology diverges (jīva-ontology / kaṣāya-restraint vs no-self / brahmavihāra path).
4. **Rāma/Kṛṣṇa maryādā-vs-līlā contrast** captured as a `structurally-parallel-to` edge — the two great avatāra-bhakti foci, distinguished by rule-bound ideal vs transgressive play.

### Corpus milestone: 223 concepts across 30 batches. 0 orphans. 0 unwritten stubs.

### Suggested Batch 31 (names only — no files written)
- `parvati` / `durga` / `kali` — the Śākta goddess nodes; would let Śiva–Śakti and the Tridevi edges point at real deity nodes (parallel to this batch's Viṣṇu-avatāra fix).
- `jivanmukti` — liberation-while-living as its own node; currently only inside `moksha-advaita`; would give `sthitaprajna` a precise `is-a-type-of`/`structurally-parallel-to` target.
- `hanuman` — devotee-deity; the paradigm of Rāma-bhakti and dāsya-bhāva.
- `ganesha` — the most-invoked Hindu deity, conspicuously absent; pañcāyatana completion.
- `naṭarāja` — Śiva's cosmic dance as a distinct iconographic/cosmological node (creation–dissolution cycle).

---

## Linker Pass 6 — Edges batch (2026-06-21)

### Scope
No new concept files. A connectivity-enrichment pass over the existing 223 nodes: degree analysis to find under-linked nodes, then add **genuinely new, prose-grounded typed edges** (not hand-maintained backlinks — §5 forward-only respected; existing reverse edges like `vyasa→valmiki` were left as the single stored direction).

### Edges added: 11 (across 8 source files)

| edge | type | rationale |
|---|---|---|
| `valmiki → rama` | shares-vocabulary-with | Vālmīki is both source-poet of Rāma's life and a character in his own poem (shelters Sītā; teaches Lava/Kuśa) — valmiki was the lowest-degree node (deg 4) |
| `dravyarthika-naya → paryayarthika-naya` | shares-vocabulary-with | the two complementary halves of the seven-naya system were not directly linked (only via member nayas) |
| `dravyarthika-naya → dravya` | shares-vocabulary-with | mirrors the existing `paryayarthika-naya → paryaya`; the substance-side naya takes dravya as its object |
| `krishna → bhakti` | shares-vocabulary-with | Kṛṣṇa is the supreme object of Vaiṣṇava bhakti (rāsa-līlā, BG 7–12, Gauḍīya) — missing from the new deity node |
| `neoplatonism → plato-soul` | historically-influenced-by | the Neoplatonic Soul-hypostasis systematises Plato's soul; gives low-inbound plato-soul a defensible inbound edge |
| `agni → stoic-logos` | structurally-parallel-to + often-conflated-NOT-equiv | both are cosmic **fire** principles bound to cosmic order (Agni = *ṛtasya gopā*; logos = *pyr technikon*) — but personal ritual deity ≠ impersonal corporeal world-reason (sanctioned two-type pair) |
| `samatva → karma-marga` | shares-vocabulary-with | samatva (BG 2.48) is the defining inner condition of karma-yoga |
| `samatva → yoga-darshana` | shares-vocabulary-with + often-conflated-NOT-equiv | both define "yoga" — Gītā as *samatva*, Patañjali as *citta-vṛtti-nirodha*; engaged equanimity ≠ meditative cessation (sanctioned pair) |
| `sthitaprajna → jnana-marga` | shares-vocabulary-with | the sage of steady *prajñā* is the realized exemplar of the knowledge-path |

### Audits (deterministic)
- **0 dangling stubs**, **0 orphans** across all 223 nodes.
- §5 checks: the two two-type pairs (`agni→stoic-logos`, `samatva→yoga-darshana`) are the sanctioned `parallel + NOT-equivalent` combination; `neoplatonism→plato-soul` is `historically-influenced-by` pointing to the influence source (correct direction); no `is-a-type-of` edges added, so no direction/bidirectional risk.
- Graph regenerated: **1373 → 1384 edges** (node count unchanged at 223). `graph.svg` re-rendered; `graph.dot`/`graph.html`/`index.md` refreshed.

### Notable
- The biggest real gap closed was the **naya group-node link**: `dravyarthika-naya` and `paryayarthika-naya` were each linked to their member nayas and to `anekantavada`, but not to each other — now the two halves of the system are directly connected and symmetric (each points to its substance/mode object: dravya / paryāya).
- The **Agni ↔ Stoic-logos fire-principle parallel** is a new honest cross-tradition edge in the prime-directive spirit: a striking structural similarity (cosmic fire + order) explicitly fenced by a NOT-equivalent edge (worshipped deity vs physical world-reason).

---

## Linker Pass 7 — Edges batch (2026-06-21)

### Scope
No new concept files. Connectivity-enrichment over the existing 223 nodes, driven by **two deterministic signals**: (1) degree analysis for under-linked nodes; (2) a **prose-reference audit** — a script that flags any concept whose own prose cites another existing concept (`(x.md)` / `[[x]]`) with no corresponding typed edge. §5 forward-only respected throughout: audit hits that were merely the *reverse* of an existing edge (computed backlinks) were left unstored.

### Edges added: 8 (across 5 source files)

| edge | type | rationale |
|---|---|---|
| `parshvanatha → ahimsa` | expressed-by | Pārśva's *cāturyāma* = ahiṃsā/satya/asteya/aparigraha; only aparigraha was linked. Completes the four-fold restraint. |
| `parshvanatha → satya` | expressed-by | 2nd of the cāturyāma (raised low-inbound satya) |
| `parshvanatha → asteya` | expressed-by | 3rd of the cāturyāma (raised low-inbound asteya) |
| `mudita → karuna` | shares-vocabulary-with | the two middle *appamaññā* (joy-at-fortune ∥ compassion-at-suffering); the pair was the one brahmavihāra link missing in either direction |
| `karuna → upekkha` | shares-vocabulary-with | equanimity completes/regulates compassion; the other missing brahmavihāra pair — the four immeasurables are now a fully-connected K4 (all 6 pairs) |
| `mahavira → utsarpini-avasarpini` | historically-influenced-by | prose-audit hit: Mahāvīra = 24th/last tīrthaṅkara closing the present avasarpiṇī; mirrors Pārśva's existing kālacakra edge |
| `papa → samayasara` | expressed-by | prose-audit hit: the "iron chain / golden chain, both bind" doctrine is expounded in Kundakunda's Samayasāra |
| `papa → nishchaya-vyavahara` | shares-vocabulary-with | prose-audit hit: from the niścaya standpoint the whole puṇya/pāpa axis is pudgala, not the pure soul — "real" only at the vyavahāra level |

### Audits (deterministic)
- **0 orphans, 0 unwritten stubs, 0 edge-type violations** across all 223 nodes (verified by script: no bidirectional `is-a-type-of`; no `is-a-type-of`/`part-of` combined with a parallel/NOT-equivalent type on the same ordered pair).
- Graph regenerated: **1384 → 1392 edges** (223 nodes unchanged). `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md` refreshed.

### Edge surface now exhausted
The prose-reference audit's remaining hits are **all reverse-of-existing edges** (the Vedānta triangle advaita→dvaita/vishishtadvaita and vishishtadvaita→dvaita; pramanavarttika→pramana-samuccaya; dharmottara→pramanavarttika) — correctly *not* stored under §5 forward-only. The remaining lowest-degree nodes (`abhidharmakosa`, `valmiki`, `ajivika`, `neoplatonism`, `nikshepa`) can only be raised by either (a) un-cited new assertions (forbidden by §1/§4) or (b) new author/stub nodes such as `vasubandhu` (would break the 0-stub invariant — a Batch-31 decision, not a linker pass). **Further connectivity gains require new concept files, not more edges.** Per §0 ("when in doubt, assert less"), the pass halts here rather than pad.

### Suggested next (Batch 31 — names only, unwritten)
- Author/source nodes that would convert reverse-only low-degree nodes into hubs: `vasubandhu` (anchors abhidharmakosa), `makkhali-gosala` (anchors ajivika), `plotinus` / Proclus-Iamblichus (anchor neoplatonism).
- Śākta goddess nodes (`parvati`/`durga`/`kali`), `jivanmukti`, `hanuman`, `ganesha`, `nataraja` (carried over from Batch-30 suggestion).

---

## Batch 31 — Hindu deity layer completion + jīvanmukti + Vasubandhu (2026-06-21)

### Startup reconcile
- Batches 1–30 + linker passes 1–7 fully committed (223 nodes, 1392 edges, 0 orphans, 0 stubs). Working tree clean — no interrupted draft to reset.
- Baseline graph run confirms 223 nodes / 1392 edges. Existing Śākta-layer files: `shakti`, `lakshmi`, `sarasvati`, `lingam`. The planned deity names are referenced only in prose (no existing edges) → writing them is non-breaking.

### Batch 31 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `parvati.md` | done | converged, medium; benign Devī/Śakti; Himavān/Satī; mother of Gaṇeśa/Kārttikeya; Kena Up. Umā Haimavatī; Wikipedia + corpus shakti.md |
| 2 | `durga.md` | done | converged, medium; Mahiṣāsura-mardinī; formed from gods' pooled tejas (Devī Māhātmya); Wikipedia + corpus shakti.md |
| 3 | `kali.md` | done | converged, medium; *kāla*=time/black; Raktabīja; nirguṇa symbolism; Kālī-Mā bhakti; Wikipedia + corpus shakti.md |
| 4 | `ganesha.md` | done | converged, medium; Vighneśvara/Pratham-pūjya; gaṇa+īśa; Mahābhārata scribe; Gāṇapatya supreme; Wikipedia + World History Enc. |
| 5 | `hanuman.md` | done | converged, medium; Vāyu-putra; dāsya-bhakti paradigm; Sundara Kāṇḍa; Wikipedia + World History Enc. |
| 6 | `jivanmukti.md` | done | converged, medium; liberation-while-embodied vs videhamukti; prārabdha-karma; Wikipedia + corpus moksha-advaita.md |
| 7 | `vasubandhu.md` | done | converged, medium; Abhidharmakośa→Yogācāra; two-Vasubandhus flagged; Wikipedia + SEP (independent) |

## Run log — Batch 31 (2026-06-21)

### Concepts completed: 7 / 7 (0 blocked, 0 needs-opus-review)
All converged, confidence medium. Three Hindu deity threads + one soteriology gap + one Buddhist author anchor.

| concept | status | conf | key source(s) | signal independence |
|---|---|---|---|---|
| parvati | converged | medium | Wikipedia "Parvati" + corpus shakti.md | 2 (deity article + corpus tradition file) |
| durga | converged | medium | Wikipedia "Durga" + corpus shakti.md | 2 |
| kali | converged | medium | Wikipedia "Kali" + corpus shakti.md | 2 |
| ganesha | converged | medium | Wikipedia "Ganesha" + World History Encyclopedia | 2 independent encyclopedias |
| hanuman | converged | medium | Wikipedia "Hanuman" + World History Encyclopedia | 2 independent encyclopedias |
| jivanmukti | converged | medium | Wikipedia "Jivanmukta" + corpus moksha-advaita.md | 2 |
| vasubandhu | converged | medium | Wikipedia + **Stanford Enc. of Philosophy** + corpus Yogācāra cluster | 3 (2 independent refs) |

### Linker integration (inbound edges so the new cluster is not self-isolated)
New nodes' forward edges connect them outward to existing hubs (shakti, shaivism, shiva, brahman, mahabharata, vyasa, rama, bhakti, ramayana, moksha-advaita, arihant, nirvana-buddhist, karma-vedic, yogacara, abhidharmakosa, vijnaptimatrata, trisvabhava, alaya-vijnana, nagarjuna, avatara-vedanta, prakriti-samkhya, upanishad). To give the four "all-outbound" new nodes a stored inbound edge **without** double-storing a symmetric relation (§5 forward-only), one edge was *relocated* into the existing hub file in each case:
- `shiva → ganesha` (relocated from ganesha→shiva)
- `ramayana → hanuman` (relocated from hanuman→ramayana)
- `sthitaprajna → jivanmukti` (relocated from jivanmukti→sthitaprajna; complements the pre-existing sthitaprajna→moksha-advaita "anticipates the jīvanmukta" edge)
- `dignaga-pramana → vasubandhu` (**new**, correctly directed `historically-influenced-by`: Dignāga built on Vasubandhu's *Vāda-vidhi*)
- `parvati → durga` (relocated from durga→parvati: the "gentle goddess manifests her fierce aspect" direction)
- Removed the one intra-trio bidirectional pair (`kali→durga` dropped; kept `durga→kali` — Kālī springs from Durgā's brow).

### Audits (deterministic, via build_graph parser)
- **0 dangling stubs**, **0 orphans** (every node has ≥1 inbound), **0 bidirectional is-a-type-of**, **0 forbidden hier+similarity combos** across all 230 nodes.
- §5 sanctioned two-type pair verified: `jivanmukti → arihant` (`structurally-parallel-to` + `often-conflated-with-NOT-equivalent`). `is-a-type-of` directions checked specific→general: `jivanmukti → moksha-advaita` (a mode of Advaita liberation).
- A broader (stricter-than-project-standard) scan surfaced ~80 **pre-existing** bidirectional symmetric pairs corpus-wide (e.g. krishna↔rama, mahabharata↔ramayana from Batch 30) — **none involve the 7 new nodes**. Not introduced here; a corpus-wide forward-only refactor is a §10 fork decision, deferred.
- Graph regenerated: **223 → 230 nodes, 1392 → 1430 edges**. `graph.svg` rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md` refreshed.

### Notable findings this batch
1. **The Hindu deity layer is now substantially complete.** The Śākta trio (Pārvatī/Durgā/Kālī) gives the long-standing `shakti.md` prose descriptions real target nodes; Gaṇeśa (the conspicuously-absent most-invoked deity) and Hanumān (the dāsya-bhakti paradigm) fill the two biggest remaining gaps. The avatāra/epic/Tridevi region of the graph now points at deities, not prose.
2. **`jivanmukti` closes a soteriology gap with a tight cross-tradition cluster.** Liberation-while-embodied links Advaita (prārabdha-karma), the Gītā sthitaprajña, the Jain arihant (the prārabdha ∥ aghātiyā-karma parallel is striking — flagged NOT-equivalent on metaphysics), and the Buddhist saupādisesa/anupādisesa distinction — four traditions' "already-free-while-alive" accounts, honestly fenced.
3. **`vasubandhu` is one of the best-sourced person nodes** (Wikipedia + SEP independently agree, including on the *unresolved* "two Vasubandhus" question and the non-nihilist reading of vijñaptimātra). It converts the low-degree, reverse-only `abhidharmakosa` into a properly-anchored text and ties the whole Yogācāra cluster (vijñaptimātra/trisvabhāva/ālaya-vijñāna) to its author, plus the Vasubandhu→Dignāga logic lineage.

### Corpus milestone: 230 concepts across 31 batches. 0 orphans. 0 unwritten stubs.

### Suggested Batch 32 (names only — no files written)
- Remaining author/source anchors for low-degree reverse-only nodes: `asanga` (Vasubandhu's half-brother, co-founder of Yogācāra — would anchor the Yogācāra cluster from the other side), `makkhali-gosala` (anchors `ajivika`), `plotinus`/`proclus` (anchor `neoplatonism`), `dharmakirti` (anchors `pramanavarttika`).
- Remaining Hindu deity/iconography nodes: `nataraja` (Śiva's cosmic dance — creation/dissolution cycle), `kartikeya`/`skanda` (Pārvatī's other son, completes the family), `surya`, `nandi`.
- **Legacy forward-only refactor (a §10 fork to put to the user):** decide whether to collapse the ~80 pre-existing bidirectional symmetric pairs to single stored direction (strict §5) or formally accept bidirectional `shares-vocabulary-with`/`structurally-parallel-to` as the corpus convention and update CLAUDE.md §5 to say so.

---

## Edge-integrity decision + audit upgrade (2026-06-22)

### Decision (user-directed): the ~80 bidirectional **symmetric** pairs are ACCEPTED, not collapsed.
Evidence-based call after inspecting real pairs (krishna↔rama notes near-verbatim; ramayana/mahabharata and digambara/svetambara carry a small distinct per-vantage note). Rationale:
- `shares-vocabulary-with` / `structurally-parallel-to` / `often-conflated-with-NOT-equivalent` are **semantically symmetric** — no natural "forward." §5's forward-only rule was written for *directional* edges; it never cleanly applied to these.
- **Invisible to the rendered graph** (edge + both nodes' degree derive from a single stored direction), so collapsing 80 pairs is pure churn with zero visual payoff.
- They **cannot misrepresent** (no directional claim), unlike bidirectional `is-a-type-of` (mutual subsumption — forbidden, absent).
- Bidirectional storage keeps each concept file **self-contained/readable**; collapsing would need an arbitrary tie-break and silently drop visible links from ~half the files.
- → Treated as the legitimate **weaker associative layer** (drawn dashed/dotted). CLAUDE.md §5 amended to permit symmetric bidirectional storage explicitly (permitted, not required; no mechanical mirroring; no bulk-collapse).

### The deeper finding the audit surfaced: bidirectional **directional** edges (real defects)
A stricter check (now built into `build_graph.py audit_graph`) flags directional types stored in **both** directions — these assert two contradictory structural claims. The old audit only checked bidirectional `is-a-type-of`, so these were never surfaced.
- **Fixed now (2, unambiguous by chronology):**
  - removed `nagarjuna → historically-influenced-by: santideva` (backwards: Śāntideva ~8th c. is *after* Nāgārjuna ~2nd c.; the correct `santideva → nagarjuna` already exists).
  - retyped `yajna → historically-influenced-by: mimamsa-pramana` to `shares-vocabulary-with` (Vedic ritual predates Mīmāṃsā hermeneutics; the correct directional `mimamsa-pramana → yajna` already exists).
- **Queued for Batch 32 — directional-edge integrity pass (30 pre-existing pairs, each needs a per-pair direction judgment, §10 fork):**
  - `aggregates-into`: namokara↔sadhu, namokara↔upadhyaya
  - `formalizes`: nishchaya-vyavahara↔samayasara
  - `part-of`: anatta-buddhist↔nirvana-buddhist, anuvrata↔shad-avashyaka, atman-vedanta↔moksha-advaita, dhyana-jain↔tapas
  - `expressed-by` (23): abhidharma↔theravada, advaita-vedanta↔jnana-marga, advaita-vedanta↔vivartavada, agni↔yajna, anatta-buddhist↔citta, aristotle-substance↔four-causes, asrava↔bandha, avatara-vedanta↔gita, avatara-vedanta↔karma-marga, bhakti↔dvaita-vedanta, bhakti↔gita, bhakti↔vishishtadvaita, bodhicitta↔bodhisattva, bodhicitta↔santideva, gita↔karma-marga, kala-dravya↔paryaya, karma-vargana↔leshya, kundakunda↔nishchaya-vyavahara, kundakunda↔samayasara, nirjara↔samvara, pancha-mahabhuta↔prakriti-samkhya, parinamavada↔vishishtadvaita, vishnu↔vishnu-sahasranama
  - Resolution per pair: keep the one chronologically/structurally correct direction, OR retype to a symmetric edge if the relation is genuinely mutual/associative. Run `python graph/build_graph.py` → "structural audit" must read CLEAN when done.

### Audit upgrade
`build_graph.py` now ends every run with a deterministic **structural audit** (`audit_graph`): dangling stubs, orphans, bidirectional **directional** edges, forbidden hier+similarity combos → prints CLEAN / DEFECTS PRESENT.

---

## Directional-edge integrity pass (2026-06-22) — resolves the 30, audit now CLEAN

Worked through all 30 flagged bidirectional **directional** pairs, adjudicating each from its own note text. Method per pair: keep the one chronologically/structurally correct direction and drop the reverse; where the relation is genuinely **mutual/non-hierarchical**, retype the survivor to symmetric `shares-vocabulary-with`. Inbound-adjacency was computed first so **no deletion orphans a node**.

### Resolutions
- **23 keep-one-direction** (dropped the reverse defect): dhyana-jain→tapas (part-of); abhidharma→theravada, advaita-vedanta→jnana-marga, advaita-vedanta→vivartavada, yajna→agni, anatta-buddhist→citta, avatara-vedanta→gita, karma-marga→avatara-vedanta, dvaita-vedanta→bhakti, bhakti→gita, vishishtadvaita→bhakti, bodhisattva→bodhicitta, karma-marga→gita, paryaya→kala-dravya, karma-vargana→leshya, kundakunda→nishchaya-vyavahara, kundakunda→samayasara, pancha-mahabhuta→prakriti-samkhya, vishishtadvaita→parinamavada, vishnu→vishnu-sahasranama, aristotle-substance→four-causes, samayasara→nishchaya-vyavahara (formalizes), bodhicitta→santideva (kept this dir, not the author→doctrine one, to preserve santideva's only inbound).
- **5 retyped to symmetric `shares-vocabulary-with`** (genuinely mutual, no part/whole or means/goal hierarchy): anatta-buddhist↔nirvana-buddhist (insight↔goal), anuvrata↔shad-avashyaka (two classification-schemes overlapping in sāmāyika), atman-vedanta↔moksha-advaita (realization = liberation, co-defining), asrava↔bandha (adjacent causal tattvas), samvara↔nirjara ("the active purification pair").
- **2 retyped to complementary `aggregates-from`** (container/member leaf pair where strict forward-only would orphan the member): namokara→sadhu and namokara→upadhyaya. Members `aggregates-into` the mantra; the mantra `aggregates-from` its members — the script's intended complementary directional pair, so no same-type bidirectional. This is the one sanctioned exception to forward-only: a container and its leaf-members each need the other to stay non-orphan.
- **Bonus:** removed a pre-existing exact-duplicate edge `vishnu → vaishnavism (part-of)` (two identical lines merged into one).

### Audit
`python graph/build_graph.py` → structural audit reads **CLEAN**: stubs NONE, orphans NONE, bidirectional-directional NONE, forbidden-combos NONE, exact-duplicate edges NONE. Graph: **230 nodes, 1429 → 1401 edges** (28 defect edges removed; 7 retyped in place). `graph.svg` re-rendered via Graphviz; `graph.dot`/`graph.html`/`index.md` refreshed.

### Net effect on the §5 policy
The corpus now cleanly separates the two layers the decision defined: a **directional skeleton** (`is-a-type-of`/`part-of`/`formalizes`/`expressed-by`/`aggregates-into`/`aggregates-from`/`historically-influenced-by`) stored single-direction and audited for contradictions, and a **symmetric associative web** (`shares-vocabulary-with`/`structurally-parallel-to`/`often-conflated-with-NOT-equivalent`) where bidirectional storage is accepted. The standing audit keeps the skeleton honest going forward.

---


## ⟶ Rotated from progress.md on 2026-06-24 (Batch-34 close): Batch 32, Batch 33, Ch 13 run

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

---

---

## Batch 34 — darśana root-text author-anchors + Hindu serpent/bird iconography + Neoplatonic depth (2026-06-24)

### Startup reconcile
- Batches 1–33 + Ch-13 chapter run fully committed. Audit CLEAN at start: 251 nodes, 1491 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Ran in **parallel-research mode** (user request: "run 3–5 agents to fish for concepts"): **4 read-only scout agents** gathered §4 signal bundles for disjoint key-sets; all writing, dedup gating, and commits done **serially** in the main session. Parallelism confined to the safe (research) half — the dedup gate and one-commit-per-concept invariants stayed intact, the graph never forked.
- All 15 candidate filenames confirmed missing before writing; `vyasa` already existed → dropped from the pool (new nodes link to it instead).

### Batch 34 concepts (plan) — 15 concepts, three clusters

**Cluster A — darśana root-text author/source anchors (5):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | kanada | done | medium | founder of Vaiśeṣika; expressed-by vaiseshika-sutra |
| 2 | jaimini | done | medium | author of Mīmāṃsā Sūtra; expressed-by mimamsa-sutra |
| 3 | badarayana | done | medium | author of Brahma Sūtra; **contested** — Bādarāyaṇa=Vyāsa identity |
| 4 | vatsyayana | done | **high** | author of Nyāya-Bhāṣya; ≠ Kāmasūtra Vātsyāyana |
| 5 | vyasa-yogabhasya | done | **low** | Yogabhāṣya author; **contested** — authorship (Maas: =Patañjali) |

**Cluster B — Neoplatonic depth (4):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 6 | iamblichus | done | high | theurgy; the contemplation-vs-ritual break with Porphyry |
| 7 | psyche-neoplatonic | done | high | Soul, the third hypostasis; ≠ modern psyche / jīva / Brahman |
| 8 | proclus-henad | done | medium | the henads; mediating the One; origin contested (Iamblichus/Syrianus) |
| 9 | ammonius-saccas | **blocked** | low | Plotinus' teacher; wrote nothing, doctrine unattested |

**Cluster C — Hindu serpent/bird iconography + wish-objects (6):**

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 10 | jatayu | done | medium | Rāmāyaṇa vulture-demigod; dies fighting Rāvaṇa for Sītā |
| 11 | sampati | done | medium | elder vulture brother; locates Sītā on Laṅkā |
| 12 | kadru | done | medium | serpent-mother of the nāgas; co-wife rival of Vinatā |
| 13 | vinata | done | medium | mother of Garuḍa & Aruṇa; bird-line rival of Kadrū |
| 14 | shesha | done | **high** | cosmic serpent Śeṣa/Ananta; the remainder at pralaya (ananta = alias, NOT a separate node) |
| 15 | kalpavriksha | done | medium | wish-fulfilling tree of the churning; parallels Kāmadhenu |

## Run log — Batch 34 (2026-06-24)

### Concepts completed: 15 / 15 (1 blocked, 2 contested, 0 needs-opus-review)
Author-anchor payoff again: each darśana-author node gives a reverse-only root-text node a correctly-directed `expressed-by` inbound (kanada→vaiseshika-sutra, jaimini→mimamsa-sutra, badarayana→brahma-sutra). Neoplatonic depth completes the One→Nous→Soul triad (psyche-neoplatonic) and adds the henad/theurgy layer. Cluster C completes the Aruṇa/Vinatā/Kadrū avian-serpent family and the churning wish-objects.

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **badarayana** `contested`: authorship of the Brahma Sūtra converged, but the **Bādarāyaṇa = Veda-Vyāsa** identification is a later (8th–9th c.) overlay flagged as anachronism — mapped as a divergence table, drawn `often-conflated-with-NOT-equivalent → vyasa`.
- **vyasa-yogabhasya** `contested`/low: the modern single-author thesis (sūtra+bhāṣya = one *Pātañjalayogaśāstra* by Patañjali) traces to **one scholar (Maas)** reported by many — the §4 independence trap; confidence capped low. The "Vyāsa" ≠ legendary Mahābhārata Vyāsa (later honorific overlay).
- **ammonius-saccas** `blocked`: wrote nothing + "pledge of silence" ⇒ no doctrine to gloss; Christian-vs-pagan and "two Ammonii" both irreducibly contested; only tertiary modern sources exist (no SEP entry). Committed blocked with the absence recorded as the finding.
- **vatsyayana**: name-collision with **Vātsyāyana Mallanāga** (Kāmasūtra author) taught in prose, single node (the patanjali-grammarian precedent) — any future Kāmasūtra node must take a disambiguating key.
- **shesha/ananta**: resolved to **one node** (every source treats Ananta as an epithet, not a distinct being); ananta recorded as a verified alias, no `ananta.md` minted. The *śeṣa* = "remainder at pralaya" doctrine recorded precisely, NOT as a cosmological-physics claim.
- **kanada**: the *paramāṇu* atomism guardrail noted in-file — the "ancient Indian atom = modern physics" conflation belongs on the paramanu node, not the author file.
- Genuine source disagreements surfaced per §4: darśana-author **datings** all left as wide ranges (Kaṇāda, Jaimini, Vātsyāyana); proclus-henad **origin** (Iamblichus vs Syrianus); Jaṭāyu/Sampāti **genealogy** (encyclopedic "Śyenī as mother" vs Vālmīki's "Śyenī a distant ancestress, Aruṇa the father").

### De-orphan inbounds relocated into existing hubs (§5 forward-only / symmetric-where-apt; no mechanical mirroring beyond the established de-orphan practice)
`kumarila-bhatta → historically-influenced-by → jaimini` · `gautama-aksapada → structurally-parallel-to → kanada` (sym) · `pramana-nyaya → historically-influenced-by → vatsyayana` · `proclus → expressed-by → proclus-henad` (replacing `part-of: proclus` in the henad file to avoid a bidirectional-directional defect) · `plotinus → expressed-by → psyche-neoplatonic` · `vishnu → shares-vocabulary-with → shesha` (sym) · `kamadhenu → structurally-parallel-to → kalpavriksha` (sym) · `vyasa → often-conflated-with-NOT-equivalent → vyasa-yogabhasya`. The 8 within-cluster nodes (jatayu↔sampati, kadru↔vinata, iamblichus, badarayana) self-anchored via their cluster edges.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups. The `व्यास` DEVANAGARI flag (vyasa / vyasa-yogabhasya) is the **intended** tradition/identity split — carries the required `often-conflated-with-NOT-equivalent` edge, so the map teaches the distinction rather than forking.
- Graph regenerated: **251 → 266 nodes, 1491 → 1541 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 266 concepts across 34 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

---

## Batch 35 — churning-of-the-ocean cluster + darśana author-anchors + Neoplatonic/Greek depth (2026-06-26)

### Startup reconcile
- Batches 1–34 fully committed. Audit CLEAN at start: 266 nodes, 1541 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** (no scout agents this run — user did not request them). One concept end-to-end, then commit; dedup gate before each.
- All 12 candidate filenames confirmed MISSING before writing (Glob check). `naga` is NOT a node (the glob `naga*` matched `nagarjuna` only) → no nāga-class parent edge minted (would have been a dangling stub).

### Batch 35 concepts — 12 / 12 done (0 blocked, 2 contested, 0 needs-opus-review)

**Cluster A — darśana author/source anchors (3):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | prashastapada | done | medium | author of *Padārthadharmasaṃgraha*; the bhāṣya that overshadowed Kaṇāda's sūtra |
| 2 | mandana-mishra | done | medium | **contested** — Mīmāṃsā→Advaita bridge; the doubtful Maṇḍana=Sureśvara identity |
| 3 | vindhyavasin | done | **low** | Sāṃkhya reformer known only via Paramārtha's *Life of Vasubandhu* + Frauwallner; no extant work |

**Cluster B — Neoplatonic/Greek depth (4):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 4 | syrianus | done | **high** | Proclus's teacher; likely *originator* of the henads (resolves the contested origin to a node) |
| 5 | theurgy | done | **high** | salvation by ritual means (Iamblichus); the contemplation-vs-ritual break |
| 6 | damascius | done | **high** | last Athenian scholarch; the Ineffable (*arrhēton*) beyond the One |
| 7 | liber-de-causis | done | **high** | Proclus-derived "Book of the Pure Good"; long mistaken for Aristotle; Aquinas corrected it |

**Cluster C — Hindu churning cluster (5):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 8 | samudra-manthana | done | medium | the churning episode — apparatus + ratna-cluster anchor |
| 9 | vasuki | done | medium | king of nāgas; churning-cord; Śiva's neck-serpent; Kadrū's son |
| 10 | kurma | done | medium | **contested** — tortoise avatāra / churning-pivot; Vedic Prajāpati-tortoise reattributed to Viṣṇu |
| 11 | amrita | done | medium | nectar of immortality; IE cognate of Greek *ambrosia*; Buddhist *amata* reuse |
| 12 | dhanvantari | done | medium | physician of the gods; rises with the amṛta-pot; deity of Āyurveda |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **kurma** `contested`: the churning-pivot role converges, but the deeper identity splits diachronically — the **Śatapatha Brāhmaṇa cosmic tortoise = Prajāpati/Brahmā**, later *transferred* to Viṣṇu as Vaiṣṇavism rose. Mapped as a reading table; the Vedic→Vaiṣṇava shift is the finding, not a single timeless avatāra.
- **mandana-mishra** `contested`: Mīmāṃsā→Advaita bridge + Brahmasiddhi authorship converge, but the **Maṇḍana = Sureśvara** identification is "doubtful" and the debate-legend's subordination to Śaṅkara is questioned (he may have been the dominant Advaitin for a century). Two-question divergence table.
- **vindhyavasin** low conf: known **only at second hand** through a hostile Buddhist biography (Paramārtha) + Frauwallner's reconstruction (weak independence), **no extant work**; dates/king (Vikramāditya = Candragupta II?) contested. The batch-plan's "alternate Yogabhāṣya attribution" was **NOT supported by any source consulted** → explicitly dropped, not asserted.
- **amrita**: the Greek *ambrosia* cognate (PIE *\*n̥-mr̥-tós*) recorded as a **linguistic/structural** parallel, never an identity of myths; Buddhist *amata* = "the deathless" flagged as a reuse for a *different referent* (state, not nectar).
- **prashastapada**: the §4 commentary-tradition inversion noted — the most influential "bhāṣya" is really an independent compendium that **overshadowed the mūla-sūtra** (Vaiśeṣika doctrine anchored on the bhāṣya, not the sūtra).
- **liber-de-causis**: the headline *often-conflated-with-NOT-equivalent* case — a Proclan (Neoplatonic) text long worn as an **Aristotelian** mask until Aquinas (1272, via Moerbeke's Proclus) exposed it. Drawn as the conflation edge to `aristotle-substance`.
- **syrianus**: resolves the Batch-34 proclus-henad **origin** crux — SEP: the henads were "probably introduced by Syrianus himself," making him the likelier of the two candidates (vs Iamblichus); both candidate-origin edges now point to nodes.

### De-orphan inbounds relocated into existing hubs (established de-orphan practice; all purely-symmetric pairs, proven-clean)
`vishnu → shares-vocabulary-with → kurma` · `shiva → shares-vocabulary-with → vasuki` · `paramanu-vaisheshika → shares-vocabulary-with → prashastapada` · `advaita-vedanta → shares-vocabulary-with → mandana-mishra` · `vasubandhu → shares-vocabulary-with → vindhyavasin` · `plotinus-one → shares-vocabulary-with → damascius` · `plotinus-one → shares-vocabulary-with → liber-de-causis`.
Directional edges added to existing files: `proclus → historically-influenced-by → syrianus` (his actual teacher, previously missing) · `iamblichus → formalizes → theurgy` · `proclus-henad → historically-influenced-by → syrianus` (the second/likelier henad-origin candidate). The remaining new nodes (samudra-manthana, amrita, dhanvantari, syrianus, theurgy) self-anchored via cluster edges.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups; manifest in sync. Existing DEVANAGARI/SPLIT flags (ahimsa, vyasa, dravya, karma, moksa, paramanu, pramana, skandha) are the intended tradition-splits, unchanged.
- Graph regenerated: **266 → 278 nodes, 1541 → 1585 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 278 concepts across 35 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 36 (names only — no files written)
- **Churning cluster finish:** `halahala` (the poison Śiva drinks — Nīlakaṇṭha), `mohini` (Viṣṇu's enchantress who distributes the amṛta; the asura-trick), `rahu`/`ketu` (the beheaded asura → eclipse-demon), `parijata` (the churning-tree conflated with kalpavṛkṣa), `airavata`/`ucchaihshravas` (the churning steed and elephant), `lakshmi` already exists.
- **Daśāvatāra spine** (kurma now anchors it): `matsya` (first avatāra, the flood-fish — Manu/Noah parallel), `varaha` (boar, lifts the earth), `narasimha`, `vamana` (the three steps — ties to Bali of the churning frame).
- **Āyurveda** (dhanvantari opens it): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha) — a whole proto-medicine sub-graph.
- **Neoplatonic/Greek closure:** `simplicius` (Damascius's pupil, the great commentator), `marinus` (Proclus's successor), `pseudo-dionysius` (the Christian channel for Proclus — pairs with liber-de-causis as the *other* transmission line), `chaldean-oracles` (theurgy's source-text).
- **Mīmāṃsā/Advaita:** `sureshvara` (would let the Maṇḍana-identity edge resolve), `shankara`/`adi-shankara` (conspicuously still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya` (Vindhyavāsin's teacher).

---

## Batch 36 — daśāvatāra spine + churning-cluster finish (2026-06-28)

### Startup reconcile
- Batches 1–35 fully committed. Audit CLEAN at start: 278 nodes, 1585 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** (no scout agents). One concept end-to-end, then commit; dedup gate (Glob) before each.
- All 11 candidate filenames confirmed MISSING before writing. **Decision:** did NOT mint a separate `dashavatara` umbrella node — the existing `avatara-vedanta` already carries the daśāvatāra list; each new avatāra is `is-a-type-of: avatara-vedanta` (matching `kurma`).

### Batch 36 concepts — 11 / 11 done (0 blocked, 0 contested-as-status, 0 needs-opus-review)

**Cluster A — daśāvatāra spine (4; kurma/matsya already anchored it):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | matsya | done | medium | first avatāra, flood-fish; ŚB flood-fish → Brahmā (MBh) → Viṣṇu (Purāṇa) diachronic shift |
| 2 | varaha | done | medium | third avatāra, boar lifts earth, slays Hiraṇyākṣa; Vedic Emūṣa/Prajāpati → Viṣṇu |
| 3 | narasimha | done | medium | fourth avatāra, man-lion; the **boon-loophole** theology of the liminal; slays Hiraṇyakaśipu, saves Prahlāda |
| 4 | vamana | done | medium | fifth avatāra, dwarf/Trivikrama; grows from Viṣṇu's **own** Ṛgvedic three strides (NOT a Prajāpati reattribution) |

**Cluster B — churning-cluster finish (7):**
| # | concept | status | conf | notes |
|---|---|---|---|---|
| 5 | halahala | done | medium | churning-poison (Kālakūṭa) Śiva drinks; etiology of Nīlakaṇṭha |
| 6 | mohini | done | medium | Viṣṇu's enchantress-form; distributes amṛta; occasions Rāhu's beheading; avatāra-vs-māyā recorded |
| 7 | rahu | done | medium | severed head of Svarbhānu, eclipse-demon & ascending lunar node |
| 8 | ketu | done | medium | severed body of Svarbhānu, descending lunar node & comet-stratum |
| 9 | airavata | done | medium | churning white elephant, Indra's mount |
| 10 | ucchaihshravas | done | medium | churning seven-headed horse; hinge of the Kadrū–Vinatā wager |
| 11 | parijata | done | medium | churning-tree & Kṛṣṇa–Satyabhāmā episode; the Pārijāta=Kalpavṛkṣa conflation mapped |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **The Prajāpati→Viṣṇu reattribution thread** (matsya/varaha, echoing kurma): the Vedic Brāhmaṇa cosmic animals (flood-fish, boar Emūṣa) were **Prajāpati/Brahmā**, later transferred to Viṣṇu as Vaiṣṇavism rose — recorded as a diachronic shift (image continuous, theology not), NOT a timeless avatāra. ŚB 14.1.2 explicitly harmonizes Emūṣa into Prajāpati.
- **vamana** is the deliberate contrast case: NOT a reattribution — the avatāra grows from **Viṣṇu's own** Ṛgvedic Trivikrama (1.154); but "neither Bali nor Vāmana appears in" the Vedic strides → the dwarf-frame is the later accretion. Two distinct kinds of Vedic continuity kept apart.
- **rahu/ketu** §0 case: the eclipse-by-swallowing **myth** is NOT an astronomical eclipse theory; classical siddhāntic astronomy gave the shadow/node account **separately**, and the node-points merely took the names Rāhu/Ketu. Mapped as **naming + correlation, not identity** — explicitly resisting "the ancients secretly knew the lunar nodes."
- **mohini** classification divergence: avatāra vs Viṣṇu's *māyā* — function stable, label contested; linked to avatara-vedanta as shares-vocabulary (not is-a-type-of) to honor the open classification.
- **parijata** §5 headline conflation: Pārijāta and Kalpavṛkṣa are **distinct named members** of the five celestial trees (pañca-vṛkṣa: Mandāra/Pārijāta/Santāna/Kalpavṛkṣa/Haricandana), yet "Kalpavṛkṣa" is **also** the class-name — so Pārijāta is "a kalpavṛkṣa" generically while ≠ the tree *named* Kalpavṛkṣa. Drawn as `shares-vocabulary-with` + `often-conflated-with-NOT-equivalent` (the sanctioned two-type pair).

### De-orphan inbounds relocated into existing hubs (established practice; pure-symmetric pairs, no hierarchy on those pairs, proven-clean)
`vishnu → shares-vocabulary-with → vamana` · `shiva → shares-vocabulary-with → halahala` · `kalpavriksha → shares-vocabulary-with / often-conflated-with-NOT-equivalent → parijata`. The other 8 new nodes self-anchored via intra-batch cluster edges (matsya↔varaha↔narasimha; mohini↔rahu↔ketu; airavata↔ucchaihshravas; ucchaihshravas→kadru/vinata/garuda) and existing hubs.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Existing DEVANAGARI/SPLIT ~groups (moksa, paramanu, pramana, skandha, etc.) are intended tradition-splits, unchanged.
- Graph regenerated: **278 → 289 nodes, 1585 → 1636 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 289 concepts across 36 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

---

## Batch 37 — daśāvatāra completion + churning loose ends (2026-07-09)

### Startup reconcile
- Batches 1–36 fully committed. Audit CLEAN at start: 289 nodes, 1636 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked **serially** with a research fork per concept (one concept in progress at a time; each fork's findings synthesized and written by the primary agent, never delegated wholesale). Dedup gate (Glob) before writing.
- Cluster chosen via user forced-choice (§10 genuine fork — "what to build next" among 4 suggested clusters from Batch 36's suggestion list): **daśāvatāra + churning loose ends**, 7 concepts.

### Batch 37 concepts — 7 / 7 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | parashurama | converged | medium | sixth daśāvatāra; unique avatāra-to-avatāra overlap — meets Rāma directly in Rāmāyaṇa Bāla Kāṇḍa 74–76; daśāvatāra list-instability caveat (Balarāma/Buddha swap doesn't touch his slot) |
| 2 | kalki | converged | medium | tenth/future daśāvatāra; two-tier confidence split (cosmological core high, Puranic biographical chain medium — Viṣṇu Purāṇa→Bhāgavata→Kalki Purāṇa is textual inheritance, not triangulation); Vāyu Purāṇa's rival Pramīti noted; Kālacakra vocabulary-borrowing flagged, not equated |
| 3 | bali | contested | medium | Mahābali, Vāmana's foil; TWO distinct contested splits mapped: grace-vs-punishment (Sutala-as-elevation vs Garuḍa-drags-him-down) and devotional-vs-Dravidian-historiographical readings of Onam |
| 4 | indra | contested | medium | hub node closing 7 prior dangling inbound refs (airavata, ucchaihshravas, vamana, bali, samudra-manthana, krishna, agni); Doniger-sourced Vedic-supremacy→Puranic-demotion divergence as central finding; etymology deliberately left unresolved |
| 5 | kaustubha | converged | medium | churning-gem on Viṣṇu's chest; uncontested member of the variable 14-ratnas list; continuous into Kṛṣṇa's iconography |
| 6 | varuni | contested | medium | churning-wine-goddess; Rāmāyaṇa (devas accept) directly contradicts Bhāgavata Purāṇa 8.8.30 (asuras take her); sura/asura wordplay flagged as folk/narrative etymology, NOT the scholarly Proto-Indo-Iranian derivation |
| 7 | svarbhanu | contested | medium | pre-beheading whole resolving Rāhu/Ketu origin; genuine two-layer finding — independent Ṛgveda 5.40 Atri-restores-the-sun eclipse myth vs. the Puranic churning-beheading myth, linked by name-continuity not plot-continuity; identity (Sāyaṇa) vs whole-then-split (Wikipedia) contested via the sanctioned shares-vocabulary + conflated-NOT-equivalent edge pair |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **kalki**: explicitly separated a high-confidence cosmological-role tier from a medium-confidence biographical tier, because the biographical detail (village, parents, horse-name) traces a Viṣṇu Purāṇa→Bhāgavata→Kalki Purāṇa elaboration chain — exactly the "copies are not confirmation" trap in §4 signal 1.
- **bali**: two independent contested axes on the same figure (theological grace/punishment; cultural devotional/Dravidian-historiographical) kept as two separate tables rather than merged into one, since they split along different source-clusters.
- **indra**: the demotion arc (Ahalyā curse, Govardhana humbling, Bali's conquest) is the central finding — Indra's Vedic supremacy is not a static fact carried into the epics/Purāṇas but a documented decline (Doniger, *Encyclopedia of Religion*), paralleling Varuṇa's decline (no `varuna.md` yet — flagged, not linked).
- **varuni**: a direct textual contradiction between two primary sources (Rāmāyaṇa vs Bhāgavata Purāṇa) on who accepts her — recorded as genuine contestation, not resolved by picking the "more authoritative" text.
- **svarbhanu**: the load-bearing finding is that "Svarbhānu" names two textually unconnected myths (Vedic eclipse-etiology vs. Puranic amṛta-theft) sharing only a name — the file explicitly resists reading the older Vedic layer as a proto-version of the churning story.
- A Grokipedia (AI-generated tertiary) hit was explicitly excluded as a source during svarbhanu research, consistent with the same exclusion made during bali research — noted as a recurring, correct discipline, not a one-off.

### De-orphan inbounds relocated into existing hubs (established practice; pure-symmetric pairs, no hierarchy on those pairs, proven-clean)
`vishnu → shares-vocabulary-with → parashurama` · `vishnu → shares-vocabulary-with → kalki` · `samudra-manthana → shares-vocabulary-with → kaustubha` · `samudra-manthana → shares-vocabulary-with → varuni` · `rahu ↔ svarbhanu` (shares-vocabulary-with + often-conflated-with-NOT-equivalent, the sanctioned two-type pair) · `ketu → shares-vocabulary-with → svarbhanu`. `bali` and `indra` self-anchored via dense intra-batch/existing-hub cross-links (narasimha, vamana, krishna, airavata, ucchaihshravas, agni).

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- **First pass found 4 orphans** (kalki, kaustubha, parashurama, varuni — written but not yet a target of any edge) — resolved by adding the hub-inbound edges above; **second pass CLEAN**: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE.
- `find_duplicates.py`: 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Existing DEVANAGARI/SPLIT groups unchanged.
- Graph regenerated: **289 → 296 nodes, 1636 → 1669 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"`; `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed (manifest in sync).

### Corpus milestone: 296 concepts across 37 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 38 (names only — no files written)
- **Āyurveda** (dhanvantari opens it, still unclaimed): `ayurveda`, `sushruta`, `charaka`, `tridosha` (vāta/pitta/kapha).
- **Neoplatonic/Greek closure:** `simplicius`, `marinus`, `pseudo-dionysius`, `chaldean-oracles`.
- **Mīmāṃsā/Advaita:** `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by mandana-mishra, advaita-vedanta), `varsaganya`.
- **Newly opened by this batch:** `varuna` (Indra's Vedic-decline parallel, cited in indra.md but unwritten), `atri` (the RV 5.40 sage who restores the sun, cited in svarbhanu.md but unwritten), `balarama` (Kṛṣṇa's brother, cited in varuni.md but unwritten), `prahlada` (Bali's grandfather, cited in bali.md but unwritten), `vritra`/`verethragna` comparanda cluster (Indo-European dragon-slaying — flagged in indra.md as a future structurally-parallel-to candidate, not yet a node).

## Batch 39 — Āyurveda opening cluster (2026-07-10)

### Startup reconcile
- Batches 1–38 fully committed. Audit CLEAN at start: 300 nodes, 1686 edges, 0 orphans, 0 stubs. Working tree clean — no interrupted draft.
- Worked serially, one concept end-to-end then commit. Dedup gate (Glob) before writing each file — confirmed `ayurveda`/`sushruta`/`charaka`/`tridosha` all unclaimed; `dhanvantari.md` already existed and explicitly names Āyurveda/Suśruta as unclaimed forward-references.
- Cluster chosen autonomously (user directive: proceed without asking, assume reasonably) from progress.md's four suggested Batch-39 clusters: **Āyurveda**, the most self-contained. Mīmāṃsā/Advaita, the carried-over Vedic-figures cluster, and Eriugena/Psellos were left for a future batch.

### Batch 39 concepts — 4 / 4 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | ayurveda | converged | medium | the umbrella medical tradition; flagged the honest gap between the popular "5,000-year-old" claim and Wikipedia's sourced "first centuries CE" dating for the classical texts; scientific-critique material (doshas "fictional," no cancer-cure evidence, rasaśāstra heavy-metal toxicity) recorded as the external secular assessment, held separate from the internal doctrinal account |
| 2 | charaka | contested | medium | the internal-medicine Saṃhitā + its eponymous physician; three-layer redaction (Agniveśa → Charaka → Dṛḍhabala) surfaced; `status: contested` set specifically for Chattopadhyay's "lineage not person" thesis vs. the traditional individual-author reading; Britannica fetch blocked (HTTP 403) and flagged as a sourcing gap rather than papered over |
| 3 | sushruta | contested | medium | the surgery-centered Saṃhitā + its eponymous physician; Dhanvantari-vs-Divodāsa manuscript-framing split (oldest MSS attribute directly to Divodāsa); flagged a genuine rigor-divergence between Meulenbeld's philological caution (Wikipedia) and a peer-reviewed PMC medical-history source's flat, uncritical "~600 BCE" dating with no debate acknowledged at all |
| 4 | tridosha | converged | medium | vāta/pitta/kapha, each a mahābhūta-pairing; *duṣ*-root etymology (imbalance, not inherent harm); open item honestly flagged — two comparative-review PDFs (Charaka/Suśruta/Vāgbhaṭa treatment differences) could not be read (fetch tool returned unparseable binary/OCR), so that deeper cross-textual comparison is deferred |

### Prime-directive / honest-divergence findings recorded (not smoothed over)
- **ayurveda**: the "5,000 years old" self-presentation vs. the textually-verifiable "first centuries CE" dating band — recorded as a real gap, not rounded away.
- **charaka**: Chattopadhyay's claim that "Charaka" names a lineage/sect rather than an individual, set against the traditional-author reading assumed by most popular medical-history literature — presented as contested, not resolved.
- **sushruta**: two internal-tradition attribution frames (printed editions: Dhanvantari teaching a group including Sushruta; oldest manuscripts: direct Divodāsa attribution) plus a cross-genre rigor gap — a peer-reviewed PMC piece asserts an unqualified "~600 BCE" date with zero historiographical caveat, while the Meulenbeld-sourced Wikipedia account treats the dating as a live, unresolved 2000 BCE–6th c. CE range.
- **tridosha**: an open item honestly logged rather than silently dropped — the intended three-way Charaka/Suśruta/Vāgbhaṭa comparative-elaboration content could not be sourced this round because both comparative-review PDFs returned as unreadable binary content via the fetch tool.
- Two Britannica fetches (charaka.md, ayurveda-adjacent) returned HTTP 403 and were recorded as sourcing gaps rather than silently substituted with an indirect citation.

### Cross-tradition honesty-layer edges added (new, this batch)
- `ayurveda often-conflated-with-NOT-equivalent prakriti-samkhya` (paired with `shares-vocabulary-with` on the same ordered pair, the one sanctioned two-type combination) — Āyurvedic *prakṛti* (individual dosha-constitution) vs. Sāṃkhya *prakṛti* (cosmic primal matter): same word, different tradition, not the same concept at different scales.
- `tridosha often-conflated-with-NOT-equivalent guna-samkhya` — the dosha (physiological) and guṇa (psychological, sattva/rajas/tamas) personality-classification layers are sometimes run together in popular wellness literature as one system; they are two distinct schemes over the same person.
- `charaka structurally-parallel-to sushruta` / `sushruta structurally-parallel-to charaka` (symmetric type, both directions written independently from each node's own vantage per §5's storage rule) — same core subjects, opposite emphasis (internal medicine vs. surgery), unresolved relative chronology.

### Audits (deterministic, via build_graph audit_graph + find_duplicates.py)
- Single pass CLEAN: dangling stubs NONE, orphans NONE, bidirectional-directional edges NONE, forbidden hier+similarity combos NONE. (No orphans to resolve this batch — every new concept picked up an inbound edge naturally via the `structurally-parallel-to`/`shares-vocabulary-with` cluster above plus each `formalizes: ayurveda` edge.)
- `find_duplicates.py`: exit 0, 0 hard-collision groups (IAST/TRANSLIT/PHANTOM); manifest in sync. Pre-existing DEVANAGARI/SPLIT groups (aḥiṃsā, vyāsa pairs) unchanged, not touched by this batch.
- Graph regenerated: **300 → 304 nodes, 1686 → 1700 edges**. `graph.svg` re-rendered via `"C:\Program Files\Graphviz\bin\dot.exe"` (Graphviz not on PATH this session — explicit binary path used, same as Batch 38); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` refreshed.

### Corpus milestone: 304 concepts across 39 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 40 (names only — no files written)
- **Mīmāṃsā/Advaita** (carried over, untouched this round): `sureshvara`, `shankara`/`adi-shankara` (still unwritten — referenced by `mandana-mishra`, `advaita-vedanta`), `varsaganya`.
- **Carried over from Batch 37/38:** `varuna` (Indra's Vedic-decline parallel, cited in `indra.md`), `atri` (RV 5.40 sage, cited in `svarbhanu.md`), `balarama` (cited in `varuni.md`), `prahlada` (Bali's grandfather, cited in `bali.md`), `vritra`/`verethragna` comparanda cluster (cited in `indra.md`); `eriugena` (cited in `pseudo-dionysius.md`); `psellos`/`michael-psellos` (cited in `chaldean-oracles.md`).
- **Newly opened by this batch:** a possible `vagbhata` node (Aṣṭāṅga Hṛdayam author, the third major classical Āyurveda authority alongside Charaka/Suśruta — named in `ayurveda.md` and `sushruta.md` but not yet a node); the Āyurveda cluster's own internal open item (a `dhatu`/`mala` node — the seven-tissue/waste-product framework mentioned in `ayurveda.md` but not yet broken out as its own concept).

---

## Batch 40 — Advaita founders pair (2026-07-10)

### Startup reconcile
- Batches 1–39 fully committed; working tree clean; audit CLEAN at start (304 nodes, 1700 edges).
- Cluster chosen autonomously from Batch-40 suggestions (user directive: extended autonomous session): the **twice-carried-over Mīmāṃsā/Advaita pair `shankara` + `sureshvara`** — the most-referenced unwritten keys in the corpus (`advaita-vedanta`, `atman-vedanta`, `brahman`, `maya-advaita`, `mandana-mishra` all cite Śaṅkara). `varsaganya`, the Vedic-figures cluster, Eriugena/Psellos, and the newly-opened `vagbhata`/`dhatu` items remain for a future batch.
- Dedup gate: Glob confirmed neither `shankara*` nor `*sureshvara*` existed; grep confirmed no `## Links` target had yet reserved either key; canonical key `shankara` chosen (matches the corpus founder-file convention — kanada, kapila, patanjali — and every existing file's prose usage) with Ādi Śaṅkara as in-file alias.

### Batch 40 concepts — 2 / 2 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | shankara | converged | medium | SEP + Wikipedia independently agree on the authentic-works list (Brahmasūtra-bhāṣya, ten Upaniṣad bhāṣyas, Gītā-bhāṣya, Upadeśasāhasrī) against the 300+-text attribution problem (Vivekacūḍāmaṇi "mostly rejected" — flagged because two existing files list it as a future fetch *as Śaṅkara's*); the honest headline is the **history-vs-hagiography gap**: "relatively unknown during his life-time," overshadowed by Maṇḍana Miśra, unmentioned for centuries, fame constructed in the 14th-c. Vijayanagara period (Vidyāraṇya) and amplified by Neo-Vedānta — recorded as a two-layer evidential standing, not smoothed |
| 2 | sureshvara | converged | medium | the Vārttikakāra disciple; Naiṣkarmyasiddhi (423 vv.) + the two great vārttikas; signature avidyā-locus doctrine (in **Brahman**, vs Maṇḍana's jīva — āśraya/viṣaya distinction recorded); the **Maṇḍana=Sureśvara identity left contested** (Kuppuswami Sastri: distinct; Balasubramanian: unproven) convergent with the existing mandana-mishra.md's independent record; a dating tension (9th-c. claim vs direct-disciple status under a 700–750 Śaṅkara) flagged rather than resolved |

### Honesty-layer edges added
- `shankara often-conflated-with-NOT-equivalent shiva` — the philosopher is not the god whose name he shares; devotional literature exploits the pun; the map now teaches the name-collision.
- `shankara structurally-parallel-to kundakunda` — each tradition's most authoritative philosopher-monk whose attributed corpus far exceeds the authentic one and whose biography is hagiographic accretion.
- `sureshvara often-conflated-with-NOT-equivalent mandana-mishra` (stored both directions per §5 symmetric-storage rule; the mirror edge in mandana-mishra.md also resolved this batch's one audit defect — sureshvara orphanhood) — the debate-conversion legend vs the doctrinal oppositions (locus of avidyā; role of meditation).

### Audits
- First build pass flagged **orphan: sureshvara** → fixed per §10 by adding the mirror symmetric edge in mandana-mishra.md (content-motivated, not a mechanical mirror — written from Maṇḍana's vantage). Re-run: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0; pre-existing DEVANAGARI/SPLIT groups unchanged.
- Graph: **304 → 306 nodes, 1700 → 1711 edges**; `graph.svg` rendered via explicit `"C:\Program Files\Graphviz\bin\dot.exe"` (Graphviz still not on PATH — same workaround as Batches 38/39); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` regenerated.

### Also completed this session (other two tracks, committed separately)
- **Chapters 16 (Nyāya & Vaiśeṣika) and 17 (Mīmāṃsā & Cārvāka)** drafted — the six āstika darśanas are now all covered in the teaching layer; next planned chapter is **Ch 18 (Hindu Deities)**.
- **Translation reading-room units #10–13 (TS Adhyāyas 7, 3, 4, 10)** — **the Tattvārtha Sūtra is now complete in the reading room: all ten adhyāyas, both recensions, first pass.** Headline finds logged in `chapters/jain/translations/INDEX.md` (the "block promotion" fork type at sizes 5/21/1; the 26-vs-39 heavens divergence; the strīmokṣa split living in commentary on a shared sūtra).

### Corpus milestone: 306 concepts across 40 batches. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 41 (names only — no files written)
- **Carried over (again):** `varsaganya` (Sāṃkhya teacher, cited in `samkhya-karika`-adjacent material); `varuna`, `atri`, `balarama`, `prahlada`, `vritra`/`verethragna` (Vedic-figures cluster); `eriugena`; `psellos`/`michael-psellos`.
- **Āyurveda continuation:** `vagbhata`; `dhatu`/`mala`.
- **Newly opened by Batch 40:** `padmapada` (Śaṅkara's other direct disciple, named in `sureshvara.md` — the Vivaraṇa-prasthāna counterpart to the Vārttika school); `gaudapada` (Śaṅkara's parama-guru, Māṇḍūkya-kārikā author — named in `advaita-vedanta.md` and `shankara.md` but not yet a node); `vidyaranya` (the 14th-c. fame-constructor, named in `shankara.md`).

---

## Batch 41 — the Advaita lineage completed (2026-08-26)

### Startup reconcile
- Batches 1–40 committed; working tree clean at start; audit CLEAN (306 nodes, 1711 edges).
- Session began on the **chapter** track and exhausted it: Chapters 24–28 drafted (see below), after which the re-derived roadmap came back empty and the standing rule sent work to the concept track.
- Cluster chosen from the Batch-41 suggestions: the three **Advaita lineage** keys opened by Batch 40 and leaned on hard by Ch 25 — `gaudapada`, `padmapada`, `vidyaranya`. All three are named in existing files' prose and none had a node.
- Dedup gate for each: `Glob concepts/<key>*.md` returned nothing; grep confirmed no `## Links` target had reserved any of the three keys.

### Batch 41 concepts — 3 / 3 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | notes |
|---|---|---|---|---|
| 1 | gaudapada | contested | medium | Wikipedia + IEP, independently authored, agree **exactly** on the Māṇḍūkya-kārikā's 215 verses / four chapters (29·38·48·100), ajātivāda, turīya, asparśa-yoga and the paramaguru relation — and **disagree on the dating**, with the two Buddhist arguments running in opposite directions (dated by who cites him vs by whom he cites; 4th–7th c. spread). Three live disputes recorded as findings: the date, chapter 4's authorship (six positions tabulated — Murti, King, Bhattacārya, Sarma, Nikhilananda, Mayeda; with the hard datum that later Advaitins quote only chs. 1–3), and IEP's explicit **"multiple Gauḍapāda-s."** |
| 2 | padmapada | converged | medium | mid-8th c., direct disciple; the Pañcapādikā surviving as a gloss on the **first four aphorisms** only; Prakāśātman's 10th-c. Vivaraṇa naming the school; *pratibimbavāda*. The substance is the Vivaraṇa/Bhāmatī locus-of-avidyā split, which **independently corroborates Batch 40** from a different source-set — the founding generation divides into two camps, not four positions, with Padmapāda and Sureśvara on the same side. Records Satchidānandendra Sarasvatī's dissent that the whole locus debate misconstrues Śaṅkara, who held avidyā beginningless and its origin fruitless to seek. |
| 3 | vidyaranya | contested | medium | 1296–1391, Śṛṅgeri jagadguru; the other end of `shankara.md`'s fame-construction claim. Three open identifications (Mādhava/Vidyāraṇya; the SDS's authorship, with Cannibhaṭṭa named against tradition; the Digvijaya) and the Vijayanagara foundation story judged **legendary** — no contemporary inscriptions, "imagined probably at least 200 years afterward," a political foundation myth. Confidence honestly capped because signal 2 is a second article on the **same platform**. |

### Findings that reach beyond their own nodes
- **A near-miss the dedup gate caught.** `samkhya-karika.md` already listed a "Gauḍapāda-bhāṣya" among its commentaries, so the corpus was one edge away from silently merging the Advaitin with the Sāṃkhya commentator. IEP's "multiple Gauḍapāda-s" is now stored as an explicit `often-conflated-with-NOT-equivalent` so the map teaches the doubt.
- **A fourth interested-channel case.** The *Sarva-darśana-saṅgraha* is one of very few surviving sources on Cārvāka and ranks it lowest by design, in a hierarchy built to end at Advaita. That joins the Chaldean Oracles (Ch 24 §4.4), Vindhyavāsin (Ch 25 §8) and Makkhali Gosāla (Ch 27 §8).
- **An internal tension flagged, not smoothed.** `shankara.md` and Ch 25 §3.2 date "Mādhava's Śaṅkaradigvijaya" to the **17th century**; Vidyāraṇya died in **1391**. Reconcilable only if the attribution is pseudepigraphic — which is what "attribution disputed" would mean — but no source states that reconciliation, so it is recorded in `vidyaranya.md` as the likely explanation and **not** as a finding. **Whoever next upgrades either node must resolve this first.**

### Honesty-layer edges added
- `gaudapada often-conflated-with-NOT-equivalent samkhya-karika` — the multiple-Gauḍapādas problem, so the Advaitin is not silently merged with the Sāṃkhya commentator.
- `gaudapada shares-vocabulary-with madhyamaka` **and** `often-conflated-with-NOT-equivalent madhyamaka` — the §5 sanctioned two-type pattern: the Yogācāra/Mādhyamika borrowing is real and extensive, and a positive unborn Ātman-Brahman is still what Madhyamaka denies.
- `shankara historically-influenced-by gaudapada` added to `shankara.md`, which named him in prose but carried no edge.
- `vidyaranya structurally-parallel-to marinus` and `structurally-parallel-to simplicius` — the successor-hagiographer and the interested-transmission-channel patterns, drawn across traditions.

### Audits
- Build pass 1 flagged **orphans: padmapada, vidyaranya** -> fixed per §10 with two **content-motivated** symmetric mirrors, each written from its own node's vantage (not mechanical mirroring): `sureshvara -> shares-vocabulary-with -> padmapada` (the two disciples, the two lineages, the same side of the locus question) and `marinus -> structurally-parallel-to -> vidyaranya` (with the disanalogy stated in the note). Re-run: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0; pre-existing DEVANAGARI/SPLIT groups unchanged.
- Graph: **306 -> 309 nodes, 1711 -> 1733 edges**; `graph.svg` rendered via the explicit `"C:\Program Files\Graphviz\bin\dot.exe"` path (Graphviz still not on PATH — same workaround as Batches 38–40); `graph.dot`/`graph.html`/`index.md`/`MANIFEST.tsv` regenerated.

### Also completed this session (chapter track, committed separately)
- **Chapters 24–28 drafted, closing the teaching layer.** Ch 24 (Later Neoplatonists), Ch 25 (the commentators and the identity problems), Ch 26 (the Jain karma machinery), Ch 27 (Buddhist process + two adversaries), Ch 28 (the modern-physics comparanda — the §0 chapter). The roadmap was re-derived twice and is now **complete**: every one of the 306 nodes then in `concepts/` has a chapter home.

### Open follow-ups (not acted on — deliberately left for a maintenance pass)
1. **`ajiva.md` stores `part-of: jiva`**, which inverts the partition its own note describes. The controlled vocabulary has no **complement-of** relation, so this is a schema question, not a typo (Ch 26 §2.3).
2. **`many-valued-logic` carries `tradition: Modern Physics`** — it is formal logic, and the mis-tag mis-colours the node in the rendered graph (Ch 28 §5).
3. **`atman-vedanta.md` and `brahman.md` both queue a Vivekacūḍāmaṇi fetch *as Śaṅkara's***; per Ch 25 §3.1 it must be re-scoped to *attributed*.
4. **Ch 11 predates `shankara`/`sureshvara`/`mandana-mishra`/`gaudapada`/`padmapada`** and should be re-read against Ch 25 §§3–6 and this batch.
5. The **Digvijaya dating tension** above.

### Corpus milestone: 309 concepts across 41 batches; 28 chapters. 0 orphans. 0 unwritten stubs. Audit CLEAN.

### Suggested Batch 42 (names only — no files written)
- **Opened by this batch:** `prakasatman` (the Vivaraṇa school's namesake, 10th c.); `vacaspati-mishra` (the Bhāmatī school's namesake — the corpus now describes the split from only one side); `govinda-bhagavatpada` (the missing link between Gauḍapāda and Śaṅkara).
- **Opened by Chs 24/27:** `psellos` (the separate Byzantine transmission line for the Chaldean Oracle fragments); `prajnakaragupta` (who challenged Dharmottara's *niścaya-pratyaya*); `utpaladeva` (Pratyabhijñā — named across Ch 18 and Ch 27 and still unwritten).
- **Opened by Ch 26:** the four ***aghāti* karmas** — the corpus has no node for them at all, and Ch 26 §6.4 flags the residual *yoga*-driven influx in a kevalin as a genuine hole.
- **Carried over (again):** `varsaganya`; the Vedic-figures cluster (`varuna`, `atri`, `balarama`, `prahlada`, `vritra`/`verethragna`); `eriugena`; and the Āyurveda continuation `vagbhata`, `dhatu`/`mala` — the last of which Ch 23 calls "a hole in the chapter."

---

## Batch 42 — post-Śaṅkara Advaita, the Āyurvedic body, the Jain aghāti half, and the asura question (2026-08-26)

### Startup reconcile
- Batches 1–41 committed; working tree clean at start; audit CLEAN (309 nodes, 1733 edges).
- Took the **Suggested Batch 42** list from the Batch-41 run-log and worked it end to end, including every "carried over (again)" item.
- Dedup gate run for all twenty keys: `Glob concepts/<key>*.md` returned nothing for any of them, and a grep of all `## Links` targets confirmed none had been reserved.

### Batch 42 concepts — 20 / 20 done (0 blocked, 0 needs-opus-review)

| # | concept | status | conf | the finding |
|---|---|---|---|---|
| 1 | prakasatman | contested | medium | *mūlāvidyā* as **positive (*bhāvarūpa*) beginningless** material cause — the doctrinal hinge of all later Advaita. Date **contested across three centuries** (10th c. per IEP/wisdomlib vs c. 1200–1300 per Wikipedia ×2 + Hindupedia), with **no source arguing** for a date. Adds the *pratibimba*/*avaccheda*/*ābhāsa* three-way table. |
| 2 | vacaspati-mishra | contested | medium | The Bhāmatī side of the locus split finally stated **by its own partisans**, and it matches what IEP said from the Vivaraṇa side. New: avidyā is **plural** in Bhāmatī ("plural since the jīvas are plural"). Date rests on one colophon reading **898** with the **era unstated** — Vikrama gives 840, Śaka 976. Records a **visible reference-work error** (Hindupedia gives him Śaṅkara's dates, 788–820). |
| 3 | govinda-bhagavatpada | contested | **low** | The lineage's load-bearing joint, attested only by the lineage. Four attributions tabulated with **four different reasons** each fails. The Narmada episode read for *what it does*: Śaṅkara supplies the doctrine **before** initiation. |
| 4 | utpaladeva | contested | medium | *pratyabhijñā* **does not occur in Somānanda's *Śivadṛṣṭi*** — the second man supplies the thesis. The lost *Vivṛti*'s largest fragment survives **in the margins of Abhinavagupta's *Vivṛtivimarśinī***; Śaṅkarakaṇṭha's 17th-c. notes date the decay. Journal-grade (Ratié ×2). |
| 5 | aghati-karma | converged | medium | **TS 8.11 enumerates 42** subdivisions of *nāma* against the systematised **93** — and every other count checkable against the sūtra matches, so the whole 148-vs-sūtra gap is inside *nāma* and equals **51**. Only visible because three sūtras were fetched directly. Also: *tīrthakaratva* is item 42. |
| 6 | iryapathika-asrava | converged | medium | **TS 6.4 fetched**, closing the sourcing gap `asrava.md` had flagged against itself. Guṇasthāna **11–13**; "the *īryāpatha* karmas do not have the power to bind." Stage 11 suppresses rather than destroys passion, so *akaṣāya* is **operational**, not biographical. |
| 7 | dhatu | contested | medium | Classical Āyurveda transmits **three incompatible nourishment mechanisms simultaneously** (*kṣīra-dadhi* / *kedārī-kulyā* / *khale-kapota*), each explaining what the others cannot. Contested **by design**, not by scholarly disagreement. |
| 8 | mala | converged | medium | The *dhātu-mala* of **rasa is kapha** and of **rakta is pitta** — two of the three doṣas appear as tissue wastes, reversing the standard picture. *Vāta* has **no row**, flagged. |
| 9 | agni-ayurveda | converged | medium | **§8 tradition-split** from the Vedic deity `agni`, with the sanctioned two-type edge. Four states of *jāṭharāgni* keyed to the doṣas — a **non-linear** model in which one pathology (*viṣamāgni*) is instability, not a quantity. |
| 10 | vagbhata | contested | medium | The AH **travelled** — Tibetan, Arabic, Persian. Authorship kept in **two** forms usually conflated: the traditional Elder/Junior harmonisation vs philology's merely **negative** verdict. The AS colophon is already a grandson explaining a homonym. |
| 11 | varsaganya | contested | **low** | Reconstructed **entirely out of Vācaspati Miśra's citations** (Frauwallner). Two literatures that **do not meet**: Wikipedia attributes the *Ṣaṣṭitantra* to Pañcaśikha and does not mention him at all. |
| 12 | psellos | contested | medium | The Oracles survive largely because an **11th-c. Christian** quoted them; his is "the most extensive surviving commentary" and the route back to Proclus's lost treatise. **des Places 1971 omits fragments he quotes** — the problem does not stop at antiquity. 1054 charge from the future Patriarch. |
| 13 | eriugena | contested | medium | Built a complete Neoplatonic system and **"did not have direct knowledge" of Plotinus or Proclus**. *nihil per excellentiam* typed **NOT-equiv** *śūnyatā* — a superlative predicated of a plenum vs an absence asserted to block any source. |
| 14 | prajnakaragupta | converged | medium | The name four corpus files already cited. Says what he **rejected** (Dharmottara's *niścaya-pratyaya*) and explicitly **not** what he proposed. Serves as the **control case** for evidence-vs-reading confidence. |
| 15 | vritra | contested | medium | Dragon or **obstruction**? Benveniste & Renou against the combat-myth reading, with the neuter-abstract morphology as the hinge. |
| 16 | verethragna | contested | medium | **The corpus's first Iranian node.** The *Bahrām Yašt*'s ten forms contain **no adversary** — the strongest datum for the abstract reading. Three-way dispute mapped (traditional / Benveniste-Renou / **Thieme's functional merger**). |
| 17 | varuna | contested | medium | *asura* at RV 5.63.3 is an **approving** title of the supreme moral god. The *pāśa*, the thousand-eyed spies, RV 7.86–88's confessions, the *Varuṇapraghāsa* wife's confession — a **conscience-religion that did not become the mainline**. Dumézil's Ouranos etymology recorded as **withdrawn**. |
| 18 | balarama | contested | medium | Jainism **enrols** both brothers among the 63 *śalākāpuruṣa*s and then **reverses the ranking**: Kṛṣṇa (ninth *Vāsudeva*) is reborn in hell for his violence, Balarāma (ninth *Baladeva*) is liberated directly. |
| 19 | prahlada | converged | medium | *navavidhā bhakti* (BhP 7.5.23–24) read **in order** as a progression of intimacy; and **portable** — the *Śiva Purāṇa* lists the same nine for Śiva. |
| 20 | atri | contested | medium | "Atri's eclipse": **three dates 391 years apart, two from the same authors**, from a hymn containing no date. The corpus **declines** the datings without asserting them false. |

### Chapters written over the new nodes — 5 (Chs 29–33)
- **Ch 29 — How Things Reach Us** (`cross-tradition/`): the transmission chapter. Four channel-types with the corpus's full inventory and each one's failure mode; the Chaldean Oracles' two filters; Prajñākaragupta as the control case; Atri's eclipse as the *reader's* filter. Primary: psellos · eriugena · vārṣagaṇya · govinda-bhagavatpāda · utpaladeva · prajñākaragupta · vāgbhaṭa · atri.
- **Ch 30 — Where Does Ignorance Live?** (`hindu/darsana/`): the *āśraya* dispute stated from both sides. Primary: prakāśātman · vācaspati-miśra.
- **Ch 31 — The Body as a Rate** (`hindu/shastra/`): closes Ch 23's named gap; argues Āyurveda is an **equilibrium theory, not a vitalist one**. Primary: agni-āyurveda · dhātu · mala.
- **Ch 32 — What Survives Omniscience** (`jain/`): closes Ch 26 §6.4. Primary: aghāti-karma · īryāpathika-āsrava.
- **Ch 33 — The Asura Question** (`cross-tradition/`): one word across four traditions. Primary: varuṇa · vṛtra · verethragna · prahlāda · balarāma.

### Findings that reach beyond their own nodes
- **A §0 case handled as a case.** `atri` separates *what is well-founded* (RV 5.40 describes solar obscuration by Svarbhānu; he heads a long line of eclipse-thinking) from *what is not* (a datable observation; the world's earliest record; a date for the Ṛgveda) — and phrases the negative claim as **not established by what the corpus has seen**, not as false.
- **Confidence levels now mean two different things, deliberately.** `varsaganya` is `low` because of *the evidence that exists*; `prajnakaragupta` is `medium` because of *the reading that was done*. Ch 29 §7 makes the distinction explicit.
- **A source used for its terms and refused for its editorialising.** Caraka-Saṃhitā-Online glosses *jāṭharāgni* as "amylolytic, proteolytic and lipolytic enzymes." Quoted in `dhatu.md` and Ch 31 §7, **not adopted** — §4's "take the term, leave the editorialising," applied by name.
- **Independent corroboration, achieved.** Batches 40–41 recorded the Bhāmatī position only through IEP's Vivaraṇa-side vantage. Batch 42 reached it through the Bhāmatī literature and **everything came back unchanged**.
- **Two chapter-flagged holes closed**: Ch 23's (`vagbhata`/`dhatu`/`mala`) and Ch 26 §6.4's (the *aghāti* four and the kevalin's residual influx). Both old notes left standing, struck through or annotated, so the hole and its closure are both visible.

### Honesty-layer edges added (selection)
- `agni-ayurveda` ↔ `agni`: `shares-vocabulary-with` **+** `often-conflated-with-NOT-equivalent` — a §8 tradition-split so the deity's prestige does not underwrite the physiology.
- `vritra` ↔ `verethragna`: same pair of types — same root, **inverted referent**.
- `verethragna` ↔ `avatara-vedanta`: same pair — drawn specifically so the coincidence of *ten forms* cannot be read as descent.
- `eriugena` → `sunyata`: NOT-equivalent — the same negation doing opposite structural jobs.
- `balarama` → `gita`: NOT-equivalent — bondage in the **intention** vs in the **act**.
- `prahlada` → `shaivism`: NOT-equivalent — the same nine devotional forms, a different addressee.
- `prakasatman` → `prakriti-samkhya`: parallel **+** NOT-equivalent — *mūlāvidyā* in prakṛti's job-slot.
- `prajnakaragupta` → `kevala-jnana`: parallel **+** NOT-equivalent — omniscience as an epistemological result, but not a property of a permanent jīva.
- `varuna` → `karma-vedic`: NOT-equivalent — a personal moral order with confession vs an impersonal mechanism.

### Audits
- Three de-orphaning passes, all fixed per §10 with **content-motivated** inbound edges written from their own node's vantage (never mechanical mirrors): `nirjara→iryapathika-asrava`, `vacaspati-mishra→prakasatman`, `vijnaptimatrata→utpaladeva`, `charaka→vagbhata`, `krishna→balarama`, `henosis→eriugena`, `santaraksita→prajnakaragupta`, `prakriti-samkhya→varsaganya`, `svarbhanu→atri`, `bhakti→prahlada`.
- Final: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos.
- `find_duplicates.py`: exit 0. One new expected DEVANAGARI group (`अग्नि : agni, agni-ayurveda`) — a typed split, edge verified.
- Graph: **309 → 329 nodes, 1733 → 1910 edges**; `graph.svg` rendered via the explicit Graphviz `dot.exe` path (still not on PATH — same workaround as Batches 38–41).
- **Chapter-coverage re-derivation**: 329 / 329 covered; eight rows added to `chapters/INDEX.md` (gauḍapāda, padmapāda, vidyāraṇya, jina, tīrthaṅkara, tattvārtha-sūtra, samyagdarśana, sarvajñatva) — all *covered-in-prose, missing-a-row*, none needing a chapter.

### Open follow-ups (carried, not acted on)
1. **`ajiva.md` stores `part-of: jiva`**, inverting its own partition. A schema question (no *complement-of* relation exists), not a typo. *(carried from Batch 41)*
2. **`many-valued-logic` carries `tradition: Modern Physics`** — it is formal logic, and the mis-tag mis-colours the node. *(carried)*
3. **`atman-vedanta.md` and `brahman.md` queue a Vivekacūḍāmaṇi fetch *as Śaṅkara's***; must be re-scoped to *attributed*. *(carried)*
4. **Ch 11 predates the whole Advaita-lineage cluster** and should be re-read against Ch 25 §§3–6, Batch 41, and now Ch 30. *(carried)*
5. **The Digvijaya dating tension** (`shankara.md` dates "Mādhava's Śaṅkaradigvijaya" to the 17th c.; Vidyāraṇya died 1391). *(carried)*
6. **`karma-vargana.md` remains the Jain layer's one `low` node.** *(carried from Ch 26)*
7. **NEW — `dharmottara.md` and `dharmottara-nyayabindu.md` both exist.** Not flagged by `find_duplicates.py` (keys and IAST differ), but the person/text split should be checked for redundancy. *(opened by Ch 29)*
8. **NEW — the 42-vs-93 *nāma*-karma discrepancy** is unresolved and needs the *Karma-grantha* / *Gommaṭasāra Karmakāṇḍa* read directly. *(opened by `aghati-karma`)*
9. **NEW — Ch 23's §"A third authority, and a gap in the graph" and Ch 26 §6.4** both now describe closed holes and should be rewritten when those chapters are next revised.

### Corpus milestone: **329 concepts across 42 batches; 33 chapters.** 0 orphans. 0 unwritten stubs. Audit CLEAN. Chapter coverage 329/329.

### Suggested Batch 43 (names only — no files written)
- **Opened by Batch 42:** `somananda` (the *Śivadṛṣṭi*; Utpaladeva's teacher, and the man who did **not** coin *pratyabhijñā*); `abhinavagupta` (named across Chs 18/27/29 and still unwritten — the grand-disciple whose manuscripts carry Utpaladeva); `rasesvara` (the mercurial school, opened by `govinda-bhagavatpada`); `amalananda` and `appayya-dikshita` (the Bhāmatī continuation); `sarvajnatman` (the third holder of *pratibimbavāda*).
- **Opened by Chs 29/31:** `cakrapanidatta` (Caraka's commentator, to whom the three *dhātu-poṣaṇa-nyāya*s are credited on a single derivative source) and `dalhana` (Suśruta's commentator).
- **Opened by Ch 33:** `ahura-mazda` (the corpus's second Iranian node, and the one that would let the *asura/ahura* + *ṛta/aša* correspondence be drawn from the Iranian side); `hiranyakashipu`; `hemacandra` (the *Triṣaṣṭiśalākāpuruṣacaritra*, whose Johnson translation is the named upgrade path for Ch 33 §7).
- **Structural/maintenance pass:** follow-ups 1, 2, 3 and 7 above — all four are §10-mechanical or near-mechanical, and none has been touched in three batches.

---

## Batch 43 — COMPLETE (2026-08-27) — post-Śaṅkara continuations, the Āyurvedic commentators, the mercurial school, and two named upgrade paths

### Startup reconcile
- Working tree clean; git and `progress.md` agreed; audit CLEAN at 332 nodes / 1939 edges; `find_duplicates.py` exit 0.
- Resumed at row 4 of the 11-concept queue (rows 1–3 and the maintenance pass had been committed in the previous session).
- `graph.svg` still requires the explicit `dot.exe` path — Graphviz is not on PATH (same workaround as Batches 38–42).
- **`WebSearch` was available again** (the previous session hit its limit), which is why the remaining eight nodes are better sourced than the first three.

### Concepts — 11 / 11 done (0 blocked, 0 needs-opus-review). Rows 4–11 written this session.

| # | concept | status | conf | the finding |
|---|---|---|---|---|
| 4 | sarvajñātman | contested | medium | ***dvāra***. He holds every Vivaraṇa-side doctrine and still denies avidyā is the world's **material cause** — "Brahman in association and jointly with ajñāna cannot be regarded as the material cause." So the *āśraya* axis and the material-cause axis are **independent**, and "the Vivaraṇa view" flattens them. Also the corpus's cleanest §4-signal-5 case: the **critical edition's own blurb** carries the Kāñchī succession claim, so *provenance on the text ≠ provenance on the biography*. Date spread ~1,400 years. And a fourth source has him saluting **Deveśvara**, not Sureśvara, as guru — so Dasgupta's computed c. 900 rests on a premise the text does not supply. |
| 5 | amalānanda | converged | medium | The Bhāmatī stack is **five storeys and the tradition names the set**: "*Vedānta Śāstra* means 'the five texts…'" — in that usage the discipline **is** the stack. Storey 5 exists because storey 4 was unreadable. He also wrote on the **rival** school (*Pañcapādikā-darpaṇa*): fact recorded, "early link between the schools" inference **declined**. The corpus's **control case for lineage claims** — three formulations that reconcile once *dīkṣā*- and *vidyā*-guru are distinguished. Plus a checkable reference-work error (the *Pañcapādikā* given to Vācaspati; it is Padmapāda's). |
| 6 | appayya-dīkṣita | contested | medium | **The opponent who leaves no trace in the titles.** He named books after Madhva and wrote nothing explicitly against Rāmānuja — yet Duquette (OUP 2021) has the Śaiva oeuvre "mainly directed against Viśiṣṭādvaita." Compatible, and the point: polemical targets are **not readable off a bibliography**. Three readings of his own allegiance tabulated, not settled. The *Siddhāntaleśasaṃgraha* drawn as a 16th-c. doxography of one school's internal splits — structurally what a `contested` node is — parting from §4 at exactly one commitment: it declares the sub-schools to converge. Typed ∥ + NOT-equiv against `anekāntavāda`. |
| 7 | raseśvara | contested | medium | Its chapter opens with an **objection to the other six darśanas**, not with metallurgy: liberation is deferred past death, so "a man should preserve that body by means of mercury." The alchemy is the argument's **second premise**. Dating: Cowell & Gough (1882) put the school at the "commencement of the Christian era" and Wikipedia repeats it **with attribution** — one source and its echo — against three literatures dating the root texts to the **10th–12th c.** So "Raseśvara *darśana*" is treated as partly a 14th-century classificatory artefact. Sharpest new honesty edge: **siddha** — perfected by having **no** body (Jain) vs an **indestructible** one. Mercury handled in both directions per §0. |
| 8 | cakrapāṇidatta | converged | medium | Ch 31 §4.2's caveat answered by reading a peer-reviewed review **in full with its endnotes** — and the picture corrected three ways: the *nyāya*s are **four** not three (the fourth, *eka-kāla*, is **Aruṇadatta's**); they are credited to **three different** authorities; and the numbered enumeration is footnoted to a **2017 textbook**, i.e. modern pedagogy over classical images. **§0's failure mode running backwards.** Also the **best-dated person in the corpus** — a regnal anchor (Nayapāla, r. 1040–1070). |
| 9 | ḍalhaṇa | converged | medium | ***Rakta* is a fourth doṣa — for surgery.** Because *śalyatantra* is about *vraṇa* and blood is the main constituent in wound pathogenesis. So the doṣa-count is **discipline-relative**, which the corpus declines to flatten into inconsistency. He also admits ***mala* as a *śalya***, and his three-part *pariṇāma* (*sūkṣma*/*mala*/*sthūla-bhāga*) is the mechanism `dhatu.md` needed: it makes transformation **partial** and answers the fasting objection. Dated by **citation-bracketing**. |
| 10 | hiraṇyakaśipu | converged | medium | The verses put under Ch 33 §5.3's paraphrase (*Bhāgavata* 7.3.35–38, Tagare). **He never asks for immortality**, and he asks for Brahmā's own station in the same breath. And the clause that fails first is the **first**: everything is fenced against beings "created by You" — by Brahmā, who is Viṣṇu's creature. Viṣṇu is not in the domain at all, so the dusk and the threshold are a **surplus**. Flagged as the corpus's own reading. Logic edges bounded hard: ∥ + NOT-equiv `catuṣkoṭi`, NOT-equiv `many-valued-logic`. |
| 11 | hemacandra | converged | medium | **Two of the corpus's own upgrade paths run through one author.** `syādvāda` and `saptabhaṅgī` both name Malliṣeṇa's *Syādvādamañjarī* as their unfetched upgrade — and it is a commentary on Hemacandra's **32-verse** *Anyayogavyavacchedadvātriṃśikā*. That is now the **cheapest high-value primary text visible to this corpus**. Also ***Ardhacakrin***: Johnson's class-term for the Vāsudevas is "half-cakravartin," so Jainism ranks Kṛṣṇa **in the category name**, before any verdict about hell. Fibonacci claim handled in both directions per §0. |

### Chapter written — Ch 34 (and one fold)
- **Ch 34 — The Commentator** (`cross-tradition/`), over seven of the eight. Positioned explicitly against its neighbours: **Ch 25** asks *who* the commentators were, **Ch 29** how texts survive, **Ch 34** what a commentary is as a *form* — and it is the first of the three to work **across traditions**, which is what makes §5's comparison possible.
- Two things it argues rather than reports: **(a)** how well a pre-modern Indian figure can be dated is mostly a fact about *what institution they stood next to* — court vs maṭha — not how much was written about them; **(b)** a scholar's real opponents are not readable off his tables of contents.
- Its **source ceiling is stated at the top and repeated where it bites**: *not one commentary was read.* That is why all seven nodes are `medium`.
- **`hiraṇyakaśipu` folded into Ch 33 §§5.3.1–5.3.2** rather than given a chapter.
- `chapters/INDEX.md`: Ch 34 row, Ch 33 row updated, **eight** concept rows. **Coverage 340 / 340.**

### Findings that reach beyond their own nodes
- **A dating-method triptych, assembled by accident.** Regnal anchor (Cakrapāṇi, 30-year window) · citation-bracketing (Ḍalhaṇa, 150-year bracket, needs nothing but texts) · lineage arithmetic (Sarvajñātman, and it broke). Ch 34 §5.
- **The doxographic turn**, in four genres deliberately **not** merged: compilation (Ḍalhaṇa) · refutation-doxography (Hemacandra) · ordering (Mādhava) · reconciling (Appayya). Offered as a pattern noticed, **not a thesis argued** — four cases across four centuries is a suggestion.
- **§0's failure mode has a mirror image.** `cakrapanidatta` found a *modern organising scheme mistaken for an old one* (the four-fold *nyāya* list, footnoted to 2017). Same mechanism, opposite direction, equally invisible from summaries.
- **Two sources used for their terms and refused for their editorialising**: the IJAM Ḍalhaṇa paper's western-surgical correlations, and Wikipedia's framing of mercury toxicology as refuting the Raseśvaras. §0 applies in the debunking direction too.
- **A carried follow-up advanced, not closed.** `govinda-bhagavatpada`'s Raseśvara attribution is now blocked from **both** ends by dating (1st c. too early for an 8th-c. guru; 10th–12th c. too late). Two men, one name.
- **A dispute opened rather than papered over.** `dhatu.md`'s "incompatible by design" reading now carries a flagged challenge from the Āyurvedic academic press ("a cohesive group… they do not conflict"). Neither retired, neither adopted, and the question neither source asks is named.

### Audits
- Final: **CLEAN** — 0 stubs, 0 orphans, 0 bidirectional-directional, 0 forbidden combos. `find_duplicates.py` exit 0 throughout.
- De-orphaning passes, all §10-mechanical, all with **content-motivated** inbound edges written from the inbound node's own vantage: `prakasatman→sarvajnatman` (both sanctioned types), `vacaspati-mishra→amalananda`, `amalananda→appayya-dikshita`, `jivanmukti→rasesvara`, `govinda-bhagavatpada→rasesvara`, `cakrapanidatta→dalhana`, `narasimha→hiranyakashipu`, `prahlada→hiranyakashipu`, `balarama→hemacandra`, `syadvada→hemacandra`, `anekantavada→hemacandra`.
- Graph: **332 → 340 nodes, 1939 → 2022 edges.** `graph.svg` rendered via the explicit Graphviz path.
