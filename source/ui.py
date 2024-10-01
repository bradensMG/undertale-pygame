import pygame
screen = pygame.display.set_mode((640, 480))

import source.player as player
import globals as globals

# button shits
fightbt = {}
actbt = {}
itembt = {}
mercybt = {}

fightbt[0] = pygame.image.load('assets/images/ui/bt/fight0.png')
fightbt[1] = pygame.image.load('assets/images/ui/bt/fight1.png')
actbt[0] = pygame.image.load('assets/images/ui/bt/act0.png')
actbt[1] = pygame.image.load('assets/images/ui/bt/act1.png')
itembt[0] = pygame.image.load('assets/images/ui/bt/item0.png')
itembt[1] = pygame.image.load('assets/images/ui/bt/item1.png')
mercybt[0] = pygame.image.load('assets/images/ui/bt/mercy0.png')
mercybt[1] = pygame.image.load('assets/images/ui/bt/mercy1.png')

# fonts
fonts = {}
fonts['ui'] = pygame.font.Font('assets/fonts/Mars_Needs_Cunnilingus.ttf', 23)

# ui strings
name = fonts['ui'].render(player.name + '     LV ' + str(player.lv), True, 'white')

def drawButtons():
    screen.blit(name, (30, 400))
    screen.blit(fightbt[int(globals.choice == 0)], (32, 432))
    screen.blit(actbt[int(globals.choice == 1)], (185, 432))
    screen.blit(itembt[int(globals.choice == 2)], (345, 432))
    screen.blit(mercybt[int(globals.choice == 3)], (500, 432))
    pygame.display.flip()