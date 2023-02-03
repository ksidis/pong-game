from dataclasses import dataclass


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 60

BALL_RADIUS = SCREEN_HEIGHT // 50
BALL_MAX_VELOCITY = 5

PADDLE_WIDTH = 20
PADDLE_HEIGHT = SCREEN_HEIGHT // 8
PADDLE_VELOCITY = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



@dataclass
class Point:
    x: int
    y: int
