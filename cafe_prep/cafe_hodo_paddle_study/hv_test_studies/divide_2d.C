

void divide_2d(){
  
  
  // histos

  gStyle->SetOptStat(0);

  //TH2F dc_xfp_vs_yfp_hvON = TH2F("h1", "", 13, -50, 50, 13, -50, 50);
  //dc_xfp_vs_yfp_hvOFF = TH2F("h2"); // new TH2F("dc_xfp_vs_yfp_hvOFF", "", 13, -50, 50, 13, -50, 50); 
  TH2F *dc_fp_ratio = new TH2F("dc_fp_ratio", "", 13, -50, 50, 13, -50, 50);

  TH2F *hod_S1X_ScinPos_ratio = new TH2F("hod_S1X_ScinPos_ratio", "", 13, -50, 50, 13, -50, 50);  
  TH2F *hod_S1X_TrackPos_ratio = new TH2F("hod_S1X_TrackPos_ratio", "", 13, -50, 50, 13, -50, 50); 

  TH2F *hod_S1Y_ScinPos_ratio = new TH2F("hod_S1Y_ScinPos_ratio", "", 13, -50, 50, 13, -50, 50);  
  TH2F *hod_S1Y_TrackPos_ratio = new TH2F("hod_S1Y_TrackPos_ratio", "", 13, -50, 50, 13, -50, 50); 

  TH2F *hod_S2X_ScinPos_ratio = new TH2F("hod_S2X_ScinPos_ratio", "", 14, -67, 67, 14, -67, 67);  
  TH2F *hod_S2X_TrackPos_ratio = new TH2F("hod_S2X_TrackPos_ratio", "", 14, -67, 67, 14, -67, 67); 

  TH2F *hod_S2Y_ScinPos_ratio = new TH2F("hod_S2Y_ScinPos_ratio", "", 21, -53, 53, 21, -53, 53);  
  TH2F *hod_S2Y_TrackPos_ratio = new TH2F("hod_S2Y_TrackPos_ratio", "", 21, -53, 53, 21, -53, 53); 
  
  


  TFile *f1 = new TFile("cafe_replay_prod_16036_-1.root");
  TFile *f2 = new TFile("cafe_replay_prod_16037_-1.root "); 

  Double_t hvON_scale = 65./16.655; // Ps2_factor / total_charge (assuming full run)
  Double_t hvOFF_scale = 17./7.822;

  f1->cd();
  TTree *T_hv_on = (TTree*)f1->Get("T");
  
  T_hv_on->Draw("P.kin.primary.W>>W_hvON(100,0.5,1.5)", "P.cal.etottracknorm>0.6");
  TH1F *W_hvON = (TH1F*)gPad->GetPrimitive("W_hvON");

  // DC focal plane
  T_hv_on->Draw("P.dc.x_fp:P.dc.y_fp>>dc_fp_hvON(13,-50,50,13,-50,50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *dc_fp_hvON = (TH2F*)gPad->GetPrimitive("dc_fp_hvON");

  // S1X
  T_hv_on->Draw("P.hod.1x.ScinXPos:P.hod.1x.ScinYPos>>S1X_ScinPos_XvsY_hvON(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S1XScinPos_hvON = (TH2F*)gPad->GetPrimitive("S1X_ScinPos_XvsY_hvON"); 

  T_hv_on->Draw("P.hod.1x.TrackXPos:P.hod.1x.TrackYPos>>S1X_TrackPos_XvsY_hvON(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S1XTrackPos_hvON = (TH2F*)gPad->GetPrimitive("S1X_TrackPos_XvsY_hvON");  

  // S1Y
  T_hv_on->Draw("P.hod.1y.ScinXPos:P.hod.1y.ScinYPos>>S1Y_ScinPos_XvsY_hvON(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S1YScinPos_hvON = (TH2F*)gPad->GetPrimitive("S1Y_ScinPos_XvsY_hvON"); 

  T_hv_on->Draw("P.hod.1y.TrackXPos:P.hod.1y.TrackYPos>>S1Y_TrackPos_XvsY_hvON(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S1YTrackPos_hvON = (TH2F*)gPad->GetPrimitive("S1Y_TrackPos_XvsY_hvON");  

  // S2X
  T_hv_on->Draw("P.hod.2x.ScinXPos:P.hod.2x.ScinYPos>>S2X_ScinPos_XvsY_hvON(14,-67,67, 14, -67, 67)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S2XScinPos_hvON = (TH2F*)gPad->GetPrimitive("S2X_ScinPos_XvsY_hvON"); 

  T_hv_on->Draw("P.hod.2x.TrackXPos:P.hod.2x.TrackYPos>>S2X_TrackPos_XvsY_hvON(14,-67,67, 14, -67, 67)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S2XTrackPos_hvON = (TH2F*)gPad->GetPrimitive("S2X_TrackPos_XvsY_hvON");  

  // S2Y
  T_hv_on->Draw("P.hod.2y.ScinXPos:P.hod.2y.ScinYPos>>S2Y_ScinPos_XvsY_hvON(21,-53,53, 21, -53, 53)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S2YScinPos_hvON = (TH2F*)gPad->GetPrimitive("S2Y_ScinPos_XvsY_hvON"); 

  T_hv_on->Draw("P.hod.2y.TrackXPos:P.hod.2y.TrackYPos>>S2Y_TrackPos_XvsY_hvON(21,-53,53, 21, -53, 53)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S2YTrackPos_hvON = (TH2F*)gPad->GetPrimitive("S2Y_TrackPos_XvsY_hvON");  


  // Shower Pulse Int/Amp vs. event number and adcCounter
  T_hv_on->Draw("P.cal.fly.goodAdcPulseInt:g.evnum>>fly_pI_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 20)", "", "colz");
  TH2F *fly_pI_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("fly_pI_vs_evNum_hvON");

  T_hv_on->Draw("P.cal.fly.goodAdcPulseInt:P.cal.fly.adcCounter>>fly_pI_vs_PMT_hvON(224,0.5,224.5, 100,0.001,20)", "", "colz");
  TH2F *fly_pI_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("fly_pI_vs_PMT_hvON");
    
  T_hv_on->Draw("P.cal.fly.goodAdcPulseAmp:g.evnum>>fly_pA_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 30)", "", "colz");
  TH2F *fly_pA_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("fly_pA_vs_evNum_hvON");
 
  T_hv_on->Draw("P.cal.fly.goodAdcPulseAmp:P.cal.fly.adcCounter>>fly_pA_vs_PMT_hvON(224,0.5,224.5, 100,0.001,30)", "", "colz");
  TH2F *fly_pA_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("fly_pA_vs_PMT_hvON");

  // pre-Shower (+,-) Pulse Int vs. event number and adcCounter
  T_hv_on->Draw("P.cal.pr.goodPosAdcPulseInt:g.evnum>>prSh_pI_pos_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 20)", "", "colz");
  TH2F *prSh_pI_pos_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("prSh_pI_pos_vs_evNum_hvON");

  T_hv_on->Draw("P.cal.pr.goodNegAdcPulseInt:g.evnum>>prSh_pI_neg_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 20)", "", "colz");
  TH2F *prSh_pI_neg_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("prSh_pI_neg_vs_evNum_hvON");
  
  T_hv_on->Draw("P.cal.pr.goodPosAdcPulseInt:P.cal.pr.posAdcCounter>>prSh_pI_pos_vs_PMT_hvON(14,0.5,14.5, 100,0.001,20)", "", "colz");
  TH2F *prSh_pI_pos_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("prSh_pI_pos_vs_PMT_hvON");

  T_hv_on->Draw("P.cal.pr.goodNegAdcPulseInt:P.cal.pr.negAdcCounter>>prSh_pI_neg_vs_PMT_hvON(14,0.5,14.5, 100,0.001,20)", "", "colz");
  TH2F *prSh_pI_neg_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("prSh_pI_neg_vs_PMT_hvON");

  // pre-Shower (+,-) Pulse Amp vs. event number and adcCounter
  T_hv_on->Draw("P.cal.pr.goodPosAdcPulseAmp:g.evnum>>prSh_pA_pos_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 30)", "", "colz");
  TH2F *prSh_pA_pos_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("prSh_pA_pos_vs_evNum_hvON");

  T_hv_on->Draw("P.cal.pr.goodNegAdcPulseAmp:g.evnum>>prSh_pA_neg_vs_evNum_hvON(12, 0, 2600000, 100, 0.001, 30)", "", "colz");
  TH2F *prSh_pA_neg_vs_evNum_hvON = (TH2F*)gPad->GetPrimitive("prSh_pA_neg_vs_evNum_hvON");
  
  T_hv_on->Draw("P.cal.pr.goodPosAdcPulseAmp:P.cal.pr.posAdcCounter>>prSh_pA_pos_vs_PMT_hvON(14,0.5,14.5, 100,0.001,30)", "", "colz");
  TH2F *prSh_pA_pos_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("prSh_pA_pos_vs_PMT_hvON");

  T_hv_on->Draw("P.cal.pr.goodNegAdcPulseAmp:P.cal.pr.negAdcCounter>>prSh_pA_neg_vs_PMT_hvON(14,0.5,14.5, 100,0.001,30)", "", "colz");
  TH2F *prSh_pA_neg_vs_PMT_hvON = (TH2F*)gPad->GetPrimitive("prSh_pA_neg_vs_PMT_hvON");

  //--------------------
  
  W_hvON->Scale(hvON_scale);
  dc_fp_hvON->Scale(hvON_scale);

  hod_S1XScinPos_hvON->Scale(hvON_scale);
  hod_S1XTrackPos_hvON->Scale(hvON_scale);   

  hod_S1YScinPos_hvON->Scale(hvON_scale);
  hod_S1YTrackPos_hvON->Scale(hvON_scale);

  hod_S2XScinPos_hvON->Scale(hvON_scale);
  hod_S2XTrackPos_hvON->Scale(hvON_scale);

  hod_S2YScinPos_hvON->Scale(hvON_scale);
  hod_S2YTrackPos_hvON->Scale(hvON_scale);
  
  f2->cd();  
  
  TTree *T_hv_off = (TTree*)f2->Get("T"); 
  
  T_hv_off->Draw("P.kin.primary.W>>W_hvOFF(100,0.5,1.5)", "P.cal.etottracknorm>0.6"); 
  TH1F *W_hvOFF = (TH1F*)gPad->GetPrimitive("W_hvOFF"); 
  
  T_hv_off->Draw("P.dc.x_fp:P.dc.y_fp>>dc_fp_hvOFF(13, -50, 50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");  
  TH2F *dc_fp_hvOFF = (TH2F*)gPad->GetPrimitive("dc_fp_hvOFF");  

  // S1X
  T_hv_off->Draw("P.hod.1x.ScinXPos:P.hod.1x.ScinYPos>>S1X_ScinPos_XvsY_hvOFF(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S1XScinPos_hvOFF = (TH2F*)gPad->GetPrimitive("S1X_ScinPos_XvsY_hvOFF"); 
  
  T_hv_off->Draw("P.hod.1x.TrackXPos:P.hod.1x.TrackYPos>>S1X_TrackPos_XvsY_hvOFF(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");  
  TH2F *hod_S1XTrackPos_hvOFF = (TH2F*)gPad->GetPrimitive("S1X_TrackPos_XvsY_hvOFF");      

  // S1Y
  T_hv_off->Draw("P.hod.1y.ScinXPos:P.hod.1y.ScinYPos>>S1Y_ScinPos_XvsY_hvOFF(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S1YScinPos_hvOFF = (TH2F*)gPad->GetPrimitive("S1Y_ScinPos_XvsY_hvOFF"); 
  
  T_hv_off->Draw("P.hod.1y.TrackXPos:P.hod.1y.TrackYPos>>S1Y_TrackPos_XvsY_hvOFF(13,-50,50, 13, -50, 50)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");  
  TH2F *hod_S1YTrackPos_hvOFF = (TH2F*)gPad->GetPrimitive("S1Y_TrackPos_XvsY_hvOFF");

  // S2X
  T_hv_off->Draw("P.hod.2x.ScinXPos:P.hod.2x.ScinYPos>>S2X_ScinPos_XvsY_hvOFF(14,-67,67, 14, -67, 67)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S2XScinPos_hvOFF = (TH2F*)gPad->GetPrimitive("S2X_ScinPos_XvsY_hvOFF"); 

  T_hv_off->Draw("P.hod.2x.TrackXPos:P.hod.2x.TrackYPos>>S2X_TrackPos_XvsY_hvOFF(14,-67,67, 14, -67, 67)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S2XTrackPos_hvOFF = (TH2F*)gPad->GetPrimitive("S2X_TrackPos_XvsY_hvOFF");  

  // S2Y
  T_hv_off->Draw("P.hod.2y.ScinXPos:P.hod.2y.ScinYPos>>S2Y_ScinPos_XvsY_hvOFF(21,-53,53, 21, -53, 53)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz");
  TH2F *hod_S2YScinPos_hvOFF = (TH2F*)gPad->GetPrimitive("S2Y_ScinPos_XvsY_hvOFF"); 

  T_hv_off->Draw("P.hod.2y.TrackXPos:P.hod.2y.TrackYPos>>S2Y_TrackPos_XvsY_hvOFF(21,-53,53, 21, -53, 53)", "P.kin.primary.W>0.85&&P.kin.primary.W<1.05", "colz"); 
  TH2F *hod_S2YTrackPos_hvOFF = (TH2F*)gPad->GetPrimitive("S2Y_TrackPos_XvsY_hvOFF"); 


  
  // Shower Pulse Int/Amp vs. event number and adcCounter
  T_hv_off->Draw("P.cal.fly.goodAdcPulseInt:g.evnum>>fly_pI_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 20)", "", "colz");
  TH2F *fly_pI_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("fly_pI_vs_evNum_hvOFF");

  T_hv_off->Draw("P.cal.fly.goodAdcPulseInt:P.cal.fly.adcCounter>>fly_pI_vs_PMT_hvOFF(224,0.5,224.5, 100,0.001,20)", "", "colz");
  TH2F *fly_pI_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("fly_pI_vs_PMT_hvOFF");
    
  T_hv_off->Draw("P.cal.fly.goodAdcPulseAmp:g.evnum>>fly_pA_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 30)", "", "colz");
  TH2F *fly_pA_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("fly_pA_vs_evNum_hvOFF");
 
  T_hv_off->Draw("P.cal.fly.goodAdcPulseAmp:P.cal.fly.adcCounter>>fly_pA_vs_PMT_hvOFF(224,0.5,224.5, 100,0.001,30)", "", "colz");
  TH2F *fly_pA_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("fly_pA_vs_PMT_hvOFF");

  // pre-Shower Pulse Int vs. event number and adcCounter
  T_hv_off->Draw("P.cal.pr.goodPosAdcPulseInt:g.evnum>>prSh_pI_pos_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 20)", "", "colz");
  TH2F *prSh_pI_pos_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pI_pos_vs_evNum_hvOFF");

  T_hv_off->Draw("P.cal.pr.goodNegAdcPulseInt:g.evnum>>prSh_pI_neg_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 20)", "", "colz");
  TH2F *prSh_pI_neg_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pI_neg_vs_evNum_hvOFF");
  
  T_hv_off->Draw("P.cal.pr.goodPosAdcPulseInt:P.cal.pr.posAdcCounter>>prSh_pI_pos_vs_PMT_hvOFF(14,0.5,14.5, 100,0.001,20)", "", "colz");
  TH2F *prSh_pI_pos_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pI_pos_vs_PMT_hvOFF");

  T_hv_off->Draw("P.cal.pr.goodNegAdcPulseInt:P.cal.pr.negAdcCounter>>prSh_pI_neg_vs_PMT_hvOFF(14,0.5,14.5, 100,0.001,20)", "", "colz");
  TH2F *prSh_pI_neg_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pI_neg_vs_PMT_hvOFF");

  // pre-Shower Pulse Amp vs. event number and adcCounter
  T_hv_off->Draw("P.cal.pr.goodPosAdcPulseAmp:g.evnum>>prSh_pA_pos_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 30)", "", "colz");
  TH2F *prSh_pA_pos_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pA_pos_vs_evNum_hvOFF");

  T_hv_off->Draw("P.cal.pr.goodNegAdcPulseAmp:g.evnum>>prSh_pA_neg_vs_evNum_hvOFF(8, 0, 1600000, 100, 0.001, 30)", "", "colz");
  TH2F *prSh_pA_neg_vs_evNum_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pA_neg_vs_evNum_hvOFF");
  
  T_hv_off->Draw("P.cal.pr.goodPosAdcPulseAmp:P.cal.pr.posAdcCounter>>prSh_pA_pos_vs_PMT_hvOFF(14,0.5,14.5, 100,0.001,30)", "", "colz");
  TH2F *prSh_pA_pos_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pA_pos_vs_PMT_hvOFF");

  T_hv_off->Draw("P.cal.pr.goodNegAdcPulseAmp:P.cal.pr.negAdcCounter>>prSh_pA_neg_vs_PMT_hvOFF(14,0.5,14.5, 100,0.001,30)", "", "colz");
  TH2F *prSh_pA_neg_vs_PMT_hvOFF = (TH2F*)gPad->GetPrimitive("prSh_pA_neg_vs_PMT_hvOFF");

  //--------------------
  
  W_hvOFF->Scale(hvOFF_scale);
  dc_fp_hvOFF->Scale(hvOFF_scale); 

  hod_S1XScinPos_hvOFF->Scale(hvOFF_scale); 
  hod_S1XTrackPos_hvOFF->Scale(hvOFF_scale); 

  hod_S1YScinPos_hvOFF->Scale(hvOFF_scale); 
  hod_S1YTrackPos_hvOFF->Scale(hvOFF_scale);

  hod_S2XScinPos_hvOFF->Scale(hvOFF_scale); 
  hod_S2XTrackPos_hvOFF->Scale(hvOFF_scale); 

  hod_S2YScinPos_hvOFF->Scale(hvOFF_scale); 
  hod_S2YTrackPos_hvOFF->Scale(hvOFF_scale);
  
  // Take ratio of HV ON to OFF for efficiency study (if there is no loss, should be W[0.85, 1.05] should be 100% efficient 
  dc_fp_ratio->Divide(dc_fp_hvOFF,dc_fp_hvON);

  hod_S1X_ScinPos_ratio->Divide(hod_S1XScinPos_hvOFF, hod_S1XScinPos_hvON);
  hod_S1X_TrackPos_ratio->Divide(hod_S1XTrackPos_hvOFF, hod_S1XTrackPos_hvON);

  hod_S1Y_ScinPos_ratio->Divide(hod_S1YScinPos_hvOFF, hod_S1YScinPos_hvON);
  hod_S1Y_TrackPos_ratio->Divide(hod_S1YTrackPos_hvOFF, hod_S1YTrackPos_hvON);

  hod_S2X_ScinPos_ratio->Divide(hod_S2XScinPos_hvOFF, hod_S2XScinPos_hvON);
  hod_S2X_TrackPos_ratio->Divide(hod_S2XTrackPos_hvOFF, hod_S2XTrackPos_hvON);

  hod_S2Y_ScinPos_ratio->Divide(hod_S2YScinPos_hvOFF, hod_S2YScinPos_hvON);
  hod_S2Y_TrackPos_ratio->Divide(hod_S2YTrackPos_hvOFF, hod_S2YTrackPos_hvON);

  TList *Hlist = new TList();

  Hlist->Add(W_hvON);
  Hlist->Add(W_hvOFF);

  Hlist->Add(dc_fp_hvON);  
  Hlist->Add(dc_fp_hvOFF);
  Hlist->Add(dc_fp_ratio);


  // S1X
  Hlist->Add(hod_S1XScinPos_hvON);
  Hlist->Add(hod_S1XScinPos_hvOFF);  
  Hlist->Add(hod_S1X_ScinPos_ratio);  

  Hlist->Add(hod_S1XTrackPos_hvON); 
  Hlist->Add(hod_S1XTrackPos_hvOFF);
  Hlist->Add(hod_S1X_TrackPos_ratio);

  //S1Y
  Hlist->Add(hod_S1YScinPos_hvON);
  Hlist->Add(hod_S1YScinPos_hvOFF);  
  Hlist->Add(hod_S1Y_ScinPos_ratio); 

  Hlist->Add(hod_S1YTrackPos_hvON); 
  Hlist->Add(hod_S1YTrackPos_hvOFF);
  Hlist->Add(hod_S1Y_TrackPos_ratio);  

  // S2X
  Hlist->Add(hod_S2XScinPos_hvON);
  Hlist->Add(hod_S2XScinPos_hvOFF);  
  Hlist->Add(hod_S2X_ScinPos_ratio);  

  Hlist->Add(hod_S2XTrackPos_hvON); 
  Hlist->Add(hod_S2XTrackPos_hvOFF);
  Hlist->Add(hod_S2X_TrackPos_ratio);

  //S2Y
  Hlist->Add(hod_S2YScinPos_hvON);
  Hlist->Add(hod_S2YScinPos_hvOFF);  
  Hlist->Add(hod_S2Y_ScinPos_ratio); 

  Hlist->Add(hod_S2YTrackPos_hvON); 
  Hlist->Add(hod_S2YTrackPos_hvOFF);
  Hlist->Add(hod_S2Y_TrackPos_ratio);

  TList *Hlist2 = new TList();

  //Shower/pre-Shower (HV ON)
  Hlist->Add(fly_pI_vs_evNum_hvON);
  Hlist->Add(fly_pI_vs_PMT_hvON);
  Hlist->Add(fly_pA_vs_evNum_hvON);
  Hlist->Add(fly_pA_vs_PMT_hvON);
  
  Hlist->Add(prSh_pI_pos_vs_evNum_hvON);
  Hlist->Add(prSh_pI_neg_vs_evNum_hvON);
  Hlist->Add(prSh_pI_pos_vs_PMT_hvON);
  Hlist->Add(prSh_pI_neg_vs_PMT_hvON);

  Hlist->Add(prSh_pA_pos_vs_evNum_hvON);
  Hlist->Add(prSh_pA_neg_vs_evNum_hvON);
  Hlist->Add(prSh_pA_pos_vs_PMT_hvON);
  Hlist->Add(prSh_pA_neg_vs_PMT_hvON);

  //Shower/pre-Shower (HV OFF)
  Hlist->Add(fly_pI_vs_evNum_hvOFF);
  Hlist->Add(fly_pI_vs_PMT_hvOFF);
  Hlist->Add(fly_pA_vs_evNum_hvOFF);
  Hlist->Add(fly_pA_vs_PMT_hvOFF);
  
  Hlist->Add(prSh_pI_pos_vs_evNum_hvOFF);
  Hlist->Add(prSh_pI_neg_vs_evNum_hvOFF);
  Hlist->Add(prSh_pI_pos_vs_PMT_hvOFF);
  Hlist->Add(prSh_pI_neg_vs_PMT_hvOFF);

  Hlist->Add(prSh_pA_pos_vs_evNum_hvOFF);
  Hlist->Add(prSh_pA_neg_vs_evNum_hvOFF);
  Hlist->Add(prSh_pA_pos_vs_PMT_hvOFF);
  Hlist->Add(prSh_pA_neg_vs_PMT_hvOFF);
  
  TFile *fout = new TFile("hv_study_histos.root","RECREATE"); 

  Hlist->Write("2D_Hodo_Histos", TObject::kSingleKey);

  Hlist2->Write("2D_Cal_Histos", TObject::kSingleKey);

  fout->ls();


}
