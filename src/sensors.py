import pygame
import math

class SensorArray:

    def __init__(self):

        self.offsets = [-20, -10, 0, 10, 20]

    def read(self, robot, screen):

        readings = []

        for offset in self.offsets:

            sx = robot.x
            sy = robot.y + offset

            color = screen.get_at((int(sx), int(sy)))

            if color[:3] == (0, 0, 0):
                readings.append(1)
            else:
                readings.append(0)

        return readings

    def get_error(self, readings):

        weights = [-2, -1, 0, 1, 2]

        numerator = 0
        denominator = 0

        for w, r in zip(weights, readings):

            numerator += w * r
            denominator += r

        if denominator == 0:
            return 0

        return numerator / denominator
