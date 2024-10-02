---
layout: "@layouts/Simple.astro"
title: "Assignment: Tic Tac Toe pt. 1"
---

← [Course Homepage](/2024/fall/computer-science)

# Tic Tac Toe (part 1)

<mark>Due 10/09 at 11:59</mark>

Previously your projects have been simple enough to complete in one week, but now it's time to turn up the heat 🔥

During the next two weeks, you will program a game of _Tic, Tac, Toe_ to test your knowledge of functions. This week, you must submit a program that matches the following specifications:

- Define a function called `print_column`
  - Must have one parameter, `piece`
  - `piece` will be one of the following values:
    - `None` if no player has played on this cell yet
    - `'X'` if the X player has played on this cell
    - `'O'` if the Y player has played on this cell
  - Must print `piece` [without printing a newline character](#printing-without-a-newline)
- Define a function called `print_row`
  - Must have one parameter, `columns`, which will be a list of 3 values
  - Must call `print_column()` 3 times, once for each piece in `columns`
  - The printed pieces must be separated by the `|` character
- Define a function called `print_board`
  - Must have one parameter, `rows`, which will be a list of 3 values
  - Must call `print_row()` 3 times, once for each value in `rows`
  - The printed rows must be separated by a line of `-` characters
- Call `print_board()` to print a test board to the console, like so:
  ```py
  print_board([
    ['X', None, None],
    [None, 'O', 'X'],
    ['O', None, None],
  ])
  ```
  Which will result in somthing like the following output:
  ```
  -------------
  | X |   |   |
  -------------
  |   | O | X |
  -------------
  | O |   |   |
  -------------
  ```

### Printing Without a Newline

So far, each time we have called `print()` it has automatically added a newline character to the end of whatever string we pass as an argument. However, according to the [Python 3 docs](https://docs.python.org/3/library/functions.html#print) we can provide a _named argument_ for the parameter `end` to change what gets printed at the end of our string. Here is an example:

```py
print('Hello, ', end='')
print('World!')
print('This is a new line.')
```

Which prints the following output:

```
Hello, World!
This is a new line.
```

> _Named arguments_ are a more advanced feature in Python. If you are curious, [this article](https://pythonsimplified.com/python-parameters-and-arguments-demystified/) dives into different types of arguments and parameters.

### Submit Assignment

<p style="text-align:center"><a href="https://docs.google.com/forms/d/e/1FAIpQLSfwGIIqC4l_fX_AxlaJ007Tjbg11nTtZjU50rW7UY1nz-u3rw/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a></p>