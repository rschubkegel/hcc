---
title: 'Python - Reading & Writing Files'
date: 2024-11-07
---

# Reading & Writing Files <!-- .element: class="r-fit-text" -->

Week 10

---

## Review: Modules

<!-- TODO -->

--

### What is a Python Module?

Another Python file. <!-- .element: class="fragment" -->

--

### How do You Import a Module?

```py
import module_name
import module_name as module_alias
from module_name import something
from module_name import something as something_alias
```
<!-- .element: class="fragment" -->

---

## Review: Files

<!-- TODO -->

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

---

## Tabular Data

<!-- TODO -->

--

### What is Tabular Data?

> Refers to data that is organized in a table with rows and columns <sup>[<a href="https://www.statology.org/tabular-data/">1</a>]</sup>

--

### Why is it Useful?

- Organization <!-- .element: class="fragment" -->
- Data analysis <!-- .element: class="fragment" -->
- Scalability <!-- .element: class="fragment" -->

--

### Where Have You Seen It?

- Google Sheets <!-- .element: class="fragment" -->
- Microsoft Excel <!-- .element: class="fragment" -->

--

### Databases

- Databases are special programs that store _massive_ amounts of data
- Databases _structure data_ just like tabular data
- Databases do not store all the data in a single file

NOTE:
This is how data is stored for large-scale, professional apps.
They often allow data to be _related_ for performance and analysis.

---

## Pandas Module

<!-- TODO -->

---

## Exercise

<!-- TODO -->