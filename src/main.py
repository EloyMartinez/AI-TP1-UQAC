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

# Fonction qui va gerer l'aspirateur (Appelé dans un thread)
def gestion_aspi(aspi, grille):
    count = 0
    intMesure = 1
    while True:
        mutex.acquire()
        try:
            #L'aspi va utiliser ses sensor pour clone la grille: il fait cela tous les count modulo intMesure
            aspi.useSensor(grille,count,intMesure)
            count = count + 1
        finally:
            mutex.release()
        
        #L'aspi va mettre a jour sa liste d'action a réaliser
        aspi.setIntentDFS()
        #aspi.get_bdi().get_intent()
        
        #Puis va mettre a jour la position de l'aspi et regler la grille
        aspi.update_pos(aspi.get_bdi().get_belief(), grille)
        time.sleep(1)

        


### MAIN

if __name__ == "__main__":

    grille = Grid()
    aspi = Aspi(random.randint(0,4), random.randint(0,4))
    grille.initialize()
    grille.add_vaccum(aspi.get_x(), aspi.get_y())
    grille.generate_environment()

    ### THREAD NE MARCHE PAS
    #t1 = thrd.Thread(target = gestion_grille, args=(grille,))
    #t1.setDaemon(True)
    #t1.start()

    t2 = thrd.Thread(target = gestion_aspi, args=(aspi,grille,))
    t2.start()


    grille.main()

    #Boucle d'environement
    cmt = 1
    while True:
        grille.generate_environment()
        time.sleep(5)
        print("\nPERFORMANCE " + str(cmt) + " : "+str(aspi.get_sensor().get_performance()) + "\n")
        cmt = cmt+1
   



   




