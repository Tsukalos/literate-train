import pygame, sys
from pygame.locals import *
from player import *
from entity import *

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), 0, 32)
update_list = []
keypress = []
for i in range(500):
    keypress.append(False)
p = Player(Rect(20,20,10,10),pygame.image.load("data/player.png").convert())
background = pygame.image.load("data/background.png").convert()
screen.blit(background, (0,0))
pygame.display.update()
def event():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keypress[event.key] = True
        if event.type == KEYUP:
            keypress[event.key] = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

while True:
    update_list = []
    p.update(keypress, update_list, screen, background)
    event()
    timePassed = fpsClock.tick(FPS)
    pygame.display.update(update_list)
