reset
#set folder = vUL045 #### aQGC added, new fakes, systematics completed
set folder = vUL050 #### same as UL035, but SF ele and met unclust sys

#######    2017   #######
set year = 'UL2017'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d VBS_SSWW_SM_,VBS_SSWW_c
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --rw --or -d VBS_SSWW_SM_,VBS_SSWW_c
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016   #######
set year = 'UL2016'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --or --rw -d VBS_SSWW_SM_,VBS_SSWW_c
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016APV   #######
set year = 'UL2016APV'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --or --rw -d VBS_SSWW_SM_,VBS_SSWW_c
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#set year = 'UL2016M'
#python3 PrepareToPlot.py -f $folder -y $year --rw --or 
set year = 'ULRunII'
python3 PrepareToPlot.py -f $folder -y $year --rw --or -d WrongSign_


