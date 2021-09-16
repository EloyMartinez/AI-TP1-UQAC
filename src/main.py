from agent.aspi import Aspi
from envir.grille import Grille
from envir.case import Case
import time

if __name__ == "__main__":
   grille = Grille()
#     grille.
#     aspi = Aspi(grille.randomPlace(), grille.randomPlace(), 1000)
grille.initialize()
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
    grille.generateEnvr()
    time.sleep(0.5)
        
        
    
    
     
