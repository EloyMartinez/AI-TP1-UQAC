import os
#Hide pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
from envir.case import Case
import time


#black_color = (0, 0, 0)
brown_color = (139,69,19)
white_color = (230, 230, 230)

class Grid:

    def __init__(self):
        pygame.init()
        self.height = 500
        self.cols = 5
        self.rows = 5
        self.width= 500
        self.blocksize = 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(white_color)
        self.arr = [[0 for i in range(0,5)] for y in range(0,5)] 

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def get_block(self):
        return self.blocksize

    #Fonction pour initialiser le tableau
    def initialize(self):
        self.add_vaccum()
        for x in range(0, self.get_width(),  self.get_block()):
            for y in range(0, self.get_height(), self.get_block()):
                pygame.draw.rect(self.screen, (0,0,0), (x, y, self.blocksize, self.blocksize), 2)
                self.arr[int(x/100)][int(y/100)] = Case(int(x/100),int(y/100),False,False,self)
    
    #Fonction pour generer les bijoux et salete
    def generateEnvr(self):
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                (self.arr[i][j]).generate_bijoux()
                (self.arr[i][j]).generate_salete()

    def addBijoux(self,x,y):
        self.add_diamond((x*100),(y*100))

    def addSalete(self,x,y):
        self.add_dust((x*100),(y*100))

                    
    #Fontion d'execution
    def execute(self):
        self.generateEnvr()


    #A appeler quand on recoit la notif
    def add_dust(self,x,y):
        dust = pygame.image.load('envir/img/dust.png')
        pic_dust = pygame.transform.scale(dust, (40, 40))
        self.screen.blit(pic_dust, (x,y))
        print("Bijoux : " + str(x) + " " +str(y))


    def add_diamond(self,x,y):
        diamond = pygame.image.load('envir/img/diamond.png')
        pic_diamond = pygame.transform.scale(diamond, (50, 50))
        self.screen.blit(pic_diamond, (x+50,y))
        print("Diamant: " + str(x) + " " +str(y))


    def add_vaccum(self):
        posX = random.randint(0, 4)
        posY = random.randint(0, 4)
        vaccum= pygame.image.load('envir/img/vaccum.png')
        pic_vaccum = pygame.transform.scale(vaccum, (50, 50))
        self.screen.blit(pic_vaccum, ((posX*100)+40,(posY*100)+40))
        self.arr[int(posX)][int(posY)] = 3


    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        print("hello")


if __name__ == "__main__":
    grid = Grid()
    grid.initialize()
    grid.generateEnvr()
    grid.check()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



