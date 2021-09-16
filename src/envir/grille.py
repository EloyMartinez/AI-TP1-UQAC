#!/usr/bin/python3
import random
class Grille:

    #Fonction pour donner une place random
    def randomPlace(self):
        return random.randint(0, 4)
    
    #Fonction pour initialiser le tableau
    def initialize(self):
        rows, cols = (5, 5) 
        arr = [[0 for i in range(cols)] for j in range(rows)] 
        return arr

    #Fonction qui affiche la grille (Pour l'instant)
    def displayGrid(self,arr, aspi):
        print("---------------------")
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                self.add_robot(i,j,aspi,arr)
                if(j==len(arr[i])-1):
                    print("| "+str(arr[i][j])+" |")
                else:
                    print("| "+str(arr[i][j])+""),
            print("---------------------")

    #Fonction qui ajoute de la poussiere random
    def add_dust(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                num = random.uniform(0, 1) 
                if(num>0.7):
                    arr[i][j] = 1

    #Fonction qui ajoute le robot
    def add_robot(self,i,j,aspi,arr):
        if(i == aspi.get_y() and j == aspi.get_x()):
            arr[i][j]="A"
    


