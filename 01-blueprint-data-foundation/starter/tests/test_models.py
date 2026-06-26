"""Exercise 1 — Expense data model."""
from __future__ import annotations

from datetime import date
from decimal import Decimal

from expense_tracker.models import Expense


def _sample() -> Expense:
    return Expense(
        amount=Decimal("12.50"),
        category="food",
        description="lunch",
        date=date(2026, 6, 9),
    )


def test_expense_holds_typed_fields() -> None:
    e = _sample()
    assert e.amount == Decimal("12.50")
    assert e.category == "food"
    assert e.description == "lunch"
    assert e.date == date(2026, 6, 9)


def test_expense_round_trips_through_dict_preserving_types() -> None:
    e = _sample()
    restored = Expense.from_dict(e.to_dict())
    assert restored == e
    assert isinstance(restored.amount, Decimal)
    assert isinstance(restored.date, date)


def test_expense_serializes_date_and_amount_as_strings() -> None:
    raw = _sample().to_dict()
    assert raw["date"] == "2026-06-09"
    assert raw["amount"] == "12.50"  # string, not float — no precision loss
