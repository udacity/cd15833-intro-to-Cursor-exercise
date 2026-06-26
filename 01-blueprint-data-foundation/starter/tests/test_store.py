"""Exercise 1 — JSON-backed store."""
from __future__ import annotations

import json
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from expense_tracker.models import Expense
from expense_tracker.store import StoreError, load_expenses, save_expenses


def _sample() -> Expense:
    return Expense(Decimal("12.50"), "food", "lunch", date(2026, 6, 9))


def test_save_then_load_round_trips(tmp_path: Path) -> None:
    path = tmp_path / "expenses.json"
    expenses = [_sample(), Expense(Decimal("4.00"), "coffee", "latte", date(2026, 6, 10))]
    save_expenses(path, expenses)
    assert load_expenses(path) == expenses


def test_saved_file_is_valid_json_array(tmp_path: Path) -> None:
    path = tmp_path / "expenses.json"
    save_expenses(path, [_sample()])
    parsed = json.loads(path.read_text())
    assert isinstance(parsed, list)
    assert parsed[0]["category"] == "food"


def test_load_missing_file_returns_empty_list(tmp_path: Path) -> None:
    assert load_expenses(tmp_path / "does-not-exist.json") == []


def test_load_corrupt_file_raises_store_error(tmp_path: Path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text("{ this is not valid json ]")
    with pytest.raises(StoreError) as excinfo:
        load_expenses(path)
    assert str(path) in str(excinfo.value)


def test_load_non_array_json_raises_store_error(tmp_path: Path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text('{"amount": "1.00"}')  # object, not the expected array
    with pytest.raises(StoreError):
        load_expenses(path)
