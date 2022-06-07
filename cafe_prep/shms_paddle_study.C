void shms_paddle_study(){

  TFile *f = new TFile("cafe_replay_prod_3376_-1.root", "READ");

  TTree *T=(TTree *)f->Get("T");

  TH1F *hcoin_time=0;

  //TCanvas *c1 = new TCanvas("c1", "", 500,500);
  TCanvas *c2 = new TCanvas("c2", "", 500,500);
  //TCanvas *c3 = new TCanvas("c3", "", 500,500);
  //TCanvas *c4 = new TCanvas("c4", "", 500,500);
  //TCanvas *c5 = new TCanvas("c5", "", 500,500);
  
  //c1->cd();
  //T->Draw("CTime.epCoinTime_ROC2>>hcoin_time(100,-100,400)");


  c2->cd();
  c2->Divide(2,2);
  c2->cd(1);
  // S1X+ occupancy
  T->Draw("P.hod.1x.numGoodPosAdcHits>>noCuts(100,0.01,14)", "");  
  T->Draw("P.hod.1x.numGoodPosAdcHits>>delta>=5(100,0.01,14)", "P.gtr.dp>=5", "sames");  
  T->Draw("P.hod.1x.numGoodPosAdcHits>>ctime.AND.delta>=5(100,0.01,14)", "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5", "sames"); 
 
  
  c2->cd(2);
  // S1X- occupancy
  T->Draw("P.hod.1x.numGoodNegAdcHits>>noCuts(100,0.01,14)", "");
  T->Draw("P.hod.1x.numGoodNegAdcHits>>delta>=5(100,0.01,14)", "P.gtr.dp>=5", "sames");
  T->Draw("P.hod.1x.numGoodNegAdcHits>>ctime.AND.delta>=5(100,0.01,14)", "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5", "sames");
  c2->cd(3);
  // S2X+ occupancy
  T->Draw("P.hod.2x.numGoodPosAdcHits>>noCuts(100,0.01,14)", "");
  T->Draw("P.hod.2x.numGoodPosAdcHits>>delta>=5(100,0.01,14)", "P.gtr.dp>=5", "sames");
  T->Draw("P.hod.2x.numGoodPosAdcHits>>ctime.AND.delta>=5(100,0.01,14)", "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5", "sames");
  c2->cd(4);
  // S2X- occupancy
  T->Draw("P.hod.2x.numGoodNegAdcHits>>noCuts(100,0.01,14)", "");
  T->Draw("P.hod.2x.numGoodNegAdcHits>>delta>=5(100,0.01,14)", "P.gtr.dp>=5", "sames");
  T->Draw("P.hod.2x.numGoodNegAdcHits>>ctime.AND.delta>=5(100,0.01,14)", "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5", "sames");
  /*
  c3->cd();
  // shms delta (with / without occupancy cuts)
  T->Draw("P.gtr.dp>>delta_noCuts(100,-10,22)", "");
  //T->Draw("P.gtr.dp>>delta_S1X+S2X_GoodadcCounter>=7(100,-10,22)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7", "sames");
  //T->Draw("P.gtr.dp>>delta_S1X+S2X_adcCounter>=7(100,-10,22)", "P.hod.1x.posAdcCounter>=7&&P.hod.1x.negAdcCounter>=7&&P.hod.2x.posAdcCounter>=7&&P.hod.2x.negAdcCounter>=7", "sames");
  //T->Draw("P.gtr.dp>>delta_S1X+S2X_adcCounter>=7.AND.ctime(100,-10,22)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7&&CTime.epCoinTime_ROC2>0&&CTime.epCoinTime_ROC2<20.", "sames");

  
  c4->cd();
  c4->Divide(3,2);
  // Hodo Track X vs. delta (track x is in dispersive direction, i.e., vertical bend)
  c4->cd(1);
  T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>noCut(100,-10,22, 100,-70,70)", "", "colz");
  c4->cd(2);
  T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>S1X+S2X_adcCounter>=7(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7", "colz");
  c4->cd(3);
  T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>S1X+S2X_adcCounter>=7.AND.ctime(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7&&CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.", "colz");
  c4->cd(4);
  T->Draw("P.hod.2x.TrackXPos:P.gtr.dp>>noCut(100,-10,22, 100,-70,70)", "", "colz");
  c4->cd(5);
  T->Draw("P.hod.2x.TrackXPos:P.gtr.dp>>S1X+S2X_adcCounter>=7(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7", "colz");
  c4->cd(6);
  T->Draw("P.hod.2x.TrackXPos:P.gtr.dp>>S1X+S2X_adcCounter>=7.AND.ctime(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7&&CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.", "colzs");
  
  
  c5->cd();
  //T->Draw("P.kin.primary.W>>noCut(40,0.85,1.05)", "", "");
  //T->Draw("P.kin.primary.W>>ctime(40,0.85,1.05)", "CTime.epCoinTime_ROC2>0&&CTime.epCoinTime_ROC2<20.", "sames");
  T->Draw("P.kin.primary.W>>ctime.AND.delta>=5(40,0.85,1.05)",                "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5", "");
  T->Draw("P.kin.primary.W>>ctime.AND.delta>=5.AND.S1X+S2X>=7(40,0.85,1.05)", "CTime.epCoinTime_ROC2>=0&&CTime.epCoinTime_ROC2<=20.&&P.gtr.dp>=5&&P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7", "sames");
  */
  
}
/*
root [4] T->Draw("CTime.epCoinTime_ROC2>>(100,0,400)")
root [5] T->Draw("CTime.epCoinTime_ROC2>>(100,-50,400)")
root [6] T->Draw("CTime.epCoinTime_ROC2>>(100,-50,50)")
root [7] T->Draw("P.hod.1x.numGoodPosAdcHits")
root [8] T->Draw("P.hod.1x.numGoodPosAdcHits>>(100,0.01,14)")
root [9] T->Draw("P.hod.1x.numGoodPosAdcHits>>S1X+_noCuts(100,0.01,14)")
root [10] T->Draw("P.hod.1x.numGoodPosAdcHits>>S1X+_delta>=5(100,0.01,14)", "P.gtr.dp>=5")
(long long) 373191
root [11] T->Draw("P.hod.1x.numGoodPosAdcHits>>S1X+_delta>=5&&coinTimeCut(100,0.01,14)", "P.gtr.dp>=5&&CTime.epCoinTime_ROC2>0&&CTime.epCoinTime_ROC2<20.")
(long long) 213408
root [12] T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>(100,-10,22, 100,-70,70)", "", "colz")
(long long) 35778
root [13] T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7", "colz")
(long long) 39992
root [14] T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7", "colz")
(long long) 12565
root [15] T->Draw("P.hod.1x.TrackXPos:P.gtr.dp>>(100,-10,22, 100,-70,70)", "P.hod.1x.numGoodPosAdcHits>=7&&P.hod.1x.numGoodNegAdcHits>=7&&P.hod.2x.numGoodPosAdcHits>=7&&P.hod.2x.numGoodNegAdcHits>=7&&P.gtr.dp>=5&&CTime.epCoinTime_ROC2>0&&CTime.epCoinTime_ROC2<20.", "colz")
(long long) 5966
*/
