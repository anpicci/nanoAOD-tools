reset
#set folder = vUL035 #### aQGC added, new fakes, systematics completed
set folder = vUL040 #### same as UL035, but SF ele and met unclust sys

#######    2017   #######
set year = 'UL2017'
#reset
#python3 PrepareToPlot.py -f $folder -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d TTTo2L2Nu_UL2017,TVX_UL2017,Triboson_UL2017
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d Triboson_UL2018
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d TVX_UL2018,TTTo2L2Nu_UL2018,WpWpJJ_UL2018,WrongSign_UL2018 #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016   #######
set year = 'UL2016'
#reset
#python3 PrepareToPlot.py -f $folder -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d TTTo2L2Nu_UL2016,Triboson_UL2016,WrongSign_UL2016,WpWpJJ_UL2016 #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016APV   #######
set year = 'UL2016APV'
#reset
#python3 PrepareToPlot.py -f $folder -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d TTTo2L2Nu_UL2016APV,WrongSign_UL2016APV #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

set year = 'UL2016M'
#set year = 'ULRunII'
python3 PrepareToPlot.py -f $folder -y $year -d WpWpJJ_QCD_,WpWpJJ_EWK_
