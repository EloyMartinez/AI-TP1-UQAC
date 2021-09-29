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
        
    #Fonction expand
    '''
     def expand(self,grid,aspi):
        succesors = []
        actions = self.possibleActions()
        goalCase = aspi.findBoxGoal()  #we get the goalCase once bc the agent doesnt move till the end of the sim
        if(goalCase!=None):
            for a in actions:
                currentCase=self.actionCase(a,grid)
                print("SELF.GET_PARENT")
               # print(self.get_parent())
               # print("L'action est : " + a)
                if(self.get_parent() == None):
                           # startNode = Noeud(None,0,self.norme(goal),str('origin'),0,grid[self.get_x()][self.get_y()]) 
                    tmp = Noeud(self,1,self.norme(currentCase,goalCase),a,1,currentCase)
                   # print(tmp.get_parent())
                    succesors.append(tmp)
                else:
                    succesors.append(Noeud(self,self.get_parent().get_cost() + 1,self.norme(currentCase,goalCase),a,self.get_depth()+1,currentCase))
            return succesors
        else:
            return None ### we have to check if return is none
    '''
   
             
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
        if(action == "grab"):
           # print("GRAB")
            currentActionCase.set_jewel(False)
        elif(action == "suck"):
           # print("SUCK")
            currentActionCase.set_jewel(False)
            currentActionCase.set_dirt(False)
        elif(action == "right"):
            if(currentActionCase.get_x() < 4):
                currentActionCase = (grid)[self.get_currentCase().get_x()+1][self.get_currentCase().get_y()].clone()
               # print("RIGHT -> X : " + str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))
        elif(action == "left"):
            if(currentActionCase.get_x() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()-1][self.get_currentCase().get_y()].clone()
               # print("LEFT -> X : " +str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))

        elif(action == "down"):
            if(currentActionCase.get_y() < 4):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()+1].clone()
               # print("DOWN -> X : " +str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))

        elif(action == "up"):
            if(currentActionCase.get_y() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()-1].clone()
               # print("UP -> X : " + str(currentActionCase.get_x()) + " Y : " + str(currentActionCase.get_y()))

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
                    # startNode = Noeud(None,0,self.norme(goal),str('origin'),0,grid[self.get_x()][self.get_y()]) 
                    tmp = Noeud(self,0,0,a,1,currentCase)
                else:
                    #print(self.get_depth())
                    tmp = Noeud(self,0,0,a,self.get_depth()+1,currentCase)
                succesors.append(tmp)        
        return succesors


      #Fonction expand
    def expand(self,grid,aspi, goalCase):
        succesors = []
        actions = self.possibleActions()
        #goalCase = aspi.findBoxGoal()  #we get the goalCase once bc the agent doesnt move till the end of the sim
        if(goalCase!=None):
            for a in actions:
                currentCase=self.actionCase(a,grid)
                if(self.get_parent() == None):
                    # print("Current case : " + str(currentCase.get_coords))
                    # print("Goal Cases : " + str(goalCase.get_coords))
                    # print("Action : " + str(a))
                    tmp = Noeud(self,1,self.norme(currentCase,goalCase),a,1,currentCase)
                    succesors.append(tmp)
                else:
                    if(a == 'suck'):
                       # print("CAS OU ACTION EST SUCK : ")
                        succesors.append(Noeud(self,self.get_parent().get_cost() + 1,0,a,self.get_depth()+1,currentCase))
                    else:
                        succesors.append(Noeud(self,self.get_parent().get_cost() + 1,self.norme(currentCase,goalCase),a,self.get_depth()+1,currentCase))
            return succesors
        else:
            return None ### we have to check if return is none
    
    def actionCaseBFS(self,action,grid):
        #On clone a chaque fois donc ca bug
        currentActionCase = grid[self.get_currentCase().get_x()][self.get_currentCase().get_y()].clone()
        if(action == "grab"):
            print("GRAB")
            currentActionCase.set_jewel(False)
        elif(action == "suck"):
            print("SUCK")
            currentActionCase.set_jewel(False)
            currentActionCase.set_dirt(False)
        elif(action == "right"):
            if(currentActionCase.get_x() < 4):
                currentActionCase = (grid)[self.get_currentCase().get_x()+1][self.get_currentCase().get_y()].clone()
                print("RIGHT -> X : " + str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))
        elif(action == "left"):
            if(currentActionCase.get_x() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()-1][self.get_currentCase().get_y()].clone()
                print("LEFT -> X : " +str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))

        elif(action == "down"):
            if(currentActionCase.get_y() < 4):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()+1].clone()
                print("DOWN -> X : " +str(currentActionCase.get_x()) + " Y : " +str(currentActionCase.get_y()))

        elif(action == "up"):
            if(currentActionCase.get_y() > 0):
                currentActionCase= (grid)[self.get_currentCase().get_x()][self.get_currentCase().get_y()-1].clone()
                print("UP -> X : " + str(currentActionCase.get_x()) + " Y : " + str(currentActionCase.get_y()))

        return currentActionCase


	
        