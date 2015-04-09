from graphics import *
from Maze import *
from random import randint

## This file is used for the normal version of the maze, the MainwithPlayerInteractivity.py file
## is used for the interactive Version

def main():
    N = eval(input("Please enter the dimensions for your maze (Your maze will be N x N) "))
    myMaze = Maze(N)

    print("The Red Square is the start")
    print("The Yellow Square is the key")
    print("The Green Square is the end")
    print("The Blue Circles represent the path to the key")
    print("The Black Circles represent the path to the end")
    print("The top left Cell is (0,0), x increases as you move right and y increases as you move down")

    myMaze.generateMaze()
    myMaze.explore(myMaze.entrance[0],myMaze.entrance[1])
    ##myMaze.printSolution()
    myMaze.Draw()

main()
