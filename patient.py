"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
Special Thanks: Michael Gelbart, Noah Bayless
"""

import random

class Patient(): #Creates an object (like list or array) that has its own modules
    def __init__(self, x, y, PImmune, IncP, InfP, RecP): #Automatically run as soon as object is created
        #x and y - int
        #PImmune - float
        #IncP, InfP and RecP - lists
        self.xLoc = x #Stores the inputted x location in the object
        self.yLoc = y #Same as above
        
        vaccination = random.random()        
        if vaccination <= PImmune: #If the "roll" is below the PImmune probability
            self.Status = "IMMUNE" #The Individual becomes immune
        else: self.Status = "SUSCEPTIBLE" #If not, the individual becomes susceptible
        
        self.IncLen = random.choice(IncP) #Picks a incubation rate out of the IncP list  
        self.InfLen = random.choice(InfP) #Same as above for infectious rate
        self.RecLen = random.choice(RecP) #Same as above for recovery rate
        self.IncState = False #Sets incubation state as false
        self.InfState = False #Same as above for infectious rate
        self.RecState = False #Same as above for recovery rate


    def Incubation(self, I, Imn):
        self.IncLen -= 1 #When the function is called, it first decreases the incubation period by 1
        if self.IncLen >= 0: #While the incubation period is more than 0, the IncState is set to True
            self.IncState = True
        else: self.IncState = False #Otherwise, the IncState is False. In other words, the patient stops incubating.
        
        if self.IncState == False: #Once the patient finishes incubating..
            luck = random.random()
            if luck <= I: #If their "roll" is less than Infectivity...
                self.Status = "INFECTIOUS" #They become Infectious
            else: 
                antibody = random.random() #If their "roll" is more than Infectivity...
                if antibody <= Imn: #If their "roll" is smaller than the Immunity
                    self.Status = "IMMUNE" #They become Immune.
                else: self.Status = "SUSCEPTIBLE" #Otherwise, they become susceptible.
        
        
    def Infection(self, Mor): #Same concepts as incubation.
        self.InfLen -= 1
        if self.InfLen >= 0:
            self.InfState = True
        else: self.InfState = False
        
        if self.InfState == False:
            hopesndreams = random.random()
            if hopesndreams <= Mor: 
                self.Status = "DEAD"
            else: self.Status = "INCUBATING"


    def Recovery(self, Imn): #Activated when patient goes into incubation or infection
        self.RecLen -= 1
        if self.RecLen >= 0:
            self.RecState = True
        else: self.RecState = False
        
        if self.RecState == False:
            antibody = random.random()
            if antibody <= Imn:
                self.Status = "IMMUNE"
            else: self.Status = "SUSCEPTIBLE"
    
    def Copy(self):
        new_pat = Dossier(self.xLoc, self.yLoc, 0, range(2,7), range(2,7), range(2,7)) 
        #^These input values doesn't matter cuz we're gonna update it anyway
        new_pat.Status = self.Status
        new_pat.IncLen = self.IncLen
        new_pat.InfLen = self.InfLen
        new_pat.RecLen = self.RecLen
        new_pat.IncState = self.IncState
        new_pat.InfState = self.InfState
        new_pat.RecState = self.RecState
        return new_pat