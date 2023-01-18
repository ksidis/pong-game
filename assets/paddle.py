import pygame.draw
from pygame.surface import Surface

from constants import *


class Paddle:
    def __init__(self, screen: Surface, x: int, y: int, width: int, height: int):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, up: bool = True):
        if up:
            self.y -= PADDLE_VELOCITY
        else:
            self.y += PADDLE_VELOCITY
