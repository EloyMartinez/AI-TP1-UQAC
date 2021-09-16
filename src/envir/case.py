import random as random   
import logging as logging
#logging.basicConfig(level=logging.INFO) #To activate loggers


class Case:

    def __init__(self, x, y,bijoux, salete):
        self._bijoux = bijoux
        self._salete = salete
        self._x = x
        self._y = y

    def get_bijoux(self):
        return self._bijoux

    def set_bijoux(self,bijoux):
        self._bijoux = bijoux

    def get_salete(self):
        return self._salete

    def set_salete(self,salete):
        self.salete = salete

    def get_x(self):        
        return self._x
    
    def set_x(self, x): 
        self._x = x 

    def get_y(self):
        return self._y
    
    def set_y(self, y): 
        self._y = y 
        
    def generate_bijoux(self):
        prob = random.random()
        if(prob<0.9):
             if (not self.get_bijoux()):
                self.set_bijoux(True)
                logging.info("Bijoux ajoute en "+str(self.get_x())+","+str(self.get_y()))
        else:
            self._bijoux = False
    
    def generate_salete(self):
        prob = random.random()
        if(prob<0.9):
            if (not self.get_salete()):
                self.set_salete(True)
                logging.info("Salete ajoute en "+str(self.get_x())+","+str(self.get_y()))
        else:
            self._bijoux = False
            
        
