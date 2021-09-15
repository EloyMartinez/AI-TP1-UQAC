#!/usr/bin/python3
import random
from aspi import Aspi

#Fonction pour donner place
def randomPlace():
    return random.randint(0, 4)


def initialize():
    rows, cols = (5, 5) 
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    return arr


def displayGrid(arr, aspi):
    print("---------------------")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            add_robot(i,j,aspi,arr)
            if(j==len(arr[i])-1):
                print "| "+str(arr[i][j])+" |"
            else:
                print "| "+str(arr[i][j])+"",
        print("---------------------")

def add_dust(arr):
     for i in range(len(arr)):
        for j in range(len(arr[i])):
            num = random.uniform(0, 1) 
            if(num>0.7):
                arr[i][j] = 1

def add_robot(i,j,aspi,arr):
    if(i == aspi.get_y() and j == aspi.get_x()):
        arr[i][j]="A"
    


if __name__ == "__main__":
    aspi = Aspi(randomPlace(), randomPlace(), 1000)
    arr = initialize()
    add_dust(arr)
    displayGrid(arr, aspi)
    aspi.move_left()
    aspi.move_left()
    displayGrid(arr, aspi)
    aspi.move_up()
    aspi.move_up()
    displayGrid(arr, aspi)
    aspi.move_right()
    aspi.move_right()
    displayGrid(arr, aspi)
    aspi.move_down()
    aspi.move_down() 
