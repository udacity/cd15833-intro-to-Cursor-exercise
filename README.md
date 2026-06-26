# Exercise 1 — Blueprint the Data Foundation

You're building a personal expense tracker CLI from scratch. This first slice is the data
foundation: the `Expense` record and the JSON store that saves and loads it. Before you write
code, blueprint the data shape, its constraints, and its edge cases — then build to that blueprint.

## What you'll build
- `expense_tracker/models.py` — the `Expense` dataclass and its `to_dict` / `from_dict` serialization.
- `expense_tracker/store.py` — `load_expenses` / `save_expenses` over a JSON file, plus `StoreError`.

## Where the TODOs are
- `expense_tracker/models.py` — define the `Expense` fields and implement `to_dict` / `from_dict`.
- `expense_tracker/store.py` — implement `load_expenses` / `save_expenses`. Watch the two edge cases
  called out in the TODO: a **missing** file returns `[]`; a **corrupt / non-array** file raises
  `StoreError`. Handle both, distinctly.

## Provided for you
`pyproject.toml`, the package skeleton, the `.cursor/rules/python-cli.mdc` rule file, and the
stage tests (`tests/test_models.py`, `tests/test_store.py`).

## Run / verify
```bash
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest tests/test_models.py tests/test_store.py
```
The exercise is complete when both test files pass.
