import sys
sys.path.append('/Users/vincedollo/Desktop/UQAC/T1/AI/AI-TP1-UQAC/src/envir')
from case import Case


class Effecteurs:

    def grab_jewel(self, Case):
        Case.set_jewel(False)
    
    def clean_case(self, Case):
        Case.set_dirt(False)
        Case.set_jewel(False)

    def move(self, aspi, direction):
        posX = aspi.get_x()
        posY = aspi.get_y()
        hasMoved = False
        if direction == "up":
            if(posY>0):
                aspi.set_y(posY+1)
        elif direction == "down":
            if(posY>3):
                aspi.set_y(posY-1)
        elif direction == "left":
            if(posX>0):
                aspi.set_x(posX-1)
        elif direction == "right":
            if(posX<3):
                aspi.set_x(posX+1)




    
