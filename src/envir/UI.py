# import tkinter module
import tkinter as tk
  
winH = 400
winW = 400
ncols = 5
nrows = 5
cellW = winW / ncols
cellH = winH / nrows

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        return

def generatGrid(nrows, ncols):
    grid = []
    for r in range(nrows):
        row = [ Node(r, c) for c in range(ncols) ]
        grid.append(row)
    return grid

def drawNode(canvas, node):
    x1 = cellW * node.col
    y1 = cellH * node.row
    x2 = x1 + cellW
    y2 = y1 + cellH
    canvas.create_rectangle(x1, y1, x2, y2)
    return

def drawGrid(canvas, grid):
    for row in grid:
        for node in row:
            drawNode(canvas, node)
    return

window = tk.Tk()
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()

grid = generatGrid(nrows, ncols)
drawGrid(canvas, grid)

window.mainloop()
