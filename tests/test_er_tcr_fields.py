import json
import pytest as pytest
import logging

exec_rep_path = "test-exec_report_book_clear.json"
trade_rep_path = "test-post_trade_information.json"
test_fields = ["executed_price", "executed_size", "order_id", "exec_type", "side"]


def is_report_message(message: dict) -> bool:
    # Check if the message does not comply to these formats
    message_formats = [{"date"}, {"routing_seq", "origin", "transact_time"}]

    return set(message.keys()) not in (fields for fields in message_formats)


def open_file(path: str) -> list:
    with open(path) as file:
        message_group = [
            json.loads(line) for line in file if is_report_message(json.loads(line))
        ]

    return message_group


def compare(m1: dict, m2: dict, keys: list) -> dict:
    return {k: (m1[k], m2[k]) for k in keys if m1[k] != m2[k]}


def find_tcr_by_exec_id(er_exec_id, tcrs):
    for tcr in tcrs:
        if tcr["execution_id"] == er_exec_id:
            return tcr


def pair_messages(ers, tcrs):
    message_pairs = []

    for er in ers:
        execution_id = er.get("execution_id")
        matching_tcr = find_tcr_by_exec_id(execution_id, tcrs)
        if matching_tcr:
            dup_exec_id = False
            message_pairs.append((er, matching_tcr, dup_exec_id))
            # Check for duplicate TCR based on execution_id
            dup_exec_id = tcrs.count(matching_tcr) > 1
            if dup_exec_id:
                message_pairs.append((er, matching_tcr, dup_exec_id))
            tcrs.remove(matching_tcr)
        else:
            message_pairs.append((er, None, False))

    for tcr in tcrs:
        message_pairs.append((None, tcr, False))

    return message_pairs


@pytest.mark.parametrize(
    "er, tcr, dup_exec_id",
    pair_messages(open_file(exec_rep_path), open_file(trade_rep_path)),
)
def test_equivalency(er: dict, tcr: dict, dup_exec_id: bool):
    assert er, "ER message unavailable"
    assert tcr, "TCR message unavailable"
    assert not dup_exec_id, "Duplicate 'execution_id' in TCR"

    diff = compare(er, tcr, test_fields)
    for k, (v1, v2) in diff.items():
        logging.error(f"{k}: {v1} | {v2}")
    assert not diff, "Field values don't match"
