import random
import sys
import time
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

x = screen.get_width()/2
y = screen.get_height()/2
heading = 0
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 1, 1)
    
    direction = random.randint(0, 3)
    
    if direction == 0:
        y -= speed
    if direction == 1:
        x += speed
    if direction == 2:
        y += speed
    if direction == 3:
        x -= speed
    
    if x >= 600:
        x -= speed
    if x <= 0:
        x += speed
    if y >= 600:
        y -= speed
    if y <= 0:
        y += speed
    
    pygame.display.flip()
    