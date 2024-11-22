---
title: 'Python - Functions'
date: 2024-10-03
---

# Python - Functions <!-- .element: class="r-fit-text" -->

Week 5

---

## Review

![](https://i.giphy.com/lrPrJWeMi0qbSjDR1y.webp) <!-- .element: style="height:400px" -->

--

### Loops

- What loops does Python have? <!-- .element: class="fragment" -->
- When should you use each? <!-- .element: class="fragment" -->

--

### Lists

- Are lists a primitive data type? <!-- .element: class="fragment" -->
- What data types can you store in a list? <!-- .element: class="fragment" -->

--

### How to Add to a List

```py
my_list = ["hello"]
my_list.append("world")
```
<!-- .element: class="fragment" -->

--

### How to Remove from a List by Item

```py
my_list = [True, False, True]
my_list.remove(True)
```
<!-- .element: class="fragment" -->

--

### How to Remove from a List by Index

```py
my_list = [3.14, 2.72, 1.62]
my_list.pop(0)
```
<!-- .element: class="fragment" -->

--

### How to Update a List by Index

```py
my_list = ["Al", "is", "crazy"]
my_list[2] = "cool"
```
<!-- .element: class="fragment" -->

---

## Functions

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmathvault.ca%2Fwp-content%2Fuploads%2FSine-Waves.jpg&f=1&nofb=1&ipt=cd2d14e0a563a52a0163fb9942460f2debb66dc594043c2ebc058606c2c120b4&ipo=images) <!-- .element: style="height:400px" -->

--

### What is a function?

```py [1-2|4]
def my_function():
  print("Hello World")

my_function()
```

--

### Defining a Function

Can only have one definition

```py
def my_function():
  print("I am inside the function")
  # check your indentation!
  print("I am also inside the function")
print("I am OUTSIDE the function")
```

--

### Calling a Function

```py
print()
print("I am a function call")
print( input("I will print what you type: ") )
```

--

### Parameters and Arguments

```py
def say_hi(name):
  print("Hello " + name)

say_hi("World")
say_hi("Kylan")
```
NOTES:
Parameters are variables in a function definition;
arguments are values passed to a function when it is called

--

### Return Values

```py
def add(num1, num2):
  return num1 + num2

print( add(2, 3) )
```

--

### Variable Scope

```py [1-3|5|6|7]
def get_text():
  text = input("Type some text: ")
  return text

return_value = get_text()
print(return_value)
print(text)
```

---

## Function Examples

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW12Mmd0dTR0MzIwdXVlMjFvZXBkdmZvdzEyMHI4Ym9nbzdhbTc0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orieS4jfHJaKwkeli/giphy.webp) <!-- .element: style="height:400px" -->

--

```py
def clean_input():
  text = input()
  text = text.strip()
  text = text.lower()
  return text
```

--

```py
def sum(numbers):
  total = 0
  for n in numbers:
    total += n
  return total
```

--

```py
def replace_spaces_with_underscores(string):
  for i in range( len(string) ):
    if string[i] == " ":
      string[i] = "_"
```

---

## Activity: Print a Table <!-- .element: class="r-fit-text" -->

- Create a list variable with multiple items
- Define a function that prints table cells
- Call your function!

```
---------------------
| foo || bar || baz |
---------------------
```