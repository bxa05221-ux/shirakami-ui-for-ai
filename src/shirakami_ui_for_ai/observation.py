"""Minimal observation-boundary data structures.

These structures preserve observation conditions and observed results without
turning them into person-level or domain-level conclusions.
"""

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class ObservationContext:
    """Conditions attached to an observation."""

    context_id: str
    timestamp: str
    source: str
    relation: str
    conditions: Mapping[str, Any]


@dataclass(frozen=True)
class ObservationResult:
    """What was observed under an ObservationContext."""

    result_id: str
    context_id: str
    value: Any
    uncertainty: Any


@dataclass(frozen=True)
class ObservationRecord:
    """A context/result pair kept together at the observation boundary."""

    context: ObservationContext
    result: ObservationResult

    def __post_init__(self) -> None:
        if self.result.context_id != self.context.context_id:
            raise ValueError("ObservationResult.context_id must match ObservationContext.context_id")
