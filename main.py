import pygame
pygame.font.init()

import source.ui as ui
import source.player as player
import globals as globals

pygame.init()
pygame.display.set_caption('undertale pygame cool')
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 0, 50))

    ui.drawButtons(screen)
    ui.drawUiText(screen)
    ui.drawArena(screen)
    player.update()
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()