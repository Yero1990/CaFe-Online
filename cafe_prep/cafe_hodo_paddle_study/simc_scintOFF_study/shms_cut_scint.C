void shms_cut_scint()
{

  // ------ all SHMS S1X , S2X paddles ON -----
  // cafe heep kin 0 : 10000 events, normfac = 890001., charge_factor = 216 mC (60 uA for 1 hr)
  // all SHMS S1X , S2X paddles ON
  // h10->Draw("W>>W_kin0(100,0.88,1.06)", "Weight*(890001./10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)")
  //h10->Draw("ssxfp:ssyfp>>Xfp_vs_Y_fp(100,-70,70, 100,-80,80)", "Weight*(890001./10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)", "colz")  

 
  //------- SHMS S1XS paddle < 7 OFF , S2X paddles < 7 OFF -------
  // cafe heep kin 0 : 10000 events, normfac=850153., charge_factor = 216 mC (60 uA for 1 hr)  
  // h10->Draw("W>>W_kin0(100,0.88,1.06)", "Weight*(850153./10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)")          
  //h10->Draw("ssxfp:ssyfp>>Xfp_vs_Y_fp(100,-70,70, 100,-80,80)", "Weight*(850153./10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)", "colz")  

  //------- SHMS S1XS paddle > 6 OFF , S2X paddles > 6 OFF (TOOK ~ 10 min to run sim, so it is a clue that its working, since its so difficult to get elastic events in a region where few to none are expected) -------   
  //cafe heep kin 0 : 10000 events, normfac=0.478232E+05, charge_factor = 216 mC (60 uA for 1 hr) 
  // h10->Draw("W>>W_kin0(100,0.88,1.06)", "Weight*(47823.2/10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)")  
  //h10->Draw("ssxfp:ssyfp>>Xfp_vs_Y_fp(100,-70,70, 100,-80,80)", "Weight*(47823.2/10000)*216.*(ssdelta>-10.&&ssdelta<22.&&abs(hsdelta)<10.&&abs(hsxptar)<=0.06&&abs(hsyptar)<0.035&&abs(ssxptar)<=0.04&&abs(ssyptar)<=0.024)", "colz")

}
