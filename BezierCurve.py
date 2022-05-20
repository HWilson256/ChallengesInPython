from re import X
import pygame

pygame.init()

class point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.selected = False
    
    def click_toggle(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True
    
    def update_point(self, x, y):
        if self.selected:
            self.x = x
            self.y = y
    
    def get_point(self):
        return (self.x, self.y)
#Class to draw cubic bezier lines
class cubic_bezier():
    def __init__(self, p1, p2, p3, p4, screen, color, width) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.screen = screen
        self.color = color
        self.width = width
    
    def draw_self(self):
        #Lower is more accurate and it has to be between 1 and 0
        accuracy = .0005
        t = 0
        while t <= 1:
            P0_x = pow((1-t), 3) * self.p1[0]
            P0_y = pow((1-t), 3) * self.p1[1]
            
            P1_x = 3 * pow((1-t), 2) * t * self.p2[0]
            P1_y = 3 * pow((1-t), 2) * t * self.p2[1]

            P2_x = 3 * (1-t) * pow(t, 2) * self.p3[0]
            P2_y = 3 * (1-t) * pow(t, 2) * self.p3[1]

            P3_x = pow((t), 3) * self.p4[0]
            P3_y = pow((t), 3) * self.p4[1]
            
            curve = (P0_x + P1_x + P2_x + P3_x, P0_y + P1_y + P2_y + P3_y)
            pygame.draw.circle(self.screen, self.color, curve, self.width, self.width)
            t += accuracy

    
#Creating the screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

#Points
points = []
p1 = point(50, 550)
p2 = point(50, 50)
p3 = point(800, 50)
p4 = point(900, 900)

points.append(p1)
points.append(p2)
points.append(p3)
points.append(p4)




running = True
while running:
    click = False
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    bezier_fun = cubic_bezier(p1.get_point(), p2.get_point(), p3.get_point(), p4.get_point(), screen, (255, 255, 255), 3)

    for p in points:
        pygame.draw.circle(screen, (155, 0, 155), p.get_point(), 10, 10)

    for p in points:
        r = pygame.Rect(p.get_point()[0] - 7, p.get_point()[1] - 7, 35, 35)
        mouseR = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
        if r.contains(mouseR) and click:
            p.click_toggle()
    
    for p in points:
        p.update_point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    bezier_fun.draw_self()
    
    
    pygame.display.flip()