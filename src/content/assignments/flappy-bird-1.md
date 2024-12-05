---
name: "Flappy Bird 1"
title: "Flappy Bird: Part 1"
startDate: 2024-12-05
endDate: 2024-12-11
---

Flappy Bird is a classic game where the player controls a bird and tries to avoid obstacles. In this assignment, you will create a simple version of Flappy Bird using Python and Pygame.

The project will be split into three weeks but **you must submit the program each week**. This week, you will get familiar with drawing graphics using basic shapes.

- Define a function to draw a bird
  - Use [basic shapes](#drawing-shapes) to compose a simple bird
  - Combine at least 3 basic shapes
  - Make sure to use more than one type of shape (i.e. don't _only_ use rectangles)
- Call the function in your main game loop

## Pygame

[Pygame](https://www.pygame.org/news) is a Python library for creating games. It provides a set of functions and classes that make it easy to create graphics and sound for your game.

### Install for Replit

![](/2024/fall/computer-science/images/flappy-bird/replit-project-config.png)

Open `project.toml` and update the `[tool.poetry.dependencies]` section to match the following:

```toml
[tool.poetry.dependencies]
python = ">=3.10.0,<3.12"
pygame = "^2.1.2"
dearpygui = "^1.6.2"
```

Next time you run a project, Replit will automatically install the required packages.

### Install for VSCode

Open Command Prompt (_View_ > _Terminal_ or <kbd>Ctrl</kbd> + <kbd>\`</kbd>) and run the following:

```cmd
pip install pygame
```

Now you can import the `pygame` module in your Python code!

## Project Structure

This project will be larger than previous projects which makes it important to _organize the code_. Here is the basic structure your program should follow:

- Import modules
- Define constants
- Define functions
- ~~Define game variables~~ (will do this next week)
- Initialize Pygame
- Main game loop

Here is a basic template for you to start with:

```python
# Import modules
import pygame

# Define constants (using CAPS_CASE convention)
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 180

# Initialize Pygame
pygame.init()
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# TODO: Define functions here

# Game loop
running = True
while running:
    # Handle events (allows the user to quit the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background color
    game_window.fill(WHITE)

    # TODO: Call functions here

    # Render graphics to window
    pygame.display.flip()
```

## Drawing Shapes

Pygame provides a set of functions that you can use to draw shapes on the screen. Here are some examples:

```python
# Draw a rectangle
color = (255, 0, 0)
x = 100
y = 100
width = 50
height = 50
pygame.draw.rect(game_window, color, (x, y, width, height))

# Draw a circle
color = (0, 255, 0)
x = 100
y = 100
radius = 50
pygame.draw.circle(game_window, color, (x, y), radius)

# Draw a line
color = (0, 0, 255)
start_x = 0
start_y = 0
end_x = 100
end_y = 100
pygame.draw.line(game_window, color, (start_x, start_y), (end_x, end_y))
```

Use these functions to draw a bird your new function!

![](/2024/fall/computer-science/images/flappy-bird/shapes-bird.png)

> NOTE: Feel free to customize the bird to your liking, it doesn't have to look like mine!

### Colors

In Pygame, colors are represented by tuples of three integers (RGB) where each integer ranges from 0 to 255. For example, `(0, 0, 0)` is black, `(255, 255, 255)` is white, and `(255, 0, 0)` is red.

To define a color that you like, you can use a color picker ([this one](https://www.w3schools.com/colors/colors_picker.asp) from W3Schools is good) and copy the RGB values.

![](/2024/fall/computer-science/images/flappy-bird/color-picker.png)

## Submit Assignment

When your program meets the requirements, submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLScYDoMGO8Nq9oymqr2b7rE4NbYHnIQnNmz6JIL2bpx-U0itDA/viewform?usp=sf_link" target="_blank" class="button">Submit Assignment</a>
</p>
