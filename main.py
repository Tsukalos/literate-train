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

def hook_file(dct):
	pass

with open("enemyFile.json") as f:
	data = json.load(f)



pSprite = pygame.image.load("data/sprite.png").convert()
pSprite.set_colorkey((255,255,255))
eSprite = pygame.image.load("data/eSprite.png").convert()
eSprite.set_colorkey((255,255,255))
p = Player(Rect(20,20,20,20),pSprite)
e = Enemy(Rect(50,50,20,20),eSprite)
p.loadSprite(pSprite,20,250) #usado p/ animation
e.loadSprite(eSprite,20,250)

e.setType(enemyType(data))

background = pygame.image.load("data/background.png").convert()
#background.set_colorkey((255,255,255))

entityList = []
entityList.append(e)
entityList.append(p)

def entityUpdate():
    for a in entityList:
        a.clearBg(update_list, screen, background)
        if type(a) == Player:
            a.update(keypress, timePassed)
        if type(a) == Enemy:
            a.update(timePassed)
    for a in entityList:
        a.draw(update_list,screen)

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
    entityUpdate()
    event()
    pygame.display.update(update_list)
