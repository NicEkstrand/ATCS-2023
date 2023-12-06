import pygame
import sys
from player import *

# Initialize Pygame
pygame.init()

class Game:
    def __init__(self, level, width, height):
        self.level = level
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

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
game = Game(1, 800, 600)

print(hero)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Low Gravity Platformer")
clock = pygame.time.Clock()

# Collision detection with platforms
def checkCollision(platforms):
    num = 0
    for platform in platforms:
        if (
            hero.get_x() < platform[0] + platform[2]
            and hero.get_x() + hero.get_size() > platform[0]
            and hero.get_y() < platform[1] + platform[3]
            and hero.get_y() + hero.get_size() > platform[1]
        ):
            # Collision occurred, stop falling/jumping
            hero.set_y_speed(0)
            hero.set_y(platform[1] - hero.get_size())
            num += 1


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Jump when space is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hero.set_y_speed(JUMP_HEIGHT)

    # Handle left and right movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.set_x_speed(-PLAYER_SPEED)
    elif keys[pygame.K_RIGHT]:
        hero.set_x_speed(PLAYER_SPEED)
    else:
        hero.set_x_speed(0)

    # Apply gravity
    hero.increase_y_speed(GRAVITY)
    hero.move_x()
    hero.move_y()

    
   

    # Keep the player within the screen bounds
    if hero.get_y() > HEIGHT - hero.get_size():
        hero.set_y(HEIGHT - hero.get_size())
        hero.set_y_speed(0)

    if hero.get_x() < 0:
        hero.set_x(0)
    elif hero.get_x() > WIDTH - hero.get_size():
        hero.set_x(WIDTH - player_size)

    # Draw the background
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (hero.get_x(), hero.get_y(), hero.get_size(), hero.get_size()))

    #Draw Rectangles
    lvl1_rects = [(300, 300, 200, 20)]
    pygame.draw.rect(screen, (0, 0, 0), (lvl1_rects[0]))

    #Check Platform Collisions
    checkCollision(lvl1_rects)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
