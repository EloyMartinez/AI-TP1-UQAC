#
# Travail n°1 - IA - UQAC
# Robot aspirateur
#
#

from agent.bdi import Bdi
from agent.noeud import Noeud
from agent.sensor import sensor
from agent.effecteurs import Effecteurs
import time

class Aspi:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._effecteurs= Effecteurs()
        self._bdi = Bdi()
        self._sensor = sensor(True)

    def get_x(self):        
        return self._x

    def set_x(self, x): 
        self._x = x 

    def get_y(self):
        return self._y

    def set_y(self, y): 
        self._y = y 

    def get_ressoucres(self):
        return self._ressources

    def get_effecteurs(self):
        return self._effecteurs

    def set_sensor(self, sensor): 
        self._sensor = sensor

    def get_sensor(self): 
        return self._sensor

    def get_bdi(self):
        return self._bdi

    def set_bdi(self,bdi):
        self._bdi=bdi


    #Fonction qui va permettre à l'aspirateur de connaître la grille
    def useSensor(self,grid,count,intMesure):
        if ((count % intMesure) == 0) or count < 3:
            newgrid = self._sensor.capture(grid)
            self._bdi.set_belief(newgrid)
            print("-1 use sensor")
            self.get_sensor().set_performance(self.get_sensor().get_performance()-1)

    #Fonction qui va permettre de trouver la case sale la plus proche
    def findBoxGoal(self):
        closest = []  #This is an object : supposed to be a case
        for x in range(0, 5):
            for y in range(0, 5):
                #Pour chaque Case de la grille que connaît l'aspirateur
                currentCase = self.get_bdi().get_belief()[x][y]
                #Vérifie s'il y a de la saleté
                if(currentCase.get_dirt()):
                    #Si sale alors on calcule la distance avec la case courante avec distance()
                    if(self.distance(closest,currentCase)):
                        #Si c'est la plus proche on affecte cette case a closest
                        closest = currentCase
        #A la fin du parcours de toutes les cases
        #Vérifie si le tableau est vide
        if(closest == []):
            return None
        #On retourne la case
        return closest

    #Fonction pour calculer la norme entre 2 cases : la case actuelle et la case que l'on veut comparer
    def norme(self,potentialGoal):
        return (abs(potentialGoal.get_x() - self.get_x()) + abs(potentialGoal.get_y() - self.get_y()))

    def distance(self,closestBox,currentCase):
        if closestBox == []:
            return True
        else:
            if(self.norme(closestBox)>self.norme(currentCase)):
                return True
            else:
                return False


    #Fonction qui va affecter à l'aspi une liste d'action
    def setIntent(self):
        action = 'forceStart'  ## This action will allow us to check further actions
        actionList = []
        node = self.aStar(self.get_bdi().get_belief())


        action = node.get_action()            
        while(action != 'origin'):
            actionList.append(action)
            node = node.get_parent()
            action = node.get_action()      
        self.get_bdi().set_intent(actionList)

    #Fonction qui va affecter a l'aspi une liste d'action
    def setIntentBFS(self):
        action = 'forceStart'  ## This action will allow us to check further actions
        actionList = []
        node = self.bfsSearch(self.get_bdi().get_belief())

        while(action != 'origin'):
            action = node.get_action()
            node = node.get_parent()
            actionList.append(action)
        self.get_bdi().set_intent(actionList)

    #Fonction qui va affecter a l'aspi une liste d'action
    def setIntentDFS(self):
        action = 'forceStart'  ## This action will allow us to check further actions
        actionList = []
        node = self.dfsSearch(self.get_bdi().get_belief())

        while(action != 'origin'):
            action = node.get_action()
            node = node.get_parent()
            actionList.append(action)
        self.get_bdi().set_intent(actionList)

    #Algo de recherche informé
    def aStar(self,grid):
        #On trouve la case que l'on veut
        goal = self.findBoxGoal()
        #On instancie un noeud sans parent, avec la norme avec la goal case, comme action origin, profondeur de 0 et la case courante
        if(goal==None):
            return Noeud(None,0,0,'origin',0,grid[self.get_x()][self.get_y()]); 
        else:
            startNode = Noeud(None,0,self.norme(goal),'origin',0,grid[self.get_x()][self.get_y()]) 

        nodelist = []
        nodelist.append(startNode)
        while(not self.isSuck(nodelist[0])):

            node = nodelist[0]

            if self.isGrab(nodelist[0]):
                if(node.get_parent() == None):
                    node = Noeud(node,1,0,'grab',node.get_depth()+1, node.get_currentCase())
                else:
                    node = Noeud(node,node.get_parent().get_cost()+1,0,'grab',node.get_depth()+1, node.get_currentCase())
            del nodelist[0]
            nodelist = nodelist+node.expand(self.get_bdi().get_belief(),self,goal)

            self.sort(nodelist)

        return nodelist[0]

    def mesurePerformance(self,action,node):
        point = self.get_points()
        if(action=='grab'):
            point = point + 10
        if(action == 'suck'):
            if((self.get_bdi().get_belief()[node.get_currentCase().get_x()][node.get_currentCase().get_y()]).get_dirt()):
                point = point + 20
            if((self.get_bdi().get_belief()[node.get_currentCase().get_x()][node.get_currentCase().get_y()]).get_jewel()):
                point = point - 30
            point = point - 1 #L'energie depense
        else:
            point = point - 1 #pour tout autre mouvement   ##si on bouge pas on depense pas d'energie
        self.set_points(point)

    #Calculer le cout 
    def calculateCost(self,node):
        action = 'forceStart' 
        cost = 0
        while (action != 'origin'):  ## noeud initial
            action = node.get_action()
            cost = cost + node.get_cost()
            node = node.get_parent()
        return cost


    #Renvoie True si l'action du noeud est d'aspirer ou de ramasser
    def isGrabOrSuck(self,node):
        if(node.get_action()=='grab' or node.get_action()=='suck'):
            return True
        else:
            return False

    #Renvoie True si l'action est d'aspirer
    def isSuck(self,node):
        if(node.get_action()=='suck'):
            return True
        else:
            return False

    #Renvoie True si l'action est de ramasser
    def isGrab(self,node):
        if(node.get_currentCase().get_jewel()==1):
            return True
        else:
            return False



    #Fonction pour trier les noeuds en fonction de leur cout et distance
    def sort(self, list_noeud):
        list_noeud.sort(key=lambda x: int(x.get_cost())+int(x.get_distance()))

    def bfsSearch(self,grid):
        queue = []
        visited = []
        startNode = Noeud(None,0,0,'origin',0,grid[self.get_x()][self.get_y()]) 
        result =  self.bfsRecursive(grid,queue,visited,startNode)
        if result == None:
            return startNode
        else:
            return result

    def bfsRecursive(self,arr,queue,visited,node):
        queue =    queue + node.expandBFS(arr,visited) ### node.expandBFS(arr,visited) + queue pour faire depth search
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
            return self.bfsRecursive(arr,queue,visited,currentNode)

    def dfsSearch(self,grid):
        queue = []
        visited = []
        startNode = Noeud(None,0,0,'origin',0,grid[self.get_x()][self.get_y()]) 
        result =  self.dfsRecursive(grid,queue,visited,startNode)
        if result == None:
            return startNode
        else:
            return result

    def dfsRecursive(self,arr,queue,visited,node):
        queue =    node.expandBFS(arr,visited) + queue  
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
            return self.dfsRecursive(arr,queue,visited,currentNode)

    def update_pos(self, grid, reelGrid, lock):
        action = self.get_bdi().get_intent()
        action.reverse()
        for a in action:
            lock.acquire()
            try:
                if(a == "suck"):
                    self.get_effecteurs().clean_case(grid[self.get_x()][self.get_y()])
                    self.get_effecteurs().clean_case(reelGrid.get_arr()[self.get_x()][self.get_y()])
                    reelGrid.update_dirt((self.get_x()*100), (self.get_y()*100))
                    reelGrid.update_jewel(self.get_x()*100, (self.get_y()*100))
                elif(a == "grab"):
                    self.get_effecteurs().grab_jewel(reelGrid.get_arr()[self.get_x()][self.get_y()])
                    self.get_effecteurs().grab_jewel(grid[self.get_x()][self.get_y()])
                    reelGrid.update_jewel(self.get_x()*100, (self.get_y()*100))
                else:
                    posx = self.get_x()
                    posy = self.get_y()
                    self.get_effecteurs().move(self,a)
                    reelGrid.update_vaccum((posx*100)+40, (posy*100)+40, self.get_x(),self.get_y())
                reelGrid.main()
            finally:
                lock.release()
            self.get_sensor().mesure_performance(self, a)


            time.sleep(0.2)



    
     
        
                
                
        
        
