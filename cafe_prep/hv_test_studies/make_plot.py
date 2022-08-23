import plotly.express as px
import numpy as np
import pandas as pd

df = pd.read_csv("hv_test_data.csv") 
run = df['run']
evt = df['evt']
W_cnts = df['W_cnts_per_mC']
charge = df['charge']
T1_scl = df['T1_scl']
T2_scl = df['T2_scl']
df['T1_scl_err'] = np.sqrt(T1_scl)
df['T2_scl_err'] = np.sqrt(T2_scl)
hv_status = df['hv_status']
df['T_ratio'] =  T2_scl / T1_scl

#covariance matrix (diagonal elements - variances, sigA^2, sigB^2,  off-diagonal, covariance sigAB)
cov_M = np.cov(T1_scl, T2_scl)

# correlation between A and B
rho_AB = cov_M[0][1] / (np.sqrt(cov_M[0][0])*np.sqrt(cov_M[1][1]))

# error in ratio f = A/B = |f| sqrt( (sigA/A)^2 + (sigB/B)^2 - 2*sigAB/(A*B) )
#df['T_ratio_err'] = df['T_ratio'] * np.sqrt( np.abs((df['T1_scl_err']/T1_scl)**2 + (df['T2_scl_err']/T2_scl)**2 - 2.*cov_M[0][1]/(np.sqrt(cov_M[0][0])*np.sqrt(cov_M[1][1]))) )
df['T_ratio_err'] = df['T_ratio'] * np.sqrt((df['T1_scl_err']/T1_scl)**2 + (df['T2_scl_err']/T2_scl)**2)


# plot ratio of T2 / T1 scaler counts
fig1 = px.scatter(df, x='evt', y='T_ratio', error_y=df['T_ratio_err'], color='hv_status')

fig1.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig1.update_layout(
    title="Ratio SHMS EL-REAL to Scin. 3/4 Scaler Counts",
    xaxis_title="Events Replayed",
    yaxis_title="R = $T2_{\mathrm{SHMS EL-REAL} } / T1_{\mathrm{SHMS-3/4}}$",
    legend_title="",
    font=dict(
        family="Times",
        size=18,
        color="Black"
    )
)

fig1.show()


# recover pure statsitical counts on W
W_on  = df.query('hv_status=="hv_on"')['W_cnts_per_mC'] 
W_off = df.query('hv_status=="hv_off"')['W_cnts_per_mC'] 

# error is computed on true statistical counts, since charge/pre-scale factor is a constant, it does not contribure to stat. unc., so it must be taken out of sqrt(N_counts)
W_on_err = np.sqrt( df.query('hv_status=="hv_on"')['W_cnts_per_mC'] * df.query('hv_status=="hv_on"')['charge'] / 65. ) * (65/df.query('hv_status=="hv_on"')['charge'])
W_off_err = np.sqrt( df.query('hv_status=="hv_off"')['W_cnts_per_mC'] * df.query('hv_status=="hv_off"')['charge'] / 17. ) * (17./df.query('hv_status=="hv_off"')['charge'])

W_on_err = np.sqrt( df.query('hv_status=="hv_on"')['W_cnts_per_mC'] )
W_off_err = np.sqrt( df.query('hv_status=="hv_off"')['W_cnts_per_mC'] )


W_on = W_on.reset_index()
W_off = W_off.reset_index()

W_on_err = W_on_err.reset_index()
W_off_err = W_off_err.reset_index()


W_ratio = W_off / W_on
W_ratio_err = W_ratio * np.sqrt(  (W_off_err/W_off)**2 + (W_on_err/W_on)**2   )

print(W_ratio)
print(W_ratio_err)

fig2 = px.scatter(x=['10k', '50k', '100k', '500k', '800k', '1M', 'full'], y=[0.66476407, 0.79650518, 0.88077711, 0.85370827, 0.89277749, 0.9161074, 0.89256247],
                  error_y=[0.002924, 0.003040, 0.003336, 0.003122, 0.003266, 0.003350, 0.003213])

fig2.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig2.update_layout(
    title="Ratio of Invariant Mass W",
    xaxis_title="Events Replayed",
    yaxis_title="R = $W_{\mathrm{HV OFF}} / W_{\mathrm{HV ON}}$",
    legend_title="",
    font=dict(
        family="Times",
        size=18,
        color="Black"
    )
)

fig2.show()
