"""
PSi

Developed By: Uma GuanYue Wu
Research and Calibrated By: LiQing Wang
Special Thanks: Michael Gelbart, Noah Bayless
"""

import matplotlib.pyplot as plt

def update(Dossier, Trends, ID, t):
    SUSCEPTIBLE = 0
    INFECTIOUS = 0
    INCUBATING = 0
    IMMUNE = 0
    DEAD = 0

    for P in range(1, ID+1):
        if Dossier[P].Status == "SUSCEPTIBLE":
            SUSCEPTIBLE += 1
        elif Dossier[P].Status == "INFECTIOUS":
            INFECTIOUS += 1
        elif Dossier[P].Status == "INCUBATING":
            INCUBATING += 1
        elif Dossier[P].Status == "IMMUNE":
            IMMUNE += 1
        elif Dossier[P].Status == "DEAD":
            DEAD += 1

    Trends["SUSCEPTIBLEtrend"].append(SUSCEPTIBLE)
    Trends["INCUBATINGtrend"].append(INCUBATING)
    Trends["INFECTIOUStrend"].append(INFECTIOUS)
    Trends["IMMUNEtrend"].append(IMMUNE)
    Trends["DEADtrend"].append(DEAD)

def matrix(Dossier, Population, t):
    for P in range(1, Population+1):
        x = Dossier[P].xLoc
        y = Dossier[P].yLoc

        if Dossier[P].Status == 'SUSCEPTIBLE':
            colour = "white"
        elif Dossier[P].Status == 'IMMUNE':
            colour = "blue"
        elif Dossier[P].Status == 'INFECTIOUS':     
            colour = "red"
        elif Dossier[P].Status == 'INCUBATING':     
            colour = "yellow"
        elif Dossier[P].Status == 'DEAD':
            colour = "black"
            
        if colour == "white":    
            plt.plot(x, y, "wo")
        elif colour == "blue":
            plt.plot(x, y, "bo")
        elif colour == "red":
            plt.plot(x, y, "ro")
        elif colour == "yellow":
            plt.plot(x, y, "yo")
        elif colour == "black":
            plt.plot(x, y, "ko")
    plt.show() #Use this if making any changes to the code or just testing.
    # plt.savefig("PandemicDay%i.pdf" %t)

def plotTrend(Trends):
    plt.plot(Trends["SUSCEPTIBLEtrend"], "g", label = "SUSCEPTIBLE")
    plt.plot(Trends["INCUBATINGtrend"], "y", label = "INCUBATING")
    plt.plot(Trends["INFECTIOUStrend"], "r", label = "INFECTIOUS")
    plt.plot(Trends["IMMUNEtrend"], "b", label = "IMMUNE")
    plt.plot(Trends["DEADtrend"], "k", label = "DEAD")

    plt.legend(loc="best")
    plt.title("===========")
    plt.ylabel("Number of Individuals")
    plt.xlabel("Time (in days)")
    plt.show()
    # plt.savefig("SimulatedPandemic.pdf")

def Print(Dossier, ID, Population):
    SUSCEPTIBLE = 0
    INFECTIOUS = 0
    INCUBATING = 0
    IMMUNE = 0
    DEAD = 0

    for P in range(1, ID+1):
        if Dossier[P].Status == "SUSCEPTIBLE":
            SUSCEPTIBLE += 1
        elif Dossier[P].Status == "INFECTIOUS":
            INFECTIOUS += 1
        elif Dossier[P].Status == "INCUBATING":
            INCUBATING += 1
        elif Dossier[P].Status == "IMMUNE":
            IMMUNE += 1
        elif Dossier[P].Status == "DEAD":
            DEAD += 1

    print "SUSCEPTIBLE = %i" %SUSCEPTIBLE
    print "INFECTIOUS = %i" %INFECTIOUS
    print "INCUBATING = %i" %INCUBATING
    print "IMMUNE = %i" %IMMUNE
    print "DEAD = %i" %DEAD
    print "Percent Dead = %f" %(float(DEAD)/float(Population))
