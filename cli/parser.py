import sys

COMMAND_LENGTH = 3

USAGE = """Usage:
    task-cli add <description>
    task-cli update <id> <new description>
    task-cli delete <id>
    task status <id> (1 -> in-progress, 2 -> done)
    task list <optional status>"""

commands = {
    "add": (1, 1),
    "update": (2, 2),
    "delete": (1, 1),
    "status": (2, 2),
    "list": (0, 1),
}


def parse_command():
    cmd_args = sys.argv[1:]

    if not cmd_args:
        return SystemExit(USAGE)

    command, *argument = cmd_args

    if command not in commands:
        return SystemExit(f"command '{command}' is not a valid command!\n{USAGE}")

    lowest, highest = commands[command]

    if len(argument) < lowest or len(argument) > highest:
        return SystemExit(USAGE)

    return command, argument
