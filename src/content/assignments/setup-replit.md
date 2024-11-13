---
name: Setup Replit
startDate: 2024-09-19
---

Time for a new development environment!

I apologize for changing our tooling so much, I am trying to find an <abbr title="integrated development environment">IDE</abbr> that is _free_, _simple_, and _performant_. Hopefully Replit will be the last one 🤞🏻

Replit is has a free tier that allows up to 3 projects. Since we will have more than 3 projects, each project will be a separate file in a single project. That means _all the assignments for the semester will be in a **single project**_.

> REPL stands for Read-Eval-Print Loop. It is a computer environment where user inputs are read and evaluated, and then the results are returned to the user.

### 1. Sign Up

Go to [replit.com](https://replit.com/) and click "Sign Up."

![](/2024/fall/computer-science/images/setup-replit/landing.png)

Create an account using your Google account.

![](/2024/fall/computer-science/images/setup-replit/signup.png)

### 2. Create a Project

From the dashboard, you will see a blue button at the top of the screen that says "+ Create Repl"--press that to show the new project dialog.

![](/2024/fall/computer-science/images/setup-replit/dashboard.png)

Select Python as the project language. Give the project a descriptive title, such as "HCC Comp Sci." Press "Create Repl" to enter the editor.

![](/2024/fall/computer-science/images/setup-replit/new-project.png)

### 3. Add Project File

Your editor will look similar to this to start. If you press "Run" you should see the "Console" tab (a console is type of terminal) appear with "Hello, World!" printed to the screen.

![](/2024/fall/computer-science/images/setup-replit/empty-project.png)

For each project going forward, you will create a new file by pressing the "New file" button at the top left of the screen. Use lowercase and underscores to write a file name that matches the project. Make sure to end the file name with the `.py` extension so Replit knows it is a Python script.

In my example, I created the `guess_the_number.py` file for the "Guess the Number" project.

![](/2024/fall/computer-science/images/setup-replit/new-file.png)

This file is where you will write all your code. For the "Guess the Number" project, you can copy and paste the example code from the [assignment page](/2024/fall/computer-science/assignments/guess-the-number).

![](/2024/fall/computer-science/images/setup-replit/paste-code.png)

If you try to run your code, you will still see "Hello, World!" printed to the console. That is because the Replit environment looks for a file called `main.py` and automatically runs that one. To run the `guess_the_number.py` script, you must import it in the main file.

In `main.py`, replace the "Hello, World!" code with the following line:

```py
import guess_the_number
```

Make sure it matches the file name _exactly_. When you press "Run" you will see the code from the `guess_the_number.py` file execute!

![](/2024/fall/computer-science/images/setup-replit/import-file.png)

In future projects, you will comment out the import in `main.py` and import a new project file.

```py
# import guess_the_number
import another_project_file
```

### Submit

There is no submission for this assigment 🎉

If you have any trouble with the steps above, reach out as soon as possible!