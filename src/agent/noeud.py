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
        
	# def expand(grid, agent) {
	# 	 successors = []
	# 	 actions = self.possibleActions()
	# 	for (String act : actions) {
	# 		Node s = new Node(this, simulAct(act, belief), act, this.depth + 1, costAction(action) + parent.getCost(),
	# 				0);
	# 		if (agent != null) {
	# 			s.affectHeuristique(agent);
	# 		}
	# 		successors.add(s);
	# 	}
	# 	return successors;
	# }
 
 
    def possibleActions(self):
        actions = []
        if currentCase.getJewel() == 1:
            actions.append("grab")
        if currentCase.getDirt() == 1:
            actions.append("aspire")
        if currentCase.getPositionJ() != 5:
            actions.append("right")
        if currentCase.getPositionJ() != 0:    
            actions.append("left")
        if currentCase.getPositionI() != 5:
            actions.append("down")
        if currentCase.getPositionI() != 0:
            actions.append("up")
        return actions

	
        