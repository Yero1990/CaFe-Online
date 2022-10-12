import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
import pandas as pd
from matplotlib import rc

rc('text', usetex=True)

#df_scaler = pd.read_csv("ca48_report_files/fall2021_bcm/ca48_bcmFall2021.csv")
df_scaler = pd.read_csv("ca48_scaler_report_files/ca48_bcmInfo.csv")

plt.rcParams["font.family"] = "Times New Roman"


run = df_scaler['run']
kin = df_scaler['kin']

# fall 2021 bcm calib
T2_scaler = df_scaler['T2_scaler']  # T2 (SHMS EL-REAL)
bcm1_charge = df_scaler['q_bcm1']   # charge [mC]
bcm2_charge = df_scaler['q_bcm2']
bcm4a_charge = df_scaler['q_bcm4a']
bcm4b_charge = df_scaler['q_bcm4b']
bcm4c_charge = df_scaler['q_bcm4c']
I_bcm4a_avg  = df_scaler['I_bcm4a_avg']

# summer 2022 bcm calib
T2_scaler_new = df_scaler['T2_scaler_new']  # T2 (SHMS EL-REAL)
bcm1_charge_new = df_scaler['q_bcm1_new']   # charge [mC]
bcm2_charge_new = df_scaler['q_bcm2_new']
bcm4a_charge_new = df_scaler['q_bcm4a_new']
bcm4b_charge_new = df_scaler['q_bcm4b_new']
bcm4c_charge_new = df_scaler['q_bcm4c_new']
I_bcm4a_avg_new  = df_scaler['I_avg_new']


# calculate T2 scaler counts per charge (fall 2021 bcm calib)
T2_per_mC_bcm1 = T2_scaler / bcm1_charge
T2_per_mC_bcm2 = T2_scaler / bcm2_charge
T2_per_mC_bcm4a = T2_scaler / bcm4a_charge
T2_per_mC_bcm4b = T2_scaler / bcm4b_charge
T2_per_mC_bcm4c = T2_scaler / bcm4c_charge

# calculate T2 scaler counts per charge (summer 2022 bcm calib)
T2_per_mC_bcm1_new = T2_scaler_new / bcm1_charge_new
T2_per_mC_bcm2_new = T2_scaler_new / bcm2_charge_new
T2_per_mC_bcm4a_new = T2_scaler_new / bcm4a_charge_new
T2_per_mC_bcm4b_new = T2_scaler_new / bcm4b_charge_new
T2_per_mC_bcm4c_new = T2_scaler_new / bcm4c_charge_new

# normalize T2 by 1st SRC run (fall 2021 bcm calib)
T2_per_mC_bcm4a_norm = T2_per_mC_bcm4a / T2_per_mC_bcm4a[2]

# normalize T2 by 1st SRC run (summer 2022 bcm calib)
T2_per_mC_bcm4a_norm_new = T2_per_mC_bcm4a_new / T2_per_mC_bcm4a_new[2]

'''
# fall 2021 bcm calibrations
fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')
ax1.plot(run[:2],   T2_per_mC_bcm4a_norm[:2], marker='o', color='blue', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF')
ax1.plot(run[2:23], T2_per_mC_bcm4a_norm[2:23], marker='o', color='red', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 SRC')
ax1.plot(run[23:],  T2_per_mC_bcm4a_norm[23:], marker='o', color='green', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF (round 2)')
ax1.set_ylim([0.9, 1.05])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left',fontsize=12)
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2],   I_bcm4a_avg[:2], marker='o', color='blue', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF')
ax2.plot(run[2:23], I_bcm4a_avg[2:23], marker='o', color='red', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 SRC')
ax2.plot(run[23:],  I_bcm4a_avg[23:], marker='o', color='green', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF (round 2)')
ax2.set_ylim([25, 65])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
plt.show()


# summer 2022 bcm calibrations
fig0, (ax1, ax2) = plt.subplots(2)

ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')
ax1.plot(run[:2],   T2_per_mC_bcm4a_norm_new[:2], marker='^', color='blue', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF (bcm_calib22)')
ax1.plot(run[2:23], T2_per_mC_bcm4a_norm_new[2:23], marker='^', color='red', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 SRC (bcm_calib22)')
ax1.plot(run[23:],  T2_per_mC_bcm4a_norm_new[23:], marker='^', color='green', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF (round 2, bcm_calib22)')
ax1.set_ylim([0.9, 1.05])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left',fontsize=12)
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2],   I_bcm4a_avg_new[:2], marker='^', color='blue', markerfacecolor='white',   markersize=8, linestyle='None', label='Ca48 MF (bcm_calib22)')
ax2.plot(run[2:23], I_bcm4a_avg_new[2:23], marker='^', color='red', markerfacecolor='white',  markersize=8, linestyle='None', label='Ca48 SRC (bcm_calib22)')
ax2.plot(run[23:],  I_bcm4a_avg_new[23:], marker='^', color='green', markerfacecolor='white', markersize=8, linestyle='None', label='Ca48 MF (round 2, bcm_calib22)')
ax2.set_ylim([25, 65])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
plt.show()
'''

'''
# bcm calib sanity check
fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Fall 2021 BCM Calibration Parameters', fontsize=16, fontweight='bold')
ax1.plot(run,  bcm1_charge, marker='^', color='blue', markerfacecolor='None', markersize=9, linestyle='None', label='BCM1')
ax1.plot(run,  bcm2_charge, marker='s', color='green', markerfacecolor='None', markersize=9, linestyle='None', label='BCM2')
ax1.plot(run,  bcm4a_charge, marker='o', color='red', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4A')
ax1.plot(run,  bcm4b_charge, marker='D', color='magenta', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4B')
ax1.plot(run,  bcm4c_charge, marker='+', color='violet', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4C')
ax1.set_ylim([-50, 230])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_ylabel('BCM Charge [mC]', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Summer 2022 BCM Calibration Parameters', fontsize=16, fontweight='bold')
ax2.plot(run,  bcm1_charge_new, marker='^', color='blue', markerfacecolor='None', markersize=9, linestyle='None', label='BCM1')
ax2.plot(run,  bcm2_charge_new, marker='s', color='green', markerfacecolor='None', markersize=9, linestyle='None', label='BCM2')
ax2.plot(run,  bcm4a_charge_new, marker='o', color='red', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4A')
ax2.plot(run,  bcm4b_charge_new, marker='D', color='magenta', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4B')
ax2.plot(run,  bcm4c_charge_new, marker='+', color='violet', markerfacecolor='None', markersize=9, linestyle='None', label='BCM4C')
ax2.set_ylim([0, 230])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('BCM Charge [mC]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
plt.show()
'''



#-----------------------------------
# Select Ca48 SRC runs with Ib>50 uA and do exponential fit
# (parametrize the percentage drop in T2 scalers versus charge)
#-----------------------------------
'''
run_src = list(run[2:8]) + list(run[12:23])
T2_scl_per_mC_src = list(T2_per_mC_bcm4a_norm_new[2:8]) + list(T2_per_mC_bcm4a_norm_new[12:23])
Q_src = list(bcm4a_charge_new[2:8]) +  list(bcm4a_charge_new[12:23])
Q_csum_src = np.cumsum(Q_src)

T2_scl_per_mC_src = np.array(T2_scl_per_mC_src)
Q_csum_src = np.array(Q_csum_src)
print('x=',Q_csum_src)
print('y=',T2_scl_per_mC_src)

# define exponential-fit function with parameters (a,b)
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# fit the data
popt, pcov = curve_fit(func, Q_csum_src,  T2_scl_per_mC_src, p0=[1, 1e-05, 200])

print('a = ', popt[0])
print('b = ', popt[1])
print('c = ', popt[2])

print(pcov)

# error in parameters is squareroot of diagonal elements of covariant matrix (diagonal elements -> variances (sig^2))
# off diagonal element represents correlations errors
p_sigma = np.sqrt(np.diag(pcov))

print(p_sigma)

# plot data 
fig0, (ax1) = plt.subplots(1)
ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')
ax1.plot(Q_csum_src, T2_scl_per_mC_src, marker='^', color='black', markerfacecolor='white', markersize=8, linestyle='None', label=r'Ca48 SRC data ($I_{b} > 50 \mu$A')
ax1.set_ylim([0.96, 1.02])
ax1.grid()
ax1.legend(loc='upper left',fontsize=12)
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.set_xlabel('Cumulative Charge Q [mC]', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)
# plot fit curve 
ax1.plot(Q_csum_src, func(Q_csum_src, *popt), 'r-', label=r"fit: $A e^{-\alpha Q}$ + C" "\n" "A = %.3E $\pm$ %.3E" "\n" r"$\alpha$ = %.3E $\pm$ %.3E" "\n" "C = %.3E $\pm$ %.3E" % (popt[0], p_sigma[0], popt[1], p_sigma[1], popt[2], p_sigma[2]) )
ax1.legend(loc='upper left',fontsize=15)

plt.show()
'''

#-----------------------------------
# Select Ca48 SRC runs with Ib<50 uA
# and parametrize the percentage drop
# in T2 scalers versus current)
#-----------------------------------

run_src = list(run[8:12])
T2_scl_per_mC_src = list(T2_per_mC_bcm4a_norm_new[8:12])
I_bcm4a_avg_src = list(I_bcm4a_avg_new[8:12])
Q_src = list(bcm4a_charge_new[8:12])
Q_csum_src = np.cumsum(Q_src)

T2_scl_per_mC_src = np.array(T2_scl_per_mC_src)
I_bcm4a_avg_src = np.array(I_bcm4a_avg_src)
Q_csum_src = np.array(Q_csum_src)

print('Q=',Q_csum_src)
print('T2_scaler=',T2_scl_per_mC_src)
print('Ib = ', I_bcm4a_avg_src)

fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')

ax1.plot(I_bcm4a_avg_src, T2_scl_per_mC_src, marker='^', color='black', markerfacecolor='white', markersize=8, linestyle='None', label=r'Ca48 SRC data ($I_{b} < 50 \mu$A')

ax1.set_ylim([0.93, 0.98])
ax1.grid()
ax1.legend(loc='upper left',fontsize=12)
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.set_xlabel(r'Beam Current [$\mu$A]', fontsize=16)

ax1.tick_params(axis='both', which='both', labelsize=15)

#-----

ax2.plot(Q_csum_src, T2_scl_per_mC_src, marker='^', color='black', markerfacecolor='white', markersize=8, linestyle='None', label=r'Ca48 SRC data ($I_{b} < 50 \mu$A')

ax2.set_ylim([0.93, 0.98])
ax2.grid()
ax2.legend(loc='upper left',fontsize=12)
ax2.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax2.set_xlabel(r'Beam Charge [mC]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)



plt.show()
