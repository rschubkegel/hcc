---
layout: "@layouts/Simple.astro"
title: "Assignment: Tic Tac Toe pt. 3"
---

← [Course Homepage](/2024/fall/computer-science)

# Tic Tac Toe (part 3)

<mark>Due 10/23 at 11:59</mark>

In [part 1](/2024/fall/computer-science/assignments/tic-tac-toe-1) of this project, you created the functions necessary to print a game board. In [part 2](/2024/fall/computer-science/assignments/tic-tac-toe-2) you added the game state and player input. Now, it's time to add the final touch: winning! 👑

Your program must follow these specifications:

- Add new code to the `tic_tac_toe.py` file
- Create a new function called `check_winner` (see [details below](#checking-the-winner))
  - Will return one of these values: `'X'`, `'O'`, `'tie'`, or `None`
- In the main game loop, call the function `check_winner` and do the following with the results:
  - If `'X'` or `'O'`, stop looping and announce the winner
  - If `'tie'`, stop looping and announce that the game was a "cat game"
  - If `None`, continue the loop as normal

- When a player gets three pieces in a row (horizontally, vertically, or diagonally) the game loop must end and the winner must be announced
- If all cells on the board are filled with pieces (but no player has won) the game loop must end and it must be announced that it was a "cat game" (draw, tie)

### Checking the Winner

Your new function `check_winner` must check the current game state (in `board` variable) and do the following:

- If a player gets three pieces in a row (horizontally, vertically, or diagonally) return that player's piece (`'X'` or `'O'`)
- If all cells on the board are filled with pieces (but no player has won) return `'tie'`
- Otherwise, return `None`

Thare are several ways that you can check whether a player has three pieces in a row, it doesn't really matter how you do it. The important thing is that a player can win, lose, or tie to end the game.

Just make sure to test your code before submitting!

### Submit Assignment

When your program meets the requirements, download and submit `tic_tac_toe.py` (which is part 2 & 3 of the project).

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSeYqPABtKvrF871e5wXUvl67RENvQB50YmacgPPNC1yuonJyQ/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a>
</p>