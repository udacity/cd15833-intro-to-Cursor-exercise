"""JSON-backed persistence for expenses."""
from __future__ import annotations

import json
from pathlib import Path

from expense_tracker.models import Expense


class StoreError(Exception):
    """Raised when the data file exists but cannot be read as a valid expense store."""


def load_expenses(path: Path) -> list[Expense]:
    """Load expenses from ``path``."""
    # TODO: Read the file and parse its JSON into a list of Expense objects.
    # TODO (edge cases — handle BOTH, distinctly; they are easy to conflate):
    #   - a MISSING file returns an empty list and does NOT raise;
    #   - a file that exists but is corrupt/not JSON, or is not a JSON array, raises StoreError
    #     with the file path in the message (not a raw traceback).
    raise NotImplementedError


def save_expenses(path: Path, expenses: list[Expense]) -> None:
    """Write ``expenses`` to ``path`` as a JSON array, creating parent directories as needed."""
    # TODO: Serialize each expense with to_dict() and write a JSON array to the file.
    raise NotImplementedError
