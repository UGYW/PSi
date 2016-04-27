"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
Special Thanks: Michael Gelbart, Noah Bayless
"""

import flux
import genesis
import patient
import plot
import status

import copy
import random
import numpy
import sys


def main():
	Parameters = []
	Parameters.append(float(sys.argv[1])) #I - Percentage Probable (PP) Infectivity
	Parameters.append(int(sys.argv[2])) #InfP - Mean (M) Infectious Period
	Parameters.append(float(sys.argv[3])) #Mob - PP Mobility
	Parameters.append(int(sys.argv[4])) #IncP - M Incubation Period
	Parameters.append(float(sys.argv[5])) #Mor - PP Mortality
	Parameters.append(float(sys.argv[6])) #Imn - PP Immunity
	Parameters.append(int(sys.argv[7])) #RecP - M Recovery Period
	PImmune = 0.0 #Pre-Immune can also be viewed as Population Density

	xDimension = int(sys.argv[8])
	yDimension = int(sys.argv[9])

	tElapsed = int(sys.argv[10])

	move_range = float(sys.argv[11]) #PP of switching places

	PLOT = sys.argv[12]

	I = Parameters[0] #Percentage
	InfP = range(int(Parameters[1])-3, int(Parameters[1])+4) 
	Mob = Parameters[2] #Percentage
	IncP = range(int(Parameters[3])-3, int(Parameters[3])+4) 
	Mor = Parameters[4] #Percentage
	Imn = Parameters[5] #Percentage
	RecP = range(int(Parameters[6])-3, int(Parameters[6])+4)

	Population = xDimension*yDimension

	Dossier, Record, Pos2Pat, ID = genesis.genesis(Parameters, xDimension, yDimension)
	Trends = genesis.initial()

	for t in range(tElapsed):
		if len(sys.argv) >= 13:
			plot.matrix(Dossier, Population, t)

		for P in range(1, ID+1):
			status.StatusUpdate(Dossier, Record, Pos2Pat, xDimension, yDimension, P, Mob, I, Imn, Mor)
			flux.flux(xDimension, yDimension, Pos2Pat, Dossier, move_range)
			plot.update(Dossier, Trends, ID, t)
		print Pos2Pat

		Record = copy.deepcopy(Dossier)

	if len(sys.argv) >= 13:
		plot.plotTrend(Trends)
		plot.Print(Dossier, ID, Population)

main()