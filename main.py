import pygame
pygame.font.init()

import source.ui as ui
import source.player as player

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 100, 50))

    ui.drawButtons()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()