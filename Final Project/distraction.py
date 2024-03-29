import pygame
from fsm import FSM
"Code Generated by ChatGPT, Edited by Nic Ekstrand"
class Distraction:
    def __init__(self, x, y, size, speed, hero):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.target = hero

        #Create the Bot's finite state machine (self.fsm) with initial state
        self.fsm = FSM("tracking")
        self.init_fsm(self.target)

    def init_fsm(self, hero):
        self.fsm.add_transition("see_player", "tracking", self.track, "tracking")
        self.fsm.add_transition("adderall", "tracking", self.stay_still, "staying_still")
        self.fsm.add_transition("time_up", "staying_still", self.track, "tracking")

    def stay_still(self):
        self.speed = 0

    def track(self):
        self.speed = 1
        # Move towards the target object
        dx = self.target.get_x() - self.x
        dy = self.target.get_y() - self.y
        dist = pygame.math.Vector2(dx, dy).length()

        if dist > 0:
            dx /= dist
            dy /= dist

        self.x += dx * self.speed
        self.y += dy * self.speed

    def update(self, input=None):
        self.fsm.process(input)

    # Getter methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size

    # Setter methods
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_size(self, size):
        self.size = size


