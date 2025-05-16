
# TaskCLI

**TaskCLI** is a lightweight, Python-based command-line application that helps you manage your daily tasks efficiently. It supports basic task management operations such as add, update, delete, and list. all through simple commands.

## 🚀 Features

- ✅ Add new tasks with a description
- ✏️ Update existing tasks (description and status)
- ❌ Delete tasks by ID
- 📋 List tasks filtered by status (`todo`, `in-progress`, `done`)
- 🧠 Persists tasks in a local JSON file
- 💡 Easy to extend and customize


## 📦 Installation

Clone the repository and install it locally using `pip`:

```bash
git clone https://github.com/GautamSavsaviya/taskcli.git
cd taskcli
pip install .
```

This will install the `taskcli` command globally within your virtual environment or system Python.


## 🛠️ Usage

```bash
taskcli [command] [options]
```

### Commands:

#### `add`

Add a new task.

```bash
taskcli add "Read documentation"
```

#### `update`

Update a task's description or status.

```bash
taskcli update 1 --description "Read API docs" --status in-progress
```

#### `delete`

Remove a task by its ID.

```bash
taskcli delete 1
```

#### `list`

Display all tasks or filter by status.

```bash
taskcli list --status done
```


## 🗃️ Task Storage Format

All tasks are stored in a local `tasks.json` file in the following format:

```json
{
  "1": {
    "description": "Read documentation",
    "status": "in-progress",
    "created_at": "14/05/2025, 10:23:45",
    "updated_at": "14/05/2025, 10:30:12"
  }
}
```


## 💻 Development

### Project Structure:

```
taskcli/
├── main.py
├── __init__.py
└── utils/
    ├── commands.py
    └── __init__.py
setup.py
```

### To Run Locally:

```bash
python taskcli/main.py [command] [options]
```

Example:

```bash
python taskcli/main.py add "Test CLI"
```


## 🧪 Testing

Manual testing is supported via CLI:

```bash
taskcli add "Sample Task"
taskcli list
taskcli update 1 --status done
taskcli delete 1
```


## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.


## 👤 Author

**Gautam Savsaviya**
GitHub: [@GautamSavsaviya](https://github.com/GautamSavsaviya)

