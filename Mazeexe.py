import pygame
from MazeGen import Maze
import copy
import math
import heapq as h

maze_0= Maze.createMaze(36,36,0.5)
maze_ = maze_0[0]
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

def checkBounds(x, y, w, l, visited, maze, listpoints):
    if(x-1 >= 0):
        if(visited[y][x-1] == 0 and not(maze[y][x-1] == 'x') ):
            listpoints.append([y,x-1])
    if(x+1 < w):
        if(visited[y][x+1] == 0 and not(maze[y][x+1] == 'x')):
            listpoints.append([y,x+1])
    if(y-1 >= 0):
        if(visited[y-1][x] == 0 and not(maze[y-1][x] == 'x')):
            listpoints.append([y-1,x])
    if(y+1 < l):
        if(visited[y+1][x] == 0 and not(maze[y+1][x] == 'x')):
            listpoints.append([y+1,x])        
    
    return listpoints

def Heuristic(x1, x2, y1, y2):
    return  math.sqrt( (x1 - x2)**2 + ((y1 - y2)**2))

def Heuristic2(x1, x2, y1, y2):
    return  abs(x1 - x2) + abs(y1 - y2) 

def drawGrid(mazes):
    blockSize = 20
    i = 0
    j = 0
    for x in range(0, screen.get_width(), blockSize):
        for y in range(0, screen.get_height(), blockSize):
            b = pygame.Rect(x, y, blockSize, blockSize)
            if(mazes[int(x/blockSize)][int(y/blockSize)] == '.'):
                pygame.draw.rect(screen, "white", b )
            elif(mazes[int(x/blockSize)][int(y/blockSize)] == 'G'):
                pygame.draw.rect(screen, "purple", b )
            elif(mazes[int(x/blockSize)][int(y/blockSize)] == '@'):
                pygame.draw.rect(screen, "lightblue", b )
            elif(mazes[int(x/blockSize)][int(y/blockSize)] == '*'):
                pygame.draw.rect(screen, "blue", b )
            elif(mazes[int(x/blockSize)][int(y/blockSize)] == 'S'):
                pygame.draw.rect(screen, "green", b )


l = len(maze_[1])
w = len(maze_[0])
visited = [[0 for _ in range(w)] for _ in range(l)]
s = maze_0[1]
g = maze_0[2]
queue1 = [(Heuristic(s[0], g[0], s[1], g[1]), s)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if queue1:
        h.heapify(queue1)
        point = queue1[0][1]
        x = point[1]
        y = point[0]
        listpoints = []
        visited[y][x] = 1
        listpoints = checkBounds(x, y, w, l, visited, maze_, listpoints)
        if (maze_[y][x] != 'S'): maze_[y][x] = '*'
        if(listpoints):
            hlist = []
            choice = []
            for f in listpoints:
                hlist.append(Heuristic(f[0], g[0], f[1], g[1]))
            for i in range(len(listpoints)):
                choice.append((hlist[i], listpoints[i]))
            for c in choice:
                if(not(c in queue1)):
                   queue1.append(c)
                if(maze_[c[1][0]][c[1][1]] == 'G'):
                    queue1.clear()
                elif(not(maze_[c[1][0]][c[1][1]] == 'S' or maze_[c[1][0]][c[1][1]] == 'G')):
                    maze_[c[1][0]][c[1][1]] = '@' 
        if(queue1):
            queue1.pop(0)

    screen.fill("black")
    drawGrid(maze_)
    blockSizes = 20
    pygame.display.flip()
    clock.tick(10)

pygame.quit()