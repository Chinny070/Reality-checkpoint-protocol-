# Security Model

## Assets and actors

Assets are the meaning of a finalized checkpoint, its evidence identity, its validity interval, lineage, and downstream usability. Actors include checkpoint creators, source owners, site operators, leaders, validators, challenge submitters, and consuming contracts.

## Threats

- Prompt injection in retrieved pages.
- A creator choosing redundant or syndicated URLs and claiming corroboration.
- A leader fabricating a well-formed positive result.
- A source changing between validator observations.
- A transport failure being misrepresented as contradiction or support.
- Oversized definitions, dependency cycles, composition depth attacks, duplicate challenges, and stale certificates.
- A transient revalidation failure erasing a previously valid checkpoint.

## Controls

- Fetched page content is data only; prompts explicitly deny it instruction authority.
- Validators independently retrieve/render and classify decision-critical fields.
- Strict schema/enum/ID coverage validation rejects extra, missing, duplicate, and unknown fields.
- Contract-generated IDs/hashes/timestamps and deterministic thresholds stay outside the model boundary.
- Source independence is determined from unique independent cluster IDs, not URL count.
- Opposing findings create a reality fork only when both sides have independent relationships and distinct contract-derived source clusters.
- Evidence receipts are compared by every validator against its own retrieval, including URL, mode, render/content hashes, status, and normalization version.
- Supplemental challenge sources must be available, independently classified, claim-bound, on a new domain cluster, and satisfy the frozen claim floor. Inadmissible submissions create no contract storage and cannot exhaust challenge rounds; every persisted inconclusive challenge attempt consumes one bounded round, whether or not it included an admitted supplemental source.
- Unavailable and inconclusive attempts preserve the prior finalized state.
- Composite and claim graphs are bounded and cycle-checked.
- Challenge rounds, evidence text, definitions, and page responses are bounded. At most three nonfinal challenge receipts can be persisted per checkpoint; rejected supplemental submissions persist nothing.
- Usability is a deterministic view and expires with the certificate.

## Trust limitations

Consensus does not prove that source-owner/syndication classification is perfectly correct. Validators may see different page snapshots; typed semantic disagreement is retained rather than hidden. A checkpoint only certifies its bounded claim definition and source set, at its timestamp and validity window. It does not establish timeless truth.

## Fail-closed policy

Unknown enums, malformed model output, incomplete evidence, insufficient independent clusters, unsupported retrieval modes, stale checkpoints, and material disagreement cannot yield a usable positive certificate. External failure is not a semantic change.
