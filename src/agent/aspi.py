
from agent.bdi import Bdi
from agent.noeud import Noeud
from agent.sensor import sensor
from agent.effecteurs import Effecteurs

class Aspi:

    def __init__(self, x, y, ressources):
        self._x = x
        self._y = y
        self._ressources= ressources
        self._effecteurs= Effecteurs()
        self._bdi = Bdi()
        self._sensor = sensor(True)
        self._points = 0
    
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

    def set_ressources(self, effecteurs): 
        self._effecteurs = effecteurs 

    def set_ressources(self, ressources): 
        self._ressources = ressources 
        
    def get_bdi(self):
        return self._bdi
    
    def set_bdi(self,bdi):
        self._bdi=bdi
    
    def set_points(self, points):
        self._points = points
    
    def get_points(self):
       return self._points
   
    #Fonction qui va permettre à l'aspirateur de connaitre la grille
    def useSensor(self,grid):
        newgrid = self._sensor.capture(grid)
        self._bdi.set_belief(newgrid)
       
    #Fonction qui va permettre de trouver la case sale la plus proche de nous
    def findBoxGoal(self):
        closest = []  #This is an object : supposed to be a case
        for x in range(0, 5):
            for y in range(0, 5):
                #Pour chaque Case de la grille que connait l'aspi
                currentCase = self.get_bdi().get_belief()[x][y]
               # print("x : " + str(x) + " - y: " + str(y) + "//  currentCase :" +str(currentCase))
                #Check pour voir la saleté
                if(currentCase.get_dirt()):
                    #Si sale alors on clacule la distance avec la case courante avec distance()
                    if(self.distance(closest,currentCase)):
                        #Si c'est la plus proche on affecte cette case a closest
                        closest = currentCase
        #A la fin du parcours de toutes les cases
        #Check si le tableau est vide
        if(closest == []):
            return None  ### !!!!! WE HAVE TO CHECK IF RESULT IS NOT NONE
        #On retourne la case
        print("La case la plus proche " + str(closest))
        print("La case la plus proche X : " +str(closest.get_x()) + " // y : " + str(closest.get_y()))
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
   

    #Fonction qui va affecter a l'aspi une liste d'action
    def setIntent(self):
        action = 'forceStart'  ## This action will allow us to check further actions
        actionList = []
       # print("get belief " + str(self.get_bdi().get_belief())) 
        print()
        print("*******************************************************************************************************************************")
        print()
       # print(self.get_bdi().get_belief())

        node = self.aStar(self.get_bdi().get_belief())

        print("Current Case x : " + str(node.get_currentCase().get_x()))
        print("Current Case y : " + str(node.get_currentCase().get_y()))
        action = node.get_action()
      #  print("Action : " + str(action))            
        while(action != 'origin'):
            print("Action : " + str(action))  
            actionList.append(action)
            action = node.get_parent().get_action()     
            print(action)       
        self.get_bdi().set_intent(actionList)
        print("Voici les actions a réaliser : " + str(actionList))
        
    #Fonction qui va affecter a l'aspi une liste d'action
    def setIntentBFS(self):
        action = 'forceStart'  ## This action will allow us to check further actions
        actionList = []
       # print("get belief " + str(self.get_bdi().get_belief())) 
        print()
        print("*******************************************************************************************************************************")
        print()
       # print(self.get_bdi().get_belief())
        node = self.bfsSearch(self.get_bdi().get_belief())
        print("Current Case x : " + str(node.get_currentCase().get_x()))
        print("Current Case y : " + str(node.get_currentCase().get_y()))

        while(action != 'origin'):
            action = node.get_action()
           # print("Action : " + str(action))
            node = node.get_parent()
            actionList.append(action)
        self.get_bdi().set_intent(actionList)
    
    #Algo de recherche informé
    def aStar(self,grid):
        #On trouve la case que l'on veut
        goal = self.findBoxGoal()
        print("\n\n\n******************************\nLE GOAL EST : " + str(goal) + "\n\n")
        #On instancie un noeud sans parent, avec la norme avec la goal case, comme action origin, profondeur de 0 et la case courante
        if(goal==None):
            print("goal is current case")
            return Noeud(None,0,0,'origin',0,grid[self.get_x()][self.get_y()]); 
        else:
            startNode = Noeud(None,0,self.norme(goal),'origin',0,grid[self.get_x()][self.get_y()]) 
            print("Goal find : En x " + str(goal.get_x()) + " - EN y " + str(goal.get_y()))
        
        #print("grid :" + str(grid))
        #Creation d'un objet vide
        nodelist = []
        nodelist.append(startNode)
        while(not self.isGrabOrSuck(nodelist[0])):
            print("Dans le while isGrabOrSuck")
            node = nodelist[0]
            del nodelist[0]
            nodelist = nodelist+node.expand(self.get_bdi().get_belief(),self)  ## we want to add list of extended nodes into list of nodes  //array concatination
            #for a in nodelist:
                #print(a.get_parent())
            self.sort(nodelist)
        print("On va aller sur ici : " + str(nodelist[0].get_currentCase().get_coords()))
        return nodelist[0]
            
    #Point a mettre en global 
    #Voir ou utiliser cette fonction
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
        

    def isGrabOrSuck(self,node):
        if(self.get_points() < (self.get_points() + self.calculateCost(node))):
            return True
        else:
            return False

    #Fonction pour trier les noeuds en fonction de leur cout et distance
    def sort(self, list_noeud):
        list_noeud.sort(key=lambda x: int(x.get_cost())+int(x.get_distance()))
        
    def bfsSearch(self,arr):
        queue = []
        visited = []
        startNode = Noeud(None,0,0,'origin',0,arr[self.get_x()][self.get_y()]) 
        return self.bfsRecursive(arr,queue,visited,startNode)
    
    def bfsRecursive(self,arr,queue,visited,node):   
            queue =    queue + node.expandBFS(arr,visited) ### node.expandBFS(arr,visited) + queue pour faire depth search
            print(node.get_currentCase().get_coords())
            currentNode = queue[0]
            del queue[0]
            if currentNode.get_currentCase().get_dirt() == True or currentNode.get_currentCase().get_jewel() == True:
                return currentNode
            else:
                visited.append(currentNode.get_currentCase().get_coords())
                return self.bfsRecursive(arr,queue,visited,currentNode)
    

     
        
                
                
        
        
