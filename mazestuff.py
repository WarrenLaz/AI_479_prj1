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
    l,w = (y,x)
    maze = [['x' for _ in range(l)] for _ in range(w)]
    
    start, end = ([random.randint(0,l-1), random.randint(0,w-1)], [random.randint(0,l-1), random.randint(0,w-1)])

    while(start[0] == end[0] and start[1] == end[1]):
        end =  [random.randint(0,l-1), random.randint(0,w-1)]

    maze[start[0]][start[1]] = 'S'

    maze[end[0]][end[1]] = 'G'

    return [createMazeAux(maze, start) , start, end]

def createMazeAux(maze, s):
    l = len(maze)
    w = len(maze[0])
    visited = [[0 for _ in range(l)] for _ in range(w)]
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
    visited = [[0 for _ in range(l)] for _ in range(w)]
    weights = [[float('inf') for _ in range(l)] for _ in range(w)]
    stack = []
    stack.append(s)
    weights[s[0]][s[1]] = 1

    while(stack):
        point = stack[len(stack)-1]
        x = point[1]
        y = point[0]
    
        listpoints = []

        listpoints = checkBounds(x, y, l, w, visited, DFSmaze, listpoints)

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

def BFS(maze, s):
    l = len(maze)
    w = len(maze[0])

    BFSmaze = copy.deepcopy(maze)
    visited = [[0 for _ in range(l)] for _ in range(w)]
    queue1 = []
    queue1.append(s)

    while(queue1):
        visited[queue1[0][0]][queue1[0][1]] = 1
        point = queue1[0]
        x = point[1]
        y = point[0]
        listpoints = []

        listpoints = checkBounds(x,y, l, w, visited, BFSmaze, listpoints)

        if(listpoints and queue1):
            for h in listpoints:
                if(not(h in queue1)):
                    queue1.append(h)

            current = queue1[0]

            if(not(BFSmaze[current[0]][current[1]] == 'S')):
                BFSmaze[current[0]][current[1]] = '@'

            if(BFSmaze[current[0]][current[1]] == 'G'):
                queue1.clear()
                break

        if(queue1):
            queue1.pop(0)

    return BFSmaze

def Djikstras(maze, s, end):
    l = len(maze)
    w = len(maze[0])
    Dijkstrasmaze = copy.deepcopy(maze)
    visited = [[0 for _ in range(l)] for _ in range(w)]
    weights = [[float('inf') for _ in range(l)] for _ in range(w)]
    queue1 = []
    queue1.append(s)
    weights[s[0]][s[1]] = 1

    while(queue1):
        visited[queue1[0][0]][queue1[0][1]] = 1
        point = queue1[0]
        x = point[1]
        y = point[0]
        listpoints = []

        listpoints = checkBounds(x,y, l, w, visited, Dijkstrasmaze, listpoints)

        if(listpoints and queue1):
            for h in listpoints:
                if(not(h in queue1)):
                    queue1.append(h)
            current = queue1[0]

            for r in listpoints:
                neweight = 1 + weights[current[0]][current[1]]
                if( neweight < weights[r[0]][r[1]]):
                    weights[r[0]][r[1]] = neweight

            if(Dijkstrasmaze[queue1[0][0]][queue1[0][1]] == 'G'):
                break

        queue1.pop(0)

    return AuxDjikstras(Dijkstrasmaze, weights, end)



def AuxDjikstras(maze, weights, end):
    l = len(maze)
    w = len(maze[0])

    BFSmaze = maze.copy()



    x = end[1]
    y = end[0]
    next = weights[end[0]][end[1]]

    while(not(next==1)):
        listpoints = []
        wlist = []
        if(x-1 >= 0):
            if(not(BFSmaze[y][x-1] == 'x') ):
                listpoints.append([y,x-1])
                wlist.append(weights[y][x-1])
        if(x+1 < w):
            if(not(BFSmaze[y][x+1] == 'x')):
                listpoints.append([y,x+1])
                wlist.append(weights[y][x+1])
        if(y-1 >= 0):
            if(not(BFSmaze[y-1][x] == 'x')):
                listpoints.append([y-1,x])
                wlist.append(weights[y-1][x])
        if(y+1 < l):
            if(not(BFSmaze[y+1][x] == 'x')):
                listpoints.append([y+1,x])
                wlist.append(weights[y+1][x])
        
        
        minweight = min(wlist)
        if(minweight == 1):
            break
        pathind = listpoints[wlist.index(minweight)]
        BFSmaze[pathind[0]][pathind[1]] = '@'
        next = minweight
        x = pathind[1]
        y = pathind[0]


    return BFSmaze

def Heuristic(x1, x2, y1, y2):
    return  abs( x1 - x2 ) + abs(y1 - y2)

def Astar(maze, s, g):
    l = len(maze)
    w = len(maze[0])
    Astarmaze = copy.deepcopy(maze)
    visited = [[0 for _ in range(l)] for _ in range(w)]
    queue1 = []
    queue1.append(s)
    
    while(queue1):
        point = queue1[0]
        x = point[1]
        y = point[0]

        listpoints = []

        listpoints = checkBounds(x, y, l, w, visited, Astarmaze, listpoints)

        if(listpoints):
            hlist = []
            choice = []
            for d in listpoints:
                hlist.append(Heuristic(d[0], g[0], d[1], g[1]))
            
            choice.append(listpoints[hlist.index(min(hlist))])

            for d in hlist:
                if not(hlist.index(d) == listpoints.index(choice[0]) and hlist[0] == d):
                    choice.append(listpoints[hlist.index(d)])
            for d in choice:
                heapq.heappush(queue1, d)
                visited[d[0]][d[1]] = 1
            
                if(Astarmaze[d[0]][d[1]] == 'G'):
                    queue1.clear()
                    break
                elif(not(Astarmaze[d[0]][d[1]] == 'S')):
                    Astarmaze[d[0]][d[1]] = '@'
        if(queue1):
            heapq.heappop(queue1)
    
    return Astarmaze.copy()

def printMaze(x): 
    for i in x:
        for j in i:
            print(j, end=" ")
        print()

def main():
    x = 10
    for i in range(20):
        
        n = createMaze(x,x)
        maze = n[0].copy()
        q = DFS(copy.deepcopy(maze), n[1])
        r = Astar(copy.deepcopy(maze), n[1], n[2])
        y = BFS(copy.deepcopy(maze), n[1])
        z = Djikstras(copy.deepcopy(maze), n[1], n[2])

        print("----------------------------------------")
        print("GENERATED MAZE: ")
        printMaze(maze)
        print("----------------------------------------")
        print("SHORTEST PATH DFS: ")
        printMaze(q)
        print("----------------------------------------")
        print("SHORTEST PATH BFS: ")
        printMaze(y)
        print("----------------------------------------")
        print("SHORTEST PATH Djikstras: ")
        print("----------------------------------------")
        printMaze(z)
        print("----------------------------------------")
        print("SHORTEST PATH A*: ")
        printMaze(r)
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        x = x + 1
if __name__ == '__main__':
    main()  

