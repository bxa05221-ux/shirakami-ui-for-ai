# shirakami-ui-for-ai

UI for AI — an implementation project for the boundary between human Landscape and AI interaction.

[日本語 README](README.ja.md)

## Position

`shirakami-OS` is the Runtime foundation.

`shirakami-ui-for-ai` is the human/AI observation boundary that prepares and preserves context before it enters the Runtime.

Conceptual flow:

`Human Landscape → Observation Boundary → Shirakami Runtime → AI Adapter`

## Initial implementation target

The first target is deliberately small:

> Preserve Observation Context without turning an observation into a claim about the person or the world.

The implementation must preserve:

- observation conditions
- observed result
- uncertainty / unresolved state
- lineage needed to pass the observation to the Runtime

## Boundary rules

- Do not invent new Protocol semantics in this repository.
- Formal research handoffs (`的目yaml`) are the source for adopted theory.
- Observation is not truth.
- A single observation is not an essence/personality judgment.
- Unknown context remains unknown.
- AI has no authority to declare domain truth.
- `shirakami-OS` remains the Runtime boundary.

## Development order

1. Observation Boundary Design
2. Minimal observation data structures
3. Tests for condition/result separation
4. Runtime handoff integration
5. Further observation-path / lens work only after formal adoption

## Status

Initial repository. Design-first implementation phase.
