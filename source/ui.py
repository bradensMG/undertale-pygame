import pygame

import source.player as player
import globals as globals

# button shits
fightbt = {
    0:pygame.image.load('assets/images/ui/bt/fight0.png'),
    1:pygame.image.load('assets/images/ui/bt/fight1.png')
}

actbt = {
    0:pygame.image.load('assets/images/ui/bt/act0.png'),
    1:pygame.image.load('assets/images/ui/bt/act1.png')
}

itembt = {
    0:pygame.image.load('assets/images/ui/bt/item0.png'),
    1:pygame.image.load('assets/images/ui/bt/item1.png')
}

mercybt = {
    0:pygame.image.load('assets/images/ui/bt/mercy0.png'),
    1:pygame.image.load('assets/images/ui/bt/mercy1.png')
}

# arena
arena = {
    'width':570,
    'height':135,
    'x':320,
    'y':320
}

# fonts
fonts = {
    'ui':pygame.font.Font('assets/fonts/Mars_Needs_Cunnilingus.ttf', 23)
}

# ui strings
uiStrings = {
    'name':fonts['ui'].render(player.name + '     LV ' + str(player.lv), True, 'white')
}

def drawButtons(screen):
    screen.blit(fightbt[int(globals.choice == 0)], (32, 432))
    screen.blit(actbt[int(globals.choice == 1)], (185, 432))
    screen.blit(itembt[int(globals.choice == 2)], (345, 432))
    screen.blit(mercybt[int(globals.choice == 3)], (500, 432))

def drawUiText(screen):
    screen.blit(uiStrings['name'], (30, 400))

def drawArena(screen):
    pygame.draw.rect(screen, 'black', [arena['x'] - (arena['width']//2), arena['y'] - (arena['height']//2), arena['width'], arena['height']])
    pygame.draw.rect(screen, 'white', [arena['x'] - (arena['width']//2), arena['y'] - (arena['height']//2), arena['width'], arena['height']], 5)