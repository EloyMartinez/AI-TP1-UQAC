from agent.aspi import Aspi
from envir.grille import Grille
from envir.case import Case


if __name__ == "__main__":
    grille = Grille()
    aspi = Aspi(grille.randomPlace(), grille.randomPlace(), 1000)
    arr = grille.initialize()
    grille.add_dust(arr)
    grille.displayGrid(arr, aspi)
    aspi.move_left()
    aspi.move_left()
    grille.displayGrid(arr, aspi)
    aspi.move_up()
    aspi.move_up()
    grille.displayGrid(arr, aspi)
    aspi.move_right()
    aspi.move_right()
    grille.displayGrid(arr, aspi)
    aspi.move_down()
    aspi.move_down()
    case = Case(grille.randomPlace(), grille.randomPlace(),False,False)
    case.generate_bijoux()
    case.generate_salete()
    
     
