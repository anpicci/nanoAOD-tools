reset
#set folder = vUL003
#set folder = vUL002 #### with loose bveto
set folder = vUL007 #### with loose bveto, new txt files
#set folder = vUL004

#######    2016APV   #######
set year = 'UL2016APV'
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year --skipML #--rw # -d Data

#######    2016   #######
set year = 'UL2016'
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year --skipML #--rw #-d DYJetsToLL_FxFx

#######    2017   #######
set year = 'UL2017'
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw #-d DataMu
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year --skipML #--rw #-d DYJetsToLL_FxFx

#######    2018   #######
set year = 'UL2018'
python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year
#python3 PrepareToPlot.py -f $folder -y $year --skipML #--rw #-c
