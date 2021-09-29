import sys
sys.path.append('../')
from envir.case import Case


class Effecteurs:

    def grab_jewel(self, Case):
        print("ON MET JEWEL A FALSE\n")
        Case.set_jewel(False)
    
    def clean_case(self, Case):
        print("ON MET JEWEL ET DIRT A FALSE\n\n")
        Case.set_dirt(False)
        Case.set_jewel(False)

    def move(self, aspi, direction):
        posX = aspi.get_x()
        posY = aspi.get_y()
        if direction == "up":
            if(posY>0):
                aspi.set_y(posY-1)

        elif direction == "down":
            if(posY<4):
                aspi.set_y(posY+1)

        elif direction == "left":
            if(posX>0):
                aspi.set_x(posX-1)
                
        elif direction == "right":
            if(posX<4):
                aspi.set_x(posX+1)




    
