import random  
import logging
import pygame
#logging.basicConfig(level=logging.INFO) #To activate loggers


class Case:

    # Constructeur
    def __init__(self, x, y, jewel, dirt, grid):
        self._jewel = jewel
        self._dirt = dirt
        self._x = x
        self._y = y
        self._grid = grid



    # Getters/Setters
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
        if(prob<0.2):
            if (not self.get_jewel()):
                self.set_jewel(True)
                self.get_grid().add_jewel(self.get_x(),self.get_y())
                logging.info("Bijoux ajoute en "+str(self.get_x())+","+str(self.get_y()))
        else:
            self._jewel = False
    
    def generate_dirt(self):
        prob = random.random()
        if(prob<0.7):
            if (not self.get_dirt()):
                self.set_dirt(True)
                self.get_grid().add_dirt(self.get_x(),self.get_y())
                logging.info("Salete ajoute en "+str(self.get_x())+","+str(self.get_y()))
        else:
            self._dirt = False
            
        
