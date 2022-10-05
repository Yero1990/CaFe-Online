import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

#df_scaler = pd.read_csv("ca48_report_files/fall2021_bcm/ca48_bcmFall2021.csv")
df_scaler = pd.read_csv("ca48_report_files/ca48_bcmInfo.csv")


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


# fall 2021 bcm calibrations
fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Charge-normalized T2 Scaler Counts Relative to 1st SRC Run', fontsize=16, fontweight='bold')
ax1.plot(run[:2],   T2_per_mC_bcm4a_norm[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax1.plot(run[2:23], T2_per_mC_bcm4a_norm[2:23], marker='o', color='red', markersize=5, linestyle='None', label='Ca48 SRC')
ax1.plot(run[23:],  T2_per_mC_bcm4a_norm[23:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')
ax1.set_ylim([0.9, 1.05])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2],   I_bcm4a_avg[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax2.plot(run[2:23], I_bcm4a_avg[2:23], marker='o', color='red', markersize=5, linestyle='None', label='Ca48 SRC')
ax2.plot(run[23:],  I_bcm4a_avg[23:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')
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
ax1.plot(run[:2],   T2_per_mC_bcm4a_norm_new[:2], marker='^', color='blue', markerfacecolor='white', markersize=5, linestyle='None', label='Ca48 MF (bcm_calib22)')
ax1.plot(run[2:23], T2_per_mC_bcm4a_norm_new[2:23], marker='^', color='red', markerfacecolor='white', markersize=5, linestyle='None', label='Ca48 SRC (bcm_calib22)')
ax1.plot(run[23:],  T2_per_mC_bcm4a_norm_new[23:], marker='^', color='green', markerfacecolor='white', markersize=5, linestyle='None', label='Ca48 MF (round 2, bcm_calib22)')
ax1.set_ylim([0.9, 1.05])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_ylabel('Relative T2 scalers/mC', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2],   I_bcm4a_avg_new[:2], marker='^', color='blue', markerfacecolor='white',   markersize=5, linestyle='None', label='Ca48 MF (bcm_calib22)')
ax2.plot(run[2:23], I_bcm4a_avg_new[2:23], marker='^', color='red', markerfacecolor='white',  markersize=5, linestyle='None', label='Ca48 SRC (bcm_calib22)')
ax2.plot(run[23:],  I_bcm4a_avg_new[23:], marker='^', color='green', markerfacecolor='white', markersize=5, linestyle='None', label='Ca48 MF (round 2, bcm_calib22)')
ax2.set_ylim([25, 65])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
plt.show()


# bcm calib sanity check
fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Fall 2021 BCM Calibration Parameters', fontsize=16, fontweight='bold')
ax1.plot(run,  bcm1_charge, marker='^', color='blue', markerfacecolor='white', markersize=5, linestyle='None', label='BCM1')
ax1.plot(run,  bcm2_charge, marker='^', color='green', markerfacecolor='white', markersize=5, linestyle='None', label='BCM2')
ax1.plot(run,  bcm4a_charge, marker='^', color='red', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4A')
ax1.plot(run,  bcm4b_charge, marker='^', color='magenta', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4B')
ax1.plot(run,  bcm4c_charge, marker='^', color='violet', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4C')
ax1.set_ylim([-50, 50])
ax1.set_xticklabels([])
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_ylabel('BCM Charge [mC]', fontsize=16)
ax1.tick_params(axis='both', which='both', labelsize=15)

ax2.set_title('Summer 2022 BCM Calibration Parameters', fontsize=16, fontweight='bold')
ax2.plot(run,  bcm1_charge_new, marker='^', color='blue', markerfacecolor='white', markersize=5, linestyle='None', label='BCM1')
ax2.plot(run,  bcm2_charge_new, marker='^', color='green', markerfacecolor='white', markersize=5, linestyle='None', label='BCM2')
ax2.plot(run,  bcm4a_charge_new, marker='^', color='red', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4A')
ax2.plot(run,  bcm4b_charge_new, marker='^', color='magenta', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4B')
ax2.plot(run,  bcm4c_charge_new, marker='^', color='violet', markerfacecolor='white', markersize=5, linestyle='None', label='BCM4C')
ax2.set_ylim([0, 230])
ax2.grid()
ax2.legend(loc='upper left', fontsize=12)
ax2.set_ylabel('BCM Charge [mC]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
plt.show()
