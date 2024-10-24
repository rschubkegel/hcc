---
layout: "@layouts/Course.astro"
---

← [Course Homepage](/2024/fall/computer-science)

# Running Python Locally

[Replit](https://replit.com/) is a _cloud_ service, meaning your code runs on _someone else's machine_. However, if you run out of "Development Time" (bottom left corner of dashboard) and you don't want to pay for the service, it's time to set up your computer to run Python locally.

> You are **not required** to run Python locally. If you want to pay for a Replit subscription, you can skip this assignment. It does not matter for projects.

## Install Python

A Python _interpreter_ reads a line of Python, converts it to _bytecode_, then executes it in the Python Virtual Machine (which is machine code that your computer can understand). In order to run any Python program, you need an interpreter.

Go to the [downloads page on python.org](https://www.python.org/downloads/) and download the latest Python version (big yellow button). When the installer finishes downloading, run it.

Make sure "run as admin" is _unchecked_ and "add to PATH" is _checked_.

Run the default installation (not custom install).

When the installation finishes, you can verify that Python is installed by opening Windows Command Prompt and running the following:

```sh
python --version
```

If you have any issues with this step of the process, send me an email and I can help walk through the process.

## Install VS Code

You don't need anything special to write Python code. However, an _integrated development environment_ (IDE) makes it much easier.

OneCompiler, JDoodle, and Replit are IDEs that include syntax highlighting, code completion, and a simple <abbr title="user interface">UI</abbr> to run your code. However, they are limited because they run in your browser (as a cloud application). _Visual Studio Code_ (VS Code) is an IDE that you can run on your own computer.

Go to [code.visualstudio.com](https://code.visualstudio.com/) and download VS Code.

When the installation finishes, run the application. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) to enable syntax highlighting, code formatting, and other features.

When the installation finishes, you are now ready to code!

## Organizing Projects

To keep everything organized, I recommend keeping your Python files in a single folder. For example, `C:\Users\Rylan\Documents\Scripts`. After you create a folder for your projects, open it in VS Code by navigating to _File > Open Folder_.

You can now create a python file in the "Explorer" tab (two pages icon, left side), write some code in it (e.g. `print("Hello, World!")`), save it, and run it using the "Run Python File" button (play icon, top right).

> Previously you had to import each project in `main.py`; that is no longer required when running VS Code locally!

## Resolving Issues

The quickest and easiest way to resolve issues is to **contact me**. I am happy to set up a time to walk through the installation process or help you transfer projects from Replit.