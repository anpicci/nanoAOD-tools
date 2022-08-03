reset
set folder = vUL035 #### aQGC added, new fakes, systematics completed
#set folder = vUL040 #### same as UL035, but lepjet

#######    2017   #######
set year = 'UL2017'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --rw -v TT_,WJets_ -d VBS_SSWW_aQGC_ --or
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d VBS_SSWW_aQGC_
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --rw -v TT_,WJets_
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -c -d WpWpJJ_$year
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016   #######
set year = 'UL2016'
#reset
#python3 PrepareToPlot.py -f $folder -y $year --rw -v TT_,WJets_
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d ZZtoLep_$year,TTTo2L2Nu_$year,TVX_$year
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016APV   #######
set year = 'UL2016APV'
#reset
python3 PrepareToPlot.py -f $folder -y $year --rw -v TT_,WJets_ -d VBS_SSWW_aQGC_ --or
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -c -d DYJets
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

