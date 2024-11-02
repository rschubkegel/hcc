---
layout: "@layouts/Simple.astro"
title: "Assignment: Dice Rolling Simulator"
---

← [Course Homepage](/2024/fall/computer-science)

# Dice Rolling Simulator

<mark>Due 11/06 at 11:59</mark>

A common way to add excitement to games is to add randomness. For board games, this is usually in the form of dice; in this project, you will create a program that emulates rolling dice.

Your program must satisfy the following specifications:

- Allow user to select the number of faces of the die they will roll (D6, D12, or D20)
- In a loop, allow the user to do one of two things:
  - Roll the die (and print result)
  - Exit the loop
- [Load](#reading-a-file) the total number of rolls from a file
- Print the following information
  - Highest roll
  - Number of rolls (this session)
  - Number of rolls (for all time)
- Save the number of rolls (for all time) to a file

## Reading a File

When trying to read a file that does not exists, you will get an error like this:

```
FileNotFoundError: [Errno 2] No such file or directory
```

One way to avoid this is by checking if the file exists by using a function in the `os` module:

```py
import os
if os.path.exists("my_file.txt"):
  # TODO read the file
```

## Submit Assignment

When your program meets the requirements, download and submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSfD0gZZwuVTFfkzV6rFlCxgNqbciU3aRMU2sIfCu39PK5yfsw/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a>
</p>
