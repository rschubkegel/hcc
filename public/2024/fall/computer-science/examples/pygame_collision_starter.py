# Import modules
import pygame

# Define constants
SCREEN_W = 600
SCREEN_H = 300
BOX_SIZE = 50
MOVE_SPEED = 5

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (200, 50, 50)
COLOR_GREEN = (50, 200, 50)
COLOR_BLUE = (50, 50, 200)

# Define game state variables
player_x = SCREEN_W / 3
player_y = SCREEN_H / 3
box_x = SCREEN_W * 2 / 3
box_y = SCREEN_H * 2 / 3

# Define functions
def are_boxes_colliding():
    # TODO return True if there are collisions
    return False

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

    # Handle continuous input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= MOVE_SPEED
    if keys[pygame.K_s]:
        player_y += MOVE_SPEED
    if keys[pygame.K_a]:
        player_x -= MOVE_SPEED
    if keys[pygame.K_d]:
        player_x += MOVE_SPEED

    # Change box color if there is a collision
    is_colliding = are_boxes_colliding()
    if is_colliding:
        box_color = COLOR_BLUE
    else:
        box_color = COLOR_RED

    # Draw stuff on screen
    screen.fill(COLOR_BLACK)
    pygame.draw.rect(screen, COLOR_GREEN, (player_x, player_y, BOX_SIZE, BOX_SIZE))
    pygame.draw.rect(screen, box_color, (box_x, box_y, BOX_SIZE, BOX_SIZE))
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)