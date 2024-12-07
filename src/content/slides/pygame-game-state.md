---
title: 'Python - Pygame State Variables'
date: 2024-12-05
---

# Pygame - State Variables <!-- .element: class="r-fit-text" -->

Week 14

---

## Review

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjhlaHVsYm11MGNrcXcydzlweTAxZjJpNXJxcGhrZ2RuZjVxZmNrbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0dUSXH2kWrm3GPh4Q/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is a package?

It's a _module_ which is a collection of Python code.
<!-- .element: class="fragment" -->

--

### What is a "3rd Party" module?

A module that is not part of the Python standard library.
<!-- .element: class="fragment" -->

It must be installed before use.
<!-- .element: class="fragment" -->

--

### Why are package versions important?

Security, conflict prevention, rollbacks, etc.
<!-- .element: class="fragment" -->

--

### What is a "constant?"

A constant is a variable whose value never changes\*
<!-- .element: class="fragment" -->

\*at least, it is not _intended_ to change
<!-- .element: class="fragment" -->

--

### What is the naming convention for constants?

`CAPS_CASE` <!-- .element: class="fragment" -->

--

### What is the basic structure of a Pygame program?

1. Import modules <!-- .element: class="fragment" -->
2. Define constants <!-- .element: class="fragment" -->
3. Define functions <!-- .element: class="fragment" -->
4. Define game variables <!-- .element: class="fragment" -->
5. Initialize Pygame <!-- .element: class="fragment" -->
6. Main game loop <!-- .element: class="fragment" -->

--

### What goes in the game loop?

1. Event handling <!-- .element: class="fragment" -->
2. Drawing <!-- .element: class="fragment" -->

--

### What three things need to happen (in the game loop) in order to draw on the screen?

- Clear screen <!-- .element: class="fragment" -->
- Draw shapes <!-- .element: class="fragment" -->
- Update screen <!-- .element: class="fragment" -->

---

## State Variables

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWNvOGZrcmU3aG5udWMwNDhwZW8waDhqOWlzMnZxbml6Y3B0NWl4diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f6gpUL2BgvJSOBMQV2/giphy.webp) <!-- .element: style="height:400px" -->

--

### What is "State?"

The current status of a program.

--

### Example: Text Editor

- Cursor position <!-- .element: class="fragment" -->
- Text selection <!-- .element: class="fragment" -->
- Word count <!-- .element: class="fragment" -->

--

### Example: Game

- Player position <!-- .element: class="fragment" -->
- Score <!-- .element: class="fragment" -->
- Paused / playing <!-- .element: class="fragment" -->

---

## Pygame State

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzA3dTN5djR4bmM4MmNiMW56dmlraW5hYmhodzZvZ2lrYTFpMTVnaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iFCsF4HIdyTEhy66rF/giphy.webp) <!-- .element: style="height:400px" -->

--

### Defining State

```py [5-7]
# Import modules
# Define constants
# Define functions

# Define game variables
player_x = 0
score = 0

# Initialize Pygame
# Main game loop
```

--

### Updating State

```py [4|5-6|7-8]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT
                player_x += 10
            elif event.key == pygame.K_LEFT
                player_x -= 10
  # TODO: draw game based on state
```

--

### Using State

```py [5-10]
running = True
while running:
    # TODO: update state
    game_window.fill(game_window, (0, 0, 0))
    pygame.draw.circle(
      game_window,
      (0, 255, 0),
      (player_x, 0),
      10
    )
    pygame.display.flip()
```

---

## Pygame Continuous Input

![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2t2Z29zYzAyamNiMWkwbWZjcDEyZG52dGRwdXR3cW13OWZmbWg3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/y0NFayaBeiWEU/200.webp) <!-- .element: style="height:400px" -->

--

In this example, _when_ does the player move?

```py
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT
                player_x += 10
```

Whenever the player _first presses_ the right arrow key.
<!-- .element: class="fragment" -->

What if the player _holds down_ the key?
<!-- .element: class="fragment" -->

--

### Using Continuous Input

```py
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += 10
```

`get_pressed` returns a dictionary of keys being _held down_.
<!-- .element: class="fragment" -->

--

### `event.get()` vs `key.get_pressed()`

- `event.get()` is for _one-time_ events
- `key.get_pressed()` is for _continuous_ events

- `event.get()` is for mouse, joystick, other events
- `key.get_pressed()` is only for keyboard

---

## Pygame Timing

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHF6dWN5YXNqa3cwZ2N4Y2J5bmF5M2ZjYTYxczZ1YTN2dXV6MnFyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FLTSJQxfI71Ouf2EYY/giphy.webp) <!-- .element: style="height:400px" -->

--

### What does FPS stand for?

Frames per Second. <!-- .element: class="fragment" -->

--

### How often does the game loop run?

As often as the computer/OS allows. <!-- .element: class="fragment" -->

--

### How fast will my character move?

```py
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += 10
```

Depends on the speed of the computer!
<!-- .element: class="fragment" -->

--

### Two Solutions

- Throttle game loop
- Measure frame rate

--

### Throttle Game Loop

```py [1-2|8|7]
FPS = 30
clock = pygame.time.Clock()
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += 10 # 10 * 30 = 300 px / sec
    clock.tick(FPS)
```

---

## Activity: Frogger Movement

- Draw a shape
- Use up/down to jump lanes
- Use left/right to smoothly move left/right