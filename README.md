# Task Tracker CLI

A simple command-line task tracker built with Python. I created this project to have my own personal to-do list while practicing and improving my Python programming skills.

## About the Project

Task Tracker CLI is a command-line application that allows me to manage my daily tasks directly from the terminal. It helps me keep track of things I need to do, tasks I'm currently working on, and tasks I've already completed.

This is also a learning project where I practice working with command-line arguments, file handling, JSON, and organizing Python code into separate modules.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress
- Mark tasks as done
- List all tasks
- Filter tasks by status:
  - To-do
  - In progress
  - Done
- Automatically save tasks to a JSON file

## Built With

- Python
- JSON
- Python Standard Library

## Project Structure

```text
task-tracker/
│
├── main.py
├── cli/
│   ├── parser.py
│   └── commands.py
├── services/
│   └── task_service.py
├── storage/
│   └── json_storage.py
├── data/
│   └── tasks.json
└── README.md
```

## Usage

Run the application from your terminal using Python.

### Add a task

```bash
python main.py add "Study Python"
```

### Update a task

```bash
python main.py update 1 "Study FastAPI"
```

### Delete a task

```bash
python main.py delete 1
```

### Mark a task as in progress

```bash
python main.py status 1
```

### Mark a task as done

```bash
python main.py status 2
```

### List all tasks

```bash
python main.py list
```

### List tasks by status

```bash
python main.py list done
python main.py list todo
python main.py list in-progress
```

## What I'm Learning

Through this project, I'm practicing:

- Python functions and modules
- Command-line arguments using `sys.argv`
- Reading and writing JSON files
- File and directory handling
- Lists and dictionaries
- Exception handling
- Basic application structure and separation of concerns

## Purpose

I built this project mainly for two reasons:

1. To have a simple personal to-do list that I can use from my terminal.
2. To improve my understanding of Python by building something practical instead of just following tutorials.
