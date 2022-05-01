# Intensive Study Plan for Noah Swan
## Description
This github repository is intended to be used for and by the graduate student (Noah Swan) to save the work (relevant computer codes / notes) on this project (CaFe). The main part of the study plan will consist of giving an introduction to: <br>
	
1. general (e,e'p) simulations using the (e,e'p) simulation package, `SIMC`, used in Jefferson Lab Hall A and C.  <br>
	
2. actual data replay using the Hall C `hallc_replay` repository, and familiarize with general analysis procedure followed by all Hall C experiments <br>

As a by-product of this study plan, Noah will also be familiarized with github used to organize and stored relevant codes/scripts in future work. Noah will also get familiarized with LaTeX, as he will write his final report of this study plan in said format. <br> 

**Specific Software Requirements** <br>
To successfully carry out this study plan, we will need to have installed the following: <br>

* GitHub (which is a web-based version-control and collaboratio platform for software developers)
	* `deut_simc` repository which contains the simulation source code SIMC 
	* `hallc_simulations` repository used for carrying out simulations
	* `cafe_online_replay` repository used to do data replay
	* `hcana` repository which is the Hall C source code (needed for data replay)
* Python programming language (preferably Python < 3.0, required by hcana to execute Scons compiler)
* LaTeX (which is a document preparation system to facilitate the writing of research and scientific papers) 
* ROOT CERN (object oriented programming designed for physics data analysis) <br>

NOTE: C++ should already be part of the system.
 
Reading Material: <br>
[SIMC Intro](https://hallcweb.jlab.org/DocDB/0008/000866/002/hallc_mc_overview_v2.pdf) by D. Gaskell <br>
[General Hall C 12 GeV Analysis Procedure](https://hallcweb.jlab.org/DocDB/0010/001032/001/analysis_notes.pdf) by C. Yero

## Overview of Tasks/Meetings and Timeline
Noah will be assigned several tasks on a weekly basis to be completed by the end of each week, and we'll meet at the start of the following week to discuss the progress made and new tasks to be completed. The entire study plan will last 10 weeks (can be flexible, depending on difficulty of tasks), after which Noah will have the necessary tools to be able to carry out and analyze the upcoming CaFe experiment in Hall C (Mid-August 2022) <br>

By the end of the program, Noah will provide **a 2-4 page report on what has been learned.** It is also encouraged to present a  10-20 informal talk on the topics covered during the study plan. This will help solidify what has been learned. <br>

> **We will meet on Mondays (flexible time) to discuss new tasks to be done during the week and Fridays (flexible time) to discuss work that has been done during that week.**

**In-Person Meeting Information:** <br>
Meeting Days:  Mondays @ 9:00 am <br>
Meeting Room: PSB 2100L <br>

Meeting Link (in case one of us can't attend in person): <br>
> 
> Join ZoomGov Meeting <br>
> [https://jlab-org.zoomgov.com/j/16178802265](https://jlab-org.zoomgov.com/j/16178802265)
> 
> Meeting ID: 161 7880 2265 <br>
> One tap mobile <br>
> +16692545252, 16178802265# US (San Jose) <br>
> +16468287666, 16178802265# US (New York)


`First Week` <br>

* discuss weekly meeting times 

* discuss the study plan, timeline and expectations

* Discuss current knowledge of student on C++, Python, GitHub and LaTeX

* install and setup (if not done already):
	*  ROOT, GitHub, Python and LaTeX if necessary <br> 
  ( see [root-installation](https://root.cern/install/), [github-installation](https://github.com/git-guides/install-git), [python-installation](https://www.wikihow.com/Install-Python#Mac) and [latex-installation](https://www.latex-project.org/get/) )

* clone (preferably fork+clone) the following GitHub repositories in any desired work space (and make sure they compile without errors):
	*  [https://github.com/Yero1990/deut_simc](https://github.com/Yero1990/deut_simc)
	*  [https://github.com/Yero1990/hallc_simulations](https://github.com/Yero1990/hallc_simulations)
	*  [https://github.com/JeffersonLab/hcana](https://github.com/JeffersonLab/hcana)
	*  [https://github.com/Yero1990/cafe\_online\_replay](https://github.com/Yero1990/cafe_online_replay)

	Alternatively, the student can fork+clone the repository: [https://github.com/Yero1990/CaFe-Online
](https://github.com/Yero1990/CaFe-Online) <br>
which contains the 4 above-mentioned repositories as git submodules (repositories within a repository) and follow the instructions of the README file. 


**First Week Tasks:** <br>

If installation proceeds smoothly, we will move on to attempting a simulation with a recent CaFe input file to get familiar with the process and will assign Noah to do a few simulations for the CaFe using different targets/kinematics, 
and familiarize with the relevant root leaf variables. Also, should begin writing a script that reads the SIMC output simulation file, loops over events and fills certain histograms needed for further analysis.

`Second Week` <br>

**Second Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week

* Noah will start writing code if not already started on previous week (with help from Carlos) for CaFe rate estimations using deuteron (SRC kinematics) and Carbon-12 (Mean-Field or MF kinematics). Although this code may have already been written previously, it is a good exercise to do as it will give a more comprehensive understanding of concepts such as beam charge, time, currents, yields, rates etc. 
as well as the idea of 'weighted' events, and many more finer technical details that could be easily missed if one does not explicitly write the code.


`Third Week` <br>

**Third Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* Noah will continue writing code for CaFe rate estimations.

`Fourth Week` <br>

**Fourth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* Noah is expected to almost be finishing up code, and preliminary rate
estimates should start to be calculated.
* rate estimates can be compared to those determined by Dien Thi Nguyen.

`Fifth Week` <br>

**Fifth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* Start to get familiarized with `hallc_replay` infrastructure (there are many technical details and this task is expected to extend beyond the study plan)
* Try to do a successful replay of existing data (you will need `hcana` to also be compiled)

`Sixth Week` <br>

**Sixth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* start to learn about setting reference times/detector time window cuts

`Seventh Week` <br>

**Seventh Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* start to learn how to run hodoscope calibration code

`Eigth Week` <br>

**Eigth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* start to learn how to run drift chambers calibration code

`Ninth Week` <br>

**Ninth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* start to learn how to run calorimeter calibration code

`Tenth Week` <br>

**Tenth Week Tasks:** <br>

* discuss/clarify any questions from work done on previous week.
* discuss preparation of final report in LaTeX format as well as a 10-20 min presentation of what has been learned.