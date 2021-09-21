from agent import effecteurs
from agent.effecteurs import Effecteurs
from agent.bdi import Bdi
from agent.noeud import Noeud

class Aspi:

    def __init__(self, x, y, ressources):
        self._x = x
        self._y = y
        self._ressources= ressources
        self._effecteurs= Effecteurs()
        self._bdi = Bdi()
    
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
    
   
    #Fonction qui va permettre à l'aspirateur de connaitre la grille
    def useSensor(self,grid):
        #C'est un tableau
        self._bdi.set_belief = grid.clone()


    ## ATTENTION ICI, L'OBJET VA PRENDRE UNE VALEUR CAR ON LUI AFFECTE UNE VALEUR DE ARRAY
    def findBoxGoal(self):
        closest = []  #this is supposed to be a case
        for x in range(0, 5):
            for y in range(0, 5):
                #Pour chaque Case de la grille que connait l'aspi
                currentCase = self.get_bdi().get_belief()[x][y]
                #Check pour voir la saleté
                if(currentCase.get_dirt()):
                    #Si sale alors on clacule la distance avec la case courante avec distance()
                    if(self.distance(self,closest,currentCase)):
                        #Si c'est la plus proche on affecte cette case a closest
                        closest = currentCase
        #A la fin du parcours de toutes les cases
        #Check si le tableau est vide
        if(closest == []):
            return None  ### !!!!! WE HAVE TO CHECK IF RESULT IS NOT NONE
        #On retourne la case
        return closest
    
    #Calculer la norme entre 2 cases : la case actuelle et la case que l'on veut comparer
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
   

    def setIntent(self):
        action = 'forceStart'  ## this action will allow us to check further actions
        actionList = []
        node = aStar(self.get_bdi().get_belief())
        while(action != 'origin'):
            action = node.get_action()
            node = node.get_parent()
            actionList.append(action)
        self.set_bdi().set_intent(actionList)
    
    #Algo de recherche informé
    def aStar(self,grid):
        #On trouve la case que l'on veut
        goal = self.findBoxGoal()
        #On instancie un noeud sans parent, avec la norme avec la goal case, comme action origin, profondeur de 0 et la case courante
        startNode = Noeud(None,0,self.norme(goal),'origin',0,grid.get_arr()[self.get_x()][self.get_y()]) 
        if(goal==None):
            return startNode
        #Creation d'un objet vide
        nodelist = []
        nodelist.append(startNode)
        while(not self.isGrabOrSuck(nodelist[0])):
            node = nodelist[0]
            del nodelist[0]
            nodelist =+ node.expand(self.get_bdi().get_belief(),self)  ## we want to add list of extended nodes into list of nodes  //array concatination
            sort(nodelist)# a implementer
        return nodelist[0]
            
    #Point a mettre en global
    def mesurePerformance(self,action,node):
        point = 0
        if(action=='grab'):
            point = point + 10
        if(action == 'suck'):
            if((self.get_bdi().get_belief()[node.get_currentCase().get_x()][node.get_currentCase().get_y()]).get_dirt()):
                point = point + 20
            if((self.get_bdi().get_belief()[node.get_currentCase().get_x()][node.get_currentCase().get_y()]).get_jewel()):
                point = point - 30
            point = point - 1 #L'energie depense
        else:
            point = point - 1 #pour tout autre mouvement
            
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
        
        
                
                
        
        
