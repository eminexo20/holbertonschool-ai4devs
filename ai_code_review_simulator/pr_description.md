# Pull Request: Add Multi-Criteria Task Filtering and Priority Sorting Feature

## Summary
Implements multi-criteria task filtering (`status`, `priority`, `due_before`, `assignee`, and keyword search) along with priority-based sorting to support the `/tasks/filter` workflow.

## Changes
- Added `Task` domain model with `to_dict()` serialization helper in `task_filter.py`
- Implemented `filter_tasks()` supporting status, priority, due-date cutoff (`YYYY-MM-DD`), assignee, and case-insensitive title search
- Implemented `sort_tasks_by_priority()` to order filtered results (`high` -> `medium` -> `low`)
- Added 5 unit tests in `run_tests()` verifying single-filter, multi-filter, date-boundary, keyword, and sorting behavior

## Context
~125 LOC. Related issue: #42. Enables team members to quickly isolate high-priority and upcoming deadline tasks without scanning the full backlog.
