# progress.md — Batch 1 & 2 Work Queue

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
| 3 | `saptabhangi.md` | pending | forward-link stub exists; sevenfold predication |
| 4 | `karma.md` | pending | karmic matter as fine skandha; bridges physics/soteriology |
| 5 | `moksha.md` | pending | liberation; completes jīva arc |
| 6 | `paramanu-vaisheshika.md` | pending | forward-link stub exists; Vaiśeṣika side |
| 7 | `skandha-buddhist.md` | pending | forward-link stub exists; Buddhist khandhas |

## Run log — Batch 2
*(appended at end-of-batch per §9)*
