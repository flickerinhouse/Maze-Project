from graphics import *
from Character import *
from Maze import *
from random import randint

## This file is used for the player interactive version of the maze, the Main.py file
## is used for the normal version
def main():
    N = eval(input("Please enter the dimensions for your maze (Your maze will be N x N) "))
    myMaze = Maze(N)

    print("The Red Square is the start")
    print("The Yellow Square is the key")
    print("The Green Square is the end")
    print("The Blue Circles represent the path to the key")
    print("The Black Circles represent the path to the end")
    print("The top left Cell is (0,0), x increases as you move right and y increases as you move down")
    print("The top left Cell is (0,0), x increases as you move right and y increases as you move down")

    myMaze.generateMaze()
    myMaze.explore(myMaze.entrance[0],myMaze.entrance[1])
    myMaze.printSolution()
    myMaze.Draw()

    myCharacter = Character(myMaze)
    print("You have " + str(len(myMaze.SolutionStack)-2) + " steps to reach the ending")
    print("You are the pink circle, you may use the arrow keys to move")
    gameLoop(myMaze,myCharacter)

    replay = input("Would you like to play again (Y/N)")
    if replay == "Y":
        myMaze.win.close()
        main()
    elif replay == "N":
        myMaze.win.close()
        quit()
    myMaze.win.close()

    

def gameLoop(myMaze,myCharacter):
    count = 0
    while ((myCharacter.getXPos(),myCharacter.getYPos()) != (myMaze.exit[0]+1,myMaze.exit[1]+1) or myCharacter.gotKey == False) and count < len(myMaze.SolutionStack)-2:
        if myMaze.win.getKey() == "Up" and myMaze.map[(myCharacter.getYPos())][myCharacter.getXPos()][3][3] == 1:
            myCharacter.move(0,-1)
            count += 1
        elif myMaze.win.getKey() == "Down" and myMaze.map[myCharacter.getYPos()][myCharacter.getXPos()][3][1] == 1:
            myCharacter.move(0,1)
            count += 1
        elif myMaze.win.getKey() == "Left" and myMaze.map[myCharacter.getYPos()][myCharacter.getXPos()][3][0] == 1:
            myCharacter.move(-1,0)
            count += 1
        elif myMaze.win.getKey() == "Right" and myMaze.map[myCharacter.getYPos()][myCharacter.getXPos()][3][2] == 1:
            myCharacter.move(1,0)
            count += 1
        
        myCharacter.undraw()
        myCharacter.draw(myMaze.win)
        

        if (myCharacter.getXPos(),myCharacter.getYPos()) == (myMaze.key[0]+1,myMaze.key[1]+1) and myCharacter.gotKey == False:
            myCharacter.getKey()
            print("You have found the key")

        if (myCharacter.getXPos(),myCharacter.getYPos()) == (myMaze.exit[0]+1,myMaze.exit[1]+1) and myCharacter.gotKey == True:
            myCharacter.winGame()
    if myCharacter.wonGame == False:
        print("You have run out of turns")
    else:
        print("You win")
            


main()
