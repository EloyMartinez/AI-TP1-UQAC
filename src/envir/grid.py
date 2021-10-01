import os
#Hide pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
from envir.case import Case
import time

white_color = (230, 230, 230)
black_color = (0,0,0)


class Grid:

    ### Constructeur
    def __init__(self):
        pygame.init()
        self._height = 500
        self._cols = 5
        self._rows = 5
        self._width= 500
        self._blocksize = 100
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._screen.fill(white_color)
        self._arr = [[0 for i in range(0,5)] for y in range(0,5)] 

    
    
    ### Getters/Setters
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
        
    def get_block(self):
        return self._blocksize

    def get_arr(self):
        return self._arr



    ### Methodes
    
    #Fonction pour initialiser la grille
    #On va parcourir x et y de 0 à 500 avec un pas de 100
    def initialize(self):
        for x in range(0, self.get_width(),  self.get_block()):
            for y in range(0, self.get_height(), self.get_block()):
                pygame.draw.rect(self._screen, black_color, (x, y, self._blocksize, self._blocksize), 2)
                self._arr[int(x/100)][int(y/100)] = Case(int(x/100),int(y/100),False,False,self)
                
    def clone(self):
        clone_array = [[0 for i in range(0,5)] for y in range(0,5)] 
        for x in range(0, self.get_width(),  self.get_block()):
            for y in range(0, self.get_height(), self.get_block()):
                clone_array[int(x/100)][int(y/100)] = self._arr[int(x/100)][int(y/100)].clone()
        return clone_array
        
    
    #Fonction pour generer les bijoux et salete
    def generate_environment(self):
        for i in range(0,self._cols):
            for j in range(0,self._rows):
                (self._arr[i][j]).generate_jewel()
                (self._arr[i][j]).generate_dirt()





    def add_jewel(self,x,y):
        self.display_jewel((x*100),(y*100))

    def add_dirt(self,x,y):
        self.display_dirt((x*100),(y*100))
                    
    #Fontion d'execution
    def execute(self):
        self.generate_environment()


    def display_dirt(self,x,y):
        dirt = pygame.image.load('envir/img/dirt.png')
        pic_dirt = pygame.transform.scale(dirt, (40, 40))
        self._screen.blit(pic_dirt, (x,y))
        


    def display_jewel(self,x,y):
        jewel = pygame.image.load('envir/img/jewel.png')
        pic_jewel = pygame.transform.scale(jewel, (50, 50))
        self._screen.blit(pic_jewel, (x+50,y-9))


    def add_vaccum(self, x, y):
        vaccum= pygame.image.load('envir/img/vaccum.png')
        pic_vaccum = pygame.transform.scale(vaccum, (50, 50))
        self._screen.blit(pic_vaccum, ((x*100)+40,(y*100)+40))


    def update_vaccum(self, x_vaccum, y_vaccum, newx, newy):
        pygame.draw.rect(self._screen,white_color, (x_vaccum, y_vaccum, 50,50))
        vaccum= pygame.image.load('envir/img/vaccum.png')
        pic_vaccum = pygame.transform.scale(vaccum, (50, 50))
        self._screen.blit(pic_vaccum, ((newx*100)+40,(newy*100)+40))

    def update_dirt(self, x_vaccum, y_vaccum):
        pygame.draw.rect(self._screen,white_color, (x_vaccum+2, y_vaccum+2, 40,40))
    
    def update_jewel(self, x_vaccum, y_vaccum):
        pygame.draw.rect(self._screen,white_color, (x_vaccum+49, y_vaccum+2, 49,37))

    #Boucle pour l'affichage de la grille
    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


    #Boucle pour l'affichage de la grille
    def display(self):
        print(self.get_arr())
               
