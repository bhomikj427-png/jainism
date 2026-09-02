# chapters/coverage.md — the concept → chapter lookup table
#
# Split out of chapters/INDEX.md so it is NOT loaded at startup (CLAUDE.md §7): this is a
# LOOKUP table — grep it when you need "which chapter covers X", the same way MANIFEST.tsv
# is grepped instead of loading index.md. INDEX.md keeps the chapter list and the roadmap.
#
# Each concept is primary-covered in exactly one chapter.
# Verified by `python graph/check_chapters.py` — never re-derive coverage by hand.

## Full concept → chapter index

| concept | primary chapter | cross-referenced in |
|---|---|---|
| paryāya | Ch 01 | Ch 02 (paryāyārthika nayas) |
| pudgala | Ch 01 | — |
| paramāṇu | Ch 01 | — |
| skandha | Ch 01 | — |
| naya | Ch 02 | — |
| anekāntavāda | Ch 02 | Ch 03 (§2 jīva conflation note) · Ch 06 (§5.3 fuzzy-logic NOT-equiv) |
| syādvāda | Ch 02 | — |
| saptabhaṅgī | Ch 02 | Ch 06 (§2.1, §5.1–5.2 logic NOT-equiv) |
| dravyārthika-naya | Ch 02 | — |
| paryāyārthika-naya | Ch 02 | — |
| tattva-jain | Ch 03 | — |
| jīva | Ch 03 | Ch 01 (as one of six dravyas) |
| karma | Ch 03 | — |
| kaṣāya | Ch 03 | — |
| āsrava | Ch 03 | — |
| bandha | Ch 03 | — |
| saṃvara | Ch 03 | — |
| nirjarā | Ch 03 | — |
| mokṣa | Ch 03 | — |
| guṇasthāna | Ch 03 | — |
| brahman | Ch 04 | — |
| ātman-vedānta | Ch 04 | Ch 03 (§2 jīva conflation) |
| karma-vedic | Ch 04 | Ch 03 (§3 karma conflation) |
| mokṣa-advaita | Ch 04 | Ch 03 (§10 liberation table) |
| pratītyasamutpāda | Ch 04 | — |
| nirvāṇa-buddhist | Ch 04 | Ch 03 (§10 liberation table) |
| ahiṃsā-buddhist | Ch 04 | — |
| pramāṇa-nyāya | Ch 05 | — |
| dignāga-pramāṇa | Ch 05 | — |
| mīmāṃsā-pramāṇa | Ch 05 | — |
| anumāna-nyāya | Ch 05 | — |
| vyāpti | Ch 05 | — |
| hetvābhāsa | Ch 05 | — |
| tarka | Ch 05 | — |
| jāti | Ch 05 | — |
| apoha | Ch 05 | — |
| śabda-pramāṇa | Ch 05 | — |
| arthāpatti | Ch 05 | — |
| hetu-vidyā | Ch 05 | — |
| dharmottara | Ch 05 | — |
| catuṣkoṭi | Ch 06 | — |
| many-valued-logic | Ch 06 | — |
| paraconsistent-logic | Ch 06 | — |
| fuzzy-logic | Ch 06 | — |
| ratnatraya | Ch 07 | Ch 03 (right faith/conduct jewels) |
| upayoga | Ch 07 | Ch 03 (§2.1 jīva's mark) |
| nikṣepa | Ch 07 | Ch 02 (naya disambiguation) |
| mati-jñāna | Ch 07 | — |
| śruta-jñāna | Ch 07 | — |
| parokṣa-jñāna | Ch 07 | Ch 05 (pratyakṣa/parokṣa inversion vs Nyāya/Buddhist/Mīmāṃsā) |
| avadhi-jñāna | Ch 07 | — |
| manaḥparyāya-jñāna | Ch 07 | — |
| kevala-jñāna | Ch 07 | Ch 03 (§9 guṇasthāna 13 · §10 mokṣa) |
| pramāṇa | Ch 05 | Ch 02 (naya/pramāṇa pair) · Ch 07 (§2.2 the complete-cognition instrument) |
| cāritra | Ch 08 | Ch 01 · Ch 07 (§1 third jewel of the ratnatraya) |
| satya | Ch 08 | Ch 04 (ahiṃsā-rooted vow cluster) |
| asteya | Ch 08 | Ch 04 (ahiṃsā-rooted vow cluster) |
| brahmacarya | Ch 08 | Ch 04 (ahiṃsā-rooted vow cluster) |
| aparigraha | Ch 08 | Ch 03 (§ kaṣāya-root of bandha) |
| aṇuvrata | Ch 08 | — |
| tapas | Ch 08 | Ch 03 (nirjarā mechanism) |
| dhyāna-jain | Ch 08 | Ch 03 (§ karma-binding vs karma-shedding meditation) |
| ṣaḍāvaśyaka | Ch 08 | — (sāmāyika · pratikramaṇa covered as members) |
| sallekhanā | Ch 08 | — (contested; presented as divergence table) |
| ahiṃsā | Ch 04 | Ch 08 (§2 root of the five vows) |
| astikāya | Ch 09 | Ch 01 (the extended substances) |
| dharma-dravya | Ch 09 | Ch 01 (one of six dravyas) |
| adharma-dravya | Ch 09 | Ch 01 (one of six dravyas) |
| ākāśa | Ch 09 | Ch 01 (one of six dravyas) |
| kāla | Ch 09 | Ch 01 (one of six dravyas) |
| loka | Ch 09 | Ch 03 (§ siddha-śilā summit / mokṣa address) |
| utsarpiṇī-avasarpiṇī | Ch 09 | — (Tīrthaṅkara distribution across the cycle) |
| dravya | Ch 01 | Ch 02 (naya operates on dravya) · Ch 09 (§1 the six substances in full) |
| sat | Ch 01 | Ch 02 (anekāntavāda grounding) · Ch 09 (§2 being as change-in-permanence) |
| ṇamokāra-mantra | Ch 10 | — (five-line pañca-parameṣṭhī salutation) |
| arihant | Ch 07 | Ch 10 (§1 first parameṣṭhī · §5 four ghāti destroyed) |
| siddha | Ch 03 | Ch 10 (§1 second parameṣṭhī · §5 all eight karmas gone) |
| ācārya | Ch 10 | — (third parameṣṭhī; order-head) |
| upādhyāya | Ch 10 | — (fourth parameṣṭhī; āgama-teacher) |
| sādhu | Ch 10 | — (fifth/broadest parameṣṭhī; mahāvrata-keeper) |
| pārśvanātha | Ch 10 | Ch 09 (23rd tīrthaṅkara in the kālacakra list) |
| mahāvīra | Ch 10 | Ch 09 (24th tīrthaṅkara; reformer not founder) |
| digambara | Ch 10 | Ch 08 (sky-clad reading of aparigraha) |
| śvetāmbara | Ch 10 | — (white-clad sect; Āgama canon) |
| kundakunda | Ch 10 | — (foundational Digambara philosopher-monk) |
| samayasāra | Ch 10 | — (Kundakunda's chief text; pure-soul) |
| niścaya-vyavāhara | Ch 10 | Ch 02 (two nayas; grounds in anekāntavāda) |
| puṇya | Ch 10 | Ch 03 (subtype of āsrava/bandha) |
| pāpa | Ch 10 | Ch 03 (subtype of āsrava/bandha) · Ch 08 (mahāvrata violations) |
| karma-prakṛti | Ch 10 | Ch 03 (the eight karma-types behind bandha) · Ch 07 (ghāti/aghāti behind arihant) |
| ājīvika | Ch 10 | — (Gosāla's fatalist śramaṇa rival; niyati vs effort) |
| prasthānatrayī | Ch 11 | — (triple canonical foundation of Vedānta) |
| advaita-vedanta | Ch 11 | Ch 04 (brahman/ātman) |
| maya-advaita | Ch 11 | — |
| vivartavāda | Ch 11 | Ch 04 (māyā-advaita distinction) |
| pariṇāmavāda | Ch 11 | — (real transformation; Viśiṣṭādvaita/Śaiva) |
| vishishtadvaita | Ch 11 | — (Rāmānuja qualified non-dualism) |
| dvaita-vedanta | Ch 11 | — (Madhva eternal dualism) |
| bhakti | Ch 11 | Ch 04 (devotion as mokṣa path) |
| jñāna-mārga | Ch 11 | Ch 04 (knowledge path) |
| karma-mārga | Ch 11 | Ch 04 (action path; nishkama karma) |
| sarasvatī | Ch 11 | — (knowledge goddess; Tridevi Sattva) |
| lakṣmī | Ch 11 | — (prosperity goddess; Tridevi Rajas; Viṣṇu śakti) |
| four-noble-truths | Ch 12 | Ch 04 (Buddhist foundation) |
| dukkha | Ch 12 | — |
| tanha | Ch 12 | — (craving; 2nd Noble Truth; 8th nidāna) |
| paticcasamuppada-pali | Ch 12 | Ch 04 (Pali dependent-origination treatment) |
| nibbana-theravada | Ch 12 | Ch 04 (Theravāda liberation account) |
| anatta-buddhist | Ch 12 | Ch 03 (vs Jain jīva) · Ch 04 (§1 Buddhist basics) |
| anicca | Ch 12 | Ch 04 (impermanence; tilakkhaṇa) |
| theravada | Ch 12 | — (oldest surviving school; Pali Tipiṭaka) |
| arhat | Ch 12 | Ch 04 (Theravāda liberation goal) |
| skandha-buddhist | Ch 12 | Ch 01 (vs Jain skandha) |
| abhidharma | Ch 12 | — (82-dharma analysis; Abhidharmakośa) |
| sunyata | Ch 12 | — |
| bodhicitta | Ch 12 | — (awakening mind; Mahāyāna vow) |
| bodhisattva | Ch 12 | — |
| madhyamaka | Ch 12 | Ch 06 (catuṣkoṭi grounding) |
| dvisatya | Ch 12 | — (Madhyamaka two truths; saṃvṛti/paramārtha) |
| yogacara | Ch 12 | — |
| vijñaptimātratā | Ch 12 | — (Yogācāra consciousness-only) |
| ālaya-vijñāna | Ch 12 | — (storehouse consciousness; rebirth-without-self) |
| tathāgatagarbha | Ch 12 | — (Buddha-nature; NOT-equiv ātman) |
| neoplatonism | Ch 13 | — (the school; emanation-return; ∥ Advaita) |
| plotinus | Ch 13 | Ch 11 (the One ∥ brahman; NOT-equiv) |
| plotinus-one | Ch 13 | Ch 11 (One above thought) · Ch 12 (One NOT-equiv śūnyatā/nirvāṇa) |
| nous | Ch 13 | Ch 11 (Brahman-as-cit maps to Nous, the 2nd hypostasis) |
| henosis | Ch 13 | Ch 11 (henōsis ∥ mokṣa-advaita; NOT-equivalent) |
| porphyry | Ch 13 | — (editor of the Enneads; Isagoge / problem of universals) |
| proclus | Ch 13 | — (Elements of Theology; monē-proodos-epistrophē; henads) |
| parmenides-being | Ch 14 | — (to eon; Way of Truth vs Way of Opinion) |
| democritus-atom | Ch 14 | — (atoms + void; qualitative neutrality vs Jain/Vaiśeṣika paramāṇu) |
| plato-forms | Ch 14 | Ch 13 (Forms as contents of Nous) |
| plato-soul | Ch 14 | — (tripartite soul; Phaedrus chariot) |
| aristotle-substance | Ch 14 | Ch 13 (ousia vocabulary underlies logos/Nous discussion) |
| aristotle-categories | Ch 14 | — (ten categories; primary/secondary substance) |
| aristotle-logic | Ch 14 | — (syllogistic vs Nyāya anumāna/vyāpti) |
| aristotle-ethics | Ch 14 | — (eudaimonia; function argument; doctrine of the mean) |
| four-causes | Ch 14 | — (material/formal/efficient/final; vs pratītyasamutpāda) |
| epicurus-atom | Ch 14 | — (weight + the swerve/clinamen) |
| epicurus-ethics | Ch 14 | — (ataraxia/aponia; Tetrapharmakos; vs Cārvāka/nirvāṇa) |
| stoicism | Ch 14 | Ch 13 (Stoic pneuma/logos vocabulary echoes into later comparanda) |
| stoic-logos | Ch 14 | — (material rational pneuma; NOT-equiv brahman) |
| cynicism | Ch 14 | — (autarkeia/askēsis; ancestor of Stoicism) |
| pyrrhonism | Ch 14 | — (epochē via isostheneia; vs catuṣkoṭi/Madhyamaka) |
| academic-skepticism | Ch 14 | — (Arcesilaus/Carneades; to pithanon; vs Pyrrhonism) |
| kapila | Ch 15 | — (legendary founder-by-attribution; Purāṇic Viṣṇu-avatāra Kapila NOT-equiv) |
| samkhya-karika | Ch 15 | Ch 11 (satkāryavāda underlies vivartavāda/pariṇāmavāda split) |
| prakriti-samkhya | Ch 15 | Ch 09 (structurally-parallel-to Jain pudgala) |
| purusha-samkhya | Ch 15 | Ch 03 (structurally-parallel-to Jain jīva) |
| guna-samkhya | Ch 15 | — (guṇa vs Jain dravya-guṇa NOT-equiv) |
| satkaryavada | Ch 15 | Ch 11 (§3.2/§4.1 vivartavāda/pariṇāmavāda derive from this axiom) |
| patanjali | Ch 15 | — (grammarian-Patañjali conflation rejected) |
| yoga-darshana | Ch 15 | Ch 08 (yamas share Jain mahāvrata vocabulary, NOT-equiv) · Ch 03/07 (aṣṭāṅga vs guṇasthāna NOT-equiv) |
| citta-vritti | Ch 15 | Ch 05 (vikalpa converges with Dignāga's kalpanā/apoha) |
| citta | Ch 15 | Ch 12 (Buddhist citta as processual consciousness, inverted vs Sāṃkhya-Yoga citta) |
| manas | Ch 15 | Ch 01/03 (Jain mano-yoga) · Ch 12 (Buddhist/Yogācāra manas-vijñāna) |
| gautama-akṣapāda | Ch 16 | Ch 05 (author-anchor of the Nyāya epistemology files) |
| kaṇāda | Ch 16 | — (Vaiśeṣika founder; anchor-by-attribution like kapila) |
| nyāya-sūtra | Ch 16 | Ch 05 (four pramāṇas · pañcāvayava · fallacy catalogue worked out there) |
| vaiśeṣika-sūtra | Ch 16 | Ch 14 (padārtha scheme vs aristotle-categories) |
| dravya-vaiśeṣika | Ch 16 | Ch 01/09 (nine vs six dravyas; definition-of-substance comparison) |
| paramāṇu-vaiśeṣika | Ch 16 | Ch 01 (vs Jain paramāṇu) · Ch 14 (vs democritus-atom) |
| pañcamahābhūta | Ch 16 | Ch 15 (tanmātra → mahābhūta stage of prakṛti's evolution) · Ch 12 (Buddhist four-element demotion of ākāśa) |
| asatkāryavāda | Ch 16 | Ch 15 (§5 satkāryavāda, the opposing axiom) · Ch 11 (vivartavāda/pariṇāmavāda derive from the satkārya side) |
| praśastapāda | Ch 16 | Ch 05 (realism about universals vs Dignāga's apoha) |
| jaimini | Ch 17 | Ch 11 (paired with bādarāyaṇa: Pūrva- vs Uttara-Mīmāṃsā) |
| mīmāṃsā-sūtra | Ch 17 | Ch 05 (the pramāṇa doctrine worked out there) |
| kumārila-bhaṭṭa | Ch 17 | Ch 05 (svataḥ-prāmāṇya vs Nyāya parataḥ; the Dignāga duel) |
| prabhākara | Ch 17 | Ch 05 (five-pramāṇa count; akhyāti error-theory) |
| cārvāka | Ch 17 | Ch 05 (the anti-vyāpti attack) · Ch 14 (NOT-equiv democritus-atom) · Ch 12 (NOT-equiv anattā) |
| trimūrti | Ch 18 | Ch 11 §7.1 (Trimūrti/Tridevi preview table) |
| brahmā | Ch 18 | Ch 04/11 (the Brahmā ≠ Brahman trap) |
| viṣṇu | Ch 18 | Ch 11 (the three-school Brahman relation) |
| śiva | Ch 18 | Ch 11 (Śiva as saguṇa face of Brahman) |
| śakti | Ch 18 | Ch 15 (NOT-equiv prakṛti) · Ch 11 (NOT-equiv māyā) |
| vaiṣṇavism | Ch 18 | Ch 11 (Viśiṣṭādvaita/Dvaita sampradāyas) |
| śaivism | Ch 18 | Ch 11 (the Śaiva rejection of māyāvāda) |
| kṛṣṇa | Ch 18 | Ch 11/19 (Gītā speaker) — **contested** (avatāra vs svayaṃ bhagavān) |
| rāma | Ch 18 | Ch 19 (Rāmāyaṇa) · Ch 11 (seventh avatāra) |
| avatāra | Ch 11 | Ch 18 §2.2 (re-treated as deity doctrine) · Ch 03/10 (NOT-equiv tīrthaṅkara) |
| liṅga | Ch 18 | Ch 10 (aniconism vs the arihant mūrti) |
| naṭarāja | Ch 18 | — (the CERN/Capra physics flag lives here) |
| kāla-bhairava | Ch 18 | Ch 09 (NOT-equiv Jain kāla-dravya) |
| spanda | Ch 18 | Ch 01 (∥ Jain sat: permanence-in-change) · Ch 15 (NOT-equiv prakṛti) |
| pratyabhijñā | Ch 18 | Ch 11 (∥ and NOT-equiv Advaita) · Ch 12/05 (vs Buddhist kṣaṇavāda) |
| durgā | Ch 18 | Ch 11 (∥ avatāra, but self-manifestation not descent) |
| kālī | Ch 18 | Ch 15 (NOT-equiv prakṛti) |
| pārvatī | Ch 18 | Ch 19 (Kena Up. Umā Haimavatī antecedent) |
| gaṇeśa | Ch 18 | Ch 19 (scribe of the Mahābhārata) |
| kārttikeya | Ch 18 | — (Skanda/Murukaṉ North→South shift) |
| hanumān | Ch 18 | Ch 19 (Rāmāyaṇa Sundara Kāṇḍa; Mahābhārata Vana Parva) |
| nandi | Ch 18 | Ch 03 (the *jīva* vocabulary caution) |
| garuḍa | Ch 18 | Ch 21 planned (the amṛta-quest belongs to the churning cycle) |
| sūrya | Ch 18 | Ch 19 (Gāyatrī/Savitṛ) · Ch 04 (Pañcāyatana ≈ Brahman) |
| agni | Ch 18 | Ch 19 (yajña · ṛta) · Ch 14 (∥ and NOT-equiv stoic-logos) · Ch 09 (weak ∥ dharma-dravya) |
| indra | Ch 18 | Ch 21 planned (Bali/Vāmana; churning) — **contested** (Vedic sovereign vs Purāṇic demotion) |
| aruṇa | Ch 18 | Ch 19 (Sampāti/Jaṭāyu in the Rāmāyaṇa) |
| kāmadhenu | Ch 18 | Ch 19 (Vasiṣṭha/Viśvāmitra, Rāmāyaṇa Bāla Kāṇḍa) · Ch 21 planned (churning-ratna) |
| upaniṣad | Ch 19 | Ch 11 §1 (prasthānatrayī + the four mahāvākyas) · Ch 04 (brahman/ātman) |
| ṛta | Ch 19 | Ch 18 §7.1 (Agni as *ṛtasya gopā*) · Ch 14 (∥ stoic-logos) · Ch 12 (∥ dhamma) |
| yajña | Ch 19 | Ch 17 (Mīmāṃsā's paradigm case) · Ch 18 §7.1 (Agni the mediator) · Ch 08 (NOT-equiv ahiṃsā) |
| brahma-sūtra | Ch 19 | Ch 11 §1 (as prasthānatrayī member) · Ch 17 (∥ and NOT-equiv mīmāṃsā-sūtra) · Ch 15 (refutes Sāṃkhya) |
| bādarāyaṇa | Ch 19 | Ch 17 (paired with jaimini: Uttara- vs Pūrva-Mīmāṃsā) — **contested** (identity with Vyāsa) |
| mahābhārata | Ch 19 | Ch 18 §6.1 (Gaṇeśa the scribe) · Ch 11 (container of the Gītā) |
| rāmāyaṇa | Ch 19 | Ch 18 §2.4 (the kāṇḍa-layering behind Rāma's avatāra status) |
| gītā | Ch 19 | Ch 11 (the three Vedānta readings) · Ch 18 §2.2 (BG 4.7–8) — **contested** (which mārga is its aim) |
| samatva | Ch 19 | Ch 15 (NOT-equiv yoga-darśana's citta-vṛtti-nirodha) · Ch 12 (∥ upekkhā) · Ch 08 (∥ mādhyasthya) |
| sthitaprajña | Ch 19 | Ch 11 (∥ mokṣa-advaita) · Ch 12 (∥ upekkhā) |
| jīvanmukti | Ch 19 | Ch 11 (Advaita mokṣa mode) · Ch 07/10 (∥ and NOT-equiv arihant) · Ch 12 (∥ saupādisesa nibbāna) |
| viṣṇu-sahasranāma | Ch 19 | Ch 18 §2 (Vaiṣṇava supreme stotra) · Ch 11 (the four-school commentary split) |
| vyāsa | Ch 19 | Ch 15 (NOT-equiv the Yoga-Bhāṣya "Vyāsa") · Ch 18 §6.1 (dictation to Gaṇeśa) |
| vālmīki | Ch 19 | Ch 18 §2.4 (source-poet of the Rāma cult) |
| dāna | Ch 19 | Ch 08 (Jain lay practice; abhaya-dāna and ahiṃsā) · Ch 12 (dāna-pāramitā) |
| saṃsāra | Ch 19 | Ch 03 (Jain bandha/gati) · Ch 12 (SN 15.3; the anattā paradox) · Ch 04 (three-tradition karma) |
| nāgārjuna | Ch 20 | Ch 12 §6.1 (Madhyamaka doctrine) · Ch 06 (catuṣkoṭi) |
| mūlamadhyamakakārikā | Ch 20 | Ch 12 (śūnyatā · dvisatya) · Ch 06 (the tetralemma run destructively) |
| prasaṅga | Ch 20 | Ch 05 §7.3 (NOT-equiv Nyāya tarka) · Ch 14 (∥ and NOT-equiv pyrrhonism) |
| śāntideva | Ch 20 | Ch 12 §5 (bodhicitta · bodhisattva) |
| vasubandhu | Ch 20 | Ch 12 §6.2 (Yogācāra) · Ch 15 (the Vindhyavāsin debate) |
| abhidharmakośa | Ch 20 | Ch 12 §4 (the 75 dharmas) · Ch 03 (∥ tattvartha-sutra as a root-text-plus-commentary compendium) |
| asaṅga | Ch 20 | Ch 12 §6.2 (ālaya-vijñāna) |
| trisvabhāva | Ch 20 | Ch 12 §6.2 (Yogācāra doctrine) · Ch 11 (NOT-equiv māyā-advaita) |
| pramāṇasamuccaya | Ch 20 | Ch 05 §4 (Dignāga's two pramāṇas) · Ch 05 §6.3 (apoha) · Ch 16 (NOT-equiv nyaya-sutra) |
| dharmakīrti | Ch 20 | Ch 05 §6.2 (vyāpti grounded in real relations) · Ch 12 §3.2 (the sattvānumāna proof of anicca) |
| pramāṇavārttika | Ch 20 | Ch 05 §9 (hetu-vidyā) · Ch 05 §6.3 (causal apoha) |
| śāntarakṣita | Ch 20 | Ch 12 §6 (the Madhyamaka/Yogācāra split he adjudicates) · Ch 02 (NOT-equiv anekāntavāda) |
| kamalaśīla | Ch 20 | Ch 03 (NOT-equiv guṇasthāna) · Ch 15 (NOT-equiv yoga-darśana) |
| apratiṣṭhita-nirvāṇa | Ch 20 | Ch 12 §2.4 (NOT-equiv nibbāna-theravāda) · Ch 12 §5 (the bodhisattva ideal) |
| samudra-manthana | Ch 21 | Ch 18 §7.4 (Kāmadhenu as a churning-ratna) · Ch 11 (Lakṣmī) |
| amṛta | Ch 21 | Ch 12 (Buddhist *amata* = "the deathless," NOT a nectar) · Ch 18 §6.4 (Garuḍa's quest) |
| hālāhala | Ch 21 | Ch 18 §3 (the Nīlakaṇṭha epithet it explains) |
| kūrma | Ch 21 | Ch 11/18 (daśāvatāra 2) — **contested** (Prajāpati-tortoise reattributed to Viṣṇu) |
| vāsuki | Ch 21 | Ch 18 §3 (Śiva's neck-serpent) |
| dhanvantari | Ch 21 | — (also the presiding deity of the still-uncovered Āyurveda cluster) |
| mohinī | Ch 21 | Ch 11 §7.2 (the avatāra-vs-māyā classification question) · Ch 18 §3 (the Ayyappa sequel) |
| rāhu | Ch 21 | — (the eclipse-myth vs *siddhānta*-astronomy flag lives here) |
| ketu | Ch 21 | — (descending node; the mokṣa-ward pole to Rāhu) |
| svarbhānu | Ch 21 | Ch 18 §7.3 (the same two-layer stratification as Indra) — **contested** |
| airāvata | Ch 21 | Ch 18 §7.3 (Indra's mount) |
| uccaiḥśravas | Ch 21 | Ch 19 (the tail-wager that drives the Rāmāyaṇa's bird-line) |
| kaustubha | Ch 21 | Ch 18 §2 (Viṣṇu's iconography; Kaustubhadhāri) |
| vāruṇī | Ch 21 | — **contested** (devas or asuras?); the *surā*/*asura* folk-etymology flag |
| pārijāta | Ch 21 | Ch 18 §2.3 (the Kṛṣṇa–Satyabhāmā uprooting) |
| kalpavṛkṣa | Ch 21 | Ch 18 §7.4 (twin of Kāmadhenu) |
| śeṣa | Ch 21 | Ch 18 §2 (Viṣṇu's serpent-couch) — the cluster's one **high**-confidence node |
| kadrū | Ch 21 | Ch 18 §6.4 (the nāga/bird enmity Garuḍa inherits) |
| vinatā | Ch 21 | Ch 18 §§6.4, 7.2 (mother of Garuḍa and Aruṇa) |
| jaṭāyu | Ch 21 | Ch 19 (Rāmāyaṇa, Araṇya Kāṇḍa) |
| sampāti | Ch 21 | Ch 19 (Rāmāyaṇa, Kiṣkindhā Kāṇḍa) |
| matsya | Ch 21 | Ch 11/18 (daśāvatāra 1); the three-stage identity shift |
| varāha | Ch 21 | Ch 11/18 (daśāvatāra 3); ŚB 14.1.2 caught mid-harmonisation |
| narasiṃha | Ch 21 | Ch 11/18 (daśāvatāra 4); the boon-loophole |
| vāmana | Ch 21 | Ch 18 §7.3 (the three worlds restored to Indra); RV 1.154 Trivikrama |
| bali | Ch 21 | Ch 18 §7.3 (dispossesses Indra) — **contested** (grace vs punishment; Onam) |
| paraśurāma | Ch 21 | Ch 19 (Mahābhārata + Rāmāyaṇa Bāla 74–76) · Ch 18 §2.4 (the tejas-handover to Rāma) |
| kalki | Ch 21 | Ch 11/18 (daśāvatāra 10); two confidence tiers; the Kālacakra borrowing |
| mettā | Ch 22 | Ch 04 (the positive ground of Buddhist ahiṃsā) · Ch 12 (brahmavihāra practice) |
| karuṇā | Ch 22 | Ch 12 §5 / Ch 20 §3 (*mahākaruṇā* → bodhicitta; Śāntideva) |
| muditā | Ch 22 | — (the least-practised brahmavihāra; structurally essential) |
| upekkhā | Ch 22 | Ch 12 §3.1 (grounded in anattā) · Ch 19 §6.3.1 (∥ samatva) |
| maitrī-jain | Ch 22 | Ch 04/08 (the affective ground of the ahiṃsā vow) · TS 7.11 fetched directly |
| pramoda | Ch 22 | Ch 03 (the *māna* kaṣāya it opposes) |
| kāruṇya | Ch 22 | Ch 08 (motive behind the ahiṃsā vow) |
| mādhyasthya | Ch 22 | Ch 08 (∥ aparigraha — internal non-attachment) · Ch 03 (kaṣāya-restraint) |
| ahiṃsā-vedic | Ch 22 | Ch 04 (NOT-equiv Jain ahiṃsā, despite the shared maxim) · Ch 15 (Yoga-Sūtra II.30 yamas) |
| āyurveda | Ch 23 | Ch 16 §6 (pañcamahābhūta) · Ch 15 (NOT-equiv Sāṃkhya prakṛti) |
| caraka | Ch 23 | Ch 15 (the guṇa-typology's borrowed vocabulary) — **contested** (person or lineage?) |
| suśruta | Ch 23 | Ch 21 §5 / Ch 19 (the Dhanvantari-vs-Divodāsa frame; the same stratigraphy as the Rāmāyaṇa) — **contested** |
| tridoṣa | Ch 23 | Ch 16 §6 (each doṣa = two mahābhūtas) · Ch 15 (NOT-equiv guṇa-sāṃkhya) |
| ammonius-saccas | Ch 24 | Ch 13 §1 (Plotinus's teacher) — **blocked** (doctrine unattested; the "two Ammonii" split, and a third Ammonius Hermiae) |
| iamblichus | Ch 24 | Ch 13 §5 (the contemplation-vs-ritual divide) · Ch 24 §6.2 (contested henad origin) |
| theurgy | Ch 24 | Ch 13 §5 (∥ and NOT-equiv henosis) · Ch 24 §5 (NOT-equiv mimamsa apūrva; ∥ yajña) |
| chaldean-oracles | Ch 24 | Ch 24 §4.4 (the provenance problem: no fragment survives outside a Neoplatonist quoting it) |
| syrianus | Ch 24 | Ch 13 §6 (teacher of Proclus) · Ch 14 (Aristotle's *Metaphysics* commentary) |
| proclus-henad | Ch 24 | Ch 13 §6 (Proclus's signature doctrine) · Ch 18/11 (∥ and NOT-equiv the Hindu one-and-many) — **contested** (Iamblichus vs Syrianus origin) |
| marinus | Ch 24 | Ch 13 §6 (Proclus's *diadochos*) · Ch 24 §6.4 (biography as argument; theurgic virtue at the top of the ladder) |
| damascius | Ch 24 | Ch 06 / Ch 20 (∥ and NOT-equiv catuṣkoṭi/prasaṅga) · Ch 11 (NOT-equiv nirguṇa Brahman) · Ch 13 §3 (NOT-equiv plotinus-one) |
| simplicius | Ch 24 | Ch 14 (the channel through which ~⅔ of verbatim Presocratic fragments survive) · Ch 05/20 (∥ and NOT-equiv the bhāṣya tradition) |
| psyche-neoplatonic | Ch 24 | Ch 13 §2 (the third hypostasis) · Ch 03/09 (NOT-equiv jīva) · Ch 11 (NOT-equiv brahman — Brahman maps to Nous) |
| liber-de-causis | Ch 24 | Ch 13 §6 (Proclus's *Elements* in Arabic dress) · Ch 14 (NOT-equiv aristotle-substance — Aquinas, 1272) |
| pseudo-dionysius | Ch 24 | Ch 13 §5 (∥ and NOT-equiv henosis) · Ch 24 §6.2 (deletes henad-mediated causation) — **contested** (author's identity) |
| vātsyāyana | Ch 25 | Ch 16 (Nyāya-Bhāṣya on the nyaya-sutra) · Ch 05 (the pramāṇa agenda he sets) — the chapter's one **high**-confidence node |
| śaṅkara | Ch 25 | Ch 11 (the Advaita doctrine he systematised) · Ch 10 (∥ kundakunda) · Ch 18 (NOT-equiv the god Śiva) · Ch 19 (bādarāyaṇa lineage) |
| maṇḍana-miśra | Ch 25 | Ch 17 (Kumārila's student) · Ch 11 (Brahmasiddhi; avidyā in the jīva) — **contested** (identity; and whose Advaita was primary) |
| sureśvara | Ch 25 | Ch 11 (Vārttika-prasthāna; avidyā in Brahman) · Ch 25 §6 (NOT-equiv maṇḍana-miśra) |
| vyāsa-yogabhāṣya | Ch 25 | Ch 15 (the bhāṣya that defines the Yoga darśana) · Ch 19 (NOT-equiv the Mahābhārata Vyāsa) — **contested**, three attributions |
| vindhyavāsin | Ch 25 | Ch 15 (Sāṃkhya reformer; the Sāṃkhyakārikā dating thesis) · Ch 20 (the Ayodhyā debate with Vasubandhu's circle) |
| ajīva | Ch 26 | Ch 09 (the five non-soul dravyas in full) · Ch 01 (pudgala) — ⚠️ its `part-of: jiva` edge inverts the partition; flagged in Ch 26 §2.3 for a maintenance pass |
| kārmaṇa-vargaṇā | Ch 26 | Ch 01 (paramāṇu · skandha) · Ch 03 (bandha) — **low** confidence; Digambara *Ṣaṭkhaṇḍāgama*/*Dhavala*, not in the Tattvārtha Sūtra |
| leśyā | Ch 26 | Ch 03 (guṇasthāna correlation — from aggregation only) · Ch 10 (Śvetāmbara *Uttarādhyayana* 34, not the TS) |
| mohanīya | Ch 26 | Ch 03 (the guṇasthāna ladder as its staged demolition) · Ch 08 (cāritra) · Ch 03 (kaṣāya — the 16 kaṣāya-vedanīya sub-types) |
| nāmarūpa | Ch 27 | Ch 12 (link 4 of paṭiccasamuppāda; the khandha mapping) · Ch 03/09 (NOT-equiv jīva — process vs substance) |
| pratyakṣa-buddhist | Ch 27 | Ch 05 (Dignāga's 2-pramāṇa system; apoha) · Ch 16 (NOT-equiv pramāṇa-nyāya — nominalism vs realism) · Ch 07 (NOT-equiv Jain pratyakṣa — the terminological inversion) |
| nyāyabindu (Dharmottaraṭīkā) | Ch 27 | Ch 05 (dharmottara the person; hetu-vidyā) · Ch 20 (NOT-equiv pramāṇavārttika — manual vs magnum opus) · Ch 18 (∥ shaivism — the Pratyabhijñā adversary) |
| makkhali-gosāla | Ch 27 | Ch 10 (the Ājīvika school) · Ch 03/26 (NOT-equiv karma and mokṣa — the word kept, the efficacy denied) · Ch 10 (mahāvīra companionship) |
| modern-atom | Ch 28 | Ch 01 (NOT-equiv paramāṇu — and the intrinsic-qualities break that leśyā depends on) · Ch 16 (NOT-equiv paramāṇu-vaiśeṣika) · Ch 14 (NOT-equiv democritus/epicurus; the clinamen misreading) · Ch 18 §4.2 (NOT-equiv naṭarāja — the CERN plaque) |
| quantum-complementarity | Ch 28 | Ch 02 (∥ **and** NOT-equiv anekāntavāda — the Kothari analogy, and the inversion) · Ch 06 (NOT-equiv many-valued-logic) |
| naigama-naya | Ch 02 | Ch 02 §4 (the first of the seven nayas; the teleological standpoint) — covered in prose, row added in the Ch 28 re-derivation |
| saṃgraha-naya | Ch 02 | Ch 02 §4 (the generic/class standpoint; maximum abstraction) — covered in prose, row added in the Ch 28 re-derivation |
| vyavahāra-naya | Ch 02 | Ch 02 §4 (the practical standpoint; unpacks the saṃgraha class into distinctions) — covered in prose, row added in the Ch 28 re-derivation |
| psellos | Ch 29 | Ch 24 §4.4 (the Chaldean Oracles' provenance problem, made concrete) · Ch 13/24 (Proclus's lost Chaldean treatise) — **contested** (his own religious position; a 1054 charge from the future Patriarch) |
| eriugena | Ch 29 | Ch 13 (∥ and NOT-equiv plotinus-one) · Ch 11 (∥ and NOT-equiv advaita-vedānta — the *vivarta* row is load-bearing) · Ch 12 (NOT-equiv śūnyatā — *nihil per excellentiam* is a superlative predicated of a plenum) — **contested** (pantheism) |
| vārṣagaṇya | Ch 29 | Ch 15 (the Ṣaṣṭitantra and the Sāṃkhyakārikā-as-abridgement thesis) · Ch 25 (vindhyavāsin, his pupil) · Ch 30 (Vācaspati Miśra as the instrument of the reconstruction) — **low** confidence, by evidence |
| govinda-bhagavatpāda | Ch 29 | Ch 25 §3.1 (the *Vivekacūḍāmaṇi* attribution that undercuts his sole textual naming) · Ch 11 (the Gauḍapāda→Śaṅkara joint) · Ch 19 (∥ vyāsa — a name in a genealogy) — **low** |
| utpaladeva | Ch 29 | Ch 18 (pratyabhijñā, the doctrine he named — the term is absent from Somānanda's *Śivadṛṣṭi*) · Ch 20/27 (the Dharmakīrti manoeuvre; NOT-equiv vijñaptimātratā) |
| prajñākaragupta | Ch 29 | Ch 27 (the *niścaya-pratyaya* he rejects) · Ch 05 §9 (dharmottara) · Ch 20 (the Pramāṇavārttika commentarial line) · Ch 07 (∥ and NOT-equiv kevala-jñāna — omniscience as an epistemological result) |
| vāgbhaṭa | Ch 29 | Ch 23 (the third of the bṛhat-trayī; the AH's Tibetan/Arabic travel) · Ch 31 (A. Hṛ. Sū. 11/24, the tissue-fire rate relation) — **contested** (one Vāgbhaṭa or two) |
| atri | Ch 29 | Ch 21 §4 (svarbhānu → rāhu/ketu; the naming-vs-identity caution one step further) · Ch 19 (Ṛgveda Maṇḍala 5) — **contested** (what RV 5.40 *is*) |
| prakāśātman | Ch 30 | Ch 11 (the Vivaraṇa-prasthāna's māyā apparatus) · Ch 25 (padmapāda, whose *Pañcapādikā* he glosses) · Ch 15 (∥ **and** NOT-equiv prakṛti-sāṃkhya — *mūlāvidyā* in prakṛti's job-slot) — **contested** (a three-century dating spread) |
| vācaspati-miśra | Ch 30 | Ch 15 (*Tattvakaumudī*, 90+ MSS) · Ch 15 (*Tattvavaiśāradī* on the Yoga-bhāṣya) · Ch 16 (the Nyāya *tātparyaṭīkā*) · Ch 17/05 (*Tattvabindu*; the Bhāṭṭa endorsement) · Ch 29 §4 (the instrument by which Vārṣagaṇya is reconstructed) — **contested** (898, era unstated) |
| agni-āyurveda | Ch 31 | Ch 18/19 (∥ **and** NOT-equiv the Vedic deity agni — a §8 tradition-split) · Ch 23 (the four states keyed to the doṣas) · Ch 16 (the five *bhūtāgni*, one per mahābhūta) |
| dhātu | Ch 31 | Ch 23 (the structural counterpart to tridoṣa) · Ch 12 (NOT-equiv skandha-buddhist — tissues sustained vs constituents in an anattā argument) · Ch 15 (NOT-equiv prakṛti-sāṃkhya) — **contested**: the tradition transmits three incompatible nourishment models at once |
| mala | Ch 31 | Ch 23 (kapha as the mala of rasa, pitta of rakta — the standard picture reversed) · Ch 10 (NOT-equiv pāpa — a residue with a job, not a stain) |
| aghāti-karma | Ch 32 | Ch 26 §5 (the other family of TS 8.4's eight) · Ch 10 (the arihant/siddha difference **is** this residue; *tīrthakaratva* as item 42 of nāma-karma) · Ch 03 (why the ladder's top rungs stop activity rather than clarify sight) — closes Ch 26 §6.4 |
| īryāpathika-āsrava | Ch 32 | Ch 03 (TS 6.4 fetched, upgrading `asrava.md`'s aggregation-only mechanism) · Ch 03 (guṇasthānas 11–13) · Ch 19 (∥ **and** NOT-equiv jīvanmukti — deny new adhesion vs deny new relevance) |
| varuṇa | Ch 33 | Ch 19 (ṛta's **moral** guardian, as Agni is its ritual one) · Ch 18 (∥ indra — narrowed vs displaced) · Ch 11 (NOT-equiv māyā-advaita) · Ch 04 (NOT-equiv karma-vedic — the road not taken) — **contested** (the withdrawn Ouranos etymology) |
| vṛtra | Ch 33 | Ch 18 (indra's epithet *Vṛtrahan*) · Ch 19 (∥ ṛta — a cosmos whose failure is blockage) · Ch 21 (∥ bali — the rehabilitated adversary) — **contested** (dragon or obstruction: Benveniste & Renou vs the combat-myth reading) |
| verethragna | Ch 33 | Ch 18 (∥ **and** NOT-equiv indra) · Ch 21 (∥ **and** NOT-equiv avatāra-vedānta — ten forms, no narrative) — the corpus's **first Iranian node**; **contested** three ways (Benveniste & Renou / Thieme / the traditional war-god view) |
| prahlāda | Ch 33 | Ch 21 (narasiṃha; bali, his grandson) · Ch 11/18 (the *navavidhā bhakti* of BhP 7.5.23–24) · Ch 18 (NOT-equiv śaivism — the *Śiva Purāṇa* lists the same nine) · Ch 06 (∥ catuṣkoṭi — the boon's failed disjunction, resonance only) |
| balarāma | Ch 33 | Ch 21 (the disputed ninth daśāvatāra slot: Buddha or Balarāma) · Ch 09 (part-of the utsarpiṇī/avasarpiṇī 63) · Ch 08 (ahiṃsā — the Jain criterion that inverts the ranking) · Ch 19 (NOT-equiv gītā — bondage in the intention vs in the act) |
| jina | Ch 10 | Ch 07 (kevala-jñāna) · Ch 03 (the four kaṣāyas as the "inner enemies" conquered) · Ch 12 (⚠️ Buddhist usage occasionally applies *Jina* to the Buddha — overlap without identity) — covered in Ch 10's prose; row added in the Batch-42 re-derivation |
| tattvārtha-sūtra | Ch 01 | the root text of the whole Jain layer — quoted directly in Chs 01, 03, 07, 08, 09, 10, 26 and 32, and the anchor text named in `progress.md`; row added in the Batch-42 re-derivation |
| samyagdarśana | Ch 07 | Ch 07 (the first of the *ratnatraya*; TS 1.1) · Ch 03 (the 4th guṇasthāna, where progress genuinely begins) · Ch 08 (what makes conduct *samyak* rather than mere behaviour) — row added in the Batch-42 re-derivation |
| gauḍapāda | Ch 25 | Ch 11 (Śaṅkara's *paramaguru*; *ajātivāda*, turīya, *asparśa-yoga*) · Ch 12 (∥ **and** NOT-equiv madhyamaka) · Ch 15 (NOT-equiv the Sāṃkhya-kārikā commentator of the same name) — **contested** (date; ch. 4's authorship; "multiple Gauḍapāda-s") |
| padmapāda | Ch 25 | Ch 30 (the Vivaraṇa side of the locus dispute; *pratibimbavāda*) · Ch 11 (the *Pañcapādikā* on the first four aphorisms) |
| vidyāraṇya | Ch 25 | Ch 11 (Śṛṅgeri jagadguru; the constructed fame of Śaṅkara) · Ch 30 §7 (*ābhāsavāda*, contested attribution) · Ch 24/29 (∥ marinus — the successor-hagiographer) — **contested** (three open identifications; the Vijayanagara foundation story judged legendary) |
| sarvajñatva (omniscience-vedānta) | Ch 11 | Ch 07 (**NOT-equiv** kevala-jñāna — Advaita attributes omniscience to *saguṇa* Brahman/Īśvara at the *vyāvahārika* level, never to *nirguṇa* Brahman, and the *mukta-jīva* does **not** become personally omniscient) · Ch 29 §7 (∥ the Buddhist argument for a founder's omniscience) — row added in the Batch-42 re-derivation |
| tīrthaṅkara | Ch 10 | Ch 09 (24 per half-cycle; pārśvanātha 23rd, mahāvīra 24th) · Ch 11/21 (**NOT-equiv** avatāra — apotheosis vs descent) · Ch 32 (*tīrthakaratva* is item 42 of nāma-karma: the office is technically a species of bondage) · Ch 33 (the Jain 63 *śalākāpuruṣa*s, of whom 24 are tīrthaṅkaras) — row added in the Batch-42 re-derivation |
| somānanda | Ch 18 | Ch 18 §Pratyabhijñā (the *Śivadṛṣṭi*, "the first philosophical treatise on monistic Śaivism" — and the founding text that never uses the word *pratyabhijñā*) · Ch 11/30 (**NOT-equiv** advaita-vedānta and māyā-advaita: the world is Śiva's free self-expression, "not Māyā's illusion") · Ch 12 (NOT-equiv vijñaptimātratā, a named target of ŚD) — **contested** (dates; the Vasugupta attribution) |
| abhinavagupta | Ch 18 | Ch 18 §Pratyabhijñā (*vimarśa*; the *Tantrāloka*'s 37-chapter Trika synthesis) · Ch 29 §6 (his manuscripts are the vehicle by which Utpaladeva's lost *Vivṛti* survives) · Ch 11 (∥ **and** NOT-equiv mokṣa-advaita — *rasāsvāda* as an **approximation** of *brahmāsvāda*, "not a complete dissolution") · Ch 25/30 (∥ śaṅkara — the systematiser whose name names the system) — **contested** (dates) |
| ahura-mazdā | Ch 33 | Ch 33 §4.1 (the three-term correspondence: *ahura*/*asura*, *aṣ̌a*/*ṛta*, and fire as the guardian of both) · Ch 19 (∥ agni — *Aṣ̌a Vahiṣta*'s fire against *ṛtasya gopā*) · Ch 33 §1 (∥ **and** NOT-equiv varuṇa) — **contested** (dualist or monotheist; Haug 1884) |
| sarvajñātman | Ch 34 | Ch 34 §4.4 (***dvāra***: Brahman alone is the material cause, ajñāna only the instrumentality — the counter-example to the *mūlāvidyā*-as-prakṛti reading Ch 30/Ch 15 draw) · Ch 30 (the third holder of *pratibimbavāda*, and the man who **splits** the *āśraya* axis from the material-cause axis) · Ch 34 §5.3 (provenance on the text ≠ provenance on the biography) — **contested** (three datings spanning ~1,400 years; he salutes **Deveśvara**, not Sureśvara, as guru) |
| amalānanda | Ch 34 | Ch 34 §2 (storey 4 of the five-text *Vedānta Śāstra*; the *Kalpataru* defends the *Bhāmatī* against **Dvaita** objections postdating it) · Ch 34 §2.3 (a *Pañcapādikā-darpaṇa* on the **rival** school — fact recorded, "early link" inference declined) · Ch 30 (the Bhāmatī line he continues) — the corpus's **control case** for lineage claims: three formulations that reconcile once *dīkṣā*- and *vidyā*-guru are distinguished |
| appayya-dīkṣita | Ch 34 | Ch 34 §7.2 (Advaitin or Śivādvaitin? three readings; Duquette's "single-handedly established") · Ch 34 §6.1 (the *Siddhāntaleśasaṃgraha* as a 16th-c. doxography of Advaita's internal splits — and where it parts from §4 of the charter, in exactly one place) · Ch 34 §2 (storey 5, written because storey 4 was unreadable) · Ch 18 (Śivādvaita) · Ch 11 (NOT-equiv-adjacent: viśiṣṭādvaita, the opponent absent from his titles) — **contested** |
| cakrapāṇidatta | Ch 34 | Ch 34 §3 (the *Āyurvedadīpikā*; Caraka is printed inside it) · Ch 34 §5 (the **regnal anchor** — best-dated person in the corpus, because his family served a king) · Ch 34 §8.1 + Ch 31 §4.2 (the *nyāya* attribution: **four** not three, spread across three commentarial traditions, and the enumeration itself from a **2017** textbook) |
| ḍalhaṇa | Ch 34 | Ch 34 §4.1 (the three-part *pariṇāma* — *sūkṣma*/*mala*/*sthūla-bhāga* — answering the fasting objection to *kṣīra-dadhi*) · Ch 34 §4.2 (**mala admitted as a *śalya***) · Ch 34 §4.3 (***rakta* as a fourth doṣa — *for surgery*: the doṣa-count is discipline-relative**) · Ch 34 §5 (**citation-bracketing**) · Ch 31 (the Āyurvedic body) — ⚠ open hole: **which** lost commentators the *Nibandhasaṅgraha* preserves is unrecorded |
| hemacandra | Ch 34 | Ch 34 §6 (refutation-doxography: 32 verses against six named schools) · Ch 34 §8 (**the cheapest upgrade path in the corpus** — Malliṣeṇa's *Syādvādamañjarī*, named by Chs 02's `syādvāda` and `saptabhaṅgī` nodes, is a commentary on those verses) · Ch 33 (the *Triṣaṣṭiśalākāpuruṣacaritra*; and ***Ardhacakrin* — Kṛṣṇa ranked "half-cakravartin" in the category name**) · Ch 08 (sallekhanā, by which he died) |
| raseśvara | Ch 34 | Ch 34 §7.1 (the charge of **deferral** against the six darśanas, and the alchemy as its second premise) · Ch 19 (∥ **and** NOT-equiv jīvanmukti — same demand, inverted conclusion about the body) · Ch 09/10 (NOT-equiv siddha — perfected by having **no** body vs an **indestructible** one) · Ch 23 (NOT-equiv vāgbhaṭa; and nāgārjuna, Ch 12) — **contested**: an 1882 dating echoed by one source against 10th–12th-c. root texts |
| hiraṇyakaśipu | Ch 33 | Ch 33 §5.3.1 (*Bhāgavata* 7.3.35–38 in Tagare; **the clause that fails first is the first one** — the boon quantifies over what *Brahmā* created) · Ch 33 §5.3.2 (the Jaya–Vijaya frame: enmity **assigned**, not chosen) · Ch 21 (narasīṃha, whose form is built to the boon's specification) · Ch 06 (∥ **and** NOT-equiv catuṣkoṭi **and** many-valued-logic — a sloppy enumeration fails in a perfectly two-valued world) |
| haricandra | Ch 35 | Ch 35 §1 (the earliest Caraka commentator; a **small portion** of the *Carakanyāsa* survives) · Ch 35 §5 (**the fragment and the reputation** — ~25 later authors quote him; Hemādri calls him the model of the Caraka commentators) · Ch 35 §5.1 (**argument preserves what praise does not** — his eighteen *kṣaya*s and the *gulma* distinction reach us through Niścalakara, Śivadāsasena and Indu **disagreeing** with him) · Ch 35 §7.1 (Niścalakara refuses the *Aṣṭāṅgahṛdaya* attribution: Vāgbhaṭa quotes him) · Ch 35 §9.2 (six other Haricandras) · Ch 35 §11 (the *Mahāvyutpatti* entry, Tibetan **Seṅ-ge zla-ba** — the chapter's only non-Indian anchor) · Ch 23 (Āyurveda) |
| jejjata | Ch 35 | Ch 35 §4 (**Meulenbeld's rule** — "as Jejjaṭa's date is disputed, it is preferable to depart from another fact"; the standard reference independently reaches this node's contested verdict, and supplies a **fourth** date, 7th–8th c., the first not routed through Vāgbhaṭa) · Ch 35 §4.1 (**the inverse rule** — being quoted is a harder fact than being dated, so he still orders Haricandra and Indu) · Ch 35 §5.3 (preserved in Ḍalhaṇa's archive) · Ch 35 §7.2 (the Kerala discipleship, rejected) · Ch 34 §5 — **contested** |
| gayadasa | Ch 35 | Ch 35 §5.2 (**the arithmetic of partial survival** — the *Nyāyacandrikā* on the Nidānasthāna in **one manuscript**, the rest lost, yet known to have covered the whole *Suśrutasaṃhitā* because Ḍalhaṇa quotes it throughout: the evidence for **extent** and the evidence for **wording** come from different places) · Ch 35 §5.3 (with Jejjaṭa, the two named occupants of the *Nibandhasaṅgraha* archive) |
| candrata | Ch 35 | Ch 35 §2 (bracketed 650–1050 by Ravigupta's *Siddhasāra* below and Cakrapāṇidatta above, narrowed to 900–1050) · Ch 35 §4 (the bracket Meulenbeld **refused** to build on Jejjaṭa) · Ch 35 §5 (his introductory verses are the corpus's clearest witness to Haricandra's standing) · Ch 35 §9.3 (**the queue premise that failed** — "Vāgbhaṭa's grandson" rests on untrustworthy colophons, and Tisaṭa's own authority-list omits Vāgbhaṭa) · Ch 35 §10 (the Sūrya observation, declined) |
| arunadatta | Ch 35 | Ch 35 §2 (**dated by having been contradicted** — the strongest form of citation-bracketing, since a later writer does not invent an opponent to refute) · Ch 35 §6 (**the fifth commentarial operation: EDIT** — at *Aṣṭāṅgahṛdaya* Ci. 19.98 he and the editors print **Śiva/Śivasuta** where Indu reads **Jina/Jinasuta**; Tārā passed over in silence) · Ch 35 §6.1 (three limits on that finding) · Ch 35 §9.2 (Gode's three men of the name) · Ch 34 §8.1 + Ch 31 (the *eka-kāla* position inside the *dhātu* dispute) |
| hemadri | Ch 35 | Ch 35 §3 (**the bracket that moved** — 1260 is the first year of his career, not the date of his medical work; Gode dates the *Āyurvedarasāyana* to 1271–1309, so Ḍalhaṇa's upper bound loosens to c. 1309) · Ch 35 §3 (⚠ the hole: no source names **which** of his works quotes Ḍalhaṇa) · Ch 35 §5 (he calls Haricandra the model of the Caraka commentators) · Ch 35 §2 (he dates Aruṇadatta by disagreeing with him) · Ch 34 §5 |
| indu | Ch 35 | Ch 35 §6 (**the commentary that shows another commentary editing** — Jina/Jinasuta glossed as the Buddha and Avalokiteśa; Āryatārā, Parṇaśabarī, Aparājitā; Ratnaketu as a *dhāraṇī*) · Ch 35 §6.1 (he is **not** thereby a Buddhist — Manu *and* Buddha, but Hindu-type *maṅgala*s) · Ch 35 §7.2 (**the best argument in the chapter** — his preface complains of *bad commentaries*, so at least one generation preceded him, and he refutes his own discipleship in justifying his book) · Ch 35 §8 (Meulenbeld vs P. V. Sharma, and the **unreliable printed text** that undercuts both) · Ch 35 §9.1 (the Kerala tradition's two rejected claims) — **contested** |
| nathamuni | Ch 36 | Ch 36 §2 (**the 120-year problem** — 823–951 is 128 years, and the alternative 582–922 is 340) · Ch 36 §7 (**compilation as the founding act** — the *Nālāyira Divya Prabandham* is what makes Śrī Vaiṣṇavism a Sanskrit philosophical tradition with a Tamil devotional canon inside it; both his own works are lost) · Ch 36 §7.1 (the recovery-legend read for what survives the miracle: a **text-critical statement dressed as a vision**) · Ch 36 §7.2 (the lost *Nyāyatattva* reconstructed from citations — **44 in Vedānta Deśika alone** — moving the material-cause thesis two generations before Rāmānuja) · Ch 35 §5.3 (∥ the same shape in medicine) — **contested** |
| yamunacarya | Ch 36 | Ch 36 §2 (918–1038 = 120 years) · Ch 36 §3.1 (**three incompatible accounts of his relation to Rāmānuja**, and why two of them are compression rather than evidence; his own three dying wishes undercut Wikipedia's summary line) · Ch 36 §8 (**the *Āgamaprāmāṇya* passage that inverts when lifted from its *pūrvapakṣa*** — "we do not regard Brahmins as a distinct species" is the objection his book exists to defeat) · Ch 36 §8 (the Pāñcarātra defence conducted on Mīmāṃsā's own ground) · Ch 19 (the *Gītārthasaṅgraha*'s three-hexad division, recorded in `gita.md` before this node existed) — **contested** |
| ramanuja | Ch 36 | Ch 36 §2.2 (**Sydnor**: reconstructing his historical life is "nearly impossible"; Carman's 1077–1157 "ultimately unverifiable") · Ch 36 §3 (**succession without teaching** — he and Yāmuna never met; authority transmitted by sign) · Ch 36 §4 (**what a founder's node is for**: dates, works, and whether the biography is history — and the works dispute has doctrinal teeth, since on the IEP's reading the **Gadya Traya is not his** and *prapatti* loses its first-person voice) · Ch 36 §4.1 (**a scholar's name on a date is not evidence he argued for it** — Carman's own encyclopedia entry prints the traditional dates) · Ch 11 (Viśiṣṭādvaita as doctrine) · Ch 37 (the *saptavidhā anupapatti* against avidyā) — **contested** |
| madhva | Ch 36 | Ch 36 §5 (**four reference works, four datings**; B. N. K. Sharma published two of them himself, 1962 and 2000) · Ch 36 §5.1 (**one charge that reads as two findings** — Appayya Dīkṣita → Mesquita "without verification" → Wikipedia in two paragraphs; had the node been written from encyclopedias alone it would have recorded convergence and been wrong about the evidence) · Ch 36 §5.2 (Rao & Sharma's method — independent pre-Madhva attestation, eight witnesses for *Paiṅgi* alone — and the **two arguments from silence**; what the corpus declines to conclude) · Ch 11 (Dvaita as doctrine) · Ch 34 (Appayya) — **contested** |
| shrikantha | Ch 36 | Ch 36 §6 (the *Brahmamīmāṃsābhāṣya* as Śivādvaita's root text) · Ch 36 §6.1 (**the internal evidence**: Appayya's pure non-dualism does not match Śrīkaṇṭha's qualified non-dualism, and Dasgupta calls the *Śivārkamaṇidīpikā* an attempt to *harmonize* — **harmonising is not expounding**) · Ch 36 §6.2 (**five readings, 3100 BCE to the 15th c.**; and the three-way distinction between inventing a **man**, a **text**, and a ***Vedānta*** — only the third is what McCrea's title claims, and a popular source had already made the upgrade) · Ch 34 §7 — **contested** |
| sivadvaita | Ch 36 | Ch 36 §6 (**a school founded by moving one text across an axis** — Duquette: Appayya's reading of Śrīkaṇṭha's *pariṇāmavāda* as *vivartavāda* establishes it as independent of Śaiva Siddhānta; the 1580 *śaivādvaitaikasāmrājya* inscription) · Ch 36 §6 (⚠ the corpus's own taxonomy from Ch 11 turns out to be **the instrument that made a school**, not a neutral description) · Ch 11 (pariṇāmavāda / vivartavāda) · Ch 18 (Śiva) · Ch 34 (Appayya) |
| udayana | Ch 37 | Ch 37 §3 (**the self-dating verse that sits in one manuscript** — Śaka 906 = 984 CE, and D. C. Bhattacharyya's four counters, of which the emendation *tarkāmvarāṅka* → *tarkāvarāṅka* moves it seventy years; the corpus adopts NEITHER date, because the two reports of Bhattacharyya's conclusion disagree and neither follows from the evidence listed) · Ch 37 §3.1 (**Cāṇḍupaṇḍita's synchronism** — Udayana defeated Śrīharṣa's father, which supplies a motive for the *Khaṇḍana*; held at arm's length twice, with an unreconciled reign-date problem) · Ch 37 §3.2 (the nine arguments of the *Nyāyakusumāñjali*) · Ch 16 (his definitions; Īśvara directing atomic combination) · Ch 05 (jāti — the six exclusion criteria) — **contested** |
| sriharsa | Ch 37 | Ch 37 §2.1 (**assert nothing, and be claimed by anyone** — the *khaṇḍana-yukti*, the three definitional criteria, and four scholarly readings of his affiliation; a book of pure refutation has no thesis to read off, which is a property of the genre and not a gap in the scholarship) · Ch 37 §2.1 (⚠ **two things deliberately not said** — not *vitaṇḍā*, which SEP says the text does not use; and not "rejects reason entirely," which is a slide from pessimism about definability) · Ch 37 §6 (the lost Dvaita reply, Viṣṇudāsācārya's *Khaṇḍana-khaṇḍana*, surviving only in Vyāsatīrtha's quotations) · Ch 30 — **contested** |
| anandabodha | Ch 37 | Ch 37 §2.3 (**the arsenal** — Dasgupta: "most of Ānandabodha's arguments were borrowed by the later writers of the Vedānta school"; the argument against the perceptibility of difference, which is Śrīharṣa's move one generation earlier and looser) · Ch 37 §4 (**the *anirvacanīya* statement of avidyā** — the neither-real-nor-unreal cause of world-appearance, which is precisely what Rāmānuja's saptavidhā anupapatti attacks) · Ch 37 §2.7 (one of the two Advaitins whose arguments Vyāsatīrtha collected in order to refute) |
| citsukha | Ch 37 | Ch 37 §2.2 (**destroy, then define anyway** — Dasgupta's contrast with Śrīharṣa, and the cost accepted deliberately: a definition is a target, and Śrīharṣa's whole book argues no definition survives contact) · Ch 37 §2.2 (**two independent sources 86 years apart** — Dasgupta 1932 and Das/SEP 2018, writing about different men — converge on his dependence on Śrīharṣa) · Ch 30 (the locus of avidyā approached by definition rather than by substrate) · Ch 34 |
| nrisimhasrama | Ch 37 | Ch 37 §2.4 (**transmit, and add nothing** — he commented across the entire Vivaraṇa stack and "has not put forward any new interpretation … yet as a commentator he is superb": a real position on the axis, with invisibility as its cost, and a tradition with a vocabulary of praise for it) · Ch 37 §2.4 (⚠ **the claim that queued him did not survive** — the Appayya *Parimala* link is unattested by three sources with every occasion to make it; both nodes qualified) · Ch 30 (the Vivaraṇa side) · Ch 34 |
| mallisena | Ch 37 | Ch 37 §2.5 (**a dialectic conducted on behalf of a theory about the limits of assertion** — the *Syādvādamañjarī* against six schools, defending anekāntavāda: not "you are wrong" but "each of you has absolutised one standpoint") · Ch 37 §2.5 (**the colophon that names the weekday** — Śaka 1214 = 1292 CE, matching Dasgupta's independent 1922 dating; so the discipline's chronic vagueness is a fact about what SURVIVED, not about how these authors wrote — and "with the help of Jinaprabhasūri," complicating the one-author picture in the first colophon the corpus read directly) · Ch 02 (syādvāda, saptabhaṅgī) · Ch 34 §8 (Hemacandra's 32 verses, the base text) |
| vyasatirtha | Ch 37 | Ch 37 §2.6 (**"demolition precedes construction"** — the pole opposite Śrīharṣa, and the source of the chapter's rule: what a polemicist declines to assert determines who can later claim him) · Ch 37 §2.7 (**the *Nyāyāmṛta*'s method is COLLECTION** — Dasgupta and Anantakrishna Sastri from opposite ends; therefore a **source** for Advaita, which is what lets Ch 36 §5.2 use its quotations as evidence) · Ch 37 §6 (rounds 1 and the lost *Khaṇḍana-khaṇḍana* he alone preserves) · Ch 11 · Ch 36 §5 |
| madhusudana-sarasvati | Ch 37 | Ch 37 §5 (**the answer, and the strange thing after it** — the *Advaitasiddhi*, then the *Bhaktirasāyana*, "the only independent treatise on bhakti written by a major Advaita preceptor") · Ch 37 §5 (**devotion AFTER liberation**, duality "assumed for the sake of devotion" — which makes duality something the liberated may ELECT; the hinge is that Kṛṣṇa is identified with *nirguṇa* Brahman, the opposite route to the Vaiṣṇava Vedāntas' personal Brahman) · Ch 37 §5 (⚠ Nelson: the thought "has received little careful study," the scholarship "largely uncritical" — a position widely admired and rarely examined) · Ch 37 §5 (five datings, one argued; the Śeṣagovinda–Appayya synchronism) · Ch 11 (the sharpest modification of mokṣa-advaita in the corpus) — **contested** |
| dhamma | Ch 12 | Ch 12 §3.0 (**the four senses of Pali *dhamma***, and why senses 3 and 4 — mental objects, and the 82 irreducible momentary events — are what make the anattā argument of §3.1 work) · Ch 12 §3.0 (⚠ the Abhidhamma enterprise is *named after* sense 4) · Ch 12 §3.0.1 (**three collisions**: Hindu *dharma* shares the cosmic-law sense but is permanent and normative; Jain *dharma-dravya* shares **only the name** — a NOT-equivalent edge; and the general lesson that shared etymology guarantees shared history, not shared referent) · Ch 09 (dharma-dravya) · Ch 05 (dharma/dhamma in the pramāṇa vocabulary) |
| navya-nyaya | Ch 38 | Ch 38 §2 (**three rival beginnings** — with Gaṅgeśa's book c. 1325, with Udayana c. 1025–1100, or with the 11th–12th-c. Nyāya/Vaiśeṣika merger; they answer different questions, and readings 2 and 3 converge on the 11th c. from independent criteria) · Ch 38 §2 (⚠ **the correction to `anandabodha.md`** — its charge of anachronism was itself resting on an unexamined periodisation) · Ch 38 §3 (**what was new was apparatus, not metaphysics**: a diagnostic theory of definition, a seventh category, and a notation) · Ch 38 §7 (the comparison with modern logic, drawn correctly) · Ch 38 §8 (a school that priced itself out) · Ch 16 · Ch 37 §3 — **contested** |
| gangesha | Ch 38 | Ch 38 §5.1 (⚠ **a date drifting one way for a century** — 13th c. in a 19th-c. catalogue, late 12th in a fossilised Wikipedia mirror, c. 1200 in aggregators, 14th c. in current scholarship: **one source at four ages mistaken for corroboration**, and the generalisable lesson that independence must be checked by provenance, not by counting URLs) · Ch 38 §5.1 (the Kālī legend as hagiography — interesting for presupposing that the book's difficulty needed explaining) · Ch 38 §5.2 (⚠ **the Śrīharṣa origin-story is in Wikipedia and absent from SEP's full entry**) · Ch 38 §5.3 (super-reliabilism; *pramāṇābhāsa*; extrinsicality against Mīmāṃsā; the *īśvarānumāna* and its domain restriction) · Ch 39 §2 (M5) — **contested** |
| tattvacintamani | Ch 38 | Ch 38 §5.2 (**three things about its construction** — it takes the *Nyāyasūtra*'s *pramāṇa* and drops *prameya*; its plan is **Dignāga's**, copied; its method is serial demolition) · Ch 38 §5.2 (⚠ SEP says 24 rejected definitions of *vyāpti*, Ganeri 21 rejected + 7 accepted — recorded, not reconciled) · Ch 38 §8.1 (**thirty commentaries in three tiers**, and the live front migrates from tier 1 to tier 2) · Ch 38 §8.1 (⚠ the tier-1 *Anumāna-khaṇḍa* by "Vācaspati Miśra" **independently confirms the I/II collision**) · Ch 38 §7.1 (*vyāpti* as an analysis of the quantifier into co-location and absence) |
| avacchedaka | Ch 38 | Ch 38 §4 (**the limitor** — the one technical term to carry away: *nitambāvacchedena parvate vahniḥ*, and *śākhāvacchedena vṛkṣaḥ kapisaṃyogī, na tu mūlāvacchedena*) · Ch 38 §4.1 (⚠ **the ancestry is grammatical, not logical** — Bhartṛhari's *abhivyāpaka*/*aikadeśika* locus, *Vākyapadīya* III with Helārāja; and the corpus has **no node** for the grammatical tradition) · Ch 38 §4.3 (⭐ **five cognitions of one blue cup** — the limitor exists because the analysandum is a **cognition**, not a sentence) · Ch 38 §4.4 (four rival accounts of *avacchedakatva*; Raghunātha favours (i) and (iv)) · Ch 38 §7.3 (**same puzzle as paraconsistency, opposite repair** — non-contradiction preserved, not relaxed) |
| abhava | Ch 38 | Ch 38 §3.2 (⭐ **the seventh category was retrofitted** — Kaṇāda and Praśastapāda did not state it; Śrīdhara and **Udayana in the *Kiraṇāvalī*** argued they approved it *implicitly*; and this vindicates rather than contradicts the corpus's six-*padārtha* Vaiśeṣika files) · Ch 38 §3.2 (⚠ Candramati's *Daśapadārthaśāstra* expressly excepted) · Ch 38 §3.3 (Ingalls's keystone — metaphysics, epistemology **and** logic; and the minority claim, held "against the opposition of all other schools," that one can **see** an absence) · Ch 38 §3.3 (two / four / six kinds; the transient–eternal cut; the Mīmāṃsā objection) · Ch 39 §8 (Jayatīrtha borrows *pratiyogin* + *atyantābhāva*) — **contested** |
| raghunatha-siromani | Ch 38 | Ch 38 §6 (⭐ **the school's best logician rejected the school's ontology** — time, space and *ākāśa* identified with God; *manas* eliminated; **atoms and dyads denied**; *viśeṣa*, the category the school is named after, dismissed as unproven; eight new categories added) · Ch 38 §6 (⚠⚠ **the §0 consequence** — Vaiśeṣika atomism is Kaṇāda's, Praśastapāda's and Udayana's, not "the school's": a doctrine its own leading later thinker discarded on metaphysical grounds is not an empirical discovery being handed forward) · Ch 38 §6 (**he attacks Udayana's universals** — apply the cross-connection criterion consistently and "virtually all universals" go) · Ch 38 §6 (***paryāpti***, the completion relation: "the table has four legs" does not entail "each leg is four") · Ch 38 §4.4 · Ch 16 — **contested** |
| gadadhara | Ch 38 | Ch 38 §8.2 (**the measure of the difficulty** — the *Gādādharī* comments on Raghunātha's *Dīdhiti*, i.e. **tier 2**; and the standard beginners' manual was nicknamed ***Bāla-gādādharī***, "a sort of Beginner's Guide to Gadādhara") · Ch 38 §8.2 (⚠ his two independent treatises, the *Vyutpattivāda* and *Śaktivāda*, are both on **language** — the school that narrowed onto inference produced its last original work on semantics) · Ch 39 §4.3 (⭐ **placing him falsifies a synchronism Batch 45 adopted** — he wrote c. 1640–60, so he cannot be Madhusūdana's contemporary; the likely source is a **panegyric verse** about Navadvīpa logicians trembling) — **contested** |
| jayatirtha | Ch 39 | Ch 39 §8 (⭐ **a Dvaitin defines nonexistence in the Naiyāyika's own words** — "being the counterpositive of a constant absence," i.e. *pratiyogin* + *atyantābhāva*, used against an Advaitin; Ingalls's export observation reached from the other end in the same batch) · Ch 39 §8 (**he structured what Madhva left elliptical** — the arguable form of Dvaita is his) · Ch 39 §8 (⚠ **Williams could not locate B. N. K. Sharma's verse** — what an independent check looks like when it lands) · Ch 39 §7 (**two Vyāsatīrthas** — his hagiographies are ascribed to a "direct disciple" born sixty years after he died) · Ch 36 — **contested** |
| vedanta-desika | Ch 39 | Ch 39 §5.1 (**five lost works survive in his quotations** — Nāthamuni's *Nyāyatattva*, Parāśara Bhaṭṭa, Rāmamiśra, the Vṛttikāra, Yādavaprakāśa: a commentator who made an archive without meaning to) · Ch 39 §4.2 (⭐ **the lifespans were stretched to connect the teachers** — Freschi citing Neevel 1977, sourcing what `nathamuni.md` had only inferred; and he himself gets ~101 years) · Ch 39 §8 (⚠⚠ **a school partly authored by its systematiser** — "would probably not have appeared such to the school's contemporaries"; he fixed Rāmānuja as the reference point, and `vishishtadvaita.md` is annotated accordingly) · Ch 39 §8 (**he criticised Yāmuna** for proving God by inference — a methodological reversal inside a supposedly smooth lineage) · Ch 39 §8 (the **Vaṭakalai claimed him retrospectively**; Hayagrīva not Gaṇeśa; the 1676 temple) · Ch 36 — **contested** |
| vimuktatman | Ch 39 | Ch 39 §6.1 (⭐ **the queued test was run and the claim failed** — the Ānandabodha discipleship works on *no* combination of the available datings, and is stated as a **negative** result) · Ch 39 §6.1 (⚠ **the transferable method note** — the claim named a site that, read directly, makes no such claim: *an aggregator's attribution to a site is not the site's claim*) · Ch 39 §6.2 (**a source contradicting itself in one article** — "c. 1200" in the prose, "10th century" in its own chronology; M5) · Ch 39 §9 (⚠ Hiriyanna's 1933 edition **pursued and unreadable**) · Ch 11 (one of the four traditional *siddhi*s — all four authors now in the corpus) — **contested** |
| tisata | Ch 39 | Ch 39 §3.1 (⭐ **M1, the blank filled with a celebrity** — the *Cikitsākalikā*'s opening verse praises his father **and does not name him**, and colophons later supply "Vāgbhaṭa") · Ch 39 §3.2 (**the other half of `candrata.md`'s Batch 45 finding** — one genealogical claim asserted at two generations) · Ch 39 §3.2 (⚠ Vāgbhaṭa "conspicuously absent" from his own authority-list — an argument from silence, labelled) · Ch 39 §5.2 (**ordinal evidence at two removes** — his terminus ad quem is Niścalakara's remark about Cakrapāṇi's sources, and the 900–1050 narrowing rests on a 16th-c. quotation of a lost commentary) · Ch 35 · Ch 31 |
| niscalakara | Ch 39 | Ch 39 §5.1 (⭐ **a commentary that is a bibliography** — ~50 of Cakrapāṇi's sources identified, many otherwise lost; the same shape as Veṅkaṭanātha in a different literature and the same batch) · Ch 39 §3.3 (**the blank nobody filled** — he quotes his *guru* constantly and never names him; P. V. Sharma's filling declined) · Ch 39 §5.3 (**M4, respect read as lineage** — *āyurvedaguru*; and Vijayarakṣita's whole date hangs on him, five scholars across four centuries) · Ch 39 §5.3 (⚠ P. V. Sharma's two published positions — the corpus's second such case) · Ch 35 — **contested** |
| vrnda | Ch 39 | Ch 39 §6.3 (⭐ **M6, the external anchor that evaporates** — al-Yaʿqūbī's reference "proves to be Ravigupta's *Siddhasāra*": the one chance to date him from outside the tradition is about a different book) · Ch 39 §7 (⚠⚠ **the counter-case** — P. V. Sharma's proposed split into two Vṛndas, declined by Meulenbeld: the chapter's pattern is a reason to **check**, not a licence to **split**) · Ch 39 §6.4 (**Hoernle's misattribution and its one-clause cause**, plus the handle: the *Siddhayoga* is also called the *Vṛndamādhava*) · Ch 39 §5.2 (Candraṭa's lost *Vṛndaṭīkā* is the conditional that tightens Tīsaṭa's date) · Ch 35 — **contested** |
| vyakarana | Ch 40 | Ch 40 §1 (**a conservative science** — *vi-ā-√kṛ*, "to take apart"; a vedāṅga whose stated motive is to "prevent sloppy usage and transmission," not to discover) · Ch 40 §1.1 (**ten lost predecessors**, and Indra supplied as a founder where the record has none) · Ch 40 §2 (the *munitraya*, both of Abhyankar's senses — incl. the text identified with its commentators) · Ch 41 §1 (⭐ **the three-way split on whether it is a *darśana***, and why the folder placement is the argument) — **contested** |
| panini | Ch 40 | Ch 40 §3 (⭐ **a date that moved 350 years**, and drifted with the KIND of evidence — linguistic impression vs. datable coins) · Ch 40 §3.1 (*yavanānī* and the Achaemenid setting, both recorded as NOT decisive) · Ch 40 §3.2 (the corpus checking itself against `gangesha`) · Ch 40 §8.1 (**states operations, not definitions** — three times in his own text) — **contested** |
| astadhyayi | Ch 40 | Ch 40 §4.1 (⭐ **five sūtra counts** for the best-transmitted text in antiquity — the boundary is a judgement, not an observation) · Ch 40 §4.2 (*anubandha*/*it* — **a real metalanguage**, stated without modern comparison) · Ch 40 §4.3 (⭐ *pratyāhāra* — the most famous device, which Pāṇini never names or defines) · Ch 40 §9 (**the prime-directive section** — Post/BNF/Turing/Chomsky, and Cardona's brake) — **contested** |
| karaka | Ch 40 | Ch 40 §5 (⭐ **meaning → role → ending** — six kārakas, seven vibhaktis, and a mediating level of representation; plus the *kāraka*/*upapada* priority rule) · Ch 40 §8.1 (A 1.4.23 is a HEADING — *kriyānvayitvaṃ kārakatvam* is the commentators') · Ch 40 §9 (the live "Pāṇinian Grammar Framework," and why NO edge was drawn) |
| katyayana | Ch 40 | Ch 40 §6.1 (⭐ **a corpus whose size depends on an 18th-c. definition** — 5000 v. 1400 on Nāgeśa's, and manuscripts that give the reduced number) · Ch 40 §2.2 (survives only inside his own commentator) · Ch 40 §8.3 (⭐ **the Vararuci identification, and a specialist lexicon holding both sides in two entries**) · Ch 40 §7 (Gārgya and Śākaṭāyana as the shared pre-Pāṇinian milieu) — **contested** |
| patanjali-grammarian | Ch 40 | Ch 40 §6.2 (⭐ **the commentator dated better than his author** — mid-2nd c. BCE, triply attested, against Pāṇini's open 350 years) · Ch 40 §2 (third of the *munitraya*, and by Kaiyaṭa's maxim its highest authority) · Ch 41 §2.1 (the first technical use of *sphoṭa*) — and see `patanjali.md` for the T1 split from the Yoga-sūtra compiler |
| mahabhashya | Ch 40 | Ch 40 §6.3 (⭐ **the Great Commentary covers 31% of its own text** — selectivity is the genre) · Ch 40 §6.4 (⭐ **five tiers**, and §2.1's maxim making the climb respectable) · Ch 41 §2.1 (*sphoṭa*/*dhvani* introduced here) · Ch 41 §4 (*abhihitānvaya* — the position Bhartṛhari rejects) · Ch 41 §3.1 (the śabda-as-Brahman lead, Āhnika 2) |
| nirukta | Ch 40 | Ch 40 §7 (⭐ **Kautsa: the Vedic mantras are MEANINGLESS** — an attack on the premise of the whole vedāṅga programme; ⚠ Yāska's answer was not read) · Ch 40 §7 (Śākaṭāyana v. Gārgya on nouns from verbs — and Gārgya's objection is the better argument) · Ch 40 §7.1 (⚠ the grammarians' *dravya* is NOT Vaiśeṣika's) — **contested** |
| bhartrhari | Ch 41 | Ch 41 §1 (⭐ **a promotion claimed, not granted** — he *argues* grammar into a darśana) · Ch 41 §1.2 (⭐ **four sources, four centuries**, and a witness wrong about his religion) · Ch 41 §4 (**against his own tradition** — rejects the *munitraya*'s *abhihitānvaya*; *kalpita*, *pratibhā*) · Ch 40 §8.2 (the source-weighting lesson his date forced) — **contested** |
| vakyapadiya | Ch 41 | Ch 41 §1.1 (⭐ **a book about words structured as a book about what there is** — kāṇḍa III's samuddeśas are the Vaiśeṣika category list) · Ch 41 §6 (⚠ **the 635-verse count challenged, not repeated**; and the *Mahābhāṣyadīpikā*'s single manuscript) · Ch 41 §6 (Helārāja as the route by which the corpus reached the grammarians) — **contested** |
| sphota | Ch 41 | Ch 41 §2.1 (⭐ **four origins that dissolve** — the name, the term, the doctrine, the generalisation) · Ch 41 §2.2 (⭐⭐ **two mechanisms manufacturing an antiquity** — Haradatta's nickname-etymology, and the Prātiśākhya COMMENTATORS retrojecting a word the texts lack) · Ch 41 §2.3 ("the grammarians hold the sphoṭa theory" is true and nearly useless) — **contested** |
| sabdabrahman | Ch 41 | Ch 41 §3 (⭐ ***pariṇāma*, not *vivarta*** — two monisms that disagree about whether the world happened; and the partial Sāṃkhya alignment) · Ch 41 §3.1 (the Mahābhāṣya anchor, recorded and NOT cashed) · Ch 41 §5 (⚠⚠ **the corpus's most inflatable claim** — four stated limits, and no physics edge drawn) — **contested** |
| kaiyata | Ch 42 | Ch 42 §2.1 (⭐ **the maxim verified at first hand** — *Pradīpa* on M.Bh. on P. 1.1.29, Vol. I: 217, closing a Batch 47 follow-up) · Ch 42 §2.2 (⭐⭐ **and bounded**: it "effectively peaks in Patañjali," so it stops one tier below its own author — correcting Ch 40 §2.2) · Ch 42 §2.4 (Deshpande: the ranking may be downstream of which incarnation myth reached Kashmir) · Ch 42 §3 (⚠ his date behaving exactly as Batch 47's source-caution predicted) — **contested** |
| kasika | Ch 42 | Ch 42 §1.1 (⭐ **the only full commentary on Pāṇini is a beginners' gloss**, where the authoritative one covers 31%) · Ch 42 §4 (half of the pair whose practice fixes the received count at 3,983) · Ch 42 §8 (⚠ dated "c. 7th century" with no evidence given anywhere) · Ch 42 §11 (⚠⚠ the Yijing problem: one witness rejected for Bhartṛhari, relied on for Jayāditya) — **contested** |
| bhattoji-dikshita | Ch 42 | Ch 42 §5 (⭐ **the order Sanskrit grammar is taught in is not Pāṇini's** — and the rationale, sourced not inferred) · Ch 42 §4 (the other half of the canon-fixing pair) · Ch 42 §5.3 (the *Prauḍhamanoramā*, a self-commentary read only to the Kāraka-prakaraṇa) · Ch 42 §8 (⚠ a general source putting him in 1700–1800) — **converged** |
| nagesha-bhatta | Ch 42 | Ch 42 §5.1 (⭐⭐ **resizing a canon by reclassifying genre** — Kātyāyana from ~5,000 to ~1,400, and into the manuscripts) · Ch 42 §2.3 (⭐ his empirical gloss on Kaiyaṭa's maxim proves too much — by his own reason he should outrank Patañjali) · Ch 42 §1 (tier 5, and a sixth tier built by his pupil in one generation) · Ch 42 §8.1 (⚠ the appositive that turned a teaching lineage into a bloodline) — **contested** |
| kaundabhatta | Ch 43 | Ch 43 §2 (⭐ Abhyankar ranks the *Bhūṣaṇasāra* **next to the *Vākyapadīya***, twelve centuries later with nothing named between) · Ch 43 §2.1 (⭐⭐ **the traffic reverses** — grammar restates its semantics in Navya-Nyāya's idiom, five centuries after supplying its central device) · Ch 43 §2.2 (the school that was a household) · Ch 43 §2.3 (⚠ two *Sphoṭavāda*s — the eighth flagged collision, and the first from a doctrine-name) — **converged** |
| vararuci | Ch 42 | Ch 42 §6 (⭐ **four men under one name**, numbered by Abhyankar himself — and the entry is an argument, not a self-contradiction, correcting Ch 40 §8.3) · Ch 42 §6.1 (⭐ **the mechanism**: a personal name and a *gotra* name colliding twice, needing no motive at all) · Ch 42 §6.2 (the rival grammars the corpus has no nodes for) — **contested** |
| pratyahara | Ch 42 | Ch 42 §9 (⚠ **the prime-directive section** — Petersen's Proposition 4.2, the 249 K5-triples forcing the doubled *h*, and **four limits in the author's own words**, including that "optimal" does NOT mean shortest) · Ch 42 §9 (⭐ Kiparsky reaching the same result from inside Pāṇini's own economy principle) · Ch 40 §4.3 (the device Pāṇini uses constantly, names never, defines never) — **converged** |
| yaska | Ch 42 | Ch 42 §7 (⭐⭐ **Kautsa's six objections and Yāska's six replies**, read in Sarup's translation — closing the Ch 40 §7 gap) · Ch 42 §7.2 (⭐ **four of six replies work by exhibiting the same feature in ordinary speech** — scripture defended by assimilation, not exaltation) · Ch 42 §7.3 (⚠ the corpus qualifying Sarup: reply 6 is not an argument, and it answers the hapax objection) · Ch 42 §7.4 (the survival of the attack is itself the evidence) — **contested** |
| helaraja | Ch 43 | Ch 43 §1.1 (⭐ **reachable after all** — an open-access critical edition where the queue expected `blocked`; a D1 result) · Ch 43 §1.2 (⭐⭐ **five synonyms read as five schools**, two of them absent from listings of Bhartṛhari's own time) · Ch 43 §1.3 (⚠ **the caveat this puts on Ch 38 §4.1** — the edge stands, but the corpus has not seen those verses without his gloss) · Ch 43 §1.4 (the mechanism is invisible, not corrupting) — **contested** |
| sphotasiddhi | Ch 43 | Ch 43 §3 (⭐⭐ **refuting his own teacher** — Kumārila's case quoted from the *Ślokavārttika* and defeated with Bhartṛhari's) · Ch 43 §3.1 (⭐ a **polemic** preserving its opponent, where Ch 40 §6 had a commentary preserving its root text) · Ch 43 §3.2 (⚠ no line of the argument read — and Ch 42 §8.2 on the follow-up that falsely reported it missing) — **converged** |
| katantra | Ch 44 | Ch 44 §1 (⭐ **the batch's premise corrected**: it did not lose — it won classrooms while Pāṇini won prestige) · Ch 44 §2 (1,412 sūtras, four adhyāyas, an order that is **not** Pāṇini's) · Ch 44 §2.1 (⭐ Pāṇinian in substance, **pre-Pāṇinian in form**) · Ch 44 §2.2 (⚠ the legend and the book specify the same object — recorded as a fit, both readings refused) · Ch 44 §3 (⚠⚠ **the corpus's own error, in full**) · Ch 44 §6.1 (the divine warrant, and the seniority the corpus had assumed without checking) — **contested** |
| sarvavarman | Ch 44 | Ch 44 §2.2 (the six-month wager, and the design brief) · Ch 44 §6 (a **layman** teaching a king) · Ch 44 §6.1 (⭐ the god names the grammar, read at the primary level in Tawney) · Ch 45 §5 (the Kāśmīra thread) — ⚠ **the evidential circle: the sole witness to his date is a text whose own existence that same episode explains** (concept file, not a chapter §) — **contested**, `low` |
| candra-vyakarana | Ch 44 | Ch 44 §3.2 (⭐⭐⭐ **Timalsina: eight chapters, not six — a transmission accident read as an authorial choice**) · Ch 44 §3.3 (what survives of the generalisation) · Ch 44 §4 (the terminal module) · Ch 44 §5 (⭐⭐ **rewriting the root text instead of ranking the commentators**) · Ch 44 §5.1 (it arrived with its own commentary) — **contested** |
| candragomin | Ch 44 | Ch 44 §5 (the Buddhist grammar and its author) · Ch 44 §6 (an *upāsaka* — a layman) · Ch 45 §7 (⭐⭐ **Tatz splits him; Wikipedia merges him and drops the grammar entirely** — and the split is visible inside the Tibetan historiography, Tāranātha against Butön) — **contested** |
| prakrta-prakasha | Ch 44 | Ch 44 §4 (⭐ the third terminal module — **accreted**, 8 chapters to 12) · Ch 44 §8 (the corpus's first Prākṛt-grammar node) · Ch 44 §8.1 (⚠⚠ **the Paiśācī resonance, recorded and refused** — manufactured entirely by the Vararuci name-collision) · Ch 44 §9 (Cowell 1854) — **contested** |
| paribhasha | Ch 44 | Ch 44 §7 (⭐⭐ **T4: nine systems, fifteen collections, 500+ maxims, many word-for-word shared — at the level where grammar reasons about itself there was one discipline**) · Ch 44 §7.1 (watching one maxim travel, with the numbers) · Ch 44 §7.2 (⭐ *jñāpaka* — a shared **method**, and the reading-out-of-features move **institutionalised**) · Ch 44 §7.3 (⭐ it leaves grammar: Indu's 119 āyurvedic *paribhāṣā* verses) — **converged** |
| jinendrabuddhi | Ch 45 | Ch 45 §3 (⭐⭐ **the collision was inside this corpus** — `kasika`/`panini` held the grammarian, `pramana-samuccaya` held Dignāga's commentator) · Ch 45 §3.1 (Kobayashi 1977 against; Hayes 1983, Funayama 1999, Steinkellner 2005 for) · Ch 45 §3.2 (⭐ **the rule sharpened, not broken**: distrust identifications that rest on the **name alone**) · Ch 45 §3.3 (the same apparatus preserving and inventing) — **contested** |
| nyasa-vyakarana | Ch 45 | Ch 45 §1.1 (⭐⭐⭐ **"Manuscripts in India last no more than about five hundred years"** — the commentary is the older witness) · Ch 45 §1.2 (⚠ **Batch 48's caveat relocated, not withdrawn**) · Ch 45 §1.3 (the Kāśikā edited from nine manuscripts of 200+) · Ch 45 §2 (⭐⭐ **a manuscript's silence is evidence; a commentary's silence is nothing**) · Ch 45 §6 (*Nyāsa* is a **genre**, across five systems) · Ch 45 §8 (⚠ the OCR misattribution, caught and corrected) — **converged** |
| haradatta | Ch 45 | Ch 45 §4 (⭐⭐ **Pāṇinian grammar had regions** — eastern, southern, Benares — and the Benares school took the southern commentary) · Ch 45 §4.1 (⚠ **the theological inference refused**, with four candidate explanations and no verdict) · Ch 45 §4.2 (⭐ the other half of Ch 42 §2.4's contrast — and **T3 not discharged**) · Ch 45 §4.3 (⚠ a date that will not settle, and the outlier is the party with the best reason to be right) · Ch 45 §6.1 (collision candidate #12, undiagnosed on purpose) — **contested** |
| punyaraja | Ch 45 | Ch 45 §5 (the Candrācārya question **narrowed, not closed**) · Ch 45 §5.1 (⭐⭐ **a Kashmiri question read through a Kashmiri commentator** — §1.2's situation with the interest **named**) · Ch 45 §5.2 (⭐ a **fourth** way a text changes hands: an abridgement that displaced its original and then changed authors) · Ch 45 §7 (⚠ **one man, two names, self-reported** — name-*difference* is equally weak evidence) — **contested** |
