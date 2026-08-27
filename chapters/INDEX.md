# chapters/INDEX.md — the chapter list + roadmap (loaded at startup; keep it small)
# The concept -> chapter LOOKUP TABLE lives in chapters/coverage.md -- grep it, never load it whole.
# Each concept is primary-covered in exactly one chapter; verify with graph/check_chapters.py.
# Chapters are grouped by origin into subfolders: jain/ (Jain-tradition chapters), cross-tradition/
# (comparative chapters spanning multiple traditions), comparanda/ (non-Indian / formal-logic /
# Greek-Neoplatonic parallels), buddhist/ (Buddhist-tradition chapters), and hindu/ (Hindu chapters).
# hindu/ has a SECOND level because "Hindu" spans genuinely different domains and would not scale flat:
#   hindu/darsana/    — the philosophical systems (āstika darśanas: Vedānta, Sāṃkhya, Yoga, Nyāya, Vaiśeṣika, Mīmāṃsā)
#   hindu/devotional/ — deities, vāhanas, iconography, bhakti, the Śaiva/Vaiṣṇava/Śākta families
#   hindu/scripture/  — epics and canonical texts (Vedas, Upaniṣads, Mahābhārata, Rāmāyaṇa, Gītā, root sūtras)
#   hindu/shastra/    — technical/scientific śāstra (Āyurveda; and any future jyotiṣa, Arthaśāstra, Nāṭyaśāstra)

> **📖 THIRD TRACK — Translation Reading-Room** (separate from chapters below): word-by-word sourced translations
> of Jain texts (Tattvārtha Sūtra, Bhaktāmar Stotra, …) live under `chapters/jain/translations/`. Its own driver +
> work queue is **[chapters/jain/translations/INDEX.md](jain/translations/INDEX.md)**. If the user says
> **"build the next translation" / "build the next thing"**, go there and take the lowest-numbered `pending` unit.
> This is NOT a chapter and NOT a batch — it's a primary-source reading room with a strict no-original-translation firewall.

| chapter | file | primary concepts | status |
|---|---|---|---|
| 01 Jain Ontology | [jain/01-jain-ontology.md](jain/01-jain-ontology.md) | sat · dravya · paryāya · pudgala · paramāṇu · skandha | drafted |
| 02 Jain Epistemology | [jain/02-jain-epistemology.md](jain/02-jain-epistemology.md) | naya · anekāntavāda · syādvāda · saptabhaṅgī · dravyārthika-naya · paryāyārthika-naya | drafted |
| 03 Jain Soteriology | [jain/03-jain-soteriology.md](jain/03-jain-soteriology.md) | tattva-jain · jīva · karma · kaṣāya · āsrava · bandha · saṃvara · nirjarā · mokṣa · guṇasthāna · loka-jain | drafted |
| 04 Cross-Tradition | [cross-tradition/04-cross-tradition.md](cross-tradition/04-cross-tradition.md) | brahman · ātman-vedānta · karma-vedic · mokṣa-advaita · pratītyasamutpāda · nirvāṇa-buddhist · ahiṃsā · ahiṃsā-buddhist | drafted |
| 05 Cross-Tradition Epistemology | [cross-tradition/05-cross-tradition-epistemology.md](cross-tradition/05-cross-tradition-epistemology.md) | pramāṇa · pramāṇa-nyāya · dignāga-pramāṇa · mīmāṃsā-pramāṇa · anumāna-nyāya · vyāpti · hetvābhāsa · tarka · jāti · apoha · śabda-pramāṇa · arthāpatti · hetu-vidyā · dharmottara | drafted |
| 06 Formal-Logic Comparanda | [comparanda/06-formal-logic-comparanda.md](comparanda/06-formal-logic-comparanda.md) | catuṣkoṭi · many-valued-logic · paraconsistent-logic · fuzzy-logic | drafted |
| 07 Jain Knowledge: The Five Jñānas | [jain/07-jain-knowledge.md](jain/07-jain-knowledge.md) | ratnatraya · upayoga · nikṣepa · mati-jñāna · śruta-jñāna · parokṣa-jñāna · avadhi-jñāna · manaḥparyāya-jñāna · kevala-jñāna | drafted |
| 08 Jain Ethics & Ascetic Practice | [jain/08-jain-ethics.md](jain/08-jain-ethics.md) | cāritra · satya · asteya · brahmacarya · aparigraha · aṇuvrata · tapas · dhyāna-jain · ṣaḍāvaśyaka · sallekhanā | drafted |
| 09 The Jain Cosmos & Six Substances | [jain/09-jain-cosmos.md](jain/09-jain-cosmos.md) | dravya · sat · astikāya · jīva · pudgala · dharma-dravya · adharma-dravya · ākāśa · kāla · loka · utsarpiṇī-avasarpiṇī | drafted |
| 10 Holy Beings, Sects, Texts & History | [jain/10-jain-holy-beings.md](jain/10-jain-holy-beings.md) | ṇamokāra-mantra · ācārya · upādhyāya · sādhu · pārśvanātha · mahāvīra · digambara · śvetāmbara · kundakunda · samayasāra · niścaya-vyavāhara · puṇya · pāpa · karma-prakṛti · ājīvika | drafted |
| 11 The Vedānta Family | [hindu/darsana/11-vedanta.md](hindu/darsana/11-vedanta.md) | prasthānatrayī · brahman · ātman-vedānta · māyā-advaita · mokṣa-advaita · advaita-vedanta · vivartavāda · pariṇāmavāda · vishishtadvaita · dvaita-vedanta · bhakti · jñāna-mārga · karma-mārga · trimurti · avatāra-vedānta · sarasvatī · lakṣmī | drafted |
| 12 The Buddhist Family | [buddhist/12-buddhist.md](buddhist/12-buddhist.md) | four-noble-truths · dukkha · tanha · paticcasamuppada-pali · nibbana-theravada · anatta-buddhist · anicca · theravada · arhat · skandha-buddhist · abhidharma · śūnyatā · bodhicitta · bodhisattva · madhyamaka · dvisatya · catuṣkoṭi · yogacara · vijñaptimātratā · ālaya-vijñāna · tathāgatagarbha | drafted |
| 13 Neoplatonism | [comparanda/13-neoplatonism.md](comparanda/13-neoplatonism.md) | neoplatonism · plotinus · plotinus-one · nous · henosis · porphyry · proclus | drafted |
| 14 Greek & Hellenistic Foundation | [comparanda/14-greek-foundation.md](comparanda/14-greek-foundation.md) | parmenides-being · democritus-atom · plato-forms · plato-soul · aristotle-substance · aristotle-categories · aristotle-logic · aristotle-ethics · four-causes · epicurus-atom · epicurus-ethics · stoicism · stoic-logos · cynicism · pyrrhonism · academic-skepticism | drafted |
| 15 Sāṃkhya & Yoga | [hindu/darsana/15-samkhya-yoga.md](hindu/darsana/15-samkhya-yoga.md) | kapila · samkhya-karika · prakriti-samkhya · purusha-samkhya · guna-samkhya · satkaryavada · patanjali · yoga-darshana · citta-vritti · citta · manas | drafted |
| 16 Nyāya & Vaiśeṣika | [hindu/darsana/16-nyaya-vaisheshika.md](hindu/darsana/16-nyaya-vaisheshika.md) | gautama-aksapada · kanada · nyaya-sutra · vaiseshika-sutra · dravya-vaisheshika · paramanu-vaisheshika · pancha-mahabhuta · asatkaryavada · prashastapada | drafted |
| 17 Mīmāṃsā & Cārvāka | [hindu/darsana/17-mimamsa-carvaka.md](hindu/darsana/17-mimamsa-carvaka.md) | jaimini · mimamsa-sutra · kumarila-bhatta · prabhakara · carvaka | drafted |
| 18 The Deity World | [hindu/devotional/18-hindu-deities.md](hindu/devotional/18-hindu-deities.md) | trimurti · brahma · vishnu · shiva · shakti · vaishnavism · shaivism · krishna · rama · lingam · nataraja · kala-bhairava · spanda · pratyabhijna · durga · kali · parvati · ganesha · kartikeya · hanuman · nandi · garuda · surya · agni · indra · aruna · kamadhenu | drafted |
| 19 The Texts: Śruti, Smṛti & the Authors | [hindu/scripture/19-hindu-scripture.md](hindu/scripture/19-hindu-scripture.md) | upanishad · rta · yajna · brahma-sutra · badarayana · mahabharata · ramayana · gita · samatva · sthitaprajna · jivanmukti · vishnu-sahasranama · vyasa · valmiki · dana · samsara | drafted |
| 20 Buddhist Scholastics | [buddhist/20-buddhist-scholastics.md](buddhist/20-buddhist-scholastics.md) | nagarjuna · mulamadhyamakakarika · prasanga-nagarjuna · santideva · vasubandhu · abhidharmakosa · asanga · trisvabhava · pramana-samuccaya · dharmakirti · pramanavarttika · santaraksita · kamalasila · nirvana-mahayana | drafted |
| 21 The Churning of the Ocean | [hindu/devotional/21-churning-and-avataras.md](hindu/devotional/21-churning-and-avataras.md) | samudra-manthana · amrita · halahala · kurma · vasuki · dhanvantari · mohini · rahu · ketu · svarbhanu · airavata · ucchaihshravas · kaustubha · varuni · parijata · kalpavriksha · shesha · kadru · vinata · jatayu · sampati · matsya · varaha · narasimha · vamana · bali · parashurama · kalki | drafted |
| 22 Four and Four: Equanimity & Compassion | [cross-tradition/22-ethics-equanimity.md](cross-tradition/22-ethics-equanimity.md) | metta · karuna · mudita · upekkha · maitri-jain · pramoda · karunya · madhyasthya · ahimsa-vedic | drafted |
| 23 Āyurveda | [hindu/shastra/23-ayurveda.md](hindu/shastra/23-ayurveda.md) | ayurveda · charaka · sushruta · tridosha | drafted |
| 24 After Plotinus: Theurgy, the Henads & the End of the Academy | [comparanda/24-later-neoplatonists.md](comparanda/24-later-neoplatonists.md) | ammonius-saccas · iamblichus · theurgy · chaldean-oracles · syrianus · proclus-henad · marinus · damascius · simplicius · psyche-neoplatonic · liber-de-causis · pseudo-dionysius | drafted |
| 25 Who Wrote the Systems: Commentators, Rivals & Six Ways an Author Dissolves | [hindu/darsana/25-commentators-and-authors.md](hindu/darsana/25-commentators-and-authors.md) | vatsyayana · shankara · mandana-mishra · sureshvara · vyasa-yogabhasya · vindhyavasin | drafted |
| 26 The Machinery of Bondage: What Karma Is Made Of | [jain/26-karma-machinery.md](jain/26-karma-machinery.md) | ajīva · kārmaṇa-vargaṇā · leśyā · mohanīya | drafted |
| 27 Process All the Way Down: the Person, the Percept & Two Adversaries | [buddhist/27-process-and-adversaries.md](buddhist/27-process-and-adversaries.md) | nāmarūpa · pratyakṣa-buddhist · nyāyabindu (Dharmottaraṭīkā) · makkhali-gosāla | drafted |
| 28 The Atom That Isn't and the Duality That Isn't: Modern Physics as Comparandum | [comparanda/28-modern-physics.md](comparanda/28-modern-physics.md) | modern-atom · quantum-complementarity | drafted |
| 29 How Things Reach Us | [cross-tradition/29-transmission.md](cross-tradition/29-transmission.md) | psellos · eriugena · vārṣagaṇya · govinda-bhagavatpāda · utpaladeva · prajñākaragupta · vāgbhaṭa · atri | drafted |
| 30 Where Does Ignorance Live? | [hindu/darsana/30-locus-of-ignorance.md](hindu/darsana/30-locus-of-ignorance.md) | prakāśātman · vācaspati-miśra | drafted |
| 31 The Body as a Rate | [hindu/shastra/31-the-ayurvedic-body.md](hindu/shastra/31-the-ayurvedic-body.md) | agni-āyurveda · dhātu · mala | drafted |
| 32 What Survives Omniscience | [jain/32-what-survives-omniscience.md](jain/32-what-survives-omniscience.md) | aghāti-karma · īryāpathika-āsrava | drafted |
| 33 The Asura Question | [cross-tradition/33-the-asura-question.md](cross-tradition/33-the-asura-question.md) | varuṇa · vṛtra · verethragna · prahlāda · balarāma · hiraṇyakaśipu (§5.3.1–2) · ahura-mazdā (§4.1) | drafted |
| 34 The Commentator | [cross-tradition/34-the-commentator.md](cross-tradition/34-the-commentator.md) | sarvajñātman · amalānanda · appayya-dīkṣita · cakrapāṇidatta · ḍalhaṇa · hemacandra · raseśvara | drafted |

---

## Chapter roadmap (planned — NAMES ONLY, not yet written)

> **For a fresh session: this is the to-do list for the teaching layer.** Pick the **lowest-numbered `planned` row** unless the user names a specific one. All the listed concepts are **already written as graph nodes** in `concepts/` — a chapter is a prose reading-view over them, so authoring one writes **no new nodes** and has **no graph impact** (`build_graph.py` ignores `chapters/`). Target sub-folder is given per row; `hindu/` rows use its second level (`darsana/`/`devotional/`/`scripture/`). This roadmap supersedes the per-chapter `*Next:*` footers and the "Suggested next chapter" line in `progress.md` if they ever disagree. ⚠️ Do **not** confuse this with `progress.md`'s "Suggested Batch NN" — that queues **concept nodes**, a different track (see `chapter-vs-batch` memory).

| # | planned chapter | sub-folder | primary concepts (already written as nodes) | status |
|---|---|---|---|---|
| ~~18~~ | ~~Hindu Deities: Trimūrti & the Devotional Families~~ | `hindu/devotional/` | — | **drafted** (see table above) |
| ~~19~~ | ~~Hindu Epics & Scripture~~ | `hindu/scripture/` | — | **drafted** (see table above; picked up badarayana · samatva · sthitaprajna · jivanmukti beyond the planned list) |
| ~~20~~ | ~~Buddhist Scholastics: Madhyamaka, Yogācāra & the Logicians~~ | `buddhist/` | — | **drafted** (see table above; `dharmottara` stays primary in Ch 05 and is cross-referenced only) |
| ~~21~~ | ~~The Churning of the Ocean: the Samudra-manthana Cycle & the Daśāvatāra~~ | `hindu/devotional/` | — | **drafted** (see table above) |
| ~~22~~ | ~~Equanimity & Compassion: the Cross-Tradition Ethics Cluster~~ | `cross-tradition/` | — | **drafted** (see table above; also picked up `ahimsa-vedic`, which had no chapter home) |
| ~~23~~ | ~~Āyurveda: the Medical Tradition~~ | `hindu/shastra/` **(new sub-folder)** | — | **drafted** (see table above; `dhanvantari` stays primary in Ch 21. `vagbhata` and `dhatu`/`mala` are still **unwritten nodes** — the third classical authority is a hole in the chapter) |
| ~~24~~ | ~~The Later Neoplatonists: Theurgy, the Henads & the Christian Transmission~~ | `comparanda/` | — | **drafted** (see table above; retitled *After Plotinus: Theurgy, the Henads & the End of the Academy*. `psellos` — the separate Byzantine transmission line for the Chaldean Oracle fragments — is still an **unwritten node** and is flagged in the chapter's footer) |

| ~~25~~ | ~~Who Wrote the Systems: the commentators and the identity problems~~ | `hindu/darsana/` | — | **drafted** (see table above; re-derived 2026-08-25 from the `concepts/`-vs-index diff — six nodes that had no chapter home, three of them written after Ch 11 was drafted) |
| ~~26~~ | ~~The Jain Remainder~~ | `jain/` | — | **drafted** (see table above; retitled *The Machinery of Bondage: What Karma Is Made Of* — the four leftovers turned out to be one mechanism. `karma-vargana` remains the corpus's `low`-confidence node and the chapter says so in §4) |
| ~~27~~ | ~~Buddhist Singletons~~ | `buddhist/` | — | **drafted** (see table above; retitled *Process All the Way Down*. The placement question was resolved **in favour of `buddhist/`** and made explicit in the chapter header: Gosāla is Ājīvika but survives **only** in Buddhist and Jain polemic, and §§7–8 make that the point) |
| ~~28~~ | ~~The Modern-Physics Comparanda~~ | `comparanda/` | — | **drafted** (see table above. Written as the corpus's consolidated §0 statement: two worked cases, the five-move anatomy of the slide, the **full inventory** of every modern-science NOT-equivalent edge in `concepts/`, four portable tests, and the mirror error — deflation — from Ch 23) |

> **✅ ROADMAP COMPLETE — the teaching layer now covers the whole 306-node graph (re-derived 2026-08-26, after Ch 28).**
> The final diff of `concepts/*.md` against this file, using diacritic-aware search of chapter prose, returned **two** apparent gaps — `naigama-naya` and `saṃgraha-naya` — and both proved to be **already covered in Ch 02 §4** under their bare display names rather than their file keys. Rows for those two (and `vyavahāra-naya`) have been added to the concept→chapter index below; **no chapter was needed.**
> **→ The next unit of work is therefore a concept batch in `progress.md`, not a chapter.** New nodes first; a chapter over them afterwards. `progress.md`'s "Suggested Batch 41" is the queue. When new concepts are written, re-derive this roadmap again by the method below.

> **🔁 How to re-derive this roadmap (method, first used 2026-08-25 after Ch 24 exhausted the previous one).** Diff `concepts/*.md` against the "Full concept → chapter index" below — but **do not diff on the key alone**: the index lists concepts by IAST display name (`ahiṃsā-vedic` for `ahimsa-vedic`), so a naive comparison reports false gaps. The reliable test is a **diacritic-aware search of chapter prose** for the term. Rows 25–28 above came from that test. When these are drafted, re-derive again; if the diff comes back empty, the teaching layer is complete for the current graph and the next unit of work is a **concept batch** (`progress.md`), not a chapter — new nodes first, then a chapter over them.

*Rows 22–24 were re-derived from `concepts/` against this table when the original Ch 15–21 roadmap was exhausted (2026-08-24), per the standing instruction in this section. They were the last three clusters of written nodes with no chapter home; **all three are now drafted (2026-08-25), so the roadmap is again exhausted** — see the notice above the table. Re-derive from `concepts/` vs. this table whenever that happens.*

---

## Full concept → chapter index

➡ Moved to **[chapters/coverage.md](coverage.md)** — 342 rows, a lookup table, deliberately NOT loaded at startup. **Grep it**, don't open it whole:
`grep -n '^| <concept-key>' chapters/coverage.md`. Coverage is verified by `python graph/check_chapters.py`, never by hand.
