from envir.grid import Grid
from envir.case import Case
from agent.aspi import Aspi
from agent.effecteurs import Effecteurs
import pygame
import time
import random

if __name__ == "__main__":
    '''
    yo = Aspi(2,3,1000)
    print("Start")
    print("X : " + str(yo.get_x()) + "      Y : " +str(yo.get_y()))
    print("UP (y+1)")
    yo.get_effecteurs().move(yo,"up")
    print("X : " + str(yo.get_x()) + "      Y : " +str(yo.get_y()))
    yo.get_effecteurs().move(yo,"left")
    print("left (x-1)")
    print("X : " + str(yo.get_x()) + "      Y : " +str(yo.get_y()))
    yo.get_effecteurs().move(yo,"down")
    print("down (y-1)")
    print("X : " + str(yo.get_x()) + "      Y : " +str(yo.get_y()))

    yo.get_effecteurs().move(yo,"right")
    print("right (x+1)")
    print("X : " + str(yo.get_x()) + "      Y : " +str(yo.get_y()))

    yo.get_effecteurs().grab_jewel
    '''
   
    grille = Grid()
    aspi = Aspi(random.randint(0,4), random.randint(0,4), 1000)
    print(aspi.get_x())
    print(aspi.get_y())

#     aspi = Aspi(grille.randomPlace(), grille.randomPlace(), 1000)
    grille.initialize()
    grille.add_vaccum(aspi.get_x(), aspi.get_y())
    aspi.get_effecteurs().move(aspi,"up")
    print(aspi.get_x())
    print(aspi.get_y())
    grille.clone()
#     grille.add_dust(arr)
#     #grille.displayGrid(arr, aspi)
#     aspi.move_left()
#     aspi.move_left()
#    # grille.displayGrid(arr, aspi)
#     aspi.move_up()
#     aspi.move_up()
#    # grille.displayGrid(arr, aspi)
#     aspi.move_right()
#     aspi.move_right()
#     #grille.displayGrid(arr, aspi)
#     aspi.move_down()
#     aspi.move_down()
#     case = Case(grille.randomPlace(), grille.randomPlace(),False,False)
#     case.generate_bijoux()
#     case.generate_salete()
while True:
    grille.generate_environment()
    grille.main()
    time.sleep(5)
