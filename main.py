import pygame

pygame.init()

w, h = 650, 350
size = w, h

screen = pygame.display.set_mode(size)


def draw():
    line_color = pygame.Color('white')
    line_w = 0
    line_points = ((25, 25), (600, 100))
    pygame.draw.rect(screen, line_color, line_points, line_w)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
