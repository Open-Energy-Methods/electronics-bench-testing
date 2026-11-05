# EBT-PUB-011 — Publication, archive and communication plan (WP8/9)

**Not yet eligible for a physical-results release.** Current outputs are a controlled research programme and synthetic numerical engineering artifacts. No peer-review, physical measurements, KTH institutional sponsorship or accreditation has occurred.

## Planned publication evidence ladder

**Path A — experimental research article** only after G1 novelty framing and G2–G5 real data/uncertainty/held-out prediction evidence. Manuscript core: question/novelty; source-graded related work; experimental fixture and site authority (disclose only nonrestricted details); instrument references; protocol and independent HOLD; equations/B0–B3; observed outcomes and negative cases; reproducible error/uncertainty and discussion.

**Path B — open methods/benchmark paper** if high-quality independent physical data exist but algorithmic novelty is limited. Prioritize publicly reproducible calibration and boundary-transfer dataset with data dictionary, stable units, real remount IDs, uncertainty, abort traces and justified sensor choices.

**Path C — technical report / numerical benchmark** if no authorized lab or scientifically adequate metrology exists. Publish *simulation-labeled* results and transparent reproducibility with no measured response, effective boundary coefficient or clinical/compliance-style claim. A technical report is an acceptable programme outcome, not a failed experimental paper disguised as one.

A journal/conference venue must be chosen only after the data maturity and paper contribution are established. arXiv category, eligibility, endorsement, journal scope, fees and author instructions should be checked when a complete manuscript exists. Depositing to Zenodo may provide a DOI but is **not peer review**.

## Pre-release audit

1. **Rights:** confirm explicit site/data/photo and manufacturer artwork reuse permissions. Use own recreated figures where permission is absent; never publish restricted reference certificates, ID records or site diagrams without permission.
2. **Data labels:** physical raw in immutable source directory distinct from synthetic and numerical. Keep aborts, QC, acquisition/clock and raw-to-processed manifest; no representative fake observations.
3. **Computational reproduction:** clean checkout at fixed commit and environment rebuilds all tables/figures from openly available authorized inputs; automated hashes and numerical verification retained; independent reproduction attempted where feasible.
4. **Research record:** exact study registration and amendments, no HOLD leakage, metrology and uncertainty budget, null and failed conditions, limitations and role of qualified reviewers.
5. **Authorship/affiliations:** independent by default. Any future KTH researcher/coauthor/acknowledgement and data-sharing terms agreed and supported by actual contributions; no implied sponsorship.
6. **Metadata:** GitHub tagged release version, CITATION.cff, ORCID, authors, licenses for code/data/hardware separately, repository source commit, changelog, Zenodo/OA metadata. Add a DOI only after an actual deposit and confirmed identifier.
7. **Outputs:** publication-ready research manuscript or technical report; supplementary code and raw/processed reproducibility pack; thesis-level technical portfolio case study; concise media post that identifies what was **measured**, **numerically simulated** and **not verified**.

## G6 decision

Write a signed release-readiness review against [original checklist](../../05_publication/release_checklist.md), with evidence citations/links and an explicit **experimental article / benchmark / technical report** disposition. No release gate is automatically satisfied by a successful GitHub CI build.
