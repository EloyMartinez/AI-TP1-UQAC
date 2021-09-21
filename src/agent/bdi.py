class Bdi:
    
    def __init__(self):
        self._belief = [[0 for i in range(0,5)] for y in range(0,5)] 
        self._intent = []
        
    def get_belief(self):
        return self._belief
    
    def set_belief(self,array):
        self._belief = array
        
    def get_intent(self):
        return self._intent
    
    def set_intent(self,intent):
        self._intent=intent
        
    
   
