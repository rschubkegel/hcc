---
name: Tic Tac Toe (part 2)
title: "Assignment: TTT 2"
startDate: 2024-10-10
dueDate: 2024-10-16
---

In [part 1](/2024/fall/computer-science/assignments/tic-tac-toe-1) of this project, you created the functions necessary to print a game board; in this part you will add the game _state_ and _player input_ 🕹️

Your program must follow these specifications:

- Import your work from part 1 into a new file
- Create a `board` variable that represents an empty 3x3 game board
- Within a loop, do the following:
  - Print the board to the terminal
  - Ask "Player X" and "Player O" to take turns placing pieces
  - Update `board` variable with `'X'` or `'O'` value depending on the player's move

### Organize the Project

Previous projects have been simple enough to keep everything in a single file. Since this project is bigger, we are going to split it into multiple files!

- Rename your file from part 1 to `tic_tac_toe_board.py`
- Create a new file called `tic_tac_toe.py`
- Import _just the `print_board`_ function, like so:
  ```py
  from tic_tac_toe_board import print_board
  ```

Now, you can use the imported function to print the `board` variable each time through your loop!

### Game State

The current "state" of the game is stored in the `board` variable. Each board is a "table" that includes 3 rows, each with 3 columns. A single "cell" of the table represents what piece has been placed on the board. At the beginning of the game, no move have been made, so the board is empty. You can initialize the empty board like this:

```py
board = [
  [None, None, None],
  [None, None, None],
  [None, None, None],
]
```

As the game progresses, each player will add pieces to the board (represented by `'X'` or `'O'`) so that a complete game board might have a value like this:

```py
[
  ['X', None, 'O'],
  ['X', 'O', None],
  ['X', None, None],
]
```

### Submit Assignment

When your program meets the requirements, download and submit `tic_tac_toe.py` (which is just part 2 of the project).

<p style="text-align:center"><a href="https://docs.google.com/forms/d/e/1FAIpQLSdi9IqICUt8ctttFAtSGU0y-YjGKg4-71E6WaPnhFJlcsUHnw/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a></p>