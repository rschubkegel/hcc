# Import modules
import pygame


# Define constants
SCREEN_W = 600
SCREEN_H = 300
FPS = 30
BOX_SIZE = 50
MOVE_SPEED = 5

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (200, 50, 50)
COLOR_GREEN = (50, 200, 50)
COLOR_BLUE = (50, 50, 200)

TEXT_SIZE = 32
TEXT_MARGIN = 16


# Define game state variables
player_x = SCREEN_W / 3
player_y = SCREEN_H / 3
box_x = SCREEN_W * 2 / 3
box_y = SCREEN_H * 2 / 3


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
font = pygame.font.Font(None, TEXT_SIZE)


# Function to check of boxes are colliding.
# Returns a boolean value.
def are_boxes_colliding():
    player_left = player_x
    player_right = player_x + BOX_SIZE
    box_left = box_x
    box_right = box_x + BOX_SIZE
    x_intersection = player_left < box_right and player_right > box_left

    player_top = player_y
    player_bottom = player_y + BOX_SIZE
    box_top = box_y
    box_bottom = box_y + BOX_SIZE
    y_intersection = player_bottom > box_top and player_top < box_bottom

    return x_intersection and y_intersection


# Function to render text representing current game state.
def draw_state(colliding):
    # Render text to a surface
    text = f"Player: ({player_x}, {player_y})"
    rendered_text = font.render(text, True, COLOR_WHITE)

    # Blit the surface to the screen
    coordinates = (TEXT_MARGIN, TEXT_MARGIN)
    screen.blit(rendered_text, coordinates)

    # Render text to a surface
    text = f"Colliding? {colliding}"
    rendered_text = font.render(text, True, COLOR_WHITE)

    # Blit the surface to the screen
    coordinates = (TEXT_MARGIN, TEXT_MARGIN + TEXT_SIZE)
    screen.blit(rendered_text, coordinates)


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
        box_color = COLOR_RED
    else:
        box_color = COLOR_BLUE

    # Draw stuff on screen
    screen.fill(COLOR_BLACK)
    pygame.draw.rect(screen, COLOR_GREEN, (player_x, player_y, BOX_SIZE, BOX_SIZE))
    pygame.draw.rect(screen, box_color, (box_x, box_y, BOX_SIZE, BOX_SIZE))
    draw_state(is_colliding)
    pygame.display.flip()

    # Limit frame rate
    clock.tick(FPS)
