import pygame

from robot import Robot
from env import draw_track
from sensors import SensorArray

pygame.init()

sensors = SensorArray()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Line Follower Simulator")

clock = pygame.time.Clock()

robot = Robot()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    robot.update()

    draw_track(screen)
    readings = sensors.read(robot, screen)
    error = sensors.get_error(readings)    
    print("Sensors:", readings)
    print("Error:", error)
    
    robot.draw(screen)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
