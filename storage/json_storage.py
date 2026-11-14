import json
from pathlib import Path

file_path = Path("./data/tasks.json")


def get_tasks():
    try:
        with file_path.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return "Tasks is empty"


def write(data):
    with file_path.open("w") as file:
        json.dump(data, file, indent=4)
