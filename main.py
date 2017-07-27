import pygame, sys, json, logging, copy
from pygame.locals import *
from player import *
from entity import *
from enemy import *
from text import *
import movementpattern
from pprint import pprint
from pygame import freetype

pygame.init()
freetype.init()
f = freetype.SysFont("Lucida Console", 14, 0, 0)
fpsText = Text(freetype.SysFont("Lucida Console ", 15, 1, 0)) 
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
e = Enemy(Rect(350,200,20,20),eSprite)
p.loadSprite(pSprite,20,250) #animation
e.loadSprite(eSprite,20,250) #animation

e.loadEnemy(movementpattern.PatternStill(e), "Enemy1")

background = pygame.image.load("data/background.png").convert()

entityList = []
entityList.append(e)
entityList.append(p)




def entityUpdate():
    for a in entityList:
        clearNameBg(a)
        a.clearBg(update_list, screen, background)
        if type(a) == Player:
            a.update(keypress, timePassed)
        if type(a) == Enemy:
            a.update(timePassed, p)
    for a in entityList:
        a.draw(update_list,screen)

def event():
    global keypress
    keypress = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def debugFramesText():
    fpstime = fpsClock.get_fps()
    fpsText.clearBg(update_list,screen,background)
    fpsText.update(str(int(fpstime)),Rect(10,10,0,0))
    fpsText.draw(update_list,screen)
    pass

def clearNameBg(a):
    t = f.render(a.name)
    r = t[1]
    r.x = a.x
    r.y = a.y - 12
    r.w += 4
    r.h += 4
    screen.blit(background,r)
    update_list.append(r)

def debugNameCaptions():
    for a in entityList:
        t = f.render(a.name)
        s = t[0]
        s.convert()
        r = t[1]
        r.x = a.x
        r.y = a.y - 11
        screen.blit(s,r)
        update_list.append(r)

def despawnEntities():
    for a in entityList:
        if(a.x < -50 or a.x > 850 or a.y < -50 or a.y > 650):
            entityList.remove(a)



screen.blit(background, (0,0))
pygame.display.update()
while True:
    timePassed = fpsClock.tick(FPS)
    update_list = []
    debugFramesText()
    event()
    entityUpdate()
    debugNameCaptions()
    pygame.display.update(update_list)
