# UI for AI / Runtime Boundary

`shirakami-ui-for-ai` and `shirakami-OS` have separate responsibilities.

## UI for AI

Owns the interaction-side observation boundary:

- receive human-facing interaction context
- preserve observation conditions
- preserve observed results
- keep uncertainty and unknowns explicit
- prepare a handoff to the Runtime

## Shirakami OS

Owns the Runtime foundation:

- Protocol execution
- Evidence handling
- Landscape state
- Runtime boundaries
- Adapter boundary

## Dependency direction

```text
shirakami-ui-for-ai
        ↓
   shirakami-OS
        ↓
    AI Adapter
```

The dependency direction must not be reversed by allowing the Runtime to acquire human-facing semantic authority.

## Design constraint

This document is an implementation boundary, not a new theoretical protocol.

When a required contract is unknown, mark it `UNKNOWN` and return the question to the research side rather than inventing semantics.
