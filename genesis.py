"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
Special Thanks: Michael Gelbart, Noah Bayless
"""

import copy
import numpy as np

import patient

def genesis(Parameters, xDimension, yDimension):
    PImmune = 0.0 #Pre-Immune can also be viewed as Population Density
    InfP = range(int(Parameters[1])-3, int(Parameters[1])+4) 
    IncP = range(int(Parameters[3])-3, int(Parameters[3])+4) 
    RecP = range(int(Parameters[6])-3, int(Parameters[6])+4)
    
    #PATIENTS
    Dossier = dict()
    ID = 0
    Pos2Pat = np.zeros((yDimension, xDimension))
    for x in range(xDimension):
        for y in range(yDimension):
            ID += 1
            Dossier[ID] = patient.Patient(x, y, PImmune, IncP, InfP, RecP)
            Pos2Pat[y,x] = ID

    #GENERATING PATIENT ZERO
    x = xDimension/2
    y = yDimension/2
    Dossier[Pos2Pat[y,x]].Status = "INFECTIOUS" 

    Record = copy.deepcopy(Dossier)

    return Dossier, Record, Pos2Pat, ID

def initial():
    Trends = {}
    Trends["SUSCEPTIBLEtrend"] = []
    Trends["INCUBATINGtrend"] = []
    Trends["INFECTIOUStrend"] = []
    Trends["IMMUNEtrend"] = []
    Trends["DEADtrend"] = [] 

    return Trends