# EBT-LIT-002 · Targeted research-gap assessment (v0.2, 2026-11-05)

**Evidence class: targeted, non-systematic literature screening.** Full-text methods were **not** fully assessed for all records. This document refines the earlier v0.1 matrix, without changing the master research question or asserting novelty. Bibliographic data and links are given for independent checking.

## Questions the prior art forces us to answer

| Prior work | Source-verified scope | What EBT must NOT claim | Differentiation to investigate |
|---|---|---|---|
| Putthong, Lu & Lee (published 13 Oct 2026), DOI [10.53941/perat.2026.100014](https://doi.org/10.53941/perat.2026.100014) | Information-sufficiency criterion, SVD of thermal sensitivities, experiment-selection methodology, four power-controlled MOSFETs, independent predictive assessment. Publisher HTML abstract and reference list verified. | First use of sensitivity/SVD, optimised experimental design, or any prediction holdout in electrothermal modelling. | Boundary-property measurement uncertainty, independent interface remounts and practical transfer across explicitly characterized cooling assemblies. |
| Schulz, Strössner & Grötzbach (2026 accepted), [author record](https://erickschulz.dev/publications/src/data/publications/identifiability-cauer-thermal-networks/) | Profile likelihood and physically resolvable Cauer layers, synthetic and measured work. Author summary only. | Discovery of Cauer identifiability limits or profile likelihood. | Report how actual **sensor locations and boundary characterization** affect predictive validity rather than propose another parameter-identification method. |
| Cnudde et al. (THERMINIC 2026), [UGent record](https://biblio.ugent.be/publication/01M3C8RKZ0XAPQVC4PAPH2Q791) | Direct-cooled electronics, experimentally validated lumped spreading-resistance model; repository record screened. | First experimental validation of a lumped model for electronics cooling. | Emphasize independent remounts, sensor-dependent uncertainty and inaccessible junction conditions. **Full text required**. |
| Bourns PWR220T-20 [datasheet](https://www.bourns.com/docs/product-datasheets/pwr220t-20.pdf) | Nominal 20 W at 25 °C case for properly mounted reference heater; internal thermal specifications. | A heater is a directly measured semiconductor junction or equivalent thermal stack. | A well-defined reference heat-input benchmark for Q0 that independently qualifies the measurement chain. |
| Infineon [MOSFET safety AN](https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf) and Nexperia [AN50006](https://assets.nexperia.com/documents/application-note/AN50006.pdf) | Linear-mode/thermal instability and SOA-dependent stress. | A TO-220 switch can safely dissipate tens of DC watts merely because of nameplate power or current rating. | Gate MOSFET tests separately from resistive Q0; publish practical limitations and SOA methodology if genuinely useful. |

## Candidate scientifically defensible contribution

A **physically measured, openly reproducible benchmark** of *how compact thermal-model predictive performance changes with known versus uncertain cooling boundaries and controlled mounting reassembly*. Analyze uncertainty in accessible package/sink/air temperatures and the extent of identifiability from those signals. Treat the hidden junction temperature as a modeled latent state unless a separate, independently validated junction-sensitive electrical measurement is achieved.

### Publication-tier definitions

- **Tier 0:** synthetic feasibility and pilot instrument qualifications — useful methods note, not validated semiconductor research.
- **Tier 1:** repeatable physical heater benchmark with manufacturer-based limits, uncertainty, independent boundaries and holdouts — potentially methods or dataset paper, not automatically a semiconductor-thermal publication.
- **Tier 2:** MOSFET campaign with independently defended dissipated power and qualified junction-sensitive observations where needed — possible device-level paper if novelty review supports it.

## Provisional preregistration candidates

- Primary response: held-out error distribution for **measured accessible surface temperatures**, defined for each model.
- Core contrast: fixed cooling boundary versus boundary input measured independently *before* target holdout.
- Separate effects: interface treatment and complete assembly remount events, including reproducibility of sensor placement.
- Guard against overfitting: keep model order selection, parameter priors, exclusion logic, uncertainty convention and holdout allocation outside held-out measurements.
- Mandatory negative possibility: if boundary information contributes no statistically or practically meaningful improvement, retain the result.

## Open review work remaining (Gate G1)

1. Retrieve **full text** of Putthong, Schulz (when available) and Cnudde; create a method/measurements/sensor/holdout/uncertainty crosswalk.
2. Query IEEE Xplore, Scopus or Web of Science and KTH DiVA; register search strings, search dates, screening counts and reasons for exclusion.
3. Screen JEDEC JESD51-14 and other relevant measurement standards against actual available junction measurement method; obtain legitimate applicable text where required.
4. Distinguish independently measured boundary inputs from ones estimated using the prospective validation data.
5. Commission an external methods review before promoting a claimed novel contribution.

**No paper, peer review or physical results have yet been produced.** This working review is not a systematic search or a claim of scientific priority.
