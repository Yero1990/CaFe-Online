# CaFe-Online
-

For information on the Hall C CaFe Experiment, please see the CaFe Wiki:
[Hall C Wiki: CaFe Preparation](https://hallcweb.jlab.org/wiki/index.php/CaFe_Preparation)

This repository (repo for short), `CaFe-Online`, is used to keep track of simulation/analysis code used in preparation for the Hall C CaFe experiment scheduled for August 2022.  This work space mainly consists of various submodules (independent git repos within this repo) which are necessary to carry out a general Hall C analysis.  <br> 

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

**NOTE:**  
1. To do Hall C data analysis requires: `hcana` and `cafe_online_replay` submodules.  <br>
2. To do Hall C simulations requires: `deut_simc` and `hallc_simulations` submodules


# Setting Up a CaFe Work Space Remotely
-

In theory, any uses can clone this repository on any machine (local or remote) of their choice. In practice, it is highly recommended to set up a work space on ifarm since, it already has all the necessary tools that a local machine might not have (e.g. ROOT CERN, Python, certain library dependencies / setup for running simulations on gfortran, direct access to raw data file, etc.) 

`step 1:` Assuming the user has a Jefferson Lab account and has access to the JLab machines on ifarm, execute the following commands:

```sh
# login to ifarm
$ ssh -Y user@login.jlab.org 
$ ssh -Y ifarm 

# setup necessary environment variables 
# tip: put this command in you(.cshrc or bashrc) on ifarm so it automatically gets called
# every log-in session (and not have to type by hand every time)
$ source /site/12gev_phys/softenv.csh 2.5 

# Create symbolic link to the CaFe work directory. 
# For more info see [https://hallcweb.jlab.org/wiki/index.php/CaFe_Disk_Space]
$ ln -s /work/hallc/c-cafe-2022/ cafe_work 
$ cd cafe_work 

# If you don't have a user directory, make one and cd to it !
$ mkdir <user> 
$ cd <user>

$ git clone https://github.com/Yero1990/CaFe-Online
$ cd CaFe-Online
```

# Accessing Git Submodules for Starters
-

At this point, the user will be able to various submodules (e.g., hallc_simulations, etc.) which are currently empty and will need to be initialized only ONCE on a given machine you are working on. <br>

 Initialize the submodule of interest 

```sh
$ git submodule update --init <submodule>
NOTE 1: to initialize all submodules at once, do not specify a <submodule>
$ cd <submodule>
$ git branch
NOTE 2: the initialized submodule(s) will be in a HEAD detached state
```

##### NOTE 2 Follow-Up:  
HEAD in a detached state means you are not pointing to any particular branch, and changes can be made safely without impacting other branches. If you would like to keep the changes, then a branch would have to be created: `git checkout -b <branch_name>`, and any changes can be saved and push remotely from the new branch. 

`step 2:` If you plan to make significant contributions to the the official submodule in question, then do (from inside the submodule): <br>

```sh
$ git checkout -b <user_work_branch>

# then after making changes/additions/subtractions, do: 
$ git add <files changed>
$ git commit -m "commit message"
$ git push origin user_work_branch
```
the submodule in question will then have a new branch remotely which can be merged onto the master branch by the repository maintainer. **NOTE:** The user may need to be a member of the repository or project in order to be able to push the changes to a new branch.

# Updating Existing Git Submodules
-

Recall, a submodule is an independent repo within anothe git repo
and it might get updated by another user remotely, so you would want to
keep the local copy of your submodule up-to-date with the remote version. <br>

Assuming you already have a non-empty git submodule directory, then
to update it locally do (from the main repo containing the submodules):

```sh
$ git submodule update --recursive --remote <submodule> 
```


# Adding a New Git Submodule
-

If the user want to add a new github submodule, then from the main repo do:

```sh
$ git submodule add <remote_url>
``` 

NOTE: all the submodule contents will be added locally,
so there is no need to initialize submodule, however,
if you clone a repository with existing submodules
for the first time, then submodules will need to be initialized.
