---
title: 'Python - Modules'
date: 2024-10-10
---

# Python Modules <!-- .element: class="r-fit-text" -->

Week 6

---

## Review

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG50MHRzend2b2E1ZzNzdDFjb3h1dzNrcXR4Y2dyeDhmdWhwMzRjbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WRQBXSCnEFJIuxktnw/giphy.webp) <!-- .element: style="height:400px" -->

--

### Anatomy of a Function

```py [1|2|3]
def add(num1, num2):
  sum = num1 + num2
  return sum
print( add(2, 3) )
```

NOTES:
- What are the variables in the definition called? Parameters (or arguments).
- Is the variable "sum" accessible outside the function? No.
- What is it called when you use a function? "Calling a Function".

---

## Modules

![](https://i.giphy.com/SIMKP4dNU5znPHWSVZ.webp) <!-- .element: style="height:400px" -->

--

### What is a module?

A module is another Python file.
<!-- .element: class="fragment" -->

NOTES:
- Typically modules just define variables and functions.
- We are doing something out of the ordinary to avoid paying for Replit.

--

### Importing an Entire Module

```py
import random

print( random.randint(1, 10) )
```

--

### Using an Import Alias

```py
import random as rand

print( rand.randint(1, 10) )
```

--

### Importing Everything from a Module

```py
from random import *

print( randint(1, 10) )
```

--

### Importing Part of a Module

```py
from random import random, randint

print( random() )
print( randint(1, 10) )
```

--

### Using an Import Alias

```py
from random import random as randfloat

print( randfloat() )
```

--

### Best Practices

- Import before anything else <!-- .element: class="fragment" -->
- Use namespaces <!-- .element: class="fragment" -->

---

## Common Built-in Modules

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2tyaGg4OWZtNnQzdWw0dm4wcHJ3czJuZTAzMWE1cTNpcWk2Y2x1YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wzqCepiFLXVPujU74f/giphy.webp) <!-- .element: style="height:400px" -->

--

### `random`

```py
import random

# 0.0 - 1.0
random.random()

# 1 - 10
random.randint(1, 10)

# "Nash" or "Kylan"
random.choice(['Nash', 'Kylan'])
```

--

### `math`

```py
import math

# 3.141592653589793
math.pi

# 256.0
math.pow(2, 8)

# 4.0
math.sqrt(16)
```

--

### `datetime`

```py
import datetime

now = datetime.datetime.now()

# 2024
now.year

# 10
now.month

# 10
now.day
```

---

## Activity: Multiple Modules <!-- .element: class="r-fit-text" -->

- Utilize at least 3 built-in modules
- Define and call at least 1 function
  - Must have at least 1 parameter
- Get creative 🎨
