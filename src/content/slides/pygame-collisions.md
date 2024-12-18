---
title: 'Python - Pygame Collisions'
date: 2024-12-19
---

# Pygame - Collisions <!-- .element: class="r-fit-text" -->

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

## Collisions

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWgxNXd1cWpnaDJoM2Q1aDhtNnM5b3FtcXhpd25kMW53N2g2N3JtbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10uxwQ1FLDMCzu/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is a collision?

An intersection of two objecs
<!-- .element: class="fragment" -->

![](/2024/fall/computer-science/images/collisions/bird-hitting-pipe.png) <!-- .element: style="height:400px" -->
<!-- .element: class="fragment" -->

--

### How do we detect a collision?

Checking the boundaries of two objects
<!-- .element: class="fragment" -->

![](/2024/fall/computer-science/images/collisions/sketch-of-game-state.png) <!-- .element: style="height:400px" -->
<!-- .element: class="fragment" -->

--

### Checking the X Dimension

![](/2024/fall/computer-science/images/collisions/sketch-of-x-intersection.png) <!-- .element: style="height:400px" -->

--

### Checking the Y Dimension

![](/2024/fall/computer-science/images/collisions/sketch-of-y-intersection.png) <!-- .element: style="height:400px" -->

--

### What does the code look like?

```py [5|1-4|6-7]
pipe_r = pipe_x + PIPE_WIDTH
pipe_l = pipe_x
bird_r = bird_x + BIRD_SIZE / 2
bird_l = bird_x - BIRD_SIZE / 2
x_intersects = pipe_l < bird_r and pipe_r > bird_l
if x_intersects:
    # TODO: do something
```

Why are bird & pipe dimensions calculated differently?
<!-- .element: class="fragment" -->

---

## Activity: Checking Collisions!

Fill out the function with the "TODO" comment in the [starter project](/2024/fall/computer-science/examples/pygame_collision_starter.py)
