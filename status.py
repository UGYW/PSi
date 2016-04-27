"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
Special Thanks: Michael Gelbart, Noah Bayless
"""

import random

def Spread(Mob, NBR):
	if NBR.Status == "INFECTIOUS":
		contagion = random.random()
		if contagion <= Mob: #If the "roll" is lower than mobility, then the IDatient is infected by the virus
			return True
		else: 
			return False
	return False

def StatusUpdate(Dossier, Record, Pos2Pat, xDimension, yDimension, P, Mob, I, Imn, Mor):
	n = 8
	x = Dossier[P].xLoc
	y = Dossier[P].yLoc
	if Record[P].Status == "SUSCEPTIBLE":
		while Dossier[P].Status != "INFECTIOUS" and Dossier[P].Status != "INCUBATING" and n > 0:
			if n == 8:
				infection = Spread(Mob, Record[Pos2Pat[y,(x+1)%xDimension]]) #Right
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 7:
				infection = Spread(Mob, Record[Pos2Pat[y,(x-1)%xDimension]]) #Left
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 6:
				infection = Spread(Mob, Record[Pos2Pat[(y+1)%yDimension,x]]) #Above
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"                
			elif n == 5:
				infection = Spread(Mob, Record[Pos2Pat[(y-1)%yDimension,x]]) #Below
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 4:
				infection = Spread(Mob, Record[Pos2Pat[(y+1)%yDimension,(x+1)%xDimension]]) #Upper Right
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 3:
				infection = Spread(Mob, Record[Pos2Pat[(y-1)%yDimension,(x-1)%xDimension]]) #Lower Left
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 2:
				infection = Spread(Mob, Record[Pos2Pat[(y+1)%yDimension,(x-1)%xDimension]]) #Upper Left
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			elif n == 1:
				infection = Spread(Mob, Record[Pos2Pat[(y-1)%yDimension,(x+1)%xDimension]]) #Lower Right
				if infection == True:
					infection = random.random()
					if infection <= I:
						Dossier[P].Status = "INFECTIOUS"
					else: Dossier[P].Status = "INCUBATING"
			n -= 1

	elif Record[P].Status == "INFECTIOUS":
		Dossier[P].Recovery(Imn)
		if Dossier[P].RecState == True: #If the Dossier is still infectious...
			Dossier[P].Infection(Mor)
			
	elif Record[P].Status == "INCUBATING":
		Dossier[P].Recovery(Imn)
		if Dossier[P].RecState == True: #If the Dossier is still incubating...
			Dossier[P].Incubation(I,Imn)
