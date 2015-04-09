__author__ = 'Roberto'

from graphics import *
import Stack
from random import randint

class Maze:
    def __init__(self,size):
        ## initializes all the stacks and variables used to store info, and initializes stack object
        self.Stack = []
        self.Explore1Stack = []
        self.Explore2Stack = []
        self.SolutionStack = []
        self.linelist = []
        self.myStack = Stack.myStack()
        self.size = size

        ## self.map stores the information for all the cells, each cell has four [0,0,0,0]'s
        ## the first grouping of 0's stores info about the solution, the second grouping stores info about the solution
        ## the third grouping stores info about the borders of the maze, and the fourth grouping stores info about the walls
        ## the four 0's in each one correspond the the West,South,East and North directions
        self.map = [[[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] for i in range(self.size + 2)] for i in range(self.size + 2)]
        self.win = GraphWin("My Maze",self.size*40+1,self.size*40+1)
        
        ## randomly chooses location for the entrance, exit and key
        self.entrance,self.exit,self.key = self.generatePoints()
        
    def generatePoints(self):
        (x,y)= (randint(1,self.size-1),randint(1,self.size-1))
        entrance = (x,y)
        (x1,y1) = (randint(1,self.size-1),randint(1,self.size-1))
        myexit = (x1,y1)
        (x2,y2)= (randint(1,self.size-1),randint(1,self.size-1))
        key = (x2,y2)
        while key ==entrance or key == myexit or entrance==myexit:
            (x,y)= (randint(1,self.size-1),randint(1,self.size-1))
            entrance = (x,y)
            (x1,y1) = (randint(1,self.size-1),randint(1,self.size-1))
            myexit = (x1,y1)
            (x2,y2)= (randint(1,self.size-1),randint(1,self.size-1))
            key = (x2,y2)
        return entrance,myexit,key

    ## generates maze and builds borders
    def generateMaze(self):
        self.buildBorders()
        self.genMaze()

    ## Draws the maze and solutions
    def Draw(self):
        self.drawGrid()
        self.drawEntranceExit()
        for i in range(len(self.linelist)):
            self.linelist[i].setFill("White")
            self.linelist[i].draw(self.win)
        ##self.drawPath()

    ## explores the maze
    def explore(self,x,y):
        self.exploreToKey(x+1,y+1)
        self.resetBacktrack()
        self.exploreToEnd(self.key[0]+1,self.key[1]+1)
        self.SolutionStack = self.Explore1Stack + self.Explore2Stack

    ## generates maze 
    def genMaze(self):
    	TotalCells = (self.size) * (self.size)
    	CurrentCellx,CurrentCelly = randint(1,self.size),randint(1,self.size)
    	VisitedCells = 1
    	self.myStack.push([CurrentCellx,CurrentCelly],self.Stack)
    	while VisitedCells < TotalCells:
    		Neighbours = self.checkNeighbours(CurrentCellx,CurrentCelly)
    		if len(Neighbours) >= 1:
    			choice = Neighbours[randint(0,len(Neighbours)-1)]
    			CurrentCellx,CurrentCelly = self.breakdown(CurrentCellx,CurrentCelly,choice)
    			self.myStack.push([CurrentCellx,CurrentCelly],self.Stack)
    			self.removeWalls(CurrentCellx,CurrentCelly)
    			VisitedCells += 1
    		else:
    			choice = self.myStack.pop(self.Stack)
    			CurrentCellx,CurrentCelly = choice[0],choice[1]

    # Checks how many neighbours a cell has and which directions they exist
    def checkNeighbours(self,CurrentCellx,CurrentCelly):
        Neighbours = []
        if 1 not in self.map[CurrentCelly][CurrentCellx+1][3] and CurrentCellx+1 < self.size+1 and CurrentCelly < self.size+1 and self.map[CurrentCelly][CurrentCellx][2][2] != 1:
            Neighbours.append([CurrentCellx+1,CurrentCelly])
        if 1 not in self.map[CurrentCelly][CurrentCellx-1][3] and CurrentCellx > 1 and CurrentCellx-1 < self.size+1 and CurrentCelly < self.size+1 and self.map[CurrentCelly][CurrentCellx][2][0] != 1:
            Neighbours.append([CurrentCellx-1,CurrentCelly])
        if 1 not in self.map[CurrentCelly+1][CurrentCellx][3] and CurrentCellx < self.size+1 and CurrentCelly+1 < self.size+1 and self.map[CurrentCelly][CurrentCellx][2][1] != 1:
            Neighbours.append([CurrentCellx,CurrentCelly+1])
        if 1 not in self.map[CurrentCelly-1][CurrentCellx][3] and CurrentCelly > 1 and CurrentCellx < self.size+1 and CurrentCelly-1 < self.size+1 and self.map[CurrentCelly][CurrentCellx][2][3] != 1: 
            Neighbours.append([CurrentCellx,CurrentCelly-1])
        return Neighbours

    #Breaks down a wall
    def breakdown(self,CurrentCellx,CurrentCelly,Choice):
    	if CurrentCellx == Choice[0]:
    		if CurrentCelly > Choice[1]:
    			self.map[Choice[1]][Choice[0]][3][1] = 1
    			self.map[CurrentCelly][CurrentCellx][3][3] = 1
    			return Choice[0],Choice[1]
    		elif CurrentCelly < Choice[1]:
    			self.map[Choice[1]][Choice[0]][3][3] = 1
    			self.map[CurrentCelly][CurrentCellx][3][1] = 1
    			return Choice[0],Choice[1]
    	elif CurrentCelly == Choice[1]:
    		if CurrentCellx > Choice[0]:
    			self.map[Choice[1]][Choice[0]][3][2] = 1
    			self.map[CurrentCelly][CurrentCellx][3][0] = 1
    			return Choice[0],Choice[1]
    		elif CurrentCellx < Choice[0]:
    			self.map[Choice[1]][Choice[0]][3][0] = 1
    			self.map[CurrentCelly][CurrentCellx][3][2]=1
    			return Choice[0],Choice[1]

   	# builds borders
    def buildBorders(self):
    	for i in range(1,self.size+1):
    		for j in range(1,self.size+1):
    			if i == 1: ## builds top border
    				self.map[i][j][2][3] = 1 
    			elif i == self.size: ## builds bottom border
    				self.map[i][j][2][1] = 1 
    			if j == 1: ## builds west border
    				self.map[i][j][2][0] = 1
    			elif j == self.size: ## builds east border
    				self.map[i][j][2][2] = 1

    ##draws the grid
    def drawGrid(self):
        for i in range(1,self.size+1):
        	for j in range(1,self.size+1):
		        square = Rectangle(Point((i-1)*40+3,(j-1)*40+3),Point(i*40+3,j*40+3))
		        square.draw(self.win)

    def removeWalls(self,CurrentCellx,CurrentCelly):
    	if self.map[CurrentCelly][CurrentCellx][3][0] == 1:
    		self.linelist.append(Line(Point((CurrentCellx-1)*40+3,(CurrentCelly-1)*40+3),Point((CurrentCellx-1)*40+3,(CurrentCelly)*40+3)))
    	if self.map[CurrentCelly][CurrentCellx][3][1] == 1:
    		self.linelist.append(Line(Point((CurrentCellx-1)*40+3,CurrentCelly*40+3),Point(CurrentCellx*40+3,CurrentCelly*40+3)))
    	if self.map[CurrentCelly][CurrentCellx][3][2] == 1:
    		self.linelist.append(Line(Point(CurrentCellx*40+3,(CurrentCelly-1)*40+3),Point(CurrentCellx*40+3,CurrentCelly*40+3)))
    	if self.map[CurrentCelly][CurrentCellx][3][3] == 1:
    		self.linelist.append(Line(Point((CurrentCellx-1)*40+3,(CurrentCelly-1)*40+3),Point(CurrentCellx*40+3,(CurrentCelly-1)*40+3)))

    ## draws the entrance,key and exit on the maze
    def drawEntranceExit(self):
        entry = Rectangle(Point(self.entrance[0]*40+8,self.entrance[1]*40+8),Point((self.entrance[0]+1)*40-2,(self.entrance[1]+1)*40-2))
        entry.setFill("Red")
        entry.draw(self.win)
        exit = Rectangle(Point(self.exit[0]*40+8,self.exit[1]*40+8),Point((self.exit[0]+1)*40-2,(self.exit[1]+1)*40-2))
        exit.setFill("Green")
        exit.draw(self.win)
        key = Rectangle(Point(self.key[0]*40+8,self.key[1]*40+8),Point((self.key[0]+1)*40-2,(self.key[1]+1)*40-2))
        key.setFill("Gold")
        key.draw(self.win)

    ## explores from the entrance to the key
    def exploreToKey(self,x,y):
        if (x,y) == (self.key[0]+1,self.key[1]+1):
            self.myStack.push((x,y),self.Explore1Stack)
        elif (x,y) != (self.key[0]+1,self.key[1]+1):
            ## Explore North
            if self.map[y-1][x][3][1] == 1 and [x,y-1] not in self.Explore1Stack and self.map[y-1][x][1][1] == 0:
                self.myStack.push((x,y),self.Explore1Stack)
                self.map[y-1][x][1][1] = 1
                self.map[y][x][1][3] = 1
                self.exploreToKey(x,y-1)
            ## Explore South
            elif self.map[y+1][x][3][3] == 1 and [x,y+1] not in self.Explore1Stack and self.map[y+1][x][1][3] == 0:
                self.myStack.push((x,y),self.Explore1Stack)
                self.map[y+1][x][1][3] = 1
                self.map[y][x][1][1] = 1
                self.exploreToKey(x,y+1)
            ## Explore East
            elif self.map[y][x+1][3][0] == 1 and [x+1,y] not in self.Explore1Stack and self.map[y][x+1][1][0]==0:
                self.myStack.push((x,y),self.Explore1Stack)
                self.map[y][x+1][1][0] = 1
                self.map[y][x][1][2] = 1
                self.exploreToKey(x+1,y)
            ## Explore West
            elif self.map[y][x-1][3][2] == 1 and [x-1,y] not in self.Explore1Stack and self.map[y][x-1][1][2] == 0:
                self.myStack.push((x,y),self.Explore1Stack)
                self.map[y][x-1][1][2] = 1
                self.map[y][x][1][0] = 1
                self.exploreToKey(x-1,y)
            else:
                choice = self.myStack.pop(self.Explore1Stack)
                x,y = choice[0],choice[1]
                self.exploreToKey(x,y)

    ## explores from key to the end
    def exploreToEnd(self,x,y):
        if (x,y) == (self.exit[0]+1,self.exit[1]+1):
            self.myStack.push((x,y),self.Explore2Stack)
        elif (x,y) != (self.exit[0]+1,self.exit[1]+1):
            ## Explore North
            if self.map[y-1][x][3][1] == 1 and [x,y-1] not in self.Explore2Stack and self.map[y-1][x][1][1] == 0:
                self.myStack.push((x,y),self.Explore2Stack)
                self.map[y-1][x][1][1] = 1
                self.map[y][x][1][3] = 1
                self.exploreToEnd(x,y-1)
            ## Explore South
            elif self.map[y+1][x][3][3] == 1 and [x,y+1] not in self.Explore2Stack and self.map[y+1][x][1][3] == 0:
                self.myStack.push((x,y),self.Explore2Stack)
                self.map[y+1][x][1][3] = 1
                self.map[y][x][1][1] = 1
                self.exploreToEnd(x,y+1)
            ## Explore East
            elif self.map[y][x+1][3][0] == 1 and [x+1,y] not in self.Explore2Stack and self.map[y][x+1][1][0]==0:
                self.myStack.push((x,y),self.Explore2Stack)
                self.map[y][x+1][1][0] = 1
                self.map[y][x][1][2] = 1
                self.exploreToEnd(x+1,y)
            ## Explore West
            elif self.map[y][x-1][3][2] == 1 and [x-1,y] not in self.Explore2Stack and self.map[y][x-1][1][2] == 0:
                self.myStack.push((x,y),self.Explore2Stack)
                self.map[y][x-1][1][2] = 1
                self.map[y][x][1][0] = 1
                self.exploreToEnd(x-1,y)
            else:
                choice = self.myStack.pop(self.Explore2Stack)
                x,y = choice[0],choice[1]
                self.exploreToEnd(x,y)

    ## backtrack gets put back to all 0's after one exploration happen
    def resetBacktrack(self):
        for i in range(1,self.size+1):
            for j in range(1,self.size+1):
                self.map[i][j][1] = [0,0,0,0]
                self.map[i][j][0] = [0,0,0,0]
                
    ## draws the Path you explored
    def drawPath(self):
        for i in self.Explore1Stack:
            bigcircle = Circle(Point((i[0]-1)*40+23,(i[1]-1)*40+23),8)
            bigcircle.setFill("Blue")
            bigcircle.draw(self.win)

        for i in self.Explore2Stack:
            circle = Circle(Point((i[0]-1)*40+23,(i[1]-1)*40+23),5)
            circle.setFill("Black")
            circle.draw(self.win)

    def printSolution(self):
        print("The path from the entrance to the key is:", end = " ")
        for i in self.Explore1Stack:
            print(i,end=" ")
        print("\n")
        print("The path from the key to the exit is:", end = " ")
        for i in self.Explore2Stack:
            print(i,end=" ")
        print("\n")
