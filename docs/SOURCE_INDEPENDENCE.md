# Source Independence

RCP does not count URLs. Each validator classifies relationships as `INDEPENDENT`, `SAME_OWNER`, `SYNDICATED`, `DERIVATIVE`, `CITES_OTHER`, or `UNKNOWN_RELATIONSHIP`. The contract derives a stable cluster from the source's registrable domain; model-supplied cluster IDs are ignored, so validators cannot inflate independence by inventing labels. It counts unique domain clusters among informative findings classified `INDEPENDENT`, whether `SUPPORTED` or `CONTRADICTED`. Unknown, unavailable, and relationship-uncertain findings do not count.

Domain clustering is a conservative identity signal, not proof of legal ownership or editorial independence. Validators still classify cross-domain ownership, syndication, derivation, and citations; only independently classified informative observations with distinct domain clusters count toward the floor. Counting contradiction establishes a well-sourced negative finding or source fork; it does not treat contradiction as support. The registrable-domain suffix handling is intentionally bounded and should be updated if source sets rely on suffixes outside the contract's explicit list.

Example: five URLs grouped as three syndicated pages under one cluster, one derivative report, and one independent source yield one supported independent cluster—not five.

The relationship classification is a consensus-backed judgment, not perfect ownership graph knowledge or cryptographic proof. Unknown relationships never increase the independent count.
