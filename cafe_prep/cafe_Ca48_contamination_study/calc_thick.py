
#user

# run 16978
#N = 1156
#Q = 5.485

# run 16979
#N = 12780
#Q = 76.223

# run 17093
#N = 1756
#Q = 49.725

# run 17094
#N = 377.8
#Q = 12.675

# run 17096
N = 2914
Q = 98.943

Q = Q / 1000.
e=1.602e-19
dsig_dom = 2.409e-32
omega=0.000378
Hmol = 1.00794
Cmol =  12.011
Na = 6.0221408e23

# atoms / cm^2
nx = N / ((Q/e)*dsig_dom*omega)

# H- thick [g/cm^2]
H_thick = N / ((Q/e)*dsig_dom*omega) * Hmol / Na
# C- thick [g/cm^2]
C_thick = N / ((Q/e)*dsig_dom*omega) * (88/164.) * Cmol / Na

print('nx [atoms/cm^2]= ', nx)
print('H_thick [g/cm^2]= ', H_thick)
print('C_thick [g/cm^2]= ', C_thick)
