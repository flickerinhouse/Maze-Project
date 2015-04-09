__author__ = 'Roberto'

from graphics import *

class Character(Circle):
	def __init__(self,myMaze):
		self.xcoord = myMaze.entrance[0]
		self.ycoord = myMaze.entrance[1]
		self.gotKey = False
		self.wonGame = False
		Circle.__init__(self,Point(self.xcoord*40+23,self.ycoord*40+23),10)
		self.setFill("Pink")
		self.draw(myMaze.win)
		self.xcoord += 1
		self.ycoord += 1

	## returns the Center of the circle
	def getCenter(self):
		return super(Character,self).getCenter()

	## returns the X coordinate of the center of the circle
	def getX(self):
		point = self.getCenter()
		return point.getX()

	## returns the Y coordinate of the center of the circle
	def getY(self):
		point = super(Character,self).getCenter()
		return point.getY()

	## returns the X coordinate of the cell you are in
	def getXPos(self):
		return self.xcoord

	## returns the Y coordinate of the cell you are in
	def getYPos(self):
		return self.ycoord

	## moves the character in whichever direction you want
	def move(self,x,y):
		self.xcoord += x
		self.ycoord += y
		super(Character,self).move(x*40,y*40)

	## runs when you get the key
	def getKey(self):
		self.gotKey = True
                ## confirms that you won the game
	def winGame(self):
		self.wonGame = True



