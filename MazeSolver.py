import heapq as h
import math
import random

class MazeSolver: 
    
    def __init__(self) -> None:
        pass

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
    
    def DFS(maze, s):

        l = len(maze)
        w = len(maze[0])

        DFSmaze = maze
        visited = [[0 for _ in range(w)] for _ in range(l)]
        inorder = []
        stack = []
        stack.append(s)
        while(stack):
            point = stack[len(stack)-1]
            x = point[1]
            y = point[0]
            inorder.append([x,y])
            listpoints = []

            listpoints = MazeSolver.checkBounds(x, y, w, l, visited, DFSmaze, listpoints)

            if(listpoints):
                d = random.choice(listpoints)

                stack.append([d[0],d[1]])
                visited[d[0]][d[1]] = 1
                if(DFSmaze[d[0]][d[1]] == 'G'):
                    return DFSmaze
                elif(not(DFSmaze[d[0]][d[1]] == 'S')):
                    DFSmaze[d[0]][d[1]] = '@'
            else:
                stack.pop()

        return DFSmaze, inorder

    def BFS(maze, s):

        l = len(maze)
        w = len(maze[0])
        visitedinOrder = []
        BFSmaze = maze
        visited = [[0 for _ in range(w)] for _ in range(l)]
        queue1 = []
        queue1.append(s)

        while(queue1):
            visited[queue1[0][0]][queue1[0][1]] = 1
            point = queue1[0]
            x = point[1]
            y = point[0]
            visitedinOrder.append([x,y])
            listpoints = []

            listpoints = MazeSolver.checkBounds(x,y, w, l, visited, BFSmaze, listpoints)

            if(listpoints):
                for h in listpoints:
                    if(not(h in queue1)):
                        queue1.append(h)

                current = queue1[0]

                if(not(BFSmaze[current[0]][current[1]] == 'S' or BFSmaze[current[0]][current[1]] == 'G')):
                    BFSmaze[current[0]][current[1]] = '@'

                if(BFSmaze[current[0]][current[1]] == 'G'):
                    return BFSmaze

            if(queue1):
                queue1.pop(0)

        return BFSmaze, visitedinOrder

    def Djikstras(maze, s, end):
        l = len(maze)
        w = len(maze[0])
        Dijkstrasmaze = maze
        visited = [[0 for _ in range(w)] for _ in range(l)]
        weights = [[float('inf') for _ in range(w)] for _ in range(l)]
        queue1 = []
        queue1.append(s)
        weights[s[0]][s[1]] = 1

        while(queue1):
            visited[queue1[0][0]][queue1[0][1]] = 1
            point = queue1[0]
            x = point[1]
            y = point[0]
            listpoints = []

            listpoints = MazeSolver.checkBounds(x,y, w, l, visited, Dijkstrasmaze, listpoints)

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

        return MazeSolver.AuxDjikstras(Dijkstrasmaze, weights, end)

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
            BFSmaze[pathind[0]][pathind[1]] = '#'
            next = minweight
            x = pathind[1]
            y = pathind[0]


        return BFSmaze

    def Heuristic(x1, x2, y1, y2):
        return  math.sqrt( (x1 - x2)**2 + ((y1 - y2)**2))
    
    def Heuristic2(x1, x2, y1, y2):
        return  abs(x1 - x2) + abs(y1 - y2) 


    def Astar(maze, s, g):
        l = len(maze)
        w = len(maze[0])
        Astarmaze = maze
        visited = [[0 for _ in range(w)] for _ in range(l)]
        queue1 = []

        queue1.append((MazeSolver.Heuristic(s[0], g[0], s[1], g[1]), s))


        while(queue1):
            h.heapify(queue1)
            point = queue1[0][1]
            x = point[1]
            y = point[0]
            listpoints = []
            visited[y][x] = 1

            listpoints = MazeSolver.checkBounds(x, y, w, l, visited, Astarmaze, listpoints)

            if(listpoints):
                hlist = []
                choice = []
                for f in listpoints:
                    hlist.append(MazeSolver.Heuristic(f[0], g[0], f[1], g[1]))

                for i in range(len(listpoints)):
                    choice.append((hlist[i], listpoints[i]))

                for c in choice:
                    if(not(c in queue1)):
                       queue1.append(c)
                    if(Astarmaze[c[1][0]][c[1][1]] == 'G'):
                        return Astarmaze.copy()
                    elif(not(Astarmaze[c[1][0]][c[1][1]] == 'S' or Astarmaze[c[1][0]][c[1][1]] == 'G')):
                        Astarmaze[c[1][0]][c[1][1]] = '@' 

            if(queue1):
                queue1.pop(0)

        return Astarmaze.copy()
