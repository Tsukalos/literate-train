import pygame
from pygame.locals import *
class Entity():
    def __init__(self,rect,surf, mask):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.surface = surf
        self.timePassed = 0
        self.animationTimer = 0
        self.name = ""
        self.mask = mask

    def clearBg(self, update_list, screen, background):
        screen.blit(background,self.rect,self.rect)
        r = self.rect.copy()
        r.x -= 10
        r.y -= 10
        r.h += 10
        r.w += 10
        update_list.append(r)
        del r
        return

    def updateAction():
    	return

    def updateState():
    	return

    def loadType():
    	return

    def updateRect(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if(hasattr(self,"hitbox")):
            self.hitbox.center = self.rect.center

    def animation(self):
        self.animationTimer+=self.timePassed
        if(self.animationTimer > self.animationTime):
            if(self.currentTile == (self.surface.get_width()/self.tileSize)-1):
                self.currentTile = 0
            else:
                self.currentTile+=1
            self.animationTimer = 0

    def loadSprite(self, sprite, tileSize, animationTime):
    	self.surface = sprite
    	self.animationTime = animationTime
    	self.tileSize = tileSize
    	self.currentTile = 0

    def draw(self,update_list, screen):
        screen.blit(self.surface,self.rect,Rect(self.currentTile*self.tileSize,0,self.tileSize,self.tileSize))
        if(hasattr(self,"hitbox") and self.focus):
            screen.blit(self.hitboxsurface, self.hitbox)
        r = self.rect.copy()
        r.x -= 10
        r.y -= 10
        r.h += 10
        r.w += 10
        update_list.append(r)
