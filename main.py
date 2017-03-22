import pygame, sys, random, math, logging
from pygame.locals import *
from entities import *
from pygame.math import *


pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (  0,   0,   0)
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Danmaku')
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

while True:
    DISPLAYSURF.fill(WHITE)
    fpsClock.tick(FPS)
    checkKeypress()
    p1.Update(keypress)
    drawPlayer()

    
    pygame.display.update()
