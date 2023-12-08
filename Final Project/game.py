import pygame
import sys
from player import *

class Game:
    # Constants
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    GRAVITY = 0.5
    JUMP_HEIGHT = -20
    PLAYER_SPEED = 7
    

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    def __init__(self, level=1):
        self.hero = Player(50, self.WIDTH // 2 - 50 // 2, self.HEIGHT // 2 - 50 // 2, 0, 0)
        self.level = level
        self.level_platforms = [[(300, 300, 200, 20), (400, 400, 100, 20)],
                         [(200, 200, 100, 20)]]
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 60

        self.background_img = pygame.image.load("images/Game_Background.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.WIDTH, self.HEIGHT))

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Low Gravity Platformer")
    
     # Collision detection with platforms
    def checkCollision(self, platforms):
            for platform in platforms:
                if (
                    self.hero.get_x() < platform[0] + platform[2]
                    and self.hero.get_x() + self.hero.get_size() > platform[0]
                    and self.hero.get_y() < platform[1] + platform[3]
                    and self.hero.get_y() + self.hero.get_size() > platform[1]
                ):
                    # Collision occurred, stop falling/jumping
                    self.hero.set_y_speed(0)
                    self.hero.set_y(platform[1] - self.hero.get_size())

                    #Last platform in list is objective platform
                    if platform[0] == platforms[-1][0]:
                        self.level += 1
                        game.WIDTH += 100
                        game.HEIGHT += 100
                        self.background_img = pygame.transform.scale(self.background_img, (self.WIDTH, self.HEIGHT))
                        game.screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
                        game.hero.set_y(game.HEIGHT - 100)


    def drawPlatforms(self):
        for platform in self.level_platforms[self.level - 1]:
            pygame.draw.rect(self.screen, (0, 0, 0), platform)

    def run(self):
        # Create the game window
        clock = pygame.time.Clock()
        pygame.init()

        # Main game loop
        while True:
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Jump when space is pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.hero.set_y_speed(self.JUMP_HEIGHT)

            # Handle left and right movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.hero.set_x_speed(-(self.PLAYER_SPEED))
            elif keys[pygame.K_RIGHT]:
                self.hero.set_x_speed(self.PLAYER_SPEED)
            else:
                self.hero.set_x_speed(0)

            # Apply gravity and movement
            self.hero.increase_y_speed(self.GRAVITY)
            self.hero.move_x()
            self.hero.move_y()

            # Keep the player within the screen bounds
            if self.hero.get_y() > self.HEIGHT - self.hero.get_size():
                self.hero.set_y(self.HEIGHT - self.hero.get_size())
                self.hero.set_y_speed(0)

            if self.hero.get_x() < 0:
                self.hero.set_x(0)
            elif self.hero.get_x() > self.WIDTH - self.hero.get_size():
                self.hero.set_x(self.WIDTH - self.hero.get_size())

            # Draw the background
            self.screen.blit(self.background_img, (0, 0))

            # Draw the player
            pygame.draw.rect(self.screen, self.RED, (self.hero.get_x(), self.hero.get_y(), self.hero.get_size(), self.hero.get_size()))

            #Draw Rectangles
            self.drawPlatforms()

            #Check Platform Collisions
            self.checkCollision(self.level_platforms[self.level - 1])

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(self.FPS)

game = Game()   
game.run()