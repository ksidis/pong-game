import random

from pygame.draw import circle
from pygame.surface import Surface

from constants import *


class Ball:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.position: Point = Point(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.radius: int = BALL_RADIUS
        self.x_vel: int = random.choice((-1, 1))* BALL_MAX_VELOCITY
        self.y_vel: int = 0

    def draw(self):
        circle(self.screen, WHITE, (self.position.x, self.position.y), self.radius)

    def move(self):
        self.position.x += self.x_vel
        self.position.y += self.y_vel

