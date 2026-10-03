# Integration Guide

## Definition wire format

`create_checkpoint` accepts `claims_json` and `sources_json`, each a JSON string bounded to 12 KB. Example:

```json
[{"claim_id":"C1","text":"Public API is operational","criticality":"CRITICAL","required_sources":2,"required_independent_clusters":2}]
```

Each claim may restrict `allowed_retrieval_kinds` to any nonempty subset of `WEB_RENDER_TEXT`, `WEB_RENDER_HTML`, `WEB_GET_TEXT`, `API_JSON`, and `STATIC_DOCUMENT`. If omitted, the full set is allowed. A source kind must be allowed by every claim it is bound to. Source URLs are HTTPS-only and bounded.

```json
[{"source_id":"S1","url":"https://status.example.org","role":"STATUS","retrieval_kind":"WEB_RENDER_TEXT","declared_owner":"Example","claim_ids":["C1"]},{"source_id":"S2","url":"https://independent.example.net/report","role":"CORROBORATING","retrieval_kind":"WEB_GET_TEXT","declared_owner":"Independent publisher","claim_ids":["C1"]}]
```

Create, then call `resolve_checkpoint`. The write result is JSON with the checkpoint ID and receipt ID; inspect the lifecycle/state before treating it as finalized. Read `get_certificate` and `is_checkpoint_usable` before relying on it. `revalidate` is permissionless at any time; callers may use freshness expiry, an observed event, or their own policy as the trigger. `challenge` binds a claim, reason, factual ground, and the required `new_source_json` string (pass `""` when the factual ground is the evidence basis and no source is added). A supplemental source must bind the claim, use a new registrable domain, retrieve successfully, be validator-classified `INDEPENDENT`, and meet the frozen claim floor; otherwise the call returns `PRESERVED_PRIOR` with no stored receipt, successor, or challenge-budget use.

An initial resolution that finalizes as `INCONCLUSIVE` or `UNAVAILABLE` is intentionally terminal for that checkpoint ID. It preserves the failed attempt receipt but cannot be revalidated or challenged because no valid finalized state exists to extend. Create a new checkpoint definition to retry, retaining the old ID as the immutable record of the failed initial attempt.

Pass the contract's JSON parameters as ordinary strings containing JSON when using GenLayerJS. The currently installed GenLayer CLI 0.39.1 parses JSON-shaped `--args` values as typed arrays/objects and has no string escape; `json:` is not supported by its current parser. For reproducible live writes, use [`scripts/live_write.mjs`](../scripts/live_write.mjs), which reads the unlocked signer from the GenLayer CLI OS credential store and loads positional arguments from a JSON array file. Never put a private key in an argument file or shell command. The CLI remains suitable for writes whose arguments are scalar values.

## Public methods

- `create_checkpoint`, `resolve_checkpoint`, `revalidate`, `challenge`, `create_composite`
- `get_checkpoint`, `get_receipt`, `get_certificate`, `get_children`, `is_checkpoint_usable`

Checkpoint and receipt IDs are separate monotonic sequences. JSON output is canonicalized with sorted keys.

## Three consumers

Provider launch gates, milestone settlement, and tool authorization can independently consume the same portable certificate and usability view.

## Local and live test status

Direct Mode contract tests and pure protocol/adversarial helper tests pass locally; exact counts and commands are in `docs/RELEASE_VERIFICATION.md`. They use strict local mocks and do not prove validator consensus. For hosted verification, first deploy to Studionet, then use the installed `genlayer-test` integration interface documented at <https://docs.genlayer.com/api-references/genlayer-test/integration>. Do not represent a local Direct Mode result as a network transaction.
