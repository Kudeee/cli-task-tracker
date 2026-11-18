from services import task_service


def handle_command(command, id=0, description="", status=0, list_opt=""):
    if command == "add":
        return task_service.Add_Task(description)
    elif command == "update":
        return task_service.update_task(id, description)
    elif command == "status":
        if status == 1:
            return task_service.update_status(id, "in-progress")
        if status == 2:
            return task_service.update_status(id, "done")
    elif command == "delete":
        return task_service.delete_task(id)
    elif command == "list":
        if list_opt == "":
            return task_service.list_tasks()
        else:
            return task_service.list_filtered_tasks(list_opt)
