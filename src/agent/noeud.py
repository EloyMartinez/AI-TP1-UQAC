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
        return self._depth
    
    def set_depth(self, depth): 
        self._depth = depth
        
    def get_currentCase(self):        
        return self._currentCase
    
    def set_currentCase(self, currentCase): 
        self._action = currentCase


    #Fonction qui calcule la norme entre la case courante et la case goal
    def norme(self,currentcase,goal):
        return (abs(goal.get_x() - currentcase.get_x()) + abs(goal.get_y() - currentcase.get_y()))

    #Fonction liste les actions possible de la case courante
    def possibleActions(self):
        actions = []
        if self._currentCase.get_jewel() == 1:
            actions.append("grab")
        if self._currentCase.get_dirt() == 1:
            actions.append("suck")
        if self._currentCase.get_x() != 4:
            actions.append("right")
        if self._currentCase.get_x() != 0:    
            actions.append("left")
        if self._currentCase.get_y() != 4:
            actions.append("down")
        if self._currentCase.get_y() != 0:
            actions.append("up")
        return actions


    #Fonction qui va simuler les actions 
    def actionCase(self,action,grid):
        currentActionCase = (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()].clone()
        if(action == "right"):
            if(currentActionCase.get_x() < 4):
                currentActionCase = (grid)[self.get_currentCase().get_x()+1][self.get_currentCase().get_y()].clone()

        elif(action == "left"):
            if(currentActionCase.get_x() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()-1][self.get_currentCase().get_y()].clone()

        elif(action == "down"):
            if(currentActionCase.get_y() < 4):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()+1].clone()

        elif(action == "up"):
            if(currentActionCase.get_y() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()-1].clone()

        return currentActionCase


     #Fonction expand
    def expandBFS(self,grid,visited):
        succesors = []
        visited = visited
        actions = self.possibleActions()
        for a in actions:
            currentCase=self.actionCaseBFS(a,grid)
            if currentCase.get_coords() not in visited:
                if(self.get_parent() == None):
                    tmp = Noeud(self,0,0,a,1,currentCase)
                else:
                    tmp = Noeud(self,0,0,a,self.get_depth()+1,currentCase)
                succesors.append(tmp)        
        return succesors


      #Fonction expand
    def expand(self,grid,aspi, goalCase):
        succesors = []
        actions = self.possibleActions()
        if(goalCase!=None):
            for a in actions:
                currentCase=self.actionCase(a,grid)
                if(self.get_parent() == None):
                    tmp = Noeud(self,1,self.norme(currentCase,goalCase),a,1,currentCase)
                    succesors.append(tmp)
                else:
                    if(a == 'suck'):
                        succesors.append(Noeud(self,self.get_parent().get_cost() + 1,0,a,self.get_depth()+1,currentCase))
                    else:
                        succesors.append(Noeud(self,self.get_parent().get_cost() + 1,self.norme(currentCase,goalCase),a,self.get_depth()+1,currentCase))
            return succesors
        else:
            return None ### we have to check if return is none

    def actionCaseBFS(self,action,grid):
        currentActionCase = grid[self.get_currentCase().get_x()][self.get_currentCase().get_y()].clone()
        if(action == "grab"):
            currentActionCase.set_jewel(False)
        elif(action == "suck"):
            currentActionCase.set_jewel(False)
            currentActionCase.set_dirt(False)
        elif(action == "right"):
            if(currentActionCase.get_x() < 4):
                currentActionCase = (grid)[self.get_currentCase().get_x()+1][self.get_currentCase().get_y()].clone()
        elif(action == "left"):
            if(currentActionCase.get_x() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()-1][self.get_currentCase().get_y()].clone()

        elif(action == "down"):
            if(currentActionCase.get_y() < 4):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()+1].clone()

        elif(action == "up"):
            if(currentActionCase.get_y() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()-1].clone()

        return currentActionCase
    


	
        