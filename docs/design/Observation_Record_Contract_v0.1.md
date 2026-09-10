# Observation Record Contract v0.1

Status: implementation design

## Purpose

Define the currently implemented observation-boundary structure without extending its semantic meaning.

## Structure

```text
ObservationRecord
├── context: ObservationContext
│   ├── context_id
│   ├── timestamp
│   ├── source
│   ├── relation
│   └── conditions
│
└── result: ObservationResult
    ├── result_id
    ├── context_id
    ├── value
    └── uncertainty
```

## Invariants

1. `ObservationRecord` contains one `ObservationContext` and one `ObservationResult`.
2. `ObservationResult.context_id` must equal `ObservationContext.context_id`.
3. Observation conditions are retained separately from the observed result.
4. Uncertainty is retained as supplied.
5. The structure contains no required field for personality, hidden intent, domain truth, or semantic conclusion.
6. Different contexts remain representable as different records.

## Boundary

This contract stops at the observation boundary.

It does not define:

- Protocol selection
- Runtime execution
- EvidenceRecord conversion
- Landscape mutation
- Slit/lens semantics
- Interference semantics
- Distribution interpretation

Those require separate adopted contracts.

## Implementation note

The current Python implementation uses frozen dataclasses. This provides object-level assignment protection but does not, by itself, make every nested value immutable. No stronger immutability guarantee is claimed by this contract.
