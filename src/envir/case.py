#
# Travail n°1 - IA - UQAC
# Robot aspirateur
#
#

import random  
import logging
#logging.basicConfig(level=logging.INFO) #To activate loggers


class Case:

    # Constructeur
    def __init__(self, x, y, jewel, dirt, grid):
        self._jewel = jewel
        self._dirt = dirt
        self._x = x
        self._y = y
        self._grid = grid
        self._coords = str(x)+","+str(y)



    # Getters/Setters
    def get_coords(self):
        return self._coords

    def get_jewel(self):
        return self._jewel

    def set_jewel(self,jewel):
        self._jewel = jewel

    def get_dirt(self):
        return self._dirt

    def set_dirt(self,dirt):
        self._dirt = dirt

    def get_x(self):        
        return self._x

    def set_x(self, x): 
        self._x = x 

    def get_y(self):
        return self._y

    def set_y(self, y): 
        self._y = y 

    def get_color(self):
        return self._color

    def get_grid(self):
        return self._grid



    # Methodes
    def generate_jewel(self):
        prob = random.random()
        if (not self.get_jewel()):
            if(prob<0.01):
                    self.set_jewel(True)
                    self.get_grid().add_jewel(self.get_x(),self.get_y())
                    logging.info("Bijoux ajoute en "+str(self.get_x())+","+str(self.get_y()))
            else:
                self._jewel = False

    def generate_dirt(self):
        prob = random.random()
        if (not self.get_dirt()):
            if(prob<0.03):
                    self.set_dirt(True)
                    self.get_grid().add_dirt(self.get_x(),self.get_y())
                    logging.info("Salete ajoute en "+str(self.get_x())+","+str(self.get_y()))
            else:
                self._dirt = False

    #force add dirt to enable easy testing       
    def forceDirt(self):                    
        self.set_dirt(True)

    #force add jewel to enable easy testing       
    def forceJewel(self):                    
        self.set_jewel(True)


    def clone(self):
        return Case(self.get_x(),self.get_y(),self.get_jewel(),self.get_dirt(),self.get_grid())