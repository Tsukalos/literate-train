from pygame.math import *
import movement

class MovementPattern():
	def __init__(self):
		self.timer = 0
		self.movePointer = 0
		self.move_list = []
		self.loop = 0

	def setEntity(self, entity):
		self.entity = entity
		
	def update(self, timePassed):
		self.timer+=timePassed
		if self.move_list != []:
			if self.move_list[self.movePointer][1] > 0:
				if(self.timer > self.move_list[self.movePointer][1]):
					self.movePointer+=1
					if(self.movePointer == len(self.move_list)):
						if(self.loop):
							self.movePointer = 0
							self.move_list = self.patternList()
						else:
							self.movePointer-=1
					self.timer = 0
				self.move_list[self.movePointer][0].update(self.entity)
			else:
				if not self.move_list[self.movePointer][0].update(self.entity):
					if self.movePointer < len(self.move_list) - 1:
						self.movePointer+=1
					else:
						if self.loop:
							self.movePointer = 0
							self.move_list = self.patternList()
						else:
							self.movePointer -=1

class PatternBox(MovementPattern):
	def __init__(self):
		MovementPattern.__init__(self)
		self.move_list = self.patternList()
		self.loop = 1

	def	patternList(self):
		mList = []
		mList.append((movement.Line(Vector2(1,0),4,-3,1),5000))
		mList.append((movement.Line(Vector2(0,1),4,-3,1),5000))
		mList.append((movement.Line(Vector2(-1,0),4,-3,1),5000))
		mList.append((movement.Line(Vector2(0,-1),4,-3,1),5000))
		return mList



class PatternStill(MovementPattern):
	def __init__(self):
		MovementPattern.__init__(self)
		self.move_list = self.patternList()
		self.loop = 0

	def	patternList(self):
		mList = []
		return mList

class PatternCircle(MovementPattern):
	def __init__(self):
		MovementPattern.__init__(self)
		self.move_list = self.patternList()
		self.loop = 0

	def patternList(self):
		mList = []
		mList.append((movement.Line(Vector2(1,0),3,0,1),2000))
		mList.append((movement.Circle1FullTurn(4, True, 10),0))
		mList.append((movement.Line(Vector2(1,0),3,0,1),2000))
		return mList


