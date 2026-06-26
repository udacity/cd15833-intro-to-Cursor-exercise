"""Core expense data model."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any


@dataclass(frozen=True)
class Expense:
    """A single recorded expense."""

    amount: Decimal
    category: str
    description: str
    date: date

    def to_dict(self) -> dict[str, str]:
        """Serialize to JSON-safe primitives, preserving monetary precision as a string."""
        return {
            "amount": str(self.amount),
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),
        }

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> Expense:
        """Rebuild an Expense from its serialized form."""
        return cls(
            amount=Decimal(str(raw["amount"])),
            category=str(raw["category"]),
            description=str(raw["description"]),
            date=date.fromisoformat(str(raw["date"])),
        )
