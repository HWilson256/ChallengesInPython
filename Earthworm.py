import sys
import pygame
import math
import time

class Cell():
    def __init__(self, speed, x, y) -> None:
        self.speed = speed
        self.x = x
        self.y = y
    
    def move_towards(self, x, y, delta_time):
        x_dif = self.x - x
        y_dif = self.y - y
        a = [x_dif, y_dif]
        original_vals = a

        # get max absolute value
        original_max = max([abs(val) for val in original_vals])

        # normalize to desired range size
        new_range_val = -1
        normalized_vals = [float(val)/original_max * new_range_val for val in original_vals]
        x_speed = normalized_vals[0]*self.speed
        y_speed = normalized_vals[1]*self.speed
        self.x += x_speed * delta_time
        self.y += y_speed * delta_time

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

cells = []
length_of_worm = 350
base_speed = 300
starting_x = 0#screen_width/2
starting_y = 0#screen_height/2

for x in range(length_of_worm):
    cells.append(Cell(base_speed, starting_x, starting_y))

dt = .001
running = True
while running:
    screen.fill((0, 0, 0))
    start_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    for cell in cells:
        pygame.draw.circle(screen, (158, 31, 14), (cell.x, cell.y), 10, 10)
    
    for cell in cells:
        if cells.index(cell) == 0:
            cell.move_towards(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], dt)
        elif math.sqrt((cell.x-temp_cell.x)**2 + (cell.y-temp_cell.y)**2) >= 5:
            cell.move_towards(temp_cell.x, temp_cell.y, dt)
        temp_cell = cell
    
            
    pygame.display.flip()
    end_time = time.time()
    dt = (end_time-start_time)