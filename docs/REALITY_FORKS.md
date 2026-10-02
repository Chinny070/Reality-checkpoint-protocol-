# Reality Forks

For each claim, validators classify each associated source independently. If one source supports a claim and another contradicts it, the deterministic contract sets `state_status=DISPUTED` and `divergence_status=CONTRADICTORY_REALITY`, even when the model proposes a softer divergence label. A model-level `CONTRADICTORY_REALITY` label without opposing source findings is rejected and fails closed as `INCONCLUSIVE` / `INSUFFICIENT_EVIDENCE`.

Other typed outcomes include minor/material divergence, insufficient independence/evidence, and external failure. The system never averages opposite claims into positive certainty. Consumers should reject disputed and unavailable certificates unless their own frozen policy explicitly defines another route.
