import datetime as dt
from zoneinfo import ZoneInfo

from storage import json_storage


def id():
    try:
        task = json_storage.get_tasks()[-1]

        id = task.get("id", 0)  # pyright: ignore[reportAttributeAccessIssue]
        return id + 1
    except IndexError:
        return 1


def list_tasks():
    return json_storage.get_tasks()


def list_filtered_tasks(status):
    tasks = json_storage.get_tasks()
    if status == "todo":
        return [task for task in tasks if task["status"] == "todo"]
    if status == "in-progress":
        return [task for task in tasks if task["status"] == "in-progress"]
    if status == "done":
        return [task for task in tasks if task["status"] == "done"]


def Add_Task(task):
    date_time = dt.datetime.now(ZoneInfo("Asia/Manila"))

    tasks = json_storage.get_tasks()

    task_dict = {
        "id": id(),  # pyright: ignore[reportUnboundVariable]
        "description": task,
        "status": "todo",
        "created_at": date_time.strftime("%I:%M:%S %p, %b %d"),
        "updated_at": "",
    }

    tasks.append(task_dict)

    json_storage.save(tasks)

    return "task is save successfully!"


def update_task(id, description):

    date_time = dt.datetime.now(ZoneInfo("Asia/Manila"))

    tasks = json_storage.get_tasks()

    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updated_at"] = date_time.strftime("%I:%M:%S %p, %b %d")
            break

    json_storage.save(tasks)

    return "task is successfully updated!"


def delete_task(id):
    tasks = json_storage.get_tasks()

    for idx, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(idx)
            break

    json_storage.save(tasks)
    return "task was deleted successfully!"


def update_status(id, status):
    date_time = dt.datetime.now(ZoneInfo("Asia/Manila"))

    tasks = json_storage.get_tasks()

    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updated_at"] = date_time.strftime("%I:%M:%S %p, %b %d")
            break

    json_storage.save(tasks)

    return "task is successfully updated!"
