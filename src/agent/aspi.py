from agent import effecteurs
from agent.effecteurs import Effecteurs
from agent.bdi import Bdi

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
    
    def useSensor(self,grid):
        self._bdi.set_belief = grid.clone()
        
    def findBoxGoal(self):
        closest = []
        for x in range(0, 5):
            for y in range(0, 5):
                currentCase = self.get_bdi().get_belief()[x][y]
                if(currentCase.get_dirt()):
                    if(self.distance(self,closest,currentCase)):
                        closest = currentCase
        if(closest == []):
            return None  ### !!!!! WE HAVE TO CHECK IF RESULT IS NOT NONE
        return closest
    
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
            
    
    
    
'''   def move_right(self):
        if(self.get_x() < 4):
            self.set_x(self.get_x()+1)

    def move_left(self):
        if(self.get_x() > 0):
            self.set_x(self.get_x()-1)

    def move_up(self):
        if(self.get_y() < 4):
            self.set_y(self.get_y()+1)

    def move_down(self):
        if(self.get_y() > 0):
            self.set_y(self.get_y()-1)
            
    def useSensor(self,grid):
        self._bdi.set_belief = grid.clone()  ## this allows the vacuum to have in its memory a picture of its environment
        
    def setIntent():
        action = 'forceStart'  ## this action will allow us to check further actions
        actionList = []
 '''        
        
