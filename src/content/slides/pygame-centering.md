---
title: 'Python - Centering Drawings'
date: 2024-12-19
---

# Pygame - Centering Drawings <!-- .element: class="r-fit-text" -->

Week 15

---

## Review

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDd6azlhbTA5eWNmcW01MnIzdng4aGM3ZGw4c3F6c2xpNHQ0MHBrNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jfa07ySDdvmFzeqCek/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is "state"?

The current **status** of a program, stored in **variables**.
<!-- .element: class="fragment" -->

--

### Where in a program do you define state variables?

```py
# Import modules
# Define constants
# 👉🏻 Define game state variables 👈🏻
# Define functions
# Initialize Pygame
# Main game loop
```
<!-- .element: class="fragment" -->

--

### What are the two types of inputs in Pygame?

- Discrete inputs (once-per-frame)
<!-- .element: class="fragment" -->
- Continuous inputs (holding down a key)
<!-- .element: class="fragment" -->

--

### How do you know how fast an object is moving?

Velocity = Distance / Time.
<!-- .element: class="fragment" -->

Pixels * FPS
<!-- .element: class="fragment" -->

--

### How can we ensure an object moves the same speed on every computer?

```py [1-2|5-6]
FPS = 30
clock = pygame.time.Clock()
running = True
while running:
    player_x += 10
    clock.tick(FPS)
```

---

## Centering Things

![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjBpdzNmNGh3ZmM2bXQycGNzbXM2MWVldDlkZTJvY3N5MzZjdXpzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QFypAZbq5lz3i/200.webp) <!-- .element: style="height:400px" -->

--

### Where are the corners of this rectangle?

```py
x = 100
y = 100
width = 50
height = 50
pygame.draw.rect(screen, color, (x, y, width, height))
```

- Top-left corner **(100, 100)** <!-- .element: class="fragment" -->
- Top-right corner **(150, 100)** <!-- .element: class="fragment" -->
- Bottom-left corner **(100, 150)** <!-- .element: class="fragment" -->
- Bottom-right corner **(150, 150)** <!-- .element: class="fragment" -->

--

### Where is the center of this rectangle?

```py
x = 100
y = 100
width = 50
height = 50
pygame.draw.rect(screen, color, (x, y, width, height))
```

**(125, 125)**
<!-- .element: class="fragment" -->

--

### How to calculate the center?

![](/2024/fall/computer-science/images/centering/dimensions-1.png) <!-- .element: style="height:400px" -->

```py
center_x = x + width / 2  # 25.5
center_y = y + height / 2 # 25.5
```
<!-- .element: class="fragment" -->

--

### How to calculate the center?

![](/2024/fall/computer-science/images/centering/dimensions-2.png) <!-- .element: style="height:400px" -->

```py
center_x = x + width / 2  # 128
center_y = y + height / 2 # 80
```
<!-- .element: class="fragment" -->

--

### How to center a circle?

The x/y coordinates are already in the center!
<!-- .element: class="fragment" -->

```py
pygame.draw.circle(screen, color, (center_x, center_y), radius)
```
<!-- .element: class="fragment" -->

---

### Exercise: Center a Rectangle

Update the "TODO" section in the [starter program](/2024/fall/computer-science/examples/pygame_centering_starter.py)