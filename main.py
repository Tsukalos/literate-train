import pygame, sys
from pygame.locals import *

pygame.init()
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Danmaku')
keypress = []
for i in range(300):
    keypress.append(False)
W = 119
A = 97
S = 115
D = 100

class Player():
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = 100
        self.y = 100

p1 = Player()

def checkKeypress():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keypress[event.key] = True
        if event.type == KEYUP:
            keypress[event.key] = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def playerMov():
    if keypress[W]:
        p1.y -= 1
    if keypress[A]:
        p1.x -= 1
    if keypress[S]:
        p1.y += 1
    if keypress[D]:
        p1.x += 1

def drawPlayer():
    pygame.draw.circle(DISPLAYSURF, BLACK, (p1.x, p1.y), p1.w, p1.h)


while True:
    DISPLAYSURF.fill(WHITE)
    checkKeypress()
    playerMov()
    drawPlayer()
    pygame.display.update()
    fpsClock.tick(FPS)
