"""Core expense data model."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any


@dataclass(frozen=True)
class Expense:
    """A single recorded expense."""

    # TODO: Define the fields a recorded expense carries, with the types from your blueprint:
    #   amount (Decimal), category (str), description (str), date (datetime.date).

    def to_dict(self) -> dict[str, str]:
        """Serialize to JSON-safe primitives, preserving monetary precision as a string."""
        # TODO: Return a dict of strings — amount and date as strings (never floats) so no
        #       precision is lost — plus category and description.
        raise NotImplementedError

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> Expense:
        """Rebuild an Expense from its serialized form."""
        # TODO: Rebuild an Expense from the dict: amount back to Decimal, date via date.fromisoformat.
        raise NotImplementedError
