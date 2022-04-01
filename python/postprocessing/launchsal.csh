reset
#set folder = vUL003
#set folder = vUL002 #### with loose bveto
set folder = vUL010 #### with loose bveto, new txt files, systematics
#set folder = vUL004

#######    2017   #######
set year = 'UL2017'
#python3 PrepareToPlot.py -f $folder -y $year
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#python3 PrepareToPlot.py -f $folder -y $year 
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year


#######    2016   #######
set year = 'UL2016'
#python3 PrepareToPlot.py -f $folder -y $year
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year


#######    2016APV   #######
set year = 'UL2016APV'
#python3 PrepareToPlot.py -f $folder -y $year
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year 
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

