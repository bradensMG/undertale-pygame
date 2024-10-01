import pygame

# player vars
name = 'chara'
lv = 1
maxhp = 20
hp = 20

image = pygame.image.load('assets/images/ut-heart.png')

def update():
    pass

def draw(screen):
    screen.blit(image, (500, 432))