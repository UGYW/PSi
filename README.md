PSi (Pandemic Simulator I)

Developed By: Uma GuanYue Wu

Research and Calibrated By: LiQing Wang

Special Thanks: Michael Gelbart, Noah Bayless


CURRENT STATUS: Completed (Probably)

I (Uma) am the only person that have debugged this version of the program.
There are probably bugs I've overlooked but it looks like it works so far.



INSTRUCTIONS

The progression of the disease will be controlled by the following command line arguments (in order):

[1]: (TYPE: FLOAT [0,1]) Infectivity (Percentage probability (PP) of an individual displaying symptoms upon contracting the disease.)

[2]: (TYPE: INTEGER [4:]) Mean Infectious Period (The number of days someone will exhibit symptoms)

[3]: (TYPE: FLOAT [0,1]) Mobility (PP of the disease passing from an Infectious individual to a Susceptible one)

[4]: (TYPE: INTEGER [4:]) Mean Incubation Period (The number of days someone will carry the disease WITHOUT exhibiting symptoms)

[5]: (TYPE: FLOAT [0,1]) Mortality (PP of dying from the disease upon termination of Infectious Period)

[6]: (TYPE: FLOAT [0,1]) Immunity (PP of recovering from the disease with immunity upon termination of Recovery Period)

[7]: (TYPE: INTEGER [4:]) Mean Recovery Period (The number of days it takes to recover from the disease)

[8]: (TYPE: INTEGER [3:100]) xDimension of the matrix

[9]: (TYPE: INTEGER [3:100]) yDimension of the matrix

[10]: (TYPE: INTEGER [7:500]) tElapsed (in Days)

[11]: (TYPE: FLOAT [0,1]) The PP of live individuals switching places with each other

[12]: OPTIONAL! (TYPE: you can type anything here) if there is a 12th argument, the program will produce a plot for every day of the pandemic. You can set the frequency of this within main.py with a modulo statement.



FEATURES

Current Features

Parameters Affecting Patients

Infectivity

Mobility

Mortality

Immunity

Recovery Period

Infectious Period

Incubation Period

Flux

*Parameters Remain Constant with Time


Features to be Implemented

Population Density

Quarantine

Country Borders (?)

Cure Development

Resistance to Cure



BUGS

Please report all bugs to uma.w@alumni.ubc.ca

(If you have me on Facebook, please message me there - I check that much more often.)

NOTES

Please install python! This should be compatible with both OS and Windows systems.

Unless you are running this on a really darn good computer, please keep the product of xDimension and yDimension below 10000

Same idea with tElapsed. Keep it within the recommended range unless you've snuck into DWave somehow.

If you would like to save the results of the graph, please edit the functions within plot.py. You can also set the frequency of plotting within main.py.

[Link to the Paper: https://open.library.ubc.ca/cIRcle/collections/undergraduateresearch/51869/items/1.0319001]
