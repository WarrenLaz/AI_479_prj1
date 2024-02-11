import random
import copy
import heapq as h
import math
import time
from MazeGen import Maze
from MazeSolver import MazeSolver

def countvisited(maze):
    counter = 0
    for x in maze:
        for y in x:
            if y == '@':
                counter+=1
            elif y == '#':
                counter +=1
    return counter

def printMaze(x): 
    for i in x:
        for j in i:
            print(j, end=" ")
        print()

def printMaze(x, f): 
    for i in x:
        for j in i:
            print(j, end=" ")
            f.write(j+' ')
        print()
        f.write('\n')

def main():

    outputFile = open('output.txt', 'w')
    x = 10

    nummaze = int(input("Enter number of Mazes: "))
    l = int(input("Enter Maze Length: "))
    w = int(input("Enter Maze Width: "))
    d = float(input("Enter Maze density from Range[0.0-1.0]: "))
    for i in range(nummaze):
        
        n = Maze.createMaze(l,w, d)

        maze = n[0].copy()

        start_time = time.time()
        q = MazeSolver.DFS(copy.deepcopy(maze), n[1])
        DFStime = (time.time() - start_time)

        start_time = time.time()
        y = MazeSolver.BFS(copy.deepcopy(maze), n[1])
        BFStime = (time.time() - start_time)

        start_time = time.time()
        r = MazeSolver.Astar(copy.deepcopy(maze), n[1], n[2])
        Astartime = (time.time() - start_time)
        
        z = MazeSolver.Djikstras(copy.deepcopy(maze), n[1], n[2])


        print("----------------------------------------")
        print("GENERATED MAZE: ")
        outputFile.write("----------------------------------------\nGENERATED MAZE:\n")
        printMaze(maze, outputFile)
        outputFile.write("\n")
        outputFile.write("\n")
        print("----------------------------------------")
        print("SHORTEST PATH DFS: ")
        outputFile.write("----------------------------------------\nVISITED NODES DFS: \n")
        printMaze(q, outputFile)
        print("NUMBER OF NODES VISITED: ", countvisited(q))
        print("TIME: ", DFStime)
        outputFile.write("NUMBER OF NODES VISITED: " + str(countvisited(q)))
        outputFile.write("\nTIME: " + str(DFStime))
        outputFile.write("\n")
        print("----------------------------------------")
        print("SHORTEST PATH BFS: ")
        outputFile.write("----------------------------------------\nVISITED NODES BFS: \n")
        printMaze(y, outputFile)
        print("NUMBER OF NODES VISITED: ", countvisited(y))
        print("TIME: ", BFStime)
        outputFile.write("NUMBER OF NODES VISITED: " + str(countvisited(y)))
        outputFile.write("\nTIME: " + str(BFStime))
        outputFile.write("\n")
        print("----------------------------------------")
        print("SHORTEST PATH A*: ")
        outputFile.write("----------------------------------------\nVISITED NODES A*: \n")
        printMaze(r, outputFile)
        print("NUMBER OF NODES VISITED: ", countvisited(r))
        print("TIME: ", Astartime)
        outputFile.write("NUMBER OF NODES VISITED: " + str(countvisited(r)))
        outputFile.write("\nTIME: " + str(Astartime))
        outputFile.write("\n")
        print("----------------------------------------")
        print("SHORTEST PATH: ")
        outputFile.write("----------------------------------------\nSHORTEST PATH: \n")
        printMaze(z, outputFile)
        outputFile.write("NUMBER OF NODES VISITED: " + str(countvisited(z)))
        outputFile.write("\n")
        outputFile.write("\n")
        print("----------------------------------------")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        x = x + 1
    
    outputFile.close()

if __name__ == '__main__':
    main()  

