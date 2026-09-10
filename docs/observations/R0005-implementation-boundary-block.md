# R0005 — Implementation Boundary Block

Status: BLOCKED

## Reason

R0004 established and merged the minimal Observation Input API.
No subsequent formal research handoff currently defines the next implementation contract.

## Current verified boundary

- `ObservationContext` preserves observation conditions.
- `ObservationResult` preserves observed value and uncertainty.
- `ObservationRecord` preserves the context/result relationship.
- `observe()` constructs an `ObservationRecord` without inference or interpretation.

## Explicitly not implemented

The following remain outside the implementation boundary until formally adopted through a `的目yaml` research handoff:

- `名無し = slit`
- `連山 = lens`
- interference semantics
- distribution semantics
- 暗問層 semantics
- Observation → Evidence conversion/bridge
- Protocol selection or semantic mapping
- Landscape mutation derived from observations

## Rule

Do not invent a new implementation contract to fill this gap.
When a formal research handoff arrives, implement only the contract it defines.

## Next executable condition

A formal `的目yaml` handoff specifying the next implementation contract is required before R0005 implementation work can begin.
