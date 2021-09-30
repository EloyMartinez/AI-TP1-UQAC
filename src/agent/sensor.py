class sensor:
    
    def __init__(self,isOn):
        self._isOn = isOn
        self.perfomance = 0

    def get_performance(self):
        return self.perfomance
    
    def set_performance(self, new_performance):
        self.perfomance = new_performance
        
    def capture(self,grid):
        return grid.clone()
    
    def mesure_performance(self,aspi,action):
        perf = self.get_performance()
        if(action=='grab'):
            print("+10 car GRAB")
            perf = perf + 5
        if(action == 'suck'):
            if((aspi.get_bdi().get_belief()[aspi.get_x()][aspi.get_y()]).get_jewel()):
                print("-30 car SUCK jewel")
                perf = perf - 30
            else:
                perf = perf + 10
                print("+20 car SUCK")
            print("-1 car suck")
            perf = perf - 1 #L'energie depense
        else:
            print("-1 car bouger")
            perf = perf - 1 #pour tout autre mouvement   ##si on bouge pas on depense pas d'energie
        self.set_performance(perf)
    

     
        
    