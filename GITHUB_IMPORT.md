> **ARCHIVED IMPORT NOTE (2026-11-05):** This procedure describes the original empty-repository setup, already completed. Do **not** rerun `git init` or create a duplicate project. For current work and provenance see [current status](00_governance/CURRENT_SOURCE_AND_STATUS_2026-11-05.md) and [v0.5 preliminary engineering](10_fixture_v0.5/README.md).

# Import this research baseline into a dedicated GitHub repository

**Recommended destination:** `Open-Energy-Methods/electronics-bench-testing` (or the researcher's personal account). Create an empty repository in GitHub first. The available connector could not create a repository automatically.

Copy **the contents of this folder** (not this ZIP itself) into the repository. The repository should contain README.md, EBT_Master_Programme_Plan_v1.0.md, `.github/workflows/ebt-ci.yml`, `00_governance/` and the other research folders at its top level.

Suggested terminal workflow after creating an empty repository, from this extracted folder:

```bash
git init -b main
git add .
git commit -m "research: establish EBT controlled master baseline v1.0"
git remote add origin https://github.com/Open-Energy-Methods/electronics-bench-testing.git
git push -u origin main
```

If GitHub created an initial README/license on the remote, clone that repo first and copy this folder's contents inside it, then commit and push normally to avoid unrelated-history errors. Never use force-push to bypass conflicts.

**Quality / scope:** The existing 7 synthetic-model tests run in CI, but *no physical measurements or calibration* are claimed. The test matrix is provisional; access and safety authorization are required before electrical experiments. `00_governance/RELEASE_MANIFEST_SHA256.json` records the checksums for this import package.

**Excluded to avoid accidental release pollution:** duplicate nested ZIP, Python cache folders and compiled bytecode, and the original generated manifest whose entries referred to files not included in this cleaned import. Original unmodified package ZIP SHA256: `1c3cb87b3fb2e2ef8a5500f9a69d825c63f8506d22fe0216d2457b53d38c9fce`.
