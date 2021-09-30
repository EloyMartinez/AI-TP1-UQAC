from envir.grid import Grid
from envir.case import Case
from agent.aspi import Aspi
from agent.noeud import Noeud
from agent.sensor import sensor
from agent.effecteurs import Effecteurs
import time
import random
import threading as thrd


## GESTION DES THREADS

mutex = thrd.Lock()

'''
def gestion_grille(grille):
    grille.generate_environment()
    while True:
        grille.main()
        time.sleep(10)
'''

def gestion_aspi(aspi, grille, lock):
    count = 0
    intMesure = 1
    while True:
        #print(grille.get_arr()[aspi.get_x()][aspi.get_y()].get_jewel())
        mutex.acquire()
        try:
            aspi.useSensor(grille,count,intMesure)
            count = count + 1
        finally:
            mutex.release()
        #aspi.setIntentBFS()
        #aspi.setIntentDFS()
        aspi.setIntent()
        print("NTMMMMMMMMM : "+  str(aspi.get_bdi().get_intent()))
        aspi.get_bdi().get_intent()
        aspi.update_pos(aspi.get_bdi().get_belief(), grille, lock)
        time.sleep(1)

        


### MAIN

if __name__ == "__main__":

    grille = Grid()
  #  aspi = Aspi(4, 4, 1000)

    aspi = Aspi(random.randint(0,4), random.randint(0,4))
    grille.initialize()
    grille.add_vaccum(aspi.get_x(), aspi.get_y())
    grille.generate_environment()

    #print("Tour 1 case 0,0 : " + str(grille.get_arr()[0][0].get_dirt()))
    #print("Tour 1 case 0,1 : " + str(grille.get_arr()[0][1].get_dirt()))



    ### THREAD NE MARCHE PAS
    #t1 = thrd.Thread(target = gestion_grille, args=(grille,))
    #t1.setDaemon(True)
    t2 = thrd.Thread(target = gestion_aspi, args=(aspi,grille, mutex,))
    #t1.start()
    t2.start()

    # print("BELIEF :")
    # for x in range(0, 5):
    #     for y in range(0, 5):
    #        # print(aspi.get_bdi().get_belief()[x][y].get_coords())
    #         print("DIRT :" + str(aspi.get_bdi().get_belief()[x][y].get_dirt()))
    #         print("JEWEL :" + str(aspi.get_bdi().get_belief()[x][y].get_jewel()))

    mutex.acquire()
    try:
        grille.main()
    finally:
            mutex.release()
    while True:
        mutex.acquire()
        try:
            grille.generate_environment()
        finally:
            mutex.release()
        time.sleep(5)
        print("\nPERFORMANCE : " +str(aspi.get_sensor().get_performance()) + "\n")
    # print("Tour 2 case 0,0 : " + str(grille.get_arr()[0][0].get_dirt()))
    # print("Tour 2 case 0,1 : " + str(grille.get_arr()[0][1].get_dirt()))

    # print("BELIEF :")
    # for x in range(0, 5):
    #     for y in range(0, 5):
    #         print(str(x) + " : " +str(y) )
    #         print("DIRT BELIEF:" + str(aspi.get_bdi().get_belief()[x][y].get_dirt()) + "   JEWEL BELIEF:" + str(aspi.get_bdi().get_belief()[x][y].get_jewel()))
    #         print("DIRT REEL:" + str(grille.get_arr()[x][y].get_dirt()) + "   JEWEL REEL:" + str(grille.get_arr()[x][y].get_jewel()))


    #time.sleep(30)
    # print("BELIEF :")
    # for x in range(0, 5):
    #     for y in range(0, 5):
    #         print(str(x) + " : " +str(y) )
    #         print("DIRT BELIEF:" + str(aspi.get_bdi().get_belief()[x][y].get_dirt()) + "   JEWEL BELIEF:" + str(aspi.get_bdi().get_belief()[x][y].get_jewel()))
    #         print("DIRT REEL:" + str(grille.get_arr()[x][y].get_dirt()) + "   JEWEL REEL:" + str(grille.get_arr()[x][y].get_jewel()))




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


   




