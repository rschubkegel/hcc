---
name: "Flappy Bird 4"
title: "Flappy Bird: Part 4"
startDate: 2025-01-09
endDate: 2025-01-22
---

In [part 3](/2024/fall/computer-science/assignments/flappy-bird-3), you added scrolling pipes. In this final part, you will allow the bird to collide with the pipes!

- [Detect collision](#detecting-collisions)
- End game if collision occurs
- [Track score](#tracking-score)
- [Show score](#rendering-text)

<details>
<summary>Extra Challenge (optional)</summary>

Instead of exiting the program, show an "end game" screen:

- Stop moving the pipes and the bird
- Show a "Game Over" message

</details>

## Detecting Collisions

Review the [slideshow on collisions](/2024/fall/computer-science/slides/pygame-collisions). Remember that you'll have to check four conditions:

- Left edge of the pipe and the right edge of the bird
- Right edge of the pipe and the left edge of the bird
- Bottom of the top pipe and top of the bird
- Top of the bottom pipe and bottom of the bird

As an example, here's a sketch of the first condition you'll be checking:

![](/2024/fall/computer-science/images/collisions/sketch-of-x-intersection.png)

And here is the code to check it (you may have to adjust the calculations):

```py
# Calculate right/left sides of pipe (rectangle) hitbox
pipe_right = pipe_x + PIPE_WIDTH
pipe_left = pipe_x

# Calculate right/left sides of bird (circle) hitbox
bird_right = bird_x + BIRD_SIZE / 2
bird_left = bird_x - BIRD_SIZE / 2

# Check if there is a collision in the X dimension
x_intersects = pipe_left < bird_right and pipe_right > bird_left
```

## Tracking Score

You can keep track of the score in a couple of different ways:

- Increase score every frame
- Increase score every time the player passes a pipe

Either way, you need to make the score _increase_ as the game continues.

## Rendering Text

Rendering text in Pygame is a three-step process:

1. Create a _font_
2. Use font to render text to a _surface_
3. "Blit" the surface to the screen

Here's what those steps look like:

```py
# Create a font object (using the default font)
size = 32
font = pygame.font.Font(None, size)

# Render text to a surface
text = f"Score: {score}"
antialiased = True
color = (0, 0, 0)
rendered_text = font.render(text, antialiased, color)

# Blit the surface to the screen
coordinates = (16, 16)
game_window.blit(rendered_text, coordinates)
```

**Remember**: you will need to re-draw the text every frame.

See the [`pygame.font` documentation](https://www.pygame.org/docs/ref/font.html) for more info.

## Submit Assignment

When your program meets the requirements, submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSf5PBm4ue9U8E0pTnEdFmKtfiVipYoOqRH3DSw0XBKZeqdoYw/viewform?usp=header" target="_blank" class="button">Submit Assignment</a>
</p>
