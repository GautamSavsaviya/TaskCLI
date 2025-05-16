from argparse import ArgumentParser
from typing import Dict
from taskcli.utils.commands import Commands


def get_supported_commands(obj: Commands):
    return {
        "add": {
            "target": obj.add_task,
            "help": "Add new task in your to-do list.",
            "args": [
                {
                    "cmd_arg": ["description"],
                    "help": "Description of the task.",
                }
            ],
        },
        "update": {
            "target": obj.update_task,
            "help": "Update description and status of the task in the to-do list.",
            "args": [
                {
                    "cmd_arg": ["id"],
                    "help": "Task id to update task in to-do list.",
                },
                {
                    "cmd_arg": ["--description", "-D"],
                    "help": "Description of the task to update task in to-do list.",
                },
                {
                    "cmd_arg": ["--status", "-S"],
                    "help": "Update status of the task with choice [todo, in-progress, done] (Default is 'todo').",
                    "choices": ["todo", "in-progress", "done"],
                    "type": str.lower,
                },
            ],
        },
        "delete": {
            "target": obj.delete_task,
            "help": "Delete task from the to-do list.",
            "args": [
                {
                    "cmd_arg": ["id"],
                    "help": "Task id to delete task from to-do list.",
                }
            ],
        },
        "list": {
            "target": obj.list,
            "help": "List the all tasks or  based on your choice of status.",
            "args": [
                {
                    "cmd_arg": ["--status", "-S"],
                    "help": "Filter the task based on the status (Defaullt is 'all').",
                    "choices": ["todo", "in-progress", "done"],
                    "type": str.lower,
                }
            ],
        },
    }


def get_command(supported_commands: Dict[str, Dict]):
    parser = ArgumentParser(description="Task CLI - A Command line todo application.")

    sub_parser = parser.add_subparsers(title="command", dest="command", required=True)

    for name, prop in supported_commands.items():
        p = sub_parser.add_parser(name, help=prop["help"])
        for arg in prop["args"]:
            p.add_argument(*arg.pop("cmd_arg"), **arg)

    args = parser.parse_args().__dict__
    command = supported_commands[args.pop("command")]["target"]

    return command, args


def main():
    cmd_obj = Commands()
    supported_commands = get_supported_commands(cmd_obj)

    command, args = get_command(supported_commands)

    command(**args)
    # print(args)


if __name__ == "__main__":
    main()
