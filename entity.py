import pygame
from pygame.locals import *
class Entity():
    def __init__(self,rect,surf):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.surface = surf
        self.timePassed = 0

    def clearBg(self, update_list, screen, background):
        screen.blit(background,self.rect,self.rect)
        update_list.append(self.rect.copy())
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

    def animation(self, timePassed):
    	self.timePassed+=timePassed
    	if(self.timePassed > self.animationTime):
    		self.currentTile+=1
    		if(self.currentTile == (self.surface.get_width()/self.tileSize)-1):
    			self.currentTile = 0
    		self.timePassed = 0

    def loadSprite(self, sprite, tileSize,animationTime):
    	self.surface = sprite
    	self.animationTime = animationTime
    	self.tileSize = tileSize
    	self.currentTile = 0

    def draw(self,update_list, screen):
    	screen.blit(self.surface,self.rect,Rect(self.currentTile*self.tileSize,0,self.tileSize,self.tileSize))
    	update_list.append(self.rect.copy())
