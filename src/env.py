import pygame

WIDTH = 800
HEIGHT = 600

def draw_track(screen):

    screen.fill((255, 255, 255))

    pygame.draw.line(
        screen,
        (0, 0, 0),
        (100, 300),
        (700, 300),
        12
    )
