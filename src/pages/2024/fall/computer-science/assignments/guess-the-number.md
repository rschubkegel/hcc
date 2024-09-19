---
layout: "@layouts/Simple.astro"
title: "Assignment: Guess the Number"
---

← [Course Homepage](/2024/fall/computer-science)

# Guess the Number

<mark>Due 09/25 at 11:59</mark>

<!-- One way to settle a dispute is to "pick a number between 1 and 10" and see who is closest. After completing this project, you can use your computer as an [arbitrator](https://www.merriam-webster.com/dictionary/arbitrator) in your next disagreement! -->

Make a simple game to practice using loops! Your program must meet the following specifications:

- Ask the user to pick from the following number ranges:
  - 10
  - 100
  - 1000
- Pick a **random number** within the specified range
- Use a loop to repeatedly ask for guesses within the number range
  - If the user guessed correctly, exit the loop
  - If the user guessed incorrectly, tell them if their guess was too high or too low
- Tell the user how many guesses they made

<details>
<summary>Additional Challenges (not required)</summary>

- Give the user a different score based on how many guesses they made
- Allow the user to quit at any time by pressing <kbd>q</kbd>
- Allow the user to play multiple times in a row

</details>

### Random Numbers

To generate a random number, you can use the built-in module `random`. We will learn about modules later, but for this project you may copy/paste the following code:

```py
# Imports the randint function from the random module
from random import randint

# Generates a number within the range 1 through 10
randint(1, 10)
```

> Computers can generate numbers that appear to be random, but they are not truly random. This is because computers are deterministic machines, meaning that their output is determined by their input and the algorithms used to process that input.

### Example Code

Since I did not record the activity/project time during class, here is the code that we "pair programmed" to help you out. Make sure to fill out the `TODO` comments with your own code to meet the specifications listed above!

```py
# Import random module
from random import randint

# Ask user for "difficulty" (number range)
# TODO

# Set up "answer" variable
# TODO replace 10 with number range from above
answer = randint(1, 10)

# Set up "guess" variable
guess = 0

# Set up "score" variable
# TODO

# Until the user answers correctly...
while guess != answer:
  # Ask the user for a guess and convert to integer
  guess = int( input("What is your guess? ") )

  # If the guess was correct, exit the loop
  if guess == answer:
    print("You are correct!")

  # If the guess was incorrect, continue
  if guess > answer:
    print("You were too high.")
  if guess < answer:
    print("You were too low.")

# Tell the user their score
# TODO

# Done 🎉
```

### Submit

Make sure you test your program before submitting!

<p style="text-align:center"><a href="https://docs.google.com/forms/d/e/1FAIpQLScbsk31ajIH5YqWfpNt1NcUuTIQM5-HEv7A1ow3JIkQUEa_Jw/viewform?usp=sf_link" class="button">Submit Assignment</a></p>