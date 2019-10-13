import pygame

pygame.init()

w, h = 650, 350
size = w, h

screen = pygame.display.set_mode(size)


def draw_line(color, line_points):
    line_w = 0
    pygame.draw.rect(screen, pygame.Color(color), line_points, line_w)


def draw():
    line_1_color = "white"
    line_1_points = ((25, 25), (600, 100))
    draw_line(line_1_color, line_1_points)
    line_3_color = "red"
    line_3_points = ((25, 225), (600, 100))
    draw_line(line_3_color, line_3_points)
    line_2_color = "blue"
    line_2_points = ((25, 125), (600, 100))
    draw_line(line_2_color, line_2_points)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
