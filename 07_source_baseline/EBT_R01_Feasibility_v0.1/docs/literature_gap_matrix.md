# Literature screening — EBT-R01 (v0.1, 2026-11-05)

**Status:** targeted scoping review, NOT a systematic literature review. The evidence below is based on the publisher/author abstracts or institutional records; full-text extraction and citation screening remain open. We make no confirmed novelty claim.

| Work | Verified scholarly scope | Relationship to EBT-R01 | Novelty implication |
|---|---|---|---|
| Putthong, Lu & Lee, 2026, *Efficient Experimental Design Framework for Reliable Parameter Identification of Electro-Thermal Models*, PERA Transactions, DOI: [10.53941/perat.2026.100014](https://doi.org/10.53941/perat.2026.100014) | Information-sufficiency criterion, SVD of thermal sensitivities, guided versus unguided experiment selection and out-of-sample comparisons for four MOSFETs | Direct overlap with experiment design, identifiability and external prediction | **Cannot claim novel use of SVD, DoE or prediction transfer generally.** |
| Schulz, Strössner & Grötzbach, 2026, *Identifiability of Cauer thermal networks*, accepted IEEE TPEL (author summary: [link](https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/)) | Profile likelihood to identify resolvable Cauer layers from thermal impedance; synthetic and measured validation | Direct overlap with thermal parameter identifiability | **Cannot claim to discover Cauer network non-identifiability.** |
| Zhang et al., 2024, *A Sparsity-Promoting Time Domain Evaluation Method for Thermal Transient Measurement of Power Semiconductors*, IEEE TPEL 39(6), DOI: [10.1109/TPEL.2024.3367854](https://doi.org/10.1109/TPEL.2024.3367854) | Regularized thermal transient time-domain parameter estimation, simulated benchmarks and device proof-of-concept | Prior art for robust fitting, model selection and noise sensitivity | **Cannot claim novel regularized extraction.** |
| Ress et al., 2026, *Improved Thermal Transient Testing of Wide Bandgap Devices with Extremely Low Channel Resistance*, Energies 19(11), DOI: [10.3390/en19112678](https://doi.org/10.3390/en19112678) | Recent thermal transient measurement advances for wide-bandgap devices | Relevant to junction-temperature observability and measurement electronics | Review full methods before designing TSEP or device transient measurements. |
| Bhadoria, 2025, *Enabling Short-term Over-current Capability for SiC Power Modules and its Application for Power Flow Controllers in HVDC Grids*, KTH doctoral thesis [institutional record](https://kth.diva-portal.org/smash/person.jsf?pid=authority-person%3A105216) | Device cooling, short overcurrent and SiC thermal response, including microchannels | Strong KTH semiconductor/cooling link | Avoid treating cooling comparisons as themselves novel. |
| Cnudde et al., 2026, *Experimental Validation of a Lumped Parameter Thermal Model for Spreading Resistance in Direct-Cooled Power Electronics*, THERMINIC 2026, [Ghent institutional record](https://biblio.ugent.be/publication/01M3C8RKZ0XAPQVC4PAPH2Q791) | Lumped model of spreading resistance validated experimentally | Recent direct competition for model validation work | Need full text and more precise distinction from this paper. |
| JESD51-14 (JEDEC) and transient dual-interface method [method context, IEEE STHERM 2011](https://doi.org/10.1109/STHERM.2011.5767204) | Industry method for measuring junction-to-case thermal resistance of applicable packages | Measurement-method reference, not proof of compliance | Cannot claim JESD51-14 compliance without full applicable method and qualified setup. |

## Research gap hypothesis (NOT established novelty)

A tractable open, low-voltage, independently reproducible comparison could **jointly** examine (a) which temperatures are observable from permitted low-cost sensors; (b) error when moving a compact model between experimentally distinct cooling/interface assemblies; and (c) whether measurement uncertainty and independently characterized boundary conditions suffice to predict unseen conditions. Research novelty could derive from a carefully designed factorial dataset, quantitative decision criteria, or a new method **only after** systematic literature comparison.

## Review needed before academic contact

1. Full-text review of Putthong 2026, Schulz 2026 (if available), Cnudde 2026 and relevant JEDEC methods.
2. Database searches: IEEE Xplore, Scopus, Web of Science, KTH DiVA. Track date, query, inclusion/exclusion rules and backward/forward citation links.
3. Map specific claims: surface-versus-junction observability, transfer under mounting change, heteroscedastic uncertainty, reproducible open datasets, controlled sensor placements.
4. Identify where our target method adds knowledge beyond current open datasets and existing publications.
5. Decide whether aim should be a methodology paper, experimental benchmark/data paper, or qualified engineering report; do not force a research paper if novelty is absent.
