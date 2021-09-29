import sys
sys.path.append('../')
from src.agent.noeud import Noeud
    
    
             
def bfsSearch(grid):
        queue = []
        visited = []
        startNode = Noeud(None,0,0,'origin',0,grid.get_arr()[0][0]) 
        result =  bfsRecursive(grid.get_arr(),queue,visited,startNode)
        if result == None:
            return startNode
        else:
            return result
    
def bfsRecursive(arr,queue,visited,node):
        queue =    queue + node.expandBFS(arr,visited) ### node.expandBFS(arr,visited) + queue pour faire depth search
        print(node.get_currentCase().get_coords())
        currentNode = queue[0]
        del queue[0]
        if queue == []:
            return None
        if(currentNode.get_depth() > 20):
            return None
        if currentNode.get_currentCase().get_jewel() == True:
            if(currentNode.get_parent() == None):
                    currentNode = Noeud(currentNode,1,0,'grab',currentNode.get_depth()+1, currentNode.get_currentCase())
            else:
                    currentNode = Noeud(currentNode,currentNode.get_parent().get_cost()+1,0,'grab',currentNode.get_depth()+1, currentNode.get_currentCase())
        if currentNode.get_currentCase().get_dirt() == True:
            if(currentNode.get_parent() == None):
                    currentNode = Noeud(currentNode,1,0,'suck',currentNode.get_depth()+1, currentNode.get_currentCase())
            else:
                    currentNode = Noeud(currentNode,currentNode.get_parent().get_cost()+1,0,'suck',currentNode.get_depth()+1, currentNode.get_currentCase())
            return currentNode
        else:
            visited.append(currentNode.get_currentCase().get_coords())
            return bfsRecursive(arr,queue,visited,currentNode)
    
    
    
    

