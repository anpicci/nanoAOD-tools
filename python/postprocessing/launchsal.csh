reset
#set folder = vUL003
#set folder = vUL002 #### with loose bveto
set folder = vUL030 #### with loose bveto, new txt files, systematics
#set folder = vUL004

#######    2017   #######
set year = 'UL2017'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d TTTo2L2Nu_$year --rw
#python3 PrepareToPlot.py -f $folder -y $year -d TT_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#reset
python3 PrepareToPlot.py -f $folder -y $year -d VBS_SSWW_cW_$year --rw
#python3 PrepareToPlot.py -f $folder -y $year -d TT_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016   #######
set year = 'UL2016'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d TTTo2L2Nu_$year #--rw
#python3 PrepareToPlot.py -f $folder -y $year -d TT_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year
##python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year


#######    2016APV   #######
set year = 'UL2016APV'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d TTTo2L2Nu_$year --rw
#python3 PrepareToPlot.py -f $folder -y $year -d TT_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year
##python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

