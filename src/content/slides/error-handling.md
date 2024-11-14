---
title: 'CS - Error Handling'
date: 2024-11-21
---

# Error Handling <!-- .element: class="r-fit-text" -->

Week 12

---

## Review: Databases

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnA4ZHg2cnN4NWl4amxzOXBhNXBwZWd5aWFzbmhyaHkzM2Iwang0byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26BoDGStUAafwdZII/giphy.webp) <!-- .element: style="height:400px" -->

--

### How do applications store large amounts of structured data?

They store them in **databases**.
<!-- .element: class="fragment" -->

--

### Is a database faster than a file system?

Yes!
<!-- .element: class="fragment" -->

--

### Other than speed, why use a database?

You can ask questions using structured query language (SQL).
<!-- .element: class="fragment" -->

---

## Error Handling

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHY0dWE2dzduaTh6emFobjkyYXk5eXBkZjZjaXdubWt5OTN4a2dwaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1n4iuWZFnTeN6qvdpD/giphy.webp) <!-- .element: style="height:400px" -->

--

### Errors and Exceptions

**Errors** are synonymous with **exceptions**\*

\*for this class
<!-- .element: class="fragment" -->

NOTE: the difference is more important in languages like Java

--

### What is an Exception?

An exceptional condition requiring special processing.
<!-- .element: class="fragment" -->

--

### What Happens in Response?

An exception breaks the normal flow of execution and executes a pre-registered exception handler.
<!-- .element: class="fragment" -->

NOTE: an exception handler is a special program that runs in response to an exception.

--

### Levels of Abstraction

- ⚡ CPU interrupts <!-- .element: class="fragment" -->
- 💻 OS signals <!-- .element: class="fragment" -->
- ⌨️ Programming language exceptions <!-- .element: class="fragment" -->

--

### Most Famous Exception handler

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Bsodwindows10.png/1200px-Bsodwindows10.png) <!-- .element: style="height:400px" -->

NOTE: this is an OS-level exception handler

---

## Types of Errors

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTE4bmtxemhqamc1ODY1eTNnOHJlNnpuZWdtZXkyNmxpcWgxNWlqOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJUIAqI3JY7snl04/giphy.webp) <!-- .element: style="height:400px" -->

--

### Basic Types of Errors

- Syntax errors
- Logical errors
- User\* errors

--

### Syntax Errors

Invalid programming language syntax

```py
num = 5
if num > 5:
  print("Greater than 5")
else num < 5:
  print("Less than 5")
```
<!-- .element: class="fragment" -->

--

### Logic Errors

Invalid program logic (doesn't always raise an exception)

```py
num = 5
if num > 5:
  print("Greater than 5")
else:
  print("Less than 5")
```
<!-- .element: class="fragment" -->

--

### User\* Errors

\*Users can do something incorrectly but if it causes an exception, _it is the programmer's fault_ <!-- .element: class="fragment" -->

```py
num = int( input("Enter a number: ") )
if num > 5:
  print("Greater than 5")
elif num < 5:
  print("Less than 5")
else:
  print("Equal to 5")
```
<!-- .element: class="fragment" -->

NOTE: we will learn how to handle this in Python later

---

## "Edge Cases"

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3JqZ3F3YmJod2lrbmljYnZydGV1Mjl5aHVzdThkYzQxMGJqOTRhZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NhVA7xxximbFQRjLi1/giphy.webp) <!-- .element: style="height:400px" -->

--

### Definition

An "edge case" is an uncommon scenario that can potentially cause an error.

NOTE: edge cases are often _expected_ to occur.

--

### Example: Division by Zero

```py
average_age = 38.5
user_age = int( input("Enter your age: ") )
print(f"Your age is {user_age / average_age}% of the U.S. average")
```

What if the user was 0 years old?
<!-- .element: class="fragment" -->

--

### Example: Multiple Names

```py
user_name = input("Enter your name: ")
print(f"Your name has {len(user_name)} letters in it")
```

What if the user's name is "Alice Ann?"
<!-- .element: class="fragment" -->

---

## Review

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTdoang3OTYxaG96M3Vnamk5dnZ4YjRncGEzY240eDhwdWxlZHJmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dXRxuvGmfRMCbNA6FK/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is an Exception?

**An exceptional condition** requiring special processing.
<!-- .element: class="fragment" -->

--

### Do Exceptions Cause Crashes?

Only if they are not handled properly!
<!-- .element: class="fragment" -->

--

### Basic Types of Errors

- Syntax errors <!-- .element: class="fragment" -->
- Logical errors <!-- .element: class="fragment" -->
- \*User errors <!-- .element: class="fragment" -->

--

### What is a "Syntax" Error?

Invalid programming language syntax

--

### What is a "Logic" Error?

Invalid program logic (doesn't always raise an exception)

--

### Is it the User or Programmer's Responsibility to Prevent Errors?

The programmer!
<!-- .element: class="fragment" -->

--

### What is an Edge Case?

An extreme, unlikely, or unusual scenario.
<!-- .element: class="fragment" -->

---

## Now for Some Coding... <!-- .element: class="r-fit-text" -->

[Python: Error Handling](/2024/fall/computer-science/slides/python-error-handling)
