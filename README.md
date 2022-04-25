# CaFe-Online
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


# Accessing Git Submodules for Starters
Assuming the user has a GitHub account and has not yet cloned the `CaFe-Online` repository, here are the initial steps to get started: <br>

`step 1: ` On any machine (local or remote) of the user choice: <br>

```sh
$ git clone https://github.com/Yero1990/CaFe-Online
$ cd CaFe-Online
```

At this point, the user will be able to various submodules (e.g., hallc_simulations, etc.) which are currently empty and will need to be initialized only ONCE on a given machine you are working on. <br>

`step 2: ` Initialize the submodule of interest 

```sh
$ git submodule update --init <submodule>
NOTE 1: to initialize all submodules at once, do not specify a <submodule>
$ cd <submodule>
$ git branch
NOTE 2: the initialized submodule(s) will be in a HEAD detached state
```

From NOTE 2 , HEAD in a detached state means you are not pointing to any particular branch, and changes can be made safely without impacting other branches. If you would like to keep the changes, then a branch would have to be created: `git checkout -b <branch_name>`, and any changes can be saved and push remotely from the new branch. 

`step 3:` If you plan to make significant contributions to the the official submodule in question, then do (from inside the submodule): <br>

```sh
$ git checkout -b <user_work_branch>
$ git add <files changed>
$ git commit -m "commit message"
$ git push origin user_work_branch
```
the submodule in question will then have a new branch remotely which can be merged onto the master branch by the repository maintainer.

# Updating Existing Git Submodules

Recall, a submodule is an independent repo within anothe git repo
and it might get updated by another user remotely, so you would want to
keep the local copy of your submodule up-to-date with the remote version. <br>

Assuming you already have a non-empty git submodule directory, then
to update it locally do (from the main repo containing the submodules):

```sh
$ git submodule update --recursive --remote <submodule> 
```

If in addition to the local update, the user would like to push the changes remotely to their version of the repository, then do: <br>

```sh
$ git add <submodule>
$ git commit -m "updated submodule commit message"
$ git push origin master 
```

# Adding a New Git Submodule
If the user want to add a new github submodule, then from the main repo do:

```sh
$ git submodule add <remote_url>
``` 

NOTE: all the submodule contents will be added locally,
so there is no need to initialize submodule, however,
if you clone a repository with existing submodules
for the first time, then submodules will need to be initialized.
