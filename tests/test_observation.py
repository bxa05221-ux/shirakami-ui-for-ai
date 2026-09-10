from shirakami_ui_for_ai import ObservationContext, ObservationResult, ObservationRecord
import pytest


def make_record(context_id, relation, value):
    context = ObservationContext(
        context_id=context_id,
        timestamp="2026-09-10T00:00:00+09:00",
        source="test",
        relation=relation,
        conditions={"setting": relation},
    )
    result = ObservationResult(
        result_id=f"result-{context_id}",
        context_id=context_id,
        value=value,
        uncertainty=None,
    )
    return ObservationRecord(context=context, result=result)


def test_different_contexts_remain_separate():
    group = make_record("ctx-group", "group", "did not speak")
    one_to_one = make_record("ctx-one-to-one", "one-to-one", "spoke extensively")

    assert group.context.context_id != one_to_one.context.context_id
    assert group.result.context_id == group.context.context_id
    assert one_to_one.result.context_id == one_to_one.context.context_id
    assert group.result.value != one_to_one.result.value


def test_observation_does_not_create_personality_conclusion():
    record = make_record("ctx-1", "group", "did not speak")

    assert record.result.value == "did not speak"
    assert not hasattr(record.result, "personality")
    assert not hasattr(record.result, "intent")


def test_unknown_uncertainty_is_preserved():
    record = ObservationRecord(
        context=ObservationContext(
            context_id="ctx-unknown",
            timestamp="2026-09-10T00:00:00+09:00",
            source="test",
            relation="unknown",
            conditions={},
        ),
        result=ObservationResult(
            result_id="result-unknown",
            context_id="ctx-unknown",
            value="observed value",
            uncertainty="unresolved",
        ),
    )

    assert record.result.uncertainty == "unresolved"


def test_context_result_mismatch_is_rejected():
    context = ObservationContext("ctx-a", "2026-09-10T00:00:00+09:00", "test", "group", {})
    result = ObservationResult("result-b", "ctx-b", "value", None)

    with pytest.raises(ValueError):
        ObservationRecord(context=context, result=result)
