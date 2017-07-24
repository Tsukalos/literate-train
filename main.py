import pygame, sys, json, logging
from pygame.locals import *
from player import *
from entity import *
from enemy import *
from pprint import pprint
from pygame import freetype

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), 0, 32)
update_list = []
keypress = []



pSprite = pygame.image.load("data/sprite.png").convert()
pSprite.set_colorkey((255,255,255))
eSprite = pygame.image.load("data/eSprite.png").convert()
eSprite.set_colorkey((255,255,255))
p = Player(Rect(50,50,20,20),pSprite)
e = Enemy(Rect(50,50,20,20),eSprite)
p.loadSprite(pSprite,20,250) #animation
e.loadSprite(eSprite,20,250) #animation
e.loadPattern(pattern.patternSquare(e))


background = pygame.image.load("data/background.png").convert()

entityList = []
entityList.append(e)
entityList.append(p)

#fonts
freetype.init()
f = freetype.SysFont("Arial", 11, 1, 0)


def entityUpdate():
    for a in entityList:
        clearNameBg(a)
        a.clearBg(update_list, screen, background)
        if type(a) == Player:
            a.update(keypress, timePassed)
        if type(a) == Enemy:
            a.update(timePassed)
    for a in entityList:
        a.draw(update_list,screen)

def event():
    global keypress
    keypress = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def clearNameBg(a):
    t = f.render(a.name,None,None)
    r = t[1]
    r.x = a.x
    r.y = a.y - 12
    r.w += 2
    r.h += 2
    screen.blit(background,r)
    update_list.append(r)

def debugNameCaptions():
    for a in entityList:
        t = f.render(a.name,None,None)
        s = t[0]
        r = t[1]
        r.x = a.x
        r.y = a.y - 11
        screen.blit(s,r)
        update_list.append(r)

screen.blit(background, (0,0))
pygame.display.update()
while True:
    timePassed = fpsClock.tick(FPS)
    update_list = []
    event()
    entityUpdate()
    debugNameCaptions()
    pygame.display.update(update_list)
