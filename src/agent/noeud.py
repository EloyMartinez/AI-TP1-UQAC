class Noeud:
    
    def __init__(self, parent, cost ,distance, action, depth, currentCase):
        self._parent = parent
        self._cost = cost
        self._distance = distance
        self._action = action
        self._depth = depth
        self._currentCase = currentCase
        
    def get_parent(self):        
        return self._parent
    
    def set_parent(self, parent): 
        self._parent = parent
        
    def get_cost(self):        
        return self._cost
    
    def set_cost(self, cost): 
        self._cost = cost
        
    def get_distance(self):        
        return self._distance
    
    def set_distance(self, distance): 
        self._distance = distance
    
    def get_action(self):        
        return self._action
    
    def set_action(self, action): 
        self._action = action
        
    def get_depth(self):        
        return self._action
    
    def set_depth(self, depth): 
        self._action = depth
        
    def get_currentCase(self):        
        return self._currentCase
    
    def set_currentCase(self, currentCase): 
        self._action = currentCase
        
    def expand(self,grid,aspi):
        succesors = []
        actions = self.possibleActions()
        goalCase = aspi.findBoxGoal()  #we get the goalCase once bc the agent doesnt move till the end of the sim
        if(goalCase!=None):
            for a in actions:
                currentCase=self.actionCase(a,grid)
                succesors.append(Noeud(self,self.get_parent.get_cost() + 1,self.norme(currentCase,goalCase),a,self.get_depth()+1,currentCase))
            return succesors
        else:
            return None ### we have to check if return is none
             
            
    def norme(self,currentcase,goal):
        return (abs(goal.get_x() - currentcase.get_x()) + abs(goal.get_y() - currentcase.get_y()))
 
 
    def possibleActions(self):
        actions = []
        if self._currentCase.getJewel() == 1:
            actions.append("grab")
        if self._currentCase.getDirt() == 1:
            actions.append("suck")
        if self._currentCase.getPositionJ() != 5:
            actions.append("right")
        if self._currentCase.getPositionJ() != 0:    
            actions.append("left")
        if self._currentCase.getPositionI() != 5:
            actions.append("down")
        if self._currentCase.getPositionI() != 0:
            actions.append("up")
        return actions
    
    def actionCase(self,action,grid):
        currentActionCase = ((grid.get_arr())[self.get_currentCase().get_x()][self.get_currentCase().get_y()]).clone()
        if(action == "grab"):
            currentActionCase.set_jewel(False)
        elif(action == "suck"):
            currentActionCase.set_jewel(False)
            currentActionCase.set_dirt(False)
        elif(action == "right"):
            if(currentActionCase.get_x() < 4):
                currentActionCase= ((grid.get_arr())[self.get_currentCase().get_x()+1][self.get_currentCase().get_y()]).clone()
        elif(action == "left"):
            if(currentActionCase.get_x() > 0):
                currentActionCase= ((grid.get_arr())[self.get_currentCase().get_x()-1][self.get_currentCase().get_y()]).clone()
        elif(action == "down"):
            if(currentActionCase.get_y() < 4):
                currentActionCase= ((grid.get_arr())[self.get_currentCase().get_x()][self.get_currentCase().get_y()]+1).clone()
        elif(action == "up"):
            if(currentActionCase.get_y() > 0):
                currentActionCase= ((grid.get_arr())[self.get_currentCase().get_x()][self.get_currentCase().get_y()]-1).clone()
        return currentActionCase


	
        