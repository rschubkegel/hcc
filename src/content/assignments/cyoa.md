---
name: Choose Your Own Adventure
title: "Assignment: CYOA Story Game"
startDate: 2024-11-14
endDate: 2024-11-27
---

[Choose Your Own Adventure (CYOA)](https://www.cyoa.com/) novels allow readers to make choices that impact the story. In this project, you will make your own CYOA game.

Your program must meet the following specifications:

- Store your story data in dictionary where each _key_ represents a page number and each _value_ is a dictionary with the following data:
  - `text`: The text of this "page" of your "book"
  - `options`: A list of dictionaries with the following key/value pairs:
    - `text`: The text displayed to the user
    - `page`: The page number the user will go to next _OR_ `None` if this option ends the story.
- Use a loop to do the following:
  - Print page text
  - Print options
  - Get user input
  - If user input was a valid option, continue to page specified in `next`
  - If user input was invalid, print a warning and show the options again
- Your story must contain at least 10 "pages" (dictionary entries)

This is a great chance to flex your creative muscles 💪🏻 Have fun with it!!

## Example Story

Here is a simple example of a 2-page story dictionary (remember, yours must be at least 10 pages):

```py
story = {
  1: {
    "text": "Hello, world! It's a great day for looping, don't you agree?",
    "options": [
      {
        "text": "I agree 👍🏻",
        "page": 1
      },
      {
        "text": "I disagree 👎🏻",
        "page": 2
      }
    ]
  },
  2: {
    "text": "Well, we can agree to disagree.",
    "options": [
      {
        "text": "THE END",
        "page": None
      }
    ]
  }
}
```

## Example Output

```
Hello, world! It's a great day for looping, don't you agree?

    1) I agree!
    2) I disagree!

>> 1

Hello, world! It's a great day for looping, don't you agree?

    1) I agree!
    2) I disagree!

>> 3

Invalid choice "3"

Hello, world! It's a great day for looping, don't you agree?

    1) I agree!
    2) I disagree!

>> 2

Well, we can agree to disagree.

    1) THE END

>> 1
```

## Submit Assignment

When your program meets the requirements, download and submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScfZ2ZZ-lZsnRqg5aGbuYzuVJZzlmZXeUvL-lWVxEo5YKUXAQ/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a>
</p>
