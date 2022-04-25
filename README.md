# CaFe-Online
For information on the Hall C CaFe Experiment, please see the CaFe Wiki:
[Hall C Wiki: CaFe Preparation](https://hallcweb.jlab.org/wiki/index.php/CaFe_Preparation)

This repository, `CaFe-Online`, is used to keep track of simulation/analysis code used in preparation for the Hall C CaFe experiment scheduled for August 2022.  This work space mainly consists of various submodules (independent git repos within this repo) which are necessary to carry out a general Hall C analysis.  <br> 

The submodules are: <br>

`hcana` : main Hall C Analyzer (analysis of raw data files (.dat) into ROOTfiles in ntuple-format) <br>

`cafe_online_replay`: CaFe version of the Hall C analysis replay repository, `hallc_replay`, with: <br> 

(a) data analysis replay scripts (runs thru hcana) to generate ROOTfiles from raw data,  <br>
(b) detector calibration scripts, <br>
(c) parameters/calibration files storage thru Hall C database  <br>

`deut_simc`: modified version (for deuteron) of the Hall C simulation software, `simc_gfortran`, to read numerical files from the Laget deuteron model and apply the event weighting using either Laget PWIA or FSI models.  <br>

`hallc_simulations`: useful scripts to <br>

(a) carry out multiple simulations (using input files), <br>
(b) do simulation analysis, <br>
(c) beam time/ rate estimates, <br>
(d) data-to-simulation comparisons <br>


# Accessing Git Submodules for Starters
Assuming the user has not yet cloned the `CaFe-Online` repository, here are the initial steps to get started: <br>

`step 1: `