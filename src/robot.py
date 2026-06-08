import pygame
import math

class Robot:

    def __init__(self):
        self.x = 100
        self.y = 300

        self.theta = 0
        self.speed = 2

    def update(self):

        self.x += self.speed * math.cos(self.theta)
        self.y += self.speed * math.sin(self.theta)

        if self.x >= 700:
            self.theta = math.pi

        if self.x <= 100:
            self.theta = 0

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(self.x), int(self.y)),
            12
        )

        end_x = self.x + 20 * math.cos(self.theta)
        end_y = self.y + 20 * math.sin(self.theta)

        pygame.draw.line(
            screen,
            (0, 0, 255),
            (self.x, self.y),
            (end_x, end_y),
            3
        )
