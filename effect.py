import pygame.image
from entity import *
from pygame.math import *


class EffectSimpleSprite():
    def __init__(self, rect, isRef, surf1, duration, tileSize):
        self.surf1 = surf1
        self.surf1.convert_alpha()
        self.rect = rect.copy()
        if isRef:
            self.ref = rect
        else:
            self.ref = None
        self.rect.w = tileSize.w
        self.rect.h = tileSize.h
        self.rect.center = rect.center
        self.tileSize = tileSize
        self.nframes = self.surf1.get_width()/tileSize.w 
        self.interval = duration/self.nframes
        self.currentFrame = 0
        self.end = False
        self.timePassed = 0

    def update(self, timePassed):
        if self.ref != None:
            self.rect.center  = self.ref.center
        self.timePassed += timePassed
        if(self.timePassed >= self.interval and (not self.end)):
            if(self.currentFrame < self.nframes):
                self.currentFrame+=1
                self.timePassed = 0
            else:
                self.end = True
    
    def draw(self, update_list, screen):
        if not self.end:
            screen.blit(self.surf1,self.rect,Rect(self.currentFrame*self.tileSize.w,0,self.tileSize.w,self.tileSize.h))

    def clearBg(self, update_list, screen, background):
        screen.blit(background,self.rect,self.rect)
        r = self.rect.copy()
        r.w +=5
        r.h +=5
        update_list.append(r)
        del r

        
