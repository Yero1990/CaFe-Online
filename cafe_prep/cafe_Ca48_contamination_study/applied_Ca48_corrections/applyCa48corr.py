import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame as pdf

# define exponential function (based on our fit to T2 scalers vs Charge)
def rel_Cntm_src(Q):
    
    # used to parametrize relative drop
    # in overall contamination (units in percent)
    # for now we assume contamination from C_n+H_2n
    A = 3.090*1e-2
    alpha = 6.422*1e-4
    C = 9.728*1e-01

    return (A*np.exp(-alpha*Q) + C)*100 #percent
    

# H,C absolute contamination (used as initial parameter)
# obtained from CaFe Ca48 MF run analysis (in percent)
# assumes pure mineral oil ( mostly consisting of (C_n+H_2n) )
# absolute (H,C)-contam = (H,C)-thickness / Ca48-thickness
def absCntm(run, element=''):
    # in percent
    if(run==16978): 
        if(element=='H'):
            return 0.65 
        elif(element=='C'):
            return 3.8 
    if(run==16979):
        if(element=='H'):
            return 0.51 
        elif(element=='C'):
            return 3.1
    if(run==17093):
        if(element=='H'):
            return 0.11 
        elif(element=='C'):
            return 0.65
    if(run==17094):
        if(element=='H'):
            return 0.091 
        elif(element=='C'):
            return 0.54
    if(run==17096):
        if(element=='H'):
            return 0.09 
        elif(element=='C'):
            return 0.53
    else:
        return np.nan

df = pd.read_csv("ca48_bcmInfo.csv")
run = df['run']
kin = df['kin']
Qbcm1 =  df['q_bcm1_new']
Qprev = 0  # previous charge (for cumulative sum)


myfile = open('ca48_correction.csv', 'w')
myfile.write('idx, kin, run, Q, Qsum, H_absCntm_MF, C_absCntm_MF, C_absCntm_SRC\n')

# loop over each Ca48 run and index it
for idx, irun in enumerate(run):

    #get cumulative charge
    Qsum = Qbcm1[idx] + Qprev

    # total charge up to run 16979 (basically just add the charge of the first 2 MF Ca48 runs)
    Qsum_16979 = Qbcm1[0] +  Qbcm1[1]

    #get absolute contamination from Ca48 MF
    H_absCntm_MF = absCntm(irun, 'H')
    C_absCntm_MF = absCntm(irun, 'C')
    
    # since H-contamination initially is ~0.6 % and last Ca48 MF run ~0.09% (it is negligible in the relative drop)
    #estimate C absolute contamination from Ca48 SRC using parametrized T2scalers / mC expn. fit
    
    C_absCntm_SRC = absCntm(16979, 'C') - ( rel_Cntm_src(Qsum_16979) - rel_Cntm_src(Qsum) )
    if(kin[idx].strip()=="MF"):
        C_absCntm_SRC = np.nan

    #print("%i, %s, %i, %.3f, %.3f, %.3f, %.3f, %.3f\n" % (idx, kin[idx], irun, Qbcm1[idx], Qsum, H_absCntm_MF, C_absCntm_MF, C_absCntm_SRC))
    line="%i, %s, %i, %.3f, %.3f, %.3f, %.3f, %.3f\n" % (idx, kin[idx], irun, Qbcm1[idx], Qsum, H_absCntm_MF, C_absCntm_MF, C_absCntm_SRC)
    myfile.write(line)

    Qprev = Qsum
