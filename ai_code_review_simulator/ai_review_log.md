# AI Review Log - `ai_code_review_simulator/task_filter.py`

This log captures structured inline comments and global architectural feedback generated across three AI review personas (**Security**, **Performance**, and **Maintainability**) for PR: *Add Multi-Criteria Task Filtering and Priority Sorting Feature*.

---

## Inline Comments

- **(line 12)** `[Maintainability]` Replace raw string parameters for `status` (`"todo"`, `"in_progress"`, `"done"`) and `priority` (`"low"`, `"medium"`, `"high"`) with Python `Enum` types (`TaskStatus`, `TaskPriority`) to prevent silent typos and improve IDE autocomplete.
- **(line 15)** `[Security / Data Integrity]` Storing `due_date` as an unvalidated `Optional[str]` allows malformed date strings to enter the domain model; parse into `datetime.date` inside `Task.__init__` or validate against ISO-8601 (`YYYY-MM-DD`) on instantiation.
- **(line 38)** `[Security / Input Validation]` `datetime.strptime(due_before, "%Y-%m-%d")` raises an unhandled `ValueError` if a client passes a malformed date string (e.g., `"2026/11/25"` or `"invalid"`). Wrap parsing in a `try/except ValueError` block and raise a descriptive domain validation error.
- **(line 41)** `[Maintainability]` Add early input validation for the `status` and `priority` filter parameters against the allowed set of values so invalid filter queries fail fast instead of silently returning `[]`.
- **(line 47)** `[Performance]` `query.lower()` is recomputed on every single iteration of the `for task in tasks:` loop. Precompute `normalized_query = query.strip().lower()` once before entering the loop.
- **(line 49)** `[Maintainability / Logic Edge Case]` When `cutoff_date` is provided and `task.due_date` is `None`, tasks with no due date are currently included in urgent deadline results (`if cutoff_date and task.due_date:`). Clarify whether dateless tasks should be excluded (`if cutoff_date and (not task.due_date or task_date > cutoff_date)`).
- **(line 50)** `[Performance]` Calling `datetime.strptime(task.due_date, "%Y-%m-%d")` inside the filter loop repeatedly parses strings for every candidate task. Comparing ISO-8601 `YYYY-MM-DD` strings directly or storing `datetime.date` objects on `Task` eliminates repeated `strptime` overhead.
- **(line 60)** `[Maintainability]` Move the `order = {"high": 1, "medium": 2, "low": 3}` dictionary out of `sort_tasks_by_priority()` into a module-level constant (`PRIORITY_RANK`) so it is not re-allocated on every function call.

---

## Global Feedback

- **[Security Persona] Input Sanitization & Length Limits:** Enforce a maximum length on the `query` search string (e.g., `max_length=100`) and validate all filter arguments at the API boundary before passing them into `filter_tasks()` to prevent abusive payloads.
- **[Performance Persona] Generator Pipeline & Combined Filter/Sort:** Refactor `filter_tasks()` to avoid unnecessary intermediate list allocations when chaining filters, and consider providing a combined `query_tasks(tasks, filters, sort_by)` entry point so callers do not serialize dicts before sorting.
- **[Maintainability Persona] Modular Decomposition & Test Coverage:** Split `filter_tasks()` into smaller single-responsibility predicate helpers (`_matches_status`, `_matches_due_date`, `_matches_query`), extract tests out of `task_filter.py` into a dedicated `tests/test_task_filter.py` `pytest` suite, and add edge-case tests for invalid dates, empty task lists, and `due_date=None` behavior.
