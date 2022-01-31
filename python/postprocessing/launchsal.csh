reset
set folder = vUL003

#######    2016APV   #######
set year = 'UL2016APV'
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year --rw -d DataEle
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year -d Data

#######    2017   #######
set year = 'UL2017'
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year --rw -d DataMu
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year -d Data

#######    2016   #######
set year = 'UL2016'
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year --rw -d DataEle
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year

#######    2018   #######
set year = 'UL2018'
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year --rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year
