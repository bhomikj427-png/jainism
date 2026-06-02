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
| 2 | `samvara.md` | done | converged, LOW confidence; TS 9.1 text not fetched; definition from aggregation |
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
| 1 | `prakriti-samkhya.md` | pending | Sāṃkhya primal matter — forward-link stub from pudgala |
| 2 | `purusha-samkhya.md` | pending | Sāṃkhya consciousness — compare with jīva |
| 3 | `nirvana-buddhist.md` | pending | Buddhist liberation — compare with Jain mokṣa |
| 4 | `pratityasamutpada.md` | pending | Buddhist dependent origination — compare with karma/bandha |
| 5 | `brahman.md` | pending | Advaita absolute — connects to ātman-vedānta |
| 6 | `tattva-jain.md` | pending | the seven fundamental categories (Jain) |
| 7 | `loka-jain.md` | pending | Jain cosmology — lokāgra, siddha location |
| 8 | `bandha.md` | pending | karmic bondage (deeper treatment beyond karma.md) |

## Batch 5 concepts

| # | concept (filename) | status | notes |
|---|---|---|---|
| 1 | `democritus-atom.md` | pending | Greek atomism — cross-tradition parallel to paramāṇu |
| 2 | `anatta-buddhist.md` | pending | Buddhist no-self — deeper treatment, contrast with jīva |
| 3 | `sunyata.md` | pending | Buddhist emptiness — contrast with Jain realism |
| 4 | `maya-advaita.md` | pending | Advaita illusion doctrine — contrast with Jain ontological realism |
| 5 | `ahimsa.md` | pending | non-violence — ethical link to anekāntavāda and jīva |
| 6 | `guna-samkhya.md` | pending | Sāṃkhya three qualities (tamas/rajas/sattva) — compare with pudgala qualities |
| 7 | `many-valued-logic.md` | pending | fills saptabhaṅgī NOT-equiv stub |

## Run logs — Batches 3–5
*(appended at end-of-batch per §9)*
