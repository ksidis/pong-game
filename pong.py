import pygame
from pygame.constants import K_ESCAPE, QUIT, K_UP, K_DOWN, K_w, K_s

from assets.ball import Ball
from assets.paddle import Paddle

from constants import *


class Pong:

    def __init__(self):
        pygame.init()

        # Set up the drawing window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = False

        self.ball = Ball(self.screen)
        self.l_paddle = Paddle(self.screen, 10,
                               (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT/2),
                               PADDLE_WIDTH, PADDLE_HEIGHT)
        self.r_paddle = Paddle(self.screen,
                               SCREEN_WIDTH -
                               (10 + PADDLE_WIDTH), (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2),
                               PADDLE_WIDTH, PADDLE_HEIGHT)

    def start(self):
        # Run until the user asks to quit
        self.running = True
        self.clock.tick(FPS)
        self.main_loop()

    def main_loop(self):
        while self.running:
            self.update()

            # Do all drawing
            self.draw()

            # Did the user click the window close button?
            for event in pygame.event.get():
                # Did the user click the window
                # close button? If so, stop the loop.
                if event.type == QUIT:
                    self.running = False
                    break
            keys = pygame.key.get_pressed()
            self.handle_keys(keys, self.l_paddle, self.r_paddle)

        # Done! Time to quit.
        pygame.quit()

    def handle_keys(self, keys, l_paddle, r_paddle):
        if keys[K_w] and l_paddle.y - PADDLE_VELOCITY >= 0:
            l_paddle.move(up=True)
        if keys[K_s] and l_paddle.y + PADDLE_VELOCITY + l_paddle.height <= SCREEN_HEIGHT:
            l_paddle.move(up=False)
        if keys[K_UP] and r_paddle.y - PADDLE_VELOCITY >= 0:
            r_paddle.move(up=True)
        if keys[K_DOWN] and r_paddle.y + PADDLE_VELOCITY + r_paddle.height <= SCREEN_HEIGHT:
            r_paddle.move(up=False)

        if keys[K_ESCAPE]:
            self.running = False

    def update(self):
        self.ball.move()


    def draw(self):
        # Fill the background with white
        self.screen.fill(BLACK)

        # Draw a solid blue circle in the center
        # pygame.draw.circle(self.screen, (0, 0, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 75)
        self.ball.draw()
        self.l_paddle.draw()
        self.r_paddle.draw()

        # Flip the display
        pygame.display.flip()


if __name__ == '__main__':
    game = Pong()
    game.start()
