# Source Independence

RCP does not count URLs. Each validator classifies relationships as `INDEPENDENT`, `SAME_OWNER`, `SYNDICATED`, `DERIVATIVE`, `CITES_OTHER`, or `UNKNOWN_RELATIONSHIP`, then assigns a bounded cluster ID. The contract counts unique cluster IDs only among findings classified `INDEPENDENT` and `SUPPORTED`.

Example: five URLs grouped as three syndicated pages under one cluster, one derivative report, and one independent source yield one supported independent cluster—not five.

The relationship classification is a consensus-backed judgment, not perfect ownership graph knowledge or cryptographic proof. Unknown relationships never increase the independent count.
