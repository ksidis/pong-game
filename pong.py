import pygame
from pygame.constants import K_ESCAPE, QUIT, K_UP, K_DOWN, K_w, K_s

from assets.ball import Ball
from assets.paddle import Paddle

from constants import *


class Pong:

    def __init__(self):
        pygame.init()
        self.FONT = pygame.font.SysFont("comics", 50)

        # Set up the drawing window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = False

        self.right_score = 0
        self.left_score = 0

        self.l_paddle = Paddle(self.screen, 10,
                               (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT/2),
                               PADDLE_WIDTH, PADDLE_HEIGHT)
        self.r_paddle = Paddle(self.screen,
                               SCREEN_WIDTH -
                               (10 + PADDLE_WIDTH), (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2),
                               PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(self.screen)

    def new_round(self):
        self.ball = Ball(self.screen)

    def start(self):
        # Run until the user asks to quit
        self.running = True
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
            self.handle_collision(self.ball, self.l_paddle, self.r_paddle)

            if self.ball.position.x < 0:
                self.right_score += 1
                self.new_round()
            if self.ball.position.x > SCREEN_WIDTH:
                self.left_score += 1
                self.new_round()

            self.clock.tick(FPS)

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

    def handle_collision(self, ball: Ball, l_paddle: Paddle, r_paddle: Paddle):
        b_poz = ball.position
        if b_poz.y + ball.radius > SCREEN_HEIGHT:
            ball.y_vel *= -1
        elif b_poz.y - ball.radius <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            # left paddle
            if l_paddle.y <= b_poz.y <= l_paddle.y + l_paddle.height:
                if b_poz.x - BALL_RADIUS <= l_paddle.x + l_paddle.width:
                    ball.x_vel *= -1

                    difference_in_y = l_paddle.middle_y - b_poz.y
                    reduction_factor = (l_paddle.height / 2) / BALL_MAX_VELOCITY
                    ball.y_vel =  -1 * difference_in_y / reduction_factor

        else:
            # right paddle
            if r_paddle.y <= b_poz.y <= r_paddle.y + r_paddle.height:
                if b_poz.x + BALL_RADIUS >= r_paddle.x:
                    ball.x_vel *= -1

                    difference_in_y = r_paddle.middle_y - b_poz.y
                    reduction_factor = (r_paddle.height / 2) / BALL_MAX_VELOCITY
                    ball.y_vel = -1 * difference_in_y / reduction_factor

    def update(self):
        self.ball.move()


    def draw(self):
        # Fill the background with white
        self.screen.fill(BLACK)

        left_score_text = self.FONT.render(f"{self.left_score}", 1, WHITE)
        right_score_text = self.FONT.render(f"{self.right_score}", 1, WHITE)
        self.screen.blit(left_score_text, (SCREEN_WIDTH // 4 - left_score_text.get_width() // 2, 20))
        self.screen.blit(right_score_text, (SCREEN_WIDTH * 3/4 - right_score_text.get_width() // 2, 20))

        # Draw a solid blue circle in the center
        # pygame.draw.circle(self.screen, (0, 0, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 75)
        self.l_paddle.draw()
        self.r_paddle.draw()
        self.ball.draw()

        # Flip the display
        pygame.display.flip()


if __name__ == '__main__':
    game = Pong()
    game.start()
