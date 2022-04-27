import math
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))

length = 150
start = (300, 100)
pos1 = (0, 0)
theta = math.pi/3
vel1 = 0

gravity = 1.5
screen.fill((255, 255, 255))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    accel = -(gravity/length) * (math.sin(theta)) *.005
    vel1 += accel
    theta += vel1
    
    B = theta
    A = 180-(math.degrees(theta)+90)
    C = 90
    y1 = length * math.sin(math.radians(A))
    x1 = math.sqrt((length ** 2) - (y1 ** 2))
    
    if theta < 0:
        x1 = -x1
    pygame.draw.line(screen, (0, 0, 0), start, (x1+300, y1+100), 1)
    pygame.draw.circle(screen, (0, 0, 0), (x1+300, y1+100), 15, 35)
        
    pygame.display.flip()