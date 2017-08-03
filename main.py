import pygame, sys, json, logging, copy
from pygame.locals import *
from player import *
from entity import *
from enemy import *
from text import *
from pygame.mask import *
import movementpattern
from pprint import pprint
from pygame import freetype
from effect import *

pygame.init()
freetype.init()
f = freetype.SysFont("Lucida Console", 14, 0, 0)
fpsText = Text(freetype.SysFont("Lucida Console ", 15, 1, 0)) 
entityCounter = Text(freetype.SysFont("Lucida Console ", 15, 1, 0))
dps = Text(freetype.SysFont("Lucida Console ", 15, 1,))
FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), 0, 32)
update_list = []
keypress = []

enableCollision = False

loadedEffects = [
    pygame.image.load("data/effect1.png"),
    pygame.image.load("data/effect2.png")
]

pSprite = pygame.image.load("data/test.png").convert()
pSprite.set_colorkey((255,255,255))
eSprite = pygame.image.load("data/eSprite.png").convert()
eSprite.set_colorkey((255,255,255))
p = Player(Rect(50,50,pSprite.get_height(),pSprite.get_height()),pSprite, pygame.mask.from_surface(pSprite))
e = Enemy(Rect(350,300,20,20),eSprite, pygame.mask.from_surface(eSprite))
p.loadSprite(pSprite,21,250) #animation
e.loadSprite(eSprite,20,250) #animation

e.loadEnemy(movementpattern.PatternStill(e), "Enemy1", bulletpattern.Pattern3(),1000)

background = pygame.image.load("data/background.png").convert()

entityList = []
bulletList = []
pbulletList = []
effectList = []
entityList.append(e)
entityList.append(p)

dmg = 0


def entityUpdate():
    for a in entityList:
        clearNameBg(a)
        a.clearBg(update_list, screen, background)
        if type(a) == Player:
            a.update(keypress, timePassed, pbulletList)
        if type(a) == Enemy:
            a.update(timePassed, p, bulletList)
    bulletUpdate()
    effectUpdate()
    for a in entityList:
        a.draw(update_list,screen)
    bulletDraw()
    effectDraw()

def bulletUpdate():
    for b in bulletList + pbulletList:
        b.clearBg(update_list, screen, background)
        b.update()

def bulletDraw():
    for b in bulletList + pbulletList:
        b.draw(update_list, screen)

def event():
    global keypress, enableCollision
    keypress = pygame.key.get_pressed()
    if keypress[K_c] and keypress[K_LSHIFT]:
        enableCollision = True
    if keypress[K_v] and keypress[K_LSHIFT]:
        enableCollision = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def debugFramesText():
    global dmg
    fpstime = fpsClock.get_fps()
    entityc = len(bulletList+pbulletList)
    entityCounter.clearBg(update_list, screen, background)
    fpsText.clearBg(update_list,screen,background)
    dps.clearBg(update_list,screen,background)
    dps.update(str(int(dmg/timePassed*100)), Rect(80,10,0,0))
    entityCounter.update(str(entityc),Rect(50,10,0,0))
    fpsText.update(str(int(fpstime)),Rect(10,10,0,0))
    entityCounter.draw(update_list, screen)
    fpsText.draw(update_list,screen)
    dps.draw(update_list,screen)
    dmg = 0
    


def clearNameBg(a):
    if(type(a) == Enemy):
        txt = a.name+"["+str(a.hp)+"]"
    else:
        txt = a.name
    t = f.render(txt)
    r = t[1]
    r.x = a.x
    r.y = a.y - 12
    r.w += 4
    r.h += 4
    screen.blit(background,r)
    update_list.append(r)

def debugNameCaptions():
    for a in entityList:
        if(type(a) == Enemy):
            txt = a.name+"["+str(a.hp)+"]"
        else:
            txt = a.name
        t = f.render(txt)
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
    for a in pbulletList+bulletList:
        if(a.x < -50 or a.x > 850 or a.y < -50 or a.y > 650):
            if a in pbulletList:
                pbulletList.remove(a)
            else:
                bulletList.remove(a)

def updateDamage():
    for a in entityList:
        if(type(a) == Enemy):
            if a.hp < 0:
                a.clearBg(update_list,screen,background)
                s = loadedEffects[0]
                effectList.append(EffectSimpleSprite(a.rect,False,s,400,Rect(0,0,s.get_height(),s.get_height())))
                entityList.remove(a)
            else:
                l = a.rect.collidelistall(pbulletList)
                x = len(l)
                if(x>0):
                    l = set(l) - set(a.lastHitIndex)
                    for k in l:
                        r = pbulletList[k].rect
                        s = loadedEffects[1]
                        effectList.append(EffectSimpleSprite(r,False,s,200,Rect(0,0,s.get_height(),s.get_height())))
                        a.hp -= p.firingpattern.damage
                        global dmg
                        dmg += p.firingpattern.damage
                    a.lastHitIndex = l

def checkPlayerCollision():
    for b in bulletList:
        if(p.rect.colliderect(b.rect)):
            ox = b.rect.x - p.hitbox.x
            oy = b.rect.y - p.hitbox.y
            if(p.mask.overlap(b.mask,(ox,oy))):
                if(p in entityList):
                    p.clearBg(update_list, screen, background)
                    entityList.remove(p)
    pass

def effectUpdate():
    for e in effectList:
        e.clearBg(update_list, screen, background)
        e.update(timePassed)
        if e.end:
            effectList.remove(e)

def effectDraw():
    for e in effectList:
        e.draw(update_list, screen)

screen.blit(background, (0,0))
pygame.display.update()
while True:
    #if len(bulletList) > 20:
        #bulletList = []
    timePassed = fpsClock.tick(FPS)
    update_list = []
    debugFramesText()
    event()
    entityUpdate()
    if enableCollision:
        checkPlayerCollision()
    updateDamage()
    despawnEntities()
    debugNameCaptions()
    pygame.display.update(update_list)
