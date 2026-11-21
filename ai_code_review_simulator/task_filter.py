from datetime import datetime
from typing import List, Dict, Optional


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        status: str,
        priority: str = "medium",
        due_date: Optional[str] = None,
        assignee: Optional[str] = None,
    ):
        self.id = task_id
        self.title = title
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self.assignee = assignee

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date,
            "assignee": self.assignee,
        }


def filter_tasks(
    tasks: List[Task],
    status: Optional[str] = None,
    priority: Optional[str] = None,
    due_before: Optional[str] = None,
    assignee: Optional[str] = None,
    query: str = "",
) -> List[Dict]:
    """Filter tasks by status, priority, due date, assignee, and keyword."""
    results = []
    cutoff_date = None

    if due_before:
        cutoff_date = datetime.strptime(due_before, "%Y-%m-%d")

    for task in tasks:
        if status and task.status != status:
            continue
        if priority and task.priority != priority:
            continue
        if assignee and task.assignee != assignee:
            continue
        if query and query.lower() not in task.title.lower():
            continue
        if cutoff_date and task.due_date:
            task_date = datetime.strptime(task.due_date, "%Y-%m-%d")
            if task_date > cutoff_date:
                continue
        results.append(task.to_dict())

    return results


def sort_tasks_by_priority(tasks: List[Dict]) -> List[Dict]:
    """Sort serialized tasks from highest to lowest priority."""
    order = {"high": 1, "medium": 2, "low": 3}
    return sorted(tasks, key=lambda item: order.get(item.get("priority", "low"), 4))


def run_tests():
    sample_tasks = [
        Task(1, "Implement OAuth login", "in_progress", "high", "2026-11-25", "emin"),
        Task(2, "Fix navbar overflow", "done", "low", "2026-11-18", "asif"),
        Task(3, "Optimize SQL query", "todo", "high", "2026-11-22", "emin"),
        Task(4, "Update API docs", "todo", "medium", "2026-11-30", "zarifa"),
        Task(5, "Refactor auth middleware", "in_progress", "high", None, "emin"),
    ]

    # Test 1: Filter by status
    todo_tasks = filter_tasks(sample_tasks, status="todo")
    assert len(todo_tasks) == 2

    # Test 2: Filter by priority and assignee
    emin_high = filter_tasks(sample_tasks, priority="high", assignee="emin")
    assert len(emin_high) == 3

    # Test 3: Filter by due_before date
    urgent = filter_tasks(sample_tasks, due_before="2026-11-25")
    assert len(urgent) == 3

    # Test 4: Keyword search (case-insensitive)
    auth_tasks = filter_tasks(sample_tasks, query="AUTH")
    assert len(auth_tasks) == 2

    # Test 5: Priority sorting
    sorted_list = sort_tasks_by_priority(todo_tasks)
    assert sorted_list[0]["priority"] == "high"
    assert sorted_list[1]["priority"] == "medium"

    print("All 5 unit tests passed successfully.")


if __name__ == "__main__":
    run_tests()
