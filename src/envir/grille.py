#!/usr/bin/python3
import random
from envir.case import Case


class Grille:
    
    def __init__(self):
        self.rows = 5
        self.cols = 5
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

    
    #Fonction pour initialiser le tableau
    def initialize(self):
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                self.arr[i][j] = Case(i,j,False,False)
    
    #Fonction pour generer les bijoux et salete
    def generateEnvr(self):
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                (self.arr[i][j]).generate_bijoux()
                (self.arr[i][j]).generate_salete()


    #Fonction qui ajoute le robot
    def add_robot(self,i,j,aspi,arr):
        if(i == aspi.get_y() and j == aspi.get_x()):
            arr[i][j]="A"
            
    #Fontion d'execution
    def execute(self):
        self.generateEnvr()
    


