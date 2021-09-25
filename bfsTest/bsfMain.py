import sys
sys.path.append("../")
from src.envir.case import Case
from bfsGrid import bfsGrid
from breathFirst import *

def display(grid):
    for x in range(0, 5):
        for y in range(0, 5):
            print(str(x) + "  " + str(y))
            print(grid._arr[x][y].get_dirt())
            print("\n")

if __name__ == "__main__":
    grid = bfsGrid()
    grid.initialize()
    grid.add_dirt(3,3)
    nodefin = bfsSearch(grid)
    print(nodefin)
    
