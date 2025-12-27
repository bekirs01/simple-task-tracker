import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title})
    save_tasks(tasks)
    return tasks

def list_tasks():
    return load_tasks()

if __name__ == "__main__":
    add_task("Sample task")
    print(list_tasks())
