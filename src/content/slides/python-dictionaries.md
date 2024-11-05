---
title: 'Python - Dictionaries'
date: 2024-11-14
---

# Python Dictionaries <!-- .element: class="r-fit-text" -->

Week 11

---

## Review

![](https://media0.giphy.com/media/l2SpKBAxpCCLuUGU8/200.webp?cid=790b7611qlbo7zxkjcytskr00vqgq2fu0wb7ko2iy59wkqyb&ep=v1_gifs_search&rid=200.webp&ct=g) <!-- .element: style="height:400px" -->

--

### Name the 3 Steps to Read a File

1. Open <!-- .element: class="fragment" -->
2. Read <!-- .element: class="fragment" -->
3. Close <!-- .element: class="fragment" -->

--

### How to Auto-close a File?

```py
with open('notes.txt', 'r') as file:
  content = file.read()
```
<!-- .element: class="fragment" -->

--

### What Kinds of File Modes Are There?

```py
'rt' # read text (same as 'r')
'rb' # read binary
'wt' # write text (same as 'w')
'wb' # write binary
'at' # append text (same as 'a')
'ab' # append binary
```
<!-- .element: class="fragment" -->

--

### What is the Current Working Directory?

The folder where Python was run.
<!-- .element: class="fragment" -->

NOTE: Or the folder where terminal is running.

--

### What is the Difference Between an **Absolute** Path and a **Relative** Path?

Relative paths resolve to different locations based on the CWD, but absolute paths always resolve to same location.
<!-- .element: class="fragment" -->

--

### Relative Paths

```py
# /
# ├─ main.py
# └─ files/
#   └─ notes.txt
```

What is the path of `notes.txt` relative to `/` directory?

```
"files/notes.txt"
```
<!-- .element: class="fragment" -->

What is the path of `main.py` relative to `files/` directory?
<!-- .element: class="fragment" -->

```
"../main.py"
```
<!-- .element: class="fragment" -->

---

## Dictionary Basics

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjZ4NW5zamJ2MDB6dWMyMnB0NWNlaXVmOGhmMWN6eTY4bDcwamE1YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26BRDvCpnEukGhmHC/200.webp) <!-- .element: style="height:400px" -->

--

### Create

```py
course = {
  "year": 2024,
  "term": "Fall",
  "title": "Computer Science",
  "instructor": "Rylan",
}
```

NOTES:
- Stores key/value pairs
- Sometimes called an "associative array" or a "hash map"

--

### No Duplicates!

```py
course = {
  "year": 2024,
  "term": "Fall",
  "title": "Computer Science",
  "instructor": "Rylan",
  "instructor": "Alec",
}
```

Course instructor will be "Alec" since Python only keeps the last entry.

--

### Accessing Items

```py
instructor = course["instructor"] # 👈🏻 preferred syntax
title = course.get("title")
```

--

### Utilities

```py
print(len(course))      # 4
print("term" in course) # True
```

--

### Updating Items

```py
course["title"] = "Comp. Sci." # 👈🏻 preferred syntax
course.update({ "title": "Comp. Sci." })
```

--

### Adding Items

```py
course["grades"] = [9, 10, 11, 12] # 👈🏻 preferred syntax
course.update({ "grades": [9, 10, 11, 12] })
```

--

### Removing Items

```py
course.pop("grades")
del course["grades"]
course.clear() # removes all items
```

--

### Looping

```py
for key in course:
  print(f'Key:   {key}')
  print(f'Value: {course[key]}')
```

```py
for key, value in course.items():
  print(f'Key:   {key}')
  print(f'Value: {value}')
```
<!-- .element: class="fragment" -->

---

## Review

![](https://media4.giphy.com/media/TFP51HPcAv2J3hQnqY/200.webp?cid=ecf05e4747xluzjxdcg14o075t9a99bof0kfmuyhn3apkc7w&ep=v1_gifs_search&rid=200.webp&ct=g) <!-- .element: style="height:400px" -->

--

### Which Characters Open/Close Dictionary Definition?

- `[]`
- `()`
- `{}`

```py
my_dict = { "foo": "bar" }
```
<!-- .element: class="fragment" -->

--

### Can Dictionaries Have Duplicate Keys?

No! <!-- .element: class="fragment" -->

--

### How Do You Access Values?

```py
instructor = course["instructor"] # 👈🏻 preferred syntax
title = course.get("title")
```

--

### What Type of Data Can Be Stored in a Dictionary Value?

Any! <!-- .element: class="fragment" -->

---

## Exercise

- Create a dictionary of 2+ "commands"
  - Keys are a word the user must type, e.g. `greet`
  - Values are descriptions of the action
- Use a loop to print all commands & instructions
- Get command from user and perform relevant action

--

## Additional Challenge: Command Aliases

- Make the values of command dictionary _other dictionaries_
- 2nd level dictionary should have these keys:
  - `description`
  - `alias`
- When asking user for command, allow an alias to perform the same action

Example: `greet` and `g` would do the same thing