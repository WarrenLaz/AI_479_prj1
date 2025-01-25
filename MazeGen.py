import random

class Maze: 
    
    def __init__(self) -> None:
        pass

    def createMaze(x, y, density): #10x10
        
        l,w = (y,x) #x = 10, y = 5 therefore l = 5, w = 10
        maze = [['x' for _ in range(w)] for _ in range(l)] #5x10

        start, end = ([random.randint(0,l-1), random.randint(0,w-1)], [random.randint(0,l-1), random.randint(0,w-1)])

        while(start[0] == end[0] and start[1] == end[1]):
            end =  [random.randint(0,l-1), random.randint(0,w-1)]

        maze[start[0]][start[1]] = 'S'

        maze[end[0]][end[1]] = 'G'

        return [Maze.createMazeAux(maze, start, end, density) , start, end]

    def createMazeAux(maze, s, e, density):
        l = len(maze)
        w = len(maze[0])
        visited = [[0 for _ in range(w)] for _ in range(l)]
        visited[s[0]][s[1]] = 1
        visited[e[0]][e[1]] = 1
        temp = s[0]

        if s[0] > e[0]:
            while temp != e[0]:
                temp = temp - 1
                if visited[temp][s[1]] != 1:
                    maze[temp][s[1]] = '.'
                    visited[temp][s[1]] = 1
        if s[0] < e[0]:
            while temp != e[0]:
                temp = temp + 1
                if visited[temp][s[1]] != 1:
                    maze[temp][s[1]] = '.'
                    visited[temp][s[1]] = 1
        temp2 = s[1]
        if s[1] > e[1]:
            while temp2 != e[1]:
                temp2 = temp2 - 1
                if visited[temp][temp2] != 1:
                    maze[temp][temp2] = '.'
                    visited[temp][temp2] = 1
        if s[1] < e[1]:
            while temp2 != e[1]:
                temp2 = temp2 + 1
                if visited[temp][temp2] != 1:
                    maze[temp][temp2] = '.'
                    visited[temp][temp2] = 1
        temp = 0
        temp2 = 0

        while (Maze.sumLL(visited) / (l*w)) < density:
            randpoint1 = random.randint(0,l-1)
            randpoint2 = random.randint(0,w-1)
            if visited[randpoint1][randpoint2] != 1:
                visited[randpoint1][randpoint2] = 1
                maze[randpoint1][randpoint2] = '.'

        return maze

    def sumLL(visited):
        SUM = 0
        for w in visited:
            SUM += sum(w)
        return SUM
