import sys
import numpy as np

#user input
run = int(sys.argv[1])

N=-1
Q=-1

if run==16978:
    N = 1156   #ep elastic counts
    Q = 5.485  # charge [mC]
elif run==16979:
    N = 12780
    Q = 76.223
elif run==17093:
    N = 1756
    Q = 49.725
elif run==17094:
    N = 377.8
    Q = 12.675
elif run==17096:
    N = 2914
    Q = 98.943
else:
    print('Please enter valid Ca48 MF run')
    sys.exit()
    
Q = Q / 1000.  # convert charge from mC to C
e=1.602e-19    # elementary charge C
dsig_dom = 2.409e-32   # ep cross section [cm^2/sr] @ incident e- energy: 10.549 GeV, SHMS: 8.3 deg, 9.438 GeV
omega=0.000378         # SHMS e- solid angle
Hmol = 1.00794         # H molar mass g/mol
Cmol =  12.011         # C molar mass g/mol
Na = 6.0221408e23      # Avogadro's number
Ca48_thick = 1.051   # g/cm2

# atoms / cm^2
nx = N / ((Q/e)*dsig_dom*omega)   # areal density of target (quantiy we are trying to extract)

# H- thick [g/cm^2]
H_thick = N / ((Q/e)*dsig_dom*omega) * Hmol / Na

# C- thick [g/cm^2]
C_thick = N / ((Q/e)*dsig_dom*omega) * (88/164.) * Cmol / Na

# relative fraction of H thickness to Ca48 thickness
H_thick_rel = H_thick / Ca48_thick  * 100.

# relative fraction of C-thickness to Ca48 thickness
C_thick_rel = C_thick / Ca48_thick * 100.

print('Ca48 Run {}'.format(run))
print('nx [atoms/cm^2]= {0:.3E}'.format(nx))
print('H_thick [g/cm^2]= {0:.3E}'.format(H_thick))
print('C_thick [g/cm^2]= {0:.3E}'.format(C_thick))
print('H_thick/Ca48_thick [%] ={0:.5f}'.format(H_thick_rel))
print('C_thick/Ca48_thick [%] ={0:.5f}'.format(C_thick_rel))
