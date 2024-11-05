---
layout: "@layouts/Simple.astro"
title: "Assignment: Guess the Number - High Scores"
---

← [Course Homepage](/2024/fall/computer-science)

# Guess the Number - High Scores

<mark>Due 11/13 at 11:59</mark>

To practice loading and saving files, you will extend the _Guess the Number_ project to incorporate persistent high scores. I highly recommend that you make a copy of the project and edit the copy instead of editing the original project directly.

Your program must meet the following requirements:

- Meet requirements for original [Guess the Number](/2024/fall/computer-science/assignments/guess-the-number) project
- When the game ends, load previous scores from a file located in a `data/` directory (if available)
  - There should be a different file for each difficulty level
- Tell the user where they ranked against the previous scores
  - Only compare against the selected difficulty level
- Save the scores (including the new one) to a file in the `data/` directory
  - Make sure to save in the file associated with the selected difficulty level

It's up to you to decide how to name the files, as well as which module you prefer to save and load the data with.

If you use the `pickle` module, make sure to use either `rb`, `wb`, or `ab` file modes since _pickle does not save data in plaintext format_.

Review the [week 9 slide deck](http://localhost:4321/2024/fall/computer-science/slides/python-files) for an example of how to use `pickle` and `json` modules.

<details>

<summary>Extra Challenges (optional)</summary>

- Save cumulative statistics to another file
  - Number of times each difficulty has been played
  - Percentage of guesses that were too high
  - Percentage of guesses that were too low
- Allow users to enter their initials
  - Print initials and scores of top 5 scores at the end of the game

</details>

## Submit Assignment

When your program meets the requirements, download and submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSdzi4rS8ilsNJMGk2Sz0wU31QMHv0ej6ajWTutIcoKiHN1Q0w/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a>
</p>

