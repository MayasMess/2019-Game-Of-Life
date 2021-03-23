import pygame
import sys
from background import Background

pygame.init()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
white = (255, 255, 255)
background = Background(surface=screen, screen_width=screen_width, screen_height=screen_height)

start_life = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            background.change_color_on_click(position=pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        start_life = True

    if start_life is True:
        background.start_life_game()

    # fill the screen and draw all elements
    screen.fill(white)
    background.draw()

    pygame.display.update()
    clock.tick(10)
