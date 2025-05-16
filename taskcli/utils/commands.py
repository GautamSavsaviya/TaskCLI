"""
Storage class to manage task in form of json file.

json structore:
{
    "1": {
        "description: "Temp",
        "status": ["todo", "in-progress", "done"],
        "created_at": datetime.datetime.now().isoformat()
        "updated_at": datetime.datetime.now().isoformat()
    }
}
"""

import json
from tabulate import tabulate
from datetime import datetime
from typing import Literal


class Commands:

    def __init__(self):
        self.__file = "tasks.json"
        self.__tasks = self.__load_tasks()
        self.__id = str(max([0] + [int(id) for id in self.__tasks.keys()]) + 1)

    def __load_tasks(self):
        try:
            with open(self.__file) as f:
                return json.load(f)  # Not json.loads(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def __save_tasks(self):
        with open(self.__file, "w") as f:
            json.dump(self.__tasks, f, indent=4)

    def add_task(self, description: str):
        self.__tasks[self.__id] = {
            "description": description,
            "status": "todo",
            "created_at": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "updated_at": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }

        self.__save_tasks()
        print(f"Task: {description} added.")

    def update_task(self, id: str, description: str = None, status: str = None):
        if not id in self.__tasks:
            print("Error: Invalid task id.")
            return

        if not description and not status:
            print(
                "Error: At least one argument is required from (--description or --mark-status)"
            )
            return

        task = self.__tasks.get(id)
        if description:
            task["description"] = description
        if status:
            task["status"] = status

        task["updated_at"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.__save_tasks()
        print(f"Task updated for id: {id}.")

    def delete_task(self, id: str):
        if not id in self.__tasks:
            print("Error: Invalid task id.")
            return

        self.__tasks.pop(id)
        self.__save_tasks()
        print(f"Task deleted for id: {id}.")

    def list(self, status: Literal["all", "todo", "in-progress", "done"] = None):
        tasks = (
            {
                "Id": id,
                "Task": task["description"],
                "Status": task["status"],
                "Created At": task["created_at"],
                "Updated At": task["updated_at"],
            }
            for id, task in self.__tasks.items()
            if status is None or task["status"] == status
        )

        print(
            tabulate(tasks, headers="keys", tablefmt="rounded_grid")
            or "Nothing to Show."
        )
