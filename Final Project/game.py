import pygame
import sys
from player import *
from distraction import *

class Game:
    # Constants
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    GRAVITY = 0.5
    JUMP_HEIGHT = -10
    PLAYER_SPEED = 7

    

    #Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    #Constructor
    def __init__(self, level=1):
        #Instance Variables
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.score = 100
        self.hero = Player(25, self.WIDTH // 2 - 50 // 2, self.HEIGHT // 2 - 50 // 2, 0, 0)
        self.distraction = Distraction(self.WIDTH // 2 - 50 // 2, 0, 25, 1, self.hero)
        self.level = level
        self.level_platforms = [[(300, 300, 200, 20), (400, 400, 100, 20), (150, 200, 100, 20), (150, 100, 75, 10), (500, 500, 30, 20), (50, 50, 50, 20)],
                         [(400, 250, 100, 20), (100, 600, 80, 20), (300, 550, 50, 20), (100, 450, 40, 20), (200, 375, 100, 20), (500, 150, 100, 20), (650, 50, 40, 20)],
                         [(300, 750, 50, 10), (500, 650, 100, 10), (750, 550, 30, 10), (500, 450, 100, 10), (500, 350, 50, 10), (500, 250, 10, 10), (100, 540, 50, 20)],
                         [(0, 800, 40, 20), (200, 700, 40, 20), (0, 600, 40, 20), (201, 500, 40, 20), (400, 500, 40, 20), (500, 400, 40, 20), (800, 700, 40, 20), (1000, 600, 40, 20)],
                         [(400, 900, 30, 20), (300, 800, 30, 20), (200, 700, 30, 20), (100, 600, 30, 20), (300, 500, 30, 20), (200, 400, 30, 20), (200, 300, 30, 20), (0, 200, 20, 10), (500, 800, 30, 20), 
                          (600, 700, 30, 20), (900, 700, 30, 10), (1000, 600, 30, 10), (1001, 500, 30, 10)]]
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 60

        #Makes Pygame window
        self.background_img = pygame.image.load("images/Game_Background.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.WIDTH, self.HEIGHT))
        self.distraction_img = pygame.image.load("images/Youtube.png")
        self.distraction_img = pygame.transform.scale(self.background_img, (self.WIDTH, self.HEIGHT))

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("CogniClimb")
    
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

    def checkSingleCollision(self, thing):
        if (
            self.hero.get_x() < thing.get_x() + thing.get_size()
            and self.hero.get_x() + self.hero.get_size() > thing.get_x()
            and self.hero.get_y() < thing.get_y() + thing.get_size()
            and self.hero.get_y() + self.hero.get_size() > thing.get_y()
            ):
            self.score -= 1

    def drawPlatforms(self):
        for platform in self.level_platforms[self.level - 1]:
            pygame.draw.rect(self.screen, (13, 181, 24), platform)

    def run(self):
        # Create the game window
        clock = pygame.time.Clock()
        pygame.init()
        pygame.mixer.init()

        # Set up font
        font = pygame.font.Font(None, 36)

        # Load a sound file
        pygame.mixer.music.load("music/Cherry_Tree.mp3")      

        #Play Music
        pygame.mixer.music.play(-1)
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

            # Draw the player and distraction
            pygame.draw.rect(self.screen, self.RED, (self.hero.get_x(), self.hero.get_y(), self.hero.get_size(), self.hero.get_size()))
            pygame.draw.rect(self.screen, self.RED, (self.distraction.get_x(), self.distraction.get_y(), self.distraction.get_size(), self.distraction.get_size()))

            #Draw Rectangles
            self.drawPlatforms()

            #Check Platform Collisions
            self.checkCollision(self.level_platforms[self.level - 1])
            self.checkSingleCollision(self.distraction)
            self.checkSingleCollision()

            #Draw Score and Day
            self.screen.blit(font.render(str(self.score), True, (0, 0, 0)), (10, 0))
            self.screen.blit(font.render(self.days[self.level - 1], True, (0, 0, 0)), (self.WIDTH / 2 - 50, 0))

            #FSM Processing
            self.distraction.fsm.process("see_player")

            #Draw Distractions
            pygame.draw.rect(self.screen, (235, 213, 52), (self.distraction.get_x(), self.distraction.get_y(), self.distraction.get_size(), self.distraction.get_size()))

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(self.FPS)

game = Game()   
game.run()