# progress.md — Batches 1–5 Work Queue

## Anchor text
**Tattvārtha Sūtra** (Umāsvāti / Umāsvāmī) — to be confirmed by fetch before writing concepts.
Target edition: Nathmal Tatia (tr.), *That Which Is: Tattvārthasūtra*, HarperCollins/Sacred Literature Trust, 1994.
Secondary: Hermann Jacobi translations in Sacred Books of the East; Pandit Sukhlalji commentary.

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
| 2 | `shruta-jnana.md` | pending | |
| 3 | `anicca.md` | pending | |
| 4 | `paroksha-jnana.md` | pending | |
| 5 | `avatara-vedanta.md` | pending | |
| 6 | `acarya.md` | pending | |
| 7 | `mimamsa-pramana.md` | pending | |

## Run log — Batch 10
*(appended at end-of-batch per §9)*
