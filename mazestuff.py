import random

def createMaze(): #10x10
    w,l = (10,10)
    maze = [['x' for _ in range(w)] for _ in range(l)]
    
    start, end = ([random.randint(0,9), random.randint(0,9)], [random.randint(0,9), random.randint(0,9)])

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'G'

    return [createMazeAux(maze, start, end) , start, end]

def createMazeAux(maze, s, g):
    visited = [[0 for _ in range(10)] for _ in range(10)]
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
        if(x+1 < 10):
            if(visited[y][x+1] == 0):
                listpoints.append([y,x+1])
        if(y-1 >= 0):
            if(visited[y-1][x] == 0):
                listpoints.append([y-1,x])
        if(y+1 < 10):
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

def SolveWeights(maze, s):
    visited = [[0 for _ in range(10)] for _ in range(10)]
    weights = [[float('inf') for _ in range(10)] for _ in range(10)]
    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = 1
    weights[s[0]][s[1]] = 1

    while(stack):
        point = stack[len(stack)-1]
        x = point[1]
        y = point[0]
        listpoints = []

        if(x-1 >= 0):
            if(visited[y][x-1] == 0 and not(maze[y][x-1] == 'x') ):
                listpoints.append([y,x-1])
        if(x+1 < 10):
            if(visited[y][x+1] == 0 and not(maze[y][x+1] == 'x')):
                listpoints.append([y,x+1])
        if(y-1 >= 0):
            if(visited[y-1][x] == 0 and not(maze[y-1][x] == 'x')):
                listpoints.append([y-1,x])
        if(y+1 < 10):
            if(visited[y+1][x] == 0 and not(maze[y+1][x] == 'x')):
                listpoints.append([y+1,x])
        
        if(listpoints):
            d = random.choice(listpoints)

            stack.append([d[0],d[1]])
            visited[d[0]][d[1]] = 1
            if(weights[y][x]+1 >= weights[d[0]][d[1]]):
                weights[d[0]][d[1]] = weights[y][x] + 1
        else:
            stack.pop()
    
    return weights

def SolveDFS(maze, weights, end):
    x = end[1]
    y = end[0]
    next = weights[end[0]][end[1]]

    while(not(next==1)):
        print(next)
        listpoints = []
        w = []
        if(x-1 >= 0):
            if(not(maze[y][x-1] == 'x') ):
                listpoints.append([y,x-1])
                w.append(weights[y][x-1])
        if(x+1 < 10):
            if(not(maze[y][x+1] == 'x')):
                listpoints.append([y,x+1])
                w.append(weights[y][x+1])
        if(y-1 >= 0):
            if(not(maze[y-1][x] == 'x')):
                listpoints.append([y-1,x])
                w.append(weights[y-1][x])
        if(y+1 < 10):
            if(not(maze[y+1][x] == 'x')):
                listpoints.append([y+1,x])
                w.append(weights[y+1][x])
        
        
        minweight = min(w)
        if(minweight == 1):
            break
        pathind = listpoints[w.index(minweight)]
        maze[pathind[0]][pathind[1]] = '-'
        next = minweight
        x = pathind[1]
        y = pathind[0]

    return maze

           
for i in range(20):
    n = createMaze()

    x = n[0]

    print(x[1][1])
    for i in x:
        for j in i:
            print(j, end=" ")
        print()

    print(n[1])
    y = SolveWeights(n[0], n[1])

    for i in y:
        for j in i:
            print(j, end=" ")
        print()
    z = SolveDFS(x, y, n[2])

    for i in z:
        for j in i:
            print(j, end=" ")
        print()



