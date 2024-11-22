---
title: 'Python - Lists'
date: 2024-09-26
---

# Python Lists <!-- .element: class="r-fit-text" -->

Week 4

---

## Review: Data Types

![](https://i.giphy.com/l0JMrPWRQkTeg3jjO.webp) <!-- .element: style="height:400px" -->

--

### Two Types of Variables

- Primitive <!-- .element: class="fragment" -->
- Compound <!-- .element: class="fragment" -->

--

### Primitive Data Types

- Integer (int) <!-- .element: class="fragment" -->
- Floating Point Number (float) <!-- .element: class="fragment" -->
- String (str) <!-- .element: class="fragment" -->
- Boolean (bool) <!-- .element: class="fragment" -->
- NoneType (None) <!-- .element: class="fragment" -->

--

### Reassignment

Will this code throw an error?

```py
year = 2024
year = "crazy"
```

No ✅
<!-- .element: class="fragment" -->

--

### Reassignment

Will this code throw an error?

```py
year = 2024
message = year + " is crazy"
```

Yes 💥 Instead, do this:
<!-- .element: class="fragment" -->

```py
year = 2024
message = str(year) + " is crazy"
```

---

## List Basics

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemtuZGd0bmN6eWltM25sZW15dmo1b2swc3hpbnphaXQ0cTJ0aXJmZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0QshCl75doGqEHV3jb/giphy.webp) <!-- .element: style="height:400px" -->

--

### Creating a List

```py
my_list = [0, 1, 2] # &lt;-- most common
my_list = [0, 1] + [2]
my_list = list(range(3))
```

--

### Indexing

What does this code print?

```py
my_list = [0, 1, 2]
print(my_list[1])
```

1
<!-- .element: class="fragment" -->

--

### Negative Indexing

```py
my_list = ["hello", "python", "world"]
my_list[-1] # "world"
my_list[-2] # "python"
```

--

### Indexing Out Of Bounds 💥

```py
["hello", "world"][2]
# Traceback (most recent call last):
#   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
# IndexError: list index out of range
```

--

### Looping with `while`

```py
my_list = [0, 1, 2]
index = 0
while index &lt; 3:
  print(my_list[index])
  index = index + 1
```

--

### Looping with `for`

```py
my_list = [0, 1, 2]
for item in my_list:
  print(item)
```

--

### Looping with `range`

<div class="r-stack">
  <pre class="current-visible">
    <code data-trim data-noescape class="language-python">
      my_list = [0, 1, 2]
      for index in range(3):
        print(my_list[index])
    </code>
  </pre>
  <pre class="current-visible fragment">
    <code data-trim data-noescape class="language-python">
      my_list = ["I", "have", "so", "many", "items"]
      list_length = len(my_list)
      for index in range(list_length):
        print(my_list[index])
    </code>
  </pre>
</div>

--

### Review

```py [1|2|3|4|5]
my_list = [True, "Al", 3.14]
print(my_list[1])
print(my_list[-1])
print(my_list[-0])
print(len(my_list))
```

---

## Modifying Lists

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWdubDBhOTVrODF5c3RzYWlqMWNwd2gxYnR6bmZxdDU5OG9xamFzZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orifaGGghuf3hnmsE/giphy.webp) <!-- .element: style="height:400px" -->

--

### Updating

```py
my_list = ["hello", "world"]
my_list[1] = "Ryder"
# ["hello", "Ryder"]
```

### Append

```py
my_list = [0, 1, 2]
my_list.append(3)
# [0, 1, 2, 3]
```

--

### Remove

```py
my_list = ["foo", "bar"]
my_list.remove("bar")
# ["foo"]
```

--

### Pop

```py
my_list = [0, 1, 2]
my_list.pop()
# [0, 1]
```

--

### Pop with Index

```py
my_list = [0, 1, 2]
my_list.pop(1)
# [0, 2]
```

---

## Activity: To-Do List <!-- .element: class="r-fit-text" -->

- Infinite loop with 4 commands:
  - Print list
  - Add item
  - Remove item
  - Quit
- Format the list nicely ✨

---

## Have A Great Week 👋🏻 <!-- .element: class="r-fit-text" -->