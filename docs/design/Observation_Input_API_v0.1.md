# Observation Input API v0.1

Status: implementation

## Purpose

Provide the smallest input boundary for constructing an `ObservationRecord` from an explicit observation context and an explicit observed value.

## Contract

`observe(context, value, uncertainty, result_id) -> ObservationRecord`

The API performs construction only.

It does not infer personality, hidden intent, select a Protocol, execute Runtime behavior, convert to `EvidenceRecord`, mutate Landscape, or apply slit/lens/interference/distribution semantics.

## Invariants

1. The supplied `ObservationContext` is preserved.
2. The supplied observed value is preserved as-is.
3. The supplied uncertainty is preserved as-is.
4. The resulting `ObservationResult.context_id` equals `ObservationContext.context_id`.
5. `result_id` is explicit; the API does not invent semantic identity.
6. No domain-level conclusion is created by the input boundary.

## Boundary

```text
explicit context + explicit value + explicit uncertainty
                    |
                    v
                 observe()
                    |
                    v
            ObservationRecord
```

This document intentionally does not define the downstream relationship to Runtime Evidence or Landscape.
