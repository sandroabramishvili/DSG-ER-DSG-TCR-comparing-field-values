import json
import pytest as pytest
import itertools
import logging

exec_rep_path = 'test-exec_report_book_clear.json'
trade_rep_path = 'test-post_trade_information.json'
test_fields = ['executed_price', 'executed_size', 'order_id', 'exec_type', 'side']

def is_report_message(message: dict) -> bool:
    return 'exec_type' in message

def open_file(path: str) -> list:
    with open(path) as file:
        return [json.loads(line) for line in file if is_report_message(line)]

def compare(m1: dict, m2: dict, keys: list) -> dict:
    return {k:(m1[k],m2[k]) for k in keys if m1[k] != m2[k]}

message_pairs = list(itertools.zip_longest(open_file(exec_rep_path), open_file(trade_rep_path)))

@pytest.mark.parametrize("er, tcr", (message_pairs))
def test_equivalency(er: dict, tcr: dict):
    assert er, ("ER message unavailable")
    assert tcr, ("TCR message unavailable")
    diff = compare(er, tcr, test_fields)
    for k, (v1, v2) in diff.items():
        logging.error(f'{k}: {v1} | {v2}')
    assert not diff, ("Field values don't match")