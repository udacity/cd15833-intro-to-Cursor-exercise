"""JSON-backed persistence for expenses."""
from __future__ import annotations

import json
from pathlib import Path

from expense_tracker.models import Expense


class StoreError(Exception):
    """Raised when the data file exists but cannot be read as a valid expense store."""


def load_expenses(path: Path) -> list[Expense]:
    """Load expenses from ``path``.

    A missing file is treated as an empty store. A file that exists but does not contain a
    JSON array of expense objects raises :class:`StoreError` with a human-readable message.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []

    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        raise StoreError(f"{path} is not valid JSON: {exc}") from exc

    if not isinstance(raw, list):
        raise StoreError(f"{path} must contain a JSON array of expenses, got {type(raw).__name__}")

    try:
        return [Expense.from_dict(item) for item in raw]
    except (KeyError, ValueError, TypeError) as exc:
        raise StoreError(f"{path} contains a malformed expense record: {exc}") from exc


def save_expenses(path: Path, expenses: list[Expense]) -> None:
    """Write ``expenses`` to ``path`` as a JSON array, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [expense.to_dict() for expense in expenses]
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
