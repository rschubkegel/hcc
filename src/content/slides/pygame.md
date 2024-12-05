---
title: 'Python - Pygame'
date: 2024-12-05
---

# Pygame Package <!-- .element: class="r-fit-text" -->

Week 13

---

## Package Management

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDQ2NnRsMHA2cG05NmV3eDhiYWZ1NnBsdjNjM3J6czduZmRhYmUyYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wEhdsAyB3Ijza4AL7L/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is a "Package"?

It's a module...

...which is a collection of Python code

NOTE: sometimes packages are called libraries

--

### "3rd Party" Modules

A module that is not part of the Python standard library

Must be downloaded before it can be imported <!-- .element: class="fragment" -->

NOTE: installing your `.py` assignments is like installing a 3rd party module

--

### Package Versions

Versioniong is **very** important with packages

- Reproducibility <!-- .element: class="fragment" -->
- Prevent Conflicts <!-- .element: class="fragment" -->
- Rollbacks <!-- .element: class="fragment" -->

NOTES:
- If you download an old version of a package on a new computer, the program may not work
- Another package may use a different version of the same package
- If you know version 1 worked but 2 doesn't, you know to roll back to 1

--

### Installing a 3rd Party Module

- On local machine
  - `pip install <package_name>` <!-- .element: class="fragment" -->
- On Replit
  - Edit `pyproject.toml` <!-- .element: class="fragment" -->
  - Add via "Dependencies" window <!-- .element: class="fragment" -->

--

### 🛑

Time to try it out!

---

## Setting Up

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTVhNjhxcnQ3NzJrc29xNGl4aXRta2w2eDMxNHN6bXdvaDgyNGpwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6UL3rqweR5Y2Jcrnqb/giphy.webp) <!-- .element: style="height:400px" -->

--

### Constants

A constant is a variable whose value never changes\*

\*at least, it is not _intended_ to change

NOTE: in other languages, an error is thrown if you try to change a constant

--

### Naming Conventions

- Use `snake_case` for regular variables
- Use `CAPS_CASE` for constants

--

### Initializing Pygame

```py [1|2|3]
import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
```

Pop-quiz: what kind of data structure uses parenthesis? **Tuple** <!-- .element: class="fragment" -->
<!-- .element: class="fragment" -->

--

### 🛑

Time to try it out!

---

## Game Loop

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWZ2bGhpdjNpNmJleTZsazMxcHdkMXVqd2l0c3lsenJ6dTRidTI4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/y48ib4qzgCjyvdg2Gh/giphy.webp) <!-- .element: style="height:400px" -->

--

### Loop Until Done

```py
# Initialization here

running = True
while running:
    # TODO: game loop contents

# Cleanup here
```

NOTE: game loop called as often as possible (will control FPS next week)

--

### Events

In Pygame you must check for events like mouse clicks, key presses, etc.

```py
running = True
while running:
    for event in pygame.event.get():
        # TODO: handle event based on type
```

--

#### Quit Event

When user presses the "X" button on the window

```py
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

--

#### 🛑

Time to try it out!

--

### Drawing

`pygame.draw` is a collection of functions that draw shapes on the window

- Fill window (erases previous frame) <!-- .element: class="fragment" -->
- Draw content (background to foreground) <!-- .element: class="fragment" -->
- Update screen <!-- .element: class="fragment" -->

--

### Drawing a Rectangle

The `pygame.draw.rect` function takes three arguments:

- "Surface" to draw on (in this case the game window)
- Color (R, G, B)
- "Rectangle" (x, y, width, height)

```py
running = True
while running:
    pygame.draw.rect(game_window, (255, 0, 0), (100, 100, 20, 10))
```

--

#### Drawing a Rectangle with Constants

```py
RED = (255, 0, 0)
X = 100
Y = 100
WIDTH = 20
HEIGHT = 10
RECT = (X, Y, WIDTH, HEIGHT)

running = True
while running:
    pygame.draw.rect(game_window, RED, RECT)
```

--

#### 🛑

Time to try it out!

---

## Activity: Composite Shapes

- Rectangle with an outline
- Use loop to draw multiple rectangles