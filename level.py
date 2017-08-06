import pygame.image
import enemylist
import movementpattern
#TODO add movement patterns to enemies init
class Level1():
    spawnlist = [
            #(5000, enemylist.Type1((350,300),movementpattern.PatternStill()))
    ]
    for i in range(0,5):
        spawnlist.append((1000 + i*1000, enemylist.Type1((-30,100),movementpattern.PatternCircle())))
    background = pygame.image.load("data/background.png").convert()