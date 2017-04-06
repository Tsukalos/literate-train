from pygame.math import *
class Level():
    def __init__(self, spawnList):
        self.spawnList = spawnList

    def setList(self, listset):
        self.spawnList = listset

class Spawn():
    def __init__(self, time, pos, mobType):
        self.time = time
        self.pos = pos
        self.mobType = mobType
