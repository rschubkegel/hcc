---
name: "Flappy Bird 3"
title: "Flappy Bird: Part 3"
startDate: 2024-12-19
endDate: 2025-01-09
---

In [part 2](/2024/fall/computer-science/assignments/flappy-bird-2), you added movement to your bird. In this final part, you will add the pipes and collision detection!

- Draw pipes
- Move pipes
- [Detect collision](#detecting-collisions)
- End game if collision occurs

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
pipe_right = pipe_x + PIPE_WIDTH
pipe_left = pipe_x
bird_right = bird_x + BIRD_SIZE / 2
bird_left = bird_x - BIRD_SIZE / 2
x_intersects = pipe_left < bird_right and pipe_right > bird_left
```

## Submit Assignment

When your program meets the requirements, submit your `.py` file here:

<p style="text-align:center">
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSf5PBm4ue9U8E0pTnEdFmKtfiVipYoOqRH3DSw0XBKZeqdoYw/viewform?usp=header" target="_blank" class="button">Submit Assignment</a>
</p>
