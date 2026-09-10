# R0002 — Observation → Evidence Handoff Boundary

Status: investigation / implementation boundary

## Purpose

Verify the smallest safe boundary between UI for AI observation records and the existing Shirakami Runtime Evidence boundary.

This operation does not define a new Evidence contract.

## Known UI for AI boundary

The repository currently represents an observation as:

```text
ObservationContext
        +
ObservationResult
        ↓
ObservationRecord
```

The Observation Boundary Design requires preservation of observation conditions, observed result, uncertainty / unresolved state, and lineage needed for Runtime handoff.

## Existing Runtime boundary

The current Shirakami Runtime defines `EvidenceRecord` as an immutable record of an observed Runtime transition. Its current fields include:

- `protocol_id`
- `status`
- `transition_kind`
- `transition_data`
- `signals`
- `confidence`

`EvidenceRecord` is constructed from `ExecutionResult`.

## Boundary finding

`ObservationRecord` and `EvidenceRecord` are not currently the same contract.

In particular, the current Runtime Evidence boundary is transition-oriented, while the UI for AI observation boundary is condition/result-oriented.

Therefore this repository must not silently map one structure to the other.

## Allowed implementation direction

A future handoff may introduce an explicit bridge only after the relationship is formally defined.

The bridge must preserve:

```text
Observation conditions
Observation result
Uncertainty / unresolved state
Observation lineage
```

and must not manufacture:

```text
Protocol semantics
Runtime transition data
Domain truth
Personality conclusions
Hidden intent
```

## Current status

BLOCKED on formal contract definition for the Observation → Evidence relationship.

This is an intentional boundary, not an implementation failure.

The existing Shirakami Runtime documentation already identifies the OPPAI Observation → EvidenceRecord relationship as an unresolved contract gap. UI for AI therefore records the same boundary as UNKNOWN rather than inventing a conversion.

## Next safe operation

Define the formal handoff contract in the research project as a `的目yaml` and adopt it here before implementing a conversion or bridge.
