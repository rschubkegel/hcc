---
title: 'Python - Error Handling'
date: 2024-11-21
---

# Error Handling <!-- .element: class="r-fit-text" -->

Week 12

---

## Try/Except

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdThsejNnaTZ4Mm9nZzZpMTVpejF2cWl5bXg0MnJvdDFseGtmZ3g2aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QMHoU66sBXqqLqYvGO/giphy.webp) <!-- .element: style="height:400px" -->

--

### Handling Errors

```py
n = int( input("Enter a number: ") )
```

What happens if I input `"foobar"` in the terminal?

ValueError: invalid literal for int() with base 10: 'foobar'
<!-- .element: class="fragment" style="color:#ff4048" -->

--

### What Happens?

When an **error** or **exception** are raised, the program stops and displays the exception.

When running a script, the program "crashes" ...
<!-- .element: class="fragment" -->

...only if the error is _unhandled_.
<!-- .element: class="fragment" -->

NOTES:
- Error and exception are essentially the same in Python.
- In computing, a crash, or system crash, occurs when a computer program such as a software application or an operating system stops functioning properly and exits.

--

### Introducing Try/Except

```py
try:
  n = int( input("Enter a number: ") )
except:
  print("Sorry, that can't be converted to an integer")
```

Every `try` block must have an `except` block.
<!-- .element: class="fragment" -->

--

### What Could Go Wrong?

```py
def divide_ten():
  string = input("Enter a divisor: ")
  number = int( string )
  dividend = str(10 / number)
  print( "Result: " + dividend )
```

ValueError: invalid literal for int() with base 10
<!-- .element: class="fragment" style="color:#ff4048" -->

ZeroDivisionError: division by zero
<!-- .element: class="fragment" style="color:#ff4048" -->

--

### Handle Specific Errors

```py
try:
  divide_ten()
except ValueError:
  print("ERROR: could not convert input to an integer")
except ZeroDivisionError:
  print("ERROR: divisor must not be zero")
except:
  print("ERROR: something unexpected happened")
```

--

### Example: Handling Files

```py
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```
<!-- https://www.w3schools.com/python/python_try_except.asp -->

---

## Else

Use the `else` keyword to define a block of code that is executed _if no errors were raised_.

`else` block must be **after** the `try`/`except` blocks.
<!-- .element: class="fragment" -->

`else` block is **optional**.
<!-- .element: class="fragment" -->

--

### Example: Convert a Number

```py
try:
  n = int( input("Enter a number: ") )
except:
  print("Sorry, that can't be converted to an integer")
else:
  print("Good pick, " + str(n) + " is a great number!")
```

---

## Finally

The `finally` block will be executed regardless if the `try` block raises an error or not.

`finally` block must be **after** the `try`/`except`/`else` blocks.
<!-- .element: class="fragment" -->

`finally` is **optional**.
<!-- .element: class="fragment" -->

--

### Example: Convert a Number

```py
try:
  n = int( input("Enter a number: ") )
except:
  print("Sorry, that can't be converted to an integer")
else:
  print("Good pick, " + str(n) + " is a great number!")
finally:
  print("All done. Goodbye!")
```

--

### Example: File Handling

```py
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```

---

## Review

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDQxcms4anE3dXozcTV6bzlydjkxNGVveWVtcGpwbGZ2dDhtNXg5MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3vRioHcAYTTZbXQA/giphy.webp) <!-- .element: style="height:400px" -->

--

### Is an Error the Same as an Exception?

Yes! (in Python)
<!-- .element: class="fragment" -->

--

### What is an **Unhandled** Exception?

An exception that has not been handled (doh) and causes the program to crash.
<!-- .element: class="fragment" -->

--

### Are All Bugs Exceptions?

No! Consider the following example:
<!-- .element: class="fragment" -->

```py
first = input("First name: ")
last = input("Last name:")
print("Hello, " + first + first + "!")
```
<!-- .element: class="fragment" -->

--

### Do All `try` Blocks Need an `except` Block?

Yes!
<!-- .element: class="fragment" -->

--

### Why Might You Want Multiple `except` Blocks?

To handle different kinds of exceptions.
<!-- .element: class="fragment" -->

--

### What Does the `else` Block Do After `try`/`except`?

Executes code only if the `try` block did not raise an exception.
<!-- .element: class="fragment" -->

--

### What Does the `finally` Block Do?

Executes code regardless of whether an exception was raised.
<!-- .element: class="fragment" -->

---

## Exercise

Write a program that does the following:

- Ask user for file name
- Open the file in read (text) mode
- Print the contents of the file
- Use `try`/`except` to prevent crash if the file does not exist
