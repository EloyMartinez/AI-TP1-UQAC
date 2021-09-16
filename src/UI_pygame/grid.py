import os
#Hide pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random

black_color = (0, 0, 0)
brown_color = (139,69,19)
white_color = (230, 230, 230)

class Grid:

    def __init__(self):
        pygame.init()
        self.height = 500
        self.width= 500
        self.blocksize = 100
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(white_color)
        self.array = [[0 for i in range(0,5)] for y in range(0,5)] 


    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def get_block(self):
        return self.blocksize

    #Generer une grille sur l'ecran
    def createGrid(self):
        self.add_vaccum()
        for x in range(0, self.get_width(),  self.get_block()):
            for y in range(0, self.get_height(), self.get_block()):
                #Creation de rectangle noir
                #Where/Color/(x,y,width, height), bordure)
                pygame.draw.rect(self.screen, black_color, (x, y, self.blocksize, self.blocksize), 2)
                self.add_dust(x,y)
                self.add_diamond(x,y)
        print(self.array)

                

    #Boucle
    def run(self):
        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


    def add_dust(self,x,y):
        if(random.uniform(0, 1)<0.6):
            dust = pygame.image.load('img/dust.png')
            pic_dust = pygame.transform.scale(dust, (50, 50))
            self.screen.blit(pic_dust, (x,y))
            if(self.array[int(x/100)][int(y/100)]==3):
                #On ajoute cette case dans le tableau pour ne pas mettre plusieurs choses dedans
                self.array[int(x/100)][int(y/100)] = 4
            else:
                self.array[int(x/100)][int(y/100)] = 1


    def add_diamond(self,x,y):
         if(random.uniform(0, 1)<0.3):
            if(self.array[int(x/100)][int(y/100)]!=4 and self.array[int(x/100)][int(y/100)]!=1):
                diamond = pygame.image.load('img/diamond.png')
                pic_diamond = pygame.transform.scale(diamond, (50, 50))
                self.screen.blit(pic_diamond, (x,y))
                #On ajoute cette case dans le tableau pour ne pas mettre plusieurs choses dedans
                self.array[int(x/100)][int(y/100)] = 2
            else:
                print("Deja de la poussiere")

    def add_vaccum(self):
        posX = random.randint(0, 4)
        posY = random.randint(0, 4)
        print("X : " + str(posX))
        print("Y : " + str(posY))
        vaccum= pygame.image.load('img/vaccum.png')
        pic_vaccum = pygame.transform.scale(vaccum, (50, 50))
        self.screen.blit(pic_vaccum, ((posX*100)+40,(posY*100)+40))
        self.array[int(posX)][int(posY)] = 3


if __name__ == "__main__":
    grid = Grid()
    grid.createGrid()
    grid.run()
    print(pygame.time.Clock())