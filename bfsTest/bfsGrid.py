import sys
sys.path.append('../')
from src.envir.case import Case


class bfsGrid:
    
    def __init__(self):
        self._arr = [[0 for i in range(0,5)] for y in range(0,5)] 
        
    def get_arr(self):
        return self._arr


    def initialize(self):
        for x in range(0, 5):
            for y in range(0, 5):
               self._arr[int(x)][int(y)] = Case(int(x),int(y),False,False,self)
               
    def add_dirt(self,x,y):
        (self._arr[x][y]).forceDirt()
        