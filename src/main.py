import threading
from envir.grid import Grid
from envir.case import Case
from agent.aspi import Aspi
from agent.noeud import Noeud
from agent.sensor import sensor
from agent.effecteurs import Effecteurs
import time
import random
import threading as thrd
from threading import Thread


## GESTION DES THREADS

mutex = thrd.Lock()

def gestion_grille(grille):
    while True:
        grille.generate_environment()
        grille.main()
        time.sleep(10)

def gestion_aspi(aspi, grille):
    mutex.acquire()
    try:
        aspi.useSensor(grille)
    finally:
        mutex.release()
    aspi.setIntent()
    aspi.get_bdi().get_intent()
    aspi.update_pos(grille)

    time.sleep(3)
    




### MAIN

if __name__ == "__main__":

    grille = Grid()
    aspi = Aspi(random.randint(0,4), random.randint(0,4), 1000)
    print("Les coordonnées de l'aspi : ")
    print("en x : " + str(aspi.get_x()))
    print("en y : " + str(aspi.get_y()))


    #aspi = Aspi(grille.randomPlace(), grille.randomPlace(), 1000)
   
    #a = grille.clone()
    grille.initialize()

   # grille.display()
   # a.display()


    #noeud = Noeud(None, 0, 0, "",0,grille.get_arr()[aspi.get_x()][aspi.get_y()])


   # print(noeud.actionCase("down",grille).get_jewel())


    grille.add_vaccum(aspi.get_x(), aspi.get_y())

    sensor = sensor(True)

    
    ### THREAD NE MARCHE PAS
  
    
    #t1 = thrd.Thread(target = gestion_grille, args=(grille,))
    #t1.setDaemon(True)
    t2 = thrd.Thread(target = gestion_aspi, args=(aspi,grille,))
    #t1.start()
    while True:
        t2.start()
    

    while True:
        grille.generate_environment()
        grille.main()
        time.sleep(10)





#   aspi.get_effecteurs().move(aspi,"up")
#    print(aspi.get_x())
#    print(aspi.get_y())

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


'''
 boole = False

    while True:
        grille.generate_environment()
        grille.main()
        aspi.useSensor(grille)
        aspi.setIntent()
        aspi.update_pos(grille)

        if(boole==False):

            ### CLONE GRILLE 
            # array_clone = sensor.capture(grille)
            # print(array_clone[aspi.get_x()][aspi.get_y()].get_jewel())
            # print(array_clone[aspi.get_x()][aspi.get_y()].get_dirt())
            # print(grille.get_arr()[aspi.get_x()][aspi.get_y()].get_jewel())
            # print(grille.get_arr()[aspi.get_x()][aspi.get_y()].get_dirt())

            ### CLONE DE LA CASE
        #     print(grille.get_arr()[aspi.get_x()][aspi.get_y()-1].get_dirt())
        #     print(grille.get_arr()[aspi.get_x()][aspi.get_y()-1].get_jewel())

        #     print(noeud.actionCase("down",grille).get_jewel())
            
        #     boole = True
            boole = True

        time.sleep(20)
'''
   

   




