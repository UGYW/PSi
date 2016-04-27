"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
SIDecial Thanks: Michael Gelbart, Noah Bayless
"""

import random

def flux(xDimension, yDimension, Pos2Pat, Dossier, move_range):
    for x in range(xDimension):
        for y in range(yDimension):
            if Dossier[Pos2Pat[y,x]].Status != "DEAD":
                move = random.random()
                if move <= move_range:
                    swap = random.randint(1, 4)
                    if swap == 1: #switch with above
                        oriID = Pos2Pat[y, x]
                        newID = Pos2Pat[(y+1)%yDimension, x]
                        Dossier[oriID].yLoc = (y+1)%yDimension
                        Dossier[newID].yLoc = y
                        Pos2Pat[y,x] = newID
                        Pos2Pat[(y+1)%yDimension, x] = oriID                            
                        
                    elif swap == 2: #switch with below
                        oriID = Pos2Pat[y, x]
                        newID = Pos2Pat[(y-1)%yDimension, x]
                        Dossier[oriID].yLoc = (y-1)%yDimension
                        Dossier[newID].yLoc = y
                        Pos2Pat[y,x] = newID
                        Pos2Pat[(y-1)%yDimension, x] = oriID
                    
                    elif swap == 3: #switch with left
                        oriID = Pos2Pat[y, x]
                        newID = Pos2Pat[y, (x-1)%yDimension]
                        Dossier[oriID].xLoc = (x-1)%xDimension
                        Dossier[newID].xLoc = x
                        Pos2Pat[y,x] = newID
                        Pos2Pat[y, (x-1)%yDimension] = oriID
                        
                    elif swap == 4: #switch with right
                        oriID = Pos2Pat[y, x]
                        newID = Pos2Pat[y, (x+1)%yDimension]
                        Dossier[oriID].xLoc = (x+1)%xDimension
                        Dossier[newID].xLoc = x
                        Pos2Pat[y,x] = newID
                        Pos2Pat[y, (x+1)%yDimension] = oriID 