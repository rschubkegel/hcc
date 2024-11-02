---
title: 'Python - More Files'
date: 2024-11-02
---

# Python - More on Files <!-- .element: class="r-fit-text" -->

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
say_hello()
def say_hello():
  print("Hello, World!")
```

No! <!-- .element: class="fragment" -->

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

## Working Directory & File Paths

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FhTX2gItOECw%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=bdc1707ed6cf907a3c03f16e6dff3a7fb2a57aaaeda4b64e1c3f1b3122a4779b&ipo=images) <!-- .element: style="height:400px" -->

--

### Current Working Directory

Python _current working directory_ (CWD) is the folder where the Python interpreter was started.

```py [1|2]
import os
print( os.getcwd() )
```
<!-- .element: class="fragment" -->

```sh [1-2|3|5-6|7]
# Running script in main Replit folder
~/HCC-2024-CS$ python main.py
/home/runner/HCC-2024-CS

# Running same script in "scripts" folder
~/HCC-2024-CS$ python scripts/main.py
/home/runner/HCC-2024-CS
```
<!-- .element: class="fragment" -->

NOTE: All paths will be relative to the CWD.

--

### CWD and File Paths

What folder will text file `notes.txt` get saved?

```py
# /
# └─ main.py
```

```py
with open("notes.txt", "w") as file:
  file.write("Hello, World!")
```

```py
# /
# ├─ main.py
# └─ notes.txt
```
<!-- .element: class="fragment" -->

--

### Using Files in Other Folders

```py
# /
# └─ main.py
```

```py
with open("files/notes.txt", "wt") as file:
  file.write("Hello, World!")
```

```py
# FileNotFoundError: [Errno 2] No such file or directory
```
<!-- .element: class="fragment" -->

--

The folders you are writing to must already exist!

```py
# /
# ├─ main.py
# └─ files/
```

```py
with open("files/notes.txt", "wt") as file:
  file.write("Hello, World!")
```

```py
# /
# ├─ main.py
# └─ files/
#   └─ notes.txt
```
<!-- .element: class="fragment" -->

--

### Absolute Path vs. Relative Path

```py
import os
print( os.path.abspath("main.py") )
```

```py
# '/home/runner/HCC-2024-CS/main.py'
```
<!-- .element: class="fragment" -->

--

### Absolute Path vs. Relative Path

```py
import os
os.path.relpath("/home/runner/HCC-2024-CS/main.py")
```

```py
'main.py'
```
<!-- .element: class="fragment" -->

---

## Review

![](https://media4.giphy.com/media/xUrmE6PJBEbni/200.webp?cid=ecf05e47bz3j0qlilb9xcp9633ui9u9exp4rhffapwdeqic4&ep=v1_gifs_search&rid=200.webp&ct=g) <!-- .element: style="height:400px" -->

--

### What is the Current Working Directory?

The folder where Python was run.
<!-- .element: class="fragment" -->

NOTE: All relative file paths will be relative to the CWD.

--

### How to Check if File Exists?

```py
import os
os.path.exists("notes.txt")
```
<!-- .element: class="fragment" -->

--

### What is the Error Here?

```py
# /
# └─ main.py
```

```py
with open("files/notes.txt", "wt") as file:
  file.write("Hello, World!")
```

```py
# FileNotFoundError: [Errno 2] No such file or directory
```
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

## Exercise: Simple Database

- Create two files:
  - `data/students.txt`
  - `data/classes.txt`
- Write a program to do these actions:
  - List student names and student count
  - List class names and class count