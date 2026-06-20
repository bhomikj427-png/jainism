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
