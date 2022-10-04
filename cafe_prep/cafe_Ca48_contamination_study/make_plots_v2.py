import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

df_scaler = pd.read_csv("ca48_report_files/fall2021_bcm/ca48_bcmFall2021.csv")

run = df_scaler['run']
kin = df_scaler['kin']
T2_scaler = df_scaler['T2_scaler']  # T2 (SHMS EL-REAL)
bcm1_charge = df_scaler['q_bcm1']   # charge [mC]
bcm2_charge = df_scaler['q_bcm2']
bcm4a_charge = df_scaler['q_bcm4a']
bcm4b_charge = df_scaler['q_bcm4b']
bcm4c_charge = df_scaler['q_bcm4c']

# calculate T2 scaler counts per charge
T2_per_mC_bcm1 = T2_scaler / bcm1_charge
T2_per_mC_bcm2 = T2_scaler / bcm2_charge
T2_per_mC_bcm4a = T2_scaler / bcm4a_charge
T2_per_mC_bcm4b = T2_scaler / bcm4b_charge
T2_per_mC_bcm4c = T2_scaler / bcm4c_charge

print(T2_per_mC_bcm4a/T2_per_mC_bcm4a[2])
'''
fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')
ax1.plot(run[:2],   el_real_sclcnts_per_mC_norm[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax1.plot(run[2:21], el_real_sclcnts_per_mC_norm[2:21], marker='o', color='red', markersize=5, linestyle='None', label='Ca48 SRC')
ax1.plot(run[21:],  el_real_sclcnts_per_mC_norm[21:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')
ax1.set_ylim([0.9, 1.05])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)
#ax1.set_xlabel('Run Number', fontsize=16) 

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2],   I_avg[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax2.plot(run[2:21], I_avg[2:21], marker='o', color='red', markersize=5, linestyle='None', label='Ca48 SRC')
ax2.plot(run[21:],  I_avg[21:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')
ax2.set_ylim([25, 65])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)

plt.show()
'''
