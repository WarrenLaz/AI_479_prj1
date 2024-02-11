import tkinter
from tkinter import *

window = Tk()
window.title("Maze Display")
window.geometry("1750x500")

numGraphs = 5 #number of displayed graphs
run = 0 #the number of the run that we are currently on; run goes from 0 to 9
numDFS = 1 #the number of DFS Graphs per run
numBFS = 1 #the number of BFS Graphs per run
numAStar = 1 #the number of AStar Graphs per run

rowsPerGraph = 10 + 2 #the number of lines in each graph + 2 for the lines and name of graph

def open_txt(): #writes to each textbox
    delete()
    outputFile = open("output.txt", 'r')
    mazeFile = outputFile.readlines()

    numLines = rowsPerGraph * numGraphs

    for x in range(0 + run * numLines, numLines + run*numLines):
        if x - run * numLines <= rowsPerGraph - 1:
            generatedGraph.insert(END, mazeFile[x])
        elif x - run * numLines <= rowsPerGraph - 1 + rowsPerGraph * numDFS:
            DFSGraph.insert(END, mazeFile[x])
        elif x - run * numLines <= rowsPerGraph - 1 + rowsPerGraph * numDFS + rowsPerGraph * numBFS:
            BFSGraph.insert(END, mazeFile[x])
        elif x - run * numLines <= rowsPerGraph - 1 + rowsPerGraph * numDFS + rowsPerGraph * numBFS + rowsPerGraph * numAStar:
            AStarGraph.insert(END, mazeFile[x])
        elif x - run * numLines <= rowsPerGraph - 1 + rowsPerGraph * numDFS + rowsPerGraph * numBFS + rowsPerGraph * numAStar + rowsPerGraph:
            DijkstraGraph.insert(END, mazeFile[x])
    
    #DFSGraph.insert(END, "Number of Nodes Expanded:")
    
    runNumText.insert(END, 'Maze Run #' + str(run + 1))

    outputFile.close()

def next_maze_group():
    global run
    if run == 9:
        run = -1
    run = run + 1
    open_txt()

def previous_maze_group():
    global run
    if run == 0:
        run = 10
    run = run - 1
    open_txt()

def delete(): #clear each textbox
    generatedGraph.delete("1.0", "end")
    DFSGraph.delete("1.0", "end")
    BFSGraph.delete("1.0", "end")
    AStarGraph.delete("1.0", "end")
    DijkstraGraph.delete("1.0", "end")
    runNumText.delete("1.0", "end")
    

textboxPack = Frame(window)
textboxPack.pack(pady=20)

generatedGraph = Text(window, width=40, height=15)
generatedGraph.pack(in_=textboxPack,side = LEFT)

DFSGraph = Text(window, width=40, height=15)
DFSGraph.pack(in_=textboxPack, side = LEFT)

BFSGraph = Text(window, width=40, height=15)
BFSGraph.pack(in_=textboxPack, side = LEFT)

AStarGraph = Text(window, width=40, height=15)
AStarGraph.pack(in_=textboxPack, side = LEFT)

DijkstraGraph = Text(window, width=40, height=15)
DijkstraGraph.pack(in_=textboxPack, side = LEFT)


buttonPack = Frame(window)
buttonPack.pack()

previous_maze_button = Button(window, text="Previous Set of Mazes", command=previous_maze_group)
previous_maze_button.pack(in_= buttonPack, side = LEFT)

open_button = Button(window, text="Open Mazes", command=open_txt)
open_button.pack(padx=20, in_= buttonPack, side = LEFT)

next_maze_button = Button(window, text="Next Set of Mazes", command=next_maze_group)
next_maze_button.pack(in_= buttonPack, side = LEFT)

runNumText = Text(window, width=12, height=1)
runNumText.pack(pady=20)

window.mainloop()