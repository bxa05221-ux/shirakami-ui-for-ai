# Observation Boundary Design v0.1

Status: design

## Purpose

Define the smallest implementation boundary for UI for AI without introducing new theory.

The boundary preserves the conditions under which an observation occurred and keeps the observation separate from interpretation.

## Boundary

```text
Human Landscape
    ↓
Observation Context
    ↓
Observation Result
    ↓
Evidence handoff
    ↓
Shirakami Runtime
    ↓
AI Adapter
```

## Observation Context

Observation Context describes the conditions attached to an observation.

Initial fields are intentionally minimal:

- `context_id`
- `timestamp`
- `source`
- `relation`
- `conditions`

The implementation must not require inferred personality, intent, emotion, or truth claims.

## Observation Result

Observation Result records what was observed at the boundary.

Initial fields:

- `result_id`
- `context_id`
- `value`
- `uncertainty`

`value` is an observation payload. It is not automatically a semantic conclusion.

## Separation rule

The same apparent behavior under different Observation Contexts must remain representable as separate observations.

Example:

```text
Context A: group
Result A: did not speak

Context B: one-to-one
Result B: spoke extensively
```

The boundary must preserve both records.

It must not collapse them into:

```text
personality = "does not speak in public"
```

## Unknown

If context or meaning is unavailable, it remains unresolved.

The boundary must not manufacture missing context.

## Runtime relationship

This repository prepares the observation boundary.

`shirakami-OS` remains responsible for Runtime behavior, Protocol execution, Evidence handling, and Landscape state according to its adopted contracts.

This document does not redefine those contracts.

## Not yet implemented here

The following concepts are not fixed as implementation contracts by this document:

- `名無し = slit`
- `連山 = lens`
- interference semantics
- distribution semantics
- personality reconstruction
- automatic hidden-intent inference

Those remain research-side concepts until formally adopted through the project's required handoff process.

## Verification target

The first test should establish only this invariant:

> Different Observation Contexts can produce separately preserved Observation Results without being collapsed into a person-level conclusion.
