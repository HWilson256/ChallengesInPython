import pygame
from pygame import *
import sys
import time
import random
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))

outRect = pygame.Rect(55, 55, 490, 490)
inRect = pygame.Rect(60, 60, 480, 480)

count_inside = 0
count_outside = 0
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(count_inside/count_outside)
            sys.exit()
    
    pygame.draw.rect(screen, (0, 0, 0), outRect)
    pygame.draw.rect(screen, (255, 255, 255), inRect)
    pygame.draw.circle(screen, (100, 100, 100), (300, 300), 240, 1)
    for t in range(1500):
        rand_rect = pygame.Rect(random.randint(60, 540), random.randint(60, 540), 0, 0)
        hit = False
        draw = False
        if inRect.contains(rand_rect):
            draw = True
            dx = 300-rand_rect.x
            dy = 300-rand_rect.y
            
            if math.sqrt(dx**2 + dy**2) < inRect.width/2:
                hit = True
                count_inside += 1
            else:
                hit = False 
            count_outside += 1
        if hit:
            hit_color = (0, 255, 0)
        else:
            hit_color = (255, 0, 0)
        if draw:
            pygame.draw.circle(screen, hit_color, (rand_rect.x, rand_rect.y), 5, 5)
    if count_outside != 0:
        print("IN: " + str(count_inside) + " OUT: " + str(count_outside))
        print("Approximate Pi: ", (count_inside/count_outside)*4)
    pygame.display.flip()