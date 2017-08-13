import pygame, sys, json, logging, copy
from pygame.locals import *
from player import *
from entity import *
from enemy import *
from text import *
from pygame.mask import *
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
screenDis = pygame.display.set_mode((800, 600))
playArea = Rect(50,20,450,560)
ui = pygame.image.load("data/playareaOverlay.png").convert_alpha()
screen = pygame.Surface((450,560))
update_list = []
keypress = []

enableCollision = False
import level
loadedEffects = [
    pygame.image.load("data/effect1.png").convert_alpha(),
    pygame.image.load("data/effect2.png").convert_alpha(),
    pygame.image.load("data/effect12.png").convert_alpha()
]

pSprite = pygame.image.load("data/test.png").convert()
pSprite.set_colorkey((255,255,255))
eSprite = pygame.image.load("data/eSprite.png").convert()
eSprite.set_colorkey((255,255,255))
p = Player(Rect(50,50,pSprite.get_height(),pSprite.get_height()),pSprite, pygame.mask.from_surface(pSprite))
#e = Enemy(Rect(350,300,20,20),eSprite, pygame.mask.from_surface(eSprite))
p.loadSprite(pSprite,21,250) #animation
#e.loadSprite(eSprite,20,250) #animation

#e.loadEnemy(movementpattern.PatternStill(e), "Enemy1", bulletpattern.Pattern3(),1000)

#background = pygame.image.load("data/playArea.png").convert()
#background.set_colorkey((255,255,255))

entityList = []
bulletList = []
pbulletList = []
effectList = []
#entityList.append(e)
entityList.append(p)

dmg = 0


def entityUpdate():
    for a in entityList:
        clearNameBg(a)
        a.clearBg(update_list, screen, background)
        if type(a) == Player:
            a.update(keypress, timePassed, pbulletList)
        if type(a) == Enemy or issubclass(type(a),Enemy):
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
    entityCounter.clearBg(update_list, screenDis, ui)
    fpsText.clearBg(update_list,screenDis,ui)
    dps.clearBg(update_list,screenDis,ui)
    dps.update(str(int(dmg/timePassed*100)), Rect(700,570,0,0))
    entityCounter.update(str(entityc),Rect(650,570,0,0))
    fpsText.update(str(int(fpstime)),Rect(600,570,0,0))
    entityCounter.draw(update_list, screenDis)
    fpsText.draw(update_list,screenDis)
    dps.draw(update_list,screenDis)
    dmg = 0
    


def clearNameBg(a):
    if(type(a) == Enemy or issubclass(type(a),Enemy)):
        txt = a.name+"["+str(a.hp)+"]"
    else:
        txt = a.name
    t = f.render(txt)
    r = t[1]
    r.x = a.x
    r.y = a.y - 12
    r.w += 4
    r.h += 4
    screen.blit(background,r,r)
    update_list.append(r)

def debugNameCaptions():
    for a in entityList:
        if(type(a) == Enemy or issubclass(type(a),Enemy)):
            txt = a.name+"["+str(a.hp)+"]"
        else:
            txt = a.name
        t = f.render(txt)
        s = t[0]
        s.convert_alpha()
        s.set_colorkey((255,255,255))
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
        if(type(a) == Enemy or issubclass(type(a),Enemy)):
            if a.hp < 0:
                a.clearBg(update_list,screen,background)
                s = loadedEffects[2]
                effectList.append(EffectSimpleSprite(a.rect,False,s,400,Rect(0,0,s.get_height(),s.get_height())))
                entityList.remove(a)
            else:
                l = a.rect.collidelistall(pbulletList)
                x = len(l)
                for i in a.lastHitIndex:
                    if (not i in pbulletList):
                        a.lastHitIndex.remove(i)
                if(x>0):
                    #l = set(l) - set(a.lastHitIndex)
                    for k in l:
                        if (not pbulletList[k] in a.lastHitIndex):
                            r = pbulletList[k].rect.copy()
                            #r.center = a.rect.midbottom
                            s = loadedEffects[1]
                            effectList.append(EffectSimpleSprite(r,False,s,200,Rect(0,0,s.get_height(),s.get_height())))
                            a.hp -= p.firingpattern.damage
                            global dmg
                            dmg += p.firingpattern.damage
                            a.lastHitIndex.append(pbulletList[k])
                    #a.lastHitIndex = l

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


background = pygame.surface.Surface((450,560))
background.blit(level.Level1.background, (0,0), Rect(0,5040,450,560))
spawnlist = level.Level1.spawnlist
levelTime = 0
spawnListCounter = 0

screen.blit(background,(0,0))
screenDis.blit(ui,(0,0))
pygame.display.update()

def setLevelEntities():
    global spawnListCounter
    if spawnListCounter < len(spawnlist):
        c = spawnlist[spawnListCounter]
        if levelTime > c[0]:
            entityList.append(c[1])
            spawnListCounter+=1


timesc = 0
aaa = 0
while True:
    #if len(bulletList) > 20:
        #bulletList = []
    timePassed = fpsClock.tick(FPS)
    levelTime+=timePassed
    timesc += timePassed
    if timesc > 20:
        aaa +=1
        background.blit(level.Level1.background, (0,0), Rect(0,5040-aaa*1,450,560))
        screen.blit(background,(0,0))
        timesc = 0
    setLevelEntities()
    debugFramesText()
    event()
    entityUpdate()
    if enableCollision:
        checkPlayerCollision()
    updateDamage()
    despawnEntities()
    debugNameCaptions()
    update_list = []
    update_list.append(playArea)
    screenDis.blit(screen, playArea)
    pygame.display.update(update_list)
    
