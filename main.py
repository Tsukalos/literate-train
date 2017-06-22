import pygame, sys, json, logging
from pygame.locals import *
from player import *
from entity import *
from enemy import *
from pprint import pprint


pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), 0, 32)
update_list = []
keypress = []
for i in range(500):
    keypress.append(False)
'''	
def hook_file(dct):
	pprint(dct[])
	return enemyType("aa", dct['movements'])
with open("enemyFile.json") as f:
	data = json.load(f, object_hook=hook_file)
'''
	


pSprite = pygame.image.load("data/sprite.png").convert()
p = Player(pSprite.get_rect(topleft = (20,20)),pSprite)
p.loadSprite(pSprite,20,250) #usado p/ animation
background = pygame.image.load("data/background.png").convert()

def event():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keypress[event.key] = True
        if event.type == KEYUP:
            keypress[event.key] = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

screen.blit(background, (0,0))
pygame.display.update()
while True:
    timePassed = fpsClock.tick(FPS)
    update_list = []
    p.update(keypress, update_list, screen, background, timePassed)
    event()
    pygame.display.update(update_list)
