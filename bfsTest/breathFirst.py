import sys
sys.path.append('../')
from src.agent.noeud import Noeud
    
    
             
def bfsSearch(grid):
        queue = []
        visited = []
        startNode = Noeud(None,0,0,'origin',0,grid.get_arr()[0][0]) 
        return bfsRecursive(grid.get_arr(),queue,visited,startNode)
    
def bfsRecursive(arr,queue,visited,node):
        queue =    queue +node.expandBFS(arr,visited) ### ceci peut bugger si liste vide
        print(node.get_currentCase().get_coords())
        currentNode = queue[0]
        del queue[0]
        if currentNode.get_currentCase().get_dirt() == True or currentNode.get_currentCase().get_jewel() == True:
            return currentNode
        else:
            visited.append(currentNode.get_currentCase().get_coords())
            return bfsRecursive(arr,queue,visited,currentNode)
    
    
    
    

