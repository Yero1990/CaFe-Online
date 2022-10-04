import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# read DATA csv files
# data contains regional cuts on Emiss vs. Pmiss plots to select
# H-contamination area (region 1) and pure Ca-48 area (region 2)

df_data = pd.read_csv("ca48_data.csv")

run = df_data['run']
kin = df_data['kin']
charge = df_data['charge']
I_avg = df_data['I_avg']
region1_cnts = df_data['region1_counts']
region2_cnts = df_data['region2_counts']

# Relative Ratio1: region 1 (H-contamination) / region 2 (Ca-48 sample) --> contamination fraction
R = region1_cnts / region2_cnts  # contamination fraction
R_err = R * np.sqrt( (np.sqrt(region1_cnts)/region1_cnts)**2 + (np.sqrt(region2_cnts)/region2_cnts)**2  )

R_rel = R / R[0]  # contamination relative to 1st Ca-48 MF run
R_rel_err = R_err /R[0]

# Relative Ratio2: region 1 (H-contamination) / charge --> charge-normalized hydrogen contamination counts
R2 = region1_cnts /charge
R2_err = np.sqrt(region1_cnts) /charge

R2_rel = R2 / R2[0]
R2_rel_err = R2_err / R2[0]

#print(R)
print('R_rel_err = ', R_rel_err)

fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('Relative H-contamination to 1st Ca-48 MF run', fontsize=16, fontweight='bold')
ax1.errorbar(run[:2], R_rel[:2], R_rel_err[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax1.errorbar(run[2:], R_rel[2:], R_rel_err[2:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')

ax1.errorbar(run[:2], R2_rel[:2], R2_rel_err[:2], marker='^', markerfacecolor='None', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax1.errorbar(run[2:], R2_rel[2:], R2_rel_err[2:], marker='^', markerfacecolor='None', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')


ax1.set_ylabel('Relative H-contamination', fontsize=16) 
ax1.tick_params(axis='both', which='both', labelsize=15) 
ax1.set_xticklabels([])
#ax1.set_xlabel('Run Number', fontsize=16)
ax1.legend(loc='upper right', fontsize=12)
ax1.grid()

ax2.set_title('Beam Current', fontsize=16, fontweight='bold')
ax2.plot(run[:2], I_avg[:2], marker='o', color='blue', markersize=5, linestyle='None', label='Ca48 MF')
ax2.plot(run[2:], I_avg[2:], marker='o', color='green', markersize=5, linestyle='None', label='Ca48 MF (round 2)')
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=16)
ax2.tick_params(axis='both', which='both', labelsize=15)
ax2.set_xlabel('Run Number', fontsize=16)
ax2.legend(loc='upper left', fontsize=12)
ax2.grid()


ax1.set_ylim([0., 1.1])
ax2.set_ylim([25, 65])

plt.plot()
plt.show()


#read scaler csv file
df_scaler = pd.read_csv("ca48_scaler.csv")

run = df_scaler['run']
kin = df_scaler['kin']
I_avg = df_scaler['I_avg']

el_real_sclrate_per_I = df_scaler['sclrate_per_I_elreal']
el_real_sclcnts_per_mC = df_scaler['sclcnts_per_mC_elreal']

el_real_sclrate_per_I_norm = el_real_sclrate_per_I / el_real_sclrate_per_I[2]
el_real_sclcnts_per_mC_norm = el_real_sclcnts_per_mC / el_real_sclcnts_per_mC[2]

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
