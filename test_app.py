from app import add_task, list_tasks
import os

def test_add_task():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    add_task("Test Task")
    tasks = list_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
