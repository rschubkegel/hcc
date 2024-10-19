---
title: 'Python - Reading & Writing Files'
date: 2024-10-31
---

# Reading & Writing Files <!-- .element: class="r-fit-text" -->

Week 9

---

## Review

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXhpamp5aGh6ZWRybjMyZXZkY3gwMTMzN3VtcGxpMzdrdmpqbXMxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f8c3iR9TzCCSDyIAsY/giphy.webp) <!-- .element: style="height:400px" -->

--

#### What is a module?

Another Python script. <!-- .element: class="fragment" -->

NOTES: It's just a file (for our purposes)

--

#### Import Syntax

```py [1|2|3]
import random
from math import pi
from datetime import * # DON'T DO THIS
```

---

## Reading Files

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3d0ODM5c2RlZWNjY2U0MG1lMzZiNmsyaDR4aWVhb3Fha3F0ZjY0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oFPiPgqwof4Pe/giphy.webp) <!-- .element: style="height:400px" -->

--

### A Simple Example

```py
file = open("file.txt")
lines = file.read()
file.close()
```

NOTES: `file` is an object; lines must be manually read, the file object must be closed when finished

--

### A Closer Look

```py [1-2|4-8|10-11]
# groceries.txt is in same folder as main.py
file_name = "groceries.txt"

# "r" == reading
# "w" == writing
# "a" == append
# others include "x", "b", "t" etc.
mode = "r+"

# Talks to the OS to open the file
file = open(file_name, mode)
```

--

### Reading Contents

```py
# Returns a string
content = file.read()
print(content)
```

```py
# Iterates over all lines in file
for lines in file:
    print(line)
```

NOTES: `file` is a file object, not a list, so you can't use it like a list

--

### Using `with`

```py
with open("file.txt") as file:
    file.read()
```

NOTES: using `with` block automatically closes the file

--

### Why Close a File?

- Resource leaks <!-- .element: class="fragment" -->
- Data corruption <!-- .element: class="fragment" -->
- File locking (uncommon) <!-- .element: class="fragment" -->

NOTES:
- resource leaks slow your program down (too complex to explain in this class)
- data might be written incorrectly
- an error might occur in your program or another program if file locking is used (like checking out a book at the library)

---

## Writing Files

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmwzbXgwY2I5ejlyNXh6a3NjYzBnZmY2cjVqamxseHNnOGdiaXN4cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LmBsnpDCuturMhtLfw/giphy.webp) <!-- .element: style="height:400px" -->

--

### A Simple Example

```py
with open("text.txt", "w") as file:
    file.write("Hello, World!")
```

NOTES: by default, the mode is read-only so you **must** specify write mode

--

### Writing vs. Appending

```py
with open("text.txt", "a") as file:
    file.write("\n\nPS: I like Python")
```

NOTES: with write mode, the entire file contents are _overwritten_

---

## Complex Data

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW5kczlxMXNqZjJ0MzhvajczZTNqeTRhdG0xaXNtdXN1cnd4eXV4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2SpLKrc4mqgzELwk/giphy.webp) <!-- .element: style="height:400px" -->

--

### Writing

You can only read/write text data, so how do you save other data types?

```py
groceries = ["salami", "grapefruit", "pepperjack"]

# With pickle
import pickle
with open("data.pickle", "wb") as file:
    pickle.dump(groceries, file)

# With json
import json
with open("data.json", "w") as file:
    json.dump(groceries, file)
```

NOTES:
- `pickle` converts Python objects to steams of **bytes** and back
  - That means it must use **write binary** file mode
- `json` converts (simple) Python objects to **text** and back

--

### Reading

```py
groceries = None

# With pickle
import pickle
with open("data.pickle", "rb") as file:
    groceries = pickle.load(groceries, file)

# With json
import json
with open("data.json", "r") as file:
    groceries = json.load(file)
```

---

## Review

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTg4amowNXNxMmhsN2FldGZkaTZvaGkxM20xMTk3a214bXQ4aWJucSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ABuKD88Xnsl9HKcKwe/giphy.webp) <!-- .element: style="height:400px" -->

--

### List the 3 Steps of Reading Files

Opening, reading, closing. <!-- .element: class="fragment" -->

--

### Name 3 File Modes

Read (text), write (text), read/write (text), read (binary), write (binary), read/write (binary), etc. <!-- .element: class="fragment" -->

--

### Syntax to Automatically Close File

`with open("file_name.txt") as file:` <!-- .element: class="fragment" -->

--

### One Way to Read Contents of File

`file.read()` <!-- .element: class="fragment" -->

or

`for line in file:` <!-- .element: class="fragment" -->

--

### What is the Bug?

```py
# Write message to file
with open("text.txt") as file:
    file.write("Hello, World!")
```

Mode is "readonly" by default; I need to provide second argument "w" to open function. <!-- .element: class="fragment" -->

--

### Name a Module That Writes Complex Data

`pickle` <!-- .element: class="fragment" -->

or

`json` <!-- .element: class="fragment" -->

---

## Exercise

- Extend to-do list program with "save" feature
- Use `pickle` or `json` module
- Load list when program starts