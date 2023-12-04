import pygame
import sys
from player import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_HEIGHT = -20
PLAYER_SPEED = 7

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_velocity_y = 0
player_velocity_x = 0

hero = Player(50, WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, 0, 0)

print(hero)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Low Gravity Platformer")
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Jump when space is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_velocity_y = JUMP_HEIGHT

    # Handle left and right movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_velocity_x = -PLAYER_SPEED
    elif keys[pygame.K_RIGHT]:
        player_velocity_x = PLAYER_SPEED
    else:
        player_velocity_x = 0

    # Apply gravity
    player_velocity_y += GRAVITY
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Keep the player within the screen bounds
    if player_y > HEIGHT - player_size:
        player_y = HEIGHT - player_size
        player_velocity_y = 0

    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Draw the background
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (hero.get_x(), hero.get_y(), hero.get_size(), hero.get_size()))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
