---
layout: "@layouts/Simple.astro"
title: "Assignment: Password Generator"
---

← [Course Homepage](/2024/fall/computer-science)

# Password Generator

<mark>Due 10/02 at 11:59</mark>

A good safety practice is to _randomly generate your passwords_; this makes it very difficult for a hacker to guess your password. In this assignment, you will implement your own password generator.

Your program must meet the following specifications:

- Create a **list** variable with possible characters to pick from
- Ask the user for the password length
- Use a loop to randomly select characters (`a`-`f` & `0`-`9`)
- Print the generated password to the terminal

> A common technique in brute-force hacking is to create special "dictionary" of words and phrases that are specific to the person they are hacking. Lots of people choose a password they can remember that includes their birthday, their pet's name, the school they attend, etc. However, that is **very insecure** because that information is fairly easy to obtain through social media, conversations with friends, or public records.

### Intro to Lists

We will learn more about lists in the future, but for this assignment I will provide you with starter code to modify:

```py
# Creates a list (you must fill this out in your assignment)
characters = ["a", "b", "c"]

# ...

# Prints "a" to the terminal
print(characters[0])

# Assigns the value "b" to the variable letter
letter = characters[1]
```

### Submit

As per usual, submit the assignment via Google Form:

<p style="text-align:center"><a href="https://docs.google.com/forms/d/e/1FAIpQLScUq9psuQYHLXGSEgLyhjx3ugsBQND-10Z3X56Nuwag86PyLw/viewform?usp=sf_link" class="button">Submit Assignment</a></p>