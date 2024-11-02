---
title: 'Python - Dictionaries'
date: 2024-11-02
---

# Python Dictionaries <!-- .element: class="r-fit-text" -->

Week 10

---

## Review: Functions

![](https://media2.giphy.com/media/9tLjK1Ro0E2dzGgxlN/200.webp?cid=790b7611cluq55uamjzvz6u9d9oez7wol5cjpcof0hrg3hfz&ep=v1_gifs_search&rid=200.webp&ct=g) <!-- .element: style="height:400px" -->

--

### How Do You Call a Function?

```py
print()
print("Hello, World!")
print("Hello, World!", end="")
```
<!-- .element: class="fragment" -->

--

### How Do You Define a Function?

```py
def add_numbers(num1, num2):
  result = num1 + num2
  return result
```
<!-- .element: class="fragment" -->

--

### Is This Valid Python?

```py
print("Calling pring")
print_variable = print
print_variable("Calling print_variable")
```

Yes! <!-- .element: class="fragment" -->

NOTES:
- `print_variable` stores a reference to `print` function
- `print_variable` is now callable!

--

### Is This Valid Python?

```py
say_hello()
def say_hello():
  print("Hello, World!")
```

No! <!-- .element: class="fragment" -->

---

## Review: Files

![](https://media0.giphy.com/media/l2SpKBAxpCCLuUGU8/200.webp?cid=790b7611qlbo7zxkjcytskr00vqgq2fu0wb7ko2iy59wkqyb&ep=v1_gifs_search&rid=200.webp&ct=g) <!-- .element: style="height:400px" -->

--

### Name the 3 Steps to Read a File

1. Open <!-- .element: class="fragment" -->
2. Read <!-- .element: class="fragment" -->
3. Close <!-- .element: class="fragment" -->

--

### Name the 3 Steps to Write a File

1. Open <!-- .element: class="fragment" -->
2. Write <!-- .element: class="fragment" -->
3. Close <!-- .element: class="fragment" -->

--

### How to Auto-close a File?

```py
with open('notes.txt', 'r') as file:
  content = file.read()
```
<!-- .element: class="fragment" -->

--

### What Are File "Modes?"

Tells the OS how you will use the file. <!-- .element: class="fragment" -->

```py
file = open('notes.txt', 'r')
print( file.read() )
file.close()
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

### What Happens When You Open a File That Doesn't Exist?

In read mode (`'r'`) Python throws an error.
<!-- .element: class="fragment" -->

In write/append mode (`'w'`/`'a'`) the file is created.
<!-- .element: class="fragment" -->

--

### How to Avoid File DNE Error?

```py
import os
if os.path.exists("my_file.txt"):
  # TODO use file
```
<!-- .element: class="fragment" -->

NOTE: `try`/`catch` is another way

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
- Sometimes called an "associative array" or a "map"

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
Any! <!-- .element: class="fragment" -->

--

### What Type of Data Can Be Stored in a Dictionary Value?

Any! <!-- .element: class="fragment" -->

---

## Exercise

<!-- TODO -->