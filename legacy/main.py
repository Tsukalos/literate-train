import pygame, sys, random, math, logging
from pygame.locals import *
from entities import *
from pygame.math import *
from levelList import *


pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (  0,   0,   0)
FPS = 60
timePassed = 0.0
totalTime = 0.0
eSpawnTime = 0.0
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Nocaption')
keypress = []
enemyBullets = []
playerBullets = []
enemies = []


for i in range(300):
    keypress.append(False)

logging.basicConfig(level=logging.INFO)

p1 = Player()
p1.hitbox.x = 300;
p1.hitbox.y = 300;
p1.hitbox.w = 4;
p1.hitbox.h = 2;

def load_spawnList(levelClass):
    for i in levelClass.spawnList:
        pass


def checkKeypress():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keypress[event.key] = True
        if event.type == KEYUP:
            keypress[event.key] = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def drawPlayer():
    pygame.draw.circle(DISPLAYSURF, RED, (int(p1.hitbox.x), int(p1.hitbox.y)), p1.hitbox.w, p1.hitbox.h)

def drawEnemies():
    for en in enemies:
        pygame.draw.rect(DISPLAYSURF, BLACK, en.hitbox, 2)

def drawBullets():
    for bu in enemyBullets:
        pygame.draw.rect(DISPLAYSURF, GREEN, (bu.x,bu.y,5,5), 3)

def spawnEnemies(timePassed):
    spawnInterval = 2000
    global eSpawnTime
    eSpawnTime += timePassed
    if eSpawnTime > spawnInterval:
        enemies.append(Enemy(Rect(100,100,6,6),Vector2(1,-0.1)))
        eSpawnTime = 0.0
    if len(enemies) > 5:
        enemies.pop(0)

def updateEnemies():
    for en in enemies:
        en.Update(enemyBullets,p1, timePassed)

def updateBullets():
    for bu in enemyBullets:
        bu.Update()



while True:
	DISPLAYSURF.fill(WHITE)
	timePassed = fpsClock.tick(FPS)
	fpstime = fpsClock.get_fps()
	fon = pygame.font.SysFont('Arial', 50)
	surf = fon.render(str(int(fpstime)), True, BLACK)
	DISPLAYSURF.blit(surf, (20, 20))
	totalTime += timePassed
	spawnEnemies(timePassed)
	checkKeypress()
	p1.Update(keypress, timePassed)
	updateEnemies()
	updateBullets()
	drawPlayer()
	drawEnemies()
	drawBullets()
	pygame.display.update()
