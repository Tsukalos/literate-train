from pygame.math import *
import movement

class Pattern():
	def __init__(self, entity):
		self.timer = 0
		self.entity = entity
		self.movePointer = 0
		self.move_list = []
		
	def update(self, timePassed):
		self.timer+=timePassed
		if(self.timer > self.move_list[self.movePointer][1]):
			self.movePointer+=1
			if(self.movePointer == len(self.move_list)):
				self.movePointer = 0
				self.move_list = self.patternList()
			self.timer = 0
		self.move_list[self.movePointer][0].update(self.entity)


class PatternBox(Pattern):
	def __init__(self, entity):
		Pattern.__init__(self, entity)
		self.move_list = self.patternList()

	def	patternList(self):
		mList = []
		mList.append((movement.Line(Vector2(1,0),4,-3,1),5000))
		mList.append((movement.Line(Vector2(0,1),4,-3,1),5000))
		mList.append((movement.Line(Vector2(-1,0),4,-3,1),5000))
		mList.append((movement.Line(Vector2(0,-1),4,-3,1),5000))
		return mList


