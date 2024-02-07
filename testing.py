import random
import copy
import heapq

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

def createMaze(x, y): #10x10
    l,w = (y,x) #x = 10, y = 5 therefore l = 5, w = 10
    maze = [['x' for _ in range(w)] for _ in range(l)] #5x10
    
    start, end = ([random.randint(0,l-1), random.randint(0,w-1)], [random.randint(0,l-1), random.randint(0,w-1)])

    while(start[0] == end[0] and start[1] == end[1]):
        end =  [random.randint(0,l-1), random.randint(0,w-1)]

    maze[start[0]][start[1]] = 'S'

    maze[end[0]][end[1]] = 'G'

    return [createMazeAux(maze, start) , start, end]

def createMazeAux(maze, s):
    l = len(maze)
    w = len(maze[0])
    visited = [[0 for _ in range(w)] for _ in range(l)]
    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = 1

    while(stack):
        point = stack[len(stack)-1]
        x = point[1]
        y = point[0]
    
        listpoints = []

        if(x-1 >= 0):
            if(visited[y][x-1] == 0):
                listpoints.append([y,x-1])
        if(x+1 < w):
            if(visited[y][x+1] == 0):
                listpoints.append([y,x+1])
        if(y-1 >= 0):
            if(visited[y-1][x] == 0):
                listpoints.append([y-1,x])
        if(y+1 < l):
            if(visited[y+1][x] == 0):
                listpoints.append([y+1,x])
        
        if(listpoints):
            d = random.choice(listpoints)

            stack.append([d[0],d[1]])
            visited[d[0]][d[1]] = 1
            if(maze[d[0]][d[1]] == 'G'):
                break
            else:
                maze[d[0]][d[1]] = '.'
        else:
            stack.pop()

    return maze

def DFS(maze, s):
    l = len(maze)
    w = len(maze[0])

    DFSmaze = copy.deepcopy(maze)
    visited = [[0 for _ in range(w)] for _ in range(l)]
    stack = []
    stack.append(s)
    while(stack):
        point = stack[len(stack)-1]
        x = point[1]
        y = point[0]
    
        listpoints = []

        listpoints = checkBounds(x, y, w, l, visited, DFSmaze, listpoints)

        if(listpoints):
            d = random.choice(listpoints)

            stack.append([d[0],d[1]])
            visited[d[0]][d[1]] = 1
            if(DFSmaze[d[0]][d[1]] == 'G'):
                break
            else:
                DFSmaze[d[0]][d[1]] = '@'
        else:
            stack.pop()
    
    return DFSmaze.copy()

def printMaze(x): 
    for i in x:
        for j in i:
            print(j, end=" ")
        print()

x = createMaze(10,5)


printMaze(x[0])
x[0]=DFS(x[0], x[1])
printMaze(x[0])