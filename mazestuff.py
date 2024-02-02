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
    queue1 = []
    queue1.append(s)
    weights[s[0]][s[1]] = 1

    while(queue1):
        visited[queue1[0][0]][queue1[0][1]] = 1
        point = queue1[0]
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

        if(listpoints and queue1):
            queue1.extend(listpoints)
            current = queue1[0]

            for x in listpoints:
                neweight = 1 + weights[current[0]][current[1]]
                if( neweight < weights[x[0]][x[1]]):
                    weights[x[0]][x[1]] = neweight

        queue1.pop(0)

                    
            

    
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
        maze[pathind[0]][pathind[1]] = '@'
        next = minweight
        x = pathind[1]
        y = pathind[0]

    return maze


def printsome(x,y,z):
    z = SolveDFS(x, y, z)

    for i in z:
        for j in i:
            print(j, end=" ")
        print()

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
            if(j != float('inf')):
                print(j, end=" ")
            else:
                print('x', end=" ")
        print()
        
    printsome(x,y,n[2])



