# waldomac00-datafun-02-automation

# datafun-02-project-setup
Utilities for scripting project folders

## Project Requirements

- VS Code
- Git
- Python 

## Professional Python Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux).
Verify that all required packages are included in requirements.txt (and have NOT been commented out).


```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.

```shell
py utils_michaeljmoore.py
py dirbot_michaeljmoore.py
```

## Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```

## Reference Projects

Custom implementation of the example project at 
[datafun-02-project-setup](https://github.com/denisecase/datafun-02-project-setup)

- [Module 1 Repo](https://github.com/denisecase/datafun-01-utils/)

# datafun-01-utils

Reusable module for my Data Analytics Python projects

## Project Requirements

- VS Code
- Git
- Python 

## Use Standard Professional Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

These commands will:
1. Create virtual environment in .venv folder
2. Activate .venv
3. Upgrade core tools
4. Install external project packages
5. Verify installed packages

**Mac/Linux**

```shell
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt
pip list
```

**Windows PowerShell**

```shell
py --version
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
py -m pip list
```

## Commands to Run Python Script

**Mac/Linux**

```shell
python3 utils_michaeljmooree.py
```

**Windows PowerShell**

```shell
py utils_michaeljmoore.py
```

> To stop a running Python program, press `Ctrl + C` in the terminal 
> (works the same on Windows, Mac, and Linux).

## Commands to Git add-commit-push

Write a custom message (-m) in quotes describing what was done, e.g. "completed first TODO", "final commit", etc. 

These commands work the same in all terminals and will:
1. Add all new and modified files in the current project folder into Git staging area. The `.` means _everything in this folder_.
2. Commit (record) a snapshot of staged changes with a descriptive message that will appear in the repo history.
3. Push (upload) commits from local machine to the remote (GitHub) repo (alias `origin`) on the main branch. The -u tells Git to remember this this branch mapping on upstream commands, so future git push commands can be shorter (just `git push`).


```shell
git add .
git commit -m "custom message here"
git push -u origin main
```

## Reference Project

This project is a custom implementation of the example project at 
[datafun-01-utils](https://github.com/denisecase/datafun-01-utils).

## Writing Good README.md Files

Every GitHub project has a README.md file with an overview.
The file type is `Markdown` and it's a very simple Markup language for text. 

- A Markdown `title` starts with: hash space
- A Markdown `second-level heading` starts with: hash hash space
- A Markdown `un-ordered list` starts with: dash space
- A Markdown `ordered list` start with: 1. space
- Markdown `code fencing` uses three **back tics** on their own line to display code and commands.
- Markdown **bold text** is surrounded by: two asterisks
- Markdown *underline text* is surrounded by: one asterisk


Markdown skills are critical for project README files, Jupyter Notebooks (code, charts, and narrative together), and writing technical papers with Sphinx.

## Example Screenshots

> Know how to display an image in Markdown - you'll want this to highlight your charts and more. 

![VS Code While Working](images/vs_code_while_working.png)


## Skills Demonstrated

- GitHub repo with README.md
- Git clone to machine.
- Create Python module.
- Create Python local virtual environment in .venv folder.
- Manage external packages (e.g. for logging and read-out-loud)
- Working with variables and functions. 
- Creating a standard Python module (ready for import or running as a script).
- Git clone, add, commit, push, pull
- Using a professional IDE (VS Code)
