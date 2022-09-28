import numpy as np
import matplotlib.pyplot as plt

runs_ca48_MF = [
    16978,
    16979
]

T2_sclrate_per_I_MF_contam = [
    3315.289,
    3329.997
]

SHMS_EL_CLEAN_per_I_MF_contam = [
    2675,
    2684
]

T2_scl_per_mC_MF = [
    3268398.019,
    3283021.608
]

# normalize all runs to the 1st SRC run
T2_scl_per_mC_MF_norm = [
    3268398.019/3400973.643,
    3283021.608/3400973.643
]

avg_I_MF = [
    27.489,
    27.972
]

#-------------------------


runs_ca48_MF_uncontam = [
    17093,
    17094,
    17096
]

T2_sclrate_per_I_MF_uncontam = [
    3267.929,
    3293.225,
    3440.049
]

SHMS_EL_CLEAN_per_I_MF_uncontam = [
    2598,
    2624,
    2780
]

T2_scl_per_mC_MF_uncontam = [
    3220936.006,
    3246244.621,
    3393084.293
]

# normalize all runs to the 1st SRC run
T2_scl_per_mC_MF_uncontam_norm = [
    3220936.006/3400973.643,
    3246244.621/3400973.643,
    3393084.293/3400973.643
]

avg_I_MF_uncontam = [
    28.783,
    33.181,
    60.046
]

#---------------------------

runs_ca48_src = [
       17036,
       17037,
       17038,
       17039,
       17040,
       17041,
       17045,
       17046,
       17047,
       17048,
       17049,
       17050,
       17051,
       17052,
       17053,
       17054,
       17055,
       17056,
       17057]

avg_I_SRC = [51.922,
             51.387,
             55.110,
             52.978,
             51.435,
             53.038,
             46.177,
             43.117,
             50.509,
             51.059,
             54.599,
             55.916,
             55.529,
             54.356,
             54.631,
             55.343,
             55.056,
             56.409,
             55.121]


T2_scl_per_mC_SRC = [
    3400973.643,
    3379238.008,
    3382185.694,
    3369822.227,
    3348190.292,
    3351655.718,
    3292082.790,
    3284114.833,
    3336595.083,
    3327723.409,
    3346778.737,
    3346763.341,
    3343435.212,
    3337283.510,
    3334039.730,
    3334624.234,
    3331341.202,
    3331518.378,
    3325337.344
]


# normalize all runs to the 1st SRC run
T2_scl_per_mC_SRC_norm = [
    3400973.643/3400973.643,
    3379238.008/3400973.643,
    3382185.694/3400973.643,
    3369822.227/3400973.643,
    3348190.292/3400973.643,
    3351655.718/3400973.643,
    3292082.790/3400973.643,
    3284114.833/3400973.643,
    3336595.083/3400973.643,
    3327723.409/3400973.643,
    3346778.737/3400973.643,
    3346763.341/3400973.643,
    3343435.212/3400973.643,
    3337283.510/3400973.643,
    3334039.730/3400973.643,
    3334624.234/3400973.643,
    3331341.202/3400973.643,
    3331518.378/3400973.643,
    3325337.344/3400973.643
]


# T2 (SHMS EL-REAL) scaler rate / avg. current [Hz / uA] = [ s^-1 / (uC*s^-1)] = [uC^-1] --> T2 Counts / uC
# Obtained from analyzed scalers which have fine cut on bcm charge
T2_sclrate_per_I = [
                  3448.005,
                  3426.201,
                  3429.217,
                  3416.833,
                  3395.148,
                  3398.635,
                  3339.072,
                  3331.087,
                  3383.574,
                  3374.758,
                  3393.801,
                  3393.752,
                  3390.424,
                  3384.276,
                  3381.041,
                  3381.622,
                  3378.354,
                  3378.507,
                  3372.321]


# SHMS EL_CLEAN (done from interactive raw ROOTfile (SHMS EL CLEAN Counts / uC)
SHMS_EL_CLEAN_per_I = [2814,
                       2800,
                       2794,
                       2789,
                       2774,
                       2776,
                       2703,
                       2702,
                       2753,
                       2737,
                       2759,
                       2758,
                       2757,
                       2754,
                       2752,
                       2750,
                       2746,
                       2744,
                       2739
]

fig0, (ax1, ax2) = plt.subplots(2)
ax1.set_title('T2 Scaler Counts / Charge Normalized to 1st SRC Run: 17036')
#ax2.set_title('Beam Current')

ax1.plot(runs_ca48_MF, T2_scl_per_mC_MF_norm, marker='o', color='blue', markersize=7, linestyle='None', label='MF')
ax1.plot(runs_ca48_src, T2_scl_per_mC_SRC_norm, marker='o', color='red', markersize=7, linestyle='None', label='SRC')
ax1.plot(runs_ca48_MF_uncontam, T2_scl_per_mC_MF_uncontam_norm, marker='o', color='green', markersize=7, linestyle='None', label='MF (round 2)')
ax1.set_ylabel('Normalized T2 scalers/mC', fontsize=20)
ax1.tick_params(axis='both', which='both', labelsize=17)
#ax1.set_xlabel('Run Number', fontsize=20)

ax2.plot(runs_ca48_MF, avg_I_MF, marker='o', color='blue', markersize=7, linestyle='None', label='MF')
ax2.plot(runs_ca48_src, avg_I_SRC, marker='o', color='red', markersize=7, linestyle='None', label='SRC')
ax2.plot(runs_ca48_MF_uncontam, avg_I_MF_uncontam, marker='o', color='green', markersize=7, linestyle='None', label='MF (round 2)')
ax2.set_ylabel('Averge Beam Current [uA]', fontsize=20)
ax2.tick_params(axis='both', which='both', labelsize=17)

ax2.set_xlabel('Run Number', fontsize=20)

ax1.set_xlim([16970, 17099])
ax2.set_xlim([16970, 17099])

ax1.set_ylim([0.94, 1.02])
ax2.set_ylim([25, 65])

ax1.grid()
ax2.grid()

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

plt.show()

'''
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Ca-48 H-Contamination Study', fontsize=15)

ax1.set_title('SHMS EL-REAL (and EL-CLEAN) Scaler Rates / Avg. Current')
ax2.set_title('T2 (SHMS EL_REAL) scaler counts / charge [Counts / mC]')
ax3.set_title('Beam Current')

# plot Ca48 MF (w/ H-contamination, W peak present)
ax1.plot(runs_ca48_MF, T2_sclrate_per_I_MF_contam, marker='o', color='blue', markersize=7, linestyle='None', label='MF, EL-REAL')
ax1.plot(runs_ca48_MF, SHMS_EL_CLEAN_per_I_MF_contam, marker='^', color='blue',  markersize=7,linestyle='None', label='MF, EL-CLEAN')

ax2.plot(runs_ca48_MF, T2_scl_per_mC_MF, marker='o', color='blue', markersize=7, linestyle='None', label='MF')

ax3.plot(runs_ca48_MF, avg_I_MF, marker='o', color='blue', markersize=7, linestyle='None', label='MF')


# plot Ca48 SRC 
ax1.plot(runs_ca48_src, T2_sclrate_per_I, marker='o', color='red', markersize=7,linestyle='None', label='SRC, EL-REAL')
ax1.plot(runs_ca48_src, SHMS_EL_CLEAN_per_I, marker='^', color='red', markersize=7,linestyle='None', label='SRC, EL-CLEAN')

ax2.plot(runs_ca48_src, T2_scl_per_mC_SRC, marker='o', color='red', markersize=7,linestyle='None', label='SRC')

ax3.plot(runs_ca48_src, avg_I_SRC, marker='o', color='red', markersize=7, linestyle='None', label='SRC')

# plot Ca48 MF (w/out H-contamination)
ax1.plot(runs_ca48_MF_uncontam, T2_sclrate_per_I_MF_uncontam, marker='o', markersize=7,color='green', linestyle='None', label='MF, EL-REAL (round 2)')
ax1.plot(runs_ca48_MF_uncontam, SHMS_EL_CLEAN_per_I_MF_uncontam, marker='^',markersize=7, color='green', linestyle='None', label='MF, EL-CLEAN (round 2)')

ax2.plot(runs_ca48_MF_uncontam, T2_scl_per_mC_MF_uncontam , marker='o', markersize=7,color='green', linestyle='None', label='MF (round 2)')
ax3.plot(runs_ca48_MF_uncontam, avg_I_MF_uncontam, marker='o', color='green', markersize=7, linestyle='None', label='MF (round 2)')

ax3.set_xlabel('Run Number')


ax1.set_ylim([2600, 3500])
ax2.set_ylim([3200000, 3450000])
ax3.set_ylim([25, 65])

ax1.set_xlim([16970, 17099])
ax2.set_xlim([16970, 17099])
ax3.set_xlim([16970, 17099])

ax1.grid()
ax2.grid()
ax3.grid()

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')
ax3.legend(loc='upper left')


plt.show()
'''
