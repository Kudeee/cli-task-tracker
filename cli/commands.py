from services import task_service


def handle_command(command, args):
    if command == "add":
        return task_service.Add_Task(args[0])
    elif command == "update":
        return task_service.update_task(int(args[0]), args[1])
    elif command == "status":
        if int(args[1]) == 1:
            return task_service.update_status(int(args[0]), "in-progress")
        if int(args[1]) == 2:
            return task_service.update_status(int(args[0]), "done")
    elif command == "delete":
        return task_service.delete_task(int(args[0]))
    elif command == "list":
        if not args:
            return task_service.list_tasks()
        else:
            return task_service.list_filtered_tasks(args[0])
