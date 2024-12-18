# Import modules
import pygame

# Define constants
SCREEN_W = 600
SCREEN_H = 300
FPS = 30

COLOR_DARK_BLUE = (75, 75, 130)
COLOR_BLUE = (220, 220, 255)

BASE_SIZE = 10

# Define game state variables
last_mouse_x = SCREEN_W / 2
last_mouse_y = SCREEN_H / 2
width = BASE_SIZE
height = BASE_SIZE

# Define functions

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle discrete events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate difference between current mouse position and previous frame's
    dx = mouse_x - last_mouse_x
    dy = mouse_y - last_mouse_y

    # Remember position so it can be compared with next frame
    last_mouse_x = mouse_x
    last_mouse_y = mouse_y

    # Adjust rectangle size based on mouse speed
    width = BASE_SIZE + (abs(dx) / 3)
    height = BASE_SIZE + (abs(dy) / 3)

    # Fill screen to clear last frame
    screen.fill(COLOR_DARK_BLUE)

    # Draw the rectangle
    # TODO: change the position so that the rectangle is centered on the mouse
    pygame.draw.rect(screen, COLOR_BLUE, (mouse_x, mouse_y, width, height))

    # Put the stuff we drew on the window
    pygame.display.flip()

    # Limit frame rate
    clock.tick(FPS)